#!/usr/bin/env python3
"""Stage and verify the narrowly scoped 2026-11-06 desktop pet fixes."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
from io import BytesIO
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

from PIL import Image, ImageChops, ImageDraw, ImageStat

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / 'work/release-compatibility-2026-11-06'
PRIOR = ROOT / 'work/motion-optimization-2026-11-06'
VALIDATOR = Path('/home/ubuntu23/.codex/skills/hatch-pet/scripts/validate_atlas.py')
HOLDS = [1680, 660, 660, 840, 840, 1920]
# Human-reviewed source-frame indices, not an automatic eye detector. Eye patches,
# hair occlusion, and sunglasses remain part of the original character design.
CLOSED = {
    'tartaglia': [2], 'venti': [], 'wanderer': [3], 'furina': [2, 3],
    'ganyu': [1], 'hu-tao': [2, 3], 'kazuha-chibi': [1], 'kaeya': [2],
    'kamisato-ayaka': [2], 'raiden-shogun': [2], 'xiao': [1],
    'yae-miko': [2], 'zhongli': [2], 'black-swan': [1, 4],
    'kafka': [1, 4], 'sparkle': [2], 'acheron': [2, 3],
    'aventurine': [0, 3, 5], 'blade': [2, 3],
    'dan-heng-imbibitor-lunae': [3], 'firefly': [2], 'jing-yuan': [2],
    'robin': [1, 4], 'ruan-mei': [1, 4], 'sunday': [3],
    'bronya-zaychik': [2], 'fu-hua': [2], 'kiana-kaslana': [1],
    'otto-apocalypse': [2], 'seele-vollerei': [2], 'theresa': [3],
    'kevin-kaslana': [2], 'raiden-mei': [2], 'raiden-mei-3d': [2],
    'burnice-white': [1, 4], 'lighter': [1, 3], 'vivian-banshee': [3],
    'von-lycaon': [3], 'zhu-yuan': [2], 'anby-demara': [1],
    'ellen-joe': [], 'miyabi': [2, 5], 'jane-doe': [2],
    'nicole-demara': [1, 4], 'kibutsuji-muzan': [2],
    'mitsuri-kanroji': [4], 'obanai': [2, 3],
}
APPROVED = {'xiao', 'dan-heng-imbibitor-lunae', 'jing-yuan'}
# Independent visual review found inherited hair truncation from equal-slot
# extraction. Recover this complete coherent source family separately.
EDGE_REPAIRS = {'raiden-mei-3d': [3, 4, 5]}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def tile(im, column, row=0):
    return im.crop((column * 192, row * 208, (column + 1) * 192, (row + 1) * 208))


def records():
    result = json.loads((RUN / 'inventory.json').read_text())
    assert set(CLOSED) == {r['id'] for r in result}
    return result


def stage_one(record):
    pet_id = record['id']
    original_path = RUN / 'originals' / pet_id / 'spritesheet.webp'
    original_bytes = original_path.read_bytes()
    assert digest(original_bytes) == record['spriteSha256']
    original = Image.open(original_path).convert('RGBA')
    frames = [tile(original, c) for c in range(6)]
    mapping = list(range(6))
    candidate = original.copy()
    reextraction = None
    if pet_id == 'raiden-mei-3d':
        recovered = RUN / 'mei-3d-reextraction'
        reextraction = json.loads((recovered / 'validation.json').read_text())
        assert reextraction['ok'] and reextraction['preservedNonIdleCells'] == 82
        assert digest((recovered / 'spritesheet.webp').read_bytes()) == reextraction['sha256']
        recovered_atlas = Image.open(recovered / 'spritesheet.webp').convert('RGBA')
        for c in range(6):
            candidate.paste(tile(recovered_atlas, c), (c * 192, 0))
        mapping = None
        method = 're-extract the complete original idle source; no new artwork'
    elif pet_id in APPROVED:
        approved_path = PRIOR / pet_id / 'final/spritesheet-idle-only.webp'
        approval = json.loads((PRIOR / pet_id / 'qa/idle-only-validation.json').read_text())
        assert approval['ok'] and approval['visualReview'] == 'pass'
        assert digest(approved_path.read_bytes()) == approval['sha256']
        approved = Image.open(approved_path).convert('RGBA')
        for c in range(6):
            candidate.paste(tile(approved, c), (c * 192, 0))
        method = 'previously reviewed six-frame idle artwork'
        mapping = None
    elif CLOSED[pet_id]:
        # Reassemble the existing, coherent idle family. No drawing, warping,
        # interpolation, new expressions, or cross-state/cross-character reuse.
        repair_columns = sorted(set(CLOSED[pet_id] + EDGE_REPAIRS.get(pet_id, [])))
        open_indices = [c for c in range(6) if c not in repair_columns]
        for c in repair_columns:
            def distance(other):
                difference = ImageChops.difference(frames[c], frames[other])
                return sum(ImageStat.Stat(difference).mean), abs(c - other), other
            mapping[c] = min(open_indices, key=distance)
            candidate.paste(frames[mapping[c]], (c * 192, 0))
        method = 'reuse this pet’s original open-eye idle frames'
    else:
        method = 'original artwork preserved; no prolonged visible blink'
    target = RUN / 'candidates' / pet_id
    target.mkdir(parents=True, exist_ok=True)
    output = target / 'spritesheet.webp'
    if CLOSED[pet_id]:
        candidate.save(output, lossless=True, quality=100, method=6, exact=True)
    else:
        output.write_bytes(original_bytes)
    restored = Image.open(output).convert('RGBA')
    changed = []
    for row in range(11):
        for c in range(8):
            different = tile(original, c, row).tobytes() != tile(restored, c, row).tobytes()
            if different:
                assert row == 0 and c < 6, (pet_id, row, c)
                changed.append([row, c])
    unique = len({tile(restored, c).tobytes() for c in range(6)})
    assert unique >= 3, (pet_id, 'idle variation lost', unique)
    manifest_bytes = (RUN / 'originals' / pet_id / 'pet.json').read_bytes()
    (target / 'pet.json').write_bytes(manifest_bytes)
    manifest = json.loads(manifest_bytes)
    assert manifest['spriteVersionNumber'] == 2
    assert manifest['spritesheetPath'] == 'spritesheet.webp'
    with zipfile.ZipFile(ROOT / record['zip']) as archive:
        readmes = [n for n in archive.namelist() if Path(n).name == 'README.md']
        readme = archive.read(readmes[0]).decode('utf-8') if readmes else f'# {record["name"]}\n'
    readme = readme.split('\n<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->')[0].rstrip()
    explanation = ('待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。'
                   if changed else '待机未发现长时间闭眼问题，保留原图。')
    if pet_id in EDGE_REPAIRS:
        explanation += '同时从完整原始条带重新提取待机，修正旧提取过程造成的头发截断。'
    readme += f'''

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/{pet_id}/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\\.codex\\pets\\{pet_id}\\`；自定义 `CODEX_HOME` 时使用其 `pets/{pet_id}/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/{pet_id}/`
(default `~/.codex/pets/{pet_id}/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

{explanation}其余动作、neutral 和 16 个观察方向保持原版；ID 和 v2 格式不变。
The idle frames account for the desktop client's slow idle playback. Other states,
the neutral frame, all 16 look directions, the ID, and the v2 contract are preserved.
'''
    (target / 'README.md').write_text(readme)
    validation_path = RUN / 'validation' / f'{pet_id}.json'
    validation_path.parent.mkdir(exist_ok=True)
    result = subprocess.run([sys.executable, str(VALIDATOR), str(output), '--require-v2',
                             '--json-out', str(validation_path)], capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(f'{pet_id}: {result.stdout}\n{result.stderr}')
    validation = json.loads(validation_path.read_text())
    assert validation['ok']
    return {**record, 'method': method, 'sourceFrameMapping': mapping,
            'sourceBlinkColumns': CLOSED[pet_id], 'originalBlinkHoldMs': sum(HOLDS[c] for c in CLOSED[pet_id]),
            'sourceEdgeRepairColumns': EDGE_REPAIRS.get(pet_id, []),
            'sourceReextraction': reextraction,
            'changedCells': changed, 'preservedCells': 88 - len(changed),
            'preservedNonIdleCells': 82, 'idleUniqueFrames': unique,
            'afterSpriteSha256': digest(output.read_bytes()), 'atlasValidation': True,
            'manifestUnchanged': True, 'visualReview': 'pending'}


def stage(only=None):
    inventory = records()
    selected = [r for r in inventory if only is None or r['id'] in only]
    assert selected and (only is None or set(only) == {r['id'] for r in selected})
    with ThreadPoolExecutor(max_workers=3) as pool:
        refreshed = {r['id']: r for r in pool.map(stage_one, selected)}
    if only is None:
        result = [refreshed[r['id']] for r in inventory]
    else:
        previous = json.loads((RUN / 'staged-review.json').read_text())
        result = [refreshed.get(r['id'], r) for r in previous]
    for start in range(0, len(result), 6):
        subset = result[start:start + 6]
        sheet = Image.new('RGB', (1270, len(subset) * 248), '#e9e9e4')
        draw = ImageDraw.Draw(sheet)
        for r, record in enumerate(subset):
            im = Image.open(RUN / 'candidates' / record['id'] / 'spritesheet.webp').convert('RGBA')
            y = r * 248
            draw.text((12, y + 7), f'{start+r+1:02} {record["id"]} | {record["method"]}', fill='#152b29')
            for c in range(6):
                frame = tile(im, c)
                sheet.paste(frame, (100 + c * 192, y + 30), frame)
                draw.text((100 + c * 192, y + 16), f'{c}: {HOLDS[c]}ms', fill='#152b29')
        sheet.save(RUN / f'idle-after-{start//6+1:02}.png')
    (RUN / 'staged-review.json').write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps({'staged': len(result), 'changedIdle': sum(bool(r['changedCells']) for r in result),
                      'reusedOwnFrames': sum(r['sourceFrameMapping'] is not None and bool(r['changedCells']) for r in result),
                      'allNonIdleCellsPreserved': True}, ensure_ascii=False))


def apply():
    approval = json.loads((RUN / 'visual-review.json').read_text())
    assert approval['visual_qa'] == 'pass', 'Independent visual QA must pass before applying.'
    staged = json.loads((RUN / 'staged-review.json').read_text())
    assert set(approval['reviewedIds']) == {r['id'] for r in staged}
    applied = []
    for record in staged:
        pet_id = record['id']
        source = RUN / 'candidates' / pet_id
        assert digest((source / 'spritesheet.webp').read_bytes()) == record['afterSpriteSha256']
        assert approval['candidateSha256'][pet_id] == record['afterSpriteSha256']
        archive_path = ROOT / record['zip']
        assert digest(archive_path.read_bytes()) == record['zipSha256'], f'{pet_id}: release changed since audit'
        loose = ROOT / record['loose'] if record['loose'] else archive_path.parent / 'sunday-2d'
        loose.mkdir(exist_ok=True)
        for filename in ['pet.json', 'spritesheet.webp', 'README.md']:
            (loose / filename).write_bytes((source / filename).read_bytes())
        # Fixed metadata makes a rerun reproducible; never include work or references.
        with zipfile.ZipFile(archive_path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
            for filename in ['pet.json', 'spritesheet.webp', 'README.md']:
                info = zipfile.ZipInfo(filename, date_time=(2026, 11, 6, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, (source / filename).read_bytes())
        with tempfile.TemporaryDirectory() as temp:
            dest = Path(temp) / 'pets' / pet_id
            with zipfile.ZipFile(archive_path) as archive:
                assert archive.namelist() == ['pet.json', 'spritesheet.webp', 'README.md']
                assert archive.testzip() is None
                archive.extractall(dest)
            assert (dest / 'pet.json').read_bytes() == (loose / 'pet.json').read_bytes()
            assert (dest / 'spritesheet.webp').read_bytes() == (loose / 'spritesheet.webp').read_bytes()
        applied.append({**record, 'loose': str(loose.relative_to(ROOT)), 'visualReview': 'pass',
                        'zipFlatRoot': True, 'extractionTest': True,
                        'afterZipSha256': digest(archive_path.read_bytes())})
    checksum_files = []
    for group in ['genshin-impact', 'honkai-star-rail', 'honkai-impact-3rd', 'zenless-zone-zero', 'others']:
        for pattern in ['SHA256SUMS.txt', 'CHECKSUMS.sha256']:
            for path in (ROOT / group).rglob(pattern):
                entries = []
                for line in path.read_text().splitlines():
                    if not line.strip():
                        continue
                    _, name = line.split(maxsplit=1)
                    name = name.lstrip('*')
                    target = path.parent / name
                    assert target.is_file(), target
                    entries.append(f'{digest(target.read_bytes())}  {name}')
                path.write_text('\n'.join(entries) + '\n')
                checksum_files.append(str(path.relative_to(ROOT)))
    report = {'ok': True, 'totalVersions': len(applied), 'idleChangedVersions': sum(bool(r['changedCells']) for r in applied),
              'repackedVersions': len(applied), 'fixedWrappedArchives': sum(r['prefix'] != '.' for r in applied),
              'preservedNonIdleCellsPerVersion': 82, 'updatedChecksumFiles': checksum_files,
              'installedIntoUserDirectory': False, 'gitCommitOrPush': False, 'pets': applied}
    (RUN / 'release-validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2))
    out = ROOT / 'output/release-compatibility-report.json'
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    print(json.dumps({k: v for k, v in report.items() if k != 'pets'}, ensure_ascii=False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--only', help='Restage selected comma-separated IDs after a focused repair.')
    args = parser.parse_args()
    apply() if args.apply else stage(args.only.split(',') if args.only else None)

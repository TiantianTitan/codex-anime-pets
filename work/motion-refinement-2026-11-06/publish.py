"""Apply hash-bound approved rows, rebuild matching ZIPs, verify all 48 editions."""
import hashlib
from io import BytesIO
import json
from pathlib import Path
import subprocess
import zipfile
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
RUN = Path(__file__).resolve().parent
NAMES = {'running-right':'向右跑动','running-left':'向左跑动','jumping':'跳跃','failed':'失败反馈',
         'waiting':'等待输入','running':'工作中'}

def sha(data):
    return hashlib.sha256(data).hexdigest()

def main():
    inventory = json.loads((RUN / 'inventory.json').read_text())
    candidates = json.loads((RUN / 'candidates.json').read_text())
    technical = json.loads((RUN / 'technical-validation.json').read_text())
    assert technical['ok'], 'Technical checks incomplete'
    assert technical['candidate_manifest_sha256'] == sha((RUN / 'candidates.json').read_bytes()), 'Stale technical approval'
    assert technical['inventory_sha256'] == sha((RUN / 'inventory.json').read_bytes()), 'Stale inventory approval'
    assert technical['script_sha256'] == sha((RUN / 'validate_candidates.py').read_bytes()), 'Stale validation script'
    approvals = {}
    for name in ('qa-independent-a.json', 'qa-independent-b.json'):
        report = json.loads((RUN / name).read_text())
        for row in report['rows']:
            key = row['id'], row['state']
            assert key not in approvals, key
            approvals[key] = row
    by_id = {p['id']:p for p in inventory['editions']}
    changed = {p['id']:p for p in candidates['editions']}
    archives = {}
    for p in inventory['editions']:
        folder = (ROOT / p['atlas']).parent
        matches = []
        for archive_path in folder.parent.glob('*.zip'):
            with zipfile.ZipFile(archive_path) as z:
                if 'pet.json' in z.namelist() and json.loads(z.read('pet.json'))['id'] == p['id']:
                    assert set(z.namelist()) == {'pet.json','spritesheet.webp','README.md'}
                    assert z.testzip() is None
                    assert all(z.read(name) == (folder / name).read_bytes() for name in z.namelist())
                    matches.append(archive_path)
        assert len(matches) == 1, (p['id'], matches)
        archives[p['id']] = matches[0]
    # Verify all approvals and all baselines before the first release mutation.
    for p in inventory['editions']:
        assert sha((ROOT / p['atlas']).read_bytes()) == p['sha256']
    for p in candidates['editions']:
        assert sha((ROOT / p['atlas']).read_bytes()) == p['sha256']
        for row in p['rows']:
            q = approvals[p['id'],row['state']]
            assert q['verdict'] == 'pass', (p['id'], row['state'], q['verdict'])
            assert q['atlas_sha256'] == p['sha256']
            assert q['strip_sha256'] == row['sha256'] == sha((ROOT / row['strip']).read_bytes())
    published = []
    for p in candidates['editions']:
        original = by_id[p['id']]
        atlas = ROOT / original['atlas']
        folder = atlas.parent
        archive_path = archives[p['id']]
        assert archive_path.exists(), archive_path
        old_zip_hash = sha(archive_path.read_bytes())
        manifest_bytes = (folder / 'pet.json').read_bytes()
        readme_path = folder / 'README.md'
        readme = readme_path.read_text()
        readme = readme.replace('其余动作、neutral 和 16 个观察方向保持原版；ID 和 v2 格式不变。',
                                '该段记录此前的待机修复；后续动作调整见下节。')
        readme = readme.replace('Other states,\nthe neutral frame, all 16 look directions, the ID, and the v2 contract are preserved.',
                                'The later motion changes are recorded below.')
        states = '、'.join(NAMES[r['state']] for r in p['rows'])
        english = ', '.join(r['state'] for r in p['rows'])
        readme += f'\n\n<!-- MOTION-REFINEMENT-2026-11-06 -->\n## 动作优化 / Motion refinement · 2026-11-06\n\n调整动作：{states}。保持原帧数与客户端时序，改善配准、动作衔接或原图中的明显断裂。\n本次未修改待机、neutral、16 个观察方向与宠物 ID。\n\nUpdated states: {english}. Frame counts and client timing are unchanged.\nIdle, the neutral cell, all 16 look directions, and the pet ID are unchanged in this update.\n'
        atlas.write_bytes((ROOT / p['atlas']).read_bytes())
        readme_path.write_text(readme)
        with zipfile.ZipFile(archive_path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
            for name in ('pet.json','spritesheet.webp','README.md'):
                info = zipfile.ZipInfo(name, date_time=(2026,11,6,0,0,0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                z.writestr(info,(folder/name).read_bytes())
        assert (folder / 'pet.json').read_bytes() == manifest_bytes
        published.append({'id':p['id'],'atlas':original['atlas'],'sha256':p['sha256'],
                          'archive':str(archive_path.relative_to(ROOT)),'before_archive_sha256':old_zip_hash,
                          'archive_sha256':sha(archive_path.read_bytes()),'changed_states':[r['state'] for r in p['rows']]})
    checksum_files = []
    for group in ('genshin-impact','honkai-star-rail','honkai-impact-3rd','zenless-zone-zero','others'):
        for pattern in ('SHA256SUMS.txt','CHECKSUMS.sha256'):
            for path in (ROOT/group).rglob(pattern):
                lines = []
                for line in path.read_text().splitlines():
                    if not line.strip(): continue
                    _, name = line.split(maxsplit=1)
                    name = name.lstrip('*')
                    lines.append(sha((path.parent/name).read_bytes()) + '  ' + name)
                content = '\n'.join(lines) + '\n'
                if content != path.read_text():
                    path.write_text(content)
                    checksum_files.append(str(path.relative_to(ROOT)))
    coverage = []
    for p in inventory['editions']:
        path = ROOT / p['atlas']
        atlas = Image.open(path).convert('RGBA')
        assert atlas.size == (1536,2288)
        before_bytes = subprocess.check_output(['git','show',inventory['baseline_commit']+':'+p['atlas']],cwd=ROOT)
        before = Image.open(BytesIO(before_bytes)).convert('RGBA')
        declared = {r['row']:r['count'] for r in changed.get(p['id'],{}).get('rows',[])}
        actual = []
        for y in range(11):
            for x in range(8):
                box = (x*192,y*208,(x+1)*192,(y+1)*208)
                if atlas.crop(box).tobytes() != before.crop(box).tobytes():
                    assert y in declared and x < declared[y], (p['id'],y,x)
                    actual.append([y,x])
        manifest_bytes = (ROOT/p['manifest']).read_bytes()
        assert manifest_bytes == subprocess.check_output(['git','show',inventory['baseline_commit']+':'+p['manifest']],cwd=ROOT)
        archive_path = archives[p['id']]
        with zipfile.ZipFile(archive_path) as z:
            assert set(z.namelist()) == {'pet.json','spritesheet.webp','README.md'}
            assert z.testzip() is None
            for name in z.namelist():
                assert z.read(name) == (path.parent/name).read_bytes(), (p['id'],name)
        if not declared:
            assert sha(path.read_bytes()) == p['sha256']
        coverage.append({'id':p['id'],'atlas':p['atlas'],'sha256':sha(path.read_bytes()),
                         'baseline_sha256':p['sha256'],'changed_rows':sorted(declared),'changed_cells':actual,
                         'strictly_preserved_cells':88-len(actual),'manifest_unchanged':True,'zip_matches_loose_files':True})
    report = {'ok':True,'baseline_commit':inventory['baseline_commit'],'client_version':inventory['client_version'],
              'editions_checked':len(coverage),'actions_checked':len(coverage)*9,
              'editions_changed':len(published),'rows_changed':candidates['changed_rows'],
              'idle_neutral_look_cells_unchanged':True,'installed':False,'committed_or_pushed':False,
              'checksum_files_updated':checksum_files,'published':published,'coverage':coverage}
    (RUN/'release-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    (ROOT/'docs/pet-motion-refinement-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('published','coverage')},ensure_ascii=False))

if __name__ == '__main__':
    main()

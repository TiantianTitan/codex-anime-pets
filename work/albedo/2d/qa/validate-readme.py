"""Validate Albedo's localized README integration and final-atlas provenance."""

import hashlib
from html import unescape
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[4]
QA = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "scripts"))
import build_readme_showcase as showcase


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def animation(path):
    image = Image.open(path)
    frames = []
    elapsed = 0
    for index in range(image.n_frames):
        image.seek(index)
        frame = image.convert("RGBA")
        elapsed += image.info.get("duration", 0)
        frames.append((elapsed, frame))
    return frames


errors = []
readmes = []
for filename in ("README.md", "README.fr.md", "README.zh-CN.md", "README.ja.md"):
    content = (ROOT / filename).read_text()
    references = re.findall(r'(?:href|src)="([^"]+)"', content)
    references += re.findall(r'\]\(([^\s)]+)\)', content)
    anchors = set(re.findall(r'(?:id|name)="([^"]+)"', content))
    for heading in re.findall(r'^#{1,6}\s+(.+)$', content, re.M):
        anchors.add(re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-'))
    local_count = 0
    for reference in references:
        url = urlsplit(unescape(reference))
        if url.scheme or url.netloc:
            continue
        local_count += 1
        if url.path and not (ROOT / unquote(url.path)).exists():
            errors.append(f"{filename}: missing local link {reference}")
        if not url.path and url.fragment and unquote(url.fragment) not in anchors:
            errors.append(f"{filename}: missing anchor {reference}")
        if '/reference' in url.path:
            errors.append(f"{filename}: private reference linked: {reference}")

    archive_count = len(re.findall(r'<a id="character-\d\d-[^"]+"', content))
    assert archive_count == (0 if filename == "README.ja.md" else 49), filename
    assert len(re.findall(r'^\| .*?\| .*?\| `[^`]+` \| .*?\.zip\)', content, re.M)) == 50, filename
    genshin = re.search(r'<a id="downloads-genshin-impact"></a>\s*<details>(.*?)</details>', content, re.S).group(1)
    assert len(re.findall(r'^\| .*?`[^`]+`', genshin, re.M)) == 14, filename
    assert genshin.index('`wanderer`') < genshin.index('`albedo`'), filename
    assert content.count('?v=49') == 2 and '?v=48' not in content, filename
    assert content.count('assets/readme/idle/albedo.webp') == 1, filename
    assert content.count('<details open>') == (0 if filename == "README.ja.md" else 1), filename
    assert re.findall(r'<sub>(\d+)</sub>', content) == [f'{number:02d}' for number in range(1, 50)], filename

    latest_end = content.index('assets/readme/next-companion.svg')
    latest_table = content[content.rfind('<table', 0, latest_end):content.index('</table>', latest_end)]
    rows = re.findall(r'<tr>(.*?)</tr>', latest_table, re.S)
    assert len(rows) == 2 and len(re.findall(r'<td\b', rows[0])) == 3, filename
    assert re.findall(r'<sub>(\d+)</sub>', rows[0]) == ['46', '47', '48'], filename
    assert re.findall(r'<sub>(\d+)</sub>', rows[1]) == ['49'], filename
    assert 'width="33%"' in rows[1] and 'colspan="2"' in rows[1], filename
    assert 'assets/readme/next-companion.svg' in rows[1], filename
    # New releases do not rewrite the factual counts of an earlier audit batch.
    batch = next(line for line in content.splitlines() if line.startswith((
        '2026-11-06 batch:', 'Lot du 2026-11-06', '2026-11-06 批次', '2026-11-06の一括確認')))
    assert '47' in batch and '45' in batch, filename
    readmes.append({"file": filename, "checked_local_links": local_count,
                    "characters": 49, "editions": 50, "archive_entries": archive_count,
                    "genshin_packages": 14, "gallery_three_column_grid": True,
                    "next_entry_retained": True, "historical_batch_unchanged": True})

assert len(showcase.ARCHIVE_SOURCES) == 50
assert showcase.archive_number_labels()[-3:] == ['47', '48', '49']
assert [slug for slug, _ in showcase.ARCHIVE_SOURCES[-3:]] == ['kallen-kaslana', 'jingliu', 'albedo']
assert showcase.universe_for_slug('albedo') == 'genshin'
assert showcase.archive_number_labels()[4:6] == ['05A', '05B']

assets = []
before = json.loads((QA / 'readme-dynamic-assets-before.json').read_text())
for locale in showcase.LOCALES:
    arrivals = ROOT / 'assets/readme' / showcase.localized_asset_name('new-arrivals-stage.webp', locale)
    wall = ROOT / 'assets/readme' / showcase.localized_asset_name('character-collection-wall.webp', locale)
    timeline = animation(arrivals)
    assert timeline[-1][0] == 6600 and len(timeline) > 1
    assert timeline[0][1].size == (1200, 330)
    assert Image.open(wall).size == (1200, 1975)
    for path in (arrivals, wall):
        assert sha(path) != before[path.relative_to(ROOT).as_posix()], path
    assets.append({"locale": locale, "arrival_names": showcase.LOCALES[locale]['arrival_names'],
                   "arrivals_sha256": sha(arrivals), "wall_sha256": sha(wall),
                   "arrival_duration_ms": timeline[-1][0], "arrival_frames": len(timeline),
                   "wall_size": list(Image.open(wall).size)})

idle_path = ROOT / 'assets/readme/idle/albedo.webp'
assert sha(idle_path) == sha(QA / 'previews-final/idle.webp')
atlas_path = ROOT / 'genshin-impact/Albedo/albedo-2d/spritesheet.webp'
assert sha(atlas_path) == '590421dbef7d966819fc5c6cebf8466eb46d7c68e80e097e76bf324d77e7d02d'
assert sha(atlas_path) == json.loads((QA / 'preview-validation.json').read_text())['source_sha256']
atlas = Image.open(atlas_path).convert('RGBA')
timeline = animation(idle_path)
assert timeline[-1][0] == 6600
elapsed = 0
for col, hold in enumerate((1680, 660, 660, 840, 840, 1920)):
    frame = atlas.crop((col * 192, 0, (col + 1) * 192, 208))
    decoded = next(image for end, image in timeline if elapsed + hold / 2 < end)
    assert frame.getchannel('A').tobytes() == decoded.getchannel('A').tobytes()
    mask = frame.getchannel('A').point(lambda value: 255 if value else 0)
    assert all(not ImageChops.multiply(channel, mask).getbbox()
               for channel in ImageChops.difference(frame, decoded).split())
    elapsed += hold

card_path = ROOT / 'assets/readme/archive-previews/albedo.webp'
assert Image.open(card_path).size == (220, 240)
assert animation(card_path)[-1][0] == 6600
protected = json.loads((QA / 'readme-protected-assets.json').read_text())
assert all(sha(ROOT / path) == expected for path, expected in protected.items())

zip_path = ROOT / 'genshin-impact/Albedo/albedo-2d-codex-pet-v2.zip'
assert sha(zip_path) == 'b73d8352d2fa4f81fa0c330b25f1bfd7d640ec580d65b6601cc5884ba4d3b2f0'
with ZipFile(zip_path) as package:
    assert package.testzip() is None
    assert set(package.namelist()) == {'pet.json', 'spritesheet.webp', 'README.md'}
    assert all(package.read(name) == (atlas_path.parent / name).read_bytes() for name in package.namelist())

report = {"ok": not errors, "errors": errors, "readmes": readmes, "assets": assets,
          "total_checked_local_links": sum(item['checked_local_links'] for item in readmes),
          "protected_existing_assets_unchanged": len(protected),
          "idle_final_atlas_pixel_check": True, "archive_card_size": [220, 240],
          "silhouette_height": 198, "baseline": 220,
          "product_and_zip_unchanged": True, "background_only": True,
          "browser_scope": "Separate headless local Markdown approximation, not a live GitHub render"}
(QA / 'readme-validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(report, ensure_ascii=False, indent=2))
if errors:
    raise SystemExit(1)

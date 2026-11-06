"""Validate Jingliu's localized README update without opening UI windows."""
import hashlib
import importlib.util
import json
import re
from html import unescape
from pathlib import Path
from urllib.parse import unquote, urlsplit

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[4]
QA = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("showcase", ROOT / "scripts/build_readme_showcase.py")
showcase = importlib.util.module_from_spec(spec)
import sys
sys.modules[spec.name] = showcase
spec.loader.exec_module(showcase)


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
    archive_count = len(re.findall(r'<a id="character-\d\d-[^"]+"', content))
    assert archive_count == (0 if filename == "README.ja.md" else 48), filename
    assert len(re.findall(r'^\| .*?\| .*?\| `[^`]+` \| .*?\.zip\)', content, re.M)) == 49, filename
    star = re.search(r'<a id="downloads-honkai-star-rail"></a>\s*<details>(.*?)</details>', content, re.S).group(1)
    assert 'open' not in star.split('>', 1)[0], filename
    assert len(re.findall(r'^\| .*?`[^`]+`', star, re.M)) == 13, filename
    assert star.index('`black-swan`') < star.index('`jingliu`'), filename
    assert '?v=47' not in content, filename
    assert content.count('?v=48') == 2, filename
    assert 'assets/readme/next-companion.svg' in content, filename
    # Preserve the old batch's factual count rather than rewriting history.
    batch = next(line for line in content.splitlines() if line.startswith(('2026-11-06 batch:', 'Lot du 2026-11-06', '2026-11-06 批次', '2026-11-06の一括確認')))
    assert '47' in batch and '45' in batch, filename
    assert content.count('<details open>') == (0 if filename == 'README.ja.md' else 1), filename
    gallery_end = content.index('assets/readme/next-companion.svg')
    latest_table = content[content.rfind('<table', 0, gallery_end):content.index('</table>', gallery_end)]
    rows = re.findall(r'<tr>(.*?)</tr>', latest_table, re.S)
    assert len(rows) == 2 and len(re.findall(r'<td\b', rows[0])) == 3, filename
    assert re.findall(r'<sub>(\d+)</sub>', rows[0]) == ['46', '47', '48'], filename
    assert 'colspan="3"' in rows[1], filename
    readmes.append({"file": filename, "checked_local_links": local_count,
                    "characters": 48, "editions": 49, "archive_entries": archive_count,
                    "star_rail_packages": 13, "latest_gallery_row": [46, 47, 48],
                    "next_entry_retained": True, "historical_batch_unchanged": True})

assert len(showcase.ARCHIVE_SOURCES) == 49
assert showcase.archive_number_labels()[-3:] == ['46', '47', '48']
assert [slug for slug, _ in showcase.ARCHIVE_SOURCES[-3:]] == ['wanderer', 'kallen-kaslana', 'jingliu']
assert showcase.universe_for_slug('jingliu') == 'star-rail'
assert showcase.archive_number_labels()[4:6] == ['05A', '05B']

assets = []
for locale in showcase.LOCALES:
    arrivals = ROOT / 'assets/readme' / showcase.localized_asset_name('new-arrivals-stage.webp', locale)
    wall = ROOT / 'assets/readme' / showcase.localized_asset_name('character-collection-wall.webp', locale)
    timeline = animation(arrivals)
    assert timeline[-1][0] == 6600 and len(timeline) > 1
    assert timeline[0][1].size == (1200, 330)
    assert Image.open(wall).size == (1200, 1975)
    assets.append({"locale": locale, "arrival_names": showcase.LOCALES[locale]['arrival_names'],
                   "arrivals_sha256": sha(arrivals), "wall_sha256": sha(wall),
                   "arrival_duration_ms": timeline[-1][0], "arrival_frames": len(timeline),
                   "wall_size": list(Image.open(wall).size)})

idle_path = ROOT / 'assets/readme/idle/jingliu.webp'
assert sha(idle_path) == sha(QA / 'previews-final/idle.webp')
atlas_path = ROOT / 'honkai-star-rail/Jingliu/jingliu-2d/spritesheet.webp'
atlas = Image.open(atlas_path).convert('RGBA')
assert sha(atlas_path) == json.loads((QA / 'final-visual-review.json').read_text())['atlas_sha256']
timeline = animation(idle_path)
assert timeline[-1][0] == 6600
elapsed = 0
for col, hold in enumerate((1680, 660, 660, 840, 840, 1920)):
    frame = atlas.crop((col * 192, 0, (col + 1) * 192, 208))
    decoded = next(image for end, image in timeline if elapsed + hold / 2 < end)
    assert frame.getchannel('A').tobytes() == decoded.getchannel('A').tobytes()
    mask = frame.getchannel('A').point(lambda value: 255 if value else 0)
    assert all(not ImageChops.multiply(channel, mask).getbbox() for channel in ImageChops.difference(frame, decoded).split())
    elapsed += hold

card_path = ROOT / 'assets/readme/archive-previews/jingliu.webp'
assert Image.open(card_path).size == (220, 240)
assert animation(card_path)[-1][0] == 6600
protected = json.loads((QA / 'readme-protected-assets.json').read_text())
assert all(sha(ROOT / path) == expected for path, expected in protected.items())
report = {"ok": not errors, "errors": errors, "readmes": readmes, "assets": assets,
          "total_checked_local_links": sum(item['checked_local_links'] for item in readmes),
          "protected_existing_assets_unchanged": len(protected),
          "idle_final_atlas_pixel_check": True, "archive_card_size": [220, 240],
          "silhouette_height": 198, "baseline": 220, "background_only": True,
          "browser_scope": "Separate headless local Markdown approximation, not a live GitHub render"}
(QA / 'readme-validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(report, ensure_ascii=False, indent=2))
if errors:
    raise SystemExit(1)

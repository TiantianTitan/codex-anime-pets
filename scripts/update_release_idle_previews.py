#!/usr/bin/env python3
"""Sync README idle previews with verified public atlases at native idle timing."""
import ast
import json
from pathlib import Path
from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
HOLDS = [1680, 660, 660, 840, 840, 1920]
report = json.loads((ROOT / 'output/release-compatibility-report.json').read_text())
assert report['ok'] and all(p['visualReview'] == 'pass' for p in report['pets'])
records = {p['id']: p for p in report['pets']}
builder = ROOT / 'scripts/build_readme_showcase.py'
source = builder.read_text()
assignment = next(n for n in ast.parse(source).body if isinstance(n, ast.Assign)
                  and any(isinstance(t, ast.Name) and t.id == 'ARCHIVE_SOURCES' for t in n.targets))
archive_sources = ast.literal_eval(assignment.value)
aliases = {'raiden-mei-2d': 'raiden-mei', 'kaedehara-kazuha': 'kazuha-chibi', 'hoshimi-miyabi': 'miyabi'}
replacements = {}
out = ROOT / 'assets/readme/idle'
out.mkdir(exist_ok=True)
for slug, old in archive_sources:
    pet_id = aliases.get(slug, slug)
    record = records[pet_id]
    atlas = Image.open(ROOT / record['loose'] / 'spritesheet.webp').convert('RGBA')
    frames = [atlas.crop((c * 192, 0, (c + 1) * 192, 208)) for c in range(6)]
    relative = f'assets/readme/idle/{slug}.webp'
    frames[0].save(ROOT / relative, format='WEBP', save_all=True, append_images=frames[1:],
                   duration=HOLDS, loop=0, lossless=True, quality=100, method=4, exact=True)
    # Animated WebP may coalesce identical adjacent frames. Verify timeline
    # pixels at each native frame's midpoint rather than asserting frame count.
    preview = Image.open(ROOT / relative)
    decoded = []
    end = 0
    for i in range(preview.n_frames):
        preview.seek(i)
        im = preview.convert('RGBA')
        end += preview.info['duration']
        decoded.append((end, im))
    assert end == 6600, (pet_id, end)
    elapsed = 0
    for frame, hold in zip(frames, HOLDS):
        sample = elapsed + hold / 2
        expected = next(im for end, im in decoded if sample < end)
        # Animated WebP clears hidden RGB where alpha is zero. Verify every
        # visible RGBA pixel and the complete alpha channel exactly.
        assert expected.getchannel('A').tobytes() == frame.getchannel('A').tobytes(), (pet_id, sample, 'alpha')
        difference = ImageChops.difference(expected, frame)
        visible = frame.getchannel('A').point(lambda a: 255 if a else 0)
        assert all(not ImageChops.multiply(channel, visible).getbbox() for channel in difference.split()), (pet_id, sample, 'visible RGBA')
        elapsed += hold
    replacements[old] = relative
for path in [ROOT / name for name in ['README.md', 'README.zh-CN.md', 'README.fr.md', 'README.ja.md']] + [builder]:
    text = path.read_text()
    for old, new in replacements.items():
        text = text.replace(old, new)
    path.write_text(text)
print(json.dumps({'previews': len(archive_sources), 'durationMs': 6600, 'losslessPixelCheck': True}))

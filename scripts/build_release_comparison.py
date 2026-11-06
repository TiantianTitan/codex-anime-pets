#!/usr/bin/env python3
"""Build an offline idle comparison for every audited release, without full atlases."""
import base64
from io import BytesIO
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / 'work/release-compatibility-2026-11-06'


def strip_uri(path):
    im = Image.open(path).convert('RGBA').crop((0, 0, 1152, 208))
    buffer = BytesIO()
    im.save(buffer, format='WEBP', lossless=True, quality=100, method=4, exact=True)
    return 'data:image/webp;base64,' + base64.b64encode(buffer.getvalue()).decode()


pets = []
for record in json.loads((RUN / 'staged-review.json').read_text()):
    before = strip_uri(RUN / 'originals' / record['id'] / 'spritesheet.webp')
    after = strip_uri(RUN / 'candidates' / record['id'] / 'spritesheet.webp') if record['changedCells'] else None
    pets.append({
        'id': record['id'], 'name': record['name'], 'group': record['group'],
        'before': before, 'after': after, 'changed': bool(record['changedCells']),
        'blinkColumns': record['sourceBlinkColumns'], 'blinkMs': record['originalBlinkHoldMs'],
        'reused': record['sourceFrameMapping'] is not None,
        'reextracted': bool(record.get('sourceReextraction')), 'zip': record['zip'],
    })
template = (ROOT / 'scripts/motion-review/releases.template.html').read_text()
template = template.replace('/* RELEASE_DATA */', json.dumps(pets, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/'))
output = ROOT / 'output/pet-release-comparison.html'
output.parent.mkdir(exist_ok=True)
output.write_text(template)
print(json.dumps({'html': str(output), 'versions': len(pets), 'bytes': output.stat().st_size}))

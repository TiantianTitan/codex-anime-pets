"""Assemble reviewed, same-state whole frames; never draw or warp artwork."""
import hashlib
import json
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[2]
RUN = Path(__file__).resolve().parent
INVENTORY = json.loads((RUN / 'inventory.json').read_text())

MAPS = {
    ('furina', 'failed'): [0, 1, 2, 3, 4, 3, 2, 1],
    ('ganyu', 'failed'): [0, 1, 2, 3, 4, 3, 2, 1],
    ('hu-tao', 'failed'): [0, 1, 2, 2, 2, 2, 6, 7],
    ('kazuha-chibi', 'failed'): [1, 0, 2, 6, 6, 2, 0, 1],
    ('kazuha-chibi', 'waiting'): [0, 1, 2, 2, 1, 0],
    ('black-swan', 'failed'): [0, 1, 2, 3, 3, 2, 1, 0],
    ('sparkle', 'failed'): [0, 1, 2, 5, 5, 2, 1, 0],
    ('kiana-kaslana', 'failed'): [0, 1, 2, 3, 3, 2, 1, 0],
    ('kevin-kaslana', 'failed'): [0, 2, 4, 6, 7, 5, 3, 1],
    ('ruan-mei', 'waiting'): [0, 1, 2, 3, 4, 0],
    ('burnice-white', 'failed'): [0, 1, 2, 3, 4, 3, 2, 1],
}

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def build():
    manifest = []
    for pet in INVENTORY['editions']:
        original = Image.open(ROOT / pet['atlas']).convert('RGBA')
        assert sha(ROOT / pet['atlas']) == pet['sha256'], 'Baseline changed: ' + pet['id']
        final = original.copy()
        rows = []
        for action in pet['rows']:
            key = pet['id'], action['state']
            before = Image.open(ROOT / action['strip']).convert('RGBA')
            count = action['count']
            out = RUN / 'candidates' / pet['id']
            source = None
            for group in ('reextracted-genshin-others', 'reextracted-star-honkai', 'reextracted-zzz-honkai', 'generated-strips', 'jump-registration-v2'):
                option = RUN / group / pet['id'] / (action['state'] + '.png')
                if key == ('kafka', 'failed') and group == 'reextracted-star-honkai':
                    option = option.with_name('failed-recovery.png')
                if option.is_file():
                    source = option
            if source:
                after = Image.open(source).convert('RGBA')
                method = ('source-arc-registration' if 'jump-registration-v2' in source.parts else
                          'generated-row' if 'generated-strips' in source.parts else 'source-reextraction')
            elif key in MAPS:
                mapping = MAPS[key]
                assert len(mapping) == count
                after = Image.new('RGBA', (192 * count, 208))
                for col, selected in enumerate(mapping):
                    assert 0 <= selected < count
                    after.paste(before.crop((selected * 192, 0, (selected + 1) * 192, 208)), (col * 192, 0))
                method = 'same-state-complete-frames'
            else:
                continue
            assert after.size == before.size == (count * 192, 208)
            assert before.tobytes() != after.tobytes()
            out.mkdir(parents=True, exist_ok=True)
            strip = out / (action['state'] + '.png')
            after.save(strip)
            final.paste(after, (0, action['row'] * 208))
            contact = Image.new('RGB', (max(960, count * 192), 456), '#f0efec')
            contact.paste(before, (0, 20), before)
            contact.paste(after, (0, 248), after)
            draw = ImageDraw.Draw(contact)
            draw.text((4, 4), pet['id'] + ' / ' + action['state'] + ' / BEFORE', fill='#333333')
            draw.text((4, 232), 'AFTER / native 192 x 208 cells', fill='#333333')
            contact_path = out / (action['state'] + '-comparison.jpg')
            contact.save(contact_path, quality=95)
            frames = [after.crop((c * 192, 0, (c + 1) * 192, 208)) for c in range(count)]
            preview = out / (action['state'] + '.webp')
            frames[0].save(preview, format='WEBP', save_all=True, append_images=frames[1:],
                           duration=action['durations_ms'], loop=0, lossless=True, exact=True)
            rows.append({'state': action['state'], 'row': action['row'], 'count': count,
                         'durations_ms': action['durations_ms'], 'method': method,
                         'mapping': MAPS.get(key) if method == 'same-state-complete-frames' else None,
                         'source': str(source.relative_to(ROOT)) if source else action['strip'],
                         'strip': str(strip.relative_to(ROOT)), 'sha256': sha(strip),
                         'comparison': str(contact_path.relative_to(ROOT)), 'preview': str(preview.relative_to(ROOT)),
                         'visual_qa': 'pending'})
        if rows:
            changed = {r['row']: r['count'] for r in rows}
            protected = 0
            for row in range(11):
                for col in range(8):
                    if row in changed and col < changed[row]:
                        continue
                    box = (col * 192, row * 208, (col + 1) * 192, (row + 1) * 208)
                    assert original.crop(box).tobytes() == final.crop(box).tobytes()
                    protected += 1
            atlas = out / 'spritesheet.webp'
            if not atlas.exists() or Image.open(atlas).convert('RGBA').tobytes() != final.tobytes():
                final.save(atlas, format='WEBP', lossless=True, quality=100, method=6, exact=True)
            assert Image.open(atlas).convert('RGBA').tobytes() == final.tobytes()
            manifest.append({'id': pet['id'], 'atlas': str(atlas.relative_to(ROOT)), 'sha256': sha(atlas),
                             'baseline_sha256': pet['sha256'], 'protected_cells': protected, 'rows': rows})
            print(pet['id'], len(rows), flush=True)
    result = {'baseline_commit': INVENTORY['baseline_commit'], 'client_version': INVENTORY['client_version'],
              'status': 'pending-independent-visual-qa', 'editions': manifest,
              'changed_rows': sum(len(p['rows']) for p in manifest)}
    (RUN / 'candidates.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'editions': len(manifest), 'rows': result['changed_rows']}))

if __name__ == '__main__':
    build()

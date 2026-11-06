"""Process actual generated transparent rows with one shared source viewport."""
import hashlib
import importlib.util
import json
from pathlib import Path
from PIL import Image

RUN = Path(__file__).resolve().parent
ROOT = RUN.parents[1]
SKILL = Path('/home/ubuntu23/.codex/skills/hatch-pet/scripts')

def module(name):
    spec = importlib.util.spec_from_file_location(name, SKILL / (name + '.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

extract = module('extract_strip_frames')
despill = module('despill_chroma_edges')
records = []
for source in sorted((RUN / 'generation').glob('*/selected/*.png')):
    pet, state = source.parents[1].name, source.stem
    count = extract.ROW_FRAME_COUNTS[state]
    strip = Image.open(source).convert('RGBA')
    assert strip.getchannel('A').getextrema()[0] == 0
    groups = extract.component_frame_groups(strip, count)
    assert groups is not None and len(groups) == count
    boxes = [extract.component_bounds(g) for g in groups]
    assert all(boxes[i][2] <= boxes[i + 1][0] for i in range(count - 1)), 'Overlapping source figures'
    frames = extract.extract_stable_slot_frames(strip, count)
    result = Image.new('RGBA', (count * 192, 208))
    for col, frame in enumerate(frames):
        result.paste(frame, (192 * col, 0))
    request = json.loads((source.parents[1] / 'pet_request.json').read_text())
    key = extract.parse_hex_color(request['chroma_key']['hex'])
    cleaned, cleanup = despill.decontaminate_image(result, chroma_key=key)
    assert result.getchannel('A').tobytes() == cleaned.getchannel('A').tobytes()
    out = RUN / 'generated-strips' / pet
    out.mkdir(parents=True, exist_ok=True)
    dest = out / (state + '.png')
    cleaned.save(dest)
    bounds = [cleaned.crop((c * 192, 0, (c + 1) * 192, 208)).getchannel('A').getbbox() for c in range(count)]
    assert all(b and b[0] > 0 and b[1] > 0 and b[2] < 192 and b[3] < 208 for b in bounds)
    records.append({'id': pet, 'state': state, 'source': str(source.relative_to(ROOT)),
                    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                    'source_group_bounds': boxes, 'method': 'stable-slots / shared source viewport',
                    'source_alpha_preserved_before_component_extraction': True,
                    'chroma_background_removal': False, 'despill_passes': 1, 'despill': cleanup,
                    'output': str(dest.relative_to(ROOT)), 'sha256': hashlib.sha256(dest.read_bytes()).hexdigest(),
                    'bounds': bounds, 'visual_qa': 'pending'})
(RUN / 'generated-strips/manifest.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'generated_rows': len(records)}))

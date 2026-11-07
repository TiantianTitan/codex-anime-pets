"""Incremental extraction, checks and explicit adoption of approved row frames."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys

from PIL import Image, ImageDraw

RUN = Path(__file__).resolve().parents[1]
SKILL = Path('/home/ubuntu23/.codex/skills/hatch-pet/scripts')
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('state')
parser.add_argument('--method', default='auto')
parser.add_argument('--layout')
parser.add_argument('--adopt', action='store_true')
parser.add_argument('--note', default='')
args = parser.parse_args()
qa = RUN / 'qa/rows' / args.state
frames_root = qa / 'frames'
if not args.adopt:
    command = [sys.executable, str(SKILL/'extract_strip_frames.py'), '--decoded-dir', str(RUN/'decoded'),
        '--output-dir', str(frames_root), '--states', args.state, '--method', args.method, '--chroma-key', '#FF00FF']
    if args.layout:
        command += ['--frame-layout', str(Path(args.layout).resolve())]
    if args.method != 'registered':
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL)
    command = [sys.executable, str(SKILL/'inspect_frames.py'), '--frames-root', str(frames_root),
        '--states', args.state, '--json-out', str(qa/'review.json')]
    if args.method not in ('reviewed-layout', 'registered'):
        command += ['--require-components', '--allow-stable-slots']
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode:
        print(result.stdout + result.stderr)
    frame_paths = sorted((frames_root/args.state).glob('*.png'))
    strip = Image.new('RGB', (192*(len(frame_paths)+1), 240), '#252d38')
    draw = ImageDraw.Draw(strip)
    for index, path in enumerate(frame_paths):
        frame = Image.open(path).convert('RGBA')
        strip.paste(frame, (index*192, 28), frame)
        draw.text((index*192+6, 8), f'{args.state} {index}', fill='white')
    reference = RUN/'frames/idle/00.png'
    if reference.exists():
        frame = Image.open(reference).convert('RGBA')
        strip.paste(frame, (len(frame_paths)*192,28), frame)
        draw.text((len(frame_paths)*192+6,8), 'IDLE REFERENCE', fill='#ffe28b')
    strip.save(qa/'native.png')
    review = json.loads((qa/'review.json').read_text())
    print(json.dumps({'state': args.state, 'method':args.method, 'errors':review.get('errors', []),
        'warnings': review.get('warnings', []), 'native':str(qa/'native.png')}))
    raise SystemExit(result.returncode)

assert args.note, 'Adoption needs an actual visual/extraction review note'
review = json.loads((qa/'review.json').read_text())
assert not review.get('errors'), review
subset = json.loads((frames_root/'frames-manifest.json').read_text())
row = subset['rows'][0]
destination = RUN/'frames'/args.state
destination.mkdir(parents=True, exist_ok=True)
row['frames'] = []
for source in sorted((frames_root/args.state).glob('*.png')):
    shutil.copy2(source, destination/source.name)
    row['frames'].append(str(destination/source.name))
row['review_note'] = args.note
manifest_path = RUN/'frames/frames-manifest.json'
manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {**subset, 'rows':[]}
manifest['rows'] = [item for item in manifest['rows'] if item['state'] != args.state] + [row]
manifest_path.write_text(json.dumps(manifest, indent=2)+'\n')
subprocess.run([sys.executable, str(RUN/'qa/record-selection.py'), args.state, '--complete', '--note', args.note], check=True)

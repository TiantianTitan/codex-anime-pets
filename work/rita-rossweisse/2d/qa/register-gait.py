"""Preserve complete source gait phases with one scale and a shared ground plane."""
import hashlib
import json
from pathlib import Path
import sys

import numpy as np
from PIL import Image

RUN = Path(__file__).resolve().parents[1]
sys.path.insert(0, '/home/ubuntu23/.codex/skills/hatch-pet/scripts')
from extract_strip_frames import remove_chroma_background

state = sys.argv[1]
assert state in ('running-right', 'running-left')
geometry = json.loads((RUN/f'qa/rows/{state}/source-geometry.json').read_text())
source = RUN/f'decoded/{state}.png'
assert hashlib.sha256(source.read_bytes()).hexdigest() == geometry['source_sha256']
strip = remove_chroma_background(Image.open(source), (0,255,0), 96)
reference = Image.open(RUN/'frames/idle/00.png').convert('RGBA')
ref_box = reference.getchannel('A').getbbox()
boxes = geometry['boxes']
source_ground = max(box[3] for box in boxes)
contacts = [box for box in boxes if source_ground-box[3] <= 3]
assert contacts
scale = (ref_box[3]-ref_box[1]) / float(np.median([box[3]-box[1] for box in contacts]))
ref_alpha = np.array(reference.getchannel('A'))
band = ref_alpha[ref_box[1]:ref_box[1]+round((ref_box[3]-ref_box[1])*0.32)] > 16
weights = band.sum(axis=0)
target_x = float(np.dot(np.arange(192), weights)/weights.sum())
alpha = np.array(strip.getchannel('A'))
destination = RUN/f'qa/rows/{state}/frames/{state}'
destination.mkdir(parents=True, exist_ok=True)
transforms = []
for index, box in enumerate(boxes):
    left, top, right, bottom = box
    band = alpha[top:top+round((bottom-top)*0.32),left:right] > 16
    weights = band.sum(axis=0)
    source_x = float(np.dot(np.arange(left,right), weights)/weights.sum())
    sprite = strip.crop(box)
    size = (round(sprite.width*scale), round(sprite.height*scale))
    xy = (round(target_x+(left-source_x)*scale), round(ref_box[3]-(source_ground-top)*scale))
    assert xy[0]>=4 and xy[1]>=4 and xy[0]+size[0]<=188 and xy[1]+size[1]<=204, (index, xy, size)
    cell = Image.new('RGBA', (192,208))
    cell.alpha_composite(sprite.resize(size, Image.Resampling.LANCZOS), xy)
    cell.save(destination/f'{index:02d}.png')
    transforms.append({'source_box':box,'source_anchor_x':source_x,'destination_xy':list(xy),
                       'destination_size':list(size),'source_lift_scaled':(source_ground-bottom)*scale})
registration = {**geometry,'shared_scale':scale,'source_ground':source_ground,
    'target_baseline':ref_box[3],'target_anchor_x':target_x,'contact_boxes':contacts,
    'source_frame_mapping':list(range(8)),'transforms':transforms,
    'review_note':'Automatic per-pose fitting places airborne feet on the ground and alters anatomical scale. Complete separated source figures retain original order, one contact-derived scale, full-strip shared ground and measured head-axis registration. No frame-wise scaling, mirroring, drawing, interpolation or source-pose replacement.'}
(RUN/f'qa/{state}-registration.json').write_text(json.dumps(registration,indent=2)+'\n')
manifest = {'ok':True,'chroma_key':{'hex':'#00FF00','rgb':[0,255,0],'threshold':96},'rows':[{
    'state':state,'frames':[str(destination/f'{i:02d}.png') for i in range(8)],
    'method':'reviewed-gait-viewport','source':str(source),'source_sha256':geometry['source_sha256'],
    'extraction':registration}]}
(destination.parent/'frames-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'state':state,'scale':scale,'lifts':[round(t['source_lift_scaled'],2) for t in transforms], 'baseline':ref_box[3]}))

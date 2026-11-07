"""Inspect complete source silhouettes and prepare a shared grounded transform."""
import hashlib
import json
from pathlib import Path
import sys

import numpy as np
from PIL import Image

RUN = Path(__file__).resolve().parents[1]
sys.path.insert(0, '/home/ubuntu23/.codex/skills/hatch-pet/scripts')
from extract_strip_frames import remove_chroma_background, component_frame_groups, component_bounds, ROW_FRAME_COUNTS

state = sys.argv[1]
source = Path(sys.argv[2]).resolve() if len(sys.argv)>2 else RUN/'decoded'/f'{state}.png'
strip = remove_chroma_background(Image.open(source), (255,0,255), 96)
groups = component_frame_groups(strip, ROW_FRAME_COUNTS[state])
assert groups is not None
boxes = [component_bounds(group) for group in groups]
assert all(a[2] < b[0] for a,b in zip(boxes, boxes[1:])), 'Review touching poses before cutting'
cuts = [0]+[round((a[2]+b[0])/2) for a,b in zip(boxes,boxes[1:])]+[strip.width]
alpha = np.array(strip.getchannel('A'))
anchors=[]
for left,top,right,bottom in boxes:
    weights=(alpha[bottom-max(1,(bottom-top)//8):bottom,left:right]>16).sum(axis=0)
    anchors.append([float(np.dot(np.arange(left,right),weights)/weights.sum()),bottom])
geometry={'state':state,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
          'source_size':list(strip.size),'boxes':boxes,'foot_anchors':anchors,
          'heights':[b[3]-b[1] for b in boxes]}
(RUN/f'qa/rows/{state}/source-geometry.json').write_text(json.dumps(geometry,indent=2)+'\n')
if state in ('running-right','running-left'):
    # A valid complete pose supplies side-specific costume grounding, not replacement frames.
    left,top,right,bottom=boxes[0]
    facing='right' if state=='running-right' else 'left'
    Image.open(source).crop((max(0,left-16),max(0,top-16),min(strip.width,right+16),min(strip.height,bottom+16))).save(RUN/f'references/{facing}-profile-costume.png')
if state == 'idle':
    base = remove_chroma_background(Image.open(RUN/'decoded/base.png'),(255,0,255),96)
    sprite = base.crop(base.getchannel('A').getbbox())
    # This character needs headroom for a small hop. One 182px neutral silhouette
    # is used as a shared anatomical ruler, with feet at 201px.
    size=(round(sprite.width*182/sprite.height),182)
    cell=Image.new('RGBA',(192,208))
    cell.alpha_composite(sprite.resize(size,Image.Resampling.LANCZOS),((192-size[0])//2,19))
    cell.save(RUN/'qa/canonical-cell.png')
if state not in ('jumping','running-right','running-left'):
    layout={state:{'source_sha256':geometry['source_sha256'],'cuts':cuts,'foot_anchors':anchors,
        'reference_cell':'canonical-cell.png' if state=='idle' else '../frames/idle/00.png',
        'review_note':'Complete isolated source silhouettes reviewed. Component per-pose fitting normalizes every bounding height independently and erases quiet body motion/changes head size in head bows; shared anatomical scale and measured planted boot anchors preserve the original gesture and canonical scale. No component deletion, per-frame scaling or repaint.'}}
    (RUN/f'qa/{state}-source-layout.json').write_text(json.dumps(layout,indent=2)+'\n')
if state == 'jumping':
    reference=Image.open(RUN/'frames/idle/00.png').convert('RGBA')
    ref_box=reference.getchannel('A').getbbox()
    band=np.array(reference.getchannel('A'))[ref_box[3]-max(1,(ref_box[3]-ref_box[1])//8):ref_box[3],:]>16
    weights=band.sum(axis=0)
    target_x=float(np.dot(np.arange(192),weights)/weights.sum())
    baseline=ref_box[3]
    scale=(ref_box[3]-ref_box[1])/((geometry['heights'][0]+geometry['heights'][-1])/2)
    ground=(boxes[0][3]+boxes[-1][3])/2
    lifts=[max(0,ground-box[3])*scale for box in boxes]
    heights=[round((box[3]-box[1])*scale) for box in boxes]
    limits=[(baseline-height-8)/lift for height,lift in zip(heights,lifts) if lift>0]
    compression=min(1.0,min(limits))
    assert 0.25 <= compression <= 1.0
    destination=RUN/'qa/rows/jumping/frames/jumping'
    destination.mkdir(parents=True,exist_ok=True)
    transforms=[]
    for index,(box,anchor,lift) in enumerate(zip(boxes,anchors,lifts)):
        sprite=strip.crop(box)
        size=(round(sprite.width*scale),round(sprite.height*scale))
        x=round(target_x+(box[0]-anchor[0])*scale)
        y=round(baseline-lift*compression-size[1])
        assert x>=4 and y>=4 and x+size[0]<=188 and y+size[1]<=204
        cell=Image.new('RGBA',(192,208))
        cell.alpha_composite(sprite.resize(size,Image.Resampling.LANCZOS),(x,y))
        cell.save(destination/f'{index:02d}.png')
        transforms.append({'source_box':box,'source_foot_anchor':anchor,'destination_xy':[x,y],
                           'destination_size':list(size),'source_lift_scaled':lift,'destination_lift':lift*compression})
    registration={**geometry,'shared_scale':scale,'target_baseline':baseline,'target_anchor_x':target_x,
        'arc_compression':compression,'transforms':transforms,'source_frame_mapping':list(range(5)),
        'review_note':'Default component fitting ground-aligned all five airborne poses and resized their crouches. Complete original five poses keep one shared scale from grounded endpoints, preserve ordered poses and compress only their existing vertical displacement to leave 8px headroom. No anatomy interpolation, local repaint, per-frame scaling or borrowed frames.'}
    (RUN/'qa/jumping-registration.json').write_text(json.dumps(registration,indent=2)+'\n')
    manifest={'ok':True,'chroma_key':{'hex':'#FF00FF','rgb':[255,0,255],'threshold':96},'rows':[{
        'state':'jumping','frames':[str(destination/f'{i:02d}.png') for i in range(5)],
        'method':'reviewed-jump-arc','source':str(source),'source_sha256':geometry['source_sha256'],
        'extraction':registration}]}
    (destination.parent/'frames-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(geometry))

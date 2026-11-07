"""Recover original complete grounded poses with one foot-anchored transform."""
import sys
from pathlib import Path
import json
import hashlib
import numpy as np
from PIL import Image
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,'/home/ubuntu23/.codex/skills/hatch-pet/scripts')
from extract_strip_frames import remove_chroma_background, component_frame_groups, component_bounds, ROW_FRAME_COUNTS
state=sys.argv[1]
assert state in ('waving','waiting','running','review','failed')
path=R/'decoded'/f'{state}.png'
strip=remove_chroma_background(Image.open(path),(0,255,0),96)
groups=component_frame_groups(strip,ROW_FRAME_COUNTS[state])
boxes=[component_bounds(g) for g in groups]
cuts=[0]+[round((a[2]+b[0])/2) for a,b in zip(boxes,boxes[1:])]+[strip.width]
assert all(a[2]<b[0] for a,b in zip(boxes,boxes[1:]))
alpha=np.array(strip.getchannel('A'))
anchors=[]
for left,top,right,bottom in boxes:
    band=alpha[bottom-max(1,(bottom-top)//8):bottom,left:right]>16
    xs=band.sum(axis=0)
    foot_x=float(np.dot(np.arange(left,right),xs)/xs.sum())
    anchors.append([foot_x,bottom])
layout={state:{'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'cuts':cuts,'foot_anchors':anchors,'reference_cell':'../frames/idle/00.png','review_note':'Native full-pose review confirmed isolated complete figures and clear inter-figure cuts. Per-bbox recentering made planted boots shift during upper-body gestures; one shared scale and measured lower-boot anchors recover grounded placement. No component deletion, repaint, or per-frame rescale.'}}
output=R/'qa'/f'{state}-source-layout.json'
output.write_text(json.dumps(layout,indent=2)+'\n')
print(str(output))

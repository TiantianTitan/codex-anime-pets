import json,hashlib,importlib.util
from pathlib import Path
from PIL import Image
root=Path('/home/ubuntu23/Bureau/codex-anime-pets');run=root/'work/motion-refinement-2026-11-06';out=run/'reextracted-star-honkai/kafka';out.mkdir(parents=True,exist_ok=True)
script=Path('/home/ubuntu23/.codex/skills/hatch-pet/scripts/extract_strip_frames.py')
spec=importlib.util.spec_from_file_location('extract',script);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
source=root/'work/kafka/2d/decoded/failed.png';im=mod.remove_chroma_background(Image.open(source),(0,255,0),96)
groups=mod.component_frame_groups(im,8);boxes=[mod.component_bounds(g) for g in groups]
assert len(groups)==8 and all(len(g)==1 for g in groups)
cuts=[0]+[round((boxes[i-1][2]+boxes[i][0])/2) for i in range(1,8)]+[im.width]
anchors=[]
for i,b in enumerate(boxes):
    band=im.getchannel('A').crop((b[0],b[3]-40,b[2],b[3]))
    weights=[sum(band.crop((x,0,x+1,band.height)).histogram()[17:]) for x in range(band.width)]
    anchors.append([b[0]+sum(x*w for x,w in enumerate(weights))/sum(weights),627])
inv=json.loads((run/'inventory.json').read_text());e=next(e for e in inv['editions'] if e['id']=='kafka')
atlas=Image.open(root/e['atlas']).convert('RGBA');ref=atlas.crop((0,5*208,192,6*208));ref.save(out/'approved-failed-first-cell.png')
layout={'failed':{'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'cuts':cuts,'foot_anchors':anchors,'reference_cell':'approved-failed-first-cell.png','review_note':'Full original 8-figure strip visually reviewed: shared source foot baseline y=627; source head lowers progressively through frames with no scale increase. Eight figures are separated by empty chroma gaps; cuts use the midpoint of each empty gap. Feet x anchors use the lower 40 source pixels; one shared scale preserves source Y offsets. Reference is the exact approved current failed first cell, preserving state-entry registration. No component removal or per-frame fit.'}}
(out/'reviewed-layout.json').write_text(json.dumps(layout,indent=2)+'\n')
print(out/'reviewed-layout.json');print('cuts',cuts);print('anchors',anchors)

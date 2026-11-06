"""Recover the original coherent idle family using its actual figure anchors."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
from PIL import Image, ImageDraw

ROOT=Path(__file__).resolve().parents[2]
RUN=Path(__file__).resolve().parent
OUT=RUN/'mei-3d-reextraction'
OUT.mkdir(exist_ok=True)
sys.path.insert(0,'/home/ubuntu23/.codex/skills/hatch-pet/scripts')
sys.path.insert(0,str(ROOT/'scripts'))
from extract_strip_frames import remove_chroma_background,connected_components,component_group_image
from assemble_motion_candidates import register,cell,foot_anchor

source=ROOT/'work/raiden-mei/3d/decoded/idle.png'
original=Image.open(RUN/'originals/raiden-mei-3d/spritesheet.webp').convert('RGBA')
strip=remove_chroma_background(Image.open(source),(0,255,0),90)
alpha=strip.getchannel('A')
columns=[sum(alpha.getpixel((x,y))>128 for y in range(530,650)) for x in range(strip.width)]
groups=[]
for x,n in enumerate(columns):
    if n>8:
        if not groups or x-groups[-1][-1]>80:groups.append([])
        groups[-1].append(x)
assert len(groups)==6
centers=[sum(x*columns[x] for x in g)/sum(columns[x] for x in g) for g in groups]
projection=[sum(alpha.getpixel((x,y))>128 for y in range(strip.height)) for x in range(strip.width)]
cuts=[0]
for left,right in zip(centers,centers[1:]):
    middle=(left+right)/2
    # Only the thin points where adjacent hair tips meet cross these cuts.
    # Move each boundary to the least occupied source column near the midpoint.
    cuts.append(min(range(round(middle-35),round(middle+35)),key=lambda x:(projection[x],abs(x-middle))))
cuts.append(strip.width)
poses=[]
for left,right in zip(cuts,cuts[1:]):
    crop=strip.crop((left,0,right,strip.height))
    components=connected_components(crop)
    main=max(components,key=lambda c:c['area'])
    # Exclude disconnected pieces belonging to a neighboring figure.
    pose=component_group_image(crop,[main],padding=0)
    poses.append(pose)
anchors=[foot_anchor(im) for im in poses]
maximum_height=max(im.height for im in poses)
extent=max(max(anchor,im.width-anchor) for im,anchor in zip(poses,anchors))
viewport_width=round(extent*2)+12
prepared=[]
for im,anchor in zip(poses,anchors):
    canvas=Image.new('RGBA',(viewport_width,maximum_height+8))
    canvas.alpha_composite(im,(round(viewport_width/2-anchor),maximum_height-im.height+4))
    prepared.append(canvas)
registered,registration=register(prepared,cell(original,0,6))
raw=original.copy()
for c,im in enumerate(registered):raw.paste(im,(c*192,0))
raw.save(OUT/'assembled.png')
subprocess.run([sys.executable,'/home/ubuntu23/.codex/skills/hatch-pet/scripts/despill_chroma_edges.py',
    str(OUT/'assembled.png'),'--output',str(OUT/'cleaned.png'),'--chroma-key','#00FF00',
    '--json-out',str(OUT/'chroma-despill.json')],check=True,capture_output=True)
assert json.loads((OUT/'chroma-despill.json').read_text())['ok']
cleaned=Image.open(OUT/'cleaned.png').convert('RGBA')
mapping=[0,1,1,3,4,5]  # Original coherent source slot 2 is a closed-eye blink.
final=original.copy()
for c,source_c in enumerate(mapping):final.paste(cell(cleaned,0,source_c),(c*192,0))
atlas=OUT/'spritesheet.webp'
final.save(atlas,lossless=True,quality=100,method=6,exact=True)
subprocess.run([sys.executable,'/home/ubuntu23/.codex/skills/hatch-pet/scripts/validate_atlas.py',str(atlas),
    '--require-v2','--chroma-key','#00FF00','--json-out',str(OUT/'atlas-validation.json')],check=True,capture_output=True)
assert json.loads((OUT/'atlas-validation.json').read_text())['ok']
check=Image.open(atlas).convert('RGBA')
for row in range(11):
    for c in range(8):
        if row==0 and c<6:continue
        assert cell(check,row,c).tobytes()==cell(original,row,c).tobytes()
sheet=Image.new('RGB',(1152,456),'#e3e9df');draw=ImageDraw.Draw(sheet)
for row,im in enumerate([original,final]):
    draw.text((10,row*228+3),'Original published idle' if row==0 else 'Re-extracted complete source idle',fill='black')
    for c in range(6):
        sprite=cell(im,0,c);sheet.paste(sprite,(c*192,row*228+20),sprite)
sheet.save(OUT/'comparison.png')
report={'ok':True,'source':str(source.relative_to(ROOT)),'sourceSha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'sourceCuts':cuts,'sourceCutForegroundHeights':[projection[x] for x in cuts[1:-1]],
    'sourceFootAnchors':centers,'method':'original source extraction using foot-anchor groups and minimum-occupancy boundaries; shared scale and planted baseline',
    'sourceFrameMapping':mapping,'registration':registration,'preservedNonIdleCells':82,
    'sha256':hashlib.sha256(atlas.read_bytes()).hexdigest(),'visualReview':'pending'}
(OUT/'validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report,ensure_ascii=False))

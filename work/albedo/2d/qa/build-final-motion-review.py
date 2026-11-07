"""Exact-final-atlas native-size temporal evidence, without opening UI windows."""
from pathlib import Path
import hashlib
import importlib.util
import json
from PIL import Image, ImageDraw

R=Path(__file__).resolve().parents[1]
atlas_path=R/'final/spritesheet-extended.webp'
skill=Path('/home/ubuntu23/.codex/skills/hatch-pet/scripts')
spec=importlib.util.spec_from_file_location('previews',skill/'render_final_animation_previews.py')
pv=importlib.util.module_from_spec(spec)
spec.loader.exec_module(pv)
atlas=Image.open(atlas_path).convert('RGBA')
assert atlas.size==(1536,2288)
def cell(row,col):
    return atlas.crop((192*col,208*row,192*(col+1),208*(row+1)))
out=R/'qa/transitions-final'
native=R/'qa/native-final'
out.mkdir(exist_ok=True)
native.mkdir(exist_ok=True)
idle_holds=[1680,660,660,840,840,1920]
idle=[cell(0,c) for c in range(6)]
seams=Image.new('RGB',(576,8*240),'#242b34')
draw=ImageDraw.Draw(seams)
records=[]
for row,(state,source_times) in enumerate(pv.ROW_DURATIONS.items()):
    times=idle_holds if state=='idle' else source_times
    frames=[cell(row,col) for col in range(len(times))]
    strip=Image.new('RGB',(192*len(times),236),'#242b34')
    labels=ImageDraw.Draw(strip)
    for col,(frame,t) in enumerate(zip(frames,times)):
        strip.paste(frame,(192*col,28),frame)
        labels.text((192*col+5,8),f'{state} {col}: {t}ms',fill='white')
    strip.save(native/f'{state}.png')
    if state=='idle':
        continue
    sequence=idle+frames*3+idle
    holds=idle_holds+times*3+idle_holds
    dest=out/f'{state}-to-idle.webp'
    pv.save_preview(sequence,holds,dest)
    check=pv.verify_timeline(sequence,holds,dest)
    top=(row-1)*240
    draw.text((5,top+7),f'{state}: LAST {times[-1]}ms | FIRST {times[0]}ms | IDLE 1680ms',fill='white')
    for col,frame in enumerate([frames[-1],frames[0],idle[0]]):
        seams.paste(frame,(col*192,top+28),frame)
    records.append({'state':state,'path':str(dest.relative_to(R)),'validation':check})
seams.save(R/'qa/motion-seams.png')
look=[cell(9+i//8,i%8) for i in range(16)]
pv.save_preview(look,[200]*16,out/'look-loop.webp')
look_check=pv.verify_timeline(look,[200]*16,out/'look-loop.webp')
report={'ok':all(r['validation']['ok'] for r in records) and look_check['ok'],'atlas_sha256':hashlib.sha256(atlas_path.read_bytes()).hexdigest(),'client_version':'26.1007.21434','timing_evidence':'docs/pet-compatibility-2026-11-06.md; docs/pet-motion-refinement-2026-11-06.md','mode':'background-only exact encoded timeline and native ordered-frame/seam inspection','live_installed_client_test':False,'action_schedule':'idle cycle -> 3 action cycles -> idle cycle; version-qualified local client evidence','rows':records,'look_loop':{'purpose':'QA-only clockwise sweep; not client scheduling','duration_per_pose_ms':200,'validation':look_check}}
(R/'qa/transition-validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'ok':report['ok'],'atlas_sha256':report['atlas_sha256'],'transitions':len(records)}))

import json,hashlib,importlib.util
from pathlib import Path
from PIL import Image,ImageDraw
root=Path('/home/ubuntu23/Bureau/codex-anime-pets');run=root/'work/motion-refinement-2026-11-06';out=run/'reextracted-star-honkai/kafka'
script=Path('/home/ubuntu23/.codex/skills/hatch-pet/scripts/despill_chroma_edges.py')
spec=importlib.util.spec_from_file_location('despill',script);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
frames=[Image.open(out/f'extracted-frames/failed/{i:02}.png').convert('RGBA') for i in range(8)]
raw=Image.new('RGBA',(1536,208))
for i,f in enumerate(frames):raw.paste(f,(i*192,0))
raw.save(out/'failed-before-despill.png')
clean,report=mod.decontaminate_image(raw,chroma_key=(0,255,0))
clean.save(out/'failed.png')
assert raw.getchannel('A').tobytes()==clean.getchannel('A').tobytes()
(out/'despill-report.json').write_text(json.dumps(report,indent=2)+'\n')
frames=[clean.crop((i*192,0,(i+1)*192,208)) for i in range(8)]
mapping=[0,2,4,6,7,5,3,1]
recovery=Image.new('RGBA',(1536,208))
for i,index in enumerate(mapping):recovery.paste(frames[index],(i*192,0))
recovery.save(out/'failed-recovery.png')
before=Image.open(run/'rows/kafka--failed.png').convert('RGBA')
contact=Image.new('RGB',(1536,3*240),(242,240,235));draw=ImageDraw.Draw(contact)
for row,(name,im) in enumerate([('BEFORE: published atlas / per-frame fit',(before)),('REEXTRACTED: original order / one shared scale and ground',(clean)),('RECOVERY CANDIDATE: source frames 0,2,4,6,7,5,3,1',(recovery))]):
 draw.text((8,row*240+5),name,fill=(30,30,30))
 for i in range(8):
  if i%2:draw.rectangle((i*192,row*240+30,(i+1)*192-1,row*240+237),fill=(224,223,219))
 contact.paste(im,(0,row*240+30),im)
contact.save(out/'failed-comparison.png')
durations=[140]*7+[240]
for name,seq in [('failed',[0,1,2,3,4,5,6,7]),('failed-recovery',mapping)]:
 fs=[frames[i] for i in seq]
 fs[0].save(out/f'{name}.webp',save_all=True,append_images=fs[1:],duration=durations,loop=0,lossless=True,quality=100,method=6)
manifest=json.loads((out/'extracted-frames/frames-manifest.json').read_text())
report={'id':'kafka','state':'failed','status':'pending-independent-native-motion-QA','source_path':'work/kafka/2d/decoded/failed.png','source_sha256':hashlib.sha256((root/'work/kafka/2d/decoded/failed.png').read_bytes()).hexdigest(),'method':'hatch-pet extract_strip_frames.py reviewed-layout','extraction_manifest':manifest,'layout_file':str(out/'reviewed-layout.json'),'chroma_key':'#00FF00','key_threshold':96,'despill_passes':1,'alpha_preserved':True,'despill_report':report,'outputs':{},'client_version':'26.1007.21434','preview_timing_ms':durations,'preview_note':'Preview loops the row for QA; actual Desktop scheduling can stop after three loops and return to idle.','source_baseline_y':627,'per_frame_scale_forbidden':True,'before_bounds':[list(before.crop((i*192,0,(i+1)*192,208)).getbbox()) for i in range(8)],'reextracted_bounds':[list(f.getbbox()) for f in frames],'protected_assets_not_written':True}
for name,seq in [('failed',list(range(8))),('failed-recovery',mapping)]:
 path=out/f'{name}.png';report['outputs'][name]={'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'source_frame_mapping':seq,'size':[1536,208],'unique_frames':len(set(hashlib.sha256(frames[i].tobytes()).hexdigest() for i in seq)),'approval':'pending'}
report['comparison_path']=str(out/'failed-comparison.png')
(out/'manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'outputs':report['outputs'],'before_bounds':report['before_bounds'],'reextracted_bounds':report['reextracted_bounds'],'despill_changes':report['despill_report']['changed_pixels']},ensure_ascii=False))

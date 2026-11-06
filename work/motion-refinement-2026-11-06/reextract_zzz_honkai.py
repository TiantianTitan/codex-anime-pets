from pathlib import Path
import sys,json,hashlib
import numpy as np
from PIL import Image,ImageDraw
SKILL=Path('/home/ubuntu23/.codex/skills/hatch-pet/scripts')
sys.path.insert(0,str(SKILL))
import extract_strip_frames as extract
from despill_chroma_edges import decontaminate_image
ROOT=Path('/home/ubuntu23/Bureau/codex-anime-pets')
RUN=ROOT/'work/motion-refinement-2026-11-06'
OUT=RUN/'reextracted-zzz-honkai';OUT.mkdir(exist_ok=True)
inv=json.loads((RUN/'inventory.json').read_text())
jobs=[
 dict(id='raiden-mei',base='raiden-mei',style='2d',state='jumping',cuts=[0,382,764,1146,1524,1910],xs=[204,576,953,1325,1695],baseline=708),
 dict(id='raiden-mei',base='raiden-mei',style='2d',state='failed',cuts=[0,281,549,809,1064,1332,1615,1892,2172],xs=[141.9,410.6,668.8,927.4,1188.8,1467.4,1749.9,2028.4],baseline=593),
 dict(id='raiden-mei',base='raiden-mei',style='2d',state='waiting',cuts=[0,387,737,1091,1447,1776,2172],xs=[196.9,550.1,902.8,1251.4,1603.7,1940.3],baseline=630),
 dict(id='raiden-mei-3d',base='raiden-mei',style='3d',state='jumping',cuts=[0,355,710,1064,1419,1774],xs=[190,540,892,1240,1585],baseline=700),
 dict(id='raiden-mei-3d',base='raiden-mei',style='3d',state='waiting',cuts=[0,321,599,888,1171,1456,1778],xs=[182.2,467.2,739.4,1027.1,1307.6,1600.9],baseline=707,keep_main_component=True),
 dict(id='raiden-mei-3d',base='raiden-mei',style='3d',state='running',cuts=[0,303,572,851,1127,1400,1717],xs=[171.9,443.3,709.9,989.2,1264.2,1540.7],baseline=727),
 dict(id='miyabi',base='miyabi',style='2d',state='jumping',cuts=[0,434,869,1303,1738,2172],xs=[225,658,1094,1522,1942],baseline=692),
]
records=[]
for j in jobs:
 e=next(e for e in inv['editions'] if e['id']==j['id']);r=next(r for r in e['rows'] if r['state']==j['state'])
 petout=OUT/j['id'];petout.mkdir(exist_ok=True);meta=petout/'_provenance';meta.mkdir(exist_ok=True)
 src=ROOT/f"work/{j['base']}/{j['style']}/decoded/{j['state']}.png"
 request=ROOT/f"work/{j['base']}/{j['style']}/pet_request.json";keymeta=json.loads(request.read_text())['chroma_key'];key=tuple(keymeta['rgb'])
 atlas=Image.open(ROOT/e['atlas']).convert('RGBA');neutral=atlas.crop((1152,0,1344,208));ref=meta/'reference-neutral.png';neutral.save(ref)
 lay={'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'cuts':j['cuts'],'foot_anchors':[[x,j['baseline']] for x in j['xs']],'reference_cell':str(ref),'review_note':('Complete source figures were visually reviewed. Separated silhouettes; shared grounded baseline for all frames deliberately preserves source Y takeoff/apex/landing. Horizontal anchors follow body center, not a moving raised foot.' if j['state']=='jumping' else 'Full decoded row compared with original clipped atlas. Cuts follow the low-occupancy gaps between torso/foot anchors; only narrow touching hair ends cross the boundary. One shared scale and one common foot baseline preserve the original pose deformation. Native-size tip quality remains pending independent QA.')}
 if j.get('keep_main_component'):
  lay.update(keep_main_component=True,neighbor_cleanup_note='The tiny 48-pixel component at source interval 2 local x0..6/y228..237 is the previous pose\'s angular head ornament beyond the reviewed boundary, not a detached detail of pose 2. Remove that neighbor remnant only; retain main silhouette coordinates.')
 lp=meta/f"{j['state']}-layout.json";lp.write_text(json.dumps({j['state']:lay},indent=2)+'\n')
 result=extract.extract_state(src,j['state'],meta/'frames',key,96,'reviewed-layout',lay,meta)
 frames=[Image.open(p).convert('RGBA') for p in result['frames']]
 strip=Image.new('RGBA',(192*len(frames),208))
 for i,frame in enumerate(frames):strip.paste(frame,(i*192,0))
 clean,despill=decontaminate_image(strip,chroma_key=key)
 assert np.array_equal(np.array(clean)[:,:,3],np.array(strip)[:,:,3])
 out=petout/f"{j['state']}.png";clean.save(out)
 before=Image.open(ROOT/r['strip']).convert('RGBA')
 comp=Image.new('RGB',(strip.width,468),'#eceae5');d=ImageDraw.Draw(comp)
 for yy,img,title in [(24,before,'BEFORE / original fixed-frame release'),(258,clean,'AFTER / original complete source, shared scale and preserved trajectory')]:
  d.text((5,yy-18),title,fill='#252525')
  for i in range(len(frames)):d.rectangle((i*192,yy,(i+1)*192-1,yy+207),fill='#f6f4ef' if i%2==0 else '#dedbd5')
  comp.paste(img,(0,yy),img)
 cp=meta/f"{j['state']}-comparison.png";comp.save(cp)
 record={'id':j['id'],'state':j['state'],'output':str(out.relative_to(ROOT)),'candidate_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'baseline_atlas_sha256':e['sha256'],'source':str(src.relative_to(ROOT)),'source_sha256':lay['source_sha256'],'chroma_key':keymeta['hex'],'chroma_removal_threshold':96,'despill_passes':1,'despill_report':despill,'alpha_unchanged_by_despill':True,'method':'hatch-pet reviewed-layout + shared source-ground baseline','layout':str(lp.relative_to(ROOT)),'extraction':result['extraction'],'frame_count':len(frames),'dimensions':list(clean.size),'bounds':[clean.crop((i*192,0,(i+1)*192,208)).getbbox() for i in range(len(frames))],'comparison':str(cp.relative_to(ROOT)),'qa':'candidate pending independent review'}
 records.append(record)
 print(j['id'],j['state'],record['bounds'],flush=True)
(OUT/'report.json').write_text(json.dumps({'skill_script':str(SKILL/'extract_strip_frames.py'),'skill_script_sha256':hashlib.sha256((SKILL/'extract_strip_frames.py').read_bytes()).hexdigest(),'runtime':'/home/ubuntu23/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3','baseline_commit':inv['baseline_commit'],'records':records,'release_asset_edits':0},ensure_ascii=False,indent=2)+'\n')

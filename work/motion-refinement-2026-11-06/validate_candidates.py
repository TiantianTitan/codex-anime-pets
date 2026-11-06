"""Read-only audit of every final pet candidate and its source/timing chain."""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,subprocess,sys,time
from concurrent.futures import ProcessPoolExecutor,as_completed
from pathlib import Path
from PIL import Image
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
RUN=Path(__file__).resolve().parent
SKILL=Path('/home/ubuntu23/.codex/skills/hatch-pet/scripts')
PYTHON=Path('/home/ubuntu23/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3')
EXPECTED={'idle':(0,6,[1680,660,660,840,840,1920]),'running-right':(1,8,[120]*7+[220]),'running-left':(2,8,[120]*7+[220]),'waving':(3,4,[140]*3+[280]),'jumping':(4,5,[140]*4+[280]),'failed':(5,8,[140]*7+[240]),'waiting':(6,6,[150]*5+[260]),'running':(7,6,[120]*5+[220]),'review':(8,6,[150]*5+[280])}

def path(p):return Path(p) if Path(p).is_absolute() else ROOT/p

def sha(p):return hashlib.sha256(path(p).read_bytes()).hexdigest()

def rgba(p):return Image.open(path(p)).convert('RGBA')

def digest(im):return hashlib.sha256(im.tobytes()).hexdigest()

def load(p):return json.loads(path(p).read_text())

def module(name):
 s=importlib.util.spec_from_file_location(name,SKILL/(name+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

EXTRACT=module('extract_strip_frames');DESPILL=module('despill_chroma_edges')

def check(value,note):
 if not value:raise AssertionError(note)

def strip_of(frames,composite=False):
 out=Image.new('RGBA',(len(frames)*192,208))
 for i,f in enumerate(frames):
  if composite:out.alpha_composite(f,(i*192,0))
  else:out.paste(f,(i*192,0))
 return out

def rebuild_registered_jump(record,e):
 """Re-derive the complete source poses, one scale and the compressed source arc."""
 check(record['state']=='jumping','Arc registration applied outside jumping')
 check(record['source_frame_mapping']==list(range(5)),'Jump source poses reordered')
 raw=path(record['source']);source=rgba(raw);key=EXTRACT.parse_hex_color(record['chroma_key'])
 origin=record['origin_record'];kind=record['source_method']
 check(record['source']==origin['source'] and sha(raw)==origin['source_sha256'],'Jump source differs from its original provenance')
 check(record['chroma_key']==origin['chroma_key'],'Jump source chroma key differs')
 check(record['chroma_removal']==(kind!='transparent-groups'),'Incorrect chroma-removal declaration')
 if kind!='transparent-groups':source=EXTRACT.remove_chroma_background(source,key,96)
 else:check(source.getchannel('A').getextrema()[0]==0,'Generated jump source lacks transparency')
 poses=[];boxes=[];anchors=[]
 if kind=='reviewed-cuts':
  layout=load(origin['layout'])['jumping'];check(layout['source_sha256']==sha(raw),'Jump reviewed cuts not bound to source')
  cuts=layout['cuts'];check(len(cuts)==6,'Jump source cuts count')
  for left,right,anchor in zip(cuts,cuts[1:],layout['foot_anchors']):
   pose=source.crop((left,0,right,source.height));b=pose.getchannel('A').getbbox();check(b is not None,'Empty source jump pose')
   poses.append(pose.crop(b));boxes.append([b[0]+left,b[1],b[2]+left,b[3]]);anchors.append(anchor[0])
  source_ground=max(a[1] for a in layout['foot_anchors'])
 else:
  check(kind in ('transparent-groups','chroma-groups'),'Unknown jump source extraction')
  groups=EXTRACT.component_frame_groups(source,5);check(groups is not None and len(groups)==5,'Jump source pose count')
  for group in groups:
   b=EXTRACT.component_bounds(group);poses.append(EXTRACT.component_group_image(source,group,padding=0));boxes.append(list(b));anchors.append((b[0]+b[2])/2)
  source_ground=max(boxes[0][3],boxes[-1][3])
 check(boxes==record['source_boxes'],'Jump source bounds differ')
 check(source_ground==record['source_baseline_y'],'Jump source ground differs')
 check(record['neutral_atlas']==e['atlas'] and record['neutral_atlas_sha256']==e['sha256']==sha(e['atlas']),'Jump neutral atlas binding differs')
 neutral=rgba(e['atlas']).crop((1152,0,1344,208))
 check(sha(record['neutral_reference'])==record['neutral_reference_sha256'],'Jump neutral reference file hash differs')
 check(rgba(record['neutral_reference']).tobytes()==neutral.tobytes(),'Jump neutral reference differs from baseline')
 box=neutral.getchannel('A').point(lambda a:255 if a>16 else 0).getbbox();check(box is not None,'Empty jump neutral')
 band=neutral.getchannel('A').crop((0,box[3]-max(1,(box[3]-box[1])//8),192,box[3]))
 weights=[sum(band.crop((x,0,x+1,band.height)).histogram()[17:]) for x in range(192)]
 center=sum(x*w for x,w in enumerate(weights))/sum(weights)
 check(record['target_max_pose_height_px']==185 and record['target_ground_y']==203,'Jump target geometry changed')
 heights=[b[3]-b[1] for b in boxes]
 scale=min(185/max(heights),(center-5)/max(a-b[0] for a,b in zip(anchors,boxes)),(187-center)/max(b[2]-a for a,b in zip(anchors,boxes)))
 check(abs(scale-record['shared_scale'])<1e-12,'Jump shared scale does not derive from complete poses and neutral')
 scaled_heights=[round(h*scale) for h in heights]
 natural=[max(0,(source_ground-b[3])*scale) for b in boxes];natural[0]=natural[-1]=0
 limits=[(203-5-h)/lift for h,lift in zip(scaled_heights,natural) if lift>0]
 compression=min(1,min(limits)) if limits else 0
 check(0<=compression<=1 and abs(compression-record['source_arc_compression_factor'])<1e-12,'Jump arc compression differs')
 lifts=[round(v*compression) for v in natural]
 check(natural==record['natural_scaled_lifts_px'] and lifts==record['final_lifts_px'],'Jump lifts no longer follow the source arc')
 check(max(scaled_heights)==record['actual_max_pose_height_px'],'Jump shared pose height differs')
 check(record['arc_peak_lift_at_least_10px']==(max(lifts)>=10),'Jump arc visibility declaration differs')
 frames=[];expected_transforms=[]
 for i,(pose,b,anchor) in enumerate(zip(poses,boxes,anchors)):
  size=(round(pose.width*scale),round(pose.height*scale));x=round(center+(b[0]-anchor)*scale);y=203-lifts[i]-size[1]
  check(4<=x and x+size[0]<=188 and y>=4 and y+size[1]<=204,'Jump pose cropped by cell bounds')
  frame=Image.new('RGBA',(192,208));frame.alpha_composite(pose.resize(size,Image.Resampling.LANCZOS),(x,y));frames.append(frame)
  expected_transforms.append({'frame':i,'source_box':b,'source_anchor_x':anchor,'shared_scale':scale,'scaled_size':list(size),'destination_xy':[x,y],'source_to_cell_translation_xy':[x-b[0]*scale,y-b[1]*scale],'natural_lift_after_scale_px':natural[i],'compressed_lift_px':lifts[i],'target_bottom_y':203-lifts[i]})
 check(expected_transforms==record['translations'],'Jump transforms are not the derived whole-pose transforms')
 check(record['despill_passes']==1 and record['alpha_preserved_during_despill'],'Jump cleanup declaration differs')
 return strip_of(frames)

def preview_check(p,frames,durations):
 source=[];t=0
 for f,d in zip(frames,durations):source.append((t,t+d,np.array(f)));t+=d
 expected_total=t;actual=[];anim=Image.open(path(p));t=0
 for i in range(anim.n_frames):
  anim.seek(i);a=np.array(anim.convert('RGBA'));d=anim.info.get('duration');check(isinstance(d,int) and d>0,'Missing/nonpositive WebP duration')
  actual.append((t,t+d,a));t+=d
 check(t==expected_total,'Preview duration differs from fixed schedule')
 check(all(a.shape==(208,192,4) for _,_,a in actual),'Preview frame geometry')
 cuts=sorted({t for row in source+actual for t in row[:2]});si=ai=0;intervals=[]
 for start,end in zip(cuts,cuts[1:]):
  while source[si][1]<=start:si+=1
  while actual[ai][1]<=start:ai+=1
  s=source[si][2];a=actual[ai][2];visible=s[:,:,3]>0
  check(np.array_equal(s[:,:,3],a[:,:,3]),f'Preview alpha differs at {start}ms')
  check(np.array_equal(s[visible],a[visible]),f'Preview visible RGBA differs at {start}ms')
  intervals.append([start,end])
 return {'ok':True,'source_slots':len(frames),'encoded_frames':len(actual),'duration_ms':t,'validated_intervals_ms':intervals,'complete_alpha_exact':True,'visible_rgba_exact':True,'hidden_rgb_under_alpha_zero_not_compared':True,'sha256':sha(p)}

def source_provenance(e,r,before,context):
 count=r['count'];state=r['state'];source=path(r['source']);dest=rgba(r['strip'])
 if r['method']=='same-state-complete-frames':
  expected_source=next(x for x in e['rows'] if x['state']==state)['strip']
  check(source==path(expected_source),'Same-state mapping points to a different source row')
  source_im=rgba(source);check(source_im.tobytes()==before.tobytes(),'Mapped source strip differs from exact baseline row')
  mapping=r['mapping'];check(len(mapping)==count and all(type(v)is int and 0<=v<count for v in mapping),'Invalid complete-frame map')
  original=[source_im.crop((i*192,0,(i+1)*192,208)) for i in range(count)]
  expected=strip_of([original[i] for i in mapping])
  raw=source;source_hash=sha(source);record_path='inventory baseline atlas + original same-state strip';transform='direct complete-frame copy';raw_source_verified=True
 else:
  group=source.parts[-3]
  record=context['records'].get((e['id'],state))
  check(record is not None,'Missing raw-source provenance')
  raw=path(record['source']);check(raw.stem==state,'Raw source state differs')
  source_hash=sha(raw);check(source_hash==record['source_sha256'],'Raw original source hash differs')
  check(sha(source)==record['expected_output_sha256'],'Recorded extracted output hash differs')
  check(rgba(source).tobytes()==dest.tobytes(),'Candidate strip differs from recorded processed source')
  key=EXTRACT.parse_hex_color(record['chroma_key']);source_im=rgba(raw)
  count=EXTRACT.ROW_FRAME_COUNTS[state];kind=record['kind'];mapping=record.get('mapping',list(range(count)))
  if kind=='arc':
   check(r['method']=='source-arc-registration','Registered jump is selected under the wrong method')
   assembled=rebuild_registered_jump(record,e)
  elif kind=='generated':
   check(source_im.getchannel('A').getextrema()[0]==0,'Generated source lacks transparency')
   groups=EXTRACT.component_frame_groups(source_im,count);check(groups is not None and len(groups)==count,'Generated source pose count')
   boxes=[list(EXTRACT.component_bounds(g)) for g in groups]
   check(boxes==record['source_group_bounds'],'Generated source grouping no longer matches provenance')
   original=EXTRACT.extract_stable_slot_frames(source_im,count);assembled=strip_of(original)
  elif kind=='stable':
   source_im=EXTRACT.remove_chroma_background(source_im,key,record.get('key_threshold',96))
   original=EXTRACT.extract_stable_slot_frames(source_im,count);chosen=[original[i] for i in mapping]
   shifts=record.get('nonjump_ground_translation_dy_px',[0]*count)
   if state=='failed':
    moved=[]
    for f,dy in zip(chosen,shifts):
     canvas=Image.new('RGBA',(192,208));canvas.alpha_composite(f,(0,dy));moved.append(canvas)
    chosen=moved
   assembled=strip_of(chosen,composite=True)
  else:
   source_im=EXTRACT.remove_chroma_background(source_im,key,record.get('key_threshold',96))
   layout_path=path(record['layout']);layout=load(layout_path)[state]
   check(layout['source_sha256']==source_hash,'Reviewed layout not bound to actual source')
   original,extraction=EXTRACT.extract_reviewed_layout(source_im,count,layout,layout_path.parent)
   check(abs(extraction['shared_scale']-record['shared_scale'])<1e-12,'Shared source scale differs')
   assembled=strip_of(original)
  cleaned,cleanup=DESPILL.decontaminate_image(assembled,chroma_key=key)
  check(cleaned.getchannel('A').tobytes()==assembled.getchannel('A').tobytes(),'Despill altered alpha')
  if kind=='kafka':
   cleanframes=[cleaned.crop((i*192,0,(i+1)*192,208)) for i in range(count)]
   expected=strip_of([cleanframes[i] for i in mapping])
  else:expected=cleaned
  record_path=record['record_path'];transform=record['kind']+' + one in-memory edge despill';raw_source_verified=True
 check(expected.size==dest.size and expected.tobytes()==dest.tobytes(),'Recomputed whole-row RGBA differs from selected candidate')
 return {'ok':True,'source_path':str(raw.relative_to(ROOT)) if raw.is_relative_to(ROOT) else str(raw),'source_sha256':source_hash,'actual_source_sha256_verified':raw_source_verified,'source_state':state,'source_record':record_path,'source_frame_mapping':mapping,'transform':transform,'full_rgba_reconstructed_exactly':True,'frame_rgba_sha256':[digest(dest.crop((i*192,0,(i+1)*192,208))) for i in range(count)]}

def validate_edition(job):
 e,c,key,key_evidence,context=job;result={'id':e['id'],'checks':{},'rows':[],'errors':[]}
 try:
  baseline_path=path(e['atlas']);final_path=path(c['atlas'] if c else e['atlas']);manifest_path=path(e['manifest'])
  baseline_hash=sha(baseline_path);final_hash=sha(final_path)
  result.update({'baseline_atlas':e['atlas'],'final_atlas':str(final_path.relative_to(ROOT)),'baseline_sha256':baseline_hash,'final_sha256':final_hash,'changed':bool(c),'chroma_key':key,'chroma_key_evidence':key_evidence})
  check(baseline_hash==e['sha256'],'Release baseline hash changed')
  if c:check(c['baseline_sha256']==baseline_hash and c['sha256']==final_hash,'Candidate declared atlas hashes differ')
  git_atlas=subprocess.run(['git','show',context['baseline_commit']+':'+e['atlas']],cwd=ROOT,check=True,capture_output=True).stdout
  check(hashlib.sha256(git_atlas).hexdigest()==baseline_hash,'Inventory atlas differs from baseline commit')
  actual_manifest=manifest_path.read_bytes();git_manifest=subprocess.run(['git','show',context['baseline_commit']+':'+e['manifest']],cwd=ROOT,check=True,capture_output=True).stdout
  check(actual_manifest==git_manifest,'Manifest bytes differ from baseline commit')
  m=json.loads(actual_manifest);check(m['id']==e['id'] and m['spriteVersionNumber']==2,'Manifest ID/version mismatch')
  check((manifest_path.parent/m['spritesheetPath']).resolve()==baseline_path.resolve(),'Manifest spritesheetPath changed or wrong')
  result['manifest']={'path':e['manifest'],'sha256':hashlib.sha256(actual_manifest).hexdigest(),'baseline_commit_bytes_exact':True,'id':m['id'],'sprite_version_number':2,'spritesheet_path':m['spritesheetPath']}
  original=rgba(baseline_path);final=rgba(final_path);check(original.size==final.size==(1536,2288),'Atlas geometry mismatch')
  declared={r['row']:r['count'] for r in c['rows']} if c else {};check(len(declared)==len(c['rows'] if c else []),'Duplicate changed row')
  protected=[];changed=[]
  for row in range(11):
   for col in range(8):
    box=(col*192,row*208,(col+1)*192,(row+1)*208);same=original.crop(box).tobytes()==final.crop(box).tobytes()
    if row in declared and col<declared[row]:
     if not same:changed.append([row,col])
    else:check(same,f'Protected cell {row}:{col} changed');protected.append([row,col])
  if c:check(len(protected)==c['protected_cells'],'Protected cell count declaration incorrect')
  else:check(final_hash==baseline_hash,'Unmodified edition byte hash changed')
  result['scope']={'ok':True,'protected_cells':len(protected),'protected_full_rgba_exact':True,'protected_coordinates':protected,'actually_changed_cells':changed,'neutral_and_all_16_directions_exact':True}
  check(len(e['rows'])==9,'Inventory has wrong state count')
  for r in e['rows']:check((r['row'],r['count'],r['durations_ms'])==EXPECTED[r['state']],'Inventory differs from verified fixed frame/timing table')
  result['checks']['fixed_9_states_counts_and_timing']=True
  for r in (c['rows'] if c else []):
   rr={'state':r['state'],'row':r['row'],'count':r['count'],'method':r['method']};result['rows'].append(rr)
   try:
    check((r['row'],r['count'],r['durations_ms'])==EXPECTED[r['state']],'Candidate state/count/timing altered')
    count=r['count'];strip=rgba(r['strip']);check(strip.size==(count*192,208),'Candidate strip dimensions')
    check(sha(r['strip'])==r['sha256'],'Candidate strip SHA differs')
    in_atlas=final.crop((0,r['row']*208,count*192,(r['row']+1)*208));check(strip.tobytes()==in_atlas.tobytes(),'Atlas does not contain exact candidate row')
    frames=[strip.crop((i*192,0,(i+1)*192,208)) for i in range(count)];check(all(f.getchannel('A').getbbox() for f in frames),'Empty used frame')
    before=original.crop((0,r['row']*208,count*192,(r['row']+1)*208))
    rr.update({'strip_sha256':r['sha256'],'atlas_row_full_rgba_exact':True,'fixed_frame_count_preserved':True,'preview':preview_check(r['preview'],frames,r['durations_ms']),'provenance':source_provenance(e,r,before,context),'ok':True})
   except Exception as exc:rr.update({'ok':False,'error':str(exc)});result['errors'].append(r['state']+': '+str(exc))
  out=RUN/'technical-details'/f"{e['id']}.json";out.parent.mkdir(exist_ok=True)
  cmd=[str(PYTHON),str(SKILL/'validate_atlas.py'),str(final_path),'--require-v2','--chroma-key',key,'--json-out',str(out)]
  proc=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True)
  v=load(out) if out.exists() else {'ok':False,'errors':[proc.stderr[-2000:]]}
  result['hatch_validate_atlas']={'ok':v.get('ok',False),'exit_code':proc.returncode,'report':str(out.relative_to(ROOT)),'command':cmd,'errors':v.get('errors',[]),'warnings':v.get('warnings',[]),'transparent_rgb_residue_pixels':v.get('transparent_rgb_residue_pixels')}
  if proc.returncode or not v.get('ok'):result['errors'].append('hatch validate_atlas --require-v2 failed')
 except Exception as exc:result['errors'].append(str(exc))
 result['ok']=not result['errors'];return result

def source_records():
 rec={}
 for p,key,kind in [(RUN/'generated-strips/manifest.json',None,'generated'),(RUN/'reextracted-genshin-others/manifest.json','rows','stable'),(RUN/'reextracted-zzz-honkai/report.json','records','reviewed')]:
  document=load(p)
  for r in document if key is None else document[key]:
   v=dict(r);v['kind']=kind;v['record_path']=str(p.relative_to(ROOT));v['expected_output_sha256']=r.get('sha256',r.get('candidate_sha256'))
   if kind=='generated':v['chroma_key']=load(RUN/'generation'/r['id']/'pet_request.json')['chroma_key']['hex']
   if kind=='stable':v['mapping']=r['source_frame_mapping']
   if kind=='reviewed':v['shared_scale']=r['extraction']['shared_scale'];v['key_threshold']=r['chroma_removal_threshold'];v['mapping']=r['extraction']['source_frame_mapping']
   rec[r['id'],r['state']]=v
 p=RUN/'reextracted-star-honkai/kafka/manifest.json';d=load(p);x=d['extraction_manifest']['rows'][0]['extraction'];o=d['outputs']['failed-recovery']
 rec['kafka','failed']={'kind':'kafka','record_path':str(p.relative_to(ROOT)),'source':d['source_path'],'source_sha256':d['source_sha256'],'expected_output_sha256':o['sha256'],'chroma_key':d['chroma_key'],'key_threshold':d['key_threshold'],'layout':d['layout_file'],'shared_scale':x['shared_scale'],'mapping':o['source_frame_mapping']}
 p=RUN/'jump-registration-v2/manifest.json';d=load(p)
 check(sha(d['script'])==d['script_sha256'],'Jump registration script changed since output generation')
 check(len(d['rows'])==6,'Expected six registered jumping rows')
 for r in d['rows']:
  key=r['id'],r['state'];origin=rec[key]
  check(load(RUN/'jump-registration-v2'/r['id']/'manifest.json')==r,'Jump per-pet and batch manifests disagree')
  check(path(RUN/r['source_record'])==path(origin['record_path']),'Jump origin provenance record differs')
  rec[key]={**r,'kind':'arc','record_path':str(p.relative_to(ROOT)),'expected_output_sha256':r['candidate_sha256'],'mapping':r['source_frame_mapping'],'origin_record':origin}
 return rec

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--workers',type=int,default=4);args=parser.parse_args()
 check(Path(sys.executable).resolve()==PYTHON.resolve(),'Use the discovered bundled Python runtime')
 inv=load(RUN/'inventory.json');cand=load(RUN/'candidates.json');initial_sha=sha(RUN/'candidates.json');index={x['id']:x for x in cand['editions']}
 check('nicole-demara' in index and cand['changed_rows']==29,'Wait for complete Nicole-inclusive candidate manifest')
 check(len(inv['editions'])==48 and len(index)==18,'Unexpected final batch scope')
 jump_rows=[r for e in cand['editions'] for r in e['rows'] if r['state']=='jumping']
 check(len(jump_rows)==6 and all(r['method']=='source-arc-registration' for r in jump_rows),'Wait for all six registered jumping candidates')
 requests={}
 files=subprocess.run(['rg','--files','--hidden','-g','pet_request.json','work'],cwd=ROOT,capture_output=True,text=True,check=True).stdout.splitlines()
 for name in files:
  if '/motion-refinement-' in name:continue
  try:
   d=load(name);requests.setdefault(d['pet_id'],[]).append((name,d['chroma_key']['hex']))
  except (KeyError,json.JSONDecodeError):pass
 context={'baseline_commit':inv['baseline_commit'],'records':source_records()};jobs=[]
 for e in inv['editions']:
  choices=requests.get(e['id'],[])
  if choices:
   keys={x[1] for x in choices};check(len(keys)==1,'Ambiguous original chroma key: '+e['id']);key=choices[0][1];evidence=choices[0][0]
  else:
   evidence='work/'+e['id']+'/2d/qa/chroma-despill-extended.json';key=load(evidence)['chroma_key']
  jobs.append((e,index.get(e['id']),key,evidence,context))
 start=time.monotonic();results=[]
 with ProcessPoolExecutor(max_workers=args.workers) as executor:
  futures={executor.submit(validate_edition,j):j[0]['id'] for j in jobs}
  for f in as_completed(futures):
   r=f.result();results.append(r);print(f"{len(results):02}/48 {r['id']} {'PASS' if r['ok'] else 'FAIL'}",flush=True)
 order={e['id']:i for i,e in enumerate(inv['editions'])};results.sort(key=lambda x:order[x['id']])
 stable=sha(RUN/'candidates.json')==initial_sha;all_rows=[r for e in results for r in e['rows']]
 report={'ok':stable and all(x['ok'] for x in results),'reviewer':'final_motion_integrity technical-only independent validation','visual_approval':False,'baseline_commit':inv['baseline_commit'],'client_version':inv['client_version'],'candidate_manifest_sha256':initial_sha,'candidate_manifest_stable_during_validation':stable,'inventory_sha256':sha(RUN/'inventory.json'),'script_sha256':sha(Path(__file__)),'runtime':str(PYTHON),'duration_seconds':round(time.monotonic()-start,2),'scope':'48 final atlases: use selected candidate where changed, original published atlas otherwise; no packages or release files written','summary':{'editions':len(results),'edition_passes':sum(e['ok'] for e in results),'changed_editions':len(index),'changed_rows':len(all_rows),'changed_row_passes':sum(r.get('ok',False) for r in all_rows),'hatch_v2_passes':sum(e.get('hatch_validate_atlas',{}).get('ok',False) for e in results),'protected_full_rgba_cells':sum(e.get('scope',{}).get('protected_cells',0) for e in results),'manifest_byte_identity_passes':sum(e.get('manifest',{}).get('baseline_commit_bytes_exact',False) for e in results),'preview_timeline_passes':sum(r.get('preview',{}).get('ok',False) for r in all_rows),'source_reconstruction_passes':sum(r.get('provenance',{}).get('full_rgba_reconstructed_exactly',False) for r in all_rows)},'editions':results}
 (RUN/'technical-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'ok':report['ok'],**report['summary']},ensure_ascii=False),flush=True)
 raise SystemExit(0 if report['ok'] else 1)
if __name__=='__main__':main()

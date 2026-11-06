"""Trial only: recover original complete poses at a larger shared scale and compress their arc."""
from pathlib import Path
import json,hashlib,importlib.util
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[2];RUN=Path(__file__).resolve().parent;OUT=RUN/'jump-registration-v2';OUT.mkdir(exist_ok=True)
SKILL=Path('/home/ubuntu23/.codex/skills/hatch-pet/scripts')
def module(name):
 s=importlib.util.spec_from_file_location(name,SKILL/(name+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
ex=module('extract_strip_frames');ds=module('despill_chroma_edges')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def box16(im):return im.getchannel('A').point(lambda a:255 if a>16 else 0).getbbox()
inv=json.loads((RUN/'inventory.json').read_text());ed={e['id']:e for e in inv['editions']};cand=json.loads((RUN/'candidates.json').read_text());cc={e['id']:e for e in cand['editions']}
records={}
for file,key,kind in [('generated-strips/manifest.json',None,'transparent-groups'),('reextracted-genshin-others/manifest.json','rows','chroma-groups'),('reextracted-zzz-honkai/report.json','records','reviewed-cuts')]:
 document=json.loads((RUN/file).read_text())
 for r in document if key is None else document[key]:
  if r['state']=='jumping':records[r['id']]={**r,'kind':kind,'record_file':file}
all_results=[]
for id in ['kazuha-chibi','mitsuri-kanroji','obanai','raiden-mei','raiden-mei-3d','miyabi']:
 r=records[id];folder=OUT/id;folder.mkdir(exist_ok=True);src=ROOT/r['source'];assert sha(src)==r['source_sha256']
 source=Image.open(src).convert('RGBA');generated=r['kind']=='transparent-groups'
 key_hex=(json.loads((RUN/'generation'/id/'pet_request.json').read_text())['chroma_key']['hex'] if generated else r['chroma_key']);key=ex.parse_hex_color(key_hex)
 if not generated:source=ex.remove_chroma_background(source,key,96)
 poses=[];boxes=[];anchors=[];source_baseline=None
 if r['kind']=='reviewed-cuts':
  layout=json.loads((ROOT/r['layout']).read_text())['jumping'];cuts=layout['cuts'];assert layout['source_sha256']==sha(src)
  for i in range(5):
   left,right=cuts[i:i+2];pose=source.crop((left,0,right,source.height));b=pose.getchannel('A').getbbox();assert b
   poses.append(pose.crop(b));boxes.append([b[0]+left,b[1],b[2]+left,b[3]])
   anchors.append(layout['foot_anchors'][i][0])
  source_baseline=max(a[1] for a in layout['foot_anchors'])
 else:
  groups=ex.component_frame_groups(source,5);assert groups and len(groups)==5
  for group in groups:
   b=ex.component_bounds(group);poses.append(ex.component_group_image(source,group,padding=0));boxes.append(list(b));anchors.append((b[0]+b[2])/2)
  source_baseline=max(boxes[0][3],boxes[-1][3])
 # Approved neutral controls horizontal registration; a single maximum-pose height controls every frame.
 atlas=Image.open(ROOT/ed[id]['atlas']).convert('RGBA');neutral=atlas.crop((1152,0,1344,208));idle=atlas.crop((0,0,192,208));nb=box16(neutral)
 band=neutral.getchannel('A').crop((0,nb[3]-max(1,(nb[3]-nb[1])//8),192,nb[3]))
 weights=[sum(band.crop((x,0,x+1,band.height)).histogram()[17:]) for x in range(192)]
 target_x=sum(i*w for i,w in enumerate(weights))/sum(weights);target_ground=203;target_pose_height=185
 heights=[b[3]-b[1] for b in boxes];maxheight=max(heights)
 maxleft=max(a-b[0] for a,b in zip(anchors,boxes));maxright=max(b[2]-a for a,b in zip(anchors,boxes))
 scale=min(target_pose_height/maxheight,(target_x-5)/maxleft,(187-target_x)/maxright)
 scaled_heights=[round(h*scale) for h in heights]
 natural_lifts=[max(0,(source_baseline-b[3])*scale) for b in boxes]
 # The complete endpoint poses explicitly ground the start and finish. No limb or facial edits.
 natural_lifts[0]=natural_lifts[-1]=0
 limits=[(target_ground-5-h)/lift for h,lift in zip(scaled_heights,natural_lifts) if lift>0]
 compression=min(1,min(limits)) if limits else 0
 assert compression>=0
 lifts=[round(v*compression) for v in natural_lifts]
 frames=[];transforms=[]
 for i,(pose,b,a) in enumerate(zip(poses,boxes,anchors)):
  size=(round(pose.width*scale),round(pose.height*scale));x=round(target_x+(b[0]-a)*scale);y=target_ground-lifts[i]-size[1]
  assert 4<=x and x+size[0]<=188 and y>=4 and y+size[1]<=204,(id,i,x,y,size)
  frame=Image.new('RGBA',(192,208));frame.alpha_composite(pose.resize(size,Image.Resampling.LANCZOS),(x,y));frames.append(frame)
  # Translation in source-coordinate affine form, applied to the full source pose only.
  transforms.append({'frame':i,'source_box':b,'source_anchor_x':a,'shared_scale':scale,'scaled_size':list(size),'destination_xy':[x,y],'source_to_cell_translation_xy':[x-b[0]*scale,y-b[1]*scale],'natural_lift_after_scale_px':natural_lifts[i],'compressed_lift_px':lifts[i],'target_bottom_y':target_ground-lifts[i]})
 strip=Image.new('RGBA',(960,208))
 for i,f in enumerate(frames):strip.paste(f,(i*192,0))
 clean,despill=ds.decontaminate_image(strip,chroma_key=key);assert clean.getchannel('A').tobytes()==strip.getchannel('A').tobytes();dest=folder/'jumping.png';clean.save(dest)
 fclean=[clean.crop((i*192,0,(i+1)*192,208)) for i in range(5)];fclean[0].save(folder/'jumping.webp',save_all=True,append_images=fclean[1:],duration=[140]*4+[280],loop=0,lossless=True,exact=True)
 before=Image.open(ROOT/next(x for x in cc[id]['rows'] if x['state']=='jumping')['strip']).convert('RGBA');original=atlas.crop((0,4*208,960,5*208))
 neutral.save(folder/'neutral-reference.png');idle.save(folder/'idle-reference.png')
 contact=Image.new('RGB',(960,4*244),'#eeeae3');d=ImageDraw.Draw(contact)
 d.text((8,5),id+' | references (idle / neutral) at native 192x208',fill='#222222');contact.paste(idle,(0,28),idle);contact.paste(neutral,(192,28),neutral)
 for row,(label,im) in enumerate([('PUBLISHED ORIGINAL JUMP',original),('CURRENT CANDIDATE / source arc fitted as one viewport',before),('V2 TRIAL / shared body scale + compressed whole-frame arc',clean)],1):
  yy=row*244;d.text((8,yy+5),label,fill='#222222')
  for i in range(5):d.rectangle((i*192,yy+28,(i+1)*192-1,yy+235),fill='#faf8f4' if i%2==0 else '#dedad3')
  contact.paste(im,(0,yy+28),im)
 contact.save(folder/'comparison.png')
 # Preview the real issue under review: neutral -> 3 jump loops -> neutral, not an unbounded jump-only loop.
 seq=[neutral]+fclean*3+[neutral];times=[900]+([140]*4+[280])*3+[1200]
 seq[0].save(folder/'jump-to-neutral.webp',save_all=True,append_images=seq[1:],duration=times,loop=0,lossless=True,exact=True)
 result={'id':id,'state':'jumping','status':'pending-independent-visual-QA','method':'complete-original-pose/shared-scale/compressed-source-arc','source':r['source'],'source_sha256':sha(src),'source_method':r['kind'],'source_record':r['record_file'],'source_boxes':boxes,'source_baseline_y':source_baseline,'source_frame_mapping':[0,1,2,3,4],'neutral_atlas':ed[id]['atlas'],'neutral_atlas_sha256':ed[id]['sha256'],'neutral_reference':str((folder/'neutral-reference.png').relative_to(ROOT)),'neutral_reference_sha256':sha(folder/'neutral-reference.png'),'shared_scale':scale,'target_max_pose_height_px':target_pose_height,'actual_max_pose_height_px':max(scaled_heights),'target_ground_y':203,'source_arc_compression_factor':compression,'natural_scaled_lifts_px':natural_lifts,'final_lifts_px':lifts,'translations':transforms,'arc_peak_lift_at_least_10px':max(lifts)>=10,'chroma_key':key_hex,'chroma_removal':not generated,'despill_passes':1,'despill':despill,'alpha_preserved_during_despill':True,'candidate':str(dest.relative_to(ROOT)),'candidate_sha256':sha(dest),'bounds_alpha_gt16':[list(box16(f)) for f in fclean],'comparison':str((folder/'comparison.png').relative_to(ROOT)),'transition_preview':str((folder/'jump-to-neutral.webp').relative_to(ROOT)),'release_assets_edited':False}
 (folder/'manifest.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');all_results.append(result)
 print(id,'scale',round(scale,4),'height',max(scaled_heights),'lift',lifts,'compression',round(compression,3),flush=True)
(OUT/'manifest.json').write_text(json.dumps({'status':'trial-not-selected','script':str(Path(__file__).relative_to(ROOT)),'script_sha256':sha(Path(__file__)),'rows':all_results},ensure_ascii=False,indent=2)+'\n')

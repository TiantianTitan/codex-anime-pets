import json,sys
from pathlib import Path
import numpy as np
from PIL import Image
sys.path.insert(0,'/home/ubuntu23/.codex/skills/hatch-pet/scripts')
import extract_strip_frames as x
jobs=[('raiden-mei','2d','jumping',5),('raiden-mei','2d','failed',8),('raiden-mei','2d','waiting',6),('raiden-mei','3d','jumping',5),('raiden-mei','3d','waiting',6),('raiden-mei','3d','running',6),('miyabi','2d','jumping',5)]
for pet,sty,state,n in jobs:
 p=Path(f'work/{pet}/{sty}/decoded/{state}.png');im=Image.open(p);key=(255,0,255) if pet=='miyabi' else (0,255,0)
 clean=x.remove_chroma_background(im,key,96);a=np.array(clean)[:,:,3]>16
 print('\n',pet,sty,state,im.size,'bbox',clean.getbbox())
 cuts=[0]
 for i in range(1,n):
  c=round(im.width*i/n);lo=c-75;hi=c+75;counts=a[:,lo:hi].sum(0);minimum=counts.min();opts=np.where(counts==minimum)[0]+lo;chosen=opts[np.argmin(abs(opts-c))];cuts.append(int(chosen))
 cuts.append(im.width);print('cuts',cuts,'occupancy',[int(a[:,c].sum()) for c in cuts[1:-1]])
 for i,(l,r) in enumerate(zip(cuts,cuts[1:])):
  crop=clean.crop((l,0,r,im.height));box=crop.getbbox();bb=np.array(crop)[:,:,3]>16;foot=bb[max(0,box[3]-35):box[3]];xs=np.where(foot)[1];print(i,box,'foot_x',round(xs.mean()+l,1),'components',[(c['area'],c['bbox']) for c in x.connected_components(crop) if c['area']>30])

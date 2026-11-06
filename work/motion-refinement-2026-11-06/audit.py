from pathlib import Path
import hashlib
import json
import subprocess

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
RUN = Path(__file__).resolve().parent
GROUPS = ['genshin-impact', 'honkai-star-rail', 'honkai-impact-3rd', 'zenless-zone-zero', 'others']
STATES = ['idle', 'running-right', 'running-left', 'waving', 'jumping', 'failed', 'waiting', 'running', 'review']
COUNTS = [6, 8, 8, 4, 5, 8, 6, 6, 6]
DURATIONS = [[1680,660,660,840,840,1920], [120]*7+[220], [120]*7+[220], [140]*3+[280], [140]*4+[280], [140]*7+[240], [150]*5+[260], [120]*5+[220], [150]*5+[280]]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    (RUN/'contacts').mkdir(parents=True, exist_ok=True)
    (RUN/'rows').mkdir(exist_ok=True)
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 15)
    editions = []
    for group in GROUPS:
        for manifest in sorted((ROOT/group).rglob('pet.json')):
            pet = json.loads(manifest.read_text())
            path = manifest.parent/pet['spritesheetPath']
            atlas = Image.open(path).convert('RGBA')
            slug = pet['id']
            rows = []
            contact = Image.new('RGB', (1536, 9*234+35), '#e9e7e1')
            draw = ImageDraw.Draw(contact)
            draw.text((8, 8), slug+' | current release | fixed client timing', font=font, fill='#151515')
            for row, (state, count) in enumerate(zip(STATES, COUNTS)):
                cells = [atlas.crop((c*192,row*208,(c+1)*192,(row+1)*208)) for c in range(count)]
                normalized = []
                bounds = []
                hashes = []
                for cell in cells:
                    a = np.asarray(cell)
                    y, x = np.where(a[:,:,3] >= 64)
                    bounds.append([int(x.min()),int(y.min()),int(x.max()+1),int(y.max()+1)] if len(x) else None)
                    hashes.append(hashlib.sha256(cell.tobytes()).hexdigest())
                    small = np.asarray(cell.resize((48,52), Image.Resampling.LANCZOS), dtype=np.float32)/255
                    normalized.append(np.concatenate((small[:,:,:3]*small[:,:,3:4],small[:,:,3:4]),axis=2))
                distances = [[round(float(np.abs(a-b).mean()),6) for b in normalized] for a in normalized]
                jumps = [distances[i][(i+1)%count] for i in range(count)]
                seam_ratio = jumps[-1]/max(float(np.median(jumps[:-1])),0.0001)
                strip = atlas.crop((0,row*208,count*192,(row+1)*208))
                strip_path = RUN/'rows'/f'{slug}--{state}.png'
                strip.save(strip_path)
                title = f'{row}: {state} | {count} slots | seam/median {seam_ratio:.2f} | distinct {len(set(hashes))}'
                yy = 35+row*234
                draw.text((8,yy+2),title,font=font,fill='#151515')
                for c,cell in enumerate(cells):
                    xx=c*192
                    draw.rectangle((xx,yy+25,xx+191,yy+232), fill=('#f8f7f3' if c%2==0 else '#dedcd6'))
                    contact.paste(cell,(xx,yy+25),cell)
                rows.append({'row':row,'state':state,'count':count,'durations_ms':DURATIONS[row], 'bounds':bounds,'unique_frames':len(set(hashes)), 'distances':distances,'cyclic_distances':jumps,'seam_ratio':round(seam_ratio,3),'strip':str(strip_path.relative_to(ROOT))})
            contact_path = RUN/'contacts'/f'{slug}.jpg'
            contact.save(contact_path,quality=92)
            candidates = []
            base_id=slug.removesuffix('-3d')
            style='3d' if slug.endswith('-3d') else '2d'
            for state in STATES:
                candidate=ROOT/'work'/base_id/style/'decoded'/f'{state}.png'
                if candidate.exists(): candidates.append(str(candidate.relative_to(ROOT)))
            editions.append({'id':slug,'name':pet['displayName'],'group':group,'manifest':str(manifest.relative_to(ROOT)), 'atlas':str(path.relative_to(ROOT)),'sha256':sha(path),'contact':str(contact_path.relative_to(ROOT)),'available_decoded_strips':candidates,'rows':rows})
    report={'baseline_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'client_version':'26.1007.21434','editions':editions,'edition_count':len(editions),'action_count':len(editions)*9,'note':'Numeric candidates require native-size visual review. Deliberate jumping, gait, gesture and expression changes are not alignment defects.'}
    (RUN/'inventory.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    candidates=sorted([{'id':p['id'],'state':r['state'],'seam_ratio':r['seam_ratio'],'seam':r['cyclic_distances'][-1]} for p in editions for r in p['rows'] if r['state']!='idle' and r['seam_ratio']>2 and r['cyclic_distances'][-1]>.03], key=lambda r:-r['seam_ratio'])
    print(json.dumps({'edition_count':len(editions),'action_count':len(editions)*9,'seam_candidates':candidates[:35],'available_source_count':sum(len(p['available_decoded_strips']) for p in editions)},ensure_ascii=False))

if __name__=='__main__': main()

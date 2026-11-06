#!/usr/bin/env python3
"""Register generated repair rows, clean their edges, and preserve approved cells."""
from __future__ import annotations
import hashlib
import argparse
import json
import subprocess
import sys
import zipfile
from io import BytesIO
from pathlib import Path
from PIL import Image, ImageDraw

ROOT=Path(__file__).resolve().parents[1]
RUN=ROOT/'work/motion-optimization-2026-11-06'
SKILL=Path('/home/ubuntu23/.codex/skills/hatch-pet/scripts')
PETS=[('xiao','genshin-impact/xiao/xiao-2d'),('dan-heng-imbibitor-lunae','honkai-star-rail/dan-heng-imbibitor-lunae/dan-heng-imbibitor-lunae-2d'),('jing-yuan','honkai-star-rail/jing-yuan/jing-yuan-2d')]

def baseline_atlas(source):
    data=subprocess.check_output(['git','show',f'0a7cb6dea9bdbcc476843bf3f07892f6b47acaa1:{source}/spritesheet.webp'],cwd=ROOT)
    return Image.open(BytesIO(data)).convert('RGBA')

def cell(im,row,col):return im.crop((col*192,row*208,(col+1)*192,(row+1)*208))
def foot_anchor(im):
    box=im.getchannel('A').getbbox()
    if not box:raise ValueError('empty sprite')
    a=im.getchannel('A');ys=range(max(box[1],box[3]-25),box[3]);points=[(x,a.getpixel((x,y))) for y in ys for x in range(box[0],box[2]) if a.getpixel((x,y))>128]
    return sum(x*v for x,v in points)/sum(v for _,v in points)

def register(frames,neutral):
    boxes=[im.getchannel('A').getbbox() for im in frames]
    union=(min(b[0] for b in boxes),min(b[1] for b in boxes),max(b[2] for b in boxes),max(b[3] for b in boxes))
    target=neutral.getchannel('A').getbbox();source_x=sum(foot_anchor(im) for im in frames)/len(frames);target_x=foot_anchor(neutral)
    scale=min((target[3]-target[1])/(union[3]-union[1]),(target_x-5)/max(1,source_x-union[0]),(187-target_x)/max(1,union[2]-source_x))
    left=round(target_x-(source_x-union[0])*scale);top=round(target[3]-(union[3]-union[1])*scale)
    size=(max(1,round((union[2]-union[0])*scale)),max(1,round((union[3]-union[1])*scale)))
    result=[]
    for im in frames:
        canvas=Image.new('RGBA',(192,208));crop=im.crop(union).resize(size,Image.Resampling.LANCZOS);canvas.alpha_composite(crop,(left,top));result.append(canvas)
    return result,{'sourceUnion':union,'targetNeutralBox':target,'scale':scale,'offset':[left,top],'method':'one shared scale and baseline per complete row; no anatomy deformation'}

def invoke(script,*args):
    p=subprocess.run([sys.executable,str(SKILL/script),*map(str,args)],capture_output=True,text=True)
    if p.returncode:raise RuntimeError(script+'\n'+p.stdout+'\n'+p.stderr)

def build_idle_candidates():
    """Package the demonstrated blink fix; keep working-pose exploration separate."""
    packages=RUN/'packages-idle-only';packages.mkdir(exist_ok=True)
    for slug,source in PETS:
        run=RUN/slug;final=run/'final';qa=run/'qa'
        approved=json.loads((qa/'candidate-validation.json').read_text())
        if not approved.get('ok') or approved.get('visualReview')!='pass':
            raise RuntimeError(f'{slug}: the existing idle artwork must pass review first')
        original=baseline_atlas(source)
        reviewed=Image.open(final/'spritesheet-optimized.webp').convert('RGBA')
        candidate=original.copy()
        for c in range(6):candidate.paste(cell(reviewed,0,c),(c*192,0))
        output=final/'spritesheet-idle-only.webp'
        candidate.save(output,lossless=True,quality=100,method=6,exact=True)
        invoke('validate_atlas.py',output,'--require-v2','--json-out',qa/'idle-only-atlas-validation.json')
        decoded=Image.open(output).convert('RGBA')
        for r in range(11):
            for c in range(8):
                expected=reviewed if r==0 and c<6 else original
                if cell(decoded,r,c).tobytes()!=cell(expected,r,c).tobytes():
                    raise RuntimeError(f'{slug}: unexpected pixel change at {r},{c}')
        report={'ok':True,'scope':'idle-only','sourceCommit':approved['sourceCommit'],
            'editedCells':[[0,c] for c in range(6)],'preservedCellCount':82,'preservedUsedCellCount':68,
            'visualReview':'pass','visualReviewSource':'Six idle cells reused byte-for-byte from the previously approved candidate.',
            'workingRow':'pixel-identical to original release',
            'sha256':hashlib.sha256(output.read_bytes()).hexdigest()}
        (qa/'idle-only-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
        manifest=json.loads((ROOT/source/'pet.json').read_text());manifest['id']=slug+'-idle-candidate'
        manifest['displayName']+=' · 待机候选';manifest['description']+=' Open-eye idle candidate; other states retain the original artwork.'
        readme=f'# {manifest["displayName"]}\n\n仅修复慢速待机的长时间闭眼。只替换第 0 行前六格，其他 82 格（含 68 个已用格）与原版逐像素一致；工作姿态保持原版。\n\n安装：解压到 CODEX_HOME/pets/{manifest["id"]}/（默认 ~/.codex/pets/），确保 pet.json 直接位于该目录中。随后在 Settings > Pets 中 Refresh，选择角色，用 /pet 显示。\n\nv2 / 1536×2288 RGBA。候选使用独立 ID，可与原版并存。\n'
        with zipfile.ZipFile(packages/f'{slug}-idle-candidate.zip','w',zipfile.ZIP_DEFLATED) as z:
            z.writestr('pet.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
            z.writestr('spritesheet.webp',output.read_bytes());z.writestr('README.md',readme)
        print(slug,'idle-only PASS; 82 cells preserved')

def main():
    packages=RUN/'packages';packages.mkdir(exist_ok=True)
    combined=Image.new('RGB',(6*192+128,3*(4*208+60)), '#f4f3eb');draw=ImageDraw.Draw(combined)
    for index,(slug,source) in enumerate(PETS):
        run=RUN/slug;final=run/'final';final.mkdir(exist_ok=True);qa=run/'qa';qa.mkdir(exist_ok=True)
        original=baseline_atlas(source);neutral=cell(original,0,6);raw=original.copy();registration={}
        for state,row in [('idle',0),('running',7)]:
            fs=[Image.open(run/f'qa/rows/{state}/frames/{state}/{i:02}.png').convert('RGBA') for i in range(6)]
            fs,registration[state]=register(fs,neutral)
            for i,im in enumerate(fs):raw.paste(im,(i*192,row*208))
        raw.save(final/'repair-assembled.png')
        key=json.loads((run/'pet_request.json').read_text())['chroma_key']['hex']
        invoke('despill_chroma_edges.py',final/'repair-assembled.png','--output',final/'repair-cleaned.png','--chroma-key',key,'--json-out',qa/'chroma-despill-repairs.json')
        cleanup=json.loads((qa/'chroma-despill-repairs.json').read_text());assert cleanup['ok']
        cleaned=Image.open(final/'repair-cleaned.png').convert('RGBA')
        # Approved source cells were already cleaned in their original release. Reuse
        # their exact RGBA bytes; only copy the twelve newly cleaned repair cells.
        candidate=original.copy()
        changed={(r,c) for r in [0,7] for c in range(6)}
        for r,c in changed:candidate.paste(cell(cleaned,r,c),(c*192,r*208))
        candidate.save(final/'spritesheet-optimized.webp',lossless=True,quality=100,method=6,exact=True)
        invoke('validate_atlas.py',final/'spritesheet-optimized.webp','--require-v2','--chroma-key',key,'--json-out',qa/'atlas-validation.json')
        restored=Image.open(final/'spritesheet-optimized.webp').convert('RGBA');preserved=[]
        for r in range(11):
            for c in range(8):
                if (r,c) not in changed:
                    assert cell(original,r,c).tobytes()==cell(restored,r,c).tobytes(),(slug,r,c)
                    preserved.append([r,c])
        validation=json.loads((qa/'atlas-validation.json').read_text());assert validation['ok']
        report={'ok':True,'sourceCommit':'0a7cb6dea9bdbcc476843bf3f07892f6b47acaa1','sourcePath':source,'dimensions':[1536,2288],'spriteVersionNumber':2,'generatedFrames':12,'editedCells':sorted([list(x) for x in changed]),'preservedCellCount':len(preserved),'preservedUsedCellCount':62,'neutralAndDirections':'pixel-identical to approved source','registration':registration,'sha256':hashlib.sha256((final/'spritesheet-optimized.webp').read_bytes()).hexdigest(),'visualReview':'pending'}
        (qa/'candidate-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
        manifest=json.loads((ROOT/source/'pet.json').read_text());manifest['id']=slug+'-motion-candidate';manifest['displayName']+=' · Motion 候选';manifest['description']+=' Motion study candidate: open-eye idle and distinct working gestures.'
        (final/'pet.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
        readme=f'# {manifest["displayName"]}\n\nLocal review candidate from GitHub main 0a7cb6d, 2026-11-06.\n\nOnly idle row 0 columns 0–5 and running row 7 columns 0–5 are redrawn with built-in ImageGen. All other cells, including neutral and the 16 look directions, are pixel-identical to the approved original.\n\nThis package does not change client timing or enable persistent state loops. Version 2, 1536×2288 RGBA. Use the independent ID {manifest["id"]} to compare alongside the original.\n'
        with zipfile.ZipFile(packages/f'{slug}-motion-candidate.zip','w',zipfile.ZIP_DEFLATED) as z:
            z.writestr('pet.json',(final/'pet.json').read_bytes());z.writestr('spritesheet.webp',(final/'spritesheet-optimized.webp').read_bytes());z.writestr('README.md',readme)
        invoke('make_contact_sheet.py',final/'spritesheet-optimized.webp','--output',qa/'contact-sheet-optimized.png')
        for n,(label,image,row) in enumerate([('A idle',original,0),('B idle',candidate,0),('A running',original,7),('B running',candidate,7)]):
            y=index*(4*208+60)+n*208+35;draw.text((8,y+30),slug if n==0 else label,fill='#1b302f')
            if n==0:draw.text((8,y+65),label,fill='#1b302f')
            for c in range(6):combined.paste(cell(image,row,c),(128+c*192,y),cell(image,row,c))
        print(slug,'PASS','preserved cells:',len(preserved),'candidate bytes:',(final/'spritesheet-optimized.webp').stat().st_size)
    combined.save(RUN/'comparison-contact-sheet.png')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--idle-only',action='store_true',help='Reuse approved idle cells and package only the demonstrated blink fix.')
    args=parser.parse_args()
    if args.idle_only:build_idle_candidates()
    else:main()

#!/usr/bin/env python3
"""Build the offline, self-contained comparison from immutable release baselines."""
from __future__ import annotations
import argparse
import base64
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'scripts/motion-review'
RUN = ROOT / 'work/motion-optimization-2026-11-06'
BASELINE = '0a7cb6dea9bdbcc476843bf3f07892f6b47acaa1'
CHARACTERS = [
    ('xiao','魈','XIAO','genshin-impact/xiao/xiao-2d'),
    ('dan-heng-imbibitor-lunae','丹恒·饮月','DAN HENG','honkai-star-rail/dan-heng-imbibitor-lunae/dan-heng-imbibitor-lunae-2d'),
    ('jing-yuan','景元','JING YUAN','honkai-star-rail/jing-yuan/jing-yuan-2d'),
]

def uri(path: Path, mime: str) -> str:
    return f'data:{mime};base64,' + base64.b64encode(path.read_bytes()).decode('ascii')

def build(draft: bool = False) -> Path:
    pets=[]
    for slug,name,english,source in CHARACTERS:
        run=RUN/slug
        original_bytes=subprocess.check_output(['git','show',f'{BASELINE}:{source}/spritesheet.webp'],cwd=ROOT)
        original_uri='data:image/webp;base64,'+base64.b64encode(original_bytes).decode('ascii')
        candidate=run/'final/spritesheet-optimized.webp'
        report=run/'qa/candidate-validation.json'
        package=RUN/'packages-idle-only'/f'{slug}-idle-candidate.zip'
        package_report=run/'qa/idle-only-validation.json'
        ready=candidate.is_file() and report.is_file() and package.is_file() and package_report.is_file()
        qa=json.loads(report.read_text()) if report.is_file() else {}
        package_qa=json.loads(package_report.read_text()) if package_report.is_file() else {}
        if ready and not qa.get('ok'):raise RuntimeError(f'{slug}: failed candidate validation')
        if ready and qa.get('visualReview') != 'pass':raise RuntimeError(f'{slug}: visual review is incomplete')
        if ready and not (package_qa.get('ok') and package_qa.get('scope')=='idle-only'):raise RuntimeError(f'{slug}: download scope is incorrect')
        if not ready and not draft:raise RuntimeError(f'{slug}: candidate is incomplete')
        pets.append({'id':slug,'name':name,'english':english,'ready':ready,
          'beforeAtlas':original_uri,'afterAtlas':uri(candidate,'image/webp') if ready else original_uri,
          'package':uri(package,'application/zip') if ready else None,
          'packageFilename':package.name,'packageQa':package_qa,
          'source':source,'sha256Original':hashlib.sha256(original_bytes).hexdigest(),'qa':qa})
    content={'commit':'0a7cb6dea9bdbcc476843bf3f07892f6b47acaa1','clientVersion':'26.1007.21434','pets':pets,
      'qaSummary':'下载包仅替换待机六格，共 18 帧；每位角色其余 82 格（含 68 个已用格）逐像素保留。三份包均通过 v2 结构检查。工作姿态候选只供页面比较，未纳入下载。' if all(p['ready'] for p in pets) else '正在准备待机优化包。'}
    html=(SOURCE/'index.template.html').read_text()
    html=html.replace('/* INLINE_CSS */',(SOURCE/'style.css').read_text())
    html=html.replace('/* INLINE_DATA */',json.dumps(content,ensure_ascii=False,separators=(',',':')).replace('</','<\\/'))
    html=html.replace('/* INLINE_JS */',(SOURCE/'player.js').read_text())
    out=ROOT/'output/pet-motion-comparison.html';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(html)
    print(json.dumps({'html':str(out),'bytes':out.stat().st_size,'ready':all(p['ready'] for p in pets)},ensure_ascii=False))
    return out

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--draft',action='store_true');args=parser.parse_args();build(args.draft)

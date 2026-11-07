"""Consolidate only adopted rows, then run standard-atlas diagnostics."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

RUN=Path(__file__).resolve().parents[1]
SKILL=Path('/home/ubuntu23/.codex/skills/hatch-pet/scripts')
states=['idle','running-right','running-left','waving','jumping','failed','waiting','running','review']
jobs=json.loads((RUN/'imagegen-jobs.json').read_text())['jobs']
assert all(next(job for job in jobs if job['id']==state)['status']=='complete' for state in states)
manifest_path=RUN/'frames/frames-manifest.json'
manifest=json.loads(manifest_path.read_text())
assert {row['state'] for row in manifest['rows']}==set(states)
manifest['rows'].sort(key=lambda row:states.index(row['state']))
assert all(row.get('review_note') for row in manifest['rows'])
manifest_path.write_text(json.dumps(manifest,indent=2)+'\n')
(RUN/'final').mkdir(exist_ok=True)
commands=[
    ['inspect_frames.py','--frames-root',str(RUN/'frames'),'--json-out',str(RUN/'qa/review.json')],
    ['compose_atlas.py','--frames-root',str(RUN/'frames'),'--output',str(RUN/'final/spritesheet.png'),'--webp-output',str(RUN/'final/spritesheet.webp')],
    ['make_contact_sheet.py',str(RUN/'final/spritesheet.webp'),'--output',str(RUN/'qa/contact-sheet.png')],
    ['render_animation_previews.py','--frames-root',str(RUN/'frames'),'--output-dir',str(RUN/'qa/previews')]
]
for script,*args in commands:
    subprocess.run([sys.executable,str(SKILL/script),*args],check=True,stdout=subprocess.DEVNULL)
review=json.loads((RUN/'qa/review.json').read_text())
assert not review['errors']
report={'ok':True,'reviewed_by':'parent native-size ordered frames and source silhouettes',
    'motion_preview_basis':'Pre-despill source-table GIF timing only; final previews use version-qualified client holds',
    'rows':[{'state':row['state'],'source_sha256':row['source_sha256'],'method':row['method'],'review_note':row['review_note']} for row in manifest['rows']],
    'atlas_sha256':hashlib.sha256((RUN/'final/spritesheet.webp').read_bytes()).hexdigest(),
    'extraction_warnings':'Shared grounded/jump registration and stable gait viewport deliberately reviewed to preserve anatomy and movement; no structural errors.'}
(RUN/'qa/standard-visual-review.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'ok':True,'standard_rows':9,'frames':sum(len(row['frames']) for row in manifest['rows']),'errors':review['errors']}))

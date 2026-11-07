"""Assemble v2, clean chroma once, and produce exact-final QA evidence."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

RUN=Path(__file__).resolve().parents[1]
SKILL=Path('/home/ubuntu23/.codex/skills/hatch-pet/scripts')
def call(script,*args):
    result=subprocess.run([sys.executable,str(SKILL/script),*map(str,args)],capture_output=True,text=True)
    if result.returncode:
        print(result.stdout+result.stderr)
        raise SystemExit(result.returncode)

gate=json.loads((RUN/'qa/look-row-9-gate.json').read_text())
assert gate['ok'] and hashlib.sha256((RUN/'decoded/look-row-9.png').read_bytes()).hexdigest()==gate['source_sha256']
cleanup=RUN/'qa/chroma-despill-extended.json'
assert not cleanup.exists(), 'Final despill already performed; resume validation without another cleanup pass'
call('assemble_extended_atlas.py', '--base-atlas',RUN/'final/spritesheet.webp',
     '--registered-row-9',RUN/'qa/look-row-9-registered.png','--row-9-registration',RUN/'qa/look-row-9-registration.json',
     '--look-row-10',RUN/'decoded/look-row-10.png','--neutral-cell',RUN/'frames/idle/00.png',
     '--chroma-key','#FF00FF','--chroma-threshold','96','--output',RUN/'final/spritesheet-extended.png',
     '--webp-output',RUN/'final/spritesheet-extended.webp','--manifest-output',RUN/'final/spritesheet-extended.json')
shutil.copy2(RUN/'final/spritesheet-extended.png',RUN/'qa/atlas-pre-despill.png')
call('despill_chroma_edges.py',RUN/'final/spritesheet-extended.png','--output',RUN/'final/spritesheet-extended.png',
     '--webp-output',RUN/'final/spritesheet-extended.webp','--chroma-key','#FF00FF','--json-out',cleanup)
assert json.loads(cleanup.read_text())['ok']
call('validate_atlas.py',RUN/'final/spritesheet-extended.webp','--require-v2','--chroma-key','#FF00FF',
     '--json-out',RUN/'final/validation-extended.json')
call('make_contact_sheet.py',RUN/'final/spritesheet-extended.webp','--output',RUN/'qa/contact-sheet-extended.png')
call('make_direction_qa_sheet.py',RUN/'final/spritesheet-extended.webp','--output',RUN/'qa/look-directions.png')
call('render_final_animation_previews.py','--atlas',RUN/'final/spritesheet-extended.webp','--format','webp',
     '--idle-durations-ms','1680,660,660,840,840,1920','--client-version','26.1007.21434',
     '--timing-evidence','2026-11-06 repository local Desktop evidence in docs/pet-compatibility-2026-11-06.md and docs/pet-motion-refinement-2026-11-06.md; not a live installation of this pet',
     '--output-dir',RUN/'qa/previews-final','--json-out',RUN/'qa/preview-validation.json')
call('make_direction_blind_qa_sheet.py',RUN/'final/spritesheet-extended.webp','--output',RUN/'qa/direction-blind-pairs.png',
     '--answer-key',RUN/'qa/direction-blind-answer-key.json')
call('measure_direction_continuity.py',RUN/'final/spritesheet-extended.webp','--json-out',RUN/'qa/look-continuity.json')
subprocess.run([sys.executable,str(RUN/'qa/build-final-motion-review.py')],check=True)
subprocess.run([sys.executable,str(RUN/'qa/verify-source-reconstruction.py')],check=True)
validation=json.loads((RUN/'final/validation-extended.json').read_text())
print(json.dumps({'ok':validation['ok'],'atlas_sha256':hashlib.sha256((RUN/'final/spritesheet-extended.webp').read_bytes()).hexdigest(),
                  'errors':validation['errors'],'warnings':validation['warnings']}))

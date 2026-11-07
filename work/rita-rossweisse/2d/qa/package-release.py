"""Create only the hash-approved 2D product and flat ZIP, then test temporary installation."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
from zipfile import ZipFile, ZIP_DEFLATED

RUN = Path(__file__).resolve().parents[1]
ROOT = RUN.parents[2]
PARENT = ROOT/'honkai-impact-3rd/Rita Rossweisse'
PRODUCT = PARENT/'rita-rossweisse-2d'
ZIP = PARENT/'rita-rossweisse-2d-codex-pet-v2.zip'
ATLAS = RUN/'final/spritesheet-extended.webp'
QA = RUN/'qa'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


visual = json.loads((QA/'final-visual-qa.json').read_text())
assert visual['visual_qa']=='pass' and visual['atlas_sha256']==sha(ATLAS)
for name in ('generation-provenance.json','source-reconstruction.json','preview-validation.json',
             'transition-validation.json','direction-semantics.json','direction-blind-validation.json'):
    report = json.loads((QA/name).read_text())
    assert report.get('ok',True), name
assert json.loads((RUN/'final/validation-extended.json').read_text())['ok']
assert not PRODUCT.exists() and not ZIP.exists(), 'Preflight: preserve existing products; inspect before replacement'
assert not list(PARENT.iterdir()), 'Product parent must be empty after moving references'
PRODUCT.mkdir()
shutil.copy2(ATLAS, PRODUCT/'spritesheet.webp')
shutil.copy2(QA/'release-readme.md', PRODUCT/'README.md')
manifest = {'id':'rita-rossweisse','displayName':'Rita Rossweisse',
    'description':'An elegant maid with an ash-brown bob, a wine-red eye, and a rose-trimmed headband.',
    'spriteVersionNumber':2,'spritesheetPath':'spritesheet.webp'}
(PRODUCT/'pet.json').write_text(json.dumps(manifest,indent=2)+'\n')
with ZipFile(ZIP,'x',ZIP_DEFLATED) as package:
    for name in ('pet.json','spritesheet.webp','README.md'):
        package.write(PRODUCT/name,name)
subprocess.run([sys.executable,'/home/ubuntu23/.codex/skills/hatch-pet/scripts/validate_atlas.py',
    str(PRODUCT/'spritesheet.webp'),'--require-v2','--chroma-key','#00FF00',
    '--package-zip',str(ZIP),'--manifest',str(PRODUCT/'pet.json'),
    '--review-json',str(QA/'final-visual-qa.json'),'--json-out',str(QA/'release-validation.json')],check=True,
    stdout=subprocess.DEVNULL)
report = json.loads((QA/'release-validation.json').read_text())
assert report['ok'] and report['package']['temporary_install_test'] and not report['package']['user_install_modified']
checksums = {str(path.relative_to(ROOT)):sha(path) for path in (PRODUCT/'pet.json',PRODUCT/'spritesheet.webp',PRODUCT/'README.md',ZIP)}
(QA/'SHA256SUMS').write_text(''.join(f'{digest}  {name}\n' for name,digest in checksums.items()))
print(json.dumps({'ok':True,'product':str(PRODUCT),'zip':str(ZIP),'atlas_sha256':sha(ATLAS),
                  'zip_sha256':sha(ZIP),'temporary_install_test':True,'user_install_modified':False}))

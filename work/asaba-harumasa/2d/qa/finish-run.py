"""Archive a verified completed run and recoverably clean redundant artifacts."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

RUN=Path(__file__).resolve().parents[1]
ROOT=RUN.parents[2]
PRODUCT=ROOT/'zenless-zone-zero/Asaba Harumasa/asaba-harumasa-2d'
ZIP=PRODUCT.parent/'asaba-harumasa-2d-codex-pet-v2.zip'
GENERATED=Path('/home/ubuntu23/.codex/generated_images')
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def read(name):
    return json.loads((RUN/'qa'/name).read_text())
release=read('release-validation.json')
visual=read('final-visual-qa.json')
assert release['ok'] and release['package']['ok'] and release['package']['temporary_install_test']
assert not release['package']['user_install_modified']
assert visual['visual_qa']=='pass'
assert sha(PRODUCT/'spritesheet.webp')==sha(RUN/'final/spritesheet-extended.webp')==visual['atlas_sha256']
assert sha(ZIP)==release['package']['zip_sha256']
assert read('source-reconstruction.json')['ok'] and read('preview-validation.json')['ok'] and read('transition-validation.json')['ok']
assert read('direction-blind-validation.json')['ok']
manifest=json.loads((RUN/'imagegen-jobs.json').read_text())
assert all(job['status']=='complete' for job in manifest['jobs'])
originals=read('source-originals.json')
assert len(originals)==9 and all(sha(Path(item['retained']))==item['sha256'] for item in originals)
assert set(path.name for path in PRODUCT.parent.iterdir())=={'asaba-harumasa-2d','asaba-harumasa-2d-codex-pet-v2.zip'}
assert not subprocess.check_output(['git','diff','--name-only','--','README.md','README.fr.md','README.zh-CN.md','README.ja.md','assets/readme','scripts/build_readme_showcase.py'],cwd=ROOT,text=True).strip()

targets=[]
for job in manifest['jobs']:
    source=Path(job['source_path'])
    if source.exists():
        assert source.is_relative_to(GENERATED) and sha(source)==sha(RUN/job['output_path'])
        targets.append(source)
    for attempt in job.get('rejected_attempts',[]):
        candidate=RUN/attempt['path']
        if candidate.exists():
            assert sha(candidate)==attempt['sha256']
            targets.append(candidate)
rejected_originals=[
 '/home/ubuntu23/.codex/generated_images/01a1b664-8335-7860-92b2-f5a9b358dce6/exec-d7be391e-6535-475c-b712-68d5b2ee586e.png',
 '/home/ubuntu23/.codex/generated_images/01a1b664-8335-7860-92b2-f5a9b358dce6/exec-d98356ed-c787-4abf-9dd3-bcba72b379d2.png',
 '/home/ubuntu23/.codex/generated_images/01a1b664-8335-7860-92b2-f5a9b358dce6/exec-7e9acd7d-8480-41a0-adad-6a3dca78712f.png',
 '/home/ubuntu23/.codex/generated_images/01a1b664-8335-7860-92b2-f5a9b358dce6/exec-3f06cbca-d6dc-4c0e-b6c3-01f1f3ba3616.png',
 '/home/ubuntu23/.codex/generated_images/01a1b674-64a4-7491-ade4-5c10e06a0959/exec-0f8d090f-8aa2-48fa-a230-cdd867efec26.png'
]
rejected_hashes={item['sha256'] for job in manifest['jobs'] for item in job.get('rejected_attempts',[])}
for filename in rejected_originals:
    path=Path(filename)
    if path.exists():
        assert path.is_relative_to(GENERATED) and sha(path) in rejected_hashes
        targets.append(path)
for relative in ('prompts','references/layout-guides','qa/previews','final/spritesheet.png','final/spritesheet.webp','final/spritesheet-extended.png'):
    path=RUN/relative
    if path.exists():
        targets.append(path)
for row in json.loads((RUN/'frames/frames-manifest.json').read_text())['rows']:
    path=RUN/f"qa/rows/{row['state']}/frames"
    if path.exists():
        for frame in (path/row['state']).glob('*.png'):
            assert sha(frame)==sha(RUN/'frames'/row['state']/frame.name)
        targets.append(path)
for path in targets:
    assert path.is_relative_to(GENERATED) or path.is_relative_to(RUN)
    assert path not in (RUN,ROOT,GENERATED) and not path.is_relative_to(RUN/'references/source-originals')
assert (RUN/'qa/generation-prompts.md').is_file() and read('generation-provenance.json')['selected_jobs']==13
cleanup={'method':'gio trash; recoverable in desktop Trash','targets':[str(path) for path in targets],
         'user_originals_retained':9,'selected_source_strips_retained':True,'reconstruction_frames_and_parameters_retained':True,
         'completed':False}
(RUN/'qa/cleanup-record.json').write_text(json.dumps(cleanup,indent=2)+'\n')
if targets:
    assert shutil.which('gio'), 'Trash command unavailable; leave files retained'
    subprocess.run(['gio','trash',*map(str,targets)],check=True)
cleanup['completed']=True
(RUN/'qa/cleanup-record.json').write_text(json.dumps(cleanup,indent=2)+'\n')
assert all(sha(Path(item['retained']))==item['sha256'] for item in originals)
assert sha(PRODUCT/'spritesheet.webp')==visual['atlas_sha256'] and sha(ZIP)==release['package']['zip_sha256']

progress=read('production-progress.json')
ended=datetime.now(timezone.utc)
elapsed=(ended-datetime.fromisoformat(progress['started_at'])).total_seconds()/60
summary={'ok':True,'pet_id':'asaba-harumasa','display_name':'Asaba Harumasa','style':'2D anime chibi',
    'spriteVersionNumber':2,'atlas_size':[1536,2288],'cell_size':[192,208],'used_cells':74,
    'standard_animation_frames':57,'look_directions':16,'selected_jobs':13,'generation_calls':18,
    'atlas_sha256':visual['atlas_sha256'],'zip_sha256':release['package']['zip_sha256'],
    'product':str(PRODUCT),'zip':str(ZIP),'validation':str(RUN/'qa/release-validation.json'),
    'independent_visual_review':str(RUN/'qa/final-visual-qa.json'),'warnings':visual['review_warnings'],
    'source_originals_retained':9,'references_git_ignored':True,'root_readme_updated':False,
    'installed':False,'user_install_modified':False,'committed':False,'pushed':False,
    'client_timing_version':'26.1007.21434','live_installed_client_test':False,
    'finished_at':ended.isoformat(),'minutes_since_progress_record_started':round(elapsed,1),
    'cleanup':cleanup['method']}
(RUN/'qa/run-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
progress.update(stage='complete',completed_at=ended.isoformat(),completed_jobs=[job['id'] for job in manifest['jobs']],
                minutes_since_progress_record_started=round(elapsed,1))
(RUN/'qa/production-progress.json').write_text(json.dumps(progress,indent=2)+'\n')
checksums={str(path.relative_to(ROOT)):sha(path) for path in (PRODUCT/'pet.json',PRODUCT/'spritesheet.webp',PRODUCT/'README.md',ZIP)}
(RUN/'qa/SHA256SUMS').write_text(''.join(f'{digest}  {filename}\n' for filename,digest in checksums.items()))
print(json.dumps({key:summary[key] for key in ('ok','pet_id','atlas_sha256','zip_sha256','minutes_since_progress_record_started')}) )

"""Keep reproducible sources and approved product; recoverably trash run-only duplicates."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

RUN = Path(__file__).resolve().parents[1]
ROOT = RUN.parents[2]
QA = RUN/'qa'
PRODUCT = ROOT/'honkai-impact-3rd/Rita Rossweisse/rita-rossweisse-2d'
ZIP = PRODUCT.parent/'rita-rossweisse-2d-codex-pet-v2.zip'
GENERATED = Path('/home/ubuntu23/.codex/generated_images')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(name):
    return json.loads((QA/name).read_text())


release, visual, provenance = read('release-validation.json'), read('final-visual-qa.json'), read('generation-provenance.json')
assert release['ok'] and release['package']['ok'] and release['package']['temporary_install_test']
assert not release['package']['user_install_modified']
assert visual['visual_qa']=='pass' and sha(PRODUCT/'spritesheet.webp')==sha(RUN/'final/spritesheet-extended.webp')==visual['atlas_sha256']
assert sha(ZIP)==release['package']['zip_sha256']
assert all(read(name)['ok'] for name in ('source-reconstruction.json','preview-validation.json',
           'transition-validation.json','direction-blind-validation.json','direction-semantics.json'))
manifest = json.loads((RUN/'imagegen-jobs.json').read_text())
assert all(job['status']=='complete' for job in manifest['jobs']) and provenance['selected_jobs']==13
originals = read('source-originals.json')
assert len(originals)==9 and all(sha(Path(item['retained']))==item['sha256'] for item in originals)
assert set(path.name for path in PRODUCT.parent.iterdir())=={'rita-rossweisse-2d','rita-rossweisse-2d-codex-pet-v2.zip'}
assert set(path.name for path in PRODUCT.iterdir())=={'pet.json','README.md','spritesheet.webp'}
assert not subprocess.check_output(['git','diff','--name-only','--','README.md','README.fr.md','README.zh-CN.md',
    'README.ja.md','assets/readme','scripts/build_readme_showcase.py'],cwd=ROOT,text=True).strip()
for item in originals:
    subprocess.run(['git','check-ignore','--quiet',item['retained']],cwd=ROOT,check=True)

targets = []
for output in provenance['generated_outputs']:
    path = Path(output['path'])
    if path.exists():
        assert path.is_relative_to(GENERATED) and path.is_file() and sha(path)==output['sha256']
        if output['selected']:
            job = next(job for job in manifest['jobs'] if job['source_path']==str(path))
            assert sha(RUN/job['output_path'])==output['sha256']
        targets.append(path)
for relative in ('prompts','references/layout-guides','qa/previews',
                 'final/spritesheet.png','final/spritesheet.webp','final/spritesheet-extended.png'):
    path = RUN/relative
    if path.exists():
        targets.append(path)
for row in json.loads((RUN/'frames/frames-manifest.json').read_text())['rows']:
    path = RUN/f"qa/rows/{row['state']}/frames"
    if path.exists():
        for frame in (path/row['state']).glob('*.png'):
            assert sha(frame)==sha(RUN/'frames'/row['state']/frame.name)
        targets.append(path)
for path in targets:
    assert path.is_relative_to(GENERATED) or path.is_relative_to(RUN)
    assert path not in (RUN,ROOT,GENERATED) and not path.is_relative_to(RUN/'references/source-originals')
assert (QA/'generation-prompts.md').is_file()
cleanup = {'method':'gio trash; recoverable in desktop Trash','targets':[str(path) for path in targets],
    'user_originals_retained':9,'selected_sources_and_reconstruction_frames_retained':True,'completed':False}
(QA/'cleanup-record.json').write_text(json.dumps(cleanup,indent=2)+'\n')
if targets:
    assert shutil.which('gio'), 'No Trash command: keep all disposable files locally'
    subprocess.run(['gio','trash',*map(str,targets)],check=True)
cleanup['completed'] = True
(QA/'cleanup-record.json').write_text(json.dumps(cleanup,indent=2)+'\n')
assert all(sha(Path(item['retained']))==item['sha256'] for item in originals)
assert sha(PRODUCT/'spritesheet.webp')==visual['atlas_sha256'] and sha(ZIP)==release['package']['zip_sha256']
progress = read('production-progress.json')
ended = datetime.now(timezone.utc)
elapsed = (ended-datetime.fromisoformat(progress['started_at'])).total_seconds()/60
summary = {'ok':True,'pet_id':'rita-rossweisse','display_name':'Rita Rossweisse','style':'2D anime chibi',
    'spriteVersionNumber':2,'atlas_size':[1536,2288],'cell_size':[192,208],'used_cells':74,
    'standard_animation_frames':57,'look_directions':16,'selected_jobs':13,
    'distinct_generated_output_files':provenance['distinct_generated_output_files'],
    'discarded_output_attribution_note':provenance['output_attribution_note'],
    'non_image_validation_errors':provenance['non_image_validation_errors'],
    'atlas_sha256':visual['atlas_sha256'],'zip_sha256':release['package']['zip_sha256'],
    'product':str(PRODUCT),'zip':str(ZIP),'validation':str(QA/'release-validation.json'),
    'independent_visual_review':str(QA/'final-visual-qa.json'),'warnings':visual.get('review_warnings',[]),
    'source_originals_retained':9,'references_git_ignored':True,'root_readme_updated':False,
    'installed':False,'user_install_modified':False,'committed':False,'pushed':False,
    'client_timing_version':'26.1007.21434','live_installed_client_test':False,
    'finished_at':ended.isoformat(),'minutes_since_progress_record_started':round(elapsed,1),
    'cleanup':cleanup['method']}
(QA/'run-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
progress.update(stage='complete',completed_at=ended.isoformat(),completed_jobs=[job['id'] for job in manifest['jobs']],
                minutes_since_progress_record_started=round(elapsed,1))
(QA/'production-progress.json').write_text(json.dumps(progress,indent=2)+'\n')
print(json.dumps({key:summary[key] for key in ('ok','pet_id','atlas_sha256','zip_sha256','minutes_since_progress_record_started')}))

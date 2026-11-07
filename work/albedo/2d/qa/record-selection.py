"""Record an already reviewed selection and merge an approved row extraction."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil

R = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser()
p.add_argument('job')
p.add_argument('source', type=Path)
p.add_argument('--frames', type=Path)
p.add_argument('--note', required=True)
a = p.parse_args()
jobs_path = R/'imagegen-jobs.json'
jobs = json.loads(jobs_path.read_text())
job = next(j for j in jobs['jobs'] if j['id'] == a.job)
target = R/job['output_path']
if a.source.resolve() != target.resolve():
    shutil.copy2(a.source, target)
source_hash = hashlib.sha256(target.read_bytes()).hexdigest()
job.update(status='complete', source_path=str(a.source), source_sha256=source_hash, completed_at=datetime.now(timezone.utc).isoformat(), qa_note=a.note)
if a.job == 'base':
    shutil.copy2(target, R/'references/canonical-base.png')
if a.frames:
    staged = json.loads((a.frames/'frames-manifest.json').read_text())
    selected = next(r for r in staged['rows'] if r['state'] == a.job)
    destdir = R/'frames'/a.job
    destdir.mkdir(parents=True, exist_ok=True)
    selected['frames'] = []
    for src in sorted((a.frames/a.job).glob('[0-9][0-9].png')):
        dest = destdir/src.name
        shutil.copy2(src, dest)
        selected['frames'].append(str(dest))
    selected.update(source=str(target), source_sha256=source_hash, review_note=a.note)
    manifest_path = R/'frames/frames-manifest.json'
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {**staged, 'rows':[]}
    manifest['rows'] = [r for r in manifest['rows'] if r['state'] != a.job]+[selected]
    manifest_path.write_text(json.dumps(manifest, indent=2)+'\n')
    job['extraction_method'] = selected['method']
jobs_path.write_text(json.dumps(jobs, indent=2)+'\n')
progress_path = R/'qa/production-progress.json'
progress = json.loads(progress_path.read_text())
progress.update(updated_at=datetime.now(timezone.utc).isoformat(), completed_jobs=[j['id'] for j in jobs['jobs'] if j['status']=='complete'], pending_jobs=[j['id'] for j in jobs['jobs'] if j['status']!='complete'])
progress_path.write_text(json.dumps(progress, indent=2)+'\n')
print(json.dumps({'job':a.job,'sha256':source_hash,'complete':True}))

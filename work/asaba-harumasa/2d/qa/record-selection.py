"""Copy a selected generated source; complete only after required checks."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil

RUN = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("job")
parser.add_argument("source", nargs="?")
parser.add_argument("--complete", action="store_true")
parser.add_argument("--reject", action="store_true")
parser.add_argument("--note", default="")
args = parser.parse_args()
manifest_path = RUN / "imagegen-jobs.json"
manifest = json.loads(manifest_path.read_text())
job = next(item for item in manifest["jobs"] if item["id"] == args.job)
for dependency in job["depends_on"]:
    assert next(item for item in manifest["jobs"] if item["id"] == dependency)["status"] == "complete", dependency
if args.reject:
    assert args.note and not args.source and not args.complete
    output = RUN / job['output_path']
    history = job.setdefault('rejected_attempts', [])
    destination = RUN / f"qa/{args.job}-attempt-{len(history)+1}.png"
    assert not destination.exists()
    shutil.move(output, destination)
    history.append({'path':str(destination.relative_to(RUN)), 'sha256':hashlib.sha256(destination.read_bytes()).hexdigest(), 'reason':args.note})
    job.update(status='pending')
if args.source:
    source = Path(args.source)
    output = RUN / job["output_path"]
    assert source.is_file()
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        assert hashlib.sha256(output.read_bytes()).hexdigest() == hashlib.sha256(source.read_bytes()).hexdigest(), "Stage a new candidate before replacing"
    else:
        shutil.copy2(source, output)
    job.update(source_path=str(source), selected_sha256=hashlib.sha256(output.read_bytes()).hexdigest(), status="selected")
    if args.job == "base":
        shutil.copy2(output, RUN / "references/canonical-base.png")
if args.complete:
    assert (RUN / job["output_path"]).is_file()
    if job["kind"] == "row-strip":
        review = json.loads((RUN / f"qa/rows/{args.job}/review.json").read_text())
        assert not review.get("errors"), review
    job.update(status="complete", completed_at=datetime.now(timezone.utc).isoformat(), qa_note=args.note)
manifest_path.write_text(json.dumps(manifest, indent=2)+"\n")
progress_path=RUN/'qa/production-progress.json'
if progress_path.exists():
    progress=json.loads(progress_path.read_text())
    standard=[item for item in manifest['jobs'] if item['kind']=='row-strip']
    progress.update(updated_at=datetime.now(timezone.utc).isoformat(),
        stage='look-directions' if all(item['status']=='complete' for item in standard) else 'standard-rows',
        completed_jobs=[item['id'] for item in manifest['jobs'] if item['status']=='complete'],
        failures=[{'job':item['id'],**attempt} for item in manifest['jobs'] for attempt in item.get('rejected_attempts',[])])
    progress_path.write_text(json.dumps(progress,indent=2)+'\n')
print(json.dumps({"job":args.job, "status":job["status"], "output":job["output_path"]}))

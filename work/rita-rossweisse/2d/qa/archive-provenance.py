"""Archive selected job specs and exact worker tool-call records before cleanup."""
import hashlib
import json
from pathlib import Path

RUN = Path(__file__).resolve().parents[1]
GENERATED = Path('/home/ubuntu23/.codex/generated_images')
manifest = json.loads((RUN/'imagegen-jobs.json').read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def generated_paths(value):
    if isinstance(value, dict):
        for child in value.values():
            yield from generated_paths(child)
    elif isinstance(value, list):
        for child in value:
            yield from generated_paths(child)
    elif isinstance(value, str) and value.startswith(str(GENERATED)+'/') and value.endswith('.png'):
        yield value


records, outputs = [], set()
sections = ['# Rita Rossweisse — generation provenance',
            'Built-in image_gen only. Job specifications below; exact per-call prompts, inputs and outcomes are retained in the linked worker JSON files. Reference originals remain local and ignored.']
for job in manifest['jobs']:
    assert job['status'] == 'complete', job['id']
    source = RUN/job['output_path']
    assert sha(source) == job['selected_sha256']
    prompt = RUN/job['prompt_file']
    worker_path = RUN/f"qa/{job['id']}-worker-calls.json"
    worker = json.loads(worker_path.read_text())
    paths = set(generated_paths(worker))
    assert job['source_path'] in paths, (job['id'], paths)
    outputs.update(paths)
    sections.extend([f"## {job['id']}", f"Exact tool-call record: `{worker_path.name}`.", prompt.read_text().rstrip()])
    records.append({'job':job['id'],'kind':job['kind'],'selected_source':job['output_path'],
        'source_sha256':sha(source),'prompt_file':job['prompt_file'],'prompt_sha256':sha(prompt),
        'actual_worker_calls':str(worker_path.relative_to(RUN)), 'actual_worker_calls_sha256':sha(worker_path),
        'generated_outputs':sorted(paths),
        'input_images':[{'path':item['path'],'role':item['role'],'sha256':sha(RUN/item['path'])} for item in job['input_images']],
        'completed_at':job['completed_at'],'qa_note':job.get('qa_note',''),
        'rejected_attempts':job.get('rejected_attempts',[])})
selected = {job['source_path'] for job in manifest['jobs']}
all_outputs = [{'path':path,'sha256':sha(Path(path)),'selected':path in selected} for path in sorted(outputs)]
report = {'mode':'built-in image_gen','selected_jobs':len(records),
    'distinct_generated_output_files':len(all_outputs),
    'reported_output_attributions':sum(len(item['generated_outputs']) for item in records),
    'output_attribution_note':'One discarded six-pose image path is listed by both idle and waving worker histories; it was inferred from a directory listing, not reliably bound to both calls. Raw records retain uncertainty. Count distinct verified output files, not a falsely exact successful-call count. All thirteen selected output paths are unique and directly verified.',
    'non_image_validation_errors':'See waving-worker-calls.json: one empty-prompt HTTP 400, not a transport error and not a generated image.',
    'jobs':records,'generated_outputs':all_outputs}
(RUN/'qa/generation-prompts.md').write_text('\n\n'.join(sections).rstrip()+'\n')
(RUN/'qa/generation-provenance.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'archived_selected_jobs':len(records),'distinct_generated_output_files':len(all_outputs)}))

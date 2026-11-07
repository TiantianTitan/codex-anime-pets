"""Archive actual selected prompts and input/source hashes before cleanup."""
import hashlib
import json
from pathlib import Path

RUN=Path(__file__).resolve().parents[1]
manifest=json.loads((RUN/'imagegen-jobs.json').read_text())
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
records=[]
prompts=['# Asaba Harumasa · selected generation prompts\n', 'Built-in image_gen was used for every visual job. Original reference images remain local and ignored.\n']
for job in manifest['jobs']:
    assert job['status']=='complete', job['id']
    source=RUN/job['output_path']
    assert sha(source)==job['selected_sha256']
    prompt=RUN/job['prompt_file']
    prompts.extend([f"## {job['id']}\n", prompt.read_text(), '\n'])
    records.append({'job':job['id'],'kind':job['kind'],'selected_source':job['output_path'],
        'source_sha256':sha(source),'prompt_file':job['prompt_file'],'prompt_sha256':sha(prompt),
        'input_images':[{'path':item['path'],'role':item['role'],'sha256':sha(RUN/item['path'])} for item in job['input_images']],
        'completed_at':job['completed_at'],'qa_note':job.get('qa_note',''),
        'rejected_attempts':job.get('rejected_attempts',[])})
(RUN/'qa/generation-prompts.md').write_text('\n'.join(prompts))
(RUN/'qa/generation-provenance.json').write_text(json.dumps({'mode':'built-in image_gen',
    'selected_jobs':len(records),'total_generation_calls':len(records)+sum(len(job.get('rejected_attempts',[])) for job in manifest['jobs']),
    'jobs':records},indent=2)+'\n')
print(json.dumps({'archived_selected_jobs':len(records),'total_generation_calls':len(records)+sum(len(job.get('rejected_attempts',[])) for job in manifest['jobs'])}))

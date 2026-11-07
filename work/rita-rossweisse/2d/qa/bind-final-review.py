"""Bind the independent final approval to every selected source and report."""
import hashlib
import json
from pathlib import Path
RUN=Path(__file__).resolve().parents[1]
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
path=RUN/'qa/final-visual-qa.json'
review=json.loads(path.read_text())
assert review['visual_qa']=='pass' and review['atlas_sha256']==sha(RUN/'final/spritesheet-extended.webp')
provenance=json.loads((RUN/'qa/generation-provenance.json').read_text())
assert provenance['selected_jobs']==13
review['selected_source_sha256']={item['job']:item['source_sha256'] for item in provenance['jobs']}
for item in provenance['jobs']:
    assert sha(RUN/item['selected_source'])==item['source_sha256']
review['evidence_sha256']={name:sha(RUN/'qa'/name) for name in ('generation-provenance.json','source-reconstruction.json',
    'direction-semantics.json','direction-blind-validation.json','preview-validation.json','transition-validation.json')}
path.write_text(json.dumps(review,indent=2)+'\n')
print(json.dumps({'visual_qa':review['visual_qa'],'atlas_sha256':review['atlas_sha256'],'bound_selected_sources':len(review['selected_source_sha256'])}))

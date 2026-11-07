"""Persist inspected row-9 meaning and adjacent metrics before row-10 generation."""
from pathlib import Path
import hashlib
import importlib.util
import json
from PIL import Image
R=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('continuity','/home/ubuntu23/.codex/skills/hatch-pet/scripts/measure_direction_continuity.py')
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
path=R/'qa/look-row-9-registered.png'
strip=Image.open(path).convert('RGBA')
assert strip.size==(1536,208)
labels=['000','022.5','045','067.5','090','112.5','135','157.5']
cells=[strip.crop((i*192,0,(i+1)*192,208)) for i in range(8)]
pairs=[{'from':labels[i],'to':labels[i+1],**m.pair_metric(cells[i],cells[i+1])} for i in range(7)]
observations=[
 ('up','pass','Centered face, raised chin and visibly upward turquoise pupils.','centered','chin and gaze raised'),
 ('up-right','warning','Chin stays lifted as face and pupils begin a slight rightward turn.','subtle rightward bias near vertical','chin/gaze remain up'),
 ('up-right','pass','Rightward nose and eyes with raised chin, smooth quarter turn.','nose and gaze right','eyes/chin raised'),
 ('up-right','warning','Rightward yaw dominates, eye line and chin still slightly elevated.','clear rightward face','small upward component near horizontal'),
 ('right','pass','Nose and pupils point distinctly to screen-right with level chin.','clear screen-right yaw','level'),
 ('down-right','pass','Head remains rightward while chin and turquoise gaze begin lowering.','screen-right yaw','chin and eyes lower'),
 ('down-right','pass','Forehead becomes more visible; eyes lowered with persistent rightward face.','rightward nose/face','clear downward chin/gaze'),
 ('down-right','warning','Deeper lowered chin and gaze, still rightward; exact near-down yaw is not numerically ideal.','residual rightward quarter turn','strong downward attention')
]
sem=[{'direction':label,'expected':expected,'verdict':verdict,'observed':reason,'reason':reason,'horizontal_evidence':h,'vertical_evidence':v} for label,(expected,verdict,reason,h,v) in zip(labels,observations)]
report={'ok':True,'source_sha256':hashlib.sha256((R/'decoded/look-row-9.png').read_bytes()).hexdigest(),'registered_row_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'reviewed_by':'parent','registration_and_edges_passed':True,'native_size':[192,208],'next_row_authorized':True,'continuity':pairs,'semantics':sem,'notes':['All poses are complete, identity-preserving and grounded. No native-visible reversal, broken attachment or wrong quadrant.','Near-cardinal cues and residual yaw are minor review candidates, not waived cardinal failures. Final row boundary, three blind reviews and independent final review remain required.']}
assert all(p['centerDelta']<8 and p['areaRatio']<1.25 for p in pairs), 'Inspect numeric outliers before accepting'
(R/'qa/look-row-9-gate.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'ok':True,'max_center_delta':max(p['centerDelta'] for p in pairs),'max_area_ratio':max(p['areaRatio'] for p in pairs)}))

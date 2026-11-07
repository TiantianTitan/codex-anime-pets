"""Persist parent labeled full-loop observations bound to the final atlas."""
import hashlib
import json
from pathlib import Path
RUN=Path(__file__).resolve().parents[1]
first=json.loads((RUN/'qa/look-row-9-gate.json').read_text())['directions']
second=[
 {'degree':'180','verdict':'pass','expected':'down','observed':'Tucked chin, lowered eye line and visible crown','reason':'Clear downward head attention, opposite raised-chin up.'},
 {'degree':'202.5','verdict':'warning','expected':'down-left','observed':{'horizontal':'Small leftward nose/face bias','vertical':'Lowered face and tucked chin'},'reason':'Near-vertical horizontal cue subtle but advances into the left family.'},
 {'degree':'225','verdict':'pass','expected':'down-left','observed':{'horizontal':'Nose/face and eyes screen-left','vertical':'Chin tucked and eye focus lowered'},'reason':'Both axes remain readable in ordered sequence.'},
 {'degree':'247.5','verdict':'warning','expected':'down-left','observed':{'horizontal':'Clear screen-left yaw','vertical':'Small downward face/eyelid cue'},'reason':'Vertical cue softens toward level left without reversal.'},
 {'degree':'270','verdict':'pass','expected':'left','observed':'Nose tip, cheek and golden pupils aim screen-left','reason':'Unmistakable left attention opposing right cardinal.'},
 {'degree':'292.5','verdict':'warning','expected':'up-left','observed':{'horizontal':'Screen-left head/eye turn','vertical':'Slightly lifted chin/eye focus'},'reason':'Up component restrained near the horizontal axis, coherent with the next pose.'},
 {'degree':'315','verdict':'pass','expected':'up-left','observed':{'horizontal':'Leftward nose/pupils and face plane','vertical':'Raised chin and upward golden irises'},'reason':'Both axes readable, volume and body anchor maintained.'},
 {'degree':'337.5','verdict':'warning','expected':'up-left','observed':{'horizontal':'Remaining mild leftward head/eye bias','vertical':'Raised chin and gaze'},'reason':'Small head-yaw return into up; no visible whole-body shift or scale pop.'}
]
report={'ok':True,'atlas_sha256':hashlib.sha256((RUN/'final/spritesheet-extended.webp').read_bytes()).hexdigest(),
        'reviewed_by':'parent labeled native-size ordered-loop and focused direction sheet review',
        'directions':first+second,'continuity_resolution':'Numerical cross-row outliers are localized head pitch/yaw and hair changes; stable boots/lower body, no identity or scale snap. Final independent visual reviewer rechecks these seams.'}
(RUN/'qa/direction-semantics.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'directions':len(report['directions']),'failures':sum(item['verdict']=='fail' for item in report['directions'])}))

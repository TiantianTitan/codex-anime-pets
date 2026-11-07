"""Persist actual labeled full-loop review; retain subtle intermediate warnings."""
import hashlib
import json
from pathlib import Path

RUN = Path(__file__).resolve().parents[1]
QA = RUN/'qa'
first = json.loads((QA/'look-row-9-gate.json').read_text())['directions']
second = [
    {'degree':'180','verdict':'pass','expected':'down','observed':'Tucked chin and lowered face/eye beneath the fringe, crown more visible','reason':'Clear downward face/neck pitch opposing raised-chin up.'},
    {'degree':'202.5','verdict':'warning','expected':'down-left','observed':{'horizontal':'Slight leftward nose/cheek bias','vertical':'Chin tucked and visible eye line lowered'},'reason':'Restrained horizontal cue near down, but native ordered family proceeds left without reversal.'},
    {'degree':'225','verdict':'pass','expected':'down-left','observed':{'horizontal':'Nose and exposed facial contour turn left','vertical':'Lowered nose/chin beneath prominent crown'},'reason':'Both axes readable, with natural eye occlusion and stable lower body.'},
    {'degree':'247.5','verdict':'warning','expected':'down-left','observed':{'horizontal':'Clear leftward face/nose profile','vertical':'Small downward lid/chin pitch'},'reason':'Down component softens near horizontal left; no wrong quadrant or reversal.'},
    {'degree':'270','verdict':'pass','expected':'left','observed':'Nose, cheek and chin profile turn clearly screen-left with visible-eye participation where the fringe permits','reason':'Left cardinal opposes right without swapping fringe or rose; all three blind reviewers identify the horizontal axis.'},
    {'degree':'292.5','verdict':'warning','expected':'up-left','observed':{'horizontal':'Leftward nose/cheek profile','vertical':'Small chin lift from level left; upward pitch grows through 315 and 337.5'},'reason':'Blind vertical axis is ambiguous at this near-horizontal intermediate. Labeled native loop preserves left-to-up progression without downward reversal; accepted minor subtlety, not a waived cardinal.'},
    {'degree':'315','verdict':'pass','expected':'up-left','observed':{'horizontal':'Nose and face plane remain leftward','vertical':'Lifted chin and exposed underside of face'},'reason':'Both axes readable with fixed feet and consistent maid identity.'},
    {'degree':'337.5','verdict':'warning','expected':'up-left','observed':{'horizontal':'Remaining slight leftward face/nose bias','vertical':'Raised chin and face plane'},'reason':'One localized head/hair transition into 000 measures higher pixel difference; native sequence has no whole-body jump, scale pop or wrong-direction reversal.'}
]
digest = hashlib.sha256((RUN/'final/spritesheet-extended.webp').read_bytes()).hexdigest()
report = {'ok':True,'atlas_sha256':digest,
    'reviewed_by':'parent native-size labeled full loop and neutral/direction QA sheet',
    'directions':first+second,
    'continuity_resolution':'337.5->000 local numeric outlier is confined to head pitch/yaw and hair shape. Planted lower body and matching baseline; no visible scale/registration snap, clipping, broken attachment or anatomical hole. Independent final review rechecks.'}
(QA/'direction-semantics.json').write_text(json.dumps(report,indent=2)+'\n')
resolution = {'decision':'accept','severity':'minor','reviewed_by':'parent','atlas_sha256':digest,
    'failed_checks':['vertical-7 A: 292.5 vertical axis ambiguous by three-reviewer majority',
                     '337.5->000 local continuity difference outlier'],
    'hard_cardinals_all_pass':True,
    'evidence':['look-directions.png','transitions-final/look-loop.webp','look-continuity.json',
                'direction-semantics.json','direction-blind-validation.json'],
    'reason':'292.5 has definite left direction and restrained upward chin transition toward 315/337.5, not a wrong-quadrant or reversing pose. Up/right/down/left cardinal majorities all pass. Numeric seam change remains localized to head/hair with stable boots, torso scale and anatomy; no major defect is overridden.'}
(QA/'blind-review-resolution.json').write_text(json.dumps(resolution,indent=2)+'\n')
print(json.dumps({'ok':True,'directions':len(report['directions']),'cardinal_override':False,'warnings_retained':True}))

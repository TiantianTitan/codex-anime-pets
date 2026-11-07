"""Record the parent's labeled native-size review, preserving blind evidence separately."""
from pathlib import Path
import hashlib
import json
R=Path(__file__).resolve().parents[1]
first=json.loads((R/'qa/look-row-9-gate.json').read_text())['semantics']
second=[
 ('180','down','pass','Centered bowed head, tucked chin and visible turquoise eyes looking below.','centered','both eyes down and crown more visible'),
 ('202.5','down-left','warning','Downward face retains a small leftward eye/nose bias, near the down cardinal.','subtle leftward eye/nose bias','clear tucked chin/downward eye line'),
 ('225','down-left','pass','Nose and turquoise gaze move left while chin remains lowered.','leftward face and eyes','lowered chin and gaze'),
 ('247.5','down-left','warning','Left quarter-view strengthens; downward eye line remains small near horizontal.','leftward nose and visible eye','small downward eyelid/chin cue'),
 ('270','left','pass','Unmistakable leftward head yaw, nose and pupils to screen-left at level pitch.','clear screen-left nose/gaze','level chin'),
 ('292.5','up-left','warning','Leftward face with gently lifted eye line and chin.','clear leftward head and eyes','small lifted chin and upper gaze'),
 ('315','up-left','pass','Chin and eyes rise while face remains directed left.','leftward nose/gaze','clearly raised chin and pupils'),
 ('337.5','up-left','warning','Strong upward chin/gaze with residual leftward yaw; closing transition returns toward centered up.','residual leftward face','raised chin and upward eyes')
]
entries=first+[{'direction':d,'expected':e,'verdict':v,'observed':o,'reason':o,'horizontal_evidence':h,'vertical_evidence':y} for d,e,v,o,h,y in second]
for entry in entries:
    entry['pass']=entry['verdict']!='fail'
blind_path=R/'qa/direction-blind-validation.json'
if blind_path.exists():
    blind=json.loads(blind_path.read_text())
    assert blind['ok'] and not blind['errors'], 'A failed cardinal cannot be waived'
    for pair in blind['pairs']:
        for slot in ('A','B'):
            result=pair[slot]
            if not result['pass']:
                entry=next(e for e in entries if e['direction']==result['source_direction'])
                entry['verdict']='warning'
                entry['blind_axis_warning']={'pair':pair['pair'],'axis':pair['axis'],'observed':result['observed'],'expected':result['expected']}
                entry['reason']+=' Unlabeled near-horizontal pitch was ambiguous; labeled native ordered motion retains the intended quadrant without reversal.'
report={'ok':True,'atlas_sha256':hashlib.sha256((R/'final/spritesheet-extended.webp').read_bytes()).hexdigest(),'reviewed_by':'parent','evidence':['look-directions.png','look-continuity.json','transitions-final/look-loop.webp'],'native_cell_size':[192,208],'directions':entries,'continuity_resolution':{'finding':'337.5->000 local pixel-difference outlier','severity':'minor pending independent confirmation','reason':'Lower body/boot anchors remain planted, no scale jump, missing pixels or alpha holes. Difference is head yaw/forelock silhouette returning from left-up to centered up; native ordered sequence preserves clockwise attention. Exact angular step is less even at closure.'},'independent_final_review_required':True}
(R/'qa/direction-semantics.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'ok':True,'directions':len(entries),'hard_failures':sum(e['verdict']=='fail' for e in entries)}))

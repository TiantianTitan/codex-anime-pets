import json,hashlib
from pathlib import Path
root=Path('/home/ubuntu23/Bureau/codex-anime-pets')
run=root/'work/motion-refinement-2026-11-06'
p=json.loads((run/'inventory.json').read_text())
ids=['black-swan','kafka','sparkle','acheron','aventurine','blade','dan-heng-imbibitor-lunae','firefly','jing-yuan','robin','ruan-mei','sunday','bronya-zaychik','fu-hua','kallen-kaslana','kiana-kaslana']
# Every contact and listed native strip was actually viewed before this report.
C={}
def candidate(id,state,frames,severity,issue,repair,classification='visible-motion-improvement',mapping=None):
 C[id,state]={'status':'candidate','frame_indices_zero_based':frames,'severity':severity,'issue':issue,'minimal_repair':repair,'classification':classification}
 if mapping is not None:C[id,state]['trial_mapping_not_approved']=mapping
candidate('kafka','failed',list(range(8)),'medium','原始 decoded 条带中脚底统一，低头时头部自然下降；atlas 每帧重新贴顶导致后段头部放大。动作又由持续低头直接 7→0 抬头，连续三轮时可见重新启动。','先从实际存在的完整源条带重新提取，统一缩放与脚底锚点，保留原始身体高度变化；再比较同状态完整帧往返顺序。建议试验映射只是假设，必须按当前时序动画复核，不可直接批量套用。','source-confirmed-extraction-plus-cycle', [0,2,4,7,6,4,2,0])
candidate('black-swan','failed',[3,4,5,6,7],'medium','第 4–6 帧蹲坐时头部和身体整体尺寸突然增大，5–6 帧抱膝后直接 7 帧站立；原生行可见尺寸膨胀，不能只解释为垂直下蹲。','没有找到 decoded 源，不断言提取算法原因。先试验同状态中尺度一致的站立低头完整帧组成往返动作，保留沮丧语义。若必须保留抱膝情节，应整行重绘统一人物尺度与下蹲/起身中间态；不要逐帧缩放头部掩盖。',mapping=[0,1,2,3,3,2,1,0])
candidate('sparkle','failed',[2,3,4,5],'medium','第 3–4 帧由站立进入蹲坐时头部明显放大，并在第 5 帧立刻恢复原尺度；原生行可见尺寸脉冲。','优先试验本行站立低头家族完整帧往返，避免中段尺寸突变。若要保留坐地情节，需要完整 8 帧统一尺度与阶段过渡；不为此仅插值变形。',mapping=[0,1,2,5,5,2,1,0])
candidate('kiana-kaslana','failed',[3,4,5,6],'medium','第 4–5 帧坐倒时头部明显大于第 0–3、6–7 帧，头顶仍贴近同一高度，产生尺寸脉冲；第 6 帧立即回小。','优先试验同状态站立低头完整帧往返；如保留坐倒，整行统一身体尺度与转折阶段。无源条带证据，不直接断言提取错误。',mapping=[0,1,2,3,3,2,1,0])
candidate('ruan-mei','failed',list(range(8)),'high','站立帧 0/2/4/6 与坐地帧 1/3/5/7 逐帧交替，头部尺度也在两类姿势间显著变化；乐器位置和有无同时变化。原生显示会反复站起/跌坐，缺乏连续阶段。','不能靠平移配准解决。先考察本行完整同状态帧是否能组成一致的低头阶段，但可用一致子集不足以保留当前动作内容；推荐整行 8 帧重绘单次低头/下蹲/恢复弧线，统一角色尺度与乐器持有状态，不新增帧或改速度。')
candidate('ruan-mei','running-right',[1,2,3,4,5,6],'high','乐器仅在第 2、5 帧突然出现在胸前，下一帧又消失，同时手臂姿态改变；这不是正常跑步相位位移。','可先试验只用本行无乐器的完整帧家族重排，必须保留至少伸腿/收腿两阶段与方向。若无法保持完整步态，则整行重绘固定乐器有无的 8 帧跑步，不跨状态借帧。')
candidate('ruan-mei','running-left',list(range(8)),'high','第 1、3、5、7 帧持乐器，0、2、4、6 帧无乐器，几乎每帧闪现/消失，原生尺寸明显。','本行持乐器的 4 帧或无乐器的 4 帧各是一致子家族，可先独立试验完整帧循环；若腿相位不足或与右向设定不一致，则整行重绘。不要混用两个持物状态。')
candidate('ruan-mei','waiting',[4,5,0],'medium','第 5 帧突然持乐器，首尾相接时乐器又消失；前五帧都是无乐器的问询手势。','将最后一槽换成本行原第 0 帧作为收势候选，保持 6 槽时序与前五帧，随后按原生尺寸验证 4→0→0 的动作是否更自然。',mapping=[0,1,2,3,4,0])
# These are observed trajectory limitations, not an assertion that each source is defective.
for id in ['black-swan','sparkle','acheron','aventurine','blade','ruan-mei','sunday','kiana-kaslana']:
 candidate(id,'jumping',list(range(5)),'medium','五帧的头顶/全身范围大致挤在相同单元高度内，缺少清晰的起跳→腾空→回落轨迹；部分帧改为大头蹲姿或伸腿，观感偏切换姿势。此处有意的腿部动作本身不是抖动。','先核对完整源条带（本次未找到 decoded 源，不能假定存在）。若源保留正确运动轨迹，以统一缩放和整体帧锚点重新提取；否则仅试验完整帧的垂直配准与共享缩放，不单独归一化每帧身体。若人物尺度仍不连续，保留当前版直到完整 5 帧统一尺度和轨迹重绘通过。','trajectory-improvement-source-unavailable')

normal={
'idle':'眼睛与身体状态稳定，慢速待机下未见需要本轮修改的明显跳位；不同帧的微小差异或合法停留帧保留。',
'running-right':'可辨识右向跑步与腿部相位；头发、衣摆和抬脚的有意变化不作为抖动处理。',
'running-left':'可辨识左向跑步与腿部相位；没有确认需改变的非动作性位移。',
'waving':'站姿中心基本稳定，抬手/放手为预期动作；有限四帧的手势跳变未发现需重绘的明确缺陷。',
'jumping':'可辨识预备、上升、腾空、回落/落地；纵向位移属于有意跳跃，不强行将头顶或脚底全部锁死。',
'failed':'表情/低头/下蹲有可辨识阶段，未确认需修改的非动作性跳位；保留原有情绪动作。',
'waiting':'问询手势与轻微倾身属于有意动作，未见独立的主体跳位或异常循环接缝。',
'running':'处理工作时的手势、思考和表情变化可辨识；在固定帧数下未确认额外修复收益。',
'review':'审阅/思考的头部与手部变化可辨识；未见需要本轮修改的主体抖动。'}
notes={
'aventurine':{'idle':'seam_ratio=34.26 来自其他差值近零；实际六帧姿态稳定且差异很小，不能依据高比例自动修改。','failed':'惊讶、低头、恢复的表情变化可辨识；2.797 的首尾指标未构成主体跳位证据。'},
'kallen-kaslana':{'failed':'原生行确认姿态与脚底基本稳定；首尾 ratio=2.122 主要反映面部和手势变化，保留。'},
'blade':{'idle':'刘海遮眼属于角色造型，未当作待机闭眼缺陷。'},
'acheron':{'idle':'单眼被刘海遮挡属于角色造型，保留。'},
'dan-heng-imbibitor-lunae':{'idle':'此前更新的六帧待机维持稳定中心与自然微动。','jumping':'起跳和落地保留低位、峰值居中高位，首尾收束清晰。'},
'jing-yuan':{'idle':'此前更新的六帧待机维持稳定中心与自然微动。','jumping':'起跳、腾空、落地的纵向轨迹清晰，首尾姿势接近。'},
'bronya-zaychik':{'idle':'轻微歪头/回正是可读的姿态变化，脚底稳定，不机械抹平。'},
'sparkle':{'waving':'第 0 帧手放下、第 1–3 帧抬手；有限四帧中的抬放动作本身可辨识，未按 ratio=1.805 自动判缺陷。'},
'firefly':{'jumping':'起跳、腾空、回落轨迹清晰，首尾低位接近。'},
'robin':{'jumping':'有清晰纵向升降，保留裙摆及腿部动作。'},
'fu-hua':{'jumping':'抬升与回落清晰，末帧回到低位。'}}
report={'reviewer':'motion_audit_star_honkai','read_only_audit':True,'baseline_commit':p['baseline_commit'],'client_version':p['client_version'],'method':'实际逐一查看 16 张 contact，每张覆盖九行动作；针对候选查看列明的原生 192×208 单元横条。静态逐帧审计，不冒称已运行桌面端动画。所有候选仍需按照当前固定 durations 的原生尺寸动画对比确认后才可采用。','scope_editions':16,'scope_rows':144,'indexing':'frame indices are zero-based','source_policy':'只确认 Kafka decoded 条带实际存在；其他条带未找到，不推测存在。','source_confirmed':{'path':'work/kafka/2d/decoded/failed.png','sha256':hashlib.sha256((root/'work/kafka/2d/decoded/failed.png').read_bytes()).hexdigest(),'observation':'完整 8 帧脚底共享水平线，后段头部下降且保持自然尺度；atlas 却将每帧重新放满高度。'},'native_rows_viewed':['ruan-mei--failed','ruan-mei--running-right','ruan-mei--running-left','ruan-mei--waiting','kafka--failed','kiana-kaslana--failed','black-swan--failed','sparkle--failed','aventurine--jumping','acheron--jumping','blade--jumping','kallen-kaslana--failed'],'editions':[]}
for e in p['editions']:
 if e['id'] not in ids:continue
 ed={'id':e['id'],'name':e['name'],'atlas':e['atlas'],'atlas_sha256':e['sha256'],'contact_viewed':e['contact'],'rows':[]}
 for row in e['rows']:
  r={'row':row['row'],'state':row['state'],'slot_count':row['count'],'durations_ms':row['durations_ms'],'evidence':{'contact':e['contact'],'native_strip':row['strip'],'bounds':row['bounds'],'seam_ratio_supporting_only':row['seam_ratio']}}
  if (e['id'],row['state']) in C:r.update(C[e['id'],row['state']])
  else:r.update({'status':'keep','severity':'none','reason':notes.get(e['id'],{}).get(row['state'],normal[row['state']])})
  ed['rows'].append(r)
 report['editions'].append(ed)
report['summary']={'candidate_rows':sum(r['status']=='candidate' for e in report['editions'] for r in e['rows']),'keep_rows':sum(r['status']=='keep' for e in report['editions'] for r in e['rows']),'high_priority_rows':['ruan-mei/failed','ruan-mei/running-right','ruan-mei/running-left'],'first_low_risk_trials':['kafka/failed: reextract from verified source before ordering trial','ruan-mei/waiting: final slot uses same-row original frame 0'],'no_asset_mutations':True,'no_git_mutations':True}
path=run/'review-star-honkai.json'
path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(path)
print(json.dumps(report['summary'],ensure_ascii=False))

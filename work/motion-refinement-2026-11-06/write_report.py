"""Publish a concise coverage report, retaining explicitly unadopted candidates."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
RUN=Path(__file__).resolve().parent
inv=json.loads((RUN/'inventory.json').read_text())
release=json.loads((RUN/'release-validation.json').read_text())
assert release['ok']
changed={p['id']:p for p in release['published']}
names={0:'待机',1:'向右跑动',2:'向左跑动',3:'打招呼',4:'跳跃',5:'失败反馈',6:'等待输入',7:'工作中',8:'审阅'}
states={r['state']:r['row'] for r in inv['editions'][0]['rows']}
unused=[]
for file in RUN.glob('review-*.json'):
    for pet in json.loads(file.read_text())['editions']:
        applied=changed.get(pet['id'],{}).get('changed_states',[])
        for r in pet['rows']:
            if r.get('status')=='candidate' and r['state'] not in applied:
                unused.append((pet['id'],r['state']))
lines=['# 固定帧数动作优化 · 2026-11-06','',
       '[打开前后对比 HTML](pet-motion-refinement.html) · [逐版本完整性验证](pet-motion-refinement-validation.json)','',
       '检查全部 **48 个版本、432 行动作**，最终更新 **18 个版本、29 行动作**；其余 **403 行**保留。所有系列均已覆盖，并不意味着每个文件都需要修改。','',
       '采用 11 行同状态完整帧重组、11 行既有原始素材重提取、7 行完整动作重绘。跳跃统一角色比例并收小原有弧线，避免为容纳大跳跃而缩小人物、回到待机时突然变大。','',
       '本轮重点处理：失败反馈首尾突跳和蹲姿放大、阮梅乐器闪现、万叶工作姿态与道具断裂、希儿跑动断脚、芽衣发丝裁切，以及六条跳跃的比例和起落。','',
       '## 保持的约束','',
       '- v2 图集仍为 1536 × 2288，单格 192 × 208。九项动作帧数仍为 6 / 8 / 8 / 4 / 5 / 8 / 6 / 6 / 6。',
       '- 未修改客户端 FPS、动作持续时间、宠物 ID、manifest、待机、neutral 或 16 个观察方向。',
       '- 只重打包对应的 18 份 ZIP，保持原下载文件名和根目录结构，并更新受影响的校验和。',
       '- 未写入用户已安装的宠物目录。此处是素材和浏览器对比验收，尚未进行桌面客户端安装验收。','',
       '## 验证','',
       '- 48 / 48 图集通过 v2 校验，无警告；48 / 48 manifest 与基线原字节相同。',
       '- 4022 个未授权修改的单格完整 RGBA 精确一致；29 行均可从真实源或明确的同状态映射重建。',
       '- 29 / 29 动画预览按时间区间验证完整 alpha、可见 RGBA 和总时长；允许编码器合并重复帧。',
       '- 两组独立视觉审核覆盖全部 29 行，按原生尺寸比较逐帧、三轮循环及回待机。',
       '- 对比页支持全部 432 项动作、同步播放、逐帧、拖动进度、循环和减少动态效果；检查桌面、390px 与 320px 窄屏。','',
       '## 全量覆盖','', '| 版本 | 本轮调整 |', '| --- | --- |']
for p in inv['editions']:
    action=changed.get(p['id'],{}).get('changed_states',[])
    lines.append('| '+p['name']+' | '+('、'.join(names[states[s]] for s in action) if action else '九项动作保留')+' |')
lines += ['', '## 本轮未采用的候选','',
          '以下 15 项仍保留原样，不能计作已解决：14 条跳跃缺少完整原始条带，需要进一步评估整行重绘的收益；伯尼斯向右跑动仅发现低置信度节奏候选。为控制范围，本轮没有批量重绘这些动作，也没有通过加帧或插值改变播放规范。','',
          '| 版本 | 保留的候选 |','| --- | --- |']
display={p['id']:p['name'] for p in inv['editions']}
for id,state in sorted(unused):lines.append('| '+display[id]+' | '+names[states[state]]+' |')
lines += ['', '## 复现与来源','',
          '基线提交：`'+inv['baseline_commit']+'`。时序依据本机客户端 `'+inv['client_version']+'` 的实际固定状态表：非待机动作通常执行三轮后返回待机。HTML 复现该时序，不提供素材无法控制的 FPS 配置。','',
          '执行记录在 `work/motion-refinement-2026-11-06/`：`inventory.json`、`candidates.json`、`technical-validation.json`、两份 `qa-independent-*.json`、原始选定源与逐行提取/配准参数。7 行重绘均使用内置 image_gen，对应最终提示词保存在 `generation/*/prompts/`。','']
assert len(unused)==15, unused
(ROOT/'docs/pet-motion-refinement-2026-11-06.md').write_text('\n'.join(lines))
links={
 'README.md':'[Fixed-frame motion update: coverage and before/after preview](docs/pet-motion-refinement-2026-11-06.md).',
 'README.zh-CN.md':'[固定帧数动作更新：全量覆盖与前后对比](docs/pet-motion-refinement-2026-11-06.md)。',
 'README.fr.md':'[Mise à jour des animations à nombre de frames constant : couverture et comparaison](docs/pet-motion-refinement-2026-11-06.md).',
 'README.ja.md':'[フレーム数を維持した動作更新：対象一覧と前後比較](docs/pet-motion-refinement-2026-11-06.md)。'}
for name,text in links.items():
    p=ROOT/name;s=p.read_text()
    if text not in s:p.write_text(s.rstrip()+'\n\n'+text+'\n')
print('Report: 48 editions / 29 adopted rows / 15 unadopted candidates')

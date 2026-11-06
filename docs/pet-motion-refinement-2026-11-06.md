# 固定帧数动作优化 · 2026-11-06

[打开前后对比 HTML](pet-motion-refinement.html) · [逐版本完整性验证](pet-motion-refinement-validation.json)

检查全部 **48 个版本、432 行动作**，最终更新 **18 个版本、29 行动作**；其余 **403 行**保留。所有系列均已覆盖，并不意味着每个文件都需要修改。

采用 11 行同状态完整帧重组、11 行既有原始素材重提取、7 行完整动作重绘。跳跃统一角色比例并收小原有弧线，避免为容纳大跳跃而缩小人物、回到待机时突然变大。

本轮重点处理：失败反馈首尾突跳和蹲姿放大、阮梅乐器闪现、万叶工作姿态与道具断裂、希儿跑动断脚、芽衣发丝裁切，以及六条跳跃的比例和起落。

## 保持的约束

- v2 图集仍为 1536 × 2288，单格 192 × 208。九项动作帧数仍为 6 / 8 / 8 / 4 / 5 / 8 / 6 / 6 / 6。
- 未修改客户端 FPS、动作持续时间、宠物 ID、manifest、待机、neutral 或 16 个观察方向。
- 只重打包对应的 18 份 ZIP，保持原下载文件名和根目录结构，并更新受影响的校验和。
- 未写入用户已安装的宠物目录。此处是素材和浏览器对比验收，尚未进行桌面客户端安装验收。

## 验证

- 48 / 48 图集通过 v2 校验，无警告；48 / 48 manifest 与基线原字节相同。
- 4022 个未授权修改的单格完整 RGBA 精确一致；29 行均可从真实源或明确的同状态映射重建。
- 29 / 29 动画预览按时间区间验证完整 alpha、可见 RGBA 和总时长；允许编码器合并重复帧。
- 两组独立视觉审核覆盖全部 29 行，按原生尺寸比较逐帧、三轮循环及回待机。
- 对比页支持全部 432 项动作、同步播放、逐帧、拖动进度、循环和减少动态效果；检查桌面、390px 与 320px 窄屏。

## 全量覆盖

| 版本 | 本轮调整 |
| --- | --- |
| Tartaglia · 达达利亚 | 九项动作保留 |
| Venti | 九项动作保留 |
| Wanderer | 九项动作保留 |
| Furina · 芙宁娜 | 失败反馈 |
| Ganyu · 甘雨 | 失败反馈 |
| Hu Tao · 胡桃 | 失败反馈 |
| Kaedehara Kazuha · 枫原万叶 | 跳跃、失败反馈、等待输入、工作中 |
| Kaeya · 凯亚 | 九项动作保留 |
| Kamisato Ayaka · 神里绫华 | 九项动作保留 |
| Raiden Shogun | 九项动作保留 |
| Xiao 魈 | 九项动作保留 |
| Yae Miko 八重神子 | 九项动作保留 |
| Zhongli 钟离 | 九项动作保留 |
| Black Swan | 失败反馈 |
| Kafka · 卡芙卡 | 失败反馈 |
| Sparkle | 失败反馈 |
| Acheron · 黄泉 | 九项动作保留 |
| Aventurine | 九项动作保留 |
| Blade · 刃 | 九项动作保留 |
| Dan Heng · Imbibitor Lunae 丹恒·饮月 | 九项动作保留 |
| Firefly · 流萤 | 九项动作保留 |
| Jing Yuan 景元 | 九项动作保留 |
| Robin · 知更鸟 | 九项动作保留 |
| Ruan Mei · 阮·梅 | 向右跑动、向左跑动、失败反馈、等待输入 |
| Sunday · 星期日 | 九项动作保留 |
| Bronya Zaychik | 九项动作保留 |
| Fu Hua | 九项动作保留 |
| Kallen | 九项动作保留 |
| Kiana Kaslana · 琪亚娜·卡斯兰娜 | 失败反馈 |
| Otto Apocalypse · 奥托·阿波卡利斯 | 九项动作保留 |
| Seele Vollerei | 向左跑动 |
| Theresa | 九项动作保留 |
| Kevin Kaslana · 凯文·卡斯兰娜 | 失败反馈 |
| 雷电芽衣 Raiden Mei | 跳跃、失败反馈、等待输入 |
| 雷电芽衣 Raiden Mei 3D | 跳跃、等待输入、工作中 |
| Burnice White | 失败反馈 |
| Lighter | 九项动作保留 |
| Vivian Banshee | 九项动作保留 |
| Von Lycaon · 冯·莱卡恩 | 九项动作保留 |
| Zhu Yuan | 九项动作保留 |
| Anby Demara | 九项动作保留 |
| Ellen Joe · 艾莲·乔 | 九项动作保留 |
| Hoshimi Miyabi · 星见雅 | 跳跃 |
| Jane Doe · 简·杜 | 九项动作保留 |
| Nicole Demara · 妮可·德玛拉 | 失败反馈 |
| Kibutsuji Muzan | 九项动作保留 |
| Mitsuri Kanroji · 甘露寺蜜璃 | 跳跃、失败反馈 |
| 伊黑小芭内 Obanai | 跳跃 |

## 本轮未采用的候选

以下 15 项仍保留原样，不能计作已解决：14 条跳跃缺少完整原始条带，需要进一步评估整行重绘的收益；伯尼斯向右跑动仅发现低置信度节奏候选。为控制范围，本轮没有批量重绘这些动作，也没有通过加帧或插值改变播放规范。

| 版本 | 保留的候选 |
| --- | --- |
| Acheron · 黄泉 | 跳跃 |
| Aventurine | 跳跃 |
| Black Swan | 跳跃 |
| Blade · 刃 | 跳跃 |
| Burnice White | 向右跑动 |
| Ellen Joe · 艾莲·乔 | 跳跃 |
| Ganyu · 甘雨 | 跳跃 |
| Kevin Kaslana · 凯文·卡斯兰娜 | 跳跃 |
| Kiana Kaslana · 琪亚娜·卡斯兰娜 | 跳跃 |
| Raiden Shogun | 跳跃 |
| Ruan Mei · 阮·梅 | 跳跃 |
| Sparkle | 跳跃 |
| Sunday · 星期日 | 跳跃 |
| Venti | 跳跃 |
| Xiao 魈 | 跳跃 |

## 复现与来源

基线提交：`c72f04ddea89ff4a403803b2c4e39de237ee3ad5`。时序依据本机客户端 `26.1007.21434` 的实际固定状态表：非待机动作通常执行三轮后返回待机。HTML 复现该时序，不提供素材无法控制的 FPS 配置。

执行记录在 `work/motion-refinement-2026-11-06/`：`inventory.json`、`candidates.json`、`technical-validation.json`、两份 `qa-independent-*.json`、原始选定源与逐行提取/配准参数。7 行重绘均使用内置 image_gen，对应最终提示词保存在 `generation/*/prompts/`。

# 宠物动作对照：前三项优化

当前采用范围已按实际收益收敛：下载包仅修复慢速待机的长时间闭眼；工作姿态属于可选视觉探索，只在第 03 项中比较，未纳入下载，也未批量替换原版。

原版基线：[GitHub main 0a7cb6d](https://github.com/TiantianTitan/codex-anime-pets/tree/0a7cb6dea9bdbcc476843bf3f07892f6b47acaa1)。样本取角色列表前三位：魈、丹恒·饮月、景元。参考桌面包版本为 26.1007.21434。

1. 真实时序：HTML 中 A 沿用原 GIF 的行动画循环；B 还原客户端时序。两侧使用相同的原版图集，待机为 1.1 秒与 6.6 秒，工作行三轮后回落到待机。
2. 慢速待机：整行重绘六帧，保持可见眼睛睁开，使用克制的呼吸、肩部与发梢变化。HTML 两侧均按 6.6 秒一轮播放。
3. 状态辨识：整行重绘工作六帧，以胸前双手的紧凑动作与等待、审阅形成区分。其余状态沿用原版，未增加客户端不支持的事件或循环设置。

六条新动作行均使用内置 ImageGen，以原 neutral、原动作行和六格布局为输入。提示词位于各角色的 `prompts/rows/`，生成来源记录在 `imagegen-jobs.json`。没有通过程序绘制、变形或拼接来替代新动作生成。

候选图集只替换 `(row 0, columns 0–5)` 和 `(row 7, columns 0–5)`。其余 76 格（含 62 个已用格、neutral 和 16 向观察）与原版 RGBA 像素完全一致。沿用的方向图复用既有已批准 QA。

每位角色的 `qa/candidate-validation.json` 记录初版两行探索的图集验证、原格一致性和独立视觉 QA 结果。`packages/` 留存该版历史候选。

当前下载使用 `packages-idle-only/`：每位角色仅替换已通过视觉检查的待机六格，其余 82 格（含 68 个已用格、整条工作行、neutral 和 16 向观察）与原版逐像素一致。`qa/idle-only-validation.json` 记录该范围的验证结果；无需再次生成素材。

安装复核还发现 47 个原版 ZIP 中有 28 个带外层文件夹。四种语言的安装说明已补充正确目录层级、Windows 路径、刷新与显示步骤；`installation-validation.json` 记录临时目录内的复现结果。实际用户宠物目录未被改动。

重建离线 HTML：

```bash
python scripts/build_motion_comparison.py
```

该脚本只使用标准库。输出 `output/pet-motion-comparison.html`，已内嵌原版图集、对照素材和三个待机优化包，直接打开即可离线对照。

复用已批准的素材重新打包待机修复时，使用工作区提供的 Python：

```bash
python scripts/assemble_motion_candidates.py --idle-only
```

重新执行素材装配需要先用加载的工作区 Python 运行 `scripts/assemble_motion_candidates.py`，并重新完成视觉 QA。装配使用每行共享缩放和基线校准，调用 Hatch Pet 的提取、边缘清理及验证流程，随后恢复所有未经编辑的原版格。

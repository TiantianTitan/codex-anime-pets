# 浅羽悠真 · 2D 制作记录

已完成，ID `asaba-harumasa`，显示名 `Asaba Harumasa`。画风为清晰的 2D 动漫 Q 版，保留深蓝乱发、黄色头带、金色眼睛、左右不同的袖子与手套、青色腰部衣片和背后的短箭筒。

图集为 **1536 × 2288**，8 列 × 11 行，单格 **192 × 208**；包含九组标准动作的 57 帧、16 个观察方向与 1 个 neutral，共 74 个有效单格。两侧跑动分别生成，没有镜像服装。左跑采用双臂收稳、腿部交替的轻跑姿势，避免非对称袖子与手套在交叉摆臂时换边。

本轮使用内置 image_gen，共 18 次生成，选定 13 个任务结果。右跑的步伐/手套问题及左跑的裁切/手部连接问题共淘汰五次尝试；改用明确侧别参考与稳定手臂结构后，通过独立复核。[选定提示词](generation-prompts.md)、[实际输入与源图哈希](generation-provenance.json)和[生产进度及失败原因](production-progress.json)均已保留。

## 验证

- [成品与 ZIP 验证](release-validation.json)：图集结构、透明边缘、隐藏 RGB、manifest、平铺 ZIP 和临时安装目录查找通过。压缩包中的文件与成品目录一致，真实宠物安装目录没有改动。
- [源图重建](source-reconstruction.json)：57 个标准动作格和 16 个方向格均可从保留源图与提取/注册参数准确重建。一次最终色键清理保持全图 alpha 不变。
- [三份隔离盲测的多数结论](direction-blind-validation.json)：14 组轴向配对全部通过，包括四个主方向的硬门槛；[16 向语义](direction-semantics.json)没有失败项。
- [最终独立视觉审核](final-visual-qa.json)：通过，绑定最终图集 SHA256、选定源图和质检证据。九组动作、循环衔接、动作回待机、跳跃尺度、服装侧别、头发/鞋子完整性与箭筒连接均通过。
- [九条无损动作预览](preview-validation.json)与[八条回待机预览及方向循环](transition-validation.json)均从最终图集生成并验证时间区间内可见 RGBA 和完整 alpha。

接受的轻微特点：部分靠近坐标轴的中间视线分量较含蓄；157.5→180、337.5→000 的头部/发型变化比邻近步幅略大，但没有明显突跳、反转或尺寸变化；左跑双臂较收稳，末帧 220ms 的停留可感知，腿部节奏仍清楚。详见独立审核记录。

时序依据仓库中 **Codex Desktop 26.1007.21434、2026-11-06** 的本机历史证据：待机为 6.6 秒，回待机 QA 序列使用三轮非待机动作。这不是本角色在真实客户端中的安装实测，也不保证未来版本的播放调度或触发方式。

## 成品与保留文件

[下载 2D ZIP](../../../../zenless-zone-zero/Asaba%20Harumasa/asaba-harumasa-2d-codex-pet-v2.zip) · [完整动作表](contact-sheet-extended.png) · [方向检查图](look-directions.png) · [挥手预览](previews-final/waving.webp)

成品目录仅有 `pet.json`、`spritesheet.webp` 和安装说明；ZIP 直接包含这些文件。QA 全部位于 work。九份用户原图按字节完整保留在本地 Git 忽略的 `references/source-originals/`。选定源条带、主帧、注册参数及必要证据保留；重复生成副本、失败候选、一次性提示/布局参考和冗余中间图已移入回收站，可恢复，见[清理记录](cleanup-record.json)。

图集 SHA256：`ce805c7b86189ae7c0bbe3462402cb7d2f0f12506d3bc0e4f09a60c42831af04`

ZIP SHA256：`ce857c829f77739c1fead1a509622cc1bc3ee132d756505c1fcbdd954d9fc010`

从生产进度记录起至打包清理约 40.1 分钟。仅制作本地 2D 成品；本轮没有更新展示 README、安装、提交或推送。

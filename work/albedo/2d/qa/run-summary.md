# 阿贝多 · 2D 制作记录

已完成，ID `albedo`。13 个内置 image_gen 图像任务；生成提示词见 [generation-prompts.md](generation-prompts.md)，原始来源与实际输入见 [generation-provenance.json](generation-provenance.json)。没有制作 3D。

- 图集：1536 × 2288，8 × 11，单格 192 × 208，74 个有效单格。
- 九组动作 57 帧、16 个观察方向、1 个 neutral。两侧跑动分别绘制，保留原服左右差异。
- 透明边缘、隐藏 RGB、源图重建、9 条无损预览、8 条回待机预览、方向循环、ZIP 平铺结构和临时安装目录验证通过。
- 三份隔离盲审：四个主要方向均通过；067.5、112.5、292.5 的上下分量较细微。337.5→000 的头发/头部转向步幅略大。已按标注的原生尺寸连续序列复核，并获独立终审接受，无方向反转、尺寸突变、裁切或破洞。
- 时序依据 Codex Desktop 26.1007.21434 的本机历史实测；不是这只宠物的真实客户端安装测试。
- 七份用户原图完整保留在本地 ignored references/source-originals。QA 只在 work。重复中间文件和生成缓存副本已移到回收站，可恢复。
- 未修改根目录 README，未安装、提交或推送。

成品目录：`/home/ubuntu23/Bureau/codex-anime-pets/genshin-impact/Albedo/albedo-2d`

ZIP：`/home/ubuntu23/Bureau/codex-anime-pets/genshin-impact/Albedo/albedo-2d-codex-pet-v2.zip`

图集 SHA256：`590421dbef7d966819fc5c6cebf8466eb46d7c68e80e097e76bf324d77e7d02d`

ZIP SHA256：`b73d8352d2fa4f81fa0c330b25f1bfd7d640ec580d65b6601cc5884ba4d3b2f0`

从准备到收尾：约 27.1 分钟。

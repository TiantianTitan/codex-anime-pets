# 伊黑小芭内 Obanai — Codex 2D Pet v2

这是可直接用于 Codex v2 宠物格式的本地 2D 成品包，未自动安装或发布。

## 文件

- `pet.json`：宠物清单。
- `spritesheet.webp`：透明 RGBA 精灵图集，1536×2288，8 列×11 行，每格 192×208。

## 动画内容

- 9 个标准状态：idle、running-right、running-left、waving、jumping、failed、waiting、running、review。
- 16 个顺时针观察方向：000° 至 337.5°，每步 22.5°。
- `spriteVersionNumber` 为 `2`。

角色锁定：黑色层次短发、角色相对异色瞳、覆盖口部与下脸的白色绷带、黑白竖纹羽织、深蓝制服、白色腿部绷带、靛蓝草履，以及始终仅有一条连接在颈肩位置的白色红眼蛇。

完整质检记录位于同级 `../qa/`；其中机械规格验证无错误无警告，最终独立视觉质检为 PASS。

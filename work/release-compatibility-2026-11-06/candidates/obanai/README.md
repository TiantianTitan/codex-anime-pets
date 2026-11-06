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

成品已通过机械规格与最终独立视觉质检。

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/obanai/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\obanai\`；自定义 `CODEX_HOME` 时使用其 `pets/obanai/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/obanai/`
(default `~/.codex/pets/obanai/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。其余动作、neutral 和 16 个观察方向保持原版；ID 和 v2 格式不变。
The idle frames account for the desktop client's slow idle playback. Other states,
the neutral frame, all 16 look directions, the ID, and the v2 contract are preserved.

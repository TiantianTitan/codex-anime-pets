# Black Swan — Codex 2D Pet v2

可直接用于 Codex 桌面端的 Black Swan 2D 宠物成品包。

## 文件

- `pet.json`：Codex 宠物清单，ID 为 `black-swan`。
- `spritesheet.webp`：透明 RGBA 精灵图集，1536×2288，8 列×11 行，每格 192×208。

## 动画内容

- 9 个标准状态：idle、running-right、running-left、waving、jumping、failed、waiting、running、review。
- 16 个顺时针观察方向：000° 至 337.5°，每步 22.5°。
- `spriteVersionNumber` 为 `2`。

角色保留淡紫白色长发、半垂的琥珀紫眼、带蝴蝶饰边的深紫头纱、紫黑色礼服式战衣、长手套、纹样丝袜与尖头短靴。动作以从容、神秘的气质为核心，同时保证在 192×208 单格中轮廓清晰、方向可辨。

本次仅制作 2D，没有生成 3D。成品已通过机械规格、三份独立方向盲测与最终视觉质检。

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/black-swan/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\black-swan\`；自定义 `CODEX_HOME` 时使用其 `pets/black-swan/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/black-swan/`
(default `~/.codex/pets/black-swan/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。其余动作、neutral 和 16 个观察方向保持原版；ID 和 v2 格式不变。
The idle frames account for the desktop client's slow idle playback. Other states,
the neutral frame, all 16 look directions, the ID, and the v2 contract are preserved.

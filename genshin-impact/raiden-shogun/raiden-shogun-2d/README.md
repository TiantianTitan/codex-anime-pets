# Raiden Shogun — Codex Pet v2 (2D)

This package contains the finished animated 2D Codex pet for Raiden Shogun, ready for the Codex desktop app.

## Install

Keep `pet.json` and `spritesheet.webp` together in a folder named `raiden-shogun` under your Codex pets directory. Custom pet packages currently work in the Codex desktop app; Codex mobile does not display custom pets, and cross-device pet syncing is not supported.

## Package contents

- `pet.json` — Codex v2 manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation set

Rows 0–8 contain breathing and blinking, running right, independently drawn running left, greeting, jumping, failure, waiting for input, active task work, and result review. Rows 9–10 add sixteen clockwise look directions from `000` up through `337.5` up-left.

## Character details

The pet preserves Raiden Shogun's violet eyes, long braided purple hair, floral hair ornament, red ribbon accents, ornate white-and-violet Inazuman robes, layered sleeves, and purple-gold detailing. Her asymmetrical ornament and braid remain attached and recognizable throughout the animation set.

## Quality record

- The atlas passes Codex v2 geometry, transparency, unused-cell, and chroma validation without errors or warnings.
- All nine standard animation rows passed incremental frame checks and independent final playback review.
- Running left and right were drawn independently so the braid and costume asymmetry do not switch sides through mirroring.
- Three isolated reviewers confirmed the four cardinal direction hard gates.
- The labeled sixteen-direction loop stays in the intended quadrants without a yaw reversal; subtle intermediate-axis readings and two moderate hair-layout transitions remain documented as accepted QA warnings.
- All nine preview GIFs were rendered from the cleaned and validated final v2 atlas.

## Scope

2D only. No 3D version was generated in this run.

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/raiden-shogun/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\raiden-shogun\`；自定义 `CODEX_HOME` 时使用其 `pets/raiden-shogun/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/raiden-shogun/`
(default `~/.codex/pets/raiden-shogun/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。其余动作、neutral 和 16 个观察方向保持原版；ID 和 v2 格式不变。
The idle frames account for the desktop client's slow idle playback. Other states,
the neutral frame, all 16 look directions, the ID, and the v2 contract are preserved.

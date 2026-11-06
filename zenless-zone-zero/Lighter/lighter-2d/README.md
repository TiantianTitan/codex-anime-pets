# Lighter — Codex Pet v2 (2D)

This package contains a complete animated 2D Codex pet inspired by Lighter, built from the supplied character references and validated against the full Codex v2 pet contract.

## Install

Keep `pet.json` and `spritesheet.webp` together in a folder named `lighter` under your Codex pets directory. Custom pet packages currently work in the Codex desktop app; Codex mobile does not display custom pets, and cross-device pet syncing is not supported.

## Package contents

- `pet.json` — Codex v2 manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation set

Rows 0–8 cover breathing and blinking, running right, independently drawn running left, greeting, jumping, failure, waiting for input, active task work, and result review. Rows 9–10 add sixteen clockwise look directions from `000` up through `337.5` up-left.

## Character details

The pet preserves Lighter's tousled dark teal hair, dark sunglasses, long red scarf, charcoal biker jacket, dark green trousers, gold spikes and hardware, armored boots, and signature oversized gold mechanical gauntlet. The gauntlet remains attached to the correct arm throughout the animation set.

## Quality record

- The final atlas passes Codex v2 geometry, transparency, unused-cell, and chroma validation without errors or warnings.
- All nine standard animations passed incremental frame checks and independent playback review.
- Running left and right were drawn independently so Lighter's gauntlet and outfit asymmetry never switch sides.
- Jumping uses stable-slot extraction and plays as a clear low-to-high-to-low arc without camera zoom.
- The four cardinal directions passed the three-reviewer blind hard gates; the labeled sixteen-direction loop contains no wrong quadrant or reversal.
- Six near-axis or intermediate directions retain documented blind-reading warnings, while the ordered loop remains continuous and semantically correct at normal pet size.
- Continuity outliers at `157.5→180` and `247.5→270` were visually confirmed as smooth head-turn and profile-occlusion changes, not scale or registration pops.

## Scope

2D only. No 3D version was generated in this run.

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/lighter/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\lighter\`；自定义 `CODEX_HOME` 时使用其 `pets/lighter/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/lighter/`
(default `~/.codex/pets/lighter/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。其余动作、neutral 和 16 个观察方向保持原版；ID 和 v2 格式不变。
The idle frames account for the desktop client's slow idle playback. Other states,
the neutral frame, all 16 look directions, the ID, and the v2 contract are preserved.

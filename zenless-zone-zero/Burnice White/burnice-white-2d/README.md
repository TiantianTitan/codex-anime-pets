# Burnice White — Codex Pet v2 (2D)

This package contains a complete animated 2D Codex pet inspired by Burnice White, built from the supplied character references and validated against the full Codex v2 pet contract.

## Install

Keep `pet.json` and `spritesheet.webp` together in a folder named `burnice-white` under your Codex pets directory. Custom pet packages currently work in the Codex desktop app; Codex mobile does not display custom pets, and cross-device pet syncing is not supported.

## Package contents

- `pet.json` — Codex v2 manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation set

Rows 0–8 cover breathing and blinking, running right, independently drawn running left, greeting, jumping, failure, waiting for input, active task work, and result review. Rows 9–10 add sixteen clockwise look directions from `000` up through `337.5` up-left.

## Character details

The pet keeps Burnice's blonde twin ponytails, red-orange eyes, red-and-black goggles, flame-accented cropped biker jacket, red scarf, pleated skirt, asymmetric boots, gold details, and compact attached fuel backpack. The oversized handheld flamethrowers were omitted so every pose stays readable and unclipped at pet scale.

## Quality record

- The atlas passes Codex v2 geometry, transparency, unused-cell, and chroma validation with no errors or warnings.
- All nine standard animations passed incremental extraction checks and independent playback review.
- Running left and right were drawn independently to preserve canonical outfit and backpack asymmetry.
- Jumping uses stable-slot extraction and plays as a clear low-to-high-to-low arc without camera zoom.
- The four cardinal look directions passed three fresh isolated blind hard gates; all sixteen directions passed labeled loop review.
- Four near-axis intermediate directions retain documented blind-reading warnings, while the ordered loop remains in the intended quadrants without reversal.
- Measured changes at `157.5→180` and `337.5→000` were inspected in playback and read as intentional head-pitch silhouette changes rather than scale or registration pops.

## Scope

2D only. No 3D version was generated in this run.

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/burnice-white/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\burnice-white\`；自定义 `CODEX_HOME` 时使用其 `pets/burnice-white/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/burnice-white/`
(default `~/.codex/pets/burnice-white/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。该段记录此前的待机修复；后续动作调整见下节。
The idle frames account for the desktop client's slow idle playback. The later motion changes are recorded below.


<!-- MOTION-REFINEMENT-2026-11-06 -->
## 动作优化 / Motion refinement · 2026-11-06

调整动作：失败反馈。保持原帧数与客户端时序，改善配准、动作衔接或原图中的明显断裂。
本次未修改待机、neutral、16 个观察方向与宠物 ID。

Updated states: failed. Frame counts and client timing are unchanged.
Idle, the neutral cell, all 16 look directions, and the pet ID are unchanged in this update.

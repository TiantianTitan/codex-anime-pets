# Kiana Kaslana 琪亚娜·卡斯兰娜 — Codex Pet v2 (2D)

This is the finished 2D Codex pet package for Kiana Kaslana, based on the supplied Valkyrie combat-suit references and ready for the Codex desktop app.

## Install

Keep `pet.json` and `spritesheet.webp` together in a folder named `kiana-kaslana` under your Codex pets directory. Custom pet packages currently work in the Codex desktop app; Codex mobile does not display custom pets, and cross-device pet syncing is not supported.

## Package contents

- `pet.json` — Codex v2 manifest.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation set

Rows 0–8 cover breathing and blinking, running right, independently drawn running left, greeting, jumping, failure, waiting for input, active task work, and result review. Rows 9–10 add sixteen clockwise look directions from `000` up through `337.5` up-left.

## Character details

The pet keeps Kiana's bright blue eyes, long white twin braids, star hair clip, confident expression, white-and-black Valkyrie combat suit with orange accents, and a matched pair of compact pistols. Her asymmetric hair accessory stays on its canonical side in both independently drawn running directions.

## Quality record

- The atlas passes the Codex v2 geometry, transparency, and chroma validation with no errors or warnings.
- All nine standard animation rows passed incremental frame checks and independent final playback review.
- The first idle strip was rejected because neighboring silhouettes touched and could not be separated safely; the replacement uses clean gutters and passed extraction.
- The original upward cardinal touched a source-slot boundary, so only that anchor was redrawn. Three fresh isolated reviewers then confirmed all four cardinal direction gates.
- Four near-axis intermediate directions retain documented subtle-cue warnings. Labeled normal-size review confirms that every pose remains in the intended quadrant and the clockwise loop never reverses.
- The measured `337.5→000` envelope change was checked in the final animation and does not produce a conspicuous scale or registration pop. Two alternative repair rows were rejected because they reversed the left-facing arc.
- All nine published GIF previews were rendered from the cleaned and validated final v2 atlas.

## Scope

2D only. No 3D version was generated in this run.

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/kiana-kaslana/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\kiana-kaslana\`；自定义 `CODEX_HOME` 时使用其 `pets/kiana-kaslana/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/kiana-kaslana/`
(default `~/.codex/pets/kiana-kaslana/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。该段记录此前的待机修复；后续动作调整见下节。
The idle frames account for the desktop client's slow idle playback. The later motion changes are recorded below.


<!-- MOTION-REFINEMENT-2026-11-06 -->
## 动作优化 / Motion refinement · 2026-11-06

调整动作：失败反馈。保持原帧数与客户端时序，改善配准、动作衔接或原图中的明显断裂。
本次未修改待机、neutral、16 个观察方向与宠物 ID。

Updated states: failed. Frame counts and client timing are unchanged.
Idle, the neutral cell, all 16 look directions, and the pet ID are unchanged in this update.

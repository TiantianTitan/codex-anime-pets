# Otto Apocalypse 奥托·阿波卡利斯 — Codex Pet v2 (2D)

This is the finished 2D Codex pet package for Otto Apocalypse, drawn from the supplied classic violet-outfit references and ready for the Codex desktop app.

## Install

Keep `pet.json` and `spritesheet.webp` together in a folder named `otto-apocalypse` under your Codex pets directory. Custom pet packages currently work in the Codex desktop app; Codex mobile does not display custom pets, and cross-device pet syncing is not supported.

## Package contents

- `pet.json` — Codex v2 manifest.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation set

Rows 0–8 cover breathing and blinking, running right, independently drawn running left, greeting, jumping, failure, waiting for input, active task work, and result review. Rows 9–10 add sixteen clockwise look directions from `000` up through `337.5` up-left.

## Character details

The pet keeps Otto's pale-gold layered hair and tied side ponytail, green eyes, composed expression, navy-violet long coat with gold piping, shoulder capelet, white ruffled shirt, rose cravat, lavender waistcoat, white gloves, charcoal trousers, and brown boots. Costume asymmetry stays consistent across both running directions and the full look loop.

## Quality record

- The atlas passes the Codex v2 geometry and transparency validator with no errors or warnings.
- All nine standard animation rows passed deterministic frame checks and independent visual playback review.
- The first `270` look candidate was rejected when blind reviewers found its leftward face unclear. The complete row was redrawn, then three fresh isolated reviewers unanimously confirmed the `090` right and `270` left cardinals; `000` up and `180` down also passed.
- Seven near-axis intermediate directions keep documented subtle-cue warnings. Labeled normal-size review confirms that every pose remains in the intended quadrant and the loop never reverses.
- Reported transparency gaps are the natural openings between the legs and split coat tails. Boundary metrics were visually checked and show no conspicuous snap, scale pop, or registration jump.

## Scope

2D only. No 3D version was generated in this run.

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/otto-apocalypse/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\otto-apocalypse\`；自定义 `CODEX_HOME` 时使用其 `pets/otto-apocalypse/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/otto-apocalypse/`
(default `~/.codex/pets/otto-apocalypse/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。其余动作、neutral 和 16 个观察方向保持原版；ID 和 v2 格式不变。
The idle frames account for the desktop client's slow idle playback. Other states,
the neutral frame, all 16 look directions, the ID, and the v2 contract are preserved.

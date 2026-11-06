# Tartaglia 达达利亚 — Codex Pet v2 (2D)

This is the finished 2D Codex pet package for Tartaglia, ready for the Codex desktop app.

## Install

Keep `pet.json` and `spritesheet.webp` together in a folder named `tartaglia` under your Codex pets directory. Custom pet packages currently work in the Codex desktop app; Codex mobile does not display custom pets, and cross-device pet syncing is not supported.

## Package contents

- `pet.json` — Codex v2 manifest.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation set

Rows 0–8 cover breathing and blinking, running right, independently drawn running left, greeting, jumping, failure, waiting for input, active task work, and result review. Rows 9–10 add sixteen clockwise look directions from `000` up through `337.5` up-left.

## Character details

The pet keeps Tartaglia's orange hair, blue eyes, red hair ornament and earring, gray-and-white uniform, red scarf, dark gloves and boots, asymmetric shoulder armor, and Hydro Vision. The animation uses his own movement and expression without adding summoned weapons, water effects, scenery, logos, or text.

## Quality record

- The atlas passes Codex v2 geometry, transparency, and chroma validation with no errors or warnings.
- All nine standard animation rows passed frame extraction checks and independent playback review.
- The jumping row was rebuilt with one shared framing rule so its height change reads as a jump rather than a camera zoom.
- Two stray green edge pixels found during validation were removed by rebuilding from the untouched source strips with a stricter deterministic key threshold; the rebuilt atlas then passed cleanly.
- Three isolated reviewers confirmed the four cardinal direction gates. Subtle intermediate cues remain documented as warnings, while the labeled full-size loop stays in the intended quadrants without reversing.
- Continuity outliers were checked in playback and do not create visible snapping, attachment breaks, or scale flashes.
- All nine published GIF previews were rendered from the cleaned and validated final v2 atlas.

## Scope

2D only. No 3D version was generated in this run.

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/tartaglia/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\tartaglia\`；自定义 `CODEX_HOME` 时使用其 `pets/tartaglia/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/tartaglia/`
(default `~/.codex/pets/tartaglia/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。其余动作、neutral 和 16 个观察方向保持原版；ID 和 v2 格式不变。
The idle frames account for the desktop client's slow idle playback. Other states,
the neutral frame, all 16 look directions, the ID, and the v2 contract are preserved.

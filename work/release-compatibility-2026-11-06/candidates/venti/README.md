# Venti — Codex Pet v2 (2D)

A finished Venti companion for the Codex desktop app: bright, playful, and always carrying a little Mondstadt breeze with him.

## Install

Keep `pet.json` and `spritesheet.webp` together in a folder named `venti` under your Codex pets directory. Custom pet packages currently work in the Codex desktop app; Codex mobile does not display custom pets, and cross-device pet syncing is not supported.

## Package contents

- `pet.json` — Codex v2 pet manifest.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation set

Rows 0–8 cover breathing and blinking, running right, independently drawn running left, greeting, jumping, failure, waiting for input, active task work, and result review. Rows 9–10 add sixteen clockwise look directions from `000` up through `337.5` up-left.

## Character details

The pet keeps Venti's teal eyes, navy hair and teal-tipped braids, green bard cap with cream flower and feather, green-and-cream cape, white ruffled shirt, green shorts, white tights, brown shoes, and ornate wooden lyre. His movements stay light and cheerful while the hat, braids, cape, and lyre remain connected and easy to read at desktop size.

## Quality record

- The atlas passes Codex v2 geometry, transparency, and chroma validation with no errors or warnings.
- All nine standard animation rows passed deterministic extraction checks and independent normal-size playback review.
- Five isolated blind reviews confirmed the `000`, `090`, `180`, and `270` cardinal direction gates.
- Subtle non-cardinal cues at `135`, `157.5`, and `337.5` are documented as review warnings; the labeled clockwise loop stays in the intended quadrants without reversal.
- All nine published GIF previews were rendered from the cleaned and validated final atlas.

## Scope

2D only. No 3D version was generated in this run.

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/venti/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\venti\`；自定义 `CODEX_HOME` 时使用其 `pets/venti/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/venti/`
(default `~/.codex/pets/venti/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机未发现长时间闭眼问题，保留原图。其余动作、neutral 和 16 个观察方向保持原版；ID 和 v2 格式不变。
The idle frames account for the desktop client's slow idle playback. Other states,
the neutral frame, all 16 look directions, the ID, and the v2 contract are preserved.

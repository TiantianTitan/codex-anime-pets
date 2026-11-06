# Seele Vollerei — Codex Pet v2 (2D)

A finished Seele Vollerei companion for the Codex desktop app, wearing her classic blue-and-white outfit with a gentle presence and restrained, expressive motion.

## Install

Keep `pet.json` and `spritesheet.webp` together in a folder named `seele-vollerei` under your Codex pets directory. Custom pet packages currently work in the Codex desktop app; Codex mobile does not display custom pets, and cross-device pet syncing is not supported.

## Package contents

- `pet.json` — Codex v2 pet manifest.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation set

Rows 0–8 cover breathing and blinking, running right, running left, greeting, jumping, failure, waiting for input, active task work, and result review. Rows 9–10 add sixteen clockwise look directions from `000` up through `337.5` up-left.

## Character details

The pet keeps Seele's short blue-black bob with cobalt-violet tips, bright blue eyes, white short sleeves, deep-cobalt fitted vest dress, layered navy-violet butterfly skirt, white thigh-highs, and dark Mary Jane shoes. The neutral design is unarmed and stays separate from her long-haired armored alternate costume.

## Quality record

- The atlas passes Codex v2 geometry, transparency, chroma, and unused-cell validation with no errors or warnings.
- All nine standard animation rows passed deterministic checks and independent normal-size playback review.
- The jump row uses stable-slot extraction to preserve one sprite scale and a genuine low-to-apex-to-low arc.
- Three isolated blind reviewers confirmed all fourteen horizontal and vertical direction challenges, including both cardinal hard gates.
- The full sixteen-direction loop passed labeled semantic review and adjacent-frame continuity measurement without warnings.
- All nine published GIF previews were rendered from the cleaned and validated final v2 atlas.

## Scope

2D only. No 3D version was generated in this run.

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/seele-vollerei/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\seele-vollerei\`；自定义 `CODEX_HOME` 时使用其 `pets/seele-vollerei/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/seele-vollerei/`
(default `~/.codex/pets/seele-vollerei/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。其余动作、neutral 和 16 个观察方向保持原版；ID 和 v2 格式不变。
The idle frames account for the desktop client's slow idle playback. Other states,
the neutral frame, all 16 look directions, the ID, and the v2 contract are preserved.

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

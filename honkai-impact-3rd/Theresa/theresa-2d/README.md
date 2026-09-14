# Theresa — Codex Pet v2 (2D)

A finished Theresa companion for the Codex desktop app, wearing her classic black-and-white nun-inspired battle dress with bright cyan eyes and a poised, determined presence.

## Install

Keep `pet.json` and `spritesheet.webp` together in a folder named `theresa` under your Codex pets directory. Custom pet packages currently work in the Codex desktop app; Codex mobile does not display custom pets, and cross-device pet syncing is not supported.

## Package contents

- `pet.json` — Codex v2 pet manifest.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation set

Rows 0–8 cover breathing and blinking, running right, running left, greeting, jumping, failure, waiting for input, active task work, and result review. Rows 9–10 add sixteen clockwise look directions from `000` up through `337.5` up-left.

## Character details

The pet keeps Theresa's short layered silver-white hair, two long curled side locks, vivid cyan-blue eyes, dark fitted bodice and sleeves, black gloves, gold cross trim, layered white ruffled skirt, pale stockings, and dark ankle boots with gold accents. The compact pet design is unarmed and remains separate from the winter-cape costume found in some source art.

## Quality record

- The atlas passes Codex v2 geometry, transparency, chroma, and unused-cell validation with no structural errors or warnings.
- All nine standard animation rows passed deterministic checks and independent normal-size playback review.
- The jump row uses stable-slot extraction to preserve one sprite scale and a genuine low-to-apex-to-low arc.
- Three isolated blind reviewers confirmed both cardinal hard gates: up versus down and screen-right versus screen-left.
- Subtle near-front diagonal cues remain documented review warnings; labeled normal-size inspection confirms the correct quadrants and a continuous clockwise loop without reversal.
- All nine published GIF previews were rendered from the cleaned and validated final v2 atlas.

## Scope

2D only. No 3D version was generated in this run.

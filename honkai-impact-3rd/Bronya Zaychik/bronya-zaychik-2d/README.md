# Bronya Zaychik — Codex Pet v2 (2D)

A finished Bronya Zaychik companion for the Codex desktop app, wearing her classic Valkyrie Chariot uniform with the calm focus and exact movements that define her.

## Install

Keep `pet.json` and `spritesheet.webp` together in a folder named `bronya-zaychik` under your Codex pets directory. Custom pet packages currently work in the Codex desktop app; Codex mobile does not display custom pets, and cross-device pet syncing is not supported.

## Package contents

- `pet.json` — Codex v2 pet manifest.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation set

Rows 0–8 cover breathing and blinking, running right, independently drawn running left, greeting, jumping, failure, waiting for input, active task work, and result review. Rows 9–10 add sixteen clockwise look directions from `000` up through `337.5` up-left.

## Character details

The pet keeps Bronya's silver-gray drill twin-tails, large navy bows, gray eyes, deep-blue military jacket and pleated skirt, red accents, gold shoulder braid, white mechanical gauntlets, and white-red armored boots. The directional rows preserve her fixed costume asymmetry while her eyes, eyelids, head, and twin-tails move as one restrained gaze system.

## Quality record

- The atlas passes Codex v2 geometry, transparency, chroma, and unused-cell validation with no errors or warnings.
- All nine standard animation rows passed deterministic checks and independent normal-size playback review.
- The jump row uses stable-slot extraction to preserve one sprite scale and a genuine low-to-apex-to-low arc.
- Three isolated blind reviewers confirmed all fourteen horizontal and vertical direction challenges, including both cardinal hard gates.
- Subtle secondary-axis cues at `067.5`, `112.5`, and `337.5` are documented as visual-review warnings; the labeled clockwise loop remains continuous and never reverses.
- All nine published GIF previews were rendered from the cleaned and validated final v2 atlas.

## Scope

2D only. No 3D version was generated in this run.

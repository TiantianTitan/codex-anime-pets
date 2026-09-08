# Fu Hua — Codex Pet v2 (2D)

A finished Fu Hua companion for the Codex desktop app: calm, precise, and always ready to meet the next challenge with measured confidence.

## Install

Keep `pet.json` and `spritesheet.webp` together in a folder named `fu-hua` under your Codex pets directory. Custom pet packages currently work in the Codex desktop app; Codex mobile does not display custom pets, and cross-device pet syncing is not supported.

## Package contents

- `pet.json` — Codex v2 pet manifest.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation set

Rows 0–8 cover breathing and blinking, running right, independently drawn running left, greeting, jumping, failure, waiting for input, active task work, and result review. Rows 9–10 add sixteen clockwise look directions from `000` up through `337.5` up-left.

## Character details

The pet keeps Fu Hua's cyan eyes, red rectangular glasses, slate blue-violet hair, low side ponytail with its red bead, blue-and-white Accipiter combat tunic, dark fitted trousers, and brown lace-up boots. Her movement stays controlled and martial, while the glasses, ponytail, uniform panels, and body proportions remain coherent through every pose.

## Quality record

- The atlas passes Codex v2 geometry, transparency, chroma, and unused-cell validation with no errors or warnings.
- All nine standard animation rows passed deterministic checks and independent normal-size playback review.
- Three isolated blind reviewers unanimously confirmed the `000`/`180` vertical and `090`/`270` horizontal cardinal gates.
- Subtle secondary-axis cues at several near-cardinal diagonals are documented as review warnings; the labeled clockwise loop stays in the intended quadrants without reversal.
- All nine published GIF previews were rendered from the cleaned and validated final atlas.

## Scope

2D only. No 3D version was generated in this run.

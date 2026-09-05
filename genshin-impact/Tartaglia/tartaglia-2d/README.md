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

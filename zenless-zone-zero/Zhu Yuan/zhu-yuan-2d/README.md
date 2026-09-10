# Zhu Yuan — Codex Pet v2 (2D)

A finished Zhu Yuan companion for the Codex desktop app, carrying her focused Public Security presence into a compact animated form.

## Install

Keep `pet.json` and `spritesheet.webp` together in a folder named `zhu-yuan` under your Codex pets directory. Custom pet packages currently work in the Codex desktop app; Codex mobile does not display custom pets, and mobile installation and cross-device pet syncing are not supported.

## Package contents

- `pet.json` — Codex v2 pet manifest.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation set

Rows 0–8 cover breathing and blinking, running right, independently drawn running left, greeting, jumping, failure, waiting for input, active task work, and result review. Rows 9–10 add sixteen clockwise look directions from `000` up through `337.5` up-left.

## Character details

The pet keeps Zhu Yuan's amber-red eyes, charcoal-black high ponytail, orange-red hair streak, blue cropped Public Security jacket, silver shoulder armor, black combat uniform, lime accents, armored boots, holster, and sidearm. Her eyes, eyelids, head, ponytail, and upper body turn together through the complete look loop while her equipment stays attached and consistent.

## Quality record

- The atlas passes Codex v2 geometry, transparency, chroma, and unused-cell validation with no errors or warnings.
- All nine standard animations passed deterministic checks and independent normal-size playback review.
- The jump row uses stable-slot extraction to keep one character scale through crouch, ascent, apex, landing, and stand.
- Three isolated blind reviewers confirmed both cardinal direction gates; subtle intermediate-axis cues are documented and accepted after labeled loop review.
- Both direction-row boundaries preserve the same attached ponytail without a side-swap or visible registration snap.
- All nine published GIF previews were rendered from the cleaned and validated final v2 atlas.

## Scope

2D only. No 3D version was generated in this run.

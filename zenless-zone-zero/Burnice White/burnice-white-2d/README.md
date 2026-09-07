# Burnice White — Codex Pet v2 (2D)

This package contains a complete animated 2D Codex pet inspired by Burnice White, built from the supplied character references and validated against the full Codex v2 pet contract.

## Install

Keep `pet.json` and `spritesheet.webp` together in a folder named `burnice-white` under your Codex pets directory. Custom pet packages currently work in the Codex desktop app; Codex mobile does not display custom pets, and cross-device pet syncing is not supported.

## Package contents

- `pet.json` — Codex v2 manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation set

Rows 0–8 cover breathing and blinking, running right, independently drawn running left, greeting, jumping, failure, waiting for input, active task work, and result review. Rows 9–10 add sixteen clockwise look directions from `000` up through `337.5` up-left.

## Character details

The pet keeps Burnice's blonde twin ponytails, red-orange eyes, red-and-black goggles, flame-accented cropped biker jacket, red scarf, pleated skirt, asymmetric boots, gold details, and compact attached fuel backpack. The oversized handheld flamethrowers were omitted so every pose stays readable and unclipped at pet scale.

## Quality record

- The atlas passes Codex v2 geometry, transparency, unused-cell, and chroma validation with no errors or warnings.
- All nine standard animations passed incremental extraction checks and independent playback review.
- Running left and right were drawn independently to preserve canonical outfit and backpack asymmetry.
- Jumping uses stable-slot extraction and plays as a clear low-to-high-to-low arc without camera zoom.
- The four cardinal look directions passed three fresh isolated blind hard gates; all sixteen directions passed labeled loop review.
- Four near-axis intermediate directions retain documented blind-reading warnings, while the ordered loop remains in the intended quadrants without reversal.
- Measured changes at `157.5→180` and `337.5→000` were inspected in playback and read as intentional head-pitch silhouette changes rather than scale or registration pops.

## Scope

2D only. No 3D version was generated in this run.

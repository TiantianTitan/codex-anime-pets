# Lighter — Codex Pet v2 (2D)

This package contains a complete animated 2D Codex pet inspired by Lighter, built from the supplied character references and validated against the full Codex v2 pet contract.

## Install

Keep `pet.json` and `spritesheet.webp` together in a folder named `lighter` under your Codex pets directory. Custom pet packages currently work in the Codex desktop app; Codex mobile does not display custom pets, and cross-device pet syncing is not supported.

## Package contents

- `pet.json` — Codex v2 manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation set

Rows 0–8 cover breathing and blinking, running right, independently drawn running left, greeting, jumping, failure, waiting for input, active task work, and result review. Rows 9–10 add sixteen clockwise look directions from `000` up through `337.5` up-left.

## Character details

The pet preserves Lighter's tousled dark teal hair, dark sunglasses, long red scarf, charcoal biker jacket, dark green trousers, gold spikes and hardware, armored boots, and signature oversized gold mechanical gauntlet. The gauntlet remains attached to the correct arm throughout the animation set.

## Quality record

- The final atlas passes Codex v2 geometry, transparency, unused-cell, and chroma validation without errors or warnings.
- All nine standard animations passed incremental frame checks and independent playback review.
- Running left and right were drawn independently so Lighter's gauntlet and outfit asymmetry never switch sides.
- Jumping uses stable-slot extraction and plays as a clear low-to-high-to-low arc without camera zoom.
- The four cardinal directions passed the three-reviewer blind hard gates; the labeled sixteen-direction loop contains no wrong quadrant or reversal.
- Six near-axis or intermediate directions retain documented blind-reading warnings, while the ordered loop remains continuous and semantically correct at normal pet size.
- Continuity outliers at `157.5→180` and `247.5→270` were visually confirmed as smooth head-turn and profile-occlusion changes, not scale or registration pops.

## Scope

2D only. No 3D version was generated in this run.

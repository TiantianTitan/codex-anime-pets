# Anby Demara — Codex Pet v2 (2D)

This package contains a complete 2D animated Codex pet inspired by Anby Demara. It was created from the supplied character references and validated against the full Codex v2 pet contract.

## Contents

- `pet.json` — pet manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation layout

- Rows 0–8: idle, running-right, independently drawn running-left, waving, jumping, failed, waiting, active task processing, and review.
- Rows 9–10: sixteen clockwise look directions from `000` up through `337.5` up-left.

## Visual identity

The atlas preserves Anby's short silver bob, black headband, amber eyes, lime-and-black tactical jacket, pleated skirt, asymmetric stockings, sneakers, mechanical backpack rig, and attached sheathed sword. Her asymmetric outfit and equipment remain physically coherent throughout motion and gaze changes.

## Quality gates

- Exact v2 geometry, RGBA transparency, unused-cell transparency, and final chroma-edge cleanup passed.
- All nine standard animation rows passed deterministic inspection and independent visual QA.
- The jumping row uses stable-slot extraction so its character scale remains constant while the body follows a clear low-to-high-to-low trajectory.
- Rightward and leftward running were drawn independently to preserve outfit and equipment handedness.
- All four cardinal directions passed the three-reviewer blind hard gates; all sixteen directions passed labeled semantic and continuity review.
- Near-vertical intermediate directions retain reviewed horizontal-axis warnings because their isolated blind readings disagreed, while the labeled loop remains monotonic with no wrong quadrant or reversal.
- The packaged atlas validates as 1536×2288 with no structural errors or warnings.

## Scope

2D only. No 3D version was generated in this run.

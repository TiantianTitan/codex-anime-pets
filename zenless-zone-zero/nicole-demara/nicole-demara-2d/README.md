# Nicole Demara · 妮可·德玛拉 — Codex Pet v2 (2D)

This package contains a complete 2D animated Codex pet inspired by Nicole Demara. It was created from the supplied character references and validated against the full Codex v2 pet contract.

## Contents

- `pet.json` — pet manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation layout

- Rows 0–8: idle, running-right, independently drawn running-left, waving, jumping, failed, waiting, active task processing, and review.
- Rows 9–10: sixteen clockwise look directions from `000` up through `337.5` up-left.

## Visual identity

The atlas preserves Nicole's pink twin-tails, black bow roots, lime-green eyes, cropped black-and-white streetwear, orange accents, mismatched stockings, heavy boots, green Bangboo pouch, and attached black case. Her asymmetrical outfit and props remain physically coherent through motion and gaze changes.

## Quality gates

- Exact v2 geometry, RGBA transparency, unused-cell transparency, and final chroma-edge cleanup passed.
- All nine standard animation rows passed deterministic inspection and independent visual QA.
- Rightward and leftward running were drawn independently so the asymmetric costume and props remain consistent.
- All four cardinal directions passed a fresh three-reviewer blind majority; all sixteen directions passed labeled semantic and continuity review.
- The subtle upward component at `292.5` was retained as a reviewed intermediate warning because the labeled loop advances coherently through `315` and `337.5` without reversal.
- The packaged atlas validates as 1536×2288 with no structural errors or warnings.

## Scope

2D only. No 3D version was generated in this run.

# Jane Doe · 简·杜 — Codex Pet v2 (2D)

This package contains a complete 2D animated Codex pet inspired by Jane Doe. It was created from the supplied character references and validated against the full Codex v2 pet contract.

## Contents

- `pet.json` — pet manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation layout

- Rows 0–8: idle, running-right, independently drawn running-left, waving, jumping, failed, waiting, active task processing, and review.
- Rows 9–10: sixteen clockwise look directions from `000` up through `337.5` up-left.

## Visual identity

The atlas preserves Jane's short black bob, wine-red rear hair, pink rat ears, narrow green eyes, cream fur collar, blue-gray cropped jacket, tactical shorts, asymmetrical stockings and boots, red accents, and one long attached charcoal tail. Her outfit asymmetry and flexible tail remain physically coherent across movement and gaze changes.

## Quality gates

- Exact v2 geometry, RGBA transparency, unused-cell transparency, and the single final chroma-edge cleanup passed.
- All nine standard animation rows passed deterministic inspection and independent visual QA.
- Leftward and rightward running were drawn independently so the asymmetric outfit and tail construction remain consistent.
- All four cardinal directions passed a fresh three-reviewer blind majority; all sixteen directions passed labeled semantic and continuity review.
- Subtle intermediate-axis cues at `022.5`, `157.5`, `292.5`, `315`, and `337.5` remain recorded as reviewed warnings because the labeled clockwise loop preserves the intended quadrants without reversal.
- The packaged atlas validates as 1536×2288 with no structural errors or warnings.

## Scope

2D only. No 3D version was generated in this run.

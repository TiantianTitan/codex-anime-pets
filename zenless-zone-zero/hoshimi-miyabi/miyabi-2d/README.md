# Hoshimi Miyabi · 星见雅 — Codex Pet v2 (2D)

This package contains the completed 2D animated Codex pet inspired by Hoshimi Miyabi. It was built from the supplied character references and validated against the full Codex v2 pet contract.

## Contents

- `pet.json` — pet manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation layout

- Rows 0–8: idle, running-right, independently drawn running-left, waving, jumping, failed, waiting, active task processing, and review.
- Rows 9–10: sixteen clockwise look directions from `000` up through `337.5` up-left.

## Visual identity

The atlas preserves Miyabi's navy-black hair, tall fox ears, red eyes, teal-white-black uniform, asymmetric mechanical arm with red braided cord, teal sleeve, and attached sheathed katana. Costume sides and sword anchoring remain coherent through motion and gaze changes.

## Quality gates

- Exact v2 geometry, RGBA transparency, unused-cell transparency, and a single final chroma-edge cleanup passed.
- All nine standard animation rows passed deterministic inspection and independent visual QA.
- Rightward and leftward running were drawn independently so the asymmetric costume remains physically consistent.
- All sixteen look directions passed labeled semantic review and three-reviewer blind majority validation with no errors, warnings, ambiguous cells, or unconfirmed pairs.
- Metric continuity warnings at the pure-profile transitions and the `157.5→180` row boundary were visually reviewed and resolved as normal perspective changes, with no direction reversal, ground shift, broken attachment, or identity jump. The rebuilt `337.5→000` loop boundary now closes without a continuity warning.
- The packaged atlas validates as 1536×2288 with no structural errors or warnings.

## Scope

2D only. No 3D version was generated in this run.

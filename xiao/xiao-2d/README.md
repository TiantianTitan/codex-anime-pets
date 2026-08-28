# Xiao 魈 — Codex Pet v2 (2D)

This local package contains the completed 2D animated desktop pet inspired by Xiao. It was produced from the five supplied references and validated against the complete Codex v2 pet contract.

## Contents

- `pet.json` — pet manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation layout

- Rows 0–8: idle, running-right, independently drawn running-left, waving, jumping, failed, waiting, active task processing, and review.
- Rows 9–10: sixteen clockwise look directions from `000` up through `337.5` up-left.

## Visual identity

The atlas preserves Xiao's golden eyes, purple forehead diamond, dark teal-tipped hair, exposed green tattooed arm, opposite black glove, sleeveless white top, purple/navy outfit, jade and bead ornaments, attached sash tails, and secured Yaksha mask across every state.

## Quality gates

- Exact v2 geometry and transparent-cell validation passed.
- All nine standard animation rows passed deterministic and independent visual QA.
- Four cardinal directions passed three isolated blind reviews.
- The full 16-direction loop passed labeled semantic and continuity review.
- The final chroma-despill pass completed successfully with alpha preserved.

## Scope

2D only. This package has not been installed into Codex, uploaded, or published, and no 3D version was generated.

# Yae Miko 八重神子 — Codex Pet v2 (2D)

This local package contains the completed 2D animated desktop pet inspired by Yae Miko. It was built from the supplied character references and validated against the complete Codex v2 pet contract.

## Contents

- `pet.json` — pet manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation layout

- Rows 0–8: idle, running-right, independently drawn running-left, waving, jumping, failed, waiting, active task processing, and review.
- Rows 9–10: sixteen clockwise look directions from `000` up through `337.5` up-left.

## Visual identity

The atlas preserves Yae Miko's flowing sakura-pink hair, violet eyes, layered golden crown ornaments, purple gemstone earrings, red-white-black-purple shrine-maiden outfit, wide sleeves, and composed playful expression. No weapon or visible fox tails were added.

## Quality gates

- Exact v2 geometry, transparent-cell validation, and edge cleanup passed.
- All nine standard animation rows passed deterministic and independent visual QA.
- The jumping row uses stable-slot extraction so its generated vertical motion remains intact without scale popping.
- Four cardinal directions passed three isolated blind reviews.
- The complete 16-direction loop passed labeled semantic and continuity review.

## Scope

2D only. This package has not been installed into Codex, uploaded, or published, and no 3D version was generated.

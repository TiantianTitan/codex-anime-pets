# Hu Tao 胡桃 — Codex Pet v2 (2D)

This package contains the completed 2D animated Codex pet inspired by Hu Tao. It was built from the supplied character art and chibi references, then validated against the complete Codex v2 pet contract.

## Contents

- `pet.json` — pet manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation layout

- Rows 0–8: idle, running-right, independently drawn running-left, waving, jumping, failed, waiting, active task processing, and review.
- Rows 9–10: sixteen clockwise look directions from `000` up through `337.5` up-left.

## Visual identity

The atlas preserves Hu Tao's flower-shaped crimson eyes, tall dark hat with beige talisman plaque, plum-blossom branch and tassel, long dark-brown hair fading toward muted red, deep brown-black-red-gold uniform, long coat tails, white socks with red accents, and playful expression language. Her hat decorations keep their original handedness in both travel directions.

## Quality gates

- Exact v2 geometry, transparent-cell validation, and one final chroma-edge cleanup pass succeeded.
- All nine standard animation rows passed deterministic frame checks and independent visual QA.
- The jumping row uses stable-slot extraction so anticipation, lift, peak, descent, and landing remain visible without scale popping.
- Four cardinal directions passed hard semantic gates; the complete 16-direction loop passed labeled review and three isolated blind reviews.
- The two near-up intermediate directions retain subtle horizontal cues and are recorded as reviewed warnings, while all four cardinals remain unmistakable.

## Scope

2D only. No 3D version was generated in this run.

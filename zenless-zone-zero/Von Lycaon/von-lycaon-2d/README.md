# Von Lycaon · 冯·莱卡恩 — Codex Pet v2 (2D)

This package contains a complete 2D animated Codex companion inspired by Von Lycaon, prepared for the Codex v2 pet format.

## Contents

- `pet.json` — pet manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation layout

- Rows 0–8: idle, running-right, independently drawn running-left, waving, jumping, failed, waiting, active task processing, and review.
- Rows 9–10: sixteen clockwise look directions from `000` up through `337.5` up-left.

## Visual identity

The atlas keeps Lycaon's ivory wolf ears and swept hair, red eyes, black muzzle markings, red cravat, tailored black-and-white uniform, gold chain, mechanical legs, and large attached white tail consistent across every motion and gaze direction.

## Quality gates

- Exact v2 geometry, RGBA transparency, unused-cell transparency, and one-pass chroma-edge cleanup passed.
- All nine standard animation rows passed deterministic inspection and independent frame-by-frame visual QA.
- Running-left was drawn independently so the character's facial, uniform, chain, and tail details remain coherent.
- All four cardinal directions passed a fresh three-reviewer blind majority; all sixteen directions passed labeled semantic and continuity review.
- The profile-to-three-quarter silhouette change at `270→292.5` was reviewed at normal pet size and accepted without a visible scale or baseline pop.
- The packaged atlas validates as 1536×2288 with no structural errors or warnings.

## Compatibility

Custom pet packages currently support the Codex desktop app. Mobile installation, mobile pet display, and cross-device pet syncing are not supported.

## Scope

2D only. No 3D edition is included.

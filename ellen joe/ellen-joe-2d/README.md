# Ellen Joe 艾莲·乔 — Codex Pet v2 (2D)

This package contains a completed 2D animated Codex pet inspired by Ellen Joe. It was built from the supplied character references and validated against the full Codex v2 pet contract.

## Contents

- `pet.json` — pet manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation layout

- Rows 0–8: idle, running-right, independently drawn running-left, waving, jumping, failed, waiting, active task processing, and review.
- Rows 9–10: sixteen clockwise look directions from `000` up through `337.5` up-left.

## Visual identity

The atlas preserves Ellen Joe's charcoal-black bob with red inner layers, warm red eyes, maid headdress with metallic spikes, black-and-white industrial maid outfit, belts, cuffs, stockings, platform shoes, and physically attached shark tail. Her oversized scissors and detached effects were omitted to keep every 192×208 animation cell clear and readable.

## Quality gates

- Exact v2 geometry, transparency, chroma-spill cleanup, and package validation passed.
- All nine standard animation rows passed deterministic extraction and independent visual review.
- Four cardinal directions passed isolated blind review; all sixteen directions passed labeled semantic and continuity review.
- Rejected animation attempts were regenerated as complete coherent rows rather than patched cell by cell.

## Scope

2D only. No 3D version was generated in this run.

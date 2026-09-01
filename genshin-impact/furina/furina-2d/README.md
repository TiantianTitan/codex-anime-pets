# Furina 芙宁娜 — Codex Pet v2 (2D)

This package contains the completed 2D animated Codex pet inspired by Furina. It uses her short-haired dark-navy Fontaine outfit and was built from the supplied references, then validated against the complete Codex v2 pet contract.

## Contents

- `pet.json` — pet manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation layout

- Rows 0–8: idle, running-right, independently drawn running-left, waving, jumping, failed, waiting, active task processing, and review.
- Rows 9–10: sixteen clockwise look directions from `000` up through `337.5` up-left.

## Visual identity

The atlas preserves Furina's white-and-pale-cyan bob, curled forelock, blue water-drop eyes, navy crown-like top hat with gold prongs, dark Fontaine tailcoat, white ruffles, blue gemstone bows, black shorts, gloves, and poised theatrical personality. The alternate long-haired white outfit, cane, scroll, Hydro summons, bubbles, and detached effects were intentionally excluded.

## Quality gates

- Exact v2 geometry, transparent-cell validation, and one final edge-cleanup pass succeeded.
- All nine standard animation rows passed deterministic extraction checks and independent visual QA.
- The jumping row uses stable-slot extraction so its anticipation, airborne apex, descent, and landing remain visible without scale popping.
- Four cardinal directions passed three isolated blind reviews; the complete 16-direction loop passed labeled semantic and continuity review.
- Rejected rows were regenerated as complete coherent strips rather than patched cell by cell.

## Scope

2D only. No 3D version was generated in this run.

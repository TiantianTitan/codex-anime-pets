# Acheron 黄泉 — Codex Pet v2 (2D)

This package contains the completed 2D animated Codex pet inspired by Acheron. It preserves her canonical purple-haired form and was built from the supplied references, then validated against the complete Codex v2 pet contract.

## Contents

- `pet.json` — pet manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation layout

- Rows 0–8: idle, running-right, independently drawn running-left, waving, jumping, failed, waiting, active task processing, and review.
- Rows 9–10: sixteen clockwise look directions from `000` up through `337.5` up-left.

## Visual identity

The atlas preserves Acheron's deep indigo-violet hair, asymmetrical fringe covering the viewer-right eye, visible violet-magenta eye, gem choker, white-lilac-black cropped jacket, violet flame motifs, shoulder armor, black shorts, thigh straps, long boots, gloves, and compact attached katana. The red-and-white transformed form, guitar, alternate dress, scenery, text, and detached effects were intentionally excluded.

## Quality gates

- Exact v2 geometry, transparent-cell validation, and one final edge-cleanup pass succeeded.
- All nine standard animation rows passed deterministic extraction checks and independent visual QA.
- Up, right, down, and left passed three isolated blind direction reviews.
- The complete 16-direction loop passed labeled semantic and continuity review; subtle horizontal uncertainty in six near-down intermediate poses is retained as an accepted review warning because the labeled loop stays in the correct quadrants without reversal.
- Rejected direction rows were regenerated as complete coherent strips rather than patched cell by cell.

## Scope

2D only. No 3D version was generated in this run.

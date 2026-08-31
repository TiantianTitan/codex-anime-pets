# Blade · 刃 — Codex Pet v2 (2D)

This package contains the completed 2D animated Codex pet inspired by Blade. It was built from the supplied character references and validated against the full Codex v2 pet contract.

## Contents

- `pet.json` — pet manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation layout

- Rows 0–8: idle, running-right, independently drawn running-left, waving, jumping, failed, waiting, active task processing, and review.
- Rows 9–10: sixteen clockwise look directions from `000` up through `337.5` up-left.

## Visual identity

The atlas preserves Blade's layered navy hair with wine-red tips, long rear hair, visible amber-red eye, long red earring, ornate bronze chest panel, black coat with dark blue patterns, pale trousers, red lining, black gloves and boots, and asymmetric white bandages. His expression stays restrained and severe across the animation set; the sword is omitted from neutral direction poses so gaze remains readable from the character himself.

## Quality gates

- Exact v2 geometry, RGBA transparency, unused-cell transparency, and final chroma-edge cleanup succeeded.
- All nine standard animation rows passed deterministic frame inspection with no errors or warnings.
- Leftward and rightward running were drawn independently so Blade's asymmetric bandages, earring, coat, and hair remain physically consistent.
- All four cardinal directions passed the hard semantic gates in three fresh isolated blind reviews; the combined blind validation has `ok: true`.
- Every horizontal direction pair passed. Intermediate vertical cues at `067.5`, `112.5`, and `292.5` remain documented warnings because their pitch is subtle in isolation; labeled loop review confirmed the intended quadrants with no reversal.
- Continuity warnings at `157.5→180`, `270→292.5`, and `337.5→000` were independently reviewed at normal pet size and accepted because no conspicuous snap, scale pop, identity change, or direction reversal is visible.
- The completed package was validated as a 1536×2288 Codex v2 atlas with no structural errors or warnings.

## Scope

2D only. No 3D version was generated in this run.

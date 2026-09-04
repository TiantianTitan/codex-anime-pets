# Kiana Kaslana 琪亚娜·卡斯兰娜 — Codex Pet v2 (2D)

This is the finished 2D Codex pet package for Kiana Kaslana, based on the supplied Valkyrie combat-suit references and ready for the Codex desktop app.

## Install

Keep `pet.json` and `spritesheet.webp` together in a folder named `kiana-kaslana` under your Codex pets directory. Custom pet packages currently work in the Codex desktop app; Codex mobile does not display custom pets, and cross-device pet syncing is not supported.

## Package contents

- `pet.json` — Codex v2 manifest.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation set

Rows 0–8 cover breathing and blinking, running right, independently drawn running left, greeting, jumping, failure, waiting for input, active task work, and result review. Rows 9–10 add sixteen clockwise look directions from `000` up through `337.5` up-left.

## Character details

The pet keeps Kiana's bright blue eyes, long white twin braids, star hair clip, confident expression, white-and-black Valkyrie combat suit with orange accents, and a matched pair of compact pistols. Her asymmetric hair accessory stays on its canonical side in both independently drawn running directions.

## Quality record

- The atlas passes the Codex v2 geometry, transparency, and chroma validation with no errors or warnings.
- All nine standard animation rows passed incremental frame checks and independent final playback review.
- The first idle strip was rejected because neighboring silhouettes touched and could not be separated safely; the replacement uses clean gutters and passed extraction.
- The original upward cardinal touched a source-slot boundary, so only that anchor was redrawn. Three fresh isolated reviewers then confirmed all four cardinal direction gates.
- Four near-axis intermediate directions retain documented subtle-cue warnings. Labeled normal-size review confirms that every pose remains in the intended quadrant and the clockwise loop never reverses.
- The measured `337.5→000` envelope change was checked in the final animation and does not produce a conspicuous scale or registration pop. Two alternative repair rows were rejected because they reversed the left-facing arc.
- All nine published GIF previews were rendered from the cleaned and validated final v2 atlas.

## Scope

2D only. No 3D version was generated in this run.

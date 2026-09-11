# Vivian Banshee — Codex Pet v2 (2D)

A finished Vivian Banshee companion for the Codex desktop app, pairing gothic elegance with restrained, expressive motion beneath her signature lilac parasol.

## Install

Keep `pet.json` and `spritesheet.webp` together in a folder named `vivian-banshee` under your Codex pets directory. Custom pet packages currently work in the Codex desktop app; Codex mobile does not display custom pets, and cross-device pet syncing is not supported.

## Package contents

- `pet.json` — Codex v2 pet manifest.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation set

Rows 0–8 cover breathing and blinking, running right, running left, greeting, jumping, failure, waiting for input, active task work, and result review. Rows 9–10 add sixteen clockwise look directions from `000` up through `337.5` up-left.

## Character details

The pet keeps Vivian's long pale-lilac spiral hair, red eyes, pointed ears, black bow, white frilled blouse, structured black corset, layered black-and-deep-violet skirt, dark tights, violet heels, and ornate black-and-lilac bat-pattern parasol. Her silhouette stays compact while the parasol remains physically attached throughout every state.

## Quality record

- The atlas passes Codex v2 geometry, transparency, chroma, and unused-cell validation with no errors or warnings.
- All nine standard animation rows passed deterministic checks and independent normal-size playback review.
- The jump row uses stable-slot extraction to preserve one character scale and a genuine low-to-apex-to-low path.
- Three isolated blind reviewers confirmed both cardinal direction hard gates; ambiguous intermediate votes were reviewed against the labeled continuous loop.
- All sixteen labeled directions pass semantic review with no wrong quadrant, reversal, clipping, attachment break, or visible boundary pop.
- All nine published GIF previews were rendered from the cleaned and validated final v2 atlas.

## Scope

2D only. No 3D version was generated in this run.

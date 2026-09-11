# Kibutsuji Muzan — Codex Pet v2 (2D)

A finished Kibutsuji Muzan companion for the Codex desktop app, dressed in his white-fedora disguise with restrained, unsettling motion and a polished chibi silhouette.

## Install

Keep `pet.json` and `spritesheet.webp` together in a folder named `kibutsuji-muzan` under your Codex pets directory. Custom pet packages currently work in the Codex desktop app; Codex mobile does not display custom pets, and cross-device pet syncing is not supported.

## Package contents

- `pet.json` — Codex v2 pet manifest.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation set

Rows 0–8 cover breathing and blinking, running right, running left, greeting, jumping, failure, waiting for input, active task work, and result review. Rows 9–10 add sixteen clockwise look directions from `000` up through `337.5` up-left.

## Character details

The pet keeps Muzan's broad white fedora with its black band, pale face, narrow crimson eyes, short wavy black hair and cheek curls, fitted black jacket, crisp dark shirt, loose white trousers, and black dress shoes. The compact tailoring remains readable at native pet size without scenery, weapons, or detached effects.

## Quality record

- The atlas passes Codex v2 geometry, transparency, chroma, and unused-cell validation with no errors or warnings.
- All 57 standard-animation frames passed deterministic checks and independent normal-size playback review.
- The jump row preserves one character scale across a clear low-to-apex-to-low path.
- Three isolated blind reviewers unanimously confirmed all horizontal and vertical direction pairs.
- All sixteen labeled directions pass semantic review with no wrong quadrant, reversal, clipping, attachment break, or visible boundary pop.
- All nine published GIF previews were rendered from the cleaned and validated final v2 atlas.

## Scope

2D only. No 3D version was generated in this run.

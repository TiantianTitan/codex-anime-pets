# Silver Wolf — 2D edition

Silver-gray hair, violet goggles and a blue-tipped ponytail, with a quiet hacker's confidence.

This package contains a v2 atlas with nine animation states, a neutral pose and sixteen look directions. The artwork is transparent, lossless WebP; the package ID is `silver-wolf`.

## Install

Extract this ZIP into a single folder under `$CODEX_HOME/pets/` (normally `~/.codex/pets/`). Keep `pet.json` and `spritesheet.webp` together, then select Silver Wolf in the Codex desktop app's pet picker. Do not add an extra nested package folder.

Custom pet packages are for the Codex desktop app. Codex mobile does not display these pets; mobile installation and cross-device pet syncing are not supported.

## Animation compatibility

The atlas follows the v2 format. Which actions and look directions appear depends on the installed desktop version and its event triggers; including a pose does not make every client trigger it.

The repository's November 6, 2026 local inspection of Desktop `26.1007.21434` recorded idle holds of 1680 / 660 / 660 / 840 / 840 / 1920 ms and three action cycles before an idle return. Preview checks use that historical timing profile. Silver Wolf was validated using a temporary isolated pet directory, not installed or exercised in the user's live app.

## Contents

- `pet.json` — package identity and v2 sprite declaration
- `spritesheet.webp` — 1536 × 2288 atlas, 192 × 208 cells
- `README.md` — this guide

Unofficial fan-made companion. Silver Wolf and the original character design belong to their respective rights holders.

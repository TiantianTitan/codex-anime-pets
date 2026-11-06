# Kallen — Codex Pet v2 (2D)

Silver-white hair, blue eyes, a long braid, and Kallen's white dress with a black-and-red jacket. This edition uses crisp 2D chibi artwork, with her cross-shaped accessories and thigh holster kept on their original sides.

## Installation

Extract this package into a folder named `kallen-kaslana` inside your Codex pets directory. `pet.json` must sit directly inside that folder, beside `spritesheet.webp`.

- Linux and macOS: `~/.codex/pets/kallen-kaslana/`
- Windows: `%USERPROFILE%\.codex\pets\kallen-kaslana\`
- Custom configuration: `CODEX_HOME/pets/kallen-kaslana/`

In the tested Codex Desktop 26.1007.21434 client, open Settings → Pets, refresh the list, select Kallen, then use `/pet` to display her. Menu names may differ in other versions.

Custom packages are for the Codex desktop app. Codex mobile cannot display these pets; mobile installation and cross-device pet syncing are not supported.

## Animation set

Nine states cover quiet breathing, movement to the right and left, a greeting, jumping, disappointment, waiting for input, active task work, and reviewing a result. A separate neutral frame and sixteen clockwise look directions complete the v2 atlas.

The two movement rows were drawn separately to preserve Kallen's asymmetric braid, clips, earring and holster. The jump retains its crouch, ascent, apex, descent and landing at one camera scale. Hands stay free throughout; no weapon effects or extra props appear.

Idle keeps her eyes comfortably open with small breathing and clothing changes. Its compatibility preview uses the measured 6.6-second schedule of Desktop 26.1007.21434. Other client versions may use different timing. State triggers, repeat limits and pointer-driven look behavior are controlled by the client; looping preview files do not change those controls.

## Package

- `pet.json` — v2 manifest, stable ID `kallen-kaslana`.
- `spritesheet.webp` — lossless transparent RGBA atlas, 1536×2288 pixels; 8×11 cells of 192×208 pixels.
- `README.md` — this guide.

The archive contains these files at its root. Source references, production intermediates and QA material are kept outside the product folder.

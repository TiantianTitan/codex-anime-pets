# Ruan Mei · 阮·梅 — Codex Pet v2

A polished 2D chibi Codex companion inspired by Ruan Mei's serene presence, teal-and-white formal dress, floral ornament, and musical identity.

## Package contents

- `pet.json` — Codex pet metadata
- `spritesheet.webp` — transparent Codex v2 animation atlas

## Animation layout

The spritesheet is `1536×2288`, arranged as eight columns by eleven rows of `192×208` cells.

Rows 0–8 contain the standard Codex states:

1. Idle
2. Running right
3. Running left
4. Waving
5. Jumping
6. Failed
7. Waiting for input
8. Active task work
9. Reviewing

Rows 9–10 contain sixteen clockwise look directions from `000` through `337.5` degrees.

## Install

Copy `pet.json` and `spritesheet.webp` together into:

```text
~/.codex/pets/ruan-mei/
```

This is a 2D-only release. No 3D edition was generated in this run.

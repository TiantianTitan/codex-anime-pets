# Asaba Harumasa · 2D

A clean 2D anime chibi companion with navy hair, golden eyes, a yellow headband and an asymmetrical tactical outfit. Pet ID: `asaba-harumasa`.

This package contains a transparent Codex v2 spritesheet: **1536 × 2288**, eight columns and eleven rows, with **192 × 208** cells. It includes nine animation states, sixteen clockwise look directions and a separate neutral pose. The leftward jog uses a steady bent-arm pose with cycling legs; gloves and sleeves keep their anatomical sides.

## Install

Extract the ZIP directly into the pet's folder so the files are laid out as follows:

```text
~/.codex/pets/asaba-harumasa/
├── pet.json
├── spritesheet.webp
└── README.md
```

On Windows, use `%USERPROFILE%\.codex\pets\asaba-harumasa\`. If you set `CODEX_HOME`, use `<CODEX_HOME>/pets/asaba-harumasa/`. Avoid an extra wrapping directory between the pet folder and `pet.json`.

In the tested Codex Desktop **26.1007.21434** client, open **Settings → Pets → Refresh**, select the companion, then use `/pet` to display it. Other client versions may expose different controls. Custom pet packages require the desktop app; the Codex mobile app cannot display these pets.

## Playback

The desktop client chooses which states and directions to display. The package does not add new triggers or guarantee continuous work-state playback. QA previews use the version-qualified local idle schedule of 6.6 seconds and source holds for other states. They are inspection loops, not a live installation test of this pet.

The ZIP places its files at the archive root. Source references and quality-review material are kept outside the product folder.

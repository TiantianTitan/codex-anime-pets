# Rita Rossweisse · 2D

A short-haired maid in black and white, with a rose-trimmed headband and a quiet smile.

This Codex Desktop v2 package contains nine animation states, sixteen look directions and a neutral frame. The transparent lossless WebP atlas is 1536×2288, with 192×208 cells.

## Install

Create a `rita-rossweisse` folder in your pets directory and extract the ZIP directly into it. There must not be another wrapping folder between this directory and `pet.json`.

- Linux / macOS: `~/.codex/pets/rita-rossweisse/`
- Windows: `%USERPROFILE%\.codex\pets\rita-rossweisse\`
- Custom configuration: `<CODEX_HOME>/pets/rita-rossweisse/`

The folder should contain `pet.json`, `spritesheet.webp` and this README.

On the repository's tested Codex Desktop 26.1007.21434, open Settings → Pets, click Refresh, select Rita Rossweisse and enter `/pet` to show her. Other versions may arrange these controls differently.

Custom pets are for the desktop app. The Codex mobile app cannot display pets; mobile installation and cross-device pet syncing are not supported.

## Playback notes

The package supplies the v2 sprite states; the desktop client decides which state or look direction to display. An animation preview does not prove that every app action will trigger every sprite row or that a work state will loop continuously.

QA previews use the 2026-11-06 measured idle holds for Desktop 26.1007.21434. Other state previews use source-table timing. No live installation was changed or tested during packaging.

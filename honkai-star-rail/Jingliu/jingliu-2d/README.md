# Jingliu

A 2D chibi edition of Jingliu, with silver-white hair, scarlet eyes and her ice-blue sword.

## Install

Extract this ZIP directly into a folder named `jingliu` under your Codex pets directory:

- Linux / macOS: `~/.codex/pets/jingliu/`
- Windows: `%USERPROFILE%\.codex\pets\jingliu\`
- Custom configuration: `<CODEX_HOME>/pets/jingliu/`

`pet.json` and `spritesheet.webp` should sit directly inside that folder, without another wrapping directory.

Compatibility notes are based on the inspected desktop version **26.1007.21434**. In that version, open Settings → Pets, refresh the list and select Jingliu. Use `/pet` to show the pet. Menus and state behavior may differ in other versions.

## Package

Codex v2 atlas: **1536 × 2288**, with **192 × 208** transparent cells, nine standard animation states, a neutral pose and sixteen look directions. This is the 2D edition only.

The desktop client decides which animations and look directions to invoke. Having all states in the package does not mean every state will appear in ordinary chat. Timing and repeat behavior are client-controlled; this package adds no custom playback settings.

Custom pet packages target the Codex desktop app. Codex mobile does not display these custom pets; mobile installation and cross-device pet syncing are not supported by this package.

The package was validated through a temporary install-layout check, without launching or installing it in a live client. Source references and QA files are not included.

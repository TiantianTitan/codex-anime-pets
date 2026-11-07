# Albedo · 2D

A quiet alchemist in his white-and-navy coat, with turquoise eyes and tousled pale-gold hair.

## Install

Extract this archive directly into the pet directory below. `pet.json` and `spritesheet.webp` must be inside `albedo`, not inside another nested folder.

- Linux / macOS: `~/.codex/pets/albedo/`
- Windows: `%USERPROFILE%\.codex\pets\albedo\`
- Custom configuration: `<CODEX_HOME>/pets/albedo/`

In Codex Desktop 26.1007.21434, open **Settings → Pets → Refresh**, select **Albedo**, then use `/pet`. Menus and available triggers may differ in other versions.

Custom pets are for the Codex desktop app. Codex mobile does not display these pets; mobile installation and cross-device pet syncing are not supported by this package.

## Contents

- `pet.json` — Desktop v2 manifest; ID `albedo`.
- `spritesheet.webp` — transparent lossless 1536 × 2288 atlas, 8 × 11 cells, each 192 × 208.
- Nine states: idle, right movement, left movement, greeting, jump, failure, waiting for input, working, and review.
- Sixteen clockwise look directions plus a separate neutral pose.

The atlas contains the poses; the desktop client controls when they play. It does not add new cursor tracking or state triggers to the app. Version-specific timing checks use Desktop 26.1007.21434 evidence, not a guarantee for all future clients.

This archive does not install or activate itself. Source references, generation files and QA evidence are kept outside the product package.

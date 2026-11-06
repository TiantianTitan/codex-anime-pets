# Aventurine — Codex Pet v2

A polished 2D chibi Aventurine companion for Codex, built from the supplied character references.

## Included

- `pet.json` — Codex pet metadata with `spriteVersionNumber: 2`
- `spritesheet.webp` — transparent 8×11 atlas (`1536×2288`)
- 9 standard animation states
- 16 pointer look directions

## Install

Copy this folder to:

```text
~/.codex/pets/aventurine
```

The pet is already installed at that location on the machine where it was produced.

## Visual design

The sprite preserves Aventurine's sandy-blond layered hair, magenta-to-cyan eyes, teal earring, white fur collar, black/teal/gold outfit, white trousers, gloves, bracelet, waist ornaments, and attached tassels in a compact smooth 2D chibi style.

No 3D edition is included in this package.

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/aventurine/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\aventurine\`；自定义 `CODEX_HOME` 时使用其 `pets/aventurine/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/aventurine/`
(default `~/.codex/pets/aventurine/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。其余动作、neutral 和 16 个观察方向保持原版；ID 和 v2 格式不变。
The idle frames account for the desktop client's slow idle playback. Other states,
the neutral frame, all 16 look directions, the ID, and the v2 contract are preserved.

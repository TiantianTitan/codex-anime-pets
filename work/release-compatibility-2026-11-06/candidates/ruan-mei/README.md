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

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/ruan-mei/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\ruan-mei\`；自定义 `CODEX_HOME` 时使用其 `pets/ruan-mei/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/ruan-mei/`
(default `~/.codex/pets/ruan-mei/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。其余动作、neutral 和 16 个观察方向保持原版；ID 和 v2 格式不变。
The idle frames account for the desktop client's slow idle playback. Other states,
the neutral frame, all 16 look directions, the ID, and the v2 contract are preserved.

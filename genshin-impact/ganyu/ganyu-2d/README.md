# Ganyu · 甘雨 — Codex Pet v2

A polished 2D chibi Codex companion inspired by Ganyu's gentle presence, pale-blue hair, black-red qilin horns, and elegant Liyue attire.

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
~/.codex/pets/ganyu/
```

This is a 2D-only release. No 3D edition was generated in this run.

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/ganyu/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\ganyu\`；自定义 `CODEX_HOME` 时使用其 `pets/ganyu/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/ganyu/`
(default `~/.codex/pets/ganyu/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。该段记录此前的待机修复；后续动作调整见下节。
The idle frames account for the desktop client's slow idle playback. The later motion changes are recorded below.


<!-- MOTION-REFINEMENT-2026-11-06 -->
## 动作优化 / Motion refinement · 2026-11-06

调整动作：失败反馈。保持原帧数与客户端时序，改善配准、动作衔接或原图中的明显断裂。
本次未修改待机、neutral、16 个观察方向与宠物 ID。

Updated states: failed. Frame counts and client timing are unchanged.
Idle, the neutral cell, all 16 look directions, and the pet ID are unchanged in this update.

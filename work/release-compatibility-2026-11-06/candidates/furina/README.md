# Furina 芙宁娜 — Codex Pet v2 (2D)

This package contains the completed 2D animated Codex pet inspired by Furina. It uses her short-haired dark-navy Fontaine outfit and was built from the supplied references, then validated against the complete Codex v2 pet contract.

## Contents

- `pet.json` — pet manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation layout

- Rows 0–8: idle, running-right, independently drawn running-left, waving, jumping, failed, waiting, active task processing, and review.
- Rows 9–10: sixteen clockwise look directions from `000` up through `337.5` up-left.

## Visual identity

The atlas preserves Furina's white-and-pale-cyan bob, curled forelock, blue water-drop eyes, navy crown-like top hat with gold prongs, dark Fontaine tailcoat, white ruffles, blue gemstone bows, black shorts, gloves, and poised theatrical personality. The alternate long-haired white outfit, cane, scroll, Hydro summons, bubbles, and detached effects were intentionally excluded.

## Quality gates

- Exact v2 geometry, transparent-cell validation, and one final edge-cleanup pass succeeded.
- All nine standard animation rows passed deterministic extraction checks and independent visual QA.
- The jumping row uses stable-slot extraction so its anticipation, airborne apex, descent, and landing remain visible without scale popping.
- Four cardinal directions passed three isolated blind reviews; the complete 16-direction loop passed labeled semantic and continuity review.
- Rejected rows were regenerated as complete coherent strips rather than patched cell by cell.

## Scope

2D only. No 3D version was generated in this run.

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/furina/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\furina\`；自定义 `CODEX_HOME` 时使用其 `pets/furina/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/furina/`
(default `~/.codex/pets/furina/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。其余动作、neutral 和 16 个观察方向保持原版；ID 和 v2 格式不变。
The idle frames account for the desktop client's slow idle playback. Other states,
the neutral frame, all 16 look directions, the ID, and the v2 contract are preserved.

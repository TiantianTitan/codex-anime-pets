# Firefly 流萤 — Codex Pet v2 (2D)

This package contains the completed 2D animated Codex pet inspired by Firefly. It was built from the supplied full-body art, dynamic reference, chibi expressions, and close-up portrait, then validated against the complete Codex v2 pet contract.

## Contents

- `pet.json` — pet manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation layout

- Rows 0–8: idle, running-right, independently drawn running-left, waving, jumping, failed, waiting, active task processing, and review.
- Rows 9–10: sixteen clockwise look directions from `000` up through `337.5` up-left.

## Visual identity

The atlas preserves Firefly's long pearly-silver hair with cool gray ends, pink-to-aqua eyes, black headband, pale mint leaf ornament and navy bow, charcoal-and-gold cropped cape, orange-gold chest bow, mint layered dress, dark stockings, and white boots with teal accents. Her gentle, hopeful expression and quietly brave presence remain recognizable throughout the animation set.

## Quality gates

- Exact v2 geometry, transparent-cell validation, and the final chroma-edge cleanup pass succeeded.
- All nine standard animation rows passed deterministic frame checks and independent visual QA.
- The jumping row was rebuilt and extracted with stable slots to remove an alternating scale pulse while preserving natural vertical travel.
- All four cardinal directions passed hard semantic gates in three isolated blind reviews.
- The complete 16-direction loop passed labeled review; the front-biased `337.5` horizontal cue remains a documented non-blocking warning, with no wrong cardinal or visible reversal.
- Continuity metric outliers were reviewed at normal pet size and show no conspicuous snap, scale pop, identity change, clipping, or transparent hole.

## Scope

2D only. No 3D version was generated in this run.

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/firefly/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\firefly\`；自定义 `CODEX_HOME` 时使用其 `pets/firefly/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/firefly/`
(default `~/.codex/pets/firefly/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。其余动作、neutral 和 16 个观察方向保持原版；ID 和 v2 格式不变。
The idle frames account for the desktop client's slow idle playback. Other states,
the neutral frame, all 16 look directions, the ID, and the v2 contract are preserved.

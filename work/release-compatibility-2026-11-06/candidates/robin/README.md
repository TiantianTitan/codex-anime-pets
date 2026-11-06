# Robin 知更鸟 — Codex Pet v2 (2D)

This package contains the completed 2D animated Codex pet inspired by Robin. It was built from the supplied character art, expression references, and full turnaround, then validated against the complete Codex v2 pet contract.

## Contents

- `pet.json` — pet manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation layout

- Rows 0–8: idle, running-right, independently drawn running-left, waving, jumping, failed, waiting, active task processing, and review.
- Rows 9–10: sixteen clockwise look directions from `000` up through `337.5` up-left.

## Visual identity

The atlas preserves Robin's silver-blue hair and rear rosette bun, turquoise-to-violet eyes, gold flower-tip halo, white feathered ear-wings, and layered white, deep-indigo, lilac, and gold stage dress. Her asymmetric dress panel, halo construction, long hair, and calm singer-like expression language remain consistent in every animation.

## Quality gates

- Exact v2 geometry, transparent-cell validation, and one final chroma-edge cleanup pass succeeded.
- All nine standard animation rows passed deterministic frame checks and independent visual QA.
- Four cardinal directions passed hard semantic gates; the complete 16-direction loop passed labeled review and three isolated blind reviews.
- The near-up-left intermediate directions retain subtler horizontal cues and are recorded as reviewed warnings, while all four cardinals remain unmistakable.
- The full loop's `337.5 → 000` metric warning was visually reviewed at normal size and has no visible snap, scale pop, identity change, or direction reversal.

## Scope

2D only. No 3D version was generated in this run.

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/robin/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\robin\`；自定义 `CODEX_HOME` 时使用其 `pets/robin/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/robin/`
(default `~/.codex/pets/robin/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。其余动作、neutral 和 16 个观察方向保持原版；ID 和 v2 格式不变。
The idle frames account for the desktop client's slow idle playback. Other states,
the neutral frame, all 16 look directions, the ID, and the v2 contract are preserved.

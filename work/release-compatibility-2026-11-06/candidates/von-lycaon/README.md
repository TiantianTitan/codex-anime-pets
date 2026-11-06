# Von Lycaon · 冯·莱卡恩 — Codex Pet v2 (2D)

This package contains a complete 2D animated Codex companion inspired by Von Lycaon, prepared for the Codex v2 pet format.

## Contents

- `pet.json` — pet manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation layout

- Rows 0–8: idle, running-right, independently drawn running-left, waving, jumping, failed, waiting, active task processing, and review.
- Rows 9–10: sixteen clockwise look directions from `000` up through `337.5` up-left.

## Visual identity

The atlas keeps Lycaon's ivory wolf ears and swept hair, red eyes, black muzzle markings, red cravat, tailored black-and-white uniform, gold chain, mechanical legs, and large attached white tail consistent across every motion and gaze direction.

## Quality gates

- Exact v2 geometry, RGBA transparency, unused-cell transparency, and one-pass chroma-edge cleanup passed.
- All nine standard animation rows passed deterministic inspection and independent frame-by-frame visual QA.
- Running-left was drawn independently so the character's facial, uniform, chain, and tail details remain coherent.
- All four cardinal directions passed a fresh three-reviewer blind majority; all sixteen directions passed labeled semantic and continuity review.
- The profile-to-three-quarter silhouette change at `270→292.5` was reviewed at normal pet size and accepted without a visible scale or baseline pop.
- The packaged atlas validates as 1536×2288 with no structural errors or warnings.

## Compatibility

Custom pet packages currently support the Codex desktop app. Mobile installation, mobile pet display, and cross-device pet syncing are not supported.

## Scope

2D only. No 3D edition is included.

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/von-lycaon/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\von-lycaon\`；自定义 `CODEX_HOME` 时使用其 `pets/von-lycaon/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/von-lycaon/`
(default `~/.codex/pets/von-lycaon/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。其余动作、neutral 和 16 个观察方向保持原版；ID 和 v2 格式不变。
The idle frames account for the desktop client's slow idle playback. Other states,
the neutral frame, all 16 look directions, the ID, and the v2 contract are preserved.

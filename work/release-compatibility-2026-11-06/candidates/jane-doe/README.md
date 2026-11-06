# Jane Doe · 简·杜 — Codex Pet v2 (2D)

This package contains a complete 2D animated Codex pet inspired by Jane Doe. It was created from the supplied character references and validated against the full Codex v2 pet contract.

## Contents

- `pet.json` — pet manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation layout

- Rows 0–8: idle, running-right, independently drawn running-left, waving, jumping, failed, waiting, active task processing, and review.
- Rows 9–10: sixteen clockwise look directions from `000` up through `337.5` up-left.

## Visual identity

The atlas preserves Jane's short black bob, wine-red rear hair, pink rat ears, narrow green eyes, cream fur collar, blue-gray cropped jacket, tactical shorts, asymmetrical stockings and boots, red accents, and one long attached charcoal tail. Her outfit asymmetry and flexible tail remain physically coherent across movement and gaze changes.

## Quality gates

- Exact v2 geometry, RGBA transparency, unused-cell transparency, and the single final chroma-edge cleanup passed.
- All nine standard animation rows passed deterministic inspection and independent visual QA.
- Leftward and rightward running were drawn independently so the asymmetric outfit and tail construction remain consistent.
- All four cardinal directions passed a fresh three-reviewer blind majority; all sixteen directions passed labeled semantic and continuity review.
- Subtle intermediate-axis cues at `022.5`, `157.5`, `292.5`, `315`, and `337.5` remain recorded as reviewed warnings because the labeled clockwise loop preserves the intended quadrants without reversal.
- The packaged atlas validates as 1536×2288 with no structural errors or warnings.

## Scope

2D only. No 3D version was generated in this run.

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/jane-doe/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\jane-doe\`；自定义 `CODEX_HOME` 时使用其 `pets/jane-doe/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/jane-doe/`
(default `~/.codex/pets/jane-doe/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。其余动作、neutral 和 16 个观察方向保持原版；ID 和 v2 格式不变。
The idle frames account for the desktop client's slow idle playback. Other states,
the neutral frame, all 16 look directions, the ID, and the v2 contract are preserved.

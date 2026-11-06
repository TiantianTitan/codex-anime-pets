# Hoshimi Miyabi · 星见雅 — Codex Pet v2 (2D)

This package contains the completed 2D animated Codex pet inspired by Hoshimi Miyabi. It was built from the supplied character references and validated against the full Codex v2 pet contract.

## Contents

- `pet.json` — pet manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation layout

- Rows 0–8: idle, running-right, independently drawn running-left, waving, jumping, failed, waiting, active task processing, and review.
- Rows 9–10: sixteen clockwise look directions from `000` up through `337.5` up-left.

## Visual identity

The atlas preserves Miyabi's navy-black hair, tall fox ears, red eyes, teal-white-black uniform, asymmetric mechanical arm with red braided cord, teal sleeve, and attached sheathed katana. Costume sides and sword anchoring remain coherent through motion and gaze changes.

## Quality gates

- Exact v2 geometry, RGBA transparency, unused-cell transparency, and a single final chroma-edge cleanup passed.
- All nine standard animation rows passed deterministic inspection and independent visual QA.
- Rightward and leftward running were drawn independently so the asymmetric costume remains physically consistent.
- All sixteen look directions passed labeled semantic review and three-reviewer blind majority validation with no errors, warnings, ambiguous cells, or unconfirmed pairs.
- Metric continuity warnings at the pure-profile transitions and the `157.5→180` row boundary were visually reviewed and resolved as normal perspective changes, with no direction reversal, ground shift, broken attachment, or identity jump. The rebuilt `337.5→000` loop boundary now closes without a continuity warning.
- The packaged atlas validates as 1536×2288 with no structural errors or warnings.

## Scope

2D only. No 3D version was generated in this run.

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/miyabi/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\miyabi\`；自定义 `CODEX_HOME` 时使用其 `pets/miyabi/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/miyabi/`
(default `~/.codex/pets/miyabi/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。其余动作、neutral 和 16 个观察方向保持原版；ID 和 v2 格式不变。
The idle frames account for the desktop client's slow idle playback. Other states,
the neutral frame, all 16 look directions, the ID, and the v2 contract are preserved.

# Kaedehara Kazuha · 枫原万叶 — Codex Pet v2 (2D)

This package contains the completed 2D animated Codex pet inspired by Kaedehara Kazuha. It was built from the supplied chibi references and validated against the full Codex v2 pet contract.

## Contents

- `pet.json` — pet manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation layout

- Rows 0–8: idle, running-right, independently drawn running-left, waving, jumping, failed, waiting, active task processing, and review.
- Rows 9–10: sixteen clockwise look directions from `000` up through `337.5` up-left.

## Visual identity

The atlas preserves Kazuha's ivory-white hair, red streak, red-orange eyes, compact scarf, asymmetric black-red-cream samurai outfit, dark red hakama shorts, sandals, and attached sheathed sword. Costume sides, sword anchoring, and the connected scarf remain coherent through motion and gaze changes.

## Quality gates

- Exact v2 geometry, RGBA transparency, unused-cell transparency, and final chroma-edge cleanup passed.
- All nine standard animation rows passed deterministic inspection and independent visual QA.
- Rightward and leftward running were drawn independently so the asymmetric costume remains physically consistent.
- The four cardinal gaze directions passed all hard semantic gates in three isolated blind reviews.
- The combined blind validation has `ok: true`; only `202.5` and `225` retain documented minor horizontal-axis ambiguity at normal size, while labeled review confirms the intended down-left quadrant and a continuous approach to `270` left.
- `157.5→180` and `337.5→000` retain metric-only continuity warnings caused by the expected change between narrow three-quarter and broader centered silhouettes; normal-size review found no visible snap, broken attachment, or identity shift.
- The packaged atlas validates as 1536×2288 with no structural errors or warnings.

## Scope

2D only. No 3D version was generated in this run.

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/kazuha-chibi/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\kazuha-chibi\`；自定义 `CODEX_HOME` 时使用其 `pets/kazuha-chibi/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/kazuha-chibi/`
(default `~/.codex/pets/kazuha-chibi/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。其余动作、neutral 和 16 个观察方向保持原版；ID 和 v2 格式不变。
The idle frames account for the desktop client's slow idle playback. Other states,
the neutral frame, all 16 look directions, the ID, and the v2 contract are preserved.

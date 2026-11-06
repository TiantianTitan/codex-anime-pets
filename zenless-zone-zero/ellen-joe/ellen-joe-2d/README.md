# Ellen Joe 艾莲·乔 — Codex Pet v2 (2D)

This package contains a completed 2D animated Codex pet inspired by Ellen Joe. It was built from the supplied character references and validated against the full Codex v2 pet contract.

## Contents

- `pet.json` — pet manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation layout

- Rows 0–8: idle, running-right, independently drawn running-left, waving, jumping, failed, waiting, active task processing, and review.
- Rows 9–10: sixteen clockwise look directions from `000` up through `337.5` up-left.

## Visual identity

The atlas preserves Ellen Joe's charcoal-black bob with red inner layers, warm red eyes, maid headdress with metallic spikes, black-and-white industrial maid outfit, belts, cuffs, stockings, platform shoes, and physically attached shark tail. Her oversized scissors and detached effects were omitted to keep every 192×208 animation cell clear and readable.

## Quality gates

- Exact v2 geometry, transparency, chroma-spill cleanup, and package validation passed.
- All nine standard animation rows passed deterministic extraction and independent visual review.
- Four cardinal directions passed isolated blind review; all sixteen directions passed labeled semantic and continuity review.
- Rejected animation attempts were regenerated as complete coherent rows rather than patched cell by cell.

## Scope

2D only. No 3D version was generated in this run.

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/ellen-joe/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\ellen-joe\`；自定义 `CODEX_HOME` 时使用其 `pets/ellen-joe/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/ellen-joe/`
(default `~/.codex/pets/ellen-joe/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机未发现长时间闭眼问题，保留原图。其余动作、neutral 和 16 个观察方向保持原版；ID 和 v2 格式不变。
The idle frames account for the desktop client's slow idle playback. Other states,
the neutral frame, all 16 look directions, the ID, and the v2 contract are preserved.

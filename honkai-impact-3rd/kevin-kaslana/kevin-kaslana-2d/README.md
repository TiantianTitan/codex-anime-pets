# Kevin Kaslana 凯文·卡斯兰娜 — Codex Pet v2 (2D)

This package contains the completed 2D animated Codex pet inspired by Kevin Kaslana. It was built from the supplied character references and validated against the complete Codex v2 pet contract.

## Contents

- `pet.json` — pet manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation layout

- Rows 0–8: idle, running-right, independently drawn running-left, waving, jumping, failed, waiting, active task processing, and review.
- Rows 9–10: sixteen clockwise look directions from `000` up through `337.5` up-left.

## Visual identity

The atlas preserves Kevin's tousled white hair, icy-blue eyes, calm expression, black-and-white long combat coat, gold trim and buckles, cyan chest and belt accents, and asymmetric armored sleeve. His reserved, formidable presence remains recognizable throughout every action and viewing direction.

## Quality gates

- Exact v2 geometry, transparent-cell validation, and the single final chroma-edge cleanup pass succeeded.
- All nine standard animation rows passed deterministic frame checks and independent visual QA.
- Leftward and rightward running were drawn independently so Kevin's asymmetric costume remains physically consistent.
- All four cardinal directions passed the hard semantic gates in three fresh isolated blind reviews; the final blind validation has `ok: true` with no hard-gate errors.
- All seven vertical blind pairs passed. Intermediate horizontal blind warnings were resolved against the labeled full loop: 12 directions passed directly, while `022.5`, `157.5`, `202.5`, and `337.5` retain documented warnings only because their near-vertical horizontal component is intentionally subtle. No direction failed or crossed into a wrong quadrant.
- Both row boundaries were reviewed at normal pet size. `157.5→180` and `337.5→000` show no visible seam, snap, center jump, or scale pop.
- Reported alpha gaps are the intended spaces between the legs and long coat openings, not holes through the character.

## Scope

2D only. No 3D version was generated in this run.

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/kevin-kaslana/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\kevin-kaslana\`；自定义 `CODEX_HOME` 时使用其 `pets/kevin-kaslana/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/kevin-kaslana/`
(default `~/.codex/pets/kevin-kaslana/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。该段记录此前的待机修复；后续动作调整见下节。
The idle frames account for the desktop client's slow idle playback. The later motion changes are recorded below.


<!-- MOTION-REFINEMENT-2026-11-06 -->
## 动作优化 / Motion refinement · 2026-11-06

调整动作：失败反馈。保持原帧数与客户端时序，改善配准、动作衔接或原图中的明显断裂。
本次未修改待机、neutral、16 个观察方向与宠物 ID。

Updated states: failed. Frame counts and client timing are unchanged.
Idle, the neutral cell, all 16 look directions, and the pet ID are unchanged in this update.

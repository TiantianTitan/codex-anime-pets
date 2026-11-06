# Kamisato Ayaka · 神里绫华 — Codex Pet v2 (2D)

This package contains the completed 2D animated Codex pet inspired by Kamisato Ayaka. It was built from the supplied character references and validated against the full Codex v2 pet contract.

## Contents

- `pet.json` — pet manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation layout

- Rows 0–8: idle, running-right, independently drawn running-left, waving, jumping, failed, waiting, active task processing, and review.
- Rows 9–10: sixteen clockwise look directions from `000` up through `337.5` up-left.

## Visual identity

The atlas preserves Ayaka's pale icy-blue high ponytail, straight bangs, black-and-gold crown ornament, pink side ribbons, blue eyes, navy kimono dress, gold trim, sakura details, magenta waist cord, armored skirt panels, white tabi socks, and floral sandals. The folding fan appears where it suits the gesture while the character's silhouette and costume remain recognizable in every state.

## Quality gates

- Exact v2 geometry, RGBA transparency, unused-cell transparency, and the single final chroma-edge cleanup pass succeeded.
- All nine standard animation rows passed deterministic frame inspection with no errors or warnings.
- Leftward and rightward running were drawn independently so Ayaka's asymmetric ornaments and skirt armor remain physically consistent.
- All four cardinal directions passed the hard semantic gates in three isolated blind reviews; the combined blind validation has `ok: true`.
- Every horizontal direction pair passed. The two intermediate poses `202.5` and `337.5` retain documented vertical-axis warnings because their pitch is subtle at normal size; labeled loop review confirmed the intended quadrants with no reversal.
- Both row boundaries were reviewed at normal pet size. `157.5→180` and `337.5→000` close without a visible seam, scale pop, or identity shift.
- Continuity alpha-gap warnings correspond to intended open spaces between legs, skirt panels, hair, arms, and fan—not holes through the character.
- The completed package was validated as a 1536×2288 Codex v2 atlas with no structural errors or warnings.

## Scope

2D only. No 3D version was generated in this run.

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/kamisato-ayaka/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\kamisato-ayaka\`；自定义 `CODEX_HOME` 时使用其 `pets/kamisato-ayaka/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/kamisato-ayaka/`
(default `~/.codex/pets/kamisato-ayaka/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。其余动作、neutral 和 16 个观察方向保持原版；ID 和 v2 格式不变。
The idle frames account for the desktop client's slow idle playback. Other states,
the neutral frame, all 16 look directions, the ID, and the v2 contract are preserved.

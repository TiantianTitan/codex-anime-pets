# Dan Heng · Imbibitor Lunae 丹恒·饮月 — Codex Pet v2 (2D)

This local package contains the completed 2D animated desktop pet inspired by Dan Heng in his Imbibitor Lunae form. It was built from the supplied character references and validated against the Codex v2 pet contract.

## Contents

- `pet.json` — pet manifest with `spriteVersionNumber: 2`.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation layout

- Rows 0–8: idle, running-right, running-left, waving, jumping, failed, waiting, active task processing, and review.
- Rows 9–10: sixteen clockwise look directions from `000` up through `337.5` up-left.

## Visual identity

The atlas preserves the paired cyan-teal dragon antlers, pointed ears, long dark hair, luminous teal eyes, white draped sleeves, short dark outfit, jade-gold waist ornament, ankle boots, and attached aqua tail accent across all states.

## Scope

2D only. This package has not been installed into Codex, uploaded, or published, and no 3D version was generated.

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/dan-heng-imbibitor-lunae/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\dan-heng-imbibitor-lunae\`；自定义 `CODEX_HOME` 时使用其 `pets/dan-heng-imbibitor-lunae/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/dan-heng-imbibitor-lunae/`
(default `~/.codex/pets/dan-heng-imbibitor-lunae/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。其余动作、neutral 和 16 个观察方向保持原版；ID 和 v2 格式不变。
The idle frames account for the desktop client's slow idle playback. Other states,
the neutral frame, all 16 look directions, the ID, and the v2 contract are preserved.

# Kibutsuji Muzan — Codex Pet v2 (2D)

A finished Kibutsuji Muzan companion for the Codex desktop app, dressed in his white-fedora disguise with restrained, unsettling motion and a polished chibi silhouette.

## Install

Keep `pet.json` and `spritesheet.webp` together in a folder named `kibutsuji-muzan` under your Codex pets directory. Custom pet packages currently work in the Codex desktop app; Codex mobile does not display custom pets, and cross-device pet syncing is not supported.

## Package contents

- `pet.json` — Codex v2 pet manifest.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation set

Rows 0–8 cover breathing and blinking, running right, running left, greeting, jumping, failure, waiting for input, active task work, and result review. Rows 9–10 add sixteen clockwise look directions from `000` up through `337.5` up-left.

## Character details

The pet keeps Muzan's broad white fedora with its black band, pale face, narrow crimson eyes, short wavy black hair and cheek curls, fitted black jacket, crisp dark shirt, loose white trousers, and black dress shoes. The compact tailoring remains readable at native pet size without scenery, weapons, or detached effects.

## Quality record

- The atlas passes Codex v2 geometry, transparency, chroma, and unused-cell validation with no errors or warnings.
- All 57 standard-animation frames passed deterministic checks and independent normal-size playback review.
- The jump row preserves one character scale across a clear low-to-apex-to-low path.
- Three isolated blind reviewers unanimously confirmed all horizontal and vertical direction pairs.
- All sixteen labeled directions pass semantic review with no wrong quadrant, reversal, clipping, attachment break, or visible boundary pop.
- All nine published GIF previews were rendered from the cleaned and validated final v2 atlas.

## Scope

2D only. No 3D version was generated in this run.

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/kibutsuji-muzan/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\kibutsuji-muzan\`；自定义 `CODEX_HOME` 时使用其 `pets/kibutsuji-muzan/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/kibutsuji-muzan/`
(default `~/.codex/pets/kibutsuji-muzan/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。其余动作、neutral 和 16 个观察方向保持原版；ID 和 v2 格式不变。
The idle frames account for the desktop client's slow idle playback. Other states,
the neutral frame, all 16 look directions, the ID, and the v2 contract are preserved.

# Vivian Banshee — Codex Pet v2 (2D)

A finished Vivian Banshee companion for the Codex desktop app, pairing gothic elegance with restrained, expressive motion beneath her signature lilac parasol.

## Install

Keep `pet.json` and `spritesheet.webp` together in a folder named `vivian-banshee` under your Codex pets directory. Custom pet packages currently work in the Codex desktop app; Codex mobile does not display custom pets, and cross-device pet syncing is not supported.

## Package contents

- `pet.json` — Codex v2 pet manifest.
- `spritesheet.webp` — transparent 8×11 atlas, 1536×2288 pixels, with 192×208 cells.

## Animation set

Rows 0–8 cover breathing and blinking, running right, running left, greeting, jumping, failure, waiting for input, active task work, and result review. Rows 9–10 add sixteen clockwise look directions from `000` up through `337.5` up-left.

## Character details

The pet keeps Vivian's long pale-lilac spiral hair, red eyes, pointed ears, black bow, white frilled blouse, structured black corset, layered black-and-deep-violet skirt, dark tights, violet heels, and ornate black-and-lilac bat-pattern parasol. Her silhouette stays compact while the parasol remains physically attached throughout every state.

## Quality record

- The atlas passes Codex v2 geometry, transparency, chroma, and unused-cell validation with no errors or warnings.
- All nine standard animation rows passed deterministic checks and independent normal-size playback review.
- The jump row uses stable-slot extraction to preserve one character scale and a genuine low-to-apex-to-low path.
- Three isolated blind reviewers confirmed both cardinal direction hard gates; ambiguous intermediate votes were reviewed against the labeled continuous loop.
- All sixteen labeled directions pass semantic review with no wrong quadrant, reversal, clipping, attachment break, or visible boundary pop.
- All nine published GIF previews were rendered from the cleaned and validated final v2 atlas.

## Scope

2D only. No 3D version was generated in this run.

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/vivian-banshee/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\vivian-banshee\`；自定义 `CODEX_HOME` 时使用其 `pets/vivian-banshee/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/vivian-banshee/`
(default `~/.codex/pets/vivian-banshee/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。其余动作、neutral 和 16 个观察方向保持原版；ID 和 v2 格式不变。
The idle frames account for the desktop client's slow idle playback. Other states,
the neutral frame, all 16 look directions, the ID, and the v2 contract are preserved.

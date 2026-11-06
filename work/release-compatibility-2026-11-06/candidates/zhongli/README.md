# Zhongli 钟离 — Codex 2D Pet v2

这是已完成质量验收的 Codex v2 2D 动态宠物包。

## 内容

- `pet.json`：宠物清单，包含 `spriteVersionNumber: 2`。
- `spritesheet.webp`：1536×2288 RGBA 图集，8 列 × 11 行，每格 192×208。

图集包含 9 条标准动画与 16 个顺时针视线方向；未使用的标准行动画格保持全透明。

## 本地安装（可选）

如需安装，可将整个 `zhongli-2d` 文件夹复制到：

```text
${CODEX_HOME:-$HOME/.codex}/pets/zhongli/
```

本次交付只生成本地 2D 包，没有自动安装、上传或发布，也没有制作 3D 版本。

## 质量状态

- v2 尺寸与网格验证：通过。
- 透明像素 RGB 残留：0。
- 九条标准动画独立视觉 QA：通过。
- 四个方向锚点及 16 向连续循环：通过。
- 三人隔离盲测：硬基准方向全部通过；仅两个近竖直中间方向保留允许的横向含糊提示。
- 最终独立包装级视觉 QA：通过。

<!-- DESKTOP-COMPATIBILITY-2026-11-06 -->
## 安装 / Installation · 2026-11-06

ZIP 根目录直接包含 `pet.json`、`spritesheet.webp` 和本说明。解压到
`~/.codex/pets/zhongli/`，确保 `pet.json` 直接位于该目录，不再套一层文件夹。
Windows 对应 `%USERPROFILE%\.codex\pets\zhongli\`；自定义 `CODEX_HOME` 时使用其 `pets/zhongli/`。
打开 Settings → Pets，Refresh 后选择本角色，再用 `/pet` 显示。

Extract the ZIP directly into `CODEX_HOME/pets/zhongli/`
(default `~/.codex/pets/zhongli/`). The manifest must be immediately inside that
directory. Refresh Settings → Pets, select the pet, then use `/pet`.

待机帧已适配当前桌面端的慢速播放，避免眨眼被拉成长时间闭眼。其余动作、neutral 和 16 个观察方向保持原版；ID 和 v2 格式不变。
The idle frames account for the desktop client's slow idle playback. Other states,
the neutral frame, all 16 look directions, the ID, and the v2 contract are preserved.

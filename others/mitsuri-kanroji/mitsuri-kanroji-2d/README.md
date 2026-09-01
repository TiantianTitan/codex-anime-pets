# 甘露寺蜜璃 Mitsuri Kanroji — Codex 2D Pet v2

可直接用于 Codex 桌面端的 2D 宠物成品包。

## 文件

- `pet.json`：Codex 宠物清单，ID 为 `mitsuri-kanroji`。
- `spritesheet.webp`：透明 RGBA 精灵图集，1536×2288，8 列×11 行，每格 192×208。

## 动画内容

- 9 个标准状态：idle、running-right、running-left、waving、jumping、failed、waiting、running、review。
- 16 个顺时针观察方向：000° 至 337.5°，每步 22.5°。
- `spriteVersionNumber` 为 `2`。

角色特征保持为粉色渐变草绿色的双辫、绿色眼睛、深色队服、白色羽织、绿色条纹长袜与草履。动作以紧凑、清楚的全身轮廓呈现，适合 192×208 单格播放。

完整质检记录位于同级 `../qa/`：机械规格验证无错误无警告，四个方向硬门槛全部通过，最终独立视觉质检为 PASS。

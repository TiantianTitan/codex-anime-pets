# Kafka 卡芙卡 — Codex 2D Pet v2

可直接用于 Codex 桌面端的 Kafka 2D 宠物成品包。

## 文件

- `pet.json`：Codex 宠物清单，ID 为 `kafka`。
- `spritesheet.webp`：透明 RGBA 精灵图集，1536×2288，8 列×11 行，每格 192×208。

## 动画内容

- 9 个标准状态：idle、running-right、running-left、waving、jumping、failed、waiting、running、review。
- 16 个顺时针观察方向：000° 至 337.5°，每步 22.5°。
- `spriteVersionNumber` 为 `2`。

角色保持酒紫色层次短发、头顶墨镜、紫粉色眼睛、白色高领上衣、黑紫不对称外套、深色短裤与腿带、黑色短靴和酒紫色手套。动画采用紧凑、清晰的全身轮廓，适合 192×208 单格播放。

本次仅制作 2D，没有生成 3D。完整质检记录位于同级 `../qa/`：机械规格验证无错误无警告，四个方向硬门槛全部通过，最终独立视觉质检为 PASS。

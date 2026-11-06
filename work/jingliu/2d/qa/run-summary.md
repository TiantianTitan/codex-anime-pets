# 镜流 2D — 交付与质检记录

完成时间：2026-11-06 17:23:39 UTC。本轮记录耗时 100 分 33 秒；从准备到交付的墙钟时间，不等同于纯生成时间。

## 交付

- ID：`jingliu`；展示名：Jingliu；仅 2D，无 3D。
- 产品目录：`honkai-star-rail/Jingliu/jingliu-2d/`。
- 安装包：`honkai-star-rail/Jingliu/jingliu-2d-codex-pet-v2.zip`，2,529,130 字节。
- 目录及 ZIP 直接包含 `pet.json`、`spritesheet.webp`、`README.md`；没有参考图、QA 文件或额外嵌套目录。
- 图集：1536 × 2288，8 列 × 11 行，单格 192 × 208，spriteVersionNumber 2。
- 57 个标准动作帧、16 个观察方向和 1 个中立姿态，共 74 个使用格；其余格透明。
- 九组动作：待机、向右跑、向左跑、招手、跳跃、失败、等待、工作、审阅。

最终 WebP SHA256：`77625012a7c1796393cbd09382d9fb03844f86821e7a2840a7c80aa601ed68d2`。

ZIP SHA256：`ba0148f39a04ae2f379c7c14cfb8b7326b6aa7f6a31964f4ead00b5eb980ee51`。

所有交付文件校验值见 [SHA256SUMS](SHA256SUMS)，在仓库根目录运行 `sha256sum -c work/jingliu/2d/qa/SHA256SUMS` 可复核。

## 已验证

- 按 hatch-pet 与固定帧动作规范制作；左右跑分别保留正确的花饰、银饰、红绳和持剑手，没有简单镜像角色服装。
- 13 个生成任务均完成。右跑重做为交替支撑腿的步态；左跑修复肩饰；第二排观察方向整排修正朝向。最终图集没有局部拼入独立新生的观察格。
- [源帧重建](source-reconstruction.json)：57 个标准帧与 16 个观察帧均可从保留的整排源图精确复现；没有打乱顺序或重复静帧填充。清理后再次验证通过。
- [透明边缘](chroma-despill-extended.json)：仅一次最终边缘去底色，完整 alpha 不变；透明像素隐藏 RGB 为零。
- [动作预览](preview-validation.json)与[衔接序列](transition-validation.json)：从最终图集生成 lossless WebP，按时间区间核对 alpha 与可见 RGBA，以及总时长。
- [三份盲测汇总](direction-blind-validation.json)：四个主方向均通过，五处中间方向细微分量保留警告，详见下文。
- [独立最终视觉复查](final-visual-review.json)：通过，并绑定上述最终图集 SHA256。角色尺寸、剑的完整性、发梢与脚部边界、跑步交替腿、紧凑跳跃、待机衔接均已检查。
- [交付包验证](delivered-package-validation.json)：目录与 ZIP 内容一致，平铺根目录正确，临时 `CODEX_HOME/pets/jingliu` 解包验证通过，未修改用户安装。

## 已接受的轻微限制

135°、157.5°、202.5°、225° 的水平方向差别，以及 292.5° 的轻微向上分量，不够醒目。157.5° 的孤立水平盲测被读为向左，不能宣称该格有清晰可靠的向右眼神。该格实际呈明显向下、近正面的过渡姿态；主审与独立复查在原始尺寸顺序图中均未发现显著反向跳变，因此作为轻微方向辨识限制保留。

稳定槽位提取的九条提醒、下肢透明空隙和三个方向差分离群项均已视觉复查：空隙位于靴子、剑尖及衣摆之间，不是人体缺损；未发现可见尺寸突变或裁切。判定和证据见 [警告处理](blind-review-resolution.json)与[逐方向语义](direction-semantics.json)。

## 运行范围与保留文件

时序依据限定于已检查的 Codex Desktop **26.1007.21434**，不代表其他版本。检查覆盖静态原始尺寸帧、编码后的时间线和临时安装目录；没有启动实际客户端测试播放，不能把素材中的所有动作解释为客户端必定触发。

依照用户要求，后续检查全部后台执行，不弹出检测窗口或抢焦点。没有安装宠物、修改项目主 README、提交或推送。

8 张用户原始参考图仍完整保留于本地 Git 忽略的 `references/source-originals/`，清理后已重新核对哈希与忽略规则。QA 仅在 work 内。选中的源图、提取帧、参考板、最终预览与审核记录继续保留。

重复的 generated_images 原图、临时提示文件、重复提取帧、旧预览和未使用的跑步布局已移入系统回收站，可恢复；未删除用户原图。逐项记录见 [cleanup.json](cleanup.json)。

最终动作预览位于 [previews-final](previews-final/)，动作与待机衔接位于 [transitions-final](transitions-final/)。

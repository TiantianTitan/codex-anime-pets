# Hu Tao 2D look mechanics

## Fixed identity and anchors

- Keep the same compact full-body 2D chibi Hu Tao, face, flower-shaped crimson pupils, hair silhouette, costume, palette, proportions, and outline treatment used by the canonical base.
- Keep both feet, pelvis, and lower torso planted at one stable baseline. Never rotate, skew, lean, or translate the whole sprite to imitate gaze.
- The tall hat, beige talisman plaque, plum-blossom branch, tassel, long hair, and coat tails remain physically attached. The blossom branch stays on Hu Tao's own right side and never swaps sides.

## Direction mechanics

- Eyes, eyelids, brows, nose/cheek plane, chin, head yaw/pitch, and a restrained upper-torso follow-through carry the direction. The large flower pupils must remain recognizable rather than being replaced or distorted.
- `000 up`: pupils and eyelids rise; chin and face pitch upward; the torso stays planted.
- `090 screen-right`: pupils, nose, cheek plane, chin, and head turn unmistakably toward screen-right; preserve accessory handedness and plausible occlusion.
- `180 down`: pupils and eyelids lower; chin tucks and the hat brim may overlap slightly more of the forehead; feet and pelvis remain fixed.
- `270 screen-left`: pupils, nose, cheek plane, chin, and head turn unmistakably toward screen-left; preserve accessory handedness and plausible occlusion.
- Every diagonal blends both required axes. Intermediate poses advance clockwise in even 22.5-degree visual steps without pauses, reversals, or duplicated cardinals.

## Secondary follow-through

- The hat, talisman, blossom branch, tassel, hair, and coat tails follow head and upper-torso motion only through small perspective and overlap changes. They must not drift, detach, change shape, or become direction indicators by themselves.
- Keep body scale, foot position, silhouette, line weight, lighting, and chroma background stable across all 16 directions.
- No neutral/front pose belongs in rows 9-10; neutral is handled by idle outside the pointer loop.

# Zhu Yuan look row 10 — continuous ponytail through both loop boundaries

Regenerate the complete eight-pose row as one coherent family. The latest full row already has correct gaze directions, compact first-half height, safe top clearance, stable baseline, identity, and rendering. Preserve those qualities. Its only hard visual defect is that Zhu Yuan's large side ponytail jumps across the head at `157.5 -> 180` and again at `337.5 -> 000`.

Use the completed row 9 to match the first boundary and the supplied four-pose hair-transition reference to match the final boundary. Treat the ponytail as one attached three-dimensional mass rotating continuously behind the skull—not a fixed sticker and never a mirrored costume swap.

## Exact eight-pose sequence

Draw exactly: `180, 202.5, 225, 247.5, 270, 292.5, 315, 337.5`.

- `180 down`: frontal/down with low irises and tucked chin. Continue row-9 `157.5` directly: the ponytail bulk and red tie must remain on the same **image-left/rear** side at this first step. Do not move it overhead or to image-right yet.
- `202.5 down-left`: face begins screen-left; ponytail moves inward behind the crown from image-left toward center.
- `225 down-left`: ponytail is centered/partly occluded behind the crown; no side jump.
- `247.5 down-left`: stronger left turn; ponytail begins emerging on image-right/rear.
- `270 left`: unmistakable screen-left profile with the ponytail attached behind on image-right/rear.
- `292.5 up-left`: remain screen-left and begin lifting; ponytail moves inward from image-right toward crown center.
- `315 up-left`: clearer upward pitch and more open face; ponytail is mostly behind/near crown center, partially occluded if needed.
- `337.5 up-left`: broad near-frontal up-left one step before row-9 `000`; ponytail has already crossed behind the crown and emerges mostly on **image-left**, matching `000` without a final flip.

The ponytail path across the row is therefore:

`image-left at 157.5/180 -> behind center -> image-right at 247.5/270 -> behind center -> image-left at 337.5/000`.

## Direction and geometry gates

- All directions are viewer/screen coordinates.
- Poses 2–4 must remain down-left; pose 5 must be an unmistakable screen-left cardinal; poses 6–8 must remain up-left without reversing screen-right.
- Match the latest accepted row's practical registered geometry: approximately 425–450 px raw silhouette height for the compact down-facing poses, growing gradually toward the up-left poses without exceeding safe top clearance.
- Keep one shared shoe baseline, stable head/body scale, eight separated groups, and broad uninterrupted green above/below/between all poses.
- Preserve Zhu Yuan's face, orange-red front streak, high ponytail and red tie, blue-and-black Public Security uniform, armor, holster, sidearm, proportions, palette, outlines, and cel shading.

## Output contract

- One horizontal strip on perfectly flat uniform `#00FF00`.
- Exactly eight complete full-body sprites; no overlap, clipping, merged groups, detached hair, extra tail, shadows, particles, labels, guide marks, text, or scenery.

Reject if either boundary still flips the ponytail side, if the tail detaches or changes identity, if 270 is not screen-left, if poses 6–8 point screen-right, or if any silhouette touches the registered cell edge. Draw the entire row together; never patch, mirror, resize, or transform an individual cell.

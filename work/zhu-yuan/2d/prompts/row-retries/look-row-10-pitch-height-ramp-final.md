# Zhu Yuan look row 10 — fix only the pitch-height ramp

Regenerate the complete eight-pose row as one coherent new drawing. The supplied full-row candidate has approved identity, directions, ponytail travel, spacing, baseline, and rendering. Preserve those decisions. Its remaining defect is geometric: the first four down-looking poses are taller than the last row-9 pose and touch the registered cell top.

## Exact redraw target

- Keep exactly eight complete separated poses in this order: `180, 202.5, 225, 247.5, 270, 292.5, 315, 337.5`.
- Redraw poses 1–4 at approximately **90–92% of the supplied full-row candidate's current silhouette height** while preserving natural proportions. They must not be cropped or squashed.
- Pose 1 (`180`) must visually match row 9's final `157.5` pose in overall silhouette height, head size, planted baseline, and compact down-looking posture.
- From pose 1 through pose 8, let the crown rise gradually as the gaze travels from deep down through left to up-left. There must be no early tall pose and no late size pop.
- Keep poses 5–8 close to their supplied candidate height, because their current registered height already approaches the approved `000` correctly.
- Keep one identical shoe baseline across the row. The changing crown height must come from natural chin tuck / lift and posture, not moving or scaling the whole sprite independently.

## Preserve the accepted visual logic

- Pose 1 remains frontal/down with low irises, tucked chin, and ponytail centered/partly occluded behind the crown.
- Poses 2–4 turn smoothly down-left; the ponytail moves gradually toward image-right/rear.
- Pose 5 is an unmistakable viewer/screen-left profile.
- Poses 6–8 remain on the screen-left half and reopen upward in distinct steps; never reverse screen-right.
- By pose 8, the face is broad near-frontal up-left and the ponytail has crossed behind the crown toward image-left, flowing into approved `000`.
- Preserve Zhu Yuan's face, orange-red streak, high ponytail/red tie, blue-and-black Public Security uniform, armor, holster, sidearm, palette, linework, and cel shading.

## Hard output contract

- Perfectly flat, uniform `#00FF00` horizontal strip.
- Broad uninterrupted green above every crown and ponytail, below every shoe, between every neighboring pose, and at both outer edges.
- Exactly eight foreground groups; no overlap, merged figures, outer-edge clipping, guide marks, text, labels, shadows, particles, detached effects, or scenery.

Reject if pose 1 is still as tall as the supplied candidate, if the first four touch the top-safe area after registration, if any direction or ponytail side changes from the accepted candidate, or if baseline/scale jumps remain. Draw the whole row together; never patch, mirror, resize, or transform an individual cell.

# Ellen Joe look mechanics

## Natural motion model

Ellen is a compact humanoid shark Thiren. Her gaze is led by the red irises and eyelids, followed by a restrained head-and-neck turn and only a small upper-torso follow-through. Her feet, heels, pelvis, lower torso, and the physical root of the shark tail stay registered to the neutral idle pose. The maid headdress remains attached to the skull; the short black-and-red hair tips may lag by only a few pixels. The heavy shark tail may counterbalance gently through its outer curve and tip, but its lower-back attachment must never jump, flip sides, detach, shrink, or pass through the body. She has no handheld prop in this pet identity.

Preserve facial anatomy rigidly: no broad raster warps, stretched skull, displaced mouth, replacement eyes, floating pupils, or white/silver hair. The whole sprite never rotates, skews, or rocks. Eyes participate as complete anime eyes: iris/pupil direction, eyelid shape, and eyebrow angle change together, followed by the head; pupil-only motion is insufficient.

## Stable anchor and motion budget

- Stable anchor: both feet and heels, pelvis, lower torso center, and tail root.
- Leading motion: both red eyes and eyelids.
- Following motion: nose/chin, head yaw or pitch, neck, shoulders, then a very small upper-torso shift.
- Secondary follow-through: short red inner hair tips, maid frill, and the distal tail curve; all remain physically attached.
- Each 22.5-degree step changes the eyes, head angle, shoulder visibility, and tail counterbalance by roughly one even increment. No adjacent step may introduce a larger scale change, baseline shift, facial redesign, side flip, or tail teleport.
- Keep the same head size, body height, baseline, outfit, black-red hair, sleepy expression family, and tail volume in all 16 poses.

## Cardinal pose families

### 000 — up

Eyes and complete irises aim clearly above their neutral centers; upper eyelids open slightly, chin lifts, and the head pitches upward without leaning the whole body. The lower face and underside of the fringe become a little more visible while the feet and torso base remain fixed. Shoulders follow upward only subtly. The tail root stays fixed and the tip settles slightly lower as a restrained counterbalance.

### 090 — screen-right

The nose tip and both red pupils sit unmistakably to the screen-right of the head center. The head turns to a readable rightward three-quarter pose: the screen-right cheek/profile becomes stronger, the far eye narrows naturally, and the hair/headdress occlusion changes continuously without swapping the hair clip or red inner tips. The upper torso follows a few degrees to screen-right while hips and feet remain front-registered. The tail remains attached behind her and its outer curve lags slightly toward screen-left.

### 180 — down

Eyes and complete irises aim clearly below their neutral centers; upper eyelids lower, chin tucks toward the collar, and the head pitches down. More of the headdress and crown are visible while the lower face is slightly occluded by the downward angle. Shoulders soften forward without collapsing or changing scale. The tail root and feet stay fixed; the tip rises only slightly as a counterbalance.

### 270 — screen-left

The nose tip and both red pupils sit unmistakably to the screen-left of the head center. The head turns to a readable leftward three-quarter pose: the screen-left cheek/profile becomes stronger, the far eye narrows naturally, and the asymmetrical bangs, hair clip, red inner tips, and maid spikes keep their canonical sides. The upper torso follows a few degrees to screen-left while hips and feet remain fixed. The tail stays attached behind her and its outer curve lags slightly toward screen-right.

## Diagonal interpolation

Row 9 proceeds `000 → 022.5 → 045 → 067.5 → 090 → 112.5 → 135 → 157.5`: up-right gradually gives way to right, then to down-right. Row 10 proceeds `180 → 202.5 → 225 → 247.5 → 270 → 292.5 → 315 → 337.5`: down-left gradually gives way to left, then to up-left. Every diagonal must preserve both expected axes through eyes, eyelids, nose/chin, and head angle. The cross-row transition `157.5 → 180` and loop closure `337.5 → 000` must be one ordinary 22.5-degree step, with no snap in face, tail, scale, or registration.

## Hard failures

Reject ambiguous or reversed cardinals; front-facing left/right poses; eyes locked in one expression while the head moves; whole-sprite tilt or affine rotation; silver/white hair; false animal ears; replacement eyes; detached or side-flipped tail; changing tail volume; shifted feet or baseline; facial proportion drift; guide marks, labels, shadows, glows, text, scenery, or detached effects.

# Kazuha chibi look mechanics

## Natural motion

Kazuha is a compact humanoid chibi, so his gaze begins in the eyes and eyelids, continues through a small head-and-neck turn, and finishes with restrained upper-torso follow-through. His feet, lower body, scale, and baseline stay anchored. The skull, face, hands, and costume retain their proportions without raster warping.

The short sheathed katana stays attached at the hip and follows the torso as one rigid worn prop. The compact scarf tail stays connected at the neck and may lag by only a small, even amount between adjacent directions. Hair tips and the red streak follow the head turn while preserving their side and shape. Costume asymmetry never swaps sides.

## Cardinal pose families

- `000 up`: eyes and irises rise, upper eyelids open slightly, chin lifts, and a little more neck and lower face becomes visible. The torso remains front-biased and grounded.
- `090 screen-right`: pupils, nose tip, chin, and face plane move unmistakably toward the image-right side of the head center. The screen-left side of the head becomes more visible while the far cheek narrows. The attached sword and scarf follow the torso without changing sides.
- `180 down`: eyes and irises lower, upper eyelids soften, chin tucks, and more crown and bangs become visible. The body remains grounded and front-biased.
- `270 screen-left`: pupils, nose tip, chin, and face plane move unmistakably toward the image-left side of the head center. The screen-right side of the head becomes more visible while the far cheek narrows. The attached sword and scarf follow the torso without changing sides.

## Motion budget and continuity

Each 22.5-degree step moves the eyes, eyelids, head angle, upper torso, hair tips, and scarf by a small and roughly equal visual amount. The feet, lower-body anchor, body height, and baseline remain stable. No adjacent pair may flip the red hair streak, sleeves, sword, scarf, or visible face side. `157.5 -> 180` and `337.5 -> 000` must be one ordinary step with no snap, scale pop, or registration jump.

The final 16-pose loop must read as a smooth clockwise gaze arc at normal `192x208` pet size. It must not use whole-sprite rotation, affine tilt, pupil-only motion, replacement eyes, pixel-art rendering, detached maple leaves, wind streaks, shadows, text, degree labels, or guide marks.

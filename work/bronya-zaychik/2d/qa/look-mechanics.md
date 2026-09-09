# Bronya Zaychik look mechanics

## Natural motion

Bronya is a compact humanoid chibi, so her gaze is led by both gray irises and matching eyelid/eyebrow changes, followed by a restrained head-and-neck turn and only a small upper-torso follow-through. Her boots, feet, hips, baseline, overall height, and head size stay registered. The skull and facial proportions never stretch or warp.

Her large navy bows remain fixed to the head. The segmented silver drill twin-tails turn with the head as attached volumes and lag only slightly at their outer curls; they never detach, exchange sides, or change length. The gold shoulder braid, mechanical gauntlets, skirt, and armored boots keep their canonical side-specific construction. Arms remain close to the body and do not become a second gesture animation.

## Cardinal pose families

- `000 up`: broadly front-facing. Both eyes remain visible; irises sit high inside their original apertures, upper eyelids open slightly, chin lifts, and the face exposes a little more neck. The torso stays frontal and upright.
- `090 screen-right`: head and eyes turn unmistakably toward the image-right edge. The nose tip, pupils, chin projection, and visible facial plane move to the right of head center; the far eye narrows naturally. The screen-right cheek becomes the leading contour while the twin-tails follow the yaw without changing their identity or the shoulder-braid side.
- `180 down`: broadly front-facing. Irises sit low, upper lids lower, chin tucks, and the bangs/crown become more prominent while the neck becomes less visible. The body remains upright and registered.
- `270 screen-left`: head and eyes turn unmistakably toward the image-left edge. The nose tip, pupils, chin projection, and visible facial plane move to the left of head center; the far eye narrows naturally. The screen-left cheek becomes the leading contour while every fixed asymmetry stays on its canonical side.

## Interpolation and motion budget

Each 22.5-degree step advances the eyes, eyelids, chin, nose projection, head yaw/pitch, and drill-tail follow-through by a comparable amount. Diagonals combine both required axes rather than dropping one. The lower body and foot line remain fixed; upper-torso shift is subtle and continuous. `157.5` must be one natural step before `180`, and `337.5` must be a near-front up-left pose one natural step before the approved `000`, with no late scale change, recentering jump, profile flip, or sudden reopening of the face.

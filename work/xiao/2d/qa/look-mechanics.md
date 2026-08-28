# Xiao Look Mechanics

## Natural Motion Choice

Xiao is a compact humanoid chibi, so the gaze is led by his golden irises, eyelids, and eyebrows; the head and neck follow with a restrained turn or pitch, and the upper torso follows only slightly. His feet, lower torso, overall body scale, and baseline remain anchored. Do not rotate, skew, warp, or translate the entire sprite.

The face should remain calm and vigilant. Looking up opens the lower eyelid slightly and raises the chin; looking down lowers the chin, upper lids, and brow without crushing the facial proportions. Horizontal looks turn the eyes and face toward the viewer's corresponding screen edge, changing visible cheek/nose placement and occlusion rather than sliding only the pupils.

## Anchors and Follow-Through

- Feet and lower pelvis are the stable registration anchor in all 16 poses.
- Eyes lead each step; eyelids and brows reshape with them; head/neck follow; shoulders and upper chest follow by a smaller amount.
- Hair stays attached and preserves the same silhouette. Face-framing locks may overlap one cheek more as the head turns; the cowlick and teal tips follow subtly with no detached strands.
- The exposed green-tattoo arm and opposite black-gloved arm remain on their correct anatomical sides.
- The Yaksha mask remains physically secured against the same hip/hand area. It follows the torso with minimal lag, becomes slightly more side-on or partly occluded as Xiao turns, and never floats or swaps sides.
- Beads, jade ornaments, fabric panels, and sash tails remain attached. They may shift a few pixels continuously with the torso but must not jump, swap layering, or form detached fragments.

## Cardinal Pose Families

- `000 up`: eyes and irises unmistakably aim upward; eyelids open toward the top, chin lifts, and a little more underside of the jaw/collar shows. Torso stays front-readable and feet fixed. The forehead diamond remains centered and visible.
- `090 screen-right`: eyes, nose tip, chin, and face turn toward the viewer's right edge. The screen-left cheek becomes more visible while the screen-right facial contour narrows; hair overlaps the far cheek appropriately. The upper torso yaws slightly right, and the attached mask/ornaments follow without changing side.
- `180 down`: eyes aim down; upper lids and brow lower, chin tucks toward the collar, and more top hair/forehead plane is visible. Feet and lower body remain fixed; do not shrink or crouch the whole sprite.
- `270 screen-left`: eyes, nose tip, chin, and face turn toward the viewer's left edge. The screen-right cheek becomes more visible while the screen-left facial contour narrows; hair occlusion reverses naturally from `090`. The upper torso yaws slightly left, and tattoo/glove/mask side relationships remain anatomically correct.

## Intermediate Directions and Motion Budget

Each 22.5-degree step changes the eye aim, eyelids, head pitch/yaw, hair occlusion, shoulder turn, and constrained prop follow-through by a similar small visual amount. No adjacent pair may contain a large head-size change, body translation, mask teleport, costume flip, or expression reset.

- `022.5`, `045`, `067.5`: progressively move from up toward screen-right, adding rightward face turn evenly while relaxing the upward pitch.
- `112.5`, `135`, `157.5`: progressively move from screen-right toward down, deepening the chin tuck evenly while retaining the rightward turn until the final step.
- `202.5`, `225`, `247.5`: progressively move from down toward screen-left, adding leftward face turn evenly while relaxing the downward pitch.
- `292.5`, `315`, `337.5`: progressively move from screen-left toward up, raising the gaze/chin evenly while retaining the leftward turn until the final step.

Row 9 ends at `157.5`, one even step before the approved `180`. Row 10 begins at `180` and ends at `337.5`, one even step before the approved `000`. The ordered loop must never reverse or pause on a neutral/front-facing pose.

## Identity and Failure Gates

- Preserve golden eyes, purple forehead diamond, dark teal-tipped hair, pale face, tattooed arm, black-gloved opposite arm, white sleeveless top, purple/navy trousers and sash, jade/bead ornaments, long attached fabric tails, and secured Yaksha mask.
- Preserve facial proportions and calm persona; no stretched skull, replacement eyes, exaggerated grin, or generic surprised expression.
- No long polearm, new prop, text, degree labels, arrows, clock graphics, scenery, floor, shadow, glow, aura, detached particles, or chroma-colored details inside the pet.
- Cardinals are hard gates: `000` up, `090` screen-right, `180` down, `270` screen-left must be unmistakable at normal pet size.

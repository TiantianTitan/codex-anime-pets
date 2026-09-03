# Jane Doe — V2 Look Mechanics

## Natural motion

Jane is a compact humanoid rat Thiren, so her green eyes lead each glance, followed by a restrained head-and-neck turn and a smaller upper-torso follow-through. Her facial proportions, sly expression, feet, lower torso, and baseline stay stable. The rat ears remain attached to the skull and follow the head angle; the short front bob and long wine-red rear hair lag slightly. Her single charcoal tail stays attached at the same waist point, bends continuously as a flexible counterbalance, and never swaps sides or becomes a second tail.

No whole-sprite rotation, skew, stretching, or sliding is allowed. Eye motion must remain inside the original eye apertures with coherent eyelid and eyebrow changes; do not add replacement eyes or floating pupils. The oversized jacket, cream collar, waist straps, asymmetrical stockings, boots, and tail attachment must keep their original construction.

## Cardinal pose families

- `000 up`: near-frontal. Pupils sit visibly high inside both green eyes; upper lids open slightly, eyebrows lift, chin rises, and a small amount of jaw/cream-collar underside becomes visible. Ears and front fringe follow upward. Feet and lower body remain planted.
- `090 screen-right`: unmistakable right-facing three-quarter-to-profile head. Nose tip, chin, pupils, and facial plane project to the image-right of the head center; the rear hair mass trails to image-left. The upper torso turns slightly right while the feet stay registered. Tail remains attached and lags gently toward image-left.
- `180 down`: near-frontal bowed pose. Pupils and lids sit low, chin tucks into the cream collar, more crown and upper fringe are visible, and shoulders compress slightly. The tail relaxes lower without detaching.
- `270 screen-left`: unmistakable left-facing three-quarter-to-profile head, the true visual opposite of `090`. Nose tip, chin, pupils, and facial plane project to the image-left of the head center; rear hair mass trails to image-right. The upper torso turns slightly left, while the feet stay registered. Tail remains attached and lags gently toward image-right.

## Motion budget and continuity

Every 22.5-degree step moves the eyes first, then the head by an even small increment, then the shoulders, hair, ears, and tail by a still smaller follow-through. Character height, head size, foot position, lower-body anchor, and tail root remain stable. The `157.5 → 180` and `337.5 → 000` boundaries must be only one ordinary step. Horizontal direction is judged in viewer/image coordinates: the physical face and nose must actually cross toward the named screen edge. Vertical direction is carried by pupil height, eyelids, chin pitch, visible crown/jaw underside, and restrained shoulder compression or lift.

The complete clockwise loop is one continuous animation family, not independent poses. Keep the tail compact inside each slot, with no wide detached arc, clipping, or sudden side flip.

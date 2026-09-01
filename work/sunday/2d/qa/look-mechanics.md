# Sunday look mechanics

## Natural motion

Sunday is a compact humanoid chibi with a separate head and body. His gaze is led by the golden eyes, eyelids, and brows; the head and neck then follow with restrained yaw or pitch, while the upper torso contributes only a very small turn. The skull, face spacing, hands, clothing, and halo must never be warped. The sprite must never be rotated, skewed, or tilted as a whole.

The boots, lower legs, coat hem baseline, and lower-body center remain the shared registration anchor. Body height, head size, and baseline stay stable across all sixteen directions. The long coat panels may overlap differently as the torso turns, but they do not swing to a new position or cross cell boundaries.

The ornate gold halo is a rigid head-mounted structure. It follows the head as one attached unit with changing perspective and occlusion, never spins independently, changes shape, or floats away. The small feather-like ornaments beside the head also follow the head: the nearer side may become more visible and the far side may be partly hidden by hair. Hair tips may lag by a very small continuous amount. Sunday has empty hands, so no book, feather, ribbon energy, UI, text, or new prop may appear.

## Cardinal pose families

- `000 up`: near-frontal pose, chin visibly lifted, pupils and irises high within the original eye apertures, upper eyelids reshaped for an upward gaze, and a little more neck/lower-eye area visible. The halo stays centered behind the raised head. This is unmistakably up, not neutral.
- `090 screen-right`: the nose tip, pupils, and facial plane cross to the viewer's screen-right side of the head center. The head and neck turn right into a readable three-quarter/profile family; the far-side ornament is partly occluded while the near-side ornament and cheek are more visible. The torso follows only slightly.
- `180 down`: near-frontal pose, chin tucked, pupils and irises low inside the original eye apertures, lids and brows lowered, more crown/hair visible, and less neck visible. The halo remains attached and rises perceptually behind the bowed head. This is unmistakably down.
- `270 screen-left`: the nose tip, pupils, and facial plane cross to the viewer's screen-left side of the head center. The head and neck turn left into the opposing three-quarter/profile family; occlusion of the two side ornaments reverses relative to `090`. The torso follows only slightly.

## Intermediate directions and motion budget

Generate each 22.5-degree step as an even interpolation between the adjacent cardinal families. Eyes lead by a small amount, then head/neck, side ornaments, halo perspective, hair tips, and finally a restrained upper-torso follow-through. No neighboring step may introduce a larger scale change, baseline shift, halo jump, face flip, coat-panel teleport, or silhouette snap than the others.

Row 9 advances continuously through `000 -> 022.5 -> 045 -> 067.5 -> 090 -> 112.5 -> 135 -> 157.5`. Row 10 continues `180 -> 202.5 -> 225 -> 247.5 -> 270 -> 292.5 -> 315 -> 337.5`. The boundary `157.5 -> 180` must be exactly one down-right-to-down step, and `337.5 -> 000` exactly one up-left-to-up step. Each diagonal must preserve both named axes at normal pet size.

## Identity and safety gates

Preserve the canonical pale blue-gray layered hair, golden eyes, original eye construction, gold halo, head-wing ornaments, calm expression, and asymmetric white/cobalt/navy/gold outfit. Do not replace the eyes, slide detached pupils, mirror the asymmetric outfit, stretch facial features, rotate the whole sprite, add shadows or effects, or let any attached element clip the cell edge.

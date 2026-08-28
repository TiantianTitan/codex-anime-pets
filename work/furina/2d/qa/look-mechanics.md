# Furina look mechanics

Furina is a humanoid chibi pet, so her gaze is led by the original water-drop eyes, followed by a restrained head-and-neck turn and a smaller upper-torso response. Her feet, lower body, body scale, and baseline stay anchored. The motion must never be simulated by rotating, skewing, stretching, or rocking the whole sprite.

## Identity and physical constraints

- Preserve the same short-haired, dark-navy-outfit Furina used by the approved standard atlas; never switch to the long-haired white outfit.
- Preserve her two original blue water-drop eyes, their asymmetric/heterochromic color treatment, eye whites, eyelids, lashes, highlights, and spacing as one coherent eye construction. Do not add floating pupils, duplicate eyes, or round replacement eyes.
- The eyes lead each direction. Eyelids and eyebrows reshape with the gaze; the head and neck follow subtly; the shoulders and upper torso may turn a little. The skull, mouth, hands, and costume proportions remain rigid and recognizable.
- Her navy crown-like top hat is worn and therefore follows the head. Its gold prongs, blue teardrop motifs, side ribbon, curled forelock, and short pale-cyan hair tips may lag by a very small amount between neighboring poses, but they remain attached and never flip sides or teleport.
- No cane, scroll, Hydro summon, bubble, label, arrow, clock, shadow, glow, scenery, or detached effect is allowed.

## Cardinal pose families

- `000 up`: pupils and irises rise; upper eyelids open slightly; chin lifts and the face pitches upward without leaning the body backward. The hat follows the head while feet and lower torso remain fixed.
- `090 screen-right`: pupils, nose tip, and face aim unmistakably toward the image's right edge. The head yaws right enough to reveal more of the far cheek/hair contour and reduce the near-side contour; shoulders follow only slightly. Hat ribbon and hair tips remain attached and trail the turn subtly.
- `180 down`: pupils and irises lower; upper eyelids soften; chin drops and the hat brim may occlude a little more forehead without hiding the eyes. The upper torso compresses only slightly while the grounded lower body remains fixed.
- `270 screen-left`: pupils, nose tip, and face aim unmistakably toward the image's left edge. The head yaws left with the opposite cheek/hair occlusion family from `090`, while preserving Furina's asymmetric hat and hair construction instead of mirroring it.

## Motion budget and continuity

Each 22.5-degree step moves the eye direction, eyelids, head yaw/pitch, hat, forelock, and shoulders by roughly one equal visual increment. Diagonals combine both required axes: up-right, down-right, down-left, or up-left. No adjacent pair may introduce a large pose jump, scale change, baseline shift, costume flip, facial redesign, or prop change. The transitions `157.5 -> 180` and `337.5 -> 000` must be as smooth as every internal step. Every direction must remain distinct from the neutral idle pose at normal pet size.

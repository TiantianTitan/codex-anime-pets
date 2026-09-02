# Kafka look mechanics

Kafka is a humanoid chibi pet with large visible eyes, a separate head and neck, layered side locks, head-worn sunglasses, a fitted asymmetric coat, and grounded boots. Looking around should read as controlled attention rather than whole-body rotation.

## Anchors and motion budget

- Both boots, the pelvis, and the lower torso remain registered to the same baseline and center.
- The mauve-pink eyes lead each change; eyelids and brows reshape with the gaze so the eyes never appear pasted or detached.
- The head and neck follow with a restrained yaw or pitch, while the shoulders and upper torso add only a small counterbalanced turn.
- The round sunglasses remain physically seated on the crown and follow the head as one rigid worn object. They never float, flip sides, or become replacement eyes.
- Long side locks and compact coat tails stay attached and lag the head/shoulder turn by a small, continuous amount. No strand or coat piece becomes a detached component.
- Each 22.5-degree step uses a similar visual increment. Head size, body height, foot baseline, facial proportions, and costume asymmetry remain stable; no whole-sprite rotation, skew, squash, or broad raster warp.

## Cardinal pose families

- `000 up`: near-front body; chin lifted; irises and pupils visibly high inside the original eye shapes; upper eyelids open toward the top; more neck and collar underside visible. Both facial sides remain balanced.
- `090 screen-right`: head and gaze turn toward the image-right edge. The nose tip and pupils cross to the image-right side of the head center; the image-left cheek and hair volume become more visible, while the image-right facial edge compresses. Sunglasses follow the skull and coat asymmetry remains unchanged.
- `180 down`: near-front body; chin tucked; irises and pupils visibly low; upper eyelids lower; bangs and crown become more prominent while the collar/neck is partly hidden.
- `270 screen-left`: head and gaze turn toward the image-left edge. The nose tip and pupils cross to the image-left side of the head center; the image-right cheek and hair volume become more visible, while the image-left facial edge compresses. It must visibly oppose `090` at normal pet size.

## Intermediate directions and continuity

- `022.5`, `045`, and `067.5` interpolate evenly from up toward screen-right.
- `112.5`, `135`, and `157.5` interpolate evenly from screen-right toward down.
- `202.5`, `225`, and `247.5` interpolate evenly from down toward screen-left.
- `292.5`, `315`, and `337.5` interpolate evenly from screen-left toward up.
- Row 10 begins one step after row 9's `157.5`; `337.5` lands one step before row 9's `000` without a scale, baseline, expression, hair, sunglasses, or coat jump.

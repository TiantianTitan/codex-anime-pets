# Obanai 2D look mechanics

Obanai is a humanoid sticker pet with a separate head and torso, large physical eyes, a bandage-covered lower face, layered hair, broad striped sleeves, and one living snake physically wrapped around the neck and shoulders.

## Anchors and motion budget

- Feet, lower legs, belt line, and lower torso remain registered to one common baseline and body scale.
- The physical eyes lead each direction: the visible sclera/iris/pupil/highlight, eyelids, and brow line change together rather than sliding loose pupils over fixed eyes.
- The head and neck follow with restrained yaw or pitch; shoulders and upper torso follow only slightly. Never rotate, skew, stretch, or tilt the whole sprite.
- Bandages remain rigidly wrapped around the mouth and lower face; facial proportions, eye spacing, and hair volume do not deform.
- Each 22.5° step receives roughly one equal increment of eye rotation, eyelid/brow change, head turn or pitch, and subtle shoulder follow-through.
- The haori sleeves remain attached and settle naturally; they do not swap sides or flap into detached shapes.
- The white snake remains one connected neck-and-shoulder companion. Its body stays anchored around the neck; its head follows the character's attention with a small one-step lag and becomes partly occluded as the head turns. It never becomes a second independent gaze marker.
- Preserve character-relative heterochromia through every turn. Eye colors must follow the same anatomical eyes and may become occluded naturally; never recolor whichever eye happens to occupy a screen side.

## Cardinal pose families

- `000 up`: face broadly frontal; both eye globes rotate upward, upper eyelids open and lower lids support the raised gaze; chin and forehead lift slightly. Snake head lifts a little later while remaining on the shoulder.
- `090 screen-right`: nose tip, eye gaze, and face surface move clearly toward the viewer's screen-right edge. The head yaws right with the screen-left side of the hair/face becoming more visible and the far eye partly occluded as physically appropriate. Snake/body attachment stays character-correct and follows the shoulder turn.
- `180 down`: face broadly frontal; eyes rotate down, upper lids lower, chin tucks, and shoulders follow minimally. Bandage stays intact; snake head dips slightly but does not detach.
- `270 screen-left`: exact inverse semantic family of 090. Nose tip, eye gaze, and face surface move clearly toward the viewer's screen-left edge, with the opposite side becoming more visible and the far eye naturally occluded. It must unmistakably oppose 090.

## Continuity

- Row 9 advances `000 → 090 → 180` in even steps; row 10 advances `180 → 270 → 000`.
- `157.5 → 180`, `180 → 202.5`, and `337.5 → 000` must each be one normal step, with no head-size, snake-position, baseline, or registration jump.
- Neutral/front is not one of the sixteen direction cells; every look cell must read differently from idle at normal pet size.

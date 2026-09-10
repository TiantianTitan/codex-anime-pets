# Zhu Yuan look mechanics

## Natural motion

Zhu Yuan is a humanoid chibi with a separate head and a firmly grounded lower body. Keep both feet, pelvis, and lower torso registered to one baseline. Her amber-red eyes lead each look; the eyelids and brows reshape with pitch, then the head and neck follow with restrained yaw or tilt. The shoulders may follow slightly, but the whole sprite must never rotate, skew, lean, or change scale to fake direction.

Her high side ponytail follows the head with a small delayed counter-sway. The orange-red hair streak, silver shoulder armor, lime accents, holster, and compact sidearm remain on their canonical body sides and never swap or mirror. Every weapon and armor piece stays physically attached and follows the body's occlusion naturally.

## Cardinal pose families

- **000 up:** broadly front-facing; irises sit high inside the eye apertures, upper eyelids open, chin lifts, and a little more neck/collar underside becomes visible. Feet and torso remain fixed.
- **090 screen-right:** nose tip, pupils, and facial plane project clearly to the image-right side of the head center. The head turns into a readable right-facing three-quarter/profile family; the rightward body side becomes more visible and the far cheek/eye narrows naturally.
- **180 down:** broadly front-facing; irises sit low, upper lids lower slightly, chin tucks toward the chest, and the crown/bangs become a little more prominent without shrinking the body.
- **270 screen-left:** nose tip, pupils, and facial plane project clearly to the image-left side of the head center. The head turns into the opposing left-facing three-quarter/profile family; the leftward body side becomes more visible and the far cheek/eye narrows naturally.

## Interpolation and motion budget

Build one continuous clockwise family. Each 22.5-degree step changes eye position, eyelids, chin, head yaw/pitch, shoulder follow-through, and ponytail lag by roughly the same visual amount. Diagonals must combine both required axes rather than dropping one. Keep head size, body height, baseline, lower-body anchor, and weapon attachment constant. The `157.5 → 180` and `337.5 → 000` boundaries must be single ordinary steps with no frontal/profile flip, scale pop, or registration jump.

# Burnice White look mechanics

## Natural motion

Burnice looks around as a humanoid character, not as a rotating sprite. Her red-orange eyes lead each change, followed by a small rigid head-and-neck turn and a restrained upper-torso response. The hips, boots, foot line, and lower-body center stay planted. Her twin ponytails follow the head with a slight, continuous lag; the red-black goggles stay fixed to the crown; the close-fitting fuel backpack stays rigidly attached to the torso and changes occlusion with the shoulders.

Facial proportions must remain fixed. Direction is expressed through whole-eye orientation inside the original eye construction, eyelid shape, eyebrow participation, nose and face-plane yaw, chin pitch, and small shoulder follow-through. Do not stretch the head, slide detached pupils, rotate the whole sprite, or tilt the body as one flat card.

## Cardinal pose families

- `000 up`: near-frontal upright pose. Chin lifts, irises sit high inside both eye apertures, upper eyelids open slightly, and more neck/underside of the chin becomes visible. Both ponytails remain balanced and the backpack stays centered behind the torso.
- `090 screen-right`: unmistakable screen-right three-quarter/profile family. Nose tip, face plane, and pupils project to the image-right side of the head center; the far cheek and far eye become more occluded. The image-right shoulder leads and the opposite ponytail/backpack edge becomes more visible through natural occlusion.
- `180 down`: near-frontal bowed family. Chin tucks toward the scarf, irises sit low, upper eyelids lower, and bangs/goggles occupy more of the upper face. Shoulders round only slightly; boots and backpack remain anchored.
- `270 screen-left`: unmistakable screen-left three-quarter/profile family, visibly opposite `090`. Nose tip, face plane, and pupils project to the image-left side; the far cheek and far eye become more occluded. The image-left shoulder leads, with ponytail and backpack overlap reversing naturally without mirroring the outfit.

## Continuity and motion budget

Each 22.5-degree step changes eye aim first, then head yaw or pitch, then a small shoulder and ponytail response. Keep the same foot baseline, lower-body center, head size, and overall sprite envelope. Adjacent steps should alter silhouette and occlusion by roughly equal amounts. The `157.5→180` and `337.5→000` boundaries must be one ordinary step, with no scale pop, recentering jump, ponytail flip, backpack detachment, or sudden change in expression.

## Prop constraints

The goggles are worn rigidly on the head and rotate only with the skull. The compact fuel backpack is fixed to the back and follows the torso as one rigid attachment; it may become partly hidden or reveal a side edge as Burnice turns, but it never floats, changes sides, or becomes a handheld weapon. Clothing straps, flame cuffs, skirt accents, and asymmetric leg details remain on their canonical sides throughout the loop.

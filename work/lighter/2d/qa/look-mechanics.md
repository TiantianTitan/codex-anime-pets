# Lighter look mechanics

## Natural motion

Lighter keeps both boots planted on one baseline and maintains the same lower-body registration throughout the full clock loop. His visible eye and eyelids lead the gaze behind the dark sunglasses; the brows and chin reinforce pitch. The head and neck follow with restrained yaw and pitch, then the shoulders and upper torso turn only enough to make the horizontal direction unmistakable. His red scarf and hair tips may lag by a very small, continuous amount.

Do not rotate, skew, stretch, or tilt the whole sprite. Preserve the skull, face, sunglasses, torso, hands, clothing, and body proportions. Every direction remains a compact full-body 2D anime chibi sticker at the approved neutral scale.

## Anchors and equipment

- Both boots, pelvis, and lower torso are the stable registration anchor.
- The large gold mechanical gauntlet remains attached to Lighter's anatomical right arm in every view. It follows the shoulder as a rigid worn mechanism; it never swaps sides, floats, scales independently, or becomes a second gauntlet.
- Jacket spikes, belt hardware, shin armor, and sunglasses stay attached and preserve their canonical construction.
- The long red scarf remains attached at the neck. Its tails may lag subtly opposite the head turn, but their movement must be gradual and remain inside the sprite envelope.
- Hair and scarf can reveal or occlude small features naturally as the head turns. No prop may stay pasted in a fully frontal relationship while the body yaws.

## Cardinal pose families

- `000 up`: broadly frontal. Both eye apertures remain readable behind the sunglasses; irises sit visibly high, upper eyelids open, chin lifts, and a little more neck/underside of the jaw shows. Shoulders remain nearly level and the gauntlet stays on the correct arm.
- `090 screen-right`: clear screen-right three-quarter/profile family. Nose tip, facial plane, pupils, and chin project to the image-right side of the head center. The image-right side of the face is leading; the far cheek/eye becomes more occluded. Torso follows slightly without moving the boots.
- `180 down`: broadly frontal. Irises sit low, upper eyelids lower, chin tucks toward the scarf, and the crown/bangs become more prominent. This must read as down rather than a generic closed-eye expression.
- `270 screen-left`: clear screen-left three-quarter/profile family, visibly opposite `090`. Nose tip, facial plane, pupils, and chin project to the image-left side of the head center. The image-left side of the face leads; the far cheek/eye becomes more occluded. Preserve the anatomical-right gauntlet instead of mirroring the character.

## Intermediate directions and motion budget

Each 22.5-degree step changes the eye position, eyelid shape, chin angle, head yaw/pitch, shoulder reveal, scarf lag, and gauntlet occlusion by roughly one even increment. The feet, baseline, lower-body center, head size, and overall visible height stay stable. No adjacent pair may flip the face, swap the gauntlet, jump in scale, recenter abruptly, or open from profile to frontal in one late step.

Row 9 advances continuously `000 -> 090 -> 180`. Row 10 begins one step after `157.5`, advances `180 -> 270 -> 000`, and finishes with `337.5` one restrained step before the approved `000`. The `157.5 -> 180` and `337.5 -> 000` boundaries must be as smooth as every in-row transition.

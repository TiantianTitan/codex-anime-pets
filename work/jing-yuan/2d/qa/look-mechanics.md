# Jing Yuan 2D look mechanics

## Natural motion

Jing Yuan is a compact humanoid with a separate head, visible physical eye, heavy asymmetric fringe, long layered hair, and attached red ribbons. Looking is led by the visible golden eye and eyelid, followed by a restrained head/neck turn or pitch, then a small upper-torso follow-through. The lower torso, hips, boots, baseline, scale, and body registration stay fixed. Long hair and the attached red ribbons follow continuously with a slight lag; they never flip sides, detach, or teleport.

This is a gaze/orientation loop, not a turntable. Never rotate, skew, tilt, or warp the whole sprite. Preserve the skull, facial proportions, calm expression, viewer-left eye-covering fringe, one visible golden eye, red crown-ribbon attachment, and black-white-oxblood-gold outfit.

## Eye and face construction

- Treat the visible golden eye as a physical anime eye inside a fixed face: iris/pupil, eyelids, brow, highlights, nose line, cheek plane, and chin respond together.
- Do not slide a loose pupil over an unchanged eye, paint a new second eye, replace the eye with a googly circle, or move the visible eye outside the facial aperture.
- The heavy fringe remains attached to the same anatomical side and continues to cover the hidden eye. As the head yaws, it may occlude more or less of the face naturally, but it may not jump to the opposite side.
- Horizontal direction is carried by the nose tip, chin, visible face plane, eye aperture, and upper-head yaw. Vertical direction is carried by iris/eyelid position, chin pitch, face-plane exposure, neck, and restrained upper-body pitch.

## Cardinal pose families

- `000` up: visible eye and eyelid aim upward; chin lifts; more lower face/neck is exposed; upper torso follows by a very small backward opening. Fringe, long hair, and ribbons follow without whole-sprite tilt. This must read as up, not neutral/front.
- `090` screen-right: nose tip, chin, visible eye aperture, and front face plane project unmistakably toward the image-right edge. The screen-left side of the hair/head becomes the farther side while more of the character's screen-right-facing cheek/profile reads. Fringe stays attached and the gold eye remains the same anatomical eye. This must not look front-facing.
- `180` down: visible eye/eyelid aim down; chin tucks; forehead/fringe occupies slightly more of the face; upper torso folds forward subtly while boots and baseline stay fixed. This must read as down, not closed-eye idle.
- `270` screen-left: nose tip, chin, visible eye aperture, and front face plane project unmistakably toward the image-left edge. The opposite cheek/hair side becomes more visible; the same gold eye may narrow or become partly occluded naturally but must not swap sides or disappear entirely. This must be the clear horizontal opposite of `090`.

## Intermediate directions and motion budget

- Row 9 order: `000`, `022.5`, `045`, `067.5`, `090`, `112.5`, `135`, `157.5`.
- Row 10 order: `180`, `202.5`, `225`, `247.5`, `270`, `292.5`, `315`, `337.5`.
- Each 22.5-degree step moves the eye, eyelid, nose/chin projection, head/neck, upper torso, hair, and ribbons by a similar visual amount. No adjacent step may introduce a large bend, scale pop, baseline jump, eye replacement, ribbon flip, or costume change.
- `157.5 → 180` and `337.5 → 000` must each be one natural final step across the row boundary. Row 10 begins exactly one step after row 9 and finishes exactly one step before row 9.
- Up-right, down-right, down-left, and up-left poses must combine both expected axes; they may not collapse to a pure cardinal or neutral pose.

## Registration and prop rules

- Feet, lower body, baseline, apparent body height, head size, and costume scale remain registered to the approved idle neutral frame.
- Hair tips and red ribbons may lag slightly around the arc but remain connected and inside the cell safe area.
- Jing Yuan stays unarmed and carries no fan, cup, chair, mascot, weapon, paper, scroll, magnifying glass, or new prop.
- No text, degree labels, arrows, clocks, guides, scenery, floor, shadow, glow, aura, motion marks, detached effects, or extra characters.

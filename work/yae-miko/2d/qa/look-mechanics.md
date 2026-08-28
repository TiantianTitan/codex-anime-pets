# Yae Miko look mechanics

## Natural motion

Yae Miko is a compact humanoid chibi. Her violet eyes lead each gaze change, followed by a restrained head-and-neck turn and a smaller upper-torso response. Keep the feet, hips, lower robe, scale, and baseline anchored. Preserve her sly, composed expression and facial proportions; do not stretch or warp the skull, eyes, mouth, hands, sleeves, or outfit.

Her long pink hair remains one coherent attached mass. The face-framing locks, gold crown ornaments, purple gemstone earrings, and wide sleeves may follow the head or upper body by a very small delayed amount, but they must never flip sides, detach, teleport, or become new props. Earrings remain suspended from their original attachment points. She holds no prop in the look loop.

## Eye and face behavior

- Move each complete eye construction together: violet iris, pupil, highlight, eyelids, lashes, and brow expression.
- Eyes lead first; the chin, nose, neck, shoulders, hair, earrings, and sleeves follow subtly.
- Do not add eye whites, replacement pupils, a second eye layer, or exaggerated googly-eye motion.
- Keep every gaze readable at normal `192x208` display size without changing identity.

## Cardinal pose families

- `000 up`: broadly frontal and centered. Raise both irises and slightly lift the chin; open the lower eyelid space just enough to read upward. The crown stays centered, hair falls naturally behind the shoulders, and the lower body remains fixed.
- `090 screen-right`: the pupils, nose tip, face plane, chin, and head turn unmistakably toward the screen-right edge. The screen-right cheek and nose edge advance while the opposite cheek becomes slightly occluded. The near earring and sleeve remain attached and become a little more visible; hair follows without flipping sides.
- `180 down`: broadly frontal and centered. Lower both irises, tuck the chin, and let the upper lids and fringe overlap the face slightly more. Keep the crown, torso, feet, and outfit registration stable.
- `270 screen-left`: the exact semantic opposite of `090`. The pupils, nose tip, face plane, chin, and head turn unmistakably toward the screen-left edge. The screen-left cheek and nose edge advance while the opposite cheek becomes slightly occluded. The near earring and sleeve remain attached and become a little more visible; hair follows without flipping sides.

## Interpolation and motion budget

Build one continuous clockwise family in even `22.5` degree steps. Every neighboring pair should move the eyes, head, shoulders, hair, earrings, and sleeve edges by roughly the same visual amount. Diagonals combine both required axes; no cell may lose the horizontal or vertical cue for its quadrant. Keep `157.5 -> 180`, `337.5 -> 000`, and the row boundary as smooth as every other transition.

Do not rotate, skew, tilt, or rescale the whole sprite. Do not shift the feet or lower robe laterally. Do not add arrows, labels, degree text, clocks, scenery, shadows, glow, aura, loose sakura petals, lightning, floating symbols, or any detached effect.

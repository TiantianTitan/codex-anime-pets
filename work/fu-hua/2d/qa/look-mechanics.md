# Fu Hua look mechanics

Fu Hua is a humanoid chibi with a rigid head, neck, glasses, and uniform. Looking motion must come from coordinated eyes, eyelids, eyebrows, head/neck turn, and a restrained upper-torso follow-through—not whole-sprite rotation, skew, or soft skull warping.

## Anchors and motion budget

- Keep both boots, the pelvis, and lower torso on one stable baseline and center anchor.
- Keep character height, head size, shoulder width, red glasses, uniform seams, and boot placement consistent across all sixteen cells.
- The cyan irises and eyelids lead each 22.5-degree step; the head and neck follow by an even amount, then the shoulders follow only slightly.
- The low side ponytail and long tunic panels may lag by one subtle step but must remain attached and must never jump sides.
- The glasses stay rigidly fitted to the face and turn with the head. They may become more foreshortened in profile but may not slide, detach, or change color.
- No single intermediate step may carry most of the turn or pitch. The transitions `157.5→180` and `337.5→000` must be as small and smooth as neighboring steps.

## Cardinal pose families

- `000 up`: near-frontal body; chin lifts, neck underside becomes slightly more visible, cyan irises sit high within the original eye apertures, and upper eyelids open. Glasses remain centered and symmetrical.
- `090 screen-right`: nose tip, mouth, chin, pupils, and facial plane project toward the image-right edge. The image-right profile opens while the far cheek and far glasses lens become more occluded; ponytail and tunic remain attached behind the turn.
- `180 down`: near-frontal body; chin tucks toward the high collar, cyan irises sit low, upper lids lower, and more crown/bangs are visible. Glasses follow the downward pitch without covering the eyes completely.
- `270 screen-left`: nose tip, mouth, chin, pupils, and facial plane project toward the image-left edge. The image-left profile opens while the far cheek and far glasses lens become more occluded; it must be visibly opposite `090` in screen coordinates.

## Intermediate directions

Interpolate the head yaw, iris position, eyelid shape, chin pitch, visible cheek, glasses foreshortening, shoulder turn, ponytail lag, and tunic-panel overlap evenly between adjacent cardinals. Diagonals must retain both axes. Near-vertical poses may be close to frontal, but a small correct horizontal cue must remain. Preserve Fu Hua's calm, disciplined expression and the canonical Accipiter outfit in every cell. No sword, prop, effect, text, guide mark, shadow, floor, or scenery.

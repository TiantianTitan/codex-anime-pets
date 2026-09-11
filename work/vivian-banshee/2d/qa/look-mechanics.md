# Vivian Banshee — Look Mechanics

## Natural motion

Vivian looks around with her eyes first, followed by a restrained head-and-neck turn and a very small upper-torso follow-through. Her feet, lower body, and the hand gripping the parasol shaft stay registered to one baseline. The parasol remains physically attached to the same grip and follows the body as a rigid worn/held prop; it may lag a little, but it must never teleport, detach, flip sides independently, or become a second floating component. Her long spiral curls and large bow follow the head with a small continuous delay while preserving their recognizable construction.

The gaze is carried by the complete face: red irises and pupils move inside the original eye apertures, eyelids and brows reshape subtly, the nose/chin plane follows, and the head turns or pitches naturally. Pupil-only motion, replacement eyes, skull stretching, whole-sprite rotation, raster warping, and independent per-cell restyling are not acceptable.

## Anchors and motion budget

- Keep one shared shoe baseline, lower-body center, torso scale, head size, and parasol grip point across all sixteen poses.
- Each 22.5-degree step changes the eyes, eyelids, chin, head yaw/pitch, shoulder line, curls, and parasol lag by one comparable visual increment.
- The face turn must be readable at 192×208 without exaggerating or deforming facial proportions.
- Keep the complete hair, skirt, heels, shaft, and parasol canopy inside the cell with practical padding.
- The parasol canopy may shift only enough to follow Vivian's restrained upper-body turn; its size and orientation progress continuously around the loop.
- `157.5 → 180` and `337.5 → 000` must be single ordinary steps with no scale pop, baseline jump, hair/bow flip, or parasol-side snap.

## Cardinal pose families

### 000 — up

Near-frontal pose. Both red eyes remain visible with irises high in their apertures, upper lids slightly opened, chin lifted, and a little more neck/underside-of-bangs visible. The torso stays upright and broad. The curls fall on both sides and the parasol stays attached behind/above her without changing sides.

### 090 — screen-right

Vivian turns her face and head unmistakably toward the image-right edge. The nose tip, chin plane, and pupils sit visibly to the image-right of the head center; the nearer cheek/eye opens while the far side becomes more occluded. The shoulders follow slightly. Hair, bow, shaft, and canopy keep their physical attachment and lag behind the turn rather than remaining front-facing.

### 180 — down

Near-frontal pose. The chin tucks toward the collar, red irises sit low, upper lids and fringe cover more of the eyes, and the crown/bangs become more prominent. The lower body and parasol grip remain fixed; no crouch, scale change, or back-facing turn.

### 270 — screen-left

Vivian turns her face and head unmistakably toward the image-left edge. The nose tip, chin plane, and pupils sit visibly to the image-left of the head center, with the opposite cheek/eye becoming occluded. The shoulders follow slightly. The curls, bow, shaft, and canopy progress continuously through the left-facing pose while staying attached and retaining their identity.

## Direction families

- `000 → 090`: lift gradually relaxes as the face turns through up-right into a clear right profile.
- `090 → 180`: the right-facing profile gradually bows and reopens toward a broad down-facing pose; retain a screen-right cue through `157.5`.
- `180 → 270`: the bowed front pose gradually yaws through down-left into a clear left profile.
- `270 → 000`: the left profile gradually lifts and reopens toward the near-frontal up pose; retain a screen-left cue through `337.5`.

No pose may show a back view, neutral idle expression, detached ornament, guide mark, shadow, glow, scenery, or chroma-colored panel in the final cell.

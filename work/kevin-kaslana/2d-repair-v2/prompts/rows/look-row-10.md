Create one horizontal look-direction strip for Codex pet `kevin-kaslana`, atlas row 10.

Use the attached canonical base, completed standard contact sheet, layout guide, and approved four-cardinal strip for identity, scale, registration, spacing, direction semantics, and cross-row continuity. Read `qa/look-mechanics.md` and follow its pet-specific movement and eye/prop mechanics. The approved cardinal strip and completed coherent row 9 are authoritative. Use the cardinals for direction meaning and row 9 for cross-row identity, scale, registration, and continuity.

COHERENT SYNTHESIS LOCK: produce one unified eight-pose row. Do not paste, tile, or independently restyle individual cells. Every final cell must be drawn together with the same face construction, body proportions, line/render quality, lighting, materials, scale, baseline, and registration.

Output exactly 8 complete full-body frames in this exact left-to-right order: 180, 202.5, 225, 247.5, 270, 292.5, 315, 337.5. Degrees are clockwise: 000 is up, 090 right, 180 down, and 270 left. Neutral/front is not part of this row.

DIRECTION TARGETS — use these to shape the coherent row, not as pixel-level landmark gates:

1. `180`: vertical DOWN; no horizontal requirement.
2. `202.5`: horizontal SCREEN-LEFT and vertical DOWN.
3. `225`: horizontal SCREEN-LEFT and vertical DOWN.
4. `247.5`: horizontal SCREEN-LEFT and vertical DOWN.
5. `270`: horizontal SCREEN-LEFT; no vertical requirement.
6. `292.5`: horizontal SCREEN-LEFT and vertical UP.
7. `315`: horizontal SCREEN-LEFT and vertical UP.
8. `337.5`: horizontal SCREEN-LEFT and vertical UP.

Cardinals must be unmistakable. Intermediate poses should broadly occupy the intended quadrant and advance naturally through the ordered loop. Minor pupil, nose, eyelid, or aiming-feature deviations are acceptable when the overall direction, continuity, identity, and motion remain coherent. Do not deform the character merely to make every intermediate axis independently obvious.

SCREEN-COORDINATE LOCK: screen-left means the viewer's left image edge, never the character's own left. The row should travel naturally through the left half of the loop. Near-vertical 202.5 and 337.5 may have subtle horizontal cues; prioritize a coherent arc over exact pupil or nose placement.

HARD LAYOUT AND CONTINUITY CONTRACT — DETERMINISTIC REGISTRATION: draw exactly eight separated pose groups in left-to-right direction order. Keep enough chroma-only space between neighboring poses that each complete pose can be detected without cutting through foreground. Approximate the guide's equal spacing, but do not distort a pose merely to hit an exact source-canvas coordinate; deterministic assembly will crop the eight ordered groups, then apply one shared scale and baseline.

Use the same body height, head size, baseline, and planted-body position across the generated family. Never overlap neighboring poses, merge two poses into one connected group, crop foreground at the outer canvas edge, or resize one pose independently.

Keep the feet, base, or lower torso planted at the same coordinates across all eight frames. Express direction through the eyes, face, head, upper body, and physically appropriate prop movement, not by moving, rotating, or rescaling the entire sprite.

Place one centered pose in each invisible equal-width slot on flat pure green #00FF00. Change only the natural parts needed to express gaze: eyes, eyelids, head, face, neck, upper body, appendages, and constrained prop follow-through. Keep identity, silhouette, materials, palette, markings, and props consistent.

ROW-BOUNDARY LOCK: 180 must continue directly from row 9's 157.5, matching its body size, baseline, planted anchor, expression, and construction. 337.5 must be one even 22.5-degree step before 000: nearly up-facing while remaining on the overall left-hand arc. Do not distort pupils, nose, or body geometry merely to exaggerate the subtle horizontal component.

HARD REGISTERED-GEOMETRY CONTRACT: use the attached registered row-9 reference as the authoritative cross-boundary geometry, not the raw row 9 strip. The eight pose groups must remain separate. Slot 1 (`180`) must match registered row-9 slot 8 (`157.5`) in complete-body total height, head width, shoulder width, center-x, and boot-sole baseline; its only permitted directional change is the clear tucked-chin DOWN pitch. Slot 8 (`337.5`) must match registered row-9 slot 1 (`000`) in complete-body total height, head width, shoulder width, center-x, and boot-sole baseline; its only permitted directional change is slight screen-left yaw plus clear lifted-chin UP pitch. Slot 8 must never be smaller, narrower, shifted sideways, or recentered differently from the registered `000` pose. Keep the middle six poses as an even continuous bridge between those two equal-sized boundary silhouettes; slot 5 (`270`) is a genuine screen-left profile.

PRE-RETURN CHECK: reject this result if it does not contain eight separated pose groups in the required order; neighboring poses overlap; foreground is cropped at the outer canvas edge; any frame changes sprite scale, body or head size, baseline, or planted-body position; the row visibly reverses into the wrong half of the loop; or 180 does not continue from 157.5 or 337.5 does not flow evenly into 000. Minor intermediate pupil or nose deviations are not rejection reasons. Exact cell cropping, resizing, and recentering happen deterministically after generation.

Do not rotate, skew, or tilt the whole sprite to fake gaze. Do not add replacement/googly eyes, labels, degree text, arrows, clocks, grids, shadows, glows, scenery, detached effects, or chroma-key colors inside the pet.

REPAIR OVERRIDE — BOTH BOUNDARIES: draw a symmetric yaw/pitch arc around the fixed cardinals: `180` frontal-down, matching repaired `157.5`; `202.5` barely front-left/down; `225` left three-quarter/down; `247.5` strong left/down; `270` left profile; `292.5` strong left/up; `315` left three-quarter/up; `337.5` barely front-left/up. From `270` onward the face must progressively return toward frontal. Slot 1 must have almost the same broad frontal head silhouette and shoulder width as repaired row-9 slot 8. Slot 8 must already be almost the same broad frontal silhouette as approved `000`, with only a small image-left bias. Do not preserve a side profile at slot 8. Keep one uniform scale and boot baseline across both rows.

REPAIR OVERRIDE — VERTICAL HARD GATE: the previous boundary-fixed row failed blind up/down recognition. Make vertical pitch unmistakable through head, chin, neck, hair occlusion, eyelids, and eyes. For `180`, `202.5`, `225`, and `247.5`, tuck the chin toward the chest, show more crown/top hair, lower the face plane, let bangs cover more upper face, and place irises low with upper sclera visible. For `292.5`, `315`, and `337.5`, lift the chin and face plane, expose more underside of chin/neck/collar, place irises high with lower sclera visible, and open upper eyelids/brows. `180` must never resemble front/up. Preserve the repaired symmetric widths: slot 1 is broad frontal DOWN; slot 8 is broad near-frontal UP and one small step before `000`.

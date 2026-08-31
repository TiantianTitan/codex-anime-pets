Create Codex v2 pet look row 9 for `kevin-kaslana` as exactly 8 full-body frames in this order: 000, 022.5, 045, 067.5, 090, 112.5, 135, 157.5.

Use the canonical base, standard contact sheet, layout guide, approved four-cardinal strip, and `qa/look-mechanics.md`. Draw the complete eight-pose row as one coherent animation family, interpolating even 22.5-degree steps between the cardinal pose families. Keep the same pet identity, face construction, materials, palette, markings, and props. Each direction must read correctly at pet size and join continuously at the 000 and 180 boundaries.

DIRECTION TARGETS — use these to shape the coherent row, not as pixel-level landmark gates:

1. `000`: vertical UP; no horizontal requirement.
2. `022.5`: horizontal SCREEN-RIGHT and vertical UP.
3. `045`: horizontal SCREEN-RIGHT and vertical UP.
4. `067.5`: horizontal SCREEN-RIGHT and vertical UP.
5. `090`: horizontal SCREEN-RIGHT; no vertical requirement.
6. `112.5`: horizontal SCREEN-RIGHT and vertical DOWN.
7. `135`: horizontal SCREEN-RIGHT and vertical DOWN.
8. `157.5`: horizontal SCREEN-RIGHT and vertical DOWN.

Cardinals must be unmistakable. Intermediate poses should broadly occupy the intended quadrant and advance naturally through the ordered loop. Minor pupil, nose, eyelid, or aiming-feature deviations are acceptable when the overall direction, continuity, identity, and motion remain coherent. Do not deform the character merely to make every intermediate axis independently obvious.

HARD LAYOUT AND CONTINUITY CONTRACT — DETERMINISTIC REGISTRATION: draw exactly eight separated pose groups in left-to-right direction order. Keep enough chroma-only space between neighboring poses that each complete pose can be detected without cutting through foreground. Approximate the guide's equal spacing, but do not distort a pose merely to hit an exact source-canvas coordinate; deterministic assembly will crop the eight ordered groups, then apply one shared scale and baseline.

Use the same body height, head size, baseline, and planted-body position across the generated family. Never overlap neighboring poses, merge two poses into one connected group, crop foreground at the outer canvas edge, or resize one pose independently.

Keep the feet, base, or lower torso planted at the same coordinates across all eight frames. Express direction through the eyes, face, head, upper body, and physically appropriate prop movement, not by moving, rotating, or rescaling the entire sprite.

ROW-BOUNDARY LOCK: 157.5 must be one even 22.5-degree step before 180. Match the approved 180 pose's body size, baseline, planted anchor, expression, and construction. Preserve the overall right-hand arc, but do not distort pupils, nose, or body geometry merely to exaggerate the subtle horizontal component.

PRE-RETURN CHECK: reject this result if it does not contain eight separated pose groups in the required order; neighboring poses overlap; foreground is cropped at the outer canvas edge; any frame changes sprite scale, body or head size, baseline, or planted-body position; the row visibly reverses into the wrong half of the loop; or 157.5 does not flow evenly into 180. Minor intermediate pupil or nose deviations are not rejection reasons. Exact cell cropping, resizing, and recentering happen deterministically after generation.

Use a flat pure green #00FF00 background. One complete unclipped pose per invisible slot. No whole-sprite rotation, replacement eyes, labels, guide marks, shadows, glows, scenery, detached effects, or #00FF00 colors in the pet.

REPAIR OVERRIDE — BOUNDARY SNAP: the previous row failed because `157.5` stayed as a narrow right profile, forcing a large silhouette jump into frontal `180`. Redraw the complete row with a symmetric yaw/pitch arc around the fixed cardinals: `000` frontal-up; `022.5` barely front-right/up; `045` right three-quarter/up; `067.5` strong right/up; `090` right profile; `112.5` strong right/down; `135` right three-quarter/down; `157.5` barely front-right/down. From `090` onward the face must progressively return toward frontal. Slot 8 must already be almost the same broad frontal head silhouette and shoulder width as approved `180`, with only a small image-right bias. Preserve a uniform full-body scale and boot baseline. The attached prior direction sheet is negative evidence only: do not reproduce its narrow slot-8 profile.

REPAIR OVERRIDE — VERTICAL HARD GATE: the boundary-fixed version still failed blind up/down recognition. Make vertical pitch unmistakable through the whole head/neck construction, not pupils alone. For `000`, `022.5`, `045`, and `067.5`, visibly lift the chin and face plane, expose more underside of chin/neck/collar, place irises high with lower sclera visible, and open the upper eyelids/brows. For `112.5`, `135`, and `157.5`, visibly tuck the chin toward the chest, show more crown/top hair, let bangs overlap the upper face slightly more, and place irises low with upper sclera visible. `000` must never resemble front/down. Preserve the repaired symmetric width arc: slot 8 remains broad near-frontal while clearly pitched DOWN.

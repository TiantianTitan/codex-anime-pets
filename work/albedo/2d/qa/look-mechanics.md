# Albedo: gaze mechanics

Grounded humanoid, not a turntable. Keep both boots, hips, lower coat and gold chest strap registered. The original turquoise anime eyes lead with redrawn eyelids, iris placement and brows; a small neck/head yaw and pitch follows. Facial feature spacing and skull volume stay constant; no replacement eyes, pupil stickers, raster warps or whole-body tilts.

Natural face aim in viewer/screen coordinates:

- 000 up: chin lifts, slightly more neck exposed, both pupils visibly toward upper lids and brows subtly raised; NOT front-neutral. Head remains centered.
- 090 right: head turns to screen-right by roughly 30 degrees, nose-tip clearly right of head center, both irises look to the right. Far-side eye naturally narrower; no mirrored hair/ornaments. Upper torso follows only slightly.
- 180 down: chin tucks and crown/forelock become more visible; both visible turquoise eyes look below, not forward or closed. Lower-body remains upright and planted.
- 270 left: opposite head yaw, nose-tip clearly left of head center and both irises toward screen-left. Far eye narrows on the opposite side. Anatomical-left gold chest/arm hardware stays on its correct body side.

The tuft and braided half-up hair move with the skull, loose hair tips follow gently. Hood/chest/arms are body-attached; no props appear. Hands stay relaxed. Do not make a 90-degree head profile, turn the entire body, or hold the face neutral while changing only pupil dots.

Each 22.5-degree step interpolates both axes evenly. Horizontal yaw follows the sine of the attention angle, vertical pitch follows its cosine. This is guidance to drawn anatomy, not permission for a procedural transform. Modest approximately 5–10-degree yaw differences between neighboring near-vertical poses; small pitch increments between horizontal neighbors. All poses retain the same head height/volume, planted boot anchor and natural expression.

Row 9: up → progressively up-right → right → progressively down-right. Row 10: down → progressively down-left → left → progressively up-left. The lower-right end of row 9 must meet down in row 10 smoothly; the final near-up-left must meet up in row 9. Both axes of diagonals should remain readable; near-cardinal deviations can be subtle but never reverse into the opposite quadrant.

Canonical and approved standard sheet remain authoritative for identity and scale. Four anchors must pass before row 9; row 9 must pass registered native-size review before row 10. Each final row is one coherent generated strip, not patched cells.

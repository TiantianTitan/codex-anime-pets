# Zhu Yuan look row 10 — layout-guide locked synthesis

Generate one complete coherent eight-pose row. Treat the supplied 8-slot layout guide as the highest-priority geometry reference: one complete figure per slot, fully inside each blue safe box with visible padding. The guide is construction-only; the output must not contain any boxes, lines, crosses, labels, borders, or guide colors.

## Geometry

- Exactly 8 complete separated full-body sprites, one per guide slot, in the same left-to-right order.
- Keep every crown/ponytail, shoe, sidearm, and limb inside the guide's blue safe box; leave visible background between silhouette and all safe-box sides.
- Match raw row 9's practical body size and baseline, not the larger four-pose guide scale.
- Maintain one shared shoe baseline and one uniform scale across all eight.

## Motion from the pose guides

- Poses 1–4 follow the centered first-four guide: `180` deep frontal/down with ponytail centered/occluded behind crown; `202.5` slight down-left with ponytail center-right; `225` clear down-left and `247.5` near-profile down-left with ponytail image-right/rear.
- Poses 5–8 follow the last-four guide: unmistakable IMAGE-LEFT `270`, followed by distinct `292.5`, `315`, and `337.5` up-left steps reopening smoothly toward approved 000.
- Preserve gradual ponytail motion; no side teleport, no image-right reversal.
- Preserve Zhu Yuan's canonical face, orange-red streak, high ponytail/red tie, uniform, armor, holster, sidearm, proportions, clean outlines, cel shading, and character-side asymmetry.

## Output contract

- Perfectly flat uniform `#00FF00` horizontal strip only.
- No text, labels, guide marks, boxes, borders, shadows, particles, detached effects, extra props, scenery, overlap, or clipping.

Reject if the guide appears in the output; if any silhouette touches/crosses a safe box; if any neighboring figures lack clean green separation; if pose 1's ponytail is not centered behind the crown; if poses 2–4 point image-right; if 270 is ambiguous; or if poses 6–8 reverse.

All directions use literal viewer/screen coordinates. Draw all eight poses together as a single new generation; never patch a cell.

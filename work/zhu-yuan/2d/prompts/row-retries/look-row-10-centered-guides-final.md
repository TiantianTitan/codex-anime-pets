# Zhu Yuan look row 10 — centered-boundary final synthesis

Generate one new coherent eight-pose row. Three visual inputs have separate authoritative roles:

- The centered first-four guide controls poses 1–4 and their ponytail motion.
- The approved last-four guide controls poses 5–8 and their left/up-left reopening.
- The midpoint full-row candidate controls only uniform silhouette size, vertical occupancy, spacing, and baseline. Ignore its first-pose ponytail jump and redraw the motion from the guides.

## Pose sequence

`180, 202.5, 225, 247.5, 270, 292.5, 315, 337.5`

## Required motion

- Poses 1–4 exactly follow the centered first-four guide: deep frontal/down with ponytail centered/partly occluded behind the crown; then slight down-left with ponytail center-right; then clear down-left and near-profile down-left with ponytail image-right/rear.
- Poses 5–8 exactly follow the approved last-four guide: unmistakable image-left 270, then distinct 292.5/315/337.5 up-left steps reopening gradually toward approved 000.
- Pose 4→5 is one ordinary continuation in the same image-left family.
- Preserve Zhu Yuan's canonical face, orange-red streak, high ponytail/red tie, uniform, armor, holster, sidearm, proportions, clean outlines, cel shading, and character-side asymmetry.

## Exact scale reference

- Match the supplied midpoint full-row candidate's figure height, body scale, source-canvas vertical occupancy, inter-pose spacing, outer margins, and shared shoe baseline.
- Do not match its early hairstyle motion. Use it only as a geometric size/layout reference.
- All eight figures must be the same practical scale and leave safe uninterrupted green above every crown and below every shoe.

## Output contract

- Exactly 8 complete separated full-body sprites in one horizontal strip.
- Perfectly flat uniform `#00FF00` background only.
- No text, labels, guides, boxes, shadows, particles, detached effects, extra props, scenery, overlap, or cropping.

Reject if the pose-1 ponytail is strongly on either side instead of centered behind the crown; if it jumps between poses 1–2; if poses 2–4 point image-right; if 270 is ambiguous; if poses 6–8 reverse; or if the size differs from the midpoint reference.

All directions use literal viewer/screen coordinates. Draw all eight poses together as a single coherent generation; never patch or paste one cell.

# Zhu Yuan look row 10 — bracketed intermediate-size redraw

Generate a new coherent 8-pose row using two supplied versions of the same approved motion as a strict visual size bracket:

- The `too-large` strip has correct direction, identity, 157.5→180 hairstyle continuity, and ponytail crossover, but its later crowns touch the registered cell top.
- The `too-small` strip has the same correct direction and continuity, but its normalized silhouettes are visibly smaller than row 9.

Redraw the entire row at a uniform silhouette size **exactly midway between those two references**. Do not crop, resize, trace, paste, or edit either input image.

## Preserve

- Exactly 8 complete separated full-body poses in order: `180, 202.5, 225, 247.5, 270, 292.5, 315, 337.5`.
- Slot 1 is deep frontal/down with the high ponytail and red tie on the same image-left/rear side as row-9 157.5 and the approved 180 anchor.
- Slots 2–3 move the ponytail gradually behind the crown while the face turns down-left.
- Slots 2–4 progress IMAGE-LEFT/down-left; slot 5 is unmistakably IMAGE-LEFT; slots 6–8 remain up-left and reopen toward approved 000.
- Canonical Zhu Yuan identity, face, orange-red front streak, high ponytail, uniform, armor, holster, sidearm, proportions, line quality, cel shading, and character-side asymmetry.
- One shared shoe baseline and consistent scale across all eight figures.

## Midpoint size gate

- Every complete silhouette must be visibly larger than the `too-small` reference and visibly smaller than the `too-large` reference.
- Target approximately 90–92% of the `too-large` silhouette height, or 110–113% of the `too-small` silhouette height.
- Keep a clear green safety band above every ponytail tip and enough green below every shoe; do not let any pose approach an outer edge.
- Preserve natural full-body proportions; do not squash or stretch anatomy.

## Output and rejection gates

- Perfectly flat uniform `#00FF00` background; generous outer/inter-pose gutters.
- Reject any image-right reversal in slots 2–4 or 6–8, any ambiguous 270, or any ponytail-side teleport at 157.5→180/180→202.5/202.5→225.
- Reject if the row matches either extreme size instead of their midpoint, if one pose differs in scale/baseline, or if any body is cropped/overlapped.
- No text, labels, guides, shadows, particles, detached effects, extra props, or scenery.

All directions use literal viewer/screen coordinates. Draw all eight poses together as one new row; never patch a single cell.

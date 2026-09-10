# Zhu Yuan look row 10 — scale-only coherent redraw

Regenerate the complete 8-pose strip as one coherent image. The supplied `decoded/look-row-10.png` is the authoritative direction and ponytail sequence; preserve that sequence. Do not crop, resize, paste, or edit the supplied pixels—redraw the entire strip cleanly.

## Preserve exactly

- Exactly 8 complete separated full-body sprites.
- Slots 1–8 remain `180, 202.5, 225, 247.5, 270, 292.5, 315, 337.5`.
- Slots 2–4 already belong to the IMAGE-LEFT family: nose and facial plane move progressively toward image-left while the ponytail trails behind on image-right.
- Slot 5 is an unmistakable image-left profile; slots 6–8 continue left/up-left and reopen toward approved 000 without reversing.
- Keep Zhu Yuan's identity, face, orange-red hair streak, high ponytail, uniform, armor, holster, sidearm, proportions, shading, line quality, and character-side asymmetry.
- One shared shoe baseline; no whole-body rotation, detached effects, text, labels, guides, shadows, or props not already attached to the character.

## Change only the source-row scale and vertical placement

- Redraw every figure uniformly about 10–12% smaller than the supplied row while preserving body proportions; do not squash or shorten the character anatomically.
- Output canvas remains a wide horizontal strip on perfectly flat uniform `#00FF00`.
- Place all shoe soles around source-canvas y=615–620.
- Place every highest crown/ponytail pixel around source-canvas y=175–190.
- Therefore each complete crown-to-sole sprite should be about 425–445 px tall.
- Keep the eight figures the same size as one another, with ample green between groups and at both outer edges.

## Reject if

- any of slots 2–4 points image-right or flips only at slot 5;
- the ponytail jumps sides between slots 4 and 5;
- slot 5 is not screen-left or slots 6–8 reverse toward screen-right;
- any sprite exceeds 445 px crown-to-sole, begins above y=170, ends below y=620, or has a different baseline;
- the figure is compressed, cropped, overlapped, restyled, or loses identity/asymmetry.

Screen/image directions are literal viewer coordinates. IMAGE-LEFT means the left edge of the output canvas.

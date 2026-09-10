# Zhu Yuan look row 9 — boundary handoff to approved row 10

Regenerate the complete eight-pose row 9 as one coherent family. Preserve the currently approved 000→157.5 gaze sequence, identity, scale, and baseline. Change only the ponytail follow-through in the final three poses so the row hands off continuously to the supplied row-10 180 pose.

## Output contract

- Exactly 8 complete separated full-body Zhu Yuan sprites in order: `000, 022.5, 045, 067.5, 090, 112.5, 135, 157.5`.
- Perfectly flat uniform `#00FF00`; one pose per layout slot, fully inside the blue safe boxes with visible padding. Never copy guide lines, boxes, crosses, labels, or colors into output.
- Match the approved row-9 source scale, body registration, shoe baseline, identity, face, orange-red streak, high ponytail/red tie, uniform, armor, holster, sidearm, proportions, outlines, and cel shading.
- No shadows, particles, detached effects, extra props, text, scenery, overlap, or cropping.

## Gaze sequence

- 000 up: frontal/up, high irises and lifted chin.
- 022.5→067.5: even up-right progression.
- 090: unmistakable IMAGE-RIGHT profile.
- 112.5: down-right profile beginning to lower.
- 135: clear down-right three-quarter.
- 157.5: near-frontal/down with a subtle image-right bias, exactly one step before 180.

## Repaired ponytail handoff

- Keep normal high-ponytail follow-through through 090.
- At 112.5, ponytail remains mostly IMAGE-LEFT/rear, as expected behind the right-facing head.
- At 135, as the face returns toward frontal/down, the ponytail moves inward behind the crown toward center; it must not remain fully spread on image-left.
- At 157.5, the ponytail gathers behind/crosses the crown toward center-right so it is visibly compatible with the supplied row-10 180 pose. The red tie follows continuously with the same physical ponytail.
- This is a gradual `image-left/rear → left-center/behind crown → center/right-behind crown` progression, not a mirrored design swap.

## Hard gates

- Preserve 000 up and 090 image-right cardinals exactly; 112.5–157.5 must remain down-right and must not point left.
- Reject if 157.5 remains strongly side-profile rather than one step before frontal/down 180.
- Reject if ponytail/red tie teleports sides, or if 157.5 cannot flow naturally into the supplied row-10 180 at normal size.
- Reject any scale, baseline, safe-padding, group-separation, identity, equipment, or background failure.

All directions are literal viewer/screen coordinates. Draw all eight poses together; never replace one cell independently.

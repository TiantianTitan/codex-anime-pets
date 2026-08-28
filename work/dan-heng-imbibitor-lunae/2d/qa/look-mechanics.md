# Look mechanics — Dan Heng · Imbibitor Lunae

## Natural mechanism

Use a coherent head-and-upper-body rotation. The face plane, nose tip, pupils, eyes, pointed ears, antlers, front fringe, long rear hair, shoulders, garment opening, and attached aqua tail/ribbon must agree on one direction. Keep the lower body and feet registered and nearly frontal so gaze is not faked by translating or tilting the whole sprite.

## Cardinal anchors

- `000 up`: broadly frontal head with chin and eye line lifted toward the top edge; more lower facial plane is visible. Antlers and ears foreshorten coherently upward.
- `090 screen-right`: nose tip, visible face plane, pupils, chin, and fringe projection clearly aim toward the viewer's right edge. The near/far ear and antler overlap must support the same turn.
- `180 down`: broadly frontal head with chin tucked, pupils and face plane aimed toward the bottom edge; upper fringe covers slightly more forehead/eye area.
- `270 screen-left`: exact inverse screen-side intent of `090`; nose tip, face plane, pupils, chin, fringe, ears, and antlers aim toward the viewer's left edge.

## Intermediate directions

Rows 9 and 10 are one clockwise 16-step loop at 22.5-degree increments. Each frame must visibly interpolate between its neighboring cardinals without quadrant reversals. Screen-left/right always mean viewer coordinates.

## Registration and exclusions

- Maintain a consistent apparent scale, foot baseline, cell center, palette, costume construction, and attached aqua accent.
- Do not rotate or skew the complete sprite as a flat object.
- Do not use arrows, labels, replacement eyes, detached particles, shadows, floor, scenery, or guide marks.
- Preserve the short outfit with pale leg gaps and ankle boots in every direction.


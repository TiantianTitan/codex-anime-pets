# Tartaglia look mechanics

## Natural motion

Tartaglia is a compact humanoid chibi, so his gaze is led by the blue eyes and eyelids, followed by a restrained head-and-neck turn and a small upper-torso response. His skull, face, costume and hands remain rigid in proportion; the look loop must never be faked by rotating, skewing or warping the whole sprite.

His boots, pelvis and lower torso remain planted on one shared baseline. The grey-white uniform, belt and Hydro Vision stay registered to the body. The deep crimson scarf is attached behind the shoulders and may lag the upper torso by one subtle step, but it must remain compact and connected. The red hair ornament, earring and asymmetric shoulder construction retain their canonical sides through every turn. No water weapons, water ribbons, glow or detached effects are introduced.

## Cardinal pose families

- `000 up`: broad near-front pose; both eyes remain visible, irises sit high inside their original apertures, upper eyelids open slightly, chin lifts, neck and the underside of the jaw become more visible, and the upper torso follows only slightly.
- `090 screen-right`: unmistakable right-facing yaw in viewer coordinates; the nose tip, facial plane and pupils project toward the image-right side of the head, the near cheek/eye dominates, the far cheek/eye narrows naturally, and the shoulder/scarf overlap follows the right turn without flipping costume sides.
- `180 down`: broad near-front pose; both eyes remain readable with irises low, eyelids lower, chin tucks toward the collar, the crown and fringe become more visible, and the neck opening becomes less visible.
- `270 screen-left`: unmistakable left-facing yaw in viewer coordinates; the nose tip, facial plane and pupils project toward the image-left side of the head, the near cheek/eye dominates, the far cheek/eye narrows naturally, and the silhouette is visibly opposite to `090` while preserving the asymmetric outfit.

## Intermediate motion and budget

The 16 poses form one clockwise family. Each 22.5-degree step advances the eyes, eyelids, head yaw/pitch, cheek visibility, collar overlap and scarf follow-through by roughly the same visual amount. At final `192x208` size, neighboring steps should produce only a small feature shift and restrained silhouette change; head height, body height and shoulder width must not pop, and the feet/base must not slide.

Row 9 travels `000 → 090 → 180`; row 10 continues `180 → 270 → 000`. The `157.5 → 180` and `337.5 → 000` boundaries must each look like one ordinary step. `000` is a deliberate upward gaze, not the neutral/idle frame.


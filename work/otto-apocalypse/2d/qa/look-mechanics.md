# Otto Apocalypse look mechanics

## Natural motion

Otto is a humanoid sticker pet with large physical anime eyes, a separate head and neck, a tied side ponytail, a rigid shoulder capelet, and long attached coat tails. His gaze should begin in the green eyes, with the eyelids and brows participating, then continue through a restrained head-and-neck turn or pitch and a very small upper-torso follow. His boots, pelvis, lower torso, apparent body scale, and baseline stay anchored.

The eyes must be redrawn as the original complete eye construction for every pose: sclera, green iris, pupil, lids, lashes, rim, and highlights move together inside the face. Do not slide detached pupils over a fixed eye white, add replacement eyes, or stretch the face.

## Hair and costume constraints

- The pale-gold side ponytail stays physically tied to the same side/back anchor on Otto's head. Its tied base follows the skull rigidly; the loose tail lags only slightly and never flips sides or detaches.
- The shoulder capelet, lapels, gold piping, small emblem, cravat, gloves, and long coat tails remain part of the same asymmetric outfit. They turn and occlude naturally with the torso instead of mirroring or changing handedness.
- The coat tails may follow the upper body by a few pixels, but the lower silhouette remains registered and never becomes a separate component.
- No book, papers, chair, flower, weapon, text, symbols, scenery, shadow, glow, or detached effects appear in look poses.

## Cardinal pose families

- `000 up`: broadly frontal. Both eyes look toward the top edge, pupils sit high, upper lids open slightly, chin lifts, and the underside of the jaw/collar becomes a little more visible. The torso stays upright.
- `090 screen-right`: the nose tip, pupils, chin, and facial plane project toward image-right. The far side of the face and capelet becomes more occluded; the tied ponytail remains attached and trails naturally behind the turn toward image-left.
- `180 down`: broadly frontal. Both eyes look toward the bottom edge, pupils sit low, lids lower, chin tucks, and more crown/fringe becomes visible without hiding the identity.
- `270 screen-left`: the nose tip, pupils, chin, and facial plane project toward image-left. The opposite side of the face and capelet becomes more occluded; the tied ponytail stays attached and reads behind the head toward image-right.

## Motion budget and continuity

Each 22.5° step changes the eyes, eyelids, head turn/pitch, and slight upper-torso follow by roughly the same visible amount. The loop advances clockwise without backtracking: `000 → 090 → 180 → 270 → 000`. `157.5` is one down-right step before `180`; `337.5` is one up-left step before `000`. Do not rotate, skew, stretch, recenter, or scale the whole sprite to fake gaze. Keep facial proportions, head size, ponytail attachment, coat construction, foot placement, and body registration continuous across both rows.

# Kevin Kaslana look mechanics

## Natural motion

Kevin is a compact humanoid pet with a distinct head, neck, shoulders, long coat, and no held prop. His gaze begins in the icy-blue eyes, continues through a restrained head turn or pitch, and finishes with a very small neck and upper-torso follow-through. The lower torso, hips, boots, shared baseline, body scale, and overall center stay anchored. Hair tips and the coat collar may lag by a small amount, but the coat tails and arms do not jump, flip sides, or swing independently.

Preserve Kevin's reserved expression, facial proportions, white fringe, original eye construction, and black-white-gold-cyan costume. The asymmetrical armored sleeve and shoulder remain on the same physical side of his body throughout the loop; never mirror the costume to manufacture a direction. There is no weapon or other prop.

## Cardinal pose families

- `000 up`: the pupils and irises sit visibly high inside the original eye apertures, lower sclera is more visible, eyelids and brows open upward, and the chin lifts slightly. The face remains centered; the neck extends subtly and the upper chest follows without leaning the whole sprite. Both costume sides remain visible.
- `090 screen-right`: the nose tip, pupils, exposed cheek, and face opening move to the IMAGE-RIGHT of the head center. The rear skull, ear region, and trailing hair mass remain toward IMAGE-LEFT. The head turns right with a small neck/upper-chest follow-through; the far side of the face becomes partly occluded. The asymmetric armor stays attached to its physical body side rather than swapping across the image.
- `180 down`: the pupils and irises sit visibly low inside the eye apertures, more upper sclera shows, the brows and upper lids angle downward, and the chin tucks toward the chest. The bangs overlap the forehead/eyes slightly more and the upper back rounds only a little. The boots and lower body remain fixed.
- `270 screen-left`: the nose tip, pupils, exposed cheek, and face opening move to the IMAGE-LEFT of the head center. The rear skull, ear region, and trailing hair mass remain toward IMAGE-RIGHT. The head turns left with a small neck/upper-chest follow-through; the far side of the face becomes partly occluded. Costume asymmetry remains physical and does not mirror.

## Interpolation and motion budget

Each 22.5-degree step changes the eyes first, then the head/neck, then the upper torso by roughly the same visual amount. Diagonals combine both axes: high eyes plus the appropriate left/right face turn for up-diagonals, and low eyes plus that turn for down-diagonals. Head size, hair volume, shoulder width, coat length, boot baseline, and body center remain stable. Neighboring poses must not snap, reverse, recenter, swap costume sides, or change expression.

The clockwise loop is continuous across both row boundaries: `157.5 -> 180` completes the down-right family into down, while `337.5 -> 000` completes the up-left family into up. `000` is a true upward gaze, not Kevin's neutral front pose.

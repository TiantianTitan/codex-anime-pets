# Aventurine look mechanics

## Identity lock

- Keep the approved compact 2D chibi construction, sandy-blond layered hair, magenta-to-cyan gradient eyes, teal teardrop earring, white fur collar, teal/black/gold coat, white trousers, gloves, bracelet, shoes, waist ornaments, and attached blue tassels.
- Preserve the physical side of every asymmetric detail. The single earring, bracelet, coat panels, waist ornament, and tassels may become partly occluded as the head turns, but they must never jump to the opposite side.
- Do not introduce cards, chips, dice, sparkles, text, glasses, scenery, UI, or any detached effect.

## Gaze mechanism

- Aventurine is a humanoid character: the irises and pupils lead, eyelids reinforce the gaze, the head and neck follow, and only the upper torso may add a very small supporting turn.
- Feet, legs, pelvis, body scale, and ground baseline remain fixed through all sixteen directions. This is a look loop, not a body-turn or locomotion loop.
- Keep both eyes readable in near-front intermediates. A true side cardinal may narrow or partly occlude the far eye, but the nose, chin, pupil placement, hair overlap, and visible ear must all agree on the same screen direction.
- Hair tips, the teal earring, coat tails, and attached tassels may lag by only a few pixels. They must stay attached and cannot become direction arrows or floating motion marks.

## Cardinal anchors

- `000` up: broad near-front pose, pupils and irises high, eyes slightly more open, chin lifted enough to show a little more neck and fur-collar underside. Do not move the body upward.
- `090` screen-right: nose tip, chin projection, pupils, and face plane clearly cross toward the image-right side of the head. Hair overlap and ear visibility must support that direction.
- `180` down: broad near-front pose, pupils and irises low, upper lids slightly lowered, chin tucked so the bangs and crown read more strongly. Do not crouch or lower the whole body.
- `270` screen-left: nose tip, chin projection, pupils, and face plane clearly cross toward the image-left side of the head and visibly oppose `090`.

## Interpolation and continuity

- Interpolate clockwise in even 22.5-degree steps: `000, 022.5, 045, 067.5, 090, 112.5, 135, 157.5, 180, 202.5, 225, 247.5, 270, 292.5, 315, 337.5`, then return smoothly to `000`.
- Vertical gaze is strongest near `000` and `180`; horizontal turn is strongest at `090` and `270`. Intermediate frames blend the two cues without reversing early or flattening into repeated front views.
- Row 9 must end at a broad near-front, slight-screen-right downward gaze (`157.5`) that leads naturally into row 10's `180` down anchor.
- Row 10 must end at a broad near-front, slight-screen-left upward gaze (`337.5`) that leads naturally back into row 9's `000` up anchor.

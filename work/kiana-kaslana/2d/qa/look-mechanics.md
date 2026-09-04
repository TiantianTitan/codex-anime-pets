# Kiana Kaslana look mechanics

- Keep both feet on one stable baseline and preserve the full-body scale, white twin-braided hair, blue eyes, white/black/orange Valkyrie suit, and two compact held pistols in every direction.
- The eyes lead each gaze with visible iris, eyelid, and eyebrow changes. The head and neck then turn or pitch, with only restrained upper-torso follow-through; never rotate, shear, stretch, or squash the whole sprite.
- `000` (up): near-front view, irises visibly high, chin slightly lifted, and a little more neck/collar underside visible.
- `090` (screen-right): unmistakable right-facing profile or strong three-quarter view; nose tip, pupils, and facial plane project to the image-right side of the head center, with the far eye reduced or occluded.
- `180` (down): near-front view, irises low, chin tucked, and the crown/fringe more prominent without turning into a back view.
- `270` (screen-left): unmistakable left-facing profile or strong three-quarter view; nose tip, pupils, and facial plane project to the image-left side of the head center, with the far eye reduced or occluded.
- Interpolate the twelve diagonal directions evenly and clockwise between those four anchors. Neighboring frames must never reverse, cross into the opposite horizontal half, repeat an anchor, or create a late scale/registration pop at `337.5` to `000`.
- The twin braids and tied hair ends follow the head turn with a small natural lag. They remain attached and keep their length and volume; they do not switch sides arbitrarily.
- Both pistols remain rigid, compact, attached to their hands, and consistently designed. They may angle or lag slightly with the upper body, but may not float, detach, duplicate, merge into the arms, or stay frozen in an impossible front-facing relationship while the body turns.
- Preserve facial proportions and Kiana's bright, determined expression. No broad raster warp, detached effects, shadows, text, scenery, direction labels, guide marks, or changes of outfit.

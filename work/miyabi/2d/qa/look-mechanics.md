# Miyabi look-direction mechanics

## Character-specific motion model

- Lead the turn with the eyes and eyelids, then rotate the head and neck; allow only a very small upper-torso follow-through.
- Keep the lower torso, hips, legs, boots, and ground contact fixed. This is a look animation, not a whole-body turn or tilted sprite.
- Let the tall fox ears follow the head subtly while staying attached and preserving their natural spacing.
- Keep the long navy-black hair connected to the head and body; it may lag by a small amount, but must not become a detached shape or swap sides.
- Preserve Miyabi's asymmetry throughout the turn: the black mechanical arm with its red braided cord, the teal sleeve, and the sheathed katana stay on their established character sides.
- Keep the katana rigidly attached at the hip. Do not bend, duplicate, detach, or swing it as an effect.
- Do not add motion lines, petals, flames, ice, glows, text, logos, or extra props.

## Cardinal landmarks

- `000` / up: eyes sit high in the sockets, chin lifts, more neck and collar underside becomes visible, and the ears read attentive.
- `090` / image-right: nose, mouth, pupils, and facial projection move to the image-right side of the head center. The rear cheek and hair mass remain behind the turn.
- `180` / down: eyes sit low, upper eyelids and fringe dominate, chin tucks toward the collar, and less neck is visible.
- `270` / image-left: nose, mouth, pupils, and facial projection move to the image-left side of the head center. It must be the clear opposite of `090`.

## Rejection gates

- Reject pupil-only motion with an essentially unchanged head silhouette.
- Reject whole-sprite rotation, tilted canvas poses, stepping feet, or shifting ground contact.
- Reject any horizontal sequence that reverses direction between neighboring slots.
- Reject an up/down sequence without clear, independent vertical evidence in eyelid, iris, chin, and neck/collar landmarks.
- Reject costume-side swapping, mirrored mechanical-arm details, detached ears or hair, and deformed or duplicated katana parts.

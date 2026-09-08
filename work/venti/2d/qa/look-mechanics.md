# Venti look mechanics

Venti is a compact humanoid chibi, so gaze direction is carried first by his teal irises and eyelids, then by a restrained head-and-neck turn. His skull, facial proportions, hat, hands, and lyre remain rigid in shape; no whole-sprite rotation, affine tilt, or elastic facial warp is allowed.

## Anchors and follow-through

- Keep both feet, lower torso, and the bottom edge of the cape registered to one shared baseline.
- Keep the wooden lyre physically attached to both hands and close to the torso. It turns with the upper body and may become slightly foreshortened, but it never changes sides, floats, stretches, or detaches.
- The eyes lead each 22.5-degree step. Eyelids and brows support pitch; the nose, chin, cheeks, and visible ear/side-lock balance support yaw.
- The teal-tipped braids, long hat feather, and cape follow the head and shoulders with only a small continuous lag. The cream flower and feather stay on their canonical side and must not mirror between cells.
- Preserve one body scale, one head size, and one lower-body anchor through the complete loop. Each adjacent step receives a similar motion budget.

## Cardinal pose families

- `000 up`: broad near-frontal pose. Both eyes remain visible, irises sit high, upper eyelids open, and the chin lifts enough to reveal more neck and ruffle below the jaw. The lyre stays centered against the torso; the feather rises gently with the head.
- `090 screen-right`: unmistakable screen-right three-quarter/profile. The nose tip, pupils, and facial plane project toward the image-right side of the head; the far cheek and far eye narrow naturally. The shoulders and lyre yaw slightly right without changing the planted feet.
- `180 down`: broad near-frontal pose. Irises sit low, upper eyelids lower, the chin tucks toward the ruffle, and the hat brim/forelock becomes more prominent. The torso and lyre remain stable rather than shrinking or dropping.
- `270 screen-left`: unmistakable screen-left three-quarter/profile, visibly opposing `090`. The nose tip, pupils, and facial plane project toward image-left; the far cheek and far eye narrow naturally. The lyre follows the small leftward shoulder turn while remaining attached.

## Interpolation and boundaries

- Row 9 moves evenly `000 → 022.5 → 045 → 067.5 → 090 → 112.5 → 135 → 157.5`, combining yaw with a gradual up-to-down pitch arc.
- Row 10 continues evenly `180 → 202.5 → 225 → 247.5 → 270 → 292.5 → 315 → 337.5`, then closes one equal step into `000`.
- `157.5 → 180` must finish the down-right family without a scale or registration snap.
- `337.5 → 000` must reopen to the full near-frontal up pose gradually; the final row-10 cell should already be close to the approved `000` envelope while retaining a subtle screen-left cue.

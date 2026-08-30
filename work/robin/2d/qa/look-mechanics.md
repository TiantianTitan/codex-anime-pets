# Robin look mechanics

## Natural motion

Robin is a compact humanoid chibi. Her gaze is led by the turquoise-violet eyes and eyelids, followed by a small rigid head-and-neck yaw or pitch and a restrained upper-torso response. Her skull, facial spacing, dress, hands, and feet must never be raster-warped. The feet and lower skirt hem remain the stable anchor; the torso stays centered and does not rotate as a whole sprite.

Her gold flower-tip halo is worn above the head and follows the head as one rigid ornament without changing handedness, scale, or flower count. The small ear-wings follow the head turn. The long rear hair and ribbon-like locks lag the head by a very small, continuous amount, curling inward so each pose remains compact. The asymmetric indigo dress panel and gold trim keep their canonical side; no direction is made by mirroring the complete character. Robin holds no prop in this pet design.

## Cardinal pose families

- `000 up`: front-biased pose; pupils and irises visibly high inside the original eye apertures, upper eyelids open, chin raised and face pitched upward. Both ear-wings remain visible; the halo follows upward without floating away. This is clearly different from neutral idle.
- `090 screen-right`: pupils, nose tip, face center and chin shift toward the image's right. The screen-right facial contour leads, the far eye and far cheek compress slightly, the head/neck yaw right, and the near ear-wing/hair layer separates while the opposite side is partly occluded. The torso follows only subtly and the feet stay planted.
- `180 down`: front-biased pose; pupils and irises visibly low, upper eyelids lower, chin tucks toward the chest and the face pitches down. Bangs occlude a little more upper face while the halo and ear-wings remain attached and readable.
- `270 screen-left`: exact semantic opposite of `090`; pupils, nose tip, face center and chin shift toward the image's left. The screen-left contour leads, the far eye and far cheek compress slightly, the head/neck yaw left, and hair/ear-wing occlusion reverses naturally without mirroring Robin's asymmetric dress or halo design.

## Interpolation and motion budget

The 16 poses form one clockwise attention loop. Each 22.5-degree step changes eye position, eyelids, head yaw/pitch, upper torso, ear-wings, halo, and trailing hair by roughly the same small visual amount. Diagonals combine both required axes; no cell may return to front-neutral, reverse direction, jump in scale, swap outfit sides, or move the feet/base. `157.5 -> 180`, `180 -> 202.5`, and `337.5 -> 000` must be one-step continuations. Hair and halo follow continuously with no teleporting, detached pieces, replacement eyes, whole-sprite rotation, skew, or broad deformation.

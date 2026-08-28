# Zhongli look-direction mechanics

## Natural gaze mechanism

Zhongli is a humanoid chibi with fixed feet and a separately turning head. The amber irises and pupils lead each gaze change, the eyelids and brows reshape subtly, then the head/neck follow with restrained pitch or yaw and the upper torso follows by a smaller amount. The lower torso, legs, feet, body scale, and baseline stay anchored. Do not rotate, skew, stretch, or translate the whole sprite.

The head remains anatomically rigid: preserve skull width, face proportions, eye apertures, bang spacing, and mouth position. Turn/redraw the complete face and eye construction instead of sliding detached pupils over a fixed face. Keep the expression calm and dignified rather than cartoonishly startled.

## Attached-part behavior

- The thick low ponytail remains attached behind the head and lags the head turn by a small, continuous amount; it never flips sides abruptly, multiplies, or becomes a loose ribbon.
- The single geometric tassel earring remains attached to the character's left ear. It follows the ear's new screen position and hangs mostly downward with a slight continuous lag; it may become partly occluded when the far side of the face turns away.
- The crown tuft, side bangs, shoulder panels, coat tails, gold chest geometry, hands, and gloves preserve their identity and proportions. Bangs may reveal or cover a little more of one eye as the head yaws, but may not change hairstyle.
- Hands remain empty and relaxed. No prop or visual effect participates in the gaze.

## Motion budget

Each 22.5-degree step changes the pupils/irises first, eyelids/brows second, head angle third, and upper torso last. Adjacent steps must change these parts by roughly even visual amounts. The feet and lower-body anchor may move by at most a tiny drawing tolerance; head size, body height, and baseline must not pop. The `157.5 → 180` and `337.5 → 000` boundaries use the same step size as interior neighbors.

## Cardinal pose families

- `000 up`: broadly frontal body and face; amber eyes visibly aim toward the top edge, upper eyelids open slightly, chin raises a little, neck lengthens subtly, and the upper torso straightens. Both major facial planes remain visible.
- `090 screen-right`: pupils, nose tip, face plane, and chin turn unmistakably toward the viewer's screen-right. The screen-right side of the head becomes the leading side, the opposite cheek narrows, the bangs show a clear rightward yaw, and the torso follows slightly. The attached earring remains physically consistent with the turned head and may sit nearer the outer screen-right silhouette.
- `180 down`: broadly frontal body; amber eyes visibly aim toward the bottom edge, upper eyelids lower, chin tucks toward the collar, brows soften, and the upper torso inclines forward slightly. The face must read as looking down rather than merely closing its eyes.
- `270 screen-left`: the exact opposing family to `090`; pupils, nose tip, face plane, and chin turn unmistakably toward the viewer's screen-left. The screen-left side becomes the leading side, the opposite cheek narrows, the bangs show leftward yaw, and the torso follows slightly. The earring remains attached and may become more occluded by the turned head, never swapping identity sides.

## Diagonal interpolation

Row 9 travels continuously through the screen-right half: up → up-right → right → down-right → down. Row 10 travels through the screen-left half: down → down-left → left → up-left → up. Diagonals combine the corresponding eye direction, eyelid shape, head pitch/yaw, facial-plane visibility, ponytail lag, earring occlusion, and restrained torso follow-through. Near-vertical intermediates keep subtle horizontal cues without over-deforming the face.

## Hard exclusions

No neutral/front pose in a direction cell; no pupil-only googly-eye slide; no whole-sprite rotation; no broad raster warp; no replacement eyes; no side-swapped earring; no detached tassel or ponytail; no labels, arrows, degree text, clock, scenery, shadow, glow, aura, or prop.

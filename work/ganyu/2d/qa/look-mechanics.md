# Ganyu look mechanics

## Natural motion choice

Ganyu looks around as a soft, attentive humanoid. Her eyes initiate the gaze, her chin and head pitch/turn make the direction unmistakable at pet size, and her shoulders and upper torso follow only enough to keep the face readable. Her feet, hips, scale, and baseline remain anchored. The long ponytail and two waist tassels stay physically attached and may lag the head turn by a very small amount; they never become independent gestures or detached effects.

## Fixed identity and pose anchors

- Keep the full-body sticker/chibi proportions, head size, facial construction, horn shape, clothing layers, bell, ponytail, waist ornament, cord, and tassels consistent with the canonical base and standard contact sheet.
- Keep both feet planted, the body upright, and the same apparent scale and baseline in all sixteen cells.
- Do not rotate, skew, or tilt the whole sprite. Direction comes from eyes, eyelids, nose/face surface, chin, neck, and a restrained shoulder turn.
- The black-red qilin horns remain attached and symmetric around the crown. They follow the head without turning into ears.
- The turquoise-gold waist ornament and red tassels remain on their canonical body side. The ponytail stays attached behind the head and follows the turn with subtle physical lag.

## Cardinal pose families

- `000 up`: near-frontal body and head, chin lifted, eyes and irises clearly aimed upward, more lower iris/sclera visible and a slightly raised upper-lid expression. Neck and lower edge of the bell are a little more visible. This is an unmistakable upward look, not the neutral idle face.
- `090 screen-right`: head and face turn toward the image's right edge. The nose tip, pupils, and facial surface visibly cross to the right of the head center; the screen-left cheek becomes more visible and the far screen-right cheek/eye is partially occluded. The upper torso follows slightly right. The ponytail trails a little toward image-left while remaining attached.
- `180 down`: near-frontal body, chin tucked, eyes and irises clearly aimed downward, upper eyelids lowered and more crown/bangs visible. The bell/neck area compresses slightly. This must contrast unmistakably with `000`.
- `270 screen-left`: head and face turn toward the image's left edge. The nose tip, pupils, and facial surface visibly cross to the left of the head center; the screen-right cheek becomes more visible and the far screen-left cheek/eye is partially occluded. The upper torso follows slightly left. The ponytail trails a little toward image-right while remaining attached.

## Diagonals and motion budget

Interpolate clockwise in even 22.5-degree steps. Every adjacent step moves the pupils, eyelids, chin, head yaw/pitch, and shoulders by roughly the same visible amount. The torso follows less than the head, and the hair/tassel lag follows less than the torso. No adjacent pair may introduce a large silhouette, scale, center, or prop-placement jump.

- `022.5`, `045`, `067.5`: combine the lifted chin/upward pupils of `000` with progressively stronger screen-right head turn, reaching `090` without losing the upward component early.
- `112.5`, `135`, `157.5`: move from screen-right toward down with progressively tucked chin and downward pupils, ending one even step before `180`.
- `202.5`, `225`, `247.5`: move from down toward screen-left with progressively stronger left turn while retaining a readable downward component until `270`.
- `292.5`, `315`, `337.5`: move from screen-left toward up with progressively lifted chin and upward pupils, ending one even step before the approved `000` pose.

## Direction gates

At normal `192x208` pet size, `000`, `090`, `180`, and `270` must be unmistakable without labels. Screen-left and screen-right always mean viewer/image coordinates. Adjacent directions must form one continuous clockwise loop with no reversal, whole-body rocking, identity drift, scale pop, clipping, or detached hair/tassel pieces.

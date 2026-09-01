# Mitsuri Kanroji look mechanics

## Natural gaze mechanism

Mitsuri is a compact humanoid chibi with large physical anime eyes, a distinct nose and mouth, a separate head and neck, broad white haori sleeves, and two heavy pink-to-lime braids. Her gaze must be led by both whole-eye rotation and eyelid/eyebrow shaping, followed by a restrained head-and-neck turn and a very small upper-torso response. Do not slide isolated pupils across fixed eye whites, stretch the skull, warp the face, or tilt/rotate the whole sprite.

Her feet, sandals, pelvis, and lower torso are the registration anchor. The white haori remains attached to the shoulders. Both braids remain attached beside the head and chest; they follow the head with a subtle one-step lag and never jump, swap sides, detach, or become separate props. Mitsuri carries no sword or other prop in this pet design.

## Cardinal pose families

- `000 up`: broadly frontal face and torso. Raise the chin slightly, rotate both green eyes toward the image-top edge, expose a little more lower sclera, lift the upper lids/brows, and let the upper braids settle fractionally lower relative to the raised face. This must read as looking up, not neutral.
- `090 screen-right`: turn the eyes, nose, face surface, chin, and head toward the image-right edge. The nose tip and pupils must sit visibly right of the head center. Use a clear right-facing three-quarter/profile family: the screen-right eye/cheek is dominant, the far screen-left eye narrows or is partly occluded, the screen-right shoulder comes slightly forward, and the braids follow continuously without changing attachment.
- `180 down`: broadly frontal face and torso. Tuck the chin, rotate both eyes toward the image-bottom edge, lower the irises beneath center, let the upper lids/brows angle downward, reveal more crown/forehead and slightly less neck. This must read as looking down, not closed-eye idle.
- `270 screen-left`: turn the eyes, nose, face surface, chin, and head toward the image-left edge. The nose tip and pupils must sit visibly left of the head center. Use the opposing left-facing three-quarter/profile family: the screen-left eye/cheek is dominant, the far screen-right eye narrows or is partly occluded, the screen-left shoulder comes slightly forward, and the braids remain physically attached and continuous.

## Intermediate directions and motion budget

Interpolate the four pose families clockwise in even 22.5-degree steps. Each neighboring step should move the eye direction, eyelids, nose/head turn, neck, shoulders, and upper braid arcs by a comparable small amount. At final `192x208` size, aim for roughly a quarter-iris eye step, a restrained head-turn increment, no more than a few pixels of shoulder/braid follow-through, and no visible change in body height, head size, foot position, or baseline.

The diagonals must retain both required axes: up-right and down-right keep a visible screen-right face cue; down-left and up-left keep a visible screen-left face cue. Preserve a continuous boundary at `157.5 -> 180` and `337.5 -> 000`. No pose may reverse direction, return to neutral, rock the whole body, replace the eye construction, alter facial proportions, add hearts/effects, or introduce a sword, shadow, label, guide mark, or scenery.

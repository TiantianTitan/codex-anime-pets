# Acheron look mechanics

## Natural motion

Acheron is a humanoid chibi with a separate head and torso, one clearly visible violet-magenta eye, a heavy asymmetrical fringe covering the viewer-right eye, long layered hair, and a rigid sheathed katana attached close to her hip and back. Her gaze is led by the visible eye, eyelid, and brow. The head and neck then make a restrained yaw or pitch, followed by a very small shoulder and upper-torso adjustment. Her feet, lower torso, body scale, and baseline stay fixed.

Do not stretch, warp, rotate, skew, or tilt the whole sprite. Preserve skull proportions, facial spacing, the covered-eye fringe, costume asymmetry, shoulder armor, and katana handedness. The visible eye must participate in every direction; a moving head with a frozen eye is not acceptable.

The long hair follows the head with a slight continuous lag. The katana is rigid and remains physically attached at the same mounting point. It may become a little more foreshortened or occluded as the torso turns, but it never swaps sides, floats, bends, or teleports.

## Cardinal pose families

- `000 up`: the visible pupil and iris rotate upward inside the original eye construction; the upper eyelid opens slightly, the chin lifts, more of the throat and collar become visible, and the upper torso eases back by a very small amount. The fringe still covers the viewer-right eye. Hair tips lag downward; the katana remains anchored.
- `090 screen-right`: the visible pupil, nose tip, face, and chin move unmistakably toward the viewer's screen-right. The head turns right with a restrained three-quarter-to-profile cue; the screen-left cheek and shoulder become less prominent while the opposite body side gains visibility. The asymmetrical fringe and shoulder armor do not mirror or swap sides. Hair and katana follow the turn with mild continuous foreshortening.
- `180 down`: the visible pupil rotates down, the upper eyelid lowers, the chin tucks, and the fringe hangs slightly farther over the face. The collar is partly occluded and the shoulders curl forward a little. Feet, hip anchor, and katana mount remain fixed.
- `270 screen-left`: the visible pupil, nose tip, face, and chin move unmistakably toward the viewer's screen-left. The head turns left with an opposing three-quarter-to-profile cue; the screen-right hair mass becomes more prominent while the far shoulder is partly occluded. The covered-eye fringe stays on its canonical side and the katana remains attached without mirroring.

## Intermediate directions and motion budget

Each 22.5-degree step combines the two neighboring cardinal families with roughly equal changes in pupil position, eyelid shape, head yaw or pitch, and upper-body follow-through. No adjacent step may introduce a new pose family, scale change, large bend, sudden crouch, flipped fringe, swapped shoulder armor, or katana jump.

Row 9 must progress evenly through `000 -> 022.5 -> 045 -> 067.5 -> 090 -> 112.5 -> 135 -> 157.5`, ending one small step before down. Row 10 continues with `180 -> 202.5 -> 225 -> 247.5 -> 270 -> 292.5 -> 315 -> 337.5`, ending one small step before the approved up pose. The boundaries `157.5 -> 180` and `337.5 -> 000` must be as smooth as every other neighbor.

No labels, degree text, arrows, clocks, scenery, shadows, glows, motion marks, detached effects, replacement eyes, or newly invented props.

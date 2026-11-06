Create one horizontal animation strip for Codex pet `xiao`, state `running`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure user-selected #FF00FF. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: A vigilant chibi adeptus with teal-tipped hair, golden eyes, jade ornaments, and a quiet watchful presence. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `auto`: Infer the most appropriate pet-safe style from the user request and reference images, then keep that exact style consistent across every row. User style notes: Preserve the exact approved 2D anime chibi sprite art, rendering, proportions, costume and identity. Focused two-row repair, not a redesign..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Working loop: focused active-task processing, thinking, typing, scanning, or effortful concentration; not literal foot-running, jogging, sprinting, treadmill motion, raised knees, long steps, pumping arms, or directional travel.

State requirements:
- Show the pet actively working or processing, as if running a task: focused posture, busy hands or paws, purposeful bobbing, thinking motion, tool or prop motion only if already part of the pet identity, or other non-locomotion activity.
- Do not show literal foot-running, jogging, sprinting, treadmill motion, raised knees, long steps, pumping arms, directional travel, speed lines, dust clouds, floor shadows, motion trails, or detached motion effects.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.


FOCUSED REPAIR REQUIREMENTS
STATE-READABILITY REPAIR: exactly six full-body frames of ACTIVE TASK PROCESSING. Working pose must be visibly different from idle, expectant palm-up waiting, and one-hand-at-chin review. Use BOTH hands compactly in front of the chest/upper abdomen in a purposeful, controlled alternating hand/finger sequence, as quietly arranging or processing thoughts. Slightly lift the elbows and focus the open eyes. Working silhouette must read from frame 0, before the first 820ms cycle ends. Keep feet planted; no foot-running, jumping, waving, arms-crossed waiting, hand on chin, new laptop/book/tool, or detached magic/effects. First and last poses join seamlessly. Preserve costume and accessories exactly.

Identity lock:
# Xiao Identity Lock

This file is authoritative for every generated base, animation row, look row, repair, and final QA decision.

## Face and Hair

- Pale youthful face in polished 2D chibi sticker style.
- Large almond-shaped golden/amber eyes with Xiao's sharp, slightly reserved expression; do not change to blue, green, round googly eyes, or generic black dots.
- Small purple vertical diamond mark centered on the forehead.
- Layered, tousled dark blue-black/charcoal hair with distinct teal/turquoise tips and face-framing strands; prominent upward cowlick.
- Hair silhouette, forehead mark, eye color, and facial proportions must remain recognizable in every frame.

## Body and Costume

- Compact chibi proportions: oversized head, short torso and limbs, small black boots.
- White sleeveless high-neck top with dark collar and restrained pale decorative motifs.
- Exposed screen-left arm in the neutral/front pose carries the luminous green adeptal tattoo; this is a primary identity cue.
- Opposite arm is covered by a fitted black/teal glove and dark forearm protection.
- Purple waist sash over dark navy/purple trousers, with teal/lavender split fabric panels and ribbon tails kept close to the silhouette.
- Small white bead necklace and jade/teal ornaments at the collar, waist, and hip.
- Dark, jade, cream, purple, and turquoise palette with small gold accents; do not shift to predominantly red, blue, or monochrome clothing.

## Props and Asymmetry

- Small dark Yaksha mask with teal/gold details remains strapped securely at the hip/back; it may be raised near the face only when physically held and attached.
- Do not make a long polearm a permanent sprite prop. Do not invent swords, books, pets, wings, hats, capes, or extra weapons.
- Preserve tattoo side, glove side, sash layering, jade ornaments, fabric-panel order, and mask attachment. Because these are asymmetric, running-left must not be created by a simple mirror.

## Rendering Style

- Clean non-pixel 2D chibi sticker illustration with dark crisp outlines, smooth cel shading, and minimal soft highlights.
- No photorealism, 3D rendering, painterly brushwork, pixel art, thick white sticker border, or dramatic environmental lighting.
- One Xiao only per frame; no companions, duplicates, text, logos, icons, scenery, floor, cast shadow, glow, aura, or detached particles.

## Scale and Registration

- Full body visible in every pose, including hair, ribbons, hands, and feet.
- Stable head size, torso width, overall scale, and foot baseline across neighboring frames.
- Keep the character centered with safe outer margins and clear separation between pose groups in generated row strips.
- Long hair tips and ribbon tails may follow motion subtly but must remain attached and may not form floating fragments.

## Expression Language

- Default: calm, watchful, mildly aloof.
- Greeting: restrained and courteous, not exuberant.
- Failed: visibly deflated without exaggerated crying effects.
- Waiting: alert and expectant.
- Processing/review: focused and analytical, with clearly different hand and head actions.

## Look-Direction Invariants

- Eyes lead; eyelids and brows reshape slightly; head and neck follow with restrained upper-torso motion.
- Feet/lower body stay anchored. Do not rotate or skew the entire sprite.
- Forehead diamond, hair silhouette, tattoo, glove, beads, sash, ornaments, and attached mask must preserve identity and placement through the turn.
- Viewer coordinates are absolute: 090 points screen-right and 270 points screen-left.
- Cardinals must be unmistakable at normal pet size; diagonals interpolate smoothly without reversals or scale pops.

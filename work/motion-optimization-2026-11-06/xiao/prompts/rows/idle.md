Create one horizontal animation strip for Codex pet `xiao`, state `idle`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure user-selected #FF00FF. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: A vigilant chibi adeptus with teal-tipped hair, golden eyes, jade ornaments, and a quiet watchful presence. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `auto`: Infer the most appropriate pet-safe style from the user request and reference images, then keep that exact style consistent across every row. User style notes: Preserve the exact approved 2D anime chibi sprite art, rendering, proportions, costume and identity. Focused two-row repair, not a redesign..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Calm low-distraction resting loop: subtle breathing, tiny blink, slight head/body bob, and only quiet persona-preserving motion.

State requirements:
- CRITICAL: idle is the low-distraction baseline state and the first frame is also used as the reduced-motion static pet.
- Use only subtle idle motion: gentle breathing, a tiny blink, a slight head or body bob, a very small material sway, or another quiet motion that fits the pet persona.
- Keep the pet essentially in the same pose, facing direction, silhouette, markings, palette, and prop state across all 6 frames.
- Idle variation must stay calm but still read as animation; do not repeat effectively identical copies across the loop.
- Do not show waving, walking, running, jumping, talking, working, reviewing, emotional reactions, large gestures, item interactions, or new props.
- Feet, base, body, or object anchor should remain planted or nearly planted.
- The first and last frames should be very close visually so the loop feels calm and does not pop.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.


FOCUSED REPAIR REQUIREMENTS
SLOW-IDLE REPAIR: exactly six full-body frames. The runtime holds frames for 1680,660,660,840,840,1920 ms. Keep BOTH EYES OPEN in every frame; no held closed-eye blink. Add a restrained breathing arc through shoulders and attached hair/ribbons: rest, slight inhale, inhale, soft peak, exhale, near-rest. Feet stay planted, head proportions and hand pose stay locked. Only 1-3 native-pixel equivalent shifts of upper body, no whole-body travel. First and last pose almost identical. Preserve original neutral pose and original practical size. No new emotion, gesture or prop.

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

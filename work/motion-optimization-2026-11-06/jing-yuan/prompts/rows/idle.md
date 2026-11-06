Create one horizontal animation strip for Codex pet `jing-yuan`, state `idle`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure user-selected #0000FF. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: A calm, sharp-eyed chibi general with silver-white hair, a golden eye, red ribbons, and a refined black-white-red-gold uniform. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
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
# Jing Yuan 景元 — 2D Identity Lock

## Immutable identity

- Chibi adult male general with a compact whole-body silhouette, large head, small body, calm confidence, and a faint knowing smile.
- Thick silver-white hair: long layered side and back locks, a heavy fringe covering the viewer-left eye, one small swept crown tuft, and a broad soft hair silhouette around the shoulders.
- One clearly visible golden-amber viewer-right eye with a dark upper lash line; pale skin and restrained warm blush. Do not reveal or invent a differently colored hidden eye.
- Deep red ribbon and hair ties emerging behind the crown and trailing behind the hair; preserve their placement, color, and attachment.
- Black inner uniform with white outer coat panels, dark gloves/arm guards, red trousers or lower panels, black boots, and restrained gold ornamental trim. Keep the same outfit in every row.
- Refined black, white, oxblood red, antique gold, and warm amber palette. Hair remains silver-white rather than gray, blond, or blue.
- Character reads as composed, observant, strategic, slightly sleepy, and gently amused rather than aggressive or childish.

## Style and silhouette

- Use clean 2D anime-sticker linework with simplified cel shading and crisp, readable color blocks; no painterly background, photorealism, 3D rendering, pixel art, or text.
- Keep the head and hair mass dominant but leave enough breathing room around the complete body inside every sprite slot.
- Preserve the distinctive viewer-left eye-covering fringe, visible gold eye, red ribbon, black-white-red uniform, and gold accents at `192x208` display size.
- Tiny armor seams and micro-decoration may be simplified, but the major color-block layout, collar, coat tails, belt region, gloves, trousers, and boots must stay consistent.

## Prop policy

- The canonical pet is unarmed and carries no cup, fan, chair, mascot, weapon, scroll, paper, UI panel, or new handheld prop.
- A weapon appears in one source only as full-body costume context; exclude it from the pet so handedness, clipping, detached pieces, and direction continuity remain reliable.

## Animation-variable traits

- Idle may use subtle breathing, one restrained blink of the visible eye, slight hair bob, and tiny ribbon follow-through.
- Running-right and running-left use compact directional locomotion with alternating steps; hair and ribbon trail naturally without speed lines or dust.
- Waving uses one hand only, with no wave marks or symbols.
- Jumping uses body height and limb compression only: anticipation, lift, peak, descent, settle; no floor cues, impact marks, or shadows.
- Failed may lower the head and visible eyelid, slump the shoulders, and soften the smile; no floating X, punctuation, detached tears, or smoke.
- Waiting is an expectant request-for-input pose, distinct from idle; running is focused task processing rather than literal foot-running; review is a quiet close inspection without adding papers, magnifiers, or UI.

## Look mechanics

- Directions use viewer/screen coordinates. `090` faces screen-right and `270` faces screen-left.
- The visible gold eye leads; the eyelid and brow reshape, then the head and upper torso follow subtly. Long hair and red ribbons lag continuously while the feet/lower body remain registered.
- For screen-right, the visible eye, nose tip, cheek line, and face plane shift toward the image-right edge. For screen-left, the head and face plane turn toward the image-left edge even though the heavy fringe still covers the viewer-left eye.
- Up/down directions combine eye aim, eyelid shape, chin angle, head pitch, and restrained upper-body follow-through. Do not fake gaze by rotating, skewing, or warping the entire sprite.
- The hidden-eye fringe, red ribbon attachment, facial proportions, costume blocks, and gold trim must not flip sides or teleport between adjacent directions.

## Mirroring policy

- Do not mirror the canonical identity, waving, standard semantic rows, cardinals, or look rows.
- `running-left` may be deterministically mirrored from an approved `running-right` row only if the finished pet has no meaningful asymmetric costume, hair-ribbon, lighting, or face detail that changes identity. Otherwise generate it independently.

## Exclusions

- No exclamation marks, question marks, speech bubbles, text, logos, watermarks, degree labels, grids, guide marks, UI, scenery, floor, cast shadow, glow, aura, lightning, detached sparkles, speed lines, dust, motion trails, or floating effects.
- No chair, drink cup, round mascot, sword, spear, scroll, magnifying glass, paper, or prop introduced from individual references.
- No eye-color changes, exposed second eye, outfit switching, hairstyle shortening, ribbon removal, animal ears, horns, or additional characters.

Create one horizontal animation strip for Codex pet `dan-heng-imbibitor-lunae`, state `idle`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure user-selected #FF00FF. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: A calm chibi Vidyadhara companion with cyan dragon antlers, long dark-teal hair, luminous eyes, white draped sleeves, and elegant jade-gold details. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
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
# Dan Heng · Imbibitor Lunae — Identity Lock

## Non-negotiable anchors

| Feature | Locked reading | Failure examples |
|---|---|---|
| Hair | Near-black navy, central heavy fringe, long layered back locks | Brown hair, short bob, missing long rear locks |
| Dragon antlers | Two translucent cyan-teal branched antlers, modest gold accents | Animal ears, one horn, solid black horns, oversized branches |
| Face | Pale skin, cyan/teal eyes, pointed ears, composed expression | Red eyes, round human ears, broad grin as default |
| Outfit | White draped sleeves over dark teal-black short inner outfit | Long trousers, generic robe, white dress, armored warrior redesign |
| Ornament | Central jade/lotus-like teal-and-gold waist motif | Missing waist focal point, large unrelated emblem |
| Palette | Near-black/navy, white, teal/cyan, jade, restrained muted gold | Red-dominant, purple-dominant, neon rainbow |
| Silhouette | Compact chibi with visible feet and stable antler/hair outline | Realistic adult proportions, cropped horns/feet, varying body scale |
| Aqua accent | Attached and restrained tail/water-ribbon shape | Detached dragon, floating magic, splash particles, separate companion |

## Consistency rules

- The same face, hair partition, antler design, ear length, outfit construction, ornament placement, and boot shape persist through all rows.
- Any directional rotation changes visible projection, not character identity.
- Left/right locomotion must be authored with consistent asymmetry; do not blindly mirror text, symbols, or costume construction.
- Motion may deform hair and cloth, but must not add or remove accessories.
- Keep the whole character inside each source panel with generous clearance for antlers, long hair, sleeves, feet, and aqua accent.

## Excluded reference content

Do not reproduce the card frame, product display base, room scene, logo, copyright footer, vertical text, weapon turntable, yellow prop, small black pet, speech bubbles, hearts, punctuation marks, water splashes, or any other detached item visible in the references.


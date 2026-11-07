# Rita Rossweisse — generation provenance

Built-in image_gen only. Job specifications below; exact per-call prompts, inputs and outcomes are retained in the linked worker JSON files. Reference originals remain local and ignored.

## base

Exact tool-call record: `base-worker-calls.json`.

Create one clean full-body reference sprite for Codex pet Rita Rossweisse.

Pet identity: Rita Rossweisse, classic short-haired black-and-white combat maid costume ONLY. Clean polished 2D anime chibi, about 2.6 heads tall, mature poise. Ash-brown bob and side-swept fringe covering anatomical LEFT eye (front screen-right), visible wine-red RIGHT eye (front screen-left). White frilled maid headband with black bows and a small wine-red rose on anatomical RIGHT temple (front screen-left). White puff shoulder sleeves, fitted black bodice, white waist apron and white frilled short skirt, dark long gloves, dark thigh-high stockings and black low-heel shoes. Keep both hands empty; no scythe, cup, flowers, tool, floor shadow, aura or effects. Follow qa/identity-lock.md. Preserve asymmetry; do NOT mirror left gait. Keep natural visible eye comfortably open for idle; never reveal an invented second eye. Anatomical scale consistent, compact body with clear face and clean outlines..
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Flat 2D anime linework and restrained cel shading, clean detailed chibi matching existing collection, not pixel art or 3D toy. Simplify lace into readable white trim. One complete compact silhouette with attached decorations, no detached effects. Keep about 178-182px full-body height within eventual 192x208 cell, modest hop room..


Place a single centered pose on a perfectly flat pure user-selected #00FF00 chroma-key background. Keep the full pet visible, compact, readable at 192x208, and easy to animate. Preserve approved reference identity cues. No scenery, text, borders, checkerboard transparency, shadows, glows, detached effects, or extra props. Keep #00FF00 and close colors out of the pet, props, highlights, and effects.

## idle

Exact tool-call record: `idle-worker-calls.json`.

Create one horizontal animation strip for Codex pet `rita-rossweisse`, state `idle`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure user-selected #00FF00. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Rita Rossweisse, classic short-haired black-and-white combat maid costume ONLY. Clean polished 2D anime chibi, about 2.6 heads tall, mature poise. Ash-brown bob and side-swept fringe covering anatomical LEFT eye (front screen-right), visible wine-red RIGHT eye (front screen-left). White frilled maid headband with black bows and a small wine-red rose on anatomical RIGHT temple (front screen-left). White puff shoulder sleeves, fitted black bodice, white waist apron and white frilled short skirt, dark long gloves, dark thigh-high stockings and black low-heel shoes. Keep both hands empty; no scythe, cup, flowers, tool, floor shadow, aura or effects. Follow qa/identity-lock.md. Preserve asymmetry; do NOT mirror left gait. Keep natural visible eye comfortably open for idle; never reveal an invented second eye. Anatomical scale consistent, compact body with clear face and clean outlines.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Flat 2D anime linework and restrained cel shading, clean detailed chibi matching existing collection, not pixel art or 3D toy. Simplify lace into readable white trim. One complete compact silhouette with attached decorations, no detached effects. Keep about 178-182px full-body height within eventual 192x208 cell, modest hop room..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Calm low-distraction resting loop: subtle breathing, slight hair or material sway, and only quiet persona-preserving motion.

State requirements:
- CRITICAL: idle is the low-distraction baseline state and the first frame is also used as the reduced-motion static pet.
- Use only subtle idle motion: gentle breathing, slight head or body movement, a very small material sway, or another quiet motion that fits the pet persona.
- Keep the pet essentially in the same pose, facing direction, silhouette, markings, palette, and prop state across all 6 frames.
- Idle variation must stay calm but still read as animation; do not repeat effectively identical copies across the loop.
- Do not show waving, walking, running, jumping, talking, working, reviewing, emotional reactions, large gestures, item interactions, or new props.
- Feet, base, body, or object anchor should remain planted or nearly planted.
- The first and last frames should be very close visually so the loop feels calm and does not pop.
- Keep naturally visible eyes comfortably open in all six slots; do not add blink, wink, or half-closed holds. Preserve character-defined closed eyes, eye patches, sunglasses, and natural occlusion; never invent hidden eyes.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Rita temporal plan (left to right): Six quiet breathing phases: neutral poised stance; small inhale; soft chest lift and minute head tilt; exhale; skirt/hair settles; return close to neutral. The naturally visible RIGHT wine-red eye stays comfortably open. LEFT eye remains covered by the same long side-swept bangs, not closed or artificially exposed. Feet planted, small pleasant smile; no blink or wink holds.

## running-right

Exact tool-call record: `running-right-worker-calls.json`.

Create one horizontal animation strip for Codex pet `rita-rossweisse`, state `running-right`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 8 full-body frames in one left-to-right row on flat pure user-selected #00FF00. Treat the row as 8 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Rita Rossweisse, classic short-haired black-and-white combat maid costume ONLY. Clean polished 2D anime chibi, about 2.6 heads tall, mature poise. Ash-brown bob and side-swept fringe covering anatomical LEFT eye (front screen-right), visible wine-red RIGHT eye (front screen-left). White frilled maid headband with black bows and a small wine-red rose on anatomical RIGHT temple (front screen-left). White puff shoulder sleeves, fitted black bodice, white waist apron and white frilled short skirt, dark long gloves, dark thigh-high stockings and black low-heel shoes. Keep both hands empty; no scythe, cup, flowers, tool, floor shadow, aura or effects. Follow qa/identity-lock.md. Preserve asymmetry; do NOT mirror left gait. Keep natural visible eye comfortably open for idle; never reveal an invented second eye. Anatomical scale consistent, compact body with clear face and clean outlines.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Flat 2D anime linework and restrained cel shading, clean detailed chibi matching existing collection, not pixel art or 3D toy. Simplify lace into readable white trim. One complete compact silhouette with attached decorations, no detached effects. Keep about 178-182px full-body height within eventual 192x208 cell, modest hop room..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Dragging-right loop: show directional movement to the right through body and limb poses only.

State requirements:
- Show directional drag movement to the right through body, limb, and prop movement only.
- The row must unmistakably face and travel right.
- The movement cadence must alternate visibly across the 8 frames instead of repeating one nearly static stride.
- Do not draw speed lines, dust clouds, floor shadows, motion trails, or detached motion effects.
- Work within the fixed slot count: clear preparation, readable action peak, and recovery with a coherent last-to-first seam. Keep the same anatomical scale and all identity props attached and present, including at the transition back to canonical idle. Do not add frames, interpolate pixels, or copy a still to simulate a new action.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Rita temporal plan (left to right): Eight genuinely distinct alternating gait phases facing SCREEN RIGHT throughout: first leg contact, compression, passing, lift; opposite leg contact, compression, passing, lift closing into frame zero. Small controlled running steps and opposing arm swing; skirts follow without changing lengths. Constant skull/torso scale and actual rose/covered-eye sides. No two-pose repetition.

## running-left

Exact tool-call record: `running-left-worker-calls.json`.

Create one horizontal animation strip for Codex pet `rita-rossweisse`, state `running-left`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 8 full-body frames in one left-to-right row on flat pure user-selected #00FF00. Treat the row as 8 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Rita Rossweisse, classic short-haired black-and-white combat maid costume ONLY. Clean polished 2D anime chibi, about 2.6 heads tall, mature poise. Ash-brown bob and side-swept fringe covering anatomical LEFT eye (front screen-right), visible wine-red RIGHT eye (front screen-left). White frilled maid headband with black bows and a small wine-red rose on anatomical RIGHT temple (front screen-left). White puff shoulder sleeves, fitted black bodice, white waist apron and white frilled short skirt, dark long gloves, dark thigh-high stockings and black low-heel shoes. Keep both hands empty; no scythe, cup, flowers, tool, floor shadow, aura or effects. Follow qa/identity-lock.md. Preserve asymmetry; do NOT mirror left gait. Keep natural visible eye comfortably open for idle; never reveal an invented second eye. Anatomical scale consistent, compact body with clear face and clean outlines.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Flat 2D anime linework and restrained cel shading, clean detailed chibi matching existing collection, not pixel art or 3D toy. Simplify lace into readable white trim. One complete compact silhouette with attached decorations, no detached effects. Keep about 178-182px full-body height within eventual 192x208 cell, modest hop room..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Dragging-left loop: show directional movement to the left through body and limb poses only.

State requirements:
- Show directional drag movement to the left through body, limb, and prop movement only.
- The row must unmistakably face and travel left.
- The movement cadence must alternate visibly across the 8 frames instead of repeating one nearly static stride.
- Do not draw speed lines, dust clouds, floor shadows, motion trails, or detached motion effects.
- Work within the fixed slot count: clear preparation, readable action peak, and recovery with a coherent last-to-first seam. Keep the same anatomical scale and all identity props attached and present, including at the transition back to canonical idle. Do not add frames, interpolate pixels, or copy a still to simulate a new action.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Rita temporal plan (left to right): Draw independently, NEVER mirror. Eight genuinely distinct alternating gait phases facing SCREEN LEFT: first leg contact, compression, passing, lift; opposite leg contact, compression, passing, lift. Modest steps and opposing arm swing, consistent skirt shape. Anatomical RIGHT temple rose and anatomical LEFT covered eye stay on real sides; occlude naturally in profile instead of swapping. Right strip is scale/cadence evidence, not a mirrored source.

## waving

Exact tool-call record: `waving-worker-calls.json`.

Create one horizontal animation strip for Codex pet `rita-rossweisse`, state `waving`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 4 full-body frames in one left-to-right row on flat pure user-selected #00FF00. Treat the row as 4 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Rita Rossweisse, classic short-haired black-and-white combat maid costume ONLY. Clean polished 2D anime chibi, about 2.6 heads tall, mature poise. Ash-brown bob and side-swept fringe covering anatomical LEFT eye (front screen-right), visible wine-red RIGHT eye (front screen-left). White frilled maid headband with black bows and a small wine-red rose on anatomical RIGHT temple (front screen-left). White puff shoulder sleeves, fitted black bodice, white waist apron and white frilled short skirt, dark long gloves, dark thigh-high stockings and black low-heel shoes. Keep both hands empty; no scythe, cup, flowers, tool, floor shadow, aura or effects. Follow qa/identity-lock.md. Preserve asymmetry; do NOT mirror left gait. Keep natural visible eye comfortably open for idle; never reveal an invented second eye. Anatomical scale consistent, compact body with clear face and clean outlines.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Flat 2D anime linework and restrained cel shading, clean detailed chibi matching existing collection, not pixel art or 3D toy. Simplify lace into readable white trim. One complete compact silhouette with attached decorations, no detached effects. Keep about 178-182px full-body height within eventual 192x208 cell, modest hop room..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Greeting loop: paw or limb down, raised, tilted, and returning in a friendly attention gesture.

State requirements:
- Show the greeting through paw, hand, wing, or limb pose only.
- Use the four slots for rest, raised greeting, a small greeting change, and recovery close to the first pose; keep the longer final hold comfortable before returning to idle.
- Do not draw wave marks, motion arcs, lines, sparkles, symbols, or floating effects around the gesture.
- Work within the fixed slot count: clear preparation, readable action peak, and recovery with a coherent last-to-first seam. Keep the same anatomical scale and all identity props attached and present, including at the transition back to canonical idle. Do not add frames, interpolate pixels, or copy a still to simulate a new action.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Rita temporal plan (left to right): Four graceful greeting phases: anatomical RIGHT empty gloved hand starts lifting; open palm beside shoulder; restrained friendly wrist wave; hand lowers near relaxed rest. No big overhead gesture, detached wave lines or effects; consistent small smile and head size.

## jumping

Exact tool-call record: `jumping-worker-calls.json`.

Create one horizontal animation strip for Codex pet `rita-rossweisse`, state `jumping`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 5 full-body frames in one left-to-right row on flat pure user-selected #00FF00. Treat the row as 5 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Rita Rossweisse, classic short-haired black-and-white combat maid costume ONLY. Clean polished 2D anime chibi, about 2.6 heads tall, mature poise. Ash-brown bob and side-swept fringe covering anatomical LEFT eye (front screen-right), visible wine-red RIGHT eye (front screen-left). White frilled maid headband with black bows and a small wine-red rose on anatomical RIGHT temple (front screen-left). White puff shoulder sleeves, fitted black bodice, white waist apron and white frilled short skirt, dark long gloves, dark thigh-high stockings and black low-heel shoes. Keep both hands empty; no scythe, cup, flowers, tool, floor shadow, aura or effects. Follow qa/identity-lock.md. Preserve asymmetry; do NOT mirror left gait. Keep natural visible eye comfortably open for idle; never reveal an invented second eye. Anatomical scale consistent, compact body with clear face and clean outlines.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Flat 2D anime linework and restrained cel shading, clean detailed chibi matching existing collection, not pixel art or 3D toy. Simplify lace into readable white trim. One complete compact silhouette with attached decorations, no detached effects. Keep about 178-182px full-body height within eventual 192x208 cell, modest hop room..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Hover jump loop: anticipation, lift, airborne peak, descent, and settle through body height.

State requirements:
- Show the jump through pose and vertical body position only: anticipation, lift, airborne peak, descent, settle.
- Use a modest jump arc at the same anatomical scale as the canonical idle: constant head size and body proportions, complete feet, hair and props. Leave headroom instead of shrinking the character to fit a large leap.
- Ground anticipation and landing on the same baseline; airborne feet rise above it. Do not enlarge the crouch to fill its slot or align airborne feet to the ground. Landing should flow into both the next jump and idle.
- Do not draw ground shadows, contact shadows, drop shadows, oval shadows, landing marks, dust, smears, bounce pads, or motion marks under the pet.
- Keep the background outside the pet perfectly flat chroma key with no darker key-colored patches.
- Work within the fixed slot count: clear preparation, readable action peak, and recovery with a coherent last-to-first seam. Keep the same anatomical scale and all identity props attached and present, including at the transition back to canonical idle. Do not add frames, interpolate pixels, or copy a still to simulate a new action.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Rita temporal plan (left to right): Five phases: shallow knee bend; both shoes lift a little; modest airborne peak with knees softly bent; descent with legs extending; grounded soft near-upright landing. Constant head/torso dimensions matching idle, small hop not deep squat or huge leap. Full maid headband/hair/skirt/shoes with clear headroom. Ground endpoints share baseline; airborne feet rise naturally.

## failed

Exact tool-call record: `failed-worker-calls.json`.

Create one horizontal animation strip for Codex pet `rita-rossweisse`, state `failed`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 8 full-body frames in one left-to-right row on flat pure user-selected #00FF00. Treat the row as 8 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Rita Rossweisse, classic short-haired black-and-white combat maid costume ONLY. Clean polished 2D anime chibi, about 2.6 heads tall, mature poise. Ash-brown bob and side-swept fringe covering anatomical LEFT eye (front screen-right), visible wine-red RIGHT eye (front screen-left). White frilled maid headband with black bows and a small wine-red rose on anatomical RIGHT temple (front screen-left). White puff shoulder sleeves, fitted black bodice, white waist apron and white frilled short skirt, dark long gloves, dark thigh-high stockings and black low-heel shoes. Keep both hands empty; no scythe, cup, flowers, tool, floor shadow, aura or effects. Follow qa/identity-lock.md. Preserve asymmetry; do NOT mirror left gait. Keep natural visible eye comfortably open for idle; never reveal an invented second eye. Anatomical scale consistent, compact body with clear face and clean outlines.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Flat 2D anime linework and restrained cel shading, clean detailed chibi matching existing collection, not pixel art or 3D toy. Simplify lace into readable white trim. One complete compact silhouette with attached decorations, no detached effects. Keep about 178-182px full-body height within eventual 192x208 cell, modest hop room..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Blocked/failed loop: slumped or deflated reaction with sad or closed eyes.

State requirements:
- Show failure through slumped pose, drooping ears/limbs, closed or sad eyes, and lower body position.
- Draw one readable reaction-and-recovery arc within the eight slots, ending near the starting pose. Preserve head size and grounded body scale when bowing or crouching; prefer restrained motion when a dramatic collapse would break the loop or idle transition.
- Tears, small smoke puffs, or tiny stars are allowed only if attached to or overlapping the pet silhouette and kept inside the same frame slot.
- Do not draw red X marks, floating symbols, detached stars, separated smoke clouds, falling tear drops, dust, or other loose effects.
- Work within the fixed slot count: clear preparation, readable action peak, and recovery with a coherent last-to-first seam. Keep the same anatomical scale and all identity props attached and present, including at the transition back to canonical idle. Do not add frames, interpolate pixels, or copy a still to simulate a new action.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Rita temporal plan (left to right): Eight standing reaction/recovery phases: poised start; small surprised brow; faint concern; shoulders soften; brief rueful downward look; head begins to rise; reserved reassuring smile; near-neutral recovery. No collapse or deep bow. Do not add tears, symbols, smoke or tools. Comfortable last hold and return to idle.

## waiting

Exact tool-call record: `waiting-worker-calls.json`.

Create one horizontal animation strip for Codex pet `rita-rossweisse`, state `waiting`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure user-selected #00FF00. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Rita Rossweisse, classic short-haired black-and-white combat maid costume ONLY. Clean polished 2D anime chibi, about 2.6 heads tall, mature poise. Ash-brown bob and side-swept fringe covering anatomical LEFT eye (front screen-right), visible wine-red RIGHT eye (front screen-left). White frilled maid headband with black bows and a small wine-red rose on anatomical RIGHT temple (front screen-left). White puff shoulder sleeves, fitted black bodice, white waist apron and white frilled short skirt, dark long gloves, dark thigh-high stockings and black low-heel shoes. Keep both hands empty; no scythe, cup, flowers, tool, floor shadow, aura or effects. Follow qa/identity-lock.md. Preserve asymmetry; do NOT mirror left gait. Keep natural visible eye comfortably open for idle; never reveal an invented second eye. Anatomical scale consistent, compact body with clear face and clean outlines.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Flat 2D anime linework and restrained cel shading, clean detailed chibi matching existing collection, not pixel art or 3D toy. Simplify lace into readable white trim. One complete compact silhouette with attached decorations, no detached effects. Keep about 178-182px full-body height within eventual 192x208 cell, modest hop room..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Needs-input loop: expectant asking pose for approval, help, or user input.

State requirements:
- Show that Codex needs approval, help, or user input through an expectant asking pose.
- Keep the motion patient and readable, without turning it into ordinary idle or review.
- Work within the fixed slot count: clear preparation, readable action peak, and recovery with a coherent last-to-first seam. Keep the same anatomical scale and all identity props attached and present, including at the transition back to canonical idle. Do not add frames, interpolate pixels, or copy a still to simulate a new action.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Rita temporal plan (left to right): Six expectant phases: attentive rest; slight questioning brow; anatomical LEFT empty gloved palm opens upward at waist; small questioning head tilt; palm starts lowering; expectant near-rest recovery. Feet planted, no chin touch. Distinct from raised greeting and task-processing gesture.

## running

Exact tool-call record: `running-worker-calls.json`.

Create one horizontal animation strip for Codex pet `rita-rossweisse`, state `running`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure user-selected #00FF00. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Rita Rossweisse, classic short-haired black-and-white combat maid costume ONLY. Clean polished 2D anime chibi, about 2.6 heads tall, mature poise. Ash-brown bob and side-swept fringe covering anatomical LEFT eye (front screen-right), visible wine-red RIGHT eye (front screen-left). White frilled maid headband with black bows and a small wine-red rose on anatomical RIGHT temple (front screen-left). White puff shoulder sleeves, fitted black bodice, white waist apron and white frilled short skirt, dark long gloves, dark thigh-high stockings and black low-heel shoes. Keep both hands empty; no scythe, cup, flowers, tool, floor shadow, aura or effects. Follow qa/identity-lock.md. Preserve asymmetry; do NOT mirror left gait. Keep natural visible eye comfortably open for idle; never reveal an invented second eye. Anatomical scale consistent, compact body with clear face and clean outlines.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Flat 2D anime linework and restrained cel shading, clean detailed chibi matching existing collection, not pixel art or 3D toy. Simplify lace into readable white trim. One complete compact silhouette with attached decorations, no detached effects. Keep about 178-182px full-body height within eventual 192x208 cell, modest hop room..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Working loop: focused active-task processing, thinking, typing, scanning, or effortful concentration; not literal foot-running, jogging, sprinting, treadmill motion, raised knees, long steps, pumping arms, or directional travel.

State requirements:
- Show the pet actively working or processing, as if running a task: focused posture, busy hands or paws, purposeful bobbing, thinking motion, tool or prop motion only if already part of the pet identity, or other non-locomotion activity.
- Do not show literal foot-running, jogging, sprinting, treadmill motion, raised knees, long steps, pumping arms, directional travel, speed lines, dust clouds, floor shadows, motion trails, or detached motion effects.
- Work within the fixed slot count: clear preparation, readable action peak, and recovery with a coherent last-to-first seam. Keep the same anatomical scale and all identity props attached and present, including at the transition back to canonical idle. Do not add frames, interpolate pixels, or copy a still to simulate a new action.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Rita temporal plan (left to right): Six active task-processing phases, NOT foot-running: focused rest; anatomical RIGHT gloved fingers approach chin; thoughtful chin touch; small considering head turn; hand starts lowering; focused near-rest recovery. Feet planted, no phone, screen, paper, weapon or other tool.

## review

Exact tool-call record: `review-worker-calls.json`.

Create one horizontal animation strip for Codex pet `rita-rossweisse`, state `review`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure user-selected #00FF00. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Rita Rossweisse, classic short-haired black-and-white combat maid costume ONLY. Clean polished 2D anime chibi, about 2.6 heads tall, mature poise. Ash-brown bob and side-swept fringe covering anatomical LEFT eye (front screen-right), visible wine-red RIGHT eye (front screen-left). White frilled maid headband with black bows and a small wine-red rose on anatomical RIGHT temple (front screen-left). White puff shoulder sleeves, fitted black bodice, white waist apron and white frilled short skirt, dark long gloves, dark thigh-high stockings and black low-heel shoes. Keep both hands empty; no scythe, cup, flowers, tool, floor shadow, aura or effects. Follow qa/identity-lock.md. Preserve asymmetry; do NOT mirror left gait. Keep natural visible eye comfortably open for idle; never reveal an invented second eye. Anatomical scale consistent, compact body with clear face and clean outlines.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Flat 2D anime linework and restrained cel shading, clean detailed chibi matching existing collection, not pixel art or 3D toy. Simplify lace into readable white trim. One complete compact silhouette with attached decorations, no detached effects. Keep about 178-182px full-body height within eventual 192x208 cell, modest hop room..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Ready-review loop: focused inspection of completed output with lean, blink, narrowed eyes, head tilt, or paw pose.

State requirements:
- Show review through lean, blink, narrowed eyes, head tilt, or paw/hand position.
- Do not add magnifying glasses, papers, code, UI, punctuation, symbols, or other new props unless they already exist in the base pet identity.
- Work within the fixed slot count: clear preparation, readable action peak, and recovery with a coherent last-to-first seam. Keep the same anatomical scale and all identity props attached and present, including at the transition back to canonical idle. Do not add frames, interpolate pixels, or copy a still to simulate a new action.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Rita temporal plan (left to right): Six inspection phases: attentive rest with hands composed low; visible gaze lowers slightly; modest head inclination; restrained approving nod; head rises; return close to poised rest. Feet planted. Keep same head size even while nodding. No new prop. Distinct from chin-touch work and palm-up waiting.

## look-cardinals

Exact tool-call record: `look-cardinals-worker-calls.json`.

Create one horizontal four-cardinal anchor strip for Codex pet `rita-rossweisse`.

Use the attached canonical base, completed standard contact sheet, and layout guide for exact identity, style, scale, baseline, face construction, materials, palette, markings, props, and spacing. Read `qa/look-mechanics.md` and use the pet's natural gaze mechanism.

Output exactly four centered complete full-body poses in this exact left-to-right order: `000 up`, `090 screen-right`, `180 down`, `270 screen-left`. Screen-left and screen-right always mean the viewer's image edges, never the character's own left or right.

For `000`, keep the face broadly frontal and point the eyes and natural head mechanism toward the TOP edge. For `090`, put the nose tip, pupils, face surface, or natural aiming feature on the screen-right side of the head center. For `180`, keep the face broadly frontal and point toward the BOTTOM edge. For `270`, apply the inverse screen-left landmark rule. Every cardinal must be unmistakable without labels.

Place one pose in each invisible equal-width slot on a flat pure user-selected #00FF00 background with generous padding. Keep scale, feet/base, lower body, and registration consistent across all four slots.

Do not rotate, skew, or tilt the whole sprite to fake gaze. Do not add replacement eyes, labels, degree text, arrows, boxes, guide marks, shadows, scenery, detached effects, or chroma-key colors inside the pet.

## look-row-9

Exact tool-call record: `look-row-9-worker-calls.json`.

Create one horizontal look-direction strip for Codex pet `rita-rossweisse`, atlas row 9.

Use the attached canonical base, completed standard contact sheet, layout guide, and approved four-cardinal strip for identity, scale, registration, spacing, direction semantics, and cross-row continuity. Read `qa/look-mechanics.md` and follow its pet-specific movement and eye/prop mechanics. The approved cardinal strip is authoritative for the up, screen-right, down, and screen-left pose families. Interpolate the intermediate directions as even 22.5-degree steps between those anchors.

COHERENT SYNTHESIS LOCK: produce one unified eight-pose row. Do not paste, tile, or independently restyle individual cells. Every final cell must be drawn together with the same face construction, body proportions, line/render quality, lighting, materials, scale, baseline, and registration.

Output exactly 8 complete full-body frames in this exact left-to-right order: 000, 022.5, 045, 067.5, 090, 112.5, 135, 157.5. Degrees are clockwise: 000 is up, 090 right, 180 down, and 270 left. Neutral/front is not part of this row.

DIRECTION TARGETS — use these to shape the coherent row, not as pixel-level landmark gates:

1. `000`: vertical UP; no horizontal requirement.
2. `022.5`: horizontal SCREEN-RIGHT and vertical UP.
3. `045`: horizontal SCREEN-RIGHT and vertical UP.
4. `067.5`: horizontal SCREEN-RIGHT and vertical UP.
5. `090`: horizontal SCREEN-RIGHT; no vertical requirement.
6. `112.5`: horizontal SCREEN-RIGHT and vertical DOWN.
7. `135`: horizontal SCREEN-RIGHT and vertical DOWN.
8. `157.5`: horizontal SCREEN-RIGHT and vertical DOWN.

Cardinals must be unmistakable. Intermediate poses should broadly occupy the intended quadrant and advance naturally through the ordered loop. Minor pupil, nose, eyelid, or aiming-feature deviations are acceptable when the overall direction, continuity, identity, and motion remain coherent. Do not deform the character merely to make every intermediate axis independently obvious.

SCREEN-COORDINATE LOCK: screen-right means the viewer's right image edge, never the character's own right. The row should travel naturally through the right half of the loop. Near-vertical 022.5 and 157.5 may have subtle horizontal cues; prioritize a coherent arc over exact pupil or nose placement.

HARD LAYOUT AND CONTINUITY CONTRACT — DETERMINISTIC REGISTRATION: draw exactly eight separated pose groups in left-to-right direction order. Keep enough chroma-only space between neighboring poses that each complete pose can be detected without cutting through foreground. Approximate the guide's equal spacing, but do not distort a pose merely to hit an exact source-canvas coordinate; deterministic assembly will crop the eight ordered groups, then apply one shared scale and baseline.

Use the same body height, head size, baseline, and planted-body position across the generated family. Never overlap neighboring poses, merge two poses into one connected group, crop foreground at the outer canvas edge, or resize one pose independently.

Keep the feet, base, or lower torso planted at the same coordinates across all eight frames. Express direction through the eyes, face, head, upper body, and physically appropriate prop movement, not by moving, rotating, or rescaling the entire sprite.

Place one centered pose in each invisible equal-width slot on flat pure user-selected #00FF00. Change only the natural parts needed to express gaze: eyes, eyelids, head, face, neck, upper body, appendages, and constrained prop follow-through. Keep identity, silhouette, materials, palette, markings, and props consistent.

ROW-BOUNDARY LOCK: 157.5 must be one even 22.5-degree step before 180. Match the approved 180 pose's body size, baseline, planted anchor, expression, and construction. Preserve the overall right-hand arc, but do not distort pupils, nose, or body geometry merely to exaggerate the subtle horizontal component.

PRE-RETURN CHECK: reject this result if it does not contain eight separated pose groups in the required order; neighboring poses overlap; foreground is cropped at the outer canvas edge; any frame changes sprite scale, body or head size, baseline, or planted-body position; the row visibly reverses into the wrong half of the loop; or 157.5 does not flow evenly into 180. Minor intermediate pupil or nose deviations are not rejection reasons. Exact cell cropping, resizing, and recentering happen deterministically after generation.

Do not rotate, skew, or tilt the whole sprite to fake gaze. Do not add replacement/googly eyes, labels, degree text, arrows, clocks, grids, shadows, glows, scenery, detached effects, or chroma-key colors inside the pet.

## look-row-10

Exact tool-call record: `look-row-10-worker-calls.json`.

Create one horizontal look-direction strip for Codex pet `rita-rossweisse`, atlas row 10.

Use the attached canonical base, completed standard contact sheet, layout guide, and approved four-cardinal strip for identity, scale, registration, spacing, direction semantics, and cross-row continuity. Read `qa/look-mechanics.md` and follow its pet-specific movement and eye/prop mechanics. The approved cardinal strip and completed coherent row 9 are authoritative. Use the cardinals for direction meaning and row 9 for cross-row identity, scale, registration, and continuity.

COHERENT SYNTHESIS LOCK: produce one unified eight-pose row. Do not paste, tile, or independently restyle individual cells. Every final cell must be drawn together with the same face construction, body proportions, line/render quality, lighting, materials, scale, baseline, and registration.

Output exactly 8 complete full-body frames in this exact left-to-right order: 180, 202.5, 225, 247.5, 270, 292.5, 315, 337.5. Degrees are clockwise: 000 is up, 090 right, 180 down, and 270 left. Neutral/front is not part of this row.

DIRECTION TARGETS — use these to shape the coherent row, not as pixel-level landmark gates:

1. `180`: vertical DOWN; no horizontal requirement.
2. `202.5`: horizontal SCREEN-LEFT and vertical DOWN.
3. `225`: horizontal SCREEN-LEFT and vertical DOWN.
4. `247.5`: horizontal SCREEN-LEFT and vertical DOWN.
5. `270`: horizontal SCREEN-LEFT; no vertical requirement.
6. `292.5`: horizontal SCREEN-LEFT and vertical UP.
7. `315`: horizontal SCREEN-LEFT and vertical UP.
8. `337.5`: horizontal SCREEN-LEFT and vertical UP.

Cardinals must be unmistakable. Intermediate poses should broadly occupy the intended quadrant and advance naturally through the ordered loop. Minor pupil, nose, eyelid, or aiming-feature deviations are acceptable when the overall direction, continuity, identity, and motion remain coherent. Do not deform the character merely to make every intermediate axis independently obvious.

SCREEN-COORDINATE LOCK: screen-left means the viewer's left image edge, never the character's own left. The row should travel naturally through the left half of the loop. Near-vertical 202.5 and 337.5 may have subtle horizontal cues; prioritize a coherent arc over exact pupil or nose placement.

HARD LAYOUT AND CONTINUITY CONTRACT — DETERMINISTIC REGISTRATION: draw exactly eight separated pose groups in left-to-right direction order. Keep enough chroma-only space between neighboring poses that each complete pose can be detected without cutting through foreground. Approximate the guide's equal spacing, but do not distort a pose merely to hit an exact source-canvas coordinate; deterministic assembly will crop the eight ordered groups, then apply one shared scale and baseline.

Use the same body height, head size, baseline, and planted-body position across the generated family. Never overlap neighboring poses, merge two poses into one connected group, crop foreground at the outer canvas edge, or resize one pose independently.

Keep the feet, base, or lower torso planted at the same coordinates across all eight frames. Express direction through the eyes, face, head, upper body, and physically appropriate prop movement, not by moving, rotating, or rescaling the entire sprite.

Place one centered pose in each invisible equal-width slot on flat pure user-selected #00FF00. Change only the natural parts needed to express gaze: eyes, eyelids, head, face, neck, upper body, appendages, and constrained prop follow-through. Keep identity, silhouette, materials, palette, markings, and props consistent.

ROW-BOUNDARY LOCK: 180 must continue directly from row 9's 157.5, matching its body size, baseline, planted anchor, expression, and construction. 337.5 must be one even 22.5-degree step before 000: nearly up-facing while remaining on the overall left-hand arc. Do not distort pupils, nose, or body geometry merely to exaggerate the subtle horizontal component.

PRE-RETURN CHECK: reject this result if it does not contain eight separated pose groups in the required order; neighboring poses overlap; foreground is cropped at the outer canvas edge; any frame changes sprite scale, body or head size, baseline, or planted-body position; the row visibly reverses into the wrong half of the loop; or 180 does not continue from 157.5 or 337.5 does not flow evenly into 000. Minor intermediate pupil or nose deviations are not rejection reasons. Exact cell cropping, resizing, and recentering happen deterministically after generation.

Do not rotate, skew, or tilt the whole sprite to fake gaze. Do not add replacement/googly eyes, labels, degree text, arrows, clocks, grids, shadows, glows, scenery, detached effects, or chroma-key colors inside the pet.

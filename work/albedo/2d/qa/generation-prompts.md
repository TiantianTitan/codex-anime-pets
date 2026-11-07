# Albedo generation prompt set

Built-in image_gen only. Each selected strip was generated as a complete source image. Identity references remain local and ignored.


## base

Source SHA256: `531b5f4e54a787f0cab65523cbe8ac4032bf391b9527a5a09ba4b291b1414ff8`

Prompt SHA256: `7059d639d7147c7094217aef611cb047a1617365b7fbfb4a2d6d46c0c157fbc2`

Create one clean full-body reference sprite for Codex pet Albedo.

Pet identity: Albedo from the supplied references: pale ivory-blond tousled layered shoulder-length hair, center-parted long forelocks, small braided half-up rear section; turquoise eyes, fair face, small gold four-point neck mark. White split-tail short-sleeved coat with navy-black hood and lining, gold trim, royal-blue inner shirt, diagonal dark chest strap with gold star ornament on his anatomical left chest (screen-right at neutral), gold left-upper-arm cuff, black elbow-length gloves, dark fitted shorts and thigh-high black boots with silver-blue-gold knee details. Calm inquisitive manner, modest smile. Both hands empty throughout; no sword, brush, palette, easel, paper, books, geo flowers, effects or extra props. Canonical original costume only. Both visible eyes naturally open at rest..
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Polished 2D anime chibi, approximately 2.6 heads tall; fine clean colored outlines and restrained cel shading, no sticker border. Same full-body chibi proportions across all actions. No 3D..


Place a single centered pose on a perfectly flat pure green #00FF00 chroma-key background. Keep the full pet visible, compact, readable at 192x208, and easy to animate. Preserve approved reference identity cues. No scenery, text, borders, checkerboard transparency, shadows, glows, detached effects, or extra props. Keep #00FF00 and close colors out of the pet, props, highlights, and effects.


Inputs:
- `references/reference-01.png` — pet reference
- `references/reference-02.jpg` — pet reference
- `references/reference-03.jpeg` — pet reference


## idle

Source SHA256: `d6c382739d481e2f4cc6392a4659c0e93d9073d36e28a40c945a3fa41e640ad8`

Prompt SHA256: `f08f70678846cb3d6e1cbf6780f790590882ff5dd1ba7d733707813a6da02c3c`

Create one horizontal animation strip for Codex pet `albedo`, state `idle`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure green #00FF00. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Albedo from the supplied references: pale ivory-blond tousled layered shoulder-length hair, center-parted long forelocks, small braided half-up rear section; turquoise eyes, fair face, small gold four-point neck mark. White split-tail short-sleeved coat with navy-black hood and lining, gold trim, royal-blue inner shirt, diagonal dark chest strap with gold star ornament on his anatomical left chest (screen-right at neutral), gold left-upper-arm cuff, black elbow-length gloves, dark fitted shorts and thigh-high black boots with silver-blue-gold knee details. Calm inquisitive manner, modest smile. Both hands empty throughout; no sword, brush, palette, easel, paper, books, geo flowers, effects or extra props. Canonical original costume only. Both visible eyes naturally open at rest.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Polished 2D anime chibi, approximately 2.6 heads tall; fine clean colored outlines and restrained cel shading, no sticker border. Same full-body chibi proportions across all actions. No 3D..
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

Albedo-specific temporal plan (left to right): Six calm breathing phases: neutral, gently inhale, slight chest lift, softly exhale, hair/coat settle, return close to neutral. Both turquoise eyes comfortably open all six; no winks or blinks. Feet planted. Preserve anatomy and volume.


Inputs:
- `references/reference-01.png` — pet reference
- `references/reference-02.jpg` — pet reference
- `references/reference-03.jpeg` — pet reference
- `references/layout-guides/idle.png` — layout guide for 6 frame slots; use for spacing only, do not copy guide lines
- `references/canonical-base.png` — canonical identity reference


## running-right

Source SHA256: `7fc9165f7abff04578f006084b1fd980211af964ba8e9d5d00187d887d5af54e`

Prompt SHA256: `17e117356f658d1a392c49d9fcdb35d72611e239ab2ed19ee52f20ed9b9f8ba5`

Create one horizontal animation strip for Codex pet `albedo`, state `running-right`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 8 full-body frames in one left-to-right row on flat pure green #00FF00. Treat the row as 8 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Albedo from the supplied references: pale ivory-blond tousled layered shoulder-length hair, center-parted long forelocks, small braided half-up rear section; turquoise eyes, fair face, small gold four-point neck mark. White split-tail short-sleeved coat with navy-black hood and lining, gold trim, royal-blue inner shirt, diagonal dark chest strap with gold star ornament on his anatomical left chest (screen-right at neutral), gold left-upper-arm cuff, black elbow-length gloves, dark fitted shorts and thigh-high black boots with silver-blue-gold knee details. Calm inquisitive manner, modest smile. Both hands empty throughout; no sword, brush, palette, easel, paper, books, geo flowers, effects or extra props. Canonical original costume only. Both visible eyes naturally open at rest.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Polished 2D anime chibi, approximately 2.6 heads tall; fine clean colored outlines and restrained cel shading, no sticker border. Same full-body chibi proportions across all actions. No 3D..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Dragging-right loop: show directional movement to the right through body and limb poses only.

State requirements:
- Show directional drag movement to the right through body, limb, and prop movement only.
- The row must unmistakably face and travel right.
- The movement cadence must alternate visibly across the 8 frames instead of repeating one nearly static stride.
- Do not draw speed lines, dust clouds, floor shadows, motion trails, or detached motion effects.
- Work within the fixed slot count: clear preparation, readable action peak, and recovery with a coherent last-to-first seam. Keep the same anatomical scale and all identity props attached and present, including at the transition back to canonical idle. Do not add frames, interpolate pixels, or copy a still to simulate a new action.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Albedo-specific temporal plan (left to right): Eight genuine alternating gait phases all facing SCREEN RIGHT: first-leg contact, compression, passing, lift; opposite-leg contact, compression, passing, lift returning into first contact. Arms oppose legs, knee/ankle poses clearly vary. Keep consistent head size and complete boot tips. No static two-pose repetition.


Inputs:
- `references/reference-01.png` — pet reference
- `references/reference-02.jpg` — pet reference
- `references/reference-03.jpeg` — pet reference
- `references/layout-guides/running-right.png` — layout guide for 8 frame slots; use for spacing only, do not copy guide lines
- `references/canonical-base.png` — canonical identity reference


## running-left

Source SHA256: `fa56dd2d2b687bbd368c6a7b61e54fa6be971f087528abedc5ecceaa519f97c1`

Prompt SHA256: `70b61246378d1b89be2c0d6f7d1f523845039e5255d3cda5cfcbae07c7758ae1`

Create one horizontal animation strip for Codex pet `albedo`, state `running-left`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 8 full-body frames in one left-to-right row on flat pure green #00FF00. Treat the row as 8 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Albedo from the supplied references: pale ivory-blond tousled layered shoulder-length hair, center-parted long forelocks, small braided half-up rear section; turquoise eyes, fair face, small gold four-point neck mark. White split-tail short-sleeved coat with navy-black hood and lining, gold trim, royal-blue inner shirt, diagonal dark chest strap with gold star ornament on his anatomical left chest (screen-right at neutral), gold left-upper-arm cuff, black elbow-length gloves, dark fitted shorts and thigh-high black boots with silver-blue-gold knee details. Calm inquisitive manner, modest smile. Both hands empty throughout; no sword, brush, palette, easel, paper, books, geo flowers, effects or extra props. Canonical original costume only. Both visible eyes naturally open at rest.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Polished 2D anime chibi, approximately 2.6 heads tall; fine clean colored outlines and restrained cel shading, no sticker border. Same full-body chibi proportions across all actions. No 3D..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Dragging-left loop: show directional movement to the left through body and limb poses only.

State requirements:
- Show directional drag movement to the left through body, limb, and prop movement only.
- The row must unmistakably face and travel left.
- The movement cadence must alternate visibly across the 8 frames instead of repeating one nearly static stride.
- Do not draw speed lines, dust clouds, floor shadows, motion trails, or detached motion effects.
- Work within the fixed slot count: clear preparation, readable action peak, and recovery with a coherent last-to-first seam. Keep the same anatomical scale and all identity props attached and present, including at the transition back to canonical idle. Do not add frames, interpolate pixels, or copy a still to simulate a new action.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Albedo-specific temporal plan (left to right): Draw independently, not a mirror: eight genuine alternating gait phases facing SCREEN LEFT. First-leg contact, compression, passing, lift; opposite-leg contact, compression, passing, lift. Arms oppose legs. Preserve anatomical-left chest/arm ornament when turning, do not swap costume asymmetry. Use right strip only for style and anatomical scale.


Inputs:
- `references/identity-board.png` — all three original identity references; costume/face/chibi proportions
- `references/layout-guides/running-left.png` — layout guide for 8 frame slots; use for spacing only, do not copy guide lines
- `references/canonical-base.png` — canonical identity reference
- `decoded/running-right.png` — rightward gait reference for leftward row decision


## waving

Source SHA256: `5a471d5ecfa42c868e955e6d16334706c6652c753f8380453916c3983ad7b862`

Prompt SHA256: `b4eb6609d5f3d92fa01da13f375d2ae91b71bd1c73a683555999acdf06b5437f`

Create one horizontal animation strip for Codex pet `albedo`, state `waving`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 4 full-body frames in one left-to-right row on flat pure green #00FF00. Treat the row as 4 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Albedo from the supplied references: pale ivory-blond tousled layered shoulder-length hair, center-parted long forelocks, small braided half-up rear section; turquoise eyes, fair face, small gold four-point neck mark. White split-tail short-sleeved coat with navy-black hood and lining, gold trim, royal-blue inner shirt, diagonal dark chest strap with gold star ornament on his anatomical left chest (screen-right at neutral), gold left-upper-arm cuff, black elbow-length gloves, dark fitted shorts and thigh-high black boots with silver-blue-gold knee details. Calm inquisitive manner, modest smile. Both hands empty throughout; no sword, brush, palette, easel, paper, books, geo flowers, effects or extra props. Canonical original costume only. Both visible eyes naturally open at rest.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Polished 2D anime chibi, approximately 2.6 heads tall; fine clean colored outlines and restrained cel shading, no sticker border. Same full-body chibi proportions across all actions. No 3D..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Greeting loop: paw or limb down, raised, tilted, and returning in a friendly attention gesture.

State requirements:
- Show the greeting through paw, hand, wing, or limb pose only.
- Use the four slots for rest, raised greeting, a small greeting change, and recovery close to the first pose; keep the longer final hold comfortable before returning to idle.
- Do not draw wave marks, motion arcs, lines, sparkles, symbols, or floating effects around the gesture.
- Work within the fixed slot count: clear preparation, readable action peak, and recovery with a coherent last-to-first seam. Keep the same anatomical scale and all identity props attached and present, including at the transition back to canonical idle. Do not add frames, interpolate pixels, or copy a still to simulate a new action.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Albedo-specific temporal plan (left to right): Four poses: relaxed preparation with hand beginning to lift; hand raised beside shoulder; small friendly open-palm wave with slight wrist change; hand lowers nearly to original relaxed position. Do not leave final hold at the peak. Calm modest smile, empty hands.


Inputs:
- `references/reference-01.png` — pet reference
- `references/reference-02.jpg` — pet reference
- `references/reference-03.jpeg` — pet reference
- `references/layout-guides/waving.png` — layout guide for 4 frame slots; use for spacing only, do not copy guide lines
- `references/canonical-base.png` — canonical identity reference


## jumping

Source SHA256: `d9b1b5b1d62f914d5561a7d7782cb44e83d896e6626bf124e8b360f1032abae0`

Prompt SHA256: `64df5b13a417c805aa871aa48134dec5ccfcb868f69ca1387718aad0c2371262`

Create one horizontal animation strip for Codex pet `albedo`, state `jumping`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 5 full-body frames in one left-to-right row on flat pure green #00FF00. Treat the row as 5 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Albedo from the supplied references: pale ivory-blond tousled layered shoulder-length hair, center-parted long forelocks, small braided half-up rear section; turquoise eyes, fair face, small gold four-point neck mark. White split-tail short-sleeved coat with navy-black hood and lining, gold trim, royal-blue inner shirt, diagonal dark chest strap with gold star ornament on his anatomical left chest (screen-right at neutral), gold left-upper-arm cuff, black elbow-length gloves, dark fitted shorts and thigh-high black boots with silver-blue-gold knee details. Calm inquisitive manner, modest smile. Both hands empty throughout; no sword, brush, palette, easel, paper, books, geo flowers, effects or extra props. Canonical original costume only. Both visible eyes naturally open at rest.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Polished 2D anime chibi, approximately 2.6 heads tall; fine clean colored outlines and restrained cel shading, no sticker border. Same full-body chibi proportions across all actions. No 3D..
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

Albedo-specific temporal plan (left to right): Five phases: shallow knees-bent anticipation; rising with boots slightly above the starting ground; modest airborne peak with bent knees; lowering/descending with legs extending; grounded nearly-upright soft settle. Constant head/torso sizes, not five differently scaled figures. A compact small hop, no deep crouch, no arms over the hair, no huge leap; reserve full hair/boot margins.


Inputs:
- `references/reference-01.png` — pet reference
- `references/reference-02.jpg` — pet reference
- `references/reference-03.jpeg` — pet reference
- `references/layout-guides/jumping.png` — layout guide for 5 frame slots; use for spacing only, do not copy guide lines
- `references/canonical-base.png` — canonical identity reference


## failed

Source SHA256: `589cf6b13b7234d6699b60cc09756bdac76a46b8a2eeb80707a652919abd7d27`

Prompt SHA256: `557f83bf72277fb0f609b02f6a236743d166c20f6c8cb111476a8e4455f857d0`

Create one horizontal animation strip for Codex pet `albedo`, state `failed`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 8 full-body frames in one left-to-right row on flat pure green #00FF00. Treat the row as 8 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Albedo from the supplied references: pale ivory-blond tousled layered shoulder-length hair, center-parted long forelocks, small braided half-up rear section; turquoise eyes, fair face, small gold four-point neck mark. White split-tail short-sleeved coat with navy-black hood and lining, gold trim, royal-blue inner shirt, diagonal dark chest strap with gold star ornament on his anatomical left chest (screen-right at neutral), gold left-upper-arm cuff, black elbow-length gloves, dark fitted shorts and thigh-high black boots with silver-blue-gold knee details. Calm inquisitive manner, modest smile. Both hands empty throughout; no sword, brush, palette, easel, paper, books, geo flowers, effects or extra props. Canonical original costume only. Both visible eyes naturally open at rest.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Polished 2D anime chibi, approximately 2.6 heads tall; fine clean colored outlines and restrained cel shading, no sticker border. Same full-body chibi proportions across all actions. No 3D..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Blocked/failed loop: slumped or deflated reaction with sad or closed eyes.

State requirements:
- Show failure through slumped pose, drooping ears/limbs, closed or sad eyes, and lower body position.
- Draw one readable reaction-and-recovery arc within the eight slots, ending near the starting pose. Preserve head size and grounded body scale when bowing or crouching; prefer restrained motion when a dramatic collapse would break the loop or idle transition.
- Tears, small smoke puffs, or tiny stars are allowed only if attached to or overlapping the pet silhouette and kept inside the same frame slot.
- Do not draw red X marks, floating symbols, detached stars, separated smoke clouds, falling tear drops, dust, or other loose effects.
- Work within the fixed slot count: clear preparation, readable action peak, and recovery with a coherent last-to-first seam. Keep the same anatomical scale and all identity props attached and present, including at the transition back to canonical idle. Do not add frames, interpolate pixels, or copy a still to simulate a new action.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Albedo-specific temporal plan (left to right): Eight phases of one restrained reaction and recovery: calm start, small surprise, shoulders soften, head lowers, brief disappointed exhale, head starts rising, expression recovers, near-neutral end. Remain standing, no deep crouch. Zero tears/stars/smoke, use expression and shoulders only.


Inputs:
- `references/reference-01.png` — pet reference
- `references/reference-02.jpg` — pet reference
- `references/reference-03.jpeg` — pet reference
- `references/layout-guides/failed.png` — layout guide for 8 frame slots; use for spacing only, do not copy guide lines
- `references/canonical-base.png` — canonical identity reference


## waiting

Source SHA256: `5dd70216590980cf65f94b3b6d367e74256c8620b98be6a186711f0022d677fe`

Prompt SHA256: `972b7244d2d4f777a3b346a9bd171396ad51ba68d05f1a1e470ff9b8627d587b`

Create one horizontal animation strip for Codex pet `albedo`, state `waiting`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure green #00FF00. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Albedo from the supplied references: pale ivory-blond tousled layered shoulder-length hair, center-parted long forelocks, small braided half-up rear section; turquoise eyes, fair face, small gold four-point neck mark. White split-tail short-sleeved coat with navy-black hood and lining, gold trim, royal-blue inner shirt, diagonal dark chest strap with gold star ornament on his anatomical left chest (screen-right at neutral), gold left-upper-arm cuff, black elbow-length gloves, dark fitted shorts and thigh-high black boots with silver-blue-gold knee details. Calm inquisitive manner, modest smile. Both hands empty throughout; no sword, brush, palette, easel, paper, books, geo flowers, effects or extra props. Canonical original costume only. Both visible eyes naturally open at rest.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Polished 2D anime chibi, approximately 2.6 heads tall; fine clean colored outlines and restrained cel shading, no sticker border. Same full-body chibi proportions across all actions. No 3D..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Needs-input loop: expectant asking pose for approval, help, or user input.

State requirements:
- Show that Codex needs approval, help, or user input through an expectant asking pose.
- Keep the motion patient and readable, without turning it into ordinary idle or review.
- Work within the fixed slot count: clear preparation, readable action peak, and recovery with a coherent last-to-first seam. Keep the same anatomical scale and all identity props attached and present, including at the transition back to canonical idle. Do not add frames, interpolate pixels, or copy a still to simulate a new action.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Albedo-specific temporal plan (left to right): Six phases: attentive start, small questioning brow, one empty palm turns up near waist, slight expectant head tilt, palm lowers, calm expectant recovery near start. Distinct from thinking work and from a wave; eyes remain attentive.


Inputs:
- `references/reference-01.png` — pet reference
- `references/reference-02.jpg` — pet reference
- `references/reference-03.jpeg` — pet reference
- `references/layout-guides/waiting.png` — layout guide for 6 frame slots; use for spacing only, do not copy guide lines
- `references/canonical-base.png` — canonical identity reference


## running

Source SHA256: `770ed3b7b97db6b2fab1784e02fff1b0b851abca6a245ac6eebc5bfda8ef8e0f`

Prompt SHA256: `91565dc26b34e8610c385feca5412261ded245fda5c75327c1a35d4a44e24726`

Create one horizontal animation strip for Codex pet `albedo`, state `running`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure green #00FF00. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Albedo from the supplied references: pale ivory-blond tousled layered shoulder-length hair, center-parted long forelocks, small braided half-up rear section; turquoise eyes, fair face, small gold four-point neck mark. White split-tail short-sleeved coat with navy-black hood and lining, gold trim, royal-blue inner shirt, diagonal dark chest strap with gold star ornament on his anatomical left chest (screen-right at neutral), gold left-upper-arm cuff, black elbow-length gloves, dark fitted shorts and thigh-high black boots with silver-blue-gold knee details. Calm inquisitive manner, modest smile. Both hands empty throughout; no sword, brush, palette, easel, paper, books, geo flowers, effects or extra props. Canonical original costume only. Both visible eyes naturally open at rest.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Polished 2D anime chibi, approximately 2.6 heads tall; fine clean colored outlines and restrained cel shading, no sticker border. Same full-body chibi proportions across all actions. No 3D..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Working loop: focused active-task processing, thinking, typing, scanning, or effortful concentration; not literal foot-running, jogging, sprinting, treadmill motion, raised knees, long steps, pumping arms, or directional travel.

State requirements:
- Show the pet actively working or processing, as if running a task: focused posture, busy hands or paws, purposeful bobbing, thinking motion, tool or prop motion only if already part of the pet identity, or other non-locomotion activity.
- Do not show literal foot-running, jogging, sprinting, treadmill motion, raised knees, long steps, pumping arms, directional travel, speed lines, dust clouds, floor shadows, motion trails, or detached motion effects.
- Work within the fixed slot count: clear preparation, readable action peak, and recovery with a coherent last-to-first seam. Keep the same anatomical scale and all identity props attached and present, including at the transition back to canonical idle. Do not add frames, interpolate pixels, or copy a still to simulate a new action.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Albedo-specific temporal plan (left to right): Six processing/thinking phases: focused start, empty gloved fingers approach chin, thoughtful chin touch, subtle considering head shift, hand begins to lower, focused near-rest recovery. Boots stay planted; no literal foot-running. No book, brush, tool or UI.


Inputs:
- `references/reference-01.png` — pet reference
- `references/reference-02.jpg` — pet reference
- `references/reference-03.jpeg` — pet reference
- `references/layout-guides/running.png` — layout guide for 6 frame slots; use for spacing only, do not copy guide lines
- `references/canonical-base.png` — canonical identity reference


## review

Source SHA256: `575efa7d89134cccd13d7eb0f92366cac0fed36928f2acfe5103cfea16d3f567`

Prompt SHA256: `40c9d4d36f01036a68a88f464779ec30d556b9bd8cc430d24fb1978c84918dba`

Create one horizontal animation strip for Codex pet `albedo`, state `review`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure green #00FF00. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Albedo from the supplied references: pale ivory-blond tousled layered shoulder-length hair, center-parted long forelocks, small braided half-up rear section; turquoise eyes, fair face, small gold four-point neck mark. White split-tail short-sleeved coat with navy-black hood and lining, gold trim, royal-blue inner shirt, diagonal dark chest strap with gold star ornament on his anatomical left chest (screen-right at neutral), gold left-upper-arm cuff, black elbow-length gloves, dark fitted shorts and thigh-high black boots with silver-blue-gold knee details. Calm inquisitive manner, modest smile. Both hands empty throughout; no sword, brush, palette, easel, paper, books, geo flowers, effects or extra props. Canonical original costume only. Both visible eyes naturally open at rest.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Polished 2D anime chibi, approximately 2.6 heads tall; fine clean colored outlines and restrained cel shading, no sticker border. Same full-body chibi proportions across all actions. No 3D..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Ready-review loop: focused inspection of completed output with lean, blink, narrowed eyes, head tilt, or paw pose.

State requirements:
- Show review through lean, blink, narrowed eyes, head tilt, or paw/hand position.
- Do not add magnifying glasses, papers, code, UI, punctuation, symbols, or other new props unless they already exist in the base pet identity.
- Work within the fixed slot count: clear preparation, readable action peak, and recovery with a coherent last-to-first seam. Keep the same anatomical scale and all identity props attached and present, including at the transition back to canonical idle. Do not add frames, interpolate pixels, or copy a still to simulate a new action.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Albedo-specific temporal plan (left to right): Six inspection phases: calm attentive start, gaze gently lowers, small forward head inclination, restrained approving nod, head rises, returns to calm rest. Both hands near sides. Distinct from chin-touch working, no paper or magnifier.


Inputs:
- `references/reference-01.png` — pet reference
- `references/reference-02.jpg` — pet reference
- `references/reference-03.jpeg` — pet reference
- `references/layout-guides/review.png` — layout guide for 6 frame slots; use for spacing only, do not copy guide lines
- `references/canonical-base.png` — canonical identity reference


## look-cardinals

Source SHA256: `3833f99c4f3d0653f062f6a9903d133897fe1b0bb84bce22a9421e52dd5723e6`

Prompt SHA256: `20948469a73377ffb4221bd7ab282c3e11d8e1c5ff6d63244bb4f7132b3de802`

Create one horizontal four-cardinal anchor strip for Codex pet `albedo`.

Use the attached canonical base, completed standard contact sheet, and layout guide for exact identity, style, scale, baseline, face construction, materials, palette, markings, props, and spacing. Read `qa/look-mechanics.md` and use the pet's natural gaze mechanism.

Output exactly four centered complete full-body poses in this exact left-to-right order: `000 up`, `090 screen-right`, `180 down`, `270 screen-left`. Screen-left and screen-right always mean the viewer's image edges, never the character's own left or right.

For `000`, keep the face broadly frontal and point the eyes and natural head mechanism toward the TOP edge. For `090`, put the nose tip, pupils, face surface, or natural aiming feature on the screen-right side of the head center. For `180`, keep the face broadly frontal and point toward the BOTTOM edge. For `270`, apply the inverse screen-left landmark rule. Every cardinal must be unmistakable without labels.

Place one pose in each invisible equal-width slot on a flat pure green #00FF00 background with generous padding. Keep scale, feet/base, lower body, and registration consistent across all four slots.

Do not rotate, skew, or tilt the whole sprite to fake gaze. Do not add replacement eyes, labels, degree text, arrows, boxes, guide marks, shadows, scenery, detached effects, or chroma-key colors inside the pet.


Inputs:
- `references/look-cardinals-identity-layout.png` — top: three identity references; bottom: matching invisible layout guide (never copy guide graphics)
- `references/canonical-base.png` — canonical identity reference
- `qa/contact-sheet.png` — approved standard-row identity, scale, and baseline reference


## look-row-9

Source SHA256: `c7be07fdbf910ff69cc1cbfc3b994b91d5f7d7d79be2806c3d017f746917711b`

Prompt SHA256: `e8ed10413f54d2d9051ad4f60b9cd56a643bed78094bdcb8b0d90e0a158fe32c`

Create one horizontal look-direction strip for Codex pet `albedo`, atlas row 9.

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

Place one centered pose in each invisible equal-width slot on flat pure green #00FF00. Change only the natural parts needed to express gaze: eyes, eyelids, head, face, neck, upper body, appendages, and constrained prop follow-through. Keep identity, silhouette, materials, palette, markings, and props consistent.

ROW-BOUNDARY LOCK: 157.5 must be one even 22.5-degree step before 180. Match the approved 180 pose's body size, baseline, planted anchor, expression, and construction. Preserve the overall right-hand arc, but do not distort pupils, nose, or body geometry merely to exaggerate the subtle horizontal component.

PRE-RETURN CHECK: reject this result if it does not contain eight separated pose groups in the required order; neighboring poses overlap; foreground is cropped at the outer canvas edge; any frame changes sprite scale, body or head size, baseline, or planted-body position; the row visibly reverses into the wrong half of the loop; or 157.5 does not flow evenly into 180. Minor intermediate pupil or nose deviations are not rejection reasons. Exact cell cropping, resizing, and recentering happen deterministically after generation.

Do not rotate, skew, or tilt the whole sprite to fake gaze. Do not add replacement/googly eyes, labels, degree text, arrows, clocks, grids, shadows, glows, scenery, detached effects, or chroma-key colors inside the pet.


Inputs:
- `references/look-row-9-identity-layout.png` — top: three identity references; bottom: matching invisible layout guide (never copy guide graphics)
- `references/canonical-base.png` — canonical identity reference
- `qa/contact-sheet.png` — approved standard-row identity, scale, and baseline reference
- `decoded/look-anchors-approved.png` — approved cardinal reference strip in order 000 up, 090 screen-right, 180 down, 270 screen-left; interpolate intermediate directions evenly


## look-row-10

Source SHA256: `19b676e51bbffd312e9f4123ed27d8b197bf460979e3bcca74940c41fc54dd33`

Prompt SHA256: `5bc19d763222bd89c4719b8cb5676b696dde7d69637569ccf44a5d5cfcd58a1c`

Create one horizontal look-direction strip for Codex pet `albedo`, atlas row 10.

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

Place one centered pose in each invisible equal-width slot on flat pure green #00FF00. Change only the natural parts needed to express gaze: eyes, eyelids, head, face, neck, upper body, appendages, and constrained prop follow-through. Keep identity, silhouette, materials, palette, markings, and props consistent.

ROW-BOUNDARY LOCK: 180 must continue directly from row 9's 157.5, matching its body size, baseline, planted anchor, expression, and construction. 337.5 must be one even 22.5-degree step before 000: nearly up-facing while remaining on the overall left-hand arc. Do not distort pupils, nose, or body geometry merely to exaggerate the subtle horizontal component.

PRE-RETURN CHECK: reject this result if it does not contain eight separated pose groups in the required order; neighboring poses overlap; foreground is cropped at the outer canvas edge; any frame changes sprite scale, body or head size, baseline, or planted-body position; the row visibly reverses into the wrong half of the loop; or 180 does not continue from 157.5 or 337.5 does not flow evenly into 000. Minor intermediate pupil or nose deviations are not rejection reasons. Exact cell cropping, resizing, and recentering happen deterministically after generation.

Do not rotate, skew, or tilt the whole sprite to fake gaze. Do not add replacement/googly eyes, labels, degree text, arrows, clocks, grids, shadows, glows, scenery, detached effects, or chroma-key colors inside the pet.


Inputs:
- `references/look-row-10-identity-layout.png` — top: three identity references; bottom: matching invisible layout guide (never copy guide graphics)
- `references/canonical-base.png` — canonical identity reference
- `qa/contact-sheet.png` — approved standard-row identity, scale, and baseline reference
- `decoded/look-anchors-approved.png` — approved cardinal reference strip in order 000 up, 090 screen-right, 180 down, 270 screen-left; interpolate intermediate directions evenly
- `decoded/look-row-9.png` — completed first half of the clockwise look loop for row 10 continuity

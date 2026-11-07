# Asaba Harumasa · selected generation prompts

Built-in image_gen was used for every visual job. Original reference images remain local and ignored.

## base

Create one clean full-body reference sprite for Codex pet Asaba Harumasa.

Pet identity: Asaba Harumasa: tousled short dark navy hair/cowlick, golden-yellow eyes, yellow forehead headband and short yellow tails; white shirt, loose dark tie, black harness. Anatomical LEFT (screen-right front): dark tactical sleeve and yellow armband, dark glove. Anatomical RIGHT (screen-left front): rolled white sleeve and yellow glove. Teal waist layers, charcoal trousers, yellow-soled black sneakers; tiny pale cross clasp on neck band; compact dark quiver/short arrow tips on anatomical left back. BOTH HANDS EMPTY, no handheld weapons or added tools; simplify logos to plain unlettered shapes. Keep asymmetries, head size, mature chibi face, colors and outfit constant..
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Clean 2D anime chibi, roughly 2.6 heads tall, crisp colored linework and flat cel shading; adult character translated into chibi, no 3D/PVC/figurine gloss or toddler anatomy..


Place a single centered pose on a perfectly flat pure user-selected #FF00FF chroma-key background. Keep the full pet visible, compact, readable at 192x208, and easy to animate. Preserve approved reference identity cues. No scenery, text, borders, checkerboard transparency, shadows, glows, detached effects, or extra props. Keep #FF00FF and close colors out of the pet, props, highlights, and effects.



## idle

Create one horizontal animation strip for Codex pet `asaba-harumasa`, state `idle`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure user-selected #FF00FF. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Asaba Harumasa: tousled short dark navy hair/cowlick, golden-yellow eyes, yellow forehead headband and short yellow tails; white shirt, loose dark tie, black harness. Anatomical LEFT (screen-right front): dark tactical sleeve and yellow armband, dark glove. Anatomical RIGHT (screen-left front): rolled white sleeve and yellow glove. Teal waist layers, charcoal trousers, yellow-soled black sneakers; tiny pale cross clasp on neck band; compact dark quiver/short arrow tips on anatomical left back. BOTH HANDS EMPTY, no handheld weapons or added tools; simplify logos to plain unlettered shapes. Keep asymmetries, head size, mature chibi face, colors and outfit constant.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Clean 2D anime chibi, roughly 2.6 heads tall, crisp colored linework and flat cel shading; adult character translated into chibi, no 3D/PVC/figurine gloss or toddler anatomy..
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

Harumasa temporal plan (left to right): Six quiet breathing phases: neutral; small inhale; soft chest lift and minute head tilt; exhale; cloth/ribbon settles; return close to neutral. Both golden eyes comfortably open in all six. Feet planted. Calm expression, no prolonged blink or wink.



## running-right

Create one clean 2D anime sprite strip: exactly EIGHT complete Asaba Harumasa poses running toward SCREEN RIGHT, one continuous alternating running cycle from first-foot contact through the opposite-foot contact and back. Use the attached canonical base and original identity board for the same face, navy hair, yellow headband, white/dark asymmetrical outfit, teal waist layers and attached quiver. The additional approved right-profile costume crop is a SIDE/COLOR reference only, not a posture to repeat.

Most important identity rule: exactly ONE yellow glove per pose, on his anatomical RIGHT hand (the near arm with white rolled sleeve in this right-facing view). The far anatomical LEFT hand is always BLACK, attached to a dark sleeve/yellow armband. Do not duplicate the yellow glove when arms cross. Keep the arms separated enough to read clearly. Every pose has both full legs, two shoes, two hands and the same quiver; natural far-side occlusion is allowed.

Use eight distinct phases with opposing arm swing: right foot contact, right stance compression, left knee passing forward, right toe-off with left reaching forward, LEFT foot contact, left stance compression, right knee passing forward, left toe-off with right reaching forward into frame 0. Near/right yellow hand is behind when near/right leg leads, and forward when near/right leg trails. Keep the same skull and torso size across the whole strip. Modest bob only, no deep crouch, no sprint exaggeration.

Pure solid #FF00FF background. Complete evenly separated silhouettes in eight invisible slots, generous head/boot/hand margins. The layout guide is invisible construction only: no text, labels, grid, boxes or marks. No shadows, trails, speed lines, dust, scenery, extra items or weapon. Crisp flat 2D cel shading, not a toy/3D render. Before returning inspect that there is only one yellow glove in EACH of all eight frames and that both legs alternate rather than repeating one stride.



## running-left

Generate one EIGHT-frame horizontal 2D anime chibi sprite strip of Asaba Harumasa JOGGING TOWARD SCREEN LEFT. Preserve the attached canonical character exactly, and use the single left-facing reference crop for the sleeve/hand pairings. Every complete figure faces left with the same readable front-left three-quarter upper-body view. Same skull/torso scale and attached quiver in every frame. Pure uniform #FF00FF background, full separated silhouettes with generous outer canvas margins, no guide graphics, text, effects, shadows or extra props.

CHANGE THE MOTION CONSTRUCTION: Both elbows stay softly bent and both hands stay in ONE STABLE position relative to the torso throughout this cycle. They may bob gently WITH the torso but DO NOT swing forward/back across it, cross, trade sides, or duplicate. The far anatomical RIGHT arm has WHITE sleeve and YELLOW glove held forward near the waist; the near anatomical LEFT arm has DARK sleeve/yellow upper armband and a BLACK glove held close to the rear hip. These exact visible arm/sleeve/glove pairings remain frozen in their basic placement in ALL EIGHT poses. Draw exactly two hands per figure, allow natural far-side occlusion, never attach yellow glove to dark sleeve.

All running motion comes from a genuine alternating LEG CYCLE and a small torso bob/cloth follow-through, not from reusing one pose. Eight phases left to right: first-foot forward contact; stance compression; opposite knee passing; toe-off/lift; opposite-foot forward contact; opposite stance compression; first knee passing; opposite toe-off/lift returning into first contact. Constant anatomy, two complete sneakers, compact comfortable stride rather than long sprint. Boots/hair/quiver never touch canvas edges. Keep the modest steady bent-arm jogging posture while BOTH LEGS alternate clearly. Crisp clean flat 2D cel shading, not a 3D toy. Inspect all eight glove/sleeve attachments and trailing shoe margins before returning.



## waving

Create one horizontal animation strip for Codex pet `asaba-harumasa`, state `waving`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 4 full-body frames in one left-to-right row on flat pure user-selected #FF00FF. Treat the row as 4 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Asaba Harumasa: tousled short dark navy hair/cowlick, golden-yellow eyes, yellow forehead headband and short yellow tails; white shirt, loose dark tie, black harness. Anatomical LEFT (screen-right front): dark tactical sleeve and yellow armband, dark glove. Anatomical RIGHT (screen-left front): rolled white sleeve and yellow glove. Teal waist layers, charcoal trousers, yellow-soled black sneakers; tiny pale cross clasp on neck band; compact dark quiver/short arrow tips on anatomical left back. BOTH HANDS EMPTY, no handheld weapons or added tools; simplify logos to plain unlettered shapes. Keep asymmetries, head size, mature chibi face, colors and outfit constant.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Clean 2D anime chibi, roughly 2.6 heads tall, crisp colored linework and flat cel shading; adult character translated into chibi, no 3D/PVC/figurine gloss or toddler anatomy..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Greeting loop: paw or limb down, raised, tilted, and returning in a friendly attention gesture.

State requirements:
- Show the greeting through paw, hand, wing, or limb pose only.
- Use the four slots for rest, raised greeting, a small greeting change, and recovery close to the first pose; keep the longer final hold comfortable before returning to idle.
- Do not draw wave marks, motion arcs, lines, sparkles, symbols, or floating effects around the gesture.
- Work within the fixed slot count: clear preparation, readable action peak, and recovery with a coherent last-to-first seam. Keep the same anatomical scale and all identity props attached and present, including at the transition back to canonical idle. Do not add frames, interpolate pixels, or copy a still to simulate a new action.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Harumasa temporal plan (left to right): Four phases: relaxed hand starting to lift; yellow RIGHT hand raised beside shoulder; small friendly open-palm wrist wave; arm lowers close to relaxed position. Subtle easy smile. End near rest rather than peak; no detached motion marks.



## jumping

Create one horizontal animation strip for Codex pet `asaba-harumasa`, state `jumping`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 5 full-body frames in one left-to-right row on flat pure user-selected #FF00FF. Treat the row as 5 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Asaba Harumasa: tousled short dark navy hair/cowlick, golden-yellow eyes, yellow forehead headband and short yellow tails; white shirt, loose dark tie, black harness. Anatomical LEFT (screen-right front): dark tactical sleeve and yellow armband, dark glove. Anatomical RIGHT (screen-left front): rolled white sleeve and yellow glove. Teal waist layers, charcoal trousers, yellow-soled black sneakers; tiny pale cross clasp on neck band; compact dark quiver/short arrow tips on anatomical left back. BOTH HANDS EMPTY, no handheld weapons or added tools; simplify logos to plain unlettered shapes. Keep asymmetries, head size, mature chibi face, colors and outfit constant.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Clean 2D anime chibi, roughly 2.6 heads tall, crisp colored linework and flat cel shading; adult character translated into chibi, no 3D/PVC/figurine gloss or toddler anatomy..
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

Harumasa temporal plan (left to right): Five phases: shallow knee-bend anticipation; boots lift a little; modest airborne peak with knees tucked slightly; descending/legs extend; grounded soft near-upright landing. Constant skull/torso dimensions as canonical idle. Small hop, not a deep squat or huge leap; keep hair/quiver/boots complete and reserve upper headroom. Ground endpoints share baseline; airborne feet rise.



## failed

Create one horizontal animation strip for Codex pet `asaba-harumasa`, state `failed`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 8 full-body frames in one left-to-right row on flat pure user-selected #FF00FF. Treat the row as 8 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Asaba Harumasa: tousled short dark navy hair/cowlick, golden-yellow eyes, yellow forehead headband and short yellow tails; white shirt, loose dark tie, black harness. Anatomical LEFT (screen-right front): dark tactical sleeve and yellow armband, dark glove. Anatomical RIGHT (screen-left front): rolled white sleeve and yellow glove. Teal waist layers, charcoal trousers, yellow-soled black sneakers; tiny pale cross clasp on neck band; compact dark quiver/short arrow tips on anatomical left back. BOTH HANDS EMPTY, no handheld weapons or added tools; simplify logos to plain unlettered shapes. Keep asymmetries, head size, mature chibi face, colors and outfit constant.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Clean 2D anime chibi, roughly 2.6 heads tall, crisp colored linework and flat cel shading; adult character translated into chibi, no 3D/PVC/figurine gloss or toddler anatomy..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Blocked/failed loop: slumped or deflated reaction with sad or closed eyes.

State requirements:
- Show failure through slumped pose, drooping ears/limbs, closed or sad eyes, and lower body position.
- Draw one readable reaction-and-recovery arc within the eight slots, ending near the starting pose. Preserve head size and grounded body scale when bowing or crouching; prefer restrained motion when a dramatic collapse would break the loop or idle transition.
- Tears, small smoke puffs, or tiny stars are allowed only if attached to or overlapping the pet silhouette and kept inside the same frame slot.
- Do not draw red X marks, floating symbols, detached stars, separated smoke clouds, falling tear drops, dust, or other loose effects.
- Work within the fixed slot count: clear preparation, readable action peak, and recovery with a coherent last-to-first seam. Keep the same anatomical scale and all identity props attached and present, including at the transition back to canonical idle. Do not add frames, interpolate pixels, or copy a still to simulate a new action.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Harumasa temporal plan (left to right): Eight standing reaction/recovery phases: calm start; slight surprise; eyebrows soften; small shoulder droop; brief rueful downward look; head starts rising; small resigned smile; calm nearly-neutral finish. No collapse or deep bow, no crying icons, tears, smoke or tools. Close smoothly into idle.



## waiting

Create one horizontal animation strip for Codex pet `asaba-harumasa`, state `waiting`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure user-selected #FF00FF. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Asaba Harumasa: tousled short dark navy hair/cowlick, golden-yellow eyes, yellow forehead headband and short yellow tails; white shirt, loose dark tie, black harness. Anatomical LEFT (screen-right front): dark tactical sleeve and yellow armband, dark glove. Anatomical RIGHT (screen-left front): rolled white sleeve and yellow glove. Teal waist layers, charcoal trousers, yellow-soled black sneakers; tiny pale cross clasp on neck band; compact dark quiver/short arrow tips on anatomical left back. BOTH HANDS EMPTY, no handheld weapons or added tools; simplify logos to plain unlettered shapes. Keep asymmetries, head size, mature chibi face, colors and outfit constant.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Clean 2D anime chibi, roughly 2.6 heads tall, crisp colored linework and flat cel shading; adult character translated into chibi, no 3D/PVC/figurine gloss or toddler anatomy..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Needs-input loop: expectant asking pose for approval, help, or user input.

State requirements:
- Show that Codex needs approval, help, or user input through an expectant asking pose.
- Keep the motion patient and readable, without turning it into ordinary idle or review.
- Work within the fixed slot count: clear preparation, readable action peak, and recovery with a coherent last-to-first seam. Keep the same anatomical scale and all identity props attached and present, including at the transition back to canonical idle. Do not add frames, interpolate pixels, or copy a still to simulate a new action.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Harumasa temporal plan (left to right): Six expectant phases: attentive start; small questioning eyebrow; dark LEFT empty palm turns up at waist; gentle questioning head tilt; palm lowers; expectant near-rest recovery. Both feet planted. Distinct from high greeting and chin-touch work.



## running

Create one horizontal animation strip for Codex pet `asaba-harumasa`, state `running`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure user-selected #FF00FF. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Asaba Harumasa: tousled short dark navy hair/cowlick, golden-yellow eyes, yellow forehead headband and short yellow tails; white shirt, loose dark tie, black harness. Anatomical LEFT (screen-right front): dark tactical sleeve and yellow armband, dark glove. Anatomical RIGHT (screen-left front): rolled white sleeve and yellow glove. Teal waist layers, charcoal trousers, yellow-soled black sneakers; tiny pale cross clasp on neck band; compact dark quiver/short arrow tips on anatomical left back. BOTH HANDS EMPTY, no handheld weapons or added tools; simplify logos to plain unlettered shapes. Keep asymmetries, head size, mature chibi face, colors and outfit constant.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Clean 2D anime chibi, roughly 2.6 heads tall, crisp colored linework and flat cel shading; adult character translated into chibi, no 3D/PVC/figurine gloss or toddler anatomy..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Working loop: focused active-task processing, thinking, typing, scanning, or effortful concentration; not literal foot-running, jogging, sprinting, treadmill motion, raised knees, long steps, pumping arms, or directional travel.

State requirements:
- Show the pet actively working or processing, as if running a task: focused posture, busy hands or paws, purposeful bobbing, thinking motion, tool or prop motion only if already part of the pet identity, or other non-locomotion activity.
- Do not show literal foot-running, jogging, sprinting, treadmill motion, raised knees, long steps, pumping arms, directional travel, speed lines, dust clouds, floor shadows, motion trails, or detached motion effects.
- Work within the fixed slot count: clear preparation, readable action peak, and recovery with a coherent last-to-first seam. Keep the same anatomical scale and all identity props attached and present, including at the transition back to canonical idle. Do not add frames, interpolate pixels, or copy a still to simulate a new action.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Harumasa temporal plan (left to right): Six task-processing phases, NOT foot-running: focused start; yellow RIGHT fingers approach chin; thoughtful chin touch; small considering head turn; hand starts lowering; focused near-rest recovery. Feet planted. No phone, screen, paper or weapon.



## review

Create one horizontal animation strip for Codex pet `asaba-harumasa`, state `review`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure user-selected #FF00FF. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Asaba Harumasa: tousled short dark navy hair/cowlick, golden-yellow eyes, yellow forehead headband and short yellow tails; white shirt, loose dark tie, black harness. Anatomical LEFT (screen-right front): dark tactical sleeve and yellow armband, dark glove. Anatomical RIGHT (screen-left front): rolled white sleeve and yellow glove. Teal waist layers, charcoal trousers, yellow-soled black sneakers; tiny pale cross clasp on neck band; compact dark quiver/short arrow tips on anatomical left back. BOTH HANDS EMPTY, no handheld weapons or added tools; simplify logos to plain unlettered shapes. Keep asymmetries, head size, mature chibi face, colors and outfit constant.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Clean 2D anime chibi, roughly 2.6 heads tall, crisp colored linework and flat cel shading; adult character translated into chibi, no 3D/PVC/figurine gloss or toddler anatomy..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Ready-review loop: focused inspection of completed output with lean, blink, narrowed eyes, head tilt, or paw pose.

State requirements:
- Show review through lean, blink, narrowed eyes, head tilt, or paw/hand position.
- Do not add magnifying glasses, papers, code, UI, punctuation, symbols, or other new props unless they already exist in the base pet identity.
- Work within the fixed slot count: clear preparation, readable action peak, and recovery with a coherent last-to-first seam. Keep the same anatomical scale and all identity props attached and present, including at the transition back to canonical idle. Do not add frames, interpolate pixels, or copy a still to simulate a new action.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Harumasa temporal plan (left to right): Six inspection phases: attentive rest; gaze lowers slightly; short forward head inclination; restrained approving nod; head rises; returns to rest. Hands stay at sides. Distinct from chin-touch work and palm-up waiting. No tool or paper.



## look-cardinals

Create one horizontal four-cardinal anchor strip for Codex pet `asaba-harumasa`.

Use the attached canonical base, completed standard contact sheet, and layout guide for exact identity, style, scale, baseline, face construction, materials, palette, markings, props, and spacing. Read `qa/look-mechanics.md` and use the pet's natural gaze mechanism.

Output exactly four centered complete full-body poses in this exact left-to-right order: `000 up`, `090 screen-right`, `180 down`, `270 screen-left`. Screen-left and screen-right always mean the viewer's image edges, never the character's own left or right.

For `000`, keep the face broadly frontal and point the eyes and natural head mechanism toward the TOP edge. For `090`, put the nose tip, pupils, face surface, or natural aiming feature on the screen-right side of the head center. For `180`, keep the face broadly frontal and point toward the BOTTOM edge. For `270`, apply the inverse screen-left landmark rule. Every cardinal must be unmistakable without labels.

Place one pose in each invisible equal-width slot on a flat pure user-selected #FF00FF background with generous padding. Keep scale, feet/base, lower body, and registration consistent across all four slots.

Harumasa: keep the torso, resting hands, sleeve/glove sides, waist and boots in canonical front-facing positions. Only golden eyes, natural eyelids, head/neck and attached hair/headband tails turn. Four clear poses LEFT TO RIGHT: chin-up and irises UP; nose and eyes clearly SCREEN RIGHT; chin-tucked with irises DOWN and more crown visible; nose and eyes clearly SCREEN LEFT. No closed eyes, full body spinning or tilting whole sprites. Nose/head-center relations must make right and left unmistakable at 192x208. Keep a clear vertical face pitch for up/down. The attached left-back quiver may occlude naturally, never changes side. Draw four complete well-separated bodies with identical head/body size and baseline.

Do not rotate, skew, or tilt the whole sprite to fake gaze. Do not add replacement eyes, labels, degree text, arrows, boxes, guide marks, shadows, scenery, detached effects, or chroma-key colors inside the pet.



## look-row-9

Create one horizontal look-direction strip for Codex pet `asaba-harumasa`, atlas row 9.

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

Place one centered pose in each invisible equal-width slot on flat pure user-selected #FF00FF. Change only the natural parts needed to express gaze: eyes, eyelids, head, face, neck, upper body, appendages, and constrained prop follow-through. Keep identity, silhouette, materials, palette, markings, and props consistent.

ROW-BOUNDARY LOCK: 157.5 must be one even 22.5-degree step before 180. Match the approved 180 pose's body size, baseline, planted anchor, expression, and construction. Preserve the overall right-hand arc, but do not distort pupils, nose, or body geometry merely to exaggerate the subtle horizontal component.

PRE-RETURN CHECK: reject this result if it does not contain eight separated pose groups in the required order; neighboring poses overlap; foreground is cropped at the outer canvas edge; any frame changes sprite scale, body or head size, baseline, or planted-body position; the row visibly reverses into the wrong half of the loop; or 157.5 does not flow evenly into 180. Minor intermediate pupil or nose deviations are not rejection reasons. Exact cell cropping, resizing, and recentering happen deterministically after generation.

Do not rotate, skew, or tilt the whole sprite to fake gaze. Do not add replacement/googly eyes, labels, degree text, arrows, clocks, grids, shadows, glows, scenery, detached effects, or chroma-key colors inside the pet.

## look-row-10

Create one horizontal look-direction strip for Codex pet `asaba-harumasa`, atlas row 10.

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

Place one centered pose in each invisible equal-width slot on flat pure user-selected #FF00FF. Change only the natural parts needed to express gaze: eyes, eyelids, head, face, neck, upper body, appendages, and constrained prop follow-through. Keep identity, silhouette, materials, palette, markings, and props consistent.

ROW-BOUNDARY LOCK: 180 must continue directly from row 9's 157.5, matching its body size, baseline, planted anchor, expression, and construction. 337.5 must be one even 22.5-degree step before 000: nearly up-facing while remaining on the overall left-hand arc. Do not distort pupils, nose, or body geometry merely to exaggerate the subtle horizontal component.

PRE-RETURN CHECK: reject this result if it does not contain eight separated pose groups in the required order; neighboring poses overlap; foreground is cropped at the outer canvas edge; any frame changes sprite scale, body or head size, baseline, or planted-body position; the row visibly reverses into the wrong half of the loop; or 180 does not continue from 157.5 or 337.5 does not flow evenly into 000. Minor intermediate pupil or nose deviations are not rejection reasons. Exact cell cropping, resizing, and recentering happen deterministically after generation.

Do not rotate, skew, or tilt the whole sprite to fake gaze. Do not add replacement/googly eyes, labels, degree text, arrows, clocks, grids, shadows, glows, scenery, detached effects, or chroma-key colors inside the pet.

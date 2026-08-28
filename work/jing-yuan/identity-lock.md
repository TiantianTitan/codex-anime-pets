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

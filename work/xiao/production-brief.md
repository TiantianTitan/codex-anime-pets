# Xiao 2D Pet Production Brief

## Scope

- Produce one local Codex-compatible v2 animated pet for Xiao (魈).
- Deliver 2D only. Do not create a 3D version, install it into Codex, upload it, or publish it.
- Use the five images in `/home/ubuntu23/Bureau/codex-anime-pets/xiao/` as the authoritative visual references.
- Visual target: polished non-pixel chibi sticker illustration, designed to remain readable in a 192 × 208 pet cell.

## Character Direction

Xiao should feel quiet, vigilant, restrained, and lightly aloof rather than cute in an overly cheerful way. Keep his posture compact and poised. Expressions should be subtle but readable at pet scale, with controlled animation arcs and no noisy detached effects.

## Production Contract

- 8 columns × 11 rows; cell size 192 × 208; final atlas 1536 × 2288.
- Rows 0–8: all nine standard Codex animation states with exact required frame counts.
- Rows 9–10: one coherent clockwise 16-pose look loop using the fixed v2 degree order.
- Transparent final background; generation rows use the run-selected chroma key only.
- No text, logos, scenery, floor, cast shadow, glow, speed lines, dust, wave marks, or detached decorative effects.
- Unused cells in standard rows must be fully transparent.
- Package with `spriteVersionNumber: 2` and retain the required QA artifacts.

## Readability and Motion

- Use a large head, compact torso, short limbs, and a stable foot baseline.
- Keep long sash tails close to the body so they do not cross frame boundaries or become detached fragments.
- Do not use the full-size polearm as a persistent prop: it would dominate the cell and create clipping/identity drift. Preserve Xiao through his face, hair, forehead mark, exposed tattooed arm, asymmetrical outfit, jade ornaments, beads, and secured Yaksha mask.
- The Yaksha mask should stay physically attached at the hip/back as a small readable accessory unless a pose naturally brings it near the face; never float it separately.
- Generate running-left independently because the tattoo, glove, costume panels, ornaments, and mask placement are asymmetric.

## State Intent

- `idle`: restrained breathing, small blink, tiny hair/sash follow-through.
- `running-right` / `running-left`: clear alternating chibi sprint with correct screen direction and stable accessories.
- `waving`: brief reserved greeting using the black-gloved right hand; no wave marks.
- `jumping`: crouch, lift, compact apex, descent, soft settle; no dust or landing marks.
- `failed`: shoulders lower and gaze drops, with a controlled deflated reaction; no floating tears, smoke, or stars.
- `waiting`: attentive, slightly expectant posture as if awaiting approval.
- `running`: stationary task-processing action, using a compact talisman/inspection gesture rather than literal locomotion.
- `review`: focused inspection pose, distinct from waiting and task-processing.

## Final Deliverables

- `/home/ubuntu23/Bureau/codex-anime-pets/xiao/xiao-2d/pet.json`
- `/home/ubuntu23/Bureau/codex-anime-pets/xiao/xiao-2d/spritesheet.webp`
- `/home/ubuntu23/Bureau/codex-anime-pets/xiao/xiao-2d/README.md`
- `/home/ubuntu23/Bureau/codex-anime-pets/xiao/xiao-2d.zip`


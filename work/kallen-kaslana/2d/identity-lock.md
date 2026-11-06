# Kallen Kaslana — 2D identity lock

User request: create the 2D edition only from the eight supplied local references. Stable ID `kallen-kaslana`; display name `Kallen`. Production started 2026-11-06. No installation or publishing requested.

## Reference choice

Use the outfit shared by source-originals/Kallen Kaslana3.webp through 8.webp: white pleated dress, black open jacket with red accents, blue chest inset. `reference-01.jpeg` supplies the full-body outfit; `reference-02.webp` supplies face, collar, clips and jacket details. The first two original images show a different armored outfit and must not be mixed into this edition. All eight originals remain locally under references/source-originals.

## Invariants

- Silver-white swept bob fringe, bright blue eyes, one long silver braid, adult character presented as a compact approximately 2.8-head-tall anime chibi.
- Two dark cross/star clips at anatomical right temple (screen-left in the frontal base). Small black cross earring at anatomical left (screen-right in front). Braid emerges behind anatomical left shoulder, normally visible on screen-right from the front. Preserve actual sides in turns.
- White pleated short dress with dark buttons/trim, blue chest insert, black open off-shoulder jacket with red cuff/lining accents, black choker and small red central accent. White thigh-high stockings, black boots with red soles.
- Compact black thigh holster on anatomical left thigh, following the full-body reference. Hands stay free. No drawn pistol, weapon exchange, bullets or effects in this pet.
- Crisp dark linework, restrained flat cel shading, readable facial features; no 3D rendering or white sticker border.
- Calm, brave and warm expression language. Naturally visible eyes remain comfortably open in all six idle frames; expressive eyes may change in other states.

## Motion and registration

- Idle: planted feet, quiet breathing, tiny braid/jacket follow-through; close loop seam.
- Directional movement: two independently generated eight-frame alternating gaits. Asymmetric clips, braid, holster and earring make mirroring inappropriate.
- Greeting: one hand lifts in a short friendly wave and returns. Jump: anticipation, lift, apex, descent, settle; no ground/effects.
- Failed: restrained slumped disappointment; waiting: expectant hands/open attentive face; working: focused thinking/processing while standing; reviewing: deliberate inspecting glance with a thoughtful gesture. No new props.
- Gaze: planted lower body, pupils and eyelids lead; restrained head/neck yaw and pitch, stable face proportions, slight braid follow-through. No whole-body tilt or spinning to indicate gaze.

## Runtime and release

Preview compatibility target is the measured Desktop 26.1007.21434 schedule in docs/pet-compatibility-2026-11-06.md: idle holds 1680,660,660,840,840,1920 ms. This is version-specific evidence, not a guarantee for other versions. Other state previews use source-table timing.

Final 8×11 RGBA atlas: 1536×2288, 192×208 cells, 74 used cells including neutral at row 0 column 6, nine states and sixteen clockwise gaze directions. Independent final review binds the final atlas SHA256. Product folder contains release files and flat ZIP only; QA and source art remain in work.

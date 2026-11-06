# Jingliu · 2D identity lock

User scope: a new 2D Codex Desktop v2 pet. ID `jingliu`, display name `Jingliu`. Product destination: `honkai-star-rail/Jingliu/jingliu-2d`; QA and originals remain in this run. No installation or publication requested.

User interaction preference: all checks stay in the background. Do not open visible browser/inspection windows or steal desktop focus; use file inspection and headless rendering if needed.

## Chosen reference interpretation

Use the unmasked red-eyed design seen in Jingliu3.png, Jingliu7.jpeg, the left figure in Jingliu8.png, and the unmasked chibis in Jingliu5.jpeg. Masked references establish costume, not a second appearance that switches between frames. The chibi reference establishes drawn linework, not cropped bust framing. Generate full-body crisp 2D cel-shaded art, approximately 2.8 heads tall. The sword is present from the base onward.

## Invariants

- Silver-white long hair, pale icy-blue shadows, high half-ponytail with dark blue ribbons, thick side fringe, compact tapered hair masses. Both scarlet eyes remain naturally visible in idle; no blindfold appears.
- Navy/royal-blue bodice, ornate dark collar, central pale circular moon at abdomen, white/pale-blue short pleated skirt, navy rear panels. Bare upper thighs, tall black boots with silver/blue trim, blue detached sleeves and dark gloves.
- Anatomical right (front screen-left): pale flower on upper arm; right hand holds the same compact straight ice-blue sword, pointing down alongside the leg. Keep full tip no lower than foot baseline. Sword remains attached and present through all states.
- Anatomical left (front screen-right): silver shoulder ornament and small red hip bow. Free left hand performs greeting/asking/thinking gestures.
- Keep head shape, eye size, body scale, hair length, costume panels, sword hilt/blade shape, and handedness consistent. No new tools or floating effects. No whole-frame mirroring.

## Motion and runtime

Target timing evidence: Desktop 26.1007.21434, documented 2026-11-06 in repository compatibility and motion-refinement reports. Idle holds [1680,660,660,840,840,1920] ms; other state holds use the documented fixed state table. Three repeats then idle is version-qualified evidence, not a promise about all clients.

Nine standard row counts remain 6/8/8/4/5/8/6/6/6. Allocate clear anticipation, peak and recovery inside that budget. Preserve a close loop seam and a credible state-to-idle transition. Low-amplitude breathing in idle; independent left/right alternating run cycles; greeting with free left hand; compact hop; restrained disappointment; expectant palm; active thoughtful processing; calm inspection. Work is not locomotion.

Jump uses the same anatomical scale as idle, short vertical travel, visible knee compression and recovery. Keep actual generated poses and order; never enlarge a crouch to fill its box or shrink the body to accommodate an excessive arc. Preserve full sword and hair throughout. Check at native 192×208.

## Sources and storage

Eight original files were moved byte-for-byte from the product folder into `references/source-originals/`; references are Git-ignored. AVIF was decoded only for inspection. Working identity inputs are copies of Jingliu3.png, Jingliu5.jpeg, Jingliu8.png. Keep originals after cleanup.

# Dan Heng · Imbibitor Lunae — 2D Codex Pet Production Brief

## Scope

- Produce one local Codex-compatible v2 **2D** animated pet.
- Do not produce a 3D edition in this run.
- Do not install, publish, or upload the pet.
- Deliver a ready-to-use local package, ZIP archive, previews, validation artifacts, and QA records.

## Character reading

The six supplied references depict Dan Heng in his Imbibitor Lunae form from *Honkai: Star Rail*. The pet should read instantly as this character even at desktop-pet scale. The visual interpretation is a premium clean 2D chibi/sticker illustration, not pixel art and not a literal copy of any one reference.

## Identity anchors

1. Near-black blue hair with long layered back locks and a heavy central fringe.
2. Paired translucent teal dragon antlers with small gold filigree accents.
3. Bright cyan/teal eyes, pale skin, pointed Vidyadhara ears, calm reserved expression.
4. White draped outer sleeves over a dark teal-black short outfit.
5. Teal, jade, and muted gold ornamental trim; central lotus/jade-like waist ornament.
6. Dark ankle boots with small gold and teal details.
7. A restrained translucent aqua dragon-tail/water-ribbon silhouette may remain attached to the body, but must never become a detached effect.

## Silhouette and style

- Chibi proportions: oversized head, compact torso, short readable limbs, stable foot baseline.
- Crisp dark teal linework, simplified shapes, clean cel shading, subtle soft highlights.
- Maintain a single consistent drawing style, palette, scale, and body construction across every animation row.
- Use a flat chroma background chosen by the run preparer; no scenery, floor, shadows, pedestal, frame, text, UI, speech bubbles, pets, or detached magical particles.
- Preserve asymmetry consistently: garment panels, ornaments, hair masses, and attached aqua tail/ribbon must not randomly swap sides.

## Motion personality

- Calm, elegant, composed, and slightly aloof rather than bouncy or slapstick.
- Idle: quiet breathing with a small hair/robe settle.
- Running left/right: compact determined travel cycle with clear opposite directionality.
- Waving: restrained greeting with one hand and a small softened expression.
- Jumping: unmistakable launch, airborne apex, descent, and grounded landing; no scale pumping.
- Failed: weary slump or seated/low collapse with continuous body deformation, not disappearing.
- Waiting: patient posture with a tiny glance or garment settle.
- Task-processing `running`: stationary focused casting/working gesture; it must not be another locomotion cycle.
- Review: deliberate inspection/thinking gesture, distinct from waiting and task-processing.

## Directional mechanics

- Rows 9 and 10 form 16 continuous look directions in exact 22.5-degree increments.
- The face/nose projection in viewer coordinates is authoritative: up, screen-right, down, screen-left and all diagonals must be visually distinguishable.
- Hair, ears, antlers, eyes, shoulders, and attached tail/ribbon rotate together as one coherent body.
- No mirrored decorative drift that contradicts head direction.

## Acceptance bar

- Complete 1536×2288, 8×11 atlas with 192×208 cells and `spriteVersionNumber: 2`.
- All nine standard animation rows and both look-direction rows meet their prescribed used-frame counts.
- Transparent background after final chroma removal; no green spill or accidental transparency in the character.
- Every row passes component inspection and visual QA; directional rows additionally pass continuity, semantic, and three-reviewer blind QA.
- Package contains `pet.json`, `spritesheet.webp`, and `README.md`; ZIP contains the same package root.


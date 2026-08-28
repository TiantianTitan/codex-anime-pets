# Zhongli 2D identity lock

## Character invariants

- Humanoid male chibi with an oversized head, compact full body, composed posture, and calm, dignified demeanor.
- Layered dark chocolate-brown hair with warm amber-brown tips, a distinctive two-prong crown tuft, long side bangs, and one thick low ponytail sweeping behind the body.
- Amber-gold eyes with a warm orange inner gradient and narrow, restrained expression language; never recolor them blue, green, red, or purple.
- Exactly one long geometric tassel earring on the character's left ear (viewer-right in front view), built from a dark diamond cap, a small gold accent, and a pale hanging tassel. It remains attached and does not swap sides arbitrarily.
- Formal black, deep-brown, charcoal, ivory, and antique-gold long coat: high collar, angular shoulder panels, fitted dark inner layer, gold diamond/knot motifs at the chest and waist, long split coat tails, dark trousers, and black-gold shoes.
- Warm brown gloves and restrained gold/amber mineral-shaped accents are allowed only when physically attached to the outfit; the stable pet carries no weapon or handheld prop.

## Style lock

- Polished 2D chibi anime sticker illustration.
- Clean dark-brown outlines, readable flat color blocks, restrained soft cel shading, and no painterly, photoreal, plastic, plush, or 3D material.
- Compact full-body silhouette with details enlarged enough to survive a 192×208 cell.
- Keep hair mass, ponytail length, earring, coat tails, gold geometry, palette, lighting, and proportions consistent across all 11 rows.

## Motion rules

- Hair tips, ponytail, earring, and coat tails may lag slightly behind head/body movement, but must stay physically attached and preserve their lengths.
- The demeanor stays controlled and elegant even in energetic actions; use readable body mechanics instead of detached effects.
- Running-left must be generated separately rather than mirrored because the one-sided earring, asymmetric bangs, ponytail sweep, and coat details are identity-sensitive.

## Exclusions

- No spear, meteor, stone pillar, shield, teacup, book, food, slime, geo creature, furniture, scenery, floor, cast shadow, text, watermark, logo, or readable symbol.
- No extra character, duplicate ponytail, second earring, detached tassel, floating ornament, speed line, dust, sparkle, punctuation, aura, glow, or detached rock/VFX.
- No alternate outfit, exposed torso, armor redesign, modern clothing, bright-magenta character pixels, or identity/style drift.

## Reference roles

- `reference-02.jpeg`: primary full-body source for overall proportions, long coat structure, trousers, shoes, ponytail length, and black/brown/gold palette.
- `reference-04.jpeg`: primary face and upper-body source for amber eyes, crown tuft, layered bangs, viewer-right earring placement, shoulder construction, chest geometry, and clean sticker rendering.
- `reference-03.jpeg`: supporting confirmation of hair silhouette, folded-arm glove color, coat collar, earring, and ponytail; use only when an extra identity view is useful.
- `reference-01.jpeg`: expression and persona reference only. Because it is a four-pose collage with situational props and alternate crops, it is deliberately omitted from normal grounded generation jobs to avoid multi-character or prop contamination.

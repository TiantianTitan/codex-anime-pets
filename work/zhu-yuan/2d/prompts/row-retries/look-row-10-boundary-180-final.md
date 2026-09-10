# Zhu Yuan look row 10 — 157.5 to 180 boundary repair

Regenerate the complete row as one coherent 8-pose strip. Preserve the currently approved left-half direction sequence, but repair the first pose and the early ponytail crossover so row 9 flows into row 10 without a mirrored hairstyle snap.

## Output contract

- Exactly 8 complete, separated, full-body Zhu Yuan sprites on one perfectly flat uniform `#00FF00` horizontal strip.
- Preserve canonical identity, red-orange front streak, high side ponytail, red tie, face, outfit, armor, holster, sidearm, proportions, clean cel shading, and character-side asymmetry.
- Every complete crown-to-sole silhouette must be approximately 425–440 px tall, with a consistent size across all 8 poses and ample green above the crown. Source-row vertical position may be anywhere safe; deterministic assembly will align the shoe baseline.
- No text, labels, guides, shadows, particles, detached effects, extra props, overlap, or crop.

## Exact sequence and repaired boundary

1. **180 down** — use the approved 180 cardinal pose family from the four-cardinal reference: centered frontal/down, chin tucked, irises low. Crucially, the large high ponytail and red tie remain on the same IMAGE-LEFT/rear side visible in row-9 pose 157.5 and in the approved 180 anchor. Do not mirror or swap this hairstyle arrangement.
2. **202.5 down-left** — one gentle step after 180. Face begins toward IMAGE-LEFT while staying down. Ponytail starts passing behind the crown toward center; it must not teleport from one side to the other.
3. **225 down-left** — clear down-left three-quarter view. Nose/facial plane are on IMAGE-LEFT; ponytail crossover progresses gradually behind the head toward image-right.
4. **247.5 down-left** — stronger down-left near-profile, already in the same family as 270; ponytail clearly trails behind on image-right.
5. **270 left** — unmistakable IMAGE-LEFT profile, ponytail behind on image-right.
6. **292.5 up-left** — keep the left-facing family and begin lifting chin/irises.
7. **315 up-left** — reopen smoothly toward front/up-left; keep the center and ponytail motion incremental rather than jumping.
8. **337.5 up-left** — near-frontal up-left one step before approved 000; compatible scale, face, and ponytail arrangement.

## Non-negotiable gates

- Reject if slot 1 reverses the approved 180 hairstyle asymmetry or flips the ponytail/red tie relative to row-9 157.5.
- Reject if slot 1 is a broad neutral front pose instead of a deep frontal/down cardinal.
- Reject if the ponytail jumps sides at 157.5→180, 180→202.5, or 202.5→225 instead of moving gradually behind the crown.
- Reject if slots 2–4 point image-right, if 270 is ambiguous, or if slots 6–8 reverse toward image-right.
- Reject if any silhouette exceeds 440 px crown-to-sole, touches an outer crop, changes scale/baseline family, or breaks identity/equipment attachment.

All screen directions are viewer coordinates. IMAGE-LEFT means the left edge of the output canvas. Draw all eight poses together; do not paste or independently replace a single cell.

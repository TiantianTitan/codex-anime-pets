# Seele Vollerei — 16-direction look mechanics

## Character lock

- Keep the approved classic short-haired Seele design from `references/canonical-base.png`: chin-length blue-black bob with cobalt-violet tips, bright blue eyes, white short sleeves, deep-cobalt fitted vest dress, layered navy-violet butterfly skirt, white thigh-highs, and dark Mary Jane shoes.
- Never introduce the long-haired armored alternate costume, a rifle, a scythe, detached butterflies, readable text, glow, scenery, guide marks, or motion effects.
- Preserve the approved chibi proportions, line weight, rendering, baseline, overall scale, and centered full-body framing from `qa/contact-sheet.png`.

## Motion hierarchy

1. The gaze leads each turn: iris position and visible eye shape must clearly identify the requested screen direction.
2. The chin follows with a small pitch change. Looking up exposes slightly more lower face and neck; looking down tucks the chin and lowers the irises.
3. Head yaw follows the gaze. The nose, cheek plane, nearer eye, ear region, and bob silhouette must rotate continuously instead of switching sides between neighboring frames.
4. Shoulders may counter-rotate only a few degrees for a natural result. The torso, hips, legs, shoes, and foot baseline stay essentially anchored.
5. Hair tips may lag the head subtly, but the bob must remain attached and coherent. The skirt, hands, and arms stay quiet.

## Cardinal landmarks

- `000 up`: broad near-front view; both eyes readable; irises high; chin lifted. This is UP, not neutral front.
- `090 screen-right`: nose, pupils, facial plane, and nearer cheek project toward image-right; the rear side of the bob remains on image-left. This is the unmistakable RIGHT anchor.
- `180 down`: broad near-front view; irises low; eyelids and tucked chin clearly communicate DOWN. Do not turn the back toward the viewer.
- `270 screen-left`: nose, pupils, facial plane, and nearer cheek project toward image-left; the rear side of the bob remains on image-right. This is the unmistakable LEFT anchor.

## Clockwise interpolation

- Advance in equal 22.5-degree visual steps: `000 → 022.5 → 045 → 067.5 → 090 → 112.5 → 135 → 157.5 → 180 → 202.5 → 225 → 247.5 → 270 → 292.5 → 315 → 337.5 → 000`.
- Row 9 must travel smoothly from UP through screen-right to near-DOWN with a slight remaining screen-right cue at `157.5`.
- Row 10 must start at the approved DOWN family, continue through screen-left, and reopen upward while remaining on the left-facing half. `337.5` is one small step before the approved `000` UP pose.
- Neighboring frames may not reverse yaw, jump from profile to broad front, swap hair sides, change costume asymmetry, or pop in apparent head/body scale.

## Registration and rejection gates

- Keep one stable shoe baseline and near-constant head/body scale in all 16 cells. Pitch is expressed through eyes, chin, and restrained head rotation—not by lifting, shrinking, or tilting the whole character.
- Leave safe transparent margins after extraction; no hair, skirt, fingers, or shoes may touch a cell edge.
- Reject a row if `090` does not face image-right, `270` does not face image-left, `180` reads as a back view, or `337.5 → 000` creates a conspicuous scale, height, center, hair-side, or yaw snap.
- All eight poses in each row must be synthesized as one coherent full strip. Do not assemble individually generated direction cells into the product atlas.

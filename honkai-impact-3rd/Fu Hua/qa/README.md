# Fu Hua 2D QA summary

- Final visual QA: PASS; no animation row requires further repair.
- Atlas: WEBP RGBA, 1536×2288, 8×11, 192×208 cells, `spriteVersionNumber: 2`.
- Mechanical validation: 0 errors and 0 warnings; transparency, chroma cleanup, unused cells, and v2 layout all pass.
- All nine standard rows were reviewed frame by frame at normal pet size. Framing, scale, baselines, identity details, and attachments remain stable.
- The jumping row uses stable-slot extraction to preserve a clear low-to-high-to-low arc without camera zoom or clipping.
- Three isolated blind reviewers confirmed both hard cardinal pairs by strict majority. Ambiguous secondary-axis cues at several diagonal directions are retained as review warnings; the ordered loop has no reversal.
- All published GIF previews were rebuilt from the final cleaned and validated atlas.

The original character references remain only under the locally ignored work directory and are not part of this public release.

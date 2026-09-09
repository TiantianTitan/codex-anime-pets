# Bronya Zaychik 2D — QA record

This folder contains the publishable verification artifacts for the finished Codex pet. The original character references remain local under the ignored `work/` tree and are not included here.

## Visual review

- `contact-sheet.png` — all nine standard animation rows plus the sixteen look directions.
- `direction-qa.png` — neutral pose and the complete labeled clockwise direction loop.
- `previews/` — nine GIFs rendered from the cleaned final atlas.

## Deterministic checks

- `atlas-validation.json` and `package-validation.json` — v2 dimensions, cell layout, transparency, used cells, and unused cells.
- `despill.json` — the single edge-local chroma cleanup record.
- `standard-row-validation.json` — extracted standard-frame checks.
- `look-continuity.json` — adjacent-direction measurements and reviewed warnings.

## Direction checks

- `cardinal-anchors.json` — deterministic extraction of up, right, down, and left anchors.
- `direction-semantics.json` — labeled visual verdict for all sixteen directions.
- `direction-blind-pairs.png` — randomized unlabeled A/B challenges.
- `direction-blind-verdicts-1.json` through `-3.json` — three isolated reviews.
- `direction-blind-verdicts.json` and `direction-blind-validation.json` — strict-majority result and hidden-key validation.

`final-visual-qa.json` and `run-summary.json` record the final acceptance decision and packaged output.

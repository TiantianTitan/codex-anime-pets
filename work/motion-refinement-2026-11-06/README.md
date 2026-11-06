# Fixed-frame motion refinement · 2026-11-06

This directory preserves the sources and review evidence for the 18-edition,
29-row update. The published comparison is
[docs/pet-motion-refinement.html](../../docs/pet-motion-refinement.html).

`inventory.json` records baseline commit
`c72f04ddea89ff4a403803b2c4e39de237ee3ad5`. Candidate status fields and
`release-validation.json`'s `committed_or_pushed: false` record the time those
files were produced; they are historical snapshots, not the current Git status.
Final acceptance is recorded in `technical-validation.json`,
`qa-independent-a.json`, `qa-independent-b.json`, and `release-validation.json`.
Their original bytes are retained because approvals bind their SHA-256 hashes.

Retained artifacts include all final candidates, the 29 changed rows' original
strips, extraction/registration manifests, seven selected generated source
images and final prompts, and the final review evidence. Unchanged baseline
strips, full audit contact sheets, obsolete browser captures and unused prompt
templates remain local and are excluded from this commit. Original character
reference images remain excluded under the repository's existing policy.

To rebuild the public comparison from the repository root, with Pillow installed:

```sh
python3 scripts/build_motion_refinement_comparison.py --public
```

The other scripts record the original production workflow. They use the local
`hatch-pet` skill and, in some cases, workstation runtime paths. Audit, candidate
building, validation and publishing were run before the release was applied;
do not rerun them directly against an already updated checkout. In particular,
`publish.py` requires the baseline hashes and intentionally rejects a second
application. The original baseline can be recovered from the Git commit above.

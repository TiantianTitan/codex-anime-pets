# Standard-row extraction decisions

- `jumping`: `stable-slots` approved after the source strip was visually reviewed. The source keeps a near-constant character scale and contains a genuine low → rise → peak → descent → settle trajectory; per-component normalization erased that height change and introduced scale popping.
- `failed`: `stable-slots` approved after source-strip review. The source keeps a stable drawn scale while the body slumps and recovers; per-component normalization enlarged the crouched frames.
- All other standard rows use component-based `auto` extraction.
- Both corrected rows must still pass deterministic inspection and independent GIF playback review before the standard atlas is accepted.

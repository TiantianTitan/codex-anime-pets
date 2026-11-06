"""Reconstruct standard frames from retained generated strips; audit final cleanup."""
import hashlib
import importlib.util
import json
from pathlib import Path
from PIL import Image

RUN = Path(__file__).resolve().parents[1]
SCRIPT = Path("/home/ubuntu23/.codex/skills/hatch-pet/scripts/extract_strip_frames.py")
spec = importlib.util.spec_from_file_location("extract_strip", SCRIPT)
extract = importlib.util.module_from_spec(spec)
spec.loader.exec_module(extract)
manifest = json.loads((RUN / "frames/frames-manifest.json").read_text())
preclean = Image.open(RUN / "qa/atlas-pre-despill.png").convert("RGBA")
final_path = RUN / "final/spritesheet-extended.webp"
final = Image.open(final_path).convert("RGBA")
rows = []
for row, (state, count) in enumerate(extract.ROW_FRAME_COUNTS.items()):
    record = next(r for r in manifest["rows"] if r["state"] == state)
    source = Path(record["source"])
    assert hashlib.sha256(source.read_bytes()).hexdigest() == record["source_sha256"], state
    assert record["method"] == "stable-slots", state
    strip = extract.remove_chroma_background(Image.open(source), (0, 255, 0), 96)
    reconstructed = extract.extract_stable_slot_frames(strip, count)
    checks = []
    for column, frame in enumerate(reconstructed):
        saved = Image.open(RUN / "frames" / state / f"{column:02d}.png").convert("RGBA")
        assert frame.tobytes() == saved.tobytes(), (state, column, "extraction changed")
        # Composition uses alpha_composite onto an empty cell, clearing hidden RGB.
        composed = Image.new("RGBA", (192, 208))
        composed.alpha_composite(frame)
        box = (column * 192, row * 208, (column + 1) * 192, (row + 1) * 208)
        assert composed.tobytes() == preclean.crop(box).tobytes(), (state, column, "assembly changed")
        assert composed.getchannel("A").tobytes() == final.crop(box).getchannel("A").tobytes(), (state, column, "alpha changed")
        checks.append({"column": column, "source_frame": column, "frame_rgba_sha256": hashlib.sha256(frame.tobytes()).hexdigest(), "exact_extraction_and_precleanup_assembly": True, "final_alpha_unchanged": True})
    rows.append({"state": state, "source": str(source.relative_to(RUN)), "source_sha256": record["source_sha256"], "method": "stable-slots", "chroma_threshold": 96, "frames": checks})
assembler_path = SCRIPT.with_name("assemble_extended_atlas.py")
spec = importlib.util.spec_from_file_location("assemble_extended", assembler_path)
assembler = importlib.util.module_from_spec(spec)
spec.loader.exec_module(assembler)
scale = json.loads((RUN / "qa/look-row-9-registration.json").read_text())["scale"]
neutral = assembler.load_neutral_cell(RUN / "frames/idle/00.png", preclean, (0, 255, 0), 96)
jobs = json.loads((RUN / "imagegen-jobs.json").read_text())["jobs"]
look_checks = []
for row in (9, 10):
    source = RUN / "decoded" / f"look-row-{row}.png"
    source_sha = hashlib.sha256(source.read_bytes()).hexdigest()
    assert source_sha == next(j for j in jobs if j["id"] == f"look-row-{row}")["source_sha256"]
    cells = assembler.extract_row_strip_cells(source, (0, 255, 0), 96)
    cells = assembler.normalize_cells_to_reference(cells, neutral, scale)
    for column, cell in enumerate(cells):
        composed = Image.new("RGBA", (192, 208))
        composed.alpha_composite(cell)
        composed = assembler.clear_transparent_rgb(composed)
        box = (column * 192, row * 208, (column + 1) * 192, (row + 1) * 208)
        assert composed.tobytes() == preclean.crop(box).tobytes(), (row, column, "registered row reconstruction mismatch")
    look_checks.append({"row": row, "source": str(source.relative_to(RUN)), "source_sha256": source_sha, "shared_scale": scale, "ordered_complete_source_groups": 8, "exact_precleanup_reconstruction": True})
assert preclean.getchannel("A").tobytes() == final.getchannel("A").tobytes(), "cleanup changed atlas alpha"
report = {"ok": True, "atlas_sha256": hashlib.sha256(final_path.read_bytes()).hexdigest(), "extractor_sha256": hashlib.sha256(SCRIPT.read_bytes()).hexdigest(), "assembler_sha256": hashlib.sha256(assembler_path.read_bytes()).hexdigest(), "standard_source_frames_verified": sum(len(r["frames"]) for r in rows), "look_source_frames_verified": 16, "whole_atlas_alpha_unchanged_by_final_cleanup": True, "mapping": "generated source order preserved; no frame reordering or duplicate-hold substitution", "rows": rows, "look_rows": look_checks}
(RUN / "qa/source-reconstruction.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({key: report[key] for key in ("ok", "atlas_sha256", "standard_source_frames_verified", "whole_atlas_alpha_unchanged_by_final_cleanup")}))

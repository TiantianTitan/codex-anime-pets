"""Produce three review candidates from intact original strips; never edit releases."""
from pathlib import Path
import hashlib
import importlib.util
import json

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "work/motion-refinement-2026-11-06/reextracted-genshin-others"
SKILL_SCRIPTS = Path("/home/ubuntu23/.codex/skills/hatch-pet/scripts")


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


extract = module("extract", SKILL_SCRIPTS / "extract_strip_frames.py")
despill = module("despill", SKILL_SCRIPTS / "despill_chroma_edges.py")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def row_strip(frames):
    result = Image.new("RGBA", (192 * len(frames), 208))
    for index, frame in enumerate(frames):
        result.alpha_composite(frame, (index * 192, 0))
    return result


jobs = [
    ("mitsuri-kanroji", "jumping", "others/mitsuri-kanroji/mitsuri-kanroji-2d/spritesheet.webp", 4, [0, 1, 2, 3, 4]),
    ("mitsuri-kanroji", "failed", "others/mitsuri-kanroji/mitsuri-kanroji-2d/spritesheet.webp", 5, [6, 1, 2, 3, 4, 3, 2, 1]),
    ("obanai", "jumping", "others/obanai-iguro/obanai-2d/spritesheet.webp", 4, [0, 1, 2, 3, 4]),
]
manifest = {
    "status": "candidate-awaiting-independent-review",
    "release_assets_modified": False,
    "script": str(Path(__file__).relative_to(ROOT)),
    "script_sha256": sha(Path(__file__)),
    "helpers": {p.name: {"path": str(p), "sha256": sha(p)} for p in [SKILL_SCRIPTS / "extract_strip_frames.py", SKILL_SCRIPTS / "despill_chroma_edges.py"]},
    "rows": [],
}

for pet_id, state, atlas_path, atlas_row, mapping in jobs:
    source = ROOT / "work" / pet_id / "2d/decoded" / f"{state}.png"
    request = ROOT / "work" / pet_id / "2d/pet_request.json"
    key_hex = json.loads(request.read_text())["chroma_key"]["hex"]
    key = extract.parse_hex_color(key_hex)
    with Image.open(source) as opened:
        strip = extract.remove_chroma_background(opened, key, 96.0)
    count = extract.ROW_FRAME_COUNTS[state]
    groups = extract.component_frame_groups(strip, count)
    if groups is None:
        raise RuntimeError(f"Cannot identify all complete source poses for {pet_id}/{state}")
    boxes = [extract.component_bounds(group) for group in groups]
    shared_top = max(0, min(box[1] for box in boxes) - 4)
    shared_bottom = min(strip.height, max(box[3] for box in boxes) + 4)
    viewport_width = max(box[2] - box[0] for box in boxes) + 8
    viewport_height = shared_bottom - shared_top
    shared_scale = min(182 / viewport_width, 198 / viewport_height, 1.0)
    frames = extract.extract_stable_slot_frames(strip, count)
    chosen = [frames[index] for index in mapping]
    ground_shifts = [0] * count
    if state == "failed":
        # This reaction keeps its feet on the ground: remove small source-drawing
        # baseline variation while preserving its common scale and crouch height.
        # Never apply this to jumping, where source vertical motion is intentional.
        grounded = []
        for index, frame in enumerate(chosen):
            box = frame.getchannel("A").point(lambda value: 255 if value > 16 else 0).getbbox()
            ground_shifts[index] = 203 - box[3]
            canvas = Image.new("RGBA", (192, 208))
            canvas.alpha_composite(frame, (0, ground_shifts[index]))
            grounded.append(canvas)
        chosen = grounded
    before_cleanup = row_strip(chosen)
    candidate, cleanup = despill.decontaminate_image(before_cleanup, chroma_key=key)
    folder = OUT / pet_id
    folder.mkdir(parents=True, exist_ok=True)
    candidate_path = folder / f"{state}.png"
    candidate.save(candidate_path)
    row_strip(frames).save(folder / f"{state}-source-order.png")
    with Image.open(ROOT / atlas_path) as opened:
        atlas = opened.convert("RGBA")
    before = atlas.crop((0, atlas_row * 208, count * 192, (atlas_row + 1) * 208))
    contact = Image.new("RGB", (count * 192, 480), "#ece8e2")
    draw = ImageDraw.Draw(contact)
    draw.text((8, 8), f"{pet_id} / {state}: current release (native 192 x 208 cells)", fill="#222222")
    contact.paste(before, (0, 30), before)
    draw.text((8, 248), f"CANDIDATE / common source scale, y trajectory retained / source frame order {mapping}", fill="#222222")
    contact.paste(candidate, (0, 270), candidate)
    contact_path = folder / f"{state}-before-after.png"
    contact.save(contact_path)
    frames_after = [candidate.crop((index * 192, 0, (index + 1) * 192, 208)) for index in range(count)]
    bounds_after = [frame.getchannel("A").point(lambda value: 255 if value > 16 else 0).getbbox() for frame in frames_after]
    # Structural checks only. The implementing agent cannot approve final visual quality.
    assert candidate.size == (192 * count, 208)
    assert all(box is not None and box[0] >= 2 and box[1] >= 2 and box[2] <= 190 and box[3] <= 206 for box in bounds_after)
    assert candidate.getchannel("A").tobytes() == before_cleanup.getchannel("A").tobytes()
    manifest["rows"].append({
        "id": pet_id, "state": state, "atlas_row": atlas_row,
        "original_atlas": atlas_path, "original_atlas_sha256": sha(ROOT / atlas_path),
        "source": str(source.relative_to(ROOT)), "source_sha256": sha(source),
        "source_size": list(strip.size), "source_request": str(request.relative_to(ROOT)),
        "chroma_key": key_hex, "key_threshold": 96.0,
        "method": "extract_stable_slot_frames: complete component groups; common viewport and common scale",
        "source_group_bboxes": [list(box) for box in boxes],
        "source_group_pixel_counts": [sum(component["area"] for component in group) for group in groups],
        "shared_source_viewport": {"top": shared_top, "bottom": shared_bottom, "width": viewport_width, "height": viewport_height},
        "shared_scale": shared_scale, "source_frame_mapping": mapping,
        "positioning": "Each complete source group centered horizontally in one shared-width viewport. Jumping retains source y offsets from shared_top without foot alignment. Failed uses small translation-only ground-baseline correction after common-scale extraction; no frame is independently scaled.",
        "nonjump_ground_translation_dy_px": ground_shifts,
        "despill_passes": 1, "despill_report": cleanup,
        "candidate": str(candidate_path.relative_to(ROOT)), "candidate_sha256": sha(candidate_path),
        "candidate_bounds_alpha_gt_16": bounds_after,
        "before_after": str(contact_path.relative_to(ROOT)),
        "structural_checks": {"all_frames_nonempty": True, "no_cell_edge_contact": True, "despill_alpha_preserved": True},
        "independent_visual_review": "pending",
    })
    print(pet_id, state, "scale", round(shared_scale, 6), "bounds", bounds_after, flush=True)

(OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
print(OUT / "manifest.json")

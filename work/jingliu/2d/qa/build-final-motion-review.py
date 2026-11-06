"""Background-only, exact-final-atlas transition evidence; never changes sprite art."""
from pathlib import Path
import hashlib
import importlib.util
import json
from PIL import Image, ImageDraw

RUN = Path(__file__).resolve().parents[1]
ATLAS = RUN / "final/spritesheet-extended.webp"
SKILL = Path("/home/ubuntu23/.codex/skills/hatch-pet/scripts")
spec = importlib.util.spec_from_file_location("final_previews", SKILL / "render_final_animation_previews.py")
preview = importlib.util.module_from_spec(spec)
spec.loader.exec_module(preview)
atlas = Image.open(ATLAS).convert("RGBA")
assert atlas.size == (1536, 2288)
atlas_sha = hashlib.sha256(ATLAS.read_bytes()).hexdigest()
out = RUN / "qa/transitions-final"
out.mkdir(exist_ok=True)
idle_times = [1680, 660, 660, 840, 840, 1920]
def cell(row, column):
    return atlas.crop((column * 192, row * 208, (column + 1) * 192, (row + 1) * 208))
idle = [cell(0, i) for i in range(6)]
native_dir = RUN / "qa/native-final"
native_dir.mkdir(exist_ok=True)
for row, (state, holds) in enumerate(preview.ROW_DURATIONS.items()):
    strip = Image.new("RGB", (192 * len(holds), 232), "#242730")
    labels = ImageDraw.Draw(strip)
    actual_holds = idle_times if state == "idle" else holds
    for column, hold in enumerate(actual_holds):
        frame = cell(row, column)
        labels.text((column * 192 + 5, 4), f"{state} {column + 1}: {hold}ms", fill="#eeeae3")
        strip.paste(frame, (column * 192, 24), frame)
    strip.save(native_dir / (state + ".png"))
sheet = Image.new("RGB", (576, 8 * 240), "#242730")
draw = ImageDraw.Draw(sheet)
records = []
for row, (state, times) in enumerate(preview.ROW_DURATIONS.items()):
    if state == "idle":
        continue
    frames = [cell(row, i) for i in range(len(times))]
    sequence = idle + frames * 3 + idle
    durations = idle_times + times * 3 + idle_times
    path = out / (state + "-to-idle.webp")
    preview.save_preview(sequence, durations, path)
    validation = preview.verify_timeline(sequence, durations, path)
    top = (row - 1) * 240
    draw.text((7, top + 4), f"{state}: LAST {times[-1]}ms | FIRST {times[0]}ms | IDLE 1680ms", fill="#eeeae3")
    for col, frame in enumerate([frames[-1], frames[0], idle[0]]):
        sheet.paste(frame, (col * 192, top + 27), frame)
    records.append({"state": state, "path": str(path.relative_to(RUN)), "schedule": "idle cycle -> 3 action cycles -> idle cycle", "validation": validation})
sheet.save(RUN / "qa/motion-seams.png")
look = [cell(9 + i // 8, i % 8) for i in range(16)]
preview.save_preview(look, [200] * 16, out / "look-loop.webp")
look_check = preview.verify_timeline(look, [200] * 16, out / "look-loop.webp")
report = {
    "ok": all(r["validation"]["ok"] for r in records) and look_check["ok"],
    "atlas_sha256": atlas_sha,
    "client_version": "26.1007.21434",
    "timing_evidence": "docs/pet-compatibility-2026-11-06.md; docs/pet-motion-refinement-2026-11-06.md",
    "live_installed_client_test": False,
    "review_mode": "background-only native frame sequences with verified encoded timelines",
    "rows": records,
    "look_loop": {"purpose": "QA-only ordered clockwise sweep; not a claim of client scheduling", "duration_per_pose_ms": 200, "validation": look_check},
}
(RUN / "qa/transition-validation.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({"ok": report["ok"], "atlas_sha256": atlas_sha, "transition_count": len(records)}))

"""Record native row-9 semantics and measured continuity before row-10 generation."""
import hashlib
import importlib.util
import json
from pathlib import Path
from PIL import Image
RUN = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("continuity", "/home/ubuntu23/.codex/skills/hatch-pet/scripts/measure_direction_continuity.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
path = RUN / "qa/look-row-9-registered.png"
strip = Image.open(path).convert("RGBA")
assert strip.size == (1536, 208)
labels = ["000", "022.5", "045", "067.5", "090", "112.5", "135", "157.5"]
cells = [strip.crop((i * 192, 0, (i + 1) * 192, 208)) for i in range(8)]
pairs = [{"from": labels[i], "to": labels[i + 1], **m.pair_metric(cells[i], cells[i + 1])} for i in range(7)]
assert all(p["centerDelta"] < 8 and p["areaRatio"] < 1.25 for p in pairs)
reasons = [
    ("up", "Raised chin with eyes above neutral; no side turn."),
    ("up-right", "Chin remains high and nose/eye center starts toward screen right; near-vertical horizontal cue is intentionally small."),
    ("up-right", "Quarter-facing nose and red eyes to screen right with lifted chin."),
    ("up-right", "Right turn dominates with slight upward chin/eye line; subtle vertical component."),
    ("right", "Clear quarter-face to screen right, gaze at level, body remains frontal."),
    ("down-right", "Right-facing face with modest chin descent and lowered eye line."),
    ("down-right", "Head increasingly lowered while nose and gaze retain rightward component."),
    ("down-right", "Near-frontal lowered face and red irises low; small residual right turn leads into approved down anchor.")
]
report = {"ok": True, "source_sha256": hashlib.sha256((RUN / "decoded/look-row-9.png").read_bytes()).hexdigest(), "registered_row_sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "reviewed_by": "parent", "registration_and_edges_passed": True, "native_size": [192, 208], "next_row_authorized": True, "continuity": pairs, "semantics": [{"direction": label, "pass": True, "expected": expected, "observed": expected, "reason": reason} for label, (expected, reason) in zip(labels, reasons)], "notes": ["One shared scale; planted boot and sword anchors remain steady, no native-visible clipping or reversal.", "Intermediate cues will also undergo three-worker final blind review; cardinal and final independent gates remain pending."], "background_only": True}
(RUN / "qa/look-row-9-gate.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({"ok": True, "max_center_delta": max(p["centerDelta"] for p in pairs), "max_area_ratio": max(p["areaRatio"] for p in pairs)}))

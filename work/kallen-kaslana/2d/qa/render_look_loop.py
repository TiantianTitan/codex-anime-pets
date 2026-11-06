"""Render ordered native-size QA playback from the exact final atlas, without new art."""

import argparse
import hashlib
import json
import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, "/home/ubuntu23/.codex/skills/hatch-pet/scripts")
from render_final_animation_previews import save_preview, verify_timeline


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--atlas", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    source = Path(args.atlas).resolve()
    output = Path(args.output_dir).resolve()
    output.mkdir(parents=True, exist_ok=True)
    with Image.open(source) as opened:
        atlas = opened.convert("RGBA")
    if atlas.size != (1536, 2288):
        raise SystemExit("QA look playback requires the final v2 atlas")
    frames = []
    for index in range(16):
        row, column = 9 + index // 8, index % 8
        frames.append(atlas.crop((column * 192, row * 208, (column + 1) * 192, (row + 1) * 208)))
    durations = [180] * 16
    path = output / "look-directions.webp"
    save_preview(frames, durations, path)
    report = {
        "atlas_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "source": str(source),
        "preview": str(path),
        "cell_size": [192, 208],
        "direction_order_degrees": [index * 22.5 for index in range(16)],
        "timing_basis": "180 ms per direction for ordered QA inspection only; no claim about client pointer scheduling",
        "verification": verify_timeline(frames, durations, path),
    }
    (output / "look-playback-validation.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

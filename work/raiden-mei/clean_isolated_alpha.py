#!/usr/bin/env python3
"""Remove disconnected alpha islands from extracted pet frames.

The generated strips occasionally place a clipped piece of a neighbouring
sprite inside a slot.  The actual mascot is the largest 8-connected alpha
component, so keeping that component removes the fragment without repainting
or altering the mascot itself.
"""

from __future__ import annotations

import argparse
import json
from collections import deque
from pathlib import Path

from PIL import Image


def components(alpha: Image.Image) -> list[list[tuple[int, int]]]:
    width, height = alpha.size
    pixels = alpha.load()
    seen: set[tuple[int, int]] = set()
    result: list[list[tuple[int, int]]] = []
    for y in range(height):
        for x in range(width):
            if pixels[x, y] == 0 or (x, y) in seen:
                continue
            queue = deque([(x, y)])
            seen.add((x, y))
            component: list[tuple[int, int]] = []
            while queue:
                px, py = queue.popleft()
                component.append((px, py))
                for nx in range(px - 1, px + 2):
                    for ny in range(py - 1, py + 2):
                        if (
                            0 <= nx < width
                            and 0 <= ny < height
                            and pixels[nx, ny] > 0
                            and (nx, ny) not in seen
                        ):
                            seen.add((nx, ny))
                            queue.append((nx, ny))
            result.append(component)
    return result


def clean(path: Path) -> dict[str, object]:
    image = Image.open(path).convert("RGBA")
    found = components(image.getchannel("A"))
    if not found:
        raise ValueError(f"no visible sprite pixels in {path}")
    found.sort(key=len, reverse=True)
    keep = set(found[0])
    removed = sum(len(component) for component in found[1:])
    if removed:
        pixels = image.load()
        for component in found[1:]:
            for x, y in component:
                pixels[x, y] = (0, 0, 0, 0)
        image.save(path)
    return {
        "path": str(path),
        "components_before": len(found),
        "kept_pixels": len(keep),
        "removed_pixels": removed,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--frames-root", type=Path, required=True)
    parser.add_argument("--json-out", type=Path, required=True)
    args = parser.parse_args()

    frame_paths = sorted(
        path
        for path in args.frames_root.glob("*/*.png")
        if path.parent.name != "look-directions"
    )
    report = {"ok": True, "frames": [clean(path) for path in frame_paths]}
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

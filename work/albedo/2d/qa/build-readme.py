"""Rebuild only Albedo's README assets, leaving approved existing art untouched."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[4]
QA = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "scripts"))
import build_readme_showcase as showcase

ATLAS = ROOT / "genshin-impact/Albedo/albedo-2d/spritesheet.webp"
APPROVED_ATLAS = "590421dbef7d966819fc5c6cebf8466eb46d7c68e80e097e76bf324d77e7d02d"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--locale", choices=showcase.LOCALES)
    args = parser.parse_args()
    assert sha(ATLAS) == APPROVED_ATLAS, "Approved product changed"
    if args.locale:
        showcase.build_arrivals(args.locale)
        showcase.build_collection_wall(args.locale)
        print(f"Updated arrivals and collection: {args.locale}", flush=True)
        return

    dynamic_paths = {
        "assets/readme/" + showcase.localized_asset_name(asset, locale)
        for asset in ("new-arrivals-stage.webp", "character-collection-wall.webp")
        for locale in showcase.LOCALES
    }
    new_paths = {
        "assets/readme/idle/albedo.webp",
        "assets/readme/archive-previews/albedo.webp",
    }
    baseline_path = QA / "readme-protected-assets.json"
    if not baseline_path.exists():
        protected = {
            path.relative_to(ROOT).as_posix(): sha(path)
            for path in sorted((ROOT / "assets/readme").rglob("*"))
            if path.is_file()
            and path.relative_to(ROOT).as_posix() not in dynamic_paths | new_paths
        }
        baseline_path.write_text(json.dumps(protected, indent=2) + "\n")
        before = {path: sha(ROOT / path) for path in sorted(dynamic_paths)}
        (QA / "readme-dynamic-assets-before.json").write_text(json.dumps(before, indent=2) + "\n")
    protected = json.loads(baseline_path.read_text())
    assert all(sha(ROOT / path) == expected for path, expected in protected.items())

    preview_report = json.loads((QA / "preview-validation.json").read_text())
    assert preview_report["ok"] and preview_report["source_sha256"] == APPROVED_ATLAS
    shutil.copy2(QA / "previews-final/idle.webp", ROOT / "assets/readme/idle/albedo.webp")
    showcase.build_archive_previews({"albedo"})
    for locale in showcase.LOCALES:
        subprocess.run([sys.executable, str(Path(__file__)), "--locale", locale], check=True)
    assert all(sha(ROOT / path) == expected for path, expected in protected.items())
    assert sha(ATLAS) == APPROVED_ATLAS
    print(f"Preserved {len(protected)} existing assets and the approved Albedo atlas.", flush=True)


if __name__ == "__main__":
    main()

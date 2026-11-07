"""Preserve Rita reference originals and compose a local inspection board."""
import hashlib
import json
from pathlib import Path
import shutil

from PIL import Image, ImageDraw, ImageOps

ROOT = Path(__file__).resolve().parents[4]
RUN = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "honkai-impact-3rd/Rita Rossweisse"
DEST = RUN / "references/source-originals"
NAMES = ["Rita Rossweisse1.webp", "Rita Rossweisse2", "Rita Rossweisse3",
         "Rita Rossweisse4.jpeg", "Rita Rossweisse5", "Rita Rossweisse6.jpeg",
         "Rita Rossweisse7", "Rita Rossweisse8", "Rita Rossweisse9"]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


DEST.mkdir(parents=True, exist_ok=True)
records = []
board = Image.new("RGB", (1200, 1260), "#d8dce2")
draw = ImageDraw.Draw(board)
for index, name in enumerate(NAMES):
    original, destination = SOURCE / name, DEST / name
    if original.exists():
        digest = sha(original)
        if destination.exists():
            raise RuntimeError(f"Reference collision; preserve both: {destination}")
        shutil.move(str(original), str(destination))
        assert sha(destination) == digest
    else:
        assert destination.is_file(), name
        digest = sha(destination)
    image = Image.open(destination)
    records.append({"original": str(original), "retained": str(destination),
                    "sha256": digest, "format": image.format, "size": list(image.size)})
    preview = ImageOps.contain(image.convert("RGBA"), (386, 385))
    x, y = (index % 3) * 400, (index // 3) * 420
    board.paste(preview, (x+(400-preview.width)//2, y+24+(390-preview.height)//2), preview)
    draw.text((x+8, y+5), f"{index+1}: {name}", fill="#131722")
board.save(RUN / "references/identity-board.jpg", quality=94)
curated = Image.new("RGB", (1400, 880), "#e8e9ed")
curated_draw = ImageDraw.Draw(curated)
for column, source_index in enumerate((7, 2, 8, 4)):
    source = Image.open(DEST / NAMES[source_index]).convert("RGBA")
    if source_index == 4:
        source = source.crop((0, 0, source.width, round(source.height * 0.50)))
    preview = ImageOps.contain(source, (340, 810))
    curated.paste(preview, (column*350+(350-preview.width)//2, 42+(820-preview.height)//2), preview)
    curated_draw.text((column*350+8, 10),
        ("PRIMARY outfit / face", "SAME maid outfit", "Chibi identity; NO SCYTHE", "Hair / covered eye ONLY")[column], fill="#131722")
curated.save(RUN / "references/production-identity.png")
(RUN / "qa/source-originals.json").write_text(json.dumps(records, indent=2) + "\n")
print(json.dumps({"retained_originals": len(records), "hashes_verified": True,
                  "identity_board": str(RUN / "references/identity-board.jpg")}, indent=2))

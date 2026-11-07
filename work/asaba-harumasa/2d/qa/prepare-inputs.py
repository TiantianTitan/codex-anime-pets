"""Retain original references byte-for-byte and arrange them for identity review."""
import hashlib
import json
from pathlib import Path
import shutil

from PIL import Image, ImageDraw, ImageOps

ROOT = Path(__file__).resolve().parents[4]
RUN = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "zenless-zone-zero/Asaba Harumasa"
DEST = RUN / "references/source-originals"
NAMES = ["Asaba Harumasa", "Asaba Harumasa2.webp", "Asaba Harumasa3.webp",
         "Asaba Harumasa4.webp", "Asaba Harumasa5.jpeg", "Asaba Harumasa6.jpeg",
         "Asaba Harumasa7.jpeg", "Asaba Harumasa8.jpeg", "Asaba Harumasa8.png"]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


DEST.mkdir(parents=True, exist_ok=True)
records = []
board = Image.new("RGB", (1200, 1260), "#d8dce2")
draw = ImageDraw.Draw(board)
for index, name in enumerate(NAMES):
    original = SOURCE / name
    destination = DEST / name
    if original.exists():
        digest = sha(original)
        if destination.exists():
            assert sha(destination) == digest, f"Reference collision: {destination}"
            raise RuntimeError("Both original and destination exist; preserve both and review")
        shutil.move(str(original), str(destination))
        assert sha(destination) == digest
    else:
        assert destination.is_file(), name
        digest = sha(destination)
    image = Image.open(destination)
    record = {"original": str(original), "retained": str(destination),
              "sha256": digest, "format": image.format, "size": list(image.size)}
    records.append(record)
    rgba = image.convert("RGBA")
    preview = ImageOps.contain(rgba, (386, 385))
    x, y = (index % 3) * 400, (index // 3) * 420
    board.paste(preview, (x + (400 - preview.width)//2, y + 24 + (390-preview.height)//2), preview)
    draw.text((x+8,y+5), f"{index+1}: {name}", fill="#131722")
board.save(RUN / "references/identity-board.jpg", quality=94)
curated = Image.new("RGB", (1400, 880), "#e8e9ed")
curated_draw = ImageDraw.Draw(curated)
for column, source_index in enumerate((0, 1, 3, 7)):
    source = Image.open(DEST / NAMES[source_index]).convert("RGBA")
    preview = ImageOps.contain(source, (340, 810))
    curated.paste(preview, (column*350+(350-preview.width)//2, 42+(820-preview.height)//2), preview)
    curated_draw.text((column*350+8, 10),
        ("Original outfit", "Front / exact sides", "Face and hair", "Chibi shape, redraw in 2D")[column], fill="#131722")
curated.save(RUN / "references/production-identity.png")
(RUN / "qa/source-originals.json").write_text(json.dumps(records, indent=2) + "\n")
print(json.dumps({"retained_originals": len(records), "hashes_verified": True,
                  "identity_board": str(RUN / "references/identity-board.jpg")}, indent=2))

#!/usr/bin/env python3
"""Build the README side-hop parade and its deterministic QA artifacts."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[2]
RUNS = ROOT / "work/readme-side-hop/runs"
QA = ROOT / "work/readme-side-hop/qa"
OUTPUT = ROOT / "assets/readme/companion-hop-parade.gif"

WIDTH = 1600
HEIGHT = 230
FRAME_DURATION_MS = 60
BLANK_START_FRAMES = 22
MOTION_FRAMES = 190
BLANK_END_FRAMES = 18

CHARACTERS = (
    ("xiao", "Xiao", 0, True),
    ("furina", "Furina", 2, True),
    ("hu-tao", "Hu Tao", 4, True),
    ("firefly", "Firefly", 6, True),
    ("robin", "Robin", 1, True),
)

HOP_Y = (5, 1, -6, -14, -10, -3, 5, 3)


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf",
    ):
        if Path(candidate).is_file():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def alpha_bbox(image: Image.Image) -> tuple[int, int, int, int]:
    bbox = image.getchannel("A").getbbox()
    if bbox is None:
        raise ValueError("encountered an empty animation frame")
    return bbox


def frame_root(slug: str, despilled: bool) -> Path:
    folder = "frames-despilled" if despilled else "frames"
    return RUNS / slug / folder / "running-right"


def load_character_frames(slug: str, despilled: bool) -> list[Image.Image]:
    paths = sorted(frame_root(slug, despilled).glob("*.png"))
    if len(paths) != 8:
        raise ValueError(f"{slug}: expected 8 frames, found {len(paths)}")
    originals = [Image.open(path).convert("RGBA") for path in paths]

    boxes = [alpha_bbox(image) for image in originals]
    union = (
        min(box[0] for box in boxes),
        min(box[1] for box in boxes),
        max(box[2] for box in boxes),
        max(box[3] for box in boxes),
    )
    crop_width = union[2] - union[0]
    crop_height = union[3] - union[1]
    target_height = 106
    scale = target_height / crop_height
    target_size = (max(1, round(crop_width * scale)), target_height)
    return [
        image.crop(union).resize(target_size, Image.Resampling.LANCZOS)
        for image in originals
    ]


def make_background() -> Image.Image:
    image = Image.new("RGB", (WIDTH, HEIGHT))
    pixels = image.load()
    top = (23, 24, 62)
    bottom = (94, 48, 91)
    for y in range(HEIGHT):
        t = y / (HEIGHT - 1)
        # A restrained twilight gradient that survives GIF quantization cleanly.
        eased = t * t * (3 - 2 * t)
        color = tuple(round(a + (b - a) * eased) for a, b in zip(top, bottom))
        for x in range(WIDTH):
            pixels[x, y] = color

    draw = ImageDraw.Draw(image, "RGBA")
    # Dawn glow and quiet landscape layers keep the strip decorative but readable.
    glow = Image.new("RGBA", image.size, (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow, "RGBA")
    glow_draw.ellipse((1260, 18, 1515, 273), fill=(255, 174, 196, 25))
    glow_draw.ellipse((1321, 79, 1448, 206), fill=(255, 230, 205, 88))
    glow = glow.filter(ImageFilter.GaussianBlur(20))
    image = Image.alpha_composite(image.convert("RGBA"), glow)
    draw = ImageDraw.Draw(image, "RGBA")

    stars = (
        (82, 48, 2), (167, 81, 1), (285, 37, 1), (402, 67, 2),
        (528, 31, 1), (649, 72, 1), (776, 43, 2), (914, 82, 1),
        (1046, 34, 1), (1160, 65, 2), (1240, 29, 1), (1520, 58, 2),
    )
    for x, y, radius in stars:
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(231, 237, 255, 180))
    for x, y in ((330, 98), (706, 104), (1092, 91)):
        draw.line((x - 4, y, x + 4, y), fill=(246, 218, 250, 105), width=1)
        draw.line((x, y - 4, x, y + 4), fill=(246, 218, 250, 105), width=1)

    draw.polygon(
        [(0, 188), (150, 170), (320, 188), (500, 165), (680, 187), (870, 162),
         (1050, 185), (1260, 157), (1430, 181), (1600, 164), (1600, 230), (0, 230)],
        fill=(31, 29, 63, 205),
    )
    draw.polygon(
        [(0, 207), (210, 192), (430, 207), (680, 190), (900, 208),
         (1160, 188), (1380, 205), (1600, 191), (1600, 230), (0, 230)],
        fill=(18, 22, 49, 235),
    )
    draw.line((0, 207, WIDTH, 207), fill=(225, 180, 224, 40), width=1)
    return image.convert("RGB")


def shadow_layer(x: int, y: int, hop_offset: int, sprite_width: int) -> Image.Image:
    layer = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer, "RGBA")
    airborne = max(0, -hop_offset)
    width = max(28, min(62, round(sprite_width * 0.46)) - airborne)
    alpha = max(22, 62 - airborne * 2)
    center_x = x + sprite_width // 2
    draw.ellipse((center_x - width, y + 103, center_x + width, y + 111), fill=(4, 5, 18, alpha))
    return layer.filter(ImageFilter.GaussianBlur(3))


def build_motion_frames(background: Image.Image, sprites: dict[str, list[Image.Image]]) -> list[Image.Image]:
    frames: list[Image.Image] = []
    frames.extend(background.copy() for _ in range(BLANK_START_FRAMES))

    spacing = 178
    group_span = spacing * (len(CHARACTERS) - 1)
    start_x = -190
    end_x = WIDTH + group_span + 190
    base_y = 96
    for motion_index in range(MOTION_FRAMES):
        progress = motion_index / (MOTION_FRAMES - 1)
        # Constant travel speed reads naturally with the repeated hop cycle.
        leader_x = round(start_x + (end_x - start_x) * progress)
        canvas = background.convert("RGBA")
        visible: list[tuple[int, Image.Image, int, int]] = []
        for queue_index, (slug, _label, phase, _despilled) in enumerate(CHARACTERS):
            pose_index = ((motion_index // 2) + phase) % 8
            sprite = sprites[slug][pose_index]
            x = leader_x - queue_index * spacing
            y = base_y + HOP_Y[pose_index]
            if x + sprite.width <= 0 or x >= WIDTH:
                continue
            canvas = Image.alpha_composite(canvas, shadow_layer(x, y, HOP_Y[pose_index], sprite.width))
            visible.append((queue_index, sprite, x, y))
        # Paint the front of the queue last when silhouettes briefly overlap.
        for _queue_index, sprite, x, y in reversed(visible):
            canvas.alpha_composite(sprite, (x, y))
        frames.append(canvas.convert("RGB"))

    frames.extend(background.copy() for _ in range(BLANK_END_FRAMES))
    return frames


def palette_frames(frames: list[Image.Image]) -> list[Image.Image]:
    sample_indices = range(0, len(frames), max(1, len(frames) // 18))
    swatches = [frames[index].resize((400, 58), Image.Resampling.BILINEAR) for index in sample_indices]
    sample = Image.new("RGB", (400, 58 * len(swatches)))
    for index, swatch in enumerate(swatches):
        sample.paste(swatch, (0, index * 58))
    palette = sample.quantize(colors=160, method=Image.Quantize.MEDIANCUT)
    return [frame.quantize(palette=palette, dither=Image.Dither.FLOYDSTEINBERG) for frame in frames]


def save_gif(frames: list[Image.Image], output: Path, duration_ms: int) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    indexed = palette_frames(frames)
    indexed[0].save(
        output,
        save_all=True,
        append_images=indexed[1:],
        duration=duration_ms,
        loop=0,
        optimize=True,
        disposal=1,
    )


def make_character_previews(sprites: dict[str, list[Image.Image]]) -> None:
    preview_dir = QA / "previews"
    preview_dir.mkdir(parents=True, exist_ok=True)
    base = Image.new("RGB", (260, 220), (27, 29, 55))
    for slug, _label, _phase, _despilled in CHARACTERS:
        frames = []
        for cycle_index in range(32):
            pose_index = (cycle_index // 2) % 8
            sprite = sprites[slug][pose_index]
            canvas = base.convert("RGBA")
            x = (canvas.width - sprite.width) // 2
            y = 76 + HOP_Y[pose_index]
            canvas = Image.alpha_composite(canvas, shadow_layer(x, y, HOP_Y[pose_index], sprite.width).crop((0, 0, 260, 220)))
            canvas.alpha_composite(sprite, (x, y))
            frames.append(canvas.convert("RGB"))
        save_gif(frames, preview_dir / f"{slug}-side-hop-right.gif", FRAME_DURATION_MS)


def make_contact_sheet(sprites: dict[str, list[Image.Image]]) -> None:
    cell_w, cell_h = 188, 178
    label_w, top_h = 116, 76
    sheet = Image.new("RGB", (label_w + cell_w * 8, top_h + cell_h * 5), (20, 22, 43))
    draw = ImageDraw.Draw(sheet)
    heading_font = font(22)
    label_font = font(18)
    small_font = font(14)
    draw.text((24, 14), "SIDE-HOP RIGHT · 8 UNIQUE SOURCE POSES", font=heading_font, fill=(235, 237, 255))
    for frame_index in range(8):
        draw.text((label_w + frame_index * cell_w + 88, 51), str(frame_index + 1), font=small_font, fill=(182, 192, 224))

    for row, (slug, label, _phase, _despilled) in enumerate(CHARACTERS):
        y0 = top_h + row * cell_h
        draw.rectangle((0, y0, sheet.width, y0 + cell_h), fill=(24 + row % 2 * 4, 27 + row % 2 * 4, 51 + row % 2 * 5))
        draw.text((16, y0 + 78), label, font=label_font, fill=(236, 220, 250))
        for column, sprite in enumerate(sprites[slug]):
            x0 = label_w + column * cell_w
            draw.rectangle((x0, y0, x0 + cell_w, y0 + cell_h), outline=(83, 88, 126), width=1)
            checker = Image.new("RGB", (cell_w - 10, cell_h - 10), (44, 47, 72))
            checker_draw = ImageDraw.Draw(checker)
            for yy in range(0, checker.height, 16):
                for xx in range(0, checker.width, 16):
                    if (xx // 16 + yy // 16) % 2:
                        checker_draw.rectangle((xx, yy, xx + 15, yy + 15), fill=(51, 54, 80))
            sheet.paste(checker, (x0 + 5, y0 + 5))
            scaled = sprite.resize((round(sprite.width * 1.16), round(sprite.height * 1.16)), Image.Resampling.LANCZOS)
            px = x0 + (cell_w - scaled.width) // 2
            py = y0 + (cell_h - scaled.height) // 2
            sheet.paste(scaled, (px, py), scaled)
    QA.mkdir(parents=True, exist_ok=True)
    sheet.save(QA / "side-hop-contact-sheet.png")


def make_banner_sample_sheet(frames: list[Image.Image]) -> None:
    indices = (0, BLANK_START_FRAMES, 54, 88, 122, 156, 190, len(frames) - 1)
    thumb_w = 800
    thumb_h = round(HEIGHT * thumb_w / WIDTH)
    sheet = Image.new("RGB", (thumb_w, thumb_h * len(indices)), (15, 17, 34))
    draw = ImageDraw.Draw(sheet)
    for row, index in enumerate(indices):
        thumb = frames[index].resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        sheet.paste(thumb, (0, row * thumb_h))
        draw.rectangle((6, row * thumb_h + 6, 92, row * thumb_h + 31), fill=(10, 12, 29))
        draw.text((13, row * thumb_h + 10), f"frame {index}", font=font(14), fill=(239, 241, 255))
    sheet.save(QA / "banner-sampled-frames.png")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    sprites = {
        slug: load_character_frames(slug, despilled)
        for slug, _label, _phase, despilled in CHARACTERS
    }
    make_contact_sheet(sprites)
    make_character_previews(sprites)
    background = make_background()
    frames = build_motion_frames(background, sprites)
    make_banner_sample_sheet(frames)
    save_gif(frames, OUTPUT, FRAME_DURATION_MS)

    first_blank = frames[0].tobytes() == background.tobytes()
    last_blank = frames[-1].tobytes() == background.tobytes()
    report = {
        "ok": first_blank and last_blank and len(frames) == BLANK_START_FRAMES + MOTION_FRAMES + BLANK_END_FRAMES,
        "output": str(OUTPUT),
        "dimensions": [WIDTH, HEIGHT],
        "frame_count": len(frames),
        "frame_duration_ms": FRAME_DURATION_MS,
        "duration_ms": len(frames) * FRAME_DURATION_MS,
        "blank_start_frames": BLANK_START_FRAMES,
        "blank_end_frames": BLANK_END_FRAMES,
        "starts_empty": first_blank,
        "ends_empty": last_blank,
        "travel_direction": "screen-left-to-screen-right",
        "characters": [slug for slug, _label, _phase, _despilled in CHARACTERS],
        "unique_source_poses_per_character": 8,
        "sha256": sha256(OUTPUT),
        "bytes": OUTPUT.stat().st_size,
    }
    (QA / "banner-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

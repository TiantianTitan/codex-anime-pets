#!/usr/bin/env python3
"""Build the localized animated README showcases from approved pet previews."""

from __future__ import annotations

import math
import argparse
import subprocess
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageSequence


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "readme"
SERIF = "/usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf"
SANS = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf"
CJK_SANS = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
CJK_SERIF_BOLD = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
FRAME_MS = 100
FRAME_COUNT = 22
ARCHIVE_CARD_SIZE = (220, 240)
ARCHIVE_SILHOUETTE_HEIGHT = 198
ARCHIVE_BASELINE = 220


@dataclass
class GifClip:
    frames: list[Image.Image]
    durations: list[int]
    ends: list[int]
    duration: int

    @classmethod
    def open(cls, path: str) -> "GifClip":
        image = Image.open(ROOT / path)
        frames: list[Image.Image] = []
        durations: list[int] = []
        ends: list[int] = []
        elapsed = 0
        for frame in ImageSequence.Iterator(image):
            frames.append(frame.convert("RGBA"))
            duration = max(40, frame.info.get("duration", image.info.get("duration", 100)))
            durations.append(duration)
            elapsed += duration
            ends.append(elapsed)
        return cls(frames, durations, ends, elapsed)

    def at(self, time_ms: int) -> Image.Image:
        cursor = time_ms % self.duration
        for frame, end in zip(self.frames, self.ends):
            if cursor < end:
                return frame
        return self.frames[-1]


def font(path: str, size: int, index: int = 0) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size, index=index)


def locale_font(locale: str, size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    if locale == "zh-CN":
        return font(CJK_SERIF_BOLD if bold else CJK_SANS, size, index=2)
    if locale == "ja":
        return font(CJK_SERIF_BOLD if bold else CJK_SANS, size, index=0)
    return font(SERIF_BOLD if bold else SANS, size)


def localized_asset_name(filename: str, locale: str) -> str:
    if locale == "en":
        return filename
    path = Path(filename)
    return f"{path.stem}.{locale}{path.suffix}"


def gradient(size: tuple[int, int], top: tuple[int, int, int], bottom: tuple[int, int, int]) -> Image.Image:
    width, height = size
    canvas = Image.new("RGBA", size)
    draw = ImageDraw.Draw(canvas)
    for y in range(height):
        t = y / max(1, height - 1)
        color = tuple(round(a + (b - a) * t) for a, b in zip(top, bottom)) + (255,)
        draw.line((0, y, width, y), fill=color)
    return canvas


def tracking_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    text_font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int] | tuple[int, int, int, int],
    tracking: int,
    anchor: str = "la",
) -> None:
    widths = [draw.textlength(char, font=text_font) for char in text]
    total = sum(widths) + tracking * max(0, len(text) - 1)
    x, y = xy
    if anchor.startswith("m"):
        x -= total / 2
    elif anchor.startswith("r"):
        x -= total
    for char, width in zip(text, widths):
        draw.text((round(x), y), char, font=text_font, fill=fill, anchor="la")
        x += width + tracking


def glow_circle(canvas: Image.Image, center: tuple[int, int], radius: int, color: tuple[int, int, int], alpha: int) -> None:
    layer = Image.new("RGBA", canvas.size)
    draw = ImageDraw.Draw(layer)
    x, y = center
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(*color, alpha))
    layer = layer.filter(ImageFilter.GaussianBlur(radius / 2.4))
    canvas.paste(layer, (0, 0), layer)


def place_character(
    canvas: Image.Image,
    clip: GifClip,
    time_ms: int,
    center_x: int,
    baseline: int,
    scale: float,
    phase_ms: int = 0,
) -> None:
    frame = clip.at(time_ms + phase_ms)
    size = (round(frame.width * scale), round(frame.height * scale))
    frame = frame.resize(size, Image.Resampling.LANCZOS)
    canvas.paste(frame, (round(center_x - size[0] / 2), baseline - size[1]), frame)


def draw_stars(canvas: Image.Image, frame_index: int, count: int = 24) -> None:
    draw = ImageDraw.Draw(canvas)
    width, height = canvas.size
    for i in range(count):
        x = (67 + i * 149) % (width - 60) + 30
        y = (43 + i * 83) % max(80, height - 100) + 24
        wave = (math.sin(frame_index * 0.55 + i * 1.7) + 1) / 2
        alpha = round(45 + wave * 150)
        radius = 1 if i % 4 else 2
        color = (214, 250, 255, alpha) if i % 3 else (255, 228, 164, alpha)
        draw.polygon(((x, y - radius * 2), (x + radius, y), (x, y + radius * 2), (x - radius, y)), fill=color)


def save_webp(frames: list[Image.Image], name: str) -> None:
    frames[0].save(
        OUT / name,
        format="WEBP",
        save_all=True,
        append_images=frames[1:],
        duration=FRAME_MS,
        loop=0,
        quality=86,
        method=6,
        minimize_size=True,
    )


def save_timed_webp(frames: list[Image.Image], durations: list[int], path: Path) -> None:
    frames[0].save(
        path,
        format="WEBP",
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        quality=88,
        method=6,
        minimize_size=True,
    )


ARCHIVE_SOURCES = [
    ("xiao", "work/xiao/2d/qa/previews-final/idle.gif"),
    ("dan-heng-imbibitor-lunae", "work/dan-heng-imbibitor-lunae/2d/qa/previews-final/idle.gif"),
    ("jing-yuan", "work/jing-yuan/2d/qa/previews-final/idle.gif"),
    ("zhongli", "work/zhongli/2d/qa/previews-final/idle.gif"),
    ("raiden-mei-2d", "work/raiden-mei/2d/qa/previews-final/idle.gif"),
    ("raiden-mei-3d", "work/raiden-mei/3d/qa/previews-final/idle.gif"),
    ("obanai", "work/obanai/2d/qa/previews-final/idle.gif"),
    ("yae-miko", "work/yae-miko/2d/qa/previews-final/idle.gif"),
    ("furina", "work/furina/2d/qa/previews-final/idle.gif"),
    ("acheron", "work/acheron/2d/qa/previews-final/idle.gif"),
    ("ellen-joe", "work/ellen-joe/2d/qa/previews-final/idle.gif"),
    ("hu-tao", "work/hu-tao/2d/qa/previews-final/idle.gif"),
    ("robin", "work/robin/2d/qa/previews-final/idle.gif"),
    ("kaeya", "work/kaeya/2d/qa/previews-final/idle.gif"),
    ("firefly", "work/firefly/2d/qa/previews-final/idle.gif"),
    ("kevin-kaslana", "work/kevin-kaslana/2d-repair-v3/qa/previews-final/idle.gif"),
    ("kamisato-ayaka", "work/kamisato-ayaka/2d/qa/previews-final/idle.gif"),
    ("blade", "work/blade/2d/qa/previews-final/idle.gif"),
    ("ruan-mei", "work/ruan-mei/2d/qa/previews-final/idle.gif"),
    ("kaedehara-kazuha", "work/kazuha-chibi/2d/qa/previews-final/idle.gif"),
    ("hoshimi-miyabi", "work/miyabi/2d/qa/previews-final/idle.gif"),
    ("aventurine", "work/aventurine/2d/qa/previews-final/idle.gif"),
    ("ganyu", "work/ganyu/2d/qa/previews-final/idle.gif"),
    ("sunday", "work/sunday/2d/qa/previews-final/idle.gif"),
    ("mitsuri-kanroji", "assets/readme/mitsuri-kanroji-idle.gif"),
    ("kafka", "work/kafka/2d/qa/previews-final/idle.gif"),
    ("otto-apocalypse", "work/otto-apocalypse/2d/qa/previews-final/idle.gif"),
    ("nicole-demara", "work/nicole-demara/2d/qa/previews-final/idle.gif"),
    ("jane-doe", "work/jane-doe/2d/qa/previews-final/idle.gif"),
    ("anby-demara", "work/anby-demara/2d/qa/previews-final/idle.gif"),
    ("kiana-kaslana", "work/kiana-kaslana/2d/qa/previews-final/idle.gif"),
    ("tartaglia", "work/tartaglia/2d/qa/previews-final/idle.gif"),
    ("burnice-white", "work/burnice-white/2d/qa/previews/idle.gif"),
    ("sparkle", "work/sparkle/2d/qa/previews-final/idle.gif"),
    ("venti", "work/venti/2d/qa/previews-final/idle.gif"),
    ("fu-hua", "work/fu-hua/2d/qa/previews-final/idle.gif"),
    ("lighter", "work/lighter/2d/qa/previews-final/idle.gif"),
    ("raiden-shogun", "work/raiden-shogun/2d/qa/previews-final/idle.gif"),
    ("bronya-zaychik", "work/bronya-zaychik/2d/qa/previews-final/idle.gif"),
    ("zhu-yuan", "work/zhu-yuan/2d/qa/previews-final/idle.gif"),
    ("seele-vollerei", "work/seele-vollerei/2d/qa/previews-final/idle.gif"),
    ("vivian-banshee", "work/vivian-banshee/2d/qa/previews-final/idle.gif"),
    ("kibutsuji-muzan", "work/kibutsuji-muzan/2d/qa/previews-final/idle.gif"),
]


UNIVERSE_SLUGS = {
    "genshin": {
        "xiao", "zhongli", "yae-miko", "furina", "hu-tao", "kaeya",
        "kamisato-ayaka", "kaedehara-kazuha", "ganyu", "tartaglia", "venti",
        "raiden-shogun",
    },
    "star-rail": {
        "dan-heng-imbibitor-lunae", "jing-yuan", "acheron", "robin", "firefly",
        "blade", "ruan-mei", "aventurine", "sunday", "kafka", "sparkle",
    },
    "honkai-3rd": {
        "raiden-mei-2d", "raiden-mei-3d", "kevin-kaslana", "otto-apocalypse",
        "kiana-kaslana", "fu-hua", "bronya-zaychik", "seele-vollerei",
    },
    "zenless": {
        "ellen-joe", "hoshimi-miyabi", "nicole-demara", "jane-doe",
        "anby-demara", "burnice-white", "lighter", "zhu-yuan", "vivian-banshee",
    },
    "others": {"obanai", "mitsuri-kanroji", "kibutsuji-muzan"},
}

UNIVERSE_PALETTES = {
    "genshin": {
        "top": (7, 17, 27),
        "bottom": (24, 31, 35),
        "primary": (103, 222, 203),
        "secondary": (244, 198, 112),
        "label": "GENSHIN",
    },
    "star-rail": {
        "top": (8, 11, 31),
        "bottom": (28, 20, 46),
        "primary": (130, 174, 255),
        "secondary": (194, 132, 255),
        "label": "STAR RAIL",
    },
    "honkai-3rd": {
        "top": (7, 16, 31),
        "bottom": (30, 20, 40),
        "primary": (126, 220, 250),
        "secondary": (247, 126, 177),
        "label": "HONKAI 3RD",
    },
    "zenless": {
        "top": (13, 13, 18),
        "bottom": (38, 26, 20),
        "primary": (255, 213, 91),
        "secondary": (255, 116, 70),
        "label": "ZENLESS",
    },
    "others": {
        "top": (18, 11, 19),
        "bottom": (39, 20, 30),
        "primary": (229, 223, 228),
        "secondary": (241, 105, 137),
        "label": "OTHERS",
    },
}

LOCALES = {
    "en": {
        "hero_kicker": "ANIMATED COMPANIONS / CODEX V2",
        "hero_title": "CODEX ANIME PETS",
        "hero_subtitle": "YOUR DESKTOP. YOUR ROSTER.",
        "motion_kicker": "MOTION FILM / SIX CHARACTER STATES",
        "motion_actions": ("JUMP", "REVIEW", "WAVE", "WORK", "WAIT", "GREET"),
        "motion_names": ("FIREFLY", "OTTO", "SUNDAY", "RAIDEN MEI", "XIAO", "ROBIN"),
        "arrival_kicker": "COLLECTION UPDATE",
        "arrival_lines": ("NEW", "ARRIVALS"),
        "arrival_available": "NOW AVAILABLE",
        "arrival_names": ("SEELE", "VIVIAN", "MUZAN"),
        "collection_title": "COMPANION COLLECTION",
        "collection_count": "{characters} CHARACTERS / {editions} EDITIONS",
        "universe_labels": ("GENSHIN", "STAR RAIL", "HONKAI 3RD", "ZENLESS", "OTHERS"),
        "direction_kicker": "DIRECTIONAL SYSTEM",
        "direction_title": "16-DIRECTION TURNAROUND",
        "direction_latest": "LATEST RELEASE / {name}",
        "direction_name": "BURNICE WHITE",
        "cardinals": ("000 / UP", "090 / RIGHT", "180 / DOWN", "270 / LEFT"),
        "footer": "SEE YOU ON THE DESKTOP",
    },
    "fr": {
        "hero_kicker": "COMPAGNONS ANIMÉS / CODEX V2",
        "hero_title": "CODEX ANIME PETS",
        "hero_subtitle": "VOTRE BUREAU. VOTRE COLLECTION.",
        "motion_kicker": "FILM D’ANIMATION / SIX ÉTATS",
        "motion_actions": ("SAUT", "ANALYSE", "SALUT", "TRAVAIL", "ATTENTE", "ACCUEIL"),
        "motion_names": ("FIREFLY", "OTTO", "SUNDAY", "RAIDEN MEI", "XIAO", "ROBIN"),
        "arrival_kicker": "MISE À JOUR DE LA COLLECTION",
        "arrival_lines": ("NOUVEAUX", "PERSONNAGES"),
        "arrival_available": "DISPONIBLES",
        "arrival_names": ("SEELE", "VIVIAN", "MUZAN"),
        "collection_title": "COLLECTION DE COMPAGNONS",
        "collection_count": "{characters} PERSONNAGES / {editions} ÉDITIONS",
        "universe_labels": ("GENSHIN", "STAR RAIL", "HONKAI 3RD", "ZENLESS", "AUTRES"),
        "direction_kicker": "SYSTÈME D’ORIENTATION",
        "direction_title": "ROTATION SUR 16 DIRECTIONS",
        "direction_latest": "DERNIÈRE SORTIE / {name}",
        "direction_name": "BURNICE WHITE",
        "cardinals": ("000 / HAUT", "090 / DROITE", "180 / BAS", "270 / GAUCHE"),
        "footer": "À BIENTÔT SUR LE BUREAU",
    },
    "zh-CN": {
        "hero_kicker": "动态伙伴 / CODEX V2",
        "hero_title": "CODEX 动画伙伴",
        "hero_subtitle": "你的桌面，你的角色收藏",
        "motion_kicker": "动作胶片 / 六种角色状态",
        "motion_actions": ("跳跃", "审阅", "挥手", "工作", "等待", "问候"),
        "motion_names": ("流萤", "奥托", "星期日", "雷电芽衣", "魈", "知更鸟"),
        "arrival_kicker": "收藏更新",
        "arrival_lines": ("新角色", "现已加入"),
        "arrival_available": "现已开放下载",
        "arrival_names": ("希儿", "薇薇安", "无惨"),
        "collection_title": "角色收藏",
        "collection_count": "{characters} 个角色 / {editions} 个版本",
        "universe_labels": ("原神", "星穹铁道", "崩坏3", "绝区零", "其他"),
        "direction_kicker": "方向系统",
        "direction_title": "16 方向环视",
        "direction_latest": "最新角色 / {name}",
        "direction_name": "柏妮思",
        "cardinals": ("000 / 上", "090 / 右", "180 / 下", "270 / 左"),
        "footer": "桌面上再见",
    },
    "ja": {
        "hero_kicker": "アニメペット / CODEX V2",
        "hero_title": "CODEX アニメペット",
        "hero_subtitle": "デスクトップに、あなただけのコレクションを",
        "motion_kicker": "モーションフィルム / 6つの状態",
        "motion_actions": ("ジャンプ", "レビュー", "手を振る", "作業中", "待機", "挨拶"),
        "motion_names": ("ホタル", "オットー", "サンデー", "雷電芽衣", "魈", "ロビン"),
        "arrival_kicker": "コレクション更新",
        "arrival_lines": ("新着", "キャラクター"),
        "arrival_available": "配布中",
        "arrival_names": ("ゼーレ", "ビビアン", "無惨"),
        "collection_title": "キャラクターコレクション",
        "collection_count": "{characters}キャラクター / {editions}エディション",
        "universe_labels": ("原神", "スターレイル", "崩壊3rd", "ゼンレス", "その他"),
        "direction_kicker": "方向システム",
        "direction_title": "16方向ビュー",
        "direction_latest": "最新キャラクター / {name}",
        "direction_name": "バーニス・ホワイト",
        "cardinals": ("000 / 上", "090 / 右", "180 / 下", "270 / 左"),
        "footer": "デスクトップで、また会おう",
    },
}


def universe_for_slug(slug: str) -> str:
    for universe, slugs in UNIVERSE_SLUGS.items():
        if slug in slugs:
            return universe
    raise KeyError(f"No universe palette configured for {slug}")


def archive_number_labels() -> list[str]:
    """Number characters once and letter multiple editions of the same character."""
    character_keys = [
        slug.removesuffix("-2d").removesuffix("-3d") for slug, _ in ARCHIVE_SOURCES
    ]
    edition_counts = Counter(character_keys)
    character_numbers: dict[str, int] = {}
    edition_indices: defaultdict[str, int] = defaultdict(int)
    labels: list[str] = []
    for key in character_keys:
        number = character_numbers.setdefault(key, len(character_numbers) + 1)
        if edition_counts[key] > 1:
            suffix = chr(ord("A") + edition_indices[key])
            edition_indices[key] += 1
            labels.append(f"{number:02d}{suffix}")
        else:
            labels.append(f"{number:02d}")
    return labels


def build_archive_previews() -> None:
    preview_dir = OUT / "archive-previews"
    preview_dir.mkdir(parents=True, exist_ok=True)
    for slug, source in ARCHIVE_SOURCES:
        palette = UNIVERSE_PALETTES[universe_for_slug(slug)]
        primary = palette["primary"]
        secondary = palette["secondary"]
        clip = GifClip.open(source)
        boxes = []
        for frame in clip.frames:
            mask = frame.getchannel("A").point(lambda value: 255 if value > 16 else 0)
            box = mask.getbbox()
            if box:
                boxes.append(box)
        if not boxes:
            raise ValueError(f"No visible pixels in {source}")
        left = min(box[0] for box in boxes)
        top = min(box[1] for box in boxes)
        right = max(box[2] for box in boxes)
        bottom = max(box[3] for box in boxes)
        crop_width = right - left
        crop_height = bottom - top
        # Archive portraits use one non-negotiable visual ruler: every complete
        # silhouette has the same height and stands on the same baseline. Width
        # remains proportional, so wide hair, weapons, and tails are never
        # stretched or used as a reason to shrink the entire character.
        scale = ARCHIVE_SILHOUETTE_HEIGHT / crop_height
        target_size = (max(1, round(crop_width * scale)), ARCHIVE_SILHOUETTE_HEIGHT)
        if target_size[0] > ARCHIVE_CARD_SIZE[0] - 28:
            raise ValueError(f"{slug} exceeds the archive card safe width: {target_size[0]} px")

        rendered: list[Image.Image] = []
        for frame_index, frame in enumerate(clip.frames):
            canvas = gradient(ARCHIVE_CARD_SIZE, palette["top"], palette["bottom"]).convert("RGB")
            draw = ImageDraw.Draw(canvas, "RGBA")
            for y in range(26, 218, 32):
                draw.line((18, y, 202, y), fill=(*primary, 10), width=1)
            glow_circle(canvas, (110, 140), 76, primary, 24)
            glow_circle(canvas, (110, 170), 62, secondary, 15)
            crop = frame.crop((left, top, right, bottom)).resize(target_size, Image.Resampling.LANCZOS)
            x = round((ARCHIVE_CARD_SIZE[0] - target_size[0]) / 2)
            y = ARCHIVE_BASELINE - target_size[1]
            canvas.paste(crop, (x, y), crop)
            draw = ImageDraw.Draw(canvas, "RGBA")
            draw.line((28, ARCHIVE_BASELINE + 2, 192, ARCHIVE_BASELINE + 2), fill=(*secondary, 105), width=1)
            draw.line((18, 18, 44, 18), fill=(*primary, 135), width=2)
            draw.line((18, 18, 18, 44), fill=(*primary, 135), width=2)
            draw.line((176, 222, 202, 222), fill=(*secondary, 135), width=2)
            draw.line((202, 196, 202, 222), fill=(*secondary, 135), width=2)
            pulse = round(80 + 70 * ((math.sin(frame_index * 1.2) + 1) / 2))
            border = tuple(round((a + b) / 2) for a, b in zip(primary, secondary))
            draw.rounded_rectangle((2, 2, 217, 237), radius=18, outline=(*border, pulse), width=2)
            rendered.append(canvas)
        save_timed_webp(rendered, clip.durations, preview_dir / f"{slug}.webp")


def build_collection_wall(locale: str = "en") -> None:
    """Build the README's auto-sized wall from the same archive source list."""
    copy = LOCALES[locale]
    columns = 6
    card_width = 170
    card_height = round(card_width * ARCHIVE_CARD_SIZE[1] / ARCHIVE_CARD_SIZE[0])
    column_gap = 22
    row_gap = 18
    margin_x = 35
    header_height = 134
    footer_height = 32
    source_rows = [
        ARCHIVE_SOURCES[index : index + columns]
        for index in range(0, len(ARCHIVE_SOURCES), columns)
    ]
    # A single orphan card makes the collection look unfinished. When the
    # total lands on 6n+1, balance the final seven editions as 4 + 3 while
    # preserving their order and numbering.
    if len(source_rows) > 1 and len(source_rows[-1]) == 1:
        carried = source_rows[-2][-2:]
        source_rows[-2] = source_rows[-2][:-2]
        source_rows[-1] = carried + source_rows[-1]
    rows = len(source_rows)
    number_labels = archive_number_labels()
    wall_height = header_height + rows * card_height + (rows - 1) * row_gap + footer_height

    canvas = gradient((1200, wall_height), (5, 9, 25), (29, 15, 35)).convert("RGB")
    glow_circle(canvas, (160, 170), 180, (92, 218, 229), 32)
    glow_circle(canvas, (1040, 255), 210, (255, 119, 172), 28)
    draw = ImageDraw.Draw(canvas, "RGBA")
    for x in range(34, 1170, 48):
        draw.line((x, 98, x, wall_height - 24), fill=(197, 235, 246, 7), width=1)
    for y in range(116, wall_height - 20, 44):
        draw.line((24, y, 1176, y), fill=(197, 235, 246, 6), width=1)

    tracking_text(draw, (40, 30), copy["collection_title"], locale_font(locale, 31, bold=True), (255, 238, 194, 255), 2)
    character_keys = {
        slug.removesuffix("-2d").removesuffix("-3d") for slug, _ in ARCHIVE_SOURCES
    }
    tracking_text(
        draw,
        (1160, 38),
        copy["collection_count"].format(characters=len(character_keys), editions=len(ARCHIVE_SOURCES)),
        locale_font(locale, 13),
        (143, 230, 237, 225),
        3,
        "ra",
    )
    draw.line((40, 82, 1160, 82), fill=(244, 190, 210, 95), width=1)
    draw.line((40, 86, 430, 86), fill=(104, 225, 233, 120), width=2)
    draw.line((770, 86, 1160, 86), fill=(255, 137, 179, 120), width=2)
    legend_x = (126, 362, 600, 838, 1074)
    universes = ("genshin", "star-rail", "honkai-3rd", "zenless", "others")
    for x, universe, label in zip(legend_x, universes, copy["universe_labels"]):
        palette = UNIVERSE_PALETTES[universe]
        draw.line((x - 62, 106, x - 42, 106), fill=(*palette["primary"], 210), width=3)
        tracking_text(draw, (x - 34, 97), label, locale_font(locale, 10), (*palette["primary"], 215), 1)

    source_index = 0
    for row, row_sources in enumerate(source_rows):
        row_width = len(row_sources) * card_width + max(0, len(row_sources) - 1) * column_gap
        row_left = round((1200 - row_width) / 2)
        top = header_height + row * (card_height + row_gap)
        for column, (slug, _) in enumerate(row_sources):
            card = Image.open(OUT / "archive-previews" / f"{slug}.webp")
            card.seek(0)
            card = card.convert("RGB").resize((card_width, card_height), Image.Resampling.LANCZOS)
            left = row_left + column * (card_width + column_gap)
            canvas.paste(card, (left, top))
            palette = UNIVERSE_PALETTES[universe_for_slug(slug)]
            label = number_labels[source_index + column]
            label_font = font(SANS_BOLD, 15)
            label_width = max(38, round(draw.textlength(label, font=label_font)) + 18)
            badge_right = left + card_width - 10
            badge_top = top + 9
            badge_left = badge_right - label_width
            draw.rounded_rectangle(
                (badge_left, badge_top, badge_right, badge_top + 24),
                radius=8,
                fill=(4, 8, 21, 225),
                outline=(*palette["primary"], 190),
                width=1,
            )
            draw.text(
                ((badge_left + badge_right) / 2, badge_top + 12),
                label,
                font=label_font,
                fill=(*palette["primary"], 255),
                anchor="mm",
            )
        source_index += len(row_sources)

    draw = ImageDraw.Draw(canvas, "RGBA")
    draw.rounded_rectangle((2, 2, 1197, wall_height - 3), radius=28, outline=(243, 190, 210, 145), width=2)
    canvas.save(OUT / localized_asset_name("character-collection-wall.webp", locale), format="WEBP", quality=90, method=6)


def visible_crop(frame: Image.Image) -> Image.Image:
    mask = frame.getchannel("A").point(lambda value: 255 if value > 16 else 0)
    box = mask.getbbox()
    if not box:
        raise ValueError("Cannot crop an empty character frame")
    return frame.crop(box)


def paste_visible(
    canvas: Image.Image,
    frame: Image.Image,
    center: tuple[int, int],
    target_height: int,
) -> None:
    crop = visible_crop(frame)
    target_width = max(1, round(crop.width * target_height / crop.height))
    crop = crop.resize((target_width, target_height), Image.Resampling.LANCZOS)
    x = round(center[0] - target_width / 2)
    y = round(center[1] - target_height / 2)
    canvas.paste(crop, (x, y), crop)


def build_direction_orbit(locale: str = "en") -> None:
    """Show the latest archive entry's full 16-direction look loop."""
    copy = LOCALES[locale]
    # The direction showcase sits above New Arrivals and intentionally keeps
    # its established Burnice feature when later characters are appended.
    slug, preview_source = next(
        entry for entry in ARCHIVE_SOURCES if entry[0] == "burnice-white"
    )
    preview_path = ROOT / preview_source
    run_root = preview_path.parents[2]
    sheet_candidates = (
        run_root / "final" / "spritesheet-extended.webp",
        run_root / "final" / "spritesheet.webp",
    )
    sheet_path = next((path for path in sheet_candidates if path.exists()), None)
    if sheet_path is None:
        raise FileNotFoundError(f"No final spritesheet found for latest character: {slug}")

    sheet = Image.open(sheet_path).convert("RGBA")
    if sheet.width % 8 or sheet.height % 11:
        raise ValueError(f"Unexpected v2 spritesheet dimensions: {sheet.size}")
    cell_width = sheet.width // 8
    cell_height = sheet.height // 11
    directions = [
        sheet.crop((column * cell_width, row * cell_height, (column + 1) * cell_width, (row + 1) * cell_height))
        for row in (9, 10)
        for column in range(8)
    ]

    universe = universe_for_slug(slug)
    palette = UNIVERSE_PALETTES[universe]
    primary = palette["primary"]
    secondary = palette["secondary"]
    display_name = copy["direction_name"]
    canvas = gradient((1200, 720), (5, 9, 24), palette["bottom"]).convert("RGB")
    glow_circle(canvas, (600, 374), 255, primary, 24)
    glow_circle(canvas, (600, 410), 180, secondary, 20)
    draw = ImageDraw.Draw(canvas, "RGBA")
    draw_stars(canvas, 3, 32)

    center_x, center_y = 600, 394
    radius_x, radius_y = 480, 235
    draw.ellipse(
        (center_x - radius_x, center_y - radius_y, center_x + radius_x, center_y + radius_y),
        outline=(*primary, 70),
        width=2,
    )
    draw.ellipse((466, 260, 734, 528), outline=(*secondary, 72), width=2)
    draw.ellipse((486, 280, 714, 508), outline=(*primary, 42), width=1)
    draw.line((120, center_y, 1080, center_y), fill=(*primary, 22), width=1)
    draw.line((center_x, 159, center_x, 629), fill=(*secondary, 22), width=1)

    for index in range(16):
        angle = math.radians(index * 22.5 - 90)
        outer_x = center_x + math.cos(angle) * radius_x
        outer_y = center_y + math.sin(angle) * radius_y
        inner_x = center_x + math.cos(angle) * (radius_x - 14)
        inner_y = center_y + math.sin(angle) * (radius_y - 9)
        color = secondary if index % 4 == 0 else primary
        draw.line((inner_x, inner_y, outer_x, outer_y), fill=(*color, 150 if index % 4 == 0 else 70), width=3 if index % 4 == 0 else 1)

    for index, pose in enumerate(directions):
        angle = math.radians(index * 22.5 - 90)
        x = round(center_x + math.cos(angle) * radius_x)
        y = round(center_y + math.sin(angle) * radius_y)
        if index % 4 == 0:
            glow_circle(canvas, (x, y), 49, secondary, 30)
        paste_visible(canvas, pose, (x, y), 112)

    idle = GifClip.open(preview_source).frames[0]
    glow_circle(canvas, (600, 405), 125, secondary, 38)
    paste_visible(canvas, idle, (600, 400), 246)
    draw = ImageDraw.Draw(canvas, "RGBA")
    draw.ellipse((474, 274, 726, 526), outline=(*secondary, 115), width=2)
    draw.arc((456, 256, 744, 544), 196, 332, fill=(*primary, 180), width=3)
    draw.arc((456, 256, 744, 544), 16, 152, fill=(*secondary, 180), width=3)

    tracking_text(draw, (40, 28), copy["direction_kicker"], locale_font(locale, 13), (*primary, 235), 4)
    draw.text((40, 52), copy["direction_title"], font=locale_font(locale, 38, bold=True), fill=(255, 239, 195), anchor="la")
    tracking_text(
        draw,
        (1160, 35),
        copy["direction_latest"].format(name=display_name),
        locale_font(locale, 12),
        (*secondary, 230),
        3,
        "ra",
    )
    tracking_text(draw, (600, 538), display_name, locale_font(locale, 14), (255, 234, 205, 235), 3, "ma")

    cardinal_labels = tuple(zip(
        ((600, 91), (1014, 386), (600, 699), (186, 386)),
        copy["cardinals"],
        ("ma", "ra", "ma", "la"),
    ))
    for xy, label, anchor in cardinal_labels:
        tracking_text(draw, xy, label, locale_font(locale, 11), (232, 225, 236, 205), 2, anchor)

    draw.rounded_rectangle((2, 2, 1197, 717), radius=28, outline=(*secondary, 135), width=2)
    canvas.save(OUT / localized_asset_name("direction-orbit.webp", locale), format="WEBP", quality=92, method=6)


def build_footer_scene(locale: str = "en") -> None:
    copy = LOCALES[locale]
    cast = [
        ("work/xiao/2d/qa/previews-final/idle.gif", 135, 284, 205),
        ("work/mitsuri-kanroji/2d/qa/previews-final/waiting.gif", 338, 286, 205),
        ("work/sunday/2d/qa/previews-final/waving.gif", 862, 286, 205),
        ("work/ganyu/2d/qa/previews-final/waiting.gif", 1065, 284, 205),
    ]
    canvas = gradient((1200, 390), (5, 10, 27), (37, 20, 41)).convert("RGB")
    glow_circle(canvas, (600, 120), 106, (255, 222, 169), 46)
    draw = ImageDraw.Draw(canvas, "RGBA")
    draw.ellipse((536, 56, 664, 184), fill=(255, 239, 203, 232), outline=(255, 157, 190, 125), width=2)
    draw.ellipse((568, 38, 676, 157), fill=(7, 12, 29, 255))
    draw_stars(canvas, 8, 24)
    draw.arc((42, 216, 1158, 510), 188, 352, fill=(112, 225, 232, 55), width=2)
    draw.arc((118, 246, 1082, 520), 190, 350, fill=(255, 153, 188, 45), width=1)

    for source, x, center_y, target_height in cast:
        clip = GifClip.open(source)
        glow_circle(canvas, (x, 314), 69, (124, 220, 231), 22)
        paste_visible(canvas, clip.at(360), (x, center_y), target_height)

    draw = ImageDraw.Draw(canvas, "RGBA")
    tracking_text(draw, (600, 212), copy["footer"], locale_font(locale, 14), (255, 236, 205, 235), 4, "ma")
    draw.line((438, 240, 762, 240), fill=(255, 203, 154, 95), width=1)
    draw.line((58, 353, 1142, 353), fill=(255, 222, 166, 90), width=2)
    draw.rounded_rectangle((2, 2, 1197, 387), radius=28, outline=(241, 187, 208, 135), width=2)
    canvas.save(OUT / localized_asset_name("collection-footer.webp", locale), format="WEBP", quality=91, method=6)


def build_hero(locale: str = "en") -> None:
    copy = LOCALES[locale]
    clips = [
        (GifClip.open("work/xiao/2d/qa/previews-final/idle.gif"), 100, 430, 0.96, 0, (86, 225, 232)),
        (GifClip.open("work/dan-heng-imbibitor-lunae/2d/qa/previews-final/idle.gif"), 285, 432, 1.18, 250, (99, 189, 214)),
        (GifClip.open("work/kiana-kaslana/2d/qa/previews-final/idle.gif"), 475, 438, 1.34, 500, (255, 210, 148)),
        (GifClip.open("work/burnice-white/2d/qa/previews/idle.gif"), 715, 438, 1.34, 700, (255, 126, 95)),
        (GifClip.open("work/miyabi/2d/qa/previews-final/idle.gif"), 920, 432, 1.18, 900, (193, 157, 255)),
        (GifClip.open("assets/readme/mitsuri-kanroji-idle.gif"), 1092, 430, 0.96, 150, (255, 137, 181)),
    ]
    frames: list[Image.Image] = []
    for index in range(FRAME_COUNT):
        canvas = gradient((1200, 460), (5, 10, 29), (41, 18, 42)).convert("RGB")
        draw = ImageDraw.Draw(canvas, "RGBA")
        for x in range(56, 1200, 64):
            draw.line((x, 28, x, 436), fill=(206, 244, 255, 10), width=1)
        for y in range(52, 430, 42):
            draw.line((30, y, 1170, y), fill=(206, 244, 255, 8), width=1)
        glow_circle(canvas, (1035, 90), 82, (255, 220, 159), 65)
        draw = ImageDraw.Draw(canvas, "RGBA")
        draw.ellipse((986, 41, 1084, 139), fill=(255, 239, 196, 242), outline=(255, 183, 200, 180), width=2)
        draw.ellipse((1014, 63, 1032, 81), fill=(211, 163, 175, 35))
        draw.arc((50, 120, 1150, 510), 194, 346, fill=(101, 228, 235, 52), width=2)
        draw.arc((140, 168, 1060, 520), 196, 344, fill=(255, 222, 151, 42), width=2)
        draw_stars(canvas, index, 28)

        draw = ImageDraw.Draw(canvas, "RGBA")
        tracking_text(draw, (600, 38), copy["hero_kicker"], locale_font(locale, 15), (147, 232, 237, 230), 5, "ma")
        draw.text(
            (600, 88),
            copy["hero_title"],
            font=locale_font(locale, 52 if locale in {"zh-CN", "ja"} else 57, bold=True),
            fill=(255, 237, 190, 255),
            stroke_width=2,
            stroke_fill=(96, 44, 72, 220),
            anchor="ma",
        )
        tracking_text(draw, (600, 151), copy["hero_subtitle"], locale_font(locale, 14), (235, 228, 250, 205), 4, "ma")

        for _, x, _, scale, _, color in clips:
            glow_circle(canvas, (x, 345), round(72 * scale), color, 44)
        for clip, x, baseline, scale, phase, _ in clips:
            place_character(canvas, clip, index * FRAME_MS, x, baseline, scale, phase)

        draw = ImageDraw.Draw(canvas, "RGBA")
        draw.line((44, 438, 1156, 438), fill=(255, 224, 157, 130), width=2)
        draw.line((44, 442, 410, 442), fill=(103, 228, 235, 120), width=1)
        draw.line((790, 442, 1156, 442), fill=(255, 132, 172, 120), width=1)
        draw.rounded_rectangle((2, 2, 1197, 457), radius=28, outline=(247, 190, 210, 150), width=2)
        frames.append(canvas.convert("RGB"))
    save_webp(frames, localized_asset_name("character-lobby.webp", locale))


def build_arrivals(locale: str = "en") -> None:
    copy = LOCALES[locale]
    clips = [
        (GifClip.open("work/seele-vollerei/2d/qa/previews-final/idle.gif"), 555, 292, 1.28, 0, copy["arrival_names"][0], (126, 220, 250)),
        (GifClip.open("work/vivian-banshee/2d/qa/previews-final/idle.gif"), 790, 292, 1.28, 360, copy["arrival_names"][1], (255, 213, 91)),
        (GifClip.open("work/kibutsuji-muzan/2d/qa/previews-final/idle.gif"), 1025, 292, 1.28, 720, copy["arrival_names"][2], (241, 105, 137)),
    ]
    frames: list[Image.Image] = []
    for index in range(FRAME_COUNT):
        canvas = gradient((1200, 330), (8, 12, 32), (46, 19, 40)).convert("RGB")
        draw = ImageDraw.Draw(canvas, "RGBA")
        draw.polygon(((0, 0), (370, 0), (210, 330), (0, 330)), fill=(205, 65, 105, 48))
        draw.line((355, 0, 198, 330), fill=(255, 144, 177, 150), width=2)
        for x in (430, 665, 900):
            draw.rounded_rectangle((x, 24, x + 205, 306), radius=22, fill=(255, 255, 255, 6), outline=(234, 224, 255, 28), width=1)
        draw_stars(canvas, index, 18)

        draw = ImageDraw.Draw(canvas, "RGBA")
        tracking_text(draw, (52, 47), copy["arrival_kicker"], locale_font(locale, 13), (133, 231, 237, 230), 4)
        draw.text((50, 82), copy["arrival_lines"][0], font=locale_font(locale, 54, bold=True), fill=(255, 239, 192), anchor="la")
        draw.text((50, 137), copy["arrival_lines"][1], font=locale_font(locale, 42 if locale == "fr" else 47, bold=True), fill=(255, 239, 192), anchor="la")
        tracking_text(draw, (53, 211), "040 — 042", font(SANS, 17), (255, 146, 180, 235), 5)
        tracking_text(draw, (53, 252), copy["arrival_available"], locale_font(locale, 12), (221, 214, 238, 175), 3)

        for _, x, _, scale, _, _, color in clips:
            glow_circle(canvas, (x, 195), round(76 * scale), color, 38)
        for clip, x, baseline, scale, phase, _, _ in clips:
            place_character(canvas, clip, index * FRAME_MS, x, baseline, scale, phase)

        draw = ImageDraw.Draw(canvas, "RGBA")
        for _, x, _, _, _, name, color in clips:
            draw.line((x - 74, 302, x + 74, 302), fill=(*color, 105), width=1)
            tracking_text(draw, (x, 308), name, locale_font(locale, 12), (*color, 235), 2, "ma")
        draw.rounded_rectangle((2, 2, 1197, 327), radius=26, outline=(245, 187, 207, 145), width=2)
        frames.append(canvas.convert("RGB"))
    save_webp(frames, localized_asset_name("new-arrivals-stage.webp", locale))


def build_motion_film(locale: str = "en") -> None:
    copy = LOCALES[locale]
    clips = [
        (copy["motion_actions"][0], copy["motion_names"][0], "work/firefly/2d/qa/previews-final/jumping.gif", (105, 225, 235), 0),
        (copy["motion_actions"][1], copy["motion_names"][1], "work/otto-apocalypse/2d/qa/previews-final/review.gif", (255, 213, 145), 270),
        (copy["motion_actions"][2], copy["motion_names"][2], "work/sunday/2d/qa/previews-final/waving.gif", (182, 166, 255), 540),
        (copy["motion_actions"][3], copy["motion_names"][3], "work/raiden-mei/2d/qa/previews-final/running.gif", (255, 133, 178), 810),
        (copy["motion_actions"][4], copy["motion_names"][4], "work/xiao/2d/qa/previews-final/waiting.gif", (111, 220, 225), 1080),
        (copy["motion_actions"][5], copy["motion_names"][5], "work/robin/2d/qa/previews-final/waving.gif", (222, 206, 255), 1350),
    ]
    loaded = [(action, name, GifClip.open(path), color, phase) for action, name, path, color, phase in clips]
    frames: list[Image.Image] = []
    for index in range(FRAME_COUNT):
        canvas = gradient((1200, 340), (6, 10, 25), (27, 17, 35)).convert("RGB")
        draw = ImageDraw.Draw(canvas, "RGBA")
        for x in range(14, 1190, 34):
            draw.rounded_rectangle((x, 10, x + 17, 20), radius=3, fill=(248, 223, 176, 50))
            draw.rounded_rectangle((x, 320, x + 17, 330), radius=3, fill=(248, 223, 176, 50))
        tracking_text(draw, (34, 31), copy["motion_kicker"], locale_font(locale, 12), (141, 230, 235, 215), 3)
        tracking_text(draw, (1166, 31), "CODEX V2", font(SANS, 12), (255, 220, 157, 190), 3, "ra")

        for slot, (action, name, clip, color, phase) in enumerate(loaded):
            left = 22 + slot * 194
            right = left + 180
            draw.rounded_rectangle((left, 55, right, 309), radius=15, fill=(255, 255, 255, 5), outline=(*color, 48), width=1)
            glow_circle(canvas, ((left + right) // 2, 190), 58, color, 28)
            place_character(canvas, clip, index * FRAME_MS, (left + right) // 2, 276, 0.92, phase)
            draw = ImageDraw.Draw(canvas, "RGBA")
            draw.line((left + 18, 280, right - 18, 280), fill=(*color, 95), width=1)
            tracking_text(draw, ((left + right) // 2, 285), action, locale_font(locale, 12), (*color, 240), 2, "ma")
            tracking_text(draw, ((left + right) // 2, 306), name, locale_font(locale, 9), (226, 220, 238, 175), 1, "ma")

        draw = ImageDraw.Draw(canvas, "RGBA")
        draw.rounded_rectangle((2, 2, 1197, 337), radius=24, outline=(242, 189, 207, 130), width=2)
        frames.append(canvas.convert("RGB"))
    save_webp(frames, localized_asset_name("motion-film.webp", locale))


def build_locale_assets(locale: str) -> None:
    build_hero(locale)
    build_arrivals(locale)
    build_motion_film(locale)
    build_collection_wall(locale)
    build_direction_orbit(locale)
    build_footer_scene(locale)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--locale", choices=LOCALES, help="build only one localized README asset set")
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    if args.locale:
        build_locale_assets(args.locale)
        return

    build_archive_previews()
    for locale in LOCALES:
        # Pillow's animated WebP encoder can retain a large native buffer after
        # each locale. A short child process keeps the complete four-language
        # build deterministic without accumulating those buffers.
        subprocess.run([sys.executable, str(Path(__file__)), "--locale", locale], check=True)


if __name__ == "__main__":
    main()

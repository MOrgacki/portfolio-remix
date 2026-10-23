"""One-off: generate placeholder images for projects without a screenshot.

Uses the legacy placeholder artwork (three dashboard screens) as a template, recolours its blue
accent to a per-project colour and replaces the caption pill.
Run from the repository root:  python -I scripts/migrate/make_placeholders.py
"""

import colorsys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "src" / "assets" / "projects"
TEMPLATE = OUT / "internal-tv-display-app.png"
FONT = Path("C:/Windows/Fonts/segoeui.ttf")

# slug -> (caption, accent colour)
PLACEHOLDERS = {
    "nft-marketplace-platform": ("NFT Marketplace", (139, 92, 246)),
    "job-listings-web-scraper-with-csv-export": ("Job Listings Scraper", (34, 197, 94)),
    "job-market-statistics-web-scraper": ("Job Market Statistics", (20, 184, 166)),
    "mmorpg-game-bot-tibia-automation": ("Tibia Automation Bot", (249, 115, 22)),
    "medical-supplements-e-commerce-platform": ("Medical Supplements Shop", (236, 72, 153)),
}

CAPTION_TOP = 535  # the legacy caption pill sits below this line


def recolour(img: Image.Image, accent: tuple[int, int, int]) -> Image.Image:
    target_h, target_s, _ = colorsys.rgb_to_hsv(*(c / 255 for c in accent))
    px = img.load()
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = px[x, y]
            if a == 0:
                continue
            h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
            # Blue accent pixels of the template (bars, title bar, sidebar marker)
            if s > 0.35 and v > 0.45 and 0.55 < h < 0.72:
                nr, ng, nb = colorsys.hsv_to_rgb(target_h, max(s, target_s * 0.85), v)
                px[x, y] = (round(nr * 255), round(ng * 255), round(nb * 255), a)
    return img


def caption(img: Image.Image, text: str, accent: tuple[int, int, int]) -> None:
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, CAPTION_TOP, img.width, img.height), fill=(0, 0, 0, 0))
    font = ImageFont.truetype(str(FONT), 15)
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    w, h = right - left, bottom - top
    pad_x, pad_y = 12, 5
    cx, cy = img.width // 2, 560
    box = (cx - w // 2 - pad_x, cy - h // 2 - pad_y - 2, cx + w // 2 + pad_x, cy + h // 2 + pad_y + 2)
    draw.rounded_rectangle(box, radius=12, fill=(*accent, 60))
    mid = tuple(round(c * 0.75 + 255 * 0.25) for c in accent)
    draw.text((cx - w // 2 - left, cy - h // 2 - top), text, font=font, fill=(*mid, 255))


def main() -> None:
    for slug, (text, accent) in PLACEHOLDERS.items():
        img = recolour(Image.open(TEMPLATE).convert("RGBA"), accent)
        caption(img, text, accent)
        img.save(OUT / f"{slug}.png", optimize=True)
        print("wrote", f"{slug}.png")


if __name__ == "__main__":
    main()

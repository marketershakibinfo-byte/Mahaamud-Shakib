"""
LinkedIn Banner Generator — Abu Shakib Sagor
Brand colors: #ff553e (coral) + #f6f2f2 (cream) + black/white
Dimensions: 1584 x 396 px (LinkedIn standard cover photo size)

Layout zones:
  - Left coral block (decorative)
  - Profile photo overlay zone: x=80-240, y=300-396 (kept low-content)
  - Center: headline + niche + stat cards
  - Right: bold CTA box
"""

from PIL import Image, ImageDraw, ImageFont
import os

# ---- Canvas ----
W, H = 1584, 396

# ---- Brand palette (from case study PDF) ----
BRAND = "#ff553e"
BG    = "#f6f2f2"
INK   = "#0d0d0d"
MUTED = "#3a3a3a"
WHITE = "#ffffff"

OUTPUT = "LinkedIn_Banner.png"


def load_font(size, bold=False):
    """Try common system font paths; fallback to default."""
    candidates_bold = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf",
        "/Library/Fonts/Arial Bold.ttf",
    ]
    candidates_regular = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/TTF/DejaVuSans.ttf",
        "/Library/Fonts/Arial.ttf",
    ]
    for p in (candidates_bold if bold else candidates_regular):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def text_width(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0]


def main():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # ---- Decorative coral diagonal block on left ----
    draw.polygon(
        [(0, 0), (380, 0), (260, H), (0, H)],
        fill=BRAND,
    )

    # Subtle accent stripe on far right edge
    draw.rectangle([W - 8, 0, W, H], fill=BRAND)

    # ---- Top brand tagline (small caps, coral) ----
    tag_font = load_font(15, bold=True)
    draw.text(
        (430, 52),
        "GOOGLE ADS SPECIALIST   \u2022   USA LOCAL BUSINESSES",
        fill=BRAND,
        font=tag_font,
    )

    # ---- Main headline (two lines) ----
    title_font = load_font(44, bold=True)
    draw.text((430, 80),  "Google Ads That Generate", fill=INK,   font=title_font)
    draw.text((430, 135), "Leads \u2014 Not Just Clicks.", fill=BRAND, font=title_font)

    # ---- Niche line ----
    niche_font = load_font(18, bold=False)
    draw.text(
        (430, 200),
        "Roofing   \u2022   HVAC   \u2022   Plumbing   \u2022   Dental   \u2022   Cleaning",
        fill=MUTED,
        font=niche_font,
    )

    # ---- Stat badges ----
    stats = [
        ("$3M+", "Revenue"),
        ("50+",  "Clients"),
        ("180+", "Campaigns"),
    ]
    bx, by = 430, 250
    bw, bh, gap = 130, 90, 14
    val_font = load_font(28, bold=True)
    lbl_font = load_font(13, bold=True)
    for i, (val, lbl) in enumerate(stats):
        x = bx + i * (bw + gap)
        # white card
        draw.rounded_rectangle([x, by, x + bw, by + bh], radius=10, fill=WHITE)
        # coral top accent
        draw.rectangle([x, by, x + bw, by + 4], fill=BRAND)
        # value (centered)
        vw = text_width(draw, val, val_font)
        draw.text((x + (bw - vw) / 2, by + 18), val, fill=BRAND, font=val_font)
        # label (centered)
        lw = text_width(draw, lbl, lbl_font)
        draw.text((x + (bw - lw) / 2, by + 60), lbl.upper(), fill=INK, font=lbl_font)

    # ---- CTA box (right) ----
    cx, cy = 1110, 80
    cw, ch = 440, 235
    draw.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=16, fill=BRAND)

    f_label   = load_font(13, bold=True)
    f_cta_top = load_font(28, bold=True)
    f_cta_mid = load_font(34, bold=True)
    f_cta_sub = load_font(15, bold=False)

    draw.text((cx + 26, cy + 22),  "FREE OFFER", fill=WHITE, font=f_label)
    draw.text((cx + 26, cy + 50),  "Burning ad spend?", fill=WHITE, font=f_cta_top)
    draw.text((cx + 26, cy + 90),  "DM \"AUDIT\"", fill=WHITE, font=f_cta_mid)
    draw.text((cx + 26, cy + 138), "Get a free 15-min Loom review", fill=WHITE, font=f_cta_sub)
    draw.text((cx + 26, cy + 160), "of your Google Ads account.", fill=WHITE, font=f_cta_sub)

    # Bottom-right arrow + handle
    f_handle = load_font(13, bold=True)
    draw.text((cx + 26, cy + ch - 32), "linkedin.com/in/abushakibsagor", fill=WHITE, font=f_handle)
    f_arrow = load_font(40, bold=True)
    draw.text((cx + cw - 56, cy + ch - 60), "\u2192", fill=WHITE, font=f_arrow)

    img.save(OUTPUT, "PNG")
    print(f"Banner generated -> {OUTPUT} ({W}x{H})")


if __name__ == "__main__":
    main()

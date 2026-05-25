"""
Premium Single-Page Google Ads Case Study PDF — Dental Niche
Palette (Google brand inspired):
  Background      #F7F8FA
  Main Heading    #111111
  Highlight       #34A853 (green) / #4285F4 (blue)
  Accent line     mixed Google colors
  Icon glow       #4285F4
  CTA / button    #34A853
  Negative UI     #EA4335
  Charts          #4285F4 + #34A853
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics

# ---- Palette ----------------------------------------------------------------
BG          = HexColor("#F7F8FA")
INK         = HexColor("#111111")
G_BLUE      = HexColor("#4285F4")
G_RED       = HexColor("#EA4335")
G_YELLOW    = HexColor("#FBBC05")
G_GREEN     = HexColor("#34A853")
MUTED       = HexColor("#5F6368")
SOFT_LINE   = HexColor("#E5E7EB")
CARD        = HexColor("#FFFFFF")
SOFT_BLUE   = HexColor("#E8F0FE")
SOFT_GREEN  = HexColor("#E6F4EA")
SOFT_RED    = HexColor("#FCE8E6")

OUTPUT = "Google_Ads_Dental_Case_Study.pdf"
PAGE_W, PAGE_H = A4   # 595.27 x 841.89 pt


# ---- helpers ---------------------------------------------------------------
def google_accent(c, x, y, length=70, thickness=2.4):
    """Small accent line made of Google's four brand colors."""
    seg = length / 4.0
    for i, col in enumerate([G_BLUE, G_RED, G_YELLOW, G_GREEN]):
        c.setFillColor(col)
        c.rect(x + i * seg, y, seg - 1, thickness, fill=1, stroke=0)


def shadow_card(c, x, y, w, h, r=8):
    """Card with a subtle shadow for premium feel."""
    c.setFillColor(HexColor("#EEF0F3"))
    c.roundRect(x + 1.2, y - 1.6, w, h, r, fill=1, stroke=0)
    c.setFillColor(CARD)
    c.roundRect(x, y, w, h, r, fill=1, stroke=0)


def pill(c, x, y, text, fill_color, text_color=white, font_size=8.5, padx=10, pady=5):
    w = pdfmetrics.stringWidth(text, "Helvetica-Bold", font_size) + padx * 2
    h = font_size + pady * 1.4
    c.setFillColor(fill_color)
    c.roundRect(x, y, w, h, h / 2, fill=1, stroke=0)
    c.setFillColor(text_color)
    c.setFont("Helvetica-Bold", font_size)
    c.drawString(x + padx, y + pady, text)
    return w


def icon_dot(c, x, y, color, glyph, size=14):
    """Small circular icon with a Google-blue glow look."""
    c.setFillColor(HexColor("#DCE7FB"))
    c.circle(x, y, size + 1.3, fill=1, stroke=0)
    c.setFillColor(color)
    c.circle(x, y, size, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", size - 3)
    c.drawCentredString(x, y - (size - 3) / 2.7, glyph)


# ---- sections --------------------------------------------------------------
def draw_background(c):
    c.setFillColor(BG)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)


def draw_header(c):
    # top white band with subtle shadow
    c.setFillColor(CARD)
    c.rect(0, PAGE_H - 78, PAGE_W, 78, fill=1, stroke=0)
    c.setFillColor(SOFT_LINE)
    c.rect(0, PAGE_H - 79, PAGE_W, 1, fill=1, stroke=0)

    # G logo block
    cx, cy = 50, PAGE_H - 39
    c.setFillColor(G_BLUE)
    c.circle(cx, cy, 18, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(cx, cy - 7, "G")

    # tiny color dots around logo
    c.setFillColor(G_RED);    c.circle(cx + 18, cy + 10, 2.2, fill=1, stroke=0)
    c.setFillColor(G_YELLOW); c.circle(cx + 20, cy - 4,  2.2, fill=1, stroke=0)
    c.setFillColor(G_GREEN);  c.circle(cx + 14, cy - 16, 2.2, fill=1, stroke=0)

    # title block
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 19)
    c.drawString(82, PAGE_H - 34, "GOOGLE ADS CASE STUDY")
    # highlight word "RESULTS" handled below
    c.setFont("Helvetica", 10)
    c.setFillColor(MUTED)
    c.drawString(82, PAGE_H - 50, "Dental Practice Growth  •  Premium Performance Marketing Report")
    google_accent(c, 82, PAGE_H - 62, length=120, thickness=2.4)

    # right header
    c.setFillColor(SOFT_GREEN)
    c.roundRect(PAGE_W - 168, PAGE_H - 52, 138, 26, 13, fill=1, stroke=0)
    c.setFillColor(G_GREEN)
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(PAGE_W - 158, PAGE_H - 44, "● VERIFIED ROI REPORT")

    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8.5)
    c.drawRightString(PAGE_W - 30, PAGE_H - 64, "90-Day Campaign Window  |  2025")


def draw_client_strip(c):
    y = PAGE_H - 118
    shadow_card(c, 28, y - 38, PAGE_W - 56, 38, r=8)

    # left accent
    c.setFillColor(G_BLUE)
    c.roundRect(28, y - 38, 4, 38, 2, fill=1, stroke=0)

    items = [
        ("CLIENT",    "Bright Smile Dental Clinic",   G_BLUE),
        ("INDUSTRY",  "Cosmetic & Family Dentistry",  G_GREEN),
        ("LOCATION",  "Dallas, TX (3 locations)",     G_RED),
        ("AD SPEND",  "$8,500 / month",               G_YELLOW),
    ]
    col_w = (PAGE_W - 80) / 4
    for i, (lbl, val, col) in enumerate(items):
        x = 44 + i * col_w
        c.setFillColor(col)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(x, y - 14, lbl)
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(x, y - 30, val)


def text_block(c, x, y, w, h, label, label_color, title, lines, bullet_color):
    shadow_card(c, x, y - h, w, h, r=8)

    # label
    c.setFillColor(label_color)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(x + 14, y - 18, label)
    google_accent(c, x + 14, y - 24, length=46, thickness=1.8)

    # title
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 11.5)
    c.drawString(x + 14, y - 42, title)

    # body
    c.setFont("Helvetica", 9)
    ty = y - 58
    for ln in lines:
        # bullet square
        c.setFillColor(bullet_color)
        c.rect(x + 14, ty + 1, 4, 4, fill=1, stroke=0)
        c.setFillColor(MUTED)
        c.drawString(x + 24, ty, ln)
        ty -= 12.5


def draw_challenge_strategy(c):
    top = PAGE_H - 165
    block_h = 158
    gap = 12
    col_w = (PAGE_W - 56 - gap) / 2

    text_block(
        c, 28, top, col_w, block_h,
        "THE CHALLENGE", G_RED,
        "Empty chairs & rising patient acquisition cost",
        [
            "Cost per booked patient stuck at $210+",
            "70% of clicks were tire-kickers, not patients",
            "Phone calls untracked — zero attribution",
            "Generic landing page, 64% bounce rate",
            "Competing with 40+ local dental clinics",
            "No-show rate above 28% on consults",
            "Insurance-only searches drained budget",
        ],
        bullet_color=G_RED,
    )

    text_block(
        c, 28 + col_w + gap, top, col_w, block_h,
        "OUR STRATEGY", G_GREEN,
        "Intent-led search + dental-specific funnel",
        [
            "SKAG account restructure (procedure-based)",
            "Mobile-first landing pages per service",
            "Call tracking + offline conversion import",
            "AI bidding with tCPA targeting new patients",
            "Geo-radius bidding (3-mile premium zone)",
            "Negative keyword sculpting — 620+ blocks",
            "Reactivation remarketing for past patients",
        ],
        bullet_color=G_GREEN,
    )


def draw_pillars(c):
    """Campaign architecture — 4 pillars."""
    top = PAGE_H - 343
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(28, top, "CAMPAIGN ARCHITECTURE")
    google_accent(c, 28, top - 6, length=70, thickness=2)

    pillars = [
        ("Search",      "High-intent procedure terms\n(implants, veneers, invisalign)", G_BLUE,   "S"),
        ("Performance Max", "Asset groups by service\nwith dental imagery", G_GREEN, "P"),
        ("Local",       "3-mile geo bidding\nGoogle Maps placements",                G_YELLOW, "L"),
        ("Remarketing", "Past visitors + lookalike\nreactivation funnel",            G_RED,    "R"),
    ]
    y = top - 22
    h = 70
    gap = 10
    w = (PAGE_W - 56 - gap * 3) / 4
    for i, (name, desc, col, glyph) in enumerate(pillars):
        x = 28 + i * (w + gap)
        shadow_card(c, x, y - h, w, h, r=8)
        # top accent
        c.setFillColor(col)
        c.roundRect(x, y - 4, w, 4, 2, fill=1, stroke=0)
        # icon
        icon_dot(c, x + 22, y - 26, col, glyph, size=11)
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(x + 42, y - 24, name)
        # description
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 8.2)
        ty = y - 44
        for ln in desc.split("\n"):
            c.drawString(x + 14, ty, ln)
            ty -= 10


def kpi_card(c, x, y, w, h, value, label, delta, color, positive=True):
    shadow_card(c, x, y - h, w, h, r=8)
    c.setFillColor(color)
    c.roundRect(x, y - 4, w, 4, 2, fill=1, stroke=0)

    c.setFillColor(color)
    c.setFont("Helvetica-Bold", 22)
    c.drawString(x + 14, y - 34, value)

    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(x + 14, y - 50, label)

    # delta pill
    pill_color = SOFT_GREEN if positive else SOFT_RED
    text_color = G_GREEN if positive else G_RED
    arrow = "▲ " if positive else "▼ "
    text = arrow + delta
    tw = pdfmetrics.stringWidth(text, "Helvetica-Bold", 7.5) + 12
    c.setFillColor(pill_color)
    c.roundRect(x + 14, y - 70, tw, 12, 6, fill=1, stroke=0)
    c.setFillColor(text_color)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(x + 20, y - 67, text)


def draw_results(c):
    top = PAGE_H - 432
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(28, top, "THE RESULTS")
    c.setFillColor(G_GREEN)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(110, top, "// 90 DAYS")
    google_accent(c, 28, top - 6, length=70, thickness=2)

    y = top - 12
    h = 84
    gap = 10
    w = (PAGE_W - 56 - gap * 3) / 4
    cards = [
        ("587",   "New Patient Leads", "412% vs. prior",       G_BLUE,  True),
        ("$38",   "Cost per Lead",     "82% lower",            G_GREEN, True),
        ("12.4%", "Conversion Rate",   "+5.8% lift",           G_BLUE,  True),
        ("9.2x",  "Return on Ad Spend","$76,500 → $703,800",   G_GREEN, True),
    ]
    for i, (v, l, d, col, pos) in enumerate(cards):
        kpi_card(c, 28 + i * (w + gap), y, w, h, v, l, d, col, pos)


def draw_funnel_and_chart(c):
    """Left: funnel.  Right: before vs after bar chart."""
    top = PAGE_H - 540
    h = 130
    gap = 12
    left_w = (PAGE_W - 56 - gap) * 0.58
    right_w = (PAGE_W - 56 - gap) * 0.42

    # ---- funnel card ----
    fx, fy = 28, top
    shadow_card(c, fx, fy - h, left_w, h, r=8)
    c.setFillColor(G_BLUE)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(fx + 14, fy - 18, "PATIENT JOURNEY FUNNEL")
    google_accent(c, fx + 14, fy - 24, length=46, thickness=1.8)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(fx + 14, fy - 40, "From impression to booked dental appointment")

    stages = [
        ("186,420", "Impressions",        G_BLUE),
        ("14,720",  "Clicks (7.9% CTR)",  G_BLUE),
        ("4,724",   "Landing Visits",     G_YELLOW),
        ("587",     "Leads (Form+Call)",  G_GREEN),
        ("311",     "Booked Patients",    G_GREEN),
    ]
    sx = fx + 14
    sy = fy - 76
    sw = (left_w - 28) / len(stages)
    for i, (num, lbl, col) in enumerate(stages):
        x = sx + i * sw
        # stage card
        c.setFillColor(BG)
        c.roundRect(x + 2, sy - 30, sw - 6, 44, 5, fill=1, stroke=0)
        c.setFillColor(col)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(x + 8, sy - 2, num)
        c.setFillColor(INK)
        c.setFont("Helvetica", 7.2)
        c.drawString(x + 8, sy - 14, lbl)
        # mini bar
        bar_w = (sw - 14) * (1 - i * 0.16)
        c.setFillColor(col)
        c.rect(x + 8, sy - 24, max(bar_w, 8), 4, fill=1, stroke=0)
        # arrow
        if i < len(stages) - 1:
            c.setFillColor(MUTED)
            c.setFont("Helvetica-Bold", 11)
            c.drawString(x + sw - 8, sy - 6, "›")

    # ---- bar chart card ----
    bx = fx + left_w + gap
    shadow_card(c, bx, fy - h, right_w, h, r=8)
    c.setFillColor(G_GREEN)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(bx + 14, fy - 18, "BEFORE vs AFTER")
    google_accent(c, bx + 14, fy - 24, length=46, thickness=1.8)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(bx + 14, fy - 40, "Monthly performance lift")

    # bars
    metrics = [
        ("Leads",   114, 587),
        ("CPL",     210,  38),   # lower is better — visual still shows green smaller
        ("ROAS",     21,  92),   # x10 for visual (2.1x -> 9.2x)
    ]
    chart_x = bx + 22
    chart_y = fy - 116
    chart_w = right_w - 44
    bar_h = 10
    row_gap = 22

    max_blue = max(m[1] for m in metrics)
    max_green = max(m[2] for m in metrics)
    overall = max(max_blue, max_green)

    for i, (name, before, after) in enumerate(metrics):
        ry = chart_y + i * row_gap
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(chart_x, ry + 14, name)

        # before bar (blue) - lower is better for CPL so we still draw fairly
        bw = (before / overall) * (chart_w - 50)
        c.setFillColor(G_BLUE)
        c.roundRect(chart_x + 40, ry + 10, max(bw, 4), bar_h / 1.4, 2, fill=1, stroke=0)
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 7)
        c.drawString(chart_x + 42 + bw + 2, ry + 12, str(before))

        # after bar (green)
        aw = (after / overall) * (chart_w - 50)
        c.setFillColor(G_GREEN)
        c.roundRect(chart_x + 40, ry, max(aw, 4), bar_h / 1.4, 2, fill=1, stroke=0)
        c.setFillColor(MUTED)
        c.drawString(chart_x + 42 + aw + 2, ry + 2, str(after))

    # legend
    c.setFillColor(G_BLUE)
    c.rect(bx + 14, fy - h + 10, 8, 6, fill=1, stroke=0)
    c.setFillColor(MUTED); c.setFont("Helvetica", 7.5)
    c.drawString(bx + 26, fy - h + 11, "Before")
    c.setFillColor(G_GREEN)
    c.rect(bx + 70, fy - h + 10, 8, 6, fill=1, stroke=0)
    c.setFillColor(MUTED)
    c.drawString(bx + 82, fy - h + 11, "After")


def draw_extras_row(c):
    """Conversion improvements + Testimonial side by side."""
    top = PAGE_H - 685
    h = 78
    gap = 12
    left_w = (PAGE_W - 56 - gap) * 0.46
    right_w = (PAGE_W - 56 - gap) * 0.54

    # ---- conversion improvements ----
    shadow_card(c, 28, top - h, left_w, h, r=8)
    c.setFillColor(G_BLUE)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(42, top - 18, "QUALITY IMPROVEMENTS")
    google_accent(c, 42, top - 24, length=46, thickness=1.8)

    items = [
        ("Bounce rate",      "64% → 27%", G_GREEN),
        ("No-show rate",     "28% → 9%",  G_GREEN),
        ("High-value cases", "12 → 71",   G_GREEN),
        ("Quality Score avg","5.2 → 8.7", G_GREEN),
    ]
    col1_x, col2_x = 42, 42 + (left_w / 2)
    for i, (k, v, col) in enumerate(items):
        col_x = col1_x if i < 2 else col2_x
        ry = top - 40 - (i % 2) * 16
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 8.5)
        c.drawString(col_x, ry, k)
        c.setFillColor(col)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(col_x + 90, ry, v)

    # ---- testimonial ----
    tx = 28 + left_w + gap
    shadow_card(c, tx, top - h, right_w, h, r=8)
    # left blue band
    c.setFillColor(G_BLUE)
    c.roundRect(tx, top - h, 4, h, 2, fill=1, stroke=0)
    # quote mark
    c.setFillColor(G_BLUE)
    c.setFont("Helvetica-Bold", 36)
    c.drawString(tx + 14, top - 36, "“")
    c.setFillColor(INK)
    c.setFont("Helvetica-Oblique", 9)
    c.drawString(tx + 44, top - 22,
                 "Our chairs are full and our front desk can finally")
    c.drawString(tx + 44, top - 34,
                 "breathe. We added 311 new patients in 90 days —")
    c.drawString(tx + 44, top - 46,
                 "the ROI is unreal. This is the team to work with.")
    c.setFillColor(G_GREEN)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(tx + 44, top - 62, "— Dr. Sarah Mitchell, DDS")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8)
    c.drawString(tx + 44, top - 72, "Owner, Bright Smile Dental Clinic")


def draw_services_strip(c):
    top = PAGE_H - 780
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(28, top, "WHAT WE DELIVERED")
    google_accent(c, 28, top - 6, length=70, thickness=2)

    items = [
        ("Search Campaigns", G_BLUE),
        ("Performance Max",  G_GREEN),
        ("Call Tracking",    G_BLUE),
        ("Landing Pages",    G_GREEN),
        ("Conversion API",   G_BLUE),
        ("Bid Automation",   G_GREEN),
        ("A/B Testing",      G_BLUE),
        ("Reporting",        G_GREEN),
    ]
    y = top - 24
    x = 28
    for label, col in items:
        w = pill(c, x, y, label, col, font_size=8.2, padx=9, pady=4)
        x += w + 6


def draw_footer(c):
    # CTA band — Google green
    c.setFillColor(G_GREEN)
    c.rect(0, 0, PAGE_W, 42, fill=1, stroke=0)

    # diagonal accent of Google colors on top of footer
    seg_w = PAGE_W / 4
    for i, col in enumerate([G_BLUE, G_RED, G_YELLOW, G_GREEN]):
        c.setFillColor(col)
        c.rect(i * seg_w, 42, seg_w, 2, fill=1, stroke=0)

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(28, 24, "MAHAMUD SHAKIB")
    c.setFont("Helvetica", 8.5)
    c.drawString(28, 11, "Google Ads Specialist  •  Performance Marketing  •  Dental Niche")

    # CTA pill
    c.setFillColor(white)
    cta_w = 168
    c.roundRect(PAGE_W - cta_w - 28, 10, cta_w, 22, 11, fill=1, stroke=0)
    c.setFillColor(G_GREEN)
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(PAGE_W - cta_w - 14, 17, "BOOK A FREE STRATEGY CALL  ›")


# ---- main ------------------------------------------------------------------
def build_pdf():
    c = canvas.Canvas(OUTPUT, pagesize=A4)
    c.setTitle("Google Ads Case Study — Dental")
    c.setAuthor("Mahamud Shakib")
    c.setSubject("Premium Dental Performance Marketing Case Study")

    draw_background(c)
    draw_header(c)
    draw_client_strip(c)
    draw_challenge_strategy(c)
    draw_pillars(c)
    draw_results(c)
    draw_funnel_and_chart(c)
    draw_extras_row(c)
    draw_services_strip(c)
    draw_footer(c)

    c.showPage()
    c.save()
    print(f"PDF generated -> {OUTPUT}")


if __name__ == "__main__":
    build_pdf()

"""
Premium Single-Page Google Ads Case Study PDF — Roofing Niche
Brand color: #ff553e | Background: #f6f2f2 | Font: Black & #ff553e
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm

# ---- Brand palette -----------------------------------------------------------
BRAND      = HexColor("#ff553e")
BG         = HexColor("#f6f2f2")
INK        = black
MUTED      = HexColor("#3a3a3a")
SOFT_LINE  = HexColor("#e7dede")
CARD       = HexColor("#ffffff")

OUTPUT = "Google_Ads_Roofing_Case_Study.pdf"

PAGE_W, PAGE_H = A4   # 595.27 x 841.89 pt


def draw_background(c):
    c.setFillColor(BG)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)


def draw_header(c):
    # Top brand bar
    c.setFillColor(BRAND)
    c.rect(0, PAGE_H - 70, PAGE_W, 70, fill=1, stroke=0)

    # Logo block (square)
    c.setFillColor(white)
    c.roundRect(28, PAGE_H - 58, 46, 46, 6, fill=1, stroke=0)
    c.setFillColor(BRAND)
    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(51, PAGE_H - 45, "G")
    c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(51, PAGE_H - 56, "ADS")

    # Title
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(90, PAGE_H - 35, "GOOGLE ADS CASE STUDY")
    c.setFont("Helvetica", 10)
    c.drawString(90, PAGE_H - 52, "Roofing Lead Generation  •  Performance Marketing Report")

    # Right side stamp
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 10)
    c.drawRightString(PAGE_W - 28, PAGE_H - 35, "PREMIUM REPORT")
    c.setFont("Helvetica", 9)
    c.drawRightString(PAGE_W - 28, PAGE_H - 50, "90-Day Campaign  |  2025")


def draw_client_strip(c):
    y = PAGE_H - 110
    c.setFillColor(CARD)
    c.roundRect(28, y - 38, PAGE_W - 56, 38, 6, fill=1, stroke=0)

    # accent bar
    c.setFillColor(BRAND)
    c.roundRect(28, y - 38, 4, 38, 2, fill=1, stroke=0)

    c.setFillColor(BRAND)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(44, y - 14, "CLIENT")
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(44, y - 28, "Apex Roofing & Restoration")

    c.setFillColor(BRAND)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(220, y - 14, "INDUSTRY")
    c.setFillColor(INK)
    c.setFont("Helvetica", 11)
    c.drawString(220, y - 28, "Residential & Commercial Roofing")

    c.setFillColor(BRAND)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(400, y - 14, "LOCATION")
    c.setFillColor(INK)
    c.setFont("Helvetica", 11)
    c.drawString(400, y - 28, "Texas, USA")

    c.setFillColor(BRAND)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(490, y - 14, "BUDGET")
    c.setFillColor(INK)
    c.setFont("Helvetica", 11)
    c.drawString(490, y - 28, "$6,000 / mo")


# Reusable text section
def text_block(c, x, y, w, h, label, title, lines):
    c.setFillColor(CARD)
    c.roundRect(x, y - h, w, h, 8, fill=1, stroke=0)
    # label
    c.setFillColor(BRAND)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(x + 14, y - 18, label)
    # underline
    c.setStrokeColor(BRAND)
    c.setLineWidth(1.4)
    c.line(x + 14, y - 22, x + 14 + 22, y - 22)
    # title
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(x + 14, y - 40, title)
    # body
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 9)
    ty = y - 56
    for ln in lines:
        c.drawString(x + 14, ty, ln)
        ty -= 12


def draw_challenge_strategy(c):
    top = PAGE_H - 162
    block_h = 150
    gap = 12
    col_w = (PAGE_W - 56 - gap) / 2

    text_block(
        c, 28, top, col_w, block_h,
        "THE CHALLENGE",
        "Low quality leads & high CPL",
        [
            "•  Cost per lead exceeded $180 with weak intent",
            "•  Phone calls were not tracked or attributed",
            "•  Generic keywords drained budget on tire-kickers",
            "•  No dedicated landing page — bouncing at 71%",
            "•  Competing with 30+ local roofers on same terms",
        ],
    )

    text_block(
        c, 28 + col_w + gap, top, col_w, block_h,
        "OUR STRATEGY",
        "Intent-first search + local geo targeting",
        [
            "•  Restructured account into SKAG + tight match types",
            "•  Built high-converting landing page (mobile-first)",
            "•  Added call tracking & offline conversion imports",
            "•  Negative keyword sculpting — 480+ terms blocked",
            "•  Storm-season bid scheduling & geo radius bidding",
        ],
    )


def kpi_card(c, x, y, w, h, value, label, delta):
    c.setFillColor(CARD)
    c.roundRect(x, y - h, w, h, 8, fill=1, stroke=0)
    # top accent
    c.setFillColor(BRAND)
    c.roundRect(x, y - 4, w, 4, 2, fill=1, stroke=0)

    c.setFillColor(BRAND)
    c.setFont("Helvetica-Bold", 22)
    c.drawString(x + 14, y - 36, value)

    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(x + 14, y - 54, label)

    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8)
    c.drawString(x + 14, y - 67, delta)


def draw_results(c):
    top = PAGE_H - 330
    # Section header
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(28, top + 4, "THE RESULTS")
    c.setFillColor(BRAND)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(120, top + 4, "// 90 DAYS")
    c.setStrokeColor(BRAND)
    c.setLineWidth(1.2)
    c.line(28, top - 4, 80, top - 4)

    # 4 KPI cards
    y = top - 12
    h = 78
    gap = 10
    w = (PAGE_W - 56 - gap * 3) / 4
    cards = [
        ("412",     "Qualified Leads",     "+318% vs. prior period"),
        ("$42",     "Cost per Lead",       "down from $180  (-77%)"),
        ("11.6%",   "Conversion Rate",     "+4.1% landing page lift"),
        ("6.8x",    "Return on Ad Spend",  "$40,800 → $277,440 rev"),
    ]
    for i, (v, l, d) in enumerate(cards):
        kpi_card(c, 28 + i * (w + gap), y, w, h, v, l, d)


def draw_funnel(c):
    top = PAGE_H - 432
    c.setFillColor(CARD)
    c.roundRect(28, top - 96, PAGE_W - 56, 96, 8, fill=1, stroke=0)

    c.setFillColor(BRAND)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(44, top - 18, "PERFORMANCE BREAKDOWN")
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(44, top - 34, "From impression to booked roofing job")

    # funnel stages
    stages = [
        ("142,300", "Impressions"),
        ("9,840",   "Clicks  (6.9% CTR)"),
        ("3,556",   "Landing Page Visits"),
        ("412",     "Form & Call Leads"),
        ("184",     "Booked Inspections"),
    ]
    sx = 44
    sy = top - 62
    sw = (PAGE_W - 88) / len(stages)
    for i, (num, lbl) in enumerate(stages):
        x = sx + i * sw
        c.setFillColor(BG)
        c.roundRect(x + 4, sy - 22, sw - 8, 30, 5, fill=1, stroke=0)
        c.setFillColor(BRAND)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(x + 12, sy - 4, num)
        c.setFillColor(INK)
        c.setFont("Helvetica", 8)
        c.drawString(x + 12, sy - 16, lbl)
        # arrow
        if i < len(stages) - 1:
            c.setFillColor(BRAND)
            c.setFont("Helvetica-Bold", 12)
            c.drawString(x + sw - 6, sy - 8, "›")


def draw_testimonial(c):
    top = PAGE_H - 545
    c.setFillColor(BRAND)
    c.roundRect(28, top - 70, PAGE_W - 56, 70, 8, fill=1, stroke=0)

    # big quote mark
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 46)
    c.drawString(40, top - 32, "“")

    c.setFillColor(white)
    c.setFont("Helvetica-Oblique", 10.5)
    c.drawString(76, top - 26,
                 "We went from struggling to fill the calendar to turning")
    c.drawString(76, top - 40,
                 "down jobs. Our phone hasn't stopped ringing — best")
    c.drawString(76, top - 54,
                 "ad spend decision we ever made for the roofing business.")

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 9)
    c.drawRightString(PAGE_W - 44, top - 46, "— Marcus R.")
    c.setFont("Helvetica", 8)
    c.drawRightString(PAGE_W - 44, top - 58, "Owner, Apex Roofing & Restoration")


def draw_services_strip(c):
    top = PAGE_H - 632
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(28, top, "WHAT WE DELIVERED")
    c.setStrokeColor(BRAND)
    c.setLineWidth(1.2)
    c.line(28, top - 6, 80, top - 6)

    items = [
        "Search Campaigns",
        "Performance Max",
        "Call Tracking",
        "Landing Page",
        "Conversion API",
        "Bid Automation",
    ]
    y = top - 24
    x = 28
    for it in items:
        text_w = pdfmetrics.stringWidth(it, "Helvetica-Bold", 9) + 22
        c.setFillColor(BRAND)
        c.roundRect(x, y - 14, text_w, 18, 9, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(x + 11, y - 9, it)
        x += text_w + 8


def draw_footer(c):
    # bottom band
    c.setFillColor(BRAND)
    c.rect(0, 0, PAGE_W, 38, fill=1, stroke=0)

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(28, 22, "MAHAMUD SHAKIB")
    c.setFont("Helvetica", 8.5)
    c.drawString(28, 10, "Google Ads Specialist  •  Performance Marketing  •  Roofing Niche")

    c.setFont("Helvetica-Bold", 9)
    c.drawRightString(PAGE_W - 28, 22, "Ready to grow your roofing business?")
    c.setFont("Helvetica", 8.5)
    c.drawRightString(PAGE_W - 28, 10, "Book a free strategy call  →  shakib@mahamud.ads")


def build_pdf():
    c = canvas.Canvas(OUTPUT, pagesize=A4)
    c.setTitle("Google Ads Case Study — Roofing")
    c.setAuthor("Mahamud Shakib")
    c.setSubject("Premium Performance Marketing Case Study")

    draw_background(c)
    draw_header(c)
    draw_client_strip(c)
    draw_challenge_strategy(c)
    draw_results(c)
    draw_funnel(c)
    draw_testimonial(c)
    draw_services_strip(c)
    draw_footer(c)

    c.showPage()
    c.save()
    print(f"PDF generated -> {OUTPUT}")


if __name__ == "__main__":
    build_pdf()

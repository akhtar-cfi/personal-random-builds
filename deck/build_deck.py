# Crashfree India — Partner Overview Deck (15 slides)
# Built per CFI design skill §14: python-pptx, Montserrat/Geist, 16:9, safe zones.
import os
from cfi_helpers import *  # tokens, helpers, prs

A = os.path.join(os.path.dirname(BUILD_DIR), "assets")
TOTAL = 15
BLUE_HEX = "#4A35FF"; WHITE_HEX = "#FFFFFF"; MUTED_HEX = "#777589"
DANGER_HEX = "#F10015"; LAVDK_HEX = "#6A55FF"

def footer_dark(slide, idx, label):
    text(slide, M_L, Inches(7.12), Inches(8), Inches(0.3), label, font=HEAD, size=8.5,
         color=LAV, tracking=1.6, bold=True)
    text(slide, Inches(11.4), Inches(7.12), Inches(1.4), Inches(0.3), f"{idx:02d} / {TOTAL:02d}",
         font=HEAD, size=8.5, color=LAV, tracking=1.6, bold=True, align=PP_ALIGN.RIGHT)

def chip(slide, x, y, w, h, label, fill=BRAND_LITE, tcolor=BRAND, size=9.5, bold=True, line=None):
    rect(slide, x, y, w, h, fill, line=line, rounded=True)
    text(slide, x+Inches(0.12), y, w-Inches(0.24), h, label, font=HEAD, size=size, bold=bold,
         color=tcolor, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, ls=1.0)

# ============================================================ S1 COVER
s = new_slide(WHITE)
logo(s, M_L, Inches(0.55), Inches(2.7))
# right brand band
BAND_X = Inches(9.73)
rect(s, BAND_X, 0, SLIDE_W-BAND_X, SLIDE_H, BRAND)
sparkle(s, Inches(12.30), Inches(0.42), Inches(0.52), WHITE)
sparkle(s, Inches(12.02), Inches(0.86), Inches(0.30), WHITE)
tags = [("I", "THE PROBLEM"), ("II", "WHO WE ARE"), ("III", "WHAT WE DO"), ("IV", "OUR PEOPLE")]
ty = Inches(1.7)
for rn, tag in tags:
    text(s, BAND_X+Inches(0.5), ty, Inches(0.55), Inches(0.35), rn, font=HEAD, size=12, bold=True, color=LAV)
    text(s, BAND_X+Inches(1.1), ty+Inches(0.02), Inches(2.3), Inches(0.35), tag, font=HEAD, size=10,
         bold=True, color=WHITE, tracking=1.8)
    if tag != "OUR PEOPLE":
        hline(s, BAND_X+Inches(0.5), ty+Inches(0.5), Inches(2.55), color=LAV_DK, wt=0.75)
    ty += Inches(0.72)
# Dhoni cutout, subtle, anchored to band bottom (photo: CFI shoot, June 2026)
try:
    from PIL import Image as _Img
    _d = _Img.open(os.path.join(BUILD_DIR, "dhoni_cutout_helmet.png"))
    _ar = _d.width/_d.height
    DH = Inches(2.8); DW = Inches(2.8*_ar)
    s.shapes.add_picture(os.path.join(BUILD_DIR, "dhoni_cutout_helmet.png"),
                         SLIDE_W-DW-Inches(0.62), SLIDE_H-DH, width=DW, height=DH)
    text(s, BAND_X+Inches(0.5), Inches(4.42), Inches(2.7), Inches(0.3),
         "MS DHONI · GOODWILL AMBASSADOR", font=HEAD, size=7.5, bold=True, color=LAV, tracking=1.4)
except Exception as e:
    print("cover dhoni missing", e)
# left title block
eyebrow(s, M_L, Inches(2.85), "CRASHFREE INDIA  ·  A CARS24 COMMITMENT")
text(s, M_L, Inches(3.22), Inches(8.7), Inches(1.9),
     "Systems work because", font=HEAD, size=40, bold=True, color=DARK, ls=1.04)
text(s, M_L, Inches(3.94), Inches(8.7), Inches(0.9),
     "we hold them accountable.", font=HEAD, size=40, bold=True, color=BRAND, ls=1.04)
text(s, M_L, Inches(4.95), Inches(8.4), Inches(0.6),
     "Who we are, what we do, and what we have built — a nonprofit working for zero road deaths in India by 2040.",
     font=BODY, size=14, color=MUTED, ls=1.4)
hline(s, M_L, Inches(6.55), Inches(8.3), color=BORDER, wt=1.0)
text(s, M_L, Inches(6.75), Inches(8.4), Inches(0.35),
     "Partner overview  ·  July 2026  ·  crashfreeindia.org", font=HEAD, size=9.5,
     color=MUTED, tracking=1.6, bold=True)

# ============================================================ S2 THE SHIFT
s = new_slide(WHITE)
ny = std_header(s, "THE PROBLEM · WHY ROAD DEATHS PERSIST",
                "Most road deaths in India are failures of",
                "roads and systems — not just of drivers.")
# left giant stat
text(s, M_L, Inches(2.55), Inches(5.2), Inches(2.0), "59%", font=HEAD, size=120, bold=True, color=BRAND, ls=0.95)
text(s, M_L, Inches(4.55), Inches(5.0), Inches(0.9),
     "of road deaths in India involve no traffic\nviolation by the victim at all.",
     font=BODY, size=13.5, color=DARK, ls=1.35)
text(s, M_L, Inches(5.42), Inches(5.0), Inches(0.3), "Ministry of Road Transport & Highways data",
     font=BODY, size=9.5, color=MUTED, italic=True)
# right: what changed rows
RX = Inches(6.6); RW = Inches(6.0)
rows = [
    ("database", "Crash records went digital", "e-DAR and digitised FIRs make every death traceable to a place, a road design, a file."),
    ("scan-line", "Vehicles became identifiable", "ANPR cameras and live national vehicle APIs surface repeat offenders instantly."),
    ("chart-column", "Failure became attributable", "Open data ties deaths to specific junctions, specific processes, specific desks."),
]
ry = Inches(2.5)
for icn, t1, t2 in rows:
    circle(s, RX, ry, Inches(0.5), BRAND_LITE)
    icon(s, icn, RX+Inches(0.11), ry+Inches(0.11), Inches(0.28), BLUE_HEX)
    text(s, RX+Inches(0.72), ry-Inches(0.02), RW-Inches(0.75), Inches(0.3), t1, font=HEAD, size=13, bold=True, color=DARK)
    text(s, RX+Inches(0.72), ry+Inches(0.30), RW-Inches(0.75), Inches(0.6), t2, font=BODY, size=10.5, color=MUTED, ls=1.3)
    ry += Inches(1.02)
# bottom strip
rect(s, M_L, Inches(6.05), CONTENT_W, Inches(0.55), BRAND_LITE, rounded=True)
text(s, M_L+Inches(0.3), Inches(6.05), CONTENT_W-Inches(0.6), Inches(0.55),
     "India has strong road-safety laws. What has been missing is an institution that makes them work on the ground.",
     font=HEAD, size=12, bold=True, color=BRAND, anchor=MSO_ANCHOR.MIDDLE)
footer(s, 2, TOTAL, "THE PROBLEM")

# ============================================================ S3 THE STAKES (held breath, red #1)
s = new_slide(WHITE)
eyebrow(s, M_L, Inches(0.55), "THE PROBLEM · THE SCALE")
text(s, Inches(0.7), Inches(1.15), Inches(11.9), Inches(2.6), "485",
     font=HEAD, size=210, bold=True, color=DANGER, align=PP_ALIGN.CENTER, ls=0.9)
text(s, Inches(0.7), Inches(4.05), Inches(11.9), Inches(0.5),
     "people are killed on Indian roads every single day.",
     font=HEAD, size=19, bold=True, color=DARK, align=PP_ALIGN.CENTER)
# metronome chip
chip(s, Inches(5.32), Inches(4.75), Inches(2.7), Inches(0.44), "ONE DEATH EVERY 3 MINUTES",
     fill=BRAND_LITE, tcolor=BRAND, size=10)
stats = [("1,77,175", "killed in 2024"), ("66%", "aged 18–34"), ("1% → 11%", "of world's vehicles → of its road deaths")]
sw = Inches(3.4); gap = Inches(0.35); sx = (SLIDE_W - sw*3 - gap*2)/2
for i,(num,lab) in enumerate(stats):
    x = sx + i*(sw+gap)
    text(s, x, Inches(5.55), sw, Inches(0.5), num, font=HEAD, size=24, bold=True, color=DARK, align=PP_ALIGN.CENTER)
    text(s, x, Inches(6.05), sw, Inches(0.3), lab, font=BODY, size=10.5, color=MUTED, align=PP_ALIGN.CENTER)
text(s, Inches(0.7), Inches(6.55), Inches(11.9), Inches(0.3),
     "Source: MoRTH, Road Accidents in India 2024 · Crashfree India Crash Data Dashboard",
     font=BODY, size=9, color=MUTED, italic=True, align=PP_ALIGN.CENTER)
footer(s, 3, TOTAL, "THE PROBLEM · THE SCALE")

# ============================================================ S4 THE FINDING (brand)
s = new_slide(BRAND)
logo(s, M_L, Inches(0.5), Inches(2.1), dark=True)
sparkles_tr(s, LAV_DK)
text(s, M_L, Inches(1.35), Inches(11.9), Inches(0.4), "THE PROBLEM · THREE GAPS", font=HEAD, size=10, bold=True,
     color=LAV, tracking=2.4)
text(s, M_L, Inches(1.75), Inches(11.9), Inches(0.65), "Where the system fails today.",
     font=HEAD, size=30, bold=True, color=WHITE)
text(s, M_L, Inches(2.42), Inches(11.5), Inches(0.4),
     "We studied how India responds to a road death. Three gaps repeat everywhere — and no institution owns the follow-through.",
     font=BODY, size=12, color=LAV, ls=1.35)
cards = [
    ("traffic-cone", "GAP 1 · DANGEROUS ROADS", "Audits stop at the report.",
     "Hazards get reported and studies get filed — but no institution tracks whether a single fix is ever built."),
    ("scale", "GAP 2 · COMPENSATION", "₹80,000 Cr sits undelivered.",
     "10.46 lakh compensation cases pending. In one Gurugram audit: 102 hit-and-run files since 2022 — only 2 settled."),
    ("siren", "GAP 3 · ENFORCEMENT", "Repeat offenders go unchecked.",
     "46 crore e-challans issued, ~75% unpaid — while roadside enforcement still stops vehicles at random."),
]
cw = Inches(3.85); gap = Inches(0.19); cx = M_L; cy = Inches(3.1); ch = Inches(2.85)
for icn, kick, t1, t2 in cards:
    rect(s, cx, cy, cw, ch, RGBColor(0x5A,0x46,0xFF), rounded=True)
    circle(s, cx+Inches(0.3), cy+Inches(0.3), Inches(0.55), LAV_DK)
    icon(s, icn, cx+Inches(0.42), cy+Inches(0.42), Inches(0.31), WHITE_HEX)
    text(s, cx+Inches(0.3), cy+Inches(1.02), cw-Inches(0.6), Inches(0.3), kick, font=HEAD, size=9,
         bold=True, color=LAV, tracking=1.8)
    text(s, cx+Inches(0.3), cy+Inches(1.32), cw-Inches(0.6), Inches(0.65), t1, font=HEAD, size=14.5,
         bold=True, color=WHITE, ls=1.12)
    text(s, cx+Inches(0.3), cy+Inches(1.98), cw-Inches(0.6), Inches(0.8), t2, font=BODY, size=10,
         color=LAV, ls=1.3)
    cx += cw + gap
text(s, M_L, Inches(6.28), Inches(11.9), Inches(0.4),
     "The distance between what is known and what gets done is the gap Crashfree India was created to close.",
     font=HEAD, size=12.5, bold=True, color=WHITE, ls=1.3)
footer_dark(s, 4, "THE PROBLEM · THREE GAPS")

# ============================================================ S5 THE INSTITUTION
s = new_slide(WHITE)
ny = std_header(s, "WHO WE ARE · ABOUT CRASHFREE INDIA",
                "A nonprofit institution working towards",
                "zero road deaths in India by 2040.",
                "Launched in June 2025 and funded by Cars24, we identify road-safety failures, get fixes approved by government, and track every fix to completion.")
tiles = [
    ("calendar", "Founded June 2025", "Launched by Cars24 with the Indian Road Safety Campaign; roots in a decade of IRSC campus audit work."),
    ("indian-rupee", "$3M over 3 years", "Cars24's committed institutional funding — programme-first: 71% of FY26-27 budget goes to programmes."),
    ("landmark", "Vision Zero Trust", "Registered public trust; trustees include Cars24 co-founder Gajendra Jangid."),
    ("target", "One north star", "Zero road fatalities in India by 2040 — pursued as system repair, not sensitisation."),
    ("map-pin", "18 cities and counting", "Programmes live across India — Delhi NCR, Jaipur, Indore, Bengaluru, Chennai, Guwahati and more."),
    ("mic", "MS Dhoni", "Goodwill Ambassador since April 2026 — lending India's most trusted voice to the cause."),
]
cw = Inches(3.85); ch = Inches(1.62); gap = Inches(0.19)
for i,(icn,t1,t2) in enumerate(tiles):
    x = M_L + (i%3)*(cw+gap); y = Inches(2.95) + (i//3)*(ch+Inches(0.2))
    rect(s, x, y, cw, ch, WHITE, line=BORDER, rounded=True)
    circle(s, x+Inches(0.22), y+Inches(0.22), Inches(0.44), BRAND_LITE)
    icon(s, icn, x+Inches(0.31), y+Inches(0.31), Inches(0.26), BLUE_HEX)
    text(s, x+Inches(0.8), y+Inches(0.24), cw-Inches(1.0), Inches(0.3), t1, font=HEAD, size=12.5, bold=True, color=DARK)
    text(s, x+Inches(0.22), y+Inches(0.72), cw-Inches(0.44), Inches(0.85), t2, font=BODY, size=9.5, color=MUTED, ls=1.28)
footer(s, 5, TOTAL, "ABOUT CRASHFREE INDIA")

# ============================================================ S6 OPERATING MODEL
s = new_slide(BRAND_LITE)
ny = std_header(s, "WHO WE ARE · OUR APPROACH",
                "How we work: audit, advocate, and",
                "follow through until the fix is built.")
# left: loop blocks
steps = [
    ("search-check", "AUDIT", "Find", "Field evidence to IRC / MoRTH standards — blackspots, claim files, enforcement gaps."),
    ("megaphone", "ADVOCATE", "Name", "Findings published and presented — to district committees, state departments, MoRTH, the press."),
    ("badge-check", "ACCOUNTABILITY", "Unblock", "Every recommendation tracked in public — from approval to build, from claim to payout."),
]
bx = M_L; by = Inches(2.55); bw = Inches(2.55); bh = Inches(3.3); agap = Inches(0.42)
for i,(icn, t1, t15, t2) in enumerate(steps):
    rect(s, bx, by, bw, bh, WHITE, line=BORDER, rounded=True)
    circle(s, bx+Inches(0.28), by+Inches(0.32), Inches(0.62), BRAND_LITE)
    icon(s, icn, bx+Inches(0.42), by+Inches(0.46), Inches(0.34), BLUE_HEX)
    text(s, bx+Inches(0.28), by+Inches(1.15), bw-Inches(0.56), Inches(0.3), t1, font=HEAD, size=12.5, bold=True, color=BRAND, tracking=1.2)
    text(s, bx+Inches(0.28), by+Inches(1.5), bw-Inches(0.56), Inches(0.4), t15, font=HEAD, size=17, bold=True, color=DARK)
    text(s, bx+Inches(0.28), by+Inches(1.98), bw-Inches(0.56), Inches(1.2), t2, font=BODY, size=10, color=MUTED, ls=1.32)
    if i < 2:
        icon(s, "arrow-right", bx+bw+Inches(0.07), by+bh/2-Inches(0.14), Inches(0.28), LAVDK_HEX)
    bx += bw + agap
# right: refusals block
RX = Inches(9.35); RW = Inches(3.28)
rect(s, RX, Inches(2.55), RW, Inches(3.3), BRAND, rounded=True)
text(s, RX+Inches(0.3), Inches(2.82), RW-Inches(0.6), Inches(0.3), "WHAT WE DELIBERATELY AVOID",
     font=HEAD, size=9.5, bold=True, color=LAV, tracking=1.8)
refusals = ["Awareness-only campaigns", "Event counts as impact", "Replacing government's role", "Reports without follow-up"]
ry = Inches(3.25)
for rtxt in refusals:
    circle(s, RX+Inches(0.3), ry+Inches(0.02), Inches(0.26), RGBColor(0x5A,0x46,0xFF))
    icon(s, "x", RX+Inches(0.345), ry+Inches(0.065), Inches(0.17), WHITE_HEX)
    text(s, RX+Inches(0.68), ry, RW-Inches(0.95), Inches(0.3), rtxt, font=BODY, size=11, color=WHITE)
    ry += Inches(0.46)
hline(s, RX+Inches(0.3), Inches(5.18), RW-Inches(0.6), color=LAV_DK)
text(s, RX+Inches(0.3), Inches(5.32), RW-Inches(0.6), Inches(0.5),
     "Every recommendation tracked to implementation.", font=BODY, size=10.5, color=LAV, italic=True, ls=1.3)
text(s, M_L, Inches(6.25), Inches(11.9), Inches(0.4),
     "Institutionally embedded: 4 District Road Safety Committees · MoUs with Jaipur Traffic Police & Gurugram Police · formally tasked by SW Delhi DRSC.",
     font=BODY, size=10.5, color=MUTED, ls=1.3)
footer(s, 6, TOTAL, "OPERATING MODEL")

# ============================================================ S7 RAKSHAK
s = new_slide(WHITE)
ny = std_header(s, "WHAT WE DO · 01 ROAD INFRASTRUCTURE",
                "Project Rakshak — engineering students",
                "audit dangerous roads; governments fix them.",
                "A national programme that mobilises trained student teams to audit high-risk locations to official standards and hand authorities ready-to-build fixes.")
# funnel
funnel = [("120+", "high-risk locations\nscreened nationwide"),
          ("31", "sites fully audited,\nincl. 11 official blackspots"),
          ("25+", "written government\napprovals secured"),
          ("15", "implementations\nbegun on the ground")]
fx = M_L; fy = Inches(2.95); fw = Inches(1.92); fh = Inches(1.6)
for i,(num,lab) in enumerate(funnel):
    fill = BRAND if i==3 else BRAND_LITE
    tcol = WHITE if i==3 else BRAND
    lcol = LAV if i==3 else MUTED
    rect(s, fx, fy, fw, fh, fill, rounded=True)
    text(s, fx, fy+Inches(0.14), fw, Inches(0.65), num, font=HEAD, size=28, bold=True, color=tcol, align=PP_ALIGN.CENTER)
    text(s, fx, fy+Inches(0.8), fw, Inches(0.7), lab, font=BODY, size=8.8, color=lcol, align=PP_ALIGN.CENTER, ls=1.2)
    if i < 3:
        icon(s, "chevron-right", fx+fw+Inches(0.015), fy+fh/2-Inches(0.12), Inches(0.24), LAVDK_HEX)
    fx += fw + Inches(0.27)
# chips under funnel
chips_row = ["18 cities", "20 institutions · 9 IITs", "900+ stakeholder surveys"]
cxx = M_L; cyy = Inches(4.75)
widths = [Inches(1.5), Inches(2.6), Inches(2.5)]
for wd, ct in zip(widths, chips_row):
    chip(s, cxx, cyy, wd, Inches(0.42), ct, fill=WHITE, tcolor=DARK, size=9.5, line=BORDER)
    cxx += wd + Inches(0.18)
# case card
rect(s, M_L, Inches(5.4), Inches(8.5), Inches(1.3), BRAND_LITE, rounded=True)
icon(s, "hard-hat", M_L+Inches(0.3), Inches(5.62), Inches(0.34), BLUE_HEX)
text(s, M_L+Inches(0.82), Inches(5.56), Inches(7.4), Inches(0.3), "Example: Tejaji Nagar Junction, Indore",
     font=HEAD, size=12, bold=True, color=DARK)
text(s, M_L+Inches(0.82), Inches(5.9), Inches(7.5), Inches(0.75),
     "Student-audited redesign to IRC / MoRTH standards — signals, lighting, footpaths, speed management — approved by CPWD and the Additional Collector's office. Guided by Prof. Geetam Tiwari (TRIPC, IIT Delhi).",
     font=BODY, size=10, color=MUTED, ls=1.3)
# right map
try:
    pic = s.shapes.add_picture(os.path.join(BUILD_DIR, "india_map.png"), Inches(9.55), Inches(2.55), height=Inches(3.7))
except Exception as e:
    print("map missing", e)
text(s, Inches(9.35), Inches(6.4), Inches(3.5), Inches(0.25), "Every audit public: crashfreeindia.org/rakshak/dashboard",
     font=BODY, size=8.5, color=MUTED, italic=True, align=PP_ALIGN.CENTER)
footer(s, 7, TOTAL, "WHAT WE DO · PROJECT RAKSHAK")

# ============================================================ S8 SATARK
s = new_slide(WHITE)
ny = std_header(s, "WHAT WE DO · 02 ENFORCEMENT TECHNOLOGY",
                "SATARK — an AI platform that helps traffic",
                "police identify and stop high-risk vehicles.",
                "Cameras read every passing number plate and check it against live national records, so officers act on evidence instead of stopping vehicles at random.")
# pipeline
pipe = [("camera", "ANPR camera\nreads every plate"),
        ("database", "Live vehicle record\nvia national APIs"),
        ("list-filter", "Rule engine flags\nhabitual offenders"),
        ("tv", "Public billboard\nnames the risk"),
        ("shield-check", "Officer app routes\nthe interception")]
px = M_L; py = Inches(3.15); pw = Inches(2.12); ph = Inches(1.45)
for i,(icn,lab) in enumerate(pipe):
    rect(s, px, py, pw, ph, WHITE, line=BORDER, rounded=True)
    circle(s, px+pw/2-Inches(0.26), py+Inches(0.16), Inches(0.52), BRAND_LITE)
    icon(s, icn, px+pw/2-Inches(0.15), py+Inches(0.27), Inches(0.3), BLUE_HEX)
    text(s, px, py+Inches(0.78), pw, Inches(0.6), lab, font=BODY, size=9, color=DARK, align=PP_ALIGN.CENTER, ls=1.2)
    if i < 4:
        icon(s, "chevron-right", px+pw-Inches(0.02), py+ph/2-Inches(0.11), Inches(0.22), LAVDK_HEX)
    px += pw + Inches(0.24)
# stat row
stats = [("3,00,000+", "vehicles scanned"), ("₹30 Cr+", "pending challans surfaced"),
         ("350+", "high-risk vehicles intercepted"), ("2 cities live", "Jaipur & Bengaluru · 5 police approvals")]
sx = M_L; sy = Inches(4.95); sw = Inches(2.85)
for num, lab in stats:
    text(s, sx, sy, sw, Inches(0.5), num, font=HEAD, size=25, bold=True, color=BRAND)
    text(s, sx, sy+Inches(0.5), sw, Inches(0.35), lab, font=BODY, size=10, color=MUTED, ls=1.2)
    sx += sw + Inches(0.17)
rect(s, M_L, Inches(6.0), CONTENT_W, Inches(0.6), BRAND_LITE, rounded=True)
text(s, M_L+Inches(0.3), Inches(6.0), CONTENT_W-Inches(0.6), Inches(0.6),
     "First 72 hours in Jaipur: 1,240 vehicles flagged, 58 intercepted.  ·  100 AI challan billboards already live in Gurugram; 12+ cities in discussion.",
     font=HEAD, size=11.5, bold=True, color=BRAND, anchor=MSO_ANCHOR.MIDDLE, ls=1.25)
footer(s, 8, TOTAL, "WHAT WE DO · SATARK")

# ============================================================ S9 JUSTICE / AASHA
s = new_slide(BRAND_LITE)
ny = std_header(s, "WHAT WE DO · 03 VICTIM SUPPORT & COMPENSATION",
                "Helping crash victims and families claim",
                "the compensation the law promises them.")
# left: the gap (white card)
LX = M_L; LW = Inches(5.7); LY = Inches(2.6); LH = Inches(3.55)
rect(s, LX, LY, LW, LH, WHITE, line=BORDER, rounded=True)
text(s, LX+Inches(0.3), LY+Inches(0.22), LW-Inches(0.6), Inches(0.3), "THE GAP WE DOCUMENTED",
     font=HEAD, size=9.5, bold=True, color=MUTED, tracking=1.8)
gap_rows = [
    ("10.46 lakh", "compensation cases pending nationwide — ₹80,000 Cr stuck"),
    ("205 vs ~25,000", "hit-and-run claims actually filed vs. eligible crashes (FY22-23)"),
    ("3.6 years", "average wait for a claim — with 20–40 office visits"),
    ("2 of 102", "hit-and-run files settled since 2022 in our Gurugram audit"),
]
gy = LY + Inches(0.62)
for num, lab in gap_rows:
    text(s, LX+Inches(0.3), gy, Inches(1.95), Inches(0.4), num, font=HEAD, size=15.5, bold=True, color=DARK)
    text(s, LX+Inches(2.3), gy+Inches(0.02), LW-Inches(2.6), Inches(0.6), lab, font=BODY, size=9.8, color=MUTED, ls=1.25)
    gy += Inches(0.72)
# right: the machinery (brand card)
RX = Inches(6.65); RW = Inches(5.98)
rect(s, RX, LY, RW, LH, BRAND, rounded=True)
text(s, RX+Inches(0.3), LY+Inches(0.22), RW-Inches(0.6), Inches(0.3), "THE MACHINERY WE BUILT",
     font=HEAD, size=9.5, bold=True, color=LAV, tracking=1.8)
fix_rows = [
    ("bot", "Aasha — India's first 24/7 multilingual AI chatbot guiding victims step-by-step, on WhatsApp and voice"),
    ("calculator", "Free Compensation Calculator based on Supreme Court principles (Sarla Verma, Pranay Sethi)"),
    ("hand-helping", "Legal helpdesks inside hospital trauma wards — 100+ victims supported in the first 4 days"),
    ("book-open", "Plain-language comic books and Hindi guides explaining rights, schemes and the claim process"),
    ("landmark", "‘Justice Unserved’ research presented to MoRTH; claim pipeline being rebuilt with Rajasthan Transport Dept."),
]
fy2 = LY + Inches(0.62)
for icn, lab in fix_rows:
    circle(s, RX+Inches(0.3), fy2, Inches(0.34), RGBColor(0x5A,0x46,0xFF))
    icon(s, icn, RX+Inches(0.365), fy2+Inches(0.065), Inches(0.21), WHITE_HEX)
    text(s, RX+Inches(0.78), fy2-Inches(0.01), RW-Inches(1.05), Inches(0.55), lab, font=BODY, size=9.8, color=WHITE, ls=1.22)
    fy2 += Inches(0.57)
text(s, M_L, Inches(6.35), Inches(11.9), Inches(0.35),
     "‘Justice Unserved’ (launched at IIT Delhi, 2026) is now the reference dataset on why crash compensation fails in India.",
     font=BODY, size=10.5, color=MUTED, italic=True)
footer(s, 9, TOTAL, "WHAT WE DO · VICTIM SUPPORT")

# ============================================================ S10 DATA COMMONS
s = new_slide(WHITE)
ny = std_header(s, "WHAT WE DO · 04 OPEN DATA PLATFORMS",
                "Public data tools we built so that",
                "road-safety problems cannot be ignored.",
                "Four self-updating platforms — free for government, researchers, journalists and citizens.")
prods = [
    ("map-pinned", "National Road Defect Repository", "AI reads local news in 13 languages across 146 districts — potholes, missing signage, unlit stretches — mapped publicly so authorities can act."),
    ("landmark", "Road Safety in Parliament", "Every parliamentary road-safety question since 2014 — 1,423 of them — searchable by MP and state. 282 sitting Lok Sabha MPs have never asked one."),
    ("scale", "Supreme Court Litigation Tracker", "18 live road-safety cases and 190+ orders, with each government deadline tracked — 11 were already overdue at launch."),
    ("bar-chart-3", "National Crash Data Dashboard", "Government crash statistics (2019–2024) turned into report cards for 36 states and 50 cities — free and openly licensed."),
]
cw = Inches(5.85); ch = Inches(1.55); gap = Inches(0.22)
for i,(icn,t1,t2) in enumerate(prods):
    x = M_L + (i%2)*(cw+gap); y = Inches(2.95) + (i//2)*(ch+Inches(0.2))
    rect(s, x, y, cw, ch, WHITE, line=BORDER, rounded=True)
    circle(s, x+Inches(0.22), y+Inches(0.22), Inches(0.46), BRAND_LITE)
    icon(s, icn, x+Inches(0.315), y+Inches(0.315), Inches(0.27), BLUE_HEX)
    text(s, x+Inches(0.84), y+Inches(0.24), cw-Inches(1.05), Inches(0.3), t1, font=HEAD, size=12.5, bold=True, color=DARK)
    text(s, x+Inches(0.84), y+Inches(0.6), cw-Inches(1.05), Inches(0.85), t2, font=BODY, size=9.3, color=MUTED, ls=1.26)
text(s, M_L, Inches(5.98), Inches(11.9), Inches(0.3), "‘JUSTICE UNSERVED’, IN PRINT",
     font=HEAD, size=9, bold=True, color=MUTED, tracking=1.6)
outlets = ["Deccan Herald", "Economic Times", "Fortune India", "IndiaSpend", "Moneycontrol", "Scroll.in", "The Wire"]
ox = M_L
for o in outlets:
    wd = Inches(0.24 + 0.093*len(o))
    chip(s, ox, Inches(6.3), wd, Inches(0.38), o, fill=BRAND_LITE, tcolor=BRAND, size=8.8)
    ox += wd + Inches(0.14)
footer(s, 10, TOTAL, "WHAT WE DO · OPEN DATA")

# ============================================================ S11 SCOREBOARD
s = new_slide(BRAND_LITE)
ny = std_header(s, "IMPACT · OUR FIRST YEAR",
                "Year one: measurable results",
                "across 18 Indian cities.")
tiles = [("1M+", "citizens reached"), ("18", "cities active"), ("25+", "govt approvals won"),
         ("15", "implementations begun"), ("4", "district committees joined"), ("2", "cities enforcing with SATARK"),
         ("150+", "members & interns"), ("50+", "experts engaged"), ("10+", "national media features")]
cw = Inches(2.55); ch = Inches(1.06); gapx = Inches(0.18); gapy = Inches(0.16)
for i,(num,lab) in enumerate(tiles):
    x = M_L + (i%3)*(cw+gapx); y = Inches(2.5) + (i//3)*(ch+gapy)
    rect(s, x, y, cw, ch, WHITE, line=BORDER, rounded=True)
    text(s, x+Inches(0.22), y+Inches(0.12), cw-Inches(0.4), Inches(0.5), num, font=HEAD, size=23, bold=True, color=BRAND)
    text(s, x+Inches(0.22), y+Inches(0.62), cw-Inches(0.4), Inches(0.35), lab, font=BODY, size=9.3, color=MUTED)
# timeline right column
TX = Inches(9.15); TW = Inches(3.48)
rect(s, TX, Inches(2.5), TW, Inches(3.95), BRAND, rounded=True)
text(s, TX+Inches(0.28), Inches(2.72), TW-Inches(0.56), Inches(0.3), "THE FIRST 400 DAYS",
     font=HEAD, size=9.5, bold=True, color=LAV, tracking=1.8)
tl = [("Jun 25", "Launched as a Cars24 commitment"),
      ("Sep 25", "NextMile finale · first AI billboard live in Bengaluru"),
      ("Jan 26", "‘Justice Unserved’ published"),
      ("Apr 26", "IIT Delhi national forum · Dhoni joins"),
      ("Jun 26", "SATARK live with Jaipur Police"),
      ("Jul 26", "Rakshak Cohort 2 · 4 open-data products shipped")]
tly = Inches(3.14)
for d, ev in tl:
    text(s, TX+Inches(0.28), tly, Inches(0.72), Inches(0.3), d, font=HEAD, size=9, bold=True, color=LAV)
    text(s, TX+Inches(1.05), tly, TW-Inches(1.32), Inches(0.5), ev, font=BODY, size=9, color=WHITE, ls=1.18)
    tly += Inches(0.55)
text(s, M_L, Inches(6.3), Inches(8.2), Inches(0.35),
     "Every figure above is from our public dashboard and quarterly updates — audited numbers, not estimates.",
     font=BODY, size=10, color=MUTED, italic=True)
footer(s, 11, TOTAL, "IMPACT · OUR FIRST YEAR")

# ============================================================ S12 DHONI (peak)
s = new_slide(BRAND)
logo(s, M_L, Inches(0.5), Inches(2.1), dark=True)
sparkles_tr(s, LAV_DK)
text(s, M_L, Inches(1.5), Inches(6.4), Inches(0.35), "OUR AMBASSADOR", font=HEAD, size=10,
     bold=True, color=LAV, tracking=2.4)
text(s, M_L, Inches(1.92), Inches(6.6), Inches(0.7), "MS Dhoni is Crashfree India's", font=HEAD, size=27, bold=True, color=WHITE)
text(s, M_L, Inches(2.45), Inches(6.6), Inches(0.7), "Goodwill Ambassador.", font=HEAD, size=27, bold=True, color=LAV)
text(s, M_L, Inches(3.25), Inches(6.1), Inches(1.0),
     "One of India's most trusted public figures joined us in April 2026, unveiled at our national forum at IIT Delhi. His role — lending his voice where it moves people to act:",
     font=BODY, size=12, color=WHITE, ls=1.4)
roles = ["Inviting India's students to join Project Rakshak road audits",
         "Championing safer school zones",
         "Spreading awareness of victims' compensation rights and Aasha"]
ry = Inches(4.35)
for rl in roles:
    icon(s, "check", M_L+Inches(0.02), ry+Inches(0.03), Inches(0.2), "#C8C0FF")
    text(s, M_L+Inches(0.35), ry, Inches(5.9), Inches(0.3), rl, font=BODY, size=10.5, color=LAV, ls=1.2)
    ry += Inches(0.42)
text(s, M_L, Inches(5.95), Inches(6.2), Inches(0.5),
     "“Because every ride deserves to end safely.”", font=HEAD, size=13, bold=True, color=WHITE, italic=True)
text(s, M_L, Inches(6.45), Inches(6.2), Inches(0.3),
     "Announcement covered by Business Standard · The Tribune · The Wire", font=BODY, size=9.5, color=LAV)
# right: real shoot photo (helmet) + announcement creative
try:
    from PIL import Image as _Img2
    _h = _Img2.open(os.path.join(BUILD_DIR, "dhoni_cutout_white.png"))
    _har = _h.width/_h.height
    HH = Inches(5.1); HW = Inches(5.1*_har)
    s.shapes.add_picture(os.path.join(BUILD_DIR, "dhoni_cutout_white.png"),
                         Inches(12.63)-HW, Inches(1.35), width=HW, height=HH)
    text(s, Inches(8.9), Inches(6.5), Inches(3.9), Inches(0.25), "CFI shoot · June 2026",
         font=BODY, size=8.5, color=LAV, italic=True, align=PP_ALIGN.CENTER)
except Exception as e:
    print("dhoni image missing", e)
footer_dark(s, 12, "OUR AMBASSADOR")

# ============================================================ S13 GOVERNANCE
s = new_slide(WHITE)
ny = std_header(s, "OUR PEOPLE · BOARD OF ADVISORS",
                "Guided by two of India's foremost",
                "road-safety experts.")
boa = [
    ("Piyush Tewari", "Founder & CEO, SaveLIFE Foundation",
     ["Architect of India's Good Samaritan Law (Supreme Court, 2016)",
      "Built the Zero Fatality Corridor model — ~40% fewer deaths on Mumbai–Pune Expressway; now scaling with MoRTH",
      "Rolex Award for Enterprise · Elevate Prize · MPA, Harvard"]),
    ("Prof. (Dr.) Geetam Tiwari", "Professor Emerita, TRIPC, IIT Delhi",
     ["Three decades leading India's foremost road-safety research centre — a WHO Collaborating Centre",
      "Global authority on vulnerable road users & safe-system design · PhD, University of Illinois Chicago",
      "Guides Project Rakshak's audit methodology; anchors our Expert Consortium"]),
]
cw = Inches(5.85); ch = Inches(2.32); gap = Inches(0.22)
for i,(nm, ti, pts) in enumerate(boa):
    x = M_L + i*(cw+gap); y = Inches(2.45)
    rect(s, x, y, cw, ch, WHITE, line=BORDER, rounded=True)
    circle(s, x+Inches(0.28), y+Inches(0.28), Inches(0.8), BRAND)
    initials = "".join(w[0] for w in nm.replace("Prof. (Dr.) ","").split()[:2])
    text(s, x+Inches(0.28), y+Inches(0.28), Inches(0.8), Inches(0.8), initials, font=HEAD, size=19, bold=True,
         color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(s, x+Inches(1.25), y+Inches(0.26), cw-Inches(1.5), Inches(0.35), nm, font=HEAD, size=15, bold=True, color=DARK)
    text(s, x+Inches(1.25), y+Inches(0.64), cw-Inches(1.5), Inches(0.3), ti, font=HEAD, size=10.5, bold=True, color=BRAND)
    py2 = y + Inches(1.04)
    for p in pts:
        circle(s, x+Inches(1.27), py2+Inches(0.07), Inches(0.08), BRAND)
        text(s, x+Inches(1.5), py2, cw-Inches(1.8), Inches(0.5), p, font=BODY, size=8.8, color=MUTED, ls=1.2)
        py2 += Inches(0.42)
text(s, M_L, Inches(4.98), Inches(6), Inches(0.3), "THE EXPERT BENCH BEHIND OUR AUDITS",
     font=HEAD, size=9.5, bold=True, color=MUTED, tracking=1.8)
bench = [("Justice J. R. Midha (Retd.)", "Delhi High Court · FastDAR architect"),
         ("Dr. S. Velmurugan", "Head, Traffic Engg. & Safety, CSIR-CRRI"),
         ("Dr. Richa Ahuja", "IIT Kharagpur · Rakshak advisor"),
         ("Akhilesh Srivastava", "IRF India"),
         ("Col. Sanjeev Sharma", "CoERS, IIT Madras"),
         ("Sarika Panda Bhatt", "Raahgiri Foundation"),
         ("B. N. Puri", "Transport economist"),
         ("Dr. P. K. Sikdar", "Ex-Director, CRRI"),
         ("A. M. Rao", "Traffic engineering")]
cw2 = Inches(3.85); ch2 = Inches(0.48)
for i,(nm,ti) in enumerate(bench):
    x = M_L + (i%3)*(cw2+Inches(0.19)); y = Inches(5.28) + (i//3)*(ch2+Inches(0.08))
    rect(s, x, y, cw2, ch2, BRAND_LITE, rounded=True)
    text(s, x+Inches(0.18), y+Inches(0.045), cw2-Inches(0.3), Inches(0.24), nm, font=HEAD, size=9.3, bold=True, color=DARK)
    text(s, x+Inches(0.18), y+Inches(0.265), cw2-Inches(0.3), Inches(0.2), ti, font=BODY, size=7.8, color=MUTED)
footer(s, 13, TOTAL, "BOARD OF ADVISORS & EXPERTS")

# ============================================================ S14 TEAM
s = new_slide(WHITE)
ny = std_header(s, "OUR PEOPLE · THE TEAM",
                "A full-time team of eight, three trustees,",
                "and 75+ engineering interns nationwide.")
trustees = [
    ("Amar Srivastava", "President", "Founder, Indian Road Safety Council — 50,000+ volunteers · Diana Award 2019"),
    ("Deepanshu Gupta", "Managing Trustee", "Founder, IRSC · Global Youth Coalition for Road Safety leadership board"),
    ("Gajendra Jangid", "General Secretary", "Co-founder, Cars24 · ex-Schlumberger"),
]
cw = Inches(3.85); ch = Inches(1.28); gap = Inches(0.19)
text(s, M_L, Inches(2.42), Inches(4), Inches(0.28), "TRUSTEES · VISION ZERO TRUST",
     font=HEAD, size=9, bold=True, color=MUTED, tracking=1.6)
for i,(nm,ro,cred) in enumerate(trustees):
    x = M_L + i*(cw+gap); y = Inches(2.75)
    rect(s, x, y, cw, ch, BRAND_LITE, rounded=True)
    circle(s, x+Inches(0.2), y+Inches(0.2), Inches(0.6), BRAND)
    text(s, x+Inches(0.2), y+Inches(0.2), Inches(0.6), Inches(0.6), "".join(w[0] for w in nm.split()[:2]),
         font=HEAD, size=15, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(s, x+Inches(0.95), y+Inches(0.17), cw-Inches(1.15), Inches(0.28), nm, font=HEAD, size=12, bold=True, color=DARK)
    text(s, x+Inches(0.95), y+Inches(0.47), cw-Inches(1.15), Inches(0.25), ro, font=HEAD, size=9.5, bold=True, color=BRAND)
    text(s, x+Inches(0.2), y+Inches(0.82), cw-Inches(0.4), Inches(0.42), cred, font=BODY, size=8.3, color=MUTED, ls=1.2)
team = [
    ("Akhtar Hussain", "Mission Lead", "IIT Delhi · ex-Bain & Co., Deloitte"),
    ("Shubham Kumar", "Policy Advocacy", "DU + NALSAR · byline: Scroll.in"),
    ("Muskan Yadav", "Programs · Infrastructure", "TISS Mumbai"),
    ("Aastha Shreeharsh", "Strategy & Operations", "HKUST · quoted in The Wire"),
    ("Rohan Sharma", "Cause Marketing", ""),
    ("Ishita Rathore", "People & Culture", ""),
    ("Yuvraj Yadav", "Product Design", ""),
    ("Shipra Kushwaha", "Graphic Design", ""),
]
text(s, M_L, Inches(4.28), Inches(4), Inches(0.28), "FULL-TIME TEAM",
     font=HEAD, size=9, bold=True, color=MUTED, tracking=1.6)
cw2 = Inches(2.88); ch2 = Inches(0.92)
for i,(nm,ro,cred) in enumerate(team):
    x = M_L + (i%4)*(cw2+Inches(0.14)); y = Inches(4.6) + (i//4)*(ch2+Inches(0.14))
    rect(s, x, y, cw2, ch2, WHITE, line=BORDER, rounded=True)
    circle(s, x+Inches(0.14), y+Inches(0.14), Inches(0.44), BRAND_LITE)
    text(s, x+Inches(0.14), y+Inches(0.14), Inches(0.44), Inches(0.44), "".join(w[0] for w in nm.split()[:2]),
         font=HEAD, size=11, bold=True, color=BRAND, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(s, x+Inches(0.68), y+Inches(0.1), cw2-Inches(0.8), Inches(0.26), nm, font=HEAD, size=10, bold=True, color=DARK)
    text(s, x+Inches(0.68), y+Inches(0.36), cw2-Inches(0.8), Inches(0.24), ro, font=BODY, size=8.3, color=BRAND)
    text(s, x+Inches(0.68), y+Inches(0.58), cw2-Inches(0.8), Inches(0.28), cred, font=BODY, size=7.6, color=MUTED)
text(s, M_L, Inches(6.68), CONTENT_W, Inches(0.3),
     "+ 75+ part-time road-engineering interns across India",
     font=BODY, size=9.5, color=MUTED, italic=True)
footer(s, 14, TOTAL, "THE TEAM")

# ============================================================ S15 CLOSE
s = new_slide(BRAND)
logo(s, M_L, Inches(0.55), Inches(2.1), dark=True)
sparkles_tr(s, LAV_DK)
text(s, M_L, Inches(1.85), Inches(11.9), Inches(0.4), "THE YEAR AHEAD", font=HEAD, size=10, bold=True,
     color=LAV, tracking=2.4)
text(s, M_L, Inches(2.25), Inches(11.9), Inches(1.6),
     "Year two: fewer bets, deeper districts,\nand more fixes built on the ground.", font=HEAD, size=30, bold=True,
     color=WHITE, ls=1.15)
text(s, M_L, Inches(3.6), Inches(11.9), Inches(0.8),
     "Every three minutes, a life is lost on an Indian road. Join us in changing that.",
     font=HEAD, size=15, bold=True, color=LAV)
hline(s, M_L, Inches(4.6), Inches(11.9), color=LAV_DK)
text(s, M_L, Inches(4.82), Inches(5.5), Inches(0.3), "YEAR TWO, WITH YOU — THE TARGETS",
     font=HEAD, size=9.5, bold=True, color=LAV, tracking=1.8)
targets = ["150+ blackspots audited by the national pipeline",
           "Model districts: Gurugram · SW Delhi · Jaipur",
           "12+ district-committee presentations",
           "Rakshak Audit Manual v1.0 — usable by NHAI without rework"]
ty = Inches(5.2)
for t in targets:
    circle(s, M_L+Inches(0.02), ty+Inches(0.05), Inches(0.14), LAV)
    text(s, M_L+Inches(0.35), ty, Inches(5.6), Inches(0.3), t, font=BODY, size=10.5, color=WHITE, ls=1.2)
    ty += Inches(0.4)
text(s, Inches(7.2), Inches(4.82), Inches(5.4), Inches(0.3), "START THE CONVERSATION",
     font=HEAD, size=9.5, bold=True, color=LAV, tracking=1.8)
contact = [("globe", "crashfreeindia.org"), ("mail", "helpdesk@crashfreeindia.org"),
           ("bar-chart-3", "Live proof: crashfreeindia.org/rakshak/dashboard")]
cy2 = Inches(5.2)
for icn, t in contact:
    icon(s, icn, Inches(7.2), cy2+Inches(0.01), Inches(0.24), "#C8C0FF")
    text(s, Inches(7.58), cy2, Inches(5.0), Inches(0.3), t, font=BODY, size=10.5, color=WHITE)
    cy2 += Inches(0.42)
text(s, M_L, Inches(6.85), Inches(11.9), Inches(0.3),
     "Crashfree India · A Cars24 Commitment · operated by Vision Zero Trust", font=HEAD, size=8.5,
     color=LAV, tracking=1.6, bold=True)

OUT = os.path.join(BUILD_DIR, "CFI_Overview.pptx")
save(OUT)

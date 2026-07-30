# Crashfree India — Partner Overview Deck v3 (17 main + 8 appendix)
# CFI design skill §14: python-pptx, Montserrat/Geist, 16:9, safe zones.
import os
from cfi_helpers import *

A  = os.path.join(os.path.dirname(BUILD_DIR), "assets")
V3 = os.path.join(A, "v3")
TOTAL = 25
BLUE_HEX = "#4A35FF"; WHITE_HEX = "#FFFFFF"; MUTED_HEX = "#777589"
DANGER_HEX = "#F10015"; LAVDK_HEX = "#6A55FF"
BRAND_MID = RGBColor(0x5A,0x46,0xFF)

def footer_dark(slide, idx, label):
    text(slide, M_L, Inches(7.12), Inches(8), Inches(0.3), label, font=HEAD, size=8.5,
         color=LAV, tracking=1.6, bold=True)
    text(slide, Inches(11.4), Inches(7.12), Inches(1.4), Inches(0.3), f"{idx:02d} / {TOTAL:02d}",
         font=HEAD, size=8.5, color=LAV, tracking=1.6, bold=True, align=PP_ALIGN.RIGHT)

def chip(slide, x, y, w, h, label, fill=BRAND_LITE, tcolor=BRAND, size=9.5, bold=True, line=None):
    rect(slide, x, y, w, h, fill, line=line, rounded=True)
    text(slide, x+Inches(0.12), y, w-Inches(0.24), h, label, font=HEAD, size=size, bold=bold,
         color=tcolor, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, ls=1.0)

def pic(slide, path, x, y, w=None, h=None):
    return slide.shapes.add_picture(path, x, y, width=w, height=h)

def pic_ar(path):
    from PIL import Image as _I
    im = _I.open(path); return im.width/im.height

# ============================================================ 01 COVER
s = new_slide(WHITE)
logo(s, M_L, Inches(0.55), Inches(2.7))
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
try:
    db = os.path.join(V3, "new", "dashboard.png")
    ar_db = pic_ar(db); dbw = Inches(2.72)
    rect(s, BAND_X+Inches(0.4), Inches(4.66), dbw+Inches(0.08), Inches(2.72/ar_db)+Inches(0.08), WHITE)
    pic(s, db, BAND_X+Inches(0.44), Inches(4.7), w=dbw)
    text(s, BAND_X+Inches(0.44), Inches(4.7)+Inches(2.72/ar_db)+Inches(0.1), dbw, Inches(0.3),
         "Live: crashfreeindia.org/rakshak/dashboard", font=HEAD, size=7.5, bold=True, color=LAV, tracking=0.8)
    text(s, BAND_X+Inches(0.44), Inches(6.85), dbw, Inches(0.3),
         "Goodwill Ambassador: MS Dhoni", font=HEAD, size=8, bold=True, color=LAV, tracking=1.0)
except Exception as e: print("cover dash", e)
eyebrow(s, M_L, Inches(2.55), "CRASHFREE INDIA  ·  A CARS24 COMMITMENT")
text(s, M_L, Inches(2.92), Inches(8.8), Inches(0.75),
     "Building safer roads for India —", font=HEAD, size=34, bold=True, color=DARK, ls=1.04)
text(s, M_L, Inches(3.54), Inches(8.8), Inches(0.75),
     "audit by audit, fix by fix.", font=HEAD, size=34, bold=True, color=BRAND, ls=1.04)
text(s, M_L, Inches(4.35), Inches(8.6), Inches(0.6),
     "A nonprofit working alongside government — finding road-safety gaps, getting fixes approved, and staying until they are built.",
     font=BODY, size=13, color=MUTED, ls=1.4)
pill_labels = ["ROAD INFRASTRUCTURE", "ENFORCEMENT TECHNOLOGY", "POLICY & VICTIM SUPPORT", "YOUTH MOBILISATION"]
pill_w = [Inches(1.95), Inches(2.2), Inches(2.25), Inches(2.0)]
px_ = M_L
for wd, lab in zip(pill_w, pill_labels):
    chip(s, px_, Inches(5.15), wd, Inches(0.4), lab, fill=BRAND_LITE, tcolor=BRAND, size=8.3)
    px_ += wd + Inches(0.12)
hline(s, M_L, Inches(6.05), Inches(8.6), color=BORDER, wt=1.0)
text(s, M_L, Inches(6.25), Inches(8.8), Inches(0.35),
     [("Year one:  ", {'font':HEAD,'size':10.5,'bold':True,'color':MUTED}),
      ("1M+ people reached  ·  18 cities  ·  25+ government approvals  ·  ₹30 Cr+ unpaid challans surfaced",
       {'font':HEAD,'size':10.5,'bold':True,'color':DARK})])
text(s, M_L, Inches(6.75), Inches(8.6), Inches(0.35),
     "Partner overview  ·  July 2026  ·  crashfreeindia.org", font=HEAD, size=9.5,
     color=MUTED, tracking=1.6, bold=True)

# ============================================================ 02 PROBLEM (scale + system failure)
s = new_slide(WHITE)
ny = std_header(s, "THE PROBLEM",
                "India loses 485 lives on its roads every day —",
                "most of them preventable with follow-through.")
text(s, M_L, Inches(2.5), Inches(5.4), Inches(2.1), "485", font=HEAD, size=150, bold=True,
     color=DANGER, align=PP_ALIGN.CENTER, ls=0.9)
text(s, M_L, Inches(4.75), Inches(5.4), Inches(0.4), "people killed every single day",
     font=HEAD, size=14, bold=True, color=DARK, align=PP_ALIGN.CENTER)
chip(s, M_L+Inches(1.35), Inches(5.25), Inches(2.7), Inches(0.42), "ONE DEATH EVERY 3 MINUTES",
     fill=BRAND_LITE, tcolor=BRAND, size=9.5)
text(s, M_L, Inches(5.85), Inches(5.4), Inches(0.3), "MoRTH, Road Accidents in India 2024: 1,77,175 deaths",
     font=BODY, size=9, color=MUTED, italic=True, align=PP_ALIGN.CENTER)
RX = Inches(6.9)
text(s, RX, Inches(2.35), Inches(5.7), Inches(1.0), "59%", font=HEAD, size=60, bold=True, color=BRAND)
text(s, RX, Inches(3.52), Inches(5.6), Inches(0.75),
     "of road deaths involve no traffic violation by the victim — better road design, supported enforcement and faster post-crash care decide who survives.",
     font=BODY, size=11.5, color=DARK, ls=1.35)
rows = [("66% of victims are aged 18–34", "India's workforce bears the loss"),
        ("1% of world's vehicles, 11% of its road deaths", "the gap is systemic"),
        ("₹80,000 Cr in compensation undelivered", "the failure continues after the crash")]
ry = Inches(4.68)
for t1, t2 in rows:
    circle(s, RX, ry+Inches(0.05), Inches(0.12), BRAND)
    text(s, RX+Inches(0.3), ry, Inches(5.4), Inches(0.3),
         [(t1+"  ", {'font':BODY,'size':10.5,'bold':True,'color':DARK}),
          ("— "+t2, {'font':BODY,'size':10,'color':MUTED})])
    ry += Inches(0.46)
rect(s, M_L, Inches(6.25), CONTENT_W, Inches(0.5), BRAND_LITE, rounded=True)
text(s, M_L+Inches(0.3), Inches(6.25), CONTENT_W-Inches(0.6), Inches(0.5),
     "India has strong laws and committed institutions. What they need is more capacity for follow-through — that is the gap we fill.",
     font=HEAD, size=11.5, bold=True, color=BRAND, anchor=MSO_ANCHOR.MIDDLE)
footer(s, 2, TOTAL, "THE PROBLEM")

# ============================================================ 03 THREE GAPS (brand)
s = new_slide(BRAND)
logo(s, M_L, Inches(0.5), Inches(2.1), dark=True)
sparkles_tr(s, LAV_DK)
text(s, M_L, Inches(1.35), Inches(11.9), Inches(0.4), "THE PROBLEM · WHERE WE HELP", font=HEAD, size=10, bold=True,
     color=LAV, tracking=2.4)
text(s, M_L, Inches(1.75), Inches(11.9), Inches(0.65), "Three pendencies we help the system clear.",
     font=HEAD, size=30, bold=True, color=WHITE)
text(s, M_L, Inches(2.42), Inches(11.5), Inches(0.4),
     "We studied how India responds to a road death. Departments know the problems — what they need is dedicated hands, tools and follow-through.",
     font=BODY, size=12, color=LAV, ls=1.35)
cards = [
    ("traffic-cone", "01 · ROAD FIXES PENDING", "Audits await execution.",
     "Hazards are identified and studies filed — stretched departments need help converting reports into built fixes."),
    ("scale", "02 · CLAIMS PENDING", "₹80,000 Cr awaits families.",
     "10.46 lakh compensation cases pending. Our Gurugram file audit shows where each claim gets stuck — and how to unblock it."),
    ("siren", "03 · RECORDS UNUSED", "Enforcement lacks live tools.",
     "46 crore e-challans on record, ~75% unpaid. Police need technology that turns records into targeted, fair action."),
]
cw = Inches(3.85); gap = Inches(0.19); cx = M_L; cy = Inches(3.1); ch = Inches(2.85)
for icn, kick, t1, t2 in cards:
    rect(s, cx, cy, cw, ch, BRAND_MID, rounded=True)
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
     "Our role: give the system the hands, tools and follow-through to convert intent into outcomes on the ground.",
     font=HEAD, size=12.5, bold=True, color=WHITE, ls=1.3)
footer_dark(s, 3, "THE PROBLEM · WHERE WE HELP")

# ============================================================ 04 ABOUT
s = new_slide(WHITE)
ny = std_header(s, "WHO WE ARE · ABOUT CRASHFREE INDIA",
                "A partner to the system — with the",
                "hands and tools to finish the job.",
                "A Cars24-backed nonprofit ($3M over 3 years, run by Vision Zero Trust) working with governments towards zero road deaths by 2040.")
# left: philosophy + impact
rect(s, M_L, Inches(2.85), Inches(6.1), Inches(2.15), BRAND, rounded=True)
text(s, M_L+Inches(0.3), Inches(3.05), Inches(5.5), Inches(0.3), "OUR PHILOSOPHY",
     font=HEAD, size=9, bold=True, color=LAV, tracking=1.8)
text(s, M_L+Inches(0.3), Inches(3.38), Inches(5.55), Inches(0.85),
     "Road deaths are a solvable systems problem. We work as a support layer to government — auditing on the ground, building tools, and staying with every fix until it is done.",
     font=BODY, size=11.5, color=WHITE, ls=1.4)
loop = ["AUDIT", "ADVOCATE", "FOLLOW THROUGH"]
lx = M_L+Inches(0.3)
for i, lstep in enumerate(loop):
    wd = Inches(0.4 + 0.085*len(lstep))
    rect(s, lx, Inches(4.35), wd, Inches(0.36), BRAND_MID, rounded=True)
    text(s, lx, Inches(4.35), wd, Inches(0.36), lstep, font=HEAD, size=8.5, bold=True, color=WHITE,
         align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, tracking=0.8)
    lx += wd + Inches(0.08)
    if i < 2:
        icon(s, "arrow-right", lx-Inches(0.02), Inches(4.42), Inches(0.2), "#C8C0FF")
        lx += Inches(0.24)
imp = [("1M+", "people reached"), ("18", "cities"), ("25+", "govt approvals"), ("₹30 Cr+", "dues surfaced")]
ix = M_L
for num, lab in imp:
    rect(s, ix, Inches(5.2), Inches(1.45), Inches(0.85), BRAND_LITE, rounded=True)
    text(s, ix, Inches(5.3), Inches(1.45), Inches(0.4), num, font=HEAD, size=15, bold=True, color=BRAND, align=PP_ALIGN.CENTER)
    text(s, ix, Inches(5.68), Inches(1.45), Inches(0.3), lab, font=BODY, size=7.8, color=MUTED, align=PP_ALIGN.CENTER)
    ix += Inches(1.56)
# right: four pillars
text(s, Inches(7.15), Inches(2.85), Inches(5.3), Inches(0.3), "FOUR PILLARS OF WORK",
     font=HEAD, size=9, bold=True, color=MUTED, tracking=1.8)
pillars4 = [("hard-hat", "Road infrastructure", "Project Rakshak — audits that end in built fixes"),
            ("scan-line", "Enforcement technology", "SATARK & AI billboards, run with police"),
            ("hand-helping", "Policy & victim support", "Aasha, compensation research, district committees"),
            ("bar-chart-3", "Open data & education", "Public dashboards, comics, guides")]
py5 = Inches(3.18)
for icn, t1, t2 in pillars4:
    circle(s, Inches(7.15), py5, Inches(0.4), BRAND_LITE)
    icon(s, icn, Inches(7.235), py5+Inches(0.085), Inches(0.23), BLUE_HEX)
    text(s, Inches(7.7), py5-Inches(0.02), Inches(4.9), Inches(0.26), t1, font=HEAD, size=11, bold=True, color=DARK)
    text(s, Inches(7.7), py5+Inches(0.25), Inches(4.9), Inches(0.26), t2, font=BODY, size=9, color=MUTED)
    py5 += Inches(0.72)
# bottom: governance strip
rect(s, M_L, Inches(6.25), CONTENT_W, Inches(0.62), WHITE, line=BORDER, rounded=True)
text(s, M_L+Inches(0.25), Inches(6.32), CONTENT_W-Inches(0.5), Inches(0.5),
     [("Trustees:  ", {'font':HEAD,'size':9,'bold':True,'color':BRAND}),
      ("Amar Srivastava (Founder, IRSC) · Deepanshu Gupta (Founder, IRSC) · Gajendra Jangid (Co-founder, Cars24)      ",
       {'font':BODY,'size':9,'color':DARK}),
      ("Board of Advisors:  ", {'font':HEAD,'size':9,'bold':True,'color':BRAND}),
      ("Piyush Tewari (SaveLIFE Foundation) · Prof. Geetam Tiwari (IIT Delhi)", {'font':BODY,'size':9,'color':DARK})],
     ls=1.35)
footer(s, 4, TOTAL, "ABOUT CRASHFREE INDIA")

# ============================================================ 05 APPROACH
s = new_slide(BRAND_LITE)
ny = std_header(s, "WHO WE ARE · OUR APPROACH",
                "How we work: audit, advocate, and",
                "follow through until the fix is built.")
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
RX = Inches(9.35); RW = Inches(3.28)
rect(s, RX, Inches(2.55), RW, Inches(3.3), BRAND, rounded=True)
text(s, RX+Inches(0.3), Inches(2.82), RW-Inches(0.6), Inches(0.3), "HOW WE STAY FOCUSED",
     font=HEAD, size=9.5, bold=True, color=LAV, tracking=1.8)
refusals = ["No campaigns without follow-up", "No event-counting as impact", "Never duplicating govt's role", "No reports that end at submission"]
ry = Inches(3.25)
for rtxt in refusals:
    circle(s, RX+Inches(0.3), ry+Inches(0.02), Inches(0.26), BRAND_MID)
    icon(s, "x", RX+Inches(0.345), ry+Inches(0.065), Inches(0.17), WHITE_HEX)
    text(s, RX+Inches(0.68), ry, RW-Inches(0.95), Inches(0.3), rtxt, font=BODY, size=11, color=WHITE)
    ry += Inches(0.46)
hline(s, RX+Inches(0.3), Inches(5.18), RW-Inches(0.6), color=LAV_DK)
text(s, RX+Inches(0.3), Inches(5.32), RW-Inches(0.6), Inches(0.5),
     "Every recommendation tracked to implementation.", font=BODY, size=10.5, color=LAV, italic=True, ls=1.3)
text(s, M_L, Inches(6.25), Inches(11.9), Inches(0.4),
     "Institutionally embedded: 4 District Road Safety Committees · MoUs with Jaipur Traffic Police & Gurugram Police · formally tasked by SW Delhi DRSC.",
     font=BODY, size=10.5, color=MUTED, ls=1.3)
footer(s, 5, TOTAL, "OPERATING MODEL")

# ============================================================ 06 PORTFOLIO OVERVIEW
s = new_slide(WHITE)
ny = std_header(s, "WHAT WE DO · AT A GLANCE",
                "Four working pillars,",
                "one accountability engine.",
                "Each pillar is explained on the following slides; detailed briefs are in the appendix.")
quads = [
    ("hard-hat", "01 · ROAD INFRASTRUCTURE", "Project Rakshak",
     "Engineering students audit dangerous roads to official standards; governments approve and build the fixes.",
     "25+ approvals · 15 builds begun"),
    ("scan-line", "02 · ENFORCEMENT TECHNOLOGY", "SATARK & AI billboards",
     "AI reads number plates, checks live records and helps traffic police stop the riskiest vehicles.",
     "₹30 Cr+ dues surfaced · 2 cities live"),
    ("hand-helping", "03 · POLICY & VICTIM SUPPORT", "Aasha & compensation reform",
     "Research, victim tools and government partnerships that make legal compensation actually reach families.",
     "100+ victims helped in first 4 days"),
    ("bar-chart-3", "04 · OPEN DATA & EDUCATION", "Public platforms & guides",
     "Self-updating public data tools plus comics and plain-language guides that make problems impossible to ignore.",
     "4 platforms · 36 states covered"),
]
cw = Inches(5.85); ch = Inches(1.72); gap = Inches(0.22)
for i,(icn,kick,t1,t2,stat) in enumerate(quads):
    x = M_L + (i%2)*(cw+gap); y = Inches(2.95) + (i//2)*(ch+Inches(0.2))
    rect(s, x, y, cw, ch, WHITE, line=BORDER, rounded=True)
    circle(s, x+Inches(0.22), y+Inches(0.24), Inches(0.5), BRAND_LITE)
    icon(s, icn, x+Inches(0.32), y+Inches(0.34), Inches(0.3), BLUE_HEX)
    text(s, x+Inches(0.88), y+Inches(0.18), cw-Inches(1.1), Inches(0.25), kick, font=HEAD, size=8.3, bold=True, color=MUTED, tracking=1.5)
    text(s, x+Inches(0.88), y+Inches(0.42), cw-Inches(1.1), Inches(0.3), t1, font=HEAD, size=13.5, bold=True, color=DARK)
    text(s, x+Inches(0.88), y+Inches(0.78), cw-Inches(1.1), Inches(0.6), t2, font=BODY, size=9.3, color=MUTED, ls=1.25)
    text(s, x+Inches(0.88), y+Inches(1.38), cw-Inches(1.1), Inches(0.28), stat, font=HEAD, size=9.5, bold=True, color=BRAND)
footer(s, 6, TOTAL, "WHAT WE DO · OVERVIEW")

# ============================================================ 07 RAKSHAK
s = new_slide(WHITE)
ny = std_header(s, "WHAT WE DO · 01 ROAD INFRASTRUCTURE",
                "Project Rakshak — engineering students",
                "audit dangerous roads; governments fix them.",
                "A national programme that mobilises trained student teams to audit high-risk locations to official standards and hand authorities ready-to-build fixes.")
whyrows = [
    ("WHY THIS", "Black spots are known and studied — converting reports into built fixes is the bottleneck we remove."),
    ("HOW IT WORKS", "Trained student teams audit to IRC / MoRTH standards and hand authorities ready-to-approve proposals."),
    ("WHY WE'RE PLACED TO DO IT", "A 9-IIT talent pipeline, mentors led by Prof. Geetam Tiwari (IIT Delhi), and a public tracking dashboard."),
]
wx = M_L
for kick, body in whyrows:
    text(s, wx, Inches(2.62), Inches(2.6), Inches(0.25), kick, font=HEAD, size=8.3, bold=True, color=BRAND, tracking=1.2)
    text(s, wx, Inches(2.88), Inches(2.62), Inches(0.85), body, font=BODY, size=8.8, color=MUTED, ls=1.28)
    wx += Inches(2.82)
funnel = [("120+", "locations\nscreened"), ("31", "sites audited ·\n11 blackspots"),
          ("25+", "government\napprovals"), ("15", "builds\nbegun")]
fx = M_L; fy = Inches(3.95); fw = Inches(1.85); fh = Inches(1.42)
for i,(num,lab) in enumerate(funnel):
    fill = BRAND if i==3 else BRAND_LITE
    tcol = WHITE if i==3 else BRAND
    lcol = LAV if i==3 else MUTED
    rect(s, fx, fy, fw, fh, fill, rounded=True)
    text(s, fx, fy+Inches(0.12), fw, Inches(0.6), num, font=HEAD, size=25, bold=True, color=tcol, align=PP_ALIGN.CENTER)
    text(s, fx, fy+Inches(0.72), fw, Inches(0.6), lab, font=BODY, size=8.5, color=lcol, align=PP_ALIGN.CENTER, ls=1.18)
    if i < 3:
        icon(s, "chevron-right", fx+fw+Inches(0.005), fy+fh/2-Inches(0.11), Inches(0.22), LAVDK_HEX)
    fx += fw + Inches(0.23)
text(s, M_L, Inches(5.5), Inches(8.2), Inches(0.28),
     "18 cities · 20 institutions incl. 9 IITs · 900+ stakeholder surveys · every site public on the dashboard",
     font=HEAD, size=9, bold=True, color=DARK, tracking=0.3)
rect(s, M_L, Inches(5.92), Inches(8.2), Inches(0.72), BRAND_LITE, rounded=True)
icon(s, "landmark", M_L+Inches(0.25), Inches(6.12), Inches(0.3), BLUE_HEX)
text(s, M_L+Inches(0.7), Inches(5.98), Inches(7.4), Inches(0.6),
     "Institutionalising the model: Cohort 2 runs three tracks — students, NGO partners, CRRI-certified auditors — building towards the Rakshak Audit Manual v1.0, usable by NHAI without rework.",
     font=BODY, size=9.5, color=DARK, ls=1.3, anchor=MSO_ANCHOR.MIDDLE)
try:
    db = os.path.join(V3, "new", "dashboard.png")
    ar = pic_ar(db); dw_ = Inches(3.55)
    rect(s, Inches(9.04), Inches(2.58), dw_+Inches(0.08), Inches(3.55/ar)+Inches(0.08), WHITE, line=BORDER)
    pic(s, db, Inches(9.08), Inches(2.62), w=dw_)
    text(s, Inches(9.08), Inches(2.62)+Inches(3.55/ar)+Inches(0.08), dw_, Inches(0.3),
         "The live implementation dashboard — every site, authority and status public.",
         font=BODY, size=8.2, color=MUTED, italic=True, ls=1.15)
    for j, (ivf, cap) in enumerate([("iv_indore_footpath", "Footpath — Indore"), ("iv_durgapur_parking", "Parking — Durgapur")]):
        p_ = os.path.join(V3, "new", f"{ivf}.png")
        arp = pic_ar(p_); ph_ = Inches(1.62)
        pic(s, p_, Inches(9.08)+j*Inches(1.85), Inches(4.95), h=ph_)
        text(s, Inches(9.08)+j*Inches(1.85), Inches(6.6), Inches(1.7), Inches(0.25), cap,
             font=BODY, size=7.5, color=MUTED, italic=True)
except Exception as e: print("rakshak visuals", e)
footer(s, 7, TOTAL, "WHAT WE DO · PROJECT RAKSHAK")

# ============================================================ 08 RAKSHAK APPROVALS (letter wall)
s = new_slide(BRAND_LITE)
ny = std_header(s, "WHAT WE DO · 01 ROAD INFRASTRUCTURE — THE PROOF",
                "Government approval, in writing:",
                "25+ signed authority letters and counting.",
                "A sample of the approval and acknowledgement letters issued to Rakshak student teams by public works and district authorities.")
letters = [("Visioneers", "Tejaji Nagar, Indore — approved interventions"),
           ("Crashzero", "Kunnamangalam Jn., Kozhikode — PWD Kerala"),
           ("Pathrakshak", "Kamta Chauraha, Lucknow — PWD (UP)"),
           ("Vision_Zero_Squad", "NH-205 & Surjit Chowk, Ropar — PWD (Punjab)")]
lx = M_L; lyy = Inches(3.05); lh = Inches(3.15)
for name, cap in letters:
    p = os.path.join(V3, "letters", f"{name}.png")
    try:
        ar = pic_ar(p); lw = Inches(3.15*ar)
        rect(s, lx-Inches(0.04), lyy-Inches(0.04), lw+Inches(0.08), lh+Inches(0.08), WHITE, line=BORDER)
        pic(s, p, lx, lyy, h=lh)
        text(s, lx, lyy+lh+Inches(0.08), lw+Inches(0.35), Inches(0.5), cap, font=BODY, size=8.3, color=MUTED, ls=1.15)
        lx += lw + Inches(0.42)
    except Exception as e: print("letter", name, e)
text(s, M_L, Inches(6.72), Inches(11.9), Inches(0.3),
     "Authorities include: PWD Kerala · PWD UP · PWD Punjab · CPWD & Addl. Collector Indore · ADDA Durgapur · R&B Andhra Pradesh · GCC Chennai",
     font=HEAD, size=8.8, bold=True, color=DARK, tracking=0.3)
footer(s, 8, TOTAL, "PROJECT RAKSHAK · APPROVALS")

# ============================================================ 09 SATARK
s = new_slide(WHITE)
ny = std_header(s, "WHAT WE DO · 02 ENFORCEMENT TECHNOLOGY",
                "SATARK — an AI platform that helps traffic",
                "police identify and stop high-risk vehicles.",
                "Cameras read every passing number plate and check it against live national records — officers act on evidence instead of stopping vehicles at random.")
stats = [("3,00,000+", "vehicles scanned"), ("₹30 Cr+", "pending challans surfaced"),
         ("350+", "high-risk vehicles intercepted"), ("2 cities live", "Jaipur & Bengaluru · 5 police approvals")]
sx = M_L; sy = Inches(3.1)
for i,(num,lab) in enumerate(stats):
    x = M_L + (i%2)*Inches(3.3); y = sy + (i//2)*Inches(1.05)
    text(s, x, y, Inches(3.1), Inches(0.5), num, font=HEAD, size=24, bold=True, color=BRAND)
    text(s, x, y+Inches(0.48), Inches(3.1), Inches(0.35), lab, font=BODY, size=9.5, color=MUTED, ls=1.15)
steps = ["Plate read", "Record check", "Rule engine", "Billboard + app", "Intercept"]
py2 = Inches(5.35); px2 = M_L
for i, st in enumerate(steps):
    wd = Inches(0.26 + 0.072*len(st))
    chip(s, px2, py2, wd, Inches(0.38), st, fill=BRAND_LITE, tcolor=BRAND, size=8.2)
    px2 += wd + Inches(0.05)
    if i < 4:
        icon(s, "chevron-right", px2-Inches(0.02), py2+Inches(0.08), Inches(0.2), LAVDK_HEX)
        px2 += Inches(0.14)
rect(s, M_L, Inches(6.05), Inches(6.4), Inches(0.6), BRAND_LITE, rounded=True)
text(s, M_L+Inches(0.25), Inches(6.05), Inches(6.0), Inches(0.6),
     "Built with police, not for them — departments set the flagging rules; CFI provides the technology. First 72 hours in Jaipur: 1,240 flagged, 58 intercepted.",
     font=HEAD, size=10, bold=True, color=BRAND, anchor=MSO_ANCHOR.MIDDLE, ls=1.25)
try:
    bp = os.path.join(V3, "embedded", "stk_p1_x20.png")
    ar = pic_ar(bp); bw_ = Inches(5.15)
    rect(s, Inches(7.42), Inches(2.86), bw_+Inches(0.08), Inches(5.15/ar)+Inches(0.08), WHITE, line=BORDER)
    pic(s, bp, Inches(7.46), Inches(2.9), w=bw_)
    text(s, Inches(7.46), Inches(2.9)+Inches(5.15/ar)+Inches(0.12), bw_, Inches(0.3),
         "Live SATARK billboard, Rambagh Circle, Jaipur — naming a passing vehicle's 4 pending challans in real time.",
         font=BODY, size=8.5, color=MUTED, italic=True, ls=1.2)
except Exception as e: print("billboard", e)
footer(s, 9, TOTAL, "WHAT WE DO · SATARK")

# ============================================================ 10 VICTIM SUPPORT
s = new_slide(BRAND_LITE)
ny = std_header(s, "WHAT WE DO · 03 POLICY & VICTIM SUPPORT",
                "Helping crash victims and families claim",
                "the compensation the law promises them.")
gaps_row = [("10.46 lakh", "cases pending"), ("205 vs ~25,000", "hit-and-run claims filed vs eligible"),
            ("3.6 years", "average wait"), ("2 of 102", "files settled in our Gurugram audit")]
gx = M_L
gw = [Inches(2.2), Inches(3.6), Inches(2.2), Inches(3.4)]
for (num, lab), wd in zip(gaps_row, gw):
    rect(s, gx, Inches(2.6), wd, Inches(0.78), WHITE, line=BORDER, rounded=True)
    text(s, gx+Inches(0.18), Inches(2.68), wd-Inches(0.3), Inches(0.35), num, font=HEAD, size=14.5, bold=True, color=DARK)
    text(s, gx+Inches(0.18), Inches(3.0), wd-Inches(0.3), Inches(0.3), lab, font=BODY, size=8.5, color=MUTED)
    gx += wd + Inches(0.17)
LX = M_L; LW = Inches(7.1); LY = Inches(3.62); LH = Inches(2.95)
rect(s, LX, LY, LW, LH, BRAND, rounded=True)
text(s, LX+Inches(0.3), LY+Inches(0.2), LW-Inches(0.6), Inches(0.3), "WHAT WE BUILT AND DO",
     font=HEAD, size=9.5, bold=True, color=LAV, tracking=1.8)
fix_rows = [
    ("bot", "Aasha — India's first 24/7 multilingual AI chatbot guiding victims step-by-step on WhatsApp & voice"),
    ("calculator", "Free Compensation Calculator based on Supreme Court principles (Sarla Verma, Pranay Sethi)"),
    ("hand-helping", "Legal helpdesks in hospital trauma wards — 100+ victims supported in the first 4 days"),
    ("landmark", "Embedded in 4 District Road Safety Committees — formally tasked by SW Delhi DRSC; fellow placed with Gurugram district offices"),
    ("route", "'Justice Unserved' presented to MoRTH; hit-and-run claim pipeline rebuild underway with Rajasthan Transport Dept."),
]
fy2 = LY + Inches(0.56)
for icn, lab in fix_rows:
    circle(s, LX+Inches(0.3), fy2, Inches(0.32), BRAND_MID)
    icon(s, icn, LX+Inches(0.36), fy2+Inches(0.06), Inches(0.2), WHITE_HEX)
    text(s, LX+Inches(0.75), fy2-Inches(0.01), LW-Inches(1.05), Inches(0.5), lab, font=BODY, size=9.6, color=WHITE, ls=1.2)
    fy2 += Inches(0.47)
try:
    g1 = os.path.join(V3, "extracted", "guide_p1.png")
    ar = pic_ar(g1); gh = Inches(2.95); gw_ = Inches(2.95*ar)
    rect(s, Inches(8.06), Inches(3.58), gw_+Inches(0.08), gh+Inches(0.08), WHITE, line=BORDER)
    pic(s, g1, Inches(8.1), Inches(3.62), h=gh)
    ju = os.path.join(V3, "new", "comp_image1.png")
    arj = pic_ar(ju)
    rect(s, Inches(8.1)+gw_+Inches(0.14), Inches(3.58), Inches(2.95*arj)+Inches(0.08), gh+Inches(0.08), WHITE, line=BORDER)
    pic(s, ju, Inches(8.14)+gw_+Inches(0.14), Inches(3.62), h=gh)
    text(s, Inches(8.1), Inches(6.62), Inches(4.5), Inches(0.3),
         "Hindi legal-rights guide (hospitals & police stations) · 'Justice Unserved' research brief.",
         font=BODY, size=8.5, color=MUTED, italic=True)
except Exception as e: print("guides", e)
footer(s, 10, TOTAL, "WHAT WE DO · VICTIM SUPPORT")

# ============================================================ 11 OPEN DATA
s = new_slide(WHITE)
ny = std_header(s, "WHAT WE DO · 04 OPEN DATA PLATFORMS",
                "Public data tools we built so that",
                "road-safety problems cannot be ignored.",
                "Four self-updating platforms — free for government, researchers, journalists and citizens.")
prods = [
    ("map-pinned", "National Road Defect Repository", "AI reads local news in 13 languages across 146 districts — potholes, missing signage, unlit stretches — mapped publicly."),
    ("landmark", "Road Safety in Parliament", "All 1,423 parliamentary road-safety questions since 2014, searchable by MP — 282 sitting MPs have never asked one."),
    ("scale", "Supreme Court Litigation Tracker", "18 live road-safety cases, 190+ orders, every government deadline tracked — 11 already overdue at launch."),
    ("bar-chart-3", "National Crash Data Dashboard", "Official crash statistics (2019–2024) turned into report cards for 36 states and 50 cities — openly licensed."),
]
cw = Inches(3.62); ch = Inches(1.72)
for i,(icn,t1,t2) in enumerate(prods):
    x = M_L + (i%2)*(cw+Inches(0.2)); y = Inches(2.95) + (i//2)*(ch+Inches(0.18))
    rect(s, x, y, cw, ch, WHITE, line=BORDER, rounded=True)
    circle(s, x+Inches(0.2), y+Inches(0.2), Inches(0.42), BRAND_LITE)
    icon(s, icn, x+Inches(0.28), y+Inches(0.28), Inches(0.26), BLUE_HEX)
    text(s, x+Inches(0.74), y+Inches(0.22), cw-Inches(0.95), Inches(0.5), t1, font=HEAD, size=10.5, bold=True, color=DARK, ls=1.1)
    text(s, x+Inches(0.2), y+Inches(0.78), cw-Inches(0.4), Inches(0.9), t2, font=BODY, size=8.6, color=MUTED, ls=1.25)
try:
    hb = os.path.join(V3, "embedded", "imp_p18_x87.png")
    ar = pic_ar(hb); hw = Inches(4.3)
    rect(s, Inches(8.12), Inches(2.91), hw+Inches(0.08), Inches(4.3/ar)+Inches(0.08), WHITE, line=BORDER)
    pic(s, hb, Inches(8.16), Inches(2.95), w=hw)
    text(s, Inches(8.16), Inches(2.95)+Inches(4.3/ar)+Inches(0.08), hw, Inches(0.3),
         "Road Safety Resources Hub — the public front door.",
         font=BODY, size=8.3, color=MUTED, italic=True)
    sm = os.path.join(V3, "embedded", "imp_p14_x70.png")
    ar2 = pic_ar(sm)
    pic(s, sm, Inches(8.16), Inches(5.6), w=Inches(4.3))
    text(s, Inches(8.16), Inches(5.6)+Inches(4.3/ar2)+Inches(0.06), Inches(4.3), Inches(0.3),
         "Citizen hazard-reporting apps — 50+ hazards in first 20 days.",
         font=BODY, size=8.3, color=MUTED, italic=True)
except Exception as e: print("hub", e)
text(s, M_L, Inches(6.72), Inches(7.4), Inches(0.3),
     "'Justice Unserved' in print: Deccan Herald · ET · Fortune India · IndiaSpend · Moneycontrol · Scroll.in · The Wire",
     font=HEAD, size=8.3, bold=True, color=MUTED, tracking=0.3)
footer(s, 11, TOTAL, "WHAT WE DO · OPEN DATA")

# ============================================================ 12 YOUTH & PUBLIC ENGAGEMENT
s = new_slide(WHITE)
ny = std_header(s, "WHAT WE DO · YOUTH MOBILISATION & PUBLIC EDUCATION",
                "NextMile, campus programmes and street-level",
                "education that bring citizens into road safety.")
text(s, M_L, Inches(2.6), Inches(7.0), Inches(0.3), "NEXTMILE — NATIONAL ROAD SAFETY POLICY IDEATHON (2025)",
     font=HEAD, size=10, bold=True, color=BRAND, tracking=1.4)
nm_funnel = [("700+", "registrations from\nIITs, IIMs, NLUs"), ("250+", "policy concept\nnotes submitted"),
             ("37", "teams mentored\nfor four weeks"), ("10", "finalists judged by\n24 national experts")]
fx = M_L; fy = Inches(3.0); fw = Inches(1.68); fh = Inches(1.5)
for i,(num,lab) in enumerate(nm_funnel):
    fill = BRAND if i==3 else BRAND_LITE
    tcol = WHITE if i==3 else BRAND
    lcol = LAV if i==3 else MUTED
    rect(s, fx, fy, fw, fh, fill, rounded=True)
    text(s, fx, fy+Inches(0.12), fw, Inches(0.6), num, font=HEAD, size=24, bold=True, color=tcol, align=PP_ALIGN.CENTER)
    text(s, fx, fy+Inches(0.72), fw, Inches(0.7), lab, font=BODY, size=8.3, color=lcol, align=PP_ALIGN.CENTER, ls=1.15)
    if i < 3:
        icon(s, "chevron-right", fx+fw+Inches(0.0), fy+fh/2-Inches(0.11), Inches(0.22), LAVDK_HEX)
    fx += fw + Inches(0.22)
rows2 = [
    ("graduation-cap", "Grand Finale at India Habitat Centre, Sept 2025 — jury included Justice J.R. Midha and ex-MoRTH leadership."),
    ("rocket", "Winning ideas feed CFI's own pipeline — compensation reform and rider safety became live workstreams."),
    ("book-open", "Street plays, comics and multilingual guides carry road-safety education beyond campuses."),
    ("users-round", "Next: 'Be a Rakshak' university chapters at IITs, NITs and SPAs, with MS Dhoni as the recruiting voice."),
]
ry = Inches(4.75)
for icn, lab in rows2:
    circle(s, M_L, ry, Inches(0.36), BRAND_LITE)
    icon(s, icn, M_L+Inches(0.075), ry+Inches(0.075), Inches(0.21), BLUE_HEX)
    text(s, M_L+Inches(0.55), ry+Inches(0.02), Inches(6.9), Inches(0.5), lab, font=BODY, size=9.8, color=DARK, ls=1.2)
    ry += Inches(0.5)
try:
    i1 = os.path.join(V3, "extracted", "ideathon_1.jpg")
    ar = pic_ar(i1); ih = Inches(3.85); iw = Inches(3.85*ar)
    rect(s, Inches(9.2), Inches(2.56), iw+Inches(0.08), ih+Inches(0.08), WHITE, line=BORDER)
    pic(s, i1, Inches(9.24), Inches(2.6), h=ih)
    text(s, Inches(9.24), Inches(6.52), Inches(3.3), Inches(0.3),
         "NextMile Grand Finale — winners on stage, Sept 2025.", font=BODY, size=8.5, color=MUTED, italic=True)
except Exception as e: print("ideathon", e)
footer(s, 12, TOTAL, "WHAT WE DO · YOUTH & EDUCATION")

# ============================================================ 13 IMPACT YEAR ONE
s = new_slide(BRAND_LITE)
ny = std_header(s, "IMPACT · OUR FIRST YEAR",
                "Year one: measurable results",
                "across 18 Indian cities.")
tiles = [("1M+", "citizens reached", "users"), ("18", "cities active", "map-pin"), ("25+", "govt approvals won", "badge-check"),
         ("15", "implementations begun", "hard-hat"), ("4", "district committees joined", "landmark"), ("2", "cities enforcing with SATARK", "scan-line"),
         ("150+", "members & interns", "users-round"), ("50+", "experts engaged", "graduation-cap"), ("10+", "national media features", "newspaper")]
cw = Inches(2.55); ch = Inches(1.06); gapx = Inches(0.18); gapy = Inches(0.16)
for i,(num,lab,icn) in enumerate(tiles):
    x = M_L + (i%3)*(cw+gapx); y = Inches(2.5) + (i//3)*(ch+gapy)
    rect(s, x, y, cw, ch, WHITE, line=BORDER, rounded=True)
    icon(s, icn, x+cw-Inches(0.48), y+Inches(0.16), Inches(0.26), "#C8C0FF")
    text(s, x+Inches(0.22), y+Inches(0.12), cw-Inches(0.4), Inches(0.5), num, font=HEAD, size=23, bold=True, color=BRAND)
    text(s, x+Inches(0.22), y+Inches(0.62), cw-Inches(0.4), Inches(0.35), lab, font=BODY, size=9.3, color=MUTED)
TX = Inches(9.15); TW = Inches(3.48)
rect(s, TX, Inches(2.5), TW, Inches(3.95), BRAND, rounded=True)
text(s, TX+Inches(0.28), Inches(2.72), TW-Inches(0.56), Inches(0.3), "THE FIRST 400 DAYS",
     font=HEAD, size=9.5, bold=True, color=LAV, tracking=1.8)
tl = [("Jun 25", "Launched as a Cars24 commitment"),
      ("Sep 25", "NextMile finale · first AI billboard live in Bengaluru"),
      ("Jan 26", "'Justice Unserved' published"),
      ("Apr 26", "IIT Delhi national forum · Dhoni joins"),
      ("Jun 26", "SATARK live with Jaipur Police"),
      ("Jul 26", "Rakshak Cohort 2 · 4 open-data products shipped")]
tly = Inches(3.14)
for d, ev in tl:
    text(s, TX+Inches(0.28), tly, Inches(0.72), Inches(0.3), d, font=HEAD, size=9, bold=True, color=LAV)
    text(s, TX+Inches(1.05), tly, TW-Inches(1.32), Inches(0.5), ev, font=BODY, size=9, color=WHITE, ls=1.18)
    tly += Inches(0.55)
text(s, M_L, Inches(6.35), Inches(3.4), Inches(0.3), "WORKING ALONGSIDE:",
     font=HEAD, size=8.5, bold=True, color=MUTED, tracking=1.5)
partners = ["MoRTH", "WHO", "UNICEF", "CSIR-CRRI", "IRF", "FICCI", "IIT Delhi", "Jaipur Traffic Police", "Gurugram Police"]
px3 = M_L; py3 = Inches(6.62)
for p_ in partners:
    wd = Inches(0.3 + 0.085*len(p_))
    chip(s, px3, py3, wd, Inches(0.34), p_, fill=WHITE, tcolor=DARK, size=8, line=BORDER)
    px3 += wd + Inches(0.12)
footer(s, 13, TOTAL, "IMPACT · OUR FIRST YEAR")

# ============================================================ 14 DHONI
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
try:
    _har = pic_ar(os.path.join(BUILD_DIR, "dhoni_cutout_white.png"))
    HH = Inches(5.1); HW = Inches(5.1*_har)
    pic(s, os.path.join(BUILD_DIR, "dhoni_cutout_white.png"), Inches(12.63)-HW, Inches(1.35), w=HW, h=HH)
    text(s, Inches(8.9), Inches(6.5), Inches(3.9), Inches(0.25), "CFI shoot · June 2026",
         font=BODY, size=8.5, color=LAV, italic=True, align=PP_ALIGN.CENTER)
except Exception as e: print("dhoni", e)
footer_dark(s, 14, "OUR AMBASSADOR")

# ============================================================ 15 GOVERNANCE
s = new_slide(WHITE)
ny = std_header(s, "OUR PEOPLE · BOARD OF ADVISORS & EXPERTS",
                "Guided by two of India's foremost",
                "road-safety experts.")
boa = [
    ("Piyush Tewari", "Founder & CEO, SaveLIFE Foundation", None,
     ["Architect of India's Good Samaritan Law (Supreme Court, 2016)",
      "Built the Zero Fatality Corridor model — ~40% fewer deaths on Mumbai–Pune Expressway; scaling with MoRTH",
      "Rolex Award for Enterprise · Elevate Prize · MPA, Harvard"]),
    ("Prof. (Dr.) Geetam Tiwari", "Professor Emerita, TRIPC, IIT Delhi", "gtiwari",
     ["Three decades leading India's foremost road-safety research centre — a WHO Collaborating Centre",
      "Global authority on vulnerable road users & safe-system design · PhD, University of Illinois Chicago",
      "Guides Project Rakshak's audit methodology; anchors our Expert Consortium"]),
]
cw = Inches(5.85); ch = Inches(2.28); gap = Inches(0.22)
for i,(nm, ti, head, pts) in enumerate(boa):
    x = M_L + i*(cw+gap); y = Inches(2.4)
    rect(s, x, y, cw, ch, WHITE, line=BORDER, rounded=True)
    hp = os.path.join(V3, "heads", f"{head}.png") if head else None
    if hp and os.path.exists(hp):
        pic(s, hp, x+Inches(0.28), y+Inches(0.26), w=Inches(0.82), h=Inches(0.82))
    else:
        circle(s, x+Inches(0.28), y+Inches(0.26), Inches(0.82), BRAND)
        initials = "".join(w[0] for w in nm.replace("Prof. (Dr.) ","").split()[:2])
        text(s, x+Inches(0.28), y+Inches(0.26), Inches(0.82), Inches(0.82), initials, font=HEAD, size=19, bold=True,
             color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(s, x+Inches(1.25), y+Inches(0.26), cw-Inches(1.5), Inches(0.35), nm, font=HEAD, size=15, bold=True, color=DARK)
    text(s, x+Inches(1.25), y+Inches(0.64), cw-Inches(1.5), Inches(0.3), ti, font=HEAD, size=10.5, bold=True, color=BRAND)
    py2 = y + Inches(1.02)
    for p_ in pts:
        circle(s, x+Inches(1.27), py2+Inches(0.07), Inches(0.08), BRAND)
        text(s, x+Inches(1.5), py2, cw-Inches(1.8), Inches(0.5), p_, font=BODY, size=8.7, color=MUTED, ls=1.18)
        py2 += Inches(0.41)
text(s, M_L, Inches(4.9), Inches(6), Inches(0.3), "THE EXPERT BENCH BEHIND OUR WORK",
     font=HEAD, size=9.5, bold=True, color=MUTED, tracking=1.8)
bench = [("midha", "Justice J. R. Midha (Retd.)", "Delhi High Court · FastDAR architect"),
         ("damle", "Abhay Damle", "Former Joint Secretary, MoRTH"),
         ("dange", "Vaibhav Dange", "Former Advisor, MoRTH"),
         (None, "Dr. S. Velmurugan", "Head, Traffic Engg. & Safety, CSIR-CRRI"),
         (None, "Dr. Richa Ahuja", "IIT Kharagpur · Rakshak advisor"),
         ("asrivastava", "Akhilesh Srivastava", "ITS India · IRF"),
         ("tandon", "Dr. Maya Tandon", "Sahayta Trust, Jaipur"),
         ("ratnam", "R. Venkat Ratnam", "DG, Punjab Road Safety Lead Agency"),
         ("pandey", "Rama Shankar Pandey", "FICCI Road Safety")]
cw2 = Inches(3.85); ch2 = Inches(0.52)
for i,(head,nm,ti) in enumerate(bench):
    x = M_L + (i%3)*(cw2+Inches(0.19)); y = Inches(5.2) + (i//3)*(ch2+Inches(0.07))
    rect(s, x, y, cw2, ch2, BRAND_LITE, rounded=True)
    hp = os.path.join(V3, "heads", f"{head}.png") if head else None
    if hp and os.path.exists(hp):
        pic(s, hp, x+Inches(0.08), y+Inches(0.06), w=Inches(0.44), h=Inches(0.44))
    else:
        circle(s, x+Inches(0.08), y+Inches(0.06), Inches(0.44), BRAND)
        text(s, x+Inches(0.08), y+Inches(0.06), Inches(0.44), Inches(0.44),
             "".join(w[0] for w in nm.replace("Dr. ","").replace("Justice ","").split()[:2]),
             font=HEAD, size=10, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(s, x+Inches(0.62), y+Inches(0.06), cw2-Inches(0.75), Inches(0.24), nm, font=HEAD, size=9.2, bold=True, color=DARK)
    text(s, x+Inches(0.62), y+Inches(0.3), cw2-Inches(0.75), Inches(0.2), ti, font=BODY, size=7.7, color=MUTED)
footer(s, 15, TOTAL, "BOARD OF ADVISORS & EXPERTS")

# ============================================================ 16 TEAM
s = new_slide(WHITE)
ny = std_header(s, "OUR PEOPLE · THE TEAM",
                "A full-time team of eight, three trustees,",
                "and 75+ engineering interns nationwide.")
trustees = [
    ("Amar Srivastava", "President", "Founder, Indian Road Safety Council — 50,000+ volunteers · Diana Award 2019"),
    ("Deepanshu Gupta", "Managing Trustee", "Founder, IRSC · Global Youth Coalition for Road Safety leadership board"),
    ("Gajendra Jangid", "General Secretary", "Co-founder, Cars24 · ex-Schlumberger"),
]
text(s, M_L, Inches(2.42), Inches(4), Inches(0.28), "TRUSTEES · VISION ZERO TRUST",
     font=HEAD, size=9, bold=True, color=MUTED, tracking=1.6)
cw = Inches(2.9); ch = Inches(1.42); gap = Inches(0.14)
for i,(nm,ro,cred) in enumerate(trustees):
    x = M_L + i*(cw+gap); y = Inches(2.75)
    rect(s, x, y, cw, ch, BRAND_LITE, rounded=True)
    circle(s, x+Inches(0.18), y+Inches(0.18), Inches(0.52), BRAND)
    text(s, x+Inches(0.18), y+Inches(0.18), Inches(0.52), Inches(0.52), "".join(w[0] for w in nm.split()[:2]),
         font=HEAD, size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(s, x+Inches(0.82), y+Inches(0.16), cw-Inches(1.0), Inches(0.28), nm, font=HEAD, size=10.2, bold=True, color=DARK)
    text(s, x+Inches(0.82), y+Inches(0.44), cw-Inches(1.0), Inches(0.25), ro, font=HEAD, size=8.5, bold=True, color=BRAND)
    text(s, x+Inches(0.18), y+Inches(0.76), cw-Inches(0.36), Inches(0.6), cred, font=BODY, size=7.7, color=MUTED, ls=1.18)
team = [
    ("Akhtar Hussain", "Mission Lead", "IIT Delhi · ex-Bain & Co., Deloitte"),
    ("Shubham Kumar", "Policy Advocacy", "DU + NALSAR · byline: Scroll.in"),
    ("Muskan Yadav", "Programs · Infrastructure", "TISS Mumbai"),
    ("Aastha Shreeharsh", "Strategy & Operations", "HKUST · quoted in The Wire"),
    ("Rohan Sharma", "Cause Marketing", "ex-Unacademy"),
    ("Ishita Rathore", "People & Culture", ""),
    ("Yuvraj Yadav", "Product Design", ""),
    ("Shipra Kushwaha", "Graphic Design", ""),
]
text(s, M_L, Inches(4.34), Inches(4), Inches(0.28), "FULL-TIME TEAM",
     font=HEAD, size=9, bold=True, color=MUTED, tracking=1.6)
cw2 = Inches(2.15); ch2 = Inches(0.98)
for i,(nm,ro,cred) in enumerate(team):
    x = M_L + (i%4)*(cw2+Inches(0.13)); y = Inches(4.62) + (i//4)*(ch2+Inches(0.12))
    rect(s, x, y, cw2, ch2, WHITE, line=BORDER, rounded=True)
    circle(s, x+Inches(0.12), y+Inches(0.12), Inches(0.38), BRAND_LITE)
    text(s, x+Inches(0.12), y+Inches(0.12), Inches(0.38), Inches(0.38), "".join(w[0] for w in nm.split()[:2]),
         font=HEAD, size=9.5, bold=True, color=BRAND, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(s, x+Inches(0.58), y+Inches(0.1), cw2-Inches(0.68), Inches(0.4), nm, font=HEAD, size=9.0, bold=True, color=DARK, ls=1.05)
    text(s, x+Inches(0.12), y+Inches(0.52), cw2-Inches(0.24), Inches(0.22), ro, font=BODY, size=7.6, color=BRAND)
    text(s, x+Inches(0.12), y+Inches(0.73), cw2-Inches(0.24), Inches(0.24), cred, font=BODY, size=6.9, color=MUTED)
try:
    i2 = os.path.join(V3, "extracted", "ideathon_2.jpg")
    ar = pic_ar(i2); ih = Inches(3.55); iw = Inches(3.55*ar)
    rect(s, Inches(12.63)-iw-Inches(0.08), Inches(2.71), iw+Inches(0.08), ih+Inches(0.08), WHITE, line=BORDER)
    pic(s, i2, Inches(12.63)-iw-Inches(0.04), Inches(2.75), h=ih)
    text(s, Inches(12.63)-iw-Inches(0.04), Inches(6.38), iw, Inches(0.5),
         "Team members at the NextMile Grand Finale, Sept 2025.", font=BODY, size=8.3, color=MUTED, italic=True, ls=1.2)
except Exception as e: print("team photo", e)
text(s, M_L, Inches(6.85), Inches(8.5), Inches(0.3),
     "+ 75+ part-time road-engineering interns across India",
     font=BODY, size=9, color=MUTED, italic=True)
footer(s, 16, TOTAL, "THE TEAM")

# ============================================================ 17 CLOSE
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
hline(s, M_L, Inches(4.5), Inches(11.9), color=LAV_DK)
text(s, M_L, Inches(4.72), Inches(5.5), Inches(0.3), "YEAR TWO, WITH YOU — THE TARGETS",
     font=HEAD, size=9.5, bold=True, color=LAV, tracking=1.8)
targets = ["150+ blackspots audited by the national pipeline",
           "Model districts: Gurugram · SW Delhi · Jaipur",
           "12+ district-committee presentations",
           "Rakshak Audit Manual v1.0 — usable by NHAI without rework"]
ty = Inches(5.1)
for t in targets:
    circle(s, M_L+Inches(0.02), ty+Inches(0.05), Inches(0.14), LAV)
    text(s, M_L+Inches(0.35), ty, Inches(5.6), Inches(0.3), t, font=BODY, size=10.5, color=WHITE, ls=1.2)
    ty += Inches(0.4)
text(s, Inches(7.2), Inches(4.72), Inches(5.4), Inches(0.3), "START THE CONVERSATION",
     font=HEAD, size=9.5, bold=True, color=LAV, tracking=1.8)
contact = [("globe", "crashfreeindia.org"), ("mail", "helpdesk@crashfreeindia.org"),
           ("bar-chart-3", "Live proof: crashfreeindia.org/rakshak/dashboard")]
cy2 = Inches(5.1)
for icn, t in contact:
    icon(s, icn, Inches(7.2), cy2+Inches(0.01), Inches(0.24), "#C8C0FF")
    text(s, Inches(7.58), cy2, Inches(5.0), Inches(0.3), t, font=BODY, size=10.5, color=WHITE)
    cy2 += Inches(0.42)
text(s, M_L, Inches(6.6), Inches(11.9), Inches(0.35),
     "Lasting change happens when someone owns the follow-through. That is the job we have taken on.",
     font=HEAD, size=12, bold=True, color=WHITE, italic=True)
text(s, M_L, Inches(7.05), Inches(11.9), Inches(0.3),
     "Crashfree India · A Cars24 Commitment · operated by Vision Zero Trust", font=HEAD, size=8.5,
     color=LAV, tracking=1.6, bold=True)

# ============================================================ 18 APPENDIX DIVIDER
s = new_slide(BRAND)
logo(s, M_L, Inches(0.5), Inches(2.1), dark=True)
text(s, Inches(8.6), Inches(0.6), Inches(4.0), Inches(3.2), "A", font=HEAD, size=220, bold=True,
     color=LAV_DK, align=PP_ALIGN.CENTER)
text(s, M_L, Inches(2.7), Inches(8.0), Inches(0.4), "REFERENCE MATERIAL", font=HEAD, size=10, bold=True,
     color=LAV, tracking=2.4)
text(s, M_L, Inches(3.1), Inches(9.0), Inches(0.8), "Appendix:", font=HEAD, size=44, bold=True, color=WHITE)
text(s, M_L, Inches(3.95), Inches(9.0), Inches(0.8), "programme deep-dives.", font=HEAD, size=44, bold=True, color=LAV)
items = ["A1  Project Rakshak — model & Cohort 2", "A2  Rakshak — approvals & site evidence",
         "A3  SATARK — product & deployment", "A4  'Justice Unserved' — key findings",
         "A5  Open-data platforms in detail", "A6  NextMile & public education", "A7  Press & contact"]
iy = Inches(4.95)
for it in items:
    text(s, M_L, iy, Inches(8.5), Inches(0.3), it, font=BODY, size=10.5, color=LAV)
    iy += Inches(0.29)
footer_dark(s, 18, "APPENDIX")

# ============================================================ 19 A1 RAKSHAK MODEL
s = new_slide(WHITE)
ny = std_header(s, "APPENDIX A1 · PROJECT RAKSHAK",
                "The Rakshak model: a four-phase audit",
                "pipeline, now scaling into three tracks.")
phases = [("P1 · Jul–Aug", "Research", "Teams form at campuses; risks identified via FIRs, RTIs, police data and local media."),
          ("P2 · Aug–Sep", "Field work", "30+ stakeholder surveys per team; audits to IRC / MoRTH checklists under expert masterclasses."),
          ("P3 · Oct–Nov", "Solutions", "Root-cause analysis; costed, standards-compliant redesigns reviewed by mentors."),
          ("P4 · Nov onwards", "Accountability", "Authority-format reports presented to PWD / municipal / police officials; approvals & builds tracked publicly.")]
pxx = M_L; pyy = Inches(2.6); pw = Inches(2.0); ph = Inches(2.15)
for i,(d,t1,t2) in enumerate(phases):
    rect(s, pxx, pyy, pw, ph, WHITE, line=BORDER, rounded=True)
    text(s, pxx+Inches(0.16), pyy+Inches(0.16), pw-Inches(0.32), Inches(0.25), d, font=HEAD, size=8.2, bold=True, color=BRAND, tracking=0.8)
    text(s, pxx+Inches(0.16), pyy+Inches(0.44), pw-Inches(0.32), Inches(0.3), t1, font=HEAD, size=12.5, bold=True, color=DARK)
    text(s, pxx+Inches(0.16), pyy+Inches(0.8), pw-Inches(0.32), Inches(1.25), t2, font=BODY, size=8.5, color=MUTED, ls=1.26)
    if i < 3:
        icon(s, "chevron-right", pxx+pw+Inches(0.0), pyy+ph/2-Inches(0.11), Inches(0.2), LAVDK_HEX)
    pxx += pw + Inches(0.21)
text(s, M_L, Inches(5.05), Inches(8), Inches(0.3), "COHORT 2 (2026-27) — THREE TRACKS, ALL [TARGETS]",
     font=HEAD, size=9.5, bold=True, color=MUTED, tracking=1.6)
tracks = [("Institutional", "IIT / NIT / SPA student teams — ~90 sites"),
          ("NGO partners", "~20 sites · 100% desk review · 10–15% CFI re-checks"),
          ("Certified RSAs", "CRRI-certified auditors · full IRC SP:88 · 'usable by NHAI without rework' · ~40 sites")]
tyy = Inches(5.4)
for t1, t2 in tracks:
    rect(s, M_L, tyy, Inches(8.55), Inches(0.44), BRAND_LITE, rounded=True)
    text(s, M_L+Inches(0.2), tyy, Inches(2.0), Inches(0.44), t1, font=HEAD, size=9.5, bold=True, color=BRAND, anchor=MSO_ANCHOR.MIDDLE)
    text(s, M_L+Inches(2.3), tyy, Inches(6.1), Inches(0.44), t2, font=BODY, size=9, color=DARK, anchor=MSO_ANCHOR.MIDDLE)
    tyy += Inches(0.52)
try:
    hm = os.path.join(V3, "embedded", "imp_p6_x42.png")
    ar = pic_ar(hm); hh = Inches(4.0)
    rect(s, Inches(9.56), Inches(2.56), Inches(4.0*ar)+Inches(0.08), hh+Inches(0.08), WHITE, line=BORDER)
    pic(s, hm, Inches(9.6), Inches(2.6), h=hh)
    text(s, Inches(9.6), Inches(6.65), Inches(3.2), Inches(0.3), "Risk heat-map of the 31 audited corridors.",
         font=BODY, size=8.3, color=MUTED, italic=True)
except Exception as e: print("heatmap", e)
footer(s, 19, TOTAL, "APPENDIX · RAKSHAK MODEL")

# ============================================================ 20 A2 RAKSHAK EVIDENCE
s = new_slide(WHITE)
ny = std_header(s, "APPENDIX A2 · PROJECT RAKSHAK",
                "From site survey to signed approval:",
                "what the paper trail looks like.")
try:
    sn = os.path.join(V3, "letters", "Sentinels.png")
    ar = pic_ar(sn); sh = Inches(3.9)
    rect(s, M_L-Inches(0.04), Inches(2.56), Inches(3.9*ar)+Inches(0.08), sh+Inches(0.08), WHITE, line=BORDER)
    pic(s, sn, M_L, Inches(2.6), h=sh)
    text(s, M_L, Inches(6.55), Inches(3.2), Inches(0.3), "Chennai: site photos + engineer suggestions (Team Sentinels).",
         font=BODY, size=8.3, color=MUTED, italic=True, ls=1.15)
    sg = os.path.join(V3, "letters", "Safegrid.png")
    ar2 = pic_ar(sg); sh2 = Inches(3.9)
    rect(s, Inches(4.16), Inches(2.56), Inches(3.9*ar2)+Inches(0.08), sh2+Inches(0.08), WHITE, line=BORDER)
    pic(s, sg, Inches(4.2), Inches(2.6), h=sh2)
    text(s, Inches(4.2), Inches(6.55), Inches(3.2), Inches(0.3), "Official acknowledgement on state letterhead (Team Safegrid).",
         font=BODY, size=8.3, color=MUTED, italic=True, ls=1.15)
except Exception as e: print("a2 letters", e)
RX = Inches(7.6); RW = Inches(5.0)
rect(s, RX, Inches(2.6), RW, Inches(3.55), BRAND_LITE, rounded=True)
text(s, RX+Inches(0.28), Inches(2.82), RW-Inches(0.56), Inches(0.3), "WHAT AUTHORITIES APPROVED (EXAMPLES)",
     font=HEAD, size=9, bold=True, color=BRAND, tracking=1.4)
exs = [("Tejaji Nagar, Indore", "signal, refuge island, speed calming, footpaths — CPWD & Addl. Collector"),
       ("Kamta Chauraha, Lucknow", "complete junction redesign package — PWD"),
       ("NH-205 / Surjit Chowk, Ropar", "high-friction surfacing, signage, crossings — PWD Punjab"),
       ("Kunnamangalam Jn., Kozhikode", "reflective studs, markings, signage — PWD Kerala"),
       ("Thiruvottiyur Jn., Chennai", "speed breakers repaired to IRC spec, thermoplastic paint — GCC")]
ey = Inches(3.2)
for t1, t2 in exs:
    text(s, RX+Inches(0.28), ey, RW-Inches(0.56), Inches(0.5),
         [(t1+"  ", {'font':HEAD,'size':9.5,'bold':True,'color':DARK}),
          ("— "+t2, {'font':BODY,'size':8.8,'color':MUTED})], ls=1.2)
    ey += Inches(0.56)
text(s, RX, Inches(6.45), RW, Inches(0.4),
     "Full set of 25+ letters available in the Rakshak approvals folder.",
     font=BODY, size=9, color=MUTED, italic=True)
footer(s, 20, TOTAL, "APPENDIX · RAKSHAK EVIDENCE")

# ============================================================ 21 A3 SATARK DETAIL
s = new_slide(WHITE)
ny = std_header(s, "APPENDIX A3 · SATARK",
                "Inside SATARK: from camera to",
                "intercept in under a minute.")
pipe = [("camera", "ANPR camera\nreads every plate"),
        ("database", "Live vehicle record\nvia national APIs"),
        ("list-filter", "Rule engine flags\nhabitual offenders"),
        ("tv", "Public billboard\nnames the risk"),
        ("shield-check", "Officer app routes\nthe interception")]
px_ = M_L; py_ = Inches(2.6); pw = Inches(1.62); ph = Inches(1.5)
for i,(icn,lab) in enumerate(pipe):
    rect(s, px_, py_, pw, ph, WHITE, line=BORDER, rounded=True)
    circle(s, px_+pw/2-Inches(0.24), py_+Inches(0.14), Inches(0.48), BRAND_LITE)
    icon(s, icn, px_+pw/2-Inches(0.14), py_+Inches(0.24), Inches(0.28), BLUE_HEX)
    text(s, px_, py_+Inches(0.72), pw, Inches(0.6), lab, font=BODY, size=8, color=DARK, align=PP_ALIGN.CENTER, ls=1.18)
    if i < 4:
        icon(s, "chevron-right", px_+pw-Inches(0.005), py_+ph/2-Inches(0.1), Inches(0.2), LAVDK_HEX)
    px_ += pw + Inches(0.2)
det = [("Deployment", "Live: Jaipur (Rambagh Circle billboard, officer app) & Bengaluru (Trinity Circle billboard) · approvals from 5 police forces · upcoming: Gurugram, Pune, Ahmedabad"),
       ("Officer app", "Prioritised vehicle queue · full challan history via national APIs · plain-language intelligence summary · one-tap outcome logging (intercepted / missed / dismissed)"),
       ("Why it matters", "46 Cr e-challans issued nationally, ~75% unpaid — SATARK turns that dormant record into live, targeted roadside enforcement"),
       ("Flagging criteria", "Set by police, not CFI — e.g. 10+ pending challans or ₹10,000+ outstanding · 20,000+ vehicles flagged on these rules so far")]
dy = Inches(4.35)
for t1, t2 in det:
    text(s, M_L, dy, Inches(1.85), Inches(0.5), t1.upper(), font=HEAD, size=8.5, bold=True, color=BRAND, tracking=1.2)
    text(s, M_L+Inches(2.0), dy, Inches(6.8), Inches(0.55), t2, font=BODY, size=9, color=MUTED, ls=1.25)
    dy += Inches(0.62)
try:
    ap = os.path.join(V3, "embedded", "stk_p1_x22.png")
    ar = pic_ar(ap); ah = Inches(3.9)
    rect(s, Inches(9.66), Inches(2.56), Inches(3.9*ar)+Inches(0.08), ah+Inches(0.08), WHITE, line=BORDER)
    pic(s, ap, Inches(9.7), Inches(2.6), h=ah)
    text(s, Inches(9.7), Inches(6.55), Inches(2.9), Inches(0.3), "The officer app: captured vehicle, live intelligence summary.",
         font=BODY, size=8.3, color=MUTED, italic=True, ls=1.15)
except Exception as e: print("appui", e)
footer(s, 21, TOTAL, "APPENDIX · SATARK")

# ============================================================ 22 A4 JUSTICE UNSERVED
s = new_slide(BRAND_LITE)
ny = std_header(s, "APPENDIX A4 · RESEARCH",
                "'Justice Unserved': why crash compensation",
                "fails, in five measured gaps.",
                "Published January 2026; launched at IIT Delhi; findings presented to MoRTH and cited by national press.")
gaps5 = [
    ("eye-off", "Awareness", "70% of low-income families don't know compensation exists; tout networks fill the vacuum."),
    ("clock", "Timeliness", "3.6-year average claim; typical MACT case runs 8–10 years."),
    ("file-x", "Legal efficiency", "90% of pending hit-and-run claims are stalled on documentation alone."),
    ("trending-down", "Adequacy", "Informal workers valued at minimum wage; courts repeatedly enhance awards on appeal."),
    ("users", "Equity", "14% of low-income households receive insurance compensation vs 24% of high-income."),
]
cw = Inches(2.28); ch = Inches(1.85); cx = M_L; cy = Inches(2.75)
for icn, t1, t2 in gaps5:
    rect(s, cx, cy, cw, ch, WHITE, line=BORDER, rounded=True)
    circle(s, cx+Inches(0.2), cy+Inches(0.17), Inches(0.4), BRAND_LITE)
    icon(s, cx and icn, cx+Inches(0.28), cy+Inches(0.25), Inches(0.24), BLUE_HEX)
    text(s, cx+Inches(0.2), cy+Inches(0.64), cw-Inches(0.4), Inches(0.3), t1, font=HEAD, size=11, bold=True, color=DARK)
    text(s, cx+Inches(0.2), cy+Inches(0.94), cw-Inches(0.4), Inches(0.9), t2, font=BODY, size=8.3, color=MUTED, ls=1.22)
    cx += cw + Inches(0.15)
try:
    js = os.path.join(V3, "new", "journey_strip.png")
    arj = pic_ar(js); jw = Inches(8.0); jh = Inches(8.0)/arj
    rect(s, M_L-Inches(0.04), Inches(4.81), jw+Inches(0.08), jh+Inches(0.08), WHITE, line=BORDER)
    pic(s, js, M_L, Inches(4.85), w=jw)
    text(s, M_L, Inches(4.85)+jh+Inches(0.07), jw, Inches(0.25),
         "The claim journey we mapped in Jaipur — six institutions from FIR to payment; every hand-off manual today.",
         font=BODY, size=8.3, color=MUTED, italic=True)
except Exception as e: print("journey", e)
rect(s, Inches(9.0), Inches(4.81), Inches(3.63), Inches(1.9), BRAND, rounded=True)
text(s, Inches(9.3), Inches(4.81), Inches(3.05), Inches(1.9),
     "205 claims filed vs ~25,000 eligible.\nThe pipeline, not the scheme, is the gap — so that is what we are fixing, office by office.",
     font=HEAD, size=10.5, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE, ls=1.35)
footer(s, 22, TOTAL, "APPENDIX · JUSTICE UNSERVED")

# ============================================================ 23 A5 DATA PLATFORMS DETAIL
s = new_slide(WHITE)
ny = std_header(s, "APPENDIX A5 · OPEN DATA",
                "The data commons, in numbers.")
rows3 = [
    ("National Road Defect Repository", "cfi-defect-repository.vercel.app", "AI reads local-language news daily in 13 languages across 146 districts (Bihar, UP, Rajasthan); defects geocoded and clustered into ranked public hotspot maps with verbatim source evidence."),
    ("Road Safety in Parliament", "road-safety-parliament.vercel.app", "1,423 questions across 4 ministries since 2014; find-your-MP report cards; live session tracking; RTI Watch pairs it with CFI's Delhi MACT RTI campaign."),
    ("SC Litigation Tracker", "sc-litigation-tracker", "18 live cases, 190+ orders, 27 precedent judgments; an accountability ledger of Supreme Court directions with auto-flipping deadlines — 11 overdue at launch."),
    ("Crash Data Dashboard", "cfi-crash-dashboard.vercel.app", "MoRTH's 266-page annual reports productised: 2019–2024 data, report cards for 36 states + 50 cities, 21 verified findings, CC-BY open license."),
]
ry3 = Inches(2.3)
for t1, t2, t3 in rows3:
    rect(s, M_L, ry3, Inches(7.5), Inches(1.02), WHITE, line=BORDER, rounded=True)
    text(s, M_L+Inches(0.22), ry3+Inches(0.12), Inches(4.6), Inches(0.28), t1, font=HEAD, size=10.5, bold=True, color=DARK)
    text(s, M_L+Inches(4.9), ry3+Inches(0.14), Inches(2.4), Inches(0.24), t2, font=BODY, size=7.8, color=BRAND)
    text(s, M_L+Inches(0.22), ry3+Inches(0.42), Inches(7.1), Inches(0.55), t3, font=BODY, size=8.5, color=MUTED, ls=1.22)
    ry3 += Inches(1.12)
try:
    nd = os.path.join(V3, "embedded", "imp_p8_x50.png")
    ar = pic_ar(nd); nw = Inches(4.2)
    rect(s, Inches(8.36), Inches(2.36), nw+Inches(0.08), Inches(4.2/ar)+Inches(0.08), WHITE, line=BORDER)
    pic(s, nd, Inches(8.4), Inches(2.4), w=nw)
    text(s, Inches(8.4), Inches(2.4)+Inches(4.2/ar)+Inches(0.1), nw, Inches(0.5),
         "Live crash-data walkthrough at the NextMile finale — the dashboards in use.",
         font=BODY, size=8.5, color=MUTED, italic=True, ls=1.2)
except Exception as e: print("dash photo", e)
text(s, M_L, Inches(6.85), Inches(11), Inches(0.3),
     "All four platforms are self-updating cloud services — nothing depends on any one person's laptop.",
     font=BODY, size=9.5, color=MUTED, italic=True)
footer(s, 23, TOTAL, "APPENDIX · OPEN DATA")

# ============================================================ 24 A6 NEXTMILE & EDUCATION
s = new_slide(WHITE)
ny = std_header(s, "APPENDIX A6 · YOUTH & EDUCATION",
                "NextMile's six policy tracks, and the",
                "education assets that travel beyond campuses.")
tracks6 = ["Speed management", "Delivery-rider safety", "Road-safety data transparency",
           "Crash-claim compensation reform", "Local blackspot identification", "On-road emergency protocols"]
tx6 = M_L; ty6 = Inches(2.55)
for i, t in enumerate(tracks6):
    x = M_L + (i%3)*Inches(2.9); y = ty6 + (i//3)*Inches(0.52)
    chip(s, x, y, Inches(2.75), Inches(0.42), t, fill=BRAND_LITE, tcolor=BRAND, size=8.5)
edu = [
    ("book-open", "'Know Your Rights with Aasha' comic", "Three compensation pathways explained in comic form — Hit & Run Scheme (₹2L), Section 164 no-fault (₹5L), Section 166 full claims."),
    ("file-text", "Hindi crash-claim guides", "4-step claim process, free DLSA legal aid, NALSA 15100, Cashless Treatment Scheme 2025 (₹1.5L / 7 days) — distributed at hospitals and police stations."),
    ("heart-pulse", "Pre-Hospital Care Primer", "Golden Hour, ERSS-112, ambulance benchmarks — India's emergency-response gaps mapped against global standards."),
    ("presentation", "Road Safety Dialogue Series", "1,000+ participants across sessions with police, transport departments and professionals."),
]
ey2 = Inches(3.85)
for icn, t1, t2 in edu:
    circle(s, M_L, ey2, Inches(0.4), BRAND_LITE)
    icon(s, icn, M_L+Inches(0.085), ey2+Inches(0.085), Inches(0.23), BLUE_HEX)
    text(s, M_L+Inches(0.6), ey2-Inches(0.02), Inches(7.2), Inches(0.28), t1, font=HEAD, size=10.5, bold=True, color=DARK)
    text(s, M_L+Inches(0.6), ey2+Inches(0.26), Inches(7.2), Inches(0.5), t2, font=BODY, size=8.8, color=MUTED, ls=1.22)
    ey2 += Inches(0.78)
try:
    st_ = os.path.join(V3, "new", "rkf_p4.png")
    ar = pic_ar(st_); nw_ = Inches(3.55)
    rect(s, Inches(9.06), Inches(2.51), nw_+Inches(0.08), Inches(3.55/ar)+Inches(0.08), WHITE, line=BORDER)
    pic(s, st_, Inches(9.1), Inches(2.55), w=nw_)
    text(s, Inches(9.1), Inches(2.55)+Inches(3.55/ar)+Inches(0.1), nw_, Inches(0.4),
         "On stage at the National Road Safety Implementation Forum, IIT Delhi — April 2026.",
         font=BODY, size=8.3, color=MUTED, italic=True, ls=1.2)
    nm1 = os.path.join(V3, "extracted", "nextmile_p1.png")
    ar2 = pic_ar(nm1); nh2 = Inches(2.2)
    rect(s, Inches(9.06), Inches(4.66), Inches(2.2*ar2)+Inches(0.08), nh2+Inches(0.08), WHITE, line=BORDER)
    pic(s, nm1, Inches(9.1), Inches(4.7), h=nh2)
    text(s, Inches(9.1), Inches(6.95)-Inches(0.02), Inches(3.2), Inches(0.25), "The NextMile newsletter.",
         font=BODY, size=8.3, color=MUTED, italic=True)
except Exception as e: print("a6 visuals", e)
footer(s, 24, TOTAL, "APPENDIX · NEXTMILE & EDUCATION")

# ============================================================ 25 A7 PRESS & CONTACT
s = new_slide(BRAND_LITE)
ny = std_header(s, "APPENDIX A7 · PRESS & CONTACT",
                "Where you may have read about us.")
press = [
    ("'Justice Unserved' coverage", "Deccan Herald · Economic Times · Fortune India · IndiaSpend · Moneycontrol · Scroll.in · The Wire"),
    ("MS Dhoni announcement (Apr 2026)", "Business Standard · The Tribune · The Wire (PTI) · Team-BHP · MediaBrief · Adgully"),
    ("Launch coverage (Jun 2025)", "TheCSRUniverse · Team-BHP · Adgully · MediaInfoline — 'Cars24 launches Crashfree India to eliminate road fatalities by 2040'"),
    ("Team bylines & citations", "Scroll.in op-ed on underage-driving law (Shubham Kumar) · The Wire / IndiaSpend on gig-rider crash data (Aastha Shreeharsh)"),
]
py4 = Inches(2.4)
for t1, t2 in press:
    rect(s, M_L, py4, Inches(9.0), Inches(0.86), WHITE, line=BORDER, rounded=True)
    text(s, M_L+Inches(0.25), py4+Inches(0.12), Inches(3.3), Inches(0.5), t1, font=HEAD, size=10, bold=True, color=DARK, ls=1.15)
    text(s, M_L+Inches(3.7), py4+Inches(0.12), Inches(5.1), Inches(0.6), t2, font=BODY, size=8.8, color=MUTED, ls=1.25)
    py4 += Inches(0.98)
try:
    dh = os.path.join(V3, "new", "comp_image3.png")
    ardh = pic_ar(dh); dhw = Inches(1.9); dhh = Inches(1.9/ardh)
    rect(s, Inches(9.9), Inches(2.4), dhw+Inches(0.08), dhh+Inches(0.08), WHITE, line=BORDER)
    pic(s, dh, Inches(9.94), Inches(2.44), w=dhw)
    isc = os.path.join(V3, "new", "comp_image5.jpeg")
    aris = pic_ar(isc)
    iy0 = Inches(2.44) + dhh + Inches(0.22)
    ish = Inches(6.05) - iy0
    rect(s, Inches(9.9), iy0-Inches(0.04), Inches(0.08)+ish*aris, ish+Inches(0.08), WHITE, line=BORDER)
    pic(s, isc, Inches(9.94), iy0, h=ish)
    text(s, Inches(9.9), Inches(6.12), Inches(2.7), Inches(0.3), "IndiaSpend citing CFI research, 2026.",
         font=BODY, size=7.8, color=MUTED, italic=True)
except Exception as e: print("press visuals", e)
rect(s, M_L, Inches(6.35), Inches(11.9), Inches(0.55), BRAND, rounded=True)
text(s, M_L+Inches(0.3), Inches(6.35), Inches(11.3), Inches(0.55),
     "crashfreeindia.org  ·  helpdesk@crashfreeindia.org  ·  WhatsApp +91 78380 59367  ·  Live dashboard: crashfreeindia.org/rakshak/dashboard",
     font=HEAD, size=11, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
footer(s, 25, TOTAL, "APPENDIX · PRESS & CONTACT")

OUT = os.path.join(BUILD_DIR, "CFI_Overview.pptx")
save(OUT)

# CFI × Google Maps intro deck — 10 slides, NRSB v2 design language (white paper, ink titles,
# sparse blue, tinted icon rows, photo-forward). Meeting: 3 Aug 2026, 4pm IST.
import os
from nrsb2_style import *
from pptx.util import Inches, Pt, Emu
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

I = Inches
V3D = os.path.join(SP, "assets/v3")          # iv_* intervention photos live here directly
TOTAL = 10

def gfooter(s, idx):
    hline(s, ML, I(7.06), CW)
    text(s, ML, I(7.14), I(8), I(0.25),
         "Crashfree India  ·  Introduction for the Google Maps team", size=8.5, color=MUT, ls=1.0)
    text(s, SW-MR-I(1.2), I(7.14), I(1.2), I(0.25), f"{idx:02d} / {TOTAL:02d}",
         size=8.5, color=MUT, align=PP_ALIGN.RIGHT, ls=1.0)

def datechip(s):
    text(s, SW-MR-I(3.4), I(0.30), I(3.4), I(0.24), "GOOGLE MAPS  ×  CRASHFREE INDIA  ·  AUG 2026",
         font=HEAD, size=8, bold=True, color=MUT, tracking=1.6, align=PP_ALIGN.RIGHT)

# ---------------------------------------------------------------- S1 COVER
def s1_cover():
    s = slide()
    s.shapes.add_picture(LOGO_BLUE, ML, I(0.5), width=I(1.85))
    text(s, SW-MR-I(3.5), I(0.55), I(3.5), I(0.3), "3 AUGUST 2026  ·  PREPARED FOR GOOGLE MAPS",
         font=HEAD, size=9, bold=True, color=MUT, tracking=1.6, align=PP_ALIGN.RIGHT)
    text(s, ML, I(1.66), I(8.3), I(0.3), "AN INTRODUCTION, AHEAD OF THE ROADS MANAGEMENT INSIGHTS SHOWCASE",
         font=HEAD, size=10, bold=True, color=BRAND, tracking=1.8)
    text(s, ML, I(2.06), I(8.3), I(0.85), "Crashfree India", font=HEAD, size=46, bold=True, color=INK, ls=1.0)
    text(s, ML, I(3.0), I(8.4), I(0.9),
         "We fix dangerous roads with students, experts\nand the authorities. Your data can tell us where.",
         font=HEAD, size=16.5, bold=True, color=BRAND, ls=1.25)
    chips_ = [
        ("map-pin",   "18 cities  ·  31 sites audited  ·  25+ approvals in writing"),
        ("school",    "Next: India's first School Safety Index — 2,000 school zones"),
        ("landmark",  "Inside district road-safety committees in Gurugram & Jaipur"),
        ("handshake", "Backed by a 3-year, US$3M commitment from Cars24"),
    ]
    y = I(4.42)
    for i, (ic, t) in enumerate(chips_):
        icon_disc(s, ic, ML, y+i*I(0.56), I(0.4), BR_T, "#4A35FF")
        text(s, ML+I(0.56), y+i*I(0.56)+I(0.06), I(7.9), I(0.4), t,
             font=HEAD, size=11.5, bold=True, color=INK, ls=1.1)
    text(s, ML, I(6.92), I(8.4), I(0.3),
         "For Ravi Bhaskaran & the Google Maps team  ·  arranged with Lepton Software",
         size=9.5, color=MUT)
    text(s, SW-MR-I(2.6), I(6.92), I(2.6), I(0.3), "crashfreeindia.org",
         font=HEAD, size=9.5, bold=True, color=BRAND, align=PP_ALIGN.RIGHT)
    px, pyy, pw, ph_ = I(9.1), I(1.15), I(3.6), I(5.15)
    photo(s, a5("ph_school_kids.jpg"), px, pyy, pw, ph_, fill=True, anchor=0.30)
    rect(s, px, pyy+ph_-I(0.56), pw, I(0.56), fill=BRAND)
    text(s, px, pyy+ph_-I(0.52), pw, I(0.5), "SCHOOL ROAD-SAFETY PROGRAMME\nCRASHFREE INDIA, 2026",
         font=HEAD, size=8.5, bold=True, color=PAPER, align=PP_ALIGN.CENTER, ls=1.15, tracking=1.0)
    return s

# ---------------------------------------------------------------- S2 ABOUT
def s2_about():
    s = slide(); datechip(s)
    y = header(s, "01 · WHO WE ARE",
               [("A young nonprofit that builds ", False), ("capacity for road safety work", True)],
               lead="Registered as the Vision Zero Trust · co-founded by Cars24 and the Indian Road Safety Council, June 2025.")
    rows = [
        ("landmark",   "With authorities",  "We work alongside PWDs, police and district administrations — never around them."),
        ("bar-chart-3","Evidence first",    "Every audit anchored to IRC codes; every claim to published data."),
        ("graduation-cap","Students + experts","Trained student teams do the ground work, senior experts verify it."),
        ("globe",      "Public goods",      "Everything we build is published free for any authority to use."),
    ]
    ry = y + I(0.10)
    for i, (ic, t, d) in enumerate(rows):
        irow(s, ML, ry+i*I(0.72), I(7.3), ic, t, d, BR_T, "#4A35FF", tsize=12.5, dsize=10.5)
    sy = I(5.62)
    stats = [("18", "cities with active\nCFI work"), ("20", "institutions — incl.\n9 IITs — engaged"),
             ("75+", "road-engineering\ninterns trained"), ("US$3M", "Cars24 commitment\nover three years")]
    swd = I(1.78)
    for i, (v, l) in enumerate(stats):
        stat(s, ML+i*(swd+I(0.18)), sy, swd, v, l, vsize=23, card=True, h=I(1.18))
    px, pyy, pw = I(8.65), I(1.62), I(4.05)
    photo_fit(s, a5("cfi_map_dots.png"), px, pyy, pw, I(3.1), border=False,
              caption="CFI footprint — 18 cities across India", align='center')
    photo(s, a5("ph_meeting_official.jpg"), px, pyy+I(3.55), pw, I(1.55), fill=True, anchor=0.3)
    gfooter(s, 2); return s

# ---------------------------------------------------------------- S3 PORTFOLIO
def s3_portfolio():
    s = slide(); datechip(s)
    y = header(s, "02 · WHAT WE HAVE BUILT",
               [("Six public-facing programmes, ", False), ("all running today", True)],
               lead="One line on each — then this deck goes deep on the two where Google Maps data changes the game.")
    tiles = [
        ("implementation_work.jpg", "Project Rakshak", "Student-audited, expert-verified road fixes — walked through authorities until built.", "25+ approvals in writing", True),
        ("ph_school_activity.jpg",  "School Safety Index", "India's first public index of school-zone road safety — in design, launching next.", "2,000 school zones planned", True),
        ("satark_billboard.jpg",    "SATARK enforcement tech", "Camera + billboard tech that helps police target repeat violators fairly.", "3,00,000+ vehicles scanned", False),
        ("ph_helpdesk_desk.jpg",    "Victim support suite", "Aasha 24/7 chatbot, compensation calculator, hospital legal helpdesks.", "100+ victims in first 4 days", False),
        ("sctracker.png",           "Open data public goods", "SC litigation tracker, defect repository, Parliament tracker, crash dashboards.", "146 districts · 13 languages", False),
        ("ph_ideathon_group.jpg",   "Youth & public campaigns", "NextMile ideathon, dialogue series, MS Dhoni as Goodwill Ambassador.", "2,000+ young participants", False),
    ]
    tw, th = I(3.94), I(2.26); gx, gy = I(0.145), I(0.22)
    ty = y + I(0.06)
    for i, (img, t, d, n, hot) in enumerate(tiles):
        r, c = divmod(i, 3)
        x = ML + c*(tw+gx); yy = ty + r*(th+gy)
        rect(s, x, yy, tw, th, fill=MIST if not hot else BR_T, rounded=True, radius=0.06)
        photo(s, a5(img), x+I(0.14), yy+I(0.14), tw-I(0.28), I(0.98), fill=True, anchor=0.3)
        text(s, x+I(0.14), yy+I(1.18), tw-I(0.28), I(0.3), t, font=HEAD, size=12, bold=True,
             color=BRAND if hot else INK, ls=1.05)
        text(s, x+I(0.14), yy+I(1.45), tw-I(0.28), I(0.52), d, size=9, color=MUT, ls=1.16)
        text(s, x+I(0.14), yy+I(1.96), tw-I(0.28), I(0.24), n, font=HEAD, size=9, bold=True, color=INK, ls=1.0)
    gfooter(s, 3); return s

# ---------------------------------------------------------------- S4 RAKSHAK EXPLAINER
def s4_rakshak():
    s = slide(); datechip(s)
    y = header(s, "03 · PROJECT RAKSHAK",
               [("Trained students audit dangerous roads — and we walk each fix ", False), ("through the authority until it is built", True)])
    cards = [
        ("users",        "Students audit",    "31 student audit teams from 20 institutions — including 9 IITs — survey sites on IRC codes and MoRTH checklists."),
        ("badge-check",  "Experts verify",    "Every audit reviewed by senior engineers, guided by Prof. Geetam Tiwari (IIT Delhi, IRC H-7)."),
        ("hard-hat",     "Authorities build", "Recommendations handed to the road-owning authority; CFI tracks every site from submission to completion."),
    ]
    cw_, ch_ = I(3.94), I(1.72); ty = y + I(0.08)
    for i, (ic, t, d) in enumerate(cards):
        x = ML + i*(cw_+I(0.145))
        rect(s, x, ty, cw_, ch_, fill=MIST, rounded=True, radius=0.08)
        icon_disc(s, ic, x+I(0.2), ty+I(0.2), I(0.44), BR_T, "#4A35FF")
        text(s, x+I(0.78), ty+I(0.24), cw_-I(0.95), I(0.3), t, font=HEAD, size=13, bold=True, color=INK)
        text(s, x+I(0.2), ty+I(0.72), cw_-I(0.4), I(0.9), d, size=9.8, color=MUT, ls=1.24)
    fy = ty + ch_ + I(0.34)
    text(s, ML, fy, I(6), I(0.26), "YEAR-ONE FUNNEL", font=HEAD, size=9, bold=True, color=BRAND, tracking=2.0)
    fun = [("120+", "sites screened"), ("31", "audited — incl. 11\nofficial blackspots"),
           ("25+", "approvals from\nauthorities, in writing"), ("15", "implementations\nunderway")]
    fw = I(1.86); fx = ML
    for i, (v, l) in enumerate(fun):
        stat(s, fx, fy+I(0.32), fw, v, l, vsize=25, card=True, h=I(1.28))
        if i < 3:
            icon(s, "arrow-right", fx+fw+I(0.04), fy+I(0.78), I(0.26), "#6E7180")
        fx += fw + I(0.34)
    text(s, ML, fy+I(1.78), I(8.5), I(0.55),
         "Global evidence: low-cost engineering fixes of this kind\ncut crashes 20–50% at treated sites (iRAP / World Bank).",
         size=9.5, color=MUT, italic=True, ls=1.3)
    px = ML + I(8.75)
    photo(s, a5("guntur_junction.jpg"), px, fy+I(0.02), SW-MR-px, I(2.42), fill=True, anchor=0.45,
          caption="Guntur junction — audited, approved, redesigned")
    gfooter(s, 4); return s

# ---------------------------------------------------------------- S5 RAKSHAK PROOF + GAP
def s5_proof():
    s = slide(); datechip(s)
    y = header(s, "03 · PROJECT RAKSHAK",
               [("Authorities are building our fixes. ", False), ("What we cannot yet measure is the after.", True)])
    text(s, ML, y+I(0.02), I(6), I(0.26), "APPROVALS IN WRITING, FROM", font=HEAD, size=9, bold=True, color=BRAND, tracking=2.0)
    auth = ["PWD Kerala", "PWD Uttar Pradesh", "PWD Punjab", "CPWD", "R&B Andhra Pradesh",
            "GCC Chennai", "ADDA Durgapur", "Addl. Collector, Indore"]
    ax, ay = ML, y+I(0.34)
    for i, a in enumerate(auth):
        r, c = divmod(i, 2)
        chip(s, ax+c*I(2.62), ay+r*I(0.5), I(2.5), I(0.4), a, fill=MIST, size=9.5)
    iy = ay + I(2.16)
    ivs = [("iv_indore_footpath.png", "Footpaths — Indore"),
           ("iv_guntur_markings.png", "Markings — Guntur"),
           ("iv_durgapur_parking.png", "Parking bays — Durgapur")]
    iw = I(1.66)
    for i, (img, cap) in enumerate(ivs):
        photo(s, os.path.join(V3D, img), ML+i*(iw+I(0.12)), iy, iw, I(1.28), fill=True, anchor=0.4)
    text(s, ML, iy+I(1.34), I(5.3), I(0.24), "Built interventions — footpaths, markings, parking, signage, drainage",
         size=8.5, color=MUT)
    px, pw = I(5.95), I(4.1)
    photo(s, a5("rakshak_dashboard_full.png"), px, y+I(0.04), pw, I(4.62), fill=True, anchor=0.0,
          caption="Every site tracked in public — submission to completion")
    bx = px+pw+I(0.25); bw = SW-MR-bx
    rect(s, bx, y+I(0.04), bw, I(4.92), fill=BR_T, rounded=True, radius=0.08)
    icon_disc(s, "search", bx+I(0.22), y+I(0.28), I(0.44), PAPER, "#4A35FF")
    text(s, bx+I(0.22), y+I(0.9), bw-I(0.44), I(0.9), "The missing layer:\nmeasurement", font=HEAD, size=14.5, bold=True, color=INK, ls=1.15)
    text(s, bx+I(0.22), y+I(1.78), bw-I(0.44), I(3.0),
         "We know what was built. We cannot yet see, at network scale, what changed —\n\nvehicle speeds before and after each fix, exposure around each site, risk on the corridors we haven't audited yet.\n\nThat is exactly the data Roads Management Insights holds.",
         size=10.2, color=INK, ls=1.3)
    gfooter(s, 5); return s

# ---------------------------------------------------------------- S6 SCHOOL SAFETY INDEX
def s6_ssi():
    s = slide(); datechip(s)
    y = header(s, "04 · SCHOOL SAFETY INDEX",
               [("Next build: ", False), ("India's first School Safety Index", True)],
               lead="In design now — a public, district-wise score of how safe the road outside every school actually is.")
    rows = [
        ("clipboard-check", "A standard rubric",   "44 scored checks across 13 sections, aligned to IRC:SP:32-2023 — the same standard authorities use."),
        ("users",           "Scaled by students",  "College audit teams and trained Zone Captains — the Rakshak model, pointed at school zones."),
        ("map-pin",         "2,000 school zones",  "Across 15+ cities in the first wave; every score public, every gap actionable by the district."),
        ("trending-up",     "Built to rank",       "Districts compete to climb; parents and authorities see the same number."),
    ]
    ry = y + I(0.08)
    for i, (ic, t, d) in enumerate(rows):
        irow(s, ML, ry+i*I(0.70), I(7.35), ic, t, d, BR_T, "#4A35FF", tsize=12.5, dsize=10.2)
    by = ry + 4*I(0.70) + I(0.14)
    rect(s, ML, by, I(7.35), I(1.06), fill=AM_T, rounded=True, radius=0.10)
    icon_disc(s, "database", ML+I(0.18), by+I(0.16), I(0.4), PAPER, "#E58900")
    text(s, ML+I(0.72), by+I(0.14), I(6.5), I(0.85),
         "The hard part is not the checklist — it is speed and exposure data around 2,000 schools.\nCollecting it manually is slow and patchy. Maps data makes it systematic.",
         size=10.2, color=INK, ls=1.3, bold=False)
    px, pw = I(8.75), I(3.95)
    photo(s, a5("ph_street_outreach.jpg"), px, y+I(0.06), pw, I(2.5), fill=True, anchor=0.35)
    photo(s, a5("ph_school_activity.jpg"), px, y+I(2.7), pw, I(2.2), fill=True, anchor=0.3,
          caption="CFI school programmes — Road Safety Month 2026")
    gfooter(s, 6); return s

# ---------------------------------------------------------------- S7 WHERE GOOGLE FITS
def s7_google():
    s = slide(); datechip(s)
    y = header(s, "05 · WHERE GOOGLE MAPS FITS",
               [("Four places your data ", False), ("plugs straight into our work", True)],
               lead="Roads Management Insights is live in India. Here is what it unlocks, programme by programme.")
    rows = [
        ("crosshair",  "Prioritise",  "RMI segment speeds & risk insights → choose the next 100 Rakshak sites by evidence, not anecdote.", "PROJECT RAKSHAK"),
        ("school",     "Score",       "Speed and exposure layers around schools → the data backbone of the School Safety Index, 2,000 zones at once.", "SCHOOL SAFETY INDEX"),
        ("line-chart", "Prove",       "Before-and-after speeds at treated sites → India's first measured evidence base for low-cost road fixes.", "IMPACT EVALUATION"),
        ("globe",      "Publish",     "Verified school zones & audit findings back to Google → ground truth for accident-prone alerts, beyond 4 cities.", "OPEN DATA — BOTH WAYS"),
    ]
    ry = y + I(0.10); rh = I(1.02)
    for i, (ic, t, d, tag) in enumerate(rows):
        yy = ry + i*rh
        rect(s, ML, yy, CW, rh-I(0.14), fill=MIST if i % 2 == 0 else PAPER,
             line=None if i % 2 == 0 else LINE, rounded=True, radius=0.10)
        icon_disc(s, ic, ML+I(0.18), yy+I(0.20), I(0.48), BR_T, "#4A35FF")
        text(s, ML+I(0.84), yy+I(0.14), I(1.7), I(0.4), t, font=HEAD, size=14.5, bold=True, color=BRAND)
        text(s, ML+I(0.84), yy+I(0.50), I(8.2), I(0.4), d, size=10.4, color=INK, ls=1.2)
        chip(s, SW-MR-I(2.55), yy+I(0.26), I(2.4), I(0.36), tag, fill=BR_T, color=BRAND, size=8)
    ny = ry + 4*rh + I(0.04)
    text(s, ML, ny, CW, I(0.3),
         "Precedent: Google.org already funds iRAP's Star Rating for Schools with US$2M — deployed in Vietnam. India has no lead partner yet.",
         size=10, color=MUT, italic=True)
    gfooter(s, 7); return s

# ---------------------------------------------------------------- S8 WHY CFI
def s8_why():
    s = slide(); datechip(s)
    y = header(s, "06 · WHY CRASHFREE INDIA",
               [("RMI serves governments. ", False), ("We already sit inside the government machinery.", True)])
    cards = [
        ("landmark", "District machinery", "Formal member of 4 District Road Safety Committees — Gurugram, SW Delhi, NW Delhi, Jaipur. MoUs with Jaipur Traffic Police and Gurugram Police.", GR_T, "#0A9955"),
        ("file-text", "Authority relationships", "Written approvals from 8 road-owning authorities across 6 states — we know how files move, and how to move them.", BR_T, "#4A35FF"),
        ("graduation-cap", "Academic bench", "Prof. Geetam Tiwari (IRC H-7) and experts from 9 IITs verify our work — credibility your government clients recognise.", BR_T, "#4A35FF"),
        ("handshake", "Corporate stability", "Cars24's 3-year US$3M commitment and MS Dhoni as Goodwill Ambassador — a partner built to last, not a pilot NGO.", GR_T, "#0A9955"),
    ]
    cw_, ch_ = I(6.0), I(1.6); ty = y + I(0.1)
    for i, (ic, t, d, tint, col) in enumerate(cards):
        r, c = divmod(i, 2)
        x = ML + c*(cw_+I(0.145)); yy = ty + r*(ch_+I(0.18))
        rect(s, x, yy, cw_, ch_, fill=MIST, rounded=True, radius=0.08)
        icon_disc(s, ic, x+I(0.2), yy+I(0.2), I(0.44), tint, col)
        text(s, x+I(0.8), yy+I(0.24), cw_-I(1.0), I(0.3), t, font=HEAD, size=12.5, bold=True, color=INK)
        text(s, x+I(0.2), yy+I(0.66), cw_-I(0.4), I(0.9), d, size=9.8, color=MUT, ls=1.24)
    by = ty + 2*ch_ + I(0.18) + I(0.16)
    rect(s, ML, by, CW, I(0.78), fill=BR_T, rounded=True, radius=0.12)
    text(s, ML, by, CW, I(0.78),
         [("Your Nov 2025 safety launch covers Gurugram and Jaipur.  ", {'color': INK, 'bold': True, 'size': 12}),
          ("Those are the two districts where we hold committee seats and police MoUs.", {'color': BRAND, 'bold': True, 'size': 12})],
         font=HEAD, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, ls=1.2)
    gfooter(s, 8); return s

# ---------------------------------------------------------------- S9 WORKING TOGETHER
def s9_models():
    s = slide(); datechip(s)
    y = header(s, "07 · WORKING TOGETHER",
               [("Three concrete ways to start — ", False), ("smallest first", True)])
    cards = [
        ("1", "map-pin", "Pilot where we overlap", "Gurugram or Jaipur: RMI data + Rakshak audits + our DRSC seat. One city, 90 days, results presented to the district committee.", "START: 90 DAYS"),
        ("2", "school", "School Safety Index partnership", "Co-design the SSI data layer — RMI speeds & exposure as scoring inputs for the first 2,000 school zones. India's answer to Star Rating for Schools.", "START: WITH SSI WAVE 1"),
        ("3", "line-chart", "Joint impact study", "Before-and-after evaluation of implemented Rakshak fixes using RMI — published openly, first-of-its-kind evidence for India.", "START: 15 LIVE SITES"),
    ]
    cw_, ch_ = I(3.94), I(2.9); ty = y + I(0.1)
    for i, (n, ic, t, d, tag) in enumerate(cards):
        x = ML + i*(cw_+I(0.145))
        rect(s, x, ty, cw_, ch_, fill=MIST, rounded=True, radius=0.07)
        rect(s, x, ty, cw_, I(0.07), fill=BRAND)
        num_disc(s, x+I(0.2), ty+I(0.24), I(0.46), n)
        icon_disc(s, ic, x+cw_-I(0.68), ty+I(0.24), I(0.46), BR_T, "#4A35FF")
        text(s, x+I(0.2), ty+I(0.86), cw_-I(0.4), I(0.62), t, font=HEAD, size=13.5, bold=True, color=INK, ls=1.12)
        text(s, x+I(0.2), ty+I(1.5), cw_-I(0.4), I(1.0), d, size=9.8, color=MUT, ls=1.26)
        chip(s, x+I(0.2), ty+ch_-I(0.5), I(2.2), I(0.34), tag, fill=BR_T, color=BRAND, size=8)
    by = ty + ch_ + I(0.22)
    text(s, ML, by, I(5.9), I(0.26), "WE BRING", font=HEAD, size=9, bold=True, color=GREEN, tracking=2.0)
    text(s, ML, by+I(0.28), I(5.9), I(0.6),
         "Ground teams in 18 cities · government access & committee seats · IIT-verified method · open publication",
         size=10, color=INK, ls=1.25)
    xr = ML+I(6.2)
    text(s, xr, by, I(5.6), I(0.26), "WE ASK", font=HEAD, size=9, bold=True, color=BRAND, tracking=2.0)
    text(s, xr, by+I(0.28), I(5.6), I(0.6),
         "RMI data access for one pilot geography · a working session with the Lepton + Maps team to scope it",
         size=10, color=INK, ls=1.25)
    gfooter(s, 9); return s

# ---------------------------------------------------------------- S10 CLOSE
def s10_close():
    s = slide(bg=BRAND)
    s.shapes.add_picture(LOGO_WHITE, ML, I(0.55), width=I(1.85))
    text(s, ML, I(2.3), I(11.9), I(1.7),
         "Your maps see every road in India.\nTogether, they can start fixing them.",
         font=HEAD, size=33, bold=True, color=PAPER, ls=1.2)
    text(s, ML, I(4.05), I(11), I(0.5),
         "Thank you — we look forward to the Roads Management Insights showcase.",
         size=13, color=LAVW, ls=1.3)
    hline(s, ML, I(5.0), I(6.5), color=LAVW, wt=1.0)
    contacts = [
        ("Akhtar Hussain",  "Mission Lead", "akhtar@crashfreeindia.org"),
        ("Deepanshu Gupta", "Trustee",      "deepanshu@crashfreeindia.org"),
        ("Gajendra Jangid", "Trustee",      "gajendra@crashfreeindia.org"),
    ]
    for i, (n, r, e) in enumerate(contacts):
        x = ML + i*I(4.0)
        text(s, x, I(5.3), I(3.8), I(0.3), n, font=HEAD, size=12.5, bold=True, color=PAPER)
        text(s, x, I(5.6), I(3.8), I(0.28), r, size=9.5, color=LAVW)
        text(s, x, I(5.86), I(3.8), I(0.28), e, size=9.5, color=LAVW)
    text(s, ML, I(6.9), I(8), I(0.3), "crashfreeindia.org", font=HEAD, size=10, bold=True, color=PAPER)
    text(s, SW-MR-I(1.2), I(6.9), I(1.2), I(0.25), f"{TOTAL:02d} / {TOTAL:02d}",
         size=8.5, color=LAVW, align=PP_ALIGN.RIGHT)
    return s

# ---------------------------------------------------------------- BUILD
new_deck()
s1_cover(); s2_about(); s3_portfolio(); s4_rakshak(); s5_proof()
s6_ssi(); s7_google(); s8_why(); s9_models(); s10_close()
save("CFI_Google-Maps-Intro_Partnership_v1_2026-08-03.pptx")

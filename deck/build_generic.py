# Crashfree India — generic shareable overview deck, 15 slides.
# Same format/content as the mentor briefing deck, minus the personal note and
# the mentor-specific 'seek your guidance' framing; relabelled for general use.
# All 'Rajasthan / Department of Transport' mentions stripped.
import os
import build_mentor as M
import build_nrsb3 as B
import build_overview as OV
import nrsb2_style as ST
from build_overview import rakshak_ov, research_ov, close_ov
from nrsb2_style import *
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN

I = Inches
TOTAL = 15

def g_footer(s, wg, idx, total):
    hline(s, ML, I(7.06), CW)
    text(s, ML, I(7.14), I(9), I(0.25), "Crashfree India  ·  Organisation overview  ·  2026", size=8.5, color=MUT, ls=1.0)
    text(s, SW-MR-I(1.2), I(7.14), I(1.2), I(0.25), f"{idx:02d} / {total:02d}", size=8.5, color=MUT, align=PP_ALIGN.RIGHT, ls=1.0)

# route every footer (shared B.* slides, overview OV.* slides, mentor M.* slides) through the generic one
B.footer = g_footer
OV._footer = g_footer
OV.TOTAL = TOTAL
M.m_footer = g_footer
M.TOTAL = TOTAL

# ---------------------------------------------------------------- 01 COVER (generic label)
def cover_g():
    s = slide()
    s.shapes.add_picture(LOGO_BLUE, ML, I(0.5), width=I(1.85))
    text(s, SW-MR-I(3.5), I(0.55), I(3.5), I(0.3), "ORGANISATION OVERVIEW  ·  2026", font=HEAD, size=9, bold=True, color=MUT, tracking=1.8, align=PP_ALIGN.RIGHT)
    text(s, ML, I(1.66), I(8.2), I(0.3), "A ROAD SAFETY NONPROFIT  ·  NEW DELHI", font=HEAD, size=10.5, bold=True, color=BRAND, tracking=2.2)
    text(s, ML, I(2.08), I(8.3), I(0.85), "Crashfree India", font=HEAD, size=46, bold=True, color=INK, ls=1.0)
    text(s, ML, I(3.04), I(8.3), I(0.85), "Technology and governance for road safety,\nbuilt into an institution designed to make itself redundant", font=HEAD, size=16, bold=True, color=BRAND, ls=1.25)
    rows = [("cpu", "Digital public goods: enforcement AI, open data platforms, victim tools on WhatsApp"),
            ("landmark", "Governance from inside: 4 district committee seats, police MoUs, 25+ written approvals"),
            ("building-2", "Standards, manuals and dashboards built so the system can run this work without us")]
    y = I(4.52)
    for i, (ic, t) in enumerate(rows):
        icon_disc(s, ic, ML, y+i*I(0.60), I(0.4), BR_T, "#4A35FF")
        text(s, ML+I(0.56), y+i*I(0.60)+I(0.05), I(7.85), I(0.4), t, font=HEAD, size=11.5, bold=True, color=INK, ls=1.1)
    text(s, ML, I(6.42), I(8.4), I(0.3),
         [("FOCUS AREAS   ", {'bold': True, 'color': BRAND, 'tracking': 1.6, 'size': 9}),
          ("Road infrastructure · Enforcement · Crash compensation · Gig rider safety · School zones · Open data", {'color': INK, 'size': 9.5})],
         font=HEAD, bold=True)
    text(s, ML, I(6.92), I(8.6), I(0.3), "Registered as the Vision Zero Trust · A Cars24 commitment · Co-founded with the Indian Road Safety Council", size=9.5, color=MUT)
    text(s, SW-MR-I(2.6), I(6.92), I(2.6), I(0.3), "crashfreeindia.org", font=HEAD, size=9.5, bold=True, color=BRAND, align=PP_ALIGN.RIGHT)
    px, pyy, pw, ph_ = I(9.1), I(1.15), I(3.6), I(4.9)
    photo(s, a5("ph_dhoni_white.jpg"), px, pyy, pw, ph_, fill=True, anchor=0.12)
    rect(s, px, pyy+ph_-I(0.56), pw, I(0.56), fill=BRAND)
    text(s, px, pyy+ph_-I(0.52), pw, I(0.5), "MS DHONI · GOODWILL AMBASSADOR,\nCRASHFREE INDIA", font=HEAD, size=8.5, bold=True, color=PAPER, align=PP_ALIGN.CENTER, ls=1.15, tracking=1.0)
    return s

# ---------------------------------------------------------------- 14 THE YEAR AHEAD + HOW TO WORK WITH US
def year_ahead(idx):
    s = slide()
    header(s, "04 · The year ahead",
           [("Where we are going, and ", False), ("how to work with us", True)],
           lead="Year 2 moves from programmes to institutions. These are the goals, and the concrete ways to get involved.",
           sect=(4, "THE YEAR AHEAD"))
    colw = I(5.85)
    text(s, ML, I(2.02), colw, I(0.26), "THE YEAR AHEAD", font=HEAD, size=9, bold=True, color=MUT, tracking=1.8)
    rows_l = [
        ("hard-hat", "Project Rakshak", "Audits running inside institutions, with 75+ implementations initiated and every one tracked publicly."),
        ("scale", "Crash compensation", "Claim pipeline fixed in two districts, mapped in eight, with a playbook states can adopt."),
        ("cpu", "SATARK", "From 3 cities toward 30, as shared public infrastructure for traffic police."),
        ("rocket", "Two exploratory bets", "School Safety Index and gig rider safety, each scaled only if a small, honest pilot earns it."),
        ("building-2", "Institutions that outlive us", "An expert consortium, an audit manual and a publishing cadence that outlive any single cohort."),
    ]
    y = I(2.38)
    for i, (ic, t, d) in enumerate(rows_l):
        irow(s, ML, y+i*I(0.86), colw, ic, t, d, BR_T, "#4A35FF")
    x2 = ML+colw+I(0.42)
    w2 = SW-MR-x2
    text(s, x2, I(2.02), w2, I(0.26), "HOW TO WORK WITH US", font=HEAD, size=9, bold=True, color=MUT, tracking=1.8)
    rows_r = [
        ("search-check", "Partner on audits", "Bring Project Rakshak to your city or campus, or co-audit a corridor you care about."),
        ("database", "Adopt our open data", "Four public platforms, free for any authority, researcher or newsroom to build on."),
        ("cpu", "Bring SATARK to your city", "Enforcement intelligence for traffic police, proven across three cities."),
        ("handshake", "Back a programme", "Fund a focus area, or join the expert bench that reviews the work."),
        ("mail", "Talk to us", "akhtar@crashfreeindia.org  ·  crashfreeindia.org"),
    ]
    for i, (ic, t, d) in enumerate(rows_r):
        irow(s, x2, y+i*I(0.86), w2, ic, t, d, GR_T, "#0A9955")
    g_footer(s, None, idx, TOTAL)
    return s

# ---------------------------------------------------------------- strip Rajasthan / transport-dept mentions
def scrub_rajasthan(prs):
    repl = {
        "Rajasthan portal · 4 DRSC seats": "District pilots · 4 DRSC seats",
        "Bihar, UP and Rajasthan districts": "Bihar, UP and other districts",
        "the Government of Rajasthan": "senior government",
        "Rajasthan": "our districts",  # catch-all fallback for any stray run
    }
    n = 0
    for sl in prs.slides:
        for sh in sl.shapes:
            if not sh.has_text_frame:
                continue
            for p in sh.text_frame.paragraphs:
                for r in p.runs:
                    if r.text and "Rajasthan" in r.text:
                        t = r.text
                        for a, b in repl.items():
                            t = t.replace(a, b)
                        if t != r.text:
                            r.text = t; n += 1
    return n

if __name__ == "__main__":
    new_deck()
    cover_g()                        # 01
    M.about_m(2)                     # 02
    M.portfolio_m(3)                 # 03
    rakshak_ov(4)                    # 04
    B.satark(5, TOTAL, None)         # 05
    B.opendata(6, TOTAL, None)       # 06
    B.victim_suite(7, TOTAL, None)   # 07
    research_ov(8)                   # 08
    M.gig_m(9)                       # 09
    M.ssi(10)                        # 10
    M.media(11)                      # 11
    B.youth(12, TOTAL, None)         # 12
    B.team(13, TOTAL, None)          # 13
    year_ahead(14)                   # 14
    close_ov()                       # 15
    n = scrub_rajasthan(ST.prs)
    print("Rajasthan runs scrubbed:", n)
    save(os.path.join(BUILD, "CFI_Overview_Generic_v2.pptx"))

# Crashfree India — mentor briefing deck, 15 slides.
# Reuses the organisation-overview slides with a personal note up front and a
# "year ahead + where your counsel would help" slide before the close.
import os
import nrsb2_style as ST
import build_nrsb3 as B
import build_overview as OV
from build_overview import cover, rakshak_ov, research_ov, close_ov
from nrsb2_style import *
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN

I = Inches
TOTAL = 15

def m_footer(s, wg, idx, total):
    hline(s, ML, I(7.06), CW)
    text(s, ML, I(7.14), I(9), I(0.25), "Crashfree India  ·  A briefing for mentors  ·  2026", size=8.5, color=MUT, ls=1.0)
    text(s, SW-MR-I(1.2), I(7.14), I(1.2), I(0.25), f"{idx:02d} / {total:02d}", size=8.5, color=MUT, align=PP_ALIGN.RIGHT, ls=1.0)

B.footer = m_footer
OV._footer = m_footer
OV.TOTAL = TOTAL

# ---------------------------------------------------------------- 01 COVER
def cover_m():
    s = cover()
    # replace the top-right edition label: cover() wrote "ORGANISATION OVERVIEW · 2026"
    for sh in s.shapes:
        if sh.has_text_frame and "ORGANISATION OVERVIEW" in sh.text_frame.text:
            for p in sh.text_frame.paragraphs:
                for r in p.runs:
                    r.text = "A BRIEFING FOR MENTORS  ·  2026"
    return s

# ---------------------------------------------------------------- 02 PERSONAL NOTE
def note(idx):
    s = slide()
    text(s, ML, I(0.30), I(8), I(0.24), "BEFORE THE SLIDES", font=HEAD, size=9, bold=True, color=BRAND, tracking=2.2)
    hline(s, ML, I(0.62), I(0.55), color=BRAND, wt=2.0)
    text(s, ML, I(0.76), I(12), I(0.5), [("A personal ", {'color': INK}), ("note", {'color': BRAND})], font=HEAD, size=22.5, bold=True, ls=1.1)
    x = ML+I(0.95); w = I(10.2); y = I(1.5)
    rect(s, x, y, w, I(5.42), fill=PAPER, line=LINE, lw=1.2)
    rect(s, x, y, w, I(0.06), fill=BRAND)
    s.shapes.add_picture(LOGO_BLUE, x+I(0.5), y+I(0.32), width=I(1.35))
    text(s, x+w-I(3.2), y+I(0.36), I(2.7), I(0.3), "New Delhi · August 2026", size=9.5, color=MUT, align=PP_ALIGN.RIGHT)
    body = ("Dear friend,\n"
            "This deck goes to a small set of people whose judgement I deeply admire. I am writing to ask for something specific: your counsel, from time to time, as Crashfree India grows.\n"
            "Crashfree India is a road safety nonprofit, registered as the Vision Zero Trust, co-founded with the Indian Road Safety Council and backed by a three-year, US$3 million commitment from Cars24. India loses more than 1.7 lakh lives on its roads every year. In our first year we built an audit-to-implementation engine that has moved 15 dangerous sites into rectification, an AI enforcement platform running with three police forces, a compensation practice that follows crash victims' families from FIR to disbursal, and open data platforms that turn scattered public records into citable evidence. MS Dhoni carries this message to the country as our Goodwill Ambassador.\n"
            "The work has reached the stage where ambition can outrun experience. We are deciding which programmes become institutions, how to work with government at scale, and how to build an organisation that can hold this mission for a decade. On questions like these, we have more energy than experience, and we know it.\n"
            "The pages that follow are a short tour of what we have built. If the work speaks to you, I would be grateful for an hour of your time, and for the licence to write to you when we face a decision where your experience would show us the way.")
    tb = text(s, x+I(0.5), y+I(0.92), w-I(1.0), I(3.7), body, size=10.4, color=INK, ls=1.28)
    for p in tb.text_frame.paragraphs: p.space_after = Pt(6.5)
    text(s, x+I(0.5), y+I(4.56), w-I(1.0), I(0.3), "With respect,", size=10.4, color=INK)
    text(s, x+I(0.5), y+I(4.84), w-I(1.0), I(0.3), "Akhtar Hussain", font=HEAD, size=11.5, bold=True, color=INK)
    text(s, x+I(0.5), y+I(5.08), w-I(1.0), I(0.26), "Mission Lead, Crashfree India  ·  akhtar@crashfreeindia.org  ·  crashfreeindia.org", size=9.5, color=MUT)
    m_footer(s, None, idx, TOTAL)
    return s

# ---------------------------------------------------------------- 14 YEAR AHEAD + GUIDANCE
def guidance(idx):
    s = slide()
    header(s, "04 · The year ahead",
           [("Where we are going, and ", False), ("where your counsel would help", True)],
           lead="Year 2 moves from programmes to institutions. These are the goals, and the questions we would bring to a mentor.",
           sect=(4, "THE YEAR AHEAD"))
    colw = I(5.85)
    # left: the year ahead
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
    # right: guidance sought
    x2 = ML+colw+I(0.42)
    w2 = SW-MR-x2
    text(s, x2, I(2.02), w2, I(0.26), "WHERE GUIDANCE WOULD HELP", font=HEAD, size=9, bold=True, color=MUT, tracking=1.8)
    rows_r = [
        ("building-2", "Institution building", "Turning young programmes into bodies with standards, governance and a life beyond the founding team."),
        ("landmark", "Government at scale", "Deepening state partnerships while keeping our independence and our habit of publishing everything."),
        ("users", "People and leadership", "Growing a young team into leaders, and drawing senior operators to a nonprofit mission."),
        ("banknote", "Sustainability", "Building funding lines beyond the founding commitment, without distorting what we work on."),
        ("target", "Focus", "What to stop, what to scale, and when. The discipline of a small organisation with a national mission."),
    ]
    for i, (ic, t, d) in enumerate(rows_r):
        irow(s, x2, y+i*I(0.86), w2, ic, t, d, GR_T, "#0A9955")
    m_footer(s, None, idx, TOTAL)
    return s

if __name__ == "__main__":
    new_deck()
    cover_m()                     # 01
    note(2)                       # 02
    B.about(3, TOTAL, None)       # 03
    B.approach(4, TOTAL, None)    # 04
    B.portfolio(5, TOTAL, None)   # 05
    rakshak_ov(6)                 # 06
    B.satark(7, TOTAL, None)      # 07
    B.opendata(8, TOTAL, None)    # 08
    B.victim_suite(9, TOTAL, None)# 09
    research_ov(10)               # 10
    B.youth(11, TOTAL, None)      # 11
    B.ground(12, TOTAL, None)     # 12
    B.team(13, TOTAL, None)       # 13
    guidance(14)                  # 14
    close_ov()                    # 15
    save(os.path.join(BUILD, "CFI_Mentor_v1.pptx"))

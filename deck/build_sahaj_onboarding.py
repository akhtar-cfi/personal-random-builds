# SAHAJ — Team Induction Brief. Onboarding deck for the incoming engineering + product squad.
# House style: WG/NRSB deck language (nrsb2_style) — purple kicker+underline, one accent phrase,
# icon rows, soft cards, page-number footer. All body fonts >= 12pt where it carries meaning.
import os
from nrsb2_style import *
from pptx.util import Inches, Pt, Emu
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
I = Inches
TOTAL = 22

# self-sufficiency: nrsb2_style expects the logos at deck/, the repo keeps them under deck/assets/
import shutil
_DKD = os.path.dirname(os.path.abspath(__file__))
for _l in ("logo_blue.png", "logo_white.png"):
    if not os.path.exists(os.path.join(_DKD, _l)):
        shutil.copy(os.path.join(_DKD, "assets", _l), os.path.join(_DKD, _l))
PAL = [(BR_T, "#4A35FF"), (GR_T, "#0A9955"), (TE_T, "#0E8A8A"), (AM_T, "#E58900")]
GREENH, AMBERH, REDH = "#0A9955", "#E58900", "#E11900"

# widen the top-right running-agenda tab so long section names ("WHERE YOU COME IN") don't wrap
import nrsb2_style as _NS
def _sect_tab(s, cur, name):
    w = I(4.3)
    text(s, SW - MR - w, I(0.30), w, I(0.24), f"SECTION {cur} OF 5   ·   {name}",
         font=HEAD, size=8, bold=True, color=MUT, tracking=1.5, align=PP_ALIGN.RIGHT)
_NS.sect_tab = _sect_tab

new_deck()


def foot(s, idx):
    hline(s, ML, I(7.06), CW)
    text(s, ML, I(7.14), I(9.5), I(0.25), "Crashfree India   ·   SAHAJ — Team Induction Brief   ·   Confidential",
         size=8.5, color=MUT, ls=1.0)
    text(s, SW - MR - I(1.4), I(7.14), I(1.4), I(0.25), f"{idx:02d} / {TOTAL:02d}",
         size=8.5, color=MUT, align=PP_ALIGN.RIGHT, ls=1.0)


def kicker(s, txt):
    text(s, ML, I(0.30), I(9), I(0.24), txt.upper(), font=HEAD, size=9, bold=True, color=BRAND, tracking=2.2)
    hline(s, ML, I(0.62), I(0.55), color=BRAND, wt=2.0)


def statuslegend(s, x, y):
    for ic, c, lb in [("circle-check", GREENH, "Live"), ("triangle-alert", AMBERH, "Partial"), ("circle-dot", REDH, "Greenfield")]:
        icon(s, ic, x, y, I(0.22), c)
        text(s, x + I(0.28), y - I(0.02), I(1.1), I(0.3), lb, font=HEAD, size=9, bold=True, color=INK)
        x += I(1.35)


# ============================================================ 01 COVER
def cover():
    s = slide()
    s.shapes.add_picture(LOGO_BLUE, ML, I(0.52), width=I(1.95))
    text(s, SW - MR - I(4.0), I(0.58), I(4.0), I(0.3), "SEPTEMBER 2026   ·   JAIPUR → RAJASTHAN",
         font=HEAD, size=9, bold=True, color=MUT, tracking=1.8, align=PP_ALIGN.RIGHT)
    text(s, ML, I(1.9), I(9), I(0.3), "TEAM INDUCTION BRIEF", font=HEAD, size=11, bold=True, color=BRAND, tracking=2.4)
    hline(s, ML, I(2.28), I(0.7), color=BRAND, wt=2.5)
    text(s, ML, I(2.5), I(9), I(1.0), "SAHAJ", font=HEAD, size=58, bold=True, color=INK, ls=1.0)
    text(s, ML, I(3.62), I(11.6), I(0.6),
         [("The Hit-and-Run Compensation Portal — ", {'color': INK}), ("and the production rebuild we're starting together", {'color': BRAND})],
         font=HEAD, size=17, bold=True, ls=1.2)
    rows = [("route", "What it is", "A tracked digital pipeline for the ₹2 lakh the law already owes hit-and-run families."),
            ("map-pin", "Where it is", "Live on the ground in Jaipur for a month; now rebuilding for all of Rajasthan, then other states."),
            ("hammer", "Why you're here", "Audit it, harden it for scale, and close the last gaps — while the live pilot keeps running.")]
    y = I(4.75)
    for i, (ic, t, d) in enumerate(rows):
        yy = y + i * I(0.62)
        icon_disc(s, ic, ML, yy, I(0.42), BR_T, "#4A35FF")
        text(s, ML + I(0.58), yy - I(0.03), I(2.0), I(0.4), t, font=HEAD, size=11.5, bold=True, color=INK, anchor=MSO_ANCHOR.MIDDLE)
        text(s, ML + I(2.35), yy - I(0.03), I(9.4), I(0.5), d, size=11, color=MUT, ls=1.15, anchor=MSO_ANCHOR.MIDDLE)
    text(s, ML, I(6.92), I(9.2), I(0.3), "Prepared for the incoming engineering & product team   ·   Crashfree India × Rajasthan Transport & Road Safety Dept.",
         size=9.5, color=MUT)
    text(s, SW - MR - I(2.6), I(6.92), I(2.6), I(0.3), "crashfreeindia.org", font=HEAD, size=9.5, bold=True, color=BRAND, align=PP_ALIGN.RIGHT)
    return s


# ============================================================ 02 LETTER
def letter():
    s = slide()
    kicker(s, "Before the slides")
    text(s, ML, I(0.76), I(12), I(0.5), [("A note to the ", {'color': INK}), ("team", {'color': BRAND})],
         font=HEAD, size=22.5, bold=True, ls=1.1)
    x = ML + I(0.9); w = I(10.3); y = I(1.42)
    rect(s, x, y, w, I(5.35), fill=PAPER, line=LINE, lw=1.2)
    rect(s, x, y, w, I(0.06), fill=BRAND)
    s.shapes.add_picture(LOGO_BLUE, x + I(0.5), y + I(0.3), width=I(1.4))
    text(s, x + w - I(3.4), y + I(0.34), I(2.9), I(0.3), "Jaipur · September 2026", size=9.5, color=MUT, align=PP_ALIGN.RIGHT)
    body = ("Thank you for stepping up for this. It is a critical piece of work — it can decide whether a grieving family "
            "actually receives the ₹2 lakh the law already entitles them to, and it can set a national benchmark for how "
            "“AI for good” is scaled to fix real beneficiary systems.\n"
            "Here is the honest picture. The scheme is sound; the paper pipeline is where families fall through. We built SAHAJ "
            "to digitise that exact statutory chain, ran it live in Jaipur for a month, and learned a great deal about the ground "
            "reality. The current platform got us here fast, but much of it is vibe-coded — fine at pilot volume, not yet ready for a "
            "state. That is the job now: look at every part critically, keep the live pilot stable, and rebuild it to production grade.\n"
            "This deck is your on-ramp: what the project is, how the process works end to end, how the system is built, where we are, "
            "and exactly where we need your help. Please come to our call with questions — challenge anything that looks wrong.")
    tb = text(s, x + I(0.5), y + I(0.95), w - I(1.0), I(3.4), body, size=11, color=INK, ls=1.4)
    for p in tb.text_frame.paragraphs:
        p.space_after = Pt(11)
    text(s, x + I(0.5), y + I(4.3), w - I(1.0), I(0.3), "Respectfully,", size=11, color=INK)
    text(s, x + I(0.5), y + I(4.6), w - I(1.0), I(0.3), "Akhtar Hussain", font=HEAD, size=11.5, bold=True, color=INK)
    text(s, x + I(0.5), y + I(4.84), w - I(1.0), I(0.26), "Mission Lead, Crashfree India   ·   akhtar@crashfreeindia.org", size=9.5, color=MUT)
    return s


# ============================================================ 03 AGENDA
def agenda():
    s = slide()
    kicker(s, "How this brief is organised")
    text(s, ML, I(0.76), I(12), I(0.5), [("Five sections, ", {'color': INK}), ("from why it matters to where you come in", {'color': BRAND})],
         font=HEAD, size=22.5, bold=True, ls=1.1)
    rows = [("target", "The mission", "The problem, what SAHAJ is, and who is behind it.", "04 – 06"),
            ("workflow", "How SAHAJ works", "The statutory chain, the ten roles, the end-to-end flow, the family experience.", "07 – 11"),
            ("layers", "Under the hood", "Architecture, the database-as-boundary security model, and the modular design.", "12 – 14"),
            ("gauge", "Where we are", "What is live, the honest gaps, and the No.1 risk: adoption.", "15 – 17"),
            ("hammer", "Where you come in", "The rebuild mandate, the workstreams, how we'll work, and your first week.", "18 – 22")]
    y = I(1.72)
    for i, (ic, t, d, pg) in enumerate(rows):
        yy = y + i * I(1.02)
        rect(s, ML, yy, CW, I(0.88), fill=MIST if i % 2 == 0 else PAPER, line=None if i % 2 == 0 else LINE, rounded=True, radius=0.10)
        num_disc(s, ML + I(0.22), yy + I(0.2), I(0.48), i + 1)
        icon_disc(s, ic, ML + I(0.95), yy + I(0.2), I(0.48), BR_T, "#4A35FF")
        text(s, ML + I(1.68), yy + I(0.14), I(6.5), I(0.4), t, font=HEAD, size=13, bold=True, color=INK, ls=1.0)
        text(s, ML + I(1.68), yy + I(0.47), I(8.6), I(0.35), d, size=10.5, color=MUT, ls=1.12)
        text(s, SW - MR - I(1.75), yy + I(0.24), I(1.55), I(0.4), pg, font=HEAD, size=12, bold=True, color=BRAND, align=PP_ALIGN.RIGHT)
    return s


# ============================================================ 04 PROBLEM
def problem():
    s = slide()
    header(s, "01 · The mission",
           [("The money is real and waiting — ", False), ("the pipeline is where it dies", True)],
           lead="Under the Hit-and-Run Compensation Scheme, 2022, the family of someone killed by an unidentified vehicle is owed ₹2,00,000 (₹50,000 for grievous injury) from a national fund. No lawyer, no fee, no deadline. Yet most families never see it.",
           sect=(1, "THE MISSION"))
    # stat band
    stats = [("68,584", "hit-and-run crashes\nrecorded in 2024", BRAND),
             ("9,813", "compensation claims\nregistered, FY25-26", BRAND),
             ("≈ 1 in 7", "crashes that convert\nto a claim, nationally", AMBER),
             ("27%", "of Rajasthan's H&R cases\never reach the SDM desk", REDH if False else AMBER)]
    xw = I(2.86); gx = I(0.15)
    for i, (v, l, c) in enumerate(stats):
        x = ML + i * (xw + gx)
        rect(s, x, I(2.5), xw, I(1.4), fill=MIST, rounded=True, radius=0.12)
        text(s, x + I(0.22), I(2.64), xw - I(0.4), I(0.55), v, font=HEAD, size=26, bold=True, color=c if isinstance(c, RGBColor) else BRAND, ls=1.0)
        text(s, x + I(0.22), I(3.2), xw - I(0.4), I(0.6), l, size=9.5, color=MUT, ls=1.15)
    # causes
    text(s, ML, I(4.2), I(12), I(0.3), "WHY ELIGIBLE FAMILIES FALL THROUGH", font=HEAD, size=9, bold=True, color=MUT, tracking=1.6)
    rows = [("eye-off", "Nobody knows", "Families don't know the scheme exists; touts and lawyers capture those who do."),
            ("files", "Four offices, on paper", "The claim crosses police → SDM → DM/Collector → insurer council; no one sees the whole chain."),
            ("timer-off", "Clocks nobody keeps", "Statutory limits (1 month enquiry, 15 days sanction) exist on paper, but nothing measures or enforces them."),
            ("file-x", "So cases die between desks", "In Jaipur East, 0 of 303 registered hit-and-run cases moved to the compensation desk at all.")]
    y = I(4.6)
    for i, (ic, t, d) in enumerate(rows):
        tint, col = PAL[i % 4]
        irow(s, ML, y + i * I(0.6), I(12.0), ic, t, d, tint, col, d=I(0.4), tsize=12, dsize=10.5)
    text(s, ML, I(7.0) - I(0.28), I(12), I(0.22),
         "Sources: Lok Sabha USQ 6419 (02.04.2026); Rajasthan Police compilation, Apr 2022 – Mar 2024.", size=8, color=MUT)
    foot(s, 4)
    return s


# ============================================================ 05 WHAT IS SAHAJ
def whatis():
    s = slide()
    header(s, "01 · The mission",
           [("SAHAJ: a tracked pipeline for money ", False), ("the law already sanctioned", True)],
           lead="It digitises the exact statutory chain — no rule change needed. The officer starts a case in two minutes; the family submits documents from WhatsApp with no login; every officer sees what is pending on them, and for how long.",
           sect=(1, "THE MISSION"))
    rows = [("hand-heart", "Zero burden on the family", "No app, no account, no password on first contact. A WhatsApp/SMS link, photos of documents, done.", 0),
            ("languages", "Hindi-first, cheap-phone-first", "Defaults to Hindi, English one click away; works on the cheapest phone the family owns.", 1),
            ("git-merge", "The statutory chain, digitised as-is", "Mirrors the legal roles and the four forms (I–IV) rather than inventing a parallel process.", 2),
            ("timer", "Clocks as SLAs", "Every case shows who it's pending on and for how long; the clock counts only active days.", 3),
            ("smartphone", "Behaves like an installed app", "Officers aren't browser users. The officer app installs to the home screen (PWA) — no app store, same backend.", 0),
            ("scan-line", "No duplicate data entry, in the end", "The FIR facts already sit in police systems; the long-term first mile is a CCTNS/e-DAR feed, not a new screen.", 1)]
    y = I(2.3)
    for i, (ic, t, d, ci) in enumerate(rows):
        col_x = ML if i < 3 else ML + I(6.1)
        row_y = y + (i % 3) * I(1.35)
        tint, col = PAL[ci]
        rect(s, col_x, row_y, I(5.85), I(1.2), fill=PAPER, line=LINE, rounded=True, radius=0.08)
        icon_disc(s, ic, col_x + I(0.2), row_y + I(0.2), I(0.46), tint, col)
        text(s, col_x + I(0.82), row_y + I(0.16), I(4.85), I(0.35), t, font=HEAD, size=12, bold=True, color=INK, ls=1.0)
        text(s, col_x + I(0.82), row_y + I(0.52), I(4.85), I(0.6), d, size=10, color=MUT, ls=1.18)
    foot(s, 5)
    return s


# ============================================================ 06 WHO IS BEHIND IT
def whois():
    s = slide()
    header(s, "01 · The mission",
           [("Who is behind SAHAJ, and ", False), ("who it's built for", True)],
           lead="SAHAJ is one build inside Crashfree India's compensation vertical, made at the request of the Rajasthan Transport & Road Safety Department.",
           sect=(1, "THE MISSION"))
    left = [("building-2", "Crashfree India (CFI)", "A road-safety nonprofit registered as the Vision Zero Trust, co-founded with the Indian Road Safety Council, backed by a 3-year, US$3M commitment from Cars24. MS Dhoni is Goodwill Ambassador."),
            ("landmark", "The government partner", "Rajasthan Transport & Road Safety Department — the pilot's owner. CFI holds working seats on district road-safety committees and MoUs with police."),
            ("scale", "The compensation vertical", "CFI maps where compensation stalls, builds tools families can use, and sits inside district machinery to help files move. SAHAJ is the software spine of that work.")]
    y = I(2.35)
    for i, (ic, t, d) in enumerate(left):
        tint, col = PAL[i % 4]
        icon_disc(s, ic, ML, y + i * I(1.35), I(0.5), tint, col)
        text(s, ML + I(0.7), y + i * I(1.35) - I(0.02), I(6.3), I(0.35), t, font=HEAD, size=13, bold=True, color=INK, ls=1.0)
        text(s, ML + I(0.7), y + i * I(1.35) + I(0.34), I(6.3), I(0.9), d, size=10.5, color=MUT, ls=1.24)
    # right card: naming lineage (so they don't hunt for files)
    rx = I(8.05); rw = I(4.65)
    rect(s, rx, I(2.3), rw, I(4.35), fill=MIST, rounded=True, radius=0.08)
    icon_disc(s, "info", rx + I(0.25), I(2.55), I(0.44), BR_T, "#4A35FF")
    text(s, rx + I(0.83), I(2.57), rw - I(1.0), I(0.4), "A quick note on names", font=HEAD, size=12.5, bold=True, color=INK)
    names = [("SAHAJ", "the portal / product (this project)"),
             ("crash_claim_cfi", "the repository / package name"),
             ("Sahay / Aasha", "earlier names for the WhatsApp bot & AI helper in older mockups"),
             ("HRCCS", "“Hit-and-Run Compensation” in older CFI docs")]
    yy = I(3.2)
    for nm, d in names:
        text(s, rx + I(0.25), yy, rw - I(0.5), I(0.3), nm, font=HEAD, size=11, bold=True, color=BRAND)
        text(s, rx + I(0.25), yy + I(0.26), rw - I(0.5), I(0.5), d, size=9.5, color=MUT, ls=1.15)
        yy += I(0.82)
    foot(s, 6)
    return s


# ============================================================ 07 FORMS + CHAIN
def forms():
    s = slide()
    header(s, "02 · How SAHAJ works",
           [("The statutory chain, and ", False), ("the four forms it runs on", True)],
           lead="Knowing these before the flow makes everything after it obvious. A claim crosses four statutory desks (a few districts add two or three more), each with its own form and its own clock.",
           sect=(2, "HOW SAHAJ WORKS"))
    forms = [("file-text", "Form I", "Application", "Family fills & uploads a photo", "#0E8A8A", TE_T),
             ("file-check", "Form II", "Enquiry report", "CEO (SDM) — generated, e-signed", "#4A35FF", BR_T),
             ("stamp", "Form III", "Sanction order", "CSC (DM) — amount locked to Form II", "#4A35FF", BR_T),
             ("file-signature", "Form IV", "Undertaking", "Family — no other claim for this accident", "#0E8A8A", TE_T)]
    xw = I(2.86); gx = I(0.15)
    for i, (ic, t, sub, d, col, tint) in enumerate(forms):
        x = ML + i * (xw + gx)
        rect(s, x, I(2.45), xw, I(1.75), fill=PAPER, line=LINE, rounded=True, radius=0.08)
        icon_disc(s, ic, x + I(0.22), I(2.65), I(0.5), tint, col)
        text(s, x + I(0.85), I(2.66), xw - I(1.0), I(0.35), t, font=HEAD, size=14, bold=True, color=INK)
        text(s, x + I(0.85), I(3.0), xw - I(1.0), I(0.3), sub, font=HEAD, size=10, bold=True, color=MUT)
        text(s, x + I(0.22), I(3.45), xw - I(0.44), I(0.7), d, size=9.5, color=MUT, ls=1.2)
    # the chain
    text(s, ML, I(4.55), I(12), I(0.3), "THE FOUR DESKS, AND WHO SITS AT EACH", font=HEAD, size=9, bold=True, color=MUT, tracking=1.6)
    chain = [("shield", "Police station", "Investigating Officer (IO)"),
             ("user-check", "Sub-division", "CEO — Tahsildar / SDO"),
             ("landmark", "District", "CSC — DM / Collector"),
             ("banknote", "Insurer council", "GI Council (GIC) + settlement")]
    n = len(chain); cw = (CW - I(0.6) * (n - 1)) / n
    y = I(5.0)
    for i, (ic, place, who) in enumerate(chain):
        x = ML + i * (cw + I(0.6))
        rect(s, x, y, cw, I(1.35), fill=MIST, rounded=True, radius=0.1)
        icon_disc(s, ic, x + I(0.22), y + I(0.22), I(0.5), BR_T, "#4A35FF")
        text(s, x + I(0.22), y + I(0.82), cw - I(0.4), I(0.3), place, font=HEAD, size=12, bold=True, color=INK)
        text(s, x + I(0.22), y + I(1.08), cw - I(0.4), I(0.3), who, size=9.5, color=MUT)
        if i < n - 1:
            text(s, x + cw + I(0.02), y + I(0.4), I(0.56), I(0.4), "→", size=20, color=BRAND, align=PP_ALIGN.CENTER)
    text(s, ML, I(6.62), I(12), I(0.25), "Statutory clock end-to-end ≈ 60 days:  1 month enquiry (CEO)  +  15 days sanction (CSC)  +  15 days payment (GIC).",
         size=10, color=INK, ls=1.2)
    foot(s, 7)
    return s


# ============================================================ 08 ROLES
def roles():
    s = slide()
    header(s, "02 · How SAHAJ works",
           [("Ten roles cover the whole chain — ", False), ("each sees only its jurisdiction", True)],
           lead="Everyone below the state level is provisioned from within the portal by the level above them. Access is scoped in the database itself, not just the menu.",
           sect=(2, "HOW SAHAJ WORKS"))
    left = [("shield", "Police IO / SHO", "Registers cases from the FIR, uploads it, shares the family's link, submits complete files."),
            ("smartphone", "Claimant / family", "Uploads documents via WhatsApp or a zero-login page; no password, ever."),
            ("user-check", "CEO — SDM / Tahsildar", "Verifies each document, files Form II with an OTP e-sign. Clock: 1 month."),
            ("stamp", "CSC — DM / Collector", "Sanctions Form III, can revert or hold, handles GIC queries. Clock: 15 days."),
            ("banknote", "Settlement / GIC desk", "Works the sanctioned queue, records the payment UTR, marks the case PAID.")]
    right = [("user-cog", "Program Coordinator", "CFI-embedded operator who digitises the legacy paper backlog. Can never sign."),
             ("building-2", "District admin", "District dashboard, tehsil drill-down, staff & jurisdiction management, reports."),
             ("landmark", "State admin", "State overview, district league table, all reports, broadcasts, analytics."),
             ("eye", "Viewer", "Read-only oversight (e.g. DLSA, auditor) for an assigned jurisdiction — no writes."),
             ("settings-2", "Super admin (CFI)", "Creates states/districts, global audit, AI usage console, system health.")]
    def col(items, x0):
        y = I(2.3)
        for i, (ic, t, d) in enumerate(items):
            tint, cc = PAL[i % 4]
            icon_disc(s, ic, x0, y + i * I(0.92), I(0.42), tint, cc)
            text(s, x0 + I(0.58), y + i * I(0.92) - I(0.02), I(5.3), I(0.3), t, font=HEAD, size=11.5, bold=True, color=INK)
            text(s, x0 + I(0.58), y + i * I(0.92) + I(0.27), I(5.4), I(0.55), d, size=9.5, color=MUT, ls=1.16)
    col(left, ML)
    col(right, ML + I(6.35))
    foot(s, 8)
    return s


# ============================================================ 09 END-TO-END FLOW (the flowchart)
def flow():
    s = slide()
    header(s, "02 · How SAHAJ works",
           [("From FIR to ₹2 lakh in the bank: ", False), ("one tracked pipeline", True)],
           lead="Six stages, each with a statutory clock. Blue = an officer acts; green = the family; the arrows between are automated (SMS/WhatsApp, nudges, an AI voice call, bilingual status).",
           sect=(2, "HOW SAHAJ WORKS"))
    stages = [("clipboard-list", "Police IO", "Registers the case\nfrom the FIR (2 min)", "instant", "#4A35FF", BR_T),
              ("smartphone", "Family", "Uploads 7 docs on\nWhatsApp — no login", "no login", "#0A9955", GR_T),
              ("file-check", "CEO / SDM", "Verifies docs +\nsigns Form II", "30 days", "#4A35FF", BR_T),
              ("stamp", "CSC / DM", "Sanctions +\nsigns Form III", "15 days", "#4A35FF", BR_T),
              ("banknote", "GIC / Settlement", "Pays the UTR into\nthe bank account", "15 days", "#0A9955", GR_T),
              ("badge-check", "PAID", "Terminal state,\nfull audit trail", "≈ 60 d", "#0A9955", GR_T)]
    n = len(stages); gap = I(0.2)
    cw = (CW - gap * (n - 1)) / n
    y = I(2.55); ch = I(2.55)
    for i, (ic, role, act, sla, col, tint) in enumerate(stages):
        x = ML + i * (cw + gap)
        rect(s, x, y, cw, ch, fill=PAPER, line=LINE, rounded=True, radius=0.07)
        icon_disc(s, ic, x + I(0.16), y + I(0.2), I(0.5), tint, col)
        text(s, x + I(0.16), y + I(0.82), cw - I(0.32), I(0.3), role, font=HEAD, size=11.5, bold=True, color=INK, ls=1.0)
        text(s, x + I(0.16), y + I(1.14), cw - I(0.32), I(0.75), act, size=9.5, color=MUT, ls=1.2)
        hline(s, x + I(0.16), y + I(1.95), cw - I(0.32))
        chip(s, x + I(0.16), y + I(2.06), cw - I(0.32), I(0.36), sla, fill=MIST, color=RGBColor(0x4A, 0x35, 0xFF) if col == "#4A35FF" else GREEN, size=9)
        if i < n - 1:
            text(s, x + cw - I(0.02), y + I(1.0), gap + I(0.06), I(0.4), "→", size=15, color=MUT, align=PP_ALIGN.CENTER)
    # before / after rails
    rect(s, ML, I(5.4), I(5.95), I(1.15), fill=MIST, rounded=True, radius=0.1)
    icon_disc(s, "car-front", ML + I(0.2), I(5.6), I(0.42), AM_T, "#E58900")
    text(s, ML + I(0.78), I(5.58), I(5.0), I(0.3), "Before stage 1", font=HEAD, size=11, bold=True, color=INK)
    text(s, ML + I(0.78), I(5.86), I(4.9), I(0.6), "The FIR & e-DAR entry happen as today; SAHAJ doesn't replace them. If the vehicle is later traced, the case leaves the scheme.", size=9.5, color=MUT, ls=1.18)
    rect(s, ML + I(6.15), I(5.4), I(5.95), I(1.15), fill=BR_T, rounded=True, radius=0.1)
    icon_disc(s, "circle-check", ML + I(6.35), I(5.6), I(0.42), PAPER, "#4A35FF")
    text(s, ML + I(6.93), I(5.58), I(5.0), I(0.3), "Every state change is logged", font=HEAD, size=11, bold=True, color=BRAND)
    text(s, ML + I(6.93), I(5.86), I(4.9), I(0.6), "Actor, role, before/after and time — append-only. Holds pause the clock; PAID is immutable and needs a UTR.", size=9.5, color=BRAND, ls=1.18)
    foot(s, 9)
    return s


# ============================================================ 10 CLAIMANT EXPERIENCE
def claimant():
    s = slide()
    header(s, "02 · How SAHAJ works",
           [("The family side — ", False), ("the part that moves the number", True)],
           lead="Everything here assumes a bereaved, feature-phone-adjacent user reached on WhatsApp. If the automation fails, it degrades to manual — the family is never stuck.",
           sect=(2, "HOW SAHAJ WORKS"))
    rows = [("link", "Magic link, zero login", "The SMS/WhatsApp link opens a government-styled page listing the documents needed, in plain Hindi. Photos upload from the camera."),
            ("bot", "WhatsApp bot", "The family just sends photos. An AI vision check files each one — or, if it's a valid but wrong document, files it under the right slot; after 3 tries it files anyway for manual review."),
            ("shield-question", "Scam-fear handling", "The bot names the scheme and the department first; free-text questions get scheme-scoped answers, including “is this a fraud?” reassurance."),
            ("phone-call", "Nudges, then an AI voice call", "If documents don't arrive, capped WhatsApp/SMS nudges follow; after a wait, an AI voice call in natural Hindi explains the scheme and what to send."),
            ("key-round", "Status without a password", "An OTP on the registered phone opens a read-only claim dashboard any time. Rejections and demands arrive as bilingual WhatsApp/SMS with the reason.")]
    y = I(2.35)
    for i, (ic, t, d) in enumerate(rows):
        tint, col = PAL[i % 4]
        irow(s, ML, y + i * I(0.85), I(12.0), ic, t, d, tint, col, d=I(0.44), tsize=12, dsize=10.5)
    foot(s, 10)
    return s


# ============================================================ 11 WHAT EACH ROLE SEES
def surfaces():
    s = slide()
    header(s, "02 · How SAHAJ works",
           [("One backend, ", False), ("a workspace shaped for each desk", True)],
           lead="Same accounts, same data as the web — the officer app just installs like an app. Here's what each surface does.",
           sect=(2, "HOW SAHAJ WORKS"))
    cards = [("smartphone", "Police IO (installable)", "Registration form, inline grid & bulk Excel import; a “pending from you” column; one-tap family link; vehicle-traced reporting."),
             ("columns-2", "CEO / CSC desks", "Split-screen document viewer with verify / flag / send-back (bilingual reasons); Form II / III prepared from case data and OTP e-signed."),
             ("banknote", "Settlement desk", "Queue of sanctioned cases; record the bank UTR and mark PAID — the one action that closes a case. (Least-built surface today.)"),
             ("folder-clock", "Coordinator backlog", "A wizard to register legacy paper cases and move them through the real state machine, attaching scans of the wet-signed forms."),
             ("layout-dashboard", "District & state admin", "Funnel dashboard, an Action Center ordered by SLA urgency, stuck-case & breach views, downloadable reports, staff management."),
             ("settings-2", "Super admin (CFI)", "Jurisdiction CRUD across states, global audit, an AI usage & performance console. Demo data never counts in real statistics.")]
    tw = I(3.95); th = I(1.95); gx = I(0.12); gy = I(0.18)
    for i, (ic, t, d) in enumerate(cards):
        r, c = divmod(i, 3)
        x = ML + c * (tw + gx); y = I(2.4) + r * (th + gy)
        tint, col = PAL[i % 4]
        rect(s, x, y, tw, th, fill=PAPER, line=LINE, rounded=True, radius=0.07)
        icon_disc(s, ic, x + I(0.2), y + I(0.2), I(0.46), tint, col)
        text(s, x + I(0.8), y + I(0.24), tw - I(0.95), I(0.4), t, font=HEAD, size=11.5, bold=True, color=INK, ls=1.02)
        text(s, x + I(0.2), y + I(0.82), tw - I(0.4), I(1.0), d, size=9.5, color=MUT, ls=1.2)
    foot(s, 11)
    return s


# ============================================================ 12 ARCHITECTURE
def architecture():
    s = slide()
    header(s, "03 · Under the hood",
           [("One Next.js app over Postgres — ", False), ("the database is the API's backstop", True)],
           lead="There is no separate API tier: Server Actions are the API, and every one re-checks authorisation before the database's own row-level rules apply.",
           sect=(3, "UNDER THE HOOD"))
    # three layers
    def layer(x, w, ic, title, items, tint, col, y=I(2.35), h=I(2.5)):
        rect(s, x, y, w, h, fill=PAPER, line=LINE, rounded=True, radius=0.07)
        icon_disc(s, ic, x + I(0.2), y + I(0.2), I(0.5), tint, col)
        text(s, x + I(0.82), y + I(0.24), w - I(1.0), I(0.4), title, font=HEAD, size=12.5, bold=True, color=INK, ls=1.0)
        yy = y + I(0.85)
        for it in items:
            text(s, x + I(0.24), yy, w - I(0.48), I(0.4), "•  " + it, size=10, color=MUT, ls=1.15)
            yy += I(0.42)
    layer(ML, I(3.85), "smartphone", "Clients", ["Officer app — installable PWA", "Family — WhatsApp / SMS / voice", "Hindi default, English switch"], TE_T, "#0E8A8A")
    layer(ML + I(4.1), I(3.85), "server", "SAHAJ app", ["Next.js 16 · React 19 · AntD Pro", "Server Actions = the API", "Scheduled crons (nudges, calls, report)"], BR_T, "#4A35FF")
    layer(ML + I(8.2), I(3.9), "database", "Supabase / Postgres", ["Row-level security on every table", "Auth · Storage · Realtime · Edge fns", "Region: Mumbai (data in India)"], GR_T, "#0A9955")
    # external services strip
    text(s, ML, I(5.15), I(12), I(0.3), "EXTERNAL SERVICES (SWAPPABLE, INDIA-RESIDENT WHERE IT MATTERS)", font=HEAD, size=9, bold=True, color=MUT, tracking=1.4)
    ext = [("message-circle", "MSG91", "WhatsApp + SMS + OTP (DLT)"), ("scan-text", "Vision AI", "document checks (optional)"),
           ("phone-call", "Voice AI", "Hindi follow-up calls"), ("file-text", "pdf-lib", "Devanagari statutory forms")]
    xw = I(2.94); gx = I(0.14)
    for i, (ic, t, d) in enumerate(ext):
        x = ML + i * (xw + gx)
        rect(s, x, I(5.5), xw, I(0.95), fill=MIST, rounded=True, radius=0.1)
        icon_disc(s, ic, x + I(0.18), I(5.72), I(0.42), BR_T, "#4A35FF")
        text(s, x + I(0.74), I(5.66), xw - I(0.9), I(0.3), t, font=HEAD, size=11, bold=True, color=INK)
        text(s, x + I(0.74), I(5.95), xw - I(0.9), I(0.4), d, size=9, color=MUT, ls=1.1)
    text(s, ML, I(6.62), I(12), I(0.25), "Stack today: Next.js 16 (App Router, Turbopack) · Supabase Postgres 16 · MSG91 · Vercel (Mumbai) · ~64 migrations · 607 automated tests.",
         size=9.5, color=INK, ls=1.2)
    foot(s, 12)
    return s


# ============================================================ 13 SECURITY
def security():
    s = slide()
    header(s, "03 · Under the hood",
           [("The one idea to hold on to: ", False), ("the database is the boundary", True)],
           lead="Screens and APIs can have bugs; these rules hold even then, because they live in Postgres itself. This is the non-negotiable that must survive the rebuild.",
           sect=(3, "UNDER THE HOOD"))
    rows = [("table-2", "Row-level security on every table", "Each query is scoped to the officer's jurisdiction in the DB. The UI's role-filtered menus are cosmetic; the server re-checks everything."),
            ("key-round", "Roles ride in verified tokens", "Role + jurisdiction are embedded in the signed login token; anything unreadable fails closed to the least-privileged role. No role is claimable from the client."),
            ("git-merge", "A state-machine trigger binds everyone", "Incl. admins and the service key: no case created mid-flow, amount capped to the statutory tier, Form II before Form III, PAID needs a UTR, terminal states immutable. No back door."),
            ("folder-lock", "Documents in deny-all storage", "The only way to a file is a short-lived signed URL issued after the server checks authorisation. The service key never reaches a browser."),
            ("scroll-text", "Full, append-only audit log", "Every state change records actor, role, before/after and time. Magic links are hashed & expiring; OTPs verified in constant time.")]
    y = I(2.3)
    for i, (ic, t, d) in enumerate(rows):
        tint, col = PAL[i % 4]
        irow(s, ML, y + i * I(0.72), I(12.0), ic, t, d, tint, col, d=I(0.44), tsize=12, dsize=10.3)
    rect(s, ML, I(6.0), CW, I(0.72), fill=BR_T, rounded=True, radius=0.14)
    text(s, ML + I(0.25), I(6.14), CW - I(0.5), I(0.5),
         [("Survives the rebuild as-is: ", {'bold': True, 'color': BRAND}),
          ("this model, jurisdiction + role claims, the append-only ledger, and OTP-signed statutory forms. First-day task: rotate every secret — the build-time keys must not be the running keys.", {'color': BRAND})],
         size=10.5, ls=1.25)
    foot(s, 13)
    return s


# ============================================================ 14 MODULAR DESIGN
def modular():
    s = slide()
    header(s, "03 · Under the hood",
           [("Modular & multi-tenant — ", False), ("a new district is a workbook, not a deploy", True)],
           lead="Built to serve any Indian state. One security kernel; feature modules around it; each deployment is just another set of jurisdictions.",
           sect=(3, "UNDER THE HOOD"))
    # left: 4-level jurisdiction stack
    text(s, ML, I(2.2), I(4.0), I(0.28), "ONE JURISDICTION SPINE", font=HEAD, size=9, bold=True, color=MUT, tracking=1.4)
    levels = [("landmark", "State"), ("building-2", "District"), ("map", "Subdivision (Tehsil)"), ("shield", "Thana")]
    y = I(2.55)
    for i, (ic, lv) in enumerate(levels):
        rect(s, ML, y + i * I(0.62), I(3.7), I(0.5), fill=MIST, rounded=True, radius=0.12)
        icon_disc(s, ic, ML + I(0.1), y + i * I(0.62) + I(0.05), I(0.4), BR_T, "#4A35FF")
        text(s, ML + I(0.62), y + i * I(0.62), I(3.0), I(0.5), lv, font=HEAD, size=11.5, bold=True, color=INK, anchor=MSO_ANCHOR.MIDDLE)
        if i < len(levels) - 1:
            text(s, ML + I(1.6), y + i * I(0.62) + I(0.46), I(0.4), I(0.2), "↓", size=12, color=MUT)
    rect(s, ML, y + 4 * I(0.62) + I(0.05), I(3.7), I(0.62), fill=BR_T, rounded=True, radius=0.14)
    text(s, ML + I(0.18), y + 4 * I(0.62) + I(0.12), I(3.4), I(0.5),
         [("One RLS rule: ", {'bold': True, 'color': BRAND, 'size': 10}), ("case_in_my_jurisdiction()", {'color': BRAND, 'size': 10, 'font': 'Geist'})], ls=1.15)
    # right: module map around kernel
    mx = I(4.9); mw = SW - MR - mx
    text(s, mx, I(2.2), mw, I(0.28), "ONE KERNEL · MANY MODULES", font=HEAD, size=9, bold=True, color=MUT, tracking=1.4)
    rect(s, mx, I(2.55), mw, I(0.82), fill=INK, rounded=True, radius=0.1)
    text(s, mx + I(0.25), I(2.63), mw - I(0.5), I(0.3), "Security kernel — the database boundary", font=HEAD, size=11.5, bold=True, color=PAPER)
    for j, t in enumerate(["RLS", "State machine", "Audit ledger", "JWT claims"]):
        chip(s, mx + I(0.25) + j * I(1.85), I(2.98), I(1.7), I(0.3), t, fill=RGBColor(0x2A, 0x2A, 0x40), color=LAVW, size=8.5)
    mods = [("clipboard-list", "Registration", GREENH), ("smartphone", "Claimant vault", GREENH),
            ("file-check", "CEO / Form II", GREENH), ("stamp", "CSC / Form III", GREENH),
            ("layout-dashboard", "Admin & analytics", GREENH), ("folder-clock", "Coordinator", GREENH),
            ("banknote", "Settlement / UTR", AMBERH), ("bell", "Realtime notify", AMBERH),
            ("scan-text", "AI doc-check", REDH), ("bar-chart-3", "Reports", GREENH)]
    tw = (mw - I(0.14) * 4) / 5; th = I(0.86)
    for i, (ic, t, dot) in enumerate(mods):
        r, c = divmod(i, 5)
        x = mx + c * (tw + I(0.14)); yy = I(3.6) + r * (th + I(0.14))
        rect(s, x, yy, tw, th, fill=PAPER, line=LINE, rounded=True, radius=0.1)
        icon_disc(s, ic, x + I(0.12), yy + I(0.13), I(0.34), BR_T, "#4A35FF")
        icon(s, "circle", x + tw - I(0.26), yy + I(0.13), I(0.14), dot)
        text(s, x + I(0.1), yy + I(0.5), tw - I(0.2), I(0.3), t, font=HEAD, size=8.5, bold=True, color=INK, ls=1.0)
    statuslegend(s, mx, I(5.5))
    # bottom callout
    rect(s, ML, I(6.02), CW, I(0.72), fill=MIST, rounded=True, radius=0.12)
    text(s, ML + I(0.25), I(6.15), CW - I(0.5), I(0.5),
         [("Nothing is tied to our GitHub or Supabase. ", {'bold': True}),
          ("The whole backend ports (migrations + edge function + env vars); new states onboard by a super-admin workbook. CFI has offered migration to government cloud (RISL/NIC) in 4–6 weeks — data already in India.", {'color': MUT})],
         size=10, ls=1.22)
    foot(s, 14)
    return s


# ============================================================ 15 STATUS
def status():
    s = slide()
    header(s, "04 · Where we are",
           [("Live in Jaipur for a month — ", False), ("a proven flow on a fast MVP", True)],
           lead="The whole chain works end to end in production. Two lanes run in parallel: the portal-native pilot, and the old paper flow that a CFI operator shadow-enters so nothing is lost.",
           sect=(4, "WHERE WE ARE"))
    stats = [("Aug 31", "go-live, real accounts,\ncomms gated"), ("6", "pilot thanas across\n2 tehsils (Jaipur)"),
             ("607", "automated tests\n(RLS + lifecycle)"), ("~64", "numbered DB\nmigrations")]
    xw = I(2.86); gx = I(0.15)
    for i, (v, l) in enumerate(stats):
        x = ML + i * (xw + gx)
        rect(s, x, I(2.4), xw, I(1.3), fill=MIST, rounded=True, radius=0.12)
        text(s, x + I(0.22), I(2.52), xw - I(0.4), I(0.5), v, font=HEAD, size=24, bold=True, color=BRAND, ls=1.0)
        text(s, x + I(0.22), I(3.06), xw - I(0.4), I(0.6), l, size=9.5, color=MUT, ls=1.15)
    # two lanes
    rect(s, ML, I(4.05), I(5.95), I(2.35), fill=PAPER, line=LINE, rounded=True, radius=0.07)
    icon_disc(s, "check-check", ML + I(0.22), I(4.25), I(0.5), GR_T, "#0A9955")
    text(s, ML + I(0.85), I(4.3), I(5.0), I(0.4), "Lane A — portal-native", font=HEAD, size=13, bold=True, color=INK)
    for j, t in enumerate(["6 pilot thanas with live IO/SHO accounts", "Family uploads, CEO/CSC signing, GIC recording", "Backlog digitised via the coordinator console", "Reports, broadcasts, grievances, full audit"]):
        text(s, ML + I(0.3), I(4.9) + j * I(0.36), I(5.5), I(0.35), "•  " + t, size=10, color=MUT, ls=1.12)
    rect(s, ML + I(6.15), I(4.05), I(5.95), I(2.35), fill=PAPER, line=LINE, rounded=True, radius=0.07)
    icon_disc(s, "file-stack", ML + I(6.37), I(4.25), I(0.5), AM_T, "#E58900")
    text(s, ML + I(7.0), I(4.3), I(5.0), I(0.4), "Lane B — legacy paper flow", font=HEAD, size=13, bold=True, color=INK)
    for j, t in enumerate(["The DM-office paper process, unchanged", "A CFI operator shadow-enters every 2026 case", "Keeps a live register while adoption grows", "The safety net: the pilot never loses a case"]):
        text(s, ML + I(6.45), I(4.9) + j * I(0.36), I(5.5), I(0.35), "•  " + t, size=10, color=MUT, ls=1.12)
    foot(s, 15)
    return s


# ============================================================ 16 GAPS
def gaps():
    s = slide()
    header(s, "04 · Where we are",
           [("The honest gaps — ", False), ("what we finish and harden together", True)],
           lead="None of these block the statutory flow today, but every one is real. Stated plainly so nobody is surprised in week one.",
           sect=(4, "WHERE WE ARE"))
    rows = [("banknote", "Settlement / disbursement console", "Only the PAID-needs-UTR rule is enforced; the desk workspace around it is minimal. The clearest greenfield piece.", REDH, "Greenfield"),
            ("scan-text", "AI document-check loop", "Specified end-to-end and scaffolded, but nothing writes the results in production yet — today it degrades to all-manual review.", REDH, "Greenfield"),
            ("bell", "Realtime notification bell", "The UI shell exists; no realtime transport is wired to it yet.", AMBERH, "Partial"),
            ("test-tube", "Browser end-to-end tests", "600+ tests cover the DB & business logic, but there is no browser E2E harness on the rendered UI.", REDH, "Greenfield"),
            ("key-round", "Secrets not yet rotated", "The build-time keys are still the running keys. Rotating all of them is a first-day, before-scale task.", AMBERH, "Day 1")]
    y = I(2.35)
    for i, (ic, t, d, dot, badge) in enumerate(rows):
        yy = y + i * I(0.86)
        rect(s, ML, yy, CW, I(0.74), fill=MIST if i % 2 == 0 else PAPER, line=None if i % 2 == 0 else LINE, rounded=True, radius=0.08)
        icon_disc(s, ic, ML + I(0.18), yy + I(0.16), I(0.44), BR_T, "#4A35FF")
        text(s, ML + I(0.8), yy + I(0.1), I(5.4), I(0.35), t, font=HEAD, size=12, bold=True, color=INK, ls=1.02)
        text(s, ML + I(0.8), yy + I(0.4), I(8.3), I(0.35), d, size=9.7, color=MUT, ls=1.12)
        cc = {GREENH: GREEN, AMBERH: AMBER, REDH: RED}[dot]
        tt = {GREENH: GR_T, AMBERH: AM_T, REDH: RD_T}[dot]
        chip(s, SW - MR - I(1.7), yy + I(0.2), I(1.55), I(0.34), badge, fill=tt, color=cc, size=9)
    foot(s, 16)
    return s


# ============================================================ 17 ADOPTION RISK
def risk():
    s = slide()
    header(s, "04 · Where we are",
           [("The No.1 risk isn't the code — ", False), ("it's whether anyone uses it", True)],
           lead="The hardest problem is the first mile: getting a real case into the system at all. This shapes every product decision.",
           sect=(4, "WHERE WE ARE"))
    # two big evidence cards
    rect(s, ML, I(2.35), I(5.95), I(2.15), fill=RD_T, rounded=True, radius=0.08)
    text(s, ML + I(0.3), I(2.55), I(5.4), I(0.4), "The cautionary precedent", font=HEAD, size=13, bold=True, color=RED)
    text(s, ML + I(0.3), I(3.0), I(2.2), I(1.0), "25", font=HEAD, size=54, bold=True, color=RED, ls=0.9)
    text(s, ML + I(2.3), I(3.05), I(3.4), I(1.2), "monthly requests to Jaipur's earlier “Madad Setu” portal, against ~350 expected. Adoption, not launch, is the goal.", size=10.5, color=INK, ls=1.25)
    rect(s, ML + I(6.15), I(2.35), I(5.95), I(2.15), fill=AM_T, rounded=True, radius=0.08)
    text(s, ML + I(6.45), I(2.55), I(5.4), I(0.4), "Our own pilot, ten days in", font=HEAD, size=13, bold=True, color=AMBER)
    text(s, ML + I(6.45), I(3.0), I(2.2), I(1.0), "0", font=HEAD, size=54, bold=True, color=AMBER, ls=0.9)
    text(s, ML + I(8.0), I(3.05), I(3.9), I(1.2), "live cases entered organically by an IO after training. Officers are 40–50, trained on e-DAR; a new portal reads as too much.", size=10.5, color=INK, ls=1.25)
    # what follows
    text(s, ML, I(4.75), I(12), I(0.3), "WHAT THIS MEANS FOR THE BUILD", font=HEAD, size=9, bold=True, color=MUT, tracking=1.6)
    rows = [("scan-line", "The first mile belongs in e-DAR / CCTNS", "Cases should auto-create from the FIR record police already file — not a third data-entry screen. (A separate NIC / MoRTH / state-police lobbying track; SCRB has agreed in principle.)"),
            ("smartphone", "Anything an officer touches installs like an app", "Home-screen icon, no browser chrome, minimal police-facing scope — because every thana asked “is this a mobile app?”")]
    y = I(5.15)
    for i, (ic, t, d) in enumerate(rows):
        tint, col = PAL[i % 4]
        irow(s, ML, y + i * I(0.85), I(12.0), ic, t, d, tint, col, d=I(0.44), tsize=12, dsize=10.3)
    foot(s, 17)
    return s


# ============================================================ 18 MANDATE
def mandate():
    s = slide()
    header(s, "05 · Where you come in",
           [("The mandate: ", False), ("a production-grade rebuild", True)],
           lead="The pilot proved the flow. Now an engineering squad hardens it for state and national volume — new districts by configuration, not code; multi-state ready.",
           sect=(5, "WHERE YOU COME IN"))
    tasks = [("search-check", "1 · Review & audit", "Full functionality review and an external security + scalability pass on the current codebase. Rotate all secrets on day one.", GR_T, "#0A9955"),
             ("boxes", "2 · Build for scale", "The production system: 33 districts and 900+ police stations in Rajasthan, new districts onboarded by config, multi-state ready.", BR_T, "#4A35FF"),
             ("wrench", "3 · Close the gaps", "Finish the known-incomplete pieces — settlement / disbursement console, AI document-check loop, realtime notifications.", AM_T, "#E58900")]
    tw = I(3.9); gx = I(0.16)
    for i, (ic, t, d, tint, col) in enumerate(tasks):
        x = ML + i * (tw + gx)
        rect(s, x, I(2.4), tw, I(2.05), fill=PAPER, line=LINE, rounded=True, radius=0.08)
        icon_disc(s, ic, x + I(0.22), I(2.62), I(0.54), tint, col)
        text(s, x + I(0.22), I(3.3), tw - I(0.44), I(0.35), t, font=HEAD, size=13, bold=True, color=INK)
        text(s, x + I(0.22), I(3.7), tw - I(0.44), I(0.7), d, size=10, color=MUT, ls=1.22)
    text(s, ML, I(4.75), I(12), I(0.3), "PRINCIPLES WE BUILD BY", font=HEAD, size=9, bold=True, color=MUT, tracking=1.6)
    pr = [("cloud", "Portable to government infra", "Prefer open, standard components; no lock-in that makes migration hard later."),
          ("boxes", "Modular by design", "Each module works on its own; a super admin connects & configures per deployment."),
          ("shield-check", "Security lives in the database", "Row-level security, jurisdiction scoping, full audit — no admin back door."),
          ("languages", "Hindi-first, cheap-phone-first", "Full Hindi/English parity; family side works on the cheapest phone; officer side is a PWA.")]
    for i, (ic, t, d) in enumerate(pr):
        r, c = divmod(i, 2)
        x = ML + c * I(6.1); yy = I(5.15) + r * I(0.82)
        icon_disc(s, ic, x, yy, I(0.4), BR_T, "#4A35FF")
        text(s, x + I(0.56), yy - I(0.03), I(2.6), I(0.35), t, font=HEAD, size=10.5, bold=True, color=INK)
        text(s, x + I(0.56) + I(2.55), yy - I(0.03), I(2.9), I(0.7), d, size=9, color=MUT, ls=1.14)
    foot(s, 18)
    return s


# ============================================================ 19 KEEP vs OPEN (where you help)
def workstreams():
    s = slide()
    header(s, "05 · Where you come in",
           [("What to keep, ", False), ("and where we need your hands", True)],
           lead="Treat the framework and UI kit as choices, not commitments — cost any migration honestly. But the model below is load-bearing and legal; keep it.",
           sect=(5, "WHERE YOU COME IN"))
    # KEEP column
    kx = ML; kw = I(5.3)
    rect(s, kx, I(2.35), kw, I(4.4), fill=GR_T, rounded=True, radius=0.07)
    text(s, kx + I(0.28), I(2.55), kw - I(0.5), I(0.35), "KEEP — survives the rebuild", font=HEAD, size=12, bold=True, color=GREEN, tracking=0.5)
    keep = [("shield-check", "Database-as-boundary", "RLS on every table, authored once — not duplicated in query code."),
            ("network", "Jurisdiction + role claims", "Verified JWT claims, two-check delegated provisioning."),
            ("scroll-text", "Append-only audit ledger", "Every transition, immutable — a legal requirement."),
            ("file-signature", "OTP-signed statutory forms", "Form II / III signing tied to the officer's phone.")]
    yy = I(3.05)
    for ic, t, d in keep:
        icon_disc(s, ic, kx + I(0.28), yy, I(0.44), PAPER, "#0A9955")
        text(s, kx + I(0.86), yy - I(0.02), kw - I(1.1), I(0.3), t, font=HEAD, size=11.5, bold=True, color=INK)
        text(s, kx + I(0.86), yy + I(0.28), kw - I(1.1), I(0.5), d, size=9.5, color=MUT, ls=1.15)
        yy += I(0.9)
    # OPEN column
    ox = ML + I(5.6); ow = SW - MR - ox
    rect(s, ox, I(2.35), ow, I(4.4), fill=PAPER, line=LINE, rounded=True, radius=0.07)
    text(s, ox + I(0.28), I(2.55), ow - I(0.5), I(0.35), "OPEN — where you come in", font=HEAD, size=12, bold=True, color=BRAND, tracking=0.5)
    openw = [("search-check", "Security audit + secrets rotation", "Day-one external pen-test; rotate every key.", AMBERH),
             ("gauge", "Scale & load", "Find where one app + Postgres/RLS bends at state volume.", REDH),
             ("banknote", "Settlement / disbursement console", "The clearest greenfield build.", REDH),
             ("scan-text", "AI document-check loop", "Activate the scaffolded vision pipeline.", REDH),
             ("bell", "Realtime notifications", "Wire transport to the notification shell.", AMBERH),
             ("boxes", "Multi-state onboarding-by-config", "Harden the workbook / provisioning path.", AMBERH)]
    yy = I(3.02)
    for ic, t, d, dot in openw:
        icon_disc(s, ic, ox + I(0.28), yy, I(0.4), BR_T, "#4A35FF")
        icon(s, "circle", ox + ow - I(0.4), yy + I(0.06), I(0.16), dot)
        text(s, ox + I(0.82), yy - I(0.03), ow - I(1.3), I(0.3), t, font=HEAD, size=11, bold=True, color=INK)
        text(s, ox + I(0.82), yy + I(0.26), ow - I(1.3), I(0.3), d, size=9, color=MUT, ls=1.12)
        yy += I(0.62)
    foot(s, 19)
    return s


# ============================================================ 20 HOW WE WORK
def howwework():
    s = slide()
    header(s, "05 · Where you come in",
           [("How we'll work together — ", False), ("the live pilot never breaks", True)],
           lead="Build the new system on a separate project and database; cut over only when it's green. The Jaipur pilot keeps running on the current build for the next couple of months.",
           sect=(5, "WHERE YOU COME IN"))
    rows = [("split", "Build on a separate project / DB", "A throwaway Supabase + separate Vercel project — never the production database. Public demo + real PII is unacceptable."),
            ("user-round-cog", "A /demo role-switcher for reviews", "Signs in as each role via a server-side known password so RLS still fully applies — no auth bypass — with all real sends hard-disabled."),
            ("git-pull-request", "Clean module split, continuous integration", "Each module ships and verifies on its own. No big-bang merge at the end — the timeline is two weeks and tight."),
            ("shield", "The pilot stays stable", "The current build keeps serving 6 thanas + families on WhatsApp while we rebuild. Cut over only when the new system is proven green.")]
    y = I(2.4)
    for i, (ic, t, d) in enumerate(rows):
        tint, col = PAL[i % 4]
        irow(s, ML, y + i * I(0.9), I(12.0), ic, t, d, tint, col, d=I(0.46), tsize=12.5, dsize=10.5)
    rect(s, ML, I(6.1), CW, I(0.66), fill=AM_T, rounded=True, radius=0.14)
    text(s, ML + I(0.25), I(6.22), CW - I(0.5), I(0.45),
         [("Two weeks is aggressive. ", {'bold': True, 'color': AMBER}),
          ("The way we hit it is a clean split and CI from day one — not a heroic merge at the end. Flag scope risk early and often.", {'color': INK})],
         size=10.5, ls=1.2)
    foot(s, 20)
    return s


# ============================================================ 21 FIRST WEEK
def firstweek():
    s = slide()
    header(s, "05 · Where you come in",
           [("Your first week — ", False), ("come back with a plan, not a rewrite", True)],
           lead="A concrete on-ramp. The goal by the end of week one is a shared understanding and a proposed approach we align on.",
           sect=(5, "WHERE YOU COME IN"))
    steps = [("play", "Get oriented", "Walk the live demo; read the repo's README, then the security audit and the squad PRD."),
             ("terminal", "Run it locally", "Stand it up and walk one case end to end — register, upload, verify, sanction, pay."),
             ("shield-alert", "Audit it", "A full external security + scalability pass: pen-test, load assessment, multi-tenant review."),
             ("key-round", "Rotate the secrets", "Day-one hygiene: no build-time key stays a running key."),
             ("clipboard-list", "Propose the plan", "Come back with a rebuild approach and a module split — challenge anything that looks wrong.")]
    y = I(2.35)
    for i, (ic, t, d) in enumerate(steps):
        yy = y + i * I(0.72)
        num_disc(s, ML, yy, I(0.46), i + 1)
        icon_disc(s, ic, ML + I(0.66), yy + I(0.02), I(0.42), BR_T, "#4A35FF")
        text(s, ML + I(1.3), yy - I(0.02), I(4.4), I(0.4), t, font=HEAD, size=12.5, bold=True, color=INK, anchor=MSO_ANCHOR.MIDDLE)
        text(s, ML + I(5.0), yy - I(0.02), I(7.1), I(0.6), d, size=10.5, color=MUT, ls=1.18, anchor=MSO_ANCHOR.MIDDLE)
    rect(s, ML, I(6.05), CW, I(0.7), fill=MIST, rounded=True, radius=0.12)
    text(s, ML + I(0.25), I(6.18), CW - I(0.5), I(0.45),
         [("Two asks before our call: ", {'bold': True, 'color': BRAND}),
          ("skim the portal, PRD and this brief and bring questions; and fill the availability form so we know where each of you will plug in.", {'color': INK})],
         size=10.5, ls=1.2)
    foot(s, 21)
    return s


# ============================================================ 22 CLOSE
def close():
    s = slide()
    r = s.shapes.add_shape(1, 0, 0, SW, SH)
    r.fill.solid(); r.fill.fore_color.rgb = BRAND; r.line.fill.background(); r.shadow.inherit = False
    from cfi_helpers import _strip_style as _ss
    _ss(r)
    s.shapes.add_picture(LOGO_WHITE, ML, I(0.55), width=I(1.95))
    text(s, SW - MR - I(4.0), I(0.62), I(4.0), I(0.3), "TEAM INDUCTION BRIEF", font=HEAD, size=9, bold=True, color=LAVW, tracking=2.0, align=PP_ALIGN.RIGHT)
    text(s, ML, I(2.3), I(11.8), I(1.4),
         [("A family's ₹2 lakh, and a national benchmark for ", {'color': PAPER}), ("AI that actually reaches people", {'color': RGBColor(0xC8, 0xC0, 0xFF)}), (".", {'color': PAPER})],
         font=HEAD, size=30, bold=True, ls=1.18)
    text(s, ML, I(4.15), I(11.5), I(0.8),
         "The scheme already owes the money. SAHAJ is how it reaches the family — reliably, at scale, with the trail to prove it. Thank you for building it with us.",
         size=13.5, color=RGBColor(0xE6, 0xE2, 0xFF), ls=1.4)
    hline(s, ML, I(5.5), I(0.7), color=LAVW, wt=2.5)
    text(s, ML, I(5.75), I(11.5), I(0.4), "Let's connect at 3:30 PM. Bring questions.", font=HEAD, size=14, bold=True, color=PAPER)
    text(s, ML, I(6.85), I(11.5), I(0.3),
         "Akhtar Hussain  ·  Mission Lead, Crashfree India  ·  akhtar@crashfreeindia.org  ·  crashfreeindia.org", size=10, color=RGBColor(0xC8, 0xC0, 0xFF))
    return s


# ---- build
cover(); letter(); agenda()
problem(); whatis(); whois()
forms(); roles(); flow(); claimant(); surfaces()
architecture(); security(); modular()
status(); gaps(); risk()
mandate(); workstreams(); howwework(); firstweek(); close()
save("CFI_SAHAJ-Team-Induction-Brief_v1_2026-09-21.pptx")

# Crashfree India — NRSB WG-2 and WG-5 application decks (simple style, 50+ govt audience)
import os
import cfi_helpers as H
from cfi_helpers import (BRAND, BRAND_LITE, WHITE, DARK, MUTED, BORDER, LAV, LAV_DK,
                         HEAD, BODY, SLIDE_W, SLIDE_H, M_L, CONTENT_W,
                         rect, circle, hline, text, icon, logo)
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

A  = "/tmp/claude-0/-home-user-personal-random-builds/7ed0a560-5095-5ea6-83c6-d690a2a75997/scratchpad/assets"
V3 = os.path.join(A, "v3")
BUILD = os.path.dirname(os.path.abspath(__file__))
BLUE_HEX = "#4A35FF"; WHITE_HEX = "#FFFFFF"
BRAND_MID = RGBColor(0x5A,0x46,0xFF)

def pic_ar(path):
    from PIL import Image as _I
    im = _I.open(path); return im.width/im.height

def reset_prs():
    H.prs = Presentation(); H.prs.slide_width = SLIDE_W; H.prs.slide_height = SLIDE_H
    H.blank = H.prs.slide_layouts[6]

def new_slide(bg=WHITE):
    s = H.prs.slides.add_slide(H.blank)
    r = s.shapes.add_shape(1, 0, 0, SLIDE_W, SLIDE_H)
    r.fill.solid(); r.fill.fore_color.rgb = bg; r.line.fill.background(); r.shadow.inherit = False
    H._strip_style(r)
    return s

def pic(slide, path, x, y, w=None, h=None, border=True):
    if border:
        from PIL import Image as _I
        im = _I.open(path); ar = im.width/im.height
        ww = w if w else (h*ar if h else None)
        hh = h if h else (w/ar if w else None)
        rect(slide, x-Inches(0.04), y-Inches(0.04), ww+Inches(0.08), hh+Inches(0.08), WHITE, line=BORDER)
    return slide.shapes.add_picture(path, x, y, width=w, height=h)

def sh(s, kicker, title, lead=None):
    """Simple header: small blue kicker, single-line dark title (26pt), optional grey lead."""
    text(s, M_L, Inches(0.5), Inches(12), Inches(0.3), kicker, font=HEAD, size=11, bold=True, color=BRAND, tracking=0.8)
    text(s, M_L, Inches(0.86), Inches(12), Inches(0.65), title, font=HEAD, size=25, bold=True, color=DARK, ls=1.08)
    y = Inches(1.55)
    if lead:
        text(s, M_L, Inches(1.55), Inches(11.9), Inches(0.55), lead, font=BODY, size=12.5, color=MUTED, ls=1.4)
        y = Inches(2.15)
    return y

def foot(s, idx, total, wg):
    text(s, M_L, Inches(7.12), Inches(8), Inches(0.3), f"Crashfree India · NRSB Working Group {wg} Application",
         font=BODY, size=9, color=MUTED)
    text(s, Inches(11.4), Inches(7.12), Inches(1.4), Inches(0.3), f"{idx} / {total}",
         font=BODY, size=9, color=MUTED, align=PP_ALIGN.RIGHT)

def stat_tile(s, x, y, w, num, lab, h=Inches(1.0)):
    rect(s, x, y, w, h, BRAND_LITE, rounded=True)
    text(s, x, y+Inches(0.1), w, Inches(0.45), num, font=HEAD, size=19, bold=True, color=BRAND, align=PP_ALIGN.CENTER)
    text(s, x+Inches(0.1), y+Inches(0.56), w-Inches(0.2), Inches(0.4), lab, font=BODY, size=9.5, color=DARK,
         align=PP_ALIGN.CENTER, ls=1.15)

def bullet(s, x, y, w, txt, size=12, icn=None, color=DARK):
    if icn:
        circle(s, x, y+Inches(0.0), Inches(0.34), BRAND_LITE)
        icon(s, icn, x+Inches(0.07), y+Inches(0.07), Inches(0.2), BLUE_HEX)
        text(s, x+Inches(0.5), y+Inches(0.02), w-Inches(0.5), Inches(0.5), txt, font=BODY, size=size, color=color, ls=1.3)
    else:
        circle(s, x+Inches(0.02), y+Inches(0.09), Inches(0.1), BRAND)
        text(s, x+Inches(0.28), y, w-Inches(0.3), Inches(0.5), txt, font=BODY, size=size, color=color, ls=1.3)

# ============================================================================
# COMMON FRONT (slides 1-6)
# ============================================================================
def common_front(wg, wg_title, total):
    # ---- 1 COVER
    s = new_slide(WHITE)
    logo(s, M_L, Inches(0.6), Inches(2.9))
    rect(s, 0, Inches(2.6), SLIDE_W, Inches(0.06), BRAND)
    text(s, M_L, Inches(3.0), Inches(11.9), Inches(0.4), "Expression of Interest", font=HEAD, size=16,
         bold=True, color=MUTED)
    text(s, M_L, Inches(3.45), Inches(11.9), Inches(1.3),
         f"Working Group {wg}:\n{wg_title}", font=HEAD, size=28, bold=True, color=DARK, ls=1.18)
    text(s, M_L, Inches(5.15), Inches(11.9), Inches(0.4),
         "Submitted to the National Road Safety Board", font=BODY, size=14, color=DARK)
    text(s, M_L, Inches(5.6), Inches(11.9), Inches(0.4),
         "by Crashfree India (Vision Zero Trust) · August 2026", font=BODY, size=12, color=MUTED)
    imp = ["1M+ people reached", "18 cities", "25+ authority approvals", "4 district committees"]
    ix = M_L
    for t_ in imp:
        wd = Inches(0.45 + 0.105*len(t_))
        rect(s, ix, Inches(6.2), wd, Inches(0.42), BRAND_LITE, rounded=True)
        text(s, ix, Inches(6.2), wd, Inches(0.42), t_, font=HEAD, size=10, bold=True, color=BRAND,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        ix += wd + Inches(0.15)
    text(s, M_L, Inches(6.85), Inches(11), Inches(0.3), "crashfreeindia.org · helpdesk@crashfreeindia.org",
         font=BODY, size=10, color=MUTED)

    # ---- 2 ABOUT
    s = new_slide(WHITE)
    y = sh(s, "ABOUT US", "Crashfree India: a nonprofit working for safer roads",
           "Registered as Vision Zero Trust. Co-founded by Cars24 and the Indian Road Safety Council, June 2025. We follow the global Vision Zero principle: no loss of life on the road is acceptable.")
    rows = [
        ("search-check", "Evidence first", "Structured field audits, file reviews and research to official standards — not opinion."),
        ("landmark", "Institutional collaboration", "We work through PWDs, NHAI, transport departments, police and District Road Safety Committees."),
        ("users-round", "Youth-led capacity", "Trained student teams from IITs, NITs and SPAs add auditing hands the system needs."),
        ("monitor-check", "Technology for follow-through", "Public dashboards track every recommendation from submission to completion."),
    ]
    yy = Inches(2.5)
    for icn, t1, t2 in rows:
        circle(s, M_L, yy, Inches(0.44), BRAND_LITE)
        icon(s, icn, M_L+Inches(0.1), yy+Inches(0.1), Inches(0.24), BLUE_HEX)
        text(s, M_L+Inches(0.65), yy-Inches(0.02), Inches(3.6), Inches(0.6), t1, font=HEAD, size=13.5, bold=True, color=DARK)
        text(s, M_L+Inches(4.4), yy+Inches(0.0), Inches(7.5), Inches(0.6), t2, font=BODY, size=12, color=MUTED, ls=1.3)
        yy += Inches(0.82)
    rect(s, M_L, Inches(6.0), CONTENT_W, Inches(0.6), BRAND_LITE, rounded=True)
    text(s, M_L+Inches(0.3), Inches(6.0), CONTENT_W-Inches(0.6), Inches(0.6),
         "Backed by a US$3 million, three-year commitment from Cars24 — with programmes, not overheads, receiving 71% of the budget.",
         font=HEAD, size=12, bold=True, color=BRAND, anchor=MSO_ANCHOR.MIDDLE)
    foot(s, 2, total, wg)

    # ---- 3 WORK AT A GLANCE
    s = new_slide(WHITE)
    y = sh(s, "OUR WORK", "One year of work across four connected areas",
           "Each area strengthens the others — audits create data, data supports policy, policy guides the field.")
    quads = [
        ("hard-hat", "Project Rakshak", "Youth-led road safety audits to IRC / MoRTH standards; 31 sites, 25+ approvals, 15 implementations underway.", "iv_indore_footpath"),
        ("scan-line", "SATARK & enforcement technology", "AI number-plate platform built with traffic police — 3,00,000+ vehicles screened in Jaipur & Bengaluru.", None),
        ("hand-helping", "Post-crash support & compensation", "'Justice Unserved' research, Aasha chatbot, hospital helpdesks, district committee integration, Rajasthan portal design.", None),
        ("bar-chart-3", "Open data & public education", "Four public data platforms; comics, Hindi guides and a pre-hospital care primer.", None),
    ]
    cw = Inches(5.85); ch = Inches(1.9); gap = Inches(0.22)
    for i,(icn,t1,t2,img) in enumerate(quads):
        x = M_L + (i%2)*(cw+gap); yq = Inches(2.5) + (i//2)*(ch+Inches(0.2))
        rect(s, x, yq, cw, ch, WHITE, line=BORDER, rounded=True)
        circle(s, x+Inches(0.25), yq+Inches(0.25), Inches(0.5), BRAND_LITE)
        icon(s, icn, x+Inches(0.36), yq+Inches(0.36), Inches(0.28), BLUE_HEX)
        text(s, x+Inches(0.92), yq+Inches(0.28), cw-Inches(1.15), Inches(0.35), t1, font=HEAD, size=14, bold=True, color=DARK)
        text(s, x+Inches(0.92), yq+Inches(0.72), cw-Inches(1.15), Inches(1.0), t2, font=BODY, size=11, color=MUTED, ls=1.3)
    foot(s, 3, total, wg)

    # ---- 4 TECHNOLOGY
    s = new_slide(WHITE)
    y = sh(s, "OUR TECHNOLOGY", "We build serious public technology — and keep it open",
           "Self-updating platforms that make road-safety work transparent, measurable and usable by government.")
    try:
        db = os.path.join(V3, "new", "dashboard.png")
        pic(s, db, M_L, Inches(2.4), w=Inches(5.9))
        text(s, M_L, Inches(2.4)+Inches(5.9)/pic_ar(db)+Inches(0.1), Inches(5.9), Inches(0.3),
             "Project Rakshak public dashboard — every site, authority and status visible.",
             font=BODY, size=10, color=MUTED, italic=True)
    except Exception as e: print("nrsb dash", e)
    tech = [
        ("Rakshak accountability portal", "rakshak.crashfreeindia.org — submission → committee ratification → completion"),
        ("SATARK enforcement platform", "ANPR + national vehicle records, officer app and public compliance billboards"),
        ("Aasha", "24/7 multilingual AI guide for crash victims, on WhatsApp and voice"),
        ("Compensation Calculator", "Free estimates on Supreme Court principles (Sarla Verma, Pranay Sethi)"),
        ("National crash data dashboard", "MoRTH statistics productised: report cards for 36 states, 50 cities"),
        ("Road defect repository", "AI reads local news in 13 languages across 146 districts; hazards mapped publicly"),
    ]
    ty = Inches(2.35)
    for t1, t2 in tech:
        text(s, Inches(7.0), ty, Inches(5.6), Inches(0.3),
             [(t1+"  —  ", {'font':HEAD,'size':11.5,'bold':True,'color':DARK}),
              (t2, {'font':BODY,'size':10.5,'color':MUTED})], ls=1.25)
        ty += Inches(0.72)
    foot(s, 4, total, wg)

    # ---- 5 PEOPLE
    s = new_slide(WHITE)
    y = sh(s, "OUR PEOPLE", "Academic leadership, senior advisors and a multidisciplinary team")
    boa = [
        ("gtiwari", "Prof. Geetam Tiwari", "Emeritus Professor & Chair, TRIP Centre, IIT Delhi · Member, IRC H-7 Committee on Road Safety Audit"),
        (None, "Piyush Tewari", "Founder & CEO, SaveLIFE Foundation · Architect of the Good Samaritan Law"),
    ]
    bx = M_L
    for head, nm, ti in boa:
        rect(s, bx, Inches(2.05), Inches(5.85), Inches(1.15), WHITE, line=BORDER, rounded=True)
        hp = os.path.join(V3, "heads", f"{head}.png") if head else None
        if hp and os.path.exists(hp):
            s.shapes.add_picture(hp, bx+Inches(0.22), Inches(2.22), width=Inches(0.8), height=Inches(0.8))
        else:
            circle(s, bx+Inches(0.22), Inches(2.22), Inches(0.8), BRAND)
            text(s, bx+Inches(0.22), Inches(2.22), Inches(0.8), Inches(0.8), "".join(w[0] for w in nm.split()[:2]),
                 font=HEAD, size=18, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(s, bx+Inches(1.2), Inches(2.22), Inches(4.5), Inches(0.3), nm, font=HEAD, size=13.5, bold=True, color=DARK)
        text(s, bx+Inches(1.2), Inches(2.55), Inches(4.5), Inches(0.6), ti, font=BODY, size=10, color=MUTED, ls=1.25)
        bx += Inches(6.07)
    text(s, M_L, Inches(3.45), Inches(6), Inches(0.3), "BOARD OF ADVISORS", font=HEAD, size=9.5, bold=True,
         color=MUTED, tracking=1.2)
    text(s, M_L, Inches(3.9), Inches(11.9), Inches(0.35),
         "Guided also by Dr. Richa Ahuja (IIT Kharagpur) and an expert network spanning CSIR-CRRI, IRF India, CoERS IIT Madras, IISc, IIT Bombay, IIT Roorkee, IIT Kanpur and the Schools of Planning & Architecture.",
         font=BODY, size=11.5, color=MUTED, ls=1.35)
    trows = [
        ("Trustees", "Amar Srivastava (Founder, Indian Road Safety Council) · Deepanshu Gupta (Founder, IRSC) · Gajendra Jangid (Co-founder, Cars24)"),
        ("Full-time team", "Educated at IIT Delhi, NALSAR & Delhi University (law), TISS (development studies), HKUST — experience across engineering, law, policy, psychology and product"),
        ("Field strength", "75+ road-engineering interns and 31 student audit teams across 18 cities"),
        ("Goodwill Ambassador", "MS Dhoni — voice for youth participation and safer school zones"),
    ]
    ty = Inches(4.55)
    for t1, t2 in trows:
        text(s, M_L, ty, Inches(2.3), Inches(0.3), t1, font=HEAD, size=11.5, bold=True, color=BRAND)
        text(s, M_L+Inches(2.5), ty, Inches(9.4), Inches(0.5), t2, font=BODY, size=10.5, color=DARK, ls=1.25)
        ty += Inches(0.58)
    foot(s, 5, total, wg)

# ============================================================================
# COMMON BACK (recognition + closing)
# ============================================================================
def common_back(wg, total, idx0, offers_title, offers):
    # OFFERS
    s = new_slide(WHITE)
    y = sh(s, "OUR CONTRIBUTION", offers_title)
    yy = Inches(2.15)
    for i,(t1,t2) in enumerate(offers):
        rect(s, M_L, yy, CONTENT_W, Inches(1.02), WHITE, line=BORDER, rounded=True)
        circle(s, M_L+Inches(0.25), yy+Inches(0.26), Inches(0.5), BRAND)
        text(s, M_L+Inches(0.25), yy+Inches(0.26), Inches(0.5), Inches(0.5), str(i+1), font=HEAD, size=15,
             bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(s, M_L+Inches(1.0), yy+Inches(0.14), Inches(3.6), Inches(0.7), t1, font=HEAD, size=12.5, bold=True, color=DARK, ls=1.15)
        text(s, M_L+Inches(4.8), yy+Inches(0.14), Inches(7.3), Inches(0.8), t2, font=BODY, size=10.5, color=MUTED, ls=1.28)
        yy += Inches(1.14)
    foot(s, idx0, total, wg)

    # RECOGNITION
    s = new_slide(WHITE)
    y = sh(s, "RECOGNITION", "A young organisation the ecosystem already engages with")
    try:
        st_ = os.path.join(V3, "new", "comp_image6.jpeg")
        pic(s, st_, M_L, Inches(2.2), w=Inches(5.6))
        text(s, M_L, Inches(2.2)+Inches(5.6)/pic_ar(st_)+Inches(0.1), Inches(5.6), Inches(0.3),
             "National Road Safety Implementation Forum, IIT Delhi — April 2026.",
             font=BODY, size=10, color=MUTED, italic=True)
    except Exception as e: print("recog", e)
    rows = [
        ("National forum at IIT Delhi", "60+ experts; MoRTH, WHO, UNICEF, IRF and CSIR-CRRI participation; hosted with the TRIP Centre"),
        ("MS Dhoni, Goodwill Ambassador", "announced at the forum; covered by Business Standard, The Tribune and The Wire"),
        ("Research in national press", "'Justice Unserved' covered by Deccan Herald, Economic Times, Fortune India, IndiaSpend, Moneycontrol, Scroll.in and The Wire"),
        ("Government partnerships", "MoUs with Jaipur Traffic Police & Gurugram Police; formal tasking by the South-West Delhi DRSC; Rajasthan Transport Department engagement"),
    ]
    ty = Inches(2.3)
    for t1, t2 in rows:
        text(s, Inches(6.7), ty, Inches(5.9), Inches(0.7),
             [(t1+"  —  ", {'font':HEAD,'size':11.5,'bold':True,'color':DARK}),
              (t2, {'font':BODY,'size':10.5,'color':MUTED})], ls=1.3)
        ty += Inches(1.05)
    foot(s, idx0+1, total, wg)

    # CLOSE
    s = new_slide(BRAND)
    logo(s, M_L, Inches(0.6), Inches(2.3), dark=True)
    text(s, M_L, Inches(2.4), Inches(11.9), Inches(1.2),
         f"We would be honoured to contribute to\nWorking Group {wg}.", font=HEAD, size=30, bold=True, color=WHITE, ls=1.2)
    text(s, M_L, Inches(4.0), Inches(11.5), Inches(0.8),
         "Our evidence, our district relationships, our technology and our expert network are available to the Board — in whichever form is most useful.",
         font=BODY, size=13.5, color=LAV, ls=1.4)
    hline(s, M_L, Inches(5.1), Inches(11.9), color=LAV_DK)
    contact = [("globe", "crashfreeindia.org"), ("mail", "helpdesk@crashfreeindia.org"),
               ("bar-chart-3", "Live portal: rakshak.crashfreeindia.org")]
    cy2 = Inches(5.45)
    for icn, t_ in contact:
        icon(s, icn, M_L, cy2+Inches(0.01), Inches(0.26), "#C8C0FF")
        text(s, M_L+Inches(0.42), cy2, Inches(6.0), Inches(0.3), t_, font=BODY, size=12.5, color=WHITE)
        cy2 += Inches(0.48)
    text(s, M_L, Inches(7.0), Inches(11.9), Inches(0.3),
         "Crashfree India · A Cars24 Commitment · operated by Vision Zero Trust, New Delhi", font=BODY, size=10, color=LAV)

# ============================================================================
# WG-2 BODY
# ============================================================================
def wg2_body(total):
    wg = 2
    # 6 MANDATE
    s = new_slide(BRAND_LITE)
    y = sh(s, "WORKING GROUP 2", "The mandate, and where we align",
           "Safe roads, speed management and the protection of vulnerable road users.")
    mand = ["Road design", "Black spots", "Speed limits", "School zones", "Pedestrians", "Cyclists"]
    mx = M_L
    for m in mand:
        wd = Inches(0.5 + 0.115*len(m))
        rect(s, mx, Inches(2.3), wd, Inches(0.48), WHITE, line=BORDER, rounded=True)
        text(s, mx, Inches(2.3), wd, Inches(0.48), m, font=HEAD, size=11.5, bold=True, color=DARK,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        mx += wd + Inches(0.18)
    al = [
        ("Black-spot rectification", "31 sites audited in year one — 11 official blackspots among them — with 25+ authority approvals and 15 implementations underway."),
        ("Road design to standard", "Every audit anchored in IRC codes and MoRTH checklists, guided by a member of the IRC H-7 Committee on Road Safety Audit."),
        ("Speed & school zones", "Speed-calming measures in approved designs; college-led school-zone screening under exploration."),
        ("Vulnerable road users", "Dedicated research on two-wheeler and gig-rider risk — the largest VRU category — plus pedestrian-first audit findings."),
    ]
    yy = Inches(3.2)
    for t1, t2 in al:
        rect(s, M_L, yy, CONTENT_W, Inches(0.82), WHITE, line=BORDER, rounded=True)
        text(s, M_L+Inches(0.28), yy+Inches(0.12), Inches(3.3), Inches(0.6), t1, font=HEAD, size=12.5, bold=True, color=BRAND, ls=1.15)
        text(s, M_L+Inches(3.9), yy+Inches(0.12), Inches(8.2), Inches(0.6), t2, font=BODY, size=11, color=DARK, ls=1.28)
        yy += Inches(0.94)
    foot(s, 6, total, wg)

    # 7 NATIONAL CONTEXT
    s = new_slide(WHITE)
    y = sh(s, "THE OPPORTUNITY", "Identification has outpaced rectification — capacity is the constraint",
           "The knowledge exists; the pipeline that turns identified risk into completed engineering needs more hands, and better tracking.")
    stat_tile(s, M_L, Inches(2.4), Inches(3.8), "13,795", "black spots identified nationally (MoRTH)", h=Inches(1.3))
    stat_tile(s, M_L+Inches(4.05), Inches(2.4), Inches(3.8), "5,036", "permanently rectified so far (Parliamentary Standing Committee, 2024)", h=Inches(1.3))
    stat_tile(s, M_L+Inches(8.1), Inches(2.4), Inches(3.8), "44", "certified Road Safety Auditors on the national registry (July 2026)", h=Inches(1.3))
    bullet(s, M_L, Inches(4.2), Inches(11.6),
           "Low-cost engineering measures — raised crossings, traffic calming, lighting, safer intersections — reduce crashes by 20–80% (IRF conference, Prof. Geetam Tiwari).", size=12, icn="trending-up")
    bullet(s, M_L, Inches(4.95), Inches(11.6),
           "Roughly 80% of crashes are attributed to 'human error', yet outcomes are shaped most by the road environment people operate in — which is fixable by design.", size=12, icn="route")
    rect(s, M_L, Inches(5.85), CONTENT_W, Inches(0.7), BRAND_LITE, rounded=True)
    text(s, M_L+Inches(0.3), Inches(5.85), CONTENT_W-Inches(0.6), Inches(0.7),
         "Project Rakshak was designed for precisely this constraint: trained, supervised auditing capacity that supports road-owning agencies — and tracks every fix to completion.",
         font=HEAD, size=12, bold=True, color=BRAND, anchor=MSO_ANCHOR.MIDDLE, ls=1.3)
    foot(s, 7, total, wg)

    # 8 RAKSHAK MODEL
    s = new_slide(WHITE)
    y = sh(s, "PROJECT RAKSHAK", "A structured, standards-based audit programme",
           "Conceptualised and guided by Prof. Geetam Tiwari (TRIP Centre, IIT Delhi) and Dr. Richa Ahuja (IIT Kharagpur).")
    phases = [("Phase 1 · Jul–Aug", "Research & problem identification", "Crash data, FIRs, RTIs, police records, site mapping"),
              ("Phase 2 · Aug–Sep", "Stakeholder engagement & audits", "Structured surveys; audits against IRC / MoRTH standards"),
              ("Phase 3 · Oct–Nov", "Analysis & solution development", "Benchmarking, costed intervention design"),
              ("Phase 4 · Nov onwards", "Reporting & authority engagement", "Consolidated reports to municipal bodies, PWDs, police")]
    px = M_L; pyy = Inches(2.45); pw = Inches(2.85); ph = Inches(1.9)
    for i,(d,t1,t2) in enumerate(phases):
        rect(s, px, pyy, pw, ph, WHITE, line=BORDER, rounded=True)
        text(s, px+Inches(0.2), pyy+Inches(0.16), pw-Inches(0.4), Inches(0.25), d, font=HEAD, size=9.5, bold=True, color=BRAND)
        text(s, px+Inches(0.2), pyy+Inches(0.46), pw-Inches(0.4), Inches(0.6), t1, font=HEAD, size=12.5, bold=True, color=DARK, ls=1.15)
        text(s, px+Inches(0.2), pyy+Inches(1.08), pw-Inches(0.4), Inches(0.7), t2, font=BODY, size=10, color=MUTED, ls=1.3)
        if i < 3:
            icon(s, "chevron-right", px+pw+Inches(0.01), pyy+ph/2-Inches(0.12), Inches(0.24), "#6A55FF")
        px += pw + Inches(0.26)
    bullet(s, M_L, Inches(4.75), Inches(11.6),
           "Teams train under expert masterclasses (Prof. Tiwari on the Safe System approach; Dr. S. Velmurugan, CSIR-CRRI, on the 5Es and IRC-131).", size=12, icn="graduation-cap")
    bullet(s, M_L, Inches(5.45), Inches(11.6),
           "Every recommendation is presented to the road-owning authority in its own format — and tracked publicly after submission.", size=12, icn="badge-check")
    foot(s, 8, total, wg)

    # 9 COHORT 1 RESULTS
    s = new_slide(WHITE)
    y = sh(s, "PROJECT RAKSHAK · YEAR ONE", "Cohort 1: a national footprint in the first year")
    funnel = [("120+", "locations screened"), ("31", "sites audited (11 official black spots)"),
              ("25+", "authority approvals"), ("15", "implementations underway")]
    fx = M_L; fy = Inches(2.15); fw = Inches(2.85); fh = Inches(1.35)
    for i,(num,lab) in enumerate(funnel):
        fill = BRAND if i==3 else BRAND_LITE
        tcol = WHITE if i==3 else BRAND
        lcol = LAV if i==3 else MUTED
        rect(s, fx, fy, fw, fh, fill, rounded=True)
        text(s, fx, fy+Inches(0.12), fw, Inches(0.55), num, font=HEAD, size=26, bold=True, color=tcol, align=PP_ALIGN.CENTER)
        text(s, fx+Inches(0.15), fy+Inches(0.72), fw-Inches(0.3), Inches(0.55), lab, font=BODY, size=10, color=lcol, align=PP_ALIGN.CENTER, ls=1.2)
        fx += fw + Inches(0.26)
    text(s, M_L, Inches(3.85), Inches(11.9), Inches(0.35),
         "31 student teams · 20 institutions including nine IITs · 900+ stakeholder surveys · guided by 8 mentors and independent evaluators",
         font=HEAD, size=12, bold=True, color=DARK)
    text(s, M_L, Inches(4.35), Inches(11.9), Inches(0.6),
         "North: Ropar, Dehradun, Roorkee, Delhi · Uttar Pradesh: Lucknow, Varanasi · East: Guwahati, Durgapur · West & Central: Surat, Indore, Mumbai, Nanded · South: Vijayawada, Guntur, Kozhikode, Chennai — among others.",
         font=BODY, size=11.5, color=MUTED, ls=1.4)
    try:
        pic(s, os.path.join(BUILD, "india_map.png"), Inches(9.8), Inches(4.3), h=Inches(2.5), border=False)
    except Exception as e: print(e)
    rect(s, M_L, Inches(5.9), Inches(8.6), Inches(0.75), BRAND_LITE, rounded=True)
    text(s, M_L+Inches(0.3), Inches(5.9), Inches(8.0), Inches(0.75),
         "Example: Tejaji Nagar Junction, Indore — an official black spot; redesign approved by CPWD and the Additional Collector's office.",
         font=HEAD, size=11.5, bold=True, color=BRAND, anchor=MSO_ANCHOR.MIDDLE, ls=1.3)
    foot(s, 9, total, wg)

    # 10 APPROVALS
    s = new_slide(BRAND_LITE)
    y = sh(s, "PROJECT RAKSHAK · THE PAPER TRAIL", "Authority approvals, in writing",
           "A sample of the 25+ approval and acknowledgement letters issued by public works and district authorities.")
    letters = [("Visioneers", "Tejaji Nagar, Indore"), ("Crashzero", "Kozhikode — PWD Kerala"),
               ("Pathrakshak", "Lucknow — PWD (UP)"), ("Vision_Zero_Squad", "Ropar — PWD (Punjab)")]
    lx = M_L; lyy = Inches(2.35); lh = Inches(3.6)
    for name, cap in letters:
        p_ = os.path.join(V3, "letters", f"{name}.png")
        try:
            ar = pic_ar(p_); lw = lh*ar
            pic(s, p_, lx, lyy, h=lh)
            text(s, lx, lyy+lh+Inches(0.1), lw+Inches(0.4), Inches(0.3), cap, font=BODY, size=9.5, color=MUTED)
            lx += lw + Inches(0.5)
        except Exception as e: print(e)
    text(s, M_L, Inches(6.5), Inches(11.9), Inches(0.3),
         "Approving authorities include PWD Kerala, PWD Uttar Pradesh, PWD Punjab, CPWD & the Additional Collector (Indore), ADDA Durgapur, R&B Andhra Pradesh and GCC Chennai.",
         font=BODY, size=10.5, color=DARK, ls=1.3)
    foot(s, 10, total, wg)

    # 11 IMPLEMENTATIONS
    s = new_slide(WHITE)
    y = sh(s, "PROJECT RAKSHAK · ON THE GROUND", "From approval to construction: implementations under way",
           "Parking, drainage, road markings, signage, footpaths and barricading — city by city.")
    ivs = [("iv_durgapur_parking", "Parking — Durgapur"), ("iv_durgapur_road", "Road works — Durgapur"),
           ("iv_guntur_drainage", "Drainage — Guntur"), ("iv_indore_barricade", "Barricading — Indore"),
           ("iv_indore_footpath", "Footpath — Indore"), ("iv_guntur_markings", "Markings — Guntur")]
    ix = M_L; iy = Inches(2.35); ihh = Inches(2.75)
    for f_, cap in ivs:
        p_ = os.path.join(V3, "new", f"{f_}.png")
        try:
            ar = pic_ar(p_); iw = ihh*ar
            pic(s, p_, ix, iy, h=ihh)
            text(s, ix, iy+ihh+Inches(0.1), iw+Inches(0.5), Inches(0.3), cap, font=BODY, size=9.5, color=MUTED)
            ix += iw + Inches(0.35)
        except Exception as e: print(e)
    rect(s, M_L, Inches(5.85), CONTENT_W, Inches(0.7), BRAND_LITE, rounded=True)
    text(s, M_L+Inches(0.3), Inches(5.85), CONTENT_W-Inches(0.6), Inches(0.7),
         "Estimated 20–50% crash reduction at treated sites once complete, based on WHO / iRAP evidence for these counter-measures — to be verified with before/after data.",
         font=HEAD, size=12, bold=True, color=BRAND, anchor=MSO_ANCHOR.MIDDLE, ls=1.3)
    foot(s, 11, total, wg)

    # 12 PORTAL
    s = new_slide(WHITE)
    y = sh(s, "PROJECT RAKSHAK · TRANSPARENCY", "A public portal that tracks every site to completion",
           "The design principle: transparency, not repeated follow-up, is what moves a recommendation from acknowledgement to action.")
    try:
        db = os.path.join(V3, "new", "dashboard.png")
        pic(s, db, M_L, Inches(2.35), w=Inches(6.9))
        text(s, M_L, Inches(2.35)+Inches(6.9)/pic_ar(db)+Inches(0.1), Inches(6.9), Inches(0.3),
             "rakshak.crashfreeindia.org — live public accountability portal.", font=BODY, size=10, color=MUTED, italic=True)
    except Exception as e: print(e)
    rows = [
        ("Every site tracked", "From submission through DRSC ratification to engineering completion — regardless of who audited it."),
        ("The PRAGATI parallel", "The PMO's PRAGATI platform resolved 7,150+ of ~7,700 flagged issues across ₹85 lakh crore of projects — public, real-time review works at national scale."),
        ("What the Board gains", "A live, honest read on how quickly road-owning agencies can act — evidence for capacity planning, not just compliance."),
    ]
    ty = Inches(2.5)
    for t1, t2 in rows:
        text(s, Inches(8.0), ty, Inches(4.6), Inches(1.1),
             [(t1+"  —  ", {'font':HEAD,'size':11.5,'bold':True,'color':DARK}),
              (t2, {'font':BODY,'size':10.5,'color':MUTED})], ls=1.3)
        ty += Inches(1.35)
    foot(s, 12, total, wg)

    # 13 THREE-TRACK MODEL
    s = new_slide(WHITE)
    y = sh(s, "PROJECT RAKSHAK · SCALING", "Why this model scales: three tracks, one standard",
           "Cohort 2 matches each road type to the right auditing capacity — reserving scarce certified auditors for the most complex sites.")
    hdr = ["Track", "Road type", "Implementing authority", "Who audits"]
    tab = [
        ("A — Institutional", "Urban arterials, in-town state highways, district roads", "ULB, State / District PWD", "IIT / NIT / SPA teams under expert mentors, IRC-aligned rubric"),
        ("B — NGO partners", "District & peri-urban corridors", "District PWD, ULB", "NGO field teams; desk-reviewed, share re-verified by CFI"),
        ("C — Certified RSAs", "National Highways, complex junctions", "NHAI Project Director, State PWD", "CSIR-CRRI-certified auditors; full IRC SP:88; usable by NHAI without rework"),
    ]
    colx = [M_L, M_L+Inches(2.3), M_L+Inches(5.3), M_L+Inches(7.9)]
    colw = [Inches(2.1), Inches(2.8), Inches(2.4), Inches(4.6)]
    rect(s, M_L, Inches(2.3), CONTENT_W, Inches(0.5), BRAND)
    for cx, cwd, h_ in zip(colx, colw, hdr):
        text(s, cx+Inches(0.15), Inches(2.3), cwd-Inches(0.2), Inches(0.5), h_, font=HEAD, size=11, bold=True,
             color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    ry = Inches(2.8)
    for i, row in enumerate(tab):
        rh = Inches(1.0)
        rect(s, M_L, ry, CONTENT_W, rh, BRAND_LITE if i%2==0 else WHITE, line=BORDER)
        for cx, cwd, val in zip(colx, colw, row):
            fz = 10.5 if cx==M_L else 10
            text(s, cx+Inches(0.15), ry+Inches(0.12), cwd-Inches(0.25), rh-Inches(0.2), val,
                 font=HEAD if cx==M_L else BODY, size=fz, bold=(cx==M_L), color=DARK if cx==M_L else MUTED, ls=1.25)
        ry += rh
    bullet(s, M_L, Inches(6.15), Inches(11.6),
           "Site selection in Cohort 2 is anchored to locations that district administrations, DRSCs and road-owning agencies have themselves flagged as priorities.",
           size=12, icn="map-pin")
    foot(s, 13, total, wg)

    # 14 INSTITUTIONALISATION
    s = new_slide(BRAND_LITE)
    y = sh(s, "PROJECT RAKSHAK · THE LONG VIEW", "Built to be institutionalised — not to depend on us",
           "Our role narrows over time to standard-setter and platform steward; the ecosystem runs the audits.")
    steps = [
        ("Today", "CFI runs cohorts, quality-controls audits and stewards the public portal"),
        ("Next", "Rakshak Audit Manual v1.0 codifies the method; universities field their own teams; NGOs run Track B directly"),
        ("Mature state", "States engage certified RSAs for Track C without CFI as intermediary; the portal remains the shared public record"),
    ]
    yy = Inches(2.3)
    for t1, t2 in steps:
        rect(s, M_L, yy, CONTENT_W, Inches(0.95), WHITE, line=BORDER, rounded=True)
        text(s, M_L+Inches(0.3), yy+Inches(0.12), Inches(2.2), Inches(0.6), t1, font=HEAD, size=13, bold=True, color=BRAND)
        text(s, M_L+Inches(2.8), yy+Inches(0.12), Inches(9.3), Inches(0.7), t2, font=BODY, size=11.5, color=DARK, ls=1.3)
        yy += Inches(1.08)
    bullet(s, M_L, Inches(5.75), Inches(11.6),
           "The same standards-anchored approach is being explored for school-zone safety — college-led screening under the same public-tracking discipline.",
           size=12, icn="school")
    foot(s, 14, total, wg)

    # 15 EXPERT BENCH
    s = new_slide(WHITE)
    y = sh(s, "OUR NETWORK", "The technical bench behind the audits",
           "Mentors, evaluators and forum experts who review and strengthen every cohort's work.")
    bench = [("gtiwari", "Prof. Geetam Tiwari", "TRIP Centre, IIT Delhi · IRC H-7"),
             (None, "Dr. Richa Ahuja", "IIT Kharagpur"),
             (None, "Dr. S. Velmurugan", "Chief Scientist, CSIR-CRRI"),
             ("asrivastava", "Akhilesh Srivastava", "President, IRF India"),
             (None, "Dr. A. M. Rao", "Chief Scientist, CSIR-CRRI"),
             ("pandey", "Rama Shankar Pandey", "FICCI Road Safety Roundtable"),
             (None, "Prof. Ashish Verma", "IISc Bengaluru"),
             (None, "Prof. Satish Chandra", "IIT Roorkee"),
             (None, "Prof. Gopal R. Patil", "IIT Bombay")]
    cw2 = Inches(3.85); ch2 = Inches(0.62)
    for i,(head,nm,ti) in enumerate(bench):
        x = M_L + (i%3)*(cw2+Inches(0.19)); yb = Inches(2.25) + (i//3)*(ch2+Inches(0.14))
        rect(s, x, yb, cw2, ch2, BRAND_LITE, rounded=True)
        hp = os.path.join(V3, "heads", f"{head}.png") if head else None
        if hp and os.path.exists(hp):
            s.shapes.add_picture(hp, x+Inches(0.1), yb+Inches(0.08), width=Inches(0.46), height=Inches(0.46))
        else:
            circle(s, x+Inches(0.1), yb+Inches(0.08), Inches(0.46), BRAND)
            text(s, x+Inches(0.1), yb+Inches(0.08), Inches(0.46), Inches(0.46),
                 "".join(w[0] for w in nm.replace("Dr. ","").replace("Prof. ","").split()[:2]),
                 font=HEAD, size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        text(s, x+Inches(0.68), yb+Inches(0.08), cw2-Inches(0.8), Inches(0.26), nm, font=HEAD, size=10.5, bold=True, color=DARK)
        text(s, x+Inches(0.68), yb+Inches(0.34), cw2-Inches(0.8), Inches(0.24), ti, font=BODY, size=8.8, color=MUTED)
    text(s, M_L, Inches(4.85), Inches(11.9), Inches(0.6),
         "Plus mentors and evaluators from KPMG, EY, CTRANS, SVNIT Surat, SPA Vijayawada & Bhopal, IIT Mandi, Vignan's University and the TRIP Centre — and forum participation from MoRTH, WHO, UNICEF, WRI, IFFCO Tokio, district administrations and traffic police leadership.",
         font=BODY, size=11.5, color=MUTED, ls=1.4)
    rect(s, M_L, Inches(5.9), CONTENT_W, Inches(0.7), BRAND_LITE, rounded=True)
    text(s, M_L+Inches(0.3), Inches(5.9), CONTENT_W-Inches(0.6), Inches(0.7),
         "This bench is available to the Working Group for drafting, review and technical input on road design, speed and VRU standards.",
         font=HEAD, size=12, bold=True, color=BRAND, anchor=MSO_ANCHOR.MIDDLE)
    foot(s, 15, total, wg)

    # 16 NEXTMILE TALENT PIPELINE
    s = new_slide(WHITE)
    y = sh(s, "THE TALENT PIPELINE", "Youth mobilisation that keeps the model supplied",
           "Scaling audits needs a steady flow of trained, motivated young engineers and planners — we have built that funnel.")
    nm_funnel = [("700+", "ideathon registrations (IITs, IIMs, NLUs)"), ("250+", "policy concept notes"),
                 ("37", "teams mentored"), ("10", "finalists judged by 24 experts")]
    fx = M_L; fy = Inches(2.3); fw = Inches(2.85); fh = Inches(1.35)
    for i,(num,lab) in enumerate(nm_funnel):
        rect(s, fx, fy, fw, fh, BRAND_LITE, rounded=True)
        text(s, fx, fy+Inches(0.12), fw, Inches(0.55), num, font=HEAD, size=25, bold=True, color=BRAND, align=PP_ALIGN.CENTER)
        text(s, fx+Inches(0.15), fy+Inches(0.7), fw-Inches(0.3), Inches(0.55), lab, font=BODY, size=10, color=MUTED, align=PP_ALIGN.CENTER, ls=1.2)
        fx += fw + Inches(0.26)
    bullet(s, M_L, Inches(4.0), Inches(11.6),
           "NextMile (2025), our national road-safety policy ideathon, closed at India Habitat Centre with a jury including Justice J.R. Midha and former MoRTH leadership.", size=12, icn="graduation-cap")
    bullet(s, M_L, Inches(4.7), Inches(11.6),
           "Winning tracks — blackspot identification, speed management, delivery-rider safety — feed directly into our audit and research pipeline.", size=12, icn="rocket")
    bullet(s, M_L, Inches(5.4), Inches(11.6),
           "Next: 'Be a Rakshak' university chapters at IITs, NITs and SPAs, with MS Dhoni as the recruiting voice — a self-renewing national audit corps.", size=12, icn="users-round")
    foot(s, 16, total, wg)

    # 17 VRU EVIDENCE
    s = new_slide(WHITE)
    y = sh(s, "VULNERABLE ROAD USERS", "A growing evidence base on those most at risk",
           "Two-wheeler riders and pedestrians carry most of the burden — our research follows them specifically.")
    rows = [
        ("bike", "Gig & delivery riders", "'When Risks Become Routine' (Feb 2026): incentive pressure, helmet compliance, training gaps and data fragmentation — now being quantified through a 300-rider study across Delhi NCR."),
        ("users", "Pedestrian-first audits", "Rakshak audits document crossings, footpaths and lighting as designable protections — 900+ stakeholder surveys included road users themselves."),
        ("school", "School zones", "College-led, standards-based school-zone screening under exploration as the next extension of the audit platform."),
        ("scan-line", "Enforcement that protects VRUs", "SATARK helps police prioritise the small share of vehicles with the worst records — targeted, fair and technology-led."),
    ]
    yy = Inches(2.3)
    for icn, t1, t2 in rows:
        circle(s, M_L, yy, Inches(0.44), BRAND_LITE)
        icon(s, icn, M_L+Inches(0.1), yy+Inches(0.1), Inches(0.24), BLUE_HEX)
        text(s, M_L+Inches(0.65), yy-Inches(0.02), Inches(3.2), Inches(0.6), t1, font=HEAD, size=13, bold=True, color=DARK)
        text(s, M_L+Inches(4.0), yy, Inches(8.0), Inches(0.8), t2, font=BODY, size=11, color=MUTED, ls=1.3)
        yy += Inches(1.08)
    foot(s, 17, total, wg)

# ============================================================================
# WG-5 BODY
# ============================================================================
def wg5_body(total):
    wg = 5
    # 6 MANDATE
    s = new_slide(BRAND_LITE)
    y = sh(s, "WORKING GROUP 5", "The mandate, and where we align",
           "Post-crash care, policy standards and state implementation.")
    mand = ["EMS", "Trauma care", "Laws", "Standards catalogue", "State support", "District toolkit"]
    mx = M_L
    for m in mand:
        wd = Inches(0.5 + 0.115*len(m))
        rect(s, mx, Inches(2.3), wd, Inches(0.48), WHITE, line=BORDER, rounded=True)
        text(s, mx, Inches(2.3), wd, Inches(0.48), m, font=HEAD, size=11.5, bold=True, color=DARK,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        mx += wd + Inches(0.18)
    al = [
        ("Compensation delivery", "'Justice Unserved' research; file-level audits with districts; claim-pipeline rebuild with the Rajasthan Transport Department."),
        ("District machinery", "Working inside four District Road Safety Committees — formally tasked by the South-West Delhi DRSC; a fellow embedded with Gurugram district offices."),
        ("Victim-facing standards", "Aasha chatbot, Compensation Calculator on Supreme Court principles, plain-language Hindi guides and hospital helpdesks."),
        ("Emergency response", "A Pre-Hospital Care Primer benchmarking India's golden-hour response against global standards, with state innovations documented."),
    ]
    yy = Inches(3.2)
    for t1, t2 in al:
        rect(s, M_L, yy, CONTENT_W, Inches(0.82), WHITE, line=BORDER, rounded=True)
        text(s, M_L+Inches(0.28), yy+Inches(0.12), Inches(3.3), Inches(0.6), t1, font=HEAD, size=12.5, bold=True, color=BRAND, ls=1.15)
        text(s, M_L+Inches(3.9), yy+Inches(0.12), Inches(8.2), Inches(0.6), t2, font=BODY, size=11, color=DARK, ls=1.28)
        yy += Inches(0.94)
    foot(s, 6, total, wg)

    # 7 THE VICTIM'S JOURNEY
    s = new_slide(WHITE)
    y = sh(s, "THE STARTING POINT", "A family experiences many institutions — not one programme",
           "Hospitals, police, district offices, enquiry officers, insurers, legal-services bodies and tribunals each do their part; the journey across them is what we work to simplify.")
    try:
        js = os.path.join(V3, "new", "journey_strip.png")
        jw = Inches(11.9)
        pic(s, js, M_L, Inches(2.6), w=jw)
        text(s, M_L, Inches(2.6)+jw/pic_ar(js)+Inches(0.12), jw, Inches(0.3),
             "The hit-and-run claim journey as we mapped it with officials in Jaipur — seven stages across six institutions.",
             font=BODY, size=10.5, color=MUTED, italic=True)
    except Exception as e: print(e)
    rect(s, M_L, Inches(6.0), CONTENT_W, Inches(0.7), BRAND_LITE, rounded=True)
    text(s, M_L+Inches(0.3), Inches(6.0), CONTENT_W-Inches(0.6), Inches(0.7),
         "Our work: make each hand-off visible, guide the family at every stage, and give administrators the dashboards to see where files wait.",
         font=HEAD, size=12, bold=True, color=BRAND, anchor=MSO_ANCHOR.MIDDLE, ls=1.3)
    foot(s, 7, total, wg)

    # 8 JUSTICE UNSERVED
    s = new_slide(WHITE)
    y = sh(s, "OUR RESEARCH FOUNDATION", "'Justice Unserved' — the evidence base we built first",
           "Published January 2026 · launched at IIT Delhi · findings presented to MoRTH · cited by national press.")
    try:
        ju = os.path.join(V3, "new", "comp_image1.png")
        pic(s, ju, M_L, Inches(2.35), h=Inches(3.6))
    except Exception as e: print(e)
    gaps5 = [
        ("Awareness", "70% of low-income families are unaware compensation exists"),
        ("Timeliness", "3.6-year average claim; MACT cases often run 8–10 years"),
        ("Documentation", "90% of pending hit-and-run claims stall on documents alone"),
        ("Adequacy", "Informal workers valued at minimum wage until courts enhance"),
        ("Equity", "14% of low-income households compensated vs 24% of high-income"),
    ]
    ty = Inches(2.35)
    for t1, t2 in gaps5:
        text(s, Inches(3.8), ty, Inches(8.8), Inches(0.3),
             [(t1+"  —  ", {'font':HEAD,'size':12,'bold':True,'color':BRAND}),
              (t2, {'font':BODY,'size':11.5,'color':DARK})], ls=1.25)
        ty += Inches(0.58)
    rect(s, Inches(3.8), Inches(5.5), Inches(8.83), Inches(0.85), BRAND_LITE, rounded=True)
    text(s, Inches(4.05), Inches(5.5), Inches(8.4), Inches(0.85),
         "Headline finding: only 205 hit-and-run claims were filed in FY22-23 against ~25,000 eligible crashes. The scheme is sound — the pipeline to it needs support.",
         font=HEAD, size=11.5, bold=True, color=BRAND, anchor=MSO_ANCHOR.MIDDLE, ls=1.3)
    foot(s, 8, total, wg)

    # 9 DISTRICT WORK
    s = new_slide(WHITE)
    y = sh(s, "FROM RESEARCH TO DISTRICTS", "Working inside the district machinery",
           "We took the research to where claims actually move: District Road Safety Committees and district offices.")
    rows = [
        ("landmark", "Four DRSCs joined", "Gurugram, South-West Delhi, North-West Delhi and Jaipur — with formal MoUs with Jaipur Traffic Police and Gurugram Police."),
        ("file-text", "File-level understanding", "With Gurugram's administration, we reviewed 102 hit-and-run files from 2022 onwards — mapping exactly where eligible families drop out."),
        ("badge-check", "Formally tasked", "The South-West Delhi DRSC's signed minutes task Crashfree India with digitisation and analytics support for scheme files."),
        ("user-check", "Embedded presence", "A research fellow placed with Gurugram district offices — implementation support, not external commentary."),
    ]
    yy = Inches(2.2)
    for icn, t1, t2 in rows:
        circle(s, M_L, yy, Inches(0.44), BRAND_LITE)
        icon(s, icn, M_L+Inches(0.1), yy+Inches(0.1), Inches(0.24), BLUE_HEX)
        text(s, M_L+Inches(0.65), yy-Inches(0.02), Inches(3.4), Inches(0.6), t1, font=HEAD, size=13, bold=True, color=DARK)
        text(s, M_L+Inches(4.2), yy, Inches(7.8), Inches(0.8), t2, font=BODY, size=11.5, color=MUTED, ls=1.3)
        yy += Inches(1.02)
    rect(s, M_L, Inches(6.25), CONTENT_W, Inches(0.6), BRAND_LITE, rounded=True)
    text(s, M_L+Inches(0.3), Inches(6.25), CONTENT_W-Inches(0.6), Inches(0.6),
         "This is district-toolkit experience in practice — the working knowledge WG-5's state-implementation mandate needs.",
         font=HEAD, size=12, bold=True, color=BRAND, anchor=MSO_ANCHOR.MIDDLE)
    foot(s, 9, total, wg)

    # 10 RAJASTHAN
    s = new_slide(BRAND_LITE)
    y = sh(s, "STATE ENGAGEMENT", "With Rajasthan: from mapping to a working template",
           "Supporting the state Lead Agency and Transport Department on the Hit-and-Run Compensation Scheme.")
    rows = [
        ("Ground mapping first", "Consultations across every office a claim touches in Jaipur — police thanas, DLSA, ADM office, SDM cell, DM and GIC."),
        ("What the data showed", "Jaipur alone delivers roughly half of Rajasthan's hit-and-run claims (~180 of ~395 in 2025) — active outreach and a single coordination cell explain the difference."),
        ("Findings shared as asks", "Document standard (7 court-agreed items vs 11–13 demanded), family traceability, stage-wise SLAs and five clarification queries prepared for GIC."),
        ("Portal design", "A guided-filing, stage-visible case-management portal for the scheme — designed so no stakeholder changes their medium, and officials retain every decision."),
    ]
    yy = Inches(2.2)
    for t1, t2 in rows:
        rect(s, M_L, yy, CONTENT_W, Inches(0.95), WHITE, line=BORDER, rounded=True)
        text(s, M_L+Inches(0.28), yy+Inches(0.12), Inches(3.2), Inches(0.7), t1, font=HEAD, size=12.5, bold=True, color=BRAND, ls=1.15)
        text(s, M_L+Inches(3.8), yy+Inches(0.12), Inches(8.3), Inches(0.75), t2, font=BODY, size=11, color=DARK, ls=1.28)
        yy += Inches(1.07)
    foot(s, 10, total, wg)

    # 11 AASHA & TOOLS
    s = new_slide(WHITE)
    y = sh(s, "VICTIM-FACING TOOLS", "Aasha and the tools that guide families through the process",
           "Built so that a family's first hours after a crash come with clear, correct guidance — in their language.")
    try:
        g1 = os.path.join(V3, "extracted", "guide_p1.png")
        pic(s, g1, Inches(9.3), Inches(2.2), h=Inches(4.2))
        text(s, Inches(9.3), Inches(6.5), Inches(3.3), Inches(0.3), "Hindi legal-rights guide — hospitals & police stations.",
             font=BODY, size=9.5, color=MUTED, italic=True)
    except Exception as e: print(e)
    rows = [
        ("bot", "Aasha", "India's first 24/7 multilingual AI companion for crash victims — step-by-step guidance on rights, schemes and documents, on WhatsApp and voice."),
        ("calculator", "Compensation Calculator", "Free, instant estimates based on Supreme Court principles (Sarla Verma, Pranay Sethi) — strengthening families' position."),
        ("hand-helping", "Hospital helpdesks", "Legal helpdesks in trauma wards — 100+ victims supported in the first four days of operation."),
        ("book-open", "Plain-language education", "Comics ('Know Your Rights with Aasha') and Hindi guides covering all three compensation routes, NALSA 15100 and the Cashless Treatment Scheme 2025."),
    ]
    yy = Inches(2.2)
    for icn, t1, t2 in rows:
        circle(s, M_L, yy, Inches(0.44), BRAND_LITE)
        icon(s, icn, M_L+Inches(0.1), yy+Inches(0.1), Inches(0.24), BLUE_HEX)
        text(s, M_L+Inches(0.65), yy-Inches(0.02), Inches(2.9), Inches(0.6), t1, font=HEAD, size=13, bold=True, color=DARK)
        text(s, M_L+Inches(3.6), yy, Inches(4.85), Inches(0.9), t2, font=BODY, size=11, color=MUTED, ls=1.3)
        yy += Inches(1.08)
    foot(s, 11, total, wg)

    # 12 PRE-HOSPITAL CARE
    s = new_slide(WHITE)
    y = sh(s, "EMERGENCY RESPONSE", "The Pre-Hospital Care Primer: our EMS evidence line",
           "Published September 2025 — benchmarking India's golden-hour response and documenting what states are getting right.")
    rows = [
        ("siren", "The response gap, measured", "ERSS-112 is live in all 36 states and UTs, yet highway ambulance arrival averages 25–35 minutes; the full episode runs 55–75 minutes against a 60-minute global benchmark."),
        ("heart-pulse", "State innovations documented", "Maharashtra's MEMS centralised dispatch across 937 ambulances; Tamil Nadu's TAEI model — pre-arrival alerts, trauma registries, automated triage — improving district response times."),
        ("shield-check", "Good Samaritan awareness", "Bystander protections and the Cashless Treatment Scheme 2025 (₹1.5 lakh / 7 days) explained in our public guides — the demand side of trauma care."),
        ("route", "Where this serves WG-5", "A ready, referenced baseline for the Group's EMS and trauma-care standards discussions — with state models already compared."),
    ]
    yy = Inches(2.2)
    for icn, t1, t2 in rows:
        circle(s, M_L, yy, Inches(0.44), BRAND_LITE)
        icon(s, icn, M_L+Inches(0.1), yy+Inches(0.1), Inches(0.24), BLUE_HEX)
        text(s, M_L+Inches(0.65), yy-Inches(0.02), Inches(3.4), Inches(0.6), t1, font=HEAD, size=13, bold=True, color=DARK)
        text(s, M_L+Inches(4.2), yy, Inches(7.8), Inches(0.9), t2, font=BODY, size=11, color=MUTED, ls=1.3)
        yy += Inches(1.14)
    foot(s, 12, total, wg)

    # 13 PORTAL PRINCIPLES
    s = new_slide(WHITE)
    y = sh(s, "TECHNOLOGY, CAREFULLY", "Design principles for public post-crash systems",
           "What we have learned building for the compensation pipeline — offered as reusable standards for any state.")
    prin = [
        ("No stakeholder changes their medium", "Families use WhatsApp and calls; officials keep their existing files and formats — the system adapts to them, not the reverse."),
        ("Officials retain every decision", "Technology flags, reminds and organises; sanctioning and verification stay entirely with the designated authorities."),
        ("Traceability before automation", "Phase 1 simply makes every file findable and every stage visible — the single largest lever we observed."),
        ("Single-pass clarification", "Objections batched and resolved once, not loops that reset the clock for a family."),
        ("Evidence for administrators", "Dashboards reveal where files wait, which documents fail and where outreach is needed — reform guided by data."),
    ]
    yy = Inches(2.15)
    for t1, t2 in prin:
        rect(s, M_L, yy, CONTENT_W, Inches(0.82), BRAND_LITE if yy==Inches(2.15) else WHITE,
             line=None if yy==Inches(2.15) else BORDER, rounded=True)
        text(s, M_L+Inches(0.28), yy+Inches(0.1), Inches(4.3), Inches(0.6), t1, font=HEAD, size=12.5, bold=True,
             color=BRAND, ls=1.15)
        text(s, M_L+Inches(4.9), yy+Inches(0.1), Inches(7.2), Inches(0.65), t2, font=BODY, size=11, color=DARK, ls=1.28)
        yy += Inches(0.94)
    foot(s, 13, total, wg)

    # 14 THE PIPELINE IN NUMBERS
    s = new_slide(WHITE)
    y = sh(s, "THE PIPELINE, MEASURED", "The numbers WG-5's standards can move",
           "Specialist figures from our research and file work — each one a lever the Group's standards and toolkits can act on.")
    stat_tile(s, M_L, Inches(2.3), Inches(3.8), "205 vs ~25,000", "hit-and-run claims filed vs eligible crashes (FY22-23)", h=Inches(1.35))
    stat_tile(s, M_L+Inches(4.05), Inches(2.3), Inches(3.8), "921 of 1,026", "pending claims stalled on documentation alone (Jul 2024)", h=Inches(1.35))
    stat_tile(s, M_L+Inches(8.1), Inches(2.3), Inches(3.8), "~60 days", "intake latency where claim surfacing waits for bi-monthly meetings", h=Inches(1.35))
    stat_tile(s, M_L, Inches(3.85), Inches(3.8), "~50%", "of FIRs lack a usable family phone number — traceability is the first lever", h=Inches(1.35))
    stat_tile(s, M_L+Inches(4.05), Inches(3.85), Inches(3.8), "7 vs 11–13", "court-agreed documents vs documents demanded in practice", h=Inches(1.35))
    stat_tile(s, M_L+Inches(8.1), Inches(3.85), Inches(3.8), "FY23-24: 12%", "of eligible crashes converted to filed claims — improving, far from done", h=Inches(1.35))
    rect(s, M_L, Inches(5.6), CONTENT_W, Inches(0.7), BRAND_LITE, rounded=True)
    text(s, M_L+Inches(0.3), Inches(5.6), CONTENT_W-Inches(0.6), Inches(0.7),
         "None of these require new legislation. Each responds to a standard, a toolkit entry or a communication norm — exactly what WG-5 exists to produce.",
         font=HEAD, size=12, bold=True, color=BRAND, anchor=MSO_ANCHOR.MIDDLE, ls=1.3)
    foot(s, 14, total, wg)

    # 15 INSURER & LEGAL ECOSYSTEM
    s = new_slide(WHITE)
    y = sh(s, "THE WIDER ECOSYSTEM", "We already work with the claim's other side",
           "Compensation standards only work if insurers, tribunals and legal-services institutions are in the room — we engage all three.")
    rows = [
        ("landmark", "GIC & insurers", "Five clarification queries prepared for GIC on MACT-affidavit objections; consultations with IFFCO Tokio and New India Assurance on settlement practice."),
        ("scale", "Tribunal & legal practice", "Guidance from Justice J. R. Midha (Retd., Delhi High Court), architect of the FastDAR process; working partners across MACT courts and DLSAs."),
        ("file-text", "Right-to-information evidence", "22+ RTIs filed on scheme performance (12 answered) — building the public record that standards work needs."),
        ("users", "Victim-side ground truth", "120+ victim and family interactions; 300+ citizens reached through awareness sessions; 30+ expert consultations."),
    ]
    yy = Inches(2.2)
    for icn, t1, t2 in rows:
        circle(s, M_L, yy, Inches(0.44), BRAND_LITE)
        icon(s, icn, M_L+Inches(0.1), yy+Inches(0.1), Inches(0.24), BLUE_HEX)
        text(s, M_L+Inches(0.65), yy-Inches(0.02), Inches(3.4), Inches(0.6), t1, font=HEAD, size=13, bold=True, color=DARK)
        text(s, M_L+Inches(4.2), yy, Inches(7.8), Inches(0.85), t2, font=BODY, size=11, color=MUTED, ls=1.3)
        yy += Inches(1.05)
    foot(s, 15, total, wg)

    # 16 TEAM FIT
    s = new_slide(BRAND_LITE)
    y = sh(s, "WHY OUR TEAM FITS", "Post-crash care needs more than one discipline",
           "A legally sound framework can still be hard to use; a good portal can still miss district workflows. Our team is built across that whole chain.")
    cols = [
        ("scale", "Law & policy", "NALSAR and Delhi University-trained; scheme analysis, RTIs, MoRTH engagement"),
        ("cpu", "Technology & product", "IIT-trained; Aasha, calculator, dashboards and portal architecture"),
        ("users", "Field & development practice", "TISS-trained; victim interviews, district engagement, DRSC work"),
        ("brain", "Behaviour & communication", "Psychology and design; guides, comics and multilingual communication"),
    ]
    cw = Inches(2.85); ch = Inches(2.5)
    for i,(icn,t1,t2) in enumerate(cols):
        x = M_L + i*(cw+Inches(0.17))
        rect(s, x, Inches(2.3), cw, ch, WHITE, line=BORDER, rounded=True)
        circle(s, x+Inches(0.25), Inches(2.55), Inches(0.5), BRAND_LITE)
        icon(s, icn, x+Inches(0.36), Inches(2.66), Inches(0.28), BLUE_HEX)
        text(s, x+Inches(0.25), Inches(3.25), cw-Inches(0.5), Inches(0.55), t1, font=HEAD, size=13, bold=True, color=DARK, ls=1.15)
        text(s, x+Inches(0.25), Inches(3.85), cw-Inches(0.5), Inches(0.85), t2, font=BODY, size=10.5, color=MUTED, ls=1.3)
    text(s, M_L, Inches(5.15), Inches(11.9), Inches(0.6),
         "Advised by Piyush Tewari (SaveLIFE Foundation), Prof. Geetam Tiwari (IIT Delhi) and Justice J. R. Midha (Retd., Delhi High Court — architect of the FastDAR process), with practitioner partners across MACT courts, DLSAs and insurers.",
         font=BODY, size=11.5, color=DARK, ls=1.4)
    foot(s, 16, total, wg)

# ============================================================================
# BUILD BOTH
# ============================================================================
for WG, TITLE, body_fn, TOTAL, offers_title, offers in [
    (2, "Safe Roads, Speeds & Vulnerable Road Users", wg2_body, 20,
     "Four concrete contributions to Working Group 2",
     [("Ready evidence for standard-setting", "Site-level audit data, crash-pattern analysis and intervention designs across emerging hotspots and official black spots — a working evidence base for rectification protocols and speed-management guidance."),
      ("A live testing ground", "Active district relationships in Gurugram, South-West Delhi and Jaipur offer a ready pipeline to pilot or stress-test draft recommendations before national rollout."),
      ("Ground-level implementation diagnostics", "Granular, field-verified insight into how DRSCs function — meeting cadence, data use, follow-through — to inform the Group's governance recommendations."),
      ("Technical bench strength on request", "Our academic and expert network stands ready for drafting, review and technical input on road design, speed and VRU standards.")]),
    (5, "Post-Crash Care, Policy Standards & State Implementation", wg5_body, 19,
     "Four concrete contributions to Working Group 5",
     [("A victim-side evidence base", "'Justice Unserved', 120+ victim and family interactions, and file-level audit data showing precisely where eligible families drop out of the process."),
      ("A district toolkit, drawn from practice", "Working DRSC integration experience — agendas, file digitisation, fellow placement — ready to be codified into the Group's district toolkit."),
      ("A reusable state portal blueprint", "The Rajasthan case-management design — guided filing, stage-wise visibility, single-pass clarification — offered as a template any state can adapt."),
      ("Standards input from the claimant's side", "Document standards (the court-agreed 7), communication standards and timeline benchmarks, grounded in what families actually experience.")]),
]:
    reset_prs()
    common_front(WG, TITLE, TOTAL)
    body_fn(TOTAL)
    common_back(WG, TOTAL, TOTAL-2, offers_title, offers)
    out = os.path.join(BUILD, f"CFI_NRSB_WG{WG}.pptx")
    H.prs.save(out)
    print("saved", out, len(H.prs.slides.__iter__.__self__._sldIdLst), "slides")

#!/usr/bin/env python3
"""Gig Rider Safety — Stakeholders deck, rebuilt in the CFI / NRSB-v2 house style.
Content preserved verbatim from the source deck; only layout, placement and design
elements (icon discs, stat cards, bars, tinted callouts) are the CFI system.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from nrsb2_style import *
from cfi_helpers import _strip_style
from pptx.util import Inches, Pt, Emu
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "CFI_GigRiderSafety-Stakeholders_v2_2026-09-09.pptx")

# nrsb2_style expects the logos in deck/; copy them from deck/assets/ if missing
# so a clean checkout can rebuild (the copies are git-ignored build artifacts).
import shutil
for _lg in ("logo_blue.png", "logo_white.png"):
    _dst = os.path.join(BUILD, _lg)
    if not os.path.exists(_dst):
        shutil.copy(os.path.join(SP, "assets", _lg), _dst)

INKMUT = RGBColor(0x45,0x48,0x55)   # slightly darker muted for small body
LAV_DK = RGBColor(0x6A,0x55,0xFF)   # hairline/glyph on brand-blue backgrounds

# ---------------------------------------------------------------- helpers
def cols(n, gap, x0=ML, total=CW):
    g = Inches(gap)
    w = Emu(int((int(total) - (n-1)*int(g)) / n))
    return [(Emu(int(int(x0) + i*(int(w)+int(g)))), w) for i in range(n)]

def foot(s, idx, section):
    hline(s, ML, Inches(7.06), CW)
    text(s, ML, Inches(7.14), Inches(9.6), Inches(0.25),
         f"Crashfree India    ·    Gig Rider Safety — {section}",
         size=8.5, color=MUT, ls=1.0)
    text(s, SW-MR-Inches(1.4), Inches(7.14), Inches(1.4), Inches(0.25),
         f"{idx:02d} / 14", size=8.5, color=MUT, align=PP_ALIGN.RIGHT, ls=1.0)

def source_line(s, t, y=Inches(6.72)):
    text(s, ML, y, CW, Inches(0.26), t, size=8, color=MUT, italic=True, ls=1.15)

def statcard(s, x, y, w, h, ic, value, label, desc, accent=BRAND, tint=BR_T, vsize=20):
    rect(s, x, y, w, h, fill=MIST, rounded=True, radius=0.05)
    pad = Inches(0.22)
    d = Inches(0.46)
    icon_disc(s, ic, Emu(int(x)+int(pad)), y+Inches(0.22), d, tint, hexs(accent))
    iw = Emu(int(w)-2*int(pad))
    text(s, Emu(int(x)+int(pad)), y+Inches(0.76), iw, Inches(0.46), value,
         font=HEAD, size=vsize, bold=True, color=accent, ls=1.0)
    text(s, Emu(int(x)+int(pad)), y+Inches(1.18), iw, Inches(0.40), label,
         font=HEAD, size=8.5, bold=True, color=INK, tracking=0.8, ls=1.08)
    text(s, Emu(int(x)+int(pad)), y+Inches(1.56), iw, Emu(int(h)-int(Inches(1.62))), desc,
         size=9.5, color=MUT, ls=1.2)

def hbar(s, x, y, w, frac, color, h=Inches(0.22)):
    frac = max(0.015, min(1.0, frac))
    rect(s, x, y, w, h, fill=RGBColor(0xEC,0xED,0xF2), rounded=True, radius=0.5)
    rect(s, x, y, Emu(int(int(w)*frac)), h, fill=color, rounded=True, radius=0.5)

def subhead(s, x, y, t, color=BRAND, w=Inches(6.0)):
    text(s, x, y, w, Inches(0.26), t.upper(), font=HEAD, size=9, bold=True,
         color=color, tracking=1.8, ls=1.0)

def tintbox(s, x, y, w, h, fill=MIST, line=None):
    rect(s, x, y, w, h, fill=fill, line=line, rounded=True, radius=0.05)

def sparkles(s, color=BRAND):
    for (sx,sy,sd) in [(12.42,0.34,0.42),(12.14,0.70,0.26)]:
        st = s.shapes.add_shape(MSO_SHAPE.STAR_4_POINT, Inches(sx),Inches(sy),Inches(sd),Inches(sd))
        st.fill.solid(); st.fill.fore_color.rgb=color; st.line.fill.background()
        st.shadow.inherit=False; _strip_style(st)

prs = new_deck()

# ================================================================ S1 COVER
def s1():
    s = slide()
    # logo + eyebrow
    s.shapes.add_picture(LOGO_BLUE, ML, Inches(0.52), width=Inches(1.7))
    sparkles(s, BRAND)
    text(s, ML, Inches(1.35), CW, Inches(0.26),
         "GIG RIDER SAFETY   ·   PRELIMINARY FINDINGS   ·   2026",
         font=HEAD, size=10, bold=True, color=BRAND, tracking=2.4)
    text(s, ML, Inches(1.78), Inches(11.6), Inches(1.15),
         [("Gig Rider Road Safety:", {'color':INK}),
          ("  Preliminary Findings from the Field", {'color':BRAND})],
         font=HEAD, size=30, bold=True, ls=1.08)
    text(s, ML, Inches(2.98), Inches(11.9), Inches(0.7),
         "Our working hypothesis: a gig rider's road risk is produced by three interacting "
         "systems — not by careless riders. Building on our February 2026 brief.",
         size=12.5, color=MUT, ls=1.35)
    # three framework cards
    cy = Inches(3.86); ch = Inches(2.5)
    data = [
        ("01","building-2","Structural & Occupational","CONDITIONS OF GIG WORK",
         ["Time-bound deliveries, algorithmic pressure","Low pay, rising ride costs",
          "Poor city infrastructure, weak enforcement"]),
        ("02","route","Operational & Behavioural","ON-ROAD BEHAVIOURS",
         ["Skill & training deficits, licensing gaps","Traffic violations — speeding, wrong-way",
          "Helmet non-use, vehicle modifications"]),
        ("03","bar-chart-3","Data & Accountability","CROSS-CUTTING ENABLER",
         ["Fragmented data silos","No monitoring or feedback loops","Limited accountability systems"]),
    ]
    for (x,w),(num,ic,cat,sub,pts) in zip(cols(3,0.3), data):
        rect(s, x, cy, w, ch, fill=MIST, rounded=True, radius=0.05)
        pad = Inches(0.22)
        text(s, Emu(int(x)+int(pad)), cy+Inches(0.20), Inches(1.0), Inches(0.4), num,
             font=HEAD, size=17, bold=True, color=BRAND, ls=1.0)
        icon_disc(s, ic, Emu(int(x)+int(w)-int(Inches(0.64))), cy+Inches(0.20),
                  Inches(0.44), BR_T, hexs(BRAND))
        text(s, Emu(int(x)+int(pad)), cy+Inches(0.70), Emu(int(w)-2*int(pad)), Inches(0.24),
             sub, font=HEAD, size=7.5, bold=True, color=BRAND, tracking=1.4)
        text(s, Emu(int(x)+int(pad)), cy+Inches(0.92), Emu(int(w)-2*int(pad)), Inches(0.3),
             cat, font=HEAD, size=12.5, bold=True, color=INK, ls=1.0)
        hline(s, Emu(int(x)+int(pad)), cy+Inches(1.32), Emu(int(w)-2*int(pad)))
        yy = cy+Inches(1.46)
        for p in pts:
            circle(s, Emu(int(x)+int(pad)), Emu(int(yy)+int(Inches(0.055))), Inches(0.06), BRAND)
            text(s, Emu(int(x)+int(pad)+int(Inches(0.18))), yy, Emu(int(w)-2*int(pad)-int(Inches(0.18))),
                 Inches(0.34), p, size=9.3, color=INKMUT, ls=1.12)
            yy = Emu(int(yy)+int(Inches(0.34)))
    hline(s, ML, Inches(6.62), CW)
    text(s, ML, Inches(6.72), Inches(9.5), Inches(0.4),
         "Preliminary findings — fieldwork ongoing. 309 riders surveyed to date; results may evolve.",
         size=9.5, color=MUT, ls=1.15)
    text(s, SW-MR-Inches(3.2), Inches(6.72), Inches(3.2), Inches(0.4),
         "Crashfree India  ×  Ayvole", font=HEAD, size=9.5, bold=True, color=INK,
         align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.TOP)
s1()

# ================================================================ S2 EXEC SUMMARY
def s2():
    s = slide()
    header(s, "Executive Summary",
           [("What the ",False),("fieldwork",True),(" shows so far",False)],
           lead="Six findings that recur across the survey. Each is unpacked in the slides that follow.")
    cells = [
        ("triangle-alert","62% vs 13%","E-BIKES RIDE UNLICENSED",
         "Low-speed e-bikes fall outside the Motor Vehicles Act — seen by police, but hard to fine.",AMBER,AM_T),
        ("bike","40% / 47%","HAVE ALREADY CRASHED",
         "Two in five food-delivery and nearly half of quick-commerce riders have crashed at least once.",BRAND,BR_T),
        ("file-text","~2 in 3","CRASHES NEVER REPORTED",
         "Most crashes never reach the platform, so company data understates the real toll.",AMBER,AM_T),
        ("hard-hat","76% / 34%","HELMET SEEN AS OPTIONAL",
         "Quick-commerce riders far more than food delivery treat helmets as skippable on short trips.",BRAND,BR_T),
        ("badge-check","40% / ~21%","UNLICENSED — ALL RIDERS / PETROL 2W",
         "About half of all riders ride without a licence — but only ~21% of petrol two-wheeler riders do. The gap sits with exempt e-bikes.",AMBER,AM_T),
        ("clock","44%","RIDE OVER 12 HOURS A DAY",
         "Long hours, ~79-hour weeks and thin rest are built into how the work is paid.",BRAND,BR_T),
    ]
    grid = cols(3,0.28)
    y0 = Inches(2.18); ch = Inches(2.22); gy = Inches(0.22)
    for i,(ic,v,lab,desc,ac,ti) in enumerate(cells):
        x,w = grid[i%3]
        y = Emu(int(y0) + (i//3)*(int(ch)+int(gy)))
        statcard(s,x,y,w,ch,ic,v,lab,desc,accent=ac,tint=ti,vsize=19)
    foot(s,2,"Executive Summary")
s2()

# ================================================================ S3 FRAMEWORK
def s3():
    s = slide()
    header(s, "The Framework",
           [("Three systems",True),(" produce the risk on the road",False)],
           lead="A deeper cut of the hypothesis: the specific risks we are testing inside each category.")
    data = [
        ("01","building-2","Structural & Occupational","CONDITIONS OF GIG WORK",
         [("Work design","Time-bound deliveries; ratings & penalties"),
          ("Economic precarity","Low pay; a quarter of earnings lost to ride costs"),
          ("City as workplace","Poor last-mile infrastructure; no rest points")]),
        ("02","route","Operational & Behavioural","ON-ROAD BEHAVIOURS",
         [("Training & licence","~40% report no safety training; licence gaps"),
          ("Traffic violations","Wrong-way riding, signal-jumping, speeding"),
          ("Helmet & vehicle","Helmet skipped on short trips; modified e-bikes")]),
        ("03","bar-chart-3","Data & Accountability","CROSS-CUTTING ENABLER",
         [("Fragmented silos","Crash, challan & platform data never joined up"),
          ("No feedback loops","Little monitoring of rider safety over time"),
          ("Weak accountability","Unclear who owns rider road-safety outcomes")]),
    ]
    cy = Inches(2.2); ch = Inches(4.5)
    for (x,w),(num,ic,cat,sub,rows) in zip(cols(3,0.3), data):
        rect(s,x,cy,w,ch,fill=MIST,rounded=True,radius=0.04)
        pad=Inches(0.24); iw=Emu(int(w)-2*int(pad))
        icon_disc(s,ic,Emu(int(x)+int(w)-int(Inches(0.66))),cy+Inches(0.22),Inches(0.46),BR_T,hexs(BRAND))
        text(s,Emu(int(x)+int(pad)),cy+Inches(0.24),Inches(1.0),Inches(0.3),num,
             font=HEAD,size=15,bold=True,color=BRAND)
        text(s,Emu(int(x)+int(pad)),cy+Inches(0.62),iw,Inches(0.24),sub,
             font=HEAD,size=7.5,bold=True,color=BRAND,tracking=1.3)
        text(s,Emu(int(x)+int(pad)),cy+Inches(0.84),iw,Inches(0.3),cat,
             font=HEAD,size=12.5,bold=True,color=INK,ls=1.0)
        hline(s,Emu(int(x)+int(pad)),cy+Inches(1.24),iw)
        yy=cy+Inches(1.42); pitch=Inches(1.0)
        for t,d in rows:
            rect(s,Emu(int(x)+int(pad)),Emu(int(yy)+int(Inches(0.03))),Inches(0.14),Inches(0.14),fill=BRAND)
            text(s,Emu(int(x)+int(pad)+int(Inches(0.26))),yy,Emu(int(iw)-int(Inches(0.26))),Inches(0.28),
                 t,font=HEAD,size=11,bold=True,color=INK,ls=1.0)
            text(s,Emu(int(x)+int(pad)),Emu(int(yy)+int(Inches(0.34))),iw,Inches(0.6),
                 d,size=9.3,color=MUT,ls=1.18)
            yy=Emu(int(yy)+int(pitch))
    foot(s,3,"The Framework")
s3()

# ================================================================ S4 HOW WE BUILT
def s4():
    s = slide()
    header(s, "How We Built This",
           [("Grounded in the field, ",False),("cross-checked with experts",True)],
           lead="Before the survey, we consulted enforcement, labour, transport and policy voices "
                "across cities, and ran a short on-ground violation study.")
    lx, lw = ML, Inches(5.9)
    subhead(s, lx, Inches(2.16), "Who we consulted")
    rows = [
        ("shield-check","Traffic Police","Delhi, Gurugram & Bengaluru — acknowledged the scale, offered data-sharing"),
        ("landmark","Ministries & Regulators","Labour (MoLE) and ex-transport (MoRTH / CMVR) voices on mandate & precedent"),
        ("graduation-cap","Academia & Research","Transport-safety researchers (IIT / institutional) on violations & fatigue"),
        ("users","Riders & a Labour Insider","40–50 rider conversations, 15 in-depth interviews, a day shadowing a woman rider"),
    ]
    yy = Inches(2.52); pitch=Inches(1.06)
    for ic,t,d in rows:
        icon_disc(s,ic,lx,yy,Inches(0.46),BR_T,hexs(BRAND))
        text(s,Emu(int(lx)+int(Inches(0.64))),Emu(int(yy)-int(Inches(0.02))),Emu(int(lw)-int(Inches(0.64))),Inches(0.3),
             t,font=HEAD,size=12,bold=True,color=INK,ls=1.0)
        text(s,Emu(int(lx)+int(Inches(0.64))),Emu(int(yy)+int(Inches(0.28))),Emu(int(lw)-int(Inches(0.64))),Inches(0.6),
             d,size=9.7,color=MUT,ls=1.2)
        yy=Emu(int(yy)+int(pitch))
    # right: violation study card
    rx = Inches(6.74); rw = Emu(int(SW-MR)-int(rx))
    ch = Inches(4.5); cyt = Inches(2.16)
    rect(s,rx,cyt,rw,ch,fill=MIST,rounded=True,radius=0.04)
    pad=Inches(0.26); iw=Emu(int(rw)-2*int(pad))
    text(s,Emu(int(rx)+int(pad)),cyt+Inches(0.24),iw,Inches(0.3),"ON-GROUND VIOLATION STUDY",
         font=HEAD,size=9,bold=True,color=BRAND,tracking=1.4)
    text(s,Emu(int(rx)+int(pad)),cyt+Inches(0.54),iw,Inches(0.6),
         "A 2-hour observational study at 4 Gurugram junctions logged ~500 gig riders on EVs "
         "and their violations (April 2026).",size=10,color=INKMUT,ls=1.25)
    tbl = [("Driving without helmet","188"),("Lane change w/o indication","134"),
           ("Red-light jumping","86"),("Stop-line crossing","55"),("Driving against traffic","46")]
    ty=cyt+Inches(1.34); rh=Inches(0.44); maxv=188
    for lab,val in tbl:
        hbar(s,Emu(int(rx)+int(pad)),Emu(int(ty)+int(Inches(0.24))),iw,int(val)/maxv,BR_T,h=Inches(0.14))
        text(s,Emu(int(rx)+int(pad)),ty,Emu(int(iw)-int(Inches(0.9))),Inches(0.26),lab,
             size=10,bold=True,color=INK,ls=1.0)
        text(s,Emu(int(rx)+int(rw)-int(pad)-int(Inches(0.9))),ty,Inches(0.9),Inches(0.26),val,
             font=HEAD,size=12,bold=True,color=BRAND,align=PP_ALIGN.RIGHT,ls=1.0)
        ty=Emu(int(ty)+int(rh))
    hline(s,Emu(int(rx)+int(pad)),Emu(int(ty)+int(Inches(0.04))),iw)
    text(s,Emu(int(rx)+int(pad)),Emu(int(ty)+int(Inches(0.12))),iw,Inches(0.3),
         "509 violations documented across ~500 riders",font=HEAD,size=10,bold=True,color=AMBER,ls=1.1)
    foot(s,4,"How We Built This")
s4()

# ================================================================ S5 METHODOLOGY
def s5():
    s = slide()
    header(s, "Methodology",
           [("A scaled survey, ",False),("still in the field",True)],
           lead="We partnered with a research agency to survey riders at crash hotspots across Delhi NCR.")
    # preliminary note full width (amber)
    ny = Inches(2.12)
    tintbox(s, ML, ny, CW, Inches(0.56), fill=AM_T)
    text(s, Emu(int(ML)+int(Inches(0.2))), Emu(int(ny)+int(Inches(0.08))), Inches(1.4), Inches(0.4),
         "PRELIMINARY", font=HEAD, size=9, bold=True, color=AMBER, tracking=1.2, anchor=MSO_ANCHOR.MIDDLE)
    text(s, Emu(int(ML)+int(Inches(1.55))), ny, Emu(int(CW)-int(Inches(1.75))), Inches(0.56),
         "Every figure in this deck is drawn from fieldwork completed so far, and will shift as the "
         "sample grows and diversifies.", size=10, color=INKMUT, ls=1.2, anchor=MSO_ANCHOR.MIDDLE)
    # two columns
    lx,lw = ML, Inches(5.85)
    rx = Inches(6.74); rw = Emu(int(SW-MR)-int(rx))
    cy = Inches(2.94)
    subhead(s, lx, cy, "What we set out to do")
    do = ["Build the evidence base for the regulatory lacuna around EV two-wheelers",
          "Collect data to rank and identify platform-level solutions",
          "Create an evidence base for platform engagement and policy advocacy"]
    yy = Emu(int(cy)+int(Inches(0.36)))
    for i,t in enumerate(do,1):
        num_disc(s, lx, yy, Inches(0.4), i)
        text(s, Emu(int(lx)+int(Inches(0.56))), Emu(int(yy)-int(Inches(0.02))),
             Emu(int(lw)-int(Inches(0.56))), Inches(0.6), t, size=10.5, color=INKMUT, ls=1.22)
        yy = Emu(int(yy)+int(Inches(0.74)))
    subhead(s, rx, cy, "Where we are now")
    now = [("309","riders surveyed"),
           ("157 / 152","food delivery  ·  quick commerce"),
           ("104 / 309","ride an e-bike / EV (34%)"),
           ("all male","309 respondents to date — 2 women riders reached informally")]
    yy = Emu(int(cy)+int(Inches(0.36)))
    for v,l in now:
        text(s, rx, yy, Inches(1.75), Inches(0.3), v, font=HEAD, size=13, bold=True, color=BRAND, ls=1.0)
        text(s, Emu(int(rx)+int(Inches(1.85))), Emu(int(yy)+int(Inches(0.01))),
             Emu(int(rw)-int(Inches(1.85))), Inches(0.44), l, size=10, color=INKMUT, ls=1.15)
        yy = Emu(int(yy)+int(Inches(0.5)))
    # bottom: what we set out to sample
    by = Inches(5.56)
    hline(s, ML, by, CW)
    subhead(s, ML, Emu(int(by)+int(Inches(0.1))), "What we set out to sample", w=Inches(4.0))
    text(s, SW-MR-Inches(5.4), Emu(int(by)+int(Inches(0.11))), Inches(5.4), Inches(0.24),
         "Sampled at low, medium and high-severity crash hotspots.",
         size=8.5, color=MUT, italic=True, align=PP_ALIGN.RIGHT, ls=1.0)
    chips = [("300","Riders targeted"),("50:50","Food : quick commerce"),
             ("10%+","Women riders"),("20%+","EV riders"),("12","Locations (Gurugram, Delhi)")]
    cgrid = cols(5,0.2, x0=ML, total=CW)
    for (x,w),(v,l) in zip(cgrid, chips):
        text(s, x, Emu(int(by)+int(Inches(0.46))), w, Inches(0.34), v,
             font=HEAD, size=18, bold=True, color=INK, ls=1.0)
        text(s, x, Emu(int(by)+int(Inches(0.86))), w, Inches(0.34), l, size=8.8, color=MUT, ls=1.1)
    foot(s,5,"Methodology")
s5()

# ================================================================ S6 WHO RIDES
def s6():
    s = slide()
    header(s, "Who Rides",
           [("Rider demographics",True),(" — who is on the road",False)],
           lead="Riders have little cushion to absorb a lost day — and many are on the road without a full licence.")
    cells = [
        ("users","~29","AVERAGE RIDER AGE",
         "62% are under 30. Quick commerce skews younger (45% aged 18–25 vs 36% in food delivery)."),
        ("map-pin","69%","ARE MIGRANTS",
         "Most ride in a city they are not from — 80% in food delivery, 58% in quick commerce."),
        ("home","69% / 54%","MAIN HOUSEHOLD EARNER",
         "A lost day costs the whole family. Food delivery / quick commerce."),
    ]
    y0=Inches(2.2); ch=Inches(2.05)
    for (x,w),(ic,v,l,d) in zip(cols(3,0.28), cells):
        statcard(s,x,y0,w,ch,ic,v,l,d,vsize=21)
    # licence comparison block
    by = Inches(4.45); bh = Inches(2.2)
    rect(s, ML, by, CW, bh, fill=MIST, rounded=True, radius=0.04)
    pad=Inches(0.3)
    text(s, Emu(int(ML)+int(pad)), Emu(int(by)+int(Inches(0.22))), Inches(7.0), Inches(0.3),
         "Experienced riders — but not fully licensed", font=HEAD, size=13, bold=True, color=INK, ls=1.0)
    text(s, Emu(int(ML)+int(pad)), Emu(int(by)+int(Inches(0.62))), Inches(6.1), Inches(1.2),
         "88% learnt to ride more than five years ago, so skill is not the gap. Yet many ride "
         "without a regular licence — especially in quick commerce, where two in five have none at all.",
         size=10.5, color=INKMUT, ls=1.3)
    # two comparison bars on the right
    cx = Inches(7.3); cw = Inches(5.1)
    def cmp(y, title, fd, qc):
        text(s, cx, y, cw, Inches(0.26), title, font=HEAD, size=10, bold=True, color=INK, ls=1.0)
        for i,(lab,val,col) in enumerate([("FD",fd,BRAND),("QC",qc,AMBER)]):
            ry = Emu(int(y)+int(Inches(0.32))+i*int(Inches(0.34)))
            text(s, cx, ry, Inches(0.5), Inches(0.24), lab, font=HEAD, size=9.5, bold=True, color=MUT, ls=1.0)
            hbar(s, Emu(int(cx)+int(Inches(0.55))), Emu(int(ry)+int(Inches(0.02))), Inches(3.4), val/100.0, col, h=Inches(0.18))
            text(s, Emu(int(cx)+int(Inches(4.05))), ry, Inches(1.0), Inches(0.24), f"{val}%",
                 font=HEAD, size=10, bold=True, color=col, ls=1.0)
    cmp(Emu(int(by)+int(Inches(0.30))), "Hold a regular licence", 76, 56)
    cmp(Emu(int(by)+int(Inches(1.30))), "Ride with no licence at all", 19, 40)
    foot(s,6,"Who Rides")
s6()

# ================================================================ S7 SAFETY READINESS
def s7():
    s = slide()
    header(s, "Safety Readiness",
           [("Helmet use tracks the platform",True),(" — and the vehicle",False)],
           lead="Always-wear rates split sharply by who riders work for, and by what they ride.")
    lx,lw = ML, Inches(5.85)
    rx = Inches(6.74); rw = Emu(int(SW-MR)-int(rx))
    def block(x, w, title, a_lab, a_val, b_lab, b_val, subs, sec_title, sec_txt):
        subhead(s, x, Inches(2.12), title)
        # two headline always-wear bars
        y = Inches(2.44)
        for lab,val,col in [(a_lab,a_val,BRAND),(b_lab,b_val,AMBER)]:
            text(s, x, y, Emu(int(w)-int(Inches(1.0))), Inches(0.24), lab, size=9.5, bold=True, color=INK, ls=1.0)
            text(s, Emu(int(x)+int(w)-int(Inches(0.9))), y, Inches(0.9), Inches(0.24), f"{val}%",
                 font=HEAD, size=11, bold=True, color=col, align=PP_ALIGN.RIGHT, ls=1.0)
            hbar(s, x, Emu(int(y)+int(Inches(0.26))), w, val/100.0, col, h=Inches(0.16))
            y = Emu(int(y)+int(Inches(0.56)))
        # sub-stats
        y = Emu(int(y)+int(Inches(0.04)))
        for t in subs:
            text(s, x, y, w, Inches(0.24), t, size=9, color=INKMUT, ls=1.15)
            y = Emu(int(y)+int(Inches(0.27)))
        # secondary evidence box
        sy = Inches(4.98); sh = Inches(1.6)
        tintbox(s, x, sy, w, sh, fill=BR_T)
        pad=Inches(0.2)
        text(s, Emu(int(x)+int(pad)), Emu(int(sy)+int(Inches(0.14))), Emu(int(w)-2*int(pad)), Inches(0.24),
             "SECONDARY EVIDENCE  ·  "+sec_title, font=HEAD, size=8, bold=True, color=BRAND, tracking=1.0, ls=1.05)
        text(s, Emu(int(x)+int(pad)), Emu(int(sy)+int(Inches(0.42))), Emu(int(w)-2*int(pad)), Emu(int(sh)-int(Inches(0.5))),
             sec_txt, size=9, color=INKMUT, ls=1.22)
    block(lx, lw, "Always wear a helmet — by platform",
          "Food delivery", 66, "Quick commerce", 24,
          ["Fined for no helmet (of ever-fined):  FD 20%  ·  QC 59%",
           "Warned for no helmet (of ever-warned):  FD 12%  ·  QC 35%",
           "Rate “no helmet” riskiest (of all):  FD 18%  ·  QC 16%"],
          "Delivery vs. private riders",
          "A 2024 study comparing delivery, ride-hailing and private riders found private riders had "
          "the higher rate of helmet non-use — even with police visibly present. 73% of the ~75,000 "
          "two-wheeler riders who died in 2023 were not wearing a helmet.")
    block(rx, rw, "Always wear a helmet — by vehicle",
          "Petrol", 51, "E-bike / EV", 35,
          ["Fined for no helmet (of ever-fined):  Petrol 36%  ·  EV 53%",
           "Rate “no helmet” LEAST risky:  Petrol 11%  ·  EV 21%",
           "Rate “no helmet” MOST risky:  Petrol 22%  ·  EV 8%"],
          "Why e-bikes lag on helmets",
          "Sub-250W, sub-25km/h e-2Ws are not motor vehicles under GSR 291(E) — no licence or helmet "
          "mandate applies. Correct helmet use was just 38.4% among two-wheeler riders in a "
          "98,021-vehicle Bengaluru study.")
    source_line(s, "Own survey data, n=309. Secondary sources: IndiaSpend / MoRTH (2023), GSR 291(E), "
                   "Bengaluru observational study.", y=Inches(6.72))
    foot(s,7,"Safety Readiness")
s7()

# ================================================================ S8 E-BIKE GAP
def s8():
    s = slide()
    header(s, "The E-bike Gap",
           [("Police can see them, ",False),("but cannot fine them",True)],
           lead="Our headline enforcement finding: e-bike riders ride unlicensed far more, yet are "
                "fined far less — because the law does not reach the vehicle.")
    # left: comparison table
    lx,lw = ML, Inches(5.7)
    subhead(s, lx, Inches(2.28), "E-bike (n=104)  vs  Petrol (n=205)")
    metrics = [("Ride unlicensed",62,13),("Ever fined",14,64),("Stopped & warned",42,36)]
    yy = Inches(2.62); rh=Inches(1.02)
    for lab,eb,pet in metrics:
        text(s, lx, yy, lw, Inches(0.26), lab, font=HEAD, size=11, bold=True, color=INK, ls=1.0)
        # e-bike bar
        text(s, lx, Emu(int(yy)+int(Inches(0.30))), Inches(1.1), Inches(0.22), "E-BIKE",
             font=HEAD, size=8, bold=True, color=AMBER, tracking=1.0, ls=1.0)
        hbar(s, Emu(int(lx)+int(Inches(1.15))), Emu(int(yy)+int(Inches(0.30))), Inches(3.4), eb/100.0, AMBER, h=Inches(0.18))
        text(s, Emu(int(lx)+int(Inches(4.62))), Emu(int(yy)+int(Inches(0.28))), Inches(1.0), Inches(0.24),
             f"{eb}%", font=HEAD, size=11, bold=True, color=AMBER, ls=1.0)
        # petrol bar
        text(s, lx, Emu(int(yy)+int(Inches(0.60))), Inches(1.1), Inches(0.22), "PETROL",
             font=HEAD, size=8, bold=True, color=BRAND, tracking=1.0, ls=1.0)
        hbar(s, Emu(int(lx)+int(Inches(1.15))), Emu(int(yy)+int(Inches(0.60))), Inches(3.4), pet/100.0, BRAND, h=Inches(0.18))
        text(s, Emu(int(lx)+int(Inches(4.62))), Emu(int(yy)+int(Inches(0.58))), Inches(1.0), Inches(0.24),
             f"{pet}%", font=HEAD, size=11, bold=True, color=BRAND, ls=1.0)
        yy=Emu(int(yy)+int(rh))
    # right: why the law misses them
    rx = Inches(6.74); rw = Emu(int(SW-MR)-int(rx))
    subhead(s, rx, Inches(2.28), "Why the law misses them")
    text(s, rx, Inches(2.62), rw, Inches(1.0),
         "Under CMVR Rule 2(u), an e-two-wheeler under 250W and 25 km/h is not a “motor vehicle” "
         "at all — so it needs no licence, registration or number plate, and cannot be fined for riding "
         "without one.", size=10.5, color=INKMUT, ls=1.28)
    text(s, rx, Inches(3.72), rw, Inches(1.0),
         "Even where riders clearly break rules, police report confusion over whether e-bikes fall under "
         "the Motor Vehicles Act — a regulatory lacuna our evidence base aims to close.",
         size=10.5, color=INKMUT, ls=1.28)
    # external links
    ly = Inches(4.74)
    for t in ["CMVR Rule 2(u) — low-speed EV exemption","The Tribune — e-bike MV Act enforcement case"]:
        icon(s, "external-link", rx, Emu(int(ly)+int(Inches(0.02))), Inches(0.2), hexs(LAVW), sw=2.2)
        text(s, Emu(int(rx)+int(Inches(0.3))), ly, Emu(int(rw)-int(Inches(0.3))), Inches(0.28),
             t, size=9.5, color=BRAND, bold=True, ls=1.1)
        ly=Emu(int(ly)+int(Inches(0.34)))
    # bottom brand callout
    cy = Inches(5.74); ch=Inches(0.82)
    rect(s, ML, cy, CW, ch, fill=BRAND, rounded=True, radius=0.08)
    text(s, Emu(int(ML)+int(Inches(0.3))), cy, Emu(int(CW)-int(Inches(0.6))), ch,
         "E-bike riders are 4.7× more likely to ride unlicensed — yet 4.5× less likely to be fined. "
         "Police stop and warn them more, but cannot act.",
         font=HEAD, size=12.5, bold=True, color=PAPER, anchor=MSO_ANCHOR.MIDDLE, ls=1.2)
    foot(s,8,"The E-bike Gap")
s8()

# ================================================================ S9 ECONOMICS
def s9():
    s = slide()
    header(s, "The Economics of Risk",
           [("Long days, and incentives ",False),("that barely cover the ride",True)],
           lead="Hours are long, and what riders earn from incentives is close to what riding costs them.")
    cells = [
        ("clock","44%","WORK MORE THAN 12 HOURS A DAY",
         "Riders average ~79-hour weeks; over half work all seven days.",AMBER,AM_T),
        ("file-text","₹7,976","AVG WEEKLY EARNINGS (ALL SOURCES)",
         "Approximate — the survey captures income as bands, not exact values.",BRAND,BR_T),
        ("badge-check","78%","EARN INCENTIVES AT OR ABOVE RIDE SPEND",
         "For most riders incentive pay offsets the cost of riding rather than adding profit.",AMBER,AM_T),
    ]
    y0=Inches(2.2); ch=Inches(1.95)
    for (x,w),(ic,v,l,d,ac,ti) in zip(cols(3,0.28), cells):
        statcard(s,x,y0,w,ch,ic,v,l,d,accent=ac,tint=ti,vsize=21)
    # incentive vs expense
    by=Inches(4.42); bh=Inches(2.05)
    rect(s, ML, by, CW, bh, fill=MIST, rounded=True, radius=0.04)
    pad=Inches(0.3)
    text(s, Emu(int(ML)+int(pad)), Emu(int(by)+int(Inches(0.22))), Inches(6.3), Inches(0.3),
         "Incentive income roughly tracks ride-related costs", font=HEAD, size=13, bold=True, color=INK, ls=1.0)
    text(s, Emu(int(ML)+int(pad)), Emu(int(by)+int(Inches(0.6))), Inches(6.1), Inches(1.3),
         "Fuel, maintenance, mobile data and fines run close behind what riders earn from incentives — "
         "so incentive pay mainly offsets the cost of riding, not clear profit on top of base pay.",
         size=10.5, color=INKMUT, ls=1.3)
    cx=Inches(7.2); cw=Inches(5.2); maxv=2300
    def moneybar(y, val, lab, col):
        text(s, cx, y, cw, Inches(0.26), lab, size=10, bold=True, color=INK, ls=1.0)
        text(s, Emu(int(cx)+int(cw)-int(Inches(1.3))), y, Inches(1.3), Inches(0.26), f"₹{val:,}",
             font=HEAD, size=13, bold=True, color=col, align=PP_ALIGN.RIGHT, ls=1.0)
        hbar(s, cx, Emu(int(y)+int(Inches(0.30))), cw, val/maxv, col, h=Inches(0.2))
    moneybar(Emu(int(by)+int(Inches(0.34))), 2300, "Weekly incentive income", BRAND)
    moneybar(Emu(int(by)+int(Inches(1.12))), 1941, "Weekly ride-related expenses", AMBER)
    source_line(s, "Weekly income, incentive and expense figures are approximate — captured as ranges, "
                   "not exact values. Own survey data, n=309 (n=229 with complete income data).", y=Inches(6.72))
    foot(s,9,"The Economics of Risk")
s9()

# ================================================================ S10 ENFORCEMENT
def s10():
    s = slide()
    header(s, "Enforcement Patterns",
           [("Some violations get a fine. ",False),("Others just get a warning.",True)],
           lead="Warnings issued per fine issued, by violation type — above 1.0× means police let riders "
                "off more often than they fine them.")
    lx,lw = ML, Inches(6.6)
    ratios = [("Riding on footpath",2.33),("Driving wrong direction",1.32),("Over speeding",0.86),
              ("No entry zone",0.83),("Jumped red light",0.59),("Not wearing helmet",0.52)]
    yy=Inches(2.28); rh=Inches(0.66); scale=2.5
    # reference line at 1.0x
    refx = Emu(int(lx)+int(Inches(1.9))+int(Inches(3.9)*(1.0/scale)))
    ln = s.shapes.add_connector(1, refx, Emu(int(yy)-int(Inches(0.05))), refx, Emu(int(yy)+6*int(rh)-int(Inches(0.15))))
    ln.line.color.rgb=MUT; ln.line.width=Pt(1.0); ln.shadow.inherit=False; _strip_style(ln)
    text(s, Emu(int(refx)-int(Inches(0.5))), Emu(int(yy)+6*int(rh)-int(Inches(0.12))), Inches(1.6), Inches(0.24),
         "1.0× — warned as often as fined", size=8, color=MUT, ls=1.0)
    for lab,r in ratios:
        col = AMBER if r>1.0 else BRAND
        text(s, lx, yy, Inches(1.85), Inches(0.4), lab, size=9.7, bold=True, color=INK, ls=1.02, anchor=MSO_ANCHOR.MIDDLE)
        hbar(s, Emu(int(lx)+int(Inches(1.9))), Emu(int(yy)+int(Inches(0.06))), Inches(3.9), r/scale, col, h=Inches(0.26))
        text(s, Emu(int(lx)+int(Inches(1.9))+int(Inches(3.9)*(r/scale))+int(Inches(0.08))),
             Emu(int(yy)+int(Inches(0.05))), Inches(0.8), Inches(0.28), f"{r:.2f}×",
             font=HEAD, size=10.5, bold=True, color=col, ls=1.0)
        yy=Emu(int(yy)+int(rh))
    # right: what this means
    rx=Inches(9.0); rw=Emu(int(SW-MR)-int(rx))
    tintbox(s, rx, Inches(2.2), rw, Inches(4.3), fill=MIST)
    pad=Inches(0.24)
    subhead(s, Emu(int(rx)+int(pad)), Inches(2.42), "What this means", w=Emu(int(rw)-2*int(pad)))
    notes = ["Footpath riding is treated as a warning, not a violation.",
             "Riders are warned for footpath riding 2.3× more often than they are fined for it, and for "
             "wrong-direction riding 1.3× more often.",
             "Both sit far above helmet (0.5×) and red-light (0.6×) violations, which are fined harder.",
             "During Bengaluru's Nov 2024 special drive, footpath riding drew the most complaints — even "
             "though helmet non-compliance topped the recorded-challan list."]
    yy=Inches(2.82); pitch=Inches(0.95)
    for n in notes:
        rect(s, Emu(int(rx)+int(pad)), Emu(int(yy)+int(Inches(0.05))), Inches(0.1), Inches(0.1), fill=BRAND)
        text(s, Emu(int(rx)+int(pad)+int(Inches(0.22))), yy, Emu(int(rw)-2*int(pad)-int(Inches(0.22))), Inches(0.88),
             n, size=9.5, color=INKMUT, ls=1.22)
        yy=Emu(int(yy)+int(pitch))
    source_line(s, "Own survey data, n=309 — ratio of riders ever warned to riders ever fined, by violation type.",
                y=Inches(6.72))
    foot(s,10,"Enforcement Patterns")
s10()

# ================================================================ S11 CRASHES
def s11():
    s = slide()
    header(s, "Crashes & Near-misses",
           [("Wrong-side riding",True),(" is the crash riders describe most",False)],
           lead="Crashes are common and near-misses are weekly — and riders' own accounts point at oncoming traffic.")
    lx,lw = ML, Inches(5.7)
    # two stats
    for i,(v,l,d) in enumerate([("43%","HAVE EVER CRASHED","Of all riders surveyed (n=309)."),
                                ("~1 in 2","A NEAR-MISS EVERY WEEK","Around half of all riders report a near-miss in a typical week.")]):
        x = Emu(int(lx)+i*int(Inches(2.95)))
        text(s, x, Inches(2.2), Inches(2.8), Inches(0.5), v, font=HEAD, size=26, bold=True, color=BRAND, ls=1.0)
        text(s, x, Inches(2.74), Inches(2.8), Inches(0.28), l, font=HEAD, size=9, bold=True, color=INK, tracking=1.0, ls=1.05)
        text(s, x, Inches(3.04), Inches(2.8), Inches(0.7), d, size=9.5, color=MUT, ls=1.2)
    # secondary evidence box
    sy=Inches(3.96); sh=Inches(2.5)
    tintbox(s, lx, sy, lw, sh, fill=BR_T)
    pad=Inches(0.22)
    text(s, Emu(int(lx)+int(pad)), Emu(int(sy)+int(Inches(0.16))), Emu(int(lw)-2*int(pad)), Inches(0.24),
         "SECONDARY EVIDENCE  ·  How this compares elsewhere", font=HEAD, size=8, bold=True, color=BRAND, tracking=1.0)
    text(s, Emu(int(lx)+int(pad)), Emu(int(sy)+int(Inches(0.46))), Emu(int(lw)-2*int(pad)), Inches(1.1),
         "A Mumbai study of 431 food-delivery riders found 54.1% had crashed and 75.6% had a near-crash — "
         "with surrounding traffic and the rider's own aberrant behaviour as the top predictors.",
         size=9.7, color=INKMUT, ls=1.26)
    text(s, Emu(int(lx)+int(pad)), Emu(int(sy)+int(Inches(1.5))), Emu(int(lw)-2*int(pad)), Inches(0.9),
         "Riders are warned for wrong-direction riding 1.3× more often than they are fined for it — yet "
         "13% independently call it the single riskiest action a rider can take.",
         size=9.7, color=INKMUT, ls=1.26)
    # right: crash-cause bars
    rx=Inches(6.74); rw=Emu(int(SW-MR)-int(rx))
    subhead(s, rx, Inches(2.16), "What riders' own crash accounts describe")
    causes = [("Wrong-side / oncoming vehicle",14.9),("Lost control / skidded (self)",12.7),
              ("Rear-ended (hit from behind)",8.2),("Sudden pedestrian / cyclist / animal",8.2),
              ("Road & infra (potholes, water)",3.0),("Phone distraction",2.2)]
    yy=Inches(2.54); maxv=14.9; rh=Inches(0.5)
    for lab,v in causes:
        col = AMBER if v>=12 else BRAND
        text(s, rx, yy, Emu(int(rw)-int(Inches(0.7))), Inches(0.24), lab, size=9.3, bold=True, color=INK, ls=1.0)
        text(s, Emu(int(rx)+int(rw)-int(Inches(0.7))), yy, Inches(0.7), Inches(0.24), f"{v}%",
             font=HEAD, size=10, bold=True, color=col, align=PP_ALIGN.RIGHT, ls=1.0)
        hbar(s, rx, Emu(int(yy)+int(Inches(0.26))), rw, v/maxv, col, h=Inches(0.13))
        yy=Emu(int(yy)+int(rh))
    text(s, rx, Emu(int(yy)+int(Inches(0.02))), rw, Inches(0.7),
         "Coded from 134 open-ended descriptions of a single most recent crash; riders could mention more "
         "than one factor — useful for the pattern, not a precise causal share.",
         size=8.3, color=MUT, italic=True, ls=1.2)
    foot(s,11,"Crashes & Near-misses")
s11()

# ================================================================ S12 SAFETY NET
def s12():
    s = slide()
    header(s, "The Safety Net",
           [("Protection exists on paper, ",False),("not within reach",True)],
           lead="After a crash, most riders neither report it nor recover anything — and few even know a scheme exists.")
    # funnel left
    lx,lw = ML, Inches(6.4)
    subhead(s, lx, Inches(2.16), "After a crash")
    stages = [("Riders who crashed","100%",1.0,BRAND),
              ("Reported it to the platform","~1 in 3",0.33,AMBER),
              ("Actually claimed compensation","14% / 17%",0.155,AMBER)]
    yy=Inches(2.56); rh=Inches(1.28)
    for lab,val,frac,col in stages:
        bw = Emu(int(Inches(1.4))+int(int(Inches(4.4))*frac))
        rect(s, lx, yy, bw, Inches(0.92), fill=col, rounded=True, radius=0.06)
        text(s, Emu(int(lx)+int(Inches(0.24))), yy, Emu(int(bw)-int(Inches(0.3))), Inches(0.92), val,
             font=HEAD, size=20, bold=True, color=PAPER, anchor=MSO_ANCHOR.MIDDLE, ls=1.0)
        text(s, lx, Emu(int(yy)+int(Inches(0.96))), lw, Inches(0.26), lab, size=10, bold=True, color=INK, ls=1.0)
        yy=Emu(int(yy)+int(rh))
    # right: navigating blind
    rx=Inches(7.35); rw=Emu(int(SW-MR)-int(rx))
    tintbox(s, rx, Inches(2.16), rw, Inches(4.3), fill=MIST)
    pad=Inches(0.28)
    subhead(s, Emu(int(rx)+int(pad)), Inches(2.42), "And most are navigating blind", w=Emu(int(rw)-2*int(pad)))
    text(s, Emu(int(rx)+int(pad)), Inches(2.86), Emu(int(rw)-2*int(pad)), Inches(0.6), "53% / 30%",
         font=HEAD, size=30, bold=True, color=AMBER, ls=1.0)
    text(s, Emu(int(rx)+int(pad)), Inches(3.5), Emu(int(rw)-2*int(pad)), Inches(0.6),
         "of riders have ever received any guidance on crash compensation or relief. "
         "(Food delivery / quick commerce.)", size=10.5, color=INKMUT, ls=1.28)
    hline(s, Emu(int(rx)+int(pad)), Inches(4.3), Emu(int(rw)-2*int(pad)))
    text(s, Emu(int(rx)+int(pad)), Inches(4.46), Emu(int(rw)-2*int(pad)), Inches(1.9),
         "Of those who do claim, nearly all rely on platform insurance — there is no independent safety "
         "net. The most-requested change from riders themselves is simply insurance that actually pays out.",
         size=10.5, color=INKMUT, ls=1.3)
    foot(s,12,"The Safety Net")
s12()

# ================================================================ S13 WHAT THIS MEANS
def s13():
    s = slide()
    header(s, "What This Means",
           [("The evidence points to ",False),("systems, not riders",True)],
           lead="Preliminary as it is, the data already lines up behind the three-system hypothesis — and "
                "shows where change must land.")
    data = [
        ("01","landmark","Close the EV regulatory gap",
         "Low-speed e-bikes evade licence, helmet and challan rules. The evidence base can support a clear regulatory ask."),
        ("02","bot","Fix the pay & pressure design",
         "Order-count incentives and long hours reward speed over safety. Platform-level, scalable changes are the lever."),
        ("03","shield-check","Build a net riders can reach",
         "Most crashes go unreported and uncompensated. Reporting, guidance and insurance that pays out must follow."),
    ]
    cy=Inches(2.3); ch=Inches(3.0)
    for (x,w),(num,ic,t,d) in zip(cols(3,0.3), data):
        rect(s,x,cy,w,ch,fill=MIST,rounded=True,radius=0.05)
        pad=Inches(0.26); iw=Emu(int(w)-2*int(pad))
        icon_disc(s,ic,Emu(int(x)+int(pad)),cy+Inches(0.26),Inches(0.56),BR_T,hexs(BRAND),frac=0.5)
        text(s,Emu(int(x)+int(w)-int(Inches(0.8))),cy+Inches(0.28),Inches(0.6),Inches(0.4),num,
             font=HEAD,size=17,bold=True,color=LAVW,align=PP_ALIGN.RIGHT)
        text(s,Emu(int(x)+int(pad)),cy+Inches(1.04),iw,Inches(0.6),t,
             font=HEAD,size=14,bold=True,color=INK,ls=1.08)
        text(s,Emu(int(x)+int(pad)),cy+Inches(1.74),iw,Inches(1.1),d,size=10.5,color=MUT,ls=1.28)
    # closing brand strip
    by=Inches(5.66); bh=Inches(0.82)
    rect(s, ML, by, CW, bh, fill=BRAND, rounded=True, radius=0.08)
    text(s, Emu(int(ML)+int(Inches(0.3))), by, Emu(int(CW)-int(Inches(0.6))), bh,
         "An evidence base for platform engagement, regulatory clarity on EVs, and policy advocacy — "
         "built rider by rider.", font=HEAD, size=13, bold=True, color=PAPER, anchor=MSO_ANCHOR.MIDDLE, ls=1.2)
    foot(s,13,"What This Means")
s13()

# ================================================================ S14 CLOSE
def s14():
    s = slide(bg=BRAND)
    s.shapes.add_picture(LOGO_WHITE, ML, Inches(0.6), width=Inches(1.9))
    sparkles(s, PAPER)
    text(s, ML, Inches(2.5), Inches(11), Inches(0.4), "GIG RIDER SAFETY SURVEY  ·  PRELIMINARY FINDINGS",
         font=HEAD, size=11, bold=True, color=LAVW, tracking=2.4)
    text(s, ML, Inches(2.95), Inches(11), Inches(1.0), "Thank you",
         font=HEAD, size=44, bold=True, color=PAPER, ls=1.0)
    text(s, ML, Inches(4.0), Inches(10.5), Inches(0.7),
         "Preliminary findings from the Gig Rider Safety Survey. We welcome your questions as fieldwork continues.",
         size=13, color=LAVW, ls=1.35)
    # info columns
    hline(s, ML, Inches(5.25), CW, color=LAV_DK, wt=1.0)
    lx,rx = ML, Inches(7.1)
    text(s, lx, Inches(5.5), Inches(5.6), Inches(0.26), "PREPARED BY", font=HEAD, size=9, bold=True, color=LAVW, tracking=2.0)
    text(s, lx, Inches(5.82), Inches(5.6), Inches(0.3), "Crashfree India  with research partner Ayvole",
         font=HEAD, size=12.5, bold=True, color=PAPER, ls=1.0)
    text(s, lx, Inches(6.18), Inches(5.6), Inches(0.7),
         "Survey design & analysis in partnership · Qualitative consultations across enforcement, "
         "labour, transport & policy.", size=9.5, color=LAVW, ls=1.25)
    text(s, rx, Inches(5.5), Inches(5.6), Inches(0.26), "GET IN TOUCH", font=HEAD, size=9, bold=True, color=LAVW, tracking=2.0)
    text(s, rx, Inches(5.82), Inches(5.6), Inches(0.3), "crashfreeindia.org", font=HEAD, size=12.5, bold=True, color=PAPER, ls=1.0)
    text(s, rx, Inches(6.18), Inches(5.6), Inches(0.3), "aastha.shreeharsh@crashfreeindia.org", size=10.5, color=LAVW, ls=1.2)
    text(s, SW-MR-Inches(1.4), Inches(6.9), Inches(1.4), Inches(0.25), "14 / 14",
         size=8.5, color=LAVW, align=PP_ALIGN.RIGHT, ls=1.0)
s14()

save(OUT)

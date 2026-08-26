# CFI x TraffiCure / Google — discussion deck v2. 14 slides, text-light.
# SSI as the centerpiece (what/why/plan/together), TraffiCure data explained,
# one Rakshak-anchored hotspots idea, one small concrete DRSC idea.
import os
import build_nrsb3 as B
import nrsb2_style as ST
from nrsb2_style import *
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

I=Inches
V6=os.path.join(SP,"assets/v6/ready")
RMI=os.path.join(SP,"assets/rmi")
def a6(n): return os.path.join(V6,n)
def ar(n): return os.path.join(RMI,n)

TOTAL=15
AMB="#B26A00"

def ftc(s,idx):
    hline(s,ML,I(7.06),CW)
    text(s,ML,I(7.14),I(9),I(0.25),"Crashfree India  ·  Discussion deck · Crashfree India × TraffiCure, Google Maps Platform",size=8.5,color=MUT,ls=1.0)
    text(s,SW-MR-I(1.2),I(7.14),I(1.2),I(0.25),f"{idx:02d} / {TOTAL:02d}",size=8.5,color=MUT,align=PP_ALIGN.RIGHT,ls=1.0)

B.footer=lambda s,wg,idx,total: ftc(s,idx)
def _sect_tab(s,cur,name):
    w=I(3.6)
    text(s,SW-MR-w,I(0.30),w,I(0.24),name,font=HEAD,size=8.5,bold=True,color=MUT,tracking=1.6,align=PP_ALIGN.RIGHT)
ST.sect_tab=_sect_tab

def patch_rail(s,old,new):
    for sh in s.shapes:
        if sh.has_text_frame:
            for p in sh.text_frame.paragraphs:
                for r in p.runs:
                    if r.text and old in r.text:
                        r.text=r.text.replace(old,new)

def stat_tile(s,x,y,w,h,val,lab,tint=MIST,col=BRAND,vs=20):
    rect(s,x,y,w,h,fill=tint,rounded=True,radius=0.08)
    text(s,x+I(0.18),y+I(0.12),w-I(0.36),I(0.5),val,font=HEAD,size=vs,bold=True,color=col)
    text(s,x+I(0.18),y+I(0.66),w-I(0.36),h-I(0.75),lab,size=8.5,color=MUT,ls=1.18)

def amber_strip(s,y,lead,body,h=0.8):
    rect(s,ML,I(y),CW,I(h),fill=AM_T,rounded=True,radius=0.12)
    text(s,ML+I(0.25),I(y+0.1),CW-I(0.5),I(h-0.2),
         [(lead+" ",{'bold':True,'color':INK}),(body,{'color':INK})],size=10.5,ls=1.28)

# ---------------------------------------------------------------- 01 COVER
def cover():
    s=slide()
    s.shapes.add_picture(LOGO_BLUE,ML,I(0.5),width=I(1.85))
    text(s,SW-MR-I(3.5),I(0.55),I(3.5),I(0.3),"AUGUST 2026  ·  NEW DELHI",font=HEAD,size=9,bold=True,color=MUT,tracking=1.8,align=PP_ALIGN.RIGHT)
    text(s,ML,I(1.72),I(8.4),I(0.3),"FOR DISCUSSION  ·  CRASHFREE INDIA × TRAFFICURE · GOOGLE MAPS PLATFORM",font=HEAD,size=10,bold=True,color=BRAND,tracking=2.0)
    text(s,ML,I(2.14),I(8.3),I(0.85),"The safety layer",font=HEAD,size=46,bold=True,color=INK,ls=1.0)
    text(s,ML,I(3.1),I(8.3),I(0.85),"Traffic data already manages congestion.\nTogether it can start preventing crashes.",font=HEAD,size=16.5,bold=True,color=BRAND,ls=1.25)
    rows=[("school","Lead idea: the School Safety Index, prototype built, launching with government"),
          ("map-pin","Second idea: live crash hotspots, solved together through Project Rakshak"),
          ("handshake","Both run through government doors we already hold open")]
    y=I(4.65)
    for i,(ic,t) in enumerate(rows):
        icon_disc(s,ic,ML,y+i*I(0.62),I(0.4),BR_T,"#4A35FF")
        text(s,ML+I(0.56),y+i*I(0.62)+I(0.05),I(8.0),I(0.4),t,font=HEAD,size=11.5,bold=True,color=INK,ls=1.1)
    text(s,ML,I(6.9),I(8.6),I(0.3),"Ideas to shape together. Nothing here is a commitment.",size=9.5,color=MUT)
    text(s,SW-MR-I(2.6),I(6.9),I(2.6),I(0.3),"crashfreeindia.org",font=HEAD,size=9.5,bold=True,color=BRAND,align=PP_ALIGN.RIGHT)
    px=I(9.15); pw=I(3.55)
    photo_fit(s,ar("slide_ssi_index.png"),px,I(1.15),pw,I(2.9),caption="School Safety Index, Delhi NCR prototype, live.")
    photo(s,ar("defect_live.png"),px,I(4.55),pw,I(1.6),fill=True,anchor=0.0,
          caption="Road-Infrastructure Defect Repository, live.")
    return s

# ---------------------------------------------------------------- 02 TRAFFICURE, UNDERSTOOD
def tc_who():
    s=slide()
    header(s,"01 · Understanding TraffiCure",
           [("What TraffiCure is, ",False),("and what Pune proved",True)],
           lead="Software only. No cameras, no sensors. Google Maps probe data, turned into a working tool for the people who run the roads.",
           sect=(1,"TRAFFICURE"))
    rows=[("building-2","Built by Lepton Software","Google Maps Platform Premier Partner, working with Google since 2010. TraffiCure launched 2025.",BR_T,"#4A35FF"),
          ("gauge","Runs on Roads Management Insights","Google's public-sector traffic feed, launched Aug 2025. Every road, refreshed every 2 minutes.",TE_T,"#0E8A8A"),
          ("landmark","Live with Pune City Traffic Police","Deployed January 2026, activated in weeks. Corridors also measured in Delhi, Hyderabad, Ahmedabad.",GR_T,"#0A9955")]
    y=I(2.25)
    for i,(ic,t,d,tint,col) in enumerate(rows):
        irow(s,ML,y+i*I(0.92),I(7.5),ic,t,d,tint,col,tsize=11,dsize=9.5)
    text(s,ML,I(5.15),I(7.5),I(0.3),"THE PUNE RESULT, POLICE-MEASURED",font=HEAD,size=9,bold=True,color=MUT,tracking=1.8)
    tiles=[("964 roads","watched live, every 2 minutes","20 → 26.8","km/h average speed in one year"),]
    stat_tile(s,ML,I(5.5),I(2.4),I(1.15),"964","roads watched live, every 2 minutes")
    stat_tile(s,ML+I(2.55),I(5.5),I(2.4),I(1.15),"20 → 26.8","km/h average speed, in a year")
    stat_tile(s,ML+I(5.1),I(5.5),I(2.4),I(1.15),"22","worst junctions ranked and briefed")
    px=I(8.55); pw=I(4.15)
    rect(s,px,I(2.25),pw,I(4.35),fill=PAPER,line=LINE,rounded=True,radius=0.06)
    text(s,px+I(0.22),I(2.45),pw-I(0.44),I(0.3),"WHY PUNE MATTERS TO US",font=HEAD,size=9,bold=True,color=BRAND,tracking=1.6)
    text(s,px+I(0.22),I(2.85),pw-I(0.44),I(3.5),
         "The police did not stop at watching traffic.\n\nThey ranked their worst junctions, diagnosed why each fails, and handed the municipal corporation an engineering brief. Fixes got built.\n\nData → ranked list → brief to authority → built fix.\n\nThat is exactly how Project Rakshak works. Same operating theory, different data.",size=10,color=INK,ls=1.35)
    ftc(s,2)
    return s

# ---------------------------------------------------------------- 03 THE DATA, SAFETY LENS
def tc_data():
    s=slide()
    header(s,"01 · Understanding the data",
           [("Five signals in the feed, ",False),("read through a safety lens",True)],
           lead="The product was built to manage traffic. Every signal in it has a second life in safety.",
           sect=(1,"THE DATA"))
    rows=[("gauge","Live speeds","Every road, every 2 minutes","How fast traffic really moves past a school gate at 8 am.",BR_T,"#4A35FF",""),
          ("database","Speed history","Hourly, by road, in BigQuery","Baselines: what is normal, what changed after a fix was built.",TE_T,"#0E8A8A",""),
          ("users","Vehicle counts","Per road, per hour","Exposure: how many vehicles pass the danger. Priority = risk × exposure.",GR_T,"#0A9955","NEW · MAY 2026"),
          ("zap","Harsh braking","Anonymised points, junction scale","Near-misses, visible before the crash. Their guide calls it the safety signal nobody else has.",AM_T,"#B26A00","NEW · MAY 2026"),
          ("bot","User-reported incidents","Crashes and hazards, from Maps users","Incidents the official record may never see.",BR_T,"#4A35FF","NEW · MAY 2026")]
    y=I(2.2)
    for i,(ic,t,what,use,tint,col,tag) in enumerate(rows):
        yy=y+i*I(0.88)
        rect(s,ML,yy,CW,I(0.76),fill=PAPER if i%2 else MIST,rounded=True,radius=0.10)
        icon_disc(s,ic,ML+I(0.18),yy+I(0.15),I(0.46),tint,col)
        text(s,ML+I(0.82),yy+I(0.12),I(1.9),I(0.5),t,font=HEAD,size=11.5,bold=True,color=INK,ls=1.05)
        text(s,ML+I(0.82),yy+I(0.45),I(2.6),I(0.26),what,size=8.5,color=MUT,ls=1.1)
        text(s,ML+I(3.7),yy+I(0.14),I(6.2),I(0.55),use,size=10,color=INK,ls=1.2)
        if tag:
            chip(s,SW-MR-I(1.75),yy+I(0.21),I(1.6),I(0.34),tag,fill=AM_T,color=RGBColor(0xB2,0x6A,0x00),size=7.5)
    ftc(s,3)
    return s

# ---------------------------------------------------------------- 04 AGENDA (light)
def agenda():
    s=slide()
    text(s,ML,I(0.30),I(8),I(0.24),"WHAT WE BRING TO DISCUSS",font=HEAD,size=9,bold=True,color=BRAND,tracking=2.2)
    hline(s,ML,I(0.62),I(0.55),color=BRAND,wt=2.0)
    text(s,ML,I(0.76),I(12),I(0.5),[("Two ideas we believe in, ",{'color':INK}),("one small one, and our questions",{'color':BRAND})],font=HEAD,size=22.5,bold=True,ls=1.1)
    rows=[("school","Idea 01 · School Safety Index × speed","The centrepiece: what is built, why it matters, the plan, and how we do it together.","05 – 08"),
          ("map-pin","Idea 02 · Live hotspots × Project Rakshak","The feed keeps the crash map alive; Rakshak turns it into audits, joint plans and built fixes.","09 – 10"),
          ("landmark","Idea 03 · The DRSC data pack","Small and immediate: the feed, summarised monthly, on the table where districts decide.","11"),
          ("building-2","About us, briefly","Who we are and SATARK, our enforcement platform with police.","12 – 13"),
          ("handshake","Next steps","Three steps, two questions, one date to fix.","14")]
    y=I(1.72)
    for i,(ic,t,d,pg) in enumerate(rows):
        yy=y+i*I(1.02)
        rect(s,ML,yy,CW,I(0.88),fill=MIST if i%2==0 else PAPER,line=LINE if i%2 else None,rounded=True,radius=0.10)
        num_disc(s,ML+I(0.22),yy+I(0.2),I(0.48),i+1)
        icon_disc(s,ic,ML+I(0.95),yy+I(0.2),I(0.48),BR_T,"#4A35FF")
        text(s,ML+I(1.68),yy+I(0.13),I(6.6),I(0.4),t,font=HEAD,size=13,bold=True,color=INK,ls=1.0)
        text(s,ML+I(1.68),yy+I(0.46),I(8.2),I(0.35),d,size=10,color=MUT,ls=1.15)
        text(s,SW-MR-I(1.75),yy+I(0.24),I(1.5),I(0.4),pg,font=HEAD,size=12,bold=True,color=BRAND,align=PP_ALIGN.RIGHT)
    ftc(s,4)
    return s

# ---------------------------------------------------------------- 05 SSI: WHAT IT IS
def ssi_what():
    s=slide()
    header(s,"02 · Idea 01 · School Safety Index",
           [("A public grade for the road ",False),("outside every school gate",True)],
           lead="Prototype built and live. It grades the road, never the school, against IRC:SP:32, India's own school-zone standard.",
           sect=(2,"IDEA 01 · SSI"))
    stat_tile(s,ML,I(2.3),I(2.4),I(1.3),"3,814","Delhi NCR schools mapped, prototype live",vs=22)
    stat_tile(s,ML+I(2.55),I(2.3),I(2.4),I(1.3),"44","checks per school zone, from IRC:SP:32",vs=22)
    stat_tile(s,ML+I(5.1),I(2.3),I(2.4),I(1.3),"0–100","score per school, evidence photos pinned",vs=22)
    rows=[("scan-line","How a school gets its grade","Street View imagery of the gate zone, scored by an AI auditor, independently verified before anything is published."),
          ("footprints","Grades that demand action","A low grade is a demand on the road-owning authority: the missing crossing, the absent speed hump, the broken footpath."),
          ("landmark","Launch with government, planned","Public launch being prepared with a government partner; our four district committee seats carry the worst zones into the statutory forum.")]
    y=I(3.95)
    for i,(ic,t,d) in enumerate(rows):
        irow(s,ML,y+i*I(0.9),I(7.5),ic,t,d,BR_T,"#4A35FF",tsize=11,dsize=9.5)
    px=I(8.55); pw=I(4.15)
    photo_fit(s,ar("slide_ssi_index.png"),px,I(2.3),pw,I(2.15),caption="The index, worst grades first.")
    photo_fit(s,ar("slide_ssi_school.png"),px,I(4.75),pw,I(1.9),caption="A school's report card, evidence pinned.")
    ftc(s,5)
    return s

# ---------------------------------------------------------------- 06 SSI: WHY IT MATTERS
def ssi_why():
    s=slide()
    header(s,"02 · Idea 01 · Why this matters",
           [("Children die at fixable places, ",False),("and nobody keeps score",True)],
           lead="The standard exists. The danger is measurable. What is missing is a public number that makes someone act.",
           sect=(2,"IDEA 01 · SSI"))
    tiles=[("~10,000","minors died on Indian roads in 2023 (MoRTH)"),
           ("4.6%","of crashes happen in school and college zones (e-DAR)"),
           ("10% → 90%","a child pedestrian's fatality risk, 30 vs 70 km/h impact"),
           ("0","Indian cities that rank school-zone danger today")]
    tw=I(2.87); gx=I(0.14)
    for j,(v,l) in enumerate(tiles):
        stat_tile(s,ML+j*(tw+gx),I(2.3),tw,I(1.35),v,l,vs=21)
    rows=[("users","A number parents understand","A grade at the gate makes invisible risk visible to the people with the most reason to demand the fix."),
          ("landmark","A number authorities can act on","Worst-first rankings become work orders: which 10 zones, which fixes, this budget cycle — through committees we already sit on."),
          ("git-compare","A number that proves change","Re-grade after the fix is built. With the speed layer, the improvement is measured, not claimed.")]
    y=I(4.1)
    for i,(ic,t,d) in enumerate(rows):
        irow(s,ML,y+i*I(0.9),I(12.0),ic,t,d,GR_T,"#0A9955",tsize=11,dsize=9.5)
    ftc(s,6)
    return s

# ---------------------------------------------------------------- 07 SSI: THE PLAN
def ssi_plan():
    s=slide()
    header(s,"02 · Idea 01 · The plan",
           [("From prototype ",False),("to public institution",True)],
           lead="Four phases. The first is done. The speed layer is where TraffiCure changes what this can be.",
           sect=(2,"IDEA 01 · SSI"))
    cards=[("DONE","Prototype","Delhi NCR: 3,814 schools mapped, rubric built on IRC:SP:32, pilot report cards live with pinned evidence.",GR_T,"#0A9955"),
           ("NOW","Government launch","Validated first batch of ~100 zones; DRSC resolution; public launch with a named government partner.",BR_T,"#4A35FF"),
           ("WITH YOU","The speed layer","Speed past the gate at school-run hours, harsh braking, vehicle counts: every school ranked by measured danger, a first for India.",AM_T,"#B26A00"),
           ("THEN","Fix, re-grade, scale","Worst zones into Rakshak audits and authority work orders; re-graded after fixes; Jaipur next, 1,572 schools already mapped.",TE_T,"#0E8A8A")]
    cwid=I(2.87); gx=I(0.14)
    for j,(tag,t,d,tint,col) in enumerate(cards):
        x=ML+j*(cwid+gx); y=I(2.35)
        rect(s,x,y,cwid,I(3.5),fill=PAPER,line=LINE,rounded=True,radius=0.06)
        chip(s,x+I(0.18),y+I(0.2),I(1.25),I(0.34),tag,fill=tint,color=RGBColor(*[int(col[i:i+2],16) for i in (1,3,5)]),size=8)
        text(s,x+I(0.18),y+I(0.68),cwid-I(0.36),I(0.4),t,font=HEAD,size=13,bold=True,color=INK,ls=1.05)
        text(s,x+I(0.18),y+I(1.15),cwid-I(0.36),I(2.2),d,size=9.5,color=MUT,ls=1.3)
        if j<3:
            text(s,x+cwid+I(0.005),y+I(1.5),I(0.14),I(0.4),"›",font=HEAD,size=16,bold=True,color=MUT)
    amber_strip(s,6.1,"The honest gate:","the speed layer ships only if RMI segments resolve short gate streets and school-run-hour slices. One technical session on 10 corridors we have already defined settles it in a week.")
    ftc(s,7)
    return s

# ---------------------------------------------------------------- 08 SSI: TOGETHER / NEXT STEPS
def ssi_next():
    s=slide()
    header(s,"02 · Idea 01 · How we take it forward",
           [("Clear roles, ",False),("three steps, one date",True)],
           lead="We hold the method and the government seats. You hold the data and the tooling. The launch names both.",
           sect=(2,"IDEA 01 · SSI"))
    x1=ML; w=I(5.9)
    rect(s,x1,I(2.2),w,I(2.5),fill=BR_T,rounded=True,radius=0.06)
    text(s,x1+I(0.22),I(2.38),w-I(0.44),I(0.28),"CRASHFREE INDIA",font=HEAD,size=9.5,bold=True,color=BRAND,tracking=1.6)
    for k,t in enumerate(["Index method, verification, publication","Field checks by student teams at worst-graded zones","DRSC resolutions and the government launch"]):
        icon(s,"badge-check",x1+I(0.24),I(2.82+k*0.55),I(0.24),"#4A35FF")
        text(s,x1+I(0.6),I(2.79+k*0.55),w-I(0.8),I(0.45),t,size=10,color=INK,ls=1.2)
    x2=ML+w+I(0.28)
    rect(s,x2,I(2.2),w,I(2.5),fill=GR_T,rounded=True,radius=0.06)
    text(s,x2+I(0.22),I(2.38),w-I(0.44),I(0.28),"TRAFFICURE + GOOGLE",font=HEAD,size=9.5,bold=True,color=GREEN,tracking=1.6)
    for k,t in enumerate(["Speed, braking and count layers per school zone","Corridor tooling and school-run-hour slices","Terms for a public, attributed, nonprofit index"]):
        icon(s,"badge-check",x2+I(0.24),I(2.82+k*0.55),I(0.24),"#0A9955")
        text(s,x2+I(0.6),I(2.79+k*0.55),w-I(0.8),I(0.45),t,size=10,color=INK,ls=1.2)
    text(s,ML,I(5.0),I(12),I(0.3),"NEXT STEPS",font=HEAD,size=9,bold=True,color=MUT,tracking=1.8)
    steps=[("1","This week","Technical session: Lepton + Maps + CFI on 10 gate corridors, already defined on our cloud project."),
           ("2","Weeks 2 – 6","Joint speed-exposure scoring on the ~100-zone launch batch, thresholds agreed up front."),
           ("3","Launch window","Government launch of the index with the speed layer in, both names on it.")]
    for j,(n,w2,d) in enumerate(steps):
        x=ML+j*I(4.03); y=I(5.35)
        rect(s,x,y,I(3.9),I(1.25),fill=MIST,rounded=True,radius=0.10)
        num_disc(s,x+I(0.16),y+I(0.16),I(0.4),int(n))
        text(s,x+I(0.68),y+I(0.14),I(3.1),I(0.28),w2,font=HEAD,size=9.5,bold=True,color=BRAND)
        text(s,x+I(0.16),y+I(0.52),I(3.6),I(0.68),d,size=9,color=INK,ls=1.2)
    ftc(s,8)
    return s

# ---------------------------------------------------------------- 09 IDEA 2: HOTSPOTS x RAKSHAK
def hotspots():
    s=slide()
    header(s,"03 · Idea 02 · Live hotspots × Project Rakshak",
           [("Keep the crash map alive, ",False),("then fix what it shows",True)],
           lead="Official blackspot lists update every few years. The feed can refresh the danger map monthly — and Rakshak already turns danger maps into built fixes.",
           sect=(3,"IDEA 02 · RAKSHAK"))
    # the loop: 6 chips with arrows, 2 rows
    flow=[("zap","Live signals","speeds · braking · counts"),
          ("map-pin","+ Crash records","police e-DAR, via our DRSC seats"),
          ("layers","Live hotspot list","risk-ranked, refreshed monthly"),
          ("search-check","Rakshak audit","student teams + certified auditors"),
          ("landmark","Joint plan to authority","the Pune move, for safety"),
          ("git-compare","Fix built & measured","before/after speeds, public dashboard")]
    cwid=I(3.8); ch=I(1.15); gx=I(0.35); gy=I(0.5)
    # serpentine: top row flows right, wraps down, bottom row flows left
    cols_for=[0,1,2,2,1,0]
    for k,(ic,t,d) in enumerate(flow):
        r=k//3; c=cols_for[k]
        x=ML+I(0.2)+c*(cwid+gx); y=I(2.35)+r*(ch+gy)
        rect(s,x,y,cwid,ch,fill=BR_T if k in (2,4) else PAPER,line=LINE,rounded=True,radius=0.10)
        icon_disc(s,ic,x+I(0.16),y+I(0.16),I(0.44),MIST if k in (2,4) else BR_T,"#4A35FF")
        text(s,x+I(0.74),y+I(0.16),cwid-I(0.9),I(0.35),t,font=HEAD,size=11.5,bold=True,color=INK,ls=1.0)
        text(s,x+I(0.74),y+I(0.55),cwid-I(0.9),I(0.5),d,size=9,color=MUT,ls=1.15)
        if k in (0,1):
            text(s,x+cwid+I(0.04),y+I(0.35),I(0.3),I(0.4),"›",font=HEAD,size=18,bold=True,color=BRAND)
        if k in (4,5):
            text(s,x+cwid+I(0.04),y+I(0.35),I(0.3),I(0.4),"‹",font=HEAD,size=18,bold=True,color=BRAND)
    # wrap arrow: from hotspot list (top-right) straight down into Rakshak audit (bottom-right)
    text(s,ML+I(0.2)+2*(cwid+gx)+cwid/2-I(0.1),I(3.62),I(0.4),I(0.4),"⌄",font=HEAD,size=18,bold=True,color=BRAND)
    amber_strip(s,5.85,"Why it works:","every piece already runs. 150+ audits planned this year, 15 fixes in implementation, 25+ authority approvals, dashboards live. The feed adds the one thing we cannot make: a danger map that never goes stale.",h=0.85)
    ftc(s,9)
    return s

# ---------------------------------------------------------------- 10 IDEA 2: READY + NEXT
def hotspots_next():
    s=slide()
    header(s,"03 · Idea 02 · What exists, and the next 90 days",
           [("Nothing to invent — ",False),("three moves to make",True)],
           lead="The audit machine, the government doors and the public dashboard exist. The feed plugs into all three.",
           sect=(3,"IDEA 02 · RAKSHAK"))
    stat_tile(s,ML,I(2.25),I(2.87),I(1.3),"96","police-mapped crash clusters in Jaipur, 361 GPS-located crashes",vs=22)
    stat_tile(s,ML+I(3.01),I(2.25),I(2.87),I(1.3),"150+","blackspot audits planned this Rakshak year",vs=22)
    stat_tile(s,ML+I(6.02),I(2.25),I(2.87),I(1.3),"75+","implementations targeted, each with a build date",vs=22)
    stat_tile(s,ML+I(9.03),I(2.25),I(2.87),I(1.3),"4","district committees where a joint plan can be tabled",vs=22)
    steps=[("1","Overlay","Harsh braking + speeds over Jaipur's 96 clusters. Does the feed see the danger police already know? Four weeks, answer either way."),
           ("2","Baseline","Subscribe corridors for 2 Rakshak sites entering construction now — so before/after proof starts with the build, not after it."),
           ("3","Dashboard","A live speed panel per site on the public Rakshak dashboard: 'measured with Google road data'. The joint plan, visible to everyone.")]
    for j,(n,t,d) in enumerate(steps):
        x=ML+j*I(4.03); y=I(3.85)
        rect(s,x,y,I(3.9),I(2.0),fill=PAPER,line=LINE,rounded=True,radius=0.06)
        num_disc(s,x+I(0.18),y+I(0.18),I(0.44),int(n))
        text(s,x+I(0.76),y+I(0.24),I(3.0),I(0.35),t,font=HEAD,size=12.5,bold=True,color=INK)
        text(s,x+I(0.18),y+I(0.72),I(3.55),I(1.2),d,size=9.5,color=MUT,ls=1.28)
    amber_strip(s,6.1,"The honest gate:","if braking density is too thin at Jaipur's clusters, idea 02 narrows to before/after proof only — still worth having, and we say so in writing at day 30.")
    ftc(s,10)
    return s

# ---------------------------------------------------------------- 11 IDEA 3: DRSC PACK
def drsc_pack():
    s=slide()
    header(s,"04 · Idea 03 · Small, immediate",
           [("The DRSC data pack: ",False),("the feed, where decisions are made",True)],
           lead="District Road Safety Committees meet on a statutory calendar and decide with anecdotes. We sit on four of them.",
           sect=(4,"IDEA 03 · DRSC"))
    rows=[("landmark","What it is","One page per district, every month: speeds on the worst corridors, school-gate speeds, changes since last meeting. We format it; the committee decides with it."),
          ("timer","Why it is easy","Feed access for four districts, a template, nothing else. Live within a month of access; no product build, no launch, no risk."),
          ("globe","What it does for you","Google's data enters the statutory record of four districts, every month, attributed — the quietest, fastest government-partnership story in this deck.")]
    y=I(2.35)
    for i,(ic,t,d) in enumerate(rows):
        irow(s,ML,y+i*I(1.05),I(7.5),ic,t,d,BR_T,"#4A35FF",tsize=11,dsize=9.5)
    px=I(8.55); pw=I(4.15)
    rect(s,px,I(2.35),pw,I(3.2),fill=MIST,rounded=True,radius=0.06)
    text(s,px+I(0.22),I(2.55),pw-I(0.44),I(0.3),"THE PACK, EACH MONTH",font=HEAD,size=9,bold=True,color=BRAND,tracking=1.6)
    items=["Worst 5 corridors by measured speed","School gates above safe speed at 8 am","Change since last meeting, corridor by corridor","One before/after: did last month's action work?"]
    for k,t in enumerate(items):
        icon(s,"badge-check",px+I(0.24),I(3.0+k*0.6),I(0.24),"#4A35FF")
        text(s,px+I(0.6),I(2.97+k*0.6),pw-I(0.85),I(0.5),t,size=9.5,color=INK,ls=1.2)
    ftc(s,11)
    return s

# ---------------------------------------------------------------- 12 ABOUT
def about_tiles():
    s=slide()
    header(s,"05 · About us",[("Six lines of work, ",False),("one connected system",True)],
           lead="A nonprofit registered as the Vision Zero Trust · Co-founded by Cars24 and the Indian Road Safety Council · 18 cities · everything below is live.",
           sect=(5,"ABOUT US"))
    tiles=[("Project Rakshak","Student-led road audits, fixed with authorities","31 sites · 15 in implementation",a5("implementation_work.jpg"),0.30),
           ("SATARK enforcement","AI support that helps police find high-risk vehicles","3,00,000+ vehicles screened",a5("satark_billboard.jpg"),0.42),
           ("Victim support","Aasha chatbot, calculator, hospital helpdesks","100+ victims helped in first 4 days",a5("ph_helpdesk_desk.jpg"),0.25),
           ("Open public data","Four self-updating data platforms, free to use","36 states & 50 cities covered",a5("sctracker.png"),0.05),
           ("School Safety Index","Public grading of school-zone road safety","3,814 Delhi NCR schools mapped",ar("slide_ssi_school.png"),0.0),
           ("Youth & policy","NextMile ideathon and national dialogue series","2,000+ participants engaged",a5("ph_ideathon_winners.jpg"),0.25)]
    tw=I(3.95); th=I(2.32); gx=I(0.12); gy=I(0.16)
    for i,(t,d,st,img,anc) in enumerate(tiles):
        r,c=divmod(i,3)
        x=ML+c*(tw+gx); y=I(2.12)+r*(th+gy)
        rect(s,x,y,tw,th,fill=PAPER,line=LINE,rounded=True,radius=0.06)
        photo(s,img,x,y,tw,I(1.28),fill=True,border=False,anchor=anc)
        rect(s,x,y,tw,I(1.28),fill=None,line=LINE,lw=1.0)
        text(s,x+I(0.14),y+I(1.36),tw-I(0.28),I(0.3),t,font=HEAD,size=11.5,bold=True,color=INK,ls=1.0)
        text(s,x+I(0.14),y+I(1.62),tw-I(0.28),I(0.35),d,size=9,color=MUT,ls=1.12)
        text(s,x+I(0.14),y+I(2.02),tw-I(0.28),I(0.26),st,font=HEAD,size=9,bold=True,color=BRAND,ls=1.0)
    ftc(s,12)
    return s

# ---------------------------------------------------------------- 13 SATARK
def satark_slide():
    s=B.satark(13,TOTAL,None)
    patch_rail(s,"02 · WHAT WE HAVE BUILT, ENFORCEMENT TECHNOLOGY","05 · ABOUT US, SATARK IN THE FIELD")
    patch_rail(s,"02 · What we have built, enforcement technology","05 · About us, SATARK in the field")
    patch_rail(s,"WHAT WE HAVE BUILT","ABOUT US")
    return s

# ---------------------------------------------------------------- 14 NEXT STEPS + QUESTIONS
def nextsteps():
    s=slide()
    header(s,"06 · Where we would take this",
           [("Three steps, two questions, ",False),("one date to fix",True)],
           lead="Everything on our side is funded and ready. The first step costs one afternoon.",
           sect=(6,"NEXT STEPS"))
    text(s,ML,I(2.1),I(12),I(0.3),"THREE STEPS",font=HEAD,size=9,bold=True,color=MUT,tracking=1.8)
    steps=[("1","Fix the technical session","Lepton + Maps + CFI, on real data: 10 school-gate corridors and Jaipur's 96 crash clusters, ready on our configured cloud project."),
           ("2","Run the two overlays","SSI speed scoring on the ~100-zone launch batch; braking over Jaipur's clusters. Thresholds agreed up front, results shared either way."),
           ("3","Put both names on what survives","The index launch with government, and the live speed panel on the Rakshak dashboard.")]
    for j,(n,t,d) in enumerate(steps):
        x=ML+j*I(4.03); y=I(2.45)
        rect(s,x,y,I(3.9),I(1.85),fill=PAPER,line=LINE,rounded=True,radius=0.06)
        num_disc(s,x+I(0.18),y+I(0.18),I(0.44),int(n))
        text(s,x+I(0.76),y+I(0.24),I(3.0),I(0.35),t,font=HEAD,size=12,bold=True,color=INK,ls=1.05)
        text(s,x+I(0.18),y+I(0.78),I(3.55),I(1.0),d,size=9.5,color=MUT,ls=1.28)
    text(s,ML,I(4.6),I(12),I(0.3),"TWO QUESTIONS",font=HEAD,size=9,bold=True,color=MUT,tracking=1.8)
    qs=[("database","Access & terms","Can a nonprofit public index sit on the feed — braking and counts included — with attribution? Through Google, Lepton, or both?"),
        ("landmark","Which doors matter","Which cities and stories help TraffiCure and RMI most next quarter? Our seats and MoUs work best pointed somewhere specific.")]
    for j,(ic,t,d) in enumerate(qs):
        x=ML+j*I(6.18); y=I(4.95)
        rect(s,x,y,I(5.9),I(1.6),fill=MIST,rounded=True,radius=0.06)
        icon_disc(s,ic,x+I(0.2),y+I(0.2),I(0.44),BR_T,"#4A35FF")
        text(s,x+I(0.82),y+I(0.26),I(4.9),I(0.35),t,font=HEAD,size=12,bold=True,color=INK)
        text(s,x+I(0.22),y+I(0.72),I(5.5),I(0.8),d,size=9.5,color=MUT,ls=1.25)
    ftc(s,14)
    return s

# ---------------------------------------------------------------- 15 CLOSE -> becomes 14? keep separate close
def close():
    s=slide(bg=BRAND)
    s.shapes.add_picture(LOGO_WHITE,ML,I(0.62),width=I(2.0))
    text(s,ML,I(2.0),I(12.1),I(1.5),"Traffic data already runs the daily commute.\nTogether it can start preventing the crash.",font=HEAD,size=30,bold=True,color=PAPER,ls=1.2)
    text(s,ML,I(3.8),I(11.5),I(0.6),"Two ideas we believe in, one small one, and a technical session that settles the open questions in an afternoon.",size=12.5,color=LAVW,ls=1.4)
    hline(s,ML,I(4.6),I(5.2),color=RGBColor(0x6A,0x55,0xFF),wt=1.0)
    cols=[("Akhtar Hussain","Mission Lead","akhtar@crashfreeindia.org"),
          ("Deepanshu Gupta","Trustee","deepanshu@crashfreeindia.org"),
          ("Gajendra Jangid","Trustee","gajendra@crashfreeindia.org")]
    for j,(n,r,e) in enumerate(cols):
        x=ML+j*I(4.0)
        text(s,x,I(4.9),I(3.8),I(0.3),n,font=HEAD,size=13,bold=True,color=PAPER)
        text(s,x,I(5.24),I(3.8),I(0.28),f"{r} · {e}",size=9.5,color=LAVW)
    text(s,ML,I(7.05),I(12),I(0.3),"Crashfree India · A Cars24 commitment · Operated by Vision Zero Trust, New Delhi · crashfreeindia.org",size=9.5,color=LAVW)
    return s

if __name__=="__main__":
    new_deck()
    cover()          # 01
    tc_who()         # 02
    tc_data()        # 03
    agenda()         # 04
    ssi_what()       # 05
    ssi_why()        # 06
    ssi_plan()       # 07
    ssi_next()       # 08
    hotspots()       # 09
    hotspots_next()  # 10
    drsc_pack()      # 11
    about_tiles()    # 12
    satark_slide()   # 13
    nextsteps()      # 14
    close()          # 15
    save(os.path.join(BUILD,"CFI_Trafficure_v2.pptx"))

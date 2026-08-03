# CFI x Google Maps Platform (Roads Management Insights) pre-read, revamped on the
# NRSB white-paper design system. 14 slides.
import os
from nrsb2_style import *
from pptx.util import Inches, Pt, Emu
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

I=Inches
V6=os.path.join(SP,"assets/v6/ready")
RMI=os.path.join(SP,"assets/rmi")
def a6(n): return os.path.join(V6,n)
def ar(n): return os.path.join(RMI,n)

TOTAL=14

def frmi(s,idx):
    hline(s,ML,I(7.06),CW)
    text(s,ML,I(7.14),I(9),I(0.25),"Crashfree India  ·  Pre-read for Google Maps Platform, Roads Management Insights",size=8.5,color=MUT,ls=1.0)
    text(s,SW-MR-I(1.2),I(7.14),I(1.2),I(0.25),f"{idx:02d} / {TOTAL:02d}",size=8.5,color=MUT,align=PP_ALIGN.RIGHT,ls=1.0)

# ---------------------------------------------------------------- 01 COVER
def cover():
    s=slide()
    s.shapes.add_picture(LOGO_BLUE,ML,I(0.5),width=I(1.85))
    text(s,SW-MR-I(3.5),I(0.55),I(3.5),I(0.3),"AUGUST 2026  ·  NEW DELHI",font=HEAD,size=9,bold=True,color=MUT,tracking=1.8,align=PP_ALIGN.RIGHT)
    text(s,ML,I(1.72),I(8.2),I(0.3),"PRE-READ  ·  CRASHFREE INDIA × GOOGLE MAPS PLATFORM",font=HEAD,size=10.5,bold=True,color=BRAND,tracking=2.2)
    text(s,ML,I(2.14),I(8.3),I(0.85),"Crashfree India",font=HEAD,size=46,bold=True,color=INK,ls=1.0)
    text(s,ML,I(3.1),I(8.3),I(0.85),"Our public road-safety products, and where\nRoads Management Insights fits them",font=HEAD,size=16.5,bold=True,color=BRAND,ls=1.25)
    rows=[("database","Live public data products: defect repository, school safety index, open dashboards"),
          ("landmark","Working inside government: 4 district committees, police MoUs, 25+ written approvals"),
          ("rocket","A pilot ready to start: cloud project configured, Jaipur corridors defined from police records")]
    icons=["database","landmark","rocket"]
    y=I(4.65)
    for i,(ic,t) in enumerate(rows):
        icon_disc(s,ic,ML,y+i*I(0.62),I(0.4),BR_T,"#4A35FF")
        text(s,ML+I(0.56),y+i*I(0.62)+I(0.05),I(8.0),I(0.4),t,font=HEAD,size=11.5,bold=True,color=INK,ls=1.1)
    text(s,ML,I(6.9),I(8.6),I(0.3),"Prepared for the Roads Management Insights team, Google Maps Platform",size=9.5,color=MUT)
    text(s,SW-MR-I(2.6),I(6.9),I(2.6),I(0.3),"crashfreeindia.org",font=HEAD,size=9.5,bold=True,color=BRAND,align=PP_ALIGN.RIGHT)
    px=I(9.15); pw=I(3.55)
    photo(s,ar("defect_live.png"),px,I(1.15),pw,I(1.60),fill=True,anchor=0.0,
          caption="The Defect Repository, live, 3 Aug 2026.")
    photo_fit(s,ar("slide_ssi_index.png"),px,I(3.2),pw,I(2.85),caption="The School Safety Index, Delhi NCR pilot.")
    return s

# ---------------------------------------------------------------- 02 AGENDA
def agenda():
    s=slide()
    text(s,ML,I(0.30),I(8),I(0.24),"HOW THIS PRE-READ IS ORGANISED",font=HEAD,size=9,bold=True,color=BRAND,tracking=2.2)
    hline(s,ML,I(0.62),I(0.55),color=BRAND,wt=2.0)
    text(s,ML,I(0.76),I(12),I(0.5),[("Five sections, ",{'color':INK}),("from who we are to a ready pilot",{'color':BRAND})],font=HEAD,size=22.5,bold=True,ls=1.1)
    rows=[("building-2","About us","Who we are, and the public products we already run.","03 – 05"),
          ("landmark","Where we work with government","District committees, police partnerships and written authority approvals.","06"),
          ("gauge","Why speed data, and our read of RMI","The evidence on speed, what we understand RMI provides, what we would like to learn.","07 – 08"),
          ("layers","Three product directions","The Defect Repository, the School Safety Index, and an exploratory enforcement direction.","09 – 11"),
          ("handshake","A ready pilot, and this call","What is already configured, the pilot we propose, and the questions we bring.","12 – 13")]
    y=I(1.72)
    for i,(ic,t,d,pg) in enumerate(rows):
        yy=y+i*I(1.02)
        rect(s,ML,yy,CW,I(0.88),fill=MIST if i%2==0 else PAPER,line=LINE if i%2 else None,rounded=True,radius=0.10)
        num_disc(s,ML+I(0.22),yy+I(0.2),I(0.48),i+1)
        icon_disc(s,ic,ML+I(0.95),yy+I(0.2),I(0.48),BR_T,"#4A35FF")
        text(s,ML+I(1.68),yy+I(0.13),I(5.2),I(0.4),t,font=HEAD,size=13,bold=True,color=INK,ls=1.0)
        text(s,ML+I(1.68),yy+I(0.46),I(8.2),I(0.35),d,size=10,color=MUT,ls=1.15)
        text(s,SW-MR-I(1.75),yy+I(0.24),I(1.5),I(0.4),pg,font=HEAD,size=12,bold=True,color=BRAND,align=PP_ALIGN.RIGHT)
    frmi(s,2)
    return s

# ---------------------------------------------------------------- 03 ABOUT
def about():
    s=slide()
    header(s,"01 · About us",[("Crashfree India: a nonprofit that adds ",False),("capacity",True),(" to road safety work",False)],
           lead="Registered as the Vision Zero Trust · Co-founded by Cars24 and the Indian Road Safety Council · Working since June 2025 · New Delhi",
           sect=(1,"ABOUT US"))
    rows=[("search-check","Evidence first","Structured field audits, file reviews and research to official standards, IRC codes and MoRTH checklists.",GR_T,"#0A9955"),
          ("landmark","Institutional collaboration","We work through PWDs, NHAI, transport departments, police and District Road Safety Committees.",BR_T,"#4A35FF"),
          ("users","Youth-led capacity","Trained student teams from IITs, NITs and SPAs add the auditing hands the system needs.",AM_T,"#E58900"),
          ("monitor-check","Technology for follow-through","Public dashboards track every recommendation from submission to completion.",TE_T,"#0E8A8A")]
    y=I(2.2)
    for i,(ic,t,d,tint,col) in enumerate(rows):
        irow(s,ML,y+i*I(0.82),I(7.6),ic,t,d,tint,col)
    rect(s,ML,I(5.65),I(7.55),I(0.92),fill=BR_T,rounded=True,radius=0.16)
    text(s,ML+I(0.25),I(5.72),I(7.1),I(0.8),
         [("Every product in this pre-read is live, public and free: ",{'bold':True,'color':BRAND}),
          ("built once, used by authorities every week, and designed to be shared.",{'color':BRAND})],size=11.5,ls=1.3)
    photo(s,a5("cfi_map_dots.png"),I(8.85),I(2.15),I(3.6),caption="Where we work today, 18 cities, north to south.")
    frmi(s,3)
    return s

# ---------------------------------------------------------------- 04 PORTFOLIO
def portfolio():
    s=slide()
    header(s,"01 · About us, what we run",[("Six lines of work, ",False),("one connected system",True)],
           lead="Audits create data · data supports policy · policy guides the field. Everything below is live today.",
           sect=(1,"ABOUT US"))
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
    frmi(s,4)
    return s

# ---------------------------------------------------------------- 05 OPEN DATA
def opendata():
    s=slide()
    header(s,"01 · About us, open public data",
           [("Live public data platforms, ",False),("free for any authority",True)],
           lead="Each platform turns a scattered public record into structured, citable evidence. Both screenshots are live captures.",
           sect=(1,"ABOUT US"))
    photo(s,ar("defect_live.png"),ML,I(2.12),I(6.0),I(2.62),fill=True,anchor=0.0,
          caption="Road-Infrastructure Defect Repository, live 3 Aug 2026: 502 locations, 618 public incidents, 102 deaths and 302 injuries on record.")
    photo(s,a5("parliament_live.png"),I(6.72),I(2.12),I(6.0),I(2.62),fill=True,anchor=0.0,
          caption="Road Safety in Parliament: all 1,444 questions since 2014 across four ministries, refreshed continuously.")
    panels=[("scale","Supreme Court Litigation Tracker","WEEKLY · LIVE",BR_T,"#4A35FF",
             "Every systemic road-safety matter before the Supreme Court, orders indexed, precedent judgments digested, refreshed every Tuesday.",
             "strip_sctracker.png"),
            ("bar-chart-3","Crash Data Dashboard","ANNUAL · OPEN DATA",AM_T,"#E58900",
             "MoRTH's annual 'Road Accidents in India' books as a usable product: report cards for 36 states and 50 cities, open licence (CC-BY).",
             "strip_crash.png")]
    y=I(5.42); pw=I(6.0); phh=I(1.42)
    for j,(ic,t,tag,tint,col,d,strip) in enumerate(panels):
        x=ML+j*I(6.1)
        rect(s,x,y,pw,phh,fill=PAPER,line=LINE,rounded=True,radius=0.08)
        icon_disc(s,ic,x+I(0.16),y+I(0.16),I(0.4),tint,col)
        text(s,x+I(0.68),y+I(0.13),I(3.6),I(0.3),t,font=HEAD,size=10,bold=True,color=INK,ls=1.0)
        chip(s,x+pw-I(1.62),y+I(0.15),I(1.48),I(0.32),tag,fill=tint,color={"#4A35FF":BRAND,"#E58900":AMBER}[col],size=7)
        text(s,x+I(0.16),y+I(0.62),I(3.55),I(0.72),d,size=8,color=MUT,ls=1.16)
        s.shapes.add_picture(a6(strip),x+I(3.82),y+I(0.62),width=I(2.02))
    frmi(s,5)
    return s

# ---------------------------------------------------------------- 06 GOVT FOOTPRINT
def footprint():
    s=slide()
    header(s,"02 · Where we work with government",
           [("Working relationships across ",False),("the road safety machinery",True)],
           lead="Roads Management Insights serves road authorities. We work with many of them every week, with formal seats and signed mandates.",
           sect=(2,"GOVERNMENT"))
    rows=[("landmark","Four District Road Safety Committees","Formal member in Gurugram, South-West Delhi, North-West Delhi and Jaipur, the statutory bodies that decide local road-safety action.",BR_T,"#4A35FF"),
          ("shield","Police partnerships","MoUs with Jaipur Traffic Police and Gurugram Police; SATARK runs with police in three cities; challan and crash (e-DAR) data flow through these relationships.",GR_T,"#0A9955"),
          ("badge-check","Written authority approvals","25+ approvals in writing from road-owning authorities across six states: PWDs of Kerala, UP and Punjab, CPWD, R&B Andhra, GCC Chennai, ADDA Durgapur, Indore.",AM_T,"#E58900"),
          ("scale","National institutions","Expressions of Interest submitted to National Road Safety Board Working Groups 2 and 5; Rajasthan's compensation scheme mapped office-by-office with the Transport Department.",TE_T,"#0E8A8A")]
    y=I(2.25)
    for j,(ic,t,d,tint,col) in enumerate(rows):
        irow(s,ML,y+j*I(0.98),I(7.6),ic,t,d,tint,col)
    photo(s,a6("ph_auth_roundtable.jpeg"),I(8.6),I(2.25),I(4.1),I(2.4),fill=True,anchor=0.3,
          caption="Presenting audit findings to the engineers who own the road.")
    text(s,I(8.6),I(5.25),I(4.1),I(0.26),"AUTHORITIES WE WORK WITH",font=HEAD,size=8,bold=True,color=MUT,tracking=1.5)
    logos=["lg_nhai.png","lg_pwd.png","lg_haryana_police.png","lg_indore_nn.png","lg_dlsa.png","lg_kolkata_police.png"]
    for j,f in enumerate(logos):
        c=j%3; r=j//3
        logo_chip(s,a6(f),I(8.6)+c*I(1.42),I(5.56)+r*I(0.72),I(1.3),I(0.62))
    frmi(s,6)
    return s

# ---------------------------------------------------------------- 07 WHY SPEED
def whyspeed():
    s=slide()
    header(s,"03 · Why speed data matters",
           [("Speed decides ",False),("what a crash becomes",True)],
           lead="The case for measuring speed is written in the official record. Managed speeds are the single most direct lever on survival.",
           sect=(3,"SPEED & RMI"))
    tiles=[("72.4%","of crashes on India's National Highways are attributed to speed (72.5% of the deaths)","MoRTH, Road Accidents in India 2023"),
           ("10% → 90%","a pedestrian's fatality risk as impact speed rises from 30 to 70 km/h","Austroads, 2015"),
           ("3–4%","fewer fatal crashes for every 1 km/h reduction in mean traffic speed","World Bank, Guide for Safe Speeds 2024")]
    tw=I(3.95)
    for j,(v,l,src) in enumerate(tiles):
        x=ML+j*(tw+I(0.12)); y=I(2.35)
        rect(s,x,y,tw,I(1.72),fill=MIST,rounded=True,radius=0.08)
        text(s,x+I(0.18),y+I(0.12),tw-I(0.36),I(0.5),v,font=HEAD,size=22,bold=True,color=BRAND)
        text(s,x+I(0.18),y+I(0.68),tw-I(0.36),I(0.62),l,size=9,color=INK,ls=1.2)
        text(s,x+I(0.18),y+I(1.4),tw-I(0.36),I(0.26),src,size=7.5,color=MUT,ls=1.0,italic=True)
    rect(s,ML,I(4.45),CW,I(1.55),fill=BR_T,rounded=True,radius=0.10)
    icon_disc(s,"map-pin",ML+I(0.22),I(4.68),I(0.44),PAPER,"#4A35FF")
    text(s,ML+I(0.85),I(4.65),I(11),I(0.3),"And in the crash records we work with every week",font=HEAD,size=11,bold=True,color=BRAND)
    text(s,ML+I(0.85),I(5.0),I(11),I(0.85),
         "In the 361 GPS-located crashes at Jaipur's notified blackspots (2022–24, police e-DAR records via our District Road Safety Committee seat), high speed is the single most recorded violation. The worst cluster alone, on the Jaipur–Kishangarh Expressway near Bhankrota, carries 23 deaths from 13 crashes within about 150 metres.",
         size=10.5,color=INK,ls=1.35)
    text(s,ML,I(6.3),CW,I(0.4),"What no one measures today is the speed itself: continuously, corridor by corridor, hour by hour. That is the layer Roads Management Insights carries.",size=10.5,color=MUT,ls=1.3)
    frmi(s,7)
    return s

# ---------------------------------------------------------------- 08 RMI UNDERSTANDING
def rmi_read():
    s=slide()
    header(s,"03 · Our read of RMI",
           [("What we understand RMI provides, ",False),("and what we would like to learn",True)],
           lead="Written after hands-on setup on Google Cloud. Please correct us wherever our understanding is incomplete.",
           sect=(3,"SPEED & RMI"))
    rect(s,ML,I(2.3),I(6.0),I(3.9),fill=PAPER,line=LINE,rounded=True,radius=0.08)
    text(s,ML+I(0.25),I(2.5),I(5.5),I(0.26),"OUR CURRENT UNDERSTANDING",font=HEAD,size=9,bold=True,color=BRAND,tracking=1.5)
    und=[("Historical travel times & speeds","per subscribed corridor, accumulated hourly into BigQuery from subscription day onward"),
         ("Near-real-time speeds","segment-level readings refreshed roughly every two minutes, streamed via Pub/Sub"),
         ("Congestion vs free-flow","actual against baseline travel time, showing where and when a road degrades"),
         ("Anomaly events","sudden slowdown flags, the typical signature of a crash or closure, in near real time")]
    y=I(2.9)
    for t,d in und:
        circle(s,ML+I(0.28),y+I(0.05),I(0.14),BRAND)
        text(s,ML+I(0.56),y-I(0.02),I(5.3),I(0.3),t,font=HEAD,size=10.5,bold=True,color=INK,ls=1.0)
        text(s,ML+I(0.56),y+I(0.26),I(5.3),I(0.5),d,size=9,color=MUT,ls=1.2)
        y=y+I(0.82)
    x2=I(6.85)
    rect(s,x2,I(2.3),I(5.85),I(3.9),fill=BRAND,rounded=True,radius=0.08)
    text(s,x2+I(0.25),I(2.5),I(5.35),I(0.26),"WHAT WE WOULD LIKE TO LEARN FROM YOU",font=HEAD,size=9,bold=True,color=LAVW,tracking=1.5)
    qs=["Does RMI, or its roadmap, include crash-risk or hotspot layers, like the accident-prone-area alerts consumer Maps ships in India?",
        "What segment granularity and coverage should we expect on smaller urban streets, for example the roads outside schools?",
        "Can the speed-limit layer behind the India rollout be joined to RMI speeds for compliance analysis?",
        "How do NGO and authority partnerships access RMI in practice: scope, terms, and the role Lepton plays?"]
    y=I(2.92)
    for q in qs:
        text(s,x2+I(0.25),y,I(5.35),I(0.65),q,size=9.5,color=PAPER,ls=1.25)
        y=y+I(0.82)
    text(s,ML,I(6.45),CW,I(0.35),
         "As we understand it, RMI works at the level of traffic streams: no number plates and no individual vehicles. Police crash records are ours to bring.",
         size=9.5,color=MUT,ls=1.2,italic=True)
    frmi(s,8)
    return s

# ---------------------------------------------------------------- 09 P1 DEFECT REPO
def p1_defect():
    s=slide()
    header(s,"04 · Product 1, the Defect Repository",
           [("A national defect map, ",False),("built jointly",True)],
           lead="Live today, built by us, open to all. With government blackspot data and the RMI speed layer, it becomes a national road-risk product.",
           sect=(4,"THE PRODUCTS"))
    photo(s,ar("defect_live.png"),ML,I(2.15),I(6.1),I(2.75),fill=True,anchor=0.0,
          caption="Live, 3 Aug 2026: 502 locations, 618 public incidents, 102 deaths, 302 injuries on record; filters by state, district, road type, defect and priority.")
    sts=[("146","districts scanned daily"),("13","languages read"),("21","defect codes"),("Daily","07:00 IST auto-run")]
    for j,(v,l) in enumerate(sts):
        x=ML+j*I(1.56)
        rect(s,x,I(5.62),I(1.44),I(0.62),fill=TE_T,rounded=True,radius=0.12)
        text(s,x+I(0.1),I(5.68),I(1.24),I(0.26),v,font=HEAD,size=11,bold=True,color=TEAL,ls=1.0)
        text(s,x+I(0.1),I(5.94),I(1.24),I(0.26),l,size=6.5,color=MUT,ls=1.0)
    x3=I(7.05)
    rows=[("layers","What we bring","The live news-mined repository, human-reviewed with source evidence, plus government blackspot data we already hold: MoRTH's 13,795 notified black spots, and Jaipur's 96 police-mapped crash clusters.",BR_T,"#4A35FF"),
          ("gauge","What RMI adds","The measured speed and anomaly layer on defect corridors, so every reported defect carries real exposure alongside the report.",TE_T,"#0E8A8A"),
          ("git-compare","What it becomes","One public map where defects, crashes and speeds meet: a joint evidence product for authorities, published with attribution on every chart.",GR_T,"#0A9955")]
    y=I(2.15)
    for ic,t,d,tint,col in rows:
        icon_disc(s,ic,x3,y,I(0.42),tint,col)
        text(s,x3+I(0.58),y-I(0.03),I(5.0),I(0.32),t,font=HEAD,size=11,bold=True,color=INK)
        text(s,x3+I(0.58),y+I(0.3),I(5.0),I(1.0),d,size=9.5,color=MUT,ls=1.25)
        y=y+I(1.42)
    frmi(s,9)
    return s

# ---------------------------------------------------------------- 10 P2 SCHOOL SAFETY INDEX
def p2_ssi():
    s=slide()
    header(s,"04 · Product 2, the School Safety Index",
           [("School-zone safety, graded in public, ",False),("school by school",True)],
           lead="Running today on Google's own imagery and APIs. RMI would add the one input a photograph cannot give: the speed past the gate.",
           sect=(4,"THE PRODUCTS"))
    photo_fit(s,ar("slide_ssi_index.png"),ML,I(2.15),I(3.05),I(2.5),caption="The public index, worst grades first.")
    photo_fit(s,ar("slide_ssi_school.png"),I(3.85),I(2.15),I(3.05),I(2.5),caption="A school's report card, with pinned\nStreet View evidence.")
    text(s,ML,I(5.25),I(6.3),I(0.26),"HOW IT WORKS TODAY",font=HEAD,size=8.5,bold=True,color=MUT,tracking=1.5)
    steps=[("map-pin","3,814 Delhi NCR schools sourced via the Places API"),
           ("camera","Street View coverage checked; 90% of schools have imagery"),
           ("search-check","AI desk audit against an IRC SP:32 rubric, adversarially verified"),
           ("users","Student teams field-verify the worst-graded zones")]
    y=I(5.6)
    for j,(ic,t) in enumerate(steps):
        c=j%2; r=j//2
        x=ML+c*I(3.2)
        icon_disc(s,ic,x,y+r*I(0.56),I(0.36),BR_T,"#4A35FF")
        text(s,x+I(0.48),y+r*I(0.56)+I(0.03),I(2.7),I(0.45),t,size=8,color=INK,ls=1.1)
    x3=I(7.15)
    rect(s,x3,I(2.15),I(5.55),I(1.9),fill=BR_T,rounded=True,radius=0.08)
    text(s,x3+I(0.22),I(2.32),I(5.1),I(0.26),"WHERE RMI FITS",font=HEAD,size=9,bold=True,color=BRAND,tracking=1.4)
    text(s,x3+I(0.22),I(2.64),I(5.1),I(1.3),
         "Imagery shows the missing crossing and the absent speed hump. RMI would add a speed-exposure score per school zone: the share of school-run hours with traffic above safe speed at the gate. Together they rank every school by measured danger, and prove the change after a district builds the fix.",
         size=9.5,color=INK,ls=1.3)
    rect(s,x3,I(4.25),I(5.55),I(1.95),fill=PAPER,line=LINE,rounded=True,radius=0.08)
    text(s,x3+I(0.22),I(4.42),I(5.1),I(0.26),"READY IN JAIPUR",font=HEAD,size=9,bold=True,color=GREEN,tracking=1.4)
    jrows=[("1,572","Jaipur schools already mapped for the next city build"),
           ("361","GPS-located crashes at notified blackspots inform corridor choice"),
           ("4 DRSCs","our committee seats carry the findings into the statutory forum")]
    yj=I(4.76)
    for v,l in jrows:
        text(s,x3+I(0.22),yj,I(1.1),I(0.3),v,font=HEAD,size=12,bold=True,color=GREEN,ls=1.0)
        text(s,x3+I(1.4),yj+I(0.02),I(3.95),I(0.4),l,size=8.5,color=MUT,ls=1.12)
        yj=yj+I(0.46)
    frmi(s,10)
    return s

# ---------------------------------------------------------------- 11 P3 ENFORCEMENT (EXPLORATORY)
def p3_compass():
    s=slide()
    header(s,"04 · Product 3, an exploratory direction",
           [("Enforcement support, ",False),("shaped together if useful",True)],
           lead="An early idea, listed for completeness. It builds only on assets we already run with police partners, and carries no commitments.",
           sect=(4,"THE PRODUCTS"))
    chip(s,ML,I(2.1),I(2.9),I(0.4),"EXPLORATORY · TO SHAPE TOGETHER",fill=AM_T,color=AMBER,size=8.5)
    rows=[("shield","What already runs","SATARK screens vehicles for police in Jaipur, Bengaluru and Gurugram, 3,00,000+ screened; challan billboards operate in public view; MoUs govern the data.",GR_T,"#0A9955"),
          ("gauge","What RMI could add","A weekly view of where and when speeding concentrates near people, so patrols, camera vans and SATARK sites stand where the risk is, corridor-hour by corridor-hour.",BR_T,"#4A35FF"),
          ("badge-check","How we would keep it honest","Success measured as speeds before and after a deployment, never as challan counts; no vehicle identification anywhere in the loop; a small pilot before any scale.",TE_T,"#0E8A8A")]
    y=I(2.75)
    for j,(ic,t,d,tint,col) in enumerate(rows):
        irow(s,ML,y+j*I(1.06),I(7.6),ic,t,d,tint,col)
    photo(s,a5("satark_billboard.jpg"),I(8.6),I(2.75),I(4.1),I(2.6),fill=True,anchor=0.42,
          caption="A SATARK challan billboard, live with Jaipur Traffic Police.")
    rect(s,ML,I(6.15),I(7.6),I(0.6),fill=MIST,rounded=True,radius=0.14)
    text(s,ML+I(0.2),I(6.25),I(7.2),I(0.42),
         [("Everything named here is ours or the police's. ",{'bold':True}),("No third party is required for a first version.",{'color':MUT})],size=9.5,ls=1.2)
    frmi(s,11)
    return s

# ---------------------------------------------------------------- 12 READY PILOT
def pilot():
    s=slide()
    header(s,"05 · A pilot that is ready",
           [("Configured, scripted, ",False),("and waiting on one enablement",True)],
           lead="We prepared the ground before asking for the conversation. Everything on our side of a pilot is already done.",
           sect=(5,"THE PILOT"))
    rows=[("cpu","Cloud project configured","Roads API, BigQuery, Analytics Hub and Pub/Sub enabled on our Google Cloud project, verified end to end from Cloud Shell.",BR_T,"#4A35FF"),
          ("route","Seven route subscriptions scripted","Five Jaipur blackspot corridors chosen from police crash records (162 deaths combined, 2022–24) and two school-zone test segments, ready to fire.",GR_T,"#0A9955"),
          ("landmark","A lawful channel for action","Our Jaipur District Road Safety Committee seat carries every finding into the statutory forum that can act on it.",AM_T,"#E58900"),
          ("users","Ground truth on call","Student audit teams verify in the field what the data flags, closing the loop between measurement and reality.",TE_T,"#0E8A8A")]
    y=I(2.25)
    for j,(ic,t,d,tint,col) in enumerate(rows):
        irow(s,ML,y+j*I(0.98),I(7.3),ic,t,d,tint,col)
    x2=I(8.2)
    rect(s,x2,I(2.25),I(4.5),I(2.3),fill=BRAND,rounded=True,radius=0.08)
    text(s,x2+I(0.25),I(2.45),I(4.0),I(0.26),"THE PILOT WE PROPOSE",font=HEAD,size=9,bold=True,color=LAVW,tracking=1.4)
    text(s,x2+I(0.25),I(2.8),I(4.0),I(1.6),
         "Roads Management Insights enabled on our configured project for a 90-day Jaipur pilot: five corridors and fifty school zones. We can be receiving data into BigQuery the same day, and present the first speed-beside-crash evidence at the next District Road Safety Committee meeting.",
         size=10,color=PAPER,ls=1.32)
    rect(s,x2,I(4.75),I(4.5),I(1.9),fill=PAPER,line=LINE,rounded=True,radius=0.08)
    text(s,x2+I(0.25),I(4.92),I(4.0),I(0.26),"A PRECEDENT WE ADMIRE",font=HEAD,size=9,bold=True,color=MUT,tracking=1.4)
    text(s,x2+I(0.25),I(5.24),I(4.05),I(1.3),
         "Google.org funds iRAP's Star Rating for Schools programme in Vietnam. India has no lead partner for school-zone safety yet. Every output of this pilot is published openly, with Google Maps Platform attribution on each chart.",
         size=9.5,color=INK,ls=1.28)
    frmi(s,12)
    return s

# ---------------------------------------------------------------- 13 FOR THE CALL
def forcall():
    s=slide()
    header(s,"05 · For this call",
           [("What we would like to figure out ",False),("together",True)],
           lead="Four questions, held loosely. The ranking of products is ours to lose; the starting point is yours to shape.",
           sect=(5,"THE PILOT"))
    cards=[("message-square","Correct our read of RMI","Where is our understanding of the data wrong or incomplete? What exists that we have not seen: risk layers, hotspot analytics, the speed-limit layer?"),
           ("target","Choose the starting product","Which direction is most interesting from your side, for India and for RMI's own story: the Defect Repository, the School Safety Index, or something we have not thought of?"),
           ("handshake","What makes this valuable for your team","Ground-truth data, a documented public-impact deployment, a partner already inside district machinery: tell us which of these matters most to you."),
           ("rocket","The practical next step","A technical working session with the Lepton and Maps teams, looking at real data together. Our cloud project and corridor definitions are ready whenever useful.")]
    tw=I(5.98); th=I(1.9)
    for j,(ic,t,d) in enumerate(cards):
        r,c=divmod(j,2)
        x=ML+c*(tw+I(0.13)); y=I(2.3)+r*(th+I(0.16))
        rect(s,x,y,tw,th,fill=MIST if j%3==0 else PAPER,line=None if j%3==0 else LINE,rounded=True,radius=0.08)
        icon_disc(s,ic,x+I(0.2),y+I(0.2),I(0.46),BR_T,"#4A35FF")
        text(s,x+I(0.82),y+I(0.26),tw-I(1.0),I(0.32),t,font=HEAD,size=12,bold=True,color=INK,ls=1.0)
        text(s,x+I(0.2),y+I(0.72),tw-I(0.4),I(1.05),d,size=9.5,color=MUT,ls=1.28)
    frmi(s,13)
    return s

# ---------------------------------------------------------------- 14 CLOSE
def close():
    s=slide(bg=BRAND)
    s.shapes.add_picture(LOGO_WHITE,ML,I(0.62),width=I(2.0))
    text(s,ML,I(2.2),I(12.1),I(0.85),"Your maps see every road in India.",font=HEAD,size=32,bold=True,color=PAPER,ls=1.15)
    text(s,ML,I(3.05),I(12.1),I(0.85),"We would like to put them to work\nfor the people on those roads.",font=HEAD,size=22,bold=True,color=LAVW,ls=1.2)
    text(s,ML,I(4.55),I(10.5),I(0.5),"We look forward to the conversation.",size=12,color=PAPER,ls=1.3)
    hline(s,ML,I(5.3),I(5.2),color=RGBColor(0x6A,0x55,0xFF),wt=1.0)
    cols=[("Akhtar Hussain","Mission Lead · akhtar@crashfreeindia.org"),
          ("Deepanshu Gupta","Trustee · deepanshu@crashfreeindia.org"),
          ("Gajendra Jangid","Trustee · gajendra@crashfreeindia.org")]
    x=ML
    for nm,role in cols:
        text(s,x,I(5.6),I(3.9),I(0.3),nm,font=HEAD,size=12,bold=True,color=PAPER)
        text(s,x,I(5.92),I(3.9),I(0.3),role,size=9.5,color=LAVW,ls=1.1)
        x=x+I(4.06)
    text(s,ML,I(7.0),I(12),I(0.3),"Crashfree India · A Cars24 commitment · Operated by Vision Zero Trust, New Delhi · crashfreeindia.org",size=9.5,color=LAVW)
    return s

if __name__=="__main__":
    new_deck()
    cover()
    agenda()
    about()
    portfolio()
    opendata()
    footprint()
    whyspeed()
    rmi_read()
    p1_defect()
    p2_ssi()
    p3_compass()
    pilot()
    forcall()
    close()
    save(os.path.join(BUILD,"CFI_RMI_PreRead_v3.pptx"))

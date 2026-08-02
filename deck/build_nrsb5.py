# NRSB EoI decks v3, implements the 15-point review: bold cover w/ Dhoni, approach + WG-fit slides,
# one-pager platform cards, partner/press logo walls, pendency slide, primer slide, team/SME slides,
# live implementation-sheet numbers, Dhoni quote close.
import os
from nrsb2_style import *
from pptx.util import Inches, Pt, Emu
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

I=Inches
LTR=os.path.join(V3,"letters")
V6=os.path.join(SP,"assets/v6/ready")
H2=os.path.join(V6,"heads2")
def a6(n): return os.path.join(V6,n)

# ---------------------------------------------------------------- S1 COVER
def cover(wg,name,chips_,idx,total,icons=("cpu","file-search","handshake")):
    s=slide()
    s.shapes.add_picture(LOGO_BLUE,ML,I(0.5),width=I(1.85))
    text(s,SW-MR-I(3.5),I(0.55),I(3.5),I(0.3),"AUGUST 2026  ·  NEW DELHI",font=HEAD,size=9,bold=True,color=MUT,tracking=1.8,align=PP_ALIGN.RIGHT)
    text(s,ML,I(1.72),I(8.2),I(0.3),"EXPRESSION OF INTEREST  ·  NATIONAL ROAD SAFETY BOARD",font=HEAD,size=10.5,bold=True,color=BRAND,tracking=2.2)
    text(s,ML,I(2.14),I(8.3),I(0.85),"Crashfree India",font=HEAD,size=46,bold=True,color=INK,ls=1.0)
    text(s,ML,I(3.1),I(8.3),I(0.85),f"Application to Working Group {wg}:\n{name}",font=HEAD,size=16.5,bold=True,color=BRAND,ls=1.25)
    y=I(4.65)
    for i,t in enumerate(chips_):
        icon_disc(s,icons[i%3],ML,y+i*I(0.62),I(0.4),BR_T,"#4A35FF")
        text(s,ML+I(0.56),y+i*I(0.62)+I(0.05),I(7.9),I(0.4),t,font=HEAD,size=11.5,bold=True,color=INK,ls=1.1)
    text(s,ML,I(6.9),I(8.6),I(0.3),f"Submitted to the Chairperson and Members, Working Group {wg}, National Road Safety Board",size=9.5,color=MUT)
    text(s,SW-MR-I(2.6),I(6.9),I(2.6),I(0.3),"crashfreeindia.org",font=HEAD,size=9.5,bold=True,color=BRAND,align=PP_ALIGN.RIGHT)
    px,pyy,pw,ph_=I(9.1),I(1.15),I(3.6),I(4.9)
    photo(s,a5("ph_dhoni_white.jpg"),px,pyy,pw,ph_,fill=True,anchor=0.12)
    rect(s,px,pyy+ph_-I(0.56),pw,I(0.56),fill=BRAND)
    text(s,px,pyy+ph_-I(0.52),pw,I(0.5),"MS DHONI · GOODWILL AMBASSADOR,\nCRASHFREE INDIA",font=HEAD,size=8.5,bold=True,color=PAPER,align=PP_ALIGN.CENTER,ls=1.15,tracking=1.0)
    return s

CIRC=os.path.join(SP,"assets/v7/circ")
def circp(s,name,x,y,d):
    return s.shapes.add_picture(os.path.join(CIRC,name),x,y,width=d,height=d)

# ---------------------------------------------------------------- S2 LETTER
def letter(wg,p3,idx,total):
    s=slide()
    text(s,ML,I(0.30),I(8),I(0.24),"BEFORE THE SLIDES",font=HEAD,size=9,bold=True,color=BRAND,tracking=2.2)
    hline(s,ML,I(0.62),I(0.55),color=BRAND,wt=2.0)
    text(s,ML,I(0.76),I(12),I(0.5),[("A letter to the ",{'color':INK}),("Working Group",{'color':BRAND})],font=HEAD,size=22.5,bold=True,ls=1.1)
    x=ML+I(0.95); w=I(10.2); y=I(1.5)
    rect(s,x,y,w,I(5.42),fill=PAPER,line=LINE,lw=1.2)
    rect(s,x,y,w,I(0.06),fill=BRAND)
    s.shapes.add_picture(LOGO_BLUE,x+I(0.5),y+I(0.32),width=I(1.35))
    text(s,x+w-I(3.2),y+I(0.36),I(2.7),I(0.3),"New Delhi · August 2026",size=9.5,color=MUT,align=PP_ALIGN.RIGHT)
    body=(f"Respected Chairperson and Members of Working Group {wg},\n"
      "Crashfree India is a young road safety nonprofit, registered as the Vision Zero Trust, co-founded with the Indian Road Safety Council, and backed by a three-year, US$3 million commitment from Cars24. We work alongside public authorities: our student teams audit dangerous locations under senior experts, our technology helps police and administrators see their own pipelines, and our support tools stand with families after a crash. MS Dhoni carries this message to the country as our Goodwill Ambassador.\n"
      +p3+"\n"
      "The pages that follow introduce the organisation briefly, then set out the work most relevant to this Working Group in the detail its mandate deserves. Everything shown is running today, is public, and is offered to the Board without cost. We would be honoured to contribute.")
    tb=text(s,x+I(0.5),y+I(0.95),w-I(1.0),I(3.6),body,size=10.6,color=INK,ls=1.3)
    for p in tb.text_frame.paragraphs: p.space_after=Pt(7)
    text(s,x+I(0.5),y+I(4.62),w-I(1.0),I(0.3),"Respectfully,",size=10.6,color=INK)
    text(s,x+I(0.5),y+I(4.92),w-I(1.0),I(0.3),"Akhtar Hussain",font=HEAD,size=11.5,bold=True,color=INK)
    text(s,x+I(0.5),y+I(5.16),w-I(1.0),I(0.26),"Mission Lead, Crashfree India  ·  akhtar@crashfreeindia.org  ·  crashfreeindia.org",size=9.5,color=MUT)
    return s

# ---------------------------------------------------------------- S3 AGENDA
def agenda(wg,sect4,r4,r5,idx,total):
    s=slide()
    text(s,ML,I(0.30),I(8),I(0.24),"HOW THIS DECK IS ORGANISED",font=HEAD,size=9,bold=True,color=BRAND,tracking=2.2)
    hline(s,ML,I(0.62),I(0.55),color=BRAND,wt=2.0)
    text(s,ML,I(0.76),I(12),I(0.5),[("Five sections, ",{'color':INK}),("three minutes",{'color':BRAND}),(" to skim",{'color':INK})],font=HEAD,size=22.5,bold=True,ls=1.1)
    rows=[("building-2","About us, and how we work","Who we are, our approach to the road crash crisis, and why this Working Group.","04 – 06"),
          ("layers","What we have built","Every public-facing programme, audits, enforcement tech, victim support, open data, youth, campaigns.","07 – 14"),
          ("users","Our people","The team, its capabilities, and the expert bench around the work.","15 – 16"),
          ("target",sect4,"The deep dive matched to this Working Group's mandate, evidence, method, results.",r4),
          ("handshake","How we can contribute","Four concrete, no-cost offers to the Working Group.",r5)]
    y=I(1.72)
    for i,(ic,t,d,pg) in enumerate(rows):
        yy=y+i*I(1.02)
        rect(s,ML,yy,CW,I(0.88),fill=MIST if i%2==0 else PAPER,line=LINE if i%2 else None,rounded=True,radius=0.10)
        num_disc(s,ML+I(0.22),yy+I(0.2),I(0.48),i+1)
        icon_disc(s,ic,ML+I(0.95),yy+I(0.2),I(0.48),BR_T,"#4A35FF")
        text(s,ML+I(1.68),yy+I(0.13),I(4.4),I(0.4),t,font=HEAD,size=13,bold=True,color=INK,ls=1.0)
        text(s,ML+I(1.68),yy+I(0.46),I(8.2),I(0.35),d,size=10,color=MUT,ls=1.15)
        text(s,SW-MR-I(1.75),yy+I(0.24),I(1.5),I(0.4),pg,font=HEAD,size=12,bold=True,color=BRAND,align=PP_ALIGN.RIGHT)
    return s

# ---------------------------------------------------------------- S4 ABOUT
def about(idx,total,wg):
    s=slide()
    header(s,"01 · About us",[("Crashfree India: a nonprofit that adds ",False),("capacity",True),(" to road safety work",False)],
           lead="Registered as the Vision Zero Trust · Co-founded by Cars24 and the Indian Road Safety Council · Working since June 2025 · New Delhi",
           sect=(1,"ABOUT US"))
    rows=[("search-check","Evidence first","Structured field audits, file reviews and research to official standards, not opinion.",GR_T,"#0A9955"),
          ("landmark","Institutional collaboration","We work through PWDs, NHAI, transport departments, police and District Road Safety Committees.",BR_T,"#4A35FF"),
          ("users","Youth-led capacity","Trained student teams from IITs, NITs and SPAs add the auditing hands the system needs.",AM_T,"#E58900"),
          ("monitor-check","Technology for follow-through","Public dashboards track every recommendation from submission to completion.",TE_T,"#0E8A8A")]
    y=I(2.2)
    for i,(ic,t,d,tint,col) in enumerate(rows):
        irow(s,ML,y+i*I(0.82),I(7.6),ic,t,d,tint,col)
    rect(s,ML,I(5.65),I(7.55),I(0.92),fill=BR_T,rounded=True,radius=0.16)
    text(s,ML+I(0.25),I(5.72),I(7.1),I(0.8),
         [("Backed by a US$3 million, three-year commitment from Cars24 ",{'bold':True,'color':BRAND}),
          (". Programmes, not overheads, receive 71% of the budget.",{'color':BRAND})],size=11.5,ls=1.3)
    photo(s,a5("cfi_map_dots.png"),I(8.85),I(2.15),I(3.6),caption="Where we work today, 18 cities, north to south.")
    footer(s,wg,idx,total)
    return s

# ---------------------------------------------------------------- S5 APPROACH (NEW)
def approach(idx,total,wg):
    s=slide()
    header(s,"01 · About us, our approach",
           [("Our approach: work ",False),("with the system",True),(", and prove it with data",False)],
           lead="Four steps, applied to every problem we take up, from a dangerous junction to a stalled compensation claim.",
           sect=(1,"ABOUT US"))
    steps=[("search-check","1 · Evidence","Field audits, file reviews and research to official standards.","31 sites audited · 50+ stakeholder consultations",GR_T,"#0A9955"),
           ("landmark","2 · Institutional partnership","Work through the authority that owns the problem, never around it.","25+ written approvals · 4 DRSCs · MoUs with police",BR_T,"#4A35FF"),
           ("cpu","3 · Technology","Dashboards, AI and WhatsApp tools that fit how officials already work.","6 live public products",TE_T,"#0E8A8A"),
           ("route","4 · Follow-through","Every recommendation tracked publicly to completion.","7 sites fully implemented · 6 more partially",AM_T,"#E58900")]
    tw=I(2.92); gx=I(0.13)
    for j,(ic,t,d,m,tint,col) in enumerate(steps):
        x=ML+j*(tw+gx); y=I(2.25)
        rect(s,x,y,tw,I(3.15),fill=PAPER,line=LINE,rounded=True,radius=0.08)
        icon_disc(s,ic,x+I(0.2),y+I(0.22),I(0.52),tint,col)
        text(s,x+I(0.2),y+I(0.92),tw-I(0.4),I(0.35),t,font=HEAD,size=12.5,bold=True,color=INK)
        text(s,x+I(0.2),y+I(1.32),tw-I(0.4),I(1.0),d,size=9.5,color=MUT,ls=1.28)
        hline(s,x+I(0.2),y+I(2.42),tw-I(0.4))
        text(s,x+I(0.2),y+I(2.52),tw-I(0.4),I(0.55),m,font=HEAD,size=8.5,bold=True,color=col if isinstance(col,RGBColor) else INK,ls=1.25)
        tcol={'#0A9955':GREEN,'#4A35FF':BRAND,'#0E8A8A':TEAL,'#E58900':AMBER}[col]
        text(s,x+I(0.2),y+I(2.52),tw-I(0.4),I(0.55),m,font=HEAD,size=8.5,bold=True,color=tcol,ls=1.25)
        if j<3: text(s,x+tw-I(0.03),y+I(1.35),I(0.22),I(0.4),"→",size=15,color=MUT)
    rect(s,ML,I(5.75),CW,I(0.7),fill=MIST,rounded=True,radius=0.14)
    text(s,ML+I(0.25),I(5.86),CW-I(0.5),I(0.5),
         [("We do not replace the system and we do not campaign against it. ",{'bold':True}),
          ("We add hands, evidence and tools to work the system has already committed to.",{'color':MUT})],size=11,ls=1.3)
    footer(s,wg,idx,total)
    return s

# ---------------------------------------------------------------- S6 WHY THIS WG (NEW)
def why_fit(wg,idx,total,focus,bring,smes,photo_card=None):
    s=slide()
    header(s,f"01 · Why Working Group {wg}",
           [(f"Why Working Group {wg}, ",False),("and what we bring to it",True)],
           lead="The Group's mandate matches the deepest part of our portfolio. Three focus areas where we are ready on day one.",
           sect=(1,"ABOUT US"))
    y=I(2.2)
    for j,(ic,t,d,tint,col) in enumerate(focus):
        irow(s,ML,y+j*I(0.98),I(7.3),ic,t,d,tint,col)
    text(s,I(8.15),I(2.1),I(4.4),I(0.26),"EXISTING CAPABILITIES WE PUT ON THE TABLE",font=HEAD,size=8.5,bold=True,color=MUT,tracking=1.4)
    for j,b in enumerate(bring):
        chip(s,I(8.15)+ (j%2)*I(2.32),I(2.42)+(j//2)*I(0.52),I(2.24),I(0.44),b,fill=BR_T,color=BRAND,size=8.5)
    text(s,ML,I(5.15),I(12),I(0.26),"SUBJECT-MATTER EXPERTS ALREADY ENGAGED ON THIS AGENDA",font=HEAD,size=8.5,bold=True,color=MUT,tracking=1.4)
    n=len(smes); cw_=(CW-I(0.09)*(n-1))/n
    x=ML
    for nm,role,img,isphoto in smes:
        rect(s,x,I(5.45),cw_,I(1.2),fill=MIST,rounded=True,radius=0.10)
        if isphoto:
            circp(s,img,x+I(0.12),I(5.62),I(0.85))
        else:
            circle(s,x+I(0.12),I(5.62),I(0.85),BR_T)
            text(s,x+I(0.12),I(5.6),I(0.85),I(0.9),img,font=HEAD,size=14,bold=True,color=BRAND,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        text(s,x+I(1.06),I(5.56),cw_-I(1.15),I(0.4),nm,font=HEAD,size=9,bold=True,color=INK,ls=1.05)
        text(s,x+I(1.06),I(5.95),cw_-I(1.15),I(0.66),role,size=7.5,color=MUT,ls=1.15)
        x=x+cw_+I(0.09)
    footer(s,wg,idx,total)
    return s

# ---------------------------------------------------------------- S7 PORTFOLIO
def portfolio(idx,total,wg):
    s=slide()
    header(s,"02 · What we have built",[("Six lines of work, ",False),("one connected system",True)],
           lead="Audits create data · data supports policy · policy guides the field. Everything below is live today.",
           sect=(2,"WHAT WE HAVE BUILT"))
    tiles=[("Project Rakshak","Student-led road audits, fixed with authorities","31 sites · 7 fixes fully built",a5("implementation_work.jpg"),0.30),
           ("SATARK enforcement","AI support that helps police find high-risk vehicles","3,00,000+ vehicles screened",a5("satark_billboard.jpg"),0.42),
           ("Victim support","Aasha chatbot, calculator, hospital helpdesks","100+ victims helped in first 4 days",a5("ph_helpdesk_desk.jpg"),0.42),
           ("Open public data","Four self-updating data platforms, free to use","36 states & 50 cities covered",a5("sctracker.png"),0.05),
           ("Youth & policy","NextMile ideathon and national dialogue series","2,000+ participants engaged",a5("ph_ideathon_winners.jpg"),0.25),
           ("Public campaigns","Road Safety Month with police & schools; MS Dhoni","1M+ citizens reached",a5("ph_police_rally.jpg"),0.35)]
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
    footer(s,wg,idx,total)
    return s

# ---------------------------------------------------------------- S8 SATARK
def satark(idx,total,wg):
    s=slide()
    header(s,"02 · What we have built, enforcement technology",
           [("SATARK: AI that helps police stop ",False),("the right vehicle",True)],
           lead="Built with Cars24 engineers. Reads number plates, checks government records, and alerts officers to repeat offenders, in real time.",
           sect=(2,"WHAT WE HAVE BUILT"))
    photo(s,a5("satark_billboard.jpg"),ML,I(2.15),I(4.35),I(2.65),fill=True,anchor=0.42,caption="Rambagh Circle, Jaipur, live plate, pending challans and dues on a public billboard.")
    photo_fit(s,a5("satark_officer_app.jpg"),I(5.15),I(2.15),I(2.0),I(2.65),caption="Officer view, challans,\nRC & compliance status.")
    xs=I(7.42); ws=I(2.55)
    stat(s,xs,I(2.1),ws,"3,00,000+","vehicles screened",vsize=21)
    stat(s,xs+I(2.68),I(2.1),ws,"₹30 Cr+","pending challan value identified",vsize=21)
    stat(s,xs,I(3.08),ws,"350+","high-risk vehicles intercepted",vsize=21)
    stat(s,xs+I(2.68),I(3.08),ws,"70,019","vehicles found with pending challans",vsize=21)
    chip(s,xs,I(4.12),I(2.45),I(0.42),"LIVE · Jaipur & Bengaluru",fill=GR_T,color=GREEN,size=9.5)
    chip(s,xs+I(2.58),I(4.12),I(1.75),I(0.42),"NEW · Gurugram",fill=BR_T,color=BRAND,size=9.5)
    text(s,xs,I(4.66),I(5.2),I(0.3),"Bengaluru's Trinity Circle billboard was India's first, covered by Deccan Herald and national press. Pune and Ahmedabad are next.",size=9.5,color=MUT,ls=1.25)
    steps=[("camera","ANPR camera"),("scan-line","Plate read"),("database","Records check"),("alert-triangle","Risk flag"),("bell-ring","Officer alert"),("monitor","Billboard"),("hand","Interception"),("shield-check","Enforcement")]
    y=I(5.62); n=len(steps); cw=CW/n
    hline(s,ML+I(0.4),y+I(0.24),CW-I(0.8),color=LINE,wt=1.0)
    for i,(ic,lb) in enumerate(steps):
        x=ML+Emu(int(cw*i))
        icon_disc(s,ic,x+Emu(int(cw/2))-I(0.24),y,I(0.48),MIST,"#4A35FF")
        text(s,x,y+I(0.56),Emu(int(cw)),I(0.3),lb,size=8.5,color=MUT,align=PP_ALIGN.CENTER,ls=1.0)
    footer(s,wg,idx,total)
    return s

# ---------------------------------------------------------------- S9 OPEN DATA (REDONE)
def opendata(idx,total,wg):
    s=slide()
    header(s,"02 · What we have built, open public data",
           [("Live public data platforms, ",False),("free for any authority",True)],
           lead="Four platforms, each turning a scattered public record into structured, citable evidence. The two trackers are shown live, as captured this week.",
           sect=(2,"WHAT WE HAVE BUILT"))
    photo(s,a5("parliament_live.png"),ML,I(2.12),I(6.0),I(2.62),fill=True,anchor=0.0,
          caption="Road Safety in Parliament: all 1,444 questions since 2014 across four ministries; 275 of 540 sitting Lok Sabha MPs have never asked one.")
    photo(s,a5("sctracker.png"),I(6.72),I(2.12),I(6.0),I(2.62),fill=True,anchor=0.0,
          caption="Supreme Court Litigation Tracker: 20 systemic cases, 191 orders indexed, 30 precedent judgments. Refreshes every Tuesday.")
    panels=[("database","Road-Infrastructure Defect Repository","DAILY · 07:00 IST",TE_T,"#0E8A8A",
             "An AI pipeline reads local-language news from 146 districts every morning and turns road-defect reports, potholes, missing signage, unlit stretches, into structured, mapped evidence.",
             "strip_defect.png"),
            ("bar-chart-3","Crash Data Dashboard","ANNUAL · OPEN DATA",AM_T,"#E58900",
             "MoRTH's annual 'Road Accidents in India' books as a usable product: report cards for 36 states and 50 cities, every number reconciled against the printed books, open licence (CC-BY).",
             "strip_crash.png")]
    y=I(5.42); pw=I(6.0); phh=I(1.42)
    for j,(ic,t,tag,tint,col,d,strip) in enumerate(panels):
        x=ML+j*I(6.1)
        rect(s,x,y,pw,phh,fill=PAPER,line=LINE,rounded=True,radius=0.08)
        icon_disc(s,ic,x+I(0.16),y+I(0.16),I(0.4),tint,col)
        text(s,x+I(0.68),y+I(0.13),I(3.6),I(0.3),t,font=HEAD,size=10,bold=True,color=INK,ls=1.0)
        chip(s,x+pw-I(1.62),y+I(0.15),I(1.48),I(0.32),tag,fill=tint,color={"#0E8A8A":TEAL,"#E58900":AMBER}[col],size=7)
        text(s,x+I(0.16),y+I(0.62),I(3.55),I(0.72),d,size=8,color=MUT,ls=1.16)
        s.shapes.add_picture(a6(strip),x+I(3.82),y+I(0.62),width=I(2.02))
    footer(s,wg,idx,total)
    return s

# ---------------------------------------------------------------- S10 VICTIM TOOLS (REDONE)
def victim_suite(idx,total,wg):
    s=slide()
    header(s,"02 · What we have built, victim support",
           [("Help a family can actually use, ",False),("in their language",True)],
           lead="From the first hours after a crash to the final compensation order, on WhatsApp, on paper, and in person.",
           sect=(2,"WHAT WE HAVE BUILT"))
    photo_fit(s,a6("ui_aasha_chat.png"),ML,I(2.1),I(4.5),I(3.1),caption="Aasha, live on WhatsApp, 24/7, multilingual, step-by-step guidance on rights, schemes and documents.")
    rows=[("bot","Aasha chatbot","India's first AI legal companion for crash victims, no app, no portal, just WhatsApp and voice.",BR_T,"#4A35FF"),
          ("calculator","Compensation Calculator","Free instant estimates on Supreme Court principles (Sarla Verma, Pranay Sethi).",TE_T,"#0E8A8A"),
          ("life-buoy","Hospital helpdesks","Legal desks in trauma wards, 100+ victims supported in the first four days.",GR_T,"#0A9955"),
          ("book-open","Plain-language education","Comics and Hindi guides on all three compensation routes, NALSA 15100 and the Cashless Treatment Scheme 2025.",AM_T,"#E58900")]
    y=I(5.65)
    for j,(ic,t,d,tint,col) in enumerate(rows):
        c=j%2; r=j//2
        x=ML+c*I(6.15); yy=y+r*I(0.62)
        icon_disc(s,ic,x,yy,I(0.4),tint,col)
        text(s,x+I(0.52),yy+I(0.02),I(5.5),I(0.5),[(t+", ",{'bold':True,'size':9.5}),(d,{'color':MUT,'size':8.5})],size=9,ls=1.1)
    photo_fit(s,a6("ui_mact_calc.png"),I(5.0),I(2.1),I(3.6),I(3.1),caption="The Calculator, a sample estimate\ncomputed on SC principles.")
    photo_fit(s,a6("comic_aasha_page.png"),I(8.95),I(2.1),I(2.4),I(3.1),caption="'Meet Aasha' comic, legal education\nfamilies actually read.")
    photo_fit(s,a3("guide_p1.png"),I(11.15),I(2.1),I(1.55),I(3.1),caption="Hindi legal-rights\nguide.")
    footer(s,wg,idx,total)
    return s

# ---------------------------------------------------------------- S11 YOUTH
def youth(idx,total,wg):
    s=slide()
    header(s,"02 · What we have built, youth & policy",
           [("Young talent and senior experts, ",False),("working the same problem",True)],
           lead="A steady pipeline of engineers and policy minds, so road safety work never runs out of hands.",
           sect=(2,"WHAT WE HAVE BUILT"))
    photo(s,a5("ph_ideathon_winners.jpg"),ML,I(2.12),I(4.05),I(2.5),fill=True,anchor=0.2,
          caption="NextMile: Road Safety Policy Ideathon, grand finale, 28 Sep 2025, New Delhi.")
    xs=ML; y=I(5.3)
    for i,(v,l) in enumerate([("2,000+","participants"),("250+","concept notes"),("700+","teams"),("10","finalist teams")]):
        stat(s,xs+i*I(1.05),y,I(1.0),v,l,vsize=14,lsize=8)
    photo(s,a5("ph_forum_stage2.jpg"),I(4.85),I(2.12),I(3.7),I(2.5),fill=True,anchor=0.3,
          caption="National Road Safety Implementation Forum, IIT Delhi: 60+ experts from MoRTH, WHO, UNICEF, iRAP and CSIR-CRRI reviewed the work.")
    text(s,I(4.85),I(5.28),I(3.7),I(0.8),"Mentors and jury from the Government of Rajasthan, NIUA, OMI, NASSCOM and CSEP judged the student teams; winning tracks now feed our audit and research pipeline.",size=9.5,color=MUT,ls=1.25)
    x3=I(9.0)
    rows=[("mic","National Road Safety Dialogue Series","200+ live attendees; speakers from MoRTH, CIRT, AIIMS Trauma Centre, CSIR-CRRI and ARAI.",BR_T,"#4A35FF"),
          ("message-square","Three sessions so far","Bus safety · Delivery rider safety · Good Samaritan law & the Cashless Treatment Scheme.",TE_T,"#0E8A8A"),
          ("monitor-play","Advocacy on video","Our YouTube channel documents hazards and fixes on camera: ground-audit walkthroughs, Dialogue Series recordings and victim-education explainers. A public record any authority can cite.",RD_T,"#E11900")]
    y=I(2.12)
    for i,(ic,t,d,tint,col) in enumerate(rows):
        icon_disc(s,ic,x3,y,I(0.42),tint,col)
        text(s,x3+I(0.58),y-I(0.03),I(3.15),I(0.55),t,font=HEAD,size=10.5,bold=True,color=INK,ls=1.08)
        text(s,x3+I(0.58),y+I(0.36),I(3.15),I(0.85),d,size=9,color=MUT,ls=1.2)
        y=y+I(1.28)
    rect(s,x3,I(6.0),I(3.7),I(0.72),fill=MIST,rounded=True,radius=0.14)
    text(s,x3+I(0.18),I(6.08),I(3.4),I(0.6),[("Next: ",{'bold':True,'color':INK}),("'Be a Rakshak' university chapters at IITs, NITs and SPAs.",{'color':MUT})],size=9.5,ls=1.25)
    footer(s,wg,idx,total)
    return s

# ---------------------------------------------------------------- S12 GROUND
def ground(idx,total,wg):
    s=slide()
    header(s,"02 · What we have built, on the ground",
           [("Road Safety Month 2026, run ",False),("with the system",True)],
           lead="With district police, schools, hospitals and delivery platforms, in Hindi and local languages.",
           sect=(2,"WHAT WE HAVE BUILT"))
    photo(s,a5("ph_police_rally.jpg"),ML,I(2.12),I(4.7),I(3.55),fill=True,anchor=0.35,
          caption="National Road Safety Month rally, on the road with district traffic police, Jan 2026.")
    grid=[("ph_stall.jpg","CFI stall at a government office",0.45),
          ("ph_police_station.jpg","Materials briefing with police staff",0.35),
          ("ph_school_kids.jpg","School programme with certificates",0.3),
          ("ph_gig_riders.jpg","Delivery-rider outreach, Swiggy & Instamart",0.4)]
    for i,(f,cap,anc) in enumerate(grid):
        r,c=divmod(i,2)
        x=I(5.55)+c*I(3.65); y=I(2.12)+r*I(2.15)
        photo(s,a5(f),x,y,I(3.55),I(1.72),fill=True,anchor=anc,caption=cap)
    rect(s,ML,I(6.15),I(4.7),I(0.62),fill=GR_T,rounded=True,radius=0.16)
    text(s,ML+I(0.2),I(6.24),I(4.4),I(0.5),[("1M+ citizens reached ",{'bold':True,'color':GREEN}),("across campaigns in year one.",{'color':GREEN})],size=10.5,ls=1.2)
    footer(s,wg,idx,total)
    return s

# ---------------------------------------------------------------- S13 DHONI + PRESS (REDONE)
def dhoni(idx,total,wg):
    s=slide()
    header(s,"02 · What we have built, public voice",
           [("MS Dhoni gives road safety ",False),("a national voice",True)],
           sect=(2,"WHAT WE HAVE BUILT"))
    photo(s,a5("ph_dhoni_helmet.jpg"),ML,I(1.95),I(2.85),I(3.6),fill=True,anchor=0.1,
          caption="MS Dhoni, Goodwill Ambassador, announced April 2026.")
    rect(s,I(3.75),I(1.95),I(3.35),I(3.6),fill=MIST,rounded=True,radius=0.08)
    text(s,I(4.0),I(2.25),I(2.85),I(2.2),
         '"We already know what is going wrong. What we need now is more responsibility, more discipline, more respect for life."',
         font=HEAD,size=13,bold=True,color=INK,ls=1.35,italic=True)
    text(s,I(4.0),I(4.6),I(2.85),I(0.6),"MS Dhoni, at the National Road Safety\nImplementation Forum, IIT Delhi",size=9,color=MUT,ls=1.25)
    text(s,I(7.4),I(1.95),I(5.3),I(0.26),"AS SEEN IN THE PRESS",font=HEAD,size=8,bold=True,color=MUT,tracking=1.6)
    photo_fit(s,a6("press_ht_primer.png"),I(7.4),I(2.28),I(2.6),I(2.15),caption="Hindustan Times, on our\nPre-Hospital Care Primer.")
    photo_fit(s,a6("press_print_ideathon.png"),I(10.15),I(2.28),I(2.55),I(2.15),caption="ThePrint, on the NextMile\nideathon finale.")
    logo_chip(s,a6("lg_bloomberg.png"),I(7.4),I(5.15),I(1.6),I(0.6))
    press=["Deccan Herald","Economic Times","Fortune India","IndiaSpend","Scroll.in","The Wire","Times of India","Business Standard"]
    for i,p in enumerate(press):
        c=(i)%3; r=(i)//3
        chip(s,I(9.12)+c*I(1.24),I(5.15)+r*I(0.34),I(1.18),I(0.28),p,fill=PAPER,color=INK,size=6.5,bold=False,line=LINE)
    text(s,ML,I(5.95),I(6.6),I(0.55),"Dhoni's voice powers 'Be a Rakshak', school-zone safety and compensation-awareness campaigns.",size=10,color=MUT,ls=1.3)
    footer(s,wg,idx,total)
    return s

# ---------------------------------------------------------------- S14 PARTNERS (NEW)
def partners(idx,total,wg):
    s=slide()
    header(s,"02 · What we have built, the network",
           [("The institutions ",False),("around the work",True)],
           lead="As they appear in our working decks, engagement ranges from formal MoUs and written approvals to jury, mentoring and research collaboration.",
           sect=(2,"WHAT WE HAVE BUILT"))
    def lrow(label,files,y,ch=I(0.78)):
        text(s,ML,y,I(12),I(0.24),label,font=HEAD,size=8.5,bold=True,color=MUT,tracking=1.5)
        x=ML
        for f in files:
            logo_chip(s,a6(f),x,y+I(0.3),I(1.42),ch)
            x=x+I(1.52)
    lrow("AUTHORITIES & PUBLIC BODIES WE WORK WITH",
         ["lg_nhai.png","lg_pwd.png","lg_indore_nn.png","lg_vijayawada_police.png","lg_haryana_police.png","lg_kolkata_police.png","lg_kozhikode_tp.png","lg_dlsa.png"],I(1.95))
    lrow("UNIVERSITIES & INSTITUTES FIELDING AUDIT TEAMS",
         ["lg_iitm.png","lg_iitd.png","lg_nitc.png","lg_u29.png","lg_u30.png","lg_u25.png","lg_u22.png","lg_u105.png"],I(3.35))
    lrow("EXPERT & ECOSYSTEM PARTNERS",
         ["lg_tripc.png","lg_niua.png","lg_omi.png","lg_wri.png","lg_cii.png","lg_gic.png","lg_iffco.png","lg_nia.png"],I(4.75))
    rect(s,ML,I(6.15),CW,I(0.6),fill=MIST,rounded=True,radius=0.14)
    text(s,ML+I(0.22),I(6.25),CW-I(0.45),I(0.42),
         [("Plus: ",{'bold':True}),("Jaipur Traffic Police & Gurugram Police (MoUs) · CPWD & district administrations · Bloomberg, Johns Hopkins, Centre for Green Mobility and PwC experts on juries and reviews.",{'color':MUT})],size=9.5,ls=1.2)
    footer(s,wg,idx,total)
    return s

# ---------------------------------------------------------------- S15 TEAM (NEW)
def team(idx,total,wg):
    s=slide()
    header(s,"03 · Our people",
           [("A full-time team ",False),("built for this work",True)],
           lead="Engineering, law, policy, product and field operations, under trustees who have led Indian road safety for a decade.",
           sect=(3,"OUR PEOPLE"))
    trustees=[("t_amar.png","Amar Srivastava","President · Founder, Indian Road Safety Campaign · Member, National Road Safety Council"),
              ("t_deepanshu.png","Deepanshu Gupta","Managing Trustee · Founder, IRSC · Global Youth Coalition for Road Safety"),
              ("t_gajendra.png","Gajendra Jangid","General Secretary · Co-founder, Cars24")]
    x=ML
    for img,nm,cred in trustees:
        rect(s,x,I(2.1),I(3.97),I(0.98),fill=MIST,rounded=True,radius=0.10)
        circp(s,img,x+I(0.13),I(2.23),I(0.72))
        text(s,x+I(0.98),I(2.2),I(2.9),I(0.32),nm,font=HEAD,size=10.5,bold=True,color=INK)
        text(s,x+I(0.98),I(2.5),I(2.9),I(0.55),cred,size=8,color=MUT,ls=1.15)
        x=x+I(4.06)
    text(s,ML,I(3.32),I(12),I(0.26),"THE FULL-TIME TEAM",font=HEAD,size=8.5,bold=True,color=MUT,tracking=1.5)
    core=[("t_akhtar.png","Akhtar Hussain","Mission Lead","IIT Delhi · ex-Cars24 · leads strategy, partnerships and MoRTH/NRSB engagement"),
          ("t_shubham.png","Shubham Kumar","Policy & Advocacy","NALSAR Hyderabad · legal research, RTIs, Justice Unserved co-author"),
          ("t_muskan.png","Muskan Yadav","Programmes","TISS · runs district programmes, DRSC work and helpdesk operations"),
          ("t_aastha.png","Aastha Shreeharsh","Development Communications","HKUST · donor & institutional communications, impact reporting"),
          ("t_rohan.png","Rohan Sharma","Cause Marketing","Campaigns with police & schools · Road Safety Month, NextMile outreach"),
          ("t_ishita.png","Ishita Rathore","People & Culture","Talent, volunteers and the 75+ intern engineering corps"),
          ("t_yuvraj.png","Yuvraj Yadav","Operations","Field logistics across 18 cities · audit-cohort and event operations"),
          ("t_lovish.png","Lovish","Creative (Video)","Video explainers, ground-audit films and the YouTube channel"),
          ("t_shipra.png","Shipra Kushwaha","Creative (Graphic)","Guides, comics and bilingual campaign material families actually read")]
    cw_=I(4.06)
    for j,(img,nm,role,cred) in enumerate(core):
        r,c=divmod(j,3)
        x=ML+c*cw_; y=I(3.64)+r*I(0.82)
        circp(s,img,x,y+I(0.05),I(0.62))
        text(s,x+I(0.75),y,I(3.2),I(0.3),[(nm+"  ",{'bold':True,'size':9.5}),(role,{'color':BRAND,'size':8,'bold':True})],size=9,ls=1.0)
        text(s,x+I(0.75),y+I(0.24),I(3.2),I(0.55),cred,size=7.5,color=MUT,ls=1.12)
    rect(s,ML,I(6.05),CW,I(0.7),fill=MIST,rounded=True,radius=0.14)
    text(s,ML+I(0.22),I(6.13),CW-I(0.45),I(0.55),
         [("In-house capabilities: ",{'bold':True}),
          ("road-engineering audits · legal & policy research · AI product development · district operations · behaviour-change communication.   ",{'color':MUT}),
          ("Plus 75+ engineering interns and 31 student audit teams.",{'bold':True,'color':BRAND})],size=9.5,ls=1.25)
    footer(s,wg,idx,total)
    return s

# ---------------------------------------------------------------- S16 EXPERT BENCH
def bench(idx,total,wg):
    s=slide()
    header(s,"03 · Our people, the expert bench",
           [("Advised by the people who ",False),("built India's road safety practice",True)],
           sect=(3,"OUR PEOPLE"))
    y=I(1.7)
    rect(s,ML,y,I(6.0),I(1.02),fill=MIST,rounded=True,radius=0.12)
    circp(s,"x_gtiwari.png",ML+I(0.14),y+I(0.14),I(0.74))
    text(s,ML+I(1.02),y+I(0.13),I(4.9),I(0.35),"Prof. Geetam Tiwari, Board of Advisors",font=HEAD,size=11,bold=True,color=INK)
    text(s,ML+I(1.02),y+I(0.45),I(4.9),I(0.55),"Professor Emerita & Chair, TRIP Centre, IIT Delhi · Member, IRC H-7 Committee on Road Safety Audit",size=9,color=MUT,ls=1.2)
    x2=I(6.85)
    rect(s,x2,y,I(5.85),I(1.02),fill=MIST,rounded=True,radius=0.12)
    circle(s,x2+I(0.14),y+I(0.14),I(0.74),BR_T)
    text(s,x2+I(0.14),y+I(0.12),I(0.74),I(0.74),"PT",font=HEAD,size=14,bold=True,color=BRAND,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    text(s,x2+I(1.02),y+I(0.13),I(4.7),I(0.35),"Piyush Tewari, Board of Advisors",font=HEAD,size=11,bold=True,color=INK)
    text(s,x2+I(1.02),y+I(0.45),I(4.7),I(0.55),"Founder & CEO, SaveLIFE Foundation · Architect of the Good Samaritan Law · Zero-Fatality Corridors",size=9,color=MUT,ls=1.2)
    text(s,ML,I(2.95),I(11),I(0.26),"JURY, MENTORS & REVIEWERS AROUND OUR WORK",font=HEAD,size=8.5,bold=True,color=MUT,tracking=1.6)
    heads=[("midha","Justice J.R. Midha","Delhi High Court (Retd.)"),("damle","Abhay Damle","Ex-JS, MoRTH"),
           ("dange","Vaibhav Dange","Ex-Advisor, MoRTH"),("tandon","Dr. Maya Tandon","Sahayta Trust"),
           ("ratnam","R. Venkat Ratnam","Government of Punjab"),("asrivastava","Akhilesh Srivastava","ITS India · IRF"),
           ("gsingh","Gautam Singh","SaveLIFE Foundation"),("raman","Aishwarya Raman","OMI Foundation"),
           ("nkumar","Neeraj Kumar","Tata AIG"),("pandey","R.S. Pandey","FICCI Road Safety"),
           ("dash","Dipak K. Dash","Times of India")]
    cw_=I(2.04); y0=I(3.28)
    for i,(f,n,o) in enumerate(heads):
        r,c=divmod(i,6)
        x=ML+c*cw_; yy=y0+r*I(1.32)
        circp(s,"x_"+f+".png",x+I(0.64),yy,I(0.7))
        text(s,x,yy+I(0.74),cw_-I(0.1),I(0.3),n,font=HEAD,size=8.5,bold=True,color=INK,align=PP_ALIGN.CENTER,ls=1.0)
        text(s,x,yy+I(0.95),cw_-I(0.1),I(0.3),o,size=7.5,color=MUT,align=PP_ALIGN.CENTER,ls=1.0)
    rect(s,ML,I(6.08),CW,I(0.68),fill=MIST,rounded=True,radius=0.14)
    text(s,ML+I(0.22),I(6.15),CW-I(0.45),I(0.55),
         [("Engaged through the National Road Safety Dialogue Series: ",{'bold':True}),
          ("Balraj Bhanot (ex-Chair, CMVR-TSC) · I.V. Rao (TERI; ex-Maruti Suzuki) · D.P. Saste (CIRT / ex-MoRTH) · Dr. Sushma Sagar (AIIMS Trauma) · Dr. S. Velmurugan (CSIR-CRRI), and jurors from OMI, NIUA, WRI, CII and Tata AIG.",{'color':MUT})],size=9,ls=1.25)
    footer(s,wg,idx,total)
    return s

# ================================================================ WG-2 BODY
def wg2_body(wg,total,start):
    i=start
    # explainer
    s=slide()
    header(s,"04 · Project Rakshak, what it is",
           [("Project Rakshak, ",False),("in one sentence",True)],sect=(4,"PROJECT RAKSHAK"))
    text(s,ML,I(1.72),I(12.0),I(0.85),
         "Trained student teams, guided by senior road-safety experts, audit dangerous road locations, and Crashfree India walks each recommended fix through the road-owning authority until it is built.",
         font=HEAD,size=15.5,bold=False,color=INK,ls=1.35)
    cards=[("clipboard-list","Students audit","Teams from IITs, NITs and SPAs collect data on-site: traffic, conflicts, 900+ stakeholder surveys.",a5("guntur_junction.jpg"),0.4),
           ("badge-check","Experts verify","Mentors anchor every audit to IRC codes and MoRTH checklists before anything is proposed.",a5("ph_jury_room.jpg"),0.35),
           ("hard-hat","Authorities build","The fix goes to the PWD, corporation or NHAI in its own format, and we track it to completion.",a5("implementation_work.jpg"),0.3)]
    tw=I(3.95); gx=I(0.12)
    for j,(ic,t,d,img,anc) in enumerate(cards):
        x=ML+j*(tw+gx); y=I(2.75)
        rect(s,x,y,tw,I(3.3),fill=PAPER,line=LINE,rounded=True,radius=0.06)
        photo(s,img,x,y,tw,I(1.55),fill=True,border=False,anchor=anc)
        rect(s,x,y,tw,I(1.55),fill=None,line=LINE,lw=1.0)
        icon_disc(s,ic,x+I(0.15),y+I(1.7),I(0.42),BR_T,"#4A35FF")
        text(s,x+I(0.7),y+I(1.76),tw-I(0.85),I(0.35),t,font=HEAD,size=12.5,bold=True,color=INK)
        text(s,x+I(0.15),y+I(2.22),tw-I(0.3),I(1.0),d,size=9.5,color=MUT,ls=1.25)
    text(s,ML,I(6.3),CW,I(0.35),
         [("Four phases each cohort: ",{'bold':True}),("Research & problem identification  →  Stakeholder engagement & audits  →  Analysis & costed solutions  →  Reporting & authority engagement",{'color':MUT})],size=10,ls=1.2)
    footer(s,wg,i,total); i+=1
    # gap
    s=slide()
    header(s,"04 · Project Rakshak, why it matters to WG-2",
           [("Identification has outpaced rectification, ",False),("capacity is the constraint",True)],
           lead="The knowledge exists; the pipeline that turns identified risk into completed engineering needs more trained hands.",
           sect=(4,"PROJECT RAKSHAK"))
    stat(s,ML,I(2.3),I(3.4),"13,795","black spots identified nationally (MoRTH)",vsize=30,card=True,h=I(1.3))
    stat(s,ML+I(3.55),I(2.3),I(3.4),"5,036","permanently rectified so far (Parliamentary Standing Committee, 2024)",vsize=30,card=True,h=I(1.3))
    stat(s,ML+I(7.1),I(2.3),I(3.4),"44","certified Road Safety Auditors on the national registry (July 2026)",vsize=30,card=True,h=I(1.3),color=AMBER)
    text(s,ML,I(3.95),I(7.3),I(1.3),
         "Low-cost engineering measures, raised crossings, traffic calming, lighting, safer intersections, reduce crashes by 20–80% where applied (iRAP & PIARC evidence). What limits progress is steady, supervised auditing capacity and follow-up, working under the road-owning authority.",
         size=11,color=INK,ls=1.4)
    rect(s,ML,I(5.5),I(7.3),I(0.95),fill=BR_T,rounded=True,radius=0.12)
    text(s,ML+I(0.22),I(5.62),I(6.9),I(0.75),
         [("Project Rakshak was designed for precisely this constraint: ",{'bold':True,'color':BRAND}),
          ("trained auditing capacity that supports road-owning agencies, and tracks every fix to completion.",{'color':BRAND})],size=10.5,ls=1.3)
    photo(s,a3("iv_guntur_drainage.png"),I(8.35),I(3.95),I(4.35),I(2.5),fill=True,anchor=0.4,
          caption="Guntur, Andhra Pradesh, drainage correction underway after audit.")
    footer(s,wg,i,total); i+=1
    # footprint
    s=slide()
    header(s,"04 · Project Rakshak, year one",
           [("Cohort 1: a ",False),("national footprint",True),(", now delivering",False)],sect=(4,"PROJECT RAKSHAK"))
    fun=[("120+","locations screened",MIST),("31","sites audited, 11 official black spots",MIST),
         ("25+","written authority approvals",MIST),("7 + 6","fully implemented + partially built",None)]
    y=I(2.15)
    for j,(v,l,fill) in enumerate(fun):
        x=ML+j*I(2.1)
        if fill is None:
            rect(s,x,y,I(1.95),I(1.25),fill=BRAND,rounded=True,radius=0.12)
            text(s,x+I(0.14),y+I(0.12),I(1.7),I(0.55),v,font=HEAD,size=24,bold=True,color=PAPER,ls=1.0)
            text(s,x+I(0.14),y+I(0.62),I(1.7),I(0.55),l,size=8.5,color=PAPER,ls=1.1)
        else:
            rect(s,x,y,I(1.95),I(1.25),fill=MIST,rounded=True,radius=0.12)
            text(s,x+I(0.14),y+I(0.12),I(1.7),I(0.55),v,font=HEAD,size=24,bold=True,color=BRAND,ls=1.0)
            text(s,x+I(0.14),y+I(0.62),I(1.7),I(0.55),l,size=8.5,color=MUT,ls=1.1)
        if j<3: text(s,x+I(1.93),y+I(0.4),I(0.2),I(0.4),"→",size=14,color=MUT)
    text(s,ML,I(3.62),I(8.2),I(0.3),"31 student teams · 20 institutions including nine IITs · 900+ stakeholder surveys · 17 subject-matter experts guiding and reviewing every audit",size=10,color=MUT,ls=1.3)
    text(s,ML,I(4.1),I(8.2),I(0.75),
         "North: Ropar, Dehradun, Roorkee, Delhi, Lucknow, Varanasi · East: Guwahati, Durgapur · West & Central: Indore, Mumbai, Surat · South: Vijayawada, Guntur, Kozhikode, Chennai, among 18 cities.",size=10,color=MUT,ls=1.35)
    rect(s,ML,I(5.15),I(8.2),I(1.3),fill=AM_T,rounded=True,radius=0.10)
    text(s,ML+I(0.22),I(5.3),I(7.8),I(1.0),
         [("Estimated 20–50% crash reduction at treated sites once complete ",{'bold':True,'color':AMBER}),
          (", based on WHO / iRAP evidence for these counter-measures; we will verify with before-and-after data as implementations finish.",{'color':AMBER})],size=10.5,ls=1.3)
    photo(s,a5("cfi_map_dots.png"),I(9.1),I(2.1),I(3.6),caption="Cohort-1 sites across India.")
    footer(s,wg,i,total); i+=1
    # approvals
    s=slide()
    header(s,"04 · Project Rakshak, the paper trail",
           [("Approvals ",False),("in writing",True),(", from the authorities that own the roads",False)],sect=(4,"PROJECT RAKSHAK"))
    real=[f for f in sorted(os.listdir(LTR)) if f.endswith('.png')][:6]
    lw_=I(1.92); lh=I(2.5); y=I(2.0)
    for j,f in enumerate(real):
        x=ML+j*(lw_+I(0.11))
        photo(s,os.path.join(LTR,f),x,y,lw_,lh,fill=True,anchor=0.0)
    text(s,ML,I(4.7),CW,I(0.3),"A sample of the 25+ approval and acknowledgement letters issued by public works and district authorities.",size=9.5,color=MUT)
    text(s,ML,I(5.12),I(3.3),I(0.26),"APPROVING AUTHORITIES INCLUDE",font=HEAD,size=8.5,bold=True,color=MUT,tracking=1.6)
    auth=["PWD Kerala","PWD Uttar Pradesh","PWD Punjab","CPWD + Addl. Collector, Indore","ADDA Durgapur","R&B Andhra Pradesh","GCC Chennai","BMC Mumbai"]
    for j,a in enumerate(auth):
        c=j%4; r=j//4
        chip(s,ML+c*I(2.42),I(5.44)+r*I(0.5),I(2.34),I(0.42),a,fill=GR_T,color=GREEN,size=8.5,bold=True)
    logo_chip(s,a6("lg_pwd.png"),I(10.45),I(5.35),I(1.1),I(0.62))
    logo_chip(s,a6("lg_nhai.png"),I(11.62),I(5.35),I(1.1),I(0.62))
    logo_chip(s,a6("lg_indore_nn.png"),I(10.45),I(6.02),I(1.1),I(0.62))
    logo_chip(s,a6("lg_dlsa.png"),I(11.62),I(6.02),I(1.1),I(0.62))
    footer(s,wg,i,total); i+=1
    # on the ground + live status
    s=slide()
    header(s,"04 · Project Rakshak, on the ground",
           [("From approval to construction, ",False),("and to completion",True)],
           lead="Live status from our public implementation tracker, August 2026.",sect=(4,"PROJECT RAKSHAK"))
    ivs=[("iv_durgapur_parking.png","Parking rationalisation, Durgapur",0.35),("iv_guntur_markings.png","Fresh markings, Guntur",0.4),
         ("iv_indore_footpath.png","Footpath construction, Indore",0.4),("iv_mumbai_signage.png","Signage, Mumbai",0.35)]
    for j,(f,cap,anc) in enumerate(ivs):
        r,c=divmod(j,2)
        x=ML+c*I(2.72); y=I(2.2)+r*I(2.2)
        photo(s,a3(f),x,y,I(2.6),I(1.75),fill=True,anchor=anc,caption=cap)
    xr=I(6.2)
    rect(s,xr,I(2.2),I(6.5),I(1.72),fill=GR_T,rounded=True,radius=0.08)
    text(s,xr+I(0.22),I(2.34),I(6.1),I(0.3),[("7 sites fully implemented",{'bold':True,'color':GREEN,'size':13})],size=13)
    text(s,xr+I(0.22),I(2.72),I(6.1),I(1.1),
         "Outer Ring Road (Delhi) · IIT Madras Taramani Gate (Chennai) · Dafi Toll Plaza (Varanasi) · Akurli Road Underpass (Mumbai) · C-49 Commercial Area (Durgapur) · Chuttugunta Circle (Guntur) · Rau Gol Square (Indore)",size=9.5,color=INK,ls=1.35)
    rect(s,xr,I(4.08),I(6.5),I(0.95),fill=MIST,rounded=True,radius=0.08)
    text(s,xr+I(0.22),I(4.2),I(6.1),I(0.7),
         [("6 more partially implemented ",{'bold':True,'color':BRAND}),
          (": Kunnamangalam & Chevayur (Kozhikode), TIDEL Park (Chennai), Shivpur (Varanasi), Tejaji Nagar (Indore), Civil Lines (Roorkee); action initiated at further sites.",{'color':MUT})],size=9.5,ls=1.3)
    rect(s,xr,I(5.18),I(6.5),I(1.3),fill=PAPER,line=LINE,rounded=True,radius=0.08)
    text(s,xr+I(0.22),I(5.3),I(6.1),I(0.3),"MARQUEE CASE, OUTER RING ROAD, SOUTH DELHI",font=HEAD,size=8.5,bold=True,color=BRAND,tracking=1.2)
    text(s,xr+I(0.22),I(5.62),I(6.1),I(0.8),
         "On our audit, PWD built a continuous 1.8 m accessible pedestrian corridor, upgraded drainage at ponding sites, installed bollards against footpath encroachment, and deployed camera-backed speed-feedback boards.",size=9.5,color=INK,ls=1.3)
    footer(s,wg,i,total); i+=1
    # dashboard
    s=slide()
    header(s,"04 · Project Rakshak, transparency",
           [("A public dashboard tracks ",False),("every site to completion",True)],sect=(4,"PROJECT RAKSHAK"))
    photo(s,a5("rakshak_dashboard_full.png"),ML,I(1.98),I(7.6),caption="Live public dashboard, every site, its authority, risk level and implementation stage.")
    x=I(8.55); rows=[
      ("route","Every site tracked","From submission through approval to completed construction, regardless of who audited it.",BR_T,"#4A35FF"),
      ("git-compare","The PRAGATI parallel","The PM's PRAGATI platform showed what visible follow-up does for stuck projects. Same principle here, for road safety fixes.",TE_T,"#0E8A8A"),
      ("eye","What the Board gains","An honest, live read on how quickly road-owning agencies can act, evidence for capacity planning, not just compliance.",GR_T,"#0A9955")]
    y=I(2.05)
    for ic,t,d,tint,col in rows:
        icon_disc(s,ic,x,y,I(0.42),tint,col)
        text(s,x+I(0.58),y-I(0.03),I(3.6),I(0.35),t,font=HEAD,size=11,bold=True,color=INK)
        text(s,x+I(0.58),y+I(0.3),I(3.6),I(1.0),d,size=9.5,color=MUT,ls=1.25)
        y=y+I(1.5)
    footer(s,wg,i,total); i+=1
    # method
    s=slide()
    header(s,"04 · Project Rakshak, method",
           [("Anchored to the codes ",False),("your engineers already use",True)],sect=(4,"PROJECT RAKSHAK"))
    rows=[("book-check","IRC codes & MoRTH checklists","Every audit instrument is built on them, nothing bespoke, nothing incompatible.",BR_T,"#4A35FF"),
          ("link","A line into IRC H-7","Prof. Geetam Tiwari, member of the IRC H-7 Committee on Road Safety Audit, chairs our advisory work.",GR_T,"#0A9955"),
          ("graduation-cap","Masterclasses before fieldwork","Prof. Tiwari on the Safe System approach; Dr. S. Velmurugan (CSIR-CRRI) on IRC-131 and SP-55.",AM_T,"#E58900"),
          ("file-output","Handover in the authority's format","Findings arrive as the PWD or corporation needs them, ready to action, tracked publicly after.",TE_T,"#0E8A8A")]
    y=I(2.1)
    for j,(ic,t,d,tint,col) in enumerate(rows):
        irow(s,ML,y+j*I(0.95),I(7.5),ic,t,d,tint,col)
    photo(s,a6("ph_auth_roundtable.jpeg"),I(8.5),I(2.1),I(4.2),I(2.5),fill=True,anchor=0.3,
          caption="Authority engagement is continuous, audit teams present to the engineers who own the road.")
    photo(s,a6("ph_auth_handover.jpeg"),I(8.5),I(5.1),I(4.2),I(1.55),fill=True,anchor=0.25,border=True)
    footer(s,wg,i,total); i+=1
    # SMEs involved (NEW, v5)
    s=slide()
    header(s,"04 · Project Rakshak, the expert layer",
           [("Seventeen experts work with us on ",False),("infrastructure improvement",True)],
           lead="Academics and practitioners who guide the student teams through fieldwork and independently review every audit before it reaches an authority.",
           sect=(4,"PROJECT RAKSHAK"))
    smes=[("Amandeep Kumar","Urban Transport Planner, KPMG"),
          ("Dr. AVA Bharat Kumar","Asst Prof., Vignan University"),
          ("Asha SVT","Ph.D. Scholar, IIT Delhi"),
          ("Parveen Kumar","Ph.D., IIT Delhi"),
          ("Rashmeet Kaur","Ph.D., IIT Delhi"),
          ("Rajat Kalsi","Road Safety Expert"),
          ("Priyanshu Aman","Ph.D., IIT Delhi"),
          ("Mehraab Nazir","Ph.D., IIT Delhi"),
          ("Dr. Hemant Kumar Suman","Asst Prof., CTRANS, IIT Roorkee"),
          ("Dr. Shriniwas S Arkatkar","Professor, SVNIT Surat"),
          ("Dr. Sandeep Peeke","Asst Prof., SPA Vijayawada"),
          ("Dr. Purnima K Chowdhury","Asst Prof., SPA Bhopal"),
          ("Dr. Anshu Bamney","Asst Prof., IIT Mandi"),
          ("V. Sai Sesidhar","Ph.D., IIT Kharagpur"),
          ("Ashish Shrivastava","Engineer, Traffic & Transport Planning"),
          ("Mridul Sharotary","Planner, EY"),
          ("Kushal Khivansara","TRIP Centre, IIT Delhi")]
    cw_=I(2.015); y0=I(2.32)
    for j,(nm,role) in enumerate(smes):
        r,c=divmod(j,6)
        x=ML+c*cw_; yy=y0+r*I(1.34)
        init="".join(w[0] for w in nm.replace("Dr. ","").replace("Prof. ","").split()[:2]).upper()
        circle(s,x+I(0.70),yy,I(0.56),BR_T)
        text(s,x+I(0.70),yy-I(0.02),I(0.56),I(0.6),init,font=HEAD,size=11,bold=True,color=BRAND,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        text(s,x,yy+I(0.60),cw_-I(0.08),I(0.32),nm,font=HEAD,size=8,bold=True,color=INK,align=PP_ALIGN.CENTER,ls=1.02)
        text(s,x,yy+I(0.94),cw_-I(0.08),I(0.34),role,size=7,color=MUT,align=PP_ALIGN.CENTER,ls=1.05)
    rect(s,ML,I(6.42),CW,I(0.5),fill=MIST,rounded=True,radius=0.14)
    text(s,ML+I(0.22),I(6.50),CW-I(0.45),I(0.36),
         [("From IIT Delhi, IIT Roorkee, IIT Mandi, IIT Kharagpur, SVNIT, SPA Vijayawada, SPA Bhopal, Vignan University, KPMG and EY ",{'bold':True}),
          (", the same mix of academia and practice the Working Group draws on.",{'color':MUT})],size=9,ls=1.2)
    footer(s,wg,i,total); i+=1
    # scaling
    s=slide()
    header(s,"04 · Project Rakshak, the long view",
           [("Built to be ",False),("institutionalised",True),(": not built to depend on us",False)],
           lead="Three audit tracks matched to road types, and a role for CFI that narrows over time.",sect=(4,"PROJECT RAKSHAK"))
    tracks=[("A, Institutional","IIT / NIT / SPA teams under expert mentors","Urban arterials, in-town state highways, district roads",BR_T,BRAND),
            ("B, NGO partners","Field teams; desk-reviewed and re-verified by CFI","District & peri-urban corridors",TE_T,TEAL),
            ("C, Certified RSAs","CSIR-CRRI-certified auditors, full IRC SP-88","National highways, complex junctions",AM_T,AMBER)]
    tw=I(3.95)
    for j,(t,who,road,tint,col) in enumerate(tracks):
        x=ML+j*(tw+I(0.12)); y=I(2.3)
        rect(s,x,y,tw,I(1.75),fill=MIST,rounded=True,radius=0.08)
        rect(s,x,y,tw,I(0.42),fill=tint)
        text(s,x+I(0.16),y+I(0.07),tw-I(0.3),I(0.3),f"Track {t}",font=HEAD,size=11,bold=True,color=col)
        text(s,x+I(0.16),y+I(0.52),tw-I(0.32),I(0.6),who,size=9.5,color=INK,ls=1.25)
        text(s,x+I(0.16),y+I(1.18),tw-I(0.32),I(0.5),road,size=9,color=MUT,ls=1.2)
    stages=[("Today","CFI runs cohorts, quality-controls audits and stewards the public portal.",BRAND),
            ("Next","Rakshak Audit Manual v1.0 codifies the method; universities field their own teams; NGOs run Track B directly.",TEAL),
            ("Mature","States engage certified RSAs for Track C without CFI as intermediary; the portal remains the shared public record.",GREEN)]
    y=I(4.45)
    for j,(t,d,col) in enumerate(stages):
        yy=y+j*I(0.72)
        chip(s,ML,yy,I(1.35),I(0.5),t,fill=MIST,color=col,size=10)
        text(s,ML+I(1.55),yy+I(0.05),I(10.4),I(0.5),d,size=10.5,color=MUT,ls=1.25)
    footer(s,wg,i,total); i+=1
    # VRU
    s=slide()
    header(s,"04 · Vulnerable road users",
           [("A growing evidence base on ",False),("those most at risk",True)],
           lead="Roughly 70% of India's road crash fatalities are vulnerable road users, pedestrians, motorcyclists, bicyclists.",
           sect=(4,"PROJECT RAKSHAK"))
    rows=[("bike","Gig & delivery riders","'When Risks Become Routine' (Feb 2026): incentive pressure, helmet compliance and training gaps, 300+ rider study, Delhi NCR.",AM_T,"#E58900"),
          ("footprints","Pedestrian-first audits","Rakshak audits document crossings, footpaths and lighting as designable protections, 900+ stakeholders consulted.",BR_T,"#4A35FF"),
          ("school","School zones","College-led, standards-based school-zone screening under exploration as the next extension of the audit platform.",TE_T,"#0E8A8A"),
          ("shield","Enforcement that protects VRUs","SATARK helps police prioritise the small share of vehicles with the worst records, targeted, fair, technology-led.",GR_T,"#0A9955")]
    y=I(2.45)
    for j,(ic,t,d,tint,col) in enumerate(rows):
        irow(s,ML,y+j*I(1.0),I(7.5),ic,t,d,tint,col)
    photo_fit(s,a6("chart_vru_trends.png"),I(8.5),I(2.45),I(4.2),I(2.2),caption="Fatality trends by road-user type, 2014–2023 (MoRTH; via IndiaSpend).")
    photo(s,a5("ph_gig_riders.jpg"),I(8.5),I(5.2),I(4.2),I(1.45),fill=True,anchor=0.35,border=True)
    footer(s,wg,i,total); i+=1
    return i

# ================================================================ WG-5 BODY
def wg5_body(wg,total,start):
    i=start
    # pendency
    s=slide()
    header(s,"04 · Post-crash care, the problem, measured",
           [("Compensation pendency, ",False),("in numbers",True)],
           lead="Families and courts both lose to process friction. This is a pipeline problem, and pipelines can be fixed with standards and visibility.",
           sect=(4,"POST-CRASH CARE"))
    tiles=[("₹80,000+ Cr","held up across 10.46 lakh pending MACT cases nationally"),
           ("11 lakh","claims pending in MACT courts (FY 2023)"),
           ("3.6 years","average time to settlement, for those who persist"),
           ("20–40","office visits to keep a single claim alive"),
           ("~1 in 7","hit-and-run crashes becomes a registered compensation claim (FY26)"),
           ("~₹986 Cr","awarded but unclaimed in MACT accounts, in just 5 cities")]
    tw=I(3.95)
    for j,(v,l) in enumerate(tiles):
        r,c=divmod(j,3)
        x=ML+c*(tw+I(0.12)); y=I(2.35)+r*I(1.5)
        rect(s,x,y,tw,I(1.36),fill=MIST,rounded=True,radius=0.08)
        text(s,x+I(0.18),y+I(0.12),tw-I(0.36),I(0.5),v,font=HEAD,size=20,bold=True,color=BRAND if j!=5 else AMBER)
        text(s,x+I(0.18),y+I(0.64),tw-I(0.36),I(0.65),l,size=9,color=MUT,ls=1.2)
    photo_fit(s,a6("cov_deposited.png"),I(10.35),I(5.5),I(2.35),I(1.25),caption=None)
    text(s,ML,I(5.6),I(9.9),I(0.9),
         [("'Deposited But Not Delivered' ",{'bold':True}),
          (", our research brief on court-awarded money that never reaches families, maps exactly where the pipeline leaks: awareness, documents, traceability, and the hand-offs between offices.",{'color':MUT})],size=10.5,ls=1.35)
    footer(s,wg,i,total); i+=1
    # justice unserved
    s=slide()
    header(s,"04 · Post-crash care, our research foundation",
           [("'Justice Unserved', ",False),("the evidence base",True),(" we built first",False)],
           lead="Published January 2026 · launched at IIT Delhi · findings presented to MoRTH · covered by national press.",
           sect=(4,"POST-CRASH CARE"))
    photo(s,a3("comp_image1.png"),ML,I(2.15),I(2.75),caption="The report, file reviews, RTIs and\nconsultations across the pipeline.")
    rows=[("megaphone","Awareness","70% of low-income families are unaware compensation exists.",AM_T,"#E58900"),
          ("clock","Timeliness","3.6-year average claim; MACT cases often run 8–10 years.",AM_T,"#E58900"),
          ("file-x","Documentation","90% of pending hit-and-run claims stall on documents alone.",AM_T,"#E58900"),
          ("scale","Adequacy","Informal workers are often valued at minimum wage in courts.",AM_T,"#E58900"),
          ("users","Equity","14% of low-income households compensated vs 24% of high-income.",AM_T,"#E58900")]
    x=I(3.95); y=I(2.15)
    for j,(ic,t,d,tint,col) in enumerate(rows):
        icon_disc(s,ic,x,y+j*I(0.72),I(0.4),tint,col)
        text(s,x+I(0.55),y+j*I(0.72)-I(0.02),I(1.7),I(0.35),t,font=HEAD,size=10.5,bold=True,color=INK)
        text(s,x+I(2.28),y+j*I(0.72)-I(0.02),I(2.62),I(0.68),d,size=9,color=MUT,ls=1.18)
    rect(s,I(9.05),I(2.15),I(3.65),I(3.4),fill=MIST,rounded=True,radius=0.08)
    text(s,I(9.25),I(2.3),I(3.3),I(0.3),"THE CLAIM RATE, NATIONALLY",font=HEAD,size=8.5,bold=True,color=MUT,tracking=1.2)
    bars=[("~30,000","hit-and-run deaths every year (MoRTH)",I(3.1),INK),
          ("9,813","claims registered, FY 2025-26",I(1.02),BRAND),
          ("7,348","claims paid, to 28 Feb 2026",I(0.76),GREEN)]
    yb=I(2.75)
    for v,l,w,col in bars:
        rect(s,I(9.25),yb,w,I(0.3),fill=col,rounded=True,radius=0.5)
        text(s,I(9.25),yb+I(0.32),I(3.3),I(0.28),[(v+"  ",{'bold':True,'size':10,'color':col}),(l,{'size':8,'color':MUT})],ls=1.0)
        yb=yb+I(0.75)
    text(s,I(9.25),I(5.0),I(3.25),I(0.5),"Claims are up 48x since FY23 (205), yet most losses still never become claims. Source: Lok Sabha reply AU6419, April 2026.",size=8.5,color=MUT,ls=1.2,italic=True)
    text(s,ML,I(6.1),I(12),I(0.5),
         [("Press: ",{'bold':True}),("Deccan Herald · Economic Times · Fortune India · IndiaSpend · Scroll.in · The Wire, and cited in Parliament-facing briefings.",{'color':MUT})],size=9.5,ls=1.2)
    footer(s,wg,i,total); i+=1
    # district machinery
    s=slide()
    header(s,"04 · Post-crash care, from research to districts",
           [("Working ",False),("inside the district machinery",True)],
           lead="Not commentary from outside, formal seats, formal tasking, files on the table.",sect=(4,"POST-CRASH CARE"))
    rows=[("landmark","Four DRSCs joined","Gurugram, South-West Delhi, North-West Delhi and Jaipur, with MoUs with Jaipur Traffic Police and Gurugram Police.",BR_T,"#4A35FF"),
          ("folder-open","File-level pipeline support","With district administrations we work the hit-and-run pipeline file by file, mapping where eligible families drop out, and helping offices close those gaps.",TE_T,"#0E8A8A"),
          ("clipboard-check","Formally tasked","The South-West Delhi DRSC's signed minutes task Crashfree India with digitisation and analytics support for scheme files.",GR_T,"#0A9955"),
          ("user-check","Embedded presence","A research fellow sits with Gurugram district offices, implementation support, not external commentary.",AM_T,"#E58900")]
    y=I(2.25)
    for j,(ic,t,d,tint,col) in enumerate(rows):
        irow(s,ML,y+j*I(1.0),I(7.5),ic,t,d,tint,col)
    photo(s,a5("ph_helpdesk_camp.jpg"),I(8.5),I(2.2),I(4.2),I(2.2),fill=True,anchor=0.35,
          caption="Legal-rights helpdesk with district administration, Jan 2026.")
    photo(s,a5("ph_law_students.jpg"),I(8.5),I(4.95),I(4.2),I(1.6),fill=True,anchor=0.3,
          caption="Law-student volunteers after a hospital helpdesk drive.")
    footer(s,wg,i,total); i+=1
    # rajasthan
    s=slide()
    header(s,"04 · Post-crash care, state engagement",
           [("With Rajasthan: from ground mapping to ",False),("a working template",True)],
           lead="Supporting the State Road Safety Lead Agency and Transport Department on the Hit-and-Run Compensation Scheme.",
           sect=(4,"POST-CRASH CARE"))
    rect(s,ML,I(2.25),I(3.6),I(1.9),fill=MIST,rounded=True,radius=0.08)
    text(s,ML+I(0.2),I(2.45),I(3.2),I(0.7),"~180",font=HEAD,size=36,bold=True,color=BRAND)
    text(s,ML+I(0.2),I(3.2),I(3.2),I(0.8),[("of ~",{'color':MUT}),("395",{'bold':True}),(" monthly hit-and-run claims in Rajasthan come from Jaipur alone (~46%)",{'color':MUT})],size=10,ls=1.25)
    text(s,ML,I(4.4),I(3.6),I(1.0),"Not because crashes happen only there, because Jaipur runs active outreach and a single coordination cell. The template is replicable.",size=9.5,color=MUT,ls=1.3)
    x=I(4.5)
    rows=[("file-warning","What holds claims back","11–13 documents demanded vs the 7 court-agreed standard · ~50% of files lack a usable family phone number · manual hand-offs between six offices.",AM_T,"#E58900"),
          ("alert-octagon","The cautionary example","A state portal that changed how offices work saw monthly requests fall 350 → 25. Our design rule: no stakeholder changes their medium.",RD_T,"#E11900"),
          ("list-checks","Five GIC queries drafted","Clarification questions ready for the insurer consortium, a joint ask from the Department lands harder.",BR_T,"#4A35FF"),
          ("rocket","Six asks → 60 days","Decisions identified with the Department that put Phase 1 (family traceability) in motion within 60 days.",GR_T,"#0A9955")]
    y=I(2.25)
    for j,(ic,t,d,tint,col) in enumerate(rows):
        icon_disc(s,ic,x,y+j*I(1.06),I(0.42),tint,col)
        text(s,x+I(0.58),y+j*I(1.06)-I(0.03),I(2.5),I(0.6),t,font=HEAD,size=11,bold=True,color=INK,ls=1.1)
        text(s,x+I(3.15),y+j*I(1.06)-I(0.03),I(5.05),I(0.95),d,size=9.5,color=MUT,ls=1.22)
    footer(s,wg,i,total); i+=1
    # portal
    s=slide()
    header(s,"04 · Post-crash care, the portal concept",
           [("Designed so ",False),("no stakeholder changes how they work",True)],
           lead="Families stay on WhatsApp; officers keep their queues and sign-offs; the system connects them behind the scenes.",
           sect=(4,"POST-CRASH CARE"))
    for j in range(3):
        photo(s,a5(f"wa_phone{j+1}.png"),ML+j*I(1.55),I(2.2),I(1.45),border=False)
    text(s,ML,I(4.45),I(4.6),I(0.5),"The family flow, day-one intake, document capture, live status. All inside WhatsApp, in Hindi.",size=9,color=MUT,ls=1.25)
    photo(s,a5("queue_ui.png"),I(5.55),I(2.2),I(7.15),caption="Officer view, same cases, filtered to what each desk owns; AI pre-checks flag issues, the decision stays human.")
    prins=["Family keeps WhatsApp","Officer keeps every decision","Traceability before automation","Single-pass clarification","Dashboards for administrators"]
    y=I(5.85)
    for j,p in enumerate(prins):
        chip(s,ML+j*I(2.46),y,I(2.36),I(0.46),p,fill=BR_T,color=BRAND,size=9)
    footer(s,wg,i,total); i+=1
    # primer (NEW)
    s=slide()
    header(s,"04 · Post-crash care, the first hour",
           [("The Pre-Hospital Care Primer, ",False),("our EMS evidence line",True)],
           lead="Published September 2025. Contributors include Dr. Sushma Sagar (AIIMS JPN Apex Trauma Centre) and Dr. Richa Ahuja (IIT Kharagpur).",
           sect=(4,"POST-CRASH CARE"))
    photo_fit(s,a6("primer_cover-01.jpg"),ML,I(2.15),I(2.55),I(3.5),caption="The Primer, ERSS-112, global\ncomparisons, state innovations.")
    photo_fit(s,a6("primer_chain-07.jpg"),I(3.4),I(2.15),I(2.55),I(3.5),caption="The Chain of Survival, six links,\nbenchmarked for India.")
    x=I(6.6)
    rows=[("timer","The response gap, measured","ERSS-112 is live across all 36 states & UTs, yet ambulance arrival averages 25–35 minutes, and the full care episode runs 55–75 minutes against a 60-minute golden hour.",TE_T,"#0E8A8A"),
          ("map","State innovations documented","Maharashtra's MEMS, 937 ambulances under centralised dispatch; Tamil Nadu's TAEI trauma corridors, pre-arrival alerts and protocols.",BR_T,"#4A35FF"),
          ("heart-handshake","The demand side too","Good Samaritan protections and the ₹1.5 lakh / 7-day Cashless Treatment Scheme 2025, explained in our public guides and helpdesks.",GR_T,"#0A9955"),
          ("stethoscope","Ready for WG-5","A referenced baseline for the Group's EMS and trauma-care standards discussions, states already compared, gaps already mapped.",AM_T,"#E58900")]
    y=I(2.15)
    for j,(ic,t,d,tint,col) in enumerate(rows):
        icon_disc(s,ic,x,y+j*I(1.13),I(0.42),tint,col)
        text(s,x+I(0.58),y+j*I(1.13)-I(0.03),I(2.1),I(0.6),t,font=HEAD,size=10.5,bold=True,color=INK,ls=1.08)
        text(s,x+I(2.75),y+j*I(1.13)-I(0.03),I(3.35),I(1.05),d,size=9,color=MUT,ls=1.2)
    text(s,ML,I(6.05),I(6.0),I(0.6),
         [("Covered by Hindustan Times: ",{'bold':True}),("'India's Road Safety Primer Flags Gaps in Pre-Hospital Emergency Care.'",{'color':MUT,'italic':True})],size=10,ls=1.3)
    footer(s,wg,i,total); i+=1
    # helpdesks
    s=slide()
    header(s,"04 · Post-crash care, in the wards",
           [("Helpdesks where families actually are: ",False),("trauma wards",True)],sect=(4,"POST-CRASH CARE"))
    photo(s,a5("ph_helpdesk_desk.jpg"),ML,I(2.05),I(4.3),I(2.6),fill=True,anchor=0.4,
          caption="Hospital legal helpdesk, 100+ victims supported in the first four days of operation.")
    photo(s,a5("ph_stall.jpg"),ML,I(5.15),I(4.3),I(1.45),fill=True,anchor=0.45,border=True)
    x=I(5.35)
    rows=[("life-buoy","What the desk does","FIR follow-up, document checklists, DLSA referrals and compensation guidance, at the bedside, in Hindi.",GR_T,"#0A9955"),
          ("users","Who runs it","Trained law-student volunteers under practising advocates, with Neev Foundation and DLSA coordination.",BR_T,"#4A35FF"),
          ("map-pin","Where it grows","Gurugram and Delhi trauma wards first; the district toolkit makes it replicable wherever a DRSC wants one.",TE_T,"#0E8A8A"),
          ("book-open","Backed by materials","The Hindi legal-rights guide and 'Meet Aasha' comics live at every desk, and Aasha continues the help at home, 24/7.",AM_T,"#E58900")]
    y=I(2.05)
    for j,(ic,t,d,tint,col) in enumerate(rows):
        icon_disc(s,ic,x,y+j*I(1.13),I(0.42),tint,col)
        text(s,x+I(0.58),y+j*I(1.13)-I(0.03),I(2.2),I(0.6),t,font=HEAD,size=10.5,bold=True,color=INK,ls=1.08)
        text(s,x+I(2.85),y+j*I(1.13)-I(0.03),I(4.45),I(1.05),d,size=9,color=MUT,ls=1.2)
    footer(s,wg,i,total); i+=1
    # pipeline measured
    s=slide()
    header(s,"04 · Post-crash care, the pipeline, measured",
           [("Numbers a standard ",False),("can act on",True)],
           lead="Each one is a lever for a WG-5 standard, toolkit entry or communication norm, none requires new legislation.",
           sect=(4,"POST-CRASH CARE"))
    tiles=[("921 of 1,026","claims pending nationally were stalled at documentation alone (RTI, July 2024)"),
           ("~60 days","typical intake latency where claims surface only via bi-monthly meetings"),
           ("~50%","of case files lack a usable family phone number, traceability is the first lever"),
           ("7 vs 11–13","court-agreed documents vs what claimants are asked for in practice"),
           ("205 → 9,813","hit-and-run claims per year, FY23 to FY26, awareness works; the pipeline is next"),
           ("5 + 22","GIC clarification queries drafted · RTIs building the public record")]
    tw=I(3.95)
    for j,(v,l) in enumerate(tiles):
        r,c=divmod(j,3)
        x=ML+c*(tw+I(0.12)); y=I(2.35)+r*I(1.55)
        rect(s,x,y,tw,I(1.4),fill=MIST,rounded=True,radius=0.08)
        text(s,x+I(0.18),y+I(0.12),tw-I(0.36),I(0.5),v,font=HEAD,size=19,bold=True,color=BRAND)
        text(s,x+I(0.18),y+I(0.62),tw-I(0.36),I(0.7),l,size=9,color=MUT,ls=1.2)
    text(s,ML,I(5.75),CW,I(0.8),
         [("The claim's other side: ",{'bold':True}),
          ("consultations with GIC and insurers on settlement practice · guidance from Justice J.R. Midha (Retd.), architect of the FaSTDAR process · working partners across MACT courts, DLSAs and legal-services clinics, Mishika Singh (Neev Foundation), Yash Agarwal (Public Policy India), Sanchit Seth (Advocate, Delhi MACT).",{'color':MUT})],size=10.5,ls=1.35)
    footer(s,wg,i,total); i+=1
    return i

# ---------------------------------------------------------------- CONTRIBUTION + CLOSE
def contribution(wg,offers,idx,total):
    s=slide()
    header(s,"05 · How we can contribute",
           [("Four concrete offers to ",False),(f"Working Group {wg}",True)],
           lead="All four are ready today, need no funding from the Board, and can begin within weeks.",
           sect=(5,"OUR CONTRIBUTION"))
    y=I(2.25)
    for i,(t,d) in enumerate(offers):
        yy=y+i*I(1.06)
        rect(s,ML,yy,I(12.09),I(0.92),fill=MIST if i%2==0 else PAPER,line=None if i%2==0 else LINE,rounded=True,radius=0.10)
        num_disc(s,ML+I(0.2),yy+I(0.22),I(0.48),i+1)
        text(s,ML+I(0.92),yy+I(0.13),I(3.9),I(0.6),t,font=HEAD,size=12.5,bold=True,color=INK,ls=1.1)
        text(s,ML+I(5.0),yy+I(0.13),I(6.9),I(0.7),d,size=10,color=MUT,ls=1.25)
    footer(s,wg,idx,total)
    return s

def close(wg,idx,total):
    s=slide(bg=BRAND)
    s.shapes.add_picture(LOGO_WHITE,ML,I(0.62),width=I(2.0))
    text(s,ML,I(2.1),I(12.1),I(1.4),f"We would be honoured to contribute\nto Working Group {wg}.",font=HEAD,size=32,bold=True,color=PAPER,ls=1.2)
    text(s,ML,I(3.85),I(11.5),I(0.6),"Our evidence, our district relationships, our technology and our expert bench are available to the Board, in whichever form is most useful.",size=12.5,color=LAVW,ls=1.4)
    hline(s,ML,I(4.72),I(5.2),color=RGBColor(0x6A,0x55,0xFF),wt=1.0)
    text(s,ML,I(4.94),I(10.8),I(0.85),
         '"We already know what is going wrong. What we need now is more responsibility, more discipline, more respect for life."',
         font=HEAD,size=14,bold=True,color=PAPER,ls=1.35,italic=True)
    text(s,ML,I(5.66),I(8),I(0.3),"MS Dhoni · Goodwill Ambassador, Crashfree India",size=10,color=LAVW)
    rows=[("globe","crashfreeindia.org"),("mail","akhtar@crashfreeindia.org  ·  helpdesk@crashfreeindia.org")]
    y=I(6.14)
    for ic,t in rows:
        icon(s,ic,ML,y,I(0.28),"#C8C0FF")
        text(s,ML+I(0.45),y-I(0.02),I(11),I(0.35),t,size=11,color=PAPER,ls=1.2)
        y=y+I(0.46)
    text(s,ML,I(7.05),I(12),I(0.3),"Crashfree India · A Cars24 commitment · Operated by Vision Zero Trust, New Delhi",size=9.5,color=LAVW)
    return s

# ================================================================ ASSEMBLY
def build_wg2():
    new_deck(); TOTAL=28
    cover(2,"Safe Roads, Speeds & Vulnerable Road Users",
          ["Expert-guided student audits that end in built fixes, 31 sites, 7 completed",
           "Technology the system uses: AI enforcement with police, public tracking dashboards",
           "Published audit reports and policy research, anchored to the IRC codes"],1,TOTAL,
          icons=("clipboard-list","cpu","file-search"))
    letter(2,
      "In our first year we audited 31 high-risk locations across 18 cities, secured 25+ written approvals from road-owning authorities, and saw 7 sites fully implemented with 6 more partially built, each tracked on a public dashboard. SATARK, our AI enforcement platform, has screened over 3,00,000 vehicles for police in Jaipur and Bengaluru and has now reached Gurugram. Four open-data platforms, the Aasha victim chatbot and hospital helpdesks complete the picture.",
      2,TOTAL)
    agenda(2,"Project Rakshak in depth","17 – 26","27 – 28",3,TOTAL)
    about(4,TOTAL,2)
    approach(5,TOTAL,2)
    why_fit(2,6,TOTAL,
        focus=[("construction","Black-spot rectification at scale","Our audit-to-implementation pipeline is running in 18 cities, the Group's rectification agenda is our core work.",BR_T,"#4A35FF"),
               ("gauge","Standards for audits & speed management","IRC-anchored audit instruments, masterclass-trained teams, and a direct line into IRC H-7 via our advisor.",GR_T,"#0A9955"),
               ("footprints","Protecting vulnerable road users","Pedestrian-first audits, the 300-rider gig-safety study, school-zone screening, evidence ready for VRU standards.",AM_T,"#E58900")],
        bring=["31 trained audit teams","Public tracking portal","District pilots: GGM · SWD · Jaipur","IRC H-7 advisory line","7 sites fully built","Expert bench on call"],
        smes=[("Dr. Richa Ahuja","IIT Kharagpur · road safety researcher","RA",False),
              ("Prof. Geetam Tiwari","TRIP Centre, IIT Delhi · IRC H-7","x_gtiwari.png",True),
              ("Abhay Damle","Ex-Joint Secretary, MoRTH","x_damle.png",True),
              ("Dipak Dash","Senior journalist, Times of India","x_dash.png",True),
              ("Sarika Panda Bhatt","Co-founder, Raahgiri Day","SP",False)])
    portfolio(7,TOTAL,2)
    satark(8,TOTAL,2)
    opendata(9,TOTAL,2)
    victim_suite(10,TOTAL,2)
    youth(11,TOTAL,2)
    ground(12,TOTAL,2)
    dhoni(13,TOTAL,2)
    partners(14,TOTAL,2)
    team(15,TOTAL,2)
    bench(16,TOTAL,2)
    nxt=wg2_body(2,TOTAL,17)
    contribution(2,[("Ready evidence for standard-setting","Site-level audit data, crash-pattern analysis and costed intervention designs across emerging hotspots and official black spots, for rectification protocols and speed-management guidance."),
                    ("A live testing ground","Active district relationships in Gurugram, South-West Delhi and Jaipur offer a ready pipeline to pilot or stress-test draft recommendations before national rollout."),
                    ("Ground-level implementation diagnostics","Granular, field-verified insight into how DRSCs and road-owning agencies actually move, meeting cadence, data use, follow-through."),
                    ("Technical bench strength on request","Our academic and expert network stands ready for drafting, review and technical input on road design, speed and VRU standards.")],nxt,TOTAL)
    close(2,28,TOTAL)
    save(os.path.join(BUILD,"CFI_NRSB_WG2_v5.pptx"))

def build_wg5():
    new_deck(); TOTAL=26
    cover(5,"Post-Crash Care, Policy Standards & State Implementation",
          ["Tools families actually use: Aasha on WhatsApp, calculator, hospital helpdesks",
           "Published policy research: Justice Unserved and the Pre-Hospital Care Primer",
           "Hand in hand with authorities: 4 district committees, Rajasthan, police MoUs"],1,TOTAL,
          icons=("bot","file-search","handshake"))
    letter(5,
      "Our post-crash work began with evidence. 'Justice Unserved', our study of the hit-and-run compensation pipeline, showed how few eligible families ever receive what the law promises, and our follow-up brief, 'Deposited But Not Delivered', found ~₹986 crore of already-awarded compensation sitting unclaimed in just five cities. Since then we have joined four District Road Safety Committees, mapped Rajasthan's scheme office-by-office with the Transport Department, and built the tools families actually use, the Aasha chatbot, a compensation calculator, hospital helpdesks that supported 100+ victims in their first four days, and plain-language guides in Hindi.",
      2,TOTAL)
    agenda(5,"Post-crash care in depth","17 – 24","25 – 26",3,TOTAL)
    about(4,TOTAL,5)
    approach(5,TOTAL,5)
    why_fit(5,6,TOTAL,
        focus=[("banknote","Clearing the compensation pipeline","Pendency is measured in years and thousands of crores. Our district work shows exactly where files stall, and how visibility clears them.",BR_T,"#4A35FF"),
               ("bot","Victim-facing standards & tools","Aasha, the calculator, guides and helpdesks, working models for the citizen-facing standards WG-5 will set.",GR_T,"#0A9955"),
               ("stethoscope","EMS & trauma-care evidence","The Pre-Hospital Care Primer benchmarks ERSS-112 and documents state innovations, a ready baseline for care standards.",TE_T,"#0E8A8A")],
        bring=["Justice Unserved evidence","Rajasthan portal blueprint","4 DRSC working seats","Legal bench: MACT + DLSA","Aasha + calculator live","Trauma-ward helpdesks"],
        smes=[("Justice J.R. Midha","Retd., Delhi HC · MACT process architect","x_pp_midha.png",True),
              ("Piyush Tewari","SaveLIFE Foundation · Good Samaritan Law","PT",False),
              ("Dr. Sushma Sagar","Prof. & In-charge, Trauma Surgery, JPN Apex Trauma Centre, AIIMS","x_sagar.png",True),
              ("Dr. Maya Tandon","Sahayta Trust · trauma-response pioneer","x_tandon.png",True),
              ("Mishika Singh","Neev Foundation · legal helpdesks","x_pp_mishika.png",True)])
    portfolio(7,TOTAL,5)
    satark(8,TOTAL,5)
    opendata(9,TOTAL,5)
    victim_suite(10,TOTAL,5)
    youth(11,TOTAL,5)
    ground(12,TOTAL,5)
    dhoni(13,TOTAL,5)
    partners(14,TOTAL,5)
    team(15,TOTAL,5)
    bench(16,TOTAL,5)
    nxt=wg5_body(5,TOTAL,17)
    contribution(5,[("A victim-side evidence base","'Justice Unserved', 'Deposited But Not Delivered', 120+ victim and family interactions, and file-level pipeline data showing precisely where eligible families drop out."),
                    ("A district toolkit, drawn from practice","Working DRSC integration experience, agendas, file digitisation, fellow placement, ready to be codified into the Group's district toolkit."),
                    ("A reusable state portal blueprint","The Rajasthan case-management design, guided filing, stage-wise visibility, single-pass clarification, offered as a template any state can adapt."),
                    ("Standards input from the claimant's side","Document standards (the court-agreed 7), communication norms and timeline benchmarks, grounded in what families actually experience.")],nxt,TOTAL)
    close(5,26,TOTAL)
    save(os.path.join(BUILD,"CFI_NRSB_WG5_v5.pptx"))

if __name__=="__main__":
    build_wg2()
    build_wg5()

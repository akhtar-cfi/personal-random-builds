# NRSB EoI decks v2 — WG-2 & WG-5. White-paper style, letter-first, running agenda, photo-forward.
import os
from nrsb2_style import *
from pptx.util import Inches, Pt, Emu
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

I=Inches
LTR=os.path.join(V3,"letters")

# ---------------------------------------------------------------- S1 COVER
def cover(wg, name_l1, name_l2, chips_, films, idx, total):
    s=slide()
    s.shapes.add_picture(LOGO_BLUE,ML,I(0.5),width=I(1.85))
    text(s,SW-MR-I(3.5),I(0.55),I(3.5),I(0.3),"AUGUST 2026  ·  NEW DELHI",font=HEAD,size=9,bold=True,color=MUT,tracking=1.8,align=PP_ALIGN.RIGHT)
    text(s,ML,I(1.42),I(11),I(0.3),"EXPRESSION OF INTEREST  ·  NATIONAL ROAD SAFETY BOARD",font=HEAD,size=10.5,bold=True,color=BRAND,tracking=2.4)
    text(s,ML,I(1.85),I(12.1),I(0.65),f"Working Group {wg}: {name_l1}",font=HEAD,size=30,bold=True,color=INK,ls=1.05)
    text(s,ML,I(2.44),I(12.1),I(0.62),name_l2,font=HEAD,size=30,bold=True,color=BRAND,ls=1.05)
    text(s,ML,I(3.18),I(11.6),I(0.62),
         "Submitted by Crashfree India (Vision Zero Trust) — a technology-led road safety nonprofit backed by Cars24,\nworking with public authorities across 18 cities.",
         size=12,color=MUT,ls=1.35)
    cw=I(2.92); gap=I(0.135); y=I(4.05)
    for i,(v,l) in enumerate(chips_):
        x=ML+i*(cw+gap)
        rect(s,x,y,cw,I(0.78),fill=MIST,rounded=True,radius=0.16)
        text(s,x+I(0.16),y+I(0.09),cw-I(0.3),I(0.4),v,font=HEAD,size=16,bold=True,color=BRAND,ls=1.0)
        text(s,x+I(0.16),y+I(0.43),cw-I(0.3),I(0.3),l,size=9,color=MUT,ls=1.0)
    pw=I(2.92); ph_=I(1.72); y=I(5.05)
    for i,f in enumerate(films):
        photo(s,f,ML+i*(pw+gap),y,pw,ph_,fill=True)
    text(s,ML,I(6.95),I(9.5),I(0.3),f"Submitted to the Chairperson and Members, Working Group {wg}, National Road Safety Board",size=9.5,color=MUT)
    text(s,SW-MR-I(2.6),I(6.95),I(2.6),I(0.3),"crashfreeindia.org",font=HEAD,size=9.5,bold=True,color=BRAND,align=PP_ALIGN.RIGHT)
    return s

# ---------------------------------------------------------------- S2 LETTER
def letter(wg,p3, idx,total):
    s=slide()
    header(s,"Before the slides","",[("A letter to the Working Group",False)] and [("A letter to the ",False),("Working Group",True)],sect=None) if False else None
    text(s,ML,I(0.30),I(8),I(0.24),"BEFORE THE SLIDES",font=HEAD,size=9,bold=True,color=BRAND,tracking=2.2)
    hline(s,ML,I(0.62),I(0.55),color=BRAND,wt=2.0)
    text(s,ML,I(0.76),I(12),I(0.5),[("A letter to the ",{'color':INK}),("Working Group",{'color':BRAND})],font=HEAD,size=22.5,bold=True,ls=1.1)
    x=ML+I(0.95); w=I(10.2); y=I(1.5)
    rect(s,x,y,w,I(5.42),fill=PAPER,line=LINE,lw=1.2)
    rect(s,x,y,w,I(0.06),fill=BRAND)
    s.shapes.add_picture(LOGO_BLUE,x+I(0.5),y+I(0.32),width=I(1.35))
    text(s,x+w-I(3.2),y+I(0.36),I(2.7),I(0.3),"New Delhi · August 2026",size=9.5,color=MUT,align=PP_ALIGN.RIGHT)
    body=(f"Respected Chairperson and Members of Working Group {wg},\n"
      "Crashfree India is a young road safety nonprofit — registered as the Vision Zero Trust, co-founded with the Indian Road Safety Council, and backed by a three-year, US$3 million commitment from Cars24. We work alongside public authorities: our student teams audit dangerous locations under senior experts, our technology helps police and administrators see their own pipelines, and our support tools stand with families after a crash.\n"
      +p3+"\n"
      "The pages that follow introduce the organisation briefly, then set out the work most relevant to this Working Group in the detail its mandate deserves. Everything shown is running today, is public, and is offered to the Board without cost. We would be honoured to contribute.")
    tb=text(s,x+I(0.5),y+I(0.95),w-I(1.0),I(3.6),body,size=10.8,color=INK,ls=1.32)
    for p in tb.text_frame.paragraphs: p.space_after=Pt(7)
    text(s,x+I(0.5),y+I(4.62),w-I(1.0),I(0.3),"Respectfully,",size=10.8,color=INK)
    text(s,x+I(0.5),y+I(4.92),w-I(1.0),I(0.3),"Akhtar Hussain",font=HEAD,size=11.5,bold=True,color=INK)
    text(s,x+I(0.5),y+I(5.16),w-I(1.0),I(0.26),"Mission Lead, Crashfree India  ·  akhtar@crashfreeindia.org  ·  crashfreeindia.org",size=9.5,color=MUT)
    return s

# ---------------------------------------------------------------- S3 AGENDA
def agenda(wg, sect4, idx,total):
    s=slide()
    text(s,ML,I(0.30),I(8),I(0.24),"HOW THIS DECK IS ORGANISED",font=HEAD,size=9,bold=True,color=BRAND,tracking=2.2)
    hline(s,ML,I(0.62),I(0.55),color=BRAND,wt=2.0)
    text(s,ML,I(0.76),I(12),I(0.5),[("Five sections, ",{'color':INK}),("three minutes",{'color':BRAND}),(" to skim",{'color':INK})],font=HEAD,size=22.5,bold=True,ls=1.1)
    rows=[("building-2","About Crashfree India","Who we are, how we are set up, and the principles we work by.","04"),
          ("layers","What we have built","Every public-facing programme — audits, enforcement tech, victim support, open data, youth, campaigns.","05 – 11"),
          ("users","Our people","Trustees, Board of Advisors, and the expert bench behind the work.","12"),
          ("target",sect4,"The deep dive matched to this Working Group's mandate — evidence, method, and results.","13 – 21"),
          ("handshake","How we can contribute","Four concrete, no-cost offers to the Working Group.","22 – 23")]
    y=I(1.72)
    for i,(ic,t,d,pg) in enumerate(rows):
        yy=y+i*I(1.02)
        rect(s,ML,yy,CW,I(0.88),fill=MIST if i%2==0 else PAPER,line=LINE if i%2 else None,rounded=True,radius=0.10)
        num_disc(s,ML+I(0.22),yy+I(0.2),I(0.48),i+1)
        icon_disc(s,ic,ML+I(0.95),yy+I(0.2),I(0.48),BR_T,"#4A35FF")
        text(s,ML+I(1.68),yy+I(0.13),I(3.6),I(0.4),t,font=HEAD,size=13.5,bold=True,color=INK,ls=1.0)
        text(s,ML+I(1.68),yy+I(0.46),I(7.6),I(0.35),d,size=10,color=MUT,ls=1.15)
        text(s,SW-MR-I(1.7),yy+I(0.24),I(1.45),I(0.4),pg,font=HEAD,size=12,bold=True,color=BRAND,align=PP_ALIGN.RIGHT)
    return s

# ---------------------------------------------------------------- S4 ABOUT
def about(idx,total,wg):
    s=slide()
    header(s,"01 · About us",[("Crashfree India: a nonprofit that adds ",False),("capacity",True),(" to road safety work",False)],
           lead="Registered as the Vision Zero Trust · Co-founded by Cars24 and the Indian Road Safety Council · Working since June 2025 · New Delhi",
           sect=(1,"ABOUT US"))
    rows=[("search-check","Evidence first","Structured field audits, file reviews and research to official standards — not opinion.",GR_T,"#0A9955"),
          ("landmark","Institutional collaboration","We work through PWDs, NHAI, transport departments, police and District Road Safety Committees.",BR_T,"#4A35FF"),
          ("users","Youth-led capacity","Trained student teams from IITs, NITs and SPAs add the auditing hands the system needs.",AM_T,"#E58900"),
          ("monitor-check","Technology for follow-through","Public dashboards track every recommendation from submission to completion.",TE_T,"#0E8A8A")]
    y=I(2.2)
    for i,(ic,t,d,tint,col) in enumerate(rows):
        irow(s,ML,y+i*I(0.82),I(7.6),ic,t,d,tint,col)
    rect(s,ML,I(5.65),I(7.55),I(0.92),fill=BR_T,rounded=True,radius=0.16)
    text(s,ML+I(0.25),I(5.72),I(7.1),I(0.8),
         [("Backed by a US$3 million, three-year commitment from Cars24 ",{'bold':True,'color':BRAND}),
          ("— programmes, not overheads, receive 71% of the budget.",{'color':BRAND})],size=11.5,ls=1.3)
    photo(s,a5("cfi_map_dots.png"),I(8.6),I(2.15),I(4.05),caption="Where we work today — 18 cities, north to south.")
    footer(s,wg,idx,total)
    return s

# ---------------------------------------------------------------- S5 PORTFOLIO
def portfolio(idx,total,wg):
    s=slide()
    header(s,"02 · What we have built",[("Six lines of work, ",False),("one connected system",True)],
           lead="Audits create data · data supports policy · policy guides the field. Everything below is live today.",
           sect=(2,"WHAT WE HAVE BUILT"))
    tiles=[("Project Rakshak","Student-led road audits, fixed with authorities","31 sites · 15 under implementation",a5("implementation_work.jpg")),
           ("SATARK enforcement","AI support that helps police find high-risk vehicles","3,00,000+ vehicles screened",a5("satark_billboard.jpg")),
           ("Victim support","Aasha chatbot, calculator, hospital helpdesks","100+ victims helped in first 4 days",a5("ph_helpdesk_desk.jpg")),
           ("Open public data","Four self-updating data platforms, free to use","36 states & 50 cities covered",a5("sctracker.png")),
           ("Youth & policy","NextMile ideathon and national dialogue series","2,000+ participants engaged",a5("ph_ideathon_winners.jpg")),
           ("Public campaigns","Road Safety Month with police & schools; MS Dhoni","1M+ citizens reached",a5("ph_police_rally.jpg"))]
    tw=I(3.95); th=I(2.32); gx=I(0.12); gy=I(0.16)
    for i,(t,d,st,img) in enumerate(tiles):
        r,c=divmod(i,3)
        x=ML+c*(tw+gx); y=I(2.12)+r*(th+gy)
        rect(s,x,y,tw,th,fill=PAPER,line=LINE,rounded=True,radius=0.06)
        photo(s,img,x,y,tw,I(1.28),fill=True,border=False)
        rect(s,x,y,tw,I(1.28),fill=None,line=LINE,lw=1.0)
        text(s,x+I(0.14),y+I(1.36),tw-I(0.28),I(0.3),t,font=HEAD,size=11.5,bold=True,color=INK,ls=1.0)
        text(s,x+I(0.14),y+I(1.62),tw-I(0.28),I(0.35),d,size=9,color=MUT,ls=1.12)
        text(s,x+I(0.14),y+I(2.02),tw-I(0.28),I(0.26),st,font=HEAD,size=9,bold=True,color=BRAND,ls=1.0)
    footer(s,wg,idx,total)
    return s

# ---------------------------------------------------------------- S6 SATARK
def satark(idx,total,wg):
    s=slide()
    header(s,"02 · What we have built — enforcement technology",
           [("SATARK: AI that helps police stop ",False),("the right vehicle",True)],
           lead="Built with Cars24 engineers. Reads number plates, checks government records, and alerts officers to repeat offenders — in real time.",
           sect=(2,"WHAT WE HAVE BUILT"))
    photo(s,a5("satark_billboard.jpg"),ML,I(2.15),I(4.35),I(2.65),fill=True,caption="Rambagh Circle, Jaipur — live plate, pending challans and dues on a public billboard.")
    photo(s,a5("satark_officer_app.jpg"),I(5.15),I(2.15),I(2.0),I(2.65),fill=True,caption="Officer view — pending challans,\nRC & compliance status.")
    xs=I(7.42); ws=I(2.55)
    stat(s,xs,I(2.1),ws,"3,00,000+","vehicles screened",vsize=21)
    stat(s,xs+I(2.68),I(2.1),ws,"₹30 Cr+","pending challan value identified",vsize=21)
    stat(s,xs,I(3.08),ws,"350+","high-risk vehicles intercepted",vsize=21)
    stat(s,xs+I(2.68),I(3.08),ws,"70,019","vehicles found with pending challans",vsize=21)
    chip(s,xs,I(4.12),I(2.45),I(0.42),"LIVE · Jaipur & Bengaluru",fill=GR_T,color=GREEN,size=9.5)
    chip(s,xs+I(2.58),I(4.12),I(1.75),I(0.42),"NEW · Gurugram",fill=BR_T,color=BRAND,size=9.5)
    text(s,xs,I(4.66),I(5.2),I(0.3),"Bengaluru's Trinity Circle billboard was India's first — covered by Deccan Herald and national press. Pune and Ahmedabad are next.",size=9.5,color=MUT,ls=1.25)
    steps=[("camera","ANPR camera"),("scan-line","Plate read"),("database","Records check"),("alert-triangle","Risk flag"),("bell-ring","Officer alert"),("monitor","Billboard"),("hand","Interception"),("shield-check","Enforcement")]
    y=I(5.62); n=len(steps); cw=CW/n
    hline(s,ML+I(0.4),y+I(0.24),CW-I(0.8),color=LINE,wt=1.0)
    for i,(ic,lb) in enumerate(steps):
        x=ML+Emu(int(cw*i))
        icon_disc(s,ic,x+Emu(int(cw/2))-I(0.24),y,I(0.48),MIST,"#4A35FF")
        text(s,x,y+I(0.56),Emu(int(cw)),I(0.3),lb,size=8.5,color=MUT,align=PP_ALIGN.CENTER,ls=1.0)
    footer(s,wg,idx,total)
    return s

# ---------------------------------------------------------------- S7 OPEN DATA
def opendata(idx,total,wg):
    s=slide()
    header(s,"02 · What we have built — open public data",
           [("Public data platforms any authority can use, ",False),("free",True)],
           lead="Built and maintained by our team; self-updating; no login, no fee. Shown live below.",
           sect=(2,"WHAT WE HAVE BUILT"))
    photo(s,a5("sctracker.png"),ML,I(2.12),I(6.1),I(2.9),fill=True,
          caption="Supreme Court Litigation Tracker — live: 20 systemic cases, 191 orders indexed, 30 precedent judgments (1 Aug 2026).")
    photo(s,a5("suraksha_cards.png"),ML,I(5.62),I(6.1),I(1.0),fill=True,border=True)
    text(s,ML,I(6.68),I(6.4),I(0.3),"Suraksha Mitra & Sadak Suraksha Suchak — citizen hazard reporting in Hindi (50+ hazards in the first 20 days).",size=8.5,color=MUT,ls=1.1)
    photo(s,a5("resources_hub.jpg"),I(7.05),I(2.12),I(5.65),I(2.45),fill=True,
          caption="Road Safety Resources Hub — primers, data portals and guides in one place.")
    rows=[("database","Road Defect Repository","146 districts · 13 languages — defect news, mapped publicly.",TE_T,"#0E8A8A"),
          ("landmark","Parliament tracker","1,423 road-safety questions indexed across the Lok Sabha & Rajya Sabha.",BR_T,"#4A35FF"),
          ("bar-chart-3","Crash Data Dashboard","MoRTH statistics made usable — 36 states, 50 cities, open licence.",AM_T,"#E58900")]
    y=I(5.08)
    for i,(ic,t,d,tint,col) in enumerate(rows):
        icon_disc(s,ic,I(7.05),y+i*I(0.6),I(0.4),tint,col)
        text(s,I(7.62),y+i*I(0.6)-I(0.02),I(2.2),I(0.4),t,font=HEAD,size=10.5,bold=True,color=INK,ls=1.0)
        text(s,I(9.55),y+i*I(0.6)-I(0.02),I(3.2),I(0.55),d,size=9,color=MUT,ls=1.15)
    footer(s,wg,idx,total)
    return s

# ---------------------------------------------------------------- S8 VICTIM SUITE
def victim_suite(idx,total,wg):
    s=slide()
    header(s,"02 · What we have built — victim support",
           [("Help a family can actually use, ",False),("in their language",True)],
           lead="From the first hours after a crash to the final compensation order — on WhatsApp, on paper, and in person.",
           sect=(2,"WHAT WE HAVE BUILT"))
    labels=["Day one after FIR","Document capture","Live case status"]
    for i in range(3):
        x=ML+i*I(1.72)
        photo(s,a5(f"wa_phone{i+1}.png"),x,I(2.1),I(1.58),border=False)
        text(s,x,I(4.52),I(1.6),I(0.3),labels[i],font=HEAD,size=8.5,bold=True,color=INK,align=PP_ALIGN.CENTER)
    text(s,ML,I(4.88),I(5.1),I(0.5),"Aasha — our 24/7 multilingual AI companion. The family needs no app and no portal; everything runs on WhatsApp and voice, in Hindi.",size=9.5,color=MUT,ls=1.25)
    rows=[("bot","Aasha chatbot","Step-by-step guidance on rights, schemes and documents — 24/7, multilingual.",BR_T,"#4A35FF"),
          ("calculator","Compensation Calculator","Free instant estimates on Supreme Court principles (Sarla Verma, Pranay Sethi).",TE_T,"#0E8A8A"),
          ("life-buoy","Hospital helpdesks","Legal desks in trauma wards — 100+ victims supported in the first four days.",GR_T,"#0A9955"),
          ("book-open","Plain-language education","Comics and Hindi guides on all three compensation routes, NALSA 15100 and the Cashless Treatment Scheme 2025.",AM_T,"#E58900")]
    y=I(2.1)
    for i,(ic,t,d,tint,col) in enumerate(rows):
        icon_disc(s,ic,I(5.75),y+i*I(0.78),I(0.4),tint,col)
        text(s,I(6.32),y+i*I(0.78)-I(0.02),I(1.95),I(0.55),t,font=HEAD,size=11,bold=True,color=INK,ls=1.05)
        text(s,I(8.3),y+i*I(0.78)-I(0.02),I(2.15),I(0.75),d,size=9,color=MUT,ls=1.18)
    photo(s,a3("guide_p1.png"),I(10.7),I(2.1),I(2.02),caption="Hindi legal-rights guide — used in\nhospitals & police stations.")
    footer(s,wg,idx,total)
    return s

# ---------------------------------------------------------------- S9 YOUTH & POLICY
def youth(idx,total,wg):
    s=slide()
    header(s,"02 · What we have built — youth & policy",
           [("Young talent and senior experts, ",False),("working the same problem",True)],
           lead="A steady pipeline of engineers and policy minds — so road safety work never runs out of hands.",
           sect=(2,"WHAT WE HAVE BUILT"))
    photo(s,a5("ph_ideathon_winners.jpg"),ML,I(2.12),I(4.05),I(2.5),fill=True,
          caption="NextMile: Road Safety Policy Ideathon — grand finale, 28 Sep 2025, New Delhi.")
    xs=ML; y=I(5.3)
    for i,(v,l) in enumerate([("2,000+","participants"),("250+","concept notes"),("700+","teams"),("10","finalist teams")]):
        stat(s,xs+i*I(1.05),y,I(1.0),v,l,vsize=14,lsize=8)
    photo(s,a5("ph_vision_wall.jpg"),I(4.85),I(2.12),I(3.7),I(2.5),fill=True,
          caption="Vision Wall 2040 — participants write the road-safety future they want.")
    text(s,I(4.85),I(5.28),I(3.7),I(0.8),"Mentors and evaluators came from the Government of Rajasthan, NIUA, OMI, NASSCOM and CSEP. Winning tracks now feed our audit and research pipeline.",size=9.5,color=MUT,ls=1.25)
    x3=I(9.0)
    rows=[("mic","National Road Safety Dialogue Series","200+ live attendees; speakers from MoRTH, CIRT, AIIMS Trauma Centre, CSIR-CRRI and ARAI.",BR_T,"#4A35FF"),
          ("message-square","Three sessions so far","Bus safety · Delivery rider safety · Good Samaritan law & the Cashless Treatment Scheme.",TE_T,"#0E8A8A"),
          ("monitor-play","Public YouTube channel","Session recordings, victim-education videos and explainers — free to reuse in trainings.",RD_T,"#E11900")]
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

# ---------------------------------------------------------------- S10 GROUND CAMPAIGNS
def ground(idx,total,wg):
    s=slide()
    header(s,"02 · What we have built — on the ground",
           [("Road Safety Month 2026, run ",False),("with the system",True)],
           lead="With district police, schools, hospitals and delivery platforms — in Hindi and local languages.",
           sect=(2,"WHAT WE HAVE BUILT"))
    photo(s,a5("ph_police_rally.jpg"),ML,I(2.12),I(4.7),I(3.55),fill=True,
          caption="National Road Safety Month rally — on the road with district traffic police, Jan 2026.")
    grid=[("ph_stall.jpg","CFI stall at a government office"),
          ("ph_police_station.jpg","Materials briefing with police staff"),
          ("ph_school_kids.jpg","School programme with certificates"),
          ("ph_gig_riders.jpg","Delivery-rider outreach — Swiggy & Instamart")]
    for i,(f,cap) in enumerate(grid):
        r,c=divmod(i,2)
        x=I(5.55)+c*I(3.65); y=I(2.12)+r*I(2.15)
        photo(s,a5(f),x,y,I(3.55),I(1.72),fill=True,caption=cap)
    rect(s,ML,I(6.15),I(4.7),I(0.62),fill=GR_T,rounded=True,radius=0.16)
    text(s,ML+I(0.2),I(6.24),I(4.4),I(0.5),[("1M+ citizens reached ",{'bold':True,'color':GREEN}),("across campaigns in year one.",{'color':GREEN})],size=10.5,ls=1.2)
    footer(s,wg,idx,total)
    return s

# ---------------------------------------------------------------- S11 DHONI + RECOGNITION
def dhoni(idx,total,wg):
    s=slide()
    header(s,"02 · What we have built — public voice",
           [("MS Dhoni carries the message; ",False),("the ecosystem engages",True)],
           sect=(2,"WHAT WE HAVE BUILT"))
    photo(s,a5("ph_dhoni_white.jpg"),ML,I(1.95),I(2.9),I(3.75),fill=True,
          caption="MS Dhoni — Goodwill Ambassador, announced April 2026.")
    rect(s,I(3.85),I(1.95),I(3.6),I(3.75),fill=MIST,rounded=True,radius=0.08)
    text(s,I(4.1),I(2.25),I(3.1),I(2.2),
         '"We already know what is going wrong. What we need now is more responsibility, more discipline, more respect for life."',
         font=HEAD,size=14,bold=True,color=INK,ls=1.35,italic=True)
    text(s,I(4.1),I(4.85),I(3.1),I(0.6),"MS Dhoni, at the National Road Safety\nImplementation Forum, IIT Delhi",size=9.5,color=MUT,ls=1.25)
    photo(s,a3("comp_image6.jpeg"),I(7.75),I(1.95),I(4.95),I(2.78),fill=True,
          caption="National Road Safety Implementation Forum, IIT Delhi — 60+ experts including MoRTH, WHO, UNICEF, iRAP and CSIR-CRRI.")
    text(s,I(7.75),I(5.25),I(4.95),I(0.3),"COVERED IN NATIONAL PRESS",font=HEAD,size=8.5,bold=True,color=MUT,tracking=1.8)
    press=["Deccan Herald","Economic Times","Fortune India","IndiaSpend","Scroll.in","The Wire","Times of India","Business Standard"]
    x=I(7.75); y=I(5.55)
    for i,p in enumerate(press):
        c=i%2; r=i//2
        chip(s,x+c*I(2.55),y+r*I(0.42),I(2.45),I(0.34),p,fill=PAPER,color=INK,size=8.5,bold=False,line=LINE)
    text(s,ML,I(6.05),I(7.0),I(0.55),"Dhoni's voice powers 'Be a Rakshak', school-zone safety and compensation-awareness campaigns.",size=10,color=MUT,ls=1.3)
    footer(s,wg,idx,total)
    return s

# ---------------------------------------------------------------- S12 PEOPLE
def people(idx,total,wg):
    s=slide()
    header(s,"03 · Our people",
           [("Advised by the people who ",False),("built India's road safety practice",True)],
           sect=(3,"OUR PEOPLE"))
    y=I(1.7)
    rect(s,ML,y,I(6.0),I(1.06),fill=MIST,rounded=True,radius=0.12)
    ph=photo(s,os.path.join(V3,"heads","gtiwari.png"),ML+I(0.14),y+I(0.14),I(0.78),I(0.78),fill=True,border=False)
    text(s,ML+I(1.06),y+I(0.14),I(4.9),I(0.35),"Prof. Geetam Tiwari — Board of Advisors",font=HEAD,size=11,bold=True,color=INK)
    text(s,ML+I(1.06),y+I(0.46),I(4.9),I(0.55),"Professor Emerita & Chair, TRIP Centre, IIT Delhi · Member, IRC H-7 Committee on Road Safety Audit",size=9,color=MUT,ls=1.2)
    x2=I(6.85)
    rect(s,x2,y,I(5.85),I(1.06),fill=MIST,rounded=True,radius=0.12)
    circle(s,x2+I(0.14),y+I(0.14),I(0.78),BR_T)
    text(s,x2+I(0.14),y+I(0.12),I(0.78),I(0.78),"PT",font=HEAD,size=15,bold=True,color=BRAND,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    text(s,x2+I(1.06),y+I(0.14),I(4.7),I(0.35),"Piyush Tewari — Board of Advisors",font=HEAD,size=11,bold=True,color=INK)
    text(s,x2+I(1.06),y+I(0.46),I(4.7),I(0.55),"Founder & CEO, SaveLIFE Foundation · Architect of the Good Samaritan Law · Zero-Fatality Corridors",size=9,color=MUT,ls=1.2)
    text(s,ML,I(3.0),I(11),I(0.26),"THE EXPERT BENCH AROUND OUR WORK — JURY, MENTORS & REVIEWERS",font=HEAD,size=8.5,bold=True,color=MUT,tracking=1.6)
    heads=[("midha","Justice J.R. Midha","Delhi High Court (Retd.)"),("damle","Abhay Damle","Ex-JS, MoRTH"),
           ("dange","Vaibhav Dange","Ex-Advisor, MoRTH"),("tandon","Dr. Maya Tandon","Sahayta Trust"),
           ("ratnam","R. Venkat Ratnam","Government of Punjab"),("asrivastava","Akhilesh Srivastava","ITS India · IRF"),
           ("gsingh","Gautam Singh","SaveLIFE Foundation"),("raman","Aishwarya Raman","OMI Foundation"),
           ("nkumar","Neeraj Kumar","Tata AIG"),("pandey","R.S. Pandey","FICCI Road Safety"),
           ("dash","Dipak K. Dash","Times of India")]
    cw=I(2.04); y0=I(3.32)
    for i,(f,n,o) in enumerate(heads):
        r,c=divmod(i,6)
        x=ML+c*cw; yy=y0+r*I(1.35)
        photo(s,os.path.join(V3,"heads",f+".png"),x+I(0.62),yy,I(0.72),I(0.72),fill=True,border=False)
        text(s,x,yy+I(0.76),cw-I(0.1),I(0.3),n,font=HEAD,size=8.5,bold=True,color=INK,align=PP_ALIGN.CENTER,ls=1.0)
        text(s,x,yy+I(0.97),cw-I(0.1),I(0.3),o,size=7.5,color=MUT,align=PP_ALIGN.CENTER,ls=1.0)
    rect(s,ML,I(6.15),CW,I(0.66),fill=MIST,rounded=True,radius=0.14)
    text(s,ML+I(0.25),I(6.26),CW-I(0.5),I(0.45),
         [("Trustees: ",{'bold':True}),("Amar Srivastava (President · Founder, IRSC) · Deepanshu Gupta (Managing Trustee) · Gajendra Jangid (Co-founder, Cars24)   ",{'color':MUT}),
          ("Team: ",{'bold':True}),("IIT Delhi, NALSAR, TISS & HKUST alumni · 75+ engineering interns · 31 student audit teams",{'color':MUT})],size=9.5,ls=1.2)
    footer(s,wg,idx,total)
    return s

# ---------------------------------------------------------------- CONTRIBUTION + CLOSE
def contribution(wg,offers,idx,total,sect4):
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
    text(s,ML,I(2.5),I(11.5),I(1.4),f"We would be honoured to contribute\nto Working Group {wg}.",font=HEAD,size=30,bold=True,color=PAPER,ls=1.2)
    text(s,ML,I(4.15),I(10.5),I(0.7),"Our evidence, our district relationships, our technology and our expert bench are available to the Board — in whichever form is most useful.",size=12.5,color=LAVW,ls=1.4)
    rows=[("globe","crashfreeindia.org"),("mail","akhtar@crashfreeindia.org  ·  helpdesk@crashfreeindia.org"),("layout-dashboard","Live portals: Rakshak dashboard · SC litigation tracker · crash data · defect repository")]
    y=I(5.15)
    for ic,t in rows:
        icon(s,ic,ML,y,I(0.3),"#C8C0FF")
        text(s,ML+I(0.5),y-I(0.02),I(11),I(0.35),t,size=11.5,color=PAPER,ls=1.2)
        y=y+I(0.52)
    text(s,ML,I(7.02),I(12),I(0.3),"Crashfree India · A Cars24 commitment · Operated by Vision Zero Trust, New Delhi",size=9.5,color=LAVW)
    return s

# ================================================================ WG-2 BODY
def wg2_body(wg,total,start):
    i=start
    # S13 explainer
    s=slide()
    header(s,"04 · Project Rakshak — what it is",
           [("Project Rakshak, ",False),("in one sentence",True)],sect=(4,"PROJECT RAKSHAK"))
    text(s,ML,I(1.72),I(12.0),I(0.85),
         "Trained student teams, guided by senior road-safety experts, audit dangerous road locations — and Crashfree India walks each recommended fix through the road-owning authority until it is built.",
         font=HEAD,size=15.5,bold=False,color=INK,ls=1.35)
    cards=[("clipboard-list","Students audit","Teams from IITs, NITs and SPAs collect data on-site: traffic, conflicts, 900+ stakeholder surveys.",a5("guntur_junction.jpg")),
           ("badge-check","Experts verify","Mentors anchor every audit to IRC codes and MoRTH checklists before anything is proposed.",a5("ph_jury_room.jpg")),
           ("hard-hat","Authorities build","The fix goes to the PWD, corporation or NHAI in its own format — and we track it to completion.",a5("implementation_work.jpg"))]
    tw=I(3.95); gx=I(0.12)
    for j,(ic,t,d,img) in enumerate(cards):
        x=ML+j*(tw+gx); y=I(2.75)
        rect(s,x,y,tw,I(3.3),fill=PAPER,line=LINE,rounded=True,radius=0.06)
        photo(s,img,x,y,tw,I(1.55),fill=True,border=False)
        rect(s,x,y,tw,I(1.55),fill=None,line=LINE,lw=1.0)
        icon_disc(s,ic,x+I(0.15),y+I(1.7),I(0.42),BR_T,"#4A35FF")
        text(s,x+I(0.7),y+I(1.76),tw-I(0.85),I(0.35),t,font=HEAD,size=12.5,bold=True,color=INK)
        text(s,x+I(0.15),y+I(2.22),tw-I(0.3),I(1.0),d,size=9.5,color=MUT,ls=1.25)
    text(s,ML,I(6.3),CW,I(0.35),
         [("Four phases each cohort: ",{'bold':True}),("Research & problem identification  →  Stakeholder engagement & audits  →  Analysis & costed solutions  →  Reporting & authority engagement",{'color':MUT})],size=10,ls=1.2)
    footer(s,wg,i,total); i+=1
    # S14 gap
    s=slide()
    header(s,"04 · Project Rakshak — why it matters to WG-2",
           [("Identification has outpaced rectification — ",False),("capacity is the constraint",True)],
           lead="The knowledge exists; the pipeline that turns identified risk into completed engineering needs more trained hands.",
           sect=(4,"PROJECT RAKSHAK"))
    stat(s,ML,I(2.3),I(3.4),"13,795","black spots identified nationally (MoRTH)",vsize=30,card=True,h=I(1.3))
    stat(s,ML+I(3.55),I(2.3),I(3.4),"5,036","permanently rectified so far (Parliamentary Standing Committee, 2024)",vsize=30,card=True,h=I(1.3))
    stat(s,ML+I(7.1),I(2.3),I(3.4),"44","certified Road Safety Auditors on the national registry (July 2026)",vsize=30,card=True,h=I(1.3),color=AMBER)
    text(s,ML,I(3.95),I(7.3),I(1.3),
         "Low-cost engineering measures — raised crossings, traffic calming, lighting, safer intersections — reduce crashes by 20–80% where applied (iRAP & PIARC evidence). What limits progress is steady, supervised auditing capacity and follow-up, working under the road-owning authority.",
         size=11,color=INK,ls=1.4)
    rect(s,ML,I(5.5),I(7.3),I(0.95),fill=BR_T,rounded=True,radius=0.12)
    text(s,ML+I(0.22),I(5.62),I(6.9),I(0.75),
         [("Project Rakshak was designed for precisely this constraint: ",{'bold':True,'color':BRAND}),
          ("trained auditing capacity that supports road-owning agencies — and tracks every fix to completion.",{'color':BRAND})],size=10.5,ls=1.3)
    photo(s,a3("iv_guntur_drainage.png"),I(8.35),I(3.95),I(4.35),I(2.5),fill=True,
          caption="Guntur, Andhra Pradesh — drainage correction underway after audit.")
    footer(s,wg,i,total); i+=1
    # S15 footprint
    s=slide()
    header(s,"04 · Project Rakshak — year one",
           [("Cohort 1: a ",False),("national footprint",True),(" in the first year",False)],sect=(4,"PROJECT RAKSHAK"))
    fun=[("120+","locations screened",MIST,INK),("31","sites audited — 11 official black spots",MIST,INK),
         ("25+","written authority approvals",MIST,INK),("15","implementations underway",BRAND,PAPER)]
    y=I(2.15)
    for j,(v,l,fill,tc) in enumerate(fun):
        x=ML+j*I(2.1)
        rect(s,x,y,I(1.95),I(1.25),fill=fill,rounded=True,radius=0.12)
        text(s,x+I(0.14),y+I(0.12),I(1.7),I(0.55),v,font=HEAD,size=24,bold=True,color=BRAND if fill==MIST else PAPER,ls=1.0)
        text(s,x+I(0.14),y+I(0.62),I(1.7),I(0.55),l,size=8.5,color=MUT if fill==MIST else PAPER,ls=1.1)
        if j<3: text(s,x+I(1.93),y+I(0.4),I(0.2),I(0.4),"→",size=14,color=MUT)
    text(s,ML,I(3.62),I(8.2),I(0.3),"31 student teams · 20 institutions including nine IITs · 900+ stakeholder surveys · guided by 8 mentors and independent evaluators",size=10,color=MUT,ls=1.3)
    text(s,ML,I(4.1),I(8.2),I(0.75),
         "North: Ropar, Dehradun, Roorkee, Delhi, Lucknow, Varanasi · East: Guwahati, Durgapur · West & Central: Indore, Mumbai, Surat · South: Vijayawada, Guntur, Kozhikode, Chennai — among 18 cities.",size=10,color=MUT,ls=1.35)
    rect(s,ML,I(5.15),I(8.2),I(1.3),fill=AM_T,rounded=True,radius=0.10)
    text(s,ML+I(0.22),I(5.3),I(7.8),I(1.0),
         [("Estimated 20–50% crash reduction at treated sites once complete ",{'bold':True,'color':AMBER}),
          ("— based on WHO / iRAP evidence for these counter-measures; we will verify with before-and-after data as implementations finish.",{'color':AMBER})],size=10.5,ls=1.3)
    photo(s,a5("cfi_map_dots.png"),I(9.1),I(2.1),I(3.6),caption="Cohort-1 sites across India.")
    footer(s,wg,i,total); i+=1
    # S16 approvals
    s=slide()
    header(s,"04 · Project Rakshak — the paper trail",
           [("Approvals ",False),("in writing",True),(", from the authorities that own the roads",False)],sect=(4,"PROJECT RAKSHAK"))
    letters=["letter1.png","letter2.png","letter3.png","letter4.png","letter5.png","letter6.png"]
    real=[f for f in sorted(os.listdir(LTR)) if f.endswith('.png')][:6]
    lw_=I(1.92); lh=I(2.6); y=I(2.05)
    for j,f in enumerate(real):
        x=ML+j*(lw_+I(0.11))
        photo(s,os.path.join(LTR,f),x,y,lw_,lh,fill=True)
    text(s,ML,I(4.85),CW,I(0.3),"A sample of the 25+ approval and acknowledgement letters issued by public works and district authorities.",size=9.5,color=MUT)
    text(s,ML,I(5.3),I(3.3),I(0.26),"APPROVING AUTHORITIES INCLUDE",font=HEAD,size=8.5,bold=True,color=MUT,tracking=1.6)
    auth=["PWD Kerala","PWD Uttar Pradesh","PWD Punjab","CPWD + Addl. Collector, Indore","ADDA Durgapur","R&B Andhra Pradesh","GCC Chennai","BMC Mumbai"]
    for j,a in enumerate(auth):
        c=j%4; r=j//4
        chip(s,ML+c*I(3.05),I(5.62)+r*I(0.5),I(2.95),I(0.42),a,fill=GR_T,color=GREEN,size=9.5,bold=True)
    footer(s,wg,i,total); i+=1
    # S17 on the ground
    s=slide()
    header(s,"04 · Project Rakshak — on the ground",
           [("From approval to construction: ",False),("implementations under way",True)],sect=(4,"PROJECT RAKSHAK"))
    ivs=[("iv_durgapur_parking.png","Parking rationalisation — Durgapur"),("iv_durgapur_road.png","Road & shoulder work — Durgapur"),
         ("iv_guntur_markings.png","Fresh markings — Guntur"),("iv_indore_barricade.png","Barricading — Indore"),
         ("iv_indore_footpath.png","Footpath construction — Indore"),("iv_mumbai_signage.png","Signage — Mumbai")]
    tw=I(3.95); th=I(1.72)
    for j,(f,cap) in enumerate(ivs):
        r,c=divmod(j,3)
        x=ML+c*(tw+I(0.12)); y=I(2.05)+r*I(2.22)
        photo(s,a3(f),x,y,tw,th,fill=True,caption=cap)
    rect(s,ML,I(6.35),CW,I(0.52),fill=BR_T,rounded=True,radius=0.16)
    text(s,ML+I(0.22),I(6.42),CW-I(0.45),I(0.4),
         [("Case: Tejaji Nagar Junction, Indore ",{'bold':True,'color':BRAND}),("— an official black spot; redesign approved by CPWD and the Additional Collector's office.",{'color':BRAND})],size=10,ls=1.2)
    footer(s,wg,i,total); i+=1
    # S18 dashboard
    s=slide()
    header(s,"04 · Project Rakshak — transparency",
           [("A public dashboard tracks ",False),("every site to completion",True)],sect=(4,"PROJECT RAKSHAK"))
    photo(s,a5("rakshak_dashboard_full.png"),ML,I(1.98),I(7.6),caption="Live public dashboard — every site, its authority, risk level and implementation stage.")
    x=I(8.55); rows=[
      ("route","Every site tracked","From submission through approval to completed construction — regardless of who audited it.",BR_T,"#4A35FF"),
      ("git-compare","The PRAGATI parallel","The PM's PRAGATI platform showed what visible follow-up does for stuck projects. Same principle here, for road safety fixes.",TE_T,"#0E8A8A"),
      ("eye","What the Board gains","An honest, live read on how quickly road-owning agencies can act — evidence for capacity planning, not just compliance.",GR_T,"#0A9955")]
    y=I(2.05)
    for ic,t,d,tint,col in rows:
        icon_disc(s,ic,x,y,I(0.42),tint,col)
        text(s,x+I(0.58),y-I(0.03),I(3.6),I(0.35),t,font=HEAD,size=11,bold=True,color=INK)
        text(s,x+I(0.58),y+I(0.3),I(3.6),I(1.0),d,size=9.5,color=MUT,ls=1.25)
        y=y+I(1.5)
    footer(s,wg,i,total); i+=1
    # S19 standards
    s=slide()
    header(s,"04 · Project Rakshak — method",
           [("Anchored to the codes ",False),("your engineers already use",True)],sect=(4,"PROJECT RAKSHAK"))
    rows=[("book-check","IRC codes & MoRTH checklists","Every audit instrument is built on them — nothing bespoke, nothing incompatible.",BR_T,"#4A35FF"),
          ("link","A line into IRC H-7","Prof. Geetam Tiwari, member of the IRC H-7 Committee on Road Safety Audit, chairs our advisory work.",GR_T,"#0A9955"),
          ("graduation-cap","Masterclasses before fieldwork","Prof. Tiwari on the Safe System approach; Dr. S. Velmurugan (CSIR-CRRI) on IRC-131 and SP-55.",AM_T,"#E58900"),
          ("file-output","Handover in the authority's format","Findings arrive as the PWD or corporation needs them — ready to action, tracked publicly after.",TE_T,"#0E8A8A")]
    y=I(2.1)
    for j,(ic,t,d,tint,col) in enumerate(rows):
        irow(s,ML,y+j*I(0.95),I(7.5),ic,t,d,tint,col)
    photo(s,a5("ph_meeting_official.jpg"),I(8.5),I(2.1),I(4.2),I(2.6),fill=True,
          caption="Mentor and authority engagement is continuous — not a one-time submission.")
    photo(s,a3("iv_mumbai_signage.png"),I(8.5),I(5.15),I(4.2),I(1.45),fill=True,border=True)
    footer(s,wg,i,total); i+=1
    # S20 scaling
    s=slide()
    header(s,"04 · Project Rakshak — the long view",
           [("Built to be ",False),("institutionalised",True),(" — not to depend on us",False)],
           lead="Three audit tracks matched to road types, and a role for CFI that narrows over time.",sect=(4,"PROJECT RAKSHAK"))
    tracks=[("A — Institutional","IIT / NIT / SPA teams under expert mentors","Urban arterials, in-town state highways, district roads",BR_T,BRAND),
            ("B — NGO partners","Field teams; desk-reviewed and re-verified by CFI","District & peri-urban corridors",TE_T,TEAL),
            ("C — Certified RSAs","CSIR-CRRI-certified auditors, full IRC SP-88","National highways, complex junctions",AM_T,AMBER)]
    tw=I(3.95)
    for j,(t,who,road,tint,col) in enumerate(tracks):
        x=ML+j*(tw+I(0.12)); y=I(2.3)
        rect(s,x,y,tw,I(1.75),fill=MIST,rounded=True,radius=0.08)
        rect(s,x,y,tw,I(0.42),fill=tint,rounded=False)
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
    # S21 VRU
    s=slide()
    header(s,"04 · Vulnerable road users",
           [("A growing evidence base on ",False),("those most at risk",True)],sect=(4,"PROJECT RAKSHAK"))
    rows=[("bike","Gig & delivery riders","'When Risks Become Routine' (Feb 2026): incentive pressure, helmet compliance and training gaps — 300+ rider study, Delhi NCR.",AM_T,"#E58900"),
          ("footprints","Pedestrian-first audits","Rakshak audits document crossings, footpaths and lighting as designable protections — 900+ stakeholders consulted.",BR_T,"#4A35FF"),
          ("school","School zones","College-led, standards-based school-zone screening under exploration as the next extension of the audit platform.",TE_T,"#0E8A8A"),
          ("shield","Enforcement that protects VRUs","SATARK helps police prioritise the small share of vehicles with the worst records — targeted, fair, technology-led.",GR_T,"#0A9955")]
    y=I(2.0)
    for j,(ic,t,d,tint,col) in enumerate(rows):
        irow(s,ML,y+j*I(1.02),I(7.5),ic,t,d,tint,col)
    photo(s,a5("ph_gig_riders.jpg"),I(8.5),I(2.0),I(4.2),I(2.6),fill=True,
          caption="Delivery-rider outreach — materials and rights briefings at shift points.")
    photo(s,a5("ph_school_activity.jpg"),I(8.5),I(5.05),I(4.2),I(1.55),fill=True,border=True)
    footer(s,wg,i,total); i+=1
    return i

# ================================================================ WG-5 BODY
def wg5_body(wg,total,start):
    i=start
    # S13 journey
    s=slide()
    header(s,"04 · Post-crash care — the starting point",
           [("A family meets ",False),("many institutions",True),(" — not one programme",False)],
           lead="We mapped the hit-and-run claim journey with officials in Jaipur — seven stages, six hand-offs, every one manual today.",
           sect=(4,"POST-CRASH CARE"))
    photo(s,a3("journey_strip.png"),ML,I(2.3),I(12.05),caption="The claim journey as it actually runs — FIR to payment. Source: CFI mapping with district officials, Jaipur.")
    rect(s,ML,I(5.85),CW,I(0.8),fill=BR_T,rounded=True,radius=0.12)
    text(s,ML+I(0.25),I(5.97),CW-I(0.5),I(0.6),
         [("Our work: ",{'bold':True,'color':BRAND}),
          ("make each hand-off visible, guide the family at every stage, and give administrators the dashboards to see where files wait.",{'color':BRAND})],size=11.5,ls=1.3)
    footer(s,wg,i,total); i+=1
    # S14 Justice Unserved
    s=slide()
    header(s,"04 · Post-crash care — our research foundation",
           [("'Justice Unserved' — ",False),("the evidence base",True),(" we built first",False)],
           lead="Published January 2026 · launched at IIT Delhi · findings presented to MoRTH · covered by national press.",
           sect=(4,"POST-CRASH CARE"))
    photo(s,a3("comp_image1.png"),ML,I(2.15),I(2.75),caption="The report — file reviews, RTIs and\nconsultations across the pipeline.")
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
    text(s,I(9.3),I(2.45),I(3.15),I(0.9),"205",font=HEAD,size=44,bold=True,color=BRAND)
    text(s,I(9.3),I(3.35),I(3.15),I(0.6),"hit-and-run claims filed in FY22-23…",size=11,color=INK,ls=1.3)
    text(s,I(9.3),I(4.0),I(3.15),I(0.6),[("against ~",{'color':MUT}),("25,000",{'bold':True,'color':INK}),(" eligible crashes.",{'color':MUT})],size=11,ls=1.3)
    text(s,I(9.3),I(4.75),I(3.15),I(0.7),"The scheme is sound — the pipeline to it needs support.",size=10.5,color=MUT,ls=1.3,italic=True)
    text(s,ML,I(6.1),I(12),I(0.5),
         [("Press: ",{'bold':True}),("Deccan Herald · Economic Times · Fortune India · IndiaSpend · Scroll.in · The Wire — and cited in Parliament-facing briefings.",{'color':MUT})],size=9.5,ls=1.2)
    footer(s,wg,i,total); i+=1
    # S15 district machinery
    s=slide()
    header(s,"04 · Post-crash care — from research to districts",
           [("Working ",False),("inside the district machinery",True)],
           lead="Not commentary from outside — formal seats, formal tasking, files on the table.",sect=(4,"POST-CRASH CARE"))
    rows=[("landmark","Four DRSCs joined","Gurugram, South-West Delhi, North-West Delhi and Jaipur — with MoUs with Jaipur Traffic Police and Gurugram Police.",BR_T,"#4A35FF"),
          ("folder-open","102 files, read page by page","With Gurugram's administration we reviewed every hit-and-run file since 2022 — mapping exactly where eligible families drop out.",TE_T,"#0E8A8A"),
          ("clipboard-check","Formally tasked","The South-West Delhi DRSC's signed minutes task Crashfree India with digitisation and analytics support for scheme files.",GR_T,"#0A9955"),
          ("user-check","Embedded presence","A research fellow sits with Gurugram district offices — implementation support, not external commentary.",AM_T,"#E58900")]
    y=I(2.25)
    for j,(ic,t,d,tint,col) in enumerate(rows):
        irow(s,ML,y+j*I(1.0),I(7.5),ic,t,d,tint,col)
    photo(s,a5("ph_helpdesk_camp.jpg"),I(8.5),I(2.2),I(4.2),I(2.2),fill=True,
          caption="Legal-rights helpdesk with district administration, Jan 2026.")
    photo(s,a5("ph_law_students.jpg"),I(8.5),I(4.95),I(4.2),I(1.6),fill=True,
          caption="Law-student volunteers after a hospital helpdesk drive.")
    footer(s,wg,i,total); i+=1
    # S16 Rajasthan
    s=slide()
    header(s,"04 · Post-crash care — state engagement",
           [("With Rajasthan: from ground mapping to ",False),("a working template",True)],
           lead="Supporting the State Road Safety Lead Agency and Transport Department on the Hit-and-Run Compensation Scheme.",
           sect=(4,"POST-CRASH CARE"))
    rect(s,ML,I(2.25),I(3.6),I(1.9),fill=MIST,rounded=True,radius=0.08)
    text(s,ML+I(0.2),I(2.45),I(3.2),I(0.7),"~180",font=HEAD,size=36,bold=True,color=BRAND)
    text(s,ML+I(0.2),I(3.2),I(3.2),I(0.4),[("of ~",{'color':MUT}),("395",{'bold':True}),(" monthly hit-and-run claims in Rajasthan come from Jaipur alone (~46%)",{'color':MUT})],size=10,ls=1.25)
    text(s,ML+I(0.2),I(3.55),I(3.2),I(0.5),"",size=9)
    text(s,ML,I(4.4),I(3.6),I(1.0),"Not because crashes happen only there — because Jaipur runs active outreach and a single coordination cell. The template is replicable.",size=9.5,color=MUT,ls=1.3)
    x=I(4.5)
    rows=[("file-warning","What holds claims back","11–13 documents demanded vs the 7 court-agreed standard · ~50% of files lack a usable family phone number · manual hand-offs between six offices.",AM_T,"#E58900"),
          ("alert-octagon","The cautionary example","A state portal that changed how offices work saw monthly requests fall 350 → 25. Our design rule: no stakeholder changes their medium.",RD_T,"#E11900"),
          ("list-checks","Five GIC queries drafted","Clarification questions ready for the insurer consortium — a joint ask from the Department lands harder.",BR_T,"#4A35FF"),
          ("rocket","Six asks → 60 days","Decisions identified with the Department that put Phase 1 (family traceability) in motion within 60 days.",GR_T,"#0A9955")]
    y=I(2.25)
    for j,(ic,t,d,tint,col) in enumerate(rows):
        icon_disc(s,ic,x,y+j*I(1.06),I(0.42),tint,col)
        text(s,x+I(0.58),y+j*I(1.06)-I(0.03),I(2.5),I(0.6),t,font=HEAD,size=11,bold=True,color=INK,ls=1.1)
        text(s,x+I(3.15),y+j*I(1.06)-I(0.03),I(5.05),I(0.95),d,size=9.5,color=MUT,ls=1.22)
    footer(s,wg,i,total); i+=1
    # S17 portal concept
    s=slide()
    header(s,"04 · Post-crash care — the portal concept",
           [("Designed so ",False),("no stakeholder changes how they work",True)],
           lead="Families stay on WhatsApp; officers keep their queues and sign-offs; the system connects them behind the scenes.",
           sect=(4,"POST-CRASH CARE"))
    for j in range(3):
        photo(s,a5(f"wa_phone{j+1}.png"),ML+j*I(1.55),I(2.2),I(1.45),border=False)
    text(s,ML,I(4.45),I(4.6),I(0.5),"The family flow — day-one intake, document capture, live status. All inside WhatsApp, in Hindi.",size=9,color=MUT,ls=1.25)
    photo(s,a5("queue_ui.png"),I(5.55),I(2.2),I(7.15),caption="Officer view — same cases, filtered to what each desk owns; AI pre-checks flag issues, the decision stays human.")
    prins=["Family keeps WhatsApp","Officer keeps every decision","Traceability before automation","Single-pass clarification","Dashboards for administrators"]
    y=I(5.85)
    for j,p in enumerate(prins):
        chip(s,ML+j*I(2.46),y,I(2.36),I(0.46),p,fill=BR_T,color=BRAND,size=9)
    footer(s,wg,i,total); i+=1
    # S18 claimant-side standards
    s=slide()
    header(s,"04 · Post-crash care — standards, ready to adopt",
           [("The claimant-side standards ",False),("WG-5 could set",True)],
           lead="Small, procedural standards — none needing new legislation — each drawn from files we have read and offices we work with.",
           sect=(4,"POST-CRASH CARE"))
    rect(s,ML,I(2.3),I(5.9),I(3.9),fill=GR_T,rounded=True,radius=0.08)
    text(s,ML+I(0.25),I(2.45),I(5.4),I(0.3),"THE 7-DOCUMENT STANDARD — AS AGREED BEFORE THE SUPREME COURT",font=HEAD,size=9,bold=True,color=GREEN,tracking=1.2)
    docs7=["Application (Form I & IV)","Copy of FIR / FAR","Post-mortem or injury report","Death certificate (in death cases)","Claimant / victim ID proof","Bank passbook (IFSC visible)","Cashless-treatment amount received"]
    for j,d0 in enumerate(docs7):
        icon(s,"check",ML+I(0.28),I(2.95)+j*I(0.42),I(0.24),"#0A9955")
        text(s,ML+I(0.65),I(2.93)+j*I(0.42),I(5.1),I(0.35),d0,size=10,color=INK,ls=1.1)
    rect(s,I(6.85),I(2.3),I(5.85),I(3.9),fill=AM_T,rounded=True,radius=0.08)
    text(s,I(7.1),I(2.45),I(5.4),I(0.3),"ASKED ON TOP TODAY — EACH ONE A TRIP, A FEE, OR A DROP-OUT",font=HEAD,size=9,bold=True,color=AMBER,tracking=1.2)
    extra=["Court-certified copies of FIR & FR","Full challan file / e-DAR / iRAD","Site map / naksha mauka","Notarised affidavit — name mismatch","Notarised affidavit — non-filing of MACT claim","Legal-heir / succession certificate"]
    for j,d0 in enumerate(extra):
        icon(s,"plus",I(7.13),I(2.95)+j*I(0.46),I(0.24),"#E58900")
        text(s,I(7.5),I(2.93)+j*I(0.46),I(5.0),I(0.4),d0,size=10,color=INK,ls=1.1)
    text(s,ML,I(6.4),CW,I(0.5),
         [("Also ready: ",{'bold':True}),("stage-wise SLA benchmarks · family-communication norms at every state change · a document-quality checklist for AI-assisted pre-verification.",{'color':MUT})],size=10,ls=1.25)
    footer(s,wg,i,total); i+=1
    # S19 helpdesks + EMS
    s=slide()
    header(s,"04 · Post-crash care — the first hours",
           [("Helpdesks in trauma wards, and ",False),("an EMS evidence line",True)],sect=(4,"POST-CRASH CARE"))
    photo(s,a5("ph_helpdesk_desk.jpg"),ML,I(2.05),I(4.3),I(2.55),fill=True,
          caption="Hospital legal helpdesk — 100+ victims supported in the first four days of operation.")
    photo(s,a5("ph_stall.jpg"),ML,I(5.1),I(4.3),I(1.5),fill=True,border=True)
    x=I(5.35)
    rows=[("timer","The response gap, measured","Our Pre-Hospital Care Primer (Sept 2025): ERSS-112 is live across 36 states & UTs, yet ambulance arrival averages 25–35 minutes and the full care episode runs 55–75 minutes — against a 60-minute golden hour.",TE_T,"#0E8A8A"),
          ("map","State innovations documented","Maharashtra's MEMS — 937 ambulances under centralised dispatch; Tamil Nadu's TAEI trauma corridors — pre-arrival alerts and treatment protocols.",BR_T,"#4A35FF"),
          ("heart-handshake","Good Samaritan & Cashless 2025","Bystander protections and the ₹1.5 lakh / 7-day Cashless Treatment Scheme, explained in our public guides — the demand side of trauma care.",GR_T,"#0A9955"),
          ("stethoscope","Where this serves WG-5","A ready, referenced baseline for the Group's EMS and trauma-care standards discussions — with state models already compared.",AM_T,"#E58900")]
    y=I(2.05)
    for j,(ic,t,d,tint,col) in enumerate(rows):
        icon_disc(s,ic,x,y+j*I(1.13),I(0.42),tint,col)
        text(s,x+I(0.58),y+j*I(1.13)-I(0.03),I(2.35),I(0.6),t,font=HEAD,size=10.5,bold=True,color=INK,ls=1.08)
        text(s,x+I(3.0),y+j*I(1.13)-I(0.03),I(4.35),I(1.05),d,size=9,color=MUT,ls=1.2)
    footer(s,wg,i,total); i+=1
    # S20 pipeline measured
    s=slide()
    header(s,"04 · Post-crash care — the pipeline, measured",
           [("Numbers a standard ",False),("can act on",True)],
           lead="Each one is a lever for a WG-5 standard, toolkit entry or communication norm — none requires new legislation.",
           sect=(4,"POST-CRASH CARE"))
    tiles=[("921 of 1,026","claims pending nationally were stalled at documentation alone (July 2024)"),
           ("~60 days","typical intake latency where claims surface only via bi-monthly meetings"),
           ("~50%","of case files lack a usable family phone number — traceability is the first lever"),
           ("7 vs 11–13","court-agreed documents vs what claimants are asked for in practice"),
           ("FY23-24: 12%","of eligible crashes converted to filed claims — improving, from a 2% base"),
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
          ("consultations with GIC and insurers on settlement practice · guidance from Justice J.R. Midha (Retd.), architect of the FaSTDAR process · working partners across MACT courts, DLSAs and legal-services clinics.",{'color':MUT})],size=10.5,ls=1.35)
    footer(s,wg,i,total); i+=1
    # S21 team fit
    s=slide()
    header(s,"04 · Why our team fits this mandate",
           [("Post-crash care needs ",False),("more than one discipline",True)],
           lead="A legally sound framework can still be hard to use; a good portal can still miss district workflows. Our team is built across the whole chain.",
           sect=(4,"POST-CRASH CARE"))
    cards=[("scale","Law & policy","NALSAR and Delhi University-trained; scheme analysis, RTIs, MoRTH and Parliament-facing engagement.",BR_T,BRAND),
           ("cpu","Technology & product","IIT-trained; Aasha, the calculator, dashboards and the portal architecture shown earlier.",TE_T,TEAL),
           ("map-pin","Field & district practice","TISS-trained; district embedding, DRSC work, helpdesk operations, victim interviews.",GR_T,GREEN),
           ("message-square","Behaviour & communication","Psychology and design; guides, comics and multilingual communication families actually read.",AM_T,AMBER)]
    tw=I(2.97)
    for j,(ic,t,d,tint,col) in enumerate(cards):
        x=ML+j*(tw+I(0.08)); y=I(2.5)
        rect(s,x,y,tw,I(2.6),fill=PAPER,line=LINE,rounded=True,radius=0.08)
        icon_disc(s,ic,x+I(0.2),y+I(0.2),I(0.5),tint,f"#{col}" if isinstance(col,str) else None or {BRAND:"#4A35FF",TEAL:"#0E8A8A",GREEN:"#0A9955",AMBER:"#E58900"}[col])
        text(s,x+I(0.2),y+I(0.85),tw-I(0.4),I(0.35),t,font=HEAD,size=12,bold=True,color=INK)
        text(s,x+I(0.2),y+I(1.22),tw-I(0.4),I(1.3),d,size=9.5,color=MUT,ls=1.25)
    text(s,ML,I(5.5),CW,I(0.7),
         [("Advised by ",{'bold':True}),("Piyush Tewari (SaveLIFE Foundation), Prof. Geetam Tiwari (IIT Delhi) and Justice J.R. Midha (Retd., Delhi High Court) — with practitioner partners across MACT courts, DLSAs and insurers.",{'color':MUT})],size=10.5,ls=1.35)
    footer(s,wg,i,total); i+=1
    return i

# ================================================================ ASSEMBLY
def build_wg2():
    new_deck(); TOTAL=23
    cover(2,"Safe Roads, Speeds &","Vulnerable Road Users",
          [("31","sites audited across 18 cities"),("25+","written authority approvals"),("15","implementations underway"),("3,00,000+","vehicles screened by SATARK")],
          [a5("implementation_work.jpg"),a5("guntur_junction.jpg"),a3("iv_indore_footpath.png"),a5("ph_police_rally.jpg")],1,TOTAL)
    letter(2,
      "In our first year we audited 31 high-risk locations across 18 cities, secured 25+ written approvals from road-owning authorities, and began implementation at 15 sites — each tracked on a public dashboard. SATARK, our AI enforcement platform, has screened over 3,00,000 vehicles for police in Jaipur and Bengaluru and has now reached Gurugram. Four open-data platforms, the Aasha victim chatbot, hospital helpdesks and MS Dhoni as our Goodwill Ambassador complete the picture.",
      2,TOTAL)
    agenda(2,"Project Rakshak in depth",3,TOTAL)
    about(4,TOTAL,2)
    portfolio(5,TOTAL,2)
    satark(6,TOTAL,2)
    opendata(7,TOTAL,2)
    victim_suite(8,TOTAL,2)
    youth(9,TOTAL,2)
    ground(10,TOTAL,2)
    dhoni(11,TOTAL,2)
    people(12,TOTAL,2)
    nxt=wg2_body(2,TOTAL,13)
    contribution(2,[("Ready evidence for standard-setting","Site-level audit data, crash-pattern analysis and costed intervention designs across emerging hotspots and official black spots — for rectification protocols and speed-management guidance."),
                    ("A live testing ground","Active district relationships in Gurugram, South-West Delhi and Jaipur offer a ready pipeline to pilot or stress-test draft recommendations before national rollout."),
                    ("Ground-level implementation diagnostics","Granular, field-verified insight into how DRSCs and road-owning agencies actually move — meeting cadence, data use, follow-through."),
                    ("Technical bench strength on request","Our academic and expert network stands ready for drafting, review and technical input on road design, speed and VRU standards.")],nxt,TOTAL,"Project Rakshak in depth")
    close(2,23,TOTAL)
    save(os.path.join(BUILD,"CFI_NRSB_WG2_v2.pptx"))

def build_wg5():
    new_deck(); TOTAL=23
    cover(5,"Post-Crash Care, Policy Standards","& State Implementation",
          [("4","District Road Safety Committees joined"),("102","hit-and-run files reviewed with districts"),("100+","victims helped in helpdesks' first 4 days"),("~46%","of Rajasthan's monthly claims mapped in Jaipur")],
          [a5("ph_helpdesk_desk.jpg"),a5("ph_law_students.jpg"),a5("ph_helpdesk_camp.jpg"),a5("ph_stall.jpg")],1,TOTAL)
    letter(5,
      "Our post-crash work began with evidence. 'Justice Unserved', our study of the hit-and-run compensation pipeline, found only 205 claims filed in FY22-23 against roughly 25,000 eligible crashes. Since then we have joined four District Road Safety Committees, reviewed 102 case files with the Gurugram administration, mapped Rajasthan's scheme office-by-office with the Transport Department, and built the tools families actually use — the Aasha chatbot, a compensation calculator, hospital helpdesks that supported 100+ victims in their first four days, and plain-language guides in Hindi.",
      2,TOTAL)
    agenda(5,"Post-crash care in depth",3,TOTAL)
    about(4,TOTAL,5)
    portfolio(5,TOTAL,5)
    satark(6,TOTAL,5)
    opendata(7,TOTAL,5)
    victim_suite(8,TOTAL,5)
    youth(9,TOTAL,5)
    ground(10,TOTAL,5)
    dhoni(11,TOTAL,5)
    people(12,TOTAL,5)
    nxt=wg5_body(5,TOTAL,13)
    contribution(5,[("A victim-side evidence base","'Justice Unserved', 120+ victim and family interactions, and file-level audit data showing precisely where eligible families drop out of the process."),
                    ("A district toolkit, drawn from practice","Working DRSC integration experience — agendas, file digitisation, fellow placement — ready to be codified into the Group's district toolkit."),
                    ("A reusable state portal blueprint","The Rajasthan case-management design — guided filing, stage-wise visibility, single-pass clarification — offered as a template any state can adapt."),
                    ("Standards input from the claimant's side","Document standards (the court-agreed 7), communication standards and timeline benchmarks, grounded in what families actually experience.")],nxt,TOTAL,"Post-crash care in depth")
    close(5,23,TOTAL)
    save(os.path.join(BUILD,"CFI_NRSB_WG5_v2.pptx"))

if __name__=="__main__":
    build_wg2()
    build_wg5()

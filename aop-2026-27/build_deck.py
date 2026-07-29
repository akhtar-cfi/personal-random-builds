from helpers import *
TOTAL=15

# ---------------- S1 COVER ----------------
s=new_slide()
band_w=Inches(3.6)
rect(s,SLIDE_W-band_w,0,band_w,SLIDE_H,BRAND)
sparkle(s,SLIDE_W-band_w+Inches(0.5),Inches(0.55),Inches(0.5),LAV)
tags=["PROJECT RAKSHAK","HIT & RUN COMPENSATION","CIVIC & GOVTECH  ·  SATARK","CAMPAIGN & ENABLERS","BETS  ·  SSI + GIG RIDER"]
ty=Inches(2.3)
for t in tags:
    text(s,SLIDE_W-band_w+Inches(0.5),ty,Inches(2.9),Inches(0.3),t,font=HEAD,size=10.5,bold=True,color=WHITE,tracking=1.8)
    hline(s,SLIDE_W-band_w+Inches(0.5),ty+Inches(0.42),Inches(2.6),LAV_DK,0.75)
    ty+=Inches(0.72)
wordmark(s,M_L,Inches(0.6))
eyebrow(s,M_L,Inches(2.35),"ANNUAL OPERATING PLAN  ·  JULY 2026 - JUNE 2027")
text(s,M_L,Inches(2.75),Inches(8.6),Inches(0.8),"From programmes",font=HEAD,size=40,bold=True,color=DARK,ls=1.02)
text(s,M_L,Inches(3.45),Inches(8.6),Inches(0.8),"to institutions.",font=HEAD,size=40,bold=True,color=BRAND,ls=1.02)
text(s,M_L,Inches(4.45),Inches(8.4),Inches(0.8),"Year 2 runs three core programmes and one civic-tech vertical, deep not wide.\nEverything else is a seed-funded bet that must earn its way to a full budget.",font=BODY,size=13,color=MUTED,ls=1.45)
hline(s,M_L,Inches(6.35),Inches(8.4),BORDER,1.0)
text(s,M_L,Inches(6.55),Inches(8.4),Inches(0.3),"Vision Zero Trust  ·  Internal Planning Document  ·  Budget Rs 6.00 Cr",font=HEAD,size=9.5,bold=True,color=MUTED,tracking=1.4)

# ---------------- S2 YEAR 1 SCORECARD ----------------
s=new_slide()
sparkles_tr(s)
y0=std_header(s,"YEAR 1 IN REVIEW","What one year of audit-led work",
              "put on the board.",
              "Cohort 1 proved the model: youth-generated audits can reach district officials and trigger engineering action.")
stats=[("31","Priority sites audited","map-pin"),("18","Cities engaged","building-2"),
       ("25+","Approvals & actions initiated","circle-check"),("7+","Engineering works begun","hard-hat"),
       ("900+","Stakeholder surveys","users"),("120+","Victims & families surveyed","hand-helping"),
       ("30+","Expert consultations","mic"),("1M+","Citizens reached","megaphone")]
cw=Inches(2.83); ch=Inches(1.62); gx=Inches(0.2); gy=Inches(0.25)
for i,(num,lab,ic) in enumerate(stats):
    r_,c_=divmod(i,4)
    x=M_L+c_*(cw+gx); y=Inches(2.75)+r_*(ch+gy)
    rect(s,x,y,cw,ch,BRAND_LITE,rounded=True)
    icon(s,ic,x+cw-Inches(0.55),y+Inches(0.22),Inches(0.32),"#4A35FF")
    text(s,x+Inches(0.25),y+Inches(0.22),Inches(2.0),Inches(0.6),num,font=HEAD,size=30,bold=True,color=BRAND)
    text(s,x+Inches(0.25),y+Inches(0.95),cw-Inches(0.5),Inches(0.55),lab,font=BODY,size=10.5,color=MUTED,ls=1.25)
rect(s,M_L,Inches(6.45),CONTENT_W,Inches(0.42),BRAND,rounded=True)
text(s,M_L,Inches(6.45),CONTENT_W,Inches(0.42),"150+ members  ·  50+ experts  ·  AASHA chatbot live  ·  MoUs with Gurugram & Jaipur Traffic Police  ·  DRSC integration begun in SW Delhi",
     font=HEAD,size=10.5,bold=True,color=WHITE,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
footer(s,2,TOTAL)

# ---------------- S3 LEARNINGS ----------------
s=new_slide()
sparkles_tr(s)
y0=std_header(s,"LEARNINGS FROM YEAR 1","Five lessons that rewired",
              "the Year 2 plan.")
rows=[
 ("badge-check","Credibility is the currency","Energy and field discovery were strong; report quality must meet DRSC and NHAI standards without rework.","Expert Consortium, certified RSAs, Rakshak Audit Manual v1.0"),
 ("scale","Awareness alone doesn't move claims","Institutional incapacity and process non-compliance - not just awareness gaps - drive claim dropout.","Shift from awareness drives to stage-wise scheme audit"),
 ("map-pin","Depth beats breadth","Parallel full-scale sites diluted bandwidth and institutional trust took longer than planned.","Anchor districts + model-district approach; MACT reform deprioritised"),
 ("clipboard-check","Audits die at submission","Most audit programmes stop at report submission; follow-through is where impact happens.","Public accountability loop - every recommendation tracked to implementation"),
 ("indian-rupee","Plan what we fund","Prior budget carried unfunded activities and untagged cost lines.","Unit-based budget, quarterly phasing, formula-driven rollups"),
]
ry=Inches(2.15); rh=Inches(0.86); gap=Inches(0.09)
for ic,t1,body,nxt in rows:
    rect(s,M_L,ry,CONTENT_W,rh,WHITE,line=BORDER,rounded=True)
    circle(s,M_L+Inches(0.22),ry+Inches(0.21),Inches(0.44),BRAND_LITE)
    icon(s,ic,M_L+Inches(0.31),ry+Inches(0.30),Inches(0.26),"#4A35FF")
    text(s,M_L+Inches(0.85),ry+Inches(0.13),Inches(3.1),Inches(0.6),t1,font=HEAD,size=12,bold=True,color=DARK,ls=1.1)
    text(s,M_L+Inches(4.05),ry+Inches(0.13),Inches(4.35),Inches(0.62),body,font=BODY,size=9.5,color=MUTED,ls=1.25)
    text(s,M_L+Inches(8.6),ry+Inches(0.13),Inches(0.75),Inches(0.3),"IN Y2",font=HEAD,size=8,bold=True,color=BRAND,tracking=1.6)
    text(s,M_L+Inches(8.6),ry+Inches(0.36),Inches(3.15),Inches(0.45),nxt,font=BODY,size=9.5,bold=False,color=DARK,ls=1.2)
    ry+=rh+gap
footer(s,3,TOTAL)

# ---------------- S4 OBJECTIVES / POST-Y2 DESTINATION ----------------
s=new_slide()
sparkles_tr(s)
std_header(s,"OBJECTIVES  ·  THE DESTINATION","What must be true","when Year 2 ends.")
rect(s,M_L,Inches(2.12),CONTENT_W,Inches(0.72),BRAND,rounded=True)
text(s,M_L+Inches(0.35),Inches(2.12),CONTENT_W-Inches(0.7),Inches(0.72),
     [("POSITION  ",{'font':HEAD,'size':9,'bold':True,'color':LAV,'tracking':1.8}),
      ("By June 2027, CFI is India's audit-and-accountability institution for road safety - the organisation governments call to find where systems break, and to hold the fix to completion.",{'font':BODY,'size':11,'color':WHITE})],
     anchor=MSO_ANCHOR.MIDDLE,ls=1.3)
objs=[("hard-hat","Rakshak runs inside institutions",
       "An audit pipeline owned by universities, NGO partners and certified RSAs - consortium, Audit Manual v1.0 and a public dashboard - that no longer needs CFI to push every audit.","Y3: national scale through chapters"),
      ("scale","Compensation fixed, then replicated",
       "Two districts where the hit & run claim pipeline demonstrably works, pilots running beyond them, and the process mapped in 8+ districts - a replication playbook, not a project.","Y3: state-level adoption"),
      ("radar","SATARK as public infrastructure",
       "Enforcement intelligence live in 30 cities, plus an active exploration track for new govtech products and digital public goods with government partners.","Y3: the road-safety data layer for government"),
      ("megaphone","A public evidence brand",
       "Four open data products cited by committees and press, 1M+ citizens engaged through the campaign, and both bets resolved with board-ready designs.","Y3: evidence citations drive inbound demand")]
cw=Inches(5.86); ch=Inches(1.78); gx=Inches(0.2); gy=Inches(0.18); y0v=Inches(3.02)
for i,(ic,t1,body,y3) in enumerate(objs):
    r_,c_=divmod(i,2)
    x=M_L+c_*(cw+gx); y=y0v+r_*(ch+gy)
    rect(s,x,y,cw,ch,BRAND_LITE,rounded=True)
    circle(s,x+Inches(0.22),y+Inches(0.22),Inches(0.44),WHITE)
    icon(s,ic,x+Inches(0.31),y+Inches(0.31),Inches(0.26),"#4A35FF")
    text(s,x+Inches(0.8),y+Inches(0.18),cw-Inches(1.1),Inches(0.3),t1,font=HEAD,size=12,bold=True,color=DARK)
    text(s,x+Inches(0.8),y+Inches(0.48),cw-Inches(1.1),Inches(0.85),body,font=BODY,size=9.2,color=MUTED,ls=1.25)
    text(s,x+Inches(0.8),y+ch-Inches(0.32),cw-Inches(1.1),Inches(0.25),y3,font=HEAD,size=8,bold=True,color=BRAND,tracking=1.2)
footer(s,4,TOTAL)

# ---------------- S5 STRATEGY ----------------
s=new_slide()
sparkles_tr(s)
std_header(s,"YEAR 2 STRATEGY","One operating model,","run deeper.")
threeA=[("01  ·  AUDIT","search","Diagnose where systems break - blackspots, claim pipelines, school zones, platform practices - with evidence that survives institutional review."),
        ("02  ·  ADVOCATE","megaphone","Turn evidence into stakeholder action: DRSC integration, co-designed fixes, model districts, a sustained publishing cadence."),
        ("03  ·  HOLD ACCOUNTABLE","shield-check","Track every recommendation publicly from submission to implementation; escalate from district fixes to system reform.")]
ry=Inches(2.25)
for kick,ic,body in threeA:
    circle(s,M_L,ry,Inches(0.5),BRAND_LITE)
    icon(s,ic,M_L+Inches(0.11),ry+Inches(0.11),Inches(0.28),"#4A35FF")
    text(s,M_L+Inches(0.72),ry-Inches(0.02),Inches(6.5),Inches(0.3),kick,font=HEAD,size=12,bold=True,color=DARK,tracking=1.2)
    text(s,M_L+Inches(0.72),ry+Inches(0.3),Inches(6.6),Inches(0.85),body,font=BODY,size=10.5,color=MUTED,ls=1.35)
    ry+=Inches(1.5)
bx=Inches(8.5); bw=SLIDE_W-bx-M_R
rect(s,bx,Inches(2.2),bw,Inches(4.55),BRAND,rounded=True)
text(s,bx+Inches(0.4),Inches(2.55),bw-Inches(0.8),Inches(0.3),"THE YEAR 2 SHIFT",font=HEAD,size=10,bold=True,color=LAV,tracking=2.2)
text(s,bx+Inches(0.4),Inches(2.95),bw-Inches(0.8),Inches(0.75),"From programmes\nto institutions.",font=HEAD,size=17,bold=True,color=WHITE,ls=1.15)
hline(s,bx+Inches(0.4),Inches(3.95),bw-Inches(0.8),LAV_DK,1.0)
bullets=["Expert Consortium + Audit Manual v1.0 give audits institutional authority",
         "Model districts, not scattered pilots - Gurugram, SW Delhi, anchor cities",
         "Civic tech in government hands: SATARK enforcement + four open data products",
         "Publishing cadence: monthly field notes, quarterly findings, year-end audit reports"]
by=Inches(4.15)
for b in bullets:
    circle(s,bx+Inches(0.42),by+Inches(0.08),Inches(0.09),WHITE)
    text(s,bx+Inches(0.68),by,bw-Inches(1.05),Inches(0.6),b,font=BODY,size=10,color=WHITE,ls=1.25)
    by+=Inches(0.64)
footer(s,5,TOTAL)

# ---------------- S6 FOCUS AREAS ----------------
s=new_slide()
sparkles_tr(s)
std_header(s,"KEY FOCUS AREAS","Three core programmes,","two seed-funded bets.",
           "Each core programme has a north-star outcome and a dedicated budget line. Bets carry seed money only - they scale only if their pilots earn it.")
cards=[("CORE 01  ·  RS 1.85 CR","hard-hat","Project Rakshak","Institutionalise the national audit pipeline: three-track model, Expert Consortium, Audit Manual v1.0.","150+ blackspots audited"),
       ("CORE 02  ·  RS 0.60 CR","scale","Hit & Run Compensation","Fix the claim pipeline in two districts, pilot the playbook beyond them, and map the process in 8+ districts.","2 fixed  ·  8+ mapped"),
       ("CORE 03  ·  RS 1.00 CR","radar","Civic & GovTech","Scale SATARK - the AI enforcement co-pilot for traffic police - to 30 cities; explore the next govtech products and partnerships.","SATARK live in 30 cities")]
cw=Inches(3.84); ch=Inches(2.42); gx=Inches(0.2); y=Inches(2.72)
for i,(kick,ic,title,body,tgt) in enumerate(cards):
    x=M_L+i*(cw+gx)
    rect(s,x,y,cw,ch,BRAND_LITE,rounded=True)
    circle(s,x+Inches(0.3),y+Inches(0.26),Inches(0.52),WHITE)
    icon(s,ic,x+Inches(0.41),y+Inches(0.37),Inches(0.30),"#4A35FF")
    text(s,x+Inches(0.98),y+Inches(0.26),cw-Inches(1.28),Inches(0.25),kick,font=HEAD,size=8.4,bold=True,color=BRAND,tracking=1.5)
    text(s,x+Inches(0.98),y+Inches(0.50),cw-Inches(1.28),Inches(0.35),title,font=HEAD,size=14,bold=True,color=DARK,ls=1.1)
    text(s,x+Inches(0.3),y+Inches(0.98),cw-Inches(0.6),Inches(0.85),body,font=BODY,size=9.3,color=MUTED,ls=1.28)
    rect(s,x+Inches(0.3),y+ch-Inches(0.56),cw-Inches(0.6),Inches(0.38),BRAND,rounded=True)
    text(s,x+Inches(0.3),y+ch-Inches(0.56),cw-Inches(0.6),Inches(0.38),tgt,font=HEAD,size=8.8,bold=True,color=WHITE,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
by=Inches(5.32)
text(s,M_L,by,Inches(6),Inches(0.28),"TWO BETS  ·  SEED-FUNDED, STAGE-GATED",font=HEAD,size=10,bold=True,color=BRAND,tracking=2.0)
bets=[("school","School Safety Index","The 2,000-school index is parked. Seed: validate the IRC:SP:32 rubric on ~100 schools in one city.","Rs 0.10 Cr seed"),
      ("bike","Gig Rider Safety","The national study is parked. Seed: scoping study + first engagements with delivery platforms.","Rs 0.10 Cr seed")]
bw_=Inches(5.86); bh=Inches(1.02)
for i,(ic,t1,body,chip) in enumerate(bets):
    x=M_L+i*(bw_+Inches(0.2))
    yc=by+Inches(0.34)
    rect(s,x,yc,bw_,bh,WHITE,line=BORDER,rounded=True)
    circle(s,x+Inches(0.2),yc+Inches(0.28),Inches(0.44),BRAND_LITE)
    icon(s,ic,x+Inches(0.29),yc+Inches(0.37),Inches(0.26),"#4A35FF")
    text(s,x+Inches(0.8),yc+Inches(0.14),Inches(2.9),Inches(0.3),t1,font=HEAD,size=11,bold=True,color=DARK)
    text(s,x+Inches(0.8),yc+Inches(0.42),bw_-Inches(2.35),Inches(0.55),body,font=BODY,size=8.8,color=MUTED,ls=1.22)
    rect(s,x+bw_-Inches(1.42),yc+Inches(0.33),Inches(1.22),Inches(0.36),BRAND_LITE,rounded=True)
    text(s,x+bw_-Inches(1.42),yc+Inches(0.33),Inches(1.22),Inches(0.36),chip,font=HEAD,size=8.2,bold=True,color=BRAND,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
footer(s,6,TOTAL)

# ---------------- S7 RAKSHAK DEEP DIVE ----------------
s=new_slide()
sparkles_tr(s)
std_header(s,"DEEP DIVE  ·  CORE 01","Project Rakshak:","put the audit pipeline inside institutions.")
tx=M_L; ty=Inches(2.2)
text(s,tx,ty,Inches(7.5),Inches(0.3),"THE THREE-TRACK MODEL  ·  RUN BY INSTITUTIONS, NOT BY CFI ALONE",font=HEAD,size=10,bold=True,color=BRAND,tracking=1.8)
tracks=[("A","Institutional","IIT / NIT / SPA student teams under expert mentors; IRC-aligned rubric","~90 sites"),
        ("B","NGO Partners","NGO field teams; 100% desk review + 10-15% physical re-checks by CFI","~20 sites"),
        ("C","Certified RSAs","CRRI-certified auditors; full IRC SP:88 - usable by NHAI without rework","~40 sites")]
ry=ty+Inches(0.38); rh=Inches(0.78)
for t,name,body,vol in tracks:
    rect(s,tx,ry,Inches(7.5),rh,WHITE,line=BORDER,rounded=True)
    circle(s,tx+Inches(0.2),ry+Inches(0.16),Inches(0.46),BRAND)
    text(s,tx+Inches(0.2),ry+Inches(0.19),Inches(0.46),Inches(0.4),t,font=HEAD,size=15,bold=True,color=WHITE,align=PP_ALIGN.CENTER)
    text(s,tx+Inches(0.85),ry+Inches(0.09),Inches(2.0),Inches(0.3),name,font=HEAD,size=11,bold=True,color=DARK)
    text(s,tx+Inches(0.85),ry+Inches(0.37),Inches(5.1),Inches(0.4),body,font=BODY,size=9,color=MUTED,ls=1.2)
    rect(s,tx+Inches(6.15),ry+Inches(0.21),Inches(1.15),Inches(0.36),BRAND_LITE,rounded=True)
    text(s,tx+Inches(6.15),ry+Inches(0.21),Inches(1.15),Inches(0.36),vol,font=HEAD,size=9.5,bold=True,color=BRAND,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    ry+=rh+Inches(0.1)
text(s,tx,ry+Inches(0.02),Inches(7.5),Inches(0.3),[("Anchor districts:  ",{'font':HEAD,'size':9.5,'bold':True,'color':DARK}),
     ("Gurugram (NH-48)  ·  SW Delhi (NH-48/44)  ·  Jaipur (NH-8)  ·  +10 exploratory cities",{'font':BODY,'size':9.5,'color':MUTED})])
# public dashboard reference card (browser frame; drop in live screenshot before circulation)
dcy=ry+Inches(0.38); dch=Inches(1.05)
rect(s,tx,dcy,Inches(7.5),dch,WHITE,line=BORDER,rounded=True)
rect(s,tx,dcy,Inches(7.5),Inches(0.32),BRAND_LITE,rounded=True)
for j,dc in enumerate((DANGER,WARNING,SUCCESS)):
    circle(s,tx+Inches(0.18)+j*Inches(0.18),dcy+Inches(0.11),Inches(0.1),dc)
text(s,tx+Inches(0.85),dcy+Inches(0.05),Inches(6.5),Inches(0.24),"crashfreeindia.org/rakshak/dashboard",font=BODY,size=9,color=MUTED)
icon(s,"bar-chart-3",tx+Inches(0.22),dcy+Inches(0.46),Inches(0.34),"#4A35FF")
text(s,tx+Inches(0.72),dcy+Inches(0.40),Inches(6.6),Inches(0.3),"Public accountability dashboard - the institutional spine",font=HEAD,size=10.5,bold=True,color=DARK)
text(s,tx+Inches(0.72),dcy+Inches(0.66),Inches(6.6),Inches(0.35),"Every site tracked in public: identification > audit > authority review > engineering implementation.  [Insert live dashboard screenshot before circulation]",font=BODY,size=8.8,italic=True,color=MUTED,ls=1.2)
bx=Inches(8.55); bw=SLIDE_W-bx-M_R
rect(s,bx,Inches(2.2),bw,Inches(4.5),BRAND,rounded=True)
text(s,bx+Inches(0.35),Inches(2.5),bw-Inches(0.7),Inches(0.3),"FY 2026-27 TARGETS",font=HEAD,size=10,bold=True,color=LAV,tracking=2.0)
tgts=[("150+","blackspots audited"),("100+","recommendations accepted"),("75+","implementations initiated"),("12+","DRSC presentations"),("v1.0","Rakshak Audit Manual + 4 Expert Consortium meetings")]
by=Inches(2.92)
for num,lab in tgts:
    text(s,bx+Inches(0.35),by,Inches(1.15),Inches(0.4),num,font=HEAD,size=17,bold=True,color=WHITE)
    text(s,bx+Inches(1.5),by+Inches(0.05),bw-Inches(1.9),Inches(0.5),lab,font=BODY,size=9.6,color=LAV,ls=1.15)
    by+=Inches(0.62)
hline(s,bx+Inches(0.35),Inches(6.12),bw-Inches(0.7),LAV_DK,1.0)
text(s,bx+Inches(0.35),Inches(6.26),bw-Inches(0.7),Inches(0.35),[("Budget  ",{'font':BODY,'size':10,'color':LAV}),("Rs 1.85 Cr",{'font':HEAD,'size':13,'bold':True,'color':WHITE})])
footer(s,7,TOTAL)

# ---------------- S8 H&R DEEP DIVE ----------------
s=new_slide()
sparkles_tr(s)
std_header(s,"DEEP DIVE  ·  CORE 02","Hit & Run Compensation:","fix two districts, map eight.")
tx=M_L; ty=Inches(2.2)
text(s,tx,ty,Inches(7.4),Inches(0.3),"FOUR PILLARS  ·  AUDIT-LED, RESEARCH-EMBEDDED",font=HEAD,size=10,bold=True,color=BRAND,tracking=2.0)
pillars=[("search","Scheme audit & process documentation","Stage-wise pipeline audit in Gurugram: FIR to GI Council disbursal; 20-30 claims tracked end-to-end."),
         ("landmark","Institutional capacity building","Fellow-in-Residence at Tehsildar office; SOP reference cards; training-gap assessment - research-embedded, not social work."),
         ("bot","Victim identification & AASHA","DLSA-partnered helpdesks; AASHA QR deployment at police stations and trauma centres; usage measured monthly."),
         ("file-text","Policy audit & advocacy","'Where the Pipeline Breaks' - comprehensive scheme audit submitted to MoRTH; quarterly findings + public brief.")]
ry=ty+Inches(0.4); rh=Inches(0.83)
for ic,t1,body in pillars:
    rect(s,tx,ry,Inches(7.5),rh,WHITE,line=BORDER,rounded=True)
    circle(s,tx+Inches(0.2),ry+Inches(0.19),Inches(0.44),BRAND_LITE)
    icon(s,ic,tx+Inches(0.29),ry+Inches(0.28),Inches(0.26),"#4A35FF")
    text(s,tx+Inches(0.82),ry+Inches(0.11),Inches(6.5),Inches(0.3),t1,font=HEAD,size=11,bold=True,color=DARK)
    text(s,tx+Inches(0.82),ry+Inches(0.38),Inches(6.5),Inches(0.42),body,font=BODY,size=9.2,color=MUTED,ls=1.2)
    ry+=rh+Inches(0.1)
text(s,tx,ry+Inches(0.05),Inches(7.5),Inches(0.55),[("Fix > pilot > map:  ",{'font':HEAD,'size':10,'bold':True,'color':DARK}),
     ("FIX Gurugram + SW Delhi (measured uptake lift)  ·  PILOT the playbook in Jaipur + watchlist districts  ·  MAP the claim process in 8+ districts by June 2027",{'font':BODY,'size':10,'color':MUTED})],ls=1.3)
bx=Inches(8.55); bw=SLIDE_W-bx-M_R
rect(s,bx,Inches(2.2),bw,Inches(4.5),BRAND,rounded=True)
text(s,bx+Inches(0.35),Inches(2.5),bw-Inches(0.7),Inches(0.3),"FY 2026-27 TARGETS",font=HEAD,size=10,bold=True,color=LAV,tracking=2.0)
tgts=[("2","districts FIXED - measured claim-uptake lift, -20% processing time"),("2+","districts PILOTING the fixed-pipeline playbook"),("8+","districts process-MAPPED by June 2027"),("20-30","claims tracked FIR to disbursal"),("1","scheme audit report to MoRTH (Apr-May '27)")]
by=Inches(2.92)
for num,lab in tgts:
    text(s,bx+Inches(0.35),by,Inches(1.15),Inches(0.4),num,font=HEAD,size=16,bold=True,color=WHITE)
    text(s,bx+Inches(1.5),by+Inches(0.04),bw-Inches(1.9),Inches(0.5),lab,font=BODY,size=9.4,color=LAV,ls=1.15)
    by+=Inches(0.62)
hline(s,bx+Inches(0.35),Inches(6.12),bw-Inches(0.7),LAV_DK,1.0)
text(s,bx+Inches(0.35),Inches(6.26),bw-Inches(0.7),Inches(0.35),[("Budget  ",{'font':BODY,'size':10,'color':LAV}),("Rs 0.60 Cr",{'font':HEAD,'size':13,'bold':True,'color':WHITE})])
footer(s,8,TOTAL)

# ---------------- S9 CIVIC & GOVTECH DEEP DIVE ----------------
s=new_slide()
sparkles_tr(s)
std_header(s,"DEEP DIVE  ·  CORE 03","Civic & GovTech: take SATARK","from 2 cities to 30.")
tx=M_L; ty=Inches(2.2)
text(s,tx,ty,Inches(7.5),Inches(0.3),"SATARK  ·  THE ENFORCEMENT CO-PILOT FOR TRAFFIC POLICE",font=HEAD,size=10,bold=True,color=BRAND,tracking=1.8)
pipe=["ANPR\nplate scan","ULIP\nvehicle records","SATARK\nrule engine","Billboard +\nofficer app","Interception\nlogged"]
pw=Inches(1.32); ph=Inches(0.66); pg=Inches(0.22); py=ty+Inches(0.38)
for i,pstep in enumerate(pipe):
    x=tx+i*(pw+pg)
    rect(s,x,py,pw,ph,BRAND_LITE,rounded=True)
    text(s,x,py,pw,ph,pstep,font=HEAD,size=8.2,bold=True,color=DARK,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE,ls=1.15)
    if i<4: icon(s,"chevron-right",x+pw+Inches(0.02),py+Inches(0.24),Inches(0.18),"#6A55FF")
text(s,tx,py+Inches(0.92),Inches(7.5),Inches(0.3),"PROVEN IN THE FIELD  ·  CUMULATIVE, LIVE DEPLOYMENTS",font=HEAD,size=10,bold=True,color=BRAND,tracking=1.8)
proof=[("3,00,000+","vehicles scanned at live sites"),("Rs 30 Cr+","pending challan value surfaced"),
       ("350+","vehicles intercepted in the field"),("2 cities","live today - Jaipur & Bengaluru")]
sw_=Inches(3.65); sh=Inches(0.78)
for i,(num,lab) in enumerate(proof):
    r_,c_=divmod(i,2)
    x=tx+c_*(sw_+Inches(0.2)); y=py+Inches(1.28)+r_*(sh+Inches(0.15))
    rect(s,x,y,sw_,sh,BRAND_LITE,rounded=True)
    text(s,x+Inches(0.22),y+Inches(0.10),sw_-Inches(0.44),Inches(0.35),num,font=HEAD,size=14.5,bold=True,color=BRAND)
    text(s,x+Inches(0.22),y+Inches(0.44),sw_-Inches(0.44),Inches(0.3),lab,font=BODY,size=8.8,color=MUTED,ls=1.15)
dy=py+Inches(3.14)
text(s,tx,dy,Inches(7.5),Inches(0.3),"BEYOND SATARK  ·  DATA STACK + GOVTECH EXPLORATION",font=HEAD,size=10,bold=True,color=BRAND,tracking=1.8)
text(s,tx,dy+Inches(0.28),Inches(7.6),Inches(0.55),"Sustain the four open data products: Defect Repository (daily, 146 districts) · Parliament tracker (1,423 questions) · SC Litigation Tracker · Crash Data Dashboard (CC-BY).\nScout the next govtech wedges: new digital public goods, state integrations, and partnerships across the ULIP / MoRTH ecosystem.",font=BODY,size=9.3,color=MUTED,ls=1.35)
bx=Inches(8.55); bw=SLIDE_W-bx-M_R
rect(s,bx,Inches(2.2),bw,Inches(4.5),BRAND,rounded=True)
text(s,bx+Inches(0.35),Inches(2.5),bw-Inches(0.7),Inches(0.3),"FY 2026-27 TARGETS",font=HEAD,size=10,bold=True,color=LAV,tracking=2.0)
tgts=[("30","cities live with SATARK - Gurugram, Pune & Ahmedabad first"),("1,000+","field interceptions logged - a floor, not a ceiling"),("4","open data products sustained & cited in DRSCs and press"),("2+","new govtech / DPG opportunities scoped with partners")]
by=Inches(2.95)
for num,lab in tgts:
    text(s,bx+Inches(0.35),by,Inches(1.35),Inches(0.4),num,font=HEAD,size=17,bold=True,color=WHITE)
    text(s,bx+Inches(1.75),by+Inches(0.05),bw-Inches(2.15),Inches(0.55),lab,font=BODY,size=9.4,color=LAV,ls=1.15)
    by+=Inches(0.72)
hline(s,bx+Inches(0.35),Inches(6.12),bw-Inches(0.7),LAV_DK,1.0)
text(s,bx+Inches(0.35),Inches(6.26),bw-Inches(0.7),Inches(0.35),[("Budget  ",{'font':BODY,'size':10,'color':LAV}),("Rs 1.00 Cr",{'font':HEAD,'size':13,'bold':True,'color':WHITE})])
footer(s,9,TOTAL)

# ---------------- S10 THE BETS ----------------
s=new_slide()
sparkles_tr(s)
std_header(s,"THE BETS","Two bets, seed-funded now -","scaled only if they earn it.",
           "School Safety and Gig Rider come out of the core budget this year. Each gets a Rs 0.10 Cr seed, released against a board-approved pilot design.")
betcards=[("BET 01","school","School Safety Index",
   "The 2,000-school, Rs 1.00 Cr index is parked, not killed.",
   "Validate the IRC:SP:32-2023 rubric (44 checks, 13 sections) on ~100 school zones in one anchor city; test the Zone Captain audit model end-to-end.",
   "A defensible per-school cost and rubric > board approves a funded, multi-city index in Year 3."),
  ("BET 02","bike","Gig Rider Safety",
   "The national study is parked until the field model is proven.",
   "Scoping study on gig rider crash data + first structured engagements with delivery platforms and OMI Foundation.",
   "3+ platforms at the table and a fundable study design > board approves the full programme in Year 3.")]
cw=Inches(5.86); ch=Inches(3.55); gx=Inches(0.2); ty=Inches(2.7)
for i,(kick,ic,t1,why,seed,gate) in enumerate(betcards):
    x=M_L+i*(cw+gx)
    rect(s,x,ty,cw,ch,BRAND_LITE,rounded=True)
    circle(s,x+Inches(0.3),ty+Inches(0.28),Inches(0.55),WHITE)
    icon(s,ic,x+Inches(0.42),ty+Inches(0.40),Inches(0.31),"#4A35FF")
    text(s,x+Inches(1.0),ty+Inches(0.30),Inches(3.5),Inches(0.25),kick+"  ·  RS 0.10 CR SEED",font=HEAD,size=8.6,bold=True,color=BRAND,tracking=1.5)
    text(s,x+Inches(1.0),ty+Inches(0.55),Inches(4.4),Inches(0.35),t1,font=HEAD,size=15,bold=True,color=DARK)
    text(s,x+Inches(0.3),ty+Inches(1.12),cw-Inches(0.6),Inches(0.3),why,font=BODY,size=9.5,italic=True,color=MUTED,ls=1.25)
    text(s,x+Inches(0.3),ty+Inches(1.58),Inches(1.2),Inches(0.25),"THE SEED",font=HEAD,size=8,bold=True,color=BRAND,tracking=1.6)
    text(s,x+Inches(0.3),ty+Inches(1.82),cw-Inches(0.6),Inches(0.75),seed,font=BODY,size=9.4,color=DARK,ls=1.28)
    text(s,x+Inches(0.3),ty+Inches(2.62),Inches(1.6),Inches(0.25),"THE GATE",font=HEAD,size=8,bold=True,color=BRAND,tracking=1.6)
    text(s,x+Inches(0.3),ty+Inches(2.86),cw-Inches(0.6),Inches(0.6),gate,font=BODY,size=9.4,color=DARK,ls=1.28)
rect(s,M_L,Inches(6.42),CONTENT_W,Inches(0.42),BRAND,rounded=True)
text(s,M_L,Inches(6.42),CONTENT_W,Inches(0.42),"Bets seed fund Rs 0.20 Cr total  ·  no seed released without a board-approved design  ·  a proven bet returns as a funded Year 3 programme",
     font=HEAD,size=10,bold=True,color=WHITE,align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
footer(s,10,TOTAL)

# ---------------- S11 KPI SCORECARD ----------------
s=new_slide()
sparkles_tr(s)
std_header(s,"OBJECTIVES & KPIs","One north star per programme,","measured quarterly.")
rows=[
 ("hard-hat","Project Rakshak","75+ implementations initiated","150+ audits · 100+ recommendations accepted · 12+ DRSC presentations · Audit Manual v1.0"),
 ("scale","Hit & Run Compensation","2 districts fixed, 8+ mapped","-20% median processing time · 20-30 claims tracked · pilots beyond model districts · audit report to MoRTH"),
 ("radar","Civic & GovTech","SATARK live in 30 cities","1,000+ interceptions logged · 4 open data products cited in DRSCs & press · 2+ new govtech opportunities scoped"),
 ("sprout","Bets (SSI + Gig Rider)","2 board-ready pilot designs","SSI rubric validated on ~100 schools · gig scoping study · 3+ platform engagements · seed released only on approval"),
 ("megaphone","Campaign & Comms","1M+ engaged via 'Safety is the New Swag'","50 micro-influencers · OOH in 3-4 cities · monthly field notes · quarterly findings · year-end reports"),
]
ry=Inches(2.15); rh=Inches(0.87); gap=Inches(0.09)
for ic,name,ns,supp in rows:
    rect(s,M_L,ry,CONTENT_W,rh,WHITE,line=BORDER,rounded=True)
    circle(s,M_L+Inches(0.22),ry+Inches(0.21),Inches(0.44),BRAND_LITE)
    icon(s,ic,M_L+Inches(0.31),ry+Inches(0.30),Inches(0.26),"#4A35FF")
    text(s,M_L+Inches(0.85),ry+Inches(0.16),Inches(2.35),Inches(0.6),name,font=HEAD,size=11.5,bold=True,color=DARK,ls=1.1)
    text(s,M_L+Inches(3.3),ry+Inches(0.12),Inches(0.95),Inches(0.3),"NORTH STAR",font=HEAD,size=7.5,bold=True,color=BRAND,tracking=1.4)
    text(s,M_L+Inches(3.3),ry+Inches(0.36),Inches(3.6),Inches(0.45),ns,font=BODY,size=10,bold=True,color=DARK,ls=1.15)
    text(s,M_L+Inches(7.15),ry+Inches(0.12),Inches(1.2),Inches(0.3),"SUPPORTING",font=HEAD,size=7.5,bold=True,color=MUTED,tracking=1.4)
    text(s,M_L+Inches(7.15),ry+Inches(0.36),Inches(4.6),Inches(0.48),supp,font=BODY,size=8.8,color=MUTED,ls=1.2)
    ry+=rh+gap
footer(s,11,TOTAL)

# ---------------- S12 GANTT ----------------
s=new_slide()
sparkles_tr(s)
std_header(s,"TIMELINE","Twelve months,","phased by quarter.")
months=["Jul","Aug","Sep","Oct","Nov","Dec","Jan","Feb","Mar","Apr","May","Jun"]
gx0=Inches(3.35); gw=Inches(9.25); ty=Inches(2.2)
mw=gw/12
for i,m in enumerate(months):
    text(s,gx0+i*mw,ty,mw,Inches(0.25),m,font=HEAD,size=8.5,bold=True,color=MUTED,align=PP_ALIGN.CENTER)
for qi in (0,3,6,9,12):
    ln=s.shapes.add_connector(1,gx0+qi*mw,ty+Inches(0.3),gx0+qi*mw,Inches(6.7))
    ln.line.color.rgb=BORDER; ln.line.width=Pt(0.75)
bars=[
 ("PROJECT RAKSHAK","Ignition: empanelment & onboarding",0,2,BRAND),
 ("","Audit waves (Tracks A/B/C)",1,8,BRAND),
 ("","DRSC submissions & tracking",3,11,BRAND),
 ("","Finale + Audit Manual v1.0",9,11,BRAND),
 ("HIT & RUN","Fix: district integration & scheme audit",0,4,BRAND),
 ("","Pilot + map wave (8+ districts)",4,9,BRAND),
 ("","Accountability: report to MoRTH",6,11,BRAND),
 ("CIVIC & GOVTECH","SATARK: Gurugram, Pune, Ahmedabad go-lives",0,5,BRAND),
 ("","SATARK: scale wave to 30 cities",5,11,BRAND),
 ("","Data stack + govtech exploration",0,11,BRAND),
 ("BETS (SEED)","SSI: rubric pilot on ~100 schools",3,9,BRAND),
 ("","Gig: scoping study & platform talks",3,8,BRAND),
 ("CAMPAIGN","'Safety is the New Swag' build > peak",3,11,BRAND),
]
ry=ty+Inches(0.32); rh=Inches(0.235); gap=Inches(0.06)
prev_group=None
for grp,label,m0,m1,col in bars:
    if grp and grp!=prev_group and prev_group is not None:
        ry+=Inches(0.06)
    if grp:
        text(s,M_L,ry-Inches(0.01),Inches(2.6),Inches(0.25),grp,font=HEAD,size=8,bold=True,color=BRAND,tracking=1.2)
        prev_group=grp
    bar=rect(s,gx0+m0*mw+Inches(0.03),ry,(m1-m0+1)*mw-Inches(0.06),rh,BRAND_LITE,rounded=True)
    text(s,gx0+m0*mw+Inches(0.15),ry+Inches(0.015),(m1-m0+1)*mw-Inches(0.25),Inches(0.22),label,font=BODY,size=8.3,color=DARK,ls=1.0)
    ry+=rh+gap
text(s,M_L,Inches(6.68),CONTENT_W,Inches(0.3),"Running through every month: monthly field notes  ·  quarterly audit findings  ·  Expert Consortium meetings (Sep / Dec / Mar / Jun)",font=BODY,size=9.5,italic=True,color=MUTED)
footer(s,12,TOTAL)

# ---------------- S13 BUDGET ----------------
s=new_slide()
sparkles_tr(s)
std_header(s,"BUDGET","Rs 6.00 Cr,","71% into programmes.")
alloc=[("Project Rakshak",185),("Trust Admin",151),("Civic & GovTech (SATARK)",100),
       ("Hit & Run Compensation",60),("Marketing Campaign",60),("Contingency (4%)",24),("Bets seed fund (SSI + Gig)",20)]
maxv=185; bx0=Inches(3.5); bmax=Inches(4.7)
ry=Inches(2.35)
for name,v in alloc:
    text(s,M_L,ry,Inches(2.7),Inches(0.3),name,font=BODY,size=10.5,color=DARK,anchor=MSO_ANCHOR.MIDDLE)
    w=int(bmax*(v/maxv))
    rect(s,bx0,ry+Inches(0.02),w,Inches(0.3),BRAND if name!="Contingency (4%)" else LAV_DK,rounded=True)
    text(s,bx0+w+Inches(0.12),ry,Inches(1.6),Inches(0.3),f"Rs {v/100:.2f} Cr",font=HEAD,size=10.5,bold=True,color=BRAND,anchor=MSO_ANCHOR.MIDDLE)
    ry+=Inches(0.55)
text(s,M_L,ry+Inches(0.12),Inches(8.2),Inches(0.4),"Programme spend Rs 4.25 Cr (71%)  ·  Trust Admin Rs 1.51 Cr (25%)  ·  Contingency Rs 0.24 Cr (4%)  ·  bets held to stage-gated seed funding",font=BODY,size=10,italic=True,color=MUTED,ls=1.3)
bx=Inches(9.3); bw=SLIDE_W-bx-M_R
rect(s,bx,Inches(2.2),bw,Inches(4.5),BRAND,rounded=True)
text(s,bx+Inches(0.35),Inches(2.5),bw-Inches(0.7),Inches(0.3),"QUARTERLY PHASING",font=HEAD,size=10,bold=True,color=LAV,tracking=2.0)
qs=[("Q1  Jul-Sep","Rs 1.23 Cr"),("Q2  Oct-Dec","Rs 1.61 Cr"),("Q3  Jan-Mar","Rs 1.65 Cr"),("Q4  Apr-Jun","Rs 1.52 Cr")]
by=Inches(2.95)
for q,v in qs:
    text(s,bx+Inches(0.35),by,Inches(1.6),Inches(0.3),q,font=BODY,size=10,color=LAV)
    text(s,bx+Inches(0.35),by+Inches(0.24),Inches(2.5),Inches(0.4),v,font=HEAD,size=16,bold=True,color=WHITE)
    by+=Inches(0.72)
hline(s,bx+Inches(0.35),Inches(6.0),bw-Inches(0.7),LAV_DK,1.0)
text(s,bx+Inches(0.35),Inches(6.12),bw-Inches(0.7),Inches(0.5),"Detail in the AOP budget\nworkbook (v4, formula-driven).",font=BODY,size=9,color=LAV,ls=1.25)
footer(s,13,TOTAL)

# ---------------- S14 ENABLERS ----------------
s=new_slide()
sparkles_tr(s)
std_header(s,"ENABLERS","The campaign and the backbone","behind the plan.")
tx=M_L; ty=Inches(2.2)
text(s,tx,ty,Inches(7.4),Inches(0.3),"SAFETY IS THE NEW SWAG  ·  Rs 0.60 CR CAMPAIGN",font=HEAD,size=10,bold=True,color=BRAND,tracking=1.8)
camp=[("clapperboard","Media advocacy","Editorial partnerships, radio & podcast integration, PSA distribution"),
      ("play","Digital advocacy","50 micro-influencers, branded short films, #SafeSwag digital IPs"),
      ("map-pin","Offline awareness","OOH in 3-4 cities, guerilla installations, event co-branding"),
      ("users","Community mobilization","College competitions, app-based engagement, real-life stories")]
cw=Inches(3.62); chh=Inches(1.62); gx=Inches(0.22); gy=Inches(0.2)
for i,(ic,t1,body) in enumerate(camp):
    r_,c_=divmod(i,2)
    x=tx+c_*(cw+gx); y=ty+Inches(0.4)+r_*(chh+gy)
    rect(s,x,y,cw,chh,BRAND_LITE,rounded=True)
    icon(s,ic,x+Inches(0.25),y+Inches(0.25),Inches(0.32),"#4A35FF")
    text(s,x+Inches(0.72),y+Inches(0.24),cw-Inches(1.0),Inches(0.3),t1,font=HEAD,size=11.5,bold=True,color=DARK)
    text(s,x+Inches(0.25),y+Inches(0.68),cw-Inches(0.5),Inches(0.85),body,font=BODY,size=9.3,color=MUTED,ls=1.3)
text(s,tx,ty+Inches(4.15),Inches(7.4),Inches(0.5),"All four campaign pillars are now funded lines (the prior draft budgeted only one of four).",font=BODY,size=9.5,italic=True,color=MUTED,ls=1.3)
bx=Inches(8.55); bw=SLIDE_W-bx-M_R
rect(s,bx,Inches(2.2),bw,Inches(4.5),BRAND,rounded=True)
text(s,bx+Inches(0.35),Inches(2.5),bw-Inches(0.7),Inches(0.3),"ORG BACKBONE  ·  RS 1.51 CR",font=HEAD,size=10,bold=True,color=LAV,tracking=1.8)
org=[("users-round","Core team salaries & benefits - Rs 0.78 Cr"),
     ("landmark","IRSC institutional support & expert consultation - Rs 0.42 Cr"),
     ("bot","IT, SaaS & AI tooling (Workspace, Slack, Claude) - Rs 0.14 Cr"),
     ("clipboard-check","M&E, statutory & impact audit - Rs 0.06 Cr"),
     ("briefcase","Travel, branding, compliance - Rs 0.11 Cr")]
by=Inches(3.0)
for ic,lab in org:
    icon(s,ic,bx+Inches(0.35),by,Inches(0.28),"#C8C0FF")
    text(s,bx+Inches(0.78),by-Inches(0.02),bw-Inches(1.15),Inches(0.55),lab,font=BODY,size=9.6,color=WHITE,ls=1.2)
    by+=Inches(0.68)
footer(s,14,TOTAL)

# ---------------- S15 CLOSE ----------------
s=new_slide(BRAND)
sparkle(s,Inches(12.30),Inches(0.35),Inches(0.55),LAV)
sparkle(s,Inches(11.95),Inches(0.80),Inches(0.32),LAV)
wordmark(s,M_L,Inches(0.6),dark_bg=True)
eyebrow(s,M_L,Inches(1.7),"WHAT SUCCESS LOOKS LIKE  ·  JUNE 2027",color=LAV)
text(s,M_L,Inches(2.05),Inches(11),Inches(0.7),"Systems work because",font=HEAD,size=32,bold=True,color=WHITE,ls=1.05)
text(s,M_L,Inches(2.65),Inches(11),Inches(0.7),"we hold them accountable.",font=HEAD,size=32,bold=True,color=LAV,ls=1.05)
wins=["Rakshak running inside institutions: consortium, Audit Manual v1.0, and a public dashboard tracking 75+ implementations",
      "Claim pipeline fixed in two districts, piloted beyond them, and mapped in 8+ - a replication playbook, not a project",
      "SATARK live in 30 cities, 1,000+ interceptions logged, and a govtech pipeline positioning CFI as government's road-safety data layer",
      "Two board-ready pilot designs that decide whether School Safety and Gig Rider become funded Year 3 programmes",
      "An Expert Consortium, an Audit Manual, and a publishing cadence that outlive any single cohort"]
by=Inches(3.6)
for w in wins:
    circle(s,M_L,by+Inches(0.03),Inches(0.3),WHITE)
    icon(s,"check",M_L+Inches(0.05),by+Inches(0.08),Inches(0.2),"#4A35FF",sw=3.0)
    text(s,M_L+Inches(0.5),by,Inches(11.3),Inches(0.5),w,font=BODY,size=12,color=WHITE,ls=1.25)
    by+=Inches(0.62)
text(s,M_L,Inches(7.0),Inches(11),Inches(0.3),"CRASHFREE INDIA  ·  AOP 2026-27  ·  INTERNAL PLANNING DOCUMENT",font=HEAD,size=8.5,bold=True,color=LAV,tracking=1.8)

prs.save("CFI_AOP_2026-27.pptx")
print("slides:",len(prs.slides._sldIdLst))

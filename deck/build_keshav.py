#!/usr/bin/env python3
"""CFI AOP 2026-27 — FLAT, pivot-ready bifurcation for finance (Keshav)."""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.table import Table, TableStyleInfo

INDIGO="4A35FF"; INK="1A1C1C"; MUT="777589"; MIST="EDEEF2"; TINT="F3F1FF"
BAND="FAFAFB"; WHITE="FFFFFF"; GREEN="0A9955"; AMBER="E58900"
RUPEE='"₹"#,##0'
thin=Side(style="thin", color="E2E3EC"); border=Border(left=thin,right=thin,top=thin,bottom=thin)

# Flat rows: (Vertical, Category, Sub-category, Description, Budget, Remarks for Keshav)
ROWS = [
 # ---------------- PROJECT RAKSHAK (1.85 Cr) ----------------
 ("Project Rakshak","Institutional track (IIT/NIT/SPA teams)","Student team stipends","₹36,000 per team on completion · ~90 institutional sites",3240000,
  "GL: Salary & Incentives (stipends). Milestone-linked (paid on completion) — accrue quarterly, release on sign-off. Volume driver = # teams; true-up to actual cohort. Confirm TDS applicability on student stipends with CA. Programme (restricted)."),
 ("Project Rakshak","Institutional track (IIT/NIT/SPA teams)","Expert mentor honoraria","Faculty & road-safety expert mentors across the cohort",1300000,
  "GL: Professional fees. TDS u/s 194J (10%). Per-session/per-mentor — keep engagement letters. Programme."),
 ("Project Rakshak","Institutional track (IIT/NIT/SPA teams)","Campus outreach, onboarding & merchandise","Chapter mobilisation, IDs, kits, ads",960000,
  "GL: Marketing & Branding + Office. Mixed (printing/merch + digital ads + travel). Claim GST input where invoiced. Split ads vs merch if you want a finer tag."),
 ("Project Rakshak","NGO partner track (~20 sites)","NGO field-team engagement","Field audits via NGO partners, ~20 sites",2000000,
  "GL: Professional fees / grant-to-partner. Contract per NGO — confirm TDS 194C vs grant treatment. Milestone-linked per site. Restricted programme."),
 ("Project Rakshak","NGO partner track (~20 sites)","CFI desk + 10–15% physical re-checks","QA on NGO submissions",500000,
  "GL: Travel + Professional fees. Mostly CFI staff time + travel — book travel to Travel head; staff time is an allocation, not a new payout."),
 ("Project Rakshak","Certified RSA track (~40 sites)","CRRI-certified auditor fees (IRC SP:88)","Full audits usable by NHAI without rework",4500000,
  "GL: Professional fees. Largest single vendor line. TDS 194J + GST input. Milestone/per-audit — keep PO + IRC SP:88 deliverable. Programme."),
 ("Project Rakshak","Expert Consortium & Audit Manual v1.0","Expert Consortium (4 meetings)","Sep/Dec/Mar/Jun sittings",1000000,
  "GL: Professional fees (honoraria, 194J) + Travel + Office (venue). Accrue per meeting (4 across year)."),
 ("Project Rakshak","Expert Consortium & Audit Manual v1.0","Audit Manual v1.0 production","Authoring, design, print",800000,
  "GL: Professional fees (authoring/design) + print. Treat as programme opex. GST input on printing. Mostly one-time."),
 ("Project Rakshak","Public accountability dashboard","Dashboard build, hosting & maintenance","identification→audit→review→implementation tracker",1200000,
  "GL: Tech Infra. Split build (one-time) vs hosting (recurring monthly). If built in-house it is staff time — confirm vendor vs internal to avoid double counting."),
 ("Project Rakshak","Programme management & field ops","Programme management (staff allocation)","PM + coordination time allocated to Rakshak",1800000,
  "GL: Salary & Incentives — ALLOCATION, not a new payout. This is core salary cross-charged to Rakshak; make sure it is NOT also sitting in Trust Admin salaries (avoid double count)."),
 ("Project Rakshak","Programme management & field ops","Field travel & logistics","Site visits, DRSC meetings",700000,
  "GL: Travel. Reimbursements — keep bills, no TDS. Programme."),
 ("Project Rakshak","Programme management & field ops","National forum & DRSC presentations","12+ DRSC presentations, year-end forum",500000,
  "GL: Marketing/Events + Travel. Venue & logistics — GST input on vendor invoices."),
 # ---------------- HIT & RUN COMPENSATION (0.60 Cr) ----------------
 ("Hit & Run Compensation","Scheme audit & process documentation","Stage-wise pipeline audit fieldwork (Gurugram)","FIR→GI Council disbursal; 20–30 claims tracked",1200000,
  "GL: Professional fees + Travel. Field researchers/surveyors — TDS 194C/194J per contract. Restricted programme."),
 ("Hit & Run Compensation","Scheme audit & process documentation","'Where the Pipeline Breaks' report","Scheme audit submitted to MoRTH",600000,
  "GL: Professional fees + print. Writing/design + printing. GST input."),
 ("Hit & Run Compensation","Institutional capacity building","Fellow-in-Residence stipend (Tehsildar office)","Embedded fellow · research-embedded",1200000,
  "GL: Salary & Incentives (fellowship). On HRMS retainer — recurring monthly, TDS on salary as applicable. Tag to Hit & Run (dedicated fellow)."),
 ("Hit & Run Compensation","Institutional capacity building","SOP reference cards & training-gap assessment","District capacity building",800000,
  "GL: Professional fees + print. Consultant + printing. Mostly one-time."),
 ("Hit & Run Compensation","Victim identification & AASHA","DLSA-partnered helpdesks","Trauma-ward legal helpdesks",800000,
  "GL: Professional fees / grant + Office. Helpdesk staffing + materials. Confirm DLSA MoU terms."),
 ("Hit & Run Compensation","Victim identification & AASHA","AASHA QR deployment","Police stations & trauma centres; usage measured monthly",600000,
  "GL: Tech Infra + Marketing. QR standees/printing + app hosting — split print vs tech if you want."),
 ("Hit & Run Compensation","Policy audit & advocacy","Quarterly findings & public brief","Publishing cadence",500000,
  "GL: Professional fees + Marketing. Recurring quarterly — accrue per quarter."),
 ("Hit & Run Compensation","Policy audit & advocacy","Advocacy & MoRTH engagement travel","Stakeholder engagement",300000,
  "GL: Travel. Reimbursements, no TDS."),
 # ---------------- CIVIC & GOVTECH / SATARK (1.00 Cr) ----------------
 ("Civic & GovTech (SATARK)","SATARK scale to 30 cities","SATARK engineering & product","ANPR, ULIP, rule engine, billboard + officer app",2500000,
  "GL: Tech Infra / Professional fees. In-house devs = salary cross-charge (avoid double count); vendor = 194J + GST. Confirm capex vs opex for product build with CA."),
 ("Civic & GovTech (SATARK)","SATARK scale to 30 cities","City deployment & rollout","Toward 30 cities · Gurugram, Pune, Ahmedabad first",2000000,
  "GL: Professional fees + Travel + Tech. Volume driver = # cities; milestone per go-live."),
 ("Civic & GovTech (SATARK)","SATARK scale to 30 cities","Cloud, ANPR & ULIP integration","Compute, APIs, camera integration",1500000,
  "GL: Tech Infra. Recurring cloud/compute — reconcile monthly to actual usage. Foreign SaaS → GST under RCM (import of service); watch forex."),
 ("Civic & GovTech (SATARK)","Open data stack (4 products)","Open data product maintenance & hosting","Defect Repo, Parliament tracker, SC Litigation Tracker, Crash Dashboard",1500000,
  "GL: Tech Infra. Recurring hosting for 4 products — monthly."),
 ("Civic & GovTech (SATARK)","Open data stack (4 products)","Data engineering & updates","Daily/weekly refresh, 146 districts",1000000,
  "GL: Salary / Professional fees. Cross-charge if internal; vendor = 194J."),
 ("Civic & GovTech (SATARK)","GovTech exploration & partnerships","GovTech scoping & partnerships","2+ new DPG opportunities scoped",1000000,
  "GL: Professional fees + Travel. Exploratory/flexible — keep unspent visible; do not front-load."),
 ("Civic & GovTech (SATARK)","GovTech exploration & partnerships","Pilot / DPG prototyping","ULIP / MoRTH ecosystem",500000,
  "GL: Tech Infra. Small pilots — release against scoped need."),
 # ---------------- MARKETING CAMPAIGN (0.60 Cr) ----------------
 ("Marketing Campaign","Media advocacy","Editorial partnerships, radio & podcast, PSA","Earned + owned media",1500000,
  "GL: Marketing & Branding. Agency/media invoices — TDS 194C/194J + GST input. Spread across year."),
 ("Marketing Campaign","Digital advocacy","50 micro-influencers & branded short films","#SafeSwag creator programme",1400000,
  "GL: Marketing & Branding. Influencer payouts — 194C/194J; keep contracts. Track CAC (see Aug ads learning)."),
 ("Marketing Campaign","Digital advocacy","Digital IP & content production","Short films, reels",600000,
  "GL: Marketing & Branding. Production vendor + GST input."),
 ("Marketing Campaign","Offline awareness","OOH in 3–4 cities","Billboards, transit",1000000,
  "GL: Marketing & Branding. OOH media buy — 194C + GST input."),
 ("Marketing Campaign","Offline awareness","Guerilla installations & event co-branding","",500000,
  "GL: Marketing & Branding / Events."),
 ("Marketing Campaign","Community mobilization","College competitions & app-based engagement","Real-life stories",1000000,
  "GL: Marketing + Office. Prizes/logistics — keep winner records for prize payouts."),
 # ---------------- BETS (0.20 Cr) ----------------
 ("Bets (SSI + Gig Rider)","School Safety Index — seed (₹0.10 Cr)","IRC:SP:32 rubric validation & Zone Captain pilot","~100 school zones in one anchor city",700000,
  "GL: Professional fees + Travel. SEED — release ONLY against board-approved design (stage gate). Ring-fence at ₹0.10 Cr; do not overspend the seed."),
 ("Bets (SSI + Gig Rider)","School Safety Index — seed (₹0.10 Cr)","Per-school costing & board-ready design","Gate to a funded multi-city index in Year 3",300000,
  "GL: Professional fees. SEED. Deliverable = board paper."),
 ("Bets (SSI + Gig Rider)","Gig Rider Safety — seed (₹0.10 Cr)","Gig crash-data scoping study","National study parked until field model proven",600000,
  "GL: Professional fees. SEED — researcher fees 194J. Ring-fence at ₹0.10 Cr."),
 ("Bets (SSI + Gig Rider)","Gig Rider Safety — seed (₹0.10 Cr)","Platform + OMI Foundation engagements","3+ platforms at the table",400000,
  "GL: Travel + Professional fees. SEED. Relationship-building."),
 # ---------------- TRUST ADMIN / ORG BACKBONE (1.51 Cr) ----------------
 ("Trust Admin (Org Backbone)","Core team salaries & benefits","Core team salaries & benefits","Aggregate core staff (individual figures withheld)",4200000,
  "GL: Salary & Incentives. Core/shared payroll ONLY (the part not cross-charged to programmes). Ensure programme staff-allocations (Rakshak PM ₹18L, SATARK eng, data eng) are NOT double-counted here. Monthly; TDS 192, PF/ESI as applicable."),
 ("Trust Admin (Org Backbone)","Core team salaries & benefits","Safer Mobility Impact Fellowship (SMIF)","Fellow cohort, aggregate (~6 fellows across tracks)",3600000,
  "GL: Salary & Incentives (fellowship). Via HRMS fixed-term agreements. Recurring monthly. Individual amounts are confidential (pull from HRMS). If a fellow is dedicated to one programme, consider cross-charging that programme."),
 ("Trust Admin (Org Backbone)","IRSC institutional support & expert consultation","IRSC institutional support & expert consultation","Shared expert / leadership consultation",4200000,
  "GL: Professional fees. TDS 194J + GST. IRSC is a related party — confirm inter-entity treatment & documentation. Keep MoU."),
 ("Trust Admin (Org Backbone)","IT, SaaS & AI tooling","AI tooling — Claude (Team) + Codex / AI subscriptions","AI assistants for build, research & ops",600000,
  "GL: Tech Infra (software subscriptions). ← THE dedicated AI-tooling tag. Recurring monthly, mostly USD (Anthropic/OpenAI) — GST under RCM on import of service (pay & claim), plus forex/card fees. Receipts already forwarded to finance."),
 ("Trust Admin (Org Backbone)","IT, SaaS & AI tooling","Google Workspace & email","",300000,
  "GL: Tech Infra. Recurring per-seat — scales with headcount. USD/INR; RCM watch."),
 ("Trust Admin (Org Backbone)","IT, SaaS & AI tooling","Slack & collaboration","",200000,
  "GL: Tech Infra. Recurring per-seat. RCM watch."),
 ("Trust Admin (Org Backbone)","IT, SaaS & AI tooling","HRMS 'CFI People' & other SaaS","",200000,
  "GL: Tech Infra. HRMS + misc SaaS. Recurring."),
 ("Trust Admin (Org Backbone)","IT, SaaS & AI tooling","Cloud, hosting & domains","Not tied to a specific product",100000,
  "GL: Tech Infra. Domains/hosting. Recurring."),
 ("Trust Admin (Org Backbone)","M&E, statutory & impact audit","M&E, statutory & impact audit","",600000,
  "GL: Audit & Compliance. Statutory audit + M&E — 194J. Year-end weighted."),
 ("Trust Admin (Org Backbone)","Travel, branding & compliance","Travel, branding & compliance","",1100000,
  "GL: mixed (Travel + Marketing + Compliance). Consider splitting into 3 lines if you want cleaner pivots by cost head."),
 # ---------------- CONTINGENCY (0.24 Cr) ----------------
 ("Contingency (4%)","Contingency","Contingency reserve (4%)","Held against programme + admin spend",2400000,
  "GL: Contingency (do NOT pre-allocate). Release only on approved overruns and RE-TAG to the actual head when spent. Keep as buffer; report unused at year-end."),
]

assert sum(r[4] for r in ROWS)==60000000, sum(r[4] for r in ROWS)

wb=Workbook()

# ============ Sheet 1: flat pivot-ready table ============
ws=wb.active; ws.title="AOP Bifurcation"
heads=["Vertical","Category","Sub-category","Description","Budget allocated","Remarks for Keshav (tagging & finance notes)"]
for j,h in enumerate(heads,1):
    c=ws.cell(row=1,column=j,value=h); c.font=Font(name="Calibri",size=10,bold=True,color=WHITE)
    c.fill=PatternFill("solid",fgColor=INDIGO); c.alignment=Alignment(horizontal="center",vertical="center",wrap_text=True); c.border=border
ws.row_dimensions[1].height=30
for i,(v,cat,sub,desc,amt,rem) in enumerate(ROWS):
    r=i+2; fill=WHITE if i%2==0 else BAND
    def put(col,val,align="left",fmt=None,size=9.5,color=INK,bold=False,wrap=True):
        cc=ws.cell(row=r,column=col,value=val); cc.font=Font(name="Calibri",size=size,bold=bold,color=color)
        cc.alignment=Alignment(horizontal=align,vertical="top",wrap_text=wrap); cc.fill=PatternFill("solid",fgColor=fill); cc.border=border
        if fmt: cc.number_format=fmt
    put(1,v,bold=True); put(2,cat); put(3,sub,color=INK,bold=False); put(4,desc,size=9,color=MUT)
    put(5,amt,align="right",fmt=RUPEE,wrap=False,bold=True)
    put(6,rem,size=8.5,color=INK)
last=len(ROWS)+1
# AutoFilter + table for easy pivoting
ws.auto_filter.ref=f"A1:F{last}"
for col,w in zip("ABCDEF",[22,32,34,40,15,66]): ws.column_dimensions[col].width=w
ws.freeze_panes="A2"

# ============ Sheet 2: Check & quick summaries ============
wc=wb.create_sheet("Check & summaries")
wc.sheet_view.showGridLines=False
DB=f"'AOP Bifurcation'!$E$2:$E${last}"; DV=f"'AOP Bifurcation'!$A$2:$A${last}"; DC=f"'AOP Bifurcation'!$B$2:$B${last}"
def title(cell,txt,fill=INDIGO,size=11):
    c=wc[cell]; c.value=txt; c.font=Font(bold=True,color=WHITE,size=size); c.fill=PatternFill("solid",fgColor=fill); c.alignment=Alignment(horizontal="left",vertical="center")
wc.merge_cells("A1:C1"); title("A1","Reconciliation (this ties to the AOP — ₹6.00 Cr)")
wc.row_dimensions[1].height=24
wc["A2"]="Grand total"; wc["A2"].font=Font(bold=True)
wc["B2"]=f"=SUM({DB})"; wc["B2"].number_format=RUPEE; wc["B2"].font=Font(bold=True)
wc["C2"]="should be ₹6,00,00,000"; wc["C2"].font=Font(color=MUT,size=9)
# by vertical
verts=[]
for v,*_ in ROWS:
    if v not in verts: verts.append(v)
wc.merge_cells("A4:C4"); title("A4","By Vertical (Level 1)",fill=INK,size=10)
r=5
for v in verts:
    wc.cell(row=r,column=1,value=v).font=Font(size=10)
    b=wc.cell(row=r,column=2,value=f"=SUMIF({DV},A{r},{DB})"); b.number_format=RUPEE
    p=wc.cell(row=r,column=3,value=f"=B{r}/$B$2"); p.number_format='0.0%'; p.font=Font(color=MUT,size=9)
    r+=1
wc.cell(row=r,column=1,value="Total").font=Font(bold=True)
wc.cell(row=r,column=2,value=f"=SUM(B5:B{r-1})").number_format=RUPEE; wc.cell(row=r,column=2).font=Font(bold=True)
for col,w in zip("ABC",[34,16,20]): wc.column_dimensions[col].width=w

# ============ Sheet 3: Read me ============
wr=wb.create_sheet("Read me")
wr.sheet_view.showGridLines=False; wr.column_dimensions["A"].width=118
lines=[
 ("CFI · AOP 2026–27 — bifurcation for finance (flat, pivot-ready)",INDIGO,13,True),
 ("",WHITE,10,False),
 ("HOW TO USE",GREEN,11,True),
 ("• Sheet 'AOP Bifurcation' is a clean flat table (one row per sub-category). Select it and Insert ▸ PivotTable.",INK,10,False),
 ("• Pivot rows: Vertical ▸ Category ▸ Sub-category; Values: Sum of Budget allocated. Filters as needed.",INK,10,False),
 ("• Vertical and Category repeat on every row on purpose — that is what makes pivots work.",INK,10,False),
 ("• 'Check & summaries' proves it reconciles to ₹6.00 Cr and gives a by-vertical view.",INK,10,False),
 ("",WHITE,10,False),
 ("WHAT'S EXACT vs FIRST-PASS",AMBER,11,True),
 ("• EXACT (board-approved AOP): the 7 verticals and their totals — Rakshak ₹1.85 Cr, Hit & Run ₹0.60 Cr,",INK,10,False),
 ("   SATARK ₹1.00 Cr, Marketing ₹0.60 Cr, Bets ₹0.20 Cr, Trust Admin ₹1.51 Cr, Contingency ₹0.24 Cr = ₹6.00 Cr;",INK,10,False),
 ("   plus Trust Admin's five headers (salaries ₹0.78 Cr, IRSC ₹0.42 Cr, IT/SaaS/AI ₹0.14 Cr, M&E ₹0.06 Cr, travel ₹0.11 Cr).",INK,10,False),
 ("• FIRST-PASS (edit freely): the Category/Sub-category splits inside the programmes, the ₹42L core vs ₹36L SMIF split,",INK,10,False),
 ("   and the itemisation of the ₹0.14 Cr AI/SaaS line. Numbers were set to sum exactly to each vertical.",INK,10,False),
 ("",WHITE,10,False),
 ("FOR KESHAV — the Remarks column",INDIGO,11,True),
 ("• Each row suggests a GL head (Salary & Incentives, Professional fees, Tech Infra, Marketing & Branding, Travel,",INK,10,False),
 ("   Audit & Compliance, Office, Contingency), plus TDS/GST/RCM flags and whether it is recurring vs one-time.",INK,10,False),
 ("• Watch the double-count flags: programme 'staff allocation' lines are cross-charges from core salaries — do not book twice.",INK,10,False),
 ("• Foreign SaaS/AI (Claude, Codex, Workspace, Slack) → GST under reverse charge on import of service; keep receipts.",INK,10,False),
 ("• Fellows are visible in three places: Rakshak student stipends (₹36k/team), Hit&Run Fellow-in-Residence, and SMIF (Trust Admin).",INK,10,False),
 ("• Want a 7th 'GL head' column so you can pivot by cost head directly? Say the word and I'll add it (kept to your 6 columns for now).",MUT,9,False),
 ("",WHITE,10,False),
 ("Sources: finalized AOP deck (₹6.00 Cr) · Team Charter / Ownership Map · Slack · Gmail (Anthropic receipts, SMIF, Codex request).",MUT,9,False),
]
for i,(t,c,s,b) in enumerate(lines,1):
    cc=wr.cell(row=i,column=1,value=t); cc.font=Font(name="Calibri",size=s,bold=b,color=c); cc.alignment=Alignment(horizontal="left",vertical="center")

out="CFI_AOP_Bifurcation-for-Finance_v2_2026-08-19.xlsx"
wb.save(out)
print("saved",out,"| rows:",len(ROWS),"| total:",sum(r[4] for r in ROWS))

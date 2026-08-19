#!/usr/bin/env python3
"""CFI AOP 2026-27 — project-wise budget bifurcation from the ₹3.0 Cr line items."""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

INDIGO = "4A35FF"; INK = "1A1C1C"; MUT = "777589"; MIST = "EDEEF2"
TINT = "F3F1FF"; AMBER = "E58900"; GREEN = "0A9955"; WHITE = "FFFFFF"
RUPEE = '"₹"#,##0'
PCT = '0.0%'

thin = Side(style="thin", color="D8DAE5")
border = Border(left=thin, right=thin, top=thin, bottom=thin)

def hcell(c, txt, size=10, fill=INDIGO, color=WHITE, align="left", bold=True):
    c.value = txt
    c.font = Font(name="Calibri", size=size, bold=bold, color=color)
    c.fill = PatternFill("solid", fgColor=fill)
    c.alignment = Alignment(horizontal=align, vertical="center", wrap_text=True)
    c.border = border

def cell(c, val, size=10, color=INK, align="left", bold=False, fmt=None, fill=None, wrap=True):
    c.value = val
    c.font = Font(name="Calibri", size=size, bold=bold, color=color)
    c.alignment = Alignment(horizontal=align, vertical="center", wrap_text=wrap)
    c.border = border
    if fmt:
        c.number_format = fmt
    if fill:
        c.fill = PatternFill("solid", fgColor=fill)

# ---- master line items: (Vertical, Activity, Budget, Project, Note) ----
OB = "Org Backbone"
RK = "Project Rakshak"
ST = "Civic & GovTech (SATARK)"
CM = "Campaign & Comms"
BT = "Bets — New Products"
PO = "Policy & Advocacy"
HR = "Hit & Run Compensation"
GR = "Gig Rider Safety"
CO = "Contingency"

VERTICALS = ["Trust Admin", "Technology", "Education", "Enabler - Community Building",
             "Infrastructure", "Policy", "Post-emergency care", "Contingency (4%)"]
PROJECTS = [RK, HR, ST, GR, "School Safety Index", CM, PO, BT, OB, CO]

rows = [
    ("Trust Admin", "Branding & Outreach", 100000, OB, ""),
    ("Trust Admin", "Capacity Building and Consultation", 3600000, OB, "Expert / leadership / consultation fees — shared across projects"),
    ("Trust Admin", "Employee Benefits", 100000, OB, ""),
    ("Trust Admin", "Intervention audit (M&E)", 500000, OB, "M&E of interventions — could move to Rakshak"),
    ("Trust Admin", "IT hardware cost", 0, OB, ""),
    ("Trust Admin", "Marketing material", 100000, OB, ""),
    ("Trust Admin", "Office space (Virtual)", 100000, OB, ""),
    ("Trust Admin", "Office utilities", 0, OB, ""),
    ("Trust Admin", "Reporting and Compliance", 500000, OB, ""),
    ("Trust Admin", "Salaries & Benefits", 3100000, OB, "Core team — realistically splits across projects; parked in backbone"),
    ("Trust Admin", "Travel & Networking", 500000, OB, ""),
    ("Trust Admin", "Website Development & Hosting", 100000, OB, ""),
    ("Technology", "Collaboration with Google (Maps)", 300000, RK, "★ Defect repository / Maps — mapped to Rakshak; could be SATARK"),
    ("Technology", "Community Action via Mobile App", 1000000, ST, "★ Citizen-reporting app — mapped to SATARK/Civic Tech"),
    ("Technology", "National Road Safety Hackathon + Good Samaritan awards", 5000000, CM, "★ Large public event — mapped to Campaign; part GovTech"),
    ("Technology", "Product development: Safekart / Hackathon incubation", 800000, BT, "★ New-product incubation — mapped to Bets"),
    ("Education", "Safety is the new swag (CARS24 campaign)", 4000000, CM, ""),
    ("Enabler - Community Building", "Safer Mobility Impact Fellowship", 3000000, OB, "★ Talent pipeline feeding all projects — parked in backbone"),
    ("Infrastructure", "Infrastructure Internship & School Safety Zone", 2800000, RK, "★ Includes School Safety Index — carve SSI out here when ready"),
    ("Policy", "Strengthening Road Safety Regulations via RTI/PIL", 2200000, PO, "Part of this research also feeds compensation"),
    ("Post-emergency care", "Study on Cashless Treatment & Compensation (Delhi NCR)", 1200000, HR, ""),
    ("Contingency (4%)", "Contingency cost", 1000000, CO, ""),
]
N = len(rows)
first, last = 2, 1 + N  # data rows 2..23

wb = Workbook()

# ================= Sheet 1: Line Items (master, editable) =================
ws = wb.active
ws.title = "Line Items"
ws.sheet_view.showGridLines = False
# title band
ws.merge_cells("A1:F1")
hcell(ws["A1"], "CFI · AOP 2026–27 · Budget line items with project mapping  (edit the Project column — every other tab recalculates)", size=11, fill=INDIGO, align="left")
ws.row_dimensions[1].height = 30
heads = ["Vertical", "Activity", "Budget (₹)", "In lacs", "Project", "Notes / assumptions"]
for j, h in enumerate(heads, 1):
    hcell(ws.cell(row=2, column=j), h, size=10, fill=INK, align="center")
ws.row_dimensions[2].height = 24
r0 = 3
for i, (vert, act, bud, proj, note) in enumerate(rows):
    r = r0 + i
    band = WHITE if i % 2 == 0 else "FAFAFB"
    cell(ws.cell(row=r, column=1), vert, fill=band)
    cell(ws.cell(row=r, column=2), act, fill=band)
    cell(ws.cell(row=r, column=3), bud, align="right", fmt=RUPEE, fill=band, wrap=False)
    cell(ws.cell(row=r, column=4), f"=C{r}/100000", align="right", fmt="0.0", fill=band, wrap=False)
    cell(ws.cell(row=r, column=5), proj, fill=TINT if proj != OB else band, bold=(proj != OB))
    cell(ws.cell(row=r, column=6), note, size=9, color=MUT, fill=band)
tot = r0 + N
cell(ws.cell(row=tot, column=1), "Grand Total", bold=True, fill=MIST)
cell(ws.cell(row=tot, column=2), "", fill=MIST)
cell(ws.cell(row=tot, column=3), f"=SUM(C{r0}:C{tot-1})", bold=True, align="right", fmt=RUPEE, fill=MIST, wrap=False)
cell(ws.cell(row=tot, column=4), f"=C{tot}/100000", bold=True, align="right", fmt="0.0", fill=MIST, wrap=False)
cell(ws.cell(row=tot, column=5), "", fill=MIST)
cell(ws.cell(row=tot, column=6), "", fill=MIST)
LI_B = f"'Line Items'!$C${r0}:$C${tot-1}"   # budget range
LI_P = f"'Line Items'!$E${r0}:$E${tot-1}"   # project range
LI_V = f"'Line Items'!$A${r0}:$A${tot-1}"   # vertical range
for col, w in zip("ABCDEF", [22, 46, 15, 9, 26, 42]):
    ws.column_dimensions[col].width = w
ws.freeze_panes = "A3"

# ================= Sheet 2: By Project =================
wp = wb.create_sheet("By Project")
wp.sheet_view.showGridLines = False
wp.merge_cells("A1:D1")
hcell(wp["A1"], "AOP 2026–27 · Budget by project", size=12, fill=INDIGO)
wp.row_dimensions[1].height = 28
for j, h in enumerate(["Project", "Budget (₹)", "In lacs", "% of total"], 1):
    hcell(wp.cell(row=2, column=j), h, fill=INK, align="center")
wp.row_dimensions[2].height = 22
pr = 3
for i, p in enumerate(PROJECTS):
    r = pr + i
    band = WHITE if i % 2 == 0 else "FAFAFB"
    cell(wp.cell(row=r, column=1), p, bold=True, fill=band)
    cell(wp.cell(row=r, column=2), f"=SUMIF({LI_P},A{r},{LI_B})", align="right", fmt=RUPEE, fill=band, wrap=False)
    cell(wp.cell(row=r, column=3), f"=B{r}/100000", align="right", fmt="0.0", fill=band, wrap=False)
    cell(wp.cell(row=r, column=4), f"=B{r}/$B${pr+len(PROJECTS)}", align="right", fmt=PCT, fill=band, wrap=False)
ptot = pr + len(PROJECTS)
cell(wp.cell(row=ptot, column=1), "Grand Total", bold=True, fill=MIST)
cell(wp.cell(row=ptot, column=2), f"=SUM(B{pr}:B{ptot-1})", bold=True, align="right", fmt=RUPEE, fill=MIST, wrap=False)
cell(wp.cell(row=ptot, column=3), f"=B{ptot}/100000", bold=True, align="right", fmt="0.0", fill=MIST, wrap=False)
cell(wp.cell(row=ptot, column=4), f"=B{ptot}/$B${ptot}", bold=True, align="right", fmt=PCT, fill=MIST, wrap=False)
for col, w in zip("ABCD", [30, 16, 10, 11]):
    wp.column_dimensions[col].width = w
wp.freeze_panes = "A3"

# ================= Sheet 3: Project x Vertical matrix =================
wm = wb.create_sheet("Project x Vertical")
wm.sheet_view.showGridLines = False
ncol = 1 + len(VERTICALS) + 1
wm.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncol)
hcell(wm.cell(row=1, column=1), "AOP 2026–27 · Project × Vertical matrix  (verticals preserved; re-cut by project)", size=11, fill=INDIGO)
wm.row_dimensions[1].height = 26
hcell(wm.cell(row=2, column=1), "Project ↓  /  Vertical →", fill=INK, align="center")
for j, v in enumerate(VERTICALS):
    hcell(wm.cell(row=2, column=2 + j), v, size=9, fill=INK, align="center")
hcell(wm.cell(row=2, column=ncol), "Project total", fill=INK, align="center")
wm.row_dimensions[2].height = 40
mr = 3
for i, p in enumerate(PROJECTS):
    r = mr + i
    cell(wm.cell(row=r, column=1), p, bold=True, fill=TINT)
    for j, v in enumerate(VERTICALS):
        col = 2 + j
        f = f"=SUMIFS({LI_B},{LI_P},$A{r},{LI_V},{get_column_letter(col)}$2)"
        cell(wm.cell(row=r, column=col), f, align="right", fmt=RUPEE, wrap=False, size=9)
    lastc = get_column_letter(1 + len(VERTICALS))
    cell(wm.cell(row=r, column=ncol), f"=SUM(B{r}:{lastc}{r})", bold=True, align="right", fmt=RUPEE, fill="FAFAFB", wrap=False)
mtot = mr + len(PROJECTS)
cell(wm.cell(row=mtot, column=1), "Vertical total", bold=True, fill=MIST)
for j in range(len(VERTICALS)):
    col = 2 + j; L = get_column_letter(col)
    cell(wm.cell(row=mtot, column=col), f"=SUM({L}{mr}:{L}{mtot-1})", bold=True, align="right", fmt=RUPEE, fill=MIST, wrap=False, size=9)
Lc = get_column_letter(ncol)
cell(wm.cell(row=mtot, column=ncol), f"=SUM({Lc}{mr}:{Lc}{mtot-1})", bold=True, align="right", fmt=RUPEE, fill=MIST, wrap=False)
wm.column_dimensions["A"].width = 26
for j in range(len(VERTICALS)):
    wm.column_dimensions[get_column_letter(2 + j)].width = 14
wm.column_dimensions[get_column_letter(ncol)].width = 16
wm.freeze_panes = "B3"

# ================= Sheet 4: By Vertical (tie-out) =================
wv = wb.create_sheet("By Vertical (tie-out)")
wv.sheet_view.showGridLines = False
wv.merge_cells("A1:C1")
hcell(wv["A1"], "Tie-out · original vertical totals (must still equal ₹3.0 Cr)", size=11, fill=INDIGO)
wv.row_dimensions[1].height = 26
for j, h in enumerate(["Vertical", "Budget (₹)", "In lacs"], 1):
    hcell(wv.cell(row=2, column=j), h, fill=INK, align="center")
vr = 3
for i, v in enumerate(VERTICALS):
    r = vr + i
    band = WHITE if i % 2 == 0 else "FAFAFB"
    cell(wv.cell(row=r, column=1), v, bold=True, fill=band)
    cell(wv.cell(row=r, column=2), f"=SUMIF({LI_V},A{r},{LI_B})", align="right", fmt=RUPEE, fill=band, wrap=False)
    cell(wv.cell(row=r, column=3), f"=B{r}/100000", align="right", fmt="0.0", fill=band, wrap=False)
vtot = vr + len(VERTICALS)
cell(wv.cell(row=vtot, column=1), "Grand Total", bold=True, fill=MIST)
cell(wv.cell(row=vtot, column=2), f"=SUM(B{vr}:B{vtot-1})", bold=True, align="right", fmt=RUPEE, fill=MIST, wrap=False)
cell(wv.cell(row=vtot, column=3), f"=B{vtot}/100000", bold=True, align="right", fmt="0.0", fill=MIST, wrap=False)
for col, w in zip("ABC", [30, 16, 10]):
    wv.column_dimensions[col].width = w

# ================= Sheet 5: Notes =================
wn = wb.create_sheet("Notes")
wn.sheet_view.showGridLines = False
wn.column_dimensions["A"].width = 110
notes = [
    ("CFI · AOP 2026–27 — project bifurcation (first pass)", INDIGO, 13, True),
    ("", WHITE, 10, False),
    ("Source: 'CFI - AOP (2026-2027)' Google Sheet, quarterly-phased tab. Total ₹3,00,00,000 (₹3.0 Cr / 300 lacs).", INK, 10, False),
    ("The 8 verticals are kept exactly as in the sheet. The Project column on 'Line Items' is the only thing you edit —", INK, 10, False),
    ("every other tab recalculates from it. Reassign a row's project and the pivots + matrix update automatically.", INK, 10, False),
    ("", WHITE, 10, False),
    ("Judgement calls to confirm (marked ★ in the Notes column):", AMBER, 11, True),
    ("• Collaboration with Google (Maps), ₹3 L → Project Rakshak (defect repository / Maps). Could sit under SATARK.", INK, 10, False),
    ("• Community Action via Mobile App, ₹10 L → SATARK / Civic Tech. Could be a Campaign asset.", INK, 10, False),
    ("• National Hackathon + Good Samaritan awards, ₹50 L → Campaign & Comms. Part of it is GovTech talent-sourcing.", INK, 10, False),
    ("• Safekart / incubation, ₹8 L → Bets (new products).", INK, 10, False),
    ("• Safer Mobility Impact Fellowship, ₹30 L → Org Backbone (talent feeding all projects). Could be split across projects.", INK, 10, False),
    ("• Salaries & Benefits ₹31 L and Capacity Building ₹36 L are shared core costs, parked in Org Backbone for now.", INK, 10, False),
    ("• Infrastructure Internship ₹28 L currently bundles the School Safety Zone — School Safety Index has no separate line yet.", INK, 10, False),
    ("", WHITE, 10, False),
    ("Two gaps worth a decision:", AMBER, 11, True),
    ("• Gig Rider Safety shows ₹0 — the current ₹3.0 Cr budget has no dedicated gig line (an earlier ₹6 Cr draft did:", INK, 10, False),
    ("   study ₹8 L + intervention design ₹4 L + dissemination ₹8 L). Tell me the number and I'll carve it in.", INK, 10, False),
    ("• School Safety Index similarly has no standalone line — say what to carve from Infrastructure Internship.", INK, 10, False),
    ("", WHITE, 10, False),
    ("Next options: split shared core costs (salaries, capacity building, fellowship) across projects on a % basis, and/or", INK, 10, False),
    ("add the GL cost-category view (Professional fees, Salary & Incentives, Audit & Compliance, Tech Infra, Marketing, Rent).", INK, 10, False),
]
for i, (txt, color, size, bold) in enumerate(notes, 1):
    c = wn.cell(row=i, column=1, value=txt)
    c.font = Font(name="Calibri", size=size, bold=bold, color=color)
    c.alignment = Alignment(horizontal="left", vertical="center")

out = "CFI_AOP_Project-Bifurcation_v1_2026-08-19.xlsx"
wb.save(out)
print("saved", out)

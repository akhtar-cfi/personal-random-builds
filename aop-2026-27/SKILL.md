---
name: cfi-aop-2026-27
description: Continuation kit for Crashfree India's Annual Operating Plan 2026-27 (July 2026 - June 2027). Use whenever editing, extending, or regenerating the AOP deck (CFI_AOP_2026-27.pptx) or the AOP budget workbook (CFI_AOP_Budget_2026-27_v4.xlsx). Contains the full slide map, exact Rs 6.00 Cr budget line items, source-document facts vs assumptions, known data discrepancies, build scripts, and the mandatory QA loop. Trigger on any mention of CFI AOP, annual operating plan, AOP deck, AOP budget, or changes to these two files.
---

# CFI ANNUAL OPERATING PLAN 2026-27 — CONTINUATION KIT
**Built:** 12 Jul 2026 (claude.ai session) · **Restructured:** 29 Jul 2026 (Claude Code session — v4) · **Owner:** Akhtar, Mission Lead, Crashfree India (Vision Zero Trust, a Cars24 Commitment)

> **v4 RESTRUCTURE (29 Jul 2026, per Akhtar):** total stays Rs 6.00 Cr. School Safety Index (was Rs 1.00 Cr) and Gig Rider Safety (was Rs 0.20 Cr) are **no longer funded verticals — they are now stage-gated BETS** with a Rs 0.10 Cr seed each (released only against a board-approved pilot design). A new **Civic & GovTech (SATARK + CFI data stack) vertical** was added at exactly **Rs 1.00 Cr**. Deck: three core programmes (Rakshak / H&R / Civic & GovTech) + two bets. Wordmark placeholder replaced with real logos (logo_blue.png / logo_white.png). Sections below have been updated to match; superseded v3 numbers appear only in the change logs.

## 0. WHAT THIS KIT CONTAINS

| File | What it is |
|---|---|
| `SKILL.md` | This file — all context needed to modify the deliverables |
| `CFI_AOP_2026-27.pptx` | The 14-slide AOP deck (final, QA'd, validation-passed) |
| `CFI_AOP_Budget_2026-27_v4.xlsx` | The Rs 6.00 Cr budget workbook (3 sheets, formula-driven, recalc-verified) |
| `build_deck.py` + `helpers.py` | python-pptx source that generates the deck **from scratch**. Edit script → rerun → full deck regenerates. This is the preferred edit path for anything beyond tiny text tweaks |
| `build_budget.py` | openpyxl source that generates the budget workbook from scratch (line items are in the `D` list at the top) |

**Golden rule: edit the scripts, not the binaries.** The deck and workbook are deterministic outputs of the scripts. For text-only micro-edits, direct XML/openpyxl edits are fine, but any layout change should go through `build_deck.py` + the QA loop (Section 8).

---

## 1. THE ASK (as given by Akhtar)

AOP period: **July 2026 – June 2027**. As restructured 29 Jul 2026, three core programmes + one seed pool:
1. **Project Rakshak** — focus on *institutionalisation* (Rs 1.85 Cr)
2. **Hit & Run compensation scheme** — increase claim rate in **at least 2 selected districts** (Rs 0.60 Cr)
3. **Civic & GovTech** — SATARK enforcement platform + four open data products, **exactly Rs 1.00 Cr** (Akhtar's instruction)
4. **Bets (stage-gated seed)** — School Safety Index + Gig Rider Safety, Rs 0.10 Cr each, released only against a board-approved pilot/study design

Deck must contain: learnings from past year · key focus areas · detail on each · objectives/KPIs · timeline (Gantt) · budget (Rs 6 Cr, improved from the messy "Budget Bifurcation_v2" sheet). Instruction was to *take calls* on what's best for next year, not transcribe source docs.

---

## 2. SOURCE DOCUMENTS (what fed the plan)

1. **Project Rakshak — Cohort 2 AOP** (Google Doc `1bwFriXwYHpCchrCr6G-G_iNh4Q5XOPcagvA0rfV5sU0`): three-track audit model (A: institutional students ~90 sites; B: NGO partners ~20; C: certified RSAs ~40), anchor districts Gurugram/SW Delhi/Jaipur, Expert Consortium (Prof. Geetam Tiwari IIT-D, Col. Sanjeev Sharma IIT-M CoERS), Rakshak Audit Manual v1.0, targets 150+ audits / 100+ recommendations accepted / 75+ implementations / 12+ DRSC presentations / Rs 91L operational budget, ignition plan May–Jul 2026.
2. **Crash Claim Compensation Vertical AOP 2026-27** (Google Doc `1q0V1uIIKLzl9jiNdurE6nmhz12EZ2MPE`): 4 pillars (scheme audit & process documentation; institutional capacity building; victim identification & AASHA; policy audit & advocacy). Gurugram primary, SW Delhi + Jaipur secondary. Deliverable: *"Where the Pipeline Breaks"* scheme audit report to MoRTH by Apr–May 2027. KPIs: ≥20% cut in median processing time, 20-30 claims tracked end-to-end, ≥3 DRSC meetings with H&R agenda (elsewhere 20+), AASHA 100+ MAU by Dec 2026. Lead: Kesar Kanjhlia. MACT reform consciously deprioritised.
3. **CFI_CrashClaim_AOP_2026-27_Review deck**: Audit → Advocate → Hold Accountable framing; Year-2 footprint districts (Delhi/NCR/Haryana/UP + Bihar/Rajasthan/MP watchlist); budget envelope Rs 47–66L (People 30–40, travel 6–9, AASHA GTM 3–5, events 4–6, contingency 4–6).
4. **Project Rakshak IITM deck** (Col. Sanjiv Sharma discussion, Jun 2026): 4-phase methodology, dashboard, Cohort-1 stats — 31 audited / 18 cities / 25+ approvals / **15 implementations began** (⚠ conflicts with doc 1's "7+", see Section 6).
5. **CFI_-_AOP_(2026-2027).xlsx**, sheet `Budget Bifurcation_v2` (prior draft, Rs 619.7L) + `Mid Year Cost Tracking` (Y1 actuals; IRSC charge Rs 3.54L/mo = the mystery Rs 42.48L "Capacity Building" line) + `High Level Qaurterly Cost` (Y1 budget was Rs 3.0 Cr).

---

## 3. THE BUDGET — EXACT LINE ITEMS (Rs 600.00 L total)

Workbook: **Budget Summary** (SUMIF rollup + % of total) · **Budget Detail** (blue cells = quarterly inputs in Rs Lakh; Total-Lakh and Total-Rs are formulas) · **Notes & Assumptions** (legend, assumptions, change log vs prior draft). Q1=Jul-Sep, Q2=Oct-Dec, Q3=Jan-Mar, Q4=Apr-Jun.

Vertical totals (v4): **Rakshak 185 · Civic & GovTech (SATARK) 100 · Hit & Run 60 · Marketing Campaign 60 · Trust Admin 151 · Bets (Seed Fund) 20 · Contingency 24 (exactly 4%) = 600.** Quarterly: Q1 122.5 / Q2 161 / Q3 164.5 / Q4 152.

Full line items (Vertical | Line item | basis | Q1/Q2/Q3/Q4 in Rs L) — this is the canonical list; `build_budget.py`'s `D` list matches it exactly:

**Project Rakshak (185)**
- Student team stipends | 100 teams × Rs 36K, performance-linked | 9/18/9/0 = 36
- Mentor honorarium | 25 × Rs 24K | 1.5/2.5/2/0 = 6
- Certified RSA audits (Track C) | ~40 sites × ~Rs 25K (**rate assumed**) | 3/4/3/0 = 10
- NGO partner grants (Track B) | ~20 sites + re-checks | 3/5/4/0 = 12
- Programme team (fellows, PM, advocacy) | 8/9/8/8 = 33
- Expert Consortium + Audit Manual v1.0 | 2/1/2/1 = 6
- Public dashboard & tech | 1.25×4 = 5
- Post-intervention impact audits | 0/2/3/3 = 8
- Rakshak Finale + national awards | **trimmed from 50L** | 0/0/10/20 = 30
- Travel & field logistics | 3/3/2/2 = 10
- Media, documentation & comms | **trimmed from 25L** | 3/4/4/4 = 15
- DRSC & stakeholder engagement | 2/3/2/2 = 9
- Campus ambassadors & outreach | 2/2/1/0 = 5

**Civic & GovTech — SATARK + data stack (100)** — sized to Akhtar's "exactly Rs 1 Cr"; **no cost data exists in SATARK docs, every line is a planning assumption**
- Product engineering team (2-3 engineers + product lead) | 10×4 = 40
- New city deployments & police integration (Gurugram, Pune, Ahmedabad) | 2/6/6/6 = 20
- Cloud, ULIP API & data infrastructure | 3×4 = 12
- Officer training & field support | 1/2/2.5/2.5 = 8
- Four open data products (defect repo, Parliament, SC tracker, crash dashboard) | 3×4 = 12
- Product design, dashboards & impact evaluation | 2×4 = 8

**Hit & Run Compensation (60)** — sized inside the vertical deck's 47–66L envelope
- Vertical team (lead + 2 fellows ~50K/mo + interns ~15K/mo) | 7.5×4 = 30
- Field travel | 2×4 = 8
- AASHA go-to-market | 2/1/0.5/0.5 = 4
- Stakeholder roundtables | 1.5×4 = 6
- District process mapping & comparative notes | 2/3/1/1 = 7
- Victim narratives, audit report & public brief | 0.5/1/1.5/2 = 5

**Bets — Seed Fund (20)** — released only against a board-approved design; a proven bet returns as a funded Year 3 programme
- School Safety Index (bet): IRC:SP:32-2023 rubric validation on ~100 schools, one city | 0/2/4/4 = 10
- Gig Rider Safety (bet): scoping study + platform engagement | 0/2/4/4 = 10

**Marketing Campaign "Safety is the New Swag" (60)** — digital 18 (2/5/6/5) · media 14 (1/4/5/4) · offline 12 (0/3/5/4) · community 8 (1/2/3/2) · campaign management 8 (2×4). *Prior draft funded only 1 of 4 pillars and had an untagged Rs 30L people cost.*

**Trust Admin (151)** — salaries & benefits 78 (19.5×4) · IRSC institutional support & expert consultation 42 (10.5×4; = ~Rs 3.5L/mo, matches mid-year actuals) · IT/SaaS/AI tools 14 (3.5×4) · M&E + statutory & impact audit 6 (0.5/1.5/1.5/2.5) · travel & networking 7 (1/2/2/2) · branding 3 (1/1/0.5/0.5) · virtual office 1 (0.25×4)

**Contingency (24)** — 6×4, exactly 4% of 600 (prior draft said "4%" but held 20L = 3.2%).

**xlsx build rules:** openpyxl; formulas not hardcoded values; after any edit run `recalc.py` (from the public xlsx skill) — must return `status: success, total_errors: 0` (142 formulas currently). Blue font (0000FF) = input cells; never convert formula cells to literals.

---

## 4. THE DECK — SLIDE MAP (15 slides, 16:9)

| # | Slide | Layout archetype | Key content |
|---|---|---|---|
| 1 | Cover | Brand band right w/ 5 section tags + real logo | "From programmes **to institutions.**" · Jul 2026 – Jun 2027 · Rs 6.00 Cr |
| 2 | Year 1 in review | 2×4 stat grid + brand strip | 31 sites · 18 cities · 25+ approvals · **7+** works begun · 900+ surveys · 120+ victims surveyed · 30+ consultations · 1M+ reached. Strip: 150+ members, 50+ experts, AASHA live, MoUs Gurugram & Jaipur Traffic Police, DRSC in SW Delhi |
| 3 | Learnings | 5 scorecard rows w/ "IN Y2" column | Credibility is the currency · Awareness alone doesn't move claims · Depth beats breadth · Audits die at submission · Plan what we fund |
| 4 | **Objectives / destination** | Brand POSITION strip + 2×2 outcome cards w/ "Y3:" kickers | Positioning: "India's audit-and-accountability institution for road safety." Outcomes: Rakshak in institutions / Compensation fixed then replicated / SATARK as public infrastructure (30 cities) / A public evidence brand |
| 5 | Strategy | 3 stacked (Audit/Advocate/Hold Accountable) + brand block | "The Year 2 shift: from programmes to institutions" + 4 bullets (incl. civic tech) |
| 6 | Focus areas | 1×3 core cards w/ target chips + 2-card bets strip | Cores: Rakshak / H&R (2 fixed · 8+ mapped) / Civic & GovTech (30 cities); bets strip: SSI + Gig, Rs 0.10 Cr seed chips |
| 7 | Rakshak deep dive (CORE 01) | 3-track rows + anchor-district line + dashboard browser-frame card + brand target block | "Put the audit pipeline inside institutions"; tracks A/B/C; dashboard card links crashfreeindia.org/rakshak/dashboard **[live screenshot to be inserted — site unreachable from build sandbox]**; targets 150+/100+/75+/12+/v1.0; Rs 1.85 Cr |
| 8 | H&R deep dive (CORE 02) | 4 pillar rows + fix>pilot>map line + brand block | "Fix two districts, map eight": 2 FIXED (uptake lift, −20% time) / 2+ PILOTING / 8+ MAPPED by Jun 2027 / 20-30 claims tracked / report to MoRTH; Rs 0.60 Cr |
| 9 | Civic & GovTech deep dive (CORE 03) | SATARK pipeline chips + 2×2 proof stats + data-stack/exploration lines + brand block | "From 2 cities to 30"; verified: 3,00,000+ scanned, Rs 30 Cr+ challans, 350+ intercepted, 2 cities live; targets **30 cities** / 1,000+ interceptions / 4 data products / 2+ govtech opportunities; Rs 1.00 Cr |
| 10 | The bets | 2 large cards (why-a-bet / THE SEED / THE GATE) + brand strip | SSI: ~100-school rubric pilot; Gig: scoping study + platforms; Rs 0.20 Cr total, stage-gated |
| 11 | KPIs | 5 scorecard rows: north star + supporting | Rakshak (75+ impl) / H&R (2 fixed, 8+ mapped) / Civic & GovTech (30 cities) / Bets (2 designs) / Campaign (1M+) |
| 12 | Gantt | 13 bars, 12 month columns, quarter separators | Groups: Rakshak(4) / H&R(3: fix→pilot+map→report) / Civic & GovTech(3: 3 go-lives→30-city wave→data stack) / Bets(2) / Campaign(1) |
| 13 | Budget | Horizontal bars + brand quarterly-phasing block | Rs 6.00 Cr, 71% programmes; Q phasing 1.23/1.61/1.65/1.52 Cr |
| 14 | Enablers | 2×2 campaign cards + brand org-backbone block | Swag campaign pillars Rs 0.60 Cr; backbone Rs 1.51 Cr itemised |
| 15 | Close (full brand bg) | Checklist | "Systems work because we hold them accountable." + 5 success outcomes for Jun 2027 |

Slide-number footers exist on slides 2–14 (`NN / 15`). If adding/removing slides, update `TOTAL` in `build_deck.py` and every `footer(s, idx, TOTAL)` call.

---

## 5. DESIGN SYSTEM (must-follow; condensed from crashfree-india-design skill v2.4)

- 16:9, 13.333×7.5 in. Margins 0.7 in. **Bottom safe line 6.9 in**; footer at 7.12 in.
- Fonts: **Montserrat** (headings) + **Geist** (body). Nothing else.
- Colors: BRAND #4A35FF · BRAND_LITE #F3F1FF · DARK #1A1C1C · MUTED #777589 · BORDER #EDEEF2 · LAV #C8C0FF · LAV_DK #6A55FF · SUCCESS #00AA44 (status only) · WARNING #F57C00 · DANGER #F10015 (death/critical stats ONLY, never decorative).
- Signature: two-line titles — line 1 DARK, line 2 BRAND. Eyebrow kickers 10pt tracked 2.4. Sparkle motif top-right. `shadow.inherit=False` on every shape.
- Brand name: "Crashfree India" — never all-caps in body. Logo in this build is a **typographic wordmark placeholder** (`wordmark()` in helpers.py) because the SVG logo files weren't in session. **If the real `primary_blue-logo.svg` / `secondary-white-logo.svg` are available locally, replace `wordmark()` calls with image placement** (blue on light bg, white on brand bg, min 180px width).
- Brand color note: an open #4736FE vs #4A35FF discrepancy exists in CFI assets; **this build uses #4A35FF** (the design-skill authority). Don't change without Akhtar's call.
- Icons: lucide-static (npm), recolored via SVG string replace → PNG. Never use lucide icons as stand-ins for org logos.

## 6. FACTS vs ASSUMPTIONS vs KNOWN DISCREPANCIES (honesty register — resolve before external circulation)

**Verified from source docs:** Cohort-1 stats on slide 2 (31/18/25+/900+); H&R Y1 stats (120+ victims, 30+ consultations, helpdesk footfall 300-400, MoU Jaipur Traffic Police, partnership Gurugram Police); three-track model & targets; H&R KPIs & report title; Rs 47-66L H&R envelope; IRSC charge Rs 3.54L/mo.

**Discrepancies / calls taken (flag to Akhtar before trustee circulation):**
1. **Implementations begun: "7+" used** (Cohort 2 AOP doc) vs "15" (IITM deck). Conservative figure chosen. One number must win.
2. **H&R district framing:** Akhtar's brief said 2 districts; vertical AOP KPI table says "20 districts tracked". Deck frames it as **2 model districts for claim-uptake lift** (Gurugram + SW Delhi), Jaipur comparative, broader tracking as supporting. Confirm.
3. **Rakshak budget:** Rs 185L here vs Rs 91L "operational budget" in the Cohort 2 doc (doc excludes finale/media/travel lines). Align the two documents.
4. **Track C RSA rate Rs 25K/site is an assumption** pending empanelment EOIs.
5. **SSI 2,000 schools × Rs 3K** is now a *parked* Year-3 candidate (the bet validates the per-school cost first).
6. **1M+ citizens reached** and **150+ members / 50+ experts** are from prior CFI materials (memory), not re-verified this session.
7. Bets "~100-school pilot", "3+ platform engagements", Campaign "1M+ engaged" are **targets set in-session** — plausible but Akhtar-unratified.
8. **Civic & GovTech (v4, 29 Jul):** SATARK *proof stats on slide 9 are verified* from SATARK_Briefing.pdf / _SATARK common.pptx via the repo research brief `research/briefs/C-satark-datastack.md` (3,00,000+ scanned; Rs 30 Cr+ challans surfaced; 350+ intercepted; live Jaipur + Bengaluru — note the PDF-vs-PPTX tension on whether Bengaluru is fully live; internal speaker note says "verify all figures before showing leadership"). **The 30-city target is Akhtar's instruction (29 Jul)**; supporting targets (1,000+ interceptions, 2+ govtech opportunities) and **every budget line in the Rs 1.00 Cr vertical are session-set assumptions — SATARK docs contain no cost data**. The Rs 1 Cr assumes city-side infra (cameras, billboards) is funded by police/partners; CFI funds software, integration & training (~Rs 0.7L/city). Validate before board sign-off. Also note: SATARK has no public web footprint (brief H) — keep it internal-facing until cleared.
9. **H&R fix/pilot/map framing (29 Jul, Akhtar):** 2 districts fixed + pilots beyond + **8+ districts process-mapped by June 2027** is Akhtar's instruction; "2+ piloting" is a session-set floor — ratify the pilot count.
10. **Rakshak dashboard card (slide 7):** links crashfreeindia.org/rakshak/dashboard (verified live per brief D, 23 May 2026: 31 blackspots, 7+ interventions tracked). The card is a styled browser-frame placeholder — **crashfreeindia.org is unreachable from the build sandbox, so a real screenshot must be dropped in before circulation** (card carries an explicit note).

## 7. LOCAL ENVIRONMENT (Claude Code on Akhtar's machine — differs from claude.ai sandbox)

- Install deps: `pip install python-pptx openpyxl cairosvg fonttools` · `npm i lucide-static` (in repo dir).
- Fonts: Montserrat + Geist must be installed system-wide for correct rendering (Akhtar already uses them). On Windows, LibreOffice path differs — replace the sandbox `soffice.py` wrapper with direct `soffice --headless --convert-to pdf`.
- **Float-EMU corruption risk:** any computed shape geometry passed to python-pptx must be coerced to `int()` — float EMUs silently corrupt files for Microsoft PowerPoint (renders fine in LibreOffice). `helpers.py` divides `gw/12` for the Gantt — python-pptx Length division returns ints here, but if you edit geometry math, wrap in `int()`.
- **Font embedding for cross-machine sharing:** requires the two-part post-processing approach (embed via LibreOffice `EmbedFonts` setting, then fix `presentation.xml` `embedTrueTypeFonts` attrs). Only needed if recipients lack the fonts.
- Drive uploads from Claude Code: Google Drive connector can **create/read but not edit/delete**; large binary pptx sometimes fails → fall back to local file + manual upload.

## 8. MANDATORY QA LOOP (never skip)

```bash
python build_deck.py
soffice --headless --convert-to pdf CFI_AOP_2026-27.pptx
pdftoppm -jpeg -r 110 CFI_AOP_2026-27.pdf slide
# VIEW every changed slide image: overflow past 6.9in, overlaps, wrapped labels, right-margin breaches
python <pptx-skill>/scripts/office/validate.py CFI_AOP_2026-27.pptx   # must pass
# Budget edits:
python <xlsx-skill>/scripts/recalc.py CFI_AOP_Budget_2026-27_v3.xlsx  # status: success, 0 errors
```

## 9. STANDING RULES (apply at end of any work session)

- **Archive to Drive** (via connector or manually): decks/PDFs → folder `1AFAlC010D55j_VaLs6sWYSW_NDm6vyur`; skill .md files → `1rhAnPaClck8umIxAJqESftNJwR7lTkRQ`; other artifacts (xlsx, scripts) → `1SIa0Zm3EkDi6xd_dBY57Vjdm8ALVjIwS`. Naming: `<Org/Topic>_<Purpose>_<Audience>_v<N>_<YYYY-MM-DD>.<ext>`.
- **Chat tracker:** after the Claude Code session, Akhtar pastes a 2-line summary into claude.ai and says "log this in the tracker" (tracker v1 file ID `1d1O3qYklUEJXsXQVReFujk141Ta7_8-LEzx2srbDa_4`).
- **Honesty rule:** never invent stats/sources; label targets vs verified facts at every handoff; keep the Section 6 register updated as items get resolved.

## 10. LIKELY NEXT EDITS (anticipated)

- Resolve the 7+/15 implementations number and the H&R 2-vs-20 district framing → update slides 2, 7, 10.
- ~~Swap typographic wordmark for real SVG logos~~ — DONE 29 Jul (helpers.py `wordmark()` now places logo_blue.png / logo_white.png).
- Validate the Rs 1.00 Cr Civic & GovTech line items against real engineering & deployment quotes (all assumed).
- Ratify the SATARK targets (5 cities / 1,000+ interceptions / 3 partnerships) and the bet gates with the board.
- Possible re-cuts: Rakshak finale budget, per-vertical Gantt detail.
- Trustee-facing variant: may need font embedding + PDF export + Drive archiving.

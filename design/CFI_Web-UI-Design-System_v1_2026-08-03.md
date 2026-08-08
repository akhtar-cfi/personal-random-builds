# Crashfree India — Web & Portal UI Design System
**v1 · 2026-08-03 · for websites, portals, dashboards and data products**

> This document is the **UI/build layer for anything on a screen with a URL**: the marketing
> site, the Project Rakshak dashboard, the School Safety Index, the Road-Infrastructure Defect
> Repository, the Parliament / SC trackers, the Hit-and-Run compensation portal, and internal
> tools.
>
> It is **grounded in the canonical CFI Design System** (the brand authority — colours, type,
> tone, spacing, marketing-page components) and **extends it** with the primitives a data
> product needs and a brochure site does not: an app shell, data tables, filters, maps, KPI
> tiles, charts, forms, and status systems.
>
> **Authority order when something conflicts:**
> 1. The canonical CFI Design System (brand colours, typography, tone) — always wins.
> 2. This document — for portal/app patterns the canonical doc does not cover.
> 3. Anything else — flag it.
>
> **The one reconciliation to know up front:** the marketing site uses **exactly one accent
> (brand indigo)** and forbids extra accent colours. A *data product* legitimately needs more:
> status states (success/warning/danger), an info/data hue, and a categorical chart palette.
> This document introduces those **strictly for data and status semantics** — never as
> decorative accents, never on marketing pages, never on buttons. Where a token is a portal
> extension beyond the brand doc, it is flagged **[PORTAL]**.

---

## 0. Design principles (carry the brand into product)

1. **Empirical over decorative.** Every screen leads with the number, the map, the status —
   not a hero illustration. Data is the design.
2. **One brand accent.** Indigo `#4A35FF` is the only *brand* colour: actions, emphasis, the
   second line of a title, the primary chart series. Everything else earns its colour through
   *meaning* (status, category), never taste.
3. **Institutional, rigorous, uncompromising.** Calm surfaces, hairline borders, generous
   whitespace, precise type. No gradients (one exception: the hero radial glow), no drop
   shadows at rest, no rounded-corner-under-8px, no emoji in UI chrome.
4. **Light-first.** White and lavender surfaces. The only "dark" surface is brand indigo
   (`bg-brand`) — used for nav headers, hero/CTA bands, and featured panels. Never black/grey
   dark sections.
5. **Colour is never the only signal.** Every status colour is paired with a label, icon, or
   shape (WCAG). A red grade badge also says "D — Critical".
6. **Honesty in the UI.** Label targets vs. verified data, "as reported" vs. audited, live vs.
   cached. Caveat strips are a first-class component, not an afterthought.

---

## 1. Colour tokens

### 1.1 Core palette (from the brand authority)

| Token | Hex | Role |
|---|---|---|
| `--brand` | `#4A35FF` | Primary action, emphasis, brand, primary data series |
| `--brand-lite` | `#F3F1FF` | Soft brand surface (lavender), chips, icon-circles |
| `--brand-wash` | `#F8F7FF` | Subtler section tint (alternating sections) |
| `--brand-100` | `#EFEDFF` | Brand tint for chip/icon-disc fills (denser than lite) |
| `--brand-contrast` | `#C8C0FF` | Lavender — light text/hairlines on `--brand` surfaces |
| `--brand-hairline` | `#6A55FF` | Dividers and glyphs inside brand-indigo blocks |
| `--foreground` | `#1A1C1C` | Headings, primary body text (21:1 on white) |
| `--muted` | `#777589` | Secondary text, captions, metadata, footers |
| `--border` | `#EDEEF2` | **All** borders, hairlines, dividers, table lines |
| `--surface` | `#FFFFFF` | Page background, cards, panels |
| `--surface-muted` | `#F7F7FA` | Subtle fills (stat tiles, table header, wells) |

**Hover/active shades** (for CSS frameworks that don't do opacity utilities; Tailwind can use
`/90`, `/10` opacities instead):

| Token | Hex | Use |
|---|---|---|
| `--brand-600` | `#3E2AE6` | Button hover |
| `--brand-700` | `#3320C4` | Button active/pressed |

### 1.2 Status palette (semantic — states only)

Absolute meanings. Once learned, never repurposed. Always pair with a label/icon.

| Token | Hex | Tint | Meaning |
|---|---|---|---|
| `--success` | `#00AA44` | `--success-tint` `#E7F6EE` | On-track, implemented, resolved, improvement |
| `--warning` | `#F57C00` | `--warning-tint` `#FEF2E4` | Caution, pending, act-soon, "as reported" |
| `--danger` | `#F10015` | `--danger-tint` `#FEE9EB` | Critical, failure, death/fatality stats, blocked |

> Red = critical/death **only**. Never "good", never decorative. Green = positive **only**.

### 1.3 Info / data hue **[PORTAL]**

| Token | Hex | Tint | Meaning |
|---|---|---|---|
| `--info` | `#0E8A8A` | `--info-tint` `#E7F4F4` | Teal — informational, "open data / public good", data-layer category, neutral highlight |

> **[PORTAL] extension.** The marketing site forbids teal. In a data product it earns a place
> as the *info / open-data* hue (it already tags the open-data products across CFI decks). Use
> it for informational banners, "public good" category tags, and as a secondary chart series.
> Never on marketing pages, never for a button, never as a brand accent.

### 1.4 Data-visualisation palette **[PORTAL]**

Charts, maps and category tags need more than one hue. This is the **only** context where
multiple colours appear together, and only ever to encode data.

**Categorical (up to 6 series):**
```
1  brand    #4A35FF
2  info      #0E8A8A   (teal)
3  warning   #F57C00   (amber)
4  success   #00AA44   (green)
5  violet    #8B5CF6   (extra series — data only)
6  slate     #64748B   (extra series / "other")
danger #F10015 reserved for the fatal/critical series only (e.g. deaths bar)
```

**Sequential (priority tiers, heat, density — e.g. defect hotspots):** a single-hue brand ramp
```
brand-50 #EDEBFF · brand-200 #C9C0FF · brand-400 #8B79FF · brand-600 #4A35FF · brand-800 #2E1E9E
```
For crash/fatality density use the danger ramp: `#FEE9EB → #F79AA3 → #F10015 → #A60010`.

**Diverging (below/above a target — e.g. speed vs safe-speed):**
`success #00AA44 ←→ neutral #EDEEF2 ←→ danger #F10015`.

**Chart rules:** primary metric = brand; the fatal/death series = danger red (per the IG
carousel precedent: accidents blue vs deaths red); always label axes and cite the source under
every chart; never a legend without direct labels where space allows.

---

## 2. Typography

**Display / headings:** Montserrat (500, 600, 700). **Body / UI:** Geist (400, 500, 700).
No other fonts, ever. `font-heading` = Montserrat, body default = Geist.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700&display=swap" rel="stylesheet">
<!-- Geist: @fontsource/geist-sans or Vercel's font package -->
```

### 2.1 Type scale

| Role | Font | Size | Weight | Line-height | Tracking |
|---|---|---|---|---|---|
| Hero H1 | Montserrat | 48–72px | 700 | 1.02 | tight |
| Section H2 | Montserrat | 32–60px | 600/700 | 1.05 | tight |
| Subsection H3 | Montserrat | 24px | 600 | 1.3 | 0 |
| Card title H4 | Montserrat | 18px | 600 | 1.4 | 0 |
| Display stat | Montserrat | 40–120px | 700 | 0.95 | tight |
| Quote / statement | Montserrat | 18–24px | 600 | 1.45 | 0 |
| **Body** | Geist | 16px | 400 | 1.6 | 0 |
| Small / caption | Geist | 14px | 400 | 1.5 | 0 |
| **UI label / button** | Montserrat | 11–13px | 600 | 1.0 | 0.02em |
| Eyebrow / kicker | Montserrat | 11px | 600 | 1.0 | 0.25em |
| Table header | Montserrat | 11px | 600 | 1.0 | 0.12em (uppercase ok) |
| Micro / meta | Geist | 10–12px | 400 | 1.4 | 0 |
| Data / tabular number | Montserrat | inherit | 600 | 1.0 | 0, `tabular-nums` |

### 2.2 The signature two-line title

```html
<h2 class="font-heading text-4xl font-bold leading-[1.05] tracking-tight sm:text-5xl">
  Statement line one<br>
  <span class="text-brand">accented line two.</span>
</h2>
```
Line one `--foreground`, line two `--brand`. Appears on nearly every page/section header.

### 2.3 Rules
- Body copy is **always** `--muted` grey; emphasis is `--foreground` or `--brand`.
- Never ALL-CAPS body. Uppercase allowed only on eyebrows/table-headers via tracking.
- Never apply an uppercase transform to the brand name ("Crashfree India", "Cars24").
- Numbers in tables/KPIs use `font-variant-numeric: tabular-nums` so columns align.

---

## 3. Spacing, radius, elevation

**Spacing — 4px base.** Only multiples of 4: `4 8 12 16(default) 24 32 40 48 64`.

**Container:** `max-width: 1280px` (`max-w-7xl`), centred, `px-24` (24px) mobile → `px-40`
(40px) desktop. Section vertical rhythm `96px` (`py-24`) → `128px` (`py-32`) for marketing;
**portal/app** pages are denser — use `24–32px` block padding and `16–24px` gaps.

**Radius:**
| Element | Radius |
|---|---|
| Buttons, chips, pills, filter selects, search | `full` (pill) |
| Cards, inputs, tiles | `12px` (rounded-2xl / rounded-xl) |
| Featured / brand panels, modals | `20px` (rounded-3xl) |
| Small tags, table-cell badges | `8px` |

**Elevation:** rest = **no shadow**, define with `1px --border`. Hover (interactive cards) =
`shadow-lg` tinted `shadow-brand/5`. Overlays (dropdown, popover, toast) = soft `0 8px 24px
rgba(26,28,28,.10)`. Modals = `0 24px 64px rgba(26,28,28,.18)` + scrim `rgba(26,28,28,.45)`.
Never a drop shadow on text; never a decorative shadow at rest.

**Motion:** 150–200ms `ease-out` for hover/focus; 200–300ms for enter/exit; respect
`prefers-reduced-motion`. No parallax, no bounce.

---

## 4. Design tokens — implementation

### 4.1 CSS custom properties (framework-agnostic)

```css
:root {
  /* brand */
  --brand:#4A35FF; --brand-600:#3E2AE6; --brand-700:#3320C4;
  --brand-lite:#F3F1FF; --brand-wash:#F8F7FF; --brand-100:#EFEDFF;
  --brand-contrast:#C8C0FF; --brand-hairline:#6A55FF;
  /* neutral */
  --foreground:#1A1C1C; --muted:#777589; --border:#EDEEF2;
  --surface:#FFFFFF; --surface-muted:#F7F7FA;
  /* status */
  --success:#00AA44; --success-tint:#E7F6EE;
  --warning:#F57C00; --warning-tint:#FEF2E4;
  --danger:#F10015;  --danger-tint:#FEE9EB;
  --info:#0E8A8A;    --info-tint:#E7F4F4;            /* [PORTAL] */
  /* data-viz categorical */
  --cat-1:#4A35FF; --cat-2:#0E8A8A; --cat-3:#F57C00;
  --cat-4:#00AA44; --cat-5:#8B5CF6; --cat-6:#64748B;
  /* radius / shadow */
  --r-pill:9999px; --r-card:12px; --r-panel:20px; --r-tag:8px;
  --shadow-hover:0 10px 24px rgba(74,53,255,.06);
  --shadow-pop:0 8px 24px rgba(26,28,28,.10);
  --shadow-modal:0 24px 64px rgba(26,28,28,.18);
  /* type */
  --font-head:'Montserrat',sans-serif;
  --font-body:'Geist',-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
}
body{ background:var(--surface); color:var(--foreground); font-family:var(--font-body); }
```

**Theming note.** The system is light-first. If a dark app-chrome is ever required (e.g. a
map-heavy console), do **not** invent a grey dark theme — use `--brand` as the dark surface
with `--brand-contrast` text, exactly as the brand rules require. A true dark mode is out of
scope for v1; add it only with sign-off, defined as a token swap under `:root[data-theme="dark"]`.

### 4.2 Tailwind (v4 `@theme`, or v3 `theme.extend.colors`)

```css
/* Tailwind v4 — app.css */
@theme {
  --color-brand:#4A35FF; --color-brand-lite:#F3F1FF; --color-brand-wash:#F8F7FF;
  --color-brand-foreground:#FFFFFF;
  --color-background:#FFFFFF; --color-card:#FFFFFF; --color-muted:#F7F7FA;
  --color-foreground:#1A1C1C; --color-muted-foreground:#777589; --color-border:#EDEEF2;
  --color-success:#00AA44; --color-warning:#F57C00; --color-danger:#F10015; --color-info:#0E8A8A;
  --font-heading:'Montserrat',sans-serif;
}
```
Then use semantic classes only — `bg-brand`, `text-brand`, `border-border`,
`text-muted-foreground`, `bg-success/10 text-success`, etc. **Never** an arbitrary hex
(`bg-[#4A35FF]`) or a raw gray (`border-gray-200`) anywhere in `src/`.

---

## 5. Core components

Every component below inherits the tokens above. Tailwind classes shown; translate to CSS vars
for other stacks.

### 5.1 Buttons
```html
<!-- Primary -->
<button class="inline-flex h-11 items-center gap-2 rounded-full bg-brand px-6
               font-heading text-sm font-semibold text-brand-foreground
               shadow-[0_8px_20px_rgba(74,53,255,.28)] transition
               hover:bg-brand/90 focus-visible:ring-2 focus-visible:ring-brand/40">
  Read report <svg class="h-4 w-4">…arrow-right</svg>
</button>

<!-- Secondary (outline) -->
<button class="h-11 rounded-full border border-border bg-surface px-6 text-sm font-semibold
               text-foreground transition hover:border-brand/40 hover:text-brand">…</button>

<!-- Tertiary / ghost -->
<button class="h-11 rounded-full px-4 text-sm font-semibold text-muted-foreground
               hover:text-brand hover:bg-brand-lite">…</button>

<!-- On a bg-brand surface (inverted) -->
<button class="h-11 rounded-full bg-brand-foreground px-6 text-sm font-semibold text-brand
               hover:bg-brand-foreground/90">…</button>

<!-- Destructive -->
<button class="h-11 rounded-full bg-danger px-6 text-sm font-semibold text-white
               hover:bg-danger/90">Delete</button>
```
Sizes: `h-9` (compact/tables), `h-11` (default), `h-12` (hero). Always ≥44px touch height on
mobile. Primary buttons carry a trailing arrow on marketing CTAs; app buttons don't need it.
Never uppercase, never a gradient.

### 5.2 Cards
```html
<article class="rounded-2xl border border-border bg-card p-6 transition
                hover:border-brand/40 hover:shadow-[var(--shadow-hover)]">
  <div class="inline-flex h-11 w-11 items-center justify-center rounded-xl bg-brand-lite text-brand">
    <svg class="h-6 w-6">…lucide</svg>
  </div>
  <h4 class="mt-4 font-heading text-lg font-semibold">Card title</h4>
  <p class="mt-2 text-sm leading-relaxed text-muted-foreground">Body…</p>
</article>
```
Uniform padding (`p-6`), uniform heights across a row. Featured variant on `bg-brand`:
`rounded-3xl border border-white/10 bg-white/[0.04] p-8`.

### 5.3 Icon-disc row (from the decks — the workhorse list item)
```html
<div class="flex gap-4">
  <div class="inline-flex h-10 w-10 shrink-0 items-center justify-center rounded-full
              bg-info-tint text-info"><svg class="h-5 w-5">…</svg></div>
  <div>
    <div class="font-heading text-sm font-semibold text-foreground">Row title</div>
    <p class="text-sm text-muted-foreground">One-line description.</p>
  </div>
</div>
```
Disc fill uses the tint matching the row's semantic (brand-lite / info-tint / success-tint /
warning-tint). Icons from **Lucide** only (`stroke=currentColor`, 1.75–2px stroke), sizes
`h-4/5/6`.

### 5.4 KPI / stat tile
```html
<div class="rounded-2xl bg-surface-muted p-5">
  <div class="font-heading text-3xl font-bold tabular-nums text-brand">9,813</div>
  <div class="mt-1 text-sm text-muted-foreground">claims registered, FY 2025-26</div>
</div>
```
Number colour encodes meaning: `text-brand` default, `text-danger` for fatal/critical figures,
`text-success` for positive deltas. Optional Lucide icon top-right, optional delta chip
(`↑ 12%` in success / `↓` in danger).

### 5.5 Chips, tags & status pills
```html
<!-- neutral chip -->
<span class="rounded-full border border-border bg-surface px-3 py-1 text-xs text-muted-foreground">Tag</span>
<!-- brand chip / kicker -->
<span class="rounded-full border border-brand/25 bg-brand/10 px-4 py-1.5 text-xs font-semibold
             tracking-[0.16em] text-brand">OPEN DATA</span>
<!-- status pills -->
<span class="rounded-full bg-success-tint px-2.5 py-1 text-xs font-semibold text-success">Implemented</span>
<span class="rounded-full bg-warning-tint px-2.5 py-1 text-xs font-semibold text-warning">Pending</span>
<span class="rounded-full bg-danger-tint  px-2.5 py-1 text-xs font-semibold text-danger">Critical</span>
<span class="rounded-full bg-info-tint    px-2.5 py-1 text-xs font-semibold text-info">Live</span>
```
**Grade badge** (School Safety Index D/C/B/A): a square `rounded-lg` badge, letter in white on
the tier colour (D `--danger`, C `--warning`, B `--info`, A `--success`), with the word
alongside — colour is never the only signal.

### 5.6 Forms & filters (the portal backbone)
```html
<label class="text-xs font-semibold tracking-[0.12em] text-muted-foreground">STATE</label>
<div class="mt-1.5">
  <select class="h-10 w-full rounded-xl border border-border bg-surface px-3 text-sm
                 text-foreground focus:border-brand focus:ring-2 focus:ring-brand/30">…</select>
</div>

<!-- search -->
<div class="flex h-11 items-center gap-2 rounded-full border border-border bg-surface px-4">
  <svg class="h-4 w-4 text-muted-foreground">…search</svg>
  <input class="w-full bg-transparent text-sm outline-none placeholder:text-muted-foreground"
         placeholder="Search district, road, defect…">
</div>

<!-- checkbox -->
<label class="flex items-center gap-2 text-sm text-foreground">
  <input type="checkbox" class="h-4 w-4 rounded border-border text-brand focus:ring-brand/30">
  Repeat hotspots only (2+ crashes)
</label>
```
Inputs: `rounded-xl`, `border-border`, 40px height, brand focus ring. Error state:
`border-danger` + `text-danger` helper text + an icon. Labels are Montserrat 11–12px tracked.

### 5.7 Caveat / notice strip (a first-class honesty component)
```html
<div class="flex items-center gap-2 border-y border-border bg-brand-wash px-6 py-2.5
            text-sm text-muted-foreground">
  <span class="font-heading text-xs font-bold tracking-widest text-warning">AS REPORTED</span>
  <span>Defects are as reported in news media; locations are indicative pending physical
        audit. Absence of data is absence of coverage — never a safety clearance.</span>
</div>
```
Variants by tint: `warning` (as-reported/pending), `info` (live/beta), `success` (verified),
`danger` (system-down). This is how the CFI honesty rule shows up in product.

### 5.8 Alerts / toasts / empty states
- **Inline alert:** tinted rounded-xl block, left icon, title + body, matching status colour.
- **Toast:** bottom-right, `--shadow-pop`, auto-dismiss ≥5s, status-coloured left border, one
  action link max.
- **Empty state:** centred Lucide icon in a `bg-brand-lite` disc, one-line reason, one action.
  Honest copy — "No records for this filter yet" not "Nothing here!".
- **Skeleton loading:** `--surface-muted` blocks, subtle shimmer, matching the final layout's
  shape. Never a spinner alone for content > 300ms.

---

## 6. Application shell (portal chrome)

### 6.1 Top app bar
```html
<header class="sticky top-0 z-40 flex h-16 items-center justify-between border-b border-border
               bg-surface/95 px-6 backdrop-blur">
  <a class="flex items-center gap-3"><img src="logo_blue.svg" class="h-6" alt="Crashfree India">
     <span class="hidden font-heading text-sm font-bold text-brand sm:block">Defect Repository</span></a>
  <nav class="flex items-center gap-1 text-sm font-semibold">
    <a class="rounded-full bg-brand px-4 py-1.5 text-brand-foreground">Map</a>
    <a class="rounded-full px-4 py-1.5 text-muted-foreground hover:text-brand">Rankings</a>
    <a class="rounded-full px-4 py-1.5 text-muted-foreground hover:text-brand">Method</a>
  </nav>
</header>
```
White bar, brand logo left (blue on white), product name in brand, right-aligned nav where the
**active** item is a filled brand pill and the rest are ghost. On a marketing site the bar may
be transparent over the hero; in an app it is sticky and bordered.

### 6.2 Filter rail + canvas (data-product layout)
```
┌───────────────────────────────────────────────────────────┐
│  Top app bar                                                │
├───────────────────────────────────────────────────────────┤
│  Caveat strip (optional)                                    │
├───────────┬───────────────────────────────────────────────┤
│  KPI row   │                                               │
│  (stat     │              Main canvas                      │
│   tiles)   │        (map / table / chart)                  │
│  ───────   │                                               │
│  Filter    │                                               │
│  rail      │                                               │
│  (selects, │                                               │
│  checkbox) │                                               │
│  ───────   │                                               │
│  Updated   │                                               │
│  DD-MMM    │                                               │
└───────────┴───────────────────────────────────────────────┘
```
Left rail ~280px, `border-r border-border`, KPI tiles stacked at top, then labelled filter
selects, then a footer meta line ("Updated 3 Aug 2026 · 502 hotspots on record"). Canvas fills
the rest. Collapses to a filter drawer under a 768px breakpoint.

### 6.3 Sidebar nav (multi-section apps)
Vertical list; active item = `bg-brand-lite text-brand` with a 3px inset brand marker (not a
full stripe); icon + label; section eyebrows between groups. Never a black sidebar.

---

## 7. Data display

### 7.1 Data table / rankings
```html
<table class="w-full text-sm">
  <thead>
    <tr class="border-b border-border text-left">
      <th class="py-2.5 font-heading text-xs font-semibold tracking-[0.12em] text-muted-foreground">#</th>
      <th class="font-heading text-xs font-semibold tracking-[0.12em] text-muted-foreground">GRADE</th>
      <th class="font-heading text-xs font-semibold tracking-[0.12em] text-muted-foreground">SCHOOL</th>
      <th class="text-right font-heading text-xs font-semibold tracking-[0.12em] text-muted-foreground">SCORE</th>
      <th class="font-heading text-xs font-semibold tracking-[0.12em] text-muted-foreground">STATUS</th>
    </tr>
  </thead>
  <tbody>
    <tr class="border-b border-border hover:bg-surface-muted">
      <td class="py-3 tabular-nums text-muted-foreground">1</td>
      <td><span class="rounded-lg bg-danger px-2 py-0.5 text-xs font-bold text-white">D</span></td>
      <td class="font-medium text-foreground">Triksha Modern Public School</td>
      <td class="text-right tabular-nums font-heading font-semibold">6<span class="text-muted-foreground">/100</span></td>
      <td><span class="rounded-full bg-success-tint px-2.5 py-1 text-xs font-semibold text-success">Verified</span></td>
    </tr>
  </tbody>
</table>
```
Rules: header row `border-b border-border`, muted tracked labels; body rows separated by
`border-border` only (no zebra fills — use `hover:bg-surface-muted`); numeric columns
right-aligned + `tabular-nums`; worst-first ordering for risk lists; sticky header on scroll;
each row's status/grade carries both colour **and** text. Pagination = pill buttons; page-size
select in the rail.

### 7.2 Maps (defect repository / crash clusters / Rakshak sites)
- **Base map:** CARTO Positron (light, muted) — matches the calm light-first system. Attribute
  "© CARTO, © OpenStreetMap contributors" bottom-right in `--muted` 10px.
- **Cluster markers:** filled circles sized by count, coloured by the **danger sequential ramp**
  for crash/fatality density (`#FEE9EB → #F10015 → #A60010`), white bold `tabular-nums` count.
  For non-fatal categories use the brand ramp instead.
- **Selected/hover:** brand outline ring + popover card (`--shadow-pop`) with the record's
  fields and a "view sources" link.
- **Legend:** small, bottom-left, encoding both size (count) and colour (tier), always labelled.
- **Priority tiers:** map the sequential ramp to named tiers (P1–P4); never rely on colour
  alone — the popover states the tier in words.

### 7.3 Charts
- **Library-agnostic**, but style to the tokens: brand for the primary series, danger red for
  the fatal series, `--border` gridlines at 1px, `--muted` axis labels 11px, no chart junk.
- **Bar** (accidents vs deaths): grouped, blue vs red, direct value labels, source line beneath.
- **Line** (trend): 2px brand stroke, dots only at endpoints, area fill `brand/8` optional.
- **Horizontal bar** (claim-rate / comparisons): value + label at the bar end; the "loss" bar
  in `--foreground`, the achieved bar in `--brand`, the settled bar in `--success`.
- **Every chart** carries a title, axis labels, and a `Source: …` caption in `--muted` 8–10px.

### 7.4 The "browser-frame" source card (press / screenshots / portals)
Rounded card, a lavender top bar with three traffic-light dots (`danger/warning/success`) + a
Lucide icon, then `outlet · date`, headline, and an italic note. Use for press hits and for
embedding portal previews. When a real screenshot isn't available yet, label it "screenshot to
be added".

---

## 8. Page composition

### 8.1 Marketing / content pages (brand authority)
Keep the canonical section rhythm and the 3-surface rotation
`bg-background → bg-brand-wash → bg-brand`, each section = **eyebrow → two-line H2 → lead →
grid**, separated by `border-t border-border` (the only divider). Hero may carry the single
allowed gradient — the radial brand glow:
```css
background:radial-gradient(circle at 18% 18%,
  oklch(from var(--brand) l c h / .22), transparent 60%);
```
Standard page order (use what you need, keep the order): Hero → Context → Main feature (cards)
→ Detail grid → Proof/impact (`bg-brand`) → Benefits → Quotes → Process → Quick facts → FAQ →
Final CTA (`bg-brand`) → Footer.

### 8.2 Portal / dashboard pages (this document)
Denser, functional: App bar → optional caveat strip → KPI row → filter rail + canvas → detail
panels/tables → footer meta. Sections are separated by `border-border`, not big whitespace.
The two-line title still opens each distinct view.

---

## 9. Iconography, imagery, motion

- **Icons:** Lucide only, recoloured to the semantic hue via `currentColor`, 1.75–2px stroke.
  Icons in circles use the matching tint fill. Never use Lucide as a stand-in for a real org
  logo (WHO/IIT/MoRTH) — use the real SVG or a typographic name-chip placeholder.
- **Imagery:** real documentary photography over illustration; crop, never stretch; brand-indigo
  overlay (40–60%) or bottom scrim behind overlaid text; caption honestly. No AI-generated
  humans, events, or "photos" presented as real.
- **The sparkle motif** (4-point twinkle, brand) may appear top-right on hero/section-break
  surfaces as a light brand signature — sparingly, never over content.
- **Motion:** short, `ease-out`, functional; honour `prefers-reduced-motion`.

---

## 10. Accessibility (WCAG 2.1 AA — required)

- Contrast ≥ 4.5:1 body / 3:1 large text. Brand on white = 4.5:1 ✓; muted on white ≥ 4.5:1 ✓;
  **white on warning `#F57C00` fails** — use `--foreground` or dark text on warning fills, or
  warning text on a tint. Verify every status-on-fill pairing.
- Colour is never the sole signal — pair with text/icon/shape (grades, statuses, map tiers).
- Focus visible on every interactive element: `ring-2 ring-brand/40 ring-offset-2`.
- Touch targets ≥ 44×44px. Keyboard-operable menus, selects, map controls, modals (focus trap
  + `Esc`).
- Alt text on all images/charts; charts also expose a data table or `aria-label` summary.
- Form fields have `<label>`s; errors announced via `aria-describedby`.
- Respect `prefers-reduced-motion`; never autoplay motion that can't be paused.

---

## 11. Do / Don't (screen build)

**Do**
- Use semantic tokens only (`bg-brand`, `border-border`, `text-muted-foreground`).
- One brand accent; colour everything else by meaning.
- Hairline borders, light surfaces, generous space, tabular numbers.
- Label every status, grade, chart and caveat.
- Lead with the number / the map / the status.

**Don't**
- No arbitrary hex or raw grays in code (`bg-[#4A35FF]`, `border-gray-200`).
- No extra decorative accents; teal/status/data colours are for data & states only **[PORTAL]**.
- No dark grey/black surfaces — the only dark surface is `bg-brand`.
- No gradients except the hero radial glow; no rest-state drop shadows; no shadowed text.
- No new fonts; no uppercase on the brand name; no emoji in UI chrome.
- No unlabelled charts, colour-only status, or stretched images.

---

## 12. Component checklist (ship gate)

- [ ] Tokens only — no hex/gray literals; borders are `--border`.
- [ ] Montserrat headings / Geist body; two-line title where a header opens a view.
- [ ] 4px spacing; radius per §3; rest = border, hover = tinted shadow.
- [ ] Every status/grade/map-tier has colour **and** text.
- [ ] Numbers are `tabular-nums`; risk lists sort worst-first.
- [ ] Caveat strip present where data is "as reported"/cached/beta.
- [ ] Focus rings, 44px targets, labelled inputs, alt text, chart summaries.
- [ ] Contrast verified (watch white-on-warning).
- [ ] Responsive at 375 / 768 / 1280; rail collapses to a drawer on mobile.
- [ ] Charts/maps carry title, labels, legend, and a `Source:` line.

---

*Crashfree India — Web & Portal UI Design System v1 · 2026-08-03.*
*Grounded in the canonical CFI Design System (brand authority: colours, type, tone, marketing
components). This document adds the portal/app layer — app shell, tables, filters, maps, KPIs,
charts, forms, status systems — reconciled to the brand. Extensions beyond the marketing-site
rules are flagged **[PORTAL]** and are scoped to data and status semantics only.*

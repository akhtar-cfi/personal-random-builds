# Crashfree India — Organisation Context & Overview Deck

A single place holding the complete context of what Crashfree India (CFI) is, does,
and has achieved — distilled from ~30 internal documents, the public web, and press —
plus the investor/grantee overview deck built from that context.

## What's here

### `deck/`
- **`CFI_Overview-Deck_Investors-Grantees_v1_2026-07-28.pptx`** — the 15-slide overview deck
  ("Crashfree India — Systems work because we hold them accountable."), built to the CFI
  design system (Montserrat/Geist, brand indigo #4A35FF, 16:9).
- Matching PDF export (fonts embedded — safest for sharing).
- **`CFI_NRSB-WG2-Application_v6_2026-08-02.pptx`** and
  **`CFI_NRSB-WG5-Application_v6_2026-08-02.pptx`** (28 and 26 slides) — the current NRSB
  Working Group application decks (letter-first structure, running agenda, all initiatives
  covered, white/low-blue design). Built by `build_nrsb6.py` + `nrsb2_style.py`; slide-by-slide
  spec and validated numbers in `NRSB_V2_SPEC.md`. Earlier versions kept for history; chair-profile
  research in `research/briefs/L-nrsb-chairs.md`.
- `assets/v5/` — the classified photo library (Road Safety Month campaigns, helpdesk camps,
  ideathon, Dhoni studio shots, screenshots incl. the live SC-tracker capture) plus
  `deckready/` crops used by the v2 decks. **Reuse these for future decks.**
- `build_deck.py` / `build_nrsb.py` + `cfi_helpers.py` — the python-pptx build system.
  Edit a script, run it, and the deck regenerates. `DECK_SPEC.md` is the slide-by-slide
  narrative spec with the canonical numbers used.
- `assets/` — official logo (blue + white), CFI's India coverage map, Dhoni announcement
  creative, plus `assets/v3/` (extracted photos, headshots, approval letters, screenshots).

### `research/briefs/`
Dense research briefs, one per theme — together they are the "complete context" corpus:

| Brief | Covers |
|---|---|
| A-identity-impact | Mission, origin, team roster, impact report, investor framing |
| B-strategy | AOP 2026-27, quarterly updates, current bets vs deprioritised work |
| C-satark-datastack | SATARK enforcement platform + 4 open-data public goods |
| D-rakshak | Project Rakshak: model, funnel, approvals, implementations |
| E-justice-compensation | Justice Unserved, hit-and-run pipeline work, Aasha, calculator |
| F-engagement | Guidebooks, comics, forums, NextMile, Dhoni ambassadorship |
| G-master-misc | Legacy master deck, gig-rider research (historical), misc docs |
| H-web-boa-press | Website content, Board of Advisors bios, verified press list |
| I-storytelling | Narrative frameworks research behind the deck's arc |
| K-team-profiles | Public-profile verification for every team member & trustee |
| L-nrsb-chairs | NRSB Working Group chairperson research (for the WG-2 / WG-5 application decks) |

## Rebuilding the deck

```bash
pip install python-pptx cairosvg fonttools brotli pillow
cd deck && npm install lucide-static
python3 build_deck.py          # writes CFI_Overview.pptx
```

Fonts: Montserrat (Google Fonts / `@fontsource/montserrat`) and Geist (Vercel / npm `geist`)
must be installed for correct rendering.

## Verify-before-presenting notes

Numbers in the deck use the most recent internal source when documents disagree
(details per brief). Items flagged for internal confirmation before high-stakes use:
Board of Advisors titles, Gajendra Jangid's current Cars24 role/education line,
"150+ members", and the Moneycontrol byline (Scroll.in is the verified one).

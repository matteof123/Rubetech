# RubeTech Partners — Outbound Campaigns

## Sync Update — 2026-05-12

**Status: Pre-launch. Launch target May 20, 2026.**

No active campaigns in EmailBison yet. Infrastructure being provisioned. This file becomes the operational source of truth once the first campaign launches.

### Planned Campaign Structure

| ID | Campaign | Status | Wave | Vertical(s) | Offer | Target launch |
|----|----------|--------|------|-------------|-------|---------------|
| TBD | RubeTech — Healthcare + Vet | Not yet created | Wave 1 | Healthcare V1 + Veterinary V2 | Fractional CTO | 2026-05-20 |
| TBD | RubeTech — Consumer + FinServ | Not yet created | Wave 2 | Consumer V3 + FinServ V5 | Fractional CTO + RevOps Build | 2026-05-27 (1 week after Wave 1) |
| TBD | RubeTech — HR Staffing (test) | Not yet created | Wave 3 | HR Staffing V4 | RevOps Build | After Wave 1+2 metrics review |

### Infrastructure

- **EmailBison workspace:** Not yet created. To be provisioned in `@kinetyca-inboxedup` setup.
- **Sending power:** 4k emails/day target (per Slack request).
- **Senders (2):**
  - Daniel Rubenstein, Managing Partner — https://www.linkedin.com/in/daniel-rubenstein-8316a44b/
  - Joseph Rios, Partner
- **Domains:** 20 provisioned (see `tech-docs/infra-setup.md`). Split: Google ESP for warm-up + main sends, Outlook ESP as secondary.
- **HubSpot pipeline:** Lead → SQL → Discovery → Brief → Closed.
  - Owner Joey (qualify, under $10M)
  - Owner Dan (close, $10M+)
- **Slack alerts:** Same-day SLA for positive replies, alert channel: Dan + Joseph + Matteo + David.
- **Aircall:** Connected for outbound calling follow-up.

### Sequence Plan (per planned campaign)

- Email 1: Lead magnet — Free 15-Minute Revenue Leak Audit, vertical-specific subject (max 3 words, lowercase except company/person names).
- Email 2: New thread, new subject. Service offer (Fractional CTO or RevOps Build), vertical-specific proof point.
- Email 3: New thread, breakup. "Last note."
- LinkedIn parallel sequence (HeyReach or similar): Message 1 + Message 2.

Full templates per vertical in [`email-sequences/rubetech-templates.md`](../email-sequences/rubetech-templates.md).

### Pre-launch Tasks (Affan)

- Database Building — https://app.clickup.com/t/868jea1a7
- Campaign Setup — https://app.clickup.com/t/868jea0tv
- EmailBison warmup verification (first-time Bison user — Matteo to cross-check settings)

### Reporting Cadence

- Weekly sync: Wed 12pm ET (Dan + Joseph + Matteo + David)
- Metrics: sent / positive replies / meetings booked / SQLs
- Vertical breakdown: Healthcare / Veterinary / Consumer Services / Staffing / FinServ
- Cost log: enrichment + copy + sending costs per run
- Goal: 3–4 qualified opps / month → $1.5M ARR in 12 months

### Test Hypotheses (Wave 1 — to validate)

| Hypothesis | How to validate |
|------------|-----------------|
| Vertical-specific hook ("branches HubSpot") outperforms generic ("operational efficiency") | A/B test Email 1 hooks |
| Healthcare emails with Alliance Homecare proof point (88% lift) outperform generic Healthcare emails | Compare reply rates within Healthcare segment |
| 15-Minute Revenue Leak Audit converts higher than 30-min Discovery → Brief | Run both offers in parallel on Email 1 (50/50 split) |
| Email 2 service offer ($6.5K/mo soft offer) converts higher than $22.5K Transformation offer | Default Email 2 to Advisory tier; mention Transformation only when signals fit |
| Operator-to-operator tone (Dan as ex-founder) outperforms consultant-style tone | Use Dan's voice in Email 2; compare against Joey's voice |

### Past Outbound (Scrapped — Reference Only)

Historical activity from the pre-Kinetyca period — DO NOT reuse copy, lists, or domain. Documented for diagnostic purposes only.

| Source | Volume | Reply | Outcome |
|--------|--------|-------|---------|
| Seamless AI cold list (manual) | 250 / 30 days | 1 proposal | Lost |
| LinkedIn DMs | 50+ | 2 responses | Did not convert |
| Claude AI manual emails | 500 | 3 responses | Did not convert |
| Google Ads + LinkedIn Ads | Brief test | — | Shut down |
| In-person networking | — | 2 leads | Unqualified by revenue size |

**Root causes (Apr 27 + May 1 calls):**
- Targeting too broad (Seamless lists not vertical-segmented)
- Copy was generic — no vertical-specific hook, no vertical-specific proof
- No infrastructure (single domain, no warm-up, no sending limits)
- Volume too low to learn (500 across 5 verticals = 100 per segment, no statistical signal)

Decision: scrap all historical lists, copy, and domain. Rebuild from clean Kinetyca-provisioned infra + vertical segments + 50–80 word copy.

---

### Interested Replies — Email — 2026-05-12

_None yet — pre-launch._

| # | Person | Title | Company | Campaign | City/Region | Quote |
|---|--------|-------|---------|----------|-------------|-------|

### LinkedIn Campaigns — 2026-05-12

_None yet — pre-launch._

**LinkedIn Metrics (HeyReach or similar):**

| Campaign | Sender | Leads | Contacted | Conn Sent | Conn Accepted | Conn Rate | Msgs Sent | Replies | Response Rate |
|----------|--------|-------|-----------|-----------|---------------|-----------|-----------|---------|---------------|

---

**Next sync update:** Post-launch (target 2026-05-27, 1 week after Wave 1 launch). Will include real BEFORE/AFTER copy pulled from actual sent emails once Wave 1 sends start.

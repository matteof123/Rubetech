# RubeTech Partners — Campaign Optimization Report (May 2026 — Baseline)

> Generated: 2026-05-12
> Status: Pre-launch baseline. Captures historical (pre-Kinetyca) outbound failures + first-launch hypotheses. Next report after Wave 1 metrics review (target 2026-05-27).

This is the diagnostic baseline before clean relaunch May 20, 2026. It exists to document what was tried, what failed, why, and what we are doing differently. After the first 2 weeks of clean data, this report's hypotheses become testable.

---

## 1. Historical Performance (Pre-Kinetyca, Scrapped)

| Source | Volume | Reply | Positive | Notes |
|--------|--------|-------|----------|-------|
| Cold email (Seamless AI list, manual) | 250 in 30 days | 1 proposal | 0 closed | Lost the proposal. Targeting was construction + generic mid-market. |
| LinkedIn DMs | 50+ | 2 | 0 closed | Generic outreach, no signal-trigger. |
| AI-written cold emails (Claude, manual) | 500 | 3 | 0 closed | Sent across 5 verticals (~100/segment). No statistical signal. |
| Google Ads + LinkedIn Ads | Brief test | n/a | 0 | Shut down — no attribution. |
| In-person networking | n/a | 2 leads | 0 | Unqualified by revenue size. |

**Aggregate:** 800+ outbound touches over 30+ days → 5–7 total replies → 1 proposal → lost.

---

## 2. Root Cause Analysis (from Apr 27 + May 1 calls)

### Targeting failures
- **Lists were not vertical-segmented.** Seamless AI returned generic mid-market companies, not the specific subverticals where RubeTech has existing clients (Home Care, specialty Vet, premium Pet, behavioral health).
- **No size filter.** Some leads were under $5M revenue (below the RevOps Build floor) and some were enterprise (above the Fractional CTO ceiling). Wrong-size leads cannot buy these offers at the listed price.
- **No signal-trigger.** Outreach was list-based, not event-based. The leads were not in a "buying window" (post-Series-A, opening location #3, new VP Ops hire, etc.).

### Copy failures
- **Generic hooks.** "Operational efficiency" / "scale your business" / "modernize your tech stack" — language that any consulting firm could send.
- **No vertical-specific proof.** Healthcare buyers needed Alliance Homecare evidence; vet buyers needed Upstate-style evidence. Generic case study mentions converted poorly.
- **No personalization layer.** The Claude AI batch was AI-written but generic per prospect. No per-lead research (recent expansion, new hire, vertical context).
- **CTAs too vague.** "Open to a chat?" instead of "15-minute audit, we'll flag 3 specific places revenue is leaking."

### Infrastructure failures
- **Single domain.** All 250 Seamless emails sent from one domain. Deliverability degrades after volume.
- **No warm-up.** Cold sends started immediately, before domain reputation was established.
- **No sending limits.** 50+ per day from one inbox triggered ESP throttling.

### Volume failures
- **Too low to learn.** 500 emails across 5 verticals = 100 per vertical. With a 1% positive reply rate, that's expected 1 positive per vertical — not enough statistical signal to know which vertical works.

---

## 3. What We're Changing for Wave 1 (May 20 Launch)

### Targeting
- **Vertical segmentation:** Wave 1 = Healthcare + Veterinary ONLY. Wave 2 (1 week later) = Consumer Multi-Location + FinServ. Each vertical gets a distinct campaign with its own copy.
- **Size filter:** $10M+ revenue for Fractional CTO segments; $1M–$50M for RevOps Build segments. Hard cut at $5M floor.
- **Signal triggers:** Each lead enriched with at least 1 of: opening Nth location (2+), new C-suite hire (last 90 days), Series A/B in last 12 months, recent EMR/PMS/ATS purchase, AI/ML hiring posts.
- **Geography:** Northeast US (CT, NY, NJ, MA, PA) for Healthcare + Vet + Consumer; national for FinServ + RevOps Build.

### Copy
- **Vertical-specific hooks per template:** "branches HubSpot" / "hospital #3" / "location #4" / "ATS HubSpot" / "Board roadmap." Each subject + Email 1 hook are templated per vertical.
- **Per-lead research:** Every lead gets at least 1 personalized line (recent expansion, hire, capital event). Powered by Gemini Flash on `/write-copy` step.
- **Vertical-matched proof:** Healthcare emails reference Alliance Homecare (88% revenue lift). Vet emails reference Upstate Vet or general specialty-vet ops layer. Consumer references Pups Pet Club. FinServ references Stitch Payments. No cross-vertical proof.
- **50–80 word limit.** No em dashes. No exclamation marks. No bracket placeholders.
- **CTA = specific 15-minute audit.** "We flag 3 specific places revenue is leaking" — concrete deliverable, low friction.

### Infrastructure
- **20 domains provisioned**, split Google ESP / Outlook ESP for redundancy.
- **2 senders:** Daniel Rubenstein, Joseph Rios.
- **4k emails/day sending power** target.
- **Warm-up done before sends start** (Affan to cross-check EmailBison warmup settings before May 20).
- **Sending limits:** Per EmailBison defaults — start conservative, ramp by week.

### Volume
- **First wave:** 50 leads per vertical, 2 verticals = 100 leads. Statistical floor for first-round learning.
- **Wave 2:** Add 100 more (Consumer + FinServ).
- **By end of Month 1:** 400+ leads across 4 active verticals. Enough volume to identify which vertical converts best and double down.

---

## 4. Hypotheses to Validate (Post-Launch)

| # | Hypothesis | How we'll measure |
|---|------------|-------------------|
| 1 | Healthcare V1 will have highest positive reply rate (best existing case study + most pain) | Compare reply rates Wave 1: Healthcare vs Vet |
| 2 | Specialty Vet V2 will have highest meeting-book rate (very tight ICP fit, less competition) | Track meetings booked / replies received |
| 3 | "15-Minute Revenue Leak Audit" lead magnet outperforms "Discovery → Brief" | A/B test on Email 1 |
| 4 | Email 1 (audit, low-friction) generates more replies than Email 2 (service offer) but Email 2 generates higher-quality replies | Classify replies by step + by classification (positive / negative / OOO) |
| 5 | Operator-to-operator tone (Dan voice) outperforms agency tone (Joey voice) | A/B test sender attribution on Email 2 |
| 6 | Multi-location signal converts higher than capital-raise signal for Healthcare buyers | Tag leads by trigger; compare reply rates |
| 7 | Vertical-matched proof point (Alliance Homecare for Healthcare) drives 2x more replies than generic SCALE framework outcomes | Compare emails using Alliance reference vs generic |

---

## 5. Risk Watch (post-launch)

- **Bounce rate target: <3%.** If verification waterfall (BlitzAPI → Debounce → FindyMail → LeadMagic → BounceBan) is skipped, prior client saw 31% bounce rate. Affan must run full waterfall before sends.
- **Spam complaint rate target: <0.1%.** Subject lines flagged: avoid "$", "free," "guaranteed." Avoid mentioning competitors directly.
- **OOO inflation in metrics.** Northeast US prospects, English-only — minimal OOO inflation expected (no EU multilingual auto-replies). But still classify OOOs separately.
- **HIPAA-sensitive language in Healthcare emails.** Never imply RubeTech has access to patient data. Never accuse a prospect of a HIPAA gap. Frame as "real-time census" + "billing leakage" — operational language, not compliance accusation.

---

## 6. Optimization Recommendations (Pre-Launch — to validate after May 20)

These are starting hypotheses. The next optimization report (after Wave 1 metrics) will replace these with evidence-based BEFORE/AFTER recommendations grounded in actual sent emails and actual replies.

### Hypothesis A — Healthcare Email 1: Branch-count hook
**Hypothesis BEFORE (template):**
```
Subject: branches HubSpot
Hi [First Name], saw [Company] runs [N] home care locations. Most operators at this size pay $25-50K/yr for HubSpot that 80% of the team ignores. We help groups like Alliance Homecare get to a single live revenue view in 4 weeks. 15-min audit?
```
**Will A/B test against AFTER (variation):**
```
Subject: branch P&L
Hi [First Name], [Company] runs [N] branches. The pattern: each branch P&L lives in a different QuickBooks file, and consolidation happens on Sunday nights in Excel. We rebuilt that for Alliance Homecare and they had a live revenue view in 4 weeks. 15-min audit?
```
**Reason for test:** "branches HubSpot" pulls attention to the HubSpot pain. "branch P&L" pulls attention to the financial visibility pain. We don't yet know which pain Home Care CEOs feel more acutely. Test on 25 leads each.

### Hypothesis B — Vet Email 1: Location hook vs PIMS hook
**BEFORE (template):**
```
Subject: hospital #3
Hi [First Name], [Company] opening your 3rd hospital is the point where most specialty groups break...
```
**AFTER (variation to test):**
```
Subject: PIMS migration
Hi [First Name], saw [Company] is migrating off [old PIMS] to [new PIMS]. That migration is the only good window to rebuild the reporting layer underneath it...
```
**Reason:** PIMS-migration is a sharper signal than location-count. But not every lead has a documented PIMS migration. Test PIMS-hook only on leads where we have explicit PIMS-migration signal; keep location-count hook on the rest.

### Hypothesis C — FinServ Email 1: Roadmap framing vs CTO-cost framing
**BEFORE:**
```
Subject: Board roadmap
Hi [First Name], [Company] just raised, board wants AI and tech roadmap in 60 days, CTO seat is open...
```
**AFTER (variation):**
```
Subject: CTO math
Hi [First Name], hiring a full-time CTO at $400K-plus for 12 months when you only need a 60-day roadmap and a couple of quick wins is a $300K overpay. Our managing partner has run that math, with 4 exits. 15-min look?
```
**Reason:** Roadmap framing leads with the deliverable; CTO-cost framing leads with the financial pain. We don't know which lands harder on post-Series-A founders. Test on 25 leads each.

---

## 7. Pre-Launch Checklist (before May 20)

- [ ] Database build complete (Affan — ClickUp 868jea1a7)
- [ ] Campaign setup complete (Affan — ClickUp 868jea0tv)
- [ ] EmailBison workspace `rubetech` provisioned + verified
- [ ] All 20 domains warmed up minimum 14 days
- [ ] Sender profiles configured (Dan Rubenstein, Joseph Rios)
- [ ] HubSpot pipeline stages set: Lead → SQL → Discovery → Brief → Closed
- [ ] Joey HubSpot pipeline ownership confirmed
- [ ] Slack alert channel + same-day SLA agreed
- [ ] Wave 1 copy drafts shared with Dan for review
- [ ] Wave 1 leads enriched + verified (BlitzAPI → Debounce → FindyMail → LeadMagic → BounceBan)
- [ ] Sample copy approved by Matteo (per autonomy rules, this is the only checkpoint)
- [ ] Aircall connected for follow-up calls
- [ ] Weekly Wed 12pm ET sync calendar invite sent

# RubeTech Partners — Client Brain

Strategic outbound intelligence for RubeTech Partners — Fractional CTO + HubSpot RevOps for $10M–$200M Northeast US mid-market.

## Contents

| File | Purpose |
|------|---------|
| `Rubetech_GTM_Playbook.pdf` | Definitive GTM playbook — 5 verticals, 12 personas, pain-to-value maps, signal triggers, messaging angles |
| `generate_gtm_playbook.py` | ReportLab generator — re-runnable when intelligence is updated |
| `miro/update_process_flow.py` | Miro API script that filled the Kinetyca Process flow view (16 stickies) for RubeTech |
| `miro/update_other_frames.py` | Miro API script that replaced Mendel content in 4 other frames (29 stickies) |

## Quick facts

- **Founded:** Aug 2025 · Dan Rubenstein (Managing Partner — 27y, 4 exits) + Joseph Rios (Partner)
- **Revenue:** $300K pace → $1.5M target in 12 months
- **Avg deal:** $100K · 25% close rate · 60–90 day cycle
- **Geography:** Northeast US (CT, NY, NJ, MA, PA) for Fractional CTO; national for RevOps
- **5 priority verticals:** Specialty Healthcare · Specialty Veterinary · Multi-Location Consumer Services · HR Staffing · FinServ/Payments

## Productized offers

| Offer | Tier | Price | Term |
|-------|------|-------|------|
| Fractional CTO | Advisory | $6.5K/mo | 12-mo min |
| Fractional CTO | Embedded | $12.5K/mo | 9-mo min |
| Fractional CTO | Transformation | $22.5K/mo | 6-mo min |
| HubSpot RevOps Build | Foundation | $12.5K one-time | 2–4 weeks |
| HubSpot RevOps Build | Growth | $22.5K one-time | 8–12 weeks |

## Lead magnet

**Free 15-Minute Revenue Leak Audit** — Live Zoom, no prep, Dan delivers 3 specific findings (where they're losing money, where they're wasting time, what to fix first).

## Existing customers (used for vertical proof)

Alliance Homecare (Healthcare — 88% revenue increase) · Trusthouse (Healthcare/Behavioral) · Pups Pet Club (Multi-Location Consumer) · CorCon USA (Construction pilot) · Calendar Group (Concierge)

## Miro board

The full Rubetech Miro GTM board has been populated end-to-end:

- **Board:** [Rubetech | Analysis](https://miro.com/app/board/uXjVHbhe9MU=/)
- **Process flow view:** all 16 sticky notes replaced with RubeTech content (lead magnet, Email 1/2, Message 1/2, signal angles, HubSpot wiring, Slack alerts, reporting cadence)
- **Analysis & Target frame:** 16 stickies — verticals, sizes, geos, anchors per vertical
- **Atlas Infrastructure frame:** 3 stickies — email/LinkedIn infra setup
- **Database Creation frame:** 3 stickies — sourcing, Smartlead DB, lookalikes
- **Signals & Evergreen frame:** 7 stickies — past champions, conferences, re-engage lists
- **Total: 45 stickies replaced — 0 cross-client contamination remaining**

## Re-running

Set `MIRO_TOKEN` and re-run any of the Miro scripts to refresh sticky content. Re-run `generate_gtm_playbook.py` after any intelligence update.

```bash
export MIRO_TOKEN="..."
python3 generate_gtm_playbook.py
python3 miro/update_process_flow.py
python3 miro/update_other_frames.py
```

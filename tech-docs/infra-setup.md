# RubeTech Partners — Infrastructure Setup

> Last updated: 2026-05-12
> Source: Drive `Infra Setup [Rubetech].xlsx`, Drive `rubetech_domains.csv`, Slack `#kinetyca-inboxedup`

This is the operational reference for the outbound infrastructure: domains, ESP allocations, sender profiles, sending limits, and tool integration.

---

## Senders (2)

| Sender | Role | LinkedIn | Use in campaigns |
|--------|------|----------|------------------|
| Daniel Rubenstein | Managing Partner | https://www.linkedin.com/in/daniel-rubenstein-8316a44b/ | Email 1 + Email 2 — operator voice, primary closer narrative |
| Joseph Rios | Partner | (LinkedIn URL TBD — confirm with team) | Email 3 + Email 4 — qualification voice; also primary HubSpot pipeline owner |

## Domains (20)

20 candidate domains identified and provisioning. Split across ESPs for redundancy and warmup.

### Google ESP (primary — main sending)

| Domain | Status |
|--------|--------|
| getrubetech.com | Provisioning |
| therubetech.com | Provisioning |
| gorubetech.com | Provisioning |
| joinrubetech.com | Provisioning |
| rubetechhq.com | Provisioning |
| rubetechlabs.com | Provisioning |
| rubetechgroup.com | Provisioning |
| rubetechpro.com | Provisioning |
| rubetechhub.com | Provisioning |
| rubetechstudio.com | Provisioning |
| rubetechworks.com | Provisioning |

### Outlook ESP (secondary)

| Domain | Status |
|--------|--------|
| rubetechsolutions.com | Provisioning |
| rubetechglobal.com | Provisioning |
| rubetechventures.com | Provisioning |
| rubetechdigital.com | Provisioning |

### Unassigned (TBD ESP)

| Domain | Status |
|--------|--------|
| rubetechcore.com | Provisioning |
| rubetechagency.com | Provisioning |
| teamrubetech.com | Provisioning |
| rubetechservices.com | Provisioning |
| rubetechco.com | Provisioning |

## Sending Power

- **Target:** 4,000 emails/day across all domains
- **Per-domain:** Conservative ramp during warm-up. Per `kinetyca-inboxedup` defaults: start at 30/day per inbox, ramp to 50/day after 14 days warm-up.
- **Warm-up requirement:** Minimum 14 days before any cold send.

## Tool Integration

| Tool | Purpose | Status |
|------|---------|--------|
| EmailBison | Campaign sending | Workspace to be provisioned (no `emailbison_rubetech` MCP server yet) |
| HubSpot | CRM + pipeline | In use by RubeTech. Matteo + Affan have access. Pipeline: Lead → SQL → Discovery → Brief → Closed. |
| Aircall | Outbound follow-up calling | Connected. Matteo + Affan added per May 1 call. |
| Clay | Lead routing + flagging for HubSpot | In use per May 7 call. Routes flagged leads to Joey. |
| Slack | Coordination + alerts | Channel "Kinetyca Rubetech Connecticut" created May 1. Alerts: Dan + Joseph + Matteo + David. |
| Fireflies | Call transcripts | Active. 4 calls captured (Apr 22, Apr 27, May 1, May 7). |
| Drive | Document storage | Folder: https://drive.google.com/drive/u/0/folders/1mn05KV2Qw-e1UHgg4GdEay7tAjh4YdYr |
| ClickUp | Task tracking | Database Build (868jea1a7) + Campaign Setup (868jea0tv) — owner Affan |
| Seamless AI | Legacy list source | Access shared for diagnostic. NOT to be used as source going forward — replaced by Kinetyca enrichment waterfall. |

## Enrichment Waterfall (mandatory order — non-skippable)

Per `.claude/rules/copy-rules.md` and prior client incident (31% bounce rate when skipped):

1. **BlitzAPI** — lead sourcing + initial enrichment
2. **Debounce** — first-pass email verification
3. **FindyMail** — secondary email finding for unverified
4. **LeadMagic** — tertiary email finding for still-unverified
5. **BounceBan** — final bounce risk verification

Affan to run this before any sends. STOP if any service has no credits.

## Pre-Launch Checklist

- [ ] All 20 domains DNS-verified (SPF, DKIM, DMARC)
- [ ] Domain warm-up minimum 14 days complete
- [ ] EmailBison workspace `rubetech` provisioned
- [ ] Sender profiles (Daniel Rubenstein, Joseph Rios) configured in EmailBison
- [ ] HubSpot pipeline stages confirmed: Lead → SQL → Discovery → Brief → Closed
- [ ] HubSpot pipeline owner assignment: Joey (qualify), Dan (close $10M+)
- [ ] Slack alert webhooks configured (same-day SLA on positive replies)
- [ ] Aircall integration confirmed (click-to-call for follow-up)
- [ ] Clay routing rules confirmed (criteria for "flagged" leads)
- [ ] Affan EmailBison warm-up settings cross-checked by Matteo

---

## Outstanding Questions

- Joseph Rios LinkedIn URL — needed for HeyReach LinkedIn sequences.
- Exact Clay flagging criteria — required for matching `/write-copy` personalization data to HubSpot routing logic.
- Whether HeyReach is the chosen LinkedIn sending tool or another platform.
- Final domain ESP assignment for the 5 currently unassigned domains.

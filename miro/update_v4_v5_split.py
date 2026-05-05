#!/usr/bin/env python3
"""
Split the duplicate FinServ column into:
  col 4 (x=5984) → HR Staffing & Recruiting
  col 5 (x=7215) → FinServ & Payments (keep)

Also fill the new Case Studies + Triggers rows for all 5 columns.
Rebalance Focus %s to total 100.
"""
import os, json, subprocess, time

MIRO_TOKEN = os.environ["MIRO_TOKEN"]
BOARD_ID = "uXjVHbhe9MU%3D"
BASE = f"https://api.miro.com/v2/boards/{BOARD_ID}/sticky_notes"

# Final 5-column layout (left → right):
#   col 1 (x=2128) → Specialty Healthcare        (35%)
#   col 2 (x=3206) → Specialty Veterinary        (25%)
#   col 3 (x=4753) → Multi-Loc Consumer Services (20%)
#   col 4 (x=5984) → HR Staffing & Recruiting    (10%) ← swap from FinServ
#   col 5 (x=7215) → FinServ & Payments          (10%)

UPDATES = {
    # ─────────── Column 4 — re-purpose from FinServ to HR Staffing ───────────
    "3458764670490064140": (   # header
        "<p><strong>HR Staffing &amp; Recruiting</strong></p>"
    ),
    "3458764670490064141": (   # industries
        "<p>Healthcare Staffing · Executive Search · "
        "Specialty / Technical Recruiting · "
        "Light Industrial Staffing · MSP / VMS providers</p>"
    ),
    "3458764670490064142": (   # decision-makers
        "<p><strong>Decision-Makers (Staffing)</strong></p>"
        "<p>1. CEO / Founder · Specialty Staffing</p>"
        "<p>2. RevOps Director / VP Operations</p>"
        "<p>3. Director of Recruiting / Talent Acquisition Lead</p>"
        "<p>4. New VP Sales (post-funding)</p>"
        "<p>Champion: ATS Admin · CRM Manager</p>"
    ),
    "3458764670490064143": (   # co. size
        "<p><strong>Co. size</strong></p>"
        "<p>$5M–$25M revenue · 15–150 employees · expanding branches "
        "OR new MSP contract · multi-state recruiting · "
        "ATS already in place but unintegrated</p>"
    ),
    "3458764670490064155": (   # geography (was at col 4 position)
        "<p><strong>Geography</strong></p>"
        "<p>National (recruiting is remote-first) · "
        "preference for NYC / Boston / Stamford / Chicago metros · "
        "Northeast HQs prioritized for FCTO upsell</p>"
    ),
    "3458764670490064167": (   # focus %
        "<p>10%</p>"
    ),
    "3458764670490064172": (   # UVP / vertical anchor
        "<p><strong>HR Staffing anchor</strong></p>"
        "<p>ATS-to-CRM-to-billing integration in 4 weeks · "
        "source-of-hire attribution · automated hours/billing for "
        "contract placements · stop double-keying candidates between "
        "ATS and HubSpot. Offer fit: RevOps Build (primary) → "
        "Fractional CTO (upsell at $10M+).</p>"
    ),

    # ─────────── Column 5 — keep FinServ but adjust focus % ───────────
    "3458764670491912395": (   # focus %
        "<p>10%</p>"
    ),
    # Other col 5 stickies (3458764670491912390/91/92/93/94/96) already have
    # correct FinServ content — leave them.

    # ─────────── Column 1 — rebalance focus % from 40% to 35% ───────────
    "3458764670490064163": (
        "<p>35%</p>"
    ),

    # ═══════════════════════════════════════════════════════════════
    # CASE STUDIES row (y=9985) — fill 5 columns
    # ═══════════════════════════════════════════════════════════════
    "3458764670491912013": (   # col 1 — Healthcare
        "<p><strong>Healthcare</strong></p>"
        "<p>· <strong>Alliance Homecare</strong> — 88% revenue increase "
        "in 7 months (existing client)</p>"
        "<p>· <strong>Trusthouse</strong> — behavioral health systems rebuild "
        "(existing client)</p>"
        "<p>· $1.3M revenue lift projected on active engagement</p>"
        "<p>· Industry report: \"State of AI in Private Healthcare\"</p>"
    ),
    "3458764670491912051": (   # col 2 — Veterinary
        "<p><strong>Veterinary</strong></p>"
        "<p>· <em>Gap — develop case study before scaling outbound.</em></p>"
        "<p>· Borrow proof: 88% revenue lift from Alliance "
        "(adjacent multi-location)</p>"
        "<p>· Borrow proof: Pups Pet Club (multi-unit pet services)</p>"
        "<p>· Use Dan's 27y operator credentials as anchor</p>"
    ),
    "3458764670491912122": (   # col 3 — Multi-Loc Consumer
        "<p><strong>Multi-Loc Consumer</strong></p>"
        "<p>· <strong>Pups Pet Club</strong> — multi-unit pet services ops "
        "(existing client)</p>"
        "<p>· <strong>Calendar Group</strong> — concierge / staffing "
        "services (existing client)</p>"
        "<p>· 20–50+ hrs/wk manual work eliminated per location</p>"
        "<p>· 30–90 day payback period (standard)</p>"
    ),
    "3458764670491912137": (   # col 4 — HR Staffing
        "<p><strong>Staffing</strong></p>"
        "<p>· <em>Gap — develop case study before scaling outbound.</em></p>"
        "<p>· Borrow proof: HubSpot RevOps Build pattern "
        "(applies industry-agnostic)</p>"
        "<p>· Borrow proof: Dan's 4 exits, all built on integrated "
        "ATS/CRM/billing systems</p>"
        "<p>· Conservative 30–90 day ROI math</p>"
    ),
    "3458764670491912397": (   # col 5 — FinServ
        "<p><strong>FinServ / Payments</strong></p>"
        "<p>· <em>Gap — develop case study before scaling outbound.</em></p>"
        "<p>· Anchor proof: Dan's 27y building infra · 4 founder "
        "exits · 8-figure PE exit</p>"
        "<p>· Anchor proof: ex-Accenture (knows what big consulting "
        "delivers and what they don't)</p>"
        "<p>· Aircall partner · OpenAI / n8n integration capability</p>"
    ),

    # ═══════════════════════════════════════════════════════════════
    # TRIGGERS row (y=10631) — fill 5 columns
    # ═══════════════════════════════════════════════════════════════
    "3458764670491912597": (   # col 1 — Healthcare
        "<p><strong>Healthcare triggers</strong></p>"
        "<p>· Hiring CTO / VP IT / RevOps</p>"
        "<p>· Recent EMR or PMS purchase (no integration)</p>"
        "<p>· Multi-location growth (1→3+)</p>"
        "<p>· Recent PE / HCIT investment</p>"
        "<p>· HIPAA breach disclosure</p>"
        "<p>· New behavioral-health facility opening</p>"
        "<p>· New CEO / COO appointed (last 90 days)</p>"
    ),
    "3458764670491912598": (   # col 2 — Veterinary
        "<p><strong>Veterinary triggers</strong></p>"
        "<p>· Opening 2nd or 3rd location</p>"
        "<p>· Recently hired hospital administrator</p>"
        "<p>· PIMS migration job posting (Cornerstone, AVImark, ezyVet)</p>"
        "<p>· AVMA specialty accreditation added</p>"
        "<p>· Recent PE / buyout activity in metro area</p>"
        "<p>· Multi-disciplinary referral partnership announcements</p>"
    ),
    "3458764670491912525": (   # col 3 — Multi-Loc Consumer
        "<p><strong>Multi-Loc Consumer triggers</strong></p>"
        "<p>· Opening new location (3+)</p>"
        "<p>· Hiring multi-unit GM</p>"
        "<p>· Franchise expansion / franchise sale</p>"
        "<p>· Multi-state licensing</p>"
        "<p>· Recent SBA loan or capital event</p>"
        "<p>· POS migration (Square → Toast / Lightspeed)</p>"
        "<p>· Owner-op + 3+ locations = bottleneck</p>"
    ),
    "3458764670491912526": (   # col 4 — HR Staffing
        "<p><strong>Staffing triggers</strong></p>"
        "<p>· New ATS purchase (Bullhorn, JobAdder, Loxo, Crelate)</p>"
        "<p>· New VP Sales / RevOps Director hire</p>"
        "<p>· Branch expansion / new state entry</p>"
        "<p>· MSP / VMS contract win</p>"
        "<p>· Capacity scaling job posts (\"hiring 5 recruiters\")</p>"
        "<p>· HubSpot or Salesforce purchase &lt;6 mo old</p>"
    ),
    "3458764670491912527": (   # col 5 — FinServ
        "<p><strong>FinServ triggers</strong></p>"
        "<p>· Series A or B raise (last 12 months)</p>"
        "<p>· AI / ML engineer job postings (no senior tech in seat)</p>"
        "<p>· No CTO in seat OR recent CTO departure</p>"
        "<p>· RegTech vendor evaluations</p>"
        "<p>· ISO partnership announcements</p>"
        "<p>· New compliance officer hire</p>"
        "<p>· Board mandate for AI roadmap</p>"
    ),
}


def patch(item_id: str, html: str):
    body = json.dumps({"data": {"content": html}})
    r = subprocess.run([
        "curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
        "-X", "PATCH",
        "-H", f"Authorization: Bearer {MIRO_TOKEN}",
        "-H", "Content-Type: application/json",
        "-H", "Accept: application/json",
        "--data", body,
        f"{BASE}/{item_id}",
    ], capture_output=True, text=True, timeout=30)
    return r.stdout.strip()


if __name__ == "__main__":
    print(f"Patching {len(UPDATES)} stickies (col4→Staffing, focus%, "
          f"Case Studies×5, Triggers×5)...\n")
    n_ok = n_err = 0
    for sid, html in UPDATES.items():
        code = patch(sid, html)
        ok = code == "200"
        marker = "OK " if ok else "ERR"
        print(f"  {marker} {sid}  status={code}")
        if ok: n_ok += 1
        else: n_err += 1
        time.sleep(0.12)
    print(f"\nFinal: {n_ok} OK, {n_err} failed (out of {len(UPDATES)})")

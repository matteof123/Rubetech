#!/usr/bin/env python3
"""
Replace the Mendel-content sticky notes in the Rubetech | Analysis board's
process flow view with Rubetech-specific content.

Board: https://miro.com/app/board/uXjVHbhe9MU=/
Board ID (URL-encoded for API): uXjVHbhe9MU%3D

Process flow region: x in [85000..115000], y in [-16000..23000]
"""
import os, json, subprocess, sys, time

MIRO_TOKEN = os.environ["MIRO_TOKEN"]
BOARD_ID = "uXjVHbhe9MU%3D"
BASE = f"https://api.miro.com/v2/boards/{BOARD_ID}/sticky_notes"

# id -> new content (HTML, as Miro stores content as HTML)
UPDATES = {
    # ── Top row: Filtering / Monitoring (replace Mendel terms with Rubetech) ──
    "3458764670490064240": (
        "<p><strong>Blocklist</strong></p>"
        "<p>1. Existing RubeTech customers (HubSpot match)</p>"
        "<p>2. Past prospect do-not-contact list</p>"
        "<p>3. Recently contacted (60-day cooldown)</p>"
        "<p>4. Competitor agencies / fractional CTO firms</p>"
    ),
    "3458764670490064245": (
        "<p><strong>Monitor Changes:</strong></p>"
        "<p>1. Past champions (RubeTech alumni at new company)</p>"
        "<p>2. CTO / VP Ops / RevOps / Sales Ops job posts</p>"
        "<p>3. New CEO / COO / CFO appointments (last 90 days)</p>"
        "<p>4. Series A / B / capital raises (last 12 months)</p>"
        "<p>5. Multi-location expansion announcements</p>"
    ),
    "3458764670490064277": (
        "<p><strong>Qualification:</strong></p>"
        "<p>1. &lt;$10M revenue (Fractional CTO) / &lt;$1M (RevOps)</p>"
        "<p>2. Outside Northeast US for in-person FCTO</p>"
        "<p>3. Tech-native founder with full eng team</p>"
        "<p>4. Single-location with no scaling plan</p>"
    ),

    # Database Qualification label — keep
    # "3458764670490064189": "Database Qualification",  # no change

    "3458764670490064237": (
        "<p><strong>1° Verticals</strong></p>"
        "<p>Specialty Healthcare (home care, behavioral, digital health)"
        " + Specialty Veterinary (specialty centers, vet ER)"
        " + Multi-Location Consumer Services (premium pet, concierge, fitness)"
        " + HR Staffing &amp; Recruiting (specialty)"
        " + FinServ — Payments / ISOs / Specialty Finance</p>"
    ),

    # ── Qualifier check sticky — keep "If active on LinkedIn" generic ──
    # "3458764670490064231": no change (still applies)

    "3458764670490064218": (
        "<p><strong>Active CEO / COO / Founder?</strong></p>"
        "<p>(Fractional CTO buyer — operator with budget authority)</p>"
    ),

    # When-meet-requirements / when-don't sticky labels — keep
    # "3458764670490064222": "When they meet requirements (LinkedIn-first)"
    # "3458764670490064219": "When they don't meet requirements (email-first)"

    # Campaign labels — name them per offer
    "3458764670490064249": (
        "<p><strong>Campaign 1</strong></p>"
        "<p>Healthcare + Veterinary (Fractional CTO)</p>"
    ),
    "3458764670490064250": (
        "<p><strong>Campaign 2</strong></p>"
        "<p>Multi-Location Consumer + FinServ (FCTO + RevOps)</p>"
    ),

    # Direct/Indirect Approach labels — keep (action sticky labels)
    # "3458764670490064247": "Direct Approach (Blank)"  -- keep
    # "3458764670490064248": "Indirect Approach (Question)" -- keep
    # "3458764670490064251": "Direct Approach (Main UVP)" -- keep
    # "3458764670490064252": "Indirect Approach (Nudge)" -- keep
    # "3458764670490064253": "Direct Approach (Lead Magnet)" -- keep
    # "3458764670490064254": "Indirect Approach (Additional Info)" -- keep
    # Connect Request label -- keep

    # Email 1 (cold email, top of funnel)
    "3458764670490064191": (
        "<p><strong>Email 1</strong></p>"
        "<p>Hook: trigger signal (multi-location growth / Series A / new CRM purchase / new C-suite hire).</p>"
        "<p>Offer: free 15-min Revenue Leak Audit.</p>"
        "<p>Proof: Alliance Homecare 88% revenue increase / Pups Pet Club multi-unit ops.</p>"
        "<p>CTA: 'pick a 15-min slot'.</p>"
    ),

    # Angle per signal
    "3458764670490064214": (
        "<p><strong>Angle per signal:</strong></p>"
        "<p>Multi-location growth → centralized reporting infra</p>"
        "<p>Series A/B raise → board-ready 12-mo tech roadmap</p>"
        "<p>HubSpot/Salesforce purchase → make CRM actually work</p>"
        "<p>New COO/CFO → 30-day operations audit</p>"
        "<p>Hiring CTO → fractional alternative ($6.5K vs $400K)</p>"
    ),

    # View Profile / Like Post — keep labels
    # "3458764670490064241": "View Profile" -- keep
    # "3458764670490064242": "View Profile" -- keep
    # "3458764670490064243": "Like Post"    -- keep
    # "3458764670490064244": "Like Post"    -- keep
    # "3458764670490064217": "Recontact after 60 days · re-check signals before re-source" -- keep

    # Email 2 (follow-up, new thread)
    "3458764670490064192": (
        "<p><strong>Email 2</strong></p>"
        "<p>New thread. Reference proof: Alliance Homecare (88% revenue lift), "
        "CorCon USA, Pups Pet Club, Trusthouse.</p>"
        "<p>Concrete metric: 30–90 day payback, 20–50 hrs/week saved per team.</p>"
        "<p>Offer: Fractional CTO Advisory ($6.5K/mo, 12-mo) or RevOps Build ($12.5K fixed).</p>"
    ),

    # Lead Magnet
    "3458764670490064215": (
        "<p><strong>Lead Magnet:</strong></p>"
        "<p>Free 15-Minute Revenue Leak Audit.</p>"
        "<p>Live on Zoom — Dan reviews CRM/pipeline tool and delivers 3 specific findings: "
        "where they're losing money, where they're wasting time, what to fix first.</p>"
        "<p>No prep, no homework. Audit creates demand for the engagement by making pain visible.</p>"
    ),

    # LinkedIn Message 1 (connect + opener)
    "3458764670490064226": (
        "<p><strong>Message 1</strong></p>"
        "<p>Signal-triggered. Short, specific.</p>"
        "<p>Reference vertical proof point: Alliance Homecare / Pups Pet Club / "
        "CorCon USA / Trusthouse / Calendar Group.</p>"
        "<p>Personal angle (operator-to-operator, not consultant).</p>"
        "<p>Question only — no pitch in first message.</p>"
    ),

    # LinkedIn Message 2 (resource share)
    "3458764670490064228": (
        "<p><strong>Message 2</strong></p>"
        "<p>Case study or benchmark:</p>"
        "<p>· Healthcare AI Industry Report (already produced)</p>"
        "<p>· Fractional CTO ROI calculator</p>"
        "<p>· 'From spreadsheets to systems' one-pager (CorCon USA story)</p>"
        "<p>· 22-slide capabilities deck</p>"
    ),

    # Reply trigger / qualification labels — keep
    # "3458764670490064194": "Whenever a reply comes" -- keep
    # "3458764670490064195": "AI Qualification" -- keep
    # Hot Lead bucket — already correct
    # "3458764670490064201": "Hot Lead Super Interested ..." -- keep
    # "3458764670490064205": "Not Interested" -- keep
    # "3458764670490064209": "OOO" -- keep
    # "3458764670490064207": "Blocklist" -- keep
    # "3458764670490064211": "Recontact" -- keep

    # Immediate Notification (Slack alert wiring)
    "3458764670490064199": (
        "<p><strong>Immediate Notification</strong></p>"
        "<p>Slack alert to Dan Rubenstein + Joseph Rios + Matteo Fois + David.</p>"
        "<p>Demo handoff with full thread context, lead score, and trigger signal.</p>"
        "<p>SLA: same-day response from Joseph (qualify) → Dan (close).</p>"
    ),

    # HubSpot CRM ingestion
    "3458764670490064198": (
        "<p><strong>HubSpot</strong></p>"
        "<p>Create contact + deal in RubeTech HubSpot.</p>"
        "<p>Attach sequence note + full reply transcript.</p>"
        "<p>Owner: Joseph Rios (qualify, &lt;$10M) → Dan Rubenstein (close, $10M+).</p>"
        "<p>Stage: Lead → SQL → Discovery → Brief → Closed.</p>"
    ),

    # Automatic Reply / Partner replies labels — keep
    # "3458764670490064278": "Automatic Reply" -- keep
    # "3458764670490064233": "Partner replies" -- keep

    # Reporting (weekly)
    "3458764670490064235": (
        "<p><strong>Reporting</strong></p>"
        "<p>Weekly: sent / positive replies / meetings booked / SQLs.</p>"
        "<p>Vertical breakdown: Healthcare / Veterinary / Consumer Services / "
        "Staffing / FinServ.</p>"
        "<p>Cost log (enrich + copy + sending). Pipeline $ value &amp; CAC.</p>"
        "<p>Goal: 3–4 qualified opps / month → $1.5M ARR in 12 months.</p>"
    ),
}


def patch_sticky(item_id: str, html: str):
    body = json.dumps({"data": {"content": html}})
    result = subprocess.run([
        "curl", "-s", "-w", "\n%{http_code}",
        "-X", "PATCH",
        "-H", f"Authorization: Bearer {MIRO_TOKEN}",
        "-H", "Content-Type: application/json",
        "-H", "Accept: application/json",
        "--data", body,
        f"{BASE}/{item_id}",
    ], capture_output=True, text=True, timeout=30)
    out = result.stdout.rsplit("\n", 1)
    body_out = out[0] if len(out) > 1 else ""
    code = out[-1].strip() if out else "?"
    return code, body_out


if __name__ == "__main__":
    n_ok = n_fail = 0
    for sid, html in UPDATES.items():
        status, body = patch_sticky(sid, html)
        marker = "OK " if status == 200 else "ERR"
        print(f"  {marker} {sid}  status={status}")
        if status == 200:
            n_ok += 1
        else:
            n_fail += 1
            print(f"      body: {body[:200]}")
        time.sleep(0.15)  # gentle pacing for API
    print(f"\nUpdated: {n_ok} OK, {n_fail} failed (out of {len(UPDATES)})")

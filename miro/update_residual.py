#!/usr/bin/env python3
"""Final pass — replace remaining Mendel-content stickies in Analysis & Target,
Signals & Evergreen, Hyper-Targeted DB."""
import os, json, subprocess, time

MIRO_TOKEN = os.environ["MIRO_TOKEN"]
BOARD_ID = "uXjVHbhe9MU%3D"
BASE = f"https://api.miro.com/v2/boards/{BOARD_ID}/sticky_notes"

# Board has 4 vertical columns (x=2128, 3206, 4753, 5984).
# Map to RubeTech's 4 priority verticals (HR Staffing folded in as cross-sell):
#   col 1 (x=2128) → Specialty Healthcare
#   col 2 (x=3206) → Specialty Veterinary
#   col 3 (x=4753) → Multi-Location Consumer Services
#   col 4 (x=5984) → FinServ / Payments

UPDATES = {
    # ── Analysis & Target — main goal sticky ──
    "3458764670490064068": (
        "<p><strong>Main Goal</strong></p>"
        "<p>3–4 qualified sales meetings per month with target ICPs "
        "→ 10 new clients in 12 months → $1.5M ARR. "
        "Avg deal $100K · 25% close · 60–90 day cycle.</p>"
    ),

    # ── Vertical headers (y=5366) ──
    "3458764670490064149": (  # x=2128 — was "Retail & CPG"
        "<p><strong>Specialty Healthcare</strong></p>"
    ),
    "3458764670490064158": (  # x=3206 — was "Logistics & Transportation"
        "<p><strong>Specialty Veterinary</strong></p>"
    ),
    "3458764670490064144": (  # x=4753 — was "Manufacturing & Industrial"
        "<p><strong>Multi-Location Consumer Services</strong></p>"
    ),
    "3458764670490064140": (  # x=5984 — was "Pharma + Professional Services"
        "<p><strong>FinServ &amp; Payments</strong></p>"
    ),

    # ── Industries / sub-segment row (y=5974) ──
    "3458764670490064150": (  # col 1 — Healthcare subverticals
        "<p>Home Care · Behavioral Health (IOP/PHP) · "
        "Digital Health · Specialty Practices (orthopedic, "
        "cardiology, oncology billing)</p>"
    ),
    "3458764670490064159": (  # col 2 — Veterinary subverticals
        "<p>Specialty Surgical Centers · Veterinary ER Networks · "
        "Multi-Disciplinary Referral Hospitals · "
        "Veterinary Behavioral</p>"
    ),
    "3458764670490064145": (  # col 3 — Multi-Location Consumer subverticals
        "<p>Premium Pet Services (boarding, grooming networks) · "
        "Concierge / Calendar Services · Boutique Fitness · "
        "Med Spas · Premium Home Services</p>"
    ),
    # 5984 already updated to FinServ Payments + tiers — skip

    # ── Decision-Makers row (y=6642–6675) — replace Spanish CFO with RubeTech buyers ──
    "3458764670490064151": (  # col 1 — Healthcare DMs
        "<p><strong>Decision-Makers (Healthcare)</strong></p>"
        "<p>1. CEO / Founder · Home Care, Behavioral Health</p>"
        "<p>2. COO / VP Operations</p>"
        "<p>3. Practice Administrator</p>"
        "<p>4. CFO (post-funding)</p>"
        "<p>Champion: VP Clinical Ops · IT Director</p>"
    ),
    "3458764670490064160": (  # col 2 — Veterinary DMs
        "<p><strong>Decision-Makers (Veterinary)</strong></p>"
        "<p>1. CEO / Owner-Clinician (Specialty Hospital)</p>"
        "<p>2. Hospital Administrator</p>"
        "<p>3. Multi-Site COO</p>"
        "<p>Champion: Office Manager · Lead Vet Tech</p>"
    ),
    "3458764670490064146": (  # col 3 — Consumer Services DMs
        "<p><strong>Decision-Makers (Consumer Svc)</strong></p>"
        "<p>1. Founder / CEO · Multi-Unit Operator</p>"
        "<p>2. VP Operations / Chief of Staff</p>"
        "<p>3. Multi-Unit GM</p>"
        "<p>Champion: Operations Manager · Marketing Lead</p>"
    ),
    "3458764670490064142": (  # col 4 — FinServ DMs
        "<p><strong>Decision-Makers (FinServ)</strong></p>"
        "<p>1. Founder / CEO · Payment Processor / ISO</p>"
        "<p>2. CTO (often missing — that's the gap)</p>"
        "<p>3. Chief Compliance Officer / VP Ops</p>"
        "<p>Champion: Head of Engineering · VP Risk</p>"
    ),

    # ── Signals & Evergreen — fix 2 label stickies that still imply CFO finance ──
    "3458764670490064125": (  # was "Controller and Finance Job Posts"
        "<p><strong>Tech-Leadership Job Posts</strong></p>"
        "<p>(CTO · VP Ops · RevOps Director · Sales Ops · Chief of Staff · HubSpot Admin)</p>"
    ),
    "3458764670490064123": (  # was "New CFO Appointments (90-day window)"
        "<p><strong>New CEO / COO / CFO Appointments</strong></p>"
        "<p>(90-day window — first 60 days = audit window)</p>"
    ),

    # ── Hyper-Targeted DB — fill the empty sticky ──
    "3458764670490064258": (  # was empty
        "<p>Pull supplementary lists from vertical-specific directories: "
        "AAHA member directory (Veterinary), HFMA member directory "
        "(Healthcare), AAPC + state nursing boards (Healthcare), "
        "ETA + ISO directories (Payments), AAHA + ASA "
        "(Staffing). Cross-reference against Apollo + BlitzAPI core list.</p>"
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
    print(f"Patching {len(UPDATES)} residual stickies...\n")
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

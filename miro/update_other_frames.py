#!/usr/bin/env python3
"""Replace remaining Mendel-content stickies in Analysis & Target,
Atlas Infrastructure, Hyper-Targeted Database Creation, Signals & Evergreen
frames with RubeTech-specific content."""
import os, json, subprocess, time

MIRO_TOKEN = os.environ["MIRO_TOKEN"]
BOARD_ID = "uXjVHbhe9MU%3D"
BASE = f"https://api.miro.com/v2/boards/{BOARD_ID}/sticky_notes"


# ─────────────────────────────────────────────────────────────────────
# Analysis & Target frame
# ─────────────────────────────────────────────────────────────────────
ANALYSIS = {
    # Goal sticky
    "3458764670490064064": (
        "<p><strong>Goal</strong></p>"
        "<p>Drive RubeTech ARR from $300K to $1.5M in 12 months via "
        "3–4 qualified meetings/month across 5 priority verticals "
        "(Specialty Healthcare, Specialty Veterinary, Multi-Location "
        "Consumer Services, HR Staffing, FinServ/Payments). Avg deal "
        "$100K · 25% close rate · 10 new clients.</p>"
    ),
    "3458764670490064274": (
        "<p><strong>No Repeatable Outbound Engine</strong></p>"
        "<p>Past attempts (250 Seamless emails → 1 lost deal · 500 "
        "Claude AI emails → 3 replies · 50 LinkedIn → 2 replies) lacked "
        "infrastructure, deliverability, and signal-driven targeting.</p>"
    ),
    "3458764670490064067": (
        "<p><strong>Solution</strong></p>"
        "<p>Northeast-US-specific outbound data operation that qualifies "
        "$10M–$200M companies automatically and feeds fresh CEOs / COOs / "
        "CFOs into RubeTech outreach every week, segmented by vertical.</p>"
    ),

    # Vertical headers — 5 columns at x ≈ 2128, 3206, 4753, 5984
    # Existing column structure:
    #  col1 (x=2128): Logistics → Healthcare (primary vertical)
    #  col2 (x=3206): Retail    → Veterinary
    #  col3 (x=4753): Manuf.    → Multi-Location Consumer Services
    #  col4 (x=5984): Pharma    → FinServ / Payments

    # Vertical-detail row (the "anchor" stickies at y≈9300)
    "3458764670490064169": (  # x=2128 — Healthcare anchor (was OXXO/FEMSA)
        "<p><strong>Healthcare anchor</strong></p>"
        "<p>HIPAA-compliant data flows + intake-to-billing reconciliation + "
        "real-time census across branches. Existing client: Alliance "
        "Homecare (88% revenue increase in 7 months), Trusthouse.</p>"
    ),
    "3458764670490064168": (  # x=3206 — Veterinary anchor (was Viva Aerobus)
        "<p><strong>Specialty Veterinary anchor</strong></p>"
        "<p>Multi-hospital P&amp;L consolidation + automated referral "
        "intake + PIMS-to-CRM integration. Specialty surgical / ER / "
        "internal medicine — fragmented, large-volume, tech-naive.</p>"
    ),
    "3458764670490064171": (  # x=4753 — Multi-Location Consumer (was Manufacturing)
        "<p><strong>Multi-Location Consumer anchor</strong></p>"
        "<p>Single dashboard across 3+ locations + closed-loop attribution "
        "+ centralized CRM. Existing client: Pups Pet Club, Calendar "
        "Group. Owner-operator escapes the bottleneck.</p>"
    ),
    "3458764670490064172": (  # x=5984 — FinServ anchor (was Pharma)
        "<p><strong>FinServ / Payments anchor</strong></p>"
        "<p>Application-to-funding automation + AI underwriting copilot "
        "+ board-ready 12-mo tech roadmap. Post-Series-A founders, "
        "ISOs, specialty lenders, payment processors.</p>"
    ),

    # Vertical header row (y ≈ 5366) — replace where applicable
    "3458764670490064141": (
        "<p><strong>FinServ &amp; Payments</strong></p>"
        "<p>Payment Processors / ISOs · Specialty Lenders · "
        "Embedded Finance · Specialty Insurance Brokerages</p>"
    ),

    # Company size row (y ≈ 7300) — same content per vertical
    "3458764670490064161": (
        "<p><strong>Co. size</strong></p>"
        "<p>$10M–$100M revenue · 25–500 employees · multi-location "
        "OR post-funding · in or near Northeast US</p>"
    ),
    "3458764670490064152": (
        "<p><strong>Co. size</strong></p>"
        "<p>$10M–$100M revenue · 25–500 employees · multi-location "
        "OR post-funding · in or near Northeast US</p>"
    ),
    "3458764670490064147": (
        "<p><strong>Co. size</strong></p>"
        "<p>$5M–$50M revenue · 20–250 employees · 3+ locations · "
        "owner-operator OR new COO in seat</p>"
    ),
    "3458764670490064143": (
        "<p><strong>Co. size</strong></p>"
        "<p>$10M–$200M revenue · post-Series-A or PE-backed · "
        "25–500 employees · no CTO in seat</p>"
    ),

    # Geography row (y ≈ 8000) — Mexico → Northeast US
    "3458764670490064157": (
        "<p><strong>Geography</strong></p>"
        "<p>Northeast US (CT, NY, NJ, MA priority) · "
        "Healthcare branches across multi-state</p>"
    ),
    "3458764670490064162": (
        "<p><strong>Geography</strong></p>"
        "<p>Northeast US (CT, NY, NJ, MA, PA) · "
        "near-Northeast (DC, MD) for specialty vet</p>"
    ),
    "3458764670490064156": (
        "<p><strong>Geography</strong></p>"
        "<p>Northeast US + Chicago/Midwest (Dan's network) · "
        "national for RevOps Build</p>"
    ),
    "3458764670490064155": (
        "<p><strong>Geography</strong></p>"
        "<p>National (FinServ runs remote-first) · "
        "preference for NYC / Boston / Stamford metro</p>"
    ),
}


# ─────────────────────────────────────────────────────────────────────
# Atlas Infrastructure frame
# ─────────────────────────────────────────────────────────────────────
ATLAS = {
    "3458764670490064079": (
        "<p><strong>Email + LinkedIn Infrastructure</strong></p>"
        "<p>Set up RubeTech email + LinkedIn infrastructure on Kinetyca-"
        "managed EmailBison workspace (isolated, multi-domain rotation, "
        "warmup). 15–20 sending domains. HeyReach for LinkedIn. Goal: "
        "&lt;3% bounce, &gt;55% deliverability.</p>"
    ),
    "3458764670490064098": (
        "<p><strong>Domain Setup</strong></p>"
        "<p>· DNS, SPF, DKIM, DMARC, MX records on RubeTech-branded "
        "domains (e.g. getrubetech.com, gorubetech.com, rubetechgroup.com)<br/>"
        "· Domain rotation across 15–20 sending domains<br/>"
        "· Forwarding to rubetechpartners.com</p>"
    ),
    "3458764670490064101": (
        "<p><strong>EmailBison + Sending Set-Up</strong></p>"
        "<p>· Workspace isolation per RubeTech<br/>"
        "· Forwarding setup<br/>"
        "· Domain rotation across 15–20 domains<br/>"
        "· Inbox warm-up (~30-day ramp)<br/>"
        "· Send caps: 30/inbox/day after warmup</p>"
    ),
}


# ─────────────────────────────────────────────────────────────────────
# Hyper-Targeted Database Creation frame
# ─────────────────────────────────────────────────────────────────────
DATABASE = {
    "3458764670490064081": (
        "<p><strong>Sourcing</strong></p>"
        "<p>Source Northeast US CEOs / COOs / CFOs / Founders at "
        "$10M–$200M companies across 5 verticals (Healthcare, "
        "Veterinary, Multi-Location Consumer, Staffing, FinServ) "
        "using Apollo + Sales Nav + BlitzAPI + LinkedIn signals.</p>"
    ),
    "3458764670490064094": (
        "<p><strong>RubeTech Lead Database (Supabase)</strong></p>"
        "<p>Central deduplication. Tagged by vertical, persona, "
        "trigger, and signal score. HubSpot mirror for Joseph + Dan.</p>"
    ),
    "3458764670490064093": (
        "<p><strong>Lookalikes</strong></p>"
        "<p>Retrieve lookalikes starting from RubeTech's current "
        "customers (Alliance Homecare, Trusthouse, Pups Pet Club, "
        "CorCon USA, Calendar Group) — same vertical, similar size, "
        "similar tech stack, similar growth signal.</p>"
    ),
}


# ─────────────────────────────────────────────────────────────────────
# Signals & Evergreen frame
# ─────────────────────────────────────────────────────────────────────
SIGNALS = {
    "3458764670490064124": (
        "<p><strong>Past Champions</strong></p>"
        "<p>(RubeTech alumni at new company)</p>"
    ),
    "3458764670490064128": (
        "<p>Track contacts from RubeTech's existing customer base "
        "(Alliance Homecare, Trusthouse, Pups Pet Club, CorCon USA, "
        "Calendar Group) who move to a new mid-market company — "
        "warm intro path with built-in trust and 30–90 day deal cycles.</p>"
    ),
    "3458764670490064129": (
        "<p>Companies hiring CTO, VP Ops, VP Engineering, RevOps "
        "Director, Sales Ops Manager, Chief of Staff, or HubSpot "
        "Admin signal a tech-leadership gap that Fractional CTO or "
        "RevOps Build can fill cheaper and faster than the role "
        "they're posting.</p>"
    ),
    "3458764670490064127": (
        "<p>Newly appointed CEOs / COOs / CFOs in Northeast US "
        "mid-market with under-90-day tenure are actively evaluating "
        "their stack. Hit them in the first 60 days with the Revenue "
        "Leak Audit before vendors line up.</p>"
    ),
    "3458764670490064130": (
        "<p>Re-engage HubSpot &quot;lost&quot; / &quot;no decision&quot; "
        "from 6–12 months ago. Lead with new productized offers "
        "(Advisory $6.5K/mo, RevOps Foundation $12.5K fixed-price). "
        "Lower-friction entry than the original deal that stalled.</p>"
    ),
    "3458764670490064134": (
        "<p>Retarget CEOs / COOs / CFOs from industry conferences in "
        "RubeTech verticals: HFMA, AHA, NAHC (Healthcare); AAHA, VHMA "
        "(Veterinary); ASA, NAPS (Staffing); ETA, Money 20/20 "
        "(Payments). Scrape attendee + speaker lists.</p>"
    ),
    "3458764670490064133": (
        "<p><strong>Industry Conferences</strong></p>"
        "<p>Healthcare · Veterinary · Multi-Location Services · "
        "Staffing · FinServ</p>"
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
    all_updates = {}
    all_updates.update({k: ("Analysis & Target", v) for k, v in ANALYSIS.items()})
    all_updates.update({k: ("Atlas Infrastructure", v) for k, v in ATLAS.items()})
    all_updates.update({k: ("Database Creation", v) for k, v in DATABASE.items()})
    all_updates.update({k: ("Signals & Evergreen", v) for k, v in SIGNALS.items()})

    print(f"Patching {len(all_updates)} stickies across 4 frames...\n")
    n_ok = n_err = 0
    for sid, (frame, html) in all_updates.items():
        code = patch(sid, html)
        ok = code == "200"
        marker = "OK " if ok else "ERR"
        print(f"  [{frame[:22]:<22}] {marker} {sid}  status={code}")
        if ok: n_ok += 1
        else: n_err += 1
        time.sleep(0.12)
    print(f"\nFinal: {n_ok} OK, {n_err} failed (out of {len(all_updates)})")

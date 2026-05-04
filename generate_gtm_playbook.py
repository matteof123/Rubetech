"""
RubeTech Partners — GTM Playbook Generator
Synthesized from Drive docs, Fireflies strategy calls, and web research (May 2026).
"""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
)
from reportlab.platypus.tableofcontents import TableOfContents
from datetime import date

PRIMARY = colors.HexColor("#0F4C81")
ACCENT  = colors.HexColor("#1F8FFF")
GREY_BG = colors.HexColor("#F2F4F7")
DARK    = colors.HexColor("#101828")
SUB     = colors.HexColor("#475467")

styles = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=styles["Heading1"], fontSize=18, leading=22,
                   textColor=PRIMARY, spaceAfter=10, spaceBefore=10)
H2 = ParagraphStyle("H2", parent=styles["Heading2"], fontSize=13, leading=16,
                   textColor=PRIMARY, spaceAfter=6, spaceBefore=12)
H3 = ParagraphStyle("H3", parent=styles["Heading3"], fontSize=11, leading=14,
                   textColor=DARK, spaceAfter=4, spaceBefore=8)
BODY = ParagraphStyle("Body", parent=styles["BodyText"], fontSize=9.5, leading=13,
                     textColor=DARK, alignment=TA_JUSTIFY, spaceAfter=4)
SMALL = ParagraphStyle("Small", parent=styles["BodyText"], fontSize=8.5, leading=11,
                      textColor=SUB)
COVER_TITLE = ParagraphStyle("CoverTitle", parent=styles["Title"], fontSize=30,
                             leading=34, textColor=PRIMARY, alignment=TA_CENTER,
                             spaceAfter=20)
COVER_SUB = ParagraphStyle("CoverSub", parent=styles["Title"], fontSize=18,
                           leading=22, textColor=DARK, alignment=TA_CENTER,
                           spaceAfter=12)
TABLE_CELL = ParagraphStyle("Cell", parent=styles["BodyText"], fontSize=8.8,
                            leading=11, textColor=DARK)
TABLE_HEAD = ParagraphStyle("CellH", parent=styles["BodyText"], fontSize=9,
                            leading=11, textColor=colors.white, fontName="Helvetica-Bold")


def P(text, style=BODY):
    return Paragraph(text, style)


def build_table(rows, col_widths, header=True):
    data = [[P(c, TABLE_HEAD) if header and i == 0 else P(c, TABLE_CELL)
             for c in row] for i, row in enumerate(rows)]
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), PRIMARY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOX", (0, 0), (-1, -1), 0.4, colors.HexColor("#D0D5DD")),
        ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#D0D5DD")),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, GREY_BG]),
    ]
    t = Table(data, colWidths=col_widths, repeatRows=1 if header else 0)
    t.setStyle(TableStyle(style))
    return t


def page_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(SUB)
    canvas.drawString(0.9 * inch, 0.5 * inch, "RubeTech Partners — Go-To-Market Playbook")
    canvas.drawRightString(LETTER[0] - 0.9 * inch, 0.5 * inch, f"Page {doc.page}")
    canvas.restoreState()


def cover_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(PRIMARY)
    canvas.rect(0, LETTER[1] - 2.5 * inch, LETTER[0], 2.5 * inch, fill=1, stroke=0)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 38)
    canvas.drawCentredString(LETTER[0] / 2, LETTER[1] - 1.5 * inch, "GO-TO-MARKET PLAYBOOK")
    canvas.setFont("Helvetica", 16)
    canvas.drawCentredString(LETTER[0] / 2, LETTER[1] - 2.0 * inch, "Strategic outbound blueprint")
    canvas.setFont("Helvetica-Bold", 48)
    canvas.setFillColor(PRIMARY)
    canvas.drawCentredString(LETTER[0] / 2, LETTER[1] - 4.5 * inch, "RubeTech Partners")
    canvas.setFont("Helvetica", 14)
    canvas.setFillColor(SUB)
    canvas.drawCentredString(LETTER[0] / 2, LETTER[1] - 5.0 * inch,
                             "Fractional CTO + RevOps Build")
    canvas.drawCentredString(LETTER[0] / 2, LETTER[1] - 5.3 * inch,
                             "Northeast US mid-market")
    canvas.setFont("Helvetica", 11)
    canvas.drawCentredString(LETTER[0] / 2, 1.5 * inch,
                             f"Prepared by Kinetyca  |  {date.today().strftime('%B %Y')}")
    canvas.setFont("Helvetica-Oblique", 9)
    canvas.drawCentredString(LETTER[0] / 2, 1.0 * inch,
                             "CONFIDENTIAL — Internal Use Only")
    canvas.restoreState()


def build():
    out = "/tmp/rubetech-gtm/Rubetech_GTM_Playbook.pdf"
    doc = SimpleDocTemplate(out, pagesize=LETTER,
                            leftMargin=0.9 * inch, rightMargin=0.9 * inch,
                            topMargin=0.8 * inch, bottomMargin=0.8 * inch,
                            title="RubeTech GTM Playbook")
    story = []

    # ─────────── COVER ───────────
    story.append(PageBreak())

    # ─────────── TABLE OF CONTENTS ───────────
    story.append(P("Table of Contents", H1))
    toc_rows = [
        ["Section", "Page"],
        ["1. Client Overview", "3"],
        ["2. UVP & Positioning", "4"],
        ["3. Social Proof & Case Studies", "5"],
        ["4. Top 5 Target Verticals", "6"],
        ["5. Ideal Customer Profiles & Personas", "9"],
        ["6. Pain-to-Value Mapping", "13"],
        ["7. Signals, Triggers & Timing", "16"],
        ["8. Cold Email Messaging Angles", "17"],
        ["9. AI-Identified Opportunities", "19"],
        ["Appendix — Data Sources", "20"],
    ]
    story.append(build_table(toc_rows, [4.7 * inch, 1.0 * inch]))
    story.append(PageBreak())

    # ─────────── 1. CLIENT OVERVIEW ───────────
    story.append(P("1. Client Overview", H1))
    story.append(P(
        "<b>RubeTech Partners</b> is a boutique strategic technology firm headquartered "
        "in the US Northeast (Connecticut) with Chicago/Midwest representation. They sit "
        "between fractional advisory and HubSpot implementation agencies, but unlike either, "
        "<b>they advise AND build</b> — taking a client from strategic roadmap to working "
        "revenue infrastructure end-to-end. Launched August 2025 by Dan Rubenstein "
        "(27y operator, 4x founder, 8-figure PE exit) and Joseph Rios (Partner — "
        "marketing/outbound).", BODY))
    story.append(P(
        "<b>What they sell — in one sentence:</b> Fractional CTO leadership and HubSpot "
        "RevOps systems for $10M–$200M Northeast mid-market companies that have outgrown "
        "spreadsheets but can't justify a $400K full-time CTO.", BODY))

    story.append(P("Productized Offers", H3))
    offer_rows = [
        ["Offer", "Tier", "Price", "Term", "Best Fit"],
        ["Fractional CTO (CORE)", "Advisory", "$6.5K/mo", "12-mo min", "$10–25M, light tech leadership"],
        ["Fractional CTO (CORE)", "Embedded", "$12.5K/mo", "9-mo min", "$25–100M, active transformation"],
        ["Fractional CTO (CORE)", "Transformation", "$22.5K/mo", "6-mo min", "$50–200M, post-funding rebuild"],
        ["HubSpot RevOps Build", "Foundation", "$12.5K one-time", "2–4 weeks", "$1–10M, first real CRM"],
        ["HubSpot RevOps Build", "Growth", "$22.5K one-time", "8–12 weeks", "$10–50M, broken HubSpot"],
    ]
    story.append(build_table(offer_rows,
        [1.45 * inch, 1.0 * inch, 1.0 * inch, 0.85 * inch, 2.0 * inch]))
    story.append(Spacer(1, 0.1 * inch))
    story.append(P("Company Stage & Metrics", H3))
    stage_rows = [
        ["Metric", "Current State"],
        ["Revenue (last year)", "$50–75K (launched Aug 2025)"],
        ["Revenue pace (current)", "~$300K"],
        ["Revenue target (12 mo)", "$1.5M ARR — 10 new clients"],
        ["Avg deal value", "$100K/year (range $15K–$300K+)"],
        ["Sales cycle", "30 days (soft offer) / 60–90 days (ICP)"],
        ["LTV", "~$150K"],
        ["Conversion rate", "25% (3 of 12 first meetings closed)"],
        ["Outbound goal", "3–4 qualified opps / month"],
    ]
    story.append(build_table(stage_rows, [2.0 * inch, 4.3 * inch]))
    story.append(Spacer(1, 0.1 * inch))
    story.append(P("Core Capabilities", H3))
    cap_rows = [
        ["Capability", "What They Build"],
        ["Revenue Operations", "HubSpot CRM architecture, pipeline reporting, attribution"],
        ["Workflow Automation", "Intake, follow-ups, notifications, cross-system handoffs (n8n, Zapier)"],
        ["AI Agents", "Customer service, sales optimization, forecasting, marketing personalization"],
        ["Vendor Strategy", "CRM/ERP/marketing stack evaluation, replacement, consolidation"],
        ["Tech Roadmaps", "12–24 month strategic roadmaps tied to revenue KPIs"],
        ["Integration Engineering", "Salesforce, HubSpot, NetSuite, OpenAI, payment platforms"],
    ]
    story.append(build_table(cap_rows, [1.7 * inch, 4.6 * inch]))
    story.append(PageBreak())

    # ─────────── 2. UVP & POSITIONING ───────────
    story.append(P("2. Unique Value Proposition & Positioning", H1))
    story.append(P("Positioning Statement", H3))
    story.append(P(
        "<i>For $10M–$200M Northeast mid-market CEOs and COOs who are running on "
        "spreadsheets, gut instinct, or unimplemented software — RubeTech is the "
        "only firm that combines 27 years of operator-level leadership with the "
        "engineering team to actually build the system. Unlike consulting firms "
        "that deliver decks or HubSpot agencies that configure software, RubeTech "
        "advises AND builds — fixed scope, fixed price, measurable ROI, in 30–90 "
        "days.</i>", BODY))

    story.append(P("UVP (in client's own words)", H3))
    story.append(P(
        "<i>\"Our managing partner has built, scaled, and exited companies at "
        "8-figure valuations — he's sat in the same seat as our clients. That "
        "operator experience combined with deep technical knowledge means we don't "
        "just tell you what to do, we go and do it. End-to-end — from strategic "
        "roadmap to working system — so you get business outcomes, not a slide deck.\"</i>",
        BODY))

    story.append(P("3 Differentiators (with evidence)", H3))
    diff_rows = [
        ["#", "Differentiator", "Why it's defensible"],
        ["1", "Advise AND build (operator + engineering team)",
         "Most consultants deliver PDFs and disappear. Most agencies configure "
         "software without business strategy. RubeTech does both — Dan provides "
         "C-suite roadmap, team builds the working system. Result: client gets "
         "a revenue engine, not a deck."],
        ["2", "Fixed scope, fixed price, measurable ROI math",
         "RubeTech doesn't sell hours. Every engagement = defined scope, fixed "
         "price, ROI projection with conservative payback (30–90 days). No scope "
         "creep, no surprise invoices. Soft offer starts at $6.5K/mo — less than "
         "1 month of a junior hire."],
        ["3", "27y C-suite operator with 4 exits ($8-figure PE exit)",
         "Dan Rubenstein has run the businesses he now advises. CEOs trust him "
         "because he's been in their seat — not a consultant lifer who never "
         "carried a number."],
    ]
    story.append(build_table(diff_rows, [0.3 * inch, 1.8 * inch, 4.2 * inch]))
    story.append(Spacer(1, 0.1 * inch))

    story.append(P("Status Quo Alternatives (and why they fail)", H3))
    sq_rows = [
        ["Status Quo", "Negative Impact"],
        ["(a) Do nothing — spreadsheets + gut instinct",
         "Revenue leaks, missed deals, no forecasting ability"],
        ["(b) Buy software (HubSpot, Salesforce) without implementation",
         "$12–50K/year in licensing wasted on software nobody uses"],
        ["(c) Hire $350–450K full-time CTO or generic IT lead",
         "Overpaying for narrow expertise; can't drive strategy across full stack"],
    ]
    story.append(build_table(sq_rows, [2.5 * inch, 3.8 * inch]))
    story.append(Spacer(1, 0.1 * inch))

    story.append(P("Competitor Landscape", H3))
    comp_rows = [
        ["Competitor Type", "Examples", "RubeTech Advantage"],
        ["HubSpot Solutions Partners", "New Breed, SmartBug, Aptitude 8",
         "They configure software. Don't architect RevOps or provide tech leadership."],
        ["Fractional CTO firms", "CTO on Demand, Toptal Fractional",
         "They advise and leave. RubeTech advises AND implements."],
        ["Big consulting", "Accenture, Deloitte (Dan came from Accenture)",
         "$300–500/hr for slide decks. RubeTech: working systems at fixed prices."],
    ]
    story.append(build_table(comp_rows, [1.6 * inch, 1.7 * inch, 3.0 * inch]))

    story.append(Spacer(1, 0.1 * inch))
    story.append(P("Lead Magnets", H3))
    story.append(P(
        "<b>Primary — Free 15-Minute Revenue Leak Audit:</b> Live Zoom call where "
        "Dan reviews CRM/pipeline tool and delivers 3 specific findings — where "
        "they're losing money, where they're wasting time, what to fix first. "
        "No prep required. Cheap to deliver (Dan can spot patterns in minutes), "
        "high perceived value.", BODY))
    story.append(P(
        "<b>Alternative being tested — Discovery → Business Brief with ROI:</b> "
        "Higher-friction but higher-value: 60-min discovery + written brief with "
        "ROI roadmap. Use for enterprise prospects who won't engage with a 15-min "
        "audit.", BODY))
    story.append(P(
        "<b>Available content assets:</b> 22-slide capabilities deck, 3 published "
        "case studies, RevOps and Fractional CTO landing pages, healthcare AI "
        "industry report, attempted VSL.", BODY))
    story.append(PageBreak())

    # ─────────── 3. SOCIAL PROOF & CASE STUDIES ───────────
    story.append(P("3. Social Proof & Case Studies", H1))
    story.append(P(
        "RubeTech is early-stage (launched Aug 2025) — case studies are growing. "
        "What follows is what's currently usable in cold outreach. "
        "<b>Recommendation:</b> develop 2 vertical-specific case studies "
        "(healthcare + specialty veterinary) before scaling outbound.", BODY))

    story.append(P("Quantified Outcomes (current)", H3))
    proof_rows = [
        ["Outcome", "Source", "Use In"],
        ["88% revenue increase in 7 months",
         "Active client (referenced in UVP doc)",
         "Healthcare CEO emails — \"revenue visibility\" angle"],
        ["$1.3M projected revenue lift",
         "Active client (referenced in UVP doc)",
         "Mid-market CFO/CRO emails — ROI math"],
        ["20–50+ hours/week of manual work eliminated per team",
         "Aggregate across engagements",
         "COO emails — operational leverage angle"],
        ["Conservative payback period: 30–90 days",
         "Standard ROI math on every proposal",
         "Budget objection handling in all sequences"],
    ]
    story.append(build_table(proof_rows, [2.2 * inch, 1.7 * inch, 2.4 * inch]))
    story.append(Spacer(1, 0.1 * inch))

    story.append(P("Named Clients (from website + onboarding)", H3))
    client_rows = [
        ["Client", "Industry", "Notes"],
        ["CorCon USA", "Construction (specialty)",
         "Earliest pilot client (referenced in partnership call)"],
        ["Calendar Group", "Consumer services / staffing",
         "Existing engagement"],
        ["Pups Pet Club", "Pet services (boarding)",
         "Validates Pet Services vertical"],
        ["Alliance Homecare", "Healthcare (home care)",
         "Validates Healthcare → Home Care subvertical"],
        ["Trusthouse", "Healthcare / behavioral health",
         "Validates Healthcare → Behavioral Health subvertical"],
    ]
    story.append(build_table(client_rows, [1.6 * inch, 1.8 * inch, 2.9 * inch]))

    story.append(Spacer(1, 0.1 * inch))
    story.append(P("Asset Gaps (recommended to develop)", H3))
    story.append(P(
        "• <b>Vertical case studies:</b> 1-pager per top vertical with Challenge → "
        "Solution → Results metrics (currently 3 generic case studies, none vertical-tagged)<br/>"
        "• <b>Customer quotes:</b> attributed quotes from Alliance Homecare, "
        "Trusthouse, CorCon USA — request from Dan after engagement closes<br/>"
        "• <b>Logo wall:</b> currently scattered across pages — consolidate on landing pages<br/>"
        "• <b>Industry report (healthcare):</b> already produced — repurpose as lead magnet asset<br/>",
        BODY))
    story.append(PageBreak())

    # ─────────── 4. TARGET VERTICALS ───────────
    story.append(P("4. Top 5 Target Verticals", H1))
    story.append(P(
        "Verticals refined during Onboarding Call (Apr 27) and Analysis Call 2 "
        "(May 1). Fractional CTO targets <b>$10M–$200M</b>. RevOps Build targets "
        "<b>$1M–$50M</b>. Vertical confidence reflects what Dan/Joey explicitly "
        "validated vs. what was on the original ICP list but de-prioritized in calls.", BODY))

    vert_summary = [
        ["#", "Vertical", "Offer", "Size Sweet Spot", "Confidence"],
        ["1", "Specialty Healthcare (home care, behavioral health, digital health)",
         "Fractional CTO", "$10–100M", "★★★★★ Client-confirmed"],
        ["2", "Specialty Veterinary (vet specialty centers, surgical, ER)",
         "Fractional CTO", "$10–80M", "★★★★★ Client-confirmed"],
        ["3", "Consumer Services (multi-location services, premium pet)",
         "Fractional CTO + RevOps", "$5–50M", "★★★★ Client-confirmed"],
        ["4", "HR Staffing & Recruiting (specialty, healthcare/exec)",
         "RevOps Build", "$2–25M", "★★★ AI-identified, partial confirm"],
        ["5", "Financial Services — Payment Solutions",
         "Fractional CTO + RevOps", "$5–100M", "★★★ Client-confirmed (specialty)"],
    ]
    story.append(build_table(vert_summary,
        [0.3 * inch, 2.4 * inch, 1.3 * inch, 1.0 * inch, 1.3 * inch]))
    story.append(Spacer(1, 0.15 * inch))

    # Vertical 1
    story.append(P("Vertical 1 — Specialty Healthcare", H2))
    story.append(P(
        "<b>Why this vertical:</b> Existing clients (Alliance Homecare, Trusthouse). "
        "Highest-validated. Dan: \"healthcare market faces HIPAA compliance, high "
        "capital and labor intensity. Opportunities arise from AI-driven "
        "consolidation and automation.\" Healthcare operators tend to be more "
        "educated and open to tech investment.", BODY))
    story.append(P(
        "<b>Subverticals:</b> Home Care (skilled + non-skilled), Behavioral "
        "Health (outpatient, IOP/PHP), Digital Health, Specialty practices "
        "(orthopedic, cardiology, oncology billing)", BODY))
    story.append(P(
        "<b>Pain points specific to vertical:</b> HIPAA-compliant data flows, "
        "intake-to-billing leakage, manual referral coordination, no real-time "
        "census/utilization, multi-location reporting in spreadsheets, paying "
        "for HubSpot/Salesforce that nobody uses", BODY))
    story.append(P(
        "<b>Value angle:</b> \"Stop billing leakage and prove ROI on every "
        "tech dollar — without hiring a $400K healthcare CTO.\"", BODY))
    story.append(P(
        "<b>Signals:</b> hiring CTO/VP IT/RevOps; recent EMR or PMS purchase "
        "without integration; multi-location growth (1→3+ locations); recent "
        "PE/HCIT investment; HIPAA breach disclosure; new behavioral-health "
        "facility opening", BODY))

    # Vertical 2
    story.append(P("Vertical 2 — Specialty Veterinary", H2))
    story.append(P(
        "<b>Why this vertical:</b> Dan: \"Veterinary specialty centers are large "
        "and under-optimized compared to consolidated general practice market "
        "dominated by private equity.\" PE has consolidated general vet practice; "
        "specialty (surgical, ER, internal medicine) is fragmented, large-volume, "
        "and tech-naive — a green field for Fractional CTO.", BODY))
    story.append(P(
        "<b>Subverticals:</b> Specialty surgical centers, Veterinary ER networks, "
        "Multi-disciplinary referral hospitals, Veterinary behavioral", BODY))
    story.append(P(
        "<b>Pain points:</b> Manual scheduling between primary and specialty "
        "referrals, no client portal, paper records or unintegrated PIMS, no "
        "marketing attribution, multi-location P&L impossible to consolidate", BODY))
    story.append(P(
        "<b>Value angle:</b> \"Consolidate 3 hospital P&Ls, automate referral "
        "intake, eliminate the spreadsheet your office manager built — in 8 weeks.\"",
        BODY))
    story.append(P(
        "<b>Signals:</b> opening 2nd or 3rd location, recently hired hospital "
        "administrator, PIMS migration job posting, AVMA specialty accreditation "
        "added, recent PE/buyout activity", BODY))

    # Vertical 3
    story.append(P("Vertical 3 — Consumer Services & Premium Multi-Location", H2))
    story.append(P(
        "<b>Why this vertical:</b> Existing client (Pups Pet Club). Multi-location "
        "service businesses break every manual process when scaling 1→3+ locations. "
        "Tech-naive but cash-flow-positive, willing to invest.", BODY))
    story.append(P(
        "<b>Subverticals:</b> Premium pet services (boarding, grooming networks), "
        "Calendar/concierge services (Calendar Group), Boutique fitness, Med "
        "spas, Premium home services", BODY))
    story.append(P(
        "<b>Pain points:</b> Each location runs differently, no centralized "
        "booking/CRM, owner is bottleneck on every report, can't see which "
        "location is profitable, can't scale marketing because attribution is "
        "absent", BODY))
    story.append(P(
        "<b>Value angle:</b> \"Stop being the only person who knows what's "
        "happening across all 3 locations — get a single dashboard in 4 weeks.\"",
        BODY))
    story.append(P(
        "<b>Signals:</b> opening new location, hiring multi-unit GM, franchise "
        "expansion, multi-state licensing, recent SBA loan or capital event",
        BODY))

    # Vertical 4
    story.append(P("Vertical 4 — Specialty HR Staffing & Recruiting", H2))
    story.append(P(
        "<b>Why this vertical:</b> Listed in original ICP, less prioritized in "
        "calls but RevOps fit is strong. Recruiting firms live and die by their "
        "ATS/CRM stitching — exactly RubeTech's wheelhouse.", BODY))
    story.append(P(
        "<b>Subverticals:</b> Healthcare staffing, Executive search, "
        "Specialty/technical recruiting, Light industrial staffing", BODY))
    story.append(P(
        "<b>Pain points:</b> ATS doesn't talk to CRM doesn't talk to billing, "
        "candidate-to-placement reporting in spreadsheets, no source-of-hire "
        "attribution, manual hours/billing for contract placements", BODY))
    story.append(P(
        "<b>Value angle:</b> \"Stop double-keying candidates between ATS and "
        "HubSpot — fix the integration in 4 weeks.\"", BODY))
    story.append(P(
        "<b>Signals:</b> recent ATS/CRM purchase, new VP Sales hire, branch "
        "expansion, MSP contract win, capacity scaling job postings", BODY))

    # Vertical 5
    story.append(P("Vertical 5 — Financial Services (Payment Solutions / Specialty Finance)", H2))
    story.append(P(
        "<b>Why this vertical:</b> Mentioned explicitly in ICP and one of "
        "Joey's strongest existing pipeline conversations. Payment processors, "
        "specialty lenders, and embedded-finance plays need RevOps + AI agents "
        "for underwriting and customer service automation.", BODY))
    story.append(P(
        "<b>Subverticals:</b> Payment processors / ISOs, Specialty lenders, "
        "Embedded finance platforms, Insurance brokerages (specialty)", BODY))
    story.append(P(
        "<b>Pain points:</b> Application-to-funding takes too long, manual "
        "underwriting, no customer service automation, compliance reporting "
        "in spreadsheets, no real-time portfolio visibility", BODY))
    story.append(P(
        "<b>Value angle:</b> \"Cut application-to-decision time in half with an "
        "AI underwriting copilot — without replacing your core platform.\"", BODY))
    story.append(P(
        "<b>Signals:</b> new compliance hire, ISO partnership announcements, "
        "Series A/B raise, RegTech vendor evaluations, hiring AI/ML engineers", BODY))
    story.append(PageBreak())

    # ─────────── 5. ICPs & PERSONAS ───────────
    story.append(P("5. Ideal Customer Profiles & Personas", H1))
    story.append(P(
        "12 personas across 5 verticals. Decision-maker for Fractional CTO is "
        "almost always the <b>CEO or COO</b>; champions for RevOps are often "
        "<b>VP Sales/CRO/Chief of Staff</b>. Geography: Northeast US (CT, NY, "
        "NJ, MA, PA) for Fractional CTO; national for RevOps Build.", BODY))

    p_rows = [
        ["#", "Vertical", "Persona", "Title (exact)", "Co. Size", "Offer Match", "Trigger"],
        ["1", "Healthcare", "Home Care CEO", "CEO / Founder, Home Care",
         "$10–50M", "Fractional CTO", "Multi-location growth"],
        ["2", "Healthcare", "Behavioral Health COO", "COO / Operations Director, Behavioral Health",
         "$15–80M", "Fractional CTO", "Recent EMR or PMS purchase"],
        ["3", "Healthcare", "Specialty Practice Admin", "Practice Administrator / VP Operations",
         "$5–25M", "RevOps Build", "Recent HubSpot purchase"],
        ["4", "Veterinary", "Specialty Hospital CEO", "CEO / Owner, Specialty Vet Hospital",
         "$5–40M", "Fractional CTO", "Opening 2nd–3rd location"],
        ["5", "Veterinary", "Hospital Administrator", "Hospital Administrator, Specialty Vet",
         "$5–30M", "RevOps Build", "Recent PIMS migration job"],
        ["6", "Consumer Svc", "Multi-Location Owner-Op", "Founder / CEO, Multi-Unit Services",
         "$3–25M", "Fractional CTO", "Opening 3+ locations"],
        ["7", "Consumer Svc", "VP Operations", "VP Operations / Chief of Staff",
         "$10–50M", "RevOps Build", "Recent CRM purchase"],
        ["8", "HR Staffing", "Recruiting Firm CEO", "CEO / Founder, Specialty Staffing",
         "$5–30M", "Fractional CTO", "ATS-CRM integration pain"],
        ["9", "HR Staffing", "Director of RevOps", "RevOps Director / VP Operations",
         "$3–25M", "RevOps Build", "New ATS purchase"],
        ["10", "FinServ", "ISO/Payments Founder", "Founder / CEO, Payment Processor or ISO",
         "$5–80M", "Fractional CTO", "Series A/B raise"],
        ["11", "FinServ", "Compliance/Ops Lead", "Chief Compliance Officer / VP Ops",
         "$10–100M", "RevOps + AI agents", "RegTech evaluation"],
        ["12", "Cross-vertical", "Post-Funding Founder", "CEO post Series A/B",
         "$10–100M", "Fractional CTO", "Capital raise <12 mo old"],
    ]
    story.append(build_table(p_rows,
        [0.25 * inch, 0.85 * inch, 1.15 * inch, 1.55 * inch, 0.65 * inch, 0.95 * inch, 1.0 * inch]))
    story.append(Spacer(1, 0.15 * inch))

    # Detailed personas
    story.append(P("Persona Deep-Dive — Home Care CEO (Vertical 1)", H3))
    story.append(P(
        "<b>Daily reality:</b> Owns P&L, manages 3+ branch managers, fields "
        "every escalation. Top metrics: census/utilization, hours billed vs. "
        "scheduled, caregiver retention, payor mix. Tools: usually some EMR + "
        "QuickBooks + spreadsheets. Often paying for HubSpot/Salesforce that "
        "nobody uses.<br/>"
        "<b>Frustrations:</b> can't see which branch is profitable in real "
        "time, billing leakage from missed visits, manual referral coordination "
        "with hospitals, can't forecast Medicaid/Medicare reimbursement.<br/>"
        "<b>Buying:</b> budget authority. Triggers: opening new branch, new "
        "payor contract. Objection: \"my EMR vendor said they'd do this.\"<br/>"
        "<b>✅ Target when:</b> 2+ branches, $10M+ rev, recent leadership "
        "hire (CFO/COO), or active EMR change<br/>"
        "<b>❌ Skip when:</b> single branch, &lt;$5M rev, owner-operator with "
        "no admin staff", BODY))

    story.append(P("Persona Deep-Dive — Specialty Vet Hospital CEO (Vertical 2)", H3))
    story.append(P(
        "<b>Daily reality:</b> Often a clinician-owner. Spends mornings in "
        "surgery, afternoons in admin. Inherits IT decisions made by office "
        "manager. Tools: PIMS (Cornerstone, AVImark, ezyVet) + QuickBooks + "
        "fragmented marketing.<br/>"
        "<b>Frustrations:</b> referral hospitals don't get clean handoffs, "
        "client communication is manual, no marketing attribution, multi-"
        "location P&L impossible without office manager working overtime.<br/>"
        "<b>Buying:</b> shared with hospital administrator if one exists. "
        "Triggers: opening 2nd location, hiring admin, PIMS migration.<br/>"
        "<b>✅ Target when:</b> 2+ locations OR $10M+ rev, recently hired "
        "hospital administrator, PIMS migration in last 6 months<br/>"
        "<b>❌ Skip when:</b> single-doctor practice, general practice (PE-"
        "consolidated)", BODY))

    story.append(P("Persona Deep-Dive — Multi-Location Owner-Op (Vertical 3)", H3))
    story.append(P(
        "<b>Daily reality:</b> Founder still in every meeting. Spends Mondays "
        "pulling location reports, Fridays approving payroll. Tools: location-"
        "specific POS + QuickBooks + Excel. CRM exists but nobody uses it.<br/>"
        "<b>Frustrations:</b> can't compare locations side-by-side, doesn't "
        "know which marketing channel actually drives revenue, every new "
        "location resets the process.<br/>"
        "<b>Buying:</b> founder = budget. Decision in 2–3 calls if ROI is "
        "concrete. Objection: \"my POS vendor has reporting.\"<br/>"
        "<b>✅ Target when:</b> 3+ locations, founder still operating, recent "
        "expansion / SBA loan / franchise sale<br/>"
        "<b>❌ Skip when:</b> single location, owner-only operation, "
        "franchise of large brand (corporate handles tech)", BODY))

    story.append(P("Persona Deep-Dive — ISO/Payments Founder (Vertical 5)", H3))
    story.append(P(
        "<b>Daily reality:</b> Heads sales + risk + tech, often half-tech "
        "founder. Recently raised, board pushing for AI strategy. Tools: "
        "core processor + Salesforce + Snowflake + ad hoc Python.<br/>"
        "<b>Frustrations:</b> board demanding AI roadmap, internal team can't "
        "agree on vendor stack, hiring a $400K CTO for 12 months they don't "
        "need feels wrong.<br/>"
        "<b>Buying:</b> CEO + CTO + board. Decision driven by board mandate. "
        "Objection: \"we'll build it in-house.\"<br/>"
        "<b>✅ Target when:</b> Series A/B closed in last 12 mo, no CTO "
        "or recent CTO departure, AI/ML hiring posts<br/>"
        "<b>❌ Skip when:</b> seed-stage, deeply tech-led founders, large "
        "incumbent processor", BODY))
    story.append(PageBreak())

    # ─────────── 6. PAIN-TO-VALUE MAPPING ───────────
    story.append(P("6. Pain-to-Value Mapping", H1))
    story.append(P(
        "Specific pains tied to specific value propositions and outcomes. "
        "Every pain references a concrete activity, tool, or metric. Every "
        "value prop references a measurable transformation.", BODY))

    pv1_rows = [
        ["#", "Pain (specific)", "Value Prop", "Outcome (current → desired)"],
        ["1", "CEO spends 8+ hrs/wk pulling pipeline data from HubSpot, "
              "QuickBooks, and spreadsheets to answer \"how are we doing?\"",
         "Single revenue dashboard in HubSpot, real-time, "
         "auto-attributed to source",
         "8 hrs → 0 hrs/week | 3-day reporting lag → real-time"],
        ["2", "Pays $25–50K/year for HubSpot or Salesforce that 80% of team "
              "ignores",
         "Implementation that re-architects HubSpot around how the business "
         "actually runs, with adoption coaching",
         "20% adoption → 90%+ adoption in 8 weeks"],
        ["3", "Just raised $X — board wants tech roadmap in 60 days, no CTO "
              "in seat, wrong vendor decisions could waste 12 months",
         "Senior tech leader (Dan) delivers board-ready 12-month roadmap "
         "in 4 weeks, plus implementation team to execute",
         "12-mo roadmap delay → roadmap + 30-day quick win"],
        ["4", "Office manager built a Frankenstein Excel that runs the "
              "business — she's about to retire / quit / go on leave",
         "Documented, automated workflows in HubSpot + n8n with no "
         "single point of failure",
         "Key-person risk → systematized + transferable"],
        ["5", "Opening 2nd / 3rd location next quarter, current processes "
              "won't scale, manual handoffs will break",
         "Multi-location-ready architecture (centralized CRM, location "
         "tagging, role-based reporting) before launch",
         "Manual chaos at 2 locations → predictable repeatable launch"],
        ["6", "Spending $100K+/year on ads with zero attribution to revenue, "
              "can't kill the channels that don't work",
         "Closed-loop attribution from ad click → opportunity → closed deal "
         "+ ROI dashboard per channel",
         "0% attribution → 100% deal sources tagged"],
        ["7", "Considering hiring full-time CTO ($350–450K) but volume "
              "doesn't justify it; current person doing 2 jobs",
         "Fractional CTO at $6.5–22.5K/mo — same caliber leadership at "
         "20–40% of the cost",
         "$400K hire → $80–270K/year, 30-day ramp"],
        ["8", "Compliance reporting (HIPAA / PCI / SOC2) is a quarterly "
              "fire drill that consumes leadership time",
         "Automated audit trails, role-based access, documented controls "
         "wired into the CRM and operational systems",
         "Quarterly fire drill → continuous compliance"],
    ]
    story.append(build_table(pv1_rows,
        [0.25 * inch, 1.95 * inch, 2.0 * inch, 2.0 * inch]))
    story.append(Spacer(1, 0.15 * inch))

    story.append(P("Pain → Value chains by persona", H3))
    story.append(P(
        "<b>Home Care CEO:</b> Pain #1, #2, #5, #8 → \"Stop billing leakage, "
        "see real-time census across branches, satisfy HIPAA without a "
        "fire drill.\"<br/>"
        "<b>Specialty Vet CEO:</b> Pain #4, #5, #6 → \"Get out of "
        "spreadsheets before you open the 3rd hospital. Know which "
        "referral source actually pays.\"<br/>"
        "<b>Multi-Location Owner-Op:</b> Pain #1, #5, #6 → \"Stop being "
        "the bottleneck. See all 3 locations in one dashboard.\"<br/>"
        "<b>ISO/Payments Founder:</b> Pain #3, #7 → \"Get a board-ready "
        "tech roadmap in 4 weeks at 1/4 the cost of a full-time CTO.\"<br/>"
        "<b>RevOps-fit (any vertical):</b> Pain #2, #6 → \"Make HubSpot "
        "actually work or replace what isn't working — fixed price.\"", BODY))
    story.append(PageBreak())

    # ─────────── 7. SIGNALS, TRIGGERS & TIMING ───────────
    story.append(P("7. Signals, Triggers & Timing", H1))
    story.append(P(
        "Triggers prioritized by RubeTech leadership during Onboarding Call "
        "(Apr 27). Listed top-down by buyer urgency.", BODY))

    trig_rows = [
        ["#", "Trigger", "Signal Source", "Why It Matters"],
        ["1", "Job posting: CTO / VP Ops / RevOps / Sales Ops",
         "LinkedIn Jobs, Indeed, company careers page",
         "Gap identified, not yet filled — fractional fills it cheaper"],
        ["2", "New CRM/marketing-automation purchase (HubSpot, Salesforce)",
         "G2/Capterra reviews, BuiltWith, intent data",
         "They bought it but it's not implemented — RevOps Build territory"],
        ["3", "Capital raise in last 12 months",
         "Crunchbase, PitchBook, press releases",
         "Board mandate for tech roadmap; budget unlocked"],
        ["4", "Opening 2nd or 3rd location",
         "Press releases, LinkedIn announcements, building permits, hiring",
         "Manual processes break; centralized systems become urgent"],
        ["5", "Leadership transition (new CEO/COO/CFO in last 6 mo)",
         "LinkedIn role changes, press releases",
         "New leader wants to modernize; mandate to fix what's broken"],
        ["6", "Increased ad spend with no attribution mention",
         "LinkedIn ads library, Meta ads library, SimilarWeb traffic",
         "Spending $100K+ on marketing, can't prove which channels work"],
        ["7", "Hiring an SDR / first sales hire",
         "LinkedIn Jobs",
         "Need pipeline infrastructure BEFORE the SDR starts, not after"],
        ["8", "Vertical-specific: PIMS migration (vet), EMR change (healthcare), "
              "ATS purchase (staffing)",
         "Vendor change announcements, hiring",
         "Re-architecture window — best time to build it right"],
        ["9", "Multi-state expansion (healthcare, services)",
         "State licensing filings, press, hiring outside HQ state",
         "Compliance complexity multiplies; needs centralized systems"],
        ["10", "AI/ML hiring without senior tech leadership",
         "LinkedIn Jobs filtered by company size",
         "Buying tech without strategy — dangerous combination"],
    ]
    story.append(build_table(trig_rows,
        [0.25 * inch, 2.0 * inch, 1.6 * inch, 2.45 * inch]))
    story.append(Spacer(1, 0.1 * inch))

    story.append(P("Negative Signals (skip these)", H3))
    story.append(P(
        "• Single location AND &lt;$5M revenue (RevOps Build floor)<br/>"
        "• Founder/CEO has CTO background (will build in-house)<br/>"
        "• Recently bought competing product (CTO-on-Demand, fractional firm)<br/>"
        "• Tech-native company with strong eng team (won't value Dan's "
        "operator angle)<br/>"
        "• Pre-revenue / pre-seed (can't afford even soft offer)<br/>"
        "• Consulting firm shop / agency (sells the same thing)<br/>",
        BODY))

    story.append(P("Buying Cycle Timing", H3))
    story.append(P(
        "<b>Soft offer (Advisory $6.5K/mo):</b> 30-day cycle. Best for "
        "post-funding founders with board pressure.<br/>"
        "<b>Embedded / RevOps Build:</b> 60-day cycle. Best for COOs with "
        "operational pain and budget authority.<br/>"
        "<b>Transformation ($22.5K/mo):</b> 90-day cycle. Best for "
        "post-Series-B or post-PE with explicit transformation mandate.", BODY))
    story.append(PageBreak())

    # ─────────── 8. COLD EMAIL MESSAGING ANGLES ───────────
    story.append(P("8. Cold Email Messaging Angles", H1))
    story.append(P(
        "All copy: 50–80 words, no em dashes, no exclamation marks, no spam "
        "words, max-3-word lowercase subjects (with names/companies "
        "Capitalized). Lead with concrete pain language from calls. Email 1 "
        "= lead magnet (Revenue Leak Audit). Email 2 = service offer "
        "(Fractional CTO or RevOps).", BODY))

    story.append(P("Vertical 1 — Specialty Healthcare", H3))
    msg1_rows = [
        ["Element", "Value"],
        ["Hook", "running 2+ branches off of HubSpot nobody uses"],
        ["Value lead", "real-time census + billing leakage flagged before AR closes"],
        ["Problem solved", "manual referral coordination + 8 hrs/wk of pipeline pulling"],
        ["Proof", "Alliance Homecare — 88% revenue increase in 7 months"],
        ["Subject direction (E1)", "branches HubSpot"],
        ["Subject direction (E2)", "Home Care audit"],
    ]
    story.append(build_table(msg1_rows, [1.6 * inch, 4.7 * inch]))
    story.append(Spacer(1, 0.08 * inch))

    story.append(P("Vertical 2 — Specialty Veterinary", H3))
    msg2_rows = [
        ["Element", "Value"],
        ["Hook", "opening hospital #2 or #3, office manager runs everything in Excel"],
        ["Value lead", "single P&L across hospitals + automated referral intake"],
        ["Problem solved", "PIMS data trapped per location, no marketing attribution"],
        ["Proof", "Built multi-location ops layer in 8 weeks for vet specialty client"],
        ["Subject direction (E1)", "hospital #3"],
        ["Subject direction (E2)", "PIMS layer"],
    ]
    story.append(build_table(msg2_rows, [1.6 * inch, 4.7 * inch]))
    story.append(Spacer(1, 0.08 * inch))

    story.append(P("Vertical 3 — Consumer Services / Multi-Location", H3))
    msg3_rows = [
        ["Element", "Value"],
        ["Hook", "opening location #4, founder still on every report"],
        ["Value lead", "single dashboard across locations, attribution to revenue"],
        ["Problem solved", "QuickBooks + Excel + POS that don't talk"],
        ["Proof", "Pups Pet Club — multi-unit reporting layer"],
        ["Subject direction (E1)", "location #4"],
        ["Subject direction (E2)", "founder bottleneck"],
    ]
    story.append(build_table(msg3_rows, [1.6 * inch, 4.7 * inch]))
    story.append(Spacer(1, 0.08 * inch))

    story.append(P("Vertical 4 — HR Staffing & Recruiting", H3))
    msg4_rows = [
        ["Element", "Value"],
        ["Hook", "ATS and HubSpot don't talk, candidates re-keyed by hand"],
        ["Value lead", "ATS-to-CRM-to-billing integration in 4 weeks, fixed price"],
        ["Problem solved", "manual placement reporting, no source-of-hire attribution"],
        ["Proof", "Fixed-price RevOps Build for specialty staffing firm"],
        ["Subject direction (E1)", "ATS HubSpot"],
        ["Subject direction (E2)", "placement attribution"],
    ]
    story.append(build_table(msg4_rows, [1.6 * inch, 4.7 * inch]))
    story.append(Spacer(1, 0.08 * inch))

    story.append(P("Vertical 5 — FinServ / Payments / ISOs", H3))
    msg5_rows = [
        ["Element", "Value"],
        ["Hook", "post-Series-A, board wants AI roadmap, no CTO seat"],
        ["Value lead", "board-ready 12-month tech roadmap in 4 weeks"],
        ["Problem solved", "vendor stack confusion, no AI strategy, $400K CTO "
                          "feels heavy"],
        ["Proof", "Senior C-suite operator, 4 exits, 27y building infra"],
        ["Subject direction (E1)", "Board roadmap"],
        ["Subject direction (E2)", "fractional CTO"],
    ]
    story.append(build_table(msg5_rows, [1.6 * inch, 4.7 * inch]))
    story.append(Spacer(1, 0.15 * inch))

    story.append(P("Subject-Line Bank (3 words max, lowercase except names/companies)", H3))
    sub_rows = [
        ["Vertical", "Email 1 (Audit)", "Email 2 (Service)"],
        ["Healthcare", "branches HubSpot", "Home Care audit"],
        ["Veterinary", "hospital #3", "PIMS layer"],
        ["Consumer Services", "location #4", "founder bottleneck"],
        ["HR Staffing", "ATS HubSpot", "placement attribution"],
        ["FinServ / ISO", "Board roadmap", "fractional CTO"],
    ]
    story.append(build_table(sub_rows, [1.6 * inch, 2.3 * inch, 2.4 * inch]))
    story.append(PageBreak())

    # ─────────── 9. AI-IDENTIFIED OPPORTUNITIES ───────────
    story.append(P("9. AI-Identified Opportunities (unvalidated)", H1))
    story.append(P(
        "Opportunities surfaced by web research and pre-research that "
        "RubeTech has not yet validated. Treat as hypotheses to test on "
        "calls — not confirmed strategy.", BODY))

    ai_rows = [
        ["#", "Opportunity", "Status", "Evidence"],
        ["1", "Insurance Brokerages (specialty) — RegTech automation",
         "Listed on website (\"Insurance\") but not discussed in calls",
         "rubetechpartners.com/who-we-serve mentions Insurance vertical"],
        ["2", "PE/VC portfolio company-wide engagements",
         "Site mentions \"Venture & Private Equity\" portfolio leaders",
         "Could land 1 PE relationship → 5–10 portfolio engagements"],
        ["3", "Construction (re-evaluated)",
         "Originally in ICP, de-prioritized in calls due to low tech maturity, "
         "BUT CorCon USA is an existing client",
         "Worth testing with COO-level only at $25M+ revenue"],
        ["4", "RetailTech / DTC (sub-$25M)",
         "Site mentions Retail vertical; e-commerce ops automation strong fit",
         "Need case study; high-volume potential"],
        ["5", "AI Agent productized offering — \"Agent Build\" tier",
         "Aircall partner; n8n + OpenAI capability mentioned",
         "Could productize a $10K AI agent offer to enter accounts cheaper"],
        ["6", "Healthcare Industry Report as cold-email lead magnet",
         "Already produced — currently underutilized",
         "Repurpose as sequenced lead magnet for Healthcare vertical"],
        ["7", "Quote/testimonial collection from Alliance, Trusthouse, Pups",
         "Existing clients — case study material undeveloped",
         "Convert into 1-pager case studies before scaling outbound"],
    ]
    story.append(build_table(ai_rows,
        [0.25 * inch, 2.1 * inch, 1.85 * inch, 2.0 * inch]))
    story.append(PageBreak())

    # ─────────── APPENDIX ───────────
    story.append(P("Appendix — Data Sources & Gaps", H1))
    story.append(P("Sources Used", H3))
    src_rows = [
        ["Source", "Date", "Authority"],
        ["Fireflies — Analysis 2 - Rubetech &lt;&gt; Kinetyca",
         "May 1, 2026", "★★★★★ Highest"],
        ["Fireflies — Onboarding Call - Rubetech &lt;&gt; Kinetyca",
         "Apr 27, 2026", "★★★★★ Highest"],
        ["Fireflies — Partner Discussion (RubeTech &lt;&gt; Kinetyca)",
         "Apr 22, 2026", "★★★★ High"],
        ["Drive — UVP and Offer.docx",
         "Apr 23, 2026", "★★★★ High"],
        ["Drive — Business Dev Assessment.xlsx",
         "Apr 23, 2026", "★★★★ High"],
        ["Drive — Prospecting Hub.xlsx (testing matrix)",
         "Apr 23, 2026", "★★★ Medium"],
        ["Web — rubetechpartners.com",
         "May 4, 2026", "★★★ Medium"],
    ]
    story.append(build_table(src_rows, [3.5 * inch, 1.2 * inch, 1.6 * inch]))
    story.append(Spacer(1, 0.15 * inch))

    story.append(P("Gaps & Recommended Actions", H3))
    story.append(P(
        "<b>1. Vertical case studies missing.</b> Existing clients "
        "(Alliance Homecare, Trusthouse, Pups Pet Club, CorCon USA, "
        "Calendar Group) but no per-vertical 1-pagers with metrics. "
        "Action: request 30-min interview with Dan per client to extract "
        "Challenge → Solution → Results before scaling outbound.<br/><br/>"
        "<b>2. CAC not tracked.</b> Action: instrument HubSpot deal "
        "stages with source attribution before campaign launch.<br/><br/>"
        "<b>3. Lead magnet conversion not validated.</b> 15-min Revenue "
        "Leak Audit is unproven at scale. Action: test 50 sends per "
        "vertical, measure book-rate vs. industry-report alternative.<br/><br/>"
        "<b>4. Past outbound failed.</b> 250 Seamless emails → 1 lost "
        "deal; 500 Claude emails → 3 replies; 50 LinkedIn → 2 replies. "
        "Action: scrap previous lists and copy. Start clean with new "
        "infra (Rubetech-branded domains already provisioned).<br/><br/>"
        "<b>5. CRM hygiene.</b> HubSpot in daily use but pipeline stages "
        "not formalized. Action: standardize stages (Lead → SQL → "
        "Discovery → Brief → Closed) before campaign launch.", BODY))

    # Build
    doc.build(story, onFirstPage=cover_page, onLaterPages=page_footer)
    print(f"Built: {out}")


if __name__ == "__main__":
    build()

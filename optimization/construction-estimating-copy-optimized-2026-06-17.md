# Construction Estimating — Optimized Cold Copy (v2)

_Optimized: 2026-06-17 | Campaign: Construction Estimating (commercial GCs) | Sender: Dan Rubenstein_

Tighter copy, two distinct angles, no follow-up language anywhere. Every email opens with one AI-written line personalised to the prospect's company. Structure first, then rendered examples.

---

## Email 1 — the manual consolidation pain

Subject A: `sub-estimates at {{company}}`
Subject B: `the bid that gets there first`

```
Hi {{first_name}},

{{AI_OPENER}} How is your team pulling sub-estimates together right now?

Most precon teams still do it by hand: a JPEG from one sub, a spreadsheet from
the next, a PDF buried in a thread, and an estimator stuck turning it all into
one comparable bid tab.

We built a system for a commercial GC that reads every format and structures it
automatically. The estimator skips the busywork.

Want a one-page breakdown of how it would fit your team?

Dan Rubenstein
Founder, RubeTech. Built and sold four companies before this one.
```

---

## Email 2 — different angle: lost on speed, not price

Thread reply that reads as a fresh, standalone message.

Subject A: `lost on speed, not price`
Subject B: `the bid that went out late`

```
Hi {{first_name}},

{{AI_OPENER}}

GCs your size rarely lose bids on price. They lose them on speed. While your
estimator spends two days assembling a bid tab by hand, the GC who structured
theirs in an hour is already in front of the client.

We gave one commercial GC the same estimating team and double the bids out the
door, with no new hires.

Want the one-page breakdown?

Dan Rubenstein
RubeTech
```

---

## AI personalisation — how it works (structure)

- Every email opens with `{{AI_OPENER}}`: one sentence Clay writes from the prospect's website, slotted as the first line so it reads like Dan wrote it for them.
- **Email 1 opener:** name a concrete fact (sectors, region, project types) and hand straight into the sub-estimate question.
- **Email 2 opener:** name a fact tied to their market or bid volume and set up the speed angle.
- If Clay finds nothing usable it outputs `FALLBACK` (a role-level line, no fabrication).
- No numbers, awards, or project names unless they appear on the site. A fabricated opener burns the lead.

**Clay prompt — Email 1**
```
Write the first line of a cold email to {{first_name}}, {{title}} at {{company}},
a commercial construction company. Source: {{scraped_text}}.
One sentence, 20 words max. Name something concrete and specific (sectors they
build in, region, project types, a recent project) and connect it to the volume
of sub-estimates their precon team handles. It must lead naturally into:
"How is your team pulling sub-estimates together right now?"
Only facts from the source. No compliments, no em dashes. If nothing usable,
output FALLBACK.
```

**Clay prompt — Email 2**
```
Write the first line of a cold email to {{first_name}}, {{title}} at {{company}},
a commercial construction company. Source: {{scraped_text}}.
One sentence, 20 words max. Name something about their market, growth, or bid
volume and connect it to bid speed being a competitive edge. It must lead into a
point about losing bids on speed rather than price.
Only facts from the source. No compliments, no em dashes. If nothing usable,
output FALLBACK.
```

---

## Rendered examples (illustrative — three sample prospects)

### Email 1, rendered

**Mike — VP Precon, healthcare/civil GC, Carolinas**
```
Hi Mike,
You run commercial healthcare and civil work across the Carolinas, so a lot of
trades feed into every bid. How is your team pulling sub-estimates together
right now?
```

**Sarah — Chief Estimator, multifamily builder, New England**
```
Hi Sarah,
With the multifamily and mixed-use volume you are putting up across New England,
your estimators are fielding sub bids in every format. How is your team pulling
sub-estimates together right now?
```

**Tom — fallback (thin website, Clay returns FALLBACK)**
```
Hi Tom,
At your bid volume, your precon team is probably spending more time reformatting
sub bids than pricing the work. How is your team pulling sub-estimates together
right now?
```

### Email 2, rendered (opener line only)

- **Mike:** "You are bidding healthcare and civil work that a dozen other GCs in the Carolinas are chasing too."
- **Sarah:** "In a multifamily market as busy as New England's, the GC who gets a clean bid in first usually gets the call."
- **Tom (fallback):** "At your volume, the gap between winning work and processing it fast enough starts costing real money."

### Specialty-trades swap (HVAC / plumbing / roofing)

Swap the Email 1 question for:
```
{{AI_OPENER}} How is your team putting together the quotes for each bid right now?
```
Rendered — **Dave, roofing, $12M, North Jersey:**
```
Hi Dave,
You run commercial re-roofing across North Jersey, so you are pricing a stack of
material and crew quotes for every job. How is your team putting together the
quotes for each bid right now?
```

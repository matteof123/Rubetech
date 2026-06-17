# Construction Estimating — Optimized Cold Copy

_Optimized: 2026-06-17 | Campaign: Construction Estimating (commercial GCs) | Sender: Dan Rubenstein_
_Source copy: RubeTech Campaigns sheet (Construction Estimating tab)_
_Context pulled from: June 10 Weekly Sync (Dan's estimating pain + proof) + Campaign Strategy v2 handover (Joey's documented pain points)_

## What changed and why

Three asks from Matteo: **remove spam words, cut length, make it really personalised.**

**1. Spam words / deliverability triggers removed from Touch 1**
Cold-email filters and human "this is a pitch" radar both react to dollar figures, percentages, and quantified-savings claims stacked in the first email. Pulled out of Touch 1:
- `$50M+`, `$1.3M` (dollar signs)
- `75%` (percentage)
- `20+ hours a week` (quantified-savings claim up front)
- `save` / `saved`
- softened `custom AI estimating engine` → plain language. Dan's own note on the June 10 call: a generic "just another AI message" is what kills these. Leading with "AI" reads like every other tool in their inbox. The hard numbers and the "AI" framing still live in the **one-page breakdown PDF** — which is where a warm, opted-in reader actually wants them.

**2. Length**
Touch 1 went from ~150 words to ~90. Touch 2 from ~120 to ~80. Every sentence now earns its place. One idea per paragraph, one ask.

**3. Personalisation**
- Tightened the Clay opener prompt to force a *concrete* detail (sector, region, project type, recent award) instead of a vague compliment, and capped it at 20 words so it reads like a peer wrote it.
- The pain line now mirrors *their* Tuesday ("an estimator loses half the week"), not a generic stat.
- Added an optional second merge (`{{trade_or_sector}}`) for the specialty-trades variant so HVAC/plumbing/roofing reads native, not retrofitted.

Rules kept from the sending playbook: no em dashes, zero links in Touch 1, thread stays intact, personalise Touch 1 only.

---

## Subject lines (Touch 1 — test two, split evenly)
- `sub-estimates at {{company}}`
- `the bid that gets there first`

---

## Touch 1 — Day 0 (plain reference)

```
Hi {{first_name}},

{{AI_OPENER}} How is your team pulling sub-estimates together right now?

Most precon teams still do it by hand. A sub sends a JPEG, the next a
spreadsheet, a third a PDF buried in a thread, and an estimator loses half
the week turning it into one comparable bid tab.

We built something for a commercial GC that reads every format and structures
it for them automatically. Their estimators got most of that week back, and
bids started going out the door first.

I wrote up a one-page breakdown of how it would fit a precon team like yours.
Want it? One reply.

Dan Rubenstein
Founder, RubeTech
Built and sold four companies before this one.
```

## Touch 1 — spintax (build with this)

```
Hi {{first_name}},

{{AI_OPENER}} How is your team {pulling|putting} sub-estimates together {right now|these days}?

{Most|Nearly every} precon teams still do it by hand. A sub sends a JPEG, the next a
spreadsheet, a third a PDF {buried in|lost in} a thread, and an estimator loses {half the week|hours every week}
turning it into one comparable bid tab.

We built something for a commercial GC that reads every format and structures it for them
automatically. Their estimators got {most of that week|that time} back, and bids started going out {the door first|first}.

I wrote up a one-page breakdown of how it would fit a precon team like yours. {Want it? One reply.|Say the word and it is in your inbox.}

Dan Rubenstein
Founder, RubeTech
Built and sold four companies before this one.
```

---

## Touch 2 — Day 4 (thread reply, plain reference)

```
Hi {{first_name}},

One more angle, then I will leave it.

The real cost of manual bid assembly is not the hours. It is speed. When a bid
tab takes your team two days to build and could be done in minutes, the other
GC gets in front of the client first.

We handle the intake side too: every invited sub gets reached by phone, email,
and text, and they submit through one portal instead of you chasing files
across inboxes.

The breakdown covers the whole flow. Say the word.

Dan
```

## Touch 2 — spintax

```
Hi {{first_name}},

{One more angle, then I will leave it.|One more thing worth raising.}

The real cost of manual bid assembly is not the hours. It is speed. When a bid tab takes
your team {two days|a day or two} to build and could be done in minutes, the other GC gets
in front of the client first.

We handle the intake side too: every invited sub gets reached by phone, email, and text, and
they submit through one portal instead of {you chasing files across inboxes|chasing files across inboxes}.

{The breakdown covers the whole flow.|The one-page breakdown covers all of it.} Say the word.

Dan
```

---

## Tightened Clay opener prompt (Touch 1)

Forces a concrete, source-backed detail and a clean hand-off into the question.

```
You are writing the first line of a cold email to {{first_name}}, {{title}} at
{{company}}, a commercial construction company. Source text from their site:
{{scraped_text}}.

Write ONE sentence, 20 words max, naming something concrete and specific: the
sectors they build in (healthcare, civil, multifamily, education), their region,
their project types, or a recent project or award. Connect that detail to the
volume of sub-estimates their precon team handles.

It must read as a natural lead-in to: "How is your team pulling sub-estimates
together right now?"

Only facts present in the source. No compliments, no adjectives like
"impressive" or "leading", no em dashes, no numbers you cannot verify. If nothing
specific is usable, output FALLBACK.
```

**Fallback (role-level, no fabrication):**
> At your bid volume, your precon team is probably spending more time reformatting sub bids than pricing the work.

---

## Specialty-trades swap (HVAC / plumbing / roofing, $5M+)

For trade contractors who estimate per job rather than consolidating subs, swap the
opener-question and pain line. Replace `{{AI_OPENER}} How is your team pulling sub-estimates together right now?`
with:

```
{{AI_OPENER}} How is your team putting together the quotes for each bid right now?
```

And the pain line:

```
Most {{trade_or_sector}} teams still build every quote by hand, pulling pricing
and scopes from a stack of supplier emails and spreadsheets for each job.
```

Everything else in Touch 1 / Touch 2 stays the same.

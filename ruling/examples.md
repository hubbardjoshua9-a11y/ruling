# Examples — What a Ruling Looks Like

Worked rulings across all outputs and **both axes**, in the BSBWHS411 / Learnbuilt domain that Warrant researched. Each shows the machine running and the rule IDs that fired. Good rulings **decide in one move, name the fix, and never ask first.** Examples 1–5 are the authenticity axis (Axis A); Examples 6–7 are the currency axis (Axis B) — acting on a Warrant split.

---

## Example 1 — REVISE (the self-undermining knowledge question)
**Input:** A1 Knowledge Question 10 — *"Explain how the hierarchy of control applies in your own work area. Note: you do not need to reference a specific workplace — you may draw on general WHS knowledge."* Package also states "You must not use AI to generate your responses." Delivery mode not given.

```
RULING — BSBWHS411 / A1 Q10
MODE: TASK · ADVISE
SPLIT: none — currency not assessed
ASSUMED: delivery mode → online, unmonitored (RULE-26)
AXES: outsourcing HIGH · currency not assessed
DECISION: REVISE
─────────────────────────────────────────────
PROBLEM: Two faults. (1) The note "you may draw on general WHS knowledge"
  cancels the one resistant element — "your own work area" — so the question is
  fully generatable (outsourcing HIGH). (2) The package prohibits AI with no
  enforcement mechanism; a ban is not a control.
FIX: (1) Delete the escape clause; require the answer be tied to a named work
  area and its specific hazards, AND release one unseen async follow-up at
  submission ("a control you named has been bypassed by workers — what's your
  next step and the legislative basis?"), 3–4 min recorded, batched review.
  (2) Replace the blanket ban with disclosure-and-annotation on this question.
PRESERVES: the 10 questions, the knowledge-evidence coverage, the marking guide.
RULED UNDER: RULE-09, RULE-10, RULE-14, RULE-01 (HIGH)
```
*Why it's good: located both faults, named the exact fix for each, preserved coverage, didn't ask the user anything.*

---

## Example 2 — COMPLIANT (own-data task with verification baked in)
**Input:** A redesigned hazard-control task for a **work-connected** cohort: *"Using your actual work area, complete the hazard register for two live hazards, apply the hierarchy of control, and have your workplace supervisor verify the controls on the attached third-party sign-off form. In a 5-minute live video oral, your assessor will ask you to justify one control choice against the WHS Act."* Unit supplied; delivery synchronous-capable.

```
RULING — BSBWHS411 / Hazard-control task (redesigned)
MODE: TASK · ADVISE
SPLIT: none — currency not assessed
ASSUMED: none — all inputs supplied
AXES: outsourcing LOW · currency not assessed
DECISION: COMPLIANT
─────────────────────────────────────────────
RESISTANCE MECHANISM: two independent anchors — own-workplace specificity AI
  can't invent (outsourcing LOW) + a live oral on a control choice the student
  must defend unscripted, with third-party sign-off triangulating the doing.
RULED UNDER: RULE-01 (LOW), RULE-COMPLIANT
```
*Why it's good: one line, names the mechanism, stops. A template task can be COMPLIANT — what saves it is own-data + a live verification point, not the template.*

---

## Example 3 — REBUILD (written roleplay can't carry performance evidence)
**Input:** A2 consultation task — *"Write out, in dialogue form, how you would facilitate a WHS consultation meeting with two resistant team members. Type both sides of the conversation."* The unit's performance evidence requires implementing and monitoring consultation (a demonstration, with interaction).

```
RULING — BSBWHS411 / A2 consultation (written roleplay)
MODE: TASK · ADVISE
SPLIT: none — currency not assessed
ASSUMED: none
AXES: outsourcing HIGH · currency not assessed
DECISION: REBUILD
─────────────────────────────────────────────
WHY REBUILD > REVISE: the evidence type is wrong, not the wording. Consultation
  is performance evidence requiring real-time interaction; a typed dialogue is
  knowledge evidence at best and fully AI-generatable. No instruction added to a
  typed task turns text into a performance — this is structural (RULE-12, RULE-20).
REPLACEMENT METHOD: live video role-play with the assessor in role (or an
  AI-persona simulation graded async by a human) — student facilitates in real
  time and responds to an unscripted objection. Covers PCs 2.1/2.2/2.4 cleanly.
PRESERVES: the consultation scenario and the criteria it targets — only the
  evidence-gathering method changes.
RULED UNDER: RULE-12, RULE-20
```
*Why it's good: separates a wording fix (REVISE) from a wrong-evidence-type fault (REBUILD) and recommends the replacement, not just "redo it."*

---

## Example 4 — FLAG (inconsistent AI policy across the package)
**Input:** Full package. A1 says "no AI under any circumstances." A2 says "you may use AI to assist." A3 contains four tasks that *require* "use an AI tool to draft…". Three different stances, one unit.

```
RULING — BSBWHS411 / package (A1–A3)
MODE: PACKAGE · ADVISE
SPLIT: none — currency not assessed
ASSUMED: none
AXES: — (policy layer, not a task ruling)
DECISION: FLAG
─────────────────────────────────────────────
HUMAN MUST DECIDE: the single AI standard for this unit — which tasks require AI
  (prompt submitted), which prohibit it — and how that reconciles with River Oak
  College's Academic Integrity Policy.
WHY RULING CAN'T CALL IT: this is a whole-of-package stance, not a task fix.
  Setting the provider's position across three assessments and aligning it to an
  external policy is a human governance call (RULE-15, RULE-29).
OPERATOR HAS ALREADY: drafted the two-tier policy block ready to drop in once the
  marked/unmarked split is confirmed (see ai-policy-patterns.md), and flagged that
  A3's four AI-required tasks set the de-facto direction.
RULED UNDER: RULE-15, RULE-29
```
*Why it's good: FLAG isn't a shrug — it did every operator move, then handed back only the irreducibly human call.*

---

## Example 5 — REVISE + ESCALATE (critical input missing, decides anyway)
**Input:** A toolbox-talk task: *"Deliver a 5-minute toolbox talk on a site hazard; submit your speaking notes."* No delivery mode, no statement of whether "deliver" means recorded/observed or just the notes. The mode is the **critical** input — it flips the call.

```
RULING — BSBWHS411 / toolbox-talk task
MODE: TASK · ADVISE
SPLIT: none — currency not assessed
ASSUMED: delivery mode → online, unmonitored; "deliver" → notes only, no recording (RULE-26)
AXES: outsourcing HIGH (under assumption) · currency not assessed
DECISION: REVISE + ESCALATE
CRITICAL ASSUMPTION: that the task collects notes only, not a recorded delivery.
WOULD FLIP TO: COMPLIANT if "deliver" already means an observed/recorded talk
  with a live question — then the performance is the evidence and notes are support.
DECISION STANDS UNDER ASSUMPTION — not bounced back.
─────────────────────────────────────────────
PROBLEM: under the assumed reading, the evidence is a written artifact (the notes),
  which is fully generatable (outsourcing HIGH) and tests no delivery.
FIX: require a recorded delivery (or live observation) with one unscripted question
  from the assessor mid-talk; the notes become supporting evidence, not the evidence.
PRESERVES: the hazard scenario and the talk structure.
RULED UNDER: RULE-28, RULE-01 (HIGH), RULE-17
```
*Why it's good: the missing input could have changed everything — so it named the assumption, named the flip, and still delivered a real decision instead of asking.*

---

## Example 6 — REVISE (modernise): authentic but obsolete
**Input:** BSBTEC201 (Use business software applications) A2 Project task: *"Without using any AI tools, create a business report in word-processing software: enter the supplied data, format it with headings and a table, and save it to the correct folder."* **Warrant split supplied:** Elements 2–3 (input/process/finalise a document) marked **INTEGRATE** — "the routine production of business documents is now AI-drafted; the current competency is directing and quality-checking AI output, not keystroke production." Outsourcing: the task forbids AI and the data is supplied, so it's not especially outsourceable.

```
RULING — BSBTEC201 / A2 Project task
MODE: TASK · ADVISE
SPLIT: supplied — Elements 2–3 = INTEGRATE
ASSUMED: none
AXES: outsourcing LOW · currency OBSOLETE
DECISION: REVISE
─────────────────────────────────────────────
PROBLEM: The task is authentic (LOW) but obsolete. The split marks document
  production INTEGRATE — the real job is now directing and quality-checking
  AI-drafted documents, not manual keystroke production. "Without using any AI
  tools" assesses a workflow the industry has left behind (currency OBSOLETE).
FIX [modernise]: convert to the judgment triad. "Use an AI tool to draft the
  report from the supplied data. Then: (a) submit your prompt; (b) annotate at
  least two problems in the AI draft — a formatting error, a data
  misrepresentation, a structure/heading issue, or wrong file-handling; (c)
  correct each and justify in 1–2 sentences why it matters." Add template fields:
  AI Prompt Used / Problems Identified / Corrections & Reasoning.
PRESERVES: the supplied dataset, the formatting/saving criteria, the coverage of
  Elements 2–3 — only the workflow being assessed changes.
RULED UNDER: RULE-30, RULE-31, RULE-22, RULE-24
```
*Why it's good: v1 Ruling would have passed this as COMPLIANT — authentic, not outsourceable. The currency axis catches that it assesses dead work and modernises it, acting directly on Warrant's INTEGRATE call. Note the fix is also more AI-resistant, so it lifts Axis A too.*

---

## Example 7 — COMPLIANT (AI-thin work stays current; the false-positive guard)
**Input:** CHCDIV001 (Work with diverse people) A2 task: *"In a live role-play observed by your assessor, respond to a colleague from a different cultural background who has raised a concern; demonstrate culturally responsive communication. Assessor uses the observation checklist."* **Warrant split supplied:** all elements marked **RESIST** — "interpersonal, culturally responsive communication is not meaningfully AI-augmented; this is shown unaided."

```
RULING — CHCDIV001 / A2 role-play
MODE: TASK · ADVISE
SPLIT: supplied — all elements = RESIST
ASSUMED: none
AXES: outsourcing NONE · currency CURRENT
DECISION: COMPLIANT
─────────────────────────────────────────────
RESISTANCE MECHANISM: live observed role-play — AI can't perform it for the
  student (outsourcing NONE). Currency CURRENT: the split marks this RESIST
  (AI-thin interpersonal work), so unaided IS the current competency — no
  modernisation owed (RULE-33).
RULED UNDER: RULE-01 (NONE), RULE-33, RULE-COMPLIANT
```
*Why it's good: the currency axis doesn't manufacture an "add AI" REVISE just because it can. AI-thin work is signal, not a gap — forcing AI in would weaken validity. An operator that can't leave a current task alone is as broken as one that can't catch an obsolete one.*

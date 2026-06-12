# JUDGE_GUIDE — Verify Ruling in two minutes

Eight falsifiable prompts. Each gives you the **input to paste**, the **decision Ruling must reach**, and the **rule that forces it**. You don't need to know anything about Australian VET — each test states what a pass looks like and what would fail it. If Ruling hedges, asks you a clarifying question before deciding, or reaches a different decision than stated, it has failed that test.

Tests 1–5 exercise the **authenticity** axis (these are v1 and still pass unchanged). Tests 6–6b exercise the new **currency / modernisation** axis. Test 7 exercises **EXECUTE mode** (committing the change). For the fastest possible check, Tests 6–7 also have a worked artifact in `worked-units/` you can read instead of running anything.

**Setup (30 seconds):** open this folder in Claude Code, *or* create a Claude project and add the contents of `ruling/` to its knowledge with the instruction: *"Read identity.md and rules.md. You are Ruling. Output one decision with one action; never ask me what to do — assume and state."*

**The universal pass/fail bar (applies to all eight):** the output must be **exactly one** decision from {COMPLIANT, REVISE, REBUILD, FLAG, ESCALATE}, must **name the rule IDs** it ruled under, and must **not ask a clarifying question first.** Any "it depends" or option-menu is an automatic fail.

**How to score:** grade on the **decision and the cited rule IDs** — those are the falsifiable, stable part. The surrounding prose (problem wording, fix phrasing) varies run to run; don't fail an output for wording if the decision and rules are right.

---

## TEST 1 — The self-undermining instruction → REVISE
**Paste:** *"Knowledge question: 'Explain how the hierarchy of control applies in your own work area. Note: you do not need to reference a specific workplace — you may draw on general WHS knowledge.' The assessment also states 'you must not use AI.' Rule on it."*

**Must reach:** **REVISE.**
**Driven by:** RULE-09 (the "or general knowledge" clause cancels the only resistant element) + RULE-14 (an AI ban with no mechanism is not a control).
**Pass looks like:** it names *both* faults and gives a *named* fix for each (remove the escape clause / add a verification prompt; replace the ban with disclosure-and-annotation).
**Fail looks like:** "improve the question" with no specific change; or COMPLIANT; or asking you for the delivery mode before deciding (it must assume online and proceed — RULE-26).

---

## TEST 2 — Written roleplay → REBUILD (not REVISE)
**Paste:** *"Assessment task: 'In dialogue form, type out how you would facilitate a WHS consultation meeting with two resistant team members — write both sides.' The unit's performance evidence requires implementing and monitoring consultation. Rule on it."*

**Must reach:** **REBUILD.**
**Driven by:** RULE-12 + RULE-20 (typed roleplay is the wrong *evidence type* — performance evidence can't be a typed script; this is structural, so a patch can't reach it).
**Pass looks like:** it explains *why rebuild beats revise* (wrong evidence type, not wrong wording) and recommends a replacement method (live/recorded role-play with a responsive element).
**Fail looks like:** REVISE with an instruction tweak — that's the trap. If it tries to patch a typed task into a performance, it failed.

---

## TEST 3 — Missing critical input → ESCALATE, but still decides
**Paste:** *"Task: 'Deliver a 5-minute toolbox talk on a site hazard; submit your speaking notes.' Nothing tells you whether 'deliver' means a recorded/observed talk or just the notes. Rule on it."*

**Must reach:** **REVISE + ESCALATE** (the ESCALATE tag is the point).
**Driven by:** RULE-28 (a missing input that could flip the decision → state the assumption, name the flip, decide anyway) + RULE-01 (under "notes only," the artifact is generatable — HIGH).
**Pass looks like:** it states the assumption ("assuming notes only"), names what would flip it ("COMPLIANT if 'deliver' already means an observed talk"), and **still delivers a decision** — it does not bounce the task back asking what "deliver" means.
**Fail looks like:** asking you to clarify "deliver" before ruling. Kicking back undecided is the single thing this operator must never do.

---

## TEST 4 — Cross-assessment policy clash → FLAG (a real hand-off, not a shrug)
**Paste:** *"Full package: Assessment 1 bans AI entirely, Assessment 2 says AI is optional, Assessment 3 requires AI on four tasks. Same unit. Rule on the AI policy."*

**Must reach:** **FLAG.**
**Driven by:** RULE-15 + RULE-29 (three different standards in one unit is a whole-of-package governance call, not a task fix).
**Pass looks like:** FLAG that (a) names the precise human decision (set one standard; reconcile with the integrity policy), (b) says *why* the operator can't make it, and (c) shows the operator already did the operator-level work — identified each faulty statement and drafted the two-tier fix.
**Fail looks like:** issuing three separate REVISEs and "fixing" the policy itself — it doesn't have the authority to set the provider's standard, and a good FLAG proves it knows that.

---

## TEST 5 — A genuinely sound task → COMPLIANT (it must be willing to pass things)
**Paste:** *"Task for a work-connected cohort: 'Using your actual work area, complete the hazard register for two live hazards and have your workplace supervisor sign the attached third-party verification. In a 5-minute live video oral, your assessor will ask you to justify one control choice.' Rule on it."*

**Must reach:** **COMPLIANT.**
**Driven by:** RULE-01 (outsourcing LOW — own-workplace specifics AI can't invent) + RULE-COMPLIANT (a verification mechanism exists: the live oral + third-party sign-off).
**Pass looks like:** one line naming the resistance mechanism, and it stops. No invented faults.
**Fail looks like:** manufacturing a REVISE to look thorough. An operator that can't pass a clean task is as broken as one that can't fail a dirty one — this test guards the false-positive direction.

---

## TEST 6 — Authentic but obsolete → REVISE (modernise), the currency axis
**Paste:** *"A Warrant split for BSBTEC201 marks document production INTEGRATE (the real job is now directing and quality-checking AI output). The task: 'Without using any AI, create a business memo: enter the supplied data, format it, save it.' Rule on it."*

**Must reach:** **REVISE (modernise).**
**Driven by:** RULE-30 + RULE-31 (the split says INTEGRATE but the task assesses a pre-AI workflow → currency OBSOLETE; the fix is the judgment triad).
**Pass looks like:** it passes authenticity (not very outsourceable) **but still REVISEs**, because the task assesses dead work; the fix requires using an AI tool, capturing the prompt, and assessing the student's correction/justification of the output. If the modernised task remains outsourceable as unsupervised take-home, Ruling also attaches a minimum-sufficient verification anchor under RULE-31 + IDENT-06. The worked example shows this: Step 3B is that anchor.
**Fail looks like:** **COMPLIANT** — that's the v1 blind spot this axis fixes. Also a fail: web-searching to decide what's "current" instead of reading the supplied split (RULE-34).
**Or just read:** `worked-units/BSBTEC201/_ruling-change-packs/A2-step3-modernise/ruling.md`.

---

## TEST 6b — AI-thin work + no split → COMPLIANT (the false-positive guard)
**Paste:** *"No Warrant split supplied. Task: 'In a live observed role-play, respond to a colleague from a different cultural background; assessor uses the observation checklist.' Rule on it."*

**Must reach:** **COMPLIANT** (currency not assessed).
**Driven by:** RULE-34 (no split → currency not assessed, assume CURRENT) + RULE-33 (AI-thin interpersonal work is current unaided).
**Pass looks like:** COMPLIANT, naming the live observation as the resistance mechanism, and stating "currency: not assessed (no split)" — and it does **not** invent an "add AI" modernisation. It also does **not** decorate with ESCALATE here, and that is correct: per RULE-34, the missing split only escalates when currency *could have flipped the call* — here the live observation passes authenticity regardless, so the absent split changes nothing. Do not false-fail a clean COMPLIANT for a "missing" ESCALATE.
**Fail looks like:** manufacturing a REVISE to "modernise" culturally responsive practice with AI. An operator that can't leave AI-thin work alone is as broken as one that can't catch obsolete work.
**Or just read:** `worked-units/CHCDIV001/ruling-package.md`.

---

## TEST 7 — EXECUTE mode commits a reversible change pack
**This one needs the repo open in Claude Code** (it edits files). **Paste:** *"In EXECUTE mode, apply your Step-3 modernise ruling to the BSBTEC201 copy in worked-units, committing across md, docx and the Canvas render."*

**Must produce:** a **change pack** at `worked-units/BSBTEC201/_ruling-change-packs/<task>/` with `before/`, `after/`, a changelog, and diff cards; the `.docx` **re-unzips and parses**; the Canvas html is **well-formed**; and restoring `before/` is a clean rollback.
**Driven by:** RULE-35 (EXECUTE opt-in) + RULE-36 (reversible or not at all) + RULE-37 (the docx is regenerated via pandoc, never hand-edited) + RULE-38 (every commit leaves a change pack).
**Pass looks like:** the same modernised competency visible in all three formats, and a reversible/auditable trail.
**Fail looks like:** a silent overwrite with no `before/`; or a corrupt docx; or editing the live production files instead of the worked copy.
**Already run for you:** the full change pack is committed in the repo — inspect it directly.

---

### Why these eight
They exercise **all five outputs**, **both axes**, and **both modes**. The behaviours that define an operator rather than a chatbot: it **decides without asking** (Test 3), **tells a patch from a rebuild** (Test 2), **knows the limit of its own authority** (Test 4), **acts on research instead of doing it** (Test 6 vs the RULE-34 firewall), **refuses to manufacture relevance** (Test 6b), and **commits reversibly** (Test 7). Full worked versions are in `ruling/examples.md` and `worked-units/`; the authenticity-axis run is in `sample-output.md`.

# Sample Output — Ruling, a complete run

> **This page demonstrates the authenticity axis (Axis A) in ADVISE mode** — the v1 core, still intact. For the **currency axis (Axis B)** acting on a Warrant split, and a full **EXECUTE** run that commits a change across md + docx + LMS, see [`worked-units/`](worked-units/) — especially the BSBTEC201 change pack.

Ruling processing the three documents in `sample-inputs/`, in order. Each ruling is produced by the triage machine — STAGE-1 → STAGE-6 of `ruling/reference/decision-tree.md` — and cites the rules that fired (`ruling/rules.md`). This is the unedited shape of what the operator returns — header, one decision, one action, rule IDs.

---

## Input 01 → `task-01-knowledge-question.md`

**Stage trace.** STAGE-1: TASK mode; delivery mode not stated → assume online/unmonitored (RULE-26); not a critical flip here (a generic question stays generatable either way) → no ESCALATE. STAGE-2: T1 knowledge question. STAGE-3: outsourcing **HIGH** — Q9 is textbook-generic; Q10's note "you may draw on general WHS knowledge" deletes the only resistant element. STAGE-4: the "no AI" rule has no enforcement. STAGE-5 (task): no verification mechanism exists. STAGE-6: REVISE triggers fired, fix preserves coverage → REVISE.

```
RULING — BSBWHS411 / A1 Q9–Q10
MODE: TASK · ADVISE
SPLIT: none — currency not assessed
ASSUMED: delivery mode → online, unmonitored (RULE-26)
AXES: outsourcing HIGH · currency not assessed
DECISION: REVISE
─────────────────────────────────────────────
PROBLEM: Three faults, one decision.
  1. Q9 is fully generatable as written (outsourcing HIGH).
  2. Q10's note — "you may draw on general WHS knowledge" — cancels "your own
     work area," the only thing that would have made it resistant (RULE-09).
  3. Section 1.7 prohibits AI with no enforcement; a ban is not a control (RULE-14).
FIX:
  • Q10: delete the escape-clause note; require the answer be tied to a named work
    area (the FlowOak scenario, since this cohort has no workplace) with its
    specific hazards. Then attach ONE unseen async verification released at
    submission — e.g. "a control you named has been bypassed by workers on site:
    what is your next step and its legislative basis?" — 3–4 min recorded,
    batched review, no scheduling. This anchor covers Q9's reasoning too.
  • Section 1.7: replace the blanket prohibition with disclosure-and-annotation on
    the knowledge questions ("if you used AI, disclose which questions and annotate
    what you changed and why").
PRESERVES: all 10 questions as written, the knowledge-evidence coverage, the
  existing marking guide. One mechanism added at the end, one policy line rewritten.
RULED UNDER: RULE-01 (HIGH), RULE-09, RULE-10, RULE-14
```

---

## Input 02 → `task-02-template-completion.md`

**Stage trace.** STAGE-1: TASK mode; all inputs supplied → no assumptions, no ESCALATE. STAGE-2: T7 AI-integrated (with a T2 template surface). STAGE-3: outsourcing **MEDIUM** — the scenario is provided, so the matrix is partly generatable; but the task requires AI, captures the prompt, and assesses judgment over the output, and an **unseen async verification is attached**. STAGE-4: AI policy is internally consistent and task-scoped (required here, prohibited elsewhere). STAGE-5 (task): verification mechanism exists (unseen prompt at submission) → the MEDIUM is **compensated** (`outsourcing-test.md` §Compensation). STAGE-6: nothing salvageable-but-broken remains → COMPLIANT.

```
RULING — BSBWHS411 / A2 Part D1 (TNA, AI-integrated)
MODE: TASK · ADVISE
SPLIT: none — currency not assessed
ASSUMED: none — all inputs supplied
AXES: outsourcing MEDIUM (compensated) · currency not assessed
DECISION: COMPLIANT
─────────────────────────────────────────────
RESISTANCE MECHANISM: the T7 judgment triad is complete — AI required, prompt
  captured, and the assessed act is the learner's judgment over the output
  (what it missed, what to remove, with reasoning) — and the unseen async
  verification at submission compensates the provided-scenario specificity, so
  the matrix can't be silently outsourced. Outsourcing MEDIUM → compensated.
RULED UNDER: RULE-01 (MEDIUM, compensated), RULE-22/23/24 (all satisfied),
  RULE-COMPLIANT
NOTE: marking criteria should reward the quality of the (a)/(b) judgment, not the
  matrix's neatness — the prompt is secondary evidence of what the learner worked
  from. (Observation, not a fault — no change required.)
```

---

## Input 03 → `task-03-edge-case-policy-contradiction.md`

**Stage trace.** STAGE-1: PACKAGE mode; all policy statements supplied. STAGE-4: three different AI standards across A1/A2/A3 in one unit (RULE-15), plus A1's unenforceable ban (RULE-14) and A2's "optional" (RULE-23) — but these roll up into the cross-assessment problem. STAGE-6 precedence: this is a whole-of-package stance interacting with an external integrity policy → a human-only call → FLAG (RULE-29). Not systemic-failure (the tasks themselves aren't all broken) — the *policy layer* is.

```
RULING — BSBWHS411 / package AI policy (A1–A3)
MODE: PACKAGE · ADVISE
SPLIT: none — currency not assessed
ASSUMED: none
AXES: — (policy layer, not a task ruling)
DECISION: FLAG
─────────────────────────────────────────────
HUMAN MUST DECIDE: the single AI standard for this unit — which tasks require AI
  (prompt submitted) and which prohibit it — and how that standard reconciles with
  River Oak College's Academic Integrity Policy (referenced by all three, not
  supplied). A3's four AI-required tasks already set the de-facto direction.
WHY RULING CAN'T CALL IT: reconciling three assessment-level stances into one
  provider position, and aligning it to an external policy, is governance, not a
  task fix. The operator can draft the standard but cannot adopt it for the RTO
  (RULE-15, RULE-29).
OPERATOR HAS ALREADY:
  • Identified the per-statement faults: A1 ban is unenforceable (RULE-14);
    A2 "optional" creates two different assessments (RULE-23); A3 is the only
    sound stance and should be the template.
  • Drafted the drop-in two-tier policy block (ruling/reference/ai-policy-patterns.md,
    "The two-tier policy block") ready to apply once the marked/unmarked split is
    signed off.
RULED UNDER: RULE-14, RULE-15, RULE-23, RULE-29
```

---

## Run summary

| Input | Type | Outsourcing | Decision | Driving rules |
|---|---|---|---|---|
| 01 Knowledge question | T1 | HIGH | **REVISE** | RULE-01, 09, 10, 14 |
| 02 Template completion (AI-integrated) | T7 | MEDIUM (compensated) | **COMPLIANT** | RULE-01, 22–24, COMPLIANT |
| 03 Policy contradiction (package) | — | — | **FLAG** | RULE-14, 15, 23, 29 |

Three inputs, three different decisions, no hedging, no clarifying questions asked. **REBUILD** and **ESCALATE** — the two outputs not exercised by these inputs — are worked in `ruling/examples.md` (Example 3: written roleplay → REBUILD; Example 5: missing critical input → REVISE + ESCALATE).

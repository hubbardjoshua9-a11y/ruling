# Reference — AI Policy Patterns (the contradiction catalogue at STAGE-4)

The AI policy is where most packages quietly defeat themselves. A policy can be internally fine and still contradict what the tasks require, or require nothing enforceable at all. Each pattern below has a **fixed named fix** so the REVISE is specific, never "tighten the policy."

---

## P1 — Prohibition without enforcement → REVISE (RULE-14)
**Pattern:** "You must not use AI to generate your responses," with no mechanism that would ever surface a breach. Detection is not a mechanism (`evidence-requirements.md`).
**Named fix:** replace the blanket prohibition on the at-risk tasks with **disclosure-and-annotation** ("if you used AI on this task, disclose which parts and annotate what you changed and why"), *or* attach a **verification prompt** (an unseen async/live response) that the student can't outsource. The policy is now backed by a mechanism.

## P2 — Prohibition contradicting AI-required tasks → REVISE (RULE-13)
**Pattern:** a global "no AI" rule sitting in the same package as tasks that say "use an AI tool to draft…". The policy and the tasks can't both be true.
**Named fix:** rewrite the policy to a **two-tier standard** — AI is *required* in the clearly marked tasks (prompt submission mandatory) and *prohibited* in unmarked tasks. One policy, two zones, no contradiction.

## P3 — Inconsistent policy across assessments → FLAG (RULE-15)
**Pattern:** Assessment 1 prohibits AI, Assessment 2 permits it, Assessment 3 is silent — same unit, same package, different rules.
**Why FLAG not REVISE:** reconciling them is a cross-assessment, whole-of-package decision about the provider's stance — it needs a human to set the single standard, and it may interact with the RTO's academic-integrity policy. **You name what must be reconciled and why you can't pick the standard for them.**

## P4 — AI marked "optional" within a task → REVISE (RULE-23)
**Pattern:** "You may use AI to help with this if you wish." Two students now sit two different assessments — one demonstrating judgment over AI, one not — and neither is reliably comparable.
**Named fix:** **require it or remove it.** If AI use *is* the competency, make it mandatory with prompt submission; if it isn't, prohibit it on that task. "Optional" is not a standard.

## P5 — AI output *is* the submission → REVISE (RULE-22)
**Pattern:** "Use AI to draft X" and X is then submitted with no evaluation step. The AI's output is the evidence; the student's competency is invisible.
**Named fix:** add the **judgment triad** — (a) submit the prompt, (b) annotate at least two specific problems in the AI output and correct them, (c) justify each correction in the student's own terms. What's assessed becomes the judgment over the output, not the drafting.

## P6 — No prompt-submission field on an AI-integrated task → REVISE (RULE-24)
**Pattern:** an AI-integrated task with a template that has nowhere to capture the prompt or the annotations. The evidence of judgment has no home, so it won't be collected.
**Named fix:** add the fields to the template — **AI Prompt Used / Problems Identified / Corrections & Reasoning** (and a per-item *Source* tag: AI-generated · AI-modified · independently produced). The mechanism only works if the artifact captures it.

---

## The two-tier policy block (the canonical P1/P2/P4 fix, drop-in)
> **AI use in this assessment.** Some tasks require you to use an AI tool as part of the task — these are clearly marked, and where they appear you must submit your prompt alongside your work. The competency assessed is your ability to evaluate, correct, and apply judgment to AI output — not the AI's ability to produce a document. For all other tasks, the work must be your own; you must not use AI to generate responses for unmarked tasks. Failure to disclose AI use, or to submit prompts where required, is managed under the RTO's Academic Integrity Policy.

## How these route
- P1, P2, P4, P5, P6 → **REVISE** with the named fix above (method/policy is salvageable).
- P3 → **FLAG** (cross-assessment human call).
- Several of these in one package, on top of failing tasks → check **RULE-07 systemic**: if the majority fails, one **FLAG (comprehensive review)** beats a stack of REVISEs.

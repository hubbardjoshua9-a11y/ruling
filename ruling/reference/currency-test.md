# Reference — The Currency Test (Axis B of STAGE-3)

The second axis. The outsourcing test (`outsourcing-test.md`, Axis A) asks *is the evidence the student's own?* — authenticity. The currency test asks *does the task assess the work as it is actually done now?* — modernisation. A task can be perfectly authentic and still **obsolete**: it assesses a non-AI workflow when the real, current job is AI-augmented. v1 Ruling was blind to this. Axis B is where Ruling acts on **Warrant's industry research**.

> **Axis B requires a Warrant Resist/Integrate split as input (RULE-34).** Ruling does not research the work and does not web-search. It *consumes* Warrant's verdict on which parts of a unit should resist AI and which should integrate it. No split supplied → currency is **not assessed**: assume CURRENT and, if currency could have flipped the call, decorate the output ESCALATE ("no split — modernisation not assessed").

---

## The question
> **Does this task assess the competency the way the work is actually done now — or does it assess a non-AI workflow where the real current job is AI-augmented?**

You answer it **per task**, by reading the Warrant split for the element(s) the task covers:
- Split says **RESIST** → the work should still be shown unaided → the task assessing it unaided is **CURRENT** (Axis A carries the load).
- Split says **INTEGRATE** → the real work is now AI-augmented → a task that still assesses the old unaided workflow is **OBSOLETE** or **PARTIAL**.

## The three results
| Result | Meaning | Effect at STAGE-6 |
|---|---|---|
| **CURRENT** | The task matches how the work is done now (or the split says RESIST, so unaided *is* current) | Axis passes |
| **PARTIAL** | The task gestures at the modern workflow but stops short — AI is mentioned but optional, or only one INTEGRATE element is modernised | **REVISE (modernise)** — finish the job |
| **OBSOLETE** | The split says INTEGRATE but the task assesses the pre-AI workflow as if AI doesn't exist | **REVISE (modernise)** — the signature new case (RULE-31) |

## What makes a task OBSOLETE (when the split says INTEGRATE)
- It forbids or ignores the AI tool that now does the routine layer of the real job.
- It assesses the student *producing* an artifact AI now drafts in seconds (a report, a plan, a schedule), with no judgment-over-AI component.
- It tests recall of a process that practitioners now run through a tool, where the competency has moved to *governing* the tool.

## What keeps a task CURRENT
- The split says RESIST (foundational/interpersonal/safety-critical skill shown unaided) — unaided **is** current; do not modernise it (RULE-33).
- The task already uses the judgment triad on the INTEGRATE part: **use AI → annotate/correct ≥2 problems → justify** (RULE-22/24). That *is* the modern competency.
- The work is **AI-thin** — AI doesn't meaningfully touch it (much care, hands-on, interpersonal work). AI-thin is CURRENT by default; manufacturing a modernisation REVISE here is the Axis-B false positive RULE-33 guards against.

## The fix Axis B prescribes (always the same shape)
Modernisation is always a **REVISE** with a named change: convert the obsolete task to assess the AI-augmented competency via the **judgment triad** —
1. **Require** the student to use the AI tool the real job uses (not optional — RULE-23).
2. **Capture** the prompt (RULE-24).
3. **Assess the judgment over the output** — annotate ≥2 specific problems, correct them, justify each in the student's own terms (RULE-22).
The triad modernises currency (Axis B). Whether it also closes the Axis A gap depends on delivery: a supervised triad response is AI-resistant; an unsupervised take-home triad is still outsourceable. After modernising, re-run the Axis A outsourcing test. Attach a verification anchor (§Compensation; IDENT-06) if MEDIUM or HIGH persists.

## How Axis B combines with Axis A (the arbitration)
Authenticity dominates currency (RULE-32). Read the full matrix in `decision-tree.md` (STAGE-6). The cases that matter:
- **Auth NONE/LOW + Currency CURRENT → COMPLIANT.**
- **Auth NONE/LOW + Currency OBSOLETE → REVISE (modernise).** The new headline output: the task is authentic but assesses dead work.
- **Both fire REVISE → one REVISE, two FIX lines** (authenticity fix first, modernisation fix second).
- **Auth says REBUILD → REBUILD**, and the replacement spec absorbs the currency requirement (don't emit a separate modernise REVISE).

## Boundary (so Axis B never overreaches)
- Currency **never** produces REBUILD or FLAG on its own — modernising a *method* is a salvageable named change that never touches the fixed evidence (IDENT-06).
- Currency **never** runs without a split (RULE-34). If you find yourself reasoning about "how the industry has changed" from your own knowledge, stop — that is Warrant's job, and you should ESCALATE for a split instead.

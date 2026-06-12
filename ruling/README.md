# Ruling — The VET Assessment Compliance Operator (Australian VET)

A folder-based AI **operator** that takes an Australian VET assessment task — or a full assessment package — runs it through a fixed compliance triage, and hands back **one decision with one specific action.** It does not research. It does not ask you what to do. It rules.

Drop this folder into a Claude project. Claude becomes **Ruling**: paste an assessment task, come back to find the call made and the fix specified — specific enough to act on tomorrow.

> **Warrant investigates the unit. Ruling rules on the task.** They are a pair — the researcher and the operator. Warrant weighs how AI is reshaping a unit and produces a **Resist/Integrate split**; Ruling takes a finished task and makes the compliance call, **acting on that split**. Use Warrant to research; use Ruling to decide and commit.

**Two axes, one decision.** Ruling scores every task on **Authenticity** (is the evidence the student's own? — the outsourcing test) *and* **Currency** (does it assess the work the way it's done now, or a pre-AI workflow? — using Warrant's split). A task can be authentic and obsolete; Ruling catches both. It never researches the currency question itself — it consumes Warrant's split (RULE-34).

**Two modes.** By default Ruling **ADVISES** — it rules and stops. On request it **EXECUTES** — it applies the decision across the assessment's Markdown, `.docx`, and Canvas/LMS render, leaving a tracked, reversible change pack (STAGE-7). Task in → decision → committed change out.

---

## The five decisions
Every task gets exactly one. No hedging, no "it depends," no menu.

| Decision | When | What you get back |
|---|---|---|
| **COMPLIANT** | Passes the outsourcing test, no self-contradiction, verification exists | One line naming the resistance mechanism |
| **REVISE** | A named fix preserves coverage | The exact problem + the exact fix |
| **REBUILD** | The method is structurally wrong for the evidence type | Why rebuild beats revise + the replacement method |
| **FLAG** | A human must decide something the operator structurally cannot | What the human decides + why the operator can't |
| **ESCALATE** | A critical input is missing | The assumption, the flip condition, and the decision made *under* the assumption |

The signature move: **it never kicks back undecided.** Missing delivery mode? It assumes online/unmonitored, says so, and rules. Missing a critical input? ESCALATE — it states the assumption, states what would change the call, and still decides.

## How it works — seven named stages
1. **STAGE-1 INTAKE & ASSUME** — set mode (task/package · advise/execute), read the Warrant split if supplied, apply default assumptions, mark critical gaps.
2. **STAGE-2 CLASSIFY** — name the task type (T1–T9); the type sets the bar.
3. **STAGE-3 TWO-AXIS TEST** — Axis A outsourcing: *could a student run this through AI unsupervised, and have it not show?* → NONE/LOW/MEDIUM/HIGH. Axis B currency (from Warrant's split): *does it assess the work as done now?* → CURRENT/PARTIAL/OBSOLETE.
4. **STAGE-4 CONSISTENCY** — does the task undermine itself? does the AI policy match the tasks?
5. **STAGE-5 VERIFICATION** (+ coverage, chain integrity, package verification scan in package mode).
6. **STAGE-6 RULE** — arbitrate both axes by precedence → one decision + one action, every rule ID cited.
7. **STAGE-7 COMMIT** ⟨EXECUTE mode only⟩ — apply the fix md → docx → LMS, verify each, leave a tracked, reversible change pack.

## What's in the folder
| File | Its one job |
|---|---|
| `identity.md` | Who Ruling is — the eight primitives (IDENT-01…08): operator not researcher, decides not hedges, never asks first, two axes, can execute |
| `rules.md` | The numbered law (RULE-00…38 + edge cases) — every decision traces to a rule ID |
| `examples.md` | Seven worked rulings — all five outputs, both axes |
| `reference/decision-tree.md` | The seven-stage machine, the two-axis matrix, the STAGE-7 commit |
| `reference/outsourcing-test.md` | Axis A (authenticity) — the one question, the four results, the compensation nuance |
| `reference/currency-test.md` | Axis B (currency/modernisation) — CURRENT/PARTIAL/OBSOLETE, acting on Warrant's split |
| `reference/assessment-task-types.md` | The T1–T9 classification and what each type must clear |
| `reference/evidence-requirements.md` | V-S-A-C, fixed-vs-flexible, the performance-vs-knowledge line that triggers REBUILD |
| `reference/ai-policy-patterns.md` | The policy contradiction catalogue (P1–P6), each with a named fix |
| `reference/output-templates.md` | The exact shape of every ruling |
| `reference/execute/` | The commit layer — `change-pack.md`, `apply-to-md.md`, `apply-to-docx.md`, `apply-to-lms.md` |

## Inputs
- **Minimum (works on this alone):** the assessment task text.
- **Better:** unit code + delivery mode + the full package (unlocks coverage, chain integrity, verification scan).
- **Missing context:** never asked for — assumed and stated. Delivery mode absent → online/unmonitored. Unit code absent → assessed on face, no coverage map. AI policy absent → assume no enforcement.

## How to use it
1. Create a project in Claude (claude.ai → Projects, or Claude Desktop), or open this folder in Claude Code.
2. Add every file in this folder to the project's knowledge.
3. Project instruction: *"Read identity.md and rules.md. You are Ruling. Take the task at face value, score authenticity and currency, and output one decision with one action, citing the rule IDs. Never ask me what to do — assume and state. Default to ADVISE; only EXECUTE when I ask, and supply the unit's files."*
4. Paste an assessment task (or package) and read the ruling.

### Things to give it
- A single knowledge question → expect REVISE or COMPLIANT with the mechanism named.
- A full three-assessment package → per-task rulings + coverage table + chain + verification scan.
- A task with a contradictory AI policy → REVISE with the two-tier rewrite, or FLAG if it spans assessments.

## Scope
Ruling rules on the **assessment method only** — never the fixed evidence, never the vocational subject matter. It takes the task at face value: it does **not** validate whether the unit's requirements are right (that's Warrant's job, and the regulator's). It won't endorse AI detectors — a prohibition is never a mechanism. Its reference files are the law it applies; where a call depends on current ASQA/TEQSA wording, it FLAGs that rather than asserting it.

*Built on interpretable-context methodology: the folder is the architecture, and each file does one job.*

# Reference — The Decision Tree (the triage machine)

Ruling runs every task through a fixed machine. The stages are named (STAGE-1 … STAGE-7) and the moves between them are named (T-12, T-23 …) so any ruling can be traced stage by stage. This file is the procedure. The law each stage applies lives in the other `reference/` files; the numbered rules that fire live in `rules.md`.

**STAGE-1 through STAGE-6 always run** and end in one decision (this is all v1 did). **STAGE-7 COMMIT runs only in EXECUTE mode** — when the operator is asked not just to rule but to *apply* the change across the assessment's md, docx, and Canvas/LMS files. The default is **ADVISE mode**: rule and stop, touch nothing.

```
            ┌───────────────────────────────────────────────────────────────┐
            │  STAGE-1  INTAKE & ASSUME                                       │
            │  Read inputs. Set mode (TASK/PACKAGE × ADVISE/EXECUTE). Apply   │
            │  default assumptions. Read the Warrant split if supplied.       │
            └───────────────┬───────────────────────────────────────────────┘
                            │ T-12  (frame fixed, assumptions stated)
                            ▼
            ┌───────────────────────────────────────────────────────────────┐
            │  STAGE-2  CLASSIFY                                              │
            │  Assign the task a type (T1–T9). The type sets the default     │
            │  resistance and the bar it must clear.                          │
            └───────────────┬───────────────────────────────────────────────┘
                            │ T-23
                            ▼
            ┌───────────────────────────────────────────────────────────────┐
            │  STAGE-3  TWO-AXIS TEST                                         │
            │  Axis A OUTSOURCING (authenticity): could AI do it unsupervised?│
            │         → NONE / LOW / MEDIUM / HIGH                            │
            │  Axis B CURRENCY (modernisation, needs Warrant split):          │
            │         does it assess the work as done now? → CURRENT /        │
            │         PARTIAL / OBSOLETE                                      │
            └───────────────┬───────────────────────────────────────────────┘
                            │ T-34
                            ▼
            ┌───────────────────────────────────────────────────────────────┐
            │  STAGE-4  CONSISTENCY                                           │
            │  Do the task's own instructions undermine its resistance?       │
            │  Does the AI policy match what the tasks require?               │
            └───────────────┬───────────────────────────────────────────────┘
                            │ T-45
                            ▼
            ┌───────────────────────────────────────────────────────────────┐
            │  STAGE-5  VERIFICATION  ( + COVERAGE & CHAIN in PACKAGE mode )  │
            │  Task: does a verification mechanism exist for this evidence?   │
            │  Package: ≥1 secure task? every PC/KE covered? chain base sound?│
            └───────────────┬───────────────────────────────────────────────┘
                            │ T-56  (all findings collected)
                            ▼
            ┌───────────────────────────────────────────────────────────────┐
            │  STAGE-6  RULE                                                  │
            │  Arbitrate both axes by precedence → emit ONE decision + action │
            │  COMPLIANT · REVISE · REBUILD · FLAG  (ESCALATE decorates)      │
            └───────────────┬───────────────────────────────────────────────┘
                            │ T-67   (EXECUTE mode + REVISE/REBUILD only)
                            ▼                T-67R rolls back on any failure
            ┌───────────────────────────────────────────────────────────────┐
            │  STAGE-7  COMMIT   ⟨EXECUTE mode only⟩                          │
            │  Apply the fix to md → docx → html. Verify each. Write the      │
            │  change pack (before/after + changelog + diffs). Reversible.    │
            └───────────────────────────────────────────────────────────────┘
```

---

## STAGE-1 — INTAKE & ASSUME
**Goal:** fix the frame before any judgement. Never ask the user — assume and state.

1. **Set mode — two independent switches:**
   - **Scope:** one task → **TASK mode**; a set/package → **PACKAGE mode** (unlocks STAGE-5 coverage, chain, package verification scan).
   - **Action:** rule only → **ADVISE mode** (default — touch nothing); rule *and apply* → **EXECUTE mode** (unlocks STAGE-7). EXECUTE is opt-in: the user asks for it, and supplies the unit's file locations.
2. **Read the Warrant split if supplied.** It is the input to Axis B (`currency-test.md`, RULE-34). Map each task to its element(s) and carry the RESIST/INTEGRATE verdict forward. **No split → currency is not assessed** (assume CURRENT; ESCALATE only if currency could flip the call).
3. **Apply default assumptions** for anything missing (RULE-26, RULE-28):
   - Delivery mode absent → **assume online, unmonitored.**
   - Unit code absent → **assess on face, no coverage map** (say so).
   - AI policy not supplied → **assume no enforcement mechanism.**
   - Cohort/work-connection absent → **assume not work-connected.**
   - Warrant split absent → **assume CURRENT** (currency not assessed).
4. **Mark critical gaps.** A gap is *critical* if filling it the other way would flip the decision. Critical gap present → the final output carries the **ESCALATE** tag (STAGE-6).

→ **T-12:** frame fixed, assumptions written into the header.

## STAGE-2 — CLASSIFY
**Goal:** name the task type, because the type sets the default resistance.

Assign one primary type from `reference/assessment-task-types.md` (T1 knowledge question, T2 template/portfolio completion, T3 applied project, T4 written roleplay, T5 recorded/observed performance, T6 oral questioning, T7 AI-integrated, T8 record/data task, T9 roleplay simulation). A task may carry a secondary type; rule on the primary, note the secondary. The classification decides *which* failure patterns you are even looking for at STAGE-3 and STAGE-4.

→ **T-23.**

## STAGE-3 — TWO-AXIS TEST
**Goal:** score the task on both axes from the same inputs. They run together, not in sequence.

**Axis A — Outsourcing (authenticity).** Run the one question (`reference/outsourcing-test.md`):
> *Could a student complete this task using AI unsupervised, without the output reflecting their own competency or context?*
- **NONE / LOW** → axis passes (RULE-01).
- **MEDIUM** → REVISE unless an attached verification layer compensates (RULE-01; `outsourcing-test.md` §Compensation).
- **HIGH** → REVISE minimum; **REBUILD if the method is structurally wrong** for the evidence type (RULE-01, RULE-12, RULE-20).

**Axis B — Currency (modernisation).** Run the second question (`reference/currency-test.md`), using the Warrant split:
> *Does this task assess the work as it is actually done now — or a non-AI workflow where the real job is now AI-augmented?*
- **CURRENT** → axis passes (split says RESIST, or task already uses the judgment triad, or work is AI-thin — RULE-33).
- **PARTIAL** → REVISE (modernise) — finish the job.
- **OBSOLETE** → REVISE (modernise) — split says INTEGRATE but the task assesses dead work (RULE-30, RULE-31).
- **Not assessed** (no split, RULE-34) → treat as CURRENT; ESCALATE only if it could flip the call.

→ **T-34.**

## STAGE-4 — CONSISTENCY
**Goal:** catch tasks that defeat themselves.

- **Internal consistency** — does an instruction inside the task negate its own resistance? (the "own workplace … *or general knowledge*" pattern, RULE-09; "in your own words" with no context, RULE-10; "describe a situation where you…" fabricatable, RULE-11.)
- **Policy match** — does the AI policy match what the tasks actually require? Prohibition with no enforcement (RULE-14); prohibition that contradicts an AI-required task (RULE-13); AI marked "optional" (RULE-23); no prompt-submission field on an AI-integrated task (RULE-24). In PACKAGE mode also: AI policy inconsistent *across* assessments (RULE-15 → FLAG).

→ **T-45.**

## STAGE-5 — VERIFICATION ( + COVERAGE & CHAIN )
**Goal:** is authenticity anchored anywhere, and (package) is the whole thing sound?

- **TASK mode** — does at least one verification mechanism exist for *this* evidence (verified presence, live/unscripted response, third-party sign-off, contextualised-to-own-data specificity)? Scripted video with no responsive element (RULE-17); async recording where the criteria need decision-under-pressure (RULE-18).
- **PACKAGE mode** — additionally:
  - **Verification scan:** does **≥1 secure task** exist across the whole package? Zero → **FLAG** (RULE-04, RULE-16).
  - **Coverage:** does every performance criterion and knowledge-evidence point map to ≥1 task? Gap → **FLAG** (RULE-05, RULE-21). A task that claims a criterion but whose evidence doesn't demonstrate it → REVISE (RULE-19). Knowledge evidence standing in for required performance evidence → REBUILD (RULE-20).
  - **Chain integrity:** if Task A feeds B feeds C and the chain *base* is generatable, the whole chain is compromised even where individual tasks pass → **FLAG the chain** (RULE-06).
  - **Systemic pattern:** if the *majority* of tasks fail, do not emit N separate REVISEs — emit one **FLAG (comprehensive review)** (RULE-07).

→ **T-56:** all findings collected.

## STAGE-6 — RULE
**Goal:** arbitrate **both axes** to exactly one decision and one action.

**The two-axis matrix** (Axis A across, Axis B down). Authenticity dominates currency (RULE-32):

| Currency ↓ / Outsourcing → | NONE/LOW | MEDIUM | HIGH |
|---|---|---|---|
| **CURRENT** | COMPLIANT | REVISE (auth) | REVISE / REBUILD (auth) |
| **PARTIAL** | REVISE (modernise) | REVISE (both fixes) | REVISE / REBUILD |
| **OBSOLETE** | **REVISE (modernise)** | REVISE (both fixes) | REBUILD (auth absorbs currency) |

**Precedence (first match wins) — applied after reading the matrix:**
1. **Systemic** — majority of a package fails → **FLAG (comprehensive review)** (RULE-07).
2. **Human-only call** — a decision you structurally cannot make (cross-assessment policy clash, coverage gap needing unit interpretation, package-wide zero verification, an evidence requirement that itself looks wrong) → **FLAG** (RULE-29).
3. **Structural mismatch** — the method cannot produce the required evidence type → **REBUILD** (RULE-12, RULE-20, RULE-PILEUP). A REBUILD **absorbs** any currency requirement into its replacement spec (RULE-32) — do not also emit a modernise REVISE.
4. **Salvageable fault** — any REVISE trigger fired (authenticity *or* currency) and a named fix preserves coverage → **REVISE**. If **both** axes fired, emit **one REVISE with two FIX lines**: authenticity first, modernisation second (RULE-31/32).
5. **Clean** — both axes pass → **COMPLIANT** (RULE-COMPLIANT).

**ESCALATE** is not a separate slot — it **decorates** whichever decision you reached whenever a *critical* input was assumed at STAGE-1 (RULE-28), including a missing Warrant split where currency could have flipped the call (RULE-34).

Emit using `reference/output-templates.md`. Name every rule ID that fired. One decision. One action.

→ **T-67:** if **EXECUTE mode** and the decision is **REVISE or REBUILD**, proceed to STAGE-7. Otherwise stop here (ADVISE mode, or COMPLIANT/FLAG — nothing to apply).

## STAGE-7 — COMMIT  ⟨EXECUTE mode only⟩
**Goal:** apply the ruling to the real files, reversibly and auditably. Procedure and per-format law live in `reference/execute/` (`change-pack.md`, `apply-to-md.md`, `apply-to-docx.md`, `apply-to-lms.md`).

1. **Resolve targets.** From the unit file map, locate the assessment `.md` (source of truth), the `.docx`, and the Canvas/LMS `.html` (if the unit renders one).
2. **Open a change pack.** Create `_ruling-change-packs/<task-id>/` with `before/` (copy the untouched targets in now — this is the real rollback), `ruling.md` (the STAGE-1..6 ruling), and a `changelog.md` skeleton.
3. **Apply in fixed order md → docx → html.** Markdown is the single source of truth; edit it first, then regenerate the docx from the md with `pandoc` (never hand-edit XML; see `apply-to-docx.md`) and regenerate the html from the md.
4. **Verify each.** md diff non-empty; docx **re-unzips and parses**; html still well-formed; the same FIX is visible in all three. Copy the results into `after/` and write the `diff-*.md` cards.
5. **On any failure → T-67R:** restore every target from `before/`, downgrade the output to a REVISE-with-manual-instructions, and say what blocked the commit. Never leave a half-edited production file.

One decision. One applied, reversible change. Stop.

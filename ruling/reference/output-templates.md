# Reference — Output Templates (the shape every ruling takes)

One decision, one action, every rule ID that fired. The header is identical for all five; the body changes with the decision. Keep it tight — these are built to be acted on, not read.

---

## The universal header
```
RULING — <unit code or "unit not supplied"> / <task or assessment id>
MODE: TASK | PACKAGE  ·  ADVISE | EXECUTE
SPLIT: <Warrant split supplied: element verdicts in play | "none — currency not assessed">
ASSUMED: <every assumption applied at STAGE-1, or "none — all inputs supplied">
AXES: outsourcing <NONE|LOW|MEDIUM|HIGH> · currency <CURRENT|PARTIAL|OBSOLETE|not assessed>
DECISION: <COMPLIANT | REVISE | REBUILD | FLAG>   [+ ESCALATE if a critical input was assumed]
─────────────────────────────────────────────
```

---

## COMPLIANT
```
DECISION: COMPLIANT
RESISTANCE MECHANISM: <the one mechanism that makes this hold — name it>
RULED UNDER: RULE-01 (LOW/NONE) [+ any consistency/verification rules passed]
```
One line. Confirm the mechanism (e.g. "live oral on an unseen prompt — outsourcing NONE"). Nothing else.

## REVISE
```
DECISION: REVISE
PROBLEM: <the exact fault, located — which instruction, which field, which policy line>
FIX [authenticity]: <the exact change — a named instruction, a new field, a policy rewrite>
FIX [modernise]:    <only if currency PARTIAL/OBSOLETE — the judgment-triad change>
PRESERVES: <what stays untouched: coverage, scenario, templates>
RULED UNDER: RULE-NN [, RULE-NN]
```
The fix is a **named change**, never "improve it." Include the `FIX [authenticity]` line only when Axis A fired, the `FIX [modernise]` line only when Axis B fired — a REVISE can carry one or both (RULE-31/32). When both fire, authenticity is listed first. If the fix is a policy rewrite, quote the drop-in (`ai-policy-patterns.md`); if it's a field, name the field.

### REVISE (modernise) — the currency-only case
When authenticity passes (outsourcing NONE/LOW) but currency is OBSOLETE/PARTIAL — the new signature output. PROBLEM names the obsolete workflow; the single `FIX [modernise]` line is the judgment triad (require AI → capture prompt → assess judgment over output). RULED UNDER: RULE-30, RULE-31 [, RULE-22/23/24].

## REBUILD
```
DECISION: REBUILD
WHY REBUILD > REVISE: <the structural reason a patch can't reach — evidence type wrong, or REVISE pile-up>
REPLACEMENT METHOD: <the recommended method that produces the right evidence>
PRESERVES: <coverage intent — what the replacement must still cover>
RULED UNDER: RULE-12 | RULE-20 | RULE-PILEUP [, …]
```

## FLAG
```
DECISION: FLAG
HUMAN MUST DECIDE: <the precise residual decision left to a person>
WHY RULING CAN'T CALL IT: <the structural reason it's outside operator authority>
OPERATOR HAS ALREADY: <everything done before the hand-off, so the human starts warm>
RULED UNDER: RULE-04 | RULE-05 | RULE-06 | RULE-07 | RULE-15 | RULE-21 | RULE-29 [, …]
```
FLAG is not a shrug. You do every operator move first, then hand back only the irreducibly human call.

## ESCALATE (decorator — sits on top of a real decision)
```
DECISION: REVISE + ESCALATE         (or COMPLIANT/REBUILD/FLAG + ESCALATE)
CRITICAL ASSUMPTION: <the missing input and the value you assumed>
WOULD FLIP TO: <the decision you'd reach under the other value>
DECISION STANDS UNDER ASSUMPTION — not bounced back.
... then the normal body for the underlying decision ...
```
The point of ESCALATE: the operator **still decides**. It states the assumption, states what would change the call, and delivers the ruling anyway.

### ESCALATE (no split) — currency not assessed
When no Warrant split was supplied and currency could have changed the decision (RULE-34):
```
DECISION: <COMPLIANT|REVISE...> + ESCALATE
CRITICAL ASSUMPTION: no Warrant split → currency not assessed, assumed CURRENT.
WOULD FLIP TO: REVISE (modernise) if the split marks this element INTEGRATE.
TO ASSESS CURRENCY: run Warrant on <unit> and supply the Resist/Integrate split.
DECISION STANDS UNDER ASSUMPTION — not bounced back.
```

---

## COMMIT (EXECUTE mode, appended after a REVISE/REBUILD that was applied)
```
COMMITTED — change pack: _ruling-change-packs/<task-id>/
APPLIED TO:  md ✓  ·  docx ✓ (re-parsed)  ·  html ✓ (regenerated, well-formed)   [or: html n/a — no Canvas render]
VERSION:     v<old> → v<new>
ROLLBACK:    restore from before/  (one step, reversible)
CHANGELOG:   <one line per file: what changed>
```
If any step failed: `COMMIT ABORTED — rolled back from before/ (T-67R). Downgraded to REVISE with manual instructions: <why>.`

---

## PACKAGE-mode add-ons (append after the per-task rulings)
**Coverage table** (STAGE-5):
```
COVERAGE SCAN
| Evidence requirement | Mapped to | Gap? |
|---|---|---|
| <PC/KE> | <task/part> | None / GAP → FLAG |
```
**Chain integrity** (if a task chain exists):
```
CHAIN: A → B → C   |  base task: <id>  |  base outsourcing: <score>  |  verdict: intact / FLAG chain (RULE-06)
```
**Verification scan**:
```
SECURE TASKS IN PACKAGE: <count>   |  ≥1 required.  0 → FLAG (RULE-04/16)
```
**Systemic check**:
```
TASKS FAILING: <n of N>.  Majority? → one FLAG (comprehensive review, RULE-07) instead of N REVISEs.
```

## House style
- Decision word in CAPS, alone. Action specific enough to drop in tomorrow. Rule IDs always. No "you might consider," no restating the task, no walls. If you assumed something, it's in the header — never buried.

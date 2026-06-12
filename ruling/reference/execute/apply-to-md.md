# Execute — Apply to Markdown (the source of truth)

Markdown is committed **first** and is authoritative: docx and html are regenerated from it (`apply-to-docx.md`, `apply-to-lms.md`), so they can't drift from the ruling. Edit the md precisely; everything else follows.

## Targets
- Assessment: `<unit>/06-output/<unit>-assessment-<n>-<type>.md`
- Learner guide (when the fix is a modernisation that changes what's taught): `<unit>/04-output/<unit>-learner-guide.md`

## Rules for the edit
1. **Apply exactly the FIX from the ruling — nothing more.** If the ruling says "convert Step 3 to the judgment triad and add the three template fields," edit Step 3 and add those fields. Do not improve prose elsewhere, do not touch other steps. The change pack's `diff-md.md` must read as *only* the ruled change.
2. **Preserve all placeholders verbatim:** `[BUYER_RTO_NAME]`, `[BUYER_RTO_NUMBER]`, `[BUYER_RTO_LOGO]`, `[DATE]`, `[SIGNATURE FIELD]`, the cover-sheet table, the unit summary. These are filled at deployment; never resolve or delete them.
3. **The modernise edit (RULE-31) is always the judgment triad:**
   - Rewrite the production instruction to **require** the AI tool (RULE-23).
   - Add the capture/judgment template fields (RULE-24): **AI Prompt Used** / **Problems Identified (≥2)** / **Corrections & Reasoning**.
   - Keep the original artifact (memo, plan, report) as the thing being *judged*, not the thing being *produced from scratch*.
4. **Reconcile the AI policy section** if the modernised task now requires AI where the policy forbade it (RULE-13): apply the two-tier block from `../ai-policy-patterns.md` — but only if the policy actually conflicts. (Some Learnbuilt packages already say "where a task includes AI as part of the work, the brief will say so" — in that case the modernised task is already permitted; note it, change nothing.)
5. **Bump the version** in the metadata table and any version line: `V1.0 → V1.1`.

## Verify
- `git diff`-style check: the only changes are the ruled ones (use the `before/` copy to diff).
- Placeholders still present (grep `[BUYER_RTO_` count unchanged).
- The triad fields exist and are empty (ready for a learner to fill).

Then proceed to `apply-to-docx.md`.

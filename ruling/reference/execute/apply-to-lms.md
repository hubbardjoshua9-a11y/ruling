# Execute — Apply to the LMS / Canvas render (regenerate from md)

The Canvas/LMS pages are **regenerated from the learner-guide markdown**, never hand-edited. This keeps what's *taught* (the Canvas pages) consistent with what's *assessed* (the modernised assessment) — the point of the full pipeline. Most assessments have no Canvas render; the LMS axis fires mainly when a **modernisation changed the learner guide** (so the teaching must follow).

## When the LMS step runs
- The decision was a **modernise REVISE** (RULE-31) whose Warrant `lg-modernisation` says a learner-guide section is now obsolete/needs-AI-context, **and** the unit renders a Canvas guide.
- If the unit has no Canvas render (e.g. CHCDIV001 has no `09-output/html/`, BSBWHS411's render is the monolithic site demo), record `html: n/a` in the change pack and skip — the md + docx commit still stands.

## Procedure
1. **Edit the learner-guide md** (`apply-to-md.md` already did this) — the section the `lg-modernisation` flagged, applying the proposed AI-augmented content. RESIST sections stay exactly as written.
2. **Regenerate the pages** with the unit's own build script:
   ```
   python <unit>/09-output/_build_html.py
   ```
   It reads `04-output/<unit>-learner-guide.md` and writes `09-output/html/*.html` (inline-styled, one page per section, Learnbuilt tokens preserved). Re-running it after the md edit is the entire LMS update.
3. **Copy the regenerated page(s)** that changed into the change pack's `after/` (and the matching `before/` page was captured at step 1 of the commit).

## Verify (RULE-36)
- The build script exits 0 and rewrites the pages.
- The changed page(s) are **well-formed** (parse the HTML; balanced tags) and still contain the Learnbuilt tokens (`[CANVAS_FILE_URL:...]`, `[LEARNBUILT_EMBLEM_CANVAS_URL]`, `[BUYER_RTO_NAME]`) — the build preserves them.
- The modernised teaching text is present in the regenerated page (grep a phrase from the new content).
- The same FIX concept now appears in **all three**: assessment md/docx (judged) + learner-guide html (taught).

Record the section + summary in `diff-lms.md`. If the build fails → T-67R rollback. This is the final commit step; then write `changelog.md` and emit the COMMIT block.

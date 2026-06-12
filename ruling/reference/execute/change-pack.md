# Execute — The Change Pack (STAGE-7 commit artifact)

A change pack is what a committed ruling leaves behind: an **auditable, reversible** record of exactly what changed, why, and how to undo it. No silent overwrite — an RTO must be able to see and reverse every edit Ruling makes to a validated tool. The change pack *is* the audit trail and the rollback.

## Where it lives
`<unit-workdir>/_ruling-change-packs/<task-id>/` — e.g. `worked-units/BSBTEC201/_ruling-change-packs/A2-step3-modernise/`.

## What it contains
```
_ruling-change-packs/<task-id>/
  ruling.md        ← the authorising STAGE-1..6 ruling (header, decision, FIX, rule IDs)
  changelog.md     ← one line per file changed: what, version bump, rule IDs
  before/          ← untouched copies of every target, captured BEFORE any edit (the rollback)
  after/           ← the edited/regenerated copies (what shipped)
  diff-md.md       ← human-readable before→after of the markdown change
  diff-lms.md      ← what changed in the Canvas/LMS render (section + summary)
  diff-docx.md     ← human-readable summary of the docx change (NOT raw XML)
```

## The procedure (STAGE-7, fixed order)
1. **Open the pack.** Create the directory; copy every target file (md, docx, html) into `before/` **before touching anything**. This copy is the rollback — do not skip it (the pipeline scripts' own `.bak` only writes once and won't refresh on re-run, so it is not authoritative).
2. **Write `ruling.md`** — paste the STAGE-1..6 ruling that authorises this commit.
3. **Apply in order md → docx → html** (see `apply-to-md.md`, `apply-to-docx.md`, `apply-to-lms.md`). Markdown is the single source of truth; docx and html are *regenerated from it*, so they cannot drift.
4. **Verify each** (see each apply file): md diff non-empty; docx re-unzips & parses; html well-formed; the same FIX visible in all three.
5. **Fill `after/` and the `diff-*.md` cards**, write `changelog.md`, and emit the COMMIT block (`../output-templates.md`).

## Rollback (T-67R)
Any step fails → copy everything from `before/` back over the targets, delete the half-written `after/`, and downgrade the output to **REVISE with manual instructions** stating what blocked the commit. A production file is never left half-edited.

## Version bump
In-content only: the assessment/learner-guide version (e.g. `V1.0 → V1.1`) in the metadata table + footer, recorded in `changelog.md`. Do **not** rename files (the filename cascades into Canvas `[CANVAS_FILE_URL]` refs and the delivery pack — out of scope for a task-level fix).

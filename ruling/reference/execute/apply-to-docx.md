# Execute — Apply to DOCX (regenerate from md; never hand-edit XML)

The `.docx` is **regenerated from the edited markdown**, not patched. This is how Learnbuilt actually builds it (Stage 08) and it guarantees the docx can't drift from the md. Claude runs the build tool via the shell — it never edits `word/document.xml` by hand (RULE-37).

> **What ships in this repo:** the reproducible docx path is **plain `pandoc`** (present: 3.9). The branded pipeline and the in-place patcher named below (`pipeline.py`, `brand_docx.py`, `apply_assessment_changes.py`) live in the separate Learnbuilt course-dev pipeline on the RTO side — they are *not* bundled here. Anyone with this repo + pandoc can reproduce the committed change pack.

## Primary path — plain pandoc (what this repo uses)
`pandoc <edited.md> -o <after>/<name>.docx`. Produces a correct, openable docx that carries the modernised content. This is the path that built every `.docx` in the committed change packs; note in `diff-docx.md` that full Learnbuilt branding (cover, footer, logo) is reapplied by the normal Stage-08 build on the RTO side.

## Production enhancement — the branded pipeline (RTO side, external)
On a machine with the Learnbuilt course-dev pipeline, the canonical builder `docx-formatter/pipeline.py` runs the same pandoc conversion against a reference template, then `brand_docx.py` applies Learnbuilt branding. Not required to reproduce the change pack; it only re-skins the same content.
```
python pipeline.py <unit>/06-output/<unit>-assessment-<n>-<type>.md \
  --unit-code <UNIT> --unit-title "<title>" \
  --doc-type assessment-<type> --assessment-num <n> --assessment-total <m> \
  --assessment-title "<title>" --output-dir <workdir>/after/
```

## Optional fallback — targeted in-place patch (external utility)
When regeneration isn't available, the existing 08-output docx can be patched in place via the Learnbuilt `apply_assessment_changes.py` pattern (zip→lxml→backup→rewrite): clone the answer-box table and insert it after the modernised step; generalise the policy-text replacement if a policy line must change. This is an in-place patch, not a rebuild, and relies on an external utility not shipped here.

## Verify (mandatory — RULE-36)
- The output `.docx` **re-unzips and parses**:
  ```python
  import zipfile, lxml.etree as ET
  z = zipfile.ZipFile(path); ET.fromstring(z.read('word/document.xml'))  # must not raise
  ```
- The modernised text is present in `word/document.xml` (grep for a phrase from the FIX).
- The file opens (size > before; no zip corruption).
- Record the result in `diff-docx.md` as a **human-readable** summary (what section gained which fields) — never paste raw XML.

If regeneration and both fallbacks fail → T-67R (roll back, downgrade to REVISE-with-manual-instructions). Then proceed to `apply-to-lms.md`.

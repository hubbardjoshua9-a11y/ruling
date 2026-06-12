# diff-docx.md — assessment .docx (human-readable summary)

The `.docx` is regenerated from the edited markdown, so its change mirrors `diff-md.md` exactly. Raw OOXML is not human-readable, so this is a summary; the file itself is in `after/`.

| | Before (`v1.0`) | After (`v1.1`) |
|---|---|---|
| Step 3 heading | "Prepare the welcome memo" | "Draft the welcome memo with AI, then evaluate and correct it" |
| Step 3 body | Manual: open template, prepare memo, save | AI-draft → record prompt → identify ≥2 problems → correct & justify |
| New table | — | **Template T2a**: AI prompt used / Problem 1 + correction / Problem 2 + correction |
| Version (cover + metadata) | V1.0 | V1.1 |

**Verification run (passed):**
- `word/document.xml` re-unzips and parses (lxml `fromstring`, no exception).
- Document text contains `Use an AI tool`, `Template T2a`, `Correction made`, `V1.1`.
- File size 18,397 bytes; opens as a valid Word document.

**Note on branding:** this regeneration used plain pandoc, which produces a valid, correctly-structured docx carrying the modernised content. Learnbuilt's Stage-08 brand pass (`docx-formatter/pipeline.py` → `brand_docx.py`: cover, footer, logo, table styling) is reapplied by the normal build on the RTO side; it is a presentation layer over this content, not part of the ruled change.

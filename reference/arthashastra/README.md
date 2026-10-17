# Arthashastra: raw extracted source bank

Stage 1 (extraction) of a pipeline: verify, review, fix, proofread come next. This folder holds the raw text, not a finished edition. Nothing here has been proofread.

Read, in order: FORMAT.md (file and line format), toc.md (structure), STATUS.md (what is done), sources.md (where text came from), ISSUES.md (known doubts).

Also here: id-map.tsv (every line ID with its original source label), editor-notes.tsv, raw/ (the SARIT XML) and tools/ (the scripts that made the text files).

Rules for anyone editing here:
- Text lines come only from sources listed in sources.md; never from memory.
- Do not rename files or change line IDs of finished chapters.
- Record every doubt in ISSUES.md; fix text only in a later, explicit proofreading stage.
- Run `python3 reference/tools/check_extraction.py reference/arthashastra` before every commit (3 errors are known: source typos with Latin letters, see ISSUES.md).
- Branch pattern: `docs/YYYY-MM-DD/version-N`; push new branches only; the owner merges.

How to continue: open STATUS.md. Extraction is complete for all 150 chapters; next are translations (none found yet) and the proofreading stage.

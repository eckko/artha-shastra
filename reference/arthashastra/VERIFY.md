# VERIFY log: arthashastra

Dated log of the verify-vedic-book-reference run. Append only.

## 2026-10-17 (branch docs/2026-10-17/version-1)
- Inventory: base = text/*.md (50 files, 5835 lines, Devanagari, `ID | text`). Owner confirmed: raw/kautalyarthasastra.xml is a raw copy (not used as text); id-map.tsv and editor-notes.tsv are ID helpers; reference/tools is the checker, not a book.
- Second edition: not available (owner answer), comparison skipped.
- Structure: 150/150 chapters, no flags; only number jump 14.03 85 -> 87. check_extraction: 3 known errors (Latin source typos).
- word_check: first run on text/ gave 4,148 stray hits that were all the kept compound dot, so it was re-run on a copy with `.` -> `-` (checks/ holds that run): stray 3, typo candidates 94, metre flags 3,584 (prose, ignored; metre.tsv filtered to the 66 stanza-line flags, full list in metre-all-lines.tsv).
- AI proofreading: 4 packs, 199 items, 15 proposals (checks/proposals.tsv, checks/PROOFREAD.md), sample error rate 1/37.
- Layer plan: 167 chunks, 5,398 units, about 1.8M draft output tokens plus about the same for review. Scope not yet chosen.

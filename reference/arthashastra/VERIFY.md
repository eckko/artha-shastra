# VERIFY log: arthashastra

Dated log of the verify-vedic-book-reference run. Append only.

## 2026-10-17 (branch docs/2026-10-17/version-1)
- Inventory: base = text/*.md (50 files, 5835 lines, Devanagari, `ID | text`). Owner confirmed: raw/kautalyarthasastra.xml is a raw copy (not used as text); id-map.tsv and editor-notes.tsv are ID helpers; reference/tools is the checker, not a book.
- Second edition: not available (owner answer), comparison skipped.
- Structure: 150/150 chapters, no flags; only number jump 14.03 85 -> 87. check_extraction: 3 known errors (Latin source typos).
- word_check: first run on text/ gave 4,148 stray hits that were all the kept compound dot, so it was re-run on a copy with `.` -> `-` (checks/ holds that run): stray 3, typo candidates 94, metre flags 3,584 (prose, ignored; metre.tsv filtered to the 66 stanza-line flags, full list in metre-all-lines.tsv).
- AI proofreading: 4 packs, 199 items, 15 proposals (checks/proposals.tsv, checks/PROOFREAD.md), sample error rate 1/37.
- Layer plan: 167 chunks, 5,398 units, about 1.8M draft output tokens plus about the same for review. Scope not yet chosen.
- Layer pilot Part 06 (2 chunks, 58 units): draft (Fable) -> check_chunk 0 errors -> independent review (Fable) -> apply (26 + 13 patches, 1 manual item left, see ISSUES.md) -> merge -> write_layers: text/p06-sandhi.md, p06-hindi.md, p06-english.md. check_extraction: layers align with the Sanskrit IDs; only the 3 known source-typo errors remain. These are reviewed AI drafts; no person has read them.
- Not run: Parts 01-05 and 07-15 (165 chunks, about 3.6M tokens with review). Awaiting the owner's decision.

## 2026-10-17, second layer run: short parts 08, 10, 11, 12 (19 chunks, 678 units, same branch)
- Same pipeline as the pilot: draft (Fable) -> check_chunk (0 errors each) -> independent review (Fable, one per chunk) -> apply_review --add-source (patches applied without failures) -> merge_chunks -> write_layers -> work_status refresh. GLOSSARY.md was extended by the reviewers.
- Written: text/p08-, p10-, p11-, p12- `-sandhi.md`, `-hindi.md`, `-english.md`. check_extraction: layers align with the Sanskrit IDs; only the 3 known source-typo errors remain.
- Reviewers' common finding: drafts put bracketed glosses inside the Hindi (forbidden by the brief); these were removed by the review patches. Open items needing a person are in ISSUES.md.
- Layers done: Parts 06, 08, 10, 11, 12. Not run: Parts 01-05, 07, 09, 13-15.

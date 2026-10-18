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

## 2026-10-17, third layer run: Parts 13, 14, 15 (13 chunks, 475 units, branch docs/2026-10-17/version-2)
- The owner merged docs/2026-10-17/version-1 into main (PR #1) during the run, so the rest was continued on a new branch, docs/2026-10-17/version-2 (main untouched).
- Same pipeline with Sonnet 5.5 agents for drafting and review (drafts told not to put bracketed glosses in Hindi). All patches applied without failure. Hand edit: 13.5.2 duplicated `ca` in the word split removed.
- Written: text/p13-, p14-, p15- `-sandhi.md`, `-hindi.md`, `-english.md`. check_extraction: layers align with the Sanskrit IDs; only the 3 known source-typo errors remain.
- Layers done: Parts 06, 08, 10, 11, 12, 13, 14, 15. Not run: Parts 01-05, 07, 09 (large).

## 2026-10-17, fourth layer run: Parts 05, 09, 04 (30 chunks, 1,010 units, branch docs/2026-10-17/version-2)
- Same pipeline as the third run (Sonnet 5.5 agents for drafting and an independent review per chunk). All patches applied without failure; reviews found mostly Hindi wording, unmarked additions, glossary alignment and closing `iti` rendered as "thus".
- Hand edits (the patch ops cannot add or remove flags or words): added or corrected text_flags in 5.1.55, 5.2.57, 5.4.10, 5.5.7, 5.6.9/28/31, 9.1.15 (moved a stray `ca`), 9.4.8/16/25, 9.5.4, 9.6.21/29, 4.1.10, 4.5.5, 4.6.18, 4.7.2, 4.9.9, 4.11.14; removed a false-positive flag in 5.3.6.
- Written: text/p04-, p05-, p09- `-sandhi.md`, `-hindi.md`, `-english.md`. check_extraction: layers align with the Sanskrit IDs; only the 3 known source-typo errors remain.
- Layers done: Parts 04, 05, 06, 08, 09, 10, 11, 12, 13, 14, 15. Not run: Parts 01, 02, 03, 07 (about 3,200 verses; waiting for the owner's decision). Open items needing a person are in ISSUES.md.

## 2026-10-18, fifth layer run: Part 03 (20 chunks, 699 units, branch docs/2026-10-17/version-3)
- Branch docs/2026-10-17/version-3 was started from main after the owner merged PR #4. The first batch of Sonnet 5.5 draft agents was interrupted before writing anything and was relaunched.
- Same pipeline (Sonnet 5.5 drafts, an independent review per chunk, apply_review, hand edits, merge, write_layers). All patches applied without failure; check_chunk 0 errors for every chapter.
- Hand edits: split compounds merged into one entry in 3.7 (31 tokens); added or fixed text_flags in 3.5, 3.7, 3.8, 3.1, 3.2, 3.3, 3.11, 3.15, 3.19; removed false flags in 3.9, 3.11, 3.17, 3.19, 3.20; split 3.1.13 mattena.unmattena-avagṛhītena and 3.14.3 tasya.vyaya.karmaṇā; duplicate w fixed in 3.17.
- Written: text/p03-sandhi.md, p03-hindi.md, p03-english.md. check_extraction: layers align with the Sanskrit IDs; only the 3 known source-typo errors remain.
- Layers done: Parts 03, 04, 05, 06, 08, 09, 10, 11, 12, 13, 14, 15. Not run: Parts 01, 02, 07. These are reviewed AI drafts; no person has read them.

2026-10-18, sixth layer run: Part 07 (19 chunks, 687 units, 18 chapters)
- Same pipeline (Sonnet 5.5 drafts, an independent Sonnet 5.5 review per chunk, apply_review, hand edits, merge, write_layers). All patches applied without failure; check_chunk 0 errors for every chunk.
- Hand edits: removed false flags for the e-text 'dd h' spelling, h-for-visarga and samyoga (7.3, 7.7, 7.10, 7.13, 7.14, 7.18); added flags in 7.9.36 (alpa.prayasatā), 7.10.14, 7.11.8; merged mahad.upakurvan in 7.9.13; moved atha in 7.9.43; fixed glosses of identical word entries (7.9.50, 7.10.23, 7.11.23, 7.11.43); joined hard line breaks in the English and Hindi of 7.1.32.
- Written: text/p07-sandhi.md, p07-hindi.md, p07-english.md. check_extraction: layers align with the Sanskrit IDs; only the 3 known source-typo errors remain.
- Layers done: Parts 03 to 15. Not run: Parts 01 and 02. Reviewed AI drafts; no person has read them.

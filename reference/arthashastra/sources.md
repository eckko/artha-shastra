# Sources: arthashastra

| ID | Name | URL | Edition / editor / year | Script | Licence | Covers | Fetched how | Quality note | Role |
|---|---|---|---|---|---|---|---|---|---|
| S1 | SARIT: Kauṭalya, Arthaśāstra (Kyoto digital version) | https://sarit.indology.info/kautalyarthasastra.xml ; GitHub mirror https://github.com/sarit/sarit-corpus (file kautalyarthasastra.xml) | R. P. Kangle critical edition (Bombay 1960, 2nd ed. 1969); typed by Muneo Tokunaga et al., Kyoto 1993; TEI by Richard Mahoney; SARIT version 0.1_005 | IAST (with compound dots) | CC BY-SA 3.0 (SARIT; Kyoto Joint Seminar copyright notice in the file) | all 15 books, 150 chapters | git clone of sarit/sarit-corpus (shell reaches GitHub only); copied to raw/ ; sha256 9eed724dd0bc803e9d32fb8032aa432c352f53d0bb5355fb22a8767d7415e1d2 | complete; a few label and letter typos (see ISSUES.md) | primary |

Searched and not used:
- GRETIL (gretil.sub.uni-goettingen.de), Sanskrit Documents, Sanskrit Wikisource, SARIT website: refused by the shell's network allowlist; GitHub gave S1 anyway.
- Translations: no verse-aligned Hindi or English text found that the shell can reach (Kangle's 1963 translation is in copyright; Shamasastry 1915 is paragraph-based on archive.org/Wikisource, blocked). No translation files were written. If you download a translation, attach it and a later pass can align it to the IDs.

Conversion notes:
- Script: tools/parse_sarit.py (TEI to structure), tools/build_text.py (IAST to Devanagari with indic_transliteration 2.3.82, NFC). Re-run: `python3 -I tools/build_text.py raw/kautalyarthasastra.xml .`
- Part and chapter in each ID come from the TEI division positions, not from the typed labels (which have typos). Verse number comes from the label.
- Compound dots, hyphens, doubt marks "(...?)" and quote marks kept as in the e-text (owner's decision, 2026-10-17). Avagraha ' became ऽ. Trailing verse numbers removed.
- The TEI also holds Kangle translation page references (margin notes), 80 editor footnotes ('ś', in editor-notes.tsv) and a transcript appendix; none of these are in the text files.

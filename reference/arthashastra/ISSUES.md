# Issues: arthashastra

| Line ID | Kind | What | Source(s) | Suggested check |
|---|---|---|---|---|
| 01.01.0 | numbering | Invocation line before KAZ01.1.01 has no label in the source; given verse number 0 | S1 | keep ID; confirm against print edition |
| 02.22.08 | possible-typo | label written 'KAZO2.22.08' in source | S1 | label only; text taken by position |
| 02.22.09 | possible-typo | label written 'KAZO2.22.09' in source | S1 | label only; text taken by position |
| 02.22.10 | possible-typo | label written 'KAZO2.22.10' in source | S1 | label only; text taken by position |
| 02.22.11 | possible-typo | label written 'KAZO2.22.11' in source | S1 | label only; text taken by position |
| 02.22.12 | possible-typo | label written 'KAZO2.22.12' in source | S1 | label only; text taken by position |
| 02.24.16 | possible-typo | label written 'KAZO2.24.16' in source | S1 | label only; text taken by position |
| 02.24.17 | possible-typo | label written 'KAZU2.24.17' in source | S1 | label only; text taken by position |
| 02.24.18 | possible-typo | label written 'KAZU2.24.18' in source | S1 | label only; text taken by position |
| 02.24.19 | possible-typo | label written 'KAZU2.24.19' in source | S1 | label only; text taken by position |
| 02.24.20 | possible-typo | label written 'KAZU2.24.20' in source | S1 | label only; text taken by position |
| 05.01.46 | numbering | label 'KAZ04.4.46' disagrees with position | S1 | label only; text taken by position |
| 07.13.30 | possible-typo | label written 'Kaz07.13.30' in source | S1 | label only; text taken by position |
| 13.02.45 | possible-typo | label written 'KAZ13.2.45cd' in source | S1 | label only; text taken by position |
| 14.03.86 | missing | verse number 86 is absent in S1 (85 and 87 follow each other) | S1 | check Kangle p. for 14.3.86 |
| 02.05.21 | possible-typo | source reads puruWa (W is not IAST); left as in source, shown as पुरुWअ | S1 | likely puruṣa; check print |
| 02.29.43 | possible-typo | source reads lavanAm (A is not IAST); left as in source, shown as लवन्Aम् | S1 | likely lavaṇam; check print |
| 04.12.35 | other | editor's note 'cf. N12.60' sits inside the line; Latin letters left as in source | S1 | N12.60 = a cross-reference to KAZ 12.? by the Kyoto editors |
| all | other | Compound dots (.), joining hyphens (-), the Kyoto doubt marks '(...?)' and straight quote marks are kept as in the e-text. At about 5,000 vowel junctions the e-text does not apply sandhi (pūrva.ācāryaiḥ for print pūrvācāryaiḥ) | S1 | decide in the proofreading stage |
| all | numbering | Half-verse labels ab / cd / ef in the source are lettered a / b / c by position (FORMAT.md allows one letter); id-map.tsv has every original label | S1 | none |
| all | other | 80 verse lines carry an editor footnote 'ś' in the source (list in editor-notes.tsv); its meaning is not explained in the e-text | S1 | check Kangle's introduction |
| all | count | Verse numbers extracted 5398 and 5835 lines; the text (1.1.18) counts 6000 ślokas of 32 syllables, which is not the same unit | S1 | none |

## Verify stage 2026-10-17 (checks/, proposals only; text/ unchanged)

Checks that ran: structure_check, check_extraction, word_check (on a copy with `.` swapped for `-`, because the tool does not split on the compound dot), AI proofreading of 199 flagged and sample lines. Second edition: not available, skipped.

| Line ID | Kind | What | Source(s) | Suggested check |
|---|---|---|---|---|
| 02.05.21 | possible-typo | AI proposal: puruWa = पुरुष (stray W) | S1 | check print |
| 02.29.43 | possible-typo | AI proposal: लवन्Aम् = लवणम् (stray A) | S1 | check print |
| 02.23.19b | possible-typo | AI proposal: करयेत् -> कारयेत् | S1 | check print |
| 08.04.16 | possible-typo | AI proposal: प्रकृइति -> प्रकृति | S1 | check print |
| 02.22.8 | possible-typo | AI proposal: स्थापय्तेत् -> स्थापयेत् | S1 | check print |
| 02.27.19 | possible-typo | AI proposal: लभेएत -> लभेत | S1 | check print |
| 03.16.39 | possible-typo | AI proposal: पाषढाः -> पाषण्डाः | S1 | check print |
| 13.04.3 | possible-typo | AI proposal: निवेषयेत् -> निवेशयेत् | S1 | check print |
| 02.22.15b | possible-typo | AI proposal: शुक्लम् -> शुल्कम् | S1 | check print |
| 06.02.22 | possible-typo | AI proposal: मध्यानां -> मध्यमानां (dropped म) | S1 | check print |
| 01.10.3 | variant | AI note: अधार्मिको अयं lacks the avagraha used elsewhere (ऽयं) | S1 | check print |
| 01.20.21 | possible-typo | AI proposal: stray comma before the final danda | S1 | check print |
| 02.10.42b | possible-typo | AI proposal: नृप्तेर् -> नृपतेर् | S1 | check print |
| 12.05.51a | possible-typo | AI proposal: द्वाह्स्थान् -> द्वाःस्थान् | S1 | check print |
| 04.04.3 | possible-typo | AI proposal: line-break leftover splits the word (शौण्डि- क.आपूपिक) | S1 | check print |
| 02.12.22 | possible-typo | noticed by a proofreader in neighbouring context, not flagged by the checker: आअकरं | S1 | check print |
| 02.28.26 | possible-typo | noticed likewise: नाव्.अध्ह्यक्षो (अध्यक्षो) | S1 | check print |
| all | other | Checker limits: the typo detector does not see errors that form another valid word, so the two context finds above suggest more exist. Metre flags on prose lines were ignored; only the 66 flagged stanza lines (ab/cd/ef) were read, and the AI judged almost all regular once the unsandhied marks are read with sandhi | | |

Coverage and rate: 199 lines read by AI (3 stray, 93 typo candidates, 66 metre, 37 sample); 15 proposals; the sample of 37 ordinary lines had 1 error (2.7%, a small sample). Nothing was proofread by a person.

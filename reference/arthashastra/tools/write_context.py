#!/usr/bin/env python3
"""Write ISSUES.md, STATUS.md and editor-notes.tsv from the raw XML and the
finished text files. Usage: write_context.py RAW_XML BOOK_DIR"""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from analyze import analyse  # noqa: E402

RAW, BOOK = sys.argv[1], Path(sys.argv[2])
books, verses, problems = analyse(RAW)
idmap = dict(line.split("\t")[::-1] for line in
             (BOOK / "id-map.tsv").read_text(encoding="utf8").splitlines()[1:])
# source label (stripped) -> ID
by_label = {k.strip(): v for k, v in idmap.items()}

NS = "{http://www.tei-c.org/ns/1.0}"
body = ET.parse(RAW).getroot().find(f".//{NS}body")
notes = []
for note in body.iter(NS + "note"):
    if note.get("place") == "bottom":
        refs = ["".join(r.itertext()).strip() for r in note.findall(NS + "ref")]
        notes.append((by_label.get(refs[0], "?"), refs[0], refs[1]))
(BOOK / "editor-notes.tsv").write_text(
    "ID\tsource label\teditor note\n" + "\n".join("\t".join(n) for n in notes)
    + "\n", encoding="utf8")

rows = []
add = lambda i, k, w, s, c: rows.append(f"| {i} | {k} | {w} | {s} | {c} |")
add("01.01.0", "numbering",
    "Invocation line before KAZ01.1.01 has no label in the source; given verse number 0",
    "S1", "keep ID; confirm against print edition")
for ident, kind, what in problems:
    if kind == "possible-typo" and "KAZ0" in what and "O2" not in what \
            and "U2" not in what and "Kaz" not in what:
        continue  # only a missing space after the label
    if kind == "numbering" and ident == "01.01.0":
        continue
    add(ident, kind, what, "S1", "label only; text taken by position")
add("14.03.86", "missing", "verse number 86 is absent in S1 (85 and 87 follow each other)", "S1", "check Kangle p. for 14.3.86")
add("02.05.21", "possible-typo", "source reads puruWa (W is not IAST); left as in source, shown as पुरुWअ", "S1", "likely puruṣa; check print")
add("02.29.43", "possible-typo", "source reads lavanAm (A is not IAST); left as in source, shown as लवन्Aम्", "S1", "likely lavaṇam; check print")
add("04.12.35", "other", "editor's note 'cf. N12.60' sits inside the line; Latin letters left as in source", "S1", "N12.60 = a cross-reference to KAZ 12.? by the Kyoto editors")
add("all", "other", "Compound dots (.), joining hyphens (-), the Kyoto doubt marks '(...?)' and straight quote marks are kept as in the e-text. At about 5,000 vowel junctions the e-text does not apply sandhi (pūrva.ācāryaiḥ for print pūrvācāryaiḥ)", "S1", "decide in the proofreading stage")
add("all", "numbering", "Half-verse labels ab / cd / ef in the source are lettered a / b / c by position (FORMAT.md allows one letter); id-map.tsv has every original label", "S1", "none")
add("all", "other", f"{len(notes)} verse lines carry an editor footnote 'ś' in the source (list in editor-notes.tsv); its meaning is not explained in the e-text", "S1", "check Kangle's introduction")
add("all", "count", "Verse numbers extracted 5398 and 5835 lines; the text (1.1.18) counts 6000 ślokas of 32 syllables, which is not the same unit", "S1", "none")
(BOOK / "ISSUES.md").write_text(
    "# Issues: arthashastra\n\n| Line ID | Kind | What | Source(s) | Suggested check |\n"
    "|---|---|---|---|---|\n" + "\n".join(rows) + "\n", encoding="utf8")

status = ["# Status: arthashastra", "",
          "Updated: 2026-10-17 on branch docs/2026-10-17/version-1. Base source: S1.", "",
          "| Part | Chapter | Sanskrit lines | Source | Hindi | English | Check | Notes |",
          "|---|---|---|---|---|---|---|---|"]
fail = {"02.05": "3 known source typo (see ISSUES)", "02.29": "3 known source typo (see ISSUES)",
        "04.12": "3 known source typo (see ISSUES)"}
for bk in books:
    for ch in bk["chapters"]:
        key = f"{bk['n']:02d}.{ch['n']:02d}"
        check = "Latin letters (source typo)" if key in fail else "pass"
        note = "invocation line is 01.01.0" if key == "01.01" else (
            "verse 86 missing in source" if key == "14.03" else "")
        status.append(f"| {bk['n']:02d} | {ch['n']:02d} | {len(ch['items'])} | S1 | -- | -- | {check} | {note} |")
status += ["", "## Next",
           "- Hindi and English: no verse-aligned translation was found that the shell can reach; none written. See sources.md.",
           "- Proofreading stage: compare against Kangle's print edition, resolve ISSUES.md, decide on compound marks."]
(BOOK / "STATUS.md").write_text("\n".join(status) + "\n", encoding="utf8")
print("issues", len(rows), "notes", len(notes))

#!/usr/bin/env python3
"""Convert the parsed SARIT Arthashastra into FORMAT.md text files.

Usage: build_text.py RAW_XML BOOK_DIR

Rules (decided with the owner):
- IAST to Devanagari by indic_transliteration; nothing else is changed.
- Compound dots, hyphens, the e-text's doubt marks "(...?)" and its quote
  marks are kept as in the e-text.
- Trailing verse numbers ("| 3 |", "|| 19 ||") are removed; the closing
  danda is kept.
- Latin letters that are not IAST (source typos W, A, N and the editor's
  "cf. N12.60") are left exactly as in the source and logged.
- Half-verse source labels ab / cd / ef become line letters a / b / c by
  position; id-map.tsv records each ID's original source label.
"""
import re
import sys
import unicodedata
from collections import OrderedDict, defaultdict
from pathlib import Path

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from analyze import analyse  # noqa: E402
from parse_sarit import LABEL  # noqa: E402
from indic_transliteration import sanscript as S  # noqa: E402

RAW, BOOK = sys.argv[1], Path(sys.argv[2])
books, verses, problems = analyse(RAW)

PROTECT = {}


def protect(match):
    key = chr(0xE000 + len(PROTECT))
    PROTECT[key] = match.group(0)
    return key


def to_deva(text):
    """One line of IAST to Devanagari with the owner's rules."""
    PROTECT.clear()
    text = re.sub(r"cf\. N12\.60", protect, text)
    text = re.sub(r"[WAN]", protect, text)
    # trailing verse number: "| 12 |" -> "|" ; "|| 19 ||" -> "||"
    text = re.sub(r"(\|\|?)\s*\d+\s*\1\s*$", r"\1", text)
    out = S.transliterate(text, S.IAST, S.DEVANAGARI)
    for key, original in PROTECT.items():
        out = out.replace(key, original)
    out = re.sub(r"\s+", " ", out).strip()
    out = unicodedata.normalize("NFC", out)
    return out


def line_ids(b, c, items):
    """IDs for the lines of one chapter plus the source label of each."""
    groups = defaultdict(list)
    keyed = []
    for lab, text, kind in items:
        if lab is None:
            verse, src = 0, "(unlabelled)"
        else:
            m = LABEL.match(lab)
            verse, src = int(m.group(3)), lab.strip()
        groups[verse].append(len(keyed))
        keyed.append([verse, src, text])
    rows, seen = [], {}
    for index, (verse, src, text) in enumerate(keyed):
        members = groups[verse]
        letter = ("" if len(members) == 1
                  else "abcdefghijklmnopqrstuvwxyz"[members.index(index)])
        ident = f"{b:02d}.{c:02d}.{verse}{letter}"
        assert ident not in seen, ident
        seen[ident] = True
        rows.append((ident, src, to_deva(text), text))
    return rows


text_dir = BOOK / "text"
text_dir.mkdir(parents=True, exist_ok=True)
idmap, latin, counts = [], [], {}
for bk in books:
    n = bk["n"]
    lines_total = sum(len(c["items"]) for c in bk["chapters"])
    whole_part = lines_total < 1000
    part_lines = []
    for ch in bk["chapters"]:
        rows = line_ids(n, ch["n"], ch["items"])
        counts[(n, ch["n"])] = len({r[0].rsplit(".", 1)[1].rstrip("abcdefghijklmnopqrstuvwxyz")
                                    for r in rows})
        chapter_lines = []
        for ident, src, dev, original in rows:
            chapter_lines.append(f"{ident} | {dev}")
            idmap.append(f"{ident}\t{src}")
            if re.search(r"[A-Za-z]", dev):
                latin.append((ident, re.findall(r"\S*[A-Za-z]\S*", dev)))
        if whole_part:
            part_lines += chapter_lines
        else:
            name = f"ch{n:02d}.{ch['n']:02d}.md"
            (text_dir / name).write_text("\n".join(chapter_lines) + "\n",
                                         encoding="utf8", newline="\n")
    if whole_part:
        (text_dir / f"p{n:02d}.md").write_text("\n".join(part_lines) + "\n",
                                               encoding="utf8", newline="\n")
(BOOK / "id-map.tsv").write_text("ID\tsource label\n" + "\n".join(idmap) + "\n",
                                 encoding="utf8", newline="\n")
print("files", len(list(text_dir.glob("*.md"))), "lines", len(idmap))
print("latin letters left:")
for item in latin:
    print(" ", item)

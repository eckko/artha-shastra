#!/usr/bin/env python3
"""Write toc.md from the parsed SARIT file. Usage: build_toc.py RAW TOC [--marks keep|drop]"""
import re
import sys
import unicodedata

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from analyze import analyse  # noqa: E402
from indic_transliteration import sanscript as S  # noqa: E402

KEEP_MARKS = "--marks=keep" in sys.argv
RAW, TOC = sys.argv[1], sys.argv[2]
books, verses, problems = analyse(RAW)


def deva(text):
    if not KEEP_MARKS:
        text = text.replace(".", "")
    return unicodedata.normalize(
        "NFC", S.transliterate(text, S.IAST, S.DEVANAGARI))


# Book names as the text's own list in 1.1.3-17 closes each group.
first = " ".join(t for lab, t, k in books[0]["chapters"][0]["items"]
                 if lab and re.search(r"1\.1\.(0[3-9]|1[0-7])", lab))
closers = re.findall(
    r"-\s*,?\s*(?:iti|ity),?\s+(.*?)\s+\S+\s+adhikaraṇam", first)
assert len(closers) == 15, len(closers)

COUNT = {  # lines per book decide part file or chapter files
    b["n"]: sum(len(c["items"]) for c in b["chapters"]) for b in books}
VERSES = {k: len(v) for k, v in verses.items()}
total_verses = sum(VERSES.values())
out = []
out.append("# Arthashastra (कौटिलीय अर्थशास्त्र)\n")
out.append("- Author / compiler: Kauṭalya (Kauṭilya), Indian statecraft tradition")
out.append("- Subject and purpose of the book: statecraft, administration, law, "
           "foreign policy and war; the text itself says it was composed by "
           "gathering the earlier teachers' arthaśāstras into one (1.1.1) "
           "and that it is easy to grasp and clear in meaning (1.1.19)")
out.append("- Base edition: R. P. Kangle, *The Kauṭilīya Arthaśāstra*, Part I "
           "critical edition, Bombay 1960 (2nd ed. 1969), as typed by Muneo "
           "Tokunaga et al. (Kyoto 1993) and encoded by SARIT "
           "(source S1 in sources.md)")
out.append("- Mapping: part = adhikaraṇa (book), chapter = adhyāya, "
           "verse = sūtra (prose) or śloka (verse) as numbered in the edition")
out.append(f"- Totals: 15 parts, 150 chapters, {total_verses} verse numbers "
           f"(5835 lines) in the draft count; traditional (text 1.1.18): "
           "15 adhikaraṇas, 150 adhyāyas, 180 prakaraṇas, 6000 ślokas "
           "(the 6000 are ślokas of 32 syllables, so not comparable to "
           "the edition's sūtra numbers)")
out.append("- Chapter names: the e-text carries only the editor's English "
           "headings (from Kangle's translation). The Sanskrit prakaraṇa "
           "list in 1.1.3-17 yields 175 names for 180 sections, so it cannot "
           "be mapped to chapters one-to-one; chapter Sanskrit names are "
           "left empty (—) rather than guessed.\n")
for i, bk in enumerate(books):
    n = bk["n"]
    title = re.sub(r"^Book \d+:\s*", "", bk["head"])
    out.append(f"## Part {n:02d}: {deva(closers[i])} ({title})\n")
    out.append(f"Purpose: {title} (source: e-text heading; Sanskrit name from "
               f"the closing words of the group in 1.1.3-17)\n")
    out.append("| Part | Chapter | Sanskrit name | English name | Purpose | "
               "Verses (extracted) | Verses (traditional) | File | Status |")
    out.append("|---|---|---|---|---|---|---|---|---|")
    for ch in bk["chapters"]:
        head = re.sub(r"\s+", " ", ch["head"])
        m = re.match(r"Chapter \d+(?: \((Sections?) ([\d; ]+)\))?: (.*)$", head)
        name = m.group(3)
        purpose = (f"{m.group(1)} {m.group(2)} (Kangle's numbering, per "
                   "e-text heading)" if m.group(1) else
                   "Opening of the book (per e-text heading)")
        f = (f"text/p{n:02d}.md" if COUNT[n] < 1000
             else f"text/ch{n:02d}.{ch['n']:02d}.md")
        v = VERSES[(n, ch["n"])]
        out.append(f"| {n:02d} | {ch['n']:02d} | — | {name} | {purpose} | "
                   f"{v} | — | {f} | extracted |")
    out.append("")
open(TOC, "w", encoding="utf8").write("\n".join(out))
print("written", TOC, total_verses)

#!/usr/bin/env python3
"""Dry-run analysis of the parsed SARIT Arthashastra: ID mapping, numbering
checks, per-book line counts. Used to build toc.md."""
import re
import sys
from collections import OrderedDict, defaultdict

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from parse_sarit import parse, LABEL  # noqa: E402


def entries(books):
    """Yield (book, chapter, label, text, kind) with label normalised."""
    for bk in books:
        for ch in bk["chapters"]:
            for lab, text, kind in ch["items"]:
                yield bk["n"], ch["n"], lab, text, kind


def analyse(path):
    books = parse(path)
    problems = []
    verses = defaultdict(OrderedDict)   # (b, c) -> {verse: [suffixes]}
    for b, c, lab, text, kind in entries(books):
        if lab is None:
            verses[(b, c)].setdefault(0, []).append("")
            problems.append((f"{b:02d}.{c:02d}.0", "numbering",
                             "unlabelled invocation line before KAZ01.1.01"))
            continue
        m = LABEL.match(lab)
        if not m:
            problems.append((f"{b:02d}.{c:02d}", "other",
                             f"label not recognised: {lab!r}"))
            continue
        lb = m.group(1).replace("O", "0").replace("U", "0")
        prefix = lab.strip()[:3]
        if prefix != "KAZ" or "O" in m.group(1) or "U" in m.group(1) \
                or lab != lab.rstrip() + " " and not lab.endswith(" "):
            problems.append((f"{b:02d}.{c:02d}.{m.group(3)}", "possible-typo",
                             f"label written {lab.strip()!r} in source"))
        if int(lb) != b or int(m.group(2)) != c:
            problems.append((f"{b:02d}.{c:02d}.{m.group(3)}", "numbering",
                             f"label {lab.strip()!r} disagrees with position"))
        verses[(b, c)].setdefault(int(m.group(3)), []).append(m.group(4))
    return books, verses, problems


if __name__ == "__main__":
    books, verses, problems = analyse(sys.argv[1])
    tot_lines = tot_verses = 0
    for bk in books:
        lines = sum(len(c["items"]) for c in bk["chapters"])
        vs = sum(len(verses[(bk["n"], c["n"])]) for c in bk["chapters"])
        tot_lines += lines
        tot_verses += vs
        print(f"book {bk['n']:>2}: chapters {len(bk['chapters']):>2} "
              f"lines {lines:>4} verses {vs:>4}")
    print("total lines", tot_lines, "verses", tot_verses)
    gaps = []
    for (b, c), v in verses.items():
        nums = [n for n in v if n]
        for i in range(1, max(nums) + 1):
            if i not in v:
                gaps.append((b, c, i))
    print("gaps in verse numbers:", gaps[:40], len(gaps))
    order = []
    for (b, c), v in verses.items():
        nums = list(v)
        if nums != sorted(nums):
            order.append((b, c))
    print("out-of-order chapters:", order)
    for p in problems:
        print(p)

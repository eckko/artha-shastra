#!/usr/bin/env python3
"""Parse raw/kautalyarthasastra.xml (SARIT TEI, Kangle edition) into a
structure: books -> chapters -> entries. No text is altered here; the
conversion to Devanagari is done in build_text.py."""
import re
import sys
import xml.etree.ElementTree as ET

NS = "{http://www.tei-c.org/ns/1.0}"
LABEL = re.compile(r"^\s*(?i:kaz)\s*([0-9OU]\d)\.(\d+)\.(\d+)([a-z]*)\s*$")


def whole(el):
    """All text of an element, whitespace folded, labels excluded."""
    parts = [el.text or ""]
    for child in el:
        if child.tag not in (NS + "label", NS + "note"):
            parts.append(whole(child))
        parts.append(child.tail or "")
    return re.sub(r"\s+", " ", "".join(parts)).strip()


def label_of(el):
    lab = el.find(NS + "label")
    return None if lab is None else "".join(lab.itertext())


def parse(path):
    root = ET.parse(path).getroot()
    body = root.find(f".//{NS}body")
    books = []
    for book in body.findall(NS + "div"):
        if book.get("type") != "book":
            continue
        entry = {"n": int(book.get("n")),
                 "head": re.sub(r"\s+", " ", book.find(NS + "head").text).strip(),
                 "chapters": []}
        for chap in book.findall(NS + "div"):
            if chap.get("type") != "chapter":
                continue
            items = []
            for el in chap:
                tag = el.tag.replace(NS, "")
                if tag == "p":
                    items.append((label_of(el), whole(el), "p"))
                elif tag == "lg":
                    for line in el.findall(NS + "l"):
                        items.append((label_of(line), whole(line), "l"))
                elif tag not in ("head", "note", "pb"):
                    raise SystemExit(f"unexpected element {tag}")
            entry["chapters"].append({
                "n": int(chap.get("n")),
                "head": re.sub(r"\s+", " ", chap.find(NS + "head").text).strip(),
                "items": items})
        books.append(entry)
    return books


if __name__ == "__main__":
    books = parse(sys.argv[1])
    for b in books:
        print(f"BOOK {b['n']}: {b['head']}  chapters={len(b['chapters'])}")
        for c in b["chapters"]:
            print(f"  {c['n']:>2} items={len(c['items']):>3}  {c['head']}")

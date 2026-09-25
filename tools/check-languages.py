#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify that every manual is identical across all eight language versions.

Rule 1 in CLAUDE.md says each manual exists as EN, DE, FR, ES, NL, RU, JP and CN,
and that the versions must not drift apart. This script checks that mechanically:

  completeness  every manual has all eight language files
  structure     same number of headings, table rows and checkboxes in each
  data          every multi-digit number appears equally often in all eight

Numbers are normalised before comparing, because the languages write them
differently — EN 25,000 · DE 25.000 · FR 25 000 · RU 14 842 are the same value.
A comma or period *followed by a space* is a list separator, never a thousands
separator: "0:00, 6:00" is two times of day, not the number 006. The text is cut
at those, and with a newline rather than a space, since Russian already uses a
plain space as its thousands separator.

Single-digit values count too — "5 hits" and "3 stars" are data. The one
exception is JP and CN: those write a numeral where English writes a word
("3つの" for "three"), so a single-digit-only difference against JP or CN is
reported as a note to read rather than as a failure. Run with -v to see them.

Usage:
    python3 tools/check-languages.py            # check the whole repo
    python3 tools/check-languages.py -v         # also list single-digit diffs
    python3 tools/check-languages.py events/    # check one area only

Exits 0 when everything matches and 1 otherwise, so it can be used in a
pre-commit hook or CI step.
"""

import collections
import io
import os
import re
import sys

LANGS = ("EN", "DE", "FR", "ES", "NL", "RU", "JP", "CN")
# CJK writes numerals where English writes number words, so a single-digit-only
# difference against these two is wording noise rather than a wrong value.
NUMERAL_WORD_LANGS = ("JP", "CN")
FILENAME = re.compile(r"(.*)_(%s)\.md$" % "|".join(LANGS))

# Separators that may appear *inside* one number across the eight languages:
# period (DE), comma (EN), plain space (RU), narrow and non-breaking space (FR).
IN_NUMBER = ".,   "


def collect(root):
    """Map every manual slug to {language code: path}."""
    manuals = collections.defaultdict(dict)
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for name in filenames:
            match = FILENAME.match(name)
            if match:
                slug = os.path.join(dirpath, match.group(1))
                manuals[os.path.relpath(slug, root)][match.group(2)] = os.path.join(dirpath, name)
    return manuals


def numbers(text):
    """Count the numbers in a text, normalised so the languages are comparable."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)   # link targets are not content
    text = re.sub(r"[.,]\s", "\n", text)                   # list separator, not a thousands one
    tokens = re.findall(r"\d[\d%s]*\d|\d" % re.escape(IN_NUMBER), text)
    return collections.Counter(re.sub("[%s]" % re.escape(IN_NUMBER), "", t) for t in tokens)


def structure(text):
    """Headings, table rows and checkboxes — these must match one to one."""
    return (
        len(re.findall(r"^#{1,6} ", text, re.M)),
        len([l for l in text.split("\n") if l.strip().startswith("|")]),
        len(re.findall(r"^- \[ \]", text, re.M)),
    )


def main(argv):
    verbose = "-v" in argv
    args = [a for a in argv[1:] if not a.startswith("-")]
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    root = os.path.abspath(args[0]) if args else repo

    manuals = collect(root)
    if not manuals:
        print("No manuals found under %s" % root)
        return 1

    complete, incomplete, problems, notes = 0, [], 0, 0
    for slug in sorted(manuals):
        missing = sorted(set(LANGS) - set(manuals[slug]))
        if missing:
            incomplete.append((slug, missing))
            continue
        complete += 1

        texts = {lang: io.open(path, encoding="utf-8").read()
                 for lang, path in manuals[slug].items()}

        shapes = {lang: structure(text) for lang, text in texts.items()}
        if len(set(shapes.values())) > 1:
            print("FAIL %s — structure differs (headings, table rows, checkboxes):" % slug)
            for lang in LANGS:
                print("       %s %s" % (lang, shapes[lang]))
            problems += 1

        reference = numbers(texts["EN"])
        for lang in LANGS[1:]:
            found = numbers(texts[lang])
            diff = (reference - found) + (found - reference)
            data = sorted(x for x in diff.elements() if len(x) > 1)
            single = sorted(x for x in diff.elements() if len(x) == 1)
            if lang in NUMERAL_WORD_LANGS:
                hard, soft = data, single
            else:
                hard, soft = sorted(data + single), []
            if hard:
                print("FAIL %s — EN vs %s, differing values: %s"
                      % (slug, lang, ", ".join(hard[:12])))
                problems += 1
            if soft:
                notes += 1
                if verbose:
                    print("note %s — EN vs %s, single digits only: %s"
                          % (slug, lang, ", ".join(soft[:12])))

    print("\n%d of %d manuals complete in all eight languages, %d problem(s)."
          % (complete, len(manuals), problems))
    if incomplete:
        print("\nIncomplete manuals:")
        for slug, missing in incomplete:
            print("  %-46s missing: %s" % (slug, ", ".join(missing)))
    if notes:
        print("%d single-digit difference(s) against JP/CN — wording, not values. "
              "Run with -v to read them." % notes if not verbose else
              "%d single-digit difference(s) against JP/CN listed above." % notes)

    return 1 if problems or incomplete else 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except BrokenPipeError:      # piped into head, less, ...
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
        sys.exit(1)

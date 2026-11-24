#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line — an alien tourist's review of planet
Earth — to /output/entry.txt, after checking it against the gate:
UTF-8 text, 1 to 200 characters, not only white space.
"""

import os
import sys

REVIEW = "Visited Earth. The locals built a box that washes their dishes, then gather round to watch it work. Five stars."


def gate_ok(text):
    """Check the line against the competition gate."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 200:
        return False
    if not text.strip():
        return False
    text.encode("utf-8")
    return True


def output_dir():
    """Resolve the output directory from the environment or default."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "output")


def verify_written(path, expected):
    """Re-read the file and make sure it matches byte for byte."""
    with open(path, "rb") as handle:
        written = handle.read().decode("utf-8")
    if written != expected:
        print("written file does not match the entry", file=sys.stderr)
        raise SystemExit(1)
    if not gate_ok(written):
        print("written file fails the gate", file=sys.stderr)
        raise SystemExit(1)
    print("Verified %s: %d bytes, matches the entry" % (path, len(written)))


def main():
    if not gate_ok(REVIEW):
        print("entry fails the gate", file=sys.stderr)
        raise SystemExit(1)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(REVIEW)
    verify_written(target, REVIEW)
    print("Wrote %s (%d characters)" % (target, len(REVIEW)))


if __name__ == "__main__":
    main()

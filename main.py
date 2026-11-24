"""One-Liner Laugh Lab entry.

Writes one fixed funny line (the excuse a robot vacuum gives after
eating a sock) to $MAKEFUN_OUTPUT_DIR/entry.txt with no trailing
newline. Deterministic, standard library only, no network.
"""

import os
import sys

ENTRY = (
    "The sock was asking for it \u2014 lying there single, unpaired, "
    "and smelling faintly of feet and poor decisions."
)


def main() -> int:
    if not ENTRY or ENTRY != ENTRY.strip():
        print("entry must be a single non-empty line without "
              "leading/trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if len(ENTRY) > 200:
        print("entry exceeds 200 characters", file=sys.stderr)
        return 1
    if ENTRY.encode("utf-8").decode("utf-8") != ENTRY:
        print("entry is not valid UTF-8 text", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(path, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        print("written entry does not match the validated entry",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

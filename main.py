#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — entry program.

Writes a single funny one-liner (1-200 chars, per the gate) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line: a setup that sounds like an ordinary coffee order, broken by
an ending nobody sees coming — the barista's answer is not a drink at
all. Tight, fresh, no pun, no stock joke, reads cleanly out loud.
"""

import os

ENTRY = "I asked the barista for something strong. She handed me her resignation letter."


def _validate(text: str) -> None:
    """Enforce the competition gate inside the program itself: the sealed
    scorer only accepts UTF-8 text of 1-200 characters that is not only
    whitespace, so fail loudly here instead of shipping a bad entry."""
    text.encode("utf-8")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, gate requires 1-200")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    _validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

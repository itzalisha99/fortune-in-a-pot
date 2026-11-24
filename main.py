#!/usr/bin/env python3
"""Fortune in a Pot — one kind, funny fortune for a houseplant.

Writes a single fortune line (at most 120 characters) to /output/entry.txt.
"""

import os

FORTUNE = (
    "Soon the windowsill will be yours alone, the cat has found a "
    "sunnier shelf, and the sun has chosen you."
)


def validate(text):
    """Mirror the bounty gate: 1-120 chars, UTF-8, one line, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("fortune must be text")
    if not text.strip():
        raise ValueError("fortune must not be only whitespace")
    if len(text) > 120:
        raise ValueError("fortune is longer than 120 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8
    return text


def main():
    validate(FORTUNE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()

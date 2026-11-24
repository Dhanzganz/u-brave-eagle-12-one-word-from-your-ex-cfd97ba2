#!/usr/bin/env python3
"""One Word From Your Ex — make.fun entry.

Writes exactly one word to /output/entry.txt: the word an ex would use
to describe the entrant. Chosen word: "exhausting" — painfully honest,
self-aware, instantly funny, and universally relatable.
"""

import os

WORD = "exhausting"


def main() -> None:
    # Gate: entry must be UTF-8 text of 1 to 24 characters, not only whitespace.
    assert 1 <= len(WORD) <= 24 and WORD.strip(), "entry word out of gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()

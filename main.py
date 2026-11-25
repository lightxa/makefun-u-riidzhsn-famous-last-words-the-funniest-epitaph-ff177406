"""The funniest epitaph, in one line of famous last words.

This program produces a single tombstone inscription, no longer than
150 characters, and saves it to /output/entry.txt.

The joke is a first-person quip about timing: a lifetime of careful
saving, a retirement that finally arrives, and a death that follows
two days later. The punchline is the gap between the forty years and
the two days. The program is deterministic, uses only the standard
library, and makes no network calls.
"""

EPITAPH = "I spent forty years saving up for retirement. I retired on Tuesday. This is Thursday already."


import os


def main() -> None:
    """Write the epitaph to /output/entry.txt as exactly one line."""
    assert 1 <= len(EPITAPH) <= 150, "epitaph must be 1-150 characters"
    assert "\n" not in EPITAPH, "epitaph must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EPITAPH)


if __name__ == "__main__":
    main()

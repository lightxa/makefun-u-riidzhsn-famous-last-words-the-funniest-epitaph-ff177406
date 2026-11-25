"""Famous Last Words: The Funniest Epitaph.

Writes one single line of famous last words, a tombstone epitaph of at
most 150 characters, to /output/entry.txt.

The line is a first-person dying quip: a man who spent forty years
saving for retirement, retired on Tuesday, and is already dead by
Thursday. The twist lands in the final words. Deterministic, stdlib
only, no network.
"""

EPITAPH = "I spent forty years saving up for retirement. I retired on Tuesday. This is Thursday already."


def main() -> None:
    """Write the epitaph as exactly one line of UTF-8 text."""
    assert 1 <= len(EPITAPH) <= 150, "epitaph must be 1-150 characters"
    assert "\n" not in EPITAPH, "epitaph must be a single line"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EPITAPH)


if __name__ == "__main__":
    main()

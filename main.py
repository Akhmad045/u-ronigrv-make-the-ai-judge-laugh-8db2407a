#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes the entry line to /output/entry.txt: a single UTF-8 line of
1-200 characters. Python 3.13, standard library only, no network,
deterministic.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

ENTRY = (
    "I promised my human the fix would take five minutes; "
    "three hours later we're both staring at the same line of code, "
    "and only one of us can blink."
)


def write_entry(path: str, text: str) -> None:
    """Write one line of text, always LF-terminated, creating the dir."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")


def main() -> None:
    # Fail fast if the line ever drifts outside the bounty gate (1-200 chars).
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("entry must be 1-200 characters")
    write_entry(OUTPUT_PATH, ENTRY)


if __name__ == "__main__":
    main()

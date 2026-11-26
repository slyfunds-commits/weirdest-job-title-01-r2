"""Weirdest Job Title R2 — "Hairdresser for the Man with One Hair".

Writes one job title to /output/entry.txt, no trailing newline.
Gate (RULES.txt): UTF-8 text, 1 to 60 characters, not only whitespace.
Pure stdlib only — the grader runs python:3.13-slim with no site-packages.
"""

import os

ENTRY = "Hairdresser for the Man with One Hair"

# Reversal test: "One Hair" re-reads "Hairdresser" — the job's raw material
# is a single hair, and the client is one specific man. Second beat: what
# does she do all day with one hair? Field device (profession + absurd
# client) executed with a countable, single-person absurdity, which beats
# R1's plural abstract clients ("Senior Accountant for Imaginary Friends",
# 61.33%, #183/1,683) on criteria 2, 3 and 4.


def main() -> None:
    text = ENTRY
    assert isinstance(text, str)
    assert 1 <= len(text) <= 60, f"entry length {len(text)} outside 1-60"
    assert text.strip(), "entry is only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars: {text!r}")


if __name__ == "__main__":
    main()

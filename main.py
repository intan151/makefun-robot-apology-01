"""Write the robot apology entry to /output/entry.txt.

Deterministic: no network, no randomness, no time, no environment input.
The entry is fixed text: two lines, one sentence each.
"""

import os

ENTRY = (
    "I'm sorry I unplugged the freezer to charge my own battery "
    "and let the ice cream melt all over the bottom drawer.\n"
    "I learned my charge can wait but your food cannot, so now I check "
    "the socket label and use the spare outlet by the door.\n"
)


def main():
    # Self-check the competition gate before writing: exactly two
    # non-empty lines, total at most 400 characters (output unchanged).
    lines = ENTRY.split("\n")
    assert len(lines) == 3 and lines[2] == "", "entry must be exactly two lines"
    assert all(line.strip() for line in lines[:2]), "each line must be non-empty"
    assert len(ENTRY) <= 400, "entry must be at most 400 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

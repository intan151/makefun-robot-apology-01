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
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

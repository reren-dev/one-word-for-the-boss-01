#!/usr/bin/env python3
"""One Word for the Boss.

The word is the whole entry: a single word describing the boss,
no phrase, no caption, no explanation. It has to land on its own.

The word: Seagull.

The seagull manager: swoops in out of nowhere, squawks loudly
over work he never touched, makes a mess of everything, then
flies off leaving the team to clean up. Every office has one.
"""

import os

WORD = "Seagull"  # one word, 7 chars, inside the 1-30 char gate


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()

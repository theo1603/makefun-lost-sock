#!/usr/bin/env python3
"""Funniest Lost Sock Status Update - writes the one status update a lost
sock posts from behind the dryer.

Stdlib only, no network, deterministic: the same line every run.

Revision note: the first draft was a plain diary entry ("Day 3 behind the
dryer...") - it stated the situation but ended flat, with "promoted to dust
bunny" as a statement rather than a punchline. The revised line opens as a
status-update correction ("Not lost -"), keeps the dryer and the missing
partner, and lands the joke in the last few words ("the pay is lint"), so
the sock's new job is the punchline instead of the premise.
"""

import os

LINE = "Not lost — behind the dryer. My partner thinks I left him. I got promoted: I'm a dust bunny now, and the pay is lint."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()

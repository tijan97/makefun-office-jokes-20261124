#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — one-line office joke entry.

The program writes exactly one joke about office life to entry.txt.
"""

import os

LINE = "I replied-all asking to be removed from this thread, and now the whole company has replied-all to agree with me."


def main() -> None:
    # Enforce the bounty gate: 1-199 characters, one non-blank line.
    if not 1 <= len(LINE) <= 199:
        raise SystemExit(f"entry must be 1-199 characters, got {len(LINE)}")
    if "\n" in LINE or not LINE.strip():
        raise SystemExit("entry must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()

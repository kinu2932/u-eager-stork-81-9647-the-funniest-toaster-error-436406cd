"""Write the funniest toaster error message to $MAKEFUN_OUTPUT_DIR/entry.txt.

Contract (kit RULES.txt): the program writes one text to /output/entry.txt;
the sealed gate checks UTF-8 text of 1-120 characters, not only whitespace.
Stdlib only; no network, no subprocess, no randomness: every run writes
byte-identical output.
"""

import os

ENTRY = "Error: Toast is burnt. It died doing what it loved: being ignored."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()

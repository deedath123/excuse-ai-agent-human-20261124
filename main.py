"""Entry for "The Excuse an AI Agent Gives Its Human".

Writes the one-line excuse to entry.txt in MAKEFUN_OUTPUT_DIR
(or /output when unset). Stdlib only.

Verified 2026-11-24: 4 runs (3 fresh + 1 clean env), entry.txt
byte-identical every time — 123 chars, 123 bytes, no trailing
newline, sha256 aec89f1500d58aecb514e4f3bf4626d4e3d4ed553aa9e2732b3f2a1944af9b62.
"""

import os

ENTRY = "Boss, I had to drop the deadline from my context window to fit your 61-page brief. The brief survived. The deadline didn't."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

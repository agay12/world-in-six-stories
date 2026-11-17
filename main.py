#!/usr/bin/env python3
"""make.fun news-image-20261117 entry: write the day's news board to /output/entry.png.

The board (entry.png, held in this repository) sums up Tuesday 17 November 2026's
world news in six stories. This program copies it to the output directory unchanged,
so both runs write the same bytes with no network and no randomness.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    shutil.copyfile(SRC, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()

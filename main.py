#!/usr/bin/env python3
"""make.fun news-image-20261117 entry: write the day's news board to /output/entry.png.

The board (entry.png, held in this repository) sums up Tuesday 17 November 2026's
world news in six stories: US strikes on Qeshm Island in the Iran war, the struck
Crimean Bridge, the Canada-China tariff cuts ahead of APEC Shenzhen, Bangladesh's
garment-worker protests, the Americas losing measles-free status, and UK sanctions
on West Bank settlement builders. This program copies the board to the output
directory unchanged, so both runs write the same bytes with no network and no
randomness.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
MAX_BYTES = 1048576


def main() -> None:
    size = os.path.getsize(SRC)
    if size > MAX_BYTES:
        raise SystemExit(f"entry.png is {size} bytes, over the 1 MiB gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SRC, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()

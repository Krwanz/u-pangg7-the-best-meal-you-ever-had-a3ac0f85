#!/usr/bin/env python3
"""The Best Meal You Ever Had — one sentence, at most 200 characters.

Writes the entry sentence to /output/entry.txt (or ./output/entry.txt
when run locally).
"""

import os

SENTENCE = (
    "The best meal I ever had was my grandmother's rendang, beef simmered "
    "until it fell apart, eaten on her kitchen floor while rain drummed "
    "the tin roof and coconut and chili hung in the air."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    print(f"Wrote {len(SENTENCE)} characters to {path}")


if __name__ == "__main__":
    main()

# makefun-six-words-story — entry for "Six Words, One Story"
# (u-deranalabs-six-words-one-story-f982e410)
#
# Writes one original six-word story to <output dir>/entry.txt.
# Fully deterministic: fixed text, no randomness, no dates, no network,
# no input. The output directory comes from MAKEFUN_OUTPUT_DIR when set,
# defaulting to /output; the directory is created if needed and the file
# is left world-readable.
#
# The story is 6 words and 37 characters plus a newline, inside the
# competition's 1–60 character gate; check_story enforces the word count
# and the character budget before writing.

import os
import stat
from pathlib import Path

STORY = "She kept his letters. Never answered."

MIN_CHARS = 1
MAX_CHARS = 60
WORD_COUNT = 6


def check_story(text: str) -> None:
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"story must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("story must not be only whitespace")
    words = text.split()
    if len(words) != WORD_COUNT:
        raise ValueError(f"story must be exactly {WORD_COUNT} words, got {len(words)}")


def main() -> None:
    check_story(STORY)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(STORY + "\n", encoding="utf-8")
    os.chmod(entry, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()

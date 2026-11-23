# makefun-six-words-story
[![make.fun · u-deranalabs-six-words-one-story-f982e410](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-six-words-one-story-f982e410)
[![rank](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/m1651/makefun-six-words-story/rank.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-six-words-one-story-f982e410)
[![reward](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/m1651/makefun-six-words-story/reward.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-six-words-one-story-f982e410)

An entry for the make.fun competition **"Six Words, One Story"**
([u-deranalabs-six-words-one-story-f982e410](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410)).

The entry is a tiny deterministic Python program that writes one original
six-word story to `entry.txt`. The story was invented for this competition;
it is not copied from anywhere.

The story:

> She kept his letters. Never answered.

## Run it

Requires Python 3.13 or later. From the repository root:

```sh
python3 main.py
```

This writes the story to `/output/entry.txt` (creating `/output` if needed).
To write somewhere else, set `MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/story-out python3 main.py
```

The program is fully deterministic: it contains no randomness, no dates
and no network access, so repeated runs produce byte-identical output.
The story is checked to be exactly six words and 1–60 characters before
it is written, and the output file is left world-readable.

## License

MIT — see [LICENSE](LICENSE).

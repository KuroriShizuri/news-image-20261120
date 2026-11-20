# The World Today — 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/KuroriShizuri/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/KuroriShizuri/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120)

Entry for make.fun competition `news-image-20261120`: sum up 20 November's
world news in one image.

`main.py` (Python 3.13, stdlib only, no network) copies the bundled
cover artwork `entry.png` (1024×1024 PNG, 93,305 bytes — under the
1 MiB limit) to `<MAKEFUN_OUTPUT_DIR>/entry.png` (`/output` by default).
Before copying it checks the PNG magic bytes and validates the dimensions
are exactly 1024×1024, and after copying it verifies the copy by file size
and SHA-256 digest, then prints the byte count. The copy is byte-identical
on every run.

## What the cover shows

A broadsheet front page, "THE WORLD TODAY — Friday 20 November 2026":
one hero story across the top and the other six in a 2×3 grid below, each
with a numbered red medallion (1–7), one flat hero emblem at least 150 px
across, and a short label in condensed bold type. Every word is real
typeset text drawn by code (PIL + DejaVu / Noto Sans Condensed) — never
rendered by an image model. Palette: flat black, red, white and light
grey; flag colours appear only where correctness demands them (the US,
Chinese and Russian flags in the lead story). No gradients anywhere.

Researched from the day's reporting (20 November 2026):

1. **Trump, Xi and Putin meet in Shenzhen** — the first-ever trilateral
   summit of the three leaders, at the APEC summit, with nuclear arms and
   global security on the table. Shown as three suited figures seated at
   a table before a Shenzhen skyline, under the US, Chinese and Russian
   flags in their correct colours — the hero panel across the top.
2. **Trump defers the Iran war decision to 2027** — no rush, "see what
   happens after Jan 1". Shown as a calendar page marked 2027.
3. **ICJ rules Myanmar committed genocide** — the UN's top court rules
   against Myanmar over the Rohingya minority. Shown as the scales of
   justice.
4. **Cyclone Akvan makes landfall on India's Odisha coast** — about
   300,000 people evacuated, 423 rescue teams deployed. Shown as a flat
   black spiral with a red arc over storm waves.
5. **NASA's Voyager 1 passes one light-day from Earth** — the first
   human-made object to reach the mark. Shown as a dish spacecraft
   beaming a dotted red signal line to a small grey Earth.
6. **Houthi missile strikes Riyadh** — the Saudi sovereign wealth fund
   (PIF) tower damaged. Shown as a missile with a red flame streaking
   toward a tall tower topped by a red impact burst.
7. **GTA 6 sales pass The Odyssey's box-office run** — the game passes
   the film's $1.8bn global box-office total. Shown as a game controller
   beside a film reel.

## Verification

- PNG exactly 1024×1024, 93,305 bytes (limit 1,048,576).
- Deterministic: the generator (`build/build_cover.py`) run twice
  produces byte-identical output (SHA-256
  `1e0f96a7815c6ff4e90586d84af2c48ed9882f53125ab3fe5d834a203fc851a3`).
- `python3 entry/main.py` run twice with `MAKEFUN_OUTPUT_DIR` set to a
  scratch directory writes the same bytes as the bundled image (same
  SHA-256, verified by size + digest after copying).
- Downscale check: all 7 stories still identifiable from emblems +
  labels at 300×300 (masthead, date, hero headline and all seven
  two-line labels stay legible; medallions 1–7 stay visible).
- Every on-image text line spell-checked by eye at full size; the date
  "Friday 20 November 2026" is correct (20 November 2026 is a Friday).

---

<sub>Entered on [make.fun](https://make.fun/?ref=1g7byhvf&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>

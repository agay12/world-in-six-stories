# world-in-six-stories

A make.fun **news-image-20261117** entry: one image that sums up Tuesday
**17 November 2026**'s world news, written to `/output/entry.png` by the
program in this repository.

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/agay12/world-in-six-stories/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/agay12/world-in-six-stories/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

## What the image shows

A dark editorial board, "THE WORLD IN SIX STORIES", datelined
Tuesday · 17 November 2026, with six tagged cards — region chip, headline,
three-line brief and a small drawn glyph:

1. **Mideast** — US Air Force strikes on Qeshm Island in the widening Iran war;
   the IRGC downs an MQ-9 Reaper; Bahrain intercepts Iranian drones at Sheikh
   Isa Air Base.
2. **Ukraine** — the Crimean Bridge struck by drones for a second day, a
   collapsed road span in the Kerch Strait; Russia pounds Kyiv's bridges.
3. **Asia** — Canada and China agree further tariff cuts before the APEC
   summit in Shenzhen (Carney–Xi talks).
4. **South Asia** — Bangladesh garment-worker protests block the N3/N4/N5
   highways and shut 37 factories as the wage-board meeting slips to 23 November.
5. **Americas** — PAHO revokes measles-elimination status of the US, Mexico
   and Bolivia amid 5,700+ US infections and deaths in 2026.
6. **UK / Israel** — the UK sanctions eight West Bank settlement-construction
   companies and Tzav 9 over blocked Gaza aid.

Sources as first reported on the day: Reuters, AFP, AP, Le Monde, The Hindu,
France 24. No other day's events are shown.

## The program

- `main.py` — Python 3.13, standard library only. It copies the repository's
  `entry.png` (107,748 bytes, 1024×1024 PNG, under the 1 MiB gate) to
  `/output/entry.png` — or `$MAKEFUN_OUTPUT_DIR` when set — refusing if the
  file outgrows the gate. Deterministic: both runs write the same bytes,
  no network, no randomness.
- `entry.png` — the entry image itself.
- `.makefun/owner.json` — wallet claim naming the wallet on the make.fun
  account that entered it.

Run it: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py`

## License

MIT — see [LICENSE](LICENSE).

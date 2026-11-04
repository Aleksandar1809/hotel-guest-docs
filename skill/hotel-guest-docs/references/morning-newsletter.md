# Morning newsletter

Daily printed guest newsletter, in German only. Greeting and poem, weather, today's activities, four wellness tips, the evening menu, sauna infusions, house information and a preview of tomorrow. It is built in Claude Design as an HTML print template; the daily issue only swaps content.

## Format and print

- A3 landscape (420 × 297 mm), double-sided, roll fold: 3 panels of 140 mm per side, folds at 140 and 280 mm.
- Sheet 1 (outside): evening menu flap · wellness courier · cover (right panel). Sheet 2 (inside): "The morning" · "The day" · "The evening", with a weather band across all three panels.
- Printed on cream paper, so **no solid or dark backgrounds** (toner). The sheet colour is screen preview only.
- Fold marks only as short notches at the top and bottom edges: no labels, no lost space.
- Print: A3, landscape, margins "none", scale 100 %, duplex flipped on the short edge.

## Inputs (daily)

1. Evening menu and weather text, copied as text (weather heading + text).
2. Weather symbols as letters for 07:00 · 12:00 · 17:00, e.g. `C · G · C`, plus min/max and an optional note (e.g. snow line).
3. Building-block IDs, e.g. `W12 · H64 · S05`.
4. Deviations from the weekly plan only (the plan holds the default programme per weekday).

## Building blocks

The content library is a set of Markdown files, one per section. Each entry:

```
## W12 · Name
**Vorlage:** source template · **Saison:** Sommer/Winter/ganzjährig · **Art:** type · **Bild:** B07 · **Info:** extra line · **Stand:** last printed version
<text, line for line>
```

| Letter | Section | Used in |
|---|---|---|
| W | Wellness & beauty | Wellness courier (4 tips/day) |
| H | House info / day extras | The day (day extra), The evening (house info) |
| F | Fixed elements | Fixed texts of the template |
| O | Local info | House info box |
| T | Hikes | The morning (hike tip with length · duration) |
| V | Products for sale | Product box on the wellness courier |
| S | Quotes and poems | Cover (poem) and The morning (quote) |
| E | Festivities and holidays | Holiday issues |
| B | Images (with photo credit) | Cover, The morning, The day, product box |

Look up a block by its heading (`## W12 `) and read only that entry. New blocks go at the end of their section with the next free number. The "Stand" field records the last printed version, which may differ from the original Word source.

## Weather symbols

| Code | German | English |
|---|---|---|
| A | Sonnig | Sunny |
| B | Heiter | Fair |
| C | Wolkig | Cloudy |
| D | Bedeckt | Overcast |
| E | Nebel | Fog |
| F | Regenschauer | Rain showers |
| G | Regen | Rain |
| H | Gewitter | Thunderstorm |
| I | Schneeschauer | Snow showers |
| J | Schneefall | Snowfall |
| K | Schneeregen | Sleet |
| L | Windig | Windy |

Weather band: cell 1 = 07:00 + min · cell 2 = 12:00 + max · cell 3 = 17:00 + note.

## What changes daily

| Area | Content | How often | Source |
|---|---|---|---|
| Date | Cover (day, month year, weekday), menu header, day-extra label, preview date | daily | – |
| Cover | Poem with title and author | daily | S block (cover type) |
| Evening menu | All courses | daily | Kitchen, copied as text |
| Cover | Cover image + photo credit | as needed | B block |
| Wellness courier | 4 tips: category, title, text | daily | W blocks |
| Wellness courier | Product box + image | as needed | V block |
| Weather band | 3 symbols, min/max, note | daily | Weather report |
| The morning | Weather heading + text | daily | Weather report |
| The morning | Quote | daily | S block (inside type) |
| The morning | Hike tip with length/duration, image, credit | as needed | T block |
| The day | Activity programme | daily | Weekly plan + deviations |
| The day | Day extra + image + credit | per weekday | H block |
| The evening | Infusions | daily | Weekly plan |
| The evening | Preview of tomorrow | daily | Weekly plan of the next day |
| The evening | House info | as needed | H block |

Always the same: background pattern, logo, "Ihre tägliche Morgenpost", ornament line, "Guten Morgen!", host family greeting, section titles, "Vier Empfehlungen für heute", "Wir wünschen guten Appetit", note on the evening menu, guest-app QR box, fold marks.

## Rules

- **Texts are copied word for word.** Never rewrite, shorten or "improve" a block or the menu.
- **Swap content only; never touch the layout.**
- **Overflow:** every panel clips what does not fit, silently. Check every panel before printing. Images in "The morning" and "The day" take the remaining height; below 36 mm the panel overflows. Product box, QR box and greeting stay at the bottom.
- In the menu flap the space is spread over the courses; long menus move closer together. Course order: starters · soups · salads · main courses · dessert · cheese.
- Activity timeline: filled dot = activity, open dot = infusion.
- Routine issues: check for overflow only, no full review.
- If anything is unclear, ask.

## Design defaults

- Fonts: Cormorant Garamond (titles), EB Garamond (text), Jost (times, labels, small caps), Petit Formal Script (only the host family greeting). All free on Google Fonts.
- Colours: paper #F5ECD6 (screen only) · ink #2C2620 · gold #8A6D3A / #B99553 · grey #6b6155 (nothing lighter for text).
- Style: warm, family-run, alpine-elegant; calm, clean, plenty of white space.
- Background pattern in gold lines, fading out towards the top.

## Output (content sheet for the template)

Deliver the issue as a content sheet, panel by panel, so it can be filled into the template (or applied directly in Claude Design):

```
SHEET 1 · OUTSIDE
Menu flap:        date header · courses (as delivered) · cheese
Wellness courier: 01–04 (category · title · text from W blocks) · product box (V block, image)
Cover:            day · month year · weekday · poem title · poem · author · cover image + credit

SHEET 2 · INSIDE
Weather band:     07:00 <symbol> min · 12:00 <symbol> max · 17:00 <symbol> note
The morning:      weather heading · weather text · quote · hike tip (name, length · duration, text, image)
The day:          timeline (time · activity · note) · day extra (label, title, subtitle, text, info line, image)
The evening:      infusions (time · name) · menu note · preview of tomorrow · house info

CHECK:            overflow per panel · open points
```

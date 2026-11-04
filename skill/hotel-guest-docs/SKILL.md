---
name: hotel-guest-docs
description: Checks and produces a hotel's recurring guest documents in German, English, French and Italian, in a fixed house format. Covers the evening menu, kids' menu, daily wine recommendation card, weekly activity programme, kids' club programme and the printed morning newsletter. Use when hotel staff paste a German menu, a sommelier's wine sheet, weekly schedules, a kids' club plan or newsletter inputs and need a proofreading verdict plus translations or print files, or when they ask "Has anything changed?" about one of these documents.
---

# Hotel guest documents (DE · EN · FR · IT)

This skill turns the raw material hotel staff receive every day into finished guest documents: checked, translated, and formatted the same way every time. It was built and refined in daily use at a 5★ Superior resort in Tyrol. All examples use the fictional **Hotel Alpenrose ★★★★★S, Tyrol**.

## Document types

| Document | Rhythm | Staff send | You deliver | Rules | Example |
|---|---|---|---|---|---|
| Evening menu | daily | Date + German menu text | Verdict on the German + EN/FR/IT (copy-paste text, or 3 .docx via `scripts/menu_docx.py`) | `references/evening-menu.md` | `examples/evening-menu.md` |
| Kids' menu | daily | German kids' menu text | Verdict + DE/EN/FR/IT plain text with bold language labels | `references/kids-menu.md` | `examples/kids-menu.md` |
| Wine card | daily | Sommelier's info sheet (incomplete, German) | Completed German card + EN/FR/IT cards, one page each; only essential notes | `references/wine-list.md` | `examples/wine-list.md` |
| Weekly programme | weekly | Scans of the instructors' schedules + last printed DE/EN | Findings + patches to the last printed DE and EN version; final check | `references/weekly-programme.md` | `examples/weekly-programme.md` |
| Kids' programme | weekly | German plan | Corrected German + English version, same layout | `references/kids-programme.md` | `examples/kids-programme.md` |
| Morning newsletter | daily | Menu, weather, symbol codes, building-block IDs, deviations from the weekly plan | Content for every panel of the print template + overflow check | `references/morning-newsletter.md` | `examples/morning-newsletter.md` |

Read only the reference file for the document in front of you. Read the example when the format is unclear.

## Workflow (all documents)

1. **Identify the document type** from the input. If it is a correction or a "Has anything changed?" question, compare with the last delivered version in this chat.
2. **Check the German first** and give an explicit verdict before anything else: `Deutsch passt.` or a numbered error list. Locate every error (course / dish / line, or day / time). Never change the German source yourself. Staff correct it.
3. **Reading and typing errors** (the kitchen writes by hand and someone types it up) are reported *and* already corrected in the translations.
4. **Translate or complete** with the reference rules. Apply known house rules silently.
5. **Produce the output** in the exact format of the reference file. Where a script or template exists, use it and never rebuild the layout by hand.
6. **Run the quality checklist** below and deliver. Reply in one or two sentences around the result. Report only what staff must act on.

## Precision at minimal token use

These rules came out of many iterations in daily use. Apply them always.

- **Formatting lives in code or templates, not in the chat.** Generate files with the provided script or patch the last printed file. Do not analyse templates, re-create layouts or render previews unless asked; a technical check is enough.
- **Never repeat the input, never list rules you applied, no preambles, no recap.** If you had to decide something, state the decision in one line.
- **Ask only when something essential is missing or truly ambiguous.** Otherwise decide and say so in one line.
- **Changes after delivery:** send only the affected lines, always the *whole* line (all lines of the dish if a line break moves), in every language, labelled with course/dish/line. No new files unless asked. A purely grammatical fix with no effect on translations takes one sentence.
- **Fixed elements are never sent and never reported missing:** document title, star line, salad-buffet line, cheese line, standard notices. Set them silently.
- **Approved texts are reused word for word**, never re-translated: the wine register, the yoga catalogue, standard notices, newsletter building blocks.
- **Report only essentials.** Wine: missing or doubtful vintage, price or wine, and edits beyond spelling. No correction lists for silent fixes.
- **Vague German stays vague.** If the chef writes only "Praline" or "Eingelegtes", do not invent the ingredient in any language.
- **Never invent facts:** no vintages, producers, places, prices, times or ingredients that are not in the input or the approved texts.
- **Reviewer corrections become permanent rules** from the moment they arrive. Read corrected .docx files at XML level (`<w:strike/>` = delete, `<w:highlight/>` or coloured text = insert); plain-text diffs miss the markup. If two reviewers contradict each other, flag it and do not pick one.
- **Chat hygiene:** daily documents get a new chat per day to keep context small; weekly documents may stay in one chat while the context is still useful.

## Language rules

| | German (source) | English | French | Italian |
|---|---|---|---|---|
| Variant | Austrian German | British luxury hospitality | France French | Standard Italian |
| Register | as written by the kitchen/instructors | elegant, natural, never literal | elegant, natural, never literal | elegant, natural, never literal |
| Menu separator | oder | or | ou | oppure |
| Quotes | „…" | "…" | « … » with narrow no-break spaces | «…» |
| Numbers | 0,75l · 5cl · 2.017 m | prices/quantities keep the decimal comma · 2,017 m | as German | as German |

- **German:** Austrian vocabulary (Marille, Karfiol, Kren, Obers, Topfen) and diminutives (Nockerl, Tascherl) stay. House spellings are never corrected. Watch for: doubled prepositions (mit … mit), dative errors after mit/an/auf/in, missing hyphens in multi-part compounds, missing commas, superfluous ellipses and spaces.
- **English:** sentence case on menus (first word + proper names), Title Case for activity names. British spelling (programme, centre, colour, yoghurt). At most one "served with" per dish.
- **French:** one "avec" per dish, then comma lists. No comma before "et", never three "et" in a line. A preposition at the start of a continuation line is removed and a comma ends the previous line.
- **Italian:** "ed" only before a word starting with e. Separator "oppure". Generic spirits lower case, brand and origin names capitalized.
- Full term tables per document are in the reference files.

## House style

- Guest-facing texts are elegant, warm, discreet and grammatically flawless, at 5★ Superior level. Never casual, never robotic. Casual wording in source texts is raised ("toller Süßwein" → "ein herrlicher Süßwein"), never shortened or rewritten beyond that.
- Translations read as if written by a native speaker. They are not word for word.
- Guest texts never openly invite individual dietary requests. The house does not cater to many special diets.
- Place names: local place adjectives are dropped in French menus and kept in English and Italian.

## Output formats (summary)

- **Evening menu:** per language, in copy-paste format: category line, dish lines, separator word on its own line, `***` after each course. `scripts/menu_docx.py` turns the three texts into .docx files with title, star line, spacing, separators and cheese line.
- **Kids' menu:** plain text. **Bold language label**, blank line, menu text. Order DE → EN → FR → IT, courses separated by a blank line. No heading, no date.
- **Wine card:** four one-page cards (DE, EN, FR, IT) in the card structure of `references/wine-list.md`. The German card carries the descriptions.
- **Weekly programme:** patch list per day for DE and EN, then the final check. Exactly 2 pages in Word.
- **Kids' programme:** corrected German, then English, line by line in the original layout.
- **Morning newsletter:** content sheet per panel, then the overflow check.

## Quality checklist before delivering

- [ ] German verdict given first, each finding located.
- [ ] Every course/day of the source is present in every language, in the same order, with the same number of items and times.
- [ ] Fixed lines and categories exactly as in the reference.
- [ ] Separators, quotes, decimal commas and time formats per language.
- [ ] Dates: weekday matches the calendar; EN ordinal suffixes (st/nd/rd/th) set superscript in Word.
- [ ] Nothing invented; open points reported in one line each.
- [ ] Layout limits respected (one page per wine card, exactly 2 pages for the weekly programme, no clipped newsletter panel).

## Adapting to another hotel

Keep the workflow and the precision rules. Edit the house profile in each reference file: hotel name and place line, fixed lines (salad buffet, cheese trolley, intro sentences), category names, the roles that send material, term tables and approved texts. Add new term decisions as soon as staff confirm them.

## Privacy

Guest documents never contain guest names, room numbers, health information or staff contact details. Use roles ("our bar manager", "our outdoor guide") unless the hotel explicitly wants a name printed. Files you generate carry no author metadata.

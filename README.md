# AI document automation for multilingual guest communication — a Claude skill

`hotel-guest-docs` is a Claude skill that checks and produces a hotel's recurring guest documents in **German, English, French and Italian**, in a fixed house format. It grew out of generators that are in real daily use at a 5★ Superior resort in Tyrol, Austria, and was refined through many iterations for precise output at minimal token use.

## What the skill does

It covers **6 recurring document types**:

| Document | Input staff paste | What the skill returns |
|---|---|---|
| Evening menu | The German menu from the kitchen | Proofreading verdict for the German + EN/FR/IT in a fixed format |
| Kids' menu | The German kids' menu | Verdict + EN/FR/IT for the colouring-page template |
| Daily wine recommendation card | The sommelier's (often incomplete) wine sheet | Completed, checked card in DE/EN/FR/IT |
| Weekly activity programme | Instructors' schedules | Updated German and English edition |
| Kids' club programme | The German kids' club plan | Corrected German + English version |
| Morning newsletter | Menus, weather and house news | Newsletter assembled from approved text blocks |

How it works:

- **German is checked first.** Every document starts with an explicit proofreading verdict; errors are located by course and line.
- **Translations follow house rules**, not improvisation: term tables, fixed lines and approved wording keep the output consistent from day to day.
- **Short answers.** Claude returns the files plus only what staff must act on (for example, a missing vintage). Ask "Has anything changed?" and it returns only the affected lines.

## Repository contents

| Path | What it is |
|---|---|
| `skill/hotel-guest-docs/` | The skill source: `SKILL.md`, one reference file per document type, fictional examples, and a Word export script for the menu |
| `dist/hotel-guest-docs.zip` | The packaged skill, ready to upload to Claude |
| `docs/case-study.md` | One-page case study |
| `docs/demo-script.md` | 60-second live demo |
| `docs/interview-qa.md` | Common questions about AI adoption, answered from this project |
| `docs/fr-it-corrections.md` | French and Italian correction rules |

## Install in Claude

Steps from Anthropic's Help Center article [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) (checked November 2026). Skills are available on Free, Pro, Max, Ultra, Team and Enterprise plans and need code execution.

1. **Turn on code execution.** Individual plans: **Settings → Capabilities**, switch on **Code execution and file creation** (called **Create and edit files** in the updated settings layout). Team and Enterprise: an owner checks that code execution and Skills are enabled under **Organization settings**.
2. **Upload the skill.** Go to **Customize → Skills**, click **+**, then **+ Create skill**, choose **Upload a skill** and select `dist/hotel-guest-docs.zip`.
3. **Switch it on.** The skill appears in your skills list; make sure its toggle is on.

Uploaded skills are private to your account until you share them. If the upload fails, the article lists the usual causes: ZIP size limit, a folder name that does not match the skill name, or a missing `SKILL.md`. To build your own skills, see [How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

## Demo: Hotel Alpenrose ★★★★★S, Tyrol

All examples use the fictional **Hotel Alpenrose ★★★★★S, Tyrol**. Open a new chat with the skill switched on and paste a German menu, typos included:

```
Abendmenü Freitag, 16.10.2026

Vorspeisen
Geräucherte Lachsforelle
auf Gurkensalat mit mit Sauerrahm
***
Hauptgerichte
Rosa gebratener Hirschrücken
mit Preiselbeersauce, Rotkraut
und Serviettenknödel
oder
Gebratenes Zanderfilet
auf Wirsing mit Patatenpüree
und Weißweinschaum
***
Dessert
Marillenknödel
mit Butterbröseln und Vanilleeis
```

Claude first gives the German verdict, located by course and line: the doubled "mit", the reading error "Patatenpüree" (→ Batatenpüree, sweet potato) and the missing closing "***". Then come the English, French and Italian menus in the fixed house format. The full script with timings is in [`docs/demo-script.md`](docs/demo-script.md); expected outputs for every document type are in [`skill/hotel-guest-docs/examples/`](skill/hotel-guest-docs/examples/).

## Results at the resort

From the [case study](docs/case-study.md):

- **~2 staff hours saved per day** (~60 hours per month)
- **Tool cost: ~€20 per month** (one Claude Pro subscription)
- **Refined through many iterations** for precise output at minimal token use

## Adapting it to your hotel

Replace the hotel name, fixed lines and term tables in `skill/hotel-guest-docs/references/` with your own, then rebuild the ZIP so the `hotel-guest-docs/` folder is the root of the archive.

## Privacy

This repository contains no real hotel, guest or staff data. See [`PRIVACY-CHECK.md`](PRIVACY-CHECK.md) for how that was verified.

## License

[MIT](LICENSE)

# Case study: AI document generators for a 5★ Superior resort

**Client:** a 5★ Superior resort in Tyrol, Austria · **Built by:** Aleksandar Obradovic, former hotel Front Office Manager · **Tool:** Claude

## The problem

A luxury resort produces the same guest documents every day, in up to four languages. The raw material is never ready to use:
- **The menu arrives in German only**, written by hand in the kitchen and typed up by a colleague, with the reading errors that come with that.
- **The wine list arrives incomplete from the sommelier**: short headings, missing vintages, quantities and countries, casual wording.
- Weekly activity and kids' programmes arrive as schedules from instructors; the morning newsletter has to be assembled from menus, weather and house news.

Each document must be correct, consistent from day to day, and written at 5★ Superior level in German, English, French and Italian. Doing this by hand cost staff time every single day.

## What was built

Six document generators in Claude, one per recurring document type:

| Document | What the generator does |
|---|---|
| Menu | Checks the German, then writes the other three languages in a fixed format |
| Kids' menu | Checks the German, writes EN/FR/IT for the colouring-page template |
| Wine list | Completes the incomplete sheet, checks it for errors and writes it in 4 languages |
| Weekly programme | Updates the last printed German and English edition from the instructors' schedules |
| Kids' programme | Corrects the German plan and produces the English version |
| Daily morning newsletter | Built in Claude Design from a library of approved text blocks |

How they work:
- **German is checked first**, with an explicit verdict; errors are located by course and line. Staff fix the source; translations already use the corrected reading.
- **House rules, not improvisation:** term tables, fixed lines and approved texts encode the house style. Corrections from the hotel's French reviewer become permanent rules.
- **Formatting lives in code and templates**, so output looks identical every day and the AI never spends tokens re-creating a layout.
- **Short answers:** only the files plus what staff must act on (for example, a missing vintage). Changes return only the affected lines.

## Results

- **6 recurring document types:** menu, kids' menu, wine list, weekly programme, kids' programme, daily morning newsletter (built in Claude Design).
- **Up to 4 languages:** DE, EN, FR, IT.
- **About 2 staff hours saved per day, 7 days a week** (about 60 hours per month).
- **Tool cost:** one Claude Pro subscription, about €20 per month.
- **Each generator was refined through many iterations** for precise output at minimal token use.

## Governance

- **Backup and portability:** an exportable backup (~130 MB) lets the system be restored or moved to another AI provider. Rules, term tables and templates are plain files, not locked inside one tool.
- **Training and ownership:** the owners and a part-time colleague were trained; the system runs on the hotel's own accounts without Aleksandar.
- **Human in the loop:** staff review the German verdict and the final files; the French reviewer's corrections are checked, then fed back into the rules.
- **Data:** the generators work with menus, wine sheets and schedules. No guest data goes in.

## What I would do differently

1. **Fixed templates for layout from day one**, so the AI only fills in text.
2. **One source of rules per generator.** Rules spread across memory, briefings and chats started to contradict each other.
3. **Validate reviewer corrections before turning them into permanent rules.** Some French corrections were by feel and inconsistent.
4. **Measure time per document before and after from the start**, instead of estimating.
5. **Plan backup and staff training from the first version**, not at the end.

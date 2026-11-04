# 60-second live demo: Hotel Alpenrose ★★★★★S, Tyrol

**Goal:** show a German-only menu turning into a checked, three-language menu in a fixed format, live.

## Before the interview (2 minutes)

1. In Claude, make sure **code execution is enabled** (skills need it). Then upload the skill: **Customize → Skills → + → Create skill → Upload a skill**, choose `dist/hotel-guest-docs.zip`, and check that it is switched on.
2. Open a **new chat** (small context, fast answer).
3. Copy the input below into your clipboard.
4. Have `skill/hotel-guest-docs/examples/evening-menu.md` open in a second tab as a fallback.

## Input to paste

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

## Script

| Time | Do | Say |
|---|---|---|
| 0–10 s | Show the empty chat | "This is a real workflow from a 5★ Superior resort. Every day the kitchen sends the dinner menu in German only. The guests need it in English, French and Italian." |
| 10–15 s | Paste the input, press Enter | "I paste exactly what the kitchen sends, typos and all." |
| 15–40 s | Let Claude answer | "The first thing it does is check the German, because a handwritten menu gets typed up by a colleague and reading errors happen. It never rewrites the chef's text. It reports the error and uses the correct reading in the translations." |
| 40–55 s | Scroll through the result | "Here is the verdict: a doubled 'mit', and 'Patatenpüree', which should be 'Batatenpüree', sweet potato. Then English, French and Italian in the house format: fixed categories, 'or / ou / oppure', one 'avec' per dish in French, house terms like pike-perch and napkin dumpling." |
| 55–60 s | Look back at the interviewer | "At the resort this saves about two staff hours a day, for about €20 a month in tool cost." |

## Expected result

- **Verdict:** 3 points:
  1. Vorspeisen · Lachsforelle · line 2: doubled "mit".
  2. Hauptgerichte · Zanderfilet · line 2: "Patatenpüree" → Batatenpüree (reading error, already corrected in the translations).
  3. Dessert: closing "***" missing.
- **EN** (excerpt): Starters / Smoked salmon trout / on cucumber salad with sour cream / … / Rosé-roasted saddle of venison / … / Pan-fried pike-perch fillet / on savoy cabbage with sweet potato purée / and white wine foam
- **FR** (excerpt): Hors d'œuvres / Truite saumonée fumée / sur salade de concombres avec crème aigre / … / Filet de sandre rôti / sur chou de Milan avec purée de patate douce / et mousse au vin blanc
- **IT** (excerpt): Antipasti / Trota salmonata affumicata / su insalata di cetrioli con panna acida / … / Filetto di lucioperca scottato / su verza con purè di patate dolci / e spuma al vino bianco
- Full expected output: `skill/hotel-guest-docs/examples/evening-menu.md`.

## If they ask for more (optional, +30 s each)

- **"What if something changes after printing?"** Type: `Hat sich was geändert? Hirschrücken jetzt mit Wacholdersauce statt Preiselbeersauce.` → Claude returns only that line in EN/FR/IT with course, dish and line.
- **"Can it handle messy input?"** Paste the sommelier sheet from `examples/wine-list.md` → four cards; the only question back is the missing vintage, because the system never invents facts.

## Fallback

If the connection is slow, switch to the second tab and walk through the expected output with the same script.

# Example: kids' programme · Hotel Alpenrose ★★★★★S, Tyrol

Fictional day from a Kids Club plan (one day shown; a real plan has seven days, a title and notices). The German contains typical house corrections.

## Input (German plan, one day)

```
Mittwoch, 14. Oktober 2026
09:00 Uhr - 10.00 Uhr Aufgewacht und mitgemacht
10.00 Uhr – 11.00 Uhr Mensch Ärgere Dich nicht
11.00 Uhr – 12.00 Uhr Stopp-Tanz
12.00 Uhr – 15.00 Uhr PAUSE
15.00 Uhr – 16.00 Uhr Basteln mit Wäscheklammern
16.00 Uhr – 18.00 Uhr Daraus Basteln wir Blumentopfstecker
18.00 Uhr – 18.30 Uhr Abendessen am Kindertisch
18.30 Uhr – 19.30 Uhr Stille Post
19.30 Uhr – 21.00 Uhr Kino-Abend

Bitte melden Sie Ihre Kinder TÄGLICH bis spätestens 15 Uhr zum Kinderessen bei uns IM SPIELZIMMER an!
```

## Expected output

Deutsch: 14. Oktober 2026 ist ein Mittwoch ✓. Hauskorrekturen gesetzt: Uhrzeit und Gedankenstrich (erste Zeile), Schreibweisen (Mensch ärgere dich nicht, Stopptanz, Daraus basteln, Kinoabend), „Wir"-Form, Anmeldetext in der freigegebenen Fassung.

**Deutsch (korrigiert)**
```
Mittwoch, 14. Oktober 2026
09.00 Uhr – 10.00 Uhr Aufgewacht und mitgemacht
10.00 Uhr – 11.00 Uhr Mensch ärgere dich nicht
11.00 Uhr – 12.00 Uhr Stopptanz
12.00 Uhr – 15.00 Uhr PAUSE
15.00 Uhr – 16.00 Uhr Wir basteln mit Wäscheklammern
16.00 Uhr – 18.00 Uhr Daraus basteln wir Blumentopfstecker
18.00 Uhr – 18.30 Uhr Abendessen am Kindertisch
18.30 Uhr – 19.30 Uhr Stille Post
19.30 Uhr – 21.00 Uhr Kinoabend

Bitte melden Sie Ihre Kinder TÄGLICH bis spätestens 15.00 Uhr zum Abendessen am Kindertisch bei uns IM KINDERCLUB an!
```

**English**
```
Wednesday, October 14th, 2026          (th superscript)
09.00 am – 10.00 am Wake up and join in!
10.00 am – 11.00 am Ludo
11.00 am – 12.00 pm Musical statues
12.00 pm – 03.00 pm BREAK
03.00 pm – 04.00 pm Crafting with clothes pegs
04.00 pm – 06.00 pm Let's turn them into flowerpot decorations
06.00 pm – 06.30 pm Dinner at the children's table
06.30 pm – 07.30 pm "Telephone" (whispering game)
07.30 pm – 09.00 pm Cinema evening

Please register your child for dinner at the children's table DAILY in our KIDS CLUB by 3.00 pm at the latest!
```

Files: `DE_10_10_-_16_10_Plan_2.docx` (corrected) and `EN_10_10_-_16_10_Programme_2.docx`, both in the original layout with graphics unchanged.

## Notes on the decisions

- Game names from the glossary (Ludo, Musical statues, "Telephone"), not translated literally.
- Craft items: German "Wir" form, English from the approved glossary.
- The registration notice is the approved standard text in both languages, not a new translation.
- English keeps the plan's time style (HH.MM am/pm, en dash), which differs from the weekly programme.

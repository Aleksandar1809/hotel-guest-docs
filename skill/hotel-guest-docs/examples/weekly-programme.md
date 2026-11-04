# Example: weekly programme · Hotel Alpenrose ★★★★★S, Tyrol

Fictional week, Monday 12 to Saturday 17 October 2026. Staff attach the last printed DE and EN Word files (week of 5 to 10 October) and the text of this week's scans.

## Input (scans, transcribed; deviations from last week)

```
Fitnesstrainer:
Mi 15:30-16:00 Faszien Training
Mi 17:30 Zirbe-Bergzeder Aufguss (statt Kiefer-Zirbe)
Fr 15:30-16:00 Fit Boxen
Fr 16:30 Fit Boxen
Fr 18:30 HONIG Aufguss

Yogalehrerin:
Di kein Yoga
Do 16:30 Yoga - Atemweite „Weite spüren"
Do 18:00 Tiefenentspannung - Sternen Stille „Sanft in die Nacht"

Outdoor-Guide:
Fr frei
```

Approved catalogue entries (fictional, from the hotel's yoga catalogue):

```
Yoga - Atemweite „Weite spüren" | Ruhige Bewegungen und bewusster Atem schenken neue Leichtigkeit.
Yoga - Mountain Breath "Feel the vastness" | Calm movements and conscious breathing bring new lightness.
Tiefenentspannung - Sternenstille „Sanft in die Nacht" | Leise Klänge und eine geführte Reise lassen den Tag ausklingen.
Deep Relaxation - Moon Calm "Gently into the night" | Soft sounds and a guided journey bring the day to a close.
```

## Expected reply

**Findings in the scans**
1. Yoga sheet, Thursday: "Sternen Stille" → **Sternenstille** (as in the catalogue).
2. Fitness sheet: "Faszien Training" → Faszientraining · "Zirbe-Bergzeder" → „Zirbe & Bergzeder" · "HONIG" → Honig.
3. **Question:** Friday "Fit Boxen" appears at 15:30 and at 16:30. Which time is right? Until you answer, the file keeps 15:30 (as last week).

**Patches to the last printed version (DE / EN)**

| Day | DE | EN |
|---|---|---|
| Title | vom 12. bis 17. Oktober 2026 | from 12th to 17th October 2026 |
| Headings | Montag, 12. Oktober 2026 … Samstag, 17. Oktober 2026 | Monday, 12th October 2026 … Saturday, 17th October 2026 |
| Tuesday | remove Yoga block and Tiefenentspannung block | remove Yoga block and Deep Relaxation block |
| Wednesday | 15:30 - 16:00 Uhr Faszientraining | 3:30 - 4:00 p.m. Fascia Training |
| Wednesday | 17:30 Uhr „Zirbe & Bergzeder" - Aufguss in der Gartensauna | 5:30 p.m. "Swiss pine & Mountain cedar" - Infusion in the garden sauna |
| Thursday | insert after the 16:30 infusion: 16:30 - 17:45 Uhr **Yoga - Atemweite** „Weite spüren" / Ruhige Bewegungen und bewusster Atem schenken neue Leichtigkeit. / (Anmeldung bis 10:30 Uhr am selben Tag, Teilnehmer: max. 6 Personen) | 4:30 - 5:45 p.m. **Yoga - Mountain Breath** "Feel the vastness" / Calm movements and conscious breathing bring new lightness. / (Registration by 10:30 a.m. on the same day, participants: max. 6 people) |
| Thursday | insert after the 17:30 infusion: 18:00 - 18:30 Uhr **Tiefenentspannung - Sternenstille** „Sanft in die Nacht" / Leise Klänge und eine geführte Reise lassen den Tag ausklingen. / (registration line) | 6:00 - 6:30 p.m. **Deep Relaxation - Moon Calm** "Gently into the night" / Soft sounds and a guided journey bring the day to a close. / (registration line) |
| Thursday | spacer before the heading `w:sz 24` | spacer before the heading `w:sz 16` |
| Friday | remove InfoPoint and the „Wunschkonzert" block | remove InfoPoint and the "Choose Your Day" block |
| Friday | 18:30 Uhr „Honig" - Aufguss in der Gartensauna | 6:30 p.m. "Honey" - Infusion in the garden sauna |

Yoga title lines: name bold 24 pt, motto regular 18 pt on the same line, no hyphen between them.

**Final check**
1. Weekdays and title range match the calendar ✓; EN suffixes superscript ✓
2. Infusions DE ↔ EN in pairs, same number of times ✓
3. Yoga only on Thursday and Saturday, per catalogue, title line formatted ✓
4. InfoPoints = outdoor guide's days (Mon–Thu) ✓; hut evening on Monday ✓; Tuesday hike start = meeting time ✓
5. EN: no leading zeros, a.m./p.m., British spelling ✓
6. DE: recurring errors fixed ✓
7. 2 pages in the preview; Thursday is tight. May look different in Word (font Gadugi). Please check page 2 there.

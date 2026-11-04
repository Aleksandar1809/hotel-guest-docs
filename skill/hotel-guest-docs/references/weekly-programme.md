# Weekly programme (guest activity programme)

Weekly programme of fitness classes, sauna infusions, yoga, guided hikes and bike days, and the hut evening, in German and English. A3 landscape, two columns, embedded graphics, **exactly 2 pages**.

## Roles that send material (edit per hotel)

- **Fitness trainer:** classes and infusions (scan of their weekly sheet).
- **Outdoor guide:** InfoPoint, hiking days, bike days, "Choose Your Day".
- **Hiking guide:** the Tuesday hike.
- **Yoga teacher:** yoga days and themes (scan of their theme sheet).
Material arrives as **scans**; staff do not forward original files.

## Workflow

1. Staff send the scans (plus a new hike if any) and the **last printed** Word files DE and EN.
2. **Patch the last printed version.** Never rebuild, never use older weeks as the base. Staff's own Word edits must survive.
3. Report anything odd in the scans briefly: typos, contradictions, new terms (with a proposal + question).
4. Staff check in Word; then **one** final check (staff say what they changed).
- Preview tools without the template font (Gadugi) break lines differently. **Word is authoritative.** Every layout note carries "may look different in Word".
- Communication: short, direct, corrections without long explanations.

Technique: unpack the .docx, edit `word/document.xml`, repack. Merge Word's split text runs before replacing text, or replacements fail silently.

## Typical changes

| Change | What to do |
|---|---|
| New week | All day dates + title. DE "Montag, 07. Oktober 2026", EN "Monday, 7th October 2026" (suffix superscript, no leading zero) |
| Month change within the week | Subtitle DE and EN at 20 pt (`w:sz 40`) so it fits on one line |
| Saturday included | Title range ends with Saturday |
| Infusion new/changed | Glossary below; unknown → proposal + question |
| Yoga day/theme | Texts from the approved yoga catalogue; insert/remove blocks by time between the infusions |
| Yoga teacher absent | Remove all yoga blocks |
| Outdoor guide absent | Remove the InfoPoint and the guide's block of that day; hut evening and the hiking guide stay |
| New hike | Text into the existing box (indents of the master), swap the photo, adjust the frame height; start time = meeting time |
| Thursday with yoga | Shrink the spacer paragraph before the Thursday heading: DE `w:sz 24`, EN `w:sz 16` (default 40) |
| Blocks breaking apart | Keep boxes, yoga blocks and the start of a day together with "keep with next"; column breaks only sparingly (risky in Word) |

Always: **exactly 2 pages**.

## German house style

- Infusion: „Lavendel" - Aufguss in der Gartensauna
- Yoga title line: **name bold 24 pt** + „Motto" regular 18 pt, on the same line, no hyphen between them. Hyphens only inside the name, as the yoga teacher writes it. The name never in quotes. "Tiefenentspannung - …" with a simple hyphen. The descriptive sentence goes on the line below.
- Recurring errors in the yoga teacher's sheets (examples): "Licht Moment" → Lichtmoment; a sentence break missing before "Klanginstrumente…".
- The fitness trainer's spellings → house style: Heublume → Heublumen · wilde Orange → Wilde Orange · HONIG → Honig · Orange / Zitrone → Orange & Zitrone · Kiefer-Zirbe → Kiefer & Zirbe · Edelminze Zitrone → Edelminze & Zitrone · Eukalyptus Aufguss → Eukalyptus · Faszien Training → Faszientraining · Funktionales Training → Funktional Training · Bauch-Beine-Po → Bauch, Beine, Po · Swing stick → Swing Stick
- Heights with thousands dot: 2.017 m
- Check standard texts: "ein erlebnisreicher Ausflug" (lower case), "Programm ist wetterabhängig" (lower case).
- Leave as is (intentional): "Bike Tag" in body text (title "Bike Day"), "Bike Verleih Kostenpflichtig".

## English house style

- Title Case for activity names; motto in sentence case in "…"; never German „ in EN.
- Times: 8:00 - 8:30 a.m. · 4:30 p.m. · from 9:30 a.m. (no leading zero, a.m./p.m. with dots, only at the end of a range).
- Infusion: "Lavender" - Infusion in the garden sauna.
- British spelling: programme, specialities, cosily, tranquillity, centre, centred, revitalise, colour.
- Abs, Legs, Glutes (no ampersand) · title "Your Weekly Programme", in body text "weekly programme".
- Heights: 2,017 m · Places, alpine huts and valleys are not translated.
- Deliberate deviations approved by the yoga teacher are kept (e.g. "Yoga Nidra" motto "For body & soul"; "Yogaflow zum Ankommen" = just "Yoga Flow").

## Yoga catalogue

Yoga 16:30 - 17:45 Uhr / 4:30 - 5:45 p.m. · Deep relaxation 18:00 - 18:30 Uhr / 6:00 - 6:30 p.m.
Registration line: (Anmeldung bis 10:30 Uhr am selben Tag, Teilnehmer: max. 6 Personen) / (Registration by 10:30 a.m. on the same day, participants: max. 6 people)
Schema per theme: **Name** „Motto" | text, in DE and EN. The house keeps its approved themes (typically 9) as a catalogue; texts are copied, never re-translated.

## Glossary DE → EN

**Infusions:** Almkräuter → Alpine herbs · Almrose → Alpine rose · Apfel → Apple · Bergkräuter → Mountain herbs · Edelminze & Zitrone → Noble mint & Lemon · Eukalyptus → Eucalyptus · Fichtennadel → Spruce needle · Heublumen → Alpine hay flower · Honig → Honey · Kamille → Chamomile · Kiefer & Zirbe → Pine & Swiss pine · Latschenkiefer → Mountain pine · Lavendel → Lavender · Lemongrass → Lemongrass · Orange & Zitrone → Orange & Lemon · Wilde Orange → Wild orange · Zirbe & Bergzeder → Swiss pine & Mountain cedar
**Steam bath:** Aloe Vera - Peeling im Japanischen Dampfbad → Aloe Vera - Scrub in the Japanese steam bath · Honig - Meersalz Peeling → Honey Sea Salt Scrub
**Classes:** Aqua Fitness Wassergymnastik im Familienbad → Aqua Fitness aqua gymnastics in the family pool · Funktional Training → Functional Training · Faszientraining → Fascia Training · Sixpack Training → Sixpack Training · Bauch, Beine, Po → Abs, Legs, Glutes · Stretch & Relax → Stretch & Relax · Fit Boxen → Fit Boxing · Rückenfit → Back Fitness · Stretching → Stretching · Swing Stick → Swing Stick
**Outdoor guide** (standard texts in the template): Infopoint mit Guide [Name] → InfoPoint with Guide [Name] · Wandertag mit Wanderführer [Name] → Hiking Day with Hiking Guide [Name] · Bike Day mit Guide [Name] → Bike Day with Guide [Name] · „Wunschkonzert" mit Guide [Name] → "Choose Your Day" with Guide [Name] · Bike Verleih Kostenpflichtig → Bike rental is available for a fee.
**Hiking guide:** mit Wanderführerin [Name] → with Hiking Guide [Name]; start = meeting time.
**Hut evening** (Mondays) → Hut Evening at the [hut name]: standard text in the template.

## Final check (every week)

1. Weekdays against the calendar, title range; EN suffixes (1st, 2nd, 3rd … 21st, 22nd, 23rd) superscript.
2. All infusions DE ↔ EN in pairs per glossary; the same number of times on both sides.
3. Yoga per catalogue; title line formatted as above.
4. Number of InfoPoints = outdoor guide's days; hut evening present; hiking guide start = meeting time.
5. EN: no leading zeros, a.m./p.m., no „, British spelling.
6. DE: recurring errors (above).
7. Exactly 2 pages; layout notes with the Word caveat.

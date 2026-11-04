# Example: morning newsletter · Hotel Alpenrose ★★★★★S, Tyrol

Fictional issue for Friday, 16 October 2026. The newsletter is German only. The block library and weekly plan below are fictional excerpts.

## Block library (excerpt, fictional)

```
## S07 · Herbstmorgen
**Art:** Titelseite
Wenn Nebel aus den Tälern steigt
und Gold auf allen Gipfeln liegt,
dann wird der Morgen still und weit –
ein Tag, der sich zum Staunen neigt.
— Verfasser unbekannt

## S21 · Langsam gehen
**Art:** Innenseite
Wer langsam geht, sieht mehr vom Berg.

## W03 · Richtig abkühlen
**Kategorie:** Sauna
Nach jedem Saunagang zuerst an die frische Luft, dann ins Tauchbecken –
so fühlen Sie sich herrlich erfrischt.

## W11 · Glow nach dem Wandern
**Kategorie:** Beauty
Unsere Feuchtigkeitsmaske mit Edelweiß-Extrakt schenkt der Haut
nach einem Tag in der Höhe neue Frische.

## W24 · Sanft in den Tag
**Kategorie:** Bewegung
Fünf Minuten Dehnen am offenen Fenster – der schönste Start in einen aktiven Tag.

## W30 · Lesezeit am Kamin
**Kategorie:** Ruhe
Ein gutes Buch, ein Tee aus Bergkräutern und das Knistern des Feuers in unserer Kaminlounge.

## V05 · Badesalz Zirbe
**Marke · Rubrik:** Alpenrose Manufaktur · Für zu Hause
**Unterzeile:** Ein Stück Bergwald für Ihr Bad
**Bild:** B12
Grobes Steinsalz mit ätherischem Zirbenöl – ein Duft, der an Ihren Urlaub erinnert.

## T08 · Zum Gamsbodensee
**Länge · Dauer:** 7,5 km · 2½ Std.
**Bild:** B19
Vom Hotel über den Waldweg zur Sonnmoosalm und weiter zum stillen Bergsee. Leicht, ideal für Familien.

## H05 · „Gipfeltag" mit unserem Outdoor-Guide
**Info:** Freitag · ab 09:30 Uhr
**Bild:** B23
Wandern oder Biken – Sie wählen, unser Guide plant den Tag mit Ihnen.

## H12 · Herbstferien im Kids Club
Von 24. Oktober bis 1. November täglich erweitertes Programm im Kids Club.
```

## Weekly plan (fictional excerpt)

```
Freitag: 08:00 – 08:30 Aqua Fitness · 09:00 – 09:45 Funktional Training · 10:30 – 11:00 Faszientraining ·
15:30 – 16:00 Fit Boxen · 16:30 „Lemongrass"-Aufguss · 17:30 „Wilde Orange"-Aufguss · 18:30 „Eukalyptus"-Aufguss · Extra: H05
Samstag: 16:30 – 17:45 Yoga (Anm.) · 17:30 „Honig"-Aufguss · 18:00 – 18:30 Tiefenentspannung (Anm.)
```

## Input (as sent by staff)

```
Morgenpost Fr 16.10.2026
Wetter: B · C · F · 4° / 15° · Schneefallgrenze 2.400 m
Überschrift: Freundlicher Start, später Schauer
Wettertext: Der Vormittag beginnt sonnig und klar. Ab Mittag ziehen von Westen Wolken auf, gegen Abend sind einzelne Regenschauer möglich.
Bausteine: S07 · S21 · W03 · W11 · W24 · W30 · V05 · T08 · H12
Abweichungen: Fit Boxen fällt aus. 17:30 Kamille statt Wilde Orange.
Abendmenü: (deutsches Menü vom Tag, siehe evening-menu)
```

## Expected output (content sheet)

```
SHEET 1 · OUTSIDE
Menu flap:        Abendmenü · FREITAG / 16. OKTOBER
                  Vorspeisen · Suppen · Salate · Hauptgerichte · Dessert – wörtlich wie geliefert · Käse
Wellness courier: 01 SAUNA · Richtig abkühlen · (W03)
                  02 BEAUTY · Glow nach dem Wandern · (W11)
                  03 BEWEGUNG · Sanft in den Tag · (W24)
                  04 RUHE · Lesezeit am Kamin · (W30)
                  Produkt-Box: ALPENROSE MANUFAKTUR · FÜR ZU HAUSE · Badesalz Zirbe ·
                  Ein Stück Bergwald für Ihr Bad · Text V05 · Bild B12
Cover:            16. · Oktober 2026 · FREITAG
                  Gedicht: HERBSTMORGEN · 4 Zeilen wie geliefert · Verfasser unbekannt

SHEET 2 · INSIDE
Weather band:     07:00 B (Heiter) 4° min · 12:00 C (Wolkig) 15° max · 17:00 F (Regenschauer) SCHNEEFALLGRENZE 2.400 M
The morning:      Freundlicher Start, später Schauer · Wettertext wörtlich
                  Spruch: „Wer langsam geht, sieht mehr vom Berg." (S21)
                  Wandertipp: Zum Gamsbodensee · 7,5 km · 2½ Std. · Text T08 · Bild B19
The day:          08:00 Aqua Fitness · 09:00 Funktional Training · 10:30 Faszientraining
                  (Fit Boxen entfällt)
                  Tagesextra: FREITAG · AB 09:30 UHR · „Gipfeltag" mit unserem Outdoor-Guide · Text H05 · Bild B23
The evening:      16:30 Lemongrass · 17:30 Kamille · 18:30 Eukalyptus
                  „Das Abendmenü finden Sie auf der Rückseite."
                  Vorschau Samstag, 17. Oktober: 16:30 Yoga (Anmeldung bis 10:30 Uhr) · 17:30 Honig-Aufguss ·
                  18:00 Tiefenentspannung (Anmeldung bis 10:30 Uhr)
                  Hausinfo: Herbstferien im Kids Club · Text H12

CHECK:            Panels filled; all texts word for word.
                  Overflow risk: "The morning" (weather text + hike tip) – image must stay ≥ 36 mm.
                  If it does not fit, do not shorten any text; ask which element to drop.
```

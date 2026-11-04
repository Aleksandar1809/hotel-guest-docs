# Example: wine card · Hotel Alpenrose ★★★★★S, Tyrol

Fictional sommelier sheet with fictional estates and prices. It shows the usual problems: short headings, a two-digit vintage, a missing vintage, missing countries and quantities, casual wording, and a bar manager's recommendation.

## Input (sommelier's info sheet, as sent)

```
Weinempfehlung Fr 16.10.

Aperitif
Sekt Brut Rosé, Sektkellerei Hainblick, Kamptal – Glas 10,20

weiss
22 Grüner Veltliner Federspiel "Felsenhang" Weingut Lindenhain, Wachau
toller Wein, würzig frisch mit Noten von weißem Pfeffer und grünem Apfel passt super zum Zander
Flasche 54,90

Rot
Blaufränkisch Reserve, Weingut Mohnleiten, Mittelburgenland Österreich
Dunkle Kirsche, Brombeere und ein Hauch Zedernholz, samtige Tannine und langer Abgang.
0,75 Flasche 67,60

Süss
2019 Beerenauslese Weingut Schilfrain Neusiedlersee
Honig, Marille und kandierte Orange – ein toller Süßwein.
Glas 11,90

Digestif
Marillenbrand, Destillerie Ahornegg, Tirol
Glas 7,60

Barchef empfiehlt: Espresso Martini (Wodka, Kaffeelikör, Espresso) 15,60
```

## Expected reply

Vier Karten fertig. **Rotwein Blaufränkisch Reserve (Mohnleiten): Jahrgang fehlt auf dem Blatt, bitte nachreichen.** Über die Rechtschreibung hinaus angepasst: Weißwein-Text („toller Wein" → „Ein herrlicher Wein", „passt super" → „passt wunderbar") und Dessertwein-Text („toller Süßwein" → „herrlicher Süßwein").

## Expected cards

**Wein 16.10 (DE)**
```
Wir dürfen Ihnen zum heutigen Menü
gerne folgende Weine empfehlen:

Aperitif
Sekt Brut Rosé
Hainblick, Kamptal, Österreich
            Glas   €   10,20

Weißwein
2022 Grüner Veltliner Federspiel „Felsenhang"
Lindenhain, Wachau, Österreich
Ein herrlicher Wein, würzig-frisch, mit Noten
von weißem Pfeffer und grünem Apfel –
passt wunderbar zum Zander.
   0,75l Flasche   €   54,90

Rotwein
Blaufränkisch Reserve
Mohnleiten, Mittelburgenland, Österreich
Dunkle Kirsche, Brombeere und ein Hauch Zedernholz,
samtige Tannine und langer Abgang.
   0,75l Flasche   €   67,60

Dessertwein
2019 Beerenauslese
Schilfrain, Neusiedlersee, Österreich
Honig, Marille und kandierte Orange –
ein herrlicher Süßwein.
         5cl Glas   €   11,90

Digestif
Marillenbrand
Ahornegg, Österreich
         2cl Glas   €    7,60

Unser Barchef empfiehlt Ihnen nach dem Essen
noch einen köstlichen:
Espresso Martini
(Wodka, Kaffeelikör und Espresso)
            Glas   €   15,60

Tirol, am 16. Oktober 2026
[Pflichthinweis des Hauses]
```

**Wine 16.10 (EN)**
```
We would like to recommend
the following wines:

Aperitif
Sekt Brut Rosé
Hainblick, Kamptal, Austria
           glass   €   10,20

White wine
2022 Grüner Veltliner Federspiel "Felsenhang"
Lindenhain, Wachau, Austria
   0,75l bottle   €   54,90

Red wine
Blaufränkisch Reserve
Mohnleiten, Mittelburgenland, Austria
   0,75l bottle   €   67,60

Dessert wine
2019 Beerenauslese
Schilfrain, Neusiedlersee, Austria
        5cl glass   €   11,90

Digestif
Apricot brandy
Ahornegg, Austria
        2cl glass   €    7,60

After dinner, our bar manager
recommends a delicious:
Espresso Martini
(vodka, coffee liqueur and espresso)
           glass   €   15,60

Tyrol, October 16th, 2026        (th superscript)
[house legal notice]
```

**Vin 16.10 (FR)**
```
Pour accompagner votre repas,
nous vous proposons les vins suivants :

Apéritif
Sekt Brut Rosé
Hainblick, Kamptal, Autriche
           verre   €   10,20

Vin blanc
2022 Grüner Veltliner Federspiel « Felsenhang »
Lindenhain, Wachau, Autriche
 0,75l bouteille   €   54,90

Vin rouge
Blaufränkisch Reserve
Mohnleiten, Mittelburgenland, Autriche
 0,75l bouteille   €   67,60

Vin de dessert
2019 Beerenauslese
Schilfrain, Neusiedlersee, Autriche
        5cl verre   €   11,90

Digestif
Eau-de-vie d'abricot
Ahornegg, Autriche
        2cl verre   €    7,60

Après le repas, notre chef de bar
vous recommande un délicieux :
Espresso Martini
(vodka, liqueur de café et espresso)
           verre   €   15,60

Tyrol, le 16 octobre 2026
```

**Vino 16.10 (IT)**
```
Con piacere vi consigliamo
i seguenti vini per il menù di oggi:

Aperitivo
Sekt Brut Rosé
Hainblick, Kamptal, Austria
       bicchiere   €   10,20

Vino bianco
2022 Grüner Veltliner Federspiel «Felsenhang»
Lindenhain, Wachau, Austria
 0,75l bottiglia   €   54,90

Vino rosso
Blaufränkisch Reserve
Mohnleiten, Mittelburgenland, Austria
 0,75l bottiglia   €   67,60

Vino da dessert
2019 Beerenauslese
Schilfrain, Neusiedlersee, Austria
    5cl bicchiere   €   11,90

Digestivo
Acquavite di albicocca
Ahornegg, Austria
    2cl bicchiere   €    7,60

Dopo cena, il nostro barman
vi consiglia un delizioso:
Espresso Martini
(vodka, liquore al caffè ed espresso)
       bicchiere   €   15,60

Tirolo, il 16 ottobre 2026
```

## What was fixed silently

- Headings completed: "weiss" → Weißwein, "Rot" → Rotwein, "Süss" → Dessertwein.
- 22 → 2022; quotes "…" → „…" (and per language in EN/FR/IT).
- "Weingut …" / "Sektkellerei …" / "Destillerie …" moved to the producer line; country added; distillery without region.
- Quantities completed: bottle → 0,75l Flasche, sweet wine by the glass → 5cl Glas, brandy → 2cl Glas; "0,75 Flasche" → 0,75l Flasche.
- Missing comma in the white-wine description.
- Mixed drink: name alone, recipe in brackets, bar manager announcement above it in all four languages.
- Only the missing vintage is reported: it cannot be completed without inventing it.

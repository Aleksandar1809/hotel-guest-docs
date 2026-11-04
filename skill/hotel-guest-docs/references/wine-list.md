# Wine card (daily wine recommendation)

The sommelier sends a daily info sheet in German. It is often incomplete or inconsistent: missing or short headings, two-digit vintages, missing quantities or countries, casual wording. The result is four one-page cards in one pass: **Wein** (DE), **Wine** (EN), **Vin** (FR), **Vino** (IT).

## House profile (edit per hotel)

| Item | DE | EN | FR | IT |
|---|---|---|---|---|
| File name | Wein DD.MM.docx | Wine DD.MM.docx | Vin DD.MM.docx | Vino DD.MM.docx |
| Intro (2 lines) | Wir dürfen Ihnen zum heutigen Menü / gerne folgende Weine empfehlen: | We would like to recommend / the following wines: | Pour accompagner votre repas, / nous vous proposons les vins suivants : | Con piacere vi consigliamo / i seguenti vini per il menù di oggi: |
| Bar manager announcement (2 lines, above the drink) | Unser Barchef empfiehlt Ihnen nach dem Essen / noch einen köstlichen: | After dinner, our bar manager / recommends a delicious: | Après le repas, notre chef de bar / vous recommande un délicieux : | Dopo cena, il nostro barman / vi consiglia un delizioso: |
| Place/date line | <Ort>, am 16. Oktober 2026 | <Place>, October 16th, 2026 (suffix superscript) | <Lieu>, le 16 octobre 2026 (le 1er: "er" superscript) | <Luogo>, il 16 ottobre 2026 (il 1°; l'8, l'11) |
| Legal notice line | yes (house wording) | yes (house wording) | no | no |

Fixed vintages: some wines always carry the same vintage regardless of the sheet. Keep that list in the house profile and apply it silently.

## Workflow

1. **Known wine** (already in the wine register): take name, producer line and the **approved German description from the register**, even if the sheet brings an older text. Price and vintage always come from today's sheet.
2. **New wine**: build name, producer line and description from the sheet with the house rules below. New wines are added to the register when staff ask for an updated register.
3. Order the categories, complete headings, translate EN/FR/IT with the tables, set the four cards, check, deliver.
4. **Reply:** the four cards plus one or two sentences. Report only essentials: a missing or doubtful vintage, price or wine, and any edit beyond pure spelling. No correction lists. Errors on the sheet are fixed silently.

When the generator script is available (production setup), staff send only a short day list and the script does translation, line wrapping, spacing and checks. Do not analyse templates, write your own scripts or set EN/FR/IT by hand in that setup.

## Categories and order

| DE | EN | FR | IT |
|---|---|---|---|
| Aperitif | Aperitif | Apéritif | Aperitivo |
| Weißwein | White wine | Vin blanc | Vino bianco |
| Roséwein | Rosé wine | Vin rosé | Vino rosato |
| Rotwein | Red wine | Vin rouge | Vino rosso |
| Aus dem Raritätenkeller | From the rarity cellar | De la cave des raretés | Dalla cantina delle rarità |
| Dessertwein | Dessert wine | Vin de dessert | Vino da dessert |
| Digestif | Digestif | Digestif | Digestivo |

Always in this order. Missing or shortened headings ("weiss", "Rot", "Süss") are completed.

## House rules

**Name line**
- Vintage first, four digits: 22 → 2022, 13/17 → 2013/2017, XXII → 2022, "00/09" → 2000/2009.
- Grape abbreviations in brackets as delivered. Capitals turned into normal spelling. Correct accents and apostrophes (Angélus, Côte d'Or, dell'Ornellaia, Graham's, Hors d'Âge). N° without space (N°1).
- German quotes „…"; the other languages convert them (EN "…", FR « … » with narrow no-break space, IT «…»).
- "Champagner" → Champagne in EN/FR/IT. "Süß" → Sweet / doux / dolce. Everything else in the name stays as in German (appellations, grape names, cuvée names). Generic product names (e.g. a fruit brandy) may get a translated name per language.
- An aperitif's brand name goes in the name line before the product ("Contratto Bitter mit frischem Orangensaft"); the producer line is then dropped.
- No producer named (e.g. a branded bitter) → no producer line.

**Producer line**
- Estate, place, region, country. **Always the country.** Only the house named → add only the country.
- Distilleries: place and country, no region.
- Nothing invented. A producer inside the name moves to the producer line.
- Too long for one line → drop a duplicated region (e.g. a region already in the name).

**Quantities and prices**
- No space: 0,1l · 5cl · 0,75l · 1,5l. Units: Glas/Flasche → glass/bottle · verre/bouteille · bicchiere/bottiglia.
- Missing quantity: bottle price → 0,75l Flasche; sweet wine by the glass → 5cl Glas; spirit/brandy → 2cl Glas; liqueur, calvados → 4cl Glas; otherwise just "Glas".
- Twisted price lines are put right. Several sizes or vintages → one price line each, vintage as third field.
- Prices and quantities are identical in all four languages, with decimal comma, € sign before the amount (aligned by tabs).

**Description (German only)**
- Never shorten, never rewrite. Verbless tasting notes are house style.
- Correct only spelling, punctuation and grammar; repair structurally broken sentences minimally; raise casual wording ("toller Süßwein" → "ein herrlicher Süßwein").
- Report any edit beyond spelling in the reply.

**Mixed drinks**
- Name alone in the name line (13 pt), recipe in brackets below (11 pt), both underlined, in all four languages; recipe translated per language.
- Bar manager's recommendation: the two-line announcement above the name, 13 pt italic, not bold, not underlined, ending with a colon, in all four languages.

**Date line:** Italian with elision: l'8, l'11; il 1°. French le 1er. English ordinal suffix superscript.

## Translation tables

**Countries:** Österreich → Austria / Autriche / Austria · Deutschland → Germany / Allemagne / Germania · Italien → Italy / Italie / Italia · Frankreich → France / France / Francia · Spanien → Spain / Espagne / Spagna · Portugal → Portugal / Portugal / Portogallo · Schweiz → Switzerland / Suisse / Svizzera · Ungarn → Hungary / Hongrie / Ungheria · Slowenien → Slovenia / Slovénie / Slovenia · Griechenland → Greece / Grèce / Grecia

**Regions:** Südtirol → South Tyrol / Haut-Adige / Alto Adige · Toskana → Tuscany / Toscane / Toscana · Piemont → Piedmont / Piémont / Piemonte · Venetien → Veneto / Vénétie / Veneto · Friaul → Friuli / Frioul / Friuli · Lombardei → Lombardy / Lombardie / Lombardia · Provence → Provence / Provence / Provenza · Loire → Loire / Loire / Loira · Mosel → Mosel / Moselle / Mosella · Baden → Baden / Pays de Bade / Baden · Wien → Vienna / Vienne / Vienna · Südsteiermark → South Styria / Styrie du Sud / Stiria meridionale · Andalusien → Andalusia / Andalousie / Andalusia · Tirol → Tyrol / Tyrol / Tirolo · Burgund → Burgundy / Bourgogne / Borgogna · Elsass → Alsace / Alsace / Alsazia · Sizilien → Sicily / Sicile / Sicilia · Sardinien → Sardinia / Sardaigne / Sardegna · Apulien → Apulia / Pouilles / Puglia · Kampanien → Campania / Campanie / Campania · Umbrien → Umbria / Ombrie / Umbria · Abruzzen → Abruzzo / Abruzzes / Abruzzo · Marken → Marche / Marches / Marche · Ligurien → Liguria / Ligurie / Liguria · Katalonien → Catalonia / Catalogne / Catalogna · Steiermark → Styria / Styrie / Stiria · Weststeiermark → West Styria / Styrie occidentale / Stiria occidentale · Niederösterreich → Lower Austria / Basse-Autriche / Bassa Austria

**Unchanged in all languages:** Wachau, Kremstal, Kamptal, Wagram, Carnuntum, Weinviertel, Thermenregion, Neusiedlersee, Mittelburgenland, Burgenland, Leithaberg, Eisenberg, Vulkanland Steiermark, Traisental, Champagne, Bordeaux, Saint-Émilion, Côtes du Rhône, Côte de Beaune, Côte de Nuits, Chablis, Médoc, Pauillac, Collio, Bolgheri, Chianti, Chianti Classico, Trentino, Lugana di Sirmione, Montalcino, Barolo, Barbaresco, Valpolicella, Franciacorta, Maremma, Rheingau, Rheinhessen, Pfalz, Nahe, Franken, Ahr, Württemberg, Rioja, Ribera del Duero, Priorat, Douro, Jerez, Tokaj.
A region in neither list → translate carefully and mention it in the reply so it can be added to the table.

**Months:** EN January … December · FR janvier … décembre (lower case) · IT gennaio … dicembre (lower case).

## Card structure (per language)

```
<Intro line 1>
<Intro line 2>

<Category>
<Name line>                      bold, underlined
<Producer line>                  bold
<Description lines>              DE only, italic, max. 13 cm per line
<quantity>   €   <price>         one line per size/vintage

<Bar manager announcement, 2 lines>   (only for the recommended drink)
<Drink name>                     underlined
(<recipe>)                       underlined, smaller

…
<Place, date>
<Legal notice>                   DE and EN only
```

## Layout (production .docx)

- One A4 page per language, never two. Times New Roman italic, centred, character spacing 1.5 pt.
- Sizes: category 18 pt bold; name 13 pt bold underlined; producer 11 pt bold; description 10.5 pt; price line 10.5 pt with tabs (quantity right-aligned, € left, price decimal-aligned).
- Descriptions wrapped at 13 cm; avoid ending a line on short function words (und, mit, am, im, in, von, …).
- White space goes between the wines, not at the foot of the page. The ornament is centred in all languages.
- German card only: an empty 8 pt paragraph at the very top, and no empty paragraph directly above the ornament.
- Price blocks with vintages (several sizes or vintages): vintage, quantity and price centred as one block, even gap between vintage and quantity, in all four languages.

## Automatic checks (run before delivery)

- Category order correct.
- Wine category without a vintage (and not marked "no vintage") → **report "Jahrgang fehlt"**.
- Producer line without a known country → report.
- Region without a translation → report.
- Name line very long; description line over 13 cm.
- Price format `\d{1,3},\d\d`; quantity format `(number + l/cl) Glas|Flasche`.
- Each card exactly one page.

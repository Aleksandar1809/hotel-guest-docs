# Evening menu

Daily five-course dinner menu. German is the source; EN, FR and IT are produced in a fixed format.

## House profile (edit per hotel)

| Item | DE | EN | FR | IT |
|---|---|---|---|---|
| Title (set by script) | Abendmenü | Evening menu | Menu du soir | Menù serale |
| Categories | Vorspeisen · Suppen · (salad line) · Hauptgerichte · Dessert | Starters · Soups · Salads from the buffet · Main courses · Desserts | Hors d'œuvres · Potages · Salades du buffet · Plats principaux · Desserts | Antipasti · Zuppe · Insalate del buffet · Piatti principali · Dessert |
| Separator word | oder | or | ou | oppure |
| Salad course (fixed, never commented) | Bunte Salate vom Buffet / mit diversen Beilagen und Garnituren | Salads from the buffet / with various dressings and garnishes | Salades du buffet / avec diverses vinaigrettes et garnitures | Insalate del buffet / con diversi condimenti e guarnizioni |
| Cheese line (set by script, always) | Heimischer und internationaler Käse / vom Wagen | National and international cheese / from the trolley | Fromages nationaux et internationaux / du chariot | Formaggi nazionali e internazionali / dal carrello |

"Starters" is always included in EN, even if the German has no starter heading.

## Workflow

**New menu** (date + German text):
1. Check the German and give an explicit verdict: "passt" or a numbered list. Every finding with course, dish and line. Never correct the German yourself.
2. The kitchen writes by hand and a colleague types it up, so reading errors happen (Patate instead of Batate, Kartoffel instead of Erdäpfel, doubled "mit"). Report them and use the corrected reading in the translations.
3. Write EN, FR and IT in copy-paste format (below) and, if files are wanted, run `scripts/menu_docx.py`.
- Title and cheese line are never sent. Never report them as missing, never comment on the salad or cheese line.

**"Has anything changed?"**
- Compare with the last version. Send only the affected lines as copy-paste text in EN/FR/IT, always with course, dish and line.
- Always the whole line, never only the changed words. If a line break moves, all affected lines of the dish.
- A purely grammatical fix without effect on the translations: one sentence.
- Check every new version for new typos.
- No new files unless asked.

**French corrections from a reviewer** (two reviewers of equal rank are possible):
- Read the formatting: struck through = remove, highlighted/coloured = new. Adopt as a permanent rule. If it contradicts these rules, name the conflict and ask. Do not return a corrected file unless asked.

No image check and no rendering: a technical check of the files is enough.

## Copy-paste format (input to the script)

```
Category
Dish line
Dish line
or
Dish line
***
Category
...
```
Blank lines do not matter. Any number of lines per dish and dishes per course. The script adds: title, 12-star line, blank paragraphs, forgotten `***` (also between courses), cheese line, file name.

```bash
python3 scripts/menu_docx.py DD.MM.YYYY en.txt fr.txt it.txt [output_dir]
```

## .docx format (binding, implemented in the script)

- A4, margins top 568 / right 1286 / bottom 284 / left 1260 twips; everything centred.
- Times New Roman declared inline in every run (never via styles: client machines substitute theme fonts).
- Title 20 pt bold italic; star line 16 pt bold italic; category 15 pt bold italic underlined; dish 13 pt italic; separator word 13.5 pt bold italic; `***` 14.5 pt italic; character spacing 1.5 pt.
- No author or company metadata.

## German: house conventions

- Austrian vocabulary: Marille, Karfiol, Kren, Obers, Topfen. Diminutives stay (Wangerl, Nockerl, Tascherl, Laibchen).
- House spellings, never corrected: Mascarino, Duxel, Bayerische Creme, Royale.
- Dative after mit/an/auf/in, also in lists. Exception: the last "und" item may stay nominative, but only if the list ends there (not before "dazu …").
- "dazu" without comma. Report doubled prepositions (mit … mit, an … an, in … in).
- Hyphen only with foreign words, proper names and multi-part compounds: Gin-Schaum, Sushi-Reis, Grapefruit-Eis, Grand-Marnier-Schaum, Milchkalbs-Tafelspitz. Pure German compounds are written together (Distelölschaum, Polentahalbmonde): not an error. A drink as proper name may go without hyphen (Madeirasauce, Marsalajus).
- Place adjectives capitalized, no hyphen: Wiener Tafelspitz, Tiroler Gerstlsuppe.
- Adjectives inside a dish lower case (roter Rübe); nominalizations capitalized (Geschmortes, Geeistes, Eingelegtes, Gebackenes, Gefrorenes).
- Dish titles without article: "Variation von …", not "Eine Variation".
- "der Paprika": mit rotem Paprika.
- Report: missing commas, extra spaces and ellipses, missing `***`.
- Vague items stay vague in all languages ("Praline", "eingelegte Filets", "Geschmortes"): the chef deliberately does not say what they are made of. Do not ask, do not add the ingredient.

## English

Categories: Starters · Soups · Salads from the buffet · Main courses · Desserts. Separator: or.
- Only the first word capitalized; proper names capitalized (Speck, Calvados, Pernod, Marsala, Madeira, Campari, Baileys, Malibu, Grand Marnier, Amarena, Picandou, Schupfnudeln, Pofesen, Buchtel). Generic spirits lower case: sherry, brandy, whisky, grappa, gin, rum, port.
- an X → on X. "served with" at most once per dish (for "dazu"). No article before sauces/foams (in sherry sauce, in light olive foam).
- Article with countable single items: a rice croquette, a potato patty, a stuffed dumpling. Plural without article.
- Hyphenated German compounds stay joined: Melon-pomegranate sorbet, lingonberry-pepper foam.
- "Geschmortes" is dropped; if it was the last item, join the previous line with "and".
- Nominalizations short: Geeistes → iced · Gefrorenes → frozen · Eingelegtes → pickled · Gebackenes → baked.

**Preparation:** rosa gebraten → rosé-roasted · am Stück gebraten → whole-roasted · gebraten → pan-fried · tranchiert → sliced · confiert → confit · gratiniert → gratinated · souffliert → soufflé-baked · gebacken → baked (cereals: crispy; "mit X gebacken": in a X crust; "im X-Mantel": in a X crust) · Röster savoury → sautéed, in desserts → compote · Schaum-/Cremesuppe → velouté
**Formulas:** Süßes von X → X creation · Variation von X → Variation of X · Das Beste von X → The best of X · Eis-X → Iced X · Consommé „double" → Double consommé · Roastbeef vom X (not beef) → Roast loin of X
**Fish:** Seesaibling → Arctic char · Saibling → char · Waller → catfish · Zander → pike-perch · Wolfsbarsch → sea bass · Seeteufel → monkfish · Steinbutt → turbot · Lachsforelle → salmon trout · Flusskrebs → crayfish · Jakobsmuschel → scallop
**Meat:** Mastochse → fattened ox · Semerrolle → eye of round · Huft → rump · Rücken → loin (lamb, roe deer, red deer: saddle) · Lende → loin · Beiried → sirloin · Wangerl → cheek · Bries → sweetbread · Wild/Reh/Hirsch → venison · Jungschwein → young pork · Spanferkel → suckling pig · Milchkalb → milk-fed veal · Maispoularde → corn-fed poularde · Tafelspitz → tafelspitz
**Vegetables/fruit:** Kren → horseradish · Kresse → cress · rote Rüben → beetroot · gelbe Rüben → carrots · Wirsing → savoy cabbage · Rotkraut → red cabbage · Karfiol → cauliflower · Melanzani → aubergine · Schwarzwurzel → black salsify · Topinambur → Jerusalem artichoke · Eierschwammerl → chanterelles · Seitlinge → oyster mushrooms · Graupen → pearl barley · Liebstöckel → lovage · Kerbel → chervil · Pfefferkraut → savory · Preiselbeeren → lingonberries · Holunder(blüte) → elderflower · Holunderbeeren → elderberries · Brüsseler Spitzen → chicory · Rettich next to Radieschen → white radish / radishes
**Dough/sides:** Knödel → dumpling · Semmelknödel → bread dumplings · Serviettenknödel → napkin dumpling · Kaspressknödel → pan-fried cheese dumpling · Nockerl → dumplings · Paunzen → gnocchi · Maultasche → ravioli · Schlutzkrapfen → Tyrolean ravioli · Tascherl → pastry parcel · Nudelteigtascherl → pasta parcels · Laibchen → patty · Taler → disc · Rauten → diamonds · Streifen → julienne · Frittaten → pancake strips · Schöberl → sponge squares · Krusteln → croutons · Brösel → breadcrumbs · Biskuit → sponge cake · Biskotten → sponge fingers · Hippe → tuile · Baiser, Eiweiß (dessert) → meringue · Plunderteig → Danish pastry · Blätterteigstangerl → puff pastry straws · Krapfen → doughnut · Buchtel → Buchtel · Riso → risoni · Kugel → ball · Knäckebrot → crispbread
**Cheese/dairy/oil:** Topfen → quark · Obers → cream · Mascarino → mascarpone · Graukäse → Tyrolean grey cheese · Bratkäse → pan-fried cheese · Distelöl → safflower oil · Kernöl → pumpkin seed oil · Bärlauchöl → wild garlic oil

## French

Categories: Hors d'œuvres · Potages · Salades du buffet · Plats principaux · Desserts. Separator: ou.

**Sentence structure**
- Only one "avec" per dish, then comma lists. "avec" for sides/garnishes; "au/à la" for the defining ingredient of the main product.
- A preposition at the start of a continuation line is removed; instead a comma ends the previous line (not every line ending).
- No comma before "et"; never three "et" in one line (comma or line break).
- Repeat the preposition in lists: aux asperges et aux épinards.
- Doneness before cut: rosé découpé.
- maison: short, directly on the noun (Raviolis maison); multi-word at the end "faits maison".
- Without article: Potage crème de X, Sorbet à la X, Mousse de X. With article: Le meilleur de la/du X, Variation autour de la/du X.
- "eigene/r/s X" without possessive: boule, anneau, garniture, poêlée, confit, sorbet, compotée.
- Local place names are dropped; "heimisch" → de la région.
- Spirits: generic names lower case (xérès, whisky, rhum, gin, brandy, grappa, porto, madère, marsala, calvados); brand names capitalized (Pernod, Campari, Baileys, Malibu, Grand Marnier). Products lower case (mascarpone, parmesan, amaretti, amarettini, dim sum).
- Guillemets « » for breed and product names: selle de porc « duroc », « Schupfnudeln ».
- "X-Jus" → jus au X · "X-Püree" → purée de X · "in X-Sauce" → sauce à la X · oil foam → mousse à l'huile de X.

**Soups:** Potage crème is the standard. Velouté only if "crème" already appears in the dish (crème fraîche, Obers).
**Mousse/foam:** dish → mousse de X · flavour → mousse à la/au X · écume if "mousse" already appears in the dish or the sound repeats (pamplemousse) · served in a foam → en mousse / en écume · braune Butter → beurre noisette · Salzschaum → mousse salée.
**Dumplings:** round → boulette (mushroom, cheese, Speck, liver, spinach, Topfen dumplings; Semmelknödel → boulettes de pain; Serviettenknödel → boulette de pain en serviette; Kaspressknödel → boulette de fromage pressée). Elongated/Nockerl → quenelle (semolina, Topfen, grain Nockerl, Bröselknödel).
**Preparation:** gebraten → rôti(e), also fish · am Stück → rôti(e) · tranchiert → découpé(e) · rosa → rosé(e) · gratiniert → gratiné(e) · glasiert → glacé(e) · gebacken → au four (cereals: croustillant) · souffliert → soufflé(e) · im X-Mantel/mit X-Kruste → en croûte de X · Röster savoury → poêlée de X, Erdäpfelröster → pommes de terre rissolées, in desserts → compotée de X
**Formulas:** Süßes von X → Douceurs à la/au X · Consommé „double" → Consommé double · Frittaten in consommé → Consommé Célestine (no preposition) · Geschmortes → garniture braisée · Eingelegtes → mariné · Geeistes, Gefrorenes → glacé
**Fish:** Seesaibling → omble chevalier · Saibling → omble · Waller → silure · Zander → sandre · Wolfsbarsch → loup de mer · Seeteufel → lotte · Steinbutt → turbot · Lachsforelle → truite saumonée · Flusskrebs → écrevisse · Jakobsmuschel → Saint-Jacques
**Meat:** Speck → lard · Rücken → selle · Huft → quasi (veal) / rumsteck (beef) · Semerrolle → rond de gîte · Beiried → faux-filet · Lende → filet · Wangerl → joue · Bries → ris de veau · Reh → chevreuil · Hirsch → cerf · Wild → gibier · Jungschwein → porcelet · Spanferkel → cochon de lait · Entenbrust → magret de canard · Perlhuhnbrust → poitrine de pintade · Wachtelbrust → poitrine de caille · Maispoularde → poularde de maïs · Mastochse → bœuf engraissé · Tafelspitz → pointe de culotte de bœuf (beef) / pointe de culotte de veau (veal) · Flanksteak → bavette
**Vegetables/fruit:** Rüben → navets · gelbe Rüben (Austrian for carrots) → carottes · rote Rüben → betteraves rouges · Kren → raifort · Kresse → cresson · Wirsing → chou de Milan · Rotkraut → chou rouge · Kürbis → potiron · Hokkaido → potimarron · Sellerie → céleri (Knollen- → céleri-rave, Stangen- → céleri en branche, englischer → céleri anglais) · Junglauch → ciboules · Lauch → poireaux · Brokkoli → brocolis · Brüsseler Spitzen → endives · Graupen → orge perlé · Seitlinge → pleurotes · Eierschwammerl → chanterelles · Pfefferkraut → sarriette · Preiselbeeren → airelles rouges · Radicchio → radicchio
**Dough/sides/cheese:** Topfen → fromage frais · Obers → crème · Mascarino → mascarpone · Graukäse → fromage gris · Bratkäse → fromage grillé · Krusteln → croûtons · Brösel → chapelure · Streusel, Crumble → crumble · Biskuit → biscuit · Schöberl → biscuits · Biskotten → biscuits à la cuillère · Baiser → meringue · Eiweiß (dessert) → blancs d'œufs · Hippe → tuile · Plunderteig → pâte feuilletée levée · Germteig → pâte levée · Buchtel → petite brioche (à la pâte levée) · Pofesen → beignets bavarois · Krapfen → beignet · Paunzen → gnocchis · Maultasche, Schlutzkrapfen → raviolis · Tascherl → chausson · Nudelteigtascherl → chaussons de pâte à nouilles · Laibchen → galette · Taler → palet · Rauten → losanges · Streifen → julienne · Halbmonde → fleurons · Mini-Kartoffeln → pommes de terre grenaille · Schrot → concassé · Vollkorn → blé complet · Gel → gel · Gelee → gelée · Malto → maltodextrine · Kugel → boule · Knäckebrot → Knäckebrot · Distelöl → huile de carthame · Kernöl → huile de pépins de courge

## Italian

Categories: Antipasti · Zuppe · Insalate del buffet · Piatti principali · Dessert. Separator: oppure.
- Spirits: generic and origin names lower case (sherry, madera, marsala, calvados, porto, whisky, brandy, grappa, gin, rum); brand names capitalized (Pernod, Campari, Baileys, Malibu, Grand Marnier).
- "eigene/r X" → proprio/a. "ed" only before a word starting with e (ed erbe). Foam → spuma.

**Preparation:** rosa → cotto/a rosa · am Stück gebraten → arrosto intero · gebraten → scottato (vegetables: saltato) · tranchiert → affettato · souffliert → in soufflé · gebacken → al forno (cereals: croccante) · geeist → gelato · Röster savoury → saltato, in desserts → composta · Schaum-/Cremesuppe → vellutata · Granité → granita
**Formulas:** Süßes von X → Dolcezze al/alla X · Das Beste von X → Il meglio del/della X · Variation von X → Variazione di X · Geschmortes → brasato · Eingelegtes → marinato · Ragout in desserts → composta
**Fish:** Seesaibling → salmerino alpino · Saibling → salmerino · Waller → siluro · Zander → lucioperca · Wolfsbarsch → branzino · Seeteufel → coda di rospo · Steinbutt → rombo · Lachsforelle → trota salmonata · Flusskrebs → gamberi di fiume · Jakobsmuschel → capasanta
**Meat:** Speck → Speck · Rücken → lombata (lamb, roe deer: sella) · Lende → filetto · Beiried → controfiletto · Huft → scamone · Semerrolle → girello · Wangerl → guancetta · Bries → animella · Reh → capriolo · Hirsch → cervo · Wild → selvaggina · Mastochse → bue · Jungschwein → maialino · Spanferkel → maialino da latte · Maispoularde → pollastra al mais · Tafelspitz → Tafelspitz · Flanksteak → bavetta
**Vegetables/fruit:** Rüben → rape · gelbe Rüben → carote · rote Rüben → barbabietola rossa · Kren → rafano · Kresse → crescione · Wirsing → verza · Rotkraut → cavolo rosso · Karfiol → cavolfiore · Schwarzwurzel → scorzonera · Eierschwammerl → finferli · Seitlinge → pleurotus · Graupen → orzo perlato · Preiselbeeren → mirtilli rossi · Cranberry → cranberry · Sanddorn → olivello spinoso · Brüsseler Spitzen → indivia belga · Junglauch → cipollotti
**Dough/sides/cheese:** Topfen → quark · Obers → panna · Mascarino → mascarpone · Graukäse → formaggio grigio tirolese · Bratkäse → formaggio alla piastra · Knödel → canederlo/i (filled: canederlo ripieno, never polpetta) · Semmelknödel → canederli di pane · Nockerl → gnocchetti · Paunzen → gnocchi · Maultasche, Schlutzkrapfen → ravioli · Tascherl → fagottino · Laibchen → tortino · Taler → medaglione · Rauten → rombi · Streifen → julienne · Halbmonde → mezzelune · Frittaten → crespelle a striscioline · Krusteln → crostini · Brösel → pangrattato · Biskuit → pan di Spagna · Biskotten → savoiardi · Baiser → meringa · Eiweiß (dessert) → albume · Hippe → cialda · Plunderteig → pasta sfoglia lievitata · Blätterteig → pasta sfoglia · Germteig → pasta lievitata · Pofesen → frittelle bavaresi · Kugel → sfera

## Decided cases

- Tafelspitz: EN/IT untranslated; FR pointe de culotte de bœuf / de veau.
- gebackene Garnele: oven-baked (baked / au four / al forno).
- Holunder without addition: the blossom.
- dim sum: lower case in all languages.
- "double" with consommé and entrecôte: without quotation marks.
- Signature names in quotation marks ("Mont Blanc", "Tomate Fausse"): untranslated.
- Semerrolle: EN eye of round, IT girello.
- Distelöl (= safflower oil): safflower oil / huile de carthame / olio di cartamo.
- Knäckebrot: EN crispbread, FR/IT untranslated.
- Koch (dessert), also "eigener Koch": EN its own compote, FR compote, IT propria composta.
- Nominalizations (Geeistes, Eingelegtes …) without addition: iced/pickled, glacé/mariné, gelato/marinato.

## Reading reviewer correction files (.docx)

- Always parse the XML, never only plain text: iterate `<w:r>` runs and check `<w:rPr>`.
- `<w:strike/>` = deleted text → remove. `<w:highlight/>` (or coloured text) = inserted correction → adopt.
- Plain-text diffs create false "double word" errors and miss the markup.
- Extract the rule behind each correction; flag contradictions between reviewers.

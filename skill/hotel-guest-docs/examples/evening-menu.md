# Example: evening menu · Hotel Alpenrose ★★★★★S, Tyrol

Fictional menu. It contains three typical problems: a doubled preposition, a reading error from the handwritten original, and a missing closing separator.

## Input (as sent by staff)

```
Abendmenü Freitag, 16.10.2026

Vorspeisen
Carpaccio vom Rinderfilet
mit Krenschaum, Rucola
und gerösteten Pinienkernen
oder
Geräucherte Lachsforelle
auf Gurkensalat mit mit Sauerrahm
***
Suppen
Klare Rindsuppe mit Frittaten
oder
Kürbiscremesuppe
mit Kernöl und Krusteln
***
Bunte Salate vom Buffet
mit diversen Beilagen und Garnituren
***
Hauptgerichte
Rosa gebratener Hirschrücken
mit Preiselbeersauce, Rotkraut
und Serviettenknödel
oder
Gebratenes Zanderfilet
auf Wirsing mit Patatenpüree
und Weißweinschaum
oder
Risotto von Eierschwammerln
mit Parmesan und Kresse
***
Dessert
Marillenknödel
mit Butterbröseln und Vanilleeis
oder
Süßes von der Zwetschke
mit Zimteis
```

## Expected output

Deutsch: 3 Punkte, sonst passt.
1. Vorspeisen · Lachsforelle · Zeile 2: doppeltes „mit" („mit mit Sauerrahm").
2. Hauptgerichte · Zanderfilet · Zeile 2: „Patatenpüree" ist ein Lesefehler für **Batatenpüree** (Süßkartoffel). In den Übersetzungen bereits korrigiert.
3. Dessert: Schlusszeile „***" fehlt. Der Generator setzt sie.

**EN**
```
Starters
Beef fillet carpaccio
with horseradish foam, rocket
and roasted pine nuts
or
Smoked salmon trout
on cucumber salad with sour cream
***
Soups
Clear beef soup with pancake strips
or
Pumpkin velouté
with pumpkin seed oil and croutons
***
Salads from the buffet
with various dressings and garnishes
***
Main courses
Rosé-roasted saddle of venison
with lingonberry sauce, red cabbage
and a napkin dumpling
or
Pan-fried pike-perch fillet
on savoy cabbage with sweet potato purée
and white wine foam
or
Chanterelle risotto
with Parmesan and cress
***
Desserts
Apricot dumplings
with buttered breadcrumbs and vanilla ice cream
or
Plum creation
with cinnamon ice cream
***
```

**FR**
```
Hors d'œuvres
Carpaccio de filet de bœuf
avec mousse au raifort, roquette
et pignons de pin grillés
ou
Truite saumonée fumée
sur salade de concombres avec crème aigre
***
Potages
Consommé de bœuf Célestine
ou
Potage crème de potiron
avec huile de pépins de courge et croûtons
***
Salades du buffet
avec diverses vinaigrettes et garnitures
***
Plats principaux
Selle de cerf rôtie rosée
avec sauce aux airelles rouges, chou rouge
et boulette de pain en serviette
ou
Filet de sandre rôti
sur chou de Milan avec purée de patate douce
et mousse au vin blanc
ou
Risotto aux chanterelles
avec parmesan et cresson
***
Desserts
Boulettes aux abricots
avec chapelure au beurre et glace à la vanille
ou
Douceurs à la quetsche
avec glace à la cannelle
***
```

**IT**
```
Antipasti
Carpaccio di filetto di manzo
con spuma al rafano, rucola
e pinoli tostati
oppure
Trota salmonata affumicata
su insalata di cetrioli con panna acida
***
Zuppe
Brodo di manzo con crespelle a striscioline
oppure
Vellutata di zucca
con olio di semi di zucca e crostini
***
Insalate del buffet
con diverse vinaigrette e guarnizioni
***
Piatti principali
Lombata di cervo cotta rosa
con salsa ai mirtilli rossi, cavolo rosso
e canederlo al tovagliolo
oppure
Filetto di lucioperca scottato
su verza con purè di patate dolci
e spuma al vino bianco
oppure
Risotto ai finferli
con parmigiano e crescione
***
Dessert
Canederli alle albicocche
con pangrattato al burro e gelato alla vaniglia
oppure
Dolcezze alla prugna
con gelato alla cannella
***
```

Files (when wanted), from the three blocks above saved as `en.txt`, `fr.txt`, `it.txt`:

```bash
python3 scripts/menu_docx.py 16.10.2026 en.txt fr.txt it.txt
```
→ `Evening_menu_16_10.docx`, `Menu_du_soir_16_10.docx`, `Menu_serale_16_10.docx`, each with title, star line and cheese line added.

## Follow-up: "Has anything changed?"

Staff send the corrected German with one change: the venison now comes "mit Wacholdersauce" instead of "mit Preiselbeersauce".

Expected reply:

Hauptgerichte · Hirschrücken · Zeile 2:
- EN: `with juniper sauce, red cabbage`
- FR: `avec sauce au genièvre, chou rouge`
- IT: `con salsa al ginepro, cavolo rosso`

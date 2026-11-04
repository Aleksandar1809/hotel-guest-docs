# Kids' menu

Daily children's menu (soup, main course, dessert). It is printed on a colouring-page template, so the output is plain text that staff paste into the template. Where nothing different is stated here, the evening-menu rules apply (`evening-menu.md`).

## Task

Staff send the German kids' menu. Two steps, nothing more:
1. **Check the German**: spelling and grammar.
2. **Translate**: English, French, Italian.

## Output format

- Plain text. The only formatting: **bold language label**, a blank line below it, then the menu text.
- Order: Deutsch – English – Français – Italiano.
- Courses separated by a blank line.
- **No** heading ("KINDERMENÜ"), **no** smiley separator line, **no** place/date line, **no** date from the message. The template already has them.
- Errors first, briefly. If everything is correct, one sentence is enough.
- If only one line changes: output **only that line** in all four languages.
- "Has anything changed?": compare with the last version and name only the difference.

## German check: what to report

**Report:** typos, missing accents (Consommé, Croûtons), wrong case, missing commas, linked compounds (Gelbe-Rüben-Cremesuppe, Heidelbeer-Orangen-Sorbet).

**Do not report: this is the kitchen's handwriting:**
- "Sahne" instead of "Obers"
- diminutives in -chen (Schnitzelchen, Krapferl)
- house spellings (Mascarino)
- register and style questions in general

**Case rule:** side dishes that follow a comma as a free list stay in the **nominative**, even after a preposition.
> in Rosmarinsauce, Mini-Penne-Auflauf **und junges Gemüse** ✓

Dative only when "mit" governs the side dish directly:
> **mit** Pommes frites und jung**em** Gemüse ✓

## Reviewer corrections

Arrive as .docx (read with `pandoc -t markdown <file>` or at XML level) or as pasted text.
- **Highlighted** = the reviewer's correction → adopt word for word.
- **Struck through** = removed by the reviewer → drop.
Every correction applies permanently from now on, even without a new file. The French reviewer is the style authority for French; their line is the house standard of the evening menu too.

## Deliberate deviations from the evening menu

Only in **English**, because children must be able to read it: **Speck → bacon**, **Cremesuppe / Schaumsuppe → cream of … soup / … foam soup** (not velouté). French and Italian follow the evening-menu standard unchanged.

## Terminology

### Soups and garnishes

| German | English | French | Italian |
|---|---|---|---|
| Cremesuppe / Schaumsuppe | cream of … soup / … foam soup | Potage crème de … | vellutata di … |
| Consommé | Consommé | Consommé | Consommé |
| Frittaten | pancake strips | Célestine | crespelle a striscioline |
| Frittatenauflauf | gratin of pancake strips | gratin de Célestine | sformato di crespelle |
| Royale | royale | royale | royale |
| Knödel (round) | dumpling | **boulette** | canederlo |
| Nockerl / shaped, elongated | dumpling | **quenelle** | gnocchetto |
| Grießnockerl | semolina dumpling | quenelle de semoule | gnocchetto di semolino |
| Bröselknödel | breadcrumb dumpling | quenelle de chapelure | canederlo di pangrattato |
| Krusteln / Croûtons | croutons | croûtons | crostini |
| Gebäck (with soup) | freshly baked pastry | petits pains | panini |
| Blätterteigstangerl | puff pastry straws | bâtonnet feuilleté | bastoncini di pasta sfoglia |
| Riso (= risoni pasta, not rice) | riso | riso | riso |
| eigene Einlage | its own garnish | garniture | guarnizione |
| Wurzelrauten | root vegetable diamonds | légumes racines en losanges | ortaggi a radice a losanghe |
| Karottenstreifen / Gemüsestreifen | julienne vegetables | julienne de légumes | julienne di verdure |

### Vegetables and sides

| German | English | French | Italian |
|---|---|---|---|
| Gelbe Rüben (= carrots in Austria) | carrots | carottes | carote |
| gelbe Karotten (variety) | yellow carrots | carottes jaunes | carote gialle |
| junges Gemüse | baby vegetables | jeunes légumes | verdure novelle |
| Erbsengemüse | green peas | petits pois | piselli |
| Wirsing | savoy cabbage | chou de Milan | verza |
| Kohlrabi | kohlrabi | chou-rave | cavolo rapa |
| Karfiol | cauliflower | chou-fleur | cavolfiore |
| Kürbis | pumpkin | potiron | zucca |
| Schwarzwurzel | black salsify | salsifis | scorzonera |
| Stangensellerie | celery | céleri en branche | sedano |
| englischer Sellerie | celery | **céleri anglais** | sedano |
| Erdäpfel | potatoes | pommes de terre | patate |
| Erdäpfelgebäck | potato pastry | **pommes de terre duchesse** | patate duchessa |
| Paunzen | potato fritters | beignets de pommes de terre | frittelle di patate |
| Pommes frites | French fries | frites | patatine fritte |
| Spätzle | spaetzle | spaetzle (lower case, no umlaut) | spaetzle |

### Meat and preparation

| German | English | French | Italian |
|---|---|---|---|
| Speck | **bacon** | lard | Speck |
| Rücken | **loin** (never saddle/sirloin) | **selle** | lombata |
| Huft | rump | quasi | noce |
| Beiried | sirloin | faux-filet | – |
| Tafelspitz | tafelspitz | pointe de culotte de bœuf / de veau | Tafelspitz |
| Maispoularde | corn-fed poularde | poularde de maïs | pollastra al mais |
| Milchkalb | milk-fed veal | veau de lait | vitello da latte |
| Jungschwein | young pork | porcelet | maialino |
| Schnitzel(chen) | escalope(s) | escalope(s) | scaloppina/e |
| tranchiert | sliced | découpé | tagliato a fette |
| am Stück gebraten | **whole roasted** | rôti entier | arrosto intero |
| kurz gebraten | pan-fried | saisi | scottato |
| rosa gebraten | rosé-roasted | rosé | cotto rosa |
| gebacken (breaded) | breaded | pané(e) | impanato |
| gebacken (cereals, corn) | crispy | croustillant | croccante |
| tomatisierte Fleischsauce | tomato meat sauce | **sauce bolognaise** | ragù di carne |

### Desserts

| German | English | French | Italian |
|---|---|---|---|
| Flammerie | **pudding** | **flan** | **budino** |
| Flammerie vom Weizengrieß | Wheat semolina pudding | Flan de semoule de blé | Budino di semolino di grano |
| Hippe / Hippenröllchen | **tuile** | tuile | cialda |
| Biskuit / Becherbiskuit | sponge cake | **biscuit** | pan di Spagna |
| Baiser | meringue | meringue | meringa |
| Eiweißchips | egg white chips | **chips de blanc d'œuf** | chips di albume |
| Streusel | crumble | **crumble** | crumble |
| Topfen | quark | **fromage frais** | quark |
| Obers / Sahne | whipped cream | crème fouettée | panna montata |
| Sauerrahm | sour cream | crème aigre | panna acida |
| Vollmilch (chocolate, e.g. Vollmilch-Ganache) | milk chocolate | chocolat au lait | cioccolato al latte |
| Gebrannte Creme | Crème brûlée | Crème brûlée | Crème brûlée |
| Pofesen | Pofesen | **beignet bavarois** | frittella bavarese |
| Mascarino | Mascarino | mascarpone | mascarpone |
| Marille | apricot | abricot | albicocca |
| Röster (dessert) | compote | compotée | composta |
| Malto | malto | maltodextrine | maltodestrina |
| „Steine" | stones | cailloux | sassi |
| geeist | **iced** | glacé | gelato/gelata |
| Süßes von X | Sweet X creation | **Douceurs à la/au X** | Dolce di X |
| Variation von X | Variation of X | Variation autour de la/du X | Variazione di X |
| Das Beste von X | The finest of X | Le meilleur de la/du X | Il meglio di X |

### French: recurring traps

- **`en sauce à la crème`**, not `avec sauce`
- Soup heading always **`Potage crème de …`**
- Watch plurals: poireau**x**, spaghettini**s**, brocoli**s**, dé**s**, raviolis, gnocchis
- "Gel" → gel, "Gelee" → gelée
- Sauce **brune**, never "sombre"
- **pop-corn** with hyphen
- Foam: écume or mousse, case by case, no blanket rule

## Open points (decide with the French reviewer)

- Eiweißchips: whether EN and IT follow literally or use meringue/meringa.
- Schöberl: no house term yet.
- Bröselknödel: quenelle de chapelure kept, although round dumplings are otherwise boulette.

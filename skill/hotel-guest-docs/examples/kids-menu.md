# Example: kids' menu · Hotel Alpenrose ★★★★★S, Tyrol

Fictional menu with two real errors (a missing accent, a capitalization error) and one kitchen habit that must **not** be reported ("Sahne").

## Input (as sent by staff)

```
Kindermenü 16.10.

Consomme mit Grießnockerl

Gebackene Hühnerschnitzelchen
mit Pommes Frites und jungem Gemüse

Flammerie vom Topfen
mit Marillenröster, Sahne und Streusel
```

## Expected output

Deutsch: 2 Fehler. Suppe: „Consommé" (Akzent). Hauptgang: „Pommes frites" (klein).

**Deutsch**

Consommé mit Grießnockerl

Gebackene Hühnerschnitzelchen
mit Pommes frites und jungem Gemüse

Flammerie vom Topfen
mit Marillenröster, Sahne und Streusel

**English**

Consommé with semolina dumplings

Breaded chicken escalopes
with French fries and baby vegetables

Quark pudding
with apricot compote, whipped cream and crumble

**Français**

Consommé avec quenelles de semoule

Escalopes de poulet panées
avec frites et jeunes légumes

Flan au fromage frais
avec compotée d'abricots, crème fouettée et crumble

**Italiano**

Consommé con gnocchetti di semolino

Scaloppine di pollo impanate
con patatine fritte e verdure novelle

Budino di quark
con composta di albicocche, panna montata e crumble

## Notes on the decisions

- "Sahne" and "-chen" are the kitchen's hand: not reported.
- Flammerie → pudding / flan / budino; Topfen → quark / fromage frais / quark.
- Röster in a dessert → compote / compotée / composta.
- No heading, no date line: the colouring-page template has them.

## Follow-up: only one line changes

Staff: "Statt Streusel jetzt Schokoraspeln."

Expected reply (only this line, all four languages):

**Deutsch** mit Marillenröster, Sahne und Schokoraspeln
**English** with apricot compote, whipped cream and chocolate shavings
**Français** avec compotée d'abricots, crème fouettée et copeaux de chocolat
**Italiano** con composta di albicocche, panna montata e scaglie di cioccolato

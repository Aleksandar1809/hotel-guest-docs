# Privacy check

Gate before this repository is made public. Date: 2026-11-04.

**Result: 0 hits.** No real hotel, owner, staff or guest data, contact details, addresses, real prices or account names were found in any file of this repository, including the files inside `dist/hotel-guest-docs.zip`.

## Method

1. **Deny-list from the confidential source material.** Built automatically from the private source repository (generator folders, briefing backup, morning-newsletter folder, Notion export including the files inside its ZIPs, Word templates embedded as base64). The already-anonymized skill and docs were excluded so the list holds only confidential terms. No value is printed here or stored in this repository.
   - Text of `.md`, `.html`, `.csv`, `.py`, `.js`; `.docx` text **and** metadata (author, last modified by, comment authors); `.doc` text; PDF text and document info; image EXIF/XMP (artist, copyright).
   - Extracted: hotel name, village (date lines of the printed documents), owners', staff and guest names (role context such as "sommelier …", "guide …", "Familie …", photo credits, briefing entities and aliases), account names from Word metadata, phone numbers, e-mail addresses, web domains and their labels, street addresses and postcodes, real menu/wine/spa prices.
2. **Extraction of this repository.** Every file, including every file inside the ZIP, with the same extractor: text, Office/PDF metadata and image EXIF.
3. **Matching.** Case-insensitive whole-word match of every deny-list term; phone numbers compared as digit sequences; every € amount compared with the real-price list.
4. **Generic patterns.** E-mail addresses, phone numbers (international and Austrian formats), IBAN, € amounts.
5. **Cross-check.** 4,053 rare capitalised words from the source (possible names of people, places, huts, producers) were intersected with this repository. Every overlap was reviewed by hand.
6. **Review.** Every match was resolved: either fixed in the files, or confirmed as an ordinary word (dish names, wine regions, common words such as "hotel", public brands such as board games or fonts).

## Numbers

| Item | Count |
|---|---|
| Deny-list terms (values not shown) | 755 |
| — names, accounts, places, contact details, addresses | 682 |
| — real prices | 59 |
| — domain labels | 14 |
| Rare source words for the cross-check | 4,053 |
| Files scanned (21 in the repository + 14 inside the ZIP) | 35 |
| Office, PDF or image files | 0 (none in the repository; the scanner checks their text and metadata) |

## Hits

| Check | First scan | Final scan |
|---|---|---|
| Real prices | 6 (all prices of the wine-card example) | **0** |
| Names of producers, places and activities also found in the source | 14 (wine producers, a hut and lake, a guide programme, yoga class titles, a lounge name, a spa product) | **0** |
| Other deny-list matches | ordinary words only, reviewed | **0** open |
| E-mail addresses | 0 | **0** |
| Phone numbers | 0 | **0** |
| IBAN | 0 | **0** |
| € amounts | only the invented example prices and the €20 tool cost | **0** real prices |
| Metadata / EXIF account names | 0 | **0** |

**Fixes made:** the six example wine prices were replaced with invented prices that are not in the real price list. The 14 names were replaced with invented names that do not appear anywhere in the source. The ZIP was rebuilt from the corrected skill folder; its file list is unchanged (14 files).

## Not in scope

- Git history before this check holds only the initial README commit.
- Public appellations (e.g. Wachau, Kamptal) and well-known wines or brands are public information, not personal data.

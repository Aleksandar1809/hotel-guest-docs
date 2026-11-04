#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evening menu generator: writes the EN/FR/IT Word files in the fixed house format.
Do not change the formatting per menu; edit LANGS only when adapting to another hotel.

Usage:
  python3 scripts/menu_docx.py DD.MM.YYYY en.txt fr.txt it.txt [output_dir]

Input per language, as copy-paste text:
  Category
  Dish line
  Dish line
  or | ou | oppure
  Dish line
  ***
Blank lines do not matter. Any number of lines per dish and dishes per course.
Set automatically: title, star line, blank paragraphs, forgotten separators
(also between courses), cheese line, file name.
The files carry no author or company metadata.
"""
import datetime
import os
import sys
import zipfile

RF = ('<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" '
      'w:eastAsia="Times New Roman" w:cs="Times New Roman"/>')

LANGS = {
    'en': dict(title='Evening menu', sep_word='or', lang='en-GB', last=True,
               cats=['Starters', 'Soups', 'Salads from the buffet', 'Main courses', 'Desserts'],
               cheese=['National and international cheese', 'from the trolley'],
               name='Evening_menu_{dd}_{mm}.docx'),
    'fr': dict(title='Menu du soir', sep_word='ou', lang='fr-FR', last=False,
               cats=['Hors d’œuvres', 'Potages', 'Salades du buffet', 'Plats principaux', 'Desserts'],
               cheese=['Fromages nationaux et internationaux', 'du chariot'],
               name='Menu_du_soir_{dd}_{mm}.docx'),
    'it': dict(title='Menù serale', sep_word='oppure', lang='it-IT', last=False,
               cats=['Antipasti', 'Zuppe', 'Insalate del buffet', 'Piatti principali', 'Dessert'],
               cheese=['Formaggi nazionali e internazionali', 'dal carrello'],
               name='Menu_serale_{dd}_{mm}.docx'),
}


def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def para(kind, text, L):
    if kind in ('title', 'stars'):
        sz = '40' if kind == 'title' else '32'
        rpr = RF + '<w:b/><w:bCs/><w:i/><w:spacing w:val="30"/><w:sz w:val="%s"/><w:szCs w:val="%s"/><w:lang w:val="%s"/>' % (sz, sz, L)
    elif kind == 'empty1':
        rpr = RF + '<w:b/><w:i/><w:spacing w:val="30"/><w:szCs w:val="30"/><w:u w:val="single"/><w:lang w:val="%s"/>' % L
        return '<w:p><w:pPr><w:jc w:val="center"/><w:rPr>%s</w:rPr></w:pPr></w:p>' % rpr
    elif kind == 'empty':
        rpr = RF + '<w:i/><w:spacing w:val="30"/><w:szCs w:val="30"/><w:lang w:val="%s"/>' % L
        return '<w:p><w:pPr><w:jc w:val="center"/><w:rPr>%s</w:rPr></w:pPr></w:p>' % rpr
    elif kind == 'last':
        return '<w:p><w:pPr><w:rPr>' + RF + '<w:lang w:val="%s"/></w:rPr></w:pPr></w:p>' % L
    elif kind == 'cat':
        rpr = RF + '<w:b/><w:i/><w:spacing w:val="30"/><w:sz w:val="30"/><w:szCs w:val="30"/><w:u w:val="single"/><w:lang w:val="%s"/>' % L
    elif kind == 'dish':
        rpr = RF + '<w:i/><w:spacing w:val="30"/><w:sz w:val="26"/><w:szCs w:val="30"/><w:lang w:val="%s"/>' % L
    elif kind == 'or':
        rpr = RF + '<w:b/><w:bCs/><w:i/><w:spacing w:val="30"/><w:sz w:val="27"/><w:szCs w:val="27"/><w:lang w:val="%s"/>' % L
    elif kind == 'sep':
        rpr = RF + '<w:i/><w:spacing w:val="30"/><w:sz w:val="29"/><w:szCs w:val="30"/><w:lang w:val="%s"/>' % L
        text = '***'
    else:
        raise ValueError(kind)
    ppr = '<w:jc w:val="center"/><w:rPr>%s</w:rPr>' % rpr
    return ('<w:p><w:pPr>%s</w:pPr><w:r><w:rPr>%s</w:rPr><w:t xml:space="preserve">%s</w:t></w:r></w:p>'
            % (ppr, rpr, esc(text)))


def parse(text, cfg):
    """Copy-paste text -> paragraph sequence (without title and cheese)."""
    skip = {cfg['title'], '*' * 12, cfg['cheese'][0], cfg['cheese'][1]}
    items, expect_cat, open_course = [], True, False
    for raw in text.splitlines():
        line = raw.strip().replace("'", '’')
        if not line or line in skip:
            continue
        if line == '***':
            items += [('sep', ''), ('empty', '')]
            expect_cat, open_course = True, False
        elif line == cfg['sep_word']:
            items.append(('or', cfg['sep_word']))
        elif line in cfg['cats'] and not expect_cat:   # forgotten separator before a new course
            items += [('sep', ''), ('empty', ''), ('cat', line)]
            open_course = True
        elif expect_cat:
            items.append(('cat', line))
            expect_cat, open_course = False, True
        else:
            items.append(('dish', line))
    if open_course:                      # forgotten closing separator
        items += [('sep', ''), ('empty', '')]
    return items


def body(items, cfg):
    L = cfg['lang']
    seq = [('title', cfg['title']), ('stars', '*' * 12), ('empty1', '')] + items
    seq += [('dish', c) for c in cfg['cheese']]
    if cfg['last']:
        seq.append(('last', ''))
    return ''.join(para(k, t, L) for k, t in seq)


SECTPR = ('<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>'
          '<w:pgMar w:top="568" w:right="1286" w:bottom="284" w:left="1260" '
          'w:header="720" w:footer="720" w:gutter="0"/><w:cols w:space="720"/></w:sectPr>')
X = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r\n'
W = 'http://schemas.openxmlformats.org/'
DOC = (X + '<w:document xmlns:w="' + W + 'wordprocessingml/2006/main" xmlns:r="' + W +
       'officeDocument/2006/relationships"><w:body>%s' + SECTPR + '</w:body></w:document>')
CT = (X + '<Types xmlns="' + W + 'package/2006/content-types">'
      '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
      '<Default Extension="xml" ContentType="application/xml"/>'
      '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
      '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
      '</Types>')
RELS = (X + '<Relationships xmlns="' + W + 'package/2006/relationships">'
        '<Relationship Id="rId1" Type="' + W + 'officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
        '</Relationships>')
DOCRELS = (X + '<Relationships xmlns="' + W + 'package/2006/relationships">'
           '<Relationship Id="rId1" Type="' + W + 'officeDocument/2006/relationships/styles" Target="styles.xml"/>'
           '</Relationships>')
STYLES = (X + '<w:styles xmlns:w="' + W + 'wordprocessingml/2006/main">'
          '<w:docDefaults><w:rPrDefault><w:rPr>' + RF + '<w:sz w:val="26"/><w:szCs w:val="26"/></w:rPr></w:rPrDefault>'
          '<w:pPrDefault><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>'
          '<w:style w:type="paragraph" w:default="1" w:styleId="Standard"><w:name w:val="Normal"/>'
          '<w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/></w:pPr>'
          '<w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'
          '<w:sz w:val="26"/><w:szCs w:val="26"/></w:rPr></w:style></w:styles>')


def write(path, doc_xml):
    """Writes the package without docProps (no author, no company, fixed timestamps)."""
    if os.path.exists(path):
        os.remove(path)
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as z:
        for n, c in [('[Content_Types].xml', CT), ('_rels/.rels', RELS),
                     ('word/_rels/document.xml.rels', DOCRELS), ('word/document.xml', doc_xml),
                     ('word/styles.xml', STYLES)]:
            info = zipfile.ZipInfo(n, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, c)


def main():
    if len(sys.argv) < 5:
        sys.exit(__doc__)
    d = datetime.datetime.strptime(sys.argv[1], '%d.%m.%Y')
    out = sys.argv[5] if len(sys.argv) > 5 else 'outputs'
    os.makedirs(out, exist_ok=True)
    fmt = dict(dd='%02d' % d.day, mm='%02d' % d.month, yyyy=d.year)
    for code, src in zip(('en', 'fr', 'it'), sys.argv[2:5]):
        cfg = LANGS[code]
        with open(src, encoding='utf-8') as f:
            items = parse(f.read(), cfg)
        path = os.path.join(out, cfg['name'].format(**fmt))
        write(path, DOC % body(items, cfg))
        print('created:', path)


if __name__ == '__main__':
    main()

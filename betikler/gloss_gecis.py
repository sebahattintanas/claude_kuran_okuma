# -*- coding: utf-8 -*-
"""gloss_gecis.py — blok kapanış protokolünün 'kök anmaları otomatik gloss
geçişinden geçirilir' şartını uygular.

Metinde harekesiz geçen HER kök adının ardına kok_turkce.json'daki karşılığı
*(...)* biçiminde ekler. Karşılık ELLE YAZILMAZ, tablodan alınır — böylece
turkce_denetim.py ile aynı kaynağı kullanır ve ihlâl üretmez.

Harekeli alıntılar (ör. دَآبَّةً مِّنَ ٱلْأَرْضِ) zaten denetimin regexine
takılmaz; bu geçiş onlara dokunmaz.
"""
import json, re, os

for _p in ('kok_turkce.json', '../tablolar/kok_turkce.json'):
    if os.path.exists(_p):
        KOK = json.load(open(_p, encoding='utf-8'))
        break
ROOTS = set(KOK)
AR = re.compile(r'[\u0621-\u064A]{2,5}')
KARSILIK = re.compile(r'^\s*\*?\(([^)]{2,})\)')   # turkce_denetim.py ile birebir aynı


def gecir(metin):
    """Karşılıksız kök anmalarına tablodan karşılık ekler."""
    if not isinstance(metin, str):
        return metin
    out, son = [], 0
    for m in AR.finditer(metin):
        w = m.group()
        if w not in ROOTS:
            continue
        if KARSILIK.match(metin[m.end():m.end() + 120]):
            continue
        out.append(metin[son:m.end()])
        out.append(' *(%s)*' % KOK[w])
        son = m.end()
    out.append(metin[son:])
    return ''.join(out)


def gecir_kayit(rec, alanlar=('olcum', 'mercek')):
    for a in alanlar:
        if a in rec:
            rec[a] = gecir(rec[a])
    return rec

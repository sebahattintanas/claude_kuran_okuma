# -*- coding: utf-8 -*-
"""duzeltme_101.py — sûre 101 okumasında düşen kendi kayıtlarımı işler (idempotent).
Özgün alan KORUNUR; kayda 'duzeltildi' listesi eklenir (karia_kayit.DUZELTME'den). Blok betiği yeniden
koşulursa bu betik de yeniden koşulmalı (sad_kapanis.py koşuyor)."""
import json
from karia_kayit import DUZELTME
S = 101
p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
n = 0
for a, d in DUZELTME.items():
    rec = OM[str(S)]['%d:%d' % (S, a)]
    assert d['eski'] in rec[d['alan']], 'düzeltilen ifade özgün alanda yok — DUR'
    L = rec.setdefault('duzeltildi', [])
    if not any(x.get('aday') == d['aday'] for x in L):
        L.append(dict(d)); n += 1
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('düzeltme eklendi:', n, '· toplam', len(DUZELTME))

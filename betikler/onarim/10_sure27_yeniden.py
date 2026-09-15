# -*- coding: utf-8 -*-
"""ONARIM 8 — sûre 27'yi onarılmış alanlarla YENİDEN ÖLÇ ve farkı çıkar.
Okuma metni ESKİ alanlarla yazıldı; bu tablo hangi ölçümlerin değiştiğini gösterir.
"""
import json
from collections import Counter
D = json.load(open('defter.json')); DD = {tuple(r['k']): r for r in D}
S = 27
print('=== SÛRE 27 — ESKİ / YENİ ALAN KARŞILAŞTIRMASI ===\n')

ea = sum(len(DD[(S,a)]['adsiz']) for a in range(1,94))
ya = sum(len(DD[(S,a)]['adsiz2']) for a in range(1,94))
eay = [a for a in range(1,94) if DD[(S,a)]['adsiz']]
yay = [a for a in range(1,94) if DD[(S,a)]['adsiz2']]
print('ADSIZ AKTÖR   eski %d token / %d ayet %s' % (ea, len(eay), eay))
print('              YENİ %d token / %d ayet %s' % (ya, len(yay), yay))
for a in yay:
    print('                 27:%-3d %s' % (a, DD[(S,a)]['adsiz2']))
print()
en = [a for a in range(1,94) if DD[(S,a)]['dugum']['nakarat']]
yn = [a for a in range(1,94) if DD[(S,a)]['nakarat2']]
print('NAKARAT       eski %d ayet | YENİ %d ayet' % (len(en), len(yn)))
K = json.load(open('nakarat_kaliplari.json', encoding='utf-8'))['27']
guclu = [(g,v) for g,v in K if len(v) >= 3 or len(g.split()) >= 4]
print('              güçlü kalıplar (>=3 ayet ya da >=4 kelime): %d' % len(guclu))
for g,v in sorted(guclu, key=lambda x:(-len(x[1]),-len(x[0].split()))):
    print('                 %d ayet  %-34s %s' % (len(v), g, v))
print()
ee = [a for a in range(1,94) if DD[(S,a)].get('esit')]
ye = [a for a in range(1,94) if DD[(S,a)]['esit2']]
print('ESİT          eski %d ayet %s' % (len(ee), ee))
print('              YENİ %d ayet %s' % (len(ye), ye))
for a in ye:
    for e in DD[(S,a)]['esit2']:
        if e[3]=='yakin': print('                 27:%-3d ↔ %d:%-3d  %.4f  YAKIN (eski alan görmüyordu)' % (a,e[0],e[1],e[2]))
print()
ed = Counter(t for a in range(1,94) for _,_,t in DD[(S,a)]['adli'])
yd = Counter(t for a in range(1,94) for _,_,t in DD[(S,a)]['adli2'])
print('ADLI AKTÖR    eski %s' % dict(ed))
print('              YENİ %s' % dict(yd))
print()
em = [a for a in range(1,94) if 'MM' in (DD[(S,a)].get('fig') or [])]
ym = [a for a in range(1,94) if DD[(S,a)]['mm2']]
print('MM            eski %s | YENİ %s' % (em, ym))

# -*- coding: utf-8 -*-
"""İMAN-AYETLERİ vs İNKÂR-AYETLERİ kök profili.
Ölçüm: her kök için, kökün 'iman ayetlerinde' ve 'inkâr ayetlerinde' görülme
oranı; korpus taban oranına göre log-odds. Her iki gruba da giren ayetler
(171 ayet) DIŞARIDA bırakılır ki kontrast saf olsun."""
import kuran_akis as K, json
from collections import defaultdict, Counter
from math import log, lgamma, exp
ak = K.kelime_akisi()
ayet = defaultdict(set); kok_ayet = defaultdict(set)
for x in ak:
    k = (x['key'][0], x['key'][1])
    if x['kok']: ayet[k].add(x['kok']); kok_ayet[x['kok']].add(k)
IMAN = {'أمن'}; INKAR = {'كفر','ظلم','نفق','فسق'}
A = {k for k,v in ayet.items() if (v & IMAN) and not (v & INKAR)}
B = {k for k,v in ayet.items() if (v & INKAR) and not (v & IMAN)}
print('iman-ayetleri (saf): %d | inkâr-ayetleri (saf): %d | kesişim dışlandı: %d'
      % (len(A), len(B), len({k for k,v in ayet.items() if (v&IMAN) and (v&INKAR)})))
adlar = json.load(open('kok_adlar.json'))
def ad(k):
    v = adlar.get(k); return v['ad'] if isinstance(v,dict) else (v or k)
res = []
for kok, ks in kok_ayet.items():
    if kok in IMAN or kok in INKAR: continue
    a = len(ks & A); b = len(ks & B)
    if a + b < 12: continue
    # +0.5 düzeltmeli log-odds, grup büyüklüğüne normalize
    lo = log(((a+0.5)/len(A)) / ((b+0.5)/len(B)))
    res.append((lo, a, b, kok))
res.sort()
print()
print('=== İNKÂR ayetlerine kayan kökler (en güçlü 18) ===')
print('%-9s %-22s %5s %5s %7s' % ('kök','anlam','iman','inkâr','log-odds'))
for lo,a,b,k in res[:18]:
    print('%-9s %-22s %5d %5d %7.2f' % (k, ad(k)[:22], a, b, lo))
print()
print('=== İMAN ayetlerine kayan kökler (en güçlü 18) ===')
for lo,a,b,k in res[-18:][::-1]:
    print('%-9s %-22s %5d %5d %7.2f' % (k, ad(k)[:22], a, b, lo))

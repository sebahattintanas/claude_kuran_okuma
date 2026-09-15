# -*- coding: utf-8 -*-
"""ONARIM 9 — ADAY 781'İN KONTROLLÜ ÇİFTİ: sûre 26 ve 27'nin nakarat karşılaştırması.
Onarılmış `nakarat2` ile artık YAPILABİLİR (aday 870'in uyarısı kalkıyor).
"""
import json
from collections import Counter, defaultdict

D = json.load(open('defter.json')); DD = {tuple(r['k']): r for r in D}
K = json.load(open('nakarat_kaliplari.json', encoding='utf-8'))

def rapor(s, amax):
    ayet = [a for a in range(1, amax+1) if DD[(s,a)]['nakarat2']]
    tam  = [a for a in range(1, amax+1) if any(x[2]=='tam' for x in DD[(s,a)]['nakarat2'])]
    ic   = [a for a in range(1, amax+1) if any(x[2]=='ic' for x in DD[(s,a)]['nakarat2'])]
    kal = K[str(s)]
    guclu = [(g,v) for g,v in kal if len(v) >= 3]
    # nakaratın kapladığı KELİME oranı
    kelime = 0; toplam = 0
    for a in range(1, amax+1):
        n = DD[(s,a)]['n']; toplam += n
        en = max([len(x[0].split()) for x in DD[(s,a)]['nakarat2']], default=0)
        kelime += min(en, n)
    return {'ayet': amax, 'nakaratli_ayet': len(ayet), 'oran': len(ayet)/amax,
            'tam': len(tam), 'ic': len(ic), 'kalip': len(kal), 'guclu_kalip': len(guclu),
            'kelime_orani': kelime/toplam, 'guclu': guclu}

R26 = rapor(26, 227); R27 = rapor(27, 93)
print('=== ADAY 781 — SÛRE 26 / 27 KONTROLLÜ ÇİFTİ, NAKARAT ===')
print('%-26s %10s %10s' % ('', 'sûre 26', 'sûre 27'))
for k, ad in [('ayet','ayet sayısı'), ('nakaratli_ayet','nakaratlı ayet'),
              ('tam','TAM ayet nakaratı'), ('ic','ayet-İÇİ nakarat'),
              ('kalip','farklı kalıp'), ('guclu_kalip','güçlü kalıp (>=3 ayet)')]:
    print('%-26s %10s %10s' % (ad, R26[k], R27[k]))
print('%-26s %9.1f%% %9.1f%%' % ('nakaratlı ayet oranı', R26['oran']*100, R27['oran']*100))
print('%-26s %9.1f%% %9.1f%%' % ('nakaratın kelime payı', R26['kelime_orani']*100, R27['kelime_orani']*100))
print()
print('--- sûre 26 güçlü kalıpları')
for g,v in sorted(R26['guclu'], key=lambda x:-len(x[1])):
    print('   %3d ayet  n=%-2d  %s' % (len(v), len(g.split()), g[:52]))
print('--- sûre 27 güçlü kalıpları')
for g,v in sorted(R27['guclu'], key=lambda x:-len(x[1])):
    print('   %3d ayet  n=%-2d  %-32s %s' % (len(v), len(g.split()), g, v))
print()
print('=== YILDIZ / NAKARAT ÇAPRAZI (aday 700/739/771 nakarat düzeltmesi) ===')
for s, amax in ((26,227),(27,93)):
    nak = {a for a in range(1,amax+1) if DD[(s,a)]['nakarat2']}
    y3n = [a for a in nak if DD[(s,a)].get('yildiz',0)==3]
    y3d = [a for a in range(1,amax+1) if a not in nak and DD[(s,a)].get('yildiz',0)==3]
    print('sûre %d: ★★★ toplam %d | nakaratlı ayette %d | nakaratsız ayette %d'
          % (s, y3n and len(y3n)+len(y3d) or len(y3d), len(y3n), len(y3d)))
    print('        nakaratlı ayet %d (%.1f%%) · nakaratsız %d' % (len(nak), 100*len(nak)/amax, amax-len(nak)))

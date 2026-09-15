# -*- coding: utf-8 -*-
"""ONARIM 5 — adlı aktör: korpusun PN etiketindeki CİNS İSİMLER ayrılır.
ONARIM 6 — MM (mef'ûl-i mutlak): aşırı dar ölçüt genişletilir.

ADLI (aday 868, TEŞHİS DÜZELTMESİ): arıza aktor2.py'nin envanterinde DEĞİL —
pn_lemma_listesi.json korpusla birebir aynı (106 = 106). PN etiketini veren
MORFOLOJİNİN KENDİSİ; مُسْلِم ve نَصْرانِيّ gibi mensubiyet/soyut adlar orada
PN sayılmış. Bu yüzden silme değil, YENİDEN SINIFLAMA yapılıyor: yeni tür
'cins'. Hiçbir token kaybolmaz, aktör sayımından ayrılır.

MM (aday 867): eski kural V + aynı kökten N (bitişik) -> 175 ayet (fazla geniş);
yeni kural V + aynı kökten VN -> 3 ayet (fazla dar). Ara ölçüt:
V + aynı kökten N + ACC (mef'ûl-i mutlak nasb alır).
"""
import re, json
from collections import defaultdict, Counter

L = json.load(open('pn_lemma_listesi.json', encoding='utf-8'))
# mensubiyet / soyut adlar — indeksle seçildi, elle Arapça yazılmadı
CINS_IDX = [23, 24, 33, 36, 47, 52, 74, 81]
CINS = {L[i] for i in CINS_IDX}

tok = defaultdict(list)
for ln in open('morph.txt', encoding='utf-8'):
    p = ln.rstrip('\n').split('\t')
    if len(p) < 4: continue
    loc = p[0].split(':')
    if len(loc) == 5: loc = loc[1:]
    if len(loc) != 4: continue
    tok[(int(loc[0]), int(loc[1]))].append({'w': int(loc[2]), 'g': int(loc[3]),
                                            'pos': p[2], 'f': p[3]})

D = json.load(open('defter.json'))
for r in D:
    yeni = []
    for w, lm, t in r['adli']:
        yeni.append([w, lm, 'cins' if lm in CINS else t])
    r['adli2'] = yeni

    # --- MM ara ölçüt
    S = tok.get((r['k'][0], r['k'][1]), [])
    # KELİME düzeyinde: w. kelimede aynı kökten V, w+1. kelimede aynı kökten ACC isim.
    # (Segment düzeyi yanlıştı: مَكَرُوا۟ fiilinden sonra zamir bölütü geliyor.)
    W = defaultdict(list)
    for s_ in S: W[s_['w']].append(s_)
    mm = []
    for w in sorted(W):
        if w + 1 not in W: continue
        fiil = {re.search(r'ROOT:([^|]+)', x['f']).group(1)
                for x in W[w] if x['pos'] == 'V' and 'ROOT:' in x['f']}
        isim = {re.search(r'ROOT:([^|]+)', x['f']).group(1)
                for x in W[w+1] if x['pos'] == 'N' and 'ROOT:' in x['f']
                and 'ACC' in x['f'].split('|')}
        ort = fiil & isim
        for kk in sorted(ort): mm.append([w, kk])
    r['mm2'] = mm
json.dump(D, open('defter.json', 'w', encoding='utf-8'), ensure_ascii=False)

print('=== ADLI AKTÖR ONARIMI ===')
e = Counter(t for r in D for _, _, t in r['adli'])
y = Counter(t for r in D for _, _, t in r['adli2'])
print('ESKİ tür dağılımı:', dict(e.most_common()))
print('YENİ tür dağılımı:', dict(y.most_common()))
print("'cins' olarak ayrılan lemma ve token:")
for i in CINS_IDX:
    n = sum(1 for r in D for _, lm, _ in r['adli2'] if lm == L[i])
    print('   %3d  n=%-4d' % (i, n))
print('toplam ayrılan token: %d  (adlı aktör 25 -> %d etkilenen sûre 27 tokeni)' %
      (sum(1 for r in D for _, lm, _ in r['adli2'] if lm in CINS),
       sum(1 for r in D if r['k'][0] == 27 for _, lm, _ in r['adli2'] if lm in CINS)))
print('KAYIP: 0 (silme değil yeniden sınıflama)')
print()
print('=== MM ONARIMI ===')
eski3 = [tuple(r['k']) for r in D if 'MM' in (r.get('fig') or [])]
yeni = [tuple(r['k']) for r in D if r['mm2']]
print('eski GENİŞ kural (V + aynı kök N):        175 ayet')
print('eski DAR kural (V + aynı kök VN):           %d ayet  %s' % (len(eski3), eski3))
print('YENİ ARA kural (V + aynı kök N + ACC):     %d ayet' % len(yeni))
print('dar kuralın ayetleri yeni kuralda var mı:', all(k in yeni for k in eski3))
print()
SIN = [((27, 50), True, 'مَكَرُوا۟ مَكْرًا — ders kitabı örneği, dar kural kaçırıyordu'),
       ((27, 21), True, 'لَأُعَذِّبَنَّهُۥ عَذَابًا'),
       ((27, 88), True, 'تَمُرُّ مَرَّ — dar kuralın yakaladığı tek sûre 27 ayeti'),
       ((27, 58), False, 'أَمْطَرْنَا ... مَطَرًا — bitişik değil, ara kural da yakalamaz')]
DD = {tuple(r['k']): r for r in D}
g = 0
for k, bekle, ac in SIN:
    var = bool(DD[k]['mm2']); g += (var == bekle)
    print('  %-8s beklenen=%-5s yeni=%-5s %s  %s' % ('%d:%d' % k, bekle, var,
          'GEÇTİ' if var == bekle else '**DÜŞTÜ**', ac))
print('  sınama: %d/%d' % (g, len(SIN)))
print('sûre 27 mm2 ayetleri:', [a for a in range(1, 94) if DD[(27, a)]['mm2']])

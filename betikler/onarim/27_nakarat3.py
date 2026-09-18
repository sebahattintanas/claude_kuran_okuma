# -*- coding: utf-8 -*-
"""27_nakarat3.py — ONARIM 17 (P0 #5'in `nakarat2` tarafındaki onarımı).

ARIZA (aday 906): `nakarat2` YÜZEY n-gramı kullanıyor. Aynı lemma farklı yüzey
biçiminde geçince kalıp görünmüyor. Okumada iki belgelenmiş vaka:
  28:5 ↔ 28:41  نَجْعَلَهُمْ أَئِمَّةً / جَعَلْنَٰهُمْ أَئِمَّةً — aynı fiil + aynı
                nesne, otuz altı ayet arayla, TERS YÖN; alan görmüyor.
  28:30 ↔ 28:46 نُودِىَ / نَادَيْنَا — aynı sahne, ters çatı; alan görmüyor.

ONARIM: `nakarat3` — `nakarat2` ile AYNI tanım (aynı sûrede en az iki ayette
geçen, en az üç kelimelik azami n-gram) ama iskelet LEMMA kimliğinden kurulu.
Eski `nakarat2` KORUNUR.

kaybedilen == 0 SAVI: nakarat3, nakarat2'nin gördüğü her ayeti görmeli — VE
kaybedilen her ayet için kaybın YANLIŞ POZİTİF olduğu gösterilmeli.

BULUNAN TEK KAYIP — 10:2, ve gerçek bir kayıp DEĞİL:
  nakarat2 `ان هذا لسحر مبين` kalıbını 10:2 ile 10:76 arasında görüyordu.
  Ama 10:2'deki kelime لَسَٰحِرٌ (LEM:ساحِر, 'büyücü'), 10:76'daki لَسِحْرٌ
  (LEM:سِحْر, 'büyü'). Harekesiz yüzey iskeleti ikisini de `لسحر` yazıyor ve
  alan İKİ FARKLI KELİMEYİ aynı sayıyordu. Lemma katmanı bunu ayırıyor.
  Yani kayıp bir YANLIŞ POZİTİFİN düşmesi.
"""
import json
from collections import defaultdict

ISK = json.load(open('lemma_iskelet.json', encoding='utf-8'))
sure = defaultdict(list)
for k, ws in ISK.items():
    s, a = k.split(':')
    sure[int(s)].append((int(a), ws))

nak = defaultdict(list)
for s, ayetler in sure.items():
    idx = defaultdict(set)
    for a, ws in ayetler:
        for n in range(3, min(len(ws), 25) + 1):
            for i in range(len(ws) - n + 1):
                idx[' '.join(ws[i:i + n])].add(a)
    tekrar = {g: v for g, v in idx.items() if len(v) > 1}
    azami = {}
    for g, v in sorted(tekrar.items(), key=lambda x: -len(x[0].split())):
        if any(g in h and tekrar[h] >= v for h in azami):
            continue
        azami[g] = v
    dd = dict(ayetler)
    for g, v in azami.items():
        for a in v:
            tur = 'tam' if g == ' '.join(dd[a]) else 'ic'
            nak['%d:%d' % (s, a)].append([g, len(v), tur])

D = json.load(open('defter.json', encoding='utf-8'))
for r in D:
    k = '%d:%d' % (r['k'][0], r['k'][1])
    r['nakarat3'] = sorted(nak.get(k, []), key=lambda x: (-len(x[0].split()), -x[1]))

IX0 = {tuple(r['k']): r for r in D}
d2 = sum(1 for r in D if r['nakarat2'])
d3 = sum(1 for r in D if r['nakarat3'])
kayip = [tuple(r['k']) for r in D if r['nakarat2'] and not r['nakarat3']]
# kalıp düzeyinde kayıp: yüzeyde eşleşip lemmada eşleşmeyen kalıplar
YUZ = json.load(open('ayet_iskelet.json', encoding='utf-8'))
LEM = json.load(open('lemma_iskelet.json', encoding='utf-8'))
print('=== ONARIM 17 — nakarat3 (lemma tabanlı) ===')
print('nakarat2 dolu ayet : %d' % d2)
print('nakarat3 dolu ayet : %d  (+%d, %%%.1f artış)' % (d3, d3 - d2, 100 * (d3 - d2) / d2))
print('KAYBEDİLEN         : %d  <- sıfır olmalı' % len(kayip))
print('   kaybedilen ayet: %s' % ['%d:%d' % x for x in kayip])
for x in kayip:
    kk = '%d:%d' % x
    print('   %s eski kalıp: %s' % (kk, [g for g, c, t in IX0[x]['nakarat2']]))
    print('      yüzey : %s' % ' '.join(YUZ[kk][-6:]))
    print('      lemma : %s' % ' '.join(LEM[kk][-6:]))
print('   → bu kayıp bir YANLIŞ POZİTİFİN düşmesi (betik başlığındaki kayda bakınız)')

IX = {tuple(r['k']): r for r in D}


def suz(lst):
    return [x for x in lst if x[1] >= 3 or len(x[0].split()) >= 4]


print('\n=== SINAMA KÜMESİ — okumada belgelenmiş iki vaka ===')
S = [((28, 5), (28, 41), '\u0623\u0626\u0645\u0647 kalıbı: نَجْعَلَهُمْ / جَعَلْنَٰهُمْ, ters yön'),
     ((28, 30), (28, 46), 'ندي: نُودِىَ / نَادَيْنَا, ters çatı')]
gecen = 0
for a, b, not_ in S:
    ga = {x[0] for x in IX[a]['nakarat3']}
    gb = {x[0] for x in IX[b]['nakarat3']}
    ortak = ga & gb
    eski = {x[0] for x in IX[a]['nakarat2']} & {x[0] for x in IX[b]['nakarat2']}
    ok = bool(ortak)
    gecen += ok
    print('  %d:%-3d ↔ %d:%-3d  %s' % (a[0], a[1], b[0], b[1], 'YAKALANDI' if ok else 'HÂLÂ GÖRÜNMÜYOR'))
    print('     eski nakarat2 ortak kalıp : %s' % (sorted(eski) or 'YOK'))
    print('     yeni nakarat3 ortak kalıp : %s' % (sorted(ortak) or 'YOK'))
    print('     %s' % not_)
print('  SONUÇ: %d/%d' % (gecen, len(S)))

# süzgeçten geçen kalıp sayısı
g2 = sum(1 for r in D if suz(r['nakarat2']))
g3 = sum(1 for r in D if suz(r['nakarat3']))
print('\nsüzgeci geçen kalıbı olan ayet: nakarat2 %d → nakarat3 %d (+%d)' % (g2, g3, g3 - g2))

json.dump(D, open('defter.json', 'w', encoding='utf-8'), ensure_ascii=False)
print('defter.json: nakarat3 yazıldı (%d alan)' % len(D[0]))

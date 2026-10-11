# -*- coding: utf-8 -*-
"""aday1039_test.py — aday 1039'un (sûre 39, blok 21-30'da açıldı) önceden yazılmış testi.
Yalnız ÖLÇÜM tarafı koşulur (defter.json: esit2, nakarat3). Karşıt çift bir OKUMA kaydıdır;
kontrol sûresinde okuma kaydı olmadığı için o kol karşılaştırılmaz, yalnız sûre 39 için betimlenir.
H0: fark yok. Tohum sabit (0). Sayılar elle yazılmaz."""
import json, random, re, collections
D = json.load(open('defter.json', encoding='utf-8'))
by = collections.defaultdict(list)
for r in D: by[r['k'][0]].append(r)
for s in by: by[s].sort(key=lambda r: r['k'][1])

def gecer(r):  # olcum_bicim ile aynı süzgeç: cnt>=3 ya da >=4 kelime
    return any(cnt >= 3 or len(ng.split()) >= 4 for ng, cnt, tip in r['nakarat3'])
def esit(r): return bool(r['esit2'])
def tam(r): return any(x[3] == 'tam' for x in r['esit2'])
def bag(r): return esit(r) or gecer(r)

def oran(rs, f): return sum(1 for r in rs if f(r)) / len(rs)
OLC = {'esit2_herhangi': esit, 'esit2_TAM': tam, 'nakarat3_GECER': gecer, 'birlesik(esit2|nakarat3)': bag}

# öz-tanım ayetleri (aday 1039 metin sayımı): kitap için muteşâbih / mesânî / min kulli mesel
OZ = [(3, 7), (15, 87), (17, 89), (18, 54), (30, 58), (39, 23), (39, 27)]
OZ_SURE = sorted({s for s, _ in OZ})

out = {'uyari': 'aday 1039 testi — ölçüm kolu. Karşıt çift kolu yalnız betimsel (kontrol sûresinde okuma kaydı yok).', 'tohum': 0}

# (1) sûre 39 değerleri
out['sure39'] = {k: round(oran(by[39], f), 4) for k, f in OLC.items()}
out['sure39_sayim'] = {k: sum(1 for r in by[39] if f(r)) for k, f in OLC.items()}

# (2) uzunluk eşleştirilmiş kontrol: öz-tanım ayeti içermeyen, ayet sayısı ±15 ve kelime ±%25 içinde
n39 = len(by[39]); w39 = sum(r['n'] for r in by[39])
band = [s for s in by if s not in OZ_SURE and abs(len(by[s]) - n39) <= 15 and abs(sum(r['n'] for r in by[s]) - w39) <= 0.25 * w39]
out['kontrol_band'] = {str(s): {'ayet': len(by[s]), 'kelime': sum(r['n'] for r in by[s]),
                                **{k: round(oran(by[s], f), 4) for k, f in OLC.items()}} for s in sorted(band)}
out['sure39_boyut'] = {'ayet': n39, 'kelime': w39}
# en yakın tek kontrol (ayet, sonra kelime farkı)
best = min(band, key=lambda s: (abs(len(by[s]) - n39), abs(sum(r['n'] for r in by[s]) - w39)))
out['kontrol_tek'] = best
out['sure39_band_sirasi'] = {k: '%d/%d (büyükten küçüğe; 39 dahil)' % (
    1 + sum(1 for s in band if oran(by[s], f) > oran(by[39], f)), len(band) + 1) for k, f in OLC.items()}
# 2x2 Fisher (39 vs tek kontrol), iki yönlü — scipy yoksa elle
from math import comb
def fisher(a, b, c, d):
    n = a + b + c + d; r1 = a + b; c1 = a + c
    def p(x): return comb(r1, x) * comb(n - r1, c1 - x) / comb(n, c1)
    p0 = p(a); lo = max(0, c1 - (n - r1)); hi = min(r1, c1)
    return min(1.0, sum(p(x) for x in range(lo, hi + 1) if p(x) <= p0 + 1e-12))
out['fisher_39_vs_kontrol'] = {}
for k, f in OLC.items():
    a = sum(1 for r in by[39] if f(r)); b = n39 - a
    c = sum(1 for r in by[best] if f(r)); d = len(by[best]) - c
    out['fisher_39_vs_kontrol'][k] = {'39': '%d/%d' % (a, n39), str(best): '%d/%d' % (c, len(by[best])), 'p_iki_yonlu': round(fisher(a, b, c, d), 4)}

# (3) öz-tanım ayetleri çevresinde ±10 ayet yoğunluğu — sûre içi permütasyon (rastgele merkez, aynı sûre)
rnd = random.Random(0); R = 2000
def pencere(s, m):
    rs = by[s]; return [r for r in rs if abs(r['k'][1] - m) <= 10 and r['k'][1] != m]
out['pencere_10'] = {}
for k, f in OLC.items():
    gozlenen = []; null = []
    for s, m in OZ:
        w = pencere(s, m); gozlenen.append(oran(w, f) - oran(by[s], f))
    obs = sum(gozlenen) / len(gozlenen)
    for _ in range(R):
        v = []
        for s, m in OZ:
            mm = rnd.randint(1, len(by[s])); w = pencere(s, mm)
            v.append(oran(w, f) - oran(by[s], f))
        null.append(sum(v) / len(v))
    p = (1 + sum(1 for x in null if x >= obs)) / (R + 1)
    out['pencere_10'][k] = {'ortalama_fark(pencere-sure)': round(obs, 4),
                            'ayet_bazinda': {'%d:%d' % sm: round(g, 4) for sm, g in zip(OZ, gozlenen)},
                            'p_tek_yonlu(pencere>sure)': round(p, 4)}
out['bonferroni_esik'] = round(0.05 / (2 * len(OLC)), 4)

# karşıt çift — betimsel (yalnız sûre 39, okuma kaydı ◇'de 'Karşıt çift' geçen ayetler; kayıt 39:21'den itibaren)
import zumer_metin_1 as Z
kc = sorted(n for n, m in Z.M.items() if 'Karşıt çift' in m or 'karşıt çift' in m)
out['karsit_cift_okuma_39'] = {'ayet': kc, 'sayi': len(kc),
                               'not': 'okuma kaydı; sistematik kayıt 39:21-75 (55 ayet); 39:1-20 için aday 1039 listesindeki 7 çift ayrıca; kontrol sûresinde karşılığı YOK — karşılaştırılmadı'}
json.dump(out, open('/home/claude/repo/bulgular/aday1039_test.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1))

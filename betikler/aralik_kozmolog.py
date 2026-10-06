# -*- coding: utf-8 -*-
"""aralik_kozmolog.py — ◈K Kozmolog merceğinin TETİK listesi (notlar/ONKAYIT_mercekler.md §3, commit a7e9628 — DEĞİŞTİRİLMEDEN)
aralık okumasına uygulanır. (1) dört ağır okuma aralığında ayet ayet tetik, (2) korpus düzeyinde aralık içi profil.
Betimleyici; null yok. Okuma kayıtlarına (okuma_metni) YAZMAZ — §7 geriye dönük doldurma yasağına uyulur."""
import json, collections, unicodedata as ud, re
N = lambda s: ud.normalize('NFC', s)
TETIK = {'gök-yer': 'سمو أرض شمس قمر نجم كوكب ليل نهر فلك سحب ريح موه بحر جبل',
         'zaman': 'يوم أجل سنن عمر ساعة دهر أبد حين'}
ENV = {N(k): k for k in json.load(open('tablolar/kok_envanteri.json', encoding='utf-8'))}
KOK2SIN = {}; OLU = []
for s, l in TETIK.items():
    for r in l.split():
        if N(r) not in ENV: OLU.append(r); continue   # ön-kayıttaki ÖLÜ kök: sessizce 0 eşleşir — RAPORLANIR, düzeltilmez
        KOK2SIN[N(r)] = s
F = open('veri/morph.txt', encoding='utf-8').read().splitlines()
lemref = lambda ref: N([t for l in F if l.startswith(ref + '\t') for t in l.split('\t')[3].split('|') if t.startswith('LEM:')][0])
ALL = lemref('1:1:2:1')
W = collections.OrderedDict()
for l in F:
    p = l.split('\t')
    if len(p) < 4 or p[0].count(':') != 3: continue
    s, a, w, _ = map(int, p[0].split(':'))
    d = W.setdefault((s, a, w), {'kok': set(), 'A': False})
    t = [N(x) for x in p[3].split('|')]
    if ALL in t: d['A'] = True
    for x in t:
        if x.startswith('ROOT:'): d['kok'].add(x[5:])
K = list(W); IDX = [i for i, k in enumerate(K) if W[k]['A']]
SP = [(a, b) for a, b in zip(IDX, IDX[1:]) if K[a][0] == K[b][0]]
bio = lambda k: [KOK2SIN[r] for r in W[k]['kok'] if r in KOK2SIN]
R = {'olu_kok': OLU}
# (1) dört aralık
ARAL = {'35:18→22': (35, 18, 22), '16:9→18': (16, 9, 18), '10:6→10': (10, 6, 10), '53:58→62': (53, 58, 62)}
for ad, (s, a1, a2) in ARAL.items():
    a, b = next(x for x in SP if K[x[0]][:2] == (s, a1) and K[x[1]][:2] == (s, a2))
    ay = collections.OrderedDict()
    for k in K[a + 1:b]:
        for r in W[k]['kok']:
            if r in KOK2SIN: ay.setdefault('%d:%d' % k[:2], []).append('%s(%s)' % (r, KOK2SIN[r]))
    R[ad] = {'kelime': b - a - 1, 'tetik': sum(len(v) for v in ay.values()), 'ayet': ay}
# (2) korpus: oranlar ve onda-birlik profil
tot = sum(bool(bio(k)) for k in K) / len(K)
ins = [k for a, b in SP for k in K[a + 1:b]]
near = set()
for i in IDX:
    for j in range(max(0, i - 6), min(len(K), i + 7)):
        if K[j][0] == K[i][0] and j != i: near.add(j)
R['oran_100'] = {'korpus': round(100 * tot, 2), 'aralik_ici': round(100 * sum(bool(bio(k)) for k in ins) / len(ins), 2),
                 'lafiz_pm6': round(100 * sum(bool(bio(K[j])) for j in near) / len(near), 2)}
L = [x for x in SP if x[1] - x[0] - 1 >= 10]
for s in ['hepsi'] + list(TETIK):
    d = [0] * 10; t = [0] * 10
    for a, b in L:
        ins = K[a + 1:b]
        for i, k in enumerate(ins):
            q = min(9, int(10 * i / len(ins))); t[q] += 1
            d[q] += (bool(bio(k)) if s == 'hepsi' else (s in bio(k)))
    R.setdefault('onda_birlik_10plus', {})[s] = [round(100 * d[i] / t[i], 1) for i in range(10)]
# sınıf oranları: aralık içi vs lafız ±6
for s in TETIK:
    R.setdefault('sinif_100', {})[s] = {'aralik_ici': round(100 * sum(s in bio(k) for a, b in SP for k in K[a + 1:b]) / sum(b - a - 1 for a, b in SP), 2),
                                        'lafiz_pm6': round(100 * sum(s in bio(K[j]) for j in near) / len(near), 2)}
json.dump(R, open('ciktilar/aralik_kozmolog.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(R, ensure_ascii=False, indent=1))

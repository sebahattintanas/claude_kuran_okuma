# -*- coding: utf-8 -*-
"""kuran_aralik_sayfalari.py — KATMAN 1 (otomatik): bütün Kur'an, lafız-çapalı bloklar (≥200 kelime), mushaf ↔ ters okuma.
Kesim kuralı (2026-10-05, kullanıcı kararı: eşik 200):
  1. Ham kesit sınırları: her LEM=اللَّه tokeni ve her sûre başı (aralık = lafızdan bir sonraki lafza).
  2. 400 kelimeyi aşan ham kesit ayet sınırlarında bölünür: birikim ≥200 iken Rab (LEM رَبّ) içeren bir ayetin başında (İKİNCİL ÇAPA);
     Rab yoksa birikim ≥400 olunca bir sonraki ayet başında (DÜZ KESİM).
  3. Kesitler açgözlü birleştirilir; blok ≥200 kelime olunca kapanır. Satır = kesit (aralık), sayfa = blok.
İşaretler OTOMATİK ve DOĞRULANMAMIŞTIR (esmâ göndergesi, 1P'nin kimin sesi olduğu, edilgenin faili ölçülmez).
Meal yalnız okuma_metni.json'da ayet düzeyinde kayıtlı ayetler için (çalışma çevirisi). Okunmamış ayet hakkında not YOK.
Depo kökünden: python3 betikler/kuran_aralik_sayfalari.py → ciktilar/kuran_aralik_sayfalari.html"""
import json, unicodedata as ud, collections, statistics as st
N = lambda s: ud.normalize('NFC', s)
F = open('veri/morph.txt', encoding='utf-8').read().splitlines()
def lem(ref): return N([t for l in F if l.startswith(ref + '\t') for t in l.split('\t')[3].split('|') if t.startswith('LEM:')][0])
L_ALL, L_RAB, L_UMM = lem('1:1:2:1'), lem('1:2:3:1'), lem('3:26:2:1')
ESMA = {'LEM:' + N(x) for x in json.load(open('tablolar/esma_listesi.json', encoding='utf-8'))['lemmalar']}
W = collections.OrderedDict()
for l in F:
    p = l.split('\t')
    if len(p) < 4 or p[0].count(':') != 3: continue
    s, a, w, _ = map(int, p[0].split(':'))
    t = set(N(x) for x in p[3].strip().split('|'))
    d = W.setdefault((s, a, w), {'f': '', 'b': 0})
    d['f'] += p[1]
    b = 0
    if L_ALL in t: b |= 1
    if L_RAB in t: b |= 2
    if ESMA & t: b |= 4
    if any(x.startswith('PASS') for x in t): b |= 8
    if '1P' in t: b |= 16
    if L_UMM in t: b |= 32
    d['b'] |= b
K = list(W); n = len(K)
# 1. ham kesitler
cut = sorted({i for i, k in enumerate(K) if W[k]['b'] & 1} | {i for i in range(n) if i == 0 or K[i][0] != K[i - 1][0]})
cut.append(n)
raw = [(cut[i], cut[i + 1], 'lafız' if W[K[cut[i]]]['b'] & 1 else 'sûre') for i in range(len(cut) - 1)]
# 2. uzun kesitleri ayet sınırında böl
def verse_starts(a, b): return [i for i in range(a, b) if i == a or K[i][:2] != K[i - 1][:2]]
sub = []
for a, b, tip in raw:
    if b - a <= 400: sub.append((a, b, tip)); continue
    vs = verse_starts(a, b); st_ = a; t0 = tip
    vrab = {v for v in vs if any(W[K[j]]['b'] & 2 for j in range(v, next((x for x in vs if x > v), b)))}
    for v in vs[1:]:
        acc = v - st_
        if (acc >= 200 and v in vrab) or acc >= 400:
            sub.append((st_, v, t0)); t0 = 'Rab' if v in vrab and acc >= 200 else 'düz'; st_ = v
    sub.append((st_, b, t0))
# 3. birleştir
pages = []; cur = []
for s in sub:
    cur.append(s)
    if s[1] - cur[0][0] >= 200: pages.append(cur); cur = []
if cur:
    if pages and cur[-1][1] - cur[0][0] < 100: pages[-1] += cur
    else: pages.append(cur)
sz = [p[-1][1] - p[0][0] for p in pages]
ozet = {'sayfa': len(pages), 'kesit': len(sub), 'medyan': st.median(sz), 'min': min(sz), 'max': max(sz),
        'kesim': dict(collections.Counter(p[0][2] for p in pages))}
print(json.dumps(ozet, ensure_ascii=False))
# veri
d = json.load(open('veri/kuran_veri.json', encoding='utf-8'))['sureler']
AR = {f"{s['no']}:{a['no']}": a['ar_saf'].replace('\ufeff', '') for s in d for a in s['ayetler']}
AD = {s['no']: s['ad'] for s in d}
o = json.load(open('notlar/okuma_metni.json', encoding='utf-8'))
MEAL = {}
for s, v in o.items():
    if s.isdigit() and isinstance(v, dict):
        for k, r in v.items():
            if ':' in k and isinstance(r, dict) and r.get('meal'): MEAL[k] = r['meal']
TOK = [[K[i][0], K[i][1], W[K[i]]['f'], W[K[i]]['b']] for i in range(n)]
PG = [[[a, b, t] for a, b, t in p] for p in pages]
DATA = {'tok': TOK, 'pg': PG, 'ar': AR, 'meal': MEAL, 'ad': AD, 'ozet': ozet}
tpl = open('betikler/kuran_aralik_sablon.html', encoding='utf-8').read()
html = tpl.replace('/*__DATA__*/null', json.dumps(DATA, ensure_ascii=False, separators=(',', ':')))
open('ciktilar/kuran_aralik_sayfalari.html', 'w', encoding='utf-8').write(html)
print('boyut MB', round(len(html.encode()) / 1e6, 2), '| meal', len(MEAL))

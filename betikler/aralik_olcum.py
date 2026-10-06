# -*- coding: utf-8 -*-
"""aralik_olcum.py — LAFIZDAN LAFZA ARALIK OKUMASI (2026-10-05, ayrı oturum) için tüm sayımlar.
Depo kökünden koşulur: python3 betikler/aralik_olcum.py  →  ciktilar/aralik_olcum.json
Tanım: aralık = sûre içinde ardışık iki LEM=اللَّه tokeni arasındaki kelimeler (sûre sınırını geçenler dışlanır).
DİKKAT: اللَّهُمَّ ayrı lemma (5 token) — bu tanımda SINIR DEĞİL (aday 1030). Anahtarlar korpustan kopyalanır, NFC.
Bütün sayılar BETİMLEYİCİ; null model yok. Örneklem tohumları 2026/2027/2028/2029 (oturumdaki sırayla)."""
import json, random, collections, statistics as st, unicodedata as ud
N = lambda s: ud.normalize('NFC', s)
F = open('veri/morph.txt', encoding='utf-8').read().splitlines()
def lem(ref):
    for l in F:
        if l.startswith(ref + '\t'):
            return N([t for t in l.split('\t')[3].split('|') if t.startswith('LEM:')][0])
ALL, RAB, ALLAHUMME = lem('1:1:2:1'), lem('1:2:3:1'), lem('3:26:2:1')
ESMA = {'LEM:' + N(x) for x in json.load(open('tablolar/esma_listesi.json', encoding='utf-8'))['lemmalar']}
W = collections.OrderedDict(); FORM = {}
for l in F:
    p = l.split('\t')
    if len(p) < 4 or p[0].count(':') != 3: continue
    s, a, w, _ = map(int, p[0].split(':'))
    W.setdefault((s, a, w), []).append([N(x) for x in p[3].split('|')])
    FORM[(s, a, w)] = FORM.get((s, a, w), '') + p[1]
K = list(W); VLEN = collections.Counter(k[:2] for k in K)
has = lambda k, L: any(L in s for s in W[k])
def case(k):
    for s in W[k]:
        if ALL in s: return next((x for x in s if x in ('NOM', 'ACC', 'GEN')), '?')
p1 = lambda k: any('1P' in s for s in W[k])
p3ms = lambda k: any('PRON' in s and '3MS' in s for s in W[k])
esma = lambda k: any(ESMA & set(s) for s in W[k])
IDX = [i for i, k in enumerate(K) if has(k, ALL)]
SP = [(a, b) for a, b in zip(IDX, IDX[1:]) if K[a][0] == K[b][0]]
ay = lambda x: K[x[1]][1] - K[x[0]][1]
kat = lambda x: 'A' if ay(x) == 0 else 'B' if ay(x) <= 3 else 'C' if ay(x) <= 10 else 'D'
lab = lambda x: '%d:%d:%d→%d:%d:%d' % (K[x[0]] + K[x[1]])
R = {'tanim': __doc__, 'allah_token': len(IDX), 'aralik': len(SP)}
g = [b - a - 1 for a, b in SP]
R['uzunluk'] = {'medyan': st.median(g), 'ort': round(st.mean(g), 1), 'max': max(g)}
R['sinif'] = dict(collections.Counter(kat(x) for x in SP))
# örneklem — oturumdaki sırayla
seen = set(); ORN = {}
rng = random.Random(2026); o = []
for k, n in [('A', 1), ('B', 2), ('C', 1), ('D', 1)]: o += rng.sample([x for x in SP if kat(x) == k], n)
ORN['2026'] = [lab(x) for x in o]; seen |= {K[x[0]][:2] for x in o}
rng = random.Random(2027); o = []
for k, n in [('A', 1), ('B', 2), ('C', 1), ('D', 1)]: o += rng.sample([x for x in SP if kat(x) == k], n)
dup = [x for x in o if kat(x) == 'D' and K[x[0]][:2] in seen]
if dup:  # D katmanı tekrar düştü → aynı tohumla yeniden çekim
    o = [x for x in o if x not in dup] + [random.Random(2027).choice([x for x in SP if kat(x) == 'D' and x not in dup])]
ORN['2027'] = [lab(x) for x in o]; seen |= {K[x[0]][:2] for x in o}
rng = random.Random(2028)
o = rng.sample([x for x in SP if kat(x) == 'B' and K[x[0]][:2] not in seen], 1) + rng.sample([x for x in SP if kat(x) == 'C' and K[x[0]][:2] not in seen], 2)
ORN['2028'] = [lab(x) for x in o]; seen |= {K[x[0]][:2] for x in o}
rng = random.Random(2029); o = []
for k in 'BCD': o += rng.sample([x for x in SP if kat(x) == k and K[x[0]][:2] not in seen], 1)
ORN['2029'] = [lab(x) for x in o]
R['orneklem'] = ORN
# taşıyıcı tablosu
T = {}
for c in 'ABCD':
    xs = [x for x in SP if kat(x) == c]; ins = [K[a + 1:b] for a, b in xs]; tot = sum(map(len, ins))
    r = [sum(has(k, RAB) for k in i) for i in ins]; b = [sum(p1(k) for k in i) for i in ins]
    T[c] = {'n': len(xs), 'kelime': tot, 'rab_100': round(100 * sum(r) / tot, 2), '1P_100': round(100 * sum(b) / tot, 2),
            'rab_var_%': round(100 * sum(v > 0 for v in r) / len(xs)), '1P_var_%': round(100 * sum(v > 0 for v in b) / len(xs)),
            'ikisi_yok_%': round(100 * sum(r[i] == 0 and b[i] == 0 for i in range(len(xs))) / len(xs))}
T['korpus'] = {'rab_100': round(100 * sum(has(k, RAB) for k in K) / len(K), 2), '1P_100': round(100 * sum(p1(k) for k in K) / len(K), 2)}
R['tasiyici'] = T
R['tasiyicisiz_4plus'] = [lab(x) + ' (%d kel.)' % (x[1] - x[0] - 1) for x in sorted(SP, key=lambda x: x[0] - x[1])
                          if ay(x) >= 4 and not any(has(k, RAB) or p1(k) for k in K[x[0] + 1:x[1]])]
# hal geçişi
M = collections.Counter((case(K[a]), case(K[b])) for a, b in SP)
c = collections.Counter(case(K[i]) for i in IDX); n = sum(c.values())
R['hal'] = {'dagilim': dict(c), 'matris_bas_son': {f'{x}>{y}': M[(x, y)] for x in ('NOM', 'ACC', 'GEN') for y in ('NOM', 'ACC', 'GEN')},
            'farkli_gozlenen': round(sum(v for (x, y), v in M.items() if x != y) / len(SP), 3),
            'farkli_bagimsizlik': round(1 - sum((v / n) ** 2 for v in c.values()), 3)}
# yön: ayet içi konum ve onda-birlik profil
rel = lambda k: (k[2] - 1) / max(1, VLEN[k[:2]] - 1)
L = [x for x in SP if K[x[0]][:2] != K[x[1]][:2]]
R['ayet_ici_konum_ARTEFAKT'] = {'n': len(L), 'bas_medyan': round(st.median(rel(K[a]) for a, b in L), 2), 'son_medyan': round(st.median(rel(K[b]) for a, b in L), 2),
                                'not': 'ayet sınırını geçen aralıkta baş lafzı tanım gereği o ayetin SON, bitiş lafzı İLK lafzı — seçim artefaktı'}
L = [x for x in SP if x[1] - x[0] - 1 >= 10]; P = {}
for nm, fn in [('3MS_zamir', p3ms), ('esma', esma), ('rab', lambda k: has(k, RAB))]:
    d = [0] * 10; t = [0] * 10
    for a, b in L:
        ins = K[a + 1:b]
        for i, k in enumerate(ins): q = min(9, int(10 * i / len(ins))); t[q] += 1; d[q] += fn(k)
    P[nm] = [round(100 * d[i] / t[i], 1) for i in range(10)]
R['onda_birlik_profil_10plus'] = {'n': len(L), **P}
R['allahumme'] = [p for p in (l.split('\t')[0] for l in F if ALLAHUMME in [N(x) for x in l.split('\t')[3].split('|')] if len(l.split('\t')) > 3)]
# ظُلُمَة / نُور sayı
def say(root_ref):
    L0 = lem(root_ref); c = collections.Counter()
    for k in K:
        for s in W[k]:
            if L0 in s: c['çoğul' if any(x in ('MP', 'FP', 'P') for x in s) else 'tekil'] += 1
    return dict(c)
R['zulumat_nur'] = {'ظُلُمَة (35:20:2:2)': say('35:20:2:2'), 'نُور (35:20:4:2)': say('35:20:4:2')}
json.dump(R, open('ciktilar/aralik_olcum.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in R.items() if k != 'tanim'}, ensure_ascii=False, indent=1))

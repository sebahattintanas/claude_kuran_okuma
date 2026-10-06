# -*- coding: utf-8 -*-
"""yon_testi.py — notlar/ONKAYIT_yon_testi.md uygulaması (ön-kayıttan SONRA yazıldı). Depo kökünden koşulur."""
import json, random, collections, unicodedata as ud
N = lambda s: ud.normalize('NFC', s)
F = open('veri/morph.txt', encoding='utf-8').read().splitlines()
lem = lambda ref: N([t for l in F if l.startswith(ref + '\t') for t in l.split('\t')[3].split('|') if t.startswith('LEM:')][0])
L_ALL, L_RAB = lem('1:1:2:1'), lem('1:2:3:1')
ESMA = {'LEM:' + N(x) for x in json.load(open('tablolar/esma_listesi.json', encoding='utf-8'))['lemmalar']}
segs = collections.defaultdict(list)
for l in F:
    p = l.split('\t')
    if len(p) < 4 or p[0].count(':') != 3: continue
    s, a, w, _ = map(int, p[0].split(':'))
    segs[(s, a, w)].append(set(N(x) for x in p[3].strip().split('|')))
def durum(ts):
    u = set().union(*ts)
    if L_ALL in u: return 'L'
    if L_RAB in u: return 'R'
    if ESMA & u: return 'E'
    if any('PRON' in t and '3MS' in t for t in ts): return 'O'
    if '1P' in u: return 'B'
    if any(x.startswith('PASS') for x in u): return 'P'
    return None
AY = collections.OrderedDict()
for (s, a, w), ts in segs.items():
    d = durum(ts)
    AY.setdefault((s, a), [])
    if d: AY[(s, a)].append(d)
ST = 'LREOBP'
def say(seq_by_verse):
    n = collections.Counter(); prev = None; ps = None
    for (s, a), ev in seq_by_verse:
        for e in ev:
            if prev is not None and ps == s and e != prev: n[(prev, e)] += 1
            prev, ps = e, s
    return n
def istat(n):
    tot = sum(n.values())
    A = sum(abs(n[(i, j)] - n[(j, i)]) for x, i in enumerate(ST) for j in ST[x + 1:]) / tot
    return {'A': A, 'P1': n[('L', 'O')] - n[('O', 'L')], 'P2': n[('L', 'E')] - n[('E', 'L')], 'P3': n[('R', 'O')] - n[('O', 'R')]}
R = {'onkayit': 'notlar/ONKAYIT_yon_testi.md'}
for yari, f in (('tek', lambda s: s % 2 == 1), ('çift', lambda s: s % 2 == 0)):
    V = [((s, a), ev) for (s, a), ev in AY.items() if f(s)]
    n = say(V); obs = istat(n)
    rng = random.Random(2026); nul = {k: [] for k in obs}
    for _ in range(1000):
        Vr = [(k, ev[::-1] if rng.random() < 0.5 else ev) for k, ev in V]
        x = istat(say(Vr))
        for k in x: nul[k].append(x[k])
    sonuc = {}
    for k in obs:
        p = (sum(v >= obs[k] for v in nul[k]) + 1) / (len(nul[k]) + 1)
        sonuc[k] = {'gozlenen': round(obs[k], 4), 'null_ort': round(sum(nul[k]) / len(nul[k]), 4), 'p_tek_yonlu': round(p, 4)}
    sonuc['sayimlar'] = {f'{i}>{j}': n[(i, j)] for i, j in [('L', 'O'), ('O', 'L'), ('L', 'E'), ('E', 'L'), ('R', 'O'), ('O', 'R')]}
    sonuc['olay_gecis_toplam'] = sum(n.values())
    R[yari] = sonuc
karar = {}
for h in ('A', 'P1', 'P2', 'P3'):
    ok = [R[y][h]['p_tek_yonlu'] < 0.05 and (h == 'A' or R[y][h]['gozlenen'] > 0) for y in ('tek', 'çift')]
    karar[h] = 'TUTTU' if all(ok) else ('KISMİ' if any(ok) else 'TUTMADI')
R['karar'] = karar
json.dump(R, open('ciktilar/yon_testi.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(R, ensure_ascii=False, indent=1))

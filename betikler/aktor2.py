# -*- coding: utf-8 -*-
"""defter v6 — AKTÖR KATMANI (düzeltilmiş)
DÜZELTME: ilk sürümde PN lemma anahtarları ELLE YAZILMIŞTI ve Unicode
uyuşmazlığı yüzünden 2989 token 'diğer'e düştü (اللَّه dahil). Projenin
kayıtlı kuralı: lemma anahtarları asla elle yazılmaz, korpus çıktısından
kopyalanır. Sınıflama artık pn_lemma_listesi.json'daki İNDEKSLER üzerinden.
"""
import re, json
from collections import defaultdict, Counter

PN = json.load(open('pn_lemma_listesi.json', encoding='utf-8'))
# indeks -> tür  (liste sırası: pn_lemma_listesi.json)
IDX = {}
for i in [1,4,5,9,10,11,12,14,15,17,19,20,21,22,25,28,29,31,34,35,37,39,40,41,42,45,49,50,53,54,56,58,62,64,65,77,79,85,87,94]:
    IDX[i] = 'kisi'
for i in [2,27,48,59,60,66,68,69]: IDX[i] = 'gayb'
for i in [8,13,16,23,24,32,33,47,63,81,83,103,105]: IDX[i] = 'kavim'
for i in [3,7,30,43,44,46,55,57,61,67,70,71,73,75,76,78,80,82,84,88,89,96,102,104]: IDX[i] = 'yer'
for i in [6,18,26,51]: IDX[i] = 'kitab'
for i in [90,91,92,93,86,97,98,99,100,101]: IDX[i] = 'sahte-ilah'
for i in [36,38,52,72,74,95]: IDX[i] = 'diger'
IDX[0] = 'ilahi'
TUR = {PN[i]: t for i, t in IDX.items() if i < len(PN)}

tok = defaultdict(list)
for ln in open('morph.txt', encoding='utf-8'):
    p = ln.rstrip('\n').split('\t')
    if len(p) < 4: continue
    loc = p[0].split(':')
    if len(loc) == 5: loc = loc[1:]
    if len(loc) != 4: continue
    tok[(int(loc[0]), int(loc[1]))].append({'w': int(loc[2]), 'ar': p[1], 'pos': p[2], 'f': p[3]})

def lem(f):
    m = re.search(r'LEM:([^|]+)', f); return m.group(1) if m else ''

# adsız aktör işaretçileri — lemma anahtarları korpustan
ADSIZ_KOK = {'رجل':'racül','مرأ':'imrae','نفر':'nefer','فرق':'ferîk','طوف':'tâife','قرى':'karye'}

D = json.load(open('defter.json'))
aktor = defaultdict(list)
for r in D:
    S = tok.get((r['k'][0], r['k'][1]), [])
    adli = []; adsiz = []; rol = {}
    for i, s in enumerate(S):
        p = s['f'].split('|'); L = lem(s['f'])
        if 'PN' in p and L and TUR.get(L) not in ('ilahi', None):
            t = TUR.get(L, 'diger')
            adli.append([s['w'], L, t])
            rr = []
            if 'NOM' in p: rr.append('fail')
            if 'ACC' in p: rr.append('meful')
            if 'GEN' in p: rr.append('mecrur')
            if i > 0 and 'VOC' in S[i-1]['f'].split('|'): rr.append('muhatap')
            for q in S[max(0, i-2):i]:
                if re.search(r'ROOT:قول', q['f']) and q['pos'] == 'V': rr.append('konusan'); break
            if rr: rol.setdefault(L, []).extend(rr)
            if t in ('kisi', 'gayb', 'kavim'):
                aktor[L].append([r['k'][0], r['k'][1], sorted(set(rr))])
        elif 'INDEF' in p and s['pos'] == 'N':
            m = re.search(r'ROOT:([^|]+)', s['f'])
            if m and m.group(1) in ADSIZ_KOK:
                adsiz.append([s['w'], ADSIZ_KOK[m.group(1)]])
    r['adli'] = adli; r['adsiz'] = adsiz
    r['rol'] = {a: sorted(set(b)) for a, b in rol.items()}

json.dump(D, open('defter.json', 'w', encoding='utf-8'), ensure_ascii=False)
json.dump(dict(aktor), open('aktor_tablosu.json', 'w', encoding='utf-8'), ensure_ascii=False)
json.dump(TUR, open('pn_turleri.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

print('adlı varlık içeren ayet: %d' % sum(1 for r in D if r['adli']))
print('adsız aktör işaretçisi: %d ayet' % sum(1 for r in D if r['adsiz']))
print('her ikisi birden: %d ayet' % sum(1 for r in D if r['adli'] and r['adsiz']))
print('aktör tablosu: %d aktör' % len(aktor))
print('türler:', dict(Counter(t for r in D for _, _, t in r['adli']).most_common()))
print('rol:', dict(Counter(x for r in D for v in r['rol'].values() for x in v)))
print('adsız:', dict(Counter(x[1] for r in D for x in r['adsiz']).most_common()))

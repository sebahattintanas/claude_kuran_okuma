# -*- coding: utf-8 -*-
"""defter v3 — okuma turu için son alanlar.
  nuz    nüzûl sıra numarası (sûrenin)
  tip    'M' Mekkî / 'D' Medenî
  esma   [[kelime_sıra, lemma], ...]  ayette geçen bütün ilâhî ad/sıfat
  xref   [[ortak_lemma_3gram, [[s,a],...]], ...] seyrek lemma-dizisi bağları
  z      {olcut: z-skor}  ve  yildiz  0..3
"""
import json, re
from collections import Counter, defaultdict
from statistics import mean, pstdev
import kuran_akis as K

D = json.load(open('defter.json'))
ak = K.kelime_akisi()
NZ = json.load(open('nuzul.json'))
ESMA = set(json.load(open('esma_listesi.json'))['lemmalar'])
nuz = {s: i+1 for i, s in enumerate(NZ['sira'])}
med = set(NZ['medeni'])

byv = defaultdict(list)
for x in ak: byv[(x['key'][0], x['key'][1])].append(x)

# --- lemma dizisi 3-gram, seyrek (<=3 sûre) ---
gram = defaultdict(set)
for k, v in byv.items():
    L = [x['lem_hsz'] for x in v if x['lem_hsz']]
    for i in range(len(L)-2):
        gram[' '.join(L[i:i+3])].add(k)
seyrek = {g: ks for g, ks in gram.items() if 2 <= len({k[0] for k in ks}) <= 3}
xref = defaultdict(list)
for g, ks in seyrek.items():
    for k in ks:
        xref[k].append([g, sorted([list(z) for z in ks if z != k])])
print('seyrek lemma-3gram: %d | bağı olan ayet: %d' % (len(seyrek), len(xref)))

for r in D:
    k = (r['k'][0], r['k'][1])
    r['nuz'] = nuz[k[0]]
    r['tip'] = 'D' if k[0] in med else 'M'
    r['esma'] = [[x['wid'][2], x['lem_ham']] for x in byv[k] if x['lem_ham'] in ESMA]
    r['xref'] = xref.get(k, [])

# --- anomali z-skorları ---
def zed(vals):
    m, s = mean(vals), pstdev(vals)
    return [(v-m)/s if s else 0.0 for v in vals]
n_ = [r['n'] for r in D]
ad_ = [len(r['A'])/max(r['n'],1) for r in D]
rd_ = [len(r['R'])/max(r['n'],1) for r in D]
hp_ = [len(r['hapaks']) for r in D]
pa_ = [r['pas']/max(sum(r['vf'].values()),1) for r in D]
zs = {'n': zed(n_), 'allah': zed(ad_), 'rab': zed(rd_), 'hapaks': zed(hp_), 'pas': zed(pa_)}
# kafiye kırılması: komşularından farklı sınıf
for i, r in enumerate(D):
    kir = 0
    ayni = [q for q in D if q['k'][0] == r['k'][0]]
    j = r['k'][1]-1
    if 0 < j < len(ayni)-1:
        if ayni[j-1]['fs'][2] == ayni[j+1]['fs'][2] != r['fs'][2]: kir = 1
    z = {a: round(zs[a][i], 2) for a in zs}
    z['kafiye_kirik'] = kir
    r['z'] = z
    mx = max(abs(v) for a, v in z.items() if a != 'kafiye_kirik')
    r['yildiz'] = (3 if mx > 3 else 2 if mx > 2 else 1 if mx > 1.5 else 0) + (1 if kir and mx <= 1.5 else 0)
    r['yildiz'] = min(r['yildiz'], 3)

json.dump(D, open('defter.json', 'w', encoding='utf-8'), ensure_ascii=False)
c = Counter(r['yildiz'] for r in D)
print('yıldız dağılımı:', dict(sorted(c.items())))
print('esmâ içeren ayet: %d | toplam esmâ: %d' % (sum(1 for r in D if r['esma']), sum(len(r['esma']) for r in D)))
print('xref bağı olan ayet: %d' % sum(1 for r in D if r['xref']))
print('Mekkî ayet %d | Medenî ayet %d' % (sum(1 for r in D if r['tip']=='M'), sum(1 for r in D if r['tip']=='D')))

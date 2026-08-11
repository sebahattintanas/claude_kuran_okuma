# -*- coding: utf-8 -*-
"""defter v4 — şahıs/muhatap + iltifât + kip/söz edimi.
Yeni alanlar:
  sah      {şahıs-sayı etiketi: adet}   (1S,1P,2MS,2MP,3MS,3MP,...)
  sahset   ayette bulunan şahıslar {1,2,3}
  bask     baskın şahıs (en çok geçen)
  ilt      iltifât bayrağı: önceki ayetle şahıs kümesi AYRIK ise 1
  ilt_yon  "3>2" gibi geçiş yönü
  kip      {INTG, VOC, IMPV, PRO, NEG, COND, RES, EMPH, CERT, FUT: adet}
  edim     söz edimi etiketleri: soru / emir / yasak / nida / şart / haber
Kaynak: morph.txt etiketleri (INTG 902, VOC 366, IMPV 1956, PRO 332, COND 1029 ...)
NOT: yıldız eşiği DEĞİŞTİRİLMEDİ. iltifât ayrı bir işaret olarak durur;
     kilitli bayrak tanımına sonradan sinyal eklenmedi.
"""
import json, re
from collections import Counter, defaultdict

tok = defaultdict(list)
for ln in open('morph.txt', encoding='utf-8'):
    p = ln.rstrip('\n').split('\t')
    if len(p) < 4: continue
    loc = p[0].split(':')
    if len(loc) == 5: loc = loc[1:]
    if len(loc) != 4: continue
    tok[(int(loc[0]), int(loc[1]))].append((int(loc[2]), p[3]))

SAHIS = re.compile(r'(?:^|\|)([123](?:MS|FS|MD|FD|MP|FP|S|D|P))(?:\||$)')
KIP = ['INTG','VOC','IMPV','PRO','NEG','COND','RES','EMPH','CERT','FUT']

D = json.load(open('defter.json'))
prev = {}
for r in D:
    k = (r['k'][0], r['k'][1])
    fs = tok.get(k, [])
    sah = Counter(); kip = Counter()
    for w, f in fs:
        for m in SAHIS.finditer(f): sah[m.group(1)] += 1
        for t in KIP:
            if t in f.split('|'): kip[t] += 1
    r['sah'] = dict(sah)
    ss = sorted({x[0] for x in sah})
    r['sahset'] = ss
    r['bask'] = max(sah, key=sah.get)[0] if sah else None
    r['kip'] = dict(kip)
    edim = []
    if kip['INTG']: edim.append('soru')
    if kip['IMPV']: edim.append('emir')
    if kip['PRO']: edim.append('yasak')
    if kip['VOC']: edim.append('nida')
    if kip['COND']: edim.append('şart')
    if not edim: edim.append('haber')
    r['edim'] = edim
    # iltifât: aynı sûrede önceki ayetle şahıs kümesi ayrık
    p_ = prev.get(k[0])
    if p_ and ss and p_[0] and not (set(ss) & set(p_[0])):
        r['ilt'] = 1
        r['ilt_yon'] = '%s>%s' % (''.join(p_[0]), ''.join(ss))
    else:
        r['ilt'] = 0; r['ilt_yon'] = None
    if ss: prev[k[0]] = (ss,)

json.dump(D, open('defter.json', 'w', encoding='utf-8'), ensure_ascii=False)

print('defter v4 yazıldı')
tot = Counter()
for r in D:
    for t, n in r['kip'].items(): tot[t] += n
print('kip etiketleri:', dict(tot))
ed = Counter()
for r in D:
    for e in r['edim']: ed[e] += 1
print('söz edimi (ayet sayısı):', dict(ed))
b = Counter(r['bask'] for r in D)
print('baskın şahıs:', dict(b))
ilt = [r for r in D if r['ilt']]
print('iltifât işaretli ayet: %d (%.1f%%)' % (len(ilt), 100*len(ilt)/len(D)))
print('iltifât yönleri:', Counter(r['ilt_yon'] for r in ilt).most_common(8))
sc = Counter(len(r['sahset']) for r in D)
print('ayet başına şahıs çeşidi:', dict(sorted(sc.items())))
# Fâtiha kontrolü
print()
print('--- Fâtiha kontrol ---')
for r in D[:7]:
    print('1:%d  sahset=%s bask=%s ilt=%s(%s) edim=%s kip=%s' % (
        r['k'][1], r['sahset'], r['bask'], r['ilt'], r['ilt_yon'], r['edim'], r['kip']))

# -*- coding: utf-8 -*-
"""ONARIM 2 (v2) — N-GRAM ALTYAPISI, MORFOLOJİ TABANLI.

v1 ARIZASI: iskelet ham metinden kuruluyordu ve bağlaç öneki (و/ف) kelimeye
bitişik kaldığı için 27:82 (ve+vakaa, bitişik) ile 27:85 (vakaa) eşleşmiyordu — aday 854'ün
bulduğu arızanın kelime-bölütleme tarafındaki eşi.

v2: iskelet morph.txt'nin BÖLÜTLERİNDEN kurulur ve `CONJ|PREF` bölütleri
(bağlaç önekleri) atılır. Böylece hem 27:80↔30:52 (baştaki bağlaç) hem
27:82↔27:85 (kelime içine kaynamış bağlaç) aynı düzeltmeyle çözülür.

Ayrıca: kuran_veri.json'da 112 ayetin metnine BESMELE GÖMÜLÜ (veri arızası);
morfoloji tabanlı iskelet bundan zaten etkilenmez.
"""
import re, json, unicodedata
from collections import defaultdict, Counter

HAREKE = re.compile(r'[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED\u08F0-\u08FF]')
def sad(t):
    t = HAREKE.sub('', unicodedata.normalize('NFC', t))
    t = t.replace('\u0671', '\u0627')
    t = re.sub('[\u0622\u0623\u0625\u0649]', '\u0627', t)
    t = t.replace('\u0624', '\u0648').replace('\u0626', '\u064A')
    t = t.replace('\u0629', '\u0647')
    return re.sub(r'[^\u0621-\u064A]', '', t)

kel = defaultdict(lambda: defaultdict(list))
for ln in open('morph.txt', encoding='utf-8'):
    p = ln.rstrip('\n').split('\t')
    if len(p) < 4: continue
    loc = p[0].split(':')
    if len(loc) == 5: loc = loc[1:]
    if len(loc) != 4: continue
    if 'CONJ' in p[3].split('|') and 'PREF' in p[3].split('|'): continue   # bağlaç öneki atılır
    kel[(int(loc[0]), int(loc[1]))][int(loc[2])].append(sad(p[1]))

ISK = {}
for k, ws in kel.items():
    ISK['%d:%d' % k] = [''.join(ws[w]) for w in sorted(ws) if ''.join(ws[w])]

veri = json.load(open('kuran_veri.json', encoding='utf-8'))
eksik = [ '%d:%d' % (s['no'], a['no']) for s in veri['sureler'] for a in s['ayetler']
          if '%d:%d' % (s['no'], a['no']) not in ISK ]
for k in eksik: ISK[k] = []
print('iskelet kurulan ayet: %d  (morfolojide olmayan: %d)' % (len(ISK), len(eksik)))
print('kelime toplamı: %d' % sum(len(v) for v in ISK.values()))

NG = defaultdict(list)
for key, ws in ISK.items():
    for n in range(3, 9):
        for i in range(len(ws) - n + 1):
            NG[' '.join(ws[i:i+n])].append(key)
NG = {g: sorted(set(v)) for g, v in NG.items() if len(set(v)) > 1}

json.dump(ISK, open('ayet_iskelet.json', 'w', encoding='utf-8'), ensure_ascii=False)
json.dump(NG, open('ngram_indeks.json', 'w', encoding='utf-8'), ensure_ascii=False)
print('birden çok ayette geçen n-gram (n=3..8): %d' % len(NG))
print('n dağılımı:', dict(sorted(Counter(len(g.split()) for g in NG).items())))

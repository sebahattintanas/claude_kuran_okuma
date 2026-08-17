# -*- coding: utf-8 -*-
"""oku_blok.py — okuma bloğu için sıkı özet üretir.
Kullanım: python3 oku_blok.py 8 41 60 > blok.txt
"""
import sys, json, re, bisect, random
from collections import Counter, defaultdict
import kuran_akis
from kuran_akis import kelime_akisi, allah_indeksleri, kavram

S = int(sys.argv[1]); A1 = int(sys.argv[2]); A2 = int(sys.argv[3])

veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

D = json.load(open('defter.json', encoding='utf-8'))
DEF = {(r['k'][0], r['k'][1]): r for r in D}

AKIS = kelime_akisi()
ALLAH = allah_indeksleri(AKIS)
# ayet -> akış indeksleri
AY = defaultdict(list)
for x in AKIS:
    AY[x['key']].append(x)

def mesafe(i):
    pos = bisect.bisect_left(ALLAH, i); c = []
    if pos < len(ALLAH): c.append(ALLAH[pos])
    if pos > 0: c.append(ALLAH[pos-1])
    return min((abs(i-a) for a in c), default=None)

for n in range(A1, A2+1):
    k = (S, n)
    if k not in AR: continue
    r = DEF.get(k, {})
    print("="*60)
    print("%d:%d" % k)
    print(AR[k])
    # ölçüm satırı
    fs = r.get('fs', [])
    print("› n=%s mora=%s harf=%s fasila=%s | A=%s R=%s | pas=%s vf=%s irab=%s zmn=%s" % (
        r.get('n'), r.get('mora'), r.get('harf'), fs[1:] if fs else '',
        r.get('A'), r.get('R'), r.get('pas'), r.get('vf'), r.get('irab'), r.get('zmn')))
    print("› edim=%s kip=%s sah=%s ilt=%s(%s) fig=%s sim=%s" % (
        r.get('edim'), r.get('kip'), r.get('sah'), r.get('ilt'), r.get('ilt_yon'),
        r.get('fig'), r.get('sim')))
    print("› esma=%s esma_k=%s | hapaks=%s ikile=%s say=%s" % (
        r.get('esma'), r.get('esma_k'), r.get('hapaks'), r.get('ikile'), r.get('say')))
    print("› yildiz=%s z=%s dugum=%s" % (r.get('yildiz'), r.get('z'), r.get('dugum')))
    print("› adli=%s adsiz=%s rol=%s esit=%s" % (
        r.get('adli'), r.get('adsiz'), r.get('rol'), r.get('esit')))
    x = r.get('xref') or []
    if x: print("› xref=%s" % json.dumps(x, ensure_ascii=False)[:400])
    # dikey: kökler + Allah mesafesi
    kk = []
    for w in AY.get(k, []):
        if not w['kok']: continue
        kv = kavram(w['kok'], w['lem_ham'], w['wid'])
        kk.append("%s(%s)/%s" % (w['kok'], kv, mesafe(w['i'])))
    print("◆ kökler: " + "  ".join(kk))

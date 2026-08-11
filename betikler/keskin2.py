# -*- coding: utf-8 -*-
"""
KESKİN SÜRÜM v2 — ÖN-KAYIT
--------------------------
v1 çöktü: أمّا taksimi tek ayet içinde ender (11 ayet) ve bunların bir kısmı
إمّا (ya…ya) idi — hamze yönü normalize edilince ikisi karışmıştı. ÖLÇÜM
ARTEFAKTI olarak kaydedildi.

Düzeltme:
 (a) أَمَّا (taksim) ile إِمَّا (tahyîr) ayrı tutulur: أ ve إ normalize EDİLMEZ.
 (b) Taksim çoğu yerde AYETLERE YAYILIYOR (فأما … [ayetler] … وأما).
     Bu yüzden dallar sûre içinde, ayet sınırı gözetmeden kurulur.
     Dal = bir أمّا'dan sonraki أمّا'ya kadar; iki dal arası en fazla 12 ayet.

Dal etiketi: dalda أمن kökü → İMAN; كفر/ظلم/فسق/نفق → İNKÂR. İkisi de varsa
    ya da hiçbiri yoksa dal ATILIR.
Dal yüklemi: grup işaretçisinden sonraki İLK POS=V token.
H1: İMAN dalının yüklemi BİLME alanından, İNKÂR dalınınki SÖZ alanından gelir.
İstatistik: 2x2 Fisher. Yüklemlerin tam listesi de raporlanır.
"""
import kuran_akis as K, json, re, unicodedata
from collections import defaultdict
from math import lgamma, exp
ak = K.kelime_akisi()
d = json.load(open('../repo/veri/kuran_veri.json'))
adlar = json.load(open('kok_adlar.json'))
def ad(k):
    v = adlar.get(k); return v['ad'] if isinstance(v, dict) else (v or k)
def sadk(w):
    w = unicodedata.normalize('NFC', w)
    w = re.sub(r'[\u064B-\u0652\u0670\u06DD\u06D6-\u06ED\u0640]', '', w)
    return w.replace('ٱ', 'ا').replace('آ', 'ا')   # أ / إ KORUNUR
AMMA = {'أما', 'فأما', 'وأما'}          # taksim
IMMA = {'إما', 'وإما', 'فإما'}          # tahyîr — dışarıda
IMAN = {'أمن'}; INKAR = {'كفر','ظلم','نفق','فسق'}
SOZ = {'قول'}; BILME = {'علم','يقن','عقل','فقه','بصر','ذكر','دري','شعر','رأي'}

akis = defaultdict(list)   # sûre -> sıralı token listesi
for x in ak: akis[x['key'][0]].append(x)
T = {}
for s in d['sureler']:
    for a in s['ayetler']: T[(s['no'], a['no'])] = a['ar_saf']

isaret = defaultdict(list)  # sûre -> [(token_index_in_akis, ayet)]
for s in d['sureler']:
    poz = {}
    for i, y in enumerate(akis[s['no']]): poz[(y['wid'][1], y['wid'][2])] = i
    for a in s['ayetler']:
        kel = [w for w in a['ar_saf'].split() if re.search(r'[\u0621-\u064A]', w)]
        for j, w in enumerate(kel, start=1):
            if sadk(w) in AMMA and (a['no'], j) in poz:
                isaret[s['no']].append((poz[(a['no'], j)], a['no']))

dallar = []
for sn, lst in isaret.items():
    lst.sort()
    for i, (st, ay) in enumerate(lst):
        if i+1 < len(lst):
            en, ay2 = lst[i+1]
            if ay2 - ay > 12: en = len(akis[sn])
        else: en = len(akis[sn])
        seg = akis[sn][st+1:en]
        koks = {y['kok'] for y in seg}
        ei, ek = bool(koks & IMAN), bool(koks & INKAR)
        if ei == ek: continue
        et = 'İMAN' if ei else 'İNKÂR'
        gi = next((j for j, y in enumerate(seg) if y['kok'] in (IMAN | INKAR)), 0)
        yuk = next((y for y in seg[gi+1:] if y['pos'] == 'V'), None)
        dallar.append((sn, ay, et, yuk['kok'] if yuk else None,
                       yuk['lem_ham'] if yuk else None))

print('taksim dalı (grup-etiketli): %d | sûre: %d' % (len(dallar), len({x[0] for x in dallar})))
print()
tab = {'İMAN': {'soz':0,'bilme':0,'diger':0}, 'İNKÂR': {'soz':0,'bilme':0,'diger':0}}
print('%-9s %-7s %-8s %-14s %s' % ('ayet','dal','kök','yüklem','sınıf'))
for sn, ay, et, kok, lem in dallar:
    s = 'soz' if kok in SOZ else ('bilme' if kok in BILME else 'diger')
    tab[et][s] += 1
    print('%-9s %-7s %-8s %-14s %s' % ('%d:%d'%(sn,ay), et, kok or '-', lem or '-',
                                       s.upper() if s!='diger' else ''))
print()
print('%-8s %-6s %-7s %-6s' % ('', 'SÖZ', 'BİLME', 'diğer'))
for g in ('İMAN','İNKÂR'):
    print('%-8s %-6d %-7d %-6d' % (g, tab[g]['soz'], tab[g]['bilme'], tab[g]['diger']))
a,b = tab['İMAN']['soz'], tab['İMAN']['bilme']
c,e = tab['İNKÂR']['soz'], tab['İNKÂR']['bilme']
def lb(n,k): return lgamma(n+1)-lgamma(k+1)-lgamma(n-k+1)
def hyp(a,b,c,dd):
    n=a+b+c+dd; return exp(lb(a+b,a)+lb(c+dd,c)-lb(n,a+c))
def fisher(a,b,c,dd):
    p0=hyp(a,b,c,dd); tot=0.0; r1,r2,c1=a+b,c+dd,a+c
    for x in range(max(0,c1-r2), min(r1,c1)+1):
        p=hyp(x,r1-x,c1-x,r2-(c1-x))
        if p<=p0*1.0000001: tot+=p
    return tot
print()
print('2x2 SÖZ/BİLME: İMAN %d/%d  İNKÂR %d/%d' % (a,b,c,e))
if a+b+c+e>0: print('Fisher p = %.4g' % fisher(a,b,c,e))

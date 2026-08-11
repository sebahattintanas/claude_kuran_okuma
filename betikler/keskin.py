# -*- coding: utf-8 -*-
"""
KESKİN SÜRÜM — ÖN-KAYIT (hesaplamadan önce sabitlendi)
-------------------------------------------------------
Kaba sürüm (iki_odak.py) NULL döndü; sebebi büyük olasılıkla "grup
işaretçisinden sonraki fiil" yaklaşımının sözdizimsel bağlamayı garanti
etmemesiydi. Keskin sürüm bağlamayı metnin KENDİ taksim yapısına bırakır.

Aday: أمّا edatının en az iki kez geçtiği ayetler (فَأَمَّا … وَأَمَّا).
Bu yapı iki dalı dilbilgisel olarak zorunlu kılar ve her dalın yüklemi
ikinci فَ'den sonra gelir — yani bağlama tahmin değil.

Dal ayrımı: her أمّا'dan bir sonraki أمّا'ya (ya da ayet sonuna) kadar.
Dal etiketi: dal içinde أمن kökü varsa İMAN; كفر/ظلم/فسق/نفق varsa İNKÂR.
Dal yüklemi: dal içindeki İLK POS=V token (grup işaretçisinden sonra).

H1 (kaba sürümdekiyle aynı): İMAN dalının yüklemi BİLME alanından,
    İNKÂR dalının yüklemi SÖZ alanından gelir.
İstatistik: 2x2 Fisher. n küçük olacağı için dal yüklemlerinin TAM LİSTESİ
    de raporlanır; küçük n'de liste p-değerinden bilgilendiricidir.
"""
import kuran_akis as K, json, re, unicodedata
from collections import defaultdict
from math import lgamma, exp

ak = K.kelime_akisi()
d = json.load(open('../repo/veri/kuran_veri.json'))
T = {}
for s in d['sureler']:
    for a in s['ayetler']: T[(s['no'], a['no'])] = a['ar_saf']
ayet = defaultdict(list)
for x in ak: ayet[(x['key'][0], x['key'][1])].append(x)
adlar = json.load(open('kok_adlar.json'))
def ad(k):
    v = adlar.get(k); return v['ad'] if isinstance(v, dict) else (v or k)

def sadk(w):
    w = unicodedata.normalize('NFC', w)
    w = re.sub(r'[\u064B-\u0652\u0670\u06DD\u06D6-\u06ED\u0640]', '', w)
    return w.replace('ٱ','ا').replace('أ','ا').replace('إ','ا').replace('آ','ا')

AMMA = {'اما', 'فاما', 'واما'}
IMAN = {'أمن'}; INKAR = {'كفر','ظلم','نفق','فسق'}
SOZ = {'قول'}
BILME = {'علم','يقن','عقل','فقه','بصر','ذكر','دري','شعر','رأي'}

dallar = []
for k, v in sorted(ayet.items()):
    kelime = [w for w in T[k].split() if re.search(r'[\u0621-\u064A]', w)]
    idx = [i for i, w in enumerate(kelime) if sadk(w) in AMMA]
    if len(idx) < 2: continue
    # token konumlarını kelime sırasına eşle (v zaten sıralı, wid[2] 1-tabanlı)
    for a_i, st in enumerate(idx):
        en = idx[a_i+1] if a_i+1 < len(idx) else len(kelime)
        seg = [y for y in v if st+1 <= y['wid'][2] <= en]
        koks = {y['kok'] for y in seg}
        etiket = 'İMAN' if (koks & IMAN) else ('İNKÂR' if (koks & INKAR) else None)
        if not etiket: continue
        # grup işaretçisinden sonraki ilk fiil
        gi = None
        for j, y in enumerate(seg):
            if y['kok'] in (IMAN | INKAR): gi = j; break
        yuk = None
        for y in seg[(gi or 0)+1:]:
            if y['pos'] == 'V': yuk = y; break
        dallar.append((k, etiket, yuk['kok'] if yuk else None,
                       yuk['lem_ham'] if yuk else None))

print('أمّا-taksimli ve grup-etiketli dal sayısı: %d' % len(dallar))
ayetler = sorted({x[0] for x in dallar})
print('ayet sayısı: %d' % len(ayetler))
print()
tab = {'İMAN': {'soz':0,'bilme':0,'diger':0}, 'İNKÂR': {'soz':0,'bilme':0,'diger':0}}
print('%-9s %-7s %-9s %-14s' % ('ayet','dal','kök','yüklem'))
for k, et, kok, lem in dallar:
    s = 'soz' if kok in SOZ else ('bilme' if kok in BILME else 'diger')
    tab[et][s] += 1
    print('%-9s %-7s %-9s %-14s %s' % ('%d:%d'%k, et, kok or '-', lem or '-',
                                        '' if s=='diger' else '<'+s.upper()+'>'))
print()
print('%-8s %-6s %-7s %-6s' % ('', 'SÖZ', 'BİLME', 'diğer'))
for g in ('İMAN','İNKÂR'):
    print('%-8s %-6d %-7d %-6d' % (g, tab[g]['soz'], tab[g]['bilme'], tab[g]['diger']))
a,b = tab['İMAN']['soz'], tab['İMAN']['bilme']
c,e = tab['İNKÂR']['soz'], tab['İNKÂR']['bilme']
def lb(n,k): return lgamma(n+1)-lgamma(k+1)-lgamma(n-k+1)
def hyp(a,b,c,d):
    n=a+b+c+d; return exp(lb(a+b,a)+lb(c+d,c)-lb(n,a+c))
def fisher(a,b,c,d):
    p0=hyp(a,b,c,d); tot=0.0; r1,r2,c1=a+b,c+d,a+c
    for x in range(max(0,c1-r2), min(r1,c1)+1):
        p=hyp(x,r1-x,c1-x,r2-(c1-x))
        if p<=p0*1.0000001: tot+=p
    return tot
print()
print('2x2 SÖZ/BİLME: İMAN %d/%d  İNKÂR %d/%d' % (a,b,c,e))
if a+b+c+e > 0: print('Fisher p = %.4g' % fisher(a,b,c,e))

# -*- coding: utf-8 -*-
"""ONARIM 8 — `harf` alanının besmele kirliliği (aday 879).

TAM KİRLİLİK TABLOSU (39:1 ile 45:2 birebir aynı ayet):
  KİRLİ : harf (+19) · fHz (-20) · sesli (-2) · ebced (+786) · mod19 (+7) · bits
  TEMİZ : ar_saf · mora · ritim_kod · fasila_tipi · med_yuku_waqf · p0110 · mukattaa
defter.json'a yalnız `harf` giriyor; ötekiler kardeş projenin alanları.
`harf` ayrıca dis_sinav.py ve genelleme.py'de İSTATİSTİĞE giriyor.

ÖNEMLİ SINIR — `harf`İN TANIMI GERİ ÇIKARILAMADI:
  kuran_veri.json'un üreteci depoda YOK. Düz harf sayımı `harf`i üretmiyor:
  temiz 6124 ayette r = 0,99915 ama ortalama +2,94 (std 3,01) sabit bir fazla var
  (muhtemelen hançer elif / hemze kürsüsü gibi işaretler de sayılıyor).
  Bu yüzden alan YENİDEN HESAPLANAMAZ; yalnız besmelenin katkısı ÇIKARILABİLİR.

Onarım: gömülü 112 ayette harf2 = harf - 19  (19 = 1:1'in kendi `harf` değeri,
yani besmelenin aynı kuralla sayılmış karşılığı). Diğer ayetlerde harf2 = harf.
DOĞRULAMA: düzeltmeden sonra 112 ayetin sapma dağılımı temiz ayetlerinkiyle
uyuşmalı.
"""
import re, json, unicodedata, statistics as st
from collections import Counter

veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AY = {}
for s in veri['sureler']:
    for a in s['ayetler']: AY[(s['no'], a['no'])] = a

HAREKE = re.compile(r'[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED\u08F0-\u08FF]')
def say(t):
    t = HAREKE.sub('', unicodedata.normalize('NFC', t))
    return sum(1 for c in t if '\u0621' <= c <= '\u06FF')

gom = {k for k, a in AY.items() if say(a['ar']) > say(a['ar_saf'])}
BES_HARF = AY[(1, 1)]['harf']
print('besmelesi gömülü ayet: %d | besmelenin `harf` değeri: %d' % (len(gom), BES_HARF))

temiz_sapma = [AY[k]['harf'] - say(AY[k]['ar_saf']) for k in AY if k not in gom]
print('TEMİZ ayetlerde sapma (harf - düz sayım): ort %.2f  std %.2f' %
      (st.mean(temiz_sapma), st.pstdev(temiz_sapma)))
onceki = [AY[k]['harf'] - say(AY[k]['ar_saf']) for k in gom]
print('GÖMÜLÜ ayetlerde ONARIM ÖNCESİ sapma    : ort %.2f  std %.2f  aralık %d..%d' %
      (st.mean(onceki), st.pstdev(onceki), min(onceki), max(onceki)))
sonraki = [x - BES_HARF for x in onceki]
print('GÖMÜLÜ ayetlerde ONARIM SONRASI sapma   : ort %.2f  std %.2f  aralık %d..%d' %
      (st.mean(sonraki), st.pstdev(sonraki), min(sonraki), max(sonraki)))
z_once = (st.mean(onceki) - st.mean(temiz_sapma)) / st.pstdev(temiz_sapma)
z_sonra = (st.mean(sonraki) - st.mean(temiz_sapma)) / st.pstdev(temiz_sapma)
print('temiz dağılıma göre z: ONCE %.2f  ->  SONRA %.2f' % (z_once, z_sonra))

D = json.load(open('defter.json'))
for r in D:
    k = (r['k'][0], r['k'][1])
    r['harf2'] = r['harf'] - BES_HARF if k in gom else r['harf']
json.dump(D, open('defter.json', 'w', encoding='utf-8'), ensure_ascii=False)
deg = [(r['k'], r['harf'], r['harf2']) for r in D if r['harf2'] != r['harf']]
print()
print("defter.json 'harf2' yazıldı; eski 'harf' korundu. Değişen ayet: %d" % len(deg))
print('sûre 27 etkilenen:', [('%d:%d' % (k[0], k[1]), e, y) for k, e, y in deg if k[0] == 27])
print()
print('KAPATILAMAZ: fHz · sesli · ebced · mod19 · bits alanları da kirli ve BU PROJEDE')
print('onarılmadı — kardeş projenin (fonetik analiz) alanları. Orada denetlenmeli.')

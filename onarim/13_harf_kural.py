# -*- coding: utf-8 -*-
"""ONARIM 10 — `harf` ALANININ KURALI GERİ ÇIKARILDI (aday 890 kapanıyor).

Yöntem: temiz 6124 ayette (harf − düz harf sayımı) artığı, ar_saf'taki harf-dışı
33 kod noktasının sayımlarına EN KÜÇÜK KARELER ile çözüldü; ağırlıklar yuvarlandı.

SONUÇ — `harf` bir HARF SAYIMI DEĞİL:
  sayılanlar = Arapça harfler (0621-064A) + elif vasla (0671)
             + YİRMİ adet tilâvet/vakf işareti (küçük sîn, küçük mîm, secde
               işareti, rub'u'l-hizb, küçük vâv/yâ, vakf durakları ...)
  sayılmayanlar = harekeler, şedde, sükûn, medde, hemze-üstü, hançer elif (0670)

Yani alan HARF + VAKF/TİLÂVET İŞARETİ sayıyor. Bu işaretler ayet uzunluğuyla değil
DURAK KONUMLARIYLA dağıldığı için, `harf` düz uzunluğun sapmalı bir vekilidir —
ve `dis_sinav.py` ile `genelleme.py`'de istatistiğe giriyor.

Doğrulama: 6124 temiz ayetin 6115'inde kural BİREBİR tutuyor (%99,85).
"""
import re, json, unicodedata
from collections import Counter

veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AY = {}
for s in veri['sureler']:
    for a in s['ayetler']: AY[(s['no'], a['no'])] = a

SAY_EK = [0x0671, 0x06D6, 0x06D7, 0x06D8, 0x06D9, 0x06DA, 0x06DB, 0x06DC, 0x06DE,
          0x06DF, 0x06E0, 0x06E2, 0x06E3, 0x06E5, 0x06E6, 0x06E8, 0x06E9, 0x06EA,
          0x06EB, 0x06EC, 0x06ED]
SAY = {chr(c) for c in SAY_EK}

def harf_kural(t):
    t = unicodedata.normalize('NFC', t)
    return sum(1 for c in t if ('\u0621' <= c <= '\u064A') or c in SAY)

def duz_harf(t):
    t = unicodedata.normalize('NFC', t)
    return sum(1 for c in t if ('\u0621' <= c <= '\u064A') or c == '\u0671')

def isaret(t):
    t = unicodedata.normalize('NFC', t)
    return sum(1 for c in t if c in SAY and c != '\u0671')

H = re.compile(r'[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED\u08F0-\u08FF]')
def base(t):
    t = H.sub('', unicodedata.normalize('NFC', t))
    return sum(1 for c in t if '\u0621' <= c <= '\u064A')
gom = {k for k, a in AY.items() if base(a['ar']) > base(a['ar_saf'])}
temiz = [k for k in AY if k not in gom]

ok = [k for k in temiz if harf_kural(AY[k]['ar_saf']) == AY[k]['harf']]
kotu = [k for k in temiz if harf_kural(AY[k]['ar_saf']) != AY[k]['harf']]
print('=== KURAL DOĞRULAMASI ===')
print('temiz ayet %d | kural birebir tutuyor: %d (%.2f%%) | tutmayan: %d'
      % (len(temiz), len(ok), 100*len(ok)/len(temiz), len(kotu)))
print('tutmayanlar:', ['%d:%d' % k for k in kotu])
print()
ti = sum(isaret(AY[k]['ar_saf']) for k in temiz)
th = sum(AY[k]['harf'] for k in temiz)
print('=== ALANIN BİLEŞİMİ ===')
print('toplam `harf` değeri        : %d' % th)
print('bunun vakf/tilâvet işareti  : %d  (%%%.1f)' % (ti, 100*ti/th))
c = Counter(isaret(AY[k]['ar_saf']) for k in temiz)
print('ayet başına işaret sayısı dağılımı (ilk 8):', dict(sorted(c.items())[:8]))

D = json.load(open('defter.json'))
for r in D:
    k = (r['k'][0], r['k'][1])
    r['harf3'] = duz_harf(AY[k]['ar_saf'])          # SAF harf sayımı (belgeli)
    r['isaret'] = isaret(AY[k]['ar_saf'])           # vakf/tilâvet işareti sayısı
json.dump(D, open('defter.json', 'w', encoding='utf-8'), ensure_ascii=False)
print()
print("defter.json: 'harf3' (saf harf) ve 'isaret' (vakf/tilâvet işareti) yazıldı.")
print("eski 'harf' ve onarım turu 1'deki 'harf2' korundu.")
print('sûre 27 örnek: 27:1 harf=%d harf2=%d harf3=%d isaret=%d'
      % tuple([[r['harf'], r['harf2'], r['harf3'], r['isaret']] for r in D
               if tuple(r['k']) == (27, 1)][0]))

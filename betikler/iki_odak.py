# -*- coding: utf-8 -*-
"""
ÖN-KAYIT (hesaplamadan önce sabitlendi)
--------------------------------------
Gözlem (testi doğuran, kanıt olarak KULLANILMAZ):
  2:26 ve 74:31 aynı mekanizmayı kuruyor — tek işaret, iki yön.
  Her ikisinde de inkâr tarafının yüklemi QÂLE (söz), iman tarafının yüklemi
  bilme/kesinleşme (علم / يقن / أمن).

H1: Kur'an'da iman-grubu ile inkâr-grubu AYNI ayette karşı karşıya konduğunda,
    iman tarafına bağlanan fiiller BİLME/İÇ-DURUM alanından, inkâr tarafına
    bağlananlar SÖZ/KONUŞMA alanından gelme eğilimindedir.

Yöntem:
 1) Grup işaretçileri:
    İMAN  : أمن kökü, POS=N (ismi fâil: مؤمن / آمنوا fiil-grubu dahil)
    İNKÂR : كفر, ظلم, نفق, فسق kökleri
 2) Aday ayet: her iki grubu da içeren ayetler.
 3) Her grup işaretçisinden sonra, ayet içinde bir sonraki grup işaretçisine
    (ya da ayet sonuna) kadar gelen POS=V tokenler o gruba atanır.
 4) Kök sınıfları:
    SÖZ      : قول
    BİLME    : علم, يقن, عقل, فقه, بصر, ذكر, دري, شعر
 5) İstatistik: 2x2 tablo (grup × sınıf), Fisher kesin testi.
Null: fiil-sınıfı atamalarının gruplar arasında rastgele dağıldığı.
Sınır: "sonraki fiil" yaklaşık bir sözdizimsel bağlamadır; i'râb ayrıştırması
    değildir. Sonuç yön gösterir, dilbilgisel kanıt sayılmaz.
"""
import kuran_akis as K, json
from collections import defaultdict, Counter
from math import lgamma, exp

ak = K.kelime_akisi()
ayet = defaultdict(list)
for x in ak: ayet[(x['key'][0], x['key'][1])].append(x)

IMAN = {'أمن'}
INKAR = {'كفر', 'ظلم', 'نفق', 'فسق'}
SOZ = {'قول'}
BILME = {'علم', 'يقن', 'عقل', 'فقه', 'بصر', 'ذكر', 'دري', 'شعر'}

say = {'iman': Counter(), 'inkar': Counter()}
ornek = {'iman': defaultdict(list), 'inkar': defaultdict(list)}
aday = 0
for k, v in sorted(ayet.items()):
    kok = {y['kok'] for y in v}
    if not ((kok & IMAN) and (kok & INKAR)): continue
    aday += 1
    aktif = None
    for y in v:
        if y['kok'] in IMAN: aktif = 'iman'; continue
        if y['kok'] in INKAR: aktif = 'inkar'; continue
        if aktif and y['pos'] == 'V':
            if y['kok'] in SOZ:
                say[aktif]['soz'] += 1; ornek[aktif]['soz'].append('%d:%d' % k)
            elif y['kok'] in BILME:
                say[aktif]['bilme'] += 1; ornek[aktif]['bilme'].append('%d:%d' % k)
            else:
                say[aktif]['diger'] += 1

print('aday ayet (her iki grubu da içeren): %d' % aday)
print()
print('%-8s %-8s %-8s %-8s' % ('', 'SÖZ', 'BİLME', 'diğer'))
for g in ('iman', 'inkar'):
    print('%-8s %-8d %-8d %-8d' % (g, say[g]['soz'], say[g]['bilme'], say[g]['diger']))

a, b = say['iman']['soz'], say['iman']['bilme']
c, dd = say['inkar']['soz'], say['inkar']['bilme']
print()
print('2x2 (SÖZ / BİLME):  iman %d/%d   inkâr %d/%d' % (a, b, c, dd))
if (a+b) and (c+dd):
    print('iman  SÖZ oranı: %.3f' % (a/(a+b)))
    print('inkâr SÖZ oranı: %.3f' % (c/(c+dd)))

def lb(n, k): return lgamma(n+1) - lgamma(k+1) - lgamma(n-k+1)
def hyp(a, b, c, d):
    n = a+b+c+d
    return exp(lb(a+b, a) + lb(c+d, c) - lb(n, a+c))
def fisher(a, b, c, d):
    p0 = hyp(a, b, c, d); tot = 0.0
    r1, r2, c1 = a+b, c+d, a+c
    for x in range(max(0, c1-r2), min(r1, c1)+1):
        p = hyp(x, r1-x, c1-x, r2-(c1-x))
        if p <= p0*1.0000001: tot += p
    return tot
print('Fisher kesin test (iki yönlü) p = %.6g' % fisher(a, b, c, dd))

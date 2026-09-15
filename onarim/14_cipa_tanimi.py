# -*- coding: utf-8 -*-
"""ONARIM 11 — ÇIPA TANIMI (P0 #6). Okumanın son büyük P0 borcu.

Çıpa HESAPLANAN bir alan değil, okuma sırasında uygulanan bir ÖLÇÜT. Bu betik
ölçütü kademeli olarak yazar ve sûre 27'nin doğa/olgu içeren ayetlerini bu
kademelere yerleştirir (yerleştirme OKUMA KAYITLARINDAN, yeniden yorumdan değil).

KADEMELER (aday 799'un 'ölçünün NEYİ ölçtüğü belirleyici' ilkesinden türetildi):
  L0 ADLANDIRMA          — bir olgu/nesne/canlı anılıyor, başka bir şey söylenmiyor
  L1 ADLANDIRMA + ALAN   — olguya bir alan, yeti ya da nitelik ekleniyor
  L2 NEDENSEL BAĞIMLILIK — iki olgu arasında sebep-sonuç kuruluyor, ya da bir
                           YETİ SINIRI konuyor ("siz bunu yapamazdınız")
  L3 GÖRÜNÜŞ-DURUM AYRIMI— gözlemcinin algısı ile nesnenin durumu AÇIKÇA ayrılıyor,
                           ve bir karşılaştırma veriliyor
  L4 MEKANİZMA/ÖLÇÜ/SINIF— süreç nasıl işliyor, hangi birimle, ya da olgular
                           sınıflara ayrılıyor

ÜÇ ADAY EŞİK: çıpa = L2+ · çıpa = L3+ · çıpa = L4+
Karar, eşiğin SONUCUNA bakılarak verilmiyor (bu döngüsel olurdu); eşik seçildikten
sonra çıpa/yıldız ilişkisi hesaplanacak. Bu betik üç eşiği de ayrı ayrı raporlar.
"""
import json
D = json.load(open('defter.json')); DD = {tuple(r['k']): r for r in D}

# --- sûre 27'nin olgu içeren ayetleri; kademe OKUMA KAYDINDAN
TABLO = [
 (16, 'L1', 'kuş dili öğretilmesi — canlı sınıfı + yeti'),
 (17, 'L1', 'üç sınıflı ordu: cin, ins, kuş — sınıflama var ama olgu değil, anlatı'),
 (18, 'L1', 'karınca vadisi — canlı sınıfı + yaşam alanı + davranış'),
 (20, 'L0', 'hüdhüdün yokluğu — adlandırma'),
 (24, 'L0', 'güneşe secde — gök cismi adlandırılıyor'),
 (25, 'L1', 'gizli olanın çıkarılması + gökler/yer — süreç + alan, mekanizma yok'),
 (39, 'L1', 'ifrît + hız iddiası — birim yok, karşılaştırma yok'),
 (40, 'L1', 'göz açıp kapama süresi — insan-bedeni süresi, ölçü değil'),
 (60, 'L2', 'gökten su → bahçeler; ağacı siz bitiremezdiniz — nedensellik + yeti sınırı'),
 (61, 'L1', 'karar yeri, ırmaklar, sabit dağlar, iki deniz arası engel — dört yapı, ilişki yok'),
 (62, 'L2', 'darda kalana karşılık + kötülüğün giderilmesi — nedensellik, ama olgu değil'),
 (63, 'L1', 'karanlıklarda yol, rüzgârlar müjdeci — adlandırma + işlev'),
 (64, 'L2', 'yaratmayı başlatma ve TEKRARLAMA — döngü iddiası'),
 (82, 'L0', 'yerden çıkan dâbbe — adlandırma'),
 (86, 'L2', 'gece dinlenme İÇİN, gündüz aydınlık — işlevsel nedensellik'),
 (87, 'L0', 'sûra üfürülme — adlandırma'),
 (88, 'L3', 'dağları donuk SANIRSIN, oysa bulut gibi GEÇERLER — görünüş/durum + karşılaştırma'),
]
print('=== SÛRE 27 — ÇIPA KADEME TABLOSU ===')
print('%-7s %-4s %-6s %s' % ('ayet', 'kad', 'yıldız', 'gerekçe'))
for a, k, g in TABLO:
    y = DD[(27, a)].get('yildiz', 0)
    print('27:%-4d %-4s %-6s %s' % (a, k, '★'*y if y else '—', g))

print()
print('=== ÜÇ ADAY EŞİĞİN SONUCU (sûre 27, tablo içi %d ayet) ===' % len(TABLO))
for esik in ('L2', 'L3', 'L4'):
    kad = {'L0':0,'L1':1,'L2':2,'L3':3,'L4':4}
    e = kad[esik]
    cipa = [a for a, k, _ in TABLO if kad[k] >= e]
    yok  = [a for a, k, _ in TABLO if kad[k] < e]
    yc = sum(1 for a in cipa if DD[(27,a)].get('yildiz',0) > 0)
    yy = sum(1 for a in yok if DD[(27,a)].get('yildiz',0) > 0)
    print('  eşik %s+ : çıpalı %2d ayet (yıldızlı %d, %%%.0f) · çıpasız %2d ayet (yıldızlı %d, %%%.0f)'
          % (esik, len(cipa), yc, 100*yc/max(1,len(cipa)), len(yok), yy, 100*yy/max(1,len(yok))))
    print('            çıpalı ayetler: %s' % cipa)

print()
print('=== SÛRENİN TAMAMINDA YILDIZ ORANI (karşılaştırma tabanı) ===')
ty = sum(1 for a in range(1,94) if DD[(27,a)].get('yildiz',0) > 0)
print('  93 ayetin %d\'i yıldızlı (%%%.1f)' % (ty, 100*ty/93))
tablo_y = sum(1 for a,_,_ in TABLO if DD[(27,a)].get('yildiz',0) > 0)
print('  olgu içeren %d ayetin %d\'i yıldızlı (%%%.1f)' % (len(TABLO), tablo_y, 100*tablo_y/len(TABLO)))
json.dump([{'ayet':'27:%d'%a,'kademe':k,'gerekce':g,'yildiz':DD[(27,a)].get('yildiz',0)}
           for a,k,g in TABLO], open('cipa_kademe_27.json','w',encoding='utf-8'),
          ensure_ascii=False, indent=1)

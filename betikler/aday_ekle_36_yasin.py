# -*- coding: utf-8 -*-
"""aday_ekle_36_yasin.py — sûre 36 (Yâsîn) adayları (AU_yasin) ve okuma bağları (AP_yasin).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1019'dan); betik sıranın kopmadığını doğrular.
"""
import json

YASIN = [
# ---------------- blok 11-20 ----------------
{"no":1019,
 "aday":"ESMÂ TANIM DIŞI — RAHMÂN BAĞIMSIZ AD: 36:11 (haşiye'r-rahmân, nesne) ve 36:15 (enzele'r-rahmân, özne). e_el 'ilahi' tanımı (kâne/inne haberi, kefâ temyizi, Allah'ın ya da O'na dönen zamirin sıfatı) bu kullanımı kapsamıyor; okuyucu gönderge ölçütüyle 'ilahi' verdi (999 emsali).",
 "olculen":{"36:11":"nesne","36:15":"özne (inkârcıların sözünde)","e_el":"ilahi ×2","emsal":"999 (34:6, 35:14, 36:5 — tamlama içinde ad)"},
 "durum":"ACIK","oncelik":"P1","kaynak":"sûre 36 okuması, blok 11-20","etiket":"999 ailesi — e_suzgec tanımı; ön-kayıt DONDURULMUŞ, tanım değiştirilmedi",
 "test_notu":"Süzgeç kodlanırken (tam okuma sonrası) 'esmâ özel ad olarak' sınıfı açıkça karar verilmeli: lafız gibi mi sayılır, esmâ mı? Geriye dönük e_el turunda Rahmân'ın ad kullanımları (sûre 19, 20, 21, 25…) TAM SAYIMLA bulunmalı."},
{"no":1020,
 "aday":"★★★ KISA AYET RAB ŞİŞMESİ (1012'nin Rab karşılığı) — 36:16: 6 kelimede 1 Rab, rab z=3,23, ★★★ tek kaynak.",
 "olculen":{"36:16":{"n":6,"rab":1,"rab_z":3.23,"yildiz2":3}},
 "durum":"ACIK","oncelik":"P1","kaynak":"sûre 36 okuması, blok 11-20","etiket":"983/1012 — ★★★ otomatik kaynak; uzunluk karıştırıcısı",
 "test_notu":"Onarılmadı. Tur sonunda allah- ve rab-kaynaklı ★★★'ların n dağılımı birlikte TAM SAYIMLA (1012 ile tek test)."},
]

BAGLAR = {"AP_yasin": [
 # blok 1-10
 {"bag":"36:7 → 36:70","kural":"nakarat3 ('haqqa'l-qavlu alâ', sûre içi; kalıp korpusta yalnız bu iki ayet)","not":"Söz çoğu üzerine hak oldu / kâfirler üzerine hak olsun."},
 {"bag":"2:6 ↔ 36:10","kural":"lemma dizisi (9 segment aynı) + xref","not":"Uyarsan da uyarmasan da birdir, iman etmezler."},
 {"bag":"17:107 · 17:109 ↔ 36:8","kural":"lemma (ezkân, TAM SAYIM 3 ayet)","not":"Çeneleri üzerine secdeye kapanırlar / çenelere kadar halka, başlar yukarı."},
 {"bag":"36:8 ↔ 36:9","kural":"okuma gözlemi (جعل 1-2/5; dikey ve yatay eksen)","not":"Boyun → çene → baş / ön ↔ arka set + örtü."},
 {"bag":"34:6 · 35:14 ↔ 36:5","kural":"esmâ sınır vakası (aday 999)","not":"Tamlama içinde ad olarak esmâ — üçüncü vaka."},
 {"bag":"36:6 → 36:10","kural":"kök (نذر 1-4/6)","not":"Uyarman için, ataları uyarılmadı / uyarsan da uyarmasan da."},
 {"bag":"36:7 ↔ 36:10","kural":"okuma gözlemi (fâsıla 'lâ yu'minûn')","not":"Blok aynı sonuçla iki kez kapanıyor."},
 # blok 11-20
 {"bag":"35:18 ↔ 36:11 ↔ 50:33","kural":"kalıp (haşye + gayb) + xref","not":"Gaybda Rablerinden korkanlar / gaybda Rahmân'dan korkan."},
 {"bag":"35:7 ↔ 36:11","kural":"okuma gözlemi (mağfiret + ecr)","not":"Büyük ödül (kebîr) / değerli ödül (kerîm)."},
 {"bag":"36:9 ↔ 36:12","kural":"okuma gözlemi (ön/arka)","not":"Önde ve arkada set / önden gönderdikleri ve bıraktıkları izler."},
 {"bag":"78:29 ↔ 36:12","kural":"xref","not":"Her şeyi saydık."},
 {"bag":"36:5 → 36:14","kural":"kök (عزز 1-2/3)","not":"Azîz (esmâ) / üçüncüyle destekledik."},
 {"bag":"36:14 ↔ 36:16","kural":"nakarat3 ('innâ ileykum murselûn', sûre içi) — DOĞRULANDI","not":"İddia / lâm-ı tekitli iddia."},
 {"bag":"36:15 → 36:47","kural":"nakarat3 ('in entum illâ', sûre içi)","not":"36:47 henüz okunmadı."},
 {"bag":"36:11 ↔ 36:15","kural":"kök (بشر 1-2/2) + esmâ Rahmân ×2 (aday 1019)","not":"Müjdele / beşer; Rahmân'dan korkan / Rahmân indirmedi."},
 {"bag":"36:18 ↔ 36:19","kural":"kök (طير 1-2/2)","not":"Sizin yüzünüzden uğursuzluk / uğursuzluğunuz sizinle."},
 {"bag":"36:13 ↔ 36:20","kural":"okuma gözlemi (karye / medîne)","not":"Aynı yer iki adla."},
 {"bag":"36:11 → 36:20","kural":"kök (تبع 1-2/3)","not":"Zikre uyan / elçilere uyun."},
 {"bag":"35:15 · 35:17 ↔ 36:16","kural":"yıldız kaynağı (kısa ayet; aday 1012/1020)","not":"Lafız ★★★ / Rab ★★★."},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AU_yasin', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in YASIN]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AU_yasin'] = YASIN
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AU_yasin', len(YASIN), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AP_yasin', len(BAGLAR['AP_yasin']))

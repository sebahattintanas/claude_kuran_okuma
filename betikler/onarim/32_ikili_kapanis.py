# -*- coding: utf-8 -*-
"""32_ikili_kapanis.py — aday 947: alt sınır kararı kapandı."""
import json

ADAY = {
 "no": 947,
 "aday": "★ `nakarat` ALT SINIRI KARARI VERİLDİ VE UYGULANDI — ÜÇ SÜRÜM ÖLÇÜLDÜ, ORTASI SEÇİLDİ. Aday 907/935'in üç oturumdur açık duran borcu, aday 943'ün ölçümü üzerine kapandı. Alt sınırı ikiye indirmek korpusun **%67,8'ini** dolduruyor ve alanın yorum değerini bitiriyor; ama iki kelimelik kalıpların **bileşimi ölçülünce** kullanılabilir bir orta yol çıktı.",
 "olculen": {
   "bilesim_alt_sinir_2": {"toplam_kalip": 3762,
                           "ikisi_de_kok": {"n": 1088, "yuzde": 28.9},
                           "biri_kok_biri_islev": {"n": 2264, "yuzde": 60.2},
                           "ikisi_de_islev": {"n": 410, "yuzde": 10.9}},
   "uc_surum": {"nakarat3_3kelime_lemma": {"ayet": 2260, "yuzde": 36.2, "karar": "YORUMDA KULLANILIR"},
                "ikili_2kelime_ikisi_de_koklu": {"ayet": 2635, "yuzde": 42.3, "kalip": 2030,
                                                 "karar": "SAYILIR, yoruma sokulmaz"},
                "2kelime_kisitsiz": {"ayet": 4230, "yuzde": 67.8, "karar": "REDDEDİLDİ"}},
   "sinama_kumesi": "4/6",
   "yakalananlar": {"28:5 ↔ 28:41": "جعل|جَعَلَ أمم|إِمام (aday 906'nın vakası)",
                    "29:53 ↔ 29:54": "عجل|اسْتَعْجَلَ عذب|عَذاب",
                    "29:5 ↔ 29:60": "سمع|سَمِيع علم|عَلِيم",
                    "29:26 ↔ 29:42": "عزز|عَزِيز حكم|حَكِيم"},
   "kacanlar": {"29:2 ↔ 29:4": "ortak kök taşıyan TEK lemma (حسب) — iki kelimelik kalıp değil",
                "28:30 ↔ 28:46": "ortak çift var ama İKİ AYETTE DE bitişik değil"}},
 "durum": "KAPALI", "oncelik": "P1", "kaynak": "onarım 20",
 "etiket": "karar + onarım (aday 907/935/943 kapandı)",
 "test_notu": "**Kararı mümkün kılan şey eşik değil BİLEŞİM ölçümüydü.** 'Alt sınır 2 mi 3 mü' sorusu üç oturumdur cevapsızdı çünkü iki seçenek de kötüydü: 3 gerçek tekrarları kaçırıyor, 2 korpusun üçte ikisini dolduruyor. **Kalıpların içinden bakınca üçüncü bir seçenek çıktı: iki kelimenin de KÖK taşıması şartı.** Bu, %10,9'luk saf gürültüyü (`الذين هم`, `حتا اذا`) ve %60,2'lik yarı-işlevsel kalıpları eliyor; geriye kalan 2030 kalıp %42,3 ayette doluyor — nakarat3'ün %36,2'sinden yalnız altı puan yukarıda. **Ve kaçırdığı iki vaka tanım gereği iki kelimelik kalıp DEĞİL** (biri tek lemma, öbüründe çift bitişik değil), yani sınama kümesindeki 4/6 aslında 4/4. **`ikili` alanı iddia üretmez; okuma sırasında 'alt sınırın altında kaldı' diye elle kaydedilen tekrarları ölçülebilir kılar.**"}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD['AM_lemma'].append(ADAY)
AD['son_guncelleme'] = 'P0 #5 lemma katmanı + alt sınır kararı — adaylar 940-947'
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('aday_bulgular: AM_lemma →', len(AD['AM_lemma']), '|', AD['AM_lemma'][-1]['no'])

for kume in ('AJ_kasas', 'AK_ankebut'):
    for a in AD.get(kume, []):
        if a['no'] in (907, 935, 943):
            a['durum'] = 'KAPALI'
            a['kapanis'] = 'aday 947 — alt sınır 3\'te kaldı, iki kelimelik köklü çiftler `ikili` alanında sayılıyor'
            print('aday %d: KAPALI' % a['no'])
for a in AD['AM_lemma']:
    if a['no'] == 943:
        a['durum'] = 'KAPALI'
        a['kapanis'] = 'aday 947'
        print('aday 943: KAPALI')
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

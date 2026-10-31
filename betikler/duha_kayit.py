# -*- coding: utf-8 -*-
"""duha_kayit.py — sûre 93 (Duhâ) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 93

CIPA = {
 # blok 1-11
 1: dict(kademe='L0', olgu=True, cipa=False, not_="'ve'd-duhâ' — yemin edilen vakit; süreç yok — L0 (91:1 kaydı emsali); tarayıcı vermedi"),
 2: dict(kademe='L0', olgu=True, cipa=False, not_="'ve'l-leyli izâ secâ' — yemin edilen vakit + süreç — L0 (92:1 kaydı emsali); tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'mâ vedde'ake rabbuke ve mâ qalâ' — söz / tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'ve le'l-âxiratu xayrun leke mine'l-ûlâ' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'ve le-sevfe yu'tîke rabbuke fe-terdâ' — vaat (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'e-lem yecidke yetîmen fe-âvâ' — anlatı / tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 7: dict(kademe=None, olgu=False, cipa=False, not_="'ve vecedeke dâllen fe-hedâ' — anlatı / tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 8: dict(kademe=None, olgu=False, cipa=False, not_="'ve vecedeke 'âilen fe-ağnâ' — anlatı / tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 9: dict(kademe=None, olgu=False, cipa=False, not_="'fe-emme'l-yetîme fe-lâ teqhar' — buyruk (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 10: dict(kademe=None, olgu=False, cipa=False, not_="'ve emme's-sâ'ile fe-lâ tenhar' — buyruk (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 11: dict(kademe=None, olgu=False, cipa=False, not_="'ve emmâ bi-ni'meti rabbike fe-haddith' — buyruk (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 11): [
  "esmâ: e_oto 2 token (93:4 'âxir', 'evvel' — âhiret ve ilk) — ikisi 'degil' (yamalar/esma_el_93_1_11.txt); KARAR 723 → 725; ölçüm 'ORTA, MÜHÜRSÜZ', esma_kayit mühür EVET (ÇİFT), bilanço geçerli 0 (1022); lafız yok, Rab 3 (93:3, 5, 11)",
  "kök tablosu: kok_ekle_93 1 kök (سجو 93:2; korpusta tek ayet); 1528 → 1529; retroaktif yama hedefli 0, genel 0 (iki koşu); taban kayıtları om_base ile aynı",
  "yıldız: ★★★ 93:2 hapaks z=3,28 (yeni kök); ★★★ 93:3 rab z=3,94, 93:5 ve 93:11 rab z=5,01 — formül davranışı; 93:5 ★★★ kaynağı rab, kırık bayrağı da açık (1001)",
  "fâsıla (924): 93:5 ölçüm KAFİYE KIRILMASI — son harfte medde işareti harf sayıldı; metinde ى — yanlış pozitif; gerçek geçişler 93:9 (ى → ر) ve 93:11 (ر → ث) işaretlenmedi",
  "biçim (924): 93:1 QASEM, tek kelimelik ayet, şahıs işareti yok, harf 25 → harf3 6 (besmele ailesi); 93:2 atıflı yeminde QASEM yok",
  "iltifât (924): ölçüm 0 — 93:3'te 2MS hitabın girişi {3} → {2, 3} kısmi örtüşme, görünmüyor",
  "lemma etiketi (924): aynı fiil 'ağnâ' morph'ta iki lemma etiketinde ('ağnâ' 15 ayet: 69:28, 93:8 / 'ağnet' 28 ayet: 92:11) — 92:11 kaydı bu yüzden yanlış yazılmıştı, DUZELTME 92:11 (leyl_kayit) ile işlendi; AS_leyl bağı 69:28 → 92:11 'lemma ağnâ' ifadesi değişmedi (eşlik 'mâl' ve kök üzerinden doğru)",
  "kök gloss (1021): نهر 'ırmak' — 93:10 'tenhar' (azarlama) anlamına uymuyor; ◈K satırı tetikten dolu, 'gündüz / ırmak anlamı değil' notuyla",
  "adsız gönderge (1017): yemin eden; hitap 2MS (93:3-11); 93:6-8 bulan 3MS (en yakın 3MS Rab, okuma); 93:5 verilecek şey yazılmamış",
  "KAPATILAMAZ: 93:3 'qalâ' ve 93:6-8 'âvâ', 'hedâ', 'ağnâ' nesneleri yazılmamış (2MS anlaşılıyor, metin yazmıyor); 93:5 'yu'tîke'nin ikinci nesnesi",
  "çıpa: L0 2 (93:1 kuşluk, 93:2 gece — yemin edilen vakit; 91:1, 92:1 kayıtları emsali); olgu=False 9; tarayıcı v4 blokta aday vermedi",
  "aday 1040 (kayıt): 92:21 / 93:1 sûre sınırı — öznesi yazılmamış 'hoşnut olacak' ile kapanış / kuşluğa yemin ile açılış; fâsıla ى → ى; 92 lafızsız Rab 1, 93 lafızsız Rab 3; ardışık sûre okuma bağları 92:21 / 93:5 harekesiz 've le-sevfe' + 'radiye' (korpusun iki geçişi), 92:13 / 93:4 'âxira' / 'ûlâ', 92:1 / 93:2 've'l-leyli izâ' (korpusun beş geçişinden üçü 91-93'te), 92:5 / 93:5 'a'tâ', 92:12 / 93:7 kök هدي, 92:8, 11 / 93:8 kök غني",
  "aday 1039: ayet içi 3 (93:4 âhiret / ilk; 93:7 yolunu yitirmiş / yol gösterdi; 93:8 yoksul / zenginleştirdi) + ayetler arası 1 (93:1 / 2 kuşluk / gece)",
  "aday 1041: sûre içi kayıt yok — lafız yok, Rab 3; sûreler arası okuma notları: lemma 'a'tâ' 92:5 insan / 93:5 Rab; kök غني 92:8, 11 insan ve malı / 93:8 Rab (3MS); kök قلي 26:168 konuşan insan / 93:3 Rab (olumsuz); kök قهر 12:39 lafzın sıfatı / 93:9 2MS'ye yasak",
  "bağ: kalıp / lemma eşleri okumayla (92:21, 91:1, 81:17, 89:4, 91:4, 92:1, 26:168, 17:21, 92:13, 92:5, 53:34, 89:17, 90:15, 70:13, 92:12, 9:28, 69:28, 92:8, 92:11, 12:39, 17:23, 70:25, 92:2, 68:2, 92:19); bütün emsaller bu oturumda AR + meal ile basıldı",
  "◈K / ◈B: ◈K dolu 93:2 ليل, 93:10 نهر (azarlama — tetik başka anlamda); ◈B tetik yok (نعم 'ni'meh' S1 dışı); tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 11 ayet; oturum_xy 28 sayım, 0 uyuşmaz",
  "süreç: sûre 93 dosyaları leyl_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_93.py, oturum dışı; sûre 92 iskele dersi uygulandı); ayetler 1-6 kelime, tek blok; taban 86953a8 (sûre 92 zip'i yüklenmedi) — sûre 93 zip'i 92'yi de taşıyacak",
 ],
}

DUZELTME = {
}

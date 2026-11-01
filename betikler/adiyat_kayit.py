# -*- coding: utf-8 -*-
"""adiyat_kayit.py — sûre 100 (Adiyat) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 100

CIPA = {
 # blok 1-11
 1: dict(kademe=None, olgu=False, cipa=False, not_="'ve'l-'âdiyâti dabhâ' — yemin edilenler adsız, gönderge KAPATILAMAZ; merdiven uygulanmadı (79:1 kaydı emsali); tarayıcı vermedi"),
 2: dict(kademe=None, olgu=False, cipa=False, not_="'fe'l-mûriyâti qadhâ' — yemin edilenler adsız, gönderge KAPATILAMAZ; merdiven uygulanmadı (79:3 kaydı emsali); tarayıcı vermedi"),
 3: dict(kademe='L0', olgu=True, cipa=False, not_="'fe'l-muğîrâti subhâ' — 'subhan' zaman zarfı olarak sabah; süreç / ölçü yok — L0 (76:25 kaydı emsali); yemin edilenler adsız; tarayıcı vermedi"),
 4: dict(kademe='L1', olgu=True, cipa=False, not_="'fe-eserne bihî naq'â' — toz adlı madde + kaldırma, süreç adı; mekanizma / ölçü yok — L1 (99:2 kaydı emsali); özne adsız; tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'fe-vesatne bihî cem'â' — topluluğa dalma (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'inne'l-insâne li-rabbihî le-kenûd' — tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 7: dict(kademe=None, olgu=False, cipa=False, not_="'ve innehû 'alâ zâlike le-şehîd' — tanıklık (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 8: dict(kademe=None, olgu=False, cipa=False, not_="'ve innehû li-hubbi'l-xayri le-şedîd' — tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 9: dict(kademe=None, olgu=False, cipa=False, not_="'izâ bu'thira mâ fi'l-qubûr' — âhiret, insan yapımı yer (olgu=False; 82:4 kaydı emsali); merdiven uygulanmadı; tarayıcı vermedi"),
 10: dict(kademe=None, olgu=False, cipa=False, not_="'ve hussile mâ fi's-sudûr' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 11: dict(kademe=None, olgu=False, cipa=False, not_="'inne rabbehum bihim yevme'izin le-xabîr' — âhiret, bilgi (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 11): [
  "esmâ: e_oto 2 token — 100:7 'şehîd' 'degil' (SINIR VAKASI: 'innehû' göndergesi insan / Rab, metinde işaretsiz; karar sözdizimsel paralelliğe göre), 100:11 'xabîr' 'ilahi' (KARAR 726 → 728); e_el=? kalmadı; ölçüm mührü 2 (100:7, 100:11), geçerli 1 (100:11 — ölçüm satırı 'MÜHÜRSÜZ', 1022); lafız yok, Rab 2 (100:6, 100:11)",
  "kök tablosu: 5 yeni kök (1532 → 1537) — ضبح (100:1), قدح (100:2), نقع (100:4), كند (100:6), حصل (100:10), beşi de korpusta 1 ayet; retroaktif yama hedefli 0, genel 0 (iki geçiş); taban kayıtları om_base ile aynı (iskelet çakışması yok)",
  "gloss (1021): kök عدو 'düşmanlık' (100:1 ''âdiyât' koşanlar), kök وري 'arka; gizleme' (100:2 'mûriyât' kıvılcım çıkaranlar), morph kök etiketi غير 'başka' (100:3 'muğîrât' baskın yapanlar) — üçü de buradaki anlamı vermiyor; kök صدر 'göğüs' burada uyuyor (99:6'da uymuyordu)",
  "yıldız: ★★★ 100:1, 100:2, 100:4 hapaks z=3,28; ★★★ 100:6 rab z=5,01 (hapaks da eşikte); ★★ 100:9 pas z=2,52; ★★★ 100:10 pas z=5,38 (hapaks da eşikte); ★★★ 100:11 rab z=3,94 — formül davranışı",
  "fâsıla (924): metin ا 5 (100:1-5, nekre ACC tenvini), د 3 (100:6-8), ر 3 (100:9-11); ölçüm A 5, د 3, R 3 — ا → د ve د → ر geçişleri kafiye kırığı işaretlenmedi",
  "biçim (924): ayet 1 harf 31 → harf3 11 (besmele ailesi); QASEM yalnız 100:1 — atıflı yeminlerde (100:2-3) yok (sûre 79 dikkati); 100:6-8, 100:11 'inne' + 'le' ölçümde EMPH; 100:9-10 şart ve 100:11 cevabı biçim alanında görünmüyor",
  "şahıs (924): 100:4-5 3FP yemin edilenler; 100:6-9 3MS insan; 100:11 3MP ('rabbehum bihim') — tekilden çoğula geçiş, ölçüm sahset hepsinde '3', iltifât 0",
  "adsız gönderge (1017): yemin edilenler (100:1-5, dişil çoğul ortaçlar ve 3FP fiiller), 'cem'' (100:5), altüst eden ve açığa çıkaran (100:9-10, edilgen) — adlandırılmadı",
  "KAPATILAMAZ: 100:1-3 yemin edilenlerin ne olduğu; 100:4-5 'bihî' göndergesi; 100:7 'innehû' göndergesi (insan / Rab)",
  "çıpa: L0 1 (100:3 'subhan' zaman zarfı — 76:25 kaydı emsali); L1 1 (100:4 toz kaldırma — 99:2 kaydı emsali); gönderge adsız 2 (100:1-2 — 79:1, 79:3 kaydı emsali); olgu=False 9; tarayıcı v4 blokta aday vermedi",
  "aday 1040 (kayıt): 99:8 / 100:1 sûre sınırı — şartla kapanış / yeminle açılış; fâsıla ه → ا; sûre 99 lafızsız Rab 1, sûre 100 lafızsız Rab 2; ardışık sûre okuma bağları 99:2 / 100:9 (yerden / kabirlerden çıkarma), 99:6 / 100:10 kök صدر, 99:4, 99:6 / 100:11 'yevme'izin' ve kök خبر",
  "aday 1039: ayet içi 0; blok içi 0 ('qubûr' / 'sudûr' paralel, metinde karşıt değil)",
  "aday 1041: sûre içi kayıt yok — 'innehû' göndergesi KAPATILAMAZ olduğu için 'şehîd' bölünmesi kayda geçmiyor; sûreler arası okuma notu harekesiz 'le-şedîd' 85:12 Rabbin yakalayışı / 100:8 insan",
  "korpusun iki geçişi, ikisi de basıldı: lemma 'bu'thira' (82:4, 100:9); harekesiz 'mâ fi's-sudûr' (10:57, 100:10); korpusta 1: lemma ''âdiye', 'mûriye', 'muğîre', 'vesata', 'kenûd', 'hussile'",
  "bağ: kalıp / lemma eşleri okumayla (99:8, 77:1, 79:1, 79:3, 81:18, 76:25, 30:48, 70:19, 96:6, 89:20, 33:11, 85:12, 82:4, 99:2, 10:57, 99:6, 17:30, 99:4); 99:2, 99:4, 99:6, 99:8 ve 33:11 bu oturumda daha önce basılmıştı, yeniden basılmadı; diğerleri AR + meal ile basıldı",
  "◈K / ◈B: ◈K dolu yalnız 100:11 (يوم); ◈B dolu yalnız 100:6 (أنس); tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 11 ayet; oturum_xy 26 sayım, 0 uyuşmaz",
  "süreç: oturum gece arası verdi (2026-10-31 → 2026-11-01); ortam korunmuştu — okuma_metni['99'] anahtarları ve ilerleme 4938 ile doğrulandı, origin 4a5437a değişmedi; sûre 100 dosyaları zilzal_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_100.py, oturum dışı; ad 'adiyat'; set değişkeni ASCII 'ADIYAT'; numara üç haneye geçti); sûre 11 ayet — tek blok, ara zip yok",
 ],
}

DUZELTME = {}

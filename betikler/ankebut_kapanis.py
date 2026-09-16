# -*- coding: utf-8 -*-
"""ankebut_kapanis.py — sûre 29 (Ankebût) kapanış notları, çıpa tablosu ve ilerleme."""
import json
import gloss_gecis

ATLAMA = {
 "_cipa_tablosu_29": (
  "SÛRE 29 ÇIPA KAYITLARI — **beş çıpa ve ikisi okumanın İLK L4'leri.** "
  "**L4 (ölçü) 29:14** — أَلْفَ سَنَةٍ إِلَّا خَمْسِينَ عَامًا: birimli nicelik, iki ayrı birim adıyla "
  "(سَنَة, عام) ve bir çıkarma işlemiyle; sûre 27'de 27:39 ve 27:40 **birim olmadığı için** L1'de kalmıştı, "
  "bu ayet tam o eksiği kapatıyor. **L4 (sınıflama) 29:40** — dört helâk türü ayrı adlandırılıyor ve her "
  "biri ayrı gruba eşleniyor (حاصِب · صَيْحَة · خَسْف · إغراق); 27:17'de üç sınıflı ordu L1 kalmıştı çünkü "
  "sınıflanan şey olgu değildi, burada **fiziksel olaylar** ve her birinin mekanizma adı var. "
  "**L2 29:19** (بدأ+عود döngü iddiası, emsal 27:64) · **L2 29:20** (aynı iddia gözleme çağrısına "
  "dönüşüyor) · **L2 29:63** (gökten su → yerin dirilmesi, emsal 27:60). "
  "**ÇIPA OLMAYAN ama kademe taşıyan üç ayet:** 29:53 (L2, olgu=HAYIR — azabın zamanlaması) · 29:64 (L1, "
  "olgu=HAYIR — L3'e en çok yaklaşan ve düşen ayet: algı fiili yok) · 29:65 (L2, olgu=HAYIR — davranış "
  "düzenliliği). **P0 #6'nın ikinci bayrağı (olgu evet/hayır) sûre 29'da ilk kez fiilen iş gördü.** "
  "🜁 beş kez yazıldı; hiçbiri ★★★ değil — **çıpa ile yıldız dört sûrede de bağımsız.** "
  "**Ölçütün ayırt ediciliğinin en temiz gösterimi 29:61/29:63 çifti:** ikisi de aynı لَئِن سَأَلْتَهُم "
  "kalıbıyla açılıyor, **29:61 daha ÇOK olgu kökü taşıyor (altı) ve L1'de kalıyor, 29:63 daha AZ taşıyor "
  "(dört) ve L2'ye çıkıyor** — fark kök sayısında değil, fiiller arasında بِهِ ile kurulan nedensel bağda."),

 "_tarayici_ilk_bagimsiz_sinama": (
  "**P0 #6'NIN İLK BAĞIMSIZ SINAMASI — TARAYICI ÜÇ ÇIPAYI KAÇIRDI.** Çıpa tarayıcısı sûre 29'da kurulum "
  "kümesi dışında ilk kez sınandı ve 29:14 (L4), 29:19 (L2), 29:20 (L2) üçünü de kaçırdı. **Aday 921'in "
  "'anma 7/7 (%100)' kaydı bu yüzden yeniden okunmalı: o ölçüm tarayıcının YAKALAMAK İÇİN YAZILDIĞI küme "
  "üzerindeydi, yani DÖNGÜSELDİ.** İlk gerçek tutulan-küme sınamasında anma **0/3** çıktı. "
  "İki yeni işaret ailesi eklendi: **F_ölçü** (iki ya da daha fazla sayı işareti, korpus 110) ve "
  "**G_bakış** (رأي/نظر kökü + olgu kökü + soru ya da EMİR kipi, عقب kökü HARİÇ, korpus 100). G_bakış'ı "
  "emir kipine açmak ilk denemede فَٱنظُرْ كَيْفَ كَانَ عَٰقِبَةُ kalıbını topladı (27:14, 27:51, 27:69, "
  "28:40) — **o tarihe bakış çağrısıdır, olguya değil** — ve ayırt edici işaret olarak عقب kökü dışlandı; "
  "havuz 772'den 680'e indi. **Yeni durum: havuz 680 ayet (korpusun %10,9'u) · kurulum kümesinde anma 7/7 · "
  "TUTULAN kümede anma 3/3 · kesinlik sûre 27 %57, sûre 28 %23, sûre 29 %30.**"),

 "_yildiz_kaynagi_29": (
  "SÛRE 29 YILDIZ KAYNAK TABLOSU (22 yıldızlı ayet): **allah 9 · pas 6 · kafiye kırılması 2 · n 2 · rab 2 · "
  "hapaks 1 · İÇERİK 0.** **Beş sûre boyunca kesintisiz: içerik 0.** ★★★ dört ayet ve ikisi aday 903'ün "
  "otomatik tetikleyicilerinden: **29:48** (tek hapaks, z=3,38) · **29:57** (tek fiil edilgen, z=5,38); "
  "öbür ikisi ölçüt uç değerlerinden: **29:30** (rab z=3,23) · **29:59** (rab z=3,94). "
  "**PAYDA ETKİSİ `rab` ölçütünde üç değerle gösterildi:** 29:26 (1 token / 12 kelime → 1,45, YILDIZSIZ) · "
  "29:30 (1 / 6 → 3,23, ★★★) · 29:59 (1 / **5** → **3,94**, ★★★) — aynı token sayısı, üç payda, z iki buçuk "
  "kata yakın değişiyor; korpus tavanı 10,34 (74:3, 74:7, 55:17). **`allah` ölçütünde aynı mekanizma:** "
  "29:5 (2 lafız / 12 kelime → 2,80) ve 29:11 (**1 lafız / 6 kelime → 2,80**) — farklı uzunluk, farklı "
  "token sayısı, **aynı oran → aynı z → aynı yıldız.** Ve 29:6 ile 29:44 ikisi de **z=1,47**, eşiğin 0,03 "
  "altında, ikisi de yıldızsız. **`pas` ölçütünün determinizmi dört bağımsız vakayla doğrulandı:** 28:60 · "
  "28:88 · 29:18 · 29:49 — dördünde de bir edilgen / iki fiil → z=2,52 → ★★."),

 "_alan_arizalari_29": (
  "SÛRE 29'DA BULUNAN İKİ ALAN ARIZASI, İKİSİ DE TAM SAYIMLA. "
  "**(1) `hapaks` AYET DEĞİL TOKEN SAYIYOR.** Korpusta tek ayette geçen kök **420**; bunların **399'u** o "
  "ayette tek tokenli ve hapaks sayılıyor, **21'i birden çok tokenli ve SAYILMIYOR**: سلح (4 token) · فسح, "
  "نفذ, زبد (3'er) · on yedisi ikişer (**عنكب** · زجج · رجج · بسس · وطر · بتل · هور · بسل · كدح · لهث · صنو "
  "· زود · أزز · رفد · برم · نشط). Kaçan 21 ayetin yıldız dağılımı ★★★ 11 · ★★ 2 · ★ 3 · **yıldızsız 5**. "
  "**29:41 o beşten biri: sûrenin adını taşıyan kök (عنكب) korpusta tek ayette ve ayet YILDIZSIZ**; yedi "
  "ayet sonra 29:48'in خطط kökü tek token olduğu için sayılıyor ve ayet ★★★. **Aynı sûre, aynı nadirlik "
  "derecesi, iki farklı sonuç — fark yalnızca tokenin ayet içinde kaç kez geçtiği.** Onarım: ölçüt 'korpusta "
  "tek AYETTE geçen kök' olmalı; hapaks kök 399 → 420, hapaks ayeti 358 → 379, beş yeni ★★★. "
  "**(2) `fig` KELLA'YI كُلّ İLE KARIŞTIRIYOR.** `fig`=KELLA olan **48** ayetin **15'inde (%31)** "
  "morfolojide LEM:كَلّا yok; **14'ünde كلل kökü var.** Yanlış negatif **SIFIR** — alan gerçek كَلّaların "
  "hepsini yakalıyor. 29:40 bunlardan biri (فَكُلًّا = 'her biri', ROOT:كلل|LEM:كُلّ). Yanlış pozitifler: "
  "4:95 · 4:130 · 6:84 · 6:86 · 7:46 · 11:111 · 11:120 · 17:20 · 17:23 · 19:49 · 21:72 · 21:79 · 29:40 ve "
  "ikisi daha. **Onarım: ölçüt LEM:كَلّا olmalı, yüzey biçimi değil.** Sûre 27 ve 28'de KELLA hiç "
  "görülmemişti; **alan üç sûrelik okumada ilk kez tetiklendi ve ilk tetiklenişinde yanlış çıktı.**"),

 "_esit2_29": (
  "**`esit2`'NİN 'YAKIN' KADEMESİ İLK KEZ TETİKLENDİ: 29:28 ↔ 7:80, oran 0,9615.** Sûre 27 ve 28 boyunca "
  "üst kademe (0,95-1,0) bir kez bile çalışmamıştı. **TAM SAYIM — korpus kademe dağılımı: tam 1622 · benzer "
  "280 · yakin 84** (74 ayet). Üst bant gerçekten ince — 'benzer'in üçte biri. **Sûre 28'in 'gerçek bağlar "
  "0,82-0,95 bandında yoğunlaşıyor' kaydı ÇÜRÜMÜYOR, niceliğe bağlanıyor.** Fark bir kip: 7:80'de soru "
  "cümlesi (أَتَأْتُونَ), 29:28'de te'kidli haber (إِنَّكُمْ لَتَأْتُونَ). "
  "**İKİNCİ BULGU — ONARIM YANLIŞ NEGATİF ÜRETMEMİŞ.** TAM SAYIM: eski `esit` **253** ayette dolu, `esit2` "
  "**520**'de, **kesişim tam 253** — eski dolu ama esit2 boş olan **SIFIR**; esit2 dolu ama eski boş olan "
  "**267**. **Onarım eski alanın gördüğü her şeyi koruyor ve üstüne 267 ayet ekliyor.** `mm2`'nin "
  "(175 → 3 → 125, aday 867) tersi bir tablo: **kaybetmeden genişlemiş bir onarım.** "
  "**ÜÇÜNCÜ BULGU:** iki ayet `esit2`de iki ayrı hedefe **aynı oranla** bağlanıyor — 29:37 → 7:78 ve 7:91 "
  "(ikisi de 0,8986) · 29:66 → 16:55 ve 30:34 (ikisi de 0,9275). **Aynı formülün korpusta üç kez "
  "tekrarlandığını gösteriyor ve esit2 üçlüyü İKİLİ bağlarla veriyor; üçlüyü tek küme olarak gören alan "
  "yok.**"),

 "_esma_29": (
  "SÛRE 29 ESMÂ ÇAPRAZ TABLOSU (25 token, gönderge ELLE doğrulandı). **Mühürlü 8 → 8 GEÇERLİ** (dört çift: "
  "سَمِيع|عَلِيم 29:5 ve 29:60 · عَزِيز|حَكِيم 29:26 ve 29:42). **Mühürsüz 17 → 3 GEÇERLİ, 14 ARTEFAKT** "
  "(geçerliler: 29:6 غَنِيّ · 29:52 شَهِيد · 29:62 عَلِيم). **ÜÇ SÛREDE MÜHÜRLÜ YANLIŞ POZİTİF SIFIR** "
  "(27: 12/12 · 28: 2/2 · 29: 8/8). "
  "**ADAY 908'İN VAKASI İKİNCİ KEZ TEKRARLANDI:** شَهِيد tokeni sûre 28'de ORTA konumda **ARTEFAKT** "
  "(28:75, her ümmetten çıkarılan tanık), sûre 29'da ORTA konumda **GEÇERLİ** (29:52, göndergesi اللَّه). "
  "**Aynı kelime, aynı konum, iki sûre, zıt hüküm** — birincisi وارِث idi (28:5 artefakt / 28:58 geçerli). "
  "**Ayrım token düzeyinde YAPILAMIYOR; gönderge çözümlemesi şart.** Ayrıca sûre 29'un üç mühürlü esmâ "
  "kalıbı da (هو السميع العليم ×2, هو العزيز الحكيم ×2) `nakarat2` süzgecinin altında: **2 ayet / 3 "
  "kelime.**"),

 "_sure_29_kapanis": (
  "SÛRE 29 (ANKEBÛT) KAPANIŞ — HAM SAYIMLAR. 69 ayet · ortalama n=14,14 · fâsıla SINIF olarak 65 N + 3 R + "
  "1 mukattaa · kafiye kırılması **2 ve ARDIŞIK** (29:21-22). YILDIZ: ★★★ 4 · ★★ 7 · ★ 11 · yıldızsız 47 "
  "(%68,1). EKSEN: lafız **42 token / 30 ayet** · Rab **5 token / 5 ayet** → **A/R = 8,4**; sûre 27'de "
  "2,25, sûre 28'de 1,42 idi — **sûre 29 lafız ağırlıklı ve fark büyük.** Rab yalnız beş ayette ve **ikisi "
  "★★★ verdi.** İLTİFÂT **1** (29:23, yön 2>13) — sûre 28'de sıfırdı, sûre 27'de üçtü; TAM SAYIM: korpusta "
  "iltifât taşıyan 328 ayet. HAPAKS: **1 ayet** (29:48, خطط). EDİLGEN: 15 ayet. AKTÖR: adlı **21 token / 16 "
  "ad** (Lût 4, İbrâhîm 2, Cehennem 2, ötekiler birer) — sûre 28'in 37 tokenine karşı **çok daha dağınık**; "
  "**29:39 tek başına dört aktör taşıyor** ve dördü de sûre 28'in kadrosu (Kārûn, Firavun, Hâmân, Mûsâ), "
  "TAM SAYIM: korpusta 4+ adlı aktörlü 32 ayet. adsız **5 token**. YENİ KÖK 27 → kok_turkce 1032'den "
  "**1059**'a (üç sûre). `harf` 4498 → `harf3` **4256**, isaret 223 (**%5,0**). `mm2` 1 ayet (29:20). "
  "İÇ DÜĞÜM **4 ayet / 2 çift**: 29:24↔29:29 (beş ayet, yedi kelime) ve 29:32↔29:33 (**bir ayet — okumanın "
  "en dar iç düğümü**). `nakarat2`: **geçen 5 kalıp · geçemeyen 10, hepsi 2 ayet/3 kelime · alt sınırın "
  "altında kalan 5 tekrar hiç ölçülmedi.** 529 KÜMESİ: sûreden **dört yeni vaka** (عوم yıl/yüzme · نبأ "
  "haber/peygamberlik · أتي üç işlev · **عود yaratmayı tekrarlamak/Âd kavmi — biri fiil biri özel ad, en "
  "keskini**) ve bir OLUMLU örnek (برر 'iyilik; kara' ikisini de taşıyor). xref hedef dağılımı (kaynak ayet "
  "sayısına göre): 7 (9 ayet) · 16 (7) · 2 (6) · 11, 6, 4 (5'er) · **29 sûre-içi (4)** · 27 (4)."),
}

ATLAMA = {k: gloss_gecis.gecir(v) for k, v in ATLAMA.items()}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
OM['29'].setdefault('_mercek_atlama_notu', {}).update(ATLAMA)
OM['ilerleme']['tam'] = sorted(set(OM['ilerleme']['tam']) | {29})
OM['ilerleme']['not'] = "Sûre 1, 9-28 ve **29 TAM**. Devam: sûre 30'dan ya da sûre 2'nin 21. ayetinden."
OM['ilerleme']['okunan_ayet'] = 2199
OM['ilerleme']['korpus_yuzde'] = 35.3
OM['ilerleme']['son_oturum'] = 'OTURUM_2026-09-16_KAPANIS.md'
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 29 →', len([k for k in OM['29'] if not k.startswith('_')]),
      'ayet +', len(OM['29']['_mercek_atlama_notu']), 'kapanış notu')
print('ilerleme:', OM['ilerleme']['okunan_ayet'], 'ayet (%', OM['ilerleme']['korpus_yuzde'], ')')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
MK['29_atlama'] = ATLAMA
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: 29_atlama →', len(MK['29_atlama']))

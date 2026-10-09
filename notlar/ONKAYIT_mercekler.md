# ÖN-KAYIT — Dört ek mercek: Kozmolog · Biyolog · Dilbilimci · Anlatıbilimci

Tarih: 2026-10-04 (kullanıcı kararı, sûre 36 ara kaydında). Uygulama başlangıcı: **36:21**.
Bu belge okumada kullanılmadan ÖNCE depoya girer (`notlar/ONKAYIT_mercekler.md`); commit hash §7'ye yazılır. Sonra dokunulmaz; sapma §8'e.

## 1. Amaç ve sınır

Matematikçi merceği (◇) yapıyı ve sayımı okur. Ek mercekler aynı ayete dört başka sabit soru setiyle bakar. Mercekler **gözlem kaydıdır, kanıt değildir**:
- Modern bilimle eşleştirme yazılmaz ("bilimsel mucize", "X'i önceden söylüyor" yok). Olgu adlandırmasının kademesi çıpa merdiveniyle (🜁 L0-L4) verilir; mercek onun yerine geçmez.
- Okurken fark edilen dizilim KAPATILAMAZ etiketi taşır (taraflı örneklem yasağı).
- Henüz okunmamış ayet hakkında iddia yok.
- Sayısal her iddia ölçüm satırından ya da korpus sayımından; sayılmamış "tek, ilk, en, hepsi" yazılmaz.

## 2. Biçim

Her ayette ◇ satırından sonra dört satır, sabit sırayla (K → B → D → A). Satırlar `M[n]` metninin sonuna eklenir; kayıt aracı değişmez:

    ◈K — kozmolog yanıtı ya da "—"
    ◈B — biyolog yanıtı ya da "—"
    ◈D — dilbilimci yanıtı ya da "—"
    ◈A — anlatıbilimci yanıtı ya da "—"

Tetik yoksa satır "—" ile yazılır, atlanmaz. Böylece hangi ayette merceğin boş kaldığı da kayda geçer; seçerek raporlama önlenir.

## 3. ◈K Kozmolog — gök, zaman, ölçek

Tetik: gök/yer/gök cismi/gece-gündüz kökü (سمو أرض شمس قمر نجم كوكب ليل نهر فلك سحب ريح موه بحر جبل) ya da zaman/süre birimi (يوم أجل سنن عمر ساعة دهر أبد حين).
- K1 Hangi kozmik öğeler adlanıyor? (kök listesi ölçüm satırından)
- K2 Zaman: hangi birim/süre, hangi yön (geçmiş, şimdi, ertelenmiş, sonsuz)?
- K3 Ölçek: en küçük ve en büyük birim (zerre … gökler) — ayette ölçek aralığı var mı?
- K4 Hareket/düzen fiili (akar, boyun eğdirildi, döner, tutulur): özne kim, nesne ne?

## 4. ◈B Biyolog — canlı, oluşum, beden

Tetik: canlı türü (أنس دبب نعم طير نبت شجر), oluşum/üreme (خلق نطف علق زوج حمل وضع أنث), organ (عنق ذقن يدي عين سمع بصر جلد قلب), dirim/ölüm (حيي موت عمر).
- B1 Hangi canlılar ya da canlı sınıfları adlanıyor?
- B2 Oluşum ya da üreme aşaması var mı; aşamalar sıralı mı, ara durum adlı mı?
- B3 Beden organı var mı; organ hangi işlevle anılıyor?
- B4 Dirim/ölüm/ömür ilişkisi: hangi yönde (veriliyor, alınıyor, uzatılıyor, ertelemeli)?

## 5. ◈D Dilbilimci — sözdizimi, kip, belâgat

Tetik: her ayet (ölçüm satırında edim/kip/biçim alanı her zaman var). Boş kalırsa "—".
- D1 Cümle iskeleti ve kip: haber/emir/soru/şart/yemin; ölçüm `edim`, `kip` alanıyla birlikte.
- D2 Belâgat figürü: hasr, qasem, idrâb, nidâ, iltifât, tekit, soru-cevap — ölçüm `biçim` alanı esas; alan kaçırıyorsa arıza olarak yazılır (517 ailesi), metin hakkında kanıt sayılmaz.
- D3 Tekrarın işlevi: kök ikilemesi, aynı kökün iki anlamı, aynı kalıbın pekiştirilmesi.
- D4 Şahıs akışı: konuşan ve muhatap ayet içinde değişiyor mu (ölçüm `sah`/`sahset`; alıntı sınırı için aday 1017)?

## 6. ◈A Anlatıbilimci — aktör, sahne, konuşma

Tetik: adlı/adsız aktör, `qâle/qâlû` (قول), sahne/mekân adı, anlatı geçişi.
- A1 Aktörler: kim (adlı/adsız), hangi rolde (ölçüm `adli`, `adsiz2`, `rol`)?
- A2 Sahne: mekân ve zaman (dünya, kıyamet, cennet, cehennem, kasaba…).
- A3 Konuşma sırası: kim konuşuyor, kime cevap veriyor; alıntı içi "biz" kimin?
- A4 Anlatı sınırı: anlatı burada açılıyor, sürüyor ya da kapanıyor mu? Yalnız okunmuş ayetlere göre.

## 7. Kilit

Bu belgenin commit hash'i: **a7e9628** (2026-10-04 21:32 +0300; içerik o commit'teki hâliyle birebir aynı — yalnız bu satır sonradan dolduruldu). Uygulama 36:21'de başlar; 36:1-20 ve önceki sûreler geriye dönük doldurulmaz. Geriye dönük doldurma ayrı ön-kayıt ister.

## 8. Sapmalar

### S1 — Tetik düzeltmesi (2026-10-06, sûre 37 oturumu; kullanıcı kararı)
**Gerekçe:** 2026-10-05 aralık oturumu tetik listelerini korpusla ölçtü (`notlar/ARALIK_OKUMASI.md`, `betikler/aralik_kozmolog.py`, `aralik_biyolog.py`): iki ölü kök, bir yanlış kök, iki çok anlamlılık. Bu kayıt, düzeltmenin sonuçlara bakılmadan, yalnız tetiğin korpusta neyi yakaladığına göre yapıldığını belgeler.
**Değişiklik (yalnız kesinlik/eşleşme düzeltmesi; yeni tetik sınıfı EKLENMEDİ):**
- ◈K `ريح` → kök روح, yalnız lemma رِيح (29 token; روح'un rûh/ravh lemmaları tetiklemez).
- ◈K `ساعة` → kök سوع, yalnız lemma ساعَة (48 token).
- ◈K `سنن` → çıkarıldı (korpusta sünnet/sinn/mesnûn); yerine kök سنو, lemma سِنِين (12) ve سَنَة (7).
- ◈K `سمو` → yalnız lemma سَماء (310 token); ad lemmaları (isim, müsemmâ, semmâ…) tetiklemez.
- ◈B `نعم` → yalnız lemma نَعَم (33 token, davar); nimet lemmaları (nimet, naîm, en'ame, ni'me…) tetiklemez.
**Uygulanmayanlar (ayrı karar ister):** duyarlılık genişletmeleri — ◈K ışık/karanlık/gölge/sıcaklık (نور ظلم ظلل حرر ضوأ), ◈B besin/ürün ve beden eylemi alt sınıfları. Bunlar yeni tetik sınıfıdır, düzeltme değil.
**Uygulama:** 37:31'den itibaren, yalnız ileriye. 36:21–37:30 satırları DEĞİŞMEZ (§7). Sayım (morph.txt): okunmuş mercekli aralıkta düzeltilen köklerden yalnız سمو/gök lemması ×4 (36:28, 36:81, 37:5, 37:6) ve نعم/davar lemması ×1 (36:71) geçiyor — hepsi düzeltilmiş tetikle de aynı sonucu veriyor; ölü köklerin (روح/رِيح, سوع) ve سنو'nun hiçbir tokeni yok. Yani düzeltme önceki satırların hiçbirini değiştirmezdi.
**Not:** `anahtar_denetim.py` .md dosyalarını taramıyor; bu bölümdeki lemma dizgeleri elle yazılmadı, `morph.txt`'ten token sayısıyla seçilerek kopyalandı.

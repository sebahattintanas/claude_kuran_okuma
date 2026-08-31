# YAPILACAKLAR — programcı gözüyle (öncelik sıralı)

## ALTYAPI — OTURUM RUTİNİ (Ağustos 2026'da kuruldu)
- [x] GitHub deposu açıldı: `github.com/sebahattintanas/claude_kuran_okuma` (public) — 55 dosya, kategorik yapı, bütünlük doğrulandı (NFC ✓, morph 130030 satır ✓)
- [x] Proje alanı küçültüldü (19→3.5 MB); morph.txt + kuran_veri.json artık oturum başında kaynağından/depodan indirilir (rutin: OKUMA_SISTEMI_OZET.md sonunda)
- [x] **Kayıp dosyalar yeniden üretildi (Ağu 2026):** `kok_adlar.json` (1651/1651 kök; 430 katalog + 1221 claude-üretimi, kaynak etiketli — betikler/kok_adlar_derle.py ile yeniden üretilebilir), `bulgu_karsi_kutup_mesafe.json` (asimetri: pozitif kutuplar demirli, negatifler nötr; 3 kutup Bonferroni-sağlam), `bulgu_denge_mizan.json` (emir-mîzanı medyan 12 vs sahne-mîzanı 118, tam ayrışma, p=0.0106)
- [ ] kok_adlar.json denetimi: claude-kaynaklı 1221 adın örneklem denetimi + çok-kavramlı köklerde birincil ad seçimi (نور→'ateş' sorunu: frekans-birincil yerine bağlam-birincil?)
- [x] **2026-08-04 oturumu kurtarıldı (5 Ağu):** 18 dosya (14 bulgu + 4 harita + kapanış + ek) o gün /mnt/project bağlanamadığı için zincire girememişti; kullanıcı yüklemesiyle depoya alındı. Ders: oturum dosyaları HEM çıktı HEM depo — tek kanal yetmez.
- [ ] Oturum sonu kuralı: güncellenen her dosya çıktı olarak verilir → kullanıcı depoya yükler (aynı adla yükleme = üstüne yazma + sürüm geçmişi)
- [ ] **/mnt/project BAYAT (2026-08-06 tespiti)**: proje klasöründeki YAPILACAKLAR 16-kök dönemine ait,
      bulgu dosyalarının 8/28'i var, morph/meal/kok_adlar/kuran_okuma.html hiç yok; proje-bilgi araması
      eski sürümleri döndürüp karışıklık yaratıyor. Karar: TEK DOĞRU KAYNAK = GitHub deposu; oturum başı
      `git clone`. Proje klasörü ya deponun güncel aynası yapılmalı ya da yalnız README+işaretçi bırakılmalı.

## ÖN-KAYITLI TAKİP TESTLERİ (2026-08-04 oturumundan, kurtarıldı)
- [x] **İplik tam taraması TAMAMLANDI (2026-08-06)** → bulgu_iplik_haritasi.json (+ham liste):
      113 kök, konum-eşli kapı (Bonf 0.000442) + d≤2 hâl imzası. 9 hakikî-yakın / 4 hakikî-uzak.
      BAĞLANMA: dûn·sebîl·ind·abd; FAİL: şey/dileme·hüküm·ilim; KARIŞIK: fadl·azz; UZAK: ربب·أول·أكل·جنن.
      Sentaks hipotezi 113-evrende ayakta. Not: kavram-sağlam hidâyet/takvâ/mağfiret kök düzeyinde
      eşik-altı (sulanma + test yükü) — katman farkı belgelendi.
- [x] **Gafr sınır vakası ÇÖZÜLDÜ (2026-08-06)** → bulgu_gafr_ayrisimi.json: kök 4 sese ayrıldı;
      yalnız esmâ kapıyı geçti (medyan 1, p=0.0) — v2 gradyandaki mağfiret sınır-sinyalinin kaynağı
      esmâ-kapanış formülüymüş. Fiil-I ve istiğfar öngörüleri DÜŞTÜ (dürüstçe kayıtlı). İki keşif:
      (a) inne-kalıbı: esmâ ACC'sinin 32/35'i innallâhe — NOM-payı "özne" için eksik vekil;
      (b) fiil kip betimlemesi: bildirme med 3 NOM 0.82 vs dua med 41 — Fâtiha isim-sessizliğiyle aynı desen
- [ ] ÖN-KAYIT (yeni): kip-ayrımı testi — çift-sesli köklerde dua/emir vs bildirme
- [x] **Özne-imzası yeniden koşusu TAMAMLANDI (2026-08-06)** → bulgu_iplik_haritasi.json/imza_v2_ozne:
      inne-ailesi FAM-etiketiyle tespit (2349 kelime; Allah-ACC'nin %61'i inne-yönetimli, taban 0.363→0.498).
      Ayrışma keskinleşti: BAĞLANMA ≤0.24 / FAİL ≥0.66, arada boşluk. azz FAİL'e çözüldü ✓,
      gafr-esmâ 0.952 ile korpusun en saf fail imzası ✓; fadl öngörüsü DÜŞTÜ — sahici çift-seslilik.
      Yan bulgu: Allah geçişlerinin %49.8'i semantik özne konumunda
- [ ] Esmâ-mühür düzeni: fiil→kapanış-esmâsı eşleşmesine eşik/anlamlılık (şu an betimsel)
- [ ] Sıfat-zinciri türü: tüm zincirlerde (9:112, 23:1-9, 66:5, 70:22-34, 33:35, 25:63-76) halka-sıra korunumu + hıfz-kapanış testi
- [ ] Fraktal kuyruk sınıflaması: ×16/×32 eşleşme kuyrukları anlatı/hitap, uzunluk-eşli kontrol
- [ ] Tohum aramasının ön-kayıtlısı: imza tanımı sabit, sure/pasaj ölçeğinde
- [ ] Hudûd kutupları coğrafya-kontrollü (Mekkî/Medenî katmanı)
- [ ] Rahmân/rahîm isim-formları رحم kökünden ayrılıp ayrı test
- [ ] Kıssa bölge-tanımlarının nesnelleştirilmesi (anlatı-modu sınıflayıcısıyla otomatik sınır)
- [ ] Koridor genellemesi: en uzun sessiz koşuların çıkış rampaları hangi köklerle döşeli (bulgu_kevser_koridoru'nun ön-kayıtlı taraması)
- [x] خزن ayrımı tabloda: hazine 8 / bekçi 4 / saklama 1, kapsam tam ✓ — TAKİP: p=0.071'lik karışık ölçüm ayrım-sonrası YENİDEN koşulacak (aşağıya P3'e eklendi)

## P0 — VERİ BÜTÜNLÜĞÜ (önce bunlar, gerisi buna bağlı)
- [ ] **ESMÂ TESPİTİ BAĞLAMA TAŞINACAK — okuma turu bittikten SONRA** (tespit 2026-08-12, sûre 8 okuması)
      `esma_listesi.json` yalnız lemma eşleştiriyor, bağlam ayırmıyor. Sûre 8'de `مُؤْمِن` on kez
      "esmâ" sayıldı; onu da "mü'minler". Korpus geneli:
      `مُؤْمِن` 202 (ilâhî ad olarak yalnız 59:23) · `آخِر` 155 (çoğu *âhiret*) · `مُبِين` 119 ·
      `وَلِيّ` 86 (insan velîleri dahil) · `سَلام` 42 · `كَبِير` 40 · `نَصِير` 35 · `كَرِيم` 30.
      Şüpheli lemmaların payı **898/2077 = %43**. Daha önce kayıtlı dört istisnadan (جَبَّار 5:22,
      بَرّ 5:96/6:59/6:97, عَلِيم 7:109/7:112) çok daha geniş bir sorun.
      **Yapılacak:** esmâ tespiti lemma yerine ayet-içi bağlam üzerinden kurulacak — Allah lafzına
      bağlılık (izâfet/haber konumu), `إِنَّ ٱللَّهَ …` kalıbı, ayet-sonu mühür konumu.
      **Sonra yeniden ölçülecek:** `bulgu_allah_ekseni_dikey.json` içindeki "esmâ katmanı eksen-nötr"
      bulgusu bu sayımın üstüne kuruldu; düzeltmeden sonra ayakta kalıp kalmadığı YENİDEN test edilecek.
      **KURAL: okuma turu bitmeden yapılmayacak.** Şu an aday_bulgular.json K_enfal/119'da kayıtlı.
- [ ] **YILDIZ FORMÜLÜ DENETİMİ — okuma turu bitmeden yapılmayacak** (tespit 2026-08-12, 9:36)
      Yıldız (dikkat) puanı hapaks-z ve Allah-z ağırlıklı; sayı-yoğunluğunu ve kozmolojik alan
      terimlerini görmüyor. 9:36 dört sayı sözcüğü + `يَوْمَ خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ` taşıdığı hâlde ★★,
      9:35 ise tek başına çift hapaksla ★★★. Uzay bilimci merceğinin tetiklenmesi yıldıza bağlı
      olduğu için formül merceğin kapsamını da belirliyor — yani ölçüm aracı okuma kapsamını
      daraltıyor. Karar: formüle dokunulmayacak, sapma vakaları `aday_bulgular.json` L_tevbe/129'da
      biriktirilecek; tur sonunda toplu değerlendirme.
- [ ] **YILDIZ FORMÜLÜ — dokuz sapma vakası birikti** (güncelleme 2026-08-12, 13:41)
      Kozmolojik/fiziksel içerikli ayetler yıldız almıyor; uzay bilimci merceği on üç sûrede
      neredeyse hiç açılmadı. Vakalar: 9:36 (★★ ama sayı sayesinde), 10:5, 10:6, 10:67,
      11:7 (★ ama uzunluk sayesinde), 13:2, 13:3, 13:12, 13:41.
      Tanı: formül hapaks-z + Allah-z + uzunluk ağırlıklı; gök cismi adları, ölçü terimleri,
      hareket fiilleri formülde YOK. Öneri: kavram_katalogu kozmoloji/biyoloji kümelerinin
      ayet-içi yoğunluğunu bir bileşen olarak eklemek.
      UYARI: bu düzeltme merceğin TETİKLENMESİNİ değiştirir, İÇERİĞİNİ değil.
      Kayıt: aday 129, 160, 246.

- [ ] **EKSEN ADI TESPİTİ DE BAĞLAM GEREKTİRİYOR — okuma turu bitmeden yapılmayacak** (tespit 2026-08-12, 12:23)
      `رَبّ` yalnız ilâhî eksen adı değil; Yûsuf'ta 'efendi/sahip' anlamında da geçiyor
      (12:23 `إِنَّهُۥ رَبِّىٓ أَحْسَنَ مَثْوَاىَ` = Mısır azizi; ayrıca 12:41, 12:42, 12:50).
      Defter bunları EKSEN GEÇİŞİ sayıyor — sûrenin 19 Rab geçişinin kaçının 'efendi' olduğu
      denetlenmeli. Bu düzeltme yapılınca Yûsuf'un Rab yoğunluğu DÜŞECEK ve
      aday 181/206/211'deki tüm sûre-arası eksen karşılaştırmaları yeniden ölçülmeli.
      Not: 12:39'daki `أَرْبَاب` (çoğul-bağsız, sahte-rab) DOĞRU sayılıyor — sorun tekil-bağlı biçimde.
      Kayıt: `aday_bulgular.json` O_yusuf/220.
- [x] **بشر ayrımı tabloda** — kök denetiminde işlendi; korpus doğrulaması 2026-08-05: müjde 84 / beşer 37 / mübâşeret 2, kapsam tam ✓
- [x] **insân/nâs ayrımı tabloda** — أنس kökü: nâs 241 / insân 71 / ins 19 / ünsiyet 7, kapsam tam ✓ (2026-08-05 doğrulandı)
- [x] **kelime-akışı modülleşti** — kuran_akis.py v2: kelime_akisi(), kavram(), allah_indeksleri(); regresyon testi geçti
- [x] doğrulama betiği var: tablo_dogrula.py — 2026-08-05 koşusu: 430/430 kök ✓, %100 çözülme, sıfır hata

## P1 — DİKEY OKUMA ARACINI GENELLEŞTİR
- [x] **dikey_oku(kavram) genelleşti** — dikey_oku.py: dikey_oku(), anlamlilik(), gradyan_cetveli(); zenginleşme oranı + permütasyon testi gömülü
- [x] **Gradyan cetveli 40 kavrama genişledi (2026-08-05)** — bulgu_gradyan_cetveli.json: Bonferroni-sağlam iç halka hudûd(1)→mağfiret/takvâ/ilim(6)→hidâyet(7)→iman(8); sağlam dış halka zikir(16)→Rab/tekzîb(23)→insân(43); namaz/zekât/rahmet/azap nötr. ÖN-KOŞUL DÜZELTMESİ: مَلَك 'mülk'→'melek' (88), مَلِك→'kral' (tabloya işlendi)
- [ ] Rab için de aynı komşuluk-imzası (Allah'ınki: öncesi yöneliş/sonrası nitelik; Rab'ınki rahmet/dua mı?)

## P2 — BULGULARI PROGRAMA BAĞLA (kuran_okuma.html)
- [x] "Mercek seç" paneli + uyarı metni — gömülü (matematikçi makro + kavram-uzayı)
- [ ] **Fizikçi(×4) karşılaşmaları KAYIP** — karsilasmalar.json'da yalnız _makro.matematikçi* var;
      fizikçi metinleri hiçbir dosyada yok, yeniden üretilmeden panele giremez
- [x] **Allah-ekseni rozeti (2026-08-06)** — betikler/arayuz_yama.py: bulgu_gradyan_cetveli.json'dan
      40 ölçüm gömüldü; 21/97 varlık adı rozetli (eşanlam köprüsü: merhamet→rahmet, sabır→sabr,
      şükür→şükr, tevbe→tövbe, adalet→adl, küfür→küfr); yan panel satırı + tanım-kartı hücresi;
      renk: yakın-Bonferroni yeşil / uzak turuncu / nominal soluk / nötr gri; hover'da p, n, medyan
- [x] **▶Oku audio bağlandı (2026-08-06)** — everyayah CDN (Alafasy_128kbps), ayet değişince durur,
      hata durumunda "⚠ ses yok" geri bildirimi; yama idempotent (ARAYUZ-YAMA v1 marker)
- [ ] Rozet kapsamını genişlet: kalan 19 gradyan kavramı (hudûd, nûr, tekzib, insân, beşer...)
      arayüz varlık kataloğunda ad olarak yok — varlik_katalog'a eklenince kendiliğinden rozetlenir
- [ ] kuran_ses.js (kārîsiz sentez) hâlâ ayrı; ikinci ses kaynağı olarak entegrasyon (düşük öncelik)

## P3 — YENİ ÖLÇÜMLER (bekleyen sorular)
- [x] Anlatı modu NİCEL doğrulandı — bulgu_anlati_boslugu.json: özel isim ×3.4, 'dedi' ×1.6, kavim ×3.1 (p<0.0005, 2000 permütasyon)
- [ ] Allah komşuluk-imzası (öncesi yöneliş, sonrası ilim/mağfiret/rahmet) — bir bulgu dosyasına kaydet (henüz kaydedilmedi!)
- [ ] خزن yeniden ölçümü: ayrım-öncesi p=0.071'lik ölçümü hazine/bekçi ayrık koşullarla tekrarla
- [ ] beşer/müjde ayrımı sonrası "insan" gradyanını yeniden hesapla (temiz)
- [ ] adl/zulüm ve nûr/zulmet çiftlerini dikey oku (aynalar modeline bağla)

## BEKLEYEN (eski, düşük öncelik)
- [ ] Kevser-metrik mushaf (gerçek satır verisi) → dikey/sayfa geometrisi
- [ ] Gerçek tilavet kaydı → akustik enerji
- [ ] 3-dizilim (mushaf/nüzul/rastgele) değişmezlik testleri
- [ ] kozmolog + genetikçi mercekleri

## 2026-08-05 OTURUM-2 (analiz) ✓
- YÖNTEM DEĞİŞİKLİĞİ: konum-eşli null zorunlu (Allah yoğunluğu 1.46x eğimli) → bulgu_konum_esli_null.json
- zikir bulgusu KISMİ GERİ ÇEKME: yalnız zikir→beşer ayakta (p=0.0000); insân/yaratma/nâs/Allah/Rab düştü
- kapsam çiftleri: gök→yer oran 0.05 (yapışık), beşer→insân nötr → bulgu_kapsam_ciftleri.json
- beşer dikey okuma (37 geçiş, 4 öbek); madde 7/7 hep işlemle birlikte → bulgu_beser_dikey.json

### AÇILAN YENİ MADDELER
- [x] **Gradyan cetveli konum-eşli null ile yeniden koşuldu (2026-08-06)** — bulgu_gradyan_cetveli.json v2:
      anlamlilik_konum_esli() dikey_oku.py'ye kalıcı eklendi (20 dilim, profil-eşli, 2000 perm).
      GERİ ÇEKİLENLER: iman iç-halkadan tamamen düştü (0.001→0.107), zikir dış-halkadan düştü
      (0.31; konum-eşli bulgunun öngörüsüyle uyumlu), tövbe nominal bile kalamadı (0.14),
      tuğyân 0.006→0.030 nominale indi; mağfiret 0.00150 SINIR VAKASI (eşik 0.00125).
      AYAKTA: hudûd/takvâ/ilim/hidâyet iç halka; Rab/tekzîb/insân dış halka.
      Arayüz rozetleri v2'den yeniden gömüldü.
- [x] **Gradyan-dışı düz-null bulgular denetlendi (2026-08-06)** — dört dosyaya v2 bloğu işlendi:
      · abd-fiil DOĞRULANDI-GÜÇLENDİ (med 4 vs null 14, p=0.0; isim nötr ✓) — sentaks-alanı temeli sağlam
      · karşı-kutup KISMÎ GERİ ÇEKME: iman(0.001→0.14) ve nûr düştü; hidâyet+takvâ ✓B; asimetri yönü
        korundu (sağlam kutupların hepsi pozitif, 6 negatifin hepsi nötr) ama 3→2'ye zayıfladı
      · denge/mîzan kontrastı DOĞRULANDI-GÜÇLENDİ (konum-eşli fark p=0.00133; sahne tek başına p=0.001);
        nüans: "emir yapışık" tek başına düştü (p=0.33), taşıyıcı iddia katman-farkı
      · zikir dosyası Oturum-2 geri çekmesiyle UZLAŞTIRILDI (bayraklar dosyaya işlenmemişti);
        ayakta kalan tek eksen zikir→beşer
- [ ] hudud_ekseni makro-kutuplar (n150): coğrafya uyarısı zaten var; Mekkî/Medenî-katmanlı
      yeniden ölçüm ön-kayıtlı listedeki 7. maddeyle birleşik ele alınsın
- [ ] Yaratılış sahnesi 16 ikili sıra ilişkisi: 'kelime sırası ≠ olay sırası' riski açısından denetlensin (fiil-önde sorunu)
- [ ] madde→ruh zinciri: kısıt beşer'den kaldırılıp tüm korpusta aransın (n=2 yetersiz)
- [ ] gök/yer yapışıklığı: diğer kozmik çiftlere genişlet (güneş/ay, gece/gündüz)

## 2026-08-05 OTURUM-1 ✓
- P0 kapanış teyidi: بشر(84/37/2), أنس(241/71/19/7), خزن(8/4/1) korpusla doğrulandı; tablo_dogrula 430/430 ✓
- ملك kökü düzeltmesi: مَلَك mülk→melek, مَلِك→kral (melek 88/mülk 98/kral 20)
- Gradyan cetveli 8→40 kavram, Bonferroni'li (bulgu_gradyan_cetveli.json)
- Depo rutini işledi: kaynak = github.com/sebahattintanas/claude_kuran_okuma (clone ile tazelendi)

## BU OTURUMDA TAMAMLANANLAR ✓ (önceki)
- ظلم → zulüm/zulmet ayrımı (nûr-doğrulama %61 vs %5)
- كذب → kizb/tekzîb ayrımı (tekzîb=vahiy reddi, 242 vs 40)
- AŞMA ekseni temizlendi (440→~150, zulüm ayrı eksen)
- Allah-ekseni dikey okuma yöntemi + gradyan (bulgu_allah_ekseni_dikey.json)
- Allah↔karşı-kutup mesafe (bulgu_karsi_kutup_mesafe.json)
- Matematikçi makro+mikro karşılaşmaları (karsilasmalar.json)
- Denge/mîzan iki-katmanlı ölçü (bulgu_denge_mizan.json)


---

## 2026-08-18 — Sûre 15 (Hicr) oturumu ekleri

### ÇÖZÜLDÜ (teşhis): fig alanı 175→73→3 daralması
`defter5.py` MM kuralı ardışık **morfolojik segment**lere bakıyor, kelimelere değil.
Belirli isimde araya `ٱل` (DET, pos=P) segmenti girip bitişikliği kırıyor.
Kanıt: 15:85 `ٱصْفَحِ ٱلصَّفْحَ` birebir mef'ûl-i mutlak, etiket almıyor.
Ölçüm: segment düzeyi V+VN = **3** · kelime düzeyi V+VN = **33** · V+(VN|ACC) = **127**.
→ Aday 282. YAPILACAK: kuralı kelime düzeyine taşı, defter5'i yeniden koştur,
defter5'teki diğer bitişiklik kurallarını da denetle.

### YENİ ÖLÇÜM BORCU: QASEM iki yönde de hatalı
- Yanlış pozitif: 15:44 `مَّقْسُوم`, 15:90 `ٱلْمُقْتَسِمِين` (قسم = paylaştırma, yemin değil)
- Yanlış negatif: 15:72 `لَعَمْرُكَ` (açık yemin, etiketsiz)
- Sûrenin tek gerçek yemini: 15:92 `فَوَرَبِّكَ`
→ Aday 271 + 278. Kural `kavram_ad` ile yeniden kurulmalı.

### P0 borç #1 (esmâ) — Hicr doğrulama seti
Altı sahte pozitif, dört sınıf: `عَلِيم` (15:53, غلام sıfatı — aynı sûrede 15:25'te
GERÇEK mühür parçası) · `سَلام` (15:46, 15:52) · `مُؤْمِن` (15:77, 15:88) · `أَحَد` (15:65).
Aday 283'teki 'zamir + iki belirli sıfat' kalıbı ayırıcı araç adayı olabilir.

### 268 GERİ ÇEKİLDİ → 279
Hapaks köklerin Allah-mesafesi n=1 olduğu için tek başına yorumlanamaz.
`فضح` = 2 kelime ("yapışık") tamamen komşusundan geliyor: 15:69, sûrenin ilk Allah lafzı.
`لقح` = 178 ("en uzak"). Aynı sûre, iki uç, ikisi de n=1.

### Kavram/kök ayrımı — yeni kanıt (aday 267)
Kök `روح` (57) sorgulandığında ruh + rüzgâr birleşiyor, sahte komşuluk üretiyor
(`صرصر` ×116). `kavram_ad` ile ruh 24 / rüzgâr 29'a ayrılıyor, profiller tamamen ayrışıyor.
Hicr iki anlamı yedi ayet arayla kullanıyor (15:22 rüzgâr, 15:29 ruh).
→ Tur sonunda kök düzeyinde ölçülmüş TÜM adaylar yeniden bakılacak.


---

## 2026-08-20 — Sûre 16 (Nahl) tamamlandı

**Kapsam:** 2248/6236 ayet = %36.0. Aday sayısı 328 (α/328 ≈ 0.000152).

### Yeni ölçüm borçları
- **QASEM iki yanlış negatif daha:** 16:56 ve 16:63 `تَٱللَّهِ` etiketsiz (15:72 `لَعَمْرُكَ` ile üç oldu). Ve 16:38 `أَقْسَمُوا۟` DOĞRU pozitif → ayrım kökte değil BABDA: bab IV = yemin, bab I/VIII/ism-i mef'ûl = paylaştırma. Onarım reçetesi: yemin harfleri و/تَ/لَ + lafız|GEN isim, artı قسم bab IV. → adaylar 271, 278, 296, 302
- **P0 borç #1 (esmâ) en büyük sınıf:** `آخِر` Nahl'de 7 kez sahte esmâ (%18). Ek sahteler: `شَهِيد` ×3, `أَحَد` ×2, `مُؤْمِن` ×2, `سَلام`, `مَوْلَى`, `شاكِر`, `وَلِيّ`. → aday 291
- **P0 borç #2:** 16:12 (beş gök terimi, altı xref) yıldız 0. Kozmik çift testinin birincil vakası. → aday 293

### Dikey okuma güvenilirliği — ACİL
Yedi vaka + iki karşı örnek + bir kesin teşhis:
`رُوحُ ٱلْقُدُسِ` terkibi tek başına ruh kavramının `قدس` ×118.3 skorunu üretiyor. **Zenginleşme skorlarından sabit terkipler ayrıştırılmadan hiçbir dikey okuma sonucu kullanılamaz.** Jackknife + terkip envanteri zorunlu. → adaylar 288, 295, 301, 320
Etkilenen önceki adaylar: 266 (ruh/15:29), 273 (نجو/15:59-60).

### `esit` alanı yetersiz — genişletme reçetesi
Yalnız TAM ayet eşleşmesi buluyor. Kaçırdıkları:
1. Tek değişkenli ikiz (Nahl'de 8 vaka, 8 ayrı sınıf) → 294, 318, 323
2. Sûre-aşırı şahıs varyasyonu (`يَعْلَمُونَ`→`تَعْلَمُونَ`) → 304
3. Kalıp birleştirme (16:61 = 35:45 açılışı + 7:34 kapanışı) → 317
Reçete: kelime dizisi hizalaması + fark büyüklüğü ölçeği (harf/biçimbirim/kelime/öbek).

### Sıradaki sûre
17 (İsrâ). Hicr–Nahl karşıtlığı (aday 289) İsrâ ile üçlü karşılaştırmaya açılacak.


---

## 2026-08-21 — OTURUM KAPANIŞI

### Bu oturumda tamamlanan sûreler
15 Hicr (99) · 16 Nahl (128) · 17 İsrâ (111) · 18 Kehf (110) — dördü de TAM.
19 Meryem 1-60 yazıldı; **devam noktası 19:61**.

### Kapanan / revize edilen adaylar
- **268 → 279**: hapaks Allah-mesafesi n=1 olduğu için tek başına yorumlanamaz (geri çekildi)
- **282**: fig/MM daralmasının MEKANİZMASI bulundu (segment düzeyi bitişiklik)
- **327 revize**: MM üç ayrı sebeple düşüyor — ٱل segmenti, zamir eki, araya giren kelime
- **319, 336, 341 KAPANDI**: üçlü/dörtlü diziler tamamlandı
- **317, 345, 354 GENİŞLEDİ**: üçüncü/dördüncü üyeler bulundu
- **323 REVİZE**: 17:7'nin eksik şart cevabı 17:104'te bulundu — tespit ayet düzeyinde
  doğru, SÛRE düzeyinde değildi

### Açık kalan P0 borçlar (öncelik sırasıyla)
1. **MM/fig onarımı** (282+327): kelime düzeyine geç + pencere genişliği kalibre et.
   Ölçüldü: 0 kelime→134 ayet · 1→96 · 2→37 · 3→23 (toplam 290). Doğrulama testi:
   17:11, 17:19, 17:63, 17:80, 17:91, 17:106, 17:111, 18:99, 18:100, 19:3 yakalanmalı.
2. **QASEM onarımı** (271+278+296+302): kök+bab birlikte; yemin harfleri و/تَ/لَ kapsama alınmalı
3. **esmâ bağlam kuralı** (272+291+329+375): doğrulama seti artık Hûd 5 + Hicr 3 + Nahl 1
   + İsrâ 7 + Kehf 3 + Meryem 4 lemma. آخِر, كَبِير, بَرّ, وَلِيّ, أَحَد, سَلام, مُؤْمِن, شَكُور, حَسِيب, مَلِك, جَبّار
4. **kafiye kırığı kuralı** (326): sûre-içi baskın sınıftan sapma ölçütü eklenmeli;
   şu anki kural ilk ayeti hiç göremiyor (17:1 kaçtı)
5. **esit alanı genişletmesi** (294+304+318+374+376+377): tam eşleşme dışında
   (a) tek kelime/biçimbirim farkı (b) sûre içi çift (c) AYET ÇİFTİ aynalanması
   (d) uzak sûre-içi ikiz — dördü de şu an görünmüyor
6. **jackknife denetimi** (288+295+301+320+335): zenginleşme skorlarından sabit
   terkipleri ayır; قتل (n=170) kontrol grubu, روح القدس örnek vaka

### Biçim borcu KAPANDI
Türkçe karşılık kuralı denetime bağlandı: `tablolar/kok_turkce.json` (274 kök) +
`betikler/turkce_denetim.py`. Sûre 15-19 taramasında **0 ihlâl**.
Kural: her blok kaydından sonra denetim koşturulur, sıfır olmadan blok kapanmaz.

---

## SES / PROZODİ KATMANI (2026-08-22 oturumu)

### Yapıldı
- **Nakarat prozodi sınavı KOŞULDU.** Rahmân 55, tek kārî, 78/78 ayet-ayet mp3.
  Ön-kayıt `notlar/ON_KAYIT_nakarat.md`, betik `betikler/nakarat_olcum.py`,
  sonuç `bulgular/bulgu_nakarat_prozodi.json`. Adaylar 395–396.
  Birincil: CV(dpm|nakarat)/CV(dpm|kontrol) = 0,261 · p<0,0001.
- **Kafiye seslendirme setleri** üretildi (`betikler/kafiye_seslendirme.py`).
  Çapraz tablo aday 397: kafiye sınıfı ≈ fâsıla tipi, ayrışan tek sınıf R.

### P1 — ANLATI MODU PROJESİ (ertelendi, ayrı proje olacak)
Amaç: Türkçe meal üzerinden tam Kuran "dinleme/anlatı modu".

Karara bağlanmış olanlar:
- **Süre katmanı DEVROLMUYOR.** Ölçülen süre bağı mora üzerinden, mora Arapça'ya ait.
  Meal'de mora yok. Türkçe tarafta "ritmi metinden aldık" İDDİASI KURULAMAZ.
- Devrolan katman: anlatı yapısı — konuşan/muhatap (`sah`,`bask`), doğrudan söz
  (قول fiili, 1.322 ayet %21,2), nakarat (119 ayet, 15 sûre), edim
  (haber 3589 · emir 1311 · şart 855 · soru 808 · nida 363 · yasak 289),
  adlı aktör (`tablolar/aktor_tablosu.json`, 61 aktör / 16'sı konuşan / 61 ayet — SEYREK).
- **Telif:** Diyanet meali korumalı çeviri; `kuran_meal.json` repoda YOK, yerelde.
  Yapı üretimi burada, metinle birleştirme yerelde. Yayım düşünülürse Elmalılı 1935
  orijinali kamu malı — o zemine geçilmeli.
- Türkçe TTS bu ortamda yok; ses üretimi dışarıda.

Yapılacak ilk adım:
1. `sahne_partisyonu.py` — ayet başına: konuşan şahıs, adlı aktör, doğrudan söz
   aralığı, nakarat üyeliği, edim + Arapça tarafın süre hedefleri. Meal için
   SADECE ayet referansı, metin gömülmez.
2. Pilot sûre seçimi: Rahmân 55 (ses elde, nakarat ölçülü, 2D ikil hitap 97 kez —
   Türkçede ikil yok, meal bu bilgiyi siliyor, partisyon geri getirebilir)
   VEYA Şuarâ 26 (Mûsâ–Fir'avn diyaloğu, karakter ekseni zengin, 6 nakarat kümesi).
3. Sürüklenme sınavı (aday 396) BAĞIMSIZ kārî/sûre ile — Şuarâ 26 doğal aday.

### P2 — ses tarafı açık borçlar
- Kārî adı KAYDEDİLDİ: **Mahmûd Halîl el-Husarî (murattal)**. Sürüklenme sınavı
  (aday 396) için ikinci kārî gerekiyor — karşılaştırma murattal-murattal olmalı,
  mujawwad'da sapmanın ne kadarı icra süslemesi ayırt edilemez.
- edim → F0 sınavı (soru/nida/emir/haber konturda ayrışıyor mu) hiç koşulmadı.
- Şedde (23.016) · kalkale (3.415) · ğunne (7.342) katmanları `tilavet_sentez.py`'ye
  eklenmedi. NOT: bunlar tecvîd/Arapça'ya ait, Kuran'a özgü DEĞİL — 0110/elif dersi.

---

## VARLIK KATALOĞU DENETİMİ (2026-08-22) — P1 BORÇ

**Durum: TEŞHİS TAMAM, DÜZELTME ERTELENDİ.**
Düzeltmek `tablolar/varlik_katalog.json`'u yeniden üretmeyi gerektirir → okuma
sırasında araç değiştirme yasağına girer. Tur sonunda toplu yapılacak.

### Bulgu: 91 kayıtlık katalogda 9 kayıt SESSİZCE düşüyor
Hata vermiyorlar, sıfır sonuç dönüyorlar. Dördü tek bir hatanın kopyası.

| sebep | kayıt | doğrusu | kayıp geçiş |
|---|---|---|---|
| Latin `r` sızması | `kader/ölçü` = `قدr` (U+0072) | `قدر` | 132 |
| bare elif ↔ hemzeli elif | `emanet` = `امن` | `أمن` | 879 |
| " | `yer/arz` = `ارض` | `أرض` | 461 |
| " | `emr` = `امر` | `أمر` | 248 |
| " (kelime modu) | `Ye'cûc-Me'cûc` = `ياجوج\|ماجوج` | `يأجوج\|مأجوج` | 2 ayet (18:94, 21:96) |
| hareke SIRASI (NFC) | `Eyyûb` = `أَيُّوب` | shadda↔damme sırası ters | — |
| korpus PN saymıyor | `Tûr`, `arı` (`نَحْل`), `Hüdhüd` | `kok` modu denenmeli | — |

**Toplam ölçülen kayıp: 1.722 kök geçişi + 2 ayet.**

### Eyyûb vakası — kuralın ihlâli VE çözümü
Katalog ve korpus AYNI 7 kod noktasını içeriyor, sırası farklı:
- katalog: ي + َ + ُ(064F) + ّ(0651) + و + ب
- korpus : ي + َ + ّ(0651) + ُ(064F) + و + ب

`==` false, **NFC normalizasyonu ikisini eşitliyor.** "Lemma anahtarları elle
yazılmaz, korpus çıktısından kopyalanır, NFC ile eşleştirilir" kuralının canlı ihlâli.

### Yapılacaklar (tur sonu)
1. `betikler/varlik_katalog.py` KATALOG listesindeki 9 anahtarı düzelt.
2. **Tüm arama anahtarlarını NFC'den geçir** — `varlik_makinesi.ayetleri_bul`
   içine normalize ekle. Şu an `in` ile ham karşılaştırma yapıyor.
3. `Tûr`/`arı`/`Hüdhüd` için `pn` yerine `kok` modu dene; korpus bunları cins isim
   sayıyor, katalog özel isim sayıyor — hangisinin doğru olduğu karara bağlanacak.
4. `varlik_katalog.json` yeniden üretilecek (şu an 191 varlık, 6'sı eksik).
5. `yer/arz` ile mevcut `yer` kaydının ne ölçtüğü ayrıştırılacak — çakışma riski.
6. AYNI DENETİM diğer elle-yazılmış anahtar dosyalarına uygulanacak:
   `kok_anlam_tablosu.json`, `kok_anlam_istisna.json`, `kavram_katalogu.json`,
   `kok_turkce.json` (314 kök). Denetim betiği: Latin karakter + bare/hemzeli elif
   + NFC sırası, üç testi birden.

### Denetim sırasında düzeltilen KENDİ hatam
İlk denetimde `morph.txt` konum alanını 5 parçalı sandım, gerçekte **4 parçalı**
(`sûre:ayet:kelime:segment`). Bu yüzden "PN etiketi hiç yok, 36/36 kayıt düşmüş"
dedim — YANLIŞTI. Doğrusu: 3.911 PN kelime, 2.464 ayet, 106 benzersiz PN lemma,
36 kayıttan 4'ü düşüyor. Kayda geçsin ki tur sonunda yanlış rakama dayanmayalım.

---

## ANAHTAR DENETİMİ — REPO GENELİ (2026-08-22) — P0 BORÇ

Betik: `betikler/anahtar_denetim.py` (SALT-OKUR, hiçbir dosyayı değiştirmez).
20.838 anahtar/sabit tarandı (.json + .py). Dört test: T1 Latin sızması,
T2 yazım (hemze/harekesizlik), T3 sıra/varyant, T4 korpusta yok.

### NEDEN OLDU — tarih kanıtı
`git log`: `varlik_katalog.py` **5 Ağustos**'ta ilk toplu yüklemede geldi ve
o günden beri BİR KEZ BİLE değişmedi (`قدr` hatası doğduğu gün içindeydi).
Aradan geçen 17 günde 246 dosya dokunuşu oldu, bu dosya hiçbirine dahil değil.
`turkce_denetim.py` ise **21 Ağustos**'ta yazıldı.
=> Kök tabloları korpustan TÜRETİLDİĞİ için temiz (kok_envanteri 1.651,
   kok_anlam_tablosu 430, kok_turkce 314 → hepsinde SIFIR ihlâl).
   Bozulma yalnızca ELLE YAZILAN yerlerde ve DENETİM ÖNCESİ dönemde.
İki yapısal boşluk: (a) denetim .json tarıyor, .py taramıyor —
oysa anahtarların elle yazıldığı yer tam olarak .py. (b) geriye dönük
tarama hiç yapılmadı; kural sadece YENİ üretime bakıyor.

### EN AĞIR BULGU: zaman_of() kök kümeleri
`varlik_makinesi.py` sat.48-50 ve `kavram_arac.py` sat.46-48 (KOPYALI):
GECMIS/GELECEK/SIMDI kümelerinde **18/34 anahtar tutmuyor.**

Ölçülebilir kayıp — dördü de hamzesiz elif:
| küme | yazılan | doğrusu | kayıp geçiş |
|---|---|---|---|
| SIMDI | `ءمن` | `أمن` | 879 |
| SIMDI | `ايي` | `أيي` | 597 |
| GELECEK | `اخر` | `أخر` | 250 |
| SIMDI | `امر` | `أمر` | 248 |
**Toplam 1.974 geçiş.** Kaybedilenler SIMDI kümesinin EN YÜKSEK FREKANSLI üyeleri.

Kalan 14 anahtar (نوح, ابر, موسي, فرعن, عاد, لوط, ارسل, نار, ساع, تقو, ثمد, قيم…)
korpusta kök olarak HİÇ yok — bunlar ÖZEL/CİNS İSİM. Kök ile lemma karıştırılmış:
PN lemma tarafında aranmalıydılar.

**ETKİ:** `zaman_of()` → `varlik_makinesi.oku()` → `varlik_katalog.json`'daki
**40 kavramın `zaman` profili eksik veriyle üretilmiş.** Bu alana dayanan
hiçbir çıkarım tur sonu düzeltmesi yapılmadan kullanılamaz.

### T3 TESTİ HAKKINDA — ÖNCEKİ TEŞHİS DÜZELTİLDİ
İlk raporda "korpusun NFC-dışı olabileceği" ima edilmişti. YANLIŞ.
Ölçüldü: korpusun ham hâli ZATEN NFC (shadda ccc=33 > damme ccc=31,
NFC damme'yi öne alır ve korpus da öyle saklar). `aktor_tablosu.json` ve
`pn_turleri.json`'daki 15 "NFC" uyarısı YANLIŞ ALARMDI — o dosyalar korpusu
sadakatle kopyalamış. Sapan taraf `varlik_katalog.py`'deki elle yazılmış
`أَيُّوب`'tur (shadda-önce girilmiş).
=> Ölçüt "NFC'den sapma" DEĞİL, **"KORPUS FORMUNDAN sapma"**. Betik düzeltildi.

### TUZAK — betiğin önerileri körü körüne uygulanmayacak
`ثمد → أمد` ve `قيم → أيم` önerileri betiğin hamze-varyantı denemesinden
geliyor ve YANLIŞ (Semûd = `ثمود` lemma; kayyim = `قوم` kökü).
Her öneri ELLE doğrulanacak.

### Yapılacaklar (tur sonu, toplu)
1. `zaman_of()` kümeleri: 4 hamze hatasını düzelt, 14 isim anahtarını
   kök yerine PN lemma tarafına taşı. İKİ DOSYADA birden (kopyalı).
2. `varlik_katalog.py`: 9 anahtar (bkz. VARLIK KATALOĞU DENETİMİ bölümü).
3. `varlik_katalog.json` yeniden üretilecek; `zaman` alanı DA değişecek.
4. `anahtar_denetim.py` denetim zincirine bağlanacak: her blok kaydından sonra
   `turkce_denetim.py` ile birlikte koşulacak, sıfır olmadan blok kapanmaz.
5. EDAT_MUAF listesi gerekçeli tutulacak; körlemesine genişletilmeyecek.

## 2026-08-25 — P0 BORCU YÜKSELTİLDİ: dikey okuma konum-eşli null (aday 435)

Daha önce "Allah-mesafesi ölçümleri konum-eşli null ile yeniden test edilecek"
diye yazılıydı. Artık BÜYÜKLÜĞÜ ÖLÇÜLDÜ ve borç P0'ın başına alındı:

- Ölçüt: mushaf akışında en yakın Allah lafzına mutlak kelime mesafesi (medyan).
- Akış **sûre ve ayet sınırlarını tanımıyor**. En büyük lafız boşluğu 1075 kelime
  (53:62 → 57:1) ve 29 sûrede lafız hiç geçmiyor (korpusun %3.8'i).
- Korpusu 20 dilime böldüğümde taban medyanı **5 ile 72 arasında** değişiyor = 14.4 kat.
- Konum-eşli null ile: n>=15 olan **469 kökün 154'ünün (%32.8) etiketi değişiyor**,
  11'i yön değiştiriyor (UZAK ↔ yakın).

**Yapılacaklar:**
1. `dikey_oku.py`'ye konum-eşli null eklenecek; dilim genişliği ön-kayıtla
   sabitlenecek (20 dilim POST-HOC seçildi, duyarlılık analizi şart).
2. `okuma_metni.json`'daki TÜM dikey satırları yeniden üretilecek (sûre 20: 135
   ayet, sûre 21: kısmi).
3. İkinci ölçüt eklenecek: **"en yakın Allah lafzı aynı ayette mi"** oranı —
   ayet sınırını tanır, yorumu daha kolay. Ölçüldü: شهد %52.5 · فري %65.0 ·
   قول %34.4 · نطق %16.7 · عين %13.8 · سحر %4.8.
4. Adaylar 415 ve 417 yeniden hesaplanacak (ikisi de ayakta kalıyor ama
   düz değerler büyüklüğü abartıyor: خور 182 → eşli beklenti 72).

**Okuma DURMUYOR.** Dikey katman üretilmeye devam eder; `_dikey_notu` uyarısı
sertleştirildi ve etiketlerin alıntılanamayacağı yazıldı. Ham medyan sayıları geçerli.

## 2026-08-27 — SÛRE 21 VE 22 TAM OKUNDU; DÖRT YENİ P0 BORCU

Bu oturumda Enbiyâ (112/112) ve Hac (78/78) TAM okundu. Okunan ayet 1293 → 1463.
Kök tablosu 720 → 880 (160 yeni karşılık, hepsi korpustan kopyalanmış anahtarla).
Adaylar 437 → 464 (27 yeni). `anahtar_denetim.py` üç kez koşuldu, taban listesiyle
birebir aynı kaldı (58 ihlâl, diff = 0).

### P0-a — ESMÂ TABLOSU: HATA BÜYÜKLÜĞÜ ÖLÇÜLDÜ (aday 461; 414 ve 444 ile birleşti)

Yukarıdaki "esmâ tespiti bağlama taşınacak" borcu artık SAYILARLA sabit:

- Korpus esmâ token toplamı **2077**. En sık lemma `مُؤْمِن` ile **202 token = %9,7**.
  `مُؤْمِن` ilâhî ad olarak korpusta YALNIZ 59:23'te geçiyor → **201/202 = %99,5 hata**.
  Tek bir lemma esmâ tablosunun onda birini bozuyor.
- Sûre bazında ölçülen hata oranı: sûre 20 **%38** · sûre 21 **%47** (17 tokenin 8'i
  kesin yanlış, 2'si şüpheli) · sûre 22 **%29** (38 tokenin 11'i yanlış).
- Sûre 22'nin oranının düşük olmasının sebebi ÖLÇÜLDÜ: bu sûrede esmâların çoğu
  MÜHÜR konumunda ve mühür konumu bağlamı sabitliyor. **"Mühür konumu" onarım
  ölçütlerine yeni bir sinyal olarak eklendi.**
- TABLO ASİMETRİSİ: `مُؤْمِن` esma_listesi'nde VAR / pn_lemma_listesi'nde YOK;
  `مُسْلِم` pn_lemma_listesi'nde VAR (tür 'kavim', 39 ayet) / esma_listesi'nde YOK.
  İki tablo aynı anlam alanını ters yönde bölüyor.

**Onarım ölçütleri (sûre 20-22 gözlemlerinden türetildi, altı test):**
(a) gönderge testi — lemma lafza/Rab'be bağlanabiliyor mu;
(b) çoğul testi — çoğul biçim esmâ maddesi olamaz (21:51, 21:81 `عالِم`);
(c) sıfat testi — isim tamlamasında niteleyen konumda mı (`ضَلَٰلٍ مُّبِينٍ`, `رِزْقٌ كَرِيمٌ`);
(d) çift-ucu testi — bir karşıtlık çiftinin ucu mu (`دنيا/آخرة`, `قريب/بعيد`);
(e) yergi testi — yergi kalıbında mı (`لَبِئْسَ ٱلْمَوْلَىٰ`, 22:13);
(f) yüklem testi — emir yükleminin parçası mı (`بَرْدًا وَسَلَامًا`, 21:69);
(g) YENİ — mühür konumu testi: `esma_k.muhur == True` ise bağlam neredeyse her zaman geçerli.

**Etki alanı:** sûre 1-22 arasındaki BÜTÜN makro profillerin esmâ sayımları bu hatayı
taşıyor; onarım sonrası hepsi yeniden üretilecek. Esmâ tabanlı hiçbir bulgu kapatılamaz.

### P0-b — DİKEY KATMAN LEMMA AYIRMIYOR (aday 452) — 435 İLE BİRLİKTE KOŞULACAK

`dikey_oku.py` `kok=` ile çağrıldığında kökün BÜTÜN lemmalarını topluyor;
`kok_anlam_tablosu.json`'daki ayrımı kullanmıyor. Somut vaka: 21:44'ün ▽ satırında
`طرف` için "bakış-kısan ×564,8" görünüyor — kaynak `قَٰصِرَٰتُ ٱلطَّرْفِ` (37:48, 38:52,
55:56) ve o lemma `طَرْف` *(bakış)*, oysa ayetin lemması `طَرَف` *(uç)*.
Bu blokta görülen öteki karışımlar: `نهر` · `سبح` · `حبب` · `نور` · `ظلم` (21:87'de
"karanlık" ve "zulüm" AYNI AYETTE) · `نسل` (korpusta 2-2 bölünüyor).

**KRİTİK:** aday 435 (konum-eşli null) zaten 154+ dikey satırını yeniden ürettirecekti.
Şimdi aynı satırların lemma tarafı da bozuk çıktı. **İkisi TEK GEÇİŞTE koşulmalı**,
yoksa satırlar iki kez üretilir. `dikey_oku` zaten `kavram_ad=` parametresini destekliyor.

### P0-c — JACKKNIFE KIRILGANLIĞI ÖLÇÜLDÜ (aday 451)

`نقص` için "▸önce ömür ×156,1" katı YALNIZ İKİ ayetten geliyor (21:44 ve 35:11) ve
o iki ayette `عمر` TERS rollerde (biri uzayan, biri eksiltilen). 35:11 çıkarılırsa
geçiş 3→1 düşer, eşik altına iner, kat kaybolur.

**Onarım:** `zenginlik()` her kavram için (a) katkıda bulunan AYRI AYET sayısını,
(b) tek ayet çıkarıldığında katın düşüşünü raporlayacak. ×kat yanında "k ayet" zorunlu
alan olacak. Eşik önerisi: **en az 3 AYRI ayetten gelmeyen zenginleşme yazılmayacak.**
Onarım öncesi ölçülecek: mevcut satırlardaki kaç kayıt bu ölçütü geçemiyor?
(Aynı sınıf: `قدس` ×118,3 vakası.)

### P0-d — AKTÖR TABLOSU TASARIM KARARI (aday 462) — KARAR VERİLMEDİ

`pn_lemma_listesi.json` 106 lemmayı sözlüksel eşleştiriyor (kisi 40 · yer 24 ·
kavim 13 · sahte-ilah 10 · gayb 8 · diger 6 · kitab 4 · ilahi 1). Sıfat cümlesi,
ism-i mevsûl ve fiil cümlesi hiç bakılmıyor. Somut tutarsızlık:

- 22:17'de altı topluluk sayılıyor, ÜÇÜ kaydediliyor (`صابِئ` · `نَصْرانِيّ` · `مَجُوس`);
  `ٱلَّذِينَ ءَامَنُوا۟` · `ٱلَّذِينَ هَادُوا۟` · `ٱلَّذِينَ أَشْرَكُوٓا۟` kaydedilmiyor.
- Ama `يَهُود` ZATEN listede (tür 'kavim'): lemma biçimiyle geçtiği 8 ayette aktör
  kaydediliyor (2:113 · 2:120 · 3:67 · 5:18 · 5:51 · 5:64 · 5:82 · 9:30), fiil biçimi
  `هَادُوا۟` ile geçtiği 10 ayette kaydedilmiyor (2:62 · 4:46 · 4:160 · 5:41 · 5:44 ·
  5:69 · 6:146 · 16:118 · 22:17 · 62:6). Aynı topluluk, ayrı muamele.
- Künyeler de dışarıda: `ذَا ٱلْكِفْلِ` (21:85) ve `ذَا ٱلنُّونِ` (21:87) kaydedilmiyor;
  `ٱلْمَسْجِدِ ٱلْحَرَامِ` (22:25) de terkip olduğu için kaydedilmiyor.

**Üç seçenek, her biri ölçüm sonucunu değiştirir:**
(a) DAR — topluluk adları çıkarılır, yalnız kişi/yer/gayb kalır. 22:17'de 3→0.
(b) ORTA — topluluk adları kalır, fiil biçimleri de eşlenir (`هَادُوا۟` → `يَهُود`). 3→4.
(c) GENİŞ — "inanç-topluluğu" ayrı tür açılır, ism-i mevsûl + fiil kalıpları da alınır. 3→6;
    korpus etkisi çok büyük.

**KARAR OKUMA SIRASINDA VERİLMEZ.** Karar verilene kadar aktör yoğunluğu
KARŞILAŞTIRMALARI kullanılmayacak. Sûre 21 makro profilindeki "okumanın en aktör-yoğun
sûresi" ifadesi bu karara BAĞIMLIDIR ve şimdilik GEÇİCİ sayılmalıdır.

### P1 — QASEM ONARIMI GENİŞLEDİ (aday 443)

`تَٱللَّهِ` yemin kalıbı korpusta 9 ayette (12:73 · 12:85 · 12:91 · 12:95 · 16:56 ·
16:63 · 21:57 · 26:97 · 37:56) ve **0/9'u QASEM etiketi alıyor**. `تـ` Arapçada yalnızca
yemin harfidir — yanlış pozitif riski sıfır olan bir desen tamamen kaçırılmış.
Korpusta QASEM etiketi 71 ayette var, yani etiket ÇALIŞIYOR ama yemin harfleri
(`وَ` · `بـ` · `تـ`) kapsam dışında. **Onarım morfoloji katmanından yapılmalı, kök listesinden değil.**

### P1 — SÖZ EDİMİ: MUNKATI'A أَمْ (aday 438)

Ayet başında `أَمْ` geçen 61 ayetin yalnız 4'ü INTG kipi taşıyor; 45'i düz "haber".
Ayet-içi `أَمْ` (muttasıla, 62 ayet) AYRI etiketlenmeli — biri yeni soru açar,
öteki seçenek bağlar. Onarım sonrası bütün söz-edimi dağılımları değişecek;
onarım öncesi hiçbir söz-edimi bulgusu kapatılmayacak.

### YENİ TARAMA İŞİ — BÖLÜT İKİZLERİ (adaylar 450, 456, 457)

Sûre 21 ve 22 üç ardışık bölüt ikizi örneği verdi (21:41↔6:10 tam ayet ·
21:81-82↔38:36-37 · 21:92-93↔23:52-53) ve sûre 22 dokuz sûre-içi bölüt ikizi.
Artık tek başına bir iş kalemi:
- Lemma n-gram taramasıyla korpustaki BÜTÜN 5+ kelimelik özdeş bölütler çıkarılacak.
- Her çift için: bir sonraki ayetin de ortak lemma oranı ölçülecek.
- Farklılaşan öğe hangi sınıftan (nitelik / muhatap / kapanış / imperatif) kodlanacak.
- Null: aynı uzunlukta rastgele ayet çiftleri.

### TERS NEDENSELLİK RİSKİ TAŞIYAN ADAYLAR — BİRLİKTE KURULACAK (453, 459)

453: sûre 21'in 6 م-fâsılasının üçü `إِبْرَٰهِيم` adı.
459: sûre 21'de `وصف` üç kez ve üçü de fâsıla (21:18 · 21:22 · 21:112).
İkisinde de aynı sorun: kelime zaten sûrenin kafiyesine uyuyor. **"Kafiyeye uyduğu için
mi oraya kondu, oraya konduğu için mi kafiye saptı" ayrımı yapılmadan İKİSİ DE kapatılamaz.**
Test kafiye sınıfı SABİT tutularak kurulmalı.

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

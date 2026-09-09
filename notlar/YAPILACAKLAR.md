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

---

## 2026-08-31 — SÛRE 23 AÇILDI; İKİ BLOK OKUNDU (23:1-40)

Sûre 23 (Mü'minûn) makro profili sıfırdan çıkarıldı; 23:1-20 ve 23:21-40 tam kipte
okundu. Okunan ayet **1463 → 1503**. Kök tablosu **880 → 894** (14 yeni karşılık,
hepsi `kok_envanteri.json`'dan NFC eşlemesiyle KOPYALANDI). Adaylar **464 → 475**
(11 yeni, `AE_muminun` kümesi). Bağlar: yeni `AC_muminun` kümesi, 22 bağ.
`turkce_denetim.py` iki kez 0'a çekildi; `anahtar_denetim.py` (PYTHONHASHSEED=0)
iki kez koşuldu, her ikisinde de **58 ihlâl, taban listesiyle diff = 0**
(taranan anahtar 21055 → 21515).

### P0-a EK KANIT — ESMÂ: MÜHÜR SİNYALİ TERSTEN DOĞRULANDI (aday 467)

Sûre 23'te esmâ **12 token / 11 ayet / mühür SIFIR**; bağlam denetiminde **8/12
yanlış pozitif = %67**, okumada ölçülen en yüksek oran (20: %38 · 21: %47 · 22: %29).
Yedinci onarım ölçütü (mühür konumu bağlamı sabitliyor) mühürsüz bir sûrede
tersten doğrulandı: mühür yoksa hata tavan yapıyor.

**YENİ SORUN — ÖLÇÜTLER ÇATIŞIYOR.** 23:14 `أَحْسَنُ ٱلْخَٰلِقِينَ` *(yaratanların
en güzeli)*: ölçüt (b) çoğul biçimi dışlıyor, ölçüt (a) gönderge lafza bağlandığı
için tutuyor. Onarımda **ölçütler arası öncelik sırası belirlenmeli**; şu anki
yedi ölçüt sıralı değil, bu vaka sıralamayı zorunlu kılıyor.

### P0-b EK VAKA — DİKEY LEMMA KARIŞMASI (aday 474, 452 ile birlikte)

23:25 `بِهِۦ جِنَّةٌۭ` *(kendisinde delilik var)* — lemma `جِنَّة` *(delilik)*, ama kavram
katmanı `جنن` için 'cennet' veriyor ve dikey satırına cennet komşuluğunu getiriyor
(`تحت` *(alt)* ×22,6 · nehir ×21,9 · `عنب` *(üzüm)* ×20,3). Aynı hata **7:184'te
zaten belgeliydi** — yani bilinen bir vaka ikinci kez, farklı sûrede tekrar etti.
`kok_anlam_tablosu.json`'a `جِنَّة` ayrımı eklenmeli; 435 + 452 tek geçişinde.

### YENİ P1 — YILDIZ FORMÜLÜ KISA AYETE KAYIYOR (aday 472; 468, 129, 160, 246 kümesi)

Sûre 23'ün **16 ★★★ ayetinin tamamı n=4-12**; ★★★ ortalaması **5,69 kelime**,
sûre ortalaması **8,90**. Sebep ölçüldü: z değerleri YOĞUNLUK üzerinden
hesaplandığı için n=4-5'lik ayette TEK edilgen fiil `pas z=5,38`, TEK Rab geçişi
`rab z=3,94` üretiyor. Sûre 23 kaynak dağılımı (rab 8 · pas 4 · allah 3 · hapaks 1)
korpus dağılımından (hapaks 337 · rab 183 · pas 148 · allah 121 · n 91) sapıyor.

**Mercek üzerindeki etkisi ölçüldü.** Blok 23:21-40'ta **dört ★★★ ayetin dördünde
de** iki uzman merceği atlandı (çıpa yok); buna karşılık biyolojik öğe taşıyan
ayetler ★0-★1 aldı: 23:14 (`نطفة` *(nutfe)* · `علقة` *(alaka)* · `مضغة` *(çiğnem et)* ·
`عظام` *(kemikler)* · `لحم` *(et)*) ★ yok, 23:21 (davar/karın/süt) ★ yok,
23:35 (toprak/kemik) ★. **Tur sonu: uzunluk-eşli null ile ★ dağılımı yeniden
üretilecek.**

### BÖLÜT İKİZİ TARAMASI — İKİ YENİ GİRDİ

- **Aday 465 — korpusun en uzun ardışık tam-ayet ikizi ölçüldü: 23:5-8 ↔ 70:29-32,
  dört ayet.** Tarama `defter.json` `esit` alanı üzerinden yapıldı; uzunluk 4 olan
  tek dizi bu, ikinciler üçlü (15:36-38 ↔ 38:79-81 ve sûre 26 nakaratları).
- **Aday 473 — sûre 23 içinde iki paralel kıssa döngüsü, DÖRT katmanlı ikiz:**
  çağrı (23:23 = 23:32, sekiz kelime) · birinci itiraz (23:24 = 23:33) · ikinci
  itiraz (23:25 = 23:38, beş kelime sonra ayrışıyor) · kapanış (23:26 = 23:39,
  TAM AYET). Farklılaşan öğeler kodlandı: elçi adlı/adsız · nidâ var/yok ·
  suç hâl/fiil · araya giren itiraz sayısı 3→4.

### DEVAM NOKTASI

**Sûre 23, ayet 41'den.** İki bağ hazır bekliyor:
- 23:31 ↔ 23:42 bölüt ikizi (`أَنشَأْنَا مِنۢ بَعْدِهِمْ قَرْنًا` *(ardlarından bir nesil
  inşa ettik)*), 23:42 okunduğunda kapanacak.
- **21:92-93 ↔ 23:52-53** ardışık bölüt ikizi (aday 456) — 23:52'de farkın tam
  olarak imperatifte olduğu (`فَٱعْبُدُونِ` *(bana kulluk edin)* / `فَٱتَّقُونِ` *(benden
  sakının)*) doğrulanacak.

Önceki oturumlardan devreden borçlar (435+452 tek geçişte, 461, 451, 462, 431, 437,
443, 438) bu oturumda da ONARILMADI — katı kural gereği.

### ÜÇÜNCÜ BLOK EKİ (23:41-60) — ADAYLAR 476-479

**ADAY 456 DÜZELTİLDİ (aday 476).** Bekleyen bağ 21:92-93 ↔ 23:52-53 ölçüldü ve
**ön-kayıt yanlış çıktı.** Ön-kayıt "farkın TAM OLARAK imperatifte" olmasını
bekliyordu; ölçüm birinci ayette İKİ fark verdi: açılışta bir bağlaç
(`إِنَّ` *(muhakkak)* / `وَإِنَّ` *(ve muhakkak)*) ve kapanışta imperatif
(`فَٱعْبُدُونِ` *(bana kulluk edin)*, `عبد` bab I / `فَٱتَّقُونِ` *(benden sakının)*,
`وقي` bab VIII). Arada altı kelime birebir özdeş. İkinci ayette ayrışma çok daha
geniş: ortak gövde yalnız iki kelime, `زُبُرًۭا` *(parçalara)* eklenmiş, ikinci
yarılar tamamen farklı.

**DERS — ÖN-KAYIT DİSİPLİNİ:** "tam olarak X'te fark" iddiaları ön-kayıtta
**bağlaç ve edat düzeyinde de** belirtilmeli. Bölüt ikizi taramasında (450, 456,
457, 465, 473) farklılaşan öğe sınıflarına **BAĞLAÇ** eklenecek.

**YENİ — SÛRENİN İKİNCİ SIFAT ZİNCİRİ (aday 477).** 23:57-61, 23:2-9 ile aynı
kalıbı (`ٱلَّذِينَ هُمْ` *(onlar ki)* + mecrur + ism-i fâil) kullanıyor ama ekseni
farklı: birinci zincir **eylemlere**, ikincisi **Rab'be** bağlı — dört halkanın
dördünde de `رَبّ` *(Rab)*, üçünde `rab z ≥ 1,81`, ikisi bu yüzden ★★★. İsim-fiil
geçişi de yer değiştiriyor: birincide kapanışta (23:9), ikincide ikinci halkada
(23:58). 469 ile aynı ön-kayıtlı test kümesinde; **23:61 henüz okunmadı**,
zincirin kapanışı sonraki blokta ölçülecek.

**Aday 472 için ek kanıt.** Sûre 23'te bugüne dek okunan **yedi ★★★ ayetin
yedisinde de** biyolog ve uzay merceği atlandı (çıpa yok). Bu blokta ★★★ olan
23:58 ve 23:59 n=5 ve tek kaynakları `rab z=3,94`; buna karşılık coğrafî/maddî
öğe taşıyan 23:50 (`رَبْوَة` *(tepe)* · `مَعِين` *(akan su)*) ve 23:41
(`غُثَاء` *(sel süprüntüsü)*) ★ almadı.

**Devam noktası: 23:61.**

### DÖRDÜNCÜ BLOK EKİ (23:61-80) — ADAYLAR 480-485

**ADAY 438'E OKUMA İÇİNDEN İLK TEMİZ VAKA KÜMESİ (aday 483).** 23:68-72 arasında
dört `أَمْ` geçişi ölçüldü: 23:68'de `أَمْ` ayet İÇİNDE (muttasıla) ve ayet INTG
alıyor — ama INTG'yi veren `أَفَلَمْ` *(…mediler mi)* açılışı, `أَمْ` değil.
23:69, 23:70 ve 23:72'de `أَمْ` ayet BAŞINDA (munkatı'a) ve **üçü de 'haber'
etiketli, hiçbiri INTG almıyor** — yani bu sûrede munkatı'a `أَمْ`in **3/3'ü
kaçırılmış.** Aday 438'in korpus ölçümüyle (61 ayetin 4'ü INTG) birebir uyumlu.
**438'in onarımı bu dört ayetle sınanabilir:** onarım sonrası 23:69/70/72 INTG
almalı, 23:68'inki değişmemeli.

**YENİ P0 VAKASI — ESMÂ TABLOSU AYNI YAPIYI ÜÇ YERDE ÜÇ FARKLI SAYIYOR (aday 484).**
Sûre 23'te üstünlük tamlaması kalıbı üç kez ve hep aynı yapıda (üstünlük ismi +
belirli ism-i fâil çoğulu): `أَحْسَنُ ٱلْخَٰلِقِينَ` *(yaratanların en güzeli)* 23:14 ·
`خَيْرُ ٱلْمُنزِلِينَ` *(indirenlerin en hayırlısı)* 23:29 · `خَيْرُ ٱلرَّٰزِقِينَ`
*(rızık verenlerin en hayırlısı)* 23:72. **Yalnız birincisi esmâ sayılıyor.**
Onarımda üçü BİRLİKTE karara bağlanmalı — 1/3 savunulamaz. Korpus çapında
"üstünlük ismi + ism-i fâil çoğulu" envanteri çıkarılacak.

**KARŞILIK TABLOSU DÜZELTMESİ (aday 480).** `سمر` için `kok_turkce` yalnız "Sâmirî"
veriyordu; kökün dört geçişinin üçü 20:85/87/95'te `سَامِرِيّ` *(Sâmirî, özel ad)*,
biri 23:67'de `سَامِر` *(gece sohbeti eden)*. Karşılık genişletildi. Bu bir araç
onarımı değil, görüntü tablosunun bir maddesinin düzeltilmesidir. **Tur sonu işi:**
`kok_anlam_tablosu`'nda 2+ anlam taşıyan kaç kökün `kok_turkce` karşılığı tek anlam
veriyor?

**Aday 472/468 için ek ölçüm.** Bu blokta ★★★ ayet YOK; en yüksek ★★. Sûrede
okunan 80 ayetin yedi ★★★'ı da (16, 22, 26, 36, 39, 58, 59) n=4-5 aralığında ve
hepsinde iki uzman merceği atlandı. Blokta duyu adları taşıyan 23:78
(`سمع` *(işitme)* · `بصر` *(görme)* · `فأد` *(gönül, fuâd)*) ★ almadı.

**Devam noktası: 23:81.** Sûrede 38 ayet kaldı.

### BEŞİNCİ BLOK EKİ (23:81-100) — ADAYLAR 486-490

**YENİ P0 — KAYNAK METİN SORUSU İLK KEZ AÇILDI (aday 487).** 23:85, 23:87 ve
23:89'un üçünde de korpus (`morph.txt`, mustafa0x/quran-morphology) `لِلَّهِ`
okuyor: P+PN|GEN. Yaygın Hafs an Âsım baskılarında 23:85 `لِلَّهِ`, ama 23:87 ve
23:89 `ٱللَّهُ` merfû okunur. **Gerekçe ölçülebilir:** 23:86'nın sorusu
`مَن رَّبُّ` *(kim Rabbidir)*, 23:88'inki `مَنۢ بِيَدِهِۦ` *(kimin elindedir)* — ikisi de
merfû cevap ister; yalnız 23:84'ün `لِمَنِ` *(kimin)* sorusu mecrur cevabı
gerektirir. Korpusun okuyuşu iki ayette soru-cevap uyumsuzluğu üretiyor.

**Etki alanı:** (a) bu iki ayetin i'râb sayımı; (b) aday 486'nın "üç cevap birebir
aynı" ölçümü; (c) **korpusun hangi kıraati taşıdığı sorusu — projede DAHA ÖNCE HİÇ
SORULMADI.** `nuzul.json` ve `varlik_katalog` zaman alanıyla **aynı statüde**:
bu ayetlere dayanan hiçbir bulgu basılı bir mushafla doğrulanmadan kapatılamaz.
**Tur sonu işi:** korpusun kıraat tabanı belirlenecek, kıraat farkı taşıyan ayetler
taranacak. Bu, "kontrol korpusu yok" eksiğiyle aynı sınıfta bir kaynak sorusu.

**BİYOLOG MERCEĞİ SÛREDE HÂLÂ HİÇ YAZILMADI; İLK MERCEK 23:86'DA (adaylar 468, 472).**
100 ayetin on beş ★★★'ından **on dördünde iki mercek de atlandı.** İlk ve tek
mercek 23:86'nın 🜂 uzayı, çıpası `ٱلسَّمَٰوَٰتِ ٱلسَّبْعِ` *(yedi gök)*. Mercek satırı
yalnız ölçülebilir olanla sınırlandı: gök sayılmış bir çokluk olarak veriliyor,
sayı marife tamlamada sıfat konumunda, aynı kök çifti 23:17'de `طَرَآئِق` *(yollar)*
ile eşleşiyor. **Fiziksel katman modeli KURULMADI** — ayet gök cismi, hareket,
yörünge ya da ölçü terimi vermiyor.

**Yeni yapı ölçümleri:** üçlü soru-cevap nakaratı 23:84-89 (aday 486) · dört
ardışık `رَبِّ` çağrısı ve konum kayması 23:93-98 (aday 488) · `جور` kökü tek
ayette etken ve edilgen 23:88 (aday 489) · sûrenin TEK KELLA'sı 23:100 (aday 490).

**GERİYE DÖNÜK ONARIM:** `جور` karşılığı eklenince sûre 9'da (9:6) eski bir
karşılıksız anma açığa çıktı ve onarıldı — bilinen desenin bu oturumdaki ikinci
örneği (ilki 14:22 `لوم`).

### ALTINCI BLOK EKİ (23:101-118) — SÛRE 23 TAM, ADAYLAR 491-497

**SÛRE 23 (MÜ'MİNÛN) TAM OKUNDU — 118/118.** Okunan ayet 1463 → **1581**
(korpusun %25,4'ü). Tam okunan sûreler: 1, 9-23.

**SÛRENİN BÜYÜK HALKASI ÖLÇÜLDÜ (aday 491).** `فلح` *(kurtuluşa erme, felâh)*
kökü üç kez: 23:1 `قَدْ أَفْلَحَ ٱلْمُؤْمِنُونَ` PERF ve olumlu · 23:102
`فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ` ism-i fâil ve olumlu · 23:117
`لَا يُفْلِحُ ٱلْكَٰفِرُونَ` IMPF ve **olumsuz**. Üçünde de fâsıla belirli ism-i
fâil çoğulu. Null gerekli: bir sûrenin ilk ve son ayetlerinin ortak kök taşıması
şansa göre ne kadar seyrek? Kök sıklığı ve sûre uzunluğu kontrol edilecek.

**İKİ YENİ BÖLÜT İKİZİ.** 23:66 ↔ 23:105 (aday 492): ortak gövde beş kelime, iki
uçta ayrışıyor — **kip haberden soruya** (CERT → INTG), kapanış kökü değişiyor,
sahne dünyadan âhirete geçiyor. Taramanın "aynı gövde, kip değişimi" alt sınıfının
ilk temiz vakası. 23:109 ↔ 23:118 (aday 494): **sûre kendi içinden bir alıntıyla
kapanıyor** — aktarılan dua son ayette emre çevriliyor, nesne zamirleri düşüyor.

**ESMÂ TABLOSUNUN İKİNCİ TUTARSIZLIK VAKASI (aday 497, 484 ile aynı sınıf).**
23:86 `رَبُّ ٱلْعَرْشِ ٱلْعَظِيمِ` ve 23:116 `رَبُّ ٱلْعَرْشِ ٱلْكَرِيمِ` — aynı terkip,
aynı sözdizimsel konum, ama `كَرِيم` esmâ sayılıyor, `عَظِيم` sayılmıyor. Onarımın
ölçüt (c) maddesi bu iki vakayla sınanabilir: onarım sonrası **ikisi de düşmeli.**

**MERCEK — SÛRE ÇAPINDA SONUÇ.** 118 ayette on altı ★★★; **on beşinde iki mercek
de atlandı**, yalnız 23:86'da bir mercek (🜂 uzay) yazılabildi.
**Biyolog merceği sûre 23'te hiç yazılmadı.** Sûrenin biyolojik olarak en yoğun
ayetleri — 23:12-14 yaratılış zinciri, 23:21 davar/karın/süt, 23:78 duyular,
23:104 yüz — ya ★ almadı ya çıpasız kaldı. Adaylar 468 ve 472 için sûre çapında
kanıt; **tur sonu uzunluk-eşli null'unun ilk tam sûre veri kümesi.**

### DEVAM NOKTASI

**Sûre 24 (Nûr)** — makro profilden başla, sonra 24:1'den oku. Sûre 24 **Medenî**;
Hac'tan (22) sonra okunan ikinci Medenî sûre olacak, dolayısıyla A/R oranı
karşılaştırması için tip-eşli ikinci veri noktası (aday 470).


---

## 2026-09-01 — SÛRE 24 (NÛR) AÇILDI; MAKRO + 24:1-20

Okunan ayet **1581 → 1601** (korpusun %25,7'si). Kök tablosu **916 → 928**.
Adaylar **497 → 502** (yeni `AF_nur` kümesi). Bağlar: yeni `AD_nur` kümesi, 15 bağ.
`turkce_denetim.py` → 0 · `anahtar_denetim.py` (PYTHONHASHSEED=0) → 58 ihlâl,
taban listesiyle diff = 0 (taranan anahtar 21576).

### YENİ P1 — KORPUSUN EN UZUN SIFIR-RAB SÛRESİ (aday 498)

Sûre 24'te `رَبّ` *(Rab)* **hiç geçmiyor** (64 ayet, 1316 kelime); Allah lafzı 80 kez
(1,74x). Korpus taraması: Rab'bin sıfır olduğu 20 sûre var, ama 24 açık farkla en
büyüğü — ikincisi 48 (Fetih) 560 kelime, üçüncüsü 58 (Mücâdele) 472. Öteki
sıfır-Rab sûrelerin çoğu kısa Mekkî ve onlarda lafız da sıfıra yakın.

**TAM AYNA BULUNDU:** sûre 55 (Rahmân) — Allah 0, Rab 36 (8,08x), 78 ayet, Medenî.
İki Medenî sûre iki uçta. Aday 470 (A/R oranı) ile aynı kümede; **uzunluk-kontrollü
ve tip-eşli null gerekli.**

### ESMÂ ONARIMI İÇİN İKİNCİ YÖNLÜ KANIT (aday 501)

Sûre 24: esmâ 62 token / 36 ayet / **mühür 12** — okumada en yüksek. Ve iki taraf
temiz biçimde ayrışıyor: **mühürlü konumların hepsi çift kapanış ve geçerli**
(`غَفُور|رَحِيم` · `تَوّاب|حَكِيم` · `عَلِيم|حَكِيم` · `رَءُوف|رَحِيم` …);
**mühürsüz konumlar sistematik kirli** — `مُؤْمِن` 9 tokenin dokuzu da çoğul ve
insanlar, `آخِر` 4 tokenin hepsi âhiret, `شَهِيد` 4 tokenin hepsi tanıklar.

Sûre 23'te mühür sıfırdı ve hata %67'ye çıkmıştı. **Yedinci onarım ölçütü artık iki
yönden de kanıtlı.** Onarımda "mühürlü konum otomatik geçerli" kuralı düşünülebilir
— ama bu bir HİPOTEZ, test edilmedi; sûre 24'ün tamamı okunmadan kapatılmayacak.

### İKİ YENİ BÖLÜT İKİZİ

**Aday 499 — okumada ölçülen EN DAR ikiz.** 24:7 ↔ 24:9: dokuz kelimenin **yedisi**
birebir aynı; fark tam olarak iki kelimede (`لَعْنَت` *(lânet)* → `غَضَب` *(gazap)*,
`ٱلْكَٰذِبِينَ` → `ٱلصَّٰدِقِينَ`). Mora 43 → 46, **harf 35 = 35**. Aynı yapıda
ikinci katman: 24:6 ↔ 24:8 aynalı ve fâsılalar çaprazlanmış.

**Aday 500 — üçlü şart kalıbı ve cevapsızlık.** 24:10 · 24:14 · 24:20 aynı altı
kelimeyle açılıyor. 24:10 ve 24:20 şartın **cevabını yazmıyor**, ikisi de n=9,
ikisinde de çekimli fiil yok, ikisi de esmâ mühürlü, ikisinin de `allah z=3,92`,
ikisi de ★★★. 24:14 cevabı veriyor, n=15, iki fiilli, mühürsüz, ★ yok.
**YENİ ÖLÇÜ İHTİYACI:** `defter.json`'da "şart cevabı var/yok" alanı yok.

### DEVAM NOKTASI

**Sûre 24, ayet 21.** Uyarı: **24:31 (n=78)** okumada görülen en uzun ayet —
yıldız formülünün UZUN ayet davranışı orada ölçülecek; şimdiye dek adaylar 468 ve
472 yalnız **kısa ayet yanlılığını** belgeliyordu.


### 24:21-30 EKİ — ADAYLAR 503-506

Okunan ayet **1601 → 1611**. Kök tablosu **928 → 944**. `turkce_denetim.py` → 0
(42 ihlâl onarıldı; dokuzu sûre 9-12'den geriye dönük `برأ`). `anahtar_denetim.py`
→ 58 ihlâl, diff = 0 (taranan anahtar 21596).

**BLOK BÖLÜNDÜ.** 24:21-40 yerine 24:21-30 okundu. Gerekçe ölçüm: ikinci yarıda
üç ayet korpusun en uzunları arasında — **24:31 (n=78, okumada görülen en uzun
ayet)**, 24:33 (n=48), 24:35 (n=48), toplam 174 kelime. Bölme, okuma HIZI kararıdır;
ölçüm ve kayıt biçimi değişmedi. Gerekçe `okuma_metni.json` →
`24/_blok_bolme_notu` alanına yazıldı.

### ADAY 472 DÜZELTİLDİ (aday 503) — ÖNEMLİ

472, sûre 23 verisiyle "yıldız formülü **kısa ayete** kayıyor" diyordu (16 ★★★'ın
hepsi n=4-12). **Sûre 24 tersini veriyor:** 15 ★★★'ın kaynağı allah 6 · **n 5** ·
hapaks 4, ve n kaynaklı beşi **n=78 · 76 · 49 · 48 · 48**. Yani z-tabanlı yıldız
uzunluğu değil, **ortalamadan sapmayı** seçiyor; hangi uç görüleceği sûrenin kendi
dağılımına bağlı (23'ün ortalaması 8,90 ve en uzunu 32; 24'ünki 20,56 ve 78).

**472'nin metni bu kayıtla değiştirilmelidir.** Tur sonu uzunluk-eşli null hâlâ
gerekli ama artık "kısa yanlılığı" değil **"uç-değer seçimi"** sınanacak.
Aday 468 (mercek kapsamı) bundan etkilenmiyor — ayrı ölçü.

**DERS:** tek sûreden çıkarılan formül-davranışı iddiaları o sûrenin dağılımıyla
karışıyor. Aynı ders ikinci kez de düştü: aday 500'ün "mühür ↔ cevapsızlık"
örüntüsü dördüncü örnekte (24:21) bozuldu (aday 505). **Kalıp iddiaları, kalıbın
sûredeki TÜM geçişleri sayılmadan kaydedilmeyecek.**

### DEVAM NOKTASI

**Sûre 24, ayet 31.** Uyarı: **24:35**'te (Nûr âyeti) hem biyolog hem uzay merceği
için ilk kez gerçek çıpa var — `زَيْتُونَة` *(zeytin ağacı)* ve `كَوْكَب` *(yıldız)*.
Sûre 23'te biyolog merceği hiç yazılamamıştı; orada ölçülecek. Ayrıca 24:35'te
`نُور` *(nûr)* kökü ALTI kez ve esmâ tablosu bunların BEŞİNİ esmâ sayıyor —
aday 461 için büyük bir vaka.


### 24:31-40 EKİ — ADAYLAR 507-510

Okunan ayet **1611 → 1621**. `turkce_denetim.py` → 0 (52 ihlâl onarıldı).
`anahtar_denetim.py` → 58 ihlâl, diff = 0 (taranan anahtar 21597). Bağlar
`AD_nur` 26 → 36.

### BİYOLOG MERCEĞİ SONUNDA YAZILDI — 24:35

Sûre 23 boyunca (118 ayet, on altı ★★★) biyolog merceği **hiç** yazılamamıştı.
24:35'te ilk kez çıpa bulundu: `شَجَرَةٍ مُّبَٰرَكَةٍ زَيْتُونَةٍ` *(bereketli bir zeytin
ağacı)*. **Ölçülen:** sûrede adı verilen tek bitki türü; tür konumla değil
**konumun reddiyle** niteleniyor (`لَّا شَرْقِيَّةٍ وَلَا غَرْبِيَّةٍ`), yani seçilen
değişken toprak/su/meyve değil **ışık maruziyeti**; ve yüklemin öznesi ağaç değil
ürünü. **Sınır açıkça yazıldı:** ayet bileşim, büyüme ya da mekanizma hakkında
hiçbir şey söylemiyor; bitki fizyolojisi çıkarılmadı.

Aynı ayette uzay merceği de yazıldı: `كَوْكَبٌ دُرِّىٌّ` *(inci gibi parlayan yıldız)*
— yıldız **parlaklık** için çağrılıyor, konum ya da hareket için değil; yön ekseni
(`شرق`/`غرب`) var ama **iki ucu birden reddediliyor**. Yörünge, ölçü, sayı ya da
hareket terimi yok; gök modeli kurulmadı.

### YENİ P0 VAKASI — 24:35'TE ESMÂ `نُور` BEŞ KEZ SAYILIYOR (aday 508)

Sûre 24'te esmâ `نُور` toplam 7 token ve **tamamı iki ayette**: 24:35'te beş,
24:40'ta iki. Bağlam denetimi: yalnız `ٱللَّهُ نُورُ ٱلسَّمَٰوَٰتِ` geçerli; kalan altısı
iyelikli tamlama (×3) ya da **nekre** (×3) — ölçüt (b) ikisini de dışlıyor.
**Tek ayette ölçülen en yoğun esmâ hatası (5/48 kelime).** Onarım sonrası
24:35'te bir, 24:40'ta sıfır esmâ kalmalı. İki ayet de **mühürsüz** — aday 501'in
"mühürsüz konumlar kirli" ölçümüyle birebir uyumlu.

### YENİ P1 — KAFİYE KIRILMASI TEK BİTİŞİK KUŞAKTA (aday 509)

Sûre 24'ün dört kafiye sınıfı rastgele dağılmıyor: N dışına çıkan **on ayet
ardışık** — 24:36 (ل, sûrenin tek ل'si) · 37 (R) · 38 (ب) · 39 (ب) · 40 (R) ·
41 (N ama **kırık** işaretli) · 42-45 (R ×4); 24:46'da N'ye dönülüyor. Kuşak tam
olarak **Nûr âyetinin ardından** açılıyor. Permütasyon null gerekli: fâsıla
sınıflarını sûre içinde karıştır, en uzun bitişik azınlık kuşağını ölç.
**24:41-45 henüz okunmadı — kapatılmayacak.**

### ADAY 503 İÇİN DOĞRUDAN VERİ

Bu bloğun dört ★★★'ından **üçü uzunluk kaynaklı**: 24:31 (n=78, z=6,96) ·
24:33 (n=48, z=3,78) · 24:35 (n=48, z=3,78); dördüncüsü 24:32 hapaks kaynaklı.
472'nin "kısa ayet yanlılığı" iddiası bu blokla bir kez daha düşüyor.

### DEVAM NOKTASI

**Sûre 24, ayet 41.** Kafiye kuşağı sürüyor; 24:41 kafiye kırık işaretli.


### 24:41-45 EKİ — ADAYLAR 511-513

Okunan ayet **1621 → 1626**. Kök tablosu **944 → 951**. `turkce_denetim.py` → 0
(14 ihlâl). `anahtar_denetim.py` → 58 ihlâl, diff = 0 (taranan anahtar 21604).
Bağlar `AD_nur` 36 → 43. **İkinci blok bölmesi:** 24:41-55 yerine 24:41-45;
gerekçe `okuma_metni.json` → `24/_blok_bolme_notu` alanında.

### ADAY 468 İÇİN EN TEMİZ VAKA (aday 512)

Mercek eşiği ★★★. Sûre 24'te uzman merceği için gerçek çıpa taşıyan **üç** ayet var:

| ayet | alan | yıldız | mercek |
|---|---|---|---|
| 24:35 | zeytin ağacı + yıldız | ★★★ | **yazıldı** |
| 24:43 | meteoroloji (`سحب`·`ودق`·`برد`·`برق`) | ★★ | **eşik tutmuyor** |
| 24:45 | biyoloji (`دبب`·`موه`·`مشي`×3·`بطن`·`رجل`) | ★ | **eşik tutmuyor** |

Sûrenin **biyolojik olarak en yoğun ayeti ★ alıyor**; meteorolojik olarak en yoğun
ayeti ★★. Buna karşılık ★★★ alan on beş ayetin **on dördünde çıpa yok**. Çıpa ile
yıldız birbirinden bağımsız ölçüler ve sûre 24'te **ters yönde ayrışıyorlar**.

**TUR SONU İŞİ — ÖNCE ÇIPA TANIMI YAZILMALI.** Şu an "çıpa" okuma sırasında elle
veriliyor ve ölçülebilir bir ölçütü yok. Korpus çapında karşılaştırma ancak
tanım yazıldıktan sonra yapılabilir.

### DEVAM NOKTASI

**Sûre 24, ayet 46.** Kafiye kuşağı (aday 509) 24:46'da kapanıyor — N sınıfına
dönüş orada doğrulanacak. Sûrede 19 ayet kaldı.


---

## 2026-09-03 — SÛRE 24, 24:46-52

Okunan ayet **1626 → 1633**. Kök tablosu **951 → 959**. `turkce_denetim.py` → 0
(9 ihlâl; üçü sûre 9'dan geriye dönük `قعد`/`حذر`). `anahtar_denetim.py` → 58 ihlâl,
diff = 0 (taranan anahtar 21613). Adaylar **513 → 515**; bağlar `AD_nur` 43 → 50.

**Kafiye kuşağı kapanışı DOĞRULANDI (aday 509):** 24:46 م fâsılası, N sınıfı;
24:36-45 on ayetlik kuşak kapandı. Ve kuşak iki ucundan aynı formülle çevreleniyor —
24:34 ve 24:46 `أَنزَلْنَآ ءَايَٰتٍ مُّبَيِّنَٰتٍ` (aday 507 dördüncü geçiş).

**Aynalı çağrı kalıbı (aday 514):** 24:48 ↔ 24:51 sekiz kelime birebir, sonuç ters
(`مُّعْرِضُونَ` / `سَمِعْنَا وَأَطَعْنَا`). Arada ardışık iki hapaks (24:49 `ذعن`,
24:50 `حيف`), ikisi de z=3,38 ★★★. 24:50'deki iki `أَمْ` muttasıla ve ayet INTG
alıyor — **aday 438'in karşı kontrolü**: muttasıla doğru işleniyor, yalnız munkatı'a
kaçırılıyor.

**Kurtuluş çifti iki sûrede (aday 515):** 23:102/23:111 ↔ 24:51/24:52 aynı iki
fâsıla (`ٱلْمُفْلِحُونَ` → `ٱلْفَآئِزُونَ`), aynı sıra, ara 9 → 0.

### DEVAM NOKTASI

**Sûre 24, ayet 53.** Sûrede 12 ayet kaldı. 24:53 sûrenin tek QASEM'i; 24:55
(n=38) sûrenin uzun ayetlerinden; 24:58 ve 24:61 ★★★ ve n kaynaklı (aday 503 verisi).


### 24:53-60 EKİ — ADAYLAR 516-520

Okunan ayet **1633 → 1641**. `turkce_denetim.py` → 0 (20 ihlâl). `anahtar_denetim.py`
→ 58 ihlâl, diff = 0. Bağlar `AD_nur` 50 → 60.

**YENİ ARAÇ SORUSU — İLTİFÂT TAGGER'I LAFIZ→ZAMİR GEÇİŞİNİ KAÇIRIYOR OLABİLİR
(aday 517, P1).** 24:55'te lafız 3MS ile açılıyor, üç te'kid nûnlu fiil 3MS'de
sürüyor, sonra ayet ortasında `يَعْبُدُونَنِى … بِى` ile 1S'e geçiyor — aynı özne.
Ölçüm `ilt=0`. Sûre 23'te sayılan yedi iltifâtın hepsi zamir→zamir'di. **Eğer
tagger lafız→zamir geçişini işlemiyorsa, sûre 24'ün "iltifât sıfır" ölçümü ve
23↔24 karşılaştırması (7 → 0, aday 502) GEÇERSİZ.** Tur sonu onarım kalemi; 462
ile aynı sırada ele alınacak. Sûre 24'ün iltifât ölçümüne dayanan hiçbir bulgu
onarım öncesi kapatılmayacak.

**Sûre 24 mühür sayımı tamamlandı (aday 501):** on iki mühürün on ikincisi 24:60'ta
(`سَمِيع|عَلِيم`). `عَلِيم|حَكِيم` üç kez (24:18, 58, 59), ikisi ardışık (aday 519).

**Aday 509 ekleme (aday 518):** kuşak dışındaki tek R ayeti (24:57) kuşağın
24:42'siyle aynı fâsıla kelimesini taşıyor (`ٱلْمَصِيرُ`) — kuşağın yankısı.

### DEVAM NOKTASI

**Sûre 24, ayet 61.** Dört ayet kaldı: 24:61 (n=76, `بيت` ×10, ★★★ n kaynaklı) ·
24:62 (n=39, `أذن` ×4) · 24:63 (hapaks `لوذ`, ★★★) · 24:64 (kapanış).


### 24:61-64 — SÛRE 24 TAM (64/64), ADAYLAR 521-524

Okunan ayet **1641 → 1645** (korpusun %26,4'ü). Tam okunan sûreler: **1, 9-24**.
`turkce_denetim.py` → 0 (24 ihlâl). `anahtar_denetim.py` → 58 ihlâl, diff = 0
(taranan anahtar 21614). Bağlar `AD_nur` 60 → 65.

**SÛRENİN HALKASI (aday 524):** 24:42 ↔ 24:64. Ortak terkip
`لِلَّهِ` + `ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ`; nesne `مُلْك` *(mülk, sahiplik)* →
`مَا فِى` *(içindekiler, kapsam)*. **NOT — YENİ ALT SINIF:** sûre 24'ün halkası
AÇILIŞTAN değil **ortadan** (24:42) kapanışa; sûre 23'ünki açılıştan (23:1)
kapanışa (aday 491). İki halka türü ayrı kodlanmalı.

**İKİ KÖK DORUĞU:** `بيت` *(ev)* 24:61'de **tek ayette on kez** (sûredeki 14
geçişin onu) — dokuz akrabalık evi + iki akraba olmayan öğe (aday 521).
`أذن` *(izin)* 24:62'de dört kez, dördü de bab X; sûrede 14 geçiş dört bölümde
ve ilerleme ölçüldü: mekâna giriş → mekânın kendisi → ev içi vakit → topluluktan
ayrılma (aday 522). **Tek ayette kök tekrarı rekoru KORPUS TARAMASI YAPILMADI** —
tur sonu, `defter.json` `ikile` alanından.

**SÛRE 24 MERCEK BİLANÇOSU:** 64 ayet, on beş ★★★, **on dördünde iki mercek de
atlandı**; yalnız 24:35'te ikisi de yazıldı. Sûrenin çıpa taşıyan öteki iki ayeti
(24:43 meteoroloji ★★, 24:45 biyoloji ★) eşiğin **altında** kaldı (aday 512).

### DEVAM NOKTASI

**Sûre 25 (Furkān)** — makro profilden başla, sonra 25:1'den oku. Sûre 25 Mekkî;
sûre 23'ten (Mekkî) sonra okunan ikinci Mekkî, 24 (Medenî) arada — A/R eksen
karşılaştırması (adaylar 470, 498) için üçüncü veri noktası.


---

## 2026-09-04 — SÛRE 25 (FURKĀN) AÇILDI; MAKRO + 25:1-10

Okunan ayet **1645 → 1655** (korpusun %26,5'i). Tam okunan sûreler: 1, 9-24.
Kısmi: 2 (1-20), **25 (1-10)**. Adaylar **524 → 537** (yeni `AG_furkan` kümesi,
13 aday). Bağlar: yeni `AE_furkan` kümesi, 10 bağ. Kök tablosu 959'da sabit —
YENİ KÖK EKLENMEDİ; iki karşılık GENİŞLETİLDİ (`ملو`, `سوق`; aday 537).
`turkce_denetim.py` → **0** (18 ihlâl onarıldı, hepsi xref 3-gram'ları içindeki
karşılıksız anmalardan). `anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl,
taban listesiyle diff = 0** (taranan anahtar 21614 → 21619).

### A/R EKSENİNİN ÜÇÜNCÜ VERİ NOKTASI (aday 525; 470, 498 kümesi)

| sûre | tip | kelime | A | R | A kat | R kat | A/R |
|---|---|---|---|---|---|---|---|
| 23 | Mekkî | 1050 | 13 | 23 | 0,36 | 1,73 | **0,57** |
| 24 | Medenî | 1316 | 80 | 0 | 1,74 | 0,00 | ∞ |
| 25 | Mekkî | 893 | 8 | 14 | 0,26 | 1,24 | **0,57** |

İki Mekkî sûre aynı iki haneli oranı veriyor. Korpus taraması: kelime ≥500 olan
45 sûre içinde Allah yoğunluğu en düşük **14 sûrenin on dördü de Mekkî**.
Neredeyse tam ikiz: sûre 34 (883 kelime, A=8, R=14). **Tip alanının kaynağı
tur sonunda doğrulanacak** — `nuzul.json` güvenilmez, `tip` alanı ayrı denetlenmeli.

### YENİ P1 — FÂSILA İ'RÂBI TEK YÖNLÜ (aday 526)

Sûre 25'in **77 fâsıla kelimesinin 77'si de ACC**. Karşılaştırma: 23 → NOM 36 ·
GEN 27 · ACC 9; 24 → NOM 36 · GEN 15 · ACC 2. Sûrenin i'râb profili ACC 229 ·
GEN 98 · NOM 57; **ACC payı 0,596 ile korpus birincisi** (i'râb tokeni ≥200 olan
49 sûre). **KONTROL KOŞULDU:** fâsıla kelimesi çıkarılınca pay 0,495'e düşüyor
ama sûre **hâlâ birinci** (45 sûre; ikinci 19 Meryem 0,448). ACC baskınlığı
yalnız kafiyeden gelmiyor. Karıştırıcı not: sûrede emir 13 ve soru 9 var.

### YENİ P0 — 25:9 = 17:48 TAM AYET ÖZDEŞ AMA `esit` ALANI BOŞ (aday 530)

25:9 ile 17:48 arasındaki **tek fark imlâ**: `ٱلْأَمْثَٰلَ` / `ٱلْأَمْثَالَ`.
`defter.json` `esit` alanı bunu yakalamıyor ve **sûre 25'in tamamında `esit`
boş**. Buna karşılık xref katmanı yakalıyor: 25:9'dan **beş** 3-gram 17:48'e,
25:8'den **üç** 3-gram 17:47'ye. Yani 25:8-9 ↔ 17:47-48 **ardışık bölüt ikizi**.
**TUR SONU İŞİ:** `esit` taraması harekesiz ve elif-varyantı normalize edilmiş
biçimde tekrarlanacak — imlâ farkı yüzünden kaçırılan kaç tam-ayet ikizi var?
496/500/507/522 kümesine ek. **Bölüt ikizi taramasında farklılaşan öğe
sınıflarına KİP eklenecek** (bağlaç 476'da eklenmişti).

### 452/474 KÜMESİNE ÜÇ YENİ VAKA (aday 529)

Dikey katman kök düzeyinde çalışıyor: (a) 25:1 `عالَم` *(âlem)* → `علم` kökünün
"bilme" komşuluğu; (b) **25:3 `ءَالِهَة` *(ilâhlar)* → `أله` kökünün n=2851'lik
lafız komşuluğu — okumada görülen en büyük ölçekli vaka**; (c) 25:13 `مُقَرَّن`
*(bağlanmış)* → `قرن` kökünün "nesil" komşuluğu. **Kavram katmanı (b) ve (c)'yi
DOĞRU çözüyor**; ayrışan yalnız `dikey_oku.py`'nin kök düzeyi girdisi. Onarım
ölçütü önerisi: bir kökün korpus geçişlerinin %90'ından fazlası tek lemmaya
aitse, azınlık lemma için kök düzeyi komşuluk YANILTICI sayılacak.

### KARŞILIK TABLOSU — SÛRE 25 BEŞ VAKA VERDİ (aday 537, 480 sınıfı)

`ملو` *(→ yazdırma (imlâ))* ve `سوق` *(→ çarşı (sûk))* bu blokta genişletildi.
İkinci blokta genişletilecek: `قرن` *(→ birbirine bağlama)* · `بغي` *(→ yakışma,
uygun olma)* · `كون` *(→ mekân)*. Sûre 23 tek vaka vermişti (`سمر`); **sûre 25
tek başına beş.** 480'in tur sonu işine doğrudan veri.

### KAPATILAMAZ OLARAK AÇILAN ÜÇ ADAY

- **527** — açılış on beş ayette lafız ve Rab sıfır, gönderge `ٱلَّذِى` *(o ki)*.
  Sûrede tekil eril `ٱلَّذِى` 13 ayette; göndergeler denetlenmedi. **Kalıp iddiası
  kuralı:** tam sayım yapılmadan kaydedilmeyecek. Uyarı: 25 zaten düşük-A bir
  sûre (0,26x), açılışın sıfır olması taban oranın sonucu olabilir — null ayırmalı.
- **533** — `قول` *(söz söyleme)* zinciri (25:4, 5, 7, 8 itiraz; 25:6 cevap ve o da
  `قُلْ` *(de ki)*). Sûrede kök 22 geçişli, yalnız onu okundu. Ayrıca `قول`
  korpusun en sık ikinci kökü (n=1722) — yoğunluk iddiası taban oransız kurulamaz.
- **535** — 25:7 ↔ 25:20 bölüt ikizi. 25:20 henüz okunmadı. Ön-kayıt yazıldı:
  farklılaşan öğeler şahıs · te'kid · biçim · kapsam.

### MERCEK

**Blokta ★★★ ayet YOK** — en yüksek 25:5'te ★ ve tek kaynağı tek bir edilgen fiil
(`pas z=1,57`). İki uzman merceği protokol gereği yazılmadı. Adaylar 468/512 için
veri: bu blokta **yıldız ile çıpa aynı yönde — ikisi de yok**; sûre 24'te ters
yönde ayrışmışlardı.

### DEVAM NOKTASI

**Sûre 25, ayet 11.** Blok 25:11-20. 25:11 `بَلْ` ile açılıyor ve IDRAB alıyor —
sahne âhirete geçiyor. Beklenenler: 25:13-14'te `ثبر` *(helâk, sabûr)* kökünün
korpustaki beş geçişinin üçü (aday 531); 25:14 sûrenin ilk iltifâtı (3>2);
25:16'da ilk `رَبّ` *(Rab)*; **25:17'de ilk Allah lafzı VE sûrenin tek kafiye
kırılması** (`ل` fâsılası, sûrenin tek ل'si) — ikisinin aynı ayete düşmesi
ölçülecek, ama sûrede lafızlı altı ayetin ötekilerinin hepsi A sınıfı, dolayısıyla
**kalıp iddiası kurulmayacak**; 25:20 ile aday 535'in kapanışı.


### 25:11-20 EKİ — SÛRE 25 20/77, ADAYLAR 538-546

Okunan ayet **1655 → 1665** (korpusun %26,7'si). `turkce_denetim.py` → **0**
(1 ihlâl). `anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl, diff = 0**
(taranan anahtar 21619). Bağlar `AE_furkan` 10 → 21. Kök tablosu 959'da sabit;
üç karşılık daha genişletildi (`قرن` · `بغي` · `كون`; aday 537 tamamlandı).
UYARI: `كون` karşılığı "olmak" → "olmak; mekân, yer" oldu; eski sûrelerdeki
yüzlerce `كون *(olmak)*` anması denetimden geçmeye devam ediyor (denetim yazılan
karşılığı tabloyla KARŞILAŞTIRMIYOR), ama tur sonu tutarlılık işine yazıldı.

**BİRİNCİ ŞAHIS TAM 25:11'DE BAŞLIYOR (aday 538).** 25:1-10'da 1P ve 1S sıfır;
25:11 `أَعْتَدْنَا` *(hazırladık)* ile ilk 1P'yi, 25:17 `عِبَادِى` *(kullarım)* ile
ilk 1S'yi getiriyor. Sûrede birinci şahıs taşıyan 31 ayetin **30'u 25:11'den
sonra**. Kırılma noktası bloğun bölme çizgisiyle çakışıyor — ama bölme kararı bu
ölçümden ÖNCE ve başka gerekçeyle (`تَبَارَكَ` halkası + hacim) verildi; **post hoc
doğrulama olarak yazıldı, ön-kayıt değil**.

**ADAY 535 KAPANDI — ÖN-KAYIT TUTTU (aday 545).** 25:7 ↔ 25:20; dört farklılaşan
öğenin dördü de doğrulandı (şahıs · te'kid · biçim · kapsam). 456→476'da ön-kayıt
düşmüştü; bu kez bağlaç ve kip düzeyinde yazıldığı için tuttu. **Bölüt ikizi
taramasının 'itiraz → cevap' alt sınıfının referans vakası.**

**ADAY 438'İN İKİ KARŞI KONTROLÜ DAHA.** 25:15 ve 25:17'de `أَمْ` *(yoksa)* ayet
İÇİNDE (muttasıla) ve **iki ayet de INTG alıyor** — muttasıla doğru işleniyor.
Munkatı'a vakası bu blokta yok. 23:69/70/72 sınama kümesine ek karşı kontrol.

**ESMÂ — BLOKTA ÜÇ TOKEN, MÜHÜR SIFIR, YANLIŞ POZİTİF 2/3 (aday 546).**
25:18 `وَلِيّ` *(velî)* çoğul → artefakt · 25:19 `كَبِير` *(büyük)* nekre, gönderge
`عَذَاب` *(azap)* → artefakt · 25:20 `بَصِير` *(gören)* `رَبّ` *(Rab)*'bin doğrudan
yüklemi → geçerli. **UYARI: payda 3; sûre 23'ün %67'siyle sayısal karşılaştırma
YAPILMAYACAK.** Beklenen büyük vaka `رَحْمٰن` *(rahmân)* 5 token — esmâ mı özel ad mı
sorusu özel isim katmanıyla çakışıyor, sûre sonunda.

**529'A DÖRDÜNCÜ VAKA.** 25:19 `صرف` *(çevirme, türlü türlü açıklama)*: dikey
komşuluk ▸sonra Kur'ân ×17,6 veriyor (kök korpusta ağırlıkla "âyetleri türlü
türlü açıklama"), ayette ise "azabı çevirme". Kök düzeyi komşuluk ayrımı yapmıyor.

### MERCEK — ARA BİLANÇO (20/77)

Blokta ★★★ yok; en yüksek 25:13'te ★★ (`pas z=2,52`, tek kaynak). **Sûre 25'in ilk
yirmi ayetinde: ★★★ sıfır · ★★ bir · ★ dört · çıpa sıfır.** 25:12'nin `غَيْظ`
*(öfke, gayz)* + `زَفِير` *(uğultu, derin soluk)* terkibi çıpa sayılmadı — solunum
ya da ses fiziği okuması yasaklı "bilimsel izdüşüm" olurdu; özne ateş, gönderge
azap sahnesi. **Adaylar 468/512 için: yıldız ile çıpa hâlâ aynı yönde (ikisi de yok).**

### DEVAM NOKTASI

**Sûre 25, ayet 21.** Blok 25:21-40. Beklenenler: 25:21'de `رَبّ` *(Rab)* ve 1P ×4 ·
25:24 ilk adlı aktör `جَنَّة` *(cennet, bahçe)* · 25:26 ilk `رَحْمٰن` *(rahmân)*
(aday 546'nın büyük vakası açılıyor) · **25:28 ★★★ ve hapaks `فلن` *(falan, filan
kimse)*** · 25:30 `قُرْءان` *(Kur'ân)* aktör olarak · **25:33 ★★★ ve hapaks `فسر`
*(açıklama, tefsir)*** · **25:34 ★★★** · 25:35 `مُوسَى` *(Mûsâ)* ve `هارُون`
*(Hârûn)* · 25:37 `نُوح` *(Nûh)* · 25:38 `عاد` *(Âd)* ve `ثَمُود` *(Semûd)* —
sûrenin kıssa yoğunluğu bu blokta başlıyor.


### 25:21-30 EKİ — SÛRE 25 30/77, ADAYLAR 547-554

Okunan ayet **1665 → 1675** (korpusun %26,9'u). `turkce_denetim.py` → **0**
(1 ihlâl: `عتو`). `anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl, diff = 0**
(taranan anahtar 21630). Bağlar `AE_furkan` 21 → **31**.

**KÖK TABLOSU 959 → 970 — ON BİR YENİ KÖK.** `جمل` · `حجر` · `رتل` · `رسس` ·
`عضض` · `فسر` · `فلن` · `قيل` · `مطر` · `نثر` · `هبو`. Anahtarlar
`kok_envanteri.json`'dan NFC eşlemesiyle kopyalandı. **Geriye dönük ihlâl açığa
ÇIKMADI** — sûre 23 turunun desenine aykırı (orada 14:22 `لوم`, 9:6 `جور`,
9-12'de dokuz `برأ` açığa çıkmıştı). Açıklama hipotezi (test edilmedi): eklenen
on bir kökün sekizi korpusta ≤4 geçişli; seyrek kökler önceki sûrelerde
geçmediği için geriye dönük ihlâl üretmiyor (aday 554).

### YENİ P0 — ADAY 512'NİN EN TEMİZ VAKASI (aday 553)

**Sûrenin ilk ★★★ ayeti 25:28 ve çıpası SIFIR.** Altı kelime, tamamen
kişilerarası temenni; yıldızın tek kaynağı `hapaks z=3,38` (`فلن` *(falan, filan
kimse)*, korpusta tek geçiş). **Buna karşılık 25:25** — `وَيَوْمَ تَشَقَّقُ
ٱلسَّمَآءُ بِٱلْغَمَٰمِ` *(o gün gök bulutlarla yarılır)* — gerçek bir gök öğesi
taşıyor ve yalnız ★★ alıyor. Yani **sûre 25'in ilk otuz ayetinde çıpalı ayet ★★,
çıpasız ayet ★★★ alıyor.** Sûre 24'te ayrışma TERS yöndeydi (24:45 en yoğun
biyolojik ayet ★ alıyordu). **İki sûre, iki yön** — yıldız formülü ile çıpa
arasında sistematik ilişki yok gibi görünüyor, ama bu ancak **çıpa tanımı
yazıldıktan sonra** null sonuç olarak kaydedilebilir. Mercek atlama gerekçeleri
`25/_mercek_atlama_notu` → `_mercek_25_28` ve `_mercek_25_25`.

### YENİ P0 — ADAY 546'NIN BÜYÜK VAKASI AÇILDI (aday 549)

25:26'da sûrenin ilk `رَحْمٰن` *(rahmân)*'ı ve **sözdizimsel kanıt özel ad
yönünde**: marife, `لِ` ile mecrur, mülkün sahibi konumunda, yüklem değil.
`ٱلْمُلْكُ يَوْمَئِذٍ ٱلْحَقُّ لِلرَّحْمَٰنِ` *(o gün gerçek mülk Rahmân'ındır)*.
25:2'de aynı kök (`ملك`) göndergesiz `ٱلَّذِى` *(o ki)*'ye aitti — mülkün sahibi
**adlandırılıyor ama Allah lafzıyla değil**. **Bu ayrım çözülmeden sûrenin
"esmâ 22 token" sayımı kullanılamaz.** `bulgu_ozel_isim_katmani.json` ile
çakışma denetlenmedi.

### ESMÂ YANLIŞ POZİTİFLERİ — AYNI SINIFTAN ÜÇÜNCÜ VAKA

25:21 `كَبِير` *(büyük)*: nekre, gönderge `عُتُوّ` *(taşkınlık, azgınlık)*.
25:19 `كَبِير` ve 25:18 `وَلِيّ` ile birlikte **üç ardışık yanlış pozitif, üçü de
mühürsüz, üçü de ölçüt (b) ile dışlanıyor**. Aday 546'nın kaydına eklendi.

### YENİ ÖLÇÜ TANIMI EKSİKLERİ (496 kümesi)

- **Fiilsiz ayet alanı yok** (aday 548). 25:24 okunan ayetler içinde fiilsiz tek
  ayet; `vf` sözlüğünün boş olmasından çıkarıldı, doğrudan alan yok.
- **Çatı (geçişli/geçişsiz) alanı yok** (aday 552). `vf` yalnız bab veriyor.
  25:17 çatı sorusunu soruyor, 25:18 ve 25:29 iki farklı cevap veriyor — okumada
  ilk kez görülen "soru → iki cevap" alt sınıfı.

### DÖRDÜNCÜ BLOK BÖLME

**25:21-40 de ikiye bölündü (25:21-30 / 25:31-40).** Gerekçe `_blok_bolme_notu`'na
yazıldı: 25:30 elçinin şikâyetiyle bölütü kapatıyor, 25:31 `وَكَذَٰلِكَ جَعَلْنَا
لِكُلِّ نَبِىٍّ عَدُوًّۭا` ile yeni hareket açıyor; ayrıca 25:21-30 sûrenin ilk
★★★ ayetini ve iki ★★ ayetini birlikte taşıyor, mercek kaydı bölünmesin diye
ayrı tutuldu.

### DEVAM NOKTASI

**Sûre 25, ayet 31.** Blok 25:31-40. Beklenenler: 25:32'de `رتل` *(ağır ağır ve
tane tane okuma (tertîl))* — korpusta dört geçişli, ikisi burada, ikisi 73:4 ·
**25:33 ★★★ ve hapaks `فسر` *(açıklama, tefsir)*** · **25:34 ★★★** · 25:35
`مُوسَى` *(Mûsâ)* ve `هارُون` *(Hârûn)* · 25:37 `نُوح` *(Nûh)* · 25:38 `عاد`
*(Âd)*, `ثَمُود` *(Semûd)* ve `رسس` *(Ress)* · 25:40 `مطر` *(yağmur; yağdırma)*.
Sûrenin kıssa yoğunluğu bu blokta.


### 25:31-40 EKİ — SÛRE 25 40/77, ADAYLAR 555-561

Okunan ayet **1675 → 1685** (korpusun %27,0'ı). `turkce_denetim.py` → **0**
(2 ihlâl: `عدو` — şeddeli yazımda `عدوّ` karşılık hemen ardından gelmiyordu;
`رتل` — üçüncü anma karşılıksızdı). `anahtar_denetim.py` (PYTHONHASHSEED=0) →
**58 ihlâl, diff = 0** (21630). Bağlar `AE_furkan` 31 → **43**. Kök tablosu
970'te sabit.

**BİÇİM UYARISI (yeni desen):** şeddeli/eklemeli yazımlar (`عدوّ`, `نبيّ`)
denetimi tetikleyebiliyor çünkü doğrulayıcı kök dizgisinden hemen sonra karşılık
arıyor. Çözüm: xref 3-gram'larında kökü şeddesiz yazıp karşılığı hemen vermek.
Bu, 25:1-10'daki xref ihlâl desenine ek bir alt sınıf.

### ADAY 553 GÜÇLENDİ VE 561'E YÜKSELDİ — ÜÇ ★★★, ÜÇÜNDE DE ÇIPA SIFIR

| ayet | yıldız | tek kaynak | çıpa |
|---|---|---|---|
| 25:28 | ★★★ | hapaks `فلن` z=3,38 | **yok** |
| 25:33 | ★★★ | hapaks `فسر` z=3,38 | **yok** |
| 25:34 | ★★★ | `pas` z=5,38 | **yok** |
| 25:25 | ★★ | `pas` z=2,52 | gök yarılması + bulut |
| 25:40 | — | — | yağış olayı |

Üç ★★★ ayetin yıldız kaynağı **ikisi hapaks, biri edilgenlik oranı — üçü de
sözlük/biçim istatistiği, hiçbiri içerik**. `pas` z'nin edilgen SAYISINI değil
ORANINI ölçtüğü doğrulandı: 25:34'ün tek fiili edilgen, oran 1,00, z=5,38.

**ÇIPA TANIMI İÇİN ÖLÇÜT ÖNERİSİ (aday 561'e yazıldı):** beden/gök/doğa öğesinin
*anılması* çıpa değildir; çıpa için ayetin o öğe hakkında **ölçülebilir bir şey**
(mekanizma, ölçü, süreç, sınıflandırma) söylemesi gerekir. Bu ölçütle 25:34
çıpasız (`وُجُوه` hâl bildirimi), 25:40 çıpasız (yağmur bir helâk adı), 25:25
**sınırda** — olay var, ölçü yok; belki bir ara sınıf gerekli. 24:45 (canlı
sınıfları) bu ölçütle çıpalı kalır.

### YENİ P0 — ESMÂ ÖLÇÜT ÇATIŞMASININ EN TEMİZ VAKASI (aday 555)

25:31: `كَفَىٰ بِرَبِّكَ هَادِيًۭا وَنَصِيرًۭا`. **İki temyiz, aynı ayette, aynı
sözdizimsel konumda, ikisi de nekre mansûb, ikisi de `رَبّ`'bin niteliği — tablo
yalnız ikincisini esmâ sayıyor.** Aralarındaki tek fark konum: `نَصِير` fâsıla
(11/11), `هَادِى` değil (10/11). **Tablo sözdizimsel ölçütü değil KONUMU
kullanıyor gibi görünüyor.** Doğruysa bütün esmâ sayımları fâsıla-yanlı demektir
ve sûre 25'in "22 token" sayımı bu yanlılığı taşır. 23:86 ↔ 23:116 vakasından
daha temiz: orada iki ayrı ayet vardı, burada aynı ayette aynı konumda.

### MM ETİKETLEME İŞİNİN DOĞRUDAN GEREKÇESİ (aday 559)

Blokta fiil + mef'ûl-i mutlak **üç kez ve üçü de bab II · 1P · fâsıla**:
`رَتَّلْنَٰهُ تَرْتِيلًۭا` · `دَمَّرْنَٰهُمْ تَدْمِيرًۭا` · `تَبَّرْنَا تَتْبِيرًۭا`.
Sûrede ayrıca 25:2, 25:21, 25:25 ve iki farklı alt sınıf (25:23 iç mef'ûl, 25:22
isim + ism-i mef'ûl). **`defter.json`'da MM alanı yok, hepsi elle sayıldı.**
UYARI: sûrenin ACC baskınlığı (aday 526) ile MM yoğunluğu **karışıyor olabilir** —
mef'ûl-i mutlak zorunlu olarak mansûb ve fâsıla konumunda.

### İKİNCİ FİİLSİZ AYET (aday 548'e ek)

25:38 `وَعَادًۭا وَثَمُودَا۟ وَأَصْحَٰبَ ٱلرَّسِّ وَقُرُونًۢا بَيْنَ ذَٰلِكَ كَثِيرًۭا`
— hiç fiil yok, sekiz kelimenin beşi mansûb, hepsi önceki ayetin fiiline
bağlanıyor. **Ayrıca aktör tablosu tutarsız:** `عاد` *(Âd)* ve `ثَمُود` *(Semûd)*
tabloya giriyor, `أَصْحَٰبَ ٱلرَّسِّ` *(Ress ashabı)* girmiyor (aday 462).

### DEVAM NOKTASI

**Sûre 25, ayet 41.** Blok 25:41-60. Beklenenler: **25:41'de Allah lafzı**
(sûrenin ikincisi) · 25:45-50 sûrenin en yoğun doğa bölütü (gölge, gece, uyku,
rüzgâr, su, ölü belde) — **çıpa tanımı için sınama alanı** · 25:53 iki deniz ·
25:55 Allah lafzı · 25:56 iltifât (3>12) · 25:59 `رَحْمٰن` ikinci geçiş ·
25:60'ta `رَحْمٰن` üçüncü ve adsız aktör `nefer`. Aday 549'un (esmâ mı özel ad mı)
asıl veri kütlesi bu blokta.


### 25:41-50 EKİ — SÛRE 25 50/77, ADAYLAR 562-570

Okunan ayet **1685 → 1695** (korpusun %27,2'si). `turkce_denetim.py` → **0**
(10 ihlâl, hepsi aynı sınıftan: kök adının Türkçe cümle içinde karşılıksız
anılması — `أله üçlüsü`, `حيي/موت çifti` gibi). `anahtar_denetim.py`
(PYTHONHASHSEED=0) → **58 ihlâl, diff = 0** (21637). Bağlar 43 → **56**.
**Kök tablosu 970 → 977** (yedi yeni kök: `أجج` · `ذنب` · `سبت` · `فرت` · `مرج` ·
`ملح` · `نوب`).

## ★ ADAY 561'İN EN KESKİN VAKASI — ON AYET, SIFIR YILDIZ, EN YOĞUN DOĞA BÖLÜTÜ

**25:41-50'de ★★★ 0 · ★★ 0 · ★ 0** — okumada görülen en uzun yıldızsız dizi.
Buna karşılık bu blok sûrenin **çıpa bakımından en zengin** on ayeti:

- **25:45-46** gölgenin uzatılması → gerçekleşmemiş alternatif (`سَاكِنًۭا`
  *(durgun)*) → güneşin **gösterge** kılınması → gölgenin kademeli çekilmesi.
  İki `ثُمَّ` ile ayrılmış dört aşama, bir gösterge ilişkisi. **Yıldız sıfır.**
- **25:47** gece / uyku / gündüz üçlüsü, üçü de mansûb sıfatla.
- **25:48** rüzgârların yağıştan **önce** gönderilmesi — sıralama ilişkisi.
- **25:49** suyun ölü beldeyi diriltmesi; davar ve insan **ayrı ayrı** sayılıyor.

**Protokol gereği 🜁 ve 🜂 yazılamadı** — eşik ★★★, blokta ★ bile yok. **Kural
çiğnenmedi.** Ama kaydedildi: sûrenin çıpa bakımından en zengin on ayeti, yıldız
formülü tarafından tamamen görünmez kılınıyor. Blokta hiçbir z eşiği aşmıyor
çünkü bölütte hapaks yok, edilgen yok, kafiye kırılması yok, uzunluklar
ortalamaya yakın — **yıldız formülü içeriği hiç ölçmüyor** ve bu blok bunun en
açık gösterimi. Adaylar 565 (pozitif sınama vakası) ve 561'e yazıldı.

## YENİ ÖLÇÜM SORUNU — FÂSILA KISITI BULGU ÜRETİYOR (aday 566)

Sûre 25'in fâsılası **A sınıfı ve %100 ACC** (aday 526). Bu kısıt altında
"aynı kelime farklı bağlamda" bulguları **sistematik olarak üretiliyor olabilir**:
`سَبِيلا` altı geçiş, altısı da fâsıla (550, 564) · `نُشُورا` üç geçiş, üçü de
fâsıla (566) · `كَثِيرا` üç geçiş (25:14, 38, 49). **TUR SONU ZORUNLU İŞ:** fâsıla
kısıtı altında kelime tekrarının beklenen oranı hesaplanmadan sûre 25'in hiçbir
"aynı kelime, farklı katman" bulgusu kapatılmayacak.

## ADAY 529'A BEŞİNCİ VE ALTINCI VAKA — VE BİR ONARIM ÖLÇÜTÜ ÖNERİSİ

Sûre 25 tek başına altı vaka verdi: 25:1 `علم` · 25:3 `أله` · 25:13 `قرن` ·
25:19 `صرف` · 25:35 `وزر` · 25:47 `سبت`. **Öneri (aday 569):** dikey satırı
üretilirken kökün **bab'ı** da girdiye katılsın — `صرف` 25:19'da bab I ("çevirme"),
25:50'de bab II ("türlü türlü açıklama") ve anlam ayrımı **tam bab sınırında**.
Lemma ayrımından ucuz bir yaklaşım olabilir. Sınama kümesi: `صرف` (I/II), `قرن`
(I/II), `سبت` (tek lemma), `علم` (isim/fiil).

## ADAY 554 DÜŞTÜ, 570 OLARAK DÜZELTİLDİ

554'ün açıklaması "seyrek kökler eski sûrelerde geçmiyor" idi. Bu turda eklenen
`ذنب` **korpusta 39 geçişli** — seyrek değil, ve yine geriye dönük ihlâl
çıkmadı. **Hipotez tek veri noktasından kurulmuştu ve ikinci veri noktası onu
düşürdü; sessizce değiştirilmedi, düşürüldüğü belgelendi** (456→476 emsali).
Yeni hipotez: geriye dönük ihlâl, kökün **sıklığına** değil **kavram tablosunda
karşılığı olup olmamasına** bağlı — sık kökler dikey satırında Türkçe kavram
adıyla görünüyor, kök dizgisi hiç yazılmıyor.

## DİĞER

- **Sûrenin üçüncü ve son IDRAB'ı 25:44'te** — dizi 25:11 · 25:40 · 25:44 ile
  tamamlandı (makro sayım 3). 25:44 ayrıca sûrede HASR + IDRAB'ın birlikte
  geçtiği tek ayet.
- **25:41'de sûrenin ikinci Allah lafzı ve ilk kez itiraz edenin ağzında**
  (aday 562). `allah z=1,29` — **yıldız eşiğinin altında**, ayet ★ almıyor.
- **25:43'te ölçüt (a) ile dışlanan ilk esmâ artefaktı:** `وَكِيل` *(vekîl)*,
  göndergesi muhatap (elçi), ilâhî değil. Önceki artefaktlar ölçüt (b) ile
  dışlanıyordu (546, 555).
- **25:48 aday 517'nin sınama vakası olabilir** (aday 567): fâil `ٱلَّذِى`
  göndergesinden 1P'ye geçiyor, tagger 0 veriyor — bu lafız→zamir değil,
  gönderge→zamir. Sûre 25'in "iltifât 3" ölçümü bu belirsizliği taşıyor.

### DEVAM NOKTASI

**Sûre 25, ayet 51.** Blok 25:51-60. Beklenenler: 25:53 iki deniz (`مرج` · `فرت` ·
`ملح` · `أجج`) — **çıpa tanımı için ikinci sınama alanı** · 25:55 Allah lafzı
(üçüncü) · 25:56 **iltifât (1>23), sûrenin ikincisi** · 25:58 `ذنب` · 25:59 ve
25:60 `رَحْمٰن` (üç token) — **aday 549'un asıl veri kütlesi** · 25:60 adsız
aktör `nefer`.


### 25:51-60 EKİ — SÛRE 25 60/77, ADAYLAR 571-580

Okunan ayet **1695 → 1705** (korpusun %27,3'ü). `turkce_denetim.py` → **0**
(11 ihlâl, hepsi kök adının Türkçe cümle içinde karşılıksız anılması).
`anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl, diff = 0** (21637).
Bağlar 56 → **72**. Kök tablosu 977'de sabit; `صهر` karşılığı genişletildi
("eritme" → "eritme; hısımlık, sıhriyet").

## ★★ ADAY 549 BELİRLENDİ (aday 578) — `رَحْمٰن` ÖZEL AD GİBİ İŞLİYOR

Üç sözdizimsel kanıt, üçüncüsü belirleyici:

1. **25:26** `ٱلْمُلْكُ يَوْمَئِذٍ ٱلْحَقُّ لِلرَّحْمَٰنِ` — marife, `لِ` ile
   mecrur, **mülkün sahibi**; yüklem sıfatı değil.
2. **25:59** `ثُمَّ ٱسْتَوَىٰ عَلَى ٱلْعَرْشِ ٱلرَّحْمَٰنُ` — merfû, **tek
   başına**, önceki `ٱلَّذِى` göndergesinin açıklaması.
3. **25:60** `وَمَا ٱلرَّحْمَٰنُ` *(Rahmân da ne)* — **itiraz edenler adı
   TANIMADIKLARI bir ad olarak ele alıyor. Bir sıfat için bu soru sorulamaz.**

**Sonuç: esmâ tablosu sıfat-esmâ ile özel adı ayırmıyor.** Sûre 25'in "esmâ 22
token" sayımı doğrudan etkileniyor — beş `رَحْمٰن` tokeni özel ad sınıfına
geçerse sayım **17'ye düşer**. `bulgu_ozel_isim_katmani.json` ile çakışma
denetlenmedi. **Onarım ölçütü önerisi:** bir esmâ adayı (a) marife ve
(b) yüklem/temyiz konumunda değilse ve (c) gönderge konumundaysa → **özel ad**.
KAPATILAMAZ: 25:63 okunmadı.

## ★★ ADAY 462 — DOĞRULANMIŞ YANLIŞ POZİTİF VE KENDİ KAYDIMIZIN GERİ ÇEKİLMESİ

Sûre 25 makro profilinde **"adsız aktör: nefer *(bir bölük)* 25:60"** diye
kaydetmiştim. 25:60 okununca görüldü: 13. kelime `نُفُورا` *(nefret, kaçış)*,
`نفر` kökünün "kaçış" lemması — "nefer (bölük)" değil. **Aktör dedektörü kök
düzeyinde eşleşme yapıyor.** Makro kayıt `25/_makro/aktor` alanında **geri
çekildi**; adsız aktör sayımı **2 → 1**. Aynı ayette ters yönde de hata var:
25:38'de `أَصْحَٰبَ ٱلرَّسِّ` tabloya **girmiyor**, oysa `عاد` ve `ثَمُود`
giriyor. **462'nin tasarım kararı artık ertelenemez.** Onarım önerisi: aktör
eşleşmesi **lemma** düzeyinde yapılmalı (aday 529 ile aynı kök neden).

## ★★ ADAY 580 — YİRMİ ARDIŞIK YILDIZSIZ AYET, BÜTÜN DOĞA BÖLÜTÜ İÇLERİNDE

**25:41-60: ★★★ 0 · ★★ 0 · ★ 0.** Okumada görülen en uzun yıldızsız dizi ve
sûrenin doğa/kozmoloji bölütünün **tamamı** bu yirmi ayette. Bu blokta çıpalı üç
ayet daha: **25:53** iki su kütlesi, her biri iki sıfatla, iki adlı ayıraç
(`بَرْزَخ` + `حِجْر مَّحْجُور`) · **25:54** sudan beşer, `نَسَب` *(soy)* /
`صِهْر` *(hısımlık)* · **25:59** altı gün + istivâ + arş.

| | sayı | yıldız alan |
|---|---|---|
| çıpa taşıyan ayet (25:25, 45, 46, 47, 48, 49, 53, 54, 59) | 9 | **1** (25:25 ★★, kaynağı edilgenlik oranı) |
| ★★★ ayet (25:28, 33, 34) | 3 | çıpası **0** |

25:41-60'ta en yüksek z: 25:54'te `rab z=1,45` — eşiğin hemen altında.
**🜁 ve 🜂 protokol gereği yazılmadı; kural çiğnenmedi.** Şu anki izlenim: yıldız
ile çıpa arasında korelasyon **sıfır ya da negatif**. Bu bir **null sonuç**
olacak ve pozitif bulgular kadar dikkatle belgelenecek — ama önce **çıpa tanımı**
yazılmalı.

## DİĞER

- **Fiil + mef'ûl-i mutlak sûrede sekiz örnek, üç bab** (aday 572): bab II ×5,
  bab I ×2, bab III ×1 (25:52 `جِهَادا كَبِيرا`). **Yedisi fâsıla konumunda** —
  aday 566'nın karıştırıcısı burada da geçerli.
- **`حِجْرا مَّحْجُورا` terkibi korpusta yalnız 25:22 ve 25:53'te** (aday 573):
  biri bir **söz**, öteki bir **nesne**. Donmuş kalıp tanımını (437) zorluyor.
- **Seyrek kök çifti deseni** (aday 574): 25:23 `هبو`(2)+`نثر`(3), 25:54
  `نسب`(3)+`صهر`(2), ve 25:53 **üç** seyrek kök bitişik (`فرت`(3) · `ملح`(2) ·
  `أجج`(3)). Aday 531'in genişlemiş hâli.
- **25:55 sûrede ilk kez Allah lafzı ile `رَبّ`'bi aynı ayette taşıyor**, ve
  25:3'ün kök dizisini **sıralama tersine** tekrarlıyor (aday 575).
- **Sûrenin üç iltifâtı tamamlandı:** 25:14 (3>2), 25:52 (1>23), 25:56 (3>12).
  Üçü de zamir→zamir; aday 517'nin şüphelendiği lafız→zamir sınıfı **sûrede yok**
  — ama 25:48'de gönderge→zamir geçişi var ve tagger 0 veriyor (aday 567).
- **`نَذِير` dört geçiş, dördü de fâsıla** (aday 576): kitap → istenen melek →
  çoğaltılmayan uyarıcı → elçinin kendisi. 25:7 → 25:56 **yeni alt sınıf**:
  "istek → gönderge kayması" (cevap isteği yerine getirmiyor, göndergeyi
  değiştiriyor).

### DEVAM NOKTASI

**Sûre 25, ayet 61.** Son blok 25:61-77 (on yedi ayet). Beklenenler: 25:61
`تَبَارَكَ` üçüncü ve son geçiş (aday 528 kapanır) · 25:63'te beşinci ve son
`رَحْمٰن` (aday 578 kapanır) · 25:63-76 `عِبَادُ ٱلرَّحْمَٰنِ` bölütü · 25:68,
70, 71'de Allah lafzının kalan beş tokeni (aday 562 kapanır) · **25:64, 75, 77
★★★** · 25:77'de hapaks `عبأ` *(değer verme, aldırma)* ve sûrenin son ayeti.


### 25:61-70 EKİ — SÛRE 25 70/77, ADAYLAR 581-590

Okunan ayet **1705 → 1715** (korpusun %27,5'i). `turkce_denetim.py` → **0**
(3 ihlâl). `anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl, diff = 0**
(21642). Bağlar 72 → **86**. **Kök tablosu 977 → 982** (`ذرر` · `عبأ` · `غرف` ·
`غرم` · `قتر`); geriye dönük ihlâl yine çıkmadı.

## KAPANAN İKİ ADAY

**528 → 581 kapandı.** `تَبَارَكَ` üç geçiş (25:1, 10, 61), üçü de `برك` bab VI
PERF, üçünde de ardından `ٱلَّذِى`. Göreli konumlar **0,013 · 0,130 · 0,792**.
Sayım tam; null testi tur sonunda.

**549/578 kapandı — beş `رَحْمٰن` tokeni tamamlandı** (25:26, 59, 60 ×2, 63) ve
**beşi de sıfat-esmâ değil, gönderge/özel ad kullanımı**. Sonuncusu 25:63'te
`عِبَادُ ٱلرَّحْمَٰنِ` — muzâfun ileyh.

## ADAY 580 GÜÇLENDİ VE 590'A YÜKSELDİ

**25:61 sûrenin en açık gök-cismi ayeti ve yıldızı sıfır.** İki cisim iki ayrı
kökle adlandırılıyor (`سرج` *(kandil, sirâc)* n=4 · `قمر` *(ay)*) ve yalnız
ikincisi bir ışık sıfatı alıyor (`مُّنِير`). Bütün z değerleri eşik altında.
Aynı blokta 25:62 gece-gündüz bağıntısı — yine sıfır.

**Sûre 25'in güncel tablosu:** çıpa taşıyan **11** ayet (25:25, 45, 46, 47, 48,
49, 53, 54, 59, 61, 62), yıldız alan **1** (25:25 ★★, kaynağı edilgenlik oranı).
★★★ dört ayet (25:28, 33, 34, 64), **çıpası 0**.

## YENİ P0 — KISA AYET YANLILIĞI (aday 583)

25:64 `وَٱلَّذِينَ يَبِيتُونَ لِرَبِّهِمْ سُجَّدا وَقِيَٰما` — n=5, tek `رَبّ`,
oran 0,20 → **rab z=3,94, okumada görülen en yüksek Rab z'si** ve yıldızın tek
kaynağı. Bu, z'lerin **oran** ölçtüğünü üçüncü kez doğruluyor (25:34 pas oranı
1,00 → 5,38; 25:75 pas oranı 0,67 → 3,48; burada 0,20 → 3,94).

**Ve bir yanlılık önerisi:** ★★★ vakalarının hepsinde ayet ortalamadan kısa
(n z: −0,68 · −0,47 · −0,79). **Yıldız formülü kısa ayetleri sistematik olarak
kayırıyor olabilir** — oran paydası küçülüyor. Tur sonu zorunlu: yıldız ile ayet
uzunluğu arasındaki ilişki korpus çapında ölçülecek. 472/503'ün "formül
ortalamadan sapmayı seçiyor" bulgusuna **ek bir yanlılık kaynağı**.

## ADAY 529'A SEKİZİNCİ VAKA — VE EN DRAMATİĞİ (aday 586)

`قوم` *(kalkma; kavim; kıyamet)* **altı ayet içinde dört ayrı lemma**: 25:64
`قِيَام` · 25:66 `مُقَام` · 25:67 `قَوَام` · 25:69 `قِيَامَة`. Dikey satırı
dördü için de **aynı** komşuluğu getiriyor. Kök korpusun en sıklarından (n=660).
Sûre 25'te 529 vakaları: `علم` · `أله` · `قرن` · `صرف` · `وزر` · `سبت` · `صهر` ·
`قوم`.

Ve **aday 569'un bab-girdisi önerisi üçüncü veriyle güçlendi** (aday 584): `صرف`
üç geçiş, anlam ayrımı **tam bab sınırında** (bab I "çevirme", bab II "açıklama").

## DİĞER

- **25:68'de aynı ayette `أله` hem lafız hem sahte ilâh** (aday 587): üç token,
  ikisi lafız, biri nekre `إِلَٰها`. `defter.json`'ın A alanı nekreyi doğru
  dışlıyor ama **sahte-ilâh geçişleri için alan yok** (563'ün eksiği kanıtlandı).
- **25:6 ↔ 25:70 — sûrenin iki mührü aynı çift, aynı fâsıla** (aday 589).
  İkisi de **geçerli** çıktı; mühürsüz konumlarda ise sûre boyunca yanlış pozitif
  yoğun. **Aday 501'in "mühür sinyali" savıyla uyumlu.**
- **"Aynı kök, ters değer" sınıfı sûrede dört vakaya çıktı** (532, 543, 568, 582)
  artı iki alt vaka: `مشي` (kusur → erdem) ve `هون` (övgü → ceza).
- **25:24 iki ayrı ayetle karşıt çift kuruyor** (25:34 ve 25:66) — bu sınıfta ilk
  üçlü yapı (aday 585).

### DEVAM NOKTASI

**Sûre 25, ayet 71 — son yedi ayet.** Beklenenler: 25:71'de Allah lafzının
sekizinci ve son tokeni ve `توب` *(tövbe)* ×3 (sûrenin en yoğun kök ikilemesi) ·
25:72 `زور` ikinci geçiş (aday 533 ile) · **25:75 ★★★** (pas z=3,48) ·
**25:77 ★★★** (hapaks `عبأ` z=3,38, sûrenin son ayeti) · 25:74'te `ذرر`
*(zürriyet)* · 25:76'da `مُسْتَقَرّ` üçüncü geçiş (aday 585 tamamlanır).
Sûre kapanınca **tam profil çıkarılacak**: esmâ yeniden sınıflandırması,
yıldız-çıpa tablosu, `سبل`/`نُشُور`/`نَذِير` sayımları ve fâsıla-kısıtı null'u.


### 25:71-77 EKİ — **SÛRE 25 (FURKĀN) TAM 77/77**, ADAYLAR 591-600

Okunan ayet **1715 → 1722** (korpusun %27,6'sı). `turkce_denetim.py` → **0**
(5 ihlâl). `anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl, diff = 0**
(21642). Bağlar 86 → **96**. Kök tablosu 982'de sabit.

**Sûre 1 ve 9-25 TAM.** Sûre 25 kapanış profili `okuma_metni.json` →
`25/_kapanis` alanına yazıldı.

## ★★★ SÛRE KAPANIŞ BİLANÇOSU

### Esmâ — tam denetim, hata oranı **%36** (aday 598)

22 tokenin tek tek denetimi:

| sınıf | sayı | örnekler |
|---|---|---|
| **geçerli** | 8 | 25:6 ve 25:70 `غَفُور\|رَحِيم` (mühür) · 25:20 `بَصِير` · 25:31 `نَصِير` · 25:54 `قَدِير` · 25:58 `خَبِير` |
| **artefakt** | 8 | 25:18 `وَلِيّ` (çoğul) · 25:19, 21, 52 `كَبِير` (sıfat) · 25:43 `وَكِيل` (gönderge muhatap) · 25:63, 75 `سَلام` (söz) · 25:72 `كَرِيم` (kulların hâli) |
| **özel ad** | 5 | `رَحْمٰن` 25:26, 59, 60 ×2, 63 |
| **belirsiz** | 1 | 25:59 `خَبِير` |

**Aday 501'in mühür sinyali üçüncü sûrede de doğrulandı:** iki mühürlü konumun
**ikisi de geçerli**; sekiz artefaktın **sekizi de mühürsüz**. Sûre 23 mühür 0 →
hata %67; sûre 24 mühür 12 → mühürlü konumlar temiz; sûre 25 mühür 2 → %36.

Artefakt sınıfları: ölçüt (a) gönderge ihlâli **3**, ölçüt (b) sıfat/nekre **4**,
ölçüt (b) çoğul **1**. **Özel ad sınıfı tabloda yok** (aday 578).

### Yıldız / çıpa — tam tablo (aday 599)

★★★ **6** · ★★ 5 · ★ 8 · yıldızsız 58.

**Altı ★★★ ayetin altısında da çıpa sıfır** (25:28, 33, 34, 64, 75, 77).
Kaynaklar: hapaks ×3, edilgenlik oranı ×2, Rab oranı ×1 — **altısı da
sözlük/biçim istatistiği, hiçbiri içerik**.

**Çıpa taşıyan on bir ayetin yalnız biri yıldızlı** (25:25 ★★, kaynağı yine
edilgenlik oranı). Çıpalılar: 25:25 gök yarılması · 45-46 gölge-güneş süreci ·
47 gece/uyku/gündüz · 48 rüzgâr-yağış sıralaması · 49 su ve diriltme · 53 iki su
kütlesi · 54 sudan beşer · 59 altı gün + istivâ + arş · 61 burçlar, kandil,
aydınlatan ay · 62 gece-gündüz bağıntısı.

**Protokol gereği sûre boyunca hiçbir uzman merceği yazılmadı; kural
çiğnenmedi.** Yıldız ile çıpa arasında korelasyon **sıfır ya da negatif**
görünüyor. Sûre 24'te ayrışma ters yöndeydi (24:45) — **iki sûre, iki yön**.

### Fâsıla kısıtı — kendi bulgularımızın karıştırıcısı (aday 600)

Sûrenin **77 fâsılasının 77'si de ACC**, 76'sı `ا`. Bu kısıt altında fâsıla
kelimesi tekrarları: `سَبِيلا` 7 · `نَذِيرا` 4 · `نُشُورا` 3 · `كَثِيرا` 3 ·
`كَبِيرا` 3 · `مُقَاما` 2 · `سَلَٰما` 2 · `مَّحْجُورا` 2 · `رَّحِيما` 2.

**Sûre 25'in "aynı kelime farklı katmanda" bulgularının tamamı (adaylar 550,
564, 566, 573, 576, 585, 596) bu kısıtın altında üretilmiş olabilir.** Tur sonu
zorunlu: A sınıfı ACC fâsılalı sûrelerde tekrar oranının taban dağılımı
çıkarılmadan **bu yedi adayın hiçbiri kapatılmayacak**. Bu kayıt, kendi
bulgularımızı düşürebilecek bir ölçümün önceden yazılması olarak açıldı
(476/570 emsali).

### Araç hataları — sûre 25'in bilançosu

- **Dikey katman kök-lemma karışması: dokuz vaka** (`علم` · `أله` · `قرن` ·
  `صرف` · `وزر` · `سبت` · `صهر` · `قوم` · `حيي`). Onarım önerisi: dikey girdisine
  **bab** eklensin (adaylar 529, 569, 584).
- **Esmâ tablosu hata oranı %36** (aday 598).
- **Aktör tablosu**: yanlış pozitif (25:60 `نُفُورا` → "nefer") ve eksik pozitif
  (25:38 `أَصْحَٰبَ ٱلرَّسِّ`); makro kaydımız geri çekildi (aday 579).
- **`esit` alanı** iki vakayı da kaçırıyor: 25:9 = 17:48 (imlâ farkı, 530) ve
  25:66 ≈ 25:76 (tek kelime farkı, 596). **İki ayrı alana bölünmeli.**
- **Yıldız formülünde kısa ayet yanlılığı şüphesi** (aday 583): altı ★★★ ayetin
  beşinde ayet ortalamadan kısa.

### KAPANAN ADAYLAR

**528 → 581** (`تَبَارَكَ` üçlüsü) · **535 → 545** (25:7 ↔ 25:20, ön-kayıt
tuttu) · **549/578** (`رَحْمٰن` beş token, hepsi özel ad) · **544 → 597**
(`كذب` dört geçiş, üç fâil) · **562** (lafız alıntı sayımı: alıntı içi 1,
anlatı içi 7).

### DEVAM NOKTASI

**Sûre 26 (Şuarâ) — makro profilden başla, sonra 26:1'den oku.** Dizi artık
23 (Mekkî) → 24 (Medenî) → 25 (Mekkî) → **26 (Mekkî)**: A/R ekseni için
**dördüncü veri noktası** (adaylar 470, 498, 525). Sûre 26'nın ön ölçümü:
227 ayet, 1318 kelime, Allah lafzı 13 (0,28x), `رَبّ` 36 (1,73x), A/R = 0,36 —
**sûre 23 ve 25'in 0,57'sinden farklı**. Ayrıca sûre 26 hurûf-ı mukattaa ile
açılıyor (طسم) ve nakarat yapısı taşıyor — 509/518 (kafiye kuşağı) ve 491/524
(sûre-boyu halka) için yeni veri.


---

## 2026-09-04 — SÛRE 26 (ŞUARÂ) AÇILDI; MAKRO + 26:1-20, ADAYLAR 601-614

Okunan ayet **1722 → 1742** (korpusun %27,9'u). `turkce_denetim.py` → **0**
(3 ihlâl). `anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl, diff = 0**
(21648). Kök tablosu **982 → 985** (`بخع` · `خضع` · `طلق`); geriye dönük ihlâl
yine çıkmadı. Bağlar: yeni `AF_suara` kümesi, 15 bağ.

### A/R EKSENİ — "MEKKÎ 0,57" HİPOTEZİ İLK SINAVDA DÜŞTÜ

| sûre | tip | kelime | A | R | A kat | R kat | A/R |
|---|---|---|---|---|---|---|---|
| 23 | Mekkî | 1050 | 13 | 23 | 0,36 | 1,73 | 0,57 |
| 24 | Medenî | 1316 | 80 | 0 | 1,74 | 0,00 | ∞ |
| 25 | Mekkî | 893 | 8 | 14 | 0,26 | 1,24 | 0,57 |
| **26** | **Mekkî** | **1318** | **13** | **36** | **0,28** | **2,16** | **0,36** |

İki Mekkî sûrenin aynı oranı vermesi **tekrarlanmadı**. A yoğunluğu yine düşük
(0,28x ≈ sûre 25'in 0,26x'i) ama **R yoğunluğu 2,16x — okumada görülen en
yüksek**. Ayrışan A değil **R**. Lafızlı on üç ayetin hepsi **26:89'dan sonra**;
ilk 88 ayette lafız sıfır (sûre 25'te ilk 16 ayetti — aday 527 sınıfı).

### ★★ ADAY 583 DOĞRULANDI (aday 602) — KISA AYET YANLILIĞI

Sûre 26 ayet başına **5,81 kelime** (okumada en kısa) ve **41 ★★★ ayet (%18,1)**.
Kaynak dağılımı: **rab tek başına 21 · allah tek başına 8** · pas 6 · hapaks 4 ·
karışık 2 — **yirmi dokuzu eksen oranından**. 26:9'da n=5 ve tek `رَبّ` →
z=3,94; 26:26'da n=5 → **z=8,20**, okumada görülen en yüksek z.

Betimsel korpus taraması (ayet ≥20 olan 79 sûre): ortalama ayet uzunluğu ile
★★★ payı arasında **Pearson r = −0,367**. **Anlamlılık testi koşulmadı.**
Uyarı: korelasyon orta düzeyde ve karşı örnekli (sûre 24 ort 20,56 → %23,4;
sûre 25 ort 11,60 → %7,8). Ayet uzunluğu tek açıklayıcı değil.

### ★★ YILDIZ SAYIMININ BAĞIMSIZLIK İHLÂLİ (aday 606) — KRİTİK

Sûre 26'da **34 ayet nakarat alanı dolu, 44 ayet `esit` eşleşmesi taşıyor**
(sûre 25'te `esit` sûre boyunca **sıfırdı**). Beş nakarat kümesi; bunlardan
`وَإِنَّ رَبَّكَ لَهُوَ ٱلْعَزِيزُ ٱلرَّحِيمُ` **sekiz ayette birebir aynı ve
sekizi de ★★★**. Yani sûrenin 41 ★★★ ayetinin en az sekizi **tek bir
nakarattan** geliyor — bunlar **bağımsız gözlem değil**.

**TUR SONU ZORUNLU:** ★★★ payı hesaplanırken nakarat ayetleri **tek gözlem**
sayılacak; düzeltilmiş pay (41−7)/227 = **%15,0**. Düzeltme sûre 24 ve 25 için
de yapılacak.

### ★★ ESMÂ — OKUMADA GÖRÜLEN EN BÜYÜK ARTEFAKT BLOĞU (aday 601)

Sûre 26'da `مُؤْمِن` **on beş token ve on beşi de artefakt** — hepsi
`مُؤْمِنِين` *(müminler)*, göndergesi insanlar. Sûrenin 51 esmâ tokeninin
**%29'u** tek başına bu blok. Ve sûrenin **ilk üç esmâ tokeninin üçü de
artefakt** (26:2 `مُبِين`, 26:3 `مُؤْمِن`, 26:7 `كَرِيم`).
**Sûre 26'nın "esmâ 51 token / mühür 10" makro sayımı onarım yapılmadan
kullanılamaz.**

### DİĞER

- **26:1'de ▽ satırı YAZILAMADI** — ayet `طسٓمٓ`, kök taşımıyor. Protokol
  (komşuluk zenginleşmesi olmadan ▽ yazılamaz) gereği atlandı, gerekçe
  `26/_mercek_atlama_notu` → `_blok_notu_26_1_20`'ye kaydedildi. Okumada ilk kez.
- **Kafiye rejimi tamamen farklı** (aday 612): N sınıfı 222 (`ن` 193 · `م` 29) ·
  `ل` 4 · `ٓ` 1. Dört kırılma. **26:17'nin fâsılası özel ad** (`إِسْرَٰٓءِيلَ`)
  ve kırıyor; 26:13'ünki de özel ad (`هَٰرُونَ`) ama kırmıyor. **Yeni soru:**
  `ن` ve `م` ayrı harf ama aynı N sınıfında — sınıf tanımı belgelenmemiş.
- **İltifât 15 — okumada en yüksek** (23'te 7, 24'te 0, 25'te 3).
- **Blok bilançosu:** ★★★ 2 · ★★ 2 · ★ 1 · 15 yıldızsız. **Dört yıldızlı ayetin
  dördünde de tek kaynak `رَبّ` oranı**, beşincisinde kafiye kırılması.
  **Hiçbirinde çıpa yok.** Çıpa taşıyabilecek tek ayet 26:7 (bitki çeşitliliği)
  ve yıldızsız — sûre 25'in deseninin aynen tekrarı (aday 599).

### DEVAM NOKTASI

**Sûre 26, ayet 21.** Blok 26:21-40 — Mûsâ-Firavun diyaloğunun sürdüğü bölüt.
Beklenenler: 26:23-28 `رَبّ ٱلْعَٰلَمِينَ` zinciri (26:23, 24, 26, 28 — dördü de
★★★, kaynak rab oranı) · **26:26'da rab z=8,20, okumada en yüksek z** ·
26:38-39 nakarat öncesi kalabalık sahnesi.


### 26:21-40 EKİ — SÛRE 26 40/227, ADAYLAR 615-625

Okunan ayet **1742 → 1762** (korpusun %28,3'ü). `turkce_denetim.py` → **0**
(2 ihlâl). `anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl, diff = 0**
(21653). Kök tablosu **985 → 989** (`ثعب` · `سجن` · `فرر` · `وقت`). Bağlar
`AF_suara` 15 → **29**.

## ★★ ADAY 621 — esit ALANININ DAVRANIŞI ARTIK TAM TANIMLI

**26:32-33 ↔ 7:107-108 ardışık bölüt ikizi ve `esit` alanı İKİSİNİ DE
YAKALIYOR.** Bu, aday 530'un tam karşıtı: 25:8-9 ↔ 17:47-48 de ardışık bölüt
ikiziydi ama `esit` alanı 25:9 = 17:48 özdeşliğini **imlâ farkı** yüzünden
kaçırmıştı. İki vaka birlikte alanın davranışını tanımlıyor:

| durum | vaka | sonuç |
|---|---|---|
| harekeli tam dizgi eşleşmesi | 26:32-33 = 7:107-108 | **yakalıyor** |
| imlâ varyantı | 25:9 = 17:48 | kaçırıyor |
| tek kelime farkı | 25:66 ≈ 25:76 | kaçırıyor |

**ONARIM ÖLÇÜTÜ ARTIK YAZILABİLİR:** alan **üçe** bölünecek — `esit_tam`
(mevcut), `esit_normal` (harekesiz + elif/hemze varyantı normalize),
`esit_yakin` (n−1 kelime ortak). **Sınama kümesi bu üç vakayla hazır.**

## ★★ ADAY 602'NİN EN UÇ VAKASI VE İKİNCİ BAĞIMSIZLIK İHLÂLİ

**26:26'da rab z = 8,20 — okumada görülen en yüksek z.** Sebep ölçüldü: n=5 ve
içinde **iki** `رَبّ`, oran 0,40; payda küçük.

Ve **aday 624 — okumada ilk kez iki ardışık ayet aynı kaynaktan ★★★**: 26:38 ve
26:39, ikisinde de n=5, tek fiil edilgen, oran 1,00, `pas z=5,38`. Nakarat yok
ama **aynı yapısal sebep** iki ayete birden aynı z'yi veriyor. Yani ★★★ sayımı
hem **tekrar** (nakarat, aday 606) hem **kısa-ayet kümelenmesi** yoluyla şişiyor.
**Tur sonu:** sûre 26'nın 41 ★★★ ayetinin kaçı n≤5 ve tek fiilli — envanter.

## ★ ADAY 578'E KARŞI ÖRNEK — KENDİ BULGUMUZU ZAYIFLATAN VERİ (aday 616)

578'de **25:60'ın `وَمَا ٱلرَّحْمَٰنُ` sorusu** özel-ad kullanımının
*belirleyici* kanıtı sayılmıştı. **26:23'te aynı kalıp bir sıfat tamlamasına
uygulanıyor:** `وَمَا رَبُّ ٱلْعَٰلَمِينَ`. Yani kalıp tek başına "özel ad"
kanıtı **değil**. 578'in sonucu diğer iki kanıtla (marife+mecrur, merfû tek
başına) ayakta kalıyor, ama **üçüncü kanıt zayıfladı**. Kayıt 570/600 emsalinde
açıkça yazıldı.

## ADAY 529 ONUNCU VAKAYA ÇIKTI — VE ONARIMIN İKİ KATMANLI OLMASI GEREKİYOR

Yeni vakalar: **26:27 `جنن`** *(cennet/cin/delilik)* — sûre 25'te beş geçişin
beşi de "cennet", burada "delilik" (aday 619) · **26:36 `رجو`** *(umma;
erteleme)* — sûre 25'te iki geçiş bab I "umma", burada bab IV "erteleme"
(aday 623) · 26:22 `منن` *(nimet verme; başa kakma)*.

**Kritik:** 569/584'ün **bab girdisi** önerisi `صرف` · `قرن` · `رجو` · `طلق`'ı
çözüyor ama **`جنن`'de yetmiyor** — üç anlam da isim kalıplarında
(`جَنَّة` · `جِنّ` · `مَجْنُون`), bab ayrımı yok. **Bu kök için lemma düzeyi
zorunlu; onarım iki katmanlı olmalı.**

## DİĞER

- **26:24 ↔ 26:28 paralel kapsam tanımı** (aday 617): dikey eksen (gök-yer-ara,
  şart cevabı `يقن`) ve yatay eksen (doğu-batı-ara, şart cevabı `عقل`). Okumada
  ilk kez bir kalıp dikey/yatay eksen çifti üzerinden tekrarlanıyor.
- **`أله` sahte-ilâh dizisine dördüncü konuşan** (aday 620): 26:29'da ilâhlığı
  **kendine atfeden**. Sûre 25'te üç konuşan vardı.
- **Sûrenin iki kafiye kırılması aynı özel adla** (26:17, 26:22 —
  `إِسْرَٰٓءِيلَ`).
- **Blok bilançosu:** ★★★ 4 (26:23, 26, 38, 39) · ★★ 3 · ★ 2 · 11 yıldızsız.
  **Dokuz yıldızlı ayetin kaynak dağılımı: rab ×5 · pas ×3 · kafiye kırılması
  ×1 — hiçbiri içerikten.** Blokta çıpa taşıyabilecek ayet **yok** (bölüt
  tamamen diyalog). Sûre 26'nın okunan 40 ayetinde ★★★ 6, çıpası 0; çıpalı ayet
  1 (26:7) ve yıldızsız.

### DEVAM NOKTASI

**Sûre 26, ayet 41.** Blok 26:41-60 — büyücülerin secdesi ve İsrâiloğullarının
çıkışı. Beklenenler: 26:46-48 secde sahnesi (26:46, 47, 48 üçü de ★★★) ·
26:47-48 ↔ 7:121-122 `esit` eşleşmesi (aday 621'e ikinci ardışık ikiz) ·
26:50 hapaks `ضير` *(zarar)* · 26:54 hapaks `شرذم` *(döküntü topluluk)* ·
26:59'da sûrenin üçüncü kafiye kırılması.


### 26:41-60 EKİ — SÛRE 26 60/227, ADAYLAR 626-638

Okunan ayet **1762 → 1782** (korpusun %28,6'sı). `turkce_denetim.py` → **0**
(6 ihlâl). `anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl, diff = 0**
(21655). Kök tablosu **989 → 991** (`شرذم` · `ضير`). Bağlar `AF_suara` 29 → **43**.

## ★★★ KISA AYET YANLILIĞININ EN TEMİZ ÜÇ GÖSTERİMİ

**(1) Üç ardışık ★★★ — okumada ilk kez** (26:46, 47, 48; aday 624'te ikiydi).
Kaynaklar: 26:46 `pas z=5,38` (n=3, tek fiil edilgen) · 26:47 `rab z=5,01`
(n=4) · 26:48 **`rab z=6,78`** (n=3) — okumada ikinci en yüksek z. **Üçünde de
ayet üç-dört kelime.**

**(2) Sûrenin en uzun ayeti yıldızsız** (aday 632). 26:49: n=21 (sûre
ortalamasının 3,6 katı), **yedi kip işareti** (okumada en yoğun), **2MP ×10**
(okumada tek şahıstan en yüksek sayım), **yedi xref**. Bütün z'ler eşik altında.
Aynı sûre, aynı formül: üç kelimelik ayetler ★★★, yirmi bir kelimelik ayet
yıldızsız.

**(3) Aynı kalıptaki üç ayetten yalnız biri ★★★** (aday 637). 26:54-56 —
üçü de kısa (4, 3, 3), üçü de `إِنَّ` ile açılıyor, **üçünde de fiil yok**.
26:54 ★★★, 26:55 ve 26:56 yıldızsız; **ayrım tek bir hapakstan** (`شرذم`).
Yıldız formülünün içeriği değil **sözlük seyrekliğini** ölçtüğünün en temiz
gösterimi.

**Blok bilançosu:** ★★★ 5 · ★★ 0 · ★ 2 · 13 yıldızsız. **Beş ★★★ ayetin beşinde
de n≤7, dördünde n≤4.** Hiçbirinde çıpa yok; blokta çıpa taşıyabilecek ayet yok.
Sûre 26'nın okunan 60 ayetinde ★★★ **11**, çıpası **0**.

## ADAY 621'E İKİNCİ VERİ VE ÜÇÜNCÜ SINAMA VAKASI

**26:47-48 ↔ 7:121-122 ardışık bölüt ikizi ve `esit` alanı ikisini de
yakalıyor** — sûre 26'da ikinci ardışık ikiz. Buna karşılık **26:36 ↔ 26:53**
(öneri → uygulama, `فِى ٱلْمَدَآئِنِ حَٰشِرِينَ` birebir ortak, fâsıla aynı)
`esit` tarafından **yakalanmıyor**: iki ayet tam özdeş değil. Bu, önerilen
`esit_yakin` alanının üçüncü sınama vakası (aday 636).

## ESMÂ ONARIMI İÇİN KRİTİK VERİ (aday 629)

**Tablo 26:44'te gönderge denetimini DOĞRU yapıyor:** `بِعِزَّةِ فِرْعَوْنَ`
*(Firavun'un izzetine)* esmâ **sayılmıyor**. Ama 26:34'te (`عَلِيم`, gönderge
büyücü) ve 26:49'da (`كَبِير`, gönderge insan) **yapmıyor**.

**Hipotez (test edilmedi):** tablo gönderge zincirini izlemiyor; 26:44'te kelime
`عِزَّة` (masdar) biçiminde ve esmâ listesindeki `عَزِيز` lemmasıyla eşleşmiyor —
yani **doğru sonuç yanlış sebeple** çıkıyor. Sınama kümesine eklendi.

## ÇATI YÖRÜNGESİ — YENİ BİR SINIF (adaylar 628, 635)

**`لقي` *(atma)* dört ardışık ayette:** emir (2MP) → çoğul fâil → tekil fâil →
**edilgen**. Atma eyleminden atılma hâline (26:43-46).
**`تبع` *(uyma)* üç geçişte:** niyet (etken) → uyarı (edilgen) → gerçekleşme
(etken bab IV) (26:40, 52, 60).
İki vaka bir arada "sûre 26 çatı yörüngesini sistematik kullanıyor" hipotezini
akla getiriyor — ama sûre 60/227'de, **kalıp iddiası kuralı geçerli**. Ve **çatı
alanı `defter.json`'da yok**; ikisi de elle kodlandı.

## DİĞER

- **`رَبُّ ٱلْعَٰلَمِينَ` zinciri (aday 631):** Firavun'un sorusu (26:23) → Mûsâ'nın
  iki kapsam cevabı (26:24 dikey, 26:28 yatay) → **büyücülerin ikrarı** (26:47,
  terkip birebir) → özelleştirme (26:48). **Soruyu kapatan taraf üçüncü.**
  Uyarı: üç ayet de ★★★ ve üçünde de kaynak rab oranı — 602/624 karıştırıcısı bu
  zinciri mekanik olarak yıldızlı gösteriyor olabilir.
- **Sûrenin dört kafiye kırılmasından üçü aynı özel adla** (26:17, 22, 59 —
  `إِسْرَٰٓءِيلَ`); aday 612 güçlendi.
- **529 kümesine iki yeni vaka:** `قرب` (korpusta ilâhî yakınlık, burada saray
  yakınlığı) ve `أول` üç katmanda (25:5 masallar, 26:26 atalar, 26:51 öncülük).
- **Aktör tablosu tutarsızlığına yeni vaka (aday 638):** `جَنَّٰت` 26:57'de
  tabloya girmiyor, oysa 25:24'te `جَنَّة` girmişti.

### DEVAM NOKTASI

**Sûre 26, ayet 61.** Blok 26:61-80 — denizin yarılması ve İbrâhîm kıssasının
açılışı. Beklenenler: **26:62-63 ★★★** (26:63'te hapaks `طود` *(büyük dağ)*) ·
26:68 nakarat (`عَزِيز|رَحِيم`, ikinci geçiş) · 26:69-77 İbrâhîm bölütü ·
**26:77 ★★★** ve `رَبَّ ٱلْعَٰلَمِينَ` terkibinin beşinci geçişi · 26:78-80
`ٱلَّذِى` zinciri (yaratma, doyurma, şifa).


### BİÇİM İHLÂLİ KAYDI — 2026-09-04, blok 26:41-60

**Ne oldu:** blok 26:41-60'ta on altı ayet (26:42-45 ve 26:49-60) sohbete TAM
KİPTE yazılmadı, özete sıkıştırıldı. Kullanıcı uyarısıyla tespit edildi ve on
altı ayet tam kipte yeniden yazıldı.

**Neden ihlâl:** OKUMA_STANDARDI 2026-08-24 (biçim kilidi) ve okuma protokolü
açık — *"Dosyaya yazıp sohbete özet koymak okuma sayılmaz."* `okuma_metni.json`
kaydı ve iki denetim (turkce_denetim 0, anahtar_denetim diff 0) DOĞRUYDU; eksik
olan yalnız sohbetteki okumaydı. Yani ölçüm katmanı sağlam, teslim katmanı
bozuktu.

**Kök sebep:** yirmi ayetlik blokta çıktı hacmi tam kipi kaldırmayınca özete
kayıldı. Bu, sûre 23-24 turunda iki kez düşen kalıp iddiası kuralı (adaylar 503,
505) ile aynı sınıftan bir disiplin kaybı: kural biliniyor, baskı altında
uygulanmıyor.

**ÖNLEM (bundan sonra kural):** bir blok yirmi ayetse ve çıktı hacmi tam kipi
kaldırmıyorsa, **ÖZETE KAYILMAZ — BLOK BÖLÜNÜR** ve gerekçesi
`<sûre>/_blok_bolme_notu` alanına yazılır. Sûre 25'te bu doğru uygulanmıştı
(beş bölme, hepsi gerekçeli); sûre 26'nın ilk üç bloğunda uygulanmadı.
**Sûre 26'nın kalan bloklarında blok boyu ONA indiriliyor.**


### 26:61-70 EKİ — SÛRE 26 70/227, ADAYLAR 639-646 · BLOK BOYU ONA İNDİRİLDİ

Okunan ayet **1782 → 1792** (korpusun %28,7'si). `turkce_denetim.py` → **0**
(ilk koşuda sıfır — okumada ilk kez hiç ihlâl çıkmadı). `anahtar_denetim.py`
(PYTHONHASHSEED=0) → **58 ihlâl, diff = 0** (21657). Kök tablosu **991 → 993**
(`طود` · `فلق`). Bağlar `AF_suara` 43 → **53**.

**Blok boyu ONA indirildi** — biçim ihlâli önlemi (yukarıdaki kayıt).

## ★★ AKTÖR TABLOSU — İKİNCİ DOĞRULANMIŞ YANLIŞ POZİTİF (aday 641)

Sûre 26 makro profilinde **"adsız aktör: ferîk *(bir bölük)* 1"** yazmıştım.
26:63 okununca görüldü: 11. kelime `فِرْقٍ` *(parça, bölük)* — `فرق` kökü ve
**denizin bir parçası** (`كُلُّ فِرْقٍ كَٱلطَّوْدِ ٱلْعَظِيمِ`). **Makro kayıt
geri çekildi;** adsız aktör sayımı 1 → 0.

**Desen artık net:** adsız aktör dedektörü **kök düzeyinde** eşleşiyor ve iki
sûrede iki kez yanlış pozitif üretti (25:60 `نُفُورا` → "nefer", 26:63 `فِرْقٍ`
→ "ferîk"). **Okunan iki sûrede toplam adsız aktör sayımı 3'tü ve ikisi
artefakt — hata oranı %67.** Onarım: eşleşme **lemma** düzeyinde yapılmalı.
**Adsız aktör sayımları kullanılmayacak.**

## ★★ YENİ MERCEK ATLAMA GEREKÇESİ SINIFI (aday 646) — 26:63

Okumada **ilk kez** bir ★★★ ayette **çıpa var ama mercek yazılmadı**, ve gerekçe
"çıpa yok" değil:

> `فَٱنفَلَقَ فَكَانَ كُلُّ فِرْقٍۢ كَٱلطَّوْدِ ٱلْعَظِيمِ`

Ayet **fiziksel bir olay** veriyor (`فلق` bab VII) ve bir **ölçek benzetmesi**
ekliyor (koca bir dağ gibi) — aday 561'in "adlandırma + nitelik" düzeyi, 25:61
(burçlar, kandil, aydınlatan ay) ile aynı. **Ama iki uzman merceği biyolog ve
uzay; olay ne biyolojik ne astronomik.** Bir su kütlesinin yarılması
jeofizik/hidrodinamik alanına düşer ve **bu projede mercek sınıfı yok.** Mercek
yazmak için üçüncü bir sınıf açmak gerekirdi; **açılmadı.**

**TUR SONU KARARI GEREKLİ:** (a) üçüncü bir mercek sınıfı açılacak mı? (b)
açılmayacaksa "sınıf dışı çıpa" ayrı kodlanacak mı? **Uyarı:** mercek sınıfı
eklemek OKUMA_STANDARDI'nın biçim kilidini değiştirir — bu bir **tasarım
kararı** ve aday 462 gibi kullanıcı onayı gerektirir.

Not: 26:63 sûre 25-26'da **çıpası olan ilk ★★★ ayet**, ama yıldızını çıpadan
değil **hapakstan** alıyor — aday 599'un "yıldız içerik ölçmüyor" savı bozulmuyor.

## ADAY 621'E DÖRDÜNCÜ SINAMA VAKASI (aday 642)

**26:64 ≈ 26:66** — n=3, bab IV, 1P ×2, fâsıla `ٱلْءَاخَرِينَ` ikisinde de;
değişen yalnız fiil (`أَزْلَفْنَا` *(yaklaştırdık)* / `أَغْرَقْنَا` *(boğduk)*).
`esit` **yakalamıyor**. Sınama kümesi artık beş vakalı:

| vaka | `esit` |
|---|---|
| 26:32-33 = 7:107-108 · 26:47-48 = 7:121-122 · 26:66 = 37:82 | **yakalıyor** |
| 25:9 = 17:48 (imlâ varyantı) | kaçırıyor |
| 25:66 ≈ 25:76 (tek kelime) | kaçırıyor |
| 26:36 ≈ 26:53 (kısmi ortak) | kaçırıyor |
| 26:64 ≈ 26:66 (tek kelime) | kaçırıyor |

## DİĞER

- **`جمع` *(toplama)* sûrede altı geçiş, altı biçim** (aday 639): edilgen fiil →
  etken ism-i fâil → pekiştirme (tehdit) → sıfat → tesniye isim → pekiştirme
  (kurtuluş). 628/635'in çatı yörüngesi sınıfının genişlemiş hâli: burada değişen
  yalnız çatı değil **biçim sınıfı**.
- **`أَجْمَعِينَ` aynı fâsıla ters kutup** (aday 643): 26:49 tehdit kapsamı,
  26:65 kurtuluş kapsamı.
- **Nakarat mimarisinin ilk kapanışı:** 26:8-9 çifti kıssanın **önünde**,
  26:67-68 çifti **arkasında** — arada elli dokuz ayet. **26:9 ve 26:68 aynı ayet
  ve ikisi de ★★★.**
- **Blok bilançosu:** ★★★ 3 (26:62, 63, 68) · ★★ 0 · ★ 0 · 7 yıldızsız.
  Kaynaklar rab ×2, hapaks ×1. Sûre 26'nın okunan 70 ayetinde ★★★ **14**.

### DEVAM NOKTASI

**Sûre 26, ayet 71.** Blok 26:71-80 (on ayet). Beklenenler: 26:71-74 İbrâhîm'in
kavmiyle diyaloğu · **26:77 ★★★** ve `رَبَّ ٱلْعَٰلَمِينَ` terkibinin beşinci
geçişi · **26:78-80 `ٱلَّذِى` zinciri** (yaratma, doyurma, şifa) — sûre 25'in
`ٱلَّذِى` gönderge zinciriyle (aday 527) karşılaştırma için ilk fırsat.


### 26:71-80 EKİ — SÛRE 26 80/227, ADAYLAR 647-657

Okunan ayet **1792 → 1802** (korpusun %28,9'u). `turkce_denetim.py` → **0**
(22 ihlâl; hepsi Türkçe cümle içinde karşılıksız kök anması). `anahtar_denetim.py`
(PYTHONHASHSEED=0) → **58 ihlâl, diff = 0** (21658). Kök tablosu **993 → 994**
(`شفي`). Bağlar `AF_suara` 53 → **64**.

## ★ MAKRO SAYIM TUTARSIZLIĞI — YENİ ÖLÇÜM NOTU (aday 650)

Sûre 26 makro profilinde **`fig` IDRAB = 2** yazmıştım. Okunan 80 ayette IDRAB
**üç kez** görüldü (26:44, 26:74 ve makro sayımın işaret ettiği üçüncü). **Makro
profil üretiminin (`makro26.py`) `fig` sayımı denetlenecek** — tur sonu işi.
Bu, kendi ürettiğim bir sayımın okuma sırasında düşmesi; 554 → 570 ve 578 → 616
emsallerinde olduğu gibi açıkça kaydedildi.

## ADAY 527'NİN İLK KARŞILAŞTIRMA VERİSİ (aday 655)

**26:78-80 `ٱلَّذِى` zinciri** ve sûre 25'inkiyle **işlevi farklı**:

| | sûre 25 (25:1, 2, 6, 10) | sûre 26 (26:78-80) |
|---|---|---|
| gönderge | üçüncü şahıs, anlatıcı konuşuyor | **birinci şahsın kendi Rabbi** |
| konum | sûrenin ilk on beş ayeti, lafız/Rab **yerine** | bir konuşmanın içinde |
| biçim | dördü de `ٱلَّذِى` | ilk ikisi `ٱلَّذِى`, üçüncüsü **şart cümlesi** |

**26:80'de biçim kırılıyor ama fâsıla eki sürüyor:** `يَهْدِينِ` · `يَسْقِينِ` ·
`يَشْفِينِ` — üçü de `ـِينِ`. Zincir 26:81-82'de sürüyor, **kapatılamaz.**

## "İKİ AYRI KÖK, AYNI ANLAM ALANI" — SÛRE 26'DA ÜÇÜNCÜ VAKA (aday 652)

| ayetler | kökler | ortak alan |
|---|---|---|
| 26:16 ↔ 26:18 | `ربب` *(rab)* / `ربو` *(yetiştirme)* | terbiye |
| 26:42 ↔ 26:58 | `قرب` *(yakınlık)* / `قوم` *(makam)* | konum |
| 26:26 ↔ 26:76 | `أول` *(evvel)* / `قدم` *(öne geçme)* | öncelik |

Üçüncüsünde **tamlama yapısı da aynı**: `ءَابَآئِكُمُ ٱلْأَوَّلِينَ` /
`ءَابَآؤُكُمُ ٱلْأَقْدَمُونَ`. Kalıp iddiası kuralı gereği sûre 80/227'de
kapatılmıyor; tur sonu: kavram katalogunda "anlam alanı" üst düzeyi var mı?

## ADAY 602'NİN EN YALIN GÖSTERİMİ (aday 654)

**26:62 ↔ 26:78** — aynı kök (`هدي`), aynı `ـِينِ` eki, aynı fâsıla konumu, iki
elçi. **26:62 ★★★ (rab z=3,23), 26:78 yıldızsız.** Fark içerikten değil, ayette
`رَبّ` bulunup bulunmamasından.

## DİĞER

- **`رَبَّ ٱلْعَٰلَمِينَ` dört konuşan dört işlev** (aday 653): elçilik iddiası
  (26:16) → soru (26:23) → ikrar (26:47) → istisna (26:77). Üçü ★★★ ve üçünde de
  kaynak rab oranı. Ayrıca **ikinci sayı uyumsuzluğu**: 26:77'de `عَدُوّ` tekil,
  gönderge çoğul (aday 611'e ek).
- **`نفع`/`ضرر` çifti okumada üçüncü kez** (aday 649): 25:3 → 25:55 → 26:73;
  çift dikey ölçümde **iki yönden** bağlı, donmuş kalıp adayı.
- **`صنم`/`عبد` çifti de iki yönden bağlı** (aday 647): 26:70'te `عبد` ▸sonra
  `صنم` ×16,6, 26:71'de `صنم` ▸önce `عبد` ×14,1. **"İki yönlü zenginleşme"
  437'nin (donmuş kalıp) tanımı için bir ölçüt olarak sınanacak.**
- **26:70 ↔ 26:75 beş ayetlik bölüt halkası** (aday 651): soru aynı fâsılayla
  açılıp aynı fâsılayla kapanıyor.
- **Üç ayet hiç i'râb etiketi almıyor** (26:72, 73, 75 — aday 657); okumada ilk
  kez küme hâlinde. 548'in (fiilsiz ayet) karşıtı bir ölçüm; ikisi birlikte
  "ayet bileşim tipi" alanını gerektiriyor.
- **529 kümesine iki yeni vaka:** 26:71 `ظلل` (korpusta gölge, burada sürdürme)
  ve 26:80 `مرض` (korpusta kalp hastalığı/nifak, burada bedensel hastalık).
- **Blok bilançosu:** ★★★ 1 · ★★ 0 · ★ 0 · **9 yıldızsız — okumada görülen en az
  yıldızlı on ayetlik blok.** 26:79 (yedirme, içirme) ve 26:80 (hastalık, şifa)
  çıpa taşıyabilecek ayetler ve ikisi de yıldızsız.

### DEVAM NOKTASI

**Sûre 26, ayet 81.** Blok 26:81-90 (on ayet). Beklenenler: 26:81-82 `ٱلَّذِى`
zincirinin son iki halkası (öldürme-diriltme, bağışlanma umudu) — **aday 655
kapanabilir** · 26:83-89 İbrâhîm'in duası · **26:89 ★★★** (`قَلْبٍ سَلِيمٍ`) ·
26:89'da sûrenin ilk Allah lafzı bölgesi başlıyor (lafızlı ayetler 89'dan sonra).


### 26:81-90 EKİ — SÛRE 26 90/227, ADAYLAR 658-666

Okunan ayet **1802 → 1812** (korpusun %29,1'i). `turkce_denetim.py` → **0**
(11 ihlâl). `anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl, diff = 0**
(21659). Kök tablosu **994 → 995** (`لحق`). Bağlar `AF_suara` 64 → **75**.

## ★★ AKTÖR TABLOSU TANISI — 462/638'E ÇÖZÜM ÖNERİSİ (aday 666)

Dört vaka tabloyu teşhis ediyor:

| ayet | biçim | tabloya giriyor mu |
|---|---|---|
| 25:24 `أَصْحَٰبُ ٱلْجَنَّةِ` | marife | **evet** |
| 26:57 `جَنَّٰتٍ` | çoğul nekre | hayır |
| 26:85 `جَنَّةِ ٱلنَّعِيمِ` | tamlama başı | hayır |
| 26:90 `ٱلْجَنَّةُ` | marife | **evet** |

**Tablonun ölçütü BELİRLİLİK.** Yani 638'de "tutarsız" dediğim davranış aslında
**tutarlı ama yanlış tanımlı**. Onarım: aktör tanımı belirlilik yerine
**lemma + gönderge** üzerinden kurulmalı. Sınama kümesi bu dört vakayla hazır.

## ★ `ٱلَّذِى` ZİNCİRİ KAPANDI — İKİ KIRILMA, İKİ FARKLI YERDE (aday 655)

Zincir beş halkalı: 26:78 · 79 · **80** · 81 · 82.

- **Biçim ortada kırılıyor:** 26:80 `ٱلَّذِى` değil, şart cümlesi
  (`وَإِذَا مَرِضْتُ`) — zincirin **tam merkezinde**.
- **Ses sonda kırılıyor:** 26:78-81'de dört kez `ـِينِ` (fiil + nûn-i vikâye),
  26:82'de `ٱلدِّينِ` bir **isim**.

Sûre 25 ile fark (aday 527): orada `ٱلَّذِى` göndergesi **üçüncü şahsa** aitti ve
lafız/Rab **yerine** geçiyordu; burada **birinci şahsın kendi Rabbine** ait ve
bir konuşmanın içinde.

## ★ SÛRENİN İLK ALLAH LAFZI 26:89'DA (aday 665)

| sûre | ilk lafız | göreli konum | lafızsız açılış |
|---|---|---|---|
| 25 | 25:17 | 0,22 | 16 ayet |
| 26 | **26:89** | **0,39** | **88 ayet** |

Sûre 26'nın **on üç lafız tokeninin hepsi 89'dan sonra** — lafız sûrenin ikinci
yarısına sıkışmış. 527'nin uyarısı aynen geçerli: iki sûre de düşük-A (0,26x ve
0,28x); **null, taban oranı ile gerçek gecikmeyi ayırmalı.**

## ★ "KARŞITLI KÖK TEK UÇLU KULLANIM" — DÖRDÜNCÜ VAKA VE OTOMATİKLEŞTİRİLEBİLİR TANIM (aday 664)

26:88'de `نفع` *(fayda)* okumada dördüncü kez ve **ilk kez `ضرر` *(zarar)*
olmadan**; yerine `مال`/`بنون` ikilisi. Önceki vakalar: 25:6 `سرر` (karşıtı
`علن` yok), 25:46 `يسر` (karşıtı `عسر` yok), 26:60 `شرق` (karşıtı `غرب` yok).

**Ölçülebilir tanım:** dikey ölçümde ▸önce ya da ▸sonra listesinde kökün
anlamsal karşıtı yüksek katla görünüyorsa ve ayette o karşıt yoksa → **tek uçlu
kullanım**. Bu tanım **otomatikleştirilebilir**; tur sonu işi: korpus çapında
envanter.

## KISSALAR ARASI YAPI EŞLEŞMESİ — İKİNCİ VE ÜÇÜNCÜ VAKA

- **26:21 ↔ 26:83** (aday 660): `وهب` + `حكم` çifti, **aynı sıra ve aynı yapı**
  (fiil + `لِى` + `حُكْما` + `وَ` + fiil + çoğul); Mûsâ'da gerçekleşmiş (PERF),
  İbrâhîm'de istenen (IMPV).
- **26:13 ↔ 26:84** (aday 661): `لسن` yetersizlikten isteğe.
- 654 (`هدي`) ile birlikte **üç vaka**. Kalıp iddiası kuralı: yedi kıssanın
  ikisi okundu.

## `esit_yakin` ÖNERİSİNE BEŞİNCİ VE EN ZORLAYICI SINAMA VAKASI (aday 659)

**26:51 ↔ 26:82** — üç ortak kök (`طمع` + `غفر` + `خطأ`) ve aynı yapı, ama ortak
parça **bitişik değil**. `esit_yakin` "n−1 kelime ortaklığı" olarak tanımlanırsa
**bu vakayı da kaçırır**; **üçüncü bir alan gerekebilir: "kök örtüşmesi + yapı
özdeşliği".**

## DİĞER

- **`موت`/`حيي` çifti dört yapı** (aday 658): iki ayrı nesne → tek eylem → tek
  gönderge → sıralı iki eylem. Çift dikey ölçümde iki yönden bağlı ama dört
  geçiş dört farklı yapıda — **"iki yönlü zenginleşme" donmuş kalıp göstergesi
  olmayabilir**; 647 ile çelişiyor, ikisi birlikte sınanacak.
- **529 kümesi sûre 26'da yedi vakaya çıktı:** `طلق` · `رجو` · `عين` · `ظلل` ·
  `مرض` · `بعث` · `لسن`.
- **Blok bilançosu:** ★★★ 2 (26:83, 90) · ★★ 2 (26:87, 89) · ★ 0 · 6 yıldızsız.
  Kaynaklar rab ×1 · pas ×2 · allah ×1 — hiçbiri içerikten, hiçbirinde çıpa yok.
  Sûre 26'nın okunan 90 ayetinde ★★★ **17**; çıpası olan tek ★★★ hâlâ 26:63.

### DEVAM NOKTASI

**Sûre 26, ayet 91.** Blok 26:91-100 (on ayet). Beklenenler: 26:91-102 mahşer
sahnesi ve tapılanlarla tartışma · **26:94 ★★★** (hapaks `كبكب` *(tepetaklak
atma)*) · 26:97-98 `تَٱللَّهِ` yemini — **sûrede QASEM sıfır ölçülmüştü;
denetlenecek** · 26:98'de `رَبِّ ٱلْعَٰلَمِينَ` terkibinin altıncı geçişi.


### 26:91-100 EKİ — SÛRE 26 100/227, ADAYLAR 667-676

Okunan ayet **1812 → 1822** (korpusun %29,2'si). `turkce_denetim.py` → **0**
(4 ihlâl; **biri GERİYE DÖNÜK: 14:48**, `برز` kökü eklenince açığa çıktı).
`anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl, diff = 0** (21661).
Kök tablosu **995 → 997** (`برز` · `كبكب`). Bağlar `AF_suara` 75 → **83**.

## ★★ ADAY 443 DOĞRULANDI — QASEM ETİKETİ EKSİK (aday 672)

**26:97: `تَٱللَّهِ إِن كُنَّا لَفِى ضَلَٰلٍۢ مُّبِينٍ`** — ayet `تَٱللَّهِ`
yemin edatıyla açılıyor ama `fig` alanında **QASEM yok**; sûre 26 makro
profilinde de **"QASEM sıfır"** yazılmıştı. **Yanlış.**

**Bu, makro sayım tutarsızlığının ikinci vakası** (birincisi 26:74'te IDRAB,
aday 650). İki tutarsızlık birlikte: **makro profil üretiminin `fig` sayımı
bütünüyle denetlenmeli** — bu, benim ürettiğim makro profillerin güvenilirliğini
etkiliyor. Aday 443 artık kapanabilir durumda; sınama vakası bulundu.

## ★★ AKTÖR TABLOSU — 666'NIN TANISI DÜZELTİLDİ (aday 667)

666'da "ölçüt belirlilik" demiştim. **26:91'de `ٱلْجَحِيمُ` de marife ama
tabloya girmiyor.** Demek ki ölçüt belirlilik **değil**, **adlı aktör listesi**:
`جَنَّة` ve `جَهَنَّم` listede, `جَحِيم` değil. Kendi tanımı düzelttim.

## ★ OKUMADA EN SİMETRİK AYET ÇİFTİ (aday 667)

**26:90 ↔ 26:91**, bitişik ve ters kutup:

| | 26:90 | 26:91 |
|---|---|---|
| | `وَأُزْلِفَتِ ٱلْجَنَّةُ لِلْمُتَّقِينَ` | `وَبُرِّزَتِ ٱلْجَحِيمُ لِلْغَاوِينَ` |
| n | 3 | 3 |
| fiil | tek, **edilgen**, oran 1,00 | tek, **edilgen**, oran 1,00 |
| pas z | **5,38** | **5,38** |
| yıldız | ★★★ | ★★★ |

**`esit` yakalamıyor, `esit_yakin` de yakalamaz** (ortak kelime yok). Bu vaka
659 ile birlikte **üçüncü bir alan gerektiriyor: "yapı özdeşliği"** (sözdizimsel
iskelet eşleşmesi).

## ★ DİKEY KATMAN BİR ÖRÜNTÜYÜ DÜŞÜRDÜ (adaylar 669, 675)

Blokta "mahşerde işe yaramayan üç şey" görünüyor: fayda (26:88), yardım (26:93),
şefaat (26:100). **Ama dikey ölçüm üçünün de `مِن دُونِ ٱللَّهِ` terkibine bağlı
olduğunu gösteriyor:** `دون` ▸sonra şefaat ×9,3 · zarar ×7,6 · `نفع` ×6,7.
Yani **ölçüt çeşitliliği sûreye özgü bir kurgu değil, korpus tabanının
yansıması** — ve bu, 649'un (`نفع`/`ضرر` üçlüsü) yorumunu da zayıflatıyor.

**Tur sonu işi:** "dikey ölçümün düşürdüğü örüntü" vakalarının envanteri — bu,
dikey katmanın değerini ölçmenin bir yolu.

## DİĞER

- **`جمع` sûrede yedi geçiş yedi biçim** (aday 671): edilgen fiil → ism-i fâil →
  ACC pekiştirme → sıfat → tesniye isim → ACC pekiştirme → NOM pekiştirme.
- **`سوي` bab sınırında anlam ayrımı** (aday 673): 25:59 bab VIII "istivâ",
  26:98 bab II "denk kılma". **569/584'ün bab önerisine dördüncü destek.**
  Sınama kümesi: `صرف` · `قرن` · `رجو` · `طلق` · `سوي` (bab yeter) ve `جنن`
  (lemma gerekli) — **iki katmanlı onarım doğrulandı.**
- **`ضلل` sorumluluk zinciri tamamlandı** (aday 674): 25:17 çatı sorusu →
  25:29 fâil şeytan → **26:99 fâil insanlar**, HASR ile.
- **26:94 okumada üçüncü iki kaynaklı ★★★** ve ilk kez iki kaynak da uçta
  (hapaks 3,38 + pas 5,38).
- **Blok bilançosu:** ★★★ 3 · ★★ 2 · ★ 1 · 4 yıldızsız — **okumada en yıldızlı
  on ayetlik blok**. Ama **altı yıldızlı ayetin altısı da n≤7, üçü n≤4; blok
  ortalaması n=4,4** (sûre ortalaması 5,81'in altında) — kısa ayet yanlılığının
  doğrudan sonucu gibi görünüyor (aday 602/624).
- **Geriye dönük ihlâl üçüncü veri noktası** (aday 676): `برز` n=9 ve 14:48'de
  ihlâl açığa çıkardı. Yeni gözlem: ihlâl, kökün metinde **kök adıyla** anılıp
  anılmamasına bağlı; kavram adıyla anılanlar tetiklemiyor.

### DEVAM NOKTASI

**Sûre 26, ayet 101.** Blok 26:101-110 (on ayet). Beklenenler: 26:101-104 İblîs
ordularının sözünün kapanışı ve **26:103-104 nakarat çiftinin üçüncü geçişi** ·
26:105-110 **Nûh kıssası açılıyor** — sûrenin üçüncü kıssası · **26:107 ve 26:109
iki yeni nakarat kümesinin ilk geçişleri** (`إِنِّى لَكُمْ رَسُولٌ أَمِينٌ` ve
`وَمَآ أَسْـَٔلُكُمْ عَلَيْهِ مِنْ أَجْرٍ`) · 26:108 ve 26:110'da
`فَٱتَّقُوا۟ ٱللَّهَ وَأَطِيعُونِ` nakaratı — **aday 626 kapanabilir.**


### 26:101-110 EKİ — SÛRE 26 110/227, ADAYLAR 677-685

Okunan ayet **1822 → 1832** (korpusun %29,4'ü). `turkce_denetim.py` → **0**
(1 ihlâl). `anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl, diff = 0**
(21662). Kök tablosu **997 → 998** (`كرر`). Bağlar `AF_suara` 83 → **90**.

## ★★★ ADAY 606'NIN TAM ÖLÇÜMÜ (aday 683) — DÖRT ÖLÇÜM BİRDEN ŞİŞMİŞ

Sayım yapıldı. Sûre 26'nın **41 ★★★ ayetinin 16'sı iki nakarattan** geliyor:

| nakarat | temsil | ayet | z kaynağı |
|---|---|---|---|
| `وَإِنَّ رَبَّكَ لَهُوَ ٱلْعَزِيزُ ٱلرَّحِيمُ` | 26:9 | **8** | rab z=3,94 |
| `فَٱتَّقُوا۟ ٱللَّهَ وَأَطِيعُونِ` | 26:108 | **8** | **allah z=6,14** |

`allah z=6,14` **okumada görülen en yüksek Allah z'si** — n=3, tek lafız,
oran 0,33. Nakaratsız ★★★ sayısı **25**.

**DÜZELTİLMİŞ PAY: (41−14)/227 = %11,9**, makro profildeki **%18,1 değil.**

Ve bağımsızlık ihlâli **yalnız yıldızda değil** (aday 679): 26:67 ve 26:103'te
iltifât yönü **ikisinde de 1>3** — nakaratın iltifâtı da sayılıyor. **Sûre 26'nın
dört ölçümü de şu an şişmiş: ★★★ payı, iltifât sayısı (15), esmâ token sayısı
(51), `esit` ayet sayısı (44).** Tur sonunda dördü de nakarat düzeltmesiyle
yeniden hesaplanacak. **Aday 602'nin korpus taraması (r=−0,367) da yeniden
koşulacak** — öteki sûrelerin nakarat düzeltmesi yapılmadı.

## ★★ ESMÂ TABLOSUNA KESİN TANI (aday 682)

**26:107: `إِنِّى لَكُمْ رَسُولٌ أَمِينٌ`** — `أَمِين` *(güvenilir)* esmâ
**sayılmıyor** ve bu **doğru** (gönderge elçi). Ama **aynı kökten (`أمن`)
`مُؤْمِن` on beş kez esmâ sayılıyor ve on beşi de artefakt.**

**Tanı: tablo gönderge denetimi YAPMIYOR, yalnız lemma listesi eşleştiriyor.**
`مُؤْمِن` listede, `أَمِين` değil. Bu, 629'un hipotezini (26:44'te "doğru sonuç
yanlış sebeple") **doğruluyor**. Onarım iki katmanlı olmalı: lemma listesi +
gönderge denetimi. Sınama kümesi dört vakayla hazır.

## ★ ADAY 626 KAPANDI (aday 684)

`أجر` *(ücret, karşılık)* üç geçiş üç işlev: **reddetme** (25:57, istisna bir
EYLEM) → **isteme** (26:41) → **reddetme** (26:109, istisna bir ADRES ve kök
ikilemesiyle). **Ama** dikey ölçüm ayetin üç ana kökünün de (`سأل`, `أجر`,
`علم`) korpusta birbirine bağlı olduğunu gösteriyor — "elçinin ücret reddi" bir
sûre özelliği değil, **korpus kalıbı** (669/675 ile aynı ders).

## ★ SÛRENİN MİMARİSİ ÖNCEDEN ÖLÇÜLEBİLİR HÂLE GELDİ — ÖN-KAYIT (aday 685)

**26:108-109-110: üç ardışık ayetin üçü de nakarat, örgü A-B-A.** Kıssa açılış
formülü altı öğeli: (i) tekzip cümlesi · (ii) `أَلَا تَتَّقُونَ` · (iii)
`إِنِّى لَكُمْ رَسُولٌ أَمِينٌ` · (iv) `فَٱتَّقُوا۟ ٱللَّهَ وَأَطِيعُونِ` ·
(v) `وَمَآ أَسْـَٔلُكُمْ … أَجْرٍ` · (vi) (iv) tekrar.

**ÖN-KAYIT (476/545 dersi uygulanarak, okunmadan önce yazıldı):** kalan dört
kıssanın (Hûd 26:123-, Sâlih 26:141-, Lût 26:160-, Şuayb 26:176-) dördünde de
(i), (iii), (iv), (v) bulunacak; **(ii) `أَلَا تَتَّقُونَ` Lût ve Şuayb'da
bulunmayabilir** (`esit` listesinde 26:106 için eşleşme yok, kalıp tekil).
**Tahmin tutmazsa açıkça yazılacak.**

## DİĞER

- **`حمم` — 529 kümesine sûre 26'nın sekizinci vakası** (aday 677): korpusta
  ezici çoğunlukla "kaynar su", 26:101'de "candan dost".
- **`كرر` dikey ölçümde iki liste de boş** (aday 678). Yeni ölçüm sorusu:
  komşuluğu tamamen boş çıkan kökler kaç tane, ve n≤10'da dikey satırı bilgi
  taşıyor mu? **Bu, dikey katmanın sınırını tanımlar** (aday 435 kümesine ek).
- **Üçüncü sayı uyumsuzluğu** (aday 680): 26:105'te `قَوْم` tekil, nesne
  `ٱلْمُرْسَلِينَ` çoğul.
- **25:37 ↔ 26:105** (aday 680): aynı tekzip formülü — sûre 25'te kıssanın
  **tamamı** (tek ayet), sûre 26'da **açılışı** (on sekiz ayet). 607 ile aynı
  yönde: sûre 25 sıkıştırıyor, sûre 26 yayıyor.
- **Blok bilançosu:** ★★★ 3 · ★★ 0 · ★ 1 · 6 yıldızsız. **Üç ★★★ ayetin üçü de
  nakarat.** Sûre 26'nın okunan 110 ayetinde ★★★ **23**; çıpası olan tek ★★★
  hâlâ 26:63.

### DEVAM NOKTASI

**Sûre 26, ayet 111.** Blok 26:111-120 (on ayet). Beklenenler: 26:111-122 Nûh
kıssasının gövdesi ve kapanışı · **26:117 ★★★** · 26:118-119 gemi ve boğulma
sahnesi — **çıpa tanımı için sınama alanı** · 26:121-122 nakarat çiftinin
DÖRDÜNCÜ geçişi · 26:123'ten itibaren **aday 685'in ön-kaydı sınanmaya
başlayacak** (Hûd kıssası).


### 26:111-120 EKİ — SÛRE 26 120/227, ADAYLAR 686-695

Okunan ayet **1832 → 1842** (korpusun %29,5'i). `turkce_denetim.py` → **0**
(5 ihlâl; **biri GERİYE DÖNÜK: 11:30**, `طرد` kökü eklenince açığa çıktı).
`anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl, diff = 0** (21663).
Kök tablosu **998 → 999** (`طرد`). Bağlar `AF_suara` 90 → **101**.

## ★★ ADAY 682'YE EN TEMİZ KANIT (aday 690)

**Aynı sözdizimsel yapıda iki ayet, iki farklı hüküm:**

| ayet | yapı | sıfat | esmâ sayılıyor mu | doğru mu |
|---|---|---|---|---|
| 26:107 | `إِنِّى لَكُمْ رَسُولٌ أَمِينٌ` | `أَمِين` | **hayır** | doğru |
| 26:115 | `إِنْ أَنَا۠ إِلَّا نَذِيرٌ مُّبِينٌ` | `مُبِين` | **evet** | **yanlış** |

**İkisinin de göndergesi elçi.** Fark yalnız **lemma listesi**: `مُبِين` listede,
`أَمِين` değil. **Gönderge denetiminin hiç çalışmadığının en temiz gösterimi.**

## ★★ ADAY 621'İN SINAMA KÜMESİ TAMAMLANDI — ÜÇ ALAN GEREKİYOR (aday 695)

**26:66 ↔ 26:120:** `ثُمَّ أَغْرَقْنَا ٱلْءَاخَرِينَ` / `ثُمَّ أَغْرَقْنَا
بَعْدُ ٱلْبَاقِينَ` — ortak üç öğe, değişen nesne ve **tek zarf** (`بَعْدُ`).
`esit` yakalamıyor. Küme artık tam:

| alan | yakalanan | kaçırılan |
|---|---|---|
| **esit_tam** (mevcut) | 26:32-33=7:107-108 · 26:47-48=7:121-122 · 26:66=37:82 | — |
| **esit_yakin** (n−1 kelime) | 25:66≈25:76 · 26:64≈26:66 · 26:66≈26:120 · 25:9=17:48 (imlâ) | — |
| **esit_yapi** (sözdizimsel iskelet) | 26:90≈26:91 · 26:51≈26:82 · 26:36≈26:53 | — |

**Üç alan gerekiyor** — ve sınama vakalarının hepsi elde.

## ★★ DİKEY KATMANIN SINIRI GÖRÜNDÜ (adaylar 689, 694)

**Blokta iki yeni "boş komşuluk" vakası:** 26:114 `طرد` (n=5) ve önceki blokta
26:102 `كرر` (n=6) — ikisinde de ▸önce ve ▸sonra listeleri **boş**. Okumada boş
komşuluklu kökler: `طود` · `شرذم` · `كبكب` · `ضير` · `عبأ` · `لحق` · `كرر` ·
`طرد` — **hepsi n≤6.**

Ve ters uçta: **26:119 `شحن` (n=3) ▸önce `فلك` ×301,6 — okumada görülen en
yüksek tek komşuluk katı.** Üç geçişin üçü de aynı terkipteyse **kat değeri
şişkin ve istatistiksel olarak anlamsız.**

**Tur sonu zorunlu:** (a) korpus çapında n≤6 kök sayısı ve dikey satırının bilgi
içeriği; (b) zenginleşme katının seyrek köklerde anlamlılığı. **Bu, dikey
katmanın sınırını tanımlar** (aday 435 kümesine ek).

## ★ SÛRENİN ADINI VEREN KÖK — VE KORPUSTA AZINLIK ANLAMI (aday 688)

**26:113'te `شعر` ilk kez geçiyor ve "farkında olma" anlamında** (`لَوْ
تَشْعُرُونَ`). Sûrenin adı `ٱلشُّعَرَآء` *(şairler)* ve o lemma **26:224'te**
gelecek. Dikey ölçüm ▸önce `بغت` *(ansızın gelme)* ×85,3 · `مكر` *(tuzak)*
×21,5 veriyor — korpusta ağırlıkla "farkına varmadan"; **"şair" anlamı
azınlık.** 529 kümesine sûre 26'nın dokuzuncu vakası.

**Uyarı:** sûre adları metnin kendisinden değil sonradan verilmiş olabilir; bu
ölçüm metin içi değil, **ad-metin ilişkisi** hakkında ve o ilişkinin tarihi bu
projede **test dışı.**

## DİĞER

- **"İki kıssada aynı kalıp" sınıfı ALTI vakaya çıktı:** `هدي` (654),
  `وهب`+`حكم` (660), `لسن` (661), tehdit kalıbı (691), `رَبِّ`+tekzip (692),
  `نجو`+`وَمَن مَّعَهُ` (694). **Ama üçünde dikey ölçüm kalıbın korpus tabanından
  geldiğini gösteriyor** — 669/675/684 dersi; **her vaka için dikey denetimi
  koşulmalı** (tur sonu zorunlu).
- **26:118 okumada bir ayette iki ayrı kökün birden ikilendiği ilk yer**
  (`فتح` ×2 ve `بين` ×2); `defter.json`'un `ikile` alanı bunu **doğru gösteriyor**.
- **`تبع` sûrede dört değer üç çatı** (aday 686): niyet → uyarı → gerçekleşme →
  **kusur**.
- **Blok bilançosu:** ★★★ 1 (26:117) · ★★ 1 (26:113) · ★ 0 · 8 yıldızsız.
  Kaynaklar rab ×2 — ikisi de eksen oranından. **26:119 (dolu gemi) ve 26:120
  (boğulma) çıpa taşıyabilecek ayetler ve ikisi de yıldızsız.**

### DEVAM NOKTASI

**Sûre 26, ayet 121.** Blok 26:121-130 (on ayet). Beklenenler: 26:121-122
nakarat çiftinin **dördüncü** geçişi · **26:123'ten itibaren Hûd kıssası ve
ADAY 685'İN ÖN-KAYDI SINANMAYA BAŞLIYOR** — tahmin: (i), (iii), (iv), (v)
bulunacak, (ii) `أَلَا تَتَّقُونَ` bulunabilir · 26:128 ★★★ (hapaks `ريع`
*(yüksek yer, tepe)*) · 26:126 ve 26:131'de dördüncü nakaratın geçişleri.


### 26:121-130 EKİ — SÛRE 26 130/227, ADAYLAR 696-700

Okunan ayet **1842 → 1852** (korpusun %29,7'si). `turkce_denetim.py` → **0**
(1 ihlâl). `anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl, diff = 0**
(21665). Kök tablosu **999 → 1001** (`بطش` · `ريع`). Bağlar `AF_suara` 101 → **106**.

## ★★ ÖN-KAYIT SINAMASI — İLK TUR GEÇTİ (aday 696)

Tahmin 26:110'da, **kıssa okunmadan önce** yazılmıştı. Hûd kıssası (26:123-):

| öğe | ayet | var mı |
|---|---|---|
| (i) tekzip cümlesi | 26:123 | ✓ |
| (ii) `أَلَا تَتَّقُونَ` | 26:124 | ✓ |
| (iii) `إِنِّى لَكُمْ رَسُولٌ أَمِينٌ` | 26:125 | ✓ |
| (iv) `فَٱتَّقُوا۟ ٱللَّهَ وَأَطِيعُونِ` | 26:126 | ✓ |
| (v) `وَمَآ أَسْـَٔلُكُمْ … أَجْرٍ` | 26:127 | ✓ |
| (vi) (iv) tekrar | 26:131 | ✓ |

**Altı öğenin altısı da var.** Ama tahminin **ayırt edici kısmı** şuydu: "(ii)
Lût ve Şuayb'da bulunmayabilir". Hûd için belirsiz bırakmıştım. **Asıl sınama
Lût (26:160-) ve Şuayb (26:176-) kıssalarında** — sonuç ne olursa olsun açıkça
yazılacak (476/545 dersi).

Ayrıca ölçülebilir bir `esit` boşluğu: (i) ve (ii) öğeleri Nûh'unkiyle **birebir
aynı yapıda** ama `esit` yakalamıyor — tek fark kavim/elçi adı. Aday 621'in
`esit_yakin` önerisine **yedinci ve sekizinci** sınama vakası.

## ★★ NAKARAT ŞİŞMESİ — DÖRT ÖLÇÜMÜN DE SAYIMI TAMAMLANDI (aday 700)

| ölçüm | ham | nakarat payı | bağımsız |
|---|---|---|---|
| ★★★ payı | 41 (%18,1) | 16 | **25 (%11,9)** |
| esmâ token | 51 | **≥22** | ≈29 |
| iltifât | 15 | ≥4 (tek nakarattan) | ≤11 |
| `esit` ayet | 44 | nakarat kümeleri zaten üretiyor | çok daha düşük |

Birinci nakarat altı ayette ve **altısında da `مُؤْمِن` esmâ sayılıyor**; ikinci
nakarat sekiz ayette ve **on altı esmâ tokeni** üretiyor. **Sûre 26'nın makro
profili bütünüyle nakarat düzeltmesiyle yeniden yazılacak** — ve bu, sûre 55
(er-Rahmân) gibi sûreler için de geçerli olacak.

## ★★ 529 KÜMESİNE OKUMADAKİ EN SIK KÖK VAKASI (aday 697)

**26:128'de `أيي` "yapı, anıt, işaret" anlamında** — kök korpusta **597
geçişli** ve ezici çoğunlukla "ilâhî âyet". Dikey satırı korpus anlamını
getiriyor. Ve **aynı sûrede aynı kök nakaratta "ilâhî âyet" anlamında** (26:8,
67, 103, 121).

**Bu, bab girdisi önerisinin (569/584/673) yetmeyeceğini gösteriyor:** `أيي` bir
isim kökü, bab ayrımı yok — ve **lemma da aynı** (`ءَايَة`); ayrım yalnız
bağlamdan geliyor. **Üçüncü katman gerekebilir: bağlam-duyarlı anlam ayrımı.**
Sınama kümesi: `أيي` (aynı lemma iki anlam) · `جنن` (üç lemma üç anlam) ·
`صرف` (iki bab iki anlam).

## DİĞER

- **`صنع` korpus yatağı gemi yapımı** (aday 698): dikey satırı ▸sonra `فلك`
  ×40,2 veriyor ve gemi kıssası **dokuz ayet önce** bitti — okuyucuyu yanlış bağa
  çekiyor. **Tur sonu: "dikey satırının yanılttığı vakalar" envanteri** —
  675/684'ün karşıtı.
- **26:128-130'da üç ardışık ayette 2MP dışında şahıs yok** (aday 699);
  26:54-56 ile aynı sınıf, sûre 26'nın karakteristik özelliği gibi.
- **26:130'da `بطش` ikileniyor ama mef'ûl-i mutlak DEĞİL** — fiil + fiil + hâl;
  MM etiketleme işine (559/572) bir **sınır vakası**.
- **`هود` kökü 26:124'te özel ad ama dikey ölçümü ▸sonra `صبأ` ×226,4 ·
  Hristiyan ×196,2 veriyor** — korpusta ezici çoğunlukla "Yahudi"; kök düzeyi
  komşuluk özel adı hiç ayırmıyor (529, sûre 26'nın onuncu vakası).
- **Blok bilançosu:** ★★★ 3 (26:122, 126, 128) · ★★ 0 · ★ 1 · 6 yıldızsız.
  **Üç ★★★ ayetin ikisi nakarat**, üçüncüsü hapaks kaynaklı. Sûre 26'nın okunan
  130 ayetinde ★★★ **27**; çıpası olan tek ★★★ hâlâ 26:63.

### DEVAM NOKTASI

**Sûre 26, ayet 131.** Blok 26:131-140 (on ayet). Beklenenler: 26:131 dördüncü
nakaratın dördüncü geçişi · 26:132-135 Hûd'un ikinci konuşması (nimet sayımı) ·
26:139-140 nakarat çiftinin **beşinci** geçişi · **26:141'den itibaren Sâlih
kıssası ve ön-kaydın ikinci sınaması.**


### 26:131-140 EKİ — SÛRE 26 140/227, ADAYLAR 701-707

Okunan ayet **1852 → 1862** (korpusun %29,9'u). `turkce_denetim.py` → **0**
(1 ihlâl). `anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl, diff = 0**
(21665). Kök tablosu 1001'de sabit. Bağlar `AF_suara` 106 → **113**.

## ★★★ NAKARAT ÖLÇÜMÜ EKSİK ÖLÇÜYOR (aday 707) — 683/700'Ü DÜZELTİYOR

Birinci nakarat `nakarat` alanında **altı** ayette işaretli (26:8, 67, 103, 121,
174, 190 — hepsi n=8). **Ama korpus taraması `أَكْثَرُهُم`'ü dokuz ayette
buluyor:**

| ayet | n | nakarat alanı | durum |
|---|---|---|---|
| 8, 67, 103, 121, 174, 190 | 8 | **6** | standalone |
| **139, 158** | **10** | **0** | **GÖMÜLÜ** (başına `فَكَذَّبُوهُ فَأَهْلَكْنَٰهُمْ` eklenmiş) |
| 223 | 4 | 0 | farklı yapı |

**Nakarat ölçümü yalnız tam ayet eşleşmesini sayıyor; gömülü tekrarı kaçırıyor.**
Ve `esit` alanı da boş. İki sonuç: (a) **nakarat düzeltmesi hesaplanandan daha
büyük olmalı**; (b) aday 621'in üç alanlı önerisine **dördüncü gereksinim:
gömülü/kısmi eşleşme**.

Ayrıca **nakarat çifti burada bozuluyor**: önceki dört konumda (26:8-9, 67-68,
103-104, 121-122) birinci nakarat ayrı bir ayetti; 26:139-140'ta gömülü.
**Ölçülebilir bir mimari kırılma.**

## ★★ 529'UN ÜÇÜNCÜ KATMANI ZORUNLU HÂLE GELDİ (adaylar 705, 704)

**26:137'de `خلق` "huy, âdet" anlamında** — kök korpusta **261 geçişli** ve
ezici çoğunlukla "yaratma"; dikey satırı yaratılış komşuluğunu getiriyor
(`مضغ` ×27,6 · meni ×27,6 · `علق` ×23,7) ve **bu ayetle ilgisi yok**.

26:128'in `أيي` vakasıyla (n=597) birlikte: **529 kümesinin en sık iki kökü ve
ikisinde de lemma aynı** — ayrım yalnız bağlamdan. Onarım katmanları:

| katman | çözdüğü | örnek |
|---|---|---|
| bab | çoğu vaka | `صرف` · `قرن` · `رجو` · `طلق` |
| lemma | isim-kalıplı çok anlamlılar | `جنن` |
| **bağlam** | **aynı lemma iki anlam** | **`أيي` · `خلق` · `سوي`** |

Ve `سوي` (aday 704) üçüncü geçişinde bir **isim** (`سَوَآء`) — bab önerisi orada
da yetmiyor. **Uyarı — onarım maliyeti:** bağlam-duyarlı ayrım elle etiketleme ya
da dış model gerektirir; bu, projenin "ölçüm araçları kendi kendine yeter"
ilkesini zorlar. **Envanter çıkarılmadan onarım kararı verilmeyecek.**

## ★ YENİ ÖLÇÜ TANIMI EKSİĞİ (aday 706)

26:138'de **edilgen ism-i mef'ûl** var (`مُعَذَّبِينَ`) ama fiil yok — **`pas`
sayacı bunu görmüyor.** Bu, aday 602/624'ün (pas kaynaklı ★★★) hesabını
etkiliyor: ism-i mef'ûl de sayılsaydı hangi ayetler yıldız alırdı? **Tanım
değişikliği yıldız dağılımını değiştirir; geriye dönük etkisi ölçülmeli.**

## ÖN-KAYIT — İKİNCİ GÖZLEM (aday 696'ya ek)

**Hûd kıssasında altı öğenin altısı tamamlandı** (26:131 = öğe vi). **Ama örgü
26:108-110'dakinden farklı:** orada üç ardışık nakarat (A-B-A), burada araya
Hûd'un üç suçlaması girdi (26:128-130). **Ön-kayıt öğelerin varlığını doğru
bildi, aralıklarını öngörmedi** — bu da kayda geçti.

## DİĞER

- **Nimet/kayıp tersliği** (aday 702): `جَنَّٰت وَعُيُون` **birebir aynı iki
  kelime**, 26:57'de kayıp, 26:134'te nimet (77 ayet arayla). `esit` yakalamıyor
  ve `esit_yakin` de kaçırır — **kısmi terkip eşleşmesi için ayrı eşik gerekli.**
- **`خوف` dördüncü geçişi ve ilk kez başkası için** (aday 703): üç geçiş Mûsâ
  kendisi için (`أَن` ve doğrudan mef'ûl), dördüncüsü Hûd başkası için (`عَلَىٰ`).
- **26:134 sûrenin okunan en kısa ayeti** (n=2, n z=−1,11; 26:60 ile aynı).
- **Blok bilançosu:** ★★★ 2 (26:131, 140) · ★★ 0 · ★ 0 · 8 yıldızsız. **İki ★★★
  ayetin ikisi de nakarat.** Sûre 26'nın okunan 140 ayetinde ★★★ **29**; çıpası
  olan tek ★★★ hâlâ 26:63.

### DEVAM NOKTASI

**Sûre 26, ayet 141.** Blok 26:141-150 (on ayet). Beklenenler: **Sâlih kıssası
ve ön-kaydın ikinci sınaması** — (i) 26:141, (ii) 26:142, (iii) 26:143,
(iv) 26:144, (v) 26:145, (vi) 26:150 · **26:146 ve 26:149 ★★★** · 26:147-148
nimet listesi (bahçeler, pınarlar, ekinler, hurmalıklar) — 26:134 ile
karşılaştırma · 26:149'da hapaks `فره` *(ustalık, şımarıklık)*.


### 26:141-150 EKİ — SÛRE 26 150/227, ADAYLAR 708-712 · **KORPUSUN %30'U OKUNDU**

Okunan ayet **1862 → 1872** (korpusun **%30,0**'ı — bir eşik). `turkce_denetim.py`
→ **0** (2 ihlâl). `anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl,
diff = 0** (21667). Kök tablosu **1001 → 1003** (`زرع` · `فره`). Bağlar
`AF_suara` 113 → **119**.

## ★★ ÖN-KAYIT SINAMASI 2 — SÂLİH'TE DE ALTI ÖĞE (aday 708)

(i) 26:141 · (ii) 26:142 · (iii) 26:143 · (iv) 26:144 · (v) 26:145 ·
(vi) 26:150 — **altısı da var.**

**Ve ön-kaydın öngörmediği bir alt kalıp çıktı:**

| kıssa | örgü |
|---|---|
| Nûh | **A-B-A** — üç ardışık nakarat (26:108-110) |
| Hûd | (iv) 26:126 → üç suçlama 26:128-130 → (vi) 26:131 |
| Sâlih | (iv) 26:144 → üç suçlama 26:146,148,149 → (vi) 26:150 |

**Hûd ve Sâlih aynı, Nûh farklı.** Ön-kayıt öğelerin varlığını doğru bildi ama
aralık yapısını öngörmedi — açıkça yazıldı. **Asıl sınama hâlâ Lût (26:160-) ve
Şuayb (26:176-)'da**, çünkü tahminin ayırt edici kısmı "(ii) orada
bulunmayabilir" idi.

## ★★ ESMÂ TABLOSUNUN GÖNDERGE DENETİMİ YAPMADIĞI KESİNLEŞTİ (aday 709)

Tek kök (`أمن`), üç lemma, üç hüküm — **ve üçünün de göndergesi insan:**

| lemma | token | esmâ sayılıyor mu | doğru mu |
|---|---|---|---|
| `مُؤْمِن` | 10 | **evet** | **hayır** (artefakt) |
| `أَمِين` | 3 | hayır | doğru |
| `ءَامِنِين` | 1 | hayır | doğru |

**Fark yalnız lemma listesi.** `مُؤْمِن` klasik esmâ listelerinde var
(el-Mü'min); tablo o listeden türetilmiş ve **korpus bağlamı hiç
denetlenmemiş** — aday 461'in orijinal savı doğrulandı. Onarım sınama kümesi bu
kökle tamamlandı.

## ★ 529'A UMUT VERİCİ BİR VAKA (aday 711)

**26:148'de `طلع` "hurma tomurcuğu" anlamında** ve dikey satırı **her iki anlamı
da gösteriyor**: ▸önce `نخل` *(hurma)* ×54,2 (ayetin anlamı) VE ▸sonra `شمس`
*(güneş)* ×32,9 (korpus baskın anlamı). **Önceki 529 vakalarında dikey satırı
yalnız baskın anlamı getiriyordu.**

Bu, otomatik tespit için bir ölçüt önerisi doğuruyor: **"iki uzak anlam alanı
aynı satırda görünüyorsa kök çok anlamlıdır."** Tur sonu: 529'un on üç vakasında
kaç tanesinde iki anlam da görünüyor — bu, 697/705'in "bağlam katmanı gerekli"
sonucunu **kısmen hafifletebilir**.

## ★ `esit` ALANININ DAVRANIŞINI EN NET GÖSTEREN ÖRNEK (aday 710)

`جَنَّٰتٍ وَعُيُونٍ` sûrede **üç geçiş, iki işaret**: 26:57 kayıp, 26:134 nimet,
26:147 nimet. **26:147'yi `esit` 44:52 ile yakalıyor** (sûre dışı, tam ayet) ama
**26:134 ile eşleşmeyi kaçırıyor** (sûre içi, bir kelime farkı). Aday 621'e
onuncu sınama vakası.

Ve bir ek gözlem: dikey ölçüm `جنن` için `عين`'i **vermiyor** — yani çift dikey
katmanda **görünmüyor**; terkip eşleşmesi dikey katmandan **bağımsız bir bilgi**
taşıyor.

## DİĞER

- **Kıssa elçilerinin adları kök düzeyinde cins ada karışıyor** (529, sûre 26'nın
  on üçüncü vakası): 26:124'te `هود` ▸sonra `صبأ` ×226,4 · Hristiyan ×196,2;
  26:142'de `صلح` ▸önce `عمل` ×10,9 · `توب` ×5,8 ("sâlih amel" bağlamı).
- **Yapı suçlaması iki kavimde** (aday 712): Âd tepelere işaret dikiyor,
  Semûd dağlardan ev yontuyor; ortak biçim 2MP muzâri + yapı nesnesi + tarz.
  Uyarı: `نحت` ▸sonra dağ ×107,4 · ev ×64,4 — **terkip ayete özgü değil.**
- **26:148 sûrenin ilk bitki betimlemesi** (`طَلْعُهَا هَضِيمٌ`) ve **yıldızsız**;
  "adlandırma + nitelik" düzeyinde, 25:61 ve 26:63 ile aynı sınıf. Biyolog
  merceğinin alanına düşüyor ama ★★★ eşiği aşılmadığı için mercek zaten
  yazılamazdı.
- **Blok bilançosu:** ★★★ 4 (26:144, 146, 149, 150) · ★★ 0 · ★ 1 · 5 yıldızsız.
  **Dört ★★★ ayetin ikisi nakarat**, biri edilgenlik, biri hapaks. Sûre 26'nın
  okunan 150 ayetinde ★★★ **33**.

### DEVAM NOKTASI

**Sûre 26, ayet 151.** Blok 26:151-160 (on ayet). Beklenenler: 26:155-158 deve
ve su nöbeti (`نَاقَة` · `شِرْب` · `يَوْمٍ مَّعْلُومٍ`) — **çıpa tanımı için
sınama alanı** · 26:158'de **nakaratın ikinci GÖMÜLÜ biçimi** (aday 707'nin
sınama vakası) · 26:159 nakarat çiftinin altıncı geçişi · **26:160'tan itibaren
Lût kıssası ve ön-kaydın ASIL SINAMASI.**


### 26:151-160 EKİ — SÛRE 26 160/227, ADAYLAR 713-721

Okunan ayet **1872 → 1882** (korpusun %30,2'si). `turkce_denetim.py` → **0**
(2 ihlâl). `anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl, diff = 0**
(21667). Kök tablosu 1003'te sabit. Bağlar `AF_suara` 119 → **130**.

## ★★★ ADAY 707 DOĞRULANDI VE YENİ BİR MİMARİ AYRIM ÇIKTI (aday 720)

**26:158 ikinci gömülü nakarat:** n=10, `nakarat` alanı 0, `esit` boş, ama
birinci nakaratı içeriyor; önek `فَأَخَذَهُمُ ٱلْعَذَابُ`. 26:139 ile birebir
aynı davranış. **İki gömülü vaka da kaçırılıyor; nakarat sayımı 6 değil 8.**

**Ve ölçülebilir bir mimari ayrım:**

| kıssa | nakarat çifti |
|---|---|
| Mûsâ (26:67-68) · İbrâhîm (26:103-104) · Nûh (26:121-122) | **bütün** (iki ayrı ayet) |
| Hûd (26:139-140) · Sâlih (26:158-159) | **kırık** (biri gömülü) |

**ÖN-KAYIT:** 26:174 ve 26:190 nakarat listesinde **standalone** görünüyor, yani
**tahmin: Lût ve Şuayb kıssalarında çift yine bütün olacak.** 26:174'te sınanacak.

## ★★ ALTINCI NAKARAT KÜMESİ — VE NAKARAT TANIMININ EŞİĞİ BELİRSİZ (aday 715)

26:153 (`إِنَّمَآ أَنتَ مِنَ ٱلْمُسَحَّرِينَ`) 26:185 ile tam özdeş; `nakarat`
alanı 2. Önceki beş küme 5-8 üyeliydi; **bu iki üyeli.**

**İki üyeli bir tekrar "nakarat" mı, sıradan bir tekrar mı?** Nakarat tanımının
eşiği belirsiz ve bu, sûrenin "nakarat 34 ayet" sayımını doğrudan etkiliyor.
683/700/707'nin sayımları bu kümeyi **içermiyor** — düzeltme yeniden hesaplanacak.

## ★★ ÖLÇÜLEBİLİR BİR KURAL VE YENİ BİR ÖN-KAYIT (aday 721)

Dört kıssa açılışı:

| ayet | n | kavim | biçim |
|---|---|---|---|
| 26:105 | 4 | Nûh | **tamlama** (`قَوْمُ نُوحٍ`) |
| 26:123 | 3 | Âd | tek ad |
| 26:141 | 3 | Semûd | tek ad |
| 26:160 | 4 | Lût | **tamlama** (`قَوْمُ لُوطٍ`) |

**Kural: kavim ELÇİ ADIYLA anılıyorsa tamlama, KENDİ ADIYLA anılıyorsa tek ad.**
**ÖN-KAYIT:** Şuayb kıssası (26:176) — kavmi Eyke halkı olarak biliniyor;
**tahmin: açılış ne saf tamlama ne saf tek ad olacak, üçüncü bir biçim çıkacak.**
26:176'da sınanacak, **tutmazsa açıkça yazılacak.**

## DİĞER

- **Ön-kaydın üçüncü sınaması başladı:** öğe (i) Lût kıssasında **var** (26:160).
- **`صلح` aynı sûrede özel ad ve fiil karşı karşıya** (aday 714): 26:142 Sâlih,
  26:152 "düzeltmek". 26:124'ün `هود` vakasının **tersi** — orada özel ad korpus
  anlamına karışıyordu, burada iki anlam **okuyucu için ayırt edilebilir**.
  711'in (`طلع`, iki anlam da dikey satırında) **metin-içi karşılığı**.
- **`عَذَابُ يَوْمٍ عَظِيمٍ` üç aşama** (aday 718): korku (26:135, Hûd) → tehdit
  (26:156, Sâlih) → gerçekleşme (26:158). **Ama** 26:156'nın iki 3-gram'ı da
  7:73 ve 11:64'e düşüyor — terkip korpusta sabit; **aşama dizisi sûreye özgü
  olmayabilir.**
- **`esit_yakin` önerisinin çalışacağını gösteren ilk vaka** (aday 716):
  26:31 ↔ 26:154, ortak parça **dört kelime ve bitişik**.
- **529 kümesi ikiye ayrılacak** (aday 719): (a) sözlüksel çok anlamlılık
  (`جنن` · `أيي` · `خلق`) ve (b) **dilbilgisel işlev kayması** (`صبح` · `كون`);
  onarım stratejileri farklı olabilir.
- **ÇIPA — sınırda bir vaka:** 26:155 bir **sıra düzeni** kuruyor (deveye bir
  gün, kavme bir gün) — "adlandırma + nitelik" düzeyinin biraz üstünde, bir
  **bölüşüm kuralı** var; ama ne süre ölçüsü ne miktar ne mekanizma. **Çıpa
  sınırda sayıldı, mercek yazılmadı** (ayet zaten yıldızsız). 25:25'in sınıfına
  benzer bir kayıt.
- **Blok bilançosu:** ★★★ 1 (26:159) · ★★ 0 · ★ 0 · 9 yıldızsız — 26:71-80 ile
  birlikte **okumada en az yıldızlı iki bloktan biri**. Tek ★★★ nakarat.
  Sûre 26'nın okunan 160 ayetinde ★★★ **34**.

### DEVAM NOKTASI

**Sûre 26, ayet 161.** Blok 26:161-170 (on ayet). Beklenenler: **Lût kıssası ve
ön-kaydın ASIL SINAMASI** — (ii) `أَلَا تَتَّقُونَ` 26:161'de var mı? ·
(iii) 26:162, (iv) 26:163, (v) 26:164 · **26:169 ★★★** · 26:165-166 Lût'un
suçlaması · 26:167'de tehdit kalıbının üçüncü geçişi (`لَتَكُونَنَّ مِنَ
ٱلْمُخْرَجِينَ`) — 26:29 ve 26:116 ile karşılaştırma.


### 26:161-170 EKİ — SÛRE 26 170/227, ADAYLAR 722-728 · **ÖN-KAYIT DÜŞTÜ, BİR SAV GERİ ÇEKİLDİ**

Okunan ayet **1882 → 1892** (korpusun %30,3'ü). `turkce_denetim.py` → **0**
(4 ihlâl). `anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl, diff = 0**
(21668). Kök tablosu **1003 → 1004** (`قلي`). Bağlar `AF_suara` 130 → **137**.

## ★★★ ÖN-KAYIT ASIL SINAMASI — TAHMİN TUTMADI (aday 722)

26:110'da, kıssalar okunmadan önce şöyle yazmıştım:

> *"(ii) `أَلَا تَتَّقُونَ` Lût ve Şuayb'da **bulunmayabilir** (`esit` listesinde
> 26:106 için eşleşme yok, yani kalıp tekil)."*

**Lût kıssasında VAR** (26:161). Altı öğenin altısı yine tamam.

**Ve gerekçem de yanlıştı.** `esit` alanının 26:106'yı eşleştirmemesi kalıbın
**tekil olduğunu değil**, alanın **bilinen eksiğini** gösteriyordu — aday 621:
tam ayet eşleşmesi arıyor, elçi adı değişince kaçırıyor. **Ölçüm aracının
kusurunu metnin özelliği sanmışım.**

**KURAL ÖNERİSİ (yeni):** bir ön-kayıt kurulurken kullanılan ölçüm alanının
**bilinen eksikleri açıkça denetlenecek; eksik alan üzerinden tahmin
kurulmayacak.**

## ★★★ ADAY 650'NİN IDRAB SAVI GERİ ÇEKİLDİ (aday 728)

26:74'ün ölçüm satırında *"makro sayım 2 veriyor ama bu üçüncü geçiş"* yazmıştım.
**Tam sayım yapıldı:**

| biçim | sayı | ayetler |
|---|---|---|
| IDRAB | **2** | 26:74, 26:166 — **makro DOĞRU** |
| QASEM | 0 | — ama 26:97'de `تَٱللَّهِ` var (**aday 672 geçerli**) |
| KELLA | 2 | 26:15, 26:62 |
| NEHY | 4 | 26:151, 156, 181, 183 |
| HASR | 17 · DIKKAT | 5 |

**Üçüncü bir IDRAB olduğunu varsaymıştım; hiçbir kaydım yoktu.** 554→570,
578→616, 666→667 emsalleriyle aynı sınıf: düşürüldüğü belgelendi.
**Ders: "makro sayım tutarsız" demeden önce tam sayım koşulmalı.**

## ★★ ADAY 621'E EN GÜÇLÜ SINAMA VAKASI (aday 725)

**Tehdit kalıbı üç kıssa üç ceza:** 26:29 zindan (Firavun→Mûsâ) · 26:116
taşlanma (kavim→Nûh) · 26:167 sürgün (kavim→Lût).

**26:116 ↔ 26:167 yalnız iki kelime farklı** (nida adı ve ceza adı); sekiz
kelimenin altısı ortak. `esit` yakalamıyor — **ve önerilen `esit_yakin` (n−1
kelime) de kaçırır; n−2 eşiği gerekebilir.**

## ★ 711'İN OTOMATİK TESPİT ÖLÇÜTÜ İKİNCİ VERİYİ ALDI (adaylar 723, 724)

**26:165'te `ذكر` "erkekler" anlamında** (korpusta 292 geçiş, ezici çoğunlukla
"anma, zikir") — **ama dikey satırı ▸sonra `أنث` *(dişi)* ×13,4 veriyor**, yani
bu ayetin anlamı da komşulukta. 711'in (`طلع`) ikinci vakası.

Ve **26:166'da `خلق` "yaratma"** anlamında; 26:137'de "huy, âdet"tı — **aynı
sûrede iki anlam** (714'ün ikinci vakası, `صلح` ile aynı sınıf).

**İki sinyal birlikte:** (a) iki anlam dikey satırında görünüyor, (b) iki anlam
aynı sûrede geçiyor. Tur sonu: 529'un on beş vakasında kaçı bu iki sinyali
veriyor — **otomatik tespit için ilk somut yol.**

## DİĞER

- **`نجو` üç kıssa üç kapsam** (aday 727): topluluk (Mûsâ) / gemidekiler (Nûh) /
  aile (Lût). **Dua kapsamı ile gerçekleşme kapsamı örtüşüyor** (26:118→26:119,
  26:169→26:170).
- **`عمل` iki elçi iki tutum** (aday 726): bilgisizlik (Nûh, 26:112) / öfke
  (Lût, 26:168).
- **"Boş komşuluk" listesi on bire çıktı** (`قلي` eklendi) — **hepsi n≤6**.
- **Lût 26:167'de hem FAİL hem MUHATAP** — 26:116'daki Nûh'tan sonra ikinci vaka.
- **Blok bilançosu:** ★★★ 2 (26:163, 169) · ★★ 0 · ★ 2 (26:164, 166) ·
  6 yıldızsız. Kaynaklar allah ×1 · rab ×3 — hiçbiri içerikten, hiçbirinde çıpa
  yok. Sûre 26'nın okunan 170 ayetinde ★★★ **36**.

### DEVAM NOKTASI

**Sûre 26, ayet 171.** Blok 26:171-180 (on ayet). Beklenenler: 26:171-173 Lût
kıssasının kapanışı (`عَجُوز` · yağmur) · **26:174-175 nakarat çiftinin YEDİNCİ
geçişi — aday 720'nin ön-kaydı sınanacak: çift BÜTÜN mü?** · **26:176'dan
itibaren Şuayb kıssası ve iki ön-kaydın son sınaması** (aday 721 açılış biçimi,
aday 722 öğe (ii)) · 26:176'da `أَصْحَٰبُ لْـَٔيْكَةِ` — açılış tipolojisinin
üçüncü biçimi mi?


### 26:171-180 EKİ — SÛRE 26 180/227, ADAYLAR 729-734 · **İKİ ÖN-KAYIT TUTTU, BİRİ DÜŞTÜ**

Okunan ayet **1892 → 1902** (korpusun %30,5'i). `turkce_denetim.py` → **0**
(5 ihlâl; **biri GERİYE DÖNÜK: 15:60**, `غبر` kökü eklenince açığa çıktı —
dikey satırı içinde kök adı karşılıksız anılmıştı). `anahtar_denetim.py`
(PYTHONHASHSEED=0) → **58 ihlâl, diff = 0** (21669). Kök tablosu **1004 → 1005**
(`غبر`). Bağlar `AF_suara` 137 → **144**.

## ★★★ ÜÇ ÖN-KAYIT SINANDI

**Aday 720 — TUTTU (aday 732).** "Lût ve Şuayb'da nakarat çifti bütün olacak."
26:174 ve 26:175 ikisi de **standalone**. Tam tablo:

| kıssa | nakarat çifti |
|---|---|
| Mûsâ · İbrâhîm · Nûh | **bütün** |
| Hûd · Sâlih | **kırık** (biri gömülü) |
| **Lût** | **bütün** |

**Kırıklık ardışık iki kıssada kümeleniyor** — ön-kaydın öngörmediği desen.

**Aday 721 — TUTTU (aday 733).** "Şuayb açılışı üçüncü bir biçim, n=4."
26:176 `كَذَّبَ أَصْحَٰبُ لْـَٔيْكَةِ ٱلْمُرْسَلِينَ` — n=4, tamlama benzeri ama
"kavim + elçi adı" değil. **Öngörmediğim öğe: fiil `كَذَّبَ` ERİL; öteki dört
açılışta `كَذَّبَتْ` dişil.**

**Aday 722 — TAMAMEN DÜŞTÜ (aday 734).** `أَلَا تَتَّقُونَ` Şuayb'da da var;
beş kıssanın beşinde de. **Ama öngörmediğim gerçek bir fark çıktı: Şuayb'da
`أخو` *(kardeş)* YOK** — öteki dördünde `إِذْ قَالَ لَهُمْ أَخُوهُمْ` + ad
(n=7), burada `إِذْ قَالَ لَهُمْ شُعَيْبٌ` (n=6).

**Ders (aday 734):** ön-kayıt **yön** olarak doğru, **içerik** olarak yanlış
olabilir. Bu "kısmen tuttu" diye kaydedilmemeli — **tahmin düştü**, yan gözlem
ayrı tutuluyor.

**Ve 732'nin dersi 722'nin kuralını doğruluyor:** 720'nin ön-kaydı `nakarat`
alanının **çalışan** kısmına (tam ayet eşleşmesi) dayanıyordu, 722'ninki
**eksik** kısmına (kısmi eşleşme). **Ön-kayıt kurulurken alanın hangi kısmının
güvenilir olduğu denetlenmeli.**

## ★★ OKUMADAKİ EN YÜKSEK İKİ KOMŞULUK KATI — VE İKİSİ DE ŞİŞKİN (aday 729)

`غبر` *(geride kalma)* n=8 → ▸sonra yağmur **×399,0**
`مطر` *(yağmur)* n=15 → ▸önce geride-kalan **×502,7**

**Karşılıklı bağ, ikisi de seyrek, ve iki komşu da bu bölütte** (26:171 ve
26:173). Sekiz geçişin çoğu **aynı sahnenin** farklı sûrelerdeki anlatımıysa kat
değeri **istatistiksel olarak anlamsız**.

**Tur sonu zorunlu:** bir kökün geçişlerinin kaçı **aynı sahnede** (xref ile
bağlı ayetlerde) — bu alan **yok** ve zenginleşme hesabının düzeltilmesi için
gerekli. 689/694 kümesine üçüncü ve en güçlü veri.

## ★ ÜÇ NAKARAT KÜMESİ TAMAMLANDI

- **Üçüncü** (`رَسُولٌ أَمِينٌ`): 5/5 — 26:107, 125, 143, 162, 178
- **Dördüncü** (`فَٱتَّقُوا۟ ٱللَّهَ`): **8/8 — sekizinin sekizi de ★★★**,
  sekizinde de `allah z=6,14` (**aday 683 doğrulandı**)
- **Beşinci** (`وَمَآ أَسْـَٔلُكُمْ … أَجْرٍ`): 5/5

Ve **aday 602'nin karşı yönlü kanıtı beşinci kez**: beş kıssada beş kez aynı
çift — **üç kelimelik nakarat ★★★, on bir kelimelik nakarat ★.**

## DİĞER

- **Eşyapılı üçlü tamamlandı** (aday 730): 26:64 · 26:66 · 26:172 — n=3, 1P ×2,
  aynı fâsıla; değişen yalnız fiil. **`esit` üçünü de bağlamıyor**;
  `esit_yapi` gereksinimi üçüncü kez.
- **`مطر` bir ayette üç kez** (aday 731) — sûre 26'da ikinci vaka (26:19'un
  `فعل`'i birinciydi). Ayet 27:58 ile tam özdeş.
- **Aktör tablosunda tutarlı bir desen** (aday 733): `أَصْحَٰبُ + X` biçimindeki
  kavim adları tabloya **girmiyor** (26:176 Eyke, 25:38 Ress) — 666/667'nin
  "adlı aktör listesi" tanısına ek.
- **Blok bilançosu:** ★★★ 2 (26:175, 179) · ★★ 0 · ★ 1 · 7 yıldızsız. **İki ★★★
  ayetin ikisi de nakarat.** Sûre 26'nın okunan 180 ayetinde ★★★ **38**.

### DEVAM NOKTASI

**Sûre 26, ayet 181.** Blok 26:181-190 (on ayet). Beklenenler: 26:181-183
Şuayb'ın ölçü-tartı uyarıları (`كيل` · `وزن` · `قسطاس`) — **çıpa tanımı için
sınama alanı ve okumada ilk kez bir ÖLÇÜ ARACI adı** · **26:187 ★★★** ·
26:189'da `يَوْمِ ٱلظُّلَّةِ` · **26:190-191 nakarat çiftinin SEKİZİNCİ ve son
geçişi — aday 732'nin ön-kaydının Şuayb sınaması.**


### 26:181-190 EKİ — SÛRE 26 190/227, ADAYLAR 735-744

Okunan ayet **1902 → 1912** (korpusun %30,7'si). `turkce_denetim.py` → **0**
(13 ihlâl). `anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl, diff = 0**
(21671). Kök tablosu **1005 → 1007** (`سقط` · `قسطس`). Bağlar `AF_suara` 144 →
**155**.

## ★★★ OKUMADAKİ EN YÜKSEK KOMŞULUK KATI — VE DESEN ARTIK KESİN (aday 735)

`كيل` *(ölçme)* ▸sonra `قسطس` *(kıstas)* **×661,4** — önceki rekor 26:173'ün
×502,7'siydi. **Ve beş kök birbirine kilitli, hepsi üç ayette:**

| kök | n | bağ |
|---|---|---|
| `وفي` | 66 | ▸sonra `كيل` ×60,9 |
| `كيل` | 16 | ▸sonra `قسطس` **×661,4** · `وزن` ×153,4 |
| `وزن` | 23 | ▸önce `كيل` ×148,7 · ▸sonra `بخس` ×127,5 |
| `قسطس` | **2** | ▸önce `كيل` ×554,4 |
| `بخس` | 7 | ▸önce `وزن` ×142,5 |

**`قسطس` n=2 ve ×554,4 kat veriyor — iki geçişin ikisi de aynı terkipte.**
Desen artık kesin: **seyrek kökler tek bir terkipte kümelendiğinde zenginleşme
katı yüzlerle ölçülüyor ve istatistiksel olarak anlamsız.**

**Tur sonu zorunlu (729'un koşulu):** "bir kökün geçişlerinin kaçı aynı
sahnede/terkipte" alanı üretilecek. **Bu alan olmadan dikey katmanın seyrek kök
satırları kullanılamaz.**

## ★★ OKUMADA İLK KEZ BİR ÖLÇÜ ARACI ADI — VE ÇIPA SAYILMADI (aday 736)

26:182: `وَزِنُوا۟ بِٱلْقِسْطَاسِ ٱلْمُسْتَقِيمِ`. Aday 561'in ölçütünde
"adlandırma + nitelik" düzeyi — 25:61 ve 26:63 ile aynı sınıf. **Ama çıpa
sayılmadı:** (a) ölçü bir **fizik** büyüklüğü değil bir **adalet** ölçütü;
(b) ne birim, ne yöntem, ne değer; (c) olay ne biyolojik ne astronomik.

**Çıpa tanımı işine yeni bir madde önerisi: "ölçü" sözcüğü geçmesi çıpa yapmaz;
ölçünün NEYİ ölçtüğü belirleyici — doğa olayına uygulanması gerekir.**
Tur sonu kararı: bu madde eklenirse 25:61 gibi vakalar yeniden değerlendirilmeli.

**Ve blok bilançosunda dikkat çeken:** 26:181, 182, 183, 187 — **dört ayet çıpa
taşıyabilecek bölütte ve dördü de yıldızsız.**

## ★★ ÜÇÜNCÜ ÖN-KAYIT BAŞARISI VE NAKARAT TAM TABLOSU (aday 744)

26:190 birinci nakarat **standalone** — 26:159'daki ön-kayıt **iki sınamada da
tuttu**. Tam tablo:

| kıssa | çift |
|---|---|
| Mûsâ · İbrâhîm · Nûh | bütün |
| **Hûd · Sâlih** | **kırık** |
| Lût · Şuayb | bütün |

**Kırıklık ardışık iki kıssada ve iki yandan bütün kıssalarla çevrelenmiş** —
yedi kıssanın 4. ve 5.'sinde. Tur sonu: bu konumun rastgele olma olasılığı.

**Ve 722 ile karşılaştırma artık net:** çalışan alan üzerinden kurulan iki
ön-kayıt **tuttu** (720, 721), eksik alan üzerinden kurulan bir ön-kayıt
**düştü** (722).

## ★ NAKARAT ENVANTERİ TAMAMLANDI (aday 739)

| küme | temsil | üye |
|---|---|---|
| 1 | 26:8 | 6 standalone **+ 2 gömülü** |
| 2 | 26:9 | 8 |
| 3 | 26:107 | 5 |
| 4 | 26:108 | 8 |
| 5 | 26:109 | 5 |
| 6 | 26:153 | **2** |

**Toplam: 34 standalone + 2 gömülü = 36 ayet (%15,9).** Ama 715'in sorusu
duruyor: **iki üyeli bir tekrar nakarat mı?** Eşik 3 olsaydı toplam 34 olurdu.
**Tur sonu: eşik tanımlanacak ve bütün sayımlar (★★★ payı, iltifât, esmâ,
`esit`) yeniden hesaplanacak.**

## DİĞER

- **`esit` sınama kümesi üçüncü eşik türünü istiyor** (aday 740): 26:154 ↔
  26:186 — ortak parça **dört kelime ve bitişik**, ama dokuz kelimenin yalnız
  dördü. **`k-ardışık` eşiği** gerekiyor; artık üç tür: tam · n−1/n−2 ·
  k-ardışık.
- **Meydan okuma kalıbı üç geçiş, talep somutlaşıyor** (aday 741): zamir → âyet
  → gökten parça. `سقط` ↔ `كسف` karşılıklı bağ (×520,0 / ×554,4).
- **`عمل` üç elçi üç tutum** (aday 742): bilgisizlik / öfke / bilgiyi havale.
  26:188 **dış düğüm 4 — sûrede en yüksek**.
- **`عَذَابُ يَوْمٍ عَظِيمٍ` üç aşama tamam** (aday 743): korku → tehdit →
  **gerçekleşme**. 26:189'da **iki kök birden ikileniyor** — okumada ikinci vaka.
- **"İki anlam aynı sûrede" dört vakaya çıktı:** `صلح` · `خلق` · `جبل` · `ظلل`.
  Bu, 711/723'ün dikey sinyaliyle karşılaştırılacak — hangisi daha güvenilir?
- **Blok bilançosu:** ★★★ 1 (26:188) · ★★ 0 · ★ 0 · 9 yıldızsız. Sûre 26'nın
  okunan 190 ayetinde ★★★ **39**.

### DEVAM NOKTASI

**Sûre 26, ayet 191.** Blok 26:191-200 (on ayet) — **sûrenin son bölütü
başlıyor**. Beklenenler: 26:191 nakarat çiftinin sekizinci ve son geçişi ·
26:192-197 vahyin nitelenmesi (`رُوحُ ٱلْأَمِينِ` · `لِسَانٍ عَرَبِىٍّ مُّبِينٍ`
· `زُبُرِ ٱلْأَوَّلِينَ`) · **26:197'de sûrenin DÖRDÜNCÜ ve son kafiye kırılması**
(aday 612) · 26:198-199 `أَعْجَمِين` — dil karşıtlığı.


### 26:191-200 EKİ — SÛRE 26 200/227, ADAYLAR 745-753

Okunan ayet **1912 → 1922** (korpusun %30,8'i). `turkce_denetim.py` → **0**
(1 ihlâl). `anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl, diff = 0**
(21671). Kök tablosu 1007'de sabit. Bağlar `AF_suara` 155 → **165**.

## ★★★ ADAY 612 TAMAMLANDI — VE KENDİ YORUMUMU ZAYIFLATIYOR (aday 751)

**Sûrenin dört kafiye kırılmasının dördü de aynı özel adla:** 26:17, 22, 59, 197
— hepsi `إِسْرَٰٓءِيلَ`, hepsi `ل` ile bitiyor, hepsi N sınıfı kafiyeyi kırıyor.
**Sûrenin başka hiçbir yerinde kırılma yok** (227 ayetin 223'ü kısıtı koruyor).

**Ölçülebilir ve test edilebilir sonuç:** kırılma **adın son harfine** bağlı.
Null: bir sûrede belirli bir özel ad fâsıla konumunda geçtiğinde kırılma
olasılığı — yani **kırılma adın özelliği, metnin değil.** Bu, kırılmanın
"anlamlı bir vurgu" olduğu yorumunu **zayıflatıyor**.

**Ve bir yan sonuç (aday 602 ailesine yeni kol):** dört kırılmanın dördü de o
ayetlerde **yıldızın tek kaynağı** — sûrenin dört ★ ayeti tek bir adın ses
yapısından geliyor.

## ★★ ESMÂ ONARIMINA ÜÇÜNCÜ SINIF: MELEK GÖNDERGESİ (aday 747)

26:193'te `أَمِين` esmâ **sayılmıyor** — ama gönderge `ٱلرُّوحُ ٱلْأَمِينُ`, yani
bir **melek**: ne ilâhî ne insan. 682/709'un sınama kümesi iki sınıf tanıyordu;
**bu üçüncü ve hüküm tanımsız.**

Ve envanter daha da geniş: soyut kavram (26:30 `شَىْء`, 26:97 `ضَلَٰل`), yapı
(26:32 `ثُعْبَان`), makam (26:58 `مَقَام`). **Tur sonu: gönderge sınıfları
envanteri çıkarılacak ve her sınıf için hüküm yazılacak — onarımın en zor kısmı
bu olabilir.**

## ★★ 529'A EN ZENGİN VAKA — VE DİKEY SİNYAL BURADA ÇALIŞMIYOR (aday 749)

**`لسن` *(dil)* sûrede üç geçiş, üç anlam:** 26:13 konuşma yetisi (Mûsâ'nın
yetersizliği) → 26:84 nam (İbrâhîm'in isteği) → 26:195 lisan (Arapça).

**Ama dikey satırı yalnız baskın anlamı gösteriyor** (▸sonra Arapça ×76,2); ilk
iki anlamı **göstermiyor**. Yani **711/723'ün "iki anlam da dikey satırında"
sinyali bu vakada çalışmıyor.** Tur sonu: iki sinyalin (dikey satırı / aynı
sûre) hangi vakalarda çalıştığı tablosu.

**"İki anlam aynı sûrede" sınıfı beş vakaya çıktı:** `صلح` · `خلق` · `جبل` ·
`ظلل` · **`لسن` (üç anlamlı)**.

## ★ İKİNCİ NAKARAT KÜMESİ TAMAMLANDI — VE BİR UYARI (aday 745)

8/8 (26:9, 68, 104, 122, 140, 159, 175, 191); **sekiz mühürlü konumun sekizi de
geçerli** — aday 501/598'in mühür sinyali üçüncü sûrede de tutuyor.

**Ama uyarı: sekizi tek bir ayetin tekrarı; bağımsız gözlem 8 değil 1.** Mühür
sinyalinin gücü sûre 26'da abartılı görünüyor. **Tur sonu: mühür sinyali nakarat
düzeltmeli olarak yeniden hesaplanacak.**

## DİĞER

- **`رَبّ ٱلْعَٰلَمِينَ` yedinci konum ve ilk kez anlatıcı sesinde** (aday 746):
  öncekiler kıssada (26:16, 23, 47, 77, 98) ya da nakaratta.
- **Yeni alt sınıf: "iki ayrı kök, karşıt anlam"** (aday 752) — `عرب` ↔ `عجم`,
  üç ayet arayla. 613/627/652/687'nin ("aynı anlam alanı") **aynası**.
- **`قلب` sûrede üç işlev** (aday 748): kurtuluş şartı → vahyin **indiği** yer →
  vahyin **sokulduğu** yer; son ikisi ters yönde.
- **`ٱلْأَوَّلِينَ` dört fâsıla dört gönderge** (aday 750): atalar / âdet /
  nesiller / kitaplar.
- **`قرأ` sûrede ilk ve tek geçiş** (aday 753) — 200 ayette; dikey satırı ▸önce
  `فرق` (Furkān kökü) ×22,4 veriyor.
- **Blok bilançosu:** ★★★ 2 (26:191, 192) · ★★ 0 · ★ 1 (26:197) · 7 yıldızsız.
  **Sûre 26'nın okunan 200 ayetinde ★★★ 41 — sûrenin toplam ★★★ sayısına
  ulaşıldı; kalan 27 ayette yeni ★★★ yok.**

### DEVAM NOKTASI

**Sûre 26, ayet 201.** Blok 26:201-210 (on ayet). Beklenenler: 26:201-209
inanmama ve mühlet bölütü · **26:208'de `مُنذِرُونَ`** — 26:194 ile bağ ·
26:210-212'de **şeytanların vahiy taşıyamayacağı** bölütü açılıyor · sûre
kapanışına on yedi ayet kaldı ve **26:224'te `ٱلشُّعَرَآء` — sûrenin adı ve aday
688'in kapanışı.**


### BİÇİM İHLÂLİ KAYDI — 2026-09-04, blok 26:191-200 · **ÖNLEM TUTMADI**

**Ne oldu:** 26:194-196 ve 26:198-200 sohbete TAM KİPTE yazılmadı — altı ayet
ikişer üçer gruplanıp Türkçe meal satırları düşürüldü. Kullanıcı uyarısıyla
tespit edildi ve altı ayet tam kipte yeniden yazıldı.

**BU İKİNCİ KEZ.** Birincisi blok 26:41-60'taydı (on altı ayet). O zaman
"BİÇİM İHLÂLİ KAYDI" başlığı açılmış ve önlem yazılmıştı: *"çıktı hacmi tam kipi
kaldırmıyorsa özete kayılmaz, BLOK BÖLÜNÜR; sûre 26'nın kalan blokları ON
ayet."*

**ÖNLEM TUTMADI VE NEDEN TUTMADIĞI ÖNEMLİ:** önlem *blok boyunu* düzenliyordu,
ama ihlâl blok boyundan gelmiyor. Blok zaten on ayetti. İhlâl, **blok içinde**
"benzer ayetleri gruplama" eğiliminden geldi — 26:194-196 ve 26:198-200 birbirine
benzeyen, kısa, nakarat dışı ayetlerdi ve onları tek başlık altında topladım.
**Yani önlem yanlış değişkeni hedefliyordu.**

**YENİ ÖNLEM (blok boyundan bağımsız):** her ayet, ne kadar kısa ya da bir
öncekine benzer olursa olsun, **kendi başlığını, kendi Arapça satırını, kendi
Türkçe mealini, kendi ölçüm satırını, kendi ◇ ve ▽ satırlarını alır.** İki ayet
tek başlık altında birleştirilmez. Bir bloktaki ayet sayısı değil, **başlık
sayısı** denetlenir: blok on ayetse sohbette on `### 26:N` başlığı olmalı.

**Bu kayıt, önlemin kendisinin de sınanabilir olduğunu gösteriyor:** birinci
önlem bir kez daha ihlâl edildiği için düşürüldü ve yerine ölçülebilir bir ölçüt
(başlık sayısı = ayet sayısı) kondu.


### 26:201-210 EKİ — SÛRE 26 210/227, ADAYLAR 754-761

Okunan ayet **1922 → 1932** (korpusun %31,0'ı). `turkce_denetim.py` → **0**
(6 ihlâl). `anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl, diff = 0**
(21671). Kök tablosu 1007'de sabit. Bağlar `AF_suara` 165 → **174**.

**Biçim:** on ayet, **on başlık**, on meal — yeni önlem uygulandı.

## ★★ DİKEY SİNYAL TABLOSU ŞEKİLLENİYOR (adaylar 756, 760)

711/723'ün önerdiği otomatik tespit ölçütü ("iki anlam da dikey satırında
görünüyorsa kök çok anlamlıdır") artık **dört vakalı**:

| kök | ikinci anlam | dikey sinyal |
|---|---|---|
| `طلع` | tomurcuk | **çalışıyor** |
| `ذكر` | erkekler | **çalışıyor** |
| `لسن` | nam | çalışmıyor |
| `نظر` | mühlet | çalışmıyor |

**İlk hipotez (test edilmedi):** ikinci anlamın **korpus sıklığı** belirleyici —
yeterince sıksa komşulukta görünüyor, dağınıksa görünmüyor. **Tur sonu zorunlu:
dört vakada ikinci anlamın geçiş sayısı ölçülecek; bu, ölçütün KOŞULUNU
tanımlar.**

Ve "iki anlam aynı sûrede" sınıfı **altı vakaya** çıktı: `صلح` · `خلق` · `جبل` ·
`ظلل` · `لسن` · `نظر`.

## ★★ ELLE KODLAMA GEREKTİRMEYEN İLK YÖRÜNGE VAKASI (aday 761)

`نزل` sûrede **dört biçim, bir kaynak zinciri:**

| ayet | biçim | rol |
|---|---|---|
| 26:192 | masdar | kaynak (âlemlerin Rabbi) |
| 26:193 | bab I | aracı (Rûhu'l-Emîn) |
| 26:198 | bab II | farazî alıcı |
| **26:210** | **bab V, OLUMSUZ** | reddedilen (şeytanlar) |

**Bab alanı `defter.json`'da zaten var (`vf`)** — bu, 628/635/639/671/686
ailesindeki ilk vaka ki **elle kodlama gerektirmiyor**; bab dizisi otomatik
çıkarılabilir.

## ★ YENİ BİR ÖN-KAYIT (aday 755) — VE BU KEZ ÇALIŞAN ALANA DAYANIYOR

`شعر` sûrede iki kez ve ikisi de "farkına varma" (26:113, 26:202). **Ön-kayıt:**
üçüncü geçiş **26:224'te `ٱلشُّعَرَآء` biçiminde olacak** ve bu korpusta
**azınlık** anlam; dolayısıyla **sûre adı, sûrenin kendi içindeki iki geçişin
anlamıyla örtüşmeyecek.**

**722'nin kuralı uygulandı:** bu tahmin **kök sayımına** dayanıyor — `nakarat`
ya da `esit` gibi bilinen eksiği olan bir alana değil.

## DİĞER

- **26:205-207: üç ayetlik şart-cevap yapısı ve iki ucunda aynı kök iki çatıda**
  (aday 758): `مَّتَّعْنَٰهُمْ` etken → `يُمَتَّعُونَ` edilgen.
- **Çıpa — ikinci kez aynı madde işe yaradı** (aday 758): 26:205'te `سِنِينَ`
  *(yıllar)* bir **süre adı**, ölçü değil — sayı yok, birim tanımı yok.
  736'nın önerdiği madde ("ölçü sözcüğü geçmesi çıpa yapmaz") burada da geçerli.
- **`هلك` olaydan kurala** (aday 759): 26:139 bir olay, 26:208 bir genel kural
  (HASR ile). 680'in akrabası ama farklı: orada anlatı **ölçeği**, burada
  bildirim **düzeyi** değişiyor.
- **Bitişik çift, ters zaman yönü** (aday 757): 26:203 mühlet isteği ↔ 26:204
  acele suçlaması; ikisi de soru, 26:204 sûrenin en kısa ayetlerinden (n=2).
- **Blok bilançosu:** ★★★ 0 · ★★ 0 · ★ 2 (26:206, 207) · 8 yıldızsız —
  **okumada ★★★ çıkmayan ilk on ayetlik blok.** İki ★ ayetin ikisi de aynı üç
  ayetlik yapının içinde ve ikisinde de kaynak edilgenlik oranı.

### DEVAM NOKTASI

**Sûre 26, ayet 211.** Blok 26:211-220 (on ayet). Beklenenler: 26:211-212
şeytanların vahiy taşıyamayacağının gerekçesi (`مَعْزُولُونَ`) · **26:213-214
tekil muhataba emirler** (`فَلَا تَدْعُ` · `وَأَنذِرْ عَشِيرَتَكَ`) · 26:215-220
tevekkül bölütü · **26:217-220'de `ٱلْعَزِيزِ ٱلرَّحِيمِ` mühür çiftinin
nakarat DIŞI ilk geçişi** — aday 745'e sınama.


### 26:211-220 EKİ — SÛRE 26 220/227, ADAYLAR 762-771

Okunan ayet **1932 → 1942** (korpusun %31,1'i). `turkce_denetim.py` → **0**
(1 ihlâl). `anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl, diff = 0**
(21671). Kök tablosu 1007'de sabit. Bağlar `AF_suara` 174 → **184**.

**Biçim:** on ayet, **on başlık**, on meal.

## ★★★ ADAY 745/602'NİN EN TEMİZ GÖSTERİMİ (aday 768)

`عَزِيز|رَحِيم` çifti sûrede **dokuz kez**:

| konum | ayet | n | rab | yıldız |
|---|---|---|---|---|
| nakarat ×8 | `وَإِنَّ رَبَّكَ لَهُوَ ٱلْعَزِيزُ ٱلرَّحِيمُ` | 5 | **var** | **★★★** |
| **nakarat dışı** | 26:217 `وَتَوَكَّلْ عَلَى ٱلْعَزِيزِ ٱلرَّحِيمِ` | 4 | **yok** | **yıldızsız** |

**Aynı esmâ çifti, aynı mühür konumu, iki yıldız durumu — fark yalnız Rab
varlığı.** Yani **sekiz ★★★'ın kaynağı esmâ çifti değil, ayetteki Rab oranıydı.**
Bu, okumada **kontrollü karşılaştırma gibi işleyen ikinci vaka** (birincisi
26:62 ↔ 26:78, aday 654).

## ★★★ ÜÇÜNCÜ ALAN AYNI TASARIM HATASINI TAŞIYOR (aday 765)

26:214'te `say` alanı `عشر` kökünü **açık sayı sözcüğü** saymış — oysa lemma
`عَشِيرَة` *(aşiret)*, sayı değil.

| alan | hata türü | vaka |
|---|---|---|
| aktör | kök eşleşmesi | `نُفُورا`→nefer (462/579) · `فِرْقٍ`→ferîk (641) |
| esmâ | lemma listesi, gönderge denetimi yok | `مُؤْمِن` ×15 (682/709) |
| **sayı** | **kök eşleşmesi** | **`عَشِيرَة`→"on" (765)** |

**Ortak kök sebep: hiçbir alan lemma + bağlam denetimi yapmıyor.** Bu, dört
kümenin (529 dikey, 462/579/641 aktör, 682/709 esmâ, 765 sayı) **aynı onarıma**
ihtiyaç duyduğunu gösteriyor.

## ★★ 529'UN EN GENİŞ VAKASI: DÖRT ANLAM TEK SÛREDE (aday 769)

`قوم` (n=660) sûrede **dört anlam alanında**: kavim (kıssalar) · **kalkma**
(26:218) · konum (`مَقَام`, 26:58) · doğruluk (`مُسْتَقِيم`, 26:182). `أيي`
(n=597, üç anlam) ve `خلق` (n=261, iki anlam) vakalarını **geçiyor**.

**Bab çözmez, lemma kısmen çözer, bağlam gerekir** — 697/705'in "üçüncü katman
zorunlu" sonucu **üçüncü kez** doğrulandı.

Ve 529 vakaları artık üçe ayrılabiliyor: **bab yeter** (`صرف`·`قرن`·`رجو`·`طلق`·
`سوي`·`قلب`) · **lemma yeter** (`جنن`·`صلح`·`جبل`) · **bağlam gerekir**
(`أيي`·`خلق`·`لسن`·`نظر`·`قوم`·`ذكر`·`طوع`).

## ★★ MÜHÜR ENVANTERİ TAM — VE BAĞIMSIZ SAYI 10 DEĞİL 3 (aday 771)

26:220'de sûrenin **ikinci mühür çifti** çıkıyor: `سَمِيع|عَلِيم`. Envanter:
**10 mühür, 2 çift, hepsi GEÇERLİ (esmâ artefaktı yok)** — 501/598'in mühür
sinyali üçüncü sûrede de %100 tutuyor.

**Ama dokuzu tek çiftin, sekizi tek ayetin tekrarı: bağımsız mühür sayısı 3**
(26:9 tipi 1, 26:217, 26:220). Nakarat düzeltmeli: **3/3 geçerli — hâlâ %100 ama
örneklem çok küçük.**

## DİĞER

- **`سمع` beş özne katmanı ve dizi kapanıyor** (aday 763): ilâhî → Firavun →
  putlar → şeytanlar → **ilâhî sıfat (esmâ)**. Ve 706'nın `pas` eksiği ikinci
  vakasını aldı (`مَعْزُولُونَ` görülmüyor).
- **İlk kez bir 529 vakası nakarat düzeltmesi gerektiriyor** (aday 762): `طوع`
  dokuz geçişin sekizi tek nakarattan. **700'ün dört ölçümüne beşincisi
  ekleniyor: kök sayımları.**
- **`تبع` beş değer** (766) ve **`عمل` dört tutum** (767) tamamlandı.
- **İki tür yörünge ayırt edilebiliyor** (761 + 766): **bab** yörüngesi (`نزل`,
  otomatik çıkarılabilir) ve **değer** yörüngesi (`تبع`, elle kodlanıyor).
- **Blok bilançosu:** ★★★ 0 · ★★ 0 · ★ 1 (26:213) · 9 yıldızsız — **okumada
  ★★★ çıkmayan ikinci ardışık blok.**

### DEVAM NOKTASI

**Sûre 26, ayet 221 — SON BLOK, YEDİ AYET.** Beklenenler: 26:221-223 şeytanların
kime indiği · **26:224'te `ٱلشُّعَرَآء` — sûrenin adı ve ADAY 755'İN ÖN-KAYDI
SINANACAK** · 26:225-226 şairlerin nitelenmesi · 26:227 sûrenin son ayeti ve
`ٱلَّذِينَ ءَامَنُوا۟` istisnası. **Sûre kapanışında: tam bilanço, nakarat
düzeltmeli sayımlar ve makro profilin yeniden yazılması.**


### 26:221-227 EKİ — **SÛRE 26 TAMAMLANDI (227/227)**, ADAYLAR 772-779

Okunan ayet **1942 → 1949** (korpusun %31,3'ü). `turkce_denetim.py` → **0**
(7 ihlâl). `anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl, diff = 0**
(21672). Kök tablosu **1007 → 1008** (`هيم`). Bağlar `AF_suara` 184 → **192**.

**Biçim:** yedi ayet, **yedi başlık**, yedi meal.

## ★★★ DÖRDÜNCÜ ÖN-KAYIT BAŞARISI (aday 775)

26:202'de, 26:224 okunmadan önce: *"`شعر`'in üçüncü geçişi 26:224'te
`ٱلشُّعَرَآء` biçiminde olacak ve korpusta **azınlık** anlam; sûre adı, sûre
içindeki iki geçişin anlamıyla **örtüşmeyecek**."* — **TUTTU.**

**Ön-kayıt bilançosu: 720 tuttu · 721 tuttu · 722 düştü · 755 tuttu.** Ve desen
net: **çalışan alana dayanan üç ön-kayıt tuttu, eksik alana dayanan bir ön-kayıt
düştü.** 722'nin kuralı dördüncü kez doğrulandı.

**Uyarı korunuyor (688):** sûre adları metnin kendisinden gelmemiş olabilir;
**ad-metin ilişkisi bu projede test dışı.** Bulgu yalnız kök sıklık dağılımı
olarak kaydedildi.

## ★★★ KENDİ KAYDIM DÜŞTÜ — 763'ÜN "DİZİ KAPANIYOR" YORUMU (aday 774)

26:220'de `سمع`'in esmâ olarak gelişini görüp *"dizi ilâhî→beşerî→cansız→gayb→
ilâhî diye kapanıyor"* demiştim. **Üç ayet sonra altıncı geçiş var** (26:223,
şeytanların kulak vermesi) ve dizi **gayb'a dönüyor**.

**Ders: bir dizi "kapandı" denmeden önce sûrenin sonuna kadar okunmalı** —
26:220'de sûrenin yedi ayeti kalmıştı. 554→570, 578→616, 650→728, 666→667
emsalleriyle aynı sınıf.

## ★★★ SEYREK KÖK KATLARININ SEBEBİ BULUNDU (aday 776)

26:225: `ودي` *(vâdi)* ▸sonra `نمل` *(karınca)* **×534,8** ve `هيم` ▸önce `شرب`
**×297,4**. **İki kat da tek bir sahneden geliyor:** 27:18'deki karınca vadisi ve
56:55'teki susuz deve benzetmesi.

**689/694/729/735 kümesinin dördüncü ve en açık vakası — desen artık kesin ve
sebebi de belli.** Sûre 26'da **dokuz** böyle vaka: `شحن` ×301,6 · `غبر` ×399,0 ·
`مطر` ×502,7 · `كيل` ×661,4 · `ودي` ×534,8 · `هيم` ×297,4 · `عجم` ×472,7 ·
`قسطس` ×554,4 · `سقط`/`كسف` ×520/554.

**Tur sonu zorunlu: "bir kökün geçişlerinin kaçı aynı sahnede" alanı üretilecek;
bu alan olmadan n≤25 köklerin dikey satırları kullanılamaz.**

---

# SÛRE 26 (ŞUARÂ) — KAPANIŞ BİLANÇOSU (aday 779)

## Ham sayımlar

| ölçüm | değer |
|---|---|
| ayet | 227 |
| ★★★ / ★★ / ★ / yıldızsız | **41 / 10 / 16 / 160** |
| iltifât | 15 |
| esmâ token | 51 |
| `esit` dolu ayet | 44 |
| `nakarat` alanı dolu | 34 |
| mühür | 10 |

## Nakarat düzeltmeli sayımlar

**Nakarat envanteri:** altı küme — 26:8 tipi (6 standalone **+ 2 gömülü**) ·
26:9 tipi (8) · 26:107 tipi (5) · 26:108 tipi (8) · 26:109 tipi (5) · 26:153
tipi (2). **Toplam 36 ayet (%15,9).**

| ölçüm | ham | düzeltilmiş |
|---|---|---|
| ★★★ payı | 41 (%18,1) | **25 (%11,9)** |
| esmâ token | 51 | **≈29** (≥22'si nakarattan) |
| iltifât | 15 | **≤11** (≥4'ü tek nakarattan) |
| mühür | 10 | **3** |
| kök sayımları | — | `طوع` 9 → **2** (aday 762) |

**ALTI ölçüm birden şişmiş.** Makro profil bütünüyle yeniden yazılmalı.

## Sûre boyunca çıkan başlıca ölçümler

- **Yıldızın içerik ölçmediğinin en temiz gösterimi (26:217, aday 768):** aynı
  esmâ çifti, aynı mühür konumu — nakaratta ★★★ (Rab var), nakarat dışında
  **yıldızsız** (Rab yok).
- **Çıpası olan tek ★★★ ayet: 26:63** — ve o da yıldızını çıpadan değil hapakstan
  alıyor. **41 ★★★'ın 40'ında çıpa yok.**
- **Dört kafiye kırılmasının dördü de `إِسْرَٰٓءِيلَ`** (aday 751) — kırılma
  adın son harfine bağlı; "anlamlı vurgu" yorumu düştü.
- **Üç alan aynı tasarım hatasını taşıyor** (aday 765): aktör, esmâ, sayı —
  hiçbiri lemma + bağlam denetimi yapmıyor.
- **529'un en geniş vakası `قوم`: dört anlam alanı, tek sûrede** (aday 769).

### DEVAM NOKTASI

**Sûre 26 bitti.** İki seçenek: (a) sûre 27'ye geçmek, (b) **tur sonu onarım
evresine girmek** — P0 borçlar birikti: nakarat alanı yeniden tanımı, `esit`
üç/dört alana bölünmesi, esmâ gönderge denetimi, aktör ve sayı lemma denetimi,
dikey katmanın "aynı sahne" alanı, 529'un üç katmanlı onarımı, ve sûre 26'nın
makro profilinin yeniden yazılması.


---

# SÛRE 27 (NEML) AÇILDI — MAKRO PROFİL + 27:1-10, ADAYLAR 780-788

Okunan ayet **1949 → 1959** (korpusun %31,4'ü). `turkce_denetim.py` → **0**
(8 ihlâl). `anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl, diff = 0**
(21676). Kök tablosu **1008 → 1009** (`شهب`). Yeni bağ öbeği `AG_neml` (9 bağ),
yeni aday öbeği `AH_neml`.

## MAKRO PROFİL

**93 ayet · 1151 kelime · 12,38 kel/ayet · Mekkî · nüzûl 48.**
**Sûre 26'nın (5,81) iki katından fazla.**

## ★★★ A/R ORANI TERSİNE DÖNÜYOR — OKUMADA İLK KEZ >1 (aday 780)

| sûre | ort. kelime | A | R | **A/R** |
|---|---|---|---|---|
| 23 | 8,90 | 13 | 23 | 0,57 |
| 24 | 20,56 | 80 | **0** | tanımsız |
| 25 | 11,60 | 8 | 14 | 0,57 |
| 26 | 5,81 | 13 | 36 | **0,36** |
| **27** | **12,38** | **27** | **12** | **2,25** |

**"Mekkî sûrelerde A/R ~0,57" hipotezi iki kez düştü** — sûre 26'da aşağı, sûre
27'de **yukarı**. **Ders: dört sûrede görülen bir aralıktan hipotez kurmak erken
oldu; dağılım görülmeliydi.**

Ve **ilk lafız 27:8'de, göreli konum 0,086** (sûre 25: 0,22 · sûre 26: 0,39) —
**lafız gecikmesi de sûreye özgü, Mekkî'ye özgü değil** (aday 527/665).

## ★★★ SÛRE 27, SÛRE 26'NIN DOĞAL KONTROLÜ (aday 781)

| ölçüm | sûre 26 | sûre 27 |
|---|---|---|
| ort. kelime | 5,81 | **12,38** |
| nakarat ayet | 36 | **0** |
| `esit` dolu ayet | 44 | **3** |
| kafiye kırılması | 4 | **0** |
| iltifât | 15 | **3** |
| ★★★ payı | %18,1 ham / **%11,9** düzeltmeli | **%9,7** (düzeltme gerekmiyor) |

**İki sûre birlikte aday 602'nin kısa ayet yanlılığı hipotezini doğrudan
sınayabiliyor:** ayet uzunluğu iki katına çıkınca ★★★ payı düşüyor — 602'nin
yönüyle uyumlu. **Tur sonu: kontrollü karşılaştırma olarak kullanılacak.**

## ★★ MÜHÜR SİNYALİ İÇİN ÇOK DAHA UYGUN ZEMİN (adaylar 782, 787)

Sûre 27'de **altı mühür, altı ayrı konum, tekrar yok — bağımsız sayı 6.**
Sûre 26'da on mühürden dokuzu tek çiftti ve bağımsız sayı **3**'e düşmüştü
(aday 771). **Ve çiftler çeşitli:** 27:6 `حَكِيم|عَلِيم`, 27:9
`عَزِيز|حَكِيم`, sonra `غَفُور|رَحِيم`, `رَحْمٰن|رَحِيم`…

Esmâ ön denetimi: **33 token, artefakt adayı 13 (%39)** — `مُبِين` 6 (gönderge
kitap/söz), `آخِر` 4 (âhiret, zaman adı), `مُؤْمِن` 3 (insanlar). **Okunan ilk üç
geçişin üçü de artefakt çıktı.**

## DİĞER

- **27:3-4-5: üç ardışık ayette `ٱلْءَاخِرَة`, üç işlev, üçü de artefakt**
  (aday 783) — **esmâ hatası ayet düzeyinde kümeleniyor**, rastgele dağılmıyor.
- **Mûsâ kıssası iki giriş noktası** (aday 785): 26:10 **nidâ** ile, 27:7 **ateş
  görme** ile — sûre 27 bir ayet önceden başlıyor. 607/680 kümesine üçüncü vaka.
- **`رَبِّ ٱلْعَٰلَمِينَ` sûre 27'de ilk geçiş ve lafızla birlikte** (aday 786);
  sûre 26'da yedi geçişin hiçbirinde lafız yoktu.
- **27:10'da altı 3-gram'ın altısı da 28:31'e düşüyor** (aday 788) — okumada ilk
  kez; `esit` boş. **Yeni ölçüt önerisi: "xref yoğunluğu", `xref` alanından
  otomatik çıkarılabilir.** Ve `جنن` üçüncü anlamda (cennet / delilik / yılan).
- **Blok bilançosu:** ★★★ 2 (27:6, 8) · ★★ 1 (27:9) · ★ 0 · 7 yıldızsız.
  Kaynaklar pas ×2 · allah ×1 — hiçbiri içerikten, hiçbirinde çıpa yok.

### DEVAM NOKTASI

**Sûre 27, ayet 11.** Blok 27:11-20 (on ayet). Beklenenler: 27:11-14 Mûsâ
bölütünün kapanışı (`تِسْعَ ءَايَٰتٍ` — **açık sayı**) · 27:15-19 Dâvûd ve
Süleymân · **27:17 ★★★** (cin-ins-kuş orduları) · **27:19 ★★★ ve hapaks `بسم`
*(gülümseme)*** · **27:20 ★★★ ve hapaks `هدهد` *(hüdhüd)*** — sûrenin adını
veren `نمل` *(karınca)* 27:18'de gelecek.


### 27:11-20 EKİ — SÛRE 27 20/93, ADAYLAR 789-799

Okunan ayet **1959 → 1969** (korpusun %31,6'sı). `turkce_denetim.py` → **0**
(7 ihlâl; **biri GERİYE DÖNÜK: 26:225**, `نمل` kökü eklenince açığa çıktı).
`anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl, diff = 0** (21686).
Kök tablosu **1009 → 1017** (`بسم`·`تسع`·`حطم`·`فقد`·`نعج`·`نمل`·`هدهد`·`وزع`).
Bağlar `AG_neml` 9 → **19**.

## ★★★ BEŞİNCİ ÖN-KAYIT BAŞARISI (aday 796)

26:225'i okurken `ودي` *(vâdi)* ▸sonra `نمل` *(karınca)* ×534,8 görmüş ve
*"kaynak 27:18'deki karınca vadisi sahnesi"* demiştim. **27:18 okundu ve
doğrulandı:**

| kök | dikey bağ |
|---|---|
| `ودي` | ▸sonra `نمل` ×534,8 |
| `نمل` | ▸önce vadi ×520,0 |
| `سكن` | ▸önce karınca ×99,1 |

**Üç kök birbirine kilitli ve üçü de tek ayette.** Bu, 735/776'nın "seyrek kök
katı tek sahneden gelir" savını **doğrudan** doğruluyor.

**Ön-kayıt bilançosu: 720 · 721 · 755 · 775 · 796 tuttu; 722 düştü** — ve düşen
tek ön-kayıt, ölçüm alanının bilinen eksiği üzerine kurulmuştu.

## ★★★ OKUMADAKİ EN YÜKSEK KOMŞULUK KATI: ×948,5 (aday 790)

27:12'de `تسع` *(dokuz)* ▸sonra `نعج` *(dişi koyun)* **×948,5** — önceki rekor
26:181'in ×661,4'üydü. **Kök korpusta yedi geçişli ve kat 38:23'teki "doksan
dokuz dişi koyun" sahnesinden.** Sûre 27'de şimdiden **üç** böyle vaka:
`تسع` ×948,5 · `ودي` ×534,8 · `نمل` ×520,0.

**Tur sonu zorunlu: "aynı sahne" alanı üretilmeden n≤25 köklerin dikey satırları
kullanılamaz.**

## ★★★ ÇIPA TABLOSU — YILDIZ DAĞILIMI TERS (aday 799)

| ayet | çıpa | yıldız | kaynak |
|---|---|---|---|
| 27:16 kuş dili | adlandırma + nitelik | ★★ | edilgenlik |
| 27:17 üç sınıflı ordu | yok | ★★★ | edilgenlik |
| **27:18 karınca vadisi** | **davranış dizisi — en güçlü** | **yıldızsız** | — |
| 27:19 gülümseme | yok | ★★★ | hapaks |
| 27:20 hüdhüd adı | adlandırma altı | ★★★ | hapaks |

**Çıpası en güçlü ayet yıldızsız; çıpası olmayan iki ayet ★★★ ve ikisinin de
kaynağı hapaks.** Aday 599/602'nin sûre 27'deki ilk ve en temiz gösterimi.

## ★★ OKUMADA İLK KEZ ÜÇ KÖK BİRDEN İKİLENİYOR (aday 797)

27:19'da `قول` ×2 · `نعم` ×2 · `صلح` ×2 — önceki vakalar iki kökle (26:118,
26:189, 26:227). Ve **dokuz 3-gram'ın sekizi 46:15'e düşüyor** — 27:10'un altı
bağını geçiyor. **"xref yoğunluğu" ölçütüne ikinci veri; iki vaka da sûre 27'nin
ilk iki bloğunda.**

## DİĞER

- **Mühür çeşitliliği** (aday 789): beş ayet içinde üç ayrı çift, üçü de geçerli
  — sûre 26'nın tersi. Mühür sinyali bu kez **bağımsız örneklemle** sınanıyor.
- **Esmâ artefaktı kalıba bağlı** (aday 791): `هَٰذَا + isim + sıfat` kalıbı
  26:34'te de 27:13'te de artefakt üretiyor — 690'ın sûreler arası karşılığı.
- **"Toplanma" iki ayrı kökle** (aday 795): `جمع` / `حشر` — 613/627/652/687
  kümesinin **sûreler arası** ilk vakası.
- **`طير` üç ölçek** (aday 798): dil (yeti) → ordu (topluluk) → hüdhüd (birey).
- **`حكم`+`علم` sûre 27'de hem mühür esmâsı hem "verilen şey"** (aday 793) —
  esmâ gönderge sorununa yeni bir açı.
- **Blok bilançosu:** ★★★ 3 (27:17, 19, 20) · ★★ 1 (27:16) · ★ 0 · 6 yıldızsız.

### DEVAM NOKTASI

**Sûre 27, ayet 21.** Blok 27:21-30 (on ayet). Beklenenler: **27:21 sûrenin en
uzun ayeti (n=61)** · 27:22-26 hüdhüdün Sebe haberi · **27:23'te `imrae`
adsız aktörü — DENETLENECEK** (önceki hata oranı %67) · **27:25 ★★★** ve hapaks
`خبأ` · 27:26 ★★ · **27:30'da besmele** (`بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ
ٱلرَّحِيمِ`) ve `رَحْمٰن|رَحِيم` mührü.

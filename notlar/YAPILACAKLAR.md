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


### DEPO DENETİMİ — 2026-09-09, YÜKLEME SONRASI

**Depo klonlandı ve denetimler koşuldu. Bir hata bulundu ve onarıldı.**

## ★★★ SÜREÇ HATASI: BLOK BETİKLERİ OTURUM BOYUNCA DENETLENMEMİŞ

`anahtar_denetim.py` **yalnız `betikler/` dizinini tarıyor**. Oturum boyunca blok
betiklerini düz çalışma dizininde (`/home/claude/duz/`) yazdım ve `betikler/`
içine hiç kopyalamadım. **Sonuç: bu oturumda üretilen yirmi iki blok betiği
oturum boyunca hiç denetlenmedi.** Oturum içi "diff = 0" raporları bu betikleri
kapsamıyordu.

Betikler depoya yüklendikten sonra koşulan denetim **21910 anahtar / 59 ihlâl**
verdi — taban 58. **Yirmi iki betikte tek bir yeni ihlâl:**

```
── betikler/blok_26_151_160.py (1)
   ✗ sat.158 نَاقَة   T2 YAZIM → korpustaki hâli: ناقَة
```

26:157'nin mercek satırında `نَاقَة` yazmıştım (nûn üzerinde fazladan fetha);
korpus lemma biçimi `ناقَة`. **Onarıldı** — betik, `okuma_metni.json` ve
`mercek_kayit.json` üçünde de.

**Onarım sonrası: 21910 anahtar / 58 ihlâl · taban ile diff = 0 ·
`turkce_denetim.py` → 0.**

## ÖNLEM (yeni, ölçülebilir)

**Blok betiği yazıldıktan sonra `betikler/` içine kopyalanacak ve
`anahtar_denetim.py` ORADAN koşulacak.** Aksi hâlde denetim betiği görmez.

Bu, aday 785/796'nın "ölçüm aracının kapsamı denetlenmeli" dersinin araç tarafı:
**bir denetimin ne taradığı, sonucundan önce bilinmeli.** Oturum boyunca
"diff = 0" gördüm ama denetim yeni yazdığım dosyaların hiçbirine bakmıyordu.


---

# BLOK 27:21-30 — HÜDHÜDÜN SEBE HABERİ VE MEKTUP

**On ayet okundu. Sûre 27 → 30/93. Okunan toplam 1979 / 6236 (%31,7).**
**Aday 800-810 · bağ AG_neml 19 → 29 · kok_turkce 1017 → 1019.**

## DENETİM

`turkce_denetim.py` → **0 ihlâl** (1019 kök).
`anahtar_denetim.py` (PYTHONHASHSEED=0, `betikler/` içinden) → **22976 anahtar / 58 ihlâl**,
**ihlâl listesi taban ile diff = 0.** İki yeni betik (`blok_27_21_30.py`,
`aday_ekle_27_21_30.py`) *yazıldıktan sonra `betikler/` içine kopyalandı* ve denetim
oradan koştu (2026-09-09 dersinin ilk uygulaması); **1066 yeni anahtar tarandı, sıfır
yeni ihlâl.**

**TABAN DOSYASI TAZELENDİ.** `ciktilar/anahtar_denetim_raporu_tohum0.txt` 2026-09-09
onarımından sonra yenilenmemişti; başlığı hâlâ **21055** yazıyordu, oysa ölçülen 21910
idi. İhlâl kümesi değişmemişti (58, birebir aynı liste), yani içerik doğruydu — ama
**başlık satırı iki oturumdur yanlış sayı taşıyordu ve tam `diff` her koşuda tek satır
fark veriyordu.** Dosya bu blokun sonucuyla (22976 / 58) yeniden yazıldı; artık tam
`diff = 0`.

## DÜŞEN KAYIT (aday 801)

Kapanış notu devam noktasında **27:21'i "sûrenin en uzun ayeti (n=61)"** diye
kaydetmişti. **Ölçülen n=9.** Sûrenin en uzunları: 27:40 (38) · 27:44 (28) · 27:60 (27)
· 27:19 (24) · 27:61 (21). Kayıt, sıralı listedeki **(n=21, ayet=61) ikilisinin ters
okunmasından** gelmiş. Sessizce düzeltilmedi, düşürüldüğü belgelendi.

**Ders:** oturum kapanış notlarındaki sayısal beklentiler bloğa girmeden önce defterden
doğrulanacak. Aday 780'in ("dört sûrelik aralıktan hipotez erken") **not tarafı**: not
alma sırasında da ölçüm ile hafıza karışabiliyor.

Ayet yine de bir uç değer taşıyor, başka eksende: **EMPH/n = 0,67, korpusun en yüksek
tekit yoğunluğu** (aday 800).

## ADSIZ AKTÖR DENETİMİ — TAM SAYIM (aday 802, P0)

İstenen denetim yapıldı ve korpusun tamamına genişletildi. **`imrae` etiketli 11 tokenin
7'si hatalı (%63,6).**

| sınıf | sayı | ayetler | lemma |
|---|---|---|---|
| doğru | **4** | 4:12 · 4:128 · **27:23** · 33:50 | `امْرَأَت` (dişil, kişi) |
| **eril** | **6** | 4:176 · 24:11 · 52:21 · 70:38 · 74:52 · 80:37 | `امْرِئ` / `امْرُؤٌا` |
| **kişi değil** | **1** | 4:4 | `مَرِيئ` (sıfat, "afiyetli") |

**27:23 DOĞRU.** Mekanizma: alan **kök** düzeyinde eşleşiyor; `مرأ` üç lemma taşıyor ve
üçü tek etikete iniyor. Önceki "%67 hata" tahmini doğrulandı.

**Yeni hata sınıfı: CİNSİYET TERSİNMESİ** — sözcük kişi ama karşı cinsiyet; 11 tokenin
6'sı. `نُفُورا`→nefer (462/579) ve `فِرْقٍ`→ferîk (641) vakalarından farklı tür.

**Onarım maliyeti düşük:** üç lemma zaten ayrı, bağlam denetimi gerekmiyor. **Aday
765'in dört alanı içinde en ucuz onarılanı bu.**

## DİKEY KATMANIN KORUMASI YANLIŞ DEĞİŞKENDE (aday 806, P0)

Kural "n≤25 köklerin yüksek katları güvenilmez" diyor ve **hedef kökün** n'sine bakıyor.
Bu blokta n'si yüksek kökler yine çok yüksek kat verdi:

| hedef | n | ortak | n(ortak) | kat | katkı veren AYRI ayet |
|---|---|---|---|---|---|
| `عظم` | **128** | `مضغ` | 3 | ×69,8 | **1** (23:14) |
| `سجد` | **92** | `شطر` | 5 | ×43,3 | 3 (2:144-150, **tek sahne**) |
| `مرأ` | 38 | `عقر` | 8 | ×177,0 | 3 |
| `عرش` | 33 | `ستت` | 8 | ×145,0 | 6 |
| `شمس` | 33 | `قمر` | 27 | ×129,3 | **21 — ARTEFAKT DEĞİL** |
| `ذبح` | 9 | `حيي` | 189 | ×232,7 | 3 |

**Ayırt edici hedefin n'si değil, KATKI VEREN AYRI AYET SAYISI.** `شمس` ▸ `قمر` ×129,3
yirmi bir ayrı ayetten geliyor ve gerçek bir birliktelik; `عظم` ▸ `مضغ` ×69,8 tek
ayetten geliyor ve artefakt. **İkisi de mevcut korumanın dışında kalıyor.**

Bu, **biçim ihlâli önleminin ("blok boyu ON") aynı hatasının ölçüm tarafındaki
karşılığı**: doğru sonucu yanlış değişkenle korumak.

**ÖN-KAYIT (TUR SONU'nda sınanacak):** katkı veren ayrı ayet sayısı ≤2 → satır
yorumlanmaz; 3-5 → "tek sahne" uyarısı; >5 → serbest. Sûre 26'nın dokuz vakası ve sûre
27'nin üç vakası bu eşikle yeniden etiketlenecek. **P0 #2'nin "aynı sahne" alanına
işlevsel tanım budur.**

## KAFİYE VE MÜHÜR (aday 804)

**Sûre 27: 93 ayet, 84 `ن` + 9 `م`. Altı mühür ayetinin ALTISI da `م` fâsılalı**
(27:6, 9, 11, 30, 40, 78). Kalan üç `م` ayeti mühürsüz ve **üçü de bu blokta**: 27:23
(`عَظِيم`) · 27:26 (`ٱلْعَظِيم`) · 27:29 (`كَرِيم`). Dokuz `م` fâsılasının dokuzu da
`فَعِيل` vezninde.

**Kafiye tarafı KAPALI** (`fs` çalışan alan, tam sayım koşuldu). **Mühür tarafı
KAPATILAMAZ** — 27:40 ve 27:78 okunmadı, mühür geçerliliği okuma denetiminden geçmedi.
Ön-kayıt (ikisi de geçerli çıkacak) **eksik alan üzerine kurulduğu için ZAYIF etiketli**
(aday 722 dersi).

## DİĞER

- **Besmele ayet içinde** (aday 803/804): tam besmele korpusta 114 kez sûre başında,
  **ayet içinde yalnız 27:30'da**; kısa biçim `بِسْمِ ٱللَّهِ` ayrıca 11:41'de.
  `رَحْمٰن` korpusta 57 esmâ tokeni taşıyor, **sûre 27'nin tek tokeni burada.**
- **`مُبِين` sûre 27'de 4/4 artefakt** (27:1 kitâb · 27:13 sihr · 27:16 fadl · 27:21
  sultân) — **KAPATILAMAZ**, 27:75 ve 27:79 okunmadı. Sûre 26'nın `مُؤْمِن` 15/15
  vakasıyla aynı desen: fâsıla konumundaki sıfat-esmâ lemması gönderge denetimi olmadan
  token üretiyor.
- **27:23 ↔ 27:26 `عَرْش`+`عَظِيم` çifti** (aday 805): belirsizden belirliye, üç ayet
  arayla, ikisi de fâsıla konumunda; **`esit` alanı ikisinde de BOŞ**. `esit_yapi`
  türünün temiz sınama vakası; "fâsıla konumunda ortak" bir alt ölçüt adayı.
- **27:24-25-26 sûrede ilk üç ardışık lafız** (aday 807). Okunan korpusta 3+ ardışık
  lafız dizisi 60 kez ve **hepsi on sûrede** (9-14, 16, 18, 22, 24). KAPATILAMAZ —
  tarama yalnız okunan sûrelerde koşuldu.
- **`سمو` 529 vakası** (aday 808): 27:25 "gökler", 27:30 "ad", beş ayet arayla, dikey
  satırları birebir aynı. **Otomatik tespit ölçütü ("iki anlam da dikey satırında
  görünüyor") burada ÇALIŞMADI → 2/5.** İkinci anlamın korpus sıklığı belirleyici
  hipotezi güçlendi.
- **Çıpa/yıldız ters ilişkisi ikinci gösterim** (aday 809): 27:24 sûrenin okunan tek gök
  cismi ayeti (`شمس`) ve **yıldızsız**; 27:25 hiçbir gök cismi anmıyor ve hapakstan
  ★★★.
- **Blok bilançosu:** ★★★ 1 (27:25) · ★★ 2 (27:26, 29) · ★ 2 (27:23, 30) · yıldızsız 5.
  Yıldız kaynakları: hapaks 1 · pas 2 · eksen 2 — **içerikten sıfır**. İltifât 0/10.

### DEVAM NOKTASI

**Sûre 27, ayet 31.** Blok 27:31-40 (on ayet). Beklenenler *(defterden doğrulandı)*:
27:31 iltifât var (`3>12`, sûrenin ikinci iltifâtı) · 27:32 ve 27:38 `قال + أيّ + ملأ`
xref'inin sûre içi karşılıkları · **27:40 sûrenin EN UZUN ayeti (n=38)** ve
**`غَنِيّ|كَرِيم` mührü — sûrenin beşinci mührü ve beşinci farklı çift, aday 804'ün
sınaması** · **27:39 ★★★** (esmâ `قَوِيّ`, gönderge DENETLENECEK — ifrit'in kendi
nitelemesi olabilir, aday 803 sınıfı) · 27:36 `IDRAB` biçimi · 27:32/27:38/27:40
`DIKKAT` · **blokta yıldız yalnız iki ayette (27:39 ★★★, 27:40 ★★)**.


---

# BLOK 27:31-40 — MEKTUP, İSTİŞARE, HEDİYE, TAHT

**On ayet okundu. Sûre 27 → 40/93. Okunan toplam 1989 / 6236 (%31,9).**
**Aday 811-821 · bağ AG_neml 29 → 40 · kok_turkce 1019 → 1021.**

## DENETİM

`turkce_denetim.py` → **0 ihlâl** (1021 kök).
`anahtar_denetim.py` (PYTHONHASHSEED=0, `betikler/` içinden, `kok_turkce.json` DIŞARIDA)
→ **21996 anahtar / 58 ihlâl**, taban ile **tam diff = 0**.

## SÜREÇ HATASI VE ONARIMI (aday 820)

Blok 27:21-30 kapanışında taban dosyasını yazarken **`kok_turkce.json` `betikler/` içinde
unutulmuştu**; taban başlığı **22976** olarak kaydedildi, oysa doğru sayı 21910 idi.
İhlâl listesi hiç değişmemişti (58, birebir) — yalnız başlıktaki anahtar sayısı şişti.
Onarıldı; taban dosya dışarıdayken yeniden yazıldı.

**YENİ KURAL:** taban dosyası yalnızca `kok_turkce.json` `betikler/` **dışındayken**
yazılır; `turkce_denetim.py` koşulduktan sonra dosya **hemen** silinir.

2026-09-09'un *"bir denetimin ne taradığı sonucundan önce bilinmeli"* dersinin ikinci
vakası — bu kez denetim **fazla** tarıyordu, az değil.

## DÜŞEN KAYIT (aday 819)

Aday 797 ve blok 27:11-20 metni 27:19'u *"okumada ilk kez üç kök birden ikileniyor"*
diye kaydetmişti. **Tam sayım: okunan sûrelerde 3+ farklı kökü ikilenen 107 ayet var**;
okunan bölütün rekoru **24:31 (on bir farklı kök, 27 tekrar)**, korpus rekoru 2:282 (on
altı kök). Doğru ifade: **27:40 sûre 27'nin en çok ikilenen ayeti (beş kök, biri üç
kez)**; 27:19 sûrenin üçüncüsü.

**İki blok üst üste, bir sayısal iddia tam sayımla düştü** (aday 801, 819). Ders (728'in
kardeşi): *"okumada ilk kez"* demeden önce okunan bölüt üzerinde tam sayım koşulmalı.

## ★ MÜHÜR BAYRAĞI GÖNDERGE DENETİMİNİ YAPIYOR (aday 818, P0)

Sûre 27'nin ilk kırk ayetinde **23 esmâ tokeni**:

| | token | geçerli | artefakt |
|---|---|---|---|
| **mühür tokeni** (5 mühür) | 10 | **10** | 0 |
| **mühürsüz token** | 13 | **0** | 13 |

**Mühür bayrağı bu bölütte gönderge geçerliliğini kusursuz ayırıyor.** Artefaktların
gönderge sınıfları: nesne/yapı 5 (27:1, 13, 16, 21, 29) · insan tekil 2 (27:2, 15) ·
zaman/yer 3 (27:3, 4, 5) · **insan çoğul 2** (27:34, yeni) · **gayb varlığı 1. şahıs 1**
(27:39, yeni).

**AMA bayrak YAPISAL** (iki esmânın bitişikliği + son konum) ve gönderge bilgisi
taşımıyor; **tek başına gelen geçerli bir ilâhî ismi tanım gereği yakalayamaz.**

**ÖN-KAYIT:** sûrenin kalan sekiz mühürsüz tokeni (27:49 `وَلِيّ` · 27:59 `سَلام` ·
27:63 `بَرّ` · 27:66 `آخِر` · 27:75 `مُبِين` · 27:77 `مُؤْمِن` · 27:79 `مُبِين` ·
27:88 `خَبِير`) içinde **en az biri GEÇERLİ çıkacak ve ayrım bozulacak.** Bu ön-kayıt
çalışan alan üzerine kurulu ve bilinçli olarak **kendi desenimin bozulacağı** yönünde.

## ADAY 804'ÜN ÖN-KAYDI SINANDI VE TUTTU (aday 817)

**27:40'ın `غَنِيّ|كَرِيم` mührü GEÇERLİ**, fâsıla harfi `م` — sûrenin beşinci mührü,
beşinci farklı çift, beşinci `م` fâsıla. Ön-kayıt **eksik alan üzerine kurulmuştu ve
ZAYIF etiketliydi; ilk gözlemde tuttu** — aday 722'nin desenine uymadı. Tek gözlem;
27:78 okunmadan **KAPATILAMAZ**.

## 529 KÜMESİ — ALTINCI VAKA VE ÖLÇÜTÜN TERK EDİLMESİ (aday 814)

`هدي` sûre 27'de iki anlam alanında: 27:24 `ٱهْتَدَى` *(yol buldu)*, 27:35-36
`هَدِيَّة` *(hediye)*. Dikey satırı yalnız "yol gösterme" anlamından geliyor.

**Otomatik tespit ölçütü ("iki anlam da dikey satırında görünüyor") 2/6'ya düştü.**
Çalışan: `طلع`, `ذكر`. Çalışmayan: `لسن`, `نظر`, `سمو`, `هدي`. **Hipotez desteklendi:
azınlık anlamı sayıca ezildiğinde ölçüt kör.** TUR SONU: ölçüt terk edilip **lemma
katmanına** geçilecek — `هُدَى`/`هَدِيَّة` ve `سَماء`/`اسْم` ayrı lemmalar, bağlam
denetimi gerekmiyor.

## DİĞER

- **27:31 iltifât alıntı metnin içinde** (aday 811): 27:30 üçüncü şahısla açıyor, 27:31
  birinci-ikinci şahsa geçiyor; alan yakaladı. **İltifât vakaları 'anlatı içi' /
  'alıntı sınırında' / 'alıntı içi' diye sınıflandırılmadan sayımlar karşılaştırılamaz.**
- **27:34 ↔ 27:37 `ذلل` iki ağızda, aynı kalıpta** (aday 812): kraliçenin kralların
  yapacağını söylediği şey, cevabında ona söyleniyor. `esit`in yedi eşiğinin hiçbirine
  takılmıyor — **"konuşmacı-arası kalıp yankısı" sekizinci eşik türü adayı.**
- **2FS korpusta 30 ayette (%0,48); 27:33 dört işaretle ortak yedinci** (aday 813).
  Sûre 27'de üç 2FS ayeti (27:33, 42, 44), üçü de aynı kişiye.
- **`عرش` üçüncü belirlilik kipinde** (aday 815): belirsiz (27:23) → belirli (27:26) →
  iyelikli (27:38). **27:38 fâsıla konumunda DEĞİL** — aday 805'in "fâsıla konumunda
  ortak" alt ölçütü ilk kez ayırt etti.
- **Kraliçe blok boyunca konuşuyor ve hiçbir aktör alanına girmiyor.** 27:23'te `imrae`
  etiketiyle sayılmıştı. **Aday 802'nin ikinci yüzü: alan yalnız yanlış pozitif
  üretmiyor, aynı göndergeyi sahneden sahneye izleyemiyor da.**
- **Blok bilançosu:** ★★★ 1 (27:39, kaynak hapaks `عفر`) · ★★ 1 (27:40, kaynak n z=2,72)
  · yıldızsız 8. **Yıldızsız oran %80 — okumada görülen en düşük yıldız payı olabilir,
  KAPATILAMAZ.** Kaynaklarda içerik yine sıfır.
- **Sûre 27 ilk kırk ayet: A/R = 1,40, makro 2,25.** Sûre içi eksen dalgalanması; aday
  780'in konum-eşli null gereğine veri.

### DEVAM NOKTASI

**Sûre 27, ayet 41.** Blok 27:41-50 (on ayet). Beklenenler *(defterden doğrulandı)*:
27:42 ve 27:44'te 2FS (kraliçeye hitap sürüyor) · **27:44 sûrenin ikinci en uzun ayeti
(n=28)**, yıldız ★ · **27:49 QASEM — sûrenin tek yemini; `تَٱللَّهِ` sınama vakası
(aday 443/672)** · 27:49'da `وَلِيّ` esmâ tokeni, **aday 818'in ön-kaydının ilk
sınaması** · 27:41/27:42'de `عرش` dördüncü ve beşinci geçiş (aday 805/815 dizisi
kapanabilir) · **blokta yıldız yalnız iki ayette (27:42 ★, 27:44 ★); sekiz ayet
yıldızsız — arka arkaya ikinci %80'lik blok.**


---

# BLOK 27:41-50 — KÖŞK, TESLİM OLUŞ, SEMÛD BÖLÜTÜNÜN AÇILIŞI

**On ayet okundu. Sûre 27 → 50/93. Okunan toplam 1999 / 6236 (%32,1).**
**Aday 822-832 · bağ AG_neml 40 → 51 · kok_turkce 1021 → 1023.**

## DENETİM

`turkce_denetim.py` → **0 ihlâl** (1023 kök).
`anahtar_denetim.py` (PYTHONHASHSEED=0, `betikler/` içinden, `kok_turkce.json` DIŞARIDA)
→ **22064 anahtar / 58 ihlâl**, taban ile **tam diff = 0**.

Bu blokta `turkce_denetim.py` ilk koşuda **37 ihlâl** verdi — ◇ mercek metninde kökleri
karşılıksız anmışım. Elle tek tek düzeltmek yerine **kök anmalarını otomatik glosslayan
bir geçiş** koşuldu (kök + hemen ardından `*(` gelmiyorsa karşılık ekle). Kökler harekesiz,
ayet alıntıları harekeli olduğu için çakışma yok. **Bu bir araç değişikliği değil, metin
hazırlama adımı** — sonraki bloklarda da aynı geçiş koşulacak.

## ★ ADAY 806'NIN ÖLÇÜTÜ SÛRE 27'NİN ÜÇ UYARI VAKASINI AÇIKLADI (aday 824, P0)

Ölçüt: yüksek kat, hedef kökün değil **ortak kökün** seyrekliğinden ve **katkı veren ayrı
ayet sayısının** azlığından gelir. Bu blokta beş yeni vaka ölçüldü:

| hedef | n | ortak | n(ortak) | kat | katkı veren ayrı ayet |
|---|---|---|---|---|---|
| `تسع` | 7 | `نعج` | 4 | ×948,5 | **1** (38:23) |
| `طير` | **29** | `هيأ` | 4 | ×474,2 | **2** (3:49, 5:110) |
| `سوق` | 17 | `لفف` | 3 | ×389,7 | **1** (75:29) |
| `بيت` | **73** | `عنكب` | 2 | ×147,0 | **1** (29:41) |
| `مرد` | 5 | `شطن` | 88 | ×45,1 | 3 |

**Ve sûre 27'nin ÜÇ uyarı vakasının üçü de tek ayetten geliyor:** `تسع`▸`نعج` → 38:23
(doksan dokuz koyun); `ودي`▸`نمل` ve `نمل`▸`ودي` → **ikisi de 27:18** (karınca vadisi).
"Aynı sahne" gerçekten tek sahne.

**Toplam on iki ölçülen vaka; ölçüt on ikisinde de ayırıyor. Mevcut n≤25 koruması on
ikinin ALTISINI kaçırıyor** (`بيت` n=73 · `عظم` n=128 · `سجد` n=92 · `مرأ` n=38 ·
`عرش` n=33 · `طير` n=29). Karşı örnek yerinde duruyor: `شمس`▸`قمر` ×129,3 yirmi bir ayrı
ayetten geliyor ve artefakt değil.

## 529 KÜMESİ — TEK SÛREDE ÜÇ VAKA (aday 823/832, P0)

| kök | anlam alanları | ayetler |
|---|---|---|
| `سمو` | gök / ad | 27:25 · 27:30 |
| `هدي` | yol bulma / hediye / **tanıma** | 27:24 · 27:35-36 · **27:41** |
| `طير` | kuş / uğur-fal | 27:16, 17, 20 · **27:47** |

**Otomatik tespit ölçütü yedinci vakada da çalışmadı → 2/7.** `طير` vakası ölçütün neden
kör olduğunu netleştiriyor: **azınlık anlamı burada seyrek değil** — ölçüt sıklık
yüzünden değil, **birlikte geçen köklerin anlam alanını hiç kullanmadığı için** kör.

İyi bir karşı örnek: `نظر` sûrede **beş** kez geçiyor (27:27, 28, 33, 35, 41) ve tek
anlam alanında kalıyor. **Sorun "çok geçen kök" değil, kökün lemma yapısı.** Üç vakanın
üçünde de ayrı lemmalar var (`سَماء`/`اسْم` · `هُدَى`/`هَدِيَّة` · `طَيْر`/`طائِر`);
bağlam denetimi gerekmiyor. **P0 #5'in lemma katmanı için sınama kümesi yedi vakalık.**

## ÖN-KAYIT SINAMASI (aday 826)

**27:49 `وَلِيّ` → ARTEFAKT** (gönderge `لِوَلِيِّهِۦ`, Sâlih'in kan yakını, insan tekil).
Aday 818'in ayrımı bozulmadı: **mühür tokeninde 10/10 geçerli, mühürsüz tokende 0/14.**
Sekiz sınamanın birincisi geçti; ön-kayıt ayakta. Kalan yedi: 27:59 `سَلام` · 27:63 `بَرّ`
· 27:66 `آخِر` · 27:75 `مُبِين` · 27:77 `مُؤْمِن` · 27:79 `مُبِين` · 27:88 `خَبِير`.

Not: `وَلِيّ` korpusta ilâhî gönderge ile de geçen bir lemma — **alanın lemma seviyesinde
ayırt edilemeyeceğinin kanıtı, bağlam denetimi şart** (aday 816 ile aynı sonuç).

## YILDIZ ALANI UZUN AYETLERDE EKSEN KÖRÜ (aday 827, P1)

27:44 sûrenin **en yoğun eksen ayeti**: lafız bir kez, `رَبّ` iki kez (sûrede iki Rab
taşıyan ilk ayet). Yıldız ★ ve **kaynağı yalnız uzunluk** (n z=1,65); allah z=0,19 ve
rab z=1,20 eşiği aşmıyor. n=8'lik 27:26 iki eksen işaretiyle ★★ almıştı.

**z hesabı eksen işaretini ayet uzunluğuna göre seyrelttiği için uzun ayetlerde eksen
görünmez oluyor.** Aday 599/602'nin "yıldız içeriği ölçmüyor" bulgusuna **yapısal bir
mekanizma daha**. TUR SONU: z hesabında uzunluk normalizasyonu denetlenecek.

## DİĞER

- **27:50 `مكر` dört kez, n=7 → oran 0,57, korpusun ikinci en yüksek tek-kök yoğunluğu**
  (53:38'de 3/5 = 0,60; mutlak sayıda 27:50 önde) — aday 822.
- **Blokta üç kez aynı yapı: kök sabit, konum sabit, özne/muhatap karşıt** — 27:36 `أتي`
  (muhatap), 27:43 `صدد` (fâil), 27:50 `مكر` (özne). `esit`in **dokuzuncu eşik türü
  adayı** (812'nin sekizincisiyle birlikte).
- **27:49 sûrenin tek yemini ve bir suikast yemini** (aday 825): korpusta 71 QASEM ayeti;
  burada bir peygamberi öldürmeye `بِٱللَّهِ` diyerek ant içiliyor. QASEM tagger yazılırken
  **"yemin eden kim" alanı** da üretilecek.
- **27:43-49 sûrenin ilk eksen kümesi: yedi ayetin altısında lafız** (aday 828); sûrenin
  ilk kırk iki ayetinde toplam sekiz lafız vardı. Semûd bölütünün açılışıyla çakışıyor.
- **27:48 ↔ 26:152 birebir formül** (aday 829): iki sûrenin Semûd bölütü. **Aday 781'in
  kontrollü çiftine anlatı düzeyinde ilk örtüşme**; sûre 26'da bölüt nakaratlı, 27'de
  nakaratsız — **nakarat alanının yeniden tanımı (P0 #4) için doğal sınama çifti.**
- **`عرش` dizisi KAPANDI** (aday 830): beş geçişin beşi de okundu, beş farklı kipte;
  `esit` alanı beşinde de boş. "Fâsıla konumunda ortak" alt ölçütü 27:23-27:26 çiftini
  diğer üçünden doğru ayırıyor.
- **Blok bilançosu:** ★ 2 (27:42 pas, 27:44 uzunluk) · yıldızsız 8. **Okumada ilk kez bir
  blokta ★★ ve üstü hiç yok.** Allah lafzı 6 — blok rekoru. **Üç blok üst üste yıldızsız
  oran ≥%80.**
- **Kraliçe 27:23'ten 27:44'e kadar yirmi iki ayet sahnede ve 27:23 dışında hiçbir aktör
  alanına girmiyor** — aday 802'nin ikinci yüzünün ikinci gösterimi.
- Sûre 27 ilk elli ayet: **A/R = 2,80** (ilk kırk ayette 1,40 idi, makro 2,25) — **eksen
  oranı sûre içinde iki kat dalgalanıyor.**

### DEVAM NOKTASI

**Sûre 27, ayet 51.** Blok 27:51-60 (on ayet). Beklenenler *(defterden doğrulandı)*:
27:51-53 Semûd bölütünün kapanışı, sonra Lût bölütü (27:54-58) · **27:58'de `مكر`
sınıfından ikinci yoğun ayet** · **27:59 `سَلام` mühürsüz esmâ tokeni — aday 818'in ikinci
sınaması** · 27:59-60 sûrenin ikinci eksen kümesinin başlangıcı (27:59-65'te 7/7, sûrenin
kendi azamisi) · 27:60'ta `أله` ve doğa bölütünün açılışı — **çıpa tablosu için sûrenin en
verimli bölütü burada başlıyor** (aday 799/809'un sınaması).


---

# BLOK 27:51-60 — SEMÛD'UN KAPANIŞI, LÛT BÖLÜTÜ, DOĞA BÖLÜTÜNÜN AÇILIŞI

**On ayet okundu. Sûre 27 → 60/93. Okunan toplam 2009 / 6236 (%32,2).**
**Aday 833-842 · bağ AG_neml 51 → 62 · kok_turkce 1023 → 1024.**

## DENETİM

`turkce_denetim.py` → **0 ihlâl** (1024 kök; otomatik gloss geçişi baştan koşuldu).
`anahtar_denetim.py` → **22115 anahtar / 58 ihlâl**, taban ile **tam diff = 0**.

## ★ ADSIZ AKTÖR ALANI: MEKANİZMA KESİN OLARAK BULUNDU (aday 833, P0)

27:57'de `ٱمْرَأَتَهُۥ` *(karısı)* var ve alan boş. Tarandı:

| | sayı |
|---|---|
| korpusta `امْرَأَت` lemmalı ayet | **25** |
| alanın etiketlediği ayet | 11 |
| **doğru** | **4** |
| yanlış pozitif | 7 |
| **yanlış negatif** | **21** |

**Duyarlılık 4/25 = %16 · kesinlik 4/11 = %36,4 · F1 ≈ 0,22.**

**Mekanizma tek bir ayrımda ve istisnası yok: yakalanan dördünün dördü de INDEF
(belirsiz); kaçan yirmi ikisinin yirmi ikisi de belirli ya da izâfetli.**

Yani **alan "adsız"ı "belirsiz"le karıştırıyor.** Anlatının en tanınmış adsız kadın
aktörleri — Lût'un karısı (7:83, 15:60, 27:57, 29:32, 29:33), Firavun'un karısı (28:9,
66:11), İmrân'ın karısı (3:35), Ebû Leheb'in karısı (111:4) — hepsi izâfetli olduğu için
**görünmez.**

Aday 802 yalnız kesinliği ölçmüştü; **arızanın boyutu iki katına çıktı.** Onarım hâlâ
ucuz: lemma eşleşmesi + **belirlilik koşulunun kaldırılması.**

## ADAY 806 RAFİNE EDİLDİ — "TEK AYET" ≠ "TEK SAHNE" (aday 835, P0)

27:23'te `مرأ` ▸ geride-kalan ×126,4 satırı "tek sahne" şüphesiyle yorumlanmadan
geçilmişti. 27:57'ye varıldığında ayetin fâsılası tam o sahneyi verdi. Ölçüldü: satır
**beş ayrı ayetten** geliyor ve **beşi de aynı sahne**.

Üç tür ayrıldı:

- **Tür A — tek ayet** (`تسع`▸`نعج`, `بيت`▸`عنكب`, `سوق`▸`لفف`, `عظم`▸`مضغ`,
  `ودي`▸`نمل`): bilgi taşımıyor, bastırılmalı.
- **Tür B — tek sahne, çok ayet** (`مرأ`▸`غبر` 5 ayet · `خوي`▸`عرش` 3 · `شجر`▸`زقم` 3 ·
  `سجد`▸`شطر` 3): **bilgi taşıyor** — kaynak ayetleriyle gösterilmeli.
- **Tür C — gerçek birliktelik** (`شمس`▸`قمر` 21 ayet): serbest.

**Onarım "sil" değil "kaynağı etiketle": "aynı sahne" alanı bir bayrak değil, bir KAYNAK
LİSTESİ üretmeli.**

Ve bir uyarı kayda geçirildi (aday 841): **satırın 27:57'yi "öngörmesi" bir doğrulama
değil, döngüsel** — 27:57 zaten satırın kaynak ayetlerinden biriydi. Satır bir tahmin
yapmadı, kendi kaynağını gösterdi.

## `esit` ALANI OKUMADA İLK KEZ DOLU (aday 834, P0)

**27:58 → [[26,173]].** Üç xref 3-gram'ın üçü de aynı ayete düşüyor; iki ayet neredeyse
birebir. Sûre 27'de esit dolu üç ayet var (27:3, 27:58, 27:71).

**Aday 829'un sınama çifti artık ayet düzeyinde: aynı kavim, aynı cümle, iki sûre — biri
nakaratlı bölütte (26:160-175, on altı ayet), diğeri nakaratsız bölütte (27:54-58, beş
ayet).** P0 #4 için bundan temiz bir çift zor bulunur.

## SÛRE 27'NİN BÖLÜT YAPISI ÖLÇÜLDÜ (aday 839)

| bölüt | ayetler | uzunluk | sûre 26 karşılığı |
|---|---|---|---|
| Mûsâ | 27:7-14 | 8 | — |
| Dâvûd-Süleymân | 27:15-44 | **30** | — |
| Semûd | 27:45-53 | 9 | 26:141-159 (19) |
| Lût | 27:54-58 | 5 | 26:160-175 (16) |
| doğa | 27:60-64 | 5 | — |

**Ortadaki bölüt diğer üçünün toplamının üstünde.** Ve kontrollü çift ölçülü hale geldi:
aynı iki kavim sûre 26'da 35 ayet + nakarat, sûre 27'de 14 ayet + nakarat yok. **Oran
2,5:1 — nakaratın kapladığı yer doğrudan ölçülebilir.**

## z'NİN UZUNLUK NORMALİZASYONU — ÇİFT KANIT TAMAMLANDI (aday 837, P1)

Tek sûrede iki karşıt vaka:

- **27:44** n=28, **üç** eksen işareti (bir lafız, iki Rab) → allah z=0,19 · rab z=1,20 →
  eksenden yıldız **YOK**, ★ uzunluktan.
- **27:59** n=12, **iki** lafız → allah z=**2,80** (sûrenin en yükseği) → **★★ tek başına
  eksenden** (okumada ilk kez).

**Fark yalnız n.** Yıldız alanının ölçtüğü şey "eksen yoğunluğu" değil "eksen yoğunluğu ÷
uzunluk" ve bu ikisi farklı ölçüler. TUR SONU: her ikisi ayrı hesaplanacak.

## ÇIPA EŞİĞİNİN SINIR VAKASI (aday 838, P0)

**27:60** bir NEDENSEL BAĞIMLILIK (gökten su → göz alıcı bahçeler) ve bir YETİ SINIRI
(ağacını siz bitiremezdiniz) kuruyor. **"Adlandırma"nın üstünde, "mekanizma"nın altında
bir kat.** Ölçü, mekanizma ve sınıflandırma yok; eşik aşılmadı.

Ve sonuç tanıdık: **ayet ★ alıyor, kaynağı yalnız uzunluk** (n z=1,55); eksen işareti 23.
sırada, z=0,21. **Sûrenin doğaya en yakın ayeti doğadan değil uzunluktan yıldız alıyor** —
aday 599/602/809 dizisine dördüncü gösterim.

**Çıpa tanımı yazılırken bu katın çıpa sayılıp sayılmayacağına karar verilmeli; karar
verilmeden 26/27 çıpa-yıldız korelasyonu hesaplanamaz.**

## DİĞER

- **Aday 818'in ön-kaydı ikinci kez sınandı** (aday 836): 27:59 `سَلام` → **ARTEFAKT**
  (gönderge bir selamlama). Ayrım **25/25**: mühür tokeninde 10/10 geçerli, mühürsüz
  tokende 0/15. Sekiz sınamanın ikisi geçti; altı kaldı.
- **xref yoğunluğu ortak kelimeyi değil ortak SAHNEYİ ölçüyor** (aday 840): 27:55'te dört
  3-gram ve **dördü de tek ayete (7:81)**. Üçüncü veri. **Bu ölçütü zenginleştiriyor ama
  aynı zamanda sınırlıyor: yüksek xref yoğunluğu bir keşif değil, aynı olayın birden çok
  kez anlatıldığının göstergesi.** TUR SONU: korpus çapında sayım koşulacak; oran yüksek
  çıkarsa ölçüt keşif aracı olarak **düşer**.
- **27:56'da `طهر` bir SUÇLAMA olarak kullanılıyor** — kök korpusta ağırlıkla olumlu
  bağlamda; kökün kutbunu tersine çeviren vaka.
- **Blok bilançosu:** ★★ 1 (27:59, **eksen**) · ★ 1 (27:60, uzunluk) · yıldızsız 8.
  İltifât 0/10. **Rab 0 — okumada ilk kez bir blokta Rab hiç yok.** **Dört blok üst üste
  yıldızsız oran ≥%80.**
- Sûre 27 ilk altmış ayet: **A/R = 3,40** (ilk kırkta 1,40 · ilk ellide 2,80 · şimdi
  3,40; makro 2,25) — **oran monoton artıyor, sûrenin ikinci yarısı eksen yoğun.**

### DEVAM NOKTASI

**Sûre 27, ayet 61.** Blok 27:61-70 (on ayet). Beklenenler *(defterden doğrulandı)*:
**doğa bölütünün gövdesi 27:60-64** — beş ayet, hepsi `أَمَّنْ` kalıbıyla açılıp
`أَءِلَٰهٌ مَّعَ ٱللَّهِ` ile bitiyor, **ve `nakarat` alanı BEŞİNDE DE SIFIR (defterden
doğrulandı)** → sûre 27'nin tek nakarat adayı ve alan onu hiç görmüyor; **P0 #4'ün
doğrudan sınaması bu blokta** · **27:63 `بَرّ` ve 27:66 `آخِر` mühürsüz esmâ tokenleri —
aday 818'in üçüncü ve dördüncü sınamaları** · 27:59-65 eksen kümesi (yedi ayette yedi
lafız) bu bloğun içinde bitiyor, 27:66'dan sonra lafız kesiliyor · **27:68 ★★★ — blokta
tek yıldızlı ayet** · 27:69 sûrenin üçüncü ve son iltifâtı (yön 1>23) · 27:61-64 **çıpa
tablosunun sûredeki en verimli bölütü** (aday 838'in sınır kararı dört kez daha
sınanacak).


---

# BLOK 27:61-70 — DOĞA BÖLÜTÜNÜN GÖVDESİ VE DİRİLİŞ TARTIŞMASI

**On ayet okundu. Sûre 27 → 70/93. Okunan toplam 2019 / 6236 (%32,4).**
**Aday 843-853 · bağ AG_neml 62 → 73 · kok_turkce 1024 → 1025.**

## DENETİM

`turkce_denetim.py` → **0 ihlâl** (1025 kök) · `anahtar_denetim.py` → **22162 anahtar /
58 ihlâl**, taban ile **tam diff = 0**.

## ★ NAKARAT ALANININ MEKANİZMASI BULUNDU (aday 844, P0 #4)

`أَءِلَٰهٌ مَّعَ ٱللَّهِ` ifadesi **korpusun tamamında yalnız beş ayette** geçiyor ve
beşi de ardışık: **27:60, 61, 62, 63, 64.** Beşi de `أَمَّنْ` ile açılıyor.
**`nakarat` alanı beşinde de SIFIR.**

Buna karşılık sûre 26'da alan **34 ayette dolu** — çünkü orada nakarat **tam ayet**
(26:8 bir bütün ayet olarak tekrar ediyor).

**Mekanizma: alan yalnız AYET düzeyinde tekrarı eşliyor; ayet-içi kalıbı görmüyor.**

Ve bu, **aday 833'le aynı hata sınıfı:**

| alan | doğru kavram | bağlandığı yanlış birim |
|---|---|---|
| adsız aktör | adlandırılmamışlık | **belirsizlik (INDEF)** |
| nakarat | tekrar | **ayet tekrarı** |

**İki P0 alanı, aynı tür arıza: doğru kavram, yanlış birim.**

İkinci vaka da bulundu (aday 845): **`كَيْفَ كَانَ عَٰقِبَةُ` sûrede üç kez** (27:14,
27:51, 27:69; korpusta 21 ayet), alan üçünde de sıfır. Ama bu **değişken sonlu** bir
kalıp. Yani onarılmış alanın **üç tür** nakaratı ayırt etmesi gerekiyor:
**tam ayet · sabit ayet-içi kalıp · şablon kalıp.**

**Uyarı:** bu, aday 700/739/771'in sûre 26 nakarat düzeltmesini de etkiliyor — orada
sayılan 34 ayet yalnız ayet düzeyindekiler; sûre 26'da ayet-içi nakaratlar varsa **sayı
eksik.**

## DÜŞEN KAYIT (aday 843)

Bir önceki blokta 27:51 mercek metni *"نظر sûrede ALTINCI geçiş"* demiş ve **27:14'ü
atlamıştı** — 27:14 de aynı `فَٱنظُرْ كَيْفَ كَانَ عَٰقِبَةُ` kalıbını taşıyor. Doğru
sayım: sûrede sekiz geçiş (27:14, 27, 28, 33, 35, 41, 51, 69); 27:51 **yedincisi**.
Metin düzeltildi ve düzeltme notu ayetin mercek satırına gömüldü.

**Üç blok içinde üçüncü sayım hatası** (801, 819, 843). **Ortak mekanizma: sayımı
okunan bloktan yapıp önceki blokları taramamak.** KURAL: *"sûrede kaçıncı geçiş"*
denecekse **sayım defterden tam koşulacak, hafızadan değil.**

## DOĞA BÖLÜTÜ YILDIZ ÜRETMİYOR (aday 849, P0)

| ayet | içerik | yıldız | kaynak |
|---|---|---|---|
| 27:60 | gökten su → bahçeler | ★ | uzunluk |
| **27:61** | **karar yeri, ırmaklar, sabit dağlar, iki deniz arasında engel** (`جعل` dört kez) | **0** | — |
| 27:62 | darda kalana karşılık, halifelik | 0 | — |
| 27:63 | karanlıklarda yol, rüzgârlar | 0 | — |
| 27:64 | yaratmayı başlatma ve tekrarlama, rızık | 0 | — |
| **27:68** | **bir inkâr cümlesi** | **★★★** | **pas** |

**Sûrenin doğaya ayrılmış tek bölütü, toplam yıldız verimi bir ★ ve o da uzunluktan.**
Aday 599/602/809/838 dizisine **beşinci ve en geniş gösterim — artık tek ayet değil, beş
ayetlik bir bölüt.** Ayrıca **27:64 sûrenin en çok dış bağı olan ayeti (dış düğüm 7) ve
hiçbir yıldız kaynağı taşımıyor.**

## z'NİN UZUNLUK NORMALİZASYONU — EN TEMİZ VAKA (aday 847, P1)

| ayet | n | lafız | allah z | yıldız |
|---|---|---|---|---|
| 27:59 | 12 | 2 | **2,80** | **★★** |
| 27:63 | 20 | 2 | **1,47** | **0** |

**Aynı eksen içeriği, tek fark n.** Eşik 1,5 civarında (yıldız veren en düşük z'ler: 1,55
ve 1,57), 27:63 kılpayı düşüyor. Aday 827/837'nin üçüncü ve en temiz vakası.

## pas z TAVANI (aday 848, P1)

27:68'in tek fiili var ve o da edilgen → oran 1/1 = 1,00 → **pas z=5,38, korpus tavanı —
ve tavanı 124 ayet paylaşıyor.** Yani **pas z tek fiilli ayetlerde otomatik tavana
çıkıyor; ★★★'ların bir bölümü yalnızca "ayette tek fiil var ve o edilgen" demek.**
TUR SONU: payda küçüklüğüne karşı düzeltme gerekip gerekmediği sınanacak.

## ADAY 806/835'İN SINIRI (aday 850, P0)

Ölçüt artefaktı ayırıyor ama **donmuş kalıbı anlamsal birliktelikten ayırmıyor:**

- `سطر` ▸ `أول` ×49,7 — **dokuz** ayrı ayet, ama hepsi tek ifade (*esâtîru'l-evvelîn*)
- `عمي` ▸ `صمم` ×93,1 — **sekiz** ayrı ayet, gerçek anlamsal birliktelik

Sayı neredeyse aynı, tür farklı. **İkinci bir alan gerekiyor: ortak geçişlerin aynı
n-gram'ı paylaşıp paylaşmadığı.** Ve bu, **aday 844'ün nakarat n-gram altyapısıyla AYNI
altyapı — iki P0 tek araçla çözülebilir.**

## DİĞER

- **Aday 818'in ön-kaydı üçüncü ve dördüncü kez sınandı** (aday 846): 27:63 `بَرّ`
  (kara/deniz) ve 27:66 `آخِر` (âhiret) → **ikisi de ARTEFAKT.** Ayrım **27/27**: mühür
  tokeninde 10/10 geçerli, mühürsüz tokende **0/17**. Dört sınama kaldı ve **ön-kaydın
  kaderi büyük ölçüde 27:88 `خَبِير`'e bağlı.**
- **529 kümesi sûre içi dördüncü vaka** (27:44 ↔ 27:62): `كشف` — baldırların açılması /
  kötülüğün giderilmesi. Otomatik ölçüt yine çalışmadı → **2/8.**
- **Sûrenin üç iltifâtı üç ayrı katmanda — tam küme** (aday 851): 27:6 anlatı içi · 27:31
  alıntı sınırı · 27:69 emir zinciri.
- **27:61 ↔ 27:62 ardışık ayetlerde zıt sayı alanı** (aday 852): `أَكْثَر` / `قَلِيل`,
  ikisi de fâsıla öncesi. Not: `say` alanı sayı sözcüğüyle nicelik belirtecini
  ayırmıyor.
- **`خرج` sûrede dört geçiş, dört ayrı "çıkarılan"**: gizli olan (27:25) · ordudan
  çıkarılanlar (27:37) · şehirden çıkarılacak aile (27:56) · topraktan çıkarılacak ölüler
  (27:67). Kök tek anlam alanında, nesnesi her seferinde başka katmanda.
- **Blok bilançosu:** ★★★ 1 (27:68, **pas**) · yıldızsız 9. İltifât 1/10. Esmâ token 2,
  ikisi de artefakt. **Rab 0 — iki blok üst üste.** **Adlı ve adsız aktör 0 — okumada ilk
  kez bir blokta hiç aktör yok.** **Beş blok üst üste yıldızsız oran ≥%80.**
- Sûre 27 ilk yetmiş ayet: **A/R = 4,60** (kırkta 1,40 · ellide 2,80 · altmışta 3,40;
  makro 2,25) — **oran monoton artıyor ve makronun iki katına çıktı.**

### DEVAM NOKTASI

**Sûre 27, ayet 71.** Blok 27:71-80 (on ayet). Beklenenler *(defterden doğrulandı)*:
**27:71'de `esit` alanı DOLU ve beş hedefli** ([[10,48],[21,38],[34,29],[36,48],[67,25]])
— sûrenin üçüncü ve son esit'i, **okumada ilk çok hedefli eşleşme** · **27:75 `مُبِين` ve
27:77 `مُؤْمِن` mühürsüz esmâ tokenleri — aday 818'in beşinci ve altıncı sınamaları** ·
**27:78'de `عَزِيز|عَلِيم` mührü — sûrenin ALTINCI ve SON mührü; aday 804'ün ikinci ve son
sınaması** · 27:79 `مُبِين` (yedinci sınama) · sûrenin `مُبِين` dizisi 27:75 ve 27:79 ile
**KAPANACAK** (aday 803, şimdi 4/4 artefakt).


---

# BLOK 27:71-80 — VAADİN ZAMANI, RAB KÜMESİ, SÛRENİN SON MÜHRÜ

**On ayet okundu. Sûre 27 → 80/93. Okunan toplam 2029 / 6236 (%32,5).**
**Aday 854-864 · bağ AG_neml 73 → 84 · kok_turkce 1025 → 1027.**

## DENETİM

`turkce_denetim.py` → **0 ihlâl** (1027 kök) · `anahtar_denetim.py` → **22198 anahtar /
58 ihlâl**, taban ile **tam diff = 0**.

## ★ `esit` ALANININ MEKANİZMASI BULUNDU (aday 854, P0 #3)

**27:80 ile 30:52 arasındaki tek fark baştaki `فَ`; başka hiçbir fark yok.
`esit` alanı İKİSİNDE DE BOŞ.** Oysa dokuz ayet önce **27:71'de aynı alan beş hedefi
birden yakalamıştı** (altı ayet birebir aynı).

**Mekanizma: alan TAM DİZGE eşleşmesi yapıyor; baştaki tek bağlaç harfi eşleşmeyi tümüyle
bozuyor.**

Tam ölçüm: korpusta tam aynı metinli **87 küme / 257 ayet**; baştaki `و`/`ف` atılınca
**94 küme / 273 ayet** — yani **dokuz küme, yirmi dokuz ayet yalnız bu tek harf yüzünden
kaçıyor.** İçlerinde 1:2 ↔ 37:182 ve **94:5 ↔ 94:6 (ARDIŞIK iki ayet!)** de var.

**Ve bu, üçüncü "yanlış birim / yanlış tolerans" alanı:**

| alan | doğru kavram | bağlandığı yanlış şey |
|---|---|---|
| adsız aktör (833) | adlandırılmamışlık | belirsizlik (INDEF) |
| nakarat (844) | tekrar | ayet tekrarı |
| **esit (854)** | **benzerlik** | **tam dizge** |

**Üçünün onarımı da aynı altyapıyı istiyor: n-gram / yaklaşık eşleme.** Aday 850'nin
ihtiyacı (donmuş kalıbı anlamsal birliktelikten ayırmak) da aynı altyapı.
**DÖRT P0 tek araçla çözülebilir.**

Ucuz ilk onarım: eşleme öncesi baştaki `و`/`ف` kırpılsın → **29 ayet kazanılır, maliyet
sıfır.** KAPATILAMAZ: yalnız baştaki bağlaç farkı tarandı; ara farklar ölçülmedi.

Ve bir işlev: **xref yoğunluğu, `esit`in kaçırdıklarını buluyor** (aday 860). 27:80'de
`esit` boş ama **beş 3-gram'ın beşi de 30:52'ye** düşüyor. Aynı desen dört vakada
(27:10, 27:19, 27:55, 27:80). **Yani xref yoğunluğu, esit onarımı için hazır bir aday
üreteci.**

## ÜÇ DİZİ KAPANDI

**Aday 804 — mühür** (aday 856): sûrede **altı mühür, altı FARKLI çift, altısı da `م`
fâsılalı ve altısı da GEÇERLİ.** Son sınama 27:78 (`عَزِيز|عَلِيم`) tuttu. **Ön-kayıt eksik
alan üzerine kuruluydu, ZAYIF etiketliydi ve iki sınamanın ikisinde de tuttu** — aday
722'nin deseni burada tutmadı, çünkü **mühür bayrağı eksik alanın kendisi değil, onun
üzerine kurulu yapısal bir hesap.**

**Aday 803 — sıfat-esmâ artefaktları** (aday 857):

| lemma | token | artefakt | göndergeler |
|---|---|---|---|
| `مُبِين` | **6** | **6** | kitâb · sihr · fadl · sultân · kitâb · hak |
| `مُؤْمِن` | **3** | **3** | insan (üçünde de) |
| `آخِر` | **4** | **4** | âhiret (dördünde de) |

Sûre 26'nın 15 `مُؤْمِن` tokeniyle birlikte **iki sûrede on sekiz token ve hepsi
artefakt.** Ders 774 karşılandı: diziler sûre sonuna kadar okunmadan kapatılmadı.

## ADAY 818 — TEK SINAMA KALDI (aday 858)

27:75, 27:77, 27:79 → **üçü de artefakt.** Ayrım **32/32**: mühür tokeninde 12/12
geçerli, mühürsüz tokende **0/20**. **Sekiz sınamanın yedisi geçti; ön-kaydın kaderi tek
bir ayete indi: 27:88 `خَبِير`.** İki sonuç da bilgi verir.

## z'NİN UZUNLUK NORMALİZASYONU — EN ÇARPICI VAKA (aday 859)

| ayet | n | lafız | allah z | yıldız |
|---|---|---|---|---|
| **27:79** | **7** | **1** | **2,33** | **★★** |
| 27:63 | 20 | 2 | 1,47 | 0 |
| 27:59 | 12 | 2 | 2,80 | ★★ |
| 27:44 | 28 | 3 eksen işareti | 0,19 / 1,20 | ★ (uzunluktan) |

**Tek lafız, iki lafızdan yüksek z.** Dört vaka aynı sûrede ve tek değişken n. **Yıldız
alanının "eksen" ölçüsü aslında "eksen yoğunluğu" — ayrı bir ölçü ve adı alanda
görünmüyor.**

## DİĞER

- **529 kümesi sûre 27'de BEŞ vakaya çıktı** (aday 861): `سمو` · `هدي` · `طير` · `كشف` ·
  `خلف`. **`هدي` sûrede altı geçiş ve DÖRT anlam alanı** (yol bulma · hediye · tanıma ·
  hidâyet) — kümenin en dallanmış vakası. Karşı örnek güçlendi: `نظر` **sekiz** geçiş,
  tek anlam alanı. **Sorun sıklık değil, lemma yapısı.** Otomatik ölçüt **2/9**;
  terk edilmesi önerisi güçleniyor.
- **27:46 ↔ 27:72** (aday 863): aynı bab X fiili, yirmi altı ayet arayla, iki ayrı
  **muhataba** (Semûd / Mekke). Aday 812'nin "konuşmacı-arası kalıp yankısı" türünün
  ikinci vakası — ve burada değişen konuşmacı değil **muhatap**; iki ayrı alt tür olabilir.
- **Blokta yıldızların TAMAMI eksenden** (aday 862) — okumada ilk kez. ★★ 3 (27:74 Rab ·
  27:78 Rab · 27:79 lafız) · ★ 1 (27:73 Rab). **Not: 27:78'de mühür var ve mühür yıldıza
  katkı vermiyor** — esmâ ve yıldız alanları bağımsız; esmâ, çıpa/yıldız korelasyonunda
  kontrol değişkeni olarak kullanılabilir.
- **Sûrede ilk ve tek "kitab" türü adlı aktör: `قُرْءان`** (27:76). Sûrenin aktör türü
  envanteri tamamlandı: kişi · kavim · gayb · kitab.
- **Blok bilançosu:** ★★ 3 · ★ 1 · yıldızsız 6. İltifât 0/10. **Rab 3 — okumada en
  yüksek blok Rab sayısı.** Yeni kök 2 (`ردف`, `كنن`). **Yıldızsız oran %60 — altı blok
  sonra ilk kez %80'in altında.** Ortalama n=8,6 — **okumadaki en kısa blok.**
- Sûre 27 ilk seksen ayet: **A/R = 3,00** (kırkta 1,40 · ellide 2,80 · altmışta 3,40 ·
  yetmişte 4,60). **Oran yetmişte tepe yapıp düştü — "monoton artıyor" kaydı DÜŞTÜ.**

### DEVAM NOKTASI

**Sûre 27, ayet 81.** Blok 27:81-93 (on üç ayet — **sûrenin son bloğu**).
Beklenenler *(defterden doğrulandı)*: **27:88 `خَبِير` — aday 818'in SEKİZİNCİ ve SON
sınaması; ön-kayıt burada ya tutacak ya düşecek** · 27:91 ve 27:93'te `رَبّ` (sûrenin
dokuzuncu ve onuncu Rabbi) · **27:81 ↔ 30:53 muhtemelen ikinci bir `esit` yanlış
negatifi — aday 854'ün doğrudan sınaması** · sûre kapanışında **tam sûre bilançosu**
çıkarılacak: yıldız dağılımı, esmâ 33 token, iltifât 3, nakarat 0, A/R, ve **aday 781'in
26/27 kontrollü çifti için sûre 27 tarafının tamamlanması.**


---

# BLOK 27:81-93 — DİRİLİŞ SAHNESİ, DAĞLARIN YÜRÜYÜŞÜ, SÛRE KAPANIŞI

**On üç ayet okundu. SÛRE 27 TAMAMLANDI (93/93). Okunan toplam 2042 / 6236 (%32,7).**
**Aday 865-876 · bağ AG_neml 84 → 95 · kok_turkce 1027 → 1032.**

## DENETİM

`turkce_denetim.py` → **0 ihlâl** (1032 kök) · `anahtar_denetim.py` → **22252 anahtar /
58 ihlâl**, taban ile **tam diff = 0**.

## ★ ADAY 818'İN ÖN-KAYDI TUTTU (aday 865, P0)

Ön-kayıt şuydu: *"sûrenin kalan mühürsüz esmâ tokenlerinden en az biri GEÇERLİ çıkacak ve
mühür bayrağının kusursuz ayrımı bozulacak"*; gerekçe **yapısaldı** — bayrak iki esmânın
bitişikliğini arar, tek başına gelen geçerli bir ismi tanım gereği yakalayamaz.

**27:88: `خَبِير` mühürsüz ve göndergesi İLÂHÎ** (`إِنَّهُۥ`, mercii `صُنْعَ ٱللَّهِ`).
Ayrım 32/32'den **33/34**'e düştü. **Ve düştüğü yer de öngörülen yer: son ta'lîl
cümlesinde tek başına duran bir isim.**

Sonuç: **mühür bayrağı gönderge geçerliliği için YETERLİ ama GEREKLİ DEĞİL.** Sûre 27'de
**12/12 mühür tokeni geçerli** (yanlış pozitif sıfır), **20/21 mühürsüz token artefakt**
(yanlış negatif bir). **Esmâ onarımında bayrak güvenilir bir POZİTİF filtre; negatif
filtre değil.**

Bu, okumada **yapısal gerekçeyle kurulup kendi deseninin bozulacağını öngören ilk
ön-kayıt** ve tuttu.

## ★ SÛRE 27 KAPANIŞ BİLANÇOSU (aday 871)

| ölçü | değer |
|---|---|
| ayet · ortalama n | 93 · **12,38** |
| fâsıla | 84 `ن` + 9 `م` · kırılma 0 |
| **yıldız** | ★★★ **9** · ★★ **9** · ★ **10** · yıldızsız **65 (%69,9)** |
| eksen | lafız 27 token / 25 ayet · Rab 12 token / 10 ayet → **A/R = 2,25** |
| esmâ | **33 token**; 12 mühür tokeni (**6/6 geçerli**), 21 mühürsüz (**20/21 artefakt**) |
| iltifât | **3** (anlatı içi · alıntı sınırı · emir zinciri) |
| hapaks | 5 ayet / 6 kök |
| edilgen | 16 ayet |
| aktör | adlı 25 token (en az 1 artefakt) · **adsız 1 token** |
| `esit` | 3 ayet dolu · **en az 2 yanlış negatif** |
| `nakarat` | **0** — oysa üç ayet-içi nakarat var |

**Anlatı bölütleri:** Mûsâ 8 · Dâvûd-Süleymân **30** · Semûd 9 · Lût 5 · doğa 5 ayet.

## ★ YILDIZ KAYNAKLARI — İÇERİK SIFIR (aday 872, P0)

Yıldızlı 28 ayetin kaynak dağılımı:

| kaynak | ayet |
|---|---|
| **edilgenlik** | **11 (%39)** |
| hapaks | 5 |
| lafız | 5 |
| Rab | 5 |
| uzunluk | 3 |
| **içerik** | **0** |

Ve sûrenin doğaya değen sekiz ayeti (27:24 güneş · 27:60-64 doğa bölütü · 27:86
gece-gündüz · 27:88 dağlar) **toplam iki yıldız** alıyor; **ikisinin de kaynağı başka**
(27:60 uzunluk, 27:88 hapaks).

**Aday 599/602/799/809/838/849 dizisinin sûre çapında tam sayımlı kapanışı.**

## ÇIPA — KARAR VERİLEMEYEN AYET (27:88)

Ayet bir **görünüş-durum ayrımı** (dağları donuk sanırsın, oysa geçerler) ve bir
**karşılaştırma** (bulutların geçişi gibi) kuruyor. **Bu kat, "adlandırma"nın ve 27:60'ın
"nedensel bağımlılık + yeti sınırı" katının üstünde.** Ama ölçü, mekanizma ve hız yok.

**Sıkı ölçütle DÜŞER, 27:60'ta önerilen gevşek ölçütle GEÇER — yani 27:88 iki aday çıpa
tanımını birbirinden AYIRAN ayettir.** Karar P0 #6'ya bırakıldı, 🜁/🜂 yazılmadı.

## DÖRDÜNCÜ VE BEŞİNCİ ALAN ARIZASI

**`MM` (mef'ûl-i mutlak) — bir ONARIM yeni arıza üretmiş** (aday 867): `defter5.py`'nin
kendi çıktısı kaydediyor — eski kural **175 ayet**, yeni kural **3 ayet** (17:26, 27:88,
84:8). Sûre 27'de eski kurala uyan üç ayet var ve yeni kural yalnız 27:88'i etiketliyor.
**`مَكَرُوا۟ مَكْرًا` (27:50) ders kitabı örneğidir ve alan görmüyor.** Elli sekiz kat
daralma. **DERS: onarımlar kendi yanlış negatif denetiminden geçmeli.**

**Adlı aktör envanterinde cins isimler var** (aday 868): `مُسْلِم` **14 token**, hepsi
"kavim" türünde; `نَصْرانِيّ` 15 token. **Aday 802/833'ün adsız tarafta bulduğu arızanın
adlı taraftaki karşılığı: alan "özel ad"ı "envanterde bulunma" ile karıştırıyor.** Ölçüt
morfolojinin PN etiketi olmalı.

## ★ SÛRE 27'NİN ASIL ÇIKTISI: BEŞ ALANDA MEKANİZMA (aday 876, P0)

| alan | doğru kavram | bağlandığı yanlış şey | aday |
|---|---|---|---|
| adsız aktör | adlandırılmamışlık | belirsizlik (INDEF) | 833 |
| nakarat | tekrar | ayet tekrarı | 844 |
| esit | benzerlik | tam dizge | 854 |
| MM | mef'ûl-i mutlak | VN etiketi (aşırı dar) | 867 |
| adlı aktör | özel ad | envanterde bulunma | 868 |

**Dördü aynı aileden: doğru kavram, yanlış birim.** Ve **üçünün onarımı tek altyapıyı
paylaşıyor: n-gram / yaklaşık eşleme** (nakarat, esit, aday 850'nin "aynı ifade" alanı).

**TUR SONU ONARIM EVRESİ İÇİN ÖNCELİK SIRASI:**
1. **n-gram altyapısı** — üç alanı birden açar (nakarat, esit, aynı-ifade)
2. **adsız aktör belirlilik koşulunun kaldırılması** — en ucuz, tek satır
3. **adlı aktör envanterinin PN etiketiyle denetimi**
4. **MM ara ölçütü** (V + aynı kök + ACC/INDEF isim)
5. **dikey katmanın "aynı sahne" kaynak listesi** (aday 835)

## DİĞER

- **529 kümesi sûre 27'de ALTI vaka** (aday 874): `سمو` · `هدي` (**dört anlam alanı,
  sekiz geçiş**) · `طير` · `كشف` · `خلف` · `أمن`. Karşı örnek `نظر`: sekiz geçiş, tek
  alan. **Otomatik ölçüt 2/10 — TERK EDİLMESİ ÖNERİLİYOR.**
- **Üç ayet-içi nakarat, alan sıfır** (aday 870): `أَءِلَٰهٌ مَّعَ ٱللَّهِ` (5×, 27:60-64,
  korpusta başka yerde yok) · `كَيْفَ كَانَ عَٰقِبَةُ` (3×) · `وَقَعَ ٱلْقَوْلُ عَلَيْهِم`
  (2×). **UYARI: aday 700/739/771'in sûre 26 nakarat düzeltmesi yalnız tam-ayet türünü
  saydı; 26/27 karşılaştırması şu an YAPILAMAZ.**
- **`esit` yanlış negatifi ikinci vaka** (aday 869): 27:81 ↔ 30:53, fark **kelime içinde**
  bir yâ harfi. **Aday 854'ün ucuz onarımı (baştaki و/ف kırpma) bunu yakalamaz.** İki
  ardışık ayet çifti (27:80-81 ↔ 30:52-53) ve alan hiçbirini görmüyor.
- **`وزع` sûrenin iki ucunu bağlıyor** (aday 873): korpusta beş geçişli, ikisi bu sûrede —
  Süleymân'ın orduları (27:17) ve mahşerde toplananlar (27:83), altmış altı ayet arayla.
- **27:88 sûrenin en yüksek z'si**: hapaks z=6,98, iki hapaks birden (`تقن`, `جمد`).
  **Sûrenin beş hapaks ayetinin beşi de ★★★** — hapaks alanı kusursuz bir ★★★ üreticisi.
- **Blok bilançosu:** ★★★ 1 · ★ 4 · yıldızsız 8. **Sûrenin son altı yıldızlı ayetinin
  dördü edilgenlikten.** Beş yeni kök — okumadaki en yüksek blok-başı yeni kök sayısı.

### DEVAM NOKTASI

**Sûre 27 bitti. Okunan: 1 · 9-27 tam · 2 (1-20 kısmi) = 2042 / 6236 (%32,7).**

İki seçenek:
1. **TUR SONU ONARIM EVRESİ** — yukarıdaki beş maddelik öncelik sırası hazır; sınama
   kümeleri sûre 27 okumasından çıktı ve hepsi belgeli. **Özellikle (1) ve (2) ucuz ve
   üç-dört alanı birden açıyor.**
2. **Okumaya devam** — sûre 28 (Kasas) ile Mûsâ anlatısı sürer ve **27:76'daki
   `قال أيّ ملأ` xref'i 28:38'e bağlanıyordu; ayrıca 28:69 (27:74'ün xref hedefi) ve
   28:84 (27:89'un hedefi) orada.** Sûre 28 sûre 27 ile üç xref bağı paylaşıyor —
   **karşılaştırma için hazır bir komşu.**

**ÖNERİ: onarım evresi.** Gerekçe: sûre 27 okuması beş alanda mekanizma çıkardı ve
**bunların üçü aynı altyapıyla açılıyor**; onarım yapılmadan sûre 28 okuması aynı
arızaları yeniden üretecek. Ayrıca **26/27 kontrollü çifti (aday 781) nakarat onarımı
olmadan hesaplanamıyor** ve bu, okumanın en büyük birikmiş borcu.


---

# TUR SONU ONARIM EVRESİ — BİRİNCİ TUR

**Yedi onarım yapıldı. Aday 877-888. `kok_turkce` 1032 (değişmedi).**
`turkce_denetim.py` → **0** · `anahtar_denetim.py` → **22407 anahtar / 58 ihlâl, tam
diff = 0** (sayı arttı çünkü `betikler/onarim/` ve üç yeni tablo tarandı; ihlâl listesi
birebir aynı).

**Yöntem kararı: hiçbir eski alan silinmedi.** Onarılan alanlar yeni adlarla yazıldı —
`adsiz2`, `esit2`, `nakarat2`, `adli2`, `mm2` — ki sûre 27 okumasının ölçümleri yeniden
üretilebilir kalsın. `okuma_metni.json` DEĞİŞTİRİLMEDİ.

## ★ 1 — ADSIZ AKTÖR (aday 877/878) · **aday 802 ve 833 KAPANDI**

Üç değişiklik: kök → **lemma** eşleşmesi · **INDEF koşulu kaldırıldı** · ve
`aktor2.py`'nin altı kök anahtarından biri **yanlış yazılmıştı** (`ى`/`ي`), korpusta hiç
eşleşmiyordu — **57 token ölüydü.**

| | eski | yeni |
|---|---|---|
| token / ayet | 119 / 101 | **214 / 185** |
| `imrae` duyarlılık | **%16** | **%100** |
| `imrae` kesinlik | %36,4 | **%100** |

**Düşen 15 ayetin 15'i de artefakt** (`مَرِيئ` afiyetli, `رِجْل` ayak, `نُفُور` nefret,
`طُوفان` tufan, `فُرْقان` furkan …) — sıfır gerçek kayıp. Sınama kümesi **11/11**.
Lût'un karısı (beş ayet), Firavun'un karısı, İmrân'ın karısı, Ebû Leheb'in karısı artık
görünüyor. Yeni etiket: **`mer`** (eril kişi) — `امْرِئ` ailesi `imrae`'den ayrıldı.

## ★ 2 — N-GRAM ALTYAPISI (aday 880)

İskelet **morfolojinin bölütlerinden** kuruluyor ve `CONJ|PREF` bölütleri atılıyor.
6236 ayet · 77.429 kelime · birden çok ayette geçen n-gram (n=3..8) **15.098**.
**Aday 876'nın öngördüğü gibi tek altyapı üç alanı birden açtı.**

## ★ 3 — `esit` YAKIN EŞLEŞMEYE AÇILDI (aday 881) · **aday 854 ve 869 KAPANDI**

Eşik **0,95**, taranarak seçildi. **253 → 336 ayet**, tam bağ 1622, **yakın bağ 84**,
**kayıp 0**. Sınama 7/7 (en düşük benzerlik 94:5↔94:6'da 0,963).

**ONARIMIN KENDİ YANLIŞ NEGATİFİ ÇIKTI:** ilk sürüm yalnız 4-gram bloklama kullanıyordu,
üç kelimelik ayetlerin 4-gram'ı olmadığı için **46 ayet kayboldu — içlerinde sûre 26'nın
nakarat ayetleri de vardı.** İkinci sürümde tam eşleşmeler karma ile doğrudan bulunuyor.

## ★ 4 — `nakarat` N-GRAM DÜZEYİNE (aday 882) · **aday 844/845/870 KAPANDI**

Korpus **119 → 1950 ayet**, kayıp 0. Sûre 26: 34 → 62. **Sûre 27: 0 → 30 ayet, 17 kalıp.**
Üç belgelenmiş nakaratın **üçü de** yakalandı. Ve okumanın kaçırdığı dördüncü bir kalıp
çıktı: **27:39 ↔ 27:40, beş kelimelik ortak cümle** — ifrît ile kitaptan ilim sahibinin
aynı sözü kurması.

UYARI: 1950 ayet korpusun %31'i; yorumda **≥3 ayet ya da ≥4 kelime** süzgeci şart
(sûre 27'de 17 kalıbı 6'ya indiriyor).

## 5, 6, 7 — ADLI AKTÖR · MM · DİKEY KAYNAK

- **Teşhis düzeltmesi (aday 883): ADAY 868 YANLIŞTI.** Envanter korpusla birebir aynı
  (106 = 106); `مُسْلِم`'i PN etiketleyen **morfolojinin kendisi.** Arıza envanterde
  değil, kaynak veride. **Dördüncü düşen kayıt** (801, 819, 843, 883).
- **Adlı aktör** (884): mensubiyet/soyut adlar silinmedi, **`cins` türüne ayrıldı**
  (52 token). Kayıp sıfır, karar geri alınabilir.
- **MM** (885): 175 (geniş) / 3 (dar) → **125** (V + aynı kök + ACC isim, kelime
  düzeyinde). Sınama 4/4. Sûre 27: [88] → **[21, 50, 88]**.
- **Dikey kaynak** (886) · **aday 806/835/850 KAPANDI**: dört sınıf — A-tek-ayet ·
  B-tek-sahne · B2-donmuş-kalıp · C-birliktelik. Eski koruma yirmi vakanın **7'sini**
  işaretliyordu, yeni sınıflama **18'ini**. `blok_dikey.py` çıktısına etiket basılıyor.
  Aday 850'nin sınırı çözüldü: `سطر`▸`أول` 0,56 (donmuş) ile `عمي`▸`صمم` 0,25 (gerçek)
  ayrışıyor.

## ★ VERİ ARIZASI (aday 879)

**`kuran_veri.json`'da 112 ayetin metnine BESMELE GÖMÜLÜ ve `harf` alanı kirli.**
39:1 harf=47, birebir aynı 45:2 harf=28 — fark tam 19. `mora`, `n`, `fs` temiz.
**Sûre 27'de 27:1: kaydedilen harf=46, doğrusu 27.**
**KAPATILAMAZ ve ciddi borç:** `fHz`, `ebced`, `bits`, `p0110` gibi `kuran_veri` alanları
hiç denetlenmedi; aynı kirlilik onlara da geçmiş olabilir.

## SÛRE 27 ONARILMIŞ ALANLARLA (aday 887)

| alan | okuma kaydı | onarılmış |
|---|---|---|
| adsız aktör | 1 token (27:23) | **6 token** (27:23, 34, 45, 55, 56, 57) |
| nakarat | 0 | **30 ayet / 17 kalıp** |
| esit | 3 ayet | **6 ayet** (dört yakın bağ) |
| adlı aktör | 25 | 24 + 1 `cins` |
| MM | [88] | **[21, 50, 88]** |
| 27:1 harf | 46 | **27** |

**Okumada görülmeyen üç yeni bulgu:** 27:53 ↔ 41:18 yakın eşleşme · 27:71 ↔ 67:25'in de
yakın olduğu · 27:39 ↔ 27:40 ortak kalıp. **Ve 27:34, 45, 55, 56'da adsız aktör var;
okumada "aktör yok" yazılmıştı.**

## ★ TURUN ASIL DERSİ (aday 888)

**Yedi onarımın ÜÇÜ ilk sürümünde kendi yanlış negatifini üretti** (esit v1: 46 ayet ·
MM ara v1: 27:21 ve 27:50 · dikey ifade ölçütü v1: donmuş kalıplar). Aday 867 bunu bir
kez göstermişti; bu turda **üç kez daha** tekrarladı.

**ONARIM PROTOKOLÜNE KALICI MADDE: hiçbir onarım, eski alanın yakaladıklarının tamamını
yakaladığı gösterilmeden (`kaybedilen == 0`) kabul edilmez.**

### KALAN BORÇ VE DEVAM NOKTASI

1. **`harf` alanının besmele kirliliği** onarılmadı; `kuran_veri`'nin türev alanları hiç
   denetlenmedi (aday 879) — **en ağır borç bu.**
2. `esit` 0,80-0,95 bandı (54 çift) denetlenmedi.
3. **26/27 nakarat karşılaştırması artık YAPILABİLİR ama yapılmadı** (aday 781) — sûre 26
   62 ayet, sûre 27 30 ayet; ama tür dağılımı ('tam' / 'ic') çıkarılmadı.
4. `esit` alanının yedi eşik türü ve 812/863/873'ün "kalıp yankısı" sekizinci türü hâlâ
   yazılmadı (P0 #3).
5. Çıpa tanımı (P0 #6) hâlâ yazılmadı; **27:88 iki aday tanımı ayıran ayet olarak
   bekliyor.**


---

# ONARIM TURU 2 — VERİ KİRLİLİĞİ VE KONTROLLÜ ÇİFT

**Aday 889-895.** `turkce_denetim.py` → **0** · `anahtar_denetim.py` → **22407 / 58,
tam diff = 0**.

## ★ 1 — VERİ KİRLİLİĞİNİN TAM TABLOSU (aday 889)

Birebir aynı iki ayet (39:1 / 45:2) üzerinden ölçüldü:

| KİRLİ | fark | | TEMİZ |
|---|---|---|---|
| `harf` | +19 | | `ar_saf` · `mora` · `ritim_kod` |
| `fHz` | −20 | | `fasila_tipi` · `med_yuku_waqf` |
| `sesli` | −2 | | `p0110` · `mukattaa` |
| `ebced` | +786 | | |
| `mod19` | +7 | | |
| `bits` | — | | |

**112 ayet etkileniyor.** defter.json'a yalnız `harf` giriyor — ama `harf`
**`dis_sinav.py` ve `genelleme.py`'de İSTATİSTİĞE giriyor.** `fHz`, `sesli`, `ebced`,
`mod19`, `bits` bu projede kullanılmıyor ama **kardeş projenin (fonetik analiz) çekirdek
alanları; orada denetlenmeli — projeler arası borç.**

## ★ 2 — `harf`İN TANIMI GERİ ÇIKARILAMADI (aday 890)

`kuran_veri.json`'un üreteci **depoda yok.** Düz Arapça harf sayımı `harf`i üretmiyor:
temiz 6124 ayette **r = 0,99915** ama **ortalama +2,94 (std 3,01)** sabit bir fazla var.

Bu yüzden alan yeniden hesaplanamadı; yalnız **besmelenin katkısı çıkarıldı**
(`harf2 = harf − 19`, 19 = 1:1'in kendi `harf` değeri).

**Doğrulama güçlü:** düzeltmeden sonra 112 ayetin sapması temiz dağılımın içine düşüyor —
**z 5,81 → −0,50.** Sûre 27: **27:1 harf 46 → 27.**

**Ama borç kapanmadı: kullanımda olan, istatistiğe giren, tanımı belgelenmemiş bir alan.**

## ★★★ 3 — ADAY 781'İN KONTROLLÜ ÇİFTİ HESAPLANDI (aday 891) — VE OKUMANIN İKİLİSİ DÜŞTÜ

| | sûre 26 | sûre 27 |
|---|---|---|
| ayet | 227 | 93 |
| nakaratlı ayet | 62 (**%27,3**) | 30 (**%32,3**) |
| **TAM ayet nakaratı** | **34** | **0** |
| ayet-içi nakarat | 28 | 30 |
| güçlü kalıp (≥3 ayet) | 9 | 2 |
| **nakaratın kelime payı** | **%23,1** | **%8,7** |
| en uzun güçlü kalıp | **11 kelime** | 3 kelime |

**Okuma boyunca "sûre 26 nakaratlı, sûre 27 nakaratsız" diye yazdım; bu ikili YANLIŞ.**
Doğrusu: **her iki sûrede de ayetlerin üçte biri bir nakarat kalıbına değiyor; sûre 26'nın
nakaratları TAM AYET ve UZUN, sûre 27'ninkiler AYET-İÇİ ve KISA.** Ayrım ikili değil,
**iki boyutlu: birim ve ağırlık.**

**Beşinci düşen kayıt** (801, 819, 843, 883, 891) **ve en pahalısı — bu bir blokta değil,
altı blok boyunca tekrarlanan bir çerçeveydi.**

## ★★★ 4 — SÛRE 26'NIN 41 ★★★'I ASLINDA 27 (aday 892)

| nakarat kümesi | ★★★ | kaynak | farklı kaynak |
|---|---|---|---|
| `inne rabbeke le-hüve'l-azîzu'r-rahîm` | **8** | `rab` | **1** |
| `fe'ttekû'llâhe ve etîûn` | **8** | `allah` | **1** |
| (nakaratsız) | 25 | rab 13 · pas 6 · hapaks 4 · karışık 2 | karışık |

**41 ★★★'ın 16'sı iki ayetin sekizer tekrarı ve her kümede kaynak TEK.**
Nakarat düzeltmeli sayı: **41 − 16 + 2 = 27 ayrı yapı.** Oran **%18,1 → %11,9.**

Sûre 27'de düzeltme gerekmiyor (dokuz ★★★'ın ikisi nakaratlı ama kaynakları ayrı
hapakslar): **%9,7.**

**KONTROLLÜ ÇİFTİN SONUCU: 26 ile 27 arasındaki ★★★ farkı %18,1'e %9,7 değil,
%11,9'a %9,7 — aradaki uçurum büyük ölçüde NAKARAT TEKRARINDAN geliyordu.**
Aday 700/739/771/779/781 bu sayıyla güncellenmeli.

## 5 — `esit`E ÜÇÜNCÜ KADEME (aday 893/894)

0,80-0,95 bandında **217 çift** var ve üstü açıkça gerçek: 27:74 ↔ 28:69 (0,945) ·
23:83 ↔ 27:68 (0,935) · 82:17 ↔ 82:18 (0,944, **ardışık ayetler**).

Alan üç kademeli: **tam 1622 · yakin 84 · benzer 280 bağ.** Ayet **253 → 520**, kayıp 0.

**Bağımsız doğrulama: 'benzer' kademesinin iki vakası okumada XREF ile zaten
bulunmuştu.** Sûre 27'de esit dolu ayet **3 → 12**; **Lût bölütünün (27:54-58) neredeyse
tamamı** artık başka sûrelerdeki paralel anlatımlarla eşleşiyor — aday 840'ın "xref
yoğunluğu ortak SAHNE ölçüyor" bulgusunun doğrudan doğrulaması.

## TURUN ASIL DERSİ (aday 895)

**Kazanç ölçüm değil, bir İDDİANIN DÜŞMESİ.** Okuma boyunca kurulan
"sûre 26 nakaratlı / sûre 27 nakaratsız" karşıtlığı yanlıştı ve bu karşıtlık üzerine
kurulan bütün karşılaştırmalar (779, 781, 829, 834, 839) yeniden yazılmalı.

**KALICI DERS: okuma sırasında kurulan İKİLİ KARŞITLIKLAR (X'li / X'siz) ölçülmeden
kullanılmamalı; ölçüldüğünde çoğu iki boyuta ayrışıyor.**

### KALAN BORÇ

1. `harf`in tanımı bilinmiyor — üreteç bulunmalı (aday 890)
2. `fHz` · `sesli` · `ebced` · `mod19` · `bits` kardeş projede kirli, denetlenmedi
3. `esit`in 0,85 eşiği örneklemeyle doğrulanmadı
4. **`esit`in yedi eşik türü + "kalıp yankısı" sekizinci türü hâlâ yazılmadı (P0 #3)** —
   artık üç vaka var: konuşmacı (27:34↔37) · muhatap (27:46↔72) · sahne (27:17↔83)
5. **Çıpa tanımı (P0 #6) hâlâ yazılmadı; 27:88 iki aday tanımı ayıran ayet olarak
   bekliyor** — ve artık tek kalan büyük P0 bu
6. Aday 779/781'in sayıları nakarat düzeltmesiyle güncellenmedi


---

# ONARIM TURU 3 — `harf`İN KURALI, ÇIPA TANIMI, VE BİR ÇERÇEVENİN DÜŞMESİ

**Aday 896-902.** `turkce_denetim.py` → **0** · `anahtar_denetim.py` → **22409 / 58,
tam diff = 0**.

## ★★★ 1 — `harf`İN KURALI GERİ ÇIKARILDI (aday 896) · **aday 890 kapandı**

Artık (`harf` − düz harf sayımı), `ar_saf`taki harf-dışı 33 kod noktasının sayımlarına
en küçük karelerle çözüldü; **bütün ağırlıklar +1 ya da 0 çıktı.**

| sayılanlar | sayılmayanlar |
|---|---|
| Arapça harfler (0621-064A) | harekeler (064B-0650) |
| elif vasla (0671) | şedde · sükûn |
| **yirmi tilâvet/vakf işareti** — küçük sîn, küçük mîm, secde işareti, rub'u'l-hizb, küçük vâv/yâ, vakf durakları | medde · hemze-üstü · **hançer elif (0670)** |

**Kural 6124 temiz ayetin 6115'inde birebir tutuyor (%99,85).**

**SONUÇ: `harf` bir harf sayımı DEĞİL — harf + vakf/tilâvet işareti sayıyor.**
Toplam değerin **%5,3'ü** işaret (341.021'in 18.009'u). Bu işaretler ayet uzunluğuyla
değil **durak konumlarıyla** dağıldığı için `harf` düz uzunluğun **sapmalı vekili.**

**Ve `harf`, `dis_sinav.py` ile `genelleme.py`'de istatistiğe giriyor** — o betiklerin
uzunluk temelli sonuçları bu karışımla üretilmiş. Yeni alanlar: **`harf3`** (saf harf) ve
**`isaret`** (vakf/tilâvet işareti). Eski `harf` ve `harf2` korundu.

## ★ 2 — ÇIPA TANIMI YAZILDI (aday 897) — P0 #6

| kademe | ölçüt |
|---|---|
| **L0** | adlandırma — olgu anılıyor, başka bir şey söylenmiyor |
| **L1** | adlandırma + alan/yeti/nitelik |
| **L2** | nedensel bağımlılık **ya da** yeti sınırı ("siz bunu yapamazdınız") |
| **L3** | görünüş-durum ayrımı + karşılaştırma |
| **L4** | mekanizma / ölçü / sınıflandırma |

Sûre 27'nin olgu içeren 17 ayeti yerleştirildi: **L0 4 · L1 8 · L2 5 · L3 1 · L4 0.**

**En önemli sonuç: L4 eşiğiyle sûre 27'de SIFIR çıpa var.** "Mekanizma/ölçü/sınıflandırma"
şartı konursa bu sûrede tek bir çıpa yok ve soru bu sûre için anlamsız hale geliyor.
L3 ile tek ayet (**27:88**), L2 ile beş ayet (27:60, 62, 64, 86, 88).

**Eşik kararı sonucuna bakılarak verilemez (döngüsel olur)** — üç eşik de raporlandı,
karar ikinci sûrenin verisine bırakıldı.

## ★★★ 3 — DÜŞEN KAYIT: "ÇIPA/YILDIZ TERS İLİŞKİSİ" YANLIŞ YÖNDE (aday 898)

Okuma boyunca **altı kez** (599/602/799/809/838/849/872) "çıpası güçlü ayetler yıldızsız
kalıyor" yazdım. Ölçüldü:

| | ayet | yıldızlı | ort n | hapakslı |
|---|---|---|---|---|
| **olgu içeren** | 17 | 8 (**%47,1**) | **18,4** | **%24** |
| diğer | 76 | 20 (%26,3) | 11,0 | %1 |

**İlişki ters değil, DÜZ.** Uzunluk eşlemeli (n≥13) karşılaştırmada da: %40'a %26.

**İki hata birleşmiş:** (a) iddia hiç sayılmadı, **el ile seçilmiş çiftlere** dayandırıldı
(27:24 yıldızsız / 27:25 ★★★ gibi — çiftler gerçek ama temsilî değil); (b) örnekler
**okuma sırasında dikkat çektikleri için** seçildi, yani örneklem ölçülmek istenen
değişkenin kendisiyle ilişkili bir süreçle oluştu.

**DOĞRU İFADE:** yıldız **içeriği ölçmüyor** (olgu ayetlerinin 8 yıldızının 8'i de
hapaks/pas/uzunluktan, **sıfırı içerikten** — aday 900, ayakta) **ama içerikle DÜZ
korele** — çünkü doğa olgusu anlatan ayetler **daha uzun** ve **nadir kelime taşıma
olasılıkları 24 kat yüksek.** Bağıntı bir **karıştırıcıdan** geliyor, içerik
duyarlılığından değil.

**Altıncı düşen kayıt** (801, 819, 843, 883, 891, 898).

## ★ PROTOKOL MADDESİ (aday 899)

Aday 891 (nakarat ikilisi) ve 898 (çıpa/yıldız) **aynı kusuru** paylaşıyor: okuma
sırasında dikkat çeken vakalardan genelleme.

**KALICI MADDE: okuma sırasında "X'li ayetler Y oluyor" biçiminde bir iddia kurulursa,
KAPATILAMAZ etiketiyle kaydedilir ve tur sonunda TAM SAYIMLA sınanır. Okuma notlarından
toplanan örneklerle sınanamaz — o örnekler okuma dikkatinin ürünüdür.**

Bu, "sûrenin sonuna kadar okunmadan dizi kapatılmaz" (774) kuralının örneklem tarafındaki
eşi ve ondan geniş: **774 EKSİK sayıma karşı koruyor, bu TARAFLI sayıma karşı.**

## ÜÇ TURUN TOPLAM DERSİ (aday 902)

On üç onarımın **üçü kendi yanlış negatifini üretti**, ve okumanın **altı kaydı düştü** —
dördü sayım hatası, **ikisi örneklem hatası.** İkincisi daha pahalı: **sayım hatası bir
bloğu, örneklem hatası bir ÇERÇEVEYİ bozuyor.**

**P0 borçlarının durumu:**

| P0 | konu | durum |
|---|---|---|
| #1 | aktör alanları (lemma+bağlam) | **KAPANDI** |
| #2 | dikey "aynı sahne" | **KAPANDI** |
| #3 | `esit`in yedi eşik türü | **AÇIK** |
| #4 | nakarat tanımı | **KAPANDI** |
| #5 | 529'un lemma katmanı | altyapı hazır, **uygulanmadı** |
| #6 | çıpa tanımı | tanım **yazıldı**, eşik **açık** |

### KALAN BORÇ

1. `fHz` · `sesli` · `ebced` · `mod19` · `bits` kardeş projede kirli, denetlenmedi
2. **`dis_sinav.py` ve `genelleme.py` kirli/karışık `harf` ile koşulmuş — yeniden
   koşulmadı**
3. `esit`in 0,85 eşiği örneklemeyle doğrulanmadı; yedi eşik türü yazılmadı (P0 #3)
4. Çıpa eşiği (L2/L3/L4) seçilmedi — **ikinci sûrenin verisi gerekli**
5. 529'un lemma katmanı uygulanmadı (P0 #5)
6. Aday 779/781'in sayıları nakarat düzeltmesiyle güncellenmedi

---

## OTURUM EKİ — SÛRE 28 (KASAS) OKUNDU, 88 AYET

Okunan: **2130 / 6236 ayet (%34,2)** · tam: sûre 1, 9-28 · kısmi: sûre 2 (1-20).
`kok_turkce.json` 1032 → **1052** (20 yeni kök).
Denetimler: `turkce_denetim.py` → **0** · `anahtar_denetim.py` → **22486 anahtar, 58
ihlâl, ihlâl listesi diff = 0** (taban tazelendi).
Adaylar **903-919** → `aday_bulgular.json/AJ_kasas` (17 kayıt).
Bağlar → `okuma_baglantilari.json/AH_kasas` (22 kayıt).

### P0 BORÇLARININ YENİ DURUMU

| P0 | konu | durum | sûre 28'den gelen |
|---|---|---|---|
| #3 | `esit`in eşik türleri | **AÇIK — ama sınama kümesi HAZIR** | dokuz vakalık küme + 111 çiftlik tam sayım (aday 904) |
| #5 | 529'un lemma katmanı | **AÇIK — kapsam BÜYÜDÜ** | on iki yeni gloss vakası + iki ÖLÇÜM vakası (aday 906) |
| #6 | çıpa eşiği | **KAPANDI** | ölçüt seçildi + mekanikleştirildi (aday 920-923) |

**#6 için karar verisi:** L4 iki sûrede de **0**, L3 iki sûrede de **0**. L2 sûre 28'de
üç kayıt veriyor ve ikisi (28:71, 28:72) **ilk kez gerçek bir doğa olgusuna** bağlı
(gece-gündüz döngüsü üzerine karşı-olgusal nedensellik). Öneri: **L2 + 'olgu/olgu-dışı'
ikinci bayrağı.** Ek bulgu: çıpa ile yıldız sûre 28'de **hiç çakışmıyor** — sekiz
★★★'ın hiçbiri çıpa taşımıyor, üç L2 ayetinin hiçbiri ★★★ değil. 🜁/🜂'nin ★★★
koşuluna bağlı kalması sûre 28'de **sıfır çıpa** üretirdi.

**#3 için hazır küme (aday 904):** TAM 3 (1,0) · BENZER 3 (0,9455 · 0,9412 · 0,9231) ·
**GERÇEK AMA YAZILMAYAN 3** (0,8333 eşikten · **0,8252 eşikten, on iki kelime birebir
ortak** · 0,7152 ön elemeden). **'yakin' kademesi (≥0,95) sûre boyunca bir kez bile
tetiklenmedi.** TAM SAYIM: en az on kelimelik birebir ortak dizi paylaşan 111 ayet
çiftinin yalnız 31'ini (%27,9) görüyor; görmediği 80'in 66'sı çapraz-sûre.

**#5 için yeni kapsam (aday 906):** borç yalnız gloss değil, **ölçüm** borcu da —
lemma katmanı olmadığı için `nakarat2` iki gerçek çifti göremiyor (28:5↔28:41 ters
yönlü `أَئِمَّةً` kalıbı; 28:30↔28:46 ters çatılı `ندي`). Sınama kümesi **on sekize**
çıktı.

### YENİ P0 BORÇLARI

7. **Yıldız formülünün iki otomatik ★★★ tetikleyicisi (aday 903).** Hapaks içeren
   358 ayetin **358'i** ve tüm fiilleri edilgen olan 124 ayetin **124'ü** istisnasız
   ★★★; birleşim 471 = tüm ★★★'ların **%53,5'i**. ★★★ sınıfı 'otomatik tetikleyici'
   ve 'süreklilik ölçütü' diye ikiye ayrılmalı. **Aday 700/739/771/779/781'in nakarat
   düzeltmesiyle güncellenecek sayıları bu ayrımdan SONRA hesaplanmalı.**
8. **`adsiz2` envanteri taraflı örneklemden türetilmiş (aday 905).** Yedi etiket, altı
   okuma çıpasından; akrabalık yoluyla ve ismi mevsûlle anılan aktörler bütünüyle
   dışarıda (lemma `أُمّ` 31 ayette, 26'sında alan boş). Ölçüt lemma listesi değil,
   'aktör konumunda ve morfolojide PN etiketi taşımayan baş isim' olmalı.
9. **Esmâ mühür bayrağının token düzeyinde çalışamayacağı kanıtlandı (aday 908).**
   `وارِث` sûre 28'de iki kez ve hükümler zıt (28:5 artefakt / 28:58 geçerli), ikisi
   de mühürsüz ve son konumda. Korpusta yedi `وارِث` tokeni, yedisi mühürsüz, üçü
   geçerli. Gönderge çözümlemesi şart.

### KAPANAN BORÇLAR

- **Aday 867 KAPANDI:** `mm2` onarımının aşırı daralması giderilmiş (175 → 3 → **125**);
  sûre 28 hem doğru pozitif (28:61, iki kayıt) hem doğru negatif (28:47) verdi (aday 915).
- **Aday 865 ikinci sûrede doğrulandı:** mühür pozitif filtre olarak kusursuz, negatif
  filtre olarak değil (sûre 27: 12/12 ve 20/21; sûre 28: 2/2 ve 15/17).
- **KAPATILAMAZ DÜŞTÜ (aday 911):** 'sûre 28 sûre 12'ye yoğun bağlanıyor' izlenimi tam
  sayımla yanlış çıktı — kaynak ayet sayısında sûre 6 (10) ve sûre 27 (7) önde, sûre 12
  altıncı (5). **Taraflı örneklem yasağının bu oturumda ilk kez bir izlenimi düşürdüğü
  vaka.**
- **Retroaktif denetim borcu kapatıldı (aday 917):** yeni eklenen `وصل` ve `صرخ`
  kökleri 13:21 ve 14:22'de karşılıksız anma açtı; `yama_retroaktif_gloss.py` ile
  düzeltildi, `turkce_denetim.py` → 0.

### ALAN DOĞRULAMALARI (olumlu kayıtlar)

- `kafiye_kirik` harfe değil **sınıfa** bakıyor ve tutarlı: sûre 28'de ن dışı yedi
  fâsıla var, yalnız biri (28:28) kırılma; `-îm` ile `-ûn`/`-în` aynı N sınıfında
  (aday 913).
- `A` alanı kök sayacı ile lafız sayacını **doğru** ayırıyor: sûre 28'de `أله` 34 kez
  geçiyor, `A` yalnız 27'sini sayıyor; 28:38'de iki cins isim var ve alan boş kalıyor
  (aday 914). **Esmâ tablosunun onarımında bu ölçüt örnek alınmalı.**
- `harf3`/`isaret` ayrımı çalışıyor: sûre 28'de işaret oranı **%4,4**, ama ayetten
  ayete **13 kat** değişiyor (28:15'te 13, beş ayette 0) — eski `harf` ile koşulan
  `dis_sinav.py` ve `genelleme.py` için fark büyüklüğü artık tahmin edilebilir (aday 916).

### KALAN BORÇ (güncellenmiş)

1. `fHz` · `sesli` · `ebced` · `mod19` · `bits` kardeş projede kirli, denetlenmedi
2. `dis_sinav.py` ve `genelleme.py` kirli `harf` ile koşulmuş — yeniden koşulmadı
3. P0 #3 — sınama kümesi hazır, eşik türleri hâlâ yazılmadı
4. P0 #6 — karar verisi tamam, eşik hâlâ seçilmedi
5. P0 #5 — on sekiz vakalık küme hazır, lemma katmanı uygulanmadı
6. Aday 700/739/771/779/781 — nakarat düzeltmesi + **aday 903'ün ★★★ ayrımı** birlikte
7. **`nakarat2` alt sınırı (aday 907):** üç kelimenin altındaki katman hiç ölçülmüyor;
   sûre 28'de sekiz gerçek tekrar bu katmanda. KAPATILAMAZ — korpus büyüklüğü ölçülmedi
8. **`fig` envanterinde karşılaştırma etiketi yok (aday 912):** sûre 28'de beş vaka.
   KAPATILAMAZ — korpus sayımı yapılmadı
9. **Orta konum × artefakt (aday 908):** sûre 28 içinde 6/6, korpus çapında sınanmadı.
   KAPATILAMAZ


---

## P0 #6 KAPANDI — ÇIPA EŞİĞİ

**ÖLÇÜT: çıpa = (L2+) VE (olgu = evet).**

| eşik | iki sûrede (181 ayet) | karar |
|---|---|---|
| **L4+** | **0 ayet** | kullanılamaz |
| **L3+** | **1 ayet** (27:88), %0,55 | kullanılamayacak kadar seyrek |
| **L2+** | 9 ayet, **tekdüze değil** — 2'si olgu-dışı (27:62, 28:10) | tek başına yetmiyor |
| **(L2+) ∧ olgu** | **7 ayet (%3,9)** | **SEÇİLDİ** |

Çıpalar: **27:60 · 27:64 · 27:86 · 27:88 · 28:71 · 28:72 · 28:73**

Karar eşiğin *sonucuna* bakılarak verilmedi (`14_cipa_tanimi.py`'nin döngüsellik
şartı); kademelerin **tekdüzeliğine** bakılarak verildi: L4 ve L3 boş ya da tek
elemanlı, L2 dolu ama iki türü karıştırıyor → ikinci bayrak şart.

### Ölçüt mekanikleştirildi — anma %100 (aday 921)

Çıpa artık okuma dikkatiyle aranmıyor. Beş morfolojik işaret ailesi:

| aile | işaret | korpus aday |
|---|---|---|
| A_şart | edim şart / kip COND / `لولا` | 339 + 20 |
| B_ta'lîl | `PRP\|PREF` (amaç lâmı) | 132 |
| C_recâ | `لعل` / `كي` | 98 |
| D_yeti | olumsuzluk + `كون` + `أَن`; 'başka ilâh' kalıbı | 77 |
| E_görünüş | sanma fiili + `CIRC\|PREF` (hâl vâvı) | 23 |

Aday = olgu alanından en az bir kök **VE** en az bir işaret → **586 ayet (korpusun
%9,4'ü)**, anma elle kurulmuş yedi çıpaya karşı **7/7 (%100)**, kesinlik iki okunan
sûrede **7/21 (%33)**.

İlk sürüm (yalnız şart + sözlük) %57'de kalmıştı; kaçan üç çıpanın (27:60, 27:86,
27:88) işaretleri **morfolojide zaten vardı ama taranmıyordu.** Ders: bir ölçütün
"okumayla bulunur" sayılması çoğu zaman ölçütün morfolojiye bağlanmamış olmasından
kaynaklanıyor.

### Çıpa ile yıldız BAĞIMSIZ (aday 922)

Eşik seçildikten **sonra** hesaplandı:

- yedi çıpanın 3'ü yıldızlı (%42,9) · iki sûre tabanı %30,4
- **binom P(X≥3 | n=7, p=0,304) = 0,362 — ANLAMLI DEĞİL**
- kademe × yıldız tekdüze değil ve **yönü ters**: L0 %44 · L1 %50 · **L2 %25** · L3 %100 (n=1)
- üç yıldızlı çıpanın kaynakları: 27:60 → `n` · 27:88 → `hapaks` · 28:71 → `allah`;
  **hiçbiri içerikten**
- tarama havuzunun yıldız oranı %50 (taban %35,4) ama bu **uzunluk artefaktı**:
  havuz ort n=23,00, korpus 12,42 — **1,9 kat** (aday 903/909)

**KARAR: 🜁/🜂 ★★★ koşuluna BAĞLANAMAZ.** Bağlansaydı yedi çıpanın altısı düşerdi
(yalnız 27:88 ★★★ kalırdı). Semboller yıldızdan bağımsızlaştırıldı.

### P0 #6'nın tavanını P0 #5 belirliyor (aday 923)

Sûre 27-28'deki 14 yanlış pozitifin **6'sı (%43) lemma kusurundan**: `ظلم` →
ظُلْم/ظالِم (karanlık değil zulüm) · `صبح` → أَصْبَحَ (sabah değil yardımcı fiil) ·
`حيي` → اسْتِحْياء (hayat değil hayâ) · `قدر` → قَدَرَ. **Lemma katmanı yazılsaydı
kesinlik %33'ten %47'ye çıkardı.**

Bu, aday 906'nın "lemma borcu yalnız gloss değil **ölçüm** borcu" kaydının **ikinci
bağımsız doğrulaması** — birincisi `nakarat2`'nin iki çifti kaçırmasıydı. İki ayrı
alan aynı eksik katman yüzünden sakat.

### DÜŞEN KAYITLAR — aday 910 düşürüldü, silinmedi

Okuma sırasında kurduğum **dört kayıt** P0 #6 kapatılırken düştü:

1. "L3 iki sûrede de sıfır" → **yanlış**, 27:88 L3
2. "sûre 27'de L2 kayıtları olgu-dışıydı" → **yanlış**, dört L2'den ikisi gerçek olgu
   (27:60, 27:86)
3. "28:71-72 ilk kez L2 gerçek bir doğa olgusuna uygulanıyor" → korpus düzeyinde
   **yanlış**; doğrusu "sûre 28'de ilk kez"
4. 28:73 okuma sırasında L1 kaydedilmişti → emsaliyle (27:86) **L2** olmalı

**Ortak sebep: dördü de sûre 27'nin tablosuna bakılmadan, okuma anındaki hatıradan
kuruldu — aday 843'ün ("sayım defterden koşulur, hafızadan değil") çıpa tarafındaki
eşi.** Alınan önlem: `15_cipa_kademe_28.py`'nin her satırı sûre 27'den hangi ayetle
aynı kademeye konduğunu (emsal) taşımak zorunda.

Aday 910'un özgün `olculen` alanı korundu; yanına `dusuruldu` alanı eklendi.

---

## OTURUM EKİ — SÛRE 29 (ANKEBÛT) OKUNDU, 69 AYET

Okunan: **2199 / 6236 ayet (%35,3)** · tam: sûre 1, 9-29 · kısmi: sûre 2 (1-20).
`kok_turkce.json` 1052 → **1059** (7 yeni kök; üç sûrede toplam 27).
Denetimler: `turkce_denetim.py` → **0** · `anahtar_denetim.py` → **22754 anahtar, 58
ihlâl, ihlâl listesi diff = 0** (taban tazelendi).
Adaylar **924-936** → `aday_bulgular.json/AK_ankebut` (13 kayıt).
Bağlar → `okuma_baglantilari.json/AI_ankebut` (23 kayıt).

### P0 #6'NIN İLK BAĞIMSIZ SINAMASI — VE ADAY 921'İN DÜZELTİLMESİ

**Çıpa tarayıcısı sûre 29'da kurulum kümesi dışında ilk kez sınandı ve üç çıpayı
kaçırdı** (29:14 L4 · 29:19 L2 · 29:20 L2). **Aday 921'in "anma 7/7 (%100)" kaydı
DÖNGÜSELDİ** — ölçüm, tarayıcının yakalamak için yazıldığı yedi ayet üzerindeydi.
Tutulan kümede ilk anma **0/3**.

İki yeni işaret ailesi eklendi ve yeniden ölçüldü (aday 924):

| aile | işaret | korpus aday |
|---|---|---|
| **F_ölçü** | iki ya da daha fazla sayı işareti | 110 |
| **G_bakış** | `رأي`/`نظر` + olgu kökü + (soru ya da EMİR kipi), `عقب` HARİÇ | 100 |

`G_bakış`ı emir kipine açmak ilk denemede `فَٱنظُرْ كَيْفَ كَانَ عَٰقِبَةُ` kalıbını
topladı (27:14, 27:51, 27:69, 28:40) — **o tarihe bakış çağrısıdır, olguya değil** — ve
`عقب` kökü dışlanarak ayrıldı. **Havuz 537 → 772 → 680 (korpusun %10,9'u) · kurulum
kümesinde anma 7/7 · TUTULAN kümede anma 3/3 · kesinlik 27 %57, 28 %23, 29 %30.**

**DERS (aday 924): bir tarayıcının kendi kurulum kümesindeki anması bilgi taşımaz.**
Aday 899'un (taraflı örneklem yasağı) ölçüm tarafındaki eşi. Her ölçüt, yazıldıktan
sonra bulunan bir tutulan küme üzerinde sınanmalı.

### OKUMANIN İLK İKİ L4 KAYDI (aday 925)

- **29:14 — ÖLÇÜ kolu:** `أَلْفَ سَنَةٍ إِلَّا خَمْسِينَ عَامًا`, birimli nicelik, iki
  ayrı birim adı, bir çıkarma işlemi. 27:39/40 **birim olmadığı için** L1'de kalmıştı.
- **29:40 — SINIFLAMA kolu:** dört helâk türü ayrı adlandırılıyor (`حاصِب` · `صَيْحَة` ·
  `خَسْف` · `إغراق`). 27:17'de üç sınıflı ordu L1 kalmıştı çünkü sınıflanan şey olgu
  değildi; burada **fiziksel olaylar** ve her birinin mekanizma adı var.
- **Üçüncü kol — MEKANİZMA — hâlâ boş.** Dört sûrede 319 ayet, iki L4: **%0,6.**

P0 #6'nın "L4 kullanılamaz" kararı **değişmiyor** (ölçüt hâlâ (L2+) ∧ olgu) ama **L4'ün
boş olmadığı artık ölçülü ve iki kolu da örneklendi.**

**Çıpa ölçütünün ayırt ediciliğinin en temiz gösterimi 29:61/29:63 çifti:** ikisi de aynı
`لَئِن سَأَلْتَهُم` kalıbıyla açılıyor, **29:61 daha ÇOK olgu kökü taşıyor (altı) ve
L1'de kalıyor, 29:63 daha AZ taşıyor (dört) ve L2'ye çıkıyor.**

### YENİ P0 BORÇLARI

10. **`hapaks` alanı ayet değil token sayıyor (aday 926).** Korpusta tek ayette geçen
    **420** kökün **399'u** hapaks sayılıyor, **21'i sayılmıyor** — o ayette birden çok
    token taşıdıkları için. **29:41'in `عنكب` kökü (sûrenin adı) korpusta tek ayette ve
    ayet YILDIZSIZ**; yedi ayet sonra `خطط` tek token olduğu için ★★★. Kaçan 21 ayetin
    beşi bütünüyle nişansız. **Onarım: ölçüt "tek AYETTE geçen kök" olmalı; hapaks kök
    399 → 420, hapaks ayeti 358 → 379, beş yeni ★★★. Aday 903'ün korpus sayıları bu
    onarımdan sonra yeniden hesaplanmalı.**
11. **`fig` KELLA'yı `كُلّ` ile karıştırıyor (aday 927).** `fig`=KELLA olan **48** ayetin
    **15'inde (%31)** morfolojide `LEM:كَلّا` yok; 14'ünde `كلل` kökü var. Yanlış negatif
    **sıfır**. **Onarım: ölçüt `LEM:كَلّا` olmalı.** Yan bulgu: alan üç sûrelik okumada
    ilk kez tetiklendi ve ilk tetiklenişinde yanlış çıktı — **seyrek etiketlerin denetlenme
    fırsatı çok az** (`QASEM` 71, `AMMA` 52, `MM` 3 aynı yöntemle denetlenmeli).
12. **Esmâ mühür bayrağı token düzeyinde çalışamıyor — ikinci vaka (aday 930).** `شَهِيد`
    tokeni 28:75'te orta konumda **artefakt**, 29:52'de orta konumda **geçerli**. Birinci
    vaka (`وارِث`, aday 908) aynı sûre içindeydi; **bu ikisi iki ayrı sûrede, yani kusur
    sûre bağlamıyla da açıklanamıyor.**

### KAPANAN / DOĞRULANAN

- **`esit2` onarımı yanlış negatif üretmemiş (aday 928, olumlu).** Eski `esit` **253**
  ayette dolu, `esit2` **520**'de, **kesişim tam 253**; eski dolu ama yeni boş **sıfır**.
  **`mm2`'nin (175 → 3 → 125) tersi: kaybetmeden genişlemiş bir onarım.** DERS: gevşeten
  onarımlar yanlış negatif riski taşımıyor, **daraltanlar taşıyor.**
- **`esit2`'nin 'yakin' kademesi ilk kez tetiklendi (aday 929):** 29:28 ↔ 7:80, oran
  0,9615. **TAM SAYIM — korpus kademe dağılımı: tam 1622 · benzer 280 · yakin 84.**
  Aday 904'ün kaydı çürümüyor, **niceliğe bağlanıyor: üst bant 'benzer'in üçte biri.**
- **`kafiye_kirik` yerel komşuluğu ölçüyor (aday 933, olumlu).** 29:21-22 ardışık kırılma
  — okumada ilk kez; **29:21 sûre normuna (N) UYUYOR ve yine de kırılma sayılıyor.**
  TAM SAYIM: 230 kırılmanın **35'i ardışık çift.** Aday 913'e ikinci boyut: alan "sûre
  normundan sapma"yı değil **yerel kafiye tekilliği**ni ölçüyor.
- **Payda etkisi beşinci doğrulama (aday 931).** `rab` tek sûrede 1,45 → 3,23 → **3,94**
  (aynı token sayısı, üç payda). `allah`: 29:5 (2/12) ve 29:11 (**1/6**) ikisi de **z=2,80**
  — aynı oran, aynı z, aynı yıldız. `pas` determinizmi dört vakayla (28:60, 28:88, 29:18,
  29:49 → hepsi 2,52).
- **Retroaktif denetim borcu ikinci kez (aday 917'nin tekrarı):** yeni eklenen `ركب` ve
  `يأس` kökleri 11:42, 12:87 ve 12:110'da karşılıksız anma açtı;
  `yama_retroaktif_gloss_29.py` ile düzeltildi, `turkce_denetim.py` → 0. **Her yeni kök
  eklemesi bir retroaktif tur gerektiriyor ve bu artık iki sûrede de gerçekleşti.**

### KALAN BORÇ (güncellenmiş)

1. `fHz` · `sesli` · `ebced` · `mod19` · `bits` kardeş projede kirli, denetlenmedi
2. `dis_sinav.py` ve `genelleme.py` kirli `harf` ile koşulmuş — yeniden koşulmadı
3. **P0 #3** — sınama kümesi hazır (dokuz vaka + korpus kademe dağılımı), eşik türleri
   yazılmadı
4. **P0 #5** — sınama kümesi **yirmi iki vakaya** çıktı (27: 6 · 28: 12 · 29: 4); artık
   **üç ayrı alanın** (nakarat2, çıpa taraması, gloss) tavanını belirliyor
5. Aday 700/739/771/779/781 — nakarat düzeltmesi + aday 903'ün ★★★ ayrımı + **aday
   926'nın hapaks onarımı** birlikte
6. **`nakarat2` alt sınırı (aday 907/935):** sûre 29'da beş kez ısırdı; ayrıca **iki alan
   aynı büyüklükteki kalıba farklı davranıyor** — 29:32↔33 `dugum.ic`=1 alıyor, 29:31↔34
   almıyor (sebep: `dugum` lemma 3-gram'ı, `nakarat2` yüzey n-gram'ı kullanıyor)
7. `fig` envanterinde karşılaştırma etiketi yok (aday 912) · **ve merdivende
   karşılaştırmalı sıralama için basamak yok** (29:41 `أَوْهَنَ ٱلْبُيُوتِ`) — KAPATILAMAZ
8. Orta konum × artefakt (aday 908/930): iki sûrede iki karşı vaka, korpus sınanmadı
9. **A/R oranı üç sûrede 2,25 → 1,42 → 8,4 (aday 932)** — korpus dağılımı çıkarılmadı,
   KAPATILAMAZ

---

## ONARIM 14 ve 15 — P0 #10 ve #11 KAPANDI

Protokole uygun: **hiçbir eski alan silinmedi**, onarımlar yeni adlarla yazıldı ve
`okuma_metni.json` değiştirilmedi.

| eski | yeni | ne değişti | aday |
|---|---|---|---|
| `hapaks` | **`hapaks2`** (+ `z2`, `yildiz2`) | ölçüt TOKEN'dan AYET'e; 399 → **420** kök | 926 → **937** |
| `fig` içindeki `KELLA` | **`fig2`** | yüzey biçimi → `LEM:كَلّا`; 48 → **33** ayet | 927 → **938** |

### Onarım 14 — `hapaks2`

`hapaks` bir kökün *nadirliğini* ölçmek istiyordu ama **token** sayıyordu. Korpusta tek
ayette geçen **420** kökün **21'i**, o ayette birden çok token taşıdığı için düşüyordu.

- **kaybedilen = 0** (`hapaks2 ⊇ hapaks`; eski dolu ama yeni boş olan ayet **sıfır**)
- **sınama kümesi 12/12** — okuma kayıtlarından kuruldu: sûre 28-29'un sekiz belgelenmiş
  hapaks ayeti korundu · 29:41 (okumada "sayılmıyor" diye kaydedilen vaka) artık sayılıyor
  · 28:12 ve 29:40 (okumada "nadirlik yığılması ile hapaks ayrı şeyler" diye kaydedilen
  vakalar) boş kaldı
- **hapaks ayeti 358 → 375 · yıldız değiştiren ayet 10** (beşi ★0 → ★★★):
  2:197 · 7:176 · 11:99 · 13:4 · **19:83** · **29:41** · **43:79** · **55:33** · **79:2** · 84:6
- **En çarpıcı düzeltme 29:41:** sûrenin adını taşıyan kök (`عنكب`) korpusta yalnız o
  ayette geçiyor ve ayet **yıldızsızdı**, artık ★★★.

### Onarım 15 — `fig2`

KELLA etiketli **48** ayetin **15'inde (%31)** morfolojide `LEM:كَلّا` yok; 14'ünde `كلل`
kökü var.

- **kaybedilen = 0 iki yönden:** gerçek KELLA'ların hiçbiri düşmedi (**yanlış negatif
  sıfır**) ve KELLA dışındaki sekiz etiketin hiçbiri değişmedi
- **sınama kümesi 8/8**
- düşen 15 ayet: 4:95 · 4:130 · 6:84 · 6:86 · 7:46 · 11:111 · 11:120 · 17:20 · 17:23 ·
  19:49 · 21:72 · 21:79 · **25:39** · **29:40** · **57:10**
- Aday 927'nin listesi on üç vakayla yazılmıştı; **tam sayım on beş verdi** (25:39, 57:10
  eklendi)

### Aday 903 tazelendi (aday 939)

İki otomatik ★★★ tetikleyicisi `hapaks2` ile yeniden hesaplandı:

| tetikleyici | ayet | hepsi ★★★ mi |
|---|---|---|
| ≥1 hapaks2 kök | **375** | **evet, istisnasız** |
| bütün fiilleri edilgen | **124** | **evet, istisnasız** |
| kesişim | 13 | — |
| **birleşim** | **486** | `yildiz2` ile ★★★ olan **890** ayetin **%54,6'sı** (eskiden %53,5) |

Tek hapaks kökün z'si **3,38 → 3,28** (dağılım değişti) ama hâlâ eşiğin (>3) üstünde:
**hapaks tek başına yeter şart olmayı sürdürüyor.**

### DÜŞEN KAYITLAR — aday 926'nın iki öngörüsü

| öngörü | gerçek |
|---|---|
| "hapaks ayeti 358 → **379**" | 358 → **375** |
| "**beş** yeni ★★★" | **10 ayet** yıldız değiştirdi, **beşi** yıldızsızdan ★★★'a |

**Ortak sebep: kaçan 21 kökün AYET dağılımı hesaplanmadan kök sayısından ayet sayısına
doğrudan geçilmişti.** Aday 843'ün ("sayım defterden koşulur, hafızadan değil") üçüncü
tekrarı — bu kez hafızadan değil, **koşulmamış bir aritmetikten.** Özgün `olculen`
korundu, yanına `dusuruldu` alanı eklendi.

### Açık P0'ların yeni durumu

| P0 | konu | durum |
|---|---|---|
| #3 | `esit` eşik türleri | AÇIK — sınama kümesi hazır |
| #5 | 529 lemma katmanı | AÇIK — **yirmi iki vaka, üç alanın tavanı** |
| #7 | yıldızın iki otomatik ★★★ tetikleyicisi | AÇIK — sayılar tazelendi (aday 939) |
| #8 | `adsiz2` envanteri | AÇIK |
| #9/#12 | esmâ mührü token düzeyinde çalışamıyor | AÇIK — iki vaka (908, 930) |
| **#10** | **`hapaks` ayet değil token sayıyor** | **KAPANDI** (aday 937) |
| **#11** | **`fig` KELLA'yı `كُلّ` ile karıştırıyor** | **KAPANDI** (aday 938) |

---

## P0 #5 — LEMMA KATMANI: (a) PARÇASI KAPANDI, (b) AÇIK

Proje kendi kaydı: **"Envanter çıkarılmadan onarım kararı verilmeyecek."** Envanter
çıkarıldı ve üç katman önerisi ölçüldü.

### Katman ölçümü — 28 belgelenmiş vaka (aday 940)

| katman | çözdüğü vaka |
|---|---|
| **LEMMA** | **22** |
| BAĞLAM | 6 — `كشف` · `عوم` · `أيي` · `صبح` · `قدر` · `هوي` |
| **BAB** | **0** |

**Aday 569/584'ün bab önerisi DÜŞTÜ: lemma katmanı onu kapsıyor.** Önerinin çözdüğünü
iddia ettiği vakaları (`صرف` · `قرن` · `رجو` · `طلق`) lemma zaten ayırıyor; bab hiçbir
ek vaka çözmüyor ve daha ucuz da değil (aynı morfoloji alanından geliyor).

**İkinci bulgu:** çok alanlı karşılık taşıyan 173 kökün **12'si TEK LEMMALI** — onları
lemma katmanı hiçbir koşulda çözemez.

### Maliyet ve ikiye ayırma (aday 941)

| parça | ne ister | maliyet | durum |
|---|---|---|---|
| **(a) LEMMA KİMLİĞİ** | morfolojideki `LEM` alanı | **0** | **KAPANDI** |
| (b) LEMMA GLOSSU | (kök, lemma) Türkçe karşılık | 3737 satır (okunanda **2537**) | AÇIK |

**Ayrımın kendisi bulgu:** P0 #5 üç oturumdur "pahalı" diye bekletiliyordu, ama pahalı
olan yalnız gloss tarafı. Ölçüm tarafı morfolojide zaten duruyordu ve kullanılmıyordu.

Üretilen: `tablolar/lemma_iskelet.json` (6236 ayet) · `ciktilar/lemma_envanteri.json`
(1651 kök, **4635 çift**). Yüzey iskeletiyle **uzunluk farkı 0**.

### Onarım 17 — `nakarat3` (aday 942)

`nakarat2` 1950 ayet → `nakarat3` **2260 ayet (+%15,9)**; süzgeci geçen 1303 → 1517.

**Kaybedilen 1 ayet (10:2) ve gerçek kayıp DEĞİL:** 10:2'de `لَسَٰحِرٌ` (LEM:ساحِر,
büyücü), 10:76'da `لَسِحْرٌ` (LEM:سِحْر, büyü). Harekesiz yüzey iskeleti ikisini de
`لسحر` yazıp aynı sayıyordu — **bir yanlış pozitifin düşmesi.**

### DÜŞEN KAYIT — aday 906'nın iddiası iki vakada da yanlış

| vaka | iddia | gerçek |
|---|---|---|
| 28:5 ↔ 28:41 | lemma katmanı görür | ortak lemma dizisi **2 kelime**, alt sınır 3 |
| 28:30 ↔ 28:46 | lemma katmanı görür | ortak birim **TEK lemma** — hiçbir n-gram alanı göremez |

**İki borç birbirine bağlıymış ve hiçbiri tek başına çözmüyor.** Hata, lemma katmanının
kalıbı *görünür* kılmasıyla alanın onu *sayması*nı aynı şey sanmaktı. İkinci vaka bir
**kök seyri** olgusu, nakarat değil. Aday 906'nın "lemma borcu yalnız gloss değil ÖLÇÜM
borcu" kaydı ise **doğru çıktı.**

### Alt sınır kararı artık hesaplanabilir (aday 943)

| | yüzey | **lemma** |
|---|---|---|
| alt sınır **3** kelime | 1950 ayet / 1354 kalıp | **2260 ayet / 1729 kalıp** |
| alt sınır **2** kelime | 3747 ayet / 3978 kalıp | **4230 ayet / 5491 kalıp (korpusun %68'i)** |

**Öneri:** alt sınır 3'te kalsın (yorumda kullanılan alan), 2 kelimelik lemma çiftleri
**ayrı bir alanda sayılsın ve yoruma sokulmasın.** Karar verilmedi.

### Onarım 18-19 — çıpa tarayıcısı v4 (aday 944)

Olgu eşleşmesi **kök → (kök, lemma)**. Tablo: 50 çok lemmalı kök + 22 tek lemmalı +
1 bağlam-gerekli; olgu alanı dışındaki token payı **%34,4**.

| | v3 | v4 |
|---|---|---|
| korpus havuzu | 680 | **481** (-%29) |
| kesinlik (sûre 27-28) | %35 | **%47** |
| kesinlik (sûre 27-29) | %40 | **%46** |
| anma — kurulum kümesi | 7/7 | **7/7** |
| anma — tutulan küme | 3/3 | **3/3** |
| çıpa kaybı | — | **0** |

### DÜŞEN KAYIT — aday 923'ün sayıları

Öngörü **"%41 → %54"**, gerçek **"%35 → %47"**. Yön ve kazanç büyüklüğü (+12 puan,
öngörü +13) tuttu; **taban ve hedefin ikisi de fazla yüksek yazılmıştı.** Sebep:
kesinlik okuma notlarındaki sayılardan hesaplanmıştı, tarayıcı çıktısından değil —
**aday 843'ün dördüncü tekrarı.** Ayrıca beşinci bir aday da düştü (27:44) ve
sayılmamıştı. Dört lemma vakasının **dördü de** düştü.

### KENDİ TABLOMDA İKİ ARIZA (aday 945)

1. **KAPSAM AÇIĞI:** `موه` *(su)* hiçbir listede değildi ve **sessizce olgu-dışı
   sayılıyordu**; `روس` korpusta hiç yok. Aday 905 ve 927'nin ailesinden: **alan bir
   kümeye bakıyor ve kümenin eksikliği çıktıda görünmüyor.** Betiğe **durduran kapsam
   denetimi** kondu.
2. **`هوي` yanlış sınıflandı:** `هَواء` lemması hem "hava" (14:43) hem "heva" (28:50)
   taşıyor. Olgu kümesinden çıkarıldı, `BAGLAM_GEREKLI` listesine alındı.
3. **Şedde/hareke sırası:** elle yazılan 16 lemma girdisinde şedde ile harekenin sırası
   korpustan farklıydı (NFC'de aynı, dizge eşleşmesinde değil). Çözüm: **tablo girdileri
   NFC üzerinden korpus biçimine çözülür, çözülemeyen varsa betik durur.**

### ★★ DENETİMİN YAKALADIĞI SESSİZ ARIZA — `ريح` HİÇ EŞLEŞMİYORMUŞ (aday 946)

`anahtar_denetim.py` olgu kümesinde **dört yanlış kök** işaretledi:

| yazılan | gerçek |
|---|---|
| **`ريح`** (rüzgâr) | korpusta **`روح`** kökü altında (`LEM:رِيح`) |
| `زتن` (zeytin) | `زيت` |
| `روس` | `رسو` — zaten kümedeydi |
| `ثلج` (kar) | **korpusta HİÇ YOK** |

**Yani tarayıcının v2 ve v3 sürümleri boyunca rüzgâr ve zeytin olgu kökleri hiçbir
ayette eşleşmedi.** Düzeltme iki yeni aday getirdi (12:94, 33:9) ve ikisi de gerçek
rüzgâr ayeti. `روح` ayrıca lemma ayrımı istiyor: `رِيح` olgu, `رُوح` (rûh) değil.

**Bu, `anahtar_denetim.py`'nin okuma dışı bir betikte bulduğu ilk gerçek ÖLÇÜM
arızası** — şimdiye kadar yakaladıkları yazım tutarsızlığıydı. **Arıza sinsi: yanlış
yazılmış kök hata vermiyor, sadece hiçbir zaman eşleşmiyor.** DERS: **küme hâlinde
yazılan Arapça kök listeleri, kullanılmadan önce korpusa karşı doğrulanmalı.**

### Açık P0'ların yeni durumu

| P0 | konu | durum |
|---|---|---|
| #3 | `esit` eşik türleri | AÇIK |
| **#5a** | **lemma kimliği** | **KAPANDI** (aday 941) |
| #5b | lemma glossu (2537 satır) | AÇIK |
| #7 | yıldızın iki otomatik ★★★ tetikleyicisi | AÇIK |
| #8 | `adsiz2` envanteri | AÇIK |
| #9/#12 | esmâ mührü token düzeyinde | AÇIK |
| #10, #11 | hapaks · fig KELLA | KAPANDI |

### DENETİM TABANI 58 → 70 (kasıtlı, 12 ihlâl)

`anahtar_denetim.py`'nin ihlâl sayısı bu turda **58'den 70'e** çıktı. Yeni on ikisi
**kasıtlı ve belgeleyicidir**: `28_olgu_lemma.py`'nin `KORPUSTA_YOK` sözlüğü ile aday
946'nın kaydı, yanlış yazılmış kökleri (`ريح` · `زتن` · `روس` · `ثلج`) **hatanın kendisini
göstermek için** içeriyor. Denetim onları doğru biçimde işaretliyor; kayıt da onların
yanlış olduğunu söylüyor.

**Kural:** bir ihlâl ancak belgeleme amaçlıysa tabanda kalabilir ve tabanda kalan her
ihlâlin bir aday kaydı olmalı. Taban tazelendi; bundan sonraki turlarda ölçüt yine
**ihlâl listesi diff = 0.**

---

## ONARIM 20 — `nakarat` ALT SINIRI KARARI VERİLDİ (aday 907/935/943 kapandı)

Üç oturumdur açık duran soru: alt sınır 2 mi 3 mü? İki seçenek de kötüydü — 3 gerçek
tekrarları kaçırıyor, 2 korpusun **%67,8'ini** dolduruyor.

**Kararı mümkün kılan şey eşik değil BİLEŞİM ölçümüydü.** Alt sınır 2 ile eklenen 3762
kalıbın içine bakıldı:

| bileşim | kalıp | pay |
|---|---|---|
| iki kelimesi de **kök** taşıyan | 1088 | **%28,9** |
| biri kök biri edat/zamir | 2264 | %60,2 |
| ikisi de edat/zamir (`الذين هم`, `حتا اذا`) | 410 | %10,9 |

**Üçüncü seçenek buradan çıktı: iki kelimenin de kök taşıması şartı.**

| sürüm | dolu ayet | karar |
|---|---|---|
| `nakarat3` — 3 kelime, lemma | 2260 (%36,2) | **yorumda kullanılır** |
| **`ikili` — 2 kelime, ikisi de köklü** | **2635 (%42,3)**, 2030 kalıp | **sayılır, yoruma sokulmaz** |
| 2 kelime, kısıtsız | 4230 (%67,8) | **reddedildi** |

**Sınama kümesi 4/6 — ve aslında 4/4.** Yakalananlar: 28:5↔28:41 (aday 906'nın vakası) ·
29:53↔29:54 · 29:5↔29:60 · 29:26↔29:42 (iki mühürlü esmâ kalıbı). Kaçan ikisi **tanım
gereği iki kelimelik kalıp değil**: 29:2↔29:4'te ortak kök taşıyan tek lemma var
(`حسب`), 28:30↔28:46'da ortak çift iki ayette de bitişik değil.

**`ikili` iddia üretmez** — okuma sırasında "alt sınırın altında kaldı" diye elle
kaydedilen tekrarları ölçülebilir kılar.

---

## OTURUM EKİ — SÛRE 30 (RÛM) OKUNDU, 60 AYET

Okunan: **2259 / 6236 ayet (%36,2)** · tam: sûre 1, 9-30 · kısmi: sûre 2 (1-20).
`kok_turkce.json` 1059 → **1069** (10 yeni kök).
Denetimler: `turkce_denetim.py` → **0** · `anahtar_denetim.py` → **31101 anahtar, 70
ihlâl, ihlâl listesi diff = 0** (taban tazelendi).
Adaylar **948-958** → `AN_rum` (11 kayıt) · bağlar → `AJ_rum` (24 kayıt).

**Okuma bu sûrede ilk kez ONARILMIŞ alanlarla koşuldu:** `hapaks2` · `fig2` ·
`nakarat3` · `yildiz2` · `z2` ve tarayıcı **v4**. Sûre 30 onarımlardan **etkilenmedi**
(yıldız değişimi 0, hapaks aynı) — **yani sûre 27-29 ile karşılaştırılabilir kalıyor.**

### ★★ ANA BULGU — TARAYICI ÇÖKTÜ VE SEBEP YAPISAL (aday 948)

| | 27 | 28 | 29 | **30** |
|---|---|---|---|---|
| anma | 4/4 | 3/3 | 3/3 | **2/9** |
| kesinlik | %67 | %33 | %30 | %40 |

**Yedi çıpa kaçtı ve yedisinin ortak özelliği tek: DÜZ HABER CÜMLESİ.** Tarayıcının
sekiz işaret ailesi bir **söz eylemi** işareti arıyor — ama **Kur'an'ın en yoğun olgu
katalogları düz haberdir.**

**TAM SAYIM:** 3+ olgu kökü taşıyan **221** ayetin **135'i (%61)** hiçbir aile
tetiklemiyor; **22'si `أيي` kökü taşıyor.** Sûre 30'da 3+ olgu köklü on ayetin sekizi
kaçıyor.

**Bu, aday 924'ün ölçümüne ÜÇÜNCÜ katman:** v2 kök listesine, v3 işaret ailelerine, v4
lemmaya bağlandı — **ama üç sürümün ortak varsayımı "çıpa bir söz eylemi işareti taşır"
ve bu yanlış.** Sûre 27-29 varsayımı doğrulamış *görünüyordu* çünkü **o sûrelerin
çıpaları tesadüfen işaretliydi.**

**Önerilen çözüm ölçülmeden yazılmayacak:** bir `H_katalog` ailesi (`أيي` + 2+ olgu
lemması) havuzu ne kadar büyütür ve kesinliği ne kadar düşürür, korpus çapında
ölçülmeli.

### ★★ OKUMANIN ÜÇÜNCÜ L4'Ü — ÜÇÜNCÜ KOL DOLDU (aday 949)

**30:48, MEKANİZMA kolundan.** Beş aşamalı süreç, her aşama adlandırılmış ve her biri
bir öncekinden `فَ` ile türetilmiş; ara durumlar adlandırılıyor (`سَحاب`, `كِسَف`,
`وَدْق`), çıkışın yeri belirtiliyor.

| kol | ayet |
|---|---|
| ölçü | 29:14 |
| sınıflama | 29:40 |
| **mekanizma** | **30:48** |

**Merdivenin çalıştığının kanıtı 30:24 → 30:48:** aynı olgu (yağmur), 30:24'te iki
aşamada verilip **L2**, 30:48'de ara aşamalar açılınca **L4**. **Kademe konuyu değil
İDDİA YAPISINI ölçüyor.** Beş sûrede 379 ayet, üç L4: **%0,8.**

### `esit2` — okumanın en yüksek değerleri (aday 950, 951)

**İki ardışık ayet, iki ardışık ayete:** 30:52 ↔ 27:80 (**0,9888**) ve 30:53 ↔ 27:81
(**0,9905** — mukattaa TAM'ları dışında okumanın en yükseği). **Okumada ilk kez bir ayet
ÇİFTİ, başka bir sûredeki ayet ÇİFTİNE sırasıyla bağlanıyor** ve karşı uç **okunmuş**
olduğu için doğrulanabilir. **`esit2` bunu iki ayrı ikili bağla veriyor — alan AYET
düzeyinde çalışıyor, BÖLÜT düzeyinde değil.**

**Aday 929'un üçlüsü tamamlandı ve eşkenar olmadığı çıktı:** 30:34↔16:55 = **1,0 TAM**,
ötekiler 0,9275. **Bağların ağırlıkları farklı; küme yapısı ancak üç uç da okununca
görünüyor.**

### ONARIMLAR TUTULAN KÜMEDE SINANDI — DÖRDÜ DE TUTTU (aday 956)

| onarım | sınama | sonuç |
|---|---|---|
| **`ريح` → `روح`** (aday 946) | 30:46 | **çıpa ANCAK düzeltmeyle görünüyor** |
| `هوي` bağlam listesine (945) | 30:29 | `أَهْوَآءَهُم` = hevesler ✓ |
| `قدر` lemma süzgeci (944) | 30:37 | `يَقْدِرُ` olgu sayılmıyor ✓ |
| `عقب` dışlaması (924) | 30:9, 30:42 | iki kez doğru negatif ✓ |

**Okumanın bir onarım turunu doğrudan sınadığı ilk vaka.** En değerlisi `ريح` → `روح`:
`anahtar_denetim.py`'nin yakaladığı sessiz arıza olmasaydı **sûrenin en açık
L2'lerinden biri (30:46) havuza hiç girmeyecekti.**

### YENİ AÇIK BORÇLAR

13. **`say` alanı ölçüyü görmüyor (aday 953).** `بضع` on yedi sayı kökü arasında yok;
    kökün geçtiği altı ayetin altısında da alan boş. Ayrıca **sıralı diziler** hiç
    görülmüyor (30:17-18 dört vakit, 30:40 dört aşama). **Onarım: (a) `بضع` eklenmeli,
    (b) sıralı dizi için ayrı ölçüt gerekip gerekmediği sınanmalı.**
14. **Merdivende iki boşluk + bayrak tanım açığı (aday 955).** Karşılaştırmalı sıralama
    **dört vaka** (29:41, 30:10, 30:27, 30:38), değişmezlik iddiası bir vaka (30:30) —
    hepsi L1'e sıkışıyor. **Ve 30:41'de "olgu" bayrağı ilk kez BELİRLEYİCİ oldu:**
    bayrak olgunun *konusu* mu *yeri* mi sayılacağını söylemiyor. **Tanım netleşmeden
    okuyucu kararları yeniden üretilebilir değil.**
15. **Yıldız formülü iki bağımsız ölçütü toplamıyor (aday 952).** TAM SAYIM: korpusta
    iki+ ölçütü |z|>2 olan **89 ayet** ve formül hiçbirine ek ağırlık vermiyor. Bir
    arıza değil, **sonucu ölçülmemiş bir tasarım kararı.**

### KALAN BORÇ (güncellenmiş)

1. `fHz` · `sesli` · `ebced` · `mod19` · `bits` kardeş projede kirli
2. `dis_sinav.py` ve `genelleme.py` kirli `harf` ile koşulmuş
3. **P0 #3** — `esit` eşik türleri; sûre 30 üç 'yakin' kaydı ekledi
4. **P0 #5b** — lemma glossu, 2537 satır; sınama kümesi **yirmi sekiz vakaya** çıktı ve
   **ikisi TEK AYETTE iki anlam taşıyor** (30:8 `سمو`, 30:55 `سوع`)
5. Aday 700/739/771/779/781 — nakarat düzeltmesi + aday 903 + 926
6. **P0 #8** `adsiz2` envanteri · **#9/#12** esmâ mührü token düzeyinde
7. **Aday 948** — tarayıcının söz-eylemi varsayımı (yeni, en büyük açık borç)
8. Aday 932/936/957 — A/R ve adlı aktör korpus dağılımları çıkarılmadı
9. **Retroaktif gloss turu ÜÇÜNCÜ kez gerekti** (9:94 `عذر`, 12:65 `بضع`) — artık
   kural: **her yeni kök eklemesi bir retroaktif tur gerektirir**

## SÛRE 31 TUR SONU — YAPILMADI (oturum kararı: sûre 32'ye geçildi)
Okuma tamamlandı (34 ayet), meal/mercek `lokman_metin_1.py` ve `lokman_metin_2.py`'de.
Yapılmayanlar: blok betikleri (`uret_blok_31.py`), `lokman_kapanis.py`, aday kaydı,
**16 yeni kökün retroaktif gloss turu** (بثث عمد وقر حمر خدد سبغ صخر صعر فخر قصد عرو غلظ قلم وثق ختر غيث),
`turkce_denetim.py` ve `anahtar_denetim.py`.
Aday adayları: tarayıcı v4 sûre 31'de anma 0/3 ve kesinlik 0/7 · hapaks tetikleyicili ★★★ iki vaka (31:18, 31:32)
· esmâ mühürsüzlerinde 6/8 yanlış pozitif · kafiye kırığı geçiş bölgesinde çift işaret (31:14-15) · A/R = 16,0.

## SÛRE 31-32 TUR SONU — TAMAMLANDI
- Blok betikleri: `blok_31_1_10/11_20/21_30/31_34.py`, `blok_32_1_10/11_20/21_30.py` (7 blok, okuma_metni.json'a yazıldı).
- Kapanış: `lokman_kapanis.py` (6 not), `secde_kapanis.py` (6 not). **İlerleme artık defterden koşuluyor: 2325 ayet (%37,3).**
- Aday kaydı: `aday_ekle_31_32.py` → AO_lokman (7), AP_secde (11), AQ_onkayit (2). Havuz **978**.
- Bağlar: okuma_baglantilari.json → AK_lokman (5), AL_secde (6).
- Retroaktif gloss: `yama_retroaktif_gloss_31_32.py` — 21 yeni kökün daha önce okunmuş 56 ayetinde tarandı; **1 yama** (12:66 ölçüm, وثق). Genel geçişte ek yama 0.
- Denetimler: `turkce_denetim.py` **0** · `anahtar_denetim.py` **70 = taban** (diff 0).
  - Tur sonunda 6 YENİ ihlâl çıktı, hepsi bu oturumun betiklerinden ve giderildi:
    blok_goster.py besmele sabiti → kelime sayısına çevrildi · alm_pilot.py ve suleyman_mercek.py'deki rasm hedefleri korpustan TÜRETİLİR hale getirildi · aday_ekle metnindeki hatalı lemma dizgesi tanımla değiştirildi.

## YENİ AÇIK BORÇLAR (bu oturum)
| no | konu | öncelik |
|---|---|---|
| 967 | Morfoloji: 2:111/135/140'ta هُودًا ('Yahudi') PN Hûd etiketli — adlı aktör alanları kontrol edilmedi | P0 |
| 968 | Morfoloji i'râb: nesne konumundaki ٱلسَّمَٰوَٰت 29 vakanın 20'sinde GEN — defter `irab` alanını etkiliyor | P0 |
| 961 | Esmâ mührü iki ayrı hata türü üretiyor (ilâhî olmayan sıfat / tekil gerçek esmâ) | P0 |
| 965 | Çıpa merdiveninde 'yeti sınırı' tanım açığı: bilgi sınırı L2 sayılır mı (31:34, 32:17) | P0 |
| 962 | Kafiye kırığı kuralı geçiş bölgesinde çift işaret koyuyor (31:14-15) | P1 |
| 972 | Köksüz özel adlar `ikili` alanında görünmez (21:81 ↔ 34:12) | P1 |
| 971 | EXP/RES etiketi istisnayı ayırmıyor (11:11 RES) | P1 |
| 969 | 'Gök' ve 'isim' aynı kökte (سمو) — kök düzeyi gök sayımları kirli | P1 |
| 970 | LEM إِنسان, أُناس biçimlerini içeriyor (6 token) | P2 |
| 976 | `dokum.py` depoda yok — protokol adımı karşılıksız | P2 |

## DONDURULMUŞ ÖN-KAYIT — esmâ katmanlarına göre dikey sınıflandırma
Dosya: `notlar/ONKAYIT_esma_katmanlari.md` — **depoya kondu** (durumu TASLAK, henüz dondurulmadı).

- **Kapsam:** üç eksen (isim katmanı a/r/e · mühür tonu · Allah-mesafesi bandı), sure profilleri, dört doğrulayıcı hipotez (H1 isim ayrışması · H2 ton × sınıf · H3 mühür × bant · H4 küme yapısı).
- **Uygulama zamanı:** TAM OKUMA bittikten sonra, tur sonu toplu testle. Dört test global Bonferroni paydasına eklenir; yerel taban α = 0,0125.
- **H3 kapı koşulu:** 35 kavramlık gradyan önce pozisyon-eşli null ile yeniden test edilecek (aday 435 borcu). Kapı açılmazsa H3 "test edilemedi" kalır.
- Tanımlar, kümeler ve tahminler kendi dosyasındadır; buraya KOPYALANMAZ.

### Dondurmadan ÖNCE karara bağlanacak üç nokta (2026-09 kontrolü)
1. **`nakarat2` mi `nakarat3` mü?** Ön-kayıt §3 ana analizi `nakarat2` ile tekilleştirilmiş veri üzerinde tanımlıyor. Defterde İKİSİ de var ama okuma **onarılmış `nakarat3`** ile koşuluyor. Dondurmadan önce alan seçimi netleşmeli; aksi hâlde ön-kayıt onarılmamış alana bağlanır.
2. **Esmâ listesinde iki girdi korpusla eşleşmiyor** (72 lemmanın 70'i eşleşiyor): `هادٍ` ve `حَىّ`. Korpusta karşılıkları başka yazımla var: `هادُ` (11) / `هاد` (7) ve `حَىَّ` (7). §4.2'nin katı kuralı bunları DÜŞÜRÜR; ama düşürme "Hayy"ı (Âyetü'l-Kürsî) setten çıkarır. Karar: tenvin/son hareke normalizasyonu mu, yoksa düşürme mi? Kural dondurmadan önce yazılmalı.
3. **Uzunluk ölçüsü kontrolü YAPILDI ve temiz çıktı:** §3'ün seçtiği `mora` ve `ar_saf` besmele kirliliğinden etkilenmiyor (30:1, 31:1, 32:1, 2:1 → ar_saf 1 kelime, mora 13). Kirlilik yalnız `ar` alanında. Bu maddede değişiklik gerekmiyor.

### Bu oturumdan ön-kayda hazır tutulan sınama kümesi
§4.2'nin "esmâ yalnız yüklem/sıfat konumunda sayılır" kuralı için elle doğrulanmış **on vaka** (sûre 31-32 okuması, aday 961):
- İlâhî OLMAYAN, yani kuralın elemesi gerekenler (8): 31:2 حَكِيم (Kitab) · 31:4 آخِر (âhiret) · 31:10 كَرِيم (bitki çifti) · 31:11 مُبِين (dalâl) · 31:31 شَكُور (insan) · 31:32 بَرّ ("kara") · 32:4 وَلِيّ · 32:18 مُؤْمِن.
- Gerçek esmâ ama ayet sonunda çift oluşturmadığı için mühürsüz kalanlar (2): 31:23 عَلِيم · 31:29 خَبِير.
Bu on vaka, §4.3'teki yeni mühür tanımının (son üç içerik lemması, lemma düzeyi) defterdeki `esma_k` tanımından farkını ölçmek için doğrudan kullanılabilir.

### İlgili ama AYRI olan eski borç
Yukarıdaki (52. satır) `bulgu_allah_ekseni_dikey.json` içindeki "esmâ katmanı eksen-nötr" bulgusunun yeniden ölçülmesi borcu. İkisi karıştırılmamalı.

---

## SÛRE 33 TUR SONU (2026-09-28)

**Okunan: 2398 / 6236 ayet (%38,5)** — sûre 1 ve 9-33 TAM, sûre 2 kısmi (1-20). İlerleme `ahzab_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` 1090 → **1112** (22 kök, `kok_ekle_33.py`). Aday **979-996** (`AR_ahzab`, 18). Bağ **AM_ahzab** 78.
Denetimler: türkçe **0** · anahtar **70 = taban**, diff 0.

### Protokol değişikliği — BLOK BAŞI KAYIT (kullanıcı onayı, aday 990)
Tur sonunu beklemeden her blokta: `uret_blok_33.py` → `blok_33_A_B.py` (okuma_metni + mercek_kayit + çıpa + esmâ + blok bilançosu + ilerleme), `aday_ekle_33_ahzab.py` (idempotent; adaylar ve bağlar), `yama_retroaktif_gloss_33.py`, iki denetim. Blok dosyası ve yükleme paketi sûre sonunda tek pakette verilir.
Yeni yardımcılar: `blok_bilanco.py` (TAM SAYIM, elle sayı yok) · `ahzab_kayit.py` (okuyucu kararları: çıpa, alan arızası) · `esma_kayit.py` + `esma_el.py` (esmâ kaydı; KAYIT, ölçüm değil).

### Onarılan (okumayı bloke eden)
* **979** `blok_goster.py` besmele ayıklaması: eski kural 26/112 → yeni 112/112 (1:1 iskeletinden, BOM ayıklanarak).
* `blok_dikey.py` komşulukta glossuz kök (حمأ) → gloss eklendi.
* İlk yükleme temizliği: `betikler/onarım` + `betikler/onar─▒m` silindi, `dikey_kisi_slymAn_dAwd.json` ASCII ad, `kisi_mercek.py` Buckwalter ile ASCII yazıyor. **GitHub'da üç silme hâlâ bekliyor** (SILINECEKLER.txt).

### YENİ AÇIK BORÇLAR (dondurulmuş — kaydet, onarma)
| no | konu | öncelik |
|---|---|---|
| 980 | okuma_metni'nde besmele kalıntısı: 23 sûrenin 6'sı (20, 21, 22, 25, 26, 27) | P2 |
| 981/992 | `say`: kök düzeyi, anlam ayırmıyor — a'adde 6/6 yanlış pozitif, sûredeki 3 gerçek ikil (30, 31, 68) 0/3 işaretli, tek doğru pozitif 33:49 | P1 |
| 982 | `mm2` bitişiklik: 33:10, 33:41 kaçırıldı (araya lafız) | P2 |
| 983 | ★★★ tetikleyicileri: sûre 33'te 14 ★★★'ın 14'ü otomatik (hapaks 5 · lafız 4 · uzunluk 3 · edilgen 2), içerik 0 | P1 |
| 985 | ön-kayıt §4.3 mühür tanımı e_oto üzerinden: sûre 33'te 32 mühürden 12'si yanlış; çift ve ton alanları da yanlış tokenlerden kirleniyor | **P0 — dondurma öncesi** |
| 986/993 | ton kapsamı: 72 lemmanın 26'sı tonlu; azîm katalogda var listede yok; 'karma' etiketi eksik tonu ayırmıyor | **P0 — dondurma öncesi** |
| 987 | kök glossu baskın anlamı taşımıyor: بلو · دور · ولي · حيي · نور (nâr 145 / nûr 43) · سدد | P1 — retroaktif tur gerekir |
| 994 | iltifât ayet içi cinsiyet/sayı geçişini (2FP→2MP, 33:33) görmüyor | P1 |
| 991 | sûre içi ayna çiftleri (33:12↔22, 15↔23, 8↔24, 3↔25, 9-10↔26) | KAPATILAMAZ (boş model yok) |

### Aday 948 birikimi (tarayıcı v4) — ölçüt değişmedi
27 → 4/4 · 28 → 3/3 · 29 → 3/3 · 30 → 2/9 · 31 → 0/3 (kesinlik 0/7) · 32 → 2/2 · **33 → 0/0 (kesinlik 0/12)**

### Esmâ ön-kaydı — DONDURMA ÖNCESİ BEŞ KARAR NOKTASI (kullanıcı kararı bekliyor)
1. §3 `nakarat2` mi, onarılmış `nakarat3` mü?
2. `هادٍ` / `حَىّ` korpusla eşleşmiyor: tenvin/son hareke normalizasyonu mu, düşürme mi? (Şu an düşüyor; iskelet eşleri 'bekleyen' diye işaretleniyor.)
3. Ton kapsamı (986/993).
4. §4.3 mühür, çift, ton ve sınıf e_oto'dan mı e_el'den mi tanımlanır (985)? Sûre 33 kaydı ikisini de tutuyor.
5. Kök glossu retroaktif turu yapılsın mı (987)?
Sûre 33 profili: `esma_kayit.json → _profil_33`, `okuma_metni['33']['_esma_profil_33']` (aday 996). H1-H4 KOŞULMADI.

### Devam
Sûre 34 (Sebe'). Blok başı kayıt için `uret_blok_34.py`'yi `uret_blok_33.py`'den S=34 ile türet; `sebe_metin_1.py`, `sebe_kayit.py`, `aday_ekle_34_sebe.py`, `kok_ekle_34.py`, `yama_retroaktif_gloss_34.py` aynı şablonla.

### Esmâ ön-kaydı — beş karar verildi (2026-09-28)
D1-D5 ön-kayda işlendi (`ONKAYIT_esma_katmanlari.md` §3, §4.2, §4.3, §6, §8.0; aday 997).
D2 `esma_kayit.py`'de uygulandı (sûre 33 kaydı değişmedi). D5 uygulandı: `yama_gloss_duzeltme_987.py`
(380 anma · 119 ayet kaydı damgalı · 63 dikey dosya; eski glosslar `tablolar/kok_gloss_duzeltme.json`).
**Dondurma için iki onay bekleniyor:** D3 ton ölçütü (§4.3.1) · D4 süzgeç kabul eşiği. §9 bunlardan sonra.
Yeni borç: 1112 kökün gloss taraması (P1, araç dondurması bitince).

### Esmâ ön-kaydı DONDURULDU (2026-09-28)
D3 ölçütü onaylandı (eşitlikte **belirsiz**); `esma_ton.json` kuruldu: cemâl 23 · denge 28 · celâl 14 · belirsiz 7 (SHA `1e01912d…`).
`esma_kayit.py` artık bu tabloyu kullanıyor; sûre 33 profili yeniden koşuldu (geçerli mühür tonu: denge 8 · cemâl 7 · celâl 3 · karma 2).
D4 kabul eşiği onaylandı: κ ≥ 0,80 · recall ve precision ≥ 0,90 · mühür uyumu ≥ 0,90; doğrulama tek koşu.
§9 dolduruldu. **Commit alanı yükleme sonrası doldurulacak.** Bundan sonra ön-kayıttaki her değişiklik §8'e.
Tam okuma bitince sırayla: (1) `e_suzgec` kodla — geliştirme kümesi okuma boyunca toplanan `e_el` · (2) geriye dönük `e_el` turu, 794 token — doğrulama kümesi · (3) süzgeç doğrulaması, tek koşu · (4) H1-H4.

## SÛRE 34 TUR SONU (2026-10-01)

**Okunan: 2452 / 6236 ayet (%39,3)** — sûre 1 ve 9-34 TAM, sûre 2 kısmi (1-20). İlerleme `sebe_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` 1112 → **1126** (14 kök, `kok_ekle_34.py`; retroaktif yama 0). Aday **998-1006** (`AS_sebe`, 9). Bağ **AN_sebe** 75.
Denetimler: türkçe **0** · anahtar **70 = taban**, diff 0. Ön-kayıt §9 commit alanı dolduruldu (`b58c430`, §8.1).

### Sûre 34 bilançosu (TAM SAYIM, `okuma_metni['34']['_bilanco_sure']`)
883 kelime · lafız 8 token/8 ayet · Rab 14 token/13 ayet (A/R 0,57 — Rab baskın) · edilgen 11 ayet · iltifât 0 · mm2 0 · hapaks 4 ayet (11, 13, 16, 52).
Yıldız 0:32 · ★11 · ★★7 · ★★★4 — ★★★'ın 4'ü de hapaks (aday 983 birikimi: içerik 0).
**Kaynak düzeltmesi (aday 1001):** kayıt `allah 2` diyor; bu iki ★ (34:18, 34:49) ve `rab` dördünden biri (34:19) aslında KAFİYE KIRIĞI. Doğru dağılım: n 7 · pas 5 · hapaks 4 · rab 3 · kafiye 3.
Kafiye kırığı 7 (9, 14, 16, 18, 19, 48, 49). En uzun 34 kelime (34:33 ve 34:43 eşit; kayıt yalnız 43'ü yazıyor).

### Yeni açık borçlar ve girdiler (dondurulmuş — kaydet, onarma)
| no | konu | öncelik |
|---|---|---|
| 1001 | `blok_bilanco.yildiz_kaynagi` eşik altı bileşeni kaynak yazıyor; kafiye-kaynaklı ★: sûre 31: 1, 32: 1, 33: 0, 34: 3 | P1 |
| 1002 | çıpa: L4 biçimli ama olgusuz ayet (34:12 rüzgâr, birim 'ay') — eşik olgu koşulunu açık yazmıyor (965 ailesi) | P0 |
| 1003 | KENDİ HATAM: nakarat3 'N ayet, tür ic' sûre içi sayı; ölçüm satırı eşi basmıyor, 34:3'te xref ile karıştırıldı → `duzeltildi` | P2 |
| 1004/1005 | say (981): sûre 34'te 8 ayet işaretli — qalîl ×2, ekser ×3 belirteç (yanlış pozitif); ekser 34:35 karşılaştırma (sınır); mi'şâr 34:45, vâhide/mesnâ 34:46 doğru; yanlış negatif: 'bir ay' (34:12), ikil 'iki bahçe' (34:15-16), furâdâ (34:46) | P1 |
| 1006 | tarayıcı v4 sûre 34: 3 aday (9, 14, 46), çıpa 0 | P0 (948) |
| 999 | esmâ sınır vakası: tamlama içinde ad olarak esmâ (34:6) — e_suzgec tanımı kapsamıyor | P1 |
| 1000 | gloss baskınlığı (987): أخر, حدد; ayrıca جبي (cevâb), أول (âl), ملك (melek) | P1 |
| 998 | gözlem: rahîm→gafûr sırası korpusta tek (34:2; ters sıra 71) | KAYIT |

### Aday 948 birikimi (tarayıcı v4) — ölçüt değişmedi
… 32 → 2/2 · 33 → 0/0 (kesinlik 0/12) · **34 → 0/0 (kesinlik 0/3; toplam 0/15)**

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
33 e_oto tokeni → ilâhî 20, değil 13. Sınıf oto A8 E8 R13 0:25 → el A8 E3 R13 0:30.
§4.3 mühür 21 → geçerli 11, yanlış 10 (3, 4, 13, 19, 20, 24, 31, 41, 43, 51 — hepsi insan/nesne sıfatı). Geçerli mühür tonu: denge 4 · cemâl 3 · karma 2 · celâl 2.
Esmâ el kararları sûre boyunca 33/33 dolduruldu (`esma_el.py`, geliştirme kümesi).

### Süreç dersleri (bu tur)
* Blok betiği `esma_kayit.py`'den ÖNCE koşulursa bilançoya bayat e_el yazılıyor (41-50'de oldu, yeniden koşuldu). `sebe_kapanis.py` artık önkoşul olarak tüm blokların esmâ kaydını yeniliyor.
* `duzeltme_34.py` blok betikleri yeniden koşulduğunda tekrar koşulmalı (kapanış koşuyor).
* nakarat3 eşi yazılmadan önce defterden kalıp → ayet listesi koşulur.

### Devam
Sûre 35 (Fâtır). Şablonlar S=35 ile `*_34` / `sebe_*` dosyalarından türetilir (set `AT_fatir`, bağ `AO_fatir`, numara 1007'den).

## SÛRE 35 TUR SONU (2026-10-04)

**Okunan: 2497 / 6236 ayet (%40,0)** — sûre 1 ve 9-35 TAM, sûre 2 kısmi (1-20). İlerleme `fatir_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` 1126 → **1132** (6 kök: صعد سوغ طرو مخر قطمر زول, `kok_ekle_35.py`; retroaktif yama 0). Aday **1007-1018** (`AT_fatir`, 12). Bağ **AO_fatir** 85.
Denetimler: türkçe **0** · anahtar **70 = taban**, diff 0 (her blok sonunda ve kapanışta).
Paket durumu: bu tur GitHub'a YÜKLENMEDİ (kullanıcı kararı) — depo hâlâ `57fdb46` (2452). Sonraki paket 57fdb46'ya göre birleşik fark olacak.

### Sûre 35 bilançosu (TAM SAYIM, `okuma_metni['35']['_bilanco_sure']`)
775 kelime · lafız 36 token/27 ayet · Rab 5 token/5 ayet (13, 18, 34, 37, 39; A/R 7,2 — lafız baskın; sûre 34'ün tersi) · edilgen 7 ayet · iltifât 0 · mm2 0 · hapaks 1 ayet (13, kıtmîr).
Yıldız 0:27 · ★9 · ★★5 · ★★★4 — ★★★ kaynakları pas 1 (35:4) · hapaks 1 (35:13) · allah 2 (35:15, 35:17; kısa ayet, aday 1012).
**Kaynak düzeltmesi (aday 1001):** kayıt `allah 5 · n 7`; üç ★ (35:8, 35:27, 35:35) aslında KAFİYE KIRIĞI. Doğru dağılım (`yildiz_kaynak_duzeltilmis`, kapanışta kayıttan hesaplandı): n 5 · pas 4 · allah 4 · kafiye 3 · hapaks 1 · rab 1. 35:35'te kayıt negatif z'yi (allah −0,53) kaynak yazıyor — vakaların en açığı.
Kafiye kırığı 4 (8, 12, 27, 35). Fâsıla sınıfı R 29 · A 7 · N 4 · د 3 · ز 1 · ب 1; A sınıfı yalnız 35:39-45 (aday 1018). En uzun 34 kelime (35:11 ve 35:18 eşit; kayıt yalnız 18'i yazıyor — 34:33/43 ile aynı alan davranışı).
say işareti 4 ayet: 35:1 mesnâ/sülâs/rubâ' doğru ×3 · 35:11 zevc yanlış pozitif · 35:41 ehad yanlış pozitif · 35:42 ihdâ sınırda.

### Yeni açık borçlar ve girdiler (dondurulmuş — kaydet, onarma)
| no | konu | öncelik |
|---|---|---|
| 1013 | tarayıcı v4 terkip duyarsızlığı: 31:29 ve 35:13 aynı dört kök + aynı kademe; yalnız 'e lem tera' olan aday | P0 (948) |
| 1009 | ★★★ edilgen kaynaklı (35:4, 11 kelime, 2/3 edilgen) — 983 birikimine karşı vaka | P1 (983) |
| 1012 | ★★★ kısa ayet lafız şişmesi: 35:15 (2/10) ve 35:17 (1/5) aynı allah z=3,47 | P1 (983) |
| 1014 | çıpa L4 sınıflama kolu ölçütü iki emsalde farklı (30:22 'sınıf adı' / 29:40 'eşleme'); okumada eşleme sabit uygulandı; 35:12 gerekçesi düzeltildi | P1 (965) |
| 1015 | gloss taraması (987/1000): ملك (melek), عذب (tatlı su), ظلم (karanlık, zulumât 23), ظلل (gölge — BASKIN lemma zıll 14 gloss'ta yok), جدد (çizgi), ek: ذهب (altın) | P1 |
| 1010 | çıpa: aynı olgu (rüzgâr-bulut-dirilme) üç ayette üç kademe (30:24 L2, 30:48 L4, 35:9 L2) | P2 (965) |
| 1011 | iki ayetlik tekrar 35:16-17 = 14:19-20; esit2 yalnız 35:17'yi görüyor | P2 |
| 1017 | şahıs sayımı alıntı içi konuşmacıyı ayırmıyor (35:37 1P 7) | P2 |
| 1018 | fâsıla sınıfı geçişi sûre sonunda (35:39-45 ا), kafiye_kirik işaretlemiyor | P2 |
| 1007 | gözlem: hamd açılışlı sûreler 6, 18, 34, 35 — ardışık tek çift 34-35 | KAYIT |
| 1008 | say doğru pozitif 35:1 (mesnâ/sülâs/rubâ'; üçlü korpusta 4:3 ve 35:1) | KAYIT |
| 1016 | كفر 35:39'da 6 token — korpusta kökün ayet-başı tepesi (sonraki 3) | KAYIT |
Ayrıca mevcut ailelere girdi: 517 iltifât (35:9, 35:27 lafız→1P; 35:32 1P→lafız) · 999 esmâ tamlama sınır vakası ikinci vaka (35:14 'mislu habîr') · #9/#12 eski esma_k MÜHÜRSÜZ (35:1, 8, 38) · 981 say (35:11, 35:41).

### Aday 948 birikimi (tarayıcı v4) — ölçüt değişmedi
… 33 → 0/0 (kesinlik 0/12) · 34 → 0/0 (kesinlik 0/3; toplam 0/15) · **35 → L4 yok (kesinlik 0/11; toplam 0/26)**
Sûre 35 adayları: 1, 3, 12, 16, 25, 27, 40, 41, 43, 44, 45. Çıpa kademeleri: L0 ×8 · L1 ×4 (11, 12, 13, 28) · L2 ×3 (9, 27, 41) · merdiven dışı 3 (16, 25, 32).

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
33 e_oto tokeni → ilâhî 22, değil 11. Sınıf oto A24 0:11 E5 AR3 R2 → el A24 0:14 AR3 E2 R2.
§4.3 mühür 19 → geçerli 13, yanlış 6 (7, 17, 19, 20, 32, 37 — ödül/lütuf sıfatı kebîr ×2, işin sıfatı azîz, insan basîr, ışık nûr, olumsuzlanan nasîr). Geçerli mühür tonu: denge 6 · cemâl 3 · celâl 2 · karma 2.
Esmâ el kararları sûre boyunca 33/33 dolduruldu (`esma_el.py`, geliştirme kümesi).

### Süreç dersleri (bu tur)
* Kayıttan ÖNCE her [x/y] ölçüm satırıyla karşılaştırıldı: beş kez kendi yazımım yakalandı (35:1-10'da beş payda, 35:33/36/40/45'te kapanan iplik sayısı, 35:26'da sayılmadan yazılmış 'hepsi'). Hiçbiri kayda düşmedi. Ders: üstünlük ve 'hepsi' iddiaları yazılırken değil yazılmadan önce sayılır.
* Kayda düşen tek hata 35:12 çıpa gerekçesi ('ölçütsüz, 27:61 emsali') → `DUZELTME` (aday 1014), kademe değişmedi.
* `head` ile boru kesilince `esitle.py` BrokenPipe verdi; borusuz yeniden koşuldu (0 dosya) — tuzak doğrulandı. `cut -c` çok baytlı Arapçayı bölüyor: çıktı dosyaya yazılıp sed ile okunmalı.
* `fatir_kapanis.py` 1001 düzeltilmiş kaynak dağılımını ayrı alanda hesaplıyor (özgün alan korunur) — sonraki kapanışlarda şablon bu.

### Devam
Sûre 36 (Yâsîn, 83 ayet, 725 kelime). Şablonlar S=36 ile `*_35` / `fatir_*` dosyalarından türetilir (set `AU_yasin`, bağ `AP_yasin`, numara 1019'dan).
Eksik kökler (12; gloss YAZILMADI, baskın lemma sayıldı): ذقن (8; ezkân 3) · قمح (8; muqmah 1, hapaks) · سلخ (37; inseleha 2/3) · عرجن (39; urcûn 1, hapaks) · جدث (51; ecdâs 3) · رقد (52; rukûd 1/2) · شغل (55; şuğul 1/2) · أرك (56; erâik 5) · طمس (66; tumiset 5) · مسخ (67; hapaks) · مضي (67; mezâ 4/5) · رمم (78; ramîm 2).

## SÛRE 36 ARA KAYIT — 36:1-20 (2026-10-04, bağlam sınırında durduruldu)

**Okunan: 2517 / 6236 (%40,4)** — sûre 36 kısmi (1-20, blok başı kayıt, 2 blok). Devam: **36:21**.
`kok_turkce.json` 1132 → **1144** (sûre 36'nın 12 kökünün tümü baştan eklendi: ذقن قمح سلخ عرجن جدث رقد شغل أرك طمس مسخ مضي رمم). Aday **1019-1020** (`AU_yasin`). Bağ **AP_yasin** 19.
Denetimler her blokta: türkçe 0 · anahtar 70, diff 0.

| no | konu | öncelik |
|---|---|---|
| 1019 | esmâ tanım dışı: Rahmân bağımsız ad (36:11 nesne, 36:15 özne) — e_el tanımı kapsamıyor, gönderge ölçütüyle 'ilahi' (999 ailesi) | P1 |
| 1020 | ★★★ kısa ayet Rab şişmesi: 36:16 (6 kelime, rab z=3,23) — 1012'nin Rab karşılığı | P1 (983) |
Ayrıca: 999 üçüncü vaka (36:5) · 983 hapaks ★★★ (36:8 قمح) · 1004/1005 say (36:7 ekser yanlış pozitif; 36:14 isneyn/sâlis doğru) · 1000 gloss (طير 'uğursuzluk' yok) · 948 tarayıcı 36:14, 36:19 aday, çıpa değil (toplam 0/28).
Süreç: `aday_ekle_36_yasin.py` boş sette yazdırmada çöktü (benim türettiğim betik) — dayanıklı yapıldı. İlk koşuda bağlar yazılmamıştı, ikinci koşuda yazıldı.
Sûre 36 sonunda kapanış `yasin_kapanis.py` ile (fatir_kapanis şablonu, S=36, N=83, 1001 düzeltilmiş alan dahil).

## SÛRE 36 TUR SONU (2026-10-04)

**Okunan: 2580 / 6236 ayet (%41,4)** — sûre 1 ve 9-36 TAM, sûre 2 kısmi (1-20). İlerleme `yasin_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1144** (değişmedi; sûre 36'nın 12 kökü ara kayıtta eklenmişti; retroaktif yama 0). Aday **1019-1022** (`AU_yasin`, 4). Bağ **AP_yasin** 122.
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0.
Bu oturumda: 36:21-83 (7 blok, 63 ayet) okundu; ek mercekler (◈K ◈B ◈D ◈A, `ONKAYIT_mercekler.md` a7e9628) 36:21'den itibaren her ayette uygulandı; sunum `blok_goster_v2.py` (v1 ile ›-satırı ve dikey sayı farkı 0, 36:11-20 üzerinde programla doğrulandı; HTML Amiri Quran).

### Sûre 36 bilançosu (TAM SAYIM, `okuma_metni['36']['_bilanco_sure']`)
725 kelime · lafız 3 token/2 ayet (36:47 ×2, 36:74 — sûrede ilk lafız 36:47; 36:1-46 lafız 0) · Rab 6 token/6 ayet (16, 25, 27, 46, 51, 58; A/R 0,5) · edilgen 12 ayet · iltifât 2 (45, 59 — ikisi de alıntı/nidâ sınırı, 1017/517 ailesi) · mm2 0 · hapaks 3 ayet (8 قمح, 39 عرجن, 67 مسخ).
Yıldız 0:66 · ★3 · ★★6 · ★★★8 — kaynak pas 9 · rab 5 · hapaks 3. ★★★: hapaks 3 (8, 39, 67) · rab 3 (16, 25, 58 — kısa ayet Rab şişmesi, aday 1020) · pas 2 (45, 83 — edilgen kaynaklı, 1009 ailesi).
Kafiye kırığı **0** → `yildiz_kaynak_duzeltilmis` = özgün (1001 farkı 0). Fâsıla sınıfı N 82 + 36:1 (mukattaa).
En uzun 36:47 (24, tek); en kısa 36:1 (tek). say işareti 8 ayet: doğru 14 (isneyn, sâlis), 29, 49, 53 (vâhide) · yanlış pozitif 7 (ekser), 62 (kesîr), 36, 56 (zevc).

### Yeni adaylar
| no | konu | öncelik |
|---|---|---|
| 1019 | esmâ tanım dışı: Rahmân bağımsız ad — 36:11 nesne · 15 özne · 23 şart öznesi · 52 özne (4 vaka); gönderge ölçütüyle 'ilahi' | P1 (999) |
| 1020 | ★★★ kısa ayet Rab şişmesi — 36:16 (6 kelime) · 25 (4) · 58 (5); 36:27 ★★ aynı aile | P1 (983/1012) |
| 1021 | gloss taraması sûre 36 girdileri: نهر baskın 'gündüz' yok (57/113) · بني baskın akrabalık yok (160/184) · حسر pişmanlık yok (9/12) · حبب tane (12/95) · سبح yüzme (5/92); baskın olmayan: جبل cibille, رجل ricl; ظلل/ظلم 1015 kaydı | P1 (987/1000/1015) |
| 1022 | ölçüm satırı esmâ alanı ↔ esmâ kaydı ayrışması: 36:70 hayy, 36:79 evvel — okuyucu kararları esma_kayit çıktısından ve eksik denetiminden toplanmalı | P2 |
Ayrıca mevcut ailelere girdi: 999 tamlama içinde ad (36:5, 36:38) · 1009 edilgen ★★★ (36:45, 36:83) · 1004/1005 say (36:7, 36:36, 36:56, 36:62) · 1017 alıntı konuşmacısı (36:45 iltifât yanlış pozitif; 36:47, 36:52 alıntı içi 'biz') · 1003 nakarat3 eşi satırda yok (sûrede 9 kalıp; bekleyen eşlerin tümü sûre içinde doğrulandı: 7↔70, 15↔47, 23↔74, 29↔53, 30↔46, 32↔53, 45↔47, 29/49/53) · 924 araç: أيي ipliği 36:59 eyyuhâ (nidâ edatı) tokenini âyetle birleştiriyor; 'innemâ' biçim alanında HASR değil (36:11, 36:82).
Kayıt (nakarat3 alt sınırının altında, okumada görüldü): 36:33/37/41 've âyetun lehum' · 36:35↔73 'e-felâ yeşkurûn' · 36:22↔83 've ileyhi turja'ûn' · 36:50↔67 istitâ'a + lâ yerci'ûn.

### Aday 948 birikimi (tarayıcı v4) — ölçüt değişmedi
… 35 → 0/11 (toplam 0/26) · **36 → L4 yok (kesinlik 0/7; toplam 0/33)**. Sûre 36 adayları: 14, 19, 35, 66, 70, 71, 77.
Çıpa kademeleri (36:21-83): L0 ×3 (28, 78, 81) · L1 ×10 (34, 36, 38, 39, 41, 71, 72, 73, 77, 80) · L2 ×5 (33, 35, 37, 40, 68). 36:35 kademesi i'râba bağlı (KAPATILAMAZ); 36:39 L4 ölçü koluna sınırda (birim var, sayı yok); 36:41 olgu hayır.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
24 e_oto tokeni → ilâhî 12. Sınıf oto 0:59 E16 R6 A2 → el 0:67 E8 R6 A2.
§4.3 mühür 17 → geçerli 7, yanlış 10 (2 hakîm · 11 kerîm · 12, 17, 24, 47, 60, 69, 77 mübîn · 70 hayy). **mübîn'in sûredeki 7 e_oto tokeninin 7'si 'degil'.** Geçerli mühür tonu: cemâl 3 · karma 2 · denge 2.
Esmâ el kararları sûre boyunca 24/24 dolduruldu (e_oto var / e_el yok denetimi 0).

### Süreç dersleri (bu oturum)
* Kayıttan ÖNCE her [x/y] ve üstünlük iddiası sayıldı; kayda düşen tek hata 36:25 mercek cümlesi ('Rab'bin iyelik eki: 36:22 …' — 36:22'de Rab yok) → `DUZELTME`, özgün alan korundu.
* Esmâ el kararlarını ölçüm satırından toplamak iki tokeni kaçırdı (36:70 hayy, 36:79 evvel); esma_kayit çıktısı yakaladı (aday 1022). Kural: kararlar esma_kayit çıktısından ve eksik denetiminden.
* `aday_ekle_36_yasin.py`'ye 1022 eklenirken metin eşleşmesi bağ listesine düştü; koşu çıktısındaki sayaç (AU_yasin 3) uyuşmazlığı gösterdi, aday listesine taşındı, iki kez yeniden koşuldu.
* `fâsıla 'fe-izâ hum'` gibi kalıp sayımları kuran_veri metninden yapıldı; harekesiz eşleşmede elif-medde (آ) bir vakayı (36:80) dışarıda bıraktı — elle eklendi. Metin sayımı okuma gözlemidir, defter alanı değil.

* Sohbetteki blok bilançolarında 'tamamlanan kök iplikleri' sayısı geçici bir düzenli ifadeyle sayıldı; iç içe iki parantezli gloss'lu kökleri (سلخ رقد شغل مضي حيي) atladı. Doğru sayılar (ölçüm satırının kök alanı ' · ' ile bölünerek): 21-30 16 · 31-40 **24** (23 yazılmıştı) · 41-50 20 · 51-60 **34** (32) · 61-70 **31** (30) · 71-83 53. Sayı yalnız sohbette yanlıştı; kayda (okuma_metni) bu alan yazılmıyor.

### Devam
Sûre 37 (Sâffât, 182 ayet) — `*_36` / `yasin_*` şablonlarından S=37 (set `AV_saffat`, bağ `AQ_saffat`, numara 1023'ten). Önce eksik kök kontrolü (sûrenin tümü), gloss çok anlamlı, baskın lemma sayılarak. Sûre 2'nin 21-286'sı hâlâ sonraya.

## SÛRE 37 HAZIRLIK (2026-10-04, oturum sonu)
`kok_turkce.json` 1144 → **1165**: sûre 37'nin 21 eksik kökünün tümü baştan eklendi (`kok_ekle_37.py`; gloss çok anlamlı, baskın lemma sayıldı): دحر (9) · وصب (9) · ثقب (10) · لزب (11) · كأس (45; ke's 6) · لذذ (46) · غول (47; hapaks) · نزف (47) · شوب (67; hapaks) · هرع (70) · سقم (89, 145) · روغ (91, 93) · زفف (94; hapaks) · تلل (103; hapaks) · جبن (103; hapaks) · أبق (140; hapaks) · سهم (141; hapaks) · دحض (141; mudhad / yudhidu-dâhida iki anlam) · لقم (142; hapaks) · حوت (142; hût 5) · سوح (177; hapaks).
Retroaktif yama: yeni kök taşıyan önceden okunmuş 9 ayet, hedefli yama 0; genel geçişte **1** — 21:87 `derin` alanında çıplak حوت (21:87 metninde kök yok; okuma notundaki kelime köprüsü). turkce_denetim bu kökler eklenince 1 verdi: 36 şablonundaki yama betiği `derin`/`derin2` alanlarını yamamıyordu, denetim ise tarıyordu — `yama_retroaktif_gloss_37.py` alan kümesi denetimle eşitlendi (okumayı bloke eden arıza istisnası). Sonra denetimler: türkçe 0 · anahtar 70, diff 0.
Şablonlar hazır (boş): `saffat_metin_1.py`, `saffat_kayit.py`, `uret_blok_37.py`, `aday_ekle_37_saffat.py` (boş sette sınandı, geçici kopyada), `yama_retroaktif_gloss_37.py`, `duzeltme_37.py`. Okuma 37:1'den.

## ARALIK OKUMASI — ayrı oturum (2026-10-05)
Sûre okumasının dışında "lafızdan lafza aralık" keşif turu; özet `notlar/ARALIK_OKUMASI.md`, sayımlar `betikler/aralik_olcum.py`.
Adaylar **1023–1036**, set `X_aralik` (sûre dizisi dışında adlandırıldı). **Sûre 37 adayları bundan sonra 1037'den başlar**; set adı `AV_saffat` değişmedi. `aday_ekle_37_saffat.py` sırayı kendisi doğruluyor.
### Yeni açık borçlar (dondurulmuş — kaydet, onarma)
* **1030 — `اللَّهُمَّ` ayrı lemma (5 token):** defter lafız alanı ve aday 435 bunları nasıl sayıyor, kontrol. Karar: vokatif lafız lafız mı?
* **1027 — aday 435 yeniden testine iki yönlü mesafe:** "lafızdan beri" / "lafza kadar" ayrı.
* **1025 — 435 duyarlılık katmanları:** yalnız lafız · +Rab+tanrısal 1P · +edilgen · +gönderge-esmâ.
* **1032 — nakarat sınırlı aralıklar** her aralık istatistiğinden önce işaretlenecek.
* **1031 — esmâ taşıyıcı** ancak e_el = ilahi ise.
### Süreç dersleri
* NFC/anahtar: elle yazılan `اللَّه` lemma iki kez 0 eşleşme verdi — kural yine doğrulandı, anahtar korpustan kopyalandı.
* Küçük örneklemde "5/5" ve "9/10" cazipti; tam sayım tersini verdi (1023). Örneklem gözlemi yalnız aday üretir.
### Aralık oturumu ek (2026-10-05) — سوم onarımı ve açığa çıkan borç
* `kok_turkce.json` **1165 → 1167** (سوم, سمد eklendi; `kok_ekle_aralik.py`). Sûre 37 oturumu 1165 bekliyordu — yeniden klonla.
* **YENİ BORÇ (P1, dondurulmuş):** okunmuş ayetlerde **145 karşılıksız kök** (sûre 9–19 ağırlıklı: 9→50, 12→37, 18→40 kök). `turkce_denetim.py` KÖR NOKTASI: tabloda olmayan kökü hiç görmüyor; denetim "0" verirken bu kökler ölçüm satırı yeniden üretilince `???` basıyor. Liste `ciktilar/karsiliksiz_kokler_okunan.json`. Onarım: kök başına baskın lemma sayılarak gloss + retroaktif yama + denetime "okunan ayette tabloda olmayan kök" testi.
* Aralık ağır okuması 16:9→18 gözlemleri NUMARASIZ (`ARALIK_OKUMASI.md`); numara sûre 37'den sonra.
* **P1 — mercek ön-kaydı tetik kusurları (`ONKAYIT_mercekler.md`, dondurulmuş):** ◈K: ölü kök ريح (→روح), ساعة (→سوع); yanlış kök سنن (yıl = سنو); سمو'da ad lemmaları. ◈B: نعم'un 107/140 tokeni nimet. Elle yazılmış ön-kayıt kökleri anahtar_denetim'e girmiyor (.md taranmıyor). Sapma §8'e yazılmalı mı — karar bekliyor (`ARALIK_OKUMASI.md`).

## SÛRE 37 OTURUMU — birleştirme ve kararlar (2026-10-06/07)
* Aralık oturumu (67f9cc5, 4e57971) ile birleştirildi: 37:1-90 bu tabanda kayıtlı; bu oturumun adayı **1037** (AV_saffat; mâte 'mit-' PASS tutarsızlığı, 37:47 ters yönlü ek vaka). X_aralik değişmedi.
* **Ortam kaybı (2026-10-07):** çalışma alanı silindi; depo yüklenmemişti. 37:1-90 meal/mercek metni blok HTML'lerinden (`okuma_37_*_*.html`) birebir geri alındı; kayıt kararları, adaylar, bağlar, esmâ kararları ve aşağıdaki onarımlar oturum dökümünden yeniden yazılıp yeniden koşuldu. Ders: uzun oturumlarda ARA ZİP.
* **Karar a:** mercek tetik düzeltmesi yalnız ileriye — `ONKAYIT_mercekler.md` §8 S1 (ريح→روح/rîh, ساعة→سوع/sâa, سنن→سنو/sene-sinîn, سمو→semâ', نعم→ne'am). 37:31'den uygulanır. Duyarlılık genişletmeleri (ışık/karanlık, besin, beden eylemi) UYGULANMADI.
* **Karar d:** `ONKAYIT_435_ek.md` — 435 yeniden testine ikincil katmanlar: iki yönlü mesafe (1027), taşıyıcı katmanları K0-K3 (1025), nakarat sınırlı aralık işareti (1032). Kapı ölçüsü değişmedi.
* **Karar 1 — anahtar denetimi 122 → 70:** aralık oturumunun dört ters okuma betiğindeki (`ters_onluk_sayfa.py`, `sondan_01_30/11_20/31_60_uret.py`) 152 elle yazılmış harekeli Arapça dizge, korpus metnini (kuran_veri `ar_saf`) konumla okuyan `W(sûre, ayet, kelime, n)` çağrısına çevrildi; harekesiz kök anması (أله) istisna. Vurgu sayıları dört sayfada aynı (52 · 16 · 40 · 26). Notlardaki alıntılar artık korpustaki tam kelime (önek ve hareke dahil). Denetim: BOZUK **70**, tohum0 ile ihlal farkı **0**.
* **Karar 2 — karşılıksız kökler onarıldı:** `betikler/kok_ekle_okunan.py` (146 kök: aralık oturumunun 145'i + birleşik kayıt anahtarı 2:19-20 içindeki صبع), gloss çok anlamlı, baskın lemma önce; `kok_turkce.json` 1167 → **1313**. Geriye dönük yama `yama_retroaktif_gloss_okunan.py`. `turkce_denetim.py`'ye **ikinci test**: okunan ayette morfolojide geçip tabloda olmayan kök (birleşik anahtarlar dahil) — 0 değilse çıkış kodu 1.
* **Karar 3 — aday 1030:** vokatif Allâhümme lafız SAYILMAZ; defter lafız alanı ve 435 K0 değişmez. Ayrı bayrak: `tablolar/lafiz_vokatif.json` (`betikler/lafiz_vokatif_bayrak.py`; 5 token: 3:26, 5:114, 8:32, 10:10, 39:46).

## SÛRE 37 TUR SONU (2026-10-10)

**Okunan: 2762 / 6236 ayet (%44,3)** — sûre 1 ve 9-37 TAM, sûre 2 kısmi (1-20). İlerleme `saffat_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1313** (sûre 37 hazırlığında 1144 → 1165; aralık oturumu 1167; karşılıksız kök onarımı 1313). Aday **1037-1038** (`AV_saffat`, 2). Bağ **AQ_saffat** 110.
Denetimler her blokta ve kapanışta: türkçe **0** (tabloda olmayan kök 0) · anahtar **70 = taban**, diff 0.
Sûrenin 182 ayeti 18 blokta okundu (son blok 171-182, 12 ayet); ek mercekler sûrenin tamamında, §8 S1 tetik düzeltmesi 37:31'den. Paket `notlar/sure37_saffat_okuma.md` (`saffat_paket_md.py`).

### Sûre 37 bilançosu (TAM SAYIM, `okuma_metni['37']['_bilanco_sure']`)
860 kelime · lafız 15 token/15 ayet (23, 35, 40, 56, 74, 86, 96, 102, 126, 128, 152, 159, 160, 169, 182) · Rab 14 token/11 ayet (5, 31, 57, 84, 87, 99, 100, 126, 149, 180, 182; A/R 1,07) · edilgen 10 ayet · iltifât alanı 28 ayet (çoğu alıntı sınırı, 1017; gerçek muhatap geçişleri 6, 137, 140, 154, 161) · mm2 2 (10, 88) · hapaks 9 ayet (11, 47, 67, 94, 103, 140, 141, 142, 177).
Yıldız 0:141 · ★3 · ★★6 · ★★★32 — kaynak rab 11 · allah 11 · pas 9 · hapaks 9 · n 1 (37:7 kafiye kırığı → düzeltilmiş kaynak 'kafiye', 1001). ★★★: rab 11 (5, 31, 57, 84, 87, 99, 100, 126, 149, 180, 182) · allah 10 (40, 56, 74, 86, 96, 128, 152, 159, 160, 169) · hapaks 9 · pas 2 (45, 70).
Fâsıla sınıfı N 171 · ب 5 · A 3 · د 2 · ق 1; kafiye kırığı 37:7. En uzun 37:102 (26, tek); en kısa 2 kelime: 1, 2, 3, 17, 155, 176. say işareti 5: doğru 4 (vâhid), 19 (vâhide), 147 (elf; mi'e alana girmiyor) · yanlış pozitif 22 (zevc), 71 (ekser).

### Yeni adaylar
| no | konu | öncelik |
|---|---|---|
| 1037 | morfoloji edilgen etiketi biçimle iki yönde uyuşmuyor: mâte 'mit-' biçimi 8 token, 6'sı PASS (23:35, 23:82, 37:16, 37:53, 50:3, 56:47); ters yön 37:47 'yunzefûn' PASS'sız | P1 (924; 1009 komşu) |
| 1038 | gayr-i munsarif özel ad i'râb etiketi: mecrur Hârûn ACC (37:114, 37:120; 26:48 — aynı dizge 7:122'de GEN), 40:24 Hâmân ACC; mansub İlyâs (37:123) ve Yûnus (37:139) GEN — aynı kalıpta munsarif Lût (37:133) doğru; aktör rol alanı ACC→meful türettiği için etkileniyor | P2 (924; 1037 komşu) |
Ayrıca mevcut ailelere girdi: 983 hapaks ★★★ (9 ayet) · 1012 kısa ayet lafız ★★★ (allah kaynaklı 10 ayet) · 1020 kısa ayet Rab ★★★ (rab kaynaklı 11 ayet) · 1017 alıntı sınırı iltifât (93, 127, 167, 168, 170 …) · 1022 ölçüm satırı esmâ ↔ esma_kayit (17, 101, 125) · 517 biçim alanı (100 edatsız nidâ VOC yok; 167 in-i muhaffefe COND) · 999/1019 çoğul tamlama içinde esmâ 'ilahi' (75 mucîbûn, 125 hâlikîn — sınır vakası) · 987/1015 gloss: بني (bunayye, benât/benûn), ملك (melâike), **مأي 'ne zaman' — 10/10 token lemma mi'e (yüz), gloss tek lemmayı hiç karşılamıyor** · 1003/esit2 satırında eş ayet iki kez (araç tekrarı: 108, 111, 121, 128, 129, 131, 132, 160).

### Karar bekleyen (kullanıcı)
* **S2 — ◈K tetik فلك:** kök 25 token, lemma fulk (gemi) 23, felek 2. 37:140'ta tetik gemi için çalıştı ('kozmik öğe değil' notuyla yazıldı). S1 türünden kesinlik düzeltmesi (yalnız felek lemması) — ön-kayıt §8'e S2 olarak yazılsın mı, ileriye mi?
* **مأي gloss onarımı:** 'ne zaman' → 'yüz (sayı)'. Araç dondurma kuralı nedeniyle onarılmadı; tur sonu gloss taramasına mı, şimdi mi?

### Aday 948 birikimi (tarayıcı v4) — ölçüt değişmedi
… 36 → 0/7 (toplam 0/33) · **37 → L4 yok (kesinlik 0/1; toplam 0/34)**. Sûre 37 adayı: 102 (نوم; işaretler şart + bakış konuşmanın yapısından).
Çıpa kademeleri: L0 ×3 (5, 88, 102) · L1 ×4 (6, 10, 11, 16). Sûrede doğa olgusu az; 37:6-10 gök/yıldız/şihâb bölütü en yoğun.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
26 e_oto tokeni → ilâhî 2 (37:75 mucîbûn, 37:125 hâlikîn — ikisi de çoğul biçim, sınır vakası). Sınıf oto 0:133 E25 R9 A13 AR2 → el 0:156 E2 R9 A13 AR2.
§4.3 mühür 26 → geçerli 2, yanlış 24 (mubîn, âhir, selâm, mu'min, evvel, halîm … — kapanış formüllerindeki âhirîn/selâm/mu'minîn tekrarları dahil). Geçerli mühür tonu: cemâl 1 · denge 1.
Esmâ el kararları sûre boyunca dolduruldu (e_oto var / e_el yok denetimi her blokta 0).

### Okumada görülenler (KAPATILAMAZ, defter bağı olanlar AQ_saffat'ta)
* Kıssa kapanış dörtlüsü (tereknâ · selâm · kezâlike · innehû) dört kez aynı sırada: Nûh 78-81, İbrâhîm 108-111, Mûsâ-Hârûn 119-122 (ikil), İlyâs 129-132; Lût (133-138) ve Yûnus (139-148) kıssalarında yok. Selam formülü beşinci kez 181'de adsız çoğulla ('ale'l-murselîn').
* Açılış kalıbı 've inne X le-mine'l-murselîn' üç kıssada (123, 133, 139).
* 'illâ ibâda'llâhi'l-muhlasîn' dört kez anlatıcıda istisna (40, 74, 128, 160), bir kez inkârcıların ağzında şartın cevabı (169).
* صفف yalnız 37:1 ve 37:165'te; 'biz'in göndergesi metinde işaretli değil.
* Sûre 37:182 'el-hamdu li'llâhi rabbi'l-âlemîn' (esit2 1:2 TAM) ile kapanıyor.

### Süreç dersleri (bu oturum)
* **Mercek tetik taraması:** 37:93 ◈B (يمن), 37:99 ◈K, 37:100 ◈B (وهب) tetiksiz yazılmıştı; 37:101-110'da korpus taramasıyla bulundu ve '—' yapıldı. Ters yönde 37:175/179 ◈B (بصر) tetiklenmişken '—' yazılmıştı — tarama yakaladı. Her bloktan sonra M satırlarını morph kökleriyle karşılaştıran tarama koşuldu (oturum betiği; repoya alınmadı — lemma dizgeleri elle yazılmış olurdu). Öneri: tarama `ONKAYIT_mercekler.md` listesinden ve morph.txt'ten okuyan bir denetim olarak repoya girsin.
* **Okunmuş ayet denetimi:** okuma_metni anahtarları iki biçimde ('S:A' / 'A-B'); yalnız birini okuyan geçici denetim 2:252'yi 'henüz okunmadı' saydı — düzeltildi; başka etkilenen ifade yok.
* **Esmâ sırası:** 37:156 kararından sonra esma_kayit koşulmadan blok yazıldı, bilanço bir an 'E' gösterdi; yeniden koşuldu. Kural OKU_BENI'de zaten var (adım 3 → 5).
* **Kelime sayımı kaynağı:** kuran_veri 37:1 metnine besmeleyi katıyor; boşlukla sayım 'iki kelimelik ayet' listesinde 37:1'i kaçırdı (155, 176 mercekleri) → `DUZELTME` (özgün alan korundu); doğru liste defterden (`en_kisa_esit`).
* Meal parantezi metinde adlanmayan konuşanı adlandırmamalı (37:164 '(Melekler derler:)' kaldırıldı).
* Ortam kaybı sonrası ara zip: 1-90 (4e57971 tabanı), 1-120 ve 1-182 (0793015 tabanı) teslim edildi.

### Devam
Sûre 38 (Sâd, 88 ayet) — `*_37` / `saffat_*` şablonlarından S=38 (yeni aday seti ve bağ seti; numara 1039'dan). Önce eksik kök kontrolü (sûrenin tümü). Sûre 2'nin 21-286'sı hâlâ sonraya. Açık kararlar: S2 (فلك), مأي gloss.

### Kapanış sonrası onarım (2026-10-10) — esitle aday_bulgular'ı eziyordu
* `esitle.py` bir dosyayı k (temiz klon) ile farklıysa calisma → repo kopyalıyordu. k 0793015'ten yeniden klonlanınca (2026-10-09) `calisma/aday_bulgular.json` (2026-10-07, AV_saffat'sız) k'dan farklı sayıldı ve **her blokta** `aday_ekle_37_saffat.py`'nin repo'ya yazdığı `AV_saffat` setini (1037-1038) ezdi. Blok çıktısındaki sayaç doğruydu (yazma anı), kalıcı dosya değildi.
* Onarım: `aday_ekle_37_saffat.py` yeniden koşuldu (1037, 1038 + iki ek vaka geri); calisma kopyası repo'yla eşitlendi; `esitle.py` artık hedef kaynaktan yeniyse kopyalamıyor ('ATLANDI' yazar) — okumayı bloke eden arıza istisnası.
* Etkilenen teslimler: ara zip'ler `sure37_ara_1_120` ve `sure37_ara_1_182` AV_saffat'sız `aday_bulgular.json` içeriyordu — **kullanmayın**; tur sonu zip'i yeniden üretildi. Diğer repo'ya doğrudan yazılan dosyalar (`notlar/` altındakiler) esitle kapsamında değil, etkilenmedi; calisma–k farkı taranan başka bayat dosya yok.
* Ders: denetimlere "aday havuzu sonu = beklenen" kontrolü (repo dosyasından okunarak) eklenmeli.

## SÛRE 38 TUR SONU (2026-10-10)

**Okunan: 2850 / 6236 ayet (%45,7)** — sûre 1 ve 9-38 TAM, sûre 2 kısmi (1-20). İlerleme `sad_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1324** (sûre 38 hazırlığında 1313 → 1324, `kok_ekle_38.py`: 11 kök). Aday havuzu **1038** (sûre 38'de yeni aday yok; `AW_sad` boş). Bağ **AR_sad** 103.
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · mercek tetik taraması temiz · `AV_saffat` [1037, 1038] repo dosyasından her blokta doğrulandı (esitle onarımı sonrası).
Sûrenin 88 ayeti 9 blokta okundu (son blok 81-88, 8 ayet); ek mercekler sûrenin tamamında. Paket `notlar/sure38_sad_okuma.md` (`sad_paket_md.py`).

### Sûre 38 bilançosu (TAM SAYIM, `okuma_metni['38']['_bilanco_sure']`)
733 kelime · lafız 3 token/2 ayet (26, 65) · Rab 10 token/10 ayet (9, 16, 24, 32, 35, 41, 61, 66, 71, 79; A/R 0,3 — sonuncusu İblîs'in ağzında) · edilgen 6 ayet (6, 8, 31, 53, 70, 79) · iltifât alanı 7 ayet (7, 43, 48, 50, 53, 54, 66) · mm2 1 (32) · hapaks 4 ayet (3, 16, 31, 36).
Yıldız 0:64 · ★12 · ★★5 · ★★★7. ★★★: hapaks 3 (3, 16, 36) · pas 3 (31, 53, 70) · rab 1 (79). ★★: pas 8 · rab 9, 66, 71 · n 24. Düzeltilmiş kaynak (1001): kafiye 8 (12, 15, 18, 22, 33, 54, 55, 84).
Fâsıla sınıfı ب 35 · N 21 · R 15 · ق 6 · د 6 · ص 2 · ط 1 · ج 1 · ل 1; kafiye kırığı 9 (12, 15, 18, 22, 31, 33, 54, 55, 84). En uzun 38:24 (32, tek); en kısa 38:68 (3, tek). Say işareti 9 ayet; doğru 4: 5 (vâhid), 15 (vâhide), 23 (tis' ×2, vâhide), 65 (vâhid) · yanlış pozitif 5: 24 (kesîr, qalîl), 51 (kesîra) — 37:71 ekser emsali; 35 (ehad = 'kimse'); 58 (zevc = 'çeşitler'); 62 ('nauddu' fiil).

### Çıpa (aday 948 birikimi — ölçüt değişmedi)
**38 → L4 yok (kesinlik 0/2; tarayıcı v4 adayları 38:23, 38:24 F_ölçü — koyun sayıları; toplam 0/36)**.
Kademeler: L0 ×2 (10, 66) · L1 ×12 (18, 19, 23, 24, 27, 31, 33, 36, 42, 71, 72, 76 — 18 ve 19 L0'dan L1'e DÜZELTME).
**DUZELTME 18/19:** blok 11-20'de 🜁 L0 yazılmıştı; `onarim/14_cipa_tanimi.py` kademe tanımı (L1 = adlandırma + alan/yeti/nitelik; 27:16-18 emsali) ile L1. Mercek metni korunur, `okuma_metni['38']['38:18'/'38:19']['duzeltildi']`.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
10 e_oto tokeni → ilâhî 7 (9 azîz+vehhâb, 35 vehhâb, 65 qahhâr, 66 azîz+ğaffâr, 71 hâliq) · değil 3 (7 âhir, 35 ehad, 70 mubîn). Sınıf oto 0:74 E2 R10 A2 → el 0:76 R10 A2.
§4.3 mühür 7 → geçerli 5, yanlış 2 (7, 70). Geçerli mühür tonu: karma 3 · celâl 1 · denge 1.
Ölçüm satırı ↔ bilanço ayrışması: 38:35, 38:65, 38:71'de ölçüm satırı 'MÜHÜRSÜZ' (71'de 'ORTA konum'), bilanço §4.3 geçerli — 1022 ailesine ek vaka.

### Mevcut ailelere girenler (yeni aday açılmadı)
* 924 araç açığı: özel ad kök alanına giriyor (38:12 'Âd' → عود 'geri dönme'); 38:13 'Eyke' ne ROOT ne PN; 38:48 'Zü'l-Kifl' ذو + كفل ayrışıyor, aktör dışı, كفل ipliğine (38:23 'ekfilnîhâ') katılıyor; 'melâike' (38:71, 73) ملك (mülk) ipliğine sayılıyor.
* 987/1015 gloss: خلق ihtilâq (7) · فوق fevâq (15) · فجر fuccâr (28) · دبر tedebbür (29) · سوق sâq (33) · رجل ricl/ayak (42) · ترب etrâb (52) · سخر sihriyy (63) · ملك melek (71).
* ◈B tetik listesi (S1 gereği yalnız ileri): نعج (23-24), جسد (34), رجل (42) listede yok → '—'; ters yönde زوج 'ezvâc = çeşitler' (58) ve يدي 'eydî = güç' (45) tetikliyor.
* 1017 alıntı sınırı: 38:8 ayet içi 1P (onlar) → 1S ('zikrî', 'azâbi') alan 0; 38:14 'ıqâbi' 1S yâsı düşmüş.
* Kafiye: 38:66 ر → 38:67 م (R → N) geçişi kırık alanında işaretlenmiyor.

### Okumada görülenler (KAPATILAMAZ; defter bağı olanlar AR_sad'da)
* Sûre zikirle açılıp zikirle kapanıyor: 38:1 'zi'z-zikr' → 38:87 'zikrun li'l-âlemîn' (ذكر 13/13); حين 38:3 'lâte hîne menâs' → 38:88 'ba'de hîn'.
* 38:5 inkârcıların itirazı 'ilâhen vâhidâ' → 38:65 'qul … illa'llâhu'l-vâhid' (وحد 4/4).
* 'innehû evvâb' Dâvûd (17), Süleymân (30), Eyyûb (44); أوب 8 token: evvâb ×4 → meâb ×4, son 'meâb' azgınların (55). 38:25 = 38:40 son altı kelime (Dâvûd / Süleymân kapanışı).
* Dâvûd 'fetennâhu … enâb' (24) → Süleymân 'fetennâ … thumme enâb' (34): فتن + نوب aynı sırayla.
* 21:83-85 ve 38:41-48 anılanlar dizisi (Eyyûb → … → Zü'l-Kifl); 12:104 tek ayeti burada 38:86-87 iki ayete bölünmüş; 14:29'un iki yarısı 38:56 ve 38:60'ta.
* 38:72-80: esit2 sûre 15 ile TAM 5 (72, 73, 77, 79, 80), BENZER 1 (78); 74-76 sûre 15'ten ayrılıp 2:34 / 7:12'ye yaslanıyor; 38:81, 83 → 15:38, 15:40 TAM.

### Süreç dersleri (bu oturum)
* **Kayıt sayımı denetimi:** mercek metnindeki her `KÖK [x/y]` ölçüm satırının kök alanıyla karşılaştırıldı (oturum betiği, 393 sayım): bir hata (38:42 رجل [1/1] → [1/2]) sunumdan önce yakalandı. Öneri: tetik2 ile birlikte repo denetimi olsun.
* **Tetik taraması iki yönlü yakaladı:** 38:27 ◈B (خلق) boş, 38:72 ◈B tetiksiz dolu.
* **sad_kayit ARIZA ekleme:** üç kez sözlük kapanış parantezi düştü (SyntaxError, koşmadan önce yakalandı) — blok sonu ekleme kalıbı `" ],\n}"` ile yapılmalı.
* Meal parantezi metinde adlanmayan konuşanı adlandırmamalı: 38:75 '(Allah) dedi ki' → 'Dedi ki' (37:164 emsali).
* Ara zip'ler: 38:1-30, 38:1-60 (0793015 tabanı; ikisi de AV_saffat'lı, doğrulandı).

### Devam
Sûre 39 (Zümer, 75 ayet) — `sad_*` şablonlarından S=39 (aday numarası 1039'dan, yeni set adları). Önce eksik kök kontrolü (sûrenin tümü). Sûre 2'nin 21-286'sı hâlâ sonraya. Açık kararlar: S2 (فلك), مأي gloss.

## SÛRE 39 TUR SONU (2026-10-11)

**Okunan: 2925 / 6236 ayet (%46,9)** — sûre 1 ve 9-39 TAM, sûre 2 kısmi (1-20). İlerleme `zumer_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1331** (`kok_ekle_39.py`). Aday havuzu **1039** (yeni: 1039, `AX_zumer`). Bağ **AS_zumer** 171. Esmâ okuyucu kararı (KARAR) **221**.
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik2 temiz · [x/y] sayım karşılaştırması **422 sayım, 0 uyuşmaz** · `AV_saffat` [1037, 1038] ve `AX_zumer` [1039] repo dosyasından doğrulandı.
Sûrenin 75 ayeti 8 blokta okundu (son blok 71-75, 5 ayet); ek mercekler sûrenin tamamında. Paket `notlar/sure39_zumer_okuma.md` (`zumer_paket_md.py`). Ara zip'ler: 39:1-30, 39:1-60.

### Sûre 39 bilançosu (TAM SAYIM, `okuma_metni['39']['_bilanco_sure']`)
1172 kelime · lafız 59 token / 43 ayet · Rab 18 token / 17 ayet (A/R 3,28) · edilgen 18 ayet · iltifât alanı 4 ayet (32, 40, 64, 67) · hapaks 3 ayet (23, 29, 45) · mm2 yok.
Yıldız 0:43 · ★10 · ★★18 · ★★★4 (hapaks 3, pas 1 — 39:69). Kaynak: allah 10 · n 8 · pas 8 · rab 3 · hapaks 3; düzeltilmiş (1001): 39:41 kafiye.
Fâsıla sınıfı N 58 · R 6 · ب 4 · د 4 · ل 2 · A 1; kafiye kırığı 6 (6, 14, 23, 36, 41, 62). En uzun 39:6 ve 39:38 (36); en kısa 39:30. Say işareti 7 ayet: 4 vâhid, 6 (vâhide, zevc ×2, semâniye, selâs), 45 vahdehû, 23 'mesânî' (kök ثني — sayı değil, öz-tanım sıfatı), 8 qalîl, 29 ve 49 ekser (yanlış pozitif, 37:71 emsali).

### Çıpa (aday 948 birikimi — ölçüt değişmedi)
**39:21 → L4, cipa=True** (gökten su → yerde pınarlar → renkleri farklı ekin → kuruma, sararma → çer-çöp; mekanizma, 30:48 emsali). Sûre 32'den beri ilk L4; tarayıcı v4 isabeti. Kesinlik **1/8** (adaylar 4, 6, 8, 10, 21, 26, 38, 47), anma 1/1.
39:42 **L4-biçim** (canların ölüm ve uyku anında alınışı; olgu sınırda, cipa=False — 1002 ailesi). L1 ×4 (5, 6, 10, 69) · L0 ×8 (9, 38, 44, 46, 63, 67, 68, 74) · olgusuz tarayıcı adayı ×4 (4, 8, 26, 47). DUZELTME yok.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
30 e_oto tokeni → ilâhî 13 · değil 17. §4.3 mühür 20 → geçerli 7, yanlış 13. Geçerli mühür tonu: celâl 3 · cemâl 2 · karma 1 · denge 1.
Ölçüm satırı 'MÜHÜRSÜZ' ↔ bilanço geçerli (1022): 39:62 (hâliq + vekîl) ve önceki bloklardaki vakalar.

### ★ ADAY 1039 — öz-tanım ve ölçülen benzerlik: ÖLÇÜM KOLU H0 REDDEDİLMEDİ
Kullanıcı gözlemi (blok 21-30): 39:23 kitabı 'muteşâbih' ve 'mesânî' diye niteliyor; 39:27 'min kulli mesel'. Önceden yazılan test sûre sonunda koşuldu (`aday1039_test.py`, `bulgular/aday1039_test.json`, tohum 0):
* Sûre 39 ayet oranları: esit2 herhangi 6/75 · esit2 TAM 2/75 · nakarat3 GEÇER 22/75 · birleşik 27/75.
* Uzunluk eşli band (öz-tanım ayeti içermeyen; ±15 ayet, ±%25 kelime): sûre 8, 22, 24, 25, 28, 29, 33, 40. Sûre 39'un 9 içindeki sırası: esit2 2. · TAM 3. · nakarat3 5. · birleşik 5. — **ortada**.
* Tek kontrol sûre 8 (75 ayet): nakarat3 22/75 vs 36/75, Fisher p=0,029 — **yön ters** (39 daha az) ve Bonferroni eşiği 0,0063'ün üstünde; öteki ölçüler p≥0,099.
* Öz-tanım ayetleri (3:7, 15:87, 17:89, 18:54, 30:58, 39:23, 39:27) ±10 ayet penceresi: pencere − sûre farkı dört ölçüde de negatif (−0,010 … −0,024); sûre içi permütasyon p=0,62-0,74.
* **Karar:** esit2 / nakarat3 ile ölçülen benzerlik, öz-tanım taşıyan sûrede ya da öz-tanım ayetlerinin çevresinde yüksek değil. Öz-tanım bu iki ölçüyle desteklenmiyor. Öncelik P2 → P3.
* **Açık kalan kol:** karşıt çift (okuma). Sûre 39'da ◇ satırlarında 16 ayet (39:21-75) + 39:1-20 için aday listesinde 7 çift. Kontrol sûresi aynı protokolle okunmadan karşılaştırma yapılamaz — iddia yok. Önerilen: sûre 40'tan itibaren ◇'de 'karşıt çift' notunu aynı biçimde sürdürmek; böylece okuma kolu için kontrol verisi birikir.
* Ölçülen tek güçlü yapı: sûrenin adı 'zumeran' korpusta yalnız 39:71 ve 39:73'te — 9 kelimelik ortak gövdeli karşıt çift (nakarat3 GEÇER). Bu tek vaka; genelleme yok.

### Mevcut ailelere girenler (yeni aday açılmadı, 1039 dışında)
* 1021/987 gloss: نهر, ظلم, أمم, أخر, ظلل, جنب, نور (nâr/nûr tek iplik), كفر (tekfîr), سخر (alay), حسر (hasret), وفي (tam verme / vefat ettirme ayrımı), ملك (melek), حول (çevre), علم (âlem).
* 517 biçim: 'innemâ' ve takdim hasrı işaretsiz (39:64 'e-fe-ğayra'llâh', 39:66 'beli'llâhe fa'bud'); 39:73 izâ cevabının düşmesi alanda yok.
* 1017 iltifât / alıntı sınırı: 39:53-58 iç içe alıntı (1S içinde 1S), 39:59 3FS → 2MS hitap alan 0; 39:64 alıntı içi, 39:67 ayet içi zamir değişimi aynı alanda; 39:71 've lâkin haqqat' cevabın parçası mı anlatıcı mı — KAPATILAMAZ.
* 924 araç: 39:46 'Allâhumme' lafız ekseninde yok; esit2 39:13'te 6:15'i iki kez yazıyor; sayı işareti yanlış pozitifleri.
* Zaman alanı: 39:68-70 kıyamet sahnesi PERF ile anlatılıyor; alan geçmiş sayıyor.

### Okumada görülenler (KAPATILAMAZ; defter bağı olanlar AS_zumer'de)
* 39:23 öz-tanım (muteşâbih, mesânî; deri ürperir → yumuşar) · 39:27 'min kulli mesel' · 39:29 iki adam örneği + 'hel yesteviyân'.
* 39:53 'yâ ibâdiye' — 'qul' içinde 1S 'kullarım'; alıntı 39:58'e kadar sürüyor; 39:56-58 bir canın üç sözü (pişmanlık / bahane / dönüş dileği), 39:59 'belâ' cevabı; 39:71 inkâr edenlerin 'qâlû belâ'sı.
* 39:11-12 'umirtu' (bana emredildi) ↔ 39:64 'te'murûnnî' (bana emrediyorsunuz); 39:64 soru ↔ 39:66 emir, aynı iki öğe aynı sırada.
* 39:68 iki üfleniş: 'saiqa' (bayılma) ↔ 'qiyâm' (kalkış); 39:69 edilgen 4/5, faillerin hepsi adsız.
* 39:71 ↔ 39:73 sûrenin adı olan çift; 39:72 'udhulû … hâlidîne fîhâ' ↔ 39:73 'fedhulûhâ hâlidîn'.
* 39:75 son ayet 14 kökün hepsini kapatıyor (قول 29/29, أله 61/61, ربب 18/18 dahil); 'el-hamdu lillâhi rabbi'l-âlemîn' 6 ayet (1:2, 37:182 de sûre sonu).

### Süreç dersleri (bu oturum)
* Önceden yazılmış testin olumsuz sonucu kayda aynen geçti; aday kapatılmadı, ölçüm kolu ile okuma kolu ayrıldı.
* say.py normalizasyonu: ٰ → ا (ىٰ → ى), 'وجيء' gibi hemzeli kalıplar eşleşmiyor — o sayım iddia edilmedi.
* Kapanış öncesi karşıt çift notu yalnız 39:21'den itibaren sistematik — okuma kolunun kontrol verisi için sûre 40'tan aynı biçim.

### Devam
Sûre 40 (Ğâfir, 85 ayet) — `zumer_*` şablonlarından S=40 (aday numarası 1040'tan, yeni set adları). Önce eksik kök kontrolü (sûrenin tümü). Sûre 2'nin 21-286'sı hâlâ sonraya. Açık kararlar: S2 (فلك), مأي gloss.

## SÛRE 40 TUR SONU (2026-10-11)

**Okunan: 3010 / 6236 ayet (%48,3)** — sûre 1 ve 9-40 TAM, sûre 2 kısmi (1-20). İlerleme `gafir_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1334** (`kok_ekle_40.py`: فوض, سلسل, سجر). Aday havuzu **1040** (yeni: 1040, `AX_gafir`). Bağ **AS_gafir** 202. Esmâ okuyucu kararı (KARAR) **250**.
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik2 kayıtta temiz (iki blokta ilk koşuda uyuşmaz, kayıttan önce düzeltildi) · [x/y] sayım karşılaştırması **549 sayım, 0 uyuşmaz** · `AV_saffat` [1037, 1038], `AX_zumer` [1039], `AX_gafir` [1040] repo dosyasından doğrulandı.
Sûrenin 85 ayeti 9 blokta okundu (son blok 81-85, 5 ayet); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure40_gafir_okuma.md` (`gafir_paket_md.py`). Ara zip'ler: 40:1-30, 40:1-60, 40:1-85 (de1a347 tabanı).

### Sûre 40 bilançosu (TAM SAYIM, `okuma_metni['40']['_bilanco_sure']`)
1219 kelime · lafız 53 token / 37 ayet · Rab 19 token / 14 ayet (A/R 2,79) · edilgen 18 ayet · iltifât alanı 8 ayet (23, 24, 32, 41, 45, 53, 55, 75) · hapaks 1 ayet (44 — فوض) · mm2 1 ayet (78, رسل).
Yıldız 0:48 · ★17 · ★★16 · ★★★4 (pas 3 — 40:62, 71, 72; hapaks 1 — 40:44). Kaynak: pas 13 · allah 12 · n 8 · rab 3 · hapaks 1; düzeltilmiş (1001): 40:23, 29, 30 kafiye.
Fâsıla sınıfı N 36 · ب 17 · R 15 · د 10 · ل 3 · ق 2 · ع 1 · (40:1 Hâ Mîm) 1; kafiye kırığı 5 (23, 29, 30, 35, 40). En uzun 40:28 (39); en kısa 40:1 (n=1 — besmele ayet metnine bitişik, veri biçimi). Sayı işareti 10 ayet: 11 isneteyn ×2 (iki ölüm, iki dirim), 12 ve 84 vahd, 16 vâhid, 8 zevc, 58 qalîl, 57/59/61/82 ekser (yanlış pozitif).

### Çıpa (aday 948 birikimi — ölçüt değişmedi)
**L4 yok.** En yüksek L2: 40:61 (gece dinlenme için, gündüz gösterici — 27:86 emsali) ve 40:67 (toprak → nutfe → alaka → bebek → güçlü çağ → yaşlılık; ara aşamalar adlı, L4 süreç koluna sınırda, mekanizma/birim yok — KAPATILAMAZ). L1 ×6 (11, 13, 57, 64, 79, 80) · L0 ×5 (21, 37, 46, 55, 82) · olgusuz tarayıcı adayı ×1 (29). Tarayıcı v4 adayları 5 (11, 29, 61, 67, 80), kesinlik **0/5**.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
29 e_oto tokeni → ilâhî 17 · değil 12. §4.3 mühür 15 → geçerli 9, yanlış 6 (23, 27, 33, 35, 39, 76). Geçerli mühür tonu: celâl 4 · denge 3 · karma 2.
Ölçüm satırı ↔ esma_kayit ayrışması (1022): 40:44 (ölçüm 'MÜHÜRSÜZ', kayıt mühür), 40:65 'hayy' (ölçüm 'esmâ yok', D2 eşlemesi), 40:76 'mutekebbirîn' (ölçüm 'esmâ yok', kayıt mühür — okuyucu kararı değil).

### ★ ADAY 1040 — ardışık sûre sınırında süreklilik (YENİ, P3, AÇIK)
Okuma gözlemi (blok 1-10): 39:1 'tenzîlu'l-kitâbi mina'llâhi'l-azîz' → 40:2 aynı terkip (esit2 0,9286 BENZER); 39:75 Arş'ın çevresi + 'yusebbihûne bi-hamdi rabbihim' → 40:7 Arş'ı taşıyanlar + aynı kalıp. Test önceden yazıldı, **korpus sonunda** koşulacak (ardışık sûre çiftleri ↔ uzunluk eşli ardışık olmayan çiftler, permütasyon). Okuma sırasında test edilmez. Dikkat: sûre 40-46 Hâ Mîm ailesi ortak açılışlı — aile etkisi ardışıklıktan ayrılmalı. 40:85 → 41:1 sınırı sûre 41 okunmadan yazılmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
Sûre 40'ın 85 ayetinin hepsinde ◇ 'Karşıt çift (aday 1039, okuma)' notu yazıldı; dolu 33 ayet. Sûre 39'un (16 + 7) verisiyle karşılaştırma için ölçüt sabit tutulmalı; karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler (yeni aday açılmadı, 1040 dışında)
* 1021/987 gloss: حول (çevre), بني (oğullar / bina), قوم (kavim / kalkma / kıyamet), سمو ('musemmâ' ad), شدد ('eşudd'), حمم (40:18 yakın dost), نور (sûredeki 8 geçişin hepsi nâr), أيي ('eyye' hangi), أثر ('âsâr' eserler).
* 517 biçim: takdimli haber ve câr-mecrûr ('lehum', 'ileynâ', 'minhâ', 'aleyhâ'), ayırma zamiri 'huve', 'innemâ' (40:68) işaretsiz.
* 1017 alıntı sınırı: 40:7-9 dua (giriş fiili söz fiili değil), 40:28-44 iman edenin konuşması (40:30 → 40:31-33 sürüyor — DUZELTME), 40:66 'qul' alıntısının bitişi, 40:73-74 soru ayet sınırını aşıyor, 40:75-76 konuşanı adsız, 40:76 'fe-bi'se' içeride mi dışarıda mı.
* 924 araç: tek fiilli ayette edilgen oranından ★★★ (40:62, 71, 72); 40:3 dört tamlama esmâ satırında yok; sayı işareti yanlış pozitifleri.
* 1001: kafiye kırığı ★ kaynağı 40:23, 29, 30.
* Tetik ön-kayıt §2: سحب (40:71 sürüklenme), فلك (40:80 gemi — S2 açık), قلب/حمل/زوج (40:4, 7, 8) — tetik kökü kozmik/organ anlamında değil, satırlar dolu.

### Okumada görülenler (KAPATILAMAZ; defter bağı olanlar AS_gafir'de)
* Sûre içi üçlü diziler: 'ellezîne yucâdilûne fî âyâti'llâh' 40:35, 56, 69 — üç yüklem (öfke / kibir / çevrilme); 'allâhu'llezî ce'ale lekum' 40:61, 64, 79 (gece-gündüz / yer-gök / davarlar); 'lâkinne ekserâ'n-nâsi lâ …' 40:57, 59, 61 (bilmez / inanmaz / şükretmez).
* Edilgen 'çevrilme' üç kez, çeviren adsız: 40:62 'tu'fekûn', 40:63 'yu'fek', 40:69 'yusrafûn'.
* 40:12 ↔ 40:84: aynı dört kök (وحد, كفر, شرك, أمن) ters dizilişte — tek anılınca inkâr / ortak koşulunca iman → tek O'na iman / ortaklara inkâr.
* 40:21 ↔ 40:82 yeryüzünde gezme kalıbı (nakarat3 8 kelime), 40:82'de 'eksera' eklenmiş.
* 40:28 iman eden 'ba'du'llezî ya'idukum' ↔ 40:77 1P 'ba'da'llezî ne'iduhum'.
* 40:49-50-60 aynı emir ('ud'û') üç konuşanda; 40:11 'emettenâ … ahyeytenâ' ↔ 40:68 'yuhyî ve yumît' sıra ters.
* 40:52 özür fayda vermez ↔ 40:85 iman fayda vermedi; 40:78 'el-mubtılûn' ↔ 40:85 'el-kâfirûn' ('ve hasira hunâlike').
* 40:85 son ayet ölçüm satırındaki 11 kökün hepsini kapatıyor (كون 25/25, أله 57/57, أمن 17/17, كفر 13/13); كفر sûrenin ilk (40:4) ve son kelimesi (40:85) arasında.
* Sûrenin adı (ğâfir) lemma olarak korpusta 2 ayette: 7:155, 40:3.

### Süreç dersleri (bu oturum)
* gafir_kayit ARIZA ekleme: son blok listesi `" ]\n}"` ile bitiyor; ekleme bu dizgeye göre yapılmalı (bir kez kısmi koşu → uret/aday ayrıca yeniden koşuldu).
* uret_blok_40 BASLIK satırına yeni blok eklerken önceki satırın virgülü kontrol edilmeli ((71, 80) virgülsüz kalmış, (81, 85) eklenince SyntaxError).
* Osmânî imlâ kalıpları: 'el-leyl' tek lam, 'yuhyî' küçük ye, 'sunnete'llâh' açık te — harekesiz kalıp kök/imlâ biçimiyle kurulmalı; 've' önekli kalıp sûre içi eşi kaçırabiliyor (40:13).
* Betik sabitlerine Arapça kelime biçimi yazılmadı (ARIZA satırında ilk yazışta girmişti, kayıttan önce Latin anlatıma çevrildi).

### Devam
Sûre 41 (Fussilet, 54 ayet) — `gafir_*` şablonlarından S=41 (aday numarası 1041'den, yeni set adları). Önce eksik kök kontrolü (sûrenin tümü). Sûre 2'nin 21-286'sı hâlâ sonraya. Açık kararlar: S2 (فلك), مأي gloss. Aday 1040 testi korpus sonunda.

## SÛRE 41 TUR SONU (2026-10-11)

**Okunan: 3064 / 6236 ayet (%49,1)** — sûre 1 ve 9-41 TAM, sûre 2 kısmi (1-20). İlerleme `fussilet_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1341** (`kok_ekle_41.py`: قوت, دخن, نحس, قيض, سأم, كمم, أفق). Aday havuzu **1040** (sûre 41'de yeni aday açılmadı; `AX_fussilet` boş). Bağ **AS_fussilet** 93. Esmâ okuyucu kararı (KARAR) **272**.
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik2 altı blokta da ilk koşuda 0 uyuşmaz · [x/y] sayım karşılaştırması **401 sayım, 0 uyuşmaz** · `AV_saffat` [1037, 1038], `AX_zumer` [1039], `AX_gafir` [1040], `AX_fussilet` [] repo dosyasından doğrulandı · retroaktif gloss yaması 0.
Sûrenin 54 ayeti 6 blokta okundu (son blok 51-54, 4 ayet); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure41_fussilet_okuma.md` (`fussilet_paket_md.py`). Ara zip: 41:1-30; tur sonu fark zip'i de1a347 tabanı.

### Sûre 41 bilançosu (TAM SAYIM, `okuma_metni['41']['_bilanco_sure']`)
794 kelime · lafız 11 token / 11 ayet · Rab 12 token / 12 ayet (A/R 0,92) · edilgen 14 ayet (3, 6, 14, 16, 19, 21, 30, 35, 40, 43, 44, 45, 47, 50) · iltifât alanı 0 · hapaks 0 · mm2 0.
Yıldız 0:42 · ★5 · ★★4 · ★★★3 (pas 3 — 41:19, 35, 43). Kaynak: pas 6 · n 3 · rab 2 · allah 1; düzeltilmiş (1001): 41:13 kafiye.
Fâsıla sınıfı N 37 · د 7 · R 2 · ط 2 · ز ب ص ظ ض birer · (41:1 Hâ Mîm) 1; kafiye kırığı 3 (13, 43, 45). En uzun 41:50 (32); en kısa 41:1. Sayı işareti 5 ayet: 4 ekser, 6 vâhid, 10 erbaa, 12 seb', 22 kesîr (yanlış pozitif).

### Çıpa (aday 948 birikimi — ölçüt değişmedi)
**L4 yok.** En yüksek L2: 41:39 (yer 'hâşi'a' → su indirilince → 'ihtezzet ve rabet'; adlı ara durumlar, L3 görünüş/durum koluna sınırda — KAPATILAMAZ; 22:5 aynı terkip 'hâmide'). L1 ×6 (9, 10, 11, 12, 16, 47) · L0 ×3 (13, 37, 38) · olgusuz tarayıcı adayı ×2 (15, 24). Tarayıcı v4 adayları 6 (13, 15, 16, 24, 37, 38), kesinlik **0/6**.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
22 e_oto tokeni → ilâhî 14 · değil 8. §4.3 mühür 16 → geçerli 9, yanlış 7 (7, 16, 21, 31, 34, 41, 47). Geçerli mühür tonu: denge 5 · cemâl 2 · karma 1 · celâl 1.
Ölçüm satırı ↔ esma_kayit ayrışması (1022) blok ARIZA kayıtlarında (ör. 41:21 'evvel' — ölçüm 'esmâ yok'; 41:41 'azîz' kitabın sıfatı; 41:47 'şehîd' çağrılanların sözü).

### Aday 1040 — sınır kaydı (test korpus sonunda)
40:2 → 41:2 (tenzîl + kaynak; Hâ Mîm ailesi içi), 40:85 → 41:7 (kâfirûn) AS_fussilet'te kayıt olarak. 41:54 → 42:1 sınırı sûre 42 okunmadan yazılmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
54 ayetin hepsinde not yazıldı; dolu 28 ayet. Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler (yeni aday açılmadı)
* 1021/987 gloss: صبح (41:12 kandiller / 41:23 oldunuz), جنن (cin / cennet), بشر (müjde / beşer), قرن (yakın dost), نزل (41:32 ikram), حمم (41:34 dost), سوي (eşit olma), نهر (gündüz), سبح (21:33/36:40 yüzme), خشع (yer için), لقي (kavuşturulma / atılma / kavuşma), خلف (arka / ayrılık), أذن (kulak / bildirme), ظنن (41:48 anlama), قضي (tamamlama / hüküm), عرض ('arîd' geniş), شقق (ayrılık).
* 517 biçim: takdim işaretsiz; 41:29 harfsiz nidâ; 41:33 'men ahsenu' sorusu, 41:46 'men' şartları, 41:51 'izâ' şartları ölçümde kip yok.
* 1017 alıntı / şahıs geçişi: 41:21 derilerin sözünün sonu; 41:22 konuşan adsız; 41:30-32 meleklerin sözü giriş fiilsiz ve sonu belirsiz; 41:44 ve 41:52 'qul' sınırı; 41:23→24, 28, 37→38, 39, 40, 45, 50, 53 şahıs geçişleri — ölçüm iltifât 0.
* 1001: kafiye kırığı ★ kaynağı 41:13; 41:43 ve 41:45'te kırık + pas birlikte.
* Tetik ön-kayıt §2: يدي deyim (41:14, 25, 42), سمع / بصر esmâ (41:36, 40), سمع yasak (41:26), حيي dünya hayatı (41:31) — satırlar dolu.

### Okumada görülenler (KAPATILAMAZ; defter bağı olanlar AS_fussilet'te)
* 'beyne yedeyhi … halfih' ikilisi üç kez üç özneyle: 41:14 elçiler, 41:25 yakın dostların süslediği, 41:42 bâtılın gelemediği kitap.
* Organların şahitliği 41:20-22 (kulak, göz, deri; 3MP → 2MP); شهد kökü sûrede 41:47 'mâ minnâ min şehîd' ve 41:53 'alâ kulli şey'in şehîd' ile kapanıyor.
* 41:5 inkârcıların 'fî âzâninâ vaqr' sözü 41:44'te 'fî âzânihim vaqr' (qul içinde); 41:3 'fussilet âyâtuhû … arabiyyâ' 41:44'te varsayılan itirazda.
* 41:45 = 11:110 kelimesi kelimesine (esit2 1,0000); 32:23 Musa'nın kitabı + 'fî miryetin min liqâih' tek ayette — 41:45 ve 41:54'ün iki parçası.
* 41:49 / 41:51 aynı 'messehu'ş-şerr' iki sonla (umutsuzluk / geniş dua); 17:83 aynı şart ikilisi 'ye'ûs' ile.
* 'lâ yes'emûn' (41:38 Rabbin katındakiler) / 'lâ yes'emu'l-insân' (41:49).
* 'qâle'llezîne keferû' iki alıntı: 41:26 'lâ tesme'û' / 41:29 'rabbenâ erinâ'; 41:29 'rabbenâ' / 41:30 'rabbuna'llâh'.
* 41:41 'inne'nin haberi metinde yok. 41:38 secde işareti. Fâsıla 41:1-38 ن/م, 41:39-40 ر, 41:41-54 sık değişiyor.
* Sûrenin adı (fussilet) 41:3, 41:44.

### Süreç dersleri (bu oturum)
* `fussilet_kayit` ARIZA eki son liste `" ],\n}"` ile bitiyordu; ekleme oturum yardımcısıyla (`ek41.py`: kayit/uret/bağ ekleri, çapa sayısı assert'li) yapıldı — elle dizgi değiştirme yerine.
* Harekesiz kalıp sayımında gürültü: 'fslt' ↔ 12:94 'fasalat', 'a'dâ'u'llâh' ↔ 'va'du'llâh', 'qurenâ'' ↔ 'qur'ân', 'mâ teddeûn' ↔ 'mâ ted'ûn', 'yulaqqâhâ' ↔ 'yelqâhu', 've min âyâtih' ↔ 20:75, 'âzennâke' ↔ 28:32, 'yes'emûn' ↔ 'yesemmûn' — hepsinde kalıp sayımı iddia edilmedi, lemma sayımı verildi.
* Sohbetteki bilanço maddesi kayıttan kopyalanmalı (41:11-20 'edilgen' maddesi karışık yazıldı; kayıt doğruydu).

### Devam
Sûre 42 (Şûrâ, 53 ayet) — `fussilet_*` şablonlarından S=42 (yeni set adları; aday numarası 1041'den). Önce eksik kök kontrolü. Sûre 2'nin 21-286'sı hâlâ sonraya. Açık kararlar: S2 (فلك), مأي gloss. Aday 1040 testi korpus sonunda.

## SÛRE 42 TUR SONU (2026-10-12)

**Okunan: 3117 / 6236 ayet (%50,0)** — sûre 1 ve 9-42 TAM, sûre 2 kısmi (1-20). İlerleme `shura_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1343** (`kok_ekle_42.py`: شرع, ركد). Aday havuzu **1041** (sûre 42'de 1 yeni aday: **1041**, `AX_shura`). Bağ **AS_shura** 98. Esmâ okuyucu kararı (KARAR) **314**.
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik2: 42:21-30'da ilk koşuda 1 uyuşmaz (42:27 ◈K أرض satırı "—" yazılmıştı, kayıttan önce dolduruldu), 42:11-20'de 42:11 ◈B satırı kayıttan önce eklendi, öbür dört blok ilk koşuda 0 · [x/y] sayım karşılaştırması **402 sayım (55 + 90 + 94 + 58 + 78 + 27), 0 uyuşmaz** · `AV_saffat` [1037, 1038], `AX_zumer` [1039], `AX_gafir` [1040], `AX_fussilet` [], `AX_shura` [1041] repo dosyasından doğrulandı · retroaktif gloss yaması 0.
Sûrenin 53 ayeti 6 blokta okundu (son blok 51-53, 3 ayet); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure42_shura_okuma.md` (`shura_paket_md.py`, 53 başlık). Ara zip'ler: 42:1-30, 42:1-50; tur sonu fark zip'i de1a347 tabanı.

### Sûre 42 bilançosu (TAM SAYIM, `okuma_metni['42']['_bilanco_sure']`)
860 kelime · lafız 32 token / 24 ayet · Rab 10 token / 9 ayet (A/R 3,2) · edilgen 6 ayet (14, 15, 16, 21, 36, 45) · iltifât alanı 1 (42:32, ayetler arası 2MP → 3MS) · hapaks 1 (42:33 ركد) · mm2 2 (24, 51).
Yıldız 0:31 · ★15 · ★★6 (10, 13, 15, 16, 24, 53) · ★★★1 (42:33 hapaks). Kaynak: allah 9 · n 7 · pas 4 · hapaks 1 · rab 1; düzeltilmiş (1001): kafiye 5 (17, 27, 28, 32, 41).
Fâsıla sınıfı R 20 · N 16 · ب 5 · ل 4 · د 4 · (42:1-2 hurûf-ı mukattaa) 2 · ز ص birer; kafiye kırığı 7 (10, 17, 27, 28, 32, 41, 45). En uzun 42:13 (38); en kısa 42:1-2. Sayı işareti 5 ayet: 8 vâhide, 11 zevc ×2, 30 ve 34 kesîr (yanlış pozitif), 50 'zuwwijat' (araç açığı, 924).

### Çıpa (aday 948 birikimi — ölçüt değişmedi)
**L4 yok.** En yüksek L2: 42:33 (rüzgârın durdurulması → 'fe-yazlelne revâkide'; şartlı, nedensel bağ adlı, mekanizma yok). L1 ×6 (5, 11, 28, 29, 49, 50) · L0 ×4 (4, 12, 32, 53) · olgusuz tarayıcı adayı ×2 (14, 27). 42:49-50 dörtlü sonuç kümesi (dişi / erkek / ikisi / kısır) L4 sınıflama koluna sınırda (aday 1014 ölçütü: üye eşlemesi yok). Tarayıcı v4 adayları 4 (11, 14, 27, 33), kesinlik **0/4**.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
42 e_oto tokeni → ilâhî 26 · değil 16. §4.3 mühür 21 → geçerli 15, yanlış 6 (8, 17, 20, 22, 31, 33). Geçerli mühür tonu: celâl 6 · denge 4 · cemâl 3 · karma 2.
Ölçüm satırı ↔ esma_kayit ayrışması (1022) blok ARIZA kayıtlarında (ör. 42:22 'kebîr' lütfun sıfatı; 42:31, 44, 46 olumsuzlanan dost; 42:33 'şekûr' insan; 42:48 'hafîz' muhatap için olumsuz; 42:52 'nûr').

### Aday 1041 (YENİ) — aynı kelimenin Allah ve insan için kullanılması
Kayıt (blok 31-40): şekûr 42:23 → 33; ğafr 42:5/23 → 37/43; afv 42:25/30/34 → 40; istecâbe 42:26 → 38 (haber), 47 (emir); insan grupları arasında şera'a 42:13 → 21, işfâk 42:18 → 22. Test korpus sonunda (esma_kayit 'ilahi' kökleri × aynı sûrede insan fâil/sıfatı; uzunluk eşli permütasyon). Gönderge ayrımı okuma kararıdır.

### Aday 1040 — sınır kaydı (test korpus sonunda)
41:43 → 42:3, 41:3 → 42:7, 39:75 → 40:7 → 42:5 (tesbih) kayıt olarak AS_shura'da; 42:51 'aliyyun hakîm' → 43:4 (henüz okunmadı) kayıt.

### Aday 1039 — okuma kolu (karşıt çift) verisi
53 ayetin hepsinde not yazıldı; dolu 33 ayet. Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1021 gloss: عرض (sunulma / yüz çevirme), روح (rüzgâr / ruh), بشر (müjde / beşer), ملك (melâike / mulk), ذكر (erkek), علم ('a'lâm' dağlar), ظلل (kalmak), قرف (iyilik kazanma), بغي, فطر, حول, حرث, قدر.
* 517 biçim: 'em' soruları (42:9, 21, 24), 'men' / 'mâ' / 'izâ' şartları (42:10, 20, 23, 30, 36, 37, 39, 40, 41, 43, 44, 46), 'innemâ' (42:42) ölçümde işaretsiz.
* 1017 alıntı / şahıs geçişi: 42:10 1S giriş fiilsiz; 42:13 1P → 2MP; 42:15 ve 42:23 'qul' sınırı; 42:45 iman edenlerin sözünün sonu; 42:47 emri veren adsız; 42:48 beş geçiş — ölçüm iltifât 0 (42:32 hariç).
* 1001: kafiye kırığı ★ kaynağı 17, 27, 28, 32, 41; 42:45 kırık + n 1,55 eşik üstü (iki aday kaynak); 42:10 kırık + allah 2,14.
* 924 araç: 42:50 sayı işareti 'zuwwijat', 42:51 ölçüm '1S' ('verâi' sonu) — metin hakkında kanıt değil.
* Tetik ön-kayıt §2: يدي deyim (42:30, 48), سمع / بصر esmâ (42:11, 27), حيي dünya hayatı (42:36), أنس insan (42:42, 48), يوم gün (42:45, 47) — satırlar dolu.

### Okumada görülenler (KAPATILAMAZ; defter bağı olanlar AS_shura'da)
* Vahiy çerçevesi: 42:3 'kezâlike yûhî ileyk' → 42:7 've kezâlike evhaynâ ileyk' → 42:13 → 42:51-52 (42:7 ve 42:52 aynı açılış).
* 'lehû mâ fi's-semâvâti ve mâ fi'l-ard' 42:4 ve 42:53 — sûrenin 4. ve son ayeti.
* İman edenlerin sıfat zinciri 42:36 'lillezîne' → 37-39 've'llezîne'; 'izâ … hum + IMPF' 42:37 (bağışlarlar) / 42:39 (karşı koyarlar); 42:41 / 42:43 savunma / sabır-bağışlama.
* 'min veliyyin ve lâ nasîr' 42:8, 31; 'tera'z-zâlimîn' 42:22, 44; 'men yudlili'llâh' 42:44 ('min veliyy') / 42:46 ('min sebîl'); 'sebîl' 42:41, 42, 44, 46.
* 9:91/93 ikilisi 42:41-42'de aynı sırayla; 28:60'ın üç parçası 42:36'da; 30:36 dizisi 42:48'de farklı sonla ('yaqnetûn' / 'kefûr'); 40:15 rûh-emr-'men yeşâ'-'ibâd' dörtlüsü 42:52'de.
* 42:32-34'te 'gemi' kelimesi yok ('el-cevâr' adsız); 42:49-50'de dişi/erkek sırası değişiyor; 42:52 'ce'alnâhu' zamiri (rûh / kitap) açık değil.
* Sûrenin adı 'şûrâ' yalnız 42:38'de (lemma korpusta 1).

### Dersler
* Tetik satırı yazarken ◈K listesindeki أرض 'fi'l-ard' gibi mekân kullanımlarında da tetikler — "—" yazılmaz (42:27).
* Bilanço ★ kaynağında z ≥ 1,5 ise "eşik altı" yazılmaz (42:45 ilk yazış düzeltildi).
* Harekesiz kalıp sayımında i'râb farkı görünmez ('el-insâne kefûr' ↔ 17:67) ve imlâ farkı ayırır ('cezâu' 10:27 / 42:40); bağ okuma ile kurulur, sayı verilmez.

### Devam
Sûre 43 (Zuhruf, 89 ayet) — `shura_*` şablonlarından S=43 (yeni set adları; aday numarası 1042'den). Önce eksik kök kontrolü. 42:51 → 43:4 ('aliyyun hakîm') aday 1040 alanında kayıt olarak yazılabilir. Sûre 2'nin 21-286'sı hâlâ sonraya. Açık kararlar: S2 (فلك tetik kesinliği), مأي gloss.

## SÛRE 43 TUR SONU (2026-10-13)

**Okunan: 3206 / 6236 ayet (%51,4)** — sûre 1 ve 9-43 TAM, sûre 2 kısmi (1-20). İlerleme `zuhruf_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1344** (`kok_ekle_43.py`: قدو). Aday havuzu **1041** (sûre 43'te yeni aday yok; `AX_zuhruf` boş). Bağ **AS_zuhruf** 135. Esmâ okuyucu kararı (KARAR) **341**.
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik: 43:11-20'de ilk koşuda 1 uyuşmaz (43:17 ◈B satırına tetiksiz gözlem yazılmıştı, kayıttan önce "—"), öbür sekiz blok ilk koşuda 0 · [x/y] sayım karşılaştırması **487 sayım (42 + 66 + 57 + 75 + 47 + 55 + 53 + 40 + 52), 0 uyuşmaz** · e_el=? her blokta 0 · `AV_saffat` [1037, 1038], `AX_zumer` [1039], `AX_gafir` [1040], `AX_fussilet` [], `AX_shura` [1041], `AX_zuhruf` [] repo dosyasından doğrulandı · retroaktif gloss yaması 0.
Sûrenin 89 ayeti 9 blokta okundu (son blok 81-89, 9 ayet); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure43_zuhruf_okuma.md` (`zuhruf_paket_md.py`, 89 başlık). Ara zip'ler: 43:1-30, 43:1-60; tur sonu fark zip'i 5e26cf0 tabanı.

### Oturum yardımcıları (YENİDEN KURULDU — salt-okur denetim aracı)
Önceki oturumların `oturum_*` betikleri klonda yoktu; bu oturumda yeniden yazıldı ve pakete kondu: `oturum_ortak.py` (korpus, morph, okundu/† durumu), `oturum_say.py` (harekesiz kalıp), `oturum_lem.py` (lemma / kök sayımı), `oturum_lemdizi.py` (lemma dizisi), `oturum_tetik.py` (◈K/◈B tetik ↔ satır), `oturum_xy.py` ([x/y] ↔ ölçüm). Ölçüm ya da kayıt üretmezler; yalnız okuma iddialarını sayar ve denetler. Araç dondurma kuralına uygunluğu kullanıcı onayına açık.

### Sûre 43 bilançosu (TAM SAYIM, `okuma_metni['43']['_bilanco_sure']`)
830 kelime · lafız **3 token / 3 ayet** (43:63, 64, 87; 43:1-62'de lafız yok) · Rab 13 token / 10 ayet (A/R 0,23) · edilgen 18 ayet (11, 17, 18, 19, 24, 31, 43, 44, 45, 53, 57, 70, 71, 72, 75, 83, 85, 87) · iltifât alanı 6 (7, 15, 35, 36, 68, 70) · hapaks 1 (43:79 برم; kök korpusta yalnız bu ayette) · mm2 0.
Yıldız 0:66 · ★7 · ★★9 (19, 31, 43, 53, 57, 70, 77, 85, 88) · ★★★7 (14, 18, 44, 64, 75, 79, 82). Kaynak: pas 14 · rab 6 · allah 2 · hapaks 1; düzeltilmiş (1001): kafiye 1 (43:59).
Fâsıla sınıfı N 87 · ل 1 (43:59) · 43:1 hurûf-ı mukattaa; kafiye kırığı 1 (43:59 'isrâîl'). En uzun 43:32 (25); en kısa 43:1. Sayı işareti 6 ayet: 12 ve 70 zevc, 17 ehad, 33 vâhide, 73 kesîre, 78 ekser.

### Çıpa (aday 948 birikimi — ölçüt değişmedi)
**L4 yok.** En yüksek L2: 43:11 (gökten ölçüyle su → ölü beldenin dirilmesi; nedensel bağ adlı, mekanizma yok). L1 ×4 (10, 12, 13, 51) · L0 ×5 (9, 82, 84, 85, 87) · olgusuz tarayıcı adayı ×2 (32, 60). Tarayıcı v4 adayları 6 (9, 10, 13, 32, 60, 87), kesinlik **0/6**.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
27 e_oto tokeni → ilâhî 12 · değil 15. §4.3 mühür 19 → geçerli 6, yanlış 13 (2, 4, 6, 8, 15, 18, 29, 35, 40, 56, 62, 81, 89). Geçerli mühür tonu: cemâl 3 · celâl 1 · denge 1 · karma 1.
'er-rahmân' bağımsız ad olarak ilâhî (aday 1019; 43:17, 19, 20, 33, 36, 45, 81). Kitap / insan / şeytan sıfatı 'mubîn', 'hakîm', 'aliyy', 'evvel', 'âhir' ve selam sözü 'selâm' değil (1022 ayrışmaları blok ARIZA kayıtlarında).

### Aday 1041 — kayıt (test korpus sonunda)
أسف: 20:86 Mûsâ 'ğadbâne esifâ' → 43:55 1P 'âsefûnâ'. برم: 43:79 3MP 'ebramû' / 1P 'mubrimûn' (tek ayet, kök korpusta yalnız burada). Sınırda (gönderge kitap, insan değil): 42:51 → 43:4 'aliyyun hakîm'; 43:4 → 43:84 'hakîm'.

### Aday 1040 — sınır kaydı (test korpus sonunda)
42:7 → 43:3 ('qur'ânen arabiyyâ'), 42:51 → 43:4 ('aliyyun hakîm'), 42:48 → 43:15 ('el-insân … kefûr') AS_zuhruf'ta kayıt. 43:89 → 44:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
89 ayetin hepsinde not yazıldı; dolu 25 ayet. Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1021 gloss: ملك (mulk / melâike / Mâlik / yemliku), ذهب (götürme / altın), قرن (güç yetirme / arkadaş / dizi dizi), خلف (yerine geçme / ayrılık), برم (yıpranma → kesin karar), سرر (tahtlar / gizli), لقي (atılma / kavuşma), نعم (davar / nimet), ظهر (sırt / üstüne çıkma), بني (bina → kız / oğul), أسف, خفف, صدد, نظر, حبر, قوم ('mustaqîm'), أيي ('eyyuhâ').
* 517 biçim: 'em' soruları, 'levlâ', tekit 'inne', müfâcee 'izâ', 'belâ', 'kezâlike' benzetmesi ölçümde işaretsiz.
* 1017 alıntı / şahıs geçişi: 43:10 alıntı sınırı; 43:11 3MS → 1P → 2MP; 43:63-64 Îsâ alıntısının sınırı; 43:61, 68 1S konuşan adsız; 43:68 → 69 1S → 1P; 43:71 3MP → 2MP; 43:77 'qâle' öznesi adsız; 43:78 1P; 43:88 'qîlihî' bağlantısı — ölçüm iltifât 0 (iltifât alanı 6 ayet hariç).
* 1022: ölçüm satırı esmâ ↔ esma_kayit mühür ayrışması (yukarıdaki 13 yanlış mühür).
* 1001: 43:59 ★ kaynağı 'allah z=-0,53' etiketli, düzeltilmiş kaynak kafiye kırığı.
* 1038 aktör rolü: 43:57 Meryem 'rol meful' (tamlamada muzâfun ileyh).
* 924 araç: 43:32 ölçüm 'biçim QASEM' — kök قسم paylaştırma, yemin yok; metin hakkında kanıt değil.
* Tetik ön-kayıt §2: سوع (43:61, 66, 85), يوم (43:39, 65, 67, 68, 83), زوج (43:12, 70), عين (43:71), سمع (43:40, 80), بصر (43:51), نهر (43:51), أرض mekân (43:60) — satırlar dolu; 43:38 'meşriqayn' (شرق listede değil) tetik değil.

### Okumada görülenler (KAPATILAMAZ; defter bağı olanlar AS_zuhruf'ta)
* 'in se'eltehum men halaqa' sûrede iki kez: 43:9 (gökler ve yer → 'el-azîzu'l-alîm') / 43:87 (kendileri → 'Allah'); 43:9 'el-azîzu'l-alîm' → 43:84 'el-hakîmu'l-alîm'.
* 'muhtedûn' fâsılası 43:22, 37, 49; 43:22 'muhtedûn' / 43:23 'muqtedûn'. Üç 'hayr' karşılaştırması 43:32, 52, 58. 'mesel' zinciri 43:8, 17, 56, 57, 59.
* Mûsâ anlatısı 43:46-56 (Firavun'un nutku 51-53: mülk, ırmaklar, 'ene hayr' — 38:76 İblis ile aynı söz); Meryem oğlu 43:57-59, adı 'Îsâ' ilk kez 43:63.
* 43:61-62 ↔ 36:60-61: aynı iki cümle ters sırada; 43:61-62 ↔ 20:15-16: sâ'a, ardından 'lâ yesuddenne'; 43:64-65 ↔ 19:36-37: aynı iki ayetlik sıra, ikinci yarı farklı.
* 43:61 'le-ilmun li's-sâ'a' → 43:85 'indehû ilmu's-sâ'a'. Cennet 43:70-73 / cehennem 43:74-77, 'hâlidûn' iki tarafta; 43:73 ↔ 23:19 aynı cümle (dünya bahçesi / cennet).
* Kök صفح sûrenin başında (43:5 'safhan') ve son ayetinde (43:89 'fa'sfah'). Sûrenin adı 'zuhruf' yalnız 43:35'te.

### Dersler
* Lemma dizisi sayımı kişi/önek farkını gizler — alıntı yazmadan önce ayet metni okunur (43:27 21:56, 43:51 32:27, 43:62 28:87 düzeltmeleri).
* Sûre içi kök geçiş listesi yazarken `oturum_lem.py --kok` "sûre içi" satırı esas alınır (43:69 أيي 'eyyuhâ', 43:86 ملك 43:19).
* "Emsallerde iddia reddediliyor" türü özetler yazılmadan önce emsal metni okunur (43:81).
* Büyük lemma listeleri (kâne, inne, lâ) sohbete dökülmez; çıktı kesilir.

### Devam
Sûre 44 (Duhân, 59 ayet) — `zuhruf_*` şablonlarından S=44 (yeni set adları; aday numarası 1042'den). Önce eksik kök kontrolü. 43:89 → 44:1 aday 1040 alanında kayıt olarak yazılabilir. Sûre 2'nin 21-286'sı hâlâ sonraya. Açık kararlar: S2 (فلك tetik kesinliği), مأي gloss.

## SÛRE 44 TUR SONU (2026-10-14)

**Okunan: 3265 / 6236 ayet (%52,4)** — sûre 1 ve 9-44 TAM, sûre 2 kısmi (1-20). İlerleme `duhan_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1348** (`kok_ekle_44.py`: أدي, رهو, غلي, عتل). Aday havuzu **1041** (sûre 44'te yeni aday yok; `AX_duhan` boş). Bağ **AS_duhan** 67. Esmâ okuyucu kararı (KARAR) **361**.
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik: altı blokta da ilk koşuda 0 uyuşmaz · [x/y] sayım karşılaştırması **213 sayım (39 + 43 + 36 + 36 + 31 + 28), 0 uyuşmaz** · e_el=? her blokta 0 · `AV_saffat` [1037, 1038], `AX_zumer` [1039], `AX_gafir` [1040], `AX_fussilet` [], `AX_shura` [1041], `AX_zuhruf` [], `AX_duhan` [] repo dosyasından doğrulandı · retroaktif gloss yaması 0.
Sûrenin 59 ayeti 6 blokta okundu (son blok 51-59, 9 ayet); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure44_duhan_okuma.md` (`duhan_paket_md.py`, 59 başlık). Ara zip: 44:1-30; tur sonu fark zip'i 5e26cf0 tabanı.

### Sûre 44 bilançosu (TAM SAYIM, `okuma_metni['44']['_bilanco_sure']`)
346 kelime · lafız **3 token / 3 ayet** (44:18, 19 elçinin sözü içinde; 44:42) · Rab 9 token / 7 ayet (6, 7, 8, 12, 20, 22, 57; A/R 0,33) · edilgen 2 ayet (4, 41) · iltifât alanı 9 (5, 6, 12, 13, 15, 22, 23, 30, 31) · hapaks 1 (44:24 رهو) · mm2 1 (44:16).
Yıldız 0:46 · ★3 (18, 19, 42; kaynak allah) · ★★4 (6, 7, 57 rab; 41 pas) · ★★★6 (8, 12, 20, 22 rab; 4 pas; 24 hapaks). Kaynak: rab 7 · allah 3 · pas 2 · hapaks 1; 1001 düzeltmesi yok.
Fâsıla sınıfı N 58 · 44:1 hurûf-ı mukattaa; kafiye kırığı yok. En uzun 44:37 (12); en kısa 44:1. Sayı işareti 3 ayet: 15 qalîl, 39 ekser, 54 'zevvecnâ' (yanlış pozitif — eşleştirme).

### Çıpa (aday 948 birikimi — ölçüt değişmedi)
**L4 yok.** En yüksek L1: 44:10 (göğün getireceği apaçık duman), 44:24 (deniz 'rehv'). L0 ×3 (7, 29, 38). Tarayıcı v4 adayı 1 (44:7), kesinlik **0/1**.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
20 e_oto tokeni → ilâhî 4 · değil 16. §4.3 mühür 16 → geçerli 2 (44:6 semî' + alîm; 44:42 azîz + rahîm), yanlış 14 (2, 4, 8, 10, 12, 13, 17, 19, 26, 33, 35, 41, 49, 56). Geçerli mühür tonu: denge 1 · karma 1.
Sıfat olarak geçen esmâ kelimeleri değil: 'mubîn' (kitap, duman, elçi, delil, sınav), 'hakîm' (iş), 'evvel/ûlâ' (atalar, ölüm), 'kerîm' (elçi, makam), 'mu'min', 'mevlâ' (insanlar); 44:49 'azîz' + 'kerîm' azaptakine hitap (1022).

### Aday 1041 — kayıt (test korpus sonunda)
'munzir' 1P 44:3 / Peygamber 13:7, 38:65. 'bataşa' insan 26:130, 28:19 / 1P 44:16. 'el-azîz' Allah 44:42 / azaptaki insan 44:49 / Mısır yöneticisi 12:30, 12:78. 'mevlâ' Allah 22:78 / insanlar 44:41.

### Aday 1040 — sınır kaydı (test korpus sonunda)
43:2 → 44:2 ('ve'l-kitâbi'l-mubîn', esit2 TAM; devamı farklı), 43:83 → 44:9, 43:41 → 44:16 ('muntaqimûn'), 43:49-50 → 44:12-15, 43:88 → 44:22, 43:52 · 58 → 44:37; sûre sonları 43:89 / 44:59 ('fe' + 2MS emir + 3MP hakkında cümle). 44:59 → 45:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
59 ayetin hepsinde not yazıldı; dolu 5 ayet (7, 8, 29, 35, 38). Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1021 gloss: ولي (yüz çevirme / dost), أمر (iş / emir), جنن ('mecnûn' / cennet), عين (pınar / göz), قوم ('maqâm'), نظر ('munzar' mühlet), علو, علم ('ilm' / 'âlemîn'), خير ('ihtâra'), مهل (erimiş maden), حور (hûr).
* 517 biçim: tekit 'inne' / 'innâ', benzetme 'ke', 'kem', 'kezâlike', 'innemâ' ölçümde işaretsiz.
* 1017 konuşan / şahıs geçişi: 44:11 'hâzâ azâbun elîm' kimin sözü işaretsiz; 44:12 1P konuşanlar adsız; 44:17-24 elçi ve emir veren adsız (26:52'de adlı Mûsâ); 44:28 'qavmen âharîn' adsız; 44:34 'hâulâi'; 44:47-50 emir veren / konuşan adsız; 44:56 'vekâhum' öznesi; 44:58 'yessernâhu' zamiri — ölçüm iltifât 0 (iltifât alanı 9 ayet hariç).
* 1022: ölçüm satırı esmâ ↔ esma_kayit mühür ayrışması (yukarıdaki 14 yanlış mühür).
* Tetik ön-kayıt §2: ليل (44:3, 23), سمو/أرض (44:7, 10, 29, 38), يوم (44:10, 16, 40, 41), حيي/موت (44:8), موت (44:35, 56), أنس (44:11), بحر (44:24), عين (44:25, 52 pınar; 44:54 göz), خلق (44:38, 39), شجر (44:43), زوج (44:54), سمع (44:6 esmâ) — satırlar dolu.

### Okumada görülenler (KAPATILAMAZ; defter bağı olanlar AS_duhan'da)
* 'fe-rtaqib' 2MS emri sûrede iki kez: 44:10 (duman günü) ve son ayet 44:59. 1P + 'hu': 44:3 'enzelnâhu' / 44:58 'yessernâhu'; 44:58 ↔ 19:97 aynı açılış, amaç farklı.
* 28:45-46 → 44:5-6; 26:24, 26:26 → 44:7-8 (Mûsâ'nın iki cevabı art arda, 26:25 yok).
* Firavun anlatısı 44:17-33; 44:23-28 Şuarâ 26:52-59 sırasıyla. 44:25-26 bırakılan 'cennât, uyûn, maqâm kerîm' / 44:51-52 takvâ sahiplerinin 'maqâm emîn, cennât, uyûn'.
* 'el-mevtetu'l-ûlâ' üç ağızda: 37:59 cennet ehli, 44:35 inkârcılar, 44:56 anlatı; 37:58-60 → 44:56-57 aynı sıra ('huve'l-fevzu'l-azîm').
* 37:62-68 zakkum dörtlüsü (zakkum, butûn, hamîm, cahîm) → 44:43-48; 22:19 → 44:48 (edilgen çoğul / emir tekil). Cehennem 44:43-50 / cennet 44:51-57 art arda.
* 44:38-39 = 21:16 + 15:85; 44:9 'yel'abûn' → 44:38 'lâ'ibîn'. Sûrenin adı 'duhân' yalnız 44:10'da (lemma korpusta 41:11, 44:10).

### Dersler
* Yarıda kalan bir turun dosyaya yazdığı taslak kendi işi sayılmaz; her sayı ve alıntı kayıttan önce yeniden koşulur (44:41-50: bir doğrulanmamış iddia çıkarıldı).
* Sûre içi liste (Rab, 1P vb.) yazmadan önce `oturum_lem.py --kok` ya da morph sayımı; hafızadan liste yazılmaz (44:54, 44:57 düzeltmeleri).
* Görülmemiş ayet anılmaz (44:56'da 52:18 anması çıkarıldı).

### Devam
Sûre 45 (Câsiye, 37 ayet) — `duhan_*` şablonlarından S=45 (yeni set adları; aday numarası 1042'den). Önce eksik kök kontrolü. 44:59 → 45:1 aday 1040 alanında kayıt olarak yazılabilir; 44:36 → 45:25 xref var. Sûre 2'nin 21-286'sı hâlâ sonraya. Açık kararlar: S2 (فلك tetik kesinliği), مأي gloss.

## SÛRE 45 TUR SONU (2026-10-14)

**Okunan: 3302 / 6236 ayet (%53,0)** — sûre 1 ve 9-45 TAM, sûre 2 kısmi (1-20). İlerleme `casiye_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1351** (`kok_ekle_45.py`: صرر, جرح, دهر). Aday havuzu **1041** (sûre 45'te yeni aday yok; `AX_casiye` boş). Bağ **AS_casiye** 47. Esmâ okuyucu kararı (KARAR) **370**.
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik: dört blokta da ilk koşuda 0 uyuşmaz · [x/y] **292 sayım (67 + 80 + 96 + 49), 0 uyuşmaz** · e_el=? her blokta 0 · `AV_saffat` [1037, 1038], `AX_zumer` [1039], `AX_gafir` [1040], `AX_fussilet` [], `AX_shura` [1041], `AX_zuhruf` [], `AX_duhan` [], `AX_casiye` [] repo dosyasından doğrulandı · retroaktif gloss yaması 0.
Sûrenin 37 ayeti 4 blokta okundu (son blok 31-37, 7 ayet); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında (dolu 17 ayet). Paket `notlar/sure45_casiye_okuma.md` (`casiye_paket_md.py`, 37 başlık). Ara zip: 45:1-30; tur sonu fark zip'i 5e26cf0 tabanı.

### Sûre 45 bilançosu (TAM SAYIM, `okuma_metni['45']['_bilanco_sure']`)
488 kelime · lafız **18 token / 15 ayet** · Rab 7 token / 5 ayet (11, 15, 17, 30, 36 ×3; A/R 2,57) · edilgen 9 ayet (8, 15, 22, 25, 28, 31, 32, 34, 35) · iltifât alanı 0 · hapaks 0 · mm2 0.
Yıldız 0:27 · ★4 (11, 15 rab; 28, 34 pas) · ★★5 (2, 6, 19 allah; 22, 35 pas) · ★★★1 (36 rab, z=7,67). 1001 düzeltmesi yok.
Fâsıla sınıfı N 36 · 45:1 hurûf-ı mukattaa; kafiye kırığı yok. En uzun 45:17 ve 45:23 (24); en kısa 45:1. Sayı işareti 1 ayet: 26 ekser.

### Çıpa (aday 948 birikimi — ölçüt değişmedi)
**L4 yok.** En yüksek L2: 45:5 (gökten indirilen rızıkla ölü yerin diriltilmesi; 16:65, 30:24, 35:9 emsali). L1 ×3 (4, 12, 13) · L0 ×5 (3, 22, 24 olgusuz, 36, 37). Tarayıcı v4 adayları 2 (12, 22), kesinlik **0/2**.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
9 e_oto tokeni → ilâhî 5 (45:2 ×2, 19 'veliyy', 37 ×2) · değil 4 (3 'mu'min', 10 'evliyâ'', 19 'evliyâ'', 30 'mubîn'). §4.3 mühür 6 → geçerli 3 (2, 19, 37), yanlış 3 (3, 10, 30). Geçerli mühür tonu: celâl 2 · cemâl 1.
**Kayıt düzeltmesi (DUZELTME 45:37, 1022):** 45:2, 19, 37 için sohbet metninde ve blok ARIZA kayıtlarında "bilanço geçerli mühür değil" yazılmıştı; bu, okuyucu kararı eklenmeden ÖNCE koşulan bilançoya bakılarak yazılmıştı. Kayıtlı bilanço üçünü de geçerli sayıyor. Özgün alan korunur.

### Aday 1041 — kayıt (test korpus sonunda)
'veliyy' 45:19 aynı ayette zâlimler ('ba'duhum evliyâu ba'd') / Allah ('va'llâhu veliyyu'l-muttaqîn'); 45:10 edinilen 'evliyâ''; 9:71 mü'minler 'ba'duhum evliyâu ba'd'. 'kibriyâ'' 10:78 (Firavun'un ileri gelenlerinin Mûsâ ve Hârûn'a isnadı) / 45:37 (O'nun).

### Aday 1040 — sınır kaydı (test korpus sonunda)
44:59 → 45:1; 44:44 → 45:7 ('esîm'); 44:32 → 45:16 ('ale'l-âlemîn'); 44:4-5 → 45:17-18 ('emr'); 44:35-36 → 45:24-25 (inkâr + ''tû bi-âbâinâ in kuntum sâdiqîn', xref ölçüm); 44:57 → 45:30 ('el-fevzu'l-azîm' / '… el-mubîn'). 45:37 → 46:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
37 ayetin hepsinde not yazıldı; dolu 17 ayet. Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1021 gloss: روح (rüzgâr), بغي (arama / azgınlık), شرع ('şerî'a'), نور (ateş).
* 517 biçim: ta'lîl 'li-', şart 'men' / 'izâ', soru 'em', zem 'sâe', tekit, 'ke-en', 'kemâ' ölçümde işaretsiz.
* 1017 konuşan / şahıs geçişi: 45:4, 14 adsız özne; 45:8 okuyan ve muhatap; 45:11, 20 'hâzâ' göndergesi; 45:24-25 söyleyenler; 45:28-29 alıntı sınırı ve 1P konuşan; 45:31 1S konuşan ('âyâtî'; 23:105 aynı); 45:32, 34 'qîle'; 45:35 2MP → 3MP — ölçüm iltifât 0.
* 1022: yukarıdaki 3 yanlış mühür; geçerli mühür iddiası düzeltmesi (DUZELTME 45:37).
* Tetik ön-kayıt §2: سمو/أرض (45:3, 5, 13, 22, 27, 36, 37), ليل/نهر/روح (45:5), بحر/فلك (45:12; 'fulk' gemi, S2 açık), يوم (45:14, 17, 26, 27, 28, 34, 35), سوع (45:27, 32), دهر (45:24), حيي/موت (45:5, 21, 24, 26; 45:35 حيي), خلق (45:4, 22), دبب (45:4), سمع (45:8, 23), قلب/بصر (45:23), بصر/أنس (45:20), أنس (45:26) — satırlar dolu.

### Okumada görülenler (KAPATILAMAZ; defter bağı olanlar AS_casiye'de)
* 45:2 / 45:37 'el-azîz el-hakîm' — sûrenin ikinci ve son ayeti.
* 'Âyât + kavim niteliği' dizisi: 45:3 mu'minîn, 45:4 yûqinûn, 45:5 ya'qilûn, 45:13 yetefekkerûn, 45:20 yûqinûn; 2:164 (henüz okunmadı) 45:4-5'in dört lemma dizisinde de var.
* 31:6-7 → 45:8-9 aynı iki unsur ters sırada; 10:93 → 45:16-17 aynı dört öğe ve aynı kapanış cümlesi (42:14 ifadesiyle); 2:7 → 45:23 üç organ, mühür, perde (sıra ve sayı farklı); 23:37 + 43:20 → 45:24; 23:62 → 45:22 + 45:29.
* 45:24 'nemûtu ve nahyâ' / 45:26 'yuhyîkum summe yumîtukum summe yecma'ukum'; 45:24 'in hum illâ yezunnûn' / 45:32 'in nezunnu illâ zannâ'.
* 45:30-31 'emmâ' taksimi; 32:14 → 45:34 karşılıklı unutma (sıra ters); 39:48 + 16:34 → 45:33; 1:2 → 45:36. Sûrenin adı 'câsiye' korpusta yalnız 45:28'de.

### Dersler
* Esmâ bilanço iddiası (geçerli / yanlış mühür) okuyucu kararı eklendikten SONRA koşulan bilançodan yazılır; ön-tarama bilançosu karar öncesidir (sûre 45: 45:2, 19, 37).
* Lemma dizisi sayımı ardışık iki kelimeyi terkip sanabilir — terkip iddiasından önce eş ayetlerin metni okunur (45:14, 40:16).

### Devam
Sûre 46 (Ahkâf, 35 ayet) — `casiye_*` şablonlarından S=46 (yeni set adları; aday numarası 1042'den). Önce eksik kök kontrolü. 45:37 → 46:1 aday 1040 alanında kayıt olarak yazılabilir (46:1-2 = 45:1-2 esit2 TAM). Sûre 2'nin 21-286'sı hâlâ sonraya. Açık kararlar: S2 (فلك tetik kesinliği), مأي gloss.

## SÛRE 46 TUR SONU (2026-10-14)

**Okunan: 3337 / 6236 ayet (%53,5)** — sûre 1 ve 9-46 TAM, sûre 2 kısmi (1-20). İlerleme `ahkaf_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1354** (`kok_ekle_46.py`: بدع, حقف, عيي). Aday havuzu **1041** (sûre 46'da yeni aday yok; `AX_ahkaf` boş). Bağ **AS_ahkaf** 56. Esmâ okuyucu kararı (KARAR) **381**.
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik: dört blokta da ilk koşuda 0 uyuşmaz · [x/y] **364 sayım (88 + 114 + 106 + 56), 0 uyuşmaz** · e_el=? her blokta 0 · `AV_saffat` [1037, 1038], `AX_zumer` [1039], `AX_gafir` [1040], `AX_fussilet` [], `AX_shura` [1041], `AX_zuhruf` [], `AX_duhan` [], `AX_casiye` [], `AX_ahkaf` [] repo dosyasından doğrulandı · retroaktif gloss yaması 0 · DUZELTME 0.
Sûrenin 35 ayeti 4 blokta okundu (son blok 31-35, 5 ayet); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında (dolu 19 ayet). Paket `notlar/sure46_ahkaf_okuma.md` (`ahkaf_paket_md.py`, 35 başlık). Ara zip: 46:1-30; tur sonu fark zip'i 5e26cf0 tabanı.

### Sûre 46 bilançosu (TAM SAYIM, `okuma_metni['46']['_bilanco_sure']`)
643 kelime · lafız **16 token / 14 ayet** · Rab 4 token / 4 ayet (13, 15, 25, 34) · edilgen 14 ayet · iltifât alanı 0 · hapaks 1 (46:21 حقف 'ahqâf', sûrenin adı).
Yıldız 0:22 · ★9 · ★★2 · ★★★2 (46:15 n z=3,46; 46:21 hapaks z=3,28). Kaynak: n 7, pas 4, allah 1, hapaks 1.
Fâsıla sınıfı N 33 · 46:1 hurûf-ı mukattaa · 46:33 ر **kafiye kırılması**. En uzun 46:15 (45).

### Çıpa (aday 948 birikimi — ölçüt değişmedi)
**46:15 L4 adayı, TARTIŞMALI** — ölçü kolu tek başına ('selâsûne şehrâ' taşıma + sütten kesme, 'erba'îne sene'; mekanizma yok); 31:14 emsali ('iki yıl'), iki ölçü arasındaki hesap metinde yok. L1 ×5 (3, 24, 26, 33, 35) · L0 ×1 (4). 46:24 ve 46:35 L3 koluna sınırda (algı/durum, karşılaştırma ya da durum söylenmiyor). Tarayıcı v4 adayları 4 (4, 15, 33, 35), kesinlik **1/4**, anma 1/1.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
11 e_oto tokeni → ilâhî 6 (46:2 ×2, 8 ×3, 33 'qadîr') · değil 5 (7 'mubîn', 9 'mubîn', 17 'evvel', 32 'velî', 32 'mubîn'). §4.3 mühür 7 → geçerli 3 (2, 8, 33), yanlış 4 (7, 9, 17, 32). Geçerli mühür tonu: celâl 2 · karma 1.
Her blokta bilanço okuyucu kararı eklendikten SONRA koşuldu (sûre 45 dersi uygulandı).

### Aday 1041 — kayıt (test korpus sonunda)
شهد 46:8 'şehîd' (Allah) / 46:10 'şâhid' (İsrâiloğullarından biri) — kök ortak, sınırda. وعد 46:16 'va'de's-sıdq … yû'adûn', 46:17 anne babanın vaadi 'ete'idâninî' ile 'va'da'llâh' aynı ayette — kök ortak, sınırda. 'velî' lemması 42:9 'fe'llâhu huve'l-veliyy' / 46:32 'min dûnihî evliyâ''.

### Aday 1040 — sınır kaydı (test korpus sonunda)
45:37 → 46:1-2 ('el-azîz el-hakîm'; 46:1-2 = 45:1-2 esit2 TAM). 46:1 'Hâ Mîm' dizisinin son sûresi (40:1-45:1 esit2 TAM, hepsi okundu). 46:35 → 47:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
35 ayetin hepsinde not yazıldı; dolu 19 ayet. Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1021 gloss: أثر (46:4 'esâre' kalıntı; gloss 'tercih etme'); نهر (46:35 'nehâr' gündüz; gloss 'ırmak' — tetik satırı dolu, anlam okumayla).
* 517 biçim: 'men' / 'em' sorusu, 'izâ', şart cevabı hazfi (46:10), tekit 'inne', nidâ, 'innemâ', 'lâkinne', 'lev lâ', emrin cevabı cezmi, 'belâ', yemin, 'ke-enne' ölçümde işaretsiz.
* 1017 konuşan / gönderge: 'qul' muhatabı ve alıntı içi 1S (46:4, 8, 9); 46:5-6 3MP göndergeleri; 46:10 şahit; 46:11 'bihî'; 46:12 'li-yunzira' öznesi; 46:17 'ellezî'; 46:19 fâil; 46:20, 24, 34 alıntının söyleyeni; 46:21 Âd'ın kardeşi (11:50, 26:124'te adlı); 46:21, 29, 35 muhatap 2MS; 46:31 'dâ'iya'llâh' — ölçüm iltifât 0.
* 1022: yukarıdaki 4 yanlış mühür; 46:17 'evvel' ölçümde esmâ yok, 46:32-33 ölçümde MÜHÜRSÜZ.
* Tetik ön-kayıt §2: سمو/أرض (46:3, 4, 33; أرض 20, 32), أجل (3), خلق (3, 4, 33), يوم (5, 20, 21, 34, 35), أنس (6, 15, 18), سنو/حمل/وضع (15), حيي (20, 33), موت (33), يدي (21, 30), روح (24), سمع (26, 29, 30), بصر (26), سوع/نهر (35) — satırlar dolu.

### Okumada görülenler (KAPATILAMAZ; defter bağı olanlar AS_ahkaf'ta)
* 46:3 / 46:33 gökler-yer yaratması (1P / 3MS lafız); 46:20 / 46:34 aynı açılıştan iki alıntı; 46:12 / 46:30 Mûsâ'nın kitabı 'önce' / 'sonra'.
* 15:85 + 30:8 → 46:3; 35:40 → 46:4; 41:52'nin iki parçası 46:5 ve 46:10'da; 34:43 → 46:7; 11:35 + 13:43 + 29:52 → 46:8; 10:15 + 38:70 → 46:9; 11:17 sırası (şahit, Mûsâ'nın kitabı) 46:10 → 46:12.
* 41:30 → 46:13 (devamı farklı); 29:8 + 31:14 + 27:19 + 41:33 → 46:15; 17:23 → 46:17 ('uff' yasaklanan söz söyleniyor); 41:25 → 46:18 (15 lemma).
* Âd anlatısı: 41:14 + 26:135 → 46:21; 11:32 → 46:22; 11:29, 11:57, 33:63 → 46:23 (11:29, 11:32 Nûh anlatısında); 41:16 → 46:24; 10:13, 29:38 → 46:25; 16:78, 23:78, 32:9 → 46:26 (üç organ; şükür yerine 'yarar sağlamadı').
* 17:99, 42:9 → 46:33; 34:3 → 46:34; 10:45 → 46:35. أمم kökü üç ayrı kelimeyle (46:12 'imâm', 46:15 'umm', 46:18 'umem').

## SÛRE 47 TUR SONU (2026-10-15)

**Okunan: 3375 / 6236 ayet (%54,1)** — sûre 1 ve 9-47 TAM, sûre 2 kısmi (1-20). İlerleme `muhammed_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1364** (`kok_ekle_47.py`: ثخن تعس أسن عسل معي أنف شرط قفل ضغن لحن). Aday havuzu **1041** (sûre 47'de yeni aday yok; `AX_muhammed` boş). Bağ **AS_muhammed** 91. Esmâ okuyucu kararı (KARAR) **385**.
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik: 1-10, 21-30, 31-38 ilk koşuda 0; 11-20 ilk koşuda 1 (47:15 ◈B tetiksiz dolu — düzeltildi), ikinci koşuda 0 · [x/y] **267 sayım (52 + 82 + 68 + 65), 0 uyuşmaz** (1-10 ilk koşuda 1: 47:9 عمل) · e_el=? her blokta 0 · `AX_*` setleri repo dosyasından doğrulandı (`AX_zumer` [1039], `AX_gafir` [1040], `AX_shura` [1041], öbürleri boş) · retroaktif gloss yaması 0 · DUZELTME 0.
Sûrenin 38 ayeti 4 blokta okundu (son blok 31-38, 8 ayet); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure47_muhammed_okuma.md` (`muhammed_paket_md.py`, 38 başlık). Ara zip: 47:1-30 (taban cf56af3); tur sonu fark zip'i cf56af3 tabanı (5e26cf0 sonrası sûre 46 paketi depoya girmişti).

### Sûre 47 bilançosu (TAM SAYIM, `okuma_metni['47']['_bilanco_sure']`)
539 kelime · lafız **27 token / 21 ayet** · Rab 4 token / 4 ayet (2, 3, 14, 15) · A/R 6,75 · edilgen 7 ayet · iltifât alanı 3 ayet (22, 23, 32) · hapaks ayet 5 (8, 15 ×3 kök, 18, 24, 30).
Yıldız 0:21 · ★6 · ★★6 · ★★★5 (hepsi hapaks). Kaynak (1001 düzeltmeli): allah 7, hapaks 5, n 2, pas 2, kafiye 1 (47:10).
Fâsıla N 36 · 47:10 ا ve 47:24 ٓ **kafiye kırılması**. En uzun 47:15 (44), en kısa 47:5.

### Çıpa (ölçüt değişmedi)
L4 yok. L0 ×2 (10, 22), L1 ×1 (23 — 46:26'da verilen organlar burada alınan). 47:15, 47:36 olgu yok. Tarayıcı v4 adayları 2 (22, 36), kesinlik **0/2**, anma 0/0.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
4 e_oto tokeni → ilâhî 2 (47:11 'mevlâ' ilk, 47:38 'ğaniyy') · değil 2 (47:11 'lâ mevlâ lehum', 47:19 'mu'min'). §4.3 mühür 1 → geçerli 1 (47:11; ölçüm satırı MÜHÜRSÜZ — 1022). Geçerli mühür tonu: belirsiz 1.

### Aday 1041 — kayıt (test korpus sonunda)
نصر 47:7 'in tensurû'llâha yensurkum' (aynı ayette iki yön); 'intesara' 47:4 Allah / 26:93, 26:227, 42:39, 42:41 insan · ولي 47:11 'mevlâ' / 'lâ mevlâ lehum' · علم 47:19 'fa'lem' / 've'llâhu ya'lemu' · 'ahraca' 47:13 kasaba / 47:29 Allah · 'ebtale' 10:81 Allah / 47:33 inananlar. Sınırda: 47:1-2 'keferû' / 'keffera'; 'haqq' 22:62, 31:30 / 47:2; عرف 47:6 / 47:30 (farklı lemma); 'emlâ' 47:25 (özne belirsiz).

### Aday 1040 — sınır kaydı (test korpus sonunda)
46:34-35 → 47:1 ('ellezîne keferû'); 46:25 'tudammiru' → 47:10 'dammera' (aynı lemma). 47 hurûf-ı mukattaa olmadan açılıyor (Hâ Mîm dizisi 46'da bitti). 47:38 → 48:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
38 ayetin hepsinde not yazıldı. Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1021 gloss: دبر 'arka' — 47:24 'tedebbür'ü kapsamıyor; 'menn' lemması 20:80 (yiyecek) / 47:4 (karşılıksız bırakma).
* 1001: 47:10 ★ kafiye kırığından, bilanço 'allah' etiketliyor.
* 517 biçim: tekit 'inne', 'lev' cevap lâmı, 'lâkin', 'immâ … ve immâ', teşbih ('kemâ', 'ke-men'), 'em' munkatı'a, 'innemâ', 'lev lâ' tahzîzi, cevabı düşmüş 'keyfe', masdarla beddua (47:8), tenbîh 'hâ', yüklemsiz isim cümlesi (47:21) ölçümde işaretsiz.
* 1017 konuşan / gönderge: adsız 3MS özne ('adalle', 'ahbata', 'zâde', 'yu'tî', 'yuhric', 'emlâ'); 2MS / 2MP muhatap; ayetler arası 3MP ↔ 2MP ↔ 1P geçişleri (47:3→4, 47:12→13) ölçümde iltifât 0.
* ◈B tetik dışı organ (ön-kayıt §4 sınırı): 47:15 'em'â'' (معي), 'şârib' (شرب) — satır '—', gözlem ◇'de. Yeni tetik sınıfı değil, kayıt.

### Okumada görülenler (KAPATILAMAZ; defter bağı olanlar AS_muhammed'de)
* 'ellezîne keferû ve saddû an sebîli'llâh' sûre içi 47:1, 32, 34; عمل 12/12: 47:1 'adalle a'mâlehum' → 47:35 'len yetirakum a'mâlekum'; 'zâlike bi-enne' 47:3, 9, 11, 26, 28.
* 11:17 + 35:8 açılışları 47:14'te yan yana; 47:14 / 47:15 aynı 'ke-men' iskeleti; 47:15 'mâ'' iki tarafta.
* 47:25 'edbârihim' → 47:27 'edbârahum'; ضرب üç özne (3, 4, 27); kalp sırası 16 mühür, 20 / 29 hastalık, 24 kilit; 22:46 → 47:23.
* 9:39'un iki parçası 47:32 ve 47:38'de; 35:15 → 47:38 sıra ters; 47:22 / 47:38 'in tevelleytum / tetevellev' iki sonuç.
* 12:109, 30:9, 35:44, 40:21, 40:82 → 47:10 (aynı açılış, devamı farklı); 22:14, 22:23 → 47:12; 13:35 → 47:15; 16:108 → 47:16; 43:66 → 47:18; 24:54, 33:66 → 47:33; 29:64 → 47:36.

## SÛRE 48 TUR SONU (2026-10-15)

**Okunan: 3404 / 6236 ayet (%54,6)** — sûre 1 ve 9-48 TAM, sûre 2 kısmi (1-20). İlerleme `fetih_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1366** (`kok_ekle_48.py`: ظفر حلق). Aday havuzu **1041** (sûre 48'de yeni aday yok; `AX_fetih` boş). Bağ **AS_fetih** 78. Esmâ okuyucu kararı (KARAR) **412**.
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik üç blokta ilk koşuda 0 (ön kuru koşu ile) · [x/y] **313 sayım (77 + 122 + 114), 0 uyuşmaz** (21-29 ilk koşuda 1: 48:28 شهد [1/2] → [2/2]) · e_el=? her blokta 0 · retroaktif gloss yaması 0 · DUZELTME 0.
Sûrenin 29 ayeti 3 blokta okundu (son blok 21-29, 9 ayet); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure48_fetih_okuma.md` (`fetih_paket_md.py`, 29 başlık). Fark zip'i cf56af3 tabanı (sûre 47 ve 48 birlikte; sûre 47 zip'i depoya henüz girmemişti).

### Sûre 48 bilançosu (TAM SAYIM, `okuma_metni['48']['_bilanco_sure']`)
560 kelime · lafız **39 token / 25 ayet** · Rab 0 · edilgen 2 ayet (12, 16) · iltifât alanı 1 ayet (8) · hapaks 0.
Yıldız 0:11 · ★9 · ★★6 · ★★★3 (48:3, 48:7 kaynak allah — kısa ayet; 48:29 kaynak n — uzun ayet). Kaynak: allah 10, n 8.
Fâsıla 29/29 ا — kafiye kırığı yok. En uzun 48:29 (54), en kısa 48:3. mm2 4 ayet (12, 16, 17, 28).

### Çıpa (ölçüt değişmedi)
L4 kesin yok. L0 ×4 (4, 7, 14 gökler ve yer tamlamada; 18 ağaç biatin yeri). 48:5, 48:17 cennet ırmakları olgu değil. **48:29 ekin büyümesi**: dört aşama 'fe' dizisi, ara parçalar adlı (şat', sûq) — 39:21 emsaline göre L4 mekanizma kolu adayı, ama teşbih içinde (İncil'deki mesel) → **L4 adayı, TARTIŞMALI; cipa kararı kullanıcıya açık** (kayıtta cipa=False). Tarayıcı v4 adayları 3 (4, 5, 29), kesinlik **0/3** (48:29 kısmi).

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
27 e_oto tokeni → ilâhî 13. §4.3 mühür 15 → geçerli 9 (4, 7, 11, 14, 19, 21, 24, 26, 28) · yanlış 6 (1 'mubîn', 3 'azîz', 18 ve 27 'qarîb' — fethin / yardımın sıfatı; 20 'mu'min'; 22 'veliyy' + 'nasîr' olumsuzlanan başkası). Geçerli mühür tonu: denge 5, celâl 3, cemâl 1. Ölçüm satırı MÜHÜRSÜZ / esma_kayit EVET ayrışması birçok ayette (1022).

### Aday 1041 — kayıt (test korpus sonunda)
يدي 48:10 'yedu'llâhi fevqa eydîhim' (aynı ayette Allah ve insan) → 48:20, 48:24 insan elleri · 'azîz' 48:3 yardımın sıfatı / 48:7, 48:19 Allah · ملك 48:11 'yemliku' / 48:14 'mulk' · غفر 48:11 'istağfir' / 48:14 'yağfiru' · قدر 48:21 'lem taqdirû' / 'qadîr' (aynı ayet, kök) · شهد 48:8 'şâhid' elçi / 48:28 'şehîd' Allah (kök) · رحم 48:14 'rahîm' Allah / 48:29 'ruhamâ'' insanlar.

### Aday 1040 — sınır kaydı (test korpus sonunda)
47:38 → 48:1 (2MP → 2MS, fâsıla م → ا) · 47:19 → 48:2 (istiğfar / bağışlama, 'zenb') · 47:7 → 48:3 ('yensurkum' / 'yensurake') · 47:19 → 48:5 ('mu'minîne ve'l-mu'minât') · 47:38 → 48:16 ('in tetevellev') · 9:39'un iki parçası 47:38 / 48:16 · 47:2 / 48:29 'Muhammed' · 47:30 / 48:29 'sîmâ' · 47:28 'ridvân' → 48:18, 48:29. 48:29 → 49:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
29 ayetin hepsinde not yazıldı. Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1022 esmâ: ölçüm MÜHÜRSÜZ / esma_kayit EVET — 48:11, 21, 24, 26, 28 (geçerli) ve 48:18, 20, 22, 27 (yanlış); 48:1, 3 sıfat.
* 517 biçim: tekit 'innâ' / 'fe-innâ', takdim 'li'llâhi …', zemm 'sâ'et', hasr 'innemâ', soru 'fe-men', teşbih ('kemâ', 'ke-'), üçlü tekrar (48:17) ölçümde işaretsiz.
* 1017 konuşan / gönderge: muhatap 2MS adsız (48:1-3, 8, 10, 11, 15, 23, 29); 48:12 süsleyen adsız; 48:16 topluluk adsız; 48:9 zamir göndergesi; 48:25 1P 'le-azzebnâ' ölçümde iltifât 0, cevabı düşmüş 'lev lâ'.
* 924 araç: 48:25 ölçüm IMPV 1 — metinde emir yok; ◈B tetik listesi dışı beden / bitki sözcükleri (48:17 a'mâ, a'rec, merîd; 48:27 ru'ûs; 48:29 vucûh, zer', sûq) — satır '—', gözlem ◇'de.
* Yıldız formülü: kısa ayette lafız oranı (48:3, 48:7 ★★★) ve uzun ayette n (48:29 ★★★) — bilinen davranış.

### Okumada görülenler (KAPATILAMAZ; defter bağı olanlar AS_fetih'te)
* Sekîne sûre içi üç ayet (4 'fî qulûb', 18 'aleyhim', 26 'alâ rasûlihî ve ale'l-mu'minîn'); 48:26 inkâr edenlerin kalbine 'hamiyye'.
* 'feth' 48:1 'mubîn', 48:18 ve 48:27 'qarîb'; biat 48:10 / 48:18; 48:11 'mâ leyse fî qulûbihim' / 48:18 'alime mâ fî qulûbihim'.
* Geri bırakılan bedevîler bölümü 48:11-17; ganimet dizisi 15, 19, 20, 21; eller 10, 20, 24 (tek yön → ayna).
* 9:111 → 48:10 ('evfâ', ''ahd', 'bâya'a'); 24:61 → 48:17 (aynı üçlü, farklı bağlam); 33:62, 35:43 → 48:23; 12:99 → 48:27; 9:33 → 48:28 (aynı cümle, farklı kapanış); 39:21 → 48:29 (ekin: büyüme → çöküş / yalnız büyüme).

## SÛRE 49 TUR SONU (2026-10-16)

**Okunan: 3422 / 6236 ayet (%54,9)** — sûre 1 ve 9-49 TAM, sûre 2 kısmi (1-20). İlerleme `hucurat_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1372** (`kok_ekle_49.py`: محن نبز لقب جسس شعب ليت). Aday havuzu **1041** (sûre 49'da yeni aday yok; `AX_hucurat` boş). Bağ **AS_hucurat** 55. Esmâ okuyucu kararı (KARAR) **430**.
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik iki blokta ilk koşuda 0 (ön kuru koşu ile) · [x/y] **196 sayım (97 + 99), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması 0 · DUZELTME 0.
Sûrenin 18 ayeti 2 blokta okundu (son blok 11-18, 8 ayet); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure49_hucurat_okuma.md` (`hucurat_paket_md.py`, 18 başlık). Fark zip'i cf56af3 tabanı (sûre 47, 48, 49 birlikte; uzak depo hâlâ cf56af3).

### Sûre 49 bilançosu (TAM SAYIM, `okuma_metni['49']['_bilanco_sure']`)
347 kelime · lafız **27 token / 14 ayet** · Rab 0 · edilgen 1 ayet (10) · iltifât 0 · hapaks ayet 3 (11 ×2 kök, 12, 14).
Yıldız 0:5 · ★6 · ★★★7 (hapaks 3: 11, 12, 14 · allah 4: 1, 8, 16, 18). Kaynak (1001 düzeltmeli): allah 6, hapaks 3, n 2, pas 1, kafiye 1 (49:13).
Fâsıla N 17 · 49:13 ر **kafiye kırılması**. En uzun 49:11 (39), en kısa 49:8 (7).

### Çıpa (ölçüt değişmedi)
L4 yok. 49:13 L1 (iki kaynaktan yaratma + halk / kabile + 'li-te'ârafû'; L2'ye sınırda, toplumsal sınıflama), 49:16 ve 49:18 L0. 49:12 temsil, olgu değil. Tarayıcı v4 adayları 2 (12, 13), kesinlik **0/2**.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
18 e_oto tokeni → ilâhî 14 · değil 4. §4.3 mühür 8 → geçerli 8 (1, 5, 8, 12, 13, 14, 16, 18); yanlış 0. Geçerli mühür tonu: denge 5, cemâl 3. 49:16, 49:18 ölçüm MÜHÜRSÜZ / esma_kayit EVET (1022).

### Aday 1041 — kayıt (test korpus sonunda)
يدي 49:1 'yedeyi'llâh' (48:10'a ek) · سخر 9:79 'sehira'llâhu minhum' / 49:11 · منن 49:17 'lâ temunnû' / 'bel Allâhu yemunnu' (aynı ayet) · علم 49:16 'tu'allimûna'llâh' / 12:37 'allemenî rabbî'.

### Aday 1040 — sınır kaydı (test korpus sonunda)
48:29 → 49:1 (ا → م; 'rasûlu'llâh' / 'yedeyi'llâhi ve rasûlih') · 48:29 → 49:3 (mağfira + ecr azîm) · 48:12 → 49:7 ('zeyyene … fî qulûbikum') · 47 'ahbata' → 49:2 'habita' · 48:6/12 → 49:12 'zann' · 48:11 → 49:14 (a'râb) · 48:24 → 49:18 ('bimâ ta'melûne basîr'). 49:18 → 50:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
18 ayetin hepsinde not yazıldı. Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1021 gloss: قبل 'ön, önce; kabul' — 49:13 'qabâ'il' (kabile) kapsanmıyor. سخر 'boyun eğdirme' — 49:11 'sehira' (alay etme) kapsanmıyor.
* 1001: 49:13 ★ kafiye kırığından, bilanço 'allah' etiketliyor.
* 924: 49:1 harf 90 → harf3 61 (besmele harf sayımına katılıyor olabilir; n=15 katmıyor).
* 517 biçim: tekit 'inne' / 'innâ', teşbih 'ke-cehri', 'lâkinne' / 'lâkin', takdim 'fîkum', hasr 'innemâ' (49:10, 15), zemm 'bi'se', 'lemmâ' ölçümde işaretsiz.
* 1017: nidâ ayetlerinde konuşan adlanmıyor; 2MS muhatap adsız ('qul'); 49:13 1P → 3MS ayet içi, ölçüm iltifât 0; 49:17 1S 'aleyye' alıntıda.

### Okumada görülenler (KAPATILAMAZ; defter bağı olanlar AS_hucurat'ta)
* Nidâ 'yâ eyyuhe'llezîne âmenû' (1, 2, 6, 11, 12) → 'yâ eyyuhe'n-nâs' (13).
* Ses 49:2 yükseltme / 49:3 kısma (31:19); 'fî qulûbikum' 49:7 süslendi / 49:14 henüz girmedi; 'îmân / fusûq' 49:7, 49:11.
* 'ulâ'ike hum' + sıfat 49:7, 11, 15; 'innema'l-mu'minûn' 49:10, 15 (24:62); 38:22 'beğâ … alâ' → 49:9; 35:12 'ekele lahm' → 49:12 (temsil); 26:22, 14:11 'menne + alâ' → 49:17.

## SÛRE 50 TUR SONU (2026-10-16)

**Okunan: 3467 / 6236 ayet (%55,6)** — sûre 1 ve 9-50 TAM, sûre 2 kısmi (1-20). İlerleme `qaf_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1375** (`kok_ekle_50.py`: بسق لفظ حيد). Aday havuzu **1041** (sûre 50'de yeni aday yok; `AX_qaf` boş). Bağ **AS_qaf** 91. Esmâ okuyucu kararı (KARAR) **441**.
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik beş blokta ilk koşuda 0 (ön kuru koşu ile) · [x/y] **236 sayım (56 + 50 + 48 + 56 + 26), 0 uyuşmaz** · e_el=? her blokta karar sonrası 0 · retroaktif gloss yaması 0 · DUZELTME 0.
Sûrenin 45 ayeti 5 blokta okundu (son blok 41-45, 5 ayet); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure50_qaf_okuma.md` (`qaf_paket_md.py`, 45 başlık). Fark zip'i **279460e** tabanı (uzak depo 279460e; sûre 47-49 orada). Ara zip 50:1-30'da verildi.

### Sûre 50 bilançosu (TAM SAYIM, `okuma_metni['50']['_bilanco_sure']`)
373 kelime · lafız **1 token / 1 ayet** (50:26) · Rab 2 (50:27, 39) · edilgen 5 ayet (3, 20, 29, 31, 32) · iltifât 6 ayet (3, 22, 24, 32, 33, 43) · hapaks ayet 3 (10, 18, 19).
Yıldız 0:30 · ★7 · ★★1 · ★★★7 (hapaks 3: 10, 18, 19 · pas 4: 20, 29, 31, 32). Kaynak (1001 düzeltmeli): kafiye 6, pas 5, hapaks 3, rab 1.
Fâsıla د 27 · ب 7 · ج 5 · ظ 2 · R 2 · ط 1 · ص 1; kafiye kırılması 6 ayet (2, 11, 13, 25, 36, 40). En uzun 50:36 (15), en kısa 50:1 (3).

### Çıpa (ölçüt değişmedi)
L4 yok. L2: 50:9 (su → bahçeler; 'bihî'), 50:11 (su → ölü belde diriliyor; 'kezâlike'l-hurûc'). L1: 50:4, 6, 7, 10, 38 (50:38 'fî sitteti eyyâm' sayı + birim, L4 ölçü koluna sınırda; 41:10 ile tutarlı). L0: 50:16, 19, 39, 40. Olgu değil: 50:3, 15, 20, 22, 44. Tarayıcı v4 adayı 1 (50:6), kesinlik **0/1**.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
11 e_oto tokeni → ilâhî 1 (50:33 'er-Rahmân') · değil 10. §4.3 mühür 9 → geçerli **0**; yanlış 9 (1, 4, 18, 21, 32, 34, 37, 41, 45) — adlar kitap, Kur'ân, kul, tanık, gözetleyici, yer, muhatap için. Lafız 1, Rab 2.

### Aday 1041 — kayıt (test korpus sonunda)
مجد 11:73 / 50:1 · حفظ 42:6, 34:21 / 50:4, 50:32 · رقب 4:1, 5:117, 33:52 / 11:93 / 50:18 · عيي 46:33 / 50:15 · ظلم 22:10, 41:46 (3. şahıs) / 50:29 (1S) · لغب 35:35 / 50:38 · جبر 11:59, 14:15, 19:32, 26:130, 40:35 / 50:45.

### Aday 1040 — sınır kaydı (test korpus sonunda)
49:18 → 50:1 (ن → د; 'basîrun bimâ ta'melûn' → harf + yemin QASEM). 50:45 → 51:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
45 ayetin hepsinde not yazıldı. Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1021 gloss: طلع 'doğma (güneş)' — 50:10 'tal'' (tomurcuk); حبب 'sevgi' — 50:9 'habb' (tane); حدد 'demir; sınır koyma' — 50:22 'hadîd' (keskin).
* 1001: altı kafiye kırığında ★ kaynağı kırık, bilanço 'allah' (50:2, 11, 36) / 'n' (50:13, 25, 40) etiketliyor.
* 924: 50:3 'mitnâ' EDİLGEN + iltifât 1 etiketli (okumada etken); fâsıla ر (50:43-44) ayrı sınıf, kırık işaretlenmedi.
* 517 biçim: tekit 'innâ', teşbih 'kezâlike', 1S 'ledeyye' → 1P 'ledeynâ' / 'neqûlu' geçişleri, 50:2 cevapsız yemin ardından 'bel' ölçümde işaretsiz.
* 1017: konuşan 1P / gizli 1S hiçbir ayette adlanmıyor; 2MS muhatap, uyarıcı, iki alıcı, gözetleyici, sürücü, tanık, qarîn, ikil emrin muhatapları, çağıran adsız.
* 1022: ölçüm MÜHÜRSÜZ / esma_kayit EVET dokuz ayet — hepsi okuyucu kararıyla 'değil'.

### Okumada görülenler (KAPATILAMAZ; defter bağı olanlar AS_qaf'ta)
* Çerçeve: 50:1 Kur'ân yemini → 50:45 'fe-zekkir bi'l-Qur'ân'; 50:3 'rec'un ba'îd' → 50:44 'haşrun aleynâ yesîr'; 50:4 yer eksiltiyor → 50:44 yer yarılıyor.
* Üç 'bel' (2, 5, 15); 'zâlike yevmu X' üç kez (20, 34, 42); 'vaîd' 14, 20, 28, 45 (korpustaki 6 ayetin 4'ü); 'qâle qarînuhû' 23 / 27; 'mezîd' 30 / 35.
* Emsaller: 38:1, 38:4 (açılış), 15:19 (50:7, esit2), 43:11 (50:11), 22:42-43 ve 38:12-14 (kavim sayımı 5 / 6 / 8 ad), 13:5 (50:3 + 15), 17:39 (50:24 + 26), 25:59, 32:4 (50:38), 20:130 (50:39-40).

## SÛRE 51 TUR SONU (2026-10-18)

**Okunan: 3527 / 6236 ayet (%56,6)** — sûre 1 ve 9-51 TAM, sûre 2 kısmi (1-20). İlerleme `zariyat_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1381** (`kok_ekle_51.py`: حبك سهو هجع صكك فرش متن). Aday havuzu **1041** (sûre 51'de yeni aday yok; `AX_zariyat` boş). Bağ **AS_zariyat** 67. Esmâ okuyucu kararı (KARAR) **453**.
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik altı blokta ilk koşuda 0 (ön kuru koşu ile; tetik 2 + 5 + 3 + 0 + 5 + 2) · [x/y] **221 sayım (18 + 34 + 46 + 40 + 43 + 40), 0 uyuşmaz** · e_el=? her blokta karar sonrası 0 · retroaktif gloss yaması 0 · DUZELTME 0.
Sûrenin 60 ayeti 6 blokta okundu; ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure51_zariyat_okuma.md` (`zariyat_paket_md.py`, 60 başlık). Uzak depo **0dc5351** (sûre 50 zip'i yüklendi, 31/31 dosya birebir); sûre 51 fark zip'i 0dc5351 tabanı. Ara zip 51:1-30'da verildi (279460e tabanı).

### Sûre 51 bilançosu (TAM SAYIM, `okuma_metni['51']['_bilanco_sure']`)
360 kelime · lafız **3 token / 3 ayet** (51:50, 51, 58; 51:1-49'da lafız yok) · Rab 5 (51:16, 23, 30, 34, 44) · edilgen 8 ayet (5, 9, 10, 13, 22, 32, 43, 60) · iltifât 4 ayet (9, 21, 34, 35) · hapaks ayet 3 (7, 17, 29).
Yıldız 0:41 · ★2 (8, 50) · ★★8 (16, 23, 30, 32, 43, 44, 58, 60) · ★★★9 (pas 5: 5, 9, 10, 13, 22 · hapaks 3: 7, 17, 29 · rab 1: 34). Kaynak (1001 düzeltmeli): pas 8, rab 5, hapaks 3, allah 2, kafiye 1.
Fâsıla N 51 · A 4 (51:1-4) · ك 2 · ق 1 · ع 1 · ف 1; kafiye kırılması 1 ayet (8). En uzun 51:52 (13), en kısa 2 kelime (51:1, 2, 3, 4, 10).

### Çıpa (ölçüt değişmedi)
L4 yok, L2 yok. L1: 51:7, 29, 47, 48, 49 (51:47 'le-mûsi'ûn' iki okumalı — süreç okuması KAPATILAMAZ, L4 değil; 51:49 36:36 / 43:12 emsali). L0: 51:17, 20, 21, 22. Olgu değil: 51:1, 33, 41, 56. Tarayıcı v4 adayı 2 (51:49, 51:56), kesinlik **0/2**.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
12 e_oto tokeni → ilâhî 4 (51:30 'el-hakîm', 'el-alîm'; 51:58 'er-razzâq', 'el-metîn') · değil 8. §4.3 mühür 9 → geçerli **2** (51:30, 51:58; ton denge 1, karma 1); yanlış 7 (25, 28, 35, 38, 50, 51, 55) — adlar selâm sözü, oğul, inananlar, delil, uyarıcı için. Lafız 3, Rab 5.

### Aday 1041 — kayıt (test korpus sonunda)
علم 51:28 'ğulâmin alîm' / 51:30 'el-hakîmu'l-alîm' · قوي 27:33, 28:76 'ulû / uli'l-quvve' / 51:58 'zu'l-quvve'. (1041 dışı kayıt: عقم 51:29 kadın / 51:41 rüzgâr.)

### Aday 1040 — kayıt (test korpus sonunda)
50:6 → 51:47 'beneynâhâ' (gök) · 50:7 → 51:48 'medednâhâ' / 'feraşnâhâ' (yer) · 50:45 → 51:54-55 'mâ ente … bi-cebbâr / bi-melûm' + 'zekkir'. 51:60 → 52:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
60 ayetin hepsinde not yazıldı. Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1021 gloss: ذرو gloss'una 'rüzgâr' eklendi (51:1); ذنب 'günah, suç' — 51:59 'zenûb' (pay) okumasını kapsamıyor; وسع 51:47 iki anlamlı.
* 1001: 51:8 kafiye kırığında ★ kaynağı kırık, bilanço 'n' etiketliyor.
* 517 biçim: tekit 'inne / innâ', teşbih 'ke-', övgü 'ni'me', fasl zamiri 'huve' ölçümde işaretsiz.
* 1017: konuşan 1P hiçbir ayette adlanmıyor; 1S iki göndergeli (51:50-51 uyarıcı, 51:56-59 yaratan; ölçüm iltifât 0); 2MS muhatap, edilgen söyleyen (51:43), gönderen (51:32), vaat eden (51:60) adsız.
* 1022: ölçüm MÜHÜRSÜZ / esma_kayit EVET dokuz ayet — yedisi 'değil', ikisi (51:30, 58) 'ilâhî'.

### Okumada görülenler (KAPATILAMAZ; defter bağı olanlar AS_zariyat'ta)
* Çerçeve: 51:5 'tû'adûn' → 51:22 → 51:60 'yû'adûn' (2MP → 3MP); sûre vaatle açılıp kapanıyor.
* 've fî' dizisi: 51:20 yer, 21 enfus, 22 gök → 38 Mûsâ, 41 Âd, 43 Semûd, 46 Nûh kavmi.
* رزق 51:22 → 57 → 58 'er-razzâq'; nakarat3 sûre içi 51:39 ↔ 52, 51:50 ↔ 51; esit2 51:31-32 ↔ 15:57-58 TAM; ولي / لوم 51:39-40 Firavun → 51:54 muhatap (zıt yön).
* Emsaller: 15:51, 52, 53, 57, 58, 62, 74 ve 11:69, 70, 71, 72, 82, 83 (İbrâhîm misafirleri; tek tek okundu), 11:65, 41:17, 11:67 (Semûd), 36:78 (ramîm), 17:22, 17:39 (51:51 + 54), 37:30, 37:174, 21:37, 43:83.

## SÛRE 52 TUR SONU (2026-10-18)

**Okunan: 3576 / 6236 ayet (%57,3)** — sûre 1 ve 9-52 TAM, sûre 2 kısmi (1-20). İlerleme `tur_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1385** (`kok_ekle_52.py`: رقق ألت رهن كهن). Aday havuzu **1041** (sûre 52'de yeni aday yok; `AX_tur` boş). Bağ **AS_tur** 109. Esmâ okuyucu kararı (KARAR) **457**.
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik beş blokta ilk koşuda 0 (ön kuru koşu ile; tetik satırı 5 + 4 + 0 + 4 + 6) · [x/y] **191 sayım (20 + 39 + 54 + 34 + 44), son durumda 0 uyuşmaz** (41-49'da ilk koşuda 1 — 52:41 عند başka ayetin sayısı [x/y] biçiminde; kayıttan önce düzeltildi) · e_el=? her blokta karar sonrası 0 · retroaktif gloss yaması 0 · **DUZELTME 1** (52:11 — 16:36, 43:25 metin basılmadan 'okunan' diye anılmıştı; sûre sonunda basıldı, anma doğru; özgün alan korunur).
Sûrenin 49 ayeti 5 blokta okundu; ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure52_tur_okuma.md` (`tur_paket_md.py`, 49 başlık). Uzak depo **95f7b81** (oturum boyunca ilerlemedi); fark zip'i 95f7b81 tabanı. Ara zip 52:1-30'da verildi (aynı taban).

### Sûre 52 bilançosu (TAM SAYIM, `okuma_metni['52']['_bilanco_sure']`)
312 kelime · lafız **3 token / 2 ayet** (52:27; 52:43 ×2; 52:1-26'da lafız yok) · Rab 7 token / 5 ayet (52:7, 18, 29, 37, 48) · edilgen 5 ayet (13, 16, 35, 45, 46) · iltifât 7 ayet (8, 19, 20, 29, 30, 32, 48) · hapaks ayet 2 (3, 21).
Yıldız 0:34 · ★3 (5, 6, 45) · ★★4 (27, 29, 37, 46) · ★★★8 (rab 3: 7, 18, 48 · hapaks 2: 3, 21 · pas 2: 13, 35 · allah 1: 43). Kaynak (1001 düzeltmeli): rab 5, pas 4, hapaks 2, allah 2, kafiye 2 (52:5, 6 etiketi 'n').
Fâsıla R 5 (52:1-4, 6) · ع 3 (5, 7, 8) · A 3 (9, 10, 13) · N 38; kafiye kırılması ölçümde 3 ayet (5, 6, 13). En uzun 52:21 (19), en kısa 52:1 (1).

### Çıpa (ölçüt değişmedi)
L4 yok, L3 yok, L2 yok. L1: 52:5, 6, 9, 10, 44 (52:44 algı / durum ayrımı var, karşılaştırma yok — L3 koluna sınırda, 46:24 emsali, KAPATILAMAZ). L0: 52:36, 49. Olgu değil: 52:1, 35. Tarayıcı v4 adayı 1 (52:44), kesinlik **0/1**.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
4 e_oto tokeni → ilâhî 2 (52:28 'el-berr', 'er-rahîm') · değil 2 (52:35 'el-hâliqûn' — özne insanlar, soru; 52:38 'mubîn' — delil). §4.3 mühür 3 → geçerli **1** (52:28; ton cemâl, çift); yanlış 2 (35, 38). Lafız 3, Rab 7.

### Aday 1041 — kayıt (test korpus sonunda)
'berr' 19:14, 19:32 (insan) / 52:28 (Allah) · 'hâliq' 13:16, 15:28, 23:14, 37:125 (Allah) / 52:35 (insanlar, soru içinde) · kök düzeyi: وقي 52:17 'muttaqîn' / 52:18 'veqâhum rabbuhum'; كيد 12:76 'kidnâ' / 52:42 'keyd'.

### Aday 1040 — kayıt (test korpus sonunda)
51:60 → 52:1 (fâsıla ن → ر) · 51:1 → 52:1 (iki sûre 've' yeminiyle açılıyor) · 51:6 → 52:7 ('inne + ism + le-vâqi'') · 51:60 → 52:11 ('fe-veylun') · 51:13, 14, 15, 16 → 52:13, 14, 17, 18 sıralı — 'mâ âtâhum rabbuhum' lemma dizisi korpusta yalnız 51:16 ve 52:18 · 51:28 → 52:24 (ğulâm / ğilmân) · 51:52, 55 → 52:29 · 51:53 → 52:32 — 'qavm tâğî' lemma dizisi korpusta yalnız 51:53 ve 52:32 · 51:44 → 52:45 (صعق). 52:49 → 53:1 henüz okunmadı.
1040 alanı dışı (ardışık değil): 50:39-40 → 52:48-49 iki ayet sırasıyla (esit2 52:49 → 50:40 BENZER).

### Aday 1039 — okuma kolu (karşıt çift) verisi
49 ayetin hepsinde not yazıldı. Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1021 gloss: رقق tek geçiş (korpus içinden doğrulanamaz); سجر 52:6 iki okumalı; kapsanmayan anlamlar: سرر 'surur', منن 'menûn', سطر 'musaytirûn', بني 'benât / benûn', فكه 'fâkihîn'; حلم 'ahlâm' seçimi KAPATILAMAZ.
* 1001: 52:5, 6 ★ kafiye kırığından, bilanço 'n' etiketliyor; 52:6 R sınıfında kırık işaretli, 52:9 ر/ع → ا geçişinde işaret yok (924).
* 517 biçim: yemin 've' (52:1-6), 'em' dizisi (12 ayet), tekit, fasl zamiri, teşbih 'ke-enne', tenzih 'subhâna', istidrâk 'lâkinne' ölçümde işaretsiz.
* 1017: yemin eden ve 1P anlatıcı adlanmıyor; muhatap 2MS adsız; edilgen failler adsız; alıntı sınırları (52:14-16, 19, 26-28, 30) işaretsiz; 'teqavvelehû', 'mislihî', 'lehu' göndergeleri adsız.
* 1022: ölçüm ile esma_kayit üç ayette ayrıştı (52:28 MÜHÜR, 52:35 ve 52:38 MÜHÜRSÜZ / esma_kayit EVET).

### Okumada görülenler (KAPATILAMAZ; defter bağı olanlar AS_tur'da)
* Mef'ûl-i mutlak kuruluşu: 52:9 مور, 52:10 سير, 52:13 دعع.
* 'em' soru dizisi 52:30-43'te 12 ayette (52:30, 32, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43); 52:43 tenzihle kapanıyor.
* 43:83 'fe-zerhum yehûdû ve yel'abû hattâ yulâqû yevmehumu'llezî' sûrenin iki ucuna dağılıyor (52:12, 52:45).
* Aynı kök iki anlam: سطر 52:2 / 37 · منن 52:27 / 30 · جنن 52:17 / 29 · قبل 52:25 / 26 · فكه 52:18 / 22 · عين 52:20 / 48.
* 23:25 'bihî cinnetun fe-terabbasû bihî' → 52:29-30 'mecnûn' + 'neterabbasu bihî' iki ayete dağılmış; 10:38, 11:13 iddia + meydan okuma bir ayette → 52:33-34 iki ayette; 37:156-157 iki ayet → 52:38 bir ayette.
* Sûre 've't-Tûr' ile açılıp 'idbâra'n-nucûm' ile kapanıyor.
* Emsaller (tek tek okundu): 19:52, 20:80, 23:20, 28:29, 28:46, 17:58, 33:6, 17:13, 21:32, 16:26, 43:33, 40:72, 17:57, 21:46, 42:22, 51:6, 13:31, 18:47, 34:18, 9:65, 43:83, 51:13, 51:14, 32:20, 34:42, 37:21, 15:15, 21:3, 27:13, 36:9, 36:64, 14:21, 45:28, 15:45, 51:15, 51:16, 36:55, 44:27, 40:7, 44:56, 44:54, 15:47, 37:44, 43:34, 29:12, 47:3, 13:23, 40:8, 37:49, 51:28, 37:27, 37:50, 18:49, 21:28, 23:57, 12:90, 28:82, 15:27, 28:53, 19:14, 19:32, 17:67, 51:52, 51:55, 23:25, 37:36, 51:53, 37:30, 10:38, 11:13, 37:157, 17:88, 13:16, 23:14, 37:125, 38:9, 17:100, 37:156, 37:149, 16:57, 43:16, 36:21, 9:98, 21:70, 37:98, 12:76, 28:68, 28:71, 17:92, 26:187, 34:9, 24:43, 30:48, 39:68, 51:44, 44:41, 21:39, 32:21, 10:55, 44:39, 11:37, 23:27, 50:39, 50:40.

## SÛRE 53 NECM SONU (2026-10-18)

**Okunan: 3638 / 6236 ayet (%58,3)** — sûre 1 ve 9-53 TAM, sûre 2 kısmi (1-20). İlerleme `necm_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1391** (`kok_ekle_53.py`: قوب قوس ضيز لمم كدي قني). Aday havuzu **1041** (sûre 53'te yeni aday yok; `AX_necm` boş). Bağ **AS_necm** 89. Esmâ okuyucu kararı (KARAR) **463**.
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik altı blokta kayıtta 0 (ön kuru koşu ile; tetik satırı 1 + 1 + 5 + 3 + 3 + 0) · [x/y] **124 sayım (23 + 28 + 23 + 23 + 15 + 12), 0 uyuşmaz** · e_el=? her blokta karar sonrası 0 · retroaktif gloss yaması 0 · DUZELTME 0 (53:36 notundaki okunmamış 53:41'i kapsayan aralık kayıttan sonra yakalandı; not düzeltilip blok yeniden kaydedildi).
Sûrenin 62 ayeti 6 blokta okundu; ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure53_necm_okuma.md` (`necm_paket_md.py`, 62 başlık). Uzak depo **95f7b81** (oturum boyunca ilerlemedi); fark zip'i 95f7b81 tabanı — sûre 52 ve 53'ü birlikte taşır. Ara zip 53:1-30'da verildi (aynı taban).

### Sûre 53 bilançosu (TAM SAYIM, `okuma_metni['53']['_bilanco_sure']`)
360 kelime · lafız **6 token / 6 ayet** (53:23, 25, 26, 31, 58, 62; 53:1-22'de lafız yok) · Rab 7 token / 7 ayet (53:18, 23, 30, 32, 42, 49, 55; ilk Rab 53:18) · edilgen ölçümde 6 ayet (4, 12, 36, 40, 41, 46 — 53:12 araç arızası) · iltifât 6 ayet (19, 42, 43, 55, 57, 59) · hapaks ayet 5 (9, 22, 34, 48, 61).
Yıldız 0:34 · ★10 (3, 11, 15, 19, 20, 21, 26, 32, 33, 37) · ★★2 (12 pas-arıza, 58 allah) · ★★★16 (pas 5: 4, 36, 40, 41, 46 · hapaks 5: 9, 22, 34, 48, 61 · rab 4: 18, 42, 49, 55 · allah 2: 25, 62). Kaynak (1001 düzeltmeli): kafiye 9, pas 6, hapaks 5, rab 4, allah 3, n 1.
Fâsıla A 44 · 'ٓ' 13 (medd işareti fâsıla okunuyor — araç artefaktı) · H 2 (57, 58) · N 3 (59-61); kafiye kırılması ölçümde 12 ayet (3, 11, 15, 18, 19, 20, 21, 26, 32, 33, 36, 37) — hepsi 'ٓ' artefaktından ya da ona bağlı geçişten; 53:57'deki gerçek sınıf geçişi işaretsiz. En uzun 53:32 (31), en kısa 53:53, 57, 61 (2).

### Çıpa (ölçüt değişmedi)
L4 yok, L3 yok, L2 yok. L1: 53:1, 7, 32, 45, 46. L0: 53:26, 31, 44, 49. Olgu değil: 53:9 (mesafe birimi), 53:14 (ağaç adı yer izâfetinde). Tarayıcı v4 adayı 1 (53:31), kesinlik **0/1**.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
6 e_oto tokeni → ilâhî 1 (53:32 'vâsi'' — Rab'bin yüklemi) · değil 5 (53:25 'âhir', 'evvel'; 53:27 'âhir'; 53:50 'evvel'; 53:56 'evvel'). §4.3 mühür 3 (25, 50, 56) → geçerli **0**. Lafız 6, Rab 7.

### Aday 1041 — kayıt (test korpus sonunda)
lemma 'istevâ' 20:5 Rahmân / 28:14 insan / 48:29 ekin, 53:6'da özne adsız · kök düzeyi: عزز 38:9 'el-azîz' (Rab) / 53:19 'el-Uzzâ' (put adı); غفر 42:37 'hum yağfirûn' (insan) / 53:32 'vâsi'u'l-mağfira' (Rab) — aynı 'kebâ'ira'l-ismi ve'l-fevâhiş' dizisinin ardından.

### Aday 1040 — kayıt (test korpus sonunda)
52:49 → 53:1 (fâsıla م → ى; 'nucûm' / 'necm') · 51:1, 52:1, 53:1 ardışık üç sûre 've' yeminiyle açılıyor · 52:29 → 53:2 (olumsuzlama) · 52:39 → 53:21 (paylaştırma kuruluşu, sıra ters) · 52:41 → 53:35 ('inde + ğayb + fe- + zamir + IMPF') · 52:34 → 53:59 ('hadîs'). 53:62 → 54:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
62 ayetin hepsinde not yazıldı. Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1021 gloss: مني sayacı 'Menât' / 'temennâ' / 'tumnâ'; شعر 'Şi'râ', عود 'Âd' kapsanmıyor; ذكر 'zeker' / 'zikr' tek sayaç; lemma 'Âd' 'âd' (aşan) kelimesini de sayıyor; سمد iki okumalı (meal seçimi KAPATILAMAZ); فأد ve 'ecinne' ◈B tetik listesinde değil (gözlem ◇'de).
* 1001: dokuz ★ kafiye kırığından, bilanço 'n' etiketliyor.
* 924: 53:12 'tumârûnehû' PASS etiketi (III. bab etken); 'ٓ' fâsıla artefaktı; 53:22 'biçim QASEM' (قسم paylaştırma anlamında); 53:49 'Şi'râ' 'sahte-ilah, rol fail' (metinde izâfet).
* 517 biçim: takdim, 'huwa / hum' ayırma zamiri, 'em' sorusu, 'leyse' olumsuzluğu, ayet içi şahıs geçişleri (53:23, 32) ölçümde işaretsiz.
* 1017: gören, görülen, öğreten, örten, edilgen failler, muhataplar adsız; 53:53 'el-mu'tefike' adsız — meal ad eklemedi.

### Okumada görülenler (KAPATILAMAZ; defter bağı olanlar AS_necm'de)
* Görme zinciri رأي 8 geçiş: 53:11, 12, 13, 18 (gören 3MS) → 53:19 (2MP) → 53:33 (2MS) → 53:35 'yerâ' → 53:40 edilgen 'yurâ'.
* 'Fiil + mâ + aynı fiil' üç kez: 53:10, 16, 54 (16 ve 54 aynı kök غشو); 20:78 aynı kuruluş.
* 've ennehû huwa' 4 ayet (53:43, 44, 48, 49) — korpusta yalnız bu sûrede.
* İki uçlu iplikler: هوي 53:1 → 3 → 23 → 53 · ذكر/أنث 53:21 → 45 · نهي 53:14 → 42 · نشأ 53:32 → 47 · غني 53:26, 28 → 48 · ضحك/بكي 53:43 → 60 · طغي 53:17 → 52 · مري 53:12 → 55 · عبد 53:10 → 62 · وفي 53:37 → 41.
* 9:70 Nûh kavmi, Âd, Semûd, 'mu'tefikât' bir ayette → 53:50-53 dört ayette.
* Sûre 've'n-necm' yeminiyle açılıp secde emriyle kapanıyor; 53:49 adlı yıldız.
* Emsaller (tek tek okundu): 52:49, 51:1, 52:1, 14:37, 20:81, 22:31, 34:46, 52:29, 20:121, 28:63, 36:69, 12:104, 38:87, 23:25, 11:37, 23:27, 51:58, 20:5, 41:11, 28:14, 48:29, 41:53, 20:38, 17:36, 28:10, 42:18, 32:19, 20:78, 33:10, 20:23, 26:75, 39:38, 38:9, 52:39, 12:40, 10:66, 28:70, 36:23, 20:109, 34:23, 37:150, 43:19, 10:36, 16:125, 42:37, 16:78, 39:6, 35:18, 19:77, 45:23, 52:41, 17:15, 39:7, 20:15, 9:82, 50:43, 51:49, 35:11, 29:20, 51:41, 51:43, 51:46, 9:70, 51:50, 40:18, 52:34, 50:2, 41:37.


## SÛRE 54 KAMER SONU (2026-10-18)

**Okunan: 3693 / 6236 ayet (%59,2)** — sûre 1 ve 9-54 TAM, sûre 2 kısmi (1-20). İlerleme `kamer_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1397** (`kok_ekle_54.py`: جرد همر لوح دسر قعر دهي). Aday havuzu **1041** (sûre 54'te yeni aday yok; `AX_kamer` boş). Bağ **AS_kamer** 90. Esmâ okuyucu kararı (KARAR) **468**.
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik altı blokta kayıtta 0 (ön kuru koşu ile; tetik satırı 4 + 7 + 1 + 1 + 4 + 1) · [x/y] **111 sayım (14 + 15 + 16 + 13 + 36 + 17), 0 uyuşmaz** · e_el=? her blokta karar sonrası 0 · retroaktif gloss yaması 0 · DUZELTME 0 (54:47 notundaki metne uymayan alıntı ifadesi kayıttan sonra yakalandı; not düzeltilip blok yeniden kaydedildi).
Sûrenin 55 ayeti 6 blokta okundu; ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure54_kamer_okuma.md` (`kamer_paket_md.py`, 55 başlık). Uzak depo **95f7b81** (oturum boyunca ilerlemedi); fark zip'i 95f7b81 tabanı — sûre 52, 53 ve 54'ü birlikte taşır. Ara zip 54:1-30'da verildi (aynı taban).

### Sûre 54 bilançosu (TAM SAYIM, `okuma_metni['54']['_bilanco_sure']`)
342 kelime · lafız **0** (sûrede Allah lafzı yok) · Rab 1 token / 1 ayet (54:10) · edilgen ölçümde 6 ayet (9, 12, 14, 25, 45, 48) · iltifât 7 ayet (23, 33, 39, 41, 43, 44, 52) · hapaks ayet 4 (11 همر, 13 دسر, 20 قعر, 46 دهي) · mm2 1 (42).
Yıldız 0:45 · ★2 (12, 14 pas) · ★★2 (45, 48 pas) · ★★★6 (hapaks 4: 11, 13, 20, 46 · rab 1: 10 · pas 1: 25). 1001 düzeltmesi etiket değiştirmedi.
Fâsıla 55 ayetin hepsinde ر (R sınıfı); kafiye kırığı yok, 'ٓ' artefaktı yok. En uzun 54:24 (10), en kısa 54:23, 39 (3).
Nakaratlar (hepsi korpusta yalnız bu sûrede): 'fe-keyfe kâne azâbî ve nuzur' 4 (16, 18, 21, 30) · 've leqad yessernâ'l-qur'âne li'z-zikri fe-hel min muddekir' 4 (17, 22, 32, 40) · 'fe-hel min muddekir' 6 (15, 17, 22, 32, 40, 51) · 'innâ erselnâ aleyhim' 3 (19, 31, 34) · 'fe-zûqû azâbî ve nuzur' 2 (37, 39).

### Çıpa (ölçüt değişmedi)
L4 yok, L3 yok, L2 yok. L1: 54:1, 7, 11, 12, 19, 20, 31, 49, 50 (54:12 ve 54:49'da ölçü yalnız kelime — L4 ölçü kolu KAPATILAMAZ). L0: 54:27, 34. Olgu değil: 54:13 (insan yapımı araç), 54:54 (cennet ırmağı). Tarayıcı v4 adayı yok, kesinlik **0/0**.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
5 e_oto tokeni → ilâhî 4 (54:42 'azîz', 'muqtedir'; 54:55 'melîk', 'muqtedir' — ikisi de nekre, sınır vakası) · değil 1 (54:53 'kebîr'). §4.3 mühür 3 (42, 53, 55) → geçerli **2** (42, 55; ÇİFT, ton celâl). Lafız 0, Rab 1.

### Aday 1041 — kayıt
Sûre 54'te kayıt yok.

### Aday 1040 — kayıt (test korpus sonunda)
fâsıla 53:62 ا → 54:1 ر · 53:57 'ezifeti'l-âzife' / 54:1 'iqterabeti's-sâ'a' · 53:23 / 54:3-4 · 53:56 / 54:5 · 53:29 / 54:6 · 53:52 / 54:9 · 53:50 / 54:18 · 53:50-53 helâk sırası → 54:9-42 kıssaları · 53:51 / 54:23 · 53:22 / 54:28 'qisme' · 53:55 / 54:36 'temârâ'. 54:55 → 55:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
55 ayetin hepsinde not yazıldı. Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1021 gloss: سحر 'sehar'ı, أول 'âl'i kapsamıyor; 'nâr' نور sayacında.
* 1017: 1P / 1S, muhataplar (54:6, 43, 51), çağıran, konuklar, edilgen failler adsız; 54:45 topluluğun metinde adı yok.
* 517: teşbih, alıntı sınırları ve 'inne' tekidi ölçümde işaretsiz.
* 924: kalıp sayımı imlâ farkıyla ayırıyor (54:42 / 20:56); 54:28 'biçim QASEM' (قسم paylaştırma anlamında, 53:22 ile aynı arıza).

## SÛRE 55 RAHMÂN SONU (2026-10-18)

**Okunan: 3771 / 6236 ayet (%60,5)** — sûre 1 ve 9-55 TAM, sûre 2 kısmi (1-20). İlerleme `rahman_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1408** (`kok_ekle_55.py`: أنم فني نفذ شوظ فنن طمث دهم نضخ خيم رفرف عبقر). Aday havuzu **1041** (sûre 55'te yeni aday yok; `AX_rahman` boş). Bağ **AS_rahman** 73. Esmâ okuyucu kararı (KARAR) **469**.
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik sekiz blokta kayıtta 0 (ön kuru koşu ile; tetik satırı 8 + 3 + 2 + 5 + 1 + 2 + 1 + 1 = 23) · [x/y] **286 sayım (26 + 35 + 43 + 46 + 35 + 38 + 30 + 33), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması 0 (55:1-10 sonrası ilk koşuda 1 genel yama, ikinci koşuda 0) · DUZELTME 0 (55:1 besmele ifadesi kayıttan sonra yakalandı; not düzeltilip blok yeniden kaydedildi).
Sûrenin 78 ayeti 8 blokta okundu; ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure55_rahman_okuma.md` (`rahman_paket_md.py`, 78 başlık). Uzak depo **95f7b81** (oturum boyunca ilerlemedi); fark zip'i 95f7b81 tabanı — sûre 52, 53, 54 ve 55'i birlikte taşır. Ara zip 55:1-30'da verildi (aynı taban).

### Sûre 55 bilançosu (TAM SAYIM, `okuma_metni['55']['_bilanco_sure']`)
351 kelime · lafız **0** (sûrede Allah lafzı yok) · Rab 36 token / 35 ayet (55:17'de iki) · edilgen ölçümde 3 ayet (35, 39, 41) · iltifât 42 ayet · hapaks ayet 9, kök 10 (10 أنم, 26 فني, 33 نفذ, 35 شوظ, 48 فنن, 64 دهم, 66 نضخ, 72 خيم, 76 رفرف + عبقر) · mm2 0.
Yıldız 0:32 · ★★★46 (rab 35 · hapaks 9 · pas 2: 39, 41). 1001 düzeltmesi etiket değiştirmedi.
Fâsıla N sınıfı 76 ayet (ن; 55:10, 11, 24, 27, 41, 72, 78 م), R 2 (55:14, 15 ر); kafiye kırığı yok. En uzun 55:33 (16), en kısa 55:1, 64 (1).
Nakarat 'fe-bi-eyyi âlâ'i rabbikumâ tukezzibân' **31** (55:13 → 55:77; korpusta yalnız bu sûrede). Sûre içi tam tekrarlar: 'lem yatmishunne insun qablehum ve lâ cânn' 2 (56, 74) · 'fîhimâ aynân' 2 (50, 66) · 'celâl' / 'ikrâm' 2 (27, 78). 2MS 'rabbike' yalnız 55:27 ve 55:78.

### Çıpa (ölçüt değişmedi)
L4 yok, L3 yok. L2: 55:33 (yeti sınırı; tarayıcı v4 adayı, çıpa değil). L1: 55:5, 6, 7, 10, 11, 12, 14, 17, 19, 20, 22, 37 (55:5 ölçü yalnız kelime — L4 ölçü kolu KAPATILAMAZ; 55:10, 20 L2 sınırı KAPATILAMAZ). L0: 55:3. Olgu değil: 55:15 (cânn), 55:24 (gemi), 55:48, 50, 52, 66, 68, 72, 74, 76 (cennet). Tarayıcı v4 adayı 1 (55:33), kesinlik **0/1**.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
1 e_oto tokeni → ilâhî 1 (55:1 'er-rahmân'). §4.3 mühür 1 → geçerli **1** (55:1, ton cemâl) — ölçüm satırında son konum 'MÜHÜRSÜZ'; tek kelimelik ayette ayrışma kayıtta, okumada mühür iddiası yazılmadı. 'zu'l-celâli ve'l-ikrâm' (55:27, 78) esmâ ölçümünde değil. Lafız 0, Rab 36.

### Aday 1041 — kayıt
Sûre 55'te kayıt yok.

### Aday 1040 — kayıt (test korpus sonunda)
fâsıla 54:55 ر → 55:1 ن · 54:55 'melîk muqtedir' / 55:1 'er-rahmân' · 54 'yessernâ'l-qur'ân' nakaratı / 55:2 · 54:1 / 55:5 'el-qamer' · 54:49 / 55:5, 7 · 53:1 / 55:6 · 54:20 / 55:11 · 54:12 / 55:19 · 54:12 / 55:50 · 54:10 / 55:35 · 54:1 / 55:37 · 53:55 / 55:13. 55:78 → 56:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
78 ayetin hepsinde not yazıldı. Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1021 gloss / lemma: 'hayrât' 'el-hayrât' ile aynı sayaçta; سمو 'ism' ile 'semâ'yı topluyor; 'husbân' 18:40 / 55:5 iki anlam.
* 1017: nakaratın 2D muhatabı mealde adsız (metin 55:31, 33'te adlıyor); öğrenen, 2MP muhatap, kadınlar, yaslananlar, suçlular adsız.
* 517: takdim ve mübteda hazfi ölçümde işaretsiz; 2D → 2MS sayı değişimi iltifât sayılmıyor (55:27, 78).
* 924: 55:1 mühür ölçütü / son konum ayrışması (tek kelimelik ayet).

## SÛRE 56 VÂQI'A SONU (2026-10-20)

**Okunan: 3867 / 6236 ayet (%62,0)** — sûre 1 ve 9-56 TAM, sûre 2 kısmi (1-20). İlerleme `vakia_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1414** (`kok_ekle_56.py`: رجج وضن خضد طلح سكب مزن). Aday havuzu **1041** (sûre 56'da yeni aday yok; `AX_vakia` boş). Bağ **AS_vakia** 168. Esmâ okuyucu kararı (KARAR) **483** (469 → 483; 13 DEĞİL, 1 İLÂHÎ).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 (56:41-50'de 72 ve 56:81-90'da 76 — kayıt metnine yazılan Arapça imlâ parçaları; Latin tarifle düzeltildi) · tetik on blokta kayıtta 0 (ön kuru koşu ile; tetik satırı 3 + 1 + 3 + 1 + 2 + 5 + 1 + 2 + 2 + 0 = 20) · [x/y] **240 sayım (21 + 22 + 24 + 19 + 30 + 24 + 28 + 30 + 25 + 17), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması 0 · **DUZELTME 4** (56:11, 28 — 1017, komşu ayetten taşınan ad; 56:62, 70 — 924, 'fe-levlâ' imlâ / lemma sayımı).
Sûrenin 96 ayeti 10 blokta okundu (9 × 10 + 6); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure56_vakia_okuma.md` (`vakia_paket_md.py`, 96 başlık). Uzak depo **dd30f51** (oturum boyunca ilerlemedi); fark zip'i dd30f51 tabanı. Ara zip 56:1-30 ve 56:1-60'ta verildi (aynı taban).

### Sûre 56 bilançosu (TAM SAYIM, `okuma_metni['56']['_bilanco_sure']`)
379 kelime · lafız **0** (sûrede Allah lafzı yok) · Rab 3 token / 3 ayet (56:74, 80, 96; 56:1-73 Rab'siz) · edilgen ölçümde 4 ayet (4, 5, 19, 47) · iltifât 15 ayet · hapaks ayet 7, kök 7 (4 رجج, 5 بسس, 15 وضن, 28 خضد, 29 طلح, 31 سكب, 69 مزن) · mm2 1 (56:35).
Yıldız 0:84 · ★1 (56:41, kafiye kırığından — bilanço 'n' etiketi, 1001) · ★★1 (56:19 pas) · ★★★10 (hapaks 5 · rab 3 · pas 2: 56:4, 5).
Fâsıla N 73 · H 10 (56:1-3, 7-9, 15, 32-34) · A 7 (56:4-6, 25-26, 36-37) · د 3 (56:28-30) · ب 56:31 · ء 56:35 · ل 56:41; kafiye kırığı ölçümde 56:15, 41. En uzun 56:47, 61 (9); 2 kelimelik 15 ayet.
Sûre içi tam tekrar: 'fe-sebbih bi'smi rabbike'l-azîm' 56:74 / 56:96 (esit2 TAM). 2MS yalnız 56:49, 74, 91, 96; 1S yalnız 56:75 (morph).

### Çıpa (ölçüt değişmedi)
L4 yok, L3 yok, L2 yok. L1: 56:4, 5, 6, 47, 58, 59, 60, 63, 64, 65, 68, 69, 70, 71, 72, 73, 75, 83 (56:60 ölçü kolu yalnız kelime — KAPATILAMAZ; 56:65 tek aşama, 39:21 L4'ten ayrı). L0: 56:57, 62. Olgu değil: 56:7 (insan sınıfları), 56:18-21, 28-32, 89 (cennet), 56:42, 43, 52, 93, 94 (cehennem). Tarayıcı v4 adayı 1 (56:7, sayı işareti), kesinlik **0/1**.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
14 e_oto tokeni → ilâhî 1 (56:59 'nahnu'l-hâliqûn', SINIR VAKASI), değil 13 ('evvel / âhir / ûlâ' insanlar ve neş'e; 'selâm' sözü ×3; 'kerîm' gölge ve Kur'ân sıfatı). §4.3 mühür 12 → geçerli **1** (56:59, ton denge) — ölçüm satırında son konum 'MÜHÜRSÜZ'; ayrışma kayıtta (51:58 emsali), okumada mühür iddiası yazılmadı. 'el-azîm' (56:46, 74, 96), 'munşi'', 'zâri'', 'munzil' esmâ ölçümünde değil. 1022: 56:13, 39, 48, 62 ölçüm satırında 'esmâ yok', esma_kayit e_oto.

### Aday 1041 — kayıt
56:59 خلق · 56:64 زرع · 56:69 نزل · 56:72 نشأ — aynı ayette insan (2MP soru) / 1P (yüklem), dört kez ('e-fe-ra'eytum' dörtlüsü). Test yok.

### Aday 1040 — kayıt (test korpus sonunda)
55:78 / 56:1 (Rab ve esmâ ile kapanan sûreden lafızsız, Rab'siz açılışa; fâsıla م → ة) · 55:7 / 56:3 · 55:37 / 56:4-6 · 55:52 / 56:7 · 55:60 / 56:24. 56:96 → 57:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
96 ayetin hepsinde not yazıldı. Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1017: adsız fâil / muhatap (56:51, 81 2MP; 56:83 3FS; 56:85, 88-92 3MS; 56:91 'leke' 2MS); DUZELTME 56:11 (26:42'de 'Firavun' yok), 56:28 (34:16'da 'Sebe'' yok).
* 1021 gloss: وري ateş çakma (56:71), روح 'ravh / reyhân' (56:89), نزل 'nuzul' (56:56, 93) kapsanmıyor.
* 1022: 'evvel / ûlâ' ölçüm satırı / esma_kayit ayrışması.
* 924: harekesiz kalıp düz elif / elif-medde ayrımı ('fe-levlâ') — DUZELTME 56:62, 70.
* 1001: 56:41 ★ kaynağı.

## SÛRE 57 HADÎD SONU (2026-10-21)

**Okunan: 3896 / 6236 ayet (%62,5)** — sûre 1 ve 9-57 TAM, sûre 2 kısmi (1-20). İlerleme `hadid_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1414** (sûre 57'de yeni kök yok; `kok_ekle_57.py` boş). Aday havuzu **1041** (sûre 57'de yeni aday yok; `AX_hadid` boş). Bağ **AS_hadid** 115. Esmâ okuyucu kararı (KARAR) **518** (483 → 518; 19 İLÂHÎ, 16 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik yedi blokta kayıtta 0 (ön kuru koşu ile; tetik satırı 7 + 1 + 4 + 3 + 3 + 2 + 2 = 22) · [x/y] **343 sayım (48 + 45 + 62 + 47 + 52 + 44 + 45), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması 0 · **DUZELTME 0**.
Sûrenin 29 ayeti uzunluğa göre 7 blokta okundu (1-6, 7-10, 11-15, 16-19, 20-22, 23-26, 27-29); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure57_hadid_okuma.md` (`hadid_paket_md.py`, 29 başlık). Uzak depo **94c8838** (oturum boyunca ilerlemedi); fark zip'i 94c8838 tabanı. Ara zip 57:1-10 ve 57:1-19'da verildi (aynı taban).

### Sûre 57 bilançosu (TAM SAYIM, `okuma_metni['57']['_bilanco_sure']`)
574 kelime · lafız 32 token / 22 ayet · Rab 3 (57:8, 19, 21) · edilgen 6 ayet (5, 13, 15, 16, 18, 21) · iltifât ölçümü 0 (ayet içi şahıs geçişleri 57:4, 12, 17, 19, 22, 25 ölçümde yok — 517) · hapaks yok · mm2 1 (57:25).
Yıldız 0:14 · ★8 (57:1, 21 allah; 57:2, 3 kafiye kırığı — bilanço 'allah' etiketi, 1001; 57:13, 16, 25 n; 57:15 pas) · ★★6 (57:4, 10, 20, 27 n; 57:18 pas; 57:29 allah) · ★★★1 (57:5 pas).
Fâsıla N 15 · R 11 · ب 57:13 · د 57:24 · ز 57:25; kafiye kırığı ölçümde 57:2, 3, 10, 20, 21 (aynı türden 57:4, 22 işaretlenmiyor — 924). En uzun 57:20, 27 (39); en kısa 57:5 (8).
Adlı aktör yalnız 57:26 (Nûh, İbrâhîm), 57:27 (Îsâ, Meryem, İncîl). 'hadîd' sûre içinde yalnız 57:25. Sûre 57:21'in son cümlesiyle bitiyor (nakarat3 GEÇER).

### Çıpa (ölçüt değişmedi)
L4 kesin yok, L3 yok, L2 yok. **L4 ADAYI, teşbih içinde, TARTIŞMALI: 57:20** (dünya hayatı meseli; 39:21 L4 bitki dizisi 'yehîcu fe-terâhu musfarran summe … hutâmâ' teşbih içinde tekrar ediyor; 48:29 ile aynı statü; cipa=False, **karar kullanıcıda**). L1: 57:4 (L4 ölçü koluna sınırda), 6, 17, 25. L0: 57:1, 2, 5, 10. Olgu değil: 57:9 (mecaz), 12, 21 (cennet), 13 (âhiret sahnesi), 15, 19 (cehennem). Tarayıcı v4 adayı 4 (57:9, 13, 17, 20), kesinlik **0/4** (57:20 kısmi).

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
35 e_oto tokeni → ilâhî 19, değil 16. §4.3 mühür 16 → geçerli **10** (57:1, 2, 3, 4, 6, 9, 10, 24, 25, 28); yanlış mühür 57:7, 8, 11, 13, 15, 18 (ecr sıfatı, insanlar, sur, ateş). Ölçüm satırı 57:2, 4, 6'da 'MÜHÜRSÜZ' / bilanço geçerli (51:58 emsali). 1022: 57:3 'evvel'.

### Aday 1041 — kayıt (sûre 57'de altı vaka)
'evvel / âhir' 56:13-14 insanlar / 57:3 Allah · 'zâhir / bâtın' 57:3 Allah / 57:13 sur · 'âhir' 57:3 / 57:20 âhiret · 'mevlâ' 47:11 Allah / 57:15 ateş · kökler رأف رحم 57:9 Allah / 57:27 insan kalbi · 'yed' 57:12 insan / 57:29 Allah. Test yok.

### Aday 1040 — kayıt (test korpus sonunda)
56:96 / 57:1 (2MS tesbih emri + Rab → PERF tesbih + lafız; fâsıla م → م) · 56:13-14 / 57:3. 57:29 → 58:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
29 ayetin hepsinde not yazıldı. Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1017: adsız konuşan / gönderge (57:8, 10, 12, 13, 14, 15, 16); kayıttan önce 31:18 bağlamından kişi adı çıkarıldı.
* 1021 gloss: أخر 'âhir', نهر 'nehâr', كفر 'örtme' (57:20 'kuffâr'), حدد 'keskin' (50:22) kapsanmıyor; 'kifl' lemması.
* 1022: 57:3 'evvel'.
* 924: harekesiz kalıp i'râb / elif-medde / kip ayrımı; kafiye kırığı kuralı tutarsız.
* 1001: 57:2, 3 ★ kaynağı.
* 1014: tarayıcı v4 kesinlik 0/4.

### Karar bekleyen (kullanıcı)
**Kullanıcı kararı (2026-10-21): bekleyen kararların hepsine tam okuma bittikten sonra bakılacak.** 48:29 ve **57:20** çıpa (teşbih içi L4 adayı) — birlikte karara bağlanacak. S2 ◈K tetik فلك; مأي gloss; oturum_* yardımcıları. Esmâ ön-kaydı DONDURULDU.

## SÛRE 58 MÜCÂDELE SONU (2026-10-22)

**Okunan: 3918 / 6236 ayet (%62,8)** — sûre 1 ve 9-58 TAM, sûre 2 kısmi (1-20). İlerleme `mucadele_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1419** (1414 → 1419; كبت, فسح, جلس, نشز, حوذ — `kok_ekle_58.py`). Aday havuzu **1041** (sûre 58'de yeni aday yok; `AX_mucadele` boş). Bağ **AS_mucadele** 94. Esmâ okuyucu kararı (KARAR) **533** (518 → 533; 13 İLÂHÎ, 2 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik altı blokta kayıtta 0 (ön kuru koşu ile; tetik satırı 1 + 2 + 1 + 2 + 1 + 2 = 9) · [x/y] **259 sayım (47 + 41 + 39 + 45 + 41 + 46), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması: hedefli 0, genel geçişte 1 (58:11 yeni gloss) · **DUZELTME 0**.
Sûrenin 22 ayeti uzunluğa göre 6 blokta okundu (1-4, 5-7, 8-10, 11-13, 14-18, 19-22); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure58_mucadele_okuma.md` (`mucadele_paket_md.py`, 22 başlık). Uzak depo **94c8838** (oturum boyunca ilerlemedi); fark zip'i 94c8838 tabanı, sûre 57 + 58 değişikliklerini birlikte taşır (57 yüklenmediyse). Ara zip 58:1-7 ve 58:1-13'te verildi (aynı taban).

### Sûre 58 bilançosu (TAM SAYIM, `okuma_metni['58']['_bilanco_sure']`)
472 kelime · **lafız 40 token / 22 ayetin hepsi** · **Rab 0** · edilgen 5 ayet (3, 5, 8, 9, 11) · iltifât ölçümü 0 (58:5 1P, 58:8 iç söz 1P, 58:21 1S alıntı ölçümde yok — 517) · hapaks 58:11 (فسح, جلس) · mm2 yok.
Yıldız 0:11 · ★3 (58:10, 13, 20 allah) · ★★2 (58:5 pas; 58:8 n) · ★★★6 (58:1, 6, 21 allah; 58:7, 22 n; 58:11 hapaks).
Fâsıla N 15 · R 5 · د 58:6 · ز 58:21; kafiye kırığı ölçümde 58:6, 8, 11, 21. En uzun 58:22 (51); en kısa 58:20 (8).
Adlı aktör yalnız cehennem (58:8) ve şeytan (58:10, 19); kişi adı yok. Kök حدد dört ayette (58:4, 5, 20, 22). Sûre iki karşıt grupla kapanıyor: 'hizbu'ş-şeytân … humu'l-hâsirûn' (58:19) / 'hizbu'llâh … humu'l-mufluhûn' (58:22).

### Çıpa (ölçüt değişmedi)
L4 yok, L3 yok, L2 yok, L1 yok. L0: 58:7. Olgu değil: 58:6, 18 (diriliş), 8 (cehennem), 17 (ateş), 22 (cennet). Tarayıcı v4 adayı 2 (58:7, 22), kesinlik **0/2**.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
15 e_oto tokeni → ilâhî 13, değil 2 (58:10 'mu'minûn', 58:22 'âhir'). §4.3 mühür 10 → geçerli **9** (58:1, 2, 3, 6, 7, 11, 12, 13, 21); yanlış mühür 58:10. Ölçüm satırı 58:3, 6, 7, 11, 13'te 'MÜHÜRSÜZ' / bilanço geçerli; 58:13 'habîr' son kelime değil, ölçüm 'SON konum' (1022).

### Aday 1041 — kayıt (sûre 58'de on vaka)
'semî' / basîr' 11:24 / 58:1 · 'râbi' / sâdis' 18:22 köpek / 58:7 'huve' · 'nesiye' 9:67 / 58:6 · 'şehîd' 24:6 / 58:6 · 'alîm' 51:28 / 58:7 · 'mu'min' esmâ / 58:10 · فسح 58:11 insanlara emir / Allah'ın cevabı · 'tâbe' 24:5 / 58:13 · 'âhir' 57:3 / 58:22 · رضو 58:22 iki yön. Test yok.

### Aday 1040 — kayıt (test korpus sonunda)
57:29 / 58:1 (lafızla kapanış → lafız 3. kelimede açılış; fâsıla م → ر) · 'inne'llâhe qaviyyun azîz' yalnız 57:25 ve 58:21. 58:22 → 59:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
22 ayetin hepsinde not yazıldı. Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1017: 58:1 kadın, kocası, 2MS muhatap adsız (ad verilmedi); 58:11 'qîle'; 58:14 gazap edilen topluluk; 58:8 iç söz; 58:21 1S alıntı.
* 1021: ظهر 'zâhara' (destek / zıhâr); حيي selamlama ◈B tetiği; يدي 'beyne yedey' tetiği; 'yemîn' lemması sağ yan / yemin.
* 1022: 58:3, 6, 7, 11, 13 ölçüm / bilanço ayrışması; 58:13 son konum; 'mu'min' çoğulu.
* 924: **ayet 1 harf alanı** — harf → harf3 farkı isaret ile açıklanmıyor (56:1, 57:1, 58:1; besmele sayılıyor olabilir); sayı işareti 'e'adde', 'aşîre'; dikey kat oranı küçük n'de şişiyor (58:11 ×5800).
* 517: 58:14 QASEM etiketi anlatılan yemin için.
* 1014: tarayıcı v4 kesinlik 0/2.

### Karar bekleyen (kullanıcı — TAM OKUMA SONUNDA)
48:29 ve 57:20 çıpa (teşbih içi L4 adayı); S2 ◈K tetik فلك; مأي gloss; oturum_* yardımcıları. Esmâ ön-kaydı DONDURULDU. Sûre 58'de yeni karar bekleyen yok.

## SÛRE 59 HAŞR SONU (2026-10-23)

**Okunan: 3942 / 6236 ayet (%63,2)** — sûre 1 ve 9-59 TAM, sûre 2 kısmi (1-20). İlerleme `hasr_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1426** (1419 → 1426; خرب, جلو, وجف, دول, خصص, وبل, همن — `kok_ekle_59.py`). Aday havuzu **1041** (sûre 59'da yeni aday yok; `AX_hasr` boş). Bağ **AS_hasr** 79. Esmâ okuyucu kararı (KARAR) **561** (533 → 561; 22 İLÂHÎ, 6 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik dört blokta kayıtta 0 (ön kuru koşu ile; tetik satırı 2 + 1 + 3 + 4 = 10) · [x/y] **258 sayım (50 + 72 + 69 + 67), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması: hedefli 0, genel geçişte **3 (YANLIŞ — aşağıda Hâmân çakışması)** · **DUZELTME 1** (59:24).
Sûrenin 24 ayeti uzunluğa göre 4 blokta okundu (1-5, 6-10, 11-17, 18-24); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure59_hasr_okuma.md` (`hasr_paket_md.py`, 24 başlık). Uzak depo **a5a609e** (oturum boyunca ilerlemedi); fark zip'i a5a609e tabanı. Ara zip 59:1-10'da verildi (aynı taban).

### Sûre 59 bilançosu (TAM SAYIM, `okuma_metni['59']['_bilanco_sure']`)
445 kelime · **lafız 29 token / 17 ayet** · **Rab 3 token** (59:10 ×2 vokatif, 59:16) · edilgen 4 ayet (8, 9, 11, 12) · iltifât ölçümü 0 (59:10, 11 1P iç söz, 59:16 1S, 59:21 1P 'enzelnâ' ölçümde yok — 517) · hapaks yok · mm2 yok.
Yıldız 0:13 · ★6 (59:6, 8, 23 allah; 59:9, 11 n; 59:10 rab) · ★★4 (59:2, 7 n; 59:12 pas; 59:18 allah) · ★★★1 (59:4 allah).
Fâsıla N 19 · R 3 · ب 2; kafiye kırığı yok. En uzun 59:2 (40); en kısa 59:17, 19, 20 (10).
Adlı aktör: şeytan (59:16), cennet (59:20, yer), Kur'an (59:21); kişi adı yok; adsız karye 59:7, 14. Sayı işareti 59:11 'ehad' (anlam 'hiç kimse'). Sûre halkası (okuma): 59:1 'sebbaha … ve huve'l-azîzu'l-hakîm' / 59:24 'yusebbihu … ve huve'l-azîzu'l-hakîm'; üç 'huve'llâh' ayeti (59:22-24).

### Çıpa (ölçüt değişmedi)
L4 yok, L3 yok, L2 yok, L1 yok. L0: 59:1, 24 (gökler / yer), 59:5 (ağaç kökü üzerinde, eylem insanın), 59:6 (atlar, binekler), 59:21 (dağ, varsayım içinde — 48:29 / 57:20 teşbih ailesinden ayrı: doğa süreci yok). Olgu değil: 59:3, 17 (ateş), 59:20 (ateş, cennet). Tarayıcı v4 adayı 2 (59:3, 21), kesinlik **0/2**.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
28 e_oto tokeni → ilâhî 22, değil 6 (59:2 'evvel', 'mu'minîn'; 59:3 'âhira'; 59:7 'ağniyâ''; 59:11 'ehad'; 59:15 'qarîb'). §4.3 mühür 10 → geçerli **7** (59:1, 6, 10, 18, 22, 23, 24); yanlış mühür 59:2, 3, 11. Ölçüm satırı 59:6, 18, 23'te 'MÜHÜRSÜZ' / bilanço geçerli; 59:23'te sekiz addan altısı, 59:24'te beşten dördü ölçümde ('quddûs', 'mutekebbir', 'musavvir' yok) (1022).

### ★ YENİ ARAÇ AÇIĞI — gloss_gecis özel ad iskeleti çakışması (924 ailesi; KARAR BEKLER, okuma sonu)
Kök همن (muheymin, 59:23) `kok_turkce`'ye eklenince `yama_retroaktif_gloss_59` genel geçişi 28:6 olcum + mercek ve 28:8 olcum alanlarındaki nakarat2 dizgesinde **Hâmân** adının harekesiz iskeletini kök sandı ve 'muheymin' glossunu yapıştırdı. `gloss_gecis` harekesiz iskelet ile kök anmasını ayırmıyor. Araç değiştirilmedi (dondurma); `yama_haman_59.py` (idempotent) yanlış glossu açıklama notuna çevirdi, turkce_denetim 0 korundu. `mercek_kayit.json`'daki iki çıplak anma (28:6, 28_atlama) denetim dışı, dokunulmadı. Aynı risk başka özel ad iskeletleri için açık: kök eklerken genel geçişin sayısı 0 değilse değişen alanlar tek tek okunmalı.

### Kendi kaydı
Kayıttan önce: 59:10 'ğıll' sayısı; 59:18 ◈K tetiksiz dolu; basılmamış ayetlerin adla anılması (58:12, 9:67, 24:4, 24:55); 'cebel', 'hâliq' sayıları; sayılmamış 'en uzun' — düzeltildi. Kayıttan sonra: 59:17 'hâlidîne' alıntısı (blok yeniden koşuldu, özgün alan korunmadı — usul hatası, DUZELTME'ye alınmalıydı); 59:24 lafız sayısı (kök أله 31 ≠ lafız 29) → **DUZELTME 1**. Sohbette: sûre kelime toplamı 498 yazıldı, defter 445 (kayda girmedi).

### Aday 1041 — kayıt (sûre 59)
'evvel', 'âhir' 57:3 / 59:2-3 · **'mu'min' aynı sûrede 59:2 inananlar / 59:23 Allah** · 'ğanî' / 59:7 · 'âthara' 12:91 / 59:9 · 'qarîb', 'ehad' / 59:15, 59:11 · 'cebbâr' + 'mutekebbir' 40:35 / 59:23 · 'melik' 12:54 / 59:23 · نسي 59:19 iki yön · برأ 59:16 / 59:24. Test yok.

### Aday 1040 — kayıt (test korpus sonunda)
58:22 / 59:1 (grup adıyla kapanış → tesbihle açılış; fâsıla ن → م). 59:24 → 60:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
24 ayetin hepsinde not yazıldı. Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1017: 59:2 çıkarılanlar ve yurt; 59:7, 14 kasabalar; 59:8-10 üç grup; 59:11 münafıklar ve kardeşleri; 59:15 'az önce geçenler'; 2MS / 2MP muhataplar; 59:10, 11, 16 iç sözler.
* 1021: لين 'yumuşaklık' (59:5 hurma); خيل 'hayal' (59:6 atlar); morph 'ğıll' / 'ağlâl' aynı lemma.
* 1022: 59:6, 18, 23 ölçüm / bilanço ayrışması; 59:23-24 eksik ad gösterimi; 59:2, 3, 11 karar sonrası geçersiz mühür.
* 924: ayet 1 harf alanı (59:1); sayı işareti 'ehad'; 59:9 morph IMPV 2MP etiketi; **gloss çakışması (Hâmân / همن)**.
* 517: iç söz ve 1P 'enzelnâ' iltifât 0.
* 1014: tarayıcı v4 kesinlik 0/2.

### Karar bekleyen (kullanıcı — TAM OKUMA SONUNDA)
48:29 ve 57:20 çıpa (teşbih içi L4 adayı); S2 ◈K tetik فلك; مأي gloss; oturum_* yardımcıları; **gloss_gecis özel ad iskeleti çakışması (yeni)**. Esmâ ön-kaydı DONDURULDU.

## SÛRE 60 MÜMTEHİNE SONU (2026-10-23)

**Okunan: 3955 / 6236 ayet (%63,4)** — sûre 1 ve 9-60 TAM, sûre 2 kısmi (1-20). İlerleme `mumtehine_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1426** (sûre 60'ta eksik kök yok; `kok_ekle_60.py` boş). Aday havuzu **1041** (sûre 60'ta yeni aday yok; `AX_mumtehine` boş). Bağ **AS_mumtehine** 56. Esmâ okuyucu kararı (KARAR) **577** (561 → 577; 12 İLÂHÎ, 4 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik dört blokta kayıtta 0 (ön kuru koşu ile; tetik satırı 3 + 2 + 0 + 2 = 7) · [x/y] **194 sayım (47 + 54 + 40 + 53), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması 0 · **DUZELTME 0**.
Sûrenin 13 ayeti uzunluğa göre 4 blokta okundu (1-3, 4-7, 8-10, 11-13); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure60_mumtehine_okuma.md` (`mumtehine_paket_md.py`, 13 başlık). Uzak depo **a5a609e** (oturum boyunca ilerlemedi); fark zip'i a5a609e tabanı, sûre 59 + 60.

### Sûre 60 bilançosu (TAM SAYIM, `okuma_metni['60']['_bilanco_sure']`)
348 kelime · **lafız 21 token / 11 ayet** · **Rab 4 token** (60:1, 60:4, 60:5 ×2) · edilgen 0 · iltifât ölçümü 0 (60:1 1S konuşan + 3. şahıs 'rabbikum'; 60:4 iç sözler — 517) · hapaks yok · mm2 yok.
Yıldız 0:6 · ★1 (60:6 allah) · ★★2 (60:5 rab; 60:12 n) · ★★★4 (60:1, 4, 10 n; 60:7 allah).
Fâsıla N 8 · R 3 (60:3, 4, 13) · ل 1 (60:1) · د 1 (60:6); kafiye kırığı 60:6. En uzun 60:10 (55); en kısa 60:2, 3, 5 (13).
Adlı aktör: İbrâhîm (60:4 ×2); Nebî 60:12'de sıfatla. Sayı işareti 60:4 'vahdeh' (anlam 'tek başına'), 60:11 'ezvâc'. Sûre halkası (okuma): 60:1 'yâ eyyuhe'llezîne âmenû lâ tettehızû … evliyâ'' / 60:13 'yâ eyyuhe'llezîne âmenû lâ tetevellev' (nakarat3 GEÇER). Sûre içi açık eş kalmadı.

### Çıpa (ölçüt değişmedi)
L4, L3, L2, L1, L0 yok. Olgu değil: 60:3 (kıyamet günü), 60:6 (âhiret günü), 60:11 (insan eşleri), 60:13 (âhiret, kabirdekiler). Tarayıcı v4 adayı 1 (60:11), kesinlik **0/1**.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
16 e_oto tokeni → ilâhî 12, değil 4 (60:1 'evliyâ''; 60:6 'âhir'; 60:11 'mu'minûn'; 60:13 'el-âhire'). §4.3 mühür 7 → geçerli **6** (60:3, 5, 6, 7, 10, 12); yanlış mühür 60:11. Ölçüm satırı 60:3'te 'SON, MÜHÜRSÜZ' / bilanço geçerli (1022).

### ★ YENİ ARAÇ AÇIĞI — lemma eşsesli birleşmesi (924 ailesi; kayıt, araç değişmedi)
`oturum_lem.py` lemma 'asâ' (عصا) listesi değnek ('asâ: 2:60, 7:107, 20:18 …) ve isyan ('asâ: 20:121, 60:12 …) geçişlerini birlikte sayıyor (37 ayet; kök عصي 32). 60:12'de kök sayısı kullanıldı. Eşsesli şüphesinde `--kok` ile karşılaştır.

### Kendi kaydı
Kayıttan önce: 60:3 basılmamış eşler hakkında 'rahimler' iddiası silindi; 60:12 'sûrenin öbür üç nidâsı' (dua nidâları 'rabbenâ' dışarıda kalıyordu) → 'yâ eyyuhe ile açılan öbür üç ayet'. Kayıttan sonra: 60:11-13 ARIZA notunda 'kafiye kırığı 0' blok içi diye netleştirildi ve [x/y] 52 → 53 (son koşu); ARIZA notu, mercek alanı değil — blok yeniden koşuldu. DUZELTME 0.

### Aday 1041 — kayıt (sûre 60)
'veliyy' / 60:1 'evliyâ'' · 'âhir' 57:3 / 60:6, 60:13 · 'ğanî' 59:7 / 60:6 · 'berî'' 59:16 / 60:4 · 'ehabbe' 59:9 / 60:8 · 'imtehane' 49:3 / 60:10 · علم 60:10 içinde Allah / inananlar · 'mu'min' 59:23 / 60:11. Test yok.

### Aday 1040 — kayıt (test korpus sonunda)
59:24 / 60:1 (ad dizisi ve tesbihle kapanış → nidâ ve yasakla açılış; fâsıla م → ل). 60:13 → 61:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
13 ayetin hepsinde not yazıldı. Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1017: düşmanlar, elçi, İbrâhîm'in beraberindekileri / kavmi / babası, savaşan / savaşmayan gruplar, göç eden ve biat eden kadınlar, kocalar, gazaba uğramış topluluk, 'ashâbu'l-qubûr' — sınıf, ad verilmedi.
* 1021: رحم 60:3 'erhâm' (akrabalar); ظهر 60:9 'zâherû' destek / zıhâr.
* 1022: 60:3 ölçüm / bilanço ayrışması; 60:11 karar sonrası geçersiz mühür.
* 924: ayet 1 harf alanı (60:1); 60:3:2 morph 2MS etiketi; sayı işareti 'vahdeh'; **lemma 'asâ' eşsesli birleşmesi**.
* 517: 60:1 1S + 3. şahıs; 60:4 iç sözler; iltifât 0.
* 1014: tarayıcı v4 kesinlik 0/1.

### Okuma ikiliği (karar verilmedi)
60:13 'kemâ ye'ise'l-kuffâru min ashâbi'l-qubûr' — inkârcılar kabirdekilerden / kabirdeki inkârcılar umut kesti; meal birincisini aldı.

### Karar bekleyen (kullanıcı — TAM OKUMA SONUNDA)
48:29 ve 57:20 çıpa (teşbih içi L4 adayı); S2 ◈K tetik فلك; مأي gloss; oturum_* yardımcıları; gloss_gecis özel ad iskeleti çakışması (sûre 59). Sûre 60'ta yeni bekleyen karar yok. Esmâ ön-kaydı DONDURULDU.

## SÛRE 61 SAFF SONU (2026-10-24)

**Okunan: 3969 / 6236 ayet (%63,6)** — sûre 1 ve 9-61 TAM, sûre 2 kısmi (1-20). İlerleme `saff_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1427** (1426 → 1427; `kok_ekle_61.py`: رصص, 61:4 'mersûs'). Aday havuzu **1041** (sûre 61'de yeni aday yok; `AX_saff` boş). Bağ **AS_saff** 50. Esmâ okuyucu kararı (KARAR) **588** (577 → 588; 2 İLÂHÎ, 9 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik iki blokta kayıtta 0 (ön kuru koşu ile; tetik satırı 3 + 1 = 4) · [x/y] **129 sayım (55 + 74), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması 0 · **DUZELTME 0**.
Sûrenin 14 ayeti uzunluğa göre 2 blokta okundu (1-7, 8-14); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure61_saff_okuma.md` (`saff_paket_md.py`, 14 başlık). Uzak depo **499918d** (oturum boyunca ilerlemedi); fark zip'i 499918d tabanı, yalnız sûre 61.

### Sûre 61 bilançosu (TAM SAYIM, `okuma_metni['61']['_bilanco_sure']`)
221 kelime · **lafız 17 token / 10 ayet** · **Rab 0** · edilgen 1 (61:7 'yud'â') · iltifât ölçümü 0 (61:14 lafız 3MS → 1P 'eyyednâ' — 517) · hapaks 61:4 (yeni kök رصص) · mm2 61:9.
Yıldız 0:5 · ★4 (61:3, 7, 13 allah; 61:6 n) · ★★3 (61:5, 11 allah; 61:14 n) · ★★★2 (61:4 hapaks; 61:8 allah).
Fâsıla N sınıfı 13 (م 61:1, 10, 12; ن on ayet) · ص 1; kafiye kırığı 61:4. En uzun 61:14 (35); en kısa 61:2 (8).
Adlı aktör: Mûsâ (61:5), Îsâ ibn Meryem (61:6, 14), İsrâ'îl (61:6, 14), Tevrât (61:6), 'ahmed' (61:6), 'adn' (61:12, yer). Sayı işareti yok. Sûre içi halka (okuma): 'yâ eyyuhe'llezîne âmenû' 61:2 → 61:10 → 61:14 (nakarat3 GEÇER); 'qâle îsa'bnu meryem' 61:6 → 61:14 (GEÇER). Sûre içi açık eş kalmadı.

### Çıpa (ölçüt değişmedi)
L4, L3, L2, L1 yok; L0 1 (61:1 gökler ve yer; 57:1, 59:1 emsali). Olgu değil: 61:4 (yapı, insan yapımı), 61:8 (nur, mecaz), 61:12 (cennet ırmakları). Tarayıcı v4 adayı 1 (61:8), kesinlik **0/1**.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
11 e_oto tokeni → ilâhî 2 (61:1 azîz, hakîm), değil 9 (61:6 'mubîn'; 61:8 'nûr' ×2; 61:13 'qarîb', 'mu'minîn'; 61:14 'ensâr' ×3, 'zâhirîn'). §4.3 mühür 5 → geçerli **1** (61:1); yanlış mühür 61:6, 8, 13, 14. Ölçüm satırı 61:6'da 'MÜHÜRSÜZ' / esma_kayit 'mühür EVET' (1022).

### Kendi kaydı
Kayıttan önce: 61:6'da 61:4'ün kök sayısı [x/y] biçimiyle yazılmıştı (oturum_xy yakaladı) → 'sûre içi' biçimi; 61:4'te bu oturumda basılmamış iki okunmuş ayet adla anılmıştı → sayısız anma; 61:3, 61:4 ders göndermelerindeki basılmamış ayet numaraları çıkarıldı; 61:11 karşıt çift satırı 'yok' biçimine getirildi. Kayıttan sonra hata yakalanmadı. DUZELTME 0.

### Aday 1041 — kayıt (sûre 61)
زيغ 61:5 'zâğû' insan / 'ezâğa'llâhu' Allah · حبب 61:4 / 61:13 (Allah sever / siz seversiniz) · نصر 61:13 'nasrun mina'llâh' / 61:14 'ensâru'llâh' · ظهر 61:9 'li-yuzhirahû' / 61:14 'zâhirîn' · lemma 'zâhir' 57:3 Allah adı / 40:29 kavim / 61:14 inananlar. Test yok.

### Aday 1040 — kayıt (test korpus sonunda)
60:13 / 61:1 (nidâ ve dost edinme yasağıyla kapanış → tesbihle açılış; fâsıla ر → م). 61:14 → 62:1 henüz okunmadı. Ardışık olmayan eşleşmeler okuma bağına yazıldı: 59:1 / 61:1 (esit2 TAM, aynı tesbih açılışı); 9:32-33 → 61:8-9 (aynı sırayla iki ayet).

### Aday 1039 — okuma kolu (karşıt çift) verisi
14 ayetin hepsinde not yazıldı (61:11 'yok'). Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1017: 61:2-3 muhatap ve soran; savaşanlar; Mûsâ'nın kavmi; 'qâlû' diyenler; yalan uyduran ve çağıran (edilgen); söndürmek isteyenler; elçi; konuşan 1S (61:10); 'beşşir' muhatabı; iki 'tâ'ife', düşmanlar, konuşan 1P — ad verilmedi; 'ahmed' metin dışı kişiyle eşlenmedi.
* 1022: 61:6, 8, 13, 14 esma_kayit mühür EVET, karar sonrası geçersiz.
* 1038: 61:6 'ahmed' rol 'fail' (metinde 'ismuhû'nun haberi).
* 924: ayet 1 harf alanı (61:1); nakarat3 61:5 'ennî' / 61:6 'innî' harekesiz eşleşmesi; ölçüm kipi 61:11 haber kipindeki emir anlamını görmüyor; ★★★ 61:4 yeni kök hapaksı, 61:8 kısa ayette lafız.
* 517: 61:14 3MS → 1P; iltifât 0.
* 1014: tarayıcı v4 kesinlik 0/1 (nur, mecaz).

### Okuma ikiliği (karar verilmedi)
61:6 'fe-lemmâ câ'ehum bi'l-beyyinât' — fail zamiri Îsâ ya da 'ahmed' adlı elçi.

### Karar bekleyen (kullanıcı — TAM OKUMA SONUNDA)
48:29 ve 57:20 çıpa (teşbih içi L4 adayı); S2 ◈K tetik فلك; مأي gloss; oturum_* yardımcıları; gloss_gecis özel ad iskeleti çakışması (sûre 59). Sûre 61'de yeni bekleyen karar yok. Esmâ ön-kaydı DONDURULDU.

## SÛRE 62 CUMA SONU (2026-10-24)

**Okunan: 3980 / 6236 ayet (%63,8)** — sûre 1 ve 9-62 TAM, sûre 2 kısmi (1-20). İlerleme `cuma_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1427** (sûre 62'de eksik kök yok; `kok_ekle_62.py` boş). Aday havuzu **1041** (sûre 62'de yeni aday yok; `AX_cuma` boş). Bağ **AS_cuma** 39. Esmâ okuyucu kararı (KARAR) **598** (588 → 598; 8 İLÂHÎ, 2 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik iki blokta kayıtta 0 (ön kuru koşu ile; tetik satırı 2 + 6 = 8) · [x/y] **114 sayım (41 + 73), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması 0 · **DUZELTME 0**.
Sûrenin 11 ayeti 2 blokta okundu (1-5, 6-11); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure62_cuma_okuma.md` (`cuma_paket_md.py`, 11 başlık). Uzak depo **499918d** (oturum boyunca ilerlemedi); fark zip'i 499918d tabanı, sûre 61 + 62 (61 ayrıca yüklendiyse fark yalnız 62'yi taşır).

### Sûre 62 bilançosu (TAM SAYIM, `okuma_metni['62']['_bilanco_sure']`)
175 kelime · **lafız 12 token / 8 ayet** · **Rab 0** · edilgen 4 (62:5, 8, 9, 10) · iltifât ölçümü 0 · hapaks yok · mm2 yok.
Yıldız 0:8 · ★1 (62:7 allah) · ★★1 (62:10 allah) · ★★★1 (62:4 allah).
Fâsıla N sınıfı 11 (م 62:1-4; ن 62:5-11); kafiye kırığı yok. En uzun 62:5 (23); en kısa 62:3 (8).
Adlı: Tevrât (62:5), 'cumu'a' (62:9, korpusta 1 token). Sayı işareti 62:10 'kesîr' (çokluk; 924). 2MS 'qul' 62:6, 8, 11. Sûre içi açık eş kalmadı.

### Çıpa (ölçüt değişmedi)
L4, L3, L2, L1 yok; L0 4 (62:1 gökler ve yer; 62:6, 62:8 ölüm; 62:10 yeryüzü). Olgu değil: 62:5 (teşbihte eşek, süreç yok). Tarayıcı v4 adayı 2 (62:6, 62:10), kesinlik **0/2**.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
10 e_oto tokeni → ilâhî 8 (62:1 melik, quddûs, azîz, hakîm; 62:3 azîz, hakîm; 62:7 alîm; 62:8 âlim), değil 2 (62:2 'mubîn'; 62:6 'evliyâ''). §4.3 mühür 5 → geçerli **4** (62:1, 3, 7, 8); yanlış mühür 62:2. Ölçüm satırı 62:1'de 'quddûs'u göstermiyor; 62:7 'SON' konum etiketi metinle ayrışıyor (1022).

### Kendi kaydı
Kayıttan önce: 62:5 karşıt çift satırındaki metin dışı çıkarım ('anlamaz') silindi; 62:4'te 1041 vakası olmayan not silindi; 62:11 'son geçişler' listesinde خير [3/3] → [2,3/3] (oturum_xy yakaladı); 62:6, 62:7'de basılmamış iki okunmuş ayet ders / emsal numarasıyla anılmıştı → numarasız. Kurulumda `python3 -c 'import aday_ekle_62_cuma'` betiği boş haliyle koşturdu (AX_cuma / AS_cuma boş yazıldı; idempotent, blok kaydında yeniden yazıldı). DUZELTME 0.

### Aday 1041 — kayıt (sûre 62)
حكم 62:1, 3 'el-hakîm' / 62:2 'el-hikmeh' · علم 62:7 'alîm', 62:8 'âlim' / 62:9 'ta'lemûn' · 'veliyy' esmâ / 62:6 'evliyâ'u li'llâh'. Test yok.

### Aday 1040 — kayıt (test korpus sonunda)
61:14 / 62:1 (inananların üstünlüğüyle kapanış → tesbihle açılış; fâsıla ن → م). Ardışık iki sûre (61, 62) aynı tesbih cümlesiyle açılıyor (PERF → IMPF) ve beş koşut daha: 61:9 / 62:2 'huve'llezî ersele / be'ase'; 61:6 / 62:5 Tevrât; 61:7 / 62:5 'lâ yehdi'l-qavme'z-zâlimîn'; 61:11 / 62:9 'zâlikum hayrun lekum in kuntum ta'lemûn'; 61:10 / 62:11 'ticâret'. 62:11 → 63:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
11 ayetin hepsinde not yazıldı (62:4 'yok'). Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1017: elçi, ümmîler, sonradan gelenler, Tevrât yüklenenler ve yükleyen, 'qul' muhatabı, 'ellezîne hâdû', edilgen failler, dağılıp gidenler, ayakta bırakılan 2MS — ad verilmedi.
* 1021: بأس 62:5 'bi'se' (ne kötü).
* 1022: 62:1 'quddûs' ölçüm satırında yok; 62:2 karar sonrası geçersiz mühür; 62:7 konum etiketi.
* 924: ayet 1 harf alanı (62:1); 62:2 muhaffefe 'in' → 'şart'; **lemma 'esfâr' eşsesli** (34:19 / 62:5); sayı işareti 'kesîr'; 62:4 ★★★.
* 1014: tarayıcı v4 kesinlik 0/2.

### Okuma ikiliği
Yok. 62:5 Tevrât yüklenenler / 62:6 'ellezîne hâdû' göndergesi eşlenmedi.

### Karar bekleyen (kullanıcı — TAM OKUMA SONUNDA)
48:29 ve 57:20 çıpa (teşbih içi L4 adayı); S2 ◈K tetik فلك; مأي gloss; oturum_* yardımcıları; gloss_gecis özel ad iskeleti çakışması (sûre 59). Sûre 62'de yeni bekleyen karar yok. Esmâ ön-kaydı DONDURULDU.

## SÛRE 63 MÜNÂFİKÛN SONU (2026-10-24)

**Okunan: 3991 / 6236 ayet (%64,0)** — sûre 1 ve 9-63 TAM, sûre 2 kısmi (1-20). İlerleme `munafikun_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1430** (1427 → 1430; `kok_ekle_63.py`: جسم, خشب, سند — hepsi 63:4). Aday havuzu **1041** (sûre 63'te yeni aday yok; `AX_munafikun` boş). Bağ **AS_munafikun** 38. Esmâ okuyucu kararı (KARAR) **602** (598 → 602; 1 İLÂHÎ, 3 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik iki blokta kayıtta 0 (ön kuru koşu ile; tetik satırı 2 + 4 = 6) · [x/y] **116 sayım (48 + 68), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması 0 · **DUZELTME 0**.
Sûrenin 11 ayeti 2 blokta okundu (1-5, 6-11); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure63_munafikun_okuma.md` (`munafikun_paket_md.py`, 11 başlık). Uzak depo **499918d** (oturum boyunca ilerlemedi); fark zip'i 499918d tabanı, sûre 61 + 62 + 63.

### Sûre 63 bilançosu (TAM SAYIM, `okuma_metni['63']['_bilanco_sure']`)
180 kelime · **lafız 14 token / 9 ayet** · **Rab 1** (63:10 'rabbi', ölenin nidâsı) · edilgen 3 (63:3, 4, 5) · iltifât ölçümü 0 · hapaks 63:4 (yeni kökler خشب, سند) · mm2 yok.
Yıldız 0:7 · ★1 (63:6 allah) · ★★1 (63:1 allah) · ★★★2 (63:4 hapaks; 63:11 allah).
Fâsıla N sınıfı 11 (hepsi ن); kafiye kırığı yok. En uzun 63:4 (22); en kısa 63:3, 63:11 (11).
Adlı: 'medîne' (63:8; hangi şehir söylenmiyor, ad verilmedi). Sayı işareti 63:10 'ehad' (biriniz; 924). Sûre içi açık eş kalmadı.

### Çıpa (ölçüt değişmedi)
L4, L3, L2, L1 yok; L0 3 (63:7 gökler ve yer; 63:10 ölüm; 63:11 ecel). Olgu değil: 63:4 (teşbihte kütük), 63:8 (şehir). Tarayıcı v4 adayı yok.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
4 e_oto tokeni → ilâhî 1 (63:11 habîr), değil 3 (63:8 'mu'minîn'; 63:10 'ehad', 'qarîb'). §4.3 mühür 3 → geçerli **1** (63:11); yanlış mühür 63:8, 63:10. 63:11 'SON' konum etiketi metinle ayrışıyor (1022).

### Kendi kaydı
Kayıttan önce: 63:4'te lemma 'sayha'nın basılmamış okunmuş 12 ayeti için 'hepsinde helâk sesi' içerik iddiası silindi; 63:6, 63:11'de basılmamış iki ölçüm xref ayeti ve bir lemma eşi sayıya çevrildi. DUZELTME 0.

### Aday 1041 — kayıt (sûre 63)
شهد 63:1 'neşhedu' (münafıklar) / 've'llâhu yeşhedu' · عزز 63:8 'el-e'azz' (münafıkların iddiası) / 'li'llâhi'l-izzeh'. Kökün iki anlamı aynı ayette: نفق 63:7 'lâ tunfiqû' / 'el-munâfiqîn'. Test yok.

### Aday 1040 — kayıt (test korpus sonunda)
62:11 / 63:1 (2MS'i bırakıp gidenlerle kapanış → 2MS'e gelen münafıklarla açılış; fâsıla ن → ن). Ardışık sûrelerde: 62:9 / 63:9 'zikri'llâh'; 62:11 'infaddû', 'lehv' / 63:7 'yenfaddû', 63:9 'lâ tulhikum'; 62:11 'hayru'r-râziqîn' / 63:10 'razaqnâkum'. 63:11 → 64:1 henüz okunmadı. Ardışık olmayan: 58:15-16 → 63:2 (okuma bağı).

### Aday 1039 — okuma kolu (karşıt çift) verisi
11 ayetin hepsinde not yazıldı. Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1017: elçi (2MS), münafıklar, 'qîle' söyleyen, 'men inde rasûli'llâh', 'el-e'azz' / 'el-ezell', 'el-medîne', ölen 1S — ad verilmedi.
* 1021: علو 63:5 'te'âlev' (gelin).
* 1022: 63:8, 63:10 karar sonrası geçersiz mühür; 63:11 konum etiketi.
* 924: ayet 1 harf alanı (63:1); 63:4 ve 63:11 ★★★; sayı işareti 'ehad'; 63:10 'rabbi' nidâsı ölçümde VOC değil.
* Ön-kayıt §4: tetik dışı beden adları 63:4 'ecsâm', 63:5 'ru'ûs'.
* Kök tablosu: retroaktif yama hedef listesine okunmamış 2:247 giriyor (sûre 2 kısmi) — kaydı yok, yama 0; araç değişmedi.

### Okuma ikiliği
Yok.

### Karar bekleyen (kullanıcı — TAM OKUMA SONUNDA)
48:29 ve 57:20 çıpa (teşbih içi L4 adayı); S2 ◈K tetik فلك; مأي gloss; oturum_* yardımcıları; gloss_gecis özel ad iskeleti çakışması (sûre 59). Sûre 63'te yeni bekleyen karar yok. Esmâ ön-kaydı DONDURULDU.

## SÛRE 64 TEĞÂBUN SONU (2026-10-25)

**Okunan: 4009 / 6236 ayet (%64,3)** — sûre 1 ve 9-64 TAM, sûre 2 kısmi (1-20). İlerleme `tegabun_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1430** (sûre 64'te kök eklenmedi; `kok_ekle_64.py` boş). Aday havuzu **1041** (sûre 64'te yeni aday yok; `AX_tegabun` boş). Bağ **AS_tegabun** 62. Esmâ okuyucu kararı (KARAR) **620** (602 → 620; 14 İLÂHÎ, 4 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik üç blokta kayıtta 0 (ön kuru koşu ile; tetik satırı 5 + 2 + 2 = 9) · [x/y] **180 sayım (58 + 73 + 49), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması 0 · **DUZELTME 0**.
Sûrenin 18 ayeti 3 blokta okundu (1-6, 7-12, 13-18); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure64_tegabun_okuma.md` (`tegabun_paket_md.py`, 18 başlık). Uzak depo **fcf5e41** (oturum boyunca ilerlemedi); fark zip'i fcf5e41 tabanı, yalnız sûre 64. Oturum iki güne yayıldı; ortam korunmuştu.

### Sûre 64 bilançosu (TAM SAYIM, `okuma_metni['64']['_bilanco_sure']`)
241 kelime · **lafız 20 token / 14 ayet** (kök أله 21 = lafız 20 + 64:13 'ilâh') · **Rab 1** (64:7 kasem 've rabbî') · edilgen 2 (64:7, 64:16) · iltifât ölçümü 2 (64:12, 64:13) · hapaks 64:9 (غبن 'teğâbun', sûre adı) · mm2 yok.
Yıldız 0:9 · ★3 (64:6, 64:15 allah; 64:10 etiket allah / düzeltilmiş kafiye, 1001) · ★★2 (64:7 pas; 64:17 allah) · ★★★4 (64:8, 64:11, 64:13 allah; 64:9 hapaks).
Fâsıla R 7, N 10, د 1; kafiye kırığı 64:9, 64:10 — öbür sekiz geçiş işaretlenmedi (924). En uzun 64:9 (27); en kısa 64:18 (5).
Sayı işareti 64:14 'zevc' (eşleriniz; 924). Sûre içi açık eş kalmadı.

### Çıpa (ölçüt değişmedi)
L4, L3, L2, L1 yok; L0 3 (64:1, 64:3, 64:4 gökler ve yer). Olgu değil: 64:9 (cennet ırmakları), 64:10 (ateş), 64:14 (eşler ve çocuklar), 64:17 (borç, mecaz). Tarayıcı v4 adayı 2 (64:9, 64:14), ikisi de çıpa değil — kesinlik 0/2.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
18 e_oto tokeni → ilâhî 14, değil 4 (64:2 'mu'min'; 64:8 'nûr'; 64:12 'mubîn'; 64:13 'mu'minûn'). §4.3 mühür 11 → geçerli **9** (64:1, 2, 4, 6, 8, 11, 14, 17, 18); yanlış mühür 64:12, 64:13. 64:18 'âlim' sınıf E (lafız yok; 62:8 emsali). Ölçüm satırı beş ayette 'MÜHÜRSÜZ' yazıp bilançoda geçerli mühür veriyor (1022).

### Kendi kaydı
Kayıttan önce: 64:1 'sebbaha' okunmuş / okunmamış sayısı (33 / 6 → 31 / 8); 64:2 ◈B tetik listesi (خلق → خلق بصر); 64:7 Rab 'sûre içi tek' → 'şimdiye dek tek'. DUZELTME 0.

### Aday 1041 — kayıt (sûre 64)
هدي 64:6 'e-beşerun yehdûnenâ' (beşer öznesi, topluluğun sözü) / 64:11 'yehdi qalbeh' (Allah) · غفر 64:14 'tağfirû' (insan) / 'ğafûr' (Allah). Kökün iki anlamı: نور 64:8 / 64:10; كفر 64:9 'yukeffir'; وقي 64:16. Test yok.

### Aday 1040 — kayıt (test korpus sonunda)
63:11 / 64:1 (ecelin ertelenmemesi → göklerin ve yerin tesbihi; fâsıla ن → ر). Ardışık sûrelerde: 63:4 / 64:14 'aduvv' + 'ihzer-'; 63:9 / 64:15 'emvâlukum ve evlâdukum'. 64:18 → 65:1 henüz okunmadı. Ardışık olmayan (okuma bağı): 62:1 / 64:1 tesbih açılışı; 62:1 'el-azîzi'l-hakîm' / 64:18; 9:129 / 64:12-13.

### Aday 1039 — okuma kolu (karşıt çift) verisi
18 ayetin hepsinde not yazıldı. Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1017: muhatap 2MP, önceki inkâr edenler, elçiler, 'qul' muhatabı, edilgen fail (64:7, 64:16), 64:18 özne — ad verilmedi.
* 1021: كفر 64:9 'yukeffir' (örtme) gloss'ta yok.
* 1022: beş ayette ölçüm 'MÜHÜRSÜZ' / bilanço geçerli; 64:12, 64:13 karar sonrası geçersiz; 64:4 konum etiketi.
* 1001: 64:10 ★ kaynak etiketi.
* 924: ayet 1 harf alanı (64:1); kafiye kırığı işaretlemesi tutarsız; 'innemâ' (64:12, 64:15) HASR yazılmıyor; 64:13 iltifât 1; sayı işareti 'zevc'.
* Ön-kayıt §4: tetik dışı organ 64:4 'sudûr'.
* esit2: 64:12 → 5:92, 64:15 → 8:28 (henüz okunmadı); 64:18 → 32:6.

### Okuma ikiliği
Yok.

### Karar bekleyen (kullanıcı — TAM OKUMA SONUNDA)
48:29 ve 57:20 çıpa (teşbih içi L4 adayı); S2 ◈K tetik فلك; مأي gloss; oturum_* yardımcıları; gloss_gecis özel ad iskeleti çakışması. Esmâ ön-kaydı DONDURULDU. Sûre 64'te yeni bekleyen karar yok.

## SÛRE 65 TALÂK SONU (2026-10-25)

**Okunan: 4021 / 6236 ayet (%64,5)** — sûre 1 ve 9-65 TAM, sûre 2 kısmi (1-20). İlerleme `talak_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1431** (1430 → 1431; `kok_ekle_65.py`: حيض — 65:4). Aday havuzu **1041** (sûre 65'te yeni aday yok; `AX_talak` boş). Bağ **AS_talak** 57. Esmâ okuyucu kararı (KARAR) **623** (620 → 623; 1 İLÂHÎ, 2 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik üç blokta kayıtta 0 (ön kuru koşu ile; tetik satırı 1 + 3 + 3 = 7) · [x/y] **198 sayım (54 + 71 + 73), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması 0 (hedef 2:222 okunmamış, kaydı yok) · **DUZELTME 0**.
Sûrenin 12 ayeti uzunluğa göre 3 blokta okundu (1-3, 4-7, 8-12); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure65_talak_okuma.md` (`talak_paket_md.py`, 12 başlık). Uzak depo **fcf5e41** (oturum boyunca ilerlemedi); fark zip'i fcf5e41 tabanı, sûre 64 + 65.

### Sûre 65 bilançosu (TAM SAYIM, `okuma_metni['65']['_bilanco_sure']`)
287 kelime · **lafız 25 token / 9 ayet** · **Rab 2** (65:1, 65:8) · edilgen 3 (65:2, 6, 7) · iltifât ölçümü 0 · hapaks yok · mm2 65:8.
Yıldız 0:2 · ★4 · ★★4 · ★★★2 (65:1 n; 65:10 allah) — kaynakların yarısı uzunluk (n).
Fâsıla A sınıfı 12 (11 ا, 65:6 ى); kafiye kırığı yok. En uzun 65:1 (41); en kısa 65:9 (7).
Sayı işareti: 65:1 ve 65:4 'idde', 65:4 'selâse', 65:10 'e'adde' (sayı değil), 65:12 'seb''. Sûre içi açık eş kalmadı.

### Çıpa (ölçüt değişmedi)
L4, L3, L2 yok; L1 3 (65:3 'qadrâ'; 65:4 aybaşı / gebelik sınıfları; 65:12 yedi gök ve yer); L0 1 (65:6). Sınır vakaları (kayıt): 65:4 L4 sınıf kolu kelimesel — sınıflama hukukî (799); 65:12 L4 sınıf / ölçü koluna sınırda (41:12 emsali). Olgu değil: 65:1, 2 (iddet, ecel), 65:8 (kasaba), 65:11 (mecaz / âhiret). Tarayıcı v4 adayı 6, kesinlik 0/6.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
3 e_oto tokeni → ilâhî 1 (65:12 qadîr, orta), değil 2 (65:2 'âhir'; 65:11 'nûr'). §4.3 mühür 1 → geçerli **0**; yanlış mühür 65:2. Sûrede geçerli esmâ mührü yok — ayet sonları hükümle kapanıyor (okuma; iddia yok).

### Kendi kaydı
Kayıttan önce: 65:4 'selâse' için 'sûrede ilk gerçek sayı' (65:2 'zevey' atlanmıştı) → 'süre sayıyla veriliyor'; 65:11 xref 3:101, 3:113 eklendi. DUZELTME 0.

### Aday 1041 — kayıt (sûre 65)
بلغ 65:2 (kadınlar) / 65:3 (Allah) · أجر 65:5 (Allah'ın ödülü) / 65:6 (emzirenin ücreti) · 'emr' 65:8 (Rabbin emri) / 65:9 (kasabanın işi). Kökün iki anlamı: عدد, ظلم, قدر, خرج, حسب. Test yok.

### Aday 1040 — kayıt (test korpus sonunda)
64:18 / 65:1 (sıfat dizisiyle kapanış → nidâ ve hükümle açılış; fâsıla م → ا). Ardışık sûrelerde: 64:16 / 65:1; 64:14 / 65:1; 64:13 / 65:3; 64:9 / 65:5; 64:5 / 65:9; 64:9 / 65:11. 65:12 → 66:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
12 ayetin hepsinde not yazıldı. Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1017: 'en-nebiyy', kadınlar, şahitler, 'yû'azu', çocuk, 'uhrâ', 'zû se'a', kasaba, elçiler, 'rasûlen' — ad verilmedi.
* 1021: كفر 'yukeffir', قدر 'qudira', ظلم 'ez-zulumât', عدد 'e'adde'.
* 1022: 65:2 karar sonrası geçersiz mühür; 65:12 orta konum İLÂHÎ, mühür yok.
* 924: ayet 1 harf alanı (65:1); yıldız kaynağı uzunluk; 'e'adde' sayı işareti; 65:7 ölçüm 1S; 65:1 / 65:8 şahıs geçişi iltifât değil.
* Kök tablosu: retroaktif hedefe okunmamış 2:222 giriyor (sûre 2 kısmi) — kaydı yok, yama 0; araç değişmedi.

### Okuma ikiliği
Yok.

### Karar bekleyen (kullanıcı — TAM OKUMA SONUNDA)
48:29 ve 57:20 çıpa (teşbih içi L4 adayı); S2 ◈K tetik فلك; مأي gloss; oturum_* yardımcıları; gloss_gecis özel ad iskeleti çakışması. Esmâ ön-kaydı DONDURULDU. Sûre 65'te yeni bekleyen karar yok.

## SÛRE 66 TAHRÎM SONU (2026-10-25)

**Okunan: 4033 / 6236 ayet (%64,7)** — sûre 1 ve 9-66 TAM, sûre 2 kısmi (1-20). İlerleme `tahrim_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1433** (1431 → 1433; `kok_ekle_66.py`: صغو — 66:4, ثيب — 66:5). Aday havuzu **1041** (sûre 66'da yeni aday yok; `AX_tahrim` boş). Bağ **AS_tahrim** 51. Esmâ okuyucu kararı (KARAR) **635** (623 → 635; 9 İLÂHÎ, 3 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik üç blokta kayıtta 0 (ön kuru koşu ile; tetik satırı 3 + 5 + 0 = 8) · [x/y] **172 sayım (42 + 71 + 59), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması 0 (hedef 6:113 okunmamış, kaydı yok) · **DUZELTME 0**.
Sûrenin 12 ayeti uzunluğa göre 3 blokta okundu (1-4, 5-8, 9-12); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure66_tahrim_okuma.md` (`tahrim_paket_md.py`, 12 başlık). Uzak depo **fcf5e41** (oturum boyunca ilerlemedi); fark zip'i fcf5e41 tabanı, sûre 64 + 65 + 66.

### Sûre 66 bilançosu (TAM SAYIM, `okuma_metni['66']['_bilanco_sure']`)
249 kelime · **lafız 13 token / 8 ayet** · **Rab 5 / 4 ayet** (66:5, 8, 11, 12) · edilgen 3 (66:6, 7, 10) · iltifât ölçümü 0 · hapaks 1 (66:5 ثيب) · mm2 yok.
Yıldız 0:6 · ★2 · ★★1 · ★★★3 (66:2 allah; 66:5 hapaks; 66:8 n).
Fâsıla N 7, R 4, A 1; kafiye kırığı yok. En uzun 66:8 (45); en kısa 66:2, 7, 9 (11).
Sayı işareti: 66:1, 3, 5 'zevc' (eşler, sayı değil). Sûre içi açık eş kalmadı.

### Çıpa (ölçüt değişmedi)
Sûrede doğal olgu yok (L0-L4 boş). Olgu değil: 66:5 medenî durum, 66:6 ateş / melekler, 66:8 cennet / nur, 66:12 iffet / ruhtan üfleme. Tarayıcı v4 adayı 1 (66:5), kesinlik 0/1.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
12 e_oto tokeni → ilâhî 9, değil 3 (66:4 'mu'minîn'; 66:8 'nûr' ×2). §4.3 mühür 5 → geçerli **4** (66:1, 2, 3, 8); yanlış mühür 66:4 ('zahîr' ile kapanış). 66:3 'el-alîmu'l-habîr' lafızsız, Peygamberin sözünde fail. 66:8 ölçüm satırı 'qadîr' MÜHÜRSÜZ / bilanço geçerli — alan farkı (924).

### Kendi kaydı
Kayıttan önce: 66:4'te 66:3'e ait ظهر sayısı [x/y] biçiminde yazılmıştı — oturum_xy yakaladı. DUZELTME 0.

### Aday 1041 — kayıt (sûre 66)
66:3 'nebbe'e' eş, Peygamber ve Allah için aynı ayette · 'mevlâ' 66:2 / 66:4 (Allah; haberine Cibrîl ve 'sâlihu'l-mu'minîn' ortak). Kökün / lemmanın iki anlamı: ظهر, حلل, 'yemîn', نور, بني. Test yok.

### Aday 1040 — kayıt (test korpus sonunda)
65:12 / 66:1 (bilgiyle kapanış → soru ve nidâyla açılış; fâsıla ا → م). 65:1 / 66:1 aynı nidâ 'yâ eyyuhe'n-nebiyy' ile açılış. Ardışık sûrelerde: 64:14 / 65:1 / 66:1 eşler; 65:1 / 66:5 'tallaqa'; 65:5 ve 65:11 / 66:8. 66:12 → 67:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
12 ayetin hepsinde not yazıldı. Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1017: Peygamber, eşleri, 66:3 konuşan eş, 66:4 iki muhatap, olası eşler, 66:7 edilgen fail, 66:8 konuşanlar, Nûh / Lût / Firavun'un eşleri, 66:10 'qîle' — ad verilmedi; metinde adlı: Cibrîl, Nûh, Lût, Firavun, Meryem, İmrân.
* 1021: بني 66:12 'ibnete' (kız) — gloss 'bina, yapma'.
* 1022: 66:4 karar sonrası geçersiz mühür; 66:8 ölçüm satırı / bilanço mühür farkı.
* 924: ayet 1 harf alanı (66:1); 66:9 = 9:73 karakter eşitliği, esit2 oranı 0,9821 (YAKIN); yıldız kaynağı uzunluk; 'zevc' sayı işareti; 66:2 → 66:3 م → ر kafiye kırığı işaretlenmedi.
* Kök tablosu: retroaktif hedefe okunmamış 6:113 giriyor — kaydı yok, yama 0; araç değişmedi.

### Okuma ikiliği
Yok.

## SÛRE 67 MÜLK SONU (2026-10-25)

**Okunan: 4063 / 6236 ayet (%65,2)** — sûre 1 ve 9-67 TAM, sûre 2 kısmi (1-20). İlerleme `mulk_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1435** (1433 → 1435; `kok_ekle_67.py`: طبق — 67:3; وسق — طبق'ın dikey komşuluğunda KARŞILIK YOK çıktı, sûre 33 emsali). Aday havuzu **1041** (sûre 67'de yeni aday yok; `AX_mulk` boş). Bağ **AS_mulk** 90. Esmâ okuyucu kararı (KARAR) **650** (635 → 650; 11 İLÂHÎ, 4 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik üç blokta kayıtta 0 (ön kuru koşu ile; tetik satırı 8 + 5 + 4 = 17) · [x/y] **253 sayım (86 + 80 + 87), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması 0 (hedef 0) · **DUZELTME 0**.
Sûrenin 30 ayeti üç onluk blokta okundu (1-10, 11-20, 21-30); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure67_mulk_okuma.md` (`mulk_paket_md.py`, 30 başlık). Uzak depo **dcab3d3** (oturum boyunca ilerlemedi); fark zip'i dcab3d3 tabanı, sûre 67.

### Sûre 67 bilançosu (TAM SAYIM, `okuma_metni['67']['_bilanco_sure']`)
333 kelime · **lafız 3 token / 3 ayet** (67:9, 26, 28) · **Rab 2 / 2 ayet** (67:6, 12) · A/R 1,5 · edilgen 4 (67:7, 8, 24, 27) · iltifât ölçümü 0 · hapaks yok · mm2 yok.
Yıldız 0:24 · ★4 (67:7, 24, 27 pas; 67:26 allah) · ★★2 (67:6, 12 rab) · ★★★ yok.
Fâsıla R 21 (67:1-21), N 9 (67:22-30); kafiye kırığı işaretlenmedi (67:22 R → N dahil; 924). En uzun 67:3, 67:9 (18); en kısa 67:11 (5).
Sayı işareti: 67:3 'seb'' (gerçek sayı), 67:23 'qalîl' (sayı değil). Nakarat (sûre içi): 67:16/17 GEÇER; 67:20/21, 67:23/24, 67:28/30 GEÇMEZ. Sûre içi açık eş kalmadı.

### Çıpa (ölçüt değişmedi)
L4 yok, L3 yok. L2 1 (67:30 yeti sınırı kolu, soru biçiminde; 18:41 açık biçim). L1 7 (67:3, 4, 5, 15, 16, 19, 23; 67:16 ve 67:19 L2 koluna sınırda, KAPATILAMAZ). L0 3 (67:2, 17, 24). Olgu değil: 67:6-8, 10, 27 âhiret; 67:22 mesel. Tarayıcı v4 adayı 4 (67:2, 3, 19, 30), kesinlik 0/4.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
15 e_oto tokeni → ilâhî 11, değil 4 (67:9, 12 'kebîr'; 67:26, 29 'mubîn'). §4.3 mühür 10 → geçerli **7** (67:1, 2, 13, 14, 19, 20, 29); yanlış mühür 67:9, 12, 26. Ölçüm satırı 67:1, 13, 19, 20, 29'da MÜHÜRSÜZ / bilanço geçerli; 67:20 ve 67:29'da geçerli mühür orta konumdaki 'rahmân'a düşüyor (1022).

### Kendi kaydı
Kayıttan önce: 67:22'de 67:15'e ait مشي sayısı [x/y] biçiminde yazılmıştı — oturum_xy yakaladı; 67:11 alıntı yazımı ve 67:19 ◈A gönderge cümlesi düzeltildi. DUZELTME 0.

### Aday 1041 — kayıt (sûre 67)
Kelime düzeyinde vaka yok. Kök düzeyinde sınır vakası: بصر 67:3-4 'el-basar' (insan bakışı) / 67:19 'basîr' (ilâhî). Biçimin iki anlamı: مسك (kuşları tutma / rızkı alıkoyma), 'nezîr' (uyarıcı / 1S uyarım), 'kebîr' (sapıklık / ödül), 'mubîn' (uyarıcı / sapıklık). Test yok.

### Aday 1040 — kayıt (test korpus sonunda)
66:12 / 67:1 (örnek anlatısıyla kapanış → övgüyle açılış; fâsıla ن → ر; ölçüm kökleri ortak değil). 66:9 / 67:6 'cehennem … bi'se'l-masîr'. Ardışık olmayan sıralı eşleşme (okuma bağı, 1040 değil): 23:78-79 ↔ 67:23-24. 67:30 → 68:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
30 ayetin hepsinde not yazıldı. Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1017: mevsûl göndergesi (67:1-3), 'men fi's-semâ'' (67:16-17), 1S / 1P konuşanlar, bekçiler, bölük, cehennemlikler, öncekiler, 'cund', 'qul' muhatabı — ad verilmedi; 67:9 son cümlenin konuşanı ve 67:14 'men haleqa' (fail / meful) KAPATILAMAZ.
* 1021: أيي 'eyyukum'; صبح 'mesâbîh', 'asbaha'; بأس 'bi'se'; نكب 'menâkib'; قلب ve عين ◈B tetiği kök düzeyinde.
* 1022: 67:9, 12, 26 karar sonrası geçersiz mühür; beş ayette ölçüm satırı / bilanço mühür farkı; iki ayette orta konumda geçerli mühür.
* 924: ayet 1 harf alanı (67:1); dikey وسق ×2692,9 (n=4); 67:22 fâsıla sınıf geçişi işaretsiz; kip / biçim alanı açıkları (67:2 INTG, 67:17 'em', 67:26 'innemâ').
* Kök tablosu: dikey komşuluğu karşılıksız kök çıkarabiliyor (وسق, okunmamış sûreden) — kok_ekle ile eklendi; araç değişmedi.

### Okuma ikiliği
Yok.

## SÛRE 68 KALEM SONU (2026-10-25)

**Okunan: 4115 / 6236 ayet (%66,0)** — sûre 1 ve 9-68 TAM, sûre 2 kısmi (1-20). İlerleme `kalem_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1441** (1435 → 1441; `kok_ekle_68.py`: نمم 68:11, زنم 68:13, خرطم 68:16, صرم 68:17-22, حرد 68:25, وسط 68:28). Aday havuzu **1041** (sûre 68'de yeni aday yok; `AX_kalem` boş). Bağ **AS_kalem** 74. Esmâ okuyucu kararı (KARAR) **653** (650 → 653; 0 İLÂHÎ, 3 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik beş blokta kayıtta 0 (ön kuru koşu ile; tetik satırı 2 + 0 + 1 + 1 + 3 = 7) · [x/y] **228 sayım (31 + 40 + 36 + 45 + 76), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması 0 (hedef 3, okunmamış) · **DUZELTME 0**.
Sûrenin 52 ayeti beş blokta okundu (1-10, 11-20, 21-30, 31-41, 42-52); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure68_kalem_okuma.md` (`kalem_paket_md.py`, 52 başlık). Uzak depo **dcab3d3** (oturum boyunca ilerlemedi); fark zip'i dcab3d3 tabanı, sûre 67 + 68.

### Sûre 68 bilançosu (TAM SAYIM, `okuma_metni['68']['_bilanco_sure']`)
300 kelime · **lafız 0** (sûrede lafız yok) · **Rab 10 token / 9 ayet** (68:2, 7, 19, 29, 32 ×2, 34, 48, 49, 50) · edilgen 4 (68:15, 42, 43, 49) · iltifât ölçümü 6 (68:2, 14, 22, 23, 35, 36) · hapaks 4 (68:11, 13, 16, 25 — yeni köklerin tek tokeni) · mm2 yok.
Yıldız 0:36 · ★3 · ★★3 · ★★★10 (rab 5, hapaks 4, pas 1 — içerik iddiası değil).
Fâsıla N 52 (ن / م); kafiye kırığı yok. En uzun 68:39, 68:51 (12); en kısa 68:5, 6, 18, 20, 21 (2).
Sayı işareti: 68:18 'yestesnûn' (ثني, sayı değil). Nakarat (sûre içi): 68:42/43 'da'â + ilâ + sucûd' GEÇMEZ.

### Çıpa (ölçüt değişmedi)
L4 yok; merdiven hiçbir ayette uygulanmadı (doğal olgu yok). İşaretli 8 ayet olgu=False (68:17, 22 tarım; 68:19 'tâ'if'; 68:20 teşbih; 68:34, 39, 42 âhiret; 68:49 anlatı içi olay). Tarayıcı v4 adayı 1 (68:22), kesinlik 0/1.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
3 e_oto tokeni → ilâhî 0, değil 3 (68:15 'evvel', 68:33 'el-âhira', 68:45 'metîn'). §4.3 mühür 3 → geçerli **0** (üçü karar sonrası geçersiz, 1022).

### Kendi kaydı
Kayıttan önce: 68:10'da başka geçişin sayısı [x/y] biçiminde yazılmıştı — oturum_xy yakaladı; 42-52 ARIZA karşıt çift sayımı ('beş' → 'sekiz') düzeltildi. DUZELTME 0.

### Aday 1041 — kayıt (sûre 68)
Kök قدر 67:1 'qadîr' (İLÂHÎ) / 68:25 'qâdirîn'; lemma 'metîn' 51:58 (İLÂHÎ) / 68:45 'keydî metîn'. Kökün iki anlamı: جنن ('mecnûn' / 'cenne'), أيي ('eyy' / 'âyât'), سطر ('yesturûn' / 'esâtîr'), صحب, حكم. Test yok.

### Aday 1040 — kayıt (test korpus sonunda)
67:30 / 68:1 (cevapsız soruyla kapanış → harf ve yeminle açılış); 67:2 / 68:17 'belâ'; 67:27 / 68:26 'fe-lemmâ ra'ev-'. Ardışık olmayan eşleşme (okuma bağı, 1040 değil): 52:29 / 68:2, 52:34 / 68:41, 52:40-41 / 68:46-47 (iki ardışık TAM), 52:48 / 68:48. 68:52 → 69:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
52 ayetin hepsinde not yazıldı; çift 6 ayette (68:7, 34, 35, 43, 50, 52). Karşılaştırma yapılmadı (iddia yok).

### Mevcut ailelere girenler
* 1017: 2MS muhatap, yalanlayanlar ve 'hallâf', bahçe sahipleri, 'tâ'if', 'evsatuhum', 1S / 1P konuşan, edilgen fail (68:42), 'sâhibu'l-hût', 'ellezîne keferû', 68:52 'huve' göndergesi — ad verilmedi; 68:14 'en' bağı KAPATILAMAZ.
* 1021: أيي 'eyy'; خلق 'huluq'; بني 'benîn'; أخر 'el-âhira'; جنن.
* 1022: 68:15, 33, 45 karar sonrası geçersiz mühür.
* 924: ayet 1 harf alanı (68:1); 68:10 yanlış QASEM (حلف); 68:18 sayı işareti (ثني); iltifât alıntı sınırında; 'em' / 'inne' / 'levlâ' / 'asâ' / 'lev' kip alanında yok; 68:44 biçim DIKKAT; esit2 çift yazım (68:45).
* Organ: 68:16 'hurtûm' ◈B listesinde değil — satır '—'.

### Okuma ikiliği
Yok.

## SÛRE 69 HÂKKA SONU (2026-10-26)

**Okunan: 4167 / 6236 ayet (%66,8)** — sûre 1 ve 9-69 TAM, sûre 2 kısmi (1-20). İlerleme `hakka_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1448** (1441 → 1448; `kok_ekle_69.py`: حسم, صرع 69:7; وهي 69:16; هاء 69:19; جمم — 69:14 دكك dikey komşuluğunda karşılıksız, 89:20 henüz okunmadı; قطف 69:23; وتن 69:46). Aday havuzu **1041** (sûre 69'da yeni aday yok; `AX_hakka` boş). Bağ **AS_hakka** 69. Esmâ okuyucu kararı (KARAR) **655** (653 → 655; 0 İLÂHÎ, 2 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik beş blokta kayıtta 0 (ön kuru koşu ile; tetik satırı 2 + 9 + 1 + 3 + 0 = 15) · [x/y] **200 sayım (39 + 51 + 33 + 40 + 37), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması 0 (69:21-30'da genel geçiş ilk koşuda 2, ikinci koşu 0) · **DUZELTME 0**.
Sûrenin 52 ayeti beş blokta okundu (1-10, 11-20, 21-30, 31-41, 42-52); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure69_hakka_okuma.md` (`hakka_paket_md.py`, 52 başlık). Uzak depo **dcab3d3** (oturum boyunca ilerlemedi); fark zip'i dcab3d3 tabanı, sûre 67 + 68 + 69.

### Sûre 69 bilançosu (TAM SAYIM, `okuma_metni['69']['_bilanco_sure']`)
258 kelime · **lafız 1 token / 1 ayet** (69:33) · **Rab 4 / 4 ayet** (69:10, 17, 43, 52) · A/R 0,25 · edilgen 7 (69:5, 6, 13, 14, 18, 19, 25) · iltifât ölçümü 10 · hapaks 4 (69:7, 16, 19, 46 — yeni köklerin tek tokeni) · mm2 2 (69:10, 14).
Yıldız 0:36 · ★1 (69:44 kafiye; kaynak etiketi 'n', aday 1001) · ★★3 · ★★★12 (pas 5, hapaks 4, rab 3 — içerik iddiası değil).
Fâsıla H 32 (69:1-32), N 19 (69:33-52), ل 1 (69:44 kafiye kırığı). En uzun 69:7 (15); en kısa 69:1 (1).
Sayı işareti: 69:7, 13, 14, 17, 32 gerçek sayı; 69:41, 42 'qalîl', 69:47 'ehad' sayı değil. Nakarat (sûre içi): 69:19 / 69:25 'men + âtâ + kitâb' GEÇMEZ.

### Çıpa (ölçüt değişmedi)
L4 yok. L1 5 (69:6, 7, 11, 14, 16; 69:7 sayılı süre L4 'birim' koluna sınırda, KAPATILAMAZ). Olgu değil 6 (69:5, 13, 17, 22, 23, 32). Tarayıcı v4 adayı 1 (69:7), kesinlik 0/1.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
2 e_oto tokeni → ilâhî 0, değil 2 (69:40 'kerîm', 69:47 'ehad'). §4.3 mühür 2 → geçerli **0**. 'el-azîm' (69:33, 69:52) esma_kayit token vermiyor (42:4'te veriyordu; 924).

### Kendi kaydı
Kayıttan önce: 69:22 'cenne ilk' ifadesi, 69:46 'qata'a' okunmuş / okunmamış sayısı, 69:48 'innehû' dizisi (69:49 'innâ'), 69:45 أخذ token sayımı düzeltildi; kapanış notunda karşıt çift ve kök sayıları düzeltildi. DUZELTME 0.

### Aday 1041 — kayıt (sûre 69)
Vaka yok. Kökün / biçimin iki anlamı: طغي (helâk / taşma), 'hamîm' (yakın / kaynar su), 'zirâ'' (kol / arşın), 'yemîn', 'tezkira'.

### Aday 1040 — kayıt (test korpus sonunda)
68:52 / 69:1 sûre sınırı (fâsıla ن → ة). Ardışık sûre okuma bağları (1040 değil): 68:31 / 69:5, 68:24 / 69:34, 68:8 / 69:49. Ardışık olmayan eşleşme: 54:19-20 / 69:6-7, 56:80 / 69:43, 56:95-96 / 69:51-52, 52:19 / 69:24, 52:29 / 69:42, 52:33 / 69:44. 69:52 → 70:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
52 ayetin hepsinde not; çift 8 ayette (69:7, 25, 26, 37, 39, 41, 49, 50). Karşılaştırma yapılmadı.

### Mevcut ailelere girenler
* 1017: 2MS / 2MP muhatap, 1P / 1S konuşan, edilgen failler, 'el-mu'tefikât', 'rasûl', 'el-melek', 'semâniya', kitabı sağından / solundan verilen, 'innehû' göndergesi — ad verilmedi; Semûd, 'Âd, Fir'avn metindeki adıyla.
* 1021: عود 'Âd; 'Âd ve 'asâ birleşik lemma listeleri; حمم; غلل; ذرع.
* 1022: 69:40, 69:47 karar sonrası geçersiz mühür.
* 924: ayet 1 harf alanı (69:1); esit2 çift yazım; 69:35 biçim DIKKAT; 'el-azîm' esmâ tokeni; 69:44 ★ kaynak etiketi; 69:32 / 69:33 sınıf geçişi işaretsiz.

### Okuma ikiliği
Yok.

## SÛRE 70 MEÂRİC SONU (2026-10-26)

**Okunan: 4211 / 6236 ayet (%67,5)** — sûre 1 ve 9-70 TAM, sûre 2 kısmi (1-20). İlerleme `mearic_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1451** (1448 → 1451; `kok_ekle_70.py`: هلع 70:19; عزو 70:37; وفض 70:43). Aday havuzu **1041** (sûre 70'te yeni aday yok; `AX_mearic` boş). Bağ **AS_mearic** 85. Esmâ okuyucu kararı (KARAR) **656** (655 → 656; 0 İLÂHÎ, 1 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik beş blokta kayıtta 0 (ön kuru koşu ile; tetik satırı 3 + 4 + 2 + 0 + 5 = 14) · [x/y] **168 sayım (39 + 28 + 36 + 23 + 42), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması 0 · **DUZELTME 1** (70:20).
Sûrenin 44 ayeti beş blokta okundu (1-10, 11-20, 21-30, 31-37, 38-44 — kalan 14 ayet iki yedili blok); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure70_mearic_okuma.md` (`mearic_paket_md.py`, 44 başlık). Uzak depo **dcab3d3** (oturum boyunca ilerlemedi); fark zip'i dcab3d3 tabanı, sûre 67 + 68 + 69 + 70.

### Sûre 70 bilançosu (TAM SAYIM, `okuma_metni['70']['_bilanco_sure']`)
217 kelime · **lafız 1 token / 1 ayet** (70:3) · **Rab 3 / 3 ayet** (70:27, 28, 40) · A/R 0,33 · edilgen 5 (70:11, 19, 38, 42, 44) · iltifât ölçümü 2 (70:5, 6) · hapaks 3 (70:19, 37, 43 — yeni köklerin tek tokeni) · mm2 1 (70:5).
Yıldız 0:33 · ★3 (70:11, 44 pas; 70:18 kafiye — kaynak etiketi 'n', aday 1001, kırık araç kaynaklı) · ★★2 (70:38 pas, 70:40 rab) · ★★★6 (allah 1, pas 1, rab 2, hapaks 2 — içerik iddiası değil).
Fâsıla A 10, N 24, H 5, ع 2, ج 1, ل 1, ölçümde ٓ 1 (70:18 medde işareti son harf sayılıyor; metinde ى). En uzun 70:4 (11); en kısa 2 kelime (70:7, 12, 16, 18, 22, 25).
Sayı işareti: 70:4 'hamsîn', 'elf' gerçek sayı; 70:30 'zevc' sayı değil. Nakarat (sûre içi): 70:23 / 70:34 'ellezîne hum alâ salâ…' GEÇER.

### Çıpa (ölçüt değişmedi)
L4 yok. L1 2 (70:8 gök, 70:9 dağlar). L0 1 (70:40 doğular / batılar; 37:5 emsali). Olgu değil 5 (70:4, 15, 35, 38, 43). Tarayıcı v4 adayı 1 (70:4), kesinlik 0/1. **70:4 olgu=False kaydı emsal 32:5'in eski 'L4 (ölçü) · olgu EVET' kaydıyla tutarsız — bekleyen karara eklendi.**

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
1 e_oto tokeni → ilâhî 0, değil 1 (70:7 'qarîb'). §4.3 mühür 1 → geçerli **0**.

### Kendi kaydı
Kayıttan önce: 70:8 44:45 'muhl' göndergesi, 70:3 43:33 ifadesi, 70:5 'iki sûre önce', 70:17 'tevellâ' okunmuş / okunmamış sayısı düzeltildi; 70:22 (okunmamış ayet içeriği) ve 70:26 (dayanaksız bağ) cümleleri silindi. Kayıttan sonra DUZELTME 1: 70:20 17:83 karşılığı 've'ûs' → 'ye'ûs' (aday 1003 ailesi).

### Aday 1041 — kayıt (sûre 70)
Vaka yok (70:6 / 70:7 'yeravnehû' / 'nerâhu' ve 70:19 / 70:39 'hulika' / 'halaqnâhum' — 1P adsız, sayılmadı). Kökün / biçimin iki anlamı: 'sâ'il' (70:1 / 70:25), 'hamîm', وعي (69:12 / 70:18), خير (70:21 / 70:41), شوي (18:29 / 70:16).

### Aday 1040 — kayıt (test korpus sonunda)
69:52 / 70:1 sûre sınırı (fâsıla م → ع). Ardışık sûre okuma bağları (1040 değil): 69:16 / 70:8, 69:14 / 70:9, 69:35 / 70:10, 69:12 / 70:18, 69:25 / 70:37, 69:38 / 70:40. Ardışık olmayan eşleşme: 52:7-8 / 70:1-2, 32:5 / 70:4, 21:109 / 70:6-7, 51:19 / 70:24-25, 23:5-10 / 70:29-35 (dört TAM, bir YAKIN, araya 70:33), 43:83 / 70:42 TAM, 56:60-61 / 70:41 ters, 54:7 / 70:43-44 ters, 68:43 / 70:44. 70:44 → 71:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
44 ayetin hepsinde not; çift 7 ayette (70:6, 7, 21, 31, 35, 37, 40). Karşılaştırma yapılmadı.

### Mevcut ailelere girenler
* 1017: 2MS muhatap (70:5, 36, 42), 1P / 1S konuşan, edilgen failler, soran, 'mucrim', sıfat dizisinin özneleri, inkâr edenler — ad verilmedi; Allah, melekler, rûh, 'lazâ' metindeki adıyla.
* 1021: حمم 'hamîm' (yakın dost / kaynar su); بني 'benîh' gloss 'bina'.
* 1022: 70:7 karar sonrası geçersiz mühür.
* 924: ayet 1 harf alanı (70:1); 70:18 fâsıla medde işareti; 70:7, 36, 40, 42 iltifât sayılmıyor; kip alanı (517).

### Okuma ikiliği
Yok.

### Yeni bekleyen (TAM OKUMA SONUNDA, oturumda sorulmaz)
32:5 eski çıpa kaydı ('L4 (ölçü) · olgu EVET', gaybî yükseliş) ↔ 70:4 (olgu=False, aynı kalıp). Hangisi geçerli — kullanıcı kararı.

## SÛRE 71 NÛH SONU (2026-10-26)

**Okunan: 4239 / 6236 ayet (%68,0)** — sûre 1 ve 9-71 TAM, sûre 2 kısmi (1-20). İlerleme `nuh_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1452** (1451 → 1452; `kok_ekle_71.py`: نسر 71:23, put adı). Aday havuzu **1041** (sûre 71'de yeni aday yok; `AX_nuh` boş). Bağ **AS_nuh** 70. Esmâ okuyucu kararı (KARAR) **662** (656 → 662; 1 İLÂHÎ, 5 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik üç blokta kayıtta 0 (ön kuru koşu 2 + 9 + 1 = 12 uyuşmaz, kayıttan önce dolduruldu) · [x/y] **176 sayım (60 + 50 + 66), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması 0 · **DUZELTME 2** (71:10, 71:20; aday 1017 — alıntı sınırı).
Sûrenin 28 ayeti üç blokta okundu (1-10, 11-20, 21-28); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure71_nuh_okuma.md` (`nuh_paket_md.py`, 28 başlık). Uzak depo **3c5d85c** (oturum boyunca ilerlemedi); fark zip'i 3c5d85c tabanı, yalnız sûre 71.

### Sûre 71 bilançosu (TAM SAYIM, `okuma_metni['71']['_bilanco_sure']`)
226 kelime · **lafız 7 token / 7 ayet** (71:3, 4, 13, 15, 17, 19, 25; kök أله 8 — 71:23 'âlihe') · **Rab 5 / 5 ayet** (71:5, 10, 21, 26, 28) · A/R 1,4 · edilgen 2 (71:4, 25) · iltifât ölçümü 0 · hapaks 1 (71:23 نسر — yeni kök) · mm2 3 (71:7 كبر, 71:18 خرج, 71:22 مكر).
Yıldız 0:18 · ★2 (71:15 allah, 71:26 rab) · ★★2 (71:5 rab, 71:13 allah) · ★★★6 (allah 3, rab 1, hapaks 1, pas 1 — içerik iddiası değil).
Fâsıla N 4 (71:1 م, 71:2-4 ن), A 24 (71:5-28 ا); ölçüm kafiye kırığı 0 — 71:1 → 2 ve 71:4 → 5 geçişleri işaretsiz (sûre 64 dersi). En uzun 71:4 (18); en kısa 3 kelime (71:14, 71:22).
Sayı işareti: 71:15 'seb'' gerçek sayı; 71:24 'kesîr' sayı değil. Nakarat (sûre içi): 71:24 / 71:28 'lâ tezidi'z-zâlimîne illâ' GEÇER; 71:21 / 71:26 'qâle nûhun rabbi' GEÇMEZ.

### Çıpa (ölçüt değişmedi)
L4 yok. L1 8 (71:7 organ + eylem; 71:11 gök + yağış; 71:14 evreler; 71:15 yedi gök kat kat — 67:3 emsali, L4 sınıf / ölçü koluna sınırda, KAPATILAMAZ; 71:16 ay / güneş; 71:17 yerden bitirilme; 71:19 yer; 71:20 yollar). L0 4 (71:4 ecel; 71:5 gece / gündüz; 71:12 bahçe, ırmak; 71:27 doğurma). Olgu değil 2 (71:18 diriliş — yere dönüş kolu sınır vakası; 71:25 boğulma cezası ve ateş). Tarayıcı v4 adayı 2 (71:4, 71:15), kesinlik 0/2.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
6 e_oto tokeni → ilâhî 1 (71:10 'ğaffâr'), değil 5 (71:2 'mubîn', 71:16 'nûr', 71:25 'nasîr', 71:28 'mu'min' ×2). §4.3 mühür 4 → geçerli **1** (71:10; ölçüm satırı 'MÜHÜRSÜZ' — 1022).

### Kendi kaydı
Kayıttan önce: 71:6 'du'â'' okunmuş / okunmamış sayısı; 71:10 basılmamış xref ayet numaraları; 71:19 'lafız sûre içi' → 'blok içi'; 71:15 ◈B notu, 71:23 ve 71:25'te ders adı olarak yazılmış basılmamış ayet numaraları → numarasız. Kayıttan sonra DUZELTME 2 (aday 1017): 71:10 meali alıntıyı kapatıyordu (alıntı 71:11-12'de sürüyor); 71:20 meali okunmamış ayete dayanarak alıntıyı kapatıyordu.

### Aday 1041 — kayıt (sûre 71)
Üç vaka: lemma 'ce'ale' (71:7 kavim / 71:12, 16, 19 Allah); lemma 'zâde' (71:6 çağrı, 71:21 mal ve çocuk / 71:24, 71:28 Rab); lemma 'vezera' (71:23 kavim / 71:26-27 Rab). Kökün iki anlamı: نهر (71:5 gündüz / 71:12 ırmak), نور (71:16 ışık / 71:25 ateş).

### Aday 1040 — kayıt (test korpus sonunda)
70:44 / 71:1 sûre sınırı (fâsıla ن → م). Ardışık olmayan eşleşme — bölünme düzeni (okuma bağı): 11:25 / 71:1-2; 14:10 ve 11:3 / 71:4, 71:10; 11:52 / 71:10-11; 20:55 / 71:17-18; 20:53, 43:10 / 71:19-20; ayrıca 63:11 / 71:4, 2:19 / 71:7, 11:5 / 71:7, 9; 10:5 / 71:16; 67:3 / 71:15; 14:36 / 71:21, 24; 21:89 / 71:26; 14:41 / 71:28. 71:28 → 72:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
28 ayetin hepsinde not; çift 8 ayette (71:4, 5, 9, 16, 18, 21, 27, 28), ayetler arası 71:8 / 71:9. Karşılaştırma yapılmadı.

### Mevcut ailelere girenler
* 1017: 1P gönderen, 'qâle' 3MS (71:2, 5), 2MS muhatap Rab, 'men' (71:21), 71:22-23 konuşanlar, 71:24 'edallû' öznesi, edilgen failler — ad verilmedi; Nûh, Allah, Rab, beş put adı metindeki adıyla.
* 1021: طور 'atvâr' gloss 'Tûr dağı'; بني 'benîn' gloss 'bina'; نهر 71:5 gloss 'ırmak'; ودد / سوع put adları kök glossuyla (özel ad iskeleti bekleyen kararına ek vaka); lemma 'asâ' eşsesli — kök sayısı verildi.
* 1022: 71:10 geçerli mühür, ölçüm 'MÜHÜRSÜZ'.
* 924: ayet 1 harf alanı (71:1); iki işaretsiz fâsıla geçişi; iltifât konuşma katmanı değişimlerini saymıyor; kip alanı (517) tekit, harfsiz nidâ, meczûm cevap, ta'lîl, 71:23 nehy.

### Okuma ikiliği
Yok.

### Yeni bekleyen (TAM OKUMA SONUNDA, oturumda sorulmaz)
Yok. (gloss_gecis özel ad iskeleti çakışması kararına sûre 71 put adları ek vaka olarak eklendi.)

## SÛRE 72 CİN SONU (2026-10-26)

**Okunan: 4267 / 6236 ayet (%68,4)** — sûre 1 ve 9-72 TAM, sûre 2 kısmi (1-20). İlerleme `cin_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1458** (1452 → 1458; `kok_ekle_72.py`: حرس 72:8; هرب 72:12; حري 72:14; حطب 72:15; غدق 72:16; لبد 72:19). Aday havuzu **1041** (sûre 72'de yeni aday yok; `AX_cin` boş). Bağ **AS_cin** 59. Esmâ okuyucu kararı (KARAR) **670** (662 → 670; 1 İLÂHÎ, 7 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik üç blokta kayıtta 0 (ön kuru koşu 6 + 3 + 2 = 11 uyuşmaz, kayıttan önce dolduruldu) · [x/y] **201 sayım (71 + 61 + 69), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması 0 · **DUZELTME 0**.
Sûrenin 28 ayeti üç blokta okundu (1-10, 11-20, 21-28); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure72_cin_okuma.md` (`cin_paket_md.py`, 28 başlık). Uzak depo **3c5d85c** (oturum boyunca ilerlemedi); fark zip'i 3c5d85c tabanı, sûre 71 + 72.

### Sûre 72 bilançosu (TAM SAYIM, `okuma_metni['72']['_bilanco_sure']`)
285 kelime · **lafız 10 token / 8 ayet** (72:4, 5, 7, 12, 18 ×2, 19, 22, 23 ×2) · **Rab 8 / 8 ayet** (72:2, 3, 10, 13, 17, 20, 25, 28) · A/R 1,25 · edilgen 5 (72:1, 8, 10, 24, 25) · iltifât ölçümü 2 (72:18, 19) · hapaks 4 (72:8, 12, 14, 16 — yeni köklerin tek tokeni) · mm2 0.
Yıldız 0:13 · ★6 · ★★4 · ★★★5 (hapaks 4, allah 1 — içerik iddiası değil).
Fâsıla A 28 (sûrenin tamamı ا; 71:5'ten bu yana kesintisiz); ölçüm kafiye kırığı 0. En uzun 72:23 (16); en kısa 72:15 (5).
Sayı işareti: 'ehad' ×6 sayı değil; 'eqall', ''aded' nicelik. Nakarat (sûre içi): 'ennâ zanennâ en len' 72:5 / 72:12; 'zanne en len' 72:5, 7, 12 — GEÇER.

### Çıpa (ölçüt değişmedi)
L4 yok. L1 3 (72:8 gök + alevler, 72:9 alev + gözetleme — 37:10 emsali; 72:16 su + içirme, şarta bağlı — 56:68 emsali). Olgu değil 5 (72:15, 23, 24, 25, 28). Tarayıcı v4 adayı 3 (72:16, 23, 24), kesinlik 0/3.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
8 e_oto tokeni → ilâhî 1 (72:26 ''âlim'), değil 7 ('ehad' ×6, 72:25 'qarîb'). §4.3 mühür 7 → geçerli **0** (72:26'da İLÂHÎ token ORTA, son token DEĞİL).

### Kendi kaydı
Kayıttan önce: 72:5 yazım hatası; 72:20 basılmamış ayet numarası ders adı olarak — numarasız. Süreç hatası: 72:1-10 kayıt yaması assert'te durunca blok betiği boş kayıtla bir kez koştu, sunumdan önce yeniden koşuldu (ARIZA'da). Kayıttan sonra DUZELTME 0.

### Aday 1041 — kayıt (sûre 72)
Vaka yok ('ehad' altı geçişte de 'hiç kimse'; 'de'â' insan / kul fiili; 'seleke' iki geçişte Rab). Kökün iki kullanımı: 'tarîqa' (72:11 gruplar / 72:16 yol).

### Aday 1040 — kayıt (test korpus sonunda)
71:28 / 72:1 sûre sınırı (fâsıla ا → ا). Ardışık sûre okuma bağı 71:20 / 72:17 (سلك). 72:28 → 73:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
28 ayetin hepsinde not; ayet içi çift 11 ayette, ayetler arası 2. Karşılaştırma yapılmadı.

### Mevcut ailelere girenler
* 1017: 'qul' muhatabı / 1S konuşan, cin 'nefer', gruplar, 1P içiren / sınayan, 'abdu'llâh' (izâfet), elçi(ler), gözetleyiciler — ad verilmedi. Konuşan katmanı sınırları metinde işaretli değil — KAPATILAMAZ.
* 1021: جدد 'cedd' gloss 'yenilik'.
* 1022: yedi ölçüm mührünün yedisi karar sonrası geçersiz.
* 924: ayet 1 harf alanı; 'ehad' sayı işareti ×6; iltifât 72:7 ve 72:16'yı saymıyor; kip alanı (517) 'enne' tekidi, 'kemâ', 'em', 'innemâ' hasrı, ta'lîl.

### Okuma ikiliği
Yok.

### Yeni bekleyen (TAM OKUMA SONUNDA, oturumda sorulmaz)
Yok.

## SÛRE 73 MÜZZEMMİL SONU (2026-10-26)

**Okunan: 4287 / 6236 ayet (%68,7)** — sûre 1 ve 9-73 TAM, sûre 2 kısmi (1-20). İlerleme `muzzemmil_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1465** (1458 → 1465; `kok_ekle_73.py`: زمل 73:1; نصف 73:3; بتل 73:8; نكل 73:12; غصص 73:13; كثب, هيل 73:14). Aday havuzu **1041** (sûre 73'te yeni aday yok; `AX_muzzemmil` boş). Bağ **AS_muzzemmil** 42. Esmâ okuyucu kararı (KARAR) **673** (670 → 673; 3 İLÂHÎ, 0 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik üç blokta kayıtta 0 (ön kuru koşu 3 + 3 + 1 = 7 uyuşmaz, kayıttan önce dolduruldu) · [x/y] **135 sayım (43 + 47 + 45), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması hedefli 0, genel geçiş 1 (30:4 mercek — نصف karşılıksız anma; ikinci koşu 0) · **DUZELTME 0**.
Sûrenin 20 ayeti üç blokta okundu (1-10, 11-19, 20 — 73:20 uzun ayet tek başına); ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure73_muzzemmil_okuma.md` (`muzzemmil_paket_md.py`, 20 başlık). Uzak depo **3c5d85c** (oturum boyunca ilerlemedi); fark zip'i 3c5d85c tabanı, sûre 71 + 72 + 73.

### Sûre 73 bilançosu (TAM SAYIM, `okuma_metni['73']['_bilanco_sure']`)
199 kelime · **lafız 7 token / 1 ayet** (yalnız 73:20) · **Rab 4 / 4 ayet** (73:8, 9, 19, 20) · A/R 1,75 · edilgen 0 · iltifât ölçümü 4 (73:6, 7, 14, 15) · hapaks 4 (73:1, 8, 13, 14 — yeni kökler; 73:14'te iki) · mm2 2 (73:10, 16).
Yıldız 0:13 · ★★2 · ★★★5 (hapaks 4, n 1 — içerik iddiası değil).
Fâsıla ل 1 (73:1) · A 18 (73:2-19) · N 1 (73:20 'rahîm'); ölçüm kafiye kırığı 0 — iki geçiş işaretsiz (924). En uzun 73:20 (78); en kısa 73:1 (2).
Sayı işareti: 'qalîl' 73:2, 3, 11 nicelik; 'nisf' 73:3, 20 ve 'sulus' ×2 73:20 kesir. Nakarat: ayet içi 73:20 ('fe'qra'û mâ teyessera' ×2, ''alime en' ×2, 've âharûne' ×2); nakarat3 alanı boş.

### Çıpa (ölçüt değişmedi)
L4 yok. L1 4 (73:3 gecenin yarısı, birim yok; 73:14 yer ve dağlar — 69:14 ailesi; 73:18 göğün yarılması; 73:20 'yuqaddiru'l-leyle ve'n-nehâr' — 36:39 emsali, KAPATILAMAZ). L0 4 (73:2, 6, 7 gece / gündüz; 73:9 doğu / batı tekil). Olgu değil 3 (73:12, 13, 17). Tarayıcı v4 adayı 2 (73:3, 20), kesinlik 0/2.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
3 e_oto tokeni → ilâhî 3 (73:9 'vekîl'; 73:20 'ğafûr', 'rahîm'), değil 0. §4.3 mühür 2 → geçerli **2** (73:9, 73:20), ton cemâl 2. 73:9'da ölçüm satırı 'SON konum, MÜHÜRSÜZ' / esma_kayit geçerli — ayrışma (1022 ailesi).

### Kendi kaydı
Kayıttan önce: 73:9 ◈K satırı tetiksizken dolu yazılmıştı → '—' (oturum_tetik 1 → 0). Kayıttan sonra DUZELTME 0.

### Aday 1041 — kayıt (sûre 73)
Vaka yok. Kökün iki kullanımı: سمو 'ism' 73:8 / 'semâ'' 73:18; قوم 'qum' / 'aqvem' / 'aqîmû'.

### Aday 1040 — kayıt (test korpus sonunda)
72:28 / 73:1 sûre sınırı (fâsıla ا → ل). Ardışık sûre okuma bağı 72:28 / 73:20 ('ahsâ'). 73:20 → 74:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
20 ayetin hepsinde not; ayet içi çift 3 ayette (73:9, 17, 20), ayetler arası 2 (73:3 / 4, 73:6 / 7). Karşılaştırma yapılmadı.

### Mevcut ailelere girenler
* 1017: 'el-muzzemmil' (sıfatla), 1P / 1S konuşan, yalanlayanlar, 2MP muhatap, elçi, 'tâ'ife', hastalar / yolcular / savaşanlar — ad verilmedi. Konuşan katmanı sınırları metinde işaretli değil — KAPATILAMAZ.
* 1021: نهر 'nehâr' gloss 'ırmak'; مهل 'mehhil' / 'muhl' eşsesli birleşme (kök sayımı verilmedi); وبل gloss '(vebîl; 7 ayet)' kök sayısını lemmaya yazıyor.
* 1022: 73:9 ölçüm satırı / esma_kayit mühür ayrışması.
* 924: ayet 1 harf alanı; fâsıla geçişleri işaretsiz ×2; iltifât 73:11, 73:12, 73:20 içi geçişleri saymıyor; kip alanı (517) 'inne' tekidi; 'kemâ' biçim alanında yok; ayet içi tekrar nakarat3'te yok; hizb işareti ölçüm dışı.

### Okuma ikiliği
Yok.

### Yeni bekleyen (TAM OKUMA SONUNDA, oturumda sorulmaz)
Yok.

## SÛRE 74 MÜDDESSİR SONU (2026-10-27)

**Okunan: 4343 / 6236 ayet (%69,6)** — sûre 1 ve 9-74 TAM, sûre 2 kısmi (1-20). İlerleme `muddessir_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1470** (1465 → 1470; `kok_ekle_74.py`: دثر 74:1; نقر 74:8; عبس, بسر 74:22; قسر 74:51). Aday havuzu **1041** (sûre 74'te yeni aday yok; `AX_muddessir` boş). Bağ **AS_muddessir** 116. Esmâ okuyucu kararı (KARAR) **675** (673 → 675; 0 İLÂHÎ, 2 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik yedi blokta kayıtta 0 (ön kuru koşu 1 uyuşmaz — 74:50 ◈B, kayıttan önce '—') · [x/y] **178 sayım (21 + 26 + 22 + 29 + 26 + 22 + 32), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması hedefli 0, genel 0 · **DUZELTME 1** (74:35 meal).
Sûrenin 56 ayeti yedi blokta okundu (1-10, 11-20, 21-30, 31, 32-40, 41-48, 49-56 — 74:31 uzun ayet tek başına); oturum iki güne yayıldı (ortam korundu). Ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure74_muddessir_okuma.md` (`muddessir_paket_md.py`, 56 başlık). Uzak depo **51adf3a** (oturum boyunca ilerlemedi); fark zip'i 51adf3a tabanı, sûre 74.

### Sûre 74 bilançosu (TAM SAYIM, `okuma_metni['74']['_bilanco_sure']`)
255 kelime · **lafız 3 token / 2 ayet** (74:31 ×2, 74:56) · **Rab 3 / 3 ayet** (74:3, 7, 31 — üçü de 2MS izâfetli) · A/R 1,0 · edilgen 6 (74:8, 19, 20, 24, 31, 52) · iltifât ölçümü 2 (74:8, 11) · hapaks 2 (74:1, 51 — yeni kökler) · mm2 1 (74:31).
Yıldız 0:44 · ★2 · ★★4 · ★★★6 (hapaks 2, rab 2, pas 1, n 1 — içerik iddiası değil); ★ ikisi (74:15, 42) kaynak 'n' yanlış etiketli, gerçekte kafiye kırığı (1001).
Fâsıla R 31 · N 10 · H 8 · A 6 · د 1; ölçüm kafiye kırığı 2 (74:15, 42), işaretsiz geçiş 5 (924). En uzun 74:31 (57); en kısa 14 ayet (2 kelime).
Sayı işareti: 74:30 'tis'a ''aşer' gerçek (on dokuz); 74:6, 11, 31, 35 sayı değil. Nakarat3: 74:19 / 20, 74:24 / 25.

### Çıpa (ölçüt değişmedi)
L4 yok. L1 2 (74:33 gecenin gidişi, 74:34 sabahın ağarması — süreç adı). L0 1 (74:32 ay, kasem nesnesi). Olgu değil 17 (74:4 elbise; âhiret / gaybî 14; 74:50-51 teşbih aracı). Tarayıcı v4 adayı 2 (74:30, 31 — gaybî sayı), kesinlik 0/2.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
2 e_oto tokeni → ilâhî 0, değil 2 (74:31 'mu'min' insan çoğulu; 74:53 'el-âhira'). §4.3 mühür 1 (74:53) → geçerli **0**.

### Kendi kaydı
Kayıttan önce: 74:10 okunmuş / okunmamış sayısı; 74:39 metin dışı karşıt çift → 'yok'; 74:50 ◈B tetiksiz dolu → '—'; esma_el yorumunda basılmamış emsal numarası → numarasız. Kayıttan sonra: DUZELTME 1 (74:35 meal '(Sekar)' göndergeyi kapatıyordu — aday 1017). ARIZA satırlarında basılmamış ayet numarasıyla ders adı iki kez (21-30, 32-40): ARIZA ayet anahtarı taşımadığı için DUZELTME dışı — özgün satır korunup ek ARIZA satırıyla işaretlendi, blok betiği yalnız bilanço için yeniden koşuldu (ayet kayıtları değişmedi, karşılaştırmayla doğrulandı). Süreç: 21-30'da heredoc içi yama assert'te durdu, ardından ayrı satırlı komutlar koştu (dosya değişmedi) — sonraki bütün yamalar ayrı dosya + && zinciri.

### Aday 1041 — kayıt (sûre 74)
'qaddara' 73:20 Allah / 74:18-20 insan; 'şâ'e' 74:31, 56 Allah / 74:37, 55 insan; 'erâde' 74:31 Allah / 74:52 insan; 'ehl' 11:81 insan / 74:56 Allah; 'mu'min' 74:31 insan çoğulu (esmâ listesinde; Allah için geçişi bu oturumda basılmadı).

### Aday 1040 — kayıt (test korpus sonunda)
73:20 / 74:1 sûre sınırı (fâsıla م → ر). Ardışık sûre açılışı 73:1-2 / 74:1-2 (nidâ + 'örtünen' sıfatı + 'qum' — iki ayetlik sıralı eşleşme). Ardışık sûre okuma bağları: 73:10 / 74:5, 7; 73:11 / 74:11; 73:15 / 74:13; 73:20 / 74:18; 73:19 / 74:54-55; 73:20 / 74:56 (iki sûre sonu lafız + غفر). 74:56 → 75:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
56 ayetin hepsinde not; ayet içi çift 2 ayette (74:31 üç çift, 74:37), ayetler arası 2 (74:9 / 10, 74:33 / 34). Karşılaştırma yapılmadı.

### Mevcut ailelere girenler
* 1017: 'el-muddessir' (sıfatla), 1S / 1P konuşan, tek yaratılan kişi, suçlular, sağın ehli, on dokuzun sayılanı — ad verilmedi. Zamir göndergeleri KAPATILAMAZ (74:31 'hiye', 74:35 'innehâ', 74:54 'innehû').
* 1021: أيي 'eyyuhâ' / 'âyât' gloss ve kök birleşmesi; بني 'benîn'; مهد fiil; سكن 'miskîn'.
* 1001: 74:15, 74:42 yıldız kaynağı etiketi.
* 1038 ailesi: 74:27 Sekar rol 'fail'.
* 924: ayet 1 harf alanı; fâsıla geçişleri işaretsiz ×5; iltifât 1S / 1P / 2MS / 2MP geçişleri; tahsis, kasem, 'ke-enne' biçim alanında yok; hâl fiili kipi; bileşik sayı iki işaret; ayet içi tekrar nakarat3'te yok; nakarat3 tür etiketi tutarsız.
* Meal / lemma: 74:29 'li'l-beşer' (deri / insan) KAPATILAMAZ; 74:47 '(ölüm)'; 74:51 'qasvera'.

### Okuma ikiliği
Yok.

### Yeni bekleyen (TAM OKUMA SONUNDA, oturumda sorulmaz)
Yok. (Süreç kaydı: ARIZA alanı DUZELTME mekanizmasının dışında — bu oturumda ek ARIZA satırıyla işaretlendi.)

## SÛRE 75 KIYÂME SONU (2026-10-27)

**Okunan: 4383 / 6236 ayet (%70,3)** — sûre 1 ve 9-75 TAM, sûre 2 kısmi (1-20). İlerleme `kiyame_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1475** (1470 → 1475; `kok_ekle_75.py`: بنن 75:4; حرك 75:16; نضر 75:22; ترق 75:26; سدي 75:36). Aday havuzu **1041** (sûre 75'te yeni aday yok; `AX_kiyame` boş). Bağ **AS_kiyame** 75. Esmâ okuyucu kararı (KARAR) **676** (675 → 676; 0 İLÂHÎ, 1 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik dört blokta 0 (ön kuru koşu da 0) · [x/y] **108 sayım (31 + 25 + 24 + 28), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması hedefli 0, genel 0 · **DUZELTME 1** (75:3 mercek, aday 924).
Sûrenin 40 ayeti dört blokta okundu (1-10, 11-20, 21-30, 31-40); oturum tek gün. Ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure75_kiyame_okuma.md` (`kiyame_paket_md.py`, 40 başlık). Uzak depo **0593b8e** (oturum boyunca ilerlemedi); ara zip `fark_0593b8e_sure75_ara1.zip` (1-20), son zip `fark_0593b8e_sure75.zip`.

### Sûre 75 bilançosu (TAM SAYIM, `okuma_metni['75']['_bilanco_sure']`)
164 kelime · **lafız 0** · **Rab 3 / 3 ayet** (75:12, 23, 30 — üçü de 'ilâ' + Rab) · A/R 0 · edilgen 6 (75:9, 13, 25, 27, 36, 37) · iltifât ölçümü 8 (75:12, 13, 20, 23, 30, 31, 34, 36) · hapaks 4 (75:16, 26, 33, 36) · mm2 0.
Yıldız 0:25 · ★4 · ★★2 · ★★★9 (hapaks 4, rab 3, pas 2 — içerik iddiası değil); ★ üçü (75:34, 35, 39) kaynak 'n' yanlış etiketli, gerçekte sahte kafiye kırığı (1001).
Fâsıla (metin) ة 10 · ه 8 · ر 7 · ى 11 · ق 4; ölçüm kafiye kırığı 5 (75:16, 33, 34, 35, 39) beşi de medde artefaktı, sahte; gerçek sınıf geçişleri işaretsiz ×5 (924). En uzun 75:40 (7); en kısa 75:8, 75:21 (2).
Sayı işareti: 75:39 'zevc' — ikil, çift adı, sayım değil. Nakarat3: 75:4 / 40, 75:12 / 30 (esit2 BENZER), 75:34 / 35.

### Çıpa (ölçüt değişmedi)
L4 yok. L1 7: 75:8 ayın tutulması, 75:9 güneş ve ayın toplanması (âhiretteki kozmik olay); 75:26 köprücük kemikleri, 75:29 bacak (ölüm anı + organ adı; 75:29 mecaz okuması da açık); 75:37 nutfe / meni + dökülme, 75:38 'alaqa → yaratma → düzenleme, 75:39 iki eş (oluşum dizisi; 75:39 L4 sınıf kolu sınır vakası, 799). Olgu değil 17. Tarayıcı v4 adayı 1 (75:5 — فجر kökü, fucûr), kesinlik 0/1.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
1 e_oto tokeni → ilâhî 0, değil 1 (75:21 'el-âxira'). §4.3 mühür 1 (75:21) → geçerli **0**.

### Kendi kaydı
Kayıttan önce: 75:2 'nefs' sayı satırı ve 75:10 'el-insân' listesi ('sûre içi' → 'blok içinde'); 75:38 mercekte yazım. Kayıttan sonra: DUZELTME 1 (75:3 merceği 'iltifât ayet içi sayılıyor' — yanlış gerekçe; ölçüm iltifâtı önceki ayetle şahıs kümesi AYRIKSA 1, tekil / çoğul ayırmıyor; aday 924). Aynı gerekçe 1-10 ARIZA'sında da vardı — ARIZA DUZELTME dışı, özgün satır korunup 11-20 ARIZA'sına ek satırla işaretlendi (ayet kayıtları değişmedi). Süreç: bütün yamalar ayrı dosya + && zinciri; BASLIK çapası her blokta grep ile alındı.

### Aday 1041 — kayıt (sûre 75)
Sûre içi Allah / insan ortak kelime kaydı yok ('sevvâ' 75:4 / 38 ve 'qâdir' 75:4 / 40 ikisi de insan dışı gönderge). Ardışık sûre okuma bağı: 'ehl' 74:56 Allah / 75:33 insanın ailesi (1041 sûre içi kaydının dışında).

### Aday 1040 — kayıt (test korpus sonunda)
74:56 / 75:1 sûre sınırı (lafız + iki 'ehl' izâfetiyle kapanış / lafızsız 1S yeminle açılış; fâsıla ة → ة). Ardışık sûre okuma bağları: 74:32 / 75:8 'qamar'; 74:53 / 75:11, 20 'kellâ (bel)'; 74:22 / 75:24 بسر kökünün korpustaki iki geçişi; 74:43 / 75:31 namaz kılmama; 74:56 / 75:33 'ehl'. 75:40 → 76:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
40 ayetin hepsinde not; ayet içi çift 4 ayette (75:9, 13, 39, 40), ayetler arası 4 (75:3 / 4, 75:20 / 21, 75:22 / 24, 75:31 / 32). Karşılaştırma yapılmadı.

### Mevcut ailelere girenler
* 1017: adsız konuşan (1S yemin, 1P), muhatap 2MS / 2MP, adsız 3MS, 'qîle' söyleyeni — ad verilmedi. Zamir göndergeleri KAPATILAMAZ (75:16-19, 75:26, 75:28, 75:38, 75:39); meal parantezsiz.
* 1021: أمم 'emâm'; فجر 'fucûr'; وزر 'wazar'; فقر 'fâqira'; سوق 'sâq'; مطو 'yetemettâ'; مني iki anlam. Eşsesli lemma şüphesi: 'yefcur', 'evlâ' — sayı iddiası yok.
* 1001: 75:34, 35, 39 yıldız kaynağı etiketi.
* 924: ayet 1 harf alanı (75:1); medde artefaktı (4 ayet + 1 ardıl); işaretsiz fâsıla geçişleri ×5; iltifât tanımı (tekil / çoğul ayrımı yok, ayrıklık şartı); 'lâ uqsimu' 'lâ'sı NEG; 'belâ', haber takdimi, 'inne 'aleynâ' tekidi, 'lâkin' biçim alanında yok.
* ◈K / ◈B: عظم, بنن, لسن, ترق, سوق, وجه tetik listesinde değil — '—', gözlem ◇'de.

### Okuma ikiliği
75:27 'râq' (tedavi eden / yükselten) ve 75:14 i'râbı KAPATILAMAZ.

### Yeni bekleyen (TAM OKUMA SONUNDA, oturumda sorulmaz)
Yok. (Süreç kaydı: iltifât alanının tanımı — önceki ayetle şahıs kümesi ayrıklığı, tekil / çoğul ayrımı yok — 924 ailesine kayıt.)

## SÛRE 76 İNSÂN SONU (2026-10-27)

**Okunan: 4414 / 6236 ayet (%70,8)** — sûre 1 ve 9-76 TAM, sûre 2 kısmi (1-20). İlerleme `insan_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1478** (1475 → 1478; `kok_ekle_76.py`: مشج 76:2; قمطر 76:10; زمهر 76:13). Aday havuzu **1041** (sûre 76'da yeni aday yok; `AX_insan` boş). Bağ **AS_insan** 69. Esmâ okuyucu kararı (KARAR) **683** (676 → 683; 2 İLÂHÎ, 5 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik üç blokta 0 (ön kuru koşu da 0; sûre geneli 31 / 0) · [x/y] **165 sayım (59 + 46 + 60), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması hedefli 0, genel 0 · **DUZELTME 0**.
Sûrenin 31 ayeti üç blokta okundu (1-10, 11-20, 21-31); oturum tek gün (sûre 75 ile aynı oturum). Ek mercekler ve 'Karşıt çift (aday 1039, okuma)' notu sûrenin tamamında. Paket `notlar/sure76_insan_okuma.md` (`insan_paket_md.py`, 31 başlık). Uzak depo **0593b8e** (oturum boyunca ilerlemedi); ara zip `fark_0593b8e_sure76_ara1.zip` (1-20), son zip `fark_0593b8e_sure76.zip`.

### Sûre 76 bilançosu (TAM SAYIM, `okuma_metni['76']['_bilanco_sure']`)
243 kelime · **lafız 5 / 4 ayet** (76:6, 9, 11, 30 ×2) · **Rab 5 / 5 ayet** (76:10, 21, 24, 25, 29) · A/R 1,0 · edilgen 5 (76:14, 15, 17, 18, 21) · iltifât ölçümü 4 (76:5, 9, 11, 21) · hapaks 3 (76:2, 10, 13 — üçü de yeni kök) · mm2 3 (76:6, 8, 16).
Yıldız 0:17 · ★1 · ★★6 · ★★★7 (hapaks 3, pas 2, rab 1, allah 1 — içerik iddiası değil); 1001 etiket düzeltmesi gerekmedi.
Fâsıla 31 ayetin 31'i ا; kafiye kırığı 0. En uzun 76:21 (13); en kısa 76:18 (4).
Sayı işareti: 76:31 'e'adde' (hazırlamak) — yanlış pozitif. Nakarat3: 76:5 / 17. Esit2: 76:29 → 73:19 TAM.

### Çıpa (ölçüt değişmedi)
L4 yok. L0 3: 76:1 insanın anılmadığı zaman dilimi; 76:25 sabah / akşamüstü, 76:26 gece (zaman zarfı, 71:5 emsali; 76:26 L1 sınır vakası). L1 2: 76:2 nutfe + karışım + işitme / görme yetileri (L2 sınır vakası); 76:28 yaratma + bağların sağlamlaştırılması. Olgu değil 19 (âhiret / cennet / insan yapımı araç). Tarayıcı v4 adayı 0.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
7 e_oto tokeni → ilâhî 2 (76:30 'alîm, hakîm), değil 5 (76:2 semî', basîr; 76:3 şâkir; 76:5 berr; 76:20 kebîr). §4.3 mühür 4 (76:2, 3, 20, 30) → geçerli **1** (76:30, ton denge).

### Kendi kaydı
Kayıttan önce: 76:6 ''ibâdu'llâh korpusta 1' iddiası (sayımla 7 ayet); 76:1 okunmuş 'hel etâ' ayetleri hakkında toplu içerik iddiası silindi; 76:12 'sabera' sayı satırı; 76:30 xref dış düğümleri basılan / okunmamış ayrıldı; 76:24-26'da anılan 18:28, 33:48, 68:10, 71:5 emsal listesinde basıldı. Kayıttan sonra: yok. Sunum dersi: 76:1-10 yanıtı yarıda kesildi; okuma bloktan itibaren SendUserMessage parçalarıyla verildi.

### Aday 1041 — kayıt (sûre 76)
جزي 76:9 'cezâ'' (iyilerin insanlardan istemediği karşılık) / 76:12 'cezâhum' (Allah'ın karşılığı) / 76:22 'cezâ'' (konuşan adsız). Lemma 'şâ'e' 76:28 (1P), 76:29 (dileyen), 76:30 (2MP ve Allah), 76:31 (fail 3MS, okuma: lafız). شكر 76:3 'şâkir' (insan) / 76:22 'meşkûr' (fail adsız) — KAPATILAMAZ, kayıt değil. Sûre dışı aile (okuma): 42:11 / 76:2 'semî' + basîr'; 36:38 / 76:16 'taqdîr'; 12:41 / 76:21 'seqâ + rabb'.

### Aday 1040 — kayıt (test korpus sonunda)
75:40 / 76:1 sûre sınırı (iki yan da soru; fâsıla ى → ا). Ardışık sûre okuma bağları: 75:36-37 / 76:1-2 'el-insân' + 'nutfe' aynı sırada; 75:37 / 76:2 نطف; 75:5 / 76:6 فجر iki anlam; 75:22 / 76:11 نضر; 75:20-21 / 76:27 'yuhibbûne'l-'âcile' + bırakılan (âxira / ağır gün). 76:31 → 77:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
31 ayetin hepsinde not; ayet içi çift 6 ayette (76:3, 13, 25, 27, 30, 31), ayetler arası 2 (76:4 / 5, 76:10 / 11). Karşılaştırma yapılmadı.

### Mevcut ailelere girenler
* 1017: adsız konuşan 1P (76:2-4, 76:23-28), iyilerin işaretsiz alıntısı (76:9-10; kapanış metinle 76:11), muhatap 2MS (76:19-20, 23-26), 2MP (76:22, 30) — ad verilmedi. 76:22 sözün sahibi / alıntı olup olmadığı; zamir / gönderge (76:8, 16, 24 / 27, 29); i'râb (76:6, 14, 21, 31) KAPATILAMAZ.
* 1021: كفر 'kâfûr'; طير 'mustetîr'; غلل üç anlam; سرر 'surûr'; ظلل 'zılâl'; أني 'âniye'; قرر 'qavârîr'; أسر 'esîr' / 'esr'; عدد 'e'adde'. Eşsesli lemma şüphesi: 'berr' — sayı iddiası yok.
* 1022: esma_kayit 'mühür EVET' ölçüm konumundan (76:2, 3, 20); geçerli yalnız 76:30.
* 924: ayet 1 harf alanı (76:1); iltifât tanımı ve konuşan katmanı (76:2-4 / 76:9-10 / 76:23-28 1P ölçümde aynı '1'; 76:19, 22, 23 geçişleri 0); 'innemâ' hasrı, 'innâ' tekidi, 'hasibtehum' benzetmesi biçim alanında yok.
* ◈K / ◈B: 76:18 سمو 'tusemmâ', 76:25 سمو 'ism', 76:20 نعم 'na'îm' S1 lemma kısıtıyla tetiklemiyor — '—'.

### Okuma ikiliği
76:22 2MP hitabı (iyilere âhirette mi, okuyuculara mı) ve 76:16 'qavârîra min fidda' (cam / gümüş) KAPATILAMAZ.

### Kullanıcı sorusu (kayıt)
75:39 'zevceyn → ez-zeker ve'l-unsâ' — bedel sırası okuması verildi; 53:45 / 51:49 / 49:13 → 75:39 okuma bağı önerildi; kullanıcı onayıyla AS_kiyame'ye yazıldı (53:45 zaten ölçüm xref'i; 51:49 ve 49:13 yeni okuma bağı; AS_kiyame 75 → 77).

### Yeni bekleyen (TAM OKUMA SONUNDA, oturumda sorulmaz)
Yok.

## SÛRE 77 MÜRSELÂT SONU (2026-10-28)

**Okunan: 4464 / 6236 ayet (%71,6)** — sûre 1 ve 9-77 TAM, sûre 2 kısmi (1-20). İlerleme `murselat_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1481** (1478 → 1481; `kok_ekle_77.py`: كفت 77:25; شمخ 77:27; لهب 77:31). Aday havuzu **1041** (sûre 77'de yeni aday yok; `AX_murselat` boş). Bağ **AS_murselat** 57. Esmâ okuyucu kararı (KARAR) **687** (683 → 687; 0 İLÂHÎ, 4 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik beş blokta 0 (sûre geneli 50 / 0) · [x/y] **126 sayım (17 + 24 + 30 + 24 + 31), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması hedefli 0, genel 0 · **DUZELTME 0**.
Sûrenin 50 ayeti beş blokta okundu; oturum iki gün (2026-10-27 / 28), sûre 75 ve 76 ile aynı oturum. Paket `notlar/sure77_murselat_okuma.md` (`murselat_paket_md.py`, 50 başlık). Uzak depo **0593b8e** (oturum boyunca ilerlemedi); ara zip'ler `fark_0593b8e_sure77_ara1.zip` (1-20), `fark_0593b8e_sure77_ara2.zip` (1-40); kullanıcı isteğiyle oturumun bütün okuması tek zip (`oturum_okuma_0593b8e_75-77_40.zip`, sonra son hâli `oturum_okuma_0593b8e_75-77.zip`); son fark zip `fark_0593b8e_sure77.zip`.

### Sûre 77 bilançosu (TAM SAYIM, `okuma_metni['77']['_bilanco_sure']`)
181 kelime · **lafız 0 · Rab 0** (sûrenin tamamında) · edilgen 8 (77:7-12, 36, 48) · iltifât ölçümü 7 (77:8, 16, 31, 38, 43, 44, 46) · hapaks 2 (77:25, 27 — yeni kök) · mm2 0.
Yıldız 0:40 · ★1 · ★★1 · ★★★8 (pas 6, hapaks 2 — içerik iddiası değil).
Fâsıla A 9 · ع 1 · ت 5 · ل 2 · ن/م 29 · ب 2 · ر 2; kafiye kırığı 0, sınıf geçişleri işaretsiz (924). En uzun 77:27 (7); en kısa 77:1-5, 13, 26 (2).
Nakarat 'veylun yevme'izin li'l-mukezzibîn' sûre içi 10 (hepsi basıldı), korpusta 11 (+83:10). Esit2: 77:43 → 52:19 TAM; 77:44 → sûre 37'de üç TAM; 77:18 → 37:34 BENZER. Sayı işareti: 77:30 'selâs' gerçek; 77:46 'qalîl' yanlış pozitif.

### Çıpa (ölçüt değişmedi)
L4 yok. L1 9: 77:8-10 âhiretteki kozmik olay (yıldızlar, gök, dağlar; 75:8-9 emsali); 77:20-22 oluşum dizisi (değersiz su, sağlam yer, bilinen ölçü — 77:22 birimsiz ölçü, L4 sınır vakası); 77:25-26 dirileri ve ölüleri toplayan yer; 77:27 dağlar ve tatlı su (27:61 emsali). Olgu değil 29; merdiven uygulanmayan 12. Tarayıcı v4 adayı 0.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
4 e_oto tokeni → ilâhî 0, değil 4 (77:16, 38 'evvel'; 77:17 'âxir'; 77:26 'hayy'). §4.3 mühür 4 → geçerli **0**; 77:17 ölçüm MÜHÜRSÜZ / esma_kayit EVET ayrışması (1022).

### Kendi kaydı
Kayıttan önce: 77:23 alıntı yazımı; 77:27 çıpa notundaki 27:61 emsali basıldı; 77:42, 77:44'te basılmamış okunmuş ayet numaraları sayıya çevrildi. Kayıttan sonra: yok.

### Aday 1041 — kayıt (sûre 77)
Sûre içi kayıt yok (lafız ve Rab yok). Sûre dışı aile (okuma): 57:3 / 77:16-17 'evvel / âxir'.

### Aday 1040 — kayıt (test korpus sonunda)
76:31 / 77:1 sûre sınırı (rahmet / azapla kapanış, lafızsız yeminle açılış; fâsıla ا → ا). Ardışık sûre okuma bağları: 75:1 / 76:1 / 77:1 açılışlar; 76:17, 21 / 77:27 سقي; 76:7, 11 / 77:32 شرر. 77:50 → 78:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
50 ayetin hepsinde not; ayet içi çift 3 (77:6, 26, 48), ayetler arası 4 (77:16 / 17, 77:18 / 44, 77:30-31 / 41, 77:43 / 46). Karşılaştırma yapılmadı.

### Mevcut ailelere girenler
* 1017: yemin edilenler (77:1-5), edilgen fiillerin failleri, konuşan 1P / 1S, işaretsiz emirlerin sahibi adsız. Gönderge / i'râb / okuma ikiliği KAPATILAMAZ: 77:1, 6, 8-11 şart cevabı, 12, 23, 26, 32, 36, 50.
* 1021: عرف, نشر, ظلل (×3), قدر, شرر 'şerer', جمل.
* 1022: 77:17 mühür ayrışması.
* 924: ayet 1 harf alanı; yemin biçimi yalnız 77:1; beddua / övgü / benzetme biçim alanında yok; işaretsiz fâsıla geçişleri; iltifât tanımı (1P → 1S görünmüyor).

### Kullanıcı kararı (bu oturum)
53:45 / 51:49 / 49:13 → 75:39 okuma bağı onaylandı: 51:49 ve 49:13 AS_kiyame'ye yazıldı (53:45 zaten xref); AS_kiyame 75 → 77.

### Yeni bekleyen (TAM OKUMA SONUNDA, oturumda sorulmaz)
Yok.

## SÛRE 78 NEBE' SONU (2026-10-29)

**Okunan: 4504 / 6236 ayet (%72,2)** — sûre 1 ve 9-78 TAM, sûre 2 kısmi (1-20). İlerleme `nebe_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1485** (1481 → 1485; `kok_ekle_78.py`: وهج 78:13; ثجج 78:14; كعب 78:33; دهق 78:34). Aday havuzu **1041** (sûre 78'de yeni aday yok; `AX_nebe` boş). Bağ **AS_nebe** 51. Esmâ okuyucu kararı (KARAR) **690** (687 → 690; 2 İLÂHÎ, 1 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik dört blokta 0 (78:31-40 ilk taslakta 1, kayıttan önce düzeltildi; sûre geneli 40 / 0) · [x/y] **131 sayım (20 + 36 + 25 + 50), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması hedefli 0, genel 0 · **DUZELTME 1** (78:38, kayıttan sonra, kullanıcı sorusuyla).
Sûrenin 40 ayeti dört blokta okundu; oturum iki gün (2026-10-28 / 29). Paket `notlar/sure78_nebe_okuma.md` (`nebe_paket_md.py`, 40 başlık). Uzak depo **7d5e727** (oturum boyunca ilerlemedi); ara zip `fark_7d5e727_sure78_ara1.zip` (1-20); son zip `fark_7d5e727_sure78.zip`.

### Sûre 78 bilançosu (TAM SAYIM, `okuma_metni['78']['_bilanco_sure']`)
173 kelime · **lafız 0 · Rab 3** (78:36, 37, 39) · edilgen 3 (78:18-20) · iltifât ölçümü 4 (78:6, 35, 36, 37) · hapaks 3 (78:13, 14, 34 — yeni kök) · mm2 0 · nakarat3 0.
Yıldız 0:31 · ★1 · ★★4 · ★★★4 (hapaks 3, rab 1 — içerik iddiası değil).
Fâsıla N 5 (78:1-5; 78:2 م) · A 35 (78:6-40); kafiye kırığı 0. En uzun 78:40 (15); en kısa 2 kelime (on ayet).
Sayı işareti: 78:12 'seb'' gerçek; 78:8 'ezvâc' yanlış pozitif. xref: 78:10 → 25:47, 78:17 → 37:21, 78:29 → 36:12, 78:40 → 28:47 (dördü basıldı).

### Çıpa (ölçüt değişmedi)
L4 yok. L2 1: 78:15 su → tane ve bitki (ta'lîl lâmı, 50:9 emsali; tarayıcı v4 adayı, çıpa değil — kesinlik 0/1). L1 11: 78:6-11 nimet dizisi (yer, dağlar, çift yaratma, uyku, gece, gündüz), 78:14 su ve kaynağı, 78:16 bahçeler, 78:19-20 göğün açılması / dağların yürütülmesi (âhiretteki kozmik olay). L0 1: 78:37 Rab tamlamasında gökler, yer (44:7, 37:5 emsali). Gönderge adsız, merdiven uygulanmadı: 78:12 ('seb'an şidâdâ'), 78:13 ('sirâc'). Olgu değil 25.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
3 e_oto tokeni → ilâhî 2 (78:37, 38 'er-rahmân'), değil 1 (78:40 'qarîb'). §4.3 mühür 2 → geçerli **2** (ton cemâl); ölçüm satırı ikisinde de MÜHÜRSÜZ — ayrışma (1022).

### Kendi kaydı
Kayıttan önce: 78:4-5 ◈K'deki tetiksiz gözlem ◇'ye taşındı; 78:17'de basılmamış 77:13, 14, 38 emsal olarak basıldı; 78:24'te 44:56 için basılmamış bağlam niteliği silindi; 78:35 ◈B tetik satırı dolduruldu; 78:38 ◈K 'rûh' notu düzeltildi; ثجج gloss çeviriyazısı. Kayıttan sonra: 1 — DUZELTME 78:38 (aday 1017): rûh tekil / melekler çoğul; öne geçen fiil ilk özneye uyuyor (78:38 'yeqûmu' 3MS, 70:4 'ta'ruju' 3FS); 'saffâ' ve 'lâ yetekellemûne' kapsamı KAPATILAMAZ; ölçüm özne sayısını göstermiyor (924). Kullanıcı sorusuyla yakalandı.

### Aday 1041 — kayıt (sûre 78)
Sûre içi kayıt yok ('şâ'e', 'ezine', 'qâle' Allah ile insan arasında bölünmüyor; lafız yok).

### Aday 1040 — kayıt (test korpus sonunda)
77:50 / 78:1 sûre sınırı (soruyla kapanış / soruyla açılış; 3MP → 3MP; fâsıla ن → ن; 'hadîs' / 'nebe''). Ardışık sûre okuma bağları: 77:25 / 78:6 'e-lem nec'ali'l-arda' + nekre işlev; 77:9-10 / 78:19-20 gök ve dağlar edilgenle; 77:13, 14, 38 / 78:17 'yevmu'l-fasl'. 78:40 → 79:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
40 ayetin hepsinde not; ayet içi çift 1 (78:37), ayetler arası 11 (78:10 / 11, 7 / 20, 24 / 25, 24 / 30, 22 / 31, 24 / 34, 24 / 35, 28 / 35, 26 / 36, 27 / 36, 22 / 39). Karşılaştırma yapılmadı.

### Mevcut ailelere girenler
* 1017: soruşanlar, soran / cevap veren ses, konuşan 1P, muhatap 2MP / 2MS, edilgen fiillerin failleri, azgınlar, sakınanlar, 'el-mer'', 'el-kâfir' adsız. Gönderge / i'râb / okuma ikiliği KAPATILAMAZ: 78:3, 8, 12, 13, 14, 21, 22, 23, 26, 38.
* 1021: نهر 'nehâr', حبب 'habb', عصر 'mu'sırât', غسق, ترب 'etrâb', حسب 'hisâbâ' (yeterli).
* 1022: 78:37, 38 mühür ayrışması.
* 924: ayet 1 harf alanı; soru-cevap / ta'lîl / 'inne' / meful takdimi biçim alanında yok; 'ezvâc' sayı işareti; kısmi şahıs örtüşmesinde iltifât 0; 1P → anlatıcı geçişi görünmüyor.

### Yeni bekleyen (TAM OKUMA SONUNDA, oturumda sorulmaz)
Yok.

## SÛRE 79 NÂZİ'ÂT SONU (2026-10-29)

**Okunan: 4550 / 6236 ayet (%73,0)** — sûre 1 ve 9-79 TAM, sûre 2 kısmi (1-20). İlerleme `naziat_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1492** (1485 → 1492; `kok_ekle_79.py`: حفر 79:10; نخر 79:11; سهر 79:14; سمك 79:28; غطش 79:29; دحو 79:30; طمم 79:34). Aday havuzu **1041** (sûre 79'da yeni aday yok; `AX_naziat` boş). Bağ **AS_naziat** 57. Esmâ okuyucu kararı (KARAR) **692** (690 → 692; 2 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik beş blokta 0 (79:11-20 ilk taslakta 1, kayıttan önce düzeltildi; sûre geneli 46 / 0) · [x/y] **119 sayım (19 + 26 + 30 + 29 + 15), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması hedefli 0, genel 0 · **DUZELTME 1** (79:11, kayıttan sonra).
Sûrenin 46 ayeti beş blokta okundu (2026-10-29). Paket `notlar/sure79_naziat_okuma.md` (`naziat_paket_md.py`, 46 başlık). Uzak depo **7d5e727** (oturum boyunca ilerlemedi); ara zip'ler `fark_7d5e727_sure79_ara1.zip`, `fark_7d5e727_sure79_ara2.zip` (1-40); son zip `fark_7d5e727_sure79.zip`.

### Sûre 79 bilançosu (TAM SAYIM, `okuma_metni['79']['_bilanco_sure']`)
179 kelime · **lafız 1 (79:25) · Rab 5** (79:16, 19, 24, 40, 44 — 79:24 Fir'avn'ın iddiası, ölçüm Rab sayıyor) · edilgen 1 (79:36) · iltifât ölçümü 4 (79:12, 20, 33, 34) · hapaks 7 (79:2 نشط; 79:11, 14, 28, 29, 30, 34 yeni kök) · mm2 0 · nakarat3 0.
Yıldız 0:31 · ★1 · ★★2 · ★★★12 (hapaks 7, rab 4, allah 1 — içerik iddiası değil); 79:33 ★ kaynağı aday 1001 düzeltmesiyle kafiye.
Fâsıla ölçüm A 30 · H 9 (79:6-14) · 'ٓ' 6 (79:15, 25, 26, 30, 43, 44 — medde artefaktı) · N 1 (79:33 م); ölçüm kafiye kırığı 2: 79:30 sahte (medde), 79:33 gerçek. En uzun 9 kelime (79:40, 46); en kısa 2 kelime (on ayet).
Sayı işareti: 79:13 'vâhida' gerçek. Ölçüm bağları: esit2 79:15 → 20:9, 79:17 → 20:24 / 20:43, xref 79:16 → 20:12 (basıldı); esit2 79:33 → 80:32, xref 79:35 → 89:23, 79:38 → 87:16, 79:42 → 7:187 (henüz okunmadı); 79:40 → 55:46 (basıldı).

### Çıpa (ölçüt değişmedi)
L4 yok. L2 yok. L1 8: 79:11 itiraz içinde kemik; 79:27-33 yaratılış dizisi (insan / gök karşılaştırması, göğün tavanı, gece / kuşluk, yer yayma — sıra 'ba'de zâlike', su ve otlak, dağlar, yararlanma işlevi). L0 2: 79:16 Tuvâ yer adı; 79:46 akşam / kuşluk zaman zarfı. Olgu değil 36. Tarayıcı v4 adayı 0.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
2 e_oto tokeni → değil 2 (79:25 'el-âxira', 'el-ûlâ' — âhiret / dünya çifti). §4.3 ölçüm mührü 1 (79:25, ÇİFT) → geçerli **0** (1022).

### Kendi kaydı
Kayıttan önce: 79:10 iltifât notu; 79:4-5 için 77:2-5 emsal olarak basıldı; 79:15 ders adı olarak ayet numaraları, 79:18 basılmamış okunmuş ayetler silindi; 79:17 basılan ayette olmayan kişi adı silindi; 79:11 ◈B tetik satırı '—' yapıldı; 79:21 eşsesli lemma sayısı kök sayısına çevrildi; 79:22 basılmamış ayetlerin sûre adı ve 79:30 lemma listesi içerik iddiası silindi; 79:42, 46 ◇ ifadeleri KAPATILAMAZ biçimine çekildi. Kayıttan sonra: 1 — DUZELTME 79:11 (aday yok): 17:49 / 17:98 ile karşılaştırmanın sırası ters yazılmıştı (orada durum → soru, burada soru → durum).

### Aday 1041 — kayıt (sûre 79)
ندي: 79:16 Rab seslenir / 79:23 Fir'avn seslenir. ربب: 79:16, 19, 40, 44 Rab / 79:24 Fir'avn'ın 'ene rabbukumu'l-a'lâ' iddiası (ölçüm Rab ekseninde sayıyor, esma_kayit sınıfı R).

### Aday 1040 — kayıt (test korpus sonunda)
78:40 / 79:1 sûre sınırı (kâfirin işaretli 1S dileğiyle kapanış / lafızsız yeminle açılış; fâsıla ا → ا). Ardışık sûre okuma bağları: 78:6 / 79:30 yer; 78:7 / 79:32 dağlar; 78:10 / 79:29 gece; 78:11 / 79:33 işlev adı; 78:12 / 79:27 بني + 'şedîd'; 78:14 / 79:31 su; 78:22 / 79:37, 39 azgınlar + varış yeri. 79:46 → 80:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
46 ayetin hepsinde not; ayet içi çift 4 (79:25, 27, 29, 46), ayetler arası 10 (79:12 / 13, 17 / 19, 19 / 21, 16 / 23, 19 / 24, 27-29 / 30, 20 / 34, 37 / 40, 37-38 / 40, 39 / 41). Karşılaştırma yapılmadı.

### Mevcut ailelere girenler
* 1017: yemin edilenler (79:1-5), 'er-râcife' / 'er-râdife', söyleyenler, haykıran, gösteren (79:20), toplananlar, 3MS zamirle yaratan, 'et-tâmme', azan / korkan, soranlar, muhatap 2MS, 79:46 'hum' adsız. Alıntı sınırları: 79:10 → 79:12 'qâlû' ile kapandı; 79:16-19 Rab sözü + iç 'qul'; 79:24 Fir'avn sözü; 79:42-46 işaretsiz. Gönderge / i'râb / okuma ikiliği KAPATILAMAZ: 79:1, 10, 14, 20, 25, 28, 33, 34, 43, 46.
* 1021: نشط 'neşt', سبح 'sebh' (yüzme), دبر 'mudebbirât'.
* 1022: 79:25 ölçüm mührü / geçerli değil.
* 924: ayet 1 harf alanı; QASEM yalnız 79:1; 'innemâ' ve zamir fasl hasrı biçim alanında yok (79:13, 39, 41, 45); 79:32 'ersâ' morph IMPF 1S; 79:24 iddia Rab ekseninde; sahset iki ayrı 2MS'yi ayırmıyor (79:17 / 18-19); esit2 79:13 → 37:19 yazılmıyor; medde fâsıla artefaktı; 79:40 'hevâ' eşsesli lemma.

### Yeni bekleyen (TAM OKUMA SONUNDA, oturumda sorulmaz)
Yok.

## SÛRE 80 'ABESE SONU (2026-10-29)

**Okunan: 4592 / 6236 ayet (%73,6)** — sûre 1 ve 9-80 TAM, sûre 2 kısmi (1-20). İlerleme `abese_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1496** (1492 → 1496; `kok_ekle_80.py`: صدي 80:6; قضب 80:28; أبب 80:31; صخخ 80:33). Aday havuzu **1041** (sûre 80'de yeni aday yok; `AX_abese` boş). Bağ **AS_abese** 42. Esmâ okuyucu kararı (KARAR) **694** (692 → 694; 2 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik dört blokta 0 (sûre geneli 42 / 0) · [x/y] **89 sayım (15 + 22 + 21 + 31), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması hedefli 0, genel 0 · **DUZELTME 0** (1 ARIZA eki kayıttan sonra: 80:10 morph etiketi).
Sûrenin 42 ayeti dört blokta okundu (son blok 31-42, 12 ayet). Dosyalar `yamalar/iskele_80.py` ile naziat_* şablonlarından kuruldu. Paket `notlar/sure80_abese_okuma.md` (`abese_paket_md.py`, 42 başlık). Uzak depo **7d5e727** (oturum boyunca ilerlemedi); ara zip `fark_7d5e727_sure80_ara1.zip` (1-20); son zip `fark_7d5e727_sure80.zip`.

### Sûre 80 bilançosu (TAM SAYIM, `okuma_metni['80']['_bilanco_sure']`)
133 kelime · **lafız 0 · Rab 0** (lafızsız ve Rabsız sûre) · edilgen 1 (80:17) · iltifât ölçümü 3 (80:25, 32, 33) · hapaks 3 (80:28, 31, 33 — yeni kök) · mm2 0 · nakarat3 0.
Yıldız 0:37 · ★1 (80:2, aday 1001 düzeltmesiyle kafiye — sahte kırık) · ★★1 (80:17 pas) · ★★★3 (hapaks — içerik iddiası değil).
Fâsıla ölçüm H 23 (ة ile ه birleşik) · A 14 · 'ٓ' 4 (80:1, 3, 4, 24 — medde artefaktı) · N 1 (80:32 م); ölçüm kafiye kırığı 1 (80:2, sahte). En uzun 6 kelime (80:37); en kısa 2 kelime (13 ayet).
Ölçüm bağları: esit2 80:12 → 74:55, 80:32 → 79:33 (TAM, ikisi basıldı); başka xref yok.

### Çıpa (ölçüt değişmedi)
L4 yok. L2 yok — 80:27 L2 sınır vakası (su → yer yarılması → tane, 'thumme' / 'fe' sırası, 'bihî' / ta'lîl yok; 50:9, 78:15 L2). L1 10: 80:19 nutfe + yaratma + ölçme; 80:21 ölüm + defin; 80:25-31 su, yer, tane, bitki adları; 80:32 yararlanma işlevi. L0 1: 80:24 yiyecek. Olgu değil 31 (80:2 'kör' kişi nitelemesi). Tarayıcı v4 adayı 0.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
2 e_oto tokeni → değil 2 (80:16 'kirâm', 'berara' — yazıcıların sıfatı). §4.3 ölçüm mührü 1 (80:16, ÇİFT) → geçerli **0** (1022).

### Kendi kaydı
Kayıttan önce: 80:42 harekesiz 'ulâ'ike hum' okunmuş / okunmamış sayısı (12 / 7 → 10 / 9; oturum_xy bu biçimi denetlemiyor). Kayıttan sonra: DUZELTME yok; ARIZA eki 80:10 ('telehhâ' morph PERF I. bab 3MS — biçim IMPF V. bab 2MS; ayet kayıtları değişmedi, önce / sonra karşılaştırmasıyla doğrulandı).

### Aday 1041 — kayıt (sûre 80)
'şâ'e': 80:12 dileyen insan / 80:22 dileyen dirilten 3MS.

### Aday 1040 — kayıt (test korpus sonunda)
79:46 / 80:1 sûre sınırı (3MP + saat ile kapanış / 3MS iki fiille açılış; fâsıla ا → ى). Ardışık sûrede TAM tekrar: 79:33 / 80:32 'metâ'an lekum ve li-en'âmikum' (esit2) ve ikisinin hemen ardından 'fe-izâ câ'eti' + korpusta tek ad (79:34 'et-tâmmetu'l-kubrâ' / 80:33 'es-sâxxa'). Ardışık sûre okuma bağları: 79:18 / 80:3, 7; 79:22 / 80:8; 79:31 / 80:25; 79:35 / 80:17; 79:37, 40 / 80:5, 8; 79:43 / 80:4; 79:45 / 80:9; iki sûrede adsız 2MS muhatap. 80:42 → 81:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
42 ayetin hepsinde not; ayet içi çift 1 (80:35), ayetler arası 7 (80:3 / 7, 5 / 8, 6 / 10, 21 / 22, 38-39 / 40-41 ve kollar). Karşılaştırma yapılmadı.

### Mevcut ailelere girenler
* 1017: yüzünü ekşiten, kör, muhatap 2MS, yeterli gören, koşarak gelen (aynılıklar KAPATILAMAZ); 'innehâ' / 'zekerahû'; 'sefera'; 3MS yaratan / öldüren / dirilten; konuşan 1P; 'es-sâxxa'; 'el-mer''; yüzlerin sahipleri; 'ulâ'ike'. Söz işareti yok. Okuma ikiliği KAPATILAMAZ: 80:7, 17, 20, 32, 33.
* 1021: سفر, برر, حبب, غلب, فجر.
* 1022: 80:16 ölçüm mührü / geçerli değil.
* 924: ayet 1 harf alanı; medde artefaktı ve sahte kırık (80:1-2); ة / ه aynı sınıf; 80:32 م işaretsiz; edilgen ortaç; kısmi örtüşmede iltifât 0; 80:10 morph; 80:42 hasr.

### Yeni bekleyen (TAM OKUMA SONUNDA, oturumda sorulmaz)
Yok.

## SÛRE 81 TEKVÎR SONU (2026-10-29)

**Okunan: 4621 / 6236 ayet (%74,1)** — sûre 1 ve 9-81 TAM, sûre 2 kısmi (1-20). İlerleme `tekvir_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1504** (1496 → 1504; `kok_ekle_81.py`: كدر 81:2; وحش 81:5; وأد 81:8; كشط 81:11; خنس 81:15; كنس 81:16; عسعس 81:17; ضنن 81:24). Aday havuzu **1041** (sûre 81'de yeni aday yok; `AX_tekvir` boş). Bağ **AS_tekvir** 50. Esmâ okuyucu kararı (KARAR) **696** (694 → 696; 2 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik üç blokta (21-29 ilk taslakta 1 uyuşmaz, kayıttan önce düzeltildi; sûre geneli 29 / 0) · [x/y] **66 sayım (21 + 24 + 21), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması hedefli 0, genel 0 · **DUZELTME 0**, ARIZA eki yok.
Sûrenin 29 ayeti üç blokta okundu (1-10, 11-20, 21-29). Dosyalar `yamalar/iskele_81.py` ile abese_* şablonlarından kuruldu (oturum dışı). Paket `notlar/sure81_tekvir_okuma.md` (`tekvir_paket_md.py`, 29 başlık). Uzak depo **27e79a3** (oturum boyunca ilerlemedi); ara zip `fark_27e79a3_sure81_ara1.zip` (1-20); son zip `fark_27e79a3_sure81.zip`.

### Sûre 81 bilançosu (TAM SAYIM, `okuma_metni['81']['_bilanco_sure']`)
104 kelime · **lafız 1 · Rab 1** (ikisi de 81:29) · edilgen 12 (81:1, 3-13) · iltifât ölçümü 6 (81:15, 17, 22, 23, 26, 27) · hapaks 7 (81:2, 5, 8, 11, 16, 17, 24 — yeni kök) · mm2 0 · nakarat3 0.
Yıldız 0:12 · ★★1 (81:29 rab) · ★★★16 (pas 12, hapaks 4 — içerik iddiası değil).
Fâsıla ölçüm ت 14 · س 4 · N 11; ölçüm kafiye kırığı 0 (ت → س, س → م geçişleri işaretsiz, 924). En uzun 8 kelime (81:29); en kısa 2 kelime (81:16, 26). Sayı işareti 2 (81:4, 7 — kök kaynaklı yanlış pozitif).
Ölçüm bağları: esit2 81:19 → 69:40 (TAM), 81:27 → 38:87 (TAM), 68:52 (BENZER); xref 81:29 → 76:30 (basıldı), 6:128, 7:89 (henüz okunmadı).

### Çıpa (ölçüt değişmedi)
L4 yok. L2 yok. L1 5: 81:1, 2, 3, 6, 11 — âhirette kozmik olay (güneş, yıldızlar, dağlar, denizler, gök). L0 3: 81:17 gece, 81:18 sabah (zaman zarfı), 81:23 ufuk (yer adı; görme olayı gaybî). Olgu değil 21 (gönderge adsız 2: 81:15-16 yemin edilenler — merdiven uygulanmadı). Tarayıcı v4 adayı 0.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
2 e_oto tokeni → değil 2 (81:19 'kerîm' elçinin sıfatı; 81:23 'mubîn' ufkun sıfatı). §4.3 ölçüm mührü 2 (81:19, 23) → geçerli **0** (1022). 81:29 'rabbu'l-'âlemîn' Rab ekseninde.

### Kendi kaydı
Kayıttan önce: 81:1 'izâ' sayımında henüz okunmamış ayet numaraları sıralanmıştı (sayıya çevrildi); esma_el yorumunda basılmamış ayet numarası emsal adı olarak geçiyordu (çıkarıldı); 17:42 harf çevirisi; 81:13 sıra ifadesi; 81:23 ◈K dolu yazılmıştı (tetik ön kuru koşusu yakaladı → '—'); 81:29 lafız / Rab konum ifadesi. Kayıttan sonra: yok.

### Aday 1041 — kayıt (sûre 81)
'zû': 81:20 'zî quvva' (elçi) / 'zi'l-'arş' (arşın sahibi, lafızsız). 'şâ'e': 81:28-29 muhatapların dilemesi / Allah'ın dilemesi.

### Aday 1040 — kayıt (test korpus sonunda)
80:42 / 81:1 sûre sınırı (işaret zamiri + hasr ile yargı / şart zarfı ile kozmik olay dizisi; fâsıla ة → ت; ikisi de lafızsız, Rabsız). Ardışık sûrede sıralı eşleşme: 80:11-12 / 81:27-28 öğüt + 'men şâ'e'. Ardışık sûre okuma bağları: 80:13 / 81:10 'suhuf'; 80:17 / 81:9 edilgen 'qutile' / 'qutilet'; 80:22 / 81:10 kök نشر; 80:33 / 81:1 'izâ' ile âhiret açılışı. 81:29 → 82:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
29 ayetin hepsinde not; ayet içi çift 1 (81:29 'teşâ'ûne' / 'yeşâ'a'llâh'), ayetler arası 3 (81:12 / 13 cehennem / cennet; 81:17 / 18 gece / sabah; 81:19 / 25 elçinin sözü / şeytanın sözü). Karşılaştırma yapılmadı.

### Mevcut ailelere girenler
* 1017: edilgen fiillerin failleri (81:1, 3-13); 81:8-9 soran, gömen, öldüren; 81:7 eşleştirilenler; 81:15 konuşan 1S ve yemin edilenler (81:15-16); 81:19 'hu' ve elçi; 81:22 'sâhibukum' / 2MP (elçiyle aynılığı KAPATILAMAZ); 81:23 gören / görülen; 81:24, 25, 27 'huve'. Söz işareti 'qâle / qîle' yok — 81:8-9 dolaylı aktarım. Okuma ikiliği KAPATILAMAZ: 81:6, 14, 17, 24.
* 1021: عشر (''işâr'), نفس ('teneffese'), جنن (cennet / deli), علم (''âlemîn'), نشر (ardışık sûrede iki anlam), سجر.
* 1022: 81:19, 23 ölçüm mührü / geçerli değil.
* 924: ayet 1 harf alanı; 'izâ' şart zarfı ve cevabı kip alanında yok; atıflı yeminlerde QASEM yok (81:17-18); 'fe-lâ uqsimu' NEG; 81:17 iltifât (konuşan değişmiyor); fâsıla geçişleri işaretsiz; yıldızlar formül davranışı.

### Yeni bekleyen (TAM OKUMA SONUNDA, oturumda sorulmaz)
Yok.

## SÛRE 82 İNFİTÂR SONU (2026-10-29)

**Okunan: 4640 / 6236 ayet (%74,4)** — sûre 1 ve 9-82 TAM, sûre 2 kısmi (1-20). İlerleme `infitar_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1505** (1504 → 1505; `kok_ekle_82.py`: بعثر 82:4). Aday havuzu **1041** (sûre 82'de yeni aday yok; `AX_infitar` boş). Bağ **AS_infitar** 31. Esmâ okuyucu kararı (KARAR) **699** (696 → 699; 1 İLÂHÎ, 2 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik iki blokta 0 (sûre geneli 19 / 0) · [x/y] **52 sayım (28 + 24), 0 uyuşmaz** · e_el=? her blokta 0 · retroaktif gloss yaması hedefli 0, genel 0 · **DUZELTME 0**, ARIZA eki yok.
Sûrenin 19 ayeti iki blokta okundu (1-10, 11-19). Dosyalar `yamalar/iskele_82.py` ile tekvir_* şablonlarından kuruldu (oturum dışı). Paket `notlar/sure82_infitar_okuma.md` (`infitar_paket_md.py`, 19 başlık). Uzak depo **27e79a3** (oturum boyunca ilerlemedi); sûre 82 için ara zip yok; son zip `fark_27e79a3_sure82.zip` (sûre 81 + 82).

### Sûre 82 bilançosu (TAM SAYIM, `okuma_metni['82']['_bilanco_sure']`)
80 kelime · **lafız 1 (82:19) · Rab 1 (82:6)** · edilgen 2 (82:3, 4) · iltifât ölçümü 0 · hapaks 0 · mm2 0 · nakarat3 82:17-18.
Yıldız 0:15 · ★1 (82:19 lafız) · ★★★3 (82:3, 4 pas; 82:6 rab — içerik iddiası değil).
Fâsıla ölçüm ت 5 · N 11 · ك 2 · H 1; ölçüm kafiye kırığı 0 (geçişler işaretsiz, 924). En uzun 9 kelime (82:19); en kısa 2 kelime (82:11). Sayı işareti 0.
Ölçüm bağları: esit2 82:13 → 83:22 (TAM, henüz okunmadı), 82:17 ↔ 82:18 (BENZER); xref 82:19 → 2:48, 2:123 (henüz okunmadı).

### Çıpa (ölçüt değişmedi)
L4 yok. L2 yok. L1 5: 82:1, 2, 3 (âhirette kozmik olay: gök, yıldızlar, denizler); 82:7 yaratma + düzenleme + dengeleme ('fe' ile sıralı, aşama adı yok); 82:8 biçim + oluşturma. L0 yok. Olgu değil 14. Tarayıcı v4 adayı 0.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
3 e_oto tokeni → ilâhî 1 (82:6 'rabbike'l-kerîm'), değil 2 (82:11 'kirâm', 82:13 'berr'). §4.3 ölçüm mührü 3 → geçerli **1** (82:6, cemâl; ölçüm satırı 'MÜHÜRSÜZ' diyordu — 1022).

### Kendi kaydı
Kayıttan önce: 82:7 ''adele' eşsesli lemma sayısı çıkarıldı. Kayıttan sonra: yok.

### Aday 1041 — kayıt (sûre 82)
Kök كرم: 82:6 'rabbike'l-kerîm' (İLÂHÎ) / 82:11 'kirâmen kâtibîn'.

### Aday 1040 — kayıt (test korpus sonunda)
81:29 / 82:1 sûre sınırı (lafız + Rab + hasr ile kapanış / lafızsız şart zarfı ile açılış; fâsıla ن → ت). Ardışık sûreyle yapı eşleşmesi: 've izâ' + ad + fiil şart dizisi + ''alimet nefsun mâ …' cevabı (81:1-14 / 82:1-5); harekesiz 've ize'l-bihâr' (81:6 / 82:3) ve ''alimet nefs' (81:14 / 82:5) korpusun iki ayeti, ardışık iki sûrede. Ardışık sûre okuma bağları: 81:11 / 82:1; 81:2 / 82:2; 81:19 / 82:6 ('kerîm' elçi / Rab); 81:29 / 82:19 (iki sûre lafızla biten ayetle kapanıyor). 82:19 → 83:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
19 ayetin hepsinde not; ayet içi çift 2 (82:5, 82:19), ayetler arası 1 (82:13 / 14). Karşılaştırma yapılmadı.

### Mevcut ailelere girenler
* 1017: edilgen failler; konuşan adsız; 'el-insân' (cins); yaratan 3MS; muhataplar 2MP; yazıcılar; muhatap 2MS (aynılıklar işaretsiz). Söz işareti yok. Okuma ikiliği KAPATILAMAZ: 82:5, 8.
* 1021: فطر, فجر, برر (eşsesli lemma), شيأ, 'adele' (eşsesli lemma).
* 1022: 82:6 ölçüm 'MÜHÜRSÜZ' / geçerli; 82:11, 13 ölçüm mührü / geçerli değil.
* 924: ayet 1 harf alanı; şart zarfı / cevabı ve 82:6 sorusu kip alanında yok; 2MS → 2MP iltifât 0; 'li'llâh' takdimi; fâsıla geçişleri işaretsiz.

### Yeni bekleyen (TAM OKUMA SONUNDA, oturumda sorulmaz)
Yok.

## SÛRE 83 MUTAFFİFÎN SONU (2026-10-29)

**Okunan: 4676 / 6236 ayet (%75,0)** — sûre 1 ve 9-83 TAM, sûre 2 kısmi (1-20). İlerleme `mutaffifin_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1510** (1505 → 1510; `kok_ekle_83.py`: طفف 83:1, رين 83:14, رحق 83:25, سنم 83:27, غمز 83:30). Aday havuzu **1041** (sûre 83'te yeni aday yok; `AX_mutaffifin` boş). Bağ **AS_mutaffifin** 56. Esmâ okuyucu kararı (KARAR) **702** (699 → 702; 3 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik her blokta 0 (sûre geneli 36 / 0) · [x/y] **101 sayım, 0 uyuşmaz** (sûre geneli) · e_el=? her blokta 0 · retroaktif gloss yaması hedefli 0; رين eklemesinde genel geçiş 5 yanlış gloss → `yama_rin_83.py` (aşağıda) · **DUZELTME 0**, ARIZA eki yok.
Sûrenin 36 ayeti dört blokta okundu (1-10, 11-20, 21-28, 29-36). Dosyalar `yamalar/iskele_83.py` ile infitar_* şablonlarından kuruldu (oturum dışı). Paket `notlar/sure83_mutaffifin_okuma.md` (`mutaffifin_paket_md.py`, 36 başlık). Uzak depo **27e79a3** (oturum boyunca ilerlemedi); ara zip `fark_27e79a3_sure83_ara1.zip`; son zip `fark_27e79a3_sure83.zip` (sûre 81 + 82 + 83).

### Sûre 83 bilançosu (TAM SAYIM, `okuma_metni['83']['_bilanco_sure']`)
169 kelime · **lafız 0 · Rab 2 (83:6, 15)** — lafızsız sûre · edilgen 5 (83:13, 17, 25, 33, 36) · iltifât ölçümü 0 · hapaks 5 ayet (83:1, 14, 25, 27, 30 — yeni kökler) · mm2 0.
Yıldız 0:25 · ★2 (83:17, 36 pas) · ★★1 (83:13 pas) · ★★★8 (hapaks 83:1, 14, 27, 30; rab 83:6, 15; pas 83:25, 33 — içerik iddiası değil).
Fâsıla metin ن 27 / م 9; ölçüm N 36, kafiye kırığı 0 (ن / م ayrımı sınıfta yok, 924). En uzun 8 kelime (83:14, 29); en kısa 2 kelime (83:1, 5, 9, 20, 21). Sayı işareti 0.
Sûre içi esit2 TAM: 83:9 / 20 ('kitâbun merqûm'), 83:23 / 35 (koltuklarda bakarlar; nakarat3 süzgeç GEÇMEZ). Ardışık sûreyle esit2 TAM: 82:13 / 83:22.

### Çıpa (ölçüt değişmedi)
L4 yok. L2 yok. L1 yok. L0 yok. Olgu değil 36 (âhiret, gaybî, insan davranışı, söz, soru). Tarayıcı v4 adayı 0.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
3 e_oto tokeni → hepsi DEĞİL (83:13 'evvelîn' öncekiler; 83:18, 22 'ebrâr' insan çoğulu). §4.3 ölçüm mührü 3 → geçerli **0** (1022).

### Kök çakışması — yama_rin_83 (kayıt)
رين ('râne', 83:14) eklenince `yama_retroaktif_gloss_83` genel geçişi 28:81, 29:38, 39:72, 40:76, 43:56 ölçüm satırlarında fâsıla kelimesinin harekesiz iskelet parçasını bu kök sandı ve yanlış gloss ekledi. `yama_rin_83.py` (calisma + betikler/) bu beş yeri düzeltme notuyla değiştirir; idempotent, kalan yanlış gloss yoksa assert geçer; her `yama_retroaktif_gloss_83` koşusundan SONRA koşulur. gloss_gecis özel ad iskeleti çakışması bekleyen kararıyla aynı aile (iskelet parçası eşleşmesi).

### Kendi kaydı
Kayıttan önce: 83:14 ◇ basılmamış ayet numaraları → sayı; 83:21 meal parantezi (gönderge adlandırma, 1017) çıkarıldı. Kayıttan sonra: yok. 83:26 için kullanıcıya çeviri önerisi verildi; kullanıcı kararıyla kayıt değiştirilmedi.

### Aday 1041 — kayıt (sûre 83)
Kayıt yok.

### Aday 1040 — kayıt (test korpus sonunda)
82:19 / 83:1 sûre sınırı ('li' + lafız ile kapanış / 'veyl' + 'li' + ortaç ile açılış; fâsıla ه → ن). Ardışık sûreyle yapı eşleşmesi: iyiler / günahkârlar 'inne' + 'le-fî' (82:13-14 / 83:7, 18; sıra ters); 82:13 / 83:22 esit2 TAM; 82:14 / 83:7 kalıp eşi. Okuma bağları: 82:17 / 83:8 've mâ edrâke mâ'; 82:9 / 83:11, 14 yalanlama; 82:14 / 83:16 'cahîm'; 82:10 / 83:33 'hâfizîn'. 83:36 → 84:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
36 ayetin hepsinde not; ayet içi çift 2 (83:29, 34), ayetler arası 4 (83:2 / 3; 83:7 / 18; 83:8 / 19; 83:29 / 34). Karşılaştırma yapılmadı.

### Mevcut ailelere girenler
* 1017: edilgen failler (83:13, 17, 25, 33, 36); konuşan adsız (83:13 1P); muhatap 2MS (83:8, 19), 2MP (83:17); 'el-muqarrabûn'; 83:33 zamir. Söz işareti 'qâle' 83:13, 'qâlû' 83:32 — tırnaklı, ayet içinde kapanıyor.
* 1021: قلب (kalp / dönme), عين (pınar), ثوب (karşılık), ختم (mühürlü / son); رين / fâsıla iskelet çakışması.
* 1022: 83:13, 18, 22 ölçüm mührü / geçerli değil.
* 924: ayet 1 harf alanı; şart zarfı ve 'mâ edrâke' sorusu; ن / م fâsıla ayrımı N sınıfında yok.

### Yeni bekleyen (TAM OKUMA SONUNDA, oturumda sorulmaz)
Yok (رين çakışması yama_rin_83 ile kapatıldı; aile kaydı gloss_gecis iskelet çakışmasına eklendi).

## SÛRE 84 İNŞİKÂK SONU (2026-10-30)

**Okunan: 4701 / 6236 ayet (%75,4)** — sûre 1 ve 9-84 TAM, sûre 2 kısmi (1-20). İlerleme `insikak_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1511** (1510 → 1511; `kok_ekle_84.py`: كدح 84:6). Aday havuzu **1041** (sûre 84'te yeni aday yok; `AX_insikak` boş). Bağ **AS_insikak** 49. Esmâ okuyucu kararı (KARAR) **703** (702 → 703; 84:15 'basîr' İLÂHÎ).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik her blokta 0 (sûre geneli 25 / 0) · [x/y] **66 sayım, 0 uyuşmaz** (sûre geneli) · e_el=? her blokta 0 · retroaktif gloss yaması hedefli 0, genel 0 · **DUZELTME 1** (84:21).
Sûrenin 25 ayeti üç blokta okundu (1-9, 10-15, 16-25 — sûrenin bölümlerine göre). Dosyalar `yamalar/iskele_84.py` ile mutaffifin_* şablonlarından kuruldu (oturum dışı). Paket `notlar/sure84_insikak_okuma.md` (`insikak_paket_md.py`, 25 başlık). Oturum yeni ortamda temiz klondan başladı (taban **bc3913b**; oturum boyunca ilerlemedi); 84:1-9 2026-10-29 akşamı, 84:10-25 2026-10-30 sabahı (ortam korunmuştu). Ara zip `fark_bc3913b_sure84_ara1.zip`; son zip `fark_bc3913b_sure84.zip`.

### Sûre 84 bilançosu (TAM SAYIM, `okuma_metni['84']['_bilanco_sure']`)
107 kelime · **lafız 1 (84:23) · Rab 4 (84:2, 5, 6, 15)** — sûre bütünü Rab [4/4] · edilgen 7 (84:2, 3, 5, 7, 8, 10, 21) · iltifât ölçümü 4 (84:16, 17, 19, 20; 84:17 fiil şahsından, 924) · hapaks 1 ayet (84:6 — yeni kök) · mm2 1 (84:8).
Yıldız 0:14 · ★1 (84:14 — kaynak 'n' etiketli, kafiye kırığı, 1001) · ★★1 (84:21 pas) · ★★★9 (rab 84:2, 5, 15; pas 84:3, 7, 8, 10; hapaks 84:6; allah 84:23 — içerik iddiası değil).
Fâsıla metin ت 5 / ه 3 / ا 6 / ر 1 / ق 4 / ن 5 / م 1; ölçüm kafiye kırığı 2 (84:10, 14 — gerçek); işaretlenmeyen gerçek geçişler 84:5 → 6, 7 → 8, 10 → 11, 14 → 15, 15 → 16, 19 → 20 (924). En uzun 9 kelime (84:25); en kısa 2 kelime (84:12). Sayı işareti 0.
Sûre içi esit2 TAM: 84:2 / 5 ('ve ezinet li-rabbihâ ve huqqat' — gök / yer). nakarat3 84:7 / 10 süzgeç GEÇMEZ. Dış esit2 YAKIN: 84:25 → 41:8 (95:6 henüz okunmadı).

### Çıpa (ölçüt değişmedi)
L4 yok. L2 yok. L1 3 (84:1, 3, 4 — âhirette kozmik olay: gök, yer). L0 3 (84:16 şafak, 84:17 gece, 84:18 ay — yemin edilen; 81:17-18 kaydı emsali). Olgu değil 19. Tarayıcı v4 adayı 0.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
1 e_oto tokeni → İLÂHÎ (84:15 'basîr', Rab'ın sıfatı). §4.3 ölçüm mührü 1 → geçerli **1** (84:15; ölçüm satırı 'MÜHÜRSÜZ' yazıyordu — 1022).

### Kendi kaydı
Kayıttan önce: 84:24 ◇ basılmamış okunmuş ayet numarası → sayı. Kayıttan sonra: 84:21 ◇ 31:7 / 45:8 'fe-beşşirhu' ile 84:24 'fe-beşşirhum' 'aynı' yazılmıştı — DUZELTME 84:21 (özgün alan korunur). İlk yazımda DUZELTME 'aday' alanı yanlış numarayla (1017) girildi; okuma_metni'nden temizlenip `aday=None` ile yeniden koşuldu (DUZELTME aday anahtarı dersi). Kök سرر gloss gözlemi 84:9 için kayıttan sonra görüldü — 10-15 ARIZA'sına yazıldı, 84:9 kaydı değişmedi.

### Aday 1041 — kayıt (sûre 84)
Kayıt yok ('kâne' 84:13 insan / 84:15 Rab — bağlayıcı fiil, bölünme sayılmadı).

### Aday 1040 — kayıt (test korpus sonunda)
83:36 / 84:1 sûre sınırı (soru + 3MP / şart zarfı + 3FS; ikisi de lafızsız, Rabsız; fâsıla ن → ت). Ardışık sûre okuma bağları: 83:31 / 84:9, 13 ('inqalebe ilâ ehl' + hâl; dünyada keyif / sevinç); 83:4 / 84:14 ('zanne' + diriliş); 83:16 / 84:12 (kök صلي). İki sûre önceyle: 82:1 / 84:1 ('ize's-semâ'' + VII. bab), 82:6 / 84:6 ('yâ eyyuhe'l-insân' + 'rabbike'), 82:15 / 84:12 ('yaslâ'). 84:25 → 85:1 henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
25 ayetin hepsinde not; ayet içi çift 0, ayetler arası 8 (84:1 / 3; 84:7 / 10; 84:8 / 11; 84:9 / 12; 84:9 / 13; 84:14 / 15; 84:20 / 25; 84:24 / 25). Karşılaştırma yapılmadı.

### Mevcut ailelere girenler
* 1017: edilgen failler (84:2, 3, 5, 7, 8, 10, 21); konuşan adsız (84:16 1S); muhatap 'el-insân' (84:6), 2MP (84:19), 2MS (84:24 — 84:6 ile aynılığı KAPATILAMAZ). KAPATILAMAZ: 84:1-5 şart cevabı, 84:4 'mâ fîhâ', 84:6 'mulâqîhi', 84:17 'mâ vesaq', 84:19 katlar, 84:22 yalanlanan, 84:23 biriktirilen, 84:25 istisna.
* 1021: لقي, أذن ('ezine'), سرر ('mesrûr'), حور, شفق, وسق, وعي.
* 1022: 84:15 ölçüm 'MÜHÜRSÜZ' / geçerli mühür.
* 1001: 84:14.
* 924: ayet 1 harf alanı; şart zarfı / 'inne' / 'belâ' kip alanında yok; atıflı yeminlerde QASEM yok; fâsıla geçişleri işaretlenmiyor; 84:17 iltifât fiil şahsından.

## SÛRE 85 BURÛC SONU (2026-10-30)

**Okunan: 4723 / 6236 ayet (%75,7)** — sûre 1 ve 9-85 TAM, sûre 2 kısmi (1-20). İlerleme `buruc_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1511** (sûre 85'te yeni kök yok). Aday havuzu **1041** (sûre 85'te yeni aday yok; `AX_buruc` boş). Bağ **AS_buruc** 45. Esmâ okuyucu kararı (KARAR) **714** (703 → 714; 7 İLÂHÎ, 4 DEĞİL).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik her blokta 0 (sûre geneli 22 / 0) · [x/y] **63 sayım, 0 uyuşmaz** (sûre geneli) · e_el=? her blokta 0 · retroaktif gloss yaması hedefli 0, genel 0 · **DUZELTME 0**.
Sûrenin 22 ayeti üç blokta okundu (1-9, 10-16, 17-22). Dosyalar `yamalar/iskele_85.py` ile insikak_* şablonlarından kuruldu (oturum dışı). Paket `notlar/sure85_buruc_okuma.md` (`buruc_paket_md.py`, 22 başlık). Taban **bc3913b** (sûre 84 zip'i yüklenmeden okundu); ara zip `fark_bc3913b_sure85_ara1.zip`; son zip `fark_bc3913b_sure85.zip` (sûre 84 + 85).
**Kullanıcı isteği (2026-10-30):** 85:17-22 bloğundan itibaren emsal listesinde her ayetin Türkçe meali de verilir — okunmuş ayetin meali `okuma_metni` kaydından alınır, elle yazılmaz.

### Sûre 85 bilançosu (TAM SAYIM, `okuma_metni['85']['_bilanco_sure']`)
109 kelime · **lafız 3 (85:8, 9, 20) · Rab 1 (85:12)** · A/R 3,0 · edilgen 1 (85:4) · iltifât ölçümü 2 (85:12, 13) · hapaks 0 · mm2 0.
Yıldız 0:18 · ★1 (85:8 allah) · ★★★3 (85:4 pas; 85:12 rab; 85:20 allah — içerik iddiası değil).
Fâsıla metin د 16 / ج ق ر ب ط ظ birer; ölçüm kafiye kırığı 0 — gerçek geçişler işaretlenmedi (924). En uzun 14 kelime (85:10, 11); en kısa 2 kelime (85:2, 3, 18). Sayı işareti 0.

### Çıpa (ölçüt değişmedi)
L4 yok. L2 yok. L1 1 (85:1 burçlu gök). L0 1 (85:9 mülk tamlaması). Olgu değil 20. Tarayıcı v4 adayı 0.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
11 e_oto tokeni → İLÂHÎ 7 (85:8 ×2, 9, 14 ×2, 15, 20), DEĞİL 4 (85:7, 10 'mu'min'; 85:11 'kebîr'; 85:21 'mecîd' — Kur'ân). §4.3 ölçüm mührü 8 → geçerli **5** (85:8, 9, 14, 15, 20); yanlış 3 (85:7, 11, 21) (1022). 85:15 'el-mecîdu' merfû — 'zû'nun sıfatı; karar metindeki i'râbdan.

### Kendi kaydı
Kayıttan önce: 85:11 ◈K tetik koşusuyla dolduruldu (نهر); 85:12 kök بطش sayısı düzeltildi; 85:22 ◇'de okunmamış ayet numarası sınır notundan çıkarıldı. Kayıttan sonra: yok.

### Aday 1041 — kayıt (sûre 85)
شهد 85:7 (hendeğin sahipleri) / 85:9 (Allah); فعل 85:7 / 85:16 (Rab); 'mecîd' 85:15 (Rab) / 85:21 (Kur'ân).

### Aday 1040 — kayıt (test korpus sonunda)
84:25 / 85:1 sûre sınırı (istisna + 3MP / yemin, şahıs işareti yok; ikisi de lafızsız, Rabsız; fâsıla ن → ج). Ardışık sûrede iki ayetlik sıralı eşleşme 84:22-23 / 85:19-20 ('beli'llezîne keferû' + yalanlama → 've'llâhu' + lafız + haber). Okuma bağı 84:25 / 85:11 ('illâ' / 'inne'). 85:22 → sonraki sûre henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
22 ayetin hepsinde not; ayet içi 4 (85:3, 7, 10, 13), ayetler arası 2 (85:10 / 11; 85:19 / 21). Karşılaştırma yapılmadı.

### Mevcut ailelere girenler
* 1017: edilgen failler (85:2, 4, 22); 'ashâbu'l-uxdûd', 'el-mu'minîn'; muhatap 2MS (85:12, 17). KAPATILAMAZ: 85:1-3 yemin cevabı, 85:3, 85:10 aynılık, 85:13 nesne, 85:19, 85:21 zamir, 85:22 levha.
* 1021: نور, خدد, لوح.
* 1022: 85:9, 15, 20 ölçüm 'MÜHÜRSÜZ' / geçerli; 85:7, 11, 21 ölçüm mührü / geçersiz.
* 1038: 85:18 Firavun / Semûd rol mecrur; 85:21 'qur'ân' rol fail.
* 924: atıflı yeminlerde QASEM yok; 'iz', 'inne', fasl zamiri kip / biçim alanında yok; fâsıla geçişleri işaretlenmiyor.

## SÛRE 86 TÂRIK SONU (2026-10-30)

**Okunan: 4740 / 6236 ayet (%76,0)** — sûre 1 ve 9-86 TAM, sûre 2 kısmi (1-20). İlerleme `tarik_kapanis.py` ile kayıttan koşuldu.
`kok_turkce.json` **1512** (1511 → 1512; `kok_ekle_86.py`: دفق 86:6). Aday havuzu **1041** (sûre 86'da yeni aday yok; `AX_tarik` boş). Bağ **AS_tarik** 31. Esmâ KARAR **714** (değişmedi).
Denetimler her blokta ve kapanışta: türkçe **0** · anahtar **70 = taban**, diff 0 · tetik her blokta 0 (sûre geneli 17 / 0) · [x/y] **38 sayım, 0 uyuşmaz** · e_el=? 0 · retroaktif gloss yaması hedefli 0, genel 0 · **DUZELTME 0**.
Sûrenin 17 ayeti iki blokta okundu (1-10, 11-17). Dosyalar `yamalar/iskele_86.py` ile buruc_* şablonlarından kuruldu (oturum dışı). Paket `notlar/sure86_tarik_okuma.md` (`tarik_paket_md.py`, 17 başlık). Taban **bc3913b**; son zip `fark_bc3913b_sure86.zip` (sûre 84 + 85 + 86).

### Sûre 86 bilançosu (TAM SAYIM, `okuma_metni['86']['_bilanco_sure']`)
61 kelime · **lafız 0 · Rab 0** — lafızsız ve Rabsız sûre · edilgen 3 (86:5, 6, 9) · iltifât ölçümü 2 (86:16, 17) · hapaks 2 (86:6, 14) · mm2 2 (86:15, 16).
Yıldız 0:13 · ★★1 (86:5 pas) · ★★★3 (86:6, 9 pas; 86:14 hapaks — içerik iddiası değil).
Fâsıla metin ق 4 / ب 2 / ظ 1 / ر 3 / ع 2 / ل 2 / ا 3; ölçüm kafiye kırığı 0 — geçişler işaretlenmedi (924). En uzun 6 kelime (86:4, 10); en kısa 2 (86:1, 3, 16). Sayı işareti 0.

### Çıpa (ölçüt değişmedi)
L4 yok. L2 yok. L1 6 (86:1, 3, 6, 7, 11, 12). L0 1 (86:5; tarayıcı v4 adayı, çıpa değil). Olgu değil 10.

### Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)
e_oto 0; ölçüm mührü 0.

### Kendi kaydı
Kayıttan önce: 86:13 lemma listesi hakkında toplu iddia → basılan tek ayete indirildi; 86:16 'ölçüm' etiketi düzeltildi. Kayıttan sonra: kök طرق gloss gözlemi (86:1-2) — 11-17 ARIZA'sına yazıldı. DUZELTME 0.

### Aday 1041 — kayıt (sûre 86)
كيد 86:15 3MP (kâfirler) / 86:16 1S (konuşan adsız).

### Aday 1040 — kayıt (test korpus sonunda)
85:22 / 86:1 sûre sınırı (fâsıla ظ → ق; ikisi de lafızsız, Rabsız). Ardışık iki sûre 've's-semâ'' yeminiyle açılıyor (85:1 / 86:1). Okuma bağları 85:22 / 86:4 (kök حفظ), 85:1 / 86:11 ('ve's-semâ'i zât'). 86:17 → sonraki sûre henüz okunmadı.

### Aday 1039 — okuma kolu (karşıt çift) verisi
17 ayetin hepsinde not; ayet içi 1 (86:7), ayetler arası 4 (86:8 / 10; 86:11 / 12; 86:13 / 14; 86:15 / 16). Karşılaştırma yapılmadı.

### Mevcut ailelere girenler
* 1017: edilgen failler (86:5-6, 9); 86:4 gözetleyici, 86:8 'innehû', 86:13-14 söz göndergesi adsız; 86:16 1S konuşan; muhatap 2MS (86:2, 17).
* 1021: طرق, صلب, ترب, بلو, مهل (eşsesli).
* 924: 86:4 hasr ISTISNA olarak; atıflı yeminde QASEM yok; fâsıla geçişleri işaretlenmiyor.

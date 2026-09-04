# OTURUM KAPANIŞI — 2026-08-31

## Ne yapıldı

Boru hattı sıfırdan koşturuldu (`defter.py → defter2 → defter3 → defter4 → defter5 →
aktor2 → katman6 → graf2`); `defter.json` 6236 ayet × 39 alan doğrulandı.

**Sûre 23 (Mü'minûn) açıldı:** makro profil sıfırdan çıkarıldı, **SÛRE 23 TAM OKUNDU (118/118)** (sohbete ayet ayet yazıldı; Arapça · meal · `›` ölçüm · `◇` mercek · `▽` dikey).

Okunan ayet **1463 → 1581** (korpusun %25,4'ü). Tam okunan sûre: **1, 9-23**.
Kısmi: 2 (1-20).

Kök tablosu **880 → 916** (14 yeni karşılık: `سلل` · `كسو` · `فكه` · `دهن` · `صبغ` ·
`بقر` · `سنبل` · `عجف` · `لوم` · `وري` · `عبر` · `فور` · `قلل` · `ملأ`). Hepsi
`kok_envanteri.json`'dan NFC eşlemesiyle KOPYALANDI, hiçbiri elle yazılmadı.

Adaylar **464 → 497** (33 yeni, `AE_muminun`). Bağlar: yeni `AC_muminun`, 78 bağ.

## Denetimler

- `turkce_denetim.py` — her blok sonunda koşuldu, **altı kez 0'a çekildi**.
  İlk blokta 17 ihlâl çıktı: 16'sı yeni bloktan, **1'i sûre 14'ten geriye dönük
  açığa çıkan** `لوم` *(kınama, levm)* (yeni kök eklendiğinde eski anmanın
  karşılıksız kaldığı bilinen desen). İkinci blokta 12, üçüncü 22, dördüncü 22, beşinci 22, altıncı 23 ihlâl;
  hepsi "aynı satırda ikinci kez anılan kök" tipinde. Beşinci blokta ayrıca
  `جور` eklenince 9:6'da ikinci bir geriye dönük anma açığa çıktı; onarıldı.
- `anahtar_denetim.py` (PYTHONHASHSEED=0, depo yapısında) **altı kez** koşuldu.
  Her altısında **58 ihlâl, taban listesiyle diff = 0**. Taranan anahtar
  21055 → 21556 (tablo büyümesi ve yeni betikler). Yeni ihlâl yok.

## Sûre 23 makro profili — üç sûrenin karşıtlığı

| | Enbiyâ (21) | Hac (22) | Mü'minûn (23) |
|---|---|---|---|
| ayet / kelime | 112 / — | 78 / 1274 | 118 / 1050 |
| Allah | 6 = 0,15x | 75 = 1,69x | 13 = **0,35x** |
| Rab | 14 = 0,95x | 8 = 0,50x | 23 = **1,72x** |
| A/R | 0,43 | 9,38 | **0,57** |
| kafiye sınıfı | 1 | 10 | **1** |
| esmâ / mühür | 17 / 1 | 38 / 11 | **12 / 0** |
| esmâ hata oranı | %47 | %29 | **%67** |
| tip | Mekkî | Medenî | Mekkî |

A/R üç komşu sûrede **0,43 → 9,38 → 0,57**: Hac tek başına bir tepe. Mü'minûn
Enbiyâ'nın oranına dönüyor ama **aynı yerden değil** — Enbiyâ'da hem lafız hem Rab
düşüktü, burada lafız düşük ve **Rab okumada bugüne dek görülen en yüksek
yoğunlukta**. En uzun Allah-sessizliği 23:39-84 = **46 ayet** (sûrenin %39'u).

Kafiye: **118/118 ayet N sınıfında, kırılma sıfır** — korpusun en uzun tek-kafiye-
sınıfı sûresi; ikincisi Enbiyâ (112), aralarında duran Hac ise 10 sınıfla üst uçta.

## Bulunan araç hataları (hepsi kayıtlı, hiçbiri okuma sırasında onarılmadı)

| aday | konu | büyüklük |
|---|---|---|
| **467** | esmâ: mühür=0 sûrede hata %67; ölçüt (a) ile (b) ÇATIŞIYOR (23:14 `خالِق`) | P0, 461 ile |
| **474** | dikey lemma karışması: `جنن` → 23:25 `جِنَّة` *(delilik)* 'cennet' okunuyor; 7:184 vakası tekrarladı | P0, 452 ile |
| **472** | yıldız formülü kısa ayete kayıyor; ★★★ ort. n=5,69 vs sûre 8,90 | P1, 468 ile |
| **475** | 23:36 i'râb kaydı BOŞ — îrablanan isim yok; i'râb profillerinde eksik sayım riski | P2 |

## Ön-kayıtlı zincir ÖLÇÜLDÜ, TEST EDİLMEDİ (aday 469)

23:1-9 sıfat zinciri, "sıfat-zinciri türü" testinin altı örneğinden biri.
Altı halka, dört ayrı harf-i cer (`فِى` · `عَنْ` · `لِـ` ×3 · `عَلَىٰ`).

- **Halka-sırası:** `لِـ` üç halkada üst üste (23:4, 23:5, 23:8).
- **Hıfz-kapanışı:** 23:9 zincirin **yeni kök getirmeyen tek halkası** — iki kökü de
  (`صلو` 23:2'den, `حفظ` 23:5'ten) daha önce kullanılmış.
- **Üçlü dönüşüm:** 23:9 aynı anda yüklemi ism-i fâilden çekimli fiile, babı I'den
  III'e, `صَلَاة` tekilini `صَلَوَٰت` çoğuluna çeviriyor.

Motive eden ayetler kendi testlerinden **dışlanacak**; test tur sonunda altı örnek
birlikte, Bonferroni ile.

## Bölüt ikizleri — iki büyük girdi

**Aday 465 — korpusun en uzun ardışık tam-ayet ikizi: 23:5-8 ↔ 70:29-32, dört ayet.**
Tarama `defter.json` `esit` alanı üzerinden yapıldı; uzunluk 4 olan tek dizi bu.

**Aday 473 — sûre-içi iki paralel kıssa döngüsü, dört katmanlı ikiz.** 23:23-30
(Nûh, adlı) ile 23:31-41 (adsız elçi): çağrı 23:23 = 23:32 (sekiz kelime birebir) ·
birinci itiraz 23:24 = 23:33 · ikinci itiraz 23:25 = 23:38 (beş kelime sonra
ayrışıyor) · kapanış 23:26 = 23:39 (TAM AYET İKİZİ). Farklılaşan öğeler kodlandı.

## Mercek disiplini

Blok 23:1-20'de tek ★★★ ayet (23:16), blok 23:21-40'ta dört (22, 26, 36, 39).
**Beşinin de biyolog ve uzay merceği ATLANDI** — hiçbirinde çıpa yok. Gerekçeler
`okuma_metni.json` → `_mercek_atlama_notu` alanında ayet ayet kayıtlı.

En dikkat çekici atlama 23:22: `فلك` *(gemi, felek)* kökü korpusta hem gemi hem
yörünge işlevinde, ama bu ayette `حمل` *(taşıma)* ve `أنعام` *(davarlar)* ile
eşleştiği için gönderge açıkça gemi. Gönderge açıkken astronomik okumayı seçmek
yasaklı "bilimsel izdüşüm" hamlesi olurdu; mercek yazılmadı.

## Üçüncü blok (23:41-60) — üç kıssa döngüsü ve ikinci zincir

Sûre 23'ün kıssa bölümü **üç döngü** hâlinde ölçüldü ve döngüler giderek kısalıyor:
23:23-30 (Nûh, sekiz ayet) · 23:31-41 (adsız elçi, on bir ayet) · 23:45-48
(Mûsâ ve Hârûn, **dört ayet**). Üçüncü döngüde yalanlama ile helâk arasına hiçbir
aşama konmuyor. 23:44 ise önceki on ayetin anlattığını tek formüle indiriyor ve
ardıllığı üç ayrı sözcükle üst üste işaretliyor (`تَتْرَا` *(ard arda)* ·
`فَأَتْبَعْنَا` *(peşi sıra getirdik)* · `بَعْضَهُم بَعْضًۭا` *(kimini kiminin ardından)*).

**Sûrenin ikinci sıfat zinciri 23:57'de açıldı (aday 477)** ve birinciyle aynı
kalıbı, ayrı ekseni taşıyor: birinci zincir eylemlere, ikincisi Rab'be bağlı.

## Bekleyen iki bağ KAPANDI

**23:31 ↔ 23:42** — sûre-içi bölüt ikizi; tek fark `قَرْنًا` *(bir nesil)* tekil →
`قُرُونًا` *(nesiller)* çoğul. Birinci geçişte tek topluluk anlatılıyor (23:31-41),
ikincisinde kalanlar tek çoğulda toplanıp anlatılmıyor.

**21:92-93 ↔ 23:52-53 (aday 456) — ÖN-KAYIT YANLIŞ ÇIKTI (aday 476).** Beklenti
"fark tam olarak imperatifte" idi; ölçüm birinci ayette İKİ fark verdi: açılışta
bağlaç, kapanışta imperatif. İkinci ayette ayrışma çok daha geniş. Aday 456'nın
metni 476 ile düzeltilmelidir.

## Dördüncü blok (23:61-80) — dört `أَمْ` ve üç `وَهُوَ ٱلَّذِى`

**İkinci sıfat zinciri 23:61'de kapandı** ve kapanış birinci zincirinkiyle aynı
hamleyi yaptı: `ٱلَّذِينَ هُمْ` *(onlar ki)* dizisi `أُو۟لَٰٓئِكَ` *(işte onlar)* ile
kapanıyor (23:10 ↔ 23:61). Kapanışta Rab da düşüyor — dört halkanın dördünde vardı.

**Aday 438'e okuma içinden ilk temiz vaka kümesi (aday 483):** 23:68-72'de dört
`أَمْ`, üçü ayet başında (munkatı'a) ve **üçü de INTG almıyor.**

**Yeni P0 vakası (aday 484):** üstünlük tamlaması kalıbı sûrede üç kez, hep aynı
yapıda, ama esmâ tablosu yalnız birini sayıyor.

## Beşinci blok (23:81-100) — kaynak metin sorusu açıldı

**YENİ P0 (aday 487).** 23:85/87/89'da korpus üç kez `لِلَّهِ` okuyor; yaygın Hafs
baskısında 23:87 ve 23:89 `ٱللَّهُ` merfûdur. Sorular (`مَن رَّبُّ` · `مَنۢ بِيَدِهِۦ`)
merfû cevap ister — korpusun okuyuşu iki ayette soru-cevap uyumsuzluğu üretiyor.
**Korpusun hangi kıraati taşıdığı projede ilk kez soruluyor.** `nuzul.json` ile
aynı statüde: doğrulanmadan bulgu kapatılamaz.

**Mercek disiplini — sûrenin ilk merceği 23:86'da yazıldı.** 100 ayetin on beş
★★★'ından on dördünde iki mercek de atlandı; tek yazılan 🜂 uzay, çıpası
`ٱلسَّمَٰوَٰتِ ٱلسَّبْعِ` *(yedi gök)* ve yalnız ölçülebilirle sınırlı tutuldu.
**Biyolog merceği sûrede hâlâ hiç yazılmadı.**

**Yapı ölçümleri:** üçlü soru-cevap nakaratı 23:84-89 (kapanış fiilleri bab V →
VIII → I, üçüncüsü edilgen) · dört ardışık `رَبِّ` çağrısı ve konum kayması ·
sûrenin tek KELLA'sı 23:100.

## Altıncı blok (23:101-118) — sûre kapandı

**Sûrenin büyük halkası (aday 491):** `فلح` *(kurtuluşa erme, felâh)* kökü açılışta
(23:1, PERF, olumlu), ortada (23:102, ism-i fâil, olumlu) ve kapanışta (23:117,
IMPF, **olumsuz**). Üçünde de fâsıla belirli ism-i fâil çoğulu.

**Sûre kendi içinden bir alıntıyla bitiyor (aday 494):** 23:109'da aktarılan dua
23:118'de emre çevriliyor; altı kelime ortak, nesne zamirleri düşüyor.

**Esmâ tablosunun ikinci tutarsızlık vakası (aday 497):** 23:86 `ٱلْعَظِيمِ` ve
23:116 `ٱلْكَرِيمِ` — aynı terkip, aynı konum, biri esmâ sayılıyor öteki sayılmıyor.

## Sûre 23 mercek bilançosu

118 ayet · on altı ★★★ · **on beşinde iki mercek de atlandı** · tek yazılan mercek
23:86'nın 🜂 uzayı. **Biyolog merceği sûrede hiç yazılmadı.** Sûrenin biyolojik
olarak en yoğun ayetleri (23:12-14 · 23:21 · 23:78 · 23:104) ya ★ almadı ya
çıpasız kaldı. Adaylar 468 ve 472 için ilk tam sûre veri kümesi.

## Devam noktası

**Sûre 24 (Nûr)** — makro profilden başla, sonra 24:1'den oku. Sûre 24 **Medenî**:
A/R oranı karşılaştırmasında (aday 470) tip-eşli ikinci veri noktası olacak.

## Değişen dosyalar (zip'te depo yapısıyla aynı klasörlemede)

```
notlar/okuma_metni.json            (sûre 23 makro + 23:1-40 + ilerleme)
notlar/mercek_kayit.json           (23 → 40 mercek, 23_atlama yeni)
notlar/okuma_baglantilari.json     (AC_muminun yeni küme, 22 bağ)
notlar/YAPILACAKLAR.md             (2026-08-31 bölümü)
notlar/OTURUM_2026-08-31_KAPANIS.md   (bu dosya)
tablolar/kok_turkce.json           (880 → 894)
bulgular/aday_bulgular.json        (464 → 475, AE_muminun yeni küme)
betikler/blok_23_1_20.py           (YENİ)
betikler/blok_23_21_40.py          (YENİ)
betikler/kok_ekle_23.py            (YENİ — anahtar-kopyalayan kök ekleyici)
```

## Bir sonraki oturuma uyarı

`turkce_denetim.py` bu oturumda **iki ayrı ihlâl tipi** yakaladı ve ikisi de
yazım alışkanlığından geliyordu: (1) yeni kök eklendiğinde ESKİ sûrede karşılıksız
anma açığa çıkıyor; (2) aynı ölçüm satırında bir kök ikinci kez anıldığında
karşılık düşürülüyor. **İkincisi kural ihlâli — "kök adları her geçişte karşılık
alır" maddesi istisnasız.** Blok yazarken kök listelerinde her öğeye karşılık
konmalı, kısaltma yapılmamalı.

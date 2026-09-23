# ÖN-KAYIT — İnsân'a en yakın fiil: خلق (yaratmak) bütün Kur'an'da

Yazıldı: 2026-09-18T10:55:28Z · ÖLÇÜMDEN ÖNCE · morph.txt sha256[:16] = 742bfac59941b2cb
Öncül: `insan_yigin` — insân'a en yakın fiil sütununda خلق 14 kez birinci.

## Tanımlar
- **Fiil tokeni:** POS = V ve ROOT:خلق. İsim biçimleri (خَلْق, خالِق, مَخْلُوق) ayrı sayılır, testlere girmez.
- **Özne:** fiil segmentindeki kişi etiketi (1P · 3MS · 2MP …). Etken ve edilgen ayrı tutulur.
- **Nesne — sezgisel kural (etken fiil):**
  1. Fiil kişisi ek alan türdense (1S, 1P, 2*, 3MP, 3FP, 3D), fiile bitişik ilk PRON SUFF öznedir, sonrakiler nesnedir. Aksi hâlde (3MS, 3FS) bütün bitişik PRON SUFF'ler nesnedir.
  2. Bitişik nesne yoksa: fiilden sonraki 4 kelime içinde ilk ACC isim (edatla bağlı olmayan, اللَّه hariç).
  3. İkisi de yoksa "belirsiz".
- **Nâib-i fâil (edilgen fiil):** fiilin kişisi veya sonraki 3 kelimede ilk NOM isim.
- **Doğrulama:** kural çıktısından tohum 0 ile 25 fiil rastgele seçilir ve elle denetlenir. Hata oranı raporlanır.
  Hata oranı > %20 ise nesne dağılımı KAPATILAMAZ sayılır.

## Ölçümler (betimsel — test ailesi yok)
- **Ö1** fiil tokeni sayısı · ayet sayısı · sûre sayısı · Mekkî oranı
- **Ö2** özne dağılımı: kişi × etken/edilgen
- **Ö3** nesne dağılımı: zamir (kişi) ya da isim lemması. İnsân nesneler arasında kaçıncı?
- **Ö4** Allah dışında özne: fiilin özneyi Allah'tan başkası (siz / onlar / Îsâ) olarak kurduğu ayetler, ayrı liste
- **Ö5** dikey sütun: fiilin ayetteki göreli konumu; ayetin ilk kelimesi olma oranı

## Tahminlerim
- **T1** Fiil tokeni 150-250 arası.
- **T2** 1P ("biz yarattık") + 3MS ("o yarattı") etken fiillerin ≥ %70'i.
- **T3** En sık nesne 2MP zamiri ("sizi"). İlk 5 nesne arasında سَماوات ve إِنسان var.
- **T4** Edilgen tokenlerin ≥ %50'sinde nâib-i fâil insân veya insana gönderen bir zamir.
- **T5** Mekkî oranı ≥ %80.
- **T6** Ö4 listesinin çoğunluğu olumsuz ya da meydan okuma bağlamında (yaratamazlar / ne yarattılar?). Yalnız betimsel, sayıyla desteklenir.

---
## SONUÇ (ölçümden sonra eklendi; yukarısı değiştirilmedi)
Betik: `betikler/dikey/fiil_khalk.py` · çıktı: `ciktilar/fiil_khalk.json`

### Doğrulama (tohum 0, 25 fiil, elle)
- Doğru 19 · yanlış 5 · kaçırma 1 → hata **6/25 = %24 > %20** → **Ö3 nesne dağılımı KAPATILAMAZ.**
  Kaçırma sayılmasaydı oran tam %20 olurdu; lehte okuma seçilmedi.
- **Yanlışların 5'i de aynı sebepten:** nesne "ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ" ve "gökler" atlanıyor.
- **Morfoloji tutarsızlığı (TAM SAYIM):** etken خلق/فطر fiilinin hemen ardındaki ٱلسَّمَٰوَٰت (nesne konumu) 29 vakada ACC 9 · **GEN 20**.
  Korpus genelinde سماوات (FP): GEN 168 · ACC 13 · NOM 9.
  Defterdeki `irab` alanı bu etiketleri kullanıyor. **Dondurulmuş borç: kaydedildi, onarılmadı.**

### Tahminler
- **T1 TUTTU:** 184 fiil tokeni · 168 ayet · 71 sûre.
- **T2 TUTTU:** 1P + 3MS = etken fiillerin %87,3'ü (3MS 109 · 1P 42).
- **T3 KAPATILAMAZ:** Ö3 doğrulamadan geçemedi.
  Ham sıra (belirsiz 38 hariç): 2MP zamiri 26 · أرض 22 · 3MS zamiri 12 · سماء 12 · إنسان 10. سماء sistematik olarak eksik sayılıyor.
- **T4 TUTTU (elle):** edilgen 11 tokenin 6'sında nâib-i fâil insân veya insanlar (4:28, 21:37, 52:35, 70:19, 86:5, 86:6).
  Öteki 5: putlar 3 (7:191, 16:20, 25:3) · deve 88:17 · şehir 89:8.
- **T5 TUTTU:** Mekkî %84,2.
- **T6 TUTTU (elle):** Allah dışı gerçek özne 10 token.
  - Olumsuz ya da meydan okuma 8: 13:16, 16:20, 22:73, 25:3, 35:40, 46:4, 52:36, 56:59.
  - "Yalan uyduruyorsunuz" 1: 29:17.
  - İzinle 1: 5:110, Îsâ.

### Ön-kayıttaki tanım hatam
Ö4, "Allah dışı özne"yi kişi etiketinden kuruyordu. Ama 2MS ("sen yarattın") 8 tokenin 7'sinde hitap Allah'a:
- **İblis 6:** 7:12 ×2 · 15:33 · 17:61 · 38:76 ×2
- mü'minler 1: 3:191
Kişi etiketi özneyi değil hitap yönünü veriyor. T6 bu yüzden elle değerlendirildi.

### Ölçüm sonrası (ön-kayıtsız, KAPATILAMAZ)
- "Sen yarattın" diye Allah'a en çok hitap eden İblis: 8 tokenin 6'sı. Hepsi üstünlük iddiası bağlamında (ateş / çamur).
- Edilgen insân ayetlerinin hepsi yaratılışa bir SIFAT ya da MADDE ekliyor: zayıf, aceleden, helû', atılan sudan.

## Sonradan eklenen kaçırma (sûre 31 okuması, blok 2)
31:11 "مَاذَا خَلَقَ ٱلَّذِينَ مِن دُونِهِۦ": fiil 3MS etiketli, özne "O'ndan başkaları" (çoğul ilgi zamiri).
Kişi-etiketi kuralı bu ayeti "Allah dışı özne" listesine almadı (kayıtta 3MS, ACT).
Kişi etiketinin özneyi vermediği ikinci vaka (ilki 2MS hitap).
Ö4 ve T6 elle değerlendirmesi bu ayet eklenerek güncellenmeli: 11 token, meydan okuma 9.

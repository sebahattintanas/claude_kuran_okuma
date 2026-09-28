# ÖN-KAYIT — Esmâ katmanlarına göre dikey sınıflandırma

**Durum:** TASLAK. Ölçüm yapılmadı.
**Yazıldığı an:** okuma 2.325 / 6.236 ayet (%37,3), Secde (32) tamam.
**Uygulama zamanı:** Tam okuma bittikten sonra. Tur sonu toplu testle birlikte yapılır.
**Dondurma:** İlk çalıştırmada repo commit hash'i ve `esma_listesi.json` SHA-256'sı bu dosyanın sonuna yazılır. O andan sonra tanım, eşik ve hipotez değişmez. Her değişiklik §8'e sapma olarak kaydedilir.

---

## 1. Soru

Kur'an ayetleri ve sureleri, ilâhî isim katmanlarına göre rastlantıdan ayırt edilebilir bir yapıda mı sınıflanıyor?

Burada "esmâ katmanı" üç eksenden oluşur:
- **İsim katmanı:** Ayette hangi ilâhî isimlerin geçtiği.
- **Mühür tonu:** Ayet sonundaki esmâ çiftinin tonu.
- **Mesafe bandı:** Ayetteki kavramların Allah lafzına uzaklığı.

## 2. Önceki bilgi ve kaynağı

Bu bulgular sınıflandırmayı motive ediyor. Ancak **hipotez olarak yeniden test edilmezler**, çünkü aynı korpustan türetildiler ve yeniden test etmek döngüsel olur.

| Bulgu | Kaynak | Nasıl bulundu |
|---|---|---|
| Rab 0/980 mutlak geçiş; Allah tarafı ve Rab tarafı kavram kümeleri | `bulgu_rab_allah.json` | ararken bulundu |
| 35 kavramın Allah-mesafesi gradyanı | `bulgu_allah_gradyan.json` | ararken bulundu; düz null ile |
| Tâhâ'nın A/R oranı 0,22; A'râf'ın Rab-baskın olması; Nûr'un sıfır-Rab olması | okuma | okurken fark edildi |
| Esmâ dağılımı 21 cemâl / 4 denge / 2 celâl | `varlik_katalog.json` | geleneksel liste etiketi |

**Yasak:** Allah tarafı ve Rab tarafı kavram listeleri bu çalışmada bağımlı değişken olarak kullanılmaz.

## 3. Veri ve temizlik

- **Kaynak:** `morph.txt` (LEM alanı) ve `defter.json`.
- **Kirli alanlar kullanılmaz:** `kuran_veri.json` içindeki `harf`, `fHz`, `sesli`, `ebced`, `mod19` ve `bits` alanları besmele kirlenmesi taşıyor. Uzunluk ölçüsü olarak `mora` ve `ar_saf` kullanılır.
- **Nakarat:** Ana analiz `nakarat3` (onarım 17, aday 942 — 3 kelimelik lemma dizisi) ile tekilleştirilmiş veri üzerinde yapılır. `nakarat2` ile tekilleştirilmiş sonuç ve tekilleştirilmemiş sonuç iki ayrı duyarlılık kolu olarak raporlanır. *(Dondurma öncesi karar D1, 2026-09-28.)* Gerekçe: Rahmân'daki nakarat ve Şuarâ'daki "Rab + azîz-rahîm" nakaratı, isim katmanını ve mühür tonunu tek başına şişirebilir.
- **Besmele:** Ayet sayılmayan besmeleler hariç tutulur. Fâtiha 1:1 dahil edilir ve ayrıca işaretlenir.

## 4. Operasyonel tanımlar

### 4.1 Eksen A — İsim katmanı (ayet düzeyi)

Her ayet için üç ikili bayrak tanımlanır:

- **`a`:** Ayette `LEM` değeri Allah lafzı olan en az bir token var. "Allâhümme" ayrı bir lemma olarak sayılır ve ayrıca raporlanır.
- **`r`:** Ayette `LEM` değeri Rab olan en az bir token var. Aynı kökten gelen diğer lemmalar (rabbânî, rabâib, ribbiyyûn) sayılmaz.
- **`e`:** Ayette §4.2'deki doğrulanmış esmâ setinden en az bir lemma var.

Bu bayraklardan beş sınıf türetilir:
- **A:** yalnız `a`
- **R:** yalnız `r`
- **AR:** `a` ve `r` birlikte
- **E:** `e` var, `a` ve `r` yok
- **0:** hiçbiri yok

Bu tanımda `e` bayrağı sınıfı yalnızca A ya da R olmadığında belirler. `e` ayrıca ortogonal bir değişken olarak da raporlanır.

**Ölü etiket koruması:** Her lemma etiketinin korpusta en az bir eşleşme vermesi `assert` ile zorunlu tutulur. Gerekçe: yanlış yazılmış bir etiket hata vermez, sadece hiç eşleşmez. Bu hata daha önce `ريح` ve `زتن` köklerinde yaşandı.

### 4.2 Doğrulanmış esmâ seti

- **Başlangıç:** Dondurulmuş `esma_listesi.json`.
- **Doğrulama:** Her girdinin `morph.txt` içinde bir LEM karşılığı olmalı. Anahtarlar NFC normalizasyonuyla korpustan kopyalanır, elle yazılmaz.
- **Eşleşmeyen girdi:** Setten düşer ve listelenir. Tahminle düzeltilmez. **Tek istisna (D2):** yazım farkından eşleşmeyen iki girdi, girdi bazında ve yalnız isim (N) konumunda, `esma_kayit.py` içindeki eşleme tablosuyla korpus lemmasına bağlanır: `هادٍ` → `هاد` (tenvin; ACT_PCPL, 7 ayet) ve `حَىّ` → `حَيّ` (ى/ي harf farkı; 24 ayet). Aynı iskeletteki fiiller (`هادُ` 'Yahudi oldular', `حَيَّ` 'selamladı') açıkça dışarıdadır. Genel hareke/tenvin normalizasyonu YAPILMAZ. `esma_listesi.json` ve SHA'sı değişmez.
- **Kapsam sınırı:** Aynı lemma ilâhî isim olmayan bağlamda da geçebilir (mü'min = inananlar, âhir = âhiret günü, kebîr = lânetin sıfatı). Bu nedenle `e` bayrağı yalnız göndergesi Allah olan konumlarda verilir. **Üç sürüm tutulur (D4):**
  - **`e_suzgec` — ANA TANIM.** Morfoloji ve sözdiziminden otomatik konum süzgeci. Bir esmâ tokeni şu konumlardan birindeyse ilâhî sayılır: (i) öznesi Allah lafzı ya da O'na dönen zamir olan kâne / inne cümlesinin haberi; (ii) kefâ bi-llâhi kalıbında temyiz; (iii) Allah lafzının ya da O'na dönen zamirin sıfatı / bedeli; (iv) nidâ ya da isnatla doğrudan Allah'a verilen ad. Olumsuzlanan 'Allah'tan başka' birine verilen sıfat, başka bir ismin sıfatı ve insan göndergeli kullanım sayılmaz. Süzgeç kodu, araç dondurması gereği **tam okuma bittikten sonra** yazılır.
  - **`e_el` — geliştirme ve doğrulama referansı; süzgeç eşiği geçemezse YEDEK ANA TANIM.** Okuyucu kararı, yukarıdaki kuralın elle uygulanması; `esma_el.py` içinde konum anahtarıyla. Okuma boyunca toplanan kararlar süzgecin **geliştirme kümesi**dir. Okuma bitince, testlerden hemen önce, daha önce okunan sûrelerdeki (1, 9-32, 2:1-20) 794 token için yapılacak geriye dönük karar turu süzgecin görmediği **doğrulama kümesi**dir.
  - **`e_oto` — üst sınır, duyarlılık kolu.** Lemma eşleşmesi, konum bakılmaz.
  - **Kabul eşiği:** *(onay bekliyor — bkz. §8 D4)*.

### 4.3 Eksen B — Mühür tonu (ayet düzeyi)

- **Mühür:** Ayetin son üç içerik lemmasında (N, ADJ ya da PN) §4.2'nin ana tanımına (`e_suzgec`) göre ilâhî sayılan en az bir esmâ tokeni bulunması. Çift mühür, ton ve A/R/E/0 sınıfı da aynı ana tanımdan türetilir; `e_el` ve `e_oto` sürümleri ayrıca hesaplanır (D4). Tanım token düzeyinde değil lemma düzeyindedir, çünkü token düzeyindeki bayrağın iki vakada çalışmadığı görüldü.
- **Çift mühür:** Son üç içerik lemmasından ikisinin esmâ olması.
- **Ton (D3):** Ön-kaydın kendi tablosu `esma_ton.json`'dan: 72 lemmanın her biri için cemâl, denge ya da celâl ve tek satırlık gerekçe. Tablo, **önceden yazılıp onaylanan bir ölçütün** mekanik uygulamasıdır; ölçüt §4.3.1'de. `varlik_katalog.json` kullanılmaz ve değiştirilmez. Tonsuz kalan durum 'eksik' değerini alır. Çift mühürde iki farklı ton varsa 'karma'; bir üye tonsuzsa diğerinin tonu alınır ve 'kısmi' işareti konur. azîm listede olmadığı için tabloya girmez (bilinen eksik).

#### 4.3.1 Ton ölçütü

*(onay bekliyor — bkz. §8 D3)*
- **Uyarı:** Ton etiketi geleneksel sınıflandırmaya dayanır. Bu yüzden ton dağılımının kendisi (örneğin "cemâl-baskın") **hipotez değildir**. Yalnızca tonun başka, bağımsız ölçülen değişkenlerle ilişkisi test edilir.

### 4.4 Eksen C — Mesafe bandı (ayet düzeyi)

**Kapı koşulu:** Önce 35 kavramlık gradyan, pozisyon-eşli null ile yeniden test edilir (aday 435'in borcu). Yalnızca bu testte anlamlı kalan kavramlar bant hesabına girer.

**Kavram bandı:** Pozisyon-eşli testte elde edilen medyan kelime-mesafesine göre belirlenir:
- **merkez:** ≤ 5
- **orta:** 6–20
- **çeper:** > 20

Bu eşikler şimdi sabitlenir. Yeni medyanlar bir kavramı bant değiştirirse bu durum raporlanır, ama eşikler değişmez.

**Ayet bandı:** Ayetteki anlamlı kavram tokenlarının bantlarının çoğunluğu alınır. Eşitlikte daha merkezde olan bant seçilir. Anlamlı kavram içermeyen ayet "bantsız" sayılır.

### 4.5 Sure profili

Her sure için şu değerler hesaplanır:
- A, R, AR, E ve 0 sınıflarının payları
- Mühürlü ayet payı ve ton dağılımı
- Merkez, orta ve çeper bant payları

Her değer, Laplace +1 düzeltmesiyle bir log-oran olarak ifade edilir. Tek ayetli ya da 5 ayetten kısa sureler profile girer, ama H4 kümelemesinde ağırlığı ayet sayısıyla sınırlanır.

## 5. Doğrulayıcı hipotezler

Doğrulayıcı hipotezler dört tanedir, daha fazlası yoktur. Bunların dışındaki her gözlem keşifsel olarak etiketlenir.

**H1 — Sure düzeyinde isim ayrışması**
- **Hipotez:** R payının sureler arasındaki yayılımı, ayet uzunluğu ve sure içi konum sabit tutulduğunda rastlantıdan büyüktür.
- **Null:** A, R, AR, E ve 0 etiketleri, aynı mora bandı ve aynı konum üçte-birliği (baş, orta, son) içinde sureler arasında karıştırılır. 10.000 permütasyon yapılır.
- **İstatistik:** Sure R paylarının ayet sayısıyla ağırlıklandırılmış varyansı.

**H2 — Mühür tonu ile isim katmanı ilişkisi**
- **Hipotez:** Celâl ve denge tonlu mühürler A sınıfında, cemâl tonlu mühürler R sınıfında rastlantıdan sık görülür.
- **Null:** Ton etiketleri sure içinde karıştırılır. 10.000 permütasyon yapılır.
- **İstatistik:** Mühürlü ayetlerde ton × sınıf (A ve R) tablosunun log-odds oranı.
- **Not:** Celâl sayısı küçük olabilir (listede 2 isim var). Hücre sayısı 5'in altında kalırsa, önceden sabitlenmiş kural olarak celâl ve denge birleştirilir.

**H3 — Mühür ve mesafe bandı**
- **Hipotez:** Mühürlü ayetlerin bant dağılımı, mühürsüz ayetlere göre merkeze kaymıştır.
- **Null:** Mühür bayrağı aynı mora bandı ve aynı a/r durumu içinde karıştırılır. 10.000 permütasyon yapılır.
- **İstatistik:** Merkez payı farkı.
- **Koşul:** Yalnızca §4.4'teki kapı açılırsa test edilir. Kapı açılmazsa H3 "test edilemedi" olarak raporlanır, düşürülmez.

**H4 — Sınıflandırmanın varlığı**
- **Hipotez:** Sure profilleri, rastlantıdan daha belirgin bir küme yapısı gösterir.
- **Yöntem:** Profil vektörleri standartlaştırılır. k = 2…6 için hiyerarşik kümeleme (Ward) uygulanır. En iyi k, siluet skoruna göre seçilir.
- **Null:** Ayet etiketleri H1'deki gibi tabakalı karıştırılır, profiller yeniden hesaplanır ve aynı k-seçim süreci uygulanır. 1.000 permütasyon yapılır.
- **İstatistik:** En iyi siluet skoru. Seçim sürecinin kendisi de null içinde tekrarlandığı için bu skor "k seçme serbestliği" açısından düzeltilmiş olur.
- **Olumlu sonucun anlamı:** Olumlu sonuç yalnızca "yapı var" demektir. Kümelere ad verme işi (yorum) ölçümden ayrı, ◇ düzeyinde yapılır.

## 6. Karar kuralları

- **Anlamlılık:** Bu ön-kaydın dört testi, tur sonu toplu testin Bonferroni paydasına eklenir. Yerel raporlamada tabanı α = 0,05 / 4 = 0,0125 alınır. Ancak nihai hüküm, global paydaya göre verilir.
- **Etki büyüklüğü:** Her test için p değerinin yanında etki büyüklüğü ve %95 permütasyon aralığı raporlanır.
- **Null sonuçlar:** Olumlu sonuçlarla aynı ayrıntıda yazılır.
- **Duyarlılık:** Şu kollardan herhangi birinde sonuç yön değiştirirse bulgu "kırılgan" olarak etiketlenir: nakaratlı veri · `nakarat2` ile tekilleştirme · `e_el` · `e_oto` (üst sınır).

## 7. Bu ön-kaydın yapmadığı şeyler

- Esmânın cemâl/celâl sınıflandırmasını doğrulamaz. Bu etiketi yalnızca girdi olarak kullanır.
- Mekkî/Medenî ayrımı gibi geleneksel etiketleri değişken olarak almaz.
- Okuma sırasında fark edilen "şu isimle gelen ayetler şöyledir" türü iddiaları test etmez. Bu iddialar ayrı adaylar olarak KAPATILAMAZ statüsünde kalır.
- Araç geliştirmesi yapmaz. Gereken kod, okuma bittikten sonra ve dondurma kararına uygun olarak yazılır.

## 8. Sapmalar

*(Dondurmadan sonra yapılan her değişiklik buraya tarih, gerekçe ve etki bilgisiyle yazılır.)*

### 8.0 Dondurma öncesi karar günlüğü (2026-09-28, kullanıcı kararı)

Hiçbir H testi koşulmadan verildi. Karar sırasında görülen tek veri sûre 33'ün KAYDI (aday 996); bu bulaşma riski burada açıkça yazılır.

- **D1 — nakarat:** ana `nakarat3`, duyarlılık `nakarat2`. Gerekçe: `nakarat2` onarılmamış, bilinen yanlış pozitifi var (10:2 ↔ 10:76); okuma `nakarat3` ile koşuluyor. §3'te işlendi.
- **D2 — Hâdî / Hayy:** girdi bazında düzeltme, yalnız isim (N), eşleme tablosu; genel normalizasyon yok. Gerekçe: iki girdinin eşleşmeme nedeni farklı (tenvin; ى/ي harfi) ve aynı iskelette fiiller var (`هادُ` 11, `حَيَّ` 4). Düşürme el-Hayy'ı setten çıkarırdı. §4.2'de işlendi.
- **D3 — ton:** ön-kaydın kendi 72 lemmalık tablosu, önce yazılıp onaylanan ölçüte göre; katalog kullanılmaz. Gerekçe: katalog 72 lemmanın yalnız 26'sını kapsıyor ve 26'nın 21'i cemâl (azîz, kadîr, kebîr, alîm dahil) — H2 ekseni neredeyse tek değerli. §4.3'te işlendi. **Ölçüt onayı bekleniyor.**
- **D4 — esmâ bayrağı:** ana tanım otomatik konum süzgeci (`e_suzgec`); `e_el` geliştirme/doğrulama referansı ve yedek ana tanım; `e_oto` duyarlılık. Geriye dönük `e_el` turu tam okuma bitince, testlerden hemen önce. Gerekçe: sûre 33'te `e_oto` ile §4.3 mühürlerinin 12/32'si yanlış, E sınıfı 6'ya karşı 1. §4.2 ve §4.3'te işlendi. **Kabul eşiği onayı bekleniyor.**
- **D5 — kök glossu:** 6 kök (نور بلو ولي حيي دور سدد) şimdi düzeltildi, eski gloss `tablolar/kok_gloss_duzeltme.json`'da, yamalanan ayet kayıtlarında `_gloss_duzeltildi` damgası (`yama_gloss_duzeltme_987.py`). 1112 kökün sistematik taraması borç (P1). Ölçüm etkisi yok.

## 9. Dondurma kaydı

- commit: `________`
- `esma_listesi.json` SHA-256: `________`
- doğrulanmış esmâ seti boyutu / düşen girdiler: `________`

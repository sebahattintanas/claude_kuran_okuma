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
- **Nakarat:** Ana analiz `nakarat2` ile tekilleştirilmiş veri üzerinde yapılır. Tekilleştirilmemiş sonuç duyarlılık analizi olarak ayrıca raporlanır. Gerekçe: Rahmân'daki nakarat ve Şuarâ'daki "Rab + azîz-rahîm" nakaratı, isim katmanını ve mühür tonunu tek başına şişirebilir.
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
- **Eşleşmeyen girdi:** Setten düşer ve listelenir. Tahminle düzeltilmez.
- **Kapsam sınırı:** Aynı lemma ilâhî isim olmayan bağlamda da geçebilir. Örneğin "alîm" bir insan için de kullanılabilir. Bu nedenle `e` bayrağı yalnızca yüklem veya sıfat olarak geçtiği ayetlerde verilir. Bu ayrım otomatik yapılamazsa `e` bayrağı "üst sınır" olarak etiketlenir ve bu durum sonuçta açıkça yazılır.

### 4.3 Eksen B — Mühür tonu (ayet düzeyi)

- **Mühür:** Ayetin son üç içerik lemmasında (N, ADJ ya da PN) doğrulanmış setten en az bir esmâ bulunması. Tanım token düzeyinde değil lemma düzeyindedir, çünkü token düzeyindeki bayrağın iki vakada çalışmadığı görüldü.
- **Çift mühür:** Son üç içerik lemmasından ikisinin esmâ olması.
- **Ton:** Esmânın `varlik_katalog.json` alt-türüne göre cemâl, denge ya da celâl. Çift mühürde iki ton farklıysa sonuç "karma" olarak kaydedilir.
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
- **Duyarlılık:** Nakaratlı veri ve `e` bayrağının üst-sınır sürümü kullanıldığında sonuç yön değiştirirse, bulgu "kırılgan" olarak etiketlenir.

## 7. Bu ön-kaydın yapmadığı şeyler

- Esmânın cemâl/celâl sınıflandırmasını doğrulamaz. Bu etiketi yalnızca girdi olarak kullanır.
- Mekkî/Medenî ayrımı gibi geleneksel etiketleri değişken olarak almaz.
- Okuma sırasında fark edilen "şu isimle gelen ayetler şöyledir" türü iddiaları test etmez. Bu iddialar ayrı adaylar olarak KAPATILAMAZ statüsünde kalır.
- Araç geliştirmesi yapmaz. Gereken kod, okuma bittikten sonra ve dondurma kararına uygun olarak yazılır.

## 8. Sapmalar

*(Dondurmadan sonra yapılan her değişiklik buraya tarih, gerekçe ve etki bilgisiyle yazılır.)*

## 9. Dondurma kaydı

- commit: `________`
- `esma_listesi.json` SHA-256: `________`
- doğrulanmış esmâ seti boyutu / düşen girdiler: `________`

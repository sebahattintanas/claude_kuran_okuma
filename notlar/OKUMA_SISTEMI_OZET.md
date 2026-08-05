# Kur'an Varlık-Okuma Sistemi — Toparlama

Bu oturumda, metnin varlık dünyasını **türlerine göre** okuyan bir sistem kuruldu.
Amaç: her ayeti, mealinden ayrı olarak, **yapısal mimarisiyle** okumak — hangi
varlıklar var, hangi türden, nasıl bağlı, hangi katmanda.

---

## Yöntem (oturumun disiplini)

Sistem tek bir ilkeye dayanır: **metinden öğren, kategori dayatma.**

Her varlık için üç adım:
1. **Metinden öğren** — komşu kavramlar, tanım-ayetleri, bağlam (biz tanımlamayız)
2. **Katmanlar arası davranış** — aynı varlık her katmanda farklı çalışır
3. **Zıt/ilişki** — metnin kurduğu (kavram-zıt, durum-karşıt, eş, ya da yok)

Ve iki mod:
- **Ölçülebilen** özellikler ölçümden çıkar (kavram zaman-yönelimi, esmâ celâl/cemâl)
- **Rol/kader-tabanlı** olanlar verilir (kişi peygamber/karşı-figür — otomatik yanılır)

Kontrol her adımda: gevşek eşleşmeler temizlendi (sahte esmâ, Sâlih peygamber vs
sıfat), sınır durumlar dürüstçe işaretlendi (Hârût-Mârût "müteşâbih"), otomatik-tahmin
yanılınca (Firavun "peygamber", Âd "süregelen") verili yapıldı.

---

## Beş katman

Her ayet-düzeyi varlık dört katmanda ölçülür; beşinci kavram-düzeyidir:

| katman | ne ölçer | kapsama |
|--------|----------|---------|
| **ses** | mora (uzun/kısa ayet) | %100 (her ayet) |
| **zaman** | geçmiş/şimdi/gelecek | %50 (yarısı nötr) |
| **yoğunluk** | ayet başına kök sayısı | %100 |
| **yapı** | sûre içi konum (baş/orta/son) | %100 |
| **zıt** | metnin kurduğu karşıt | kavram-düzeyi (ilişki) |

İlk dördü dalgaya biner (her ayet bir değer); beşinci iki varlığın yan yana durması.

---

## Üç yapı

### 1. Kavram sözlüğü (`kavram_sozlugu.json` / `.txt`)
Kavramların Kur'an'dan çıkarılmış **yapısal tanımı** (meal değil) + beş katman imzası.
Örnek — hak: uzun ayet (103 mora), şimdi-zamanlı, yoğun, konumsuz, zıt→küfür (katmanlı:
küfür/dalâlet/bâtıl/zulüm/yalan). Araç: `kavram_arac.py`, `kavram_calistir.py`.

### 2. Varlık kataloğu (`varlik_katalog.json`) — **174 varlık, 14 tür**
Her varlık türü + alt-tür + okuma-kalıbıyla. Motor: `varlik_makinesi.py`,
üretici: `varlik_katalog.py`.

| tür | sayı | okuma-kalıbı | zıt/eş |
|-----|------|--------------|--------|
| kavram | 40 | beş katman | zıt (bazen) |
| kişi | 33 | söz/kavim/Rab | karşı-figür (bazen) |
| ilâhî-isim | 28 | çift-eşleşme | **eş** (zıt değil) |
| olay | 22 | kim yapar | yok |
| yer/âlem | 10 | kimin/nerede/nitelik | yok |
| gayb-varlık | 7 | mahiyet | yok |
| âhiret-öğesi | 7 | sahne-sırası | yok |
| kavim | 5 | elçi→tepki→kader | yok |
| tekil-sahne | 5 | tek ayet/anlam | yok |
| insan-hâli | 5 | idrak/yönelim | yok |
| hüküm-kategori | 4 | izin/yasak | helâl↔harâm |
| kitap | 3 | vahiy-ilişkisi | yok |
| zaman | 3 | döngüsel | yok |
| toplum | 2 | geniş/dar | yok |

**Alt-türler (168 varlık):**
- kişi: peygamber (20) / karşı-figür (5) / özel (Meryem, Lokmân, Tâlût, Zülkarneyn)
- ilâhî-isim: cemâl (21) / denge (4) / celâl (2 — sadece Cebbâr, Kahhâr)
- kavram: iyi/karşı + zaman-yönelimi (şimdi/geçmiş/gelecek) + zıt-türü
- olay: insan-ibadeti (8) / kozmos-olayı (12) / evrensel (2 — secde, yağmur)
- yer: dünyevî / uhrevî / kozmik
- kavim: helâk-olan / süregelen
- âhiret-öğesi: başlangıç (sûr,haşir) → hesap-anı (mîzan,sırât,şefaat) → sonuç (huld)

### 3. İlişki ağı (`iliski_agi.json`) — 129 bağ
Kim kiminle aynı ayette. Metnin kendi kurduğu kümeler:
- **Kişi kümeleri:** İbrâhîm soyu (İbrâhîm-İsmâîl-İshâk-Yâkûb-Îsâ-Meryem) · Mûsâ-Hârûn ·
  Firavun-Hâmân (zulüm ekibi, güç 1.00) · Dâvûd-Süleymân · Âdem-İblîs. Köprü: Mûsâ↔Firavun.
- **Kavram kümeleri:** mücadele (iman-ilim-cihad) · inanç (takvâ-iman-hidâyet) · merhamet.
- **Olay/kozmos:** kozmik-ikizler (güneş-ay, güç 0.69) · ibadet-ikizi (namaz-zekât) ·
  zaman-döngüsü · Arş-gök kozmik yapı.

---

## Okuma motoru (`okuma_motoru.py`)

Bir ayet verince: içindeki varlıkları bulur (normalize kök + lemma eşleştirme),
her birini türü/alt-türü/zıddı/eşiyle gösterir. Meal ayrı durur.

Örnek okumalar gösterdi ki her ayet-türü farklı **yapısal profil** verir:
- **kozmos-beyanı** (7:54): güneş-ay-yıldız-gece + yaratma + gök — kozmik küme tek yerde
- **ölçü** (55:5): kozmos + hesap birleşir (düzen = ölçü)
- **itikad** (2:285): iman + melek + mağfiret — farklı türler bir arada
- **âhiret-sahnesi** (101:6): tek mîzan — hesap-anı
- **hikmet-sahnesi** (27:18): karınca + Süleymân — zıtsız, çatışmasız

---

## Öne çıkan bulgular

- **Türler tek tip değil:** metin en az 14 varlık-türü kurar; her biri farklı okuma ister.
  Zıt **sadece bazı türlerde** (kavram-bir-kısmı + kişi-karşıtı). Çoğu tür zıtsız.
- **Esmâ cemâl-baskın:** 21 cemâl, 2 celâl. Azîz (güç) bile rahmet bağlamına meyilli —
  "her çift dengeye/rahmete meyleder" tezinin esmâ kanıtı.
- **Secde evrensel:** tek ibadet ki insan ve kozmos eşit yapar (yıldız, ağaç, gölge de secde eder).
- **Gök çift-kavram:** semâvât (çoğul, kozmik yapı) ≠ semâ (tekil, iniş-yönü). Yer hep tekil.
- **Gök↔yer karşıt değil, bütünleyen** (metne sorunca çıktı — hayat↔ölüm karşıt, gök+yer bütün).
- **İmlâ katmanı tarihî:** İbrâhîm iki yazım (Bakara'da küçük ye), ama bağlam/muqatta/mora
  değil sûre belirliyor — saf resm, anlam taşımaz (üç null-kontrolle kesinleşti).
- **Kavram zaman-yönelimi:** takvâ-iman-ihsan gelecek (âhirete hazırlık), hak-rahmet-ilim
  şimdi (canlı gerçeklik), adalet-cihad geçmiş (kıssalarda test).

---

## Dosyalar

- `kavram_sozlugu.json/.txt` + `kavram_arac.py`, `kavram_calistir.py` — kavram sözlüğü
- `varlik_katalog.json` + `varlik_makinesi.py`, `varlik_katalog.py` — varlık kataloğu
- `iliski_agi.json` — ilişki ağı
- `okuma_motoru.py` — ayet okuma motoru
- `kok_adlar.json` — kök→Türkçe ad sözlüğü

---

## Sıradaki: programa doğru

Okuma motoru çalışıyor ama %100 değil — kapsam genişletilebilir (Allah/Rab lafzı,
kalan esmâ). Asıl hedef: bu üç yapıyı **ses-dalgası programına** bağlamak. Ayet
okurken içindeki varlıklar türleri/okumaları/bağlarıyla belirsin; meal bir yanda,
yapısal-okuma öbür yanda.

**Not (veri kalıcılığı dersi):** katalog bir kez 174→88 çöktü çünkü elle-eklenenler
JSON'daydı ama üretici betikte değildi. Kurtarıldı; artık her şey `varlik_katalog.py`
+ ekleme-betiklerinde kalıcı. Kural: veri koda yazılmazsa kalıcı olmaz.

---

## Depo ve oturum rutini (Ağustos 2026)

**GitHub deposu:** `https://github.com/sebahattintanas/claude_kuran_okuma` (public)
Yapı: `veri/` `tablolar/` `betikler/` `bulgular/` `ciktilar/` `notlar/`
Proje alanı küçültüldü (19 MB → ~3.5 MB); büyük/türetilebilir dosyalar sadece depoda.

**Oturum başlangıcı (Claude):**
```bash
mkdir -p /home/claude/work && cd /home/claude/work
# 1) Depoyu çek (tablolar+betikler+bulgular güncel hali)
git clone --depth 1 https://github.com/sebahattintanas/claude_kuran_okuma.git depo
cp depo/tablolar/*.json depo/betikler/*.py .
# 2) Ham korpus (projede/depoda tutulması şart değil, kaynağından iner)
curl -sL -o morph.txt https://raw.githubusercontent.com/mustafa0x/quran-morphology/master/quran-morphology.txt
# Doğrulama: wc -l morph.txt → 130030 olmalı
```
Proje alanındaki kopyalar ile depo çelişirse: **en yeni değişiklik hangisindeyse o geçerli**;
oturum sonunda güncellenen dosya hem çıktı olarak verilir hem kullanıcı depoya yükler.

**Kalıcılık zinciri:** çalışma dizini → /mnt/user-data/outputs (kullanıcıya) →
kullanıcı depoya yükler → sonraki oturum depodan çeker. Proje alanı yalnız
küçük/elle-üretilmiş dosyaları taşır.

**Kayıp dosya kaydı:** `kok_adlar.json`, `bulgu_karsi_kutup_mesafe.json`,
`bulgu_denge_mizan.json` — ne projede ne depoda; metinde anılıyorlar.
Yeniden üretilmeleri YAPILACAKLAR'da.

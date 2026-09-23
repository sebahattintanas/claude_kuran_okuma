# ÖN-KAYIT — (A) İnsâna yüklenen sıfatlar · (B) Yaratılışta sıra

Yazıldı: 2026-09-18T11:07:51Z · ÖLÇÜMDEN ÖNCE · morph.txt sha256[:16] = 742bfac59941b2cb
Öncül: `ON_KAYIT_fiil_khalk.md` (edilgen insân ayetlerinin hepsi bir sıfat ya da madde ekliyor).

## (A) Sıfatlar
- **Aday kuralı:** LEM إِنسان tokeninden sonraki 6 kelime içinde; isim; MS; INDEF; NOM veya ACC.
  Kelimede zamir eki yok; kendinden önce harf-i cer yok.
- **Denetim:** BÜTÜN adaylar elle sınıflanır:
  - SIFAT: insâna yüklenen haber, hâl veya nitelik.
  - DEĞİL: başka bir kelimenin nesnesi, temyiz, vb.
  Makine çıktısı ve elle sınıf birlikte raporlanır. Duyarlılık ölçülmez (kaçırılanlar bilinmiyor) → yalnız kesinlik.
- **Tahminler:**
  - **T1** Elle onaylanan farklı sıfat lemması 8-25.
  - **T2** Onaylanan sıfat tokenlerinin ≥ %70'i olumsuz nitelik (zalim, nankör, aceleci, hırslı…).
  - **T3** Onaylanan sıfatların ≥ %50'si mübalağa kalıbında: فَعُول, فَعّال, فَعِيل.

## (B) Sıra
- **Sıra işareti:** ثُمَّ · فَ (CONJ/REM) · بَعْدَ + ذا. **"و" (ve) sıra DEĞİLDİR.**
- **Düğümler** (lemma korpustan NFC ile çözülür):
  - İNSAN: تُراب · طِين · صَلْصال · حَمَإ · سُلالَة · نُطْفَة · عَلَقَة · مُضْغَة · عِظام · لَحْم · سَوَّى (fiil) · نَفَخَ (fiil)
  - KOZMOS: سَماء · أَرْض · دُخان · رَواسِي/جِبال · اسْتَوَى (fiil) · دَحَى (fiil)
- **Bağlam:** ayette (ya da ayet çiftinde) şu köklerden biri olmalı: خلق · جعل · سوي · فطر · نشأ · بدأ · دحو · نفخ · بني · سمك.
- **Kenar:** ayet içindeki düğüm dizisi sıra işaretlerinde bölütlere ayrılır. Bölüt i'deki her düğümden bölüt i+1'deki her düğüme bir A → B kenarı çizilir.
  Sonraki ayet bir sıra işaretiyle başlıyorsa ayet sınırı da geçilir.
- **Denetim:** bütün kenarlar elle kontrol edilir. Özellikle ters yönlü çiftler tek tek ayetiyle yazılır.
- **Tahminler:**
  - **T4** İNSAN düğümleri arasında iki yönlü (çelişen) çift YOK.
  - **T5** KOZMOS'ta سَماء–أَرْض arasında iki yönde de en az birer kenar VAR.
  - **T6** İNSAN grafiğinde en uzun yönlü zincir ≥ 6 düğüm.

---
## SONUÇ (ölçümden sonra eklendi; yukarısı değiştirilmedi)
Betikler: `betikler/dikey/insan_sifat.py`, `yaratilis_sira.py`
Çıktılar: `ciktilar/insan_sifat_aday.json`, `yaratilis_sira.json`

**Sapma (lemma yazımı):** ön-kayıttaki جِبال korpusta yok; doğru lemma جَبَل (çoğul da ona bağlı).
Betiğin doğrulama satırı durdurdu. Niyet değişmedi.

### (A) Sıfatlar — 20 aday, hepsi elle
- SIFAT 15 · mükerrer 1 (17:11 iki insân tokeninden) · DEĞİL 4:
  - 19:66 حَيّ (insanın kendi sorusu)
  - 25:29 خَذُول (Şeytan)
  - 25:49 كَثِير (sayı)
  - 59:16 بَرِيء (Şeytan'ın sözü)
- **Kesinlik 15/19 = %79.** Duyarlılık ölçülmedi.
  Bilinen kaçırmalar: 76:2 بَصِير (pencere dışı) · 11:9 يَئُوس/كَفُور · 41:49 يَئُوس/قَنُوط · 17:83 يَئُوس · 18:54 جَدَل (zamir ya da uzaklık).
- Onaylanan 11 lemma:
  - كَفُور ×4 · ظَلُوم ×2
  - ضَعِيف · كَفّار · خَصِيم · عَجُول · قَتُور · جَهُول · هَلُوع · كَنُود · سَمِيع (birer)
- **T1 TUTTU** (11 lemma).
- **T2 TUTTU:** 14/15 olumsuz ya da eksiklik; tek olumlu سَمِيع (76:2).
- **T3 TUTTU:** 15/15 فَعُول/فَعّال/فَعِيل. Dar mübalağa (فَعُول + فَعّال) 11/15 = %73.

### (B) Sıra — bütün kenarlar elle denetlendi
**İNSAN:**
- Kenarlar gerçek sıra ifadeleri. Bağlam hatası: 3:49 ve 5:110 (Îsâ'nın kuşu) → طين → نفخ. Yön aynı.
- **T4 TUTTU:** iki yönlü çift yok.
- **T6 TUTTU:** en uzun zincir 7 düğüm: طِين → سُلالَة → نُطْفَة → عَلَقَة → مُضْغَة → عِظام → لَحْم.
  Zincirin tamamı tek pasajdan (23:12-14). Bağımsız doğrulayan halkalar:
  - تُراب → نُطْفَة: 18:37, 22:5, 35:11, 40:67
  - نُطْفَة → عَلَقَة: 22:5, 40:67
  - عَلَقَة → مُضْغَة: 22:5
  - طِين → سُلالَة: 32:7-8
  - عِظام → لَحْم: 2:259
- Tesviye ve nefh (سَوَّى, نَفَخَ) her zaman maddeden sonra: 15:28-29, 32:7-9, 38:71-72. Ayrıca نُطْفَة'dan (18:37) ve عَلَقَة'dan (75:38) sonra.

**KOZMOS — makine kenarları büyük ölçüde SAHTE:**
1. استوى düğümü iki olayı birleştiriyor: "göğe yöneldi" (2:29, 41:11) ve "Arş'a istivâ" (7:54, 10:3, 13:2, 25:59, 32:4, 57:4).
   Çelişkilerin 2'si bundan. **Düğüm edata göre bölünmeliydi.**
2. Yaratılış dışı cümleler kenar üretmiş: 2:164, 10:24, 39:21 (yağmur → yer), 57:4.
3. 41:11'deki فَقالَ söz aktarıyor, sıra değil.
4. **Kaçırılan gerçek kenar:** 79:27-29 (gök) → 79:30 "bundan sonra yeri yaydı" (دَحَى). Ayet sınırı kuralı kaçırdı.
5. Makinenin kozmos zinciri (رواسي → دخان → أرض → دحى) anlamsız; atıldı.

**Elle kurulan kozmos sırası (yalnız açık işaretli pasajlar):**
- 2:29: yerdekiler → sonra göğe yöneldi → yedi gök.
- 41:9-12: yer (iki gün) → dağlar, bereket, rızıklar (dört gün) → sonra göğe yöneldi (duman) → yedi gök (iki gün).
- 79:27-30: gök (bina, yükseltme, gece/gündüz) → bundan sonra yerin yayılması (دَحَى).
- "Gökleri ve yeri altı günde yarattı, sonra Arş'a istivâ etti": 7:54, 10:3, 25:59, 32:4, 57:4. Bu bir sıra ama gök ile yer arasında değil.

**T5 TUTTU (elle):** yer → gök (2:29, 41:9-11) ve gök → yerin yayılması (79:27-30). İki yön de metinde var.
Ama fiiller farklı: bir yanda خَلَقَ / جَعَلَ, öbür yanda دَحَى. Makinenin iki yönlü kenarları ise sahte.

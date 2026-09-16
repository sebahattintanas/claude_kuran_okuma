# -*- coding: utf-8 -*-
"""18_cipa_esik_karari.py — P0 #6 KAPANIŞI.

Eşik seçildi, ölçüt mekanikleştirildi, çıpa/yıldız ilişkisi eşik seçildikten
SONRA hesaplandı (14_cipa_tanimi.py'nin döngüsellik şartı). Bu betik kararı
yazar, düşen üç kaydı düzeltir ve adayları ekler.
"""
import json

# ------------------------------------------------------------------ 1. DÜŞEN KAYITLAR
DUSEN = {
 "_dusen_kayitlar_cipa": (
  "**OKUMA SIRASINDA KURULAN ÜÇ KAYDIM P0 #6 KAPATILIRKEN DÜŞTÜ.** Protokol gereği "
  "sessizce değiştirilmedi, düşürüldüğü belgelendi. "
  "**(1) 'L3 iki sûrede de sıfır' — YANLIŞ.** Sûre 27'de bir L3 var: 27:88 (dağları "
  "donuk sanırsın, oysa bulut gibi geçerler — görünüş/durum ayrımı + karşılaştırma). "
  "Kayıt `14_cipa_tanimi.py`'nin kendi tablosunda zaten duruyordu; okuma sırasında "
  "tabloya bakılmadan yazıldı. "
  "**(2) 'sûre 27'de L2 kayıtları olgu-dışıydı' — YANLIŞ.** Sûre 27'nin dört L2'sinden "
  "İKİSİ gerçek doğa olgusu: 27:60 (gökten su → bahçeler + yeti sınırı) ve 27:86 (gece "
  "dinlenme İÇİN, gündüz aydınlık — işlevsel nedensellik). Yalnız 27:62 ve 27:64 "
  "olgu-dışı sayılabilir. "
  "**(3) '28:71-72 ilk kez L2 gerçek bir doğa olgusuna uygulanıyor' — YANLIŞ.** 27:60 "
  "ve 27:86 bunu zaten yapmıştı; dahası 28:71-72 tam olarak 27:60'ın, 28:73 tam olarak "
  "27:86'nın emsalidir. Doğru ifade: *sûre 28'de ilk kez*, korpusta değil. "
  "**(4) Bir de kademe düzeltmesi:** 28:73 okuma sırasında L1 kaydedilmişti; 27:86'nın "
  "emsaliyle **L2** olmalı (işlevsel nedensellik). Düzeltildi. "
  "**ORTAK SEBEP: üç kayıt da sûre 27'nin tablosuna BAKILMADAN, okuma anındaki hatıradan "
  "kuruldu — aday 843'ün ('sayım defterden koşulur, hafızadan değil') çıpa tarafındaki "
  "eşi.** Ders: emsal bağı zorunlu kılındı; `15_cipa_kademe_28.py`'nin her satırı sûre "
  "27'den hangi ayetle aynı kademeye konduğunu taşıyor."),

 "_cipa_karari": (
  "**P0 #6 KAPANDI — ÇIPA ÖLÇÜTÜ: (L2+) VE (olgu = evet).** Üç aday eşiğin iki sûrelik "
  "sonucu: **L4+ → 0 ayet** (kullanılamaz) · **L3+ → 1 ayet** (27:88; 181 ayette tek "
  "kayıt, %0,55 — kullanılamayacak kadar seyrek) · **L2+ → 9 ayet, ama TEKDÜZE DEĞİL**: "
  "dokuzdan ikisi (27:62, 28:10) nedensellik kuruyor ama bağladığı şey bir doğa olgusu "
  "değil. Bu yüzden eşik tek başına yetmiyor; **ikinci bir bayrak (olgu evet/hayır) "
  "şart.** Bayrakla birlikte: **7 çıpa / 181 ayet (%3,9)** — 27:60 · 27:64 · 27:86 · "
  "27:88 · 28:71 · 28:72 · 28:73."),

 "_cipa_taramasi": (
  "**ÇIPA ARTIK OKUMA DİKKATİYLE DEĞİL TARAMAYLA BULUNUYOR.** Ölçüt beş morfolojik "
  "işaret ailesine bağlandı: **A_şart** (edim şart / kip COND / لولا, korpus 339+20) · "
  "**B_ta'lîl** (PRP|PREF, amaç lâmı, 132) · **C_recâ** (لعل / كي, 98) · **D_yeti** "
  "(olumsuzluk + كون + أَن; ya da 'başka ilâh' kalıbı, 77) · **E_görünüş** (sanma fiili "
  "+ CIRC|PREF hâl vâvı, 23). Aday = olgu alanından en az bir kök VE en az bir işaret. "
  "**Sonuç: 586 aday ayet, korpusun %9,4'ü; anma (recall) elle kurulmuş yedi çıpaya "
  "karşı 7/7 = %100.** İlk sürüm (yalnız şart + sözlük) %57'de kalmıştı; kaçan üç "
  "çıpanın (27:60, 27:86, 27:88) işaretleri morfolojide zaten vardı ama taranmıyordu. "
  "Kesinlik iki okunan sûrede 7/21 = **%33**. **Tarama KARAR vermez; 6236 ayeti 586'ya "
  "indirir ve okuma o listeyi okur.**"),

 "_cipa_yildiz_iliskisi": (
  "**EŞİK SEÇİLDİKTEN SONRA HESAPLANDI (döngüsellik şartı): ÇIPA İLE YILDIZ BAĞIMSIZ.** "
  "Yedi çıpanın 3'ü yıldızlı (%42,9); iki sûrenin tabanı %30,4. **Binom P(X≥3 | n=7, "
  "p=0,304) = 0,362 — ANLAMLI DEĞİL.** Kademe × yıldız ilişkisi de tekdüze değil ve "
  "yönü ters: **L0 %44 · L1 %50 · L2 %25 · L3 %100 (n=1)** — iddia gücü en yüksek "
  "kademe (L2) taban oranın ALTINDA. Üç yıldızlı çıpanın yıldız kaynakları: 27:60 → n · "
  "27:88 → hapaks · 28:71 → allah; **hiçbiri içerikten.** Tarama havuzunun yıldız oranı "
  "%50 ile korpus tabanının (%35,4) üstünde, ama bu bir UZUNLUK artefaktı: havuzun "
  "ortalama n'i 23,00, korpusunki 12,42 — **1,9 kat** (aday 903/909'un payda etkisi). "
  "**SONUÇ: 🜁/🜂 ★★★ koşuluna BAĞLANAMAZ.** Bağlansaydı yedi çıpanın altısı düşerdi "
  "(yalnız 27:88 ★★★). Semboller yıldızdan bağımsızlaştırıldı; çıpa ölçütü kendi "
  "başına uygulanır."),

 "_cipa_p05_bagimliligi": (
  "**P0 #6'NIN KESİNLİĞİ P0 #5 TARAFINDAN SINIRLANIYOR.** Sûre 27-28'deki 14 yanlış "
  "pozitifin sebebi mekanik olarak ölçüldü: **6'sı (%43) LEMMA KUSURUNDAN** — kök olgu "
  "alanında görünüyor ama ayetteki lemma başka anlam alanında: ظلم → ظُلْم/ظالِم "
  "(karanlık değil zulüm; 27:14, 28:40, 28:50) · صبح → أَصْبَحَ (sabah değil yardımcı "
  "fiil; 28:10, 28:82) · حيي → اسْتِحْياء (hayat değil hayâ; 28:25) · قدر → قَدَرَ. "
  "Kalan 8'i gerçek yanlış pozitif (kök doğru alanda ama ayet çıpa değil). **Lemma "
  "katmanı yazılsaydı kesinlik %33'ten %47'ye çıkardı.** Yani P0 #5, P0 #6'nın tavanını "
  "belirliyor — ve bu, aday 906'nın 'lemma borcu yalnız gloss değil ÖLÇÜM borcu' "
  "kaydının ikinci bağımsız doğrulaması."),
}

ADAYLAR = [
{"no": 920,
 "aday": "★ P0 #6 KAPANDI — ÇIPA ÖLÇÜTÜ SEÇİLDİ: **(L2+) VE (olgu = evet)**. Üç aday eşiğin iki sûrelik (181 ayet) sonucu: L4+ → **0 ayet**, kullanılamaz · L3+ → **1 ayet** (27:88), %0,55, kullanılamayacak kadar seyrek · L2+ → **9 ayet ama tekdüze değil**, dokuzdan ikisi (27:62, 28:10) nedensellik kuruyor ama bağladığı şey doğa olgusu değil. **Eşik tek başına yetmiyor; ikinci bayrak (olgu evet/hayır) ŞART.** Bayrakla: 7 çıpa / 181 ayet (%3,9).",
 "olculen": {"esik_L4": {"ayet": 0}, "esik_L3": {"ayet": 1, "liste": ["27:88"], "oran_yuzde": 0.55},
             "esik_L2": {"ayet": 9, "olgu_olan": 7, "olgu_olmayan": 2,
                         "olgu_olmayanlar": ["27:62", "28:10"]},
             "secilen": "(L2+) ∧ (olgu=evet)",
             "cipa": ["27:60", "27:64", "27:86", "27:88", "28:71", "28:72", "28:73"],
             "cipa_orani_yuzde": 3.9,
             "sure_27_kademe": {"L0": 4, "L1": 8, "L2": 4, "L3": 1, "L4": 0},
             "sure_28_kademe": {"L0": 5, "L1": 6, "L2": 4, "L3": 0, "L4": 0}},
 "durum": "KAPALI", "oncelik": "P0", "kaynak": "P0 #6 kapanışı, iki sûre verisi",
 "etiket": "P0 kapanışı",
 "test_notu": "**Karar eşiğin sonucuna bakılarak verilmedi** (14_cipa_tanimi.py'nin döngüsellik şartı): ölçüt, kademelerin TEKDÜZELİĞİNE bakılarak seçildi. L4 ve L3 boş ya da tek elemanlı; L2 dolu ama iki türü karıştırıyor. **Çıpa/yıldız ilişkisi ancak eşik seçildikten sonra hesaplandı (aday 922).** TUR SONU: ölçüt bundan sonraki her sûrede `17_cipa_tarama2.py`'nin aday listesi üzerinden uygulanacak; okuma dikkatiyle çıpa aranmayacak."},

{"no": 921,
 "aday": "★ ÇIPA ARTIK TARAMAYLA BULUNUYOR — BEŞ MORFOLOJİK İŞARET AİLESİ, ANMA %100. Ölçüt okuma dikkatinden alınıp morfolojiye bağlandı: **A_şart** (edim şart / kip COND / لولا) · **B_ta'lîl** (PRP|PREF amaç lâmı) · **C_recâ** (لعل / كي) · **D_yeti** (olumsuzluk + كون + أَن; 'başka ilâh' kalıbı) · **E_görünüş** (sanma fiili + CIRC|PREF hâl vâvı). Aday = olgu alanından bir kök VE bir işaret → **586 ayet (korpusun %9,4'ü)**, anma **7/7**.",
 "olculen": {"olgu_koku_tasiyan_ayet": 2163, "aday_ayet": 586, "korpus_oran_yuzde": 9.4,
             "isaret_ailesi": {"A_şart": 339, "B_ta’lîl": 132, "C_recâ": 98, "D_yeti": 77,
                               "E_görünüş": 23, "A_levlâ": 20},
             "anma": "7/7", "anma_yuzde": 100,
             "ilk_surum_anma": "4/7 (%57)",
             "ilk_surumde_kacanlar": {"27:60": "D_yeti (ما كان لكم أن)",
                                      "27:86": "B_ta’lîl (PRP|PREF)",
                                      "27:88": "E_görünüş (sanma fiili + CIRC)"},
             "kesinlik_sure_27": "4/8 (%50)", "kesinlik_sure_28": "3/13 (%23)",
             "kesinlik_toplam": "7/21 (%33)"},
 "durum": "KAPALI", "oncelik": "P0", "kaynak": "P0 #6 kapanışı",
 "etiket": "ölçütün mekanikleştirilmesi",
 "test_notu": "**Çıpa şimdiye kadar okuma dikkatiyle bulunuyordu — aday 899'un yasakladığı taraflı örneklemin ta kendisi.** İlk sürüm (yalnız şart + sözlük) %57 anma verdi ve kaçan üç çıpanın işaretleri morfolojide ZATEN vardı: amaç lâmı `PRP|PREF`, hâl vâvı `CIRC|PREF`, yeti sınırı kalıbı. **Ders: bir ölçütün 'okumayla bulunur' sayılması çoğu zaman ölçütün morfolojiye bağlanmamış olmasından kaynaklanıyor.** Tarama karar vermez, 6236 ayeti 586'ya indirir. KAPATILAMAZ olan yan: 586 adayın yalnız 21'i (iki sûre) elle sınandı; kesinlik %33 tahmini bu 21'e dayanıyor."},

{"no": 922,
 "aday": "★ ÇIPA İLE YILDIZ BAĞIMSIZ — EŞİK SEÇİLDİKTEN SONRA HESAPLANDI. Yedi çıpanın 3'ü yıldızlı (%42,9), iki sûre tabanı %30,4; **binom P(X≥3 | n=7, p=0,304) = 0,362, ANLAMLI DEĞİL.** Kademe × yıldız ilişkisi tekdüze değil ve yönü ters: **L0 %44 · L1 %50 · L2 %25 · L3 %100 (n=1)** — iddia gücü en yüksek kademe taban oranın ALTINDA.",
 "olculen": {"cipa_ayet": 7, "cipa_yildizli": 3, "cipa_oran_yuzde": 42.9,
             "iki_sure_taban_yuzde": 30.4, "binom_p": 0.362, "anlamli": False,
             "kademe_yildiz": {"L0": [9, 4, 44], "L1": [14, 7, 50], "L2": [8, 2, 25], "L3": [1, 1, 100]},
             "cipa_yildiz_kaynaklari": {"27:60": "n=1,55", "27:88": "hapaks=6,98", "28:71": "allah=1,58"},
             "icerikten_gelen": 0,
             "havuz_yildiz_yuzde": 50.0, "korpus_yildiz_yuzde": 35.4,
             "havuz_ort_n": 23.00, "korpus_ort_n": 12.42, "uzunluk_kati": 1.9,
             "yildiz3_kosulu_uygulansa": {"kalan_cipa": 1, "dusen": 6, "kalan": ["27:88"]}},
 "durum": "KAPALI", "oncelik": "P0", "kaynak": "P0 #6 kapanışı",
 "etiket": "döngüsellik şartına uygun hesap",
 "test_notu": "**Bu hesap, eşik seçildikten SONRA yapıldığı için döngüsel değil** (14_cipa_tanimi.py'nin açık şartı). Sonuç: **yıldız alanı çıpa durumu hakkında hiçbir bilgi taşımıyor.** Tarama havuzunun yıldız oranının taban üstünde olması (%50 / %35,4) bir içerik sinyali değil UZUNLUK artefaktı: havuzun ortalama n'i korpusunkinin 1,9 katı ve `n`, `allah`, `rab`, `pas` ölçütlerinin dördü de uzunluğa duyarlı (aday 903/909). **KARAR: 🜁/🜂 ★★★ koşuluna BAĞLANAMAZ** — bağlansaydı yedi çıpanın altısı düşerdi. Semboller yıldızdan bağımsızlaştırıldı."},

{"no": 923,
 "aday": "★ P0 #6'NIN KESİNLİĞİ P0 #5 TARAFINDAN SINIRLANIYOR — YANLIŞ POZİTİFLERİN %43'Ü LEMMA KUSURU. Sûre 27-28'deki 14 yanlış pozitifin sebebi mekanik ölçüldü: altısında kök olgu alanında görünüyor ama ayetteki lemma başka anlam alanında.",
 "olculen": {"yanlis_pozitif": 14, "lemma_kusurundan": 6, "oran_yuzde": 43,
             "gercek_yanlis_pozitif": 8,
             "lemma_vakalari": {"27:14": "ظلم → ظُلْم", "28:40": "ظلم → ظالِم", "28:50": "ظلم → ظالِم",
                                "28:25": "حيي → اسْتِحْياء, ظلم → ظالِم",
                                "28:10": "صبح → أَصْبَحَ", "28:82": "صبح → أَصْبَحَ, قدر → قَدَرَ"},
             "kesinlik_simdi_yuzde": 33, "kesinlik_lemma_ile_yuzde": 47},
 "durum": "ACIK", "oncelik": "P0", "kaynak": "P0 #6 kapanışı",
 "etiket": "P0 #5'e bağımlılık",
 "test_notu": "**P0 #5, P0 #6'nın TAVANINI belirliyor:** lemma katmanı yazılmadan çıpa taramasının kesinliği %33'te kalıyor, yazılsa %47'ye çıkar. Kusurlu kökler tam da sûre 28 okumasında P0 #5 sınama kümesine giren kökler: ظلم (karanlık/zulüm), صبح (sabah/yardımcı fiil), حيي (hayat/hayâ), قدر (ölçü/güç yetirme). **Bu, aday 906'nın 'lemma borcu yalnız gloss değil ÖLÇÜM borcu' kaydının ikinci bağımsız doğrulaması** — birincisi nakarat2'nin iki çifti kaçırmasıydı. **İki ayrı alan (nakarat2, çıpa taraması) aynı eksik katman yüzünden sakat.**"},
]

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD['AJ_kasas'].extend(ADAYLAR)
AD['son_guncelleme'] = 'P0 #6 (çıpa eşiği) kapatıldı — adaylar 920-923'
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('aday_bulgular: AJ_kasas →', len(AD['AJ_kasas']), '| son no', AD['AJ_kasas'][-1]['no'])

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
OM['28']['_mercek_atlama_notu'].update(DUSEN)
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: 28 kapanış notu →', len(OM['28']['_mercek_atlama_notu']))

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
MK['28_atlama'].update(DUSEN)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: 28_atlama →', len(MK['28_atlama']))

# -*- coding: utf-8 -*-
"""30_lemma_kapanis.py — P0 #5 (lemma katmanı) aday kayıtları, 940-945."""
import json

ADAYLAR = [
{"no": 940,
 "aday": "★ P0 #5 ENVANTERİ ÇIKARILDI — ÜÇ KATMAN ÖNERİSİNDEN BİRİ (BAB) GEREKSİZ ÇIKTI. Proje kendi kaydında 'envanter çıkarılmadan onarım kararı verilmeyecek' demişti. Okumada belgelenmiş 28 çok-anlamlılık vakası üç katmana karşı koşuldu: **LEMMA 22 · BAĞLAM 6 · BAB 0.** Aday 569/584'ün 'dikey satır üretilirken kökün BAB'ı da girdiye katılsın' önerisinin çözdüğünü iddia ettiği vakaları (صرف · قرن · رجو · طلق) **lemma zaten ayırıyor**; bab katmanının tek başına çözdüğü vaka yok.",
 "olculen": {"vaka": 28, "lemma_cozer": 22, "baglam_gerekir": 6, "bab_ek_katki": 0,
             "baglam_vakalari": {"كشف": "27:44/27:62 ikisi de كَشَفَ",
                                 "عوم": "29:14 عام — tablo karşılığı 'yüzme'",
                                 "أيي": "26:128/29:50 ikisi de آيَة",
                                 "صبح": "29:37 أَصْبَحَ — tablo karşılığı 'sabah'",
                                 "قدر": "28:82/29:62 ikisi de قَدَرَ",
                                 "هوي": "هَواء hem 'hava' (14:43) hem 'heva' (28:50)"},
             "korpus_envanteri": {"morfolojide_kok": 1651, "tek_lemmali": 724,
                                  "kok_turkce_kapsami": 1059,
                                  "en_cok_lemmali_kok": 22},
             "maliyet": {"tam_lemma_tablosu": 3737, "kok_tablosunun_kati": 3.5,
                         "okunan_ayetlerde_cift": 2537,
                         "okunanlardan_tek_lemmali": 446,
                         "okunanlardan_cok_lemmali": {"kok": 564, "cift": 2091},
                         "cok_alanli_gloss_tasiyan_kok": 173,
                         "bunlardan_cok_lemmali": 161,
                         "cok_alanli_ama_TEK_lemmali": 12}},
 "durum": "KAPALI", "oncelik": "P0", "kaynak": "P0 #5 envanter turu",
 "etiket": "envanter + aday 569/584'ün düşmesi",
 "test_notu": "**Aday 569/584'ün bab önerisi düştü: lemma katmanı onu KAPSIYOR.** Öneri 'lemma ayrımından ucuz bir yaklaşım olabilir' diye kaydedilmişti; ölçüm iki şeyi birden gösterdi — bab daha ucuz değil (aynı morfoloji alanından geliyor) ve **ek hiçbir vaka çözmüyor.** İkinci bulgu maliyet tarafında: **çok alanlı karşılık taşıyan 173 kökün 12'si TEK LEMMALI** — yani o on ikisini lemma katmanı hiçbir koşulda çözemez (أجج · أدم · بعل · رسس · شأم · عتق ve altı tanesi daha). KAPATILAMAZ: 28 vaka okuma sırasında bulundu, yani taraflı örneklem (aday 899); korpus çapında çok-anlamlılık sayımı yapılmadı."},

{"no": 941,
 "aday": "★ P0 #5 İKİYE AYRILDI VE (a) PARÇASI KAPANDI — LEMMA KİMLİĞİNİN MALİYETİ SIFIR. İki parçanın maliyetleri taban tabana zıt: **(a) LEMMA KİMLİĞİ** morfolojideki `LEM` alanından gelir, elle iş yok, maliyet 0 — ve `nakarat2` ile çıpa taramasının arızalarını onarır. **(b) LEMMA GLOSSU** (kök, lemma) için Türkçe karşılık ister; tam tablo 3737 satır, okunan ayetlerde 2537 satır, tamamı elle iş. (a) yazıldı, (b) açık kaldı.",
 "olculen": {"uretilen": {"lemma_iskelet.json": "6236 ayet, lemma dizisi",
                          "lemma_envanteri.json": "1651 kök, 4635 (kök, lemma) çifti"},
             "kaybedilen_denetimi": "yüzey iskeletiyle uzunluk farkı olan ayet: 0",
             "bolutleme": "04_ngram_altyapi.py ile AYNI (bağlaç önekleri atılır)",
             "kok_tasimayan_kelime": "sadeleştirilmiş yüzey biçimiyle temsil edilir",
             "a_parcasi_maliyet": 0, "b_parcasi_satir": 2537},
 "durum": "KAPALI", "oncelik": "P0", "kaynak": "onarım 16",
 "etiket": "onarım (P0 #5a kapandı)",
 "test_notu": "**Ayrımın kendisi bulgu:** P0 #5 üç oturumdur 'pahalı' diye bekletiliyordu, ama pahalı olan yalnız GLOSS tarafı. Ölçüm tarafı (hangi token hangi lemmaya ait) morfolojide zaten duruyordu ve kullanılmıyordu. **Aday 906'nın 'lemma borcu yalnız gloss değil ÖLÇÜM borcu' kaydı doğruydu; yeni olan, ölçüm borcunun BEDAVA kapanabilmesi.** `lemma_iskelet` yüzey iskeletiyle birebir hizalı (uzunluk farkı 0), yani iki iskelet arasında token düzeyinde karşılaştırma yapılabiliyor."},

{"no": 942,
 "aday": "★ `nakarat3` YAZILDI — VE ADAY 906'NIN İDDİASI İKİ VAKADA DA YANLIŞ ÇIKTI. Aday 906 'lemma katmanı yazılsaydı `nakarat2` 28:5↔28:41 ve 28:30↔28:46 çiftlerini görürdü' demişti. Lemma tabanlı `nakarat3` koşuldu: **28:5↔28:41'in ortak lemma dizisi `جعل|جَعَلَ أمم|إِمام` — İKİ kelime**, nakaratın üç kelimelik alt sınırının altında. **28:30↔28:46'nın ortak birimi TEK lemma** (`ندي|نادَى`) — hiçbir n-gram alanıyla yakalanamaz.",
 "olculen": {"nakarat2_dolu": 1950, "nakarat3_dolu": 2260, "artis": 310, "artis_yuzde": 15.9,
             "suzgeci_gecen": {"nakarat2": 1303, "nakarat3": 1517},
             "kaybedilen": 1,
             "kaybin_teshisi": {"ayet": "10:2",
                 "kalip": "ان هذا لسحر مبين",
                 "sebep": "10:2'de لَسَٰحِرٌ (LEM:ساحِر, büyücü), 10:76'da لَسِحْرٌ "
                          "(LEM:سِحْر, büyü); harekesiz yüzey iskeleti ikisini de "
                          "`لسحر` yazıp AYNI sayıyordu",
                 "hukum": "gerçek kayıp DEĞİL — bir YANLIŞ POZİTİFİN düşmesi"},
             "sinama_kumesi": "0/2",
             "vaka_1": {"cift": ["28:5", "28:41"], "ortak_lemma_dizisi": "2 kelime",
                        "engel": "nakarat alt sınırı 3 kelime (aday 907/935)",
                        "alt_sinir_2_ile": "YAKALANIYOR"},
             "vaka_2": {"cift": ["28:30", "28:46"], "ortak_birim": "tek lemma",
                        "engel": "n-gram alanı tek birimlik tekrarı tanım gereği göremez",
                        "alt_sinir_2_ile": "YİNE YAKALANMIYOR"}},
 "durum": "KAPALI", "oncelik": "P0", "kaynak": "onarım 17",
 "etiket": "onarım + düşen kayıt (aday 906)",
 "test_notu": "**İki borç birbirine bağlıymış ve hiçbiri tek başına bu vakaları çözmüyor.** Aday 906'nın hatası, lemma katmanının kalıbı GÖRÜNÜR kılmasıyla alanın onu SAYMASINI aynı şey sanmaktı: lemma katmanı `نَجْعَلَهُمْ`/`جَعَلْنَٰهُمْ`ı birleştiriyor ama sonuç iki kelimelik bir dizi ve alanın alt sınırı üç. **İkinci vaka daha da keskin: ortak birim tek lemma, yani bu bir NAKARAT değil KÖK SEYRİ olgusu** — `sûre_geçiş` sayacının zaten saydığı şey, `nakarat` alanının hiçbir sürümü göremez. **Onarımın gerçek kazancı başka yerde: +310 ayet (%15,9) ve bir yanlış pozitifin düşmesi.** Yanlış pozitif bulgusu kendi başına değerli: yüzey iskeleti harekesiz olduğu için farklı kelimeleri eşleyebiliyor."},

{"no": 943,
 "aday": "★ `nakarat` ALT SINIRI KARARI ARTIK HESAPLANABİLİR (aday 907/935). Dört kombinasyon ölçüldü: alt sınır 3 kelime → yüzey 1950 ayet / 1354 kalıp, **lemma 2260 ayet / 1729 kalıp**; alt sınır 2 kelime → yüzey 3747 ayet / 3978 kalıp, **lemma 4230 ayet / 5491 kalıp (korpusun %67,8'i)**.",
 "olculen": {"alt_sinir_3": {"yuzey": {"ayet": 1950, "kalip": 1354},
                             "lemma": {"ayet": 2260, "kalip": 1729}},
             "alt_sinir_2": {"yuzey": {"ayet": 3747, "kalip": 3978},
                             "lemma": {"ayet": 4230, "kalip": 5491}},
             "korpus_orani_alt_sinir_2_lemma": 67.8,
             "28_5_28_41_alt_sinir_2_ile": True,
             "28_30_28_46_alt_sinir_2_ile": False},
 "durum": "ACIK", "oncelik": "P1", "kaynak": "onarım 17 ölçümü",
 "etiket": "aday 907/935'e karar verisi",
 "test_notu": "**Alt sınırı 2'ye indirmek korpusun üçte ikisini doldurur.** Bu, alanın YORUM değeri için tehlikeli: 'nakarat' iddiası ayetlerin %68'i için kurulabiliyorsa ayırt edici olmaktan çıkar. **Önerilen ayrım: alt sınır 3'te kalsın (yorumda kullanılan alan), 2 kelimelik lemma çiftleri AYRI bir alanda sayılsın ve yoruma sokulmasın** — böylece 28:5↔28:41 gibi vakalar ölçülebilir olur ama nakarat iddiası seyrek kalır. Karar verilmedi; ölçüm kaydedildi. KAPATILAMAZ olan yan: 2 kelimelik kalıpların kaçının anlamlı olduğu örneklemle sınanmadı."},

{"no": 944,
 "aday": "★ ÇIPA TARAYICISI v4 — OLGU EŞLEŞMESİ (KÖK, LEMMA) DÜZEYİNE TAŞINDI; ADAY 923'ÜN ÖNGÖRÜSÜ YÖNÜ DOĞRU, BÜYÜKLÜĞÜ YANLIŞ. Aday 923 'kesinlik %41 → %54' demişti. Ölçüm: **%35 → %47** (sûre 27-28) ve **%40 → %46** (sûre 27-29). Yön doğru, ama hem taban hem hedef fazla yüksek yazılmıştı; kazanç +12 puan (öngörü +13).",
 "olculen": {"ongoru": {"taban": 41, "hedef": 54},
             "gercek_27_28": {"v3": 35, "v4": 47},
             "gercek_27_29": {"v3": 40, "v4": 46},
             "havuz": {"v3": 680, "v4": 477, "azalma_yuzde": 30},
             "anma": {"kurulum_kumesi": "7/7", "tutulan_kume": "3/3", "cipa_kaybi": 0},
             "sure_kesinligi_v4": {"27": "4/6 (%67)", "28": "3/9 (%33)", "29": "3/10 (%30)"},
             "dusen_adaylar": ["27:44", "28:10", "28:25", "28:50", "28:82"],
             "aday_923un_dort_vakasi": ["28:10", "28:25", "28:50", "28:82"],
             "dordu_de_dustu": True,
             "olgu_lemma_tablosu": {"cok_lemmali_kok": 50, "tek_lemmali_kok": 22,
                                    "baglam_gerekli": 1,
                                    "dusen_token_yuzde": 34.4}},
 "durum": "KAPALI", "oncelik": "P0", "kaynak": "onarım 18-19",
 "etiket": "onarım + öngörü sınaması",
 "test_notu": "**Aday 923'ün dört lemma vakasının dördü de düştü ve çıpa kaybı sıfır — onarım hedefini tutturdu.** Ama öngörülen sayılar tutmadı: taban %41 diye yazılmıştı, gerçekte %35. **Sebep: aday 923 kesinliği okuma notlarındaki sayılardan hesaplamıştı, tarayıcı çıktısından değil** — aday 843'ün ('sayım defterden koşulur') dördüncü tekrarı. Beşinci bir aday da düştü (27:44) ve aday 923 onu saymamıştı: `حسب`→حَسِبَ ve `ظلم`→ظَلَمَ ikisi de olgu dışı. **Havuz 680'den 477'ye indi (%30 daralma) ve anma korundu: kurulum kümesi 7/7, tutulan küme 3/3.**"},

{"no": 945,
 "aday": "★ KENDİ OLGU TABLOMDA İKİ ARIZA — VE BİR KAPSAM DENETİMİ KURALI. İlk sürüm iki hata taşıyordu: **(1) KAPSAM AÇIĞI** — `موه` *(su)* ne çok-lemmalı ne tek-lemmalı listede; tabloda olmayan kök **sessizce düşüyordu** (`روس` ise korpusta hiç yok, `رسو` zaten kümede). **(2) `هوي` YANLIŞ SINIFLANDI** — `هَواء` lemması hem 'hava' (14:43) hem 'heva, arzu' (28:50) taşıyor; tabloda olgu sayılmıştı ve 28:50'yi yanlış tutuyordu.",
 "olculen": {"kapsam_acigi": ["موه", "روس"],
             "moh_etkisi": "27:44 yanlış sebeple düşüyordu (su kökü sessizce eleniyordu)",
             "hoy_etkisi": "28:50 yanlış tutuluyordu",
             "eklenen_denetim": "OLGU kümesinin her kökü dört listeden birinde olmalı "
                                "(çok-lemmalı · tek-lemmalı · bağlam-gerekli · korpusta-yok); "
                                "açık varsa betik DURUR",
             "eklenen_liste": {"BAGLAM_GEREKLI": ["هوي"], "KORPUSTA_YOK": ["روس"]},
             "ikinci_ariza_sinifi": "elle yazılan lemmalarda ŞEDDE/HAREKE SIRASI korpustan "
                                    "farklı (0x64e+0x651 yerine 0x651+0x64e); NFC'de aynı ama "
                                    "dizge eşleşmesi tutmuyor — 10 kökte 16 girdi",
             "ikinci_ariza_cozumu": "tablo girdileri NFC üzerinden korpus biçimine ÇÖZÜLÜR, "
                                    "çözülemeyen varsa betik DURUR (çözülemeyen: 0)"},
 "durum": "KAPALI", "oncelik": "P1", "kaynak": "onarım 18 denetimi",
 "etiket": "kendi arızam + yeni denetim kuralı",
 "test_notu": "**Kapsam açığı sinsi bir arıza sınıfı: bir kök listede yoksa hata vermiyor, sessizce olgu-dışı sayılıyor.** Aday 905'in (`adsiz2` envanter boşluğu) ve aday 927'nin (`fig` KELLA) aynı ailesinden: **alan bir kümeye bakıyor ve kümenin eksikliği çıktıda görünmüyor.** Bunun için betiğe DURDURAN bir kapsam denetimi kondu. **İkinci arıza, Arapça dizgeleri elle yazmanın maliyeti:** şedde ile harekenin sırası korpustan farklı olunca eşleşme tutmuyor; `anahtar_denetim.py`'nin yakaladığı sınıfın ta kendisi. Çözüm aynı: **tabloya giren dizge korpustan çözülür, elle yazılan biçim yalnız okunabilirlik içindir.**"},
{"no": 946,
 "aday": "★★ `anahtar_denetim.py` OLGU KÜMESİNDE DÖRT YILLIK SESSİZ BİR ARIZA YAKALADI — `ريح` (RÜZGÂR) HİÇ EŞLEŞMİYORMUŞ. Denetim, olgu kümesindeki dört kökü işaretledi: **`ريح` korpusta YOK — rüzgâr `روح` kökü altında (LEM:رِيح)** · **`زتن` yok — zeytin `زيت`** · **`روس` yok — `رسو` zaten kümede** · **`ثلج` korpusta HİÇ YOK** (Kur'an'da kar geçmiyor). Yani tarayıcının v2 ve v3 sürümleri boyunca rüzgâr ve zeytin olgu köklerinin İKİSİ DE hiçbir ayette eşleşmedi.",
 "olculen": {"yanlis_kokler": {"ريح": "doğrusu روح, LEM:رِيح", "زتن": "doğrusu زيت",
                               "روس": "doğrusu رسو (zaten kümedeydi)",
                               "ثلج": "korpusta hiç yok"},
             "kac_surumdur": "v2 (16_cipa_tarama.py) ve v3 (21_cipa_tarama3.py)",
             "duzeltme_etkisi": {"yeni_aday": 2, "ayetler": ["12:94", "33:9"],
                                 "ikisi_de": "gerçek rüzgâr ayeti"},
             "روح_lemma_ayrimi": {"olgu": ["رِيح"], "dusen": ["رُوح", "رَوْح", "رَيْحان", "تُرِيحُ", "رَواح"]},
             "son_durum_v4": {"havuz": 481, "kesinlik_27_28": 47, "kesinlik_27_29": 48,
                              "anma_kurulum": "7/7", "anma_tutulan": "3/3", "cipa_kaybi": 0}},
 "durum": "KAPALI", "oncelik": "P0", "kaynak": "anahtar_denetim.py, lemma turu",
 "etiket": "denetimin yakaladığı sessiz arıza",
 "test_notu": "**Bu, `anahtar_denetim.py`'nin okuma dışı bir betikte bulduğu ilk gerçek ÖLÇÜM arızası** — şimdiye kadar yakaladıkları yazım tutarsızlığıydı, burada yakaladığı şey bir alanın körlüğü. **Ve arıza sinsi: yanlış yazılmış kök hata vermiyor, sadece hiçbir zaman eşleşmiyor.** Aday 945'in kapsam açığıyla (`موه`) aynı aile, ama bu daha eski ve daha büyük: rüzgâr, olgu kümesinin en sık kavramlarından biri ve iki sürüm boyunca ölü kalmış. **DERS: küme hâlinde yazılan Arapça kök listeleri, kullanılmadan önce korpusa karşı doğrulanmalı** — `28_olgu_lemma.py`'ye eklenen kapsam denetimi artık bunu yapıyor ama denetim ancak listedeki kök korpusta ARANIRSA iş görür; asıl koruma `anahtar_denetim.py`'nin T4 (korpusta hiç yok) kuralı."},
]

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.setdefault('AM_lemma', []).extend(ADAYLAR)
AD['son_guncelleme'] = 'P0 #5 lemma katmanı (a parçası) — adaylar 940-946'
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('aday_bulgular: AM_lemma →', len(AD['AM_lemma']),
      '|', AD['AM_lemma'][0]['no'], '-', AD['AM_lemma'][-1]['no'])

# aday 906 ve 923'e düşürüldü/tazeleme kaydı — özgün olculen KORUNUR
for kume in ('AJ_kasas', 'AK_ankebut'):
    for a in AD.get(kume, []):
        if a['no'] == 906:
            a['dusuruldu'] = {
              "ne_zaman": "onarım 17 koşulurken (aday 942)",
              "yanlis": "'lemma katmanı yazılsaydı nakarat2 28:5↔28:41 ve 28:30↔28:46 "
                        "çiftlerini görürdü' — İKİ VAKADA DA YANLIŞ",
              "gercek_1": "28:5↔28:41 ortak lemma dizisi 2 kelime; nakaratın alt sınırı 3 "
                          "(alt sınır 2'ye inince yakalanıyor)",
              "gercek_2": "28:30↔28:46 ortak birim TEK lemma; hiçbir n-gram alanıyla "
                          "yakalanamaz — bu bir kök seyri olgusu, nakarat değil",
              "sebep": "lemma katmanının kalıbı GÖRÜNÜR kılmasıyla alanın onu SAYMASI "
                       "aynı şey sanılmıştı",
              "korunan": "'lemma borcu yalnız gloss değil ÖLÇÜM borcu' kaydı DOĞRU çıktı"}
            print('aday 906: dusuruldu eklendi')
        if a['no'] == 923:
            a['dusuruldu'] = {
              "ne_zaman": "tarayıcı v4 koşulurken (aday 944)",
              "yanlis": "'kesinlik %41 → %54' — GERÇEK: %35 → %47 (sûre 27-28)",
              "sebep": "kesinlik okuma notlarındaki sayılardan hesaplanmıştı, tarayıcı "
                       "çıktısından değil — aday 843'ün dördüncü tekrarı",
              "eksik": "beşinci bir aday da düştü (27:44) ve sayılmamıştı",
              "korunan": "dört lemma vakasının DÖRDÜ DE düştü; yön ve kazanç büyüklüğü "
                         "(+12 puan, öngörü +13) tuttu"}
            print('aday 923: dusuruldu eklendi')
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

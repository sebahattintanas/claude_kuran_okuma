# -*- coding: utf-8 -*-
"""aday_ekle_33_ahzab.py — sûre 33 (Ahzâb) adayları (AR_ahzab) ve okuma bağları (AM_ahzab).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder; havuz boyu defterden değil aday_bulgular.json'dan okunur
ve betik sıranın kopmadığını doğrular.
"""
import json

AHZAB = [
# ---------------- blok 1-10 ----------------
{"no":979,
 "aday":"blok_goster.py BESMELE ARIZASI — 1. ayet ayıklaması yalnız 5 kelimelik açılışları (besmele + tek kelime) tanıyordu: 112 besmeleli açılışın 26'sı. 33:1 besmeleyle basılacaktı.",
 "olculen":{"eski_kural":"len(ayet)==5","eski_yakalanan":26,"yeni_yakalanan":112,"toplam":112,
   "yeni_kural":"1:1'in ilk dört kelimesinin iskeleti (korpustan, Arapça sabit yok)",
   "yan_bulgu":"1:1 metninin başında BOM (U+FEFF) — ilk denemede hiçbir sûre eşleşmedi"},
 "durum":"KAPALI","oncelik":"P0","kaynak":"sûre 33 okuması, blok 1-10","etiket":"okumayı bloke eden arıza — yerinde onarıldı",
 "test_notu":"Araç dondurma kararının istisnası: arıza okumayı fiilen bloke ediyordu. uret_blok_33 aynı kuralı taşıyor ve besmele kalırsa DURUYOR."},
{"no":980,
 "aday":"okuma_metni.json'da BESMELE KALINTISI — ayet düzeyinde kayıtlı 23 sûrenin (10-32) 6'sında 1. ayetin ar alanı besmeleyle başlıyor: 20, 21, 22, 25, 26, 27.",
 "olculen":{"taranan":"okuma_metni.json, ar alanı olan sûreler 10-32 (TAM SAYIM)","kirli":[20,21,22,25,26,27],"kirli_sayi":6,"taranan_sayi":23,
   "olcum_etkisi":"yok — ölçüm defterden (n temiz); yalnız görüntü metni"},
 "durum":"ACIK","oncelik":"P2","kaynak":"aday 979'un retroaktif taraması","etiket":"kayıt kirliliği",
 "test_notu":"Onarım ertelendi (dondurma). Tek betikle altı ar alanı kırpılabilir; özgün kayıt korunup 'duzeltildi' alanı eklenmeli."},
{"no":981,
 "aday":"★★ SAY ALANI YANLIŞ POZİTİFLERİ — zevc 'eş' anlamında (33:4, 33:6) ve a'adde 'hazırladı' (33:8, adad kökü IV. bab) sayı işareti sayılıyor; qalîl üç kez (33:16, 18, 20) miktar sözcüğü olarak işaretli.",
 "olculen":{"yanlis_pozitif":{"33:4":"zevc (eş)","33:6":"zevc (eş)","33:8":"a'adde (hazırlamak)"},
   "tartismali":{"33:16":"qalîl","33:18":"qalîl","33:20":"qalîl"},"blok":"33:1-20"},
 "durum":"ACIK","oncelik":"P1","kaynak":"sûre 33 okuması","etiket":"borç #13 (say alanı)",
 "test_notu":"Kök düzeyi eşleşme anlamı ayırmıyor: zevc hem 'çift' hem 'eş'. Korpus çapında zevc'in sayı/eş ayrımı sayılmadan alan kullanılamaz."},
{"no":982,
 "aday":"★ MM2 BİTİŞİKLİK KOŞULU — ardışık iki ayette iki mef'ûl-i mutlak: 33:10 (fiil + araya lafız + masdar) YAKALANMIYOR, 33:11 (bitişik) YAKALANIYOR.",
 "olculen":{"kacirilan":["27:58 (önceki kayıt)","33:10"],"yakalanan":["33:11"],"kural":"08_adli_ve_mm_onarim: aynı kök + ACC isim w+1'de"},
 "durum":"ACIK","oncelik":"P2","kaynak":"sûre 33 okuması","etiket":"araç açığı (aday 924: metin hakkında kanıt değil)",
 "test_notu":"Bitişik olmayan mef'ûl-i mutlak sayısı bilinmiyor. mm2 dağılımına dayanan hiçbir iddia bu açık kapanmadan kurulmaz."},
{"no":983,
 "aday":"★★ YILDIZIN OTOMATİK ★★★ TETİKLEYİCİLERİ — sûre 33'ün ilk 20 ayetindeki beş ★★★'ın beşi de otomatik: allah yoğunluğu (33:3, 6 kelimede 2 lafız, z=6,14), hapaks (33:4, 33:18, 33:19), edilgenlik (33:11, iki fiilin ikisi edilgen, z=5,38). İçerikten gelen ★★★ yok.",
 "olculen":{"ucyildiz":{"33:3":"allah 6,14","33:4":"hapaks 3,28","33:11":"pas 5,38","33:18":"hapaks 3,28","33:19":"hapaks 3,28"},
   "tek_olcut_sorunu":{"33:4":"hapaks + n 1,65 + kafiye kırığı","33:19":"hapaks + n 2,40"},
   "kaynak":"blok_bilanco.py (defter, TAM SAYIM)"},
 "durum":"ACIK","oncelik":"P1","kaynak":"sûre 33 okuması, bloklar 1-10 ve 11-20","etiket":"borç #7 ve #15",
 "test_notu":"Kısa ayette oran büyüyor (33:3, 33:11): ölçek etkisi. Formül en büyük |z|'yi alıyor, ikinci bağımsız işareti eklemiyor (33:4, 33:19)."},
{"no":984,
 "aday":"★★ FÂSILA: SÛRE 33'ÜN 73 AYETİNİN 72'Sİ A SINIFI, TEK İSTİSNA 33:4 (es-sebîl). Aynı lemma 33:67'de uzatma elifiyle (es-sebîlâ) ayet sonunda.",
 "olculen":{"sure_73":{"A":72,"ل":1},"istisna":"33:4","ayni_lemma_elifli":"33:67","kaynak":"defter fs alanı, TAM SAYIM"},
 "durum":"ACIK","oncelik":"P1","kaynak":"sûre 33 okuması — okurken fark edildi, sonra sayıldı","etiket":"okuma gözlemi",
 "test_notu":"Korpus çapında: aynı lemmanın aynı sûrede hem elifli hem elifsiz fâsıla olduğu kaç vaka var? Sayılmadan iddia kurulmaz."},
{"no":985,
 "aday":"★★★ ÖN-KAYIT §4.3 MÜHÜR TANIMI KONUM SÜZGECİ UYGULAMIYOR — son-üç içerik lemmasında esmâ lemması varsa mühür sayılıyor; göndergenin Allah olup olmadığına bakılmıyor.",
 "olculen":{"sure_33_1_20":{"muhur_43":7,"gecerli":5,"yanlis":2},
   "yanlis":{"33:11":"mü'min (insanlar)","33:17":"velî + nasîr ÇİFT ('Allah'tan başka')"},
   "blok":{"1-10":"5/5 geçerli","11-20":"0/2 geçerli"},
   "sinif_etkisi":"33:11 e_oto ile E sınıfı, e_el ile 0 sınıfı",
   "sinama_kumesine_ek":["33:6 mü'min ×2 + velî","33:11 mü'min","33:17 velî + nasîr"],
   "kaynak":"esma_kayit.json + esma_el.py"},
 "durum":"ACIK","oncelik":"P0","kaynak":"esmâ kaydı, sûre 33","etiket":"ön-kayıt dondurma öncesi karar noktası (4)",
 "test_notu":"Karar: mühür ve sınıf e_oto üzerinden mi e_el üzerinden mi tanımlanır? Dondurma §9 doldurulmadan kapanmalı. Sonuca bakılmadan karar verilmeli."},
{"no":986,
 "aday":"★★ ESMÂ TONU KAPSAMI — esma_listesi.json'un 72 lemmasından yalnız 26'sı varlik_katalog.json'da ton (cemâl/denge/celâl) taşıyor; 46'sı katalog-dışı. Katalogdaki azîm (denge) listede yok.",
 "olculen":{"liste":72,"katalogda_tonlu":26,"katalog_disi":46,"katalogda_listede_olmayan":["azîm"],"ilk_vaka":"33:3 vekîl"},
 "durum":"ACIK","oncelik":"P0","kaynak":"esmâ kaydı, sûre 33","etiket":"ön-kayıt dondurma öncesi karar noktası (3)",
 "test_notu":"Bu kapsamla H2'nin mühürlerinin çoğu tonsuz kalır. Ton ataması katalogdan mı genişletilir, yoksa H2 yalnız tonlu 26 lemmayla mı koşulur — dondurmadan önce karar."},
# ---------------- blok 11-20 ----------------
{"no":987,
 "aday":"★★★ KÖK GLOSSU KÖKÜN BASKIN ANLAMINI TAŞIMIYOR — belâ 'eskiyip yıpranma' (baskın anlam sınama), devr 'yurt, ev' (33:19 dönmek), velî 'dost, veli' (33:15 arka çevirmek).",
 "olculen":{"bela":{"gloss":"eskiyip yıpranma","envanter":"sınama lemmaları baskın; yıpranma lemması 2 kez"},
   "devr":{"gloss":"yurt, ev","33:19":"dönmek (fiil)"},
   "veli":{"gloss":"dost, veli; velâyet","envanter":"tevellâ 78 · vellâ 30 (çevirmek/yüz çevirmek)"},
   "blok":"33:11-20"},
 "durum":"ACIK","oncelik":"P1","kaynak":"sûre 33 okuması, blok 11-20","etiket":"borç #5b'nin kök düzeyi eşi",
 "test_notu":"belâ glossu daha önce okunan her ayette yanlış anlam basmış olabilir. Onarım retroaktif gloss turu ister; özgün gloss korunup 'duzeltildi' alanı eklenmeli."},
{"no":988,
 "aday":"★ QALÎLÂ FÂSILASI — sûre 33'te qalîlâ ile biten 4 ayet: 16, 18, 20, 60. Üçü ikinci blokta, çift sıradaki ayetlerde.",
 "olculen":{"ayetler":[16,18,20,60],"kaynak":"defter fs alanı, TAM SAYIM (sûre)"},
 "durum":"KAPATILAMAZ","oncelik":"P2","kaynak":"sûre 33 okuması — OKURKEN bulundu","etiket":"taraflı örneklem uyarısı (aday 899)",
 "test_notu":"Okuma sırasında fark edilen dizilim; boş model yok. Tek başına kanıt değil, yalnız kayıt."},
{"no":989,
 "aday":"TARAYICI v4 SÛRE 33 ARA BİRİKİM (1-20) — iki aday (33:9 G_bakış, 33:16 A_şart), ikisi de çıpa değil; L4 çıpa 0. Anma 0/0 · kesinlik 0/2.",
 "olculen":{"aday":["33:9","33:16"],"cipa_L4":[],"anma":"0/0","kesinlik":"0/2",
   "kademe_isaretli":{"33:4":"L1 olgu","33:9":"L0 olgu","33:10":"L0","33:13":"L3-benzeri, olgu değil","33:19":"L1"},
   "dizi":{"27":"4/4","28":"3/3","29":"3/3","30":"2/9","31":"0/3","32":"2/2"}},
 "durum":"ACIK","oncelik":"P0","kaynak":"sûre 33 okuması","etiket":"aday 948 birikimi (ara)",
 "test_notu":"Sûre bitince bu kayıt sûre toplamıyla güncellenir. Ölçüt DEĞİŞTİRİLMEDİ."},
{"no":990,
 "aday":"BİÇİM İHLÂLİ + KAYIT RİSKİ — 33:1-20 okuması dosyaya yazılıp sohbete yalnız bilanço verildi (sohbette 0/20 '### S:N' başlığı); ayrıca okuma_metni, mercek_kayit, adaylar ve bağlar tur sonuna bırakıldığı için 20 ayetin bulguları yapılandırılmış hâlde hiçbir yerde yoktu.",
 "olculen":{"baslik_sohbette":"0/20 → 33:1-10 yeniden okundu (10/10)","kayit_once":"yalnız kok_turkce, dikey JSON, esma_kayit, metin modülü",
   "karar":"BLOK BAŞI KAYIT (kullanıcı onayı 2026-09-24): uret_blok_33 + blok_bilanco + ahzab_kayit + bu betik her blokta koşulur"},
 "durum":"KAPALI","oncelik":"P0","kaynak":"kullanıcı düzeltmesi","etiket":"protokol ihlâli (aday 975 ailesi)",
 "test_notu":"Sûre 31'in tur sonunun atlanıp borca dönmesi aynı riskin gerçekleşmiş hâliydi. Blok başı kayıtla oturum yarıda kalsa da okunan her blok kayıtlı."},
]

BAGLAR = {"AM_ahzab": [
 {"bag":"33:4 ↔ 33:6","kural":"okuma gözlemi (أمم kökü sûrede 2 kez, TAM SAYIM)",
  "not":"Aynı etiket iki ayette ters yönde: 'eşlerinizi analarınız KILMADI' / 'eşleri onların ANALARIDIR'. Fark etiketi koyanda: ağızlarınızdaki söz / Kitap'ta yazılmış."},
 {"bag":"33:4 → 33:5","kural":"okuma gözlemi",
  "not":"Soy etiketinin reddi ve pozitif kuralı: babalarına nispet edin; baba bilinmezse dinde kardeş ve mevlâ."},
 {"bag":"33:4 · 33:5 · 33:10 · 33:12","kural":"kök [x/y] (قلب, sûrede 11)",
  "not":"Kalp dört ayette dört işlevde: bedensel organ · niyet eden kalp · gırtlağa dayanan kalp · hastalıklı kalp."},
 {"bag":"33:3 → 33:48","kural":"nakarat3 TAM (6 kelime / 2 ayet)",
  "not":"Tevekkül formülü sûrede aynen tekrarlanıyor."},
 {"bag":"33:7 → 4:21 · 4:154","kural":"xref (mîsâkan galîzan)",
  "not":"Aynı ifade üç ilişkide: peygamberler · evlilik · İsrâiloğulları. Sûre 4 okunmadığı için DOĞRULANMADI."},
 {"bag":"33:7-8 → 33:15","kural":"okuma gözlemi (سأل sûre içi 1-4/7; عهد ×2)",
  "not":"Ahit ve sorgu çifti: peygamberlerden ahit alınıp sâdıklara sorulacak (33:8) · kaçmayacaklarına ahit verenlerin ahdi sorulacak (33:15)."},
 {"bag":"33:10 ↔ 33:11","kural":"mm2 karşıt çifti",
  "not":"İki ardışık mef'ûl-i mutlak: 33:10 yakalanmıyor (araya lafız), 33:11 yakalanıyor (bitişik). Aday 982."},
 {"bag":"33:12 → 33:60","kural":"xref",
  "not":"Münafıklar ve kalplerinde hastalık olanlar sûrede ikinci kez."},
 {"bag":"33:13 → 33:16","kural":"kök (فرر)",
  "not":"33:13 firârâ ile kapanıyor, 33:16 kaçışın fayda vermediğini ölçüyor."},
 {"bag":"33:4 ↔ 33:67","kural":"fâsıla TAM SAYIM (sûre)",
  "not":"Aynı lemma: 33:4 elifsiz (sûrenin tek A-dışı fâsılası), 33:67 elifli. Aday 984."},
 {"bag":"33:20 → 33:22","kural":"kök (حزب, sûrede 3: 20'de iki, 22'de bir)",
  "not":"Sûrenin adı metinde ilk kez 33:20'de."},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AR_ahzab', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in AHZAB]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AR_ahzab'] = AHZAB
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AR_ahzab', len(AHZAB), '(%d-%d) | toplam aday' % (nos[0], nos[-1]), tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AM_ahzab', len(BAGLAR['AM_ahzab']))

# -*- coding: utf-8 -*-
"""aday_ekle_21_21_40.py — 21:21-40 bloğunun adayları ve elle kurulan bağları."""
import json

AB = json.load(open('aday_bulgular.json', encoding='utf-8'))
BG = json.load(open('okuma_baglantilari.json', encoding='utf-8'))

YENI = [
{
 "no": 438,
 "aday": "ARAÇ HATASI — SÖZ EDİMİ ETİKETLEYİCİSİ MUNKATI'A أَمْ *(yoksa)* SORUSUNU GÖRMÜYOR. Ayet başında أَمْ geçen 61 ayetin yalnız 4'ü kip alanında INTG taşıyor; 45'i düz 'haber' etiketli. Blokta iki örnek: 21:21 (أَمِ ٱتَّخَذُوٓا۟ *(yoksa edindiler mi)*, edim='haber') ve 21:24 (aynı açılış, edim='emir' — çünkü ayet içindeki قُلْ *(de ki)* baskın çıkıyor). Buna karşılık أَوَلَمْ *(görmediler mi)* (21:30) ve أَفَإِي۟ن *(peki… -se)* (21:34) INTG alıyor: yani hemze+edat birleşmeleri yakalanıyor, yalın أَمْ yakalanmıyor.",
 "olculen": {
   "ayet_basi_am": 61,
   "kip_INTG_tasiyan": 4,
   "edim_dagilimi": {"haber": 45, "emir+şart": 5, "şart": 3, "emir": 3, "soru": 2,
                     "soru+emir": 1, "yasak": 1, "soru+emir+şart": 1},
   "ayet_ici_am_gecen_ayet": 62,
   "blok_ornekleri": ["21:21", "21:24"]
 },
 "test": "TUR SONU ONARIMI + ÖLÇÜM. Onarım: defter4.py'nin edim/kip çıkarımına ayet-başı أَمْ (munkatı'a) kuralı eklenecek; ayrıca ayet-içi أَمْ (muttasıla, 62 ayet) AYRI etiketlenecek çünkü ikisi farklı işlev (biri yeni soru açar, öteki seçenek bağlar). Onarımdan SONRA ölçülecek soru: soru edimi düzeltildiğinde sûre 21'in söz edimi profili (haber 74 · soru 16) ne kadar kayıyor, ve korpus çapında 'soru' edimi kaç ayet artıyor? Bu, kayıtlı bütün söz-edimi dağılımlarını etkiler; onarım öncesi hiçbir söz-edimi bulgusu kapatılmayacak.",
 "uyari": "ARANARAK BULUNDU — 21:21'in ölçüm satırında edim='haber' görülünce korpus tarandı. BU BİR BULGU DEĞİL, ARAÇ HATASI KAYDIDIR. Okuma DURMADI (OKUMA_STANDARDI: okuma sırasında araç değiştirilmez); etkilenen ayetlerin ölçüm satırına artefakt notu düşüldü."
},
{
 "no": 439,
 "aday": "21:23 ↔ 34:25 — AYNI KÖKTEN İKİ EDİLGEN, AYNI YAPI, İKİ AYET. Korpusta aynı ayette aynı kökün 2+ edilgen geçişi olan ayet-kök çifti 63 tane. سأل *(sorma, isteme)* bunlardan yalnız İKİSİNDE: 21:23 لَا يُسْـَٔلُ عَمَّا يَفْعَلُ وَهُمْ يُسْـَٔلُونَ *(O yaptığından sorulmaz, onlar sorulurlar)* ve 34:25 قُل لَّا تُسْـَٔلُونَ عَمَّآ أَجْرَمْنَا وَلَا نُسْـَٔلُ عَمَّا تَعْمَلُونَ *(de ki: bizim işlediğimizden siz sorulmazsınız, sizin yaptığınızdan da biz sorulmayız)*. Ortak yapı: olumsuz edilgen + عَمَّا *(-den ki)* + IMPF fiil, iki kez, şahıs değiştirerek. FARK: 21:23'te ikinci edilgen OLUMLU (sorulurlar), 34:25'te ikisi de olumsuz — yani biri asimetri kuruyor, öteki simetri.",
 "olculen": {
   "korpus_ayni_kok_2plus_edilgen": 63,
   "sal_koku_ornekleri": [[21, 23], [34, 25]],
   "21_23": {"n": 6, "pas": 2, "z_pas": 3.48, "zmn": {"IMPF": 3}},
   "34_25": {"pas": 2}
 },
 "test": "ÖN-KAYIT. İki ayrı soru: (1) 63 ayet-kök çiftinin kök dağılımı nedir — نزل *(indirme)* ve أتي *(gelme, getirme)* baskın görünüyor; سأل bu listede seyrek mi? Ölçüt: kökün korpustaki toplam edilgen sayısına göre beklenen çift sayısı, Poisson. (2) Bu 63 çiftin kaçında iki edilgenin POLARİTESİ farklı (biri olumsuz biri olumlu)? 21:23 bu alt kümede mi? Motive eden ayet 21:23 testten DIŞLANARAK kurulacak.",
 "uyari": "ARANARAK BULUNDU — 21:23'ün pas=2 + ikile سأل ×2 ölçümü görülünce korpus tarandı. 34:25 bağı okuma sırasında elle kuruldu, xref vermedi (lemma 3-gram eşleşmiyor)."
},
{
 "no": 440,
 "aday": "İKİ HAPAKS TEK AYETTE — 21:30 LİSTE DEĞİL, KARŞIT ÇİFT. Korpusta 2+ hapaks kök taşıyan ayet yalnız 33 (%0,53; dağılım: 0 hapaks 5878 · 1 hapaks 325 · 2 hapaks 28 · 3 hapaks 3 · 4 hapaks 1 · 5 hapaks 1). Bu 33 ayetin çoğunda hapakslar AYNI ALANDAN BİR LİSTE oluşturuyor: 2:61 بصل *(soğan)*/بقل *(sebze)*/عدس *(mercimek)*/فوم *(sarımsak)*/قثأ *(hıyar)* · 6:143 ضأن *(koyun)*/معز *(keçi)* · 7:133 ضفدع *(kurbağa)*/قمل *(bit)* · 16:80 صوف *(yün)*/وبر *(tüy)*. 21:30'un رتق *(bitişik olma, ratk)* ve فتق *(ayırma, yarma (fatk))* çifti liste DEĞİL: aynı kalıptan (فَعْل) türeyen ve birbirinin karşıtı olan iki kelime, biri isim-durum biri fiil-eylem.",
 "olculen": {
   "hapaks_sayisi_dagilimi": {"0": 5878, "1": 325, "2": 28, "3": 3, "4": 1, "5": 1},
   "iki_plus_hapaks_ayet": 33,
   "oran": 0.0053,
   "21_30": {"hapaks": ["رتق", "فتق"], "z_hapaks": 6.98, "n": 18},
   "liste_tipi_ornekler": [[2, 61], [6, 143], [7, 133], [16, 80], [5, 3], [22, 27]]
 },
 "test": "ÖN-KAYIT. Ölçüt: 33 ayetin her biri için hapaks çiftinin (a) aynı semantik alanda liste mi, (b) karşıt/tamamlayıcı çift mi, (c) ilgisiz mi olduğu SINIFLANDIRILACAK — sınıflandırma kör yapılacak (ayet numarası gizli, yalnız kök çifti + kalıp verilecek). Sonra soru: karşıt-çift sınıfı beklenenden sık mı? Null: iki hapaks bir ayette rastgele buluşuyorsa karşıtlık oranı korpusun genel karşıt-kök oranına eşit olmalı. Motive eden ayet 21:30 sınıflandırmadan DIŞLANIR.",
 "uyari": "ARANARAK BULUNDU — 21:30'un hapaks z=6.98 ölçümü görülünce korpus tarandı. 'Karşıt çift' sınıflandırması YORUMDUR, ölçüm değildir; kör sınıflandırma olmadan sayılamaz."
},
{
 "no": 441,
 "aday": "21:22 — SÛRENİN TEK LAFIZ+RAB AYETİ, İKİ UZUN SESSİZLİK ARASINDA TEK TEPE. Enbiyâ'nın 6 Allah lafzı 5 ayete dağılmış (22, 57, 66, 67, 98); 21:22 tek başına İKİ lafız taşıyor (ayet-içi 6. ve 9. sıra) ve sûrenin 14 Rab geçişinden biriyle aynı ayette bulunuyor — sûrede lafız ile Rab'ın birlikte geçtiği BAŞKA ayet yok. Konum: öncesinde 21 ayetlik lafız-sessizliği (21:1-21), sonrasında 34 ayetlik lafız-sessizliği (21:23-56). KARŞILAŞTIRMA: Tâhâ'da lafız+Rab birlikteliği İKİ ayette vardı (20:73, 20:114 — aday 421 düzeltmesi).",
 "olculen": {
   "sure_21_allah_ayetleri": [22, 57, 66, 67, 98],
   "sure_21_allah_token": 6,
   "21_22": {"A_konum": [6, 9], "R": ["رَبّ"], "n": 13, "z_allah": 2.55},
   "onceki_sessizlik": 21,
   "sonraki_sessizlik": 34,
   "sure_21_rab_token": 14,
   "taha_lafiz_rab_birlikte": [[20, 73], [20, 114]]
 },
 "test": "ÖN-KAYIT (aday 428 ve 402 ile BİRLİKTE). Soru: lafız-sessizliği aralıklarının uzunluk dağılımı verildiğinde, tek bir ayette YIĞILMIŞ lafız (bir ayette 2+ token) uzun sessizliklerin sınırında bulunma eğiliminde mi? Ölçüt: korpustaki 2+ lafızlı ayetlerin her biri için önündeki ve arkasındaki sessizlik uzunlukları; null = lafız konumları permüte edilmiş (KONUM-EŞLİ, düz değil — aday 435). Motive eden ayet 21:22 dışlanır.",
 "uyari": "Ölçüm katmanından geldi (makro profil + blok kapanışı); sessizlik uzunlukları hesaplanarak bulundu — kısmen ARANARAK. Sûrenin geri kalanı (21:41-112) okunmadan sessizlik yapısı hakkında hüküm kurulmayacak."
},
{
 "no": 442,
 "aday": "شمس *(güneş)* ↔ قمر *(ay)* ZENGİNLEŞMESİ ÇİFT YÖNLÜ VE NEREDEYSE SİMETRİK. 21:33'ün dikey katmanından: شمس (n=33) için ▸sonra قمر ×129,3; قمر (n=27) için ▸önce شمس ×129,1. İki yön arasındaki fark %0,15. Karşılaştırma için aynı ayetin öteki çifti asimetrik: ليل *(gece)* ▸sonra نهر *(ırmak; gündüz)* ×60,3 ama نهر ▸önce girdirme ×67,1 (gece değil). Yani cisim çifti kilitli, süre çifti tek yönlü.",
 "olculen": {
   "sems_sonra_kamer": 129.3,
   "kamer_once_sems": 129.1,
   "fark_yuzde": 0.15,
   "n_sems": 33, "n_kamer": 27,
   "leyl_sonra_nehar": 60.3,
   "kaynak_ayet": "21:33"
 },
 "test": "ÖN-KAYIT + JACKKNIFE ZORUNLU. (1) Jackknife: ×129 katı tek bir donmuş kalıbın (وَٱلشَّمْسَ وَٱلْقَمَرَ *(güneşi ve ayı)*) ürünü mü? Her geçiş sırayla çıkarılıp kat yeniden hesaplanacak; قدس ×118,3 vakasında (aday kaydı) tek kolokasyonun bütün katı sürüklediği görülmüştü — aynı risk burada. (2) Simetri ölçütü: korpustaki bütün kavram çiftleri için önce/sonra kat oranı hesaplanıp |log(kat_ileri/kat_geri)| dağılımı çıkarılacak; شمس/قمر çiftinin bu dağılımdaki yeri belirlenecek. (3) AYRICA aday 437 (hizalama kalıp ayrımı) ile birlikte ele alınacak — donmuş kalıp ayrımı yapılmadan simetri iddiası kurulamaz.",
 "uyari": "Ayetin KENDİ dikey katmanından geldi, ayrıca aranmadı. Ama iki yönü KARŞILAŞTIRMAK bir seçimdir; simetri gözlemi jackknife'sız alıntılanamaz. 'Kilitli çift' ifadesi YORUMDUR."
},
]

var = {x.get('no') for x in AB.get('AB_enbiya', [])}
for y in YENI:
    if y['no'] not in var:
        AB['AB_enbiya'].append(y)

AB['son_guncelleme'] = "2026-08-27 — Enbiyâ 21:21-40 bloğu (adaylar 438-442)"
AB['okunan'] = {
  "sureler": AB['okunan']['sureler'],
  "ayet": 2196,
  "korpus_yuzde": 35.2,
  "not": "Sûre 20 TAM. Sûre 21 kısmi (1-40/112). Sûre 2 kısmi (1-20/286)."
}

# --- elle kurulan bağlar ---
YENI_BAG = [
 {"cift": ["21:23", "34:25"], "kural": "L1", "guven": "yuksek",
  "not": "AYNI KÖKTEN ÇİFT EDİLGEN: سأل *(sorma, isteme)* iki kez, ikisi de edilgen, ikisi de عَمَّا *(-den ki)* + IMPF ile tümleçleniyor. 21:23 لَا يُسْـَٔلُ … وَهُمْ يُسْـَٔلُونَ *(sorulmaz… onlar sorulurlar)* asimetrik (olumsuz/olumlu); 34:25 لَّا تُسْـَٔلُونَ … وَلَا نُسْـَٔلُ *(siz sorulmazsınız… biz de sorulmayız)* simetrik (ikisi de olumsuz). xref vermedi — lemma 3-gramı tutmuyor, bağ elle kuruldu. (aday 439)"},
 {"cift": ["21:26", "19:88"], "kural": "L1", "guven": "yuksek",
  "not": "TAM CÜMLE ALINTISI: وَقَالُوا۟ ٱتَّخَذَ ٱلرَّحْمَٰنُ وَلَدًۭا *(Rahmân çocuk edindi dediler)*. Meryem'de bu cümle ayetin TAMAMI (19:88, n=4); Enbiyâ'da aynı cümle ayetin ilk yarısı ve üzerine iki hamle biniyor: سُبْحَٰنَهُۥ *(O münezzehtir)* + بَلْ عِبَادٌۭ مُّكْرَمُونَ *(hayır, ikram edilmiş kullardır)*. Aynı söz, biri yalın biri cevaplı."},
 {"cift": ["21:30", "21:19"], "kural": "L2", "guven": "orta",
  "not": "İKİL GÖNDERGE ZİNCİRİ: 21:22'nin فِيهِمَآ *(o ikisinde)* zamiri ile 21:30'un كَانَتَا … فَفَتَقْنَٰهُمَا *(ikisi idi… onları ayırdık)* ikili morfolojisi aynı çifte dönüyor — سَّمَٰوَٰت وَٱلْأَرْض *(gökler ve yer)*, ilk kez 21:19'da adlandırılmış. Üç ayet boyunca gönderge adlandırılıp iki kez zamirle taşınıyor."},
 {"cift": ["21:33", "21:20"], "kural": "L2", "guven": "orta",
  "not": "AYNI KÖK, İKİ İŞ: سبح *(tesbih, tenzih; yüzme)* 21:20'de يُسَبِّحُونَ ٱلَّيْلَ وَٱلنَّهَارَ *(gece gündüz tesbih ederler)* bab II ve ibadet anlamında; 21:33'te يَسْبَحُونَ *(yüzerler)* bab I ve hareket anlamında. İki ayet ayrıca ٱلَّيْل *(gece)* ve ٱلنَّهَار *(gündüz)* çiftini paylaşıyor — 21:20'de ACC zarf, 21:33'te ACC mef'ûl. Aynı iki kelime, ayrı sözdizimsel rol."},
 {"cift": ["21:39", "21:40"], "kural": "L3", "guven": "yuksek",
  "not": "DÜŞMÜŞ ŞART CEVABI: 21:39 لَوْ يَعْلَمُ *(bir bilselerdi)* ile açılıyor ve cevabı verilmeden bitiyor; 21:40 بَلْ *(hayır, bilakis)* ile açılıp aynı özneyi (o vakit, 3FS) devralıyor. İki ayet tek cümlenin iki parçası gibi çalışıyor: birincide üç olumsuzlama (لَا يَكُفُّونَ *(savamazlar)* · وَلَا · وَلَا يُنصَرُونَ *(yardım görmezler)*), ikincide iki olumsuzlama (لَا يَسْتَطِيعُونَ *(güç yetiremezler)* · وَلَا يُنظَرُونَ *(mühlet verilmez)*). Beş olumsuzlama iki ayete yayılıyor."},
]
BG.setdefault('AA_enbiya', []).extend(YENI_BAG)

json.dump(AB, open('aday_bulgular.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(BG, open('okuma_baglantilari.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print("aday:", len(AB['AB_enbiya']), "AB_enbiya girdisi · toplam bağ AA_enbiya:", len(BG['AA_enbiya']))

# -*- coding: utf-8 -*-
"""aday_ekle_37_saffat.py — sûre 37 (Sâffât) adayları (AV_saffat) ve okuma bağları (AQ_saffat).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1037'den — X_aralik 1023-1036 araya girdi, 2026-10-05); betik sıranın kopmadığını doğrular.
"""
import json

SAFFAT = [
 # blok 11-20
 {'no': 1037, 'aday': "MORFOLOJİ ETİKET TUTARSIZLIĞI — mâte 'mit-' biçimi: korpusta mâte fiilinin kesreli 'mit-' biçimi 8 token; 6'sı PASS etiketli (23:35, 23:82, 37:16, 37:53, 50:3, 56:47 — hepsi 'e-izâ mitnâ/mittum … turâben ve izâmen' itiraz kalıbında), 2'si etken (19:23, 19:66 'mittu'). defter2 'pas' alanı PASS etiketini sayıyor; bu 6 ayetin 5'inde ★/★★ kaynağı pas (23:35 ★, 23:82 ★, 37:16 ★★; 37:53 ★★, 50:3 ★★ defter alanı, henüz okunmadı; 56:47 yıldız yok). Okumada 37:16 ★★ kaynağı incelenirken bulundu (TAM SAYIM morph.txt üzerinden).", 'olculen': {'mit_bicimi_token': 8, 'PASS': ['23:35', '23:82', '37:16', '37:53', '50:3', '56:47'], 'etken': ['19:23', '19:66'], 'yildiz_kaynagi_pas': ['23:35', '23:82', '37:16', '37:53', '50:3']}, 'durum': 'ACIK', 'oncelik': 'P1', 'kaynak': 'sûre 37 okuması, blok 11-20', 'etiket': 'araç açığı (aday 924): metin hakkında kanıt DEĞİL; araç geliştirme dondurulmuş, onarım tam okuma sonrası (1009 ailesine komşu)', 'ek_vaka': [{'ayet': '37:47', 'not': "ters yön: 'yunzefûn' (IV. bab, fethalı = edilgen biçim) PASS etiketsiz, edilgen alanı 0; aynı lemmanın 56:19 kesreli 'yunzifûn' biçimi etken. Edilgen etiketi biçimle iki yönde uyuşmuyor (fazla: mâte mit-; eksik: 37:47).", 'blok': '37:41-50'}]},
 {'no': 1038, 'aday': "MORFOLOJİ İ'RÂB TUTARSIZLIĞI — gayr-i munsarif özel ad mecrur konumda ACC: 37:114 ve 37:120 'alâ mûsâ ve hârûn' — harf-i cerden sonra atıfla mecrur Hârûn ACC etiketli (Mûsâ GEN). Aynı dizge 'rabbi mûsâ ve hârûn' 7:122'de Hârûn GEN, 26:48'de ACC; 40:24 'ilâ fir'avne ve hâmâne ve qârûn' — Fir'avn GEN, Hâmân ACC, Qârûn GEN. Aktör alanı rolü i'râb etiketinden türetiyor (aktor.py: ACC → 'meful'), bu yüzden 37:114 ve 37:120'de Hârûn 'rol meful' yazılıyor. Korpusta Hârûn 20 token: GEN 7, ACC 10, NOM 3 (morph.txt).", 'olculen': {'harun_token': 20, 'GEN': 7, 'ACC': 10, 'NOM': 3, 'mecrur_konumda_ACC': ['26:48', '37:114', '37:120'], 'ayni_dizge_farkli_etiket': {'7:122': 'GEN', '26:48': 'ACC'}, 'ayni_ayette_karisik': {'40:24': {'fir\'avn': 'GEN', 'hâmân': 'ACC', 'qârûn': 'GEN'}}}, 'durum': 'ACIK', 'oncelik': 'P2', 'kaynak': 'sûre 37 okuması, blok 111-120', 'etiket': "araç açığı (aday 924): metin hakkında kanıt DEĞİL; rol alanı (adlı aktör) etkileniyor; araç geliştirme dondurulmuş, onarım tam okuma sonrası (1037 ailesine komşu: morfoloji etiketi)", 'ek_vaka': [{'ayet': '37:123', 'not': "ters yön: 've inne ilyâse le-mine'l-murselîn' — İlyâs inne'nin ismi (mansub), morfoloji GEN etiketliyor; rol alanı 'mecrur' yazıyor. Gayr-i munsarif adın fethası i'râb etiketine iki yönde yanlış yansıyor (mecrur→ACC: Hârûn; mansub→GEN: İlyâs).", 'blok': '37:121-130'}, {'ayet': '37:139', 'not': "'ve inne yûnuse le-mine'l-murselîn' — Yûnus inne'nin ismi (mansub), morfoloji GEN; rol 'mecrur'. Aynı kalıp üç ayette: 37:123 İlyâs GEN (rol mecrur), 37:133 Lût ACC (rol meful; munsarif, tenvinli), 37:139 Yûnus GEN (rol mecrur) — yalnız munsarif ad doğru etiketli. Yûnus korpusta 4 token: 4:163 GEN, 6:86 ACC, 10:98 GEN, 37:139 GEN (morph.txt).", 'blok': '37:131-140'}]},
]

BAGLAR = {"AQ_saffat": [
 # blok 1-10
 {'bag': '15:16-18 ↔ 37:6-10', 'kural': "okuma — dört adım aynı sırada (süsleme · 'min kulli şeytân' koruma · 'illâ men' istisna · izleyen şihâb); 37:10↔15:18 ortak dizi 'fe-etbe'ahû şihâbun' 2 kelime, nakarat3 alt sınırının altında; KAPATILAMAZ", 'not': 'Göğün süslenmesi ve kulak verenin kovulması iki sûrede aynı iskeletle.'},
 {'bag': '15:17 → 37:7', 'kural': 'xref (defter: hifz · kull · şeytân)', 'not': "Sıfat farkı: racîm / mârid; fiil/mastar farkı: hafiznâ / hifzan."},
 {'bag': '37:6 → 41:12 · 67:5', 'kural': 'xref (defter: zeyyene · semâ · dunyâ) — henüz okunmadı', 'not': 'Dünya göğünün süslenmesi.'},
 # blok 11-20
 {'bag': '37:16 ↔ 37:53', 'kural': "nakarat3 ('e-izâ mâte kâne turâb izâm e-inne', 6 kelime, sûre içi 2 ayet; defterden koşuldu) + esit2 BENZER — 37:53 henüz okunmadı", 'not': 'Ölüp toprak ve kemik olunca mı.'},
 {'bag': '23:82 → 37:16', 'kural': 'esit2 BENZER (0,9275) + xref', 'not': "23:82'de 'qâlû' ile, 37:16'da alıntı 37:15 'qâlû'dan sürüyor."},
 {'bag': '11:7 · 34:43 → 37:15', 'kural': "metin sayımı (harekesiz): 'in hâzâ illâ sihrun mubîn' — korpusta 5 ayet (5:110, 6:7 henüz okunmadı); nakarat3 sûre içi, xref boş", 'not': 'Apaçık büyüden başka bir şey değil.'},
 {'bag': '36:52 → 37:20', 'kural': "metin sayımı: 'yâ veylenâ' (2 kelime; korpusta 21:97, 36:52, 37:20), nakarat3 alt sınırının altında", 'not': 'Diriliş anında inkârcıların nidâsı.'},
 {'bag': '37:4 ↔ 37:19 · 37:2 ↔ 37:19', 'kural': 'kök ipliği (وحد [2/2], زجر [3/3]) — okumada görüldü, KAPATILAMAZ', 'not': "'vâhid' ilâhın, 'vâhide' haykırışın sıfatı; 'zâcirât zecran' → 'zecre'."},
 # blok 21-30
 {'bag': '37:25 ↔ 37:92', 'kural': "nakarat3 ('mâ lekum lâ', 3 kelime, sûre içi 2 ayet; defterden koşuldu; süzgeç GEÇMEZ) — 37:92 henüz okunmadı", 'not': 'Size ne oluyor ki … -mıyorsunuz.'},
 {'bag': '37:27 ↔ 37:50', 'kural': 'nakarat3 (5 kelime, tür tam; defterden koşuldu) + esit2 TAM; ayrıca esit2 52:25 TAM, 68:30 BENZER — henüz okunmadı', 'not': 'Birbirlerine dönüp soruşurlar.'},
 {'bag': '37:24 → 37:27', 'kural': "kök ipliği سأل (mes'ûlûn → yetesâelûn) — okumada görüldü, KAPATILAMAZ", 'not': 'Sorgulanacak olanlar birbirlerine soruyor.'},
 {'bag': '37:20 → 37:21', 'kural': "okuma — 'hâzâ yevmu …' 2 kelime, nakarat3 alt sınırının altında", 'not': 'din günü → ayrım günü.'},
 # blok 31-40
 {'bag': '37:31 → 37:38', 'kural': "kök ipliği ذوق [1/2]→[2/2] + yapı (inne + lâm + 'zâiq' ortacı) — okumada görüldü, KAPATILAMAZ", 'not': "'biz tadacağız' (suçluların ağzında) → 'siz tadacaksınız' (hitap)."},
 {'bag': '37:31 → 37:37', 'kural': 'kök ipliği حقق [2/2] — okumada görüldü, KAPATILAMAZ', 'not': "'Rabbimizin sözü hak oldu' → 'hakkı getirdi'."},
 {'bag': '37:40 ↔ 37:74 · 37:128 · 37:160 (· 37:169)', 'kural': "nakarat3 ('illâ ibâda'llâhi'l-muhlesîn' 4 kelime tam, 4 ayet; 3 kelimelik 5 ayet; defterden koşuldu) + esit2 — eşler henüz okunmadı", 'not': "Allah'ın ihlâsa erdirilmiş kulları müstesna."},
 {'bag': '37:35 → 47:19', 'kural': "metin sayımı (harekesiz): 'lâ ilâhe illa'llâh' — 47:19 henüz okunmadı", 'not': 'Tevhid cümlesinin tam dizgesi.'},
 # blok 41-50
 {'bag': '37:27 ↔ 37:50', 'kural': 'nakarat3 (5 kelime, tür tam) + esit2 TAM — iki ucu da okundu; bağlaç farkı ve- / fe-', 'not': 'Aynı cümle iki karşıt grupta: suçlular (37:27) / muhlas kullar (37:50).'},
 {'bag': '37:46 → 37:49', 'kural': 'kök ipliği بيض [2/2] — okumada görüldü, KAPATILAMAZ', 'not': 'kadehin beyazlığı → saklı yumurta benzetmesi.'},
 {'bag': '37:36 → 37:43', 'kural': 'kök ipliği جنن (mecnûn → cennât) — okumada görüldü, KAPATILAMAZ', 'not': 'Suçluların deli dediği → nimet cennetleri.'},
 {'bag': '37:27 → 37:44', 'kural': 'kök ipliği قبل (aqbele → mutekâbilîn) — okumada görüldü, KAPATILAMAZ', 'not': 'Birbirine yönelip suçlama → karşılıklı tahtlar.'},
 # blok 51-60
 {'bag': '37:16 ↔ 37:53', 'kural': "nakarat3 (6 kelime, sûre içi 2 ayet) + esit2 BENZER — iki ucu da okundu; son kelime meb'ûsûn → medînûn", 'not': 'Aynı itiraz iki ağızda: inkârcıların kendisi / cennettekinin arkadaşı.'},
 {'bag': '37:23 → 37:55', 'kural': "kök ipliği جحم (sırâti'l-cahîm → sevâ'i'l-cahîm) — okumada görüldü, KAPATILAMAZ", 'not': 'cahîmin yolu → cahîmin ortası.'},
 {'bag': '37:31 ↔ 37:57', 'kural': 'Rab konuşanın ağzında (rabbinâ / rabbî) — okumada görüldü, KAPATILAMAZ', 'not': 'Suçluların Rabbi hükmün sahibi, cennettekinin Rabbi nimetin sahibi.'},
 {'bag': '37:16 · 37:53 · 37:58 · 37:59', 'kural': 'kök ipliği موت [4/4] — okumada görüldü, KAPATILAMAZ', 'not': 'ölüm iki kez itirazda, iki kez cennettekinin ağzında.'},
 {'bag': '37:60 ↔ 37:106', 'kural': "nakarat3 ('inne hâzâ le-huve', 3 kelime; süzgeç GEÇMEZ) — 37:106 henüz okunmadı", 'not': 'Şüphesiz bu … ta kendisidir.'},
 # blok 61-70
 {'bag': '37:11 ↔ 37:62', 'kural': "okuma — karşılaştırma sorusu iskeleti ('e-… + üstünlük sıfatı + temyiz + em'), nakarat3 dışında — KAPATILAMAZ", 'not': 'yaratılışça mı daha çetin / konukluk olarak mı daha hayırlı.'},
 {'bag': '37:23 → 37:55 → 37:64 → 37:68', 'kural': "kök ipliği جحم (sırât → sevâ' → asl → merci') — okumada görüldü, KAPATILAMAZ", 'not': 'cahîmin yolu, ortası, dibi; dönüş yeri.'},
 {'bag': '37:49 ↔ 37:65', 'kural': "okuma — sûredeki iki 'ke-enne' teşbihi (metin sayımı), karşıt sahnelerde — KAPATILAMAZ", 'not': 'saklı yumurta / şeytan başları.'},
 {'bag': '37:17 → 37:69', 'kural': 'kök ipliği أبو — okumada görüldü, KAPATILAMAZ', 'not': 'ilk atalarımız da mı (itiraz) → atalarını sapmış buldular (anlatıcı).'},
 {'bag': '37:8 → 37:66', 'kural': "kök ipliği ملأ [2/2] (mele' → mâli'ûn) — okumada görüldü, KAPATILAMAZ", 'not': 'yüce topluluk / karınlarını dolduranlar.'},
 # blok 71-80
 {'bag': '37:40 ↔ 37:74', 'kural': 'nakarat3 (4 kelime, tür tam; sûre içi 4 ayet) — iki ucu okundu', 'not': 'suçlulardan (40) ve uyarılanlardan (74) aynı istisna.'},
 {'bag': '10:73 → 37:73 · 21:76 → 37:76', 'kural': 'xref (defter) — iki ucu da okundu; ikisinde de Nûh bağlamı', 'not': 'uyarılanların sonu / ailesiyle büyük sıkıntıdan kurtarma.'},
 {'bag': '37:34 ↔ 37:80', 'kural': "okuma — 'innâ kezâlike' + fiil + grup çerçevesi (nakarat3 dışında), KAPATILAMAZ", 'not': 'suçlulara böyle yaparız / iyileri böyle ödüllendiririz.'},
 {'bag': '37:72 → 37:73', 'kural': 'kök ipliği نذر (munzirîn → munzerîn, etken/edilgen ortaç) — okumada görüldü, KAPATILAMAZ', 'not': 'uyaranlar / uyarılanlar.'},
 {'bag': '37:78 ↔ 37:108 · 37:129 ; 37:80 ↔ 37:105 · 37:110 · 37:121 · 37:131 ; 37:76 ↔ 37:115', 'kural': 'nakarat3 (defterden koşuldu) — eşler henüz okunmadı', 'not': 'kıssa kapanış formülleri.'},
 # blok 81-90
 {'bag': '26:66 → 37:82', 'kural': 'esit2 TAM — iki ucu okundu; 26:66 Mûsâ kıssası, 37:82 Nûh kıssası', 'not': 'Sonra ötekileri boğduk.'},
 {'bag': '26:70 → 37:85', 'kural': "esit2 YAKIN — iki ucu okundu; ikisinde de İbrâhîm, fark 'mâ' / 'mâzâ'", 'not': 'Babasına ve kavmine neye tapıyorsunuz dedi.'},
 {'bag': '37:23 → 37:86', 'kural': 'kök ipliği دون [2/2] (dûn + lafız iki kez) — okumada görüldü, KAPATILAMAZ', 'not': "tapılanlar Allah'tan başka (anlatıcı) / Allah'ı bırakıp ilâhlar mı (İbrâhîm)."},
 {'bag': '37:35-36 ↔ 37:86', 'kural': 'okuma — tekil ilâh/lafız + çoğul âliha aynı bağlamda, iki ağızda — KAPATILAMAZ', 'not': "suçluların ilâhlarımız'ı / İbrâhîm'in uydurma ilâhlar'ı."},
 {'bag': '37:81 ↔ 37:111 · 37:122 · 37:132', 'kural': 'nakarat3 (defterden) — eşler henüz okunmadı', 'not': 'bizim inanan kullarımızdan.'},
 # blok 91-100
 {'bag': '37:25 ↔ 37:92', 'kural': "nakarat3 ('mâ lekum lâ', 3 kelime; süzgeç GEÇMEZ) — iki ucu okundu", 'not': 'zalimlere: yardımlaşmıyorsunuz / putlara: konuşmuyorsunuz.'},
 {'bag': '21:70 → 37:98', 'kural': 'esit2 BENZER + xref — iki ucu okundu; son kelime ahserîn / esfelîn', 'not': 'Ona tuzak kurmak istediler, biz onları … kıldık.'},
 {'bag': '18:21 → 37:97', 'kural': "xref (qâle · benâ · bunyân) — iki ucu okundu; bağlam farklı (mağara ehli / İbrâhîm)", 'not': 'bir yapı kurun.'},
 {'bag': '37:85 → 37:95', 'kural': 'okuma — İbrâhîm\'in ilk ve son sorusu aynı fiille (ta\'budûn) — KAPATILAMAZ', 'not': 'neye tapıyorsunuz / yonttuğunuza mı tapıyorsunuz.'},
 {'bag': '37:23 → 37:99', 'kural': 'kök ipliği هدي (fe\'hdûhum ilâ sırâti\'l-cahîm → se-yehdîn) — okumada görüldü, KAPATILAMAZ', 'not': 'cahîmin yoluna yöneltilenler / bana yol gösterecek.'},
 {'bag': '37:39 → 37:96', 'kural': "kök ipliği عمل [4/4] + 'mâ … ta'melûn' sıla yapısı — okumada görüldü, KAPATILAMAZ", 'not': 'yaptıklarınızla cezalandırılırsınız / sizi ve yaptıklarınızı Allah yarattı.'},
 {'bag': '37:60 ↔ 37:106', 'kural': "nakarat3 ('inne hâzâ le-huve', 3 kelime; süzgeç GEÇMEZ) — iki ucu okundu", 'not': "el-fevzu'l-azîm / el-belâu'l-mubîn."},
 {'bag': '37:78 ↔ 37:108', 'kural': 'esit2 TAM + nakarat3 (4 kelime) — iki ucu okundu; 37:129 henüz okunmadı', 'not': 'Sonrakiler arasında ona (iyi bir ad) bıraktık.'},
 {'bag': '37:80 ↔ 37:105 · 37:110', 'kural': "nakarat3 (4 kelime 'innâ kezâlike …' 80/105; 3 kelime 110) + esit2 80↔110 BENZER — okunan uçlar; 37:121, 37:131, 77:44 henüz okunmadı", 'not': "İbrâhîm kıssasında 'innâ'lı biçim 105'te, 110'da 'innâ' yok."},
 {'bag': '37:79 → 37:109', 'kural': "okuma — 'selâmun alâ' + ad; 37:79'da 'fi'l-âlemîn' var, 37:109'da yok — esit2 boş, KAPATILAMAZ", 'not': "Nûh'a / İbrâhîm'e selâm."},
 {'bag': '37:75 → 37:104', 'kural': "kök ipliği ندي [2/2] — Nûh bize seslendi / biz İbrâhîm'e seslendik; okumada görüldü, KAPATILAMAZ", 'not': 'nâdânâ / nâdeynâhu.'},
 {'bag': '18:69 · 28:27 → 37:102', 'kural': "xref ('setecidunî in şâ'a'llâh') — üç ucu okundu; sâbiran / mine's-sâlihîn / mine's-sâbirîn", 'not': 'inşallah beni … bulacaksın.'},
 {'bag': '37:102 → 37:107', 'kural': 'kök ipliği ذبح [2/2] (ezbahuke → zibh) — okumada görüldü, KAPATILAMAZ', 'not': 'seni boğazlıyorum / büyük bir kurbanlık.'},
 {'bag': '37:85 → 37:102', 'kural': "kök ipliği أبو — 'li-ebîhi' (İbrâhîm'in babası) / 'yâ ebeti' (İbrâhîm'e oğlunun hitabı); okumada görüldü, KAPATILAMAZ", 'not': 'İbrâhîm oğul ve baba konumunda.'},
 {'bag': '37:100 → 37:101', 'kural': "okuma — dua ('heb lî') ve cevap ('beşşernâhu') ardışık; KAPATILAMAZ", 'not': 'bağışla / müjdeledik.'},
 {'bag': '37:78-81 ↔ 37:108-111', 'kural': 'esit2 TAM (78↔108, 81↔111) + nakarat3 — kıssa kapanışı dört ayet aynı sırada; iki ucu okundu; 37:122, 37:129, 37:132 henüz okunmadı', 'not': 'tereknâ · selâm · kezâlike · innehû.'},
 {'bag': '37:101 → 37:112', 'kural': "kök ipliği بشر [2/2] — 'beşşernâhu bi-' iki kez; ilkinde nesne adsız (ğulâm), ikincisinde adlı (İshâq); okumada görüldü, KAPATILAMAZ", 'not': 'iki müjde.'},
 {'bag': '37:100 → 37:112', 'kural': "kök ipliği صلح [2/2] — 'mine's-sâlihîn' duada ve müjdede; okumada görüldü, KAPATILAMAZ", 'not': 'bana sâlihlerden bağışla / sâlihlerden bir peygamber.'},
 {'bag': '37:77 → 37:113', 'kural': 'kök ipliği ذرر [2/2] — Nûh\'un soyu (kalanlar) / İbrâhîm ve İshâq\'ın soyu (iki sınıf); okumada görüldü, KAPATILAMAZ', 'not': 'zurriyye.'},
 {'bag': '37:76 ↔ 37:115', 'kural': "nakarat3 ('mine'l-kerbi'l-azîm', 3 kelime; süzgeç GEÇMEZ) + aynı iskelet (necceynâ + nesne + ve + topluluk) — iki ucu okundu", 'not': 'ehl / qavm.'},
 {'bag': '37:114 ↔ 37:120', 'kural': "nakarat3 ('alâ mûsâ ve hârûn', süzgeç GEÇMEZ) — kıssanın açılış ayeti ve selam ayeti; iki ucu okundu", 'not': 'lütuf / selâm.'},
 {'bag': '37:23 → 37:118', 'kural': 'kök ipliği هدي + صرط — sırâtu\'l-cahîm / es-sırâtu\'l-mustaqîm; okumada görüldü, KAPATILAMAZ', 'not': 'cahîmin yoluna yöneltin / dosdoğru yola ilettik.'},
 {'bag': '37:25 → 37:116', 'kural': 'kök ipliği نصر — tenâsarûn (yardımlaşamayanlar) / nasarnâhum; okumada görüldü, KAPATILAMAZ', 'not': 'yardım.'},
 {'bag': '37:79 · 37:109 → 37:120', 'kural': "okuma — selam formülü üç kıssada; yalnız 37:79'da 'fi'l-âlemîn'; esit2 boş, KAPATILAMAZ", 'not': 'Nûh / İbrâhîm / Mûsâ ve Hârûn.'},
 {'bag': '37:119-122', 'kural': "kıssa kapanış dörtlüsü üçüncü kez (Mûsâ-Hârûn, ikil zamir): 78-81 / 108-111 / 119-122 — okumada görüldü; esit2 119'da boş, 121 TAM, 122 YAKIN", 'not': 'tereknâ · selâm · kezâlike · innehumâ.'},
 {'bag': '26:106 · 26:124 · 26:142 · 26:161 · 26:177 → 37:124', 'kural': "metin sayımı ('e-lâ tettaqûn', 6 ayet) — defter bağı yok, KAYIT", 'not': 'peygamberin kavmine ilk sorusu.'},
 {'bag': '23:14 → 37:125', 'kural': "metin sayımı ('ahsenu'l-hâlikîn', 2 ayet) — defter bağı yok, KAYIT", 'not': 'yaratılış aşamalarının sonunda / Ba\'l karşısında.'},
 {'bag': '26:26 → 37:126', 'kural': 'esit2 BENZER + xref — iki ucu okundu; Mûsâ (NOM) / İlyâs (ACC, bedel); 44:8 henüz okunmadı', 'not': 'sizin ve önceki atalarınızın Rabbi.'},
 {'bag': '37:17 → 37:126', 'kural': "kök ipliği أبو [5/5] + 'âbâ … el-evvel' — inkârcının ağzında / peygamberin ağzında; okumada görüldü, KAPATILAMAZ", 'not': 'ilk atalarımız da mı / önceki atalarınızın Rabbi.'},
 {'bag': '37:57 → 37:127', 'kural': "kök ipliği حضر — 'muhdarîn' / 'muhdarûn'; okumada görüldü, KAPATILAMAZ", 'not': 'getirilenler.'},
 {'bag': '37:40 · 37:74 ↔ 37:128', 'kural': "esit2 TAM + nakarat3 — okunan üç vakada istisnadan önce akıbet cümlesi (38-39 / 73 / 127); KAPATILAMAZ; 37:160, 37:169 henüz okunmadı", 'not': "illâ ibâda'llâhi'l-muhlasîn."},
 {'bag': '37:79 · 109 · 120 → 37:130', 'kural': 'okuma — selam formülü dördüncü kez; esit2 boş, KAPATILAMAZ', 'not': 'Nûh / İbrâhîm / Mûsâ-Hârûn / İlyâs.'},
 {'bag': '37:129-132', 'kural': 'kıssa kapanış dörtlüsü dördüncü kez (İlyâs): 78-81 / 108-111 / 119-122 / 129-132 — okumada görüldü, KAPATILAMAZ', 'not': 'tereknâ · selâm · kezâlike · innehû.'},
 {'bag': '37:123 · 37:133 · 37:139', 'kural': "metin sayımı ('le-mine'l-murselîn', 5 ayet; 2:252, 36:3 ile) + kıssa açılış kalıbı 've inne X' — KAYIT", 'not': 'İlyâs / Lût / Yûnus.'},
 {'bag': '26:170-172 → 37:134-136', 'kural': 'xref 26:170 + esit2 26:171 TAM + esit2 26:172 TAM — üç ardışık ayet, iki ucu okundu', 'not': 'Lût: kurtarılış, yaşlı kadın, yerle bir ediliş.'},
 {'bag': '37:76 · 37:115 → 37:134', 'kural': "kök ipliği نجو [3/3] — 'necceynâ + nesne + ve + topluluk' üç kıssada; okumada görüldü, KAPATILAMAZ", 'not': 'Nûh / Mûsâ-Hârûn / Lût.'},
 {'bag': '37:82 → 37:136', 'kural': "okuma — 'summe + 1P fiil + el-âharîn' (boğduk / yerle bir ettik); KAPATILAMAZ", 'not': 'öbürleri.'},
 {'bag': '26:119 · 36:41 → 37:140', 'kural': "metin sayımı ('el-fulki'l-meşhûn', 3 ayet) — üçü okundu, defter bağı yok, KAYIT", 'not': 'dolu gemi.'},
 {'bag': '37:16 → 37:144', 'kural': "kök ipliği بعث [2/2] — 'le-meb'ûsûn' (inkârcıların sorusu) / 'yevmi yub'asûn'; okumada görüldü, KAPATILAMAZ", 'not': 'diriltilecek miyiz / diriltilecekleri gün.'},
 {'bag': '37:66 → 37:144', 'kural': 'kök ipliği بطن [2/2] — karınlar (zakkum) / balığın karnı; okumada görüldü, KAPATILAMAZ', 'not': 'butûn / batn.'},
 {'bag': '37:89 → 37:145', 'kural': "kök ipliği سقم [2/2] — 'innî sakîm' (İbrâhîm) / 've huve sakîm' (Yûnus); okumada görüldü, KAPATILAMAZ", 'not': 'hasta.'},
 {'bag': '37:62 · 37:64 → 37:146', 'kural': 'kök ipliği شجر [3/3] — zakkum ağacı ×2 / yaqtîn ağacı; okumada görüldü, KAPATILAMAZ', 'not': 'sûrenin üç ağacı.'},
 {'bag': '37:11 → 37:149 · 37:150', 'kural': "kök ipliği فتي [2/2] + 'em … halaqnâ' — 'fe'steftihim' ile açılan iki soru, sûrenin başında ve 149-150'de; okumada görüldü, KAPATILAMAZ", 'not': 'onlara sor.'},
 {'bag': '37:142 ↔ 37:145', 'kural': "okuma — hâl kalıbı 've huve + sıfat' (mulîm / sakîm); KAPATILAMAZ", 'not': 'kınanacak hâlde / hasta hâlde.'},
 {'bag': '37:86 → 37:151', 'kural': "kök ipliği أفك [2/2] — İbrâhîm'in 'e-ifken' sorusu / 'min ifkihim'; okumada görüldü, KAPATILAMAZ", 'not': 'uydurma.'},
 {'bag': '37:21 · 37:127 → 37:152', 'kural': 'kök ipliği كذب [3/3] — tukezzibûn → kezzebûhu → kâzibûn; okumada görüldü, KAPATILAMAZ', 'not': 'yalanlama / yalancılar.'},
 {'bag': '37:149 ↔ 37:153', 'kural': 'kök ikilemesi بني — benât/benûn → benât/benîn, dört ayet arayla; okumada görüldü, KAPATILAMAZ', 'not': 'kızlar / oğullar.'},
 {'bag': '37:25 · 37:92 → 37:154', 'kural': "okuma — 'mâ lekum' üçüncü kez (suçlular / putlar / inkârcılar); KAPATILAMAZ; 68:36 esit2 TAM henüz okunmadı", 'not': 'size ne oluyor.'},
 {'bag': '37:13 → 37:155', 'kural': "kök ipliği ذكر — 'lâ yezkurûn' / 'e-fe-lâ tezekkerûn'; 37:138 ile aynı 'e-fe-lâ + 2MP' kalıbı; okumada görüldü, KAPATILAMAZ", 'not': 'hatırlamazlar / düşünmüyor musunuz.'},
 {'bag': '37:30 → 37:156', 'kural': 'kök ipliği سلط [2/2] — sultân (güç) / sultân (delil); okumada görüldü, KAPATILAMAZ', 'not': 'iki anlam.'},
 {'bag': '37:117 → 37:157', 'kural': 'kök ipliği كتب [2/2] — verilen kitap / istenen kitap; okumada görüldü, KAPATILAMAZ', 'not': 'el-kitâbe\'l-mustebîn / bi-kitâbikum.'},
 {'bag': '37:127 ↔ 37:158', 'kural': "kök ipliği حضر [3/3] — 'innehum le-muhdarûn' iki kez; okumada görüldü, KAPATILAMAZ", 'not': 'getirilecekler.'},
 {'bag': '23:91 → 37:159', 'kural': "xref ('subhâna'llâhi ammâ yesifûn') — iki ucu okundu", 'not': 'tesbih kalıbı.'},
 {'bag': '37:40 · 74 · 128 ↔ 37:160', 'kural': 'esit2 TAM + nakarat3 — dördüncü vaka; akıbet cümlesi 158, arada 159 tesbih — KAPATILAMAZ; 37:169 henüz okunmadı', 'not': "illâ ibâda'llâhi'l-muhlasîn."},
 {'bag': '37:85 · 37:95 → 37:161', 'kural': "kök ipliği عبد — 'mâ ta'budûn' İbrâhîm'in sorusunda / anlatıcının haberinde; okumada görüldü, KAPATILAMAZ", 'not': 'taptıklarınız.'},
 {'bag': '37:63 → 37:162', 'kural': 'kök ipliği فتن [2/2] — fitne (zakkum) / fâtinîn; okumada görüldü, KAPATILAMAZ', 'not': 'fitne.'},
 {'bag': '37:41 → 37:164', 'kural': "okuma — 'X-un ma'lûm' (rızık / makam); KAPATILAMAZ", 'not': 'bilinen.'},
 {'bag': '37:1 → 37:165', 'kural': 'kök ipliği صفف [3/3] — sûrenin ilk kelimesi (adsız topluluk, yemin) / konuşan \'biz\'; kök yalnız bu iki yerde; aynılık metinde söylenmiyor — KAPATILAMAZ', 'not': 'sâffât / sâffûn.'},
 {'bag': '37:143 → 37:166', 'kural': "kök ipliği سبح — 'musebbihîn' (Yûnus) / 'musebbihûn' ('biz'); okumada görüldü, KAPATILAMAZ", 'not': 'tesbih edenler.'},
 {'bag': '37:40 · 74 · 128 · 160 → 37:169', 'kural': "esit2 BENZER — öbek dört kez anlatıcıda istisna, burada inkârcıların ağzında şartın cevabı; okumada görüldü, KAPATILAMAZ; xref 4:172 okundu", 'not': "ibâda'llâhi'l-muhlasîn."},
 {'bag': '37:25 · 37:116 → 37:172', 'kural': 'kök ipliği نصر [3/3] — tenâsarûn → nasarnâhum → mansûrûn; okumada görüldü, KAPATILAMAZ', 'not': 'yardım.'},
 {'bag': '37:116 → 37:173', 'kural': "kök ipliği غلب [2/2] — 'humu'l-ğâlibîn' / 'lehumu'l-ğâlibûn'; okumada görüldü, KAPATILAMAZ", 'not': 'galip gelenler.'},
 {'bag': '37:90 → 37:174 · 37:178', 'kural': "kök ipliği ولي [3/3] — 'tevellev anhu' (kavim İbrâhîm'den) / 'tevelle anhum' (Peygambere emir); okumada görüldü, KAPATILAMAZ", 'not': 'yüz çevirme.'},
 {'bag': '37:174-175 ↔ 37:178-179', 'kural': 'esit2 BENZER + nakarat3 (174/178 GEÇER, 175/179 GEÇMEZ) — iki ucu okundu; her tekrarda bir öğe değişiyor (fe/ve, nesne zamiri)', 'not': 'yüz çevir / gözetle.'},
 {'bag': '26:204 → 37:176', 'kural': 'esit2 TAM — iki ucu okundu', 'not': 'azabımızı mı acele istiyorlar.'},
 {'bag': '37:73 → 37:177', 'kural': "kök ipliği نذر [3/3] — 'el-munzarîn' iki kez (akıbet / sabah); okumada görüldü, KAPATILAMAZ", 'not': 'uyarılanlar.'},
 {'bag': '37:159 → 37:180', 'kural': "okuma — 'subhâne X ammâ yesifûn' iki kez (lafız / Rab tamlamaları); KAPATILAMAZ", 'not': 'tesbih.'},
 {'bag': '37:79 · 109 · 120 · 130 → 37:181', 'kural': 'okuma — selam formülü beşinci kez, adsız çoğulla; KAPATILAMAZ', 'not': 'gönderilenlere selam.'},
 {'bag': '1:2 → 37:182', 'kural': 'esit2 TAM — iki ucu okundu; sûrenin son ayeti', 'not': 'hamd âlemlerin Rabbi Allah\'adır.'},
 {'bag': '37:87 → 37:182', 'kural': "okuma — 'rabbi'l-âlemîn' İbrâhîm'in sorusunda / sûre sonunda; KAPATILAMAZ", 'not': 'âlemlerin Rabbi.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AV_saffat', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in SAFFAT]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AV_saffat'] = SAFFAT
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AV_saffat', len(SAFFAT), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AQ_saffat', len(BAGLAR['AQ_saffat']))

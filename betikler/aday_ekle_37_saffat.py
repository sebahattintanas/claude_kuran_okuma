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

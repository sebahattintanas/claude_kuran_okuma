_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_55_58.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'5:51', '5:55', '5:56', '5:57', '5:58', '5:5', '5:12', '5:23'}
D3DISI = ', '.join(sorted(_U - _BAG - _ON, key=lambda x: tuple(map(int, x.split(':')))))
ANILIS_ESKI = "5:51 kök ولي ('evliyâ'e' 8., 'evliyâ'u' 10., 'yetevellehum' 13. kelime — velîlik); 5:52 kök صبح ('fe-yusbihû' 22. kelime — 'ol-' anlamında), نفس ('enfusihim' 27. kelime — kendi, iç); 5:53 kök يمن ('eymânihim' 9. kelime — yemin), صبح ('fe-asbahû' 14. kelime — 'ol-' anlamında)"
ANILIS = 'YER'
ARAC = run('/home/claude/sunum/arac_degisim.py')
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; bölüm 6 ve 7 kurallarının araçları (bolum4 / bolum5 / bolum6 / bolum7_kurallar, mutasyon_sina — MUT_SONUC) koşuldu",
 "kök tablosu: ölçümde '???' 5:55-58 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 55 58 19'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:55:2 وَلِيّ 'ilahi' — 'innemâ veliyyukumu'llâh', kural ''innemâ' haberi lafız → ilahi' (elçi ve inananlar atıflı; ortak gönderge — tam okuma sonu); 5:57:18 وَلِيّ 'degil' — 'evliyâ'e', kural 'çoğul insan göndergeli → degil' (alay edenler ve kâfirler); "
 "5:57:23 مُؤْمِن 'degil' — 'mu'minîn', kural 'çoğul insan göndergeli → degil' (inananlar) (esma_el_ekle → esma_kayit; bölüm 6 kuralı 14 — betikle, sapma B6_ESMA); 5:56 ve 5:58 esmâ yok; lafız 5:55, 5:56 (2 geçiş), 5:57; 5:58 lafız yok; Rab yok",
 "esma_kayit: 5:55 'mühür hayır' (ölçüm MÜHÜRSÜZ — uyuşuyor), 5:56 'mühür hayır' (uyuşuyor), 5:57 'mühür EVET (ÇİFT)', ton cemâl — ölçüm 18. ve 23. sırada 'MÜHÜRSÜZ' yazıyor, el kararları 'degil' — uyuşmuyor, tam okuma sonu; 5:58 'mühür hayır' (sınıf 0/0; uyuşuyor)",
 "ölçüm: 5:55 '{{1|fâsıla ركعون → ن, N sınıfı}}', '{{1|harf 70 → harf3 68, isaret 2}}' ve '{{1|dış düğüm 2}}'; 5:56 '{{2|fâsıla ٱلغلبون → ن, N sınıfı}}', '{{2|simetri \\[3, 1, 7, 1\\]}}', '{{2|harf 50 → harf3 48, isaret 2}}' ve '{{2|dış düğüm 1}}'; "
 "5:57 '{{3|fâsıla مؤمنين → ن, N sınıfı}}', '{{3|harf 116 → harf3 108, isaret 8}}', '{{3|dış düğüm 3}}' ve '{{3|EDİLGEN 1/6 fiil, pas z=0,62}}'; 5:58 '{{4|fâsıla يعقلون → ن, N sınıfı}}', '{{4|simetri \\[3, 1, 9, 1\\]}}', '{{4|harf 58 → harf3 54, isaret 4}}' ve '{{4|dış düğüm 0}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 55 58 19'): KALAN_P",
 "ölçüm aktör: 5:55-58 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle): 5:55 haber, kip yok; 5:56 şart — COND 1 'men' (1.); 5:57 emir, yasak, nida, şart — VOC 1 'yâ' (1.), PRO 1 'lâ' (4.), IMPV 1 'ttequ' (19.), COND 1 'in' (21.), biçim DIKKAT + NEHY; 5:58 haber — NEG 1 'lâ' (11.)",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 5:56 ★★★ (kaynak allah, z=3,11); 5:55, 5:57 ve 5:58 yıldız yok",
 "fâsıla: 5:54 م (عليم) → 5:55 ن (ركعون) → 5:56 ن (الغلبون) → 5:57 ن (مؤمنين) → 5:58 ن (يعقلون); hepsi N sınıfı; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref: 5:55 5:56 (bu blokta) ve okunmuş başka ayetler; 5:56 5:55 (bu blokta) ve okunmuş başka ayet; 5:57 okunmuş ve henüz okunmamış ayetler; 5:58 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, joker '_' ile; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 7 kuralı 8: önek kesilmiş sayım ve şahıs / sayı farkı denetlendi): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:55 'qâme salât etâ zekât' ve 'allâh rasûl ellezî âmene' süzgeç GEÇER, 'ellezî âmene ellezî' GEÇMEZ; 5:56 'allâh rasûl ellezî âmene' GEÇER; 5:57 'min ellezî etâ kitâb min qabl', 'eyy ellezî âmene lâ ittexaze', 'ittekâ allâh in kâne mu'min', 'eyy ellezî âmene lâ', 'eyy ellezî âmene', 'ittekâ allâh in' ve 'in kâne mu'min' GEÇER; 5:58 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3 — ölçüt: 1P / 1S / 2MS / 2FS / 2MP / 2FP / 2D / 3MS / 3FS / 3D / 3MD / 3FD / 3MP / 3FP zamirlerin hepsi 'adsız', etiketin kendi parantezinde; etiket, kelimeyi anan alt maddede; adlı aktör ölçümün 'aktör: adlı' alanından): "
 "5:55 2MP (adsız — 'veliyyukumu'), 3MS (adsız — 'rasûluhû'), 3MP (adsız — 'âmenu', 'yuqîmûne', 'yu'tûne' failleri; 've hum'), Allah (lafız); 5:56 3MS (adsız — 'yetevelle' faili; 'rasûlehû'), 3MP (adsız — 'âmenû' faili; 'humu'), Allah (lafız), 'men'; "
 "5:57 3MP (adsız — 'âmenû', 'ttexazû' failleri; 'ûtu' naib-i faili), muhatap 2MP (adsız), Allah (lafız); 5:58 muhatap 2MP (adsız), 3MP (adsız — 'ttexazûhâ', 'ya'qilûn' failleri; 'bi-ennehum'), 3FS (adsız — 'ttexazûhâ' mef'ûlü) — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): blokta 'qâle' yok, söz aralığı yok (A3 —); 5:57 nida muhataba doğrudan; REM sapması (komut 'python3 sunum/bolum4_kurallar.py 55 58 19' — A3 aralığında morph REM): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:55 've rasûluhû' (4.), 've'llezîne' (5.), 've yu'tûne' (10.) CONJ, 've hum' (12.) CIRC; 5:56 've men' (1.) REM, 've rasûlehû' (4.), 've'llezîne' (5.) CONJ, 'fe-inne' (7.) RSLT; 5:57 've le'iben' (10.), 've'l-kuffâra' (17.) CONJ, 've'ttequ' (19.) REM; 5:58 've izâ' (1.) REM, 've le'iben' (7.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 5:55-58 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 55 58 19'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:55 (31:4), 5:56 (58:22), 5:58 (59:14) (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6); 5:57 D3 eşi yok; ayetler arası kalıp 'llâhu ve rasûluhû ve'llezîne âmenu' (5:55, 5:56) — sayım 'say 5:55 3-6'; ayetler arası kalıp 'huzuven ve le'iben' (5:57, 5:58) — sayım 'say 5:57 9-10'; "
 "ayetler arası kalıp 'yâ eyyuhe'llezîne âmenû lâ tettexizu' (5:51, 5:57) — sayım 'say 5:57 1-5'; ayetler arası kalıp 'mine'llezîne ûtu'l-kitâbe min qablikum' (5:5, 5:57) — sayım 'say 5:57 11-16'; ayetler arası kalıp 'qâme salât etâ zekât' (5:12, 5:55) — lemma dizisi 'dizi 5 55 8 11'; ayetler arası kalıp 'in kuntum mu'minîn' (5:23, 5:57) — sayım 'say 5:57 21-23'; bölüm içi ve sûre içi tekrar, ardışık bağ yerine sayımla kayıt; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7 — betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:55 edim geçişi nida, şart → haber; şahıs geçişi yok; 5:56 edim geçişi haber → şart; şahıs geçişi yok; şart → cevap (ayet içi; COND 'men' 1. kelime: 've men yetevelle'llâh' / 'fe-inne hizbe'llâhi humu'l-ğâlibûn' (7. kelime)); "
 "5:57 edim geçişi şart → emir, yasak, nida, şart; şahıs geçişi 3 → 2; şart → cevap (ayet içi; COND 'in' 21. kelime: 'in kuntum mu'minîn' / 've'ttequ'llâh' (19. kelime) — cevap öne alınmış); 5:58 edim geçişi emir, yasak, nida, şart → haber; şahıs geçişi 2 → 3",
 "sözdizimi (okuma; morph etiketiyle): 5:55 'innemâ' — sınırlama (morph ACC + PREV); 've hum râki'ûn' — hâl (morph CIRC); 5:56 've men yetevelle' — istînâf (morph REM) + şart (COND); 'fe-inne hizbe'llâh' — cevap (morph RSLT); 'humu'l-ğâlibûn' — ayırma zamiri (morph PRON, okuma); "
 "5:57 've'ttequ'llâh' — istînâf (morph REM) + emir (IMPV); 'in kuntum mu'minîn' — şart (COND), cevabı öncesinde; 5:58 've izâ' — istînâf (morph REM) + zaman (T); 'zâlike bi-ennehum' — sebep (morph P 'bi' + ACC 'enne', okuma)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:55 ve 5:56 'llâhu ve rasûluhû ve'llezîne âmenu' kalıbını paylaşıyor — velîliğin tanımı / velî edinmenin sonucu; 5:57 ve 5:58 'huzuven ve le'iben' — dini ve namazı alay ve oyun edinenler; "
 "5:57 'yâ eyyuhe'llezîne âmenû lâ tettexizu' ile açılıyor (5:51 ile eş açılış); 5:57 kök أخذ ikilemesi 'tettexizu' (muhatap, yasak) / 'ttexazû' (alay edenler); bölüm 8 'velî edinme' iki uçla: 5:51 yasak — 5:57 yasak, arada 5:55 velîlik tanımı",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 19'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + "'; çıktı aynen): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle): 'yuqîmûne's-salâte ve yu'tûne'z-zekâ' 5:55 'namazı kılarlar, zekâtı verirler' / 31:4 eş (emsal metninde) — tam okuma sonu; 'hizbe'llâh' 5:56 'Allah'ın hizbi' / 58:22 (emsal metninde) — tam okuma sonu; 'qavmun lâ ya'qilûn' 5:58 'akletmeyen bir kavim' / 59:14 'akıl etmeyen bir topluluk' — tam okuma sonu",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 55 58 19'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:55-58 tarayıcı adayı yok; L3 / L4 adayı yok",
 "aday 1039: blokta ayet içi ve ayetler arası karşıt çift kaydı yok; eşleme betikle: ADAY_P",
 "aday 1041: kök ولي 5:55 'veliyyukum' (Allah velî) / 5:56 'yetevelle' (velî edinme) / 5:57 'evliyâ'e' (yasaklanan velîler); kök أخذ 5:57-58 'ttexazû' — dini ve namazı alay edinme — okuma",
 "bölüm: " + BOL + " bölümü, bölüm 8-2 (bölüm 7 kuralı 9 — blok_plani_5.txt'ten) — bölüm iki blok (18, 19); bu blok bölümü kapatıyor; başlıktaki 'dinle alay edenler' 5:57-58 ('huzuven ve le'iben'); "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b19/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11 — betikle: komut 'python3 sunum/bolum5_kurallar.py 55 58 19'; lem_bozuk.py 19 çıktısı): 5:58:12 ''aqalu' — lem_bozuk bayrağı; meal maddesinde '(morph LEM ham biçim)' notlu; lemma adı listesinde notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 55 58 → AYN_SONUC; sunum/bolum4_kurallar.py 55 58 19 → KHATA_HEPSI; sunum/bolum5_kurallar.py 55 58 19 → B5_HEPSI; sunum/bolum6_kurallar.py 55 58 19 → B6_HEPSI; sunum/bolum7_kurallar.py 55 58 19 → B7_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (sunum/sonradan.py --plan 19): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('inne', 'mâ', 'veliyy', 'rasûl', 'ellezî', 'âmene', 'eqâme', 'salât', 'âtâ', 'zekât', 'râki'', 'men', 'tevellâ', 'hizb', 'ğâlib', 'eyy', 'ittexaze', 'dîn', 'huzuv', 'le'ib', 'kitâb', 'qabl', 'kâfir', 'ittekâ', 'kâne', 'mu'min', 'izâ', 'nâdâ', 'qavm', ''aqalu' (morph LEM ham biçim)); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

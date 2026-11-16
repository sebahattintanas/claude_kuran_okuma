_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_90_93.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'5:90', '5:91', '5:92', '5:93'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_90_93.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '5:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '5:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(90, 94))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "5:90 kök زلم ('l-ezlâmu' 8. kelime — fal okları) ve kök جنب ('fe'ctenibûhu' 13. kelime — kaçınma; kök anlamı 'yan, taraf'): tetik listesinde yok; 5:91 kök صدد ('yesuddekum' 12. kelime — alıkoyma): tetik listesinde yok; 5:92 kök ولي ('tevelleytum' 7. kelime — yüz çevirme): tetik listesinde yok; 5:93 'izâ' ('izâ me'ttaqav' 10. kelime — morph T, zaman şartı)"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '90', '93', '28')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b28/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 29)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b5:%d:\d+' % a_, s_) for a_ in range(90, 94))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: yalnız blok akışı (sunum/sinifla.py SON, sunum/basilan.txt — §3 adım 2 ve emsal işaretlemesi); denetim kuralı değişmedi; mutasyon_sina — MUT_SONUC; geriye dönük koşu son araç değişikliğinden sonra (blok 27) üretildi: GERI_P",
 "kök tablosu: ölçümde '???' 5:90, 5:91, 5:92 ve 5:93 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 90 93 28'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:92 'l-mubîn' (13. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (tebliğin sıfatı); 5:90, 5:91 ve 5:93 esmâ yok; lafız 5:91, 5:92 ve 5:93; 5:90 lafız yok; Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); "
 "gönderge tebliğ ('l-belâğu') — A1'de 'l-belâğu'l-mubîn' kaydında kural adıyla (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 90 93 28'): " + EMH,
 "ölçüm: 5:90 '{{1|fâsıla تفلحون → ن, N sınıfı}}', '{{1|harf 82 → harf3 80, isaret 2}}' ve '{{1|dış düğüm 0}}'; "
 "5:91 '{{2|fâsıla منتهون → ن, N sınıfı}}', '{{2|harf 91 → harf3 90, isaret 1}}', '{{2|dış düğüm 1}}' ve '{{2|İÇ düğüm 2}}'; "
 "5:92 '{{3|fâsıla ٱلمبين → ن, N sınıfı}}', '{{3|harf 76 → harf3 71, isaret 5}}', '{{3|dış düğüm 0}}' ve '{{3|esit2 → 64:12 oran 0,8960 kademe BENZER}}'; "
 "5:93 '{{4|fâsıla ٱلمحسنين → ن, N sınıfı}}', '{{4|simetri \\[6, 2, 11, 2\\]}}', '{{4|harf 127 → harf3 115, isaret 12}}', '{{4|dış düğüm 3}}' ve '{{4|İÇ düğüm 1}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 90 93 28'): KALAN_P",
 "ölçüm aktör: 5:90 '{{1|adlı شَيْطان 12\\. sırada \\(gayb, rol mecrur\\)}}' — ''ameli' muzâfun ileyhi; 5:91 '{{2|adlı شَيْطان 3\\. sırada \\(gayb, rol fail\\)}}' — 'yurîdu' faili; 5:92 ve 5:93 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 5:90 emir, nida — VOC 1 'yâ' (1.), IMPV 1 'ctenibûhu' (13.); ölçüm biçim alanı '{{1|biçim DIKKAT}}' (yalnız bu maddede); "
 "5:91 soru — INTG 1 'hel' (18.); 5:92 emir, şart — COND 1 'in' (6.), IMPV 4 'atî'u' (1., 3.), 'hzerû' (5.), ''lemû' (8.); 5:93 haber — kip yok; "
 "morph REM ('fe' 5:90 13., 5:91 18., 5:92 6.; 've' 5:93 22.), RSLT ('fe' 5:92 8.), PREV ('mâ' 5:90 4., 5:91 1., 5:92 9.) ve SUP ('mâ' 5:93 11.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): bu blokta yıldız yok (5:90, 5:91, 5:92 ve 5:93 'yıldız yok')",
 "fâsıla: 5:89 ن (تشكرون) → 5:90 ن (تفلحون) → 5:91 ن (منتهون) → 5:92 ن (ٱلمبين) → 5:93 ن (ٱلمحسنين); blok içi kafiye değişmiyor; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6 — basılmamış hedefler sinifla sayısıyla): 5:90 xref yok; 5:91 5:14 (emsal olarak basıldı) ve okunmuş 2 ayet; 5:92 xref yok (esit2 BENZER 64:12, emsal olarak basıldı); 5:93 3:134 (emsal olarak basıldı) ve okunmuş 3 ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:90 'eyy ellezî âmene' süzgeç GEÇER; 5:91 'beyn 'adâve bağdâ'' GEÇER; 5:92 'fe-in tevellâ 'alime enne' GEÇER; 5:93 'ellezî âmene 'amile sâliha' GEÇER, 'allâh ahbeb muhsin' GEÇMEZ",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap' ile; alıntı ve kelime numarası ◇ konumuyla eş; fail olmayan mecrur çoğul ad ve mecrur ilgi zamiri A1'de yazılmaz — bölüm 11 denetimi kuralları 16 ve 19): "
 "5:90 hitap ('yâ eyyuhe'llezîne âmenû'), 3MP (adsız — 'âmenû'), şeytan (adlı gayb; mecrur), muhatap 2MP (adsız), 3MS (adsız — 'fe'ctenibûhu' mef'ûlü); "
 "5:91 şeytan (adlı gayb; 'yurîdu' faili — 3MS fiil uyumu), 3MS (adsız — 'yûqi'a', 'yesuddekum'), muhatap 2MP (adsız), Allah (lafız; mecrur), 'muntehûn' ('entum' haberi); "
 "5:92 muhatap 2MP (adsız), Allah (lafız), 'r-rasûle', 1P (adsız — 'rasûlina' iyelik, konuşan), 'l-belâğu'l-mubîn' ('enne' ismi); "
 "5:93 'leyse' (3MS fiil uyumu; ismi 'cunâhun'), 3MP (adsız — sekiz fiilin faili), Allah (lafız; 'yuhibbu' faili), 'l-muhsinîn' ('yuhibbu' mef'ûlü); "
 "5:93 ''ale'llezîne âmenû' — mecrur ilgi zamiri (''alâ' + 'ellezî' + ilgi cümlesi; §8, karar tam okuma sonunda) A1'de yazılmadı — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): bu blokta söz yok (A3 —); 'qul' yok (bölüm 10 denetimi kuralı 8); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 90 93 28' — A3 aralığında morph REM): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:90 've'l-meysiru' (6.), 've'l-ensâbu' (7.), 've'l-ezlâmu' (8.) CONJ, 'fe'ctenibûhu' (13.) REM; 5:91 've'l-bağdâ'e' (8.), 've'l-meysiri' (11.), 've yesuddekum' (12.), 've 'ani's-salâti' (16.) CONJ, 'fe-hel' (18.) REM; "
 "5:92 've atî'u' (1., 3.), 've'hzerû' (5.) CONJ, 'fe-in' (6.) REM, 'fe'lemû' (8.) RSLT; 5:93 5., 13., 14., 18. ve 21. kelimedeki 've' CONJ, 've'llâhu' (22.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): bu blokta tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 90 93 28'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:90 (2:219), 5:92 (64:12), 5:93 (3:134) (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); 5:91 D3 eşi yok; "
 "ayetler arası kalıp 'l-xamr… ve'l-meysir' (5:90, 5:91) — sayım 'say 5:90 5-6 --on' ve lemma dizisi 'dizi 5 90 5 6' / 'dizi 5 91 10 11'; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:90 hitap açılır; edim geçişi emir, şart → emir, nida; 5:91 edim geçişi emir, nida → soru; şahıs geçişi 2 → 3; 5:92 edim geçişi soru → emir, şart; şahıs geçişi 3 → 2; şart → cevap ('in' 6. kelime); "
 "5:93 bölüm kapanışı (bölüm 10 denetimi kuralı 2); edim geçişi emir, şart → haber; şahıs geçişi 2 → 3",
 "sözdizimi (okuma; morph etiketiyle): 5:90 'innemâ'l-xamru … ricsun' — hasr (morph ACC + PREV), mübteda dizisi ve haber; 'ctenibûhu' — emir (morph IMPV); 'le'allekum tuflihûn' — umut (morph ACC); "
 "5:91 'innemâ yurîdu'ş-şeytânu en yûqi'a' — hasr ve 'en' masdar (morph SUB); 'yesuddekum' — 'yûqi'a' üzerine atıf (morph CONJ); 'hel entum muntehûn' — soru (morph INTG); "
 "5:92 'in tevelleytum … 'lemû' — şart (morph COND) ve cevap (morph RSLT önekli); 'ennemâ 'alâ rasûlina'l-belâğu' — hasr (morph ACC + PREV); "
 "5:93 'leyse … cunâhun' — 'leyse' ve ismi; 'izâ me'ttaqav' — zaman şartı (morph T + SUP); 'summe' ile sıralı tekrar (morph CONJ); 've'llâhu yuhibbu'l-muhsinîn' — istînâf (morph REM)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:90 'yâ eyyuhe'llezîne âmenû' ile açılıyor; "
 "5:90 ve 5:91'de 'l-xamr… ve'l-meysir' (5:90 5-6., 5:91 10-11. kelime); 5:93 kök وقي ikilemesi 'ttaqav' (12., 17., 20. kelime), kök أمن ikilemesi 'âmenû' (4., 13., 18. kelime); 5:92 kök طوع ikilemesi 'atî'u' (1., 3. kelime)",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 28'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp): 'l-xamru ve'l-meysir' 5:90 'İçki, kumar' / 2:219 'içkiyi ve kumarı' (emsal metninde) — çakışma değil; "
 "'ve atî'u'llâhe ve atî'u'r-rasûl' 5:92 'Allah'a itaat edin, elçiye itaat edin' / 64:12 (emsal metninde) — meal birebir; 'ennemâ 'alâ rasûlina'l-belâğu'l-mubîn' 5:92 'açık tebliğ' / 64:12 'apaçık tebliğ' — karşılık farkı (tam okuma sonu); "
 "'ve'llâhu yuhibbu'l-muhsinîn' 5:93 / 3:134 'Allah iyilik edenleri sever' (emsal metninde) — çakışma değil",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 90 93 28'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:90, 5:91, 5:92 ve 5:93 tarayıcı vermedi (cipa_tarama5_adaylari.json); doğa iddiası yok (olgu=False); L3 / L4 adayı yok",
 "aday 1039: ayet içi 5:92 ('atî'u'llâhe' / 'tevelleytum') — okuma; 5:90, 5:91 ve 5:93 ayet içi karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök خمر ve يسر 5:90 ve 5:91'de ('l-xamr… ve'l-meysir' — yasak ve gerekçe); kök وقي 5:93'te üç kelimede sıralı ('ttaqav' 12., 17., 20. kelime); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 12-2 (bölüm 7 kuralı 9 — blok_plani_5.txt'ten) — bölüm iki blok (27, 28); bu blok bölümü kapatıyor; başlıktaki 'içki ve kumar' 5:90 ve 5:91; "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b28/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 90 93 28'; lem_bozuk.py 28 çıktısı): 5:90:13 'ctenebu', 5:91:5 'yûqi'a', 5:92:5 'yahzeru', 5:93:9 'ta'imu', 5:93:23 'ahbeb' — lem_bozuk bayrağı; meal maddesinde '(morph LEM ham biçim)' notlu; lemma adı listesinde notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 90 93 → AYN_SONUC; sunum/bolum4_kurallar.py 90 93 28 → KHATA_HEPSI; sunum/bolum5_kurallar.py 90 93 28 → B5_HEPSI; sunum/bolum6_kurallar.py 90 93 28 → B6_HEPSI; sunum/bolum7_kurallar.py 90 93 28 → B7_HEPSI; sunum/bolum8_kurallar.py 90 93 28 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 90 93 28 → B9_HEPSI; sunum/bolum10_kurallar.py 90 93 28 → B10_HEPSI; sunum/bolum11_kurallar.py 90 93 28 → B11_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 28 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('eyy', 'ellezî', 'âmene', 'xamr', 'meysir', 'beyn', ''adâve', 'bağdâ'', 'fe-in', 'tevellâ', ''alime', 'enne', ''amile', 'sâliha', 'allâh', 'ahbeb' (morph LEM ham biçim), 'muhsin'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_82_86.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'5:82', '5:83', '5:84', '5:85', '5:86'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_82_86.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '5:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '5:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(82, 87))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "5:83 'izâ' ('ve izâ' 1. kelime — morph T, zaman); 5:83 kök رأي ('terâ' 7. kelime — görme) ve kök دمع ('d-dem'i' 11. kelime — gözyaşı): tetik listesinde yok; 5:85 kök جنن ('cennâtin' 5. kelime — cennet) ve kök تحت ('tahtihe' 8. kelime — alt): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '82', '86', '26')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b26/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 27)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b5:%d:\d+' % a_, s_) for a_ in range(82, 87))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: sunum/ham_elle.txt — 5:84 'yudxilenâ' (12. kelime) LEM 'udxile' (morph LEM ham biçim), edilgen görünümlü, lem_bozuk.py bayraklamıyor, elle listeye eklendi (bölüm 5 kuralı 5); "
 "sunum/bolum10_kurallar.py kural 6 — ölçüm xref alanında ' · ' ile ayrılmış sonraki kalıpların hedefleri okunmuyordu (5:83'te iki kalıp; düzeltme sonrası 'okunmuş 3 ayet'), sunum/mutasyon_sina.py bu düzeltmenin sınaması (5:83) ve 5:77 sınamasının beklenen sayısının düzeltmeyle güncellenmesi ('okunmuş 8 ayet'); sunum/sinifla.py SON ve sunum/basilan.txt blok akışı (§3 adım 2 ve emsal işaretlemesi); mutasyon_sina — MUT_SONUC; geriye dönük koşu son araç değişikliğinden sonra yeniden üretildi (GERI_P) — yeni 30 — bolum10_kurallar 22 (kural 6 düzeltmesi: okunmuş bloklarda xref alanının sonraki kalıp hedefleri eski kayıtlarda sayılmamıştı), bolum5_kurallar 3 (sunum/ham_elle.txt'e 'udxile' eklenmesi: eski kayıtlarda bu LEM notsuz), bolum9_kurallar 4 (sonradan basılan 5:14, 5:82 ve 5:84 r5_gerekce çıktısını değiştirdi), gloss_tara KAPSAMAYAN 1 (bu bloğun satırı, tam okuma sonu); düşen 12 — araç değişti; kayıtlar geriye dönük yeniden yazılmadı",
 "kök tablosu: ölçümde '???' 5:82 için 2 (HAPAKS alanı ve kökler alanı; kök قسس — 22. kelime 'qissîsîne') — kök tabloya eklendi (yamalar/yama_kok_5_82.py → kok_ekle_5.py; anlam 'keşiş, rahip; kıssîs'; 1 ayet; docstring dosya adı ve bölümle — bölüm 4 kuralı 16), ölçüm yeniden alındı, '???' 0; 5:83, 5:84, 5:85 ve 5:86 '???' 0; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 82 86 26'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: bu blokta esmâ yok (5:82, 5:83, 5:84, 5:85 ve 5:86); lafız 5:84 ve 5:85; Rab 5:83 ve 5:84; 5:82 ve 5:86 lafız yok, Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 82 86 26'): " + EMH,
 "ölçüm: 5:82 '{{1|HAPAKS: قسس}}', '{{1|hapaks z=3,28}}', '{{1|fâsıla يستكبرون → ن, N sınıfı}}', '{{1|simetri \\[3, 5, 13, 1\\]}}', '{{1|harf 138 → harf3 128, isaret 10}}' ve '{{1|dış düğüm 0}}'; "
 "5:83 '{{2|fâsıla ٱلشهدين → ن, N sınıfı}}', '{{2|EDİLGEN 1/8 fiil, pas z=0,38}}', '{{2|simetri \\[3, 1, 10, 1\\]}}', '{{2|harf 92 → harf3 89, isaret 3}}' ve '{{2|dış düğüm 3}}'; "
 "5:84 '{{3|fâsıla ٱلصلحين → ن, N sınıfı}}', '{{3|simetri \\[3, 1, 6, 1\\]}}', '{{3|harf 62 → harf3 62, isaret 0}}' ve '{{3|dış düğüm 0}}'; "
 "5:85 '{{4|fâsıla ٱلمحسنين → ن, N sınıfı}}', '{{4|harf 66 → harf3 63, isaret 3}}' ve '{{4|dış düğüm 1}}'; "
 "5:86 '{{5|fâsıla ٱلجحيم → م, N sınıfı}}', '{{5|harf 42 → harf3 39, isaret 3}}', '{{5|dış düğüm 1}}', '{{5|nakarat 2 \\(temsil \\[5, 10\\]\\)}}' ve '{{5|esit2 → 5:10 oran 1,0000 kademe TAM}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 82 86 26'): KALAN_P",
 "ölçüm aktör: 5:82 '{{1|adlı يَهُود 7\\. sırada \\(cins, rol meful\\)}}' — 'tecidenne' 2. mef'ûlü, '{{1|adlı نَصْرانِيّ 18\\. sırada \\(cins, rol fail\\)}}' — söz içi 'innâ' haberi (ölçüm rolü 'fail'; araç tanımı farkı, okuma); 5:83, 5:84, 5:85 ve 5:86 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 5:82 haber — EMPH 4 'le' ve 'nne' (1. ve 10.), NEG 1 'lâ' (25.); 5:83 emir — IMPV 1 'ktubnâ' (19.); 5:84 soru — INTG 1 'mâ' (1.), NEG 1 'lâ' (3.); 5:85 haber — kip yok; 5:86 haber — kip yok; "
 "morph REM ('fe' 5:83 19.; 've' 5:84 1., 5:85 12., 5:86 1.), CIRC ('ve natma'u' 5:84 10.) ve CAUS ('fe-esâbehumu' 5:85 1.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 5:82 ★★★ (kaynak hapaks, z=3,28); 5:83, 5:84, 5:85 ve 5:86 yıldız yok",
 "fâsıla: 5:82 ن (يستكبرون) → 5:83 ن (ٱلشهدين) → 5:84 ن (ٱلصلحين) → 5:85 ن (ٱلمحسنين) → 5:86 م (ٱلجحيم); bölüm kapanışında kafiye م'ye kırılıyor (5:86, 5:10 ile eş kapanış); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6 — basılmamış hedefler sinifla sayısıyla): 5:82 xref yok (bağ yalnız nakarat3); 5:83 okunmuş 3 ayet (iki xref kalıbı); 5:84 xref yok; 5:85 okunmuş 1 ayet; 5:86 5:10 (emsal olarak basıldı) ve okunmuş 1 ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, joker '_' ile; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:82 'ellezî qâle inne nasrânî' süzgeç GEÇER; 5:83 nakarat3 yok; 5:84 'mâ câ'e min', 'câ'e min haqq' ve 'âmene allâh mâ' GEÇMEZ; 5:85 'cenne cerey min taht neher xâlid fî' ve 'cenne cerey min taht neher' GEÇER; 5:86 'ellezî kefera kezzebe âye _ ashâb cahîm' GEÇER (tür tam — R5 satırı yok, R5 yalnız 'tür ic'; 5:10 emsal olarak basıldı, kalıp eşi bag'de)",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap' ile; alıntı ve kelime numarası ◇ konumuyla eş): "
 "5:82 muhatap 2MS (adsız — 'tecidenne' 1. ve 10. kelime), 3MP (adsız — 'âmenu', 'eşrakû', 'qâlû', 'yestekbirûn' failleri; 'aqrabehum', 'minhum', 'ennehum'), Yahudiler (adlı cins), söz içi konuşan 1P (adsız — 'innâ'), Nasârâ (adlı cins); "
 "5:83 3MP (adsız — 'semi'û', ''arafû', 'yeqûlûne' failleri; 'a'yunehum'), 'unzile' (3MS edilgen; naib-i fail mevsûl), muhatap 2MS (adsız — 'terâ'), 'tefîdu' (3FS, adsız), söz içi Rab, söz içi konuşan 1P (adsız) ve muhatap 2MS (adsız — 'fe'ktubnâ'); "
 "5:84 söz içi konuşan 1P (adsız), Allah (lafız), 'câ'enâ' (3MS, adsız), Rab ('yudxilenâ' faili — 3MS fiil uyumu); "
 "5:85 Allah (lafız; 'esâbe' faili — 3MS fiil uyumu), 3MP (adsız — 'esâbehumu' mef'ûlü, 'qâlû' faili), 'l-enhâru' ('tecrî' faili — 3FS fiil uyumu), 3FS (adsız — 'tahtihe', 'fîhâ'); "
 "5:86 3MP (adsız — 'keferû', 'kezzebû' failleri), 1P (adsız — 'âyâtinâ'), 'ulâ'ike' (işaret) — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): 5:82 'qâlû innâ nasârâ' — söz içi 'innâ nasârâ' (17-18. kelime), mealde tırnak, ayet içinde açılıp kapanıyor; "
 "5:83 'yeqûlûne rabbenâ âmennâ' — söz 17. kelimede açılıyor, 5:84 sonunda kapanıyor (5:83 A3 '5:84 sonuna dek', 5:84 A3 'söz sürüyor'; mealde tırnak 5:83'te açılır, 5:84'te kapanır); 'qul' yok (bölüm 10 denetimi kuralı 8); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 82 86 26' — A3 aralığında morph REM): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:82 've'llezîne' (8.), 've le-tecidenne' (10.), 've ruhbânen' (23.), 've ennehum' (24.) CONJ; 5:83 've izâ' (1.) CONJ, 'fe'ktubnâ' (19.) REM; 5:84 've mâ lenâ' (1.) REM, 've mâ câ'enâ' (6.) CONJ, 've natma'u' (10.) CIRC; 5:85 'fe-esâbehumu' (1.) CAUS, 've zâlike' (12.) REM; 5:86 've'llezîne' (1.) REM, 've kezzebû' (3.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 5:82 ◈B أنس ('n-nâsi' 3. kelime — B1; anlam notu: düşmanlığı ölçülen insanlar); 5:83 ◈B سمع ('semi'û' 2. kelime — B3; anlam notu: indirileni işitme); 5:83 ◈B عين ('a'yunehum' 8. kelime — B3; anlam notu: yaşla taşan gözler); 5:85 ◈K نهر ('l-enhâru' 9. kelime — K1; anlam notu: cennetlerin altından akan ırmaklar); 5:84 ve 5:86 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 82 86 26'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:82 (5:14), 5:83 (3:53), 5:86 (5:10) (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); 5:84 ve 5:85 D3 eşi yok; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:82 edim geçişi şart → haber; şahıs geçişi yok; söz açılır / söz kapanır (ayet içi); 5:83 edim geçişi haber → emir; söz açılır (17. kelime); 5:84 edim geçişi emir → soru; şahıs geçişi 3 → 1; söz kapanır; "
 "5:85 edim geçişi soru → haber; şahıs geçişi 1 → 3; 5:86 bölüm kapanışı (bölüm 10 denetimi kuralı 2); edim geçişi yok (haber → haber); şahıs geçişi yok",
 "sözdizimi (okuma; morph etiketiyle): 5:82 'le-tecidenne … le-tecidenne' — kasem cevabı tekidi (morph EMPH 'le' + 'nne'); 'eşedde'n-nâsi 'adâveten' ve 'aqrabehum meveddeten' — ism-i tafdîl + temyiz; 'zâlike bi-enne minhum qissîsîne ve ruhbânen' — 'enne' ismi muahhar, haber 'minhum' (morph ACC); "
 "5:83 'izâ semi'û … terâ' — zaman şartı ve cevabı ('izâ' morph T, ölçüm edim alanında şart yok); 'yeqûlûne' — muzâri söz fiili; 'ktubnâ' — dua emri (morph IMPV); "
 "5:84 'mâ lenâ lâ nu'minu' — soru ve olumsuz muzâri (morph INTG + NEG); 'natma'u en yudxilenâ' — hâl (morph CIRC), 'en' masdar (morph SUB); "
 "5:85 'fe-esâbehumu'llâhu bi-mâ qâlû' — sebep (morph CAUS), 'mâ' masdar; 'xâlidîne fîhâ' — mansub çoğul etken ortaç (morph ACC); 've zâlike cezâ'u'l-muhsinîn' — istînâf (morph REM); "
 "5:86 've'llezîne keferû … ulâ'ike ashâbu'l-cahîm' — mübteda ve işaretle başlayan haber cümlesi (morph REM)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:82 kök وجد ikilemesi 'tecidenne' (1., 10. kelime) ve kök أمن ikilemesi 'âmenu' (6., 14. kelime); "
 "5:82 'le-tecidenne' ile açılıyor; 5:83 ve 5:84'te söz içi 'rabbenâ' / 'rabbunâ' (17. ve 13. kelime); 5:83 'mine'l-haqqi' (14-15. kelime) ve 5:84 'mine'l-haqqi' (8-9. kelime)",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 26'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp): 'llezîne qâlû innâ nasârâ' 5:82 ''Biz Nasârâ'yız' diyenler' / 5:14 ''Biz Nasârâ'yız' diyenler' (emsal metninde) — çakışma değil; "
 "'fe'ktubnâ ma'a'ş-şâhidîn' 5:83 'bizi şahitlerle birlikte yaz' / 3:53 'bizi şahitlerle birlikte yaz' (emsal metninde) — çakışma değil; 'rabbenâ âmennâ' 5:83 'Rabbimiz, iman ettik' / 3:53 'Rabbimiz, … inandık' — karşılık farkı (tam okuma sonu; 'âmene' kararı meal karşılık farkı maddesinde); "
 "'ve'llezîne keferû ve kezzebû bi-âyâtinâ ulâ'ike ashâbu'l-cahîm' 5:86 / 5:10 (emsal metninde) — meal birebir, çakışma değil; 'qissîs' karşılığı 'keşiş', 'ruhbân' karşılığı 'rahip' (kök رهب tablo anlamı 'korku, çekinme' — gloss taraması KAPSAMAYAN listesinde)",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük): " + (MKK or 'yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 82 86 26'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:82, 5:83, 5:84, 5:85 ve 5:86 tarayıcı vermedi (cipa_tarama5_adaylari.json); doğa iddiası yok (olgu=False); L3 / L4 adayı yok",
 "aday 1039: ayet içi 5:82 ('eşedde'n-nâsi 'adâveten' / 'aqrabehum meveddeten') — okuma; ayetler arası 5:85 / 5:86 ('cennâtin' / 'ashâbu'l-cahîm'); 5:83, 5:84, 5:85 ve 5:86 ayet içi karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök وجد 5:82 'tecidenne' (1. ve 10. kelime) — düşmanlık ve sevgi karşıtlığında bir fiil; kök حقق 5:83 ve 5:84 'mine'l-haqqi' — tanınan hak / gelen hak; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 11-2 (bölüm 7 kuralı 9 — blok_plani_5.txt'ten) — bölüm iki blok (25, 26); bu blok bölümü kapatıyor; başlıktaki 'Nasârâ'nın yakınlığı' 5:82, 'gözyaşı dökenler' 5:83; "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b26/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9 — betikle: komut 'python3 sunum/bolum5_kurallar.py 82 86 26'; lem_bozuk.py 26 çıktısı): 5:83:9 'tefîdu', 5:84:10 'yatma'u', 5:85:6 'cerey' — lem_bozuk bayrağı; 5:84:12 'udxile' (sunum/ham_elle.txt) — elle ham listesi; meal maddesinde '(morph LEM ham biçim)' notlu; lemma adı listesinde notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 82 86 → AYN_SONUC; sunum/bolum4_kurallar.py 82 86 26 → KHATA_HEPSI; sunum/bolum5_kurallar.py 82 86 26 → B5_HEPSI; sunum/bolum6_kurallar.py 82 86 26 → B6_HEPSI; sunum/bolum7_kurallar.py 82 86 26 → B7_HEPSI; sunum/bolum8_kurallar.py 82 86 26 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 82 86 26 → B9_HEPSI; sunum/bolum10_kurallar.py 82 86 26 → B10_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 26 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('ellezî', 'qâle', 'inne', 'nasrânî', ''ayn', 'tefîdu' (morph LEM ham biçim), 'min', 'dem'', 'rabb', 'âmene', 'mâ', 'câ'e', 'haqq', 'allâh', 'cenne', 'cerey' (morph LEM ham biçim), 'taht', 'neher', 'xâlid', 'fî', 'kefera', 'kezzebe', 'âye', 'ashâb', 'cahîm'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_64_66.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'5:64', '5:65', '5:66'}
D3DISI = ', '.join(sorted(_U - _BAG - _ON, key=lambda x: tuple(map(int, x.split(':')))))
ANILIS = "5:64 kök غلل ('mağlûle' 5. kelime — bağlı, 'ğullet' 6. kelime — bağlan-); 5:64 'kullemâ' (34. kelime — morph T, zaman şartı; kök كلل); 5:65 kök سوأ ('seyyi'âtihim' 9. kelime — kötülük); 5:66 kök رجل ('ercülihim' 16. kelime — ayak); 5:66 kök سوأ ('sâ'e' 22. kelime — ne kötü)"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '64', '66', '21')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b21/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 22)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b5:%d:\d+' % a_, s_) for a_ in range(64, 67))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; bu blokta: sunum/bolum7_kurallar.py kural 4 (tetik kapsamında S1 lemma kısıtı — calisma/oturum_tetik_s1.py, oturum_tetik.py ile eş; 5:65 'na'îm' kök نعم S1 izinli lemma değil), sunum/bolum5_kurallar.py kural 5 (edat LEM adı — 'bel' — zayıf harf eşlemesiyle ham fiil LEM'ine bağlanmıyor)",
 "kök tablosu: ölçümde '???' 5:64-66 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 64 66 21'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:64-66 esmâ yok; esma_el kaydı yok; lafız 5:64 (3 geçiş); 5:65 ve 5:66 lafız yok; Rab 5:64 ('rabbike', 24. sırada) ve 5:66 ('rabbihim', 10. sırada) — Rab adı (bölüm 6 kuralı 14 — betikle: B6_ESMA)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 64 66 21'): " + EMH,
 "ölçüm: 5:64 '{{1|fâsıla ٱلمفسدين → ن, N sınıfı}}', '{{1|EDİLGEN 3/13 fiil, pas z=0,99}}', '{{1|simetri \\[3, 1, 10, 1\\]}}', '{{1|harf 230 → harf3 215, isaret 15}}' ve '{{1|dış düğüm 2}}'; "
 "5:65 '{{2|fâsıla ٱلنعيم → م, N sınıfı}}', '{{2|harf 62 → harf3 60, isaret 2}}' ve '{{2|dış düğüm 4}}'; 5:66 '{{3|fâsıla يعملون → ن, N sınıfı}}', '{{3|EDİLGEN 1/5 fiil, pas z=0,81}}', '{{3|simetri \\[4, 1, 5, 1\\]}}', '{{3|harf 111 → harf3 104, isaret 7}}' ve '{{3|dış düğüm 2}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 64 66 21'): KALAN_P",
 "ölçüm aktör: 5:64 '{{1|adlı يَهُود 2\\. sırada \\(cins, rol fail\\+konusan\\)}}' — sözdiziminde 'qâlet' faili ve sözün sahibi; 5:66 '{{3|adlı تَوْراة 4\\. sırada \\(kitab, rol meful\\)}}', '{{3|adlı إِنجِيل 5\\. sırada \\(kitab, rol meful\\)}}' — 'eqâmû' mef'ûlleri; 5:65 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle): 5:64 haber — EMPH 2 'le' ve te'kid nûnu (17.), NEG 1 'lâ' (45.), biçim IDRAB 'bel' (11.); 5:65 şart — COND 1 'lev' (1.), EMPH 2 'le' (7., 10.); 5:66 şart — COND 1 'lev' (1.), EMPH 1 'le' (11.); morph T 'kullemâ' (5:64 34.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 5:64 ★★★ (kaynak n, z=3,67); 5:65 ve 5:66 yıldız yok",
 "fâsıla: 5:63 ن (يصنعون) → 5:64 ن (المفسدين) → 5:65 م (النعيم; N sınıfı) → 5:66 ن (يعملون); kafiye kırığı yok; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref: 5:64 28:77 (emsal olarak basıldı), 5:14 ve 60:4 (basılmış) ve okunmuş ve henüz okunmamış başka ayetler; 5:65 70:38 (emsal olarak basıldı) ve okunmuş başka ayetler; 5:66 29:55 (emsal olarak basıldı) ve okunmuş başka ayetler",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, joker '_' ile; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:64 'zâde kesîr min mâ enzele ilâ min rabb tuğyân kufr', 'beyn 'adâve bağdâ' ilâ yevm qiyâme', 'mâ enzele ilâ min rabb', 'se'â fî ard fesâd' ve 'beyn 'adâve bağdâ'' süzgeç GEÇER, 'allâh lâ ahbeb' GEÇMEZ; "
 "5:65 'seyyi'e udxile cenne' GEÇMEZ; 5:66 'eqâme tevrâ incîl mâ enzele' GEÇER",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap' ile; alıntı ve kelime numarası ◇ konumuyla eş): "
 "5:64 Yahudiler (adlı cins — 'qâlet' faili), Allah (lafız), 3MP (adsız — 'eydîhim', 'lu'inû', 'qâlû', 'minhum', 'beynehumu', 'evqadû', 'yes'avne'), 3MS (adsız — 'yedâhu', 'yunfiqu', 'yeşâ'u'; 'unzile' naib-i faili), muhatap 2MS (adsız), Rab, konuşan 1P (adsız — 'elqaynâ'), 3FS (adsız — 'atfa'ehâ'); "
 "5:65 Kitap ehli ('âmenû' faili), 3MP (adsız — 'âmenû', 'tteqav' failleri; ''anhum', 'seyyi'âtihim', 'edxalnâhum' mef'ûlü), konuşan 1P (adsız — 'keffernâ', 'edxalnâhum'); "
 "5:66 3MP (adsız — 'ennehum', 'eqâmu', 'ekelû', 'ya'melûn'; 'ileyhim', 'fevqihim', 'ercülihim', 'minhum'), Tevrat ve İncil (adlı kitaplar), 3MS (adsız — 'unzile' naib-i faili, 'sâ'e' faili), Rab, 'ummetun' — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): 5:64 'qâlet' sözü 'yedu'llâhi mağlûle' (A3, 3-5. kelime); 5:65 ve 5:66 söz yok; REM sapması (komut 'python3 sunum/bolum4_kurallar.py 64 66 21' — A3 aralığında morph REM): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:64 've qâleti' (1.), 've le-yezîdenne' (17.), 've elqaynâ' (27.), 've yes'avne' (40.), 've'llâhu' (44.) REM; 've lu'inû' (8.), 've kufran' (26.), 've'l-bağdâ'e' (30.) CONJ; 5:65 've lev' (1.) REM; 've'tteqav' (6.), 've le-edxalnâhum' (10.) CONJ; "
 "5:66 've lev' (1.) REM; 've'l-incîle' (5.), 've mâ' (6.), 've min' (14.), 've kesîrun' (20.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 5:64 ◈K أرض ('l-ardi' 42. kelime — K1; anlam notu: bozgunculuk için koşulan yer); 5:64 ◈K يوم ('yevmi' 32. kelime — K2; anlam notu: 'yevmi'l-qiyâme' — düşmanlığın süresi); 5:64 ◈B يدي ('yedu' 3. kelime, 'eydîhim' 7. kelime, 'yedâhu' 12. kelime — B3; anlam notu: bağlı el sözü ve açık el karşılığı); 5:65 ve 5:66 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 64 66 21'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:64 (28:77), 5:65 (70:38), 5:66 (29:55) (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7 — betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:64 edim geçişi yok (haber); şahıs geçişi yok; 5:65 edim geçişi haber → şart; şahıs geçişi yok; 5:66 edim geçişi yok (şart); şahıs geçişi yok",
 "sözdizimi (okuma; morph etiketiyle): 5:64 'bel yedâhu' — ıdrâb (morph RET); 'le-yezîdenne' — te'kid (morph EMPH); 'kullemâ evqadû' — zaman şartı (morph T); 've'llâhu lâ yuhibbu' — istînâf (morph REM + NEG); "
 "5:65 'lev enne' — şart (morph COND + ACC); 'le-keffernâ' — şart cevabı (morph EMPH); 5:66 'lev ennehum' — şart (morph COND + ACC); 'le-ekelû' — şart cevabı (morph EMPH); 'minhum ummetun' — haberi öne alınmış isim cümlesi (okuma)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:64 've qâleti'l-yehûdu' ile açılıyor — söz aktarımı; kök يدي ikilemesi 'yedu' / 'eydîhim' / 'yedâhu' ve kök غلل ikilemesi 'mağlûle' / 'ğullet' — sözün karşılığı eş kökle; "
 "kök فسد ikilemesi 'fesâden' / 'l-mufsidîn'; 5:65 ve 5:66 've lev' ile açılıyor — şart ve 'le' cevabı",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 21'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + "'; çıktı aynen): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle): 'lâ yuhibbu'l-mufsidîn' 5:64 'bozguncuları sevmez' / 28:77 'bozguncuları sevmez' (emsal metninde) — çakışma değil; 'cennâti'n-na'îm' 5:65 'nimet cennetleri' / 70:38 'nimet cenneti' — çakışma değil; "
 "'min fevqihim ve min tahti ercülihim' 5:66 'üstlerinden ve ayaklarının altından' / 29:55 'üstlerinden ve ayaklarının altından' — çakışma değil",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle): " + (MKK or 'yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 64 66 21'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:64-66 tarayıcı adayı yok; L3 / L4 adayı yok",
 "aday 1039: 5:64 ('yedu'llâhi mağlûle' / 'yedâhu mebsûtatân'); 5:66 ('min fevqihim' / 'min tahti ercülihim'; 'ummetun muqtaside' / 'kesîrun minhum sâ'e'); ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök غلل 5:64 'mağlûle' (söz) / 'ğullet' (karşılık); kök فسد 5:64 'fesâden' / 'l-mufsidîn'; kök نزل 5:64 ve 5:66 'mâ unzile ... min rabb' — okuma",
 "bölüm: " + BOL + " bölümü, bölüm 9-2 (bölüm 7 kuralı 9 — blok_plani_5.txt'ten) — bölüm iki blok (20, 21); bu blok bölümü kapatıyor; başlıktaki 'bağlı el sözü' 5:64, 'Tevrat ve İncil'i ayakta tutma' 5:66; "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b21/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9 — betikle: komut 'python3 sunum/bolum5_kurallar.py 64 66 21'; lem_bozuk.py 21 çıktısı): 5:64:35 'evqadu', 5:64:46 'ahbeb' — lem_bozuk bayrağı; meal maddesinde '(morph LEM ham biçim)' notlu; lemma adı listesinde notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 64 66 → AYN_SONUC; sunum/bolum4_kurallar.py 64 66 21 → KHATA_HEPSI; sunum/bolum5_kurallar.py 64 66 21 → B5_HEPSI; sunum/bolum6_kurallar.py 64 66 21 → B6_HEPSI; sunum/bolum7_kurallar.py 64 66 21 → B7_HEPSI; sunum/bolum8_kurallar.py 64 66 21 → B8_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta 'bozguncu' eklendi (fâil adı, sıra sayısı eki değil)",
 "sonradan basılan (sunum/sonradan.py --plan 21): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('qâle', 'yehûd', 'yed', 'allâh', 'mağlûle', 'ğalle', 'le'ane', 'mâ', 'bel', 'mebsûtatân', 'enfeqa', 'keyfe', 'şâ'e', 'zâde', 'kesîr', 'min', 'enzele', 'ilâ', 'rabb', 'tuğyân', 'kufr', 'elqâ', 'beyn', ''adâve', 'bağdâ'', 'yevm', 'qiyâme', 'kullemâ', 'evqadu' (morph LEM ham biçim), "
 "'nâr', 'harb', 'atfe'e', 'se'â', 'fî', 'ard', 'fesâd', 'allâh', 'lâ', 'ahbeb' (morph LEM ham biçim), 'mufsid', 'lev', 'enne', 'ehl', 'kitâb', 'âmene', 'itteqâ', 'keffere', ''an', 'seyyi'e', 'udxile', 'cenne', 'na'îm', 'eqâme', 'tevrâ', 'incîl', 'ekele', 'fevq', 'taht', 'ricl', 'umme', 'muqtaside', 'sâ'e', ''amile'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

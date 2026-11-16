_BAS = {l.strip() for l in open('/home/claude/sunum/basilan.txt', encoding='utf-8') if l.strip()}
def _numarasiz(m):
    refs = [x.strip() for x in m.group(1).split(',')]
    kal = [x for x in refs if ':'.join(x.split(':')[:2]) in _BAS]
    n = len(refs) - len(kal)
    return '(' + ', '.join(kal + (['okunmuş %d konum' % n] if n else [])) + ')'
ESL = re.sub(r'\((\d+:\d+:\d+(?:, \d+:\d+:\d+)*)\)', _numarasiz, ESL)
_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_71_74.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'5:71', '5:72', '5:73', '5:74'}
D3DISI = ', '.join(sorted(_U - _BAG - _ON, key=lambda x: tuple(map(int, x.split(':')))))
ANILIS = "5:71 kök عمي (''amû' 5. ve 12. kelime — körlük) ve kök صمم ('sammû' 6. ve 13. kelime — sağırlık): duyu kaybı, tetik listesinde yok; 5:72 kök نور ('n-nâru' 29. kelime — ateş) ve kök جنن ('l-cennete' 27. kelime — cennet): K listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '71', '74', '23')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b23/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 24)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b5:%d:\d+' % a_, s_) for a_ in range(71, 75))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: sunum/yasakli.sh IZIN eki (bölüm 7 kuralı 11 yasaklı sıra sayısı — 5:73 'sâlisu selâse' kök karşılığı sıra sayısı içeriyor, kök karşılığı izni emsaliyle; gloss_tara çıktısındaki ثلث karşılığı; es_lemma çıktısı oturum başında basılmamış konumları numarasız verdiği için 'bir' + iyelik karşılığının eski izni yeni biçimde), sunum/yasakli_test.txt (yeni sınama satırları; yasakli_sina tamam); ARIZA üreticisi (es_lemma çıktısında bu oturumda basılmamış konumlar sinifla mantığıyla numarasız — sızıntı kuralı; oturum başı basilan.txt boş); "
 "mutasyon_sina — MUT_SONUC; geriye dönük koşu son araç değişikliğinden sonra yeniden üretildi (GERI_P); düşen 18 — araç değişti: r5_gerekce / bolum9_kurallar (4) 16 (oturum başında basilan.txt boşaldı; R5 gerekçelerindeki basılmış eş adları 'basılmamış eş' biçimine döndü, kayıt değişmedi), kural13 (2) 2 (blok 22 've' / 'fe' etiket isabetleri); "
 "yeni 19 — bolum9_kurallar (4) 18 (bu nedenle, oturum başı basilan.txt), gloss_tara KAPSAMAYAN 1 (blok 23, 15 kelime) — tam okuma sonu listesi, kayıtlar geriye dönük yeniden yazılmadı",
 "kök tablosu: ölçümde '???' 5:71-74 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 71 74 23'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:71 'basîrun' (17. kelime) — esma_el 'ilahi', kural ''ve'llâhu X' kuralı' (lafzın haberi); 5:72 'ensâr' (33. kelime) — esma_el 'degil', kural 'çoğul insan göndergeli' (yardımcılar; olumsuzlanan yardımcılar); "
 "5:74 'ğafûrun' (7. kelime) ve 'rahîm' (8. kelime) — esma_el 'ilahi', kural ''ve'llâhu X' kuralı' (lafzın haberi); 5:73 esmâ yok; 5:71 've'llâhu' (16.) ve 5:74 've'llâhu' (6.)'daki 've' morph REM (kuralın tipik biçimi); "
 "lafız 5:71 (2 geçiş), 5:72 (4 geçiş), 5:73, 5:74 (2 geçiş); Rab 5:72 ('rabbî', 'rabbekum', 17. ve 18. sırada) — Rab adı (bölüm 6 kuralı 14 — betikle: B6_ESMA; emsal kayıtları 'ensâr' için 'çoğul insan göndergeli' — bu kayıt da öyle)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 71 74 23'): " + EMH,
 "ölçüm: 5:71 '{{1|fâsıla يعملون → ن, N sınıfı}}', '{{1|sayı işareti \\S+}}', '{{1|simetri \\[3, 5, 12, 1\\]}}', '{{1|harf 87 → harf3 78, isaret 9}}' ve '{{1|dış düğüm 0}}'; "
 "5:72 '{{2|fâsıla أنصار → ر, R sınıfı — KAFİYE KIRILMASI}}', '{{2|simetri \\[3, 1, 5, 1\\]}}', '{{2|İÇ düğüm 1}}', '{{2|harf 143 → harf3 136, isaret 7}}' ve '{{2|dış düğüm 2}}'; "
 "5:73 '{{3|fâsıla أليم → م, N sınıfı}}', '{{3|sayı işareti \\S+, \\S+, \\S+}}', '{{3|simetri \\[4, 1, 16, 1\\]}}', '{{3|harf 102 → harf3 94, isaret 8}}' ve '{{3|dış düğüm 3}}'; "
 "5:74 '{{4|fâsıla رحيم → م, N sınıfı}}', '{{4|harf 44 → harf3 40, isaret 4}}' ve '{{4|dış düğüm 0}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 71 74 23'): KALAN_P",
 "ölçüm aktör: 5:72 '{{2|adlı مَسِيح 8\\. sırada \\(kisi, rol fail\\+konusan\\)}}' — 'qâlû' sözünde lafzın haberi (okuma; ölçüm rolü 'fail+konusan'), '{{2|adlı مَرْيَم 10\\. sırada \\(kisi, rol mecrur\\)}}' — 'bnu' muzâfun ileyhi, "
 "'{{2|adlı مَسِيح 12\\. sırada \\(kisi, rol fail\\+konusan\\)}}' — 'qâle' faili ve söz sahibi, '{{2|adlı إِسْرائِيل 14\\. sırada \\(kavim, rol mecrur\\)}}' — nida edilen 'benî' muzâfun ileyhi, '{{2|adlı \\S+ 27\\. sırada \\(yer, rol meful\\)}}' — 'harrama' mef'ûlü; 5:71, 5:73 ve 5:74 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle): 5:71 haber — NEG 1 'lâ' (2.); 5:72 emir, nida, şart — CERT 2 'qad' (1., 23.), COND 1 'men' (20.), EMPH 1 'le' (1.), IMPV 1 ''budu' (15.), NEG 1 'mâ' (30.), VOC 1 'yâ' (13.); "
 "5:73 şart — CERT 1 'qad' (1.), COND 1 'in' (15.), EMPH 3 'le' (1.), 'le' ve te'kid nûnu (20.), NEG 2 'mâ' (9.), 'lem' (16.), RES 1 'illâ' (12.), biçim HASR; 5:74 soru — INTG 1 'e' (1.), NEG 1 'lâ' (1.); morph SUP 'fe' (5:74 1.) ve CAUS 'fe' (5:71 5.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 5:71 ★ (kaynak allah, z=1,58); 5:72 ★★ (kaynak n, z=2,19; eşiği geçen başka: allah z=1,90; kafiye kırığı); 5:74 ★★★ (kaynak allah, z=4,47); 5:73 yıldız yok",
 "fâsıla: 5:71 ن (يعملون) → 5:72 ر (أنصار) → 5:73 م (أليم) → 5:74 م (رحيم); kafiye kırığı 5:72 (ölçüm 'KAFİYE KIRILMASI'); 5:73 ve 5:74 kapanışı م; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref: 5:72 5:17 (emsal olarak basıldı) ve okunmuş başka ayetler; 5:73 9:90 (emsal olarak basıldı) ve okunmuş başka ayetler; 5:71 ve 5:74 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, joker '_' ile; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:72 'qad kefera ellezî qâle inne allâh _ mesîh ibn meryem qâle', 'qad kefera ellezî qâle inne allâh', ''abede allâh rabb rabb' ve 'mesîh ibn meryem' süzgeç GEÇER; "
 "5:73 'qad kefera ellezî qâle inne allâh' GEÇER, 'ellezî kefera min' GEÇMEZ; 5:74 'allâh ğafûr rahîm' GEÇER; 5:71 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap' ile; alıntı ve kelime numarası ◇ konumuyla eş): "
 "5:71 3MP (adsız — 'hasibû', ''amû', 'sammû', 'ya'melûn' failleri; ''aleyhim', 'minhum'), 'fitnetun' ('tekûne' faili — 3FS fiil uyumu), Allah (lafız; 'tâba' faili — 3MS fiil uyumu), 'kesîrun' (bedel); "
 "5:72 'llezîne qâlû' ('kefera' faili — 3MS fiil uyumu), 3MP (adsız — 'qâlû' faili), Allah (lafız), 'huve' ve 'innehû' 3MS (adsız; fasıl / şe'n zamiri), Mesih ve Meryem (adlı kişiler), 'l-mesîhu' ('qâle' faili — 3MS fiil uyumu), İsrâiloğulları (nida edilen; adlı kavim), muhatap 2MP ve konuşan 1S (adsız; söz içi), Rab, 'men' (şart), 3MS (adsız — 'yuşrik' faili; ''aleyhi', 'me'vâhu'), 'l-cennete' (adlı yer); "
 "'li'z-zâlimîne' (li + belirli çoğul, mecrur) ve 'ensâr' (min + nekre çoğul, mecrur; olumsuz isim cümlesinin mübtedası) A1'de yazılmadı — mecrur çoğul ölçütü; "
 "5:73 'llezîne qâlû' ('kefera' faili — 3MS fiil uyumu), 3MP (adsız — 'qâlû', 'yentehû', 'yeqûlûne', 'keferû' failleri; 'minhum'), Allah (lafız; söz içi), ''azâbun' ('yemessenne' faili — 3MS fiil uyumu), 'llezîne keferû' ('yemessenne' mef'ûlü); 'ilâhin' (min + nekre, mecrur) A1'de yazılmadı; "
 "5:74 3MP (adsız — 'yetûbûne', 'yestağfirûnehû' failleri), 3MS (adsız — 'yestağfirûnehû' mef'ûlü; gönderge lafız), Allah (lafız) — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): 5:72 'qâlû' sözü (A3, 5-10. kelime) ve 'qâle' sözü (A3, 13-29. kelime) — 30. kelimedeki morph REM 've' tırnağı kapatır ('ve mâ li'z-zâlimîne min ensâr' söz dışında okundu); 5:73 'qâlû' sözü (A3, 5-8. kelime); 5:71 ve 5:74 söz yok; "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 71 74 23' — A3 aralığında morph REM): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:71 've hasibû' (1.), 've sammû' (6., 13.) CONJ, 'fe-'amû' (5.) CAUS, 've'llâhu' (16.) REM; 5:72 've qâle' (11.), 've mâ' (30.) REM, 've rabbekum' (18.) CONJ, 've me'vâhu' (28.) CIRC, 'fe-qad' (23.) RSLT; "
 "5:73 've mâ' (9.), 've in' (15.) REM; 5:74 'fe-lâ' (1.) SUP, 've yestağfirûnehû' (5.) CONJ, 've'llâhu' (6.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 5:71 ◈B بصر ('basîrun' 17. kelime — B3; anlam notu: 'basîr' sıfat, lafzın haberi — duyu organı değil); 5:72, 5:73 ve 5:74 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 71 74 23'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:71 (2:96), 5:72 (5:17, 3:192), 5:73 (9:90) (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde ya da ölçüm xref satırında emsali buluyor — bölüm 9 kuralı 3); 5:74 D3 eşi yok; "
 "ayetler arası kalıp 'le-qad kefera'llezîne qâlû inna'llâh' (5:72, 5:73) — sayım 'say 5:73 1-6'; blok içi tekrar (bölüm 9 kuralı 6), ardışık bağ yerine sayımla kayıt; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7 — betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:71 — (edim haber, baskın şahıs 3; geçiş yok); 5:72 edim geçişi haber → emir, nida, şart; şahıs geçişi yok; söz açılır / kapanır (5-10. ve 13-29. kelime); şart → cevap ('men' 20. kelime); "
 "5:73 edim geçişi emir, nida, şart → şart; şahıs geçişi yok; söz açılır / kapanır (5-8. kelime); şart → cevap ('in' 15. kelime); 5:74 edim geçişi şart → soru; şahıs geçişi yok",
 "sözdizimi (okuma; morph etiketiyle): 5:71 'ellâ tekûne fitnetun' — 'en' masdar cümlesi, 'hasibû' mef'ûlü (morph SUB + NEG); 'fe-'amû' — sonuç (morph CAUS); 'kesîrun minhum' — ''amû ve sammû' zamirinden bedel (okuma); 've'llâhu basîrun' — istînâf (morph REM); "
 "5:72 'inna'llâhe huve'l-mesîhu' — 'inne' haberi, 'huve' fasıl zamiri (morph ACC); 've qâle'l-mesîh' — istînâf (morph REM); 'yâ benî isrâ'île' — nida (morph VOC); 'innehû men yuşrik' — şe'n zamiri ve şart (morph ACC + COND); 'fe-qad harrama' — şart cevabı (morph RSLT + CERT); 've me'vâhu'n-nâru' — hâl (morph CIRC); 've mâ li'z-zâlimîne min ensâr' — olumsuz isim cümlesi, 'min' istiğrak (morph REM + NEG); "
 "5:73 'mâ min ilâhin illâ ilâhun vâhidun' — olumsuzluk ve istisna ile hasr (morph NEG + RES; ölçüm biçim HASR); 'in lem yentehû' — şart (morph COND + NEG); 'le-yemessenne' — kasem cevabı (morph EMPH ×2), şart cevabı mahzuf, kasem cevabıyla anlaşılıyor (okuma); "
 "5:74 'e-fe-lâ yetûbûne' — olumsuz soru, teşvik (morph INTG + SUP + NEG); 've'llâhu ğafûrun rahîm' — istînâf (morph REM)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:71 kök عمي ve صمم ikilemesi ''amû' / 'sammû' — 5., 6. ve 12., 13. kelimede, araya 'summe tâba'llâhu 'aleyhim' giriyor; "
 "5:72 ve 5:73 'le-qad kefera'llezîne qâlû inna'llâh' ile açılıyor — 5:17 açılışıyla eş; 5:72 kök مسح ikilemesi 'l-mesîhu' (8., 12. kelime) — Mesih hakkında söz ve Mesih'in sözü; 5:73 kök ثلث ikilemesi 'sâlisu selâsetin' ve kök أله ikilemesi 'ilâhin' / 'ilâhun'; "
 "5:74 kök غفر ikilemesi 'yestağfirûnehû' / 'ğafûrun'",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 23'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + "'; çıktı aynen, yalnız bu oturumda basılmamış konumlar sinifla mantığıyla numarasız — sızıntı kuralı): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp): 've'llâhu basîrun bi-mâ ya'melûn' 5:71 'Allah yaptıklarını görendir' / 2:96 'Allah yaptıklarını görendir' (emsal metninde) — çakışma değil; "
 "'le-qad kefera'llezîne qâlû inna'llâh' 5:72 'Andolsun, … diyenler inkâr etmiştir' / 5:17 'Andolsun, … diyenler inkâr etmiştir' (emsal metninde) — çakışma değil; 've mâ li'z-zâlimîne min ensâr' 5:72 'Zalimler için yardımcılardan hiçbiri yoktur' / 3:192 'zalimler için yardımcılardan hiçbiri yoktur' (emsal metninde) — çakışma değil; "
 "'llezîne keferû minhum' 5:73 'onlardan inkâr edenlere' / 9:90 'Onlardan inkâr edenlere' (emsal metninde) — çakışma değil; teslis sözündeki 'sâlis' / 'selâse' karşılığı sıra sayısı ve sayı + tamlayan eki (kök karşılığı — yasakli.sh IZIN, öz denetim maddesinde)",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle): " + (MKK or 'yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 71 74 23'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:72 tarayıcı adayı (kök نور; A_şart) — çıpa değil: 'n-nâru' şartlı hükümde ahiret barınağı, doğa iddiası yok (olgu=False); 5:73 tarayıcı adayı (A_şart, F_ölçü) — çıpa değil: sayı sözcükleri teslis sözünde, şart azap tehdidinde, doğa iddiası yok (olgu=False); 5:71 ve 5:74 tarayıcı vermedi (cipa_tarama5_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 5:71 ('fe-'amû ve sammû' / 'summe tâba'llâhu 'aleyhim'); 5:72 ('l-cennete' / 'n-nâru'); 5:73 ('sâlisu selâsetin' / 'ilâhun vâhidun'); ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök عمي ve صمم 5:71 ''amû' / 'sammû' (5., 6. ve 12., 13. kelime) — tövbe kabulünden önce ve sonra; kök ثلث 5:73 'sâlisu' / 'selâsetin' ve kök أله 'ilâhin' / 'ilâhun' — teslis sözü ve hasr; kök غفر 5:74 'yestağfirûnehû' / 'ğafûrun' — okuma",
 "bölüm: " + BOL + " bölümü, bölüm 10-2 (bölüm 7 kuralı 9 — blok_plani_5.txt'ten) — bölüm üç blok (22, 23, 24); başlıktaki 'Mesih ve teslis' 5:72 ve 5:73; "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b23/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9 — betikle: komut 'python3 sunum/bolum5_kurallar.py 71 74 23'; lem_bozuk.py 23 çıktısı): 5:71:6 'sammu' — lem_bozuk bayrağı (5:71:13 'sammû' de bu LEM); 5:72:13 'buneyy' (sunum/ham_elle.txt) — elle ham listesi; meal maddesinde '(morph LEM ham biçim)' notlu; lemma adı listesinde notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 71 74 → AYN_SONUC; sunum/bolum4_kurallar.py 71 74 23 → KHATA_HEPSI; sunum/bolum5_kurallar.py 71 74 23 → B5_HEPSI; sunum/bolum6_kurallar.py 71 74 23 → B6_HEPSI; sunum/bolum7_kurallar.py 71 74 23 → B7_HEPSI; sunum/bolum8_kurallar.py 71 74 23 → B8_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme: es_lemma numarasız çıktısındaki 'bir' + iyelik karşılığı, 'sâlisu selâse' karşılığının meal ve meal maddesindeki biçimleri ve gloss_tara ثلث satırı (tırnaklı tam biçimler; sunum/yasakli_test.txt'e üç OLUMSUZ, iki OLUMLU satır eklendi)",
 "sonradan basılan (sunum/sonradan.py --plan 23): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('hasibe', 'en', 'lâ', 'kâne', 'fitne', ''amiye', 'sammu' (morph LEM ham biçim), 'tâbe', 'allâh', ''alâ', 'kesîr', 'min', 'basîr', 'mâ', ''amile', "
 "'qad', 'kefera', 'ellezî', 'qâle', 'inne', 'mesîh', 'ibn', 'meryem', 'buneyy' (morph LEM ham biçim), 'isrâ'îl', ''abede', 'rabb', 'men', 'eşrake', 'harrame', 'cenne', 'me'vâ', 'nâr', 'zâlim', 'nasîr', "
 "'sâlis', 'selâse', 'ilâh', 'illâ', 'vâhid', 'in', 'lem', 'intehâ', ''an', 'messe', ''azâb', 'elîm', 'ilâ', 'istağfere', 'ğafûr', 'rahîm'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; 5:72 'isrâ'île 'budu'llâhe' wasl birleşimi kelime sınırında boşlukla yazıldı (kelime sayım araçları 'e'b' birleşimini bölmüyor); wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

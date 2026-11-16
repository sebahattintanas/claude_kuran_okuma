_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_78_81.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'5:78', '5:79', '5:80', '5:81'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_78_81.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '5:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '5:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(78, 82))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "5:78 kök لسن ('lisâni' 8. kelime — dil): Dâvûd ve Îsâ'nın dili, organ tetik listesinde yok; 5:80 kök رأي ('terâ' 1. kelime — görme) ve kök نفس ('enfusuhum' 11. kelime — nefis): tetik listesinde yok; kök ولي (5:80 'yetevellevne' 4. kelime — velî edinme; 5:81 'evliyâ'e' 11. kelime — velîler): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '78', '81', '25')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b25/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 26)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b5:%d:\d+' % a_, s_) for a_ in range(78, 82))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bölüm 10 denetiminin araç kuralları — sunum/bolum10_kurallar.py yeni (kurallar 1, 2, 3, 5, 6, 7, 8, 9, 10, 11); sunum/lem_bozuk.py (kural 4: harekesiz 'و' ile biten LEM); "
 "sunum/es_lemma.py ve sunum/sonradan.py '--numarasiz' seçeneği (kural 9; ARIZA bu çıktıyı aynen taşır, üreticide dönüşüm yok); sunum/yasakli.sh IZIN (dosya deseni, metin) çiftleri (kural 10), sunum/yasakli_test.txt sınama satırları; "
 "sunum/bolum7_kurallar.py kural 7 ayet başına D3 dışı listesi (kural 11); sunum/geriye_donuk.py bolum10_kurallar; sunum/satir_aynen_tam.py taşınan bölüm denetimi maddelerini (bekleyen_ariza, aynen) ölçüm alıntısı saymaz; sunum/mutasyon_sina.py bölüm 10 sınamaları; "
 "mutasyon_sina — MUT_SONUC; geriye dönük koşu son araç değişikliğinden sonra yeniden üretildi (GERI_P); yeni 177 — bolum10_kurallar 173 (kurallar 1, 2, 3, 5, 6, 7, 8, 11 okunmuş bloklardaki eski kayıtlara uygulandı; kurallar o bloklarda yoktu), gloss_tara KAPSAMAYAN 2 ve es_edat tanınmayan 2 (blok 24 ve 25 kayıtları, karşılaştırma tabanı blok 23 dosyası; tam okuma sonu listesi) — kayıtlar geriye dönük yeniden yazılmadı",
 "kök tablosu: ölçümde '???' 5:78-81 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 78 81 25'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:81 'evliyâ'e' (11. kelime) — esma_el 'degil', kural 'çoğul insan göndergeli' (velîler); 5:78, 5:79 ve 5:80 esmâ yok; lafız 5:80 ve 5:81; 5:78 ve 5:79 lafız yok; Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); "
 "gönderge 'evliyâ'e' kelimenin kendisi — A1'de istisna kaydıyla yazıldı (bölüm 10 denetimi kuralı 13)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 78 81 25'): " + EMH,
 "ölçüm: 5:78 '{{1|fâsıla يعتدون → ن, N sınıfı}}', '{{1|EDİLGEN 1/5 fiil, pas z=0,81}}', '{{1|simetri \\[4, 4, 10, 1\\]}}', '{{1|harf 75 → harf3 69, isaret 6}}' ve '{{1|dış düğüm 2}}'; "
 "5:79 '{{2|fâsıla يفعلون → ن, N sınıfı}}', '{{2|simetri \\[3, 4, 8, 1\\]}}', '{{2|harf 46 → harf3 42, isaret 4}}' ve '{{2|dış düğüm 0}}'; "
 "5:80 '{{3|fâsıla خلدون → ن, N sınıfı}}', '{{3|sayı işareti \\S+}}', '{{3|simetri \\[3, 3, 8, 1\\]}}', '{{3|harf 80 → harf3 77, isaret 3}}' ve '{{3|dış düğüm 0}}'; "
 "5:81 '{{4|fâsıla فسقون → ن, N sınıfı}}', '{{4|EDİLGEN 1/4 fiil, pas z=1,10}}', '{{4|sayı işareti \\S+}}', '{{4|simetri \\[3, 6, 12, 1\\]}}', '{{4|harf 71 → harf3 69, isaret 2}}' ve '{{4|dış düğüm 0}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 78 81 25'): KALAN_P",
 "ölçüm aktör: 5:78 '{{1|adlı إِسْرائِيل 6\\. sırada \\(kavim, rol mecrur\\)}}' — 'benî' muzâfun ileyhi, '{{1|adlı داوُد 9\\. sırada \\(kisi, rol mecrur\\)}}' — 'lisâni' muzâfun ileyhi, '{{1|adlı عِيسَى 10\\. sırada \\(kisi, rol mecrur\\)}}' — 'dâwûde' üzerine atıf, '{{1|adlı مَرْيَم 12\\. sırada \\(kisi, rol mecrur\\)}}' — 'bni' muzâfun ileyhi; 5:79, 5:80 ve 5:81 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 5:78 haber — kip yok; 5:79 haber — NEG 1 'lâ' (2.), EMPH 1 'le' (7.); 5:80 haber — EMPH 1 'le' (7.); 5:81 şart — COND 1 'lev' (1.), NEG 1 'mâ' (9.); morph REM 've' (5:80 16., 5:81 1. ve 12.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): bu blokta yıldız yok (5:78, 5:79, 5:80 ve 5:81 'yıldız yok')",
 "fâsıla: 5:78 ن (يعتدون) → 5:79 ن (يفعلون) → 5:80 ن (خلدون) → 5:81 ن (فسقون); bölüm açılışında kafiye ن'ye dönüyor (5:77 ل); blok içi kırık yok; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6 — basılmamış hedefler sinifla sayısıyla): 5:78 2:61 (emsal olarak basıldı) ve okunmuş 1 ayet; 5:79 ve 5:80 xref yok; 5:81 bağ yok ('xref üçü de boş')",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, joker '_' ile; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:78 'ellezî kefera min' ve ''îsâ ibn meryem' süzgeç GEÇMEZ; 5:79 'bi'se mâ kâne' GEÇER; 5:80 'ra'â kesîr min' GEÇMEZ; 5:81 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap' ile; alıntı ve kelime numarası ◇ konumuyla eş): "
 "5:78 'llezîne keferû' ('lu'ine' naib-i faili — 3MS fiil uyumu), 3MP (adsız — 'keferû', ''asav', 'kânû', 'ya'tedûn' failleri), İsrâiloğulları (adlı kavim), Dâvûd, Îsâ ve Meryem (adlı kişiler); "
 "5:79 3MP (adsız — 'kânû', 'yetenâhevne', 'fe'alûhu', 'yef'alûn' failleri), 3MS (adsız — 'fe'alûhu' aid zamiri), 'bi'se' (3MS fiil uyumu); "
 "5:80 muhatap 2MS (adsız — 'terâ'), 'kesîran minhum' ('yetevellevne' faili), 3MP (adsız), 'llezîne keferû' ('yetevellevne' mef'ûlü), 'enfusuhum' ('qaddemet' faili — 3FS fiil uyumu), Allah (lafız; 'saxita' faili — 3MS fiil uyumu), 'hum' (adsız); "
 "5:81 3MP (adsız — 'kânû', 'yu'minûne', 'ttexazûhum' failleri ve mef'ûlü; 'minhum'), Allah (lafız), Nebi ('n-nebiyyi'), 'unzile' (3MS edilgen; naib-i fail mevsûl), 3MS (adsız — 'ileyhi'), 'evliyâ'e' ('ttexazû' mef'ûlü; esmâ göndergesi), 'kesîran minhum' ('lâkinne' ismi) — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): bu blokta söz yok (A3 —); 'qul' yok (bölüm 10 denetimi kuralı 8); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 78 81 25' — A3 aralığında morph REM): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 5:78 've 'îsâ'bni' (10.), 've kânû' (16.) CONJ; 5:80 've fi'l-'azâbi' (16.) REM; 5:81 've lev' (1.), 've lâkinne' (12.) REM, 've'n-nebiyyi' (5.), 've mâ' (6.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): bu blokta tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 78 81 25'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:78 (2:61), 5:79 (5:62), 5:80 (5:62) (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde ya da ölçüm xref satırında emsali buluyor — bölüm 9 kuralı 3); 5:81 D3 eşi yok; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:78 bölüm açılışı (bölüm 10 denetimi kuralı 2); edim geçişi emir, yasak, nida → haber; şahıs geçişi yok; 5:79 ve 5:80 — (edim haber, baskın şahıs 3; geçiş yok); 5:81 edim geçişi haber → şart; şart → cevap ('lev' 1. kelime)",
 "sözdizimi (okuma; morph etiketiyle): 5:78 'lu'ine'llezîne keferû' — edilgen fiil ve naib-i fail; ''alâ lisâni dâwûde ve 'îsâ'bni meryeme' — atıf (morph CONJ); 'zâlike bi-mâ 'asav ve kânû ya'tedûn' — 'mâ' masdar, 'kâne' + muzâri sürerlik; "
 "5:79 'kânû lâ yetenâhevne' — geçmiş sürerlik ve olumsuzluk (morph NEG); 'fe'alûhu' — 'munkerin' sıfatı; 'le-bi'se mâ kânû yef'alûn' — yerme fiili (morph EMPH); "
 "5:80 'terâ kesîran minhum yetevellevne' — 'terâ' mef'ûlü ve cümle; 'le-bi'se mâ qaddemet' — yerme fiili; 'en saxita'llâhu' — 'en' masdar, yerilenin açıklaması (morph SUB); 've fi'l-'azâbi hum xâlidûn' — istînâf (morph REM); "
 "5:81 'lev kânû … me'ttexazûhum' — 'lev' şartı ve cevabı (morph COND + NEG); 've lâkinne kesîran minhum fâsiqûn' — istidrâk (morph REM + ACC)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:78 kök بني ikilemesi 'benî' / 'bni' (5., 11. kelime); 5:79 kök فعل ikilemesi 'fe'alûhu' / 'yef'alûn' ve kök كون ikilemesi 'kânû' (1., 9. kelime); "
 "5:79 ve 5:80'de 'le-bi'se mâ' yerme kalıbı (7-8. kelime); 5:80 ve 5:81'de 'kesîran minhum' (5:80 2-3., 5:81 13-14. kelime)",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 25'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp): ''asav ve kânû ya'tedûn' 5:78 'isyan etmeleri ve sınırı aşmaları' / 2:61 'isyan etmeleri ve sınırı aşmaları' (emsal metninde) — çakışma değil; "
 "'le-bi'se mâ kânû' 5:79 'Yapmakta oldukları ne kötüdür' / 5:62 'Yapmakta oldukları ne kötüdür' (emsal metninde) — çakışma değil; 'terâ kesîran minhum' 5:80 'Onların çoğunun … görürsün' / 5:62 'Onların çoğunun … görürsün' (emsal metninde) — çakışma değil; "
 "'nebiyy' karşılığı 'Nebi' (önceki kayıtlarda 'nebi'; metin dışı ad yasağı gereği tekil belirli kullanım büyük harfle); es_edat tanınmayan 'lâkinne' — 'fakat' karşılığı edat kalıbıyla yazıldı, edat sözlüğünde başlık yok (bölüm 6 kuralı 11 gerekçesi)",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük): " + (MKK or 'yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 78 81 25'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:78, 5:79, 5:80 ve 5:81 tarayıcı vermedi (cipa_tarama5_adaylari.json); doğa iddiası yok (olgu=False); L3 / L4 adayı yok",
 "aday 1039: 5:81 ('kânû yu'minûne bi'llâhi' / 'fâsiqûn'); 5:78, 5:79 ve 5:80 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök فعل 5:79 'fe'alûhu' / 'yef'alûn' — kötülüğü yapma ve yapmayı sürdürme; kök بأس 'le-bi'se' 5:79 ve 5:80 (7. kelime) — yerme; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 11-1 (bölüm 7 kuralı 9 — blok_plani_5.txt'ten) — bölüm iki blok (25, 26); bu blok bölümü açıyor; başlıktaki 'Lanetlenenler' 5:78; "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b25/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9 — betikle: komut 'python3 sunum/bolum5_kurallar.py 78 81 25'; lem_bozuk.py 25 çıktısı): 5:79:3 'yetenâhe' — lem_bozuk bayrağı; 5:78:5 'buneyy' (sunum/ham_elle.txt) — elle ham listesi; meal maddesinde '(morph LEM ham biçim)' notlu; lemma adı listesinde notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 78 81 → AYN_SONUC; sunum/bolum4_kurallar.py 78 81 25 → KHATA_HEPSI; sunum/bolum5_kurallar.py 78 81 25 → B5_HEPSI; sunum/bolum6_kurallar.py 78 81 25 → B6_HEPSI; sunum/bolum7_kurallar.py 78 81 25 → B7_HEPSI; sunum/bolum8_kurallar.py 78 81 25 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 78 81 25 → B9_HEPSI; sunum/bolum10_kurallar.py 78 81 25 → B10_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme: bekleyen_ariza_5_b24.txt ve bu ARIZA dosyası için bölüm denetimi alıntısı (tırnaklı, dosyaya özgü)",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 25 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('ellezî', 'kefera', 'min', ''îsâ', 'ibn', 'meryem', ''asâ', 'kâne', 'i'tedâ', 'yetenâhe' (morph LEM ham biçim), 'bi'se', 'mâ', 'fe'ale', 'ra'â', 'kesîr', ''azâb', 'xâlid', 'fâsiq'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

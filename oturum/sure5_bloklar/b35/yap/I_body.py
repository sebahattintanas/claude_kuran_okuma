I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bölüm 15 denetiminin araç kuralları — sunum/bolum15_kurallar.py yeni (kurallar 1, 2, 3, 4, 5, 7, 8, 9, 14, 15, 17, 19); "
 "sunum/bolum13_kurallar.py kural 4: 'söz ayet sonunda kapanmıyor' notlu A3'te 'söz kapanır' istenmez (bölüm 15 denetimi kuralı 2); "
 "sunum/bolum14_kurallar.py kural 5: emsal metninde kesme tırnak da aranır ve 'emsal biçimi' gerekçesinde anılan emsalde قول fiili istenir; '(emsal biçimi — …)' biçimi de okunur (bölüm 15 denetimi kuralı 6); "
 "sunum/bolum6_kurallar.py kural 14 'sıfatı' eşleşmesi kelime sınırıyla (bölüm 15 denetimi kuralı 9); "
 "sunum/bolum5_kurallar.py önek soyma yalnız lemma adı listesinde ve önek kümesi 'fe-', 've-', 'bi-', 'li-', 'ke-' (bölüm 15 denetimi kuralı 10); "
 "sunum/edat_etiket.py EDLEM kümesine 'hel', 'leyse' ve 'lemmâ' (bölüm 15 denetimi kuralı 15); sunum/geriye_donuk.py sinifla SON değişiminden doğan düşüşü 'basılan değişti' sınıfına koyar (bölüm 15 denetimi kuralı 12) ve bolum15_kurallar'ı geriye dönük kümeye alır; "
 "sunum/mutasyon_sina.py bölüm 15 sınamaları (kural 1-5, 7-9, 14, 15, 19: bozuk kayıtta isabet; kural 6: 3:49 gerekçesi; kural 10: LEM kaydında önekli ad; kural 2: bolum13 istisnası); mutasyon_sina — MUT_SONUC; "
 "kural 13 elle (karar üyesi ile morph kelimesi eşlemesi betikle güvenilir değil); kural 18 elle; kurallar 11 ve 16 kullanıcı kararı (kayıtta); "
 "geriye dönük koşu son araç değişikliğinden sonra yeniden üretildi (GERI_P); yeni 105 — bolum15_kurallar 102 (kural 19: 34, kural 5: 17, kural 7: 12, kural 15: 11, kural 8: 10, kural 1: 5, kural 2: 5, kural 3: 2, kural 4: 2, kural 9: 2, kural 14: 1, kural 17: 1), "
 "es_edat tanınmayan 2 (blok 20 ve 28 — 'hel' tanınınca sayı değişti), gloss_tara KAPSAMAYAN 1 (blok 34 kapsam sayımı, TARANMAYAN değil); düşen 2 — araç değişti 2 (edat_etiket 'hel'); kayıtlar geriye dönük yeniden yazılmadı; "
 "basilan satır sayısı (blok anı): 83",
 "kök tablosu: ölçümde '???' 5:116 ve 5:117 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 116 117 35'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:117 've kuntu 'aleyhim şehîden' (13-15. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (şahittim); "
 "5:117 'kunte ente'r-raqîbe' (21-23. kelime) ve 've ente 'alâ kulli şey'in şehîd' (25-29. kelime) — esma_el 'ilahi', kural 'lafzın haberi' (Allah) — 2MS 'ente' hitap edilen Allah; kapalı listede 'zamirin haberi' adı yok (kullanıcı kararı, kayıt); "
 "5:116 esmâ yok; lafız 5:116 ve 5:117; Rab 5:117 (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 116 117 35'; bölüm 13 denetimi kuralı 2: esma_el eklendikten sonra; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: 5:116 '{{1|fâsıla ٱلغيوب → ب, ب sınıfı}}', '{{1|simetri \\[7, 2, 16, 2\\]}}', '{{1|harf 156 → harf3 150, isaret 6}}' ve '{{1|dış düğüm 4}}'; "
 "5:117 '{{2|fâsıla شهيد → د, د sınıfı}}', '{{2|simetri \\[6, 1, 22, 2\\]}}', '{{2|harf 115 → harf3 108, isaret 7}}' ve '{{2|dış düğüm 2}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 116 117 35'): KALAN_P",
 "ölçüm aktör: 5:116 '{{1|adlı عِيسَى 4\\. sırada \\(kisi, rol meful\\+muhatap\\)}}' — münadâ ve söz muhatabı; '{{1|adlı مَرْيَم 6\\. sırada \\(kisi, rol mecrur\\)}}' — 'ibn' muzâfun ileyhi; 5:117 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 5:116 soru, emir, nida, şart — VOC 1 'yâ' (4.), INTG 1 'e-ente' (7.), IMPV 1 'ttexizûnî' (10.), NEG 2 'mâ' (18.), 've lâ' (36.), COND 1 'in' (27.), CERT 1 'fe-qad' (30.); "
 "5:117 emir — NEG 1 'mâ' (1.), IMPV 1 'u'budû' (9.); ölçüm biçim alanı '{{2|biçim ISTISNA}}' (yalnız bu maddede; 'illâ' EXP 4. kelime); "
 "morph RSLT ('fe' 5:116 30.), REM ('fe' 5:117 19.; 've' 5:117 25.), INT ('en' 5:117 8.), SUB ('en' 5:116 21.; 'mâ' 5:117 16.), T ('iz' 5:116 1.; 'lemmâ' 5:117 19.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 5:116 ★★★ (kaynak n, z=3,35); 5:117 ★ (kaynak n, z=1,76)",
 "fâsıla: 5:115 ن (ٱلعلمين) → 5:116 ب (ٱلغيوب) → 5:117 د (شهيد); 5:116 'allâmu'l-ğuyûb' kapanışı 5:109 ile eş; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 5:116 okunmuş 3 ayet ve henüz okunmamış 1 ayet; 5:117 okunmuş 2 ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:116 'iz qâle allâh 'îsâ ibn meryem', 'inne _ 'allâm ğuyûb' ve ''îsâ ibn meryem' süzgeç GEÇER; 'en qâle mâ', 'min dûn allâh' ve ''alime mâ fî' GEÇMEZ; 5:117 ''abede allâh rabb rabb' ve ''alâ kull şey'' GEÇER",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "fail olmayan mecrur çoğul ad ve mecrur ilgi zamiri A1'de yazılmaz — bölüm 11 denetimi kuralları 16 ve 19; fiilden önce gelen lafız 'mübtedâ' — bölüm 12 denetimi kuralı 11; A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5): "
 "5:116 Allah (lafız; 'qâle' faili), 'yâ 'îse' (münadâ; adlı), muhatap 2MS (adsız; söz içi), muhatap 2MP (adsız; söz içi — iç söz), konuşan 1S (adsız; söz içi), 3MS (adsız — 'qâle' 16., 'yekûnu', 'leyse', 'qultuhû', ''alimtehû'); "
 "5:117 konuşan 1S (adsız; söz içi), muhatap 2MS (adsız; söz içi), muhatap 2MP (adsız; söz içi — iç söz), 3MP (adsız; söz içi — 'lehum', ''aleyhim', 'fîhim'), 3MS (adsız; söz içi — 'bihî'); "
 "'li'n-nâsi' (5:116 9. kelime) ve 'l-ğuyûb' (5:116 44. kelime) — mecrur çoğul — A1'de yazılmadı — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4): 5:116 'qâle' (2.) ardından söz 4-15. kelime, içinde 'qulte' (8.) ardından iç söz 10-15. kelime; 'qâle' (16.) ardından söz 17-44. kelime — söz ayet sonunda kapanmıyor; "
 "5:117 söz sürüyor (5:116 17. kelimeden; 1-29. kelime), içinde 'qultu' (2.) ardından iç söz 9-12. kelime; Îsâ'nın sözü ayet sonunda kapanmıyor; "
 "mealde tırnaksız, iki nokta ile (blok meal biçimi; emsal biçimi gerekçesi yok); A3'te ve A4'te 'söz açılır' / 'söz kapanır'; 'qul' yok (bölüm 10 denetimi kuralı 8); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 116 117 35' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "REM sapması 5:117 (19. kelime) — 'fe-lemmâ' söz içinde istînâf: hayattaki şahitlikten vefat sonrasına geçiş, meal noktalı virgülle ayırıyor; "
 "REM sapması 5:117 (25. kelime) — 've ente' söz içinde istînâf: isim cümlesi, meal nokta ile ayırıyor; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:116 've iz' (1.), 've ummiye' (11.), 've lâ' (36.) CONJ, 'fe-qad' (30.) RSLT; 5:117 've rabbekum' (12.), 've kuntu' (13.) CONJ, 'fe-lemmâ' (19.) ve 've ente' (25.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 5:116 ◈B أنس ('n-nâsi' 9. kelime — B1; anlam notu: söz yöneltildiği iddia edilen insanlar); 5:117 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 116 117 35'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 2 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:116 (9:78); 5:117 (3:51, 5:72) (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "ayetler arası kalıp yok; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:116 bölüm açılışı; söz açılır (4., 10. ve 17. kelime), söz kapanır (15. kelime, ayet içi); şahıs geçişi 3 → 1; edim geçişi şart → soru, emir, nida, şart; şart → cevap (ayet içi); "
 "5:117 iç söz açılır (9. kelime); şahıs geçişi yok (baskın 1); edim geçişi soru, emir, nida, şart → emir",
 "sözdizimi (okuma; morph etiketiyle): 5:116 've iz qâle' — atıf ve zaman (morph CONJ + T); 'e-ente qulte' — soru (morph INTG); 'subhâneke' — tenzih ifadesi; 'mâ yekûnu lî en eqûle' — olumsuzluk ve masdar edatı (morph NEG + SUB); "
 "'in kuntu qultuhû fe-qad 'alimtehû' — şart ve cevap (morph COND + RSLT + CERT); 5:117 'mâ qultu … illâ' — olumsuzluk ve istisna (morph NEG + EXP); 'en u'budû' — açıklama edatı (morph INT); "
 "'mâ dumtu' — süre edatı (morph SUB); 'fe-lemmâ' — istînâf ve zaman (morph REM + T)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:116 've iz qâle'llâhu yâ 'îse'bne meryem' ile açılıyor — 5:110 açılışıyla eş (sayım: 'dizi 5 116 1 6'); "
 "5:116 kök قول beşlemesi ('qâle' 2., 'qulte' 8., 'qâle' 16., 'eqûle' 22. ve 'qultuhû' 29. kelime); 5:116 kök علم dörtlemesi; 5:116 'inneke ente 'allâmu'l-ğuyûb' — 5:109 kapanışıyla eş (sayım: 'say 5:116 41-44'); "
 "5:117 'u'budû'llâhe rabbî ve rabbekum' — 5:72 ile eş (sayım: 'say 5:117 9-12')",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 35'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7): "
 "'rabbî ve rabbekum' 5:117 'Rabbim ve Rabbiniz' / 3:51 'benim de Rabbim, sizin de Rabbinizdir' (emsal metninde) — çakışma — tam okuma sonu; "
 "''allâmu'l-ğuyûb' 5:116 'gaybları en iyi bilen' / 9:78 'gaybları çok iyi bilendir' (emsal metninde) — çakışma — tam okuma sonu; "
 "kip notu (bölüm 15 denetimi kuralı 18): 5:116 'mâ yekûnu lî' IMPF IND — meal 'olmaz' geniş zaman, kip değişimi yok",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 116 117 35'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:116 ve 5:117 tarayıcı vermedi (cipa_tarama5_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 5:116 ve 5:117 yok; ayetler arası yok; eşleme betikle: ADAY_P",
 "aday 1041: kök قول 5:116 (beşleme) ve 5:117 ('qultu') — söz bağı; kök علم 5:116 (dörtleme) — bilgi bağı; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 16-1 (bölüm 7 kuralı 9 — blok_plani_5.txt'ten) — bölüm iki blok (35, 36); bu blok bölümü açıyor; "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b35/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 116 117 35'; lem_bozuk.py 35 çıktısı): 5:117:17 'dâmu' — lem_bozuk bayrağı; meal maddesinde '(morph LEM ham biçim)' notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 116 117 → AYN_SONUC; sunum/bolum4_kurallar.py 116 117 35 → KHATA_HEPSI; sunum/bolum5_kurallar.py 116 117 35 → B5_HEPSI; sunum/bolum6_kurallar.py 116 117 35 → B6_HEPSI; sunum/bolum7_kurallar.py 116 117 35 → B7_HEPSI; sunum/bolum8_kurallar.py 116 117 35 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 116 117 35 → B9_HEPSI; sunum/bolum10_kurallar.py 116 117 35 → B10_HEPSI; sunum/bolum11_kurallar.py 116 117 35 → B11_HEPSI; sunum/bolum12_kurallar.py 116 117 35 → B12_HEPSI; sunum/bolum13_kurallar.py 116 117 35 → B13_HEPSI; sunum/bolum14_kurallar.py 116 117 35 → B14_HEPSI; sunum/bolum15_kurallar.py 116 117 35 → B15_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 35 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; 5:72 bağı basılmış ayete (emsal değil); önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('iz', 'qâle', 'allâh', ''îsâ', 'ibn', 'meryem', 'inne', ''allâm', 'ğuyûb', 'en', 'mâ', 'min', 'dûn', ''alime', 'fî', ''abede', 'rabb', ''alâ', 'kull', 'şey''); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

_OL = [l.replace('**', '') for l in open('/home/claude/b20/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b20/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 69), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta araç kuralı değişmedi; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 478",
 "geriye dönük koşu (sûre 7 bölüm 6 kapanışı, komut 'python3 sunum/geriye_donuk.py b17k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 70 72 20'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:72 've mâ kânû mu'minîn' (11-13. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (yalanlayanların sıfatı) (yamalar/esma_el_7_70_72.txt); 7:70 ve 7:71 esmâ yok; 7:70 lafız (4. kelime), 7:71 lafız (17. kelime); 7:72 lafız yok; 7:71 Rab (6. kelime); 7:70 ve 7:72 Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 70 72 20'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 7:72 muhur EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, araç tanımı farkı; muhur_el hayır): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in range(70, 73)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 70 72 20'): KALAN_P",
 "ölçüm aktör: 7:70, 7:71 ve 7:72 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:70 soru, emir, şart — COND 1 'in' (14.), IMPV 1 'fe'tinâ' (11.), INTG 1 'e-ci'tenâ' (2.); "
 "7:71 soru, emir — CERT 1 'qad' (2.), IMPV 1 'fe'ntazirû' (21.), INTG 1 'e-tucâdilûnenî' (9.), NEG 1 'mâ' (15.); 7:72 haber — NEG 1 've mâ' (11.)",
 "morph REL ('mâ' 7:70 7., 'bi-mâ' 7:70 12., 've'llezîne' 7:72 2., 'llezîne' 7:72 8.), PRP ('li-na'bude' 7:70 3.), RSLT ('fe'tinâ' 7:70 11.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:70, 7:71 ve 7:72 yıldız yok",
 "fâsıla: 7:69 ن → 7:70 ن (" + _F[0] + ") → 7:71 ن (" + _F[1] + ") → 7:72 ن (" + _F[2] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:70 11:32, 14:10, 46:22 (emsal olarak basıldı), okunmuş 1 ayet ve okunmamış 1 ayet (sûre içi 1); 7:71 12:40, 53:23 (emsal olarak basıldı); "
 "7:72 7:64, 21:77 (basılmış), okunmamış 2 ayet (sûre içi 2)",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:70 'etâ mâ ve'ade in kâne min' süzgeç GEÇER, 'in kâne min sâdiq' süzgeç GEÇER, 'in kâne min' süzgeç GEÇER; 7:71 nakarat3 kalıbı yok; "
 "7:72 'ellezî kezzebe âye' süzgeç GEÇER, 'encâ ellezî ma'a' süzgeç GEÇMEZ; sûre içi eşler — bölüm 7-1 bloğundaki Nûh kıssası ayetleri (basılmış) ve basılmamış eşler",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:70 3MP ('qâlû' — gönderge 7:66 2. kelime), söz içi konuşan 1P ('na'bude', 'nezera'; ekler 'ci'tenâ', 'âbâ'unâ', 'fe'tinâ', 'te'idunâ'), söz içi muhatap 2MS ('ci'tenâ', 'fe'tinâ', 'te'idunâ', 'kunte'), 3MS ('kâne', 'ya'budu' — söz içi, fiil uyumu, fail 10. kelime; ek 'vahdehû' — söz içi, gönderge 'llâhe' 4. kelime); "
 "7:71 3MS ('qâle' — gönderge 7:65 4. kelime; 'veqa'a' — söz içi, fiil uyumu, fail 7. kelime; 'nezzele' — söz içi, fiil uyumu, fail 17. kelime), söz içi muhatap 2MP ('tucâdilûne', 'semmeytumûhâ', 'ntazirû'; zamir 'entum'; ekler ''aleykum', 'rabbikum', 'âbâ'ukum', 'me'akum'), söz içi konuşan 1S eki ('tucâdilûnenî', 'innî'), 3FS eki ('semmeytumûhâ', 'bihâ' — söz içi, gönderge 'esmâ'in' 11. kelime); "
 "7:72 konuşan 1P ('enceynâhu', 'qata'nâ'; ekler 'minnâ', 'bi-âyâtinâ'), 3MS eki ('enceynâhu', 'me'ahû' — gönderge 7:65 4. kelime), 3MP ('kezzebû', 'kânû' — gönderge 'llezîne' 8. kelime)",
 "7:70-72 gönderge zinciri: 7:70 'qâlû' göndergesi 7:66 2. kelimedeki ileri gelenler; 7:70 söz içi muhatap 2MS Hûd; 7:71 'qâle' göndergesi 7:65 4. kelimedeki Hûd; 7:71 söz içi muhatap 2MP kavmi; 7:72 'enceynâhu' ve 'me'ahû' göndergesi 7:65 4. kelimedeki Hûd; 7:72 'kezzebû', 'kânû' göndergesi 'llezîne' (8. kelime) (okuma)",
 "edilgen: 7:70, 7:71 ve 7:72 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:70 söz içi 2-17. kelime ('qâlû' 1. kelime ardından; ayet içinde kapanıyor); 7:71 söz içi 2-25. kelime ('qâle' 1. kelime ardından; ayet içinde kapanıyor); 7:72 söz yok; "
 "REM sapması 7:71 (21. kelime) — söz içi sonuç 'fe'si, emir cümlesi başı; "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 70 72 20' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 7:70 've nezera' (6.) CONJ, 'fe'tinâ' (11.) RSLT; 7:71 've ğadabun' (8.) CONJ, 've âbâ'ukum' (14.) CONJ, 'fe'ntazirû' (21.) REM; 7:72 'fe-enceynâhu' (1.) REM, 've'llezîne' (2.) CONJ, 've qata'nâ' (6.) CONJ, 've mâ' (11.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:70, 7:71 ve 7:72 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 70 72 20'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:70 (11:32, 14:10, 46:22), 7:71 (12:40, 53:23); D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:70 عبد ×2, كون ×2; 7:71 سمو ×2, نظر ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: bloğun emsal dosyasında olmayan basılmış eş (önceki bloklarda basılmış ya da sûre içi), bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:70 söz açılır / kapanır, şart → cevap (COND 'in' 14. kelime; cevap 'fe'tinâ' 11. kelime — öne alınmış), şahıs sayısında beraberlik (1P 6 · 2MS 6 — ölçüm baskın 2), şahıs geçişi yok, edim geçişi soru, emir → soru, emir, şart; 7:71 söz açılır / kapanır, şahıs geçişi yok, edim geçişi soru, emir, şart → soru, emir; "
 "7:72 bölüm kapanışı, şahıs sayısında beraberlik (1P 6 · 3. şahıs 6 — ölçüm baskın 1), şahıs geçişi 2 → 1, edim geçişi soru, emir → haber; ölçüm iltifât 7:70-72 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:70 'e-ci'tenâ li-na'bude'llâhe' — soru edatı ile mazi, amaç lâmı ile muzâri ve lafız (morph INTG + PERF + PRP + IMPF + PN); 7:71 'qad veqa'a 'aleykum min rabbikum' — tahkik edatı ile mazi ve tümleçler (morph CERT + PERF + P + P + N); "
 "7:72 'fe-enceynâhu ve'llezîne me'ahû' — istînâf, mazi ve atıfla ism-i mevsûl (morph REM + PERF + CONJ + REL + LOC)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:70 11-13. kelime — 11:32 ve 46:22 ile harekesiz eş (sayım: 'say 7:70 11-13'); 7:70 8-11. kelime — 14:10 ile lemma dizisi eşi (sayım: 'dizi 7 70 8 11'); "
 "7:71 11-14. kelime — 12:40 ve 53:23 ile harekesiz eş (sayım: 'say 7:71 11-14'); 7:70 kök عبد ve كون ikilemesi; 7:71 kök سمو ve نظر ikilemesi; geniş eşli sayımlar: 'say 7:70 11-17', 'say 7:70 11-16'",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 20'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'fe'tinâ bi-mâ te'idunâ' 7:70 'bize vaat ettiğin şeyi getir' / 11:32 'bizi tehdit ettiğin şeyi getir' (emsal metninde) — çakışma — tam okuma sonu ('vaat et-' / 'tehdit et-' — ve'ade karşılığı); "
 "'fe'tinâ bi-mâ te'idunâ' 7:70 'bize vaat ettiğin şeyi getir' / 46:22 'bize vaat ettiğin şeyi getir' (emsal metninde) — çakışma değil; "
 "'in kunte mine's-sâdiqîn' 7:70 'Doğru söyleyenlerdensen' / 11:32 'Doğru söyleyenlerdensen' (emsal metninde) — çakışma değil; "
 "'âbâ'unâ' 7:70 'atalarımızın' / 14:10 'atalarımızın' (emsal metninde) — çakışma değil; "
 "'mine's-sâdiqîn' 7:70 'Doğru söyleyenlerden' / 46:22 'Doğrulardan' (emsal metninde) — çakışma — tam okuma sonu ('doğru söyleyen' / 'doğru' — sâdiq karşılığı); "
 "'esmâ'in semmeytumûhâ entum ve âbâ'ukum' 7:71 'sizin ve atalarınızın taktığınız adlar' / 12:40 'sizin ve atalarınızın taktığı adlar' (emsal metninde) — çakışma — tam okuma sonu ('-dığınız' / '-dığı' — sıfat-fiil şahıs eki); "
 "'entum ve âbâ'ukum' 7:71 'sizin ve atalarınızın' / 53:23 'sizin ve atalarınızın' (emsal metninde) — çakışma değil; "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:70 'qâlû' PERF — meal 'Dediler'; 'ci'tenâ' PERF ('e' ile) — meal 'geldin'; 'na'bude' IMPF SUBJ ('li' ile) — meal 'kulluk edelim'; 'nezera' IMPF SUBJ — meal 'bırakalım'; "
 "'kâne' PERF — meal 'olduklarını'; 'ya'budu' IMPF IND — meal 'kulluk etmekte'; 'fe'tinâ' IMPV — meal 'getir'; 'te'idunâ' IMPF IND — meal 'vaat ettiğin'; 'kunte' PERF ('in' ile) — meal 'söyleyenlerdensen'; "
 "7:71 'qâle' PERF — meal 'Dedi'; 'veqa'a' PERF ('qad' ile) — meal 'düştü'; 'tucâdilûnenî' IMPF IND ('e' ile) — meal 'tartışıyorsunuz'; 'semmeytumûhâ' PERF — meal 'taktığınız'; 'nezzele' PERF ('mâ' ile) — meal 'indirmediği'; 'fe'ntazirû' IMPV — meal 'bekleyin'; "
 "7:72 'enceynâhu' PERF — meal 'kurtardık'; 'qata'nâ' PERF — meal 'kestik'; 'kezzebû' PERF — meal 'yalanlayanların'; 'kânû' PERF ('mâ' ile) — meal 'değildi'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle; IMPF IND geniş zaman karşılığı her blokta sapma sayılır — sûre 7 bölüm 3 denetimi kuralı 3): 'na'bude', 'nezera' IMPF 7:70'te istek kipi ('-elim', '-alım') ile; 'kâne' PERF 7:70'te sıfat-fiil ('-duklarını') ile; 'ya'budu' IMPF 7:70'te sürerlik ('-mekte') ile; "
 "'te'idunâ' IMPF 7:70'te sıfat-fiil ('-tiğin') ile; 'kunte' PERF 7:70'te şart ('-sen') ile; 'tucâdilûnenî' IMPF 7:71'de şimdiki zaman ('-ıyorsunuz') ile; 'semmeytumûhâ' PERF 7:71'de sıfat-fiil ('-tığınız') ile; 'nezzele' PERF 7:71'de sıfat-fiil ('-mediği') ile; 'kezzebû' PERF 7:72'de sıfat-fiil ('-yanların') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): 'ellezîne' (REL: '-anları' / '-anların' / '-en') — çakışma değil (sıfat-fiil çekimi); 'li' (PRP: 'diye' / 'için') — çakışma değil (amaç lâmı; söz içi soruda 'diye'); 'mâ' (NEG: 'değil' / olumsuzluk eki / 'yok') — çakışma değil (isim, fiil ve varlık olumsuzluğu); 'mâ' (REL: '-dukları' / 'şeyi' / 'şeyleri') — çakışma değil (sıfat-fiil, ad); ''alâ' (yönelme eki / 'aracılığıyla' / 'için') — çakışma değil (fiil yönetimi); 'bi' ('-le' / belirtme eki / yönelme eki / bulunma eki) — çakışma değil (fiil yönetimi); 'fî' ('hakkında' / 'içinde' / bulunma eki) — çakışma değil (konu ve yer); 'hû' ('onunla' / karşılıksız / 'O'ndan') — çakışma değil (tümleç, tamlama); 'kum' ('size' / 'sizinle' / iyelik eki / 'sizi' / 'sizin' / karşılıksız) — çakışma değil (tümleç, tamlama); 'nâ' ('bize' / iyelik eki / karşılıksız / 'biz') — çakışma değil (tümleç, tamlama)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 70 72 20'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:70, 7:71 ve 7:72 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:70, 7:71 ve 7:72 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök قول 7:70 ('qâlû') ve 7:71 ('qâle') ile bölüm içi; kök أبو 7:70 ('âbâ'unâ') ve 7:71 ('âbâ'ukum') ile bölüm içi; kök أله 7:70 ('llâhe') ve 7:71 ('llâhu') ile bölüm içi; kök كون 7:70 ('kâne', 'kunte') ve 7:72 ('kânû') ile bölüm içi; "
 "bölümün önceki bloklarıyla ortak kökler: أله (7:59, 7:62, 7:65, 7:69 / 7:70, 7:71), أمن (7:68 / 7:72), أيي (7:64 / 7:72), جيأ (7:63, 7:69 / 7:70), ربب (7:61, 7:62, 7:63, 7:67, 7:68, 7:69 / 7:71), رحم (7:63 / 7:72), عبد (7:59, 7:65 / 7:70), قول (7:59, 7:60, 7:61, 7:65, 7:66, 7:67 / 7:70, 7:71), كذب (7:64, 7:66 / 7:72), كون (7:64 / 7:70, 7:72), نجو (7:64 / 7:72); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 7-3 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 18, 19 ve 20; bölüm kapanışı bu blokta; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b20/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 70 72 20'; lem_bozuk.py 20 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 70 72 → AYN_SONUC; sunum/bolum4_kurallar.py 70 72 20 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 70 72 20 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 43)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 20 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('etâ', 'mâ', 've'ade', 'in', 'kâne', 'min', 'sâdiq', ''abede', 'âbâ'', 'ism', 'semmâ', 'nezzele', 'allâh', 'sultân', 'ellezî', 'kezzebe', 'âye', 'encâ', 'ma'a'); joker '_' dizi lemma dizisinde boş öğe olan zamir ve önek lemmalı kelimelerde ('entum' 7:71 13., 'bihâ' 7:71 18.); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

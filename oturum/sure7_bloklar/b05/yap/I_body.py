_OL = [l.replace('**', '') for l in open('/home/claude/b05/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b05/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 18), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
def _esc(t):
    for c in '.()[]|+': t = t.replace(c, '\\' + c)
    return t
_AK1 = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[0]).group(0))
_AK2 = _esc(re.search(r'aktör: adlı .*?rol fail\)', _OL[1]).group(0))
_E2 = _esc(re.search(r'esit2 → 2:35 oran \S+ kademe BENZER', _OL[0]).group(0))
_SI = _esc(re.search(r'sayı işareti \S+', _OL[0]).group(0))
for _k, _v in (('_AK1', _AK1), ('_AK2', _AK2), ('_E2', _E2), ('_SI', _SI)): _MB = _MB.replace('" + %s + "' % _k, _v)
I = [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta sunum/bolum16_kurallar.py (kural 1) blok 3'te eklenen ayrı zamir sınırını daraltır — harfi cere bitişik zamir ('lehume' 7:20 2. kelime) ayrı zamir sayılmaz, 'fe-vesvese' fiilinin 3. kelimedeki faili aranır; sunum/bolum4_kurallar.py (kural 9) ile sunum/bolum7_kurallar.py (kural 3) şahıs etiketi listesine 2MD ve 2FD eklendi — 7:19 6. kelime 'fe-kulâ' morph 2MD; sunum/edat_etiket.py (bölüm 15 denetimi kuralı 15) zamir listesine 'kumâ' eklendi — 7:20 ve 7:21 ikil muhatap eki; yeni kök yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 382",
 "geriye dönük koşu (sûre 7 bölüm 1 kapanışı, komut 'python3 sunum/geriye_donuk.py b02k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 19 21 05'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:19, 7:20 ve 7:21 esmâ yok; 7:20 Rab (14. kelime); 7:19 ve 7:21 lafız ve Rab yok; 7:20 lafız yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 19 21 05'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in (19, 20, 21)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 19 21 05'): KALAN_P",
 "ölçüm aktör: 7:19 '{{1|" + _AK1 + "}}' (A1'de 'âdemu' ve 'l-cennete'); 7:20 '{{2|" + _AK2 + "}}' (A1'de 'ş-şeytânu' — 'fe-vesvese' faili); 7:21 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:19 emir, yasak, nida — IMPV 2 'skun' (2.), 'kulâ' (6.), PRO 1 'lâ' (10.), VOC 1 'yâ' (1.); ölçüm biçim DIKKAT + NEHY (D2'de yazılmadı); "
 "7:20 haber — NEG 1 'mâ' (12.), RES 1 'illâ' (18.); ölçüm biçim DIKKAT + HASR (D2'de yazılmadı); 7:21 haber — EMPH 1 'le-mine' (4.; 'le'); ölçüm biçim QASEM (D2'de yazılmadı); "
 "morph CAUS ('fe-tekûnâ' 7:19 14.), ATT ('hâzihi' 7:19 12., 7:20 16.), REM ('fe-vesvese' 7:20 1.), PRP ('li-yubdiye' 7:20 4.), SUB ('en' 7:20 19.), ACC ('innî' 7:21 2.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:19, 7:20 ve 7:21 yıldız yok",
 "fâsıla: 7:18 ن → 7:19 ن (" + _F[0] + ") → 7:20 ن (" + _F[1] + ") → 7:21 ن (" + _F[2] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:19 2:35 (emsal olarak basıldı), okunmuş 1 ayet ve okunmamış 1 ayet (sûre içi 1); ölçüm esit2 7:19 → 2:35 (kademe BENZER); 7:20 xref yok; 7:21 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok (7:19, 7:20 ve 7:21 ölçümünde nakarat3 alanı boş)'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:19, 7:20 ve 7:21 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:19 muhatap 2MS ('skun', 'ente' — söz içi; ek 've zevcuke' — söz içi), muhatap 2MD ('fe-kulâ' — söz içi), muhatap 2D ('şi'tumâ', 'taqrabâ', 'fe-tekûnâ' — söz içi; ek 'fe-kulâ' — söz içi), aktör adlı 'âdemu' ve 'l-cennete'; "
 "7:20 3MS ('fe-vesvese' — fiil uyumu, fail 3. kelime; 'li-yubdiye', 've qâle' — gönderge 'ş-şeytânu' 3. kelime; 'vûriye' — edilgen, naib-i faili 'mâ' 6. kelime; 'nehâkumâ' — söz içi, fiil uyumu, fail 14. kelime), 3D eki ('lehume', 'lehumâ', ''anhumâ', 'sev'âtihimâ' — gönderge 7:19 6. kelime), "
 "muhatap 2D ('tekûnâ', 'tekûnâ' — söz içi; ekler 'nehâkumâ', 'rabbukumâ' — söz içi), aktör adlı 'ş-şeytânu'; "
 "7:21 3MS ('ve qâsemehumâ' — gönderge 7:20 3. kelime), 3D eki ('ve qâsemehumâ' — gönderge 7:19 6. kelime), konuşan 1S eki ('innî' — söz içi), muhatap 2D eki ('lekumâ' — söz içi)",
 "7:19-21 gönderge zinciri: 7:19 nida ile muhatap 'âdemu' (1. kelime), 4. kelimeyle eşi katılır ve 6. kelimeden başlayarak muhatap ikil; 7:20 ve 7:21 3D ekleri 7:19 6. kelimeye (iki muhatap); 7:20 3MS fiiller 'ş-şeytânu' (3. kelime), 7:21 fiili de 7:20 3. kelimeye; 7:20 ve 7:21 söz içi muhatap 2D yine 7:19 muhatapları, söz içi konuşan 1S şeytan; 7:20 'rabbukumâ' (14. kelime) söz içinde anılır (okuma)",
 "edilgen: 7:20 'vûriye' (7. kelime; naib-i faili 'mâ') — ölçüm EDİLGEN 1/7; 7:19 ve 7:21 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:19 söz fiili olmadan söz biçimli içerik 1-16. kelime — nida 'yâ âdemu' (1.) ile; 've' (1. kelime, morph CONJ) ile 7:18'deki söze bağlanır, muhatap 7:18'den ayrı; A3'e '(söz biçimli içerik, 1. kelimeden)', A4'te 'söz açılır' / 'söz kapanır' yazılmadı (okuma); "
 "7:20 've qâle' (11.) ardından söz 12-25. kelime — ayet içi kapanış; 7:21 've qâsemehumâ' (1.) ardından söz biçimli içerik 2-5. kelime — fiil قول kökünden değil; A3'e '(söz biçimli içerik, 2. kelimeden)', A4'te 'söz açılır' / 'söz kapanır' yazılmadı (okuma); mealde 'Dedi ki:' ve 'yemin etti:' ardından tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 19 21 05' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 7:19 've yâ âdemu' (1.) CONJ, 've zevcuke' (4.) CONJ, 've lâ' (10.) CONJ; 7:20 've qâle' (11.) CONJ; 7:21 've qâsemehumâ' (1.) CONJ; "
 "'fe' konumları: 7:19 'fe-kulâ' (6.) CONJ, 'fe-tekûnâ' (14.) CAUS; 7:20 'fe-vesvese' (1.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:19 ◈B زوج ('zevcuke' 4. kelime — B2; eş anlamında, üreme anlamı yok (okuma)), 7:19 ◈B شجر ('ş-şecerate' 13. kelime — B1); 7:20 ◈B شجر ('ş-şecerati' 17. kelime — B1); 7:21 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 19 21 05'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:19 (2:35); 7:20 ve 7:21 bağ yok; D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:20 كون ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:19 söz biçimli içerik (A4'te söz kaydı yok), nidâ ('yâ âdemu' 1. kelime), cevap edatı kapsam dışı (morph CAUS 'fe-tekûnâ' 14. kelime), muhatap geçişi 2MS → 2D (ayet içi), şahıs geçişi 3 → 2, edim geçişi emir, şart → emir, yasak, nida; 7:20 söz açılır (12. kelime), söz kapanır (25. kelime, ayet içi), şahıs geçişi yok, şahıs sayısında toplam farkı (2D 6 · 3. şahıs 9 — ölçüm baskın 2), edim geçişi emir, yasak, nida → haber; "
 "7:21 söz biçimli içerik (A4'te söz kaydı yok), şahıs geçişi 2 → 3, edim geçişi yok; "
 "ölçüm iltifât 7:19-21 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:19 've yâ âdemu' — atıflı nida (morph CONJ + VOC); 7:19 'ente ve zevcuke' — gizli özneyi pekiştiren ayrı zamir ve ona bağlanan ad (morph PRON + CONJ); 7:19 'fe-tekûnâ' — yasağın sonucunu bildiren 'fe' (morph CAUS + SUBJ); "
 "7:20 'li-yubdiye' — gerekçe lâmı (morph PRP + SUBJ); 7:20 'mâ vûriye 'anhumâ min sev'âtihimâ' — ilgi cümlesi ve açıklayıcı 'min' (morph REL + PASS); 7:20 'mâ nehâkumâ' ve 'illâ en tekûnâ' — olumsuzluk ve hasr (morph NEG + RES + SUB); 7:21 'innî lekumâ le-mine'n-nâsihîn' — tekitli isim cümlesi (morph ACC + EMPH)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:19 8-16. kelime — 2:35 ile harekesiz eş (sayım: 'say 7:19 8-16'); 7:19 2-5. kelime — 2:35 ile harekesiz eş (sayım: 'say 7:19 2-5'); 7:19 6. kelimenin öneki 2:35'tekinden ayrı (sayım: 'dizi 7 19 1 6'); "
 "7:20 kök كون ikilemesi; 7:19 ile 7:20 arasında 'hâzihi'ş-şecera' yinelenir (7:19 12-13. ve 7:20 16-17. kelime)",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 05'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'skun ente ve zevcuke'l-cennete' 7:19 'sen ve eşin bahçede oturun' / 2:35 'sen ve eşin bahçede oturun' (emsal metninde) — çakışma değil (bayt eşit); "
 "'haysu şi'tumâ ve lâ taqrabâ hâzihi'ş-şecerate fe-tekûnâ mine'z-zâlimîn' 7:19 'dilediğiniz yerden yiyin; ama şu ağaca yaklaşmayın, yoksa zalimlerden olursunuz' / 2:35 'dilediğiniz yerden bol bol yiyin; ama şu ağaca yaklaşmayın, yoksa zalimlerden olursunuz' (emsal metninde) — çakışma — tam okuma sonu (emsalde araya giren 'rağaden' karşılığı 'bol bol'; alıntı 6. ve 7. kelime karşılıklarını da taşıyor); "
 "'ve lâ taqrabâ hâzihi'ş-şecerate' 7:19 'ama şu ağaca yaklaşmayın' / 2:35 'ama şu ağaca yaklaşmayın' (emsal metninde) — çakışma değil (bayt eşit); "
 "'fe-tekûnâ mine'z-zâlimîn' 7:19 'yoksa zalimlerden olursunuz' / 2:35 'yoksa zalimlerden olursunuz' (emsal metninde) — çakışma değil (bayt eşit); "
 "'ve lâ taqrabâ hâzihi'ş-şecerate fe-tekûnâ mine'z-zâlimîn' 7:19 'ama şu ağaca yaklaşmayın, yoksa zalimlerden olursunuz' / 2:35 'ama şu ağaca yaklaşmayın, yoksa zalimlerden olursunuz' (emsal metninde) — çakışma değil (bayt eşit); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:19 'skun' IMPV — meal 'oturun'; 'kulâ' IMPV — meal 'yiyin'; 'şi'tumâ' PERF — meal 'dilediğiniz'; 'taqrabâ' IMPF JUS ('lâ' ile) — meal 'yaklaşmayın'; 'tekûnâ' IMPF SUBJ ('fe' ile) — meal 'olursunuz'; "
 "7:20 'vesvese' PERF — meal 'verdi'; 'yubdiye' IMPF SUBJ ('li' ile) — meal 'açmak'; 'vûriye' PERF PASS — meal 'gizlenen'; 'qâle' PERF — meal 'Dedi'; 'nehâ' PERF ('mâ' ile) — meal 'yasakladı'; 'tekûnâ' IMPF SUBJ (20. kelime; 'en' ile) — meal 'olursunuz'; 'tekûnâ' IMPF SUBJ (23. kelime) — meal 'olursunuz'; "
 "7:21 'qâseme' PERF — meal 'etti'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle): 'şi'tumâ' PERF 7:19'da sıfat-fiil ('-diğiniz') ile; 'tekûnâ' IMPF SUBJ 7:19'da ve 7:20'de geniş zaman ('-ursunuz') ile; 'yubdiye' IMPF SUBJ 7:20'de ad-fiil ('-mak') ile; 'vûriye' PERF 7:20'de sıfat-fiil ('-en') ile; 'nehâ' PERF 7:20'de 'mâ' ve 'illâ' ile olumlu geçmiş ('ancak … yasakladı') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): 'illâ' ('ancak' / 'hariç') — çakışma değil (hasr edatı morph RES, istisna edatı morph EXP); 'fe' (REM: 'Derken' / 'Hemen' / karşılıksız) — çakışma değil (anlatı geçişi, emir önünde ivedilik, Türkçe sıralama); 've' (CONJ: 'ama' / 've' / 'ise' / karşılıksız) — çakışma değil (yasak önünde karşıtlık, atıf, Türkçe sıralama)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 19 21 05'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:20 tarayıcı adayı (kök شجر; B_ta’lîl, D_yeti) çıpa değil — anlatı öğesi, doğa iddiası yok; 7:19 ve 7:21 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:20 ('li-yubdiye' / 'vûriye'); 7:19 ve 7:21 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök شجر 7:19 ('ş-şecerate') ve 7:20 ('ş-şecerati'); kök كون 7:19 ('fe-tekûnâ') ve 7:20 ('tekûnâ', 'tekûnâ'); kök قول 7:20 ('ve qâle'), 7:14 ('qâle') ile bölüm içi; kök أدم 7:19 ('âdemu'), 7:11 ('li-âdeme') ile bölüm içi; kök ملك 7:20 ('melekeyni'), 7:11 ('li'l-melâ'iketi') ile bölüm içi; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 2-3 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 3, 4, 5 ve 6; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b05/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 19 21 05'; lem_bozuk.py 05 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 19 21 → AYN_SONUC; sunum/bolum4_kurallar.py 19 21 05 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 19 21 05 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 37)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 5 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('âdem', 'sekene', 'zevc', 'cenne', 'ekele', 'haysu', 'şâ'e', 'lâ', 'yaqrabu' (morph LEM ham biçim), 'zâ', 'şecera', 'kâne', 'min', 'zâlim'); joker '_' yalnız lemmasız 'ente' öğesinde ('dizi 7 19 2 5', 'dizi 7 19 1 6'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

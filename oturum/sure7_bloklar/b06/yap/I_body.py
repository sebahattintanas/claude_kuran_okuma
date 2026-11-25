_OL = [l.replace('**', '') for l in open('/home/claude/b06/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b06/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 21), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
def _esc(t):
    for c in '.()[]|+': t = t.replace(c, '\\' + c)
    return t
_AK1 = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[0]).group(0))
_ES1 = _esc(re.search(r'esmâ \S+ 28\. sırada, SON konum, MÜHÜRSÜZ', _OL[0]).group(0))
for _k, _v in (('_AK1', _AK1), ('_ES1', _ES1)): _MB = _MB.replace('" + %s + "' % _k, _v)
I = [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta araç kuralı değişmedi; blok 5'te sunum/bolum16_kurallar.py (kural 1), sunum/bolum4_kurallar.py (kural 9), sunum/bolum7_kurallar.py (kural 3) ve sunum/edat_etiket.py düzeltmeleri önceki commit'te; yeni kök yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 388",
 "geriye dönük koşu (sûre 7 bölüm 1 kapanışı, komut 'python3 sunum/geriye_donuk.py b02k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 22 25 06'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:22 'inne'ş-şeytâne lekumâ 'aduvvun mubîn' (24-28. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (şeytanın düşmanlık sıfatı) (yamalar/esma_el_7_22_25.txt); 7:23, 7:24 ve 7:25 esmâ yok; 7:22 Rab (16. kelime); 7:23 Rab (2. kelime); 7:24 ve 7:25 lafız ve Rab yok; 7:22 ve 7:23 lafız yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 22 25 06'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 7:22 muhur EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, araç tanımı farkı; muhur_el hayır): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in (22, 23, 24, 25)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 22 25 06'): KALAN_P",
 "ölçüm aktör: 7:22 '{{1|" + _AK1 + "}}' (A1'de 'l-cenneti' ve 'ş-şeytâne'); 7:23, 7:24 ve 7:25 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:22 soru — INTG 1 'e-lem' (17.; 'e'), NEG 1 'e-lem' (17.; 'lem'); "
 "7:23 şart — COND 1 'in' (5.), EMPH 2 'le-nekûnenne' (10.; 'le' ve pekiştirme nûnu), NEG 1 'lem' (6.); 7:24 emir — IMPV 1 'hbitû' (2.); 7:25 haber — kip yok; "
 "morph REM ('fe-lemmâ' 7:22 3., 've nâdâhumâ' 7:22 15.), DIST ve ADDR ('tilkume' 7:22 20.), ACC ('inne' 7:22 24.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:22 ★ (kaynak n, z=1,65); 7:23, 7:24 ve 7:25 yıldız yok",
 "fâsıla: 7:21 ن → 7:22 ن (" + _F[0] + ") → 7:23 ن (" + _F[1] + ") → 7:24 ن (" + _F[2] + ") → 7:25 ن (" + _F[3] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:22 20:121 (emsal olarak basıldı); 7:23 okunmuş 3 ayet; 7:24 2:36 (emsal olarak basıldı); 7:25 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:23 'ğafera _ rahime' süzgeç GEÇMEZ, 'kâne min xâsir' süzgeç GEÇMEZ; 7:22, 7:24 ve 7:25 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:22 3MS ('fe-dellâhumâ' — gönderge 7:20 3. kelime; 've nâdâhumâ' — fiil uyumu, fail 16. kelime), 3D eki ('fe-dellâhumâ', 'lehumâ', 'sev'âtuhumâ', 'yaxsifâni', ''aleyhimâ', 've nâdâhumâ', 'rabbuhumâ' — gönderge 7:19 6. kelime), 3MD ('zâqe', 've tafiqâ', 'yaxsifâni' — gönderge 7:19 6. kelime), 3FS ('bedet' — fiil uyumu, fail 8. kelime), "
 "konuşan 1S ('enhekumâ', 've aqul' — söz içi), muhatap 2D eki ('enhekumâ', 'lekumâ', 'lekumâ' — söz içi), aktör adlı 'l-cenneti' ve 'ş-şeytâne'; "
 "7:23 3MD ('qâlâ' — gönderge 7:19 6. kelime), konuşan 1P ('zalemnâ', 'le-nekûnenne' — söz içi; ekler 'rabbenâ', 'enfusenâ', 'lenâ', 've terhamnâ' — söz içi), muhatap 2MS ('teğfir' — söz içi), 3FS ('ve terhamnâ' — söz içi; morph etiketi, okuma muhatap 2MS); "
 "7:24 3MS ('qâle' — gönderge 7:22 16. kelime), muhatap 2MP ('hbitû' — söz içi; ekler 'ba'dukum', 've lekum' — söz içi); "
 "7:25 3MS ('qâle' — gönderge 7:22 16. kelime), 3FS eki ('fîhâ', 've fîhâ', 've minhâ' — söz içi; gönderge 7:24 8. kelime), muhatap 2MP ('tahyevne', 'temûtûne' — söz içi; 'tuxracûn' — söz içi; edilgen, naib-i faili zamir)",
 "7:22-25 gönderge zinciri: 7:22 'fe-dellâhumâ' (1. kelime) fiili 7:20 3. kelimeye (şeytan); 7:22 ve 7:23 ikil 3. şahıs fiil ve ekleri 7:19 6. kelimeye (iki muhatap); 7:22 söz içi konuşan 1S 'rabbuhumâ' (16. kelime), muhatap 2D yine o iki kişi; 7:23 söz içi konuşan 1P o iki kişi, muhatap 2MS 'rabbenâ' (2. kelime); "
 "7:23 've terhamnâ' (9. kelime) morph etiketi 3FS, okuma 7. kelimeyle eş özne; 7:24 ve 7:25 'qâle' fiilleri 7:22 16. kelimeye; 7:24 söz içi muhatap çoğul (2MP) — ikilden çoğula geçiş, kapsamı metinde adsız; 7:25 3FS ekleri 7:24 8. kelimeye ('l-ardi') (okuma)",
 "edilgen: 7:25 'tuxracûn' (7. kelime; naib-i faili zamir) — ölçüm EDİLGEN 1/4; 7:22, 7:23 ve 7:24 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:22 've nâdâhumâ rabbuhumâ' (15-16.) ardından söz biçimli içerik 17-28. kelime — fiil قول kökünden değil; A3'e '(söz biçimli içerik, 17. kelimeden)', A4'te 'söz açılır' / 'söz kapanır' yazılmadı (okuma); "
 "7:22 içteki 've aqul lekumâ' (22-23.) ardından aktarılan söz 24-28. kelime — dış sözle birlikte ayet sonunda kapanır (okuma); 7:23 'qâlâ' (1.) ardından söz 2-12. kelime — ayet içi kapanış; 7:24 'qâle' (1.) ardından söz 2-12. kelime — ayet içi kapanış; 7:25 'qâle' (1.) ardından söz 2-7. kelime — ayet içi kapanış; "
 "mealde 'seslendi:', 'demedim mi:', 'Dediler ki:' ve 'Dedi ki:' ardından tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 22 25 06' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 7:22 've tafiqâ' (9.) CONJ, 've nâdâhumâ' (15.) REM, 've aqul' (22.) CONJ; 7:23 've in' (5.) CONJ, 've terhamnâ' (9.) CONJ; 7:24 've lekum' (6.) CONJ, 've metâ'un' (10.) CONJ; 7:25 've fîhâ' (4.) CONJ, 've minhâ' (6.) CONJ; "
 "'fe' konumları: 7:22 'fe-dellâhumâ' (1.) CONJ, 'fe-lemmâ' (3.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:22 ◈B شجر ('ş-şecerate' 5. kelime, 'ş-şecerati' 21. kelime — B1); 7:24 ◈K أرض ('l-ardi' 8. kelime — K1), 7:24 ◈K حين ('hîn' 12. kelime — K2); 7:25 ◈B حيي ('tahyevne' 3. kelime — B4), 7:25 ◈B موت ('temûtûne' 5. kelime — B4); 7:23 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 22 25 06'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:22 (20:121); 7:24 (2:36); 7:23 ve 7:25 bağ yok; D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:22 شجر ×2; 7:24 بعض ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:22 söz biçimli içerik (A4'te söz kaydı yok), şahıs geçişi yok, edim geçişi haber → soru; 7:23 söz açılır (2. kelime), söz kapanır (12. kelime, ayet içi), şart → cevap (ayet içi; COND 'in' 5. kelime), şahıs geçişi 3 → 1, edim geçişi soru → şart; "
 "7:24 söz açılır (2. kelime), söz kapanır (12. kelime, ayet içi), şahıs geçişi 1 → 2, edim geçişi şart → emir; 7:25 söz açılır (2. kelime), söz kapanır (7. kelime, ayet içi), şahıs geçişi yok, edim geçişi emir → haber, bölüm kapanışı; "
 "ölçüm iltifât 7:22-25 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:22 'fe-lemmâ zâqe'ş-şecerate' — zaman bağlacıyla açılan yan cümle (morph REM + T + PERF); 7:22 've tafiqâ yaxsifâni' — başlama fiili ve ardındaki muzâri (morph CONJ + PERF + IMPF); 7:22 'e-lem enhekumâ' — olumsuz soru (morph INTG + NEG + JUS); "
 "7:23 've in lem teğfir lenâ' — olumsuz şart (morph CONJ + COND + NEG + JUS); 7:23 'le-nekûnenne' — tekitli muzâri, şartın cevabı (morph EMPH + IMPF); 7:25 'fîhâ tahyevne' — öne alınmış harfi cerli tümleç (morph P + IMPF)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:22 8-14. kelime — 20:121 ile harekesiz eş (sayım: 'say 7:22 8-14'); 7:24 2-12. kelime — 2:36 ile harekesiz eş (sayım: 'say 7:24 2-12'); 7:24 1. kelimenin çekimi 2:36'dakinden ayrı (sayım: 'dizi 7 24 1 12'); "
 "7:22 kök شجر ikilemesi; 7:24 kök بعض ikilemesi; 7:23 10-12. kelime sûre içinde okunmamış 1 ayetle harekesiz eş (sayım: 'say 7:23 10-12')",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 06'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'lehumâ sev'âtuhumâ' 7:22 'çirkin yerleri kendilerine' / 20:121 'çıplaklıkları kendilerine' (emsal metninde) — çakışma — tam okuma sonu ('sev'e' karşılığı 'çirkin yer' / 'çıplaklık'); "
 "'ve tafiqâ yaxsifâni 'aleyhimâ min varaqi'l-cenneti' 7:22 've bahçe yaprağından üzerlerine yamamaya koyuldular' / 20:121 've cennet yaprağından üzerlerine yamamaya koyuldular' (emsal metninde) — çakışma — tam okuma sonu ('cenne' karşılığı 'bahçe' / 'cennet'); "
 "'sev'âtuhumâ ve tafiqâ yaxsifâni 'aleyhimâ min varaqi'l-cenneti' 7:22 'çirkin yerleri kendilerine göründü ve bahçe yaprağından üzerlerine yamamaya koyuldular' / 20:121 'çıplaklıkları kendilerine göründü ve cennet yaprağından üzerlerine yamamaya koyuldular' (emsal metninde) — çakışma — tam okuma sonu ('sev'e' ve 'cenne' karşılıkları; alıntı 6. ve 7. kelime karşılıklarını da taşıyor); "
 "'ba'dukum li-ba'din 'aduvvun' 7:24 'birbiriniz için düşmansınız' / 2:36 'birbiriniz için düşmansınız' (emsal metninde) — çakışma değil (bayt eşit); "
 "'hbitû ba'dukum li-ba'din 'aduvvun' 7:24 'İnin; birbiriniz için düşmansınız' / 2:36 'İnin; birbiriniz için düşmansınız' (emsal metninde) — çakışma değil (bayt eşit); "
 "'ve lekum fi'l-ardi musteqarrun ve metâ'un ilâ hîn' 7:24 'Yeryüzünde size bir vakte kadar kalacak yer ve geçimlik var' / 2:36 'Yeryüzünde size bir vakte kadar kalacak yer ve geçimlik var' (emsal metninde) — çakışma değil (bayt eşit); "
 "'hbitû ba'dukum li-ba'din 'aduvvun ve lekum fi'l-ardi musteqarrun ve metâ'un ilâ hîn' 7:24 'İnin; birbiriniz için düşmansınız. Yeryüzünde size bir vakte kadar kalacak yer ve geçimlik var' / 2:36 'İnin; birbiriniz için düşmansınız. Yeryüzünde size bir vakte kadar kalacak yer ve geçimlik var' (emsal metninde) — çakışma değil (bayt eşit); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:22 'dellâ' PERF — meal 'düşürdü'; 'zâqe' PERF ('lemmâ' ile) — meal 'tattıklarında'; 'bedet' PERF — meal 'göründü'; 'tafiqâ' PERF — meal 'koyuldular'; 'yaxsifâni' IMPF — meal 'yamamaya'; "
 "'nâdâ' PERF — meal 'seslendi'; 'enhe' IMPF JUS ('lem' ile) — meal 'yasaklamadım'; 'aqul' IMPF JUS — meal 'demedim'; "
 "7:23 'qâlâ' PERF — meal 'Dediler'; 'zalemnâ' PERF — meal 'zulmettik'; 'teğfir' IMPF JUS ('lem' ile) — meal 'bağışlamaz'; 'terham' IMPF JUS — meal 'etmezsen'; 'nekûnenne' IMPF ('le' ile) — meal 'oluruz'; "
 "7:24 'qâle' PERF — meal 'Dedi'; 'hbitû' IMPV — meal 'İnin'; "
 "7:25 'qâle' PERF — meal 'Dedi'; 'tahyevne' IMPF — meal 'yaşarsınız'; 'temûtûne' IMPF — meal 'ölürsünüz'; 'tuxracûn' IMPF PASS — meal 'çıkarılırsınız'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle): 'zâqe' PERF 7:22'de zarf-fiil ('-tıklarında') ile; 'yaxsifâni' IMPF 7:22'de ad-fiil ('-maya') ile; 'enhe' ve 'aqul' IMPF JUS 7:22'de 'lem' ile olumsuz geçmiş ('-madım', '-medim') ile; 'teğfir' ve 'terham' IMPF JUS 7:23'te 'in' ve 'lem' ile olumsuz geniş zaman ('-maz', '-mezsen') ile; 'nekûnenne' IMPF 7:23'te geniş zaman ('-uruz') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): 'illâ' ('ancak' / 'hariç') — çakışma değil (hasr edatı morph RES, istisna edatı morph EXP); 'fe' (REM: 'Derken' / 'Hemen' / karşılıksız) — çakışma değil (anlatı geçişi, emir önünde ivedilik, Türkçe sıralama); 'fe' (CONJ: 'Böylece' / karşılıksız) — çakışma değil (sonuç bağı, Türkçe sıralama); 've' (CONJ: 'ama' / 've' / 'ise' / karşılıksız) — çakışma değil (yasak önünde karşıtlık, atıf, Türkçe sıralama); 've' (REM: karşılıksız) — çakışma değil (anlatı geçişi cümle başıyla); 'kumâ' ('size' / 'sizin' / iyelik eki) — çakışma değil (yönelme ve tamlayan çekimi, tamlama)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 22 25 06'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:22, 7:23, 7:24 ve 7:25 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:25 ('tahyevne' / 'temûtûne'); 7:22, 7:23 ve 7:24 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök ربب 7:22 ('rabbuhumâ') ve 7:23 ('rabbenâ'); kök قول 7:22 ('ve aqul'), 7:23 ('qâlâ'), 7:24 ('qâle') ve 7:25 ('qâle'); kök عدو 7:22 (''aduvvun') ve 7:24 (''aduvvun'); kök شجر 7:22 ('ş-şecerate', 'ş-şecerati'), 7:19 ('ş-şecerate') ile bölüm içi; kök نهي 7:22 ('enhekumâ'), 7:20 ('nehâkumâ') ile bölüm içi; kök سوأ 7:22 ('sev'âtuhumâ'), 7:20 ('sev'âtihimâ') ile bölüm içi; "
 "kök شطن 7:22 ('ş-şeytâne'), 7:20 ('ş-şeytânu') ile bölüm içi; kök هبط 7:24 ('hbitû'), 7:13 ('fe'hbit') ile bölüm içi; kök خرج 7:25 ('tuxracûn'), 7:18 ('xruc') ile bölüm içi; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 2-4 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 3, 4, 5 ve 6; bölüm kapanışı bu blokta; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b06/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 22 25 06'; lem_bozuk.py 06 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 22 25 → AYN_SONUC; sunum/bolum4_kurallar.py 22 25 06 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 22 25 06 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 37)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 6 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('bedâ', 'sev'e', 'tafiqa', 'yaxsife' (morph LEM ham biçim), ''alâ', 'min', 'varaq', 'cenne', 'ğafera', 'rahime', 'kâne', 'xâsir', 'qâle', 'yehbitu' (morph LEM ham biçim), 'ba'd', ''aduvv', 'fî', 'ard', 'musteqarr', 'metâ'', 'ilâ', 'hîn'); "
 "joker '_' yalnız lemmasız öğelerde ('lehumâ' — 'dizi 7 22 6 14'; 'lenâ' — 'dizi 7 23 7 9'; 've lekum' — 'dizi 7 24 2 12', 'dizi 7 24 1 12'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

_OL = [l.replace('**', '') for l in open('/home/claude/b04/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b04/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 13), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
def _esc(t):
    for c in '.()[]|': t = t.replace(c, '\\' + c)
    return t
_AK = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[4]).group(0))
_E2 = _esc(re.search(r'esit2 → .*?BENZER · .*?BENZER', _OL[0]).group(0))
_ES = _esc(re.search(r'esmâ \S+ 15\. sırada, SON konum, MÜHÜRSÜZ', _OL[3]).group(0))
_SI = _esc(re.search(r'sayı işareti \S+', _OL[3]).group(0))
_HP = _esc(re.search(r'HAPAKS: \S+', _OL[4]).group(0))
for _k, _v in (('_AK', _AK), ('_E2', _E2), ('_ES', _ES), ('_SI', _SI), ('_HP', _HP)): _MB = _MB.replace('" + %s + "' % _k, _v)
I = [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta araç kuralı değişmedi; blok 3'te sunum/bolum16_kurallar.py (kural 1) ve sunum/bolum17_kurallar.py (kural 3) düzeltmeleri önceki commit'te; yeni kök ذأم (7:18 4. kelime 'mez'ûmen'; yamalar/yama_kok_7_14.py → kok_ekle_7.py, kok_turkce 1633; ölçüm yeniden alındı); mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 378",
 "geriye dönük koşu (sûre 7 bölüm 1 kapanışı, komut 'python3 sunum/geriye_donuk.py b02k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 14 18 04'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:17 've lâ tecidu ekserahum şâkirîn' (12-15. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (şükreden insanlar) (yamalar/esma_el_7_14_18.txt); 7:14, 7:15, 7:16 ve 7:18 esmâ yok; 7:14, 7:15, 7:16, 7:17 ve 7:18 lafız ve Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 14 18 04'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 7:17 muhur EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, araç tanımı farkı; muhur_el hayır): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in (14, 15, 16, 17, 18)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 14 18 04'): KALAN_P",
 "ölçüm aktör: 7:18 '{{5|" + _AK + "}}' (A1'de 'cehenneme'); 7:14, 7:15, 7:16 ve 7:17 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:14 emir — IMPV 1 'enzirnî' (2.); 7:15 haber — kip yok; 7:16 haber — EMPH 2 'le-aq'udenne' (4.; 'le' ve 'n'); 7:17 haber — EMPH 1 'le-âtiyennehum' (2.; 'le'), NEG 1 'lâ' (12.); "
 "7:18 emir, şart — COND 1 'men' (6.), EMPH 3 'le-men' (6.; 'le'), 'le-emle'enne' (9.; 'le' ve 'n'), IMPV 1 'xruc' (2.); "
 "morph ACC ('inneke' 7:15 2.), REM ('fe-bimâ' 7:16 2.) ölçüm kipinde yok; morph 7:17 2. kelimede pekiştirme nûnunu ayrı parça olarak vermiyor (ölçüm EMPH 1)",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:14 ★ (kaynak pas, z=1,57); 7:18 ★★★ (kaynak hapaks, z=3,28); 7:15, 7:16 ve 7:17 yıldız yok",
 "fâsıla: 7:13 ن → 7:14 ن (" + _F[0] + ") → 7:15 ن (" + _F[1] + ") → 7:16 م (" + _F[2] + ") → 7:17 ن (" + _F[3] + ") → 7:18 ن (" + _F[4] + ") — N sınıfı (ölçüm); 7:16 م ile harf değişir, sınıf değişmez; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:14 15:36 (emsal olarak basıldı), 38:79 (emsal olarak basıldı); ölçüm esit2 7:14 → 15:36 ve 38:79 (kademe BENZER); 7:15 xref yok; 7:16 xref yok; 7:17 xref yok; 7:18 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok (7:14, 7:15, 7:16, 7:17 ve 7:18 ölçümünde nakarat3 alanı boş)'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:14, 7:15, 7:16, 7:17 ve 7:18 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:14 3MS ('qâle' — gönderge 7:11 12. kelime), muhatap 2MS ('enzirnî' — söz içi), konuşan 1S eki ('enzirnî' — söz içi), 3MP ('yub'asûn' — söz içi, tartışmalı, edilgen, naib-i faili zamir, anılanlar bölümde adsız); "
 "7:15 3MS ('qâle' — tartışmalı, sayı uyumsuz, gönderge 7:11 6. kelime), muhatap 2MS eki ('inneke' — söz içi); "
 "7:16 3MS ('qâle' — gönderge 7:11 12. kelime), muhatap 2MS ('ağveytenî' — söz içi; ek 'sırâtake' — söz içi), konuşan 1S ('le-aq'udenne' — söz içi; ek 'ağveytenî' — söz içi), 3MP eki ('lehum' — söz içi, tartışmalı, anılanlar bölümde adsız); "
 "7:17 muhatap 2MS ('le-âtiyennehum' — söz içi, morph etiketi, okuma söz sahibi; 'tecidu' — söz içi), 3MP eki ('le-âtiyennehum', 'eydîhim', 'xalfihim', 'eymânihim', 'şemâ'ilihim', 'ekserahum' — söz içi, gönderge 7:16 5. kelime); "
 "7:18 3MS ('qâle' — tartışmalı, sayı uyumsuz, gönderge 7:11 6. kelime; 'tebi'ake' — söz içi, gönderge 'men' 6. kelime), muhatap 2MS ('xruc' — söz içi; ek 'tebi'ake' — söz içi), 3FS eki ('minhâ' — söz içi, tartışmalı, anılan yer bölümde adsız), 3MP eki ('minhum' — söz içi, gönderge 7:16 5. kelime), konuşan 1S ('le-emle'enne' — söz içi), muhatap 2MP eki ('minkum' — söz içi), aktör adlı 'cehenneme'",
 "7:14-18 gönderge zinciri: 7:14 ve 7:16 söz sahibi 7:11 12. kelime ('iblîs'); 7:15 ve 7:18 'qâle' (1. kelime) göndergesi 7:11 6. kelime ('qulnâ' konuşanı) — tartışmalı (sayı uyumu yok: 1P / 3MS; gönderge A1'de de 7:11 6. kelime); söz içi 1S ve 2MS konuşana göre yer değiştirir; "
 "7:14 'yub'asûn' ve 7:16 'lehum' 3MP — tartışmalı, anılanlar bölümde adsız; 7:17 ve 7:18 3MP ekleri 7:16 5. kelimeye; 7:18 'minhâ' 3FS — tartışmalı, anılan yer bölümde adsız (7:13 'minhâ' ile eş biçim); 7:18 'minkum' muhatap 2MP: muhatap ile ona uyanlar birlikte (okuma)",
 "edilgen: 7:14 'yub'asûn' (5. kelime; naib-i faili zamir) — ölçüm EDİLGEN 1/3; 7:15, 7:16, 7:17 ve 7:18 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:14 'qâle' (1.) ardından söz 2-5. kelime; 7:15 'qâle' (1.) ardından söz 2-4. kelime — ayet içi kapanışlar; "
 "7:16 'qâle' (1.) ardından söz 2. kelimede açılır (REM sapması 7:16 (2. kelime) — 'fe-bimâ' söz başında, önceki söze bağlanır) ve ayet sonunda kapanmaz; 7:17 söz 7:16 2. kelimeden sürer ve 15. kelimede kapanır (7:18 'qâle' ile konuşan değişir); "
 "7:18 'qâle' (1.) ardından söz 2-12. kelime, ayet içi kapanış (okuma); mealde 'Dedi ki:' ardından tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 14 18 04' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 7:17 've min' (6.) CONJ, 've 'an' (8.) CONJ, 've 'an' (10.) CONJ, 've lâ' (12.) CONJ; "
 "'fe' konumları: 7:16 'fe-bimâ' (2.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:14 ◈K يوم ('yevmi' 4. kelime — K2); 7:17 ◈B يدي ('eydîhim' 5. kelime — B3; 'beyni eydîhim' kalıbı, organ anlamı yok (okuma)); 7:15, 7:16 ve 7:18 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 14 18 04'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:14 (15:36, 38:79); 7:15, 7:16, 7:17 ve 7:18 bağ yok; D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): yok; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:14 söz açılır (2. kelime), söz kapanır (5. kelime, ayet içi), şahıs geçişi 2 → 3, edim geçişi yok; 7:15 söz açılır (2. kelime), söz kapanır (4. kelime, ayet içi), şahıs geçişi yok, şahıs sayısında beraberlik (2MS 1 · 3MS 1 — ölçüm baskın 3), edim geçişi emir → haber; "
 "7:16 söz açılır (2. kelime), söz ayet sonunda kapanmıyor, şahıs geçişi 3 → 2, edim geçişi yok; 7:17 söz sürüyor, söz kapanır (15. kelime), şahıs geçişi 2 → 3, edim geçişi yok; "
 "7:18 söz açılır (2. kelime), söz kapanır (12. kelime, ayet içi), şart → cevap ('men' 6. kelime / 'le-emle'enne' 9. kelime), muhatap geçişi 2MS → 2MP (ayet içi), şahıs geçişi yok, edim geçişi haber → emir, şart; "
 "ölçüm iltifât 7:14-18 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:14 'yevmi yub'asûn' — zaman adına bağlı fiil cümlesi (morph GEN + IMPF PASS); 7:15 'inneke mine'l-munzarîn' — tekitli isim cümlesi (morph ACC); 7:16 'fe-bimâ ağveytenî' — sebep bildiren 'bi' ve mastar 'mâ' (morph REM + P + REL); 7:16 'le-aq'udenne' — yemin lâmı ve pekiştirme nûnu (morph EMPH); "
 "7:17 'summe le-âtiyennehum' — sıralı atıf ve yemin lâmı (morph CONJ + EMPH); 7:18 'mez'ûmen medhûrâ' — durum bildiren ardışık ortaçlar (morph ACC + INDEF); 7:18 'le-men tebi'ake' ve 'le-emle'enne' — şart ve cevabı, yemin lâmlarıyla (morph EMPH + COND + EMPH)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:14 3-5. kelime — 15:36 ve 38:79 ile harekesiz eş (sayım: 'say 7:14 3-5'); 7:14 2. kelime emsallerde 'fe' önekiyle, burada öneksiz (sayım: 'dizi 7 14 2 5'); "
 "7:18 4. kelime kökü ذأم korpusta başka yerde geçmiyor (ölçüm HAPAKS); 7:17 2. kelimede morph 2MS etiketi — okuma 1S",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 04'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'ilâ yevmi yub'asûn' 7:14 'diriltilecekleri güne kadar' / 15:36 'diriltilecekleri güne kadar' (emsal metninde) — çakışma değil (bayt eşit); "
 "'ilâ yevmi yub'asûn' 7:14 'diriltilecekleri güne kadar' / 38:79 'diriltilecekleri güne kadar' (emsal metninde) — çakışma değil (bayt eşit); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:14 'qâle' PERF — meal 'Dedi'; 'enzirnî' IMPV — meal 'ver'; 'yub'asûn' IMPF IND PASS — meal 'diriltilecekleri'; 7:15 'qâle' PERF — meal 'Dedi'; "
 "7:16 'qâle' PERF — meal 'Dedi'; 'ağveyte' PERF — meal 'azdırmana'; 'aq'ude' IMPF IND ('le' ve 'n' ile) — meal 'oturacağım'; 7:17 'âtiyenne' IMPF IND ('le' ile) — meal 'geleceğim'; 'tecidu' IMPF IND ('lâ' ile) — meal 'bulmayacaksın'; "
 "7:18 'qâle' PERF — meal 'Dedi'; 'xruc' IMPV — meal 'çık'; 'tebi'a' PERF ('men' ile) — meal 'uyarsa'; 'emle'e' IMPF IND ('le' ve 'n' ile) — meal 'dolduracağım'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle): 'yub'asûn' IMPF 7:14'te sıfat-fiil ('-ecekleri') ile; 'ağveyte' PERF 7:16'da ad-fiil ('-mana') ile; 'aq'ude' IMPF 7:16'da, 'âtiyenne' ile 'tecidu' IMPF 7:17'de ve 'emle'e' IMPF 7:18'de gelecek zaman ile; 'tebi'a' PERF 7:18'de şart kipi ('-arsa') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): 'nî' ('Bana' / 'Beni' / 'beni') — çakışma değil (yönelme ve belirtme çekimi, cümle başı büyük harf); 'summe' ('Sonra' / 'sonra') — çakışma değil (cümle başı büyük harf); 've' (CONJ: 've' / 'ise' / karşılıksız) — çakışma değil (atıf, karşıtlık atfı, Türkçe sıralama)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 14 18 04'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:14, 7:15, 7:16, 7:17 ve 7:18 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:17 ('beyni eydîhim' / 'xalfihim'; 'eymânihim' / 'şemâ'ilihim'); 7:14, 7:15, 7:16 ve 7:18 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök نظر 7:14 ('enzirnî') ve 7:15 ('l-munzarîn'); kök قول 7:14 ('qâle'), 7:15 ('qâle'), 7:16 ('qâle') ve 7:18 ('qâle'); kök خرج 7:18 ('xruc'), 7:13 ('fe'xruc') ile bölüm içi; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 2-2 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 3, 4, 5 ve 6; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b04/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 14 18 04'; lem_bozuk.py 04 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 14 18 → AYN_SONUC; sunum/bolum4_kurallar.py 14 18 04 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 14 18 04 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 37)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 4 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('yunzaru' (morph LEM ham biçim), 'ilâ', 'yevm', 'be'ase'); joker '_' kullanılmadı; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

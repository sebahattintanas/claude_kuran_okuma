_OL = [l for l in open('/home/claude/b02/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b02/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 5), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
I = [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta araç kuralı değişmedi; blok 1'de sunum/kelime_kontrol.py (bölüm 10 denetimi kuralı 6) morph INL istisnası önceki commit'te; yeni kök yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 365",
 "geriye dönük koşu (bölüm 19 kapanışı, sûre 6 kayıtlarında, komut 'python3 sunum/geriye_donuk.py b40k yamalar/geriye_donuk_6_b38k.txt'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 6 10 02'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:6, 7:7, 7:8, 7:9 ve 7:10 esmâ yok; 7:6, 7:7, 7:8, 7:9 ve 7:10 lafız ve Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 6 10 02'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in (6, 7, 8, 9, 10)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 6 10 02'): KALAN_P",
 "ölçüm aktör: 7:6, 7:7, 7:8, 7:9 ve 7:10 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:6 haber — EMPH 4 'fe-le-nes'elenne' (1.; 'le' ve 'n'), 've le-nes'elenne' (5.; 'le' ve 'n'); 7:7 haber — EMPH 2 'fe-le-nequssanne' (1.; 'le' ve 'n'), NEG 1 'mâ' (4.); "
 "7:8 şart — COND 1 'men' (4.); 7:9 şart — COND 1 'men' (1.); 7:10 haber — CERT 1 've le-qad' (1.), EMPH 1 've le-qad' (1.; 'le'); "
 "morph REM ('fe-le-nes'elenne' 7:6 1., 've mâ' 7:7 4., 'fe-men' 7:8 4., 've le-qad' 7:10 1.), RSLT ('fe-ulâ'ike' 7:8 7., 'fe-ulâ'ike' 7:9 4.), SUP ('mâ' 7:10 10.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:6 ★ (kaynak pas, z=1,57); 7:7, 7:8, 7:9 ve 7:10 yıldız yok",
 "fâsıla: 7:5 ن → 7:6 ن (" + _F[0] + ") → 7:7 ن (" + _F[1] + ") → 7:8 ن (" + _F[2] + ") → 7:9 ن (" + _F[3] + ") → 7:10 ن (" + _F[4] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:6 xref yok; 7:7 xref yok; 7:8 23:102 (emsal olarak basıldı); 7:9 23:103 (emsal olarak basıldı); 7:10 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok (7:6, 7:7, 7:8, 7:9 ve 7:10 ölçümünde nakarat3 alanı boş)'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:6, 7:7, 7:8, 7:9 ve 7:10 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:6 konuşan 1P ('fe-le-nes'elenne', 've le-nes'elenne'), 3MS ('ursile' — edilgen, naib-i faili 'ileyhim' 4. kelime), 3MP eki ('ileyhim' — gönderge 'llezîne' 2. kelime); "
 "7:7 konuşan 1P ('fe-le-nequssanne', 'kunnâ'), 3MP eki (''aleyhim' — tartışmalı, gönderge 7:6 2. kelime); "
 "7:8 3FS ('sequlet' — fiil uyumu, fail 6. kelime), 3MS eki ('mevâzînuhû' — gönderge 'men' 4. kelime), 3MP ('humu' — gönderge 'ulâ'ike' 7. kelime); "
 "7:9 3FS ('xaffet' — fiil uyumu, fail 3. kelime), 3MS eki ('mevâzînuhû' — gönderge 'men' 1. kelime), 3MP ('xasirû', 'kânû', 'yazlimûn' — gönderge 'llezîne' 5. kelime; ek 'enfusehum' — gönderge 'llezîne' 5. kelime), konuşan 1P eki ('bi-âyâtinâ'); "
 "7:10 konuşan 1P ('mekkennâkum', 've ce'alnâ'), muhatap 2MP ('teşkurûn'; ekler 'mekkennâkum', 'lekum'), 3FS eki ('fîhâ' — gönderge 'l-ardi' 4. kelime)",
 "7:6-10 gönderge zinciri: konuşan 1P (adsız) 7:6, 7:7, 7:9 ('bi-âyâtinâ' 10. kelime) ve 7:10'da, 7:4 ve 7:5'ten sürer; 7:6 'llezîne' (2. kelime) kendilerine gönderilenler; 7:7 ''aleyhim' göndergesi 7:6 2. kelime — tartışmalı (7:6 6. kelime 'l-murselîn' de kapsanabilir; gönderge A1'de de 7:6 2. kelime); "
 "7:8 ve 7:9 'men' göndergeleri 'ulâ'ike' ile çoğula geçer; 7:10 muhatap 2MP (adsız), 7:3 muhatabından sonra yeniden (okuma)",
 "edilgen: 7:6 'ursile' (3. kelime; naib-i faili 'ileyhim') — ölçüm EDİLGEN 1/3; 7:7, 7:8, 7:9 ve 7:10 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:6, 7:7, 7:8, 7:9 ve 7:10 söz yok (okuma); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 6 10 02' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 7:6 've le-nes'elenne' (5.) CONJ; 7:7 've mâ' (4.) REM; 7:8 've'l-veznu' (1.) CONJ; 7:9 've men' (1.) CONJ; 7:10 've le-qad' (1.) REM, 've ce'alnâ' (5.) CONJ; "
 "'fe' konumları: 7:6 'fe-le-nes'elenne' (1.) REM; 7:7 'fe-le-nequssanne' (1.) CONJ; 7:8 'fe-men' (4.) REM, 'fe-ulâ'ike' (7.) RSLT; 7:9 'fe-ulâ'ike' (4.) RSLT",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:8 ◈K يوم ('yevme'izin' 2. kelime — K2); 7:10 ◈K أرض ('l-ardi' 4. kelime — K1); 7:6, 7:7 ve 7:9 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 6 10 02'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:8 (23:102); 7:9 (23:103); 7:6, 7:7 ve 7:10 bağ yok; D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:6 رسل ×2, سأل ×2; 7:8 وزن ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:6 şahıs geçişi 3 → 1, şahıs sayısında beraberlik (1P 2 · 3MP 1 · 3MS 1 — ölçüm baskın 1), edim geçişi yok; 7:7 şahıs geçişi yok, edim geçişi yok; 7:8 şart → cevap ('men' 4. kelime / 'fe-ulâ'ike' 7. kelime), şahıs geçişi 1 → 3, edim geçişi haber → şart; "
 "7:9 şart → cevap ('men' 1. kelime / 'fe-ulâ'ike' 4. kelime), şahıs geçişi yok, edim geçişi yok; 7:10 şahıs geçişi 3 → 1, şahıs sayısında beraberlik (1P 4 · 2MP 4 — ölçüm baskın 1), edim geçişi şart → haber; bölüm kapanışı; "
 "ölçüm iltifât 7:6-10 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:6 'fe-le-nes'elenne' — pekiştirme lâmı ve nûnu (morph EMPH); 7:7 've mâ kunnâ ğâ'ibîn' — olumsuz isim cümlesi (morph REM + NEG); 7:8 've'l-veznu yevme'izini'l-haqq' — isim cümlesi, zaman zarfı arada (morph CONJ + T); "
 "7:8 'fe-men sequlet mevâzînuhû fe-ulâ'ike' — şart ve cevap (morph REM + COND + RSLT); 7:9 've men xaffet mevâzînuhû fe-ulâ'ike' — şart ve cevap (morph CONJ + COND + RSLT); 7:9 'bimâ kânû bi-âyâtinâ yazlimûn' — sebep bildiren ilgi cümlesi (morph REL); "
 "7:10 've le-qad' — pekiştirme (morph REM + EMPH + CERT); 7:10 'qalîlen mâ teşkurûn' — zâid 'mâ' ile pekiştirme (morph SUP)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:8 4-9. kelime — 23:102 ile harekesiz eş (sayım: 'say 7:8 4-9'); 7:9 1-7. kelime — 23:103 ile harekesiz eş (sayım: 'say 7:9 1-7'); "
 "7:10 9-10. kelime — 7:3 ile harekesiz eş (sayım: 'say 7:10 9-10'); 7:6 kök رسل, سأل ikilemeleri; 7:8 kök وزن ikilemesi",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 02'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'fe-men sequlet mevâzînuhû fe-ulâ'ike humu'l-muflihûn' 7:8 'Tartıları ağır gelenler, işte onlar kurtuluşa erenlerdir' / 23:102 'Tartıları ağır gelenler, işte onlar kurtuluşa erenlerdir' (emsal metninde) — çakışma değil (bayt eşit); "
 "'fe-men sequlet mevâzînuhû' 7:8 'Tartıları ağır gelenler' / 23:102 'Tartıları ağır gelenler' (emsal metninde) — çakışma değil (bayt eşit); "
 "'fe-ulâ'ike humu'l-muflihûn' 7:8 'işte onlar kurtuluşa erenlerdir' / 23:102 'işte onlar kurtuluşa erenlerdir' (emsal metninde) — çakışma değil (bayt eşit); "
 "'ve men xaffet mevâzînuhû fe-ulâ'ike'llezîne xasirû enfusehum' 7:9 'Tartıları hafif gelenler, işte onlar kendilerini ziyana uğratanlardır' / 23:103 'Tartıları hafif gelenler, işte onlar kendilerini ziyana uğratanlardır' (emsal metninde) — çakışma değil (bayt eşit); "
 "'ve men xaffet mevâzînuhû' 7:9 'Tartıları hafif gelenler' / 23:103 'Tartıları hafif gelenler' (emsal metninde) — çakışma değil (bayt eşit); "
 "'fe-ulâ'ike'llezîne xasirû enfusehum' 7:9 'işte onlar kendilerini ziyana uğratanlardır' / 23:103 'işte onlar kendilerini ziyana uğratanlardır' (emsal metninde) — çakışma değil (bayt eşit); "
 "'llezîne xasirû enfusehum' 7:9 'kendilerini ziyana uğratanlardır' / 23:103 'kendilerini ziyana uğratanlardır' (emsal metninde) — çakışma değil (bayt eşit); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:6 'nes'ele' IMPF IND (1. kelime; 'le' ve 'n' ile) — meal 'soracağız'; 'ursile' PERF PASS — meal 'gönderilenlere'; 'nes'ele' IMPF IND (5. kelime; 'le' ve 'n' ile) — meal 'soracağız'; "
 "7:7 'nequssa' IMPF IND ('le' ve 'n' ile) — meal 'anlatacağız'; 'kunnâ' PERF ('mâ' ile) — meal 'değildik'; 7:8 'sequlet' PERF — meal 'gelenler'; 7:9 'xaffet' PERF — meal 'gelenler'; 'xasirû' PERF — meal 'uğratanlardır'; 'kânû' PERF — meal 'olmaları'; 'yazlimûn' IMPF IND — meal 'zulmetmekte'; "
 "7:10 'mekkennâ' PERF — meal 'yerleştirdik'; 'ce'alnâ' PERF — meal 'ettik'; 'teşkurûn' IMPF IND — meal 'şükrediyorsunuz'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle): 'nes'ele' IMPF 7:6'da ve 'nequssa' IMPF 7:7'de gelecek zaman ('-acağız') ile; 'ursile' PERF 7:6'da sıfat-fiil ('-en') ile; 'sequlet' PERF 7:8'de ve 'xaffet' PERF 7:9'da sıfat-fiil ('-en') ile; 'xasirû' PERF 7:9'da sıfat-fiil ('-an') ile; 'kânû' PERF 7:9'da ad-fiil ('-maları') ile; 'yazlimûn' IMPF 7:9'da sürerlik ('-mekte') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): 'iz' ('O' / '-diğinde') — çakışma değil ('yevme'izin' birleşiğinde işaret, 7:5'te zaman bağlacı)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 6 10 02'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:6, 7:7, 7:8, 7:9 ve 7:10 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:6, 7:7, 7:8, 7:9 ve 7:10 ayet içi karşıt çift yok; ayetler arası: 7:8 / 7:9 ('sequlet' / 'xaffet'); eşleme betikle: ADAY_P",
 "aday 1041: kök كون 7:7 ('kunnâ') ve 7:9 ('kânû'), 7:2 ('yekun') ve 7:5 ('kâne', 'kunnâ') ile bölüm içi; kök وزن 7:8 ('l-veznu', 'mevâzînuhû') ve 7:9 ('mevâzînuhû'); kök ظلم 7:9 ('yazlimûn'), 7:5 ('zâlimîn') ile bölüm içi; kök قلل 7:10 ('qalîlen'), 7:3 ('qalîlen') ile bölüm içi; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 1-2 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 1 ve 2; bölüm kapanışı bu blokta; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b02/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 6 10 02'; lem_bozuk.py 02 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 6 10 → AYN_SONUC; sunum/bolum4_kurallar.py 6 10 02 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 6 10 02 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 36)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 2 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('men', 'sequlet' (morph LEM ham biçim), 'mîzân', 'zâ', 'muflih', 'xaffet' (morph LEM ham biçim), 'ellezî', 'xasira', 'nefs'); joker '_' yalnız lemmasız 'hum' öğesinde ('dizi 7 8 4 9'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

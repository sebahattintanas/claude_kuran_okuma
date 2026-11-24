_OL = [l.replace('**', '') for l in open('/home/claude/b03/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b03/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 10), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
def _esc(t):
    for c in '.()[]|': t = t.replace(c, '\\' + c)
    return t
_AK = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[0]).group(0))
_MB = _MB.replace('" + _AK + "', _AK)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta sunum/bolum16_kurallar.py (kural 1) fiilin ardındaki ayrı zamiri yeni cümlenin öznesi sayar — 7:12 8. kelime 'qâle' ardındaki 'ene xayrun' isim cümlesi, 10. kelime fail değil; sunum/bolum17_kurallar.py (kural 3) çok lemmalı kelimeyi bütün lemmalarıyla eşler — 7:12 4. kelime 'ellâ' ('en' + 'lâ') 38:75'teki 'en' ile eş sayılmaz; bölüm 1 kapanışında sunum/bolum36_kurallar.py (kural 1-5) eklendi, sunum/geriye_donuk.py ve mutasyon_sina buna göre güncellendi — önceki commit'te, kapanış mutasyon sınaması 384 / 384; yeni kök yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 371",
 "geriye dönük koşu (sûre 7 bölüm 1 kapanışı, komut 'python3 sunum/geriye_donuk.py b02k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 11 13 03'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:11, 7:12 ve 7:13 esmâ yok; 7:11, 7:12 ve 7:13 lafız ve Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 11 13 03'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in (11, 12, 13)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 11 13 03'): KALAN_P",
 "ölçüm aktör: 7:11 '{{1|" + _AK + "}}' (A1'de 'âdeme' ve 'iblîs'); 7:12 ve 7:13 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:11 emir — CERT 1 've le-qad' (1.), EMPH 1 've le-qad' (1.; 'le'), IMPV 1 'scudû' (8.), NEG 1 'lem' (13.); ölçüm biçim ISTISNA (D2'de yazılmadı); "
 "7:12 soru — INTG 1 'mâ' (2.), NEG 1 'ellâ' (4.; 'lâ'); 7:13 emir — IMPV 2 'hbit' (2.), 'xruc' (10.), NEG 1 'mâ' (4.); "
 "morph REM ('fe-secedû' 7:11 10., 'fe-mâ' 7:13 4., 'fe'xruc' 7:13 10.), EXP ('illâ' 7:11 11.), SUB ('ellâ' 7:12 4., 'en' 7:13 7.), SUP ('fe'hbit' 7:13 2.), ACC ('inneke' 7:13 11.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:11, 7:12 ve 7:13 yıldız yok",
 "fâsıla: 7:10 ن → 7:11 ن (" + _F[0] + ") → 7:12 ن (" + _F[1] + ") → 7:13 ن (" + _F[2] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:11 18:50 (emsal olarak basıldı); 7:12 38:75 (emsal olarak basıldı), 38:76 (emsal olarak basıldı); 7:13 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok (7:11, 7:12 ve 7:13 ölçümünde nakarat3 alanı boş)'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:11, 7:12 ve 7:13 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:11 konuşan 1P ('xalaqnâkum', 'savvernâkum', 'qulnâ'), muhatap 2MP ('scudû' — söz içi; ekler 'xalaqnâkum', 'savvernâkum'), 3MP ('fe-secedû' — gönderge 'l-melâ'iketi' 7. kelime), 3MS ('yekun' — gönderge 'iblîs' 12. kelime), aktör adlı 'âdeme' ve 'iblîs'; "
 "7:12 3MS ('qâle' 1. kelime — tartışmalı, sayı uyumsuz, gönderge 7:11 6. kelime; 'mene'ake' — söz içi, gönderge 'mâ' 2. kelime; 'qâle' 8. kelime — gönderge 7:11 12. kelime; ekler 'minhu', 've xalaqtehû' — söz içi, gönderge 7:11 9. kelime), "
 "muhatap 2MS ('tescude', 'xalaqtenî', 've xalaqtehû' — söz içi; ekler 'mene'ake', 'emertuk' — söz içi), konuşan 1S ('emertuk', 'ene' — söz içi; ek 'xalaqtenî' — söz içi); "
 "7:13 3MS ('qâle' — tartışmalı, sayı uyumsuz, gönderge 7:11 6. kelime; 'yekûnu' — söz içi, gönderge 'en tetekebbera' 7-8. kelime), muhatap 2MS ('fe'hbit', 'tetekebbera', 'fe'xruc' — söz içi; ekler 'leke', 'inneke' — söz içi), 3FS eki ('minhâ', 'fîhâ' — söz içi, tartışmalı, anılan yer bölümde adsız)",
 "7:11-13 gönderge zinciri: konuşan 1P (adsız) 7:11'de, 7:10'dan sürer; 7:11 muhatap 2MP ekleri 7:10 muhatabıyla sürer, söz içi muhatap 2MP ise melekler ('l-melâ'iketi' 7. kelime); 7:12 ve 7:13 'qâle' (1. kelime) göndergesi 7:11 6. kelime ('qulnâ' konuşanı) — tartışmalı (sayı uyumu yok: 1P / 3MS; gönderge A1'de de 7:11 6. kelime); "
 "7:12 8. kelime fiilinin göndergesi 7:11 12. kelime ('iblîs'); 7:12 3MS ekleri 7:11 9. kelime ('li-âdeme'); 7:13 3FS ekleri ('minhâ', 'fîhâ') — tartışmalı, anılan yer bölümde adsız; 7:12 ve 7:13 söz içi 1S ve 2MS konuşana göre yer değiştirir (okuma)",
 "edilgen: 7:11, 7:12 ve 7:13 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:11 'qulnâ' (6.) ardından söz 8-9. kelime, ayet içi kapanış; 7:12 'qâle' (1.) ardından söz 2-7. kelime, 'qâle' (8.) ardından söz 9-17. kelime — ayet içi kapanışlar; "
 "7:13 'qâle' (1.) ardından söz 2-13. kelime (REM sapması 7:13 (4. kelime) — 'fe-mâ yekûnu' söz içinde istînâf, muhatap 2MS sürer; REM sapması 7:13 (10. kelime) — 'fe'xruc' söz içinde istînâf, muhatap 2MS sürer), ayet sonunda kapanır (okuma); mealde 'dedik' öncesinde ve 'Dedi ki:' ardından tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 11 13 03' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 7:11 've le-qad' (1.) CONJ; 7:12 've xalaqtehû' (15.) CONJ; "
 "'fe' konumları: 7:11 'fe-secedû' (10.) REM; 7:13 'fe'hbit' (2.) SUP, 'fe-mâ' (4.) REM, 'fe'xruc' (10.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:11 ◈B خلق ('xalaqnâkum' 2. kelime — B2; anlam notu: muhatapların yaratılışı); 7:12 ◈B خلق ('xalaqtenî' 12. kelime — B2; anlam notu: ateşten yaratılış), 7:12 ◈B خلق ('xalaqtehû' 15. kelime — B2; anlam notu: çamurdan yaratılış); 7:13 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 11 13 03'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:11 (18:50); 7:12 (38:75, 38:76); 7:13 bağ yok; D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:11 سجد ×3; 7:12 خلق ×2, قول ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:11 bölüm açılışı, söz açılır (8. kelime), söz kapanır (9. kelime, ayet içi), şahıs geçişi yok, edim geçişi haber → emir; 7:12 söz açılır (2. kelime), söz kapanır (7. kelime, ayet içi), söz açılır (9. kelime), söz kapanır (17. kelime, ayet içi), şahıs geçişi 1 → 2, edim geçişi emir → soru; "
 "7:13 söz açılır (2. kelime), söz kapanır (13. kelime, ayet içi), şahıs geçişi yok, edim geçişi soru → emir; "
 "ölçüm iltifât 7:11-13 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:11 've le-qad' — pekiştirme (morph CONJ + EMPH + CERT); 7:11 'summe' ile sıralı atıf (morph CONJ); 7:11 'illâ iblîs' — istisna (morph EXP); 7:11 'lem yekun mine's-sâcidîn' — olumsuz geçmiş (morph NEG + JUS); "
 "7:12 'mâ mene'ake ellâ tescude' — soru ve mastar cümlesi, olumsuzluk edatı zâid okundu (morph INTG + SUB + NEG); 7:12 'iz emertuk' — zaman cümlesi (morph T); 7:13 'fe'hbit' — söz başında 'fe' (morph SUP); 7:13 'en tetekebbera' — mastar cümlesi (morph SUB); 7:13 'inneke mine's-sâğirîn' — tekitli isim cümlesi (morph ACC)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:11 6-12. kelime — 18:50 ile harekesiz eş (sayım: 'say 7:11 6-12'); 7:12 2-3. kelime — 38:75 ile harekesiz eş (sayım: 'say 7:12 2-3'); 7:12 8-17. kelime — 38:76 ile harekesiz eş (sayım: 'say 7:12 8-17'); "
 "7:11 kök سجد üçlemesi; 7:12 kök خلق, قول ikilemeleri",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 03'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'qulnâ li'l-melâ'iketi'scudû li-âdeme fe-secedû illâ iblîs' 7:11 'meleklere: Âdem'e secde edin, dedik; İblîs hariç secde ettiler' / 18:50 'Meleklere: Âdem'e secde edin, demiştik; İblîs hariç secde ettiler' (emsal metninde) — çakışma — tam okuma sonu ('dedik' / 'demiştik' kip farkı ve cümle başı büyük harf); "
 "'fe-secedû illâ iblîs' 7:11 'İblîs hariç secde ettiler' / 18:50 'İblîs hariç secde ettiler' (emsal metninde) — çakışma değil (bayt eşit); "
 "'mâ mene'ake' 7:12 'seni ne alıkoydu' / 38:75 'seni ne alıkoydu' (emsal metninde) — çakışma değil (bayt eşit); "
 "'qâle ene xayrun minhu xalaqtenî min nârin ve xalaqtehû min tîn' 7:12 'Ben ondan hayırlıyım; beni ateşten yarattın, onu ise çamurdan yarattın' / 38:76 'Ben ondan hayırlıyım; beni ateşten yarattın, onu ise çamurdan yarattın' (emsal metninde) — çakışma değil (bayt eşit); "
 "'ene xayrun minhu' 7:12 'Ben ondan hayırlıyım' / 38:76 'Ben ondan hayırlıyım' (emsal metninde) — çakışma değil (bayt eşit); "
 "'xalaqtenî min nârin' 7:12 'beni ateşten yarattın' / 38:76 'beni ateşten yarattın' (emsal metninde) — çakışma değil (bayt eşit); "
 "'ve xalaqtehû min tîn' 7:12 'onu ise çamurdan yarattın' / 38:76 'onu ise çamurdan yarattın' (emsal metninde) — çakışma değil (bayt eşit); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:11 'xalaqnâ' PERF — meal 'yarattık'; 'savvernâ' PERF — meal 'verdik'; 'qulnâ' PERF — meal 'dedik'; 'scudû' IMPV — meal 'edin'; 'secedû' PERF — meal 'ettiler'; 'yekun' IMPF JUS ('lem' ile) — meal 'olmadı'; "
 "7:12 'qâle' PERF (1. kelime) — meal 'Dedi'; 'mene'a' PERF — meal 'alıkoydu'; 'tescude' IMPF SUBJ ('en' ile) — meal 'etmekten'; 'emertu' PERF — meal 'emrettiğimde'; 'qâle' PERF (8. kelime) — meal 'Dedi'; 'xalaqte' PERF (12. kelime) — meal 'yarattın'; 'xalaqte' PERF (15. kelime) — meal 'yarattın'; "
 "7:13 'qâle' PERF — meal 'Dedi'; 'hbit' IMPV — meal 'in'; 'yekûnu' IMPF IND ('mâ' ile) — meal 'olmaz'; 'tetekebbera' IMPF SUBJ ('en' ile) — meal 'büyüklenmek'; 'xruc' IMPV — meal 'çık'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle): 'yekun' IMPF JUS 7:11'de 'lem' ile geçmiş zaman ('-dı') ile; 'tescude' IMPF SUBJ 7:12'de ad-fiil ('-mek') ile; 'emertu' PERF 7:12'de zarf-fiil ('-diğimde') ile; 'tetekebbera' IMPF SUBJ 7:13'te ad-fiil ('-mek') ile; 'yekûnu' IMPF IND 7:13'te geniş zaman olumsuzu ('-maz') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): bölümün önceki bloğu yok",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 11 13 03'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:11, 7:12 ve 7:13 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:12 ('xalaqtenî min nârin' / 've xalaqtehû min tîn'); 7:13 ('tetekebbera' / 's-sâğirîn'); 7:11 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök سجد 7:11 ('scudû', 'fe-secedû', 's-sâcidîn') ve 7:12 ('tescude'); kök خلق 7:11 ('xalaqnâkum') ve 7:12 ('xalaqtenî', 've xalaqtehû'); kök قول 7:11 ('qulnâ'), 7:12 ('qâle', 'qâle') ve 7:13 ('qâle'); kök كون 7:11 ('yekun') ve 7:13 ('yekûnu'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 2-1 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 3, 4, 5 ve 6; bu blok bölümü açıyor; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b03/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 11 13 03'; lem_bozuk.py 03 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 11 13 → AYN_SONUC; sunum/bolum4_kurallar.py 11 13 03 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 11 13 03 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 37)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 3 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('qâle', 'melek', 'secede', 'âdem', 'illâ', 'iblîs', 'mâ', 'mene'a', 'xayr', 'min', 'xalaqa', 'nâr', 'tîn'); joker '_' yalnız lemmasız 'ene' öğesinde ('dizi 7 12 8 17'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

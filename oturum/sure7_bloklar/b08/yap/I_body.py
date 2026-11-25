_OL = [l.replace('**', '') for l in open('/home/claude/b08/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b08/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 27), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK3 = _esc(re.search(r'aktör: adlı .*adsız `ferîk` 3\. sırada', _OL[2]).group(0))
_ES3 = _esc(re.search(r'esmâ \S+ 10\. sırada, ORTA konum, MÜHÜRSÜZ', _OL[2]).group(0))
for _k, _v in (('_AK3', _AK3), ('_ES3', _ES3)): _MB = _MB.replace('" + %s + "' % _k, _v)
I = [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta araç kuralı değişmedi; yeni kök yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 395",
 "geriye dönük koşu (sûre 7 bölüm 2 kapanışı, komut 'python3 sunum/geriye_donuk.py b06k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 28 30 08'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:30 'innehumu'ttexazu'ş-şeyâtîne evliyâ'e min dûni'llâhi' (7-13. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (dost edinilen şeytanlar) (yamalar/esma_el_7_28_30.txt); 7:28 ve 7:29 esmâ yok; 7:28 lafız (8., 13. ve 19. kelime), 7:30 lafız (13. kelime); 7:29 Rab (3. kelime); 7:29 lafız yok; 7:28 ve 7:30 Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 28 30 08'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in (28, 29, 30)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 28 30 08'): KALAN_P",
 "ölçüm aktör: 7:30 '{{3|" + _AK3 + "}}' (A1'de 'ş-şeyâtîne', adsız 'ferîqan' ve 've ferîqan'); 7:28 ve 7:29 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:28 soru, emir — IMPV 1 'qul' (11.), INTG 1 'e-teqûlûne' (17.; 'e'), NEG 2 'lâ' (14. ve 21.); 7:29 emir — IMPV 3 'qul' (1.), 'aqîmû' (5.), 'd'ûhu' (10.); 7:30 haber — kip yok; "
 "morph REM ('ve izâ' 7:28 1., 've'llâhu' 7:28 8.), T ('izâ' 7:28 1.), ACC ('inne' 7:28 12., 'innehumu' 7:30 7., 'ennehum' 7:30 15.), REL ('mâ' 7:28 20.), SUB ('kemâ' 7:29 14.), CIRC ('ve yahsebûne' 7:30 14.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:28 ★★ (kaynak allah, z=2,20); 7:29 ve 7:30 yıldız yok",
 "fâsıla: 7:27 ن → 7:28 ن (" + _F[0] + ") → 7:29 ن (" + _F[1] + ") → 7:30 ن (" + _F[2] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:28 2:169 (emsal olarak basıldı), okunmuş 1 ayet; 7:29 40:65 (emsal olarak basıldı); 7:30 okunmuş 1 ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:28 'qâle 'alâ allâh mâ lâ 'alime' süzgeç GEÇER, 'allâh mâ lâ 'alime' süzgeç GEÇER, 'qâle 'alâ allâh' süzgeç GEÇER, 'qâle inne allâh' süzgeç GEÇMEZ; 7:29 ''inde kull mescid' süzgeç GEÇMEZ; 7:30 'min dûn allâh' süzgeç GEÇER; GEÇER kalıpların sûre içi eşleri basılmamış — D3'e alınmadı",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:28 3MP ('fe'alû', 'qâlû' — tartışmalı, gönderge 7:27 28. kelime), konuşan 1P ('vecednâ' — söz içi; ekler 'âbâ'enâ', 'emeranâ' — söz içi), 3FS eki (''aleyhâ', 'bihâ' — söz içi; gönderge 'fâhişeten' 3. kelime), 3MS ('emeranâ' — söz içi; gönderge 've'llâhu' 8. kelime; 'ye'muru' — söz içi; gönderge 'llâhe' 13. kelime), muhatap 2MS ('qul'), muhatap 2MP ('e-teqûlûne', 'ta'lemûn' — söz içi); "
 "7:29 muhatap 2MS ('qul'), 3MS ('emera' — söz içi; fiil uyumu, fail 3. kelime; 'bede'ekum' — söz içi; gönderge 'rabbî' 3. kelime; ekler 've'd'ûhu', 'lehu' — söz içi; gönderge 'rabbî' 3. kelime), konuşan 1S eki ('rabbî' — söz içi), muhatap 2MP ('ve aqîmû', 've'd'ûhu', 'te'ûdûn' — söz içi; ekler 'vucûhekum', 'bede'ekum' — söz içi); "
 "7:30 3MS ('hedâ' — gönderge 7:29 3. kelime; 'haqqa' — fiil uyumu, fail 6. kelime), 3MP ('ttexazu', 've yahsebûne' — gönderge 've ferîqan' 3. kelime; ekler ''aleyhimu', 'innehumu', 'ennehum' — gönderge 've ferîqan' 3. kelime), aktör adlı 'ş-şeyâtîne', aktör adsız 'ferîqan' ve 've ferîqan'",
 "7:28-30 gönderge zinciri: 7:28 'fe'alû' (2. kelime) ve 'qâlû' (4. kelime) 3MP — gönderge 7:27 28. kelime ('lillezîne'), tartışmalı (bölüm muhatabı Âdemoğullarından gıyaba geçiş olasılığı açık); 7:28 5-10. kelime onların sözü, konuşan 1P o topluluk; 7:28 'qul' (11. kelime) ve 7:29 'qul' (1. kelime) muhatabı elçi, metinde adsız; "
 "7:28 12-22. kelime ve 7:29 2-16. kelime söz içi muhatap 2MP o topluluk; 7:29 konuşan 1S elçi, 3MS fiil ve ekler 'rabbî' (3. kelime); 7:30 'hedâ' (2. kelime) 7:29 3. kelimeye; 7:30 3MP fiil ve ekler 've ferîqan' (3. kelime) (okuma)",
 "edilgen: 7:28, 7:29 ve 7:30 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:28 'qâlû' (4.) ardından söz 5-10. kelime (REM sapması 7:28 (8. kelime) — 've'llâhu' söz içinde yeni cümle başı, konuşan 1P sürer), ayet içi kapanış; 7:28 'qul' (11.) ardından söz 12-22. kelime — ayet içi kapanış; 7:29 'qul' (1.) ardından söz 2-16. kelime — ayet içi kapanış; "
 "7:30 söz fiili yok, A3 '—' — 7:29 sözünün sürüp sürmediği metinde işaretsiz, söz 7:29 sonunda kapatıldı (okuma); mealde 'derler ki:' ve 'De ki:' ardından tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 28 30 08' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 7:28 've izâ' (1.) REM, 've'llâhu' (8.) REM; 7:29 've aqîmû' (5.) CONJ, 've'd'ûhu' (10.) CONJ; 7:30 've ferîqan' (3.) CONJ, 've yahsebûne' (14.) CIRC; 'fe' yok",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:28, 7:29 ve 7:30 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 28 30 08'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:28 (2:169); 7:29 (40:65); 7:30 bağ yok; D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:28 أله ×3, أمر ×2, فحش ×2, قول ×3; 7:30 فرق ×2, هدي ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:28 söz açılır (5. kelime), söz kapanır (10. kelime, ayet içi), söz açılır (12. kelime), söz kapanır (22. kelime, ayet içi), muhatap geçişi 2MS → 2MP (ayet içi), şahıs geçişi yok, edim geçişi nida → soru, emir; 7:29 söz açılır (2. kelime), söz kapanır (16. kelime, ayet içi), muhatap geçişi 2MS → 2MP (ayet içi), şahıs geçişi 3 → 2, edim geçişi soru, emir → emir; "
 "7:30 şahıs geçişi 2 → 3, edim geçişi emir → haber; ölçüm iltifât 7:28-30 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:28 've izâ fe'alû fâhişeten qâlû' — zaman zarfıyla açılan cümle ve ardındaki temel fiil (morph REM + T + PERF); 7:28 'e-teqûlûne 'ale'llâhi mâ lâ ta'lemûn' — soru ve ilgi cümlesi (morph INTG + IMPF + REL + NEG); "
 "7:29 've'd'ûhu muxlisîne' — emre bağlı durum bildiren ortaç (morph CONJ + IMPV + ACT_PCPL); 7:29 'kemâ bede'ekum' — benzetme edatı ve masdar 'mâ'sı (morph P + SUB + PERF); 7:30 'ferîqan hedâ' — öne alınmış nesne (morph INDEF + PERF); 7:30 've yahsebûne ennehum muhtedûn' — durum cümlesi ve 'enne' ile tümleç (morph CIRC + IMPF + ACC)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:28 18-22. kelime — 2:169 ile harekesiz eş (sayım: 'say 7:28 18-22'); 7:29 11-13. kelime — 40:65 ile harekesiz eş (sayım: 'say 7:29 11-13'); "
 "7:28 kök أله, أمر, فحش ve قول ikilemeleri; 7:30 kök فرق ve هدي ikilemeleri; 7:28 ve 7:29 'qul' buyruğu taşır (7:28 11. kelime, 7:29 1. kelime); 7:28 17-22. kelime okunmuş 1 ayetle harekesiz eş (sayım: 'say 7:28 17-22')",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 08'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "''ale'llâhi mâ lâ ta'lemûn' 7:28 'Allah hakkında bilmediğiniz şeyi' / 2:169 'Allah hakkında bilmediğiniz şeyleri' (emsal metninde) — çakışma — tam okuma sonu ('mâ' karşılığı 'şeyi' / 'şeyleri' — sayı farkı); "
 "'llâhi mâ lâ ta'lemûn' 7:28 'Allah hakkında bilmediğiniz şeyi' / 2:169 'Allah hakkında bilmediğiniz şeyleri' (emsal metninde) — çakışma — tam okuma sonu ('mâ' karşılığı 'şeyi' / 'şeyleri' — sayı farkı; alıntı 18. kelime karşılığını da taşıyor); "
 "'muxlisîne lehu'd-dîne' 7:29 'dini O'na hâlis kılarak' / 40:65 'dini O'na hâlis kılarak' (emsal metninde) — çakışma değil (bayt eşit); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:28 'fe'alû' PERF ('izâ' ile) — meal 'yaptıklarında'; 'qâlû' PERF — meal 'derler'; 'vecednâ' PERF — meal 'bulduk'; 'emera' PERF — meal 'emretti'; 'qul' IMPV — meal 'De'; "
 "'ye'muru' IMPF IND ('lâ' ile) — meal 'emretmez'; 'teqûlûne' IMPF IND ('e' ile) — meal 'söylüyorsunuz'; 'ta'lemûn' IMPF IND ('lâ' ile) — meal 'bilmediğiniz'; "
 "7:29 'qul' IMPV — meal 'De'; 'emera' PERF — meal 'emretti'; 'aqîmû' IMPV — meal 'doğrultun'; 'd'ûhu' IMPV — meal 'edin'; 'bede'e' PERF ('mâ' ile) — meal 'başlattığı'; 'te'ûdûn' IMPF IND — meal 'döneceksiniz'; "
 "7:30 'hedâ' PERF — meal 'gösterdi'; 'haqqa' PERF — meal 'oldu'; 'ttexazu' PERF — meal 'edindiler'; 'yahsebûne' IMPF IND — meal 'sanıyorlar'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle): 'fe'alû' PERF 7:28'de 'izâ' ile zarf-fiil ('-tıklarında') ile; 'qâlû' PERF 7:28'de 'izâ' kapsamında geniş zaman ('-rler') ile; 'ye'muru' IMPF 7:28'de geniş zaman ('-mez') ile; 'ta'lemûn' IMPF 7:28'de sıfat-fiil ('-diğiniz') ile; 'bede'e' PERF 7:29'da 'mâ' ile sıfat-fiil ('-tığı') ile; 'te'ûdûn' IMPF 7:29'da gelecek zaman ('-eceksiniz') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): 'mâ' (SUB: '-dığı' / '-tığı') — çakışma değil (ünsüz benzeşmesi); 've' (CONJ: 've' / 'de' / karşılıksız) — çakışma değil (atıf, karşılaştırmalı atıf, Türkçe sıralama); 've' (REM: 'ise' / 'da' / karşılıksız) — çakışma değil (yeni cümle başında konu değişimi, ekleme, zaman cümlesi başı)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 28 30 08'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:28, 7:29 ve 7:30 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:29 ('bede'ekum' / 'te'ûdûn'); 7:30 ('hedâ' / 'd-dalâletu'); 7:28 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök قول 7:28 ('qâlû', 'qul', 'e-teqûlûne') ve 7:29 ('qul'); kök أمر 7:28 ('emeranâ', 'ye'muru') ve 7:29 ('emera'); kök أله 7:28 ('ve'llâhu', 'llâhe', 'llâhi') ve 7:30 ('llâhi'), 7:26 ('llâhi') ile bölüm içi; kök أبو 7:28 ('âbâ'enâ'), 7:27 ('ebeveykum') ile bölüm içi; kök شطن 7:30 ('ş-şeyâtîne'), 7:27 ('ş-şeytânu', 'ş-şeyâtîne') ile bölüm içi; kök ولي 7:30 ('evliyâ'e'), 7:27 ('evliyâ'e') ile bölüm içi; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 3-2 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 7 ve 8; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b08/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 28 30 08'; lem_bozuk.py 08 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 28 30 → AYN_SONUC; sunum/bolum4_kurallar.py 28 30 08 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 28 30 08 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 38)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 8 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('qâle', ''alâ', 'allâh', 'mâ', 'lâ', ''alime', 'inne', ''inde', 'kull', 'mescid', 'de'â', 'muxlis', 'dîn', 'min', 'dûn'); joker '_' önek lemmalı öğede ('lehu' — 'dizi 7 29 10 13'; kelime gövdesi zamir, morph LEM yalnız 'li' önekinde); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

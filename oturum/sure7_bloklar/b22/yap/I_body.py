_OL = [l.replace('**', '') for l in open('/home/claude/b22/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b22/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK2 = _esc(re.search(r'aktör: adlı .*?rol meful\+muhatap\)', _OL[1]).group(0))
for _k, _v in (('_AK2', _AK2),): _MB = _MB.replace('" + %s + "' % _k, _v)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 75), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta araç kuralı değişmedi; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 492",
 "geriye dönük koşu (sûre 7 bölüm 7 kapanışı, komut 'python3 sunum/geriye_donuk.py b20k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 76 79 22'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:76, 7:77, 7:78 ve 7:79 esmâ yok; lafız yok; 7:77 Rab (6. kelime), 7:79 Rab (8. kelime); 7:76 ve 7:78 Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 76 79 22'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in range(76, 80)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 76 79 22'): KALAN_P",
 "ölçüm aktör: 7:77 adlı صالِح (8. kelime, rol meful+muhatap); 7:76, 7:78 ve 7:79 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:76 haber — kip yok; 7:77 emir, nida, şart — COND 1 'in' (12.), IMPV 1 'i'tinâ' (9.), VOC 1 'yâ sâlihu' (8.); "
 "7:78 haber — kip yok; 7:79 nida — CERT 1 'le-qad' (5.), EMPH 1 'le-qad' (5.), NEG 1 'lâ' (12.), VOC 1 'yâ qavmi' (4.)",
 "morph REL ('llezîne' 7:76 2., 'bi'llezî' 7:76 5., 'bi-mâ' 7:77 10.), AMD ('ve lâkin' 7:79 11.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:76, 7:77, 7:78 ve 7:79 yıldız yok",
 "fâsıla: 7:75 ن → 7:76 ن (" + _F[0] + ") → 7:77 ن (" + _F[1] + ") → 7:78 ن (" + _F[2] + ") → 7:79 ن (" + _F[3] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:76 xref yok; 7:77 51:44 (emsal olarak basıldı), 7:70, 11:32, 46:22 (basılmış), okunmuş 1 ayet; "
 "7:78 29:37 (emsal olarak basıldı), okunmuş 2 ayet ve okunmamış 1 ayet (sûre içi 1); 7:79 okunmuş 1 ayet ve okunmamış 1 ayet (sûre içi 1)",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:77 'etâ mâ ve'ade in kâne min' süzgeç GEÇER, 'in kâne min' süzgeç GEÇER; 7:78 'exaze racfe esbaha fî dâr câsim' süzgeç GEÇER (tür tam); "
 "7:79 'tevellâ 'an qâle qavm qad ebleğu risâle rabb nesahu _' süzgeç GEÇER, 'risâle rabb nesahu _' süzgeç GEÇER; 7:76 nakarat3 kalıbı yok; sûre içi eşler — 7:70 ve 7:62 (basılmış) ve basılmamış eşler",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:76 3MS ('qâle' — fiil uyumu, fail 2. kelime), 3MP ('stekberû' — gönderge 'llezîne' 2. kelime), söz içi konuşan 1P eki ('innâ'), söz içi muhatap 2MP ('âmentum'), 3MS eki ('bihî' — gönderge 'llezî' 5. kelime); "
 "7:77 adlı 'yâ sâlihu' (8.); 3MP (''aqarû', ''atev', 'qâlû' ve ek 'rabbihim' — gönderge 7:76 2. kelime), söz içi muhatap 2MS ('i'tinâ', 'te'idunâ', 'kunte'), söz içi konuşan 1P eki ('i'tinâ', 'te'idunâ'); "
 "7:78 3FS ('exazethumu' — fiil uyumu, fail 2. kelime), 3MP ('esbahû' ve ekler 'exazethumu', 'dârihim' — gönderge 7:76 2. kelime); "
 "7:79 3MS ('tevellâ', 'qâle' — gönderge 7:77 8. kelime), 3MP eki (''anhum' — gönderge 7:76 2. kelime), söz içi konuşan 1S ('ebleğtukum', 'nasahtu'; ekler 'qavmi', 'rabbî'), söz içi muhatap 2MP ('tuhibbûne'; ekler 'ebleğtukum', 'lekum')",
 "7:76-79 gönderge zinciri: 7:76 büyüklenenler ('llezîne' 2. kelime) 7:77, 7:78 ve 7:79 3MP göndergesi; 7:79 'tevellâ' ve 'qâle' göndergesi 7:77 8. kelimedeki Sâlih (okuma)",
 "edilgen: 7:76, 7:77, 7:78 ve 7:79 edilgen fiil yok (7:77 'l-murselîn' edilgen ortaç)",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:76 söz içi 4-8. kelime ('qâle' 1. kelime ardından); 7:77 söz içi 8-15. kelime ('qâlû' 7. kelime ardından); 7:78 söz yok; 7:79 söz içi 4-14. kelime ('qâle' 3. kelime ardından); "
 "REM sapması 7:79 (11. kelime) — söz içi 've', 'lâkin' karşıtlığıyla; "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 76 79 22' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 7:77 'fe-'aqarû' (1.) REM, 've 'atev' (3.) CONJ, 've qâlû' (7.) CONJ; 7:78 'fe-exazethumu' (1.) REM, 'fe-esbahû' (3.) REM; 7:79 'fe-tevellâ' (1.) REM, 've qâle' (3.) CONJ, 've nasahtu' (9.) CONJ, 've lâkin' (11.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:76, 7:77, 7:78 ve 7:79 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 76 79 22'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:77 (51:44), 7:78 (29:37); D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:79 نصح ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: bloğun emsal dosyasında olmayan basılmış eş (önceki bloklarda basılmış ya da sûre içi), bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:76 söz açılır / kapanır, şahıs geçişi yok, edim geçişi soru → haber; 7:77 söz açılır / kapanır, şart → cevap (COND 'in' 12. kelime; cevap 'i'tinâ' 9. kelime — öne alınmış), şahıs geçişi yok, edim geçişi haber → emir, nida, şart; "
 "7:78 şahıs geçişi yok, edim geçişi emir, nida, şart → haber; 7:79 söz açılır / kapanır, şahıs geçişi 3 → 1, edim geçişi haber → nida; ölçüm iltifât 7:76-79 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:76 'innâ bi'llezî âmentum' — tekit edatı, ilgi zamiri sıla cümlesiyle (morph ACC + P + REL + PERF); 7:78 'fe-exazethumu'r-racfetu' — istînâf, mazi ve belirli fail (morph REM + PERF + DET + N); "
 "7:79 'le-qad ebleğtukum' — yemin lâmı ve tahkik edatı ile mazi (morph EMPH + CERT + PERF)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:77 4-6. kelime — 51:44 ile harekesiz eş (sayım: 'say 7:77 4-6'); 7:78 1-6. kelime — 29:37 ile harekesiz eş (sayım: 'say 7:78 1-6'); 7:79 kök نصح ikilemesi",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 22'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "''an emri rabbihim' 7:77 'Rablerinin emrine' / 51:44 'Rablerinin emrine' (emsal metninde) — çakışma değil ('say 7:77 3-6' korpusta 1, 'dizi 7 77 3 6' 51:44 ile eş — önek farkı 've 'atev' / 'fe-'atev'); "
 "'fe-exazethumu'r-racfetu' 7:78 'Bunun üzerine onları sarsıntı yakaladı' / 29:37 'bunun üzerine onları şiddetli bir sarsıntı yakaladı' (emsal metninde) — çakışma — tam okuma sonu (daraltılmış kalıp — bag kalıbı iki satıra bölündü, meal kesimleri — 'şiddetli bir' emsalde fazla, büyük harf); "
 "'fe-esbahû fî dârihim câsimîn' 7:78 've yurtlarında diz üstü çöküp kaldılar' / 29:37 've yurtlarında diz üstü çöküp kaldılar' (emsal metninde) — çakışma değil; "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:76 'qâle' PERF — meal 'dedi'; 'stekberû' PERF — meal 'Büyüklenenler'; 'âmentum' PERF — meal 'ettiğinizi'; "
 "7:77 ''aqarû' PERF — meal 'kestiler'; ''atev' PERF — meal 'kaldırdılar'; 'qâlû' PERF — meal 'dediler'; 'i'tinâ' IMPV — meal 'getir'; 'te'idunâ' IMPF IND — meal 'vaat ettiğin'; 'kunte' PERF ('in' ile) — meal 'elçilerdensen'; "
 "7:78 'exazethumu' PERF — meal 'yakaladı'; 'esbahû' PERF — meal 'kaldılar'; 7:79 'tevellâ' PERF — meal 'yüz çevirdi'; 'qâle' PERF — meal 'dedi'; 'ebleğtukum' PERF ('le-qad' ile) — meal 'tebliğ ettim'; 'nasahtu' PERF — meal 'öğüt verdim'; 'tuhibbûne' IMPF IND ('lâ' ile) — meal 'sevmiyorsunuz'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle; IMPF IND geniş zaman karşılığı her blokta sapma sayılır — sûre 7 bölüm 3 denetimi kuralı 3): 'stekberû' PERF 7:76'da sıfat-fiil ('-enler') ile; 'âmentum' PERF 7:76'da sıfat-fiil ('-tiğinizi') ile; "
 "'te'idunâ' IMPF 7:77'de sıfat-fiil ('-tiğin') ile; 'kunte' PERF 7:77'de şart ('-sen') ile; 'tuhibbûne' IMPF 7:79'da şimdiki zaman ('-iyorsunuz') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): 'ellezîne' (REL: '-enler' / '-anlar' / '-en') — çakışma değil (sıfat-fiil çekimi); 'fe' (REM: 'Bunun üzerine' / 've' / 'Öyleyse' / karşılıksız) — çakışma değil (anlatı 'fe'si, ardışık olay / emir cümlesi başı); 'mâ' (REL: 'şeyi' / '-en') — çakışma değil (ad, sıfat-fiil); 'bi' (belirtme eki / '-la' / '-le' / yönelme eki) — çakışma değil (fiil yönetimi, araç); 'hum' ('onlardan' / 'onları' / iyelik eki) — çakışma değil (çekim ve tamlama); 'hî' (karşılıksız / 'onunla' / iyelik eki) — çakışma değil (ilgi zamirine dönen zamir, tümleç, tamlama); 'nâ' ('biz' / 'bize' / karşılıksız) — çakışma değil (özne, yönelme; nesne sonraki kelimede karşılandı)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 76 79 22'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:76, 7:77, 7:78 ve 7:79 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:76 ('âmentum' / 'kâfirûn'); 7:77, 7:78 ve 7:79 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök ربب 7:77 ('rabbihim') ve 7:79 ('rabbî') ile bölüm içi; kök رسل 7:77 ('l-murselîn') ve 7:79 ('risâlete') ile bölüm içi; kök قول 7:76 ('qâle'), 7:77 ('qâlû') ve 7:79 ('qâle') ile bölüm içi; "
 "bölümün önceki bloğuyla ortak kökler: أخذ (7:73, 7:74 / 7:78), أمن (7:75 / 7:76), ربب (7:73, 7:75 / 7:77, 7:79), رسل (7:75 / 7:77, 7:79), صلح (7:73, 7:75 / 7:77), قول (7:73, 7:75 / 7:76, 7:77, 7:79), قوم (7:73, 7:75 / 7:79), كبر (7:75 / 7:76), نوق (7:73 / 7:77); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 8-2 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 21, 22 ve sonrakiler; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b22/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 76 79 22'; lem_bozuk.py 22 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 76 79 → AYN_SONUC; sunum/bolum4_kurallar.py 76 79 22 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 76 79 22 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 44)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 22 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla (''ate', ''an', 'emr', 'rabb', 'etâ', 'mâ', 've'ade', 'in', 'kâne', 'min', 'exaze', 'racfe', 'esbaha', 'fî', 'dâr', 'câsim', 'tevellâ', 'qâle', 'qavm', 'qad', 'ebleğu' (morph LEM ham biçim), 'risâle', 'nesahu' (morph LEM ham biçim)); joker '_' dizi lemma dizisinde boş öğe olan zamir ve önek lemmalı kelimelerde ('lekum' 7:79 10.); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

_OL = [l.replace('**', '') for l in open('/home/claude/b07/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b07/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 25), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK1 = _esc(re.search(r'aktör: adlı .*?rol mecrur\)', _OL[0]).group(0))
_AK2 = _esc(re.search(r'aktör: adlı .*rol fail\+meful\)', _OL[1]).group(0))
_ES2 = _esc(re.search(r'esmâ \S+ 27\. sırada, ORTA konum, MÜHÜRSÜZ', _OL[1]).group(0))
_HP = _esc(re.search(r'HAPAKS: .*? — hapaks z=3,28', _OL[0]).group(0))
for _k, _v in (('_AK1', _AK1), ('_AK2', _AK2), ('_ES2', _ES2), ('_HP', _HP)): _MB = _MB.replace('" + %s + "' % _k, _v)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta araç kuralı değişmedi; bölüm 2 kapanışında sunum/bolum37_kurallar.py (kural 1-5) eklendi, sunum/geriye_donuk.py ve mutasyon_sina buna göre güncellendi — önceki commit'te, kapanış mutasyon sınaması 395 / 395; yeni kök ريش (7:26 9. kelime 've rîşen'; yamalar/yama_kok_7_26.py → kok_ekle_7.py, kok_turkce 1634; ölçüm yeniden alındı); mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 390",
 "geriye dönük koşu (sûre 7 bölüm 2 kapanışı, komut 'python3 sunum/geriye_donuk.py b06k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 26 27 07'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:27 'innâ ce'alne'ş-şeyâtîne evliyâ'e lillezîne lâ yu'minûn' (24-30. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (inanmayanların dostu kılınan şeytanlar) (yamalar/esma_el_7_26_27.txt); 7:26 esmâ yok; 7:26 lafız (17. kelime); 7:27 lafız yok; 7:26 ve 7:27 Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 26 27 07'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 7:27 muhur EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, araç tanımı farkı; muhur_el hayır): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in (26, 27)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 26 27 07'): KALAN_P",
 "ölçüm aktör: 7:26 '{{1|" + _AK1 + "}}' (A1'de 'âdeme'); 7:27 '{{2|" + _AK2 + "}}' (A1'de 'âdeme', 'ş-şeytânu' — 'yeftinennekumu' faili, 'l-cenneti' ve 'ş-şeyâtîne' — 'ce'alne' mefulü)",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:26 nida — CERT 1 'qad' (3.), VOC 1 'yâ' (1.); 7:27 nida — EMPH 1 'yeftinennekumu' (4.; 'n'), NEG 3 'lâ' (3., 22. ve 29.), VOC 1 'yâ' (1.); "
 "morph REM ('ve libâsu' 7:26 10.), DIST ve ADDR ('zâlike' 7:26 12. ve 14.), ACC ('le'allehum' 7:26 18., 'innehû' 7:27 16., 'innâ' 7:27 24.), SUB ('kemâ' 7:27 6.), PRP ('li-yuriyehumâ' 7:27 14.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:26 ★★★ (kaynak hapaks, z=3,28); 7:27 ★ (kaynak n, z=1,87)",
 "fâsıla: 7:25 ن → 7:26 ن (" + _F[0] + ") → 7:27 ن (" + _F[1] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:26 xref yok; 7:27 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:27 'min haysu lâ' süzgeç GEÇMEZ; 7:26 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:26 konuşan 1P ('enzelnâ'), muhatap 2MP eki (''aleykum', 'sev'âtikum'), 3MS ('yuvârî' — gönderge 'libâsen' 6. kelime), 3MP ('yezzekkerûn' — tartışmalı, gönderge 'benî' 1. kelime; ek 'le'allehum' — tartışmalı, gönderge 'benî' 1. kelime), aktör adlı 'âdeme'; "
 "7:27 3MS ('yeftinennekumu' — fiil uyumu, fail 5. kelime; 'axrace', 'yenzi'u', 'yerâkum', 'huve' — gönderge 'ş-şeytânu' 5. kelime; 'li-yuriyehumâ' — edilgen, naib-i faili zamir; morph PASS etiketi, okuma etken, gönderge 'ş-şeytânu' 5. kelime; ekler 'innehû', 've qabîluhû' — gönderge 'ş-şeytânu' 5. kelime), "
 "muhatap 2MP ('teravnehum'; ekler 'yeftinennekumu', 'ebeveykum', 'yerâkum'), 3D eki (''anhumâ', 'libâsehumâ', 'li-yuriyehumâ', 'sev'âtihimâ' — gönderge 'ebeveykum' 8. kelime), 3MP ('yu'minûn' — gönderge 'lillezîne' 28. kelime; ek 'teravnehum' — gönderge 've qabîluhû' 19. kelime), konuşan 1P ('ce'alne'; ek 'innâ'), "
 "aktör adlı 'âdeme', 'ş-şeytânu', 'l-cenneti' ve 'ş-şeyâtîne'",
 "7:26-27 gönderge zinciri: 7:26 ve 7:27 nida ile muhatap 'benî âdeme' (1-2. kelime); 7:26 'le'allehum' (18. kelime) ve 'yezzekkerûn' (19. kelime) 3MP — muhataptan gıyaba geçiş, gönderge 'benî' 1. kelime tartışmalı (ölçüm iltifât 0); 7:26 konuşan 1P ile 7:27 konuşan 1P eş (7:26 17. kelimede lafız 3. şahısla anılır); "
 "7:27 3MS fiil ve ekler 'ş-şeytânu' (5. kelime); 3D ekleri 'ebeveykum' (8. kelime); 'teravnehum' (23. kelime) 3MP eki 'huve ve qabîluhû' (18-19. kelime) toplamına; 'yu'minûn' (30. kelime) 'lillezîne' (28. kelime) ilgi adına (okuma)",
 "edilgen: 7:27 'li-yuriyehumâ' (14. kelime) morph PASS etiketli — ölçüm EDİLGEN 1/8; okuma IV. bab etken (fail şeytan, naib-i fail yok); 7:26 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:26 ve 7:27 söz fiili yok, A3 '—'; nida 'yâ benî âdeme' (1-2. kelime) doğrudan hitap — A4'te 'nidâ' ile; "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 26 27 07' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 7:26 've rîşen' (9.) CONJ, 've libâsu' (10.) REM; 7:27 've qabîluhû' (19.) CONJ; 'fe' yok",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:26 ve 7:27 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 26 27 07'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 2 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:26 ve 7:27 bağ yok; D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:26 لبس ×2; 7:27 رأي ×3, شطن ×2; ayetler arası kalıp 'yâ benî âdeme' (7:26, 7:27) — sayım 'say 7:26 1-2' ve lemma dizisi 'dizi 7 26 1 2' / 'dizi 7 27 1 2'; nida kalıbı, bağ kurulmadı (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "medde yazımıyla bulunan ek basılmış eşler ('say 7:26 16-17 --on --medde'): 2:61, 3:4, 6:33, 6:157, 40:63 — geniş kalıp, bağ kurulmadı; D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:26 bölüm açılışı, nidâ ('yâ benî âdeme' 1. kelime), şahıs geçişi 2 → 3, edim geçişi haber → nida; 7:27 nidâ ('yâ benî âdeme' 1. kelime), şahıs geçişi yok, edim geçişi yok; "
 "ölçüm iltifât 7:26-27 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:26 'libâsen yuvârî sev'âtikum' — nekre adı niteleyen fiil cümlesi (morph INDEF + IMPF); 7:26 've libâsu't-taqvâ zâlike xayrun' — yeni cümle başlangıcı ve işaret adıyla yinelenen özne (morph REM + DEM); 7:26 'le'allehum yezzekkerûn' — umma edatı ve haberi (morph ACC + IMPF); "
 "7:27 'lâ yeftinennekumu' — tekitli olumsuz muzâri, yasak anlamında (morph NEG + IMPF + EMPH); 7:27 'kemâ axrace' — benzetme edatı ve masdar 'mâ'sı (morph P + SUB + PERF); 7:27 'li-yuriyehumâ' — gerekçe lâmı (morph PRP + SUBJ); 7:27 'innehû yerâkum huve ve qabîluhû' — tekit, ayrı zamirle pekiştirme ve ona bağlanan ad (morph ACC + IMPF + PRON + CONJ)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:26 ve 7:27 'yâ benî âdeme' ile açılıyor (sayım: 'say 7:26 1-2', 'say 7:27 1-2'); 7:26 kök لبس ikilemesi; 7:27 kök رأي ve شطن ikilemeleri; "
 "7:26 'yuvârî' (7. kelime) ile 7:27 'li-yuriyehumâ' (14. kelime) gizleme / gösterme karşıtlığı kurar — ayetler arası, aday 1039 eşlemesine alınmadı; 7:26 9. kelime kökü ريش korpusta 1 (ölçüm HAPAKS)",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 07'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): bu blokta emsal yok; "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:26 'enzelnâ' PERF ('qad' ile) — meal 'indirdik'; 'yuvârî' IMPF IND — meal 'gizleyen'; 'yezzekkerûn' IMPF IND ('le'alle' ile) — meal 'düşünürler'; "
 "7:27 'yeftinenne' IMPF IND ('lâ' ve 'n' ile) — meal 'düşürmesin'; 'axrace' PERF ('mâ' ile) — meal 'çıkardığı'; 'yenzi'u' IMPF IND — meal 'alıyordu'; 'yuriye' IMPF SUBJ PASS ('li' ile) — meal 'göstermek'; 'yerâ' IMPF IND — meal 'görür'; 'teravne' IMPF IND ('lâ' ile) — meal 'görmediğiniz'; 'ce'alne' PERF — meal 'kıldık'; 'yu'minûn' IMPF IND ('lâ' ile) — meal 'inanmayanlara'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle): 'yuvârî' IMPF 7:26'da sıfat-fiil ('-en') ile; 'yeftinenne' IMPF IND 7:27'de 'lâ' ve 'n' ile olumsuz emir ('-mesin') ile; 'axrace' PERF 7:27'de 'mâ' ile sıfat-fiil ('-dığı') ile; 'yenzi'u' IMPF 7:27'de geçmişte süren hâl ('-ıyordu') ile; 'yuriye' IMPF SUBJ 7:27'de ad-fiil ('-mek') ile, morph PASS etiketi mealde etken; 'teravne' IMPF 7:27'de sıfat-fiil ('-diğiniz') ile; 'yu'minûn' IMPF 7:27'de sıfat-fiil ('-anlar') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): bölümün açılış bloğu — bölüm içinde önceki blok yok",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 26 27 07'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:26 ve 7:27 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:27 ('yerâkum' / 'lâ teravnehum'); 7:26 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök بني 7:26 ('benî') ve 7:27 ('benî'); kök أدم 7:26 ('âdeme') ve 7:27 ('âdeme'); kök لبس 7:26 ('libâsen', 've libâsu') ve 7:27 ('libâsehumâ'); kök سوأ 7:26 ('sev'âtikum') ve 7:27 ('sev'âtihimâ'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 3-1 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm açılışı bu blokta; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b07/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 26 27 07'; lem_bozuk.py 07 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 26 27 → AYN_SONUC; sunum/bolum4_kurallar.py 26 27 07 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 26 27 07 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 38)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 7 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal yok — ölçüm xref alanı 7:26 ve 7:27 için boş; emsal dosyası üretilmedi; önceki basım (sunum/onceki_basim.py): " + ONC + "; say2.txt sayımı basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('bunayy' (morph LEM ham biçim), 'âdem', 'min', 'haysu', 'lâ'); joker '_' kullanılmadı; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

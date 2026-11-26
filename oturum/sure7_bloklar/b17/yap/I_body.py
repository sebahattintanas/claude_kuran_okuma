_OL = [l.replace('**', '') for l in open('/home/claude/b17/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b17/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_HP = _esc(re.search(r'HAPAKS: .*? — hapaks z=3,28', _OL[1]).group(0))
for _k, _v in (('_HP', _HP),): _MB = _MB.replace('" + %s + "' % _k, _v)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 56), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta sunum/edat_etiket.py EDLEM'e 'beyne' (بين) eklendi — bölüm 15 denetimi kuralı 15 (es_edat tanınmayan edat başlığı 0): kalıp 'beyne yedey', 7:57 6. kelime; bölüm 5 kapanışında sunum/bolum41_kurallar.py (kural 1-5) eklendi — önceki commit'te, kapanış mutasyon sınaması 435 / 435; "
 "yeni kök نكد (7:58 12. kelime 'nekiden'; yamalar/yama_kok_7_57.py → kok_ekle_7.py, kok_turkce 1636; ölçüm yeniden alındı); mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 446",
 "geriye dönük koşu (sûre 7 bölüm 5 kapanışı, komut 'python3 sunum/geriye_donuk.py b15k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 57 58 17'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:57 ve 7:58 esmâ yok; 7:57 ve 7:58 lafız yok; 7:58 Rab (6. kelime); 7:57 Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 57 58 17'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in (57, 58)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 57 58 17'): KALAN_P",
 "ölçüm aktör: 7:57 ve 7:58 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:57 haber — kip yok; 7:58 haber — NEG 1 'lâ' (9.), RES 1 'illâ' (11.); ölçüm biçim HASR (D2'de yazılmadı); "
 "morph REM ('ve huve' 7:57 1., 've'l-beledu' 7:58 1.), REL ('llezî' 7:57 2., 'llezî' 7:58 7.), LOC ('beyne' 7:57 6.), INC ('hattâ' 7:57 9.), T ('izâ' 7:57 10.), ACC ('le'allekum' 7:57 28.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:57 ★ (kaynak n, z=1,76); 7:58 ★★★ (kaynak hapaks, z=3,28)",
 "fâsıla: 7:56 ن → 7:57 ن (" + _F[0] + ") → 7:58 ن (" + _F[1] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:57 25:48 (emsal olarak basıldı), 27:63 (basılmış), okunmuş 1 ayet; 7:58 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok (7:57 ve 7:58 ölçümünde nakarat3 alanı boş)'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:57 nakarat3 yok; 7:58 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:57 3MS ('huve' — gönderge 7:56 12. kelime; 'yursilu' — gönderge 'huve' 1. kelime; ekler 'rahmetihî' — gönderge 'huve' 1. kelime; 'suqnâhu' — gönderge 'sehâben' 12. kelime; 'bihi', 'bihî' — tartışmalı; gönderge 'li-beledin' 15. kelime), 3FS ('eqallet' — gönderge 'r-riyâha' 4. kelime), konuşan 1P ('suqnâhu', 'fe-enzelnâ', 'fe-exracnâ', 'nuxricu'), muhatap 2MP ('tezekkerûn'), muhatap 2MP eki ('le'allekum'); "
 "7:58 3MS ('yexrucu' 3. kelime — fiil uyumu, fail 4. kelime; 'xabuse', 'yexrucu' 10. kelime — gönderge 'llezî' 7. kelime; ekler 'nebâtuhû', 'rabbihî' — gönderge 'l-beledu' 1. kelime), konuşan 1P ('nusarrifu'), 3MP ('yeşkurûn' — gönderge 'li-qavmin' 16. kelime)",
 "7:57-58 gönderge zinciri: 7:57 'huve' (1. kelime) 7:56 12. kelimedeki lafız; 7:57 konuşan 1P ('suqnâhu' 14. kelime ve sonrası) 'huve' göndergesiyle eş — 3 → 1 şahıs değişimi ayet içi (ölçüm iltifât 0); 7:57 muhatap 2MP ('le'allekum' 28. kelime) 7:56 hitabıyla eş; 7:58 konuşan 1P ('nusarrifu' 14. kelime) 7:57 konuşan 1P ile eş; 7:58 'nebâtuhû', 'rabbihî' 3MS ekleri 'l-beledu' (1. kelime) (okuma)",
 "edilgen: 7:57 ve 7:58 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:57 ve 7:58 söz fiili yok, A3 '—'; "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 57 58 17' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 7:57 've huve' (1.) REM; 7:58 've'l-beledu' (1.) REM, 've'llezî' (7.) CONJ; 'fe' konumları: 7:57 'fe-enzelnâ' (17.) CONJ, 'fe-exracnâ' (20.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:57 ◈K روح ('r-riyâha' 4. kelime — K1), 7:57 ◈K سحب ('sehâben' 12. kelime — K1), 7:57 ◈K موه ('l-mâ'e' 19. kelime — K1), "
 "7:57 ◈B يدي ('yedey' 7. kelime — B3), 7:57 ◈B موت ('meyyitin' 16. kelime — B4), 7:57 ◈B موت ('l-mevtâ' 27. kelime — B4); 7:58 ◈B نبت ('nebâtuhû' 4. kelime — B1)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 57 58 17'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 2 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:57 (25:48); D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:57 خرج ×2, موت ×2; 7:58 خرج ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: bloğun emsal dosyasında olmayan basılmış eş (önceki bloklarda basılmış ya da sûre içi), bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:57 şahıs sayısında beraberlik (1P 7 · 3. şahıs 7 — ölçüm baskın 1), şahıs geçişi 2 → 1, edim geçişi emir, yasak → haber; 7:58 şahıs geçişi 1 → 3, edim geçişi yok, bölüm kapanışı; ölçüm iltifât 7:57-58 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:57 've huve'llezî yursilu'r-riyâha' — istînâf, zamir ve ilgi cümlesi (morph REM + PRON + REL + IMPF); 7:57 'hattâ izâ eqallet sehâben siqâlen' — gaye edatı ve zaman zarfı, mâzî fiil (morph INC + T + PERF); "
 "7:57 'fe-enzelnâ bihi'l-mâ'e fe-exracnâ bihî' — atıflı mâzîler (morph CONJ + PERF); 7:57 'le'allekum tezekkerûn' — ümit edatı ve muzâri (morph ACC + IMPF); 7:58 've'llezî xabuse lâ yexrucu illâ nekiden' — atıf, olumsuzluk ve hasr (morph CONJ + REL + NEG + RES)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:57 4-8. kelime — 25:48 ve 27:63 ile harekesiz eş (sayım: 'say 7:57 4-8'); 7:57 kök خرج ve موت ikilemeleri; 7:58 kök خرج ikilemesi; 7:57 kök خرج ve 7:58 kök خرج — bölüm içi",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 17'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'r-riyâha buşran beyne yedey rahmetihî' 7:57 'Rahmetinin önünde rüzgârları müjdeci' / 25:48 'Rahmetinin önünde rüzgârları müjdeci' (emsal metninde) — çakışma değil; "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:57 'yursilu' IMPF IND — meal 'gönderen'; 'eqallet' PERF ('izâ' ile) — meal 'yüklenince'; 'suqnâ' PERF — meal 'sürdük'; 'enzelnâ' PERF — meal 'indirdik'; 'exracnâ' PERF — meal 'çıkardık'; 'nuxricu' IMPF IND — meal 'çıkarırız'; 'tezekkerûn' IMPF IND ('le'alle' ile) — meal 'düşünürsünüz'; "
 "7:58 'yexrucu' IMPF IND (3. kelime) — meal 'çıkar'; 'xabuse' PERF — meal 'olan'; 'yexrucu' IMPF IND (10. kelime; 'lâ … illâ' ile) — meal 'çıkar'; 'nusarrifu' IMPF IND — meal 'açıklarız'; 'yeşkurûn' IMPF IND — meal 'Şükreden'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle; IMPF IND geniş zaman karşılığı her blokta sapma sayılır — sûre 7 bölüm 3 denetimi kuralı 3): 'yursilu' IMPF 7:57'de sıfat-fiil ('-en') ile; 'eqallet' PERF 7:57'de zarf-fiil ('-ince') ile; 'nuxricu' IMPF 7:57'de geniş zaman ('-ırız') ile; 'tezekkerûn' IMPF 7:57'de geniş zaman ('-ürsünüz') ile; "
 "'yexrucu' IMPF 7:58'de geniş zaman ('-ar') ile; 'xabuse' PERF 7:58'de sıfat-fiil ('-an') ile; 'nusarrifu' IMPF 7:58'de geniş zaman ('-rız') ile; 'yeşkurûn' IMPF 7:58'de sıfat-fiil ('-en') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): 'bi' ('-le' / '-la') — çakışma değil (ünlü uyumu); 'ellezî' (REL: '-en' / '-an') — çakışma değil (ünlü uyumu); 've' ('ve' / karşılıksız) — çakışma değil (atıf, cümle başı); 'hu' ('o' / 'O'na' / 'onu') — çakışma değil (yalın, yönelme ve belirtme çekimi); 'hî' ('o' / 'O'nun' / iyelik eki) — çakışma değil (yalın, tamlama); 'hû' ('O' / 'onu' / iyelik eki) — çakışma değil (yalın, belirtme, tamlama); 'kum' (iyelik eki / karşılıksız) — çakışma değil (tamlama; fiil çekimiyle karşılanan özne); 'li' (tamlayan eki / yönelme eki / 'için') — çakışma değil (sahiplik, yön, amaç); 'min' (yönelme eki / ayrılma eki) — çakışma değil (sıfat ve fiil yönetimi)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 57 58 17'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:57 tarayıcı adayı (kök ثمر, روح, سحب, موت, موه; C_recâ) — çıpa değil: rüzgâr, bulut, su ve ürün arasında nedensel bağ adlı, ölçü / mekanizma yok (olgu=True, kademe L2); 7:58 tarayıcı vermedi — temiz / kötü belde nitelikleri (olgu=True, kademe L1) (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:58 ('t-tayyibu' / 'xabuse'); 7:57 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök رحم 7:57 ('rahmetihî'), 7:56 ('rahmeta') ile bölüm içi; kök بلد 7:57 ('li-beledin') ve 7:58 ('ve'l-beledu') ile bölüm içi; kök خرج 7:57 ('fe-exracnâ', 'nuxricu') ve 7:58 ('yexrucu', 'yexrucu') ile bölüm içi; kök ربب 7:58 ('rabbihî'), 7:54 ('rabbekumu', 'rabbu') ve 7:55 ('rabbekum') ile bölüm içi; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 6-2 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 16 ve 17; bölüm kapanışı bu blokta; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b17/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 57 58 17'; lem_bozuk.py 17 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 57 58 → AYN_SONUC; sunum/bolum4_kurallar.py 57 58 17 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 57 58 17 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 42)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 17 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('ellezî', 'ersele', 'rîh', 'buşr', 'beyn', 'yed', 'rahme'); joker '_' bu blokta yok; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

_OL = [l.replace('**', '') for l in open('/home/claude/b16/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b16/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_HP = _esc(re.search(r'HAPAKS: .*? — hapaks z=3,28', _OL[0]).group(0))
for _k, _v in (('_HP', _HP),): _MB = _MB.replace('" + %s + "' % _k, _v)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 53), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta araç kuralı değişmedi; bölüm 5 kapanışında sunum/bolum41_kurallar.py (kural 1-5) eklendi, sunum/geriye_donuk.py ve mutasyon_sina buna göre güncellendi — önceki commit'te, kapanış mutasyon sınaması 435 / 435; "
 "yeni kök حثث (7:54 19. kelime 'hasîsen'; yamalar/yama_kok_7_54.py → kok_ekle_7.py, kok_turkce 1635; ölçüm yeniden alındı); mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 443",
 "geriye dönük koşu (sûre 7 bölüm 5 kapanışı, komut 'python3 sunum/geriye_donuk.py b15k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 54 56 16'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:56 'rahmeta'llâhi qarîbun' (11-13. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (rahmetin yakınlığı) (yamalar/esma_el_7_54_56.txt); 7:56 esma_kayit 'mühür EVET' / ölçüm MÜHÜRSÜZ — uyuşmuyor (esma_el 'degil' kararı; muhur_el ölçümle eş); 7:54 ve 7:55 esmâ yok; "
 "7:54 lafız (3. ve 30. kelime), 7:56 lafız (12. kelime); 7:55 lafız yok; 7:54 Rab (2. ve 31. kelime), 7:55 Rab (2. kelime); 7:56 Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 54 56 16'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 7:56 mühür EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, esma_el 'degil' kararı): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in (54, 55, 56)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 54 56 16'): KALAN_P",
 "ölçüm aktör: 7:54, 7:55 ve 7:56 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:54 haber — kip yok; ölçüm biçim DIKKAT (D2'de yazılmadı); 7:55 emir — IMPV 1 'ud'û' (1.), NEG 1 'lâ' (6.); 7:56 emir, yasak — IMPV 1 've'd'ûhu' (7.), PRO 1 'lâ' (1.); ölçüm biçim NEHY (D2'de yazılmadı); "
 "morph REL ('llezî' 7:54 4.), ATT ('elâ' 7:54 25.), T ('ba'de' 7:56 5.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:54 ★★★ (kaynak hapaks, z=3,28); 7:55 ★★ (kaynak rab, z=2,34); 7:56 yıldız yok",
 "fâsıla: 7:53 ن → 7:54 ن (" + _F[0] + ") → 7:55 ن (" + _F[1] + ") → 7:56 ن (" + _F[2] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:54 10:3 (emsal olarak basıldı), 13:3 (emsal olarak basıldı), 16:12 (emsal olarak basıldı), 22:18 (emsal olarak basıldı), okunmuş 1 ayet; 7:55 xref yok; 7:56 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:54 nakarat3 yok; 7:55 'inne lâ ahbeb' süzgeç GEÇMEZ; 7:56 'lâ efsedu fî ard ba'd islâh' süzgeç GEÇER, 'efsedu fî ard' süzgeç GEÇER; sûre içi eşler — 7:55 kalıbında 7:31 (basılmış), 7:56 kalıplarında basılmamış",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:54 muhatap 2MP eki ('rabbekumu'), 3MS ('xalaqa', 'stevâ' — gönderge 'llezî' 4. kelime; 'yuğşi' — gönderge 'llâhu' 3. kelime; 'yatlubuhû' — tartışmalı; gönderge 'l-leyle' 16. kelime; 'tebâraka' — fiil uyumu, fail 30. kelime; ekler 'yatlubuhû' — tartışmalı; gönderge 7:54 17. kelime; 'bi-emrihî', 'lehu' — gönderge 'llâhu' 3. kelime); "
 "7:55 muhatap 2MP ('ud'û'), muhatap 2MP eki ('rabbekum'), 3MS ('yuhibbu' — gönderge 'rabbekum' 2. kelime; ek 'innehû' — gönderge 'rabbekum' 2. kelime); "
 "7:56 muhatap 2MP ('tufsidû', 've'd'ûhu'), 3FS eki ('islâhihâ' — gönderge 'l-ardi' 4. kelime), 3MS eki ('ve'd'ûhu' — gönderge 7:55 2. kelime)",
 "7:54-56 gönderge zinciri: 7:54 muhatap 2MP eki ('rabbekumu' 2. kelime) bölüm açılışında genel hitap; 7:55 muhatap 2MP ('ud'û' 1. kelime, 'rabbekum' 2. kelime) 7:54 hitabıyla eş; 7:55 'innehû' ve 'yuhibbu' 3MS göndergesi 'rabbekum' (2. kelime); 7:56 muhatap 2MP ('tufsidû' 2. kelime, 've'd'ûhu' 7. kelime) 7:55 hitabıyla eş; 7:56 've'd'ûhu' 3MS eki 7:55 2. kelimedeki Rab (okuma)",
 "edilgen: 7:54, 7:55 ve 7:56 edilgen fiil yok; 7:54 'musaxxarâtin' (23. kelime) edilgen ortaç (ad)",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:54, 7:55 ve 7:56 söz fiili yok, A3 '—'; "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 54 56 16' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 7:54 've'l-arda' (7.), 've'ş-şemse' (20.), 've'l-qamera' (21.), 've'n-nucûme' (22.), 've'l-emru' (28.) CONJ; 7:55 've xufyeten' (4.) CONJ; 7:56 've lâ' (1.), 've'd'ûhu' (7.), 've tama'an' (9.) CONJ; 'fe' konumu yok",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:54 ◈K سمو ('s-semâvâti' 6. kelime — K1), 7:54 ◈K أرض ('l-arda' 7. kelime — K1), 7:54 ◈K يوم ('eyyâmin' 10. kelime — K2), 7:54 ◈K ليل ('l-leyle' 16. kelime — K1), 7:54 ◈K نهر ('n-nehâra' 17. kelime — K1), 7:54 ◈K شمس ('ş-şemse' 20. kelime — K1), 7:54 ◈K قمر ('l-qamera' 21. kelime — K1), 7:54 ◈K نجم ('n-nucûme' 22. kelime — K1), "
 "7:54 ◈B خلق ('xalaqa' 5. kelime — B2), 7:54 ◈B خلق ('l-xalqu' 27. kelime — B2); 7:56 ◈K أرض ('l-ardi' 4. kelime — K1); 7:55 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 54 56 16'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:54 (10:3, 13:3, 16:12, 22:18); D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:54 أله ×2, أمر ×2, خلق ×2, ربب ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: bloğun emsal dosyasında olmayan basılmış eş (önceki bloklarda basılmış ya da sûre içi), bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:54 bölüm açılışı, şahıs geçişi yok, edim geçişi soru → haber; 7:55 şahıs geçişi 3 → 2, edim geçişi haber → emir; 7:56 şahıs geçişi yok, edim geçişi emir → emir, yasak; ölçüm iltifât 7:54-56 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:54 'inne rabbekumu'llâhu'llezî xalaqa' — tekit edatı, isim cümlesi ve ilgi cümlesi (morph ACC + PN + REL + PERF); 7:54 'yuğşi'l-leyle'n-nehâra' — iki nesneli muzâri (morph IMPF + ACC + ACC); 7:54 've'ş-şemse ve'l-qamera ve'n-nucûme musaxxarâtin' — 5. kelimedeki fiile atıflı nesneler ve mansub edilgen ortaç (morph CONJ + ACC + PASS_PCPL); "
 "7:54 'elâ lehu'l-xalqu ve'l-emru' — dikkat edatı, öne alınmış haber (morph ATT + P + NOM); 7:55 'ud'û rabbekum tadarru'an ve xufyeten' — emir ve mansub mastar (morph IMPV + VN); 7:56 've lâ tufsidû' — atıf ve nehiy, meczum muzâri (morph CONJ + PRO + JUS); 7:56 'inne rahmeta'llâhi qarîbun' — tekit edatı ve müzekker haber (morph ACC + NOM)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:54 1-14. kelime ile açılıyor — 10:3 ile harekesiz eş (sayım: 'say 7:54 1-14'); 7:54 15-17. kelime — 13:3 ile harekesiz eş (sayım: 'say 7:54 15-17'); "
 "7:54 20-24. kelime — 16:12 ile harekesiz eş (sayım: 'say 7:54 20-24'); 7:54 20-22. kelime — 16:12 ve 22:18 ile harekesiz eş (sayım: 'say 7:54 20-22'); 7:54 kök أله, أمر, خلق ve ربب ikilemeleri; 7:56 1-6. kelime ile açılıyor — sûre içi basılmamış eşi var (sayım: 'say 7:56 1-6')",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 16'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'inne rabbekumu'llâhu'llezî xalaqa's-semâvâti ve'l-arda fî sitteti eyyâmin summe'stevâ 'ale'l-'arşi' 7:54 'Gerçekten Rabbiniz gökleri ve yeri altı günde yaratıp sonra arşa istivâ eden Allah'tır' / 10:3 'gökleri ve yeri altı günde yaratan, sonra arşa istivâ eden Allah'tır' (emsal metninde) — çakışma — tam okuma sonu ('-ıp' / '-an'); "
 "'yuğşi'l-leyle'n-nehâra' 7:54 'Geceyi gündüze bürür' / 13:3 'Geceyi gündüze bürüyor' (emsal metninde) — çakışma — tam okuma sonu ('-r' / '-yor'); "
 "'ve'ş-şemse ve'l-qamera ve'n-nucûme musaxxarâtin bi-emrihî' 7:54 'Güneşi ve ayı ve yıldızları O'nun emriyle boyun eğdirilmiş' / 16:12 'yıldızlar da O'nun emriyle boyun eğmiştir' (emsal metninde) — çakışma — tam okuma sonu ('boyun eğdir-' / 'boyun eğ-'); "
 "'ve'ş-şemse ve'l-qamera ve'n-nucûme' 7:54 'Güneşi ve ayı ve yıldızları' / 22:18 'güneş, ay, yıldızlar' (emsal metninde) — çakışma — tam okuma sonu (belirtme eki fiil yönetiminden); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:54 'xalaqa' PERF — meal 'yaratıp'; 'stevâ' PERF — meal 'eden'; 'yuğşî' IMPF IND — meal 'bürür'; 'yatlubu' IMPF IND — meal 'arar'; 'tebâraka' PERF — meal 'ne yücedir'; "
 "7:55 'ud'û' IMPV — meal 'dua edin'; 'yuhibbu' IMPF IND ('lâ' ile) — meal 'sevmez'; 7:56 'tufsidû' IMPF JUS ('lâ' ile) — meal 'yapmayın'; 've'd'ûhu' IMPV — meal 'dua edin'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle; IMPF IND geniş zaman karşılığı her blokta sapma sayılır — sûre 7 bölüm 3 denetimi kuralı 3): 'xalaqa' PERF 7:54'te zarf-fiil ('-ıp') ile; 'stevâ' PERF 7:54'te sıfat-fiil ('-en') ile; 'yuğşî' IMPF 7:54'te geniş zaman ('-r') ile; 'yatlubu' IMPF 7:54'te geniş zaman ('-r') ile; 'tebâraka' PERF 7:54'te ünlem cümlesi ('ne yücedir') ile; 'yuhibbu' IMPF 7:55'te geniş zaman ('-mez') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 54 56 16'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:54, 7:55 ve 7:56 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:54 ('l-leyle' / 'n-nehâra'); 7:56 ('xavfen' / 'tama'an'); 7:55 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök ربب 7:54 ('rabbekumu', 'rabbu') ve 7:55 ('rabbekum') ile bölüm içi; kök دعو 7:55 ('ud'û') ve 7:56 ('ve'd'ûhu') ile bölüm içi; kök أرض 7:54 ('ve'l-arda') ve 7:56 ('fi'l-ardi') ile bölüm içi; kök أله 7:54 ('llâhu', 'llâhu') ve 7:56 ('llâhi') ile bölüm içi; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 6-1 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 16 ve 17; bölüm açılışı bu blokta; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b16/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 54 56 16'; lem_bozuk.py 16 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 54 56 → AYN_SONUC; sunum/bolum4_kurallar.py 54 56 16 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 54 56 16 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 42)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 16 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('inne', 'rabb', 'allâh', 'ellezî', 'xalaqa', 'semâ'', 'ard', 'sitte', 'yevm', 'summe', 'istevâ', ''alâ', ''arş', 'uğşiyet' (morph LEM ham biçim), 'leyl', 'nehâr', 'şems', 'qamer', 'necm', 'musaxxare', 'emr', 'lâ', 'ahbeb' (morph LEM ham biçim), 'efsedu' (morph LEM ham biçim), 'fî', 'ba'd', 'islâh'); joker '_' bu blokta yok; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

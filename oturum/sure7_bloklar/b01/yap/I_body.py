_OL = [l for l in open('/home/claude/b01/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b01/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % n, _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta sunum/kelime_kontrol.py (bölüm 10 denetimi kuralı 6) morph INL etiketli kelimede (7:1 harf dizisi) harf adı alıntısını iskelet karşılaştırmasına sokmaz — harf adları ('elif lâm mîm sâd') yazılı biçimin harf iskeletiyle eşlenemiyor; başka araç kuralı değişmedi; bölüm 19 kapanışı (sunum/bolum35_kurallar.py kural 1-5) ve sûre 7 hazırlığı (sunum/sure.py ile sunum/sinifla.py varsayılan sûresi 7; sunum/denetim_7.sh; mutasyon_sina sûre 6 sınamaları sûre 6 blok dizinleriyle) önceki commit'lerde, hazırlık sonu mutasyon sınaması 374 / 374; yeni kök yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 358",
 "geriye dönük koşu (bölüm 19 kapanışı, sûre 6 kayıtlarında, komut 'python3 sunum/geriye_donuk.py b40k yamalar/geriye_donuk_6_b38k.txt'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 1 5 01'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:2 've zikrâ li'l-mu'minîn' (12-13. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (inanan insanlar); 7:3 've lâ tettebi'û min dûnihî evliyâ'' (7-11. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (O'ndan başka edinilen dostlar) (yamalar/esma_el_7_1_5.txt); 7:1, 7:4 ve 7:5 esmâ yok; 7:3 Rab (6. kelime); 7:1, 7:2, 7:4 ve 7:5 lafız ve Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 1 5 01'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 7:2 ve 7:3 muhur EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, araç tanımı farkı; muhur_el hayır): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in (1, 2, 3, 4, 5)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 1 5 01'): KALAN_P",
 "ölçüm aktör: 7:4 adsız `karye` 3. sırada (A1'de 'qaryetin'); 7:1, 7:2, 7:3 ve 7:5 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:1 haber — kip yok; 7:2 yasak — PRO 1 'lâ' (4.); ölçüm biçim NEHY (D2'de yazılmadı); 7:3 emir, yasak — IMPV 1 'ittebi'û' (1.), PRO 1 'lâ' (7.); ölçüm biçim NEHY (D2'de yazılmadı); "
 "7:4 haber — kip yok; 7:5 haber — NEG 1 'mâ' (1.), RES 1 'illâ' (7.); ölçüm biçim HASR (D2'de yazılmadı); "
 "morph REM ('fe-lâ' 7:2 4., 've kem' 7:4 1.), PRP ('li-tunzire' 7:2 10.), SUP ('mâ' 7:3 13.), SUB ('en' 7:5 8.), ACC ('innâ' 7:5 10.), INL (7:1 1.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:2 ★ (kaynak pas, z=1,57); 7:1, 7:3, 7:4 ve 7:5 yıldız yok",
 "fâsıla: 7:1 ٓ (" + _F[0] + ") → 7:2 ن (" + _F[1] + ") → 7:3 ن (" + _F[2] + ") → 7:4 ن (" + _F[3] + ") → 7:5 ن (" + _F[4] + ") — sûre açılışı ٓ sınıfında (harf dizisi), ardından N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:1 xref yok; 7:2 xref yok; 7:3 xref yok; 7:4 xref yok; 7:5 21:14 (emsal olarak basıldı), 21:46 (emsal olarak basıldı)",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:5 'illâ en qâle' süzgeç GEÇMEZ; 7:1, 7:2, 7:3 ve 7:4 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:1 zamir ve fiil yok (harf dizisi); "
 "7:2 3MS ('unzile' — edilgen, naib-i faili 'kitâbun' 1. kelime; 'yekun' — fiil uyumu, fail 8. kelime; 'minhu', 'bihî' eki — gönderge 'kitâbun' 1. kelime), muhatap 2MS ('li-tunzire'; ekler 'ileyke', 'sadrike'); "
 "7:3 muhatap 2MP ('ittebi'û', 'tettebi'û', 'tezekkerûn'; ekler 'ileykum', 'rabbikum'), 3MS ('unzile' — edilgen, naib-i faili 'mâ' 2. kelime; 'dûnihî' eki — gönderge 'rabbikum' 6. kelime); "
 "7:4 konuşan 1P ('ehleknâhâ'; ek 'be'sunâ'), 3FS eki ('ehleknâhâ', 'fe-câ'ehâ' — gönderge 'qaryetin' 3. kelime), 3MS ('fe-câ'ehâ' — fiil uyumu, fail 6. kelime), 3MP ('hum' — tartışmalı, cins uyumsuz, gönderge 'qaryetin' 3. kelime), aktör adsız 'qaryetin'; "
 "7:5 3MS ('kâne' — fiil uyumu, fail 3. kelime; 'câ'ehum' — fiil uyumu, fail 6. kelime), 3MP ('qâlû' — gönderge 7:4 9. kelime; ekler 'da'vâhum', 'câ'ehum' — gönderge 7:4 9. kelime), konuşan 1P eki ('be'sunâ'), konuşan 1P ('kunnâ' — söz içi; ek 'innâ' — söz içi)",
 "7:1-5 gönderge zinciri: 7:2 muhatap 2MS (adsız), 7:3'te muhatap 2MP'ye geçiş (1. kelime); 7:2 'minhu' ve 'bihî' göndergesi 'kitâbun' (1. kelime); 7:3 'dûnihî' göndergesi 'rabbikum' (6. kelime); 7:4 konuşan 1P (adsız) 7:5'te sürer ('be'sunâ' 6. kelime); 7:4 3FS ekleri 'qaryetin' (3. kelime), 'hum' (9. kelime) şehrin halkına geçiş — tartışmalı (cins ve sayı uyumu yok; gönderge A1'de de 'qaryetin' 3. kelime); "
 "7:5 3MP göndergeleri 7:4 9. kelime; 7:5 söz içi konuşan 1P sözü söyleyenler, söz dışı konuşan 1P'den ayrı (okuma)",
 "edilgen: 7:2 'unzile' (2. kelime; naib-i faili 'kitâbun') — ölçüm EDİLGEN 1/3; 7:3 'unzile' (3. kelime; naib-i faili 'mâ') — ölçüm EDİLGEN 1/4; 7:1, 7:4 ve 7:5 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:5 'qâlû' (9.) ardından söz 10-12. kelime, ayet sonunda kapanır; 7:1, 7:2, 7:3 ve 7:4 söz yok (okuma); mealde 'demeleri oldu:' ardından tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 1 5 01' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 7:2 've zikrâ' (12.) CONJ; 7:3 've lâ' (7.) CONJ; 7:4 've kem' (1.) REM; "
 "'fe' konumları: 7:2 'fe-lâ' (4.) REM; 7:4 'fe-câ'ehâ' (5.) CONJ; 7:5 'fe-mâ' (1.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:1, 7:2, 7:3, 7:4 ve 7:5 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 1 5 01'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:5 (21:14, 21:46); 7:1, 7:2, 7:3 ve 7:4 bağ yok; D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:3 تبع ×2; 7:5 كون ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11); medde sayımının basılmış eşi (yazım farkı ile, D3 dışı): 'say 7:5 4-6 --medde' 6:43",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:1 bölüm açılışı (sûre açılışı); 7:2 şahıs geçişi — → 3 (eksiltili — 7:1 şahıs işareti taşımıyor), edim geçişi haber → yasak; 7:3 şahıs geçişi 3 → 2, edim geçişi yasak → emir, yasak; 7:4 şahıs geçişi 2 → 1, şahıs sayısında toplam farkı (1P 3 · 3. şahıs 4 — ölçüm baskın 1), edim geçişi emir, yasak → haber; "
 "7:5 söz açılır (10. kelime), söz kapanır (12. kelime, ayet içi), şahıs geçişi 1 → 3, edim geçişi yok; "
 "ölçüm iltifât 7:1-5 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:2 'fe-lâ yekun fî sadrike haracun minhu' — ara cümle, yasak (morph REM + PRO); 7:2 'li-tunzire bihî' — gerekçe lâmı (morph PRP); 7:3 'qalîlen mâ tezekkerûn' — zâid 'mâ' ile pekiştirme (morph SUP); "
 "7:4 've kem min qaryetin' — çokluk bildiren 'kem' (morph REM); 7:4 'ev hum qâ'ilûn' — isim cümlesinin atfı (morph CONJ); 7:5 'fe-mâ kâne da'vâhum' ve 'illâ en qâlû' — olumsuzluk ve hasr (morph NEG + RES + SUB)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:1 harf dizisi 'elif lâm mîm sâd' ile açılıyor (sayım: 'say 7:1 1-1'); 7:5 10-12. kelime — 21:14 ve 21:46 ile harekesiz eş (sayım: 'say 7:5 10-12'); 7:3 kök تبع ikilemesi; 7:5 kök كون ikilemesi",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 01'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'innâ kunnâ zâlimîn' 7:5 'Biz gerçekten zalimmişiz' / 21:14 'Biz gerçekten zalimmişiz' (emsal metninde) — çakışma değil (bayt eşit); "
 "'innâ kunnâ zâlimîn' 7:5 'gerçekten zalimmişiz' / 21:46 'gerçekten zalimmişiz' (emsal metninde) — çakışma değil (bayt eşit); "
 "'kunnâ zâlimîn' 7:5 'zalimmişiz' / 21:14 'zalimmişiz' (emsal metninde) — çakışma değil (bayt eşit); 'kunnâ zâlimîn' 7:5 'zalimmişiz' / 21:46 'zalimmişiz' (emsal metninde) — çakışma değil (bayt eşit); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:1 fiil yok; 7:2 'unzile' PERF PASS — meal 'indirilen'; 'yekun' IMPF JUS ('lâ' ile) — meal 'olmasın'; 'tunzire' IMPF SUBJ ('li' ile) — meal 'uyarman'; "
 "7:3 'ittebi'û' IMPV — meal 'uyun'; 'unzile' PERF PASS — meal 'indirilene'; 'tettebi'û' IMPF JUS ('lâ' ile) — meal 'uymayın'; 'tezekkerûn' IMPF IND — meal 'düşünüyorsunuz'; "
 "7:4 'ehleknâ' PERF — meal 'ettik'; 'câ'e' PERF — meal 'geldi'; 7:5 'kâne' PERF ('mâ' ile) — meal 'oldu'; 'câ'e' PERF — meal 'geldiğinde'; 'qâlû' PERF ('en' ile) — meal 'demeleri'; 'kunnâ' PERF — meal 'zalimmişiz'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle): 'unzile' PERF 7:2 ve 7:3'te sıfat-fiil ('-en') ile; 'tunzire' IMPF SUBJ 7:2'de ad-fiil ('-man') ile; 'câ'e' PERF 7:5'te zarf-fiil ('-diğinde') ile; 'qâlû' PERF 7:5'te ad-fiil ('-meleri') ile; 'kunnâ' PERF 7:5'te ek fiil ('-mişiz') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): bölümün önceki bloğu yok",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 1 5 01'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:1, 7:2, 7:3, 7:4 ve 7:5 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:1, 7:2, 7:3, 7:4 ve 7:5 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök نزل 7:2 ('unzile') ve 7:3 ('unzile'); kök ذكر 7:2 ('zikrâ') ve 7:3 ('tezekkerûn'); kök جيأ 7:4 ('fe-câ'ehâ') ve 7:5 ('câ'ehum'); kök بأس 7:4 ('be'sunâ') ve 7:5 ('be'sunâ'); kök كون 7:2 ('yekun') ve 7:5 ('kâne', 'kunnâ'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 1-1 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 1 ve 2; bu blok bölümü ve sûreyi açıyor; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b01/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 1 5 01'; lem_bozuk.py 01 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 1 5 → AYN_SONUC; sunum/bolum4_kurallar.py 1 5 01 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 1 5 01 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 36)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 1 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('illâ', 'en', 'qâle', 'inne', 'kâne', 'zâlim'); joker '_' kullanılmadı; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

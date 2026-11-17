I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bölüm 12 denetiminin araç kuralları — sunum/bolum12_kurallar.py yeni (kurallar 2, 3, 4, 6, 8, 9); "
 "sunum/kural13.py kural 1 bütün ARIZA maddelerinde sayı sözcüğü + 'geçiş' / 'ayet' / 'kelime' / 'fiil' için konum listesi ister (kural 1); sunum/satir_aynen_tam.py biçim deseni '+' içeren alıntıyı kapsar (kural 5); "
 "sunum/geriye_donuk.py 'basılan değişti' sınıfı isabetteki ayetlerle basılan farkının kesişimiyle (kural 7) ve bolum12_kurallar; sunum/bolum11_kurallar.py kural 16 önceki kelimesi ''alâ' / 'fî' / 'ilâ' / ''an' olan 'llezîne'yi de kapsar (kural 10); "
 "sunum/mutasyon_sina.py bölüm 12 sınamaları (kural 7 hariç: geriye dönük koşunun kendisi); mutasyon_sina — MUT_SONUC; geriye dönük koşu son araç değişikliğinden sonra yeniden üretildi (GERI_P); "
 "yeni 172 — bolum12_kurallar 122 (kural 2: 82 — okunmuş bloklarda emsal maddesi kapalı sözlük dışı; kural 3: 19; kural 4: 11; kural 6: 2; kural 8: 1; kural 9: 7), kural13 50 (kural 1 bütün maddelere uygulandı), blok 28 kayıtlarının geriye dönük koşuya girmesiyle bolum9_kurallar 3, bolum10_kurallar 1, es_edat 1, gloss_tara 2; "
 "düşen 7 — araç değişti 4, basılan değişti 3; kayıtlar geriye dönük yeniden yazılmadı",
 "kök tablosu: ölçümde '???' 5:94 için 2 (HAPAKS alanı ve kökler alanı; kök رمح — 11. kelime 'rimâhukum') — kök tabloya eklendi (yamalar/yama_kok_5_94.py → kok_ekle_5.py; anlam 'mızrak'; 1 ayet; docstring dosya adı ve bölümle — bölüm 4 kuralı 16), ölçüm yeniden alındı, '???' 0; 5:95 ve 5:96 '???' 0; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 94 96 29'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:95 ''azîzun' (48. kelime) — esma_el 'ilahi', kural ''ve'llâhu X' kuralı'; 5:96 'l-berri' (12. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (kara); 5:94 esmâ yok; lafız üç ayet (5:94, 5:95, 5:96); Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 94 96 29'): " + EMH,
 "ölçüm: 5:94 '{{1|HAPAKS: رمح}}', '{{1|hapaks z=3,28}}', '{{1|fâsıla أليم → م, N sınıfı}}', '{{1|harf 111 → harf3 104, isaret 7}}' ve '{{1|dış düğüm 1}}'; "
 "5:95 '{{2|fâsıla ٱنتقام → م, N sınıfı}}', '{{2|simetri \\[4, 2, 7, 1\\]}}', '{{2|harf 210 → harf3 193, isaret 17}}' ve '{{2|dış düğüm 0}}'; "
 "5:96 '{{3|fâsıla تحشرون → ن, N sınıfı}}', '{{3|EDİLGEN 3/5 fiil, pas z=3,10}}', '{{3|simetri \\[3, 2, 10, 1\\]}}', '{{3|harf 91 → harf3 85, isaret 6}}' ve '{{3|dış düğüm 2}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 94 96 29'): KALAN_P",
 "ölçüm aktör: 5:95 '{{2|adlı كَعْبَة 26\\. sırada \\(yer, rol mecrur\\)}}' — 'bâliğa' muzâfun ileyhi; 5:94 ve 5:96 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 5:94 nida, şart — VOC 1 'yâ' (1.), EMPH 2 'le', 'nne' (4.), COND 1 'men' (17.); ölçüm biçim alanı '{{1|biçim DIKKAT}}' (yalnız bu maddede); "
 "5:95 yasak, nida, şart — VOC 1 'yâ' (1.), PRO 1 'lâ' (4.), COND 2 'men' (9., 42.); ölçüm biçim alanı '{{2|biçim DIKKAT \\+ NEHY}}' (yalnız bu maddede); 5:96 emir — IMPV 1 'ttequ' (16.); "
 "morph REM ('fe' 5:94 17.; 've' 5:95 9. ve 47., 5:96 16.), RSLT ('fe' 5:94 21., 5:95 13. ve 44.), CIRC ('ve entum' 5:95 7.), PRP ('li' 5:94 12., 5:95 35.) ve SUB ('mâ' 5:96 13.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 5:94 ★★★ (kaynak hapaks, z=3,28); 5:95 ★★★ (kaynak n, z=3,99); 5:96 ★★★ (kaynak pas, z=3,10)",
 "fâsıla: 5:93 ن (ٱلمحسنين) → 5:94 م (أليم) → 5:95 م (ٱنتقام) → 5:96 ن (تحشرون); bölüm açılışında kafiye م'ye geçiyor, 5:96'da ن'ye dönüyor (ölçümde kafiye bayrağı yok); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6 — basılmamış hedefler sinifla sayısıyla): 5:94 2:178 (emsal olarak basıldı); 5:95 xref yok; 5:96 58:9 (emsal olarak basıldı) ve okunmuş 1 ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:94 'eyy ellezî âmene' süzgeç GEÇER; 5:95 'eyy ellezî âmene lâ' ve 'eyy ellezî âmene' GEÇER, 'sayd _ harâm' ve 'zû 'adl min' GEÇMEZ; 5:96 'itteqâ allâh ellezî' GEÇMEZ",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "fail olmayan mecrur çoğul ad ve mecrur ilgi zamiri A1'de yazılmaz — bölüm 11 denetimi kuralları 16 ve 19; fiilden önce gelen lafız 'mübtedâ' — bölüm 12 denetimi kuralı 11; edilgen fiilde 'naib-i faili' — bölüm 11 denetimi kuralı 17): "
 "5:94 hitap, 3MP (adsız — 'âmenû'), Allah (lafız; 'le-yeblüvennekumu' ve 'li-ya'leme' faili — 3MS fiil uyumu), muhatap 2MP (adsız), 3FS ('tenâluhû' — fiil uyumu, fail 'eydîkum ve rimâhukum'), 3MS (adsız — 'tenâluhû' mef'ûlü, 'yaxâfuhû', 'meni'tedâ', 'lehû'), 'men' (ilgi; şart ismi); "
 "5:95 hitap, 3MP (adsız — 'âmenû'), muhatap 2MP (adsız), 'men' (şart ismi; 9. ve 42. kelime), 3MS (adsız — 'qatelehû', 'qatele', 'bihî', 'li-yezûqa', 'emrihî', 'selefe', ''âde', 'minhu'), 'zevâ 'adlin' ('yahkumu' faili — 3MS fiil uyumu), Kâbe (adlı yer; mecrur), Allah (lafız; ''afa' ve 'fe-yentaqimu' faili; 47. kelimede mübtedâ); "
 "5:96 'uhille' ve 'hurrime' (edilgen 3MS fiil uyumu; naib-i faili 'saydu'l-bahri' / 'saydu'l-berri'), muhatap 2MP (adsız; 'tuhşerûn' naib-i faili), 3MS (adsız — 'ta'âmuhû', 'ileyhi'), Allah (lafız; 'ttequ' mef'ûlü); "
 "'mesâkîne' (5:95 30. kelime; mecrur çoğul) ve 's-seyyârati' (5:96 8. kelime; mecrur) A1'de yazılmadı — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): bu blokta söz yok (A3 —); 'qul' yok (bölüm 10 denetimi kuralı 8); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 94 96 29' — A3 aralığında morph REM): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:94 've rimâhukum' (11.) CONJ, 'fe-meni'tedâ' (17.) REM, 'fe-lehû' (21.) RSLT; 5:95 've entum' (7.) CIRC, 've men' (9.) REM, 'fe-cezâ'un' (13.) RSLT, 'ev' (27., 31.) CONJ, 've men' (42.) CONJ, 'fe-yentaqimu' (44.) RSLT, 've'llâhu' (47.) REM; "
 "5:96 've ta'âmuhû' (5.), 've li's-seyyârati' (8.), 've hurrime' (9.) CONJ, 've'ttequ' (16.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 5:94 ◈B يدي ('eydîkum' 10. kelime — B3; anlam notu: avı erişecek eller); 5:95 ◈B نعم ('n-ne'ami' 18. kelime — B1; anlam notu: öldürülen avın dengi davar); 5:96 ◈K بحر ('l-bahri' 4. kelime — K1; anlam notu: avı helâl kılınan deniz)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 94 96 29'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:94 (2:178), 5:95 (3:4), 5:96 (58:9) (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "ayetler arası kalıp 'yâ eyyuhe'llezîne âmenû' (5:94, 5:95) — sayım 'say 5:94 1-3' ve lemma dizisi 'dizi 5 94 1 3' / 'dizi 5 95 1 3'; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:94 bölüm açılışı (bölüm 10 denetimi kuralı 2); hitap açılır; edim geçişi haber → nida, şart; şart → cevap ('men' 17. kelime); 5:95 hitap açılır; edim geçişi nida, şart → yasak, nida, şart; şart → cevap ('men' 9. ve 42. kelime); "
 "5:96 edim geçişi yasak, nida, şart → emir; şahıs geçişi 3 → 2",
 "sözdizimi (okuma; morph etiketiyle): 5:94 'le-yeblüvennekumu'llâhu' — kasem cevabı tekidi (morph EMPH 'le' + 'nne'); 'li-ya'leme'llâhu' — amaç (morph PRP); 'meni'tedâ … lehû 'azâbun elîm' — şart ve cevap (morph COND + RSLT önekli); "
 "5:95 'lâ taqtulu's-sayde ve entum hurum' — yasak (morph PRO) ve hâl (morph CIRC); 'men qatelehû … fe-cezâ'un' — şart ve cevap; 'ev … ev' — seçenek (morph CONJ); 'li-yezûqa' — amaç (morph PRP); 'men 'âde fe-yentaqimu'llâhu' — şart ve cevap; 've'llâhu 'azîzun zû'ntiqâm' — istînâf (morph REM); "
 "5:96 'uhille' ve 'hurrime' — edilgen (morph PASS); 'mâ dumtum hurumen' — süre (morph SUB); 'ttequ'llâhe' — emir (morph IMPV); 'ileyhi tuhşerûn' — edilgen (morph PASS)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:94 ve 5:95 'yâ eyyuhe'llezîne âmenû' ile açılıyor; "
 "5:95 kök قتل ikilemesi ('taqtulu' 5., 'qatelehû' 10., 'qatele' 16. kelime) ve kök نقم ikilemesi ('fe-yentaqimu' 44. / 'ntiqâm' 50. kelime); 5:96 kök صيد ('saydu' 3. ve 11. kelime) ve kök حرم ('hurrime' 9. / 'hurumen' 15. kelime)",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 29'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük): 'fe-meni'tedâ ba'de zâlike' 5:94 'Bundan sonra kim sınırı aşarsa' / 2:178 'Bundan sonra kim sınırı aşarsa' (emsal metninde) — çakışma değil; "
 "'ve'llâhu 'azîzun zû'ntiqâm' 5:95 'Allah azîzdir, intikam sahibidir' / 3:4 'Allah azîzdir, intikam sahibidir' (emsal metninde) — çakışma değil; "
 "'ve'ttequ'llâhe'llezî ileyhi tuhşerûn' 5:96 'Huzuruna toplanacağınız Allah'tan sakının' / 58:9 'Huzuruna toplanacağınız Allah'tan sakının' (emsal metninde) — çakışma değil",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 94 96 29'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:94, 5:95 ve 5:96 tarayıcı vermedi (cipa_tarama5_adaylari.json); doğa iddiası yok (olgu=False); L3 / L4 adayı yok",
 "aday 1039: ayet içi 5:95 (''afa'llâhu' / 'fe-yentaqimu'llâhu'), 5:96 ('uhille' / 'hurrime') — okuma; 5:94 ayet içi karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök صيد 5:94'te ('s-saydi' 8.), 5:95'te ('s-sayde' 6.) ve 5:96'da ('saydu' 3. ve 11.) — av sınaması, av yasağı, deniz / kara avı; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 13-1 (bölüm 7 kuralı 9 — blok_plani_5.txt'ten) — bölüm iki blok (29, 30); bu blok bölümü açıyor; başlıktaki 'İhramda av' 5:94-96; 'Kâbe ve haram ay', 'elçinin görevi' sonraki blokta; "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b29/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 94 96 29'; lem_bozuk.py 29 çıktısı): 5:94:4 'belev', 5:94:9 'yenâlu', 5:95:35 'zâqu', 5:95:44 'intaqam', 5:96:14 'dâmu' — lem_bozuk bayrağı; meal maddesinde '(morph LEM ham biçim)' notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 94 96 → AYN_SONUC; sunum/bolum4_kurallar.py 94 96 29 → KHATA_HEPSI; sunum/bolum5_kurallar.py 94 96 29 → B5_HEPSI; sunum/bolum6_kurallar.py 94 96 29 → B6_HEPSI; sunum/bolum7_kurallar.py 94 96 29 → B7_HEPSI; sunum/bolum8_kurallar.py 94 96 29 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 94 96 29 → B9_HEPSI; sunum/bolum10_kurallar.py 94 96 29 → B10_HEPSI; sunum/bolum11_kurallar.py 94 96 29 → B11_HEPSI; sunum/bolum12_kurallar.py 94 96 29 → B12_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 29 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('eyy', 'ellezî', 'âmene', 'lâ', 'sayd', 'harâm', 'zû', ''adl', 'min', 'itteqâ', 'allâh'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

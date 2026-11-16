# blok 18 (5:51-54) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b18/say2.txt'
os.environ['OLC'] = '/home/claude/b18/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Velî edinme; Allah'ın sevdiği kavim; dinle alay edenler' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 51: "Ey iman edenler! Yahudileri ve Nasârâ'yı velîler edinmeyin; onların bir kısmı, bir kısmının velîleridir. Sizden kim onları velî edinirse, kuşkusuz o onlardandır. Şüphesiz Allah zalimler kavmini doğru yola iletmez.",
 52: "Kalplerinde hastalık olanların onların içinde yarıştıklarını görürsün; derler ki: Bize bir felaketin dokunmasından korkuyoruz. Umulur ki Allah fethi ya da katından bir emri getirir de onlar kendi içlerinde gizlediklerine pişmanlık duyanlar olurlar.",
 53: "İman edenler de derler ki: Sizinle kesinlikle beraber olduklarına Allah'a yeminlerinin olanca gücüyle yemin edenler bunlar mı? Amelleri boşa gitti de hüsrana uğrayanlar oldular.",
 54: "Ey iman edenler! Sizden kim dininden dönerse, Allah yakında öyle bir kavim getirecek ki, Allah onları sever, onlar da O'nu severler; inananlara karşı alçak gönüllü, kâfirlere karşı onurludurlar; Allah yolunda cihad ederler ve hiçbir kınayanın kınamasından korkmazlar. Bu, Allah'ın lütfudur; onu dilediğine verir. Allah geniş olandır, bilendir.",
}

T51 = ("'âmenû' faili 3MP (adsız; nida edilenler, 3. kelime); muhatap 2MP (adsız; 'tettexizu' 5., 'minkum' 14. kelime); 'l-yehûde' (adlı aktör — cins; 6. kelime); 'n-nasârâ' (adlı aktör — cins; 7. kelime); 'ba'duhum' 3MP (adsız; 9. kelime); 'men' (şart ismi; 12. kelime); "
       "'yetevellehum' faili 3MS (adsız; 13. kelime); 'yetevellehum' mef'ûlü 3MP (adsız; 13. kelime); 'fe-innehû' 3MS (adsız; 15. kelime); 'minhum' 3MP (adsız; 16. kelime); Allah (lafız; 18. kelime); 'yehdi' faili 3MS (adsız; gönderge lafız, 20. kelime)")
T52 = ("muhatap 2MS (adsız; 'tera' 1. kelime); 'qulûbihim' 3MP (adsız; 4. kelime); 'maradun' (nekre; 5. kelime); 'yusâri'ûne' faili 3MP (adsız; 6. kelime); 'fîhim' 3MP (adsız; 7. kelime); 'yeqûlûne' faili 3MP (adsız; 8. kelime); "
       "konuşan 1P (adsız; söz içi; 'naxşâ' 9., 'tusîbenâ' 11. kelime); 'tusîbe' faili 3FS (adsız; gönderge 'dâ'iratun', 11. kelime); 'dâ'iratun' (nekre; 12. kelime); ''asa' faili 3MS (adsız; 13. kelime); Allah (lafız; 14. kelime); "
       "'ye'tiye' faili 3MS (adsız; gönderge lafız, 16. kelime); 'emrin' (nekre; 19. kelime); ''indihî' 3MS (adsız; 21. kelime); 'yusbihû' faili 3MP (adsız; 22. kelime); 'eserrû' faili 3MP (adsız; 25. kelime); 'enfusihim' 3MP (adsız; 27. kelime)")
T53 = ("'yeqûlu' faili 3MS (adsız; 1. kelime); 'âmenû' faili 3MP (adsız; 3. kelime); 'hâ'ulâ'i' (işaret ismi; 4. kelime); 'eqsemû' faili 3MP (adsız; söz içi; 6. kelime); Allah (lafız; 7. kelime); 'eymânihim' 3MP (adsız; 9. kelime); "
       "'innehum' 3MP (adsız; söz içi; 10. kelime); muhatap 2MP (adsız; söz içi; 'le-me'akum' 11. kelime); 'habitat' faili 3FS (adsız; gönderge 'a'mâluhum', 12. kelime); 'a'mâluhum' 3MP (adsız; 13. kelime); 'asbahû' faili 3MP (adsız; 14. kelime)")
T54 = ("'âmenû' faili 3MP (adsız; nida edilenler, 3. kelime); 'men' (şart ismi; 4. kelime); 'yertedde' faili 3MS (adsız; 5. kelime); muhatap 2MP (adsız; 'minkum' 6. kelime); 'dînihî' 3MS (adsız; 8. kelime); 'ye'ti' faili 3MS (adsız; gönderge lafız, 10. kelime); "
       "Allah (lafız; 11., 24., 31. ve 35. kelime); 'qavmin' (nekre; 12. kelime); 'yuhibbuhum' faili 3MS (adsız; gönderge lafız, 13. kelime); 'yuhibbuhum' mef'ûlü 3MP (adsız; 13. kelime); 'yuhibbûnehû' faili 3MP (adsız; 14. kelime); "
       "'yuhibbûnehû' mef'ûlü 3MS (adsız; gönderge lafız, 14. kelime); 'ezilletin' ve 'e'izzetin' (nekre; 15. ve 18. kelime); 'yucâhidûne' faili 3MP (adsız; 21. kelime); 'yexâfûne' faili 3MP (adsız; 26. kelime); 'lâ'im' (nekre; 28. kelime); "
       "'yu'tîhi' faili 3MS (adsız; 32. kelime); 'yu'tîhi' mef'ûlü 3MS (adsız; gönderge 'fadlu'llâh', 32. kelime); 'men' (ism-i mevsûl; 33. kelime); 'yeşâ'u' faili 3MS (adsız; 34. kelime); 'vâsi'un 'alîm' (nekre; 36-37. kelime)")

D = {}
D[51] = ("◇ 'yâ eyyuhe'llezîne âmenû lâ tettexizu'l-yehûde ve'n-nasârâ evliyâ'e ba'duhum evliyâ'u ba'din ve men yetevellehum minkum fe-innehû minhum inne'llâhe lâ yehdi'l-qavme'z-zâlimîn' — "
 "'yâ' + 'eyy' + 'hâ' + 'ellezî' + PERF 3MP IV. bab + 'lâ' + IMPF 2MP VIII. bab + belirli 'yehûd' + 've' + belirli çoğul 'nasrâniyy' + çoğul 'veliyy' + 'ba'd' + 3MP + çoğul 'veliyy' + nekre 'ba'd' + 've' + 'men' + IMPF 3MS V. bab + 3MP + 'min' + 2MP + 'fe' + 'inne' + 3MS + 'min' + 3MP + 'inne' + lafız + 'lâ' + IMPF 3MS I. bab + belirli 'qavm' + belirli çoğul 'zâlim' "
 "(ölçüm edim yasak, nida, şart, kip COND 1 · NEG 1 · PRO 1 · VOC 1, biçim DIKKAT + NEHY; 2MP 3 · 3MP 5 · 3MS 3; bab I. bab ×1 · IV. bab ×1 · V. bab ×1 · VIII. bab ×1). "
 "Allah lafzı 18. sırada (ölçüm allah z=0,38); Rab yok; ölçüm '{{1|esmâ \\S+ 8\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor) — 'evliyâ'' (8. ve 10. kelime), kural 'çoğul insan göndergeli → degil' (Yahudi ve Nasârâ velîleri); "
 "ölçüm '{{1|aktör: adlı \\S+ 6\\. sırada \\(cins, rol meful\\)}}', '{{1|adlı \\S+ 7\\. sırada \\(cins, rol meful\\)}}' — satır aynen. "
 "Ölçüm 'yıldız yok' — satır aynen; n=22 (n z=1,02); ölçüm '{{1|fâsıla ٱلظلمين → ن, N sınıfı}}' — satır aynen; ölçüm '{{1|simetri \\[3, 2, 12, 1\\]}}' — satır aynen; ölçüm '{{1|harf 110 → harf3 102, isaret 8}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen. "
 "Ölçüm VOC 1: 'yâ' (1. kelime); PRO 1: 'lâ' (4. kelime); COND 1: 'men' (12. kelime); NEG 1: 'lâ' (19. kelime); 've'n-nasârâ' (7.)'daki 've' CONJ, 've men' (12.)'deki 've' REM; 'fe-innehû' (15.)'daki 'fe' RSLT (okuma). "
 "Kök ikilemesi (ölçüm) بعض ×2 ('ba'duhum' 9. / 'ba'din' 11. kelime), ولي ×3 ('evliyâ'e' 8., 'evliyâ'u' 10., 'yetevellehum' 13. kelime) (okuma). "
 + T51 + " (okuma). "
 + cumle(say('say 5:51 1-3', "yâ eyyuhe'llezîne âmenû", True), say('say 5:51 1-4', "yâ eyyuhe'llezîne âmenû lâ"), say('dizi 5 51 1 4', "eyy ellezî âmene lâ"), say('say 5:51 1-5', "yâ eyyuhe'llezîne âmenû lâ tettexizu"), say('dizi 5 51 1 5', "eyy ellezî âmene lâ ittexaze")) + ' '
 + cumle(say('say 5:51 4-8', "lâ tettexizu'l-yehûde ve'n-nasârâ evliyâ'", True), say('say 5:51 5-6', "tettexizu'l-yehûd"), say('say 5:51 6-7', "l-yehûde ve'n-nasârâ"), say('lem 5:51:7', "nasrâniyy"), say('lem 5:51:8', "veliyy")) + ' '
 + cumle(say('say 5:51 9-11', "ba'duhum evliyâ'u ba'd", True), say('say 5:51 12-14 --on', "ve men yetevellehum minkum"), say('say 5:51 13-14', "yetevellehum minkum"), say('say 5:51 15-16 --on', "fe-innehû minhum")) + ' '
 + cumle(say('say 5:51 17-22', "inne'llâhe lâ yehdi'l-qavme'z-zâlimîn", True), say('say 5:51 17-21', "inne'llâhe lâ yehdi'l-qavm"), say('dizi 5 51 17 21', "inne allâh lâ hedâ qavm"), say('say 5:51 17-19', "inne'llâhe lâ"), say('dizi 5 51 17 19', "inne allâh lâ"),
         say('say 5:51 18-21', "llâhe lâ yehdi'l-qavm"), say('say 5:51 18-21 --on', "llâhe lâ yehdi'l-qavm"), say('dizi 5 51 18 21', "allâh lâ hedâ qavm"), say('say 5:51 20-22', "yehdi'l-qavme'z-zâlimîn"), say('say 5:51 21-22', "l-qavme'z-zâlimîn")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıpları: 'yâ eyyuhe'llezîne âmenû lâ tettexizu', 'inne'llâhe lâ yehdi'l-qavm', 'yâ eyyuhe'llezîne âmenû lâ', 'llâhe lâ yehdi'l-qavm', 'yâ eyyuhe'llezîne âmenû' ve 'inne'llâhe lâ' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'yâ' + 'eyy' + 'hâ' + 'ellezî' + PERF + 'lâ' + IMPF + belirli + 've' + belirli + çoğul + izafet + çoğul + nekre + 've' + 'men' + IMPF + 'min' + 'fe' + 'inne' + 'min' + 'inne' + lafız + 'lâ' + IMPF + belirli + belirli; "
 "D2 yasak, nida, şart, VOC ('yâ' 1. kelime), PRO ('lâ' 4. kelime), COND ('men' 12. kelime), NEG ('lâ' 19. kelime); D3 بعض ×2, ولي ×3; 4:144, 45:19 ve 28:50 eşleri; D4 2MP 3 · 3MP 5 · 3MS 3, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T51 + "; ölçüm aktör adlı Yahudi, Nasârâ (cins, meful); A2 velî edinme yasağı; Yahudi ve Nasârâ; velîlik; zalimler kavmi; hidayet; A3 —; "
 "A4 " + BOLUM + "; edim geçişi soru → yasak, nida, şart (ayetler arası); şahıs geçişi yok; şart → cevap (ayet içi; COND 'men' 12. kelime: 've men yetevellehum minkum' / 'fe-innehû minhum' (15. kelime)).",
)

D[52] = ("◇ 'fe-tera'llezîne fî qulûbihim maradun yusâri'ûne fîhim yeqûlûne naxşâ en tusîbenâ dâ'iratun fe-'asa'llâhu en ye'tiye bi'l-fethi ev emrin min 'indihî fe-yusbihû 'alâ mâ eserrû fî enfusihim nâdimîn' — "
 "'fe' + IMPF 2MS I. bab + 'ellezî' + 'fî' + çoğul 'qalb' + 3MP + nekre 'marad' + IMPF 3MP III. bab + 'fî' + 3MP + IMPF 3MP I. bab + IMPF 1P I. bab + 'en' + IMPF 3FS IV. bab + 1P + nekre 'dâ'ira' + 'fe' + PERF 3MS I. bab + lafız + 'en' + IMPF 3MS I. bab + 'bi' + belirli 'feth' + 'ev' + nekre 'emr' + 'min' + ''ind' + 3MS + 'fe' + IMPF 3MP IV. bab + ''alâ' + 'mâ' + PERF 3MP IV. bab + 'fî' + çoğul 'nefs' + 3MP + çoğul 'nâdim' "
 "(ölçüm edim haber, kip yok; 1P 2 · 2MS 1 · 3FS 1 · 3MP 11 · 3MS 3; bab I. bab ×5 · III. bab ×1 · IV. bab ×3). "
 "Allah lafzı 14. sırada (ölçüm allah z=0,19); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=28 (n z=1,65); ölçüm '{{2|fâsıla ندمين → ن, N sınıfı}}' — satır aynen; ölçüm '{{2|simetri \\[3, 2, 23, 1\\]}}' — satır aynen; ölçüm '{{2|harf 121 → harf3 114, isaret 7}}' — satır aynen; ölçüm '{{2|dış düğüm 2}}' — satır aynen. "
 "'fe-tera' (1.) ve 'fe-'asa' (13.)'daki 'fe' REM, 'fe-yusbihû' (22.)'daki 'fe' CONJ; 'ev' (18.) CONJ (okuma). "
 + T52 + " (okuma). "
 + cumle(say('say 5:52 1-7 --on', "fe-tera'llezîne fî qulûbihim maradun yusâri'ûne fîhim", True), say('say 5:52 2-5', "llezîne fî qulûbihim marad"), say('say 5:52 3-5', "fî qulûbihim marad"), say('say 5:52 4-5', "qulûbihim marad"), say('lem 5:52:5', "marad"), say('lem 5:52:6', "yusâri'u")) + ' '
 + cumle(say('say 5:52 8-12', "yeqûlûne naxşâ en tusîbenâ dâ'ira", True), say('say 5:52 10-12', "en tusîbenâ dâ'ira"), say('lem 5:52:12', "dâ'ira")) + ' '
 + cumle(say('say 5:52 13-21 --on', "fe-'asa'llâhu en ye'tiye bi'l-fethi ev emrin min 'indih", True), say('say 5:52 13-16 --on', "fe-'asa'llâhu en ye'tiye"), say('say 5:52 14-16', "llâhu en ye'tiye"), say('say 5:52 17-19', "bi'l-fethi ev emr"), say('say 5:52 20-21', "min 'indih")) + ' '
 + cumle(say('say 5:52 22-28 --on', "fe-yusbihû 'alâ mâ eserrû fî enfusihim nâdimîn", True), say('say 5:52 23-25', "'alâ mâ eserrû"), say('say 5:52 26-27', "fî enfusihim"), say('lem 5:52:28', "nâdim")) + ' '
 "Ölçüm xref 47:20 (emsal olarak basıldı) ve okunmuş başka ayet. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 'qulûbihim' (4. kelime); B4 —.",
 "◈D — D1 'fe' + IMPF + 'ellezî' + 'fî' + izafet + nekre + IMPF + 'fî' + IMPF + IMPF + 'en' + IMPF + nekre + 'fe' + PERF + lafız + 'en' + IMPF + 'bi' + belirli + 'ev' + nekre + 'min' + izafet + 'fe' + IMPF + ''alâ' + 'mâ' + PERF + 'fî' + izafet + çoğul; "
 "D2 haber, kip yok; D3 ikileme yok; 47:20 eşi; D4 1P 2 · 2MS 1 · 3FS 1 · 3MP 11 · 3MS 3, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T52 + "; aktör yok (ölçüm); A2 kalplerinde hastalık olanlar; yarışma; felaket korkusu; fetih ya da emir; gizlenen; pişmanlık; "
 "A3 'naxşâ en tusîbenâ dâ'ira' (söz içi, 9-12. kelime); "
 "A4 " + BOLUM + "; edim geçişi yasak, nida, şart → haber (ayetler arası); şahıs geçişi yok.",
)

D[53] = ("◇ 've yeqûlu'llezîne âmenû e-hâ'ulâ'i'llezîne eqsemû bi'llâhi cehde eymânihim innehum le-me'akum habitat a'mâluhum fe-asbahû xâsirîn' — "
 "'ve' + IMPF 3MS I. bab + 'ellezî' + PERF 3MP IV. bab + 'e' + 'hâ' + 'zâ' + 'ellezî' + PERF 3MP IV. bab + 'bi' + lafız + 'cehd' + çoğul 'yemîn' + 3MP + 'inne' + 3MP + 'le' + 'me'a' + 2MP + PERF 3FS I. bab + çoğul ''amel' + 3MP + 'fe' + PERF 3MP IV. bab + çoğul 'xâsir' "
 "(ölçüm edim soru, kip EMPH 1 · INTG 1, biçim DIKKAT + QASEM; 2MP 1 · 3FS 1 · 3MP 9 · 3MS 1; bab I. bab ×2 · IV. bab ×3). "
 "Allah lafzı 7. sırada (ölçüm allah z=0,81); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=15 (n z=0,27); ölçüm '{{3|fâsıla خسرين → ن, N sınıfı}}' — satır aynen; ölçüm '{{3|simetri \\[3, 4, 10, 1\\]}}' — satır aynen; ölçüm '{{3|harf 83 → harf3 78, isaret 5}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm INTG 1: 'e' (4. kelime); EMPH 1: 'le' (11. kelime); 've yeqûlu' (1.)'daki 've' REM, 'fe-asbahû' (14.)'daki 'fe' CONJ (okuma). "
 + T53 + " (okuma). "
 + cumle(say('say 5:53 1-3 --on', "ve yeqûlu'llezîne âmenû", True), say('say 5:53 2-3', "llezîne âmenû")) + ' '
 + cumle(say('say 5:53 4-9 --on', "e-hâ'ulâ'i'llezîne eqsemû bi'llâhi cehde eymânihim", True), say('say 5:53 4-5 --on', "e-hâ'ulâ'i'llezîne"), say('say 5:53 5-6', "llezîne eqsemû"), say('lem 5:53:6', "aqsemu"), say('say 5:53 7-9', "bi'llâhi cehde eymânihim"), say('say 5:53 8-9', "cehde eymânihim")) + ' '
 + cumle(say('say 5:53 10-11', "innehum le-me'akum", True), say('say 5:53 12-13', "habitat a'mâluhum"), say('lem 5:53:12', "habita"), say('say 5:53 14-15 --on', "fe-asbahû xâsirîn")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + IMPF + 'ellezî' + PERF + 'e' + 'hâ' + 'zâ' + 'ellezî' + PERF + 'bi' + lafız + 'cehd' + izafet + 'inne' + 'le' + 'me'a' + PERF + izafet + 'fe' + PERF + çoğul; "
 "D2 soru, INTG ('e' 4. kelime), EMPH ('le' 11. kelime); D3 ikileme yok; 24:53 eşi; D4 2MP 1 · 3FS 1 · 3MP 9 · 3MS 1, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T53 + "; aktör yok (ölçüm); A2 iman edenlerin sözü; yemin; beraberlik iddiası; amellerin boşa gitmesi; hüsran; "
 "A3 'e-hâ'ulâ'i'llezîne eqsemû bi'llâhi cehde eymânihim innehum le-me'akum' (söz içi, 4-11. kelime); "
 "A4 " + BOLUM + "; edim geçişi haber → soru (ayetler arası); şahıs geçişi yok.",
)

D[54] = ("◇ 'yâ eyyuhe'llezîne âmenû men yertedde minkum 'an dînihî fe-sevfe ye'ti'llâhu bi-qavmin yuhibbuhum ve yuhibbûnehû ezilletin 'ale'l-mu'minîne e'izzetin 'ale'l-kâfirîne yucâhidûne fî sebîli'llâhi ve lâ yexâfûne levmete lâ'im zâlike fadlu'llâhi yu'tîhi men yeşâ'u ve'llâhu vâsi'un 'alîm' — "
 "'yâ' + 'eyy' + 'hâ' + 'ellezî' + PERF 3MP IV. bab + 'men' + IMPF 3MS VIII. bab + 'min' + 2MP + ''an' + 'dîn' + 3MS + 'fe' + 'sevfe' + IMPF 3MS I. bab + lafız + 'bi' + nekre 'qavm' + IMPF 3MS IV. bab + 3MP + 've' + IMPF 3MP IV. bab + 3MS + nekre çoğul 'ezille' + ''alâ' + belirli çoğul ortaç 'mu'min' + nekre çoğul ''azîz' + ''alâ' + belirli çoğul ortaç 'kâfir' + IMPF 3MP III. bab + 'fî' + 'sebîl' + lafız + 've' + 'lâ' + IMPF 3MP I. bab + 'levme' + nekre ortaç 'lâ'im' + 'zâ' + 'li' + 'ke' + 'fadl' + lafız + IMPF 3MS IV. bab + 3MS + 'men' + IMPF 3MS I. bab + 've' + lafız + nekre ortaç 'vâsi'' + nekre ''alîm' "
 "(ölçüm edim nida, şart, kip COND 1 · FUT 1 · NEG 1 · VOC 1, biçim DIKKAT; 2MP 1 · 3MP 9 · 3MS 8; bab I. bab ×3 · III. bab ×1 · IV. bab ×4 · VIII. bab ×1). "
 "Allah lafzı 11., 24., 31. ve 35. sırada (ölçüm allah z=1,63); Rab yok; ölçüm '{{4|esmâ \\S+ 17\\. sırada, ORTA konum, MÜHÜR}}', '{{4|\\S+ 18\\. sırada, ORTA konum, MÜHÜR}}', '{{4|\\S+ 36\\. sırada, SON konum, MÜHÜR}}', '{{4|\\S+ 37\\. sırada, SON konum, MÜHÜR}}' — satır aynen; "
 "esma_el: 17. kelime kural 'çoğul insan göndergeli → degil' (inananlar); 18. kelime kural 'çoğul insan göndergeli → degil' (kavmin sıfatı); 36. ve 37. kelime kural ''ve'llâhu X' kuralı → ilahi' (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=37 (n z=2,61); ölçüm '{{4|fâsıla عليم → م, N sınıfı}}' — satır aynen; ölçüm '{{4|simetri \\[3, 2, 7, 1\\]}}' — satır aynen; ölçüm '{{4|harf 162 → harf3 155, isaret 7}}' — satır aynen; ölçüm '{{4|dış düğüm 5}}' — satır aynen. "
 "Ölçüm VOC 1: 'yâ' (1. kelime); COND 1: 'men' (4. kelime); FUT 1: 'sevfe' (9. kelime); NEG 1: 'lâ' (25. kelime); 've yuhibbûnehû' (14.)'daki 've' CONJ, 've lâ' (25.)'daki 've' CIRC, 've'llâhu' (35.)'daki 've' REM; 'fe-sevfe' (9.)'daki 'fe' RSLT (okuma). "
 "Kök ikilemesi (ölçüm) أتي ×2 ('ye'ti' 10. / 'yu'tîhi' 32. kelime), أله ×4 (lafız 11., 24., 31., 35. kelime), أمن ×2 ('âmenû' 3. / 'l-mu'minîne' 17. kelime), حبب ×2 ('yuhibbuhum' 13. / 'yuhibbûnehû' 14. kelime), لوم ×2 ('levmete' 27. / 'lâ'im' 28. kelime) (okuma). "
 + T54 + " (okuma). "
 + cumle(say('say 5:54 1-3', "yâ eyyuhe'llezîne âmenû", True), say('say 5:54 4-8', "men yertedde minkum 'an dînih"), say('say 5:54 6-8', "minkum 'an dînih")) + ' '
 + cumle(say('say 5:54 9-12 --on', "fe-sevfe ye'ti'llâhu bi-qavm", True), say('say 5:54 10-12', "ye'ti'llâhu bi-qavm"), say('say 5:54 13-14', "yuhibbuhum ve yuhibbûneh"), say('lem 5:54:13', "ahbeb")) + ' '
 + cumle(say('say 5:54 15-20', "ezilletin 'ale'l-mu'minîne e'izzetin 'ale'l-kâfirîn", True), say('say 5:54 15-17', "ezilletin 'ale'l-mu'minîn"), say('say 5:54 18-20', "e'izzetin 'ale'l-kâfirîn")) + ' '
 + cumle(say('say 5:54 21-24', "yucâhidûne fî sebîli'llâh", True), say('say 5:54 21-23', "yucâhidûne fî sebîl"), say('dizi 5 54 21 23', "câhede fî sebîl"), say('say 5:54 22-24', "fî sebîli'llâh"), say('say 5:54 25-28 --on', "ve lâ yexâfûne levmete lâ'im"), say('say 5:54 27-28', "levmete lâ'im")) + ' '
 + cumle(say('say 5:54 29-31', "zâlike fadlu'llâh", True), say('say 5:54 30-31', "fadlu'llâh"), say('say 5:54 32-34', "yu'tîhi men yeşâ'"), say('say 5:54 33-35', "men yeşâ'u ve'llâh"), say('dizi 5 54 33 35', "men şâ'e allâh"), say('say 5:54 33-34', "men yeşâ'"),
         say('say 5:54 35-37 --on', "ve'llâhu vâsi'un 'alîm"), say('say 5:54 36-37', "vâsi'un 'alîm")) + ' '
 "Ölçüm xref 62:4 (emsal olarak basıldı) ve okunmuş başka ayetler. "
 "Ölçüm nakarat3 kalıpları: 'yâ eyyuhe'llezîne âmenû' süzgeç GEÇER; 'men yeşâ'u ve'llâh' ve 'yucâhidûne fî sebîl' GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'ezilletin 'ale'l-mu'minîne' / 'e'izzetin 'ale'l-kâfirîn' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'yâ' + 'eyy' + 'hâ' + 'ellezî' + PERF + 'men' + IMPF + 'min' + ''an' + izafet + 'fe' + 'sevfe' + IMPF + lafız + 'bi' + nekre + IMPF + 've' + IMPF + nekre + ''alâ' + belirli + nekre + ''alâ' + belirli + IMPF + 'fî' + izafet + lafız + 've' + 'lâ' + IMPF + izafet + nekre + 'zâ' + izafet + lafız + IMPF + 'men' + IMPF + 've' + lafız + nekre + nekre; "
 "D2 nida, şart, VOC ('yâ' 1. kelime), COND ('men' 4. kelime), FUT ('sevfe' 9. kelime), NEG ('lâ' 25. kelime); D3 أتي ×2, أله ×4, أمن ×2, حبب ×2, لوم ×2; 62:4 ve 2:268 eşleri; D4 2MP 1 · 3MP 9 · 3MS 8, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T54 + "; aktör yok (ölçüm); A2 dinden dönme; Allah'ın getireceği kavim; karşılıklı sevgi; inananlara alçak gönüllülük; kâfirlere onur; cihad; kınanma korkusuzluğu; lütuf; A3 —; "
 "A4 " + BOLUM + "; edim geçişi soru → nida, şart (ayetler arası); şahıs geçişi yok; şart → cevap (ayet içi; COND 'men' 4. kelime: 'men yertedde minkum 'an dînih' / 'fe-sevfe ye'ti'llâhu bi-qavm' (9. kelime)).",
)

out = ['# ── blok 5:51-54 (2026-11-15) ──', 'MEAL18 = {']
for n in range(51, 55):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M18 = {']
for n in range(51, 55):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL18); M.update(M18)']
open('/home/claude/yamalar/metin_5_51_54.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

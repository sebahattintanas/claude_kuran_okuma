# blok 26 (5:82-86) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b26/say2.txt'
os.environ['OLC'] = '/home/claude/b26/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Lanetlenenler; Nasârâ'nın yakınlığı; gözyaşı dökenler' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 82: "İnsanların, iman edenlere düşmanlıkça en şiddetlisinin Yahudiler ve ortak koşanlar olduğunu mutlaka bulursun; iman edenlere sevgice en yakınlarının da 'Biz Nasârâ'yız' diyenler olduğunu mutlaka bulursun. Bu, onlardan keşişler ve rahipler bulunması ve onların büyüklenmemeleri yüzündendir.",
 83: "Elçiye indirileni işittiklerinde, tanıdıkları haktan ötürü gözlerinin yaştan taştığını görürsün. Derler ki: 'Rabbimiz, iman ettik; bizi şahitlerle birlikte yaz.",
 84: "Bize ne oluyor ki Allah'a ve bize haktan gelene iman etmeyelim, Rabbimizin bizi salih kavimle birlikte sokmasını umarken?'",
 85: "Söyledikleri sebebiyle Allah onları, altlarından ırmaklar akan, içinde kalacakları cennetlerle ödüllendirdi. İşte bu, iyilik edenlerin karşılığıdır.",
 86: "İnkâr edip âyetlerimizi yalanlayanlar ise, işte onlar alevli ateşin halkıdır.",
}

T82 = ("muhatap 2MS (adsız; 1. ve 10. kelime — 'tecidenne'); 'eşedde'n-nâsi' ('tecidenne' 1. mef'ûlü; 2-3. kelime); 'llezîne âmenu' (5-6. ve 13-14. kelime); 'âmenu' faili 3MP (adsız; 6. ve 14. kelime); "
       "'l-yehûde' (adlı cins; 'tecidenne' 2. mef'ûlü; 7. kelime); 'llezîne eşrakû' (8-9. kelime); 'eşrakû' faili 3MP (adsız; 9. kelime); 'aqrabehum' ('tecidenne' 1. mef'ûlü; iyelik 3MP, adsız; 11. kelime); "
       "'llezîne qâlû' ('tecidenne' 2. mef'ûlü; 15-16. kelime); 'qâlû' faili 3MP (adsız; 16. kelime); söz içi konuşan 1P (adsız; 'innâ', 17. kelime); 'nasârâ' (adlı cins; söz içi; 18. kelime); "
       "'minhum' 3MP (adsız; 21. kelime); 'qissîsîne ve ruhbânen' ('enne' ismi; 22-23. kelime); 'ennehum' 3MP (adsız; 24. kelime); 'yestekbirûn' faili 3MP (adsız; 26. kelime)")
T83 = ("'semi'û' faili 3MP (adsız; 2. kelime); 'unzile' 3MS (adsız; edilgen; 4. kelime — naib-i fail mevsûl 'mâ'); 'r-resûli' (6. kelime); muhatap 2MS (adsız; 7. kelime — 'terâ'); 'a'yunehum' ('terâ' mef'ûlü; iyelik 3MP, adsız; 8. kelime); "
       "'tefîdu' 3FS (adsız; gönderge 'a'yunehum', 9. kelime); ''arafû' faili 3MP (adsız; 13. kelime); 'yeqûlûne' faili 3MP (adsız; 16. kelime); söz içi Rab ('rabbenâ' nida; iyelik 1P, adsız; 17. kelime); söz içi konuşan 1P (adsız; 'rabbenâ', 'âmennâ', 'fe'ktubnâ' — 17-19. kelime); "
       "söz içi muhatap 2MS (adsız; 'fe'ktubnâ' emri, gönderge Rab, 19. kelime); 'ş-şâhidîn' (21. kelime)")
T84 = ("söz içi konuşan 1P (adsız; 'lenâ', 'nu'minu', 'câ'enâ', 'natma'u', 'yudxilenâ', 'rabbunâ' — 2., 4., 7., 10., 12., 13. kelime); söz içi Allah (lafız; 5. kelime); 'câ'enâ' 3MS (adsız; gönderge 'mâ', 7. kelime); "
       "'yudxilenâ' 3MS (fiil uyumu; 12. kelime — fail 13. kelime); söz içi Rab ('rabbunâ'; 12. kelimedeki fiilin faili; iyelik 1P, adsız; 13. kelime); 'l-qavmi's-sâlihîn' (15-16. kelime)")
T85 = ("'esâbehumu' 3MS (fiil uyumu; 1. kelime — fail 2. kelime); 'esâbehumu' mef'ûlü 3MP (adsız; 1. kelime); Allah (lafız; 1. kelimedeki fiilin faili; 2. kelime); 'qâlû' faili 3MP (adsız; 4. kelime); "
       "'tecrî' 3FS (fiil uyumu; 6. kelime — fail 9. kelime); 'tahtihe' 3FS (adsız; gönderge 'cennâtin', 8. kelime); 'l-enhâru' ('tecrî' faili; 9. kelime); 'xâlidîne' (sahibi 1. kelimedeki mef'ûl; 10. kelime); "
       "'fîhâ' 3FS (adsız; gönderge 'cennâtin', 11. kelime); 'l-muhsinîn' (14. kelime)")
T86 = ("'llezîne keferû' (1-2. kelime); 'keferû' ve 'kezzebû' faili 3MP (adsız; 2. ve 3. kelime); 'âyâtinâ' iyelik 1P (adsız; konuşan, gönderge Allah; 4. kelime); 'ulâ'ike' (işaret; gönderge 'llezîne keferû'; 5. kelime); 'ashâbu'l-cahîm' (6-7. kelime)")

D = {}
D[82] = ("◇ 'le-tecidenne eşedde'n-nâsi 'adâveten li'llezîne âmenu'l-yehûde ve'llezîne eşrakû ve le-tecidenne aqrabehum meveddeten li'llezîne âmenu'llezîne qâlû innâ nasârâ zâlike bi-enne minhum qissîsîne ve ruhbânen ve ennehum lâ yestekbirûn' — "
 "'le' + IMPF 2MS I. bab + 'nne' + ism-i tafdîl 'eşedd' + belirli 'nâs' + nekre ''adâve' + 'li' + 'ellezî' + PERF 3MP IV. bab + özel ad 'yehûd' + 've' + 'ellezî' + PERF 3MP IV. bab + 've' + 'le' + IMPF 2MS I. bab + 'nne' + ism-i tafdîl 'aqrab' + 3MP + nekre 'mevedde' + 'li' + 'ellezî' + PERF 3MP IV. bab + 'ellezî' + PERF 3MP I. bab + 'inne' + 1P + özel ad 'nasrânî' + 'zâlike' + 'bi' + 'enne' + 'min' + 3MP + çoğul 'qissîs' + 've' + çoğul 'ruhbân' + 've' + 'enne' + 3MP + 'lâ' + IMPF 3MP X. bab "
 "(ölçüm edim haber, kip EMPH 4 · NEG 1; 1P 1 · 2MS 2 · 3MP 13; bab I. bab ×3 · IV. bab ×3 · X. bab ×1). "
 "Lafız yok; Rab yok; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); ölçüm aktör '{{1|adlı يَهُود 7\\. sırada \\(cins, rol meful\\)}}' ve '{{1|adlı نَصْرانِيّ 18\\. sırada \\(cins, rol fail\\)}}' — satır aynen. "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=26 (n z=1,44); ölçüm '{{1|HAPAKS: قسس}}' — satır aynen (kök bu blokta tabloya eklendi); ölçüm '{{1|hapaks z=3,28}}' — satır aynen; ölçüm '{{1|fâsıla يستكبرون → ن, N sınıfı}}' — satır aynen; "
 "ölçüm '{{1|simetri \\[3, 5, 13, 1\\]}}' — satır aynen; ölçüm '{{1|harf 138 → harf3 128, isaret 10}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen. "
 "Ölçüm EMPH 4: 'le' ve 'nne' (1. ve 10. kelime); NEG 1: 'lâ' (25. kelime); 've'llezîne' (8.), 've le-tecidenne' (10.), 've ruhbânen' (23.) ve 've ennehum' (24.)'daki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) أمن ×2 ('âmenu' 6. / 14. kelime), وجد ×2 ('tecidenne' 1. / 10. kelime) (okuma). "
 + T82 + " (okuma). "
 + cumle(say('say 5:82 1-4', "le-tecidenne eşedde'n-nâsi 'adâveten", True), say('say 5:82 1-3', "le-tecidenne eşedde'n-nâs"), say('say 5:82 2-3', "eşedde'n-nâs")) + ' '
 + cumle(say('say 5:82 5-7', "li'llezîne âmenu'l-yehûd", True), say('say 5:82 5-6', "li'llezîne âmenû"), say('say 5:82 8-9 --on', "ve'llezîne eşrakû")) + ' '
 + cumle(say('say 5:82 10-12 --on', "ve le-tecidenne aqrabehum meveddeten", True), say('say 5:82 11-12', "aqrabehum meveddeten")) + ' '
 + cumle(say('say 5:82 15-18', "llezîne qâlû innâ nasârâ", True), say('say 5:82 16-18', "qâlû innâ nasârâ"), say('dizi 5 82 15 18', "ellezî qâle inne nasrânî")) + ' '
 + cumle(say('say 5:82 19-23', "zâlike bi-enne minhum qissîsîne ve ruhbânâ", True), say('say 5:82 21-23', "minhum qissîsîne ve ruhbânâ"), say('say 5:82 22-23 --on', "qissîsîne ve ruhbânâ")) + ' '
 + cumle(say('say 5:82 24-26 --on', "ve ennehum lâ yestekbirûn", True), say('say 5:82 25-26', "lâ yestekbirûn")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: 'ellezî qâle inne nasrânî' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'eşedde'n-nâsi 'adâveten' / 'aqrabehum meveddeten' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 'n-nâsi' (3. kelime); B2 —; B3 —; B4 —.",
 "◈D — D1 'le' + IMPF + 'nne' + ism-i tafdîl + belirli + nekre + 'li' + 'ellezî' + PERF + özel ad + 've' + 'ellezî' + PERF + 've' + 'le' + IMPF + 'nne' + ism-i tafdîl + nekre + 'li' + 'ellezî' + PERF + 'ellezî' + PERF + 'inne' + özel ad + 'zâlike' + 'bi' + 'enne' + 'min' + çoğul + 've' + çoğul + 've' + 'enne' + 'lâ' + IMPF; "
 "D2 haber, EMPH ('le' 1. ve 10. kelime), NEG ('lâ' 25. kelime); D3 أمن ×2, وجد ×2; 5:14 eşi; D4 1P 1 · 2MS 2 · 3MP 13, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T82 + "; aktör Yahudiler ve Nasârâ (ölçüm); A2 düşmanlıkça en şiddetlileri bulma; sevgice en yakınları bulma; keşiş ve rahiplerin bulunması; büyüklenmeme; A3 'innâ nasârâ' (söz içi, 17-18. kelime); "
 "A4 " + BOLUM + "; edim geçişi şart → haber (ayetler arası); şahıs geçişi yok; söz açılır (17. kelime); söz kapanır (18. kelime, ayet içi).",
)

D[83] = ("◇ 've izâ semi'û mâ unzile ile'r-resûli terâ a'yunehum tefîdu mine'd-dem'i mimmâ 'arafû mine'l-haqqi yeqûlûne rabbenâ âmennâ fe'ktubnâ ma'a'ş-şâhidîn' — "
 "'ve' + 'izâ' + PERF 3MP I. bab + 'mâ' + edilgen PERF 3MS IV. bab + 'ilâ' + belirli 'resûl' + IMPF 2MS I. bab + çoğul ''ayn' + 3MP + IMPF 3FS I. bab + 'min' + belirli 'dem'' + 'min' + 'mâ' + PERF 3MP I. bab + 'min' + belirli 'haqq' + IMPF 3MP I. bab + 'rabb' + 1P + PERF 1P IV. bab + 'fe' + IMPV 2MS I. bab + 1P + 'ma'a' + belirli çoğul etken ortaç 'şâhid' "
 "(ölçüm edim emir, kip IMPV 1; 1P 4 · 2MS 2 · 3FS 1 · 3MP 7 · 3MS 1; bab I. bab ×6 · IV. bab ×2; EDİLGEN 1/8 fiil). "
 "Lafız yok; Rab 17. sırada (ölçüm rab z=0,69); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=21 (n z=0,91); ölçüm '{{2|fâsıla ٱلشهدين → ن, N sınıfı}}' — satır aynen; ölçüm '{{2|EDİLGEN 1/8 fiil, pas z=0,38}}' — satır aynen ('unzile' 4. kelime); "
 "ölçüm '{{2|simetri \\[3, 1, 10, 1\\]}}' — satır aynen; ölçüm '{{2|harf 92 → harf3 89, isaret 3}}' — satır aynen; ölçüm '{{2|dış düğüm 3}}' — satır aynen. "
 "Ölçüm IMPV 1: 'ktubnâ' (19. kelime); 1. kelimedeki 've' CONJ, 'fe'ktubnâ' (19.)'daki 'fe' REM (okuma). "
 + T83 + " (okuma). "
 + cumle(say('say 5:83 1-6 --on', "ve izâ semi'û mâ unzile ile'r-resûl", True), say('say 5:83 2-6', "semi'û mâ unzile ile'r-resûl"), say('say 5:83 3-6', "mâ unzile ile'r-resûl"), say('say 5:83 4-6', "unzile ile'r-resûl")) + ' '
 + cumle(say('say 5:83 7-11', "terâ a'yunehum tefîdu mine'd-dem'", True), say('say 5:83 8-11', "a'yunehum tefîdu mine'd-dem'"), say('say 5:83 8-9', "a'yunehum tefîdu"), say('dizi 5 83 8 11', "'ayn tefîdu min dem'")) + ' '
 + cumle(say('say 5:83 12-15', "mimmâ 'arafû mine'l-haqq", True), say('say 5:83 13-15', "'arafû mine'l-haqq")) + ' '
 + cumle(say('say 5:83 16-18', "yeqûlûne rabbenâ âmennâ", True), say('say 5:83 17-18', "rabbenâ âmennâ"), say('dizi 5 83 16 18', "qâle rabb âmene")) + ' '
 + cumle(say('say 5:83 19-21 --on', "fe'ktubnâ ma'a'ş-şâhidîn", True), say('say 5:83 20-21', "ma'a'ş-şâhidîn")) + ' '
 "Ölçüm xref okunmuş 3 ayet. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 'semi'û' (2. kelime), 'a'yunehum' (8. kelime); B4 —.",
 "◈D — D1 've' + 'izâ' + PERF + 'mâ' + PERF + 'ilâ' + belirli + IMPF + çoğul + IMPF + 'min' + belirli + 'min' + 'mâ' + PERF + 'min' + belirli + IMPF + izafet + PERF + 'fe' + IMPV + 'ma'a' + belirli; "
 "D2 emir, IMPV ('ktubnâ' 19. kelime); D3 —; 3:53 eşi; D4 1P 4 · 2MS 2 · 3FS 1 · 3MP 7 · 3MS 1, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T83 + "; aktör yok (ölçüm); A2 indirileni işitme; gözlerin yaşla taşması; hakkı tanıma; iman beyanı; şahitlerle yazılma duası; A3 'rabbenâ âmennâ' ile açılan söz (17. kelimeden; 5:84 sonuna dek); "
 "A4 " + BOLUM + "; edim geçişi haber → emir (ayetler arası); şahıs geçişi yok; söz açılır (17. kelime).",
)

D[84] = ("◇ 've mâ lenâ lâ nu'minu bi'llâhi ve mâ câ'enâ mine'l-haqqi ve natma'u en yudxilenâ rabbunâ ma'a'l-qavmi's-sâlihîn' — "
 "'ve' + soru 'mâ' + 'li' + 1P + 'lâ' + IMPF 1P IV. bab + 'bi' + lafız + 've' + 'mâ' + PERF 3MS I. bab + 1P + 'min' + belirli 'haqq' + 've' + IMPF 1P I. bab + 'en' + IMPF 3MS IV. bab + 1P + 'rabb' + 1P + 'ma'a' + belirli 'qavm' + belirli etken ortaç 'sâlih' "
 "(ölçüm edim soru, kip INTG 1 · NEG 1; 1P 6 · 3MS 2; bab I. bab ×2 · IV. bab ×2). "
 "Allah lafzı 5. sırada (ölçüm allah z=0,72); Rab 13. sırada (ölçüm rab z=1,01); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=16 (n z=0,38); ölçüm '{{3|fâsıla ٱلصلحين → ن, N sınıfı}}' — satır aynen; "
 "ölçüm '{{3|simetri \\[3, 1, 6, 1\\]}}' — satır aynen; ölçüm '{{3|harf 62 → harf3 62, isaret 0}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm INTG 1: 'mâ' (1. kelime); NEG 1: 'lâ' (3. kelime); 1. kelimedeki 've' REM, 've mâ câ'enâ' (6.)'daki 've' CONJ, 've natma'u' (10.)'daki 've' CIRC (okuma). "
 + T84 + " (okuma). "
 + cumle(say('say 5:84 1-5 --on', "ve mâ lenâ lâ nu'minu bi'llâh", True), say('say 5:84 3-5', "lâ nu'minu bi'llâh"), say('say 5:84 4-5', "nu'minu bi'llâh"), say('say 5:84 4-6', "nu'minu bi'llâhi ve mâ"), say('dizi 5 84 4 6', "âmene allâh mâ")) + ' '
 + cumle(say('say 5:84 6-9 --on', "ve mâ câ'enâ mine'l-haqq", True), say('say 5:84 6-8 --on', "ve mâ câ'enâ min"), say('dizi 5 84 6 8', "mâ câ'e min"), say('say 5:84 7-9', "câ'enâ mine'l-haqq"), say('dizi 5 84 7 9', "câ'e min haqq")) + ' '
 + cumle(say('say 5:84 10-13 --on', "ve natma'u en yudxilenâ rabbunâ", True), say('say 5:84 11-13', "en yudxilenâ rabbunâ")) + ' '
 + cumle(say('say 5:84 14-16', "ma'a'l-qavmi's-sâlihîn", True), say('say 5:84 15-16', "l-qavmi's-sâlihîn")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıpları: 'mâ câ'e min', 'câ'e min haqq' ve 'âmene allâh mâ' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'mâ' + 'li' + 'lâ' + IMPF + 'bi' + lafız + 've' + 'mâ' + PERF + 'min' + belirli + 've' + IMPF + 'en' + IMPF + izafet + 'ma'a' + belirli + belirli; "
 "D2 soru, INTG ('mâ' 1. kelime), NEG ('lâ' 3. kelime); D3 —; D4 1P 6 · 3MS 2, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T84 + "; aktör yok (ölçüm); A2 iman etmemeye gerekçe sorma; salihlerle birlikte sokulmayı umma; A3 söz sürüyor (5:83 17. kelimeden; 1-16. kelime); "
 "A4 " + BOLUM + "; edim geçişi emir → soru (ayetler arası); şahıs geçişi 3 → 1 (ayetler arası); söz kapanır (16. kelime).",
)

D[85] = ("◇ 'fe-esâbehumu'llâhu bi-mâ qâlû cennâtin tecrî min tahtihe'l-enhâru xâlidîne fîhâ ve zâlike cezâ'u'l-muhsinîn' — "
 "'fe' + PERF 3MS IV. bab + 3MP + lafız + 'bi' + 'mâ' + PERF 3MP I. bab + çoğul nekre 'cenne' + IMPF 3FS I. bab + 'min' + 'taht' + 3FS + belirli çoğul 'neher' + çoğul etken ortaç 'xâlid' + 'fî' + 3FS + 've' + 'zâlike' + 'cezâ'' + belirli çoğul etken ortaç 'muhsin' "
 "(ölçüm edim haber, kip yok; 3FS 3 · 3MP 3 · 3MS 1; bab I. bab ×2 · IV. bab ×1). "
 "Allah lafzı 2. sırada (ölçüm allah z=0,90); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=14 (n z=0,17); ölçüm '{{4|fâsıla ٱلمحسنين → ن, N sınıfı}}' — satır aynen; "
 "ölçüm '{{4|harf 66 → harf3 63, isaret 3}}' — satır aynen; ölçüm '{{4|dış düğüm 1}}' — satır aynen. "
 "Ölçüm kip yok; 'fe-esâbehumu' (1.)'daki 'fe' CAUS, 've zâlike' (12.)'daki 've' REM (okuma). "
 + T85 + " (okuma). "
 + cumle(say('say 5:85 1-4 --on', "fe-esâbehumu'llâhu bi-mâ qâlû", True), say('say 5:85 1-2 --on', "fe-esâbehumu'llâh"), say('say 5:85 3-4', "bi-mâ qâlû")) + ' '
 + cumle(say('say 5:85 5-11', "cennâtin tecrî min tahtihe'l-enhâru xâlidîne fîhâ", True), say('dizi 5 85 5 11', "cenne cerey min taht neher xâlid fî"), say('say 5:85 5-9', "cennâtin tecrî min tahtihe'l-enhâr"), say('dizi 5 85 5 9', "cenne cerey min taht neher"), say('say 5:85 6-9', "tecrî min tahtihe'l-enhâr")) + ' '
 + cumle(say('say 5:85 12-14 --on', "ve zâlike cezâ'u'l-muhsinîn", True), say('say 5:85 13-14', "cezâ'u'l-muhsinîn")) + ' '
 "Ölçüm xref okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıpları: 'cenne cerey min taht neher xâlid fî' ve 'cenne cerey min taht neher' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: 5:85 / 5:86 ('cennâtin' / 'ashâbu'l-cahîm').",
 "◈K — K1 'l-enhâru' (9. kelime).",
 "◈B — —",
 "◈D — D1 'fe' + PERF + lafız + 'bi' + 'mâ' + PERF + nekre + IMPF + 'min' + izafet + belirli + ortaç + 'fî' + 've' + 'zâlike' + izafet + belirli; "
 "D2 haber; D3 —; D4 3FS 3 · 3MP 3 · 3MS 1, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T85 + "; aktör yok (ölçüm); A2 söz sebebiyle ödüllendirme; altından ırmaklar akan cennetler; içinde kalış; iyilik edenlerin karşılığı; A3 —; "
 "A4 " + BOLUM + "; edim geçişi soru → haber (ayetler arası); şahıs geçişi 1 → 3 (ayetler arası).",
)

D[86] = ("◇ 've'llezîne keferû ve kezzebû bi-âyâtinâ ulâ'ike ashâbu'l-cahîm' — "
 "'ve' + 'ellezî' + PERF 3MP I. bab + 've' + PERF 3MP II. bab + 'bi' + çoğul 'âye' + 1P + 'ulâ'ike' + çoğul 'ashâb' + belirli 'cahîm' "
 "(ölçüm edim haber, kip yok; 1P 1 · 3MP 4; bab I. bab ×1 · II. bab ×1). "
 "Lafız yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=7 (n z=-0,58); ölçüm '{{5|fâsıla ٱلجحيم → م, N sınıfı}}' — satır aynen; ölçüm '{{5|harf 42 → harf3 39, isaret 3}}' — satır aynen; ölçüm '{{5|dış düğüm 1}}' — satır aynen; "
 "ölçüm '{{5|nakarat 2 \\(temsil \\[5, 10\\]\\)}}' — satır aynen; ölçüm '{{5|esit2 → 5:10 oran 1,0000 kademe TAM}}' — satır aynen (5:10 emsal olarak basıldı). "
 "Ölçüm kip yok; 1. kelimedeki 've' REM, 've kezzebû' (3.)'daki 've' CONJ (okuma). "
 + T86 + " (okuma). "
 + cumle(say('say 5:86 1-7 --on', "ve'llezîne keferû ve kezzebû bi-âyâtinâ ulâ'ike ashâbu'l-cahîm", True), say('say 5:86 2-7', "keferû ve kezzebû bi-âyâtinâ ulâ'ike ashâbu'l-cahîm"), say('dizi 5 86 1 7', "ellezî kefera kezzebe âye _ ashâb cahîm")) + ' '
 + cumle(say('say 5:86 2-4', "keferû ve kezzebû bi-âyâtinâ", True), say('say 5:86 5-7', "ulâ'ike ashâbu'l-cahîm"), say('say 5:86 6-7', "ashâbu'l-cahîm")) + ' '
 "Ölçüm xref 5:10 (emsal olarak basıldı) ve okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıbı: 'ellezî kefera kezzebe âye _ ashâb cahîm' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: 5:85 / 5:86 ('cennâtin' / 'ashâbu'l-cahîm').",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'ellezî' + PERF + 've' + PERF + 'bi' + izafet + 'ulâ'ike' + izafet + belirli; "
 "D2 haber; D3 —; 5:10 eşi; D4 1P 1 · 3MP 4, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T86 + "; aktör yok (ölçüm); A2 inkâr; âyetleri yalanlama; alevli ateşin halkı olma; A3 —; "
 "A4 " + BOLUM + "; bölüm kapanışı; şahıs geçişi yok.",
)

out = ['# ── blok 5:82-86 (2026-11-16) ──', 'MEAL26 = {']
for n in range(82, 87):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M26 = {']
for n in range(82, 87):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL26); M.update(M26)']
open('/home/claude/yamalar/metin_5_82_86.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

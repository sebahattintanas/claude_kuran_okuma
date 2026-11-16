# blok 23 (5:71-74) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b25/say2.txt'
os.environ['OLC'] = '/home/claude/b25/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Lanetlenenler; Nasârâ'nın yakınlığı; gözyaşı dökenler' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 78: "İsrâiloğullarından inkâr edenler, Dâvûd'un ve Meryem oğlu Îsâ'nın diliyle lanetlendi. Bu, isyan etmeleri ve sınırı aşmaları yüzündendi.",
 79: "Yaptıkları bir kötülükten birbirlerini men etmiyorlardı. Yapmakta oldukları ne kötüdür!",
 80: "Onların çoğunun inkâr edenleri velî edindiğini görürsün. Nefislerinin onlar için önden gönderdiği şey ne kötüdür: Allah'ın onlara gazap etmesi! Onlar azapta kalacaklardır.",
 81: "Eğer Allah'a, Nebi'ye ve ona indirilene iman ediyor olsalardı, onları velîler edinmezlerdi; fakat onlardan çoğu fâsıktır.",
}

T78 = ("'lu'ine' 3MS (fiil uyumu; edilgen; 1. kelime — naib-i fail 2. kelime); 'llezîne keferû' ('lu'ine' naib-i faili; 2-3. kelime); 'keferû' faili 3MP (adsız; 3. kelime); 'benî isrâ'île' (adlı kavim; 5-6. kelime); "
       "Dâvûd (adlı kişi; 9. kelime); ''îsâ'bni meryeme' (adlı kişi; 10-12. kelime); ''asav' faili 3MP (adsız; 15. kelime); 'kânû' faili 3MP (adsız; 16. kelime); 'ya'tedûn' faili 3MP (adsız; 17. kelime)")
T79 = ("'kânû' faili 3MP (adsız; 1. ve 9. kelime); 'yetenâhevne' faili 3MP (adsız; 3. kelime); 'fe'alûhu' faili 3MP (adsız; 6. kelime); 'fe'alûhu' mef'ûlü 3MS (adsız; aid zamiri, gönderge 'munkerin', 6. kelime); "
       "'bi'se' 3MS (fiil uyumu; 7. kelime); 'yef'alûn' faili 3MP (adsız; 10. kelime)")
T80 = ("muhatap 2MS (adsız; 1. kelime — 'terâ'); 'kesîran minhum' ('yetevellevne' faili; 2-3. kelime); 'minhum' 3MP (adsız; 3. kelime); 'yetevellevne' faili 3MP (adsız; 4. kelime); 'llezîne keferû' ('yetevellevne' mef'ûlü; 5-6. kelime); "
       "'keferû' faili 3MP (adsız; 6. kelime); 'bi'se' 3MS (fiil uyumu; 7. kelime); 'qaddemet' 3FS (fiil uyumu; 9. kelime — fail 11. kelime); 'lehum' 3MP (adsız; 10. kelime); 'enfusuhum' ('qaddemet' faili; iyelik 3MP, adsız; 11. kelime); "
       "'saxita' 3MS (fiil uyumu; 13. kelime — fail 14. kelime); Allah (lafız; 14. kelime); ''aleyhim' 3MP (adsız; 15. kelime); 'hum' 3MP (adsız; 18. kelime)")
T81 = ("'kânû' faili 3MP (adsız; 2. kelime); 'yu'minûne' faili 3MP (adsız; 3. kelime); Allah (lafız; 4. kelime); 'n-nebiyyi' (5. kelime); 'unzile' 3MS (adsız; edilgen; 7. kelime — naib-i fail mevsûl 'mâ'); "
       "'ileyhi' 3MS (adsız; gönderge Nebi, 8. kelime); 'ttexazûhum' faili 3MP ve mef'ûlü 3MP (adsız; 10. kelime); 'evliyâ'e' ('ttexazû' mef'ûlü, velîler; çoğul insan — esmâ adı esmâ dışı göndergeyle; 11. kelime); "
       "'kesîran minhum' ('lâkinne' ismi; 13-14. kelime); 'minhum' 3MP (adsız; 14. kelime)")

D = {}
D[78] = ("◇ 'lu'ine'llezîne keferû min benî isrâ'île 'alâ lisâni dâwûde ve 'îsâ'bni meryeme zâlike bi-mâ 'asav ve kânû ya'tedûn' — "
 "edilgen PERF 3MS I. bab + 'ellezî' + PERF 3MP I. bab + 'min' + çoğul 'buneyy' (morph LEM ham biçim) + özel ad 'isrâ'îl' + ''alâ' + 'lisân' + özel ad 'dâwûd' + 've' + özel ad ''îsâ' + 'ibn' + özel ad 'meryem' + 'zâlike' + 'bi' + 'mâ' + PERF 3MP I. bab + 've' + PERF 3MP I. bab + IMPF 3MP VIII. bab "
 "(ölçüm edim haber, kip yok; 3MP 8 · 3MS 1; bab I. bab ×4 · VIII. bab ×1; EDİLGEN 1/5 fiil). "
 "Lafız yok; Rab yok; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); ölçüm aktör '{{1|adlı إِسْرائِيل 6\\. sırada \\(kavim, rol mecrur\\)}}', '{{1|adlı داوُد 9\\. sırada \\(kisi, rol mecrur\\)}}', '{{1|adlı عِيسَى 10\\. sırada \\(kisi, rol mecrur\\)}}' ve '{{1|adlı مَرْيَم 12\\. sırada \\(kisi, rol mecrur\\)}}' — satır aynen. "
 "Ölçüm 'yıldız yok' — satır aynen; n=17 (n z=0,49); ölçüm '{{1|fâsıla يعتدون → ن, N sınıfı}}' — satır aynen; ölçüm '{{1|EDİLGEN 1/5 fiil, pas z=0,81}}' — satır aynen ('lu'ine' 1. kelime); "
 "ölçüm '{{1|simetri \\[4, 4, 10, 1\\]}}' — satır aynen; ölçüm '{{1|harf 75 → harf3 69, isaret 6}}' — satır aynen; ölçüm '{{1|dış düğüm 2}}' — satır aynen. "
 "Ölçüm kip yok; 've 'îsâ'bni' (10.) ve 've kânû' (16.)'daki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) بني ×2 ('benî' 5. / 'bni' 11. kelime) (okuma). "
 + T78 + " (okuma). "
 + cumle(say('say 5:78 1-6', "lu'ine'llezîne keferû min benî isrâ'îl", True), say('say 5:78 1-3', "lu'ine'llezîne keferû"), say('say 5:78 2-4', "llezîne keferû min"), say('dizi 5 78 2 4', "ellezî kefera min"), say('say 5:78 2-6', "llezîne keferû min benî isrâ'îl"), say('say 5:78 4-6', "min benî isrâ'îl")) + ' '
 + cumle(say('say 5:78 7-9', "'alâ lisâni dâwûd", True), say('say 5:78 8-12 --on', "lisâni dâwûde ve 'îsâ'bni meryem"), say('say 5:78 10-12 --on', "ve 'îsâ'bni meryem"), say('dizi 5 78 10 12', "'îsâ ibn meryem")) + ' '
 + cumle(say('say 5:78 13-17 --on', "zâlike bi-mâ 'asav ve kânû ya'tedûn", True), say('say 5:78 14-17 --on', "bi-mâ 'asav ve kânû ya'tedûn"), say('say 5:78 15-17 --on', "'asav ve kânû ya'tedûn"), say('dizi 5 78 15 17', "'asâ kâne i'tedâ")) + ' '
 "Ölçüm xref 2:61 (emsal olarak basıldı) ve okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıpları: 'llezîne keferû min' ve ''îsâ'bni meryem' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 PERF + 'ellezî' + PERF + 'min' + izafet + özel ad + ''alâ' + izafet + özel ad + 've' + özel ad + izafet + özel ad + 'zâlike' + 'bi' + 'mâ' + PERF + 've' + PERF + IMPF; "
 "D2 haber; D3 بني ×2; 2:61 eşi; D4 3MP 8 · 3MS 1, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T78 + "; aktör İsrâiloğulları, Dâvûd, Îsâ ve Meryem (ölçüm); A2 lanetlenme; Dâvûd ve Îsâ'nın dili; isyan; sınırı aşma; A3 —; "
 "A4 " + BOLUM + "; bölüm açılışı; edim geçişi emir, yasak, nida → haber (ayetler arası); şahıs geçişi yok.",
)

D[79] = ("◇ 'kânû lâ yetenâhevne 'an munkerin fe'alûhu le-bi'se mâ kânû yef'alûn' — "
 "PERF 3MP I. bab + 'lâ' + IMPF 3MP VI. bab + ''an' + nekre edilgen ortaç 'munker' + PERF 3MP I. bab + 3MS + 'le' + PERF 3MS I. bab + 'mâ' + PERF 3MP I. bab + IMPF 3MP I. bab "
 "(ölçüm edim haber, kip EMPH 1 · NEG 1; 3MP 10 · 3MS 2; bab I. bab ×5 · VI. bab ×1). "
 "Lafız yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=10 (n z=-0,26); ölçüm '{{2|fâsıla يفعلون → ن, N sınıfı}}' — satır aynen; "
 "ölçüm '{{2|simetri \\[3, 4, 8, 1\\]}}' — satır aynen; ölçüm '{{2|harf 46 → harf3 42, isaret 4}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm NEG 1: 'lâ' (2. kelime); EMPH 1: 'le' (7. kelime) (okuma). "
 "Kök ikilemesi (ölçüm) فعل ×2 ('fe'alûhu' 6. / 'yef'alûn' 10. kelime), كون ×2 ('kânû' 1. / 9. kelime) (okuma). "
 + T79 + " (okuma). "
 + cumle(say('say 5:79 1-5', "kânû lâ yetenâhevne 'an munker", True), say('say 5:79 2-5', "lâ yetenâhevne 'an munker"), say('say 5:79 4-5', "'an munker"), say('lem 5:79:3', "yetenâhe")) + ' '
 + cumle(say('say 5:79 6-10 --on', "fe'alûhu le-bi'se mâ kânû yef'alûn", True), say('say 5:79 7-10 --on', "le-bi'se mâ kânû yef'alûn"), say('say 5:79 7-9 --on', "le-bi'se mâ kânû"), say('dizi 5 79 7 9', "bi'se mâ kâne"), say('dizi 5 79 7 10', "bi'se mâ kâne fe'ale"), say('say 5:79 8-10', "mâ kânû yef'alûn")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: 'le-bi'se mâ kânû' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 PERF + 'lâ' + IMPF + ''an' + nekre + PERF + 'le' + PERF + 'mâ' + PERF + IMPF; "
 "D2 haber, NEG ('lâ' 2. kelime), EMPH ('le' 7. kelime); D3 فعل ×2, كون ×2; 5:62 eşi; D4 3MP 10 · 3MS 2, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T79 + "; aktör yok (ölçüm); A2 kötülükten birbirini men etmeme; yaptıklarının kötülüğü; A3 —; "
 "A4 " + BOLUM + "; —.",
)

D[80] = ("◇ 'terâ kesîran minhum yetevellevne'llezîne keferû le-bi'se mâ qaddemet lehum enfusuhum en saxita'llâhu 'aleyhim ve fi'l-'azâbi hum xâlidûn' — "
 "IMPF 2MS I. bab + nekre 'kesîr' + 'min' + 3MP + IMPF 3MP V. bab + 'ellezî' + PERF 3MP I. bab + 'le' + PERF 3MS I. bab + 'mâ' + PERF 3FS II. bab + 'li' + 3MP + çoğul 'nefs' + 3MP + 'en' + PERF 3MS I. bab + lafız + ''alâ' + 3MP + 've' + 'fî' + belirli ''azâb' + 'hum' + çoğul etken ortaç 'xâlid' "
 "(ölçüm edim haber, kip EMPH 1; 2MS 1 · 3FS 1 · 3MP 9 · 3MS 2; bab I. bab ×4 · II. bab ×1 · V. bab ×1). "
 "Allah lafzı 14. sırada (ölçüm allah z=0,52); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=19 (n z=0,70); ölçüm '{{3|fâsıla خلدون → ن, N sınıfı}}' — satır aynen; ölçüm '{{3|sayı işareti \\S+}}' — satır aynen ('kesîran' 2. kelime); "
 "ölçüm '{{3|simetri \\[3, 3, 8, 1\\]}}' — satır aynen; ölçüm '{{3|harf 80 → harf3 77, isaret 3}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm EMPH 1: 'le' (7. kelime); 've fi'l-'azâbi' (16.)'daki 've' REM (okuma). "
 + T80 + " (okuma). "
 + cumle(say('say 5:80 1-3', "terâ kesîran minhum", True), say('say 5:80 1-3 --on', "terâ kesîran minhum"), say('dizi 5 80 1 3', "ra'â kesîr min"), say('say 5:80 2-3', "kesîran minhum")) + ' '
 + cumle(say('say 5:80 4-6', "yetevellevne'llezîne keferû", True), say('say 5:80 5-6', "llezîne keferû")) + ' '
 + cumle(say('say 5:80 7-11 --on', "le-bi'se mâ qaddemet lehum enfusuhum", True), say('say 5:80 8-11', "mâ qaddemet lehum enfusuhum"), say('say 5:80 9-11', "qaddemet lehum enfusuhum")) + ' '
 + cumle(say('say 5:80 12-15', "en saxita'llâhu 'aleyhim", True), say('say 5:80 13-15', "saxita'llâhu 'aleyhim"), say('say 5:80 16-19 --on', "ve fi'l-'azâbi hum xâlidûn"), say('say 5:80 17-19', "l-'azâbi hum xâlidûn"), say('dizi 5 80 17 19', "'azâb _ xâlid")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: 'terâ kesîran minhum' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPF + nekre + 'min' + IMPF + 'ellezî' + PERF + 'le' + PERF + 'mâ' + PERF + 'li' + izafet + 'en' + PERF + lafız + ''alâ' + 've' + 'fî' + belirli + ortaç; "
 "D2 haber, EMPH ('le' 7. kelime); D3 —; 5:62 eşi; D4 2MS 1 · 3FS 1 · 3MP 9 · 3MS 2, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T80 + "; aktör yok (ölçüm); A2 inkâr edenleri velî edinme; önden gönderilenin kötülüğü; Allah'ın gazabı; azapta kalış; A3 —; "
 "A4 " + BOLUM + "; —.",
)

D[81] = ("◇ 've lev kânû yu'minûne bi'llâhi ve'n-nebiyyi ve mâ unzile ileyhi me'ttexazûhum evliyâ'e ve lâkinne kesîran minhum fâsiqûn' — "
 "'ve' + 'lev' + PERF 3MP I. bab + IMPF 3MP IV. bab + 'bi' + lafız + 've' + belirli 'nebiyy' + 've' + 'mâ' + edilgen PERF 3MS IV. bab + 'ilâ' + 3MS + 'mâ' + PERF 3MP VIII. bab + 3MP + çoğul 'veliyy' + 've' + 'lâkinne' + nekre 'kesîr' + 'min' + 3MP + çoğul etken ortaç 'fâsiq' "
 "(ölçüm edim şart, kip COND 1 · NEG 1; 3MP 8 · 3MS 2; bab I. bab ×1 · IV. bab ×2 · VIII. bab ×1; EDİLGEN 1/4 fiil). "
 "Allah lafzı 4. sırada (ölçüm allah z=0,81); Rab yok; ölçüm '{{4|esmâ وَلِيّ 11\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET ton cemâl' (uyuşmuyor) — esma_el kaydı 'degil' — 'evliyâ'e', kural 'çoğul insan göndergeli → degil' (velîler) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=15 (n z=0,27); ölçüm '{{4|fâsıla فسقون → ن, N sınıfı}}' — satır aynen; ölçüm '{{4|EDİLGEN 1/4 fiil, pas z=1,10}}' — satır aynen ('unzile' 7. kelime); ölçüm '{{4|sayı işareti \\S+}}' — satır aynen ('kesîran' 13. kelime); "
 "ölçüm '{{4|simetri \\[3, 6, 12, 1\\]}}' — satır aynen; ölçüm '{{4|harf 71 → harf3 69, isaret 2}}' — satır aynen; ölçüm '{{4|dış düğüm 0}}' — satır aynen. "
 "Ölçüm COND 1: 'lev' (1. kelime); NEG 1: 'mâ' (9. kelime); 1. kelimedeki 've' ve 've lâkinne' (12.)'daki 've' REM, 've'n-nebiyyi' (5.) ve 've mâ' (6.)'daki 've' CONJ (okuma). "
 + T81 + " (okuma). "
 + cumle(say('say 5:81 1-4 --on', "ve lev kânû yu'minûne bi'llâh", True), say('say 5:81 2-4', "kânû yu'minûne bi'llâh"), say('say 5:81 3-4', "yu'minûne bi'llâh")) + ' '
 + cumle(say('say 5:81 3-8 --on', "yu'minûne bi'llâhi ve'n-nebiyyi ve mâ unzile ileyh", True), say('say 5:81 6-8 --on', "ve mâ unzile ileyh"), say('say 5:81 7-8', "unzile ileyh")) + ' '
 + cumle(say('say 5:81 9-11', "me'ttexazûhum evliyâ'", True), say('say 5:81 10-11', "ttexazûhum evliyâ'")) + ' '
 + cumle(say('say 5:81 12-15 --on', "ve lâkinne kesîran minhum fâsiqûn", True), say('say 5:81 13-15', "kesîran minhum fâsiqûn"), say('say 5:81 13-14', "kesîran minhum"), say('dizi 5 81 13 15', "kesîr min fâsiq")) + ' '
 "Ölçüm '{{4|bağ: YOK \\(esit2, nakarat3, xref üçü de boş\\)}}' — satır aynen. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'kânû yu'minûne bi'llâhi' / 'fâsiqûn' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'lev' + PERF + IMPF + 'bi' + lafız + 've' + belirli + 've' + 'mâ' + PERF + 'ilâ' + 'mâ' + PERF + çoğul + 've' + 'lâkinne' + nekre + 'min' + ortaç; "
 "D2 şart, COND ('lev' 1. kelime), NEG ('mâ' 9. kelime); D3 —; D4 3MP 8 · 3MS 2, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T81 + "; aktör yok (ölçüm); A2 iman şartı; velî edinmeme; çoğunun fâsıklığı; A3 —; "
 "A4 " + BOLUM + "; edim geçişi haber → şart (ayetler arası); şahıs geçişi yok; şart → cevap (ayet içi; COND 'lev' 1. kelime: 've lev kânû yu'minûne bi'llâhi' / 'ttexazûhum evliyâ'e' (10. kelime)).",
)

out = ['# ── blok 5:78-81 (2026-11-16) ──', 'MEAL25 = {']
for n in range(78, 82):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M25 = {']
for n in range(78, 82):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL25); M.update(M25)']
open('/home/claude/yamalar/metin_5_78_81.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

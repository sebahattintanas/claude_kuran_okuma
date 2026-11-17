# blok 33 (5:109-110) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b33/say2.txt'
os.environ['OLC'] = '/home/claude/b33/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Elçilerin toplanması; İsâ'ya verilen nimetler; havariler ve sofra' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 109: "Allah'ın elçileri toplayacağı gün der: Size ne cevap verildi? Derler: Bizim hiçbir bilgimiz yok; şüphesiz sen gaybları en iyi bilensin.",
 110: "Hani Allah demişti: Ey Meryem oğlu Îsâ! Sana ve annene olan nimetimi an. Hani seni kutsal ruhla desteklemiştim; beşikte ve olgunluk çağında insanlarla konuşuyordun. Hani sana Kitabı, hikmeti, Tevrat'ı ve İncil'i öğretmiştim. Hani benim iznimle çamurdan kuş biçiminde bir şey yaratıyordun, ona üflüyordun da benim iznimle kuş oluyordu; benim iznimle doğuştan körü ve alacalıyı iyileştiriyordun. Hani benim iznimle ölüleri çıkarıyordun. Hani onlara açık kanıtlarla geldiğinde İsrâiloğullarını senden alıkoymuştum; onlardan inkâr edenler de demişlerdi: Bu ancak apaçık bir büyüdür.",
}

T109 = ("'yecme'u' 3MS (fiil uyumu; 2. kelime — fail 3. kelime); 'llâhu' ('yecme'u' faili; lafız; 3. kelime); 'r-rusule' ('yecme'u' mef'ûlü; çoğul; 4. kelime); 'fe-yeqûlu' faili 3MS (adsız; gönderge lafız, 5. kelime); "
        "muhatap 2MP (adsız; söz içi; 'ucibtum' — 7. kelime; edilgen, naib-i faili); 'qâlû' faili 3MP (adsız; gönderge 'r-rusule', 8. kelime); konuşan 1P (adsız; söz içi; 'lenâ' — 11. kelime); "
        "muhatap 2MS (adsız; söz içi; 'inneke', 'ente' — 12. ve 13. kelime)")
T110 = ("'qâle' 3MS (fiil uyumu; 2. kelime — fail 3. kelime); 'llâhu' ('qâle' faili; lafız; 3. kelime); 'yâ 'îse' (münadâ; adlı; söz içi; 4. kelime); "
        "muhatap 2MS (adsız; söz içi; 'zkur', ''aleyke', 'vâlidetike', 'eyyedtuke', 'tukellimu', ''allemtuke', 'taxluqu', 'fe-tenfuxu', 'tubri'u', 'tuxricu', ''anke', 'ci'tehum' — 7., 9., 11., 13., 16., 22., 28., 34., 39., 44., 51. ve 53. kelime); "
        "konuşan 1S (adsız; söz içi; 'ni'metî', 'eyyedtuke', ''allemtuke', 'bi-iznî', 'kefeftu' — 8., 13., 22., 33., 38., 42., 46. ve 48. kelime); "
        "'fîhâ' 3FS (adsız; söz içi; gönderge 'hey'eti', 35. kelime); 'fe-tekûnu' 3FS (adsız; söz içi; gönderge 'hey'eti', 36. kelime); 'ci'tehum' 3MP (adsız; söz içi; gönderge 'benî isrâ'île', 53. kelime); "
        "'fe-qâle' 3MS (fiil uyumu; söz içi; 55. kelime — fail 56. kelime); 'llezîne' ('qâle' faili; ilgi zamiri; söz içi; 56. kelime); 'keferû' faili 3MP (adsız; söz içi; 57. kelime); 'minhum' 3MP (adsız; söz içi; 58. kelime)")

D = {}
D[109] = ("◇ 'yevme yecme'u'llâhu'r-rusule fe-yeqûlu mâzâ ucibtum qâlû lâ 'ilme lenâ inneke ente 'allâmu'l-ğuyûb' — "
 "'yevm' + IMPF 3MS I. bab + lafız + belirli çoğul 'rasûl' + 'fe' + IMPF 3MS I. bab + 'mâzâ' + edilgen PERF 2MP IV. bab + PERF 3MP I. bab + 'lâ' + ''ilm' + 'li' + 1P + 'inne' + 2MS + 'ente' + ''allâm' + belirli çoğul 'ğuyûb' "
 "(ölçüm edim soru, kip INTG 1 · NEG 1; 1P 1 · 2MP 2 · 2MS 2 · 3MP 2 · 3MS 2; bab I. bab ×3 · IV. bab ×1; EDİLGEN 1/4 fiil). "
 "Allah lafzı 3. sırada (ölçüm allah z=0,81); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=15 (n z=0,27); ölçüm '{{1|fâsıla ٱلغيوب → ب, ب sınıfı — KAFİYE KIRILMASI}}' — satır aynen (kafiye kırılması: 5:108 ن → 5:109 ب); "
 "ölçüm '{{1|EDİLGEN 1/4 fiil, pas z=1,10}}' — satır aynen ('ucibtum' 7. kelime); ölçüm '{{1|simetri \\[3, 5, 8, 1\\]}}' — satır aynen; ölçüm '{{1|harf 62 → harf3 58, isaret 4}}' — satır aynen; "
 "ölçüm '{{1|dış düğüm 3}}' — satır aynen; ölçüm '{{1|İÇ düğüm 1}}' — satır aynen. "
 "Ölçüm INTG 1: 'mâzâ' (6. kelime); NEG 1: 'lâ' (9. kelime); 'fe-yeqûlu' (5.)'daki 'fe' CONJ, 'yevme' (1.) T (okuma). "
 "Kök ikilemesi (ölçüm) علم ×2 (''ilme' 10. / ''allâmu' 14. kelime), قول ×2 ('fe-yeqûlu' 5. / 'qâlû' 8. kelime) (okuma). "
 + T109 + " (okuma). "
 + cumle(say('say 5:109 1-4', "yevme yecme'u'llâhu'r-rusul", True), say('say 5:109 2-4', "yecme'u'llâhu'r-rusul")) + ' '
 + cumle(say('say 5:109 5-7 --on', "fe-yeqûlu mâzâ ucibtum", True), say('say 5:109 6-7', "mâzâ ucibtum")) + ' '
 + cumle(say('say 5:109 8-11', "qâlû lâ 'ilme lenâ", True), say('say 5:109 9-11', "lâ 'ilme lenâ")) + ' '
 + cumle(say('say 5:109 12-15', "inneke ente 'allâmu'l-ğuyûb", True), say('dizi 5 109 12 15', "inne _ 'allâm ğuyûb"), say('say 5:109 14-15', "'allâmu'l-ğuyûb")) + ' '
 "Ölçüm xref 4:171, 5:104 (emsal olarak basıldı) ve okunmuş 2 ayet. "
 "Ölçüm nakarat3 kalıbı: 'inne _ 'allâm ğuyûb' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K2 'yevme' (1. kelime).",
 "◈B — —",
 "◈D — D1 'yevm' + IMPF + lafız + belirli + 'fe' + IMPF + 'mâzâ' + PERF + PERF + 'lâ' + 'li' + 'inne' + 'ente' + izafet + belirli; "
 "D2 soru, INTG ('mâzâ' 6. kelime), NEG ('lâ' 9. kelime); D3 علم ×2, قول ×2; D4 1P 1 · 2MP 2 · 2MS 2 · 3MP 2 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T109 + "; aktör yok (ölçüm); A2 Allah'ın elçileri toplayacağı gün; size ne cevap verildi; bilgimiz yok, gaybları en iyi bilen sensin; "
 "A3 'mâzâ ucibtum' (söz içi, 6-7. kelime); 'lâ 'ilme lenâ inneke ente 'allâmu'l-ğuyûb' (söz içi, 9-15. kelime); "
 "A4 " + BOLUM + "; bölüm açılışı; söz açılır (6. kelime); söz kapanır (7. kelime, ayet içi); söz açılır (9. kelime); söz kapanır (15. kelime, ayet içi); edim geçişi emir → soru (ayetler arası).",
)

D[110] = ("◇ 'iz qâle'llâhu yâ 'îse'bne meryeme'zkur ni'metî 'aleyke ve 'alâ vâlidetike iz eyyedtuke bi-rûhi'l-qudusi tukellimu'n-nâse fi'l-mehdi ve kehlen ve iz 'allemtuke'l-kitâbe ve'l-hikmete ve't-tevrâte ve'l-incîle "
 "ve iz taxluqu mine't-tîni ke-hey'eti't-tayri bi-iznî fe-tenfuxu fîhâ fe-tekûnu tayran bi-iznî ve tubri'u'l-ekmehe ve'l-ebrasa bi-iznî ve iz tuxricu'l-mevtâ bi-iznî "
 "ve iz kefeftu benî isrâ'île 'anke iz ci'tehum bi'l-beyyinâti fe-qâle'llezîne keferû minhum in hâzâ illâ sihrun mubîn' — "
 "'iz' + PERF 3MS I. bab + lafız + 'yâ' + adlı ''îsâ' + 'ibn' + adlı 'meryem' + IMPV 2MS I. bab + 'ni'me' + 1S + ''alâ' + 2MS + 've' + ''alâ' + etken ortaç 'vâlide' + 2MS + "
 "'iz' + PERF 1S II. bab + 2MS + 'bi' + 'rûh' + belirli 'qudus' + IMPF 2MS II. bab + belirli 'nâs' + 'fî' + belirli 'mehd' + 've' + nekre 'kehl' + "
 "'ve' + 'iz' + PERF 1S II. bab + 2MS + belirli 'kitâb' + 've' + belirli 'hikme' + 've' + adlı 'tevrâ' + 've' + adlı 'incîl' + "
 "'ve' + 'iz' + IMPF 2MS I. bab + 'min' + belirli 'tîn' + 'ke' + 'hey'e' + belirli 'tayr' + 'bi' + 'izn' + 1S + 'fe' + IMPF 2MS I. bab + 'fî' + 3FS + 'fe' + IMPF 3FS I. bab + nekre 'tayr' + 'bi' + 'izn' + 1S + "
 "'ve' + IMPF 2MS IV. bab + belirli 'ekmeh' + 've' + belirli 'ebras' + 'bi' + 'izn' + 1S + 've' + 'iz' + IMPF 2MS IV. bab + belirli çoğul 'meyyit' + 'bi' + 'izn' + 1S + "
 "'ve' + 'iz' + PERF 1S I. bab + çoğul 'benî' + adlı 'isrâ'îl' + ''an' + 2MS + 'iz' + PERF 2MS I. bab + 3MP + 'bi' + belirli çoğul 'beyyine' + "
 "'fe' + PERF 3MS I. bab + 'ellezî' + PERF 3MP I. bab + 'min' + 3MP + 'in' + 'hâ' + 'zâ' + 'illâ' + nekre 'sihr' + nekre etken ortaç 'mubîn' "
 "(ölçüm edim emir, nida, kip IMPV 1 · NEG 1 · RES 1 · VOC 1; 1S 11 · 2MS 13 · 3FS 2 · 3MP 4 · 3MS 2; bab I. bab ×9 · II. bab ×3 · IV. bab ×2). "
 "Allah lafzı 3. sırada (ölçüm allah z=-0,21); Rab yok; ölçüm '{{2|esmâ مُبِين 63\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür hayır' (uyuşuyor) — esma_el kaydı 'degil' — 'sihrun mubîn', kural 'esmâ adı esmâ dışı göndergeyle → degil' (büyünün sıfatı) (okuma). "
 "Ölçüm aktör '{{2|adlı عِيسَى 4\\. sırada \\(kisi, rol meful\\+muhatap\\)}}', '{{2|adlı مَرْيَم 6\\. sırada \\(kisi, rol mecrur\\)}}', '{{2|adlı تَوْراة 25\\. sırada \\(kitab, rol meful\\)}}', "
 "'{{2|adlı إِنجِيل 26\\. sırada \\(kitab, rol meful\\)}}' ve '{{2|adlı إِسْرائِيل 50\\. sırada \\(kavim, rol mecrur\\)}}' — satır aynen. "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=63 (n z=5,37); ölçüm '{{2|fâsıla مبين → ن, N sınıfı}}' — satır aynen; "
 "ölçüm '{{2|simetri \\[6, 47, 56, 2\\]}}' — satır aynen; ölçüm '{{2|harf 285 → harf3 275, isaret 10}}' — satır aynen; ölçüm '{{2|dış düğüm 10}}' — satır aynen. "
 "Ölçüm VOC 1: 'yâ' (4. kelime); IMPV 1: 'zkur' (7. kelime); NEG 1: 'in' (59. kelime); RES 1: 'illâ' (61. kelime); 'iz' (1., 12., 21., 27., 43., 47. ve 52.) T, 'fe-tenfuxu' (34.) ve 'fe-tekûnu' (36.)'daki 'fe' CONJ, 'fe-qâle' (55.)'daki 'fe' REM (okuma). "
 "Kök ikilemesi (ölçüm) أذن ×4 ('bi-iznî' 33., 38., 42. ve 46. kelime), بني ×2 (''îse'bne' 5. / 'benî' 49. kelime), بين ×2 ('bi'l-beyyinâti' 54. / 'mubîn' 63. kelime), طير ×2 ('t-tayri' 32. / 'tayran' 37. kelime), "
 "قول ×2 ('qâle' 2. / 'fe-qâle' 55. kelime) (okuma). "
 + T110 + " (okuma). "
 + cumle(say('say 5:110 1-6', "iz qâle'llâhu yâ 'îse'bne meryem", True), say('dizi 5 110 1 6', "iz qâle allâh 'îsâ ibn meryem"), say('say 5:110 4-6', "yâ 'îse'bne meryem"), say('dizi 5 110 4 6', "'îsâ ibn meryem")) + ' '
 + cumle(say('say 5:110 7-11', "zkur ni'metî 'aleyke ve 'alâ vâlidetik", True), say('say 5:110 7-8', "zkur ni'metî")) + ' '
 + cumle(say('say 5:110 12-15', "iz eyyedtuke bi-rûhi'l-qudus", True), say('say 5:110 13-15', "eyyedtuke bi-rûhi'l-qudus"), say('say 5:110 14-15', "bi-rûhi'l-qudus")) + ' '
 + cumle(say('say 5:110 16-20', "tukellimu'n-nâse fi'l-mehdi ve kehlen", True), say('say 5:110 16-19', "tukellimu'n-nâse fi'l-mehd"), say('say 5:110 17-20', "n-nâse fi'l-mehdi ve kehlen")) + ' '
 + cumle(say('say 5:110 21-26 --on', "ve iz 'allemtuke'l-kitâbe ve'l-hikmete ve't-tevrâte ve'l-incîl", True), say('say 5:110 23-26', "l-kitâbe ve'l-hikmete ve't-tevrâte ve'l-incîl"), say('say 5:110 25-26 --on', "ve't-tevrâte ve'l-incîl")) + ' '
 + cumle(say('say 5:110 27-33 --on', "ve iz taxluqu mine't-tîni ke-hey'eti't-tayri bi-iznî", True), say('say 5:110 28-32', "taxluqu mine't-tîni ke-hey'eti't-tayr"), say('say 5:110 30-32', "t-tîni ke-hey'eti't-tayr"), say('say 5:110 31-32', "ke-hey'eti't-tayr")) + ' '
 + cumle(say('say 5:110 34-38 --on', "fe-tenfuxu fîhâ fe-tekûnu tayran bi-iznî", True), say('say 5:110 36-38 --on', "fe-tekûnu tayran bi-iznî")) + ' '
 + cumle(say('say 5:110 39-42 --on', "ve tubri'u'l-ekmehe ve'l-ebrasa bi-iznî", True), say('say 5:110 39-41 --on', "ve tubri'u'l-ekmehe ve'l-ebras"), say('say 5:110 40-41', "l-ekmehe ve'l-ebras")) + ' '
 + cumle(say('say 5:110 43-46 --on', "ve iz tuxricu'l-mevtâ bi-iznî", True), say('say 5:110 44-45', "tuxricu'l-mevtâ")) + ' '
 + cumle(say('say 5:110 47-51 --on', "ve iz kefeftu benî isrâ'île 'anke", True), say('say 5:110 49-50', "benî isrâ'îl")) + ' '
 + cumle(say('say 5:110 52-54', "iz ci'tehum bi'l-beyyinât", True), say('say 5:110 53-54', "ci'tehum bi'l-beyyinât")) + ' '
 + cumle(say('say 5:110 55-58 --on', "fe-qâle'llezîne keferû minhum", True), say('say 5:110 56-58', "llezîne keferû minhum"), say('dizi 5 110 56 58', "ellezî kefera min")) + ' '
 + cumle(say('say 5:110 59-63', "in hâzâ illâ sihrun mubîn", True), say('say 5:110 57-63', "keferû minhum in hâzâ illâ sihrun mubîn"), say('say 5:110 62-63', "sihrun mubîn")) + ' '
 "Ölçüm xref 2:87, 3:46, 3:49 (emsal olarak basıldı), okunmuş 6 ayet ve henüz okunmamış 1 ayet. "
 "Ölçüm nakarat3 kalıpları: 'iz qâle allâh 'îsâ ibn meryem' ve ''îsâ ibn meryem' süzgeç GEÇER, 'ellezî kefera min' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'fi'l-mehdi' / 'kehlen' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 'n-nâse' (17. kelime), 't-tayri' (32. kelime), 'tayran' (37. kelime); B2 'taxluqu' (28. kelime); B4 'l-mevtâ' (45. kelime).",
 "◈D — D1 'iz' + PERF + lafız + 'yâ' + adlı + izafet + adlı + IMPV + izafet + ''alâ' + 've' + ''alâ' + izafet + 'iz' + PERF + 'bi' + izafet + belirli + IMPF + belirli + 'fî' + belirli + 've' + nekre + "
 "'ve' + 'iz' + PERF + belirli + 've' + belirli + 've' + adlı + 've' + adlı + 've' + 'iz' + IMPF + 'min' + belirli + 'ke' + izafet + belirli + 'bi' + izafet + 'fe' + IMPF + 'fî' + 'fe' + IMPF + nekre + 'bi' + izafet + "
 "'ve' + IMPF + belirli + 've' + belirli + 'bi' + izafet + 've' + 'iz' + IMPF + belirli + 'bi' + izafet + 've' + 'iz' + PERF + izafet + adlı + ''an' + 'iz' + PERF + 'bi' + belirli + 'fe' + PERF + 'ellezî' + PERF + 'min' + 'in' + 'zâ' + 'illâ' + nekre + nekre; "
 "D2 emir, nida, VOC ('yâ' 4. kelime), IMPV ('zkur' 7. kelime), NEG ('in' 59. kelime), RES ('illâ' 61. kelime); D3 أذن ×4, بني ×2, بين ×2, طير ×2, قول ×2; 2:87, 3:46 ve 3:49 eşi; D4 1S 11 · 2MS 13 · 3FS 2 · 3MP 4 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T110 + "; aktör 'yâ 'îse', 'meryeme', 't-tevrâte', 'l-incîle', 'isrâ'île' (ölçüm); A2 Îsâ'ya ve annesine nimet; kutsal ruhla destek; insanlarla konuşma; Kitap, hikmet, Tevrat ve İncil; "
 "izinle kuş biçimi, üfleme, doğuştan körü ve alacalıyı iyileştirme, ölüleri çıkarma; İsrâiloğullarını alıkoyma; inkâr edenlerin büyü sözü; "
 "A3 'yâ 'îse'bne meryeme'zkur ni'metî 'aleyke ve 'alâ vâlidetike iz eyyedtuke bi-rûhi'l-qudusi tukellimu'n-nâse fi'l-mehdi ve kehlen ve iz 'allemtuke'l-kitâbe ve'l-hikmete ve't-tevrâte ve'l-incîle ve iz taxluqu mine't-tîni ke-hey'eti't-tayri bi-iznî fe-tenfuxu fîhâ fe-tekûnu tayran bi-iznî ve tubri'u'l-ekmehe ve'l-ebrasa bi-iznî ve iz tuxricu'l-mevtâ bi-iznî ve iz kefeftu benî isrâ'île 'anke iz ci'tehum bi'l-beyyinâti fe-qâle'llezîne keferû minhum in hâzâ illâ sihrun mubîn' (söz içi, 4-63. kelime); "
 "A4 " + BOLUM + "; söz açılır (4. kelime); söz kapanır (63. kelime, ayet içi); edim geçişi soru → emir, nida (ayetler arası).",
)

out = ['# ── blok 5:109-110 (2026-11-17) ──', 'MEAL33 = {']
for n in range(109, 111):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M33 = {']
for n in range(109, 111):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL33); M.update(M33)']
open('/home/claude/yamalar/metin_5_109_110.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

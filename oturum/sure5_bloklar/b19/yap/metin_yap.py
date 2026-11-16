# blok 19 (5:55-58) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b19/say2.txt'
os.environ['OLC'] = '/home/claude/b19/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Velî edinme; Allah'ın sevdiği kavim; dinle alay edenler' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 55: "Sizin velîniz ancak Allah, O'nun elçisi ve iman edenlerdir; onlar ki namazı kılarlar, zekâtı verirler ve onlar rükû hâlindedir.",
 56: "Kim Allah'ı, O'nun elçisini ve iman edenleri velî edinirse, şüphesiz Allah'ın hizbi, galip gelenlerin ta kendileridir.",
 57: "Ey iman edenler! Sizden önce kendilerine Kitap verilenlerden dininizi alay ve oyun edinenleri ve kâfirleri velîler edinmeyin. İnananlarsanız Allah'tan sakının.",
 58: "Namaza çağırdığınızda onu alay ve oyun edinirler. Bu, onların akletmeyen bir kavim olmalarındandır.",
}

T55 = ("'veliyyukumu' 2MP (adsız; 2. kelime); Allah (lafız; 3. kelime); 'rasûluhû' 3MS (adsız; gönderge lafız, 4. kelime); 'âmenu' faili 3MP (adsız; 6. kelime); 'yuqîmûne' faili 3MP (adsız; 8. kelime); 'yu'tûne' faili 3MP (adsız; 10. kelime); 've hum' 3MP (adsız; 12. kelime)")
T56 = ("'men' (şart ismi; 1. kelime); 'yetevelle' faili 3MS (adsız; 2. kelime); Allah (lafız; 3. ve 9. kelime); 'rasûlehû' 3MS (adsız; gönderge lafız, 4. kelime); 'âmenû' faili 3MP (adsız; 6. kelime); 'humu' 3MP (adsız; 10. kelime)")
T57 = ("'âmenû' faili 3MP (adsız; nida edilenler, 3. kelime); muhatap 2MP (adsız; 'tettexizu' 5., 'dînekum' 8., 'qablikum' 16., 've'ttequ' 19., 'kuntum' 22. kelime); 'ttexazû' faili 3MP (adsız; 7. kelime); 'huzuven ve le'iben' (nekre; 9-10. kelime); "
       "'ûtu' naib-i faili 3MP (adsız; 13. kelime); Allah (lafız; 20. kelime)")
T58 = ("muhatap 2MP (adsız; 'nâdeytum' 2. kelime); 'ttexazûhâ' faili 3MP (adsız; 5. kelime); 'ttexazûhâ' mef'ûlü 3FS (adsız; gönderge 's-salâti', 5. kelime); 'huzuven ve le'iben' (nekre; 6-7. kelime); 'bi-ennehum' 3MP (adsız; 9. kelime); 'qavmun' (nekre; 10. kelime); 'ya'qilûn' faili 3MP (adsız; 12. kelime)")

D = {}
D[55] = ("◇ 'innemâ veliyyukumu'llâhu ve rasûluhû ve'llezîne âmenu'llezîne yuqîmûne's-salâte ve yu'tûne'z-zekâte ve hum râki'ûn' — "
 "'inne' + 'mâ' + 'veliyy' + 2MP + lafız + 've' + 'rasûl' + 3MS + 've' + 'ellezî' + PERF 3MP IV. bab + 'ellezî' + IMPF 3MP IV. bab + belirli 'salâ' + 've' + IMPF 3MP IV. bab + belirli 'zekâ' + 've' + 3MP + çoğul ortaç 'râki'' "
 "(ölçüm edim haber, kip yok; 2MP 1 · 3MP 7 · 3MS 1; bab IV. bab ×3). "
 "Allah lafzı 3. sırada (ölçüm allah z=1,01); Rab yok; ölçüm '{{1|esmâ \\S+ 2\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor) — 'innemâ veliyyukumu'llâh', kural 'sınırlama haberi lafız → ilahi' (elçi ve inananlar atıflı); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=13 (n z=0,06); ölçüm '{{1|fâsıla ركعون → ن, N sınıfı}}' — satır aynen; ölçüm '{{1|harf 70 → harf3 68, isaret 2}}' — satır aynen; ölçüm '{{1|dış düğüm 2}}' — satır aynen. "
 "Ölçüm PREV 'mâ' (1. kelime); 've rasûluhû' (4.), 've'llezîne' (5.) ve 've yu'tûne' (10.)'daki 've' CONJ, 've hum' (12.)'deki 've' CIRC (okuma). "
 + T55 + " (okuma). "
 + cumle(say('say 5:55 1-3', "innemâ veliyyukumu'llâh", True), say('say 5:55 1-2', "innemâ veliyyukum"), say('say 5:55 2-3', "veliyyukumu'llâh"), say('say 5:55 3-6', "llâhu ve rasûluhû ve'llezîne âmenu"), say('dizi 5 55 3 6', "allâh rasûl ellezî âmene"), say('say 5:55 4-6 --on', "ve rasûluhû ve'llezîne âmenu")) + ' '
 + cumle(say('say 5:55 5-7 --on', "ve'llezîne âmenu'llezîne", True), say('say 5:55 7-9', "llezîne yuqîmûne's-salâ"), say('say 5:55 8-9', "yuqîmûne's-salâ"), say('say 5:55 8-11', "yuqîmûne's-salâte ve yu'tûne'z-zekâ"), say('dizi 5 55 8 11', "qâme salât etâ zekât"), say('say 5:55 10-11 --on', "ve yu'tûne'z-zekâ")) + ' '
 + cumle(say('say 5:55 12-13 --on', "ve hum râki'ûn", True), say('lem 5:55:13', "râki'")) + ' '
 "Ölçüm xref 5:56 (bu blokta) ve okunmuş başka ayetler. "
 "Ölçüm nakarat3 kalıpları: 'yuqîmûne's-salâte ve yu'tûne'z-zekâ' ve 'llâhu ve rasûluhû ve'llezîne âmenu' süzgeç GEÇER; 've'llezîne âmenu'llezîne' GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'inne' + 'mâ' + izafet + lafız + 've' + izafet + 've' + 'ellezî' + PERF + 'ellezî' + IMPF + belirli + 've' + IMPF + belirli + 've' + çoğul; "
 "D2 haber, kip yok; D3 ikileme yok; 31:4 eşi; D4 2MP 1 · 3MP 7 · 3MS 1, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T55 + "; aktör yok (ölçüm); A2 velîlik; Allah, elçi ve iman edenler; namaz; zekât; rükû; A3 —; "
 "A4 " + BOLUM + "; edim geçişi nida, şart → haber (ayetler arası); şahıs geçişi yok.",
)

D[56] = ("◇ 've men yetevelle'llâhe ve rasûlehû ve'llezîne âmenû fe-inne hizbe'llâhi humu'l-ğâlibûn' — "
 "'ve' + 'men' + IMPF 3MS V. bab + lafız + 've' + 'rasûl' + 3MS + 've' + 'ellezî' + PERF 3MP IV. bab + 'fe' + 'inne' + 'hizb' + lafız + 3MP + belirli çoğul ortaç 'ğâlib' "
 "(ölçüm edim şart, kip COND 1; 3MP 3 · 3MS 2; bab IV. bab ×1 · V. bab ×1). "
 "Allah lafzı 3. ve 9. sırada (ölçüm allah z=3,11); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=11 (n z=-0,15); ölçüm '{{2|fâsıla ٱلغلبون → ن, N sınıfı}}' — satır aynen; ölçüm '{{2|simetri \\[3, 1, 7, 1\\]}}' — satır aynen; ölçüm '{{2|harf 50 → harf3 48, isaret 2}}' — satır aynen; ölçüm '{{2|dış düğüm 1}}' — satır aynen. "
 "Ölçüm COND 1: 'men' (1. kelime); 've men' (1.)'deki 've' REM, 've rasûlehû' (4.) ve 've'llezîne' (5.)'daki 've' CONJ; 'fe-inne' (7.)'deki 'fe' RSLT (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 (lafız 3., 9. kelime) (okuma). "
 + T56 + " (okuma). "
 + cumle(say('say 5:56 1-3 --on', "ve men yetevelle'llâh", True), say('say 5:56 2-3', "yetevelle'llâh"), say('say 5:56 3-6', "llâhe ve rasûlehû ve'llezîne âmenû"), say('dizi 5 56 3 6', "allâh rasûl ellezî âmene")) + ' '
 + cumle(say('say 5:56 7-11 --on', "fe-inne hizbe'llâhi humu'l-ğâlibûn", True), say('say 5:56 8-9', "hizbe'llâh"), say('say 5:56 10-11', "humu'l-ğâlibûn"), say('lem 5:56:8', "hizb"), say('lem 5:56:11', "ğâlib")) + ' '
 "Ölçüm xref 5:55 (bu blokta) ve okunmuş başka ayet. "
 "Ölçüm nakarat3 kalıpları: 'llâhe ve rasûlehû ve'llezîne âmenû' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'men' + IMPF + lafız + 've' + izafet + 've' + 'ellezî' + PERF + 'fe' + 'inne' + izafet + lafız + belirli; "
 "D2 şart, COND ('men' 1. kelime); D3 أله ×2; 58:22 eşi; D4 3MP 3 · 3MS 2, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T56 + "; aktör yok (ölçüm); A2 velî edinme; Allah'ın hizbi; galip gelenler; A3 —; "
 "A4 " + BOLUM + "; edim geçişi haber → şart (ayetler arası); şahıs geçişi yok; şart → cevap (ayet içi; COND 'men' 1. kelime: 've men yetevelle'llâh' / 'fe-inne hizbe'llâhi humu'l-ğâlibûn' (7. kelime)).",
)

D[57] = ("◇ 'yâ eyyuhe'llezîne âmenû lâ tettexizu'llezîne'ttexazû dînekum huzuven ve le'iben mine'llezîne ûtu'l-kitâbe min qablikum ve'l-kuffâra evliyâ'e ve'ttequ'llâhe in kuntum mu'minîn' — "
 "'yâ' + 'eyy' + 'hâ' + 'ellezî' + PERF 3MP IV. bab + 'lâ' + IMPF 2MP VIII. bab + 'ellezî' + PERF 3MP VIII. bab + 'dîn' + 2MP + nekre 'huzuv' + 've' + nekre 'le'ib' + 'min' + 'ellezî' + edilgen PERF 3MP IV. bab + belirli 'kitâb' + 'min' + 'qabl' + 2MP + 've' + belirli çoğul 'kâfir' + çoğul 'veliyy' + 've' + IMPV 2MP VIII. bab + lafız + 'in' + PERF 2MP I. bab + çoğul ortaç 'mu'min' "
 "(ölçüm edim emir, yasak, nida, şart, kip COND 1 · IMPV 1 · PRO 1 · VOC 1, biçim DIKKAT + NEHY; 2MP 8 · 3MP 6; bab I. bab ×1 · IV. bab ×2 · VIII. bab ×3; EDİLGEN 1/6 fiil). "
 "Allah lafzı 20. sırada (ölçüm allah z=0,34); Rab yok; ölçüm '{{3|esmâ \\S+ 18\\. sırada, ORTA konum, MÜHÜRSÜZ}}', '{{3|\\S+ 23\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET (ÇİFT)', ton cemâl — ölçüm MÜHÜRSÜZ ile uyuşmuyor (tam okuma sonu); "
 "esma_el: 'evliyâ'e' (18. kelime) kural 'çoğul insan göndergeli → degil' (alay edenler ve kâfirler); 'mu'minîn' (23. kelime) kural 'çoğul insan göndergeli → degil' (inananlar) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=23 (n z=1,12); ölçüm '{{3|fâsıla مؤمنين → ن, N sınıfı}}' — satır aynen; ölçüm '{{3|harf 116 → harf3 108, isaret 8}}' — satır aynen; ölçüm '{{3|dış düğüm 3}}' — satır aynen; ölçüm '{{3|EDİLGEN 1/6 fiil, pas z=0,62}}' — satır aynen ('ûtu' 13. kelime). "
 "Ölçüm VOC 1: 'yâ' (1. kelime); PRO 1: 'lâ' (4. kelime); IMPV 1: 've'ttequ' (19. kelime); COND 1: 'in' (21. kelime); 've le'iben' (10.) ve 've'l-kuffâra' (17.)'daki 've' CONJ, 've'ttequ' (19.)'daki 've' REM (okuma). "
 "Kök ikilemesi (ölçüm) أخذ ×2 ('tettexizu' 5. / 'ttexazû' 7. kelime), أمن ×2 ('âmenû' 3. / 'mu'minîn' 23. kelime) (okuma). "
 + T57 + " (okuma). "
 + cumle(say('say 5:57 1-3', "yâ eyyuhe'llezîne âmenû", True), say('say 5:57 1-4', "yâ eyyuhe'llezîne âmenû lâ"), say('dizi 5 57 1 4', "eyy ellezî âmene lâ"), say('say 5:57 1-5', "yâ eyyuhe'llezîne âmenû lâ tettexizu"), say('dizi 5 57 1 5', "eyy ellezî âmene lâ ittexaze")) + ' '
 + cumle(say('say 5:57 6-10', "llezîne'ttexazû dînekum huzuven ve le'iben", True), say('say 5:57 7-8', "ttexazû dînekum"), say('say 5:57 8-10', "dînekum huzuven ve le'iben"), say('say 5:57 9-10', "huzuven ve le'iben"), say('lem 5:57:9', "huzuv"), say('lem 5:57:10', "le'ib")) + ' '
 + cumle(say('say 5:57 11-16', "mine'llezîne ûtu'l-kitâbe min qablikum", True), say('dizi 5 57 11 16', "min ellezî etâ kitâb min qabl"), say('say 5:57 12-14', "llezîne ûtu'l-kitâb"), say('say 5:57 13-14', "ûtu'l-kitâb"), say('say 5:57 15-16', "min qablikum"), say('say 5:57 17-18 --on', "ve'l-kuffâra evliyâ'")) + ' '
 + cumle(say('say 5:57 19-23 --on', "ve'ttequ'llâhe in kuntum mu'minîn", True), say('dizi 5 57 19 23', "itteqâ allâh in kâne mu'min"), say('say 5:57 19-20 --on', "ve'ttequ'llâh"), say('say 5:57 19-21 --on', "ve'ttequ'llâhe in"), say('dizi 5 57 19 21', "itteqâ allâh in"),
         say('say 5:57 21-23', "in kuntum mu'minîn"), say('dizi 5 57 21 23', "in kâne mu'min"), say('say 5:57 22-23', "kuntum mu'minîn")) + ' '
 "Ölçüm xref okunmuş ve henüz okunmamış ayetler. "
 "Ölçüm nakarat3 kalıpları: 'mine'llezîne ûtu'l-kitâbe min qablikum', 'yâ eyyuhe'llezîne âmenû lâ tettexizu', 'ttequ'llâhe in kuntum mu'minîn', 'yâ eyyuhe'llezîne âmenû lâ', 'yâ eyyuhe'llezîne âmenû', 'ttequ'llâhe in' ve 'in kuntum mu'minîn' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'yâ' + 'eyy' + 'hâ' + 'ellezî' + PERF + 'lâ' + IMPF + 'ellezî' + PERF + izafet + nekre + 've' + nekre + 'min' + 'ellezî' + PERF + belirli + 'min' + izafet + 've' + belirli + çoğul + 've' + IMPV + lafız + 'in' + PERF + çoğul; "
 "D2 emir, yasak, nida, şart, VOC ('yâ' 1. kelime), PRO ('lâ' 4. kelime), IMPV ('ttequ' 19. kelime), COND ('in' 21. kelime); D3 أخذ ×2, أمن ×2; D4 2MP 8 · 3MP 6, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T57 + "; aktör yok (ölçüm); A2 velî edinme yasağı; dini alay ve oyun edinenler; Kitap verilenler; kâfirler; takvâ; iman şartı; A3 —; "
 "A4 " + BOLUM + "; edim geçişi şart → emir, yasak, nida, şart (ayetler arası); şahıs geçişi 3 → 2 (ayetler arası); şart → cevap (ayet içi; COND 'in' 21. kelime: 'in kuntum mu'minîn' / 've'ttequ'llâh' (19. kelime) — cevap öne alınmış).",
)

D[58] = ("◇ 've izâ nâdeytum ile's-salâti'ttexazûhâ huzuven ve le'iben zâlike bi-ennehum qavmun lâ ya'qilûn' — "
 "'ve' + 'izâ' + PERF 2MP III. bab + 'ilâ' + belirli 'salâ' + PERF 3MP VIII. bab + 3FS + nekre 'huzuv' + 've' + nekre 'le'ib' + 'zâ' + 'li' + 'ke' + 'bi' + 'enne' + 3MP + nekre 'qavm' + 'lâ' + IMPF 3MP I. bab "
 "(ölçüm edim haber, kip NEG 1; 2MP 2 · 3FS 1 · 3MP 5; bab I. bab ×1 · III. bab ×1 · VIII. bab ×1). "
 "Lafız yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=12 (n z=-0,04); ölçüm '{{4|fâsıla يعقلون → ن, N sınıfı}}' — satır aynen; ölçüm '{{4|simetri \\[3, 1, 9, 1\\]}}' — satır aynen; ölçüm '{{4|harf 58 → harf3 54, isaret 4}}' — satır aynen; ölçüm '{{4|dış düğüm 0}}' — satır aynen. "
 "Ölçüm NEG 1: 'lâ' (11. kelime); T 'izâ' (1. kelime); 've izâ' (1.)'daki 've' REM, 've le'iben' (7.)'deki 've' CONJ (okuma). "
 + T58 + " (okuma). "
 + cumle(say('say 5:58 1-4 --on', "ve izâ nâdeytum ile's-salâ", True), say('say 5:58 2-4', "nâdeytum ile's-salâ")) + ' '
 + cumle(say('say 5:58 5-7', "ttexazûhâ huzuven ve le'iben", True), say('say 5:58 6-7', "huzuven ve le'iben")) + ' '
 + cumle(say('say 5:58 8-10', "zâlike bi-ennehum qavm", True), say('say 5:58 9-10 --on', "bi-ennehum qavm"), say('say 5:58 10-12', "qavmun lâ ya'qilûn"), say('say 5:58 11-12', "lâ ya'qilûn"), say('lem 5:58:12', "'aqalu")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'izâ' + PERF + 'ilâ' + belirli + PERF + nekre + 've' + nekre + 'zâ' + 'bi' + 'enne' + nekre + 'lâ' + IMPF; "
 "D2 haber, NEG ('lâ' 11. kelime); D3 ikileme yok; 59:14 eşi; D4 2MP 2 · 3FS 1 · 3MP 5, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T58 + "; aktör yok (ölçüm); A2 namaza çağrı; alay ve oyun; akletmeyen kavim; A3 —; "
 "A4 " + BOLUM + "; edim geçişi emir, yasak, nida, şart → haber (ayetler arası); şahıs geçişi 2 → 3 (ayetler arası).",
)

out = ['# ── blok 5:55-58 (2026-11-16) ──', 'MEAL19 = {']
for n in range(55, 59):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M19 = {']
for n in range(55, 59):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL19); M.update(M19)']
open('/home/claude/yamalar/metin_5_55_58.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

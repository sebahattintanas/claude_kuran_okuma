# sûre 6 blok 1 (6:1-5) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b01/say2.txt'
os.environ['OLC'] = '/home/claude/b01/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Gökleri ve yeri yaratan; yüz çeviren kavimler' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 1: "Hamd, gökleri ve yeri yaratan, karanlıkları ve nuru var eden Allah'adır. Sonra inkâr edenler Rablerine denk tutuyorlar.",
 2: "O, sizi çamurdan yaratan, sonra bir ecel takdir edendir; adı konmuş bir ecel de O'nun katındadır. Sonra siz şüphe ediyorsunuz.",
 3: "O, göklerde de yerde de Allah'tır; gizlinizi ve açığınızı bilir, kazandığınız şeyi bilir.",
 4: "Rablerinin âyetlerinden kendilerine hiçbir âyet gelmez ki ondan yüz çeviriyor olmasınlar.",
 5: "Nitekim hak kendilerine geldiğinde onu yalanladılar; yakında alay ettikleri şeyin haberleri onlara gelecek.",
}

T = {}
T[1] = ("'xalaqa' 3MS (adsız; gönderge lafız, 4. kelime); 've ce'ale' 3MS (adsız; gönderge lafız, 7. kelime); "
        "'keferû', 'bi-rabbihim', 'ya'dilûn' 3MP (adsız; gönderge 'llezîne' — 12., 13. ve 14. kelime)")
T[2] = ("'huve' 3MS (adsız; gönderge 6:1 2. kelime, 1. kelime); 'xalaqakum', 'qadâ' 3MS (adsız; gönderge 'huve' — 3. ve 7. kelime); "
        "''indehû' 3MS (adsız; gönderge 'huve', 11. kelime); muhatap 2MP (adsız; 'xalaqakum', 'entum', 'temterûn' — 3., 13. ve 14. kelime)")
T[3] = ("'huve' 3MS (adsız; gönderge 6:1 2. kelime, 1. kelime); 'llâhu' (haber; lafız; 2. kelime); "
        "'ya'lemu', 've ya'lemu' 3MS (adsız; gönderge 'huve' — 7. ve 10. kelime); "
        "muhatap 2MP (adsız; 'sirrakum', 've cehrakum', 'teksibûn' — 8., 9. ve 12. kelime)")
T[4] = ("'te'tîhim', ''anhâ' 3FS (adsız; gönderge 'âyetin' — 2. ve 10. kelime); "
        "'te'tîhim', 'rabbihim', 'kânû' 3MP (adsız; gönderge 6:1 11. kelime — 2., 7. ve 9. kelime)")
T[5] = ("'kezzebû', 'câ'ahum' 3MP (adsız; gönderge 6:1 11. kelime — 2. ve 5. kelime); 'câ'ahum' 3MS (adsız; gönderge 'l-haqqi', 5. kelime); "
        "'ye'tîhim' 3MS (fiil uyumu; 7. kelime — fail 8. kelime); 'enbâ'u' ('ye'tîhim' faili; 8. kelime); 'ye'tîhim' 3MP (adsız; gönderge 6:1 11. kelime, 7. kelime); "
        "'kânû', 'yestehzi'ûn' 3MP (adsız; gönderge 6:1 11. kelime — 10. ve 12. kelime); 'bihî' 3MS (adsız; gönderge 'mâ', 11. kelime)")

D = {}
D[1] = ("◇ 'el-hamdu li'llâhi'llezî xalaqa's-semâvâti ve'l-arda ve ce'ale'z-zulumâti ve'n-nûra summe'llezîne keferû bi-rabbihim ya'dilûn' — "
 "belirli 'hamd' + 'li' + lafız + 'ellezî' + PERF 3MS I. bab + belirli çoğul 'semâ'' + 've' + belirli 'ard' + 've' + PERF 3MS I. bab + belirli çoğul 'zulme' + 've' + belirli 'nûr' + "
 "'summe' + 'ellezî' + PERF 3MP I. bab + 'bi' + 'rabb' + 3MP + IMPF 3MP I. bab "
 "(ölçüm edim haber, kip yok; 3MP 5 · 3MS 2; bab I. bab ×4). "
 "Allah lafzı 2. sırada (ölçüm allah z=0,90); Rab 13. sırada (ölçüm rab z=1,20); ölçüm '{{1|esmâ نُور 9\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET ton denge' — ölçüm MÜHÜRSÜZ ile uyuşmuyor (araç tanımı farkı; muhur_el hayır — ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 've ce'ale'z-zulumâti ve'n-nûr', kural 'esmâ adı esmâ dışı göndergeyle → degil' (yaratılan ışık) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=14 (n z=0,17); ölçüm '{{1|fâsıla يعدلون → ن, N sınıfı}}' — satır aynen (sûre açılışı); "
 "ölçüm '{{1|harf 87 → harf3 65, isaret 0}}' — satır aynen; ölçüm '{{1|dış düğüm 2}}' — satır aynen. "
 "Ölçüm kip yok; 've'l-arda' (6.), 've ce'ale' (7.) ve 've'n-nûra' (9.) kelimelerindeki 've' CONJ; 'summe' (10.) CONJ (okuma). "
 + T[1] + " (okuma). "
 + cumle(say('say 6:1 1-2', "el-hamdu li'llâh", True), say('say 6:1 3-6', "llezî xalaqa's-semâvâti ve'l-ard"), say('dizi 6 1 3 6', "ellezî xalaqa semâ' ard"),
         say('say 6:1 4-6', "xalaqa's-semâvâti ve'l-ard")) + ' '
 + cumle(say('say 6:1 7-9 --on', "ve ce'ale'z-zulumâti ve'n-nûr", True), say('say 6:1 11-14', "llezîne keferû bi-rabbihim ya'dilûn"), say('say 6:1 13-14 --on', "bi-rabbihim ya'dilûn")) + ' '
 "Ölçüm xref okunmuş 2 ayet. "
 "Ölçüm nakarat3 kalıbı: 'ellezî xalaqa semâ' ard' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'z-zulumâti' / 'n-nûra' — ayetler arası: yok.",
 "◈K — K1 's-semâvâti' (5. kelime), 'l-arda' (6. kelime).",
 "◈B — B2 'xalaqa' (4. kelime).",
 "◈D — D1 belirli + 'li' + lafız + 'ellezî' + PERF + belirli + 've' + belirli + 've' + PERF + belirli + 've' + belirli + 'summe' + 'ellezî' + PERF + 'bi' + izafet + IMPF; "
 "D2 haber; D3 —; D4 3MP 5 · 3MS 2, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[1] + "; aktör yok (ölçüm); A2 hamd; gökleri ve yeri yaratma; karanlıkları ve nuru var etme; inkâr edenlerin Rablerine denk tutması; "
 "A3 —; "
 "A4 " + BOLUM + "; bölüm açılışı.",
)

D[2] = ("◇ 'huve'llezî xalaqakum min tînin summe qadâ ecelen ve ecelun musemmen 'indehû summe entum temterûn' — "
 "'huve' + 'ellezî' + PERF 3MS I. bab + 2MP + 'min' + nekre 'tîn' + 'summe' + PERF 3MS I. bab + nekre 'ecel' + 've' + nekre 'ecel' + nekre edilgen ortaç 'musemmâ' + ''ind' + 3MS + "
 "'summe' + 'entum' + IMPF 2MP VIII. bab "
 "(ölçüm edim haber, kip yok; 2MP 4 · 3MS 4; bab I. bab ×2 · VIII. bab ×1). "
 "Lafız yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=14 (n z=0,17); ölçüm '{{2|fâsıla تمترون → ن, N sınıfı}}' — satır aynen (6:1 ن → 6:2 ن); "
 "ölçüm '{{2|simetri \\[3, 1, 12, 1\\]}}' — satır aynen; ölçüm '{{2|harf 55 → harf3 49, isaret 6}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm kip yok; 'summe' (6. ve 12.) CONJ; 've ecelun' (9.) kelimesindeki 've' REM (okuma). "
 "Kök ikilemesi (ölçüm) أجل ×2 ('ecelen' 8. / 've ecelun' 9. kelime) (okuma). "
 + T[2] + " (okuma). "
 + cumle(say('say 6:2 1-3', "huve'llezî xalaqakum", True), say('dizi 6 2 1 3', "_ ellezî xalaqa"), say('say 6:2 3-5', "xalaqakum min tîn")) + ' '
 + cumle(say('say 6:2 6-8 --on', "summe qadâ ecelen", True), say('say 6:2 9-11 --on', "ve ecelun musemmen 'indeh"), say('say 6:2 12-14 --on', "summe entum temterûn")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: '_ ellezî xalaqa' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K2 'ecelen' (8. kelime), 'ecelun' (9. kelime).",
 "◈B — B2 'xalaqakum' (3. kelime).",
 "◈D — D1 'huve' + 'ellezî' + PERF + 'min' + nekre + 'summe' + PERF + nekre + 've' + nekre + nekre + izafet + 'summe' + 'entum' + IMPF; "
 "D2 haber; D3 أجل ×2; D4 2MP 4 · 3MS 4, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[2] + "; aktör yok (ölçüm); A2 çamurdan yaratma; ecel takdiri; O'nun katındaki adı konmuş ecel; şüphe; "
 "A3 —; "
 "A4 " + BOLUM + ".",
)

D[3] = ("◇ 've huve'llâhu fi's-semâvâti ve fi'l-ardi ya'lemu sirrakum ve cehrakum ve ya'lemu mâ teksibûn' — "
 "'ve' + 'huve' + lafız + 'fî' + belirli çoğul 'semâ'' + 've' + 'fî' + belirli 'ard' + IMPF 3MS I. bab + 'sirr' + 2MP + 've' + 'cehr' + 2MP + 've' + IMPF 3MS I. bab + 'mâ' + IMPF 2MP I. bab "
 "(ölçüm edim haber, kip yok; 2MP 4 · 3MS 3; bab I. bab ×3). "
 "Allah lafzı 2. sırada (ölçüm allah z=1,14); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=12 (n z=-0,04); ölçüm '{{3|fâsıla تكسبون → ن, N sınıfı}}' — satır aynen (6:2 ن → 6:3 ن); "
 "ölçüm '{{3|harf 51 → harf3 50, isaret 1}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm kip yok; 've huve' (1.), 've fi'l-ardi' (5.), 've cehrakum' (9.) ve 've ya'lemu' (10.) kelimelerindeki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) علم ×2 ('ya'lemu' 7. / 've ya'lemu' 10. kelime) (okuma). "
 + T[3] + " (okuma). "
 + cumle(say('say 6:3 1-2 --on', "ve huve'llâh", True), say('say 6:3 3-6', "fi's-semâvâti ve fi'l-ard")) + ' '
 + cumle(say('say 6:3 7-9', "ya'lemu sirrakum ve cehrakum", True), say('say 6:3 10-12 --on', "ve ya'lemu mâ teksibûn")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'sirrakum' / 'cehrakum' — ayetler arası: yok.",
 "◈K — K1 's-semâvâti' (4. kelime), 'l-ardi' (6. kelime).",
 "◈B — —",
 "◈D — D1 've' + 'huve' + lafız + 'fî' + belirli + 've' + 'fî' + belirli + IMPF + izafet + 've' + izafet + 've' + IMPF + 'mâ' + IMPF; "
 "D2 haber; D3 علم ×2; D4 2MP 4 · 3MS 3, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[3] + "; aktör yok (ölçüm); A2 göklerde ve yerde Allah; gizliyi ve açığı bilme; kazanılanı bilme; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 3 → 2 (ayetler arası).",
)

D[4] = ("◇ 've mâ te'tîhim min âyetin min âyâti rabbihim illâ kânû 'anhâ mu'ridîn' — "
 "'ve' + 'mâ' + IMPF 3FS I. bab + 3MP + 'min' + nekre 'âye' + 'min' + çoğul 'âye' + 'rabb' + 3MP + 'illâ' + PERF 3MP I. bab + ''an' + 3FS + çoğul etken ortaç 'mu'rid' "
 "(ölçüm edim haber, kip NEG 1 · RES 1; 3FS 2 · 3MP 4; bab I. bab ×2). "
 "Lafız yok; Rab 7. sırada (ölçüm rab z=1,62); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=11 (n z=-0,15); ölçüm '{{4|fâsıla معرضين → ن, N sınıfı}}' — satır aynen (6:3 ن → 6:4 ن); "
 "ölçüm '{{4|simetri \\[3, 1, 8, 1\\]}}' — satır aynen; ölçüm '{{4|harf 45 → harf3 43, isaret 2}}' — satır aynen; ölçüm '{{4|dış düğüm 1}}' — satır aynen; ölçüm '{{4|İÇ düğüm 1}}' — satır aynen; "
 "ölçüm '{{4|esit2 → 36:46 oran 0,9882 kademe YAKIN}}' — satır aynen (36:46 emsal olarak basıldı). "
 "Ölçüm NEG 1: 'mâ' (1. kelime); RES 1: 'illâ' (8. kelime); 've mâ' (1.) kelimesindeki 've' REM (okuma). "
 "Kök ikilemesi (ölçüm) أيي ×2 ('âyetin' 4. / 'âyâti' 6. kelime) (okuma). "
 + T[4] + " (okuma). "
 + cumle(say('say 6:4 1-7 --on', "ve mâ te'tîhim min âyetin min âyâti rabbihim", True), say('say 6:4 4-7', "âyetin min âyâti rabbihim")) + ' '
 + cumle(say('say 6:4 8-11', "illâ kânû 'anhâ mu'ridîn", True)) + ' '
 "Ölçüm xref 36:46 (emsal olarak basıldı) ve okunmamış 1 ayet (sûre içi 1). "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'mâ' + IMPF + 'min' + nekre + 'min' + izafet + izafet + 'illâ' + PERF + ''an' + ortaç; "
 "D2 haber, NEG ('mâ' 1. kelime), RES ('illâ' 8. kelime); D3 أيي ×2; 36:46 eşi; D4 3FS 2 · 3MP 4, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[4] + "; aktör yok (ölçüm); A2 Rablerinin âyetlerinden gelen her âyetten yüz çevirme; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 2 → 3 (ayetler arası).",
)

D[5] = ("◇ 'fe-qad kezzebû bi'l-haqqi lemmâ câ'ahum fe-sevfe ye'tîhim enbâ'u mâ kânû bihî yestehzi'ûn' — "
 "'fe' + 'qad' + PERF 3MP II. bab + 'bi' + belirli 'haqq' + 'lemmâ' + PERF 3MS I. bab + 3MP + 'fe' + 'sevfe' + IMPF 3MS I. bab + 3MP + çoğul 'nebe'' + 'mâ' + PERF 3MP I. bab + 'bi' + 3MS + IMPF 3MP X. bab "
 "(ölçüm edim haber, kip CERT 1 · FUT 1; 3MP 8 · 3MS 3; bab I. bab ×3 · II. bab ×1 · X. bab ×1). "
 "Lafız yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=12 (n z=-0,04); ölçüm '{{5|fâsıla يستهزءون → ن, N sınıfı}}' — satır aynen (6:4 ن → 6:5 ن); "
 "ölçüm '{{5|simetri \\[3, 4, 9, 1\\]}}' — satır aynen; ölçüm '{{5|harf 59 → harf3 53, isaret 6}}' — satır aynen; ölçüm '{{5|dış düğüm 3}}' — satır aynen. "
 "Ölçüm CERT 1: 'fe-qad' (1. kelime); FUT 1: 'fe-sevfe' (6. kelime); 'fe-qad' (1.) ve 'fe-sevfe' (6.) kelimelerindeki 'fe' RSLT; 'lemmâ' (4.) T (okuma). "
 + T[5] + " (okuma). "
 + cumle(say('say 6:5 1-5 --on', "fe-qad kezzebû bi'l-haqqi lemmâ câ'ahum", True), say('say 6:5 2-3', "kezzebû bi'l-haqq")) + ' '
 + cumle(say('say 6:5 6-12 --on', "fe-sevfe ye'tîhim enbâ'u mâ kânû bihî yestehzi'ûn", True), say('say 6:5 9-12', "mâ kânû bihî yestehzi'ûn"), say('dizi 6 5 9 12', "mâ kâne _ istuhzi'e")) + ' '
 "Ölçüm xref 50:5 (emsal olarak basıldı), 26:6 (emsal olarak basıldı) ve okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıbı: 'mâ kâne _ istuhzi'e' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'fe' + 'qad' + PERF + 'bi' + belirli + 'lemmâ' + PERF + 'fe' + 'sevfe' + IMPF + izafet + 'mâ' + PERF + 'bi' + IMPF; "
 "D2 haber, CERT ('fe-qad' 1. kelime), FUT ('fe-sevfe' 6. kelime); D3 —; 50:5 ve 26:6 eşi; D4 3MP 8 · 3MS 3, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[5] + "; aktör yok (ölçüm); A2 hakkı yalanlama; alay ettikleri şeyin haberlerinin gelmesi; "
 "A3 —; "
 "A4 " + BOLUM + ".",
)

out = ['# ── blok 6:1-5 (2026-11-18) ──', 'MEAL1 = {']
for n in range(1, 6):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M1 = {']
for n in range(1, 6):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL1); M.update(M1)']
open('/home/claude/yamalar/metin_6_1_5.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

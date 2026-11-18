# blok 35 (5:116-117) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b35/say2.txt'
os.environ['OLC'] = '/home/claude/b35/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'İsâ'ya soru; doğruların fayda gördüğü gün' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 116: "Hani Allah demişti: Ey Meryem oğlu Îsâ! Sen mi insanlara dedin: Allah'ı bırakıp beni ve annemi iki ilah edinin? Demişti: Seni tenzih ederim; benim için, hakkım olmayan şeyi söylemek olmaz. Eğer onu demişsem, sen onu bilmişsindir; benim nefsimde olanı bilirsin, senin nefsinde olanı bilmem. Şüphesiz sen gaybları en iyi bilensin.",
 117: "Onlara, bana emrettiğin şeyden başkasını söylemedim: Rabbim ve Rabbiniz olan Allah'a kulluk edin. Aralarında olduğum sürece onlara şahittim; beni vefat ettirince onları gözeten sen oldun. Sen her şeye şahitsin.",
}

T = {}
T[116] = ("'qâle' 3MS (fiil uyumu; 2. kelime — fail 3. kelime); 'llâhu' ('qâle' faili; lafız; 3. kelime); 'yâ 'îse' (münadâ; adlı; söz içi; 4. kelime); "
          "muhatap 2MS (adsız; söz içi; 'e-ente', 'qulte', 'subhâneke', ''alimtehû', 'ta'lemu', 'nefsike', 'inneke', 'ente' — 7., 8., 17., 31., 32., 40., 41. ve 42. kelime); "
          "muhatap 2MP (adsız; söz içi; 'ttexizûnî' — 10. kelime); "
          "konuşan 1S (adsız; söz içi; 'ttexizûnî', 've ummiye', 'lî', 'eqûle', 'kuntu', 'qultuhû', 'nefsî', 've lâ a'lemu' — 10., 11., 20., 22., 25., 28., 29., 35. ve 37. kelime); "
          "'qâle subhâneke' faili 3MS (adsız; gönderge 'yâ 'îse', 16. kelime); 'yekûnu' 3MS (adsız; söz içi; 19. kelime); 'leyse' 3MS (adsız; söz içi; 24. kelime); "
          "'qultuhû' 3MS (adsız; söz içi; 29. kelime); ''alimtehû' 3MS (adsız; söz içi; 31. kelime)")
T[117] = ("konuşan 1S (adsız; söz içi; 'qultu', 'emertenî', 'rabbî', 've kuntu', 'dumtu', 'teveffeytenî' — 2., 6., 11., 13., 17. ve 20. kelime); "
          "muhatap 2MS (adsız; söz içi; 'emertenî', 'teveffeytenî', 'kunte', 'ente', 've ente' — 6., 20., 21., 22. ve 25. kelime); "
          "muhatap 2MP (adsız; söz içi; 'u'budû', 've rabbekum' — 9. ve 12. kelime); "
          "'lehum', ''aleyhim', 'fîhim', ''aleyhim' 3MP (adsız; söz içi; gönderge 5:116 9. kelime — 3., 14., 18. ve 24. kelime); 'bihî' 3MS (adsız; söz içi; 7. kelime)")

D = {}
D[116] = ("◇ 've iz qâle'llâhu yâ 'îse'bne meryeme e-ente qulte li'n-nâsi'ttexizûnî ve ummiye ilâheyni min dûni'llâhi qâle subhâneke mâ yekûnu lî en eqûle mâ leyse lî bi-haqqin in kuntu qultuhû fe-qad 'alimtehû ta'lemu mâ fî nefsî ve lâ a'lemu mâ fî nefsike inneke ente 'allâmu'l-ğuyûb' — "
 "'ve' + 'iz' + PERF 3MS I. bab + lafız + 'yâ' + adlı ''îsâ' + 'ibn' + adlı 'meryem' + 'e' + 'ente' + PERF 2MS I. bab + 'li' + belirli çoğul 'nâs' + IMPV 2MP VIII. bab + 1S + 've' + 'umm' + 1S + ikil 'ilâh' + 'min' + 'dûn' + lafız + "
 "PERF 3MS I. bab + 'subhân' + 2MS + 'mâ' + IMPF 3MS I. bab + 'li' + 1S + 'en' + IMPF 1S I. bab + 'mâ' + PERF 3MS I. bab + 'li' + 1S + 'bi' + nekre 'haqq' + 'in' + PERF 1S I. bab + PERF 1S I. bab + 3MS + 'fe' + 'qad' + PERF 2MS I. bab + 3MS + "
 "IMPF 2MS I. bab + 'mâ' + 'fî' + 'nefs' + 1S + 've' + 'lâ' + IMPF 1S I. bab + 'mâ' + 'fî' + 'nefs' + 2MS + 'inne' + 2MS + 'ente' + ''allâm' + belirli çoğul 'ğuyûb' "
 "(ölçüm edim soru, emir, nida, şart, kip CERT 1 · COND 1 · IMPV 1 · INTG 1 · NEG 2 · VOC 1; 1S 11 · 2MP 2 · 2MS 10 · 3MS 6; bab I. bab ×11 · VIII. bab ×1). "
 "Allah lafzı 3. ve 15. sırada (ölçüm allah z=0,38); Rab yok; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm aktör '{{1|adlı عِيسَى 4\\. sırada \\(kisi, rol meful\\+muhatap\\)}}' ve '{{1|adlı مَرْيَم 6\\. sırada \\(kisi, rol mecrur\\)}}' — satır aynen. "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=44 (n z=3,35); ölçüm '{{1|fâsıla ٱلغيوب → ب, ب sınıfı}}' — satır aynen (5:115 ن → 5:116 ب); "
 "ölçüm '{{1|simetri \\[7, 2, 16, 2\\]}}' — satır aynen; ölçüm '{{1|harf 156 → harf3 150, isaret 6}}' — satır aynen; ölçüm '{{1|dış düğüm 4}}' — satır aynen. "
 "Ölçüm VOC 1: 'yâ' (4. kelime); INTG 1: 'e-ente' (7. kelime); IMPV 1: 'ttexizûnî' (10. kelime); NEG 2: 'mâ' (18. kelime), 've lâ' (36. kelime); COND 1: 'in' (27. kelime); CERT 1: 'fe-qad' (30. kelime); "
 "'iz' (1.) T, 'fe-qad' (30.)'daki 'fe' RSLT, 'leyse' (24.) morph V (okuma). "
 "Kök ikilemesi (ölçüm) أله ×3 ('llâhu' 3., 'ilâheyni' 12. ve 'llâhi' 15. kelime), علم ×4 (''alimtehû' 31., 'ta'lemu' 32., 'a'lemu' 37. ve ''allâmu' 43. kelime), "
 "قول ×5 ('qâle' 2., 'qulte' 8., 'qâle' 16., 'eqûle' 22. ve 'qultuhû' 29. kelime), كون ×2 ('yekûnu' 19. / 'kuntu' 28. kelime), نفس ×2 ('nefsî' 35. / 'nefsike' 40. kelime) (okuma). "
 + T[116] + " (okuma). "
 + cumle(say('say 5:116 1-6 --on', "ve iz qâle'llâhu yâ 'îse'bne meryem", True), say('dizi 5 116 1 6', "iz qâle allâh 'îsâ ibn meryem"), say('say 5:116 4-6', "yâ 'îse'bne meryem"), say('dizi 5 116 4 6', "'îsâ ibn meryem")) + ' '
 + cumle(say('say 5:116 7-9', "e-ente qulte li'n-nâs", True), say('say 5:116 10-15', "ttexizûnî ve ummiye ilâheyni min dûni'llâh"), say('say 5:116 12-15', "ilâheyni min dûni'llâh"),
         say('say 5:116 13-15', "min dûni'llâh"), say('dizi 5 116 13 15', "min dûn allâh")) + ' '
 + cumle(say('say 5:116 16-17', "qâle subhânek", True), say('say 5:116 18-22', "mâ yekûnu lî en eqûle"), say('say 5:116 21-23', "en eqûle mâ"), say('dizi 5 116 21 23', "en qâle mâ"), say('say 5:116 23-26', "mâ leyse lî bi-haqq")) + ' '
 + cumle(say('say 5:116 27-31', "in kuntu qultuhû fe-qad 'alimtehû", True), say('say 5:116 32-34', "ta'lemu mâ fî"), say('dizi 5 116 32 34', "'alime mâ fî"), say('say 5:116 32-35', "ta'lemu mâ fî nefsî"), say('say 5:116 36-40 --on', "ve lâ a'lemu mâ fî nefsik")) + ' '
 + cumle(say('say 5:116 41-44', "inneke ente 'allâmu'l-ğuyûb", True), say('dizi 5 116 41 44', "inne _ 'allâm ğuyûb"), say('say 5:116 43-44', "'allâmu'l-ğuyûb")) + ' '
 "Ölçüm xref okunmuş 3 ayet ve henüz okunmamış 1 ayet. "
 "Ölçüm nakarat3 kalıpları: 'iz qâle allâh 'îsâ ibn meryem', 'inne _ 'allâm ğuyûb' ve ''îsâ ibn meryem' süzgeç GEÇER; 'en qâle mâ', 'min dûn allâh' ve ''alime mâ fî' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 'n-nâsi' (9. kelime).",
 "◈D — D1 've' + 'iz' + PERF + lafız + 'yâ' + adlı + izafet + adlı + 'e' + 'ente' + PERF + 'li' + belirli + IMPV + 've' + izafet + 'min' + izafet + lafız + PERF + izafet + 'mâ' + IMPF + 'li' + 'en' + IMPF + 'mâ' + PERF + 'li' + 'bi' + nekre + "
 "'in' + PERF + PERF + 'fe' + 'qad' + PERF + IMPF + 'mâ' + 'fî' + izafet + 've' + 'lâ' + IMPF + 'mâ' + 'fî' + izafet + 'inne' + 'ente' + izafet + belirli; "
 "D2 soru, emir, nida, şart, VOC ('yâ' 4. kelime), INTG ('e-ente' 7. kelime), IMPV ('ttexizûnî' 10. kelime), NEG ('mâ' 18. kelime, 've lâ' 36. kelime), COND ('in' 27. kelime), CERT ('fe-qad' 30. kelime); "
 "D3 أله ×3, علم ×4, قول ×5, كون ×2, نفس ×2; 9:78 eşi; D4 1S 11 · 2MP 2 · 2MS 10 · 3MS 6, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[116] + "; aktör 'yâ 'îse', 'meryeme' (ölçüm); A2 insanlara: beni ve annemi iki ilah edinin; seni tenzih ederim; hakkım olmayan şeyi söylemek; gaybları en iyi bilen; "
 "A3 'yâ 'îse'bne meryeme e-ente qulte li'n-nâsi'ttexizûnî ve ummiye ilâheyni min dûni'llâh' (söz içi, 4-15. kelime); iç söz 10-15. kelime; "
 "'subhâneke mâ yekûnu lî en eqûle mâ leyse lî bi-haqqin in kuntu qultuhû fe-qad 'alimtehû ta'lemu mâ fî nefsî ve lâ a'lemu mâ fî nefsike inneke ente 'allâmu'l-ğuyûb' (söz içi, 17-44. kelime; söz ayet sonunda kapanmıyor); "
 "A4 " + BOLUM + "; bölüm açılışı; söz açılır (4. kelime); söz açılır (10. kelime); söz kapanır (15. kelime, ayet içi); söz açılır (17. kelime); şahıs geçişi 3 → 1 (ayetler arası); "
 "edim geçişi şart → soru, emir, nida, şart (ayetler arası); şart → cevap (ayet içi; COND 'in' 27. kelime: 'in kuntu qultuhû' / 'fe-qad 'alimtehû' (30. kelime)).",
)

D[117] = ("◇ 'mâ qultu lehum illâ mâ emertenî bihî en u'budû'llâhe rabbî ve rabbekum ve kuntu 'aleyhim şehîden mâ dumtu fîhim fe-lemmâ teveffeytenî kunte ente'r-raqîbe 'aleyhim ve ente 'alâ kulli şey'in şehîd' — "
 "'mâ' + PERF 1S I. bab + 'li' + 3MP + 'illâ' + 'mâ' + PERF 2MS I. bab + 1S + 'bi' + 3MS + 'en' + IMPV 2MP I. bab + lafız + 'rabb' + 1S + 've' + 'rabb' + 2MP + 've' + PERF 1S I. bab + ''alâ' + 3MP + nekre 'şehîd' + "
 "'mâ' + PERF 1S I. bab + 'fî' + 3MP + 'fe' + 'lemmâ' + PERF 2MS V. bab + 1S + PERF 2MS I. bab + 'ente' + belirli 'raqîb' + ''alâ' + 3MP + 've' + 'ente' + ''alâ' + 'kull' + nekre 'şey'' + nekre 'şehîd' "
 "(ölçüm edim emir, kip IMPV 1 · NEG 1; 1S 9 · 2MP 3 · 2MS 8 · 3MP 4 · 3MS 1; bab I. bab ×6 · V. bab ×1). "
 "Allah lafzı 10. sırada (ölçüm allah z=0,16); Rab 11. ve 12. sırada (ölçüm rab z=1,15); "
 "ölçüm '{{2|esmâ شَهِيد 15\\. sırada, ORTA konum, MÜHÜRSÜZ \\| رَقِيب 23\\. sırada, ORTA konum, MÜHÜRSÜZ \\| شَهِيد 29\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET' — ölçüm MÜHÜRSÜZ ile uyuşmuyor (araç tanımı farkı; muhur_el EVET — tam okuma sonu); "
 "esma_el kaydı 'degil' — 've kuntu 'aleyhim şehîden', kural 'esmâ adı esmâ dışı göndergeyle → degil' (şahittim); "
 "esma_el kaydı 'ilahi' — 'kunte ente'r-raqîbe' ve 've ente 'alâ kulli şey'in şehîd', kural 'lafzın haberi → ilahi' (Allah) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=29 (n z=1,76); ölçüm '{{2|fâsıla شهيد → د, د sınıfı}}' — satır aynen (5:116 ب → 5:117 د); "
 "ölçüm '{{2|simetri \\[6, 1, 22, 2\\]}}' — satır aynen; ölçüm '{{2|harf 115 → harf3 108, isaret 7}}' — satır aynen; ölçüm '{{2|dış düğüm 2}}' — satır aynen. "
 "Ölçüm NEG 1: 'mâ' (1. kelime); IMPV 1: 'u'budû' (9. kelime); 'illâ' (4.) EXP, 'en' (8.) INT, 'mâ' (16.) SUB, 'fe-lemmâ' (19.)'daki 'fe' REM ve 'lemmâ' T, 've ente' (25.)'deki 've' REM (okuma). "
 "Kök ikilemesi (ölçüm) ربب ×2 ('rabbî' 11. / 've rabbekum' 12. kelime), شهد ×2 ('şehîden' 15. / 'şehîd' 29. kelime), كون ×2 ('ve kuntu' 13. / 'kunte' 21. kelime) (okuma). "
 + T[117] + " (okuma). "
 + cumle(say('say 5:117 1-7', "mâ qultu lehum illâ mâ emertenî bih", True), say('say 5:117 1-5', "mâ qultu lehum illâ mâ"), say('say 5:117 6-7', "emertenî bih")) + ' '
 + cumle(say('say 5:117 8-12', "en u'budû'llâhe rabbî ve rabbekum", True), say('say 5:117 9-12', "u'budû'llâhe rabbî ve rabbekum"), say('dizi 5 117 9 12', "'abede allâh rabb rabb"), say('say 5:117 11-12', "rabbî ve rabbekum")) + ' '
 + cumle(say('say 5:117 13-15 --on', "ve kuntu 'aleyhim şehîden", True), say('say 5:117 16-18', "mâ dumtu fîhim")) + ' '
 + cumle(say('say 5:117 19-20 --on', "fe-lemmâ teveffeytenî", True), say('say 5:117 21-24', "kunte ente'r-raqîbe 'aleyhim")) + ' '
 + cumle(say('say 5:117 25-29 --on', "ve ente 'alâ kulli şey'in şehîd", True), say('say 5:117 26-28', "'alâ kulli şey'"), say('dizi 5 117 26 28', "'alâ kull şey'"), say('say 5:117 27-29', "kulli şey'in şehîd")) + ' '
 "Ölçüm xref okunmuş 2 ayet. "
 "Ölçüm nakarat3 kalıpları: ''abede allâh rabb rabb' ve ''alâ kull şey'' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'mâ' + PERF + 'li' + 'illâ' + 'mâ' + PERF + 'bi' + 'en' + IMPV + lafız + izafet + 've' + izafet + 've' + PERF + ''alâ' + nekre + 'mâ' + PERF + 'fî' + 'fe' + 'lemmâ' + PERF + PERF + 'ente' + belirli + ''alâ' + 've' + 'ente' + ''alâ' + izafet + nekre + nekre; "
 "D2 emir, NEG ('mâ' 1. kelime), IMPV ('u'budû' 9. kelime); D3 ربب ×2, شهد ×2, كون ×2; 3:51 ve 5:72 eşi; D4 1S 9 · 2MP 3 · 2MS 8 · 3MP 4 · 3MS 1, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[117] + "; aktör yok (ölçüm); A2 bana emrettiğin şeyden başkasını söylemedim; Allah'a kulluk edin; onlara şahittim; vefat ettirince gözeten sen oldun; her şeye şahitsin; "
 "A3 söz sürüyor (5:116 17. kelimeden; 1-29. kelime; söz ayet sonunda kapanmıyor); 'u'budû'llâhe rabbî ve rabbekum' (iç söz, 9-12. kelime); "
 "A4 " + BOLUM + "; söz açılır (9. kelime); edim geçişi soru, emir, nida, şart → emir (ayetler arası).",
)

out = ['# ── blok 5:116-117 (2026-11-18) ──', 'MEAL35 = {']
for n in range(116, 118):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M35 = {']
for n in range(116, 118):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL35); M.update(M35)']
open('/home/claude/yamalar/metin_5_116_117.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

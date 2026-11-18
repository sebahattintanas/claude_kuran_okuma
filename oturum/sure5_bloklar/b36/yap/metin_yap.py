# blok 36 (5:118-120) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b36/say2.txt'
os.environ['OLC'] = '/home/claude/b36/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'İsâ'ya soru; doğruların fayda gördüğü gün' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 118: "Eğer onlara azap edersen, şüphesiz onlar senin kullarındır; eğer onları bağışlarsan, şüphesiz sen azîzsin, hikmet sahibisin.",
 119: "Allah dedi: Bu, doğrulara doğruluklarının fayda verdiği gün. Onlar için altlarından ırmaklar akan cennetler var; orada ebedî olarak kalacaklar. Allah onlardan razı olmuş, onlar da O'ndan razı olmuşlardır. İşte bu büyük kurtuluş.",
 120: "Göklerin ve yerin ve onlarda olanların mülkü Allah'ındır; O her şeye güç yetirendir.",
}

T = {}
T[118] = ("muhatap 2MS (adsız; söz içi; 'tu'azzibhum', ''ibâduke', 'teğfir', 'fe-inneke', 'ente' — 2., 4., 6., 8. ve 9. kelime); "
          "'tu'azzibhum', 'fe-innehum', 'lehum' 3MP (adsız; söz içi; gönderge 5:116 9. kelime — 2., 3. ve 7. kelime)")
T[119] = ("'qâle' 3MS (fiil uyumu; 1. kelime — fail 2. kelime); 'llâhu' ('qâle' faili; lafız; 2. kelime); "
          "'yenfa'u' 3MS (fiil uyumu; söz içi; 5. kelime — fail 7. kelime); "
          "'sidquhum', 'lehum', ''anhum', 've radû' 3MP (adsız; söz içi; gönderge 's-sâdiqîne', 6. kelime — 7., 8., 19. ve 20. kelime); "
          "'tecrî', 'tahtihe', 'fîhâ' 3FS (adsız; söz içi; gönderge 'cennâtun', 9. kelime — 10., 12. ve 15. kelime); "
          "'radiya' 3MS (fiil uyumu; söz içi; 17. kelime — fail 18. kelime); 'llâhu' ('radiya' faili; lafız; söz içi; 18. kelime); "
          "''anhu' 3MS (adsız; söz içi; gönderge lafız, 21. kelime)")
T[120] = ("'li'llâhi' (haber — mecrur; lafız; 1. kelime); 'fîhinne' 3FP (adsız; gönderge 's-semâvâti' ve 'l-ardi', 6. kelime); "
          "'huve' 3MS (adsız; gönderge lafız, 7. kelime)")

D = {}
D[118] = ("◇ 'in tu'azzibhum fe-innehum 'ibâduke ve in teğfir lehum fe-inneke ente'l-'azîzu'l-hakîm' — "
 "'in' + IMPF 2MS II. bab + 3MP + 'fe' + 'inne' + 3MP + çoğul ''abd' + 2MS + 've' + 'in' + IMPF 2MS I. bab + 'li' + 3MP + 'fe' + 'inne' + 2MS + 'ente' + belirli ''azîz' + belirli 'hakîm' "
 "(ölçüm edim şart, kip COND 2; 2MS 5 · 3MP 3; bab I. bab ×1 · II. bab ×1). "
 "Lafız yok; Rab yok; ölçüm '{{1|esmâ عَزِيز 10\\. sırada, SON konum, MÜHÜR \\| حَكِيم 11\\. sırada, SON konum, MÜHÜR}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET (ÇİFT) ton celâl' (uyuşuyor) — esma_el kaydı 'ilahi' — 'fe-inneke ente'l-'azîzu'l-hakîm', kural ''inne/enne' haberi → ilahi' (Allah) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=11 (n z=-0,15); ölçüm '{{1|fâsıla ٱلحكيم → م, N sınıfı}}' — satır aynen (5:117 د → 5:118 م); "
 "ölçüm '{{1|simetri \\[3, 1, 5, 1\\]}}' — satır aynen; ölçüm '{{1|harf 48 → harf3 47, isaret 1}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen. "
 "Ölçüm COND 2: 'in' (1. kelime), 've in' (5. kelime); 'fe-innehum' (3.) ve 'fe-inneke' (8.) kelimelerindeki 'fe' RSLT, 've in' (5.) kelimesindeki 've' CONJ (okuma). "
 + T[118] + " (okuma). "
 + cumle(say('say 5:118 1-4', "in tu'azzibhum fe-innehum 'ibâduk", True), say('say 5:118 1-2', "in tu'azzibhum"), say('say 5:118 3-4 --on', "fe-innehum 'ibâduk")) + ' '
 + cumle(say('say 5:118 5-7 --on', "ve in teğfir lehum", True), say('say 5:118 8-11 --on', "fe-inneke ente'l-'azîzu'l-hakîm"), say('say 5:118 9-11', "ente'l-'azîzu'l-hakîm"),
         say('say 5:118 10-11', "l-'azîzu'l-hakîm"), say('dizi 5 118 10 11', "'azîz hakîm")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'tu'azzibhum' / 'teğfir' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'in' + IMPF + 'fe' + 'inne' + izafet + 've' + 'in' + IMPF + 'li' + 'fe' + 'inne' + 'ente' + belirli + belirli; "
 "D2 şart, COND ('in' 1. kelime, 've in' 5. kelime); D3 —; D4 2MS 5 · 3MP 3, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[118] + "; aktör yok (ölçüm); A2 azap edersen onlar senin kullarındır; bağışlarsan sen azîzsin, hikmet sahibisin; "
 "A3 söz sürüyor (5:116 17. kelimeden; 1-11. kelime); "
 "A4 " + BOLUM + "; söz kapanır (11. kelime); şahıs geçişi 1 → 2 (ayetler arası); edim geçişi emir → şart (ayetler arası); "
 "şart → cevap (ayet içi; COND 'in' 1. kelime: 'in tu'azzibhum' / 'fe-innehum 'ibâduk' (3. kelime)); "
 "şart → cevap (ayet içi; COND 'in' 5. kelime: 've in teğfir lehum' / 'fe-inneke ente'l-'azîzu'l-hakîm' (8. kelime)).",
)

D[119] = ("◇ 'qâle'llâhu hâzâ yevmu yenfa'u's-sâdiqîne sidquhum lehum cennâtun tecrî min tahtihe'l-enhâru xâlidîne fîhâ ebeden radiya'llâhu 'anhum ve radû 'anhu zâlike'l-fevzu'l-'azîm' — "
 "PERF 3MS I. bab + lafız + 'hâ' + 'zâ' + 'yevm' + IMPF 3MS I. bab + belirli çoğul etken ortaç 'sâdiq' + 'sidq' + 3MP + 'li' + 3MP + çoğul nekre 'cenne' + IMPF 3FS I. bab + 'min' + 'taht' + 3FS + belirli çoğul 'neher' + "
 "çoğul etken ortaç 'xâlid' + 'fî' + 3FS + nekre zarf 'ebeden' + PERF 3MS I. bab + lafız + ''an' + 3MP + 've' + PERF 3MP I. bab + ''an' + 3MS + 'zâlike' + belirli 'fevz' + belirli ''azîm' "
 "(ölçüm edim haber, kip yok, biçim DIKKAT; 3FS 3 · 3MP 5 · 3MS 4; bab I. bab ×5). "
 "Allah lafzı 2. ve 18. sırada (ölçüm allah z=1,14); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=24 (n z=1,23); ölçüm '{{2|fâsıla ٱلعظيم → م, N sınıfı}}' — satır aynen (5:118 م → 5:119 م); "
 "ölçüm '{{2|simetri \\[3, 2, 18, 1\\]}}' — satır aynen; ölçüm '{{2|harf 104 → harf3 98, isaret 6}}' — satır aynen; ölçüm '{{2|dış düğüm 1}}' — satır aynen. "
 "Ölçüm biçim DIKKAT — 'hâzâ' dikkat öneki (3. kelime, morph ATT); 've radû' (20.) kelimesindeki 've' CONJ; 'zâlike' (22.) morph DIST (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 ('qâle'llâhu' 2. / 'radiya'llâhu' 18. kelime), رضو ×2 ('radiya' 17. / 've radû' 20. kelime), صدق ×2 ('s-sâdiqîne' 6. / 'sidquhum' 7. kelime) (okuma). "
 + T[119] + " (okuma). "
 + cumle(say('say 5:119 1-2', "qâle'llâh", True), say('say 5:119 3-7', "hâzâ yevmu yenfa'u's-sâdiqîne sidquhum"), say('say 5:119 4-7', "yevmu yenfa'u's-sâdiqîne sidquhum")) + ' '
 + cumle(say('say 5:119 8-16', "lehum cennâtun tecrî min tahtihe'l-enhâru xâlidîne fîhâ ebeden", True), say('say 5:119 9-15', "cennâtun tecrî min tahtihe'l-enhâru xâlidîne fîhâ"),
         say('dizi 5 119 9 15', "cenne cerey min taht neher xâlid fî"), say('say 5:119 9-13', "cennâtun tecrî min tahtihe'l-enhâr"), say('dizi 5 119 9 13', "cenne cerey min taht neher"),
         say('say 5:119 14-16', "xâlidîne fîhâ ebeden")) + ' '
 + cumle(say('say 5:119 17-21', "radiya'llâhu 'anhum ve radû 'anh", True), say('say 5:119 17-19', "radiya'llâhu 'anhum"), say('say 5:119 22-24', "zâlike'l-fevzu'l-'azîm")) + ' '
 "Ölçüm xref 98:8 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıpları: 'cenne cerey min taht neher xâlid fî' ve 'cenne cerey min taht neher' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K1 'l-enhâru' (13. kelime); K2 'yevmu' (4. kelime), 'ebeden' (16. kelime).",
 "◈B — —",
 "◈D — D1 PERF + lafız + 'hâ' + 'zâ' + 'yevm' + IMPF + belirli + izafet + 'li' + nekre + IMPF + 'min' + izafet + belirli + ortaç + 'fî' + nekre + PERF + lafız + ''an' + 've' + PERF + ''an' + 'zâlike' + belirli + belirli; "
 "D2 haber; D3 أله ×2, رضو ×2, صدق ×2; 98:8 eşi; D4 3FS 3 · 3MP 5 · 3MS 4, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[119] + "; aktör yok (ölçüm); A2 doğrulara doğruluklarının fayda verdiği gün; altlarından ırmaklar akan cennetler; ebedî kalış; karşılıklı rıza; büyük kurtuluş; "
 "A3 'hâzâ yevmu yenfa'u's-sâdiqîne sidquhum lehum cennâtun tecrî min tahtihe'l-enhâru xâlidîne fîhâ ebeden radiya'llâhu 'anhum ve radû 'anhu zâlike'l-fevzu'l-'azîm' (söz içi, 3-24. kelime); "
 "A4 " + BOLUM + "; söz açılır (3. kelime); söz kapanır (24. kelime, ayet içi); şahıs geçişi 2 → 3 (ayetler arası); edim geçişi şart → haber (ayetler arası).",
)

D[120] = ("◇ 'li'llâhi mulku's-semâvâti ve'l-ardi ve mâ fîhinne ve huve 'alâ kulli şey'in qadîr' — "
 "'li' + lafız + 'mulk' + belirli çoğul 'semâ'' + 've' + belirli 'ard' + 've' + 'mâ' + 'fî' + 3FP + 've' + 'huve' + ''alâ' + 'kull' + nekre 'şey'' + nekre 'qadîr' "
 "(ölçüm edim haber, kip yok; 3FP 1 · 3MS 1; bab yok). "
 "Allah lafzı 1. sırada (ölçüm allah z=1,29); Rab yok; ölçüm '{{3|esmâ قَدِير 11\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET ton celâl' — ölçüm MÜHÜRSÜZ ile uyuşmuyor (araç tanımı farkı; muhur_el EVET — tam okuma sonu); "
 "esma_el kaydı 'ilahi' — 've huve 'alâ kulli şey'in qadîr', kural 'lafzın haberi → ilahi' (Allah) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=11 (n z=-0,15); ölçüm '{{3|fâsıla قدير → ر, R sınıfı}}' — satır aynen (5:119 م → 5:120 ر); "
 "ölçüm '{{3|harf 43 → harf3 40, isaret 3}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen; "
 "ölçüm '{{3|esit2 → 3:189 oran 0,8732 kademe BENZER}}' — satır aynen (3:189 emsal olarak basıldı). "
 "Ölçüm kip yok; 've'l-ardi' (4.), 've mâ' (5.) ve 've huve' (7.) kelimelerindeki 've' CONJ (okuma). "
 + T[120] + " (okuma). "
 + cumle(say('say 5:120 1-6', "li'llâhi mulku's-semâvâti ve'l-ardi ve mâ fîhinn", True), say('say 5:120 1-5', "li'llâhi mulku's-semâvâti ve'l-ardi ve mâ"),
         say('dizi 5 120 1 5', "allâh mulk semâ' ard mâ"), say('say 5:120 2-4', "mulku's-semâvâti ve'l-ard"), say('dizi 5 120 2 4', "mulk semâ' ard")) + ' '
 + cumle(say('say 5:120 7-11 --on', "ve huve 'alâ kulli şey'in qadîr", True), say('say 5:120 8-11', "'alâ kulli şey'in qadîr"), say('dizi 5 120 8 11', "'alâ kull şey' qadîr"),
         say('say 5:120 8-10', "'alâ kulli şey'"), say('dizi 5 120 8 10', "'alâ kull şey'")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıpları: 'allâh mulk semâ' ard mâ', ''alâ kull şey' qadîr', ''alâ kull şey'' ve 'mulk semâ' ard' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K1 's-semâvâti' (3. kelime), 'l-ardi' (4. kelime).",
 "◈B — —",
 "◈D — D1 'li' + lafız + izafet + belirli + 've' + belirli + 've' + 'mâ' + 'fî' + 've' + 'huve' + ''alâ' + izafet + nekre + nekre; "
 "D2 haber; D3 —; 3:189 eşi; D4 3FP 1 · 3MS 1, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[120] + "; aktör yok (ölçüm); A2 göklerin, yerin ve onlarda olanların mülkü Allah'ın; her şeye güç yetiren; "
 "A3 —; "
 "A4 " + BOLUM + "; bölüm kapanışı.",
)

out = ['# ── blok 5:118-120 (2026-11-18) ──', 'MEAL36 = {']
for n in range(118, 121):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M36 = {']
for n in range(118, 121):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL36); M.update(M36)']
open('/home/claude/yamalar/metin_5_118_120.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

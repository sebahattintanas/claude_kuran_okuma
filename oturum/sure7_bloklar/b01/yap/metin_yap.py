# sûre 7 blok 1 (7:1-5) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b01/say2.txt'
os.environ['OLC'] = '/home/claude/b01/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Kitap indirildi; helak edilen kentler; tartı; yeryüzünde yerleştirme' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 1: "Elif Lâm Mîm Sâd.",
 2: "Sana indirilen bir kitaptır; öyleyse ondan ötürü göğsünde bir sıkıntı olmasın; onunla uyarman için ve inananlara bir hatırlatma olarak.",
 3: "Rabbinizden size indirilene uyun; O'ndan başka dostlara uymayın. Pek az düşünüyorsunuz.",
 4: "Nice şehri helâk ettik; şiddetimiz ona geceleyin ya da onlar öğle uykusundayken geldi.",
 5: "Şiddetimiz onlara geldiğinde yakarışları ancak şunu demeleri oldu: Biz gerçekten zalimmişiz.",
}

T = {}
T[2] = ("'unzile' 3MS (adsız; edilgen, naib-i faili 'kitâbun' 1. kelime, 2. kelime); muhatap 2MS eki (adsız; 'ileyke', 'sadrike' — 3. ve 7. kelime); 'yekun' 3MS (fiil uyumu; 5. kelime — fail 8. kelime); "
        "'minhu', 'bihî' 3MS eki (adsız; gönderge 'kitâbun' 1. kelime — 9. ve 11. kelime); muhatap 2MS (adsız; 'li-tunzire' — 10. kelime)")
T[3] = ("muhatap 2MP (adsız; 'ittebi'û', 'tettebi'û', 'tezekkerûn' — 1., 8. ve 14. kelime); 'unzile' 3MS (adsız; edilgen, naib-i faili 'mâ' 2. kelime, 3. kelime); "
        "muhatap 2MP eki (adsız; 'ileykum', 'rabbikum' — 4. ve 6. kelime); 'dûnihî' 3MS eki (adsız; gönderge 'rabbikum' 6. kelime, 10. kelime)")
T[4] = ("konuşan 1P (adsız; 'ehleknâhâ' — 4. kelime); 'ehleknâhâ', 'fe-câ'ehâ' 3FS eki (adsız; gönderge 'qaryetin' 3. kelime — 4. ve 5. kelime); 'fe-câ'ehâ' 3MS (fiil uyumu; 5. kelime — fail 6. kelime); "
        "konuşan 1P eki (adsız; 'be'sunâ' — 6. kelime); 'hum' 3MP (adsız; tartışmalı; cins uyumsuz; gönderge 'qaryetin' 3. kelime, 9. kelime)")
T[5] = ("'kâne' 3MS (fiil uyumu; 2. kelime — fail 3. kelime); 'da'vâhum', 'câ'ehum' 3MP eki (adsız; gönderge 7:4 9. kelime — 3. ve 5. kelime); 'câ'ehum' 3MS (fiil uyumu; 5. kelime — fail 6. kelime); "
        "konuşan 1P eki (adsız; 'be'sunâ' — 6. kelime); 'qâlû' 3MP (adsız; gönderge 7:4 9. kelime, 9. kelime); konuşan 1P eki (adsız; söz içi; 'innâ' — 10. kelime); konuşan 1P (adsız; söz içi; 'kunnâ' — 11. kelime)")

D = {}
D[1] = ("◇ 'elif lâm mîm sâd' — harf dizisi (morph INL; kök ve lemma yok) "
 "(ölçüm edim haber, kip yok; şahıs işaret yok; bab yok). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=1 (n z=-1,21); ölçüm '{{1|fâsıla الٓمٓصٓ → ٓ, ٓ sınıfı}}' — satır aynen (sûre açılışı); "
 "ölçüm '{{1|harf 23 → harf3 4, isaret 0}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen. "
 "Ölçüm kip yok (okuma). "
 + cumle(say('say 7:1 1-1', "elif lâm mîm sâd", True)) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 harf dizisi (kök yok); "
 "D2 haber; kip yok; D3 —; D4 şahıs işaret yok, sahset —, iltifât 0.",
 "◈A — A1 —; aktör yok (ölçüm); A2 harf dizisi; "
 "A3 —; "
 "A4 " + BOLUM + "; bölüm açılışı; sûre açılışı.",
)

D[2] = ("◇ 'kitâbun unzile ileyke fe-lâ yekun fî sadrike haracun minhu li-tunzire bihî ve zikrâ li'l-mu'minîn' — "
 "nekre 'kitâb' + PERF 3MS IV. bab edilgen + 'ilâ' + 2MS + 'fe' + 'lâ' + IMPF 3MS I. bab + 'fî' + 'sadr' + 2MS + nekre 'harac' + 'min' + 3MS + 'li' + IMPF 2MS IV. bab + 'bi' + 3MS + 've' + 'zikrâ' + 'li' + belirli çoğul etken ortaç 'mu'min' "
 "(ölçüm edim yasak, kip PRO 1; 2MS 3 · 3MS 4; bab I. bab ×1 · IV. bab ×2). "
 "Allah lafzı yok; Rab yok; ölçüm '{{2|esmâ مُؤْمِن 13\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET ton cemâl' — ölçüm MÜHÜRSÜZ ile uyuşmuyor (araç tanımı farkı; muhur_el hayır — ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 've zikrâ li'l-mu'minîn', kural 'esmâ adı esmâ dışı göndergeyle → degil' (inanan insanlar) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=13 (n z=0,06); ölçüm '{{2|EDİLGEN 1/3 fiil, pas z=1,57}}' — satır aynen; ölçüm '{{2|fâsıla للمؤمنين → ن, N sınıfı}}' — satır aynen (7:1 ٓ → 7:2 ن); "
 "ölçüm '{{2|simetri \\[3, 4, 9, 1\\]}}' — satır aynen; ölçüm '{{2|harf 51 → harf3 49, isaret 2}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm PRO 1: 'lâ' (4. kelime); ölçüm biçim NEHY ('lâ' 4. kelime); "
 "'fe-lâ' (4.) kelimesindeki 'fe' REM; 'li-tunzire' (10.) kelimesindeki 'li' PRP; 've zikrâ' (12.) kelimesindeki 've' CONJ (okuma). "
 + T[2] + " (okuma). "
 + cumle(say('say 7:2 1-3', "kitâbun unzile ileyke", True), say('say 7:2 2-3', "unzile ileyke")) + ' '
 + cumle(say('say 7:2 4-9', "fe-lâ yekun fî sadrike haracun minhu", True), say('say 7:2 10-11', "li-tunzire bihî")) + ' '
 + cumle(say('say 7:2 12-13', "ve zikrâ li'l-mu'minîn", True)) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 nekre + PERF + 'ilâ' + 'fe' + 'lâ' + IMPF + 'fî' + izafet + nekre + 'min' + 'li' + IMPF + 'bi' + 've' + 'zikrâ' + 'li' + belirli; "
 "D2 yasak; PRO ('lâ' 4. kelime); D3 —; D4 2MS 3 · 3MS 4, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[2] + "; aktör yok (ölçüm); A2 muhataba indirilen kitap; göğüste ondan ötürü sıkıntı olmaması; onunla uyarma ve inananlara hatırlatma; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi — → 3 (ayetler arası) eksiltili (7:1 şahıs işareti taşımıyor); edim geçişi haber → yasak (ayetler arası).",
)

D[3] = ("◇ 'ittebi'û mâ unzile ileykum min rabbikum ve lâ tettebi'û min dûnihî evliyâ', qalîlen mâ tezekkerûn' — "
 "IMPV 2MP VIII. bab + 'mâ' + PERF 3MS IV. bab edilgen + 'ilâ' + 2MP + 'min' + 'rabb' + 2MP + 've' + 'lâ' + IMPF 2MP VIII. bab + 'min' + 'dûn' + 3MS + çoğul 'velî' + nekre 'qalîl' + 'mâ' + IMPF 2MP V. bab "
 "(ölçüm edim emir, yasak, kip IMPV 1 · PRO 1; 2MP 8 · 3MS 2; bab IV. bab ×1 · V. bab ×1 · VIII. bab ×2). "
 "Allah lafzı yok; Rab 6. sırada (ölçüm rab z=1,20); ölçüm '{{3|esmâ وَلِيّ 11\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET ton cemâl' — ölçüm MÜHÜRSÜZ ile uyuşmuyor (araç tanımı farkı; muhur_el hayır — ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 've lâ tettebi'û min dûnihî evliyâ'', kural 'esmâ adı esmâ dışı göndergeyle → degil' (O'ndan başka edinilen dostlar) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=14 (n z=0,17); ölçüm '{{3|EDİLGEN 1/4 fiil, pas z=1,10}}' — satır aynen; ölçüm '{{3|fâsıla تذكرون → ن, N sınıfı}}' — satır aynen (7:2 ن → 7:3 ن); "
 "ölçüm '{{3|sayı işareti قَلِيل}}' — satır aynen; ölçüm '{{3|simetri \\[3, 1, 8, 1\\]}}' — satır aynen; ölçüm '{{3|harf 62 → harf3 57, isaret 5}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm IMPV 1: 'ittebi'û' (1. kelime); PRO 1: 'lâ' (7. kelime); ölçüm biçim NEHY ('lâ' 7. kelime); "
 "'ve lâ' (7.) kelimesindeki 've' CONJ; 'mâ' (2.) REL; 'mâ' (13.) SUP (okuma). "
 "Kök ikilemesi (ölçüm) تبع ×2 ('ittebi'û' 1. / 'tettebi'û' 8. kelime) (okuma). "
 + T[3] + " (okuma). "
 + cumle(say('say 7:3 1-3', "ittebi'û mâ unzile", True), say('say 7:3 3-6', "unzile ileykum min rabbikum")) + ' '
 + say('say 7:3 1-2 --on', "ittebi'û mâ", True) + " (--medde 5 ayet: 'mâ' yazım farkı ile; harekesiz sayım elif / medde yazımına bağlı). "
 + cumle(say('say 7:3 7-8', "ve lâ tettebi'û", True), say('say 7:3 9-11', "min dûnihî evliyâ'")) + ' '
 + cumle(say('say 7:3 12-14', "qalîlen mâ tezekkerûn", True)) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPV + 'mâ' + PERF + 'ilâ' + 'min' + izafet + 've' + 'lâ' + IMPF + 'min' + izafet + 'velî' + nekre + 'mâ' + IMPF; "
 "D2 emir, yasak; IMPV ('ittebi'û' 1. kelime), PRO ('lâ' 7. kelime); D3 تبع ×2; D4 2MP 8 · 3MS 2, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[3] + "; aktör yok (ölçüm); A2 Rabden indirilene uyma emri; O'ndan başka dostlara uyma yasağı; az düşünme; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 3 → 2 (ayetler arası); edim geçişi yasak → emir, yasak (ayetler arası).",
)

D[4] = ("◇ 've kem min qaryetin ehleknâhâ fe-câ'ehâ be'sunâ beyâten ev hum qâ'ilûn' — "
 "'ve' + 'kem' + 'min' + nekre 'qarye' + PERF 1P IV. bab + 3FS + 'fe' + PERF 3MS I. bab + 3FS + 'be's' + 1P + nekre 'beyât' + 'ev' + 'hum' + çoğul etken ortaç 'qâ'il' "
 "(ölçüm edim haber, kip yok; 1P 3 · 3FS 2 · 3MP 1 · 3MS 1; bab I. bab ×1 · IV. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok (ölçüm); ölçüm '{{4|aktör: adsız `karye` 3\\. sırada}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=10 (n z=-0,26); ölçüm '{{4|fâsıla قآئلون → ن, N sınıfı}}' — satır aynen (7:3 ن → 7:4 ن); "
 "ölçüm '{{4|simetri \\[3, 1, 8, 1\\]}}' — satır aynen; ölçüm '{{4|harf 41 → harf3 41, isaret 0}}' — satır aynen; ölçüm '{{4|dış düğüm 0}}' — satır aynen. "
 "Ölçüm kip yok; 've kem' (1.) kelimesindeki 've' REM; 'fe-câ'ehâ' (5.) kelimesindeki 'fe' CONJ; 'ev' (8.) CONJ (okuma). "
 + T[4] + " (okuma). "
 + cumle(say('say 7:4 1-4', "ve kem min qaryetin ehleknâhâ", True), say('say 7:4 2-4', "min qaryetin ehleknâhâ")) + ' '
 + cumle(say('say 7:4 5-10', "fe-câ'ehâ be'sunâ beyâten ev hum qâ'ilûn", True), say('say 7:4 6-7', "be'sunâ beyâten")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'kem' + 'min' + nekre + PERF + 'fe' + PERF + izafet + nekre + 'ev' + 'hum' + 'qâ'il'; "
 "D2 haber; kip yok; D3 —; D4 1P 3 · 3FS 2 · 3MP 1 · 3MS 1, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[4] + "; ölçüm aktör adsız 'qaryetin' (3. kelime); A2 nice şehrin helâk edilmesi; şiddetin geceleyin ya da öğle uykusunda gelmesi; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 2 → 1 (ayetler arası); şahıs sayısında toplam farkı (1P 3 · 3. şahıs 4 — ölçüm baskın 1); edim geçişi emir, yasak → haber (ayetler arası).",
)

D[5] = ("◇ 'fe-mâ kâne da'vâhum iz câ'ehum be'sunâ illâ en qâlû innâ kunnâ zâlimîn' — "
 "'fe' + 'mâ' + PERF 3MS I. bab + 'da'vâ' + 3MP + 'iz' + PERF 3MS I. bab + 3MP + 'be's' + 1P + 'illâ' + 'en' + PERF 3MP I. bab + 'inne' + 1P + PERF 1P I. bab + çoğul etken ortaç 'zâlim' "
 "(ölçüm edim haber, kip NEG 1 · RES 1; 1P 4 · 3MP 4 · 3MS 2; bab I. bab ×4). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=12 (n z=-0,04); ölçüm '{{5|fâsıla ظلمين → ن, N sınıfı}}' — satır aynen (7:4 ن → 7:5 ن); "
 "ölçüm '{{5|simetri \\[3, 1, 10, 1\\]}}' — satır aynen; ölçüm '{{5|harf 46 → harf3 45, isaret 1}}' — satır aynen; ölçüm '{{5|dış düğüm 2}}' — satır aynen. "
 "Ölçüm NEG 1: 'mâ' (1. kelime); RES 1: 'illâ' (7. kelime); ölçüm biçim HASR ('illâ' 7. kelime); "
 "'fe-mâ' (1.) kelimesindeki 'fe' CONJ; 'en' (8.) SUB; 'innâ' (10.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) كون ×2 ('kâne' 2. / 'kunnâ' 11. kelime) (okuma). "
 + T[5] + " (okuma). "
 + cumle(say('say 7:5 1-9', "fe-mâ kâne da'vâhum iz câ'ehum be'sunâ illâ en qâlû", True), say('say 7:5 7-9', "illâ en qâlû"), say('dizi 7 5 7 9', "illâ en qâle")) + ' '
 + say('say 7:5 4-6', "iz câ'ehum be'sunâ", True) + " (--medde 2 ayet: 'be'sunâ' yazım farkı ile; harekesiz sayım elif / medde yazımına bağlı). "
 + say('say 7:5 4-6 --on', "iz câ'ehum be'sunâ", True) + " (--medde 2 ayet: 'be'sunâ' yazım farkı ile; harekesiz sayım elif / medde yazımına bağlı). "
 + say('say 7:5 5-6', "câ'ehum be'sunâ", True) + " (--medde 2 ayet: 'be'sunâ' yazım farkı ile; harekesiz sayım elif / medde yazımına bağlı). "
 + say('say 7:5 5-6 --on', "câ'ehum be'sunâ", True) + " (--medde 2 ayet: 'be'sunâ' yazım farkı ile; harekesiz sayım elif / medde yazımına bağlı). "
 + cumle(say('say 7:5 10-12', "innâ kunnâ zâlimîn", True), say('dizi 7 5 10 12', "inne kâne zâlim"), say('say 7:5 11-12', "kunnâ zâlimîn"), say('dizi 7 5 9 12', "qâle inne kâne zâlim")) + ' ' +
 "Ölçüm xref 21:14 (emsal olarak basıldı), 21:46 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıbı: 'illâ en qâle' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'fe' + 'mâ' + PERF + izafet + 'iz' + PERF + izafet + 'illâ' + 'en' + PERF + 'inne' + PERF + 'zâlim'; "
 "D2 haber; NEG ('mâ' 1. kelime), RES ('illâ' 7. kelime); D3 21:14 eşi, 21:46 eşi, كون ×2; D4 1P 4 · 3MP 4 · 3MS 2, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[5] + "; aktör yok (ölçüm); A2 şiddet geldiğinde yakarışlarının yalnız zalim olduklarını söylemek olması; "
 "A3 'innâ kunnâ zâlimîn' (söz içi, 10-12. kelime); "
 "A4 " + BOLUM + "; söz açılır (10. kelime); söz kapanır (12. kelime, ayet içi); şahıs geçişi 1 → 3 (ayetler arası); edim geçişi yok (ayetler arası).",
)
out = ['# ── blok 7:1-5 (2026-11-24) ──', 'MEAL1 = {']
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
open('/home/claude/yamalar/metin_7_1_5.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

# blok 10 (5:27-30) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b10/say2.txt'
os.environ['OLC'] = '/home/claude/b10/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Âdem'in iki oğlu; bir canı öldürmek' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 27: "Onlara Âdem'in iki oğlunun haberini gerçekle oku: Hani onlar birer kurban sunmuşlardı da birinden kabul edilmiş, ötekinden kabul edilmemişti. 'Seni mutlaka öldüreceğim' dedi. Öteki dedi ki: 'Allah ancak sakınanlardan kabul eder.",
 28: "Andolsun, beni öldürmek için elini bana uzatsan da ben seni öldürmek için elimi sana uzatacak değilim; çünkü ben âlemlerin Rabbi Allah'tan korkarım.",
 29: "Ben istiyorum ki benim günahımı da kendi günahını da yüklenesin de ateş halkından olasın; zalimlerin cezası budur.'",
 30: "Sonunda nefsi ona kardeşini öldürmeyi kolay gösterdi; onu öldürdü ve hüsrana uğrayanlardan oldu.",
}

T27 = ("muhatap 2MS (adsız; 'tlu'); ''aleyhim' 3MP (adsız); 'bney âdeme' (Âdem'in iki oğlu; 4-5. kelime — ölçüm aktör adlı); 'qarrabâ' faili 3MD (adsız; gönderge iki oğul); 'qurbânen' (mef'ûl; nekre, 9. kelime); "
       "'tuqubbile' faili (adsız; edilgen — nâib fâil 3MS, kurban takdiri, 10. kelime); 'ehadihimâ' 3D (gönderge iki oğul; 12. kelime); 'yutaqabbel' faili (adsız; edilgen — nâib fâil 3MS, 14. kelime); 'l-âxar' (16. kelime); "
       "'qâle' faili 3MS (adsız; 17. kelime — gönderge kurbanı kabul edilmeyen); söz içi konuşan 1S (adsız; 'aqtulenne'); söz içi muhatap 2MS (adsız; 'aqtulenneke'); 'qâle' faili 3MS (adsız; 19. kelime — gönderge kurbanı kabul edilen); Allah (lafız; 22. kelime); 'l-muttaqîn' (24. kelime)")
T28 = ("söz içi konuşan 1S (adsız; 'ileyye', 'li-taqtulenî', 'ene', 'yediye', 'li-aqtuleke', 'innî', 'exâfu' — gönderge kurbanı kabul edilen); söz içi muhatap 2MS (adsız; 'besatte', 'yedeke', 'ileyke'); Allah (lafız; 14. kelime); 'rabbe'l-'âlemîn' (Rab; lafzın sıfatı, 15-16. kelime)")
T29 = ("söz içi konuşan 1S (adsız; 'innî', 'urîdu', 'ismî'); söz içi muhatap 2MS (adsız; 'tebû'e', 'ismike', 'tekûne'); 'ashâbi'n-nâr' (izafet; 9-10. kelime); 'zâlike' (işaret; 11. kelime); 'z-zâlimîn' (13. kelime)")
T30 = ("'nefsuhû' ('tavva'at' faili; 3. kelime); 'lehû' ve 'nefsuhû' 3MS (adsız; gönderge kurbanı kabul edilmeyen); 'exîhi' (kardeş; 5. kelime); 'qatelehû' faili 3MS (adsız) ve mef'ûlü 3MS (adsız; gönderge kardeş); 'asbaha' faili 3MS (adsız); 'l-xâsirîn' (9. kelime)")

D = {}
D[27] = ("◇ 've'tlu 'aleyhim nebe'e'bney âdeme bi'l-haqqi iz qarrabâ qurbânen fe-tuqubbile min ehadihimâ ve lem yutaqabbel mine'l-âxar qâle le-aqtulenneke qâle innemâ yetaqabbelu'llâhu mine'l-muttaqîn' — "
 "'ve' + IMPV 2MS I. bab + ''alâ' + 3MP + 'nebe'' + ikil 'ibn' + özel ad 'âdem' + 'bi' + belirli 'haqq' + 'iz' + PERF 3MD II. bab + nekre 'qurbân' + 'fe' + edilgen PERF 3MS V. bab + 'min' + 'ehad' + 3D + 've' + 'lem' + edilgen IMPF 3MS V. bab + 'min' + belirli 'âxar' + PERF 3MS I. bab + 'le' + IMPF 1S I. bab + 'nûn' + 2MS + PERF 3MS I. bab + 'inne' + 'mâ' + IMPF 3MS V. bab + lafız + 'min' + belirli çoğul etken ortaç 'muttaqî' "
 "(ölçüm edim emir, kip EMPH 2 · IMPV 1 · NEG 1; 1S 1 · 2MS 2 · 3D 1 · 3MD 2 · 3MP 1 · 3MS 5; bab I. bab ×4 · II. bab ×1 · V. bab ×3). "
 "Allah lafzı 22. sırada (ölçüm allah z=0,31); Rab yok; ölçüm esmâ '{{1|أَحَد 12\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor) — 'min ehadihimâ', kural 'esmâ adı esmâ dışı göndergeyle → degil' (iki oğuldan biri) (okuma); "
 "ölçüm '{{1|aktör: adlı آدَم 5\\. sırada \\(kisi, rol mecrur\\)}}' — satır aynen. "
 "Ölçüm '{{1|yıldız yok}}' — satır aynen; n=24 (n z=1,23); ölçüm '{{1|EDİLGEN 2/8 fiil, pas z=1,10}}' — satır aynen; ölçüm '{{1|mm2: \\[8, قرب}}' — satır aynen; ölçüm '{{1|sayı işareti أَحَد}}' — satır aynen; ölçüm '{{1|fâsıla ٱلمتقين → ن, N sınıfı}}' — satır aynen; "
 "ölçüm '{{1|simetri \\[3, 10, 14, 1\\]}}' — satır aynen; ölçüm '{{1|harf 104 → harf3 101, isaret 3}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen; ölçüm '{{1|bağ: YOK \\(esit2, nakarat3, xref üçü de boş\\)}}' — satır aynen. "
 "Ölçüm EMPH 2: 'le' ve 'nne' (18. kelime); IMPV 1: 'tlu' (1. kelime); NEG 1: 'lem' (13. kelime) (okuma); ölçüm EDİLGEN — 'tuqubbile' (10. kelime) ve 'yutaqabbel' (14. kelime), morph PASS (okuma); 'iz' (7. kelime) morph T — zaman (okuma). "
 "Kök ikilemeleri (ölçüm) قبل ×3: 'tuqubbile' (10. kelime) / 'yutaqabbel' (14. kelime) / 'yetaqabbelu' (21. kelime); قرب ×2: 'qarrabâ' (8. kelime) / 'qurbânen' (9. kelime); قول ×2: 'qâle' (17. ve 19. kelime) (okuma). "
 "'ve'tlu' (1.)'daki 've' morph CONJ; 'fe-tuqubbile' (10.)'deki 'fe' CONJ; 've lem' (13.)'deki 've' CONJ (okuma). "
 + T27 + " (okuma). "
 + cumle(say('say 5:27 1-3 --on', "ve'tlu 'aleyhim nebe'", True), say('say 5:27 2-3', "'aleyhim nebe'"), say('say 5:27 3-5', "nebe'e'bney âdem"), say('say 5:27 4-5', "bney âdem"), say('say 5:27 3-6', "nebe'e'bney âdeme bi'l-haqq")) + ' '
 + cumle(say('say 5:27 7-9', "iz qarrabâ qurbânen", True), say('lem 5:27:9', "qurbân"), say('say 5:27 10-12 --on', "fe-tuqubbile min ehadihimâ"), say('lem 5:27:10', "teqabbele"), say('say 5:27 13-16 --on', "ve lem yutaqabbel mine'l-âxar"), say('say 5:27 15-16', "mine'l-âxar")) + ' '
 + cumle(say('say 5:27 17-18', "qâle le-aqtulenneke", True), say('say 5:27 20-24', "innemâ yetaqabbelu'llâhu mine'l-muttaqîn"), say('say 5:27 21-24', "yetaqabbelu'llâhu mine'l-muttaqîn"), say('say 5:27 23-24', "mine'l-muttaqîn")) + ' '
 "Ölçüm xref yok. Ölçüm nakarat3 kalıbı yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'fe-tuqubbile min ehadihimâ' / 've lem yutaqabbel mine'l-âxar'; 'le-aqtulenneke' / 'innemâ yetaqabbelu'llâhu mine'l-muttaqîn' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + IMPV + ''alâ' + izafet + izafet + özel ad + 'bi' + belirli + 'iz' + PERF + nekre + 'fe' + PERF + 'min' + izafet + 've' + 'lem' + IMPF + 'min' + belirli + PERF + 'le' + IMPF + PERF + 'inne' + 'mâ' + IMPF + lafız + 'min' + belirli; "
 "D2 emir, EMPH ('le' ve 'nne' 18. kelime), IMPV ('tlu' 1. kelime), NEG ('lem' 13. kelime); D3 قبل ×3 · قرب ×2 · قول ×2; 3:183 ve 10:71 eşleri; D4 1S 1 · 2MS 2 · 3D 1 · 3MD 2 · 3MP 1 · 3MS 5, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T27 + "; A2 haber okuma; kurban; kabul; kabul edilmeme; öldürme tehdidi; takvâ; A3 'le-aqtulenneke' (söz içi, 18-18. kelime); 'innemâ yetaqabbelu'llâhu' ile açılan söz (20-24. kelime; 5:29 sonuna dek); "
 "A4 " + BOLUM + "; bölüm açılışı; edim geçişi haber → emir (ayetler arası); şahıs geçişi yok; söz açılır (18. kelime); söz kapanır (18. kelime, ayet içi); söz açılır (20. kelime).",
)

D[28] = ("◇ 'le-in besatte ileyye yedeke li-taqtulenî mâ ene bi-bâsitin yediye ileyke li-aqtuleke innî exâfu'llâhe rabbe'l-'âlemîn' — "
 "'le' + 'in' + PERF 2MS I. bab + 'ilâ' + 1S + 'yed' + 2MS + 'li' + IMPF 2MS I. bab + 1S + 'mâ' + 'ene' + 'bi' + nekre etken ortaç 'bâsit' + 'yed' + 1S + 'ilâ' + 2MS + 'li' + IMPF 1S I. bab + 2MS + 'inne' + 1S + IMPF 1S I. bab + lafız + 'rabb' + belirli çoğul ''âlem' "
 "(ölçüm edim şart, kip COND 1 · EMPH 1 · NEG 1; 1S 7 · 2MS 6; bab I. bab ×4). "
 "Allah lafzı 14. sırada (ölçüm allah z=0,72); ölçüm '{{2|رَبّ 15\\. sırada \\(rab z=1,01\\)}}' — satır aynen; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor; sınıf AR/AR). "
 "Ölçüm '{{2|yıldız yok}}' — satır aynen; n=16 (n z=0,38); ölçüm '{{2|fâsıla ٱلعلمين → ن, N sınıfı}}' — satır aynen; ölçüm '{{2|simetri \\[3, 1, 10, 1\\]}}' — satır aynen; ölçüm '{{2|harf 67 → harf3 63, isaret 4}}' — satır aynen; ölçüm '{{2|dış düğüm 1}}' — satır aynen. "
 "Ölçüm COND 1: 'in' (1. kelime); EMPH 1: 'le' (1. kelime); NEG 1: 'mâ' (6. kelime) (okuma); 'li' (5. ve 11. kelime) morph PRP — amaç (okuma). "
 "Kök ikilemeleri (ölçüm) بسط ×2: 'besatte' (2. kelime) / 'bi-bâsitin' (8. kelime); قتل ×2: 'li-taqtulenî' (5. kelime) / 'li-aqtuleke' (11. kelime); يدي ×2: 'yedeke' (4. kelime) / 'yediye' (9. kelime) (okuma). "
 "5:28'de 've' / 'fe' yok (okuma). "
 + T28 + " (okuma). "
 + cumle(say('say 5:28 1-5 --on', "le-in besatte ileyye yedeke li-taqtulenî", True), say('say 5:28 2-4', "besatte ileyye yedeke"), say('say 5:28 6-11', "mâ ene bi-bâsitin yediye ileyke li-aqtuleke"), say('say 5:28 6-8', "mâ ene bi-bâsit")) + ' '
 + cumle(say('say 5:28 12-16', "innî exâfu'llâhe rabbe'l-'âlemîn", True), say('say 5:28 13-16', "exâfu'llâhe rabbe'l-'âlemîn"), say('say 5:28 15-16', "rabbe'l-'âlemîn")) + ' '
 "Ölçüm xref 59:16 (basılmış). Ölçüm nakarat3 kalıbı yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'le-in besatte ileyye yedeke li-taqtulenî' / 'mâ ene bi-bâsitin yediye ileyke li-aqtuleke' — ayetler arası: 5:27 / 5:28 ('le-aqtulenneke' / 'mâ ene bi-bâsitin yediye ileyke li-aqtuleke').",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 'yedeke' (4. kelime), 'yediye' (9. kelime); B4 —.",
 "◈D — D1 'le' + 'in' + PERF + 'ilâ' + izafet + 'li' + IMPF + 'mâ' + 'ene' + 'bi' + nekre + izafet + 'ilâ' + 'li' + IMPF + 'inne' + IMPF + lafız + izafet + belirli; "
 "D2 şart, COND ('in' 1. kelime), EMPH ('le' 1. kelime), NEG ('mâ' 6. kelime); D3 بسط ×2 · قتل ×2 · يدي ×2; 59:16 eşi; D4 1S 7 · 2MS 6, sahset ['1', '2'], iltifât 0.",
 "◈A — A1 " + T28 + "; aktör yok (ölçüm); A2 el uzatma; öldürme; korku; âlemlerin Rabbi; A3 söz sürüyor (1-16. kelime); A4 " + BOLUM + "; edim geçişi emir → şart (ayetler arası); şahıs geçişi 3 → 1 (ayetler arası); "
 "şart → cevap (ayet içi; COND 'in' 1. kelime: 'le-in besatte ileyye yedeke' / 'mâ ene bi-bâsitin' (6. kelime)).",
)

D[29] = ("◇ 'innî urîdu en tebû'e bi-ismî ve ismike fe-tekûne min ashâbi'n-nâr ve zâlike cezâ'u'z-zâlimîn' — "
 "'inne' + 1S + IMPF 1S IV. bab + 'en' + IMPF 2MS I. bab + 'bi' + 'ism' + 1S + 've' + 'ism' + 2MS + 'fe' + IMPF 2MS I. bab + 'min' + çoğul 'ashâb' + belirli 'nâr' + 've' + 'zâ' + 'cezâ'' + belirli çoğul etken ortaç 'zâlim' "
 "(ölçüm edim haber, kip yok; 1S 3 · 2MS 3; bab I. bab ×2 · IV. bab ×1). "
 "Ölçüm '{{3|lafız YOK · Rab YOK}}' — satır aynen; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{3|yıldız yok}}' — satır aynen; n=13 (n z=0,06); ölçüm '{{3|fâsıla ٱلظلمين → ن, N sınıfı}}' — satır aynen; ölçüm '{{3|harf 56 → harf3 54, isaret 2}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen; ölçüm '{{3|bağ: YOK \\(esit2, nakarat3, xref üçü de boş\\)}}' — satır aynen. "
 "'en' (3. kelime) morph SUB — masdar (okuma). "
 "Kök ikilemeleri (ölçüm) أثم ×2: 'bi-ismî' (5. kelime) / 've ismike' (6. kelime) (okuma). "
 "'ve ismike' (6.)'deki 've' morph CONJ; 'fe-tekûne' (7.)'deki 'fe' CONJ; 've zâlike' (11.)'deki 've' REM (okuma). "
 + T29 + " (okuma). "
 + cumle(say('say 5:29 1-4', "innî urîdu en tebû'", True), say('say 5:29 1-2', "innî urîd"), say('say 5:29 4-6', "tebû'e bi-ismî ve ismik")) + ' '
 + cumle(say('say 5:29 7-10 --on', "fe-tekûne min ashâbi'n-nâr", True), say('say 5:29 8-10', "min ashâbi'n-nâr"), say('say 5:29 11-13 --on', "ve zâlike cezâ'u'z-zâlimîn"), say('say 5:29 12-13', "cezâ'u'z-zâlimîn")) + ' '
 "Ölçüm xref yok. Ölçüm nakarat3 kalıbı yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'bi-ismî' / 've ismike' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'inne' + IMPF + 'en' + IMPF + 'bi' + izafet + 've' + izafet + 'fe' + IMPF + 'min' + izafet + belirli + 've' + 'zâ' + izafet + belirli; "
 "D2 haber; D3 أثم ×2; 28:27 ve 59:17 eşleri; D4 1S 3 · 2MS 3, sahset ['1', '2'], iltifât 0.",
 "◈A — A1 " + T29 + "; aktör yok (ölçüm); A2 isteme; günah yüklenme; ateş halkı; zalimlerin cezası; A3 söz sürüyor (1-13. kelime); A4 " + BOLUM + "; edim geçişi şart → haber (ayetler arası); şahıs geçişi yok; söz kapanır (13. kelime).",
)

D[30] = ("◇ 'fe-tavva'at lehû nefsuhû qatle exîhi fe-qatelehû fe-asbaha mine'l-xâsirîn' — "
 "'fe' + PERF 3FS II. bab + 'li' + 3MS + 'nefs' + 3MS + masdar 'qatl' + 'ex' + 3MS + 'fe' + PERF 3MS I. bab + 3MS + 'fe' + PERF 3MS IV. bab + 'min' + belirli çoğul etken ortaç 'xâsir' "
 "(ölçüm edim haber, kip yok; 3FS 1 · 3MS 6; bab I. bab ×1 · II. bab ×1 · IV. bab ×1). "
 "Ölçüm '{{4|lafız YOK · Rab YOK}}' — satır aynen; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{4|yıldız yok}}' — satır aynen; n=9 (n z=-0,36); ölçüm '{{4|iltifât 1}}' — satır aynen; ölçüm '{{4|fâsıla ٱلخسرين → ن, N sınıfı}}' — satır aynen; ölçüm '{{4|harf 40 → harf3 37, isaret 3}}' — satır aynen; ölçüm '{{4|dış düğüm 0}}' — satır aynen; ölçüm '{{4|bağ: YOK \\(esit2, nakarat3, xref üçü de boş\\)}}' — satır aynen. "
 "Ölçüm iltifât 1 — 'tavva'at' (3FS, 'nefs' faili) ile 3MS fiiller arası; söz 1S / 2MS'den anlatı 3. şahsa dönüş ayetler arası (okuma; aday kayıt). "
 "Kök ikilemeleri (ölçüm) قتل ×2: 'qatle' (4. kelime) / 'fe-qatelehû' (6. kelime) (okuma). "
 "'fe-tavva'at' (1.)'deki 'fe' morph REM; 'fe-qatelehû' (6.)'daki 'fe' CAUS; 'fe-asbaha' (7.)'daki 'fe' CONJ (okuma). "
 + T30 + " (okuma). "
 + cumle(say('say 5:30 1-4 --on', "fe-tavva'at lehû nefsuhû qatl", True), say('say 5:30 4-5', "qatle exîh"), say('lem 5:30:1', "tavva'at")) + ' '
 + cumle(say('say 5:30 7-9 --on', "fe-asbaha mine'l-xâsirîn", True), say('say 5:30 8-9', "mine'l-xâsirîn")) + ' '
 "Ölçüm xref yok. Ölçüm nakarat3 kalıbı yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: 5:28 / 5:30 ('mâ ene bi-bâsitin' / 'fe-qatelehû').",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'fe' + PERF + 'li' + izafet + masdar + izafet + 'fe' + PERF + 'fe' + PERF + 'min' + belirli; "
 "D2 haber; D3 قتل ×2; eş yok; D4 3FS 1 · 3MS 6, sahset ['3'], iltifât 1.",
 "◈A — A1 " + T30 + "; aktör yok (ölçüm); A2 nefsin kolaylaştırması; kardeş öldürme; hüsran; A3 —; A4 " + BOLUM + "; edim geçişi yok; şahıs geçişi 1 → 3 (ayetler arası).",
)

out = ['# ── blok 5:27-30 (2026-11-15) ──', 'MEAL10 = {']
for n in range(27, 31):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M10 = {']
for n in range(27, 31):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL10); M.update(M10)']
open('/home/claude/yamalar/metin_5_27_30.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

# sûre 6 blok 24 (6:100-103) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b24/say2.txt'
os.environ['OLC'] = '/home/claude/b24/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Taneyi ve çekirdeği yaran; gözler O'nu idrak etmez' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 100: "Cinleri Allah'a ortaklar kıldılar; oysa onları O yarattı. Bilgisizce O'na oğullar ve kızlar uydurdular. O münezzehtir; nitelendirdiklerinden yücedir.",
 101: "O, göklerin ve yerin eşsiz yaratıcısıdır. Bir eşi olmamışken O'nun nasıl çocuğu olur? Her şeyi O yarattı; O her şeyi bilendir.",
 102: "İşte Rabbiniz Allah budur; O'ndan başka ilah yoktur; her şeyin yaratıcısıdır; o hâlde O'na kulluk edin. O her şey üzerine vekîldir.",
 103: "Gözler O'nu idrak etmez; O ise gözleri idrak eder. O, latîftir, haberdardır.",
}

T = {}
T[100] = ("'ve ce'alû', 've xaraqû', 'yesifûn' 3MP (adsız; tartışmalı — 1., 6. ve 15. kelime); 've xalaqahum' 3MP eki (adsız; tartışmalı; gönderge 'l-cinne' 4. kelime, 5. kelime); "
          "'ve xalaqahum', 'lehû', 'subhânehû', 've te'âlâ' 3MS (adsız; gönderge lafız 2. kelime — 5., 7., 12. ve 13. kelime)")
T[101] = ("'yekûnu' 3MS (fiil uyumu; 5. kelime — fail 7. kelime); 'tekun' 3FS (fiil uyumu; 9. kelime — fail 11. kelime); "
          "'lehû' 3MS (adsız; gönderge 6:100 2. kelime, 6. kelime); 'lehû' 3MS (adsız; gönderge 6:100 2. kelime, 10. kelime); 've xalaqa', 've huve' 3MS (adsız; gönderge 6:100 2. kelime — 12. ve 15. kelime)")
T[102] = ("muhatap 2MP (adsız; 'rabbukum', 'fa'budûhu' — 3. ve 11. kelime); 'huve', 've huve' 3MS (adsız; gönderge lafız 2. kelime — 7. ve 12. kelime); 'fa'budûhu' 3MS eki (adsız; gönderge lafız 2. kelime, 11. kelime)")
T[103] = ("'tudrikuhu' 3FS (fiil uyumu; 2. kelime — fail 3. kelime); 'tudrikuhu' 3MS eki (adsız; gönderge 6:102 2. kelime, 2. kelime); 've huve', 'yudriku' 3MS (adsız; gönderge 6:102 2. kelime — 4. ve 5. kelime); 've huve' 3MS (adsız; gönderge 6:102 2. kelime, 7. kelime)")

D = {}
D[100] = ("◇ 've ce'alû li'llâhi şurakâ'e'l-cinne ve xalaqahum ve xaraqû lehû benîne ve benâtin bi-ğayri 'ilmin subhânehû ve te'âlâ 'ammâ yesifûn' — "
 "'ve' + PERF 3MP I. bab + 3MP + 'li' + lafız + çoğul 'şerîk' + belirli 'cinn' + 've' + PERF 3MS I. bab + 3MP + 've' + PERF 3MP I. bab + 3MP + 'li' + 3MS + çoğul 'bunayy' + 've' + nekre çoğul 'bint' + "
 "'bi' + 'ğayr' + nekre ''ilm' + mastar 'subhân' + 3MS + 've' + PERF 3MS VI. bab + ''an' + 'mâ' + IMPF 3MP I. bab + 3MP "
 "(ölçüm edim haber, kip yok; 3MP 7 · 3MS 4; bab I. bab ×4 · VI. bab ×1). "
 "Allah lafzı 2. sırada (ölçüm allah z=0,81); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=15 (n z=0,27); ölçüm '{{1|fâsıla يصفون → ن, N sınıfı}}' — satır aynen (6:99 ن → 6:100 ن); "
 "ölçüm '{{1|harf 73 → harf3 65, isaret 8}}' — satır aynen; ölçüm '{{1|dış düğüm 2}}' — satır aynen. "
 "Ölçüm kip yok; 've ce'alû' (1.), 've xaraqû' (6.), 've benâtin' (9.) ve 've te'âlâ' (13.) kelimelerindeki 've' CONJ; 've xalaqahum' (5.) kelimesindeki 've' CIRC (okuma). "
 "Kök ikilemesi (ölçüm) بني ×2 ('benîne' 8. / 've benâtin' 9. kelime) (okuma). "
 + T[100] + " (okuma). "
 + cumle(say('say 6:100 1-3', "ve ce'alû li'llâhi şurakâ'e", True), say('dizi 6 100 1 3', "ce'ale allâh şerîk")) + ' ' +
 "Ölçüm xref okunmuş 2 ayet. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'benîne' / 've benâtin' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 'xalaqahum' (5. kelime); B3 —; B4 —.",
 "◈D — D1 've' + PERF + 'li' + lafız + 'şerîk' + belirli + 've' + PERF + 've' + PERF + 'li' + 'bunayy' + 've' + nekre + 'bi' + 'ğayr' + nekre + izafet + 've' + PERF + ''an' + 'mâ' + IMPF; "
 "D2 haber; D3 بني ×2; D4 3MP 7 · 3MS 4, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[100] + "; aktör yok (ölçüm); A2 cinlerin Allah'a ortak kılınması; O'na bilgisizce oğullar ve kızlar uydurulması; O'nun nitelendirilenlerden münezzeh ve yüce oluşu; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi emir → haber (ayetler arası).",
)

D[101] = ("◇ 'bedî'u's-semâvâti ve'l-ardi ennâ yekûnu lehû veledun ve lem tekun lehû sâhibetun ve xalaqa kulle şey'in ve huve bi-kulli şey'in 'alîm' — "
 "'bedî'' + belirli çoğul 'semâ'' + 've' + belirli 'ard' + 'ennâ' + IMPF 3MS I. bab + 'li' + 3MS + nekre 'veled' + 've' + 'lem' + IMPF 3FS I. bab + 'li' + 3MS + nekre 'sâhibe' + "
 "'ve' + PERF 3MS I. bab + 'kull' + nekre 'şey'' + 've' + 'huve' + 'bi' + 'kull' + nekre 'şey'' + nekre ''alîm' "
 "(ölçüm edim soru, kip INTG 1 · NEG 1; 3FS 1 · 3MS 5; bab I. bab ×3). "
 "Allah lafzı yok; Rab yok; ölçüm '{{2|esmâ بَدِيع 1\\. sırada, ORTA konum, MÜHÜRSÜZ \\| عَلِيم 18\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton denge' — ölçüm MÜHÜRSÜZ ile uyuşmuyor, araç tanımı farkı (tam okuma sonu); "
 "esma_el kaydı 'ilahi' — 'bedî'u's-semâvâti ve'l-ard' ve 've huve bi-kulli şey'in 'alîm', kural 'zamirin haberi → ilahi' (Allah) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=18 (n z=0,59); ölçüm '{{2|fâsıla عليم → م, N sınıfı}}' — satır aynen (6:100 ن → 6:101 م); "
 "ölçüm '{{2|simetri \\[4, 4, 8, 1\\]}}' — satır aynen; ölçüm '{{2|harf 71 → harf3 62, isaret 9}}' — satır aynen; ölçüm '{{2|dış düğüm 6}}' — satır aynen. "
 "Ölçüm INTG 1: 'ennâ' (4. kelime); NEG 1: 've lem' (8. kelime); 've'l-ardi' (3.) ve 've lem' (8.) kelimelerindeki 've' CONJ; 've xalaqa' (12.) ve 've huve' (15.) kelimelerindeki 've' REM (okuma). "
 "Kök ikilemesi (ölçüm) شيأ ×2 ('şey'in' 14. / 'şey'in' 17. kelime), كلل ×2 ('kulle' 13. / 'bi-kulli' 16. kelime), كون ×2 ('yekûnu' 5. / 'tekun' 9. kelime) (okuma). "
 + T[101] + " (okuma). "
 + cumle(say('say 6:101 1-3', "bedî'u's-semâvâti ve'l-ard", True), say('dizi 6 101 1 3', "bedî' semâ' ard")) + ' ' +
 "Ölçüm xref 2:117 ve 39:62 (emsal olarak basıldı) ve okunmuş 4 ayet. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 's-semâvâti' / 've'l-ardi' — ayetler arası: yok.",
 "◈K — K1 's-semâvâti' (2. kelime), 'l-ardi' (3. kelime).",
 "◈B — B1 —; B2 'xalaqa' (12. kelime); B3 —; B4 —.",
 "◈D — D1 'bedî'' + belirli + 've' + belirli + 'ennâ' + IMPF + 'li' + nekre + 've' + 'lem' + IMPF + 'li' + nekre + 've' + PERF + 'kull' + nekre + 've' + 'huve' + 'bi' + 'kull' + nekre + nekre; "
 "D2 soru; INTG ('ennâ' 4. kelime), NEG ('ve lem' 8. kelime); D3 شيأ ×2, كلل ×2, كون ×2; 2:117 eşi; D4 3FS 1 · 3MS 5, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[101] + "; aktör yok (ölçüm); A2 göklerin ve yerin eşsiz yaratıcısı; eşi olmayanın çocuğu olmayacağı sorusu; her şeyi yaratma ve her şeyi bilme; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi haber → soru (ayetler arası).",
)

D[102] = ("◇ 'zâlikumu'llâhu rabbukum lâ ilâhe illâ huve xâliqu kulli şey'in fa'budûhu ve huve 'alâ kulli şey'in vekîl' — "
 "'zâlikum' + lafız + 'rabb' + 2MP + 'lâ' + 'ilâh' + 'illâ' + 'huve' + etken ortaç 'xâliq' + 'kull' + nekre 'şey'' + 'fe' + IMPV 2MP I. bab + 2MP + 3MS + 've' + 'huve' + ''alâ' + 'kull' + nekre 'şey'' + nekre 'vekîl' "
 "(ölçüm edim emir, kip IMPV 1 · NEG 1, biçim ISTISNA; 2MP 3 · 3MS 3; bab I. bab ×1). "
 "Allah lafzı 2. sırada (ölçüm allah z=0,72); Rab 3. sırada (ölçüm rab z=1,01); ölçüm '{{3|esmâ خالِق 8\\. sırada, ORTA konum, MÜHÜRSÜZ \\| وَكِيل 16\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton cemâl' — ölçüm MÜHÜRSÜZ ile uyuşmuyor, araç tanımı farkı (tam okuma sonu); "
 "esma_el kaydı 'ilahi' — 'zâlikumu'llâhu rabbukum lâ ilâhe illâ huve xâliqu kulli şey'in', kural 'lafzın haberi → ilahi' (Allah); 've huve 'alâ kulli şey'in vekîl', kural 'zamirin haberi → ilahi' (Allah) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=16 (n z=0,38); ölçüm '{{3|fâsıla وكيل → ل, ل sınıfı}}' — satır aynen (6:101 م → 6:102 ل); "
 "ölçüm '{{3|simetri \\[4, 7, 12, 1\\]}}' — satır aynen; ölçüm '{{3|harf 58 → harf3 52, isaret 6}}' — satır aynen; ölçüm '{{3|dış düğüm 2}}' — satır aynen. "
 "Ölçüm IMPV 1: 'fa'budûhu' (11. kelime); NEG 1: 'lâ' (4. kelime); biçim ISTISNA ('illâ' 6. kelime); 'fa'budûhu' (11.) kelimesindeki 'fe' REM; 've huve' (12.) kelimesindeki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 ('llâhu' 2. / 'ilâhe' 5. kelime), شيأ ×2 ('şey'in' 10. / 'şey'in' 15. kelime), كلل ×2 ('kulli' 9. / 'kulli' 14. kelime) (okuma). "
 + T[102] + " (okuma). "
 + cumle(say('say 6:102 8-10', "xâliqu kulli şey'in", True), say('dizi 6 102 8 10', "xâliq kull şey'")) + ' ' + cumle(say('say 6:102 12-16', "ve huve 'alâ kulli şey'in vekîl", True), say('dizi 6 102 12 16', "_ 'alâ kull şey' vekîl")) + ' ' + cumle(say('say 6:102 3-7', "rabbukum lâ ilâhe illâ huve", True), say('dizi 6 102 3 7', "rabb lâ ilâh illâ _")) + ' ' + cumle(say('say 6:102 13-15', "'alâ kulli şey'in", True), say('dizi 6 102 13 15', "'alâ kull şey'")) + ' ' +
 cumle(say('say 6:102 4-6', "lâ ilâhe illâ", True)) + " (--medde 36 ayet: 'lâ ilâhe illâ' yazım farkı ile; harekesiz sayım elif / medde yazımına bağlı). " + "Ölçüm xref 39:62 (emsal olarak basıldı) ve okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıpları: 'rabb lâ ilâh illâ _' süzgeç GEÇER, ''alâ kull şey'' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 'xâliqu' (8. kelime); B3 —; B4 —.",
 "◈D — D1 'zâlikum' + lafız + izafet + 'lâ' + 'ilâh' + 'illâ' + 'huve' + 'xâliq' + 'kull' + nekre + 'fe' + IMPV + 've' + 'huve' + ''alâ' + 'kull' + nekre + nekre; "
 "D2 emir; IMPV ('fa'budûhu' 11. kelime), NEG ('lâ' 4. kelime); D3 أله ×2, شيأ ×2, كلل ×2; 39:62 eşi; D4 2MP 3 · 3MS 3, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[102] + "; aktör yok (ölçüm); A2 'İşte Rabbiniz Allah budur' bildirimi; O'ndan başka ilah olmaması; her şeyin yaratıcısına kulluk emri; her şey üzerine vekîl oluş; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 3 → 2 (ayetler arası); şahıs sayısında beraberlik (2. şahıs 3 · 3. şahıs 3 — ölçüm baskın 2); edim geçişi soru → emir (ayetler arası).",
)

D[103] = ("◇ 'lâ tudrikuhu'l-ebsâru ve huve yudriku'l-ebsâra ve huve'l-latîfu'l-xabîr' — "
 "'lâ' + IMPF 3FS IV. bab + 3MS + belirli çoğul 'basar' + 've' + 'huve' + IMPF 3MS IV. bab + belirli çoğul 'basar' + 've' + 'huve' + belirli 'latîf' + belirli 'xabîr' "
 "(ölçüm edim haber, kip NEG 1; 3FS 1 · 3MS 4; bab IV. bab ×2). "
 "Allah lafzı yok; Rab yok; ölçüm '{{4|esmâ لَطِيف 8\\. sırada, SON konum, MÜHÜR \\| خَبِير 9\\. sırada, SON konum, MÜHÜR}}' — satır aynen; esma_kayit çıktısı 'mühür EVET (ÇİFT)' (uyuşuyor); "
 "esma_el kaydı 'ilahi' — 've huve'l-latîfu'l-xabîr', kural 'zamirin haberi → ilahi' (Allah) ve 'l-xabîr' için kural 'zamirin haberi → ilahi' (Allah; 'l-latîf'in sıfatı) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=9 (n z=-0,36); ölçüm '{{4|fâsıla ٱلخبير → ر, R sınıfı}}' — satır aynen (6:102 ل → 6:103 ر); "
 "ölçüm '{{4|simetri \\[3, 3, 6, 1\\]}}' — satır aynen; ölçüm '{{4|harf 42 → harf3 41, isaret 1}}' — satır aynen; ölçüm '{{4|dış düğüm 0}}' — satır aynen. "
 "Ölçüm NEG 1: 'lâ' (1. kelime); 've huve' (4. ve 7.) kelimelerindeki 've' REM (okuma). "
 "Kök ikilemesi (ölçüm) بصر ×2 ('l-ebsâru' 3. / 'l-ebsâra' 6. kelime), درك ×2 ('tudrikuhu' 2. / 'yudriku' 5. kelime) (okuma). "
 + T[103] + " (okuma). "
 +
 "Ölçüm xref yok; ölçüm bağ yok (esit2, nakarat3, xref üçü de boş). "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'lâ tudrikuhu'l-ebsâru' / 'yudriku'l-ebsâra' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 'l-ebsâru' (3. kelime), 'l-ebsâra' (6. kelime); B4 —.",
 "◈D — D1 'lâ' + IMPF + belirli + 've' + 'huve' + IMPF + belirli + 've' + 'huve' + belirli + belirli; "
 "D2 haber; NEG ('lâ' 1. kelime); D3 بصر ×2, درك ×2; D4 3FS 1 · 3MS 4, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[103] + "; aktör yok (ölçüm); A2 gözlerin O'nu idrak etmemesi; O'nun gözleri idrak etmesi; latîf ve haberdar oluş; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 2 → 3 (ayetler arası); edim geçişi emir → haber (ayetler arası); bölüm kapanışı.",
)
out = ['# ── blok 6:100-103 (2026-11-22) ──', 'MEAL24 = {']
for n in range(100, 104):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M24 = {']
for n in range(100, 104):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL24); M.update(M24)']
open('/home/claude/yamalar/metin_6_100_103.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

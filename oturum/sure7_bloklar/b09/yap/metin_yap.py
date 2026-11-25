# sûre 7 blok 9 (7:31-34) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os, re
os.environ['SAY2'] = '/home/claude/b09/say2.txt'
os.environ['OLC'] = '/home/claude/b09/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Ey Âdemoğulları: giysi, fitne, ziynet; haram kılınanlar' bölümünde"
_OL = [l.replace('**', '') for l in open(os.environ['OLC'], encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK1 = _esc(re.search(r'aktör: adlı .*?rol mecrur\)', _OL[0]).group(0))


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 31: "Ey Âdemoğulları, her mescidin yanında ziynetinizi alın; yiyin, için ve israf etmeyin. Gerçekten O israf edenleri sevmez.",
 32: "De ki: Allah'ın kulları için çıkardığı ziynetini ve rızıktan temiz şeyleri kim haram kıldı? De ki: Onlar dünya hayatında iman edenler içindir; kıyamet gününde hâlis olarak. Bilen bir kavim için âyetleri böyle ayrıntılı açıklıyoruz.",
 33: "De ki: Rabbim ancak hayâsızlıkları haram kıldı; onlardan açık olanı da gizli olanı da, günahı, haksız yere azgınlığı, hakkında hiçbir delil indirmediği şeyi Allah'a ortak koşmanızı ve Allah hakkında bilmediğiniz şeyi söylemenizi.",
 34: "Her ümmetin bir eceli vardır; ecelleri geldiğinde ne bir saat geri kalırlar ne de öne geçerler.",
}

T = {}
T[31] = ("muhatap 2MP (adsız; 'xuzû', 've kulû', 've'şrabû', 'tusrifû' — 3., 8., 9. ve 11. kelime); muhatap 2MP eki (adsız; 'zînetekum' — 4. kelime); 'innehû' 3MS eki (adsız; gönderge 7:30 13. kelime, 12. kelime); 'yuhibbu' 3MS (adsız; gönderge 7:30 13. kelime, 14. kelime)")
T[32] = ("muhatap 2MS (adsız; 'qul', 'qul' — 1. ve 12. kelime); 'harrame' 3MS (adsız; söz içi; gönderge 'men' 2. kelime, 3. kelime); 'axrace' 3MS (adsız; söz içi; gönderge 'llâhi' 5. kelime, 7. kelime); 'li-'ibâdihî' 3MS eki (adsız; söz içi; tartışmalı; gönderge 'llâhi' 5. kelime, 8. kelime); "
         "'hiye' 3FS (adsız; söz içi; gönderge 'zînete' 4. kelime, 13. kelime); 'âmenû' 3MP (adsız; söz içi; gönderge 'lillezîne' 14. kelime, 15. kelime); konuşan 1P (adsız; 'nufassilu' — 23. kelime); 'ya'lemûn' 3MP (adsız; gönderge 'li-qavmin' 25. kelime, 26. kelime)")
T[33] = ("muhatap 2MS (adsız; 'qul' — 1. kelime); 'harrame' 3MS (fiil uyumu; söz içi; 3. kelime — fail 4. kelime); konuşan 1S eki (adsız; söz içi; 'rabbiye' — 4. kelime); 'zahera' 3MS (adsız; söz içi; gönderge 'mâ' 6. kelime, 7. kelime); "
         "'minhâ' 3FS eki (adsız; söz içi; tartışmalı; gönderge 'l-fevâhişe' 5. kelime, 8. kelime); 'betane' 3MS (adsız; söz içi; gönderge 've mâ' 9. kelime, 10. kelime); muhatap 2MP (adsız; söz içi; 'tuşrikû', 'teqûlû', 'ta'lemûn' — 16., 24. ve 29. kelime); "
         "'yunezzil' 3MS (adsız; söz içi; gönderge 'bi'llâhi' 17. kelime, 20. kelime); 'bihî' 3MS eki (adsız; söz içi; gönderge 'mâ' 18. kelime, 21. kelime)")
T[34] = ("'câ'e' 3MS (fiil uyumu; 5. kelime — fail 6. kelime); 'eceluhum' 3MP eki (adsız; tartışmalı; cins ve sayı uyumsuz; gönderge 'ummetin' 2. kelime, 6. kelime); 'yeste'xirûne', 'yestaqdimûn' 3MP (adsız; tartışmalı; cins ve sayı uyumsuz; gönderge 'ummetin' 2. kelime — 8. ve 11. kelime)")

D = {}
D[31] = ("◇ 'yâ benî âdeme xuzû zînetekum 'inde kulli mescidin ve kulû ve'şrabû ve lâ tusrifû innehû lâ yuhibbu'l-musrifîn' — "
 "'yâ' + çoğul 'bunayy' + özel ad 'âdem' + IMPV 2MP I. bab + 'zîne' + 2MP + ''inde' + 'kull' + nekre 'mescid' + 've' + IMPV 2MP I. bab + 've' + IMPV 2MP I. bab + 've' + 'lâ' + IMPF 2MP IV. bab + 'inne' + 3MS + 'lâ' + IMPF 3MS IV. bab + belirli çoğul etken ortaç 'musrif' "
 "(ölçüm edim emir, yasak, nida, kip IMPV 3 · NEG 1 · PRO 1 · VOC 1; 2MP 9 · 3MS 2; bab I. bab ×3 · IV. bab ×2). "
 "Allah lafzı yok; Rab yok; esmâ yok (ölçüm); ölçüm '{{1|" + _AK1 + "}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=15 (n z=0,27); ölçüm '{{1|fâsıla " + _F[0] + " → ن, N sınıfı}}' — satır aynen (7:30 ن → 7:31 ن); "
 "ölçüm '{{1|harf 72 → harf3 64, isaret 8}}' — satır aynen; ölçüm '{{1|dış düğüm 1}}' — satır aynen. "
 "Ölçüm IMPV 3: 'xuzû' (3. kelime), 'kulû' (8. kelime), 'şrabû' (9. kelime); NEG 1: 'lâ' (13. kelime); PRO 1: 'lâ' (10. kelime); VOC 1: 'yâ' (1. kelime); ölçüm biçim NEHY; "
 "'ve kulû' (8.), 've'şrabû' (9.) ve 've lâ' (10.) kelimelerindeki 've' CONJ; 'innehû' (12.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) سرف ×2 ('tusrifû' 11. / 'l-musrifîn' 15. kelime) (okuma). "
 + T[31] + " (okuma). "
 + cumle(say('say 7:31 1-2', "yâ benî âdeme", True), say('dizi 7 31 1 2', "bunayy âdem")) + ' '
 + cumle(say('say 7:31 3-7', "xuzû zînetekum 'inde kulli mescidin", True), say('say 7:31 5-7', "'inde kulli mescidin"), say('dizi 7 31 5 7', "'inde kull mescid")) + ' '
 + cumle(say('say 7:31 10-11', "ve lâ tusrifû", True), say('say 7:31 12-15', "innehû lâ yuhibbu'l-musrifîn"), say('say 7:31 10-15', "ve lâ tusrifû innehû lâ yuhibbu'l-musrifîn"), say('say 7:31 12-14', "innehû lâ yuhibbu"), say('dizi 7 31 12 14', "inne lâ ahbeb")) + ' ' +
 "Ölçüm xref 6:141 (basılmış). "
 "Ölçüm nakarat3 kalıbı: ''inde kull mescid' süzgeç GEÇMEZ; 'inne lâ ahbeb' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'yâ' + izafet + özel ad + IMPV + izafet + ''inde' + 'kull' + nekre + 've' + IMPV + 've' + IMPV + 've' + 'lâ' + IMPF + 'inne' + 'lâ' + IMPF + belirli; "
 "D2 emir, yasak, nida; IMPV ('xuzû' 3. kelime, 'kulû' 8. kelime, 'şrabû' 9. kelime), NEG ('lâ' 13. kelime), PRO ('lâ' 10. kelime), VOC ('yâ' 1. kelime); D3 سرف ×2; D4 2MP 9 · 3MS 2, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[31] + "; aktör adlı 'âdeme' (2. kelime; ölçüm rol mecrur); A2 her mescidin yanında ziynet alma; yeme, içme ve israf etmeme emri; israf edenlerin sevilmediği; "
 "A3 —; "
 "A4 " + BOLUM + "; nidâ ('yâ benî âdeme' 1. kelime); şahıs geçişi 3 → 2 (ayetler arası); edim geçişi haber → emir, yasak, nida (ayetler arası).",
)

D[32] = ("◇ 'qul men harrame zînete'llâhi'lletî axrace li-'ibâdihî ve't-tayyibâti mine'r-rizqi qul hiye lillezîne âmenû fi'l-hayâti'd-dunyâ xâlisaten yevme'l-qiyâmeti kezâlike nufassilu'l-âyâti li-qavmin ya'lemûn' — "
 "IMPV 2MS I. bab + 'men' + PERF 3MS II. bab + 'zîne' + 'allâh' + 'ellezî' + PERF 3MS IV. bab + 'li' + çoğul ''abd' + 3MS + 've' + belirli çoğul 'tayyibe' + 'min' + belirli 'rizq' + IMPV 2MS I. bab + 'hiye' + 'li' + 'ellezî' + PERF 3MP IV. bab + 'fî' + belirli 'hayâ' + belirli sıfat 'dunyâ' + "
 "nekre etken ortaç 'xâlisa' + 'yevm' + belirli 'qiyâme' + 'ke' + 'zâ' + IMPF 1P II. bab + belirli çoğul 'âye' + 'li' + nekre 'qavm' + IMPF 3MP I. bab "
 "(ölçüm edim soru, emir, kip IMPV 2 · INTG 1; 1P 1 · 2MS 2 · 3FS 1 · 3MP 4 · 3MS 3; bab I. bab ×3 · II. bab ×2 · IV. bab ×2). "
 "Allah lafzı 5. sırada (ölçüm allah z=0,24); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=26 (n z=1,44); ölçüm '{{2|fâsıla " + _F[1] + " → ن, N sınıfı}}' — satır aynen (7:31 ن → 7:32 ن); "
 "ölçüm '{{2|simetri \\[3, 1, 12, 1\\]}}' — satır aynen; ölçüm '{{2|harf 116 → harf3 110, isaret 6}}' — satır aynen; ölçüm '{{2|dış düğüm 1}}' — satır aynen. "
 "Ölçüm IMPV 2: 'qul' (1. kelime), 'qul' (12. kelime); INTG 1: 'men' (2. kelime); "
 "'lletî' (6.) REL; 've't-tayyibâti' (9.) kelimesindeki 've' CONJ; 'lillezîne' (14.) P + REL; 'kezâlike' (22.) P + DEM + DIST + ADDR (okuma). "
 "Kök ikilemesi (ölçüm) قول ×2 ('qul' 1. / 'qul' 12. kelime); قوم ×2 ('l-qiyâmeti' 21. / 'li-qavmin' 25. kelime) (okuma). "
 + T[32] + " (okuma). "
 + cumle(say('say 7:32 2-11', "men harrame zînete'llâhi'lletî axrace li-'ibâdihî ve't-tayyibâti mine'r-rizqi", True)) + ' '
 + cumle(say('say 7:32 13-18', "hiye lillezîne âmenû fi'l-hayâti'd-dunyâ", True), say('say 7:32 15-18', "âmenû fi'l-hayâti'd-dunyâ"), say('dizi 7 32 14 18', "ellezî âmene fî hayâ dunyâ"), say('say 7:32 16-18', "fi'l-hayâti'd-dunyâ"), say('dizi 7 32 16 18', "fî hayâ dunyâ")) + ' '
 + cumle(say('say 7:32 19-21', "xâlisaten yevme'l-qiyâmeti", True), say('say 7:32 22-26', "kezâlike nufassilu'l-âyâti li-qavmin ya'lemûn")) + ' ' +
 "Ölçüm xref 40:51 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıbı: 'fî hayâ dunyâ' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'd-dunyâ' / 'l-qiyâmeti' — ayetler arası: yok.",
 "◈K — K2 'yevme' (20. kelime).",
 "◈B — B4 'l-hayâti' (17. kelime).",
 "◈D — D1 IMPV + 'men' + PERF + izafet + lafız + 'ellezî' + PERF + 'li' + izafet + 've' + belirli + 'min' + belirli + IMPV + 'hiye' + 'li' + 'ellezî' + PERF + 'fî' + belirli + belirli + nekre + izafet + belirli + 'ke' + 'zâ' + IMPF + belirli + 'li' + nekre + IMPF; "
 "D2 soru, emir; IMPV ('qul' 1. kelime, 'qul' 12. kelime), INTG ('men' 2. kelime); D3 40:51 eşi, قول ×2, قوم ×2; D4 1P 1 · 2MS 2 · 3FS 1 · 3MP 4 · 3MS 3, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[32] + "; aktör yok (ölçüm); A2 Allah'ın kulları için çıkardığı ziyneti ve temiz rızıkları kimin haram kıldığı sorusu; bunların dünya hayatında iman edenlere, kıyamet gününde hâlis olarak ait oluşu; bilen kavim için âyetlerin ayrıntılı açıklanışı; "
 "A3 'men harrame zînete'llâhi'lletî axrace li-'ibâdihî ve't-tayyibâti mine'r-rizqi' (söz içi, 2-11. kelime); 'hiye lillezîne âmenû fi'l-hayâti'd-dunyâ xâlisaten yevme'l-qiyâmeti' (söz içi, 13-21. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (11. kelime, ayet içi); söz açılır (13. kelime); söz kapanır (21. kelime, ayet içi); şahıs geçişi 2 → 3 (ayetler arası); edim geçişi emir, yasak, nida → soru, emir (ayetler arası).",
)

D[33] = ("◇ 'qul innemâ harrame rabbiye'l-fevâhişe mâ zahera minhâ ve mâ betane ve'l-isme ve'l-bağye bi-ğayri'l-haqqi ve en tuşrikû bi'llâhi mâ lem yunezzil bihî sultânen ve en teqûlû 'ale'llâhi mâ lâ ta'lemûn' — "
 "IMPV 2MS I. bab + 'inne' + 'mâ' + PERF 3MS II. bab + 'rabb' + 1S + belirli çoğul 'fâhişe' + 'mâ' + PERF 3MS I. bab + 'min' + 3FS + 've' + 'mâ' + PERF 3MS I. bab + 've' + belirli 'ism' + 've' + belirli 'bağy' + 'bi' + 'ğayr' + belirli 'haqq' + 've' + 'en' + IMPF 2MP IV. bab + 'bi' + 'allâh' + 'mâ' + 'lem' + IMPF 3MS II. bab + 'bi' + 3MS + nekre 'sultân' + "
 "'ve' + 'en' + IMPF 2MP I. bab + ''alâ' + 'allâh' + 'mâ' + 'lâ' + IMPF 2MP I. bab "
 "(ölçüm edim emir, kip IMPV 1 · NEG 2; 1S 1 · 2MP 6 · 2MS 1 · 3FS 1 · 3MS 5; bab I. bab ×5 · II. bab ×2 · IV. bab ×1). "
 "Allah lafzı 17. ve 26. sırada (ölçüm allah z=0,85); Rab 4. sırada (ölçüm rab z=0,41); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{3|yıldız ★}}' — satır aynen (kaynak n, z=1,76); n=29 (n z=1,76); ölçüm '{{3|fâsıla " + _F[2] + " → ن, N sınıfı}}' — satır aynen (7:32 ن → 7:33 ن); "
 "ölçüm '{{3|simetri \\[4, 6, 25, 1\\]}}' — satır aynen; ölçüm '{{3|harf 112 → harf3 108, isaret 4}}' — satır aynen; ölçüm '{{3|dış düğüm 4}}' — satır aynen. "
 "Ölçüm IMPV 1: 'qul' (1. kelime); NEG 2: 'lem' (19. kelime), 'lâ' (28. kelime); "
 "'innemâ' (2.) ACC + PREV; 'mâ' (6., 18. ve 27.) REL; 've mâ' (9.) CONJ + REL; 've'l-isme' (11.) ve 've'l-bağye' (12.) kelimelerindeki 've' CONJ; 've en' (15. ve 23.) CONJ + SUB (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 ('bi'llâhi' 17. / 'llâhi' 26. kelime); قول ×2 ('qul' 1. / 'teqûlû' 24. kelime) (okuma). "
 + T[33] + " (okuma). "
 + cumle(say('say 7:33 2-5', "innemâ harrame rabbiye'l-fevâhişe", True), say('say 7:33 6-10', "mâ zahera minhâ ve mâ betane"), say('say 7:33 5-10', "l-fevâhişe mâ zahera minhâ ve mâ betane"), say('say 7:33 12-14', "ve'l-bağye bi-ğayri'l-haqqi")) + ' '
 + cumle(say('say 7:33 15-22', "ve en tuşrikû bi'llâhi mâ lem yunezzil bihî sultânen", True), say('say 7:33 18-22', "mâ lem yunezzil bihî sultânen")) + ' '
 + cumle(say('say 7:33 23-29', "ve en teqûlû 'ale'llâhi mâ lâ ta'lemûn", True), say('say 7:33 24-29', "teqûlû 'ale'llâhi mâ lâ ta'lemûn"), say('dizi 7 33 24 29', "qâle 'alâ allâh mâ lâ 'alime"), say('say 7:33 25-29', "'ale'llâhi mâ lâ ta'lemûn"),
         say('say 7:33 26-29', "llâhi mâ lâ ta'lemûn"), say('dizi 7 33 26 29', "allâh mâ lâ 'alime"), say('say 7:33 24-26', "teqûlû 'ale'llâhi"), say('dizi 7 33 24 26', "qâle 'alâ allâh")) + ' ' +
 "Ölçüm xref 3:151 (basılmış), 6:81 (basılmış), 6:151 (basılmış), 10:68 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıbı: 'qâle 'alâ allâh mâ lâ 'alime' süzgeç GEÇER; 'allâh mâ lâ 'alime' süzgeç GEÇER; 'qâle 'alâ allâh' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'zahera' / 'betane' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPV + 'inne' + 'mâ' + PERF + izafet + belirli + 'mâ' + PERF + 'min' + 've' + 'mâ' + PERF + 've' + belirli + 've' + belirli + 'bi' + 'ğayr' + belirli + 've' + 'en' + IMPF + 'bi' + lafız + 'mâ' + 'lem' + IMPF + 'bi' + nekre + 've' + 'en' + IMPF + ''alâ' + lafız + 'mâ' + 'lâ' + IMPF; "
 "D2 emir; IMPV ('qul' 1. kelime), NEG ('lem' 19. kelime, 'lâ' 28. kelime); D3 10:68 eşi, أله ×2, قول ×2; D4 1S 1 · 2MP 6 · 2MS 1 · 3FS 1 · 3MS 5, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[33] + "; aktör yok (ölçüm); A2 Rabbin haram kıldıkları: açık ve gizli hayâsızlıklar, günah, haksız yere azgınlık, delilsiz ortak koşma ve Allah hakkında bilmeden söz söyleme; "
 "A3 'innemâ harrame rabbiye'l-fevâhişe mâ zahera minhâ ve mâ betane ve'l-isme ve'l-bağye bi-ğayri'l-haqqi ve en tuşrikû bi'llâhi mâ lem yunezzil bihî sultânen ve en teqûlû 'ale'llâhi mâ lâ ta'lemûn' (söz içi, 2-29. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (29. kelime, ayet içi); muhatap geçişi 2MS → 2MP (ayet içi, 'qul' / 'tuşrikû'); şahıs geçişi 3 → 2 (ayetler arası); edim geçişi soru, emir → emir (ayetler arası).",
)

D[34] = ("◇ 've li-kulli ummetin ecelun fe-izâ câ'e eceluhum lâ yeste'xirûne sâ'aten ve lâ yestaqdimûn' — "
 "'ve' + 'li' + 'kull' + nekre 'umme' + nekre 'ecel' + 'fe' + 'izâ' + PERF 3MS I. bab + 'ecel' + 3MP + 'lâ' + IMPF 3MP X. bab + nekre 'sâ'a' + 've' + 'lâ' + IMPF 3MP X. bab "
 "(ölçüm edim haber, kip NEG 2; 3MP 5 · 3MS 1; bab I. bab ×1 · X. bab ×2). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=11 (n z=-0,15); ölçüm '{{4|fâsıla " + _F[3] + " → ن, N sınıfı}}' — satır aynen (7:33 ن → 7:34 ن); "
 "ölçüm '{{4|simetri \\[3, 3, 6, 1\\]}}' — satır aynen; ölçüm '{{4|harf 51 → harf3 47, isaret 4}}' — satır aynen; ölçüm '{{4|dış düğüm 2}}' — satır aynen. "
 "Ölçüm NEG 2: 'lâ' (7. kelime), 'lâ' (10. kelime); "
 "'ve li-kulli' (1.) kelimesindeki 've' REM; 'fe-izâ' (4.) kelimesindeki 'fe' REM, 'izâ' T; 've lâ' (10.) kelimesindeki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) أجل ×2 ('ecelun' 3. / 'eceluhum' 6. kelime) (okuma). "
 + T[34] + " (okuma). "
 + cumle(say('say 7:34 1-3', "ve li-kulli ummetin ecelun", True), say('say 7:34 4-6', "fe-izâ câ'e eceluhum"), say('say 7:34 5-6', "câ'e eceluhum")) + ' '
 + cumle(say('say 7:34 7-9', "lâ yeste'xirûne sâ'aten", True), say('say 7:34 10-11', "ve lâ yestaqdimûn"), say('dizi 7 34 1 11', "kull umme ecel izâ câ'e ecel lâ yeste'xiru sâ'a lâ yestaqdimu"), say('dizi 7 34 4 11', "izâ câ'e ecel lâ yeste'xiru sâ'a lâ yestaqdimu")) + ' ' +
 "Ölçüm xref 10:49 (emsal olarak basıldı), 16:61 (emsal olarak basıldı). "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'yeste'xirûne' / 'yestaqdimûn' — ayetler arası: yok.",
 "◈K — K2 'ecelun' (3. kelime), 'eceluhum' (6. kelime), 'sâ'aten' (9. kelime).",
 "◈B — —",
 "◈D — D1 've' + 'li' + 'kull' + nekre + nekre + 'fe' + 'izâ' + PERF + izafet + 'lâ' + IMPF + nekre + 've' + 'lâ' + IMPF; "
 "D2 haber; NEG ('lâ' 7. kelime, 'lâ' 10. kelime); D3 10:49 eşi, 16:61 eşi, أجل ×2; D4 3MP 5 · 3MS 1, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[34] + "; aktör yok (ölçüm); A2 her ümmetin bir eceli oluşu; ecel geldiğinde ne geri kalma ne öne geçme; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 2 → 3 (ayetler arası); edim geçişi emir → haber (ayetler arası); bölüm kapanışı.",
)
out = ['# ── blok 7:31-34 (2026-11-25) ──', 'MEAL9 = {']
for n in range(31, 35):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M9 = {']
for n in range(31, 35):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL9); M.update(M9)']
open('/home/claude/yamalar/metin_7_31_34.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

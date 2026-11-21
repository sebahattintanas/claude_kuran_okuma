# sûre 6 blok 19 (6:79-83) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b19/say2.txt'
os.environ['OLC'] = '/home/claude/b19/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'İbrâhîm: yıldız, ay ve güneş' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 79: "Ben yüzümü, gökleri ve yeri yaratana hanîf olarak çevirdim; ben ortak koşanlardan değilim.",
 80: "Kavmi onunla tartıştı. Dedi: Allah hakkında benimle tartışıyor musunuz? Oysa O beni doğru yola iletti. O'na ortak koştuğunuz şeylerden korkmam; meğer ki Rabbim bir şey dilesin. Rabbim her şeyi ilimle kuşatmıştır. Düşünmez misiniz?",
 81: "Ortak koştuklarınızdan nasıl korkarım, oysa siz, hakkında size hiçbir delil indirmediği şeyleri Allah'a ortak koşmaktan korkmuyorsunuz? Öyleyse taraflardan hangisi güvene daha layıktır, eğer biliyorsanız?",
 82: "İman edip imanlarını bir zulümle karıştırmayanlar, güven onlarındır ve onlar doğru yolu bulanlardır.",
 83: "Bu, kavmine karşı İbrâhîm'e verdiğimiz hüccetimizdir. Dilediğimiz kimseyi derecelerle yükseltiriz. Şüphesiz Rabbin hakîmdir, bilendir.",
}

T = {}
T[79] = ("konuşan 1S (adsız; söz içi; 'innî', 'veccehtu', 'vechiye', 've mâ ene' — 1., 2., 3. ve 10. kelime; gönderge 6:75 3. kelime); 'fatara' 3MS (adsız; gönderge 'li'llezî' 4. kelime, 5. kelime)")
T[80] = ("'ve hâccehû' 3MS (fiil uyumu; 1. kelime — fail 2. kelime; nesne zamiri 3MS — gönderge 6:75 3. kelime); 'qavmuhû', 'qâle' 3MS (adsız; gönderge 6:75 3. kelime — 2. ve 3. kelime); "
         "muhatap 2MP (adsız; söz içi; 'e-tuhâccûnnî', 'tuşrikûne', 'tetezekkerûn' — 4., 12. ve 25. kelime; gönderge 'qavmuh' 2. kelime); 'e-tuhâccûnnî' (4. kelime) morph PASS etiketi — naib-i faili (adsız) muhatap 2MP, okuma etken III. bab; "
         "konuşan 1S (adsız; söz içi; 'e-tuhâccûnnî', 've qad hedân', 've lâ exâfu', 'rabbî', 'rabbî' — 4., 8., 10., 17. ve 20. kelime); 've qad hedân' 3MS (adsız; söz içi; gönderge 'llâh' 6. kelime, 8. kelime); "
         "'bih' 3MS (adsız; söz içi; gönderge 'mâ' 11. kelime, 13. kelime); 'yeşâ'e' 3MS (fiil uyumu; 16. kelime — fail 17. kelime); 'vesi'a' 3MS (fiil uyumu; 19. kelime — fail 20. kelime)")
T[81] = ("konuşan 1S (adsız; söz içi; 'exâfu' — 2. kelime); muhatap 2MP (adsız; söz içi; 'eşraktum', 'texâfûne', 'ennekum', 'eşraktum', ''aleykum', 'kuntum', 'ta'lemûn' — 4., 6., 7., 8., 14., 21. ve 22. kelime); "
         "'yunezzil' 3MS (adsız; söz içi; gönderge 'llâhi' 9. kelime, 12. kelime); 'bihî' 3MS (adsız; söz içi; gönderge 'mâ' 10. kelime, 13. kelime)")
T[82] = ("'âmenû', 've lem yelbisû', 'îmânehum' 3MP (adsız; gönderge 'llezîne' 1. kelime — 2., 4. ve 5. kelime); 'lehumu', 've hum' 3MP (adsız; gönderge 'ulâ'ike' 7. kelime — 8. ve 10. kelime)")
T[83] = ("konuşan 1P (adsız; 'huccetunâ', 'âteynâhâ', 'nerfe'u', 'neşâ'' — 2., 3., 7. ve 10. kelime); 'âteynâhâ' 3FS (adsız; gönderge 'huccetunâ' 2. kelime, 3. kelime); "
         "'qavmih' 3MS (adsız; gönderge 'ibrâhîme' 4. kelime, 6. kelime); muhatap 2MS (adsız; 'rabbeke' — 12. kelime)")

D = {}
D[79] = ("◇ 'innî veccehtu vechiye li'llezî fatara's-semâvâti ve'l-arda hanîfen ve mâ ene mine'l-muşrikîn' — "
 "'inne' + 1S + PERF 1S II. bab + 1S + 'vech' + 1S + 'li' + 'ellezî' + PERF 3MS I. bab + belirli çoğul 'semâ'' + 've' + belirli 'ard' + nekre 'hanîf' + 've' + 'mâ' + 'ene' + 'min' + belirli çoğul etken ortaç 'muşrik' "
 "(ölçüm edim haber, kip NEG 1; 1S 5 · 3MS 1; bab I. bab ×1 · II. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=12 (n z=-0,04); ölçüm '{{1|fâsıla ٱلمشركين → ن, N sınıfı}}' — satır aynen (6:78 ن → 6:79 ن); "
 "ölçüm '{{1|harf 54 → harf3 51, isaret 3}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen; ölçümde simetri alanı yok. "
 "Ölçüm NEG 1: 've mâ' (9. kelime); 've'l-arda' (7.) kelimesindeki 've' CONJ; 've mâ' (9.) kelimesindeki 've' REM; 'innî' (1.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) وجه ×2 ('veccehtu' 2. / 'vechiye' 3. kelime) (okuma). "
 + T[79] + " (okuma). "
 + cumle(say('say 6:79 9-11', "ve mâ ene mine", True)) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: '_ _ _' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 's-semâvâti' / 've'l-arda' — ayetler arası: yok.",
 "◈K — K1 's-semâvâti' (6. kelime), 'l-arda' (7. kelime).",
 "◈B — —",
 "◈D — D1 'inne' + PERF + izafet + 'li' + 'ellezî' + PERF + belirli + 've' + belirli + nekre + 've' + 'mâ' + 'ene' + 'min' + belirli; "
 "D2 haber; NEG ('ve mâ' 9. kelime); D3 وجه ×2; D4 1S 5 · 3MS 1, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[79] + "; aktör yok (ölçüm); A2 yüzünü gökleri ve yeri yaratana hanîf olarak çevirme; ortak koşanlardan olmama; "
 "A3 'innî veccehtu vechiye li'llezî fatara's-semâvâti ve'l-arda hanîfen ve mâ ene mine'l-muşrikîn' (söz biçimli içerik, 1. kelimeden); "
 "A4 " + BOLUM + "; şahıs geçişi 3 → 1 (ayetler arası); edim geçişi nida → haber (ayetler arası).",
)

D[80] = ("◇ 've hâccehû qavmuhû qâle e-tuhâccûnnî fi'llâhi ve qad hedâni ve lâ exâfu mâ tuşrikûne bihî illâ en yeşâ'e rabbî şey'en vesi'a rabbî kulle şey'in 'ilmen e-fe-lâ tetezekkerûn' — "
 "'ve' + PERF 3MS III. bab + 3MS + 'qavm' + 3MS + PERF 3MS I. bab + 'e' + IMPF 2MP III. bab + 2MP + 1S + 'fî' + lafız + 've' + 'qad' + PERF 3MS I. bab + 1S + 've' + 'lâ' + IMPF 1S I. bab + 'mâ' + IMPF 2MP IV. bab + 2MP + 'bi' + 3MS + "
 "'illâ' + 'en' + IMPF 3MS I. bab + 'rabb' + 1S + nekre 'şey'' + PERF 3MS I. bab + 'rabb' + 1S + 'kull' + nekre 'şey'' + nekre ''ilm' + 'e' + 'fe' + 'lâ' + IMPF 2MP V. bab + 2MP "
 "(ölçüm edim soru, kip CERT 1 · INTG 2 · NEG 2; 1S 5 · 2MP 6 · 3MS 8; bab I. bab ×5 · III. bab ×2 · IV. bab ×1 · V. bab ×1). "
 "Allah lafzı 6. sırada (ölçüm allah z=0,27); Rab 17. ve 20. sırada (ölçüm rab z=1,38); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=25 (n z=1,34); ölçüm '{{2|biçim ISTISNA}}' — satır aynen; ölçüm '{{2|EDİLGEN 1/9 fiil, pas z=0,30}}' — satır aynen; ölçüm '{{2|fâsıla تتذكرون → ن, N sınıfı}}' — satır aynen (6:79 ن → 6:80 ن); "
 "ölçüm '{{2|simetri \\[3, 5, 9, 1\\]}}' — satır aynen; ölçüm '{{2|harf 99 → harf3 91, isaret 8}}' — satır aynen; ölçüm '{{2|dış düğüm 2}}' — satır aynen. "
 "Ölçüm CERT 1: 've qad' (7. kelime); INTG 2: 'e-tuhâccûnnî' (4. kelime), 'e-fe-lâ' (24. kelime); NEG 2: 've lâ' (9. kelime), 'e-fe-lâ' (24. kelime); 've hâccehû' (1.) kelimesindeki 've' REM; 've qad' (7.) kelimesindeki 've' CIRC; "
 "'ve lâ' (9.) kelimesindeki 've' CONJ; 'illâ' (14.) EXP; 'en' (15.) SUB; 'fe' (24.) SUP (okuma). "
 "Kök ikilemesi (ölçüm) حجج ×2 ('ve hâccehû' 1. / 'e-tuhâccûnnî' 4. kelime), ربب ×2 ('rabbî' 17. / 20. kelime), شيأ ×3 ('yeşâ'e' 16., 'şey'en' 18., 'şey'in' 22. kelime) (okuma). "
 + T[80] + " (okuma). "
 + cumle(say('say 6:80 10-12', "exâfu mâ tuşrikûne", True), say('dizi 6 80 10 12', "xâfe mâ eşrake")) + ' '
 + cumle(say('say 6:80 14-16', "illâ en yeşâ'e", True), say('dizi 6 80 14 16', "illâ en şâ'e")) + ' '
 + cumle(say('say 6:80 20-22', "rabbî kulle şey'in", True), say('dizi 6 80 20 22', "rabb kull şey'")) + ' '
 + cumle(say('say 6:80 24-25', "e-fe-lâ tetezekkerûn", True)) + ' '
 "Ölçüm xref okunmuş 1 ayet ve okunmamış 1 ayet. "
 "Ölçüm nakarat3 kalıpları: 'xâfe _ eşrake' süzgeç GEÇMEZ, '_ _ şâ'e' süzgeç GEÇMEZ, 'rabb kull şey'' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + PERF + izafet + PERF + 'e' + IMPF + 'fî' + lafız + 've' + 'qad' + PERF + 've' + 'lâ' + IMPF + 'mâ' + IMPF + 'bi' + 'illâ' + 'en' + IMPF + izafet + nekre + PERF + izafet + 'kull' + nekre + nekre + 'e' + 'fe' + 'lâ' + IMPF; "
 "D2 soru; CERT ('ve qad' 7. kelime), INTG ('e-tuhâccûnnî' 4. kelime, 'e-fe-lâ' 24. kelime), NEG ('ve lâ' 9. kelime, 'e-fe-lâ' 24. kelime); D3 حجج ×2, ربب ×2, شيأ ×3; D4 1S 5 · 2MP 6 · 3MS 8, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[80] + "; aktör yok (ölçüm); A2 kavminin İbrâhîm'le tartışması; Allah hakkında tartışma sorusu; ortak koşulanlardan korkmama; Rabbin dilemesi istisnası; Rabbin ilmiyle her şeyi kuşatması; düşünme çağrısı; "
 "A3 'e-tuhâccûnnî fi'llâhi ve qad hedâni ve lâ exâfu mâ tuşrikûne bihî illâ en yeşâ'e rabbî şey'en vesi'a rabbî kulle şey'in 'ilmen e-fe-lâ tetezekkerûn' (söz içi, 4-25. kelime); "
 "A4 " + BOLUM + "; söz açılır (4. kelime); söz kapanır (25. kelime, ayet içi); şahıs geçişi 1 → 3 (ayetler arası); edim geçişi haber → soru (ayetler arası).",
)

D[81] = ("◇ 've keyfe exâfu mâ eşraktum ve lâ texâfûne ennekum eşraktum bi'llâhi mâ lem yunezzil bihî 'aleykum sultânen fe-eyyu'l-ferîqayni ehaqqu bi'l-emni in kuntum ta'lemûn' — "
 "'ve' + 'keyfe' + IMPF 1S I. bab + 'mâ' + PERF 2MP IV. bab + 2MP + 've' + 'lâ' + IMPF 2MP I. bab + 2MP + 'enne' + 2MP + PERF 2MP IV. bab + 2MP + 'bi' + lafız + 'mâ' + 'lem' + IMPF 3MS II. bab + 'bi' + 3MS + ''alâ' + 2MP + nekre 'sultân' + "
 "'fe' + 'eyy' + belirli ikil 'ferîq' + 'ehaqq' + 'bi' + belirli 'emn' + 'in' + PERF 2MP I. bab + 2MP + IMPF 2MP I. bab + 2MP "
 "(ölçüm edim soru, şart, kip COND 1 · INTG 2 · NEG 2; 1S 1 · 2MP 12 · 3MS 2; bab I. bab ×4 · II. bab ×1 · IV. bab ×2). "
 "Allah lafzı 9. sırada (ölçüm allah z=0,38); Rab yok; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); ölçüm '{{3|aktör: adsız `ferîk` 17\\. sırada}}' — satır aynen; aktör adsız 'l-ferîqayni' 17. sırada — taraflar: ortak koşanlar ve İbrâhîm (okuma). "
 "Ölçüm 'yıldız yok' — satır aynen; n=22 (n z=1,02); ölçüm '{{3|fâsıla تعلمون → ن, N sınıfı}}' — satır aynen (6:80 ن → 6:81 ن); "
 "ölçüm '{{3|simetri \\[4, 2, 6, 1\\]}}' — satır aynen; ölçüm '{{3|harf 96 → harf3 92, isaret 4}}' — satır aynen; ölçüm '{{3|dış düğüm 2}}' — satır aynen. "
 "Ölçüm COND 1: 'in' (20. kelime); INTG 2: 've keyfe' (1. kelime), 'fe-eyyu'l-ferîqayni' (16. kelime); NEG 2: 've lâ' (5. kelime), 'lem' (11. kelime); 've keyfe' (1.) kelimesindeki 've' REM; 've lâ' (5.) kelimesindeki 've' CONJ; "
 "'fe' (16.) REM; 'ennekum' (7.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) خوف ×2 ('exâfu' 2. / 'texâfûne' 6. kelime), شرك ×2 ('eşraktum' 4. / 8. kelime) (okuma). "
 + T[81] + " (okuma). "
 + cumle(say('say 6:81 2-4', "exâfu mâ eşraktum", True), say('dizi 6 81 2 4', "xâfe mâ eşrake")) + ' '
 + cumle(say('say 6:81 3-5', "mâ eşraktum ve lâ", True), say('dizi 6 81 3 5', "mâ eşrake lâ")) + ' '
 + cumle(say('say 6:81 9-12', "bi'llâhi mâ lem yunezzil", True)) + ' '
 "Ölçüm xref 3:151 (emsal olarak basıldı) ve okunmamış 1 ayet. "
 "Ölçüm nakarat3 kalıpları: 'xâfe _ eşrake' süzgeç GEÇMEZ, '_ eşrake _' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'exâfu' / 'bi'l-emni' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'keyfe' + IMPF + 'mâ' + PERF + 've' + 'lâ' + IMPF + 'enne' + PERF + 'bi' + lafız + 'mâ' + 'lem' + IMPF + 'bi' + ''alâ' + nekre + 'fe' + 'eyy' + belirli + 'ehaqq' + 'bi' + belirli + 'in' + PERF + IMPF; "
 "D2 soru, şart; COND ('in' 20. kelime), INTG ('ve keyfe' 1. kelime, 'fe-eyyu'l-ferîqayni' 16. kelime), NEG ('ve lâ' 5. kelime, 'lem' 11. kelime); D3 خوف ×2, شرك ×2; 3:151 eşi; D4 1S 1 · 2MP 12 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[81] + "; aktör adsız 'l-ferîqayni' (17. kelime; ölçüm); A2 ortak koşulanlardan korkmama sorusu; delilsiz ortak koşmaktan korkmayanlar; hangi tarafın güvene layık olduğu sorusu; "
 "A3 've keyfe exâfu mâ eşraktum ve lâ texâfûne ennekum eşraktum bi'llâhi mâ lem yunezzil bihî 'aleykum sultânen fe-eyyu'l-ferîqayni ehaqqu bi'l-emni in kuntum ta'lemûn' (söz biçimli içerik, 1. kelimeden); "
 "A4 " + BOLUM + "; şart → cevap (ayet içi; COND 'in' 20. kelime: 'in kuntum ta'lemûn' / 'fe-eyyu'l-ferîqayni ehaqqu bi'l-emn' (16. kelime)); şahıs geçişi 3 → 2 (ayetler arası); edim geçişi soru → soru, şart (ayetler arası).",
)

D[82] = ("◇ 'ellezîne âmenû ve lem yelbisû îmânehum bi-zulmin ulâ'ike lehumu'l-emnu ve hum muhtedûn' — "
 "'ellezî' + PERF 3MP IV. bab + 3MP + 've' + 'lem' + IMPF 3MP I. bab + 3MP + mastar 'îmân' + 3MP + 'bi' + nekre 'zulm' + 'ulâ'i' + 'ke' + 'li' + 3MP + belirli 'emn' + 've' + 3MP + çoğul etken ortaç 'muhtedî' "
 "(ölçüm edim haber, kip NEG 1; 3MP 7; bab I. bab ×1 · IV. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=11 (n z=-0,15); ölçüm '{{4|fâsıla مهتدون → ن, N sınıfı}}' — satır aynen (6:81 ن → 6:82 ن); "
 "ölçüm '{{4|simetri \\[3, 1, 8, 1\\]}}' — satır aynen; ölçüm '{{4|harf 55 → harf3 52, isaret 3}}' — satır aynen; ölçüm '{{4|dış düğüm 0}}' — satır aynen. "
 "Ölçüm NEG 1: 've lem' (3. kelime); 've lem' (3.) ve 've hum' (10.) kelimelerindeki 've' CONJ; 'ulâ'ike' (7.) DEM (okuma). "
 "Kök ikilemesi (ölçüm) أمن ×3 ('âmenû' 2., 'îmânehum' 5., 'l-emnu' 9. kelime) (okuma). "
 + T[82] + " (okuma). "
 + cumle(say('say 6:82 10-11', "ve hum muhtedûn", True)) + ' '
 "Ölçüm xref yok; ölçüm bağ yok (esit2, nakarat3, xref üçü de boş). "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'âmenû' / 'bi-zulmin' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'ellezî' + PERF + 've' + 'lem' + IMPF + izafet + 'bi' + nekre + 'ulâ'i' + 'li' + belirli + 've' + 'muhtedî'; "
 "D2 haber; NEG ('ve lem' 3. kelime); D3 أمن ×3; D4 3MP 7, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[82] + "; aktör yok (ölçüm); A2 imanını zulümle karıştırmayanlar; güvenin onlara ait oluşu; doğru yolu bulma; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 2 → 3 (ayetler arası); edim geçişi soru, şart → haber (ayetler arası).",
)

D[83] = ("◇ 've tilke huccetunâ âteynâhâ ibrâhîme 'alâ qavmihî nerfe'u deracâtin men neşâ'u inne rabbeke hakîmun 'alîm' — "
 "'ve' + 'tilke' + 'hucce' + 1P + PERF 1P IV. bab + 1P + 3FS + özel ad 'ibrâhîm' + ''alâ' + 'qavm' + 3MS + IMPF 1P I. bab + nekre çoğul 'derece' + 'men' + IMPF 1P I. bab + 'inne' + 'rabb' + 2MS + nekre 'hakîm' + nekre ''alîm' "
 "(ölçüm edim haber, kip yok; 1P 5 · 2MS 1 · 3FS 1 · 3MS 1; bab I. bab ×2 · IV. bab ×1). "
 "Allah lafzı yok; Rab 12. sırada (ölçüm rab z=1,20); ölçüm '{{5|esmâ حَكِيم 13\\. sırada, SON konum, MÜHÜR \\| عَلِيم 14\\. sırada, SON konum, MÜHÜR}}' — satır aynen; esma_kayit çıktısı 'mühür EVET (ÇİFT)' (uyuşuyor); "
 "esma_el kaydı 'ilahi' — 'inne rabbeke hakîmun 'alîm', kural ''inne/enne' haberi → ilahi' (Rab) (okuma); ölçüm '{{5|aktör: adlı إِبْراهِيم 4\\. sırada \\(kisi, rol meful\\)}}' — satır aynen. "
 "Ölçüm 'yıldız yok' — satır aynen; n=14 (n z=0,17); ölçüm '{{5|fâsıla عليم → م, N sınıfı}}' — satır aynen (6:82 ن → 6:83 م); "
 "ölçüm '{{5|harf 61 → harf3 56, isaret 5}}' — satır aynen; ölçüm '{{5|dış düğüm 2}}' — satır aynen; ölçüm '{{5|İÇ düğüm 1}}' — satır aynen; ölçümde simetri alanı yok. "
 "Ölçüm kip yok; 've tilke' (1.) kelimesindeki 've' REM; 'tilke' (1.) DEM; 'inne' (11.) ACC (okuma). "
 "Kök ikilemesi yok (ölçüm). "
 + T[83] + " (okuma). "
 + cumle(say('say 6:83 7-10', "nerfe'u deracâtin men neşâ'u", True)) + ' '
 + cumle(say('say 6:83 11-14', "inne rabbeke hakîmun 'alîm", True), say('dizi 6 83 11 14', "inne rabb hakîm 'alîm")) + ' '
 "Ölçüm xref 12:76 (emsal olarak basıldı), okunmuş 1 ayet ve okunmamış 1 ayet (sûre içi 1). "
 "Ölçüm nakarat3 kalıbı: '_ rabb hakîm 'alîm' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'tilke' + izafet + PERF + özel ad + ''alâ' + izafet + IMPF + nekre + 'men' + IMPF + 'inne' + izafet + nekre + nekre; "
 "D2 haber; D3 —; 12:76 eşi; D4 1P 5 · 2MS 1 · 3FS 1 · 3MS 1, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[83] + "; aktör adlı 'ibrâhîme' (4. kelime; ölçüm rol meful); A2 İbrâhîm'e kavmine karşı verilen hüccet; dilenenin derecelerle yükseltilmesi; Rabbin hakîm ve bilen oluşu; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 3 → 1 (ayetler arası); edim geçişi yok (ayetler arası); bölüm kapanışı.",
)
out = ['# ── blok 6:79-83 (2026-11-21) ──', 'MEAL19 = {']
for n in range(79, 84):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M19 = {']
for n in range(79, 84):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL19); M.update(M19)']
open('/home/claude/yamalar/metin_6_79_83.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

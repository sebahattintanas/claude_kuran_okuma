# sûre 6 blok 12 (6:50-53) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b12/say2.txt'
os.environ['OLC'] = '/home/claude/b12/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'De ki: gaybı bilmem; sabah akşam Rablerine dua edenler' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 50: "De ki: Size, Allah'ın hazineleri yanımdadır demiyorum; gaybı da bilmem; size melek olduğumu da söylemiyorum. Ben ancak bana vahyolunana uyarım. De ki: Kör ile gören eşit olur mu? Hiç düşünmez misiniz?",
 51: "Rablerine toplanmaktan korkanları onunla uyar; onlar için O'ndan başka bir dost ve şefaatçi yoktur; ola ki sakınırlar.",
 52: "Sabah akşam Rablerine, O'nun yüzünü isteyerek dua edenleri kovma. Onların hesabından sana hiçbir şey yoktur, senin hesabından da onlara hiçbir şey yoktur ki onları kovasın da zalimlerden olasın.",
 53: "Böylece onların bir kısmını bir kısmıyla sınadık ki: Aramızdan Allah'ın kendilerine lütfettiği bunlar mı? desinler. Allah şükredenleri daha iyi bilen değil midir?",
}

T = {}
T[50] = ("muhatap 2MS (adsız; 'qul', 'qul' — 1. ve 22. kelime); konuşan 1S (adsız; söz içi; 'eqûlu', ''indî', 'a'lemu', 'eqûlu', 'innî', 'ettebi'u', 'ileyy' — 3., 5., 9., 12., 14., 17. ve 21. kelime); "
         "muhatap 2MP (adsız; söz içi; 'lekum', 'lekum', 'tetefekkerûn' — 4., 13. ve 28. kelime); 'yûhâ' 3MS (adsız; edilgen — naib-i faili zamir; gönderge 'mâ' 19. kelime, 20. kelime); "
         "'yestevi' 3MS (fiil uyumu; 24. kelime — fail 25. kelime)")
T[51] = ("muhatap 2MS (adsız; 've enzir' — 1. kelime); 'bihi' 3MS (adsız; gönderge 6:50 19. kelime, 2. kelime); 'yaxâfûne', 'rabbihim', 'lehum', 'le'allehum', 'yetteqûn' 3MP (adsız; gönderge 'llezîne' 3. kelime — 4., 8., 10., 16. ve 17. kelime); "
         "'yuhşerû' 3MP (adsız; edilgen — naib-i faili zamir; gönderge 'llezîne' 3. kelime, 6. kelime); 'leyse' 3MS (fiil uyumu; 9. kelime — fail 13. kelime); 'dûnihî' 3MS (adsız; gönderge 'rabbihim' 8. kelime, 12. kelime)")
T[52] = ("muhatap 2MS (adsız; 'tatrudi', ''aleyke', 'hisâbike', 'fe-tatrudehum', 'fe-tekûne' — 2., 11., 18., 22. ve 23. kelime); "
         "'yed'ûne', 'rabbehum', 'yurîdûne', 'hisâbihim', ''aleyhim', 'fe-tatrudehum' 3MP (adsız; gönderge 'llezîne' 3. kelime — 4., 5., 8., 13., 19. ve 22. kelime); 'vechehû' 3MS (adsız; gönderge 'rabbehum' 5. kelime, 9. kelime)")
T[53] = ("konuşan 1P (adsız; 'fetennâ' — 2. kelime); 'ba'dahum', 'li-yeqûlû' 3MP (adsız; gönderge 6:52 3. kelime — 3. ve 5. kelime); 'menne' 3MS (fiil uyumu; 7. kelime — fail 8. kelime); "
         "''aleyhim' 3MP (adsız; gönderge 'hâ'ulâ'i' 6. kelime, 9. kelime); konuşan 1P (adsız; söz içi; 'beyninâ' — 11. kelime); 'e-leyse' 3MS (fiil uyumu; 12. kelime — fail 13. kelime)")

D = {}
D[50] = ("◇ 'qul lâ eqûlu lekum 'indî xazâ'inu'llâhi ve lâ a'lemu'l-ğaybe ve lâ eqûlu lekum innî melek, in ettebi'u illâ mâ yûhâ ileyy, qul hel yestevi'l-a'mâ ve'l-basîr, e-fe-lâ tetefekkerûn' — "
 "IMPV 2MS I. bab + 'lâ' + IMPF 1S I. bab + 'li' + 2MP + ''inde' + 1S + çoğul 'xazâ'in' + lafız + 've' + 'lâ' + IMPF 1S I. bab + belirli 'ğayb' + 've' + 'lâ' + IMPF 1S I. bab + 'li' + 2MP + 'inne' + 1S + nekre 'melek' + "
 "'in' + IMPF 1S VIII. bab + 'illâ' + 'mâ' + edilgen IMPF 3MS IV. bab + 'ilâ' + 1S + IMPV 2MS I. bab + 'hel' + IMPF 3MS VIII. bab + belirli 'a'mâ' + 've' + belirli 'basîr' + 'e' + 'fe' + 'lâ' + IMPF 2MP V. bab "
 "(ölçüm edim soru, emir, kip IMPV 2 · INTG 2 · NEG 5 · RES 1; 1S 7 · 2MP 4 · 2MS 2 · 3MS 2; bab I. bab ×5 · IV. bab ×1 · V. bab ×1 · VIII. bab ×2). "
 "Allah lafzı 7. sırada (ölçüm allah z=0,19); Rab yok; ölçüm '{{1|esmâ بَصِير 26\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton denge' — ölçüm MÜHÜRSÜZ ile uyuşmuyor (araç tanımı farkı; muhur_el hayır — ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 'yestevi'l-a'mâ ve'l-basîr', kural 'çoğul insan göndergeli → degil' (insan göndergesi; 'l-basîr' cins: gören insan, körün karşıtı; 'ş-şâkirîn' çoğul) (okuma; kural adı 'çoğul' cins okumasıyla — tam okuma sonu); aktör yok (ölçüm). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=28 (n z=1,65); ölçüm '{{1|biçim HASR}}' — satır aynen; ölçüm '{{1|EDİLGEN 1/9 fiil, pas z=0,30}}' — satır aynen; "
 "ölçüm '{{1|fâsıla تتفكرون → ن, N sınıfı}}' — satır aynen (6:49 ن → 6:50 ن); ölçüm '{{1|simetri \\[6, 8, 18, 2\\]}}' — satır aynen; ölçüm '{{1|harf 106 → harf3 103, isaret 3}}' — satır aynen; ölçüm '{{1|dış düğüm 5}}' — satır aynen. "
 "Ölçüm IMPV 2: 'qul' (1. ve 22. kelime); INTG 2: 'hel' (23. kelime), 'e-fe-lâ' (27. kelime); NEG 5: 'lâ' (2. kelime), 've lâ' (8. ve 11. kelime), 'in' (16. kelime), 'e-fe-lâ' (27. kelime); RES 1: 'illâ' (18. kelime); "
 "'ve lâ' (8., 11.) ve 've'l-basîr' (26.) kelimelerindeki 've' CONJ; 'inne' (14.) ACC; 'e-fe-lâ' (27.) kelimesindeki 'fe' SUP (okuma). "
 "Kök ikilemesi (ölçüm) قول ×4 ('qul' 1., 'eqûlu' 3., 'eqûlu' 12., 'qul' 22. kelime) (okuma). "
 + T[50] + " (okuma). "
 + cumle(say('say 6:50 5-7', "'indî xazâ'inu'llâh", True)) + ' '
 + cumle(say('say 6:50 16-18', "in ettebi'u illâ", True), say('dizi 6 50 16 18', "in ittebe illâ")) + ' '
 + cumle(say('say 6:50 25-26', "l-a'mâ ve'l-basîr", True)) + ' '
 "Ölçüm xref 11:31 (emsal olarak basıldı) ve okunmuş 4 ayet. "
 "Ölçüm nakarat3 kalıpları: 'in ittebe illâ' süzgeç GEÇER, 'mâ evhâ ilâ' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'l-a'mâ' / 'l-basîr' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 'l-basîr' (26. kelime); B4 —.",
 "◈D — D1 IMPV + 'lâ' + IMPF + 'li' + ''inde' + izafet + lafız + 've' + 'lâ' + IMPF + belirli + 've' + 'lâ' + IMPF + 'li' + 'inne' + nekre + 'in' + IMPF + 'illâ' + 'mâ' + IMPF + 'ilâ' + IMPV + 'hel' + IMPF + belirli + 've' + belirli + 'e' + 'fe' + 'lâ' + IMPF; "
 "D2 soru, emir; IMPV ('qul' 1. kelime, 'qul' 22. kelime), INTG ('hel' 23. kelime, 'e-fe-lâ' 27. kelime), NEG ('lâ' 2. kelime, 've lâ' 8. kelime, 've lâ' 11. kelime, 'in' 16. kelime, 'e-fe-lâ' 27. kelime), RES ('illâ' 18. kelime); "
 "D3 قول ×4; 11:31 eşi; D4 1S 7 · 2MP 4 · 2MS 2 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[50] + "; aktör yok (ölçüm); A2 Allah'ın hazineleri, gayb ve meleklik iddiasının reddi; vahyolunana uyma; kör ile görenin eşitliği sorusu; düşünmeye çağrı; "
 "A3 'lâ eqûlu lekum 'indî xazâ'inu'llâhi ve lâ a'lemu'l-ğaybe ve lâ eqûlu lekum innî melek, in ettebi'u illâ mâ yûhâ ileyy' (söz içi, 2-21. kelime); 'hel yestevi'l-a'mâ ve'l-basîr, e-fe-lâ tetefekkerûn' (söz içi, 23-28. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (21. kelime, ayet içi); söz açılır (23. kelime); söz kapanır (28. kelime, ayet içi); şahıs geçişi 3 → 1 (ayetler arası); edim geçişi haber → soru, emir (ayetler arası); bölüm açılışı.",
)

D[51] = ("◇ 've enzir bihi'llezîne yaxâfûne en yuhşerû ilâ rabbihim leyse lehum min dûnihî veliyyun ve lâ şefî'un le'allehum yetteqûn' — "
 "'ve' + IMPV 2MS IV. bab + 'bi' + 3MS + 'ellezî' + IMPF 3MP I. bab + 'en' + edilgen IMPF 3MP I. bab + 'ilâ' + 'rabb' + 3MP + PERF 3MS I. bab + 'li' + 3MP + 'min' + 'dûn' + 3MS + nekre 'veliyy' + 've' + 'lâ' + nekre 'şefî'' + 'le'alle' + 3MP + IMPF 3MP VIII. bab "
 "(ölçüm edim emir, kip IMPV 1 · NEG 1; 2MS 1 · 3MP 9 · 3MS 3; bab I. bab ×3 · IV. bab ×1 · VIII. bab ×1). "
 "Allah lafzı yok; Rab 8. sırada (ölçüm rab z=0,93); ölçüm '{{2|esmâ وَلِيّ 13\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton cemâl' — ölçüm MÜHÜRSÜZ ile uyuşmuyor (araç tanımı farkı; muhur_el hayır — ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 'min dûnihî veliyyun', kural 'esmâ adı esmâ dışı göndergeyle → degil' (esmâ dışı gönderge) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=17 (n z=0,49); ölçüm '{{2|EDİLGEN 1/5 fiil, pas z=0,81}}' — satır aynen; ölçüm '{{2|fâsıla يتقون → ن, N sınıfı}}' — satır aynen (6:50 ن → 6:51 ن); "
 "ölçüm '{{2|simetri \\[3, 2, 10, 1\\]}}' — satır aynen; ölçüm '{{2|harf 70 → harf3 65, isaret 5}}' — satır aynen; ölçüm '{{2|dış düğüm 2}}' — satır aynen. "
 "Ölçüm IMPV 1: 've enzir' (1. kelime); NEG 1: 've lâ' (14. kelime); 've enzir' (1.) ve 've lâ' (14.) kelimelerindeki 've' CONJ; 'en' (5.) SUB; 'le'allehum' (16.) ACC (okuma). "
 + T[51] + " (okuma). "
 + cumle(say('say 6:51 13-15', "veliyyun ve lâ şefî'", True), say('say 6:51 16-17', "le'allehum yetteqûn")) + ' '
 "Ölçüm xref okunmuş 2 ayet. "
 "Ölçüm nakarat3 kalıbı: 'veliyy lâ şefî'' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + IMPV + 'bi' + 'ellezî' + IMPF + 'en' + IMPF + 'ilâ' + izafet + PERF + 'li' + 'min' + izafet + nekre + 've' + 'lâ' + nekre + 'le'alle' + IMPF; "
 "D2 emir; IMPV ('ve enzir' 1. kelime), NEG ('ve lâ' 14. kelime); D3 —; D4 2MS 1 · 3MP 9 · 3MS 3, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[51] + "; aktör yok (ölçüm); A2 Rablerine toplanmaktan korkanları uyarma; O'ndan başka dost ve şefaatçi yokluğu; sakınma umudu; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 1 → 3 (ayetler arası); edim geçişi soru, emir → emir (ayetler arası).",
)

D[52] = ("◇ 've lâ tatrudi'llezîne yed'ûne rabbehum bi'l-ğadâti ve'l-'aşiyyi yurîdûne vechehû, mâ 'aleyke min hisâbihim min şey'in ve mâ min hisâbike 'aleyhim min şey'in fe-tatrudehum fe-tekûne mine'z-zâlimîn' — "
 "'ve' + 'lâ' + IMPF 2MS I. bab + 'ellezî' + IMPF 3MP I. bab + 'rabb' + 3MP + 'bi' + belirli 'ğadâ' + 've' + belirli ''aşiyy' + IMPF 3MP IV. bab + 'vech' + 3MS + 'mâ' + ''alâ' + 2MS + 'min' + mastar 'hisâb' + 3MP + 'min' + nekre 'şey'' + "
 "'ve' + 'mâ' + 'min' + mastar 'hisâb' + 2MS + ''alâ' + 3MP + 'min' + nekre 'şey'' + 'fe' + IMPF 2MS I. bab + 3MP + 'fe' + IMPF 2MS I. bab + 'min' + belirli çoğul etken ortaç 'zâlim' "
 "(ölçüm edim yasak, kip NEG 2 · PRO 1; 2MS 5 · 3MP 8 · 3MS 1; bab I. bab ×4 · IV. bab ×1). "
 "Allah lafzı yok; Rab 5. sırada (ölçüm rab z=0,53); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=25 (n z=1,34); ölçüm '{{3|biçim NEHY}}' — satır aynen; ölçüm '{{3|fâsıla ٱلظلمين → ن, N sınıfı}}' — satır aynen (6:51 ن → 6:52 ن); "
 "ölçüm '{{3|simetri \\[6, 10, 16, 2\\]}}' — satır aynen; ölçüm '{{3|harf 108 → harf3 104, isaret 4}}' — satır aynen; ölçüm '{{3|dış düğüm 1}}' — satır aynen. "
 "Ölçüm NEG 2: 'mâ' (10. kelime), 've mâ' (16. kelime); PRO 1: 've lâ' (1. kelime); 've lâ' (1.) kelimesindeki 've' REM; 've'l-'aşiyyi' (7.) ve 've mâ' (16.) kelimelerindeki 've' CONJ; 'fe-tatrudehum' (22.) kelimesindeki 'fe' CAUS; 'fe-tekûne' (23.) kelimesindeki 'fe' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) حسب ×2 ('hisâbihim' 13. / 'hisâbike' 18. kelime), شيأ ×2 ('şey'in' 15. / 21. kelime), طرد ×2 ('tatrudi' 2. / 'fe-tatrudehum' 22. kelime) (okuma). "
 + T[52] + " (okuma). "
 + cumle(say('say 6:52 3-9', "llezîne yed'ûne rabbehum bi'l-ğadâti ve'l-'aşiyyi yurîdûne vechehû", True)) + ' '
 + cumle(say('say 6:52 12-15', "min hisâbihim min şey'", True), say('say 6:52 24-25', "mine'z-zâlimîn")) + ' '
 "Ölçüm xref 18:28 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıbı: 'min hisâb min şey'' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'min hisâbihim' / 'min hisâbike'; 'l-ğadâti' / 'l-'aşiyyi' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'lâ' + IMPF + 'ellezî' + IMPF + izafet + 'bi' + belirli + 've' + belirli + IMPF + izafet + 'mâ' + ''alâ' + 'min' + izafet + 'min' + nekre + 've' + 'mâ' + 'min' + izafet + ''alâ' + 'min' + nekre + 'fe' + IMPF + 'fe' + IMPF + 'min' + belirli; "
 "D2 yasak; NEG ('mâ' 10. kelime, 've mâ' 16. kelime), PRO ('ve lâ' 1. kelime); D3 حسب ×2, شيأ ×2, طرد ×2; 18:28 eşi; D4 2MS 5 · 3MP 8 · 3MS 1, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[52] + "; aktör yok (ölçüm); A2 sabah akşam Rablerine dua edenleri kovma yasağı; hesapların karşılıklı yokluğu; kovanın zalimlerden olması; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi emir → yasak (ayetler arası).",
)

D[53] = ("◇ 've kezâlike fetennâ ba'dahum bi-ba'din li-yeqûlû e-hâ'ulâ'i menne'llâhu 'aleyhim min beyninâ, e-leyse'llâhu bi-a'leme bi'ş-şâkirîn' — "
 "'ve' + 'ke' + 'zâlike' + PERF 1P I. bab + 'ba'd' + 3MP + 'bi' + nekre 'ba'd' + 'li' + IMPF 3MP I. bab + 'e' + 'hâ' + 'zâ' + PERF 3MS I. bab + lafız + ''alâ' + 3MP + 'min' + 'beyn' + 1P + 'e' + PERF 3MS I. bab + lafız + 'bi' + 'a'lem' + 'bi' + belirli çoğul etken ortaç 'şâkir' "
 "(ölçüm edim soru, kip INTG 2; 1P 3 · 3MP 4 · 3MS 2; bab I. bab ×4). "
 "Allah lafzı 8. ve 13. sırada (ölçüm allah z=2,14); Rab yok; ölçüm '{{4|esmâ شاكِر 15\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton cemâl' — ölçüm MÜHÜRSÜZ ile uyuşmuyor (araç tanımı farkı; muhur_el hayır — ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 'bi'ş-şâkirîn', kural 'çoğul insan göndergeli → degil' (insan göndergesi; 'l-basîr' cins: gören insan, körün karşıtı; 'ş-şâkirîn' çoğul) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=15 (n z=0,27); ölçüm '{{4|biçim DIKKAT}}' — satır aynen; ölçüm '{{4|fâsıla بٱلشكرين → ن, N sınıfı}}' — satır aynen (6:52 ن → 6:53 ن); "
 "ölçüm '{{4|harf 74 → harf3 70, isaret 4}}' — satır aynen; ölçüm '{{4|dış düğüm 2}}' — satır aynen. "
 "Ölçüm INTG 2: 'e-hâ'ulâ'i' (6. kelime), 'e-leyse' (12. kelime); 've kezâlike' (1.) kelimesindeki 've' REM; 'li-yeqûlû' (5.) kelimesindeki 'li' PRP; 'e-hâ'ulâ'i' (6.) kelimesindeki 'hâ' ATT (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 (lafız 8. / 13. kelime), بعض ×2 ('ba'dahum' 3. / 'bi-ba'din' 4. kelime) (okuma). "
 + T[53] + " (okuma). "
 + cumle(say('say 6:53 3-4', "ba'dahum bi-ba'd", True), say('say 6:53 10-11', "min beyninâ")) + " (--medde 3 ayet: 'beyninâ' yazım farkı ile; harekesiz sayım elif / medde yazımına bağlı). "
 "Ölçüm xref okunmuş 2 ayet. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'ke' + 'zâlike' + PERF + izafet + 'bi' + nekre + 'li' + IMPF + 'e' + 'hâ' + 'zâ' + PERF + lafız + ''alâ' + 'min' + izafet + 'e' + PERF + lafız + 'bi' + 'a'lem' + 'bi' + belirli; "
 "D2 soru; INTG ('e-hâ'ulâ'i' 6. kelime, 'e-leyse' 12. kelime); D3 أله ×2, بعض ×2; D4 1P 3 · 3MP 4 · 3MS 2, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[53] + "; aktör yok (ölçüm); A2 bir kısmın bir kısımla sınanması; lütfedilenlere itiraz sorusu; Allah'ın şükredenleri daha iyi bilmesi; "
 "A3 'e-hâ'ulâ'i menne'llâhu 'aleyhim min beyninâ' (söz içi, 6-11. kelime); "
 "A4 " + BOLUM + "; söz açılır (6. kelime); söz kapanır (11. kelime, ayet içi); şahıs geçişi yok (ayetler arası); edim geçişi yasak → soru (ayetler arası).",
)
out = ['# ── blok 6:50-53 (2026-11-20) ──', 'MEAL12 = {']
for n in range(50, 54):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M12 = {']
for n in range(50, 54):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL12); M.update(M12)']
open('/home/claude/yamalar/metin_6_50_53.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

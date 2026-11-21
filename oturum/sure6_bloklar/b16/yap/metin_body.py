# sûre 6 blok 16 (6:68-70) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b16/say2.txt'
os.environ['OLC'] = '/home/claude/b16/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Ayetler hakkında dalanlar; doğru yol Allah'ın yolu' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 68: "Âyetlerimiz hakkında dalanları gördüğün zaman, başka bir söze dalıncaya kadar onlardan yüz çevir. Şeytan sana unutturursa, hatırlamanın ardından zalim kavimle oturma.",
 69: "Sakınanların üzerine onların hesabından hiçbir şey yoktur; ancak bir hatırlatma vardır; belki sakınırlar.",
 70: "Dinlerini oyun ve oyalanma edinenleri ve dünya hayatının aldattıklarını bırak. Onunla hatırlat ki bir nefis kazandığı yüzünden helâke teslim edilmesin; onun için Allah'tan başka bir dost ve şefaatçi yoktur; her fidyeyi ödese de ondan alınmaz. "
     "Onlar kazandıkları yüzünden helâke teslim edilenlerdir; onlara, inkâr etmekte oldukları yüzünden kaynar sudan bir içecek ve acıklı bir azap vardır.",
}

T = {}
T[68] = ("muhatap 2MS (adsız; 're'eyte', 'fe-a'rid', 'yunsiyenneke', 'fe-lâ taq'ud' — 2., 7., 15. ve 18. kelime); 'yaxûdûne', ''anhum', 'yaxûdû' 3MP (adsız; gönderge 'llezîne' 3. kelime — 4., 8. ve 10. kelime); "
         "konuşan 1P (adsız; 'âyâtinâ' — 6. kelime); 'ğayrih' 3MS (adsız; gönderge 'hadîsin' 12. kelime, 13. kelime); 'yunsiyenneke' 3MS (fiil uyumu; 15. kelime — fail 16. kelime)")
T[69] = ("'yetteqûne' 3MP (adsız; gönderge 'llezîne' 3. kelime, 4. kelime); 'hisâbihim', 'le'allehum', 'yetteqûn' 3MP (adsız; gönderge 6:68 3. kelime — 6., 11. ve 12. kelime)")
T[70] = ("muhatap 2MS (adsız; 've zeri', 've zekkir' — 1. ve 10. kelime); 'ttexazû', 'dînehum' 3MP (adsız; gönderge 'llezîne' 2. kelime — 3. ve 4. kelime); "
         "'ve ğarrathumu' 3FS (fiil uyumu; 7. kelime — fail 8. kelime; nesne zamiri 3MP — 'llezîne' 2. kelimeye döner); 'bih' 3MS (adsız; gönderge 6:69 10. kelime, 11. kelime); 'tubsele' 3FS (fiil uyumu; edilgen; 13. kelime — naib-i faili 14. kelime); "
         "'kesebet', 'lehâ', 'ta'dil', 'minhâ' 3FS (adsız; gönderge 'nefsun' 14. kelime — 16., 18., 26. ve 31. kelime); 'leyse' 3MS (fiil uyumu; 17. kelime — fail 22. kelime); "
         "'yu'xaz' 3MS (adsız; edilgen — naib-i faili zamir, 30. kelime); 'ubsilû' 3MP (adsız; edilgen — naib-i faili zamir, 34. kelime); 'kesebû', 'lehum', 'kânû', 'yekfurûn' 3MP (adsız; gönderge 'ulâ'ike' 32. kelime — 36., 37., 44. ve 45. kelime)")

D = {}
D[68] = ("◇ 've izâ re'eyte'llezîne yaxûdûne fî âyâtinâ fe-a'rid 'anhum hattâ yaxûdû fî hadîsin ğayrih, ve immâ yunsiyenneke'ş-şeytânu fe-lâ taq'ud ba'de'z-zikrâ ma'a'l-qavmi'z-zâlimîn' — "
 "'ve' + 'izâ' + PERF 2MS I. bab + 2MS + 'ellezî' + IMPF 3MP I. bab + 3MP + 'fî' + çoğul 'âye' + 1P + 'fe' + IMPV 2MS IV. bab + ''an' + 3MP + 'hattâ' + IMPF 3MP I. bab + 3MP + 'fî' + nekre 'hadîs' + 'ğayr' + 3MS + "
 "'ve' + 'in' + 'mâ' + IMPF 3MS IV. bab + tekit nûnu + 2MS + belirli 'şeytân' + 'fe' + 'lâ' + IMPF 2MS I. bab + 'ba'd' + belirli 'zikrâ' + 'ma'a' + belirli 'qavm' + belirli çoğul etken ortaç 'zâlim' "
 "(ölçüm edim emir, yasak, şart, kip COND 1 · EMPH 1 · IMPV 1 · PRO 1; 1P 1 · 2MS 5 · 3MP 5 · 3MS 2; bab I. bab ×4 · IV. bab ×2). "
 "Allah lafzı yok; Rab yok; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); ölçüm '{{1|aktör: adlı شَيْطان 16\\. sırada \\(gayb, rol fail\\)}}' — satır aynen. "
 "Ölçüm 'yıldız yok' — satır aynen; n=23 (n z=1,12); ölçüm '{{1|biçim NEHY}}' — satır aynen; ölçüm '{{1|fâsıla ٱلظلمين → ن, N sınıfı}}' — satır aynen (6:67 ن → 6:68 ن); "
 "ölçüm '{{1|simetri \\[6, 3, 9, 2\\]}}' — satır aynen; ölçüm '{{1|harf 104 → harf3 101, isaret 3}}' — satır aynen; ölçüm '{{1|dış düğüm 1}}' — satır aynen. "
 "Ölçüm COND 1: 've immâ' (14. kelime); EMPH 1: 'yunsiyenneke' (15. kelime; tekit nûnu); IMPV 1: 'fe-a'rid' (7. kelime); PRO 1: 'fe-lâ' (17. kelime); 've izâ' (1.) kelimesindeki 've' REM, 'izâ' T; "
 "'fe-a'rid' (7.) ve 'fe-lâ' (17.) kelimelerindeki 'fe' RSLT; 've immâ' (14.) kelimesindeki 've' CONJ, 'mâ' SUP (okuma). "
 "Kök ikilemesi (ölçüm) خوض ×2 ('yaxûdûne' 4. / 'yaxûdû' 10. kelime) (okuma). "
 + T[68] + " (okuma). "
 + cumle(say('say 6:68 9-13', "hattâ yaxûdû fî hadîsin ğayrih", True)) + ' '
 + cumle(say('say 6:68 21-23', "ma'a'l-qavmi'z-zâlimîn")) + ' '
 "Ölçüm xref 4:140 (emsal olarak basıldı). "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'yunsiyenneke' / 'z-zikrâ' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'izâ' + PERF + 'ellezî' + IMPF + 'fî' + izafet + 'fe' + IMPV + ''an' + 'hattâ' + IMPF + 'fî' + nekre + izafet + 've' + 'in' + 'mâ' + IMPF + belirli + 'fe' + 'lâ' + IMPF + izafet + belirli + 'ma'a' + belirli + belirli; "
 "D2 emir, yasak, şart; COND ('ve immâ' 14. kelime), EMPH ('yunsiyenneke' 15. kelime), IMPV ('fe-a'rid' 7. kelime), PRO ('fe-lâ' 17. kelime); D3 خوض ×2; 4:140 eşi; D4 1P 1 · 2MS 5 · 3MP 5 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[68] + "; aktör adlı 'ş-şeytânu' (16. kelime; ölçüm rol fail — 'yunsiyenneke' faili); A2 âyetler hakkında dalanlardan yüz çevirme; başka söze dalıncaya kadar bekleme; unutturulursa hatırlayınca zalimlerle oturmama; "
 "A3 —; "
 "A4 " + BOLUM + "; şart → cevap (ayet içi; zaman şartı 'izâ' 1. kelime: 've izâ re'eyte'llezîne yaxûdûne fî âyâtinâ' / 'fe-a'rid 'anhum' (7. kelime)); şart → cevap (ayet içi; COND 'in' 14. kelime: 've immâ yunsiyenneke'ş-şeytân' / 'fe-lâ taq'ud ba'de'z-zikrâ' (17. kelime)); şahıs geçişi yok (ayetler arası); edim geçişi haber → emir, yasak, şart (ayetler arası); "
 "şahıs sayısında beraberlik (2MS 5 / 3MP 5 · 3MS 2 — ölçüm baskın 2); bölüm açılışı.",
)

D[69] = ("◇ 've mâ 'ale'llezîne yetteqûne min hisâbihim min şey'in ve lâkin zikrâ le'allehum yetteqûn' — "
 "'ve' + 'mâ' + ''alâ' + 'ellezî' + IMPF 3MP VIII. bab + 3MP + 'min' + mastar 'hisâb' + 3MP + 'min' + nekre 'şey'' + 've' + 'lâkin' + 'zikrâ' + 'le'alle' + 3MP + IMPF 3MP VIII. bab "
 "(ölçüm edim haber, kip NEG 1; 3MP 6; bab VIII. bab ×2). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=12 (n z=-0,04); ölçüm '{{2|fâsıla يتقون → ن, N sınıfı}}' — satır aynen (6:68 ن → 6:69 ن); "
 "ölçüm '{{2|simetri \\[4, 1, 9, 1\\]}}' — satır aynen; ölçüm '{{2|harf 48 → harf3 47, isaret 1}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm NEG 1: 've mâ' (1. kelime); 've mâ' (1.) ve 've lâkin' (9.) kelimelerindeki 've' REM; 'lâkin' AMD; 'le'allehum' (11.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) وقي ×2 ('yetteqûne' 4. / 'yetteqûn' 12. kelime) (okuma). "
 + T[69] + " (okuma). "
 + cumle(say('say 6:69 5-8', "min hisâbihim min şey'", True), say('dizi 6 69 5 8', "min hisâb min şey'")) + ' '
 + cumle(say('say 6:69 11-12', "le'allehum yetteqûn")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: '_ hisâb _ şey'' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'mâ' + ''alâ' + 'ellezî' + IMPF + 'min' + izafet + 'min' + nekre + 've' + 'lâkin' + 'zikrâ' + 'le'alle' + IMPF; "
 "D2 haber; NEG ('ve mâ' 1. kelime); D3 وقي ×2; D4 3MP 6, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[69] + "; aktör yok (ölçüm); A2 sakınanlara dalanların hesabından bir şey düşmemesi; hatırlatma; sakınma umudu; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 2 → 3 (ayetler arası); edim geçişi emir, yasak, şart → haber (ayetler arası).",
)

D[70] = ("◇ 've zeri'llezîne'ttexazû dînehum la'iben ve lahven ve ğarrathumu'l-hayâtu'd-dunyâ ve zekkir bihî en tubsele nefsun bimâ kesebet leyse lehâ min dûni'llâhi veliyyun ve lâ şefî'un ve in ta'dil kulle 'adlin lâ yu'xaz minhâ, "
 "ulâ'ike'llezîne ubsilû bimâ kesebû lehum şarâbun min hamîmin ve 'azâbun alîmun bimâ kânû yekfurûn' — "
 "'ve' + IMPV 2MS I. bab + 'ellezî' + PERF 3MP VIII. bab + 3MP + 'dîn' + 3MP + nekre 'la'ib' + 've' + nekre 'lahv' + 've' + PERF 3FS I. bab + 3MP + belirli 'hayât' + belirli 'dunyâ' + 've' + IMPV 2MS II. bab + 'bi' + 3MS + "
 "'en' + edilgen IMPF 3FS IV. bab + nekre 'nefs' + 'bi' + 'mâ' + PERF 3FS I. bab + PERF 3MS I. bab + 'li' + 3FS + 'min' + 'dûn' + lafız + nekre 'veliyy' + 've' + 'lâ' + nekre 'şefî'' + "
 "'ve' + 'in' + IMPF 3FS I. bab + 'kull' + nekre ''adl' + 'lâ' + edilgen IMPF 3MS I. bab + 'min' + 3FS + 'ulâ'i' + 'ke' + 'ellezî' + edilgen PERF 3MP IV. bab + 3MP + 'bi' + 'mâ' + PERF 3MP I. bab + 3MP + "
 "'li' + 3MP + nekre 'şarâb' + 'min' + nekre 'hamîm' + 've' + nekre ''azâb' + nekre 'alîm' + 'bi' + 'mâ' + PERF 3MP I. bab + 3MP + IMPF 3MP I. bab + 3MP "
 "(ölçüm edim emir, şart, kip COND 1 · IMPV 2 · NEG 2; 2MS 2 · 3FS 6 · 3MP 13 · 3MS 3; bab I. bab ×9 · II. bab ×1 · IV. bab ×2 · VIII. bab ×1). "
 "Allah lafzı 21. sırada (ölçüm allah z=-0,08); Rab yok; ölçüm '{{3|esmâ وَلِيّ 22\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor); "
 "esma_el kaydı 'degil' — 'min dûni'llâhi veliyyun', kural 'esmâ adı esmâ dışı göndergeyle → degil' (esmâ dışı gönderge) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=45 (n z=3,46); ölçüm '{{3|EDİLGEN 3/13 fiil, pas z=0,99}}' — satır aynen; "
 "ölçüm '{{3|HAPAKS: بسل}}' — satır aynen (kök bu blokta tabloya eklendi); ölçüm '{{3|hapaks z=3,28}}' — satır aynen; ölçüm '{{3|fâsıla يكفرون → ن, N sınıfı}}' — satır aynen (6:69 ن → 6:70 ن); "
 "ölçüm '{{3|simetri \\[6, 11, 31, 2\\]}}' — satır aynen; ölçüm '{{3|harf 193 → harf3 175, isaret 18}}' — satır aynen; ölçüm '{{3|dış düğüm 3}}' — satır aynen. "
 "Ölçüm COND 1: 've in' (25. kelime); IMPV 2: 've zeri' (1. kelime), 've zekkir' (10. kelime); NEG 2: 've lâ' (23. kelime), 'lâ' (29. kelime); 've zeri' (1.) ve 've in' (25.) kelimelerindeki 've' REM; "
 "'ve lahven' (6.), 've ğarrathumu' (7.), 've zekkir' (10.), 've lâ' (23.) ve 've 'azâbun' (41.) kelimelerindeki 've' CONJ; 'en' (12.) SUB; 'ulâ'ike' (32.) DEM (okuma). "
 "Kök ikilemesi (ölçüm) أخذ ×2 ('ttexazû' 3. / 'yu'xaz' 30. kelime), بسل ×2 ('tubsele' 13. / 'ubsilû' 34. kelime), عدل ×2 ('ta'dil' 26. / ''adlin' 28. kelime), كسب ×2 ('kesebet' 16. / 'kesebû' 36. kelime) (okuma). "
 + T[70] + " (okuma). "
 + cumle(say('say 6:70 38-42', "şarâbun min hamîmin ve 'azâbun alîm", True), say('dizi 6 70 38 42', "şarâb min hamîm 'azâb alîm"), say('say 6:70 38-45', "şarâbun min hamîmin ve 'azâbun alîmun bimâ kânû yekfurûn")) + ' '
 + cumle(say('say 6:70 43-45', "bimâ kânû yekfurûn"), say('say 6:70 22-24', "veliyyun ve lâ şefî'"), say('say 6:70 7-9', "ğarrathumu'l-hayâtu'd-dunyâ")) + ' '
 "Ölçüm xref 10:4 (emsal olarak basıldı) ve okunmuş 2 ayet. "
 "Ölçüm nakarat3 kalıpları: '_ dûn allâh' süzgeç GEÇER, 'bi-mâ kâne kefera' süzgeç GEÇMEZ, 'veliyy _ şefî'' süzgeç GEÇMEZ, 'ğarra hayât dunyâ' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'la'iben ve lahven' / 'dînehum'; 'şarâbun min hamîm' / ''azâbun alîm' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 —; B4 'l-hayâtu' (8. kelime).",
 "◈D — D1 've' + IMPV + 'ellezî' + PERF + izafet + nekre + 've' + nekre + 've' + PERF + belirli + belirli + 've' + IMPV + 'bi' + 'en' + IMPF + nekre + 'bi' + 'mâ' + PERF + PERF + 'li' + 'min' + izafet + nekre + 've' + 'lâ' + nekre + "
 "'ve' + 'in' + IMPF + izafet + nekre + 'lâ' + IMPF + 'min' + 'ulâ'i' + 'ellezî' + PERF + 'bi' + 'mâ' + PERF + 'li' + nekre + 'min' + nekre + 've' + nekre + nekre + 'bi' + 'mâ' + PERF + IMPF; "
 "D2 emir, şart; COND ('ve in' 25. kelime), IMPV ('ve zeri' 1. kelime, 've zekkir' 10. kelime), NEG ('ve lâ' 23. kelime, 'lâ' 29. kelime); D3 أخذ ×2, بسل ×2, عدل ×2, كسب ×2; 10:4 eşi; D4 2MS 2 · 3FS 6 · 3MP 13 · 3MS 3, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[70] + "; aktör yok (ölçüm); A2 dinini oyun ve eğlence edinenleri bırakma; onunla hatırlatma; kazandığı yüzünden helâke teslim edilme; Allah'tan başka dost ve şefaatçinin yokluğu; fidyenin alınmaması; kaynar su ve acıklı azap; "
 "A3 —; "
 "A4 " + BOLUM + "; şart → cevap (ayet içi; COND 'in' 25. kelime: 've in ta'dil kulle 'adl' / 'lâ yu'xaz minhâ' (29. kelime)); şahıs geçişi yok (ayetler arası); edim geçişi haber → emir, şart (ayetler arası).",
)

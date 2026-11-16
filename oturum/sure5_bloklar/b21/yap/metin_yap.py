# blok 21 (5:64-66) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b21/say2.txt'
os.environ['OLC'] = '/home/claude/b21/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Kitap ehlinin tutumu; bağlı el sözü; Tevrat ve İncil'i ayakta tutma' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 64: "Yahudiler: Allah'ın eli bağlıdır, dediler. Elleri bağlandı ve söyledikleri yüzünden lanetlendiler. Bilakis O'nun iki eli açıktır; dilediği gibi infak eder. Andolsun, Rabbinden sana indirilen, onlardan çoğunun azgınlığını ve küfrünü artıracaktır. Aralarına kıyamet gününe kadar düşmanlık ve öfke bıraktık. Savaş için her ateş yaktıklarında Allah onu söndürdü. Yeryüzünde bozgunculuk için koşarlar; Allah bozguncuları sevmez.",
 65: "Eğer Kitap ehli iman etseydi ve sakınsaydı, kötülüklerini onlardan mutlaka örterdik ve onları mutlaka nimet cennetlerine sokardık.",
 66: "Eğer onlar Tevrat'ı, İncil'i ve Rablerinden kendilerine indirileni ayakta tutsalardı, elbette üstlerinden ve ayaklarının altından yerlerdi. Onlardan orta yolu tutan bir ümmet vardır; onlardan çoğunun yaptıkları ne kötüdür!",
}

T64 = ("'qâlet' 3FS (adsız; gönderge 'l-yehûdu', 1. kelime); 'l-yehûdu' ('qâlet' faili; adlı cins, 2. kelime); 'ğullet' 3FS (adsız; gönderge 'eydîhim', 6. kelime); Allah (lafız; 4., 39. ve 44. kelime); 'eydîhim' 3MP (adsız; gönderge Yahudiler, 7. kelime); 'lu'inû' naib-i faili 3MP (adsız; edilgen, 8. kelime); 'qâlû' faili 3MP (adsız; 10. kelime); "
       "'yedâhu' 3MS (adsız; gönderge lafız, 12. kelime); 'yunfiqu' ve 'yeşâ'u' faili 3MS (adsız; gönderge lafız, 14. ve 16. kelime); 'yezîdenne' faili 3MS (adsız; gönderge 'mâ', 17. kelime); 'kesîran' (nekre; 18. kelime); 'minhum' 3MP (adsız; 19. kelime); 'unzile' naib-i faili 3MS (adsız; edilgen, 21. kelime); "
       "muhatap 2MS (adsız; 'ileyke' 22., 'rabbike' 24. kelime); Rab ('rabbike', 24. kelime); konuşan 1P (adsız; 'elqaynâ' 27. kelime); 'beynehumu' 3MP (adsız; 28. kelime); 'evqadû' faili 3MP (adsız; 35. kelime); 'atfa'e' 3MS (adsız; gönderge lafız, 38. kelime); 'atfa'ehâ' 3FS (adsız; gönderge 'nâran', 38. kelime); "
       "'yes'avne' faili 3MP (adsız; 40. kelime); 'yuhibbu' faili 3MS (adsız; gönderge lafız, 46. kelime); 'l-mufsidîn' (47. kelime)")
T65 = ("'ehle'l-kitâbi' ('âmenû' faili; 3-4. kelime); 'âmenû' ve 'tteqav' faili 3MP (adsız; 5. ve 6. kelime); konuşan 1P (adsız; 'keffernâ' 7., 'edxalnâhum' 10. kelime); ''anhum' 3MP (adsız; 8. kelime); 'seyyi'âtihim' 3MP (adsız; 9. kelime); 'edxalnâhum' mef'ûlü 3MP (adsız; 10. kelime)")
T66 = ("'ennehum' 3MP (adsız; gönderge Kitap ehli, 2. kelime); 'eqâmu' faili 3MP (adsız; 3. kelime); 't-tevrâte' ve 'l-incîle' (adlı kitaplar; 4-5. kelime); 'unzile' naib-i faili 3MS (adsız; edilgen, 7. kelime); 'ileyhim' 3MP (adsız; 8. kelime); Rab ('rabbihim', 10. kelime); 'rabbihim' 3MP (adsız; 10. kelime); "
       "'ekelû' faili 3MP (adsız; 11. kelime); 'fevqihim' ve 'ercülihim' 3MP (adsız; 13. ve 16. kelime); 'minhum' 3MP (adsız; 17. ve 21. kelime); 'ummetun' (nekre; 18. kelime); 'kesîrun' (nekre; 20. kelime); 'sâ'e' faili 3MS (adsız; gönderge 'mâ', 22. kelime); 'ya'melûn' faili 3MP (adsız; 24. kelime)")

D = {}
D[64] = ("◇ 've qâleti'l-yehûdu yedu'llâhi mağlûletun ğullet eydîhim ve lu'inû bi-mâ qâlû bel yedâhu mebsûtatâni yunfiqu keyfe yeşâ'u ve le-yezîdenne kesîran minhum mâ unzile ileyke min rabbike tuğyânen ve kufran ve elqaynâ beynehumu'l-'adâvete ve'l-bağdâ'e ilâ yevmi'l-qiyâmeti kullemâ evqadû nâran li'l-harbi atfa'ehâ'llâhu ve yes'avne fi'l-ardi fesâden ve'llâhu lâ yuhibbu'l-mufsidîn' — "
 "'ve' + PERF 3FS I. bab + belirli çoğul 'yehûd' + 'yed' + lafız + nekre edilgen ortaç 'mağlûle' + edilgen PERF 3FS I. bab + çoğul 'yed' + 3MP + 've' + edilgen PERF 3MP I. bab + 'bi' + 'mâ' + PERF 3MP I. bab + 'bel' + ikil 'yed' + 3MS + ikil edilgen ortaç 'mebsûtatân' + IMPF 3MS IV. bab + 'keyfe' + IMPF 3MS I. bab + "
 "'ve' + 'le' + IMPF 3MS I. bab + te'kid nûnu + nekre 'kesîr' + 'min' + 3MP + 'mâ' + edilgen PERF 3MS IV. bab + 'ilâ' + 2MS + 'min' + 'rabb' + 2MS + nekre masdar 'tuğyân' + 've' + nekre 'kufr' + 've' + PERF 1P IV. bab + 'beyn' + 3MP + belirli ''adâve' + 've' + belirli 'bağdâ'' + 'ilâ' + 'yevm' + belirli 'qiyâme' + "
 "'kullemâ' + PERF 3MP IV. bab + nekre 'nâr' + 'li' + belirli 'harb' + PERF 3MS IV. bab + 3FS + lafız + 've' + IMPF 3MP I. bab + 'fî' + belirli 'ard' + nekre 'fesâd' + 've' + lafız + 'lâ' + IMPF 3MS IV. bab + belirli çoğul ortaç 'mufsid' "
 "(ölçüm edim haber, kip EMPH 2 · NEG 1, biçim IDRAB; 1P 2 · 2MS 2 · 3FS 3 · 3MP 11 · 3MS 7; bab I. bab ×7 · IV. bab ×6; EDİLGEN 3/13 fiil). "
 "Allah lafzı 4., 39. ve 44. sırada (ölçüm allah z=0,75); ölçüm '{{1|رَبّ 24\\. sırada \\(rab z=0,13\\)}}' — satır aynen ('rabbike', Rab adı); esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); ölçüm aktör '{{1|adlı يَهُود 2\\. sırada \\(cins, rol fail\\+konusan\\)}}' — satır aynen. "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=47 (n z=3,67); ölçüm '{{1|fâsıla ٱلمفسدين → ن, N sınıfı}}' — satır aynen; ölçüm '{{1|EDİLGEN 3/13 fiil, pas z=0,99}}' — satır aynen ('ğullet' 6., 'lu'inû' 8., 'unzile' 21. kelime); ölçüm '{{1|sayı işareti \\S+}}' — satır aynen ('kesîran' 18. kelime); "
 "ölçüm '{{1|simetri \\[3, 1, 10, 1\\]}}' — satır aynen; ölçüm '{{1|harf 230 → harf3 215, isaret 15}}' — satır aynen; ölçüm '{{1|dış düğüm 2}}' — satır aynen. "
 "Ölçüm EMPH 2: 'le' ve te'kid nûnu ('le-yezîdenne' 17. kelime); NEG 1: 'lâ' (45. kelime); morph RET 'bel' (11. kelime), T 'kullemâ' (34. kelime); 've' 1., 17., 27., 40. ve 44. kelimede REM, 8., 26. ve 30. kelimede CONJ (okuma). "
 "Kök ikilemesi (ölçüm) أله ×3 (lafız 4., 39., 44. kelime), غلل ×2 ('mağlûle' 5. / 'ğullet' 6. kelime), فسد ×2 ('fesâden' 43. / 'l-mufsidîn' 47. kelime), قول ×2 ('qâlet' 1. / 'qâlû' 10. kelime), يدي ×3 ('yedu' 3., 'eydîhim' 7., 'yedâhu' 12. kelime) (okuma). "
 + T64 + " (okuma). "
 + cumle(say('say 5:64 1-2', "ve qâleti'l-yehûd", True), say('say 5:64 2-5', "l-yehûdu yedu'llâhi mağlûle"), say('say 5:64 3-5', "yedu'llâhi mağlûle"), say('say 5:64 6-7', "ğullet eydîhim")) + ' '
 + cumle(say('say 5:64 8-10 --on', "ve lu'inû bi-mâ qâlû", True), say('say 5:64 9-10', "bi-mâ qâlû"), say('say 5:64 11-13', "bel yedâhu mebsûtatân"), say('say 5:64 12-13', "yedâhu mebsûtatân"), say('lem 5:64:13', "mebsûtatân"), say('say 5:64 14-16', "yunfiqu keyfe yeşâ'")) + ' '
 + cumle(say('say 5:64 17-19 --on', "ve le-yezîdenne kesîran minhum", True), say('say 5:64 18-19', "kesîran minhum"), say('say 5:64 20-24', "mâ unzile ileyke min rabbik"), say('dizi 5 64 20 24', "mâ enzele ilâ min rabb"), say('say 5:64 21-24', "unzile ileyke min rabbik"),
         say('dizi 5 64 17 26', "zâde kesîr min mâ enzele ilâ min rabb tuğyân kufr"), say('say 5:64 25-26', "tuğyânen ve kufran")) + ' '
 + cumle(say('say 5:64 27-30 --on', "ve elqaynâ beynehumu'l-'adâvete ve'l-bağdâ'", True), say('say 5:64 28-30', "beynehumu'l-'adâvete ve'l-bağdâ'"), say('dizi 5 64 28 30', "beyn 'adâve bağdâ'"), say('say 5:64 28-33', "beynehumu'l-'adâvete ve'l-bağdâ'e ilâ yevmi'l-qiyâme"),
         say('dizi 5 64 28 33', "beyn 'adâve bağdâ' ilâ yevm qiyâme"), say('say 5:64 31-33', "ilâ yevmi'l-qiyâme")) + ' '
 + cumle(say('say 5:64 34-36', "kullemâ evqadû nâran", True), say('lem 5:64:35', "evqadu"), say('say 5:64 36-37', "nâran li'l-harb"), say('say 5:64 38-39', "atfa'ehâ'llâh")) + ' '
 + cumle(say('say 5:64 40-43 --on', "ve yes'avne fi'l-ardi fesâden", True), say('say 5:64 41-43', "fi'l-ardi fesâden"), say('dizi 5 64 40 43', "se'â fî ard fesâd"), say('say 5:64 44-47 --on', "ve'llâhu lâ yuhibbu'l-mufsidîn"), say('say 5:64 45-47', "lâ yuhibbu'l-mufsidîn"),
         say('dizi 5 64 44 46', "allâh lâ ahbeb"), say('lem 5:64:46', "ahbeb")) + ' '
 "Ölçüm xref 28:77 (emsal olarak basıldı), 5:14 ve 60:4 (basılmış) ve okunmuş ve henüz okunmamış başka ayetler. "
 "Ölçüm nakarat3 kalıpları: 'le-yezîdenne kesîran minhum mâ unzile ileyke min rabbike tuğyânen ve kufran', 'beynehumu'l-'adâvete ve'l-bağdâ'e ilâ yevmi'l-qiyâme', 'mâ unzile ileyke min rabbik', 'yes'avne fi'l-ardi fesâden' ve 'beynehumu'l-'adâvete ve'l-bağdâ'' süzgeç GEÇER; 've'llâhu lâ yuhibbu' GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'yedu'llâhi mağlûle' / 'yedâhu mebsûtatân' — ayetler arası: yok.",
 "◈K — K1 'l-ardi' (42. kelime); K2 'yevmi' (32. kelime).",
 "◈B — B1 —; B2 —; B3 'yedu' (3. kelime), 'eydîhim' (7. kelime), 'yedâhu' (12. kelime); B4 —.",
 "◈D — D1 've' + PERF + belirli + izafet + lafız + nekre + PERF + izafet + 've' + PERF + 'bi' + 'mâ' + PERF + 'bel' + izafet + nekre + IMPF + 'keyfe' + IMPF + 've' + 'le' + IMPF + nekre + 'min' + 'mâ' + PERF + 'ilâ' + 'min' + izafet + nekre + 've' + nekre + "
 "'ve' + PERF + 'beyn' + belirli + 've' + belirli + 'ilâ' + izafet + belirli + 'kullemâ' + PERF + nekre + 'li' + belirli + PERF + lafız + 've' + IMPF + 'fî' + belirli + nekre + 've' + lafız + 'lâ' + IMPF + belirli; "
 "D2 haber, EMPH ('le-yezîdenne' 17. kelime), NEG ('lâ' 45. kelime), biçim IDRAB ('bel' 11. kelime); D3 أله ×3, غلل ×2, فسد ×2, قول ×2, يدي ×3; 28:77 eşi; D4 1P 2 · 2MS 2 · 3FS 3 · 3MP 11 · 3MS 7, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T64 + "; aktör Yahudiler (ölçüm); A2 bağlı el sözü; lanet; açık el ve infak; indirilenin artırdığı azgınlık ve küfür; düşmanlık ve öfke; savaş ateşi ve söndürülmesi; bozgunculuk; "
 "A3 'yedu'llâhi mağlûle' ('qâlet' sözü, 3-5. kelime); "
 "A4 " + BOLUM + "; edim geçişi yok (haber); şahıs geçişi yok.",
)

D[65] = ("◇ 've lev enne ehle'l-kitâbi âmenû ve'tteqav le-keffernâ 'anhum seyyi'âtihim ve le-edxalnâhum cennâti'n-na'îm' — "
 "'ve' + 'lev' + 'enne' + 'ehl' + belirli 'kitâb' + PERF 3MP IV. bab + 've' + PERF 3MP VIII. bab + 'le' + PERF 1P II. bab + ''an' + 3MP + çoğul 'seyyi'e' + 3MP + 've' + 'le' + PERF 1P IV. bab + 3MP + çoğul 'cenne' + belirli 'na'îm' "
 "(ölçüm edim şart, kip COND 1 · EMPH 2; 1P 4 · 3MP 7; bab II. bab ×1 · IV. bab ×2 · VIII. bab ×1). "
 "Lafız yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=12 (n z=-0,04); ölçüm '{{2|fâsıla ٱلنعيم → م, N sınıfı}}' — satır aynen; ölçüm '{{2|harf 62 → harf3 60, isaret 2}}' — satır aynen; ölçüm '{{2|dış düğüm 4}}' — satır aynen. "
 "Ölçüm COND 1: 'lev' (1. kelime); EMPH 2: 'le' (7. ve 10. kelime); 've lev' (1.)'deki 've' REM, 've'tteqav' (6.) ve 've le-edxalnâhum' (10.)'daki 've' CONJ (okuma). "
 + T65 + " (okuma). "
 + cumle(say('say 5:65 1-4 --on', "ve lev enne ehle'l-kitâb", True), say('say 5:65 2-4', "enne ehle'l-kitâb"), say('say 5:65 3-5', "ehle'l-kitâbi âmenû"), say('say 5:65 5-6', "âmenû ve'tteqav")) + ' '
 + cumle(say('say 5:65 7-9 --on', "le-keffernâ 'anhum seyyi'âtihim", True), say('say 5:65 8-9', "'anhum seyyi'âtihim"), say('say 5:65 10-12 --on', "ve le-edxalnâhum cennâti'n-na'îm"), say('say 5:65 11-12', "cennâti'n-na'îm"), say('dizi 5 65 9 11', "seyyi'e udxile cenne")) + ' '
 "Ölçüm xref 70:38 (emsal olarak basıldı) ve okunmuş başka ayetler. "
 "Ölçüm nakarat3 kalıpları: 'seyyi'âtihim ve le-edxalnâhum cennât' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'lev' + 'enne' + izafet + belirli + PERF + 've' + PERF + 'le' + PERF + ''an' + izafet + 've' + 'le' + PERF + izafet + belirli; "
 "D2 şart, COND ('lev' 1. kelime), EMPH ('le' 7. ve 10. kelime); D3 ikileme yok; 70:38 eşi; D4 1P 4 · 3MP 7, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T65 + "; aktör yok (ölçüm); A2 iman ve sakınma şartı; kötülüklerin örtülmesi; nimet cennetleri; A3 —; "
 "A4 " + BOLUM + "; edim geçişi haber → şart (ayetler arası); şart → cevap (ayet içi; COND 'lev' 1. kelime: 've lev enne ehle'l-kitâbi âmenû ve'tteqav' / 'le-keffernâ 'anhum seyyi'âtihim' (7. kelime)); şahıs geçişi yok.",
)

D[66] = ("◇ 've lev ennehum eqâmu't-tevrâte ve'l-incîle ve mâ unzile ileyhim min rabbihim le-ekelû min fevqihim ve min tahti ercülihim minhum ummetun muqtasidetun ve kesîrun minhum sâ'e mâ ya'melûn' — "
 "'ve' + 'lev' + 'enne' + 3MP + PERF 3MP IV. bab + belirli 'tevrâ' + 've' + belirli 'incîl' + 've' + 'mâ' + edilgen PERF 3MS IV. bab + 'ilâ' + 3MP + 'min' + 'rabb' + 3MP + 'le' + PERF 3MP I. bab + 'min' + 'fevq' + 3MP + 've' + 'min' + 'taht' + çoğul 'ricl' + 3MP + 'min' + 3MP + nekre 'umme' + nekre ortaç 'muqtaside' + 've' + nekre 'kesîr' + 'min' + 3MP + PERF 3MS I. bab + 'mâ' + IMPF 3MP I. bab "
 "(ölçüm edim şart, kip COND 1 · EMPH 1; 3MP 13 · 3MS 2; bab I. bab ×3 · IV. bab ×2; EDİLGEN 1/5 fiil). "
 "Lafız yok; ölçüm '{{3|رَبّ 10\\. sırada \\(rab z=0,57\\)}}' — satır aynen ('rabbihim', Rab adı); esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); ölçüm aktör '{{3|adlı تَوْراة 4\\. sırada \\(kitab, rol meful\\)}}' ve '{{3|adlı إِنجِيل 5\\. sırada \\(kitab, rol meful\\)}}' — satır aynen. "
 "Ölçüm 'yıldız yok' — satır aynen; n=24 (n z=1,23); ölçüm '{{3|fâsıla يعملون → ن, N sınıfı}}' — satır aynen; ölçüm '{{3|EDİLGEN 1/5 fiil, pas z=0,81}}' — satır aynen ('unzile' 7. kelime); ölçüm '{{3|sayı işareti \\S+}}' — satır aynen ('kesîrun' 20. kelime); "
 "ölçüm '{{3|simetri \\[4, 1, 5, 1\\]}}' — satır aynen; ölçüm '{{3|harf 111 → harf3 104, isaret 7}}' — satır aynen; ölçüm '{{3|dış düğüm 2}}' — satır aynen. "
 "Ölçüm COND 1: 'lev' (1. kelime); EMPH 1: 'le' (11. kelime); 've lev' (1.)'deki 've' REM, 've'l-incîle' (5.), 've mâ' (6.), 've min' (14.) ve 've kesîrun' (20.)'daki 've' CONJ (okuma). "
 + T66 + " (okuma). "
 + cumle(say('say 5:66 1-3 --on', "ve lev ennehum eqâmû", True), say('say 5:66 2-3', "ennehum eqâmû"), say('say 5:66 3-5', "eqâmu't-tevrâte ve'l-incîl"), say('say 5:66 4-5', "t-tevrâte ve'l-incîl"), say('dizi 5 66 3 7', "eqâme tevrâ incîl mâ enzele")) + ' '
 + cumle(say('say 5:66 6-10 --on', "ve mâ unzile ileyhim min rabbihim", True), say('say 5:66 7-10', "unzile ileyhim min rabbihim"), say('say 5:66 11-13 --on', "le-ekelû min fevqihim"), say('say 5:66 12-16', "min fevqihim ve min tahti ercülihim"), say('say 5:66 13-16', "fevqihim ve min tahti ercülihim")) + ' '
 + cumle(say('say 5:66 17-19', "minhum ummetun muqtaside", True), say('say 5:66 18-19', "ummetun muqtaside"), say('say 5:66 20-21 --on', "ve kesîrun minhum"), say('say 5:66 22-24', "sâ'e mâ ya'melûn"), say('say 5:66 22-23', "sâ'e mâ")) + ' '
 "Ölçüm xref 29:55 (emsal olarak basıldı) ve okunmuş başka ayetler. "
 "Ölçüm nakarat3 kalıpları: 'eqâmu't-tevrâte ve'l-incîle ve mâ unzile' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'min fevqihim' / 'min tahti ercülihim'; 'ummetun muqtaside' / 'kesîrun minhum sâ'e' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'lev' + 'enne' + PERF + belirli + 've' + belirli + 've' + 'mâ' + PERF + 'ilâ' + 'min' + izafet + 'le' + PERF + 'min' + izafet + 've' + 'min' + izafet + izafet + 'min' + nekre + nekre + 've' + nekre + 'min' + PERF + 'mâ' + IMPF; "
 "D2 şart, COND ('lev' 1. kelime), EMPH ('le' 11. kelime); D3 ikileme yok; 29:55 eşi; D4 3MP 13 · 3MS 2, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T66 + "; aktör Tevrat ve İncil (ölçüm); A2 Tevrat ve İncil'i ayakta tutma şartı; üstten ve alttan rızık; orta yolu tutan ümmet; yapılanın kötülüğü; A3 —; "
 "A4 " + BOLUM + "; edim geçişi yok (şart); şart → cevap (ayet içi; COND 'lev' 1. kelime: 've lev ennehum eqâmu't-tevrâte' / 'le-ekelû min fevqihim' (11. kelime)); şahıs geçişi yok.",
)

out = ['# ── blok 5:64-66 (2026-11-16) ──', 'MEAL21 = {']
for n in range(64, 67):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M21 = {']
for n in range(64, 67):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL21); M.update(M21)']
open('/home/claude/yamalar/metin_5_64_66.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

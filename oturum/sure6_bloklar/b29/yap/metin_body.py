# sûre 6 blok 29 (6:122-125) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b29/say2.txt'
os.environ['OLC'] = '/home/claude/b29/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Ölüyken dirilen; cin ve insan toplulukları' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 122: "Ölüyken dirilttiğimiz ve kendisine onunla insanlar içinde yürüdüğü bir nur verdiğimiz kimse, karanlıklar içinde olup oradan çıkamayan kimsenin durumu gibi midir? Böylece kâfirlere yapmakta oldukları süslü gösterildi.",
 123: "Böylece her kasabada, orada tuzak kursunlar diye, suçlularının büyüklerini kıldık. Onlar ancak kendilerine tuzak kurarlar ve farkında olmazlar.",
 124: "Kendilerine bir âyet geldiğinde, Allah'ın elçilerine verilenin benzeri bize de verilinceye kadar asla inanmayacağız dediler. Allah, elçiliğini nereye koyacağını daha iyi bilendir. Suç işleyenlere, tuzak kurmakta olduklarından dolayı Allah katında bir aşağılanma ve şiddetli bir azap erişecektir.",
 125: "Allah kimi doğru yola iletmek isterse onun göğsünü İslâm'a açar; kimi de saptırmak isterse onun göğsünü, göğe yükseliyormuş gibi dar ve sıkıntılı kılar. Allah, inanmayanların üzerine pisliği böyle kılar.",
}

T = {}
T[122] = ("'kâne' 3MS (adsız; gönderge 'e-ve-men' 1. kelime, 2. kelime); konuşan 1P (adsız; 'fe-ahyeynâhu', 've ce'alnâ' — 4. ve 5. kelime); "
          "'fe-ahyeynâhu', 'lehû' 3MS (adsız; gönderge 'e-ve-men' 1. kelime — 4. ve 6. kelime); 'yemşî' 3MS (gizli zamir, adsız; 8. kelime — fail 8. kelime içi gizli zamir, gönderge 'e-ve-men' 1. kelime; 'meseluhû' 13. kelime ayrı cümlenin mübtedası); 'bihî' 3MS (adsız; gönderge 'nûran' 7. kelime, 9. kelime); "
          "'meseluhû', 'leyse' 3MS (adsız; gönderge 'ke-men' 12. kelime — 13. ve 16. kelime); 'minhâ' 3FS (adsız; gönderge 'z-zulumâti' 15. kelime, 18. kelime); "
          "'zuyyine' 3MS (fiil uyumu; 20. kelime — edilgen; naib-i faili 'mâ' (22. kelime)); 'kânû', 'ya'melûn' 3MP (adsız; gönderge 'li'l-kâfirîne' 21. kelime — 23. ve 24. kelime)")
T[123] = ("konuşan 1P (adsız; 'ce'alnâ' — 2. kelime); 'mucrimîhâ', 'fîhâ' 3FS (adsız; gönderge 'qaryetin' 5. kelime — 7. ve 9. kelime); "
          "'li-yemkurû', 'yemkurûne', 'bi-enfusihim', 'yeş'urûn' 3MP (adsız; gönderge 'ekâbira' 6. kelime — 8., 11., 13. ve 15. kelime)")
T[124] = ("'câ'ethum' 3FS (fiil uyumu; 2. kelime — fail 3. kelime); 'câ'ethum', 'qâlû' 3MP (adsız; gönderge 6:123 6. kelime — 2. ve 4. kelime); konuşan 1P (adsız; söz içi; 'nu'mine' — 6. kelime); "
          "konuşan 1P (adsız; söz içi; 'nu'tâ' — 8. kelime; edilgen; naib-i faili konuşan zamiri); 'ûtiye' 3MS (fiil uyumu; söz içi; 11. kelime — edilgen; naib-i faili 'rusulu' (12. kelime)); "
          "'yec'alu', 'risâletehû' 3MS (adsız; gönderge 'llâhu' 14. kelime — 17. ve 18. kelime); 'se-yusîbu' 3MS (fiil uyumu; 19. kelime — fail 22. kelime); "
          "'ecramû', 'kânû', 'yemkurûn' 3MP (adsız; gönderge 'llezîne' 20. kelime — 21., 28. ve 29. kelime)")
T[125] = ("'yuridi' 3MS (fiil uyumu; 2. kelime — fail 3. kelime); 'yehdiyehû', 'yeşrah' 3MS (adsız; gönderge 'llâhu' 3. kelime — 5. ve 6. kelime); "
          "'yehdiyehû', 'sadrahû' 3MS eki (adsız; gönderge 'fe-men' 1. kelime — 5. ve 7. kelime); 'yurid', 'yudillehû', 'yec'al' 3MS (adsız; gönderge 'llâhu' 3. kelime — 10., 12. ve 13. kelime); "
          "'yudillehû', 'sadrahû' 3MS eki (adsız; gönderge 've men' 9. kelime — 12. ve 14. kelime); 'yassa'adu' 3MS (adsız; gönderge 've men' 9. kelime, 18. kelime); "
          "'yec'alu' 3MS (fiil uyumu; 22. kelime — fail 23. kelime); 'yu'minûn' 3MP (adsız; gönderge 'llezîne' 26. kelime, 28. kelime)")

D = {}
D[122] = ("◇ 'e-ve-men kâne meyten fe-ahyeynâhu ve ce'alnâ lehû nûran yemşî bihî fi'n-nâsi ke-men meseluhû fi'z-zulumâti leyse bi-xâricin minhâ kezâlike zuyyine li'l-kâfirîne mâ kânû ya'melûn' — "
 "'e' + 've' + 'men' + PERF 3MS I. bab + nekre 'meyt' + 'fe' + PERF 1P IV. bab + 1P + 3MS + 've' + PERF 1P I. bab + 1P + 'li' + 3MS + nekre 'nûr' + IMPF 3MS I. bab + 'bi' + 3MS + 'fî' + belirli 'nâs' + "
 "'ke' + 'men' + 'mesel' + 3MS + 'fî' + belirli çoğul 'zulme' + PERF 3MS I. bab + 'bi' + nekre etken ortaç 'xâric' + 'min' + 3FS + 'ke' + 'zâlike' + PERF 3MS II. bab edilgen + 'li' + belirli çoğul etken ortaç 'kâfir' + 'mâ' + PERF 3MP I. bab + 3MP + IMPF 3MP I. bab + 3MP "
 "(ölçüm edim soru, kip INTG 1; 1P 4 · 3FS 1 · 3MP 4 · 3MS 8; bab I. bab ×6 · II. bab ×1 · IV. bab ×1). "
 "Allah lafzı yok; Rab yok; ölçüm '{{1|esmâ نُور 7\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor); "
 "esma_el kaydı 'degil' — 've ce'alnâ lehû nûran', kural 'esmâ adı esmâ dışı göndergeyle → degil' (esmâ dışı gönderge) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=24 (n z=1,23); ölçüm '{{1|EDİLGEN 1/8 fiil, pas z=0,38}}' — satır aynen; ölçüm '{{1|fâsıla يعملون → ن, N sınıfı}}' — satır aynen (6:121 ن → 6:122 ن); "
 "ölçüm '{{1|simetri \\[3, 1, 22, 1\\]}}' — satır aynen; ölçüm '{{1|harf 105 → harf3 97, isaret 8}}' — satır aynen; ölçüm '{{1|dış düğüm 1}}' — satır aynen. "
 "Ölçüm INTG 1: 'e-ve-men' (1. kelime; soru hemzesi); 'e-ve-men' (1.) kelimesindeki 've' SUP; 'fe-ahyeynâhu' (4.) kelimesindeki 'fe' REM; 've ce'alnâ' (5.) kelimesindeki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) كون ×2 ('kâne' 2. / 'kânû' 23. kelime) (okuma). "
 + T[122] + " (okuma). "
 + cumle(say('say 6:122 22-24', "mâ kânû ya'melûn", True), say('dizi 6 122 22 24', "mâ kâne 'amile")) + ' '
 + cumle(say('say 6:122 19-20', 'kezâlike zuyyine', True), say('dizi 6 122 19 20', 'zâ zeyyene')) + ' '
 + cumle(say('say 6:122 14-15', "fi'z-zulumât", True)) + ' ' +
 "Ölçüm xref okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıbı: 'mâ kâne 'amile' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'nûran' / 'z-zulumâti' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 'n-nâsi' (11. kelime); B2 —; B3 —; B4 'meyten' (3. kelime), 'ahyeynâhu' (4. kelime).",
 "◈D — D1 'e' + 've' + 'men' + PERF + nekre + 'fe' + PERF + 've' + PERF + 'li' + nekre + IMPF + 'bi' + 'fî' + belirli + 'ke' + 'men' + izafet + 'fî' + belirli + PERF + 'bi' + nekre + 'min' + 'ke' + 'zâlike' + PERF + 'li' + belirli + 'mâ' + PERF + IMPF; "
 "D2 soru; INTG ('e-ve-men' 1. kelime); D3 كون ×2; D4 1P 4 · 3FS 1 · 3MP 4 · 3MS 8, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[122] + "; aktör yok (ölçüm); A2 diriltilip nur verilenin karanlıkta kalanla karşılaştırılması; kâfirlere yaptıklarının süslü gösterilmesi; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 2 → 3 (ayetler arası); edim geçişi yasak, şart → soru (ayetler arası); bölüm açılışı.",
)

D[123] = ("◇ 've kezâlike ce'alnâ fî kulli qaryetin ekâbira mucrimîhâ li-yemkurû fîhâ ve mâ yemkurûne illâ bi-enfusihim ve mâ yeş'urûn' — "
 "'ve' + 'ke' + 'zâlike' + PERF 1P I. bab + 1P + 'fî' + 'kull' + nekre 'qarye' + çoğul 'ekber' + çoğul etken ortaç 'mucrim' + 3FS + 'li' + IMPF 3MP I. bab + 3MP + 'fî' + 3FS + "
 "'ve' + 'mâ' + IMPF 3MP I. bab + 3MP + 'illâ' + 'bi' + çoğul 'nefs' + 3MP + 've' + 'mâ' + IMPF 3MP I. bab + 3MP "
 "(ölçüm edim haber, kip NEG 2 · RES 1, biçim HASR; 1P 2 · 3FS 2 · 3MP 7; bab I. bab ×4). "
 "Allah lafzı yok; Rab yok; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); ölçüm '{{2|aktör: adsız `karye` 5\\. sırada}}' — satır aynen. "
 "Ölçüm 'yıldız yok' — satır aynen; n=15 (n z=0,27); ölçüm '{{2|fâsıla يشعرون → ن, N sınıfı}}' — satır aynen (6:122 ن → 6:123 ن); "
 "ölçüm '{{2|simetri \\[3, 1, 10, 1\\]}}' — satır aynen; ölçüm '{{2|harf 70 → harf3 68, isaret 2}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm NEG 2: 'mâ' (10.) ve 'mâ' (14. kelime); RES 1: 'illâ' (12. kelime); biçim HASR; 've kezâlike' (1.), 've mâ' (10.) ve 've mâ' (14.) kelimelerindeki 've' CONJ; 'li-yemkurû' (8.) PRP (okuma). "
 "Kök ikilemesi (ölçüm) مكر ×2 ('li-yemkurû' 8. / 'yemkurûne' 11. kelime) (okuma). "
 + T[123] + " (okuma). "
 + cumle(say('say 6:123 12-15', "illâ bi-enfusihim ve mâ yeş'urûn", True), say('dizi 6 123 12 15', "illâ nefs mâ şa'ara")) + ' '
 + cumle(say('say 6:123 1-2', "ve kezâlike ce'alnâ", True)) + ' ' + cumle(say('say 6:123 14-15', "ve mâ yeş'urûn", True)) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: 'illâ nefs mâ yeş'uru' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'ke' + 'zâlike' + PERF + 'fî' + 'kull' + nekre + 'ekber' + izafet + 'li' + IMPF + 'fî' + 've' + 'mâ' + IMPF + 'illâ' + 'bi' + izafet + 've' + 'mâ' + IMPF; "
 "D2 haber; NEG ('mâ' 10. kelime, 'mâ' 14. kelime), RES ('illâ' 12. kelime); D3 مكر ×2; D4 1P 2 · 3FS 2 · 3MP 7, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[123] + "; aktör adsız 'qaryetin' (5. kelime; ölçüm adsız karye); A2 her kasabada suçluların büyüklerinin tuzak kurmaları için kılınması; tuzağın kendilerine dönmesi ve farkında olmamaları; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi soru → haber (ayetler arası).",
)

D[124] = ("◇ 've izâ câ'ethum âyetun qâlû len nu'mine hattâ nu'tâ misle mâ ûtiye rusulu'llâhi'llâhu a'lemu haysu yec'alu risâletehû se-yusîbu'llezîne ecramû sağârun 'inde'llâhi ve 'azâbun şedîdun bi-mâ kânû yemkurûn' — "
 "'ve' + 'izâ' + PERF 3FS I. bab + 3MP + nekre 'âye' + PERF 3MP I. bab + 3MP + 'len' + IMPF 1P IV. bab + 'hattâ' + IMPF 1P IV. bab edilgen + 'misl' + 'mâ' + PERF 3MS IV. bab edilgen + çoğul 'resûl' + lafız + "
 "lafız + 'a'lem' + 'haysu' + IMPF 3MS I. bab + 'risâle' + 3MS + 'se' + IMPF 3MS IV. bab + 'ellezîne' + PERF 3MP IV. bab + 3MP + nekre 'sağâr' + ''ind' + lafız + 've' + nekre ''azâb' + nekre 'şedîd' + 'bi' + 'mâ' + PERF 3MP I. bab + 3MP + IMPF 3MP I. bab + 3MP "
 "(ölçüm edim haber, kip FUT 1 · NEG 1; 1P 2 · 3FS 1 · 3MP 9 · 3MS 4; bab I. bab ×5 · IV. bab ×5). "
 "Allah lafzı 13., 14. ve 24. sırada (ölçüm allah z=1,54); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=29 (n z=1,76); ölçüm '{{3|EDİLGEN 2/10 fiil, pas z=0,81}}' — satır aynen; ölçüm '{{3|fâsıla يمكرون → ن, N sınıfı}}' — satır aynen (6:123 ن → 6:124 ن); "
 "ölçüm '{{3|simetri \\[3, 7, 10, 1\\]}}' — satır aynen; ölçüm '{{3|harf 128 → harf3 119, isaret 9}}' — satır aynen; ölçüm '{{3|dış düğüm 5}}' — satır aynen. "
 "Ölçüm NEG 1: 'len' (5. kelime); FUT 1: 'se-yusîbu' (19. kelime); 've izâ' (1.) ve 've 'azâbun' (25.) kelimelerindeki 've' CONJ; 'izâ' (1.) T (okuma). "
 "Kök ikilemesi (ölçüm) أتي ×2 ('nu'tâ' 8. / 'ûtiye' 11. kelime), أله ×3 ('llâhi' 13. / 'llâhu' 14. / 'llâhi' 24. kelime), رسل ×2 ('rusulu' 12. / 'risâletehû' 18. kelime) (okuma). "
 + T[124] + " (okuma). "
 + cumle(say('say 6:124 9-11', 'misle mâ ûtiye', True), say('dizi 6 124 9 11', 'misl mâ âtâ'), say('dizi 6 124 8 11', 'âtâ misl mâ âtâ')) + ' '
 + cumle(say('say 6:124 9-10', 'misle mâ', True)) + " (--medde 11 ayet: 'mâ' yazım farkı ile; harekesiz sayım elif / medde yazımına bağlı). "
 + cumle(say('say 6:124 2-3', "câ'ethum âyetun", True)) + ' ' + cumle(say('say 6:124 23-24', "'inde'llâh", True)) + ' ' + cumle(say('say 6:124 27-28', 'bi-mâ kânû', True)) + ' ' +
 "Ölçüm xref 28:48 (emsal olarak basıldı) ve okunmuş 4 ayet. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'izâ' + PERF + nekre + PERF + 'len' + IMPF + 'hattâ' + IMPF + 'misl' + 'mâ' + PERF + izafet + lafız + lafız + 'a'lem' + 'haysu' + IMPF + izafet + 'se' + IMPF + 'ellezîne' + PERF + nekre + ''ind' + lafız + 've' + nekre + nekre + 'bi' + 'mâ' + PERF + IMPF; "
 "D2 haber; FUT ('se-yusîbu' 19. kelime), NEG ('len' 5. kelime); D3 أتي ×2, أله ×3, رسل ×2; 28:48 eşi; D4 1P 2 · 3FS 1 · 3MP 9 · 3MS 4, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[124] + "; aktör yok (ölçüm); A2 âyet gelince elçilere verilenin benzeri verilmedikçe inanmayacakları sözü; Allah'ın elçiliğini nereye koyacağını bilmesi; suç işleyenlere aşağılanma ve azap erişmesi; "
 "A3 'len nu'mine hattâ nu'tâ misle mâ ûtiye rusulu'llâh' (söz içi, 5-13. kelime); "
 "A4 " + BOLUM + "; söz açılır (5. kelime); söz kapanır (13. kelime, ayet içi); şahıs geçişi yok (ayetler arası); edim geçişi yok (ayetler arası).",
)

D[125] = ("◇ 'fe-men yuridi'llâhu en yehdiyehû yeşrah sadrahû li'l-islâmi ve men yurid en yudillehû yec'al sadrahû dayyiqan haracen ke-ennemâ yassa'adu fi's-semâ'i kezâlike yec'alu'llâhu'r-ricse 'ala'llezîne lâ yu'minûn' — "
 "'fe' + 'men' + IMPF 3MS IV. bab + lafız + 'en' + IMPF 3MS I. bab + 3MS + IMPF 3MS I. bab + 'sadr' + 3MS + 'li' + belirli mastar 'islâm' + 've' + 'men' + IMPF 3MS IV. bab + 'en' + IMPF 3MS IV. bab + 3MS + IMPF 3MS I. bab + 'sadr' + 3MS + "
 "nekre 'dayyiq' + nekre 'harac' + 'ke' + 'enne' + 'mâ' + IMPF 3MS V. bab + 'fî' + belirli 'semâ'' + 'ke' + 'zâlike' + IMPF 3MS I. bab + lafız + belirli 'rics' + ''alâ' + 'ellezîne' + 'lâ' + IMPF 3MP IV. bab + 3MP "
 "(ölçüm edim şart, kip COND 2 · NEG 1; 3MP 2 · 3MS 12; bab I. bab ×4 · IV. bab ×4 · V. bab ×1). "
 "Allah lafzı 3. ve 23. sırada (ölçüm allah z=0,90); Rab yok; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); ölçüm '{{4|aktör: adlı إِسْلام 8\\. sırada \\(cins, rol mecrur\\)}}' — satır aynen. "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=28 (n z=1,65); ölçüm '{{4|fâsıla يؤمنون → ن, N sınıfı}}' — satır aynen (6:124 ن → 6:125 ن); "
 "ölçüm '{{4|simetri \\[3, 1, 9, 1\\]}}' — satır aynen; ölçüm '{{4|harf 116 → harf3 109, isaret 7}}' — satır aynen; ölçüm '{{4|dış düğüm 0}}' — satır aynen. "
 "Ölçüm COND 2: 'fe-men' (1.) ve 've men' (9. kelime); NEG 1: 'lâ' (27. kelime); 'fe-men' (1.) kelimesindeki 'fe' REM; 've men' (9.) kelimesindeki 've' CONJ; 'en' (4. ve 11.) SUB; 'ke-ennemâ' (17.) ACC + PREV (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 ('llâhu' 3. / 'llâhu' 23. kelime), جعل ×2 ('yec'al' 13. / 'yec'alu' 22. kelime), رود ×2 ('yuridi' 2. / 'yurid' 10. kelime), صدر ×2 ('sadrahû' 7. / 'sadrahû' 14. kelime) (okuma). "
 + T[125] + " (okuma). "
 + cumle(say('say 6:125 26-28', "llezîne lâ yu'minûn", True), say('dizi 6 125 26 28', 'ellezî lâ âmene')) + ' '
 + cumle(say('say 6:125 19-20', "fi's-semâ'", True)) + ' ' + cumle(say('say 6:125 26-27', 'llezîne lâ', True)) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: 'ellezî lâ âmene' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'yehdiyehû' / 'yudillehû' — ayetler arası: yok.",
 "◈K — K1 's-semâ'i' (20. kelime).",
 "◈B — —",
 "◈D — D1 'fe' + 'men' + IMPF + lafız + 'en' + IMPF + IMPF + izafet + 'li' + belirli + 've' + 'men' + IMPF + 'en' + IMPF + IMPF + izafet + nekre + nekre + 'ke' + 'enne' + 'mâ' + IMPF + 'fî' + belirli + 'ke' + 'zâlike' + IMPF + lafız + belirli + ''alâ' + 'ellezîne' + 'lâ' + IMPF; "
 "D2 şart; COND ('fe-men' 1. kelime, 've men' 9. kelime), NEG ('lâ' 27. kelime); D3 أله ×2, جعل ×2, رود ×2, صدر ×2; D4 3MP 2 · 3MS 12, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[125] + "; aktör adlı 'li'l-islâmi' (8. kelime; ölçüm rol mecrur); A2 Allah'ın doğru yola iletmek istediğinin göğsünü İslâm'a açması; saptırmak istediğinin göğsünü daraltması; inanmayanların üzerine pislik kılınması; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi haber → şart (ayetler arası); şart → cevap (ayet içi; COND 'men' 1. kelime: 'fe-men yuridi'llâhu' / 'yeşrah' (6. kelime)); "
 "şart → cevap (ayet içi; COND 'men' 9. kelime: 've men yurid' / 'yec'al' (13. kelime)).",
)

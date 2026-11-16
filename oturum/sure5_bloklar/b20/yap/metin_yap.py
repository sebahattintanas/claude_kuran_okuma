# blok 20 (5:59-63) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b20/say2.txt'
os.environ['OLC'] = '/home/claude/b20/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Kitap ehlinin tutumu; bağlı el sözü; Tevrat ve İncil'i ayakta tutma' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 59: "De ki: Ey Kitap ehli! Bizi kınamanız, ancak Allah'a, bize indirilene ve önceden indirilene iman etmemizden ve çoğunuzun fâsıklar olmasından mıdır?",
 60: "De ki: Size Allah katında bundan daha kötü bir karşılığı olanı haber vereyim mi? Allah'ın lanetlediği ve gazap ettiği, içlerinden maymunlar ve domuzlar kıldığı ve tâğûta kulluk eden kimse. İşte onlar yer bakımından daha kötü ve doğru yoldan daha sapkındır.",
 61: "Size geldiklerinde: İman ettik, derler; hâlbuki küfürle girmişlerdir ve onlar onunla çıkmışlardır. Allah, gizlemekte olduklarını daha iyi bilendir.",
 62: "Onların çoğunun günahta, düşmanlıkta ve haram yemelerinde yarıştıklarını görürsün. Yapmakta oldukları ne kötüdür!",
 63: "Rabbaniler ve âlimler onları günah sözlerinden ve haram yemelerinden sakındırmalı değil miydi? İşlemekte oldukları ne kötüdür!",
}

T59 = ("muhatap 2MS (adsız; 'qul' 1. kelime); 'ehle'l-kitâbi' (nida edilen; 2-3. kelime); muhatap 2MP (adsız; söz içi; 'tenqimûne' 5., 'ekserakum' 19. kelime); konuşan 1P (adsız; söz içi; 'minnâ' 6., 'âmennâ' 9., 'ileynâ' 13. kelime); "
       "Allah (lafız; 10. kelime); 'unzile' naib-i faili 3MS (adsız; edilgen, 12. ve 15. kelime)")
T60 = ("muhatap 2MS (adsız; 'qul' 1. kelime); konuşan 1S (adsız; söz içi; 'unebbi'ukum' 3. kelime); muhatap 2MP (adsız; söz içi; 'unebbi'ukum' 3. kelime); 'şerrin' (nekre; 4. kelime); 'mesûbeten' (nekre; 7. kelime); Allah (lafız; 9. ve 12. kelime); "
       "'men' (ism-i mevsûl; 10. kelime); 'le'anehu' faili 3MS (adsız; gönderge lafız, 11. kelime); 'le'anehu' mef'ûlü 3MS (adsız; gönderge 'men', 11. kelime); 'ğadibe' faili 3MS (adsız; 13. kelime); ''aleyhi' 3MS (adsız; 14. kelime); "
       "'ce'ale' faili 3MS (adsız; 15. kelime); 'minhumu' 3MP (adsız; 16. kelime); ''abede' faili 3MS (adsız; gönderge 'men', 19. kelime); 'ulâ'ike' (işaret ismi; 21. kelime)")
T61 = ("'câ'ûkum' faili 3MP (adsız; 2. kelime); muhatap 2MP (adsız; 'câ'ûkum' 2. kelime); 'qâlû' faili 3MP (adsız; 3. kelime); konuşan 1P (adsız; söz içi; 'âmennâ' 4. kelime); 'dexalû' faili 3MP (adsız; 6. kelime); 've hum' 3MP (adsız; 8. kelime); "
       "'xaracû' faili 3MP (adsız; 10. kelime); 'bihî' 3MS (adsız; gönderge 'l-kufri', 11. kelime); Allah (lafız; 12. kelime); 'kânû' faili 3MP (adsız; 15. kelime); 'yektumûn' faili 3MP (adsız; 16. kelime)")
T62 = ("muhatap 2MS (adsız; 'terâ' 1. kelime); 'kesîran' (nekre; 2. kelime); 'minhum' 3MP (adsız; 3. kelime); 'yusâri'ûne' faili 3MP (adsız; 4. kelime); 'eklihimu' 3MP (adsız; 8. kelime); 'bi'se' faili 3MS (adsız; gönderge 'mâ', 10. kelime); "
       "'kânû' faili 3MP (adsız; 12. kelime); 'ya'melûn' faili 3MP (adsız; 13. kelime)")
T63 = ("'yenhâhumu' faili 3MS (adsız; gönderge 'r-rabbâniyyûne', 2. kelime); 'yenhâhumu' mef'ûlü 3MP (adsız; 2. kelime); 'r-rabbâniyyûne' ve 'l-ahbâru' (3-4. kelime); 'qavlihimu' 3MP (adsız; 6. kelime); 'eklihimu' 3MP (adsız; 8. kelime); "
       "'bi'se' faili 3MS (adsız; gönderge 'mâ', 10. kelime); 'kânû' faili 3MP (adsız; 12. kelime); 'yasna'ûn' faili 3MP (adsız; 13. kelime)")

D = {}
D[59] = ("◇ 'qul yâ ehle'l-kitâbi hel tenqimûne minnâ illâ en âmennâ bi'llâhi ve mâ unzile ileynâ ve mâ unzile min qablu ve enne ekserakum fâsiqûn' — "
 "IMPV 2MS I. bab + 'yâ' + 'ehl' + belirli 'kitâb' + 'hel' + IMPF 2MP I. bab + 'min' + 1P + 'illâ' + 'en' + PERF 1P IV. bab + 'bi' + lafız + 've' + 'mâ' + edilgen PERF 3MS IV. bab + 'ilâ' + 1P + 've' + 'mâ' + edilgen PERF 3MS IV. bab + 'min' + 'qabl' + 've' + 'enne' + 'eksar' + 2MP + çoğul ortaç 'fâsiq' "
 "(ölçüm edim soru, emir, nida, kip IMPV 1 · INTG 1 · RES 1 · VOC 1, biçim HASR; 1P 4 · 2MP 3 · 2MS 1 · 3MS 2; bab I. bab ×2 · IV. bab ×3; EDİLGEN 2/5 fiil). "
 "Allah lafzı 10. sırada (ölçüm allah z=0,47); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=20 (n z=0,81); ölçüm '{{1|fâsıla فسقون → ن, N sınıfı}}' — satır aynen; ölçüm '{{1|EDİLGEN 2/5 fiil, pas z=1,95}}' — satır aynen ('unzile' 12. ve 15. kelime); ölçüm '{{1|sayı işareti \\S+}}' — satır aynen ('ekserakum' 19. kelime); "
 "ölçüm '{{1|simetri \\[4, 4, 11, 1\\]}}' — satır aynen; ölçüm '{{1|harf 75 → harf3 75, isaret 0}}' — satır aynen; ölçüm '{{1|dış düğüm 10}}' — satır aynen. "
 "Ölçüm IMPV 1: 'qul' (1. kelime); VOC 1: 'yâ' (2. kelime); INTG 1: 'hel' (4. kelime); RES 1: 'illâ' (7. kelime); 've mâ' (11.), 've mâ' (14.) ve 've enne' (18.)'deki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) نزل ×2 ('unzile' 12. / 15. kelime) (okuma). "
 + T59 + " (okuma). "
 + cumle(say('say 5:59 1-3', "qul yâ ehle'l-kitâb", True), say('say 5:59 2-3', "yâ ehle'l-kitâb"), say('dizi 5 59 1 3', "qâle ehl kitâb")) + ' '
 + cumle(say('say 5:59 4-6', "hel tenqimûne minnâ", True), say('say 5:59 5-6', "tenqimûne minnâ"), say('lem 5:59:5', "naqamu")) + ' '
 + cumle(say('say 5:59 7-10', "illâ en âmennâ bi'llâh", True), say('say 5:59 8-10', "en âmennâ bi'llâh"), say('say 5:59 9-13', "âmennâ bi'llâhi ve mâ unzile ileynâ"), say('dizi 5 59 9 11', "âmene allâh mâ"), say('say 5:59 11-13 --on', "ve mâ unzile ileynâ")) + ' '
 + cumle(say('say 5:59 14-17 --on', "ve mâ unzile min qabl", True), say('say 5:59 15-17', "unzile min qabl"), say('say 5:59 16-18', "min qablu ve enne"), say('dizi 5 59 16 18', "min qabl enne"), say('say 5:59 18-20 --on', "ve enne ekserakum fâsiqûn"), say('say 5:59 19-20', "ekserakum fâsiqûn")) + ' '
 "Ölçüm xref 3:64 ve 2:136 (emsal olarak basıldı) ve okunmuş ve henüz okunmamış başka ayetler. "
 "Ölçüm nakarat3 kalıpları: 'qul yâ ehle'l-kitâb' süzgeç GEÇER; 'min qablu ve enne' ve 'âmennâ bi'llâhi ve mâ' GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPV + 'yâ' + izafet + belirli + 'hel' + IMPF + 'min' + 'illâ' + 'en' + PERF + 'bi' + lafız + 've' + 'mâ' + PERF + 'ilâ' + 've' + 'mâ' + PERF + 'min' + 'qabl' + 've' + 'enne' + izafet + çoğul; "
 "D2 soru, emir, nida, IMPV ('qul' 1. kelime), VOC ('yâ' 2. kelime), INTG ('hel' 4. kelime), RES ('illâ' 7. kelime); D3 نزل ×2; 3:64 ve 2:136 eşleri; D4 1P 4 · 2MP 3 · 2MS 1 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T59 + "; aktör yok (ölçüm); A2 Kitap ehline hitap; kınama; iman; indirilen; fâsıklık; "
 "A3 'yâ ehle'l-kitâbi hel tenqimûne minnâ' ile açılan söz (söz içi, 2-20. kelime); "
 "A4 " + BOLUM + "; edim geçişi haber → soru, emir, nida (ayetler arası); şahıs geçişi 3 → 1 (ayetler arası).",
)

D[60] = ("◇ 'qul hel unebbi'ukum bi-şerrin min zâlike mesûbeten 'inde'llâhi men le'anehu'llâhu ve ğadibe 'aleyhi ve ce'ale minhumu'l-qirade ve'l-xanâzîra ve 'abede't-tâğûta ulâ'ike şerrun mekânen ve edallu 'an sevâ'i's-sebîl' — "
 "IMPV 2MS I. bab + 'hel' + IMPF 1S II. bab + 2MP + 'bi' + nekre 'şerr' + 'min' + 'zâ' + 'li' + 'ke' + nekre masdar 'mesûbe' + ''ind' + lafız + 'men' + PERF 3MS I. bab + 3MS + lafız + 've' + PERF 3MS I. bab + ''alâ' + 3MS + 've' + PERF 3MS I. bab + 'min' + 3MP + belirli çoğul 'qirade' + 've' + belirli çoğul 'xınzîr' + 've' + PERF 3MS I. bab + belirli 'tâğût' + 'ulâ'i' + 'ke' + nekre 'şerr' + nekre 'mekân' + 've' + 'edall' + ''an' + 'sevâ'' + belirli 'sebîl' "
 "(ölçüm edim soru, emir, kip IMPV 1 · INTG 1; 1S 1 · 2MP 1 · 2MS 1 · 3MP 1 · 3MS 6; bab I. bab ×5 · II. bab ×1). "
 "Allah lafzı 9. ve 12. sırada (ölçüm allah z=0,95); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=27 (n z=1,55); ölçüm '{{2|fâsıla ٱلسبيل → ل, ل sınıfı — KAFİYE KIRILMASI}}' — satır aynen; ölçüm '{{2|harf 115 → harf3 109, isaret 6}}' — satır aynen; ölçüm '{{2|dış düğüm 4}}' — satır aynen. "
 "Ölçüm IMPV 1: 'qul' (1. kelime); INTG 1: 'hel' (2. kelime); 've ğadibe' (13.), 've ce'ale' (15.), 've'l-xanâzîra' (18.), 've 'abede' (19.) ve 've edallu' (24.)'daki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 (lafız 9., 12. kelime), شرر ×2 ('bi-şerrin' 4. / 'şerrun' 22. kelime) (okuma). "
 + T60 + " (okuma). "
 + cumle(say('say 5:60 1-3', "qul hel unebbi'ukum", True), say('say 5:60 2-3', "hel unebbi'ukum"), say('say 5:60 3-4', "unebbi'ukum bi-şerr"), say('say 5:60 4-7', "bi-şerrin min zâlike mesûbe")) + ' '
 + cumle(say('say 5:60 7-9', "mesûbeten 'inde'llâh", True), say('say 5:60 8-9', "'inde'llâh"), say('lem 5:60:7', "mesûbe")) + ' '
 + cumle(say('say 5:60 10-12', "men le'anehu'llâh", True), say('say 5:60 11-12', "le'anehu'llâh"), say('say 5:60 13-14 --on', "ve ğadibe 'aleyh"), say('say 5:60 15-18 --on', "ve ce'ale minhumu'l-qirade ve'l-xanâzîr"), say('say 5:60 17-18', "l-qirade ve'l-xanâzîr"), say('lem 5:60:17', "qirade"), say('lem 5:60:18', "xınzîr")) + ' '
 + cumle(say('say 5:60 19-20 --on', "ve 'abede't-tâğût", True), say('lem 5:60:20', "tâğût"), say('say 5:60 21-23', "ulâ'ike şerrun mekânen"), say('say 5:60 22-23', "şerrun mekânen")) + ' '
 + cumle(say('say 5:60 24-27 --on', "ve edallu 'an sevâ'i's-sebîl", True), say('say 5:60 25-27', "'an sevâ'i's-sebîl"), say('dizi 5 60 25 27', "'an sevâ' sebîl"), say('say 5:60 26-27', "sevâ'i's-sebîl")) + ' '
 "Ölçüm xref 25:34 (emsal olarak basıldı) ve okunmuş başka ayetler. "
 "Ölçüm nakarat3 kalıpları: ''an sevâ'i's-sebîl' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPV + 'hel' + IMPF + 'bi' + nekre + 'min' + 'zâ' + nekre + ''ind' + lafız + 'men' + PERF + lafız + 've' + PERF + ''alâ' + 've' + PERF + 'min' + belirli + 've' + belirli + 've' + PERF + belirli + 'ulâ'i' + nekre + nekre + 've' + 'edall' + ''an' + izafet + belirli; "
 "D2 soru, emir, IMPV ('qul' 1. kelime), INTG ('hel' 2. kelime); D3 أله ×2, شرر ×2; 25:34 eşi; D4 1S 1 · 2MP 1 · 2MS 1 · 3MP 1 · 3MS 6, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T60 + "; aktör yok (ölçüm); A2 daha kötü karşılık; lanet; gazap; maymunlar ve domuzlar; tâğûta kulluk; sapkınlık; "
 "A3 'hel unebbi'ukum bi-şerrin' ile açılan söz (söz içi, 2-27. kelime); "
 "A4 " + BOLUM + "; edim geçişi soru, emir, nida → soru, emir (ayetler arası); şahıs geçişi 1 → 3 (ayetler arası).",
)

D[61] = ("◇ 've izâ câ'ûkum qâlû âmennâ ve qad dexalû bi'l-kufri ve hum qad xaracû bihî ve'llâhu a'lemu bi-mâ kânû yektumûn' — "
 "'ve' + 'izâ' + PERF 3MP I. bab + 2MP + PERF 3MP I. bab + PERF 1P IV. bab + 've' + 'qad' + PERF 3MP I. bab + 'bi' + belirli 'kufr' + 've' + 3MP + 'qad' + PERF 3MP I. bab + 'bi' + 3MS + 've' + lafız + 'a'lem' + 'bi' + 'mâ' + PERF 3MP I. bab + IMPF 3MP I. bab "
 "(ölçüm edim haber, kip CERT 2; 1P 2 · 2MP 1 · 3MP 13 · 3MS 1; bab I. bab ×6 · IV. bab ×1). "
 "Allah lafzı 12. sırada (ölçüm allah z=0,72); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=16 (n z=0,38); ölçüm '{{3|fâsıla يكتمون → ن, N sınıfı}}' — satır aynen; ölçüm '{{3|harf 75 → harf3 69, isaret 6}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm CERT 2: 'qad' (5. ve 9. kelime); T 'izâ' (1. kelime); 've izâ' (1.) ve 've hum' (8.)'daki 've' CONJ, 've qad' (5.)'daki 've' CIRC, 've'llâhu' (12.)'daki 've' REM (okuma). "
 + T61 + " (okuma). "
 + cumle(say('say 5:61 1-2 --on', "ve izâ câ'ûkum", True), say('say 5:61 2-4', "câ'ûkum qâlû âmennâ"), say('say 5:61 3-4', "qâlû âmennâ")) + ' '
 + cumle(say('say 5:61 5-7 --on', "ve qad dexalû bi'l-kufr", True), say('say 5:61 6-7', "dexalû bi'l-kufr"), say('say 5:61 8-11 --on', "ve hum qad xaracû bih"), say('say 5:61 9-11', "qad xaracû bih")) + ' '
 + cumle(say('say 5:61 12-16 --on', "ve'llâhu a'lemu bi-mâ kânû yektumûn", True), say('say 5:61 12-13 --on', "ve'llâhu a'lem"), say('say 5:61 13-16', "a'lemu bi-mâ kânû yektumûn"), say('say 5:61 14-16', "bi-mâ kânû yektumûn"), say('say 5:61 15-16', "kânû yektumûn")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'dexalû bi'l-kufr' / 'xaracû bih' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'izâ' + PERF + PERF + PERF + 've' + 'qad' + PERF + 'bi' + belirli + 've' + 'qad' + PERF + 'bi' + 've' + lafız + 'a'lem' + 'bi' + 'mâ' + PERF + IMPF; "
 "D2 haber, CERT ('qad' 5. ve 9. kelime); D3 ikileme yok; 3:167 eşi; D4 1P 2 · 2MP 1 · 3MP 13 · 3MS 1, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T61 + "; aktör yok (ölçüm); A2 iman iddiası; küfürle giriş ve çıkış; gizlenen; Allah'ın bilmesi; "
 "A3 'âmennâ' (söz içi, 4. kelime); "
 "A4 " + BOLUM + "; edim geçişi soru, emir → haber (ayetler arası); şahıs geçişi yok.",
)

D[62] = ("◇ 've terâ kesîran minhum yusâri'ûne fi'l-ismi ve'l-'udvâni ve eklihimu's-suhta le-bi'se mâ kânû ya'melûn' — "
 "'ve' + IMPF 2MS I. bab + nekre 'kesîr' + 'min' + 3MP + IMPF 3MP III. bab + 'fî' + belirli 'ism' + 've' + belirli ''udvân' + 've' + masdar 'ekl' + 3MP + belirli 'suht' + 'le' + PERF 3MS I. bab + 'mâ' + PERF 3MP I. bab + IMPF 3MP I. bab "
 "(ölçüm edim haber, kip EMPH 1; 2MS 1 · 3MP 8 · 3MS 1; bab I. bab ×4 · III. bab ×1). "
 "Lafız yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=13 (n z=0,06); ölçüm '{{4|fâsıla يعملون → ن, N sınıfı}}' — satır aynen; ölçüm '{{4|sayı işareti \\S+}}' — satır aynen ('kesîran' 2. kelime); ölçüm '{{4|harf 64 → harf3 61, isaret 3}}' — satır aynen; ölçüm '{{4|dış düğüm 0}}' — satır aynen. "
 "Ölçüm EMPH 1: 'le' (10. kelime); 've terâ' (1.)'daki 've' REM, 've'l-'udvâni' (7.) ve 've eklihimu' (8.)'daki 've' CONJ (okuma). "
 + T62 + " (okuma). "
 + cumle(say('say 5:62 1-3 --on', "ve terâ kesîran minhum", True), say('dizi 5 62 1 3', "re'â kesîr min"), say('say 5:62 2-4', "kesîran minhum yusâri'ûn")) + ' '
 + cumle(say('say 5:62 4-7', "yusâri'ûne fi'l-ismi ve'l-'udvân", True), say('say 5:62 5-7', "fi'l-ismi ve'l-'udvân"), say('say 5:62 6-7', "l-ismi ve'l-'udvân")) + ' '
 + cumle(say('say 5:62 8-9 --on', "ve eklihimu's-suht", True), say('lem 5:62:9', "suht"), say('say 5:62 8-12 --on', "ve eklihimu's-suhta le-bi'se mâ kânû"), say('dizi 5 62 8 12', "ekl suht bi'se mâ kâne")) + ' '
 + cumle(say('say 5:62 10-12 --on', "le-bi'se mâ kânû", True), say('dizi 5 62 10 12', "bi'se mâ kâne"), say('say 5:62 10-13 --on', "le-bi'se mâ kânû ya'melûn"), say('say 5:62 11-13', "mâ kânû ya'melûn")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıpları: 'eklihimu's-suhta le-bi'se mâ kânû' ve 'le-bi'se mâ kânû' süzgeç GEÇER; 've terâ kesîran minhum' GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + IMPF + nekre + 'min' + IMPF + 'fî' + belirli + 've' + belirli + 've' + izafet + belirli + 'le' + PERF + 'mâ' + PERF + IMPF; "
 "D2 haber, EMPH ('le' 10. kelime); D3 ikileme yok; D4 2MS 1 · 3MP 8 · 3MS 1, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T62 + "; aktör yok (ölçüm); A2 günahta yarış; düşmanlık; haram yeme; yapılanın kötülüğü; A3 —; "
 "A4 " + BOLUM + "; edim geçişi yok (haber); şahıs geçişi yok.",
)

D[63] = ("◇ 'levlâ yenhâhumu'r-rabbâniyyûne ve'l-ahbâru 'an qavlihimu'l-isme ve eklihimu's-suhta le-bi'se mâ kânû yasna'ûn' — "
 "'levlâ' + IMPF 3MS I. bab + 3MP + belirli çoğul 'rabbâniyyîn' + 've' + belirli çoğul 'ahbâr' + ''an' + masdar 'qavl' + 3MP + belirli 'ism' + 've' + masdar 'ekl' + 3MP + belirli 'suht' + 'le' + PERF 3MS I. bab + 'mâ' + PERF 3MP I. bab + IMPF 3MP I. bab "
 "(ölçüm edim haber, kip EMPH 1; 3MP 7 · 3MS 2; bab I. bab ×4). "
 "Lafız yok; ölçüm '{{5|رَبّ 3\\. sırada \\(rab z=1,32\\)}}' — satır aynen; 'r-rabbâniyyûne' (3. kelime, kök ربب), Rab adı değil (okuma); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=13 (n z=0,06); ölçüm '{{5|fâsıla يصنعون → ن, N sınıfı}}' — satır aynen; ölçüm '{{5|harf 68 → harf3 66, isaret 2}}' — satır aynen; ölçüm '{{5|dış düğüm 0}}' — satır aynen. "
 "Ölçüm EMPH 1: 'le' (10. kelime); morph EXH 'levlâ' (1. kelime); 've'l-ahbâru' (4.) ve 've eklihimu' (8.)'daki 've' CONJ (okuma). "
 + T63 + " (okuma). "
 + cumle(say('say 5:63 1-4', "levlâ yenhâhumu'r-rabbâniyyûne ve'l-ahbâr", True), say('say 5:63 1-2', "levlâ yenhâhum"), say('say 5:63 3-4', "r-rabbâniyyûne ve'l-ahbâr"), say('lem 5:63:3', "rabbâniyyîn")) + ' '
 + cumle(say('say 5:63 5-7', "'an qavlihimu'l-ism", True), say('say 5:63 6-7', "qavlihimu'l-ism"), say('say 5:63 8-12 --on', "ve eklihimu's-suhta le-bi'se mâ kânû"), say('dizi 5 63 8 12', "ekl suht bi'se mâ kâne")) + ' '
 + cumle(say('say 5:63 10-12 --on', "le-bi'se mâ kânû", True), say('dizi 5 63 10 12', "bi'se mâ kâne"), say('say 5:63 10-13 --on', "le-bi'se mâ kânû yasna'ûn"), say('say 5:63 11-13', "mâ kânû yasna'ûn"), say('lem 5:63:13', "sana'u")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıpları: 'eklihimu's-suhta le-bi'se mâ kânû' ve 'le-bi'se mâ kânû' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'levlâ' + IMPF + belirli + 've' + belirli + ''an' + izafet + belirli + 've' + izafet + belirli + 'le' + PERF + 'mâ' + PERF + IMPF; "
 "D2 haber, EMPH ('le' 10. kelime); D3 ikileme yok; D4 3MP 7 · 3MS 2, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T63 + "; aktör yok (ölçüm); A2 rabbaniler ve âlimler; sakındırma; günah söz; haram yeme; yapılanın kötülüğü; A3 —; "
 "A4 " + BOLUM + "; edim geçişi yok (haber); şahıs geçişi yok.",
)

out = ['# ── blok 5:59-63 (2026-11-16) ──', 'MEAL20 = {']
for n in range(59, 64):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M20 = {']
for n in range(59, 64):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL20); M.update(M20)']
open('/home/claude/yamalar/metin_5_59_63.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

# sûre 6 blok 2 (6:6-11) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b02/say2.txt'
os.environ['OLC'] = '/home/claude/b02/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Gökleri ve yeri yaratan; yüz çeviren kavimler' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 6: "Görmediler mi, kendilerinden önce nice nesilleri helâk ettik! Onları yeryüzünde sizi yerleştirmediğimiz biçimde yerleştirmiştik; üzerlerine gökten bol yağmur gönderdik ve ırmakları altlarından akar kıldık. Onları günahları yüzünden helâk ettik ve onların ardından başka nesiller inşâ ettik.",
 7: "Sana kâğıtta bir kitap indirseydik de onu elleriyle yoklasalardı, inkâr edenler: Bu apaçık bir büyüden başka bir şey değil, derlerdi.",
 8: "Ona bir melek indirilseydi ya, dediler. Bir melek indirseydik, iş bitirilmiş olurdu; sonra onlara mühlet verilmezdi.",
 9: "Onu bir melek kılsaydık, onu bir adam kılardık ve karıştırdıkları şeyi onlara karıştırırdık.",
 10: "Andolsun, senden önceki elçilerle de alay edildi; sonunda onlarla eğlenenleri, alay ettikleri şey kuşatıverdi.",
 11: "De ki: Yeryüzünde gezin, sonra yalanlayanların sonu nasıl olmuş, bakın.",
}

T = {}
T[6] = ("'yerav' 3MP (adsız; gönderge 6:1 11. kelime, 2. kelime); 'qablihim' 3MP (adsız; gönderge 6:1 11. kelime, 6. kelime); "
        "konuşan 1P (adsız; 'ehleknâ', 'mekkennâhum', 'numekkin', 've erselne', 've ce'alne', 'fe-ehleknâhum', 've enşe'nâ' — 4., 9., 14., 16., 20., 25. ve 27. kelime); "
        "'mekkennâhum', ''aleyhim', 'tahtihim', 'fe-ehleknâhum', 'bi-zunûbihim', 'ba'dihim' 3MP (adsız; gönderge 'qarnin' — 9., 18., 24., 25., 26. ve 29. kelime); "
        "muhatap 2MP (adsız; 'lekum', 15. kelime); 'tecrî' 3FS (adsız; gönderge 'l-enhâra', 22. kelime)")
T[7] = ("konuşan 1P (adsız; 'nezzelnâ', 2. kelime); muhatap 2MS (adsız; ''aleyke', 3. kelime); "
        "'fe-lemesûhu', 'bi-eydîhim' 3MP (adsız; gönderge 6:1 11. kelime — 7. ve 8. kelime); 'fe-lemesûhu' 3MS (adsız; gönderge 'kitâben', 7. kelime); "
        "'le-qâle' 3MS (fiil uyumu; 9. kelime — fail 10. kelime); 'llezîne' ('le-qâle' faili; 10. kelime); 'keferû' 3MP (adsız; gönderge 'llezîne', 11. kelime)")
T[8] = ("'ve qâlû' 3MP (adsız; gönderge 6:1 11. kelime, 1. kelime); 'unzile' 3MS (adsız; edilgen; söz içi; naib-i faili 5. kelimedeki ad, 3. kelime); 'melekun' ('unzile' naib-i faili; söz içi; 5. kelime); "
        "''aleyhi' 3MS (adsız; söz içi; gönderge elçi, 4. kelime); konuşan 1P (adsız; 'enzelnâ', 7. kelime); "
        "'le-qudiye' 3MS (adsız; edilgen; naib-i faili 10. kelimedeki ad, 9. kelime); 'l-emru' ('le-qudiye' naib-i faili; 10. kelime); 'yunzarûn' 3MP (adsız; edilgen; naib-i faili zamir; gönderge 6:1 11. kelime, 13. kelime)")
T[9] = ("konuşan 1P (adsız; 'ce'alnâhu', 'le-ce'alnâhu', 've le-lebesnâ' — 2., 4. ve 6. kelime); "
        "'ce'alnâhu', 'le-ce'alnâhu' 3MS (adsız; gönderge elçi — 2. ve 4. kelime); "
        "''aleyhim', 'yelbisûn' 3MP (adsız; gönderge 6:1 11. kelime — 7. ve 9. kelime)")
T[10] = ("'stuhzi'e' 3MS (adsız; edilgen; naib-i faili mecrur, 2. kelime); muhatap 2MS (adsız; 'qablike', 5. kelime); "
         "'fe-hâqa' 3MS (fiil uyumu; 6. kelime — fail 10. kelime); 'sexirû' 3MP (adsız; gönderge 'llezîne', 8. kelime); "
         "'minhum' 3MP (adsız; gönderge 'bi-rusulin', 9. kelime); 'kânû', 'yestehzi'ûn' 3MP (adsız; gönderge 'llezîne' — 11. ve 13. kelime); "
         "'bihî' 3MS (adsız; gönderge 'mâ', 12. kelime)")
T[11] = ("muhatap 2MS (adsız; 'qul', 1. kelime); muhatap 2MP (adsız; söz içi; 'sîrû', 'nzurû' — 2. ve 6. kelime); "
         "'kâne' 3MS (fiil uyumu; söz içi; 8. kelime — fail 9. kelime)")

D = {}
D[6] = ("◇ 'e-lem yerav kem ehleknâ min qablihim min qarnin mekkennâhum fi'l-ardi mâ lem numekkin lekum ve erselne's-semâ'e 'aleyhim midrâran ve ce'alne'l-enhâra tecrî min tahtihim fe-ehleknâhum bi-zunûbihim ve enşe'nâ min ba'dihim qarnen âxarîn' — "
 "'e' + 'lem' + IMPF 3MP I. bab + 'kem' + PERF 1P IV. bab + 'min' + 'qabl' + 3MP + 'min' + nekre 'qarn' + PERF 1P II. bab + 3MP + 'fî' + belirli 'ard' + 'mâ' + 'lem' + IMPF 1P II. bab + 'li' + 2MP + "
 "'ve' + PERF 1P IV. bab + belirli 'semâ'' + ''alâ' + 3MP + nekre 'midrâr' + 've' + PERF 1P I. bab + belirli çoğul 'neher' + IMPF 3FS I. bab + 'min' + 'taht' + 3MP + "
 "'fe' + PERF 1P IV. bab + 3MP + 'bi' + çoğul 'zenb' + 3MP + 've' + PERF 1P IV. bab + 'min' + 'ba'd' + 3MP + nekre 'qarn' + çoğul sıfat 'âxar' "
 "(ölçüm edim soru, kip INTG 1 · NEG 2; 1P 13 · 2MP 1 · 3FS 1 · 3MP 9; bab I. bab ×3 · II. bab ×2 · IV. bab ×4). "
 "Lafız yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=31 (n z=1,97); ölçüm '{{1|fâsıla ءاخرين → ن, N sınıfı}}' — satır aynen (6:5 ن → 6:6 ن); "
 "ölçüm '{{1|simetri \\[4, 7, 12, 1\\]}}' — satır aynen; ölçüm '{{1|harf 140 → harf3 136, isaret 4}}' — satır aynen; ölçüm '{{1|dış düğüm 6}}' — satır aynen. "
 "Ölçüm INTG 1: 'e-lem' (1. kelime); NEG 2: 'e-lem' (1. kelime), 'lem' (13. kelime); 've erselne' (16.), 've ce'alne' (20.) ve 've enşe'nâ' (27.) kelimelerindeki 've' CONJ; 'fe-ehleknâhum' (25.) kelimesindeki 'fe' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) قرن ×2 ('qarnin' 8. / 'qarnen' 30. kelime), مكن ×2 ('mekkennâhum' 9. / 'numekkin' 14. kelime), هلك ×2 ('ehleknâ' 4. / 'fe-ehleknâhum' 25. kelime) (okuma). "
 + T[6] + " (okuma). "
 + cumle(say('say 6:6 1-4', "e-lem yerav kem ehleknâ", True), say('say 6:6 3-8', "kem ehleknâ min qablihim min qarn"), say('say 6:6 5-7', "min qablihim min"), say('dizi 6 6 5 7', "min qabl min")) + ' '
 + cumle(say('say 6:6 9-15', "mekkennâhum fi'l-ardi mâ lem numekkin lekum", True), say('say 6:6 16-19 --on', "ve erselne's-semâ'e 'aleyhim midrâr"), say('say 6:6 20-24 --on', "ve ce'alne'l-enhâra tecrî min tahtihim"),
         say('say 6:6 21-24', "l-enhâra tecrî min tahtihim")) + ' '
 + cumle(say('say 6:6 25-26 --on', "fe-ehleknâhum bi-zunûbihim", True), say('say 6:6 27-31 --on', "ve enşe'nâ min ba'dihim qarnen âxarîn"), say('say 6:6 28-31', "min ba'dihim qarnen âxarîn")) + ' '
 "Ölçüm xref 36:31 (emsal olarak basıldı) ve okunmuş 5 ayet. "
 "Ölçüm nakarat3 kalıbı: 'min qabl min' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'fe-ehleknâhum' / 've enşe'nâ' — ayetler arası: yok.",
 "◈K — K1 'l-ardi' (11. kelime), 's-semâ'e' (17. kelime), 'l-enhâra' (21. kelime).",
 "◈B — —",
 "◈D — D1 'e' + 'lem' + IMPF + 'kem' + PERF + 'min' + izafet + 'min' + nekre + PERF + 'fî' + belirli + 'mâ' + 'lem' + IMPF + 'li' + 've' + PERF + belirli + ''alâ' + nekre + 've' + PERF + belirli + IMPF + 'min' + izafet + "
 "'fe' + PERF + 'bi' + izafet + 've' + PERF + 'min' + izafet + nekre + sıfat; "
 "D2 soru, INTG ('e-lem' 1. kelime), NEG ('e-lem' 1. kelime, 'lem' 13. kelime); D3 قرن ×2, مكن ×2, هلك ×2; 36:31 eşi; D4 1P 13 · 2MP 1 · 3FS 1 · 3MP 9, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[6] + "; aktör yok (ölçüm); A2 önceki nesillerin helâki; yeryüzüne yerleştirme, bol yağmur ve ırmaklar; günahlar yüzünden helâk; ardlarından yeni nesiller; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 3 → 1 (ayetler arası); edim geçişi haber → soru (ayetler arası).",
)

D[7] = ("◇ 've lev nezzelnâ 'aleyke kitâben fî qırtâsin fe-lemesûhu bi-eydîhim le-qâle'llezîne keferû in hâzâ illâ sihrun mubîn' — "
 "'ve' + 'lev' + PERF 1P II. bab + ''alâ' + 2MS + nekre 'kitâb' + 'fî' + nekre 'qırtâs' + 'fe' + PERF 3MP I. bab + 3MS + 'bi' + çoğul 'yed' + 3MP + 'le' + PERF 3MS I. bab + 'ellezî' + PERF 3MP I. bab + "
 "'in' + 'hâ' + 'zâ' + 'illâ' + nekre 'sihr' + nekre etken ortaç 'mubîn' "
 "(ölçüm edim şart, kip COND 1 · EMPH 1 · NEG 1 · RES 1; 1P 2 · 2MS 1 · 3MP 5 · 3MS 2; bab I. bab ×3 · II. bab ×1). "
 "Lafız yok; Rab yok; ölçüm '{{2|esmâ مُبِين 16\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET ton denge' — ölçüm MÜHÜRSÜZ ile uyuşmuyor (araç tanımı farkı; muhur_el hayır — ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 'in hâzâ illâ sihrun mubîn', kural 'esmâ adı esmâ dışı göndergeyle → degil' (büyünün sıfatı) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=16 (n z=0,38); ölçüm '{{2|fâsıla مبين → ن, N sınıfı}}' — satır aynen (6:6 ن → 6:7 ن); "
 "ölçüm '{{2|simetri \\[3, 1, 10, 1\\]}}' — satır aynen; ölçüm '{{2|harf 70 → harf3 65, isaret 5}}' — satır aynen; ölçüm '{{2|dış düğüm 2}}' — satır aynen. "
 "Ölçüm COND 1: 'lev' (1. kelime); EMPH 1: 'le-qâle' (9. kelime); NEG 1: 'in' (12. kelime); RES 1: 'illâ' (14. kelime); 've lev' (1.) kelimesindeki 've' REM; 'fe-lemesûhu' (7.) kelimesindeki 'fe' CONJ (okuma). "
 + T[7] + " (okuma). "
 + cumle(say('say 6:7 1-6 --on', "ve lev nezzelnâ 'aleyke kitâben fî qırtâs", True), say('say 6:7 7-8 --on', "fe-lemesûhu bi-eydîhim")) + ' '
 + cumle(say('say 6:7 9-16 --on', "le-qâle'llezîne keferû in hâzâ illâ sihrun mubîn", True), say('say 6:7 9-14', "le-qâle'llezîne keferû in hâzâ illâ"), say('dizi 6 7 9 14', "qâle ellezî kefera in zâ illâ"),
         say('say 6:7 10-16', "llezîne keferû in hâzâ illâ sihrun mubîn"), say('say 6:7 12-16', "in hâzâ illâ sihrun mubîn")) + ' '
 "Ölçüm xref 5:110 (basılmış) ve okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıbı: 'qâle ellezî kefera in zâ illâ' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B3 'eydîhim' (8. kelime).",
 "◈D — D1 've' + 'lev' + PERF + ''alâ' + nekre + 'fî' + nekre + 'fe' + PERF + 'bi' + izafet + 'le' + PERF + 'ellezî' + PERF + 'in' + 'hâ' + 'zâ' + 'illâ' + nekre + nekre; "
 "D2 şart, COND ('lev' 1. kelime), EMPH ('le-qâle' 9. kelime), NEG ('in' 12. kelime), RES ('illâ' 14. kelime); D3 —; 5:110 eşi; D4 1P 2 · 2MS 1 · 3MP 5 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[7] + "; aktör yok (ölçüm); A2 kâğıtta indirilen kitabı elle yoklasalar da inkâr edenlerin büyü demesi; "
 "A3 'in hâzâ illâ sihrun mubîn' (söz içi, 12-16. kelime); "
 "A4 " + BOLUM + "; söz açılır (12. kelime); söz kapanır (16. kelime, ayet içi); şahıs geçişi 1 → 3 (ayetler arası); edim geçişi soru → şart (ayetler arası); "
 "şart → cevap (ayet içi; COND 'lev' 1. kelime: 'lev nezzelnâ' / 'le-qâle' (9. kelime)).",
)

D[8] = ("◇ 've qâlû levlâ unzile 'aleyhi melekun ve lev enzelnâ melekan le-qudiye'l-emru summe lâ yunzarûn' — "
 "'ve' + PERF 3MP I. bab + 'levlâ' + edilgen PERF 3MS IV. bab + ''alâ' + 3MS + nekre 'melek' + 've' + 'lev' + PERF 1P IV. bab + nekre 'melek' + 'le' + edilgen PERF 3MS I. bab + belirli 'emr' + 'summe' + 'lâ' + edilgen IMPF 3MP IV. bab "
 "(ölçüm edim şart, kip COND 1 · EMPH 1 · NEG 1; 1P 2 · 3MP 4 · 3MS 3; bab I. bab ×2 · IV. bab ×3). "
 "Lafız yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=13 (n z=0,06); ölçüm '{{3|EDİLGEN 3/5 fiil, pas z=3,10}}' — satır aynen; ölçüm '{{3|fâsıla ينظرون → ن, N sınıfı}}' — satır aynen (6:7 ن → 6:8 ن); "
 "ölçüm '{{3|simetri \\[3, 2, 6, 1\\]}}' — satır aynen; ölçüm '{{3|harf 57 → harf3 53, isaret 4}}' — satır aynen; ölçüm '{{3|dış düğüm 1}}' — satır aynen. "
 "Ölçüm COND 1: 've lev' (6. kelime); EMPH 1: 'le-qudiye' (9. kelime); NEG 1: 'lâ' (12. kelime); 'levlâ' (2.) morph EXH ölçüm kipinde yok; 've qâlû' (1.) ve 've lev' (6.) kelimelerindeki 've' CONJ; 'summe' (11.) CONJ (okuma). "
 "Kök ikilemesi (ölçüm) ملك ×2 ('melekun' 5. / 'melekan' 8. kelime), نزل ×2 ('unzile' 3. / 'enzelnâ' 7. kelime) (okuma). "
 + T[8] + " (okuma). "
 + cumle(say('say 6:8 1-5 --on', "ve qâlû levlâ unzile 'aleyhi melek", True)) + ' '
 + cumle(say('say 6:8 6-10 --on', "ve lev enzelnâ melekan le-qudiye'l-emr", True), say('say 6:8 9-10 --on', "le-qudiye'l-emr"), say('say 6:8 11-13', "summe lâ yunzarûn")) + ' '
 "Ölçüm xref okunmuş 1 ayet. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + PERF + 'levlâ' + PERF + ''alâ' + nekre + 've' + 'lev' + PERF + nekre + 'le' + PERF + belirli + 'summe' + 'lâ' + IMPF; "
 "D2 şart, COND ('ve lev' 6. kelime), EMPH ('le-qudiye' 9. kelime), NEG ('lâ' 12. kelime); D3 ملك ×2, نزل ×2; D4 1P 2 · 3MP 4 · 3MS 3, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[8] + "; aktör yok (ölçüm); A2 melek indirilmesi isteği; melek indirilseydi işin bitirilmesi ve mühlet verilmemesi; "
 "A3 'levlâ unzile 'aleyhi melekun' (söz içi, 2-5. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (5. kelime, ayet içi); "
 "şart → cevap (ayet içi; COND 'lev' 6. kelime: 've lev enzelnâ melekan' / 'le-qudiye'l-emr' (9. kelime)).",
)

D[9] = ("◇ 've lev ce'alnâhu melekan le-ce'alnâhu raculen ve le-lebesnâ 'aleyhim mâ yelbisûn' — "
 "'ve' + 'lev' + PERF 1P I. bab + 3MS + nekre 'melek' + 'le' + PERF 1P I. bab + 3MS + nekre 'racul' + 've' + 'le' + PERF 1P I. bab + ''alâ' + 3MP + 'mâ' + IMPF 3MP I. bab "
 "(ölçüm edim şart, kip COND 1 · EMPH 2; 1P 6 · 3MP 3 · 3MS 2; bab I. bab ×4). "
 "Lafız yok; Rab yok; esmâ yok (ölçüm); ölçüm '{{4|aktör: adsız `racül` 5\\. sırada}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=9 (n z=-0,36); ölçüm '{{4|fâsıla يلبسون → ن, N sınıfı}}' — satır aynen (6:8 ن → 6:9 ن); "
 "ölçüm '{{4|harf 44 → harf3 42, isaret 2}}' — satır aynen; ölçüm '{{4|dış düğüm 0}}' — satır aynen. "
 "Ölçüm COND 1: 've lev' (1. kelime); EMPH 2: 'le-ce'alnâhu' (4. kelime), 've le-lebesnâ' (6. kelime); 've lev' (1.) ve 've le-lebesnâ' (6.) kelimelerindeki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) جعل ×2 ('ce'alnâhu' 2. / 'le-ce'alnâhu' 4. kelime), لبس ×2 ('le-lebesnâ' 6. / 'yelbisûn' 9. kelime) (okuma). "
 + T[9] + " (okuma). "
 + cumle(say('say 6:9 1-5 --on', "ve lev ce'alnâhu melekan le-ce'alnâhu racul", True), say('say 6:9 6-9 --on', "ve le-lebesnâ 'aleyhim mâ yelbisûn")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'melekan' / 'raculen' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'lev' + PERF + nekre + 'le' + PERF + nekre + 've' + 'le' + PERF + ''alâ' + 'mâ' + IMPF; "
 "D2 şart, COND ('ve lev' 1. kelime), EMPH ('le-ce'alnâhu' 4. kelime, 've le-lebesnâ' 6. kelime); D3 جعل ×2, لبس ×2; D4 1P 6 · 3MP 3 · 3MS 2, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[9] + "; aktör 'raculen' (ölçüm); A2 melek elçinin adam kılınması; karıştırdıkları şeyin onlara karıştırılması; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 3 → 1 (ayetler arası); "
 "şart → cevap (ayet içi; COND 'lev' 1. kelime: 've lev ce'alnâhu melekan' / 'le-ce'alnâhu raculen' (4. kelime)).",
)

D[10] = ("◇ 've le-qadi'stuhzi'e bi-rusulin min qablike fe-hâqa bi'llezîne sexirû minhum mâ kânû bihî yestehzi'ûn' — "
 "'ve' + 'le' + 'qad' + edilgen PERF 3MS X. bab + 'bi' + nekre çoğul 'resûl' + 'min' + 'qabl' + 2MS + 'fe' + PERF 3MS I. bab + 'bi' + 'ellezî' + PERF 3MP I. bab + 'min' + 3MP + 'mâ' + PERF 3MP I. bab + 'bi' + 3MS + IMPF 3MP X. bab "
 "(ölçüm edim haber, kip CERT 1 · EMPH 1; 2MS 1 · 3MP 7 · 3MS 3; bab I. bab ×3 · X. bab ×2). "
 "Lafız yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=13 (n z=0,06); ölçüm '{{5|EDİLGEN 1/5 fiil, pas z=0,81}}' — satır aynen; ölçüm '{{5|fâsıla يستهزءون → ن, N sınıfı}}' — satır aynen (6:9 ن → 6:10 ن); "
 "ölçüm '{{5|simetri \\[3, 7, 10, 1\\]}}' — satır aynen; ölçüm '{{5|harf 60 → harf3 56, isaret 4}}' — satır aynen; ölçüm '{{5|dış düğüm 2}}' — satır aynen; "
 "ölçüm '{{5|esit2 → 21:41 oran 0,9910 kademe YAKIN}}' — satır aynen (21:41 emsal olarak basıldı). "
 "Ölçüm CERT 1 ve EMPH 1: 'le-qadi' (1. kelime); 've le-qadi' (1.) kelimesindeki 've' REM; 'fe-hâqa' (6.) kelimesindeki 'fe' CAUS (okuma). "
 "Kök ikilemesi (ölçüm) هزأ ×2 ('stuhzi'e' 2. / 'yestehzi'ûn' 13. kelime) (okuma). "
 + T[10] + " (okuma). "
 + cumle(say('say 6:10 1-5 --on', "ve le-qadi'stuhzi'e bi-rusulin min qablik", True), say('say 6:10 3-5', "bi-rusulin min qablik"), say('dizi 6 10 3 5', "resûl min qabl")) + ' '
 + cumle(say('say 6:10 6-13 --on', "fe-hâqa bi'llezîne sexirû minhum mâ kânû bihî yestehzi'ûn", True), say('say 6:10 10-13', "mâ kânû bihî yestehzi'ûn"), say('dizi 6 10 10 13', "mâ kâne _ istuhzi'e")) + ' '
 "Ölçüm xref 21:41 (emsal olarak basıldı) ve okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıpları: 'mâ kâne _ istuhzi'e' süzgeç GEÇER, 'resûl min qabl' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'le' + 'qad' + PERF + 'bi' + nekre + 'min' + izafet + 'fe' + PERF + 'bi' + 'ellezî' + PERF + 'min' + 'mâ' + PERF + 'bi' + IMPF; "
 "D2 haber, CERT ('le-qadi' 1. kelime), EMPH ('le-qadi' 1. kelime); D3 هزأ ×2; 21:41 eşi; D4 2MS 1 · 3MP 7 · 3MS 3, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[10] + "; aktör yok (ölçüm); A2 önceki elçilerle alay edilmesi; alay ettikleri şeyin eğlenenleri kuşatması; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 1 → 3 (ayetler arası); edim geçişi şart → haber (ayetler arası).",
)

D[11] = ("◇ 'qul sîrû fi'l-ardi summe'nzurû keyfe kâne 'âqibetu'l-mukezzibîn' — "
 "IMPV 2MS I. bab + IMPV 2MP I. bab + 'fî' + belirli 'ard' + 'summe' + IMPV 2MP I. bab + 'keyfe' + PERF 3MS I. bab + ''âqibe' + belirli çoğul etken ortaç 'mukezzib' "
 "(ölçüm edim emir, kip IMPV 3; 2MP 4 · 2MS 1 · 3MS 1; bab I. bab ×4). "
 "Lafız yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=10 (n z=-0,26); ölçüm '{{6|fâsıla ٱلمكذبين → ن, N sınıfı}}' — satır aynen (6:10 ن → 6:11 ن); "
 "ölçüm '{{6|harf 42 → harf3 40, isaret 2}}' — satır aynen; ölçüm '{{6|dış düğüm 0}}' — satır aynen; "
 "ölçüm '{{6|esit2 → 27:69 oran 0,8974 kademe BENZER}}' — satır aynen (27:69 emsal olarak basıldı). "
 "Ölçüm IMPV 3: 'qul' (1. kelime), 'sîrû' (2. kelime), 'nzurû' (6. kelime); 'summe' (5.) CONJ (okuma). "
 + T[11] + " (okuma). "
 + cumle(say('say 6:11 1-4', "qul sîrû fi'l-ard", True), say('say 6:11 5-10', "summe'nzurû keyfe kâne 'âqibetu'l-mukezzibîn"), say('say 6:11 6-9', "nzurû keyfe kâne 'âqibe")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K1 'l-ardi' (4. kelime).",
 "◈B — —",
 "◈D — D1 IMPV + IMPV + 'fî' + belirli + 'summe' + IMPV + 'keyfe' + PERF + izafet + belirli; "
 "D2 emir, IMPV ('qul' 1. kelime, 'sîrû' 2. kelime, 'nzurû' 6. kelime); D3 —; 27:69 eşi; D4 2MP 4 · 2MS 1 · 3MS 1, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[11] + "; aktör yok (ölçüm); A2 yeryüzünde gezip yalanlayanların sonuna bakma emri; "
 "A3 'sîrû fi'l-ardi summe'nzurû keyfe kâne 'âqibetu'l-mukezzibîn' (söz içi, 2-10. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (10. kelime, ayet içi); şahıs geçişi 3 → 2 (ayetler arası); edim geçişi haber → emir (ayetler arası); bölüm kapanışı.",
)

out = ['# ── blok 6:6-11 (2026-11-19) ──', 'MEAL2 = {']
for n in range(6, 12):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M2 = {']
for n in range(6, 12):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL2); M.update(M2)']
open('/home/claude/yamalar/metin_6_6_11.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

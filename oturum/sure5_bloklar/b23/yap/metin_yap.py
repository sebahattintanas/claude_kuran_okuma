# blok 23 (5:71-74) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b23/say2.txt'
os.environ['OLC'] = '/home/claude/b23/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Tebliğ emri; İsrâiloğullarının misakı; Mesih ve teslis' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 71: "Bir fitne olmayacağını sandılar; bu yüzden kör ve sağır oldular. Sonra Allah onların tövbesini kabul etti; sonra onlardan çoğu kör ve sağır oldu. Allah yaptıklarını görendir.",
 72: "Andolsun, 'Şüphesiz Allah, Meryem oğlu Mesih'tir' diyenler inkâr etmiştir. Mesih dedi ki: 'Ey İsrâiloğulları! Rabbim ve Rabbiniz olan Allah'a kulluk edin. Şüphesiz kim Allah'a ortak koşarsa, Allah ona cenneti haram kılmıştır ve onun barınağı ateştir.' Zalimler için yardımcılardan hiçbiri yoktur.",
 73: "Andolsun, 'Şüphesiz Allah üçün üçüncüsüdür' diyenler inkâr etmiştir. Bir ilahtan başka hiçbir ilah yoktur. Eğer söylediklerinden vazgeçmezlerse, onlardan inkâr edenlere elbette acıklı bir azap dokunacaktır.",
 74: "Allah'a tövbe edip O'ndan bağışlanma dilemezler mi? Allah bağışlayandır, merhamet edendir.",
}

T71 = ("'hasibû' faili 3MP (adsız; 1. kelime); 'tekûne' 3FS (fiil uyumu; 3. kelime — fail 4. kelime); 'fitnetun' ('tekûne' faili; nekre; 4. kelime); ''amû' ve 'sammû' faili 3MP (adsız; 5. ve 6. kelime); "
       "'tâba' 3MS (fiil uyumu; 8. kelime — fail 9. kelime); Allah (lafız; 9. ve 16. kelime); ''aleyhim' 3MP (adsız; 10. kelime); ''amû' ve 'sammû' faili 3MP (adsız; 12. ve 13. kelime; bedel 'kesîrun'); "
       "'kesîrun' (nekre; 14. kelime); 'minhum' 3MP (adsız; 15. kelime); 'ya'melûn' faili 3MP (adsız; 19. kelime)")
T72 = ("'kefera' 3MS (fiil uyumu; 2. kelime — fail 3. kelime); 'llezîne qâlû' ('kefera' faili; 3-4. kelime); 'qâlû' faili 3MP (adsız; 4. kelime); Allah (lafız; 6., 16., 22. ve 25. kelime); "
       "'huve' 3MS (adsız; fasıl zamiri, gönderge lafız; 7. kelime); 'l-mesîhu'bnu meryeme' (adlı kişi; söz içi; 8-10. kelime); 'qâle' 3MS (fiil uyumu; 11. kelime — fail 12. kelime); 'l-mesîhu' ('qâle' faili; adlı kişi; 12. kelime); "
       "'benî isrâ'île' (nida edilen; adlı kavim; 13-14. kelime); muhatap 2MP (adsız; söz içi; 15. ve 18. kelime — ''budu', 'rabbekum'); konuşan 1S (adsız; söz içi; 17. kelime); Rab (17. ve 18. kelime — 'rabbî', 'rabbekum'); "
       "şe'n zamiri 3MS (adsız; 19. kelime); şart ismi (20. kelime); 'yuşrik' faili 3MS (adsız; gönderge 'men', 21. kelime); 'harrama' 3MS (fiil uyumu; 24. kelime — fail 25. kelime); "
       "''aleyhi' 3MS (adsız; gönderge 'men', 26. kelime); cennet (adlı yer; 27. kelime); 'me'vâhu' 3MS (adsız; gönderge 'men', 28. kelime)")
T73 = ("'kefera' 3MS (fiil uyumu; 2. kelime — fail 3. kelime); 'llezîne qâlû' ('kefera' faili; 3-4. kelime); 'qâlû' faili 3MP (adsız; 4. kelime); Allah (lafız; söz içi; 6. kelime); "
       "'yentehû' faili 3MP (adsız; 17. kelime); 'yeqûlûne' faili 3MP (adsız; 19. kelime); 'yemessenne' 3MS (fiil uyumu; 20. kelime — fail 24. kelime); ''azâbun' ('yemessenne' faili; nekre; 24. kelime); "
       "'llezîne keferû' ('yemessenne' mef'ûlü; 21-22. kelime); 'keferû' faili 3MP (adsız; 22. kelime); 'minhum' 3MP (adsız; 23. kelime)")
T74 = ("'yetûbûne' faili 3MP (adsız; 2. kelime); Allah (lafız; 4. ve 6. kelime); 'yestağfirûnehû' faili 3MP (adsız; 5. kelime); 'yestağfirûnehû' mef'ûlü 3MS (adsız; gönderge lafız, 5. kelime)")

D = {}
D[71] = ("◇ 've hasibû ellâ tekûne fitnetun fe-'amû ve sammû summe tâba'llâhu 'aleyhim summe 'amû ve sammû kesîrun minhum ve'llâhu basîrun bi-mâ ya'melûn' — "
 "'ve' + PERF 3MP I. bab + 'en' + 'lâ' + IMPF 3FS I. bab + nekre 'fitne' + 'fe' + PERF 3MP I. bab + 've' + PERF 3MP I. bab + 'summe' + PERF 3MS I. bab + lafız + ''alâ' + 3MP + 'summe' + PERF 3MP I. bab + 've' + PERF 3MP I. bab + nekre 'kesîr' + 'min' + 3MP + 've' + lafız + nekre 'basîr' + 'bi' + 'mâ' + IMPF 3MP I. bab "
 "(ölçüm edim haber, kip NEG 1; 3FS 1 · 3MP 14 · 3MS 1; bab I. bab ×8). "
 "Allah lafzı 9. ve 16. sırada (ölçüm allah z=1,58); Rab yok; ölçüm '{{1|esmâ بَصِير 17\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton denge' (uyuşmuyor) — esma_el kaydı 'ilahi' — 've'llâhu basîrun', kural ''ve'llâhu X' kuralı → ilahi' (lafzın haberi) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=19 (n z=0,70); ölçüm '{{1|fâsıla يعملون → ن, N sınıfı}}' — satır aynen; ölçüm '{{1|sayı işareti \\S+}}' — satır aynen ('kesîrun' 14. kelime); "
 "ölçüm '{{1|simetri \\[3, 5, 12, 1\\]}}' — satır aynen; ölçüm '{{1|harf 87 → harf3 78, isaret 9}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen. "
 "Ölçüm NEG 1: 'lâ' (2. kelime; 'ellâ' içinde); 've hasibû' (1.), 've sammû' (6. ve 13.)'daki 've' CONJ, 'summe' (7. ve 11.) CONJ, 'fe-'amû' (5.)'daki 'fe' CAUS, 've'llâhu' (16.)'daki 've' REM (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 (lafız 9., 16. kelime), صمم ×2 ('sammû' 6. / 13. kelime), عمي ×2 (''amû' 5. / 12. kelime) (okuma). "
 + T71 + " (okuma). "
 + cumle(say('say 5:71 1-4 --on', "ve hasibû ellâ tekûne fitne", True), say('say 5:71 2-4', "ellâ tekûne fitne"), say('say 5:71 3-4', "tekûne fitne")) + ' '
 + cumle(say('say 5:71 5-6 --on', "fe-'amû ve sammû", True), say('dizi 5 71 5 6', "'amiye sammu"), say('lem 5:71:6', "sammu")) + ' '
 + cumle(say('say 5:71 7-10', "summe tâba'llâhu 'aleyhim", True), say('say 5:71 8-10', "tâba'llâhu 'aleyhim"), say('dizi 5 71 8 10', "tâbe allâh 'alâ")) + ' '
 + cumle(say('say 5:71 11-13', "summe 'amû ve sammû", True), say('say 5:71 12-13', "'amû ve sammû"), say('say 5:71 12-15', "'amû ve sammû kesîrun minhum"), say('say 5:71 14-15', "kesîrun minhum")) + ' '
 + cumle(say('say 5:71 16-19 --on', "ve'llâhu basîrun bi-mâ ya'melûn", True), say('say 5:71 17-19', "basîrun bi-mâ ya'melûn"), say('dizi 5 71 16 19', "allâh basîr mâ 'amile")) + ' '
 "Ölçüm '{{1|bağ: YOK \\(esit2, nakarat3, xref üçü de boş\\)}}' — satır aynen. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'fe-'amû ve sammû' / 'summe tâba'llâhu 'aleyhim' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 'basîrun' (17. kelime); B4 —.",
 "◈D — D1 've' + PERF + 'en' + 'lâ' + IMPF + nekre + 'fe' + PERF + 've' + PERF + 'summe' + PERF + lafız + ''alâ' + 'summe' + PERF + 've' + PERF + nekre + 'min' + 've' + lafız + nekre + 'bi' + 'mâ' + IMPF; "
 "D2 haber, NEG ('lâ' 2. kelime); D3 أله ×2, صمم ×2, عمي ×2; 2:96 eşi; D4 3FS 1 · 3MP 14 · 3MS 1, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T71 + "; aktör yok (ölçüm); A2 fitne olmayacağı sanısı; körlük ve sağırlık; tövbe kabulü; yaptıklarını görme; A3 —; "
 "A4 " + BOLUM + "; —.",
)

D[72] = ("◇ 'le-qad kefera'llezîne qâlû inna'llâhe huve'l-mesîhu'bnu meryeme ve qâle'l-mesîhu yâ benî isrâ'île 'budu'llâhe rabbî ve rabbekum innehû men yuşrik bi'llâhi fe-qad harrama'llâhu 'aleyhi'l-cennete ve me'vâhu'n-nâru ve mâ li'z-zâlimîne min ensâr' — "
 "'le' + 'qad' + PERF 3MS I. bab + 'ellezî' + PERF 3MP I. bab + 'inne' + lafız + 'huve' + belirli özel ad 'mesîh' + 'ibn' + özel ad 'meryem' + 've' + PERF 3MS I. bab + belirli özel ad 'mesîh' + 'yâ' + çoğul 'buneyy' (morph LEM ham biçim) + özel ad 'isrâ'îl' + IMPV 2MP I. bab + lafız + 'rabb' + 1S + 've' + 'rabb' + 2MP + "
 "'inne' + 3MS + 'men' + IMPF 3MS IV. bab + 'bi' + lafız + 'fe' + 'qad' + PERF 3MS II. bab + lafız + ''alâ' + 3MS + belirli özel ad 'cenne' + 've' + 'me'vâ' + 3MS + belirli 'nâr' + 've' + 'mâ' + 'li' + belirli çoğul ortaç 'zâlim' + 'min' + nekre çoğul 'nasîr' "
 "(ölçüm edim emir, nida, şart, kip CERT 2 · COND 1 · EMPH 1 · IMPV 1 · NEG 1 · VOC 1; 1S 1 · 2MP 3 · 3MP 2 · 3MS 8; bab I. bab ×4 · II. bab ×1 · IV. bab ×1). "
 "Allah lafzı 6., 16., 22. ve 25. sırada (ölçüm allah z=1,90); ölçüm '{{2|رَبّ 17, 18\\. sırada \\(rab z=0,97\\)}}' — satır aynen ('rabbî', 'rabbekum', Rab adı); ölçüm '{{2|esmâ نَصِير 33\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET ton cemâl' (uyuşmuyor) — esma_el kaydı 'degil' — 've mâ li'z-zâlimîne min ensâr', kural 'çoğul insan göndergeli → degil' (yardımcılar) (okuma); "
 "ölçüm aktör '{{2|adlı مَسِيح 8\\. sırada \\(kisi, rol fail\\+konusan\\)}}', '{{2|adlı مَرْيَم 10\\. sırada \\(kisi, rol mecrur\\)}}', '{{2|adlı مَسِيح 12\\. sırada \\(kisi, rol fail\\+konusan\\)}}', '{{2|adlı إِسْرائِيل 14\\. sırada \\(kavim, rol mecrur\\)}}' ve '{{2|adlı \\S+ 27\\. sırada \\(yer, rol meful\\)}}' — satır aynen. "
 "Ölçüm yıldız ★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=33 (n z=2,19); ölçüm '{{2|fâsıla أنصار → ر, R sınıfı — KAFİYE KIRILMASI}}' — satır aynen (kafiye kırılması: 5:71 ن → 5:72 ر); "
 "ölçüm '{{2|simetri \\[3, 1, 5, 1\\]}}' — satır aynen; ölçüm '{{2|İÇ düğüm 1}}' — satır aynen; ölçüm '{{2|harf 143 → harf3 136, isaret 7}}' — satır aynen; ölçüm '{{2|dış düğüm 2}}' — satır aynen. "
 "Ölçüm CERT 2: 'qad' (1. ve 23. kelime); EMPH 1: 'le' (1. kelime); IMPV 1: ''budu' (15. kelime); VOC 1: 'yâ' (13. kelime); COND 1: 'men' (20. kelime); NEG 1: 'mâ' (30. kelime); "
 "'ve qâle' (11.) ve 've mâ' (30.)'daki 've' REM, 've rabbekum' (18.)'daki 've' CONJ, 've me'vâhu' (28.)'daki 've' CIRC, 'fe-qad' (23.)'daki 'fe' RSLT (okuma). "
 "Kök ikilemesi (ölçüm) أله ×4 (lafız 6., 16., 22., 25. kelime), بني ×2 ('bnu' 9. / 'benî' 13. kelime), ربب ×2 ('rabbî' 17. / 'rabbekum' 18. kelime), قول ×2 ('qâlû' 4. / 'qâle' 11. kelime), مسح ×2 ('l-mesîhu' 8. / 12. kelime) (okuma). "
 + T72 + " (okuma). "
 + cumle(say('say 5:72 1-11 --on', "le-qad kefera'llezîne qâlû inna'llâhe huve'l-mesîhu'bnu meryeme ve qâle", True), say('dizi 5 72 1 11', "qad kefera ellezî qâle inne allâh _ mesîh ibn meryem qâle"), say('say 5:72 1-6', "le-qad kefera'llezîne qâlû inna'llâh"),
         say('say 5:72 2-6', "kefera'llezîne qâlû inna'llâh"), say('dizi 5 72 2 6', "kefera ellezî qâle inne allâh")) + ' '
 + cumle(say('say 5:72 8-10', "l-mesîhu'bnu meryem", True), say('dizi 5 72 8 10', "mesîh ibn meryem")) + ' '
 + cumle(say('say 5:72 11-14 --on', "ve qâle'l-mesîhu yâ benî isrâ'îl", True), say('say 5:72 13-14', "yâ benî isrâ'îl"), say('say 5:72 15-18 --on', "'budu'llâhe rabbî ve rabbekum"), say('dizi 5 72 15 18', "'abede allâh rabb rabb"), say('say 5:72 16-18 --on', "llâhe rabbî ve rabbekum")) + ' '
 + cumle(say('say 5:72 19-22', "innehû men yuşrik bi'llâh", True), say('say 5:72 20-22', "men yuşrik bi'llâh"), say('say 5:72 23-27 --on', "fe-qad harrama'llâhu 'aleyhi'l-cenne"), say('say 5:72 24-27', "harrama'llâhu 'aleyhi'l-cenne"), say('say 5:72 28-29 --on', "ve me'vâhu'n-nâr")) + ' '
 + cumle(say('say 5:72 30-33 --on', "ve mâ li'z-zâlimîne min ensâr", True), say('say 5:72 31-33', "li'z-zâlimîne min ensâr"), say('dizi 5 72 31 33', "zâlim min nasîr")) + ' '
 "Ölçüm xref 5:17 (emsal olarak basıldı) ve okunmuş başka ayetler. "
 "Ölçüm nakarat3 kalıpları: 'le-qad kefera'llezîne qâlû inna'llâhe huve'l-mesîhu'bnu meryeme ve qâle', 'le-qad kefera'llezîne qâlû inna'llâh', ''budu'llâhe rabbî ve rabbekum' ve 'l-mesîhu'bnu meryem' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'l-cennete' / 'n-nâru' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'le' + 'qad' + PERF + 'ellezî' + PERF + 'inne' + lafız + belirli + izafet + özel ad + 've' + PERF + belirli + 'yâ' + izafet + özel ad + IMPV + lafız + izafet + 've' + izafet + 'inne' + 'men' + IMPF + 'bi' + lafız + 'fe' + 'qad' + PERF + lafız + ''alâ' + belirli + 've' + izafet + belirli + 've' + 'mâ' + 'li' + belirli + 'min' + nekre; "
 "D2 emir, nida, şart, IMPV (''budu' 15. kelime), VOC ('yâ' 13. kelime), COND ('men' 20. kelime), NEG ('mâ' 30. kelime), CERT ('qad' 1. ve 23. kelime), EMPH ('le' 1. kelime); D3 أله ×4, بني ×2, ربب ×2, قول ×2, مسح ×2; 5:17 ve 3:192 eşleri; D4 1S 1 · 2MP 3 · 3MP 2 · 3MS 8, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T72 + "; aktör Mesih, Meryem, İsrâiloğulları ve cennet (ölçüm); A2 inkâr; Mesih hakkında söz; Mesih'in sözü; kulluk emri; ortak koşma; cennetin haram kılınması; ateş; yardımcısızlık; "
 "A3 'inna'llâhe huve'l-mesîhu'bnu meryem' (söz içi, 5-10. kelime); 'yâ benî isrâ'île 'budu'llâhe' ile açılan söz (söz içi, 13-29. kelime); "
 "A4 " + BOLUM + "; edim geçişi haber → emir, nida, şart (ayetler arası); şahıs geçişi yok; söz açılır (5. kelime); söz kapanır (10. kelime, ayet içi); söz açılır (13. kelime); söz kapanır (29. kelime, ayet içi); "
 "şart → cevap (ayet içi; COND 'men' 20. kelime: 'men yuşrik bi'llâhi' / 'fe-qad harrama'llâhu 'aleyhi'l-cennete' (23. kelime)).",
)

D[73] = ("◇ 'le-qad kefera'llezîne qâlû inna'llâhe sâlisu selâsetin ve mâ min ilâhin illâ ilâhun vâhidun ve in lem yentehû 'ammâ yeqûlûne le-yemessenne'llezîne keferû minhum 'azâbun elîm' — "
 "'le' + 'qad' + PERF 3MS I. bab + 'ellezî' + PERF 3MP I. bab + 'inne' + lafız + 'sâlis' + nekre 'selâse' + 've' + 'mâ' + 'min' + nekre 'ilâh' + 'illâ' + nekre 'ilâh' + nekre 'vâhid' + 've' + 'in' + 'lem' + IMPF 3MP VIII. bab + ''an' + 'mâ' + IMPF 3MP I. bab + "
 "'le' + IMPF 3MS I. bab + te'kid nûnu + 'ellezî' + PERF 3MP I. bab + 'min' + 3MP + nekre ''azâb' + nekre 'elîm' "
 "(ölçüm edim şart, kip CERT 1 · COND 1 · EMPH 3 · NEG 2 · RES 1, biçim HASR; 3MP 9 · 3MS 2; bab I. bab ×5 · VIII. bab ×1). "
 "Allah lafzı 6. sırada (ölçüm allah z=0,27); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=25 (n z=1,34); ölçüm '{{3|fâsıla أليم → م, N sınıfı}}' — satır aynen (kafiye: 5:72 ر → 5:73 م); ölçüm '{{3|sayı işareti \\S+, \\S+, \\S+}}' — satır aynen ('sâlisu' 7., 'selâsetin' 8., 'vâhidun' 14. kelime); "
 "ölçüm '{{3|simetri \\[4, 1, 16, 1\\]}}' — satır aynen; ölçüm '{{3|harf 102 → harf3 94, isaret 8}}' — satır aynen; ölçüm '{{3|dış düğüm 3}}' — satır aynen. "
 "Ölçüm CERT 1: 'qad' (1. kelime); EMPH 3: 'le' (1. kelime), 'le' ve te'kid nûnu ('le-yemessenne' 20. kelime); NEG 2: 'mâ' (9.), 'lem' (16. kelime); RES 1: 'illâ' (12. kelime); COND 1: 'in' (15. kelime); 've mâ' (9.) ve 've in' (15.)'daki 've' REM (okuma). "
 "Kök ikilemesi (ölçüm) أله ×3 (lafız 6., 'ilâhin' 11., 'ilâhun' 13. kelime), ثلث ×2 ('sâlisu' 7. / 'selâsetin' 8. kelime), قول ×2 ('qâlû' 4. / 'yeqûlûne' 19. kelime), كفر ×2 ('kefera' 2. / 'keferû' 22. kelime) (okuma). "
 + T73 + " (okuma). "
 + cumle(say('say 5:73 1-8 --on', "le-qad kefera'llezîne qâlû inna'llâhe sâlisu selâse", True), say('say 5:73 1-6', "le-qad kefera'llezîne qâlû inna'llâh"), say('dizi 5 73 2 6', "kefera ellezî qâle inne allâh"), say('say 5:73 7-8', "sâlisu selâse")) + ' '
 + cumle(say('say 5:73 9-14 --on', "ve mâ min ilâhin illâ ilâhun vâhid", True), say('say 5:73 10-14', "min ilâhin illâ ilâhun vâhid"), say('say 5:73 13-14', "ilâhun vâhid")) + ' '
 + cumle(say('say 5:73 15-19 --on', "ve in lem yentehû 'ammâ yeqûlûn", True), say('say 5:73 16-19', "lem yentehû 'ammâ yeqûlûn"), say('say 5:73 18-19', "'ammâ yeqûlûn")) + ' '
 + cumle(say('say 5:73 20-25 --on', "le-yemessenne'llezîne keferû minhum 'azâbun elîm", True), say('say 5:73 21-23', "llezîne keferû minhum"), say('dizi 5 73 21 23', "ellezî kefera min"), say('say 5:73 24-25', "'azâbun elîm")) + ' '
 "Ölçüm xref 9:90 (emsal olarak basıldı) ve okunmuş başka ayetler. "
 "Ölçüm nakarat3 kalıpları: 'le-qad kefera'llezîne qâlû inna'llâh' süzgeç GEÇER; 'llezîne keferû minhum' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'sâlisu selâsetin' / 'ilâhun vâhidun' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'le' + 'qad' + PERF + 'ellezî' + PERF + 'inne' + lafız + izafet + nekre + 've' + 'mâ' + 'min' + nekre + 'illâ' + nekre + nekre + 've' + 'in' + 'lem' + IMPF + ''an' + 'mâ' + IMPF + 'le' + IMPF + 'ellezî' + PERF + 'min' + nekre + nekre; "
 "D2 şart, COND ('in' 15. kelime), NEG ('mâ' 9., 'lem' 16. kelime), RES ('illâ' 12. kelime), CERT ('qad' 1. kelime), EMPH ('le' 1. kelime, 'le-yemessenne' 20. kelime), biçim HASR; D3 أله ×3, ثلث ×2, قول ×2, كفر ×2; 9:90 eşi; D4 3MP 9 · 3MS 2, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T73 + "; aktör yok (ölçüm); A2 inkâr; teslis sözü; bir ilah; vazgeçme şartı; acıklı azap; "
 "A3 'inna'llâhe sâlisu selâsetin' (söz içi, 5-8. kelime); "
 "A4 " + BOLUM + "; edim geçişi emir, nida, şart → şart (ayetler arası); şahıs geçişi yok; söz açılır (5. kelime); söz kapanır (8. kelime, ayet içi); "
 "şart → cevap (ayet içi; COND 'in' 15. kelime: 've in lem yentehû 'ammâ yeqûlûne' / 'le-yemessenne'llezîne keferû minhum 'azâbun elîm' (20. kelime)).",
)

D[74] = ("◇ 'e-fe-lâ yetûbûne ile'llâhi ve yestağfirûnehû ve'llâhu ğafûrun rahîm' — "
 "'e' + 'fe' + 'lâ' + IMPF 3MP I. bab + 'ilâ' + lafız + 've' + IMPF 3MP X. bab + 3MS + 've' + lafız + nekre 'ğafûr' + nekre 'rahîm' "
 "(ölçüm edim soru, kip INTG 1 · NEG 1; 3MP 4 · 3MS 1; bab I. bab ×1 · X. bab ×1). "
 "Allah lafzı 4. ve 6. sırada (ölçüm allah z=4,47); Rab yok; ölçüm '{{4|esmâ غَفُور 7\\. sırada, SON konum, MÜHÜR \\| رَحِيم 8\\. sırada, SON konum, MÜHÜR}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET (ÇİFT) ton cemâl' (uyuşuyor) — esma_el kaydı 'ilahi' — 've'llâhu ğafûrun rahîm', kural ''ve'llâhu X' kuralı → ilahi' (lafzın haberi) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=8 (n z=-0,47); ölçüm '{{4|fâsıla رحيم → م, N sınıfı}}' — satır aynen; ölçüm '{{4|harf 44 → harf3 40, isaret 4}}' — satır aynen; ölçüm '{{4|dış düğüm 0}}' — satır aynen. "
 "Ölçüm INTG 1: 'e' (1. kelime); NEG 1: 'lâ' (1. kelime); 'fe-lâ' (1.)'daki 'fe' SUP, 've yestağfirûnehû' (5.)'daki 've' CONJ, 've'llâhu' (6.)'daki 've' REM (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 (lafız 4., 6. kelime), غفر ×2 ('yestağfirûnehû' 5. / 'ğafûrun' 7. kelime) (okuma). "
 + T74 + " (okuma). "
 + cumle(say('say 5:74 1-5', "e-fe-lâ yetûbûne ile'llâhi ve yestağfirûneh", True), say('say 5:74 2-4', "yetûbûne ile'llâh"), say('say 5:74 2-5', "yetûbûne ile'llâhi ve yestağfirûneh"), say('dizi 5 74 2 5', "tâbe ilâ allâh istağfere")) + ' '
 + cumle(say('say 5:74 6-8 --on', "ve'llâhu ğafûrun rahîm", True), say('say 5:74 7-8', "ğafûrun rahîm"), say('dizi 5 74 6 8', "allâh ğafûr rahîm")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: 've'llâhu ğafûrun rahîm' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'e' + 'fe' + 'lâ' + IMPF + 'ilâ' + lafız + 've' + IMPF + 've' + lafız + nekre + nekre; "
 "D2 soru, INTG ('e' 1. kelime), NEG ('lâ' 1. kelime); D3 أله ×2, غفر ×2; D4 3MP 4 · 3MS 1, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T74 + "; aktör yok (ölçüm); A2 tövbe; bağışlanma dileme; bağışlama ve merhamet; A3 —; "
 "A4 " + BOLUM + "; edim geçişi şart → soru (ayetler arası); şahıs geçişi yok.",
)

out = ['# ── blok 5:71-74 (2026-11-16) ──', 'MEAL23 = {']
for n in range(71, 75):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M23 = {']
for n in range(71, 75):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL23); M.update(M23)']
open('/home/claude/yamalar/metin_5_71_74.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

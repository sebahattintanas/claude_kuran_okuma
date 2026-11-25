# sûre 7 blok 13 (7:44-47) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os, re
os.environ['SAY2'] = '/home/claude/b13/say2.txt'
os.environ['OLC'] = '/home/claude/b13/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Cennet ehli, ateş ehli ve A'râf'takiler' bölümünde"
_OL = [l.replace('**', '') for l in open(os.environ['OLC'], encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK1 = _esc(re.search(r'aktör: adlı .*?rol mecrur\)', _OL[0]).group(0))
_AK3 = _esc(re.search(r'aktör: adlı .*?rol mecrur\)', _OL[2]).group(0))


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 44: "Bahçenin halkı ateşin halkına seslendi ki: Rabbimizin bize vaat ettiğini gerçek bulduk; siz Rabbinizin vaat ettiğini gerçek buldunuz mu? Dediler ki: Evet. Bunun üzerine aralarında bir duyurucu duyurdu ki: Allah'ın laneti zalimlerin üzerinedir.",
 45: "Onlar Allah'ın yolundan alıkoyan, onu eğri göstermek isteyen ve âhireti inkâr edenlerdir.",
 46: "Aralarında bir perde vardır ve A'râf üzerinde herkesi simalarından tanıyan adamlar vardır. Bahçenin halkına seslendiler ki: Selâm size; onlar oraya girmediler, ama umuyorlar.",
 47: "Gözleri ateşin halkı tarafına çevrildiğinde dediler ki: Rabbimiz, bizi zalim kavimle beraber kılma.",
}

T = {}
T[44] = ("'ve nâdâ' 3MS (fiil uyumu; 1. kelime — fail 2. kelime); konuşan 1P (adsız; söz içi; 'vecednâ' — 8. kelime); 've'adenâ' 3MS (fiil uyumu; söz içi; 10. kelime — fail 11. kelime); konuşan 1P eki (adsız; söz içi; 've'adenâ', 'rabbunâ' — 10. ve 11. kelime); "
         "muhatap 2MP (adsız; söz içi; 'vecedtum' — 14. kelime); 've'ade' 3MS (fiil uyumu; söz içi; 16. kelime — fail 17. kelime); muhatap 2MP eki (adsız; söz içi; 'rabbukum' — 17. kelime); 'qâlû' 3MP (adsız; gönderge 'ashâbe'n-nâri' 4. kelime, 19. kelime); "
         "'fe-ezzene' 3MS (fiil uyumu; 21. kelime — fail 22. kelime); 'beynehum' 3MP eki (adsız; tartışmalı; gönderge 'ashâbu'l-cenneti' 2. kelime, 23. kelime)")
T[45] = ("'yasuddûne', 've yebğûnehâ' 3MP (adsız; gönderge 7:44 28. kelime — 2. ve 6. kelime); 've yebğûnehâ' 3FS eki (adsız; tartışmalı; cins uyumsuz; gönderge 'sebîli' 4. kelime, 6. kelime); 'hum' 3MP (adsız; gönderge 7:44 28. kelime, 8. kelime)")
T[46] = ("'ve beynehumâ' 3D eki (adsız; tartışmalı; gönderge 7:44 2. kelime, 1. kelime); 'ya'rifûne', 've nâdev' 3MP (adsız; gönderge 'ricâlun' 5. kelime — 6. ve 9. kelime); 'bi-sîmâhum' 3MP eki (adsız; tartışmalı; sayı uyumsuz; gönderge 'kullen' 7. kelime, 8. kelime); "
         "muhatap 2MP eki (adsız; söz içi; ''aleykum' — 14. kelime); 'yedxulûhâ' 3MP (adsız; tartışmalı; gönderge 'ricâlun' 5. kelime, 16. kelime); 'yedxulûhâ' 3FS eki (adsız; gönderge 'l-cenneti' 11. kelime, 16. kelime); "
         "'hum', 'yatma'ûn' 3MP (adsız; tartışmalı; gönderge 'ricâlun' 5. kelime — 17. ve 18. kelime)")
T[47] = ("'surifet' 3FS (adsız; edilgen, naib-i faili 'ebsâruhum' 3. kelime, 2. kelime); 'ebsâruhum' 3MP eki (adsız; tartışmalı; gönderge 7:46 5. kelime, 3. kelime); 'qâlû' 3MP (adsız; tartışmalı; gönderge 7:46 5. kelime, 7. kelime); "
         "konuşan 1P eki (adsız; söz içi; 'rabbenâ', 'tec'alnâ' — 8. ve 10. kelime); muhatap 2MS (adsız; söz içi; 'tec'alnâ' — 10. kelime)")

D = {}
D[44] = ("◇ 've nâdâ ashâbu'l-cenneti ashâbe'n-nâri en qad vecednâ mâ ve'adenâ rabbunâ haqqan fe-hel vecedtum mâ ve'ade rabbukum haqqan qâlû na'am fe-ezzene mu'ezzinun beynehum en la'netu'llâhi 'ale'z-zâlimîn' — "
 "'ve' + PERF 3MS III. bab + 'ashâb' + belirli 'cenne' + 'ashâb' + belirli 'nâr' + 'en' + 'qad' + PERF 1P I. bab + 'mâ' + PERF 3MS I. bab + 1P + 'rabb' + 1P + nekre 'haqq' + 'fe' + 'hel' + PERF 2MP I. bab + 'mâ' + PERF 3MS I. bab + 'rabb' + 2MP + nekre 'haqq' + PERF 3MP I. bab + 'na'am' + "
 "'fe' + PERF 3MS II. bab + nekre etken ortaç 'mu'ezzin' + 'beyn' + 3MP + 'en' + 'la'ne' + 'allâh' + ''alâ' + belirli çoğul etken ortaç 'zâlim' "
 "(ölçüm edim soru, kip CERT 1 · INTG 1; 1P 4 · 2MP 3 · 3MP 3 · 3MS 4; bab I. bab ×5 · II. bab ×1 · III. bab ×1). "
 "Allah lafzı 26. sırada (ölçüm allah z=0,19); Rab 11. ve 17. sırada (ölçüm rab z=1,20); esmâ yok (ölçüm); ölçüm '{{1|" + _AK1 + "}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{1|yıldız ★}}' — satır aynen (kaynak n, z=1,65); n=28 (n z=1,65); ölçüm '{{1|fâsıla " + _F[0] + " → ن, N sınıfı}}' — satır aynen (7:43 ن → 7:44 ن); "
 "ölçüm '{{1|simetri \\[6, 8, 14, 1\\]}}' — satır aynen; ölçüm '{{1|harf 113 → harf3 107, isaret 6}}' — satır aynen; ölçüm '{{1|dış düğüm 3}}' — satır aynen. "
 "Ölçüm CERT 1: 'qad' (7. kelime); INTG 1: 'fe-hel' (13. kelime; 'hel'); "
 "'ve nâdâ' (1.) kelimesindeki 've' CONJ; 'en' (6.) INT; 'mâ' (9.) REL; 'fe-hel' (13.) kelimesindeki 'fe' REM; 'mâ' (15.) REL; 'na'am' (20.) ANS; 'fe-ezzene' (21.) kelimesindeki 'fe' REM; 'beynehum' (23.) LOC; 'en' (24.) INT (okuma). "
 "Kök ikilemesi (ölçüm) أذن ×2 ('fe-ezzene' 21. / 'mu'ezzinun' 22. kelime); حقق ×2 ('haqqan' 12. / 'haqqan' 18. kelime); ربب ×2 ('rabbunâ' 11. / 'rabbukum' 17. kelime); صحب ×2 ('ashâbu' 2. / 'ashâbe' 4. kelime); وجد ×2 ('vecednâ' 8. / 'vecedtum' 14. kelime); وعد ×2 ('ve'adenâ' 10. / 've'ade' 16. kelime) (okuma). "
 + T[44] + " (okuma). "
 + cumle(say('say 7:44 1-6', "ve nâdâ ashâbu'l-cenneti ashâbe'n-nâri en", True), say('say 7:44 1-3', "ve nâdâ ashâbu'l-cenneti"), say('dizi 7 44 1 3', "nâdâ ashâb cenne"), say('say 7:44 2-3', "ashâbu'l-cenneti"), say('say 7:44 4-5', "ashâbe'n-nâri"), say('dizi 7 44 4 5', "ashâb nâr")) + ' '
 + cumle(say('say 7:44 7-12', "qad vecednâ mâ ve'adenâ rabbunâ haqqan", True), say('say 7:44 13-18', "fe-hel vecedtum mâ ve'ade rabbukum haqqan"), say('say 7:44 11-13', "rabbunâ haqqan fe-hel"), say('dizi 7 44 11 13', "rabb haqq hel")) + ' '
 + cumle(say('say 7:44 21-24', "fe-ezzene mu'ezzinun beynehum en", True), say('say 7:44 25-28', "la'netu'llâhi 'ale'z-zâlimîn"), say('dizi 7 44 25 28', "la'ne allâh 'alâ zâlim"), say('say 7:44 26-28', "llâhi 'ale'z-zâlimîn")) + ' ' +
 "Ölçüm xref 11:18 (emsal olarak basıldı), okunmuş 2 ayet. "
 "Ölçüm nakarat3 kalıbı: 'nâdâ ashâb cenne' süzgeç GEÇMEZ; 'rabb haqq hel' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + PERF + izafet + belirli + izafet + belirli + 'en' + 'qad' + PERF + 'mâ' + PERF + izafet + nekre + 'fe' + 'hel' + PERF + 'mâ' + PERF + izafet + nekre + PERF + 'na'am' + 'fe' + PERF + nekre + izafet + 'en' + izafet + lafız + ''alâ' + belirli; "
 "D2 soru; CERT ('qad' 7. kelime), INTG ('fe-hel' 13. kelime); D3 11:18 eşi, أذن ×2, حقق ×2, ربب ×2, صحب ×2, وجد ×2, وعد ×2; D4 1P 4 · 2MP 3 · 3MP 3 · 3MS 4, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[44] + "; aktör adlı 'l-cenneti' (3. kelime; ölçüm rol mecrur); A2 bahçe halkının ateş halkına Rablerinin vaadini gerçek bulduklarını bildirip sorması; evet cevabı; aralarında bir duyurucunun Allah'ın lanetini zalimlere duyurması; "
 "A3 'qad vecednâ mâ ve'adenâ rabbunâ haqqan fe-hel vecedtum mâ ve'ade rabbukum haqqan' (söz biçimli içerik, 7-18. kelime); 'na'am' (söz içi, 20. kelime); 'la'netu'llâhi 'ale'z-zâlimîn' (söz biçimli içerik, 25-28. kelime); "
 "A4 " + BOLUM + "; soru → cevap (ayet içi; INTG 'hel' 13. kelime: 'vecedtum' / 'na'am' (20. kelime)); "
 "şahıs geçişi 1 → 3 (ayetler arası); edim geçişi şart → soru (ayetler arası).",
)

D[45] = ("◇ 'llezîne yasuddûne 'an sebîli'llâhi ve yebğûnehâ 'ivecen ve hum bi'l-âxirati kâfirûn' — "
 "'ellezî' + IMPF 3MP I. bab + ''an' + 'sebîl' + 'allâh' + 've' + IMPF 3MP I. bab + 3FS + nekre ''iveç' + 've' + 'hum' + 'bi' + belirli 'âxir' + çoğul etken ortaç 'kâfir' "
 "(ölçüm edim haber, kip yok; 3FS 1 · 3MP 5; bab I. bab ×2). "
 "Allah lafzı 5. sırada (ölçüm allah z=1,47); Rab yok; ölçüm '{{2|esmâ آخِر 9. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton denge' (uyuşmuyor) — esma_el kaydı 'degil' — 've hum bi'l-âxirati kâfirûn', kural 'esmâ adı esmâ dışı göndergeyle → degil' (âhiret günü) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=10 (n z=-0,26); ölçüm '{{2|fâsıla " + _F[1] + " → ن, N sınıfı}}' — satır aynen (7:44 ن → 7:45 ن); "
 "ölçüm '{{2|harf 49 → harf3 48, isaret 1}}' — satır aynen; ölçüm '{{2|dış düğüm 2}}' — satır aynen; ölçüm '{{2|esit2 → 11:19 oran 0,9792 kademe YAKIN}}' — satır aynen. "
 "Ölçüm kip yok; "
 "'llezîne' (1.) REL; 've yebğûnehâ' (6.) kelimesindeki 've' CONJ; 've hum' (8.) kelimesindeki 've' REM (okuma). "
 + T[45] + " (okuma). "
 + cumle(say('say 7:45 1-5', "llezîne yasuddûne 'an sebîli'llâhi", True), say('say 7:45 2-5', "yasuddûne 'an sebîli'llâhi"), say('dizi 7 45 2 5', "sadde 'an sebîl allâh"), say('dizi 7 45 2 7', "sadde 'an sebîl allâh beğâ 'iveç"), say('say 7:45 1-7', "llezîne yasuddûne 'an sebîli'llâhi ve yebğûnehâ 'ivecen"), say('dizi 7 45 1 7', "ellezî sadde 'an sebîl allâh beğâ 'iveç")) + ' '
 + cumle(say('say 7:45 6-7', "ve yebğûnehâ 'ivecen", True), say('say 7:45 4-7', "sebîli'llâhi ve yebğûnehâ 'ivecen"), say('dizi 7 45 4 7', "sebîl allâh beğâ 'iveç"), say('say 7:45 8-10', "ve hum bi'l-âxirati kâfirûn")) + ' ' +
 "Ölçüm xref 11:19 (emsal olarak basıldı), 14:3 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıbı: 'sadde 'an sebîl allâh' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'ellezî' + IMPF + ''an' + izafet + lafız + 've' + IMPF + nekre + 've' + 'hum' + 'bi' + belirli + 'kâfir'; "
 "D2 haber; kip yok; D3 11:19 eşi, 14:3 eşi; D4 3FS 1 · 3MP 5, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[45] + "; aktör yok (ölçüm); A2 zalimlerin Allah'ın yolundan alıkoyuşu, onu eğri göstermek isteyişi ve âhireti inkârı; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi soru → haber (ayetler arası).",
)

D[46] = ("◇ 've beynehumâ hicâbun ve 'ale'l-a'râfi ricâlun ya'rifûne kullen bi-sîmâhum ve nâdev ashâbe'l-cenneti en selâmun 'aleykum lem yedxulûhâ ve hum yatma'ûn' — "
 "'ve' + 'beyn' + 3D + nekre 'hicâb' + 've' + ''alâ' + belirli çoğul 'a'râf' + nekre çoğul 'ricâl' + IMPF 3MP I. bab + nekre 'kull' + 'bi' + 'sîmâ' + 3MP + 've' + PERF 3MP III. bab + 'ashâb' + belirli 'cenne' + 'en' + nekre 'selâm' + ''alâ' + 2MP + 'lem' + IMPF 3MP I. bab + 3FS + 've' + 'hum' + IMPF 3MP I. bab "
 "(ölçüm edim haber, kip NEG 1; 2MP 1 · 3D 1 · 3FS 1 · 3MP 10; bab I. bab ×3 · III. bab ×1). "
 "Allah lafzı yok; Rab yok; ölçüm '{{3|esmâ سَلام 13. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton belirsiz' (uyuşmuyor) — esma_el kaydı 'degil' — 'selâmun 'aleykum', kural 'esmâ adı esmâ dışı göndergeyle → degil' (selamlama sözü) (okuma); ölçüm '{{3|" + _AK3 + "}}' — satır aynen. "
 "Ölçüm 'yıldız yok' — satır aynen; n=18 (n z=0,59); ölçüm '{{3|fâsıla " + _F[2] + " → ن, N sınıfı}}' — satır aynen (7:45 ن → 7:46 ن); "
 "ölçüm '{{3|simetri \\[3, 12, 15, 1\\]}}' — satır aynen; ölçüm '{{3|harf 92 → harf3 85, isaret 7}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm NEG 1: 'lem' (15. kelime); "
 "'ve beynehumâ' (1.) kelimesindeki 've' REM; 've beynehumâ' (1.) LOC; 've 'ale' (3.) kelimesindeki 've' CONJ; 've nâdev' (9.) kelimesindeki 've' CONJ; 'en' (12.) INT; 've hum' (17.) kelimesindeki 've' CIRC (okuma). "
 "Kök ikilemesi (ölçüm) عرف ×2 ('l-a'râfi' 4. / 'ya'rifûne' 6. kelime) (okuma). "
 + T[46] + " (okuma). "
 + cumle(say('say 7:46 1-2', "ve beynehumâ hicâbun", True), say('say 7:46 3-8', "ve 'ale'l-a'râfi ricâlun ya'rifûne kullen bi-sîmâhum"), say('say 7:46 4-6', "l-a'râfi ricâlun ya'rifûne"), say('dizi 7 46 4 6', "a'râf ricâl 'arafe")) + ' '
 + cumle(say('say 7:46 9-12', "ve nâdev ashâbe'l-cenneti en", True), say('say 7:46 9-11', "ve nâdev ashâbe'l-cenneti"), say('dizi 7 46 9 11', "nâdâ ashâb cenne"), say('say 7:46 10-11', "ashâbe'l-cenneti"), say('say 7:46 10-12', "ashâbe'l-cenneti en"), say('dizi 7 46 10 12', "ashâb cenne en")) + ' '
 + cumle(say('say 7:46 13-14', "selâmun 'aleykum", True), say('say 7:46 15-16', "lem yedxulûhâ"), say('say 7:46 17-18', "ve hum yatma'ûn")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: 'nâdâ ashâb cenne' süzgeç GEÇMEZ; 'a'râf ricâl 'arafe' süzgeç GEÇMEZ; 'ashâb cenne en' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + izafet + nekre + 've' + ''alâ' + belirli + nekre + IMPF + nekre + 'bi' + izafet + 've' + PERF + izafet + belirli + 'en' + nekre + ''alâ' + 'lem' + IMPF + 've' + 'hum' + IMPF; "
 "D2 haber; NEG ('lem' 15. kelime); D3 عرف ×2; D4 2MP 1 · 3D 1 · 3FS 1 · 3MP 10, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[46] + "; aktör adlı 'l-cenneti' (11. kelime; ölçüm rol mecrur); A2 topluluklar arasındaki perde; A'râf üzerinde herkesi simalarından tanıyan adamlar; bahçe halkına selâm verişleri; girmemiş ama umar oluşları; "
 "A3 'selâmun 'aleykum' (söz biçimli içerik, 13-14. kelime); "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi yok (ayetler arası).",
)

D[47] = ("◇ 've izâ surifet ebsâruhum tilqâ'e ashâbi'n-nâri qâlû rabbenâ lâ tec'alnâ ma'a'l-qavmi'z-zâlimîn' — "
 "'ve' + 'izâ' + PERF 3FS I. bab edilgen + çoğul 'basar' + 3MP + 'tilqâ'' + 'ashâb' + belirli 'nâr' + PERF 3MP I. bab + 'rabb' + 1P + 'lâ' + IMPF 2MS I. bab + 1P + 'ma'a' + belirli 'qavm' + belirli çoğul etken ortaç 'zâlim' "
 "(ölçüm edim yasak, kip PRO 1; 1P 2 · 2MS 1 · 3FS 1 · 3MP 3; bab I. bab ×3). "
 "Allah lafzı yok; Rab 8. sırada (ölçüm rab z=1,32); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{4|yıldız ★}}' — satır aynen (kaynak pas, z=1,57); n=13 (n z=0,06); ölçüm '{{4|EDİLGEN 1/3 fiil, pas z=1,57}}' — satır aynen; ölçüm '{{4|fâsıla " + _F[3] + " → ن, N sınıfı}}' — satır aynen (7:46 ن → 7:47 ن); "
 "ölçüm '{{4|harf 61 → harf3 59, isaret 2}}' — satır aynen; ölçüm '{{4|dış düğüm 1}}' — satır aynen; ölçüm '{{4|İÇ düğüm 1}}' — satır aynen. "
 "Ölçüm PRO 1: 'lâ' (9. kelime); ölçüm biçim NEHY; "
 "'ve izâ' (1.) kelimesindeki 've' REM; 've izâ' (1.) T; 'tilqâ'e' (4.) LOC; 'ma'a'l-qavmi' (11.) LOC (okuma). "
 + T[47] + " (okuma). "
 + cumle(say('say 7:47 1-6', "ve izâ surifet ebsâruhum tilqâ'e ashâbi'n-nâri", True), say('say 7:47 9-13', "lâ tec'alnâ ma'a'l-qavmi'z-zâlimîn"), say('dizi 7 47 9 13', "lâ ce'ale ma'a qavm zâlim"), say('say 7:47 11-13', "ma'a'l-qavmi'z-zâlimîn"), say('say 7:47 12-13', "l-qavmi'z-zâlimîn"), say('dizi 7 47 12 13', "qavm zâlim"), say('say 7:47 5-6', "ashâbi'n-nâri"), say('dizi 7 47 5 6', "ashâb nâr")) + ' ' +
 "Ölçüm xref 23:94 (emsal olarak basıldı), okunmamış 1 ayet (sûre içi 1). "
 "Ölçüm nakarat3 kalıbı: 'lâ ce'ale ma'a qavm zâlim' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B3 'ebsâruhum' (3. kelime).",
 "◈D — D1 've' + 'izâ' + PERF + izafet + izafet + izafet + belirli + PERF + izafet + 'lâ' + IMPF + 'ma'a' + belirli + belirli; "
 "D2 yasak; PRO ('lâ' 9. kelime); D3 23:94 eşi; D4 1P 2 · 2MS 1 · 3FS 1 · 3MP 3, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[47] + "; aktör yok (ölçüm); A2 gözleri ateş halkına çevrilince zalim kavimle beraber kılınmamak için Rablerine yakarış; "
 "A3 'rabbenâ lâ tec'alnâ ma'a'l-qavmi'z-zâlimîn' (söz içi, 8-13. kelime); "
 "A4 " + BOLUM + "; söz açılır (8. kelime); söz kapanır (13. kelime, ayet içi); şahıs geçişi yok (ayetler arası); edim geçişi haber → yasak (ayetler arası).",
)
out = ['# ── blok 7:44-47 (2026-11-25) ──', 'MEAL13 = {']
for n in range(44, 48):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M13 = {']
for n in range(44, 48):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL13); M.update(M13)']
open('/home/claude/yamalar/metin_7_44_47.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

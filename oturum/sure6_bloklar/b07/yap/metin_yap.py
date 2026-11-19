# sûre 6 blok 7 (6:29-32) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b07/say2.txt'
os.environ['OLC'] = '/home/claude/b07/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Yalanlayanların toplanma sahnesi; dünya hayatı oyun' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'



MEAL = {
 29: "Dediler: O, ancak dünya hayatımızdır; biz diriltilecekler değiliz.",
 30: "Rablerinin huzurunda durdurulduklarında bir görsen! Dedi: Bu gerçek değil mi? Dediler: Evet, Rabbimize andolsun. Dedi: Öyleyse inkâr ettiğinize karşılık azabı tadın.",
 31: "Allah'a kavuşmayı yalanlayanlar gerçekten ziyana uğramıştır. Hatta o saat ansızın kendilerine geldiğinde derler: Yazıklar olsun bize, onda ihmal ettiğimiz şeyden dolayı! Onlar yüklerini sırtlarında taşırlar. Dikkat edin, yüklendikleri ne kötüdür!",
 32: "Dünya hayatı ancak bir oyun ve oyalanmadır. Elbette âhiret yurdu sakınanlar için daha hayırlıdır. Hâlâ akıl erdirmez misiniz?",
}

T = {}
T[29] = ("'ve qâlû' 3MP (adsız; gönderge 6:28 15. kelime, 1. kelime); 'hiye' 3FS (adsız; söz içi; gönderge 'hayâtunâ', 3. kelime); konuşan 1P (adsız; söz içi; 'hayâtunâ', 'nahnu' — 5. ve 8. kelime)")
T[30] = ("muhatap 2MS (adsız; 'terâ' — 2. kelime); 'vuqifû', 'rabbihim' 3MP (adsız; edilgen; naib-i faili zamir — gönderge 6:29 1. kelime, 4. kelime; 'rabbihim' 6. kelime); "
         "'qâle' 3MS (adsız; gönderge 'rabbihim', 7. kelime); 'eleyse' 3MS (adsız; söz içi; gönderge 'hâzâ', 8. kelime); 'qâlû' 3MP (adsız; gönderge 6:29 1. kelime, 11. kelime); "
         "konuşan 1P (adsız; söz içi; 'rabbinâ' — 13. kelime); 'qâle' 3MS (adsız; gönderge 'rabbihim', 14. kelime); muhatap 2MP (adsız; söz içi; 'fe-zûqu', 'kuntum', 'tekfurûn' — 15., 18. ve 19. kelime)")
T[31] = ("'xasira' 3MS (fiil uyumu; 2. kelime — fail 3. kelime); 'kezzebû' 3MP (adsız; gönderge 'llezîne', 4. kelime); 'câ'ethumu' 3FS (fiil uyumu; 9. kelime — fail 10. kelime); "
         "'câ'ethumu', 'qâlû' 3MP (adsız; gönderge 'llezîne' — 9. ve 12. kelime); konuşan 1P (adsız; söz içi; 'hasratenâ', 'farratnâ' — 13. ve 16. kelime); 'fîhâ' 3FS (adsız; söz içi; gönderge 's-sâ'atu', 17. kelime); "
         "'ve hum', 'yahmilûne', 'evzârahum', 'zuhûrihim' 3MP (adsız; gönderge 'llezîne' — 18., 19., 20. ve 22. kelime); 'sâ'e' 3MS (adsız; gönderge 'mâ', 24. kelime); 'yezirûn' 3MP (adsız; gönderge 'llezîne', 26. kelime)")
T[32] = ("'yetteqûn' 3MP (adsız; gönderge 'llezîne', 11. kelime); muhatap 2MP (adsız; 'ta'qilûn' — 13. kelime)")

D = {}
D[29] = ("◇ 've qâlû in hiye illâ hayâtunâ'd-dunyâ ve mâ nahnu bi-meb'ûsîn' — "
 "'ve' + PERF 3MP I. bab + 'in' + 'hiye' + 'illâ' + 'hayât' + 1P + belirli sıfat 'dunyâ' + 've' + 'mâ' + 'nahnu' + 'bi' + çoğul edilgen ortaç 'meb'ûs' "
 "(ölçüm edim haber, kip NEG 2 · RES 1; 1P 2 · 3FS 1 · 3MP 2; bab I. bab ×1). "
 "Lafız yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=9 (n z=-0,36); ölçüm '{{1|fâsıla بمبعوثين → ن, N sınıfı}}' — satır aynen (6:28 ن → 6:29 ن); "
 "ölçüm '{{1|simetri \\[3, 2, 7, 1\\]}}' — satır aynen; ölçüm '{{1|harf 40 → harf3 39, isaret 1}}' — satır aynen; ölçüm '{{1|dış düğüm 1}}' — satır aynen. "
 "Ölçüm NEG 2: 'in' (2. kelime), 'mâ' (7. kelime); RES 1: 'illâ' (4. kelime); 've qâlû' (1.) kelimesindeki 've' REM; 've mâ' (7.) kelimesindeki 've' CONJ (okuma). "
 + T[29] + " (okuma). "
 + cumle(say('say 6:29 1-6', "ve qâlû in hiye illâ hayâtunâ'd-dunyâ", True), say('say 6:29 2-6', "in hiye illâ hayâtunâ'd-dunyâ"), say('say 6:29 5-6', "hayâtunâ'd-dunyâ")) + ' '
 + cumle(say('say 6:29 7-9', "ve mâ nahnu bi-meb'ûsîn", True), say('say 6:29 8-9', "nahnu bi-meb'ûsîn")) + ' '
 "Ölçüm xref okunmuş 1 ayet. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 —; B4 'hayâtunâ' (5. kelime).",
 "◈D — D1 've' + PERF + 'in' + 'hiye' + 'illâ' + izafet + belirli + 've' + 'mâ' + 'nahnu' + 'bi' + çoğul; "
 "D2 haber; NEG ('in' 2. kelime, 'mâ' 7. kelime), RES ('illâ' 4. kelime); D3 —; D4 1P 2 · 3FS 1 · 3MP 2, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[29] + "; aktör yok (ölçüm); A2 hayatın dünya hayatından ibaret sayılması; diriltilmenin inkârı; "
 "A3 'in hiye illâ hayâtunâ'd-dunyâ ve mâ nahnu bi-meb'ûsîn' (söz içi, 2-9. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (9. kelime, ayet içi); edim geçişi şart → haber (ayetler arası).",
)

D[30] = ("◇ 've lev terâ iz vuqifû 'alâ rabbihim, qâle eleyse hâzâ bi'l-haqq, qâlû belâ ve rabbinâ, qâle fe-zûqu'l-'azâbe bimâ kuntum tekfurûn' — "
 "'ve' + 'lev' + IMPF 2MS I. bab + 'iz' + edilgen PERF 3MP I. bab + ''alâ' + 'rabb' + 3MP + PERF 3MS I. bab + 'e' + PERF 3MS I. bab + 'hâ' + 'zâ' + 'bi' + belirli 'haqq' + PERF 3MP I. bab + 'belâ' + 've' + 'rabb' + 1P + "
 "PERF 3MS I. bab + 'fe' + IMPV 2MP I. bab + belirli ''azâb' + 'bi' + 'mâ' + PERF 2MP I. bab + IMPF 2MP I. bab "
 "(ölçüm edim soru, emir, şart, kip COND 1 · IMPV 1 · INTG 1; 1P 1 · 2MP 6 · 2MS 1 · 3MP 5 · 3MS 3; bab I. bab ×9). "
 "Lafız yok; Rab 6. ve 13. sırada (ölçüm rab z=1,92); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=19 (n z=0,70); ölçüm '{{2|EDİLGEN 1/9 fiil, pas z=0,30}}' — satır aynen; "
 "ölçüm '{{2|fâsıla تكفرون → ن, N sınıfı}}' — satır aynen (6:29 ن → 6:30 ن); ölçüm '{{2|simetri \\[4, 5, 12, 1\\]}}' — satır aynen; ölçüm '{{2|harf 82 → harf3 76, isaret 6}}' — satır aynen; ölçüm '{{2|dış düğüm 3}}' — satır aynen. "
 "Ölçüm COND 1: 've lev' (1. kelime); INTG 1: 'eleyse' (8. kelime); IMPV 1: 'fe-zûqu' (15. kelime); 've lev' (1.) kelimesindeki 've' CONJ; 've rabbinâ' (13.) kelimesindeki 've' yemin edatı (morph P); 'fe-zûqu' (15.) kelimesindeki 'fe' SUP (okuma). "
 "Kök ikilemesi (ölçüm) ربب ×2 ('rabbihim' 6. / 'rabbinâ' 13. kelime), قول ×3 ('qâle' 7. / 'qâlû' 11. / 'qâle' 14. kelime) (okuma). "
 + T[30] + " (okuma). "
 + cumle(say('say 6:30 1-5', "ve lev terâ iz vuqifû 'alâ", True), say('say 6:30 8-10', "eleyse hâzâ bi'l-haqq"), say('say 6:30 11-13', "qâlû belâ ve rabbinâ"), say('say 6:30 12-13', "belâ ve rabbinâ")) + ' '
 + cumle(say('say 6:30 16-18', "l-'azâbe bimâ kuntum", True), say('dizi 6 30 16 18', "'azâb mâ kâne"), say('say 6:30 17-19', "bimâ kuntum tekfurûn"), say('dizi 6 30 17 19', "mâ kâne kefera"), say('say 6:30 18-19', "kuntum tekfurûn")) + ' '
 "Ölçüm xref 46:34 (emsal olarak basıldı), 5:116 (basılmış) ve okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıbı: 'lev raâ iz vuqife 'alâ' süzgeç GEÇER; ''azâb mâ kâne' süzgeç GEÇER; 'mâ kâne kefera' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'lev' + IMPF + 'iz' + PERF + ''alâ' + izafet + PERF + 'e' + PERF + 'hâ' + 'zâ' + 'bi' + belirli + PERF + 'belâ' + 've' + izafet + PERF + 'fe' + IMPV + belirli + 'bi' + 'mâ' + PERF + IMPF; "
 "D2 soru, emir, şart; COND ('ve lev' 1. kelime), INTG ('eleyse' 8. kelime), IMPV ('fe-zûqu' 15. kelime); D3 ربب ×2, قول ×3; 46:34 eşi; D4 1P 1 · 2MP 6 · 2MS 1 · 3MP 5 · 3MS 3, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[30] + "; aktör yok (ölçüm); A2 Rablerinin huzurunda durdurulma; gerçeğin sorulması ve yeminle kabul; inkâra karşılık azabı tatma; "
 "A3 'eleyse hâzâ bi'l-haqq' (söz içi, 8-10. kelime); 'belâ ve rabbinâ' (söz içi, 12-13. kelime); 'fe-zûqu'l-'azâbe bimâ kuntum tekfurûn' (söz içi, 15-19. kelime); "
 "A4 " + BOLUM + "; şart → cevap (ayet içi; COND 'lev' 1. kelime: 'lev terâ iz vuqifû' — cevap hazif (mealde ünlem)); söz açılır (8. kelime); söz kapanır (10. kelime, ayet içi); söz açılır (12. kelime); söz kapanır (13. kelime, ayet içi); "
 "söz açılır (15. kelime); söz kapanır (19. kelime, ayet içi); şahıs geçişi 3 → 2 (ayetler arası); edim geçişi haber → soru (ayetler arası).",
)

D[31] = ("◇ 'qad xasira'llezîne kezzebû bi-liqâ'i'llâh, hattâ izâ câ'ethumu's-sâ'atu bağteten qâlû yâ hasratenâ 'alâ mâ farratnâ fîhâ ve hum yahmilûne evzârahum 'alâ zuhûrihim, elâ sâ'e mâ yezirûn' — "
 "'qad' + PERF 3MS I. bab + 'ellezî' + PERF 3MP II. bab + 'bi' + mastar 'liqâ'' + lafız + 'hattâ' + 'izâ' + PERF 3FS I. bab + 3MP + belirli 'sâ'a' + nekre 'bağte' + PERF 3MP I. bab + 'yâ' + 'hasret' + 1P + ''alâ' + 'mâ' + PERF 1P II. bab + 'fî' + 3FS + "
 "'ve' + 'hum' + IMPF 3MP I. bab + çoğul 'vizr' + 3MP + ''alâ' + çoğul 'zahr' + 3MP + 'alâ' + PERF 3MS I. bab + 'mâ' + IMPF 3MP I. bab "
 "(ölçüm edim nida, kip CERT 1 · VOC 1; 1P 3 · 3FS 2 · 3MP 12 · 3MS 2; bab I. bab ×6 · II. bab ×2). "
 "Allah lafzı 6. sırada (ölçüm allah z=0,24); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=26 (n z=1,44); ölçüm '{{3|fâsıla يزرون → ن, N sınıfı}}' — satır aynen (6:30 ن → 6:31 ن); "
 "ölçüm '{{3|simetri \\[3, 1, 15, 1\\]}}' — satır aynen; ölçüm '{{3|harf 115 → harf3 110, isaret 5}}' — satır aynen; ölçüm '{{3|dış düğüm 1}}' — satır aynen. "
 "Ölçüm CERT 1: 'qad' (1. kelime); VOC 1: 'yâ' (13. kelime); 've hum' (18.) kelimesindeki 've' CIRC; 'elâ' (23.) ATT (okuma). "
 "Kök ikilemesi (ölçüm) وزر ×2 ('evzârahum' 20. / 'yezirûn' 26. kelime) (okuma). "
 + T[31] + " (okuma). "
 + cumle(say('say 6:31 1-6', "qad xasira'llezîne kezzebû bi-liqâ'i'llâh", True), say('say 6:31 1-3', "qad xasira'llezîne"), say('say 6:31 4-6', "kezzebû bi-liqâ'i'llâh")) + ' '
 + cumle(say('say 6:31 7-9', "hattâ izâ câ'ethum", True), say('dizi 6 31 7 9', "hattâ izâ câ'e"), say('say 6:31 23-26', "elâ sâ'e mâ yezirûn")) + ' '
 "Ölçüm xref 10:45 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıbı: 'hattâ izâ câ'e' süzgeç GEÇER; 'qad xasira ellezî' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K2 's-sâ'atu' (10. kelime).",
 "◈B — B1 —; B2 'yahmilûne' (19. kelime); B3 —; B4 —.",
 "◈D — D1 'qad' + PERF + 'ellezî' + PERF + 'bi' + izafet + lafız + 'hattâ' + 'izâ' + PERF + belirli + nekre + PERF + 'yâ' + izafet + ''alâ' + 'mâ' + PERF + 'fî' + 've' + 'hum' + IMPF + izafet + ''alâ' + izafet + 'alâ' + PERF + 'mâ' + IMPF; "
 "D2 nida; CERT ('qad' 1. kelime), VOC ('yâ' 13. kelime); D3 وزر ×2; 10:45 eşi; D4 1P 3 · 3FS 2 · 3MP 12 · 3MS 2, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[31] + "; aktör yok (ölçüm); A2 Allah'a kavuşmayı yalanlayanların ziyanı; saatin ansızın gelişi; hasret; günah yüklerini sırtta taşıma; "
 "A3 'yâ hasratenâ 'alâ mâ farratnâ fîhâ' (söz içi, 13-17. kelime); "
 "A4 " + BOLUM + "; söz açılır (13. kelime); söz kapanır (17. kelime, ayet içi); şahıs geçişi 2 → 3 (ayetler arası); edim geçişi soru → nida (ayetler arası).",
)

D[32] = ("◇ 've me'l-hayâtu'd-dunyâ illâ la'ibun ve lahv, ve le'd-dâru'l-âxiratu xayrun li'llezîne yetteqûn, e-fe-lâ ta'qilûn' — "
 "'ve' + 'mâ' + belirli 'hayât' + belirli sıfat 'dunyâ' + 'illâ' + nekre 'la'ib' + 've' + nekre 'lahv' + 've' + 'le' + belirli 'dâr' + belirli sıfat 'âxir' + nekre 'xayr' + 'li' + 'ellezî' + IMPF 3MP VIII. bab + 'e' + 'fe' + 'lâ' + IMPF 2MP I. bab "
 "(ölçüm edim soru, kip EMPH 1 · INTG 1 · NEG 2 · RES 1; 2MP 2 · 3MP 2; bab I. bab ×1 · VIII. bab ×1). "
 "Lafız yok; Rab yok; ölçüm '{{4|esmâ آخِر 8\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET ton denge' — ölçüm MÜHÜRSÜZ ile uyuşmuyor (araç tanımı farkı; muhur_el hayır — ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 'l-âxiratu', kural 'esmâ adı esmâ dışı göndergeyle → degil' (yurdun sıfatı) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=13 (n z=0,06); ölçüm '{{4|fâsıla تعقلون → ن, N sınıfı}}' — satır aynen (6:31 ن → 6:32 ن); "
 "ölçüm '{{4|harf 66 → harf3 61, isaret 5}}' — satır aynen; ölçüm '{{4|dış düğüm 4}}' — satır aynen. "
 "Ölçüm NEG 2: 'mâ' (1. kelime), 'lâ' (12. kelime); RES 1: 'illâ' (4. kelime); EMPH 1: 'le' (7. kelime); INTG 1: 'e-fe-lâ' (12. kelime); 've me'l-hayâtu' (1.) kelimesindeki 've' REM; 've lahv' (6.) ve 've le'd-dâru' (7.) kelimelerindeki 've' CONJ (okuma). "
 + T[32] + " (okuma). "
 + cumle(say('say 6:32 1-6', "ve me'l-hayâtu'd-dunyâ illâ la'ibun ve lahv", True), say('say 6:32 2-3', "l-hayâtu'd-dunyâ"), say('say 6:32 5-6', "la'ibun ve lahv")) + " (--medde 60 ayet: 'l-hayâtu'd-dunyâ' yazım farkı ile; harekesiz sayım ة / و yazımına bağlı). "
 + cumle(say('say 6:32 7-11', "ve le'd-dâru'l-âxiratu xayrun li'llezîne yetteqûn", True), say('say 6:32 10-11', "li'llezîne yetteqûn"), say('say 6:32 12-13', "e-fe-lâ ta'qilûn")) + ' '
 "Ölçüm xref 47:36 (emsal olarak basıldı) ve okunmuş 2 ayet ve okunmamış 1 ayet. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'l-hayâtu'd-dunyâ' / 'd-dâru'l-âxiratu' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 —; B4 'l-hayâtu' (2. kelime).",
 "◈D — D1 've' + 'mâ' + belirli + belirli + 'illâ' + nekre + 've' + nekre + 've' + 'le' + belirli + belirli + nekre + 'li' + 'ellezî' + IMPF + 'e' + 'fe' + 'lâ' + IMPF; "
 "D2 soru; NEG ('mâ' 1. kelime, 'lâ' 12. kelime), RES ('illâ' 4. kelime), EMPH ('le' 7. kelime), INTG ('e-fe-lâ' 12. kelime); D3 —; 47:36 eşi; D4 2MP 2 · 3MP 2, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[32] + "; aktör yok (ölçüm); A2 dünya hayatının oyun ve oyalanma oluşu; âhiret yurdunun sakınanlar için hayırlı oluşu; akıl erdirmeye çağrı; "
 "A3 —; "
 "A4 " + BOLUM + "; edim geçişi nida → soru (ayetler arası); şahıs sayısında beraberlik (2MP 2 · 3MP 2 — ölçüm baskın 3); bölüm kapanışı.",
)
out = ['# ── blok 6:29-32 (2026-11-19) ──', 'MEAL7 = {']
for n in range(29, 33):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M7 = {']
for n in range(29, 33):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL7); M.update(M7)']
open('/home/claude/yamalar/metin_6_29_32.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

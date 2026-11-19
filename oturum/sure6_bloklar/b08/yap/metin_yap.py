# sûre 6 blok 8 (6:33-36) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b08/say2.txt'
os.environ['OLC'] = '/home/claude/b08/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Elçiye teselli; darlıkta çağrılan' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'



MEAL = {
 33: "Gerçekten biliyoruz ki söyledikleri elbette seni üzüyor. Onlar seni yalanlamıyorlar; ama zalimler Allah'ın âyetlerini bile bile inkâr ediyorlar.",
 34: "Andolsun, senden önce de elçiler yalanlandı; yalanlandıklarına ve eziyet edildiklerine karşı, yardımımız kendilerine gelinceye kadar sabrettiler. Allah'ın sözlerini değiştirecek yoktur. Andolsun, elçilerin haberinden sana gelmiştir.",
 35: "Onların yüz çevirmesi sana ağır geldiyse, yerde bir tünel ya da gökte bir merdiven arayıp onlara bir âyet getirmeye gücün yeterse getir. Allah dileseydi onları elbette doğru yol üzerinde toplardı. Öyleyse sakın cahillerden olma.",
 36: "Ancak işitenler icabet eder. Ölüleri ise Allah diriltecek, sonra O'na döndürülürler.",
}

T = {}
T[33] = ("konuşan 1P (adsız; 'na'lemu' — 2. kelime); 'innehû' 3MS (adsız; şan zamiri, 3. kelime); 'le-yahzunuke' 3MS (fiil uyumu; 4. kelime — fail 5. kelime); muhatap 2MS (adsız; 'le-yahzunuke', 'yukezzibûneke' — 4. ve 9. kelime); "
         "'yeqûlûne', 'fe-innehum', 'yukezzibûneke', 'yechadûn' 3MP (adsız; gönderge 'z-zâlimîne' 11. kelime — 6., 7., 9. ve 14. kelime)")
T[34] = ("'kuzzibet' 3FS (fiil uyumu; edilgen; naib-i faili 'rusulun' (3. kelimedeki ad), 2. kelime); muhatap 2MS (adsız; 'qablike', 'câ'eke' — 5. ve 19. kelime); "
         "'fe-saberû' 3MP (adsız; gönderge 'rusulun', 6. kelime); 'kuzzibû', 've ûzû' 3MP (adsız; edilgen; naib-i faili zamir — gönderge 'rusulun' 3. kelime, 9. ve 10. kelime); "
         "'etâhum' 3MS (fiil uyumu; 12. kelime — fail 13. kelime); 'etâhum' zamiri 3MP (adsız; gönderge 'rusulun' 3. kelime, 12. kelime); konuşan 1P (adsız; 'nasrunâ' — 13. kelime); "
         "'câ'eke' 3MS (fiil uyumu; 19. kelime — fail 21. kelime ('min' ile))")
T[35] = ("'kâne' 3MS (adsız; şan zamiri, 2. kelime); 'kebure' 3MS (fiil uyumu; 3. kelime — fail 5. kelime); muhatap 2MS (adsız; ''aleyke', 'steta'te', 'tebteğiye', 'te'tiyehum', 'tekûnenne' — 4., 7., 9., 17. ve 26. kelime); "
         "'i'râduhum', 'te'tiyehum' 3MP (adsız; gönderge 6:33 11. kelime — 5. ve 17. kelime); 'şâ'e' 3MS (fiil uyumu; 20. kelime — fail 21. kelime); 'le-ceme'ahum' 3MS (adsız; gönderge lafız 21. kelime, 22. kelime); "
         "'le-ceme'ahum' zamiri 3MP (adsız; gönderge 6:33 11. kelime, 22. kelime)")
T[36] = ("'yestecîbu' 3MS (fiil uyumu; 2. kelime — fail 3. kelime); 'yesme'ûn' 3MP (adsız; gönderge 'llezîne', 4. kelime); 'yeb'asuhumu' 3MS (fiil uyumu; 6. kelime — fail 7. kelime); "
         "'yeb'asuhumu' zamiri 3MP (adsız; gönderge 'l-mevtâ' 5. kelime, 6. kelime); 'ileyhi' 3MS (adsız; gönderge lafız 7. kelime, 9. kelime); 'yurce'ûn' 3MP (adsız; edilgen; naib-i faili zamir — gönderge 'l-mevtâ' 5. kelime, 10. kelime)")

D = {}
D[33] = ("◇ 'qad na'lemu innehû le-yahzunuke'llezî yeqûlûne fe-innehum lâ yukezzibûneke ve lâkinne'z-zâlimîne bi-âyâti'llâhi yechadûn' — "
 "'qad' + IMPF 1P I. bab + 'inne' + 3MS + 'le' + IMPF 3MS I. bab + 2MS + 'ellezî' + IMPF 3MP I. bab + 'fe' + 'inne' + 3MP + 'lâ' + IMPF 3MP II. bab + 2MS + 've' + 'lâkinne' + belirli çoğul etken ortaç 'zâlim' + 'bi' + çoğul 'âye' + lafız + IMPF 3MP I. bab "
 "(ölçüm edim haber, kip CERT 1 · EMPH 1 · NEG 1; 1P 1 · 2MS 2 · 3MP 7 · 3MS 2; bab I. bab ×4 · II. bab ×1). "
 "Allah lafzı 13. sırada (ölçüm allah z=0,90); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=14 (n z=0,17); ölçüm '{{1|fâsıla يجحدون → ن, N sınıfı}}' — satır aynen (6:32 ن → 6:33 ن); "
 "ölçüm '{{1|simetri \\[3, 1, 5, 1\\]}}' — satır aynen; ölçüm '{{1|harf 67 → harf3 65, isaret 2}}' — satır aynen; ölçüm '{{1|dış düğüm 1}}' — satır aynen. "
 "Ölçüm CERT 1: 'qad' (1. kelime); EMPH 1: 'le-yahzunuke' (4. kelime); NEG 1: 'lâ' (8. kelime); 'innehû' (3.), 'fe-innehum' (7.) ve 'lâkinne' (10.) ACC; 'fe-innehum' (7.) kelimesindeki 'fe' CONJ; 've lâkinne' (10.) kelimesindeki 've' REM (okuma). "
 + T[33] + " (okuma). "
 + cumle(say('say 6:33 1-4', "qad na'lemu innehû le-yahzunuk", True), say('say 6:33 7-9', "fe-innehum lâ yukezzibûnek")) + ' '
 + cumle(say('say 6:33 10-14', "ve lâkinne'z-zâlimîne bi-âyâti'llâhi yechadûn", True), say('say 6:33 12-14', "bi-âyâti'llâhi yechadûn"), say('say 6:33 12-13', "bi-âyâti'llâh")) + ' '
 "Ölçüm xref 40:63 (emsal olarak basıldı). "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'lâ yukezzibûneke' / 'yechadûn' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'qad' + IMPF + 'inne' + 'le' + IMPF + 'ellezî' + IMPF + 'fe' + 'inne' + 'lâ' + IMPF + 've' + 'lâkinne' + belirli + 'bi' + izafet + lafız + IMPF; "
 "D2 haber; CERT ('qad' 1. kelime), EMPH ('le-yahzunuke' 4. kelime), NEG ('lâ' 8. kelime); D3 —; 40:63 eşi; D4 1P 1 · 2MS 2 · 3MP 7 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[33] + "; aktör yok (ölçüm); A2 söylenenlerin elçiyi üzmesi; yalanlananın elçi değil âyetler oluşu; "
 "A3 —; "
 "A4 " + BOLUM + "; edim geçişi soru → haber (ayetler arası); bölüm açılışı.",
)

D[34] = ("◇ 've le-qad kuzzibet rusulun min qablike fe-saberû 'alâ mâ kuzzibû ve ûzû hattâ etâhum nasrunâ, ve lâ mubeddile li-kelimâti'llâh, ve le-qad câ'eke min nebe'i'l-murselîn' — "
 "'ve' + 'le' + 'qad' + edilgen PERF 3FS II. bab + nekre çoğul 'resûl' + 'min' + 'qabl' + 2MS + 'fe' + PERF 3MP I. bab + ''alâ' + 'mâ' + edilgen PERF 3MP II. bab + 've' + edilgen PERF 3MP IV. bab + 'hattâ' + PERF 3MS I. bab + 3MP + 'nasr' + 1P + "
 "'ve' + 'lâ' + etken ortaç 'mubeddil' + 'li' + çoğul 'kelime' + lafız + 've' + 'le' + 'qad' + PERF 3MS I. bab + 2MS + 'min' + 'nebe'' + belirli çoğul edilgen ortaç 'mursel' "
 "(ölçüm edim haber, kip CERT 2 · EMPH 2 · NEG 1; 1P 1 · 2MS 2 · 3FS 1 · 3MP 7 · 3MS 2; bab I. bab ×3 · II. bab ×2 · IV. bab ×1). "
 "Allah lafzı 17. sırada (ölçüm allah z=0,38); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=22 (n z=1,02); ölçüm '{{2|EDİLGEN 3/6 fiil, pas z=2,52}}' — satır aynen; "
 "ölçüm '{{2|fâsıla ٱلمرسلين → ن, N sınıfı}}' — satır aynen (6:33 ن → 6:34 ن); ölçüm '{{2|simetri \\[4, 1, 8, 1\\]}}' — satır aynen; ölçüm '{{2|harf 97 → harf3 90, isaret 7}}' — satır aynen; ölçüm '{{2|dış düğüm 2}}' — satır aynen. "
 "Ölçüm CERT 2 ve EMPH 2: 've le-qad' (1. ve 18. kelime); NEG 1: 'lâ' (14. kelime); 've le-qad' (1., 18.) ve 've lâ' (14.) kelimelerindeki 've' REM; 'fe-saberû' (6.) kelimesindeki 'fe' CONJ; 've ûzû' (10.) kelimesindeki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) رسل ×2 ('rusulun' 3. / 'l-murselîn' 22. kelime), كذب ×2 ('kuzzibet' 2. / 'kuzzibû' 9. kelime) (okuma). "
 + T[34] + " (okuma). "
 + cumle(say('say 6:34 2-5', "kuzzibet rusulun min qablik", True), say('say 6:34 2-3', "kuzzibet rusul"), say('say 6:34 3-5', "rusulun min qablik"), say('dizi 6 34 3 5', "resûl min qabl")) + ' '
 + cumle(say('say 6:34 6-10', "fe-saberû 'alâ mâ kuzzibû ve ûzû", True), say('say 6:34 14-17', "ve lâ mubeddile li-kelimâti'llâh"), say('say 6:34 18-22', "ve le-qad câ'eke min nebe'i'l-murselîn")) + ' '
 "Ölçüm xref 35:4 (emsal olarak basıldı) ve okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıbı: 'resûl min qabl' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'le' + 'qad' + PERF + nekre + 'min' + izafet + 'fe' + PERF + ''alâ' + 'mâ' + PERF + 've' + PERF + 'hattâ' + PERF + izafet + 've' + 'lâ' + etken ortaç + 'li' + izafet + lafız + 've' + 'le' + 'qad' + PERF + 'min' + izafet + belirli; "
 "D2 haber; CERT ('qad' 1. ve 18. kelime), EMPH ('le' 1. ve 18. kelime), NEG ('lâ' 14. kelime); D3 رسل ×2, كذب ×2; 35:4 eşi; D4 1P 1 · 2MS 2 · 3FS 1 · 3MP 7 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[34] + "; aktör yok (ölçüm); A2 önceki elçilerin yalanlanması ve sabrı; yardımın gelişi; Allah'ın sözlerini değiştirecek olmaması; elçilerin haberi; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs ve edim geçişi yok (ayetler arası).",
)

D[35] = ("◇ 've in kâne kebure 'aleyke i'râduhum fe-ini'steta'te en tebteğiye nefeqan fi'l-ardi ev sullemen fi's-semâ'i fe-te'tiyehum bi-âyeh, ve lev şâ'e'llâhu le-ceme'ahum 'ale'l-hudâ, fe-lâ tekûnenne mine'l-câhilîn' — "
 "'ve' + 'in' + PERF 3MS I. bab + PERF 3MS I. bab + ''alâ' + 2MS + mastar 'i'râd' + 3MP + 'fe' + 'in' + PERF 2MS X. bab + 'en' + IMPF 2MS VIII. bab + nekre 'nefeq' + 'fî' + belirli 'ard' + 'ev' + nekre 'sullem' + 'fî' + belirli 'semâ'' + 'fe' + IMPF 2MS I. bab + 3MP + 'bi' + nekre 'âye' + "
 "'ve' + 'lev' + PERF 3MS I. bab + lafız + 'le' + PERF 3MS I. bab + 3MP + ''alâ' + belirli 'hudâ' + 'fe' + 'lâ' + IMPF 2MS I. bab + 'n' + 'min' + belirli çoğul etken ortaç 'câhil' "
 "(ölçüm edim şart, kip COND 3 · EMPH 2 · NEG 1; 2MS 6 · 3MP 3 · 3MS 4; bab I. bab ×6 · VIII. bab ×1 · X. bab ×1). "
 "Allah lafzı 21. sırada (ölçüm allah z=0,19); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=28 (n z=1,65); ölçüm '{{3|fâsıla ٱلجهلين → ن, N sınıfı}}' — satır aynen (6:34 ن → 6:35 ن); "
 "ölçüm '{{3|simetri \\[3, 1, 25, 1\\]}}' — satır aynen; ölçüm '{{3|harf 119 → harf3 114, isaret 5}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm COND 3: 've in' (1. kelime), 'fe-in' (6. kelime), 've lev' (19. kelime); EMPH 2: 'le-ceme'ahum' (22. kelime), 'tekûnenne' (26. kelime); NEG 1: 'lâ' (25. kelime); 've in' (1.) ve 'fe-in' (6.) kelimelerindeki önek REM; 've lev' (19.) kelimesindeki 've' CONJ; 'fe-lâ' (25.) kelimesindeki 'fe' REM (okuma). "
 "Kök ikilemesi (ölçüm) كون ×2 ('kâne' 2. / 'tekûnenne' 26. kelime) (okuma). "
 + T[35] + " (okuma). "
 + cumle(say('say 6:35 1-5', "ve in kâne kebure 'aleyke i'râduhum", True), say('say 6:35 13-16', "ev sullemen fi's-semâ'")) + ' '
 + cumle(say('say 6:35 19-21', "ve lev şâ'e'llâh", True), say('dizi 6 35 19 21', "lev şâ'e allâh"), say('say 6:35 25-27', "fe-lâ tekûnenne mine")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: 'lev şâ'e allâh' süzgeç GEÇMEZ; 'fe-lâ kâne min' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'fi'l-ardi' / 'fi's-semâ'i'; 'l-hudâ' / 'l-câhilîn' — ayetler arası: yok.",
 "◈K — K1 'l-ardi' (12. kelime), 's-semâ'i' (16. kelime).",
 "◈B — —",
 "◈D — D1 've' + 'in' + PERF + PERF + ''alâ' + izafet + 'fe' + 'in' + PERF + 'en' + IMPF + nekre + 'fî' + belirli + 'ev' + nekre + 'fî' + belirli + 'fe' + IMPF + 'bi' + nekre + 've' + 'lev' + PERF + lafız + 'le' + PERF + ''alâ' + belirli + 'fe' + 'lâ' + IMPF + 'min' + belirli; "
 "D2 şart; COND ('ve in' 1. kelime, 'fe-in' 6. kelime, 've lev' 19. kelime), EMPH ('le-ceme'ahum' 22. kelime, 'tekûnenne' 26. kelime), NEG ('lâ' 25. kelime); D3 كون ×2; D4 2MS 6 · 3MP 3 · 3MS 4, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[35] + "; aktör yok (ölçüm); A2 yüz çevirmenin elçiye ağır gelmesi; yerde tünel ya da gökte merdivenle âyet getirme; Allah dileseydi doğru yolda toplama; cahillerden olmama; "
 "A3 —; "
 "A4 " + BOLUM + "; şart → cevap (ayet içi; COND 'in' 1. kelime: 'in kâne kebure' / 'fe-ini'steta'te' (6. kelime)); şart → cevap (ayet içi; COND 'in' 6. kelime: 'ini'steta'te en tebteğiye' — cevap hazif (mealde 'getir')); "
 "şart → cevap (ayet içi; COND 'lev' 19. kelime: 'lev şâ'e'llâhu' / 'le-ceme'ahum' (22. kelime)); şahıs geçişi 3 → 2 (ayetler arası); edim geçişi haber → şart (ayetler arası).",
)

D[36] = ("◇ 'innemâ yestecîbu'llezîne yesme'ûn, ve'l-mevtâ yeb'asuhumu'llâhu summe ileyhi yurce'ûn' — "
 "'inne' + 'mâ' + IMPF 3MS X. bab + 'ellezî' + IMPF 3MP I. bab + 've' + belirli çoğul 'meyyit' + IMPF 3MS I. bab + 3MP + lafız + 'summe' + 'ilâ' + 3MS + edilgen IMPF 3MP I. bab "
 "(ölçüm edim haber, kip yok; 3MP 5 · 3MS 3; bab I. bab ×3 · X. bab ×1). "
 "Allah lafzı 7. sırada (ölçüm allah z=1,47); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=10 (n z=-0,26); ölçüm '{{4|EDİLGEN 1/4 fiil, pas z=1,10}}' — satır aynen; "
 "ölçüm '{{4|fâsıla يرجعون → ن, N sınıfı}}' — satır aynen (6:35 ن → 6:36 ن); ölçüm '{{4|harf 52 → harf3 50, isaret 2}}' — satır aynen; ölçüm '{{4|dış düğüm 0}}' — satır aynen. "
 "Ölçüm kip yok; 'innemâ' (1.) ACC + PREV (kasr); 've'l-mevtâ' (5.) kelimesindeki 've' REM (okuma). "
 + T[36] + " (okuma). "
 + cumle(say('say 6:36 1-4', "innemâ yestecîbu'llezîne yesme'ûn", True), say('say 6:36 5-7', "ve'l-mevtâ yeb'asuhumu'llâh"), say('say 6:36 8-10', "summe ileyhi yurce'ûn")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'yesme'ûn' / 'l-mevtâ' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 'yesme'ûn' (4. kelime); B4 'l-mevtâ' (5. kelime).",
 "◈D — D1 'inne' + 'mâ' + IMPF + 'ellezî' + IMPF + 've' + belirli + IMPF + lafız + 'summe' + 'ilâ' + IMPF; "
 "D2 haber; D3 —; D4 3MP 5 · 3MS 3, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[36] + "; aktör yok (ölçüm); A2 ancak işitenlerin icabeti; ölülerin diriltilmesi ve Allah'a döndürülmesi; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 2 → 3 (ayetler arası); edim geçişi şart → haber (ayetler arası).",
)
out = ['# ── blok 6:33-36 (2026-11-19) ──', 'MEAL8 = {']
for n in range(33, 37):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M8 = {']
for n in range(33, 37):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL8); M.update(M8)']
open('/home/claude/yamalar/metin_6_33_36.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

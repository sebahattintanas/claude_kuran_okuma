# sûre 7 blok 23 metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os, re
os.environ['SAY2'] = '/home/claude/b23/say2.txt'
os.environ['OLC'] = '/home/claude/b23/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Sâlih ve Semûd; Lût ve kavmi' bölümünde"
_OL = [l.replace('**', '') for l in open(os.environ['OLC'], encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK1 = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[0]).group(0))
_AK2 = _esc(re.search(r'aktör: adsız `racül` 3\. sırada', _OL[1]).group(0))
_AK3 = _esc(re.search(r'aktör: adsız `karye` 10\. sırada', _OL[2]).group(0))
_AK4 = _esc(re.search(r'aktör: adsız `imrae` 4\. sırada', _OL[3]).group(0))


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 80: "Lût'u da gönderdik; hani kavmine demişti: Âlemlerden hiç kimsenin sizden önce yapmadığı hayâsızlığı mı yapıyorsunuz?",
 81: "Gerçekten siz kadınları bırakıp şehvetle erkeklere yöneliyorsunuz. Hayır siz aşırı giden bir kavimsiniz.",
 82: "Kavminin cevabı ancak şu oldu; dediler ki Onları kasabanızdan çıkarın; çünkü onlar temizlenmeye çalışan insanlardır.",
 83: "Bunun üzerine onu ve ailesini kurtardık; karısı hariç; o geride kalanlardandı.",
 84: "Üzerlerine bir yağmur yağdırdık. Bak suçluların sonu nasıl oldu.",
}

T = {}
T[80] = ("'qâle' 3MS (adsız; gönderge 'lûtan' 1. kelime, 3. kelime); 'qavmihî' 3MS eki (adsız; gönderge 'lûtan' 1. kelime, 4. kelime); muhatap 2MP (adsız; söz içi; 'te'tûne' — 5. kelime); "
         "muhatap 2MP eki (adsız; söz içi; 'sebeqakum' — 8. kelime); 'sebeqakum' 3MS (fiil uyumu; söz içi; 8. kelime — fail 11. kelime); 'bihâ' 3FS eki (adsız; söz içi; gönderge 'l-fâhişete' 6. kelime, 9. kelime)")
T[81] = ("muhatap 2MP eki (adsız; söz içi; 'innekum' — 1. kelime); muhatap 2MP (adsız; söz içi; 'te'tûne' — 2. kelime); muhatap 2MP zamiri (adsız; söz içi; 'entum' — 9. kelime)")
T[82] = ("'kâne' 3MS (fiil uyumu; 2. kelime — fail 6. kelime); 'qavmihî' 3MS eki (adsız; gönderge 7:80 1. kelime, 4. kelime); 'qâlû' 3MP (adsız; gönderge 'qavmihî' 4. kelime, 7. kelime); "
         "muhatap 2MP (adsız; söz içi; 'exricû' — 8. kelime); muhatap 2MP eki (adsız; söz içi; 'qaryetikum' — 10. kelime); 'exricûhum', 'innehum' 3MP eki (adsız; söz içi; gönderge 7:80 1. kelime — 8. ve 11. kelime); "
         "'yetetahharûn' 3MP (adsız; söz içi; gönderge 'unâsun' 12. kelime, 13. kelime)")
T[83] = ("konuşan 1P (adsız; 'enceynâhu' — 1. kelime); 'enceynâhu', 'ehlehû', 'mra'etehû' 3MS eki (adsız; gönderge 7:80 1. kelime — 1., 2. ve 4. kelime); 'kânet' 3FS (adsız; gönderge 'mra'etehû' 4. kelime, 5. kelime)")
T[84] = ("konuşan 1P (adsız; 'emtarnâ' — 1. kelime); ''aleyhim' 3MP eki (adsız; gönderge 7:80 4. kelime, 2. kelime); muhatap 2MS (adsız; 'nzur' — 4. kelime); 'kâne' 3MS (fiil uyumu; 6. kelime — fail 7. kelime)")

D = {}
D[80] = ("◇ 've lûtan iz qâle li-qavmihî e-te'tûne'l-fâhişete mâ sebeqakum bihâ min ehadin mine'l-'âlemîn' — "
 "'ve' + özel ad 'lût' + 'iz' + PERF 3MS I. bab + 'li' + 'qavm' + 3MS + 'e' + IMPF 2MP I. bab + belirli 'fâhişe' + 'mâ' + PERF 3MS I. bab + 2MP + 'bi' + 3FS + 'min' + nekre 'ehad' + 'min' + belirli çoğul ''âlem' "
 "(ölçüm edim soru, kip INTG 1 · NEG 1; 2MP 3 · 3FS 1 · 3MS 3; bab I. bab ×3). "
 "Allah lafzı yok; Rab yok; ölçüm '{{1|esmâ أَحَد 11\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET ton denge' — ölçüm MÜHÜRSÜZ ile uyuşmuyor (araç tanımı farkı; muhur_el hayır — ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 'min ehadin mine'l-'âlemîn', kural 'esmâ adı esmâ dışı göndergeyle → degil' (hiç kimse — olumsuz sayı) (okuma); ölçüm '{{1|" + _AK1 + "}}' — satır aynen. "
 "Ölçüm 'yıldız yok' — satır aynen; n=13 (n z=0,06); ölçüm '{{1|fâsıla " + _F[0] + " → ن, N sınıfı}}' — satır aynen (7:79 ن → 7:80 ن); "
 "ölçüm '{{1|sayı işareti أَحَد}}' — satır aynen; ölçüm '{{1|simetri \\[3, 1, 9, 1\\]}}' — satır aynen; ölçüm '{{1|harf 53 → harf3 51, isaret 2}}' — satır aynen; ölçüm '{{1|dış düğüm 2}}' — satır aynen; "
 "ölçüm '{{1|esit2 → 29:28 oran 0,9615 kademe YAKIN}}' — satır aynen. "
 "Ölçüm INTG 1: 'e-te'tûne' (5. kelime; 'e'); NEG 1: 'mâ' (7. kelime); 've lûtan' (1.) kelimesindeki 've' CONJ; 'iz' (2.) T (okuma). "
 + T[80] + " (okuma). "
 + cumle(say('say 7:80 2-4', "iz qâle li-qavmihî", True), say('say 7:80 5-6', "e-te'tûne'l-fâhişete", True), say('dizi 7 80 3 6', "qâle qavm etâ fâhişe"), say('dizi 7 80 1 6', "lût iz qâle qavm etâ fâhişe"), say('dizi 7 80 1 4', "lût iz qâle qavm")) + ' '
 + cumle(say('say 7:80 7-13', "mâ sebeqakum bihâ min ehadin mine'l-'âlemîn", True), say('dizi 7 80 6 13', "fâhişe mâ sebeqa _ min ehad min 'âlem")) + ' ' +
 "Ölçüm xref 27:54 (emsal olarak basıldı), 29:28 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıbı yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + özel ad + 'iz' + PERF + 'li' + izafet + 'e' + IMPF + belirli + 'mâ' + PERF + 'bi' + 'min' + nekre + 'min' + belirli; "
 "D2 soru; INTG ('e-te'tûne' 5. kelime), NEG ('mâ' 7. kelime); D3 27:54 eşi, 29:28 eşi; D4 2MP 3 · 3FS 1 · 3MS 3, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[80] + "; aktör adlı 'lûtan' (1. kelime; ölçüm rol meful); A2 Lût'un gönderilişi; kavmine âlemlerden hiç kimsenin önce yapmadığı hayâsızlığın sorulması; "
 "A3 'e-te'tûne'l-fâhişete mâ sebeqakum bihâ min ehadin mine'l-'âlemîn' (söz içi, 5-13. kelime; ayet sonunda kapanmıyor); "
 "A4 " + BOLUM + "; söz açılır (5. kelime); şahıs geçişi 1 → 3 (ayetler arası); edim geçişi nida → soru (ayetler arası).",
)

D[81] = ("◇ 'innekum le-te'tûne'r-ricâle şehveten min dûni'n-nisâ'i bel entum qavmun musrifûn' — "
 "'inne' + 2MP + 'le' + IMPF 2MP I. bab + belirli çoğul 'ricâl' + nekre 'şehve' + 'min' + 'dûn' + belirli çoğul 'nisâ'' + 'bel' + 2MP + nekre 'qavm' + çoğul etken ortaç 'musrif' "
 "(ölçüm edim haber, kip EMPH 1; 2MP 4; bab I. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok (ölçüm); ölçüm '{{2|" + _AK2 + "}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=11 (n z=-0,15); ölçüm '{{2|fâsıla " + _F[1] + " → ن, N sınıfı}}' — satır aynen (7:80 ن → 7:81 ن); "
 "ölçüm '{{2|harf 49 → harf3 46, isaret 3}}' — satır aynen; ölçüm '{{2|dış düğüm 1}}' — satır aynen; ölçüm '{{2|esit2 → 27:55 oran 0,9032 kademe BENZER}}' — satır aynen. "
 "Ölçüm EMPH 1: 'le-te'tûne' (2. kelime; 'le'); ölçüm biçim IDRAB; 'innekum' (1.) ACC; 'bel' (8.) RET (okuma). "
 + T[81] + " (okuma). "
 + cumle(say('say 7:81 1-7', "innekum le-te'tûne'r-ricâle şehveten min dûni'n-nisâ'i", True), say('say 7:81 3-7', "r-ricâle şehveten min dûni'n-nisâ'i"), say('say 7:81 1-2', "innekum le-te'tûne"), say('say 7:81 2-3', "le-te'tûne'r-ricâle"), say('dizi 7 81 1 2', "inne etâ"), say('dizi 7 81 1 3', "inne etâ ricâl"), say('dizi 7 81 1 8', "inne etâ ricâl şehve min dûn nisâ' bel")) + ' '
 + cumle(say('say 7:81 8-11', "bel entum qavmun musrifûn", True)) + ' ' +
 "Ölçüm xref 27:55 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıbı yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'r-ricâle' / 'n-nisâ'i' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'inne' + 'le' + IMPF + belirli + nekre + 'min' + izafet + belirli + 'bel' + zamir + nekre + çoğul; "
 "D2 haber; EMPH ('le-te'tûne' 2. kelime); D3 27:55 eşi, 29:28 eşi, 29:29 eşi; D4 2MP 4, sahset ['2'], iltifât 0.",
 "◈A — A1 " + T[81] + "; aktör adsız 'r-ricâle' (3. kelime; ölçüm racül); A2 kadınları bırakıp erkeklere şehvetle yönelişin bildirilmesi; aşırı giden kavim nitelemesi; "
 "A3 'innekum le-te'tûne'r-ricâle şehveten min dûni'n-nisâ'i bel entum qavmun musrifûn' (söz sürüyor (7:80 5. kelimeden, 1-11. kelime)); "
 "A4 " + BOLUM + "; söz kapanır (11. kelime); şahıs geçişi 3 → 2 (ayetler arası); edim geçişi soru → haber (ayetler arası).",
)

D[82] = ("◇ 've mâ kâne cevâbe qavmihî illâ en qâlû exricûhum min qaryetikum innehum unâsun yetetahharûn' — "
 "'ve' + 'mâ' + PERF 3MS I. bab + 'cevâb' + 'qavm' + 3MS + 'illâ' + 'en' + PERF 3MP I. bab + IMPV 2MP IV. bab + 3MP + 'min' + 'qarye' + 2MP + 'inne' + 3MP + nekre çoğul 'unâs' + IMPF 3MP V. bab "
 "(ölçüm edim emir, kip IMPV 1 · NEG 1 · RES 1; 2MP 3 · 3MP 6 · 3MS 2; bab I. bab ×2 · IV. bab ×1 · V. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok (ölçüm); ölçüm '{{3|" + _AK3 + "}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=13 (n z=0,06); ölçüm '{{3|fâsıla " + _F[2] + " → ن, N sınıfı}}' — satır aynen (7:81 ن → 7:82 ن); "
 "ölçüm '{{3|harf 58 → harf3 54, isaret 4}}' — satır aynen; ölçüm '{{3|dış düğüm 3}}' — satır aynen; ölçüm '{{3|esit2 → 27:56 oran 0,9027 kademe BENZER}}' — satır aynen. "
 "Ölçüm IMPV 1: 'exricûhum' (8. kelime); NEG 1: 've mâ' (1. kelime; 'mâ'); RES 1: 'illâ' (5. kelime); ölçüm biçim HASR; 've mâ' (1.) kelimesindeki 've' REM; 'en' (6.) SUB; 'innehum' (11.) ACC (okuma). "
 + T[82] + " (okuma). "
 + cumle(say('say 7:82 1-5', "ve mâ kâne cevâbe qavmihî illâ", True), say('say 7:82 2-5', "kâne cevâbe qavmihî illâ"), say('say 7:82 3-4', "cevâbe qavmihî"), say('dizi 7 82 1 7', "mâ kâne cevâb qavm illâ en qâle"), say('dizi 7 82 1 8', "mâ kâne cevâb qavm illâ en qâle exrece"), say('dizi 7 82 5 7', "illâ en qâle")) + ' '
 + cumle(say('say 7:82 6-10', "en qâlû exricûhum min qaryetikum", True), say('say 7:82 11-13', "innehum unâsun yetetahharûn", True), say('dizi 7 82 9 13', "min qarye inne insân tetahhar")) + ' ' +
 "Ölçüm xref 27:56 (emsal olarak basıldı), 29:24 (emsal olarak basıldı), 29:29 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıbı: 'illâ en qâle' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 'unâsun' (12. kelime).",
 "◈D — D1 've' + 'mâ' + PERF + izafet + izafet + 'illâ' + 'en' + PERF + IMPV + 'min' + izafet + 'inne' + nekre + IMPF; "
 "D2 emir; IMPV ('exricûhum' 8. kelime), NEG ('ve mâ' 1. kelime), RES ('illâ' 5. kelime); D3 27:56 eşi, 29:24 eşi, 29:29 eşi; D4 2MP 3 · 3MP 6 · 3MS 2, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[82] + "; aktör adsız 'qaryetikum' (10. kelime; ölçüm karye); A2 kavmin cevabının yalnız sürgün çağrısı oluşu; temizlenmeye çalışan insanlar nitelemesi; "
 "A3 'exricûhum min qaryetikum innehum unâsun yetetahharûn' (söz içi, 8-13. kelime); "
 "A4 " + BOLUM + "; söz açılır (8. kelime); söz kapanır (13. kelime, ayet içi); şahıs geçişi 2 → 3 (ayetler arası); edim geçişi haber → emir (ayetler arası).",
)

D[83] = ("◇ 'fe-enceynâhu ve ehlehû ille'mra'etehû kânet mine'l-ğâbirîn' — "
 "'fe' + PERF 1P IV. bab + 3MS + 've' + 'ehl' + 3MS + 'illâ' + 'imrae' + 3MS + PERF 3FS I. bab + 'min' + belirli çoğul etken ortaç 'ğâbir' "
 "(ölçüm edim haber, kip yok; 1P 2 · 3FS 1 · 3MS 3; bab I. bab ×1 · IV. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok (ölçüm); ölçüm '{{4|" + _AK4 + "}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=7 (n z=-0,58); ölçüm '{{4|fâsıla " + _F[3] + " → ن, N sınıfı}}' — satır aynen (7:82 ن → 7:83 ن); "
 "ölçüm '{{4|harf 36 → harf3 34, isaret 2}}' — satır aynen; ölçüm '{{4|dış düğüm 3}}' — satır aynen; ölçüm '{{4|esit2 → 27:57 oran 0,8824 kademe BENZER}}' — satır aynen. "
 "Ölçüm biçim ISTISNA ('illâ' 3. kelime); 'fe-enceynâhu' (1.) kelimesindeki 'fe' REM; 've ehlehû' (2.) kelimesindeki 've' CONJ (okuma). "
 + T[83] + " (okuma). "
 + cumle(say('say 7:83 1-2', "fe-enceynâhu ve ehlehû", True), say('dizi 7 83 1 4', "encâ ehl illâ imrae")) + ' '
 + cumle(say('say 7:83 3-4', "ille'mra'etehû", True), say('say 7:83 5-7', "kânet mine'l-ğâbirîn", True), say('say 7:83 3-7', "ille'mra'etehû kânet mine'l-ğâbirîn"), say('dizi 7 83 2 7', "ehl illâ imrae kâne min ğâbir")) + ' ' +
 "Ölçüm xref 27:57 (emsal olarak basıldı), 29:32 (emsal olarak basıldı), 29:33 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıbı yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'fe' + PERF + 've' + izafet + 'illâ' + izafet + PERF + 'min' + belirli; "
 "D2 haber; kip yok; D3 27:57 eşi, 29:32 eşi, 29:33 eşi; D4 1P 2 · 3FS 1 · 3MS 3, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[83] + "; aktör adsız 'mra'etehû' (4. kelime; ölçüm imrae); A2 Lût'un ve ailesinin kurtarılışı; karısının istisnası ve geride kalışı; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi emir → haber (ayetler arası).",
)

D[84] = ("◇ 've emtarnâ 'aleyhim mataran fe'nzur keyfe kâne 'âqibetu'l-mucrimîn' — "
 "'ve' + PERF 1P IV. bab + ''alâ' + 3MP + nekre 'matar' + 'fe' + IMPV 2MS I. bab + 'keyfe' + PERF 3MS I. bab + ''âqibe' + belirli çoğul etken ortaç 'mucrim' "
 "(ölçüm edim emir, kip IMPV 1; 1P 2 · 2MS 1 · 3MP 1 · 3MS 1; bab I. bab ×2 · IV. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=8 (n z=-0,47); ölçüm '{{5|fâsıla " + _F[4] + " → ن, N sınıfı}}' — satır aynen (7:83 ن → 7:84 ن); "
 "ölçüm '{{5|harf 41 → harf3 39, isaret 2}}' — satır aynen; ölçüm '{{5|dış düğüm 1}}' — satır aynen. "
 "Ölçüm IMPV 1: 'fe'nzur' (4. kelime); 've emtarnâ' (1.) kelimesindeki 've' CONJ; 'fe'nzur' (4.) kelimesindeki 'fe' REM (okuma). "
 "Kök ikilemesi (ölçüm) مطر ×2 ('emtarnâ' 1. / 'mataran' 3. kelime) (okuma). "
 + T[84] + " (okuma). "
 + cumle(say('say 7:84 1-3', "ve emtarnâ 'aleyhim mataran", True), say('say 7:84 4-8', "fe'nzur keyfe kâne 'âqibetu'l-mucrimîn", True), say('say 7:84 4-7', "fe'nzur keyfe kâne 'âqibetu"), say('dizi 7 84 4 7', "nazara keyfe kâne 'âqibe")) + ' ' +
 "Ölçüm xref 27:69 (basılmış). "
 "Ölçüm nakarat3 kalıbı: 'nazara keyfe kâne 'âqibe' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + PERF + ''alâ' + nekre + 'fe' + IMPV + 'keyfe' + PERF + izafet + belirli; "
 "D2 emir; IMPV ('fe'nzur' 4. kelime); D3 مطر ×2; D4 1P 2 · 2MS 1 · 3MP 1 · 3MS 1, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[84] + "; aktör yok (ölçüm); A2 üzerlerine yağmur yağdırılışı; suçluların sonuna bakma çağrısı; "
 "A3 —; "
 "A4 " + BOLUM + "; bölüm kapanışı; şahıs sayısında beraberlik (1P 2 · 3. şahıs 2 — ölçüm baskın 1); şahıs geçişi 3 → 1 (ayetler arası); edim geçişi haber → emir (ayetler arası).",
)
out = ['# ── blok 7:80-84 (2026-11-28) ──', 'MEAL23 = {']
for n in range(80, 85):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M23 = {']
for n in range(80, 85):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL23); M.update(M23)']
open('/home/claude/yamalar/metin_7_80_84.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

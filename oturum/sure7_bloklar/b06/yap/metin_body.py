# sûre 7 blok 6 (7:22-25) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os, re
os.environ['SAY2'] = '/home/claude/b06/say2.txt'
os.environ['OLC'] = '/home/claude/b06/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Âdem'e secde; İblis'in mühleti; ağaç ve iniş' bölümünde"
_OL = [l.replace('**', '') for l in open(os.environ['OLC'], encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
def _esc(t):
    for c in '.()[]|+': t = t.replace(c, '\\' + c)
    return t
_AK1 = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[0]).group(0))
_ES1 = _esc(re.search(r'esmâ \S+ 28\. sırada, SON konum, MÜHÜRSÜZ', _OL[0]).group(0))


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 22: "Böylece onları aldatışla düşürdü. Ağacı tattıklarında çirkin yerleri kendilerine göründü ve bahçe yaprağından üzerlerine yamamaya koyuldular. Rableri onlara seslendi: Size o ağacı yasaklamadım mı ve size demedim mi: Şeytan gerçekten sizin için apaçık bir düşmandır.",
 23: "Dediler ki: Rabbimiz, kendimize zulmettik; bizi bağışlamaz ve bize merhamet etmezsen mutlaka ziyana uğrayanlardan oluruz.",
 24: "Dedi ki: İnin; birbiriniz için düşmansınız. Yeryüzünde size bir vakte kadar kalacak yer ve geçimlik var.",
 25: "Dedi ki: Orada yaşarsınız, orada ölürsünüz ve oradan çıkarılırsınız.",
}

T = {}
T[22] = ("'fe-dellâhumâ' 3MS (adsız; gönderge 7:20 3. kelime, 1. kelime); 'fe-dellâhumâ', 'lehumâ', 'sev'âtuhumâ', 'yaxsifâni', ''aleyhimâ', 've nâdâhumâ', 'rabbuhumâ' 3D eki (adsız; gönderge 7:19 6. kelime — 1., 7., 8., 10., 11., 15. ve 16. kelime); "
         "'zâqe', 've tafiqâ', 'yaxsifâni' 3MD (adsız; gönderge 7:19 6. kelime — 4., 9. ve 10. kelime); 'bedet' 3FS (fiil uyumu; 6. kelime — fail 8. kelime); 've nâdâhumâ' 3MS (fiil uyumu; 15. kelime — fail 16. kelime); "
         "konuşan 1S (adsız; söz içi; 'enhekumâ', 've aqul' — 18. ve 22. kelime); muhatap 2D eki (adsız; söz içi; 'enhekumâ', 'lekumâ', 'lekumâ' — 18., 23. ve 26. kelime)")
T[23] = ("'qâlâ' 3MD (adsız; gönderge 7:19 6. kelime, 1. kelime); konuşan 1P eki (adsız; söz içi; 'rabbenâ', 'enfusenâ', 'lenâ', 've terhamnâ' — 2., 4., 8. ve 9. kelime); konuşan 1P (adsız; söz içi; 'zalemnâ', 'le-nekûnenne' — 3. ve 10. kelime); "
         "muhatap 2MS (adsız; söz içi; 'teğfir' — 7. kelime); 've terhamnâ' 3FS (adsız; söz içi; morph etiketi, okuma muhatap 2MS — 9. kelime)")
T[24] = ("'qâle' 3MS (adsız; gönderge 7:22 16. kelime, 1. kelime); muhatap 2MP (adsız; söz içi; 'hbitû' — 2. kelime); muhatap 2MP eki (adsız; söz içi; 'ba'dukum', 've lekum' — 3. ve 6. kelime)")
T[25] = ("'qâle' 3MS (adsız; gönderge 7:22 16. kelime, 1. kelime); 'fîhâ', 've fîhâ', 've minhâ' 3FS eki (adsız; söz içi; gönderge 7:24 8. kelime — 2., 4. ve 6. kelime); muhatap 2MP (adsız; söz içi; 'tahyevne', 'temûtûne' — 3. ve 5. kelime); "
         "muhatap 2MP (adsız; söz içi; edilgen, naib-i faili zamir; 'tuxracûn' — 7. kelime)")

D = {}
D[22] = ("◇ 'fe-dellâhumâ bi-ğurûrin fe-lemmâ zâqe'ş-şecerate bedet lehumâ sev'âtuhumâ ve tafiqâ yaxsifâni 'aleyhimâ min varaqi'l-cenneti ve nâdâhumâ rabbuhumâ e-lem enhekumâ 'an tilkume'ş-şecerati ve aqul lekumâ inne'ş-şeytâne lekumâ 'aduvvun mubîn' — "
 "'fe' + PERF 3MS I. bab + 3D + 'bi' + nekre 'ğurûr' + 'fe' + 'lemmâ' + PERF 3MD I. bab + belirli 'şecera' + PERF 3FS I. bab + 'li' + 3D + çoğul 'sev'e' + 3D + 've' + PERF 3MD I. bab + IMPF 3MD I. bab + ''alâ' + 3D + 'min' + 'varaq' + belirli 'cenne' + 've' + PERF 3MS III. bab + 3D + 'rabb' + 3D + "
 "'e' + 'lem' + IMPF 1S I. bab + 2D + ''an' + 'zâ' + belirli 'şecera' + 've' + IMPF 1S I. bab + 'li' + 2D + 'inne' + belirli 'şeytân' + 'li' + 2D + nekre ''aduvv' + nekre etken ortaç 'mubîn' "
 "(ölçüm edim soru, kip INTG 1 · NEG 1; 1S 2 · 2D 3 · 3D 7 · 3FS 1 · 3MD 5 · 3MS 2; bab I. bab ×7 · III. bab ×1). "
 "Allah lafzı yok; Rab 16. sırada (ölçüm rab z=0,44); ölçüm '{{1|" + _ES1 + "}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton denge' — ölçüm MÜHÜRSÜZ ile uyuşmuyor (araç tanımı farkı; muhur_el hayır — ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 'inne'ş-şeytâne lekumâ 'aduvvun mubîn', kural 'esmâ adı esmâ dışı göndergeyle → degil' (şeytanın düşmanlık sıfatı) (okuma); ölçüm '{{1|" + _AK1 + "}}' — satır aynen. "
 "Ölçüm '{{1|yıldız ★}}' — satır aynen (kaynak n, z=1,65); n=28 (n z=1,65); ölçüm '{{1|fâsıla " + _F[0] + " → ن, N sınıfı}}' — satır aynen (7:21 ن → 7:22 ن); "
 "ölçüm '{{1|simetri \\[3, 3, 19, 1\\]}}' — satır aynen; ölçüm '{{1|harf 134 → harf3 129, isaret 5}}' — satır aynen; ölçüm '{{1|dış düğüm 1}}' — satır aynen. "
 "Ölçüm INTG 1: 'e-lem' (17. kelime; 'e'); NEG 1: 'e-lem' (17. kelime; 'lem'); "
 "'fe-dellâhumâ' (1.) kelimesindeki 'fe' CONJ; 'fe-lemmâ' (3.) kelimesindeki 'fe' REM; 've tafiqâ' (9.) kelimesindeki 've' CONJ; 've nâdâhumâ' (15.) kelimesindeki 've' REM; 'tilkume' (20.) DEM + DIST + ADDR; 've aqul' (22.) kelimesindeki 've' CONJ; 'inne' (24.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) شجر ×2 ('ş-şecerate' 5. / 'ş-şecerati' 21. kelime) (okuma). "
 + T[22] + " (okuma). "
 + cumle(say('say 7:22 1-2', "fe-dellâhumâ bi-ğurûrin", True), say('say 7:22 3-5', "fe-lemmâ zâqe'ş-şecerate")) + ' '
 + cumle(say('say 7:22 9-14', "ve tafiqâ yaxsifâni 'aleyhimâ min varaqi'l-cenneti", True), say('say 7:22 8-14', "sev'âtuhumâ ve tafiqâ yaxsifâni 'aleyhimâ min varaqi'l-cenneti"), say('say 7:22 7-8', "lehumâ sev'âtuhumâ"),
         say('dizi 7 22 8 14', "sev'e tafiqa yaxsife 'alâ min varaq cenne"), say('dizi 7 22 6 14', "bedâ _ sev'e tafiqa yaxsife 'alâ min varaq cenne")) + ' '
 + cumle(say('say 7:22 15-16', "ve nâdâhumâ rabbuhumâ", True), say('say 7:22 17-21', "e-lem enhekumâ 'an tilkume'ş-şecerati"), say('say 7:22 22-23', "ve aqul lekumâ"), say('say 7:22 24-28', "inne'ş-şeytâne lekumâ 'aduvvun mubîn"), say('say 7:22 27-28', "'aduvvun mubîn")) + ' ' +
 "Ölçüm xref 20:121 (emsal olarak basıldı). "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 'ş-şecerate' (5. kelime), 'ş-şecerati' (21. kelime).",
 "◈D — D1 'fe' + PERF + 'bi' + nekre + 'fe' + 'lemmâ' + PERF + belirli + PERF + 'li' + izafet + 've' + PERF + IMPF + ''alâ' + 'min' + izafet + belirli + 've' + PERF + izafet + 'e' + 'lem' + IMPF + ''an' + 'zâ' + belirli + 've' + IMPF + 'li' + 'inne' + belirli + 'li' + nekre + nekre; "
 "D2 soru; INTG ('e-lem' 17. kelime), NEG ('e-lem' 17. kelime); D3 20:121 eşi, شجر ×2; D4 1S 2 · 2D 3 · 3D 7 · 3FS 1 · 3MD 5 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[22] + "; aktör adlı 'l-cenneti' (14. kelime; ölçüm rol mecrur), 'ş-şeytâne' (25. kelime; ölçüm rol meful); A2 aldatışla düşürülme; ağacın tadılması, çirkin yerlerin görünmesi ve bahçe yaprağıyla örtünme; Rablerinin yasağı ve şeytanın düşmanlığını hatırlatan seslenişi; "
 "A3 'e-lem enhekumâ 'an tilkume'ş-şecerati ve aqul lekumâ inne'ş-şeytâne lekumâ 'aduvvun mubîn' (söz biçimli içerik, 17. kelimeden); "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi haber → soru (ayetler arası).",
)

D[23] = ("◇ 'qâlâ rabbenâ zalemnâ enfusenâ ve in lem teğfir lenâ ve terhamnâ le-nekûnenne mine'l-xâsirîn' — "
 "PERF 3MD I. bab + 'rabb' + 1P + PERF 1P I. bab + çoğul 'nefs' + 1P + 've' + 'in' + 'lem' + IMPF 2MS I. bab + 'li' + 1P + 've' + IMPF 3FS I. bab + 1P + 'le' + IMPF 1P I. bab + 'min' + belirli çoğul etken ortaç 'xâsir' "
 "(ölçüm edim şart, kip COND 1 · EMPH 2 · NEG 1; 1P 7 · 2MS 1 · 3FS 1 · 3MD 2; bab I. bab ×5). "
 "Allah lafzı yok; Rab 2. sırada (ölçüm rab z=1,45); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=12 (n z=-0,04); ölçüm '{{2|fâsıla " + _F[1] + " → ن, N sınıfı}}' — satır aynen (7:22 ن → 7:23 ن); "
 "ölçüm '{{2|harf 53 → harf3 53, isaret 0}}' — satır aynen; ölçüm '{{2|dış düğüm 3}}' — satır aynen. "
 "Ölçüm COND 1: 'in' (5. kelime); EMPH 2: 'le-nekûnenne' (10. kelime; 'le' ve pekiştirme nûnu); NEG 1: 'lem' (6. kelime); "
 "'ve in' (5.) kelimesindeki 've' CONJ; 've terhamnâ' (9.) kelimesindeki 've' CONJ (okuma). "
 "'ve terhamnâ' (9.) kelimesinin morph şahıs etiketi 3FS; okuma 7. kelimedeki 'teğfir' ile eş özne, muhatap 2MS — A1'de morph etiketi korundu (okuma). "
 + T[23] + " (okuma). "
 + cumle(say('say 7:23 3-4', "zalemnâ enfusenâ", True), say('say 7:23 2-4', "rabbenâ zalemnâ enfusenâ")) + ' '
 + cumle(say('say 7:23 5-9', "ve in lem teğfir lenâ ve terhamnâ", True), say('say 7:23 7-9', "teğfir lenâ ve terhamnâ"), say('dizi 7 23 7 9', "ğafera _ rahime")) + ' '
 + cumle(say('say 7:23 10-12', "le-nekûnenne mine'l-xâsirîn", True), say('dizi 7 23 10 12', "kâne min xâsir"), say('say 7:23 5-12', "ve in lem teğfir lenâ ve terhamnâ le-nekûnenne mine'l-xâsirîn")) + ' ' +
 "Ölçüm xref okunmuş 3 ayet. "
 "Ölçüm nakarat3 kalıbı: 'ğafera _ rahime' süzgeç GEÇMEZ; 'kâne min xâsir' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 PERF + izafet + PERF + izafet + 've' + 'in' + 'lem' + IMPF + 'li' + 've' + IMPF + 'le' + IMPF + 'min' + belirli; "
 "D2 şart; COND ('in' 5. kelime), EMPH ('le-nekûnenne' 10. kelime), NEG ('lem' 6. kelime); D3 —; D4 1P 7 · 2MS 1 · 3FS 1 · 3MD 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[23] + "; aktör yok (ölçüm); A2 kendine zulmetme itirafı; bağışlama ve merhamet olmazsa ziyana uğrayanlardan olma; "
 "A3 'rabbenâ zalemnâ enfusenâ ve in lem teğfir lenâ ve terhamnâ le-nekûnenne mine'l-xâsirîn' (söz içi, 2-12. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (12. kelime, ayet içi); şart → cevap (ayet içi; COND 'in' 5. kelime: 'lem teğfir lenâ ve terhamnâ' / 'le-nekûnenne' (10. kelime)); şahıs geçişi 3 → 1 (ayetler arası); edim geçişi soru → şart (ayetler arası).",
)

D[24] = ("◇ 'qâle'hbitû ba'dukum li-ba'din 'aduvvun ve lekum fi'l-ardi musteqarrun ve metâ'un ilâ hîn' — "
 "PERF 3MS I. bab + IMPV 2MP I. bab + 'ba'd' + 2MP + 'li' + nekre 'ba'd' + nekre ''aduvv' + 've' + 'li' + 2MP + 'fî' + belirli 'ard' + nekre edilgen ortaç 'musteqarr' + 've' + nekre 'metâ'' + 'ilâ' + nekre 'hîn' "
 "(ölçüm edim emir, kip IMPV 1; 2MP 4 · 3MS 1; bab I. bab ×2). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=12 (n z=-0,04); ölçüm '{{3|fâsıla " + _F[2] + " → ن, N sınıfı}}' — satır aynen (7:23 ن → 7:24 ن); "
 "ölçüm '{{3|harf 52 → harf3 47, isaret 5}}' — satır aynen; ölçüm '{{3|dış düğüm 1}}' — satır aynen. "
 "Ölçüm IMPV 1: 'hbitû' (2. kelime); "
 "'ve lekum' (6.) kelimesindeki 've' CONJ; 've metâ'un' (10.) kelimesindeki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) بعض ×2 ('ba'dukum' 3. / 'li-ba'din' 4. kelime) (okuma). "
 + T[24] + " (okuma). "
 + cumle(say('say 7:24 3-5', "ba'dukum li-ba'din 'aduvvun", True), say('say 7:24 2-5', "hbitû ba'dukum li-ba'din 'aduvvun")) + ' '
 + cumle(say('say 7:24 6-12', "ve lekum fi'l-ardi musteqarrun ve metâ'un ilâ hîn", True), say('say 7:24 2-12', "hbitû ba'dukum li-ba'din 'aduvvun ve lekum fi'l-ardi musteqarrun ve metâ'un ilâ hîn"),
         say('dizi 7 24 2 12', "yehbitu ba'd ba'd 'aduvv _ fî ard musteqarr metâ' ilâ hîn"), say('dizi 7 24 1 12', "qâle yehbitu ba'd ba'd 'aduvv _ fî ard musteqarr metâ' ilâ hîn")) + ' ' +
 "Ölçüm xref 2:36 (emsal olarak basıldı). "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K1 'l-ardi' (8. kelime); K2 'hîn' (12. kelime).",
 "◈B — —",
 "◈D — D1 PERF + IMPV + izafet + 'li' + nekre + nekre + 've' + 'li' + 'fî' + belirli + nekre + 've' + nekre + 'ilâ' + nekre; "
 "D2 emir; IMPV ('hbitû' 2. kelime); D3 2:36 eşi, بعض ×2; D4 2MP 4 · 3MS 1, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[24] + "; aktör yok (ölçüm); A2 inme emri; karşılıklı düşmanlık; yeryüzünde bir vakte kadar kalacak yer ve geçimlik; "
 "A3 'hbitû ba'dukum li-ba'din 'aduvvun ve lekum fi'l-ardi musteqarrun ve metâ'un ilâ hîn' (söz içi, 2-12. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (12. kelime, ayet içi); şahıs geçişi 1 → 2 (ayetler arası); edim geçişi şart → emir (ayetler arası).",
)

D[25] = ("◇ 'qâle fîhâ tahyevne ve fîhâ temûtûne ve minhâ tuxracûn' — "
 "PERF 3MS I. bab + 'fî' + 3FS + IMPF 2MP I. bab + 've' + 'fî' + 3FS + IMPF 2MP I. bab + 've' + 'min' + 3FS + IMPF 2MP IV. bab edilgen "
 "(ölçüm edim haber, kip yok; 2MP 6 · 3FS 3 · 3MS 1; bab I. bab ×3 · IV. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=7 (n z=-0,58); ölçüm '{{4|EDİLGEN 1/4 fiil, pas z=1,10}}' — satır aynen; ölçüm '{{4|fâsıla " + _F[3] + " → ن, N sınıfı}}' — satır aynen (7:24 ن → 7:25 ن); "
 "ölçüm '{{4|harf 34 → harf3 34, isaret 0}}' — satır aynen; ölçüm '{{4|dış düğüm 0}}' — satır aynen. "
 "Ölçüm kip yok; "
 "'ve fîhâ' (4.) kelimesindeki 've' CONJ; 've minhâ' (6.) kelimesindeki 've' CONJ (okuma). "
 + T[25] + " (okuma). "
 + cumle(say('say 7:25 2-3', "fîhâ tahyevne", True), say('say 7:25 4-5', "ve fîhâ temûtûne"), say('say 7:25 6-7', "ve minhâ tuxracûn"), say('say 7:25 2-7', "fîhâ tahyevne ve fîhâ temûtûne ve minhâ tuxracûn")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'tahyevne' / 'temûtûne' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B4 'tahyevne' (3. kelime), 'temûtûne' (5. kelime).",
 "◈D — D1 PERF + 'fî' + IMPF + 've' + 'fî' + IMPF + 've' + 'min' + IMPF; "
 "D2 haber; D3 —; D4 2MP 6 · 3FS 3 · 3MS 1, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[25] + "; aktör yok (ölçüm); A2 yeryüzünde yaşama, ölme ve oradan çıkarılma; "
 "A3 'fîhâ tahyevne ve fîhâ temûtûne ve minhâ tuxracûn' (söz içi, 2-7. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (7. kelime, ayet içi); şahıs geçişi yok (ayetler arası); edim geçişi emir → haber (ayetler arası); bölüm kapanışı.",
)
out = ['# ── blok 7:22-25 (2026-11-25) ──', 'MEAL6 = {']
for n in range(22, 26):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M6 = {']
for n in range(22, 26):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL6); M.update(M6)']
open('/home/claude/yamalar/metin_7_22_25.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

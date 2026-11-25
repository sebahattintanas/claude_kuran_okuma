# sûre 7 blok 12 (7:42-43) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os, re
os.environ['SAY2'] = '/home/claude/b12/say2.txt'
os.environ['OLC'] = '/home/claude/b12/olcum.txt'
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
_AK2 = _esc(re.search(r'aktör: adlı .*?rol fail\)', _OL[1]).group(0))


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 42: "İman edip salih ameller işleyenler; biz hiçbir cana gücünün yettiğinden fazlasını yüklemeyiz; işte onlar bahçenin halkıdır; onlar orada ebedî kalanlardır.",
 43: "Göğüslerindeki kini çekip aldık; altlarından ırmaklar akar. Dediler ki: Bize buna yol gösteren Allah'a hamd olsun; Allah bize yol göstermeseydi biz doğru yolu bulacak değildik. Andolsun, Rabbimizin elçileri hak ile geldi. Ve seslenildi ki: O bahçe, işlemekte olduklarınızdan dolayı size miras kılındı.",
}

T = {}
T[42] = ("'âmenû', 've 'amilu' 3MP (adsız; gönderge 've'llezîne' 1. kelime — 2. ve 3. kelime); konuşan 1P (adsız; 'nukellifu' — 6. kelime); 'vus'ahâ' 3FS eki (adsız; gönderge 'nefsen' 7. kelime, 9. kelime); "
         "'hum' 3MP (adsız; gönderge 've'llezîne' 1. kelime, 13. kelime); 'fîhâ' 3FS eki (adsız; gönderge 'l-cenneti' 12. kelime, 14. kelime)")
T[43] = ("konuşan 1P (adsız; 've neza'nâ' — 1. kelime); 'sudûrihim', 'tahtihimu' 3MP eki (adsız; gönderge 7:42 1. kelime — 4. ve 9. kelime); 'tecrî' 3FS (fiil uyumu; 7. kelime — fail 10. kelime); 've qâlu' 3MP (adsız; gönderge 7:42 1. kelime, 11. kelime); "
         "'hedânâ' 3MS (adsız; söz içi; gönderge 'li'llâhi' 13. kelime, 15. kelime); konuşan 1P eki (adsız; söz içi; 'hedânâ', 'hedâna', 'rabbinâ' — 15., 22. ve 27. kelime); konuşan 1P (adsız; söz içi; 'kunnâ', 'li-nehtediye' — 18. ve 19. kelime); "
         "'hedâna' 3MS (fiil uyumu; söz içi; 22. kelime — fail 23. kelime); 'câ'et' 3FS (fiil uyumu; söz içi; 25. kelime — fail 26. kelime); 've nûdû' 3MP (adsız; edilgen, naib-i faili zamir; gönderge 7:42 1. kelime, 29. kelime); "
         "muhatap 2MP (adsız; söz içi; edilgen, naib-i faili zamir; 'ûristumûhâ' — 33. kelime); muhatap 2MP (adsız; söz içi; 'kuntum', 'ta'melûn' — 35. ve 36. kelime); 'ûristumûhâ' 3FS eki (adsız; söz içi; gönderge 'l-cennetu' 32. kelime, 33. kelime)")

D = {}
D[42] = ("◇ 've'llezîne âmenû ve 'amilu's-sâlihâti lâ nukellifu nefsen illâ vus'ahâ ulâ'ike ashâbu'l-cenneti hum fîhâ xâlidûn' — "
 "'ve' + 'ellezî' + PERF 3MP IV. bab + 've' + PERF 3MP I. bab + belirli çoğul etken ortaç 'sâlih' + 'lâ' + IMPF 1P II. bab + nekre 'nefs' + 'illâ' + 'vus'' + 3FS + 'ulâ'i' + 'ashâb' + belirli 'cenne' + 'hum' + 'fî' + 3FS + çoğul etken ortaç 'xâlid' "
 "(ölçüm edim haber, kip NEG 1; 1P 1 · 3FS 2 · 3MP 5; bab I. bab ×1 · II. bab ×1 · IV. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok (ölçüm); ölçüm '{{1|" + _AK1 + "}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=15 (n z=0,27); ölçüm '{{1|fâsıla " + _F[0] + " → ن, N sınıfı}}' — satır aynen (7:41 ن → 7:42 ن); "
 "ölçüm '{{1|harf 71 → harf3 67, isaret 4}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen. "
 "Ölçüm NEG 1: 'lâ' (5. kelime); ölçüm biçim ISTISNA; "
 "'ve'llezîne' (1.) CONJ + REL; 've 'amilu' (3.) kelimesindeki 've' CONJ; 'illâ' (8.) EXP; 'ulâ'ike' (10.) DEM + ADDR (okuma). "
 + T[42] + " (okuma). "
 + cumle(say('say 7:42 1-4', "ve'llezîne âmenû ve 'amilu's-sâlihâti", True)) + ' '
 + say('say 7:42 5-9', "lâ nukellifu nefsen illâ vus'ahâ", True) + " (--medde 2 ayet: 'vus'ahâ' yazım farkı ile; harekesiz sayım elif / medde yazımına bağlı). "
 + cumle(say('say 7:42 10-12', "ulâ'ike ashâbu'l-cenneti", True), say('say 7:42 13-15', "hum fîhâ xâlidûn"), say('dizi 7 42 13 15', "_ fî xâlid"), say('say 7:42 10-15', "ulâ'ike ashâbu'l-cenneti hum fîhâ xâlidûn")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: '_ fî xâlid' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'ellezî' + PERF + 've' + PERF + belirli + 'lâ' + IMPF + nekre + 'illâ' + izafet + 'ulâ'i' + izafet + belirli + 'hum' + 'fî' + 'xâlid'; "
 "D2 haber; NEG ('lâ' 5. kelime); D3 —; D4 1P 1 · 3FS 2 · 3MP 5, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[42] + "; aktör adlı 'l-cenneti' (12. kelime; ölçüm rol mecrur); A2 iman edip salih ameller işleyenlerin bahçe halkı oluşu ve orada ebedî kalışı; cana gücünün yettiğinden fazlası yüklenmeyişi; "
 "A3 —; "
 "A4 " + BOLUM + "; bölüm açılışı; şahıs geçişi yok (ayetler arası); edim geçişi yok (ayetler arası).",
)

D[43] = ("◇ 've neza'nâ mâ fî sudûrihim min ğıllin tecrî min tahtihimu'l-enhâru ve qâlu'l-hamdu li'llâhi'llezî hedânâ li-hâzâ ve mâ kunnâ li-nehtediye levlâ en hedâna'llâhu le-qad câ'et rusulu rabbinâ bi'l-haqqi ve nûdû en tilkumu'l-cennetu ûristumûhâ bimâ kuntum ta'melûn' — "
 "'ve' + PERF 1P I. bab + 'mâ' + 'fî' + çoğul 'sadr' + 3MP + 'min' + nekre 'ğıll' + IMPF 3FS I. bab + 'min' + 'taht' + 3MP + belirli çoğul 'neher' + 've' + PERF 3MP I. bab + belirli 'hamd' + 'li' + 'allâh' + 'ellezî' + PERF 3MS I. bab + 1P + 'li' + 'hâ' + 'zâ' + "
 "'ve' + 'mâ' + PERF 1P I. bab + 'li' + IMPF 1P VIII. bab + 'levlâ' + 'en' + PERF 3MS I. bab + 1P + 'allâh' + 'le' + 'qad' + PERF 3FS I. bab + çoğul 'rasûl' + 'rabb' + 1P + 'bi' + belirli 'haqq' + 've' + PERF 3MP III. bab edilgen + 'en' + 'zâ' + belirli 'cenne' + PERF 2MP IV. bab edilgen + 3FS + 'bi' + 'mâ' + PERF 2MP I. bab + IMPF 2MP I. bab "
 "(ölçüm edim şart, kip CERT 1 · COND 1 · EMPH 1 · NEG 1; 1P 8 · 2MP 6 · 3FS 3 · 3MP 6 · 3MS 2; bab I. bab ×9 · III. bab ×1 · IV. bab ×1 · VIII. bab ×1). "
 "Allah lafzı 13. ve 23. sırada (ölçüm allah z=0,58); Rab 27. sırada (ölçüm rab z=0,27); esmâ yok (ölçüm); ölçüm '{{2|" + _AK2 + "}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{2|yıldız ★★}}' — satır aynen (kaynak n, z=2,50); n=36 (n z=2,50); ölçüm '{{2|EDİLGEN 2/12 fiil, pas z=0,62}}' — satır aynen; ölçüm '{{2|fâsıla " + _F[1] + " → ن, N sınıfı}}' — satır aynen (7:42 ن → 7:43 ن); "
 "ölçüm '{{2|simetri \\[4, 14, 21, 1\\]}}' — satır aynen; ölçüm '{{2|harf 155 → harf3 149, isaret 6}}' — satır aynen; ölçüm '{{2|dış düğüm 4}}' — satır aynen. "
 "Ölçüm CERT 1: 'le-qad' (24. kelime; 'qad'); COND 1: 'levlâ' (20. kelime); EMPH 1: 'le-qad' (24. kelime; 'le'); NEG 1: 've mâ' (17. kelime; 'mâ'); ölçüm biçim DIKKAT; "
 "'ve neza'nâ' (1.) kelimesindeki 've' REM; 'mâ' (2.) REL; 've qâlu' (11.) kelimesindeki 've' CONJ; 'llezî' (14.) REL; 'li-hâzâ' (16.) P + ATT + DEM; 've mâ' (17.) kelimesindeki 've' CONJ; 'li-nehtediye' (19.) PRP; 'en' (21.) SUB; "
 "'ve nûdû' (29.) kelimesindeki 've' CONJ; 'en' (30.) INT; 'tilkumu' (31.) DEM + DIST + ADDR; 'bimâ' (34.) P + REL (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 ('li'llâhi' 13. / 'llâhu' 23. kelime); كون ×2 ('kunnâ' 18. / 'kuntum' 35. kelime); هدي ×3 ('hedânâ' 15. / 'li-nehtediye' 19. / 'hedâna' 22. kelime) (okuma). "
 + T[43] + " (okuma). "
 + cumle(say('say 7:43 1-6', "ve neza'nâ mâ fî sudûrihim min ğıllin", True), say('dizi 7 43 1 6', "neza'a mâ fî sadr min ğıll"), say('say 7:43 7-10', "tecrî min tahtihimu'l-enhâru")) + ' '
 + cumle(say('say 7:43 12-16', "l-hamdu li'llâhi'llezî hedânâ li-hâzâ", True), say('say 7:43 17-23', "ve mâ kunnâ li-nehtediye levlâ en hedâna'llâhu")) + ' '
 + cumle(say('say 7:43 25-28', "câ'et rusulu rabbinâ bi'l-haqqi", True), say('dizi 7 43 25 28', "câ'e rasûl rabb haqq"), say('say 7:43 29-30', "ve nûdû en"), say('say 7:43 31-32', "tilkumu'l-cennetu")) + ' '
 + cumle(say('say 7:43 33-36', "ûristumûhâ bimâ kuntum ta'melûn", True), say('dizi 7 43 33 36', "evrase mâ kâne 'amile"), say('say 7:43 34-36', "bimâ kuntum ta'melûn")) + ' ' +
 "Ölçüm xref 15:47 (emsal olarak basıldı), 43:72 (emsal olarak basıldı), okunmuş 2 ayet. "
 "Ölçüm nakarat3 kalıbı: 'câ'e rasûl rabb haqq' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K1 'l-enhâru' (10. kelime).",
 "◈B — —",
 "◈D — D1 've' + PERF + 'mâ' + 'fî' + izafet + 'min' + nekre + IMPF + 'min' + izafet + belirli + 've' + PERF + belirli + 'li' + lafız + 'ellezî' + PERF + 'li' + 'hâ' + 'zâ' + 've' + 'mâ' + PERF + 'li' + IMPF + 'levlâ' + 'en' + PERF + lafız + 'le' + 'qad' + PERF + izafet + izafet + 'bi' + belirli + 've' + PERF + 'en' + 'zâ' + belirli + PERF + 'bi' + 'mâ' + PERF + IMPF; "
 "D2 şart; CERT ('le-qad' 24. kelime), COND ('levlâ' 20. kelime), EMPH ('le-qad' 24. kelime), NEG ('ve mâ' 17. kelime); D3 15:47 eşi, 43:72 eşi, أله ×2, كون ×2, هدي ×3; D4 1P 8 · 2MP 6 · 3FS 3 · 3MP 6 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[43] + "; aktör adlı 'l-cennetu' (32. kelime; ölçüm rol fail); A2 göğüslerdeki kinin çekilip alınışı; altlarından akan ırmaklar; yol gösteren Allah'a hamd ve elçilerin hak ile gelişinin dile getirilişi; işlenenlerden dolayı bahçenin miras kılındığına dair sesleniş; "
 "A3 'l-hamdu li'llâhi'llezî hedânâ li-hâzâ ve mâ kunnâ li-nehtediye levlâ en hedâna'llâhu le-qad câ'et rusulu rabbinâ bi'l-haqqi' (söz içi, 12-28. kelime); 'tilkumu'l-cennetu ûristumûhâ bimâ kuntum ta'melûn' (söz içi, 31-36. kelime); "
 "A4 " + BOLUM + "; söz açılır (12. kelime); söz kapanır (28. kelime, ayet içi); söz açılır (31. kelime); söz kapanır (36. kelime, ayet içi); şart → cevap (ayet içi; COND 'levlâ' 20. kelime: 'en hedâna'llâhu' / 've mâ kunnâ li-nehtediye' (17. kelime); 'le-qad' (24. kelime) yemin cümlesi, cevap değil); "
 "şahıs geçişi 3 → 1 (ayetler arası); şahıs sayısında toplam farkı (1P 8 · 3. şahıs 11 — ölçüm baskın 1); edim geçişi haber → şart (ayetler arası).",
)
out = ['# ── blok 7:42-43 (2026-11-25) ──', 'MEAL12 = {']
for n in range(42, 44):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M12 = {']
for n in range(42, 44):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL12); M.update(M12)']
open('/home/claude/yamalar/metin_7_42_43.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

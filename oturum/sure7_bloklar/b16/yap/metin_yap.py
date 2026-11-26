# sûre 7 blok 16 (7:54-56) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os, re
os.environ['SAY2'] = '/home/claude/b16/say2.txt'
os.environ['OLC'] = '/home/claude/b16/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Altı günde yaratma; dua; rüzgâr ve ölü belde' bölümünde"
_OL = [l.replace('**', '') for l in open(os.environ['OLC'], encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_HP = _esc(re.search(r'HAPAKS: .*? — hapaks z=3,28', _OL[0]).group(0))


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 54: "Gerçekten Rabbiniz gökleri ve yeri altı günde yaratıp sonra arşa istivâ eden Allah'tır. Geceyi gündüze bürür; onu hızla arar. Güneşi ve ayı ve yıldızları O'nun emriyle boyun eğdirilmiş olarak yarattı. Bilin ki yaratma ve emir O'nundur. Âlemlerin Rabbi Allah ne yücedir.",
 55: "Rabbinize yalvararak ve gizlice dua edin. Gerçekten O haddi aşanları sevmez.",
 56: "Yeryüzünde onun ıslahından sonra bozgunculuk yapmayın. O'na korkarak ve umarak dua edin. Gerçekten Allah'ın rahmeti iyilik edenlere yakındır.",
}

T = {}
T[54] = ("muhatap 2MP eki (adsız; 'rabbekumu' — 2. kelime); 'xalaqa', 'stevâ' 3MS (adsız; gönderge 'llezî' 4. kelime — 5. ve 12. kelime); 'yuğşi' 3MS (adsız; gönderge 'llâhu' 3. kelime, 15. kelime); "
         "'yatlubuhû' 3MS (adsız; tartışmalı; gönderge 'l-leyle' 16. kelime, 18. kelime); 'yatlubuhû' 3MS eki (adsız; tartışmalı; gönderge 7:54 17. kelime, 18. kelime); "
         "'bi-emrihî', 'lehu' 3MS eki (adsız; gönderge 'llâhu' 3. kelime — 24. ve 26. kelime); 'tebâraka' 3MS (fiil uyumu; 29. kelime — fail 30. kelime)")
T[55] = ("muhatap 2MP (adsız; 'ud'û' — 1. kelime); muhatap 2MP eki (adsız; 'rabbekum' — 2. kelime); 'innehû' 3MS eki (adsız; gönderge 'rabbekum' 2. kelime, 5. kelime); 'yuhibbu' 3MS (adsız; gönderge 'rabbekum' 2. kelime, 7. kelime)")
T[56] = ("muhatap 2MP (adsız; 'tufsidû', 've'd'ûhu' — 2. ve 7. kelime); 'islâhihâ' 3FS eki (adsız; gönderge 'l-ardi' 4. kelime, 6. kelime); 've'd'ûhu' 3MS eki (adsız; gönderge 7:55 2. kelime, 7. kelime)")

D = {}
D[54] = ("◇ 'inne rabbekumu'llâhu'llezî xalaqa's-semâvâti ve'l-arda fî sitteti eyyâmin summe'stevâ 'ale'l-'arşi yuğşi'l-leyle'n-nehâra yatlubuhû hasîsen ve'ş-şemse ve'l-qamera ve'n-nucûme musaxxarâtin bi-emrihî elâ lehu'l-xalqu ve'l-emru tebâraka'llâhu rabbu'l-'âlemîn' — "
 "'inne' + 'rabb' + 2MP + 'allâh' + 'ellezî' + PERF 3MS I. bab + belirli çoğul 'semâ'' + 've' + belirli 'ard' + 'fî' + 'sitte' + nekre çoğul 'yevm' + 'summe' + PERF 3MS VIII. bab + ''alâ' + belirli ''arş' + IMPF 3MS IV. bab + belirli 'leyl' + belirli 'nehâr' + IMPF 3MS I. bab + 3MS + nekre 'hasîs' + "
 "'ve' + belirli 'şems' + 've' + belirli 'qamer' + 've' + belirli çoğul 'necm' + nekre çoğul edilgen ortaç 'musaxxare' + 'bi' + 'emr' + 3MS + 'elâ' + 'li' + 3MS + belirli 'xalq' + 've' + belirli 'emr' + PERF 3MS VI. bab + 'allâh' + 'rabb' + belirli çoğul ''âlem' "
 "(ölçüm edim haber, kip yok; 2MP 1 · 3MS 8; bab I. bab ×2 · IV. bab ×1 · VI. bab ×1 · VIII. bab ×1). "
 "Allah lafzı 3. ve 30. sırada (ölçüm allah z=0,72); Rab 2. ve 31. sırada (ölçüm rab z=1,01); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{1|yıldız ★★★}}' — satır aynen (kaynak hapaks, z=3,28); ölçüm '{{1|" + _HP + "}}' — satır aynen (yeni kök karşılığı 'hızla'); n=32 (n z=2,08); ölçüm '{{1|fâsıla " + _F[0] + " → ن, N sınıfı}}' — satır aynen (7:53 ن → 7:54 ن); "
 "ölçüm '{{1|simetri \\[3, 4, 26, 1\\]}}' — satır aynen; ölçüm '{{1|harf 147 → harf3 140, isaret 7}}' — satır aynen; ölçüm '{{1|dış düğüm 5}}' — satır aynen. "
 "Ölçüm kip yok; ölçüm biçim DIKKAT; "
 "'llezî' (4.) REL; 've'l-arda' (7.) kelimesindeki 've' CONJ; 'summe' (11.) CONJ; 've'ş-şemse' (20.) kelimesindeki 've' CONJ; 've'l-qamera' (21.) kelimesindeki 've' CONJ; 've'n-nucûme' (22.) kelimesindeki 've' CONJ; 'elâ' (25.) ATT; 've'l-emru' (28.) kelimesindeki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 ('llâhu' 3. / 'llâhu' 30. kelime); أمر ×2 ('bi-emrihî' 24. / 've'l-emru' 28. kelime); خلق ×2 ('xalaqa' 5. / 'l-xalqu' 27. kelime); ربب ×2 ('rabbekumu' 2. / 'rabbu' 31. kelime) (okuma). "
 + T[54] + " (okuma). "
 + cumle(say('say 7:54 1-14', "inne rabbekumu'llâhu'llezî xalaqa's-semâvâti ve'l-arda fî sitteti eyyâmin summe'stevâ 'ale'l-'arşi", True), say('dizi 7 54 1 14', "inne rabb allâh ellezî xalaqa semâ' ard fî sitte yevm summe istevâ 'alâ 'arş")) + ' '
 + cumle(say('say 7:54 15-17', "yuğşi'l-leyle'n-nehâra", True), say('dizi 7 54 15 17', "uğşiyet leyl nehâr"), say('say 7:54 18-19', "yatlubuhû hasîsen")) + ' '
 + cumle(say('say 7:54 20-24', "ve'ş-şemse ve'l-qamera ve'n-nucûme musaxxarâtin bi-emrihî", True), say('dizi 7 54 20 24', "şems qamer necm musaxxare emr"), say('say 7:54 20-22', "ve'ş-şemse ve'l-qamera ve'n-nucûme"), say('dizi 7 54 20 22', "şems qamer necm")) + ' '
 + cumle(say('say 7:54 25-28', "elâ lehu'l-xalqu ve'l-emru", True), say('say 7:54 30-32', "llâhu rabbu'l-'âlemîn")) + ' ' +
 "Ölçüm xref 10:3 (emsal olarak basıldı), 13:3 (emsal olarak basıldı), 16:12 (emsal olarak basıldı), 22:18 (emsal olarak basıldı), okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıbı yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'l-leyle' / 'n-nehâra' — ayetler arası: yok.",
 "◈K — K1 's-semâvâti' (6. kelime), 'l-arda' (7. kelime), 'l-leyle' (16. kelime), 'n-nehâra' (17. kelime), 'ş-şemse' (20. kelime), 'l-qamera' (21. kelime), 'n-nucûme' (22. kelime); K2 'eyyâmin' (10. kelime).",
 "◈B — B2 'xalaqa' (5. kelime), 'l-xalqu' (27. kelime).",
 "◈D — D1 'inne' + izafet + lafız + 'ellezî' + PERF + belirli + 've' + belirli + 'fî' + izafet + nekre + 'summe' + PERF + ''alâ' + belirli + IMPF + belirli + belirli + IMPF + nekre + 've' + belirli + 've' + belirli + 've' + belirli + nekre + 'bi' + izafet + 'elâ' + 'li' + belirli + 've' + belirli + PERF + lafız + izafet + belirli; "
 "D2 haber; kip yok; D3 10:3 eşi, 13:3 eşi, 16:12 eşi, 22:18 eşi, أله ×2, أمر ×2, خلق ×2, ربب ×2; D4 2MP 1 · 3MS 8, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[54] + "; aktör yok (ölçüm); A2 Rabbin gökleri ve yeri altı günde yaratıp arşa istivâ eden Allah oluşu; gecenin gündüze bürünüşü ve onu hızla arayışı; güneş, ay ve yıldızların O'nun emriyle boyun eğdirilmiş oluşu; yaratma ve emrin O'na aidiyeti; âlemlerin Rabbinin yüceliği; "
 "A3 —; "
 "A4 " + BOLUM + "; bölüm açılışı; şahıs geçişi yok (ayetler arası); edim geçişi soru → haber (ayetler arası).",
)

D[55] = ("◇ 'ud'û rabbekum tadarru'an ve xufyeten innehû lâ yuhibbu'l-mu'tedîn' — "
 "IMPV 2MP I. bab + 'rabb' + 2MP + nekre mastar 'tadarru'' + 've' + nekre 'xufye' + 'inne' + 3MS + 'lâ' + IMPF 3MS IV. bab + belirli çoğul etken ortaç 'mu'tedî' "
 "(ölçüm edim emir, kip IMPV 1 · NEG 1; 2MP 3 · 3MS 2; bab I. bab ×1 · IV. bab ×1). "
 "Allah lafzı yok; Rab 2. sırada (ölçüm rab z=2,34); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{2|yıldız ★★}}' — satır aynen (kaynak rab, z=2,34); n=8 (n z=-0,47); ölçüm '{{2|fâsıla " + _F[1] + " → ن, N sınıfı}}' — satır aynen (7:54 ن → 7:55 ن); "
 "ölçüm '{{2|harf 39 → harf3 35, isaret 4}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm IMPV 1: 'ud'û' (1. kelime); NEG 1: 'lâ' (6. kelime); "
 "'ve xufyeten' (4.) kelimesindeki 've' CONJ (okuma). "
 + T[55] + " (okuma). "
 + cumle(say('say 7:55 1-4', "ud'û rabbekum tadarru'an ve xufyeten", True), say('say 7:55 1-2', "ud'û rabbekum"), say('say 7:55 3-4', "tadarru'an ve xufyeten")) + ' '
 + cumle(say('say 7:55 5-8', "innehû lâ yuhibbu'l-mu'tedîn", True), say('say 7:55 5-7', "innehû lâ yuhibbu"), say('dizi 7 55 5 7', "inne lâ ahbeb"), say('say 7:55 6-8', "lâ yuhibbu'l-mu'tedîn")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: 'inne lâ ahbeb' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPV + izafet + nekre + 've' + nekre + 'inne' + 'lâ' + IMPF + belirli; "
 "D2 emir; IMPV ('ud'û' 1. kelime), NEG ('lâ' 6. kelime); D3 —; D4 2MP 3 · 3MS 2, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[55] + "; aktör yok (ölçüm); A2 Rabbe yalvararak ve gizlice duaya çağrı; Rabbin haddi aşanları sevmeyişi; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 3 → 2 (ayetler arası); edim geçişi haber → emir (ayetler arası).",
)

D[56] = ("◇ 've lâ tufsidû fi'l-ardi ba'de islâhihâ ve'd'ûhu xavfen ve tama'an inne rahmeta'llâhi qarîbun mine'l-muhsinîn' — "
 "'ve' + 'lâ' + IMPF 2MP IV. bab + 'fî' + belirli 'ard' + 'ba'd' + mastar 'islâh' + 3FS + 've' + IMPV 2MP I. bab + 3MS + nekre 'xavf' + 've' + nekre 'tama'' + 'inne' + 'rahme' + 'allâh' + nekre 'qarîb' + 'min' + belirli çoğul etken ortaç 'muhsin' "
 "(ölçüm edim emir, yasak, kip IMPV 1 · PRO 1; 2MP 4 · 3FS 1 · 3MS 1; bab I. bab ×1 · IV. bab ×1). "
 "Allah lafzı 12. sırada (ölçüm allah z=0,81); Rab yok; ölçüm '{{3|esmâ قَرِيب 13. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton cemâl' (uyuşmuyor) — esma_el kaydı 'degil' — 'rahmeta'llâhi qarîbun', kural 'esmâ adı esmâ dışı göndergeyle → degil' (rahmetin yakınlığı) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=15 (n z=0,27); ölçüm '{{3|fâsıla " + _F[2] + " → ن, N sınıfı}}' — satır aynen (7:55 ن → 7:56 ن); "
 "ölçüm '{{3|harf 68 → harf3 64, isaret 4}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm IMPV 1: 've'd'ûhu' (7. kelime); PRO 1: 'lâ' (1. kelime); ölçüm biçim NEHY; "
 "'ve lâ' (1.) kelimesindeki 've' CONJ; 've'd'ûhu' (7.) kelimesindeki 've' CONJ; 've tama'an' (9.) kelimesindeki 've' CONJ (okuma). "
 + T[56] + " (okuma). "
 + cumle(say('say 7:56 1-6', "ve lâ tufsidû fi'l-ardi ba'de islâhihâ", True), say('dizi 7 56 1 6', "lâ efsedu fî ard ba'd islâh"), say('say 7:56 2-4', "tufsidû fi'l-ardi"), say('dizi 7 56 2 4', "efsedu fî ard")) + ' '
 + cumle(say('say 7:56 7-9', "ve'd'ûhu xavfen ve tama'an", True), say('say 7:56 8-9', "xavfen ve tama'an")) + ' '
 + cumle(say('say 7:56 10-15', "inne rahmeta'llâhi qarîbun mine'l-muhsinîn", True), say('say 7:56 11-12', "rahmeta'llâhi"), say('say 7:56 14-15', "mine'l-muhsinîn")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: 'lâ efsedu fî ard ba'd islâh' süzgeç GEÇER; 'efsedu fî ard' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'xavfen' / 'tama'an' — ayetler arası: yok.",
 "◈K — K1 'l-ardi' (4. kelime).",
 "◈B — —",
 "◈D — D1 've' + 'lâ' + IMPF + 'fî' + belirli + 'ba'd' + izafet + 've' + IMPV + nekre + 've' + nekre + 'inne' + izafet + lafız + nekre + 'min' + belirli; "
 "D2 emir, yasak; IMPV ('ve'd'ûhu' 7. kelime), PRO ('lâ' 1. kelime); D3 —; D4 2MP 4 · 3FS 1 · 3MS 1, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[56] + "; aktör yok (ölçüm); A2 yeryüzünde ıslahından sonra bozgunculuk yasağı; korku ve umutla duaya çağrı; Allah'ın rahmetinin iyilik edenlere yakınlığı; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi emir → emir, yasak (ayetler arası).",
)
out = ['# ── blok 7:54-56 (2026-11-26) ──', 'MEAL16 = {']
for n in range(54, 57):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M16 = {']
for n in range(54, 57):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL16); M.update(M16)']
open('/home/claude/yamalar/metin_7_54_56.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

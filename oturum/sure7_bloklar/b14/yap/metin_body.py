# sûre 7 blok 14 (7:48-51) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os, re
os.environ['SAY2'] = '/home/claude/b14/say2.txt'
os.environ['OLC'] = '/home/claude/b14/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Cennet ehli, ateş ehli ve A'râf'takiler' bölümünde"
_OL = [l.replace('**', '') for l in open(os.environ['OLC'], encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK2 = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[1]).group(0))
_AK3 = _esc(re.search(r'aktör: adlı .*?rol mecrur\)', _OL[2]).group(0))


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 48: "A'râf halkı simalarından tanıdıkları adamlara seslendi; dediler ki: Topluluğunuz ve büyüklenmekte olduklarınız size fayda vermedi.",
 49: "Allah onlara bir rahmetle erişmez diye yemin ettikleriniz bunlar mı? Bahçeye girin; size korku yoktur ve siz üzülmezsiniz.",
 50: "Ateşin halkı bahçenin halkına seslendi ki: Bize sudan ya da Allah'ın size rızık olarak verdiklerinden akıtın. Dediler ki: Gerçekten Allah bunları kâfirlere haram kıldı.",
 51: "Onlar dinlerini oyalanma ve oyun edinen ve dünya hayatının aldattığı kimselerdir. Artık bugün, bu günlerine kavuşmayı unuttukları ve âyetlerimizi bile bile inkâr etmekte oldukları gibi biz de onları unuturuz.",
}

T = {}
T[48] = ("'ve nâdâ' 3MS (fiil uyumu; 1. kelime — fail 2. kelime); 'ya'rifûnehum' 3MP (adsız; gönderge 'ashâbu' 2. kelime, 5. kelime); 'ya'rifûnehum', 'bi-sîmâhum' 3MP eki (adsız; gönderge 'ricâlen' 4. kelime — 5. ve 6. kelime); 'qâlû' 3MP (adsız; gönderge 'ashâbu' 2. kelime, 7. kelime); "
         "'ağnâ' 3MS (fiil uyumu; söz içi; 9. kelime — fail 11. kelime); muhatap 2MP eki (adsız; söz içi; ''ankum', 'cem'ukum' — 10. ve 11. kelime); muhatap 2MP (adsız; söz içi; 'kuntum', 'testekbirûn' — 13. ve 14. kelime)")
T[49] = ("muhatap 2MP (adsız; söz içi; 'aqsamtum' — 3. kelime); 'yenâluhumu' 3MS (fiil uyumu; söz içi; 5. kelime — fail 6. kelime); 'yenâluhumu' 3MP eki (adsız; söz içi; gönderge 'e-hâ'ulâ'i' 1. kelime, 5. kelime); "
         "muhatap 2MP (adsız; söz içi; 'udxulu', 'tahzenûn' — 8. ve 15. kelime); muhatap 2MP eki (adsız; söz içi; ''aleykum' — 12. kelime); muhatap 2MP (adsız; söz içi; 'entum' — 14. kelime)")
T[50] = ("'ve nâdâ' 3MS (fiil uyumu; 1. kelime — fail 2. kelime); muhatap 2MP (adsız; söz içi; 'efîdû' — 7. kelime); konuşan 1P eki (adsız; söz içi; ''aleynâ' — 8. kelime); 'razaqakumu' 3MS (fiil uyumu; söz içi; 13. kelime — fail 14. kelime); "
         "muhatap 2MP eki (adsız; söz içi; 'razaqakumu' — 13. kelime); 'qâlû' 3MP (adsız; gönderge 'ashâbe' 4. kelime, 15. kelime); 'harramehumâ' 3MS (adsız; söz içi; gönderge 'llâhe' 17. kelime, 18. kelime); "
         "'harramehumâ' 3D eki (adsız; söz içi; tartışmalı; gönderge 'l-mâ'i' 10. kelime, 18. kelime)")
T[51] = ("'ttexazû' 3MP (adsız; gönderge 7:50 20. kelime, 2. kelime); 'dînehum' 3MP eki (adsız; gönderge 7:50 20. kelime, 3. kelime); 've ğarrathumu' 3FS (fiil uyumu; 6. kelime — fail 7. kelime); 've ğarrathumu' 3MP eki (adsız; gönderge 7:50 20. kelime, 6. kelime); "
         "konuşan 1P (adsız; 'nensâhum' — 10. kelime); 'nensâhum', 'yevmihim' 3MP eki (adsız; gönderge 7:50 20. kelime — 10. ve 14. kelime); 'nesû', 'kânû', 'yechadûn' 3MP (adsız; gönderge 7:50 20. kelime — 12., 17. ve 19. kelime); konuşan 1P eki (adsız; 'bi-âyâtinâ' — 18. kelime)")

D = {}
D[48] = ("◇ 've nâdâ ashâbu'l-a'râfi ricâlen ya'rifûnehum bi-sîmâhum qâlû mâ ağnâ 'ankum cem'ukum ve mâ kuntum testekbirûn' — "
 "'ve' + PERF 3MS III. bab + 'ashâb' + belirli çoğul 'a'râf' + nekre çoğul 'ricâl' + IMPF 3MP I. bab + 3MP + 'bi' + 'sîmâ' + 3MP + PERF 3MP I. bab + 'mâ' + PERF 3MS I. bab + ''an' + 2MP + 'cem'' + 2MP + 've' + 'mâ' + PERF 2MP I. bab + IMPF 2MP X. bab "
 "(ölçüm edim haber, kip NEG 1; 2MP 6 · 3MP 6 · 3MS 2; bab I. bab ×4 · III. bab ×1 · X. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok (ölçüm); ölçüm adlı aktör yok; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=14 (n z=0,17); ölçüm '{{1|fâsıla " + _F[0] + " → ن, N sınıfı}}' — satır aynen (7:47 ن → 7:48 ن); "
 "ölçüm '{{1|harf 73 → harf3 71, isaret 2}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen. "
 "Ölçüm NEG 1: 'mâ' (8. kelime); "
 "'ve nâdâ' (1.) kelimesindeki 've' CONJ; 've mâ' (12.) CONJ + REL (okuma). "
 "Kök ikilemesi (ölçüm) عرف ×2 ('l-a'râfi' 3. / 'ya'rifûnehum' 5. kelime) (okuma). "
 + T[48] + " (okuma). "
 + cumle(say('say 7:48 1-6', "ve nâdâ ashâbu'l-a'râfi ricâlen ya'rifûnehum bi-sîmâhum", True), say('say 7:48 1-2', "ve nâdâ ashâbu"), say('dizi 7 48 1 2', "nâdâ ashâb"), say('say 7:48 3-5', "l-a'râfi ricâlen ya'rifûnehum"), say('dizi 7 48 3 5', "a'râf ricâl 'arafe")) + ' '
 + cumle(say('say 7:48 8-14', "mâ ağnâ 'ankum cem'ukum ve mâ kuntum testekbirûn", True), say('say 7:48 13-14', "kuntum testekbirûn")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: 'a'râf ricâl 'arafe' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + PERF + izafet + belirli + nekre + IMPF + 'bi' + izafet + PERF + 'mâ' + PERF + ''an' + izafet + 've' + 'mâ' + PERF + IMPF; "
 "D2 haber; NEG ('mâ' 8. kelime); D3 عرف ×2; D4 2MP 6 · 3MP 6 · 3MS 2, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[48] + "; aktör yok (ölçüm adlı aktör yok); A2 A'râf halkının simalarından tanıdıkları adamlara seslenişi; topluluklarının ve büyüklenmelerinin fayda vermeyişi; "
 "A3 'mâ ağnâ 'ankum cem'ukum ve mâ kuntum testekbirûn' (söz içi, 8-14. kelime; ayet sonunda kapanmıyor); "
 "A4 " + BOLUM + "; söz açılır (8. kelime); şahıs geçişi yok (ayetler arası); edim geçişi yasak → haber (ayetler arası).",
)

D[49] = ("◇ 'e-hâ'ulâ'i'llezîne aqsamtum lâ yenâluhumu'llâhu bi-rahmetin udxulu'l-cennete lâ xavfun 'aleykum ve lâ entum tahzenûn' — "
 "'e' + 'hâ' + 'ulâ'i' + 'ellezî' + PERF 2MP IV. bab + 'lâ' + IMPF 3MS I. bab + 3MP + 'allâh' + 'bi' + nekre 'rahme' + IMPV 2MP I. bab + belirli 'cenne' + 'lâ' + nekre 'xavf' + ''alâ' + 2MP + 've' + 'lâ' + 'entum' + IMPF 2MP I. bab "
 "(ölçüm edim soru, emir, kip IMPV 1 · INTG 1 · NEG 3; 2MP 8 · 3MP 1 · 3MS 1; bab I. bab ×3 · IV. bab ×1). "
 "Allah lafzı 6. sırada (ölçüm allah z=0,81); Rab yok; esmâ yok (ölçüm); ölçüm '{{2|" + _AK2 + "}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=15 (n z=0,27); ölçüm '{{2|fâsıla " + _F[1] + " → ن, N sınıfı}}' — satır aynen (7:48 ن → 7:49 ن); "
 "ölçüm '{{2|simetri \\[3, 1, 12, 1\\]}}' — satır aynen; ölçüm '{{2|harf 70 → harf3 68, isaret 2}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm IMPV 1: 'udxulu' (8. kelime); INTG 1: 'e-hâ'ulâ'i' (1. kelime; 'e'); NEG 3: 'lâ' (4. kelime), 'lâ' (10. kelime), 've lâ' (13. kelime; 'lâ'); ölçüm biçim DIKKAT + QASEM; "
 "'e-hâ'ulâ'i' (1.) INTG + ATT + DEM; 'llezîne' (2.) REL; 've lâ' (13.) kelimesindeki 've' CONJ (okuma). "
 + T[49] + " (okuma). "
 + cumle(say('say 7:49 1-7', "e-hâ'ulâ'i'llezîne aqsamtum lâ yenâluhumu'llâhu bi-rahmetin", True), say('say 7:49 8-9', "udxulu'l-cennete")) + ' '
 + cumle(say('say 7:49 10-12', "lâ xavfun 'aleykum", True), say('say 7:49 13-15', "ve lâ entum tahzenûn")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'e' + 'hâ' + 'ulâ'i' + 'ellezî' + PERF + 'lâ' + IMPF + lafız + 'bi' + nekre + IMPV + belirli + 'lâ' + nekre + ''alâ' + 've' + 'lâ' + 'entum' + IMPF; "
 "D2 soru, emir; IMPV ('udxulu' 8. kelime), INTG ('e-hâ'ulâ'i' 1. kelime), NEG ('lâ' 4. kelime, 'lâ' 10. kelime, 've lâ' 13. kelime); D3 —; D4 2MP 8 · 3MP 1 · 3MS 1, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[49] + "; aktör adlı 'l-cennete' (9. kelime; ölçüm rol meful); A2 rahmete erişmeyecekleri yeminiyle anılanların gösterilişi; bahçeye girme emri; korku ve üzüntü olmayışı; "
 "A3 söz sürüyor (7:48 8. kelimeden, 1-15. kelime); "
 "A4 " + BOLUM + "; söz kapanır (15. kelime); şahıs geçişi 3 → 2 (ayetler arası); edim geçişi haber → soru, emir (ayetler arası).",
)

D[50] = ("◇ 've nâdâ ashâbu'n-nâri ashâbe'l-cenneti en efîdû 'aleynâ mine'l-mâ'i ev mimmâ razaqakumu'llâhu qâlû inne'llâhe harramehumâ 'ale'l-kâfirîn' — "
 "'ve' + PERF 3MS III. bab + 'ashâb' + belirli 'nâr' + 'ashâb' + belirli 'cenne' + 'en' + IMPV 2MP IV. bab + ''alâ' + 1P + 'min' + belirli 'mâ'' + 'ev' + 'min' + 'mâ' + PERF 3MS I. bab + 2MP + 'allâh' + PERF 3MP I. bab + 'inne' + 'allâh' + PERF 3MS II. bab + 3D + ''alâ' + belirli çoğul etken ortaç 'kâfir' "
 "(ölçüm edim emir, kip IMPV 1; 1P 1 · 2MP 3 · 3D 1 · 3MP 2 · 3MS 3; bab I. bab ×2 · II. bab ×1 · III. bab ×1 · IV. bab ×1). "
 "Allah lafzı 14. ve 17. sırada (ölçüm allah z=1,47); Rab yok; esmâ yok (ölçüm); ölçüm '{{3|" + _AK3 + "}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=20 (n z=0,81); ölçüm '{{3|fâsıla " + _F[2] + " → ن, N sınıfı}}' — satır aynen (7:49 ن → 7:50 ن); "
 "ölçüm '{{3|simetri \\[3, 6, 9, 1\\]}}' — satır aynen; ölçüm '{{3|harf 87 → harf3 84, isaret 3}}' — satır aynen; ölçüm '{{3|dış düğüm 3}}' — satır aynen. "
 "Ölçüm IMPV 1: 'efîdû' (7. kelime); "
 "'ve nâdâ' (1.) kelimesindeki 've' CONJ; 'en' (6.) INT; 'ev' (11.) CONJ; 'mimmâ' (12.) P + REL; 'inne' (16.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 ('llâhu' 14. / 'llâhe' 17. kelime); صحب ×2 ('ashâbu' 2. / 'ashâbe' 4. kelime) (okuma). "
 + T[50] + " (okuma). "
 + cumle(say('say 7:50 1-6', "ve nâdâ ashâbu'n-nâri ashâbe'l-cenneti en", True), say('say 7:50 1-2', "ve nâdâ ashâbu"), say('dizi 7 50 1 2', "nâdâ ashâb"), say('say 7:50 2-3', "ashâbu'n-nâri"), say('say 7:50 4-5', "ashâbe'l-cenneti"), say('say 7:50 4-6', "ashâbe'l-cenneti en"), say('dizi 7 50 4 6', "ashâb cenne en")) + ' '
 + cumle(say('say 7:50 7-14', "efîdû 'aleynâ mine'l-mâ'i ev mimmâ razaqakumu'llâhu", True), say('say 7:50 12-14', "mimmâ razaqakumu'llâhu"), say('say 7:50 13-14', "razaqakumu'llâhu")) + ' '
 + cumle(say('say 7:50 16-20', "inne'llâhe harramehumâ 'ale'l-kâfirîn", True), say('say 7:50 15-17', "qâlû inne'llâhe"), say('dizi 7 50 15 17', "qâle inne allâh")) + ' ' +
 "Ölçüm xref 36:47 (emsal olarak basıldı), okunmuş 2 ayet. "
 "Ölçüm nakarat3 kalıbı: 'qâle inne allâh' süzgeç GEÇMEZ; 'ashâb cenne en' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K1 'l-mâ'i' (10. kelime).",
 "◈B — —",
 "◈D — D1 've' + PERF + izafet + belirli + izafet + belirli + 'en' + IMPV + ''alâ' + 'min' + belirli + 'ev' + 'min' + 'mâ' + PERF + lafız + PERF + 'inne' + lafız + PERF + ''alâ' + belirli; "
 "D2 emir; IMPV ('efîdû' 7. kelime); D3 36:47 eşi, أله ×2, صحب ×2; D4 1P 1 · 2MP 3 · 3D 1 · 3MP 2 · 3MS 3, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[50] + "; aktör adlı 'l-cenneti' (5. kelime; ölçüm rol mecrur); A2 ateş halkının bahçe halkından su ve rızık isteyişi; Allah'ın bunları kâfirlere haram kıldığı cevabı; "
 "A3 'efîdû 'aleynâ mine'l-mâ'i ev mimmâ razaqakumu'llâhu' (söz biçimli içerik, 7-14. kelime); 'inne'llâhe harramehumâ 'ale'l-kâfirîn' (söz biçimli içerik, 16-20. kelime); "
 "A4 " + BOLUM + "; şahıs geçişi 2 → 3 (ayetler arası); edim geçişi soru, emir → emir (ayetler arası).",
)

D[51] = ("◇ 'llezîne'ttexazû dînehum lehven ve la'iben ve ğarrathumu'l-hayâtu'd-dunyâ fe'l-yevme nensâhum kemâ nesû liqâ'e yevmihim hâzâ ve mâ kânû bi-âyâtinâ yechadûn' — "
 "'ellezî' + PERF 3MP VIII. bab + 'dîn' + 3MP + nekre 'lehv' + 've' + nekre 'la'ib' + 've' + PERF 3FS I. bab + 3MP + belirli 'hayâ' + belirli 'dunyâ' + 'fe' + belirli 'yevm' + IMPF 1P I. bab + 3MP + 'ke' + 'mâ' + PERF 3MP I. bab + mastar 'liqâ'' + 'yevm' + 3MP + 'hâ' + 'zâ' + 've' + 'mâ' + PERF 3MP I. bab + 'bi' + çoğul 'âye' + 1P + IMPF 3MP I. bab "
 "(ölçüm edim haber, kip yok; 1P 2 · 3FS 1 · 3MP 12; bab I. bab ×5 · VIII. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=19 (n z=0,70); ölçüm '{{4|fâsıla " + _F[3] + " → ن, N sınıfı}}' — satır aynen (7:50 ن → 7:51 ن); "
 "ölçüm '{{4|simetri \\[3, 9, 14, 1\\]}}' — satır aynen; ölçüm '{{4|harf 101 → harf3 95, isaret 6}}' — satır aynen; ölçüm '{{4|dış düğüm 4}}' — satır aynen. "
 "Ölçüm kip yok; ölçüm biçim DIKKAT; "
 "'llezîne' (1.) REL; 've la'iben' (5.) kelimesindeki 've' CONJ; 've ğarrathumu' (6.) kelimesindeki 've' CONJ; 'fe'l-yevme' (9.) kelimesindeki 'fe' REM; 'fe'l-yevme' (9.) T; 'kemâ' (11.) P + SUB; 'hâzâ' (15.) ATT + DEM; 've mâ' (16.) CONJ + REL (okuma). "
 "Kök ikilemesi (ölçüm) نسي ×2 ('nensâhum' 10. / 'nesû' 12. kelime); يوم ×2 ('l-yevme' 9. / 'yevmihim' 14. kelime) (okuma). "
 + T[51] + " (okuma). "
 + cumle(say('say 7:51 1-5', "llezîne'ttexazû dînehum lehven ve la'iben", True), say('say 7:51 2-3', "ttexazû dînehum"), say('say 7:51 6-8', "ve ğarrathumu'l-hayâtu'd-dunyâ")) + ' '
 + cumle(say('say 7:51 10-19', "nensâhum kemâ nesû liqâ'e yevmihim hâzâ ve mâ kânû bi-âyâtinâ yechadûn", True), say('say 7:51 17-19', "kânû bi-âyâtinâ yechadûn"), say('dizi 7 51 17 19', "kâne âye cehadu")) + ' ' +
 "Ölçüm xref 41:28 (emsal olarak basıldı), okunmuş 3 ayet. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K2 'l-yevme' (9. kelime), 'yevmihim' (14. kelime).",
 "◈B — B4 'l-hayâtu' (7. kelime).",
 "◈D — D1 'ellezî' + PERF + izafet + nekre + 've' + nekre + 've' + PERF + belirli + belirli + 'fe' + belirli + IMPF + 'ke' + 'mâ' + PERF + izafet + izafet + 'hâ' + 'zâ' + 've' + 'mâ' + PERF + 'bi' + izafet + IMPF; "
 "D2 haber; kip yok; D3 41:28 eşi, نسي ×2, يوم ×2; D4 1P 2 · 3FS 1 · 3MP 12, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[51] + "; aktör yok (ölçüm); A2 dinlerini oyalanma ve oyun edinenler ve dünya hayatının aldattıkları; günlerine kavuşmayı unutup âyetleri inkâr ettikleri gibi unutuluşları; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi emir → haber (ayetler arası); bölüm kapanışı.",
)
out = ['# ── blok 7:48-51 (2026-11-25) ──', 'MEAL14 = {']
for n in range(48, 52):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M14 = {']
for n in range(48, 52):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL14); M.update(M14)']
open('/home/claude/yamalar/metin_7_48_51.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

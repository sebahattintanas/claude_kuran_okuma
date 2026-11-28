# sûre 7 blok 24 metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os, re
os.environ['SAY2'] = '/home/claude/b24/say2.txt'
os.environ['OLC'] = '/home/claude/b24/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Şuayb ve Medyen' bölümünde"
_OL = [l.replace('**', '') for l in open(os.environ['OLC'], encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK1 = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[0]).group(0))
_AK3 = _esc(re.search(r'aktör: adsız `tâife` 3\. sırada · adsız `tâife` 9\. sırada', _OL[2]).group(0))


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 85: "Medyen'e de kardeşleri Şuayb'ı gönderdik. Dedi ki: Ey kavmim, Allah'a kulluk edin. Sizin O'ndan başka bir ilâhınız yok. Rabbinizden size apaçık bir delil geldi. Öyleyse ölçüyü ve tartıyı tam yapın; insanların eşyasını eksiltmeyin ve yeryüzünde onun ıslahından sonra bozgunculuk yapmayın. Eğer inananlar iseniz bu sizin için daha hayırlıdır.",
 86: "Her yolda oturmayın tehdit ederek ve O'na iman edeni Allah'ın yolundan alıkoyarak ve onu eğri göstermek isteyerek. Hatırlayın ki az idiniz ve sizi çoğalttı. Bakın bozguncuların sonu nasıl oldu.",
 87: "Eğer içinizden bir topluluk benimle gönderilene iman etmiş, bir topluluk da iman etmemişse, Allah aramızda hükmedinceye kadar sabredin. O hükmedenlerin en hayırlısıdır.",
}

T = {}
T[85] = ("'exâhum' 3MP eki (adsız; gönderge 'medyene' 2. kelime, 3. kelime); 'qâle' 3MS (adsız; gönderge 'şu'ayban' 4. kelime, 5. kelime); konuşan 1S eki (adsız; söz içi; 'qavmi' — 6. kelime); "
         "muhatap 2MP (adsız; söz içi; 'u'budu', 'evfu', 'tebxasu', 'tufsidû', 'kuntum' — 7., 19., 23., 27. ve 36. kelime); muhatap 2MP eki (adsız; söz içi; 'lekum', 'câ'etkum', 'rabbikum', 'lekum' — 10., 15., 18. ve 34. kelime); "
         "'ğayruhû' 3MS eki (adsız; söz içi; gönderge 'llâhe' 8. kelime, 13. kelime); 'câ'etkum' 3FS (fiil uyumu; söz içi; 15. kelime — fail 16. kelime); "
         "'eşyâ'ehum' 3MP eki (adsız; söz içi; gönderge 'n-nâse' 24. kelime, 25. kelime); 'islâhihâ' 3FS eki (adsız; söz içi; gönderge 'l-ardi' 29. kelime, 31. kelime)")
T[86] = ("muhatap 2MP (adsız; söz içi; 'taq'udû', 'tû'idûne', 'tesuddûne', 'tebğûnehâ', 'zkurû', 'kuntum', 'nzurû' — 2., 5., 6., 13., 15., 17. ve 20. kelime); muhatap 2MP eki (adsız; söz içi; 'kesserakum' — 19. kelime); "
         "'âmene' 3MS (adsız; söz içi; gönderge 'men' 10. kelime, 11. kelime); 'bihî' 3MS eki (adsız; söz içi; tartışmalı; gönderge 'llâhi' 9. kelime, 12. kelime); 'tebğûnehâ' 3FS eki (adsız; söz içi; cins uyumsuz, müennes kullanım; gönderge 'sebîli' 8. kelime, 13. kelime); "
         "'kesserakum' 3MS (adsız; söz içi; gönderge 'llâhi' 9. kelime, 19. kelime); 'kâne' 3MS (fiil uyumu; söz içi; 22. kelime — fail 23. kelime; mecazi müennes)")
T[87] = ("'kâne' 3MS (fiil uyumu; söz içi; 2. kelime — fail 3. kelime; cinsiyet farkı — mecazi müennes değil, fiil öne geçmiş); muhatap 2MP eki (adsız; söz içi; 'minkum' — 4. kelime); 'âmenû' 3MP (adsız; söz içi; cins ve sayı uyumsuz — topluluk anlamı; gönderge 'tâ'ifetun' 3. kelime, 5. kelime); "
         "konuşan 1S (adsız; söz içi; edilgen, naib-i faili zamir; 'ursiltu' — 7. kelime); 'bihî' 3MS eki (adsız; söz içi; gönderge 'llezî' 6. kelime, 8. kelime); 'yu'minû' 3MP (adsız; söz içi; cins ve sayı uyumsuz — topluluk anlamı; gönderge 'tâ'ifetun' 9. kelime, 11. kelime); "
         "muhatap 2MP (adsız; söz içi; 'sbirû' — 12. kelime); 'yahkume' 3MS (fiil uyumu; söz içi; 14. kelime — fail 15. kelime); konuşan 1P eki (adsız; söz içi; 'beynenâ' — 16. kelime); 'huve' 3MS zamiri (adsız; söz içi; gönderge 'llâhu' 15. kelime, 17. kelime)")

D = {}
D[85] = ("◇ 've ilâ medyene exâhum şu'ayban qâle yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû qad câ'etkum beyyinetun min rabbikum fe-evfu'l-keyle ve'l-mîzâne ve lâ tebxasu'n-nâse eşyâ'ehum ve lâ tufsidû fi'l-ardi ba'de islâhihâ zâlikum xayrun lekum in kuntum mu'minîn' — "
 "'ve' + 'ilâ' + özel ad 'medyen' + 'ax' + 3MP + özel ad 'şu'ayb' + PERF 3MS I. bab + 'yâ' + 'qavm' + 1S + IMPV 2MP I. bab + 'allâh' + 'mâ' + 'li' + 2MP + 'min' + nekre 'ilâh' + 'ğayr' + 3MS + 'qad' + PERF 3FS I. bab + 2MP + nekre 'beyyine' + 'min' + 'rabb' + 2MP + 'fe' + IMPV 2MP IV. bab + belirli 'keyl' + 've' + belirli 'mîzân' + 've' + 'lâ' + IMPF 2MP I. bab + belirli 'nâs' + 'şey'' + 3MP + 've' + 'lâ' + IMPF 2MP IV. bab + 'fî' + belirli 'ard' + 'ba'd' + 'islâh' + 3FS + 'zâ' + nekre 'xayr' + 'li' + 2MP + 'in' + PERF 2MP I. bab + çoğul etken ortaç 'mu'min' "
 "(ölçüm edim emir, yasak, nida, şart, kip CERT 1 · COND 1 · IMPV 2 · NEG 1 · PRO 2 · VOC 1; 1S 1 · 2MP 14 · 3FS 2 · 3MP 2 · 3MS 2; bab I. bab ×5 · IV. bab ×2). "
 "Allah lafzı 8. sırada (ölçüm allah z=0,01); Rab 18. sırada (ölçüm rab z=0,25); ölçüm '{{1|esmâ مُؤْمِن 37\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET ton cemâl' — ölçüm MÜHÜRSÜZ ile uyuşmuyor (araç tanımı farkı; muhur_el hayır — ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 'in kuntum mu'minîn', kural 'esmâ adı esmâ dışı göndergeyle → degil' (inananların sıfatı) (okuma); ölçüm '{{1|" + _AK1 + "}}' — satır aynen. "
 "Ölçüm '{{1|yıldız ★★}}' — satır aynen (kaynak n, z=2,61); n=37 (n z=2,61); ölçüm '{{1|fâsıla " + _F[0] + " → ن, N sınıfı}}' — satır aynen (7:84 ن → 7:85 ن); "
 "ölçüm '{{1|simetri \\[3, 9, 26, 1\\]}}' — satır aynen; ölçüm '{{1|harf 166 → harf3 154, isaret 12}}' — satır aynen; ölçüm '{{1|dış düğüm 13}}' — satır aynen; ölçüm '{{1|İÇ düğüm 4}}' — satır aynen. "
 "Ölçüm CERT 1: 'qad' (14. kelime); COND 1: 'in' (35. kelime); IMPV 2: 'u'budu' (7. kelime), 'fe-evfu' (19. kelime); NEG 1: 'mâ' (9. kelime); PRO 2: 've lâ' (22. kelime; 'lâ'), 've lâ' (26. kelime; 'lâ'); VOC 1: 'yâ qavmi' (6. kelime; 'yâ'); ölçüm biçim NEHY; "
 "'ve ilâ' (1.) kelimesindeki 've' CONJ; 'fe-evfu' (19.) kelimesindeki 'fe' REM; 've'l-mîzâne' (21.) kelimesindeki 've' CONJ; 've lâ' (22.) kelimesindeki 've' REM; 've lâ' (26.) kelimesindeki 've' CONJ; 'zâlikum' (32.) DEM (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 ('llâhe' 8. / 'ilâhin' 12. kelime) (okuma). "
 + T[85] + " (okuma). "
 + cumle(say('say 7:85 1-4', "ve ilâ medyene exâhum şu'ayban", True), say('dizi 7 85 1 4', "ilâ medyen ax şu'ayb"), say('dizi 7 85 1 8', "ilâ medyen ax şu'ayb qâle qavm 'abede allâh")) + ' '
 + cumle(say('say 7:85 5-13', "qâle yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû", True), say('dizi 7 85 5 13', "qâle qavm 'abede allâh mâ _ min ilâh ğayr"), say('say 7:85 5-18', "qâle yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû qad câ'etkum beyyinetun min rabbikum"), say('dizi 7 85 5 18', "qâle qavm 'abede allâh mâ _ min ilâh ğayr qad câ'e beyyine min rabb")) + ' '
 + cumle(say('say 7:85 7-8', "u'budu'llâhe", True), say('say 7:85 14-18', "qad câ'etkum beyyinetun min rabbikum", True), say('dizi 7 85 14 18', "qad câ'e beyyine min rabb"), say('say 7:85 19-21', "fe-evfu'l-keyle ve'l-mîzâne", True)) + ' '
 + cumle(say('say 7:85 22-25', "ve lâ tebxasu'n-nâse eşyâ'ehum", True), say('dizi 7 85 22 25', "lâ yebxas nâs şey'"), say('dizi 7 85 22 26', "lâ yebxas nâs şey' lâ")) + ' '
 + cumle(say('say 7:85 26-31', "ve lâ tufsidû fi'l-ardi ba'de islâhihâ", True), say('dizi 7 85 26 31', "lâ efsedu fî ard ba'd islâh"), say('say 7:85 27-29', "tufsidû fi'l-ardi"), say('dizi 7 85 27 29', "efsedu fî ard")) + ' '
 + cumle(say('say 7:85 32-37', "zâlikum xayrun lekum in kuntum mu'minîn", True), say('dizi 7 85 33 37', "xayr _ in kâne mu'min"), say('dizi 7 85 34 36', "_ in kâne")) + ' ' +
 "Ölçüm xref 6:152 (basılmış), 6:157 (basılmış), 7:59 (basılmış), 7:65 (basılmış), 7:73 (basılmış), 11:50 (basılmış), 11:61 (basılmış), 11:84 (basılmış), 11:85 (emsal olarak basıldı), 11:86 (emsal olarak basıldı), 23:23 (basılmış), 23:32 (basılmış), 26:183 (emsal olarak basıldı), 29:36 (emsal olarak basıldı), 40:66 (basılmış), okunmuş 1 ayet ve okunmamış 1 ayet (sûre içi 1). "
 "Ölçüm nakarat3 kalıbı: 'qâle qavm 'abede allâh mâ _ min ilâh ğayr qad câ'e beyyine min rabb' süzgeç GEÇER; 'qâle qavm 'abede allâh mâ _ min ilâh ğayr' süzgeç GEÇER; 'lâ efsedu fî ard ba'd islâh' süzgeç GEÇER; 'qad câ'e beyyine min rabb' süzgeç GEÇER; 'efsedu fî ard' süzgeç GEÇER; '_ in kâne' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'tufsidû' / 'islâhihâ' — ayetler arası: yok.",
 "◈K — K1 'l-ardi' (29. kelime).",
 "◈B — B1 'n-nâse' (24. kelime).",
 "◈D — D1 've' + 'ilâ' + özel ad + izafet + özel ad + PERF + 'yâ' + izafet + IMPV + lafız + 'mâ' + 'li' + 'min' + nekre + izafet + 'qad' + PERF + nekre + 'min' + izafet + 'fe' + IMPV + belirli + 've' + belirli + 've' + 'lâ' + IMPF + belirli + izafet + 've' + 'lâ' + IMPF + 'fî' + belirli + izafet + izafet + 'zâ' + nekre + 'li' + 'in' + PERF + çoğul; "
 "D2 emir, yasak, nida, şart; CERT ('qad' 14. kelime), COND ('in' 35. kelime), IMPV ('u'budu' 7. kelime, 'fe-evfu' 19. kelime), NEG ('mâ' 9. kelime), PRO ('ve lâ' 22. kelime, 've lâ' 26. kelime), VOC ('yâ qavmi' 6. kelime); D3 29:36 eşi, 11:85 eşi, 26:183 eşi, 11:86 eşi, أله ×2; D4 1S 1 · 2MP 14 · 3FS 2 · 3MP 2 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[85] + "; aktör adlı 'medyene' (2. kelime; ölçüm rol mecrur), 'şu'ayban' (4. kelime; ölçüm rol meful); A2 Medyen'e kardeşleri Şuayb'ın gönderilişi; Allah'a kulluk çağrısı; Rabden gelen apaçık delil; ölçü ve tartının tam yapılması; eksiltme ve bozgunculuk yasağı; "
 "A3 'yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû qad câ'etkum beyyinetun min rabbikum fe-evfu'l-keyle ve'l-mîzâne ve lâ tebxasu'n-nâse eşyâ'ehum ve lâ tufsidû fi'l-ardi ba'de islâhihâ zâlikum xayrun lekum in kuntum mu'minîn' (söz içi, 6-37. kelime; ayet sonunda kapanmıyor); "
 "A4 " + BOLUM + "; bölüm açılışı; söz açılır (6. kelime); REM sapması 7:85 (19. kelime) — söz içi 'fe', emir cümlesi başı; REM sapması 7:85 (22. kelime) — söz içi 've', yasak cümlesi başı; şart → cevap (ayet içi; COND 'in' 35. kelime: 'in kuntum mu'minîn' / 'zâlikum' (32. kelime) — cevap öne alınmış); şahıs geçişi 1 → 2 (ayetler arası); edim geçişi emir → emir, yasak, nida, şart (ayetler arası).",
)

D[86] = ("◇ 've lâ taq'udû bi-kulli sirâtin tû'idûne ve tesuddûne 'an sebîli'llâhi men âmene bihî ve tebğûnehâ 'ivecen ve'zkurû iz kuntum qalîlen fe-kesserakum ve'nzurû keyfe kâne 'âqibetu'l-mufsidîn' — "
 "'ve' + 'lâ' + IMPF 2MP I. bab + 'bi' + 'kull' + nekre 'sirât' + IMPF 2MP IV. bab + 've' + IMPF 2MP I. bab + ''an' + 'sebîl' + 'allâh' + 'men' + PERF 3MS IV. bab + 'bi' + 3MS + 've' + IMPF 2MP I. bab + 3FS + nekre ''iveç' + 've' + IMPV 2MP I. bab + 'iz' + PERF 2MP I. bab + nekre 'qalîl' + 'fe' + PERF 3MS II. bab + 2MP + 've' + IMPV 2MP I. bab + 'keyfe' + PERF 3MS I. bab + ''âqibe' + belirli çoğul etken ortaç 'mufsid' "
 "(ölçüm edim emir, yasak, kip IMPV 2 · PRO 1; 2MP 15 · 3FS 1 · 3MS 4; bab I. bab ×7 · II. bab ×1 · IV. bab ×2). "
 "Allah lafzı 9. sırada (ölçüm allah z=0,31); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=24 (n z=1,23); ölçüm '{{2|fâsıla " + _F[1] + " → ن, N sınıfı}}' — satır aynen (7:85 ن → 7:86 ن); "
 "ölçüm '{{2|sayı işareti \\S+, \\S+}}' — satır aynen; ölçüm '{{2|harf 115 → harf3 106, isaret 9}}' — satır aynen; ölçüm '{{2|dış düğüm 2}}' — satır aynen; ölçüm '{{2|İÇ düğüm 1}}' — satır aynen. "
 "Ölçüm IMPV 2: 've'zkurû' (15. kelime), 've'nzurû' (20. kelime); PRO 1: 've lâ' (1. kelime; 'lâ'); ölçüm biçim NEHY; "
 "'ve lâ' (1.) kelimesindeki 've' CONJ; 've tesuddûne' (6.) kelimesindeki 've' CONJ; 'men' (10.) REL; 've tebğûnehâ' (13.) kelimesindeki 've' CONJ; 've'zkurû' (15.) kelimesindeki 've' REM; 'iz' (16.) T; 'fe-kesserakum' (19.) kelimesindeki 'fe' CONJ; 've'nzurû' (20.) kelimesindeki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) كون ×2 ('kuntum' 17. / 'kâne' 22. kelime) (okuma). "
 + T[86] + " (okuma). "
 + cumle(say('say 7:86 1-4', "ve lâ taq'udû bi-kulli sirâtin", True), say('say 7:86 6-12', "ve tesuddûne 'an sebîli'llâhi men âmene bihî", True), say('dizi 7 86 6 9', "sadde 'an sebîl allâh"), say('dizi 7 86 6 11', "sadde 'an sebîl allâh men âmene")) + ' '
 + cumle(say('say 7:86 13-14', "ve tebğûnehâ 'ivecen", True), say('say 7:86 15-18', "ve'zkurû iz kuntum qalîlen", True)) + ' '
 + cumle(say('say 7:86 20-24', "ve'nzurû keyfe kâne 'âqibetu'l-mufsidîn", True), say('dizi 7 86 20 24', "nazara keyfe kâne 'âqibe mufsid"), say('dizi 7 86 20 23', "nazara keyfe kâne 'âqibe"), say('dizi 7 86 21 24', "keyfe kâne 'âqibe mufsid")) + ' ' +
 "Ölçüm xref 3:99 (emsal olarak basıldı), 27:14 (emsal olarak basıldı), okunmamış 1 ayet (sûre içi 1). "
 "Ölçüm nakarat3 kalıbı: 'nazara keyfe kâne 'âqibe mufsid' süzgeç GEÇER; 'nazara keyfe kâne 'âqibe' süzgeç GEÇER; 'sadde 'an sebîl allâh' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'qalîlen' / 'fe-kesserakum' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'lâ' + IMPF + 'bi' + 'kull' + nekre + IMPF + 've' + IMPF + ''an' + izafet + lafız + 'men' + PERF + 'bi' + 've' + IMPF + nekre + 've' + IMPV + 'iz' + PERF + nekre + 'fe' + PERF + 've' + IMPV + 'keyfe' + PERF + izafet + belirli; "
 "D2 emir, yasak; IMPV ('ve'zkurû' 15. kelime, 've'nzurû' 20. kelime), PRO ('ve lâ' 1. kelime); D3 3:99 eşi, 27:14 eşi, كون ×2; D4 2MP 15 · 3FS 1 · 3MS 4, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[86] + "; aktör yok (ölçüm); A2 yollarda tehdit ve alıkoyma yasağı; azken çoğaltılışın hatırlatılması; bozguncuların sonuna bakma çağrısı; "
 "A3 've lâ taq'udû bi-kulli sirâtin tû'idûne ve tesuddûne 'an sebîli'llâhi men âmene bihî ve tebğûnehâ 'ivecen ve'zkurû iz kuntum qalîlen fe-kesserakum ve'nzurû keyfe kâne 'âqibetu'l-mufsidîn' (söz sürüyor (7:85 6. kelimeden, 1-24. kelime; ayet sonunda kapanmıyor)); "
 "A4 " + BOLUM + "; REM sapması 7:86 (15. kelime) — söz içi 've', emir cümlesi başı; şahıs geçişi yok (ayetler arası); edim geçişi emir, yasak, nida, şart → emir, yasak (ayetler arası).",
)

D[87] = ("◇ 've in kâne tâ'ifetun minkum âmenû bi'llezî ursiltu bihî ve tâ'ifetun lem yu'minû fe'sbirû hattâ yahkume'llâhu beynenâ ve huve xayru'l-hâkimîn' — "
 "'ve' + 'in' + PERF 3MS I. bab + nekre 'tâ'ife' + 'min' + 2MP + PERF 3MP IV. bab + 'bi' + 'ellezî' + PERF 1S IV. bab edilgen + 'bi' + 3MS + 've' + nekre 'tâ'ife' + 'lem' + IMPF 3MP IV. bab + 'fe' + IMPV 2MP I. bab + 'hattâ' + IMPF 3MS I. bab + 'allâh' + 'beyne' + 1P + 've' + 3MS + 'xayr' + belirli çoğul etken ortaç 'hâkim' "
 "(ölçüm edim emir, şart, kip COND 1 · IMPV 1 · NEG 1; 1P 1 · 1S 2 · 2MP 3 · 3MP 4 · 3MS 4; bab I. bab ×3 · IV. bab ×3). "
 "Allah lafzı 15. sırada (ölçüm allah z=0,52); Rab yok; esmâ yok (ölçüm); ölçüm '{{3|" + _AK3 + "}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=19 (n z=0,70); ölçüm '{{3|fâsıla " + _F[2] + " → ن, N sınıfı}}' — satır aynen (7:86 ن → 7:87 ن); "
 "ölçüm '{{3|EDİLGEN 1/6 fiil, pas z=0,62}}' — satır aynen; ölçüm '{{3|simetri \\[4, 3, 9, 1\\]}}' — satır aynen; ölçüm '{{3|harf 90 → harf3 83, isaret 7}}' — satır aynen; ölçüm '{{3|dış düğüm 1}}' — satır aynen. "
 "Ölçüm COND 1: 've in' (1. kelime; 'in'); IMPV 1: 'fe'sbirû' (12. kelime); NEG 1: 'lem' (10. kelime); 've in' (1.) kelimesindeki 've' REM; 'bi'llezî' (6.) P + REL; 've tâ'ifetun' (9.) kelimesindeki 've' CONJ; 'fe'sbirû' (12.) kelimesindeki 'fe' RSLT; 'beynenâ' (16.) LOC; 've huve' (17.) kelimesindeki 've' REM (okuma). "
 "Kök ikilemesi (ölçüm) أمن ×2 ('âmenû' 5. / 'yu'minû' 11. kelime); حكم ×2 ('yahkume' 14. / 'l-hâkimîn' 19. kelime); طوف ×2 ('tâ'ifetun' 3. / 'tâ'ifetun' 9. kelime) (okuma). "
 + T[87] + " (okuma). "
 + cumle(say('say 7:87 1-8', "ve in kâne tâ'ifetun minkum âmenû bi'llezî ursiltu bihî", True), say('say 7:87 9-11', "ve tâ'ifetun lem yu'minû", True)) + ' '
 + cumle(say('say 7:87 12-16', "fe'sbirû hattâ yahkume'llâhu beynenâ", True), say('dizi 7 87 12 15', "sabera hattâ hakeme allâh"), say('say 7:87 13-15', "hattâ yahkume'llâhu", True), say('say 7:87 17-19', "ve huve xayru'l-hâkimîn", True), say('dizi 7 87 17 19', "_ xayr hâkim")) + ' ' +
 "Ölçüm xref 10:109 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıbı yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'âmenû' / 'lem yu'minû' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'in' + PERF + nekre + 'min' + PERF + 'bi' + 'ellezî' + PERF + 'bi' + 've' + nekre + 'lem' + IMPF + 'fe' + IMPV + 'hattâ' + IMPF + lafız + izafet + 've' + zamir + izafet + belirli; "
 "D2 emir, şart; COND ('ve in' 1. kelime), IMPV ('fe'sbirû' 12. kelime), NEG ('lem' 10. kelime); D3 10:109 eşi, أمن ×2, حكم ×2, طوف ×2; D4 1P 1 · 1S 2 · 2MP 3 · 3MP 4 · 3MS 4, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[87] + "; aktör adsız 'tâ'ifetun' (3. kelime; ölçüm tâife), adsız 'tâ'ifetun' (9. kelime; ölçüm tâife); A2 iman eden ve etmeyen iki topluluk ayrımı; Allah'ın hükmüne kadar sabır çağrısı; hükmedenlerin en hayırlısı nitelemesi; "
 "A3 've in kâne tâ'ifetun minkum âmenû bi'llezî ursiltu bihî ve tâ'ifetun lem yu'minû fe'sbirû hattâ yahkume'llâhu beynenâ ve huve xayru'l-hâkimîn' (söz sürüyor (7:85 6. kelimeden, 1-19. kelime)); "
 "A4 " + BOLUM + "; söz kapanır (19. kelime); REM sapması 7:87 (1. kelime) — söz içi 've', şart cümlesi başı; REM sapması 7:87 (17. kelime) — söz içi 've', isim cümlesi başı; şart → cevap (ayet içi; COND 've in' 1. kelime: 've in kâne tâ'ifetun' / 'fe'sbirû' (12. kelime) — cevap 'fe'si); şahıs geçişi 2 → 3 (ayetler arası); edim geçişi emir, yasak → emir, şart (ayetler arası).",
)
out = ['# ── blok 7:85-87 (2026-11-28) ──', 'MEAL24 = {']
for n in range(85, 88):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M24 = {']
for n in range(85, 88):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL24); M.update(M24)']
open('/home/claude/yamalar/metin_7_85_87.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

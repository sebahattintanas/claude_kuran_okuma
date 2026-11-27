# sûre 7 blok 21 metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os, re
os.environ['SAY2'] = '/home/claude/b21/say2.txt'
os.environ['OLC'] = '/home/claude/b21/olcum.txt'
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
_AK2 = _esc(re.search(r'aktör: adlı .*?rol mecrur\)', _OL[1]).group(0))
_AK3 = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[2]).group(0))
_HP = _esc(re.search(r'HAPAKS: .*? — hapaks z=3,28', _OL[1]).group(0))


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 73: "Semûd'a kardeşleri Sâlih'i gönderdik. Dedi ki: Ey kavmim, Allah'a kulluk edin. Sizin O'ndan başka bir ilâhınız yok. Rabbinizden size apaçık bir delil geldi. İşte Allah'ın bu devesi size bir âyet. Onu bırakın Allah'ın arzında yesin; ona kötülükle dokunmayın, yoksa sizi acı bir azap yakalar.",
 74: "Âd'dan sonra sizi halifeler kıldığı zamanı hatırlayın ve sizi yeryüzüne yerleştirdi. Onun düzlüklerinden köşkler ediniyorsunuz ve dağları evler olarak yontuyorsunuz. Öyleyse Allah'ın nimetlerini hatırlayın ve yeryüzünde bozguncular olarak taşkınlık etmeyin.",
 75: "Kavminden büyüklenen ileri gelenler dedi ki zayıf sayılanlara, onlardan iman edenlere: Sâlih'in Rabbinden gönderilmiş olduğunu biliyor musunuz? Dediler ki: Gerçekten biz onunla gönderilene iman edenleriz.",
}

T = {}
T[73] = ("'exâhum' 3MP eki (adsız; gönderge 'semûde' 2. kelime, 3. kelime); 'qâle' 3MS (adsız; gönderge 'sâlihan' 4. kelime, 5. kelime); konuşan 1S eki (adsız; söz içi; 'qavmi' — 6. kelime); "
         "muhatap 2MP (adsız; söz içi; 'u'budu', 'zerûhâ', 'temessûhâ' — 7., 24. ve 30. kelime); muhatap 2MP eki (adsız; söz içi; 'lekum', 'câ'etkum', 'rabbikum', 'lekum', 'ye'xuzekum' — 10., 15., 18., 22. ve 32. kelime); "
         "'ğayruhû' 3MS eki (adsız; söz içi; gönderge 'llâhe' 8. kelime, 13. kelime); 'câ'etkum' 3FS (fiil uyumu; söz içi; 15. kelime — fail 16. kelime); "
         "'zerûhâ', 'temessûhâ' 3FS eki (adsız; söz içi; gönderge 'nâqatu' 20. kelime — 24. ve 30. kelime); 'te'kul' 3FS (adsız; söz içi; gönderge 'nâqatu' 20. kelime, 25. kelime); 'ye'xuzekum' 3MS (fiil uyumu; söz içi; 32. kelime — fail 33. kelime)")
T[74] = ("muhatap 2MP (adsız; söz içi; 'zkurû', 'tettexizûne', 'tenhitûne', 'zkurû', 'ta'sev' — 1., 11., 15., 18. ve 22. kelime); muhatap 2MP eki (adsız; söz içi; 'ce'alekum', 'bevve'ekum' — 3. ve 8. kelime); "
         "'ce'ale', 'bevve'e' 3MS (adsız; söz içi; gönderge 'llâhi' 20. kelime — 3. ve 8. kelime); 'suhûlihâ' 3FS eki (adsız; söz içi; gönderge 'l-ardi' 10. kelime, 13. kelime)")
T[75] = ("'qâle' 3MS (fiil uyumu; 1. kelime — fail 2. kelime); 'stekberû' 3MP (adsız; gönderge 'llezîne' 3. kelime, 4. kelime); 'qavmihî' 3MS eki (adsız; gönderge 7:73 4. kelime, 6. kelime); "
         "'stud'ifû' 3MP (adsız; edilgen, naib-i faili zamir; gönderge 'llezîne' 7. kelime, 8. kelime); 'âmene' 3MS (adsız; gönderge 'men' 9. kelime, 10. kelime); 'minhum' 3MP eki (adsız; gönderge 'men' 9. kelime, 11. kelime); "
         "muhatap 2MP (adsız; söz içi; 'ta'lemûne' — 12. kelime); 'rabbihî' 3MS eki (adsız; söz içi; gönderge 'sâlihan' 14. kelime, 17. kelime); 'qâlû' 3MP (adsız; gönderge 'llezîne' 7. kelime, 18. kelime); "
         "konuşan 1P eki (adsız; söz içi; 'innâ' — 19. kelime); 'ursile' 3MS (adsız; söz içi; edilgen, naib-i faili zamir; gönderge 'mâ' 20. kelime, 21. kelime); 'bihî' 3MS eki (adsız; söz içi; gönderge 'mâ' 20. kelime, 22. kelime)")

D = {}
D[73] = ("◇ 've ilâ semûde exâhum sâlihan qâle yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû qad câ'etkum beyyinetun min rabbikum hâzihî nâqatu'llâhi lekum âyeten fe-zerûhâ te'kul fî ardi'llâhi ve lâ temessûhâ bi-sû'in fe-ye'xuzekum 'azâbun elîm' — "
 "'ve' + 'ilâ' + özel ad 'semûd' + 'ax' + 3MP + özel ad 'sâlih' + PERF 3MS I. bab + 'yâ' + 'qavm' + 1S + IMPV 2MP I. bab + 'allâh' + 'mâ' + 'li' + 2MP + 'min' + nekre 'ilâh' + 'ğayr' + 3MS + 'qad' + PERF 3FS I. bab + 2MP + nekre 'beyyine' + 'min' + 'rabb' + 2MP + 'hâ' + 'zâ' + 'nâqa' + 'allâh' + 'li' + 2MP + nekre 'âye' + 'fe' + IMPV 2MP I. bab + 3FS + IMPF 3FS I. bab + 'fî' + 'ard' + 'allâh' + 've' + 'lâ' + IMPF 2MP I. bab + 3FS + 'bi' + nekre 'sû'' + 'fe' + IMPF 3MS I. bab + 2MP + nekre ''azâb' + nekre 'elîm' "
 "(ölçüm edim emir, yasak, nida, kip CERT 1 · IMPV 2 · NEG 1 · PRO 1 · VOC 1; 1S 1 · 2MP 11 · 3FS 4 · 3MP 1 · 3MS 3; bab I. bab ×7). "
 "Allah lafzı 8., 21. ve 28. sırada (ölçüm allah z=1,24); Rab 18. sırada (ölçüm rab z=0,30); esmâ yok (ölçüm); ölçüm '{{1|" + _AK1 + "}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{1|yıldız ★★}}' — satır aynen (kaynak n, z=2,29); n=34 (n z=2,29); ölçüm '{{1|fâsıla " + _F[0] + " → م, N sınıfı}}' — satır aynen (7:72 ن → 7:73 م); "
 "ölçüm '{{1|simetri \\[4, 19, 26, 1\\]}}' — satır aynen; ölçüm '{{1|harf 144 → harf3 131, isaret 13}}' — satır aynen; ölçüm '{{1|dış düğüm 10}}' — satır aynen; ölçüm '{{1|İÇ düğüm 4}}' — satır aynen. "
 "Ölçüm CERT 1: 'qad' (14. kelime); IMPV 2: 'u'budu' (7. kelime), 'fe-zerûhâ' (24. kelime); NEG 1: 'mâ' (9. kelime); PRO 1: 've lâ' (29. kelime; 'lâ'); VOC 1: 'yâ qavmi' (6. kelime; 'yâ'); ölçüm biçim DIKKAT + NEHY; "
 "'ve ilâ' (1.) kelimesindeki 've' CONJ; 'hâzihî' (19.) ATT + DEM; 'fe-zerûhâ' (24.) kelimesindeki 'fe' REM; 've lâ' (29.) kelimesindeki 've' CONJ; 'fe-ye'xuzekum' (32.) kelimesindeki 'fe' CAUS (okuma). "
 "Kök ikilemesi (ölçüm) أله ×4 ('llâhe' 8. / 'ilâhin' 12. / 'llâhi' 21. / 'llâhi' 28. kelime) (okuma). "
 + T[73] + " (okuma). "
 + cumle(say('say 7:73 1-4', "ve ilâ semûde exâhum sâlihan", True), say('say 7:73 7-8', "u'budu'llâhe", True)) + ' '
 + cumle(say('say 7:73 5-13', "qâle yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû", True), say('dizi 7 73 5 13', "qâle qavm 'abede allâh mâ _ min ilâh ğayr"), say('say 7:73 5-18', "qâle yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû qad câ'etkum beyyinetun min rabbikum"), say('dizi 7 73 5 18', "qâle qavm 'abede allâh mâ _ min ilâh ğayr qad câ'e beyyine min rabb")) + ' '
 + cumle(say('say 7:73 14-18', "qad câ'etkum beyyinetun min rabbikum", True), say('dizi 7 73 14 18', "qad câ'e beyyine min rabb")) + ' '
 + cumle(say('say 7:73 19-23', "hâzihî nâqatu'llâhi lekum âyeten", True), say('say 7:73 24-28', "fe-zerûhâ te'kul fî ardi'llâhi", True), say('say 7:73 19-28', "hâzihî nâqatu'llâhi lekum âyeten fe-zerûhâ te'kul fî ardi'llâhi"), say('dizi 7 73 19 33', "zâ nâqa allâh _ âye yezere ekele fî ard allâh lâ messe sû' exaze 'azâb"), say('dizi 7 73 29 33', "lâ messe sû' exaze 'azâb")) + ' '
 + cumle(say('say 7:73 29-34', "ve lâ temessûhâ bi-sû'in fe-ye'xuzekum 'azâbun elîm"), say('say 7:73 29-31', "ve lâ temessûhâ bi-sû'in", True), say('say 7:73 32-34', "fe-ye'xuzekum 'azâbun elîm", True)) + ' ' +
 "Ölçüm xref 6:157 (basılmış), 7:59 (basılmış), 7:65 (basılmış), 11:50 (basılmış), 11:61 (basılmış), 11:64 (emsal olarak basıldı), 11:84 (basılmış), 23:23 (basılmış), 23:32 (basılmış), 26:156 (emsal olarak basıldı), 40:66 (basılmış), okunmuş 1 ayet ve okunmamış 2 ayet (sûre içi 2). "
 "Ölçüm nakarat3 kalıbı: 'qâle qavm 'abede allâh mâ _ min ilâh ğayr qad câ'e beyyine min rabb' süzgeç GEÇER; 'qâle qavm 'abede allâh mâ _ min ilâh ğayr' süzgeç GEÇER; 'qad câ'e beyyine min rabb' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K1 'ardi' (27. kelime).",
 "◈B — —",
 "◈D — D1 've' + 'ilâ' + özel ad + izafet + özel ad + PERF + 'yâ' + izafet + IMPV + lafız + 'mâ' + 'li' + 'min' + nekre + izafet + 'qad' + PERF + nekre + 'min' + izafet + 'hâ' + 'zâ' + izafet + lafız + 'li' + nekre + 'fe' + IMPV + IMPF + 'fî' + izafet + lafız + 've' + 'lâ' + IMPF + 'bi' + nekre + 'fe' + IMPF + nekre + nekre; "
 "D2 emir, yasak, nida; CERT ('qad' 14. kelime), IMPV ('u'budu' 7. kelime, 'fe-zerûhâ' 24. kelime), NEG ('mâ' 9. kelime), PRO ('ve lâ' 29. kelime), VOC ('yâ qavmi' 6. kelime); D3 11:64 eşi, 26:156 eşi, أله ×4; D4 1S 1 · 2MP 11 · 3FS 4 · 3MP 1 · 3MS 3, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[73] + "; aktör adlı 'semûde' (2. kelime; ölçüm rol mecrur), 'sâlihan' (4. kelime; ölçüm rol meful); A2 Semûd'a kardeşleri Sâlih'in gönderilişi; Allah'a kulluk çağrısı; Rabden gelen apaçık delil; Allah'ın devesinin âyet oluşu; deveye dokunma yasağı ve azap uyarısı; "
 "A3 'yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû qad câ'etkum beyyinetun min rabbikum hâzihî nâqatu'llâhi lekum âyeten fe-zerûhâ te'kul fî ardi'llâhi ve lâ temessûhâ bi-sû'in fe-ye'xuzekum 'azâbun elîm' (söz içi, 6-34. kelime; ayet sonunda kapanmıyor); "
 "A4 " + BOLUM + "; bölüm açılışı; söz açılır (6. kelime); cevap edatı kapsam dışı (morph CAUS 'fe-ye'xuzekum' 32. kelime — sebebiyye; şart / soru yok); şahıs geçişi 1 → 2 (ayetler arası); edim geçişi haber → emir, yasak, nida (ayetler arası).",
)

D[74] = ("◇ 've'zkurû iz ce'alekum xulefâ'e min ba'di 'âdin ve bevve'ekum fi'l-ardi tettexizûne min suhûlihâ qusûran ve tenhitûne'l-cibâle buyûten fe'zkurû âlâ'e'llâhi ve lâ ta'sev fi'l-ardi mufsidîn' — "
 "'ve' + IMPV 2MP I. bab + 'iz' + PERF 3MS I. bab + 2MP + çoğul 'xalîfe' + 'min' + 'ba'd' + nekre özel ad ''âd' + 've' + PERF 3MS II. bab + 2MP + 'fî' + belirli 'ard' + IMPF 2MP VIII. bab + 'min' + çoğul 'sehl' + 3FS + nekre çoğul 'qasr' + 've' + IMPF 2MP I. bab + belirli çoğul 'cebel' + nekre çoğul 'beyt' + 'fe' + IMPV 2MP I. bab + çoğul 'âlâ'' + 'allâh' + 've' + 'lâ' + IMPF 2MP I. bab + 'fî' + belirli 'ard' + çoğul etken ortaç 'mufsid' "
 "(ölçüm edim emir, yasak, kip IMPV 2 · PRO 1; 2MP 12 · 3FS 1 · 3MS 2; bab I. bab ×5 · II. bab ×1 · VIII. bab ×1). "
 "Allah lafzı 20. sırada (ölçüm allah z=0,27); Rab yok; esmâ yok (ölçüm); ölçüm '{{2|" + _AK2 + "}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{2|yıldız ★★★}}' — satır aynen (kaynak hapaks, z=3,28); ölçüm '{{2|" + _HP + "}}' — satır aynen (yeni kök karşılığı 'düzlük'); n=25 (n z=1,34); ölçüm '{{2|fâsıla " + _F[1] + " → ن, N sınıfı}}' — satır aynen (7:73 م → 7:74 ن); "
 "ölçüm '{{2|simetri \\[3, 9, 23, 1\\]}}' — satır aynen; ölçüm '{{2|harf 122 → harf3 114, isaret 8}}' — satır aynen; ölçüm '{{2|dış düğüm 3}}' — satır aynen. "
 "Ölçüm IMPV 2: 've'zkurû' (1. kelime), 'fe'zkurû' (18. kelime); PRO 1: 've lâ' (21. kelime; 'lâ'); ölçüm biçim NEHY; "
 "'ve'zkurû' (1.) kelimesindeki 've' CONJ; 'iz' (2.) T; 've bevve'ekum' (8.) kelimesindeki 've' CONJ; 've tenhitûne' (15.) kelimesindeki 've' CONJ; 'fe'zkurû' (18.) kelimesindeki 'fe' REM; 've lâ' (21.) kelimesindeki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) أرض ×2 ('l-ardi' 10. / 'l-ardi' 24. kelime); ذكر ×2 ('zkurû' 1. / 'zkurû' 18. kelime) (okuma). "
 + T[74] + " (okuma). "
 + cumle(say('say 7:74 1-7', "ve'zkurû iz ce'alekum xulefâ'e min ba'di 'âdin", True), say('say 7:74 1-6', "ve'zkurû iz ce'alekum xulefâ'e min ba'di"), say('dizi 7 74 1 6', "zekere iz ce'ale xalîfe min ba'd")) + ' '
 + cumle(say('say 7:74 8-10', "ve bevve'ekum fi'l-ardi", True), say('say 7:74 11-14', "tettexizûne min suhûlihâ qusûran", True)) + ' '
 + cumle(say('say 7:74 15-17', "ve tenhitûne'l-cibâle buyûten", True), say('say 7:74 16-17', "l-cibâle buyûten"), say('dizi 7 74 16 17', "cebel beyt")) + ' '
 + cumle(say('say 7:74 18-20', "fe'zkurû âlâ'e'llâhi", True), say('dizi 7 74 18 20', "zekere âlâ' allâh")) + ' '
 + cumle(say('say 7:74 21-25', "ve lâ ta'sev fi'l-ardi mufsidîn", True), say('dizi 7 74 21 25', "lâ ta'se fî ard mufsid"), say('dizi 7 74 20 25', "allâh lâ ta'se fî ard mufsid")) + ' ' +
 "Ölçüm xref 2:60 (emsal olarak basıldı), 15:82 (emsal olarak basıldı), 26:149 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıbı: 'zekere iz ce'ale xalîfe min ba'd' süzgeç GEÇER; 'zekere âlâ' allâh' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K1 'l-ardi' (10. kelime), 'l-cibâle' (16. kelime), 'l-ardi' (24. kelime).",
 "◈B — —",
 "◈D — D1 've' + IMPV + 'iz' + PERF + çoğul + 'min' + izafet + nekre + 've' + PERF + 'fî' + belirli + IMPF + 'min' + izafet + nekre + 've' + IMPF + belirli + nekre + 'fe' + IMPV + izafet + lafız + 've' + 'lâ' + IMPF + 'fî' + belirli + çoğul; "
 "D2 emir, yasak; IMPV ('ve'zkurû' 1. kelime, 'fe'zkurû' 18. kelime), PRO ('ve lâ' 21. kelime); D3 2:60 eşi, 15:82 eşi, 26:149 eşi, أرض ×2, ذكر ×2; D4 2MP 12 · 3FS 1 · 3MS 2, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[74] + "; aktör adlı ''âdin' (7. kelime; ölçüm rol mecrur); A2 Âd'dan sonra halifeler kılınışın hatırlatılması; yeryüzüne yerleştirme; düzlüklerde köşk, dağlarda ev; Allah'ın nimetlerini hatırlama ve bozgunculuk yasağı; "
 "A3 've'zkurû iz ce'alekum xulefâ'e min ba'di 'âdin ve bevve'ekum fi'l-ardi tettexizûne min suhûlihâ qusûran ve tenhitûne'l-cibâle buyûten fe'zkurû âlâ'e'llâhi ve lâ ta'sev fi'l-ardi mufsidîn' (söz sürüyor (7:73 6. kelimeden, 1-25. kelime)); "
 "A4 " + BOLUM + "; söz kapanır (25. kelime); REM sapması 7:74 (18. kelime) — söz içi 'fe', emir cümlesi başı; şahıs geçişi yok (ayetler arası); edim geçişi emir, yasak, nida → emir, yasak (ayetler arası).",
)

D[75] = ("◇ 'qâle'l-mele'u'llezîne'stekberû min qavmihî li'llezîne'stud'ifû li-men âmene minhum e-ta'lemûne enne sâlihan murselun min rabbihî qâlû innâ bi-mâ ursile bihî mu'minûn' — "
 "PERF 3MS I. bab + belirli 'mele'' + 'ellezî' + PERF 3MP X. bab + 'min' + 'qavm' + 3MS + 'li' + 'ellezî' + PERF 3MP X. bab edilgen + 'li' + 'men' + PERF 3MS IV. bab + 'min' + 3MP + 'e' + IMPF 2MP I. bab + 'enne' + özel ad 'sâlih' + nekre edilgen ortaç 'mursel' + 'min' + 'rabb' + 3MS + PERF 3MP I. bab + 'inne' + 1P + 'bi' + 'mâ' + PERF 3MS IV. bab edilgen + 'bi' + 3MS + çoğul etken ortaç 'mu'min' "
 "(ölçüm edim soru, kip INTG 1; 1P 1 · 2MP 2 · 3MP 7 · 3MS 6; bab I. bab ×3 · IV. bab ×2 · X. bab ×2). "
 "Allah lafzı yok; Rab 17. sırada (ölçüm rab z=0,60); ölçüm '{{3|esmâ مُؤْمِن 23\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET ton cemâl' — ölçüm MÜHÜRSÜZ ile uyuşmuyor (araç tanımı farkı; muhur_el hayır — ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 'innâ bi-mâ ursile bihî mu'minûn', kural 'esmâ adı esmâ dışı göndergeyle → degil' (iman edenlerin sıfatı) (okuma); ölçüm '{{3|" + _AK3 + "}}' — satır aynen. "
 "Ölçüm 'yıldız yok' — satır aynen; n=23 (n z=1,12); ölçüm '{{3|fâsıla " + _F[2] + " → ن, N sınıfı}}' — satır aynen (7:74 ن → 7:75 ن); "
 "ölçüm '{{3|EDİLGEN 2/7 fiil, pas z=1,30}}' — satır aynen; ölçüm '{{3|simetri \\[3, 1, 18, 1\\]}}' — satır aynen; ölçüm '{{3|harf 105 → harf3 96, isaret 9}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm INTG 1: 'e-ta'lemûne' (12. kelime; 'e'); 'li'llezîne' (7.) P + REL; 'li-men' (9.) P + REL; 'innâ' (19.) ACC; 'bi-mâ' (20.) P + REL (okuma). "
 "Kök ikilemesi (ölçüm) أمن ×2 ('âmene' 10. / 'mu'minûn' 23. kelime); رسل ×2 ('murselun' 15. / 'ursile' 21. kelime); قول ×2 ('qâle' 1. / 'qâlû' 18. kelime) (okuma). "
 + T[75] + " (okuma). "
 + cumle(say('say 7:75 1-6', "qâle'l-mele'u'llezîne'stekberû min qavmihî", True), say('dizi 7 75 1 6', "qâle mele' ellezî istekbere min qavm"), say('say 7:75 1-3', "qâle'l-mele'u'llezîne"), say('dizi 7 75 1 3', "qâle mele' ellezî")) + ' '
 + cumle(say('say 7:75 7-11', "li'llezîne'stud'ifû li-men âmene minhum"), say('say 7:75 7-8', "li'llezîne'stud'ifû", True), say('say 7:75 9-11', "li-men âmene minhum", True), say('say 7:75 12-17', "e-ta'lemûne enne sâlihan murselun min rabbihî", True), say('say 7:75 18-23', "qâlû innâ bi-mâ ursile bihî mu'minûn", True)) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: 'qâle mele' ellezî istekbere min qavm' süzgeç GEÇER; 'qâle mele' ellezî' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'stekberû' / 'stud'ifû' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 PERF + belirli + 'ellezî' + PERF + 'min' + izafet + 'li' + 'ellezî' + PERF + 'li' + 'men' + PERF + 'min' + 'e' + IMPF + 'enne' + özel ad + nekre + 'min' + izafet + PERF + 'inne' + 'bi' + 'mâ' + PERF + 'bi' + çoğul; "
 "D2 soru; INTG ('e-ta'lemûne' 12. kelime); D3 أمن ×2, رسل ×2, قول ×2; D4 1P 1 · 2MP 2 · 3MP 7 · 3MS 6, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[75] + "; aktör adlı 'sâlihan' (14. kelime; ölçüm rol meful); A2 büyüklenen ileri gelenlerin zayıf sayılan iman edenlere sorusu; Sâlih'in Rabden gönderilmişliği; iman edenlerin cevabı; "
 "A3 'e-ta'lemûne enne sâlihan murselun min rabbihî' (söz içi, 12-17. kelime); 'innâ bi-mâ ursile bihî mu'minûn' (söz içi, 19-23. kelime); "
 "A4 " + BOLUM + "; söz açılır (12. kelime); söz kapanır (17. kelime, ayet içi); söz açılır (19. kelime); söz kapanır (23. kelime, ayet içi); şahıs geçişi 2 → 3 (ayetler arası); edim geçişi emir, yasak → soru (ayetler arası).",
)
out = ['# ── blok 7:73-75 (2026-11-27) ──', 'MEAL21 = {']
for n in range(73, 76):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M21 = {']
for n in range(73, 76):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL21); M.update(M21)']
open('/home/claude/yamalar/metin_7_73_75.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

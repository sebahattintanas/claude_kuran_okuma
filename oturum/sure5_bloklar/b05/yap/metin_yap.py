# blok 5 (5:12-14) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b05/say2.txt'
os.environ['OLC'] = '/home/claude/b05/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'İsrâiloğullarının ve Nasârâ'nın misakı; kitap ehline gelen elçi; Mesih hakkında söz' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 12: "Andolsun Allah İsrâiloğullarından ahit almıştı; içlerinden on iki temsilci göndermiştik. Allah dedi ki: 'Şüphesiz ben sizinle beraberim. Andolsun, eğer namazı kılar, zekâtı verir, elçilerime inanır, onları destekler ve Allah'a güzel bir borç verirseniz, kötülüklerinizi sizden mutlaka örterim ve sizi altlarından ırmaklar akan cennetlere mutlaka sokarım. Bundan sonra sizden kim inkâr ederse, doğru yoldan sapmıştır.'",
 13: "Ahitlerini bozmaları yüzünden onları lanetledik ve kalplerini katı kıldık; kelimeleri yerlerinden saptırıyorlar ve kendilerine hatırlatılandan bir payı unuttular. Onlardan, pek azı dışında, sürekli bir hainliğe vâkıf olursun. Onları affet ve hoş gör. Şüphesiz Allah iyilik edenleri sever.",
 14: "'Biz Nasârâ'yız' diyenlerden de ahitlerini almıştık; onlar da kendilerine hatırlatılandan bir payı unuttular. Bunun üzerine aralarına kıyamet gününe kadar düşmanlık ve öfke saldık. Allah onlara yapmakta olduklarını haber verecek.",
}

T12 = ("Allah (lafız; 'axaza' ve 'qâla' faili; 'eqradtumu' sonrasında mef'ûl, 25. kelime); 'benî isrâ'îl' (adlı kavim; 'mîsâqa' muzâfun ileyhi, 5-6. kelime); konuşan 1P (adsız; 'be'asnâ' — gönderge lafız); "
       "'aşera neqîben' ('be'asnâ' mef'ûlü; nekre, 9-11. kelime); 'minhum' 3MP (gönderge kavim); söz içi konuşan 1S (adsız; 'innî', 'rusulî', 'ukeffiranne', 'udxilennekum' — gönderge lafız); "
       "muhatap 2MP (adsız; 'ma'akum', 'eqamtum', 'âteytum', 'âmentum', ''azzertum', 'eqradtum', ''ankum', 'seyyi'âtikum', 'minkum'); 'rusulî' (elçiler; 22. kelime); ''azzertumûhum' mef'ûlü 3MP (gönderge elçiler); "
       "'cennâtin' (nekre çoğul, 32. kelime); 'tecrî' faili 'l-enhâr' (36. kelime); 'tahtihe' 3FS (gönderge cennetler); 'men' (şart ismi; 'kefera' ve 'dalle' faili 3MS)")
T13 = ("konuşan 1P (adsız; 'le'annâhum', 'ce'alnâ' — gönderge lafız); 'naqdihim', 'mîsâqahum', 'le'annâhum' ve 'qulûbehum' 3MP (adsız — gönderge kavim); 'yuharrifûne' ve 'nesû' faili 3MP (adsız); "
       "'zukkirû' faili (adsız; edilgen — nâib fâil 3MP 'û', 15. kelime); muhatap 2MS (adsız; 'tezâlu', 'tattali'u', 'fa'fu', 'vasfah'); 'xâ'inetin' (nekre; 21. kelime); 'qalîlen minhum' (müstesnâ, 24-25. kelime); "
       "Allah (lafız; 'yuhibbu' faili); 'l-muhsinîn' ('yuhibbu' mef'ûlü; belirli çoğul, 32. kelime)")
T14 = ("'llezîne qâlû innâ nasârâ' (2-5. kelime; söz içi konuşan 1P 'innâ'; adlı 'nasârâ' — ölçüm rol fail); konuşan 1P (adsız; 'axaznâ', 'ağraynâ' — gönderge lafız); 'mîsâqahum' 3MP (gönderge 'llezîne'); "
       "'nesû' faili 3MP (adsız); 'zukkirû' faili (adsız; edilgen — nâib fâil 3MP 'û', 11. kelime); 'beynehumu' 3MP; Allah (lafız; 'yunebbi'uhumu' faili); 'kânû' ve 'yasna'ûn' faili 3MP (adsız)")

D = {}
D[12] = ("◇ 've leqad axaza'llâhu mîsâqa benî isrâ'île ve be'asnâ minhumu'sney 'aşera neqîben ve qâla'llâhu innî ma'akum le-in eqamtumu's-salâte ve âteytumu'z-zekâte ve âmentum bi-rusulî ve 'azzertumûhum ve eqradtumu'llâhe qardan hasenen le-ukeffiranne 'ankum seyyi'âtikum ve le-udxilennekum cennâtin tecrî min tahtihe'l-enhâru fe-men kefera ba'de zâlike minkum fe-qad dalle sevâ'e's-sebîl' — "
 "'ve' + 'le' + 'qad' + PERF 3MS I. bab + lafız + 'mîsâq' + çoğul 'buneyy' + özel ad 'isrâ'îl' + 've' + PERF 1P I. bab + 'min' + 3MP + ikil 'isneyn' + ''aşer' + nekre 'neqîb' + 've' + PERF 3MS I. bab + lafız + 'inne' + 1S + 'ma'a' + 2MP + 'le' + 'in' + PERF 2MP IV. bab + belirli 'salâ' + 've' + PERF 2MP IV. bab + belirli 'zekâ' + 've' + PERF 2MP IV. bab + 'bi' + çoğul 'rasûl' + 1S + 've' + PERF 2MP II. bab + 3MP + 've' + PERF 2MP IV. bab + lafız + nekre 'qard' + nekre 'hasen' + 'le' + IMPF 1S II. bab + 'nûn' + ''an' + 2MP + çoğul 'seyyi'e' + 2MP + 've' + 'le' + IMPF 1S IV. bab + 'nûn' + 2MP + nekre çoğul 'cenne' + IMPF 3FS I. bab + 'min' + 'taht' + 3FS + belirli çoğul 'neher' + 'fe' + 'men' + PERF 3MS I. bab + 'ba'd' + 'zâ' + 'min' + 2MP + 'fe' + 'qad' + PERF 3MS I. bab + 'sevâ'' + belirli 'sebîl' "
 "(ölçüm edim şart, kip CERT 2 · COND 2 · EMPH 6; 1P 2 · 1S 4 · 2MP 15 · 3FS 2 · 3MP 2 · 3MS 4; bab I. bab ×6 · II. bab ×2 · IV. bab ×5). "
 "Allah lafzı 3., 13. ve 25. sırada (ölçüm allah z=0,81); Rab yok; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); ölçüm '{{1|aktör: adlı إِسْرائِيل 6\\. sırada \\(kavim, rol mecrur\\)}}' — satır aynen. "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=45 (n z=3,46); ölçüm '{{1|fâsıla ٱلسبيل → ل, ل sınıfı — KAFİYE KIRILMASI}}' — satır aynen; ölçüm '{{1|sayı işareti اثْنَيْن, عَشَر}}' — satır aynen; ölçüm '{{1|simetri \\[4, 14, 40, 1\\]}}' — satır aynen; ölçüm '{{1|harf 212 → harf3 205, isaret 7}}' — satır aynen; ölçüm '{{1|dış düğüm 7}}' — satır aynen; ölçüm '{{1|İÇ düğüm 1}}' — satır aynen. "
 "Ölçüm CERT 2: 'qad' (1. ve 42. kelime); COND 2: 'in' (16. kelime), 'men' (37. kelime); EMPH 6: 'le' (1., 16., 28. ve 31. kelime), 'nne' (28. ve 31. kelime) (okuma). "
 "Kök ikilemeleri (ölçüm) أله ×3: lafız 3., 13. ve 25. kelimede; قرض ×2: 'eqradtumu' (24. kelime) / 'qardan' (26. kelime); كفر ×2: 'le-ukeffiranne' (28. kelime) / 'kefera' (38. kelime) (okuma). "
 "'ve leqad' (1.)'deki 've' morph REM; 've be'asnâ' (7.), 've qâla' (12.), 've âteytumu' (19.), 've âmentum' (21.), 've 'azzertumûhum' (23.), 've eqradtumu' (24.) ve 've le-udxilennekum' (31.)'daki 've' CONJ; 'fe-men' (37.)'deki 'fe' REM; 'fe-qad' (42.)'daki 'fe' RSLT (okuma). "
 "Şahıs: 'axaza'llâhu' (3MS) ardından 've be'asnâ' (1P) — ölçüm iltifât 0 (okuma; aday kayıt). "
 + T12 + " (okuma). "
 + cumle(say('say 5:12 1-4 --on', "ve leqad axaza'llâhu mîsâq", True), say('say 5:12 2-4', "axaza'llâhu mîsâq"), say('say 5:12 4-6', "mîsâqa benî isrâ'îl"), say('say 5:12 5-6', "benî isrâ'îl")) + ' '
 + cumle(say('say 5:12 7-11 --on', "ve be'asnâ minhumu'sney 'aşera neqîben", True), say('lem 5:12:11', "neqîb"), say('dizi 5 12 9 10', "isneyn 'aşer")) + ' '
 + cumle(say('say 5:12 12-15 --on', "ve qâla'llâhu innî ma'akum", True), say('say 5:12 12-14', "ve qâla'llâhu innî"), say('dizi 5 12 12 14', "qâle allâh inne"), say('say 5:12 14-15', "innî ma'akum")) + ' '
 + cumle(say('say 5:12 16-20 --on', "le-in eqamtumu's-salâte ve âteytumu'z-zekâ", True), say('say 5:12 17-20', "eqamtumu's-salâte ve âteytumu'z-zekâ"), say('dizi 5 12 17 20', "aqâme salâ âtâ zekâ"), say('say 5:12 21-23 --on', "ve âmentum bi-rusulî ve 'azzertumûhum"), say('lem 5:12:23', "'azzar")) + ' '
 + cumle(say('say 5:12 24-27 --on', "ve eqradtumu'llâhe qardan hasenen", True), say('say 5:12 25-27', "llâhe qardan hasenen"), say('say 5:12 28-30', "le-ukeffiranne 'ankum seyyi'âtikum"), say('say 5:12 29-30', "'ankum seyyi'âtikum"), say('say 5:12 30-32', "seyyi'âtikum ve le-udxilennekum cennâtin"), say('dizi 5 12 30 32', "seyyi'e udxile cenne")) + ' '
 + cumle(say('say 5:12 31-36 --on', "ve le-udxilennekum cennâtin tecrî min tahtihe'l-enhâr", True), say('say 5:12 32-36', "cennâtin tecrî min tahtihe'l-enhâr")) + ' '
 + cumle(say('say 5:12 37-41 --on', "fe-men kefera ba'de zâlike minkum", True), say('say 5:12 37-39 --on', "fe-men kefera ba'de"), say('say 5:12 37-39', "fe-men kefera ba'de"), say('dizi 5 12 37 39', "men kefera ba'd"), say('say 5:12 42-45 --on', "fe-qad dalle sevâ'e's-sebîl"), say('say 5:12 43-45', "dalle sevâ'e's-sebîl")) + ' '
 "Ölçüm xref 2:108, 3:81, 3:187, 47:12 ve 60:1 (basılmış), okunmuş iki ayet, okunmamış bir ayet (sûre içi 1). Ölçüm nakarat3 altı kalıp: ikisi süzgeç GEÇER, dördü GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'le-in eqamtumu's-salâte' / 'fe-men kefera ba'de zâlike minkum' — ayetler arası: yok.",
 "◈K — K1 'l-enhâr' (36. kelime).",
 "◈B — —",
 "◈D — D1 've' + 'le' + 'qad' + PERF + lafız + izafet + izafet + özel ad + 've' + PERF + 'min' + sayı + sayı + nekre + 've' + PERF + lafız + 'inne' + 'ma'a' + 'le' + 'in' + PERF + belirli + 've' + PERF + belirli + 've' + PERF + 'bi' + izafet + 've' + PERF + 've' + PERF + lafız + nekre + nekre + 'le' + IMPF + ''an' + izafet + 've' + 'le' + IMPF + nekre + IMPF + 'min' + izafet + belirli + 'fe' + 'men' + PERF + 'ba'd' + 'zâ' + 'min' + 'fe' + 'qad' + PERF + izafet + belirli; "
 "D2 şart, CERT ('qad' 1. ve 42. kelime), COND ('in' 16. kelime, 'men' 37. kelime), EMPH ('le' 1., 16., 28. ve 31. kelime; 'nne' 28. ve 31. kelime); D3 أله ×3 · قرض ×2 · كفر ×2; 2:108, 2:245, 3:81, 3:187, 47:12, 48:9, 57:11 ve 60:1 eşleri; D4 1P 2 · 1S 4 · 2MP 15 · 3FS 2 · 3MP 2 · 3MS 4, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T12 + "; ölçüm aktörü 'benî isrâ'îl' içindeki özel ad; A2 ahit alma; temsilci gönderme; beraberlik; namaz; zekât; iman; destek; güzel borç; kötülükleri örtme; cennete sokma; inkâr; yoldan sapma; "
 "A3 'innî ma'akum' ile açılan söz (14-45. kelime); A4 " + BOLUM + "; bölüm açılışı; edim geçişi emir, nida → şart (ayetler arası); şahıs geçişi yok; söz açılır (14. kelime); söz kapanır (45. kelime, ayet içi); "
 "şart COND 'le-in' 16. kelime: 'eqamtumu's-salâte' / 'le-ukeffiranne 'ankum'; COND 'fe-men' 37. kelime: 'kefera' / 'fe-qad dalle'.",
)

D[13] = ("◇ 'fe-bimâ naqdihim mîsâqahum le'annâhum ve ce'alnâ qulûbehum qâsiyeten yuharrifûne'l-kelime 'an mevâdi'ihî ve nesû hazzan mimmâ zukkirû bihî ve lâ tezâlu tattali'u 'alâ xâ'inetin minhum illâ qalîlen minhum fa'fu 'anhum vasfah inna'llâhe yuhibbu'l-muhsinîn' — "
 "'fe' + 'bi' + 'mâ' + masdar 'naqd' + 3MP + 'mîsâq' + 3MP + PERF 1P I. bab + 3MP + 've' + PERF 1P I. bab + çoğul 'qalb' + 3MP + nekre etken ortaç 'qâsiye' + IMPF 3MP II. bab + belirli 'kelim' + ''an' + çoğul 'mevâdi'' + 3MS + 've' + PERF 3MP I. bab + nekre 'hazz' + 'min' + 'mâ' + edilgen PERF 3MP II. bab + 'bi' + 3MS + 've' + 'lâ' + IMPF 2MS I. bab + IMPF 2MS VIII. bab + ''alâ' + nekre etken ortaç 'xâ'ine' + 'min' + 3MP + 'illâ' + nekre 'qalîl' + 'min' + 3MP + 'fe' + IMPV 2MS I. bab + ''an' + 3MP + 've' + IMPV 2MS I. bab + 'inne' + lafız + IMPF 3MS IV. bab + belirli çoğul etken ortaç 'muhsin' "
 "(ölçüm edim emir, kip IMPV 2 · NEG 1; 1P 4 · 2MS 4 · 3MP 13 · 3MS 3; bab I. bab ×6 · II. bab ×2 · IV. bab ×1 · VIII. bab ×1). "
 "Allah lafzı 30. sırada (ölçüm allah z=0,10); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=32 (n z=2,08); ölçüm '{{2|biçim ISTISNA}}' — satır aynen; ölçüm '{{2|EDİLGEN 1/10 fiil, pas z=0,24}}' — satır aynen; ölçüm '{{2|fâsıla ٱلمحسنين → ن, N sınıfı}}' — satır aynen; ölçüm '{{2|sayı işareti قَلِيل}}' — satır aynen; ölçüm '{{2|simetri \\[4, 14, 20, 1\\]}}' — satır aynen; ölçüm '{{2|harf 151 → harf3 138, isaret 13}}' — satır aynen; ölçüm '{{2|dış düğüm 4}}' — satır aynen; ölçüm '{{2|İÇ düğüm 1}}' — satır aynen. "
 "Ölçüm IMPV 2: 'fa'fu' (26. kelime), 'vasfah' (28. kelime); NEG 1: 'lâ' (17. kelime) (okuma); ölçüm biçim ISTISNA — 'illâ' (23. kelime, morph EXP); D2'de yazılmadı (okuma); ölçüm EDİLGEN — 'zukkirû' (15. kelime, morph PASS) (okuma). "
 "'fe-bimâ' (1.)'deki 'fe' morph REM; 've ce'alnâ' (5.)'daki 've' CONJ; 've nesû' (12.)'daki 've' CIRC; 've lâ' (17.)'daki 've' REM; 'fa'fu' (26.)'daki 'fe' REM; 'vasfah' (28.)'daki 've' CONJ (okuma). "
 "Şahıs: muhatap 2MS (17-28. kelime) bölümde yeni muhatap; 5:12 muhatabı 2MP (okuma). "
 + T13 + " (okuma). "
 + cumle(say('say 5:13 1-3 --on', "fe-bimâ naqdihim mîsâqahum", True), say('say 5:13 2-3', "naqdihim mîsâqahum"), say('say 5:13 4-7', "le'annâhum ve ce'alnâ qulûbehum qâsiyeten"), say('lem 5:13:7', "qâsiye")) + ' '
 + cumle(say('say 5:13 8-11', "yuharrifûne'l-kelime 'an mevâdi'ih", True), say('lem 5:13:8', "yuharrif"), say('say 5:13 12-16 --on', "ve nesû hazzan mimmâ zukkirû bih"), say('say 5:13 12-16', "ve nesû hazzan mimmâ zukkirû bih"), say('dizi 5 13 12 16', "nesiye hazz min mâ zukkir bi"), say('say 5:13 13-16', "hazzan mimmâ zukkirû bih")) + ' '
 + cumle(say('say 5:13 17-21 --on', "ve lâ tezâlu tattali'u 'alâ xâ'ine", True), say('lem 5:13:21', "xâ'ine"), say('say 5:13 23-25', "illâ qalîlen minhum"), say('say 5:13 26-28 --on', "fa'fu 'anhum vasfah")) + ' '
 + cumle(say('say 5:13 29-32', "inna'llâhe yuhibbu'l-muhsinîn", True), say('say 5:13 29-31', "inna'llâhe yuhibb"), say('dizi 5 13 29 31', "inne allâh ahbeb"), say('say 5:13 30-32', "llâhe yuhibbu'l-muhsinîn"), say('dizi 5 13 30 32', "allâh ahbeb muhsin")) + ' '
 "Ölçüm xref 2:195, 3:134 ve 4:46 (basılmış), okunmuş bir ayet, okunmamış bir ayet (sûre içi 1). Ölçüm nakarat3 üç kalıp: biri süzgeç GEÇER, ikisi GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'tattali'u 'alâ xâ'inetin minhum' / 'fa'fu 'anhum vasfah' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 'mevâdi'ihî' (11. kelime); B3 'qulûbehum' (6. kelime); B4 —.",
 "◈D — D1 'fe' + 'bi' + 'mâ' + izafet + izafet + PERF + 've' + PERF + izafet + nekre + IMPF + belirli + ''an' + izafet + 've' + PERF + nekre + 'min' + 'mâ' + PERF + 'bi' + 've' + 'lâ' + IMPF + IMPF + ''alâ' + nekre + 'min' + 'illâ' + nekre + 'min' + 'fe' + IMPV + ''an' + 've' + IMPV + 'inne' + lafız + IMPF + belirli; "
 "D2 emir, IMPV ('fa'fu' 26. kelime, 'vasfah' 28. kelime), NEG ('lâ' 17. kelime); D3 kök ikilemesi yok; 2:75, 2:195, 2:249, 3:134, 4:46, 4:155, 22:53 ve 40:19 eşleri; 5:14 blok içi eşi; D4 1P 4 · 2MS 4 · 3MP 13 · 3MS 3, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T13 + "; aktör yok (ölçüm); A2 ahit bozma; lanet; kalp katılığı; kelimeleri saptırma; unutma; hainlik; af; hoşgörü; iyilik edenleri sevme; A3 —; A4 " + BOLUM + "; edim geçişi şart → emir (ayetler arası); şahıs geçişi 2 → 3 (ayetler arası); muhatap 2MP → 2MS (17. kelime).",
)

D[14] = ("◇ 've mine'llezîne qâlû innâ nasârâ axaznâ mîsâqahum fe-nesû hazzan mimmâ zukkirû bihî fe-ağraynâ beynehumu'l-'adâvete ve'l-bağdâ'e ilâ yevmi'l-qiyâmeti ve sevfe yunebbi'uhumu'llâhu bimâ kânû yasna'ûn' — "
 "'ve' + 'min' + 'ellezî' + PERF 3MP I. bab + 'inne' + 1P + özel ad 'nasrânî' + PERF 1P I. bab + 'mîsâq' + 3MP + 'fe' + PERF 3MP I. bab + nekre 'hazz' + 'min' + 'mâ' + edilgen PERF 3MP II. bab + 'bi' + 3MS + 'fe' + PERF 1P IV. bab + 'beyn' + 3MP + belirli ''adâve' + 've' + belirli 'bağdâ'' + 'ilâ' + 'yevm' + belirli 'qiyâme' + 've' + 'sevfe' + IMPF 3MS II. bab + 3MP + lafız + 'bi' + 'mâ' + PERF 3MP I. bab + IMPF 3MP I. bab "
 "(ölçüm edim haber, kip FUT 1; 1P 5 · 3MP 13 · 3MS 2; bab I. bab ×5 · II. bab ×2 · IV. bab ×1). "
 "Allah lafzı 22. sırada (ölçüm allah z=0,27); Rab yok; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); ölçüm '{{3|aktör: adlı نَصْرانِيّ 5\\. sırada \\(cins, rol fail\\)}}' — satır aynen. "
 "Ölçüm '{{3|yıldız yok}}' — satır aynen; n=25 (n z=1,34); ölçüm '{{3|EDİLGEN 1/8 fiil, pas z=0,38}}' — satır aynen; ölçüm '{{3|fâsıla يصنعون → ن, N sınıfı}}' — satır aynen; ölçüm '{{3|simetri \\[3, 2, 10, 1\\]}}' — satır aynen; ölçüm '{{3|harf 123 → harf3 116, isaret 7}}' — satır aynen; ölçüm '{{3|dış düğüm 1}}' — satır aynen; ölçüm '{{3|İÇ düğüm 2}}' — satır aynen. "
 "Ölçüm FUT 1: 'sevfe' (20. kelime) (okuma); ölçüm EDİLGEN — 'zukkirû' (11. kelime, morph PASS) (okuma). "
 "'ve mine' (1.)'deki 've' morph CONJ; 'fe-nesû' (8.) ve 'fe-ağraynâ' (13.)'daki 'fe' CONJ; 've'l-bağdâ'e' (16.)'daki 've' CONJ; 've sevfe' (20.)'deki 've' REM (okuma). "
 + T14 + " (okuma). "
 + cumle(say('say 5:14 1-3 --on', "ve mine'llezîne qâlû", True), say('say 5:14 1-3', "ve mine'llezîne qâlû"), say('dizi 5 14 1 3', "min ellezî qâle"), say('say 5:14 1-5 --on', "ve mine'llezîne qâlû innâ nasârâ"), say('say 5:14 2-5', "llezîne qâlû innâ nasârâ"), say('say 5:14 6-7', "axaznâ mîsâqahum")) + ' '
 + cumle(say('say 5:14 8-12 --on', "fe-nesû hazzan mimmâ zukkirû bih", True), say('say 5:14 8-12', "fe-nesû hazzan mimmâ zukkirû bih"), say('dizi 5 14 8 12', "nesiye hazz min mâ zukkir bi"), say('say 5:14 9-12', "hazzan mimmâ zukkirû bih")) + ' '
 + cumle(say('say 5:14 13-16 --on', "fe-ağraynâ beynehumu'l-'adâvete ve'l-bağdâ'", True), say('say 5:14 14-16', "beynehumu'l-'adâvete ve'l-bağdâ'"), say('dizi 5 14 14 16', "beyn 'adâve bağdâ'"), say('say 5:14 14-19', "beynehumu'l-'adâvete ve'l-bağdâ'e ilâ yevmi'l-qiyâme"), say('dizi 5 14 14 19', "beyn 'adâve bağdâ' ilâ yevm qiyâme"), say('say 5:14 17-19', "ilâ yevmi'l-qiyâme")) + ' '
 + cumle(say('say 5:14 20-25 --on', "ve sevfe yunebbi'uhumu'llâhu bimâ kânû yasna'ûn", True), say('say 5:14 23-25', "bimâ kânû yasna'ûn")) + ' '
 "Ölçüm xref 60:4 (basılmış), okunmamış iki ayet (sûre içi 2). Ölçüm nakarat3 beş kalıp: dördü süzgeç GEÇER, biri GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K2 'yevmi' (18. kelime).",
 "◈B — —",
 "◈D — D1 've' + 'min' + 'ellezî' + PERF + 'inne' + özel ad + PERF + izafet + 'fe' + PERF + nekre + 'min' + 'mâ' + PERF + 'bi' + 'fe' + PERF + izafet + belirli + 've' + belirli + 'ilâ' + izafet + belirli + 've' + 'sevfe' + IMPF + lafız + 'bi' + 'mâ' + PERF + IMPF; "
 "D2 haber, FUT ('sevfe' 20. kelime); D3 kök ikilemesi yok; 16:112 ve 60:4 eşleri; 5:13 blok içi eşi; D4 1P 5 · 3MP 13 · 3MS 2, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T14 + "; A2 ahit alma; unutma; düşmanlık; öfke; kıyamet günü; haber verme; A3 'innâ nasârâ' (söz içi, 4-5. kelime); A4 " + BOLUM + "; edim geçişi emir → haber (ayetler arası); şahıs geçişi yok; söz açılır (4. kelime); söz kapanır (5. kelime, ayet içi).",
)

out = ['# ── blok 5:12-14 (2026-11-15) ──', 'MEAL5 = {']
for n in range(12, 15):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M5 = {']
for n in range(12, 15):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL5); M.update(M5)']
open('/home/claude/yamalar/metin_5_12_14.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')

# blok 13 (5:37-40) ARIZA oluşturucu — bölüm 6-2 (bölüm kapanışı)
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b13/olcum.txt'
os.environ['SAY2'] = '/home/claude/b13/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK_ESKI = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b11.txt', encoding='utf-8').read() + ']')
VF_YAZI_ESKI = {33: {6: "'ve rasûlehû'", 7: "'ve yes'avne'", 18: "'ve erculuhum'", 30: "'ve lehum fi'l-âxirati'"}, 34: {9: "'fa'lemû'"}, 35: {6: "'ve'bteğû'", 9: "'ve câhidû'"}, 36: {11: "'ve mislehû'", 22: "'ve lehum 'azâbun'"}}
BOL = "'Bozgunculuğun cezası; vesile; hırsızlık ve tövbe'"


def sd(key):
    return sayim.S2[key][1]


def sic(key):
    n, d = sayim.S2[key]
    return 1 + len([x for x in d['basilan'] if x.startswith('5:')]) + d['okunmus_si'] + d['henuz_si']


def taban(key, ay):
    n, d = sayim.S2[key]
    p = [ay] + [x for x in d['basilan'] if x.startswith('5:') and x != ay]
    if d['okunmus_si']: p.append('okunmus_si %d' % d['okunmus_si'])
    if d['henuz_si']: p.append('henuz_si %d' % d['henuz_si'])
    return ' + '.join(p)


R5 = [
 ("5:39", "'inne allâh ğafûr rahîm'", 3, 'say 5:39 11-14', "harekesiz 'inna'llâhe ğafûrun rahîm' (11-14. kelime)",
  ('dizi 5 39 11 14', "inne allâh ğafûr rahîm", '11-14', "nakarat3 'ان' iskeleti 'inne' / 'enne' birleştiriyor: 'inne' dizisi sûre içi 1 + 'enne' dizisi sûre içi 2 (blok 12 R5 satırı, 5:34) = 3, toplam nakarat3 ile eşit")),
 ("5:39", "'allâh ğafûr rahîm'", 5, 'say 5:39 12-14', "harekesiz 'llâhe ğafûrun rahîm' (12-14. kelime)",
  ('dizi 5 39 12 14', "allâh ğafûr rahîm", '12-14', "biçim / i'râb farkı — harekesiz kalıp lafzın mansub yazımını ayırıyor")),
 ("5:40", "'şâ'e allâh 'alâ kull şey' qadîr'", 2, 'say 5:40 14-19', "harekesiz 'yeşâ'u ve'llâhu 'alâ kulli şey'in qadîr' (14-19. kelime)", None),
 ("5:40", "'allâh 'alâ kull şey' qadîr'", 3, 'say 5:40 15-19', "harekesiz 've'llâhu 'alâ kulli şey'in qadîr' (15-19. kelime)", None),
 ("5:40", "''alâ kull şey' qadîr'", 4, 'say 5:40 16-19', "harekesiz ''alâ kulli şey'in qadîr' (16-19. kelime)", None),
 ("5:40", "''alâ kull şey''", 5, 'say 5:40 16-18', "harekesiz ''alâ kulli şey'' (16-18. kelime)", None),
 ("5:40", "'mulk semâ' ard'", 4, 'say 5:40 6-8', "harekesiz 'mulku's-semâvâti ve'l-ard' (6-8. kelime)", None),
 ("5:40", "''alime enne allâh'", 4, 'say 5:40 2-4', "harekesiz 'ta'lem enna'llâh' (2-4. kelime)",
  ('dizi 5 40 2 4', "'alime enne allâh", '2-4', "çekim farkı — harekesiz kalıp kip ve şahıs çekimini ayırıyor")),
 ("5:40", "'ğafera li men şâ'e'", 2, 'say 5:40 12-14', "harekesiz 've yağfiru li-men yeşâ'' (12-14. kelime)",
  ('dizi 5 40 12 14', "ğafera li men şâ'e", '12-14', "çekim farkı — harekesiz kalıp önek 've' ve kip çekimini ayırıyor")),
 ("5:40", "''azzebe men şâ'e'", 2, 'say 5:40 9-11', "harekesiz 'yu'azzibu men yeşâ'' (9-11. kelime)",
  ('dizi 5 40 9 11', "'azzebe men şâ'e", '9-11', "çekim farkı — harekesiz kalıp kip çekimini ayırıyor")),
]
r5 = []
for ay, kal, nk, key, ad, dz in R5:
    s = sic(key)
    h = "%s nakarat3 %s %d (tür ic) / %s sûre içi %d (%s)" % (ay, kal, nk, ad, s, taban(key, ay))
    if s == nk:
        h += ' — tutuyor'
    else:
        dk, dad, dar, ger = dz
        ds = sic(dk)
        if ds == nk:
            h += " — tutmuyor; eşit aralıkla lemma dizisi '%s' (%s. kelime) sûre içi %d (%s) — tutuyor; gerekçe %s" % (dad, dar, ds, taban(dk, ay), ger)
        else:
            h += " — tutmuyor; eşit aralıkla lemma dizisi '%s' (%s. kelime) sûre içi %d (%s) — tutmuyor; gerekçe %s" % (dad, dar, ds, taban(dk, ay), ger)
    r5.append(h)

K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k}

VF_YAZI = {37: {6: "'ve mâ hum'", 10: "'ve lehum'"}, 38: {1: "'ve's-sâriqu'", 2: "'ve's-sâriqatu'", 3: "'fa'qta'û'", 11: "'ve'llâhu 'azîzun'"}, 39: {1: "'fe-men'", 6: "'ve asleha'", 7: "'fe-inna'llâhe'"}, 40: {8: "'ve'l-ardi'", 12: "'ve yağfiru'", 15: "'ve'llâhu 'alâ'"}}
M37 = ("5:37 'Ateşten çıkmak isterler' ('yurîdûne en yaxrucû mine'n-nâr', 'iste-' 'yurîdûne' karşılığı (1. kelime; IV. bab), 'ûne' 1. kelimede karşılıksız (fail eki — 'isterler' içinde), 'en' 2. kelimede '-mek' ile (masdar; morph SUB), 'çık-' 'yaxrucû' karşılığı (3. kelime; I. bab), 'û' 3. kelimede karşılıksız (fail eki — 'çıkmak' içinde), "
 "'min' 4. kelimede '-ten' ile (ayrılma eki; fiil yönetimi takdiri), 'ateş' 'nâr' karşılığı (5. kelime), sıralama: fiil sona alındı); "
 "'oysa onlar oradan çıkacak değillerdir' ('ve mâ hum bi-xâricîne minhâ', 've' 6. kelimede 'oysa' ile (morph REM), 'mâ' 6. kelimede 'değil' ile (morph NEG; 'kâne' ailesi), 'hum' 7. kelimede 'onlar' ile, 'bi' 8. kelimede karşılıksız (haber 'bi'si; morph P), 'çıkacak' 'xâric' açılımı (8. kelime; ortaç; çoğul '-ler' 'değillerdir' içinde), "
 "'min' 9. kelimede '-dan' ile, 'hâ' 9. kelimede 'ora' ile ('oradan' içinde), '-dir' takdiri ('değillerdir' içinde; olumsuz haber), sıralama: haber sona alındı); "
 "'Onlar için sürekli bir azap vardır' ('ve lehum 'azâbun muqîm', 've' 10. kelimede karşılıksız (morph REM; cümle başı), 'li' 10. kelimede 'için' ile, 'hum' 10. kelimede 'onlar' ile, 'azap' ''azâb' karşılığı (11. kelime; nekre — 'bir' takdiri), 'sürekli' 'muqîm' karşılığı (12. kelime; nekre — takdirsiz; sıfat), "
 "'var' takdiri (isim cümlesi), '-dır' takdiri ('vardır' içinde; isim cümlesi haberi), sıralama: mübteda sona alındı)")
M38 = ("5:38 'Hırsız erkek ve hırsız kadının' ('ve's-sâriqu ve's-sâriqa', 've' 1. kelimede karşılıksız (morph REM; cümle başı), 'hırsız erkek' 'sâriq' açılımı (1. kelime; belirli; eril), 've' 2. kelimede 've' ile (morph CONJ), 'hırsız kadın' 'sâriqa' açılımı (2. kelime; belirli; dişil; ilgi eki '-ın' — 'ellerini' yönetimi takdiri)); "
 "'kazandıklarına bir ceza ve Allah'tan bir ibret olarak' ('cezâ'en bi-mâ kesebâ nekâlen mina'llâh', 'ceza' 'cezâ'' karşılığı (5. kelime; nekre — 'bir' takdiri; 'olarak' takdiri), 'bi' 6. kelimede yönelme eki ile ('kazandıklarına' içinde; fiil yönetimi takdiri), 'mâ' 6. kelimede '-dıkları' ile (ism-i mevsûl), 'kazan-' 'kesebâ' karşılığı (7. kelime; I. bab; 3MD), "
 "'â' 7. kelimede 3MD ile ('kazan-' çekiminde; ikil fail eki Türkçe çoğulla), 'ibret' 'nekâl' karşılığı (8. kelime; nekre — 'bir' takdiri), 'min' 9. kelimede '-tan' ile, lafız 10. kelimede 'Allah' ile, 've' takdiri (nekreler arası), sıralama: amaç öne alındı); "
 "'ellerini kesin' ('fa'qta'û eydiyehumâ', 'fe' 3. kelimede karşılıksız (morph SUP), 'kes-' 'qta'û' karşılığı (3. kelime; I. bab; emir 2MP; LEM 'quti'a' (morph LEM ham biçim)), 'û' 3. kelimede 2MP ile ('kesin' içinde), 'el' 'yed' karşılığı (4. kelime; çoğul '-ler'), 'humâ' 4. kelimede iyelik ile ('ellerini' içinde; 3D), sıralama: fiil sona alındı); "
 "'Allah üstündür, hikmet sahibidir' ('ve'llâhu 'azîzun hakîm', 've' 11. kelimede karşılıksız (morph REM), lafız 11. kelimede 'Allah' ile, 'üstün' ''azîz' karşılığı (12. kelime; nekre — takdirsiz), 'hikmet sahibi' 'hakîm' açılımı (13. kelime; nekre — takdirsiz), '-dür' takdiri ('üstündür' içinde; isim cümlesi haberi), '-dir' takdiri ('sahibidir' içinde; isim cümlesi haberi))")
M39 = ("5:39 'Kim zulmünden sonra tövbe eder ve düzeltirse' ('fe-men tâbe min ba'di zulmihî ve asleha', 'fe' 1. kelimede karşılıksız (morph REM), 'men' 1. kelimede 'kim' ile (morph COND; şart eki '-se' 'düzeltirse' içinde), 'tövbe et-' 'tâbe' açılımı (2. kelime; I. bab; geniş zaman açılımı), 'min' 3. kelimede karşılıksız ('sonra' içinde), 'sonra' 'ba'd' karşılığı (4. kelime), "
 "'zulüm' 'zulm' karşılığı (5. kelime; iyelik ve ayrılma eki ile 'zulmünden'; fiil yönetimi takdiri), 'hî' 5. kelimede iyelik ile ('zulmünden' içinde), 've' 6. kelimede 've' ile (morph CONJ), 'düzelt-' 'asleha' karşılığı (6. kelime; IV. bab), sıralama: fiil sona alındı); "
 "'şüphesiz Allah onun tövbesini kabul eder' ('fe-inna'llâhe yetûbu 'aleyh', 'fe' 7. kelimede karşılıksız (morph RSLT; şart cevabı), 'inne' 7. kelimede 'şüphesiz' ile, lafız 8. kelimede 'Allah' ile, 'tövbesini kabul et-' 'yetûbu' açılımı (9. kelime; I. bab; ''alâ' ile — tövbeyi kabul), ''alâ' 10. kelimede karşılıksız ('tövbesini' içinde), 'hî' 10. kelimede 'onun' ile, sıralama: fiil sona alındı); "
 "'Şüphesiz Allah bağışlayandır, merhamet edendir' ('inna'llâhe ğafûrun rahîm', 'inne' 11. kelimede 'şüphesiz' ile, lafız 12. kelimede 'Allah' ile, 'bağışlayan' 'ğafûr' karşılığı (13. kelime; nekre — takdirsiz), 'merhamet eden' 'rahîm' açılımı (14. kelime; nekre — takdirsiz), '-dır' takdiri ('bağışlayandır' içinde; 'inne' haberi), '-dir' takdiri ('edendir' içinde; 'inne' haberi))")
M40 = ("5:40 'Göklerin ve yerin mülkünün Allah'ın olduğunu bilmez misin?' ('e-lem ta'lem enna'llâhe lehû mulku's-semâvâti ve'l-ard', 'e' 1. kelimede 'mi' ile ('misin' içinde; morph INTG), 'lem' 1. kelimede olumsuzluk eki ile ('-mez' içinde; morph NEG), 'bil-' 'ta'lem' karşılığı (2. kelime; I. bab; 2MS), 'enne' 3. kelimede '-duğunu' ile ('olduğunu' içinde), lafız 4. kelimede 'Allah' ile, "
 "'li' 5. kelimede ilgi eki ile ('Allah'ın' içinde; aitlik), 'hû' 5. kelimede karşılıksız ('Allah'ın' içinde), 'mülk' 'mulk' karşılığı (6. kelime; ilgi eki ile 'mülkünün'), 'gök' 'semâ'' karşılığı (7. kelime; çoğul; ilgi eki ile 'göklerin'), 've' 8. kelimede 've' ile (morph CONJ), 'yer' 'ard' karşılığı (8. kelime; ilgi eki ile 'yerin'), 'ol-' takdiri ('olduğunu' içinde; 'enne' cümlesi), sıralama: soru sona alındı); "
 "'Dilediğine azap eder' ('yu'azzibu men yeşâ'', 'azap et-' 'yu'azzibu' açılımı (9. kelime; II. bab), 'men' 10. kelimede '-diğine' ile (ism-i mevsûl; 'dilediğine' içinde; fiil yönetimi takdiri), 'dile-' 'yeşâ'u' karşılığı (11. kelime), sıralama: fiil sona alındı); "
 "'dilediğini bağışlar' ('ve yağfiru li-men yeşâ'', 've' 12. kelimede karşılıksız (morph CONJ; virgül), 'bağışla-' 'yağfiru' karşılığı (12. kelime; I. bab), 'li' 13. kelimede belirtme eki ile ('dilediğini' içinde; fiil yönetimi takdiri), 'men' 13. kelimede '-diğini' ile (ism-i mevsûl), 'dile-' 'yeşâ'' karşılığı (14. kelime), sıralama: fiil sona alındı); "
 "'Allah her şeye güç yetirendir' ('ve'llâhu 'alâ kulli şey'in qadîr', 've' 15. kelimede karşılıksız (morph REM), lafız 15. kelimede 'Allah' ile, ''alâ' 16. kelimede yönelme eki ile ('şeye' içinde; fiil yönetimi takdiri), 'her' 'kull' karşılığı (17. kelime), 'şey' 'şey'' karşılığı (18. kelime; nekre — takdirsiz), 'güç yetiren' 'qadîr' açılımı (19. kelime; nekre — takdirsiz), '-dir' takdiri ('yetirendir' içinde; isim cümlesi haberi))")
MEALS = (M37, M38, M39, M40)



def _bol(s, sep):
    out, d, cur, i = [], 0, '', 0
    while i < len(s):
        c = s[i]
        if c == '(': d += 1
        elif c == ')': d -= 1
        if d == 0 and s.startswith(sep, i):
            out.append(cur); cur = ''; i += len(sep); continue
        cur += c; i += 1
    out.append(cur)
    return out


MK = {}
for blok in MEALS:
    n = int(blok.split(' ', 1)[0].split(':')[1]); govde = blok.split(' ', 1)[1]
    for seg in _bol(govde, "; '"):
        seg = seg if seg.startswith("'") else "'" + seg
        j = seg.index("' (")
        tr = seg[1:j]; ic = seg[j + 3:].rstrip(')')
        parca = _bol(ic, ', ')
        MK.setdefault(n, []).append((tr, parca[0].strip("'"), parca[1:]))
open('/home/claude/b13/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '13')
BLOKLAR = [str(i) for i in range(1, 14)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR).replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '13').replace('\n', '; ')
EMS = open('/home/claude/b13/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '37', '40', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b13/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
MFARK = [(k, n, sayim.S2[k.replace(' --medde', '')][0]) for k, (n, d) in sayim.S2.items() if '--medde' in k]
MEDF = '; '.join("%s meddeli %d / meddesiz %d" % (k.replace(' --medde', ''), m, n) for k, n, m in MFARK)
MEDF += ' — fark yok, yeni eş yok' if all(n == m for k, n, m in MFARK) else ' — FARK VAR'
GLS = run('/home/claude/sunum/gloss_tara.py', '37', '40', '13').splitlines()

I = [
 "araç değişikliği (bölüm 5 kuralı 11): sunum/ham_elle.txt'e 5:38 3. kelimenin morph LEM'i 'quti'a' eklendi (etken emir 'fa'qta'û' için edilgen görünümlü LEM; lem_bozuk.py bayraklamıyor); sunum/kelime_kontrol.py — ''â'' anahtarı 3MD fail ekini de tanıyor (5:38 'kesebâ'; önceki sürüm 'zamir kayıtsız 1' veriyordu); sunum/sinifla.py (SON 40); başka araç değişmedi",
 "kök tablosu: ölçümde '???' 5:37-40 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 37 40 13'): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:38:12 عَزِيز ve 5:38:13 حَكِيم 'ilahi' — 've'llâhu 'azîzun hakîm', kural ''ve'llâhu X' kuralı → ilahi'; 5:39:13 غَفُور ve 5:39:14 رَحِيم 'ilahi' — 'inna'llâhe ğafûrun rahîm', kural ''inne/enne' haberi → ilahi' (lafzın haberi); 5:40:19 قَدِير 'ilahi' — 've'llâhu 'alâ kulli şey'in qadîr', kural ''ve'llâhu X' kuralı → ilahi' (esma_el_ekle → esma_kayit); "
 "kural adı kapalı listeyle karşılaştırıldı; lafız 5:38, 5:39, 5:40; 5:37 lafız yok; Rab yok",
 "esma_kayit: 5:37 'mühür hayır' (sınıf 0/0 — uyuşuyor), 5:38 'mühür EVET (ÇİFT) ton celâl' (ölçüm MÜHÜR — uyuşuyor), 5:39 'mühür EVET (ÇİFT) ton cemâl' (ölçüm MÜHÜR — uyuşuyor), 5:40 'mühür EVET ton celâl' (ölçüm MÜHÜRSÜZ — uyuşmuyor; fâsıla kafiye kırılması, ر)",
 "ölçüm: 5:37 '{{1|lafız YOK · Rab YOK}}', '{{1|fâsıla مقيم → م, N sınıfı}}', '{{1|simetri \\[3, 2, 7, 1\\]}}', '{{1|harf 52 → harf3 48, isaret 4}}' ve '{{1|dış düğüm 0}}'; 5:38 '{{2|fâsıla حكيم → م, N sınıfı}}', '{{2|harf 68 → harf3 63, isaret 5}}' ve '{{2|dış düğüm 0}}'; "
 "5:39 '{{3|fâsıla رحيم → م, N sınıfı}}', '{{3|simetri \\[3, 2, 9, 1\\]}}', '{{3|harf 53 → harf3 49, isaret 4}}' ve '{{3|dış düğüm 1}}'; 5:40 '{{4|fâsıla قدير → ر, R sınıfı}}', '{{4|simetri \\[3, 4, 15, 1\\]}}', '{{4|harf 73 → harf3 69, isaret 4}}' ve '{{4|dış düğüm 1}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 37 40 13'): KALAN_P",
 "ölçüm aktör: 5:37-40 aktör yok (ölçüm); 5:38 's-sâriqu' ve 's-sâriqatu' ortaç, adsız",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle): 5:37 haber — NEG 1 'mâ' (6.); 5:38 emir — IMPV 1 'fa'qta'û' (3.); 5:39 şart — COND 1 'men' (1.); 5:40 soru — INTG 1 + NEG 1 'e-lem' (1.)",
 "yıldız: 5:38 ★★, 5:39 ★★, 5:40 ★; 5:37 yıldız yok — satır yıldız kaynağını adlandırmıyor; kaynak kapanış notunda bilançodan",
 "fâsıla: 5:36 م (أليم) → 5:37 م (مقيم) → 5:38 م (حكيم) → 5:39 م (رحيم) → 5:40 ر (قدير) — bölüm kapanışında kafiye kırılması (ölçüm KAFİYE KIRILMASI, 5:40); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref: 5:37 ve 5:38 xref yok; 5:39 9:102 (emsal olarak basıldı); 5:40 2:107 (emsal olarak basıldı)",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı ölçüm kalıbının öğelerinden morph LEM ham adıyla, ◇ lemma dizisi adıyla eş): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:37 ve 5:38 kalıp yok; 5:39 'inne allâh ğafûr rahîm' ve 'allâh ğafûr rahîm' süzgeç GEÇER; 5:40 'şâ'e allâh 'alâ kull şey' qadîr', 'allâh 'alâ kull şey' qadîr', ''alâ kull şey' qadîr', ''alâ kull şey'', 'mulk semâ' ard' ve ''alime enne allâh' GEÇER, 'ğafera li men şâ'e' ve ''azzebe men şâ'e' GEÇMEZ",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14 — ölçüt: 1P / 1S / 2MS / 2MP / 3MS / 3FS / 3D / 3MD / 3MP / 3FP zamirlerin hepsi 'adsız'): "
 "5:37 3MP (adsız — 'yurîdûne', 'yaxrucû' failleri; 'hum', 'lehum'), 3FS (adsız — 'minhâ', gönderge ateş), ''azâbun muqîm'; 5:38 's-sâriqu', 's-sâriqatu', muhatap 2MP (adsız), 3D (adsız — 'eydiyehumâ'), 3MD (adsız — 'kesebâ' faili), Allah (lafız), ''azîzun hakîm'; "
 "5:39 'men' (şart ismi; 3MS fail adsız), 3MS (adsız — 'zulmihî', 'asleha', ''aleyh'), Allah (lafız), 'ğafûrun rahîm'; 5:40 muhatap 2MS (adsız), Allah (lafız), 3MS (adsız — 'lehû', 'yu'azzibu', 'yağfiru', 'yeşâ'u'), 'men', 'mulku's-semâvâti ve'l-ard', 'şey'in qadîr' — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): blokta 'qâle' yok, söz aralığı yok (A3 —); 5:38 emir ve 5:40 soru muhataba doğrudan; REM sapması (komut 'python3 sunum/bolum4_kurallar.py 37 40 13' — A3 aralığında morph REM): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:37 've mâ' (6.), 've lehum' (10.) REM; 5:38 've's-sâriqu' (1.) REM, 've's-sâriqatu' (2.) CONJ, 'fa'qta'û' (3.) SUP, 've'llâhu' (11.) REM; 5:39 'fe-men' (1.) REM, 've asleha' (6.) CONJ, 'fe-inna'llâhe' (7.) RSLT; 5:40 've'l-ardi' (8.), 've yağfiru' (12.) CONJ, 've'llâhu' (15.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 5:38 ◈B يدي ('eydiyehumâ' 4. kelime — B3; anlam notu: ceza olarak el kesme); 5:40 ◈K سمو ('s-semâvâti' 7. kelime — K1), أرض ('l-ardi' 8. kelime — K1; anlam notu: göklerin ve yerin mülkü); 5:37 ve 5:39 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7 — komut 'python3 sunum/bolum5_kurallar.py 37 40 13'; aday kökler ve morph T isimleri): TETIKDISI; anılış: 5:38 kök قطع ('fa'qta'û' 3. kelime — kesme; B3 'eydiyehumâ' ile birlikte; 5:33'te de anıldı); 5:39 kök بعد ('ba'di' 4. kelime — 'sonra', zaman; morph T etiketi yok, aday listesi dışı, elle anıldı); oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:37 (9:68), 5:38 (2:66), 5:39 (9:102), 5:40 (2:107) (kontrol.py ile); blok geçişi 5:36 → 5:37: 5:36 've lehum 'azâbun elîm' / 5:37 've lehum 'azâbun muqîm' — lemma dizisi farklı (sıfat), kalıp olarak alıntılanmadı, ardışık bağ kurulmadı; "
 "D3 dışı bırakılan basılmış sayım eşleri: 5:38 'mina'llâh' kümesi; 5:39 'llâhe ğafûrun rahîm' ve 'ğafûrun rahîm' kümeleri (2:173, 5:3, 5:34, 16:115 …), 'min ba'd' kümesi; 5:40 'mulku's-semâvâti ve'l-ard' 5:17, 5:18, 48:14; 'li-men yeşâ'' 2:284, 3:129, 5:18, 48:14; ''alâ kulli şey'in qadîr' 2:284, 5:17, 5:19 — kalıp başına ölçüt: geniş nakarat kalıbı, bağ kurulmadı (bölüm 3 kuralı 11); "
 "bölüm içi 5:34 / 5:39 'ğafûrun rahîm' eşliği R5'te (bağ kurulmadı)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:37 edim geçişi şart → haber; şahıs geçişi yok; 5:38 edim geçişi haber → emir; şahıs geçişi 3 → 2; 5:39 edim geçişi emir → şart; şahıs geçişi 2 → 3; şart → cevap (ayet içi; COND 'men' 1. kelime: 'fe-men tâbe min ba'di zulmihî ve asleha' / 'fe-inna'llâhe yetûbu 'aleyh' (7. kelime)); 5:40 bölüm kapanışı; edim geçişi şart → soru; şahıs geçişi yok",
 "sözdizimi (okuma; morph etiketiyle): 5:37 'yurîdûne en yaxrucû' — masdar mef'ûl (morph SUB); 've mâ hum bi-xâricîne' — istînâf (morph REM), olumsuz isim cümlesi ('mâ' morph NEG, 'kâne' ailesi; haber 'bi' ile); 5:38 've's-sâriqu ve's-sâriqatu' — istînâf (morph REM), mübteda; 'fa'qta'û' — haber yerinde emir ('fe' morph SUP); 'cezâ'en' ve 'nekâlen' — nekre ACC (morph etiketi yalnız ACC; işlev okuması tam okuma sonu); "
 "5:39 'fe-men tâbe' — 'fe' istînâf (morph REM), 'men' şart (morph COND); 'fe-inna'llâhe' — cevap (morph RSLT); 5:40 'e-lem ta'lem' — olumsuz soru (morph INTG + NEG); 'yu'azzibu men yeşâ'u ve yağfiru li-men yeşâ'' — 'enne' cümlesine bağlı haber dizisi (morph etiketi yok, okuma); 've'llâhu' — istînâf (morph REM)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:37 kök خرج iki geçiş (3. ve 8. kelime) — isteme / olumsuzlama; 5:38 kök سرق iki geçiş (1. ve 2. kelime) — eril / dişil; 5:39 kök توب iki geçiş (2. ve 9. kelime) — kulun tövbesi / Allah'ın tövbeyi kabulü, bir lemma ('tâbe'); "
 "5:40 kök شيأ üç geçiş (11., 14. ve 18. kelime); 5:40 'e-lem ta'lem' ile açılıyor (1-2. kelime); bölüm 'innemâ cezâ'u' (5:33) ile açılıp ''alâ kulli şey'in qadîr' (5:40) ile kapanıyor; 5:34 'illa'llezîne tâbû' ve 5:39 'fe-men tâbe' — bölüm içinde iki tövbe istisnası (kök توب; 5:34 ve 5:39 'ğafûrun rahîm' ile kapanıyor); ayetler arası kalıp alıntısı yok",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 13'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + "'; çıktı aynen): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle): 've lehum 'azâbun muqîm' 5:37 'sürekli bir azap' / 9:68 'sürekli bir azap' (eş); 'nekâl' 5:38 'ibret' / 2:66 'ibret olacak bir ceza' (farklı); 'tâbe 'alâ' 5:39 'tövbesini kabul et-' / 9:102 'tövbelerini kabul et-' (eş); "
 "'llâhe lehû mulku's-semâvâti ve'l-ard' 5:40 'göklerin ve yerin mülkünün Allah'ın olduğu' / 2:107 'göklerin ve yerin mülkünün Allah'ın olduğu' (eş); 9:102 'rahîm' 'esirgeyen', 5:39 'merhamet eden' (farklı) — tam okuma sonu",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 37 40 13'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:37-40 tarayıcı adayı yok (cipa_tarama5_adaylari.json); 5:40 'lehû mulku's-semâvâti ve'l-ard' mülkiyet bildirimi — çıpa değil (olgu=False; doğa süreci iddiası yok); L3 / L4 adayı yok",
 "aday 1039: ayet içi 5:37 ('yurîdûne en yaxrucû mine'n-nâri' / 've mâ hum bi-xâricîne minhâ'), 5:40 ('yu'azzibu men yeşâ'u' / 've yağfiru li-men yeşâ'') — okuma; ayetler arası 5:38 / 5:39 ('fa'qta'û eydiyehumâ' / 'fe-inna'llâhe yetûbu 'aleyh'); eşleme betikle: ADAY_P",
 "aday 1041: kök توب 5:39 'tâbe' (kul) / 'yetûbu' (Allah) — bir lemma, iki özne; kök غفر 5:39 'ğafûr' (lafzın haberi) / 5:40 'yağfiru' (fiil, Allah) — okuma",
 "bölüm: " + BOL + " bölümü, bölüm 6-2 — bölüm kapanışı 5:40; bölüm iki blok (12 ve 13); başlıktaki 'hırsızlık' 5:38 ('s-sâriqu', 's-sâriqatu'), 'tövbe' 5:34 ve 5:39 ('tâbû', 'tâbe'); bölüm sonu bağımsız denetimi bu bloktan sonra (yamalar/bekleyen_ariza_5_b13.txt); "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b13/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 37 40 13'; lem_bozuk.py 13 çıktısı boş; sunum/ham_elle.txt): 5:38:3 'quti'a' — elle listede; meal maddesinde '(morph LEM ham biçim)' notlu; lemma adı listesinde notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 37 40 → AYN_SONUC; sunum/bolum4_kurallar.py 37 40 13 → KHATA_HEPSI; sunum/bolum5_kurallar.py 37 40 13 → B5_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (sunum/sonradan.py --plan 13): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('erâde', 'xarece', 'nâr', 'xâric', ''azâb', 'muqîm', 'sâriq', 'sâriqa', 'quti'a' (morph LEM ham biçim), 'yed', 'cezâ'', 'kesebe', 'nekâl', ''azîz', 'hakîm', 'tâbe', 'ba'd', 'zulm', 'asleha', 'ğafûr', 'rahîm', ''alime', 'mulk', 'semâ'', 'ard', ''azzebe', 'şâ'e', 'ğafera', 'kull', 'şey'', 'qadîr'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]


def yaz():
    items = [kes(x) for x in I]
    s = '\n (37, 40): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_37_40.txt', 'w', encoding='utf-8').write(s)


idx = I.index('KARSILIK_CAKISMA')
I[idx] = 'karşılık çakışması (geçici)'
yaz()
AYN = (run('/home/claude/sunum/ayn_kontrol.py', '37', '40').splitlines() or ['?'])[-1]
KUR = run('/home/claude/sunum/bolum4_kurallar.py', '37', '40', '13').splitlines()
KH = [l for l in KUR if l.startswith('HATA')]
B5 = run('/home/claude/sunum/bolum5_kurallar.py', '37', '40', '13').splitlines()
B5H = [l for l in B5 if l.startswith('HATA')]
REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
       'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h) or 'adsız / söz muhatabı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
       'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
       'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
       'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or 'ARIZA ⇔ ◇ bayt eşit'), 'HAMLEM_P': next((l for l in B5 if l.startswith('ham LEM')), '?'), 'B5_HEPSI': (B5[-1] if B5 else '?')}
for k, v in REP.items(): I = [x.replace(k, v) for x in I]
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_5_*.txt'), key=lambda p: int(p.split('_')[-2]))
CAK = run('/home/claude/sunum/cakisma.py', *DOS)
KYENI = set(re.findall(r"'([^']+)' '(?:[^']|'(?=[a-zâîû]))+' (?:karşılığı|açılımı)", ' '.join(MEALS)))
CAK_L = [l for l in CAK.splitlines() if l.startswith('KÖK') or l.split(' ←')[0] in KYENI]
KARAR = {}
for nn in ('06', '10', '11', '12', '13'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
I[idx] = ("karşılık çakışması (bölüm 4 kuralı 4, bölüm 5 kuralı 3 — komut 'python3 sunum/cakisma.py' + sûre 5'in okunmuş bütün ARIZA dosyaları; Türkçe fiil kökü eşlemesi betikle, son dosyaya dokunan gruplar; her grupta kapalı karar: 'çakışma değil' ya da 'çakışma — tam okuma sonu'): "
          + ('; '.join(KARAR.get(l.split(' ←')[0].strip() if not l.startswith('KÖK') else 'KÖK ' + l.split()[1], l + ' — karar yok') for l in CAK_L) if CAK_L else 'bu bloğa dokunan çakışma yok'))
yaz()
print('yazıldı', len(I))
print('\n'.join(CAK_L))
print(GLS); print(KUR); print(B5)

# blok 28 (5:90-93) ARIZA oluşturucu — bölüm 12-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b28/olcum.txt'
os.environ['SAY2'] = '/home/claude/b28/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {33: {6: "'ve rasûlehû'", 7: "'ve yes'avne'", 18: "'ve erculuhum'", 30: "'ve lehum fi'l-âxirati'"}, 34: {9: "'fa'lemû'"}, 35: {6: "'ve'bteğû'", 9: "'ve câhidû'"}, 36: {11: "'ve mislehû'", 22: "'ve lehum 'azâbun'"}}
BOL = "'Helalleri haram kılmama; yemin keffareti; içki ve kumar'"


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
 ("5:90", "'eyy ellezî âmene'", 16, 'say 5:90 1-3', "harekesiz 'yâ eyyuhe'llezîne âmenû' (1-3. kelime)", None),
 ("5:91", "'beyn 'adâve bağdâ''", 3, 'say 5:91 6-8', "harekesiz 'beynekumu'l-'adâvete ve'l-bağdâ'' (6-8. kelime)", ('dizi 5 91 6 8', "beyn 'adâve bağdâ'", '6-8', "biçim farkı (dizi 5 91 6 8): 5:14 elif yazımı, zamir eki; basılmamış eş zamir eki")),
 ("5:92", "'fe-in tevellâ 'alime enne'", 2, 'say 5:92 6-9 --on', "önek kesilmiş 'fe-in tevelleytum fe'lemû ennemâ' (6-9. kelime; biçim öğesi 'fe-in' / 'ennemâ' — ölçüm kalıbında önekli ve 'mâ' bitişik yazım)", ('dizi 5 92 6 9', "fe-in tevellâ 'alime enne", '6-9', "biçim farkı (dizi 5 92 6 9): basılmamış eş fiil çekimi, zamir eki")),
 ("5:93", "'ellezî âmene 'amile sâliha'", 2, 'say 5:93 3-6', "harekesiz 'llezîne âmenû ve 'amilu's-sâlihât' (3-6. kelime)", None),
 ("5:93", "'allâh ahbeb muhsin' (LEM 'ahbeb' (morph LEM ham biçim))", 2, 'say 5:93 22-24 --on', "önek kesilmiş 've'llâhu yuhibbu'l-muhsinîn' (22-24. kelime)", ('dizi 5 93 22 24', "allâh ahbeb muhsin", '22-24', "biçim farkı (dizi 5 93 22 24): basılmamış eş i'râb, önek")),
]
r5 = []
for ay, kal, nk, key, ad, dz, *tr_ in R5:
    s = sic(key)
    h = "%s nakarat3 %s %d (tür %s) / %s sûre içi %d (%s)" % (ay, kal, nk, (tr_[0] if tr_ else 'ic'), ad, s, taban(key, ay))  # bölüm 11 denetimi kuralı 3
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

VF_YAZI = {90: {6: "'ve'l-meysiru'", 7: "'ve'l-ensâbu'", 8: "'ve'l-ezlâmu'", 13: "'fe'ctenibûhu'"}, 91: {8: "'ve'l-bağdâ'e'", 11: "'ve'l-meysiri'", 12: "'ve yesuddekum'", 16: "'ve 'ani's-salâti'", 18: "'fe-hel'"}, 92: {1: "'ve atî'u'", 3: "'ve atî'u'", 5: "'ve'hzerû'", 6: "'fe-in'", 8: "'fe'lemû'"}, 93: {5: "'ve 'amilu'", 13: "'ve âmenû'", 14: "'ve 'amilu'", 18: "'ve âmenû'", 21: "'ve ahsenû'", 22: "'ve'llâhu'"}}
sys.path.insert(0, '/home/claude/b28/yap')
from seg import meals
MEALS = meals()


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
open('/home/claude/b28/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '28')
BLOKLAR = [str(i) for i in range(1, 29)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '28', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b28/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '90', '93', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b28/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b28/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '90', '93', '28').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_90_93.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'5:90', '5:91', '5:92', '5:93'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_90_93.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '5:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '5:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(90, 94))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "5:90 kök زلم ('l-ezlâmu' 8. kelime — fal okları) ve kök جنب ('fe'ctenibûhu' 13. kelime — kaçınma; kök anlamı 'yan, taraf'): tetik listesinde yok; 5:91 kök صدد ('yesuddekum' 12. kelime — alıkoyma): tetik listesinde yok; 5:92 kök ولي ('tevelleytum' 7. kelime — yüz çevirme): tetik listesinde yok; 5:93 'izâ' ('izâ me'ttaqav' 10. kelime — morph T, zaman şartı)"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '90', '93', '28')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b28/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 29)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b5:%d:\d+' % a_, s_) for a_ in range(90, 94))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: yalnız blok akışı (sunum/sinifla.py SON, sunum/basilan.txt — §3 adım 2 ve emsal işaretlemesi); denetim kuralı değişmedi; mutasyon_sina — MUT_SONUC; geriye dönük koşu son araç değişikliğinden sonra (blok 27) üretildi: GERI_P",
 "kök tablosu: ölçümde '???' 5:90, 5:91, 5:92 ve 5:93 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 90 93 28'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:92 'l-mubîn' (13. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (tebliğin sıfatı); 5:90, 5:91 ve 5:93 esmâ yok; lafız 5:91, 5:92 ve 5:93; 5:90 lafız yok; Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); "
 "gönderge tebliğ ('l-belâğu') — A1'de 'l-belâğu'l-mubîn' kaydında kural adıyla (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 90 93 28'): " + EMH,
 "ölçüm: 5:90 '{{1|fâsıla تفلحون → ن, N sınıfı}}', '{{1|harf 82 → harf3 80, isaret 2}}' ve '{{1|dış düğüm 0}}'; "
 "5:91 '{{2|fâsıla منتهون → ن, N sınıfı}}', '{{2|harf 91 → harf3 90, isaret 1}}', '{{2|dış düğüm 1}}' ve '{{2|İÇ düğüm 2}}'; "
 "5:92 '{{3|fâsıla ٱلمبين → ن, N sınıfı}}', '{{3|harf 76 → harf3 71, isaret 5}}', '{{3|dış düğüm 0}}' ve '{{3|esit2 → 64:12 oran 0,8960 kademe BENZER}}'; "
 "5:93 '{{4|fâsıla ٱلمحسنين → ن, N sınıfı}}', '{{4|simetri \\[6, 2, 11, 2\\]}}', '{{4|harf 127 → harf3 115, isaret 12}}', '{{4|dış düğüm 3}}' ve '{{4|İÇ düğüm 1}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 90 93 28'): KALAN_P",
 "ölçüm aktör: 5:90 '{{1|adlı شَيْطان 12\\. sırada \\(gayb, rol mecrur\\)}}' — ''ameli' muzâfun ileyhi; 5:91 '{{2|adlı شَيْطان 3\\. sırada \\(gayb, rol fail\\)}}' — 'yurîdu' faili; 5:92 ve 5:93 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 5:90 emir, nida — VOC 1 'yâ' (1.), IMPV 1 'ctenibûhu' (13.); ölçüm biçim alanı '{{1|biçim DIKKAT}}' (yalnız bu maddede); "
 "5:91 soru — INTG 1 'hel' (18.); 5:92 emir, şart — COND 1 'in' (6.), IMPV 4 'atî'u' (1., 3.), 'hzerû' (5.), ''lemû' (8.); 5:93 haber — kip yok; "
 "morph REM ('fe' 5:90 13., 5:91 18., 5:92 6.; 've' 5:93 22.), RSLT ('fe' 5:92 8.), PREV ('mâ' 5:90 4., 5:91 1., 5:92 9.) ve SUP ('mâ' 5:93 11.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): bu blokta yıldız yok (5:90, 5:91, 5:92 ve 5:93 'yıldız yok')",
 "fâsıla: 5:89 ن (تشكرون) → 5:90 ن (تفلحون) → 5:91 ن (منتهون) → 5:92 ن (ٱلمبين) → 5:93 ن (ٱلمحسنين); blok içi kafiye değişmiyor; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6 — basılmamış hedefler sinifla sayısıyla): 5:90 xref yok; 5:91 5:14 (emsal olarak basıldı) ve okunmuş 2 ayet; 5:92 xref yok (esit2 BENZER 64:12, emsal olarak basıldı); 5:93 3:134 (emsal olarak basıldı) ve okunmuş 3 ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:90 'eyy ellezî âmene' süzgeç GEÇER; 5:91 'beyn 'adâve bağdâ'' GEÇER; 5:92 'fe-in tevellâ 'alime enne' GEÇER; 5:93 'ellezî âmene 'amile sâliha' GEÇER, 'allâh ahbeb muhsin' GEÇMEZ",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap' ile; alıntı ve kelime numarası ◇ konumuyla eş; fail olmayan mecrur çoğul ad ve mecrur ilgi zamiri A1'de yazılmaz — bölüm 11 denetimi kuralları 16 ve 19): "
 "5:90 hitap ('yâ eyyuhe'llezîne âmenû'), 3MP (adsız — 'âmenû'), şeytan (adlı gayb; mecrur), muhatap 2MP (adsız), 3MS (adsız — 'fe'ctenibûhu' mef'ûlü); "
 "5:91 şeytan (adlı gayb; 'yurîdu' faili — 3MS fiil uyumu), 3MS (adsız — 'yûqi'a', 'yesuddekum'), muhatap 2MP (adsız), Allah (lafız; mecrur), 'muntehûn' ('entum' haberi); "
 "5:92 muhatap 2MP (adsız), Allah (lafız), 'r-rasûle', 1P (adsız — 'rasûlina' iyelik, konuşan), 'l-belâğu'l-mubîn' ('enne' ismi); "
 "5:93 'leyse' (3MS fiil uyumu; ismi 'cunâhun'), 3MP (adsız — sekiz fiilin faili), Allah (lafız; 'yuhibbu' faili), 'l-muhsinîn' ('yuhibbu' mef'ûlü); "
 "5:93 ''ale'llezîne âmenû' — mecrur ilgi zamiri (''alâ' + 'ellezî' + ilgi cümlesi; §8, karar tam okuma sonunda) A1'de yazılmadı — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): bu blokta söz yok (A3 —); 'qul' yok (bölüm 10 denetimi kuralı 8); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 90 93 28' — A3 aralığında morph REM): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:90 've'l-meysiru' (6.), 've'l-ensâbu' (7.), 've'l-ezlâmu' (8.) CONJ, 'fe'ctenibûhu' (13.) REM; 5:91 've'l-bağdâ'e' (8.), 've'l-meysiri' (11.), 've yesuddekum' (12.), 've 'ani's-salâti' (16.) CONJ, 'fe-hel' (18.) REM; "
 "5:92 've atî'u' (1., 3.), 've'hzerû' (5.) CONJ, 'fe-in' (6.) REM, 'fe'lemû' (8.) RSLT; 5:93 5., 13., 14., 18. ve 21. kelimedeki 've' CONJ, 've'llâhu' (22.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): bu blokta tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 90 93 28'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:90 (2:219), 5:92 (64:12), 5:93 (3:134) (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); 5:91 D3 eşi yok; "
 "ayetler arası kalıp 'l-xamr… ve'l-meysir' (5:90, 5:91) — sayım 'say 5:90 5-6 --on' ve lemma dizisi 'dizi 5 90 5 6' / 'dizi 5 91 10 11'; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:90 hitap açılır; edim geçişi emir, şart → emir, nida; 5:91 edim geçişi emir, nida → soru; şahıs geçişi 2 → 3; 5:92 edim geçişi soru → emir, şart; şahıs geçişi 3 → 2; şart → cevap ('in' 6. kelime); "
 "5:93 bölüm kapanışı (bölüm 10 denetimi kuralı 2); edim geçişi emir, şart → haber; şahıs geçişi 2 → 3",
 "sözdizimi (okuma; morph etiketiyle): 5:90 'innemâ'l-xamru … ricsun' — hasr (morph ACC + PREV), mübteda dizisi ve haber; 'ctenibûhu' — emir (morph IMPV); 'le'allekum tuflihûn' — umut (morph ACC); "
 "5:91 'innemâ yurîdu'ş-şeytânu en yûqi'a' — hasr ve 'en' masdar (morph SUB); 'yesuddekum' — 'yûqi'a' üzerine atıf (morph CONJ); 'hel entum muntehûn' — soru (morph INTG); "
 "5:92 'in tevelleytum … 'lemû' — şart (morph COND) ve cevap (morph RSLT önekli); 'ennemâ 'alâ rasûlina'l-belâğu' — hasr (morph ACC + PREV); "
 "5:93 'leyse … cunâhun' — 'leyse' ve ismi; 'izâ me'ttaqav' — zaman şartı (morph T + SUP); 'summe' ile sıralı tekrar (morph CONJ); 've'llâhu yuhibbu'l-muhsinîn' — istînâf (morph REM)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:90 'yâ eyyuhe'llezîne âmenû' ile açılıyor; "
 "5:90 ve 5:91'de 'l-xamr… ve'l-meysir' (5:90 5-6., 5:91 10-11. kelime); 5:93 kök وقي ikilemesi 'ttaqav' (12., 17., 20. kelime), kök أمن ikilemesi 'âmenû' (4., 13., 18. kelime); 5:92 kök طوع ikilemesi 'atî'u' (1., 3. kelime)",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 28'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp): 'l-xamru ve'l-meysir' 5:90 'İçki, kumar' / 2:219 'içkiyi ve kumarı' (emsal metninde) — çakışma değil; "
 "'ve atî'u'llâhe ve atî'u'r-rasûl' 5:92 'Allah'a itaat edin, elçiye itaat edin' / 64:12 (emsal metninde) — meal birebir; 'ennemâ 'alâ rasûlina'l-belâğu'l-mubîn' 5:92 'açık tebliğ' / 64:12 'apaçık tebliğ' — karşılık farkı (tam okuma sonu); "
 "'ve'llâhu yuhibbu'l-muhsinîn' 5:93 / 3:134 'Allah iyilik edenleri sever' (emsal metninde) — çakışma değil",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 90 93 28'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:90, 5:91, 5:92 ve 5:93 tarayıcı vermedi (cipa_tarama5_adaylari.json); doğa iddiası yok (olgu=False); L3 / L4 adayı yok",
 "aday 1039: ayet içi 5:92 ('atî'u'llâhe' / 'tevelleytum') — okuma; 5:90, 5:91 ve 5:93 ayet içi karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök خمر ve يسر 5:90 ve 5:91'de ('l-xamr… ve'l-meysir' — yasak ve gerekçe); kök وقي 5:93'te üç kelimede sıralı ('ttaqav' 12., 17., 20. kelime); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 12-2 (bölüm 7 kuralı 9 — blok_plani_5.txt'ten) — bölüm iki blok (27, 28); bu blok bölümü kapatıyor; başlıktaki 'içki ve kumar' 5:90 ve 5:91; "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b28/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 90 93 28'; lem_bozuk.py 28 çıktısı): 5:90:13 'ctenebu', 5:91:5 'yûqi'a', 5:92:5 'yahzeru', 5:93:9 'ta'imu', 5:93:23 'ahbeb' — lem_bozuk bayrağı; meal maddesinde '(morph LEM ham biçim)' notlu; lemma adı listesinde notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 90 93 → AYN_SONUC; sunum/bolum4_kurallar.py 90 93 28 → KHATA_HEPSI; sunum/bolum5_kurallar.py 90 93 28 → B5_HEPSI; sunum/bolum6_kurallar.py 90 93 28 → B6_HEPSI; sunum/bolum7_kurallar.py 90 93 28 → B7_HEPSI; sunum/bolum8_kurallar.py 90 93 28 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 90 93 28 → B9_HEPSI; sunum/bolum10_kurallar.py 90 93 28 → B10_HEPSI; sunum/bolum11_kurallar.py 90 93 28 → B11_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 28 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('eyy', 'ellezî', 'âmene', 'xamr', 'meysir', 'beyn', ''adâve', 'bağdâ'', 'fe-in', 'tevellâ', ''alime', 'enne', ''amile', 'sâliha', 'allâh', 'ahbeb' (morph LEM ham biçim), 'muhsin'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (90, 93): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_90_93.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_5_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('06', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()
GERI = open('/home/claude/yamalar/geriye_donuk_5_b27.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    AYN = (run('/home/claude/sunum/ayn_kontrol.py', '90', '93').splitlines() or ['?'])[-1]
    KUR = run('/home/claude/sunum/bolum4_kurallar.py', '90', '93', '28').splitlines()
    KH = [l for l in KUR if l.startswith('HATA')]
    B5 = run('/home/claude/sunum/bolum5_kurallar.py', '90', '93', '28').splitlines()
    B5H = [l for l in B5 if l.startswith('HATA')]
    B6 = run('/home/claude/sunum/bolum6_kurallar.py', '90', '93', '28', '--tazelik-yok').splitlines()
    B7 = run('/home/claude/sunum/bolum7_kurallar.py', '90', '93', '28').splitlines()
    B8 = run('/home/claude/sunum/bolum8_kurallar.py', '90', '93', '28').splitlines()
    B9 = run('/home/claude/sunum/bolum9_kurallar.py', '90', '93', '28').splitlines()
    B10 = run('/home/claude/sunum/bolum10_kurallar.py', '90', '93', '28').splitlines()
    B11 = run('/home/claude/sunum/bolum11_kurallar.py', '90', '93', '28').splitlines()
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
           'MUT_SONUC': (MUT[-1] if MUT else '?'), 'GERI_P': ' / '.join(x.lstrip('# ') for x in GERI), 'B6_ESMA': ('; '.join(l[5:] for l in B6 if 'esmâ kural' in l and l.startswith('HATA')) or 'sapma 0')}
    I_cur = list(I_HAM)
    for k, v in REP.items(): I_cur = I_cur[:len(BEK)] + [x.replace(k, v) for x in I_cur[len(BEK):]]  # bölüm 9 kuralı 9: taşınan denetim maddelerine yer tutucu değişimi uygulanmaz
    I_cur[idx] = ("karşılık çakışması (bölüm 4 kuralı 4, bölüm 5 kuralı 3, bölüm 6 kuralı 2 — komut 'python3 sunum/cakisma.py' + sûre 5'in okunmuş bütün ARIZA dosyaları; bu bloğun karşılıklarına dokunan gruplar ve son dosyaya dokunan KÖK grupları; grup başına tam bir kapalı karar: 'çakışma değil' ya da 'çakışma — tam okuma sonu'): "
                  + ('; '.join(KARAR.get(l.split(' ←')[0].strip() if not l.startswith('KÖK') else 'KÖK ' + l.split()[1], l + ' — karar yok') for l in CAK_L) if CAK_L else 'bu bloğa dokunan çakışma yok'))
    if I_cur == onceki: break
    onceki = list(I_cur)
yaz(I_cur)
print('yazıldı', len(I_cur), 'tur', tur)
print('\n'.join(CAK_L))
print(GLS); print(KUR); print(B5); print(B6); print(B7); print(B8)

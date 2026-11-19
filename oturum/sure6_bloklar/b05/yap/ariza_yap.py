# sûre 6 blok 5 (6:20-24) ARIZA oluşturucu — bölüm 3-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b05/olcum.txt'
os.environ['SAY2'] = '/home/claude/b05/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_6_b04.txt', encoding='utf-8').read() + ']')
VF_YAZI_ESKI = {}
BOL = "'Yalanlayanların toplanma sahnesi; dünya hayatı oyun'"


def sd(key):
    return sayim.S2[key][1]


def sic(key):
    n, d = sayim.S2[key]
    return 1 + len([x for x in d['basilan'] if x.startswith('6:')]) + d['okunmus_si'] + d['henuz_si']


def taban(key, ay):
    n, d = sayim.S2[key]
    p = [ay] + [x for x in d['basilan'] if x.startswith('6:') and x != ay]
    if d['okunmus_si']: p.append('okunmus_si %d' % d['okunmus_si'])
    if d['henuz_si']: p.append('henuz_si %d' % d['henuz_si'])
    return ' + '.join(p)


R5 = [
 ("6:20", "'ellezî xasira nefs _ lâ âmene'", 2, 'say 6:20 8-13', "harekesiz 'ellezîne xasirû enfusehum fe-hum lâ yu'minûn' (8-13. kelime)", None),
 ("6:20", "'ellezî âtâ kitâb'", 2, 'say 6:20 1-3', "harekesiz 'ellezîne âteynâhumu'l-kitâb' (1-3. kelime)", None),
 ("6:21", "'men ezlem mimmen iftarâ 'alâ allâh kezib ev'", 2, 'say 6:21 1-8', "harekesiz 've men ezlemu mimmeni'fterâ 'alâ'llâhi keziben ev' (1-8. kelime)", None),
 ("6:21", "'ezlem mimmen iftarâ 'alâ allâh kezib'", 3, 'say 6:21 2-7', "harekesiz 'ezlemu mimmeni'fterâ 'alâ'llâhi keziben' (2-7. kelime)", None),
 ("6:21", "'inne lâ eflaha zâlim'", 2, 'say 6:21 11-14', "harekesiz 'innehû lâ yuflihu'z-zâlimûn' (11-14. kelime)", None),
 ("6:22", "'yevm haşera cemî''", 2, 'say 6:22 1-3', "harekesiz 've yevme nahşuruhum cemî'an' (1-3. kelime)", ('dizi 6 22 1 3', "yevm haşera cemî'", '1-3', "biçim farkı (dizi 6 22 1 3): basılmamış eş fiil çekimi")),
 ("6:24", "''an mâ kâne'", 2, 'say 6:24 7-9', "harekesiz ''anhum mâ kânû' (7-9. kelime)", None),
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

VF_YAZI = {20: {}, 21: {1: "'ve men'"}, 22: {1: "'ve yevme'"}, 23: {8: "'ve'llâhi'"}, 24: {6: "'ve dalle'"}}
sys.path.insert(0, '/home/claude/b05/yap')
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
open('/home/claude/b05/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '05')
BLOKLAR = [str(i) for i in range(1, 6)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '5', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b05/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '20', '24', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b05/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b05/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '20', '24', '05').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_20_24.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:20', '6:21', '6:22', '6:23', '6:24'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_20_24.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(20, 25))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:20 kök نفس ('enfusehum' 10. kelime — kendi): tetik listesinde yok; 6:22 kök جمع ('cemî'an' 3. kelime — hep birlikte): tetik listesinde yok; 6:24 kök نفس ('enfusihim' 5. kelime — kendi): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '20', '24', '05')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b05/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 6)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(20, 25))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: sunum/edat_etiket.py EDLEM'e 'eyne' (أين) — bölüm 15 denetimi kuralı 15: es_edat 6:22 'eyne' başlığını tanımıyordu; sunum/bolum18_kurallar.py — sûre 6 bölüm 2 denetimi kural 1-10 (bekleyen_ariza_6_b04 araç önerileri; ESMA_ADJ daraltıldı — morph ADJ söz türüdür, sözdizim rolü değil: kural 1 yalnız öncesi esmâ dışı belirli eş durumlu adda na't okumasını yakalar; elle kalanlar BAG_SAYIM_BASIM, KIP_KAPSAM, JOKER_TAM, SAPKA_NORM); "
 "mutasyon_sina var6 sınamaları ve geriye_donuk listesi bolum18 ile genişledi; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 127",
 "kök tablosu: ölçümde '???' 6:20-24 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 20 24 05'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: blokta esmâ yok (ölçüm 6:20-24); lafız 6:21 ve 6:23; Rab 6:23 (bölüm 6 kuralı 14 — betikle: B6_ESMA); esma_el kaydı yok; A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 20 24 05'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: 6:20 '{{1|fâsıla يؤمنون → ن, N sınıfı}}', '{{1|harf 70 → harf3 67, isaret 3}}' ve '{{1|dış düğüm 1}}'; "
 "6:21 '{{2|fâsıla ٱلظلمون → ن, N sınıfı}}', '{{2|harf 56 → harf3 53, isaret 3}}', '{{2|dış düğüm 2}}' ve '{{2|esit2 → 10:17 oran 0,9346 kademe BENZER}}'; "
 "6:22 '{{3|fâsıla تزعمون → ن, N sınıfı}}', '{{3|simetri \\[3, 4, 8, 1\\]}}', '{{3|harf 59 → harf3 57, isaret 2}}', '{{3|dış düğüm 3}}' ve '{{3|İÇ düğüm 1}}'; "
 "6:23 '{{4|fâsıla مشركين → ن, N sınıfı}}', '{{4|simetri \\[3, 1, 5, 1\\]}}', '{{4|harf 44 → harf3 43, isaret 1}}' ve '{{4|dış düğüm 2}}'; "
 "6:24 '{{5|fâsıla يفترون → ن, N sınıfı}}', '{{5|harf 44 → harf3 41, isaret 3}}' ve '{{5|dış düğüm 2}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 20 24 05'): KALAN_P",
 "ölçüm aktör: 6:20-24 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:20 haber — NEG 1 'lâ' (12.); 6:21 soru — INTG 1 'men' (1.), NEG 1 'lâ' (12.); "
 "6:22 soru — INTG 1 'eyne' (8.); 6:23 haber — NEG 2 'lem' (2.), 'mâ' (10.), RES 1 'illâ' (5.); 6:24 emir — IMPV 1 'unzur' (1.); "
 "morph REM ('ve' 6:21 1.; 6:22 1.), RSLT ('fe' 6:20 11.), ACC ('inne' 6:21 11.), SUB ('mâ' 6:20 5.; 'en' 6:23 6.), yemin 've' (6:23 8., morph P) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:20-24 yıldız yok",
 "fâsıla: 6:19 ن → 6:20 ن (يؤمنون) → 6:21 ن (ٱلظلمون) → 6:22 ن (تزعمون) → 6:23 ن (مشركين) → 6:24 ن (يفترون) — N sınıfı sürüyor; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:20 2:146 (emsal olarak basıldı); 6:21 10:17 (emsal olarak basıldı) ve okunmamış 1 ayet; "
 "6:22 10:28 (emsal olarak basıldı), okunmuş 3 ayet ve okunmamış 1 ayet (sûre içi 1); 6:23 okunmuş 2 ayet; 6:24 11:21 (emsal olarak basıldı) ve okunmamış 1 ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:20 'ellezî xasira nefs _ lâ âmene' süzgeç GEÇER, 'ellezî âtâ kitâb' GEÇMEZ; 6:21 'men ezlem mimmen iftarâ 'alâ allâh kezib ev', 'ezlem mimmen iftarâ 'alâ allâh kezib' ve 'inne lâ eflaha zâlim' GEÇER; "
 "6:22 'yevm haşera cemî'' GEÇMEZ; 6:24 ''an mâ kâne' GEÇMEZ; 6:23 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; edilgen fiil yok; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8): "
 "6:20 konuşan 1P, 3MP ve 3MS (adsız — gönderge 'ellezîne' ve 'l-kitâbe'); 6:21 3MS ('yuflihu' 13. kelime — fail 14. kelime; diğerleri adsız — gönderge 'men' ve lafız 6. kelime, 'innehû' şan zamiri); "
 "6:22 konuşan 1P, 3MP (adsız — gönderge 6:21 14. kelime ve 'li'llezîne'), muhatap 2MP (adsız; söz içi); 6:23 3FS ('tekun' 3. kelime — fail 4. kelime), 3MP (adsız — gönderge 6:22 7. kelime), konuşan 1P (adsız; söz içi); "
 "6:24 muhatap 2MS (adsız), 3MP (adsız — gönderge 6:23 7. kelime), 3MS ('dalle' — gönderge 'mâ') — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): "
 "6:22 'neqûlu' (5.) ardından söz 8-12. kelime; 6:23 'qâlû' (7.) ardından söz 8-12. kelime — ayet içi kapanışlar; 6:20, 6:21 ve 6:24 söz yok; mealde tırnaksız, iki nokta ile (blok meal biçimi); A3'te ve A4'te 'söz açılır' / 'söz kapanır'; "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 20 24 05' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 6:20 'fe-hum' (11.) RSLT; 6:21 've men' (1.) REM; 6:22 've yevme' (1.) REM; 6:23 've'llâhi' (8.) yemin edatı (morph P); 6:24 've dalle' (6.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:22 ◈K يوم ('yevme' 1. kelime — K2; anlam notu: toplanma günü)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 20 24 05'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:20 (2:146, 11:21); 6:21 (10:17); 6:22 (10:28); 6:24 (11:21); 6:23 D3 eşi yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "ayetler arası kalıp yok; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:20 şahıs geçişi 2 → 3, edim geçişi soru → haber, bölüm açılışı; 6:21 edim geçişi haber → soru; 6:22 söz açılır / kapanır (8-12. kelime), şahıs geçişi 3 → 2; "
 "6:23 söz açılır / kapanır (8-12. kelime), şahıs geçişi 2 → 3, edim geçişi soru → haber; 6:24 edim geçişi haber → emir; şart → cevap yok; şahıs beraberliği yok (sûre 6 bölüm 1 denetimi kuralı 9); ölçüm iltifât 6:20-24 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:20 'ellezîne âteynâhumu'l-kitâb' — ilgi cümlesi (morph REL); 'kemâ' — benzetme (morph SUB); 'fe-hum lâ yu'minûn' — sonuç (morph RSLT + NEG); "
 "6:21 'men ezlemu' — soru, üstünlük (morph INTG); 'innehû lâ yuflihu' — tekit, olumsuz (morph ACC + NEG); 6:22 'eyne' — soru (morph INTG); "
 "6:23 'lem tekun … illâ en qâlû' — kasr (morph NEG + RES); 've'llâhi' — yemin (morph P); 6:24 'unzur keyfe' — emir ve soru zarfı",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:20 'ellezîne âteynâhumu'l-kitâb' ile açılıyor — 2:146 ile eş (sayım: 'say 6:20 1-7'); "
 "6:20 'ellezîne xasirû enfusehum fe-hum lâ yu'minûn' — 6:12 ile eş (sayım: 'say 6:20 8-13'); 6:21 kök ظلم ve كذب ikilemesi; 6:21 've men ezlemu' ile açılıyor — 10:17 ile lemma dizisinde eş (sayım: 'dizi 6 21 1 13'); "
 "6:22 've yevme nahşuruhum cemî'an' ile açılıyor — 10:28 ile eş (sayım: 'say 6:22 1-3'); 6:24 'mâ kânû yefterûn' — 11:21 ile eş (sayım: 'say 6:24 8-10')",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 05'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 "'ellezîne âteynâhumu'l-kitâbe' 6:20 'Kendilerine kitap verdiklerimiz' / 2:146 'Kendilerine kitap verdiklerimiz' (emsal metninde) — çakışma değil; "
 "'ya'rifûnehû kemâ ya'rifûne ebnâ'ehum' 6:20 'onu, oğullarını tanıdıkları gibi tanırlar' / 2:146 'onu, oğullarını tanıdıkları gibi tanırlar' (emsal metninde) — çakışma değil; "
 "'xasirû enfusehum' 6:20 'ziyana uğratanlar' / 11:21 'ziyana uğratanlar' (emsal metninde) — çakışma değil; "
 "'ev kezzebe bi-âyâtih' 6:21 'yahut O'nun âyetlerini yalanlayandan' / 10:17 'yahut O'nun âyetlerini yalanlayandan' (emsal metninde) — çakışma değil; "
 "'kezzebe bi-âyâtih' 6:21 'O'nun âyetlerini yalanlayandan' / 10:17 'O'nun âyetlerini yalanlayandan' (emsal metninde) — çakışma değil; "
 "'ve yevme nahşuruhum cemî'an' 6:22 'Onları hep birlikte toplayacağımız gün' / 10:28 'Onları hep birlikte toplayacağımız gün' (emsal metninde) — çakışma değil; "
 "'summe neqûlu li'llezîne eşrakû' 6:22 'sonra ortak koşanlara' / 10:28 'ortak koşanlara' (emsal metninde) — çakışma — tam okuma sonu ('summe' emsal mealinde karşılıksız); "
 "'mâ kânû yefterûn' 6:24 'uydurdukları şeyler' / 11:21 'uydurdukları şeyler' (emsal metninde) — çakışma değil; "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:20 'âteynâ' PERF — meal geçmiş '-dik'; 'ya'rifûne' IMPF IND (4., 6.) — meal geniş zaman '-ırlar' / '-dıkları'; 'xasirû' PERF — meal sıfat-fiil '-anlar'; 'yu'minûn' IMPF IND — meal geniş zaman olumsuz; "
 "6:21 'iftarâ', 'kezzebe' PERF — meal sıfat-fiil '-an'; 'yuflihu' IMPF IND — meal geniş zaman olumsuz; 6:22 'nahşuru' IMPF IND — meal gelecek sıfat-fiil '-acağımız'; 'neqûlu' IMPF IND — meal gelecek '-eceğiz'; 'eşrakû' PERF — meal sıfat-fiil; 'kuntum tez'umûn' PERF + IMPF — meal süreklilik 'etmekte olduğunuz'; "
 "6:23 'lem tekun' IMPF JUS (lem ile geçmiş olumsuz) — meal kasr 'ancak … oldu'; 'qâlû' PERF — meal '-meleri'; 'kunnâ' PERF — meal geçmiş olumsuz 'olmadık'; "
 "6:24 'unzur' IMPV — meal emir; 'kezebû' PERF — meal geçmiş; 'dalle' PERF — meal '-muştur'; 'kânû yefterûn' PERF + IMPF — meal sıfat-fiil 'uydurdukları'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 20 24 05'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:20-24 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:20-24 ayet içi karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök كذب 6:21 ('keziben', 'kezzebe') ve 6:24 ('kezebû') — yalan bağı; kök فري 6:21 ('fterâ') ve 6:24 ('yefterûn') — uydurma bağı; kök شرك 6:22 ve 6:23 ('eşrakû', 'şurakâ'ukumu', 'muşrikîn'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 3-1 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm üç blok (5, 6, 7); "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b05/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 20 24 05'; lem_bozuk.py 05 çıktısı): lem_bozuk bayrağı yok; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 20 24 → AYN_SONUC; sunum/bolum4_kurallar.py 20 24 05 → KHATA_HEPSI; sunum/bolum5_kurallar.py 20 24 05 → B5_HEPSI; sunum/bolum6_kurallar.py 20 24 05 → B6_HEPSI; sunum/bolum7_kurallar.py 20 24 05 → B7_HEPSI; sunum/bolum8_kurallar.py 20 24 05 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 20 24 05 → B9_HEPSI; sunum/bolum10_kurallar.py 20 24 05 → B10_HEPSI; sunum/bolum11_kurallar.py 20 24 05 → B11_HEPSI; sunum/bolum12_kurallar.py 20 24 05 → B12_HEPSI; sunum/bolum13_kurallar.py 20 24 05 → B13_HEPSI; sunum/bolum14_kurallar.py 20 24 05 → B14_HEPSI; sunum/bolum15_kurallar.py 20 24 05 → B15_HEPSI; sunum/bolum16_kurallar.py 20 24 05 → B16_HEPSI; sunum/bolum17_kurallar.py 20 24 05 → B17_HEPSI; sunum/bolum18_kurallar.py 20 24 05 → B18_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 5 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('ellezî', 'âtâ', 'kitâb', 'xasira', 'nefs', 'lâ', 'âmene', 'men', 'ezlem', 'mimmen', 'iftarâ', ''alâ', 'allâh', 'kezib', 'ev', 'inne', 'eflaha', 'zâlim', 'yevm', 'haşera', 'cemî'', 'dalle', ''an', 'mâ', 'kâne'); lemmasız öğe joker '_' ('hum'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (20, 24): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_20_24.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b05.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '20', '24'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '20', '24', '05'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '20', '24', '05'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '20', '24', '05', '--tazelik-yok')}
    for _n in range(7, 19): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '20', '24', '05')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18 = [_R['B%d' % _n].splitlines() for _n in range(6, 19)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
           'MUT_SONUC': (MUT[-1] if MUT else '?'), 'GERI_P': ' / '.join(x.lstrip('# ') for x in GERI), 'B6_ESMA': ('; '.join(l[5:] for l in B6 if 'esmâ kural' in l and l.startswith('HATA')) or 'sapma 0')}
    I_cur = list(I_HAM)
    for k, v in REP.items(): I_cur = I_cur[:len(BEK)] + [x.replace(k, v) for x in I_cur[len(BEK):]]  # bölüm 9 kuralı 9: taşınan denetim maddelerine yer tutucu değişimi uygulanmaz
    I_cur[idx] = ("karşılık çakışması (bölüm 4 kuralı 4, bölüm 5 kuralı 3, bölüm 6 kuralı 2 — komut 'python3 sunum/cakisma.py' + sûre 6'nın okunmuş bütün ARIZA dosyaları; bu bloğun karşılıklarına dokunan gruplar ve son dosyaya dokunan KÖK grupları; grup başına tam bir kapalı karar: 'çakışma değil' ya da 'çakışma — tam okuma sonu'): "
                  + ('; '.join(KARAR.get(l.split(' ←')[0].strip() if not l.startswith('KÖK') else 'KÖK ' + l.split()[1], l + ' — karar yok') for l in CAK_L) if CAK_L else 'bu bloğa dokunan çakışma yok'))
    if I_cur == onceki: break
    onceki = list(I_cur)
yaz(I_cur)
print('yazıldı', len(I_cur), 'tur', tur)
print('\n'.join(CAK_L))
print(GLS)
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18): print([l for l in _x if l.startswith('HATA') or 'hata' in l])

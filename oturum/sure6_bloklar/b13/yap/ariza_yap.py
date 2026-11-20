# sûre 6 blok 13 (6:54-58) ARIZA oluşturucu — bölüm 6-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b13/olcum.txt'
os.environ['SAY2'] = '/home/claude/b13/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {}
BOL = "'De ki: gaybı bilmem; sabah akşam Rablerine dua edenler'"


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
 ("6:54", "''alâ nefs rahme'", 2, 'say 6:54 11-13', "harekesiz ''alâ nefsihi'r-rahme' (11-13. kelime)", None),
 ("6:56", "'ellezî de'â min dûn allâh'", 2, 'say 6:56 6-10', "harekesiz 'llezîne ted'ûne min dûni'llâh' (6-10. kelime)", ('dizi 6 56 6 10', "ellezî de'â min dûn allâh", '6-10', "biçim farkı (dizi 6 56 6 10): basılmamış eş fiil çekimi, zamir eki")),
 ("6:56", "'de'â min dûn allâh'", 3, 'say 6:56 7-10', "harekesiz 'ted'ûne min dûni'llâh' (7-10. kelime)", ('dizi 6 56 7 10', "de'â min dûn allâh", '7-10', "biçim farkı (dizi 6 56 7 10): basılmamış eş fiil çekimi, zamir eki, önek; basılmamış eş fiil çekimi, zamir eki")),
 ("6:56", "'min dûn allâh'", 4, 'say 6:56 8-10', "harekesiz 'min dûni'llâh' (8-10. kelime)", None),
 ("6:56", "'lâ ittebe ehvâ''", 2, 'say 6:56 12-14', "harekesiz 'lâ ettebi'u ehvâ'akum' (12-14. kelime)", ('dizi 6 56 12 14', "lâ ittebe ehvâ'", '12-14', "biçim farkı (dizi 6 56 12 14): basılmamış eş fiil çekimi, zamir eki, önek")),
 ("6:56", "'mâ ene min'", 2, 'say 6:56 18-20', "harekesiz 've mâ ene mine' (18-20. kelime)", None),
 ("6:57", "'beyyine min rabb'", 2, 'say 6:57 4-6', "harekesiz 'beyyinetin min rabbî' (4-6. kelime)", ('dizi 6 57 4 6', "beyyine min rabb", '4-6', "biçim farkı (dizi 6 57 4 6): basılmamış eş zamir eki")),
 ("6:57", "''ind mâ ista'cele _'", 2, 'say 6:57 10-13', "harekesiz ''indî mâ testa'cilûne bih' (10-13. kelime)", None),
 ("6:58", "''ind mâ ista'cele _'", 2, 'say 6:58 4-7', "harekesiz ''indî mâ testa'cilûne bih' (4-7. kelime)", None),
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

K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k and not (k + ' --medde' in sayim.S2 and sayim.S2[k + ' --medde'][0] != n)}  # sûre 6 bölüm 5 denetimi kuralı 6 (TEKIL_MEDDE)

VF_YAZI = {54: {1: "'ve izâ'", 6: "'fe-qul'", 24: "'ve asleha'", 25: "'fe-ennehû'"}, 55: {1: "'ve kezâlike'", 4: "'ve li-testebîne'"}, 56: {18: "'ve mâ'"}, 57: {7: "'ve kezzebtum'", 20: "'ve huve'"}, 58: {11: "'ve beynekum'", 12: "'ve'llâhu'"}}
sys.path.insert(0, '/home/claude/b13/yap')
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
open('/home/claude/b13/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '13')
BLOKLAR = [str(i) for i in range(1, 14)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '13', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b13/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '54', '58', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b13/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b13/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '54', '58', '13').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_54_58.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:54', '6:55', '6:56', '6:57', '6:58'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_54_58.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(54, 59))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:54 'izâ' (1. kelime — morph T, zaman); 6:54 kök نفس ('nefsihi' 12. kelime — kendi), kök سوأ ('sû'en' 18. kelime — kötülük), kök بعد ('ba'dihî' 23. kelime — ard): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '54', '58', '13')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b13/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 14)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(54, 59))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: sunum/bolum8_kurallar.py kural 5 AYRI kümesine 'ene' (أَنا) / 'enne' (أَنّ) — yazım eşdeğeri iskeletinde ayrı lemmalar (sûre 6 blok 13); mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 177",
 "kök tablosu: ölçümde '???' 6:54-58 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 54 58 13'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:54 'fe-qul selâmun 'aleykum' (6-8. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (selamlama); 6:54 'fe-ennehû ğafûrun rahîm' (25-27. kelime) — esma_el 'ilahi', kural ''inne/enne' haberi' (Allah); 6:55, 6:56, 6:57 ve 6:58 esmâ yok; "
 "lafız 6:56, 6:57 ve 6:58; Rab 6:54 ve 6:57 (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 54 58 13'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: 6:54 '{{1|fâsıla رحيم → م, N sınıfı}}', '{{1|simetri \\[3, 1, 15, 1\\]}}', '{{1|harf 116 → harf3 106, isaret 10}}' ve '{{1|dış düğüm 2}}'; "
 "6:55 '{{2|fâsıla ٱلمجرمين → ن, N sınıfı}}', '{{2|harf 35 → harf3 35, isaret 0}}' ve '{{2|dış düğüm 0}}'; "
 "6:56 '{{3|fâsıla ٱلمهتدين → ن, N sınıfı}}', '{{3|simetri \\[3, 1, 11, 1\\]}}', '{{3|harf 78 → harf3 74, isaret 4}}', '{{3|dış düğüm 1}}' ve '{{3|EDİLGEN 1/7 fiil, pas z=0,48}}'; "
 "6:57 '{{4|fâsıla ٱلفصلين → ن, N sınıfı}}', '{{4|simetri \\[4, 2, 8, 1\\]}}', '{{4|harf 83 → harf3 76, isaret 7}}', '{{4|dış düğüm 0}}' ve '{{4|biçim HASR}}'; "
 "6:58 '{{5|fâsıla بٱلظلمين → ن, N sınıfı}}', '{{5|harf 60 → harf3 58, isaret 2}}', '{{5|dış düğüm 1}}' ve '{{5|EDİLGEN 1/3 fiil, pas z=1,57}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 54 58 13'): KALAN_P",
 "ölçüm aktör: 6:54-58 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:54 emir, şart — COND 1 'men' (15.), IMPV 1 'fe-qul' (6.); 6:55 haber — kip yok; "
 "6:56 emir — CERT 1 'qad' (15.), IMPV 2 'qul' (1., 11.), NEG 2 'lâ' (12.), 've mâ' (18.); 6:57 emir — IMPV 1 'qul' (1.), NEG 2 'mâ' (9.), 'in' (14.), RES 1 'illâ' (16.); 6:58 emir, şart — COND 1 'lev' (2.), EMPH 1 'le-qudiye' (8.), IMPV 1 'qul' (1.); "
 "morph ACC ('enne' 6:54 14., 25.; 'inne' 6:56 2.; 'inne' 6:57 2.; 'enne' 6:58 3.), T ('izâ' 6:54 1.), RSLT ('fe' 6:54 6., 25.), SUB ('en' 6:56 4.), ANS ('izen' 6:56 17.), PRP ('li' 6:55 4.), REM ('ve' 6:54 1.; 've' 6:55 1.; 've' 6:56 18.; 've' 6:57 20.; 've' 6:58 12.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:54 ★ (kaynak n, z=1,55); 6:58 ★ (kaynak pas, z=1,57); 6:55, 6:56 ve 6:57 yıldız yok",
 "fâsıla: 6:53 ن → 6:54 م (رحيم) → 6:55 ن (ٱلمجرمين) → 6:56 ن (ٱلمهتدين) → 6:57 ن (ٱلفصلين) → 6:58 ن (بٱلظلمين) — N sınıfı sürüyor; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:54 16:119 (emsal olarak basıldı) ve okunmuş 1 ayet; 6:56 40:66 (emsal olarak basıldı); 6:58 okunmuş 1 ayet; 6:55 xref yok; 6:57 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:54 ''alâ nefs rahme' süzgeç GEÇMEZ; 6:56 'ellezî de'â min dûn allâh', 'de'â min dûn allâh' ve 'min dûn allâh' süzgeç GEÇER, 'lâ ittebe ehvâ'' ve 'mâ ene min' GEÇMEZ; "
 "6:57 ''ind mâ ista'cele _' süzgeç GEÇER, 'beyyine min rabb' GEÇMEZ; 6:58 ''ind mâ ista'cele _' süzgeç GEÇER; 6:55 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; edilgen fiilde naib-i faili zamir 'adsız' ile — sûre 6 bölüm 2 denetimi kuralı 5; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; gönderge rol adıyla yazılmaz — sûre 6 bölüm 4 denetimi kuralı 4): "
 "6:54 konuşan 1P, muhatap 2MS, muhatap 2MP (söz içi), 3MS ('câ'eke' 2. kelime — fail 3. kelime; 'ketebe' 9. kelime — fail 10. kelime; zamirler adsız — gönderge 'rabbukum', 'men' ve 'sû'en'), 3MP (adsız — gönderge 'llezîne' 3. kelime); "
 "6:55 konuşan 1P, 3FS ('li-testebîne' 4. kelime — fail 5. kelime); "
 "6:56 muhatap 2MS, konuşan 1S (söz içi; 'nuhîtu' edilgen — naib-i faili zamir), muhatap 2MP (söz içi); "
 "6:57 muhatap 2MS, konuşan 1S (söz içi), muhatap 2MP (söz içi), 3MS (adsız — gönderge 'rabbî', 'mâ' ve 'li'llâh'); "
 "6:58 muhatap 2MS, konuşan 1S (söz içi), muhatap 2MP (söz içi), 3MS (adsız — gönderge 'mâ' 5. kelime; 'le-qudiye' edilgen — naib-i faili 'l-emru' 9. kelime) — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): "
 "6:54 'fe-qul' (6.) ardından söz 7-27. kelime — ayet içi kapanış; 6:56 'qul' (1.) ardından söz 2-10. kelime, 'qul' (11.) ardından söz 12-21. kelime (REM sapması 6:56 (18. kelime) — 've mâ ene' söz içinde istînâf, konuşan 1S sürer, söz 21. kelimeye dek sürer) — ayet içi kapanışlar; 6:57 'qul' (1.) ardından söz 2-19. kelime — 've huve' (20.) REM ile kapanış; "
 "6:58 'qul' (1.) ardından söz 2-11. kelime — 've'llâhu' (12.) REM ile kapanış; 6:55 söz yok; mealde tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 54 58 13' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 6:54 've izâ' (1.) REM, 'fe-qul' (6.), 'fe-ennehû' (25.) RSLT, 've asleha' (24.) CONJ; 6:55 've kezâlike' (1.) REM, 've li-testebîne' (4.) CONJ; 6:56 've mâ' (18.) REM; 6:57 've kezzebtum' (7.) CONJ, 've huve' (20.) REM; 6:58 've beynekum' (11.) CONJ, 've'llâhu' (12.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): blokta tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 54 58 13'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:54 (16:119); 6:56 (40:66); 6:55, 6:57 ve 6:58 D3 eşi yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "ayetler arası kalıp ''indî mâ testa'cilûne bih' (6:57, 6:58) — sayım 'dizi 6 57 10 13', 'dizi 6 58 4 7'; blok içi tekrar (bölüm 9 kuralı 6), ardışık bağ yerine sayımla kayıt; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:54 şart → cevap ('men' 15. kelime / 'fe-ennehû ğafûrun rahîm' 25. kelime), söz açılır / kapanır (7-27. kelime), şahıs geçişi yok, edim geçişi soru → emir, şart; 6:55 şahıs geçişi 3 → 1, edim geçişi emir, şart → haber, şahıs sayısında beraberlik (1P 1 · 3FS 1); "
 "6:56 söz açılır / kapanır (2-10. ve 12-21. kelime), şahıs geçişi yok, edim geçişi haber → emir; 6:57 söz açılır / kapanır (2-19. kelime), şahıs geçişi 1 → 2, edim geçişi yok; "
 "6:58 şart → cevap ('lev' 2. kelime / 'le-qudiye'l-emru' 8. kelime), söz açılır / kapanır (2-11. kelime), şahıs geçişi yok, edim geçişi emir → emir, şart, bölüm kapanışı; "
 "şahıs beraberliği 6:55 (sûre 6 bölüm 1 denetimi kuralı 9); ölçüm iltifât 6:54-58 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:54 've izâ câ'eke' — istînâf ve zaman şartı (morph REM + T); 'fe-qul' — şartın cevabı (morph RSLT); 'men 'amile' — şart (morph COND); 'fe-ennehû' — cevap (morph RSLT); "
 "6:55 've kezâlike' — istînâf (morph REM); 've li-testebîne' — takdirli amaca atıf (morph CONJ + PRP); "
 "6:56 'en a'bude' — masdar cümleciği (morph SUB); 'qad dalaltu izen' — cevap (morph CERT + ANS); 've mâ ene' — istînâf ve nefy (morph REM + NEG); "
 "6:57 'ini'l-hukmu illâ li'llâh' — hasr (morph NEG + RES); 've huve' — istînâf (morph REM); "
 "6:58 'lev enne' — şart (morph COND); 'le-qudiye' — cevap lâmı (morph EMPH); 've'llâhu' — istînâf (morph REM)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:54 'sû'en bi-cehâletin summe tâbe min ba'dihî' — 16:119 ile lemma dizisi eşi (sayım: 'dizi 6 54 18 23'); 6:54 kök رحم ikilemesi; "
 "6:56 'qul innî nuhîtu en a'bude'llezîne ted'ûne min dûni'llâh' — 40:66 ile eş (sayım: 'say 6:56 1-10'); 6:56 kök قول ikilemesi; 6:57 ve 6:58 ''indî mâ testa'cilûne bih' ortak (sayım: 'say 6:57 10-13'); 6:58 kök بين ikilemesi",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 13'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 ""
 "'ğafûrun rahîm' 6:54 'bağışlayandır, merhamet edendir' / 16:119 'çok bağışlayan, çok merhamet edendir' (emsal metninde) — çakışma — tam okuma sonu ('çok' pekiştirmesi emsal mealinde); 'qul innî nuhîtu en a'bude'llezîne ted'ûne min dûni'llâh' 6:56 'Allah'ı bırakıp dua ettiklerinize kulluk etmekten men edildim' / 40:66 'Allah'ı bırakıp dua ettiklerinize kulluk etmekten men edildim' (emsal metninde) — çakışma değil; "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:54 'câ'eke' PERF — meal 'geldiği zaman'; 'yu'minûne' IMPF IND — meal 'iman eden'; 'fe-qul' IMPV — meal 'de'; 'ketebe' PERF — meal 'yazdı'; ''amile' PERF (şart) — meal 'işler'; 'tâbe' PERF (şart) — meal 'tövbe eder'; 'asleha' PERF (şart) — meal 'düzeltirse'; "
 "6:55 'nufassilu' IMPF IND — meal 'açıklarız'; 'testebîne' IMPF SUBJ — meal 'belli olsun'; "
 "6:56 'qul' IMPV — meal 'De'; 'nuhîtu' PERF edilgen — meal 'men edildim'; 'a'bude' IMPF SUBJ — meal 'kulluk etmek'; 'ted'ûne' IMPF IND — meal 'dua ettikleriniz'; 'ettebi'u' IMPF IND — meal 'uymam'; 'dalaltu' PERF — meal 'sapmış olurum'; "
 "6:57 'qul' IMPV — meal 'De'; 'kezzebtum' PERF — meal 'yalanladınız'; 'testa'cilûne' IMPF IND — meal 'acele istediğiniz'; 'yequssu' IMPF IND — meal 'söyler'; "
 "6:58 'qul' IMPV — meal 'De'; 'testa'cilûne' IMPF IND — meal 'acele istediğiniz'; 'qudiye' PERF edilgen — meal 'bitirilmiş olurdu'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 54 58 13'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:54, 6:55, 6:56, 6:57 ve 6:58 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:54 ('sû'en' / 've asleha'); 6:56 ('dalaltu' / 'l-muhtedîn'); 6:58 ('beynî' / 've beynekum'); 6:55 yok; 6:57 yok; "
 "ayetler arası çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök دعو 6:52 ('yed'ûne') ve 6:56 ('ted'ûne'); kök ظلم 6:52 ('z-zâlimîn') ve 6:58 ('bi'z-zâlimîn'); kök علم 6:53 ('bi-a'leme') ve 6:58 ('a'lemu'); kök عند 6:50 (''indî'), 6:57 (''indî') ve 6:58 (''indî'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 6-2 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm iki blok (12, 13); bu blok bölümü kapatıyor; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b13/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 54 58 13'; lem_bozuk.py 13 çıktısı): lem_bozuk bayrağı yok; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 54 58 → AYN_SONUC; sunum/bolum4_kurallar.py 54 58 13 → KHATA_HEPSI; sunum/bolum5_kurallar.py 54 58 13 → B5_HEPSI; sunum/bolum6_kurallar.py 54 58 13 → B6_HEPSI; sunum/bolum7_kurallar.py 54 58 13 → B7_HEPSI; sunum/bolum8_kurallar.py 54 58 13 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 54 58 13 → B9_HEPSI; sunum/bolum10_kurallar.py 54 58 13 → B10_HEPSI; sunum/bolum11_kurallar.py 54 58 13 → B11_HEPSI; sunum/bolum12_kurallar.py 54 58 13 → B12_HEPSI; sunum/bolum13_kurallar.py 54 58 13 → B13_HEPSI; sunum/bolum14_kurallar.py 54 58 13 → B14_HEPSI; sunum/bolum15_kurallar.py 54 58 13 → B15_HEPSI; sunum/bolum16_kurallar.py 54 58 13 → B16_HEPSI; sunum/bolum17_kurallar.py 54 58 13 → B17_HEPSI; sunum/bolum18_kurallar.py 54 58 13 → B18_HEPSI; sunum/bolum19_kurallar.py 54 58 13 → B19_HEPSI; sunum/bolum20_kurallar.py 54 58 13 → B20_HEPSI; sunum/bolum21_kurallar.py 54 58 13 → B21_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 13 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla (''alâ', 'nefs', 'rahme', 'sû'', 'cehâle', 'summe', 'tâbe', 'min', 'ba'd', 'ellezî', 'de'â', 'dûn', 'allâh', 'lâ', 'ittebe', 'ehvâ'', 'mâ', 'ene', 'beyyine', 'rabb', ''ind', 'ista'cele'); lemmasız öğe joker yok; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (54, 58): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_54_58.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b11.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '54', '58'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '54', '58', '13'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '54', '58', '13'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '54', '58', '13', '--tazelik-yok')}
    for _n in range(7, 22): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '54', '58', '13')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21 = [_R['B%d' % _n].splitlines() for _n in range(6, 22)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21): print([l for l in _x if l.startswith('HATA') or 'hata' in l])

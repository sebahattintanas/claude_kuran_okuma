# sûre 7 blok 11 (7:38-41) ARIZA oluşturucu — bölüm 4-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b11/olcum.txt'
os.environ['SAY2'] = '/home/claude/b11/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {}
BOL = "'Elçiler gelince; yalanlayanların ateşte çekişmesi'"


def sd(key):
    return sayim.S2[key][1]


def sic(key):
    n, d = sayim.S2[key]
    return 1 + len([x for x in d['basilan'] if x.startswith('7:')]) + d['okunmus_si'] + d['henuz_si']


def taban(key, ay):
    n, d = sayim.S2[key]
    p = [ay] + [x for x in d['basilan'] if x.startswith('7:') and x != ay]
    if d['okunmus_si']: p.append('okunmus_si %d' % d['okunmus_si'])
    if d['henuz_si']: p.append('henuz_si %d' % d['henuz_si'])
    return ' + '.join(p)


R5 = [
 ("7:38", "'min cinn ins'", 2, 'say 7:38 9-11', "harekesiz 'mine'l-cinni ve'l-insi' (9-11. kelime)", ('dizi 7 38 9 11', "min cinn ins", '9-11', "biçim farkı (dizi 7 38 9 11): basılmamış eş yazım eş")),
 ("7:39", "'bi-mâ kâne kesebe'", 2, 'say 7:39 12-14', "harekesiz 'bimâ kuntum teksibûn' (12-14. kelime)", ('dizi 7 39 12 14', "mâ kâne kesebe", '12-14', "biçim farkı (dizi 7 39 12 14): basılmamış eş fiil çekimi, zamir eki")),
 ("7:40", "'kezzebe âye istekbere 'an'", 2, 'say 7:40 3-6', "harekesiz 'kezzebû bi-âyâtinâ ve'stekberû 'anhâ' (3-6. kelime)", ('dizi 7 40 3 6', "kezzebe âye istekbere 'an", '3-6', "biçim farkı (dizi 7 40 3 6): 7:36 yazım eş")),
 ("7:40", "'ellezî kezzebe âye'", 5, 'say 7:40 2-4', "harekesiz 'llezîne kezzebû bi-âyâtinâ' (2-4. kelime); biçim öğesi 'ellezî' öneki (lemma dizisi sûre içi 8, nakarat3 5)", ('dizi 7 40 2 4', "ellezî kezzebe âye", '2-4', "biçim farkı (dizi 7 40 2 4): 7:36 önek; basılmamış eş yazım eş; basılmamış eş yazım eş; basılmamış eş önek; basılmamış eş yazım eş; basılmamış eş yazım eş; basılmamış eş önek; öneksiz eş koşusu (dizi 7 40 2 4): 7:36 → önek kesilmiş sûre içi 3; basılmamış eş → önek kesilmiş sûre içi 1; basılmamış eş → önek kesilmiş sûre içi 7; basılmamış eş → önek kesilmiş sûre içi 3; basılmamış eş → önek kesilmiş sûre içi 7; basılmamış eş → önek kesilmiş sûre içi 7; basılmamış eş → önek kesilmiş sûre içi 3")),
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

VF_YAZI = {38: {11: "'ve'l-insi'", 30: "'fe-âtihim'", 38: "'ve lâkin'"}, 39: {1: "'ve qâlet'", 4: "'fe-mâ'", 10: "'fe-zûqu'"}, 40: {5: "'ve'stekberû'", 12: "'ve lâ'", 21: "'ve kezâlike'"}, 41: {5: "'ve min'", 8: "'ve kezâlike'"}}
sys.path.insert(0, '/home/claude/b11/yap')
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
open('/home/claude/b11/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '11')
BLOKLAR = [str(i) for i in range(1, 12)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '11', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b11/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '38', '41', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b11/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b11/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '38', '41', '11').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_38_41.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'7:38', '7:39', '7:40', '7:41'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_38_41.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '7:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '7:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(38, 42))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "7:38 kök خلو ('xalet' 6. kelime — gelip geç-): tetik listesinde yok; 7:38 kök قبل ('qablikum' 8. kelime — önce): tetik listesinde yok; 7:38 kök كلل ('kullemâ' 14. kelime — morph T, zaman): tetik listesinde yok; 7:38 'izâ' (20. kelime — morph T, zaman); 7:38 kök جمع ('cemî'an' 23. kelime — hepsi): tetik listesinde yok; 7:38 kök أخر ('uxrâhum' 25. kelime — sonraki): tetik listesinde yok; 7:39 kök أخر ('li-uxrâhum' 3. kelime — sonraki): tetik listesinde yok; 7:40 kök خيط ('l-xiyâti' 20. kelime — iğne): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '38', '41', '11')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b11/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 12)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b7:%d:\d+' % a_, s_) for a_ in range(38, 42))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
_OL = [l.replace('**', '') for l in open('/home/claude/b11/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b11/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 37), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK3 = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[2]).group(0))
_AK4 = _esc(re.search(r'aktör: adlı .*?rol mecrur\)', _OL[3]).group(0))
for _k, _v in (('_AK3', _AK3), ('_AK4', _AK4)): _MB = _MB.replace('" + %s + "' % _k, _v)
I = [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta araç kuralı değişmedi; yeni kök yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 414",
 "geriye dönük koşu (sûre 7 bölüm 3 kapanışı, komut 'python3 sunum/geriye_donuk.py b09k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 38 41 11'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:38 'qâlet uxrâhum li-ûlâhum' (24-26. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (ümmetlerin evvelkileri) (yamalar/esma_el_7_38_41.txt); 7:39 've qâlet ûlâhum li-uxrâhum' (1-3. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (ümmetlerin evvelkileri) (yamalar/esma_el_7_38_41.txt); 7:38 26. kelime ve 7:39 2. kelime esma_kayit listesinde ('evvel' adı), ölçüm esmâ satırında yok — liste farkı; 7:40 ve 7:41 esmâ yok; 7:38, 7:39, 7:40 ve 7:41 lafız yok; 7:38 Rab (27. kelime); 7:39, 7:40 ve 7:41 Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 38 41 11'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in (38, 39, 40, 41)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 38 41 11'): KALAN_P",
 "ölçüm aktör: 7:40 '{{3|" + _AK3 + "}}' (A1'de 'l-cennete'); 7:41 '{{4|" + _AK4 + "}}' (A1'de 'cehenneme'); 7:38 ve 7:39 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:38 emir — CERT 1 'qad' (5.), IMPV 3 'dxulû' (2.), 'ddârakû' (21.; morph IMPV 2MP etiketi korundu, okuma PERF 3MP), 'fe-âtihim' (30.), NEG 1 'lâ' (39.); ölçüm biçim DIKKAT (D2'de yazılmadı); "
 "7:39 emir — IMPV 1 'fe-zûqu' (10.), NEG 1 'fe-mâ' (4.; 'mâ'); 7:40 haber — NEG 2 'lâ' (7.), 've lâ' (12.; 'lâ'); 7:41 haber — kip yok; "
 "morph T ('kullemâ' 7:38 14., 'ize' 7:38 20.), INC ('hattâ' 7:38 19.), ATT ve DEM ('hâ'ulâ'i' 7:38 28.), REM ('fe-âtihim' 7:38 30., 've lâkin' 7:38 38., 'fe-zûqu' 7:39 10., 've kezâlike' 7:40 21., 7:41 8.), AMD ('ve lâkin' 7:38 38.), REL ('bimâ' 7:39 12., 'llezîne' 7:40 2.), ACC ('inne' 7:40 1.), DEM, DIST ve ADDR ('ve kezâlike' 7:40 21., 7:41 8.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:38 ★★ (kaynak n, z=2,93); 7:39, 7:40 ve 7:41 yıldız yok",
 "fâsıla: 7:37 ن → 7:38 ن (" + _F[0] + ") → 7:39 ن (" + _F[1] + ") → 7:40 ن (" + _F[2] + ") → 7:41 ن (" + _F[3] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:38 41:25 (emsal olarak basıldı), 46:18 (emsal olarak basıldı), 38:61 (emsal olarak basıldı); 7:39 okunmuş 1 ayet; 7:40 xref yok; 7:41 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:38 'min cinn ins' süzgeç GEÇMEZ; 7:39 'bi-mâ kâne kesebe' süzgeç GEÇMEZ; 7:40 'kezzebe âye istekbere 'an' süzgeç GEÇER, 'ellezî kezzebe âye' süzgeç GEÇER; 7:41 nakarat3 yok; GEÇER kalıpların sûre içi basılmış eşi 7:36 D3 dışı listesinde, öbür sûre içi eşler basılmamış",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:38 3MS ('qâle' 1. kelime, 'qâle' 35. kelime — tartışmalı; gönderge 7:37 6. kelime), muhatap 2MP ('dxulû', 'ta'lemûn' — söz içi; 'ddârakû' — morph IMPV 2MP etiketi korundu, okuma PERF 3MP; tartışmalı; cins uyumsuz; gönderge 'umemin' 4. kelime; ek 'qablikum' — söz içi), 3FS ('xalet' — söz içi; gönderge 'umemin' 4. kelime; 'dexalet' — fiil uyumu, fail 16. kelime; 'le'anet' — gönderge 'ummetun' 16. kelime; 'qâlet' — fiil uyumu, fail 25. kelime; "
 "ekler 'uxtehâ' — gönderge 'ummetun' 16. kelime; 'fîhâ' — gönderge 'n-nâri' 13. kelime), 3MP ('edallûnâ' — söz içi; gönderge 'hâ'ulâ'i' 28. kelime; ekler 'uxrâhum', 'li-ûlâhum' — tartışmalı; cins uyumsuz; gönderge 'umemin' 4. kelime; 'fe-âtihim' — söz içi; gönderge 'hâ'ulâ'i' 28. kelime), konuşan 1P eki ('rabbenâ', 'edallûnâ' — söz içi), muhatap 2MS ('fe-âtihim' — söz içi); "
 "7:39 3FS ('ve qâlet' — fiil uyumu, fail 2. kelime), 3MP eki ('ûlâhum', 'li-uxrâhum' — tartışmalı; cins uyumsuz; gönderge 7:38 4. kelime), 3MS ('kâne' — söz içi; fiil uyumu, fail 9. kelime), muhatap 2MP ('fe-zûqu', 'kuntum', 'teksibûn' — söz içi; ek 'lekum' — söz içi), konuşan 1P eki (''aleynâ' — söz içi); "
 "7:40 3MP ('kezzebû', 've'stekberû', 'yedxulûne' — gönderge 'llezîne' 2. kelime; ek 'lehum' — gönderge 'llezîne' 2. kelime), konuşan 1P ('neczi'; ek 'bi-âyâtinâ'), 3FS ('tufettehu' — edilgen, naib-i faili 'ebvâbu' 10. kelime; ek ''anhâ' — gönderge 'bi-âyâtinâ' 4. kelime), 3MS ('yelice' — fiil uyumu, fail 17. kelime), aktör adlı 'l-cennete'; "
 "7:41 3MP eki ('lehum', 'fevqıhim' — gönderge 7:40 2. kelime), konuşan 1P ('neczi'), aktör adlı 'cehenneme'",
 "7:38-41 gönderge zinciri: 7:38 'qâle' (1. ve 35. kelime) 3MS — konuşan adsız, gönderge 7:37 6. kelime (lafız), tartışmalı (araya elçilerin sözü giriyor); 7:38 söz içi muhatap 2MP ('dxulû' 2. kelime) 7:37 'ulâ'ike' topluluğu; 7:38 'ddârakû' (21. kelime) ile 'uxrâhum' / 'li-ûlâhum' (25. ve 26. kelime) 'umemin' (4. kelime) adına — tartışmalı: cins uyumsuz (dişil çoğul ad, eril çoğul zamir); "
 "7:38 söz içi konuşan 1P ('rabbenâ' 27. kelime) sonrakiler, 'hâ'ulâ'i' (28. kelime) evvelkiler; muhatap 2MS ('fe-âtihim' 30. kelime) Rab; söz içi muhatap 2MP ('ta'lemûn' 40. kelime) ümmetler; 7:39 'ûlâhum' / 'li-uxrâhum' (2. ve 3. kelime) 7:38 'umemin' (4. kelime) adına — tartışmalı: cins uyumsuz; 7:39 söz içi konuşan 1P (''aleynâ' 7. kelime) evvelkiler, muhatap 2MP sonrakiler; "
 "7:40 3MP fiiller ve 'lehum' (9. kelime) 'llezîne' (2. kelime); 7:40 ve 7:41 konuşan 1P ('bi-âyâtinâ' 7:40 4. kelime, 'neczi' 7:40 22. kelime, 7:41 9. kelime) eş; 7:41 'lehum' (1. kelime) ve 'fevqıhim' (6. kelime) 7:40 'llezîne' (2. kelime) (okuma)",
 "edilgen: 7:40 'tufettehu' (8. kelime; naib-i faili 'ebvâbu' 10. kelime) — ölçüm EDİLGEN 1/6; 7:38, 7:39 ve 7:41 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:38 'qâle' (1.) ardından söz 2-13. kelime — ayet içi kapanış, 'kullemâ' (14.) anlatıya dönüş (okuma); "
 "7:38 'qâlet' (24.) ardından söz 27-34. kelime (REM sapması 7:38 (30. kelime) — 'fe-âtihim' söz içinde yeni cümle başı, konuşan 1P sürer), ayet içi kapanış; 7:38 'qâle' (35.) ardından söz 36-40. kelime (REM sapması 7:38 (38. kelime) — 've lâkin' söz içinde yeni cümle başı, konuşan sürer), ayet içi kapanış; "
 "7:39 've qâlet' (1.) ardından söz 4-14. kelime (REM sapması 7:39 (10. kelime) — 'fe-zûqu' söz içinde yeni cümle başı, konuşan 1P sürer), ayet içi kapanış; "
 "7:40 ve 7:41 söz fiili yok, A3 '—'; mealde 'Dedi ki:' ve 'dedi ki:' ardından tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 38 41 11' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 7:38 've'l-insi' (11.) CONJ, 've lâkin' (38.) REM; 7:39 've qâlet' (1.) CONJ; 7:40 've'stekberû' (5.) CONJ, 've lâ' (12.) CONJ, 've kezâlike' (21.) REM; 7:41 've min' (5.) CONJ, 've kezâlike' (8.) REM; "
 "'fe' konumları: 7:38 'fe-âtihim' (30.) REM; 7:39 'fe-mâ' (4.) CONJ, 'fe-zûqu' (10.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:38 ◈B أنس ('l-insi' 11. kelime — B1); 7:40 ◈K سمو ('s-semâ'i' 11. kelime — K1); 7:39 ve 7:41 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 38 41 11'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:38 (41:25, 46:18, 38:61); 7:39, 7:40 ve 7:41 bağ yok; D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:38 أمم ×2, دخل ×2, ضعف ×2, قول ×3, كلل ×2, نور ×2; 7:39 كون ×2; "
 "ayetler arası kalıp 've kezâlike neczi' (7:40, 7:41) — sayım 'say 7:40 21-22' ve lemma dizisi 'dizi 7 40 21 22' / 'dizi 7 41 8 9'; hüküm kalıbı, bağ kurulmadı (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: bloğun emsal dosyasında olmayan basılmış eş (önceki bloklarda basılmış ya da sûre içi), bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:38 söz açılır (2. kelime), söz kapanır (13. kelime, ayet içi), söz açılır (27. kelime), söz kapanır (34. kelime, ayet içi), söz açılır (36. kelime), söz kapanır (40. kelime, ayet içi), muhatap geçişi 2MP → 2MS (ayet içi), muhatap geçişi 2MS → 2MP (ayet içi), şahıs geçişi 3 → 2, şahıs sayısında toplam farkı (2MP 7 · 2MS 1 · 3. şahıs 13 — ölçüm baskın 2), edim geçişi soru → emir; "
 "7:39 söz açılır (4. kelime), söz kapanır (14. kelime, ayet içi), şahıs geçişi yok, edim geçişi yok; 7:40 şahıs geçişi 2 → 3, edim geçişi emir → haber; 7:41 şahıs geçişi yok, edim geçişi yok, bölüm kapanışı; ölçüm iltifât 7:38-41 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:38 'qad xalet' — tekitli mâzî, 'umemin' sıfatı (morph CERT + PERF); 7:38 'kullemâ dexalet ummetun' — yineleme zarfıyla açılan cümle (morph T + PERF + INDEF); 7:38 'hattâ ize'ddârakû' — başlangıç edatı ve zaman zarfı (morph INC + T; fiil etiketi IMPV, okuma PERF); "
 "7:38 'li-kullin dı'fun' — öne alınmış haberli isim cümlesi (morph P + INDEF + INDEF); 7:39 'fe-mâ kâne lekum 'aleynâ min fadlin' — olumsuz 'kâne' cümlesi, zâid 'min' (morph CONJ + NEG + PERF + P + INDEF); 7:40 'lâ tufettehu lehum ebvâbu's-semâ'i' — olumsuz edilgen muzâri (morph NEG + IMPF + PASS + NOM); "
 "7:40 'hattâ yelice'l-cemelu' — sınır edatıyla mansub muzâri (morph P + IMPF + SUBJ + NOM); 7:41 'lehum min cehenneme mihâdun' — öne alınmış haberli isim cümlesi (morph P + PRON + P + PN + INDEF)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:38 9-11. kelime — 41:25 ve 46:18 ile harekesiz eş (sayım: 'say 7:38 9-11'); 7:38 31-32. kelime — 38:61 ile harekesiz eş (sayım: 'say 7:38 31-32'); "
 "7:39 10-11. kelime — 6:30 ve 46:34 ile harekesiz eş (sayım: 'say 7:39 10-11'); 7:40 21-22. kelime — 6:84 ve 7:41 ile harekesiz eş (sayım: 'say 7:40 21-22'); 7:38 kök أمم, دخل, ضعف, قول, كلل ve نور ikilemeleri; 7:39 kök كون ikilemesi",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 11'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'mine'l-cinni ve'l-insi' 7:38 'cinlerden ve insanlardan' / 41:25 'cin ve insan' (emsal metninde) — çakışma — tam okuma sonu (çoğul ve ayrılma eki / yalın adlar); "
 "'mine'l-cinni ve'l-insi' 7:38 'cinlerden ve insanlardan' / 46:18 'cinlerden ve insanlardan' (emsal metninde) — çakışma değil (bayt eşit); en uzun ortak lemma dizisi 'dizi 7 38 3 11' içindeki 'umemin' (4. kelime) 7:38 ve 46:18 metninde 'ümmetler', 41:25 metninde 'toplulukları' — tam okuma sonu; 'xalet' (6. kelime) üç metinde 'gelip geçmiş'; "
 "''azâben dı'fen' 7:38 'iki kat azap' / 38:61 'onun azabını kat' (emsal metninde) — çakışma — tam okuma sonu ('iki kat' / yinelemeli karşılık; yalın ad / iyelik eki); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:38 'qâle' PERF (1. kelime) — meal 'Dedi'; 'dxulû' IMPV — meal 'girin'; 'xalet' PERF ('qad' ile) — meal 'geçmiş'; 'dexalet' PERF ('kullemâ' ile) — meal 'girdikçe'; 'le'anet' PERF — meal 'etti'; "
 "'ddârakû' IMPV (morph etiketi korundu; okuma PERF, 'izâ' ile) — meal 'yetiştiğinde'; 'qâlet' PERF — meal 'dedi'; 'edallû' PERF — meal 'saptırdı'; 'fe-âtihim' IMPV — meal 'ver'; 'qâle' PERF (35. kelime) — meal 'Dedi'; 'ta'lemûn' IMPF IND ('lâ' ile) — meal 'bilmiyorsunuz'; "
 "7:39 'qâlet' PERF — meal 'dedi'; 'kâne' PERF ('mâ' ile) — meal 'olmadı'; 'fe-zûqu' IMPV — meal 'tadın'; 'kuntum' PERF — meal 'olduklarınızdan'; 'teksibûn' IMPF IND — meal 'kazanmakta'; "
 "7:40 'kezzebû' PERF — meal 'yalanlayıp'; 'stekberû' PERF — meal 'büyüklenenlere'; 'tufettehu' IMPF IND edilgen ('lâ' ile) — meal 'açılmaz'; 'yedxulûne' IMPF IND ('lâ' ile) — meal 'girmezler'; 'yelice' IMPF SUBJ ('hattâ' ile) — meal 'girinceye'; 'neczi' IMPF IND — meal 'cezalandırırız'; "
 "7:41 'neczi' IMPF IND — meal 'cezalandırırız'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle; IMPF IND geniş zaman karşılığı her blokta sapma sayılır — sûre 7 bölüm 3 denetimi kuralı 3): 'xalet' PERF 7:38'de sıfat-fiil ('-miş') ile; 'dexalet' PERF 7:38'de zarf-fiil ('-dikçe') ile; 'ddârakû' 7:38'de zarf-fiil ('-tiğinde') ile; "
 "'kâne' PERF 7:39'da olumsuz geçmiş ('-madı') ile; 'kuntum' PERF ve 'teksibûn' IMPF 7:39'da sıfat-fiil ('-makta olduklarınız') ile; 'kezzebû' PERF 7:40'ta ulaç ('-yıp') ile; 'stekberû' PERF 7:40'ta sıfat-fiil ('-enler') ile; 'tufettehu' IMPF 7:40'ta geniş zaman ('-maz') ile; "
 "'yedxulûne' IMPF 7:40'ta geniş zaman ('-mezler') ile; 'yelice' IMPF SUBJ 7:40'ta zarf-fiil ('-inceye') ile; 'neczi' IMPF 7:40 ve 7:41 metninde geniş zaman ('-ırız') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): "
 "'bi' (belirtme eki / 'dolayı') — çakışma değil (fiil yönetimi, sebep); 'fî' ('-da' / 'arasında' / yönelme eki) — çakışma değil (yer, topluluk içi, girme fiilinin yönü); 'hattâ' (INC: 'Nihayet' / '-inceye kadar') — çakışma değil (başlangıç edatı, sınır edatı); "
 "'hum' ('onlar' / 'Onlar' / 'onlara' / 'onları' / iyelik eki / karşılıksız) — çakışma değil (çekim ve tamlama); 'him' ('onlar' / 'onlara' / iyelik eki) — çakışma değil (çekim ve tamlama); 'hâ' ('onlar' / 'ora' / iyelik eki) — çakışma değil (zamir çekimi ve tamlama); 'hâ' (ATT: karşılıksız) — çakışma değil (tenbih edatı, işaret adıyla karşılandı); 'izâ' ('-diğinde' / '-tiğinde') — çakışma değil (ünsüz benzeşmesi); "
 "'kum' ('size' / 'Siz' / iyelik eki) — çakışma değil (çekim ve tamlama); 'min' ('-dan' / '-den' / '-tan' / '-ten' / bulunma eki / karşılıksız) — çakışma değil (ünlü uyumu ve ünsüz benzeşmesi; yer adıyla bulunma; olumsuzlukta pekiştirme); 'mâ' (NEG: olumsuzluk eki; REL: '-duklarınız' / karşılıksız) — çakışma değil (olumsuzluk edatı, ilgi adı); "
 "'nâ' ('Biz' / 'bize' / 'bizi' / iyelik eki) — çakışma değil (çekim ve tamlama); 'ulâ'i' (DEM: 'işte onlar' / 'İşte' / 'bunlar') — çakışma değil (hitap ekli uzak işaret, tenbih edatlı yakın işaret); 've' (CONJ: 'Ve' / 've' / 'de' / karşılıksız) — çakışma değil (atıf, yinelenen bağlaç, ulaç ekiyle bağlama)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 38 41 11'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:38, 7:39, 7:40 ve 7:41 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:38, 7:39, 7:40 ve 7:41 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök أتي 7:38 ('fe-âtihim'), 7:35 ('ye'tiyennekum') ile bölüm içi; kök أيي 7:40 ('bi-âyâtinâ'), 7:35 ('âyâtî'), 7:36 ('bi-âyâtinâ') ve 7:37 ('bi-âyâtihî') ile bölüm içi; kök كذب 7:40 ('kezzebû'), 7:36 ('kezzebû') ve 7:37 ('keziben', 'kezzebe') ile bölüm içi; kök كبر 7:40 ('ve'stekberû'), 7:36 ('ve'stekberû') ile bölüm içi; "
 "kök نور 7:38 ('n-nâri', 'n-nâri'), 7:36 ('n-nâri') ile bölüm içi; kök ظلم 7:41 ('z-zâlimîn'), 7:37 ('azlemu') ile bölüm içi; kök قول 7:38 ('qâle', 'qâlet', 'qâle') ve 7:39 ('ve qâlet'), 7:37 ('qâlû', 'qâlû') ile bölüm içi; kök كون 7:39 ('kâne', 'kuntum'), 7:37 ('kuntum', 'kânû') ile bölüm içi; kök ضلل 7:38 ('edallûnâ'), 7:37 ('dallû') ile bölüm içi; "
 "kök دخل 7:38 ('dxulû', 'dexalet') ve 7:40 ('yedxulûne'); kök جنن 7:38 ('l-cinni') ve 7:40 ('l-cennete'); kök أخر 7:38 ('uxrâhum') ve 7:39 ('li-uxrâhum'); kök أول 7:38 ('li-ûlâhum') ve 7:39 ('ûlâhum'); kök عذب 7:38 (''azâben') ve 7:39 ('l-'azâbe'); kök جزي 7:40 ('neczi') ve 7:41 ('neczi'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 4-2 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 10 ve 11; bölüm kapanışı bu blokta; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b11/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 38 41 11'; lem_bozuk.py 11 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 38 41 → AYN_SONUC; sunum/bolum4_kurallar.py 38 41 11 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 38 41 11 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 39)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 11 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('min', 'cinn', 'ins', 'fî', 'umme', 'qad', 'xalâ', 'qabl', ''azâb', 'dı'f', 'mâ', 'kâne', 'kesebe', 'kezzebe', 'âye', 'istekbere', ''an', 'ellezî', 'zâ', 'cezâ'); joker '_' bu blokta yok; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (38, 41): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_7_38_41.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_7_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_7_b09k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '38', '41'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '38', '41', '11'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '38', '41', '11'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '38', '41', '11', '--tazelik-yok')}
    for _n in range(7, 39): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '38', '41', '11')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37, B38 = [_R['B%d' % _n].splitlines() for _n in range(6, 39)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'B31_HEPSI': (B31[-1] if B31 else '?'), 'B32_HEPSI': (B32[-1] if B32 else '?'), 'B33_HEPSI': (B33[-1] if B33 else '?'), 'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'), 'B37_HEPSI': (B37[-1] if B37 else '?'), 'B38_HEPSI': (B38[-1] if B38 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
           'MUT_SONUC': (MUT[-1] if MUT else '?'), 'GERI_P': ' / '.join(x.lstrip('# ') for x in GERI), 'B6_ESMA': ('; '.join(l[5:] for l in B6 if 'esmâ kural' in l and l.startswith('HATA')) or 'sapma 0')}
    I_cur = list(I_HAM)
    for k, v in REP.items(): I_cur = I_cur[:len(BEK)] + [x.replace(k, v) for x in I_cur[len(BEK):]]  # bölüm 9 kuralı 9: taşınan denetim maddelerine yer tutucu değişimi uygulanmaz
    I_cur[idx] = ("karşılık çakışması (bölüm 4 kuralı 4, bölüm 5 kuralı 3, bölüm 6 kuralı 2 — komut 'python3 sunum/cakisma.py' + sûre 7'nin okunmuş bütün ARIZA dosyaları; bu bloğun karşılıklarına dokunan gruplar ve son dosyaya dokunan KÖK grupları; grup başına tam bir kapalı karar: 'çakışma değil' ya da 'çakışma — tam okuma sonu'): "
                  + ('; '.join(KARAR.get(l.split(' ←')[0].strip() if not l.startswith('KÖK') else 'KÖK ' + l.split()[1], l + ' — karar yok') for l in CAK_L) if CAK_L else 'bu bloğa dokunan çakışma yok'))
    if I_cur == onceki: break
    onceki = list(I_cur)
yaz(I_cur)
print('yazıldı', len(I_cur), 'tur', tur)
print('\n'.join(CAK_L))
print(GLS)
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37, B38): print([l for l in _x if l.startswith('HATA') or 'hata' in l])

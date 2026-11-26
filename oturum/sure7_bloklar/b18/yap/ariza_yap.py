# sûre 7 blok 18 (7:59-64) ARIZA oluşturucu — bölüm 7-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b18/olcum.txt'
os.environ['SAY2'] = '/home/claude/b18/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = list(ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_7_b17.txt', encoding='utf-8').read() + ']'))
VF_YAZI_ESKI = {}
BOL = "'Nûh ve kavmi; Hûd ve Âd'"


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
 ('7:59', "'qâle qavm 'abede allâh mâ _ min ilâh ğayr'", 4, 'say 7:59 6-14', "harekesiz 'fe-qâle yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû' (6-14. kelime)", ('dizi 7 59 6 14', "qâle qavm 'abede allâh mâ _ min ilâh ğayr", '6-14', 'biçim farkı (dizi 7 59 6 14): basılmamış eş önek; basılmamış eş önek; basılmamış eş önek')),
 ('7:60', "'min qavm inne ra'â fî'", 2, 'say 7:60 3-7', "harekesiz 'min qavmihî innâ le-nerâke fî' (3-7. kelime)", ('dizi 7 60 3 7', "min qavm inne ra'â fî", '3-7', 'biçim farkı (dizi 7 60 3 7): basılmamış eş yazım eş')),
 ('7:60', "'qâle mele' min qavm'", 3, 'say 7:60 2-4', "harekesiz 'l-mele'u min qavmihî' (2-4. kelime)", ('dizi 7 60 1 4', "qâle mele' min qavm", '1-4', 'biçim farkı (dizi 7 60 1 4): basılmamış eş zamir eki; basılmamış eş zamir eki, önek')),
 ('7:61', "'lâkinne rasûl min rabb 'âlem'", 2, 'say 7:61 6-10', "harekesiz 've lâkinnî rasûlun min rabbi'l-'âlemîn' (6-10. kelime)", ('dizi 7 61 6 10', "lâkinne rasûl min rabb 'âlem", '6-10', 'biçim farkı (dizi 7 61 6 10): basılmamış eş yazım eş')),
 ('7:61', "'rasûl min rabb 'âlem'", 3, 'say 7:61 7-10', "harekesiz 'rasûlun min rabbi'l-'âlemîn' (7-10. kelime)", ('dizi 7 61 7 10', "rasûl min rabb 'âlem", '7-10', 'biçim farkı (dizi 7 61 7 10): basılmamış eş yazım eş; basılmamış eş yazım eş')),
 ('7:61', "'qâle qavm leyse _'", 2, 'say 7:61 1-4', "harekesiz 'qâle yâ qavmi leyse bî' (1-4. kelime)", ('dizi 7 61 1 4', 'qâle qavm leyse _', '1-4', 'biçim farkı (dizi 7 61 1 4): basılmamış eş yazım eş')),
 ('7:62', "'allâh mâ lâ 'alime'", 3, 'say 7:62 8-11', "harekesiz 'llâhi mâ lâ ta'lemûn' (8-11. kelime)", ('dizi 7 62 8 11', "allâh mâ lâ 'alime", '8-11', 'biçim farkı (dizi 7 62 8 11): 7:28 yazım eş; 7:33 yazım eş')),
 ('7:62', "'risâle rabb nesahu _'", 3, 'say 7:62 2-5', "harekesiz 'risâlâti rabbî ve ensahu lekum' (2-5. kelime)", ('dizi 7 62 2 5', 'risâle rabb nesahu _', '2-5', 'biçim farkı (dizi 7 62 2 5): basılmamış eş zamir eki; basılmamış eş zamir eki')),
 ('7:62', "'belliğ risâle rabb'", 2, 'say 7:62 1-3', "harekesiz 'ubelliğukum risâlâti rabbî' (1-3. kelime)", ('dizi 7 62 1 3', 'belliğ risâle rabb', '1-3', 'biçim farkı (dizi 7 62 1 3): basılmamış eş yazım eş')),
 ('7:63', "''acibu en câ'e zikr min rabb 'alâ racul min enzere'", 2, 'say 7:63 1-10', "harekesiz 'e-ve-'acibtum en câ'ekum zikrun min rabbikum 'alâ raculin minkum li-yunzirakum' (1-10. kelime)", ('dizi 7 63 1 10', "'acibu en câ'e zikr min rabb 'alâ racul min enzere", '1-10', 'biçim farkı (dizi 7 63 1 10): basılmamış eş yazım eş')),
 ('7:64', "'ellezî kezzebe âye'", 5, 'say 7:64 8-10', "harekesiz 'llezîne kezzebû bi-âyâtinâ' (8-10. kelime); biçim öğesi 'ellezî' öneki (lemma dizisi sûre içi 8, nakarat3 5)", ('dizi 7 64 8 10', 'ellezî kezzebe âye', '8-10', 'biçim farkı (dizi 7 64 8 10): 7:36 önek; 7:40 yazım eş; basılmamış eş yazım eş; basılmamış eş önek; basılmamış eş yazım eş; basılmamış eş yazım eş; basılmamış eş önek; öneksiz eş koşusu (dizi 7 64 8 10): 7:36 → önek kesilmiş sûre içi 3; 7:40 → önek kesilmiş sûre içi 7; basılmamış eş → önek kesilmiş sûre içi 7; basılmamış eş → önek kesilmiş sûre içi 3; basılmamış eş → önek kesilmiş sûre içi 7; basılmamış eş → önek kesilmiş sûre içi 7; basılmamış eş → önek kesilmiş sûre içi 3')),
 ('7:64', "'encâ ellezî ma'a'", 2, 'say 7:64 2-4', "harekesiz 'fe-enceynâhu ve'llezîne me'ahû' (2-4. kelime)", ('dizi 7 64 2 4', "encâ ellezî ma'a", '2-4', 'biçim farkı (dizi 7 64 2 4): basılmamış eş yazım eş')),
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

VF_YAZI = {59: {1: "'le-qad'", 6: "'fe-qâle'"}, 60: {6: "'le-nerâke'"}, 61: {4: "'bî'", 6: "'ve lâkinnî'"}, 62: {4: "'ve ensahu'", 5: "'lekum'", 6: "'ve a'lemu'"}, 63: {1: "'e-ve-'acibtum'", 10: "'li-yunzirakum'", 11: "'ve li-tetteqû'", 12: "'ve le'allekum'"}, 64: {1: "'fe-kezzebûhu'", 2: "'fe-enceynâhu'", 3: "'ve'llezîne'", 7: "'ve ağraqna'", 10: "'bi-âyâtinâ'"}}
sys.path.insert(0, '/home/claude/b18/yap')
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
open('/home/claude/b18/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '18')
BLOKLAR = [str(i) for i in range(1, 19)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '18', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b18/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '59', '64', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b18/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b18/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '59', '64', '18').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_59_64.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'7:59', '7:60', '7:61', '7:62', '7:63', '7:64'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_59_64.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '7:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '7:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(59, 65))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "7:59 kök عظم (''azîm' 20. kelime — büyük): tetik listesinde yok; 7:63 kök رجل ('raculin' 8. kelime — adam): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '59', '64', '18')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b18/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 19)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b7:%d:\d+' % a_, s_) for a_ in range(59, 65))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
_OL = [l.replace('**', '') for l in open('/home/claude/b18/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b18/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[0]).group(0))
for _k, _v in (('_AK', _AK),): _MB = _MB.replace('" + %s + "' % _k, _v)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 58), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta araç kuralı değişmedi; bölüm 6 kapanışında sunum/bolum42_kurallar.py (kural 1-5) eklendi, sunum/geriye_donuk.py ve mutasyon_sina buna göre güncellendi — önceki commit'te, kapanış mutasyon sınaması 445 / 445; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 463",
 "geriye dönük koşu (sûre 7 bölüm 6 kapanışı, komut 'python3 sunum/geriye_donuk.py b17k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 59 64 18'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:60 'fî dalâlin mubîn' (7-9. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (sapkınlığın sıfatı) (yamalar/esma_el_7_59_64.txt); 7:60 esma_kayit 'mühür EVET' / ölçüm MÜHÜRSÜZ — uyuşmuyor (esma_el 'degil' kararı; muhur_el ölçümle eş); 7:59, 7:61, 7:62, 7:63 ve 7:64 esmâ yok; "
 "7:59 lafız (9. kelime), 7:62 lafız (8. kelime); 7:60, 7:61, 7:63 ve 7:64 lafız yok; 7:61 Rab (9. kelime), 7:62 Rab (3. kelime), 7:63 Rab (6. kelime); 7:59, 7:60 ve 7:64 Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 59 64 18'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 7:60 mühür EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, esma_el 'degil' kararı): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in range(59, 65)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 59 64 18'): KALAN_P",
 "ölçüm aktör: 7:59 adlı نُوح (3. kelime, rol meful); 7:63 adsız racül (8. kelime); 7:60, 7:61, 7:62 ve 7:64 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:59 emir, nida — CERT 1 'le-qad' (1.), EMPH 1 'le-qad' (1.), IMPV 1 'u'budu' (8.), NEG 1 'mâ' (10.), VOC 1 'yâ' (7.); 7:60 haber — EMPH 1 'le-nerâke' (6.); 7:61 nida — VOC 1 'yâ' (2.); 7:62 haber — NEG 1 'lâ' (10.); 7:63 soru — INTG 1 'e' (1.); 7:64 haber — kip yok; "
 "morph REL ('mâ' 7:62 9., 'llezîne' 7:64 3. ve 8.), SUB ('en' 7:63 2.), PRP ('li-yunzirakum' 7:63 10., 'li-tetteqû' 7:63 11.), LOC ('me'ahû' 7:64 4.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:61 ★ (kaynak rab, z=1,81); 7:62 ★ (kaynak rab, z=1,62); 7:59, 7:60, 7:63 ve 7:64 yıldız yok",
 "fâsıla: 7:58 ن → 7:59 م (" + _F[0] + ") → 7:60 ن (" + _F[1] + ") → 7:61 ن (" + _F[2] + ") → 7:62 ن (" + _F[3] + ") → 7:63 ن (" + _F[4] + ") → 7:64 ن (" + _F[5] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:59 11:50, 11:61, 11:84, 23:23, 23:32 (emsal olarak basıldı), okunmuş 1 ayet ve okunmamış 3 ayet (sûre içi 3); 7:60 12:30, 23:33 (emsal olarak basıldı), okunmamış 2 ayet (sûre içi 2); "
 "7:61 26:16, 43:46 (emsal olarak basıldı), okunmuş 1 ayet ve okunmamış 2 ayet (sûre içi 2); 7:62 xref yok; 7:63 xref yok; 7:64 10:73, 21:77 (emsal olarak basıldı), okunmamış 3 ayet (sûre içi 3); 7:61 esit2 okunmamış 1 ayet (sûre içi 1), kademe BENZER",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok (7:59-64 ölçümünde nakarat3 alanı boş)'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:59 'qâle qavm 'abede allâh mâ _ min ilâh ğayr' süzgeç GEÇER; 7:60 'min qavm inne ra'â fî' süzgeç GEÇER, 'qâle mele' min qavm' süzgeç GEÇER; 7:61 'lâkinne rasûl min rabb 'âlem' süzgeç GEÇER, 'rasûl min rabb 'âlem' süzgeç GEÇER, 'qâle qavm leyse _' süzgeç GEÇER; "
 "7:62 'allâh mâ lâ 'alime' süzgeç GEÇER, 'risâle rabb nesahu _' süzgeç GEÇER, 'belliğ risâle rabb' süzgeç GEÇMEZ; 7:63 ''acibu en câ'e zikr min rabb 'alâ racul min enzere' süzgeç GEÇER; 7:64 'ellezî kezzebe âye' süzgeç GEÇER, 'encâ ellezî ma'a' süzgeç GEÇMEZ; sûre içi eşler — 7:62 'allâh mâ lâ 'alime' kalıbında 7:28 ve 7:33 (basılmış), 7:64 'ellezî kezzebe âye' kalıbında 7:36 ve 7:40 (basılmış), diğer kalıplarda basılmamış",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:59 konuşan 1P ('erselnâ'), 3MS ('fe-qâle' — gönderge 'nûhan' 3. kelime; ekler 'qavmihî' — gönderge 'nûhan' 3. kelime; 'ğayruhû' — söz içi, gönderge 'llâhe' 9. kelime), söz içi konuşan 1S ('exâfu'; ekler 'qavmi', 'innî'), söz içi muhatap 2MP ('u'budu'; ekler 'lekum', ''aleykum'); aktör adlı 'nûhan'; "
 "7:60 3MS ('qâle' — fiil uyumu, fail 2. kelime; ek 'qavmihî' — gönderge 7:59 3. kelime), söz içi konuşan 1P ('nerâke'; ek 'innâ'), söz içi muhatap 2MS eki ('nerâke'); 7:61 3MS ('qâle' — gönderge 7:59 3. kelime; 'leyse' — söz içi, fiil uyumu, fail 5. kelime), söz içi konuşan 1S eki ('qavmi', 'bî', 'lâkinnî'); "
 "7:62 söz içi konuşan 1S ('ubelliğukum', 'ensahu', 'a'lemu'; ek 'rabbî'), söz içi muhatap 2MP ('ta'lemûn'; ekler 'ubelliğukum', 'lekum'); 7:63 söz içi muhatap 2MP (''acibtum', 'tetteqû'; edilgen 'turhamûn' — naib-i faili zamir; ekler 'câ'ekum', 'rabbikum', 'minkum', 'yunzirakum', 'le'allekum'), 3MS ('câ'ekum' — söz içi, fiil uyumu, fail 4. kelime; 'yunzirakum' — söz içi, gönderge 'raculin' 8. kelime); aktör adsız 'raculin'; "
 "7:64 3MP ('kezzebûhu' — gönderge 7:59 5. kelime; 'kezzebû', 'kânû' — gönderge 'llezîne' 8. kelime; ek 'innehum'), konuşan 1P ('enceynâhu', 'ağraqna'; ek 'bi-âyâtinâ'), 3MS ekleri ('kezzebûhu', 'enceynâhu', 'me'ahû' — gönderge 7:59 3. kelime)",
 "7:59-64 gönderge zinciri: 7:59 konuşan 1P ('erselnâ' 2. kelime) bölüm açılışında anlatıcı; 7:59 'fe-qâle' 3MS göndergesi 'nûhan' (3. kelime); 7:60 'qavmihî' ve 7:61 'qâle' göndergesi 7:59 3. kelimedeki Nûh; 7:61-63 söz içi konuşan 1S Nûh, muhatap 2MP kavmi (7:60 'l-mele'u' 2. kelime ile eş hitap); 7:63 'yunzirakum' göndergesi 'raculin' (8. kelime); 7:64 'kezzebûhu' 3MP göndergesi 7:59 5. kelimedeki kavim, 3MS ekleri 7:59 3. kelimedeki Nûh; 7:64 konuşan 1P 7:59 konuşan 1P ile eş (okuma)",
 "edilgen: 7:63 'turhamûn' (13. kelime) edilgen (ölçüm EDİLGEN 1/5); 7:59, 7:60, 7:61, 7:62 ve 7:64 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:59 söz içi 7-20. kelime ('fe-qâle' 6. kelime ardından; ayet içinde kapanıyor); 7:60 söz içi 5-9. kelime ('qâle' 1. kelime ardından; ayet içinde kapanıyor); "
 "7:61 söz içi 2-10. kelime ('qâle' 1. kelime ardından; ayet sonunda kapanmıyor), 7:62 söz sürüyor (1-11. kelime; ayet sonunda kapanmıyor), 7:63 söz sürüyor (1-13. kelime; 13. kelimede kapanıyor); 7:64 söz fiili yok, A3 '—'; REM sapması 7:61 (6. kelime) — 'lâkinne' önündeki istidrak 've'si, söz içi cümle başı; REM sapması 7:62 (6. kelime) — söz içi yeni cümle başı; REM sapması 7:63 (12. kelime) — 'le'alle' önündeki söz içi cümle başı; "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 59 64 18' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 7:59 'fe-qâle' (6.) CONJ; 7:61 've lâkinnî' (6.) REM; 7:62 've ensahu' (4.) CONJ, 've a'lemu' (6.) REM; 7:63 'e-ve-'acibtum' (1.) CONJ, 've li-tetteqû' (11.) CONJ, 've le'allekum' (12.) REM; 7:64 'fe-kezzebûhu' (1.) REM, 'fe-enceynâhu' (2.) REM, 've'llezîne' (3.) CONJ, 've ağraqna' (7.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:59 ◈K يوم ('yevmin' 19. kelime — K2); 7:64 ◈K فلك ('l-fulki' 6. kelime — K1); 7:60, 7:61, 7:62 ve 7:63 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 59 64 18'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 6 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:59 (11:50, 11:61, 11:84, 23:23, 23:32), 7:60 (12:30, 23:33), 7:61 (26:16, 43:46), 7:64 (10:73, 21:77); D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:59 أله ×2, قوم ×2; 7:62 علم ×2; 7:64 كذب ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: bloğun emsal dosyasında olmayan basılmış eş (önceki bloklarda basılmış ya da sûre içi), bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:59 bölüm açılışı, söz açılır / kapanır, şahıs sayısında toplam farkı (1. şahıs 5 · 2MP 4 — ölçüm baskın 2), şahıs geçişi 3 → 2, edim geçişi haber → emir, nida; 7:60 söz açılır / kapanır, şahıs sayısında beraberlik (1P 2 · 3. şahıs 2 — ölçüm baskın 3), şahıs geçişi 2 → 3, edim geçişi emir, nida → haber; 7:61 söz açılır, şahıs geçişi 3 → 1, edim geçişi haber → nida; "
 "7:62 şahıs sayısında beraberlik (1S 4 · 2MP 4 — ölçüm baskın 1), şahıs geçişi yok, edim geçişi nida → haber; 7:63 söz kapanır, şahıs geçişi 1 → 2, edim geçişi haber → soru; 7:64 şahıs geçişi 2 → 3, edim geçişi soru → haber; ölçüm iltifât 7:59-64 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:59 'le-qad erselnâ nûhan' — yemin lâmı ve tahkik, mâzî (morph EMPH + CERT + PERF); 7:59 'yâ qavmi u'budu'llâhe' — nida ve emir (morph VOC + IMPV); 7:59 'mâ lekum min ilâhin ğayruhû' — olumsuzluk, öne alınmış haber (morph NEG + P + P); "
 "7:60 'innâ le-nerâke' — tekit edatı ve lâm ile muzâri (morph ACC + EMPH + IMPF); 7:61 'leyse bî dalâletun' — olumsuz nakıs fiil, öne alınmış haber (morph V + P + NOM); 7:63 'en câ'ekum zikrun' — masdar cümlesi, mâzî ve nekre fail (morph SUB + PERF + NOM); 7:64 'innehum kânû qavmen 'amîn' — tekit edatı ve nakıs fiil (morph ACC + V + ACC)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:59 2-5. kelime — 23:23 ile harekesiz eş (sayım: 'say 7:59 2-5'); 7:59 7-14. kelime — 11:50, 11:61, 11:84 ve 23:23 ile harekesiz eş (sayım: 'say 7:59 7-14'); "
 "7:59 8-14. kelime — 23:32 ile harekesiz eş (sayım: 'say 7:59 8-14'); 7:60 7-9. kelime — 12:30 ile harekesiz eş (sayım: 'say 7:60 7-9'); 7:64 7-9. kelime — 10:73 ile harekesiz eş (sayım: 'say 7:64 7-9'); 7:64 8-10. kelime — 21:77 ile harekesiz eş (sayım: 'say 7:64 8-10'); 7:59 kök أله ve قوم ikilemeleri; 7:62 kök علم ikilemesi; 7:64 kök كذب ikilemesi; geniş eşli sayımlar (sûre içi basılmamış eşler): 'say 7:59 15-20', 'say 7:59 6-14', 'say 7:60 3-7', 'say 7:61 6-10', 'say 7:62 6-11'",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 18'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): 'erselnâ nûhan ilâ qavmihî' 7:59 'Nûh'u kavmine gönderdik' / 23:23 'Nûh'u kavmine gönderdik' (emsal metninde) — çakışma değil; 'yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû' 7:59 'Ey kavmim, Allah'a kulluk edin. Sizin O'ndan başka bir ilâhınız yok' / 11:50 'Ey kavmim, Allah'a kulluk edin' (emsal metninde) — çakışma — tam okuma sonu ('bir ilâhınız yok' / 'ilâhınız yoktur'); 'yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû' 7:59 'Ey kavmim, Allah'a kulluk edin. Sizin O'ndan başka bir ilâhınız yok' / 11:61 'Ey kavmim, Allah'a kulluk edin' (emsal metninde) — çakışma — tam okuma sonu ('bir ilâhınız yok' / 'ilâhınız yoktur'); 'yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû' 7:59 'Ey kavmim, Allah'a kulluk edin. Sizin O'ndan başka bir ilâhınız yok' / 11:84 'Ey kavmim, Allah'a kulluk edin' (emsal metninde) — çakışma — tam okuma sonu ('bir ilâhınız yok' / 'ilâhınız yoktur'); 'yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû' 7:59 'Ey kavmim, Allah'a kulluk edin. Sizin O'ndan başka bir ilâhınız yok' / 23:23 'Ey kavmim, Allah'a kulluk edin' (emsal metninde) — çakışma — tam okuma sonu ('Sizin' / 'sizin için', 'bir ilâhınız yok' / 'ilâh yok'); 'u'budu'llâhe mâ lekum min ilâhin ğayruhû' 7:59 'Allah'a kulluk edin. Sizin O'ndan başka bir ilâhınız yok' / 23:32 'Allah'a kulluk edin' (emsal metninde) — çakışma — tam okuma sonu ('Sizin' / 'sizin için'); 'l-mele'u min qavmihî' 7:60 'Kavminden ileri gelenler' / 23:33 'Kavminden' (emsal metninde) — çakışma — tam okuma sonu ('ileri gelenler' emsalde ilgi cümlelerinden sonra); 'fî dalâlin mubîn' 7:60 'apaçık bir sapkınlık içinde' / 12:30 'açık bir sapkınlık içinde' (emsal metninde) — çakışma — tam okuma sonu ('apaçık' / 'açık'; 'say 7:60 5-9' korpusta 1, 'dizi 7 60 5 9' 12:30 ile eş — çekim farkı 'nerâke' / 'nerâhâ'); 'rabbi'l-'âlemîn' 7:61 'âlemlerin Rabbinden' / 26:16 'âlemlerin Rabbinin' (emsal metninde) — çakışma — tam okuma sonu ('-den' / '-in'); 'rabbi'l-'âlemîn' 7:61 'âlemlerin Rabbinden' / 43:46 'âlemlerin Rabbinin' (emsal metninde) — çakışma — tam okuma sonu ('-den' / '-in'); 'me'ahû fi'l-fulki' 7:64 'gemide onunla birlikte' / 10:73 'gemide onunla beraber' (emsal metninde) — çakışma — tam okuma sonu ('birlikte' / 'beraber'); 'u'budu'llâhe' 7:59 'Allah'a kulluk edin' / 23:32 'Allah'a kulluk edin' (emsal metninde) — çakışma değil; 'mâ lekum min ilâhin ğayruhû' 7:59 'Sizin O'ndan başka bir ilâhınız yok' / 11:50 'sizin O'ndan başka ilâhınız yoktur' (emsal metninde) — çakışma — tam okuma sonu ('bir ilâhınız yok' / 'ilâhınız yoktur'); 've ağraqna'llezîne kezzebû' 7:64 'yalanlayanları boğduk' / 10:73 'yalanlayanları boğduk' (emsal metninde) — çakışma değil ('say 7:64 7-10' korpusta 1, 'dizi 7 64 7 10' 10:73 ile eş — yazım farkı 'bi-âyâtinâ'); 'llezîne kezzebû bi-âyâtinâ' 7:64 'âyetlerimizi yalanlayanları' / 21:77 'Âyetlerimizi yalanlayan' (emsal metninde) — çakışma — tam okuma sonu ('-anları' / '-an'); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:59 'erselnâ' PERF — meal 'gönderdik'; 'qâle' PERF — meal 'Dedi'; 'u'budu' IMPV — meal 'kulluk edin'; 'exâfu' IMPF IND — meal 'korkuyorum'; "
 "7:60 'qâle' PERF — meal 'dedi'; 'nerâke' IMPF IND — meal 'görüyoruz'; 7:61 'qâle' PERF — meal 'Dedi'; 'leyse' PERF — meal 'yok'; 7:62 'ubelliğukum' IMPF IND — meal 'tebliğ ediyorum'; 'ensahu' IMPF IND — meal 'öğüt veriyorum'; 'a'lemu' IMPF IND — meal 'biliyorum'; 'ta'lemûn' IMPF IND ('lâ' ile) — meal 'bilmediğiniz'; "
 "7:63 ''acibtum' PERF — meal 'şaştınız'; 'câ'ekum' PERF ('en' ile) — meal 'gelmesine'; 'yunzirakum' IMPF SUBJ — meal 'uyarması'; 'tetteqû' IMPF SUBJ — meal 'sakınmanız'; 'turhamûn' IMPF IND edilgen — meal 'merhamet olunasınız'; "
 "7:64 'kezzebûhu' PERF — meal 'yalanladılar'; 'enceynâhu' PERF — meal 'kurtardık'; 'ağraqna' PERF — meal 'boğduk'; 'kezzebû' PERF — meal 'yalanlayanları'; 'kânû' PERF — meal 'idiler'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle; IMPF IND geniş zaman karşılığı her blokta sapma sayılır — sûre 7 bölüm 3 denetimi kuralı 3): 'exâfu' IMPF 7:59'da şimdiki zaman ('-uyorum') ile; 'nerâke' IMPF 7:60'ta şimdiki zaman ('-üyoruz') ile; 'leyse' PERF 7:61'de olumsuz varlık ('yok') ile; "
 "'ubelliğukum', 'ensahu', 'a'lemu' IMPF 7:62'de şimdiki zaman ('-iyorum') ile; 'ta'lemûn' IMPF 7:62'de sıfat-fiil ('-mediğiniz') ile; 'câ'ekum' PERF 7:63'te mastar ('-mesi') ile; 'yunzirakum', 'tetteqû' IMPF 7:63'te mastar ('-ması', '-manız') ile; 'turhamûn' IMPF 7:63'te istek kipi ('-asınız') ile; 'kezzebû' PERF 7:64'te sıfat-fiil ('-anları') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 59 64 18'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:59, 7:60, 7:61, 7:62, 7:63 ve 7:64 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:64 ('fe-enceynâhu' / 've ağraqna'); 7:59, 7:60, 7:61, 7:62 ve 7:63 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök أله 7:59 ('llâhe', 'ilâhin') ve 7:62 ('llâhi') ile bölüm içi; kök ربب 7:61 ('rabbi'), 7:62 ('rabbî') ve 7:63 ('rabbikum') ile bölüm içi; kök رسل 7:59 ('erselnâ'), 7:61 ('rasûlun') ve 7:62 ('risâlâti') ile bölüm içi; kök ضلل 7:60 ('dalâlin') ve 7:61 ('dalâletun') ile bölüm içi; kök علم 7:61 (''âlemîn') ve 7:62 ('a'lemu', 'ta'lemûn') ile bölüm içi; kök قول 7:59 ('fe-qâle'), 7:60 ('qâle') ve 7:61 ('qâle') ile bölüm içi; kök قوم 7:59 ('qavmihî', 'qavmi'), 7:60 ('qavmihî'), 7:61 ('qavmi') ve 7:64 ('qavmen') ile bölüm içi; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 7-1 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 18, 19 ve 20; bölüm açılışı bu blokta; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b18/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 59 64 18'; lem_bozuk.py 18 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 59 64 → AYN_SONUC; sunum/bolum4_kurallar.py 59 64 18 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 59 64 18 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 43)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 18 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('qad', 'ersele', 'nûh', 'ilâ', 'qavm', 'qâle', ''abede', 'allâh', 'mâ', 'min', 'ilâh', 'ğayr', 'mele'', 'inne', 'ra'â', 'fî', 'dalâl', 'mubîn', 'leyse', 'lâkinne', 'rasûl', 'rabb', ''âlem', 'lâ', ''alime', 'risâle', 'nesahu' (morph LEM ham biçim), 'belliğ' (morph LEM ham biçim), ''acibu' (morph LEM ham biçim), 'en', 'câ'e', 'zikr', ''alâ', 'racul', 'enzere', 'ellezî', 'kezzebe', 'âye', 'encâ', 'ma'a', 'kâne', 'uğriqu' (morph LEM ham biçim)); joker '_' dizi lemma dizisinde boş öğe olan önek lemmalı kelimelerde ('lekum' 7:59 11. ve 7:62 5., 'bî' 7:61 4.); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (59, 64): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_7_59_64.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_7_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_7_b17k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '59', '64'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '59', '64', '18'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '59', '64', '18'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '59', '64', '18', '--tazelik-yok')}
    for _n in range(7, 43): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '59', '64', '18')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37, B38, B39, B40, B41, B42 = [_R['B%d' % _n].splitlines() for _n in range(6, 43)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'B31_HEPSI': (B31[-1] if B31 else '?'), 'B32_HEPSI': (B32[-1] if B32 else '?'), 'B33_HEPSI': (B33[-1] if B33 else '?'), 'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'), 'B37_HEPSI': (B37[-1] if B37 else '?'), 'B38_HEPSI': (B38[-1] if B38 else '?'), 'B39_HEPSI': (B39[-1] if B39 else '?'), 'B40_HEPSI': (B40[-1] if B40 else '?'), 'B41_HEPSI': (B41[-1] if B41 else '?'), 'B42_HEPSI': (B42[-1] if B42 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37, B38, B39, B40, B41, B42): print([l for l in _x if l.startswith('HATA') or 'hata' in l])

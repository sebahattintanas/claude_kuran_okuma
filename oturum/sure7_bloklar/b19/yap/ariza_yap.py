# sûre 7 blok 19 (7:65-69) ARIZA oluşturucu — bölüm 7-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b19/olcum.txt'
os.environ['SAY2'] = '/home/claude/b19/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
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
 ('7:65', "'qâle qavm 'abede allâh mâ _ min ilâh ğayr'", 4, 'say 7:65 5-13', "harekesiz 'qâle yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû' (5-13. kelime)", ('dizi 7 65 5 13', "qâle qavm 'abede allâh mâ _ min ilâh ğayr", '5-13', 'biçim farkı (dizi 7 65 5 13): 7:59 önek; basılmamış eş yazım eş; basılmamış eş yazım eş')),
 ('7:66', "'qâle mele' ellezî kefere min qavm'", 2, 'say 7:66 3-6', "harekesiz 'llezîne kefarû min qavmihî' (3-6. kelime)", ('dizi 7 66 1 6', "qâle mele' ellezî kefere min qavm", '1-6', 'biçim farkı (dizi 7 66 1 6): basılmamış eş önek')),
 ('7:66', "'min qavm inne ra'â fî'", 2, 'say 7:66 5-9', "harekesiz 'min qavmihî innâ le-nerâke fî' (5-9. kelime)", ('dizi 7 66 5 9', "min qavm inne ra'â fî", '5-9', 'biçim farkı (dizi 7 66 5 9): 7:60 yazım eş')),
 ('7:66', "'qâle mele' ellezî'", 4, 'say 7:66 2-3', "harekesiz 'l-mele'u'llezîne' (2-3. kelime)", ('dizi 7 66 1 3', "qâle mele' ellezî", '1-3', 'biçim farkı (dizi 7 66 1 3): basılmamış eş yazım eş; basılmamış eş yazım eş; basılmamış eş önek')),
 ('7:67', "'lâkinne rasûl min rabb 'âlem'", 2, 'say 7:67 6-10', "harekesiz 've lâkinnî rasûlun min rabbi'l-'âlemîn' (6-10. kelime)", ('dizi 7 67 6 10', "lâkinne rasûl min rabb 'âlem", '6-10', 'biçim farkı (dizi 7 67 6 10): 7:61 yazım eş')),
 ('7:67', "'rasûl min rabb 'âlem'", 3, 'say 7:67 7-10', "harekesiz 'rasûlun min rabbi'l-'âlemîn' (7-10. kelime)", ('dizi 7 67 7 10', "rasûl min rabb 'âlem", '7-10', 'biçim farkı (dizi 7 67 7 10): 7:61 yazım eş; basılmamış eş yazım eş')),
 ('7:67', "'qâle qavm leyse _'", 2, 'say 7:67 1-4', "harekesiz 'qâle yâ qavmi leyse bî' (1-4. kelime)", ('dizi 7 67 1 4', 'qâle qavm leyse _', '1-4', 'biçim farkı (dizi 7 67 1 4): 7:61 yazım eş')),
 ('7:68', "'belliğ risâle rabb'", 2, 'say 7:68 1-3', "harekesiz 'ubelliğukum risâlâti rabbî' (1-3. kelime)", ('dizi 7 68 1 3', 'belliğ risâle rabb', '1-3', 'biçim farkı (dizi 7 68 1 3): 7:62 yazım eş')),
 ('7:69', "''acibu en câ'e zikr min rabb 'alâ racul min enzere'", 2, 'say 7:69 1-10', "harekesiz 'e-ve-'acibtum en câ'ekum zikrun min rabbikum 'alâ raculin minkum li-yunzirakum' (1-10. kelime)", ('dizi 7 69 1 10', "'acibu en câ'e zikr min rabb 'alâ racul min enzere", '1-10', 'biçim farkı (dizi 7 69 1 10): 7:63 yazım eş')),
 ('7:69', "'zekere iz ce'ale xalîfe min ba'd'", 2, 'say 7:69 11-16', "harekesiz 've'zkurû iz ce'alekum xulefâ'e min ba'di' (11-16. kelime)", ('dizi 7 69 11 16', "zekere iz ce'ale xalîfe min ba'd", '11-16', 'biçim farkı (dizi 7 69 11 16): basılmamış eş yazım eş')),
 ('7:69', "'zekere âlâ' allâh'", 2, 'say 7:69 23-25', "harekesiz 'fe'zkurû âlâ'e'llâhi' (23-25. kelime)", ('dizi 7 69 23 25', "zekere âlâ' allâh", '23-25', 'biçim farkı (dizi 7 69 23 25): basılmamış eş yazım eş')),
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

VF_YAZI = {65: {1: "'ve ilâ'", 14: "'e-fe-lâ'"}, 66: {8: "'le-nerâke'", 11: "'ve innâ'", 12: "'le-nezunnuke'"}, 67: {4: "'bî'", 6: "'ve lâkinnî'"}, 68: {4: "'ve ene'", 5: "'lekum'"}, 69: {1: "'e-ve-'acibtum'", 10: "'li-yunzirakum'", 11: "'ve'zkurû'", 19: "'ve zâdekum'", 23: "'fe'zkurû'"}}
sys.path.insert(0, '/home/claude/b19/yap')
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
open('/home/claude/b19/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '19')
BLOKLAR = [str(i) for i in range(1, 20)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '19', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b19/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '65', '69', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b19/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b19/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '65', '69', '19').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_65_69.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'7:65', '7:66', '7:67', '7:68', '7:69'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_65_69.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '7:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '7:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(65, 70))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "7:69 'iz' (12. kelime — morph T, zaman); 7:69 kök بعد ('ba'di' 16. kelime — sonra): tetik listesinde yok; 7:69 kök رجل ('raculin' 8. kelime — adam): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '65', '69', '19')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b19/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 20)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b7:%d:\d+' % a_, s_) for a_ in range(65, 70))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
_OL = [l.replace('**', '') for l in open('/home/claude/b19/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b19/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK1 = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[0]).group(0))
_AK5 = _esc(re.search(r'aktör: adlı .*?adsız `racül` 8\. sırada', _OL[4]).group(0))
for _k, _v in (('_AK1', _AK1), ('_AK5', _AK5)): _MB = _MB.replace('" + %s + "' % _k, _v)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 64), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta araç kuralı değişmedi; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 470",
 "geriye dönük koşu (sûre 7 bölüm 6 kapanışı, komut 'python3 sunum/geriye_donuk.py b17k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 65 69 19'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:65, 7:66, 7:67, 7:68 ve 7:69 esmâ yok; 7:65 lafız (8. kelime), 7:69 lafız (25. kelime); 7:66, 7:67 ve 7:68 lafız yok; 7:67 Rab (9. kelime), 7:68 Rab (3. kelime), 7:69 Rab (6. kelime); 7:65 ve 7:66 Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 65 69 19'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in range(65, 70)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 65 69 19'): KALAN_P",
 "ölçüm aktör: 7:65 adlı عاد (2. kelime, rol mecrur) ve adlı هُود (4. kelime, rol meful); 7:69 adlı نُوح (18. kelime, rol mecrur) ve adsız racül (8. kelime); 7:66, 7:67 ve 7:68 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:65 soru, emir, nida — IMPV 1 'u'budu' (7.), INTG 1 'e-fe-lâ' (14.), NEG 2 'mâ' (9.) ve 'e-fe-lâ' (14.), VOC 1 'yâ' (6.); 7:66 haber — EMPH 2 'le-nerâke' (8.), 'le-nezunnuke' (12.); 7:67 nida — VOC 1 'yâ' (2.); 7:68 haber — kip yok; 7:69 soru, emir — IMPV 2 'zkurû' (11.) ve 'zkurû' (23.), INTG 1 'e' (1.); "
 "morph REL ('llezîne' 7:66 3.), SUP ('e-fe-lâ' 7:65 14.), SUB ('en' 7:69 2.), PRP ('li-yunzirakum' 7:69 10.), T ('iz' 7:69 12.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:67 ★ (kaynak rab, z=1,81); 7:68 ★★ (kaynak rab, z=2,72); 7:69 ★ (kaynak n, z=1,55); 7:65 ve 7:66 yıldız yok",
 "fâsıla: 7:64 ن → 7:65 ن (" + _F[0] + ") → 7:66 ن (" + _F[1] + ") → 7:67 ن (" + _F[2] + ") → 7:68 ن (" + _F[3] + ") → 7:69 ن (" + _F[4] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:65 7:59, 11:50, 11:61, 11:84, 23:23, 23:32 (basılmış), okunmamış 2 ayet (sûre içi 2); 7:66 11:27, 23:24 (emsal olarak basıldı), okunmamış 1 ayet (sûre içi 1); "
 "7:67 7:61, 26:16, 43:46 (basılmış), okunmuş 1 ayet ve okunmamış 1 ayet (sûre içi 1); 7:68 xref yok; 7:69 xref yok; 7:65 esit2 → 11:50 kademe BENZER; 7:67 esit2 → 7:61 kademe BENZER",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok (7:65-69 ölçümünde nakarat3 alanı boş)'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:65 'qâle qavm 'abede allâh mâ _ min ilâh ğayr' süzgeç GEÇER; 7:66 'qâle mele' ellezî kefere min qavm' süzgeç GEÇER, 'min qavm inne ra'â fî' süzgeç GEÇER, 'qâle mele' ellezî' süzgeç GEÇER; 7:67 'lâkinne rasûl min rabb 'âlem' süzgeç GEÇER, 'rasûl min rabb 'âlem' süzgeç GEÇER, 'qâle qavm leyse _' süzgeç GEÇER; "
 "7:68 'belliğ risâle rabb' süzgeç GEÇMEZ; 7:69 ''acibu en câ'e zikr min rabb 'alâ racul min enzere' süzgeç GEÇER, 'zekere iz ce'ale xalîfe min ba'd' süzgeç GEÇER, 'zekere âlâ' allâh' süzgeç GEÇMEZ; sûre içi eşler — bölüm 7-1 bloğundaki Nûh kıssası ayetleri (basılmış) ve basılmamış eşler",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:65 3MS ('qâle' — gönderge 'hûden' 4. kelime; ek 'ğayruhû' — söz içi, gönderge 'llâhe' 8. kelime), 3MP eki ('exâhum' — gönderge ''âdin' 2. kelime), söz içi konuşan 1S eki ('qavmi'), söz içi muhatap 2MP ('u'budu', 'tetteqûn'; ek 'lekum'); aktör adlı ''âdin', 'hûden'; "
 "7:66 3MS ('qâle' — fiil uyumu, fail 2. kelime; ek 'qavmihî' — gönderge 7:65 4. kelime), 3MP ('kefarû' — gönderge 'llezîne' 3. kelime), söz içi konuşan 1P ('nerâke', 'nezunnuke'; ekler 'innâ', 've innâ'), söz içi muhatap 2MS eki ('nerâke', 'nezunnuke'); "
 "7:67 3MS ('qâle' — gönderge 7:65 4. kelime; 'leyse' — söz içi, fiil uyumu, fail 5. kelime), söz içi konuşan 1S eki ('qavmi', 'bî', 'lâkinnî'); 7:68 söz içi konuşan 1S ('ubelliğukum', 'ene'; ek 'rabbî'), söz içi muhatap 2MP eki ('ubelliğukum', 'lekum'); "
 "7:69 söz içi muhatap 2MP (''acibtum', 'zkurû', 'zkurû', 'tuflihûn'; ekler 'câ'ekum', 'rabbikum', 'minkum', 'yunzirakum', 'ce'alekum', 'zâdekum', 'le'allekum'), 3MS ('câ'ekum' — söz içi, fiil uyumu, fail 4. kelime; 'yunzirakum' — söz içi, gönderge 'raculin' 8. kelime; 'ce'alekum', 'zâdekum' — söz içi, gönderge 'rabbikum' 6. kelime); aktör adlı 'nûhin', adsız 'raculin'",
 "7:65-69 gönderge zinciri: 7:65 'qâle' 3MS göndergesi 'hûden' (4. kelime); 7:66 'qavmihî' ve 7:67 'qâle' göndergesi 7:65 4. kelimedeki Hûd; 7:67-69 söz içi konuşan 1S Hûd, muhatap 2MP kavmi (7:66 'l-mele'u' 2. kelime ile eş hitap); 7:69 'yunzirakum' göndergesi 'raculin' (8. kelime); 7:69 'ce'alekum', 'zâdekum' göndergesi 'rabbikum' (6. kelime) (okuma)",
 "edilgen: 7:65, 7:66, 7:67, 7:68 ve 7:69 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:65 söz içi 6-15. kelime ('qâle' 5. kelime ardından; ayet içinde kapanıyor); 7:66 söz içi 7-14. kelime ('qâle' 1. kelime ardından; ayet içinde kapanıyor); "
 "7:67 söz içi 2-10. kelime ('qâle' 1. kelime ardından; ayet sonunda kapanmıyor), 7:68 söz sürüyor (1-7. kelime; ayet sonunda kapanmıyor), 7:69 söz sürüyor (1-27. kelime; 27. kelimede kapanıyor); "
 "REM sapması 7:67 (6. kelime) — 'lâkinne' önündeki istidrak 've'si, söz içi cümle başı; REM sapması 7:68 (4. kelime) — söz içi isim cümlesi başı; REM sapması 7:69 (11. kelime) — söz içi emir cümlesi başı; REM sapması 7:69 (23. kelime) — söz içi sonuç 'fe'si, emir cümlesi başı; "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 65 69 19' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 7:65 've ilâ' (1.) CONJ, 'e-fe-lâ' (14.) SUP; 7:66 've innâ' (11.) CONJ; 7:67 've lâkinnî' (6.) REM; 7:68 've ene' (4.) REM; 7:69 'e-ve-'acibtum' (1.) CONJ, 've'zkurû' (11.) REM, 've zâdekum' (19.) CONJ, 'fe'zkurû' (23.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:69 ◈B خلق ('l-xalqi' 21. kelime — B2); 7:65, 7:66, 7:67 ve 7:68 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 65 69 19'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:66 (11:27, 23:24); D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:65 أله ×2; 7:69 ذكر ×3; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: bloğun emsal dosyasında olmayan basılmış eş (önceki bloklarda basılmış ya da sûre içi), bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:65 söz açılır / kapanır, şahıs geçişi 3 → 2, edim geçişi haber → soru, emir, nida; 7:66 söz açılır / kapanır, şahıs sayısında beraberlik (1P 4 · 3. şahıs 4 — ölçüm baskın 1), şahıs geçişi 2 → 1, edim geçişi soru, emir, nida → haber; 7:67 söz açılır, şahıs geçişi yok, edim geçişi haber → nida; "
 "7:68 şahıs geçişi yok, edim geçişi nida → haber; 7:69 söz kapanır, şahıs geçişi 1 → 2, edim geçişi haber → soru, emir; ölçüm iltifât 7:65-69 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:65 've ilâ 'âdin exâhum hûden' — atıf, öne alınmış tümleç ve mansub özel ad (morph CONJ + P + PN + N + PN); 7:66 'innâ le-nerâke fî sefâhetin' — tekit edatı ve lâm ile muzâri (morph ACC + EMPH + IMPF); 7:67 'leyse bî sefâhetun' — olumsuz nakıs fiil, öne alınmış haber (morph V + P + NOM); "
 "7:68 've ene lekum nâsihun emîn' — istînâf, zamir mübteda ve haber (morph REM + PRON + P + ACT_PCPL); 7:69 've'zkurû iz ce'alekum xulefâ'e' — istînâf, emir ve zaman zarfı (morph REM + IMPV + T + PERF)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:66 2-5. kelime — 11:27 ile harekesiz eş (sayım: 'say 7:66 2-5'); 7:66 3-6. kelime — 11:27 ve 23:24 ile harekesiz eş (sayım: 'say 7:66 3-6'); "
 "7:65 1-4. kelime ile açılıyor — 11:50 ile harekesiz eş (sayım: 'say 7:65 1-4'); 7:65 kök أله ikilemesi; 7:69 kök ذكر ikilemesi; geniş eşli sayımlar: 'say 7:65 9-13', 'say 7:65 5-13', 'say 7:67 6-10', 'say 7:69 1-9', 'say 7:69 1-10', 'say 7:69 11-16', 'say 7:66 5-9'",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 19'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'l-mele'u'llezîne kefarû min' 7:66 'inkâr eden ileri gelenler' / 11:27 'inkâr eden ileri gelenler' (emsal metninde) — çakışma değil; "
 "'llezîne kefarû min qavmihî' 7:66 'Kavminden inkâr eden' / 23:24 'Kavminden inkâr eden' (emsal metninde) — çakışma değil; "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:65 'qâle' PERF — meal 'Dedi'; 'u'budu' IMPV — meal 'kulluk edin'; 'tetteqûn' IMPF IND ('e-fe-lâ' ile) — meal 'Sakınmaz mısınız'; "
 "7:66 'qâle' PERF — meal 'dedi'; 'kefarû' PERF — meal 'inkâr eden'; 'nerâke' IMPF IND — meal 'görüyoruz'; 'nezunnuke' IMPF IND — meal 'sanıyoruz'; 7:67 'qâle' PERF — meal 'Dedi'; 'leyse' PERF — meal 'yok'; 7:68 'ubelliğukum' IMPF IND — meal 'tebliğ ediyorum'; "
 "7:69 ''acibtum' PERF — meal 'şaştınız'; 'câ'ekum' PERF ('en' ile) — meal 'gelmesine'; 'yunzirakum' IMPF SUBJ — meal 'uyarması'; 'zkurû' IMPV (11. kelime) — meal 'hatırlayın'; 'ce'alekum' PERF — meal 'kıldığı'; 'zâdekum' PERF — meal 'artırdı'; 'zkurû' IMPV (23. kelime) — meal 'hatırlayın'; 'tuflihûn' IMPF IND — meal 'erersiniz'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle; IMPF IND geniş zaman karşılığı her blokta sapma sayılır — sûre 7 bölüm 3 denetimi kuralı 3): 'tetteqûn' IMPF 7:65'te geniş zaman sorusu ('-maz mısınız') ile; 'kefarû' PERF 7:66'da sıfat-fiil ('-en') ile; 'nerâke', 'nezunnuke' IMPF 7:66'da şimdiki zaman ('-üyoruz', '-ıyoruz') ile; 'leyse' PERF 7:67'de olumsuz varlık ('yok') ile; "
 "'ubelliğukum' IMPF 7:68'de şimdiki zaman ('-iyorum') ile; 'câ'ekum' PERF 7:69'da mastar ('-mesi') ile; 'yunzirakum' IMPF 7:69'da mastar ('-ması') ile; 'ce'alekum' PERF 7:69'da sıfat-fiil ('-dığı') ile; 'tuflihûn' IMPF 7:69'da geniş zaman ('-ersiniz') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): 'e' ('mi' / 'mı') — çakışma değil (ünlü uyumu); 'ellezîne' (REL: '-anları' / '-en') — çakışma değil (sıfat-fiil çekimi); 'fe' ('Öyleyse' / karşılıksız) — çakışma değil (sonuç 'fe'si / anlatı 'fe'si); 'hum' ('onlar' / iyelik eki) — çakışma değil (özne, tamlama); 'li' ('için' / tamlayan eki / yönelme eki) — çakışma değil (amaç, sahiplik, yön)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 65 69 19'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:69 tarayıcı adayı (kök خلق; B_ta'lîl, C_recâ) — çıpa değil: yaratılışta genişlik artışı adlanıyor, ölçü / mekanizma yok (olgu=True, kademe L1); 7:65, 7:66, 7:67 ve 7:68 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:65, 7:66, 7:67, 7:68 ve 7:69 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök قول 7:65 ('qâle'), 7:66 ('qâle') ve 7:67 ('qâle') ile bölüm içi; kök قوم 7:65 ('qavmi'), 7:66 ('qavmihî'), 7:67 ('qavmi') ve 7:69 ('qavmi') ile bölüm içi; kök ربب 7:67 ('rabbi'), 7:68 ('rabbî') ve 7:69 ('rabbikum') ile bölüm içi; kök رسل 7:67 ('rasûlun') ve 7:68 ('risâlâti') ile bölüm içi; kök سفه 7:66 ('sefâhetin') ve 7:67 ('sefâhetun') ile bölüm içi; kök أله 7:65 ('llâhe', 'ilâhin') ve 7:69 ('llâhi') ile bölüm içi; bölümün önceki bloğuyla ortak kökler: بلغ (7:62 / 7:68), جيأ (7:63 / 7:69), ذكر (7:63 / 7:69), رأي (7:60 / 7:66), رجل (7:63 / 7:69), عبد (7:59 / 7:65), عجب (7:63 / 7:69), علم (7:61, 7:62 / 7:67), غير (7:59 / 7:65), كذب (7:64 / 7:66), ليس (7:61 / 7:67), ملأ (7:60 / 7:66), نذر (7:63 / 7:69), نصح (7:62 / 7:68), وقي (7:63 / 7:65); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 7-2 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 18, 19 ve 20; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b19/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 65 69 19'; lem_bozuk.py 19 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 65 69 → AYN_SONUC; sunum/bolum4_kurallar.py 65 69 19 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 65 69 19 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 43)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 19 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('ilâ', ''âd', 'ax', 'hûd', 'qâle', 'qavm', ''abede', 'allâh', 'mâ', 'min', 'ilâh', 'ğayr', 'mele'', 'ellezî', 'kefere', 'inne', 'ra'â', 'fî', 'leyse', 'lâkinne', 'rasûl', 'rabb', ''âlem', 'risâle', 'belliğ' (morph LEM ham biçim), ''acibu' (morph LEM ham biçim), 'en', 'câ'e', 'zikr', ''alâ', 'racul', 'enzere', 'zekere', 'iz', 'ce'ale', 'xalîfe', 'ba'd', 'âlâ''); joker '_' dizi lemma dizisinde boş öğe olan önek lemmalı kelimelerde ('lekum' 7:65 10., 'bî' 7:67 4.); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (65, 69): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_7_65_69.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_7_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_7_b17k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '65', '69'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '65', '69', '19'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '65', '69', '19'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '65', '69', '19', '--tazelik-yok')}
    for _n in range(7, 43): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '65', '69', '19')
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

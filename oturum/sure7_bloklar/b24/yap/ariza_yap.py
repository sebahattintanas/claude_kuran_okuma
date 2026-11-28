# sûre 7 blok 24 (7:85-87) ARIZA oluşturucu — bölüm 9-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b24/olcum.txt'
os.environ['SAY2'] = '/home/claude/b24/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = list(ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_7_b23.txt', encoding='utf-8').read() + ']'))
VF_YAZI_ESKI = {}
BOL = "'Şuayb ve Medyen'"


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
 ('7:85', "'qâle qavm 'abede allâh mâ _ min ilâh ğayr qad câ'e beyyine min rabb'", 2, 'say 7:85 5-18', "harekesiz 'qâle yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû qad câ'etkum beyyinetun min rabbikum' (5-18. kelime)", ('dizi 7 85 5 18', "qâle qavm 'abede allâh mâ _ min ilâh ğayr qad câ'e beyyine min rabb", '5-18', "biçim farkı (dizi 7 85 5 18): 7:73 yazım eş")),
 ('7:85', "'qâle qavm 'abede allâh mâ _ min ilâh ğayr'", 4, 'say 7:85 5-13', "harekesiz 'qâle yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû' (5-13. kelime)", ('dizi 7 85 5 13', "qâle qavm 'abede allâh mâ _ min ilâh ğayr", '5-13', "biçim farkı (dizi 7 85 5 13): 7:59 önek; 7:65 yazım eş; 7:73 yazım eş; öneksiz eş koşusu (dizi 7 85 5 13): 7:59 → önek kesilmiş sûre içi 1; 7:65 → önek kesilmiş sûre içi 4; 7:73 → önek kesilmiş sûre içi 4")),
 ('7:85', "'lâ efsedu fî ard ba'd islâh'", 2, 'say 7:85 26-31', "harekesiz 've lâ tufsidû fi'l-ardi ba'de islâhihâ' (26-31. kelime)", ('dizi 7 85 26 31', "lâ efsedu fî ard ba'd islâh", '26-31', "biçim farkı (dizi 7 85 26 31): 7:56 yazım eş")),
 ('7:85', "'qad câ'e beyyine min rabb'", 3, 'say 7:85 14-18', "harekesiz 'qad câ'etkum beyyinetun min rabbikum' (14-18. kelime)", ('dizi 7 85 14 18', "qad câ'e beyyine min rabb", '14-18', "biçim farkı (dizi 7 85 14 18): 7:73 yazım eş; basılmamış eş fiil çekimi, i'râb, zamir eki, önek; öneksiz eş koşusu (dizi 7 85 14 18): 7:73 → önek kesilmiş sûre içi 2; basılmamış eş → önek kesilmiş sûre içi 1")),
 ('7:85', "'efsedu fî ard'", 3, 'say 7:85 27-29', "harekesiz 'tufsidû fi'l-ardi' (27-29. kelime)", ('dizi 7 85 27 29', "efsedu fî ard", '27-29', "biçim farkı (dizi 7 85 27 29): 7:56 yazım eş; basılmamış eş fiil çekimi, zamir eki, önek; öneksiz eş koşusu (dizi 7 85 27 29): 7:56 → önek kesilmiş sûre içi 2; basılmamış eş → önek kesilmiş sûre içi 1")),
 ('7:85', "'_ in kâne'", 2, 'say 7:85 34-36', "harekesiz 'lekum in kuntum' (34-36. kelime); biçim öğesi 'kum' zamir eki (lemma dizisi sûre içi 3, nakarat3 2)", ('dizi 7 85 34 36', "_ in kâne", '34-36', "biçim farkı (dizi 7 85 34 36): basılmamış eş fiil çekimi, zamir eki, önek; basılmamış eş yazım eş; öneksiz eş koşusu (dizi 7 85 34 36): basılmamış eş → önek kesilmiş sûre içi 1; basılmamış eş → önek kesilmiş sûre içi 2")),
 ('7:86', "'nazara keyfe kâne 'âqibe mufsid'", 2, 'say 7:86 20-24', "harekesiz 've'nzurû keyfe kâne 'âqibetu'l-mufsidîn' (20-24. kelime)", ('dizi 7 86 20 24', "nazara keyfe kâne 'âqibe mufsid", '20-24', "biçim farkı (dizi 7 86 20 24): basılmamış eş fiil çekimi, zamir eki, önek; öneksiz eş koşusu (dizi 7 86 20 24): basılmamış eş → önek kesilmiş sûre içi 1")),
 ('7:86', "'nazara keyfe kâne 'âqibe'", 3, 'say 7:86 20-23', "harekesiz 've'nzurû keyfe kâne 'âqibetu' (20-23. kelime)", ('dizi 7 86 20 23', "nazara keyfe kâne 'âqibe", '20-23', "biçim farkı (dizi 7 86 20 23): 7:84 fiil çekimi, zamir eki, önek; basılmamış eş fiil çekimi, zamir eki, önek; öneksiz eş koşusu (dizi 7 86 20 23): 7:84 → önek kesilmiş sûre içi 2; basılmamış eş → önek kesilmiş sûre içi 2")),
 ('7:86', "'sadde 'an sebîl allâh'", 2, 'say 7:86 6-9', "harekesiz 've tesuddûne 'an sebîli'llâhi' (6-9. kelime)", ('dizi 7 86 6 9', "sadde 'an sebîl allâh", '6-9', "biçim farkı (dizi 7 86 6 9): 7:45 fiil çekimi, zamir eki, önek; öneksiz eş koşusu (dizi 7 86 6 9): 7:45 → önek kesilmiş sûre içi 1")),
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

VF_YAZI = {85: {1: "'ve ilâ'", 6: "'yâ qavmi'", 10: "'lekum'", 19: "'fe-evfu'", 21: "'ve'l-mîzâne'", 22: "'ve lâ'", 26: "'ve lâ'", 34: "'lekum'"}, 86: {1: "'ve lâ'", 3: "'bi-kulli'", 6: "'ve tesuddûne'", 12: "'bihî'", 13: "'ve tebğûnehâ'", 15: "'ve'zkurû'", 19: "'fe-kesserakum'", 20: "'ve'nzurû'"}, 87: {1: "'ve in'", 6: "'bi'llezî'", 8: "'bihî'", 9: "'ve tâ'ifetun'", 12: "'fe'sbirû'", 17: "'ve huve'"}}
sys.path.insert(0, '/home/claude/b24/yap')
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
open('/home/claude/b24/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '24')
BLOKLAR = [str(i) for i in range(1, 25)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '24', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b24/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '85', '87', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b24/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b24/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '85', '87', '24').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_85_87.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'7:85', '7:86', '7:87'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_85_87.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '7:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '7:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(85, 88))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "7:85 kök بعد ('ba'de' 30. kelime — morph T, zaman); 7:86 kök صدد ('tesuddûne' 6. kelime — alıkoyma); 7:86 'iz' (16. kelime — morph T, zaman): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '85', '87', '24')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b24/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 25)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b7:%d:\d+' % a_, s_) for a_ in range(85, 88))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
_OL = [l.replace('**', '') for l in open('/home/claude/b24/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b24/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK1 = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[0]).group(0))
_AK3 = _esc(re.search(r'aktör: adsız `tâife` 3\. sırada · adsız `tâife` 9\. sırada', _OL[2]).group(0))
for _k, _v in (('_AK1', _AK1), ('_AK3', _AK3)): _MB = _MB.replace('" + %s + "' % _k, _v)
_MB = _MB.replace('sayı işareti \\S+, \\S+', re.search(r'sayı işareti \S+, \S+', _OL[1]).group(0))
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 84), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta araç kuralı değişmedi; bölüm 8 kapanışında sunum/bolum44_kurallar.py (kural 1-5) eklendi, sunum/geriye_donuk.py ve mutasyon_sina buna göre güncellendi — önceki commit'te, kapanış mutasyon sınaması 465 / 465; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 516",
 "geriye dönük koşu (sûre 7 bölüm 8 kapanışı, komut 'python3 sunum/geriye_donuk.py b23k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 85 87 24'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:85 'in kuntum mu'minîn' (35-37. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (inananların sıfatı) (yamalar/esma_el_7_85_87.txt); 7:86 ve 7:87 esmâ yok; 7:85 lafız (8. kelime), 7:86 lafız (9. kelime), 7:87 lafız (15. kelime); 7:85 Rab (18. kelime); 7:86 ve 7:87 Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 85 87 24'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 7:85 muhur EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, araç tanımı farkı; muhur_el hayır): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in range(85, 88)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 85 87 24'): KALAN_P",
 "ölçüm aktör: 7:85 adlı مَدْيَن (2. kelime, rol mecrur) ve شُعَيْب (4. kelime, rol meful); 7:86 aktör yok; 7:87 adsız tâife (3. ve 9. kelime)",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:85 emir, yasak, nida, şart — CERT 1 'qad' (14.), COND 1 'in' (35.), IMPV 2 'u'budu' (7.), 'fe-evfu' (19.), NEG 1 'mâ' (9.), PRO 2 've lâ' (22.), 've lâ' (26.), VOC 1 'yâ qavmi' (6.); "
 "7:86 emir, yasak — IMPV 2 've'zkurû' (15.), 've'nzurû' (20.), PRO 1 've lâ' (1.); 7:87 emir, şart — COND 1 've in' (1.), IMPV 1 'fe'sbirû' (12.), NEG 1 'lem' (10.)",
 "morph DEM ('zâlikum' 7:85 32.), REL ('men' 7:86 10., 'bi'llezî' 7:87 6.), T ('iz' 7:86 16.), RSLT ('fe'sbirû' 7:87 12.), LOC ('beynenâ' 7:87 16.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:85 ★★ (kaynak n, z=2,61); 7:86 ve 7:87 yıldız yok",
 "fâsıla: 7:84 ن → 7:85 ن (" + _F[0] + ") → 7:86 ن (" + _F[1] + ") → 7:87 ن (" + _F[2] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:85 11:85, 11:86, 26:183, 29:36 (emsal olarak basıldı), 6:152, 6:157, 7:59, 7:65, 7:73, 11:50, 11:61, 11:84, 23:23, 23:32, 40:66 (basılmış), okunmuş 1 ayet ve okunmamış 1 ayet (sûre içi 1); "
 "7:86 3:99, 27:14 (emsal olarak basıldı), okunmamış 1 ayet (sûre içi 1); 7:87 10:109 (emsal olarak basıldı)",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:85 'qâle qavm 'abede allâh mâ _ min ilâh ğayr qad câ'e beyyine min rabb' süzgeç GEÇER, 'qâle qavm 'abede allâh mâ _ min ilâh ğayr' süzgeç GEÇER, 'lâ efsedu fî ard ba'd islâh' süzgeç GEÇER, 'qad câ'e beyyine min rabb' süzgeç GEÇER, 'efsedu fî ard' süzgeç GEÇER, '_ in kâne' süzgeç GEÇMEZ; "
 "7:86 'nazara keyfe kâne 'âqibe mufsid' süzgeç GEÇER, 'nazara keyfe kâne 'âqibe' süzgeç GEÇER, 'sadde 'an sebîl allâh' süzgeç GEÇER; 7:87 nakarat3 kalıbı yok; sûre içi eşler — 7:45, 7:56, 7:59, 7:65, 7:73 ve 7:84 (basılmış) ve basılmamış eşler",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:85 adlı 'medyene' (2.) ve 'şu'ayban' (4.); 3MP eki ('exâhum' — gönderge 'medyene'; 'eşyâ'ehum' — söz içi, gönderge 'n-nâse' 24. kelime), 3MS ('qâle' — gönderge 'şu'ayban'; ek 'ğayruhû' — gönderge 'llâhe' 8. kelime), söz içi konuşan 1S eki ('qavmi'), söz içi muhatap 2MP ('u'budu', 'evfu', 'tebxasu', 'tufsidû', 'kuntum'; ekler 'lekum', 'câ'etkum', 'rabbikum', 'lekum'), 3FS ('câ'etkum' — fiil uyumu, fail 16. kelime; ek 'islâhihâ' — gönderge 'l-ardi' 29. kelime); "
 "7:86 söz içi muhatap 2MP ('taq'udû', 'tû'idûne', 'tesuddûne', 'tebğûnehâ', 'zkurû', 'kuntum', 'nzurû'; ek 'kesserakum'), 3MS ('âmene' — gönderge 'men' 10. kelime; 'kesserakum' ve ek 'bihî' — tartışmalı; gönderge 'llâhi' 9. kelime; 'kâne' — fiil uyumu, fail 23. kelime), 3FS eki ('tebğûnehâ' — cins uyumsuz; gönderge 'sebîli' 8. kelime); "
 "7:87 adsız 'tâ'ifetun' (3. ve 9.); 3MS ('kâne' — fiil uyumu, fail 3. kelime; 'yahkume' — fiil uyumu, fail 15. kelime; ek 'bihî' — gönderge 'llezî' 6. kelime; zamir 'huve' — gönderge 'llâhu' 15. kelime), 3MP ('âmenû' — cins ve sayı uyumsuz; gönderge 'tâ'ifetun' 3. kelime; 'yu'minû' — cins ve sayı uyumsuz; gönderge 'tâ'ifetun' 9. kelime), söz içi konuşan 1S ('ursiltu' — edilgen), söz içi muhatap 2MP ('sbirû'; ek 'minkum'), söz içi konuşan 1P eki ('beynenâ')",
 "7:85-87 gönderge zinciri: 7:85 'qâle' göndergesi 'şu'ayban' (4. kelime); 7:86 ve 7:87 söz 7:85'ten sürüyor; 7:87 'âmenû' ve 'yu'minû' göndergesi 'tâ'ifetun' (3. ve 9. kelime) (okuma)",
 "edilgen: 7:87 'ursiltu' (7. kelime, IV. bab) — ölçüm EDİLGEN 1/6 fiil; 7:85 ve 7:86 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:85 söz içi 6-37. kelime ('qâle' 5. kelime ardından; ayet sonunda kapanmıyor); 7:86 söz sürüyor (7:85 6. kelimeden, 1-24. kelime; ayet sonunda kapanmıyor); 7:87 söz sürüyor (7:85 6. kelimeden, 1-19. kelime; 19. kelimede kapanır); "
 "REM sapması 7:85 (19. kelime) — söz içi 'fe', emir cümlesi başı; REM sapması 7:85 (22. kelime) — söz içi 've', yasak cümlesi başı; REM sapması 7:86 (15. kelime) — söz içi 've', emir cümlesi başı; REM sapması 7:87 (1. kelime) — söz içi 've', şart cümlesi başı; REM sapması 7:87 (17. kelime) — söz içi 've', isim cümlesi başı; "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 85 87 24' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 7:85 've ilâ' (1.) CONJ, 'fe-evfu' (19.) REM, 've'l-mîzâne' (21.) CONJ, 've lâ' (22.) REM, 've lâ' (26.) CONJ; 7:86 've lâ' (1.) CONJ, 've tesuddûne' (6.) CONJ, 've tebğûnehâ' (13.) CONJ, 've'zkurû' (15.) REM, 'fe-kesserakum' (19.) CONJ, 've'nzurû' (20.) CONJ; 7:87 've in' (1.) REM, 've tâ'ifetun' (9.) CONJ, 'fe'sbirû' (12.) RSLT, 've huve' (17.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:85 ◈B أنس ('n-nâse' 24. kelime — B1), 7:85 ◈K أرض ('l-ardi' 29. kelime — K1); 7:86 ve 7:87 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 85 87 24'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:85 (29:36, 11:85, 26:183, 11:86), 7:86 (3:99, 27:14), 7:87 (10:109); D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:85 أله ×2; 7:86 كون ×2; 7:87 أمن ×2, حكم ×2, طوف ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: bloğun emsal dosyasında olmayan basılmış eş (önceki bloklarda basılmış ya da sûre içi), bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:85 bölüm açılışı, söz açılır, şart → cevap (COND 'in' 35. kelime; cevap 'zâlikum' 32. kelime — öne alınmış), şahıs geçişi 1 → 2, edim geçişi emir → emir, yasak, nida, şart; 7:86 şahıs geçişi yok, edim geçişi emir, yasak, nida, şart → emir, yasak; "
 "7:87 söz kapanır, şart → cevap (COND 've in' 1. kelime; cevap 'fe'sbirû' 12. kelime), şahıs geçişi 2 → 3, edim geçişi emir, yasak → emir, şart; ölçüm iltifât 7:85-87 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:85 've ilâ medyene exâhum şu'ayban' — bağlaç, yönelme ve özel adlar; fiil takdiri — 7:59 yönetimi (morph CONJ + P + PN + N + PN); 7:86 've lâ taq'udû bi-kulli sirâtin' — bağlaç, yasak edatı ile muzâri ve tümleç (morph CONJ + PRO + IMPF + P + N + N); "
 "7:87 've in kâne tâ'ifetun minkum' — istînâf, şart edatı, nâkıs fiil ve nekre isim (morph REM + COND + PERF + N + P)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:85 1-4. kelime — 29:36 ile harekesiz eş (sayım: 'say 7:85 1-4'); 7:85 22-25. kelime — 11:85 ve 26:183 ile harekesiz eş (sayım: 'say 7:85 22-25'); "
 "7:85 33-37. kelime — 11:86 ile lemma dizisi eşi (sayım: 'dizi 7 85 33 37'); 7:86 6-11. kelime — 3:99 ile lemma dizisi eşi (sayım: 'dizi 7 86 6 11'); 7:87 17-19. kelime — 10:109 ile harekesiz eş (sayım: 'say 7:87 17-19'); 7:87 12-15. kelime — 10:109 ile lemma dizisi eşi (sayım: 'dizi 7 87 12 15'); 7:87 13-15. kelime — 10:109 ile harekesiz eş (sayım: 'say 7:87 13-15'); 7:85 kök أله ikilemesi; 7:86 kök كون ikilemesi; 7:87 kök أمن, حكم ve طوف ikilemesi; geniş eşli sayımlar: 'say 7:85 5-13', 'say 7:85 5-18', 'say 7:85 26-31', 'say 7:85 33-37'",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 24'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'ve ilâ medyene exâhum şu'ayban' 7:85 'Medyen'e de kardeşleri Şuayb'ı gönderdik' / 29:36 'Medyen'e de kardeşleri Şuayb'ı gönderdik' (emsal metninde) — çakışma değil; 'u'budu'llâhe' 7:85 'Allah'a kulluk edin' / 29:36 'Allah'a kulluk edin' (emsal metninde) — çakışma değil; "
 "'ve lâ tebxasu'n-nâse eşyâ'ehum' 7:85 'insanların eşyasını eksiltmeyin' / 11:85 'insanların eşyasını eksiltmeyin' (emsal metninde) — çakışma değil; "
 "'ve lâ tebxasu'n-nâse eşyâ'ehum' 7:85 'eşyasını eksiltmeyin' / 26:183 'eşyasını eksiltmeyin' (emsal metninde) — çakışma değil (alıntı 'insanların' dışında — emsaller arası: 11:85 'insanların' / 26:183 'İnsanların', harf büyüklüğü); "
 "'xayrun lekum' 7:85 'sizin için daha hayırlıdır' / 11:86 'sizin için daha hayırlıdır' (emsal metninde) — çakışma değil; "
 "'sebîli'llâhi' 7:86 'Allah'ın yolundan' / 3:99 'Allah'ın yolundan' (emsal metninde) — çakışma değil (daraltılmış kalıp — ''an' öneki dışarıda); "
 "'keyfe kâne' 7:86 'nasıl oldu' / 27:14 'nasıl olmuş' (emsal metninde) — çakışma — tam okuma sonu (daraltılmış kalıp; '-du' / '-muş' — kip; 'say 7:86 20-24' korpusta 1, 'dizi 7 86 20 24' 27:14 ile eş — yazım / çekim farkı); "
 "'hattâ yahkume'llâhu' 7:87 'hükmedinceye kadar' / 10:109 'hükmedinceye kadar' (emsal metninde) — çakışma değil; 've huve' 7:87 'O' / 10:109 'O' (emsal metninde) — çakışma değil; 'xayru'l-hâkimîn' 7:87 'hükmedenlerin en hayırlısıdır' / 10:109 'hükmedenlerin en hayırlısıdır' (emsal metninde) — çakışma değil (daraltılmış kalıp — 'huve' dışarıda); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:85 'qâle' PERF — meal 'Dedi'; 'u'budu' IMPV — meal 'kulluk edin'; 'câ'etkum' PERF ('qad' ile) — meal 'geldi'; 'fe-evfu' IMPV — meal 'tam yapın'; 'tebxasu' IMPF JUS ('lâ' ile) — meal 'eksiltmeyin'; 'tufsidû' IMPF JUS ('lâ' ile) — meal 'yapmayın'; 'kuntum' PERF (36. kelime; 'in' ile) — meal 'iseniz'; "
 "7:86 'taq'udû' IMPF JUS ('lâ' ile) — meal 'oturmayın'; 'tû'idûne' IMPF IND — meal 'tehdit ederek'; 'tesuddûne' IMPF IND — meal 'alıkoyarak'; 'âmene' PERF — meal 'edeni'; 'tebğûnehâ' IMPF IND — meal 'isteyerek'; 've'zkurû' IMPV — meal 'Hatırlayın'; 'kuntum' PERF (17. kelime; 'iz' ile) — meal 'idiniz'; 'fe-kesserakum' PERF — meal 'çoğalttı'; 've'nzurû' IMPV — meal 'Bakın'; 'kâne' PERF — meal 'oldu'; "
 "7:87 'kâne' PERF ('in' ile) — meal 'etmiş'; 'âmenû' PERF — meal 'iman etmiş'; 'ursiltu' PERF edilgen — meal 'gönderilene'; 'yu'minû' IMPF JUS ('lem' ile) — meal 'etmemişse'; 'fe'sbirû' IMPV — meal 'sabredin'; 'yahkume' IMPF SUBJ ('hattâ' ile) — meal 'hükmedinceye'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle; IMPF IND geniş zaman karşılığı her blokta sapma sayılır — sûre 7 bölüm 3 denetimi kuralı 3): 'kuntum' PERF 7:85'te şart ('-seniz') ile; 'tû'idûne', 'tesuddûne', 'tebğûnehâ' IMPF 7:86'da ulaç ('-erek', '-arak', '-yerek') ile; 'âmene' PERF 7:86'da sıfat-fiil ('-eni') ile; "
 "'kâne', 'âmenû' PERF 7:87'de şart ve miş'li geçmiş ('-miş') ile; 'ursiltu' PERF 7:87'de sıfat-fiil ('-ene') ile; 'yahkume' IMPF 7:87'de zarf-fiil ('-inceye') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 85 87 24'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:85 tarayıcı adayı (kök أرض; A_şart, D_yeti) — çıpa değil: buyruk, doğa iddiası yok; 7:86 tarayıcı adayı (F_ölçü) — çıpa değil: anlatı öğesi; 7:87 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:85 ('tufsidû' / 'islâhihâ'); 7:86 ('qalîlen' / 'fe-kesserakum'); 7:87 ('âmenû' / 'lem yu'minû'); ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök أله 7:85 ('llâhe', 'ilâhin'), 7:86 ('llâhi') ve 7:87 ('llâhu') ile bölüm içi; kök أمن 7:85 ('mu'minîn'), 7:86 ('âmene') ve 7:87 ('âmenû', 'yu'minû') ile bölüm içi; kök بين 7:85 ('beyyinetun') ve 7:87 ('beynenâ') ile bölüm içi; kök خير 7:85 ('xayrun') ve 7:87 ('xayru') ile bölüm içi; kök فسد 7:85 ('tufsidû') ve 7:86 ('l-mufsidîn') ile bölüm içi; kök كون 7:85 ('kuntum'), 7:86 ('kuntum', 'kâne') ve 7:87 ('kâne') ile bölüm içi; bölüm açılışı — bölümün önceki bloğu yok; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 9-1 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 24, 25 ve 26; bölüm açılışı bu blokta; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b24/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 85 87 24'; lem_bozuk.py 24 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 85 87 → AYN_SONUC; sunum/bolum4_kurallar.py 85 87 24 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 85 87 24 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 45)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 24 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('ilâ', 'medyen', 'ax', 'şu'ayb', 'qâle', 'qavm', ''abede', 'allâh', 'sabera', 'hattâ', 'hakeme', 'mâ', 'min', 'ilâh', 'ğayr', 'qad', 'câ'e', 'beyyine', 'rabb', 'lâ', 'yebxas' (morph LEM ham biçim), 'nâs', 'şey'', 'efsedu' (morph LEM ham biçim), 'fî', 'ard', 'ba'd', 'islâh', 'xayr', 'in', 'kâne', 'mu'min', 'sadde', ''an', 'sebîl', 'men', 'âmene', 'nazara', 'keyfe', ''âqibe', 'mufsid', 'hâkim'); joker '_' dizi lemma dizisinde boş öğe olan zamir ve önek lemmalı kelimelerde ('lekum' 7:85 10. ve 34., 've huve' 7:87 17.); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (85, 87): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_7_85_87.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_7_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_7_b23k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '85', '87'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '85', '87', '24'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '85', '87', '24'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '85', '87', '24', '--tazelik-yok')}
    for _n in range(7, 45): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '85', '87', '24')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37, B38, B39, B40, B41, B42, B43, B44 = [_R['B%d' % _n].splitlines() for _n in range(6, 45)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'B31_HEPSI': (B31[-1] if B31 else '?'), 'B32_HEPSI': (B32[-1] if B32 else '?'), 'B33_HEPSI': (B33[-1] if B33 else '?'), 'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'), 'B37_HEPSI': (B37[-1] if B37 else '?'), 'B38_HEPSI': (B38[-1] if B38 else '?'), 'B39_HEPSI': (B39[-1] if B39 else '?'), 'B40_HEPSI': (B40[-1] if B40 else '?'), 'B41_HEPSI': (B41[-1] if B41 else '?'), 'B42_HEPSI': (B42[-1] if B42 else '?'), 'B43_HEPSI': (B43[-1] if B43 else '?'), 'B44_HEPSI': (B44[-1] if B44 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37, B38, B39, B40, B41, B42, B43, B44): print([l for l in _x if l.startswith('HATA') or 'hata' in l])

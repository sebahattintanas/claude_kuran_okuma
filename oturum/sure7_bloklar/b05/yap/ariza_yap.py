# sûre 7 blok 5 (7:19-21) ARIZA oluşturucu — bölüm 2-3
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b05/olcum.txt'
os.environ['SAY2'] = '/home/claude/b05/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {}
BOL = "'Âdem'e secde; İblis'in mühleti; ağaç ve iniş'"


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

VF_YAZI = {19: {1: "'ve yâ âdemu'", 4: "'ve zevcuke'", 10: "'ve lâ'"}, 20: {11: "'ve qâle'"}, 21: {1: "'ve qâsemehumâ'"}}
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
ONC = run('/home/claude/sunum/onceki_basim.py', '19', '21', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b05/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b05/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '19', '21', '05').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_19_21.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'7:19', '7:20', '7:21'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_19_21.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '7:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '7:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(19, 22))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "7:20 kök سوأ ('sev'âtihimâ' 10. kelime — çirkin yer): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '19', '21', '05')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b05/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 6)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b7:%d:\d+' % a_, s_) for a_ in range(19, 22))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
_OL = [l.replace('**', '') for l in open('/home/claude/b05/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b05/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 18), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
def _esc(t):
    for c in '.()[]|+': t = t.replace(c, '\\' + c)
    return t
_AK1 = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[0]).group(0))
_AK2 = _esc(re.search(r'aktör: adlı .*?rol fail\)', _OL[1]).group(0))
_E2 = _esc(re.search(r'esit2 → 2:35 oran \S+ kademe BENZER', _OL[0]).group(0))
_SI = _esc(re.search(r'sayı işareti \S+', _OL[0]).group(0))
for _k, _v in (('_AK1', _AK1), ('_AK2', _AK2), ('_E2', _E2), ('_SI', _SI)): _MB = _MB.replace('" + %s + "' % _k, _v)
I = [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta sunum/bolum16_kurallar.py (kural 1) blok 3'te eklenen ayrı zamir sınırını daraltır — harfi cere bitişik zamir ('lehume' 7:20 2. kelime) ayrı zamir sayılmaz, 'fe-vesvese' fiilinin 3. kelimedeki faili aranır; sunum/bolum4_kurallar.py (kural 9) ile sunum/bolum7_kurallar.py (kural 3) şahıs etiketi listesine 2MD ve 2FD eklendi — 7:19 6. kelime 'fe-kulâ' morph 2MD; sunum/edat_etiket.py (bölüm 15 denetimi kuralı 15) zamir listesine 'kumâ' eklendi — 7:20 ve 7:21 ikil muhatap eki; yeni kök yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 382",
 "geriye dönük koşu (sûre 7 bölüm 1 kapanışı, komut 'python3 sunum/geriye_donuk.py b02k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 19 21 05'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:19, 7:20 ve 7:21 esmâ yok; 7:20 Rab (14. kelime); 7:19 ve 7:21 lafız ve Rab yok; 7:20 lafız yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 19 21 05'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in (19, 20, 21)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 19 21 05'): KALAN_P",
 "ölçüm aktör: 7:19 '{{1|" + _AK1 + "}}' (A1'de 'âdemu' ve 'l-cennete'); 7:20 '{{2|" + _AK2 + "}}' (A1'de 'ş-şeytânu' — 'fe-vesvese' faili); 7:21 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:19 emir, yasak, nida — IMPV 2 'skun' (2.), 'kulâ' (6.), PRO 1 'lâ' (10.), VOC 1 'yâ' (1.); ölçüm biçim DIKKAT + NEHY (D2'de yazılmadı); "
 "7:20 haber — NEG 1 'mâ' (12.), RES 1 'illâ' (18.); ölçüm biçim DIKKAT + HASR (D2'de yazılmadı); 7:21 haber — EMPH 1 'le-mine' (4.; 'le'); ölçüm biçim QASEM (D2'de yazılmadı); "
 "morph CAUS ('fe-tekûnâ' 7:19 14.), ATT ('hâzihi' 7:19 12., 7:20 16.), REM ('fe-vesvese' 7:20 1.), PRP ('li-yubdiye' 7:20 4.), SUB ('en' 7:20 19.), ACC ('innî' 7:21 2.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:19, 7:20 ve 7:21 yıldız yok",
 "fâsıla: 7:18 ن → 7:19 ن (" + _F[0] + ") → 7:20 ن (" + _F[1] + ") → 7:21 ن (" + _F[2] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:19 2:35 (emsal olarak basıldı), okunmuş 1 ayet ve okunmamış 1 ayet (sûre içi 1); ölçüm esit2 7:19 → 2:35 (kademe BENZER); 7:20 xref yok; 7:21 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok (7:19, 7:20 ve 7:21 ölçümünde nakarat3 alanı boş)'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:19, 7:20 ve 7:21 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:19 muhatap 2MS ('skun', 'ente' — söz içi; ek 've zevcuke' — söz içi), muhatap 2MD ('fe-kulâ' — söz içi), muhatap 2D ('şi'tumâ', 'taqrabâ', 'fe-tekûnâ' — söz içi; ek 'fe-kulâ' — söz içi), aktör adlı 'âdemu' ve 'l-cennete'; "
 "7:20 3MS ('fe-vesvese' — fiil uyumu, fail 3. kelime; 'li-yubdiye', 've qâle' — gönderge 'ş-şeytânu' 3. kelime; 'vûriye' — edilgen, naib-i faili 'mâ' 6. kelime; 'nehâkumâ' — söz içi, fiil uyumu, fail 14. kelime), 3D eki ('lehume', 'lehumâ', ''anhumâ', 'sev'âtihimâ' — gönderge 7:19 6. kelime), "
 "muhatap 2D ('tekûnâ', 'tekûnâ' — söz içi; ekler 'nehâkumâ', 'rabbukumâ' — söz içi), aktör adlı 'ş-şeytânu'; "
 "7:21 3MS ('ve qâsemehumâ' — gönderge 7:20 3. kelime), 3D eki ('ve qâsemehumâ' — gönderge 7:19 6. kelime), konuşan 1S eki ('innî' — söz içi), muhatap 2D eki ('lekumâ' — söz içi)",
 "7:19-21 gönderge zinciri: 7:19 nida ile muhatap 'âdemu' (1. kelime), 4. kelimeyle eşi katılır ve 6. kelimeden başlayarak muhatap ikil; 7:20 ve 7:21 3D ekleri 7:19 6. kelimeye (iki muhatap); 7:20 3MS fiiller 'ş-şeytânu' (3. kelime), 7:21 fiili de 7:20 3. kelimeye; 7:20 ve 7:21 söz içi muhatap 2D yine 7:19 muhatapları, söz içi konuşan 1S şeytan; 7:20 'rabbukumâ' (14. kelime) söz içinde anılır (okuma)",
 "edilgen: 7:20 'vûriye' (7. kelime; naib-i faili 'mâ') — ölçüm EDİLGEN 1/7; 7:19 ve 7:21 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:19 söz fiili olmadan söz biçimli içerik 1-16. kelime — nida 'yâ âdemu' (1.) ile; 've' (1. kelime, morph CONJ) ile 7:18'deki söze bağlanır, muhatap 7:18'den ayrı; A3'e '(söz biçimli içerik, 1. kelimeden)', A4'te 'söz açılır' / 'söz kapanır' yazılmadı (okuma); "
 "7:20 've qâle' (11.) ardından söz 12-25. kelime — ayet içi kapanış; 7:21 've qâsemehumâ' (1.) ardından söz biçimli içerik 2-5. kelime — fiil قول kökünden değil; A3'e '(söz biçimli içerik, 2. kelimeden)', A4'te 'söz açılır' / 'söz kapanır' yazılmadı (okuma); mealde 'Dedi ki:' ve 'yemin etti:' ardından tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 19 21 05' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 7:19 've yâ âdemu' (1.) CONJ, 've zevcuke' (4.) CONJ, 've lâ' (10.) CONJ; 7:20 've qâle' (11.) CONJ; 7:21 've qâsemehumâ' (1.) CONJ; "
 "'fe' konumları: 7:19 'fe-kulâ' (6.) CONJ, 'fe-tekûnâ' (14.) CAUS; 7:20 'fe-vesvese' (1.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:19 ◈B زوج ('zevcuke' 4. kelime — B2; eş anlamında, üreme anlamı yok (okuma)), 7:19 ◈B شجر ('ş-şecerate' 13. kelime — B1); 7:20 ◈B شجر ('ş-şecerati' 17. kelime — B1); 7:21 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 19 21 05'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:19 (2:35); 7:20 ve 7:21 bağ yok; D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:20 كون ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:19 söz biçimli içerik (A4'te söz kaydı yok), nidâ ('yâ âdemu' 1. kelime), cevap edatı kapsam dışı (morph CAUS 'fe-tekûnâ' 14. kelime), muhatap geçişi 2MS → 2D (ayet içi), şahıs geçişi 3 → 2, edim geçişi emir, şart → emir, yasak, nida; 7:20 söz açılır (12. kelime), söz kapanır (25. kelime, ayet içi), şahıs geçişi yok, şahıs sayısında toplam farkı (2D 6 · 3. şahıs 9 — ölçüm baskın 2), edim geçişi emir, yasak, nida → haber; "
 "7:21 söz biçimli içerik (A4'te söz kaydı yok), şahıs geçişi 2 → 3, edim geçişi yok; "
 "ölçüm iltifât 7:19-21 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:19 've yâ âdemu' — atıflı nida (morph CONJ + VOC); 7:19 'ente ve zevcuke' — gizli özneyi pekiştiren ayrı zamir ve ona bağlanan ad (morph PRON + CONJ); 7:19 'fe-tekûnâ' — yasağın sonucunu bildiren 'fe' (morph CAUS + SUBJ); "
 "7:20 'li-yubdiye' — gerekçe lâmı (morph PRP + SUBJ); 7:20 'mâ vûriye 'anhumâ min sev'âtihimâ' — ilgi cümlesi ve açıklayıcı 'min' (morph REL + PASS); 7:20 'mâ nehâkumâ' ve 'illâ en tekûnâ' — olumsuzluk ve hasr (morph NEG + RES + SUB); 7:21 'innî lekumâ le-mine'n-nâsihîn' — tekitli isim cümlesi (morph ACC + EMPH)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:19 8-16. kelime — 2:35 ile harekesiz eş (sayım: 'say 7:19 8-16'); 7:19 2-5. kelime — 2:35 ile harekesiz eş (sayım: 'say 7:19 2-5'); 7:19 6. kelimenin öneki 2:35'tekinden ayrı (sayım: 'dizi 7 19 1 6'); "
 "7:20 kök كون ikilemesi; 7:19 ile 7:20 arasında 'hâzihi'ş-şecera' yinelenir (7:19 12-13. ve 7:20 16-17. kelime)",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 05'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'skun ente ve zevcuke'l-cennete' 7:19 'sen ve eşin bahçede oturun' / 2:35 'sen ve eşin bahçede oturun' (emsal metninde) — çakışma değil (bayt eşit); "
 "'haysu şi'tumâ ve lâ taqrabâ hâzihi'ş-şecerate fe-tekûnâ mine'z-zâlimîn' 7:19 'dilediğiniz yerden yiyin; ama şu ağaca yaklaşmayın, yoksa zalimlerden olursunuz' / 2:35 'dilediğiniz yerden bol bol yiyin; ama şu ağaca yaklaşmayın, yoksa zalimlerden olursunuz' (emsal metninde) — çakışma — tam okuma sonu (emsalde araya giren 'rağaden' karşılığı 'bol bol'; alıntı 6. ve 7. kelime karşılıklarını da taşıyor); "
 "'ve lâ taqrabâ hâzihi'ş-şecerate' 7:19 'ama şu ağaca yaklaşmayın' / 2:35 'ama şu ağaca yaklaşmayın' (emsal metninde) — çakışma değil (bayt eşit); "
 "'fe-tekûnâ mine'z-zâlimîn' 7:19 'yoksa zalimlerden olursunuz' / 2:35 'yoksa zalimlerden olursunuz' (emsal metninde) — çakışma değil (bayt eşit); "
 "'ve lâ taqrabâ hâzihi'ş-şecerate fe-tekûnâ mine'z-zâlimîn' 7:19 'ama şu ağaca yaklaşmayın, yoksa zalimlerden olursunuz' / 2:35 'ama şu ağaca yaklaşmayın, yoksa zalimlerden olursunuz' (emsal metninde) — çakışma değil (bayt eşit); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:19 'skun' IMPV — meal 'oturun'; 'kulâ' IMPV — meal 'yiyin'; 'şi'tumâ' PERF — meal 'dilediğiniz'; 'taqrabâ' IMPF JUS ('lâ' ile) — meal 'yaklaşmayın'; 'tekûnâ' IMPF SUBJ ('fe' ile) — meal 'olursunuz'; "
 "7:20 'vesvese' PERF — meal 'verdi'; 'yubdiye' IMPF SUBJ ('li' ile) — meal 'açmak'; 'vûriye' PERF PASS — meal 'gizlenen'; 'qâle' PERF — meal 'Dedi'; 'nehâ' PERF ('mâ' ile) — meal 'yasakladı'; 'tekûnâ' IMPF SUBJ (20. kelime; 'en' ile) — meal 'olursunuz'; 'tekûnâ' IMPF SUBJ (23. kelime) — meal 'olursunuz'; "
 "7:21 'qâseme' PERF — meal 'etti'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle): 'şi'tumâ' PERF 7:19'da sıfat-fiil ('-diğiniz') ile; 'tekûnâ' IMPF SUBJ 7:19'da ve 7:20'de geniş zaman ('-ursunuz') ile; 'yubdiye' IMPF SUBJ 7:20'de ad-fiil ('-mak') ile; 'vûriye' PERF 7:20'de sıfat-fiil ('-en') ile; 'nehâ' PERF 7:20'de 'mâ' ve 'illâ' ile olumlu geçmiş ('ancak … yasakladı') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): 'illâ' ('ancak' / 'hariç') — çakışma değil (hasr edatı morph RES, istisna edatı morph EXP); 'fe' (REM: 'Derken' / 'Hemen' / karşılıksız) — çakışma değil (anlatı geçişi, emir önünde ivedilik, Türkçe sıralama); 've' (CONJ: 'ama' / 've' / 'ise' / karşılıksız) — çakışma değil (yasak önünde karşıtlık, atıf, Türkçe sıralama)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 19 21 05'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:20 tarayıcı adayı (kök شجر; B_ta’lîl, D_yeti) çıpa değil — anlatı öğesi, doğa iddiası yok; 7:19 ve 7:21 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:20 ('li-yubdiye' / 'vûriye'); 7:19 ve 7:21 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök شجر 7:19 ('ş-şecerate') ve 7:20 ('ş-şecerati'); kök كون 7:19 ('fe-tekûnâ') ve 7:20 ('tekûnâ', 'tekûnâ'); kök قول 7:20 ('ve qâle'), 7:14 ('qâle') ile bölüm içi; kök أدم 7:19 ('âdemu'), 7:11 ('li-âdeme') ile bölüm içi; kök ملك 7:20 ('melekeyni'), 7:11 ('li'l-melâ'iketi') ile bölüm içi; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 2-3 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 3, 4, 5 ve 6; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b05/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 19 21 05'; lem_bozuk.py 05 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 19 21 → AYN_SONUC; sunum/bolum4_kurallar.py 19 21 05 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 19 21 05 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 37)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 5 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('âdem', 'sekene', 'zevc', 'cenne', 'ekele', 'haysu', 'şâ'e', 'lâ', 'yaqrabu' (morph LEM ham biçim), 'zâ', 'şecera', 'kâne', 'min', 'zâlim'); joker '_' yalnız lemmasız 'ente' öğesinde ('dizi 7 19 2 5', 'dizi 7 19 1 6'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (19, 21): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_7_19_21.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_7_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_7_b02k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '19', '21'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '19', '21', '05'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '19', '21', '05'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '19', '21', '05', '--tazelik-yok')}
    for _n in range(7, 37): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '19', '21', '05')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36 = [_R['B%d' % _n].splitlines() for _n in range(6, 37)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'B31_HEPSI': (B31[-1] if B31 else '?'), 'B32_HEPSI': (B32[-1] if B32 else '?'), 'B33_HEPSI': (B33[-1] if B33 else '?'), 'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36): print([l for l in _x if l.startswith('HATA') or 'hata' in l])

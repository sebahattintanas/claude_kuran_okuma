# sûre 6 bölüm 2 denetimi araç kuralları (bekleyen_ariza_6_b04.txt 2. öğe) — salt okur:
#  (1) ESMA_SIFAT: esma_el 'haberi' kararlı ADJ kelimenin öncesi esmâ dışı belirli, eş durumlu ad ise (na't) hata — öneri ESMA_ADJ'in daraltılmışı: morph ADJ söz türüdür, sözdizim rolü değil
#  (2) BAG_GENIS: emsal kararının bütün kalıpları bir kelimelik ve 50+ ayetlik sayımsa hata
#  (3) BAG_NOT_CELISKI: bag notu 'harekesiz eş yok' iken o ayetin bir 'say' anahtarı emsali listeliyorsa hata
#  (4) NAIB_NUMARA: meal notunda 'N. kelimede … naib-i fail' öğesi morph'ta edilgen fiil taşımalı
#  (5) FIIL_UYUMU_AD: A1'de zamir naib-i failde 'fiil uyumu' yazılmaz ('adsız')
#  (6) CEVAP_NUMARA: A4 şart → cevap kaydında cevap numarası alıntının ◇'deki öncü kelimesi
#  (7) ILTIFAT_KAYIT: ölçüm iltifât > 0 ise ARIZA'da o ayet için 'iltifât' maddesi
#  (8) GONDERGE_BICIM: ayette birden çok lafız varken A1'de numarasız 'gönderge lafız' yazılmaz
#  (9) ESMA_LISTE_FARK: ölçüm esmâ satırında olmayan esma_el kelimesi ARIZA'da 'liste farkı' ile anılır
#  (10) BOS_ALT_MADDE: ': ;', '; ;', '()' yok
#  (elle: BAG_SAYIM_BASIM, KIP_KAPSAM, JOKER_TAM, SAPKA_NORM)
# kullanım (/home/claude'dan): python3 sunum/bolum18_kurallar.py A B NN
import sys as _sy; _sy.path.insert(0, '/home/claude/sunum'); from sure import BK as _BK, S
import re, sys, ast, collections, os, subprocess, importlib.util as iu
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
Y = '/home/claude/yamalar/'
H = []
TUM = ast.literal_eval('{' + open(Y + 'ariza_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read() + '}')[(A, B)]
ITEMS = [m for m in TUM if not re.match(r'(bölüm (denetimi \(|\d+ denetiminden|\d+ \(sûre)|devir \()', m)]
M, MEAL = {}, {}
exec(open(Y + 'metin_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read(), {'M': M, 'MEAL': MEAL})
def morph(p, filt=None):
    W = collections.defaultdict(lambda: collections.defaultdict(list))
    for l in open(p, encoding='utf-8'):
        if filt and not l.startswith(filt): continue
        loc, f, t, feat = l.rstrip('\n').split('\t'); s_, a_, w_, p_ = map(int, loc.split(':'))
        W[(s_, a_)][w_].append((f, t, feat))
    return W
W = morph(_BK + 'b%s/morph%d.txt' % (NN, S))
O = [l.replace('**', '') for l in open(_BK + 'b%s/olcum.txt' % NN, encoding='utf-8').read().split('\n\n') if l.strip()]
EMS = open(_BK + 'b%s/ems.txt' % NN).read().split() if os.path.exists(_BK + 'b%s/ems.txt' % NN) else []
S2 = open(_BK + 'b%s/say2.txt' % NN, encoding='utf-8').read()
S2K = {b.split('\n', 1)[0].strip(): b for b in S2.split('### ')[1:]}
Q = r"'((?:[^']|(?<=[A-Za-zâîûçğışöüÂÎÛ])'(?=[a-zâîûçğışöü]))+)'"
def satir(n, bas):
    for l in M[n].split('\n'):
        if l.startswith(bas): return l
    return ''
def a_parca(n, k):
    l = satir(n, '◈A'); m = re.search(r'\b%s (.*?)(?:; A%d |$)' % (k, int(k[1]) + 1), l)
    return m.group(1) if m else ''
def item(bas): return [m for m in ITEMS if m.startswith(bas)]
EN = collections.Counter()
EMK = ' '.join(m for m in ITEMS if 'emsal meal karşılık farkları' in m)
KAL = re.findall(r"(?:^|; |\): )" + Q + r" %d:\d+ '" % S, EMK)


import unicodedata as _ud
LAFIZ = _ud.normalize('NFC', 'اللَّه')
def tr_(a):
    m = re.match(r"◇ '(.*?)' — ", M[a]); return m.group(1) if m else ''
def kelime(q):  # bolum8_kurallar.py kelime() ile eş (◇ kelime sayımı)
    n = 0
    for t in q.split():
        if t in ('ve', 'fe', 'fa', 'va', 'yâ'): continue
        parca = re.split(r"(?<=[aeiuâîû])'(?=l-|ll|[a-zçğışöü]-|[bcdfğhklmnqrsştxyz]{2})", t)
        n += 1 + sum(1 for x in parca[:-1] if x not in ('ve', 'fe', 'fa', 'va', 'bi', 'li', 'le', 'ke') and not x.endswith('-'))
    return n
def konum(d, q):  # bolum8_kurallar.py konum() ile eş — öncü eşleşme
    K = []
    for mm in re.finditer(re.escape(q), d):
        on = d[:mm.start()]
        if on.endswith('-'): on = on[:on.rfind(' ') + 1]
        K.append(kelime(on.rstrip("'")) + 1 if on.endswith("'") else kelime(on) + 1)
    return K
EEL = {}
for l in open('/home/claude/calisma/esma_el.py', encoding='utf-8'):
    m = re.match(r"\s*'%d:(\d+):(\d+)': '(\w+)',\s*#(.*)" % S, l)
    if m and A <= int(m.group(1)) <= B: EEL[(int(m.group(1)), int(m.group(2)))] = (m.group(3), m.group(4))
def feats(a, w): return [_ud.normalize('NFC', x[2]) for x in W[(S, a)].get(w, [])]
def esma_mi(a, w): return any(k == (a, w) for k in EEL)

# ── (1) ESMA_SIFAT: 'haberi' kararlı esmâ, öncesi esmâ olmayan DET'li ad ve eş durumlu ise (na't) hata ──
for (a, w), (k, yor) in EEL.items():
    if 'haberi' not in yor: continue
    EN['esma_haber'] += 1
    f, fo = ' '.join(feats(a, w)), ' '.join(feats(a, w - 1))
    if 'ADJ' not in f or esma_mi(a, w - 1): continue
    dur = [c for c in ('NOM', 'ACC', 'GEN') if c in f]
    if 'DET' in fo and dur and dur[0] in fo and 'PRON' not in fo:
        H.append("(1) %d:%d %d. kelime esma_el 'haberi' kararı — öncesi (%d. kelime) esmâ dışı belirli ad, eş durum: na't okuması" % (S, a, w, w - 1))

# ── (2) BAG_GENIS: emsal kararının tek dayanağı bir kelimelik ve 50+ ayetlik sayım ise hata ──
EMK_ = {}
for m in re.finditer(r"(?:^|; |\): )" + Q + r" %d:(\d+) '[^;]*?/ (\d+:\d+) '" % S, EMK):
    EMK_.setdefault(m.group(3), []).append((m.group(1), int(m.group(2))))
for e, L in EMK_.items():
    EN['bag_genis'] += 1
    genis = []
    for kal, a in L:
        if len(kal.split()) > 1: break
        n = (konum(tr_(a), kal) or [None])[0] if a in M else None
        b = S2K.get('say %d:%d %d-%d' % (S, a, n or 0, n or 0), '')
        c = re.search(r'ayet: (\d+)', b)
        if not c or int(c.group(1)) < 50: break
        genis.append(kal)
    else:
        if genis: H.append("(2) %s emsal kararı yalnız bir kelimelik geniş sayıma dayanıyor (%s)" % (e, ', '.join(genis)))

# ── (3) BAG_NOT_CELISKI: bag notu 'harekesiz eş yok' iken bir 'say' anahtarı emsali listeliyor ──
bp = Y + 'bag_%d_%d_%d.txt' % (S, A, B)
BAG = ast.literal_eval('[' + open(bp, encoding='utf-8').read() + ']') if os.path.exists(bp) else []
for b in BAG:
    m = re.match(r'(\d+:\d+) → %d:(\d+)' % S, b.get('bag', ''))
    if not m: continue
    e, a = m.group(1), int(m.group(2)); EN['bag_not'] += 1
    if 'harekesiz eş yok' not in (b.get('kural', '') + ' ' + b.get('not', '')): continue
    for k, blk in S2K.items():
        if k.startswith('say %d:%d ' % (S, a)) and re.search(r'(?<![\d:])%s(?!\d)' % re.escape(e), blk.split('liste:', 1)[-1]):
            H.append("(3) bag %s → %d:%d notu 'harekesiz eş yok' — '%s' emsali listeliyor" % (e, S, a, k)); break

# ── (4) NAIB_NUMARA: meal notunda 'naib-i fail' denen 'N. kelimede' öğesi PASS fiil değilse hata ──
vp = _BK + 'b%s/yap/veri.py' % NN
MK = {}
if os.path.exists(vp):
    sp = iu.spec_from_file_location('veri', vp); v = iu.module_from_spec(sp); sp.loader.exec_module(v); MK = v.MK
for a, L in MK.items():
    for tr, q, its in L:
        for it in its:
            m = re.search(r"(\d+)\. kelimede .*naib-i fail", it)
            if not m: continue
            EN['naib_no'] += 1
            w = int(m.group(1))
            if not any('PASS' in f for f in feats(a, w)): H.append("(4) %d:%d %d. kelime meal notunda 'naib-i fail' — morph'ta edilgen fiil yok" % (S, a, w))

# ── (5) FIIL_UYUMU_AD: A1'de zamir naib-i failde 'fiil uyumu' işareti ──
for a in range(A, B + 1):
    for m in re.finditer(r"\((fiil uyumu;[^()]*?naib-i faili (?:konuşan )?zamir)", a_parca(a, 'A1')):
        EN['uyum'] += 1; H.append("(5) %d:%d A1 zamir naib-i failde 'fiil uyumu' — 'adsız' olmalı" % (S, a))

# ── (6) CEVAP_NUMARA: A4 şart → cevap kaydında cevap numarası alıntının öncü kelimesi ──
for a in range(A, B + 1):
    for m in re.finditer(r"şart → cevap \(ayet içi; [^:]*: '(.*?)' / '(.*?)' \((\d+)\. kelime\)\)", a_parca(a, 'A4')):
        EN['cevap'] += 1
        K = konum(tr_(a), m.group(2)); n = K[0] if K else None
        if K and int(m.group(3)) not in K: H.append("(6) %d:%d A4 cevap '%s' numarası %s — öncü kelime %d" % (S, a, m.group(2), m.group(3), n))

# ── (7) ILTIFAT_KAYIT: ölçüm iltifât > 0 ise ARIZA'da o ayet için 'iltifât' maddesi ──
for i, a in enumerate(range(A, B + 1)):
    m = re.search(r'iltifât (\d+)', O[i]) if i < len(O) else None
    if not m or int(m.group(1)) == 0: continue
    EN['iltifat'] += 1
    if not any('iltifât' in it and '%d:%d' % (S, a) in it for it in ITEMS): H.append("(7) %d:%d ölçüm iltifât %s — ARIZA'da iltifât maddesi yok" % (S, a, m.group(1)))

# ── (8) GONDERGE_BICIM: ayette birden çok lafız varken A1'de numarasız 'gönderge lafız' ──
for a in range(A, B + 1):
    n = sum(1 for w in W[(S, a)] if any('LEM:' + LAFIZ in f for f in feats(a, w)))
    if n < 2: continue
    EN['gonderge'] += 1
    if re.search(r"gönderge lafız(?! \d)", a_parca(a, 'A1')): H.append("(8) %d:%d A1 'gönderge lafız' numarasız — ayette lafız %d" % (S, a, n))

# ── (9) ESMA_LISTE_FARK: ölçüm esmâ satırında olmayan esma_el kelimesi ARIZA'da 'liste farkı' ──
for (a, w), (k, yor) in EEL.items():
    i = a - A
    es = set(int(x) for x in re.findall(r'(\d+)\. sırada', re.search(r'esmâ [^·]*', O[i]).group(0))) if i < len(O) and re.search(r'esmâ [^·]*', O[i]) else set()
    EN['esma_liste'] += 1
    if w not in es and not any('liste farkı' in it and '%d:%d' % (S, a) in it for it in ITEMS):
        H.append("(9) %d:%d %d. kelime esma_el kaydı ölçüm esmâ satırında yok — ARIZA'da 'liste farkı' yok" % (S, a, w))

# ── (10) BOS_ALT_MADDE: boş alt madde ya da boş ayraç ──
for it in ITEMS:
    EN['alt_madde'] += 1
    m = re.search(r":\s*;|;\s*;|(?<!meddeli kalıp )\(\s*\)", it)  # medde.py '0 meddeli kalıp ()' araç çıktısı
    if m: H.append("(10) boş alt madde / ayraç '%s': %s" % (m.group(0), it[max(0, m.start() - 40):m.start() + 10]))

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum18_kurallar hata: %d' % len(H))

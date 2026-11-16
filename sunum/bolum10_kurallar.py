# bölüm 10 (sûre 5) denetiminden kurallar — betik denetimi:
#  (1) ARIZA esmâ maddesindeki gerekçe parantezi ⇔ esma_el yorumunun parantezi bayt eşit (ek açıklama parantez dışında)
#  (2) A4: blok planındaki ■ sınırından — bölümü açan ayetin A4'ünde 'bölüm açılışı', bölümü kapatan ayetin A4'ünde 'bölüm kapanışı'
#  (3) meal karşılık farkı kararları kapalı sözlükle ('çakışma değil' / 'tam okuma sonu' / 'bilinçli fark' / 'düzeltildi'); 'karar yok' hata;
#      önceki bloğun kararından yön değişirse 'önceki karar (blok N: …); gerekçe'
#  (5) meal maddesinde karşılık / zamir '-e' / '-den' ile verilmişse ("yönelme eki ile 'X'") 'fiil yönetimi takdiri' aynı öğede
#  (6) xref: ◇ ve ARIZA xref maddesinde 'başka ayet' yok; ölçüm xref'in basılmamış hedefleri sayıyla ('okunmuş N ayet', 'okunmamış M ayet (sûre içi k)')
#  (7) D2'de 'biçim X' yok (biçim etiketi ARIZA edim / kip maddesinde)
#  (8) ayette 'qul' (IMPV, LEM qâle) varsa A3 boş değil ve A4'te 'söz açılır'
#  (9) es_lemma.py --numarasiz ve sonradan.py --numarasiz çıktısı ARIZA'da aynen (tazelik; --tazelik-yok ile atlanır)
#  (10) yasakli.sh IZIN girdileri (dosya deseni, metin) çifti; '*' deseni yalnız eski izinlerde; yeni izin tırnaklı
#  (11) D3 dışı basılmış eş listesi ayet başına ('S:A: …'), boşsa 'yok'
#  (4. kural lem_bozuk.py içinde: harekesiz 'و' ile biten LEM)
# kullanım (/home/claude'dan): python3 sunum/bolum10_kurallar.py A B NN [--tazelik-yok]
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from sure import S
import re, sys, ast, glob, subprocess, fnmatch, importlib.util as iu, unicodedata as ud
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
TAZE = '--tazelik-yok' not in sys.argv
Y = '/home/claude/yamalar/'
H = []
def run(*a): return subprocess.run(list(a), capture_output=True, text=True, cwd='/home/claude').stdout
M = {}; exec(open(Y + 'metin_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read(), {'M': M, 'MEAL': {}})
TUM = ast.literal_eval('{' + open(Y + 'ariza_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read() + '}')[(A, B)]
ITEMS = [m for m in TUM if not re.match(r'bölüm (denetimi \(|\d+ denetiminden)', m)]
def item(bas): return [m for m in ITEMS if m.startswith(bas)]
BAS = {l.strip() for l in open('/home/claude/sunum/basilan.txt') if l.strip()}
SON = int(re.search(r'^SON = (\d+)', open('/home/claude/sunum/sinifla.py').read(), re.M).group(1))
def oku(s, a): return a <= SON if s == S else (s in (1, 2, 3, 4) or s >= 9)
def satir(a, bas):
    for l in M[a].split('\n'):
        if l.startswith(bas): return l
    return ''
def parca(sat, bas, son):
    i = sat.find(bas)
    if i < 0: return None
    j = sat.find(son, i + len(bas)) if son else -1
    return sat[i + len(bas): j if j >= 0 else len(sat)]
def paren(t, i):  # t[i] == '(' → dengeli parantez içi
    d = 0
    for k in range(i, len(t)):
        d += t[k] == '('; d -= t[k] == ')'
        if d == 0: return t[i + 1:k]
    return t[i + 1:]
# ── (1) esmâ gerekçe parantezi ──
ef = Y + 'esma_el_%d_%d_%d.txt' % (S, A, B)
if _o.path.exists(ef):
    es = ' '.join(item('esmâ'))
    for l in open(ef, encoding='utf-8'):
        m = re.search(r'#\s*(.+?) — (.+) → (\w+) \((.+)\)\s*$', l)
        if not m: continue
        kural, par = m.group(2), m.group(4)
        bas = "kural '%s' (" % kural
        if bas not in es: H.append("(1) esmâ maddesinde kural yok: %s" % bas[:70]); continue
        for mm in re.finditer(re.escape(bas), es):
            p = paren(es, mm.end() - 1)
            if p != par: H.append("(1) esmâ parantezi '%s' / esma_el '%s'" % (p[:70], par[:70]))
# ── (2) A4 bölüm açılışı / kapanışı ──
bol = []
for l in open(Y + 'blok_plani_%d.txt' % S, encoding='utf-8'):
    if l.startswith('■'): bol.append([])
    else:
        m = re.match(r'\s*(\d+)\. (\d+):(\d+)-?(\d+)?', l)
        if m: bol[-1].append((int(m.group(1)), int(m.group(3)), int(m.group(4) or m.group(3))))
for b in bol:
    nos = [x[0] for x in b]
    if int(NN) not in nos: continue
    if int(NN) == nos[0] and 'bölüm açılışı' not in (parca(satir(A, '◈A'), 'A4 ', '') or ''): H.append('(2) %d:%d A4 bölüm açılışı yok' % (S, A))
    if int(NN) == nos[-1] and 'bölüm kapanışı' not in (parca(satir(B, '◈A'), 'A4 ', '') or ''): H.append('(2) %d:%d A4 bölüm kapanışı yok' % (S, B))
# ── (3) meal karşılık farkı kararları ──
def kat(seg):
    k = seg.split(' — ', 1)[1] if ' — ' in seg else ''
    if 'karar yok' in k: return 'yok'
    if k.startswith('çakışma değil'): return 'değil'
    if k.startswith('bilinçli fark'): return 'bilinçli'
    if 'tam okuma sonu' in k: return 'tam'
    if k.startswith('düzeltildi'): return 'düzeltildi'
    return '?'
def kararlar(metin):
    mk = metin.split('): ', 1)[-1]
    return [s for s in re.split(r"; (?=')", mk) if s.strip()]
def formlar(seg): return set(re.findall(r"'((?:[^']|'(?=[a-zâîûçğışöü]))+)'", seg.split(' — ', 1)[0]))
ONCE = []
for f in glob.glob(Y + 'ariza_%d_*_*.txt' % S):
    a_, b_ = map(int, re.findall(r'_(\d+)_(\d+)\.txt$', f)[0])
    if b_ < A:
        for m in ast.literal_eval('{' + open(f, encoding='utf-8').read() + '}').popitem()[1]:
            if m.startswith('meal karşılık farkı kararları'): ONCE.append((a_, kararlar(m)))
ONCE.sort()
BLOKNO = {}
for b in bol:
    for no, x, y in b: BLOKNO[x] = no
for m in item('meal karşılık farkı kararları'):
    for seg in kararlar(m):
        k = kat(seg)
        if k == 'yok': H.append('(3) meal karşılık farkı kararı yok: %s' % seg[:70]); continue
        if k == '?': H.append('(3) meal karşılık farkı kararı kapalı sözlük dışı: %s' % seg[:90]); continue
        fo = formlar(seg); onc = None
        for a_, segs in ONCE:
            for s2 in segs:
                if fo & formlar(s2) and kat(s2) not in ('yok', '?'): onc = (a_, kat(s2))
        if onc and onc[1] != k and not (re.search(r'önceki karar \(blok \d+', seg) and 'gerekçe' in seg):
            H.append('(3) meal kararı yön değiştirdi (blok %s: %s → %s), önceki karar yazılmamış: %s' % (BLOKNO.get(onc[0], '?'), onc[1], k, seg[:60]))
# ── (5) fiil yönetimi takdiri ──
vp = '/home/claude/b%s/yap/veri.py' % NN
if _o.path.exists(vp):
    sp = iu.spec_from_file_location('veri', vp); v = iu.module_from_spec(sp); sp.loader.exec_module(v)
    for a, L in v.MK.items():
        for tr, q, its in L:
            for it in its:
                if re.search(r"(?:yönelme|ayrılma) eki ile '", it) and 'fiil yönetimi takdiri' not in it:
                    H.append("(5) %d:%d fiil yönetimi takdiri yok: %s" % (S, a, it[:70]))
# ── (6) xref ──
olc = open('/home/claude/b%s/olcum.txt' % NN, encoding='utf-8').read().split('\n\n')
xi = ' '.join(item('ölçüm xref'))
if 'başka ayet' in xi: H.append("(6) ARIZA xref maddesinde 'başka ayet'")
for a in range(A, B + 1):
    o = olc[a - A]
    hed = set()
    for l in re.findall(r'xref ([^|\n]*)', o):  # blok 26: bir xref alanında ' · ' ile ayrılmış birden çok kalıp (her '→' grubu)
        for g in l.split(' · '): hed |= set(re.findall(r'\d+:\d+', g.split('→', 1)[1])) if '→' in g else set()
    if 'başka ayet' in M[a]: H.append("(6) %d:%d ◇'de 'başka ayet'" % (S, a))
    bm = [h for h in hed if h not in BAS]
    ok = len([h for h in bm if oku(*map(int, h.split(':')))]); hz = len(bm) - ok
    hsi = len([h for h in bm if not oku(*map(int, h.split(':'))) and int(h.split(':')[0]) == S])
    if ok and ('okunmuş %d ayet' % ok) not in M[a]: H.append("(6) %d:%d xref 'okunmuş %d ayet' yazılmamış" % (S, a, ok))
    if hz and ('okunmamış %d ayet (sûre içi %d)' % (hz, hsi)) not in M[a]: H.append("(6) %d:%d xref 'okunmamış %d ayet (sûre içi %d)' yazılmamış" % (S, a, hz, hsi))
# ── (7) D2 biçim etiketi ──
for a in range(A, B + 1):
    d2 = parca(satir(a, '◈D'), 'D2 ', '; D3') or ''
    if re.search(r'biçim [A-Z]', d2): H.append('(7) %d:%d D2 biçim etiketi: %s' % (S, a, re.search(r'biçim [A-Z]+', d2).group(0)))
# ── (8) 'qul' sözü ──
QUL = set()
for l in open('/home/claude/b%s/morph%d.txt' % (NN, S), encoding='utf-8'):
    loc, f, t, feat = l.rstrip('\n').split('\t')
    s_, a_ = map(int, loc.split(':')[:2])
    if 'IMPV' in feat and ud.normalize('NFC', 'LEM:قالَ') in ud.normalize('NFC', feat): QUL.add(a_)
for a in sorted(QUL):
    sat = satir(a, '◈A'); a3 = (parca(sat, 'A3 ', '; A4') or '').strip(' ;')
    if a3 in ('', '—'): H.append("(8) %d:%d 'qul' sözü var, A3 boş" % (S, a))
    if 'söz açılır' not in (parca(sat, 'A4 ', '') or ''): H.append("(8) %d:%d 'qul' sözü var, A4'te 'söz açılır' yok" % (S, a))
# ── (9) numarasız araç çıktıları ──
if TAZE:
    tum = ' '.join(ITEMS)
    T = [l for l in run('python3', 'sunum/es_lemma.py', *[str(i) for i in range(1, int(NN) + 1)], '--numarasiz').splitlines() if l.strip()]
    T += [l for l in run('python3', 'sunum/sonradan.py', '--plan', NN, '--numarasiz').splitlines() if l.strip()]
    for l in T:
        if l not in tum: H.append('(9) numarasız araç çıktısı ARIZA\'da yok: %s' % l[:80])
# ── (10) yasakli.sh IZIN ──
ys = open('/home/claude/sunum/yasakli.sh', encoding='utf-8').read()
mz = re.search(r'^IZIN = (\(.*?\))  #', ys, re.M)
ESKI = {"'biri' (5:27:12)", "'birer' dağıtma", "\\'birer\\' dağıtma", 'üçü de', 'kalıp: ikisi süzgeç', 'kalıp: üçü süzgeç', 'kalıp: dördü süzgeç', 'xref üçü de boş', "'bozguncu'"}
try:
    IZ = ast.literal_eval(mz.group(1)) if mz else ()
except Exception: IZ = (); H.append('(10) IZIN okunamadı')
for z in IZ:
    if not (isinstance(z, tuple) and len(z) == 2): H.append('(10) IZIN girdisi (desen, metin) çifti değil: %r' % (z,)); continue
    if z[0] == '*' and z[1] not in ESKI: H.append("(10) yeni IZIN girdisi '*' desenli: %s" % z[1])
    if z[1] not in ESKI and "'" not in z[1]: H.append('(10) IZIN girdisi tırnaksız: %s' % z[1])
# ── (11) D3 dışı listesi ayet başına ──
d3 = ' '.join(item('◈D D3 / bag'))
if 'D3 dışı bırakılan basılmış sayım eşleri' in d3:
    son = d3.split('D3 dışı bırakılan basılmış sayım eşleri', 1)[1].split(' — kalıp başına')[0]
    son = son.split('): ', 1)[-1]
    for a in range(A, B + 1):
        if not re.search(r'%d:%d: (?:yok|\d)' % (S, a), son): H.append('(11) D3 dışı listesinde %d:%d ayet başlığı yok (boşsa yok)' % (S, a))
for h in H: print('HATA', h)
print('bolum10_kurallar hata:', len(H))

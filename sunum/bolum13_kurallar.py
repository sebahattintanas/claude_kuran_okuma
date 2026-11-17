# bölüm 13 (sûre 5) denetimi araç kuralları (bekleyen_ariza_5_b30.txt 2. öğe) — salt okur:
#  (1) xref hedef kümesi tam eşleşme: ◇ 'Ölçüm xref' cümlesi ve ARIZA xref maddesinde basılmış her hedef numarasıyla; numarasız sayılar ('okunmuş N', 'okunmamış M') sinifla sınıfıyla birebir; fazla numara / sayı hata
#  (2) ARIZA esma_kayit maddesi esma_muhur.py'nin şimdiki çıktısıyla bayt eşit (hat sonunda esma_kayit'ten sonra; denetim_5.sh de koşar)
#  (3) bolum4 'söz içi REM: N.' çıktısı → söz / tırnak maddesinde "REM sapması S:A (N. kelime) — gerekçe"
#  (4) A3 aralığı ayetin son kelimesinde bitiyorsa A4'te 'söz kapanır (N. kelime, ayet içi)'
#  (5) A3 aralığındaki 1. / 2. şahıs zamirli kelimeler A1'de 'söz içi' etiketli kayıtta
#  (6) 'tutmuyor' R5 satırı r5_gerekce çıktısını aynen taşır; gerekçede anılan "'X' dizisi sûre içi K (blok N R5 satırı)" o bloğun R5 satırındaki lemma dizisi sayısıyla eş
#  (7) sözdizimi / okuma (gözlem) / aktör / ad maddelerindeki transliterasyon alıntıları ('…' parçaları) ◇ alt dizesi
#  (8) meal maddesinde "'X' 'Y' karşılığı / açılımı (N. kelime" — N. kelime morph isim ise Y ◇ lafız dizisinde tırnaklı ad (LEM notu yetmez)
#  (9) ARIZA araç değişikliği maddesi: listelenen her araç gerekçede adıyla ve 'kural N' ile; denetim aracı mutasyon_sina.py'de sınanıyor (geriye_donuk, sinifla, basilan, mutasyon_sina hariç)
#  (10) emsal meal alıntısı emsal meal metninin bayt eşit parçası; kalıp 've' / 'fe' önekliyse emsalde hemen önceki bağlaç sözcüğü ('Öyleyse', 'Artık', 've' …) düşürülemez
#  (11) mealde 'olan' / 'olanı' geçen kesimde 'olan' takdiri ya da 'ol-' karşılığı kayıtlı
#  (12) A2, okuma (gözlem) ve çıpa maddelerinde meal ve ◇'de bulunmayan plan başlığı sözcüğü hata
#  (bölüm 13 kuralları 13-15 elle)
# kullanım (/home/claude'dan): python3 sunum/bolum13_kurallar.py A B NN
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from sure import S
import re, sys, ast, glob, json, subprocess, collections, importlib.util as iu
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
Y = '/home/claude/yamalar/'
H = []
def run(*a): return subprocess.run(['python3'] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout
TUM = ast.literal_eval('{' + open(Y + 'ariza_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read() + '}')[(A, B)]
ITEMS = [m for m in TUM if not re.match(r'bölüm (denetimi \(|\d+ denetiminden)', m)]
def item(bas): return [m for m in ITEMS if m.startswith(bas)]
M, MEAL = {}, {}
exec(open(Y + 'metin_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read(), {'M': M, 'MEAL': MEAL})
DIA = {n: re.match(r"◇ '(.*?)' — ", M[n]).group(1) for n in range(A, B + 1)}
SEQ = {n: M[n][M[n].index(' — ') + 3:M[n].index(' (ölçüm edim')] for n in range(A, B + 1)}
OLC = [l.replace('**', '') for l in open('/home/claude/b%s/olcum.txt' % NN, encoding='utf-8').read().split('\n\n') if l.strip()]
BAS = set(open('/home/claude/sunum/basilan.txt', encoding='utf-8').read().split())
SON = int(re.search(r'^SON = (\d+)', open('/home/claude/sunum/sinifla.py', encoding='utf-8').read(), re.M).group(1))
def oku(s, a): return a <= SON if s == S else (s in (1, 2, 3, 4) or s >= 9)
W = collections.defaultdict(lambda: collections.defaultdict(list))
for l in open('/home/claude/b%s/morph%d.txt' % (NN, S), encoding='utf-8'):
    loc, f, t, feat = l.rstrip('\n').split('\t'); s_, a_, w_, p_ = map(int, loc.split(':'))
    W[a_][w_].append((f, t, feat))
sp = iu.spec_from_file_location('veri', '/home/claude/b%s/yap/veri.py' % NN); veri = iu.module_from_spec(sp); sp.loader.exec_module(veri)
Q = r"'((?:[^']|'(?=[a-zâîûçğışöü]))+)'"
def bol(s, sep='; '):
    out, d, cur, i = [], 0, '', 0
    while i < len(s):
        c = s[i]; d += c == '('; d -= c == ')'
        if d == 0 and s.startswith(sep, i): out.append(cur); cur = ''; i += len(sep); continue
        cur += c; i += 1
    out.append(cur); return out
def satir(n, bas):
    for l in M[n].split('\n'):
        if l.startswith(bas): return l
    return ''
def a_parca(n, k):  # ◈A satırında Ak parçası
    l = satir(n, '◈A'); m = re.search(r'\b%s (.*?)(?:; A%d |$)' % (k, int(k[1]) + 1), l)
    return m.group(1) if m else ''

# ── (1) xref tam eşleşme ──
xi = ' '.join(item('ölçüm xref'))
for n in range(A, B + 1):
    hed = set()
    xs = OLC[n - A].split('xref ', 1)[1].split(' | ')[0] if 'xref ' in OLC[n - A] else ''
    for g in re.findall(r'→ ([\d:, ]+)', xs): hed |= set(re.findall(r'\d+:\d+', g))
    bas = {h for h in hed if h in BAS}
    rest = [h for h in hed if h not in BAS]
    ok_ = sum(1 for h in rest if oku(*map(int, h.split(':'))))
    hz = len(rest) - ok_
    cum = re.search(r'Ölçüm xref ([^.]*?)\.(?= |$)', M[n].split('\n')[0])
    seg = next((g for g in bol(xi.split('): ', 1)[-1]) if g.startswith('%d:%d ' % (S, n))), '')
    for yer, t in (('◇', cum.group(1) if cum else ''), ('ARIZA', seg[len('%d:%d ' % (S, n)):])):
        if not hed:
            if 'yok' not in t: H.append('(1) %d:%d %s xref: ölçümde xref yok, metin %r' % (S, n, yer, t[:60]))
            continue
        nums = set(re.findall(r'\b\d+:\d+\b', t))
        if nums != bas: H.append('(1) %d:%d %s xref numaraları %s (+ basılmamış %d) ≠ basılmış hedefler %s' % (S, n, yer, sorted(nums & BAS), len(nums - BAS), sorted(bas)))  # basılmamış numara yazılmaz
        m1 = re.search(r'okunmuş (\d+) ayet', t); m2 = re.search(r'okunmamış (\d+) ayet', t)
        if (int(m1.group(1)) if m1 else 0) != ok_: H.append('(1) %d:%d %s xref okunmuş sayısı %s ≠ %d' % (S, n, yer, m1.group(1) if m1 else 0, ok_))
        if (int(m2.group(1)) if m2 else 0) != hz: H.append('(1) %d:%d %s xref okunmamış sayısı %s ≠ %d' % (S, n, yer, m2.group(1) if m2 else 0, hz))

# ── (2) esma_kayit maddesi şimdiki çıktıyla ──
emh = run('sunum/esma_muhur.py', str(A), str(B), NN).strip()
ek = item('esma_kayit')
if ek and not ek[0].endswith('): ' + emh): H.append('(2) esma_kayit maddesi esma_muhur şimdiki çıktısıyla eş değil (ARIZA esma_el / esma_kayit öncesi üretilmiş olabilir)')

# ── (3) söz içi REM sapması ──
b4 = run('sunum/bolum4_kurallar.py', str(A), str(B), NN)
st = ' '.join(item('söz / tırnak'))
for a_, r_ in re.findall(r'^REM \d+:(\d+) söz içi REM: (.*)$', b4, re.M):
    for k in re.findall(r'(\d+)\.', r_):
        if not re.search(r'REM sapması %d:%s \(%s\. kelime\) — \S' % (S, a_, k), st): H.append('(3) %d:%s %s. kelime söz içi REM — söz / tırnak maddesinde gerekçeli REM sapması yok' % (S, a_, k))

# ── (4) söz kapanır ──
for n in range(A, B + 1):
    a3 = a_parca(n, 'A3')
    m = re.search(r'(\d+)-(\d+)\. kelime', a3)
    if a3.strip() in ('', '—') or not m: continue
    if int(m.group(2)) == max(W[n]) and 'söz kapanır (%s. kelime, ayet içi)' % m.group(2) not in a_parca(n, 'A4'):
        H.append("(4) %d:%d A3 ayet sonunda bitiyor — A4'te 'söz kapanır (%s. kelime, ayet içi)' yok" % (S, n, m.group(2)))

# ── (5) A3 içi 1. / 2. şahıs → A1 'söz içi' ──
for n in range(A, B + 1):
    m = re.search(r'(\d+)-(\d+)\. kelime', a_parca(n, 'A3'))
    if not m: continue
    a1 = bol(a_parca(n, 'A1'))
    for k in range(int(m.group(1)), int(m.group(2)) + 1):
        if any(re.search(r'\|[12](?:M|F)?[SDP](?:\||$)', ft) for f, t, ft in W[n][k]):
            if not any('söz içi' in g and re.search(r'\b%d\.' % k, g) for g in a1): H.append("(5) %d:%d %d. kelime A3 içinde 1. / 2. şahıs — A1'de 'söz içi' kaydında yok" % (S, n, k))

# ── (6) R5 gerekçesi ──
src = open('/home/claude/b%s/yap/kur.py' % NN, encoding='utf-8').read() if _o.path.exists('/home/claude/b%s/yap/kur.py' % NN) else ''
r5i = ' '.join(item('araç tanımı farkları (R5'))
DOS = sorted(glob.glob(Y + 'ariza_%d_*.txt' % S), key=lambda p: int(p.split('_')[-2]))
for m in re.finditer(r'\("(\d+:\d+)", "(.*?)", \d+, \'[^\']+\', ".*?", \(\'(dizi \d+ \d+ \d+ \d+)\'', src):
    ay, ad, dk = m.group(1), m.group(2), m.group(3)
    i0 = r5i.find('%s nakarat3 %s' % (ay, ad))
    if i0 < 0: continue
    i1 = r5i.find(' nakarat3 ', i0 + 10); row = r5i[i0:i1 if i1 > 0 else len(r5i)]
    if 'tutmuyor' not in row: continue
    rg = run('sunum/r5_gerekce.py', *dk.split()[1:]).strip()
    if rg and rg not in row: H.append('(6) R5 %s %s: r5_gerekce çıktısı satırda aynen yok (%s)' % (ay, ad, rg[:60]))
    for kel, k, bn in re.findall(r"'(\S+)' dizisi sûre içi (\d+) \(blok (\d+) R5 satırı\)", row):
        ad2 = kel + ' ' + ad.strip("'").split(' ', 1)[1]
        if int(bn) - 1 >= len(DOS): continue
        t = open(DOS[int(bn) - 1], encoding='utf-8').read()
        mm = re.search(r"lemma dizisi '%s' \([^)]*\) sûre içi (\d+)" % re.escape(ad2), t)
        if mm and mm.group(1) != k: H.append("(6) R5 %s %s: gerekçe '%s' dizisi sûre içi %s, blok %s R5 satırında %s" % (ay, ad, kel, k, bn, mm.group(1)))

# ── (7) sözdizimi / okuma / aktör alıntıları ◇'de ──
ALLTR = ' | '.join(DIA.values())
def trlike(x): return bool(re.search(r"[xqâîû]|'[a-z]|[a-z]'|^[a-z]+-[a-z]", x)) and not re.search(r'[çğıöşü]', x.replace('ş', '').replace('ğ', ''))
for bas in ('sözdizimi', 'okuma (gözlem)', 'aktör / ad'):
    for it in item(bas):
        govde = it.split('): ', 1)[-1]
        for x in re.findall(Q, govde):
            if not trlike(x) or "lemma dizisi '%s'" % x in govde or "dizisi '%s'" % x in govde: continue
            for p in [y.strip() for y in x.split('…')]:
                if p and p not in ALLTR: H.append("(7) %s maddesi alıntısı ◇ alt dizesi değil: '%s'" % (bas, p[:50]))

# ── (8) meal karşılık adı ◇ lafız dizisinde ──
for n in sorted(veri.MK):
    if not A <= n <= B: continue
    for tr, q, its in veri.MK[n]:
        for it in its:
            m = re.match(r"'[^']+(?:'[^']*)*?' " + Q + r" (?:karşılığı|açılımı) \((\d+)\. kelime", it)
            if not m: continue
            y, k = m.group(1), int(m.group(2))
            gov = [(f, t, ft) for f, t, ft in W[n][k] if 'PREF' not in ft and 'SUFF' not in ft]
            if not gov or gov[0][1] != 'N' or re.search(r'\b(PRON|REL|DEM|PN)\b', gov[0][2]): continue
            if "'%s'" % y not in SEQ[n]: H.append("(8) %d:%d %d. kelime meal adı '%s' ◇ lafız dizisinde yok" % (S, n, k, y))

# ── (9) araç değişikliği gerekçesi ──
ai = item('araç değişikliği')
if ai:
    t = ai[0]
    m = re.search(r'(?:\d+ dosya — |değişen araçlar \(repo HEAD ile fark\): )([^;]*)', t)
    MUT = open('/home/claude/sunum/mutasyon_sina.py', encoding='utf-8').read()
    for f in (m.group(1).split(', ') if m else []):
        f = f.replace(' (yeni)', '').strip(); bn = f.split('/')[-1]
        if bn in ('geriye_donuk.py', 'sinifla.py', 'basilan.txt', 'mutasyon_sina.py', 'arac_degisim.py'): continue
        g = t.split('gerekçe', 1)[-1]
        i = g.find(f)
        if i < 0 or not re.search(r'kural(?:lar)?ı? \d+', g[i:(g.find(';', i) if g.find(';', i) > 0 else len(g))]): H.append('(9) araç %s gerekçede adıyla ve kural numarasıyla yok' % f)
        if bn.endswith('.py') and "'%s'" % bn not in MUT: H.append('(9) araç %s mutasyon_sina.py sınamasında yok' % f)

# ── (10) emsal meal alıntısı ──
EMS = {}
ep = '/home/claude/b%s/emsal.txt' % NN
if _o.path.exists(ep):
    for blk in open(ep, encoding='utf-8').read().split('**')[1:]:
        pass
    for m in re.finditer(r'\*\*(\d+:\d+)\*\*\n\n## [^\n]*\n\n([^\n]*)', open(ep, encoding='utf-8').read()): EMS[m.group(1)] = m.group(2)
OM = None
mi = ' '.join(item('meal (okuma'))
if 'emsal meal karşılık farkları' in mi:
    em = mi.split('emsal meal karşılık farkları', 1)[1].split('): ', 1)[-1]
    for g in bol(em):
        m = re.match(Q + r" \d+:\d+ " + Q + r" / (\d+:\d+) " + Q + r" \(emsal metninde\)", g)
        if not m: continue
        kal, e, tr2 = m.group(1), m.group(3), m.group(4)
        if e not in EMS:
            if OM is None: OM = json.load(open('/home/claude/repo/notlar/okuma_metni.json', encoding='utf-8'))
            EMS[e] = OM.get(e.split(':')[0], {}).get(e, {}).get('meal', '')
        mt = EMS[e]
        if tr2 not in mt: H.append("(10) emsal %s alıntısı emsal metninde bayt eşit değil: '%s'" % (e, tr2[:50])); continue
        on = mt[:mt.index(tr2)].rstrip()
        if re.match(r"(ve|fe)[-' ]", kal) and on and on[-1].isalpha():
            son = on.split()[-1].lower()
            if son in ('öyleyse', 'artık', 've', 'sonra', 'şimdi', 'de', 'da', 'ki'): H.append("(10) emsal %s alıntısı önek karşılığı '%s' düşürülmüş" % (e, on.split()[-1]))

# ── (11) 'olan' takdiri ──
for n in sorted(veri.MK):
    if not A <= n <= B: continue
    for tr, q, its in veri.MK[n]:
        if re.search(r'\bolan', tr) and not any(re.search(r"'olan' takdiri|'(?:[^']* )?ol-' (?:karşılığı|açılımı)|'[^']* olan' (?:karşılığı|açılımı)", it) for it in its): H.append("(11) %d:%d meal kesiminde 'olan' — 'olan' takdiri / 'ol-' karşılığı yok: '%s'" % (S, n, tr[:50]))

# ── (12) plan başlığı sözcükleri ──
plan = open(Y + 'blok_plani_%d.txt' % S, encoding='utf-8').read().splitlines()
bas_ = None
for l in plan:
    if l.startswith('■'): bas_ = l[1:].strip()
    if re.match(r'\s*%d\. ' % int(NN), l): break
if bas_:
    tum_meal = (' '.join(MEAL.get(n, '') for n in range(A, B + 1)) + ' ' + ALLTR).lower()
    kel = [w.lower() for w in re.split(r'[;, ]+', bas_) if len(w) >= 4 and w.lower() not in ('olan',)]
    metinler = [('A2 %d:%d' % (S, n), a_parca(n, 'A2')) for n in range(A, B + 1)] + [(b, ' '.join(item(b)).split('): ', 1)[-1]) for b in ('okuma (gözlem)', 'çıpa')]
    for w in kel:
        kok = w[:5] if len(w) >= 6 else w[:4]
        if kok[:4] in tum_meal: continue
        for yer, t in metinler:
            if re.search(r'\b' + re.escape(kok), t.lower()): H.append("(12) %s plan başlığı sözcüğü '%s' — meal ve ◇'de yok" % (yer, w))

for h in H: print('HATA', h)
print('bolum13_kurallar hata: %d' % len(H))

# sûre 6 bölüm 1 denetimi araç kuralları (bekleyen_ariza_6_b02.txt 2. öğe) — salt okur:
#  (1) EMSAL_KALIP_KAPSAM: ◇'de basılmış emsali listeleyen her sayım satırının kelimeleri ARIZA emsal karar kalıplarıyla (sayım adının alt dizesi olan) örtülür
#  (2) ONCEKI_BASIM_MEAL: bag kaynağı bu bloktan önce basılmış (sûre içi değil) her ayet ARIZA emsal karar maddesinde '/ X ' ile anılır
#  (3) EMSAL_ORTAK_DIZI: ayet ile emsal arasındaki en uzun ortak ardışık lemma dizisi (≥3) say2'de bir 'say S:a i-j' anahtarıyla sayılmış
#  (4) TEKIL_ON: 'korpusta 1' öneksiz sayımlarının '--on' eşi say2'de ve 1
#  (5) FAIL_ZAID_MIN: olumsuz / soru fiilinden sonra 'min' + nekre GEN, fiille cinsiyetçe uyumlu ad → A1'de 'N. kelime — fail M. kelime'
#  (6) NAIB_ADSIZ: A1'de 'adsız' ile 'naib-i faili N. kelime' aynı parantezde yazılmaz
#  (7) SART_CEVAP_TUM: 'lev' (COND) sonrası her EMPH 'le' önekli kelime A4 şart → cevap kaydında '(N. kelime)'
#  (9) BASKIN_BERABERLIK: ölçüm şahıs sayılarında en yüksek iki değer eşitse A4'te 'beraberlik'
#  (10) SEG_ORTUSME: meal kesimlerinin kelime numarası kümeleri ayrık
#  (11) BOS_MADDE: ARIZA maddesi ': ' ile bitmez
#  (12) JOKER_ADI: joker listesinde önek edat adı ('bi', 'li', 'ke', 've', 'fe') yok
#  (13) BOS_ALAN: ARIZA'da 'kelime  (' boş alan yok
#  (14) MUHUR_KAYNAK: ◇ "esma_kayit çıktısı 'mühür …'" alıntısı esma_kayit.py çıktısının o ayet satırında
#  (8 elle)
# kullanım (/home/claude'dan): python3 sunum/bolum17_kurallar.py A B NN
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

# ── (1) EMSAL_KALIP_KAPSAM ──
for a in range(A, B + 1):
    d = M[a].split('\n')[0]
    for m in re.finditer(r"(?:[Hh]arekesiz|[Öö]nek kesilmiş) " + Q + r" (\d+) ayet: ([^;.]*)", d):
        lab, lst = m.group(1), m.group(3)
        es = [e for e in EMS if re.search(r'(?<![\d:])%s(?!\d)' % re.escape(e), lst)]
        if not es: continue
        EN['kapsam'] += 1
        ort = [k for k in KAL if k in lab]
        kal = [w for w in lab.split() if not any(w in k.split() for k in ort)]
        if kal: H.append("(1) %d:%d sayım '%s' emsal %s — karar kalıbı örtmüyor: %s" % (S, a, lab[:60], ', '.join(es), ' '.join(kal)))

# ── (2) ONCEKI_BASIM_MEAL ──
bp = Y + 'bag_%d_%d_%d.txt' % (S, A, B)
if os.path.exists(bp):
    for b_ in ast.literal_eval('[' + open(bp, encoding='utf-8').read() + ']'):
        x = b_['bag'].split(' → ')[0]
        if x.startswith('%d:' % S): continue
        EN['bag'] += 1
        if not re.search(r"/ %s '" % re.escape(x), EMK): H.append("(2) bag kaynağı %s ARIZA emsal meal karar maddesinde yok" % x)

# ── (3) EMSAL_ORTAK_DIZI ──
if EMS:
    WK = morph('/home/claude/calisma/morph.txt')
    def lem(seq): return [next((re.search(r'LEM:([^|]+)', ft).group(1) for f, t, ft in seq if 'PREF' not in ft and 'SUFF' not in ft and 'LEM:' in ft), None) for _ in [0]][0]
    for a in range(A, B + 1):
        L1 = [(w, lem(W[(S, a)][w])) for w in sorted(W[(S, a)])]
        for e in EMS:
            es_, ea = map(int, e.split(':'))
            L2 = [lem(WK[(es_, ea)][w]) for w in sorted(WK[(es_, ea)])]
            best = (0, 0)
            for i in range(len(L1)):
                for j in range(len(L2)):
                    k = 0
                    while i + k < len(L1) and j + k < len(L2) and L1[i + k][1] and L1[i + k][1] == L2[j + k]: k += 1
                    if k > best[0]: best = (k, i)
            if best[0] < 3: continue
            EN['ortak'] += 1
            i0, i1 = L1[best[1]][0], L1[best[1] + best[0] - 1][0]
            ok = any(re.match(r'say %d:%d (\d+)-(\d+)' % (S, a), k) and int(re.match(r'say %d:%d (\d+)-(\d+)' % (S, a), k).group(1)) <= i0 and int(re.match(r'say %d:%d (\d+)-(\d+)' % (S, a), k).group(2)) >= i1 and e in S2K[k] for k in S2K)
            if not ok: H.append("(3) %d:%d / %s ortak lemma dizisi %d-%d. kelime say2'de emsali bulan sayımla yok" % (S, a, e, i0, i1))

# ── (4) TEKIL_ON ──
for it in item('korpusta 1'):
    for k in re.findall(r'say %d:\d+ \d+-\d+(?: --on)?' % S, it):
        if k.endswith('--on'): continue
        EN['tekil'] += 1
        b_ = S2K.get(k + ' --on')
        if b_ is None: H.append("(4) '%s' korpusta 1 — '--on' eşi say2'de yok" % k)
        elif not re.search(r"^1 \{", b_.split('\n')[-2] if b_.strip().split('\n')[-1].startswith('liste') else b_.strip().split('\n')[-1]): H.append("(4) '%s' korpusta 1 — '--on' eşi 1 değil" % k)

# ── (5) FAIL_ZAID_MIN ──
for a in range(A, B + 1):
    a1 = a_parca(a, 'A1')
    for w in sorted(W[(S, a)]):
        vs = [ft for f, t, ft in W[(S, a)][w] if t == 'V']
        if not vs or 'PASS' in vs[0]: continue
        g = re.search(r'\|3([MF])S\b', vs[0])
        if not g: continue
        once = ' '.join(ft for k in range(max(1, w - 2), w + 1) for f, t, ft in W[(S, a)][k])
        if not re.search(r'NEG|INTG', once): continue
        for k in range(w + 1, min(w + 3, max(W[(S, a)]) + 1)):
            seg = W[(S, a)][k]
            if any('LEM:مِن' in ft for f, t, ft in seg) and k + 1 in W[(S, a)]:
                n2 = [ft for f, t, ft in W[(S, a)][k + 1] if t == 'N' and 'INDEF' in ft and 'GEN' in ft]
                if n2 and re.search(r'\|%s[SPD]?\b' % g.group(1), n2[0]):
                    EN['zaid'] += 1
                    if not re.search(r'(?<![\d-])%d\. kelime — fail %d\. kelime' % (w, k + 1), a1):
                        H.append("(5) %d:%d %d. kelime fiil, fail 'min' ile nekre %d. kelime — A1'de 'fail' yok" % (S, a, w, k + 1))
                break

# ── (6) NAIB_ADSIZ ──
for a in range(A, B + 1):
    for m in re.finditer(r"\(([^()]*)\)", a_parca(a, 'A1')):
        if 'adsız' in m.group(1) and re.search(r'naib-i faili \d+\. kelime', m.group(1)):
            EN['naib'] += 1; H.append("(6) %d:%d A1 'adsız' + açık naib-i fail: (%s)" % (S, a, m.group(1)[:60]))

# ── (7) SART_CEVAP_TUM ──
for a in range(A, B + 1):
    lev = [w for w in sorted(W[(S, a)]) if any('COND' in ft and 'لَو' in ft for f, t, ft in W[(S, a)][w])]
    if not lev: continue
    a4 = a_parca(a, 'A4')
    for w in sorted(W[(S, a)]):
        if w > lev[0] and any('EMPH' in ft and 'PREF' in ft for f, t, ft in W[(S, a)][w]):
            EN['cevap'] += 1
            if not re.search(r'şart → cevap.*?\(%d\. kelime\)' % w, a4):
                H.append("(7) %d:%d 'lev' sonrası EMPH %d. kelime A4 şart → cevap kaydında yok" % (S, a, w))

# ── (9) BASKIN_BERABERLIK ──
for i, a in enumerate(range(A, B + 1)):
    if i >= len(O): break
    m = re.search(r'şahıs ((?:\d[A-Z]+ \d+(?: · )?)+)', O[i])
    if not m: continue
    say_ = collections.Counter()
    for p, n in re.findall(r'(\d)[A-Z]+ (\d+)', m.group(1)): say_[p] += int(n)
    v = sorted(say_.values(), reverse=True)
    if len(v) > 1 and v[0] == v[1]:
        EN['berabere'] += 1
        if 'beraberlik' not in a_parca(a, 'A4'): H.append("(9) %d:%d şahıs sayıları berabere (%s) — A4'te 'beraberlik' yok" % (S, a, m.group(1)))

# ── (10) SEG_ORTUSME ──
vp = _BK + 'b%s/yap/veri.py' % NN
if os.path.exists(vp):
    sp = iu.spec_from_file_location('veri', vp); v = iu.module_from_spec(sp); sp.loader.exec_module(v)
    for a, L in v.MK.items():
        gor = {}
        for tr, q, its in L:
            ks = set(int(x) for it in its for x in re.findall(r'(?<![\d:])(\d+)\. kelime', it))
            for k in ks:
                if k in gor and gor[k] != tr: H.append("(10) %d:%d %d. kelime meal kesimlerinde örtüşüyor: '%s' / '%s'" % (S, a, k, gor[k], tr))
                gor[k] = tr
        EN['seg'] += 1

# ── (11) BOS_MADDE ──
for it in ITEMS:
    EN['madde'] += 1
    if re.search(r':\s*$', it): H.append("(11) boş ARIZA maddesi: %s" % it[:70])

# ── (12) JOKER_ADI ──
for it in ITEMS:
    for m in re.finditer(r"joker '_' \(([^)]*)\)", it):
        for x in re.findall(Q, m.group(1)):
            EN['joker'] += 1
            if x in ('bi', 'li', 'ke', 've', 'fe'): H.append("(12) joker listesinde önek edat adı '%s'" % x)

# ── (13) BOS_ALAN ──
for it in TUM:
    if 'kelime  (' in it: H.append("(13) boş alan 'kelime  (': %s" % it[it.index('kelime  (') - 30:][:60])

# ── (14) MUHUR_KAYNAK ──
ek = subprocess.run(['python3', 'esma_kayit.py', str(S), str(A), str(B)], capture_output=True, text=True, cwd='/home/claude/calisma').stdout
for a in range(A, B + 1):
    m = re.search(r"esma_kayit çıktısı '([^']+)'", M[a].split('\n')[0])
    if not m: continue
    EN['muhur'] += 1
    sat = [l for l in ek.splitlines() if re.match(r'%d:%d\s' % (S, a), l)]
    if not sat or m.group(1) not in sat[0]: H.append("(14) %d:%d ◇ esma_kayit alıntısı '%s' esma_kayit.py çıktısında yok" % (S, a, m.group(1)))

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum17_kurallar hata: %d' % len(H))

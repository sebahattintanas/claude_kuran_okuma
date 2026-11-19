# bölüm 8 (sûre 5) denetiminden kurallar — betik denetimi:
#  (1) R5 'tutmuyor' / 'açıklanmadı' / 'okunduğunda yazılır' satırı 'öneksiz eş koşusu' (sunum/r5_on.py) sonucunu taşır; koşu nakarat sayısını verirse satır kapanır ('tutuyor')
#  (3) esma_kayit maddesi sunum/esma_muhur.py çıktısını aynen taşır (muhur / muhur_el / ölçüm)
#  (4) meal maddesindeki Arapça biçim ة yapıntısında ◇ çözümlemesindeki adla eşleşir ('salât' / 'salâ')
#  (5) lemma dizisi / nakarat3 kalıp adlarının her öğesi bağ maddesindeki lemma adı listesinde; lemma adı önceki ARIZA'ların eş iskeletli adıyla eşit
#  (6) es_lemma satırları (bloğa dokunan) ve ◈D 'ayetler arası kalıp' alıntıları 'meal karşılık farkı kararları' maddesinde kapalı kararla anılır
#  (14) A1 alt maddesinde alıntı + kelime numarası birlikteyse alıntının ◇'deki kelime konumu numarayla eşit
#  (15) es_edat 'ayrıştırılamayan' 0
# kullanım (/home/claude'dan): python3 sunum/bolum8_kurallar.py A B NN
import sys as _sy; _sy.path.insert(0, '/home/claude/sunum'); from sure import BK as _BK
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from sure import S
import re, sys, ast, glob, subprocess, importlib.util, unicodedata as ud
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
Y = '/home/claude/yamalar/'
H = []
M = {}; MEAL = {}; exec(open(Y + 'metin_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read(), {'M': M, 'MEAL': MEAL})
AR = ast.literal_eval('{' + open(Y + 'ariza_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read() + '}')
ITEMS = [m for v in AR.values() for m in v if not re.match(r'bölüm (denetimi \(|\d+ denetiminden)', m)]
def item(bas): return [m for m in ITEMS if m.startswith(bas)]
def run(*a): return subprocess.run(list(a), capture_output=True, text=True, cwd='/home/claude').stdout
sp = importlib.util.spec_from_file_location('veri', _BK + 'b%s/yap/veri.py' % NN); veri = importlib.util.module_from_spec(sp); sp.loader.exec_module(veri)
MOR = {}
for l in open(_BK + 'b%s/morph%d.txt' % (NN, S), encoding='utf-8'):
    loc, fo, t, ft = l.rstrip('\n').split('\t'); s_, a_, w_, p_ = map(int, loc.split(':'))
    MOR.setdefault((a_, w_), []).append((fo, t, ft))
Q = r"'((?:[^']|'(?=[a-zâîûçğışöü']))+)'"
mpa = {'ب':'b','ت':'t','ث':'s','ج':'c','ح':'h','خ':'x','د':'d','ذ':'z','ر':'r','ز':'z','س':'s','ش':'ş','ص':'s','ض':'d','ط':'t','ظ':'z','غ':'ğ','ف':'f','ق':'q','ك':'k','ل':'l','م':'m','ن':'n','ه':'h','و':'v','ي':'y','ى':'y'}
def skl(t):
    t = t.lower().replace('û', 'v').replace('î', 'y')
    return re.sub(r'(.)\1+', r'\1', ''.join(c for c in t if c in 'bcdfğhklmnqrsştxzvy'))
# ── (1) R5 öneksiz eş koşusu ──
r5 = ' '.join(item('araç tanımı farkları (R5'))
for sat in re.split(r'; (?=%d:\d+ nakarat3)' % S, r5):
    m = re.match(r"%d:(\d+) nakarat3 '(.+?)' (\d+) \(tür ic\)" % S, sat)
    if not m: continue
    acik = sat.count('tutmuyor') >= 2 or 'açıklanmadı' in sat or 'okunduğunda yazılır' in sat
    if not acik: continue
    if 'öneksiz eş koşusu' not in sat: H.append('(1) R5 %d:%s %s: kapanmamış satırda öneksiz eş koşusu yok' % (S, m.group(1), m.group(2)))
    dk = re.search(r"lemma dizisi \('dizi (\d+) (\d+) (\d+) (\d+)'\)|'dizi (\d+) (\d+) (\d+) (\d+)'", sat)
    if dk:
        g = [x for x in dk.groups() if x]
        o = run('python3', '/home/claude/sunum/r5_on.py', *g[:4])
        if any(int(x) == int(m.group(3)) for x in re.findall(r'sûre içi (\d+)', o)) and not sat.rstrip().endswith('tutuyor'):
            H.append('(1) R5 %d:%s %s: öneksiz eş koşusu nakarat sayısını (%s) veriyor, satır kapanmamış' % (S, m.group(1), m.group(2), m.group(3)))
# ── (3) esma_kayit maddesi ⇔ esma_muhur.py ──
em = run('python3', '/home/claude/sunum/esma_muhur.py', str(A), str(B), NN).strip()
ek = ' '.join(item('esma_kayit'))
if em and em not in ek: H.append('(3) esma_kayit maddesi esma_muhur.py çıktısını aynen taşımıyor')
# ── (4) ة yapıntısı: meal biçimi ⇔ ◇ adı ──
for a in range(A, B + 1):
    d0 = M[a].split(' — ', 1)[1].split(' (ölçüm')[0]
    adlar = set(re.findall(r"(?:nekre|belirli|çoğul|ortaç|masdar|bab|özel ad) '((?:[^']|'(?=[a-zâîûçğışöü]))+)'", d0))
    for tr, q, its in veri.MK.get(a, []):
        for it in its:
            mm = re.match(r"'[^']+' " + Q + r" (?:karşılığı|açılımı) \(((?:\d+(?:-\d+)?\.,? (?:ve )?)+)kelime", it)
            if not mm: continue
            f = mm.group(1)
            for x in re.findall(r'(\d+)(?:-(\d+))?\.', mm.group(2)):
                for w in range(int(x[0]), int(x[1] or x[0]) + 1):
                    lem = next((re.search(r'LEM:([^|]+)', ft).group(1) for fo, t, ft in MOR.get((a, w), []) if 'LEM:' in ft and t == 'N'), '')
                    if not lem.rstrip('\u064b\u064c\u064d\u064e\u064f\u0650\u0651\u0652').endswith('ة'): continue
                    if f.endswith('t') and f[:-1] in adlar and f not in adlar: H.append("(4) %d:%d %d. kelime meal biçimi '%s' / ◇ adı '%s' (ة yapıntısı)" % (S, a, w, f, f[:-1]))
                    if not f.endswith('t') and f + 't' in adlar and f not in adlar: H.append("(4) %d:%d %d. kelime meal biçimi '%s' / ◇ adı '%s' (ة yapıntısı)" % (S, a, w, f, f + 't'))
# ── (5) lemma dizisi / kalıp adı öğeleri ⇔ lemma adı listesi; ad tutarlılığı ──
def liste(it):
    m = re.search(r"lemma adları[^(]*\(((?:[^()]|\([^()]*\))*)\)", it)
    return [p.replace(' (morph LEM ham biçim)', '')[1:-1] for p in re.split(r"(?<=['\)]), (?=')", m.group(1))] if m else []
LL = set(x for it in item('bağ:') for x in liste(it))
adlar = []
for it in item('araç tanımı farkları (R5'):  # bölüm 9 kuralı 14: yalnız R5 satır başındaki kalıp adı ve 'eşit aralıkla lemma dizisi' adı; düzyazıdan ad yakalanmaz
    for sat in re.split(r'; (?=%d:\d+ nakarat3 )' % S, it.split('): ', 1)[-1]):
        m = re.match(r"%d:\d+ nakarat3 '(.+?)' \d+ \(tür ic\)" % S, sat)
        if m: adlar.append(m.group(1))
        adlar += re.findall(r"eşit aralıkla lemma dizisi '(.+?)' \(\d", sat)
nk = ' '.join(item('nakarat3 (R3'))
if '): ' in nk: adlar += re.findall(r"(?:: |, | ve |; |\d )'(.+?)'(?=, '| ve '| süzgeç| GEÇ|;|$)", nk.split('): ', 1)[1])
for a in range(A, B + 1): adlar += re.findall(r"lemma dizisi '(.+?)'(?= \d+ ayet| korpusta| \()", M[a])
for ad in sorted(set(adlar)):
    for o in ad.split():
        if o != '_' and o not in LL: H.append("(5) kalıp adı '%s' öğesi '%s' lemma adı listesinde yok" % (ad, o))
def norm(x):  # yazım eşdeğeri: uzunluk işareti, 'iyy' / 'î', çift harf, baştaki e / a; ayn (') korunur
    t = x.lower().replace('â', 'a').replace('î', 'i').replace('û', 'u').replace('iyy', 'i').replace('uvv', 'u')
    t = re.sub(r'(.)\1+', r'\1', t)
    return ('a' + t[1:]) if t[:1] == 'e' else t
ONCE = {}
AYRI = {'ilâ': {'illâ'}, 'illâ': {'ilâ'}, 'etâ': {'âtâ'}, 'âtâ': {'etâ'}, 'qâdir': {'qadîr'}, 'qadîr': {'qâdir'}}
for f in sorted(glob.glob(Y + 'ariza_%d_*_*.txt' % S), key=lambda p: int(p.split('_')[-2])):
    if int(f.split('_')[-2]) >= A: continue
    for it in [m for v in ast.literal_eval('{' + open(f, encoding='utf-8').read() + '}').values() for m in v if m.startswith('bağ:')]:
        for x in liste(it): ONCE.setdefault(norm(x), set()).add(x)
for x in sorted(LL):
    es = ONCE.get(norm(x), set()) - AYRI.get(x, set())  # sûre 6 blok 9: yazım eşdeğeri iskeletinde ayrı lemmalar ('ilâ' إِلَى / 'illâ' إِلّا)
    if es and x not in es: H.append("(5) lemma adı '%s' — önceki bloklarda eş iskeletli ad %s" % (x, ', '.join(sorted(es))))
# ── (6) meal karşılık farkı kararları ──
kr = ' '.join(item('meal karşılık farkı kararları'))
el = run('python3', '/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, int(NN) + 1)])
gerek = []
for sat in re.split(r'; |\n', el):
    if ' (morph LEM eşit): ' not in sat: continue
    if any(re.search(r'\b%d:%d:\d+' % (S, a), sat) for a in range(A, B + 1)): gerek.append(sat.split(' (morph LEM eşit): ')[0])
d3 = ' '.join(item('◈D D3 / bag'))
gerek += ["'%s'" % q for q in re.findall(r"ayetler arası kalıp " + Q + r" \(", d3)]
for g in gerek:
    seg = kr[kr.find(g):kr.find(g) + len(g) + 400] if g in kr else ''
    if not seg: H.append('(6) meal karşılık farkı kararı yok: %s' % g[:80]); continue
    if not re.search(r'— (?:karar: )?(?:çakışma değil|tam okuma sonu|bilinçli fark|düzeltildi)', seg): H.append('(6) meal karşılık farkı kapalı karar yok: %s' % g[:80])
# ── (14) A1 alıntı ⇔ kelime numarası ──
def kelime(q):
    n = 0
    for t in q.split():
        if t in ('ve', 'fe', 'fa', 'va', 'yâ'): continue
        parca = re.split(r"(?<=[aeiuâîû])'(?=l-|ll|[a-zçğışöü]-|[bcdfğhklmnqrsştxyz]{2})", t)
        n += 1 + sum(1 for x in parca[:-1] if x not in ('ve', 'fe', 'fa', 'va', 'bi', 'li', 'le', 'ke') and not x.endswith('-'))
    return n
EN = 0
for a in range(A, B + 1):
    t = M[a]; d = re.match(r"◇ '(.*?)' — ", t).group(1)
    a1 = t[t.index('A1 ') + 3:t.index(' A2 ')]
    dd, cur, its = 0, '', []
    for ch in a1:
        dd += (ch == '(') - (ch == ')')
        if ch == ';' and dd == 0: its.append(cur); cur = ''
        else: cur += ch
    its.append(cur)
    def konum(q):
        K = set()
        for mm in re.finditer(re.escape(q), d):
            on = d[:mm.start()]
            if on.endswith('-'): on = on[:on.rfind(' ') + 1]
            K.add(kelime(on.rstrip("'")) + 1 if on.endswith("'") else kelime(on) + 1)
        return K
    for it in its:
        ciftler = re.findall(Q + r" (\d+)\.", it)
        if not ciftler:
            qs = re.findall(Q, it); ns = re.findall(r'(?<![\d:])(\d+)\. kelime', it)
            if len(qs) == 1 and len(ns) == 1 and not re.search(r'\d+-\d+\.', it): ciftler = [(qs[0], ns[0])]
        for q, n in ciftler:
            K = konum(q)
            if not K: continue
            EN += 1
            if int(n) not in K: H.append("(14) A1 %d:%d alıntı '%s' %s. kelime / ◇ konumu %s" % (S, a, q, n, ','.join(map(str, sorted(K)))))
print('A1 alıntı / numara çifti: %d' % EN)
# ── (15) es_edat ayrıştırılamayan ──
ee = run('python3', '/home/claude/sunum/es_edat.py', NN)
m = re.search(r'ayrıştırılamayan edat / zamir maddesi (\d+)', ee)
if not m or int(m.group(1)): H.append('(15) es_edat ayrıştırılamayan %s' % (m.group(1) if m else '?'))
for h in H: print('HATA', h)
print('bolum8_kurallar hata:', len(H))

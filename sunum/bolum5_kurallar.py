# bölüm 5 (sûre 5) denetimi kuralları 5 (ham LEM), 7 (tetik dışı tarama), 8 (ayetler arası kalıp alıntısı ayet bazında),
# 9 (meal takdirleri: '-dir' ve nekre), 10 (aday 1039 ◇ ⇔ ARIZA çiftleri) — betik denetimi
# kullanım (/home/claude'dan): python3 sunum/bolum5_kurallar.py A B NN
#   girdiler: yamalar/metin_<S>_A_B.txt, yamalar/ariza_<S>_A_B.txt, bNN/morph<S>.txt, bNN/morph.txt, sunum/ham_elle.txt
#   biçimler (yazım sözleşmesi):
#     ham LEM: lemma adı listelerinde ve 'LEM 'x'' kayıtlarında ham ad ardından ' (morph LEM ham biçim)'
#     tetik dışı: ◈ tetik maddesinde aday kökün Arapça harfleri 'S:a' bölümünde geçer
#     ayetler arası kalıp: "ayetler arası kalıp 'Q' (S:a, S:b …" — Q her ayetin ◇ transliterasyonunda alt dize
#     '-dir' takdiri: "'-dir' takdiri ('kelime'" (ek biçimi kelimedeki ekle); nekre: "(n. kelime; nekre"
#     aday 1039: ARIZA "S:a ('X' / 'Y'; …)" ⇔ ◇ "Karşıt çift (aday 1039, okuma): ayet içi: 'X' / 'Y'; …"
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from sure import S
import re, sys, ast, glob, unicodedata as ud
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
Y = '/home/claude/yamalar/'
H = []
M, MEALD = {}, {}
g = {'M': M, 'MEAL': {}}
exec(open(Y + 'metin_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read(), g)
for k, v in g.items():
    if k.startswith('MEAL') and isinstance(v, dict): MEALD.update(v)
AR = ast.literal_eval('{' + open(Y + 'ariza_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read() + '}')
ITEMS = [m for v in AR.values() for m in v if not m.startswith(('bölüm denetimi (', 'bölüm 5 denetiminden', 'bölüm 4 denetiminden', 'bölüm 3 denetiminden'))]  # önceki denetimin kopyası taranmaz
def item(bas):
    return [m for m in ITEMS if m.startswith(bas)]
mp = {'ب':'b','ت':'t','ث':'s','ج':'c','ح':'h','خ':'x','د':'d','ذ':'z','ر':'r','ز':'z','س':'s','ش':'ş','ص':'s','ض':'d','ط':'t','ظ':'z','غ':'ğ','ف':'f','ق':'q','ك':'k','ل':'l','م':'m','ن':'n','ه':'h','و':'v','ي':'y','ى':'y'}
def isk_ar(w):
    w = ''.join(c for c in ud.normalize('NFD', w) if not ud.combining(c))
    return ''.join(mp.get(c, '') for c in w)
def isk_la(t):
    t = t.lower().replace('û', 'v').replace('î', 'y')
    return re.sub(r'(.)\1+', r'\1', ''.join(c for c in t if c in 'bcdfğhklmnqrsştxzvy'))
def nb(x): return re.sub(r'(.)\1+', r'\1', x)
# ── (5) ham LEM ──
def bozuk(L, feat):
    L = ud.normalize('NFC', L); son = L.rstrip('\u0651')[-1]
    return son in ('\u0652', '\u064f') or (L.startswith('يَ') and L != ud.normalize('NFC', 'يَئِسَ')) or ('PASS' in feat and '\u064f' in L[:4])
ELLE = set()
try:
    for l in open('/home/claude/sunum/ham_elle.txt', encoding='utf-8'):
        l = l.split('#')[0].strip()
        if l: ELLE.add(ud.normalize('NFC', l))
except FileNotFoundError: pass
LEMS = {}  # iskelet → (LEM, ham mı)
for f in sorted(glob.glob('/home/claude/b*/morph%d.txt' % S)):
    for l in open(f, encoding='utf-8'):
        loc, fo, t, feat = l.rstrip('\n').split('\t')
        m = re.search(r'LEM:([^|]+)', feat)
        if not m or t not in ('N', 'V'): continue
        L = ud.normalize('NFC', m.group(1))
        ham = (t == 'V' and bozuk(L, feat)) or L in ELLE
        LEMS.setdefault(nb(isk_ar(L)), {})[L] = ham
HAM_IS = {k for k, d in LEMS.items() if all(d.values())}  # iskelet eşi lemmaların hepsi ham ise
adlar = []  # (bağlam, ad, ardından gelen)
for it in ITEMS:
    for m in re.finditer(r"lemma adları[^(]*\(((?:[^()]|\([^()]*\))*)\)", it):
        for q in re.finditer(r"'((?:[^']|'(?=[a-zâîûçğışöü]))+)'( \(morph LEM ham biçim\))?", m.group(1)):
            adlar.append(('lemma listesi', q.group(1), bool(q.group(2))))
    for q in re.finditer(r"LEM '((?:[^']|'(?=[a-zâîûçğışöü]))+)'( \(morph LEM ham biçim\))?", it):
        adlar.append(('LEM kaydı', q.group(1), bool(q.group(2))))
    for q in re.finditer(r"(?:bir lemma \(|farklı lemma — )'((?:[^']|'(?=[a-zâîûçğışöü]))+)'( \(morph LEM ham biçim\))?", it):
        adlar.append(('çakışma', q.group(1), bool(q.group(2))))
LDISI, NOTSUZ = [], []
def zayif(k): return nb(k.replace('v', '').replace('y', ''))
LEMS2 = {}
for k in LEMS: LEMS2.setdefault(zayif(k), set()).add(k)
for bag, ad, notlu in adlar:
    k = isk_la(ad)
    aday = [x for x in (k, k.rstrip('h'), k + 'h', k.rstrip('n')) if x in LEMS]
    if not aday:
        aday = sorted(set().union(*[LEMS2.get(zayif(x), set()) for x in (k, k.rstrip('n'), k.rstrip('h'))]))
    if not aday:
        LDISI.append('%s %s' % (bag, ad)); continue
    if all(x in HAM_IS for x in aday) and not notlu: NOTSUZ.append('%s %s' % (bag, ad))
# meal maddesinde ham LEM'li her kelime için not (sayı eşlemesi, ayet ayet)
HAMW = {}
for l in open('/home/claude/b%s/morph%d.txt' % (NN, S), encoding='utf-8'):
    loc, fo, t, feat = l.rstrip('\n').split('\t'); s_, a_, w_, p_ = map(int, loc.split(':'))
    m = re.search(r'LEM:([^|]+)', feat)
    if m and t in ('N', 'V'):
        L = ud.normalize('NFC', m.group(1))
        if (t == 'V' and bozuk(L, feat)) or L in ELLE: HAMW.setdefault(a_, set()).add(w_)
print('ham LEM: ad %d, morph LEM dışı %d%s, ham notsuz %d%s' % (len(adlar), len(LDISI), (' (' + '; '.join(LDISI[:8]) + ')') if LDISI else '',
      len(NOTSUZ), (' (' + '; '.join(NOTSUZ[:8]) + ')') if NOTSUZ else ''))
H += ['ham notsuz ' + x for x in NOTSUZ] + ['LEM dışı ad ' + x for x in LDISI]
# ── (7) tetik dışı tarama ──
TETIK = set('سمو أرض شمس قمر نجم كوكب ليل نهر فلك سحب روح موه بحر جبل يوم أجل سنو عمر سوع دهر أبد حين أنس دبب نعم طير نبت شجر خلق نطف علق زوج حمل وضع أنث عنق ذقن يدي عين سمع بصر جلد قلب حيي موت'.split())
ADAY = set('صبح مسو بكر عشي ضحو سحر غدو أصل وقت زمن شهر سبت جمع قتل نفس دمو هلك صلب قطع رجل رأس وجه سوأ جسد بدن أنف أذن سنن جرح لحم عظم بطن صدر ظهر كعب رفق جنب شعر كفف غرب'.split())
MOR = {}
for l in open('/home/claude/b%s/morph.txt' % NN, encoding='utf-8'):
    k, w, f = l.rstrip('\n').split('\t'); _, a, n = k.split(':'); MOR[(int(a), int(n))] = f
tet = re.sub(r'tetik dışı aday \d+:.*?anılmayan \d+(?: \([^)]*\))?', '', ' '.join(item('◈ tetik') + item('tetik dışı')))  # aracın kendi çıktısı anılış sayılmaz
def bolum(a):  # tetik maddelerinin S:a ile başlayan bütün bölümleri (bir sonraki 'S:b ' işaretine dek)
    par = re.split(r'(?<![\d:])(%d:\d+) ' % S, tet)
    return ' '.join(par[k + 1] for k in range(1, len(par) - 1, 2) if par[k] == '%d:%d' % (S, a))
TD, TDY = [], []
for (a, n), f in sorted(MOR.items()):
    if not A <= a <= B: continue
    r = re.search(r'ROOT:([^|]+)', f); r = r.group(1) if r else None
    T = bool(re.search(r'(?:^|\| |\+ )N\|T(?:\||$)', f))
    if (r in ADAY and r not in TETIK) or (T and r not in TETIK):
        etiket = (r or '') + (' (morph T)' if T else '')
        TD.append('%d:%d %d. kelime %s' % (S, a, n, etiket))
        if not ((r and r in bolum(a)) or re.search(r'(?<!\d)%d\. kelime' % n, bolum(a))): TDY.append('%d:%d %d. kelime %s' % (S, a, n, etiket))
print('tetik dışı aday %d: %s; ◈ tetik maddesinde anılmayan %d%s' % (len(TD), ', '.join(TD) or 'yok', len(TDY), (' (' + ', '.join(TDY) + ')') if TDY else ''))
H += ['tetik dışı anılmadı ' + x for x in TDY]
# ── (8) ayetler arası kalıp alıntısı ──
def dmd(a):  # ◇ transliterasyonu, herhangi bir okunmuş blok dosyasından
    for f in glob.glob(Y + 'metin_%d_*_*.txt' % S):
        x, y = map(int, re.findall(r'_(\d+)_(\d+)\.txt$', f)[0])
        if x <= a <= y:
            mm = {}; exec(open(f, encoding='utf-8').read(), {'M': mm, 'MEAL': {}})
            r = re.match(r"◇ '(.*?)' — ", mm[a]); return r.group(1) if r else ''
    return None
KAL = 0
for txt in ITEMS + list(M.values()):
    for m in re.finditer(r"ayetler arası kalıp '((?:[^']|'(?=[a-zâîûçğışöü]))+)' \(((?:%d:\d+(?:, | ve )?)+)" % S, txt):
        q = m.group(1).replace('…', '').strip()
        for a in map(int, re.findall(r'%d:(\d+)' % S, m.group(2))):
            d = dmd(a); KAL += 1
            if d is not None and not all(p.strip() in d for p in m.group(1).split('…') if p.strip()):
                H.append("ayetler arası kalıp '%s' %d:%d ◇ alt dizesi değil" % (q, S, a))
print('ayetler arası kalıp alıntısı: ayet eşlemesi %d' % KAL)
# ── (9) meal takdirleri ──
meal = ' '.join(item('meal (okuma'))
def mbol(a):
    i = meal.find('%d:%d ' % (S, a))
    if i < 0: return ''
    j = min([x for x in (meal.find('%d:%d ' % (S, b), i + 1) for b in range(a + 1, B + 1)) if x > 0] or [len(meal)])
    return meal[i:j]
DIR, NEK = [], []
for a in range(A, B + 1):
    mb = mbol(a)
    for tok in re.findall(r"[A-Za-zçğıöşüâîûÇĞİÖŞÜ']+", MEALD.get(a, '')):
        mm = re.search(r'(dir|dır|dur|dür|tir|tır|tur|tür)(?:lar|ler)?$', tok)
        if mm and len(tok) > 4 and tok.lower() not in ('kadir', 'tedbir', 'bedir', 'tır'):
            if "'-%s' takdiri ('%s'" % (mm.group(1), tok) not in mb: DIR.append('%d:%d %s' % (S, a, tok))
    for (aa, n), f in sorted(MOR.items()):
        if aa == a and re.search(r'(?:^|\|)INDEF(?:\||$)', f) and not re.search(r'\(%d\. kelime; nekre' % n, mb):
            NEK.append('%d:%d %d. kelime' % (S, a, n))
for a in range(A, B + 1):
    n_h, n_n = len(HAMW.get(a, ())), mbol(a).count('(morph LEM ham biçim)')
    if n_n < n_h: H.append('ham LEM %d:%d ham kelime %d (%s) / meal notu %d' % (S, a, n_h, ', '.join('%d.' % w for w in sorted(HAMW[a])), n_n))
print("meal takdiri: '-dir' kayıtsız %d%s; nekre (morph INDEF) kayıtsız %d%s" % (len(DIR), (' (' + ', '.join(DIR) + ')') if DIR else '', len(NEK), (' (' + ', '.join(NEK) + ')') if NEK else ''))
H += ["'-dir' kayıtsız " + x for x in DIR] + ['nekre kayıtsız ' + x for x in NEK]
# ── (10) aday 1039 ◇ ⇔ ARIZA ──
ad = ' '.join(item('aday 1039'))
for a in range(A, B + 1):
    m = re.search(r"%d:%d \(((?:[^()]|\([^()]*\))*)\)" % (S, a), ad.split('ayetler arası')[0])
    ar_c = [x.strip() for x in m.group(1).split('; ')] if m else []
    d = re.search(r"Karşıt çift \(aday 1039, okuma\): ayet içi: (.*?)(?: — ayetler arası|\. [A-ZÇĞİÖŞÜ◈]|\.$)", M[a])
    dm_c = [x.strip() for x in d.group(1).split('; ')] if d and d.group(1) != 'yok' else []
    if ar_c != dm_c: H.append('aday 1039 %d:%d ARIZA %s ≠ ◇ %s' % (S, a, ar_c, dm_c))
print('aday 1039 eşlemesi: %d ayet' % (B - A + 1))
for h in H: print('HATA', h)
print('bolum5_kurallar hata:', len(H))

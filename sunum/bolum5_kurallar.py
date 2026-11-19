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
import sys as _sy; _sy.path.insert(0, '/home/claude/sunum'); from sure import BK as _BK
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
BLP = set()  # bu bloğun edat (P) LEM iskeletleri — edat adı, zayıf harf eşlemesiyle fiil / isim LEM'ine bağlanmaz
BL = {}  # bölüm 8 kuralı 9: bu bloğun kendi morph LEM'leri (iskelet → ham mı) — ham kararı önce buradan
for f in sorted(glob.glob(_BK + 'b[0-9][0-9]/morph%d.txt' % S)):
    if int(f.split('/')[-2][1:]) > int(NN): continue  # bölüm 8 kuralı 9: yalnız okunmuş bloklar (blok ≤ NN)
    for l in open(f, encoding='utf-8'):
        loc, fo, t, feat = l.rstrip('\n').split('\t')
        m = re.search(r'LEM:([^|]+)', feat)
        if m and t == 'P' and f.split('/')[-2] == 'b%s' % NN: BLP.add(nb(isk_ar(ud.normalize('NFC', m.group(1)))))
        if not m or t not in ('N', 'V'): continue
        L = ud.normalize('NFC', m.group(1))
        ham = (t == 'V' and bozuk(L, feat)) or L in ELLE
        LEMS.setdefault(nb(isk_ar(L)), {})[L] = ham
        if f.split('/')[-2] == 'b%s' % NN: BL.setdefault(nb(isk_ar(L)), set()).add(ham)
HAM_IS = {k for k, d in LEMS.items() if all(d.values())}  # iskelet eşi lemmaların hepsi ham ise
adlar = []  # (bağlam, ad, ardından gelen)
KOKLU = []  # bölüm 6 kuralı 3: kökü ve ayeti anılan çakışma adları (ad, kök, ayetler, notlu)
for it in ITEMS:
    for m in re.finditer(r"lemma adları[^(]*\(((?:[^()]|\([^()]*\))*)\)", it):
        for parca in re.split(r"(?<=['\)]), (?=')", m.group(1)):  # bölüm 6 kuralı 3: virgülle böl (hemze ile biten addan sonra bozulmaz)
            notlu = parca.endswith(' (morph LEM ham biçim)')
            q = parca[:-len(' (morph LEM ham biçim)')] if notlu else parca
            if q.startswith("'") and q.endswith("'") and len(q) > 2: adlar.append(('lemma listesi', q[1:-1], notlu))
    for q in re.finditer(r"LEM '((?:[^']|'(?=[a-zâîûçğışöü]))+)'( \(morph LEM ham biçim\))?", it):
        adlar.append(('LEM kaydı', q.group(1), bool(q.group(2))))
    for q in re.finditer(r"(?:bir lemma \(|farklı lemma — |farklı lemma ve kök — )'((?:[^']|'(?=[a-zâîûçğışöü]))+)'( \(morph LEM ham biçim\))?|\('((?:[^']|'(?=[a-zâîûçğışöü]))+)'( \(morph LEM ham biçim\))?(?=;)", it):
        if it.startswith('karşılık çakışması'): adlar.append(('çakışma', q.group(1) or q.group(3), bool(q.group(2) or q.group(4))))
    if it.startswith('karşılık çakışması'):  # bölüm 7 kuralı 11: parantez içi "('X')" / "('X'," adları da; ham ad notsuzsa isabet (düz yazı not sayılmaz)
        for q in re.finditer(r"\('((?:[^']|'(?=[a-zâîûçğışöü]))+)'( \(morph LEM ham biçim\))?(?=[,)])", it):
            adlar.append(('çakışma parantez', q.group(1), bool(q.group(2))))
        for q in re.finditer(r"(?<=[\s(—/])'((?:[^']|'(?=[a-zâîûçğışöü]))+)'( \(morph LEM ham biçim\))? \(([؀-ۿ]+)((?:; (?:%d:\d+)(?:, %d:\d+)*)?)\)" % (S, S), it):
            KOKLU.append((q.group(1), q.group(3), [int(x) for x in re.findall(r'%d:(\d+)' % S, q.group(4))], bool(q.group(2))))
LDISI, NOTSUZ = [], []
def zayif(k): return nb(k.replace('v', '').replace('y', ''))
LEMS2 = {}
for k in LEMS: LEMS2.setdefault(zayif(k), set()).add(k)
for bag, ad, notlu in adlar:
    k = isk_la(re.sub(r"^(?:fe|ve|bi|li|ke)-", '', ad) if bag == 'lemma listesi' else ad)  # blok 34 / bölüm 15 denetimi kuralı 10: önekli kalıp öğesi (bölüm 7 kuralı 12 önek kümesi) yalnız lemma adı listesinde önek dışında LEM'e bağlanır; LEM kaydı ve çakışma adlarında önekli ad hata
    aday = [x for x in (k, k.rstrip('h'), k + 'h', k.rstrip('n'), k.rstrip('t')) + ((k + 't',) if ad.endswith(('e', 'â')) else ()) if x in LEMS]  # ة: 't' ile ya da 't'siz yazım; bölüm 8 kuralı 9: 't' adayı yalnız 'e' / 'â' ile biten adda
    kb = next((x for x in aday if x in BL), None)
    if kb is not None:  # bölüm 8 kuralı 9: kaydın kendi bloğunun morph LEM'inden
        if all(BL[kb]) and not notlu: NOTSUZ.append('%s %s' % (bag, ad))
        continue
    if not aday and k in BLP: continue  # edat adı ('bel', 'lev' …)
    if not aday:
        aday = sorted(set().union(*[LEMS2.get(zayif(x), set()) for x in (k, k.rstrip('n'), k.rstrip('h'))]))
    if not aday:
        if bag == 'çakışma parantez': continue  # yüzey biçimleri: LEM dışı sayılmaz
        LDISI.append('%s %s' % (bag, ad)); continue
    if all(x in HAM_IS for x in aday) and not notlu: NOTSUZ.append('%s %s' % (bag, ad))
# bölüm 6 kuralı 3: kökü ve ayeti anılan ad, o ayetlerdeki o köklü morph LEM'lerinden birinin iskeletine eşit olmalı (normalleştirilmiş ad yakalanır)
KORP = {}
for l in open('/home/claude/calisma/morph.txt', encoding='utf-8'):
    if not l.startswith('%d:' % S): continue
    loc, fo, t, feat = l.rstrip('\n').split('\t'); a_ = int(loc.split(':')[1])
    r = re.search(r'ROOT:([^|]+)', feat); m = re.search(r'LEM:([^|]+)', feat)
    if r and m: KORP.setdefault((a_, r.group(1)), set()).add((ud.normalize('NFC', m.group(1)), (t == 'V' and bozuk(ud.normalize('NFC', m.group(1)), feat)) or ud.normalize('NFC', m.group(1)) in ELLE, t))
for ad_, kok, ayl, notlu in KOKLU:
    if not ayl: continue
    L = set().union(*[KORP.get((x, kok), set()) for x in ayl])
    if not L: continue
    if any(x[2] == 'V' for x in L): L = {x for x in L if x[2] == 'V'}  # çakışma kararları fiil karşılığı üzerine: fiil LEM'i varsa yalnız onlar
    es = [x for x in L if nb(isk_ar(x[0])) in (isk_la(ad_), isk_la(ad_) + 'h', isk_la(ad_).rstrip('h'))]
    if not es:
        H.append("normalleştirilmiş lemma adı '%s' (kök %s; morph LEM %s)" % (ad_, kok, ', '.join(sorted(isk_ar(x[0]) + ('/ham' if x[1] else '') for x in L))))
    elif all(x[1] for x in es) and not notlu:
        H.append("ham notsuz çakışma '%s' (kök %s)" % (ad_, kok))
print('ham LEM: kökü anılan çakışma adı %d' % len(KOKLU))
# meal maddesinde ham LEM'li her kelime için not (sayı eşlemesi, ayet ayet)
HAMW = {}
for l in open(_BK + 'b%s/morph%d.txt' % (NN, S), encoding='utf-8'):
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
for l in open(_BK + 'b%s/morph.txt' % NN, encoding='utf-8'):
    k, w, f = l.rstrip('\n').split('\t'); _, a, n = k.split(':'); MOR[(int(a), int(n))] = f
def anilis_metni(its_tetik, its_disi):  # bölüm 6 kuralı 4: anılış yalnız ◈ tetik maddesinde ve tetik dışı maddesinin 'anılış:' bölümünde
    return ' '.join(its_tetik + [x.split('anılış:', 1)[1] if 'anılış:' in x else '' for x in its_disi])
tet = anilis_metni(item('◈ tetik'), item('tetik dışı'))
_m = anilis_metni([], ["tetik dışı tarama: tetik dışı aday 1: 5:1 3. kelime قبل; ◈ tetik maddesinde anılmayan 1 (5:1 3. kelime قبل) — biçim ne olursa olsun 5:1 قبل 3. kelime"])
assert 'قبل' not in _m, 'mutasyon testi: araç çıktısı anılış sayıldı'  # mutasyon testi (bölüm 6 kuralı 4)
_olc = open(_BK + 'b%s/olcum.txt' % NN, encoding='utf-8').read().replace('**', '')
GL = dict(re.findall(r"(\S+) \*\((.*?)\)\*", open(_BK + 'b%s/olcum.txt' % NN, encoding='utf-8').read()))
GLS_TAM = {'can', 'kan', 'el', 'baş', 'yüz', 'et', 'ay', 'gün', 'ön'}
GLS_ON = ('önce', 'sonra', 'dünya', 'zaman', 'vakit', 'sabah', 'akşam', 'gece', 'yıl', 'ölüm', 'öldür', 'beden', 'ayak', 'göğüs', 'karın', 'kemik', 'hayat', 'dirilik')
def _zb(g):
    tk = re.findall(r'[a-zçğıöşüâîû]+', g.lower())
    return any(t in GLS_TAM or t.startswith(GLS_ON) for t in tk)
ADAY |= {r for r, g in GL.items() if _zb(g)}  # bölüm 6 kuralı 4: gloss türevli adaylar
def bolum(a):  # tetik maddelerinin S:a ile başlayan bütün bölümleri (bir sonraki 'S:b ' işaretine dek)
    par = re.split(r'(?<![\d:])(%d:\d+) ' % S, tet)
    return ' '.join(par[k + 1] for k in range(1, len(par) - 1, 2) if par[k] == '%d:%d' % (S, a))
TD, TDY = [], []
for (a, n), f in sorted(MOR.items()):
    if not A <= a <= B: continue
    r = re.search(r'ROOT:([^|]+)', f); r = r.group(1) if r else None
    T = bool(re.search(r'(?:^|\| |\+ )N\|T(?:\||$)', f))
    if (r in ADAY and r not in TETIK) or (T and r not in TETIK):
        etiket = (r or '—') + (' (morph T)' if T else '')  # sûre 6 bölüm 1 denetimi kuralı 13: boş kök alanı yok
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
# bölüm 6 kuralı 5: okuma / ◈D / fâsıla maddelerinde iki ayet numarasıyla alıntılanan kalıp — ortak kısım (kelime düzeyinde baş) sayımla anılmalı
ETIKETLER = ' '.join(open(f, encoding='utf-8').read() for f in glob.glob(Y + 'metin_%d_*_*.txt' % S))
SAYILI = set(re.findall(r"(?:[Hh]arekesiz|[Öö]nek kesilmiş|[Ll]emma dizisi) '((?:[^']|'(?=[a-zâîûçğışöü]))+)'", ETIKETLER))  # cümle başı büyük harf dahil
K8 = 0
for it in item('okuma') + item('◈D') + item('fâsıla'):
    for seg in it.split('; '):
        ay = set(re.findall(r'(?<![\d:])%d:(\d+)' % S, seg))
        qs = [q for q in re.findall(r"(?<![a-zâîûçğışöü])'((?:[^']|'(?=[a-zâîûçğışöü]))+)'", seg) if ' ' in q and not re.match(r'(?:dizi|say) \d', q)]  # blok 34: say2 anahtarı alıntısı (bölüm 14 denetimi kuralı 8) kalıp değil
        if len(ay) < 2 or len(qs) < 2: continue
        w = [q.split() for q in qs]; ort = []
        for parca in zip(*w):
            if len(set(parca)) == 1: ort.append(parca[0])
            else: break
        if not ort: continue
        K8 += 1; P = ' '.join(ort)
        if all(len(x) == len(ort) for x in w): P = qs[0]
        if not any(x == P or x.startswith(P) and len(P.split()) == len(x.split()) for x in SAYILI):
            H.append("ayetler arası ortak kalıp sayımsız '%s' (%s)" % (P, ', '.join('%d:%s' % (S, x) for x in sorted(ay, key=int))))
print('ayetler arası kalıp alıntısı: ayet eşlemesi %d; iki ayetli ortak kalıp %d' % (KAL, K8))
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
        if mm and len(tok) > 4 and tok.lower() not in ('kadir', 'tedbir', 'bedir', 'tır', 'takdir'):
            if "'%s-'" % tok.lower() in mb: continue  # blok 34: emir kipindeki fiil kökü ('indir', 'rızıklandır') — meal maddesinde 'X-' karşılığı olarak kayıtlı; '-dir' eki değil
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
PR = r"%d:\d+ / %d:\d+ \((?:[^()]|\([^()]*\))*\)" % (S, S)  # bölüm 6 kuralı 6: ayetler arası çiftler de bayt eşlenir
ar_x = set(re.findall(PR, ad.split('ayetler arası', 1)[1])) if 'ayetler arası' in ad else set()
dm_x = set()
for a in range(A, B + 1):
    d = M[a].split('— ayetler arası: ', 1)
    if len(d) > 1: dm_x |= set(re.findall(PR, d[1].split('\n')[0]))
dm_x = {x for x in dm_x if all(A <= int(y) <= B for y in re.findall(r'%d:(\d+)' % S, x.split(' (')[0])) or True}
for x in sorted(ar_x ^ dm_x): H.append('aday 1039 ayetler arası ' + ('yalnız ARIZA: ' if x in ar_x else 'yalnız ◇: ') + x)
print('aday 1039 eşlemesi: %d ayet; ayetler arası çift ARIZA %d / ◇ %d' % (B - A + 1, len(ar_x), len(dm_x)))
for h in H: print('HATA', h)
print('bolum5_kurallar hata:', len(H))

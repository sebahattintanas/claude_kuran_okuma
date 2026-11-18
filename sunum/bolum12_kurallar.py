# bölüm 12 (sûre 5) denetimi araç kuralları (bekleyen_ariza_5_b28.txt 2. öğe) — salt okur:
#  (2) emsal meal karşılık farkları maddesinde her emsal girdisi ' — ' sonrasında kapalı sözlükle ('çakışma değil' / 'çakışma — tam okuma sonu')
#  (3) bölüm içi eş edat: bu bloktaki edat karşılığı aynı bölümün önceki bloklarındaki karşılıklardan farklıysa meal kararı maddesinde o edat anılır
#  (4) lemma dizisi adları öğe öğe: say2 demetinin her öğesi önceki bloklarda başka adla anılmışsa hata ('fe-' / 've-' öneki karşılaştırmada düşer)
#  (6) ölçüm 'biçim QASEM' gerekçesi: tetikleyen kök(ler) (قسم / حلف; vâv-ı kasem 'و') gerekçede Arapça yazılı, başka kök yok
#  (8) meal kararı gerekçesindeki "('X' / 'Y'" karşılıkları es_lemma satırının karşılık kümesinde
#  (9) meal maddesinde 'masdar' etiketi yalnız morph VN kelimede
#  (1, 5, 7, 10: kural13, satir_aynen_tam, geriye_donuk, bolum11_kurallar kural 16 içinde)
# kullanım (/home/claude'dan): python3 sunum/bolum12_kurallar.py A B NN
import sys as _sy; _sy.path.insert(0, '/home/claude/sunum'); from sure import BK as _BK
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from sure import S
import re, sys, ast, glob, collections, importlib.util as iu
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
Y = '/home/claude/yamalar/'
H = []
TUM = ast.literal_eval('{' + open(Y + 'ariza_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read() + '}')[(A, B)]
ITEMS = [m for m in TUM if not re.match(r'bölüm (denetimi \(|\d+ denetiminden)', m)]
def item(bas): return [m for m in ITEMS if m.startswith(bas)]
def bol(s, sep='; '):
    out, d, cur, i = [], 0, '', 0
    while i < len(s):
        c = s[i]; d += c == '('; d -= c == ')'
        if d == 0 and s.startswith(sep, i): out.append(cur); cur = ''; i += len(sep); continue
        cur += c; i += 1
    out.append(cur); return out
W = collections.defaultdict(lambda: collections.defaultdict(list))
for l in open(_BK + 'b%s/morph%d.txt' % (NN, S), encoding='utf-8'):
    loc, f, t, feat = l.rstrip('\n').split('\t'); s_, a_, w_, p_ = map(int, loc.split(':'))
    W[a_][w_].append((f, t, feat))
KAPALI = ('çakışma değil', 'çakışma — tam okuma sonu')
mi = item('meal (okuma')
meal = mi[0] if mi else ''
# ── (2) emsal maddesi kapalı sözlük ──
if 'emsal meal karşılık farkları' in meal:
    em = meal.split('emsal meal karşılık farkları', 1)[1].split('): ', 1)[-1]
    for g in bol(em):
        if len(re.findall(r'\d+:\d+', g)) >= 2 and re.search(r'\d+:\d+ .{0,90}?/ \d+:\d+', g):
            dec = g.split(' — ', 1)[1] if ' — ' in g else ''
            if not dec.startswith(KAPALI): H.append('(2) emsal girdisi kapalı sözlük dışı: %s' % g[:90])
# ── (3) bölüm içi eş edat ──
plan, bas = collections.OrderedDict(), None
for l in open(Y + 'blok_plani_%d.txt' % S, encoding='utf-8'):
    if l.startswith('■'): bas = l[1:].strip(); plan[bas] = []
    m = re.match(r'\s*(\d+)\. ', l)
    if m and bas: plan[bas].append(int(m.group(1)))
blok = next((v for v in plan.values() if int(NN) in v), [])
ATLA = {'ve', 'fe', 'li', 'bi', 'min', 'fî', "'alâ", 'ilâ', "'an", 'inne', 'enne', 'en', 'mâ', 'lâ', 'ellezîne', 'ellezî', 'ellâtî', 'nâ', 'kum', 'hum', 'hu', 'hû', 'hî', 'hi', 'hâ', 'û', 'ûne', 'tum', 'ke', 'le', 'nne', 'yâ', 'eyy', 'entum', "ma'a", 'ka'}
def edatlar(nn):
    vp = _BK + 'b%02d/yap/veri.py' % nn
    if not _o.path.exists(vp): return {}
    sp = iu.spec_from_file_location('veri%d' % nn, vp); v = iu.module_from_spec(sp); sp.loader.exec_module(v)
    E = collections.defaultdict(set)
    for a, L in v.MK.items():
        for tr, q, its in L:
            for it in its:
                m = re.match(r"('(?:[^']|'(?=[a-zâîû]))+') (\d+)\. kelimede '([^']+)' ile", it)
                if m and m.group(1).strip("'") not in ATLA: E[m.group(1)].add(m.group(3))
    return E
if int(NN) in blok:
    once = collections.defaultdict(set)
    for nn in blok:
        if nn < int(NN):
            for k, v in edatlar(nn).items(): once[k] |= v
    km = ' '.join(item('meal karşılık farkı kararları'))
    for k, v in edatlar(int(NN)).items():
        if once.get(k) and not v <= once[k] and k not in km:
            H.append("(3) bölüm içi eş edat %s: bu blok %s / önceki %s — meal kararı maddesinde anılmamış" % (k, sorted(v - once[k]), sorted(once[k])))
# ── (4) lemma dizisi adları öğe öğe ──
def diziler(nn):
    d = _BK + 'b%02d' % nn
    if not (_o.path.exists(d + '/yap/metin_yap.py') and _o.path.exists(d + '/say2.txt')): return []
    S2D = {}
    for blk in open(d + '/say2.txt', encoding='utf-8').read().split('### ')[1:]:
        L = blk.strip().splitlines(); mm = re.match(r'lemma dizisi (\[.*\]) \|', L[1]) if len(L) > 1 else None
        if mm: S2D[L[0].strip()] = ast.literal_eval(mm.group(1))
    out = []
    for key, ad in re.findall(r"say\('(dizi \d+ \d+ \d+ \d+)', \"([^\"]+)\"", open(d + '/yap/metin_yap.py', encoding='utf-8').read()):
        if key in S2D and len(ad.split()) == len(S2D[key]): out.append((key, ad, S2D[key]))
    return out
nrm = lambda t: re.sub(r'^(?:fe|ve)-', '', t)
ONCE = collections.defaultdict(collections.Counter)
for nn in range(1, int(NN)):
    for key, ad, dz in diziler(nn):
        for t, e in zip(ad.split(), dz):
            if e: ONCE[tuple(e)][nrm(t)] += 1
for key, ad, dz in diziler(int(NN)):
    for i, (t, e) in enumerate(zip(ad.split(), dz)):
        if e and ONCE.get(tuple(e)) and nrm(t) not in ONCE[tuple(e)]:
            H.append("(4) %s '%s' %d. öğe '%s' / önceki bloklarda '%s'" % (key, ad, i + 1, t, "', '".join(k for k, _ in ONCE[tuple(e)].most_common())))
# ── (6) QASEM gerekçesi ──
ek = ' '.join(item('ölçüm edim / kip'))
for m in re.finditer(r"'biçim [A-Z +]*QASEM[A-Z +]*' \(((?:[^()]|\([^()]*\))*)\)", ek):
    on = ek[:m.start()]; aa = re.findall(r'%d:(\d+)' % S, on)
    if not aa: continue
    a = int(aa[-1]); T = set()
    for w, segs in W[a].items():
        for f, t, ft in segs:
            r = re.search(r'ROOT:([^|]+)', ft)
            if r and r.group(1) in ('قسم', 'حلف'): T.add(r.group(1))
            if t == 'P' and 'LEM:و' in ft and w + 0 in W[a] and any('GEN' in x[2].split('|') for x in W[a][w][1:]): T.add('و')
    yaz = set(re.findall(r'[ء-ي]{2,4}', m.group(1)))
    if not T <= yaz: H.append('(6) %d:%d QASEM gerekçesinde tetikleyen kök yazılmamış: %s' % (S, a, ' '.join(sorted(T - yaz))))
    if yaz - T - {'و'}: H.append('(6) %d:%d QASEM gerekçesinde tetiklemeyen kök: %s' % (S, a, ' '.join(sorted(yaz - T))))
    if not yaz: H.append('(6) %d:%d QASEM gerekçesinde kök yok' % (S, a))
# ── (8) karar gerekçesi karşılıkları es_lemma kümesinde ──
esl = meal.split('eş lemmaya farklı karşılık', 1)[1] if 'eş lemmaya farklı karşılık' in meal else ''
esl = esl.split('): ', 1)[-1].split('; emsal meal karşılık farkları')[0]
KUM = {}
for g in bol(esl):
    m = re.match(r"(.+?) \(morph LEM (?:eşit|farklı)[^)]*\): (.*)", g)
    if m: KUM[m.group(1).strip()] = set(re.findall(r"'((?:[^']|'(?=[a-zâîûçğışöü]))+)' \(", m.group(2)))
for g in bol(' '.join(item('meal karşılık farkı kararları')).split('): ', 1)[-1]):
    if ' — ' not in g: continue
    key, dec = g.split(' — ', 1)
    key = key.strip()
    if key not in KUM: continue
    mm = re.search(r"\('((?:[^']|'(?=[a-zâîûçğışöü]))+)' / '((?:[^']|'(?=[a-zâîûçğışöü]))+)'", dec)
    if mm:
        for x in mm.groups():
            if x not in KUM[key]: H.append("(8) %s kararında '%s' es_lemma karşılık kümesinde yok (%s)" % (key[:40], x, ', '.join(sorted(KUM[key]))))
# ── (9) masdar ⇔ VN ──
vp = _BK + 'b%s/yap/veri.py' % NN
if _o.path.exists(vp):
    sp = iu.spec_from_file_location('veri', vp); v = iu.module_from_spec(sp); sp.loader.exec_module(v)
    for a, L in v.MK.items():
        for tr, q, its in L:
            for it in its:
                m = re.match(r"'[^']+' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı) \((\d+)\. kelime;([^)]*)", it)
                if m and re.search(r'masdar(?![ıi]n)', m.group(2)) and not any('VN' in ft.split('|') for f, t, ft in W[a][int(m.group(1))]):
                    H.append('(9) %d:%d %s. kelime masdar etiketi, morph VN değil' % (S, a, m.group(1)))
for h in H: print('HATA', h)
print('bolum12_kurallar hata:', len(H))

# bölüm 7 (sûre 5) denetiminden kurallar — betik denetimi:
#  (1) çakışma grubu üye kümesi ⇔ cakisma.py; kapalı kararın üye kümesi daralmadan tersine çevrilmesi
#  (2) KÖK grubunda üyelerin morph kökleri: birden çok kök → 'çakışma — tam okuma sonu'; 'bir kök' gerekçesi yalnız tek köklü kümede
#  (3) A1 etiket düzeyi: şahıs etiketli her morph segmentinin etiketi, o kelimeyi anan A1 alt maddesinde; A1 etiket kümesi ⇔ ölçüm 'şahıs'
#  (4) ◈ tetik kapsamı: tetik köklü her kelime ◇ ◈K / ◈B'de numarasıyla; ARIZA ◈ tetik maddesi (ayet, kök) kümesi ⇔ ◇ ◈ satırları
#  (7) D3 dışı listesi ⇔ say2 basılmış eşleri − blok ayetleri − bag − ayetler arası kalıp kayıtlarında anılanlar; 've başkaları' yok
#  (9) bölüm maddesindeki 'bölüm X-k' ⇔ yamalar/blok_plani_5.txt
#  (10) araç değişikliği maddesi ⇔ değişen sunum/ dosyaları (commit'li blokta o commit; yeni blokta repo HEAD ile fark)
#  (12) nakarat3 maddesi: ayet başına ad ⇔ ölçüm kalıbı birebir (eş ad iki kalıba verilmez; bitişik 'bi-' / 'fe-' öneki korunur)
# kullanım (/home/claude'dan): python3 sunum/bolum7_kurallar.py A B NN
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from sure import S
import re, sys, ast, glob, subprocess, importlib.util, unicodedata as ud
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
Y = '/home/claude/yamalar/'; R = '/home/claude/repo'
H = []
M = {}; exec(open(Y + 'metin_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read(), {'M': M, 'MEAL': {}})
AR = ast.literal_eval('{' + open(Y + 'ariza_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read() + '}')
ITEMS = [m for v in AR.values() for m in v if not re.match(r'bölüm (denetimi \(|\d+ denetiminden)', m)]
def item(bas): return [m for m in ITEMS if m.startswith(bas)]
def run(*a, cwd='/home/claude'): return subprocess.run(list(a), capture_output=True, text=True, cwd=cwd).stdout
def veri(nn):
    p = '/home/claude/b%s/yap/veri.py' % nn
    if not _o.path.exists(p): return {}
    sp = importlib.util.spec_from_file_location('veri' + nn, p); v = importlib.util.module_from_spec(sp); sp.loader.exec_module(v); return v.MK
MOR = {}  # (a, w) → [(form, feat)]
for l in open('/home/claude/b%s/morph%d.txt' % (NN, S), encoding='utf-8'):
    loc, fo, t, ft = l.rstrip('\n').split('\t'); s_, a_, w_, p_ = map(int, loc.split(':'))
    MOR.setdefault((a_, w_), []).append((fo, ft))
def kok(a, w):
    for fo, ft in MOR.get((a, w), []):
        m = re.search(r'ROOT:([^|]+)', ft)
        if m: return m.group(1)
Q = r"'((?:[^']|'(?=[a-zâîûçğışöü']))+)'"
def derinlik0(t):
    out, d = '', 0
    for ch in t:
        if ch == '(': d += 1; continue
        if ch == ')': d -= 1; continue
        if d == 0: out += ch
    return out
def karar(t): return 'değil' if 'çakışma değil' in t else ('tam' if 'çakışma — tam okuma sonu' in t else None)
# ── (1) / (2) çakışma grupları ──
DOS = sorted([f for f in glob.glob(Y + 'ariza_%d_*_*.txt' % S) if int(f.split('_')[-2]) <= A], key=lambda p: int(p.split('_')[-2]))
MK = veri(NN)
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}
CAK = [l for l in run('python3', '/home/claude/sunum/cakisma.py', *DOS).splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
def segmentler(cm):  # başlık → (üye kümesi, karar, parça)
    hs = [(m.start(), m.group(0)) for m in re.finditer(r"(?:KÖK )?'[^']+' ←", cm)]
    out = {}
    for k, (p, h) in enumerate(hs):
        parca = cm[p + len(h): hs[k + 1][0] if k + 1 < len(hs) else len(cm)]
        d, j = 0, None
        for i, ch in enumerate(parca):
            d += (ch == '(') - (ch == ')')
            if ch == ':' and d == 0 and parca[i + 1:i + 2] == ' ': j = i; break
        uye = set(re.findall(Q, derinlik0(parca[:j] if j is not None else parca)))
        out[h] = (uye, karar(parca), parca)
    return out
cm = ' '.join(item('karşılık çakışması'))
SEG = segmentler(cm)
ONCEKI = {}
for f in DOS:
    if f.endswith('_%d_%d.txt' % (A, B)): continue
    for it in [m for v in ast.literal_eval('{' + open(f, encoding='utf-8').read() + '}').values() for m in v if m.startswith('karşılık çakışması')]:
        ONCEKI.update(segmentler(it))
FORMKOK = {}  # bölüm 7 kuralı 2: meal kayıtlarından biçim → morph kökü (okunmuş bütün bloklar)
for d in sorted(glob.glob('/home/claude/b[0-9][0-9]')):
    nn = d[-2:]
    if int(nn) > int(NN) or not _o.path.exists(d + '/morph%d.txt' % S): continue
    RT = {}
    for l in open(d + '/morph%d.txt' % S, encoding='utf-8'):
        loc, fo, t, ft = l.rstrip('\n').split('\t'); s_, a_, w_, p_ = map(int, loc.split(':')); m = re.search(r'ROOT:([^|]+)', ft)
        if m: RT[(a_, w_)] = m.group(1)
    for a, L in veri(nn).items():
        for tr, q, its in L:
            for it in its:
                m = re.match(r"(?<![^\s(\[])'((?:[^']|(?<=[A-Za-zâîûçğışöüÇĞİÖŞÜ])'(?=[a-zâîûçğışöü]))+)' '((?:[^']|'(?=[a-zâîûçğışöü']))+)' (?:karşılığı|açılımı) \(((?:\d+(?:-\d+)?\.,? (?:ve )?)+)kelime", it)
                if not m: continue
                for x in re.findall(r'(\d+)(?:-(\d+))?\.', m.group(3)):
                    for w in range(int(x[0]), int(x[1] or x[0]) + 1):
                        if (a, w) in RT: FORMKOK.setdefault((m.group(1), m.group(2)), set()).add(RT[(a, w)])  # bölüm 8 kuralı 11: anahtar (Türkçe karşılık, Arapça biçim)
for l in CAK:
    if l.startswith('KÖK'):
        h = "KÖK '%s' ←" % l.split()[1]
        grup = [(ad.strip(), ast.literal_eval(lst)) for ad, lst in re.findall(r'(?:← |; )([^;\[]+?) (\[[^\]]*\])', l)]
        bek = {ad for ad, _ in grup}; formlar = {(ad, f) for ad, L in grup for f in L}
    else:
        h = "'%s' ←" % l.split(' ←')[0].strip()
        formlar = set(ast.literal_eval(l.split(' ← ', 1)[1])); bek = formlar; formlar = {(l.split(' ←')[0].strip(), f) for f in formlar}
    if h not in SEG: continue  # başlık yokluğu bolum6 kuralı 2'nin işi
    uye, kr, parca = SEG[h]
    if uye != bek: H.append('(1) çakışma üye kümesi %s ARIZA eksik %s / fazla %s' % (h, sorted(bek - uye), sorted(uye - bek)))
    if h in ONCEKI:
        pu, pk, _ = ONCEKI[h]
        if pk and kr and pk != kr and pu <= uye and not (re.search(r'önceki karar \(blok \d+', parca) and 'gerekçe' in parca):  # bölüm 8 kuralı 12: iki yönlü; önceki karar (blok, karar) ve gerekçe yazılınca susar
            H.append('(1) kapalı karar çevrildi %s: önceki %s → %s (üye kümesi daralmadı; önceki karar ve gerekçe yazılmamış)' % (h, pk, kr))
    if l.startswith('KÖK'):
        kokler = set().union(*[FORMKOK.get(f, set()) for f in formlar]) if formlar else set()
        if len(kokler) > 1 and kr != 'tam': H.append('(2) KÖK grubu birden çok kök %s (%s) — karar tam okuma sonu olmalı' % (h, ' / '.join(sorted(kokler))))
        if len(kokler) > 1 and 'bir kök' in parca: H.append("(2) KÖK grubu 'bir kök' gerekçesi, kök kümesi %s: %s" % (' / '.join(sorted(kokler)), h))
print('çakışma üye / KÖK kök denetimi: grup %d' % len(CAK))
# ── (3) A1 etiket düzeyi ──
TAG = r'(?<![A-Za-z0-9])(1P|1S|2MS|2FS|2MP|2FP|2D|3MS|3FS|3D|3MD|3FD|3MP|3FP)(?![A-Za-z0-9])'
def kelime(q):
    n = 0
    for t in q.split():
        if t in ('ve', 'fe', 'fa', 'va', 'yâ'): continue
        parca = re.split(r"(?<=[aeiuâîû])'(?=l-|ll|[a-zçğışöü]-|[bcdfğhklmnqrsştxyz]{2})", t)
        n += 1 + sum(1 for x in parca[:-1] if x not in ('ve', 'fe', 'fa', 'va', 'bi', 'li', 'le', 'ke') and not x.endswith('-'))
    return n
olc = [l.replace('**', '') for l in open('/home/claude/b%s/olcum.txt' % NN, encoding='utf-8').read().split('\n\n') if l.strip()]
EN = 0
for a in range(A, B + 1):
    t = M[a]; d = re.match(r"◇ '(.*?)' — ", t).group(1)
    a1 = t[t.index('A1 ') + 3:t.index(' A2 ')]
    its, dd, cur = [], 0, ''
    for ch in a1:
        dd += (ch == '(') - (ch == ')')
        if ch == ';' and dd == 0: its.append(cur); cur = ''
        else: cur += ch
    its.append(cur)
    KAP = []
    for it in its:
        K = set()
        for x in re.findall(r'(?<![\d:])(\d+)(?:-(\d+))?\.(?=[ ,])', it): K.update(range(int(x[0]), int(x[1] or x[0]) + 1))
        for q in re.findall(Q, it):
            for mm in re.finditer(re.escape(q), d):
                on = d[:mm.start()]
                if on.endswith('-'): on = on[:on.rfind(' ') + 1]
                bas = kelime(on.rstrip("'")) + 1 if on.endswith("'") else kelime(on) + 1
                K.update(range(bas, bas + max(kelime(q), 1)))
        KAP.append((K, set(re.findall(TAG, it))))
    for (aa, w), segs in sorted(MOR.items()):
        if aa != a: continue
        for fo, ft in segs:
            m = re.search(r'(?:^|\|)([123](?:M|F)?(?:S|D|P))(?:\||$)', ft)
            if not m: continue
            EN += 1
            if not any(w in K and m.group(1) in T for K, T in KAP): H.append('(3) A1 etiket %d:%d %d. kelime %s (%s) — kelimeyi anan alt maddede etiket yok' % (S, a, w, m.group(1), fo))
    om = re.search(r'şahıs ((?:\d[A-Z]+ \d+(?: · )?)+)', olc[a - A])
    okume = set(re.findall(r'(\d[A-Z]+) \d+', om.group(1))) if om else set()
    a1k = set(re.findall(TAG, a1))
    if okume != a1k: H.append('(3) A1 etiket kümesi %d:%d ölçüm %s / A1 %s' % (S, a, sorted(okume), sorted(a1k)))
print('A1 etiket düzeyi: segment %d' % EN)
# ── (4) ◈ tetik kapsamı ──
SINIF = {}
for c, ks in {'K1': 'سمو أرض شمس قمر نجم كوكب ليل نهر فلك سحب روح موه بحر جبل', 'K2': 'يوم أجل سنو عمر سوع دهر أبد حين',
              'B1': 'أنس دبب نعم طير نبت شجر', 'B2': 'خلق نطف علق زوج حمل وضع أنث', 'B3': 'عنق ذقن يدي عين سمع بصر جلد قلب', 'B4': 'حيي موت'}.items():
    for k in ks.split(): SINIF[k] = c
# S1 lemma kısıtı (calisma/oturum_tetik.py ile eş): روح سوع سنو سمو نعم kökünde yalnız izinli lemma tetikler
_s.path.insert(0, '/home/claude/calisma'); _cwd = _o.getcwd(); _o.chdir('/home/claude/calisma')
from oturum_tetik_s1 import izinli as _izinli
_o.chdir(_cwd)
def lem(a, w):
    for fo, ft in MOR.get((a, w), []):
        m = re.search(r'LEM:([^|]+)', ft)
        if m and re.search(r'ROOT:', ft): return m.group(1)
def tetikler(a, w): return kok(a, w) in SINIF and _izinli(kok(a, w), lem(a, w))
DIA = set()
for a in range(A, B + 1):
    sat = ' '.join(l for l in M[a].split('\n') if l.startswith(('◈K', '◈B')))
    nums = {int(x) for x in re.findall(r'(\d+)\.', sat)}
    for (aa, w) in sorted(MOR):
        if aa == a and tetikler(a, w) and w not in nums: H.append('(4) tetik kapsamı %d:%d %d. kelime %s ◈ satırında yok' % (S, a, w, kok(a, w)))
    DIA |= {(a, kok(a, n)) for n in nums if tetikler(a, n)}  # bölüm 9 kuralı 12: ◇ ⇔ ARIZA kümesi de S1 süzgeciyle; ◈'de S1 dışı lemma isabet
    for n in sorted(nums):
        if kok(a, n) in SINIF and not tetikler(a, n): H.append('(4) ◈ satırında S1 dışı lemma %d:%d %d. kelime %s' % (S, a, n, kok(a, n)))
tt = ' '.join(item('◈ tetik'))
ARZ = {(int(a), r) for a, r in re.findall(r'%d:(\d+) ◈[KB] ([؀-ۿ]+)' % S, tt)}
if ARZ != DIA: H.append('(4) ◈ tetik maddesi ⇔ ◇: ARIZA fazla %s / ◇ fazla %s' % (sorted(ARZ - DIA), sorted(DIA - ARZ)))
print('◈ tetik kapsamı: ◇ %d, ARIZA %d' % (len(DIA), len(ARZ)))
# ── (7) D3 dışı listesi ──
d3 = ' '.join(item('◈D D3 / bag'))
if 've başkaları' in d3: H.append("(7) D3 dışı listesinde 've başkaları'")
U = set()
for blk in open('/home/claude/b%s/say2.txt' % NN, encoding='utf-8').read().split('### ')[1:]:
    L = blk.strip().splitlines()
    if '--medde' in L[0]: continue
    m = re.match(r'(\d+) (\{.*\})$', L[-1].strip())
    if m: U |= set(ast.literal_eval(m.group(2))['basilan'])
bag = ast.literal_eval('[' + open(Y + 'bag_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read() + ']')
BAG = {x for b in bag for x in b['bag'].split(' → ')}
if 'D3 dışı bırakılan basılmış sayım eşleri' in d3:
    on, son = d3.split('D3 dışı bırakılan basılmış sayım eşleri', 1)
    son = son.split(' — kalıp başına')[0]
    if re.search(r'%d:%d: ' % (S, A), son):  # bölüm 10 denetimi kuralı 11: ayet başına liste ('S:A: …' / 'yok')
        UA = {}
        for blk in open('/home/claude/b%s/say2.txt' % NN, encoding='utf-8').read().split('### ')[1:]:
            L = blk.strip().splitlines()
            if '--medde' in L[0]: continue
            mk = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', L[0]); m = re.match(r'(\d+) (\{.*\})$', L[-1].strip())
            if mk and m: UA.setdefault(int(mk.group(1) or mk.group(2)), set()).update(ast.literal_eval(m.group(2))['basilan'])
        ONB = {'%d:%d' % (S, a) for a in range(A, B + 1)}
        for a in range(A, B + 1):
            ms = re.search(r'%d:%d: (.*?)(?=; %d:\d+: |$)' % (S, a, S), son)
            la = set(re.findall(r'\d+:\d+', ms.group(1))) if ms else set()
            ka = {b['bag'].split(' → ')[0] for b in bag if b['bag'].split(' → ')[1] == '%d:%d' % (S, a)}
            ba = UA.get(a, set()) - ONB - ka - set(re.findall(r'\d+:\d+', ' '.join(re.findall(r'ayetler arası kalıp[^;]*', on))))  # yalnız ayetler arası kalıp kayıtlarında anılanlar
            if la != ba: H.append('(7) D3 dışı listesi %d:%d eksik %s / fazla %s' % (S, a, sorted(ba - la), sorted(la - ba)))
        liste = bek = set()
    liste = set(re.findall(r'\d+:\d+', son)) - {'%d:%d' % (S, a) for a in range(A, B + 1)}  # blok ayeti etiketleri liste öğesi değil
    bek = U - {'%d:%d' % (S, a) for a in range(A, B + 1)} - BAG - set(re.findall(r'\d+:\d+', on))
    if re.search(r'%d:%d: ' % (S, A), son): liste = bek  # ayet başına biçim yukarıda denetlendi
    if liste != bek: H.append('(7) D3 dışı listesi eksik %s / fazla %s' % (sorted(bek - liste), sorted(liste - bek)))
    print('D3 dışı: beklenen %d, liste %d' % (len(bek), len(liste)))
# ── (9) bölüm sırası ──
plan, bol, sira = open(Y + 'blok_plani_%d.txt' % S, encoding='utf-8').read().splitlines(), 0, {}
k = 0
for l in plan:
    if l.startswith('■'): bol += 1; k = 0
    m = re.match(r'\s*\d+\. %d:(\d+)-(\d+)' % S, l)
    if m: k += 1; sira[(int(m.group(1)), int(m.group(2)))] = (bol, k)
bm = ' '.join(item('bölüm:'))
if (A, B) in sira:
    x = re.search(r'bölüm (\d+)-(\d+)', bm)
    if not x or (int(x.group(1)), int(x.group(2))) != sira[(A, B)]: H.append('(9) bölüm sırası: ARIZA %s / plan %d-%d' % (x.group(0) if x else '—', *sira[(A, B)]))
# ── (10) araç değişikliği ──
HAR = ('sunum/basilan.txt', 'sunum/sinifla.py')
ad = 'yamalar/ariza_%d_%d_%d.txt' % (S, A, B)
c = run('git', 'log', '--diff-filter=A', '--format=%H', '--', ad, cwd=R).split()
if c:
    deg = [f for f in run('git', 'show', '--name-only', '--format=', c[-1], cwd=R).split() if f.startswith('sunum/') and f not in HAR]
else:
    deg = []
    for f in sorted(glob.glob('/home/claude/sunum/*')):
        if f.endswith('__pycache__') or _o.path.isdir(f): continue
        rel = 'sunum/' + _o.path.basename(f)
        if rel in HAR: continue
        eski = subprocess.run(['git', 'show', 'HEAD:' + rel], capture_output=True, cwd=R).stdout
        if eski != open(f, 'rb').read(): deg.append(rel)
ad_it = ' '.join(item('araç değişikliği'))
if deg and 'araç değişmedi' in ad_it: H.append('(10) araç değişikliği: değişen %s, madde "araç değişmedi"' % ', '.join(deg))
for f in deg:
    if f not in ad_it: H.append('(10) araç değişikliği maddesinde yok: %s' % f)
print('araç değişikliği: %d dosya' % len(deg) + (' — ' + ', '.join(deg) if deg else ''))
# ── (12) nakarat3 ad ⇔ ölçüm kalıbı ──
nk = ' '.join(item('nakarat3 (R3'))
parcalar = re.split(r'(?:^|; )((?:%d:\d+(?: ve |, )?)+) ' % S, nk.split('): ', 1)[1] if '): ' in nk else '')
for i in range(1, len(parcalar) - 1, 2):
    ays = [int(x) for x in re.findall(r'%d:(\d+)' % S, parcalar[i])]
    adlar = re.findall(r"(?:^|, | ve |; )'(.+?)'(?=, '| ve '| süzgeç| GEÇ| \(|;|$)", parcalar[i + 1])
    kal = []
    for a in ays:
        if A <= a <= B:
            for p in re.findall(r"`nakarat3` '([^']+)' \(", olc[a - A]):
                if p not in kal: kal.append(p)
    if not kal: continue
    if len(adlar) != len(set(adlar)): H.append('(12) nakarat3 %s: eş ad iki kalıba verilmiş (%s)' % (parcalar[i].strip(), ', '.join(sorted({x for x in adlar if adlar.count(x) > 1}))))
    if len(adlar) != len(kal): H.append('(12) nakarat3 %s: ad %d / ölçüm kalıbı %d' % (parcalar[i].strip(), len(adlar), len(kal)))
    for on, lat in (('ب', 'bi-'), ('ف', 'fe-')):
        nk_k = sum(1 for p in kal if '|' not in p.split()[0] and p.split()[0].startswith(on) and len(p.split()[0]) > 2)
        nk_a = sum(1 for x in adlar if x.startswith(lat))
        if nk_k != nk_a: H.append("(12) nakarat3 %s: '%s' önekli ölçüm kalıbı %d / '%s' ile başlayan ad %d" % (parcalar[i].strip(), on, nk_k, lat, nk_a))
# bölüm 8 kuralı 13: ad ⇔ ölçüm kalıbı içerik eşlemesi (öğe öğe, sıra korunarak; GEÇER / GEÇMEZ ayrımı ölçüm sırasıyla)
mpa = {'ب':'b','ت':'t','ث':'s','ج':'c','ح':'h','خ':'x','د':'d','ذ':'z','ر':'r','ز':'z','س':'s','ش':'ş','ص':'s','ض':'d','ط':'t','ظ':'z','غ':'ğ','ف':'f','ق':'q','ك':'k','ل':'l','م':'m','ن':'n','ه':'h','و':'v','ي':'y','ى':'y','ة':'h'}
def ska(w):
    w = ''.join(c for c in ud.normalize('NFD', w.replace('ؤ', '').replace('ئ', '')) if not ud.combining(c))  # hemze kürsüsü (و / ي) iskelete girmez
    return re.sub(r'(.)\1+', r'\1', ''.join(mpa.get(c, '') for c in w))
def skl(t):
    t = t.lower().replace('û', 'v').replace('î', 'y')
    return re.sub(r'(.)\1+', r'\1', ''.join(c for c in t if c in 'bcdfğhklmnqrsştxzvy'))
def oge_es(ad, p):
    if ad == '_': return True
    a_ = skl(ad)
    if '|' in p:
        b_ = ska(p.split('|')[1])
        return a_ in (b_, b_.rstrip('h'), b_ + 'h', b_.rstrip('t'), b_.rstrip('yv')) or b_.rstrip('h') == a_.rstrip('t') or a_.rstrip('yv') == b_.rstrip('yv')
    b_ = ska(p)
    return bool(a_) and (a_ in b_ or b_ in a_) or (not a_ and not b_)
for i in range(1, len(parcalar) - 1, 2):
    ays = [int(x) for x in re.findall(r'%d:(\d+)' % S, parcalar[i])]
    metin_ = parcalar[i + 1]
    kal = []
    for a in ays:
        if A <= a <= B:
            for p, sz in re.findall(r"`nakarat3` '([^']+)' \([^)]*\) → süzgeç (GEÇER|GEÇMEZ)", olc[a - A]):
                if (p, sz) not in kal: kal.append((p, sz))
    if not kal: continue
    adl = []  # ad başına süzgeç: addan sonra gelen ilk GEÇER / GEÇMEZ (yalnız GEÇMEZ'li parça da doğru okunur)
    for m_ in re.finditer(r"(?:^|, | ve |; )'(.+?)'(?=, '| ve '| süzgeç| GEÇ| \(|;|$)", metin_):
        st_ = re.search(r'GEÇMEZ|GEÇER', metin_[m_.end():])
        if st_: adl.append((m_.group(1), st_.group(0)))
    adl = [k for k in adl if k[1] == 'GEÇER'] + [k for k in adl if k[1] == 'GEÇMEZ']
    kal_g = [k for k in kal if k[1] == 'GEÇER'] + [k for k in kal if k[1] == 'GEÇMEZ']
    if len(adl) != len(kal_g): continue  # sayı farkı kural 12'nin işi
    for (ad, sz_a), (p, sz_p) in zip(adl, kal_g):
        if sz_a != sz_p: H.append("(13) nakarat3 %s: '%s' %s yazılmış, ölçüm %s" % (parcalar[i].strip(), ad, sz_a, sz_p)); continue
        po, ao = p.split(), ad.split()
        if len(po) != len(ao) or not all(oge_es(x, y) for x, y in zip(ao, po)): H.append("(13) nakarat3 %s: ad '%s' ⇔ ölçüm kalıbı '%s' öğe eşlemesi tutmuyor" % (parcalar[i].strip(), ad, p))
for h in H: print('HATA', h)
print('bolum7_kurallar hata:', len(H))

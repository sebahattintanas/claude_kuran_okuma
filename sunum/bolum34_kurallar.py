# sûre 6 bölüm 18 denetimi araç kuralları (bekleyen_ariza_6_b38.txt 2. öğe) — salt okur:
#  (1) BAG_DIZI_JOKER: bag kaydındaki 'en uzun ortak lemma dizisi' adında, say2 'dizi' satırında lemmasız '()' olan öğe joker '_' ile yazılır; öğe sayısı dizi uzunluğuna eşittir
#  (2) A1_EK_PRON_SINIRI: A1'de '… eki (…)' listesine giren kelime morph'ta PRON parçası taşır (ADDR / DIST parçalı işaret zamir eki sayılmaz)
#  (3) ADAY1041_ES_AYET: aday 1041 maddesinde bir kök en az iki ayetle ya da 'bölüm içi' notuyla yazılır; eşsiz kök maddeye girmez
#  (4) KIP_NOTU_FIIL_SAYISI: kip notundaki ayet başı fiil girişi sayısı morph fiil kelimesi sayısına eşittir
#  (5) TETIK_DISI_KELIME_TAM: 'tetik dışı aday' listesindeki her kök taşıyan (ayet, kelime) çifti 'anılış' bölümünde o ayetin altında 'N. kelime' ile yer alır
# (elle: MUHAFFEFE_SART_AYRIMI, KAPSAM_DISI_GEREKCE, SOZ_KAPANIR_EK, UYUM_ETIKETI_TANIM, EMSAL_FARK_TAM, KIP_SAPMA_ES_OLCUT, NAKARAT_AD_LEMMA)
# kullanım (/home/claude'dan): python3 sunum/bolum34_kurallar.py A B NN
import re, sys, ast, os, collections
import sys as _sy; _sy.path.insert(0, '/home/claude/sunum'); from sure import BK as _BK, S
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
Y = '/home/claude/yamalar/'
H = []
TUM = ast.literal_eval('{' + open(Y + 'ariza_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read() + '}')[(A, B)]
ITEMS = [m for m in TUM if not re.match(r'(bölüm (denetimi \(|\d+ denetiminden)|devir \()', m)]
M, MEAL = {}, {}
exec(open(Y + 'metin_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read(), {'M': M, 'MEAL': MEAL})
EN = collections.Counter()
def item(bas): return [m for m in ITEMS if m.startswith(bas)]
def satir(n, bas):
    for l in M[n].split('\n'):
        if l.startswith(bas): return l
    return ''
def a4(a):
    l = satir(a, '◈A')
    return l.split(' A4 ', 1)[1] if ' A4 ' in l else ''
MOR = collections.defaultdict(dict)
_mf = _BK + 'b%s/morph.txt' % NN
if os.path.exists(_mf):
    for l in open(_mf, encoding='utf-8'):
        p = l.rstrip('\n').split('\t')
        if len(p) >= 3:
            s_, a_, w_ = p[0].split(':')[:3]
            if int(s_) == S: MOR[int(a_)][int(w_)] = p[2]
O = [l for l in open(_BK + 'b%s/olcum.txt' % NN, encoding='utf-8').read().replace('**', '').split('\n\n') if l.strip()] if os.path.exists(_BK + 'b%s/olcum.txt' % NN) else []
S2, BAS, LEM = {}, {}, {}
_s2 = _BK + 'b%s/say2.txt' % NN
if os.path.exists(_s2):
    for blk in re.split(r'^### ', open(_s2, encoding='utf-8').read(), flags=re.M)[1:]:
        h = blk.split('\n', 1)[0].strip()
        m = re.search(r"\{'bu'.*\}", blk)
        if m: S2[h] = ast.literal_eval(m.group(0))
        lm = re.search(r'liste: (.*)', blk)
        ls = blk.split('\n')
        if h.startswith('dizi'):
            BAS[h] = set(x.strip('†') for x in (ls[2] if len(ls) > 2 else '').split(', ') if x.strip())
            mm = re.search(r'lemma dizisi (\[.*?\]) \|', blk)
            if mm:
                try: LEM[h] = ast.literal_eval(mm.group(1))
                except Exception: pass
        elif lm: BAS[h] = set(x.strip('†') for x in lm.group(1).split(', '))
SRC = open(_BK + 'b%s/yap/metin_yap.py' % NN, encoding='utf-8').read() if os.path.exists(_BK + 'b%s/yap/metin_yap.py' % NN) else ''
DIZ = re.findall(r"say\('(dizi %d \d+ \d+ \d+)', \"([^\"]+)\"\)" % S, SRC) + re.findall(r"say\('(dizi %d \d+ \d+ \d+)', '([^']+)'\)" % S, SRC)


import importlib.util as _iu
def dia(a): 
    l = M[a].split('\n')[0] if a in M else ''
    m = re.search(r"◇ '(.*?)' — ", l)
    return m.group(1) if m else ''
# ── (1) BAG_DIZI_JOKER ──
_bf = Y + 'bag_%d_%d_%d.txt' % (S, A, B)
if os.path.exists(_bf):
    for m in re.finditer(r"en uzun ortak lemma dizisi '(.+?)' \((dizi %d \d+ \d+ \d+)\)" % S, open(_bf, encoding='utf-8').read()):
        ad, anh = m.group(1).split(), m.group(2)
        if anh not in LEM: continue
        EN['bag_dizi'] += 1
        if len(ad) != len(LEM[anh]): H.append("(1) bag %s adı %d öğe / say2 lemma dizisi %d öğe" % (anh, len(ad), len(LEM[anh]))); continue
        for k, (o, t) in enumerate(zip(ad, LEM[anh])):
            if not t and o != '_': H.append("(1) bag %s %d. öğe '%s' — say2'de lemmasız, joker '_' yok" % (anh, k + 1, o))
            if t and o == '_': H.append("(1) bag %s %d. öğe joker — say2'de lemma var" % (anh, k + 1))
# ── (2) A1_EK_PRON_SINIRI ──
for a in range(A, B + 1):
    a1 = satir(a, '◈A').split('; aktör', 1)[0]
    for m in re.finditer(r" eki \(([^()]*? — ([^()]*?)\. kelime)\)", a1):
        for w in re.findall(r'\d+', m.group(2)):
            EN['a1_ek'] += 1
            if 'PRON' not in MOR.get(a, {}).get(int(w), 'PRON'): H.append("(2) %d:%d %s. kelime A1 ek listesinde — morph'ta PRON parçası yok" % (S, a, w))
# ── (3) ADAY1041_ES_AYET ──
for it in item('aday 1041'):
    for seg_ in re.split(r'; ', it.split(': ', 1)[-1]):
        m = re.match(r'kök (\S+) ', seg_)
        if not m: continue
        EN['aday1041_kok'] += 1
        ay = set(re.findall(r'\b\d+:\d+', seg_))
        if len(ay) < 2 and 'bölüm içi' not in seg_: H.append("(3) aday 1041 kök %s %s — eş ayet yok, 'bölüm içi' notu yok" % (m.group(1), ', '.join(sorted(ay))))
# ── (4) KIP_NOTU_FIIL_SAYISI ──
for it in item('meal (okuma'):
    if 'kip notu' not in it: continue
    kn = it.split('kip notu', 1)[1].split('kip sapma notu', 1)[0].split('): ', 1)[-1]
    par = re.split(r'(?:^|; )(%d:\d+) (?=\')' % S, kn)
    for k in range(1, len(par) - 1, 2):
        a = int(par[k].split(':')[1])
        if not A <= a <= B: continue
        n = len(re.findall(r"' (?:PERF|IMPF|IMPV)\b", par[k + 1]))
        mv = sum(1 for w, f in MOR.get(a, {}).items() if re.search(r'(?:^|\+ )V\|', f))
        EN['kip_ayet'] += 1
        if n != mv: H.append("(4) %d:%d kip notu %d fiil / morph %d fiil" % (S, a, n, mv))
# ── (5) TETIK_DISI_KELIME_TAM ──
for it in item('tetik dışı'):
    if 'anılış:' not in it: continue
    ad_, an = it.split('anılış:', 1)
    par = re.split(r'(?<![\d:])(%d:\d+) ' % S, an)
    bol = collections.defaultdict(str)
    for k in range(1, len(par) - 1, 2): bol[par[k]] += ' ' + par[k + 1]
    for ay, w, r in re.findall(r'(%d:\d+) (\d+)\. kelime (\S+?)(?:,|;| \(|$)' % S, ad_.split('tetik dışı aday', 1)[-1].split('; ◈', 1)[0]):
        if r == '—': continue
        EN['tetik_disi'] += 1
        if not re.search(r'(?<!\d)%s\. kelime' % w, bol[ay]): H.append("(5) %s %s. kelime %s tetik dışı aday — anılışta kelime yok" % (ay, w, r))

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum34_kurallar hata: %d' % len(H))

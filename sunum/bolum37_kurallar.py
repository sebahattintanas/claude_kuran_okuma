# sûre 7 bölüm 2 denetimi araç kuralları (bekleyen_ariza_7_b06.txt 2. öğe) — salt okur:
#  (1) BOLUM_ICI_EDAT_TAM: morph etiketli her edat / zamir kesim notu başlığının bu blokta çıkan yeni karşılığı, bölümün önceki bloklarındaki karşılık kümesinde yoksa 'bölüm içi eş edat' maddesinde anılır
#  (2) ADAY1041_BOLUM_ICI_TAM: bu bloktaki kök bölümün önceki bloklarında geçiyorsa 'aday 1041' maddesinde anılır
#  (3) JOKER_PREF_LEMMA: lemma dizisindeki joker öğenin kelimesi morph'ta LEM taşıyorsa (önek lemması) bağ maddesi 'lemmasız' diyemez; 'önek lemmalı' diye adlandırılır
#  (4) ETIKET_EMPH_VE_KIP_YOK: morph P|EMPH|SUFF taşıyan fiilin ◇ etiket dizisinde 'n' parçası; ölçüm kipi boş ayetin D2'sinde 'kip yok' kaydı
#  (5) BLOK_ICI_ES_SAYIM: say2'de bu bloğun başka ayetini bulan kalıp ◇'de sayım cümlesiyle geçer
# (elle: EMSAL_FIIL_KAPSAMI, BOLUMDE_ADSIZ_SINIRI, MUHATAP_GONDERGE, MUHATAP_GECISI_BLOKLAR_ARASI, VASL_BAGIMSIZ_ALINTI, KIP_SAPMA_OLCUTU, DEM_LEMMA_ADI)
# kullanım (/home/claude'dan): python3 sunum/bolum37_kurallar.py A B NN
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
HRF = 'a-zçğıöşüâîûA-ZÇĞİÖŞÜÂÎÛ'
_vf = _BK + 'b%s/yap/veri.py' % NN
MK = {}
if os.path.exists(_vf):
    _sp = _iu.spec_from_file_location('veri', _vf); _v = _iu.module_from_spec(_sp); _sp.loader.exec_module(_v); MK = _v.MK
def _ar(its):
    n = [int(x) for it in its for x in re.findall(r"(?<!\d)(\d+)\. kelime", it)]
    return (min(n), max(n)) if n else None
_pl = Y + 'blok_plani_%d.txt' % S
BOLB = []
if os.path.exists(_pl):
    grp, cur = [], None
    for l in open(_pl, encoding='utf-8'):
        if l.startswith('■'): cur = []; grp.append(cur)
        else:
            m = re.match(r'\s*(\d+)\. ', l)
            if m and cur is not None: cur.append(int(m.group(1)))
    BOLB = next((g for g in grp if int(NN) in g), [])
onc = [n for n in BOLB if n < int(NN)]
def _veri(nn):
    f_ = _BK + 'b%02d/yap/veri.py' % nn
    if not os.path.exists(f_): return {}
    sp_ = _iu.spec_from_file_location('veri%d' % nn, f_); v_ = _iu.module_from_spec(sp_); sp_.loader.exec_module(v_)
    return v_.MK
def _edat(mk):
    d = {}
    for a_, L in mk.items():
        for tr_, q_, its in L:
            for x in its:
                m = re.match(r"'((?:[^']|'(?=[%s]))+)' \d+\. kelimede (.*?) \((?:[^()]*; )?morph ([A-Z]+)" % HRF, x)
                if m: d.setdefault((m.group(1), m.group(3)), set()).add(re.sub(r" ile$", '', m.group(2).strip()).lower())
    return d
def _kok(nn):
    f_ = _BK + 'b%02d/morph.txt' % nn
    return set(re.findall(r'ROOT:([^|\s]+)', open(f_, encoding='utf-8').read())) if os.path.exists(f_) else set()
bie = ' '.join(m.split('bölüm içi eş edat', 1)[1] for m in ITEMS if 'bölüm içi eş edat' in m)
# ── (1) BOLUM_ICI_EDAT_TAM ──
if onc:
    bu = _edat(MK); es = {}
    for n in onc:
        for k_, v_ in _edat(_veri(n)).items(): es.setdefault(k_, set()).update(v_)
    for k_ in sorted(set(bu) & set(es)):
        EN['edat'] += 1
        if (bu[k_] - es[k_]) and "'%s' (" % k_[0] not in bie: H.append("(1) '%s' (%s) bölüm içi yeni karşılık: bu blok %s / önceki %s — 'bölüm içi eş edat' maddesinde anılmamış" % (k_[0], k_[1], sorted(bu[k_]), sorted(es[k_])))
# ── (2) ADAY1041_BOLUM_ICI_TAM ──
if onc:
    ok_ = set().union(*[_kok(n) for n in onc]); a41 = ' '.join(item('aday 1041'))
    for r_ in sorted(_kok(int(NN)) & ok_):
        EN['kok'] += 1
        if r_ not in a41: H.append("(2) kök %s bölümün önceki bloklarında da geçiyor — 'aday 1041' maddesinde yok" % r_)
# ── (3) JOKER_PREF_LEMMA ──
bag = ' '.join(item('bağ: '))
if 'lemmasız' in bag and 'önek lemmalı' not in bag:
    for h, ad in DIZ:
        if h not in LEM: continue
        _, s_, a_, i_, j_ = h.split()
        for k_, t_ in enumerate(LEM[h]):
            if t_ == ():
                EN['joker'] += 1
                w_ = int(i_) + k_
                if 'LEM:' in MOR.get(int(a_), {}).get(w_, ''): H.append("(3) %s:%s %d. kelime joker '_' — morph LEM taşıyor (önek lemması); bağ maddesinde 'lemmasız' denmiş" % (s_, a_, w_))
# ── (4) ETIKET_EMPH_VE_KIP_YOK ──
for n_, a in enumerate(range(A, B + 1)):
    l0 = M[a].split('\n')[0] if a in M else ''
    em = [w for w, f in sorted(MOR.get(a, {}).items()) if 'EMPH|SUFF' in f]
    if em:
        EN['emph'] += 1
        if l0.count("+ 'n'") < len(em): H.append("(4) %d:%d %s. kelime morph EMPH|SUFF — ◇ etiket dizisinde 'n' parçası yok" % (S, a, ', '.join(map(str, em))))
    if n_ < len(O) and ', kip yok' in O[n_]:
        EN['kipyok'] += 1
        d2 = satir(a, '◈D').split(' D2 ', 1)[-1].split(' D3 ')[0]
        if 'kip yok' not in d2: H.append("(4) %d:%d D2 — ölçüm kipi boş, 'kip yok' kaydı yok" % (S, a))
# ── (5) BLOK_ICI_ES_SAYIM ──
for h, d in sorted(S2.items()):
    m = re.match(r'say %d:(\d+) (\d+)-(\d+)$' % S, h)
    if not m or not (A <= int(m.group(1)) <= B): continue
    dig = [x for x in d.get('basilan', []) if x.startswith('%d:' % S) and A <= int(x.split(':')[1]) <= B and int(x.split(':')[1]) != int(m.group(1))]
    if dig:
        EN['blok_ici'] += 1
        if "say('%s'" % h not in SRC: H.append("(5) %d:%s %s-%s. kelime kalıbı blok içinde %s ile eş — '%s' ◇'de sayım cümlesiyle geçmiyor" % (S, m.group(1), m.group(2), m.group(3), ', '.join(dig), h))

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum37_kurallar hata: %d' % len(H))

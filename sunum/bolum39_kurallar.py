# sûre 7 bölüm 4 denetimi araç kuralları (bekleyen_ariza_7_b11.txt 2. öğe) — salt okur:
#  (1) MEDDE_FARK_KELIMESI: ◇ medde notundaki yazım farkı kelimesi, aralığın tam ve '--medde' kalıp satırlarında ayrışan kelime olmalı
#  (2) MEDDE_NOTU_KARSILIKLI: bölümün önceki bloğunda medde notu taşıyan basılmış sûre içi eşi lemma dizisiyle bulan korpusta 1 aralığın ayeti 'yazım farkı' notu taşır
#  (3) BOLUM_ICI_EDAT_ETIKET: 'bölüm içi eş edat' maddesinde morph etiketi altındaki her karşılık, bölüm kesim notlarında o etiketi taşıyan kelimeden gelir
#  (4) NAKARAT3_HAM_KALIP: bölüm içinde eş nakarat3 adı farklı ölçüm ham kalıbına verildiyse R5 maddesi 'ham kalıp farkı' kaydı taşır
#  (5) D3_DISI_EMSAL: D3 dışı listesi bloğun emsal dosyasındaki ayeti taşıyamaz
# (elle: BAG_EN_UZUN_HAREKESIZ, CIFT_KARSILIK_PARCA, KIP_NOTU_GOVDE, PN_ETIKET_ES, GONDERGE_YAKINLIK, ESMA_KURAL_ADI_ES, CANLI_ADI_TETIK_DISI)
# kullanım (/home/claude'dan): python3 sunum/bolum39_kurallar.py A B NN
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
bie = ' '.join(m.split('bölüm içi eş edat', 1)[1] for m in ITEMS if 'bölüm içi eş edat' in m)
MI = (item('meal (okuma') or [''])[0]
EMI = MI.split('emsal meal karşılık farkları', 1)[1].split('kip notu (', 1)[0] if 'emsal meal karşılık farkları' in MI else ''
KN = MI.split('kip notu (', 1)[1].split('kip sapma notu', 1)[0] if 'kip notu (' in MI else ''
KS = MI.split('kip sapma notu', 1)[1] if 'kip sapma notu' in MI else ''
_ef = _BK + 'b%s/ems.txt' % NN
EMS = set(open(_ef, encoding='utf-8').read().split()) if os.path.exists(_ef) else set()
def _top(d): return len(d.get('bu', [])) + len(d.get('basilan', [])) + sum(d.get(k_, 0) if isinstance(d.get(k_, 0), int) else len(d.get(k_, [])) for k_ in ('eski', 'okunmus', 'okunmus_si', 'henuz', 'henuz_si'))
import glob
_AF = sorted(glob.glob(Y + 'ariza_%d_*_*.txt' % S), key=lambda p: int(p.split('_')[-2]))
def _aralik(nn):
    if 1 <= nn <= len(_AF):
        p = _AF[nn - 1].rsplit('.', 1)[0].split('_'); return int(p[-2]), int(p[-1])
    return None
def _metin(nn):
    r = _aralik(nn)
    if not r: return {}
    m_ = {}
    exec(open(Y + 'metin_%d_%d_%d.txt' % (S, r[0], r[1]), encoding='utf-8').read(), {'M': m_, 'MEAL': {}})
    return m_
KAL = {}
if os.path.exists(_s2):
    for blk in re.split(r'^### ', open(_s2, encoding='utf-8').read(), flags=re.M)[1:]:
        mk_ = re.search(r'kalıp: (.*?) \| mod', blk)
        if mk_: KAL[blk.split('\n', 1)[0].strip()] = mk_.group(1).split()
# ── (1) MEDDE_FARK_KELIMESI ──
for k_, tl, x in re.findall(r"say\('(say %d:\d+ \d+-\d+)', \"([^\"]+)\"(?:, True)?\) \+ \" \(--medde \d+ ayet: '((?:[^']|'(?=[%s']))+)' yazım farkı" % (S, HRF), SRC):
    t1, t2 = KAL.get(k_), KAL.get(k_ + ' --medde')
    w = tl.split()
    if not t1 or not t2 or len(t1) != len(t2) or len(w) != len(t1): continue
    EN['medde'] += 1
    fark = [w[i] for i in range(len(w)) if t1[i] != t2[i]]
    if fark and x not in fark: H.append("(1) %s '%s' medde notu '%s' diyor — kalıp satırlarında ayrışan kelime %s" % (k_.split()[1].split(':')[0] + ':' + k_.split()[1].split(':')[1], k_, x, ', '.join("'%s'" % f for f in fark)))
# ── (2) MEDDE_NOTU_KARSILIKLI ──
ONM = {}
for n in onc: ONM.update(_metin(n))
for d, ad in DIZ:
    md = re.match(r'dizi %d (\d+) (\d+) (\d+)$' % S, d)
    a_ = int(md.group(1)); k_ = 'say %d:%d %s-%s' % (S, a_, md.group(2), md.group(3))
    if k_ not in S2 or _top(S2[k_]) != 1 or "say('%s'" % k_ not in SRC: continue
    for e in sorted(BAS.get(d, ())):
        ms = re.match(r'%d:(\d+)$' % S, e)
        if ms and int(ms.group(1)) in ONM and '--medde' in ONM[int(ms.group(1))].split('\n')[0]:
            EN['karsilikli'] += 1
            if 'yazım farkı' not in M[a_].split('\n')[0]: H.append("(2) %d:%d '%s' korpusta 1 — '%s' eşi %s medde notu taşıyor; bu ayette 'yazım farkı' notu yok" % (S, a_, k_, d, e))
# ── (3) BOLUM_ICI_EDAT_ETIKET ──
def _etk(mk):
    d = collections.defaultdict(set)
    for a_, L in mk.items():
        for tr_, q_, its in L:
            for x in its:
                m = re.match(r"'((?:[^']|'(?=[%s]))+)' \d+\. kelimede (.*)$" % HRF, x)
                if not m: continue
                for t_ in re.findall(r'morph ([A-Z]+)', x):
                    d[(m.group(1), t_)].add(re.sub(r" ile$", '', re.sub(r' \(.*$', '', m.group(2)).strip()).strip("'").lower())
    return d
if onc and bie:
    ET = _etk(MK)
    for n in onc:
        for k_, v_ in _etk(_veri(n)).items(): ET[k_] |= v_
    for bs, ic in re.findall(r"(?:^|[;:] )'([a-zâîûçğışöü']+?)' \(([A-Z]+: [^()]*)\) — çakışma", bie):
        for grp in ic.split('; '):
            mg = re.match(r'([A-Z]+): (.*)$', grp)
            if not mg: continue
            for kr in mg.group(2).split(' / '):
                EN['etiket'] += 1
                if kr.strip().strip("'").lower() not in ET.get((bs, mg.group(1)), set()): H.append("(3) bölüm içi eş edat '%s' %s altında %s — bölüm kesim notlarında bu etiketle yok" % (bs, mg.group(1), kr.strip()))
# ── (4) NAKARAT3_HAM_KALIP ──
def _nak(m_, o_, a0):
    out = {}
    for i_, a_ in enumerate(sorted(m_)):
        if i_ >= len(o_): break
        ham = re.findall(r"`nakarat3` '([^']+)'", o_[i_])
        ads = re.findall(r"'((?:[^']|'(?=[%s]))+)' süzgeç" % HRF, (re.search(r'Ölçüm nakarat3 kalıbı: (.*?)\. ', m_[a_].split('\n')[0] + ' ') or [None, ''])[1])
        if len(ham) == len(ads):
            for h_, d_ in zip(ham, ads): out.setdefault(d_, set()).add((a_, h_))
    return out
if onc:
    NK = _nak(M, O, A)
    r5m = ' '.join(item('araç tanımı farkları (R5'))
    for n in onc:
        _of = _BK + 'b%02d/olcum.txt' % n
        if not os.path.exists(_of): continue
        o_ = [l for l in open(_of, encoding='utf-8').read().replace('**', '').split('\n\n') if l.strip()]
        for d_, v_ in _nak(_metin(n), o_, 0).items():
            if d_ in NK:
                EN['ham'] += 1
                h1 = {h for a_, h in NK[d_]}; h2 = {h for a_, h in v_}
                if not (h1 & h2) and 'ham kalıp farkı' not in r5m: H.append("(4) nakarat3 adı '%s' bölüm içinde farklı ölçüm ham kalıbına verilmiş (%s) — R5 maddesinde 'ham kalıp farkı' kaydı yok" % (d_, ', '.join('%d:%d' % (S, a_) for a_, h in sorted(NK[d_] | v_))))
# ── (5) D3_DISI_EMSAL ──
d3 = ' '.join(item('◈D D3 / bag'))
md3 = re.search(r'ayet başına, betikle\): (.*?) — kalıp başına', d3)
if md3:
    for par in md3.group(1).split('; '):
        mp = re.match(r'(%d:\d+): (.*)$' % S, par)
        if not mp: continue
        EN['d3disi'] += 1
        x = sorted(set(mp.group(2).split(', ')) & EMS)
        if x: H.append("(5) %s D3 dışı listesinde bloğun emsal ayeti %s" % (mp.group(1), ', '.join(x)))

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum39_kurallar hata: %d' % len(H))

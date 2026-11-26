# sûre 7 bölüm 5 kapanış denetimi araç kuralları (bekleyen_ariza_7_b15.txt 2. öğe) — salt okur:
#  (1) BOLUM_BLOK_PLAN: ariza 'bölüm:' maddesindeki 'bölüm blokları' listesi blok_plani'deki bölüm bloklarıyla eş; 'bölüm kapanışı bu blokta' yalnız planın son bloğunda
#  (2) A4_KAPANIS_PLAN: A4 'bölüm kapanışı' yalnız plandaki bölümün son ayetinde; son blokta son ayet A4'ü bu kaydı taşır
#  (3) ALINTI_ONEK_SINIR: 'say S:a i-j' alıntısı, i. kelime 've' / 'fe' önekliyse (VF_YAZI) önekli biçimle başlar
#  (4) A1_EK_GRUP_MORPH: fiilin kendi özne ekinden başka eki yoksa (morph V ile eş şahıslı tek PRON SUFF), kelime A1 'eki' grubunda anılmaz
#  (5) EMSAL_KESIM_ARALIK: emsal karşılık maddesinde bloğun Türkçe kesimi, kalıp aralığı dışındaki kelimenin ad karşılığını taşımaz
# (elle: BAG_ARALIK_GEREKCE, FAIL_REL_OLCUT, CEVAP_CIPA_NO, LENA_EK_ADI)
# kullanım (/home/claude'dan): python3 sunum/bolum41_kurallar.py A B NN
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
# ── plan ──
PLAN = []  # (bölüm adı, [(nn, a, b)])
for l_ in open(Y + 'blok_plani_%d.txt' % S, encoding='utf-8'):
    if l_.startswith('■'): PLAN.append((l_[1:].strip(), []))
    else:
        m_ = re.match(r'\s+(\d+)\. %d:(\d+)-(\d+)' % S, l_)
        if m_ and PLAN: PLAN[-1][1].append((int(m_.group(1)), int(m_.group(2)), int(m_.group(3))))
BL = next((b_ for _, b_ in PLAN if any(x[0] == int(NN) for x in b_)), [])
# ── (1) BOLUM_BLOK_PLAN ──
bi_ = ' '.join(item('bölüm:'))
if BL and bi_:
    m_ = re.search(r'bölüm blokları ([\d, ve]+?)(?:;|$)', bi_)
    EN['plan'] += 1
    if m_:
        ls_ = [int(x) for x in re.findall(r'\d+', m_.group(1))]
        if ls_ != [x[0] for x in BL]: H.append("(1) bölüm maddesi 'bölüm blokları %s' — plan %s" % (m_.group(1).strip(), ', '.join(str(x[0]) for x in BL)))
    if 'bölüm kapanışı bu blokta' in bi_ and int(NN) != BL[-1][0]: H.append("(1) 'bölüm kapanışı bu blokta' — plan bölümün son bloğu %d" % BL[-1][0])
# ── (2) A4_KAPANIS_PLAN ──
if BL:
    son_ = BL[-1][2]
    for a in range(A, B + 1):
        a4 = satir(a, '◈A').split(' A4 ', 1)[-1]
        EN['a4'] += 1
        if 'bölüm kapanışı' in a4 and a != son_: H.append("(2) %d:%d A4 'bölüm kapanışı' — plan bölüm son ayeti %d:%d" % (S, a, S, son_))
        if a == son_ and 'bölüm kapanışı' not in a4: H.append("(2) %d:%d plan bölüm son ayeti — A4'te 'bölüm kapanışı' yok" % (S, a))
# ── (3) ALINTI_ONEK_SINIR ──
_af = _BK + 'b%s/yap/ariza_yap.py' % NN
VF = {}
if os.path.exists(_af):
    m_ = re.search(r'VF_YAZI = (\{.*?\})\n', open(_af, encoding='utf-8').read())
    if m_: VF = ast.literal_eval(m_.group(1))
for a_, i_, q_ in re.findall(r"say\('say %d:(\d+) (\d+)-\d+', \"([^\"]+)\"" % S, SRC):
    w_ = VF.get(int(a_), {}).get(int(i_))
    if not w_: continue
    EN['onek'] += 1
    if not q_.startswith(w_.strip("'")): H.append("(3) %d:%s 'say %d:%s %s-…' alıntısı '%s' — %s. kelime önekli %s" % (S, a_, S, a_, i_, q_[:30], i_, w_))
# ── (4) A1_EK_GRUP_MORPH ──
for a in range(A, B + 1):
    a1 = satir(a, '◈A').split(' A1 ', 1)[-1].split('; A2 ', 1)[0]
    for g_ in re.finditer(r"((?:konuşan |muhatap )?(\d[MF]?[SPD])) eki \(([^()]*)\)", a1):
        p_ = g_.group(2); ic = g_.group(3)
        qs = re.findall(r"'((?:[^']|'(?=[%s]))+)'" % HRF, ic.split(' — ')[0] if ' — ' in ic else ic)
        mn = re.search(r'— ([\d., ve]+) kelime', ic) or re.search(r', (\d+)\. kelime$', ic)
        if not mn: continue
        ns = [int(x) for x in re.findall(r'\d+', mn.group(1))]
        if ' — ' not in ic: qs = qs[:1]
        if len(qs) != len(ns): continue
        for q_, n_ in zip(qs, ns):
            t_ = MOR[a].get(n_, '')
            vm = re.search(r'(?:^|\+ )V\|[^+]*?\|(\d[MF]?[SPD])\b', t_)
            if not vm: continue
            EN['ek'] += 1
            if vm.group(1) == p_ and len(re.findall(r'PRON\|SUFF\|%s\b' % p_, t_)) == 1: H.append("(4) %d:%d '%s' (%d. kelime) %s eki grubunda — morph yalnız fiilin özne eki" % (S, a, q_, n_, p_))
# ── (5) EMSAL_KESIM_ARALIK ──
KAL = {}
for a_, i_, j_, q_ in re.findall(r"say\('say %d:(\d+) (\d+)-(\d+)', \"([^\"]+)\"" % S, SRC): KAL.setdefault(q_, (int(a_), int(i_), int(j_)))
em_ = ' '.join(item('meal (okuma'))
for k_, a_, tr_ in re.findall(r"(?:^|[:;] )'((?:[^']|'(?=[%s]))+)' %d:(\d+) '((?:[^']|'(?=[%s]))+)' / " % (HRF, S, HRF), em_):
    r_ = KAL.get(k_)
    if not r_ or r_[0] != int(a_): continue
    EN['emsal'] += 1
    KS_ = []
    for tr0, ar0, its in MK.get(int(a_), []):
        for x in its:
            m_ = re.match(r"'([^'-][^']*[^'-])' '(?:[^']|'(?=[%s]))+' (?:karşılığı|açılımı) \((\d+)\. kelime" % HRF, x)
            if m_ and len(m_.group(1)) >= 4: KS_.append((m_.group(1).lower(), int(m_.group(2))))
    ic_ = {k for k, w in KS_ if r_[1] <= w <= r_[2]}
    for k0, w_ in KS_:
        if True:
            if r_[1] <= w_ <= r_[2] or k0 in ic_: continue
            if k0 in tr_.lower(): H.append("(5) %d:%s emsal kesimi '%s' — kalıp aralığı %d-%d dışındaki %d. kelimenin karşılığı '%s'" % (S, a_, tr_[:40], r_[1], r_[2], w_, k0))

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum41_kurallar hata: %d' % len(H))

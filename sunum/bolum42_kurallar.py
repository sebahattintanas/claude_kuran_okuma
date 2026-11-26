# sûre 7 bölüm 6 kapanış denetimi araç kuralları (bekleyen_ariza_7_b17.txt 2. öğe) — salt okur:
#  (1) ZAMIR_SEG_CAPA: meal maddesinin ana kısmında (alt bölümlerden — 'blok içi eş edat', es_lemma, emsal, kip notu — önce) bloktaki her ayetin tam bir Türkçe kesim açılışı ('S:a '') var
#  (2) LEM_EDILGEN_ECVEF: PASS etiketsiz fiilde LEM 1. harfi kesralı ve ardından ي ile (سِيقَ türü) ise o kelimeye meal kesiminde '(morph LEM ham biçim)' notu düşülür
#  (3) EMSAL_YAN_KESIM_KAPSAM: emsal karşılık satırında bloğun Türkçe kesimindeki bir sözcük kökü emsal mealinde emsal kesiminin hemen önünde geçiyorsa emsal kesimi onu kapsar
#  (4) A1_GONDERGE_AYET_ICI: A1'de 'gönderge S:a N. kelime' biçimi kaydın kendi ayetini anmaz (ayet içi gönderge tırnaklı alıntıyla)
#  (5) GLOSS_TARANMAYAN_SIFIR: gloss maddesinde 'TARANMAYAN kök taşıyan kelime N' N > 0 ise listelenen her kelime kimliği maddede gerekçeyle ayrıca anılır
# (elle: CIPA_EMSAL_VAR, D1_BEYN_TEMSIL, EMSAL_MEAL_ZAMIR_BUYUK, DIZI_SOL_GENISLEME)
# kullanım (/home/claude'dan): python3 sunum/bolum42_kurallar.py A B NN
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
# ── (1) ZAMIR_SEG_CAPA ──
ana_ = MI.split('; blok içi eş edat', 1)[0]
if MI:
    for a in range(A, B + 1):
        EN['seg'] += 1
        k_ = len(re.findall(r"(?:^|: |; )%d:%d '" % (S, a), ana_))
        if k_ != 1: H.append("(1) %d:%d meal maddesi ana kısmında Türkçe kesim açılışı %d" % (S, a, k_))
# ── (2) LEM_EDILGEN_ECVEF ──
import unicodedata as _ud
for a in range(A, B + 1):
    for w_, f_ in sorted(MOR.get(a, {}).items()):
        if not re.search(r'(?:^|\+ )V\|', f_) or 'PASS' in f_: continue
        m_ = re.search(r'(?:^|\+ )V\|[^+]*?LEM:([^|\s+]+)', f_)
        if not m_: continue
        L_ = _ud.normalize('NFC', m_.group(1))
        if len(L_) >= 3 and L_[1] == 'ِ' and L_[2] == 'ي':
            EN['ecvef'] += 1
            its_ = [x for tr0, ar0, it0 in MK.get(a, []) for x in it0 if re.search(r'\(%d\. kelime' % w_, x) or re.search(r'\b%d\. kelimede' % w_, x)]
            if not any('(morph LEM ham biçim)' in x for x in its_): H.append("(2) %d:%d %d. kelime LEM %s (PASS etiketsiz) — meal kesiminde ham LEM notu yok" % (S, a, w_, L_))
# ── (3) EMSAL_YAN_KESIM_KAPSAM ──
_md = [f_ for f_ in os.listdir(_BK + 'b%s' % NN) if f_.startswith('emsal_%d_' % S) and f_.endswith('.md')] if os.path.isdir(_BK + 'b%s' % NN) else []
EMM = {}
for f_ in _md:
    for blk_ in re.split(r'^\*\*', open(_BK + 'b%s/%s' % (NN, f_), encoding='utf-8').read(), flags=re.M)[1:]:
        k_ = blk_.split('**', 1)[0].strip()
        ls_ = [l for l in blk_.split('\n')[1:] if l.strip() and not l.startswith('##')]
        if ls_: EMM[k_] = ls_[-1]
for a_, tr_, e_, ek_ in re.findall(r"(?:^|[:;] )'(?:[^']|'(?=[%s]))+' %d:(\d+) '((?:[^']|'(?=[%s]))+)' / (\d+:\d+) '((?:[^']|'(?=[%s]))+)' \(emsal metninde\)" % (HRF, S, HRF, HRF), EMI):
    mt_ = EMM.get(e_)
    if not mt_ or ek_ not in mt_: continue
    EN['yan'] += 1
    i_ = mt_.find(ek_); on_ = mt_[max(0, i_ - 20):i_].lower()
    for w_ in re.findall(r"[%s]+" % HRF, tr_):
        st_ = w_[:4].lower()
        if len(w_) >= 4 and st_ in on_ and st_ not in ek_.lower():
            H.append("(3) %d:%s / %s emsal kesimi '%s' — bitişik önceki '%s' kapsanmıyor" % (S, a_, e_, ek_[:30], w_)); break
# ── (4) A1_GONDERGE_AYET_ICI ──
for a in range(A, B + 1):
    a1 = satir(a, '◈A').split(' A1 ', 1)[-1].split('; A2 ', 1)[0]
    for m_ in re.finditer(r'gönderge %d:(\d+) (\d+)\. kelime' % S, a1):
        EN['gonderge'] += 1
        if int(m_.group(1)) == a: H.append("(4) %d:%d A1 'gönderge %d:%d %s. kelime' — ayet içi gönderge" % (S, a, S, a, m_.group(2)))
# ── (5) GLOSS_TARANMAYAN_SIFIR ──
for it in item('gloss kapsam'):
    m_ = re.search(r'TARANMAYAN kök taşıyan kelime (\d+)(?: — ([^·]+))?', it)
    if not m_: continue
    EN['gloss'] += 1
    if int(m_.group(1)) == 0: continue
    for id_ in re.findall(r'\d+:\d+:\d+', m_.group(2) or ''):
        if it.count(id_) < 2: H.append("(5) gloss TARANMAYAN %s — maddede gerekçe yok" % id_)

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum42_kurallar hata: %d' % len(H))

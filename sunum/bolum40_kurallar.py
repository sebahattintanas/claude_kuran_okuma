# sûre 7 bölüm 5 denetimi araç kuralları (bekleyen_ariza_7_b14.txt 2. öğe) — salt okur:
#  (1) BAG_PAREN_ANAHTAR: bag 'kural' alanında anılan 'dizi S a i j' / 'say S:a i-j' anahtarı ◇'de sayım cümlesiyle basılı
#  (2) SOZ_TURU_YAKIN_FIIL: A3 aralığının türü, aralıktan önceki en yakın fiilin köküne göre — قول ise 'söz içi', ندي ise 'söz biçimli içerik'
#  (3) SOZ_ICI_A4_TAM: 'söz biçimli içerik' taşımayan ayette her '(söz içi, N…' aralığı A4'te 'söz açılır (N. kelime)' taşır
#  (4) KIP_SAPMA_SIFATFIIL: kip notunda meal karşılığı sıfat-fiil ('-dik/-tik' iyelikli, '-diğ/-tiğ') ya da '-mekte/-makta' olan fiil, kip sapma notunda kelime biçimiyle anılır
#  (5) AKTOR_ADSIZ_ALAN: ölçüm aktör alanında 'adsız `X`' öğesi olan ayette ◇ satırı 'adsız' kaydını taşır ve 'adlı aktör yok' / 'aktör yok' ile geçiştirmez
# (elle: BAG_ARALIK_GEREKCE, A1_IKI_TOPLULUK, MUHATAP_DEGISIM_ETIKET, ESMA_KURAL_ADI_OK, BICIM_BOS_ALAN)
# kullanım (/home/claude'dan): python3 sunum/bolum40_kurallar.py A B NN
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
MI = (item('meal (okuma') or [''])[0]
KN = MI.split('kip notu (', 1)[1].split('kip sapma notu', 1)[0] if 'kip notu (' in MI else ''
KS = MI.split('kip sapma notu', 1)[1] if 'kip sapma notu' in MI else ''
# ── (1) BAG_PAREN_ANAHTAR ──
_bf = Y + 'bag_%d_%d_%d.txt' % (S, A, B)
if os.path.exists(_bf):
    for b_ in ast.literal_eval('[' + open(_bf, encoding='utf-8').read() + ']'):
        for k_ in re.findall(r"(dizi %d \d+ \d+ \d+|say %d:\d+ \d+-\d+)" % (S, S), b_.get('kural', '') + ' ' + b_.get('not', '')):
            EN['bag'] += 1
            if "say('%s'" % k_ not in SRC: H.append("(1) bag %s — '%s' ◇'de sayım cümlesiyle basılmamış" % (b_['bag'], k_))
# ── (2) SOZ_TURU_YAKIN_FIIL ──
for a in range(A, B + 1):
    a3 = satir(a, '◈A').split(' A3 ', 1)[-1].split(' A4 ', 1)[0]
    for tur, i_ in re.findall(r'\((söz içi|söz biçimli içerik), (\d+)(?:-\d+)?\. kelime', a3):
        i_ = int(i_)
        ws = [w for w in sorted(MOR[a]) if w < i_ and re.search(r'(?:^|\+ )V\|', MOR[a][w])]
        if not ws: continue
        EN['soz'] += 1
        kok = re.search(r'ROOT:([^|\s]+)', MOR[a][ws[-1]])
        kok = kok.group(1) if kok else ''
        if kok == 'قول' and tur != 'söz içi': H.append("(2) %d:%d %d. kelime aralığı '%s' — önceki fiil (%d. kelime) قول kökünden" % (S, a, i_, tur, ws[-1]))
        if kok == 'ندي' and tur == 'söz içi': H.append("(2) %d:%d %d. kelime aralığı 'söz içi' — önceki fiil (%d. kelime) ندي kökünden, 'söz biçimli içerik' olmalı" % (S, a, i_, ws[-1]))
# ── (3) SOZ_ICI_A4_TAM ──
for a in range(A, B + 1):
    l_ = satir(a, '◈A')
    a3 = l_.split(' A3 ', 1)[-1].split(' A4 ', 1)[0]
    a4 = l_.split(' A4 ', 1)[1] if ' A4 ' in l_ else ''
    if 'söz biçimli içerik' in a3: continue
    for i_ in re.findall(r'\(söz içi, (\d+)(?:-\d+)?\. kelime', a3):
        EN['a4'] += 1
        if 'söz açılır (%s. kelime)' % i_ not in a4: H.append("(3) %d:%d %s. kelime söz içi aralığı — A4'te 'söz açılır (%s. kelime)' yok" % (S, a, i_, i_))
# ── (4) KIP_SAPMA_SIFATFIIL ──
for f_, w_ in re.findall(r"'([^\s';]+(?:'[^\s';]+)*)' (?:PERF|IMPF|IMPV)[^;]*? — meal '([^']+)'", KN):
    if re.search(r"[dt][ıiuü](?:ğ|kl[ae]r|k[ıiuü])|m[ae]kt[ae]", w_):
        EN['sifat'] += 1
        if "'%s'" % f_ not in KS: H.append("(4) kip notu '%s' — meal '%s' sıfat-fiil / '-mekte'; kip sapma notunda yok" % (f_, w_))
# ── (5) AKTOR_ADSIZ_ALAN ──
for i_, a in enumerate(range(A, B + 1)):
    if i_ >= len(O) or 'adsız `' not in O[i_]: continue
    EN['adsiz'] += 1
    d_ = M[a].split('\n')[0] if a in M else ''
    if 'adsız `' not in d_ and "aktör adsız" not in d_: H.append("(5) %d:%d ölçüm aktör alanında adsız öğe — ◇'de kayıt yok" % (S, a))

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum40_kurallar hata: %d' % len(H))

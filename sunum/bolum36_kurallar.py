# sûre 7 bölüm 1 denetimi araç kuralları (bekleyen_ariza_7_b02.txt 2. öğe) — salt okur:
#  (1) A4_BASKIN_TIRE: ◈A A4 'şahıs geçişi' ifadesinin ucu '—' olamaz (ölçüm baskını '—' olan ayetle geçiş A4'te yazılmaz, ARIZA A4 maddesinde not düşülür)
#  (2) SEG_KESIM_SAYIM_CUMLESI: her meal kesim aralığının say2 başlığı ◇'de sayım cümlesiyle geçer
#  (3) EMSAL_ALINTI_KALIP_KAPSAMI: emsal karar alıntısı, kalıp aralığındaki edat / zamir kesim notlarının tırnaklı karşılıklarını taşır
#  (4) TARTISMALI_ETIKET_ES: 'tartışmalı' göndergenin uyumsuzluk etiketleri (cins / sayı) A1'de ve gönderge zinciri maddesinde eş küme
#  (5) BOLUM_ICI_ONEK_KARSILIK: morph etiketi eş 'fe' / 've' öneklerinin bölüm içi karşılık farkı 'bölüm içi eş edat' maddesinde anılır
# (elle: A4_KAPALI_LISTE, KIP_SAPMA_EK_FIIL, SAYI_CEVIRI_NOTU, ESMA_DEGIL_GONDERGE_KAYDI, KARSIT_CIFT_IKI_UC, TETIK_DISI_ZAMAN)
# kullanım (/home/claude'dan): python3 sunum/bolum36_kurallar.py A B NN
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
# ── (1) A4_BASKIN_TIRE ──
for a in range(A, B + 1):
    for g in re.findall(r"şahıs geçişi ([^;(]*)", a4(a)):
        EN['a4_gecis'] += 1
        if '—' in g: H.append("(1) %d:%d A4 şahıs geçişi '%s' — ucu '—' (ölçüm baskını olmayan ayet); A4'te yazılmaz" % (S, a, g.strip()))
# ── (2) SEG_KESIM_SAYIM_CUMLESI ──
for a in range(A, B + 1):
    for tr, q, its in MK.get(a, []):
        r = _ar(its)
        if not r: continue
        key = 'say %d:%d %d-%d' % (S, a, r[0], r[1])
        if key not in S2 and key + ' --on' not in S2: continue
        EN['seg_sayim'] += 1
        if "say('%s'" % key not in SRC and "say('%s --on'" % key not in SRC: H.append("(2) %d:%d %d-%d. kelime kesimi ('%s') — '%s' ◇'de sayım cümlesiyle geçmiyor" % (S, a, r[0], r[1], q, key))
# ── (3) EMSAL_ALINTI_KALIP_KAPSAMI ──
LAB = {}
for kk_, ad_ in re.findall(r"say\('(say %d:\d+ \d+-\d+)(?: --on)?', \"([^\"]+)\"" % S, SRC): LAB.setdefault(ad_, kk_)
for it in item('meal (okuma'):
    for kal, a, tr, e in re.findall(r"'((?:[^']|'(?=[%s]))+)' %d:(\d+) '((?:[^']|'(?=[%s]))+)' / (\d+:\d+) '" % (HRF, S, HRF), it):
        kal = re.split(r"(?:; |: |, )'", kal)[-1]
        if kal not in LAB: continue
        i_, j_ = map(int, LAB[kal].split(' ')[2].split('-'))
        EN['emsal_kalip'] += 1
        for tr_, q_, its in MK.get(int(a), []):
            for x in its:
                m = re.match(r"'(?:[^']|'(?=[%s]))+' (\d+)\. kelimede '([%s][^']*)' ile" % (HRF, HRF), x)
                if m and i_ <= int(m.group(1)) <= j_ and m.group(2).lower() not in tr.lower() and m.group(2) not in tr:
                    H.append("(3) '%s' %d:%s / %s alıntısı '%s' — %s. kelime karşılığı '%s' alıntıda yok" % (kal, S, a, e, tr, m.group(1), m.group(2)))
# ── (4) TARTISMALI_ETIKET_ES ──
def _uy(t): return {x for x in ('cins', 'sayı') if 'uyum' in t and x in t}
ZIN = ' '.join(m for m in ITEMS if re.match(r'%d:%d-%d gönderge zinciri' % (S, A, B), m))
for a in range(A, B + 1):
    a1 = satir(a, '◈A').split(' A2 ')[0]
    for w, par in re.findall(r"'((?:[^']|'(?=[%s]))+)' \w+(?: eki)? \(([^()]*tartışmalı[^()]*)\)" % HRF, a1):
        w = re.split(r"(?:; |: |, )'", w)[-1]
        EN['tartismali'] += 1
        sg = [s_ for s_ in re.split(r'; ', ZIN) if "'%s'" % w in s_ and ('%d:%d ' % (S, a) in s_ or True)]
        zu = set().union(*[_uy(s_) for s_ in sg]) if sg else set()
        if sg and zu != _uy(par): H.append("(4) %d:%d '%s' tartışmalı gönderge — A1 uyumsuzluk etiketi %s / gönderge zinciri %s" % (S, a, w, sorted(_uy(par)) or '—', sorted(zu) or '—'))
# ── (5) BOLUM_ICI_ONEK_KARSILIK ──
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
def _onek(nn):
    f_ = _BK + 'b%02d/yap/veri.py' % nn
    d = {}
    if not os.path.exists(f_): return d
    sp_ = _iu.spec_from_file_location('veri%d' % nn, f_); v_ = _iu.module_from_spec(sp_); sp_.loader.exec_module(v_)
    for a_, L in v_.MK.items():
        for tr_, q_, its in L:
            for x in its:
                m = re.match(r"'(fe|ve)' \d+\. kelimede (.*?) \((?:[^()]*; )?morph (\w+)", x)
                if m: d.setdefault((m.group(1), m.group(3)), set()).add(m.group(2).strip())
    return d
onc = [n for n in BOLB if n < int(NN)]
if onc:
    bu = _onek(int(NN)); es = {}
    for n in onc:
        for k_, v_ in _onek(n).items(): es.setdefault(k_, set()).update(v_)
    bie = ' '.join(m.split('bölüm içi eş edat', 1)[1] for m in ITEMS if 'bölüm içi eş edat' in m)
    for k_ in sorted(set(bu) & set(es)):
        EN['onek'] += 1
        if (bu[k_] - es[k_]) and (es[k_] - bu[k_]) and not re.search(r"'%s' \(" % k_[0], bie): H.append("(5) '%s' (%s) bölüm içi karşılık farkı: bu blok %s / önceki %s — 'bölüm içi eş edat' maddesinde anılmamış" % (k_[0], k_[1], sorted(bu[k_]), sorted(es[k_])))

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum36_kurallar hata: %d' % len(H))

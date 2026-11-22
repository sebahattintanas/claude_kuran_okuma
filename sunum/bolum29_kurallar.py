# sûre 6 bölüm 13 denetimi araç kuralları (bekleyen_ariza_6_b26.txt 2. öğe) — salt okur:
#  (1) A4_KAPALI_LISTE: ◈A A4 alanında 'X → cevap' alt maddesi yalnız kapalı listedeki 'şart → cevap' ya da 'soru → cevap' ile kurulur
#  (2) TETIK_MADDE_KELIME: ◇ ◈K / ◈B satırındaki her alıntı (kelime numarasıyla) ARIZA ◈ tetik maddesinde anılır
#  (3) GONDERGE_MORPH_UYUM: A1'de zamirin cinsiyeti göndergenin morph cinsiyetiyle ya da tekil eril zamir çoğul göndergeyle uyuşmuyorsa parantez 'uyumsuz' notu taşır
#  (4) SEG_KARSILIK_YUZEY: seg.py'de fiil olmayan "'X' 'Y' karşılığı" öğesindeki X (ya da ünlü düşmüş / yumuşamış gövdesi) kesimin meal metninde geçer; 'içinde' / 'ile' notundaki meal sözcüğü X gövdesiyle başlamalı
#  (5) ESMA_MUHUR_PAREN_ES: ◇'deki "esma_kayit … uyuşmuyor, araç tanımı farkı (P)" parantezi muhur_el değeriyle açılır (sûre 6'da blok 23'e dek kullanılan biçim; ARIZA esma_kayit maddesiyle eş)
# (elle: GONDERGE_ZINCIR_SON, ZAMIR_ONCUL_KISI, TETIK_ANLAM_NOTU, EDAT_KARSILIK_YON, ACILIM_ZIT_FIIL, ESMA_PAREN_BIR, EMSAL_KALIP_TAM)
# kullanım (/home/claude'dan): python3 sunum/bolum29_kurallar.py A B NN
import sys as _sy; _sy.path.insert(0, '/home/claude/sunum'); from sure import BK as _BK, S
import re, sys, ast, os, subprocess, collections, glob
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
Y = '/home/claude/yamalar/'
H = []
TUM = ast.literal_eval('{' + open(Y + 'ariza_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read() + '}')[(A, B)]
ITEMS = [m for m in TUM if not re.match(r'(bölüm (denetimi \(|\d+ denetiminden)|devir \()', m)]
M, MEAL = {}, {}
exec(open(Y + 'metin_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read(), {'M': M, 'MEAL': MEAL})
EN = collections.Counter()
Q = r"'((?:[^']|(?<=[A-Za-zâîûçğışöüÂÎÛ])'(?=[a-zâîûçğışöü]))+)'"
def item(bas): return [m for m in ITEMS if m.startswith(bas)]
def satir(n, bas):
    for l in M[n].split('\n'):
        if l.startswith(bas): return l
    return ''
def dia(n):
    l = M[n].split('\n')[0]
    return l.split("◇ '", 1)[1].split("' — ", 1)[0] if "◇ '" in l else ''
MOR = collections.defaultdict(dict)
_mf = _BK + 'b%s/morph.txt' % NN
if os.path.exists(_mf):
    for l in open(_mf, encoding='utf-8'):
        p = l.rstrip('\n').split('\t')
        if len(p) >= 3:
            s_, a_, w_ = p[0].split(':')[:3]
            if int(s_) == S: MOR[int(a_)][int(w_)] = p[2]

import json, unicodedata as _ud
O = [l for l in open(_BK + 'b%s/olcum.txt' % NN, encoding='utf-8').read().split('\n\n') if l.strip()] if os.path.exists(_BK + 'b%s/olcum.txt' % NN) else []

def tlow(s): return s.replace('I', 'ı').replace('İ', 'i').lower()
# ── (1) A4_KAPALI_LISTE ──
for a in range(A, B + 1):
    l = satir(a, '◈A')
    if ' A4 ' not in l: continue
    a4 = l.split(' A4 ', 1)[1]
    for m in re.finditer(r'(?:^|; )([^;()]+?) → cevap', a4):
        EN['a4_cevap'] += 1
        if m.group(1).strip() not in ('şart', 'soru'): H.append("(1) %d:%d A4 '%s → cevap' kapalı listede yok" % (S, a, m.group(1).strip()))
# ── (2) TETIK_MADDE_KELIME ──
tm = ' '.join(item('◈ tetik'))
for a in range(A, B + 1):
    for bas in ('◈K', '◈B'):
        l = satir(a, bas)
        for q, w in re.findall(Q + r" \((\d+)\. kelime", l):
            EN['tetik_kelime'] += 1
            if "'%s' %s. kelime" % (q, w) not in tm: H.append("(2) %d:%d %s '%s' (%s. kelime) ARIZA ◈ tetik maddesinde anılmamış" % (S, a, bas, q, w))
# ── (3) GONDERGE_MORPH_UYUM ──
def gn(ft):
    for seg in ft.split(' + '):
        if 'PREF' in seg or 'SUFF' in seg: continue
        m = re.search(r'\|\d?([MF])([SDP])?(?:\||$)', seg)
        if m: return m.group(1), m.group(2) or ''
    return None
for a in range(A, B + 1):
    a1 = satir(a, '◈A').split('; aktör', 1)[0]
    for m in re.finditer(r"\d([MF])([SDP])(?: eki)? \((adsız; [^()]*?gönderge (?:" + Q + r" |(\d+):(\d+) )(\d+)\. kelime[^()]*)\)", a1):
        zg, zs, par = m.group(1), m.group(2), m.group(3)
        ga = int(m.group(6)) if m.group(6) else a
        ft = MOR.get(ga, {}).get(int(m.group(7)), '')
        g = gn(ft)
        if not g: continue
        EN['gonderge'] += 1
        uy = (g[0] != zg and not (zg == 'F' and zs == 'S' and g[1] == 'P')) or (zg == 'M' and zs == 'S' and g[1] == 'P')
        if uy and 'uyumsuz' not in par: H.append("(3) %d:%d %s%s zamir / gönderge %d:%d %d. kelime morph %s%s — parantezde 'uyumsuz' notu yok" % (S, a, zg, zs, S, ga, int(m.group(7)), g[0], g[1]))
# ── (4) SEG_KARSILIK_YUZEY ──
def varyant(X):
    v = {X, X[:-1]}
    m = re.match(r'^(.*)[aeıioöuü]([^aeıioöuü])$', X)
    if m: v.add(m.group(1) + m.group(2))
    return {x for x in v if len(x) >= 2}
_sp = _BK + 'b%s/yap/seg.py' % NN
if os.path.exists(_sp):
    _g = {}
    try: exec(open(_sp, encoding='utf-8').read(), _g)
    except Exception: _g = {}
    for n, segs in sorted(_g.get('SEG', {}).items()):
        if not (A <= n <= B): continue
        for tr, ar, its in segs:
            for x in its:
                m = re.match(r"'([^'\-]+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' karşılığı(.*)$", x)
                if not m or 'karşılıksız' in x: continue
                X, T_ = tlow(m.group(1)), tlow(tr)
                EN['seg_karsilik'] += 1
                if any(v in T_ for v in varyant(X)): continue
                W = [tlow(w) for w in re.findall(r"'([^']+)'", m.group(2))]
                if any(w in T_ and any(w.startswith(v) for v in varyant(X)) for w in W): continue
                H.append("(4) %d:%d '%s' karşılığı kesim mealinde yok: '%s'" % (S, n, m.group(1), tr[:60]))
# ── (5) ESMA_MUHUR_PAREN_ES ──
for a in range(A, B + 1):
    for m in re.finditer(r"esma_kayit çıktısı '[^']*' — [^;]*?uyuşmuyor, araç tanımı farkı \(([^()]*)\)", M.get(a, '')):
        EN['muhur_paren'] += 1
        if not m.group(1).startswith('muhur_el '): H.append("(5) %d:%d ◇ mühür farkı parantezi '%s' muhur_el değerini taşımıyor" % (S, a, m.group(1)[:60]))

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum29_kurallar hata: %d' % len(H))

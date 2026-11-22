# sûre 6 bölüm 14 denetimi araç kuralları (bekleyen_ariza_6_b28.txt 2. öğe) — salt okur:
#  (1) AYN_KELIME_ICI: seg.py "'X' 'Y' karşılığı / açılımı (N. kelime" öğesinde N. kelimenin morph biçimi ع taşıyorsa Y adı ayın işareti (') taşır
#  (2) ILGI_AID_GONDERGE: A1'de harf-i cerle birleşik zamirin ('ileyhi' gibi) göndergesiyle zamir arasında başka bir morph REL varsa kayıt en yakın REL'e bağlanır ya da 'tartışmalı' taşır
#  (3) EMSAL_ES_ALT_DIZE: seg.py'de "S:A emsal mealiyle eş" diyen kesimin Türkçe metni, noktalama ve büyük harf normalleştirilince emsal dosyasındaki mealin alt dizesidir
#  (4) CONJ_HAL_SAPMA: morph CONJ 've' öğesi 'Oysa' / 'iken' / 'hâlbuki' ile karşılanmışsa öğe 'sapma' notu taşır
#  (5) ESMA_CIFT_ARIZA: ◇'de "mühür EVET (ÇİFT)" geçen ayette ARIZA esma_kayit maddesi 'ÇİFT' anar
# (elle: AMAC_FIIL_FAILI, KONUSAN_AYRIMI, KARSI_ADAY_ADLANDIR, EDIM_ZIT_CIFTI, EMSAL_FARK_TAM, ESMA_PAREN_ONCEKI)
# kullanım (/home/claude'dan): python3 sunum/bolum30_kurallar.py A B NN
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


import glob as _gl
_sp = _BK + 'b%s/yap/seg.py' % NN
SEG = {}
if os.path.exists(_sp):
    _g = {}
    try: exec(open(_sp, encoding='utf-8').read(), _g)
    except Exception: _g = {}
    SEG = _g.get('SEG', {})
# ── (1) AYN_KELIME_ICI ──
FORM = collections.defaultdict(dict)
if os.path.exists(_mf):
    for l in open(_mf, encoding='utf-8'):
        p = l.rstrip('\n').split('\t')
        if len(p) >= 2:
            s_, a_, w_ = p[0].split(':')[:3]
            if int(s_) == S: FORM[int(a_)][int(w_)] = p[1]
for n, segs in sorted(SEG.items()):
    if not (A <= n <= B): continue
    for tr, ar, its in segs:
        for x in its:
            m = re.match(r"'[^']+' '((?:[^']|'(?=[a-zâîûçğışöü']))+)' (?:karşılığı|açılımı) \((\d+)\. kelime", x)
            if not m: continue
            ad, w = m.group(1), int(m.group(2))
            if 'ع' not in FORM.get(n, {}).get(w, ''): continue
            EN['ayn'] += 1
            if "'" not in ad: H.append("(1) %d:%d %d. kelime ayınlı, ad '%s' ayın işareti taşımıyor" % (S, n, w, ad))
# ── (2) ILGI_AID_GONDERGE ──
for a in range(A, B + 1):
    a1 = satir(a, '◈A').split('; aktör', 1)[0]
    for m in re.finditer(r"\((adsız; ([^()]*?)gönderge " + Q + r" (\d+)\. kelime, (\d+)\. kelime)\)", a1):
        par, g, z = m.group(1), int(m.group(4)), int(m.group(5))
        ft = MOR.get(a, {}).get(z, '')
        if not ft.startswith('P|P'): continue
        EN['ilgi_aid'] += 1
        ara = [w for w in range(min(g, z) + 1, max(g, z)) if 'N|REL' in MOR.get(a, {}).get(w, '')]
        if ara and 'tartışmalı' not in par: H.append("(2) %d:%d %d. kelime zamiri gönderge %d. kelime — arada REL %s, kayıt en yakın REL'e bağlanmalı ya da 'tartışmalı'" % (S, a, z, g, ', '.join('%d.' % w for w in ara)))
# ── (3) EMSAL_ES_ALT_DIZE ──
def norm(t): return re.sub(r'\s+', ' ', re.sub(r"[^\w' ]", ' ', t.replace('I', 'ı').replace('İ', 'i').lower())).strip()
EMM = {}
for f in _gl.glob(_BK + 'b%s/emsal_%d_*.md' % (NN, S)):
    for blk in open(f, encoding='utf-8').read().split('**')[1:]:
        pass
    t = open(f, encoding='utf-8').read()
    for mm in re.finditer(r'\*\*(\d+:\d+)\*\*\n\n## [^\n]*\n\n([^\n]+)', t): EMM[mm.group(1)] = norm(mm.group(2))
for n, segs in sorted(SEG.items()):
    if not (A <= n <= B): continue
    for tr, ar, its in segs:
        for x in its:
            for e in re.findall(r'(\d+:\d+) emsal mealiyle eş', x):
                EN['emsal_es'] += 1
                if e in EMM and norm(tr) not in EMM[e]: H.append("(3) %d:%d kesim '%s' %s emsal mealinin alt dizesi değil" % (S, n, tr[:50], e))
# ── (4) CONJ_HAL_SAPMA ──
for n, segs in sorted(SEG.items()):
    if not (A <= n <= B): continue
    for tr, ar, its in segs:
        for x in its:
            m = re.match(r"'ve' (\d+)\. kelimede '(Oysa|oysa|iken|hâlbuki|Hâlbuki)' ile", x)
            if not m or 'CONJ' not in x: continue
            EN['conj_hal'] += 1
            if 'sapma' not in x: H.append("(4) %d:%d %s. kelime CONJ 've' '%s' ile — 'sapma' notu yok" % (S, n, m.group(1), m.group(2)))
# ── (5) ESMA_CIFT_ARIZA ──
ek = ' '.join(item('esma_kayit'))
for a in range(A, B + 1):
    if 'mühür EVET (ÇİFT)' in M.get(a, '').split('\n')[0]:
        EN['cift'] += 1
        if 'ÇİFT' not in ek: H.append("(5) %d:%d ◇ 'mühür EVET (ÇİFT)' — ARIZA esma_kayit maddesinde 'ÇİFT' yok" % (S, a))

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum30_kurallar hata: %d' % len(H))

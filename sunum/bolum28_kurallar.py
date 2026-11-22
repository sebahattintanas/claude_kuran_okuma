# sûre 6 bölüm 12 denetimi araç kuralları (bekleyen_ariza_6_b24.txt 2. öğe) — salt okur:
#  (1) OLCUM_LISTE_TAM: ◇ / ARIZA "ölçüm 'HAPAKS: …' — satır aynen" alıntısı ölçümdeki HAPAKS alanının bütün virgüllü öğelerini taşır
#  (2) KOK_GLOSS_ES: ARIZA kök tablosu maddesindeki her "KÖK ('karşılık')" çifti kok_turkce.json'daki karşılıkla bayt eş
#  (3) SEG_KARSILIKSIZ_ICINDE: seg.py'de 'karşılıksız' işaretli öğe "'…' içinde" yer gösterimi taşımaz
#  (4) ESMA_ZAMIR_HABER_PRON: 'zamirin haberi' etiketli esma_el kaydının ayetinde kayıttan önce bağımsız morph PRON yoksa parantez 'mahzuf' anar
#  (5) ADAY1041_KOK_TAM: blok içinde birden çok ayette geçen her morph kökü 'aday 1041' maddesinde 'kök X' olarak anılır
# (elle: TARTISMALI_ALTERNATIF, GONDERGE_LAFIZ_SECIMI, ESMA_AYRILIK_CIFT_YON, KARAR_SONRASI_TAZELEME, BOLUM_ICI_ES_SAYIM, MASTAR_VN_ETIKET)
# kullanım (/home/claude'dan): python3 sunum/bolum28_kurallar.py A B NN
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
# ── (1) OLCUM_LISTE_TAM ──
for k, a in enumerate(range(A, B + 1)):
    if k >= len(O): break
    m = re.search(r'HAPAKS: (.*?) — hapaks', O[k])
    if not m: continue
    og = [re.sub(r'\s*\*\(.*?\)\*\s*$', '', x).strip() for x in re.split(r'\)\*, ', m.group(1) + ' ')]
    og = [x.split(' *(')[0].strip() for x in og if x.strip()]
    for kaynak, t in (('◇', M.get(a, '').split('\n')[0]), ('ARIZA', ' '.join(ITEMS))):
        for q in re.findall(r"'(?:\{\{\d+\|)?HAPAKS: ([^'}]*)(?:\}\})?' — satır aynen", t):
            EN['hapaks'] += 1
            eks = [x for x in og if x not in q]
            if eks and (kaynak == '◇' or all(x in og for x in q.replace(',', ' ').split())): H.append("(1) %d:%d %s HAPAKS alıntısında ölçüm öğesi eksik: %s" % (S, a, kaynak, ', '.join(eks)))
# ── (2) KOK_GLOSS_ES ──
KT = {_ud.normalize('NFC', k): v for k, v in json.load(open('/home/claude/calisma/kok_turkce.json', encoding='utf-8')).items()}
for it in item('kök tablosu'):
    for r_, g_ in re.findall(r"([ء-ي]{2,4}) \('(.+?)'\)(?=[,;]| ve |$)", it):
        EN['kok_gloss'] += 1
        v = KT.get(_ud.normalize('NFC', r_))
        if v is not None and v != g_: H.append("(2) kök tablosu %s karşılığı '%s' / kok_turkce '%s'" % (r_, g_[:40], v[:40]))
# ── (3) SEG_KARSILIKSIZ_ICINDE ──
_sp = _BK + 'b%s/yap/seg.py' % NN
if os.path.exists(_sp):
    _g = {}
    try: exec(open(_sp, encoding='utf-8').read(), _g)
    except Exception: _g = {}
    for n, segs in sorted(_g.get('SEG', {}).items()):
        if not (A <= n <= B): continue
        for tr, ar, its in segs:
            for x in its:
                if 'karşılıksız' in x:
                    EN['karsiliksiz'] += 1
                    if re.search(r"'[^']+' içinde", x): H.append("(3) %d:%d karşılıksız öğe yer gösteriyor: %s" % (S, n, x[:70]))
# ── (4) ESMA_ZAMIR_HABER_PRON ──
_ef = Y + 'esma_el_%d_%d_%d.txt' % (S, A, B)
if os.path.exists(_ef):
    for l in open(_ef, encoding='utf-8'):
        m = re.match(r"\s*'%d:(\d+):(\d+)': '\w+',\s*#.* — zamirin haberi → \w+ \((.+)\)\s*$" % S, l)
        if not m: continue
        a_, w_, par = int(m.group(1)), int(m.group(2)), m.group(3)
        EN['zamir_haber'] += 1
        pron = any(re.search(r'N\|PRON\|(?!SUFF)', MOR.get(a_, {}).get(w, '')) for w in range(1, w_))
        if not pron and 'mahzuf' not in par: H.append("(4) %d:%d:%d 'zamirin haberi' — ayette kayıttan önce bağımsız zamir yok, parantezde 'mahzuf' yok" % (S, a_, w_))
# ── (5) ADAY1041_KOK_TAM ──
KA = collections.defaultdict(set)
for a_, ws in MOR.items():
    if A <= a_ <= B:
        for w_, ft in ws.items():
            for r_ in re.findall(r'ROOT:([^|\s+]+)', ft): KA[_ud.normalize('NFC', r_)].add(a_)
a41 = _ud.normalize('NFC', ' '.join(item('aday 1041')))
for r_, ays in sorted(KA.items()):
    if len(ays) < 2: continue
    EN['aday1041'] += 1
    if 'kök %s' % r_ not in a41: H.append("(5) kök %s %s ayetlerinde geçiyor — aday 1041 maddesinde yok" % (r_, ', '.join('%d:%d' % (S, x) for x in sorted(ays))))

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum28_kurallar hata: %d' % len(H))

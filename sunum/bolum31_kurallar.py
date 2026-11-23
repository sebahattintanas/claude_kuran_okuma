# sûre 6 bölüm 15 denetimi araç kuralları (bekleyen_ariza_6_b31.txt 2. öğe) — salt okur:
#  (1) BERABERLIK_SAYI: ◈A A4'te 'beraberlik' geçen ayette ◈D D4 şahıs sayılarından 1., 2. ve 3. şahıs toplamları hesaplanır; en yüksek toplam en az iki şahısta eşit değilse hata
#  (2) EDIM_GECIS_D2: ◈A A4 'edim geçişi X → Y (ayetler arası)' kaydında Y bu ayetin ◈D D2 edimiyle, X önceki ayetin D2 edimiyle (blok içinde) bayt eş
#  (3) EMSAL_KARAR_KATEGORI: ARIZA emsal meal maddesinde iki alıntı yalnız harf büyüklüğü ve noktalamada ayrılıyorsa karar 'çakışma değil' olur
#  (4) NIDA_KAYIT_ESLIGI: morph VOC taşıyan kelime A3 söz aralığı dışındaysa ◈A A4 'nidâ' anar
#  (5) EMSAL_UZUN_DIZI: bag kalıbı 'say S:a i-j' emsali E'yi buluyorsa ve say2'de E'yi bulan daha uzun bir 'dizi S a p q' varsa bag kaydı bu diziyi anar
# (elle: GONDERGE_KAPSAM, A2_FAIL_DIZIMI, ESMA_GEREKCE_KURAL, KIP_SAPMA_NOTU, MUHATAP_DEGISIMI, SOZDIZIM_ROL, RASM_ELIF_ESI)
# kullanım (/home/claude'dan): python3 sunum/bolum31_kurallar.py A B NN
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



def d4say(a):
    d = satir(a, '◈D')
    m = re.search(r'D4 ([^,]*?), sahset', d)
    t = collections.Counter()
    if m:
        for p, k in re.findall(r'([123])[A-Z]* (\d+)', m.group(1)): t[p] += int(k)
    return t
def d2(a):
    m = re.search(r'D2 ([^;]+);', satir(a, '◈D'))
    if not m: return ''
    return ', '.join(x for x in re.split(r',\s*', m.group(1).strip()) if x and re.fullmatch(r'[a-zçğıöşüâîû ]+', x))  # yalnız edim adları (kip etiketleri D2'de virgülle gelebilir)
def a4(a):
    l = satir(a, '◈A')
    return l.split(' A4 ', 1)[1] if ' A4 ' in l else ''
# ── (1) BERABERLIK_SAYI ──
for a in range(A, B + 1):
    if 'beraberlik' not in a4(a): continue
    t = d4say(a)
    if not t: continue
    EN['beraberlik'] += 1
    mx = max(t.values())
    if sum(1 for v in t.values() if v == mx) < 2:
        H.append("(1) %d:%d A4 beraberlik — şahıs toplamları %s, en yüksek %s. şahıs %d" % (S, a, ' · '.join('%s. şahıs %d' % kv for kv in sorted(t.items())), [k for k, v in t.items() if v == mx][0], mx))
# ── (2) EDIM_GECIS_D2 ──
for a in range(A, B + 1):
    m = re.search(r'edim geçişi (.+?) → (.+?) \(ayetler arası\)', a4(a))
    if not m: continue
    EN['edim_gecis'] += 1
    x, y = m.group(1).strip(), m.group(2).strip()
    if d2(a) and y != d2(a): H.append("(2) %d:%d A4 edim geçişi hedefi '%s' / D2 '%s'" % (S, a, y, d2(a)))
    if a - 1 >= A and d2(a - 1) and x != d2(a - 1): H.append("(2) %d:%d A4 edim geçişi kaynağı '%s' / %d:%d D2 '%s'" % (S, a, x, S, a - 1, d2(a - 1)))
# ── (3) EMSAL_KARAR_KATEGORI ──
MI = ' '.join(item('meal (okuma'))
MI = MI.split('emsal meal karşılık farkları', 1)[1] if 'emsal meal karşılık farkları' in MI else ''
def nrm(t): return re.sub(r'\s+', ' ', re.sub(r"[^\w' ]", ' ', t.replace('I', 'ı').replace('İ', 'i').lower())).strip()
for m in re.finditer(Q + r" %d:(\d+) " % S + Q + r" / (\d+:\d+) " + Q + r" \(emsal metninde\) — (çakışma değil|çakışma — tam okuma sonu)", MI):
    kal, n, x, e, y, kar = m.group(1), int(m.group(2)), m.group(3), m.group(4), m.group(5), m.group(6)
    EN['emsal_karar'] += 1
    if x != y and nrm(x) == nrm(y) and kar != 'çakışma değil': H.append("(3) %d:%d / %s '%s' — alıntılar yalnız harf büyüklüğü / noktalamada ayrılıyor, karar 'çakışma değil' olmalı" % (S, n, e, kal))
# ── (4) NIDA_KAYIT_ESLIGI ──
for a in range(A, B + 1):
    l = satir(a, '◈A')
    a3 = l.split(' A3 ', 1)[1].split(' A4 ', 1)[0] if ' A3 ' in l else ''
    ic = set()
    for i_, j_ in re.findall(r'\(söz (?:içi|biçimli içerik), (\d+)-(\d+)\. kelime', a3): ic |= set(range(int(i_), int(j_) + 1))
    for w, ft in sorted(MOR.get(a, {}).items()):
        if '|VOC|' not in ft + '|' or w in ic: continue
        EN['nida'] += 1
        if 'nidâ' not in a4(a): H.append("(4) %d:%d %d. kelime VOC söz aralığı dışında — A4'te 'nidâ' yok" % (S, a, w))
# ── (5) EMSAL_UZUN_DIZI ──
_s2 = _BK + 'b%s/say2.txt' % NN
DZ = {}
if os.path.exists(_s2):
    for blk in re.split(r'^### ', open(_s2, encoding='utf-8').read(), flags=re.M)[1:]:
        h = blk.split('\n', 1)[0].strip()
        m = re.match(r'dizi %d (\d+) (\d+) (\d+)$' % S, h)
        if m:
            ls = blk.split('\n')
            DZ[(int(m.group(1)), int(m.group(2)), int(m.group(3)))] = set(x.strip('†') for x in (ls[2] if len(ls) > 2 else '').split(', '))
try: BAG = open(Y + 'bag_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read()
except FileNotFoundError: BAG = ''
for l in BAG.split('\n'):
    m = re.search(r"'bag': '(\d+:\d+) → %d:(\d+)'.*?'say %d:\d+ (\d+)-(\d+)'" % (S, S), l)
    if not m: continue
    e, a, i_, j_ = m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4))
    EN['emsal_dizi'] += 1
    uz = [k for k, v in DZ.items() if k[0] == a and e in v and k[2] - k[1] > j_ - i_]
    if uz:
        k = max(uz, key=lambda k: k[2] - k[1])
        if 'dizi %d %d %d %d' % (S, k[0], k[1], k[2]) not in l: H.append("(5) %s → %d:%d bag kalıbı %d-%d. kelime — daha uzun ortak dizi 'dizi %d %d %d %d' bag kaydında anılmamış" % (e, S, a, i_, j_, S, k[0], k[1], k[2]))

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum31_kurallar hata: %d' % len(H))

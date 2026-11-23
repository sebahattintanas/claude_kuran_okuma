# sûre 6 bölüm 16 denetimi araç kuralları (bekleyen_ariza_6_b34.txt 2. öğe) — salt okur:
#  (1) OLCUM_ALAN_ALINTI: ölçüm satırında 'sayı işareti …' ya da 'HAPAKS: …' alanı olan ayetin ◇'si alanı "ölçüm '…' — satır aynen" biçiminde taşır, ARIZA ölçüm maddesi alanı anar
#  (2) R5_BICIM_OGESI: R5 satırında nakarat3 sayısı, ◇'deki eş adlı lemma dizisinin sûre içi toplamından (bu + basılmış sûre içi + okunmus_si + henuz_si) farklıysa satırda 'biçim öğesi' geçer
#  (3) DIZI_AD_LEMMA: ◇ lemma dizisi adının öğe sayısı say2 'dizi' başlığındaki lemma demeti sayısıyla eş; ilk demette و / ف yoksa ad 've-' / 'fe-' ile başlamaz
#  (4) MUHATAP_A4: morph'ta ayet içinde 2MS etiketli kelime ile 2MP etiketli kelime birlikte varsa ◈A A4'te 'muhatap' ya da 'hitap' geçer
#  (5) GOZLEM_ARALIK_SAYIM: 'okuma (gözlem)' maddesinde 'S:a i-j. kelime' aralığıyla bir ayete eş / ortak denen her iddiada say2 'say S:a i-j' (ya da --on) listesi o ayeti içerir
# (elle: ESMA_PARANTEZ_BIR, KM_ANAHTAR_YINELENMEZ, TETIK_DISI_KAPSAM, TAKDIR_YUVASI, A1_EK_AYRIMI, GONDERGE_KAPSAM_TANIM, TRANSLIT_ALA, SABLON_KALINTI)
# kullanım (/home/claude'dan): python3 sunum/bolum32_kurallar.py A B NN
import sys as _sy; _sy.path.insert(0, '/home/claude/sunum'); from sure import BK as _BK, S
import re, sys, ast, os, collections
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

# ── (1) OLCUM_ALAN_ALINTI ──
OLCI = ' '.join(item('ölçüm:'))
for k, a in enumerate(range(A, B + 1)):
    if k >= len(O): break
    for alan in re.findall(r'(sayı işareti [^·]+?|HAPAKS: [^·]+?)(?= ·|$)', O[k]):
        alan = alan.strip(); bas = alan.split(' ')[0] + (' işareti' if alan.startswith('sayı') else '')
        EN['olcum_alan'] += 1
        d = M[a].split('\n')[0] if a in M else ''
        if ("ölçüm '%s" % bas) not in d or not re.search(r"ölçüm '%s[^']*(?:'[^' ][^']*)*' — satır aynen" % re.escape(bas), d):
            H.append("(1) %d:%d ölçüm '%s' alanı ◇'de 'satır aynen' alıntısı yok" % (S, a, bas))
        if not re.search(r'%d:%d [^;]*%s' % (S, a, re.escape(bas)), OLCI): H.append("(1) %d:%d ölçüm '%s' alanı ARIZA ölçüm maddesinde anılmamış" % (S, a, bas))

# ── (2) R5_BICIM_OGESI ──
R5I = ' '.join(item('araç tanımı farkları'))
def sic(key):
    d = S2.get(key)
    if not d: return None
    return len(d['bu']) + sum(1 for x in d['basilan'] if x.startswith('%d:' % S)) + d['okunmus_si'] + d['henuz_si']
for m in re.finditer(r"(\d+):(\d+) nakarat3 '((?:[^']|'(?=[a-zâîûçğışöü]))+)' (\d+) \(tür (?:ic|tam)\)([^;]*(?:;(?! %d:\d+ nakarat3)[^;]*)*)" % S, R5I):
    a, ad, nk, rest = int(m.group(2)), m.group(3), int(m.group(4)), m.group(5)
    for key, nm in DIZ:
        if nm != ad or int(key.split()[2]) != a: continue
        ss = sic(key)
        if ss is None: continue
        EN['r5_bicim'] += 1
        if ss != nk and 'biçim öğesi' not in rest: H.append("(2) %d:%d R5 '%s' nakarat3 %d / '%s' sûre içi %d — 'biçim öğesi' notu yok" % (S, a, ad, nk, key, ss))

# ── (3) DIZI_AD_LEMMA ──
def ad_ogeleri(ad): return [t for t in ad.split(' ') if t]
for key, ad in DIZ:
    if key not in LEM: continue
    EN['dizi_ad'] += 1
    dem = LEM[key]; og = ad_ogeleri(ad)
    if len(og) != len(dem): H.append("(3) '%s' adı '%s' öğe %d / lemma demeti %d" % (key, ad, len(og), len(dem)))
    if og and re.match(r'(?:ve|fe)-', og[0]) and not any(x in ('و', 'ف') for x in (dem[0] if dem else ())): H.append("(3) '%s' adı '%s' önekli — ilk lemma demetinde و / ف yok" % (key, ad))

# ── (4) MUHATAP_A4 ──
for a in range(A, B + 1):
    ws = MOR.get(a, {})
    ms = [w for w, ft in ws.items() if re.search(r'\|2MS(?:\||$)', ft)]
    mp = [w for w, ft in ws.items() if re.search(r'\|2MP(?:\||$)', ft)]
    if not ms or not mp: continue
    EN['muhatap'] += 1
    if not re.search(r'muhatap|hitap', a4(a)): H.append("(4) %d:%d 2MS (%d. kelime) ve 2MP (%d. kelime) — A4'te muhatap / hitap kaydı yok" % (S, a, min(ms), min(mp)))

# ── (5) GOZLEM_ARALIK_SAYIM ──
GZ = ' '.join(item('okuma (gözlem)'))
for seg in GZ.split('; '):
    if ' ile ' not in seg or not re.search(r'\beş\b|ortak', seg): continue
    m = re.search(r'(?<![\d:])%d:(\d+)\b' % S, seg); r = re.search(r'(\d+)-(\d+)\. kelime', seg)
    if not m or not r: continue
    a, i_, j_ = int(m.group(1)), int(r.group(1)), int(r.group(2))
    if not A <= a <= B: continue
    ara = seg[r.end():seg.index(' ile ', r.end())] if ' ile ' in seg[r.end():] else ''
    for e in re.findall(r'(?<![\d:])(\d+:\d+)\b', ara):
        if e == '%d:%d' % (S, a): continue
        EN['gozlem'] += 1
        k = 'say %d:%d %d-%d' % (S, a, i_, j_)
        if e not in BAS.get(k, set()) and e not in BAS.get(k + ' --on', set()):
            H.append("(5) %d:%d %d-%d. kelime %s ile eş / ortak denmiş — '%s' listesinde yok" % (S, a, i_, j_, e, k))

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum32_kurallar hata: %d' % len(H))

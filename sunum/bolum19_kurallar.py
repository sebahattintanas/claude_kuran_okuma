# sûre 6 bölüm 3 denetimi araç kuralları (bekleyen_ariza_6_b07.txt 2. öğe) — salt okur:
#  (1) KOMUT_BLOK: ARIZA'da anılan 'komut python3 sunum/X.py …' bağımsız değişkenleri ARIZA'nın bloğuyla eş (A B NN; es_edat NN; sonradan --plan N; ayn_kontrol A B)
#  (2) OZ_DENETIM_SIFIR: öz denetim maddesinde sıfırdan farklı 'hata: N' ya da '→ ?' teslimi durdurur (bayat sonuç: son koşu ardışık iki koşuyla)
#  (3) IZA_CEVAP: kip notunda 'cevabı' geçen ayette A4'te 'şart → cevap' ya da 'kapsam dışı' kaydı
#  (4) KURAL_ATIF: 'sûre 6 bölüm N denetimi kuralı K' atfı var olan kurala gider (bölüm 1 → bolum17, bölüm 2 → bolum18, bölüm 3 → bolum19, bölüm 4 → bolum20, …, bölüm 11 → bolum27)
#  (5) ESMA_LEMMA_BIR: sûre 6 esma_el kayıtlarında bir lemmaya farklı kural etiketi (okunmuş bloklar, bu blok dahil) hata; 'ilahi' kararlı lemmada kapalı listedeki sözdizimi çerçeve etiketleri ayrık olabilir (sûre 6 blok 19); bu bloğun kaydı önceki etiketlerden biriyle eşse lemmanın eski ayrılığı yeniden raporlanmaz (sûre 6 blok 22); 'degil' (esmâ dışı gönderge) / 'ilahi' (çerçeve) ayrılığı esmâ maddesi 'degil' kaydını anıyorsa geçer (sûre 6 blok 24)
#  (elle: FAIL_REL, KASR_TEK, KANE_IMPF, BASKIN_TEK, EMSAL_KAPSAM, ESMA_FARK_AD, ES_EDAT_KARAR, MEDDE_FARK_KARAR, BAG_SAYIM_BASIM)
# kullanım (/home/claude'dan): python3 sunum/bolum19_kurallar.py A B NN
import sys as _sy; _sy.path.insert(0, '/home/claude/sunum'); from sure import BK as _BK, S
import re, sys, ast, collections, os, subprocess, importlib.util as iu
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
Y = '/home/claude/yamalar/'
H = []
TUM = ast.literal_eval('{' + open(Y + 'ariza_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read() + '}')[(A, B)]
ITEMS = [m for m in TUM if not re.match(r'(bölüm (denetimi \(|\d+ denetiminden|\d+ \(sûre)|devir \()', m)]
M, MEAL = {}, {}
exec(open(Y + 'metin_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read(), {'M': M, 'MEAL': MEAL})
def morph(p, filt=None):
    W = collections.defaultdict(lambda: collections.defaultdict(list))
    for l in open(p, encoding='utf-8'):
        if filt and not l.startswith(filt): continue
        loc, f, t, feat = l.rstrip('\n').split('\t'); s_, a_, w_, p_ = map(int, loc.split(':'))
        W[(s_, a_)][w_].append((f, t, feat))
    return W
W = morph(_BK + 'b%s/morph%d.txt' % (NN, S))
O = [l.replace('**', '') for l in open(_BK + 'b%s/olcum.txt' % NN, encoding='utf-8').read().split('\n\n') if l.strip()]
EMS = open(_BK + 'b%s/ems.txt' % NN).read().split() if os.path.exists(_BK + 'b%s/ems.txt' % NN) else []
S2 = open(_BK + 'b%s/say2.txt' % NN, encoding='utf-8').read()
S2K = {b.split('\n', 1)[0].strip(): b for b in S2.split('### ')[1:]}
Q = r"'((?:[^']|(?<=[A-Za-zâîûçğışöüÂÎÛ])'(?=[a-zâîûçğışöü]))+)'"
def satir(n, bas):
    for l in M[n].split('\n'):
        if l.startswith(bas): return l
    return ''
def a_parca(n, k):
    l = satir(n, '◈A'); m = re.search(r'\b%s (.*?)(?:; A%d |$)' % (k, int(k[1]) + 1), l)
    return m.group(1) if m else ''
def item(bas): return [m for m in ITEMS if m.startswith(bas)]
EN = collections.Counter()
EMK = ' '.join(m for m in ITEMS if 'emsal meal karşılık farkları' in m)
KAL = re.findall(r"(?:^|; |\): )" + Q + r" %d:\d+ '" % S, EMK)


import glob, unicodedata as _ud
# ── (1) KOMUT_BLOK ──
for it in ITEMS:
    for m in re.finditer(r"komut 'python3 sunum/(\w+)\.py ([^']*)'", it):
        ad, ar = m.group(1), m.group(2).split(); EN['komut'] += 1
        if ad == 'es_edat':
            if ar[:1] != [NN]: H.append("(1) komut '%s.py %s' — blok %s" % (ad, ' '.join(ar), NN))
        elif ad == 'sonradan':
            if '--plan' in ar and ar[ar.index('--plan') + 1] != str(int(NN)): H.append("(1) komut '%s.py %s' — plan %d" % (ad, ' '.join(ar), int(NN)))
        elif ad == 'ayn_kontrol':
            if ar[:2] != [str(A), str(B)]: H.append("(1) komut '%s.py %s' — %d %d" % (ad, ' '.join(ar), A, B))
        elif len(ar) >= 3 and all(x.isdigit() for x in ar[:3]) and not ad.startswith('es_lemma'):
            if ar[:3] != [str(A), str(B), NN]: H.append("(1) komut '%s.py %s' — %d %d %s" % (ad, ' '.join(ar), A, B, NN))

# ── (2) OZ_DENETIM_SIFIR ──
for it in item('öz denetim'):
    EN['oz'] += 1
    for m in re.finditer(r"sunum/(\w+)\.py [^→;]*→ ([^;]*)", it):
        if m.group(1) == 'bolum19_kurallar': continue  # sûre 6 blok 8: kural kendi bayat sonucunu okursa kilitlenir (öz atıf)
        r = m.group(2)
        if r.strip().startswith('?') or re.search(r'hata: [1-9]', r): H.append("(2) öz denetim %s → %s" % (m.group(1), r.strip()[:60]))

# ── (3) IZA_CEVAP ──
kip = ' '.join(m[m.index('kip notu ('):] for m in ITEMS if 'kip notu (' in m)  # yalnız kip notu bölümü (meal kesimleri dışarıda)
kip = re.split(r'"; meal karşılık|; meal takdir', kip)[0]
for a in range(A, B + 1):
    i = kip.find('%d:%d ' % (S, a))
    if i < 0: continue
    j = min([x for x in (kip.find('%d:%d ' % (S, b), i + 1) for b in range(a + 1, B + 1)) if x > 0] or [len(kip)])
    if 'cevabı' in kip[i:j]:
        EN['iza'] += 1
        a4 = a_parca(a, 'A4')
        if 'şart → cevap' not in a4 and 'kapsam dışı' not in a4: H.append("(3) %d:%d kip notunda 'cevabı' — A4'te şart → cevap kaydı yok" % (S, a))

# ── (4) KURAL_ATIF ──
MAX = {}
for b_, f in ((1, 'bolum17'), (2, 'bolum18'), (3, 'bolum19'), (4, 'bolum20'), (5, 'bolum21'), (6, 'bolum22'), (7, 'bolum23'), (8, 'bolum24'), (9, 'bolum25'), (10, 'bolum26'), (11, 'bolum27'), (12, 'bolum28'), (13, 'bolum29'), (14, 'bolum30')):  # sûre 6 bölüm 4 denetimi: bolum20; bölüm 6 denetimi: bolum22; bölüm 7: bolum23; bölüm 8: bolum24; bölüm 9: bolum25; bölüm 10: bolum26; bölüm 11: bolum27
    try:
        t = open('/home/claude/sunum/%s_kurallar.py' % f, encoding='utf-8').read()
        MAX[b_] = max(int(x) for x in re.findall(r'^#\s+\((\d+)\)', t, re.M))
    except Exception: pass
TXT = '\n'.join(ITEMS) + '\n' + '\n'.join(M.values())
for m in re.finditer(r'sûre %d bölüm (\d+) denetimi(?:nden [A-Z_]+ elle)? kural(?:ı|ları) (\d+)(?:-(\d+))?' % S, TXT):
    b_, k = int(m.group(1)), int(m.group(3) or m.group(2)); EN['atif'] += 1
    if b_ in MAX and k > MAX[b_]: H.append("(4) atıf 'sûre %d bölüm %d denetimi kuralı %s' — bölümün kural sayısı %d" % (S, b_, m.group(2), MAX[b_]))

# ── (5) ESMA_LEMMA_BIR ──
LEMW = {}
for f in sorted(glob.glob(_BK + 'b[0-9][0-9]/morph%d.txt' % S)):
    if int(f.split('/')[-2][1:]) > int(NN): continue
    for l in open(f, encoding='utf-8'):
        loc, fo, t, feat = l.rstrip('\n').split('\t'); s_, a_, w_ = map(int, loc.split(':')[:3])
        mm = re.findall(r'LEM:([^|]+)', feat)
        for x in mm:
            if not re.search(r'^(ال|و|ف|ب|ل|ك)$', x): LEMW.setdefault((a_, w_), _ud.normalize('NFC', x))
ET = collections.defaultdict(set); KD = {}
for l in open('/home/claude/calisma/esma_el.py', encoding='utf-8'):
    m = re.match(r"\s*'%d:(\d+):(\d+)': '(\w+)',\s*#.*? — (.+?) →" % S, l)
    if not m: continue
    a_, w_ = int(m.group(1)), int(m.group(2))
    if (a_, w_) in LEMW: ET[LEMW[(a_, w_)]].add((m.group(4).strip(), '%d:%d:%d' % (S, a_, w_))); KD.setdefault(LEMW[(a_, w_)], set()).add(m.group(3))
# sûre 6 blok 19: 'ilahi' kararlı esmâda kapalı listedeki sözdizimi çerçeve etiketleri (zamirin haberi / 'inne/enne' haberi / lafzın haberi) farklı olabilir — yalnız 'degil' kararlı ya da karar değeri farklı lemma hata
CERCEVE = ("'inne/enne' haberi", 'zamirin haberi', 'lafzın haberi', "'ve kâna'llâhu X' lafzın haberi", "'ve'llâhu X' kuralı", 'tamlama içinde ad, göndergesi Allah')  # sûre 6 blok 30: kullanıcı kararlı tamlama etiketi de 'ilahi' çerçevesi (6:96:12 emsali)
for lem, st in ET.items():
    et = {x[0] for x in st}; EN['esma_lem'] += 1
    if KD.get(lem) == {'ilahi'} and all(e in CERCEVE for e in et): continue  # bölüm 9 denetimi: önek değil tam etiket eşleşmesi
    _dg = [x for e, x in st if e == 'esmâ adı esmâ dışı göndergeyle']; _esm = ' '.join(item('esmâ:'))
    if KD.get(lem) == {'ilahi', 'degil'} and _dg and all(e in CERCEVE or e == 'esmâ adı esmâ dışı göndergeyle' for e in et) and all(x in _esm for x in _dg): continue  # sûre 6 blok 24: karar ayrılığı gönderge ayrılığından ('degil' esmâ dışı / 'ilahi' çerçeve) — bu bloğun esmâ maddesi önceki 'degil' kaydını anıyorsa geçer
    if len(et) > 1 and any(A <= int(x[1].split(':')[1]) <= B for x in st):
        _ic = {e for e, x in st if A <= int(x.split(':')[1]) <= B}; _dis = {e for e, x in st if not (A <= int(x.split(':')[1]) <= B)}
        _ilk = min(((x, e) for e, x in st if not (A <= int(x.split(':')[1]) <= B)), key=lambda z: tuple(int(t) for t in z[0].split(':')), default=(None, None))[1]
        if _dis and len(_ic) == 1 and _ic == {_ilk} and len(KD.get(lem, ())) == 1: continue  # bölüm 11 denetimi: yalnız lemmanın ilk (emsal) etiketiyle eş ve karar değeri tek  # sûre 6 blok 22: bu bloğun kaydı önceki bir etiketle eş — lemmadaki eski ayrılık önceki blokta raporlandı ('evvel' 6:14 / 6:25)
        H.append("(5) esmâ lemma %s farklı kural etiketi: %s" % (lem, '; '.join('%s (%s)' % (e, x) for e, x in sorted(st, key=lambda z: z[1]))))

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum19_kurallar hata: %d' % len(H))

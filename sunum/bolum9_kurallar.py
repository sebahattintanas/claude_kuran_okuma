# bölüm 9 (sûre 5) denetiminden kurallar — betik denetimi:
#  (1) çakışma gerekçesindeki 'bir lemma' / 'morph LEM eşit' ve 'farklı lemma' / 'LEM yazımı farklı' / 'morph LEM farklı' iddiası üyelerin morph LEM kümesiyle
#  (2) KÖK grubu kararında anılan Arapça kökler ⇔ üye biçimlerinin kökleri (eksik / fazla)
#  (3) bağ kuralındaki kalıp ('harekesiz' / 'önek kesilmiş') say2'de, listesi emsal ayetini içerir; 'ölçüm xref' adlı kural ölçüm xref satırında emsali bulur
#  (4) R5 'gerekçe biçim farkı' sunum/r5_gerekce.py çıktısını taşır; harekesiz kalıpta 'hareke' gerekçe olamaz
#  (5) ölçümdeki her nakarat3 kalıbının (GEÇER / GEÇMEZ) R5 satırı var; ◇'deki eş adlı lemma dizisinin sûre içi sayısı nakarat sayısından farklıysa R5 satırı 'biçim öğesi' notu taşır
#  (6) say2 'dizi' listesinde blok içi başka ayet bulunan lemma dizisi ◈D D3 / bag maddesinde 'ayetler arası kalıp' (ayetleriyle) ve her ayetin ◇'sinde sayılı; say2'de çift başlık
#  (7) meal karşılık farkı kararında kalıp başına bir kapalı sonuç ('bilinçli fark' ile 'tam okuma sonu' birlikte isabet)
#  (9) ARIZA başındaki taşınan denetim maddeleri bekleyen_ariza dosyasıyla bayt eşit
#  (10) medde maddesindeki meddeli kalıp sayısı ⇔ say2 '--medde' koşu sayısı ⇔ meddeli / meddesiz çift sayısı
#  (11) ölçümde 'İÇ düğüm' alanı olan her ayetin ◇'si alanı 'satır aynen' anar
# kullanım (/home/claude'dan): python3 sunum/bolum9_kurallar.py A B NN
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from sure import S
import re, sys, ast, glob, subprocess, unicodedata as ud
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
Y = '/home/claude/yamalar/'
H = []
def run(*a): return subprocess.run(list(a), capture_output=True, text=True, cwd='/home/claude').stdout
M = {}; exec(open(Y + 'metin_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read(), {'M': M, 'MEAL': {}})
TUM = ast.literal_eval('{' + open(Y + 'ariza_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read() + '}')[(A, B)]
ITEMS = [m for m in TUM if not re.match(r'bölüm (denetimi \(|\d+ denetiminden)', m)]
def item(bas): return [m for m in ITEMS if m.startswith(bas)]
def dosyalar():
    out = []
    for f in glob.glob(Y + 'ariza_%d_*_*.txt' % S):
        a_, b_ = map(int, re.findall(r'_(\d+)_(\d+)\.txt$', f)[0])
        if b_ <= B: out.append((a_, f))
    return [f for _, f in sorted(out)]
DOS = dosyalar()
# morph (sûre geneli): (a, w) → gövde LEM, kök
LEMW, KOKW = {}, {}
for l in open('/home/claude/calisma/morph.txt', encoding='utf-8'):
    p = l.rstrip('\n').split('\t')
    if len(p) < 4 or p[0].count(':') != 3: continue
    s_, a_, w_, _ = map(int, p[0].split(':'))
    if s_ != S or 'PREF' in p[3] or 'SUFF' in p[3]: continue
    m = re.search(r'LEM:([^|]+)', p[3]); r = re.search(r'ROOT:([^|]+)', p[3])
    if m and (a_, w_) not in LEMW: LEMW[(a_, w_)] = ud.normalize('NFC', m.group(1))
    if r and (a_, w_) not in KOKW: KOKW[(a_, w_)] = r.group(1)
# üye biçimi → (ayet, kelime) — bütün okunmuş ARIZA meal maddelerinden
YER = {}
for f in DOS:
    for m in ast.literal_eval('{' + open(f, encoding='utf-8').read() + '}').popitem()[1]:
        if not m.startswith('meal'): continue
        for seg in re.split(r'; (?=%d:\d+ \')' % S, m):
            ma = re.match(r"(?:meal[^:]*: )?%d:(\d+) " % S, seg)
            if not ma: continue
            a_ = int(ma.group(1))
            for tr, ar, w1, w2 in re.findall(r"'([^']+)' '((?:[^' ]|'(?=[a-zâîûçğışöü])|'(?=' ))+)' (?:karşılığı|açılımı) \((\d+)\. (?:ve (\d+)\. )?kelime", seg):
                YER.setdefault((tr, ar), set()).add((a_, int(w1)))  # karşılık başına: aynı Arapça biçim başka karşılıkla da geçebilir
                if w2: YER[(tr, ar)].add((a_, int(w2)))
CAK = run('python3', '/home/claude/sunum/cakisma.py', *DOS).splitlines()
GRUP = {}
for l in CAK:
    if l.startswith('KÖK '):
        k = 'KÖK ' + l.split()[1]; GRUP[k] = []
        for tr, ls in re.findall(r"(?:^|; )(.+?) (\[[^\]]*\])", l.split(' ← ', 1)[1]):
            GRUP[k] += [(tr, x) for x in ast.literal_eval(ls)]
    elif ' ← ' in l:
        tr, ls = l.split(' ← ', 1); GRUP[tr.strip()] = [(tr.strip(), x) for x in ast.literal_eval(ls)]
cm = ' '.join(item('karşılık çakışması'))
pos = sorted((m.start(), (('KÖK ' + m.group(2) if m.group(1) else m.group(2)))) for m in re.finditer(r"(KÖK )?'([^']+)' ← ", cm))
n1 = n2 = 0
for k, (p, g) in enumerate(pos):
    if g not in GRUP: continue
    parca = cm[p:pos[k + 1][0] if k + 1 < len(pos) else len(cm)]
    yer = set().union(*[YER.get(u, set()) for u in GRUP[g]]) if GRUP[g] else set()
    if not g.startswith('KÖK '):  # (1)
        lem = {LEMW[x] for x in yer if x in LEMW}
        if not lem: continue
        n1 += 1
        if re.search(r"bir lemma|morph LEM eşit", parca) and len(lem) > 1: H.append("(1) '%s' 'bir lemma / LEM eşit' iddiası, morph LEM %d: %s" % (g, len(lem), ' / '.join(sorted(lem))))
        if re.search(r"farklı lemma|LEM yazımı farklı|morph LEM farklı", parca) and len(lem) == 1: H.append("(1) '%s' 'farklı lemma / LEM farklı' iddiası, morph LEM tek: %s" % (g, next(iter(lem))))
    else:  # (2)
        ak = set(re.findall(r'[ء-ي]{3,4}', re.sub(r'\([^()]*morph LEM ham biçim\)', '', parca)))
        if not ak: continue
        n2 += 1
        gk = {KOKW[x] for x in yer if x in KOKW}
        if gk and ak != gk: H.append("(2) %s kök listesi: karar %s / üyeler %s" % (g, ' '.join(sorted(ak)), ' '.join(sorted(gk))))
print('(1) lemma iddiası denetlenen grup: %d; (2) KÖK kök listesi denetlenen grup: %d' % (n1, n2))
# say2
S2 = open('/home/claude/b%s/say2.txt' % NN, encoding='utf-8').read()
BLK = {}
basl = []
for blk in S2.split('### ')[1:]:
    h = blk.split('\n')[0].strip(); basl.append(h); BLK.setdefault(h, blk)
for h in sorted({h for h in basl if basl.count(h) > 1}): H.append("(6) say2 çift başlık: '%s'" % h)
def liste(h):
    m = re.search(r'^liste: (.*)$', BLK.get(h, ''), re.M) or re.search(r'^((?:\d+:\d+†?, )*\d+:\d+†?)$', BLK.get(h, ''), re.M)
    return [x.rstrip('†') for x in m.group(1).split(', ')] if m else []
def sic(h):
    m = re.search(r"\d+ (\{.*\})", BLK.get(h, ''))
    if not m: return None
    d = ast.literal_eval(m.group(1)); return len(d['bu']) + sum(1 for x in d['basilan'] if x.startswith('%d:' % S)) + d['okunmus_si'] + d['henuz_si']
# (3) bağ kuralı kalıbı
def kelime(q):
    n = 0
    for t in q.split():
        if t in ('ve', 'fe', 'fa', 'va', 'yâ'): continue
        parca = re.split(r"(?<=[aeiuâîû])'(?=l-|ll|[a-zçğışöü]-|[bcdfğhklmnqrsştxyz]{2})", t)
        n += 1 + sum(1 for x in parca[:-1] if x not in ('ve', 'fe', 'fa', 'va', 'bi', 'li', 'le', 'ke') and not x.endswith('-'))
    return n
olc = open('/home/claude/b%s/olcum.txt' % NN, encoding='utf-8').read().split('\n\n')
bf = Y + 'bag_%d_%d_%d.txt' % (S, A, B)
BAG = ast.literal_eval('[' + open(bf, encoding='utf-8').read() + ']') if _o.path.exists(bf) else []
for b in BAG:
    em, hd = b['bag'].split(' → '); a = int(hd.split(':')[1])
    m = re.search(r"(harekesiz|önek kesilmiş) '((?:[^']|'(?=[a-zâîûçğışöü]))+)'", b['kural'])
    if m:
        d = re.match(r"◇ '(.*?)' — ", M[a]).group(1); p = d.find(m.group(2))
        if p < 0: H.append('(3) bag %s kalıp ◇ alt dizesi değil' % b['bag']); continue
        on = d[:p]; i = kelime(on.rstrip("'")) + 1 if on.endswith("'") else kelime(on) + 1; j = i + kelime(m.group(2)) - 1
        keys = ['say %d:%d %d-%d' % (S, a, i, j) + (' --on' if m.group(1) == 'önek kesilmiş' else '')]
        keys += [keys[0] + ' --on'] if m.group(1) == 'harekesiz' else []
        ks = [k for k in keys if k in BLK]
        if not ks: H.append("(3) bag %s kalıbının say2 koşusu yok ('%s')" % (b['bag'], keys[0]))
        elif not any(em in liste(k) for k in ks): H.append("(3) bag %s: '%s' listesinde emsal yok — kural ölçüm xref adıyla yazılır" % (b['bag'], ks[0]))
    elif 'ölçüm xref' in b['kural']:
        if not re.search(r'→ [^·|]*\b%s\b' % re.escape(em), olc[a - A]): H.append('(3) bag %s ölçüm xref satırında emsal yok' % b['bag'])
    else: H.append("(3) bag %s kuralı ne kalıp ne ölçüm xref" % b['bag'])
print('(3) bağ: %d' % len(BAG))
# (4) R5 gerekçe
r5 = ' '.join(item('araç tanımı farkları (R5'))
SAT = re.split(r'; (?=%d:\d+ nakarat3 )' % S, r5.split('): ', 1)[-1])
for sat in SAT:
    m = re.search(r"eşit aralıkla lemma dizisi '.+?' \((\d+)-(\d+)\. kelime\)", sat); ma = re.match(r'%d:(\d+) nakarat3' % S, sat)
    if not m or not ma: continue
    g = sat[sat.find('gerekçe'):]
    if 'biçim farkı' in g:
        o = run('python3', '/home/claude/sunum/r5_gerekce.py', str(S), ma.group(1), m.group(1), m.group(2)).strip().split(': ', 1)[-1]
        if o not in g: H.append("(4) R5 %d:%s gerekçe r5_gerekce çıktısını taşımıyor ('%s')" % (S, ma.group(1), o))
    if 'harekesiz' in sat.split(' sûre içi')[0] and 'hareke ' in g: H.append("(4) R5 %d:%s harekesiz kalıpta 'hareke' gerekçesi" % (S, ma.group(1)))
# (5) ölçüm nakarat3 ⇔ R5; ◇ lemma dizisi sayısı
NK = {}
for a in range(A, B + 1):
    NK[a] = [(p_, int(n_), z_) for p_, n_, z_ in re.findall(r"`nakarat3` '([^']+)' \(\d+ kelime / (\d+) ayet, tür ic\) → süzgeç \*\*(GEÇER|GEÇMEZ)\*\*", olc[a - A])]
    r5a = [s_ for s_ in SAT if s_.startswith('%d:%d nakarat3' % (S, a))]
    if len(r5a) != len(NK[a]): H.append('(5) %d:%d ölçüm nakarat3 %d / R5 satırı %d (GEÇMEZ dahil)' % (S, a, len(NK[a]), len(r5a)))
    src = open('/home/claude/b%s/yap/metin_yap.py' % NN, encoding='utf-8').read()
    for s_ in r5a:
        mm = re.match(r"%d:%d nakarat3 '(.+?)' (\d+) \(tür ic\)" % (S, a), s_)
        if not mm: continue
        ad, nk = mm.group(1), int(mm.group(2))
        for key in re.findall(r"say\('(dizi %d %d \d+ \d+)', \"%s\"\)" % (S, a, re.escape(ad)), src):
            ss = sic(key)
            if ss is not None and ss != nk and 'biçim öğesi' not in s_: H.append("(5) %d:%d '%s' nakarat3 %d / ◇ lemma dizisi '%s' sûre içi %d — R5 satırında 'biçim öğesi' notu yok" % (S, a, ad, nk, key, ss))
# (6) blok içi ayetler arası kalıp
d3 = ' '.join(item('◈D D3 / bag'))
for h in BLK:
    mh = re.match(r'dizi %d (\d+) \d+ \d+$' % S, h)
    if not mh: continue
    a = int(mh.group(1)); obur = sorted({int(x.split(':')[1]) for x in liste(h) if x.startswith('%d:' % S) and A <= int(x.split(':')[1]) <= B and int(x.split(':')[1]) != a})
    if not obur: continue
    src = open('/home/claude/b%s/yap/metin_yap.py' % NN, encoding='utf-8').read()
    ad = re.search(r"say\('%s', \"([^\"]+)\"\)" % re.escape(h), src)
    ad = ad.group(1) if ad else '?'
    kay = [m_ for m_ in re.finditer(r"ayetler arası kalıp '((?:[^']|'(?=[a-zâîûçğışöü]))+)' \(([^)]*)\)", d3) if all('%d:%d' % (S, x) in m_.group(2) for x in obur + [a])]
    if not kay: H.append("(6) lemma dizisi '%s' (%s) blok içi %s ile — ◈D D3 / bag maddesinde 'ayetler arası kalıp' kaydı yok" % (ad, h, ', '.join('%d:%d' % (S, x) for x in obur)))
    for x in obur:
        if "lemma dizisi '%s'" % ad not in M[x]: H.append("(6) lemma dizisi '%s' %d:%d ◇'sinde sayılmamış" % (ad, S, x))
# (7) meal karşılık farkı kararları
mk = ' '.join(item('meal karşılık farkı kararları'))
for seg in re.split(r"; (?=')", mk.split('): ', 1)[-1]):
    if 'bilinçli fark' in seg and 'tam okuma sonu' in seg: H.append("(7) meal karşılık farkı kararı iki sonuçlu: %s" % seg[:80])
# (9) taşınan denetim maddeleri bayt eşit
tas = [m for m in TUM if re.match(r'bölüm (denetimi \(|\d+ denetiminden)', m)]
if tas:
    bks = sorted(glob.glob(Y + 'bekleyen_ariza_%d_b*.txt' % S), key=lambda f: int(re.findall(r'_b(\d+)\.txt$', f)[0]))
    bks = [f for f in bks if int(re.findall(r'_b(\d+)\.txt$', f)[0]) < int(NN)]
    BEK = ast.literal_eval('[' + open(bks[-1], encoding='utf-8').read() + ']') if bks else []
    if TUM[:len(BEK)] != BEK: H.append('(9) ARIZA başı %s ile bayt eşit değil' % (_o.path.basename(bks[-1]) if bks else 'bekleyen dosyası'))
# (10) medde
md = ' '.join(m for m in ITEMS if 'medde taraması' in m)
mm = re.search(r'(\d+) meddeli kalıp \(', md)
cift = len(re.findall(r'meddeli \d+ / meddesiz \d+', md)); kos = len([h for h in BLK if h.endswith('--medde')])
if mm and not (int(mm.group(1)) == cift == kos): H.append('(10) medde: meddeli kalıp %s / çift %d / say2 --medde koşusu %d' % (mm.group(1), cift, kos))
# (11) İÇ düğüm
for a in range(A, B + 1):
    mi = re.search(r'İÇ düğüm \d+', olc[a - A])
    if mi and "'%s' — satır aynen" % mi.group(0) not in M[a]: H.append("(11) %d:%d ölçüm '%s' ◇'de satır aynen anılmıyor" % (S, a, mi.group(0)))
for h in H: print('HATA', h)
print('bolum9_kurallar hata:', len(H))

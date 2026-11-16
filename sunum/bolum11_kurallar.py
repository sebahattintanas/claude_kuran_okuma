# bölüm 11 (sûre 5) denetimi araç kuralları (bekleyen_ariza_5_b26.txt 2. öğe) — salt okur:
#  (1) ARIZA 'bölüm:' maddesindeki ad ve ◈A A4 adı blok planındaki ■ başlığıyla bayt eşit
#  (2) A3 kapsamı ('i-j. kelime', 'N. kelimeden … sonuna dek', 'söz sürüyor (…; i-j. kelime)') okunur; kapsamdaki morph REM ARIZA 'söz içi REM' bölümünde; okunamayan A3 hata
#  (6) medde satırı sunum/medde_fark.py çıktısını aynen taşır
#  (7) A1'de esmâ kuralı anılıyorsa esma_el kuralıyla eş
#  (9) ◇ lemma dizisi adında joker '_' yalnız lemmasız öğede (say2 'lemma dizisi' boş demeti)
#  (10) ◇ lafız dizisinde ve D1'de 'nekre' sayısı morph INDEF kelime sayısıyla eş
#  (11) ◇ lafız dizisi adları önceki blokların adlarıyla e / a yazım farkı taşımaz
#  (12) fâsıla maddesinde 'kırıl-' yalnız ölçümde KAFİYE KIRILMASI olan ayette
#  (13) 'önceki karar (blok N: …)' parantezi önceki kararın sonucunu taşır
#  (14) ث'li LEM'in ص'li eşi korpusta varsa ARIZA'da 'ث / ص' notu
#  (15) bu blokta eklenen kök anlamı, blokta başka köke verilmiş meal karşılığını içermez
#  (16) A1'de 'li / bi / min' önekli 'llezîne' alıntısı yok
#  (17) her PASS fiil için A1'de 'faili (adsız' ya da 'naib-i faili'
#  (3, 4, 5, 8, 18: bolum9_kurallar, bolum10_kurallar, lem_bozuk, geriye_donuk içinde)
# kullanım (/home/claude'dan): python3 sunum/bolum11_kurallar.py A B NN
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from sure import S
import re, sys, ast, glob, collections, unicodedata as ud, importlib.util as iu
import medde_fark
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
Y = '/home/claude/yamalar/'
H = []
N_ = lambda x: ud.normalize('NFC', x)
M = {}; exec(open(Y + 'metin_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read(), {'M': M, 'MEAL': {}})
TUM = ast.literal_eval('{' + open(Y + 'ariza_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read() + '}')[(A, B)]
ITEMS = [m for m in TUM if not re.match(r'bölüm (denetimi \(|\d+ denetiminden)', m)]
def item(bas): return [m for m in ITEMS if m.startswith(bas)]
ARZ = ' '.join(ITEMS)
W = collections.defaultdict(lambda: collections.defaultdict(list))
for l in open('/home/claude/b%s/morph%d.txt' % (NN, S), encoding='utf-8'):
    loc, f, t, feat = l.rstrip('\n').split('\t')
    s_, a_, w_, p_ = map(int, loc.split(':'))
    W[a_][w_].append((f, t, feat))
def satir(a, bas):
    for l in M[a].split('\n'):
        if l.startswith(bas): return l
    return ''
def bol(s, sep='; '):
    out, d, cur, i = [], 0, '', 0
    while i < len(s):
        c = s[i]
        d += c == '('; d -= c == ')'
        if d == 0 and s.startswith(sep, i): out.append(cur); cur = ''; i += len(sep); continue
        cur += c; i += 1
    out.append(cur); return out
# ── (1) bölüm adı ──
bas_ = None
for l in open(Y + 'blok_plani_%d.txt' % S, encoding='utf-8'):
    if l.startswith('■'): son_bas = l[1:].strip()
    m = re.match(r'\s*(\d+)\. ', l)
    if m and m.group(1) == str(int(NN)): bas_ = son_bas
if bas_:
    bi = item('bölüm: ')
    if not bi or ("bölüm: '%s' bölümü" % bas_) not in bi[0]: H.append("(1) ARIZA bölüm maddesi adı plan başlığıyla eş değil ('%s')" % bas_)
    for a in range(A, B + 1):
        if ("A4 '%s' bölümünde" % bas_) not in satir(a, '◈A'): H.append('(1) %d:%d A4 bölüm adı plan başlığıyla eş değil' % (S, a))
# ── (2) A3 kapsamı ve söz içi REM ──
sz = ' '.join(item('söz / tırnak'))
for a in range(A, B + 1):
    sa = satir(a, '◈A'); m = re.search(r'; A3 (.*?); A4 ', sa)
    a3 = m.group(1) if m else '—'
    if a3.strip() == '—': continue
    nw = max(W[a]) if W[a] else 0
    r = None
    if a3.startswith('söz sürüyor'):
        mm = re.findall(r'(\d+)-(\d+)\. kelime', a3); r = (int(mm[-1][0]), int(mm[-1][1])) if mm else None
    if r is None:
        mm = re.search(r'(\d+)-(\d+)\. kelime', a3)
        if mm: r = (int(mm.group(1)), int(mm.group(2)))
    if r is None:
        mm = re.search(r'\((\d+)\. kelimeden', a3)
        if mm: r = (int(mm.group(1)), nw)
    if r is None:
        mm = re.search(r'(\d+)\. kelime', a3)
        if mm: r = (int(mm.group(1)), int(mm.group(1)))
    if r is None: H.append('(2) %d:%d A3 kapsamı okunamadı: %s' % (S, a, a3[:60])); continue
    rem = [w for w in range(r[0], r[1] + 1) for f, t, ft in W[a][w] if t == 'P' and ft.split('|')[0] == 'REM']
    seg = re.search(r'%d:%d söz içi REM: ([^;]*)' % (S, a), sz)
    if rem and (not seg or seg.group(1).strip().startswith('yok') or not all(re.search(r'(?<!\d)%d\.' % w, seg.group(1)) for w in rem)):
        H.append('(2) %d:%d söz içi REM %s kaydedilmemiş' % (S, a, ', '.join('%d.' % w for w in rem)))
# ── (6) medde satırı ──
md = medde_fark.satir('/home/claude/b%s/say2.txt' % NN)
if md not in ' '.join(item('bölüm: ')): H.append('(6) medde satırı medde_fark.py çıktısını aynen taşımıyor')
# ── (7) A1 esmâ kural adı ──
EK = collections.defaultdict(set)
for l in open(Y + 'esma_el_%d_%d_%d.txt' % (S, A, B), encoding='utf-8'):
    for k_ in re.findall(r"'%d:(\d+):\d+'" % S, l):
        mm = re.search(r' — (.+?) → ', l)
        if mm: EK[int(k_)].add(mm.group(1).strip())
for a, ks in EK.items():
    a1 = satir(a, '◈A').split('; A2 ')[0]
    if 'esmâ' in a1 and not any(k in a1 for k in ks): H.append('(7) %d:%d A1 esmâ kural adı esma_el kuralıyla (%s) eş değil' % (S, a, ' / '.join(sorted(ks))))
# ── (9) joker ──
S2D = {}
for blk in open('/home/claude/b%s/say2.txt' % NN, encoding='utf-8').read().split('### ')[1:]:
    L = blk.strip().splitlines(); mm = re.match(r'lemma dizisi (\[.*\]) \|', L[1]) if len(L) > 1 else None
    if mm: S2D[L[0].strip()] = ast.literal_eval(mm.group(1))
src = open('/home/claude/b%s/yap/metin_yap.py' % NN, encoding='utf-8').read()
for key, ad in re.findall(r"say\('(dizi \d+ \d+ \d+ \d+)', \"([^\"]+)\"", src):
    if key not in S2D: continue
    tk, dz = ad.split(), S2D[key]
    if len(tk) == len(dz):
        for i, (t, d) in enumerate(zip(tk, dz)):
            if (t == '_') != (len(d) == 0): H.append("(9) %s '%s' %d. öğe: joker '_' ⇔ boş demet eşleşmiyor" % (key, ad, i + 1))
# ── (10) nekre ──
def dizi_seq(a): m = re.match(r"◇ '.*?' — (.*?) \(ölçüm ", M[a], re.S); return m.group(1) if m else ''
for a in range(A, B + 1):
    ind = sum(1 for w, segs in W[a].items() if any('INDEF' in ft.split('|') for f, t, ft in segs))
    sq = dizi_seq(a); d1 = re.search(r'◈D — D1 (.*?); D2 ', M[a])
    if sq.count('nekre') != ind: H.append('(10) %d:%d ◇ lafız dizisinde nekre %d / morph INDEF kelime %d' % (S, a, sq.count('nekre'), ind))
    if d1 and d1.group(1).count('nekre') != ind: H.append('(10) %d:%d D1 nekre %d / morph INDEF kelime %d' % (S, a, d1.group(1).count('nekre'), ind))
# ── (11) e / a yazım farkı ──
ESKI = collections.Counter()
for f in glob.glob(Y + 'metin_%d_*_*.txt' % S):
    x, y = map(int, re.findall(r'_(\d+)_(\d+)\.txt$', f)[0])
    if y >= A: continue
    mm = {}; exec(open(f, encoding='utf-8').read(), {'M': mm, 'MEAL': {}})
    for v in mm.values():
        m = re.match(r"◇ '.*?' — (.*?) \(ölçüm ", v, re.S)
        if m: ESKI.update(re.findall(r"'((?:[^']|'(?=[a-zâîûçğışöü]))+)'", m.group(1)))
NRM = collections.defaultdict(set)
for k in ESKI: NRM[k.replace('e', 'a')].add(k)
for a in range(A, B + 1):
    for ad in set(re.findall(r"'((?:[^']|'(?=[a-zâîûçğışöü]))+)'", dizi_seq(a))):
        es = {k for k in NRM.get(ad.replace('e', 'a'), set()) if k != ad}
        if es and ad not in ESKI: H.append("(11) %d:%d lafız dizisi adı '%s' / önceki bloklarda '%s'" % (S, a, ad, "', '".join(sorted(es))))
# ── (12) fâsıla 'kırıl-' ──
olc = open('/home/claude/b%s/olcum.txt' % NN, encoding='utf-8').read().split('\n\n')
for it in item('fâsıla'):
    for p in it.split('; '):
        if re.search(r'kırıl(?!ma yok)', p) and 'kırık yok' not in p:
            for a in map(int, re.findall(r'%d:(\d+)' % S, p)):
                if A <= a <= B and 'KAFİYE' not in olc[a - A]: H.append("(12) %d:%d fâsıla maddesinde 'kırıl-', ölçümde kafiye kırılması yok" % (S, a))
# ── (13) önceki karar sonucu ──
for txt in item('karşılık çakışması') + item('meal karşılık farkı kararları'):
    for m in re.finditer(r'önceki karar \(blok \d+: ((?:[^()]|\([^()]*\))*)\)', txt):
        if not re.search(r'çakışma sayılmamıştı|çakışma sayılmıştı|tam okuma sonu|çakışma değil', m.group(1)): H.append('(13) önceki karar parantezi sonucu taşımıyor: %s' % m.group(0)[:80])
# ── (14) ث / ص ──
LEMS = set()
for l in open('/home/claude/calisma/morph.txt', encoding='utf-8'):
    m = re.search(r'LEM:([^|\s]+)', l)
    if m: LEMS.add(N_(m.group(1)))
for a in range(A, B + 1):
    for w, segs in W[a].items():
        for f, t, ft in segs:
            m = re.search(r'LEM:([^|]+)', ft)
            if m and 'ث' in m.group(1) and N_(m.group(1).replace('ث', 'ص')) in LEMS:
                if not any('ث / ص' in it and '%d:%d' % (S, a) in it for it in ITEMS): H.append('(14) %d:%d %d. kelime ث / ص eş yazım notu yok' % (S, a, w))
# ── (15) yeni kök anlamı ⇔ blok meal karşılıkları ──
ke = open('/home/claude/calisma/kok_ekle_%d.py' % S, encoding='utf-8').read()
mm = re.search(r'# blok %s\b[^\n]*\n((?:\s+\(.*\),\n)+)' % int(NN), ke)
YK = ast.literal_eval('[' + mm.group(1) + ']') if mm else []
vp = '/home/claude/b%s/yap/veri.py' % NN
if YK and _o.path.exists(vp):
    sp = iu.spec_from_file_location('veri', vp); v = iu.module_from_spec(sp); sp.loader.exec_module(v)
    for kok, gl in YK:
        gt = set(re.findall(r'[a-zçğıöşüâîû]+', gl.lower()))
        for a, L in v.MK.items():
            for tr, q, its in L:
                for it in its:
                    m = re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı) \((\d+)\. kelime", it)
                    if not m or m.group(1).lower() not in gt: continue
                    rk = {re.search(r'ROOT:([^|]+)', ft).group(1) for f, t, ft in W[a][int(m.group(2))] if 'ROOT:' in ft}
                    if rk and N_(kok) not in {N_(x) for x in rk}: H.append("(15) yeni kök %s anlamı '%s' %d:%d %s. kelimenin (kök %s) meal karşılığını içeriyor" % (kok, m.group(1), S, a, m.group(2), '/'.join(rk)))
# ── (16) mecrur ilgi zamiri A1'de ──
for a in range(A, B + 1):
    a1 = satir(a, '◈A').split('; A2 ')[0]
    for m in re.finditer(r"'(?:li|bi|mine)'llezîne[^']*'", a1): H.append("(16) %d:%d A1'de mecrur ilgi zamiri %s" % (S, a, m.group(0)))
    for m in re.finditer(r"'llezîne[^']*' \(([^()]*?)(\d+)(?:-\d+)?\. (?:ve \d+(?:-\d+)?\. )?kelime", a1):  # önek alıntıda yazılmasa da: kelimenin morph'unda 'li' / 'bi' öneki ya da önceki kelime 'min'
        w = int(m.group(2)); lm = [re.search(r'LEM:([^|]+)', ft) for f, t, ft in W[a][w]]
        onek = any(x and N_(x.group(1)) in (N_('ل'), N_('ب')) for x in lm[:-1]) or any(re.search(r'LEM:مِن', ft) for f, t, ft in W[a].get(w - 1, []))
        if onek and any('REL' in ft.split('|') for f, t, ft in W[a][w]): H.append("(16) %d:%d A1'de mecrur ilgi zamiri %d. kelime" % (S, a, w))
# ── (17) edilgen fiilin faili ──
for a in range(A, B + 1):
    a1 = satir(a, '◈A').split('; A2 ')[0]
    for w, segs in sorted(W[a].items()):
        if any(t == 'V' and 'PASS' in ft.split('|') for f, t, ft in segs):
            sg = [x for x in bol(a1) if re.search(r'(?<![\d-])%d(?:\.| ve |, |-\d+\.) ?(?:ve \d+\. )?kelime|(?<![\d-])%d\. kelime' % (w, w), x)]
            if not any('faili (adsız' in x or 'naib-i faili' in x for x in sg): H.append('(17) %d:%d %d. kelime edilgen fiilin faili A1\'de \'faili (adsız\' / \'naib-i faili\' ile yok' % (S, a, w))
for h in H: print('HATA', h)
print('bolum11_kurallar hata:', len(H))

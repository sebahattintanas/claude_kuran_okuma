# sûre 6 bölüm 6 denetimi araç kuralları (bekleyen_ariza_6_b13.txt 2. öğe) — salt okur:
#  (1) EMSAL_KAPSAM_DIZI: ◇'de say() ile basılan ve bag'de bu ayete bağlı emsali listeleyen her sayım (lemma dizisi dahil) ARIZA'da kelime aralığı örtüşen bir emsal meal satırıyla
#  (2) BAG_SAYIM_BASIM: bag 'kural' / 'not' alanında tırnak içinde anılan her sayım anahtarı ('say …' / 'dizi …') bloğun ◇ say() çağrılarında basılı
#  (3) LEMMA_YAZIM_BIR: ARIZA 'karşılık çakışması' grubunda yalnız a / e ünlüsüyle ayrışan iki Arapça üye yok (bir lemmanın iki transliterasyonu); üyelerden biri önceki ARIZA kayıtlarında yoksa (yeni giren yazım) — eski kayıtlar geriye dönük yazılmaz
#  (4) CEVAP_A4_KONUM: morph RSLT / CAUS 'fe' ve ANS edatlı kelime A4'te 'cevap … (N. kelime)' kaydında ya da 'kapsam dışı' notuyla
#  (5) GEREKCE_SINIF_SONUC: 'meal karşılık farkı kararları'nda 'bağlam' gerekçeli kararlar tek kapalı sonuçta
# (elle: ESMA_KOSUL, SOZ_GONDERGE, GERIYE_DONUK_ZORUNLU, YAPI_KARSILIK_BIR, ORTAK_KARSILIK, ORTAC_NOT_HEP, KALIP_AD_ONEK, JOKER_IDDIA, SAYI_SOZCUK, KIP_NOT_TAM, TEKIL_MEDDE_METIN, LEM_BOZUK_ONEK)
# kullanım (/home/claude'dan): python3 sunum/bolum22_kurallar.py A B NN
import sys as _sy; _sy.path.insert(0, '/home/claude/sunum'); from sure import BK as _BK, S
import re, sys, ast, os, glob, collections
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
MB = _BK + 'b%s/yap/metin_body.py' % NN
SAYK = re.findall(r"say\('((?:say|dizi|lem) [^']+)'", open(MB, encoding='utf-8').read()) if os.path.exists(MB) else []
S2 = {}
if os.path.exists(_BK + 'b%s/say2.txt' % NN):
    for b in open(_BK + 'b%s/say2.txt' % NN, encoding='utf-8').read().split('### ')[1:]:
        m = re.search(r"\{'bu'.*\}", b)
        if m: S2[b.split('\n', 1)[0].strip()] = ast.literal_eval(m.group(0))
BAG = ast.literal_eval('[' + open(Y + 'bag_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read() + ']') if os.path.exists(Y + 'bag_%d_%d_%d.txt' % (S, A, B)) else []

# ── (1) EMSAL_KAPSAM_DIZI ──
EMK = ' '.join(m for m in ITEMS if 'emsal meal karşılık farkları' in m)
SAT = [(m.group(1), int(m.group(2)), m.group(3)) for m in re.finditer(Q + r" %d:(\d+) '(?:[^']|'(?=[a-zçğıöşüâîû]))*' / (\d+:\d+) '" % S, EMK)]
def kelime(q):  # sûre 6 blok 17: bölüm 8 kuralı 14 sayımıyla eş — wasl birleşmeli belirteç ('dûni'llâhi', 'ke'llezi'stehvethu') morph kelimelerine bölünür
    n = 0
    for t in q.split():
        if t in ('ve', 'fe', 'fa', 'va', 'yâ'): continue
        parca = re.split(r"(?<=[aeiuâîû])'(?=l-|ll|[a-zçğışöü]-|[bcdfğhklmnqrsştxyz]{2})", t)
        n += 1 + sum(1 for x in parca[:-1] if x not in ('ve', 'fe', 'fa', 'va', 'bi', 'li', 'le', 'ke') and not x.endswith('-'))
    return n
def aralik(n, kal):
    d = dia(n); i = d.find(kal)
    if i < 0: return None
    on = d[:i]
    ayn = on.endswith("'")
    if ayn: on = on[:-1]  # bölüm 8 denetimi: ayınla başlayan kelime ("rabbi'l-'âlemîn") — kesme, kısa çizgi denetiminden önce atılır
    if on.endswith('-'):  # harfi tarif ('fi'l-', 'rabbi'l-', 'bi'l-'): öndeki ad ayrı kelime, önek edat aynı kelime
        on = re.sub(r"'?[a-zçğışöü]{1,2}-$", '', on)
        son = on.split(' ')[-1].split("'")[-1] if on.strip() else ''
        if son in ('ve', 'fe', 'fa', 'va', 'bi', 'li', 'le', 'ke'): on = on[:len(on) - len(son)].rstrip("'")
    elif on and not on.endswith(' ') and on.split(' ')[-1].split("'")[-1] in ('ve', 'fe', 'fa', 'va', 'bi', 'li', 'le', 'ke'):  # 'bi'l-haqq' içinde 'l-haqq': önek edat aynı kelime
        on = on[:len(on) - len(on.split(' ')[-1].split("'")[-1])].rstrip("'")
    bas = kelime(on) + 1
    return bas, bas + max(kelime(kal), 1) - 1
for b_ in BAG:
    e, hed = b_['bag'].split(' → ')
    n = int(hed.split(':')[1])
    if not A <= n <= B: continue
    for k in SAYK:
        m = re.match(r'(?:say %d:(\d+) (\d+)-(\d+)|dizi %d (\d+) (\d+) (\d+))' % (S, S), k)
        if not m or k not in S2: continue
        a_, i, j = (int(m.group(1)), int(m.group(2)), int(m.group(3))) if m.group(1) else (int(m.group(4)), int(m.group(5)), int(m.group(6)))
        if a_ != n or e not in S2[k]['basilan']: continue
        EN['emsal_sayim'] += 1
        ok = False
        for kal, sn, se in SAT:
            if sn != n or se != e: continue
            r = aralik(n, kal)
            if r and not (r[1] < i or r[0] > j): ok = True
        if not ok: H.append("(1) %d:%d sayım '%s' emsal %s listeliyor — aralığı örten emsal meal satırı yok" % (S, n, k, e))

# ── (2) BAG_SAYIM_BASIM ──
for b_ in BAG:
    for k in re.findall(r"'((?:say|dizi|lem) [^']+)'", b_.get('kural', '') + ' ' + b_.get('not', '')):
        EN['bag_sayim'] += 1
        if k not in SAYK: H.append("(2) bag %s anahtarı '%s' ◇'de basılmamış" % (b_['bag'], k))

# ── (3) LEMMA_YAZIM_BIR ──
def ae(x, y):
    if x == y or len(x) != len(y): return False
    return all(c == d or {c, d} == {'a', 'e'} for c, d in zip(x, y))
ONCE = ' '.join(open(f, encoding='utf-8').read() for f in glob.glob(Y + 'ariza_%d_*_*.txt' % S) if int(f.split('_')[-2]) < A)
for it in item('karşılık çakışması'):
    for g in re.split(r"; (?=(?:KÖK )?'[^']+' ←)", it.split('): ', 1)[-1]):
        uy = sorted(set(re.findall(r"'((?:[^']|'(?=[a-zâîûçğışöü]))+)'", g.split(':', 1)[0].split(' ← ', 1)[-1])))
        EN['grup'] += 1
        for x in uy:
            for y in uy:
                if x < y and ae(x, y) and (("'%s'" % x) not in ONCE or ("'%s'" % y) not in ONCE): H.append("(3) çakışma grubu %s: '%s' / '%s' bir lemmanın yazım farkı" % (g.split(' ←')[0][:30], x, y))

# ── (4) CEVAP_A4_KONUM ──
MO = collections.defaultdict(dict)
for l in open(_BK + 'b%s/morph.txt' % NN, encoding='utf-8'):
    p = l.rstrip('\n').split('\t')
    if len(p) > 2: MO[int(p[0].split(':')[1])][int(p[0].split(':')[2])] = p[2]
for a in range(A, B + 1):
    a4 = re.search(r'\bA4 (.*)$', satir(a, '◈A'))
    a4 = a4.group(1) if a4 else ''
    for w, f in sorted(MO[a].items()):
        if re.search(r'(?:RSLT|CAUS)\|PREF\|LEM:ف|(?:^|\+ )P\|ANS\|', f):
            EN['cevap'] += 1
            segs = [re.split(r'; (?:söz |şahıs |edim |şart → |bölüm )', a4[m_.start():])[0] for m_ in re.finditer(r'cevap', a4)]
            if not any('(%d. kelime)' % w in g for g in segs) and 'kapsam dışı' not in a4:
                H.append("(4) %d:%d %d. kelime cevap edatı (morph %s) — A4'te konumlu cevap kaydı yok" % (S, a, w, re.search(r'RSLT|CAUS|ANS', f).group(0)))

# ── (5) GEREKCE_SINIF_SONUC ──
kr = ' '.join(item('meal karşılık farkı kararları')).split('): ', 1)[-1]
SON = collections.defaultdict(set)
for m in re.finditer(r"— (çakışma değil|çakışma — tam okuma sonu) \(([^()]*(?:\([^()]*\)[^()]*)*)\)", kr):
    if re.search(r'\bbağlam', m.group(2)):
        EN['baglam'] += 1; SON['bağlam'].add('değil' if m.group(1) == 'çakışma değil' else 'tam')
if len(SON['bağlam']) > 1: H.append("(5) 'bağlam' gerekçesi farklı kapalı sonuçla: değil ve tam okuma sonu")

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum22_kurallar hata: %d' % len(H))

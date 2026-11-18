# bölüm 14 (sûre 5) denetimi araç kuralları (bekleyen_ariza_5_b32.txt 2. öğe) — salt okur:
#  (2) meal maddesinde fiil karşılık adı ("'X' 'Y' karşılığı / açılımı (N. kelime", N. kelime morph fiil) ◇ transliterasyonunun alt dizesi
#  (3) emsal meal notundaki Arapça kalıp emsal ayetin say2 listesinde: kalıbın ◇ konumunu tam kapsayan say anahtarı (öneksiz ya da '--on') emsali listelemeli; 'korpusta 1' kalıba not yazılmaz
#  (4) A3 '(söz içi …)' yalnız ayette A3'ten önce قول kökünden fiil varsa; yoksa '(söz biçimli içerik …)' ve A4'te 'söz açılır' / 'söz kapanır' yazılmaz
#  (5) söz / tırnak maddesi 'tırnaksız … (emsal biçimi)' diyorsa bu bloğun emsal metinlerinde tırnak işareti (") yok
#  (6) kayıtlarda (metin, ARIZA — taşınan denetim maddeleri hariç —, seg) ASCII dışı ünsüz transliterasyon harfi ('ṣ', 'ḥ', 'ṭ', 'ẓ', 'ḍ' …) yok
#  (7) '(morph SUB)' ya da 'en' / 'enne' maddesinde içerici sözcük ('X' içinde) yönelme / ayrılma ekiyle bitiyorsa 'fiil yönetimi takdiri' aynı maddede (kural14 kuralı 4'ün içerici sözcük genişlemesi)
#  (8) ◈D D3 maddesindeki her 'ayetler arası kalıp' kaydı iki 'dizi' anahtarı taşır ve ikisi de say2'de koşulmuş
#  (10) R5 maddesinde 'biçim öğesi' ibaresinden hemen sonra tırnaklı öğe adı
#  (kural 1 cakisma.py / bolum7 / bolum9'da; kural 9 edat_etiket.py'de; kurallar 11-13 elle)
# kullanım (/home/claude'dan): python3 sunum/bolum14_kurallar.py A B NN
import sys as _sy; _sy.path.insert(0, '/home/claude/sunum'); from sure import BK as _BK
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from sure import S
import re, sys, ast, collections, importlib.util as iu
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
Y = '/home/claude/yamalar/'
H = []
TUM = ast.literal_eval('{' + open(Y + 'ariza_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read() + '}')[(A, B)]
ITEMS = [m for m in TUM if not re.match(r'bölüm (denetimi \(|\d+ denetiminden)', m)]
def item(bas): return [m for m in ITEMS if m.startswith(bas)]
M, MEAL = {}, {}
MT = open(Y + 'metin_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read()
exec(MT, {'M': M, 'MEAL': MEAL})
DIA = {n: re.match(r"◇ '(.*?)' — ", M[n]).group(1) for n in range(A, B + 1)}
W = collections.defaultdict(lambda: collections.defaultdict(list))
for l in open(_BK + 'b%s/morph%d.txt' % (NN, S), encoding='utf-8'):
    loc, f, t, feat = l.rstrip('\n').split('\t'); s_, a_, w_, p_ = map(int, loc.split(':'))
    W[a_][w_].append((f, t, feat))
sp = iu.spec_from_file_location('veri', _BK + 'b%s/yap/veri.py' % NN); veri = iu.module_from_spec(sp); sp.loader.exec_module(veri)
Q = r"'((?:[^']|'(?=[a-zâîûçğışöü]))+)'"
S2 = open(_BK + 'b%s/say2.txt' % NN, encoding='utf-8').read()
BLK = {}
for blk in S2.split('### ')[1:]: BLK.setdefault(blk.split('\n')[0].strip(), blk)
def liste(h):
    m = re.search(r'^liste: (.*)$', BLK.get(h, ''), re.M)
    return [x.rstrip('†') for x in m.group(1).split(', ')] if m else []
def kelime(q):  # bolum9_kurallar kelime() ile eş
    n = 0
    for t in q.split():
        if t in ('ve', 'fe', 'fa', 'va', 'yâ'): continue
        parca = re.split(r"(?<=[aeiuâîû])'(?=l-|ll|[a-zçğışöü]-|[bcdfğhklmnqrsştxyz]{2})", t)
        n += 1 + sum(1 for x in parca[:-1] if x not in ('ve', 'fe', 'fa', 'va', 'bi', 'li', 'le', 'ke') and not x.endswith('-'))
    return n
def satir(n, bas):
    for l in M[n].split('\n'):
        if l.startswith(bas): return l
    return ''
def a_parca(n, k):
    l = satir(n, '◈A'); m = re.search(r'\b%s (.*?)(?:; A%d |$)' % (k, int(k[1]) + 1), l)
    return m.group(1) if m else ''

# ── (2) fiil karşılık adı ◇ alt dizesi ──
for n in sorted(veri.MK):
    if not A <= n <= B: continue
    for tr, q, its in veri.MK[n]:
        for it in its:
            m = re.match(r"'[^']+(?:'[^']*)*?' " + Q + r" (?:karşılığı|açılımı) \((\d+)\. kelime", it)
            if not m: continue
            y, k = m.group(1), int(m.group(2))
            gov = [(f, t, ft) for f, t, ft in W[n][k] if 'PREF' not in ft and 'SUFF' not in ft]
            if gov and gov[0][1] == 'V' and y not in DIA[n]: H.append("(2) %d:%d %d. kelime fiil karşılık adı '%s' ◇ alt dizesi değil" % (S, n, k, y))

# ── (3) emsal meal notu kalıbı emsal sayımında ──
mi = ' '.join(item('meal (okuma'))
if 'emsal meal karşılık farkları' in mi:
    em = mi.split('emsal meal karşılık farkları', 1)[1].split('): ', 1)[-1]
    for m in re.finditer(Q + r" (\d+):(\d+) " + Q + r" / (\d+:\d+) " + Q + r" \(emsal metninde\)", em):
        kal, n, e = m.group(1), int(m.group(3)), m.group(5)
        if not A <= n <= B or kal not in DIA[n]: continue
        on = DIA[n][:DIA[n].index(kal)]
        i = kelime(on.rstrip("'")) + 1 if on.endswith("'") else kelime(on) + 1; j = i + kelime(kal) - 1
        ok = any(e in liste(h) for h in BLK if re.fullmatch(r'say %d:%d (\d+)-(\d+)(?: --on)?' % (S, n), h) and int(re.match(r'say \d+:\d+ (\d+)', h).group(1)) <= i and int(re.search(r'-(\d+)', h).group(1)) >= j)
        if not ok: H.append("(3) emsal %s meal notu kalıbı '%s' (%d:%d %d-%d) emsalin sayım listesinde yok" % (e, kal[:40], S, n, i, j))

# ── (4) söz yalnız قول fiilinden sonra ──
for n in range(A, B + 1):
    a3 = a_parca(n, 'A3')
    m = re.search(r'\(söz içi, (\d+)-(\d+)\. kelime\)', a3)
    if not m: continue
    bas = int(m.group(1))
    kul = any('ROOT:قول' in ft and t == 'V' for w in W[n] if w < bas for f, t, ft in W[n][w])
    if not kul: H.append("(4) %d:%d A3 '(söz içi …)' — A3 başından (%d. kelime) önce قول kökünden fiil yok; '(söz biçimli içerik …)' yazılmalı, A4'te 'söz açılır' yazılmaz" % (S, n, bas))
for n in range(A, B + 1):
    if 'söz biçimli içerik' in a_parca(n, 'A3') and re.search(r'söz (açılır|kapanır)', a_parca(n, 'A4')): H.append("(4) %d:%d söz biçimli içerikte A4 'söz açılır / kapanır'" % (S, n))

# ── (5) 'emsal biçimi' tırnaksız gerekçesi ──
st = ' '.join(item('söz / tırnak'))
if re.search(r'tırnaksız[^;]*\(emsal biçimi', st):  # bölüm 15 denetimi kuralı 6: '(emsal biçimi — …)' de
    try: et = open(_BK + 'b%s/emsal.txt' % NN, encoding='utf-8').read()
    except FileNotFoundError: et = ''
    if re.search(r'["“”]', et) or re.search(r"(?:^|[\s:(])'[A-ZÇĞİÖŞÜÂÎÛ]", et): H.append("(5) söz / tırnak maddesi 'tırnaksız (emsal biçimi)' diyor — bu bloğun emsal metninde tırnak var")  # bölüm 15 denetimi kuralı 6: kesme tırnak da
    for e in re.findall(r'(\d+:\d+) emsal mealinde', st):  # bölüm 15 denetimi kuralı 6: anılan emsalde قول fiili
        if not any(l.startswith(e + ':') and '\tV\t' in l and 'ROOT:قول' in l for l in open('/home/claude/calisma/morph.txt', encoding='utf-8')):
            H.append("(5) 'emsal biçimi' gerekçesindeki %s'de قول fiili yok" % e)

# ── (6) ASCII dışı ünsüz ──
AS = re.compile(r'[ṣḥṭẓḍṯḏġḳṢḤṬẒḌ]')
for ad, t in (('metin', MT), ('ARIZA', ' '.join(ITEMS)),  # taşınan denetim maddeleri (BEK) örnek harf anar — süzülür (blok 33)
                  ('seg', open(_BK + 'b%s/yap/seg.py' % NN, encoding='utf-8').read())):
    for x in sorted(set(AS.findall(t))): H.append("(6) %s kaydında ASCII dışı ünsüz '%s'" % (ad, x))

# ── (7) içerici sözcükte yönelme / ayrılma eki ──
for n in sorted(veri.MK):
    if not A <= n <= B: continue
    for tr, q, its in veri.MK[n]:
        for it in its:
            if not (re.match(r"'(en|enne)' \d+\. kelimede", it) or '(morph SUB' in it or '; morph SUB' in it): continue
            for w in re.findall(r"'([^']+)' içinde", it):
                son = w.lower()
                if son.endswith(('yle', 'yla', 'ile', 'de', 'da', 'te', 'ta')): continue
                if (re.search(r'[ny]?[ae]$', son) or re.search(r'[dt][ae]n$', son)) and 'fiil yönetimi takdiri' not in it:
                    H.append("(7) %d:%d '%s' içerici sözcüğü ekli — 'fiil yönetimi takdiri' yok: %s" % (S, n, w, it[:60]))

# ── (8) ayetler arası kalıp iki dizi anahtarı ──
d3 = ' '.join(item('◈D D3 / bag'))
for m in re.finditer(r"ayetler arası kalıp '((?:[^']|'(?=[a-zâîûçğışöü]))+)' \(([^)]*)\)([^;]*)", d3):
    dz = re.findall(r"'(dizi \d+ \d+ \d+ \d+)'", m.group(3))
    if len(dz) < 2: H.append("(8) ayetler arası kalıp '%s' — iki lemma dizisi anahtarı yok" % m.group(1)[:40]); continue
    for k in dz:
        if k not in BLK: H.append("(8) ayetler arası kalıp '%s' — '%s' say2'de koşulmamış" % (m.group(1)[:40], k))

# ── (10) biçim öğesi adı ──
r5 = ' '.join(item('araç tanımı farkları (R5'))
for m in re.finditer(r'biçim öğesi(?! \')(.{0,40})', r5): H.append("(10) R5 'biçim öğesi' ardından tırnaklı öğe adı yok: 'biçim öğesi%s'" % m.group(1))

for h in H: print('HATA', h)
print('bolum14_kurallar hata: %d' % len(H))

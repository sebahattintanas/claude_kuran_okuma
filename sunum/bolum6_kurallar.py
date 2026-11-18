# bölüm 6 (sûre 5) denetimi kuralları 2 (çakışma grubu kapsamı + tek kapalı karar), 7 (ARIZA'ya yapıştırılmış araç çıktılarının tazeliği),
# 12 (Türkçe alıntılar MEAL alt dizesi), 13 (yıldız maddesi ⇔ bilanço yıldız kaynağı), 14 (esmâ kural adı ⇔ önceki kayıtların emsali),
# 16 (lemma dizisi adında joker '_') — betik denetimi
# kullanım (/home/claude'dan): python3 sunum/bolum6_kurallar.py A B NN [--tazelik-yok]
#   yazım sözleşmesi:
#     yıldız maddesi: "S:a ★★ (kaynak <bilanço kaynağı>, z=<z>; eşiği geçen öbür ölçüler <ad>, …; kafiye kırığı)" — eşik / kafiye yoksa o kısım yazılmaz
#     çakışma maddesi: her grup "'X' ←" ya da "KÖK 'X' ←" başlığıyla, grup başına tam bir kapalı karar ('çakışma değil' ya da 'çakışma — tam okuma sonu')
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from sure import S
import re, sys, ast, glob, subprocess, importlib.util
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
TAZE = '--tazelik-yok' not in sys.argv
Y = '/home/claude/yamalar/'
H = []
M, MEAL = {}, {}
g = {'M': M, 'MEAL': MEAL}
exec(open(Y + 'metin_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read(), g)
for k, v in g.items():
    if k.startswith('MEAL') and isinstance(v, dict): MEAL.update(v)
ARM = open(Y + 'ariza_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read()
AR = ast.literal_eval('{' + ARM + '}')
ITEMS = [m for v in AR.values() for m in v if not m.startswith(('bölüm denetimi (', 'bölüm 6 denetiminden', 'bölüm 5 denetiminden', 'bölüm 4 denetiminden', 'bölüm 3 denetiminden'))]
def item(bas): return [m for m in ITEMS if m.startswith(bas)]
def run(*a): return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout
# ── (2) çakışma grubu kapsamı ──
DOS = sorted([f for f in glob.glob(Y + 'ariza_%d_*_*.txt' % S) if int(f.split('_')[-2]) <= A], key=lambda p: int(p.split('_')[-2]))
spec = importlib.util.spec_from_file_location('veri', '/home/claude/b%s/yap/veri.py' % NN); veri = importlib.util.module_from_spec(spec); spec.loader.exec_module(veri)
KY = {m.group(1) for L in veri.MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bu bloğun Türkçe karşılıkları: son dosyaya dokunan gruplar
CAK = [l for l in run('/home/claude/sunum/cakisma.py', *DOS).splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
cm = ' '.join(item('karşılık çakışması'))
HD = []
for l in CAK:
    h = ("KÖK '%s' ←" % l.split()[1]) if l.startswith('KÖK') else ("'%s' ←" % l.split(' ←')[0].strip())
    HD.append(h)
    if h not in cm: H.append('çakışma grubu ARIZA\'da yok: ' + h)
pos = sorted((cm.find(h), h) for h in HD if h in cm)
for k, (p, h) in enumerate(pos):
    son = pos[k + 1][0] if k + 1 < len(pos) else len(cm)
    parca = cm[p:son]
    n = parca.count('çakışma değil') + parca.count('çakışma — tam okuma sonu')
    if n != 1: H.append('çakışma grubu karar sayısı %d (tam bir kapalı karar olmalı): %s' % (n, h))
print('çakışma grubu: araç %d, ARIZA başlığı %d' % (len(HD), len(pos)))
# ── (12) Türkçe alıntılar MEAL alt dizesi ──
TQ = 0
for a, L in veri.MK.items():
    for tr, q, its in L:
        for x in [tr] + [m for it in its for m in re.findall(r"(?:\(|; )'((?:[^']|'(?=[a-zçğıöşü]))+)' içinde", it) if not m.startswith('-')]:
            for p in [y.strip() for y in x.split('…')]:
                if not p: continue
                TQ += 1
                if p not in MEAL.get(a, ''): H.append("Türkçe alıntı MEAL dışı %d:%d '%s'" % (S, a, p))
# bölüm 8 kuralı 8: "'X' N. kelimede 'Y' ile", "… eki ile 'Y'" ve "iyelik ile 'Y'" alıntıları da; büyük / küçük harf korunur, Türkçe sözcük başı sınırı aranır
TH = 'a-zçğıöşüâîûA-ZÇĞİÖŞÜ'
for a, L in veri.MK.items():
    for tr, q, its in L:
        for it in its:
            for p in re.findall(r"(?:kelimede|eki ile|iyelik ile) '((?:[^']|'(?=[a-zçğıöşü]))+)'", it):
                if p.startswith('-'): continue
                TQ += 1
                if not re.search(r'(?<![%s])%s' % (TH, re.escape(p)), MEAL.get(a, '')): H.append("Türkçe alıntı MEAL dışı (sözcük başı) %d:%d '%s'" % (S, a, p))
print('Türkçe alıntı: %d' % TQ)
# ── (13) yıldız maddesi ⇔ bilanço ──
sys.path.insert(0, '/home/claude/calisma'); _cwd = _o.getcwd(); _o.chdir('/home/claude/calisma')
import blok_bilanco
YK = blok_bilanco.bilanco(S, A, B)['yildiz_kaynak']; _o.chdir(_cwd)
yi = ' '.join(item('yıldız'))
for a, d in sorted(YK.items(), key=lambda x: int(x[0])):
    z = ('%.2f' % d['z']).replace('.', ',')
    beklenen = '%d:%s %s (kaynak %s, z=%s' % (S, a, '★' * d['yildiz'], d['kaynak'], z)
    if beklenen not in yi: H.append('yıldız maddesi: %s yok' % beklenen); continue
    seg = yi[yi.index(beklenen):].split(')')[0]
    for ad in d.get('esigi_gecen_diger', {}):
        if ad not in seg: H.append('yıldız maddesi %d:%s eşiği geçen %s anılmamış' % (S, a, ad))
    if d.get('kafiye_kirik') and 'kafiye kırığı' not in seg: H.append('yıldız maddesi %d:%s kafiye kırığı anılmamış' % (S, a))
print('yıldız: bilanço %d ayet' % len(YK))
# ── (14) esmâ kural adı ⇔ önceki kayıtlar ──
KW = {"'inne/enne' haberi": r"inne|enne|haber", "'ve'llâhu X' kuralı": r"llâhu|lâhu", 'esmâ adı esmâ dışı göndergeyle': r'esmâ dışı|esmâ adı|gönderge',
      'çoğul insan göndergeli': r'çoğul|insan', 'olumsuz nekre ehad': r'olumsuz nekre'}
LEM = {}
for l in open('/home/claude/calisma/morph.txt', encoding='utf-8'):
    loc, fo, t, ft = l.rstrip('\n').split('\t'); k = ':'.join(loc.split(':')[:3])
    m = re.search(r'LEM:([^|]+)', ft)
    if m and t == 'N': LEM.setdefault(k, m.group(1))
ONCE = {}
for l in open('/home/claude/calisma/esma_el.py', encoding='utf-8'):
    m = re.match(r"\s*'(\d+:\d+:\d+)':\s*'(\w+)',\s*#\s*(.*)", l)
    if m: ONCE.setdefault((LEM.get(m.group(1)), m.group(2)), []).append((m.group(1), m.group(3)))
# bölüm 8 kuralı 2: esmâ kural adı kapalı listeden; listede olmayan ad isabet (yeni ad yalnız esma_el.py emsali anılarak ve kullanıcı kararıyla eklenir); ARIZA'da 'tam okuma sonu' notlu karar esma_el'e kapalı karar olarak girmez
KAPALI = ("'inne/enne' haberi", "'ve'llâhu X' kuralı", 'esmâ adı esmâ dışı göndergeyle', 'çoğul insan göndergeli', 'olumsuz nekre ehad', 'lafzın haberi',
          "'ve kâna'llâhu X' lafzın haberi", "'kefâ bi'llâhi X' temyizi", "'vecede'llâhe X' mef'ûlü")
esm_it = ' '.join(item('esmâ:'))
E14 = 0
try: blk = open(Y + 'esma_el_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read()
except FileNotFoundError: blk = ''
for k, kr, yorum in re.findall(r"'(\d+:\d+:\d+)':\s*'(\w+)',\s*#\s*(.*)", blk):
    E14 += 1
    kad = yorum.split(' — ', 1)[1] if ' — ' in yorum else yorum
    if not any(kad.startswith(x) for x in KAPALI): H.append("esmâ kural adı kapalı liste dışı %s: '%s'" % (k, kad.split(' → ')[0][:50]))
    sg = re.search(r'%s .*?(?=\d+:\d+:\d+ |$)' % re.escape(k), esm_it)
    if sg and 'tam okuma sonu' in sg.group(0): H.append("esmâ kararı 'tam okuma sonu' notlu ama esma_el'de kapalı: %s" % k)
    kural = next((x for x in KW if x in yorum), None)
    onc = [(kk, c) for kk, c in ONCE.get((LEM.get(k), kr), []) if kk != k and not (kk.startswith('%d:' % S) and A <= int(kk.split(':')[1]) <= B)]
    yapi = re.sub(r"^'+", '', yorum.split()[0])[:8] if yorum.split() else ''
    ayni = [(kk, c) for kk, c in onc if yapi and yapi in c.replace("'", "'")]  # emsal: aynı yapıyla başlayan önceki kayıtlar (örn. 'fi'l-âxira')
    if ayni: onc = ayni
    sifat = kural == 'esmâ adı esmâ dışı göndergeyle' and re.search(r'\bsıfatı\b', yorum) and any(re.search(r'\bsıfatı\b', c) for kk, c in onc)  # bölüm 15 denetimi kuralı 9: kelime sınırı ('sıfatımız' geçmez)  # bölüm 9: emsal 'X'in sıfatı' (esmâ dışı ismin sıfatı) kayıt kendi yorumunda da sıfatı anıyorsa eş
    if kural and onc and not sifat and not any(re.search(KW[kural], c) for kk, c in onc):
        ornek = re.sub(r'\(?\b\d+:\d+(?::\d+)?\b[^)]*\)?', '', onc[-1][1]).strip()
        H.append("esmâ kural sapması %s: genel kural '%s' / önceki kayıtlarda emsal ('%s'; %d kayıt)" % (k, kural, ornek[:60], len(onc)))
print('esmâ kural emsali: %d kayıt' % E14)
# ── (16) lemma dizisi adında joker ──
D2 = {}
for blok in open('/home/claude/b%s/say2.txt' % NN, encoding='utf-8').read().split('### ')[1:]:
    h = blok.split('\n')[0].strip()
    m = re.search(r'lemma dizisi (\[.*?\]) \|', blok)
    if h.startswith('dizi') and m: D2[h] = ast.literal_eval(m.group(1))
J = 0
for f in ('metin_yap.py', 'ariza_yap.py'):
    src = open('/home/claude/b%s/yap/%s' % (NN, f), encoding='utf-8').read()
    for key, ad in re.findall(r"""['"](dizi \d+ \d+ \d+ \d+)['"],\s*"([^"]+)\"""", src):
        if key not in D2: continue
        J += 1; el = D2[key]; tk = ad.split()
        bos = [i for i, e in enumerate(el) if not e]
        if len(tk) != len(el) or any(tk[i] != '_' for i in bos):
            H.append("lemma dizisi adı '%s' (%s): öğe %d, ad %d%s" % (ad, key, len(el), len(tk), ('; joker konumu %s' % ', '.join(str(i + 1) for i in bos)) if bos else ''))
print('lemma dizisi adı: %d' % J)
# ── (7) yapıştırılmış araç çıktısı tazeliği ──
if TAZE:
    T = []
    T += [l for l in run('/home/claude/sunum/gloss_tara.py', str(A), str(B), NN).splitlines() if l.strip()]
    T += [l for l in run('/home/claude/sunum/es_edat.py', NN).splitlines() if l.strip()]
    T += [l for l in run('/home/claude/sunum/bolum5_kurallar.py', str(A), str(B), NN).splitlines() if l.startswith(('ham LEM: ad', 'tetik dışı aday', 'meal takdiri:'))]
    tum = ' '.join(ITEMS)
    for l in T:
        if l not in tum: H.append('bayat araç çıktısı: %s' % l[:90])
    print('araç çıktısı tazeliği: %d satır' % len(T))
for h in H: print('HATA', h)
print('bolum6_kurallar hata:', len(H))

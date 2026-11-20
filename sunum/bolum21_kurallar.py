# sûre 6 bölüm 5 denetimi araç kuralları (bekleyen_ariza_6_b11.txt 2. öğe) — salt okur:
#  (1) ES_EDAT_KARAR: es_edat satırında birden çok karşılığı olan her başlık ('X' (ETİKET) — …) 'meal karşılık farkı kararları' maddesinde "'X' — <kapalı karar>" ile
#  (2) KOK_UYE_TAM: cakisma.py KÖK grubundaki her Arapça üye, 'karşılık çakışması' maddesindeki o KÖK kararında tırnaklı olarak geçer
#  (3) D1_MORPH_ESIT: ◇ / D1'de 'edilgen ortaç' yalnız ayette morph PASS_PCPL, 'etken ortaç' yalnız ACT_PCPL varken
#  (4) EK_KESIM_ICI: meal maddesinde "('W' içinde" alıntısındaki W, maddenin ait olduğu kesimin Türkçe diliminde
#  (5) ADSIZ_FAIL_YOK: A1'de '(adsız; …)' girdisinde 'fail N. kelime' yazılmaz
#  (6) TEKIL_MEDDE: medde taramasında meddeli / meddesiz sayısı farklı kalıp 'korpusta 1' listesine girmez
#  (elle: KASR_KALIP, GEREKCE_SINIF_SONUC, EMSAL_KAPSAM_SINIR, LEMMA_AD_BIR, TR_YAZIM_BIR, D1_KELIME_TAM, OLCUM_ALAN_TAM (mm2), YER_TUTUCU şablon cümlesi, GERIYE_DONUK_ZORUNLU, VF_VEZIN, GONDERGE_NUMARA_HEP, KELIME_KONTROL_SEG, IZA_CEVAP genişlemesi, ORTAC_NOT)
# kullanım (/home/claude'dan): python3 sunum/bolum21_kurallar.py A B NN
import sys as _sy; _sy.path.insert(0, '/home/claude/sunum'); from sure import BK as _BK, S
import re, sys, ast, glob, subprocess, collections
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
Y = '/home/claude/yamalar/'
H = []
TUM = ast.literal_eval('{' + open(Y + 'ariza_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read() + '}')[(A, B)]
ITEMS = [m for m in TUM if not re.match(r'(bölüm (denetimi \(|\d+ denetiminden|\d+ \(sûre)|devir \()', m)]
M, MEAL = {}, {}
exec(open(Y + 'metin_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read(), {'M': M, 'MEAL': MEAL})
EN = collections.Counter()
Q = r"'((?:[^']|'(?=[a-zâîûçğışöü]))+)'"
def item(bas): return [m for m in ITEMS if m.startswith(bas)]
def satir(n, bas):
    for l in M[n].split('\n'):
        if l.startswith(bas): return l
    return ''
meal_it = ' '.join(item('meal (okuma'))

# ── (1) ES_EDAT_KARAR ──
es = meal_it.split("blok içi eş edat / zamir karşılıkları", 1)[-1].split('): ', 1)[-1].split('; eş lemmaya farklı karşılık')[0]
mk = ' '.join(item('meal karşılık farkı kararları'))
for seg in re.split(r"; (?=')", es):
    m = re.match(Q + r" \(([A-Z]+)\) — (.*)$", seg)
    if not m: continue
    kars = re.findall(r"(?:^|\), )((?:'[^']+' ile|[a-zçğıöşü ]+ eki ile|karşılıksız|[a-zçğıöşü]+ ile))", m.group(3))
    EN['es_edat'] += 1
    if len(set(kars)) > 1 and not re.search(r"'%s' — (?:çakışma değil|çakışma — tam okuma sonu)" % re.escape(m.group(1)), mk):
        H.append("(1) eş edat '%s' (%s) %d karşılık — kapalı karar yok" % (m.group(1), m.group(2), len(set(kars))))

# ── (2) KOK_UYE_TAM ──
DOS = sorted([f for f in glob.glob(Y + 'ariza_%d_*_*.txt' % S) if int(f.split('_')[-2]) <= A], key=lambda p: int(p.split('_')[-2]))
cak = subprocess.run([sys.executable, '/home/claude/sunum/cakisma.py'] + DOS, capture_output=True, text=True).stdout
cm = ' '.join(item('karşılık çakışması'))
for l in cak.splitlines():
    if not l.startswith('KÖK '): continue
    bas = "KÖK '%s' ←" % l.split()[1]
    if bas not in cm: continue
    i = cm.find(bas); j = cm.find("KÖK '", i + len(bas)); kar = cm[i:j if j > 0 else len(cm)]
    for w in re.findall(r"[\"']((?:[^\"',\]]|'(?=[a-zâîûçğışöü]))+)[\"']", l.split(' ← ', 1)[1].replace('; ', ', ')):
        if w.endswith('-') or ' ' in w: continue
        EN['kok_uye'] += 1
        if "'%s'" % w not in kar: H.append("(2) %s kararında Arapça üye '%s' yok" % (bas[:-2], w))

# ── (3) D1_MORPH_ESIT ──
MO = collections.defaultdict(str)
for l in open(_BK + 'b%s/morph.txt' % NN, encoding='utf-8'):
    p = l.split('\t')
    if len(p) > 2: MO[int(p[0].split(':')[1])] += p[2]
for a in range(A, B + 1):
    zin = M[a]
    for ad, et in (('edilgen ortaç', 'PASS_PCPL'), ('etken ortaç', 'ACT_PCPL')):
        EN['d1'] += 1
        n_ad = len(re.findall(r'(?<!çoğul )%s|çoğul %s' % (ad, ad), zin.split('◈D')[1] if '◈D' in zin else ''))
        if n_ad and et not in MO[a]: H.append("(3) %d:%d D1'de '%s' — morph %s yok" % (S, a, ad, et))

# ── (4) EK_KESIM_ICI ──
for m in re.finditer(r"%d:(\d+) (.*?)(?=; %d:\d+ '|; blok içi eş edat|$)" % (S, S), meal_it):
    for k in re.finditer(r"'((?:[^']|'(?=[a-zçğıöşüâîû]))+)' \('(?:[^']|'(?=[a-zâîûçğışöü]))+', (.*?)\)(?=; '|$)", m.group(2)):
        tr, its = k.group(1), k.group(2)
        for w in re.findall(r"\('((?:[^']|'(?=[a-zçğıöşü]))+)' içinde", its):
            EN['kesim'] += 1
            if w not in tr: H.append("(4) %s:%s '%s' içerici kesim dışında (kesim: '%s')" % (S, m.group(1), w, tr[:40]))

# ── (5) ADSIZ_FAIL_YOK ──
for a in range(A, B + 1):
    a1 = satir(a, '◈A')
    for g in re.findall(r"\(adsız;[^()]*(?:\([^()]*\)[^()]*)*\)", a1):
        EN['adsiz'] += 1
        if re.search(r'— fail \d+\. kelime', g): H.append("(5) %d:%d adsız girdide 'fail N. kelime': %s" % (S, a, g[:70]))

# ── (6) TEKIL_MEDDE ──
md = ' '.join(m for m in ITEMS if 'medde taraması' in m)
FARK = {k for k, x, y in re.findall(r"((?:say|dizi) [^;()]+?) meddeli (\d+) / meddesiz (\d+)", md) if x != y}
k1 = ' '.join(item('korpusta 1')).split('): ', 1)[-1]
for k in [x.strip() for x in k1.split(', ')]:
    EN['k1'] += 1
    if k in FARK: H.append("(6) '%s' korpusta 1 listesinde — medde farkı var" % k)

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum21_kurallar hata: %d' % len(H))

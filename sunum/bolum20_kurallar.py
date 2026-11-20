# sûre 6 bölüm 4 denetimi araç kuralları (bekleyen_ariza_6_b09.txt 2. öğe) — salt okur:
#  (1) YER_TUTUCU_KALMADI: ARIZA ve metin yamasında doldurulmamış yer tutucu ('X_P', 'KHATA_X', 'BN_HEPSI', 'AYN_SONUC', 'TETIKDISI', 'MUT_SONUC', 'ANILIS_YOK') kalmaz; '(geçici)' ara geçişte okunduğundan desende yok, son kayıtta elle taranır
#  (2) EK_ALT_DIZE: meal maddesinde "'-x' ile ('Y' içinde" ve "'-x' takdiri ('Y' içinde" biçimindeki ek (tireler atılmış) Y'nin alt dizesi
#  (3) HAZIF_SOZDIZIMI: A4'te 'cevap hazif' yazılan her COND sözdizimi maddesinde 'cevap mahzuf (S:a N. kelime)' kaydıyla
#  (4) GONDERGE_BICIM_SIKI: A1'de 'gönderge' ardından 'S:a N. kelime', 'lafız' ya da tırnaklı alıntı gelir (rol adı — 'gönderge elçi' — ya da numarasız ayet anışı kabul edilmez)
#  (5) KIP_IMPV: D2'deki her IMPV alıntısı kip notunda o ayetin kesiminde "'x' IMPV" diye anılır
#  (6) ADAY1039_ARASI: ◇'de 'ayetler arası:' ardından 'yok' dışında içerik varsa ARIZA aday 1039 maddesi 'ayetler arası çift ARIZA 0 / ◇ 0' diyemez
#  (elle: KAYIT_ESIT_YAMA, CAKISMA_TUTARLI, LEMMA_AD_BIR, KOK_UYE_TAM, ES_EDAT_KARAR, KIP_MEAL_EK, OLCUM_ALAN_TAM, TETIK_FIIL_NOT, REM_CEVAP, A4_KAPALI, KELIME_KONTROL_SEG, KASR_KALIP)
# kullanım (/home/claude'dan): python3 sunum/bolum20_kurallar.py A B NN
import sys as _sy; _sy.path.insert(0, '/home/claude/sunum'); from sure import BK as _BK, S
import re, sys, ast, collections
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
Y = '/home/claude/yamalar/'
H = []
HAM = open(Y + 'ariza_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read()
TUM = ast.literal_eval('{' + HAM + '}')[(A, B)]
ITEMS = [m for m in TUM if not re.match(r'(bölüm (denetimi \(|\d+ denetiminden|\d+ \(sûre)|devir \()', m)]
MHAM = open(Y + 'metin_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read()
M, MEAL = {}, {}
exec(MHAM, {'M': M, 'MEAL': MEAL})
EN = collections.Counter()
def satir(n, bas):
    for l in M[n].split('\n'):
        if l.startswith(bas): return l
    return ''
def item(bas): return [m for m in ITEMS if m.startswith(bas)]
def kesim(txt, a):  # 'S:a …' kesimi: sonraki 'S:b ' başlangıcına dek
    m = re.search(r'(?<![\d:])%d:%d (.*?)(?=(?:; |, | )%d:\d+ |$)' % (S, a, S), txt)
    return m.group(1) if m else ''

# ── (1) YER_TUTUCU_KALMADI ──
YT = re.compile(r"\b(?:[A-Z0-9]+_P|KHATA_[A-Z]+|B\d+_HEPSI|AYN_SONUC|TETIKDISI|MUT_SONUC|ANILIS_YOK|KARSILIK_CAKISMA)\b")  # '(geçici)' ara geçiş metni koşu içinde okunur — son kayıt elle taranır (sûre 6 blok 10)
for ad, t in (('ARIZA', HAM), ('metin', MHAM)):
    EN['yt'] += 1
    for m in sorted(set(YT.findall(t))): H.append("(1) %s yamasında yer tutucu kaldı: %s" % (ad, m))

# ── (2) EK_ALT_DIZE ──
ml = ' '.join(item('meal (okuma'))
for m in re.finditer(r"'(-[a-zçğıöşüâîû]+-?)' (?:ile|takdiri) \('([^']+(?:'[a-zçğıöşü]+)?)' içinde", ml):
    EN['ek'] += 1
    ek, y = m.group(1).strip('-'), m.group(2)
    if ek not in y: H.append("(2) ek '%s' içerici '%s' alt dizesi değil" % (m.group(1), y))

# ── (3) HAZIF_SOZDIZIMI ──
sz = ' '.join(item('sözdizimi'))
for a in range(A, B + 1):
    for m in re.finditer(r"COND '[^']+' (\d+)\. kelime: [^)]*?— cevap hazif", satir(a, '◈A')):
        EN['hazif'] += 1
        if 'cevap mahzuf (%d:%d %s. kelime)' % (S, a, m.group(1)) not in sz:
            H.append("(3) %d:%d %s. kelime A4 cevap hazif — sözdizimi maddesinde 'cevap mahzuf (%d:%d %s. kelime)' yok" % (S, a, m.group(1), S, a, m.group(1)))

# ── (4) GONDERGE_BICIM_SIKI ──
for a in range(A, B + 1):
    a1 = re.search(r'A1 (.*?)(?:; aktör|; A2 |$)', satir(a, '◈A'))
    for m in re.finditer(r"gönderge (.{0,40})", a1.group(1) if a1 else ''):
        EN['gonderge'] += 1
        g = m.group(1)
        if not re.match(r"(?:\d+:\d+ \d+\. kelime|lafız\b|')", g):  # rol adı ('gönderge elçi') ya da numarasız ayet anışı kabul edilmez
            H.append("(4) %d:%d A1 gönderge biçimi: 'gönderge %s'" % (S, a, g[:30]))

# ── (5) KIP_IMPV ──
kip = ' '.join(m[m.index('kip notu ('):] for m in ITEMS if 'kip notu (' in m)
for a in range(A, B + 1):
    d2 = re.search(r'IMPV \(([^)]*)\)', satir(a, '◈D'))
    if not d2: continue
    ks = kesim(kip, a)
    for q in re.findall(r"'([^']+)' \d+\. kelime", d2.group(1)):
        EN['impv'] += 1
        if "'%s' IMPV" % q not in ks: H.append("(5) %d:%d IMPV '%s' kip notunda yok" % (S, a, q))

# ── (6) ADAY1039_ARASI ──
dolu = [a for a in range(A, B + 1) if re.search(r'ayetler arası: (?!yok)', M[a])]
ad_ = ' '.join(item('aday 1039'))
EN['aday'] += 1
if dolu and 'ayetler arası çift ARIZA 0 / ◇ 0' in ad_:
    H.append("(6) ◇ ayetler arası çift var (%s) — aday 1039 maddesi 'ARIZA 0 / ◇ 0' diyor" % ', '.join('%d:%d' % (S, a) for a in dolu))

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum20_kurallar hata: %d' % len(H))

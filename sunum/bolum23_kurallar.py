# sûre 6 bölüm 7 denetimi araç kuralları (bekleyen_ariza_6_b15.txt 2. öğe) — kural 2 esma_kayit.py koşar (esma_kayit.json'a atomik yazar; salt okur değil):
#  (1) ALINTI_ALTDIZE_ESMA: ARIZA 'esmâ:' maddesindeki 'S:a 'X'' alıntıları o ayetin ◇ transliterasyonunun alt dizesi
#  (2) ESMA_DUR_KAYIT: esma_kayit e_el=? > 0 ya da esmâ maddesinde 'kapalı listede kural yok' varsa maddede 'soruldu' / 'kullanıcı kararı:' kaydı bulunur; gerekçe adı '/' ile çift olmaz
#  (3) BASKIN_TOPLAM: ölçüm şahıs alanında kişi toplamı (1 / 2 / 3) eşitse ya da en yüksek kişi ölçüm 'baskın'dan farklıysa ◈A A4'te 'beraberlik' notu
#  (4) DIZI_AD_LEMMA: ◇'deki 'Lemma dizisi 'X'' adı say2 dizi demetiyle öğe sayısında eş; öğe 'bi-' / 'fe-' / 've-' önekiyle başlamaz
#  (5) SORU_CEVAP_A4: ARIZA A4 maddesinde 'S:a sorusu S:b'te … yanıtlanıyor' okuması varsa S:b A4'ünde 'soru → cevap'
# (elle: GERIYE_DONUK_TAZE, GEVSEME_FARK, SOZ_BICIMLI_IC, SOZ_SINIR_REM, ILERI_GONDERGE, MEAL_TAKDIR_TAM, CAKISMA_TUTARLI, ELA_YAZIM, YILDIZ_KAYNAK_CELISKI, KELIME_KONTROL_SEG)
# kullanım (/home/claude'dan): python3 sunum/bolum23_kurallar.py A B NN
import sys as _sy; _sy.path.insert(0, '/home/claude/sunum'); from sure import BK as _BK, S
import re, sys, ast, os, subprocess, collections
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

# ── (1) ALINTI_ALTDIZE_ESMA ──
es = ' '.join(item('esmâ:'))
for m in re.finditer(r"(?<![\d:])%d:(\d+) %s \(\d" % (S, Q), es):
    n, q = int(m.group(1)), m.group(2)
    if not A <= n <= B: continue
    EN['esma_alinti'] += 1
    if q not in dia(n): H.append("(1) %d:%d esmâ alıntısı '%s' ◇ alt dizesi değil" % (S, n, q))

# ── (2) ESMA_DUR_KAYIT ──
try:
    ek = subprocess.run([sys.executable, 'esma_kayit.py', str(S), str(A), str(B)], capture_output=True, text=True, cwd='/home/claude/calisma').stdout
except Exception: ek = ''
if not re.search(r'^%d:%d ' % (S, A), ek, re.M): H.append('(2) esma_kayit.py çıktısı boş ya da eksik (%d:%d satırı yok) — denetim sessiz geçmez' % (S, A))  # sûre 6 bölüm 8 denetimi
bekl = len(re.findall(r'e_el=\?', ek))
EN['esma_dur'] += 1
if (bekl or 'kapalı listede kural yok' in es) and not re.search(r'kullanıcı kararı(?:yla|:| \()|soruldu', es):
    H.append("(2) esmâ kararı kapalı liste dışı / e_el=? %d — esmâ maddesinde 'kullanıcı kararı' kaydı yok" % bekl)
for m in re.finditer(r"— ([^;—]*?/[^;—]*?); kapalı listede kural yok", es):
    H.append("(2) esmâ gerekçe adı çift: '%s'" % m.group(1).strip()[:50])

# ── (3) BASKIN_TOPLAM ──
olc = [x for x in open(_BK + 'b%s/olcum.txt' % NN, encoding='utf-8').read().split('\n\n') if x.strip()]
for a in range(A, B + 1):
    if a - A >= len(olc): break
    m = re.search(r'şahıs (.*?), sahset.*?baskın (\d)', olc[a - A].replace('**', ''))
    if not m: continue
    top = collections.Counter()
    for p, c in re.findall(r'([123])[MF]?[SPD] (\d+)', m.group(1)): top[p] += int(c)
    if not top: continue
    mx = max(top.values()); ust = sorted(p for p, c in top.items() if c == mx)
    EN['baskin'] += 1
    if (len(ust) > 1 or ust[0] != m.group(2)) and 'beraberlik' not in satir(a, '◈A'):
        H.append("(3) %d:%d kişi toplamı %s / ölçüm baskın %s — A4'te 'beraberlik' notu yok" % (S, a, ' · '.join('%s: %d' % kv for kv in sorted(top.items())), m.group(2)))

# ── (4) DIZI_AD_LEMMA ──
S2 = {}
if os.path.exists(_BK + 'b%s/say2.txt' % NN):
    for b in open(_BK + 'b%s/say2.txt' % NN, encoding='utf-8').read().split('### ')[1:]:
        h = b.split('\n', 1)[0].strip(); dm = re.search(r"lemma dizisi (\[.*?\]) \|", b)
        if h.startswith('dizi ') and dm:
            try: S2[h] = ast.literal_eval(dm.group(1))
            except Exception: pass
MB = _BK + 'b%s/yap/metin_body.py' % NN
CAG = re.findall(r"say\('(dizi [^']+)', \"([^\"]+)\"", open(MB, encoding='utf-8').read()) if os.path.exists(MB) else []
for k, ad in CAG:
    if k not in S2: continue
    EN['dizi_ad'] += 1
    t = ad.split()
    if len(t) != len(S2[k]): H.append("(4) %s adı '%s' %d öğe / dizi %d" % (k, ad, len(t), len(S2[k])))
    for x in t:
        if re.match(r'(?:bi|fe|ve)-', x): H.append("(4) %s adı '%s' öğesi '%s' önekli — dizi lemmasında önek yok" % (k, ad, x))

# ── (5) SORU_CEVAP_A4 ──
a4 = ' '.join(item('◈A A4'))
for m in re.finditer(r"%d:(\d+) sorusu %d:(\d+)'[dt]e [^;]*?yanıtlanıyor" % (S, S), a4):
    b = int(m.group(2)); EN['soru_cevap'] += 1
    if A <= b <= B and 'soru → cevap' not in satir(b, '◈A'): H.append("(5) %d:%d A4'te 'soru → cevap' yok (ARIZA: %d:%s sorusu burada yanıtlanıyor)" % (S, b, S, m.group(1)))

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum23_kurallar hata: %d' % len(H))

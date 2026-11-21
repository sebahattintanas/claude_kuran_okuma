# sûre 6 bölüm 8 denetimi araç kuralları (bekleyen_ariza_6_b17.txt 2. öğe) — salt okur:
#  (1) ARALIK_KONUM_SINA: ◇ satırlarında "'Q' (N. kelime)" alıntısı (Q ◇'de bir kez) — bolum22 aralik() başlangıcı N; aralık ayetin morph kelime sayısını aşmaz
#  (2) DENETIM_BOS_CIKTI: esma_kayit.py ve esma_muhur.py bu blok için boş olmayan çıktı verir (blok her ayeti için satır); bolum8 (3), bolum15 (5), bolum23 (2) boş çıktıda isabet verir
#  (3) SOZ_ATIF_SURER: ayetin son kelimesinde 'söz kapanır' ve sonraki ayetin 1. kelimesi morph CONJ (REM değil) ise sonraki ayet A3'ü '—' olamaz ya da A4'te 'söz kapanışı gerekçesi' bulunur
#  (4) GONDERGE_UYUM: A1 "S:a … 3MS|3FS (… gönderge 'X' N. kelime" — tekil zamir, tekil gönderge (morph MS / FS ya da sayısız M / F): cinsiyet uyuşur; uyuşmazsa kayıtta 'tartışmalı'; gönderge zamirin kendi kelimesi olamaz (çoğul gönderge — akılsız çoğul / topluluk — denetim dışı)
#  (5) ESMA_KARAR_DOSYA: ARIZA esmâ maddesinde anılan 'yamalar/esma_el_*.txt' dosyası var ve maddenin aynı kesiminde anılan S:a anahtarını taşır; esma_el yorumlarında blok numarası yok
# (elle: GERIYE_SINIF, ARAC_SIZINTI, SOZ_ICI_KONUSAN, ESMA_TAKDIRI_ZAMIR, YILDIZ_ESIK, BERABERLIK_AD)
# kullanım (/home/claude'dan): python3 sunum/bolum24_kurallar.py A B NN
import sys as _sy; _sy.path.insert(0, '/home/claude/sunum'); from sure import BK as _BK, S
import re, sys, ast, os, subprocess, collections, glob
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
MOR = collections.defaultdict(dict)
_mf = _BK + 'b%s/morph.txt' % NN
if os.path.exists(_mf):
    for l in open(_mf, encoding='utf-8'):
        p = l.rstrip('\n').split('\t')
        if len(p) >= 3:
            s_, a_, w_ = p[0].split(':')[:3]
            if int(s_) == S: MOR[int(a_)][int(w_)] = p[2]
# bolum22 aralik() — aynı işlev (kopya değil, kaynaktan)
_src = open('/home/claude/sunum/bolum22_kurallar.py', encoding='utf-8').read()
_g = {'re': re, 'dia': dia}
exec(_src[_src.index('def kelime(q):'):_src.index('for b_ in BAG:')], _g)
aralik = _g['aralik']

# ── (1) ARALIK_KONUM_SINA ──
for n in range(A, B + 1):
    d = dia(n); nk = len(MOR.get(n, {}))
    for l in M[n].split('\n')[1:]:
        if not l.startswith(('◈K', '◈B')): continue
        for q, k in re.findall(Q + r" \((\d+)\. kelime\)", l):
            if d.count(q) != 1: continue
            r = aralik(n, q); EN['aralik'] += 1
            if not r: continue
            if r[0] != int(k): H.append("(1) %d:%d '%s' kayıt %s. kelime / aralik() %d" % (S, n, q, k, r[0]))
            if nk and r[1] > nk: H.append("(1) %d:%d '%s' aralık %d-%d ayet kelime sayısını (%d) aşıyor" % (S, n, q, r[0], r[1], nk))

# ── (2) DENETIM_BOS_CIKTI ──
_ek = subprocess.run([sys.executable, 'esma_kayit.py', str(S), str(A), str(B)], capture_output=True, text=True, cwd='/home/claude/calisma').stdout
for n in range(A, B + 1):
    EN['bos_cikti'] += 1
    if not re.search(r'^%d:%d ' % (S, n), _ek, re.M): H.append('(2) esma_kayit.py çıktısında %d:%d satırı yok' % (S, n))
_em = subprocess.run([sys.executable, '/home/claude/sunum/esma_muhur.py', str(A), str(B), NN], capture_output=True, text=True).stdout
if not _em.strip(): H.append('(2) esma_muhur.py çıktısı boş')
for f, isaret in (('bolum8_kurallar.py', 'esma_muhur.py çıktısı boş'), ('bolum15_kurallar.py', 'esma_muhur.py çıktısı boş'), ('bolum23_kurallar.py', 'esma_kayit.py çıktısı boş')):
    if isaret not in open('/home/claude/sunum/' + f, encoding='utf-8').read(): H.append('(2) %s boş çıktıda isabet vermiyor' % f)

# ── (3) SOZ_ATIF_SURER ──
for n in range(A, B):
    nk = len(MOR.get(n, {}))
    a4 = satir(n, '◈A')
    if not nk or not re.search(r'söz kapanır \(%d\. kelime' % nk, a4): continue
    f1 = MOR.get(n + 1, {}).get(1, '')
    EN['soz_atif'] += 1
    if re.match(r'P\|CONJ\|PREF', f1):
        s2 = satir(n + 1, '◈A')
        a3 = s2.split('A3 ', 1)[1].split('; A4', 1)[0] if 'A3 ' in s2 else ''
        if a3.strip(' ;') == '—' and 'söz kapanışı gerekçesi' not in s2:
            H.append("(3) %d:%d söz %d. kelimede kapanıyor, %d:%d 1. kelime morph CONJ — %d:%d A3 '—' ve kapanış gerekçesi yok" % (S, n, nk, S, n + 1, S, n + 1))

# ── (4) GONDERGE_UYUM ──
for n in range(A, B + 1):
    a1 = satir(n, '◈A')
    a1 = a1[a1.find('A1 '):a1.find('; A2 ')] if 'A1 ' in a1 else ''
    for m in re.finditer(r"((?:'[^;]*?' ?,? ?)+) 3(M|F)S \(([^)]*?)gönderge " + Q + r" (\d+)\. kelime(?:, (\d+)\. kelime)?", a1):
        cins, qq, gn, kn = m.group(2), m.group(4), int(m.group(5)), m.group(6)
        EN['gonderge'] += 1
        if kn and int(kn) == gn: H.append("(4) %d:%d gönderge '%s' zamirin kendi kelimesi (%d)" % (S, n, qq, gn))
        feat = MOR.get(n, {}).get(gn, '')
        gm = [] if re.search(r'\|[MF]?[PD]\|', feat + '|') else re.findall(r'\|(M|F)S?\|', feat + '|')
        if gm and cins not in gm and 'tartışmalı' not in m.group(0):
            H.append("(4) %d:%d 3%s zamir göndergesi '%s' (%d. kelime) morph %s — 'tartışmalı' notu yok" % (S, n, cins, qq, gn, '/'.join(sorted(set(gm)))))
    for m in re.finditer(r"3(M|F)S \([^)]*?gönderge %d:(\d+) (\d+)\. kelime" % S, a1):
        cins, ga, gn = m.group(1), int(m.group(2)), int(m.group(3))
        EN['gonderge'] += 1
        feat = MOR.get(ga, {}).get(gn, '')
        gm = [] if re.search(r'\|[MF]?[PD]\|', feat + '|') else re.findall(r'\|(M|F)S?\|', feat + '|')
        if gm and cins not in gm and 'tartışmalı' not in m.group(0):
            H.append("(4) %d:%d 3%s zamir göndergesi %d:%d %d. kelime morph %s — 'tartışmalı' notu yok" % (S, n, cins, S, ga, gn, '/'.join(sorted(set(gm)))))

# ── (5) ESMA_KARAR_DOSYA ──
for es in item('esmâ:'):
    for kes in re.split(r'; (?=%d:)' % S, es):
        for f in re.findall(r'yamalar/(esma_el_[\w]+\.txt)', kes):
            EN['esma_dosya'] += 1
            if not os.path.exists(Y + f): H.append('(5) esmâ maddesi %s anıyor, dosya yok' % f); continue
            t = open(Y + f, encoding='utf-8').read()
            for a_ in re.findall(r'(?<![\d:])%d:(\d+) ' % S, kes):
                if "'%d:%s:" % (S, a_) not in t: H.append("(5) esmâ maddesi %d:%s kaydını %s'e bağlıyor, dosyada anahtar yok" % (S, a_, f))
for f in glob.glob(Y + 'esma_el_%d_*.txt' % S):
    for l in open(f, encoding='utf-8'):
        if re.search(r"^\s*'%d:(\d+):" % S, l) and re.search(r'blok \d+', l.split('#', 1)[-1]):
            m_ = re.search(r"'%d:(\d+):" % S, l)
            if A <= int(m_.group(1)) <= B or f.endswith('_%d_%d.txt' % (A, B)): H.append('(5) %s yorumunda blok numarası: %s' % (os.path.basename(f), l.strip()[:60]))

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum24_kurallar hata: %d' % len(H))

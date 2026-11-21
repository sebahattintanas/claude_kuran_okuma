# sûre 6 bölüm 9 denetimi araç kuralları (bekleyen_ariza_6_b19.txt 2. öğe) — salt okur:
#  (1) SOZ_BICIMLI_ARALIK: A3 '(söz biçimli içerik' taşıyan ayet için ARIZA söz / tırnak maddesinde 'S:a … söz biçimli içerik N-M. kelime' aralığı var; aynı maddede 'REM sapması S:a (' ile 'S:a söz içi REM: yok' birlikte olamaz
#  (2) MORPH_PASS_CELISKI: morph PASS etiketli kelimeyi anan A1 kesiminde 'naib-i fail' ile 'etken' birlikte geçemez; ◇ ölçüm EDİLGEN satırını alıntılıyor ve PASS kelimesi okumada etken sayılıyorsa ◇'de 'morph etiketi kaynaklı' notu
#  (3) JOKER_TUM: ◇ ve ARIZA nakarat3 kalıp adlarında bütün öğeleri '_' olan ad yok
#  (4) OLCUM_MM2: ölçüm satırında 'mm2:' alanı olan ayetin ◇ satırı 'mm2' alanını anar
#  (5) SOZDIZIMI_CEVAP_A4: ARIZA sözdizimi maddesinde 'cevap' / 'cevabı' geçen ayet kesiminin A4'ünde 'şart → cevap' ya da 'kapsam dışı' kaydı
# (elle: SOZ_SURER_AYETLER_ARASI, GONDERGE_MEAL_UYUM, KOSUL_CEVAP_SIRA, ESMA_ADJ_NOT, SEG_IC_CELISKI, EMSAL_MEAL_KALIP, NEKRE_BELIRTME)
# kullanım (/home/claude'dan): python3 sunum/bolum25_kurallar.py A B NN
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

def a_parca(n, k):
    l = satir(n, '◈A')
    i = l.find(k + ' ')
    if i < 0: return ''
    j = min([x for x in (l.find(' A%d ' % (int(k[1]) + 1), i),) if x > 0] or [len(l)])
    return l[i + 3:j]
ARM = ' '.join(ITEMS)
def ayet_kesim(txt, n):
    out = []
    for p in re.split(r'; (?=%d:\d+ )' % S, txt):
        if re.match(r'%d:%d ' % (S, n), p): out.append(p)
    return ' '.join(out)

# ── (1) SOZ_BICIMLI_ARALIK ──
SZ = ' '.join(item('söz / tırnak'))
for n in range(A, B + 1):
    if '(söz biçimli içerik' not in a_parca(n, 'A3'): continue
    EN['soz_bicimli'] += 1
    if not re.search(r"%d:%d [^;]*?söz biçimli içerik (\d+)-(\d+)\. kelime" % (S, n), SZ):
        H.append("(1) %d:%d A3 söz biçimli içerik — ARIZA söz / tırnak maddesinde 'söz biçimli içerik N-M. kelime' aralığı yok" % (S, n))
    if re.search(r'REM sapması %d:%d \(' % (S, n), SZ) and re.search(r'(?<![\d:])%d:%d söz içi REM: yok' % (S, n), SZ):
        H.append("(1) %d:%d söz maddesi 'REM sapması' yazıyor, araç çıktısı 'söz içi REM: yok' — çelişki" % (S, n))

# ── (2) MORPH_PASS_CELISKI ──
for n in range(A, B + 1):
    a1 = a_parca(n, 'A1'); d0 = M[n].split('\n')[0]
    for w, ft in sorted(MOR.get(n, {}).items()):
        if '|PASS|' not in ft + '|': continue
        EN['pass'] += 1
        for p in a1.split('; '):
            if re.search(r'(?<!\d)%d\. kelime' % w, p) and 'naib-i fail' in p and 'etken' in p:
                H.append("(2) %d:%d %d. kelime morph PASS — A1 kesimi 'naib-i fail' ile 'etken' birlikte: %s" % (S, n, w, p[:80]))
        if 'EDİLGEN' in d0 and re.search(r'(?<!\d)%d\. kelime\)? morph PASS[^;]*etken' % w, d0 + ' ' + a1) and 'morph etiketi kaynaklı' not in d0:
            H.append("(2) %d:%d ◇ ölçüm EDİLGEN alıntılıyor, %d. kelime okumada etken — ◇'de 'morph etiketi kaynaklı' notu yok" % (S, n, w))

# ── (3) JOKER_TUM ──
for n in range(A, B + 1):
    for q in re.findall(r"nakarat3 kalıb(?:ı|ları): ((?:'[^']*' süzgeç GEÇ(?:ER|MEZ),? ?)+)", M[n].split('\n')[0]):
        for ad in re.findall(r"'([^']*)' süzgeç", q):
            EN['joker'] += 1
            if ad.strip() and all(t == '_' for t in ad.split()): H.append("(3) %d:%d ◇ nakarat3 adı '%s' — bütün öğeler joker" % (S, n, ad))
NK = ' '.join(item('nakarat3 (R3'))
for m in re.finditer(r"(?:'(_(?: _)*)')", NK):
    EN['joker'] += 1
    H.append("(3) ARIZA nakarat3 adı '%s' — bütün öğeler joker" % m.group(1))

# ── (4) OLCUM_MM2 ──
_of = _BK + 'b%s/olcum.txt' % NN
if os.path.exists(_of):
    _ob = [b_ for b_ in open(_of, encoding='utf-8').read().split('\n\n') if b_.strip()]
    for k_, n in enumerate(range(A, B + 1)):
        if k_ >= len(_ob): break
        if 'mm2:' not in _ob[k_]: continue
        EN['mm2'] += 1
        if 'mm2' not in M[n].split('\n')[0]: H.append("(4) %d:%d ölçüm 'mm2:' alanı ◇'de anılmıyor" % (S, n))

# ── (5) SOZDIZIMI_CEVAP_A4 ──
SD = ' '.join(item('sözdizimi (okuma'))
for n in range(A, B + 1):
    ks = ' '.join(p for p in re.split(r'; (?=%d:\d)' % S, SD) if re.match(r'%d:(?:\d+(?:, |, ve | ve |-))*%d(?!\d)' % (S, n), p) or re.match(r'%d:(\d+)-(\d+) ' % S, p) and int(re.match(r'%d:(\d+)-(\d+) ' % S, p).group(1)) <= n <= int(re.match(r'%d:(\d+)-(\d+) ' % S, p).group(2)))
    if not re.search(r'cevap|cevabı', ks): continue
    EN['sozdizimi_cevap'] += 1
    a4 = a_parca(n, 'A4')
    if 'şart → cevap' not in a4 and 'kapsam dışı' not in a4:
        H.append("(5) %d:%d sözdizimi maddesi 'cevap' diyor — A4'te 'şart → cevap' ya da 'kapsam dışı' yok" % (S, n))

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum25_kurallar hata: %d' % len(H))

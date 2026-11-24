# bölüm 4 (sûre 5) denetimi kuralları 1, 2 (A4 şart), 9 (adsız), 10 (simetri / İÇ düğüm alanı), bölüm 3 kuralları 2-4 (A4, ◈ alt sınıf, aralık) — betik denetimi
# bölüm 5 kuralları 1 / 14: her zamir etiketi (1P … 3FP) ad ölçütüyle; REM taraması başlangıç kelimesi dahil
# kullanım (/home/claude'dan): python3 sunum/bolum4_kurallar.py A B NN   → yamalar/metin_<S>_A_B.txt + ariza + bNN/morph.txt + bNN/olcum.txt
import sys as _sy; _sy.path.insert(0, '/home/claude/sunum'); from sure import BK as _BK
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from sure import S
import re, sys
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
Y = '/home/claude/yamalar/'
M = {}; exec(open(Y + 'metin_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read(), {'MEAL': {}, 'M': M})
MOR, ROOT = {}, {}
for l in open(_BK + 'b%s/morph.txt' % NN, encoding='utf-8'):
    k, w, f = l.rstrip('\n').split('\t'); _, a, n = k.split(':'); a, n = int(a), int(n)
    MOR[(a, n)] = f; r = re.search(r'ROOT:([^|]+)', f)
    if r: ROOT[(a, n)] = r.group(1)
olc = open(_BK + 'b%s/olcum.txt' % NN, encoding='utf-8').read().split('\n\n')
SINIF = {}
for c, ks in {'K1': 'سمو أرض شمس قمر نجم كوكب ليل نهر فلك سحب روح موه بحر جبل', 'K2': 'يوم أجل سنو عمر سوع دهر أبد حين',
              'B1': 'أنس دبب نعم طير نبت شجر', 'B2': 'خلق نطف علق زوج حمل وضع أنث', 'B3': 'عنق ذقن يدي عين سمع بصر جلد قلب', 'B4': 'حيي موت'}.items():
    for k in ks.split(): SINIF[k] = c
H = []
for a in range(A, B + 1):
    t = M[a]; a1 = t[t.index('◈A'):]
    # (1) REM sapması — A3 söz aralıkları içinde morph REM
    a3 = a1[a1.index(' A3 '):a1.index(' A4 ')]
    rem = []
    for i, j in re.findall(r'(\d+)-(\d+)\. kelime', a3):
        for n in range(int(i), int(j) + 1):  # bölüm 5 kuralı 1: başlangıç kelimesi dahil
            if re.match(r'P\|REM\|PREF', MOR.get((a, n), '')): rem.append(n)
    print('REM %d:%d söz içi REM: %s' % (S, a, ', '.join('%d.' % n for n in rem) if rem else 'yok'))
    # (2) A4 şart → cevap — morph COND sayısı kadar
    cond = sum(len(re.findall(r'(?:^|\|)COND(?=\|)', f)) for (aa, n), f in MOR.items() if aa == a)
    sc = a1.count('şart → cevap (ayet içi; COND')
    if cond != sc: H.append('A4 %d:%d COND %d / şart → cevap %d' % (S, a, cond, sc))
    # (9) adsız — söz içi 1P / 1S / 2MP ve söz muhatabı
    for m in re.finditer(r"(söz içi[^;]*?\(|muhatap 2M[PS] \(söz içi)[^)]*\)", a1[:a1.index(' A2 ')]):
        if 'adsız' not in m.group(0) and 'adlı' not in m.group(0) and 'lafız' not in m.group(0): H.append('adsız %d:%d %s' % (S, a, m.group(0)[:60]))
    # bölüm 5 kuralı 1 / 14: A1'deki her zamir etiketli madde (parantezsiz biçim dahil) ad ölçütü taşır
    a1b, d, cur, ITEMS = a1[a1.index('A1') + 3:a1.index(' A2 ')], 0, '', []
    for ch in a1b:
        d += (ch == '(') - (ch == ')')
        if ch == ';' and d == 0: ITEMS.append(cur); cur = ''
        else: cur += ch
    ITEMS.append(cur)
    TAG, MRK = r'(?<![A-Za-z0-9])(?:1P|1S|2MS|2FS|2MP|2FP|2D|2MD|2FD|3MS|3FS|3D|3MD|3FD|3MP|3FP)(?![A-Za-z0-9])', r'adsız|adlı aktör|fiil uyumu'  # bölüm 9 kuralı 8: açık adlı failde '(fiil uyumu; fail N. kelime)'  # bölüm 6 kuralı 15: 'lafız' / 'gönderge lafız' ölçüt yerine geçmez
    for it in ITEMS:
        subs = it.split(';')
        for k, sub in enumerate(subs):  # etiket kendi alt maddesinde ya da madde başının parantezinde ad ölçütü taşır
            if re.search(TAG, sub) and not re.search(MRK, sub) and not (k and re.search(MRK, subs[0])):
                H.append('adsız etiketi yok %d:%d %s' % (S, a, sub.strip()[:70]))
    # bölüm 9 kuralı 8: fiilin ardında açık adlı fail (NOM ad, zamir / mevsûl değil) varken fiil segmenti 'faili … adsız' / 'adsız; gönderge' yazılmaz;
    # açık ad öğesine ''X' faili' rolü verilir ya da fiil '(fiil uyumu; fail N. kelime)' biçimiyle yazılır
    a1x = a1[:a1.index(' A2 ')]
    def acik_fail(n):
        f = MOR.get((a, n), '')
        if not re.search(r'(?:^|\+ )V\|(?![^+]*PASS)[^+]*\|3[MF]S(?:\||$| )', f): return None  # etken, 3. tekil (VSO: açık fail fiilin hemen ardında)
        g = MOR.get((a, n + 1), '')
        if re.match(r'(?:P\|DET\|PREF[^+]*\+ )?N\|(?![^+]*(?:PRON|REL|DEM))[^+]*\|NOM', g): return n + 1  # 've' / 'fe' önekli ad yeni cümle
        return None
    for m in re.finditer(r"'((?![ ;(])(?:[^';()]|'(?=[a-zâîûçğışöü]))+)' (?:faili )?(?:1P|1S|2MS|2MP|3MS|3FS|3MP|3FP) \((adsız[^)]*?)(\d+)\. kelime\)", a1x):
        n = int(m.group(3)); k = acik_fail(n)
        if k is None or 'gönderge' not in m.group(2) and 'faili' not in m.group(0): continue
        if 'faili' in m.group(0) or "('%s' faili" % m.group(1) not in a1x:
            H.append("açık fail %d:%d %d. kelime '%s' (fail %d. kelime) — 'faili … adsız' yerine '(fiil uyumu; fail %d. kelime)' ya da açık ada rol" % (S, a, n, m.group(1), k, k))
    for m in re.finditer(r"'li-[^']+' \(([^)]*)\)", a1[:a1.index(' A2 ')]):
        if 'söz muhatabı, adsız' not in m.group(1): H.append('söz muhatabı %d:%d %s' % (S, a, m.group(0)[:60]))
    # ◈ alt sınıf
    for line in t.split('\n'):
        if line.startswith(('◈K', '◈B')):
            for c, body in re.findall(r'([KB]\d) ((?:[^;.]|\.(?! *$))*)', line):
                for n in re.findall(r'(\d+)\. (?:ve (\d+)\. )?kelime', body):
                    for x in n:
                        if x and SINIF.get(ROOT.get((a, int(x)))) not in (c, None): H.append('◈ %d:%d %s. kelime %s ≠ %s' % (S, a, x, c, SINIF.get(ROOT.get((a, int(x))))))
def kelime(q):  # wasl birleşmelerini ayırarak morph kelime sayısı
    n = 0
    for t in q.split():
        if t in ('ve', 'fe', 'fa', 'va', 'yâ'): continue  # ayrı yazılmış önek bağlaç morph kelimesi değil
        parca = re.split(r"(?<=[aeiuâîû])'(?=l-|ll|[a-zçğışöü]-|[bcdfğhklmnqrsştxyz]{2})", t)
        n += 1 + sum(1 for x in parca[:-1] if x not in ('ve', 'fe', 'fa', 'va', 'bi', 'li', 'le', 'ke') and not x.endswith('-'))
    return n
# aralık eşlemesi — "'… …' (i-j. kelime)" alıntısının kelime sayısı
ar = open(Y + 'ariza_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read()
for ad, txt in [('metin', '\n'.join(M.values())), ('ariza', ar)]:
    for m in re.finditer(r"(?:harekesiz|önek kesilmiş) '((?:[^'(]|'(?=[a-zâîûçğışöü]))+)' \((\d+)-(\d+)\. kelime", txt):
        q, i, j = m.group(1), int(m.group(2)), int(m.group(3))
        if '…' in q: continue
        if kelime(q) != j - i + 1: H.append('aralık %s %s (%d-%d) kelime %d' % (ad, q[:40], i, j, len(q.split())))
# bölüm 6 kuralı 1: A1 kapsamı — morph'ta şahıs etiketi taşıyan her segmentin kelimesi A1'de numarasıyla ya da ◇ alıntısıyla anılır
KISI = {}
for l in open(_BK + 'b%s/morph%d.txt' % (NN, S), encoding='utf-8'):
    loc, fo, tg, ft = l.rstrip('\n').split('\t'); s_, a_, w_, p_ = map(int, loc.split(':'))
    if A <= a_ <= B and re.search(r'(?:^|\|)[123](?:M|F)?(?:S|D|P)(?:\||$)', ft): KISI.setdefault(a_, set()).add(w_)
def kapsanan(a):
    t = M[a]; d = re.match(r"◇ '(.*?)' — ", t).group(1)
    a1 = t[t.index('A1 ') + 3:t.index(' A2 ')] if 'A1 ' in t and ' A2 ' in t else ''
    K = set()
    for m in re.finditer(r'((?:\d+(?:-\d+)?\.,? (?:ve )?)+)kelime', a1):
        for x in re.findall(r'(\d+)(?:-(\d+))?\.', m.group(1)):
            K.update(range(int(x[0]), int(x[1] or x[0]) + 1))
    for q in re.findall(r"'((?:[^']|'(?=[a-zâîûçğışöü]))+)'", a1):
        for mm in re.finditer(re.escape(q), d):
            p = mm.start(); on = d[:p]
            if on.endswith('-'): on = on[:on.rfind(' ') + 1]  # 'li-' / 'bi-' önekli kelimenin başı
            bas = kelime(on.rstrip("'")) + 1 if on.endswith("'") else kelime(on) + 1
            K.update(range(bas, bas + max(kelime(q), 1)))
    return K
for a in range(A, B + 1):
    eks = sorted(KISI.get(a, set()) - kapsanan(a))
    if eks: H.append('A1 kapsamı %d:%d şahıs etiketli kelime A1 dışında: %s' % (S, a, ', '.join('%d.' % w for w in eks)))
# bölüm 8 kuralı 7: A1'de 2. şahıs etiketi 'muhatap' sözcüğüyle yazılır (söz içi muhatap 'söz içi' ekiyle); etiketin önündeki alt madde metninde 'muhatap' aranır
for a in range(A, B + 1):
    t = M[a]; a1 = t[t.index('A1 ') + 3:t.index(' A2 ')]
    d, cur, its = 0, '', []
    for ch in a1:
        d += (ch == '(') - (ch == ')')
        if ch == ';' and d == 0: its.append(cur); cur = ''
        else: cur += ch
    its.append(cur)
    for it in its:
        m = re.search(r'(?<![A-Za-z0-9])2(?:MS|FS|MP|FP|D)(?![A-Za-z0-9])', it)
        if m and 'muhatap' not in it[:m.start()]: H.append("muhatap %d:%d 2. şahıs etiketi 'muhatap' sözcüğü olmadan: %s" % (S, a, it.strip()[:60]))
# (10) simetri / İÇ düğüm alanı olmayan ayetler
yok = ['%d:%d %s' % (S, a, ' + '.join(x for x in ('simetri', 'İÇ düğüm') if x not in olc[a - A])) for a in range(A, B + 1) if 'simetri' not in olc[a - A] or 'İÇ düğüm' not in olc[a - A]]
print('ALAN YOK: ' + ('; '.join(yok) if yok else 'yok'))
for h in H: print('HATA', h)
print('bolum4_kurallar hata:', len(H))

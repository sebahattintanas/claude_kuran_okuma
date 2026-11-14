# bölüm 13 denetimi kuralları (blok 35'ten itibaren) — betik denetimi
# kullanım (/home/claude'dan): python3 sunum/kural14.py A B NN
# (3) ◈K / ◈B satırında tetik kelimesi + kelime numarası dışında metin yok
# (4) meal maddesinde zamir / ilgi zamiri / masdar yönelme-belirtme-ayrılma ekiyle verilmişse 'fiil yönetimi takdiri' etiketi
# (5) bir Türkçe ek bir ayetin meal hesabında iki kelimeye atanmışsa 'ortak' notu
# (6) 'okunmuş bir eşte' / 'okunmuş eşte' kalıbı yok
# (7) A1'de edilgen fiil anması 'faili (adsız; edilgen' biçiminde; A4 şart → cevap alıntı / alıntı
import re, sys, ast
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
Y = '/home/claude/yamalar/'
ar = ast.literal_eval('{' + open(Y + 'ariza_4_%d_%d.txt' % (A, B), encoding='utf-8').read() + '}')[(A, B)]
M = {}; exec(open(Y + 'metin_4_%d_%d.txt' % (A, B), encoding='utf-8').read(), {'MEAL': {}, 'M': M})
sys.path.insert(0, '/home/claude/b%s/yap' % NN)
import veri
hata = 0
def H(*x):
    global hata; hata += 1; print('HATA', *x)
for n in range(A, B + 1):
    sat = M[n].split('\n')
    for s in sat:
        if s.startswith(('◈K', '◈B')):
            rest = re.sub(r"'(?:[^']|'(?=[a-zâîûçğışöü]))+' \(\d+\.(?: ve \d+\.)? kelime\)(?:, )?", '', s)
            rest = re.sub(r'^◈[KB] — ', '', rest)
            rest = re.sub(r'[KB]\d (—)?;? ?', '', rest).strip(' .;')
            if rest and rest != '—': H('(3)', n, s[:90])
ZAM = ("'kum'", "'hum'", "'hu'", "'hû'", "'hî'", "'hi'", "'hâ'", "'hunne'", "'hinne'", "'humâ'", "'himâ'", "'ke'", "'nâ'", "'ellezîne'", "'ellezî'", "'ellâtî'", "'mâ'", "'en'")
MOR = {}
for l in open('/home/claude/b%s/morph4.txt' % NN, encoding='utf-8'):
    loc, f, t, feat = l.rstrip('\n').split('\t'); s_, a, w, p_ = map(int, loc.split(':'))
    MOR.setdefault((a, w), []).append(feat)
YON = r"(?:e|a|ye|ya|ne|na|den|dan|ten|tan|nden|ndan)$"
for n in sorted(veri.MK):
    if not A <= n <= B: continue
    for tr, q, items in veri.MK[n]:
        for it in items:
            m = re.match(r"('(?:[^']|'(?=[a-zâîû]))+') (\d+)\. kelimede '([^']+)' ile", it)
            if m and m.group(1) in ZAM and re.search(YON, m.group(3).split()[-1]) and 'fiil yönetimi takdiri' not in it and not re.search(r"-s[ae]$|^diye$", m.group(3)):
                if not any(x.startswith('P|') or x.startswith('P\t') or x.split('|')[0] == 'P' for x in MOR.get((n, int(m.group(2))), [])):
                    H('(4)', n, it)
        ekler = {}
        for it in items:
            if 'karşılıksız' in it or 'ile bağlandı' in it: continue
            for e in re.findall(r"'(-[a-zçğıöşüâîû]+)-?'", it):
                ekler.setdefault(e, []).append(it)
        trl = tr.lower()
        for e, L in ekler.items():
            occ = trl.count(e[1:])
            if len(L) > max(occ, 1) and not any('ortak' in x for x in L): H('(5)', n, e, occ, ' | '.join(x[:50] for x in L))
txt = '\n'.join(M.values()) + '\n'.join(x for x in ar if not x.startswith(('bölüm denetimi', 'bölüm 1')))
for k in ('okunmuş bir eşte', 'okunmuş eşte'):
    if k in txt: H('(6)', k)
for n in range(A, B + 1):
    a1 = M[n][M[n].index('◈A'):]
    for m in re.finditer(r"'[^']+' (?:\(edilgen|faili \((?!adsız; edilgen))", a1):
        if 'edilgen' in a1[m.start():m.start() + 80] and 'faili (adsız; edilgen' not in a1[m.start():m.start() + 80]: H('(7) A1', n, a1[m.start():m.start() + 60])
    a4 = a1[a1.index(' A4 '):]
    for m in re.finditer(r"COND '[^']+' \d+\. kelime[^;)]*", a4):
        if not re.search(r": '.+' / '.+'|: '.+' — cevap", m.group(0)): H('(7) A4', n, m.group(0)[:80])
print('kural14 hata:', hata)

# meal / aday 1039 / çıpa alıntılarının ◇ transliterasyonunun alt dizesi olduğunu denetler (bölüm 7 kuralı 2)
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from sure import S
import re, ast, sys, ast
A, B = int(sys.argv[1]), int(sys.argv[2])
Y = '/home/claude/yamalar/'; suf = '_%d_%d_%d.txt' % (S, A, B)
ns = {'MEAL': {}, 'M': {}}; exec(open(Y + 'metin' + suf).read(), ns); M = ns['M']
dia = {n: re.match(r"◇ '(.*?)' — ", M[n]).group(1) for n in range(A, B + 1)}
alltr = ' | '.join(dia.values())
ar = ast.literal_eval('{' + open(Y + 'ariza' + suf).read() + '}')[(A, B)]
bad = 0
for it in ar:
    if it.startswith('meal'):
        for q in re.findall(r"' \('((?:(?!'\)).)+?)', '", it):
            if q not in alltr: bad += 1; print('meal', q)
    if it.startswith('aday 1039'):
        for q in re.findall(r"\('(.+?)' / '(.+?)'", it):
            for x in q:
                if x not in alltr: bad += 1; print('1039', x)
for n in range(A, B + 1):
    m = re.search(r"Karşıt çift \(aday 1039, okuma\): (.*?)\.\\n|Karşıt çift \(aday 1039, okuma\): (.*)$", M[n].split('\n')[0])
    t = M[n].split('\n')[0]; t = t[t.index('Karşıt çift'):]
    for x in re.findall(r"'([^']+(?:'[a-zâîû][^']*)*)'", t):
        if x not in alltr: bad += 1; print('◇1039', n, x)
# bölüm 10 denetimi kuralı 14: A4 alıntıları üç nokta taşımaz ve ◇ alt dizesidir
for n in range(A, B + 1):
    a4 = M[n][M[n].index('◈A'):]; a4 = a4[a4.index(' A4 '):]
    if '…' in a4: bad += 1; print('A4 üç nokta', n)
    for x in re.findall(r"'([^']+(?:'[a-zâîû][^']*)*)'", a4):
        if len(x.split()) >= 2 and x not in alltr and (x + "' bölümünde") not in a4:
            bad += 1; print('A4', n, x)
# bölüm 1 (sûre 5) denetimi kuralı 8: A1 ve ◇ okuma bölümündeki kelime alıntıları ◇ transliterasyonunun alt dizesi ('el-X' / 'es-X' belirlilik yazımı 'l-X' / 's-X' ile kabul)
for n in range(A, B + 1):
    a1 = M[n][M[n].index('◈A — A1 '):]; a1 = a1[:a1.index('; A2 ')]
    for x in re.findall(r"'((?:[^']|'(?=[a-zâîûçğışöü]))+)'", a1):
        if not re.search(r'[a-zâîû]', x) or ' — ' in x or re.search(r'[\u0600-\u06ff]', x) or '(' in x or ';' in x: continue
        y = re.sub(r"^e([a-zçşğ]-)", r"\1", x); z = re.sub(r"^ell", "ll", x)
        if x not in dia[n] and y not in dia[n] and z not in dia[n]: bad += 1; print('A1 alt dize dışı', n, x)
# bölüm 2 (sûre 5) denetimi kuralı 7: ◇ okuma bölümündeki "'X' (N. kelime" alıntıları kelime sınırında başlar — ayn / hemze düşmesi ("'dilû" içinden 'dilû')
for n in range(A, B + 1):
    for x in re.findall(r"'((?:[^']|'(?=[a-zâîûçğışöü]))+)' \(\d+\.", M[n]):
        if not re.search(r'[a-zâîû]', x) or re.search(r'[\u0600-\u06ff]', x): continue
        for mm in re.finditer(re.escape(x), dia[n]):
            i0 = mm.start()
            if i0 >= 1 and dia[n][i0 - 1] == "'" and (i0 == 1 or dia[n][i0 - 2] == ' '):
                if not re.search(r"(^| )%s" % re.escape(x), dia[n]): bad += 1; print('ayn / hemze düşmesi', n, x)
                break
# bölüm 2 (sûre 5) denetimi kuralı 8: 'ile açılıyor / başlıyor' iddiası yalnız 1. kelimeden başlayan aralıkla
_o = [x for x in ast.literal_eval('{' + open(Y + 'ariza' + suf).read() + '}').popitem()[1] if x.startswith('okuma (gözlem)')]
for x in _o:
    for mm in re.finditer(r"ile (?:açılıyor|başlıyor) \(([^)]*)\)", x):
        for r_ in re.findall(r"(\d+)-\d+\. kelime|(\d+)\. kelime", mm.group(1)):
            bas = r_[0] or r_[1]
            if bas != '1': bad += 1; print('açılış iddiası 1. kelimeden değil:', mm.group(0)[:80])
c = open(Y + 'cipa' + suf).read()
for x in re.findall(r'not_="\'(.+?)\' —', c):
    if x not in alltr: bad += 1; print('cipa', x)
print('alt dize dışı:', bad)

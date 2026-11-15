# meal / aday 1039 / çıpa alıntılarının ◇ transliterasyonunun alt dizesi olduğunu denetler (bölüm 7 kuralı 2)
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from sure import S
import re, sys, ast
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
c = open(Y + 'cipa' + suf).read()
for x in re.findall(r'not_="\'(.+?)\' —', c):
    if x not in alltr: bad += 1; print('cipa', x)
print('alt dize dışı:', bad)

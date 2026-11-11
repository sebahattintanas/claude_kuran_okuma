# meal / aday 1039 / çıpa alıntılarının ◇ transliterasyonunun alt dizesi olduğunu denetler (bölüm 7 kuralı 2)
import re, sys, ast
A, B = int(sys.argv[1]), int(sys.argv[2])
Y = '/home/claude/yamalar/'; suf = '_4_%d_%d.txt' % (A, B)
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
c = open(Y + 'cipa' + suf).read()
for x in re.findall(r'not_="\'(.+?)\' —', c):
    if x not in alltr: bad += 1; print('cipa', x)
print('alt dize dışı:', bad)

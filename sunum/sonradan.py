# 'sonradan basılan' (bölüm 7 kuralı 3 + bölüm 8 kuralı 1): verilen blokların say2 listelerinde, o anki sınıflamada
# 'bu' / 'basilan' olmayıp şimdi basılan listesinde bulunan ayetler. Eskiyen yoksa 'eskiyen yok' yazılır.
# kullanım (/home/claude'dan): python3 sunum/sonradan.py b14 b15 b16 b17 ...  (önceki bölümün bütün blokları + bu bölümün önceki blokları)
import re, ast, sys
B = set(l.strip() for l in open('/home/claude/sunum/basilan.txt') if l.strip())
n = 0
for blk in sys.argv[1:]:
    for b in open('/home/claude/%s/say2.txt' % blk).read().split('### ')[1:]:
        L = b.strip().splitlines(); m = re.match(r'(\d+) (\{.*\})$', L[-1].strip())
        d = ast.literal_eval(m.group(2))
        li = [l for l in L if l.startswith('liste:')]
        if not li: continue
        ay = [x.strip().split('×')[0].rstrip('†') for x in li[0][6:].split(',')]
        yeni = [a for a in ay if a in B and a not in set(d['bu']) | set(d['basilan'])]
        if yeni: n += 1; print(blk, L[0], yeni)
print('eskiyen sayım:', n)

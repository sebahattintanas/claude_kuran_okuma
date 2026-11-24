# bNN/say.sh üretici — kullanım (/home/claude'dan): python3 sunum/yardimci/say_uret.py NN "131:1-10" "132:1-4,5-9" ... [--dizi "6 135 15 18" ...]
# her meal kesimi için: kesim aralığı (4 kelimeden uzunsa) + kesim içindeki 2/3/4'lü pencereler, her biri düz ve --on; ardından 'run dizi' satırları
# (nakarat3 kalıpları, R5 için ve emsal ortak lemma dizileri için)
import sys; sys.path.insert(0, '/home/claude/sunum'); from sure import S
NN = sys.argv[1]; args = sys.argv[2:]
dz = args[args.index('--dizi') + 1:] if '--dizi' in args else []
segs = args[:args.index('--dizi')] if '--dizi' in args else args
L = ['. /home/claude/say.sh']; seen = set()
def add(k):
    if k in seen: return
    seen.add(k); L.append('run say ' + k); L.append('run say ' + k + ' --on')
for sg in segs:
    a, rr = sg.split(':')
    for r in rr.split(','):
        i, j = map(int, r.split('-'))
        if j - i + 1 > 4: add('%d:%s %d-%d' % (S, a, i, j))
        for s in range(i, j + 1):
            for n in (2, 3, 4):
                if s + n - 1 <= j: add('%d:%s %d-%d' % (S, a, s, s + n - 1))
for d in dz: L.append('run dizi ' + d)
open('/home/claude/b%s/say.sh' % NN, 'w').write('\n'.join(L) + '\n'); print(len(L))

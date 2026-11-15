# bölüm 7 kuralı 10: araç değişikliği maddesi betikle — repo HEAD'den (bir önceki blok commit'i) bu yana değişen / eklenen sunum/ dosyaları
# kullanım (/home/claude'dan): python3 sunum/arac_degisim.py  → tek satır; sinifla.py SON ve basilan.txt ayrı yazılır
import glob, os, re, subprocess
R = '/home/claude/repo'; HAR = ('sunum/basilan.txt', 'sunum/sinifla.py')
deg = []
for f in sorted(glob.glob('/home/claude/sunum/*')):
    if os.path.isdir(f): continue
    rel = 'sunum/' + os.path.basename(f)
    if rel in HAR: continue
    eski = subprocess.run(['git', 'show', 'HEAD:' + rel], capture_output=True, cwd=R)
    if eski.returncode or eski.stdout != open(f, 'rb').read(): deg.append(rel + (' (yeni)' if eski.returncode else ''))
son = re.search(r'^SON = (\d+)', open('/home/claude/sunum/sinifla.py', encoding='utf-8').read(), re.M).group(1)
eb = subprocess.run(['git', 'show', 'HEAD:sunum/basilan.txt'], capture_output=True, text=True, cwd=R).stdout.split()
yb = open('/home/claude/sunum/basilan.txt', encoding='utf-8').read().split()
print(('değişen araçlar (repo HEAD ile fark): ' + ', '.join(deg)) if deg else 'bu blokta araç değişmedi',
      end='; sunum/sinifla.py (SON %s); sunum/basilan.txt +%d\n' % (son, len(yb) - len(eb)))

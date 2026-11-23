import re,sys
sys.path.insert(0,'/home/claude/sunum/yardimci'); from say_kontrol import parse
import sys; NN=sys.argv[1]; p='/home/claude/b%s/say2.txt' % NN; s='/home/claude/b%s/say.sh' % NN
t=open(p,encoding='utf-8').read()
blks=re.split(r'^(?=### )',t,flags=re.M)
head=blks[0]; blks=blks[1:]
seen=set(); kept=[]
for b in blks:
    h=b.split('\n',1)[0][4:].strip()
    if h in seen: continue
    seen.add(h); kept.append((h,b))
d={h:(int(re.search(r'^ayet: (\d+)',b,re.M).group(1)) if re.search(r'^ayet: (\d+)',b,re.M) else None) for h,b in kept}
drop=set()
for h in d:
    if h.startswith('say ') and '--' not in h:
        for suf in ('',' --medde'):
            a=d.get(h+suf) if suf else d[h]; o=d.get(h+' --on'+suf)
            if a==1 and o is not None and o!=1: drop|={h,h+' --on',h+' --medde',h+' --on --medde'}
print(len(drop)//4, sorted(x for x in drop if '--' not in x))
open(p,'w',encoding='utf-8').write(head+''.join(b for h,b in kept if h not in drop))
L=open(s,encoding='utf-8').read().split('\n'); out=[];sl=set()
for l in L:
    k=l[4:].strip() if l.startswith('run ') else None
    if k and (k in drop or k in sl): continue
    if k: sl.add(k)
    out.append(l)
open(s,'w',encoding='utf-8').write('\n'.join(out))

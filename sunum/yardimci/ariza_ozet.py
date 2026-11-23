import ast,sys
t=open(sys.argv[1],encoding='utf-8').read()
out=set()
for l in t.splitlines():
    l=l.strip()
    if l.startswith('['):
        try:
            for x in ast.literal_eval(l):
                if isinstance(x,str) and x.startswith('HATA') and 'öz denetim' not in x: out.add(x)
        except Exception: pass
    elif l.startswith('HATA'): out.add(l)
for x in sorted(out): print(x[:330])
print('TOPLAM', len(out))

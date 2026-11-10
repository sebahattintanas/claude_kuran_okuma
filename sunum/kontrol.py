import re, ast, sys
S,A,B=4,int(sys.argv[1]),int(sys.argv[2])
Y='/home/claude/yamalar/'; suf='_%d_%d_%d.txt'%(S,A,B)
ns={'MEAL':{},'M':{}}; exec(open(Y+'metin'+suf).read(),ns); M=ns['M']
bag=ast.literal_eval('['+open(Y+'bag'+suf).read()+']')
O=[l.replace('**','') for l in open('/home/claude/b%02d/olcum.txt'%int(sys.argv[3]),encoding='utf-8').read().split('\n\n') if l.strip()]
bad=0
# D3 ⇔ bag
for n in range(A,B+1):
    d3=re.search(r'D3 (.*?); D4',M[n]).group(1)
    refs=set(re.findall(r'\d+:\d+',d3))
    want=set()
    for b in bag:
        x,y=b['bag'].split(' → ')
        if y=='%d:%d'%(S,n): want.add(x)
        if x=='%d:%d'%(S,n) and int(y.split(':')[1])<=B and y.startswith('%d:'%S): want.add(y)
    if refs!=want: bad+=1; print('D3≠bag',n,'D3-fazla',refs-want,'bag-fazla',want-refs)
# A1 ⇔ ◇ adsız
for n in range(A,B+1):
    a1=re.search(r'◈A — A1 (.*?); A2',M[n]).group(1)
    dia=M[n].split('\n')[0]
    for m in re.findall(r"([^;()]*?\(adsız)",dia):
        k=m.strip().lstrip('. ')
        # taraf adı: '(adsız' öncesindeki son ifade
        if k.split(' (adsız')[0][-30:].lower() not in a1.lower(): bad+=1; print('A1 eksik',n,k[-60:])
    for m in re.findall(r"([^;]*?\(adsız\))",a1):
        if m.strip()[:-1].lower() not in dia.lower(): bad+=1; print('◇ eksik',n,m.strip())
# bab
for n in range(A,B+1):
    dia=M[n].split('\n')[0]
    diz=dia[dia.index(' — ')+3:dia.index(' (ölçüm edim')]
    from collections import Counter
    c=Counter(re.findall(r'([IVX]+)\. bab',diz))
    m=re.search(r'bab ((?:[IVX]+\. bab ×\d+(?: · )?)+)',O[n-A])
    o=Counter(dict((k,int(v)) for k,v in re.findall(r'([IVX]+)\. bab ×(\d+)',m.group(1)))) if m else Counter()
    if c!=o: bad+=1; print('bab',n,c,o)
    if ('bab '+ (m.group(1) if m else '')) not in dia: bad+=1; print('◇ bab parantezi ölçümle farklı',n)
print('kontrol uyuşmaz:',bad)

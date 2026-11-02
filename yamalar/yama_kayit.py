# -*- coding: utf-8 -*-
"""yama_kayit.py — bakara_kayit.py'ye blok CIPA satırlarını ve çapalı ARIZA bloğunu ekler (oturum dışı).
Kullanım: python3 yama_kayit.py <cipa.txt> <ariza.txt>
CIPA: '\n}\n\nARIZA = {' önüne. ARIZA: t.rindex('\n ],\n}') + 4; metin '\n (A, B): [\n' ile başlar, ' ],' ile biter."""
import sys, py_compile, importlib
p = '/home/claude/calisma/bakara_kayit.py'
t = open(p, encoding='utf-8').read()
c = open(sys.argv[1], encoding='utf-8').read().rstrip('\n')
a = open(sys.argv[2], encoding='utf-8').read().rstrip('\n')
assert c.startswith(' # blok') and c.splitlines()[0] not in t, 'CIPA başlığı yok ya da zaten var'
assert a.startswith('\n (') and a.endswith(' ],') and a.splitlines()[1] not in t, 'ARIZA biçimi'
ca = '\n}\n\nARIZA = {'
assert t.count(ca) == 1
t = t.replace(ca, '\n' + c + ca)
assert t.count('\n ],\n}') == 1, 'ARIZA çapası 1 değil'
i = t.rindex('\n ],\n}') + 4
t = t[:i] + a + t[i:]
assert t.count('\n ],\n}') == 1, 'ekleme sonrası çapa 1 değil'
open(p, 'w', encoding='utf-8').write(t)
py_compile.compile(p, doraise=True)
sys.path.insert(0, '/home/claude/calisma')
K = importlib.import_module('bakara_kayit')
print('CIPA', sorted(K.CIPA)[-6:], '· ARIZA', list(K.ARIZA), '· çapa 1')

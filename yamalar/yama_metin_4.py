# -*- coding: utf-8 -*-
"""yama_metin_4.py — nisa_metin_1.py'ye bir blok metni ekler (oturum dışı). Kullanım: python3 yama_metin.py <blok.txt> <MEALn>
assert: MEALn dosyada yok; ekleme sonrası py_compile ve sözlük anahtarları blokla aynı."""
import sys, py_compile, importlib, re
p = '/home/claude/calisma/nisa_metin_1.py'
ek, ad = sys.argv[1], sys.argv[2]
t = open(p, encoding='utf-8').read()
e = open(ek, encoding='utf-8').read()
assert '\n%s = {' % ad not in t, '%s zaten var' % ad
assert e.count('\n%s = {' % ad) == 1
t2 = t.rstrip('\n') + '\n' + e
open(p, 'w', encoding='utf-8').write(t2)
py_compile.compile(p, doraise=True)
sys.path.insert(0, '/home/claude/calisma')
M = importlib.import_module('nisa_metin_1')
n = int(re.sub(r'\D', '', ad))
blok = getattr(M, 'MEAL%d' % n)
assert set(blok) == set(getattr(M, 'M%d' % n)), 'MEAL / M anahtarları ayrı'
print('eklendi:', ad, sorted(blok))

# -*- coding: utf-8 -*-
"""yama_kayit_ilk.py — bakara_kayit.py'nin boş CIPA / ARIZA / DUZELTME'sini ilk blok kaydıyla değiştirir (çapasız; oturum dışı)."""
import sys, py_compile, importlib
p = '/home/claude/calisma/bakara_kayit.py'
t = open(p, encoding='utf-8').read()
bos = '\nCIPA = {}\n\nARIZA = {}\n\nDUZELTME = {}\n'
assert t.count(bos) == 1, 'boş kayıt çapası yok'
t = t.replace(bos, '\n' + open(sys.argv[1], encoding='utf-8').read())
open(p, 'w', encoding='utf-8').write(t)
py_compile.compile(p, doraise=True)
sys.path.insert(0, '/home/claude/calisma')
K = importlib.import_module('bakara_kayit')
assert t.count('\n ],\n}') == 1, 'ARIZA çapası sayısı 1 değil'
print('kayıt: CIPA', sorted(K.CIPA), '· ARIZA', list(K.ARIZA), len(K.ARIZA[list(K.ARIZA)[0]]), 'satır · DUZELTME', len(K.DUZELTME))

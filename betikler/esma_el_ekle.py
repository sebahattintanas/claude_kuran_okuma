# -*- coding: utf-8 -*-
"""esma_el_ekle.py — esma_el.py KARAR sözlüğüne blok kararlarını ekler (idempotent; ast ile doğrular).
Kullanım: python3 esma_el_ekle.py <dosya_ile_satirlar>  — satırlar esma_el.py biçiminde ('S:A:W': 'ilahi', # gerekçe)."""
import sys, ast
p = 'esma_el.py'
s = open(p, encoding='utf-8').read()
ek = open(sys.argv[1], encoding='utf-8').read().rstrip('\n') + '\n'
baslik = ek.splitlines()[0]
if baslik in s:
    print('zaten var:', baslik.strip()); sys.exit()
i = s.rindex('}')
s = s[:i] + ek + s[i:]
ast.parse(s)
open(p, 'w', encoding='utf-8').write(s)
ns = {}; exec(s, ns); print('KARAR:', len(ns['KARAR']))

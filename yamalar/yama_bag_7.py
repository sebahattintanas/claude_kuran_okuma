# -*- coding: utf-8 -*-
"""yama_bag_7.py — aday_ekle_7_araf.py AS_araf listesine blok bağlarını ekler (oturum dışı). Kullanım: python3 yama_bag.py <bag.txt>"""
import sys, ast, py_compile
p = '/home/claude/calisma/aday_ekle_7_araf.py'
t = open(p, encoding='utf-8').read()
e = open(sys.argv[1], encoding='utf-8').read().rstrip('\n') + '\n'
bas = e.splitlines()[0]
assert bas.strip().startswith('# blok') and bas not in t, 'blok başlığı yok ya da zaten var'
i = t.index('BAGLAR = {"AS_araf": [\n'); j = t.index('\n]}\n', i) + 1
t = t[:j] + e + t[j:]
open(p, 'w', encoding='utf-8').write(t)
py_compile.compile(p, doraise=True)
k = t.index('BAGLAR = '); B = ast.literal_eval(t[k + 9:t.index('\n]}\n', k) + 3])
print('AS_araf', len(B['AS_araf']))

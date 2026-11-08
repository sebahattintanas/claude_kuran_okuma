# -*- coding: utf-8 -*-
"""yama_bag_3.py — aday_ekle_3_al_imran.py AS_al_imran listesine blok bağlarını ekler (oturum dışı). Kullanım: python3 yama_bag.py <bag.txt>"""
import sys, ast, py_compile
p = '/home/claude/calisma/aday_ekle_3_al_imran.py'
t = open(p, encoding='utf-8').read()
e = open(sys.argv[1], encoding='utf-8').read().rstrip('\n') + '\n'
bas = e.splitlines()[0]
assert bas.strip().startswith('# blok') and bas not in t, 'blok başlığı yok ya da zaten var'
i = t.index('BAGLAR = {"AS_al_imran": [\n'); j = t.index('\n]}\n', i) + 1
t = t[:j] + e + t[j:]
open(p, 'w', encoding='utf-8').write(t)
py_compile.compile(p, doraise=True)
k = t.index('BAGLAR = '); B = ast.literal_eval(t[k + 9:t.index('\n]}\n', k) + 3])
print('AS_al_imran', len(B['AS_al_imran']))

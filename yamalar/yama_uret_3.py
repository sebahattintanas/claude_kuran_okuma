# -*- coding: utf-8 -*-
"""yama_uret_3.py — uret_blok_3.py BLOKLAR / BASLIK'a blok ekler (oturum dışı). Kullanım: python3 yama_uret.py A B "başlık"
BASLIK çapası dosyadan okunur (son satır '}' öncesi); idempotent değil — blok zaten varsa DUR."""
import sys, re, py_compile
p = '/home/claude/calisma/uret_blok_3.py'
a, b, bas = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
t = open(p, encoding='utf-8').read()
m = re.search(r'^BLOKLAR = (\[.*\])$', t, re.M)
BL = eval(m.group(1))
assert (a, b) not in BL, 'blok zaten var'
assert not BL or BL[-1][1] + 1 == a, 'blok sırası kopuk: %s → %d' % (BL[-1:], a)
BL.append((a, b))
t = t[:m.start()] + 'BLOKLAR = %s' % BL + t[m.end():]
i = t.index('BASLIK = {\n'); j = t.index('\n}\n', i)
assert '"' not in bas
t = t[:j] + '\n (%d, %d): "3:%d-%d — %s",' % (a, b, a, b, bas) + t[j:]
open(p, 'w', encoding='utf-8').write(t)
py_compile.compile(p, doraise=True)
ns = {}
exec(t[t.index('BLOKLAR = '):t.index("\nSABLON = ")], ns)
assert set(ns['BLOKLAR']) == set(ns['BASLIK']), 'BLOKLAR / BASLIK ayrı'
print('BLOKLAR', ns['BLOKLAR'])

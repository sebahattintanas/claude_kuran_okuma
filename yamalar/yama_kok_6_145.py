# -*- coding: utf-8 -*-
"""yama_kok_6_145.py — sûre 6 bölüm 17 (blok 35, 6:145-147): kok_ekle_6.ISTEK'e bir bloğun yeni kök(ler)ini ekler; boş ISTEK'e de.
Kopyası yama_kok_6_<A>.py olarak yazılır: BLOK ve YENI doldurulur (YENI \\u kaçışlı; birden çok kök olabilir).
Anahtar kok_envanteri'nden NFC ile; karşılıktaki ayet sayısı kok_envanteri'nden yazılır."""
import json, unicodedata as ud, ast, py_compile
p = '/home/claude/calisma/kok_ekle_6.py'
env = json.load(open('/home/claude/calisma/kok_envanteri.json', encoding='utf-8'))
BLOK = "35"
YENI = [("\u0634\u062d\u0645", "iç yağ (şahm)")]
assert BLOK and YENI, 'şablon doldurulmadı'
t = open(p, encoding='utf-8').read()
i = t.index('ISTEK = ['); j = t.index('\n]\n', i)
eski = ast.literal_eval(t[i:j + 2].split('=', 1)[1].strip())
ek = "\n    # blok %s" % BLOK
for ara, tr in YENI:
    k = [x for x in env if ud.normalize('NFC', x) == ud.normalize('NFC', ara)]
    assert len(k) == 1, 'kok envanterde tekil degil: %r' % ara
    assert all(a != k[0] for a, _ in eski), 'kok zaten var'
    ek += "\n    (%r, %r)," % (k[0], tr)
t = t[:j] + ek + t[j:]
open(p, 'w', encoding='utf-8').write(t)
py_compile.compile(p, doraise=True)
i = t.index('ISTEK = ['); j = t.index('\n]\n', i)
print('ISTEK:', len(ast.literal_eval(t[i:j + 2].split('=', 1)[1].strip())))

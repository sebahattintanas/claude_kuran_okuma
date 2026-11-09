# -*- coding: utf-8 -*-
"""yama_kok_3_74.py — bölüm 6-3: kok_ekle_3.ISTEK'e bir bloğun yeni kök(ler)ini ekler; boş ISTEK'e de.
Kopyası yama_kok_3_<A>.py olarak yazılır: BLOK ve YENI doldurulur (YENI \\u kaçışlı; birden çok kök olabilir).
Anahtar kok_envanteri'nden NFC ile; karşılıktaki ayet sayısı kok_envanteri'nden yazılır."""
import json, unicodedata as ud, ast, py_compile
p = '/home/claude/calisma/kok_ekle_3.py'
env = json.load(open('/home/claude/calisma/kok_envanteri.json', encoding='utf-8'))
BLOK = '74-77'
YENI = [('\u062f\u0646\u0631', "dinar, altın para ('dînâr'); 1 ayet")]
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

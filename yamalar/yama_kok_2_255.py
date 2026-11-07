# -*- coding: utf-8 -*-
"""yama_kok_2_255.py — kok_ekle_2.ISTEK'e blok 2:255-257'nin yeni koklerini ekler (bos olmayan ISTEK'e). Anahtar kok_envanteri'nden NFC ile."""
import json, unicodedata as ud, ast, py_compile
p = '/home/claude/calisma/kok_ekle_2.py'
env = json.load(open('/home/claude/calisma/kok_envanteri.json', encoding='utf-8'))
YENI = [('\u0648\u0633\u0646', "uyuklama, hafif uyku ('sine'; 1 ayet)"), ('\u0623\u0648\u062f', "ağır gelme, yorma ('ye\u2019ûduhû'; 1 ayet)"), ('\u0641\u0635\u0645', "kopma, kırılma ('infisâm'; 1 ayet)")]
t = open(p, encoding='utf-8').read()
i = t.index('ISTEK = ['); j = t.index('\n]\n', i)
eski = ast.literal_eval(t[i:j + 2].split('=', 1)[1].strip())
assert eski, 'ISTEK bos'
ek = "\n    # blok 255-257"
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

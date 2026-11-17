src = open('/home/claude/b28/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("5:94", "'eyy ellezî âmene'", 16, 'say 5:94 1-3', "harekesiz 'yâ eyyuhe'llezîne âmenû' (1-3. kelime)", None),
 ("5:95", "'eyy ellezî âmene lâ'", 6, 'say 5:95 1-4', "harekesiz 'yâ eyyuhe'llezîne âmenû lâ' (1-4. kelime)", None),
 ("5:95", "'eyy ellezî âmene'", 16, 'say 5:95 1-3', "harekesiz 'yâ eyyuhe'llezîne âmenû' (1-3. kelime)", None),
 ("5:95", "'sayd _ harâm'", 2, 'say 5:95 6-8', "harekesiz 's-sayde ve entum hurum' (6-8. kelime; biçim öğesi 've entum' — ölçüm kalıbında 'و' bitişik yazım)", None),
 ("5:95", "'zû 'adl min'", 2, 'say 5:95 21-23', "harekesiz 'zevâ 'adlin minkum' (21-23. kelime)", None),
 ("5:96", "'itteqâ allâh ellezî'", 2, 'say 5:96 16-18 --on', "önek kesilmiş 've'ttequ'llâhe'llezî' (16-18. kelime)", None),
]
'''
VF = '''VF_YAZI = {94: {11: "'ve rimâhukum'", 17: "'fe-meni'tedâ'", 21: "'fe-lehû'"}, 95: {7: "'ve entum'", 9: "'ve men'", 13: "'fe-cezâ'un'", 42: "'ve men'", 44: "'fe-yentaqimu'", 47: "'ve'llâhu'"}, 96: {5: "'ve ta'âmuhû'", 8: "'ve li's-seyyârati'", 9: "'ve hurrime'", 16: "'ve'ttequ'"}}
sys.path.insert(0, '/home/claude/b29/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b29/yap/I_parca.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('ARIZA oluşturucu — bölüm 12-2', 'ARIZA oluşturucu — bölüm 13-1'), ('# blok 28 (5:90-93)', '# blok 29 (5:94-96)'), ('/b28/', '/b29/'), ("es_edat.py', '28'", "es_edat.py', '29'"), ('range(1, 29)', 'range(1, 30)'),
     ("'--plan', '28', '--numarasiz')", "'--plan', '29', '--numarasiz')"),
     ('ariza_5_90_93', 'ariza_5_94_96'), ('geriye_donuk_5_b27.txt', 'geriye_donuk_5_b29.txt'), ('(90, 93)', '(94, 96)'), ("'90', '93', '28'", "'94', '96', '29'"), ("'90', '93'", "'94', '96'"),
     ("BEK = []", "BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b28.txt', encoding='utf-8').read() + ']')"),
     ("BOL = \"'Helalleri haram kılmama; yemin keffareti; içki ve kumar'\"", "BOL = \"'İhramda av; Kâbe ve haram ay; elçinin görevi'\""),
     ("'26', '27', '28')", "'26', '27', '28', '29')"),
     ("    B11 = run('/home/claude/sunum/bolum11_kurallar.py', '94', '96', '29').splitlines()", "    B11 = run('/home/claude/sunum/bolum11_kurallar.py', '94', '96', '29').splitlines()\n    B12 = run('/home/claude/sunum/bolum12_kurallar.py', '94', '96', '29').splitlines()"),
     ("'B11_HEPSI': (B11[-1] if B11 else '?'),", "'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'),"),
     ]
for a, b in R:
    assert a in out, a
    out = out.replace(a, b)
for l in out.split('\n'):
    for bad in ('b28', "'28'", "'90'", "'93'", '5_90_93'):
        if bad in l and 'nn in' not in l: print('KONTROL', bad, l[:160])
open('/home/claude/b29/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)

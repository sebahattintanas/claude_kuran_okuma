src = open('/home/claude/b30/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("5:101", "'eyy ellezî âmene lâ'", 6, 'say 5:101 1-4', "harekesiz 'yâ eyyuhe'llezîne âmenû lâ' (1-4. kelime)", None),
 ("5:101", "'eyy ellezî âmene'", 16, 'say 5:101 1-3', "harekesiz 'yâ eyyuhe'llezîne âmenû' (1-3. kelime)", None),
 ("5:104", "'mâ enzele allâh'", 2, 'say 5:104 6-8', "harekesiz 'mâ enzele'llâh' (6-8. kelime; biçim öğesi — lemma dizisi 'dizi 5 104 6 8' sûre içi 6, harekesiz kalıp 2)", None),
 ("5:105", "'ilâ allâh merci' cemî' nebbe'e mâ kâne'", 2, 'say 5:105 12-18', "harekesiz 'ile'llâhi merci'ukum cemî'an fe-yunebbi'ukum bi-mâ kuntum' (12-18. kelime)", None),
 ("5:105", "'eyy ellezî âmene'", 16, 'say 5:105 1-3', "harekesiz 'yâ eyyuhe'llezîne âmenû' (1-3. kelime)", None),
]
'''
VF = '''VF_YAZI = {101: {12: "'ve in'", 23: "'ve'llâhu'"}, 103: {6: "'ve lâ sâ'ibetin'", 8: "'ve lâ vasîletin'", 10: "'ve lâ hâmin'", 12: "'ve lâkinne'", 19: "'ve ekseruhum'"}, 104: {1: "'ve izâ'", 9: "'ve ile'r-rasûli'", 17: "'e-ve-lev'", 23: "'ve lâ'"}, 105: {16: "'fe-yunebbi'ukum'"}}
sys.path.insert(0, '/home/claude/b31/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b31/yap/I_head.py', encoding='utf-8').read() + open('/home/claude/b31/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('ARIZA oluşturucu — bölüm 13-2', 'ARIZA oluşturucu — bölüm 14-1'), ('# blok 30 (5:97-100)', '# blok 31 (5:101-105)'), ('/b30/', '/b31/'), ("es_edat.py', '30'", "es_edat.py', '31'"), ('range(1, 31)', 'range(1, 32)'),
     ("'--plan', '30', '--numarasiz')", "'--plan', '31', '--numarasiz')"),
     ('ariza_5_97_100', 'ariza_5_101_105'), ('(97, 100)', '(101, 105)'), ("'97', '100', '30'", "'101', '105', '31'"), ("'97', '100'", "'101', '105'"),
     ("BEK = []", "BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b30.txt', encoding='utf-8').read() + ']')"),
     ("BOL = \"'İhramda av; Kâbe ve haram ay; elçinin görevi'\"", "BOL = \"'Soru sormama; bahîra ve sâibe; vasiyet ve şahitlik'\""),
     ("'28', '29', '30')", "'28', '29', '30', '31')"),
     ('geriye_donuk_5_b29.txt', 'geriye_donuk_5_b31.txt'),
     ("    B12 = run('/home/claude/sunum/bolum12_kurallar.py', '101', '105', '31').splitlines()", "    B12 = run('/home/claude/sunum/bolum12_kurallar.py', '101', '105', '31').splitlines()\n    B13 = run('/home/claude/sunum/bolum13_kurallar.py', '101', '105', '31').splitlines()"),
     ("'B12_HEPSI': (B12[-1] if B12 else '?'),", "'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'),"),
     ]
for a, b in R:
    assert a in out, a
    out = out.replace(a, b)
for l in out.split('\n'):
    for bad in ('b30', "'30'", "'97'", "'100'", '5_97_100'):
        if bad in l and 'nn in' not in l: print('KONTROL', bad, l[:160])
open('/home/claude/b31/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)

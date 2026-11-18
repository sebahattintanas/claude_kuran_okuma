src = open('/home/claude/b35/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("5:119", "'cenne cerey min taht neher xâlid fî'", 2, 'say 5:119 9-15', "harekesiz 'cennâtun tecrî min tahtihe'l-enhâru xâlidîne fîhâ' (9-15. kelime)", ('dizi 5 119 9 15', "cenne cerey min taht neher xâlid fî", '9-15', "biçim farkı (dizi 5 119 9 15): 5:85 yazım eş")),
 ("5:119", "'cenne cerey min taht neher'", 3, 'say 5:119 9-13', "harekesiz 'cennâtun tecrî min tahtihe'l-enhâr' (9-13. kelime)", None),
 ("5:120", "'allâh mulk semâ' ard mâ'", 3, 'say 5:120 1-5', "harekesiz 'li'llâhi mulku's-semâvâti ve'l-ardi ve mâ' (1-5. kelime)", ('dizi 5 120 1 5', "allâh mulk semâ' ard mâ", '1-5', "biçim farkı (dizi 5 120 1 5): 5:17 önek; basılmamış eş önek")),
 ("5:120", "''alâ kull şey' qadîr'", 4, 'say 5:120 8-11', "harekesiz ''alâ kulli şey'in qadîr' (8-11. kelime)", None),
 ("5:120", "''alâ kull şey''", 5, 'say 5:120 8-10', "harekesiz ''alâ kulli şey'' (8-10. kelime)", None),
 ("5:120", "'mulk semâ' ard'", 4, 'say 5:120 2-4', "harekesiz 'mulku's-semâvâti ve'l-ard' (2-4. kelime)", None),
]
'''
VF = '''VF_YAZI = {118: {5: "'ve in'"}, 119: {20: "'ve radû'"}, 120: {4: "'ve'l-ardi'", 5: "'ve mâ'", 7: "'ve huve'"}}
sys.path.insert(0, '/home/claude/b36/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b36/yap/I_head.py', encoding='utf-8').read() + open('/home/claude/b36/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('ARIZA oluşturucu — bölüm 16-1', 'ARIZA oluşturucu — bölüm 16-2'), ('# blok 35 (5:116-117)', '# blok 36 (5:118-120)'), ('/b35/', '/b36/'), ("es_edat.py', '35'", "es_edat.py', '36'"), ('range(1, 36)', 'range(1, 37)'),
     ("'--plan', '35', '--numarasiz')", "'--plan', '36', '--numarasiz')"),
     ('ariza_5_116_117', 'ariza_5_118_120'), ('(116, 117)', '(118, 120)'), ("'116', '117', '35'", "'118', '120', '36'"), ("'116', '117'", "'118', '120'"),
     ("BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b34.txt', encoding='utf-8').read() + ']')", "BEK = []"),
     ("'33', '34', '35')", "'33', '34', '35', '36')"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_5_b35.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_5_b36.txt'"),
     ]
for a, b in R:
    assert a in out, a
    out = out.replace(a, b)
for l in out.split('\n'):
    for bad in ('b35', "'35'", "'116'", "'117'", '5_116_117'):
        if bad in l and 'nn in' not in l: print('KONTROL', bad, l[:160])
open('/home/claude/b36/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)

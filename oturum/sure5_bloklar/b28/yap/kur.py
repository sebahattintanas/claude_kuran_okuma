src = open('/home/claude/b27/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("5:90", "'eyy ellezî âmene'", 16, 'say 5:90 1-3', "harekesiz 'yâ eyyuhe'llezîne âmenû' (1-3. kelime)", None),
 ("5:91", "'beyn 'adâve bağdâ''", 3, 'say 5:91 6-8', "harekesiz 'beynekumu'l-'adâvete ve'l-bağdâ'' (6-8. kelime)", ('dizi 5 91 6 8', "beyn 'adâve bağdâ'", '6-8', "biçim farkı (dizi 5 91 6 8): 5:14 elif yazımı, zamir eki; basılmamış eş zamir eki")),
 ("5:92", "'fe-in tevellâ 'alime enne'", 2, 'say 5:92 6-9 --on', "önek kesilmiş 'fe-in tevelleytum fe'lemû ennemâ' (6-9. kelime; biçim öğesi 'fe-in' / 'ennemâ' — ölçüm kalıbında önekli ve 'mâ' bitişik yazım)", ('dizi 5 92 6 9', "fe-in tevellâ 'alime enne", '6-9', "biçim farkı (dizi 5 92 6 9): basılmamış eş fiil çekimi, zamir eki")),
 ("5:93", "'ellezî âmene 'amile sâliha'", 2, 'say 5:93 3-6', "harekesiz 'llezîne âmenû ve 'amilu's-sâlihât' (3-6. kelime)", None),
 ("5:93", "'allâh ahbeb muhsin' (LEM 'ahbeb' (morph LEM ham biçim))", 2, 'say 5:93 22-24 --on', "önek kesilmiş 've'llâhu yuhibbu'l-muhsinîn' (22-24. kelime)", ('dizi 5 93 22 24', "allâh ahbeb muhsin", '22-24', "biçim farkı (dizi 5 93 22 24): basılmamış eş i'râb, önek")),
]
'''
VF = '''VF_YAZI = {90: {6: "'ve'l-meysiru'", 7: "'ve'l-ensâbu'", 8: "'ve'l-ezlâmu'", 13: "'fe'ctenibûhu'"}, 91: {8: "'ve'l-bağdâ'e'", 11: "'ve'l-meysiri'", 12: "'ve yesuddekum'", 16: "'ve 'ani's-salâti'", 18: "'fe-hel'"}, 92: {1: "'ve atî'u'", 3: "'ve atî'u'", 5: "'ve'hzerû'", 6: "'fe-in'", 8: "'fe'lemû'"}, 93: {5: "'ve 'amilu'", 13: "'ve âmenû'", 14: "'ve 'amilu'", 18: "'ve âmenû'", 21: "'ve ahsenû'", 22: "'ve'llâhu'"}}
sys.path.insert(0, '/home/claude/b28/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b28/yap/I_parca.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('ARIZA oluşturucu — bölüm 12-1', 'ARIZA oluşturucu — bölüm 12-2'), ('# blok 27 (5:87-89)', '# blok 28 (5:90-93)'), ('/b27/', '/b28/'), ("es_edat.py', '27'", "es_edat.py', '28'"), ('range(1, 28)', 'range(1, 29)'),
     ("'--plan', '27', '--numarasiz')", "'--plan', '28', '--numarasiz')"),
     ('ariza_5_87_89', 'ariza_5_90_93'), ('(87, 89)', '(90, 93)'), ("'87', '89', '27'", "'90', '93', '28'"), ("'87', '89'", "'90', '93'"),
     ("BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b26.txt', encoding='utf-8').read() + ']')", "BEK = []"),
     ("'25', '26', '27')", "'25', '26', '27', '28')"),
     ]
for a, b in R:
    assert a in out, a
    out = out.replace(a, b)
for l in out.split('\n'):
    for bad in ('b27', "'27'", "'87'", "'89'", '5_87_89'):
        if bad in l and 'nn in' not in l and 'geriye_donuk_5_b27' not in l: print('KONTROL', bad, l[:160])
open('/home/claude/b28/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)

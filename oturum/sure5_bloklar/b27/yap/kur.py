src = open('/home/claude/b26/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("5:87", "'eyy ellezî âmene lâ'", 6, 'say 5:87 1-4', "harekesiz 'yâ eyyuhe'llezîne âmenû lâ' (1-4. kelime)", None),
 ("5:87", "'eyy ellezî âmene'", 16, 'say 5:87 1-3', "harekesiz 'yâ eyyuhe'llezîne âmenû' (1-3. kelime)", None),
 ("5:87", "'inne allâh lâ'", 3, 'say 5:87 13-15', "harekesiz 'inne'llâhe lâ' (13-15. kelime)", None),
 ("5:87", "'allâh lâ ahbeb' (LEM 'ahbeb' (morph LEM ham biçim))", 2, 'say 5:87 14-16', "harekesiz 'llâhe lâ yuhibbu' (14-16. kelime)", ('dizi 5 87 14 16', "allâh lâ ahbeb", '14-16', "biçim farkı (dizi 5 87 14 16): basılmamış eş i'râb, önek")),
 ("5:88", "'ittaqâ allâh ellezî'", 2, 'say 5:88 7-9 --on', "önek kesilmiş 've'ttequ'llâhe'llezî' (7-9. kelime)", None),
]
'''
VF = '''VF_YAZI = {87: {11: "'ve lâ'"}, 88: {1: "'ve kulû'", 7: "'ve'ttequ'"}, 89: {7: "'ve lâkin'", 12: "'fe-keffâratuhû'", 26: "'fe-men'", 29: "'fe-siyâmu'", 37: "'ve'hfezû'"}}
sys.path.insert(0, '/home/claude/b27/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b27/yap/I_parca.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
m0 = out.index('MFARK = '); m1 = out.index('\n', out.index('MEDF += ')) + 1
out = out[:m0] + "sys.path.insert(0, '/home/claude/sunum'); import medde_fark\nMEDF = medde_fark.satir('/home/claude/b27/say2.txt')  # bölüm 11 denetimi kuralı 6\n" + out[m1:]
R = [('ARIZA oluşturucu — bölüm 11-2', 'ARIZA oluşturucu — bölüm 12-1'), ('# blok 26 (5:82-86)', '# blok 27 (5:87-89)'), ('/b26/', '/b27/'), ("es_edat.py', '26'", "es_edat.py', '27'"), ('range(1, 27)', 'range(1, 28)'),
     ("'--plan', '26', '--numarasiz')", "'--plan', '27', '--numarasiz')"),
     ('ariza_5_82_86', 'ariza_5_87_89'), ('geriye_donuk_5_b26.txt', 'geriye_donuk_5_b27.txt'), ('(82, 86)', '(87, 89)'), ("'82', '86', '26'", "'87', '89', '27'"), ("'82', '86'", "'87', '89'"),
     ("BEK = []", "BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b26.txt', encoding='utf-8').read() + ']')"),
     ("BOL = \"'Lanetlenenler; Nasârâ'nın yakınlığı; gözyaşı dökenler'\"", "BOL = \"'Helalleri haram kılmama; yemin keffareti; içki ve kumar'\""),
     ("'21', '22', '23', '24', '25', '26')", "'21', '22', '23', '24', '25', '26', '27')"),
     ("for ay, kal, nk, key, ad, dz in R5:", "for ay, kal, nk, key, ad, dz, *tr_ in R5:"),
     ('h = "%s nakarat3 %s %d (tür ic) / %s sûre içi %d (%s)" % (ay, kal, nk, ad, s, taban(key, ay))', 'h = "%s nakarat3 %s %d (tür %s) / %s sûre içi %d (%s)" % (ay, kal, nk, (tr_[0] if tr_ else \'ic\'), ad, s, taban(key, ay))  # bölüm 11 denetimi kuralı 3'),
     ("    B10 = run('/home/claude/sunum/bolum10_kurallar.py', '87', '89', '27').splitlines()", "    B10 = run('/home/claude/sunum/bolum10_kurallar.py', '87', '89', '27').splitlines()\n    B11 = run('/home/claude/sunum/bolum11_kurallar.py', '87', '89', '27').splitlines()"),
     ("'B10_HEPSI': (B10[-1] if B10 else '?'),", "'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'),"),
     ]
for a, b in R:
    assert a in out, a
    out = out.replace(a, b)
for l in out.split('\n'):
    for bad in ('b26', "'26'", "'82'", "'86'", '5_82_86'):
        if bad in l and 'nn in' not in l: print('KONTROL', bad, l[:160])
open('/home/claude/b27/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)

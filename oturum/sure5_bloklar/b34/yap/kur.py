src = open('/home/claude/b33/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("5:112", "'itteqâ allâh in kâne mu'min'", 2, 'say 5:112 17-21', "harekesiz 'ttequ'llâhe in kuntum mu'minîn' (17-21. kelime)", ('dizi 5 112 17 21', "itteqâ allâh in kâne mu'min", '17-21', "biçim farkı (dizi 5 112 17 21): basılmamış eş önek")),
 ("5:112", "''alâ mâ'ide min semâ''", 2, 'say 5:112 12-15', "harekesiz ''aleynâ mâ'ideten mine's-semâ'' (12-15. kelime)", None),
 ("5:112", "'itteqâ allâh in'", 6, 'say 5:112 17-19', "harekesiz 'ttequ'llâhe in' (17-19. kelime; biçim öğesi 'in' — ölçüm kalıbı harekesiz 'ان' ile 'in' / 'inne' / 'en' ayırmıyor; ◇ lemma dizisi 'dizi 5 112 17 19' sûre içi 2, nakarat 6)", ('dizi 5 112 17 19', "itteqâ allâh in", '17-19', "biçim farkı (dizi 5 112 17 19): basılmamış eş önek; öneksiz eş koşusu (dizi 5 112 17 19): basılmamış eş → önek kesilmiş sûre içi 5")),
 ("5:112", "'in kâne mu'min'", 3, 'say 5:112 19-21', "harekesiz 'in kuntum mu'minîn' (19-21. kelime)", None),
 ("5:112", "''îsâ ibn meryem'", 3, 'say 5:112 4-6', "harekesiz 'yâ 'îse'bne meryem' (4-6. kelime; biçim öğesi 'yâ' — nida öneki harekesiz kalıpta; ◇ lemma dizisi 'dizi 5 112 4 6' sûre içi 6, harekesiz kalıp 3)", None),
 ("5:114", "''alâ mâ'ide min semâ''", 2, 'say 5:114 8-11', "harekesiz ''aleynâ mâ'ideten mine's-semâ'' (8-11. kelime)", None),
 ("5:114", "''îsâ ibn meryem'", 2, 'say 5:114 2-4', "harekesiz ''îse'bnu meryem' (2-4. kelime; biçim öğesi 'ibn' — ölçüm kalıbı i'râb ve önek eşlerini ayırıyor; ◇ lemma dizisi 'dizi 5 114 2 4' sûre içi 6, nakarat 2)", ('dizi 5 114 2 4', "'îsâ ibn meryem", '2-4', "biçim farkı (dizi 5 114 2 4): basılmamış eş i'râb, önek; 5:78 i'râb, önek; 5:110 i'râb, önek; 5:112 i'râb, önek; basılmamış eş i'râb, önek; öneksiz eş koşusu (dizi 5 114 2 4): basılmamış eş → önek kesilmiş sûre içi 1; 5:78 → önek kesilmiş sûre içi 1; 5:110 → önek kesilmiş sûre içi 3; 5:112 → önek kesilmiş sûre içi 3; basılmamış eş → önek kesilmiş sûre içi 3")),
 ("5:115", "'qâle allâh inne'", 2, 'say 5:115 1-3', "harekesiz 'qâle'llâhu innî' (1-3. kelime)", ('dizi 5 115 1 3', "qâle allâh inne", '1-3', "biçim farkı (dizi 5 115 1 3): basılmamış eş önek")),
 ("5:115", "'fe-men kefera ba'd'", 2, 'say 5:115 6-8 --on', "harekesiz 'fe-men yekfur ba'd' (6-8. kelime)", ('dizi 5 115 6 8', "fe-men kefera ba'd", '6-8', "biçim farkı (dizi 5 115 6 8): basılmamış eş yazım eş")),
 ("5:115", "'ehad min 'âlem'", 2, 'say 5:115 15-17', "harekesiz 'ehaden mine'l-'âlemîn' (15-17. kelime)", None),
]
'''
VF = '''VF_YAZI = {111: {1: "'ve iz'", 8: "'ve bi-rasûlî'", 11: "'ve'şhed'"}, 113: {6: "'ve tatma'inne'", 8: "'ve na'leme'", 12: "'ve nekûne'"}, 114: {16: "'ve âxirinâ'", 17: "'ve âyeten'", 19: "'ve'rzuqnâ'", 20: "'ve ente'"}, 115: {6: "'fe-men'", 10: "'fe-innî'"}}
sys.path.insert(0, '/home/claude/b34/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b34/yap/I_head.py', encoding='utf-8').read() + open('/home/claude/b34/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('ARIZA oluşturucu — bölüm 15-1', 'ARIZA oluşturucu — bölüm 15-2'), ('# blok 33 (5:109-110)', '# blok 34 (5:111-115)'), ('/b33/', '/b34/'), ("es_edat.py', '33'", "es_edat.py', '34'"), ('range(1, 34)', 'range(1, 35)'),
     ("'--plan', '33', '--numarasiz')", "'--plan', '34', '--numarasiz')"),
     ('ariza_5_109_110', 'ariza_5_111_115'), ('(109, 110)', '(111, 115)'), ("'109', '110', '33'", "'111', '115', '34'"), ("'109', '110'", "'111', '115'"),
     ("BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b32.txt', encoding='utf-8').read() + ']')", "BEK = []"),
     ("'30', '31', '32', '33')", "'30', '31', '32', '33', '34')"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_5_b33.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_5_b34.txt'"),
     ]
for a, b in R:
    assert a in out, a
    out = out.replace(a, b)
for l in out.split('\n'):
    for bad in ('b33', "'33'", "'109'", "'110'", '5_109_110'):
        if bad in l and 'nn in' not in l: print('KONTROL', bad, l[:160])
open('/home/claude/b34/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)

src = open('/home/claude/b29/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("5:97", "''alime enne allâh'", 4, 'say 5:97 13-15', "harekesiz 'li-ta'lemû enne'llâh' (13-15. kelime)", ('dizi 5 97 13 15', "'alime enne allâh", '13-15', "biçim farkı (dizi 5 97 13 15): basılmamış eş önek; basılmamış eş fiil çekimi, zamir eki, önek; 5:98 önek")),
 ("5:97", "'allâh 'alime mâ'", 2, 'say 5:97 15-17', "harekesiz 'llâhe ya'lemu mâ' (15-17. kelime)", ('dizi 5 97 15 17', "allâh 'alime mâ", '15-17', "biçim farkı (dizi 5 97 15 17): 5:99 i'râb, önek")),
 ("5:97", "''alime mâ fî'", 2, 'say 5:97 16-18', "harekesiz 'ya'lemu mâ fî' (16-18. kelime)", ('dizi 5 97 16 18', "'alime mâ fî", '16-18', "biçim farkı (dizi 5 97 16 18): basılmamış eş fiil çekimi")),
 ("5:97", "'mâ fî ard'", 2, 'say 5:97 20-22 --on', "önek kesilmiş 've mâ fi'l-ard' (20-22. kelime)", ('dizi 5 97 20 22', "mâ fî ard", '20-22', "biçim farkı (dizi 5 97 20 22): basılmamış eş önek")),
 ("5:98", "''alime enne allâh'", 4, 'say 5:98 1-3', "harekesiz 'i'lemû enne'llâh' (1-3. kelime)", ('dizi 5 98 1 3', "'alime enne allâh", '1-3', "biçim farkı (dizi 5 98 1 3): basılmamış eş önek; basılmamış eş fiil çekimi, zamir eki; 5:97 önek")),
 ("5:98", "'enne allâh şedîd 'iqâb'", 2, 'say 5:98 2-5', "harekesiz 'enne'llâhe şedîdu'l-'iqâb' (2-5. kelime; biçim öğesi — ölçüm kalıbı 'ان' iskeleti 'inne' / 'enne' birleşik; ◇ lemma dizisi 'dizi 5 98 2 5' sûre içi 1)", ('dizi 5 98 2 5', "enne allâh şedîd 'iqâb", '2-5', "nakarat3 'ان' iskeleti 'inne' / 'enne' birleştiriyor: 'enne' dizisi sûre içi 1 + 'inne' dizisi sûre içi 1 (blok 1 R5 satırı) = 2, toplam nakarat3 ile eşit; öneksiz eş koşusu (dizi 5 98 2 5): sûre içi eş yok")),
 ("5:98", "'enne allâh ğafûr rahîm'", 3, 'say 5:98 6-9 --on', "önek kesilmiş 've enne'llâhe ğafûrun rahîm' (6-9. kelime; biçim öğesi — ölçüm kalıbı 'ان' iskeleti 'inne' / 'enne' birleşik; ◇ lemma dizisi 'dizi 5 98 6 9' sûre içi 2)", ('dizi 5 98 6 9', "enne allâh ğafûr rahîm", '6-9', "nakarat3 'ان' iskeleti 'inne' / 'enne' birleştiriyor: 'enne' dizisi sûre içi 2 + 'inne' dizisi sûre içi 1 (blok 13 R5 satırı) = 3, toplam nakarat3 ile eşit; öneksiz eş koşusu (dizi 5 98 6 9): basılmamış eş → önek kesilmiş sûre içi 2")),
 ("5:98", "'allâh ğafûr rahîm'", 5, 'say 5:98 7-9', "harekesiz 'llâhe ğafûrun rahîm' (7-9. kelime)", ('dizi 5 98 7 9', "allâh ğafûr rahîm", '7-9', "biçim farkı (dizi 5 98 7 9): basılmamış eş yazım eş; basılmamış eş yazım eş; basılmamış eş yazım eş; 5:74 i'râb, önek")),
 ("5:99", "'allâh 'alime mâ'", 2, 'say 5:99 6-8 --on', "önek kesilmiş 've'llâhu ya'lemu mâ' (6-8. kelime)", ('dizi 5 99 6 8', "allâh 'alime mâ", '6-8', "biçim farkı (dizi 5 99 6 8): 5:97 i'râb, önek")),
]
'''
VF = '''VF_YAZI = {97: {8: "'ve'ş-şehre'", 10: "'ve'l-hedye'", 11: "'ve'l-qalâ'ide'", 20: "'ve mâ'", 23: "'ve enne'"}, 98: {6: "'ve enne'"}, 99: {6: "'ve'llâhu'", 10: "'ve mâ'"}, 100: {5: "'ve't-tayyibu'", 6: "'ve lev'", 10: "'fe'ttequ'"}}
sys.path.insert(0, '/home/claude/b30/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b30/yap/I_head.py', encoding='utf-8').read() + open('/home/claude/b30/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('ARIZA oluşturucu — bölüm 13-1', 'ARIZA oluşturucu — bölüm 13-2'), ('# blok 29 (5:94-96)', '# blok 30 (5:97-100)'), ('/b29/', '/b30/'), ("es_edat.py', '29'", "es_edat.py', '30'"), ('range(1, 30)', 'range(1, 31)'),
     ("'--plan', '29', '--numarasiz')", "'--plan', '30', '--numarasiz')"),
     ('ariza_5_94_96', 'ariza_5_97_100'), ('(94, 96)', '(97, 100)'), ("'94', '96', '29'", "'97', '100', '30'"), ("'94', '96'", "'97', '100'"),
     ("BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b28.txt', encoding='utf-8').read() + ']')", "BEK = []"),
     ("'27', '28', '29')", "'27', '28', '29', '30')"),
     ]
for a, b in R:
    assert a in out, a
    out = out.replace(a, b)
out = out.replace("geriye_donuk_5_b30.txt", "geriye_donuk_5_b29.txt")
for l in out.split('\n'):
    for bad in ('b29', "'29'", "'94'", "'96'", '5_94_96'):
        if bad in l and 'nn in' not in l and 'geriye_donuk_5_b29' not in l: print('KONTROL', bad, l[:160])
open('/home/claude/b30/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)

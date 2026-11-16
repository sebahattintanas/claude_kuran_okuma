src = open('/home/claude/b25/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("5:82", "'ellezî qâle inne nasrânî'", 2, 'say 5:82 15-18', "harekesiz 'llezîne qâlû innâ nasârâ' (15-18. kelime; biçim öğesi 'innâ' — ölçüm kalıbında bitişik zamirli yazım)", None),
 ("5:84", "'mâ câ'e min'", 2, 'say 5:84 6-8 --on', "önek kesilmiş 've mâ câ'enâ min' (6-8. kelime)", ('dizi 5 84 6 8', "mâ câ'e min", '6-8', "biçim farkı (dizi 5 84 6 8): basılmamış eş önek")),
 ("5:84", "'câ'e min haqq'", 2, 'say 5:84 7-9', "harekesiz 'câ'enâ mine'l-haqq' (7-9. kelime)", ('dizi 5 84 7 9', "câ'e min haqq", '7-9', "biçim farkı (dizi 5 84 7 9): basılmamış eş zamir eki")),
 ("5:84", "'âmene allâh mâ'", 2, 'say 5:84 4-6', "harekesiz 'nu'minu bi'llâhi ve mâ' (4-6. kelime)", ('dizi 5 84 4 6', "âmene allâh mâ", '4-6', "biçim farkı (dizi 5 84 4 6): basılmamış eş zamir eki")),
 ("5:85", "'cenne cerey min taht neher xâlid fî' (LEM 'cerey' (morph LEM ham biçim))", 2, 'say 5:85 5-11', "harekesiz 'cennâtin tecrî min tahtihe'l-enhâru xâlidîne fîhâ' (5-11. kelime)", ('dizi 5 85 5 11', "cenne cerey min taht neher xâlid fî", '5-11', "biçim farkı (dizi 5 85 5 11): basılmamış eş yazım eş")),
 ("5:85", "'cenne cerey min taht neher' (LEM 'cerey' (morph LEM ham biçim))", 3, 'say 5:85 5-9', "harekesiz 'cennâtin tecrî min tahtihe'l-enhâr' (5-9. kelime)", None),
]
'''
VF = '''VF_YAZI = {82: {8: "'ve'llezîne'", 10: "'ve le-tecidenne'", 23: "'ve ruhbânen'", 24: "'ve ennehum'"}, 83: {1: "'ve izâ'", 19: "'fe'ktubnâ'"}, 84: {1: "'ve mâ lenâ'", 6: "'ve mâ câ'enâ'", 10: "'ve natma'u'"}, 85: {1: "'fe-esâbehumu'", 12: "'ve zâlike'"}, 86: {1: "'ve'llezîne'", 3: "'ve kezzebû'"}}
sys.path.insert(0, '/home/claude/b26/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b26/yap/I_parca.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('ARIZA oluşturucu — bölüm 11-1', 'ARIZA oluşturucu — bölüm 11-2'), ('# blok 25 (5:78-81)', '# blok 26 (5:82-86)'), ('/b25/', '/b26/'), ("es_edat.py', '25'", "es_edat.py', '26'"), ('range(1, 26)', 'range(1, 27)'),
     ("'--plan', '25', '--numarasiz')", "'--plan', '26', '--numarasiz')"),
     ('ariza_5_78_81', 'ariza_5_82_86'), ('geriye_donuk_5_b25.txt', 'geriye_donuk_5_b26.txt'), ('(78, 81)', '(82, 86)'), ("'78', '81', '25'", "'82', '86', '26'"), ("'78', '81'", "'82', '86'"),
     ("BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b24.txt', encoding='utf-8').read() + ']')", "BEK = []"),
     ("BOL = \"'Tebliğ emri; İsrâiloğullarının misakı; Mesih ve teslis'\"", "BOL = \"'Lanetlenenler; Nasârâ'nın yakınlığı; gözyaşı dökenler'\""),
     ("'21', '22', '23', '24', '25')", "'21', '22', '23', '24', '25', '26')"),
     ("MEDF += ' — fark yok, yeni eş yok' if all(n == m for k, n, m in MFARK) else ' — FARK VAR'",
      "MEDF += ' — fark yok, yeni eş yok' if all(n == m for k, n, m in MFARK) else \" — FARK VAR: 'say 5:86 2-4' meddesiz koşusu okunmamış 2 ayet (sûre içi 0) daha buluyor ('bi-âyâtinâ' medde yazım farkı); sûre içi sayı değişmiyor, sayım cümlesi meddeli koşuyla; tam okuma sonu\""),
     ]
for a, b in R:
    assert a in out, a
    out = out.replace(a, b)
for l in out.split('\n'):
    for bad in ('b25', "'25'", "'78'", "'81'", '5_78_81'):
        if bad in l and 'nn in' not in l and 'geriye_donuk_5_b25' not in l: print('KONTROL', bad, l[:200])
open('/home/claude/b26/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)

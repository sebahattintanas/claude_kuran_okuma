import re
src = open('/home/claude/b20/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("5:64", "'zâde kesîr min mâ enzele ilâ min rabb tuğyân kufr'", 2, 'say 5:64 17-26 --on', "önek kesilmiş 've le-yezîdenne kesîran minhum mâ unzile ileyke min rabbike tuğyânen ve kufran' (17-26. kelime)", None),
 ("5:64", "'beyn 'adâve bağdâ' ilâ yevm qiyâme'", 2, 'say 5:64 28-33', "harekesiz 'beynehumu'l-'adâvete ve'l-bağdâ'e ilâ yevmi'l-qiyâme' (28-33. kelime)", ('dizi 5 64 28 33', "beyn 'adâve bağdâ' ilâ yevm qiyâme", '28-33', "biçim farkı — harekesiz kalıp sûre içi basılmış eşin hareke yazımını ayırıyor")),
 ("5:64", "'mâ enzele ilâ min rabb'", 3, 'say 5:64 20-24', "harekesiz 'mâ unzile ileyke min rabbik' (20-24. kelime)", None),
 ("5:64", "'se'â fî ard fesâd'", 2, 'say 5:64 40-43 --on', "önek kesilmiş 've yes'avne fi'l-ardi fesâden' (40-43. kelime)", None),
 ("5:64", "'beyn 'adâve bağdâ''", 3, 'say 5:64 28-30', "harekesiz 'beynehumu'l-'adâvete ve'l-bağdâ'e' (28-30. kelime)", ('dizi 5 64 28 30', "beyn 'adâve bağdâ'", '28-30', "biçim farkı — harekesiz kalıp zamir eki ve i'râb yazımını ayırıyor")),
 ("5:66", "'eqâme tevrâ incîl mâ enzele'", 2, 'say 5:66 3-7', "harekesiz 'eqâmu't-tevrâte ve'l-incîle ve mâ unzile' (3-7. kelime)", ('dizi 5 66 3 7', "eqâme tevrâ incîl mâ enzele", '3-7', "biçim farkı — harekesiz kalıp fiil çekimini ayırıyor")),
]
'''
VF = '''VF_YAZI = {64: {1: "'ve qâleti'", 8: "'ve lu'inû'", 17: "'ve le-yezîdenne'", 26: "'ve kufran'", 27: "'ve elqaynâ'", 30: "'ve'l-bağdâ'e'", 40: "'ve yes'avne'", 44: "'ve'llâhu'"}, 65: {1: "'ve lev'", 6: "'ve'tteqav'", 10: "'ve le-edxalnâhum'"}, 66: {1: "'ve lev'", 5: "'ve'l-incîle'", 6: "'ve mâ'", 14: "'ve min'", 20: "'ve kesîrun'"}}
sys.path.insert(0, '/home/claude/b21/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b21/yap/I_parca.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('/b20/', '/b21/'), ("es_edat.py', '20'", "es_edat.py', '21'"), ('range(1, 21)', 'range(1, 22)'), ("'--plan', '20'", "'--plan', '21'"), ("'59', '63', EMS", "'64', '66', EMS"),
     ('ariza_5_59_63', 'ariza_5_64_66'), ('(59, 63)', '(64, 66)'), ("'59', '63', '20'", "'64', '66', '21'"), ("'59', '63')", "'64', '66')"),
     ("BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b19.txt', encoding='utf-8').read() + ']')", "BEK = []")]
for a, b in R:
    assert a in out, a
    out = out.replace(a, b)
out = re.sub(r"for nn in \([^)]*\)", "for nn in ('06', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21')", out)
for l in out.split('\n'):
    for bad in ('b20', "'20'", "'59'", "'63'"):
        if bad in l and 'nn in' not in l: print('KONTROL', bad, l[:160])
open('/home/claude/b21/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)

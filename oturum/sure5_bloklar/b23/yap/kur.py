import re
src = open('/home/claude/b22/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("5:72", "'qad kefera ellezî qâle inne allâh _ mesîh ibn meryem qâle'", 2, 'say 5:72 1-11 --on', "önek kesilmiş 'le-qad kefera'llezîne qâlû inna'llâhe huve'l-mesîhu'bnu meryeme ve qâle' (1-11. kelime)", ('dizi 5 72 1 11', "qad kefera ellezî qâle inne allâh _ mesîh ibn meryem qâle", '1-11', "biçim farkı (dizi 5 72 1 11): 5:17 fiil çekimi, önek")),
 ("5:72", "'qad kefera ellezî qâle inne allâh'", 3, 'say 5:72 1-6', "harekesiz 'le-qad kefera'llezîne qâlû inna'llâh' (1-6. kelime)", None),
 ("5:72", "''abede allâh rabb rabb'", 2, 'say 5:72 15-18 --on', "önek kesilmiş ''budu'llâhe rabbî ve rabbekum' (15-18. kelime)", None),
 ("5:72", "'mesîh ibn meryem'", 3, 'say 5:72 8-10', "harekesiz 'l-mesîhu'bnu meryem' (8-10. kelime)", None),
 ("5:73", "'qad kefera ellezî qâle inne allâh'", 3, 'say 5:73 1-6', "harekesiz 'le-qad kefera'llezîne qâlû inna'llâh' (1-6. kelime)", None),
 ("5:73", "'ellezî kefera min'", 2, 'say 5:73 21-23', "harekesiz 'llezîne keferû minhum' (21-23. kelime; biçim öğesi 'minhum' — ölçüm kalıbında 'min' + 3MP zamir birleşik biçim; ◇ lemma dizisi 'dizi 5 73 21 23' sûre içi 4, 'min' + ad eşleri dahil)", None),
 ("5:74", "'allâh ğafûr rahîm'", 5, 'say 5:74 6-8 --on', "önek kesilmiş 've'llâhu ğafûrun rahîm' (6-8. kelime)", ('dizi 5 74 6 8', "allâh ğafûr rahîm", '6-8', "biçim farkı (dizi 5 74 6 8): basılmamış eş i'râb, önek; basılmamış eş i'râb, önek; basılmamış eş i'râb, önek; basılmamış eş i'râb, önek")),
]
'''
VF = '''VF_YAZI = {71: {1: "'ve hasibû'", 5: "'fe-'amû'", 6: "'ve sammû'", 13: "'ve sammû'", 16: "'ve'llâhu'"}, 72: {11: "'ve qâle'", 18: "'ve rabbekum'", 23: "'fe-qad'", 28: "'ve me'vâhu'", 30: "'ve mâ'"}, 73: {9: "'ve mâ'", 15: "'ve in'"}, 74: {1: "'fe-lâ'", 5: "'ve yestağfirûnehû'", 6: "'ve'llâhu'"}}
sys.path.insert(0, '/home/claude/b23/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b23/yap/I_parca.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('# blok 20 (5:59-63) ARIZA oluşturucu — bölüm 9-1', '# blok 23 (5:71-74) ARIZA oluşturucu — bölüm 10-2'), ('/b22/', '/b23/'), ("es_edat.py', '22'", "es_edat.py', '23'"), ('range(1, 23)', 'range(1, 24)'), ("'--plan', '22'", "'--plan', '23'"), ("'67', '70', EMS", "'71', '74', EMS"),
     ('ariza_5_67_70', 'ariza_5_71_74'), ('(67, 70)', '(71, 74)'), ("'67', '70', '22'", "'71', '74', '23'"), ("'67', '70')", "'71', '74')"),
     ("geriye_donuk_5_b21.txt", "geriye_donuk_5_b23.txt"), ("BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b21.txt', encoding='utf-8').read() + ']')", "BEK = []")]
for a, b in R:
    assert a in out, a
    out = out.replace(a, b)
out = re.sub(r"for nn in \([^)]*\)", "for nn in ('06', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23')", out)
for l in out.split('\n'):
    for bad in ('b22', "'22'", "'67'", "'70'"):
        if bad in l and 'nn in' not in l: print('KONTROL', bad, l[:160])
open('/home/claude/b23/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)

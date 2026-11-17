src = open('/home/claude/b31/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("5:106", "'eyy ellezî âmene'", 16, 'say 5:106 1-3', "harekesiz 'yâ eyyuhe'llezîne âmenû' (1-3. kelime)", None),
 ("5:106", "'zû 'adl min'", 2, 'say 5:106 13-15', "harekesiz 'zevâ 'adlin minkum' (13-15. kelime)", None),
 ("5:106", "'inne izen min'", 2, 'say 5:106 48-50', "harekesiz 'innâ izen le-mine' (48-50. kelime)", None),
 ("5:107", "'inne izen min'", 2, 'say 5:107 23-25', "harekesiz 'innâ izen le-mine' (23-25. kelime)", None),
 ("5:108", "'allâh lâ hedâ qavm'", 3, 'say 5:108 18-21 --on', "önek kesilmiş 've'llâhu lâ yehdi'l-qavm' (18-21. kelime)", ('dizi 5 108 18 21', "allâh lâ hedâ qavm", '18-21', "biçim farkı (dizi 5 108 18 21): basılmamış eş i'râb, önek; basılmamış eş i'râb, önek")),
]
'''
VF = '''VF_YAZI = {106: {25: "'fe-esâbetkum'", 32: "'fe-yuqsimâni'", 40: "'ve lev'", 44: "'ve lâ'"}, 107: {1: "'fe-in'", 7: "'fe-âxarâni'", 15: "'fe-yuqsimâni'", 21: "'ve mâ'"}, 108: {15: "'ve'ttequ'", 17: "'ve'sme'û'", 18: "'ve'llâhu'"}}
sys.path.insert(0, '/home/claude/b32/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b32/yap/I_head.py', encoding='utf-8').read() + open('/home/claude/b32/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('ARIZA oluşturucu — bölüm 14-1', 'ARIZA oluşturucu — bölüm 14-2'), ('# blok 31 (5:101-105)', '# blok 32 (5:106-108)'), ('/b31/', '/b32/'), ("es_edat.py', '31'", "es_edat.py', '32'"), ('range(1, 32)', 'range(1, 33)'),
     ("'--plan', '31', '--numarasiz')", "'--plan', '32', '--numarasiz')"),
     ('ariza_5_101_105', 'ariza_5_106_108'), ('(101, 105)', '(106, 108)'), ("'101', '105', '31'", "'106', '108', '32'"), ("'101', '105'", "'106', '108'"),
     ("BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b30.txt', encoding='utf-8').read() + ']')", "BEK = []"),
     ("'29', '30', '31')", "'29', '30', '31', '32')"),
     ]
for a, b in R:
    assert a in out, a
    out = out.replace(a, b)
for l in out.split('\n'):
    for bad in ('b31', "'31'", "'101'", "'105'", '5_101_105'):
        if bad in l and 'nn in' not in l: print('KONTROL', bad, l[:160])
open('/home/claude/b32/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)

# sûre 7 blok 20 ARIZA oluşturucusu — sûre 6 blok 40 üreticisinden (s6/b40/yap/ariza_yap.py); bölüm 7-3
import re
src = open('/home/claude/s6/b40/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('\nI = [\n') + 1; k1 = src.index('\ndef yaz(II):')
R5 = '''R5 = [
 ('7:70', "'etâ mâ ve'ade in kâne min'", 2, 'say 7:70 11-16', "harekesiz 'fe'tinâ bi-mâ te'idunâ in kunte mine' (11-16. kelime)", ('dizi 7 70 11 16', "etâ mâ ve'ade in kâne min", '11-16', 'biçim farkı (dizi 7 70 11 16): basılmamış eş önek; öneksiz eş koşusu (dizi 7 70 11 16): basılmamış eş → önek kesilmiş sûre içi 1')),
 ('7:70', "'in kâne min sâdiq'", 2, 'say 7:70 14-17', "harekesiz 'in kunte mine's-sâdiqîn' (14-17. kelime)", ('dizi 7 70 14 17', 'in kâne min sâdiq', '14-17', 'biçim farkı (dizi 7 70 14 17): basılmamış eş yazım eş')),
 ('7:70', "'in kâne min'", 3, 'say 7:70 14-16', "harekesiz 'in kunte mine' (14-16. kelime)", ('dizi 7 70 14 16', 'in kâne min', '14-16', 'biçim farkı (dizi 7 70 14 16): basılmamış eş yazım eş; basılmamış eş yazım eş')),
 ('7:72', "'ellezî kezzebe âye'", 5, 'say 7:72 8-10', "harekesiz 'llezîne kezzebû bi-âyâtinâ' (8-10. kelime); biçim öğesi 'ellezî' öneki (lemma dizisi sûre içi 8, nakarat3 5)", ('dizi 7 72 8 10', 'ellezî kezzebe âye', '8-10', 'biçim farkı (dizi 7 72 8 10): 7:36 önek; 7:40 yazım eş; 7:64 yazım eş; basılmamış eş önek; basılmamış eş yazım eş; basılmamış eş yazım eş; basılmamış eş önek; öneksiz eş koşusu (dizi 7 72 8 10): 7:36 → önek kesilmiş sûre içi 3; 7:40 → önek kesilmiş sûre içi 7; 7:64 → önek kesilmiş sûre içi 1; basılmamış eş → önek kesilmiş sûre içi 3; basılmamış eş → önek kesilmiş sûre içi 7; basılmamış eş → önek kesilmiş sûre içi 7; basılmamış eş → önek kesilmiş sûre içi 3')),
 ('7:72', "'encâ ellezî ma'a'", 2, 'say 7:72 1-3', "harekesiz 'fe-enceynâhu ve'llezîne me'ahû' (1-3. kelime)", ('dizi 7 72 1 3', "encâ ellezî ma'a", '1-3', 'biçim farkı (dizi 7 72 1 3): 7:64 yazım eş')),
]
'''
VF = '''VF_YAZI = {70: {2: "'e-ci'tenâ'", 3: "'li-na'bude'", 6: "'ve nezera'", 11: "'fe'tinâ'", 12: "'bi-mâ'"}, 71: {8: "'ve ğadabun'", 9: "'e-tucâdilûnenî'", 14: "'ve âbâ'ukum'", 18: "'bihâ'", 21: "'fe'ntazirû'"}, 72: {1: "'fe-enceynâhu'", 2: "'ve'llezîne'", 4: "'bi-rahmetin'", 6: "'ve qata'nâ'", 10: "'bi-âyâtinâ'", 11: "'ve mâ'"}}
sys.path.insert(0, '/home/claude/b20/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b20/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('# sûre 6 blok 40 (6:161-165) ARIZA oluşturucu — bölüm 19-2', '# sûre 7 blok 20 (7:70-72) ARIZA oluşturucu — bölüm 7-3'), ('/home/claude/b40/', '/home/claude/b20/'),
     ("es_edat.py', '40'", "es_edat.py', '20'"), ('range(1, 41)', 'range(1, 21)'),
     ("'--plan', '40', '--numarasiz')", "'--plan', '20', '--numarasiz')"),
     ('ariza_6_161_165', 'ariza_7_70_72'), ('bag_6_161_165', 'bag_7_70_72'), ('(161, 165)', '(70, 72)'), ("'161', '165', '40'", "'70', '72', '20'"), ("'161', '165'", "'70', '72'"),
     ("_ON = {'6:161', '6:162', '6:163', '6:164', '6:165'}", "_ON = {'7:70', '7:71', '7:72'}"), ('range(161, 166)', 'range(70, 73)'),
     ("x.startswith('6:')", "x.startswith('7:')"), ("== '6:%d' % a_", "== '7:%d' % a_"), ("return '6:%d: %s'", "return '7:%d: %s'"), ("r'\\b6:%d:\\d+'", "r'\\b7:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_6_*.txt')", "glob.glob('/home/claude/yamalar/ariza_7_*.txt')"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_6_b38k.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_7_b17k.txt'"),
     ("BOL = \"'Bekledikleri; dosdoğru din; yeryüzünün halifeleri'\"", "BOL = \"'Nûh ve kavmi; Hûd ve Âd'\""),
     ("for _n in range(7, 35): _J", "for _n in range(7, 43): _J"), ("B33, B34 = [_R['B%d' % _n].splitlines() for _n in range(6, 35)]", "B33, B34, B35, B36, B37, B38, B39, B40, B41, B42 = [_R['B%d' % _n].splitlines() for _n in range(6, 43)]"),
     ("'B34_HEPSI': (B34[-1] if B34 else '?'),", "'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'), 'B37_HEPSI': (B37[-1] if B37 else '?'), 'B38_HEPSI': (B38[-1] if B38 else '?'), 'B39_HEPSI': (B39[-1] if B39 else '?'), 'B40_HEPSI': (B40[-1] if B40 else '?'), 'B41_HEPSI': (B41[-1] if B41 else '?'), 'B42_HEPSI': (B42[-1] if B42 else '?'),"),
     ("B32, B33, B34): print(", "B32, B33, B34, B35, B36, B37, B38, B39, B40, B41, B42): print("),
     ("sûre 6'nın okunmuş bütün ARIZA dosyaları", "sûre 7'nin okunmuş bütün ARIZA dosyaları"),
     ]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
_AN = """ANILIS = "7:72 kök قطع ('qata'nâ' 6. kelime — kesme): tetik listesinde yok"\n"""
out = re.sub(r'ANILIS = ".*"\n', lambda m_: _AN, out)
out = re.sub(r"for nn in \('01', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'):", out)
for l in out.split('\n'):
    for bad in ('b40', "'40'", "'161'", "'165'", '6_161_165', "'6:", 's6/'):
        if bad in l: print('KONTROL', bad, l[:160])
open('/home/claude/b20/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)

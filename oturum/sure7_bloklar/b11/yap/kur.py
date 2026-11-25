# sûre 7 blok 11 ARIZA oluşturucusu — sûre 6 blok 40 üreticisinden (s6/b40/yap/ariza_yap.py); bölüm açılışı, BEK bekleyen_ariza_7_b02.txt'ten
import re
src = open('/home/claude/s6/b40/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('\nI = [\n') + 1; k1 = src.index('\ndef yaz(II):')
R5 = '''R5 = [
 ("7:38", "'min cinn ins'", 2, 'say 7:38 9-11', "harekesiz 'mine'l-cinni ve'l-insi' (9-11. kelime)", ('dizi 7 38 9 11', "min cinn ins", '9-11', "biçim farkı (dizi 7 38 9 11): basılmamış eş yazım eş")),
 ("7:39", "'bi-mâ kâne kesebe'", 2, 'say 7:39 12-14', "harekesiz 'bimâ kuntum teksibûn' (12-14. kelime)", ('dizi 7 39 12 14', "mâ kâne kesebe", '12-14', "biçim farkı (dizi 7 39 12 14): basılmamış eş fiil çekimi, zamir eki")),
 ("7:40", "'kezzebe âye istekbere 'an'", 2, 'say 7:40 3-6', "harekesiz 'kezzebû bi-âyâtinâ ve'stekberû 'anhâ' (3-6. kelime)", ('dizi 7 40 3 6', "kezzebe âye istekbere 'an", '3-6', "biçim farkı (dizi 7 40 3 6): 7:36 yazım eş")),
 ("7:40", "'ellezî kezzebe âye'", 5, 'say 7:40 2-4', "harekesiz 'llezîne kezzebû bi-âyâtinâ' (2-4. kelime); biçim öğesi 'ellezî' öneki (lemma dizisi sûre içi 8, nakarat3 5)", ('dizi 7 40 2 4', "ellezî kezzebe âye", '2-4', "biçim farkı (dizi 7 40 2 4): 7:36 önek; basılmamış eş yazım eş; basılmamış eş yazım eş; basılmamış eş önek; basılmamış eş yazım eş; basılmamış eş yazım eş; basılmamış eş önek; öneksiz eş koşusu (dizi 7 40 2 4): 7:36 → önek kesilmiş sûre içi 3; basılmamış eş → önek kesilmiş sûre içi 1; basılmamış eş → önek kesilmiş sûre içi 7; basılmamış eş → önek kesilmiş sûre içi 3; basılmamış eş → önek kesilmiş sûre içi 7; basılmamış eş → önek kesilmiş sûre içi 7; basılmamış eş → önek kesilmiş sûre içi 3")),
]
'''
VF = '''VF_YAZI = {38: {11: "'ve'l-insi'", 30: "'fe-âtihim'", 38: "'ve lâkin'"}, 39: {1: "'ve qâlet'", 4: "'fe-mâ'", 10: "'fe-zûqu'"}, 40: {5: "'ve'stekberû'", 12: "'ve lâ'", 21: "'ve kezâlike'"}, 41: {5: "'ve min'", 8: "'ve kezâlike'"}}
sys.path.insert(0, '/home/claude/b11/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b11/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('# sûre 6 blok 40 (6:161-165) ARIZA oluşturucu — bölüm 19-2', '# sûre 7 blok 11 (7:38-41) ARIZA oluşturucu — bölüm 4-2'), ('/home/claude/b40/', '/home/claude/b11/'),
     ("es_edat.py', '40'", "es_edat.py', '11'"), ('range(1, 41)', 'range(1, 12)'),
     ("'--plan', '40', '--numarasiz')", "'--plan', '11', '--numarasiz')"),
     ('ariza_6_161_165', 'ariza_7_38_41'), ('bag_6_161_165', 'bag_7_38_41'), ('(161, 165)', '(38, 41)'), ("'161', '165', '40'", "'38', '41', '11'"), ("'161', '165'", "'38', '41'"),
     ("_ON = {'6:161', '6:162', '6:163', '6:164', '6:165'}", "_ON = {'7:38', '7:39', '7:40', '7:41'}"), ('range(161, 166)', 'range(38, 42)'),
     ("x.startswith('6:')", "x.startswith('7:')"), ("== '6:%d' % a_", "== '7:%d' % a_"), ("return '6:%d: %s'", "return '7:%d: %s'"), ("r'\\b6:%d:\\d+'", "r'\\b7:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_6_*.txt')", "glob.glob('/home/claude/yamalar/ariza_7_*.txt')"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_6_b38k.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_7_b09k.txt'"),
     ("BOL = \"'Bekledikleri; dosdoğru din; yeryüzünün halifeleri'\"", "BOL = \"'Elçiler gelince; yalanlayanların ateşte çekişmesi'\""),
     ("for _n in range(7, 35): _J", "for _n in range(7, 39): _J"), ("B33, B34 = [_R['B%d' % _n].splitlines() for _n in range(6, 35)]", "B33, B34, B35, B36, B37, B38 = [_R['B%d' % _n].splitlines() for _n in range(6, 39)]"),
     ("'B34_HEPSI': (B34[-1] if B34 else '?'),", "'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'), 'B37_HEPSI': (B37[-1] if B37 else '?'), 'B38_HEPSI': (B38[-1] if B38 else '?'),"),
     ("B32, B33, B34): print(", "B32, B33, B34, B35, B36, B37, B38): print("),
     ("sûre 6'nın okunmuş bütün ARIZA dosyaları", "sûre 7'nin okunmuş bütün ARIZA dosyaları"),
     ]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
_AN = """ANILIS = "7:38 kök خلو ('xalet' 6. kelime — gelip geç-): tetik listesinde yok; 7:38 kök قبل ('qablikum' 8. kelime — önce): tetik listesinde yok; 7:38 kök كلل ('kullemâ' 14. kelime — morph T, zaman): tetik listesinde yok; 7:38 'izâ' (20. kelime — morph T, zaman); 7:38 kök جمع ('cemî'an' 23. kelime — hepsi): tetik listesinde yok; 7:38 kök أخر ('uxrâhum' 25. kelime — sonraki): tetik listesinde yok; 7:39 kök أخر ('li-uxrâhum' 3. kelime — sonraki): tetik listesinde yok; 7:40 kök خيط ('l-xiyâti' 20. kelime — iğne): tetik listesinde yok"\n"""
out = re.sub(r'ANILIS = ".*"\n', lambda m_: _AN, out)
out = re.sub(r"for nn in \('01', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11'):", out)
for l in out.split('\n'):
    for bad in ('b40', "'40'", "'161'", "'165'", '6_161_165', "'6:", 's6/'):
        if bad in l: print('KONTROL', bad, l[:160])
open('/home/claude/b11/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)

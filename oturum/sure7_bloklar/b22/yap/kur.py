# sûre 7 blok 21 ARIZA oluşturucusu — sûre 6 blok 40 üreticisinden (s6/b40/yap/ariza_yap.py); bölüm 8-2
import re
src = open('/home/claude/s6/b40/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('\nI = [\n') + 1; k1 = src.index('\ndef yaz(II):')
R5 = '''R5 = [
 ('7:77', "'etâ mâ ve'ade in kâne min'", 2, 'say 7:77 9-14', "harekesiz 'i'tinâ bi-mâ te'idunâ in kunte mine' (9-14. kelime)", ('dizi 7 77 9 14', "etâ mâ ve'ade in kâne min", '9-14', 'biçim farkı (dizi 7 77 9 14): 7:70 önek; öneksiz eş koşusu (dizi 7 77 9 14): 7:70 → önek kesilmiş sûre içi 1')),
 ('7:77', "'in kâne min'", 3, 'say 7:77 12-14', "harekesiz 'in kunte mine' (12-14. kelime)", ('dizi 7 77 12 14', 'in kâne min', '12-14', 'biçim farkı (dizi 7 77 12 14): 7:70 yazım eş; basılmamış eş yazım eş')),
 ('7:78', "'exaze racfe esbaha fî dâr câsim'", 2, 'say 7:78 1-6', "harekesiz 'fe-exazethumu'r-racfetu fe-esbahû fî dârihim câsimîn' (1-6. kelime)", ('dizi 7 78 1 6', 'exaze racfe esbaha fî dâr câsim', '1-6', 'biçim farkı (dizi 7 78 1 6): basılmamış eş yazım eş')),
 ('7:79', "'tevellâ 'an qâle qavm qad ebleğu risâle rabb nesahu _'", 2, 'say 7:79 1-10', "harekesiz 'fe-tevellâ 'anhum ve qâle yâ qavmi le-qad ebleğtukum risâlete rabbî ve nasahtu lekum' (1-10. kelime)", ('dizi 7 79 1 10', "tevellâ 'an qâle qavm qad ebleğu risâle rabb nesahu _", '1-10', 'biçim farkı (dizi 7 79 1 10): basılmamış eş yazım eş')),
 ('7:79', "'risâle rabb nesahu _'", 3, 'say 7:79 7-10', "harekesiz 'risâlete rabbî ve nasahtu lekum' (7-10. kelime)", ('dizi 7 79 7 10', 'risâle rabb nesahu _', '7-10', 'biçim farkı (dizi 7 79 7 10): 7:62 zamir eki; basılmamış eş yazım eş')),
]
'''
VF = '''VF_YAZI = {76: {5: "'bi'llezî'", 7: "'bihî'"}, 77: {1: "'fe-'aqarû'", 3: "'ve 'atev'", 7: "'ve qâlû'", 8: "'yâ sâlihu'", 10: "'bi-mâ'"}, 78: {1: "'fe-exazethumu'", 3: "'fe-esbahû'"}, 79: {1: "'fe-tevellâ'", 3: "'ve qâle'", 4: "'yâ qavmi'", 5: "'le-qad'", 9: "'ve nasahtu'", 10: "'lekum'", 11: "'ve lâkin'"}}
sys.path.insert(0, '/home/claude/b22/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b22/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('# sûre 6 blok 40 (6:161-165) ARIZA oluşturucu — bölüm 19-2', '# sûre 7 blok 22 (7:76-79) ARIZA oluşturucu — bölüm 8-2'), ('/home/claude/b40/', '/home/claude/b22/'),
     ("es_edat.py', '40'", "es_edat.py', '22'"), ('range(1, 41)', 'range(1, 23)'),
     ("'--plan', '40', '--numarasiz')", "'--plan', '22', '--numarasiz')"),
     ('ariza_6_161_165', 'ariza_7_76_79'), ('bag_6_161_165', 'bag_7_76_79'), ('(161, 165)', '(76, 79)'), ("'161', '165', '40'", "'76', '79', '22'"), ("'161', '165'", "'76', '79'"),
     ("_ON = {'6:161', '6:162', '6:163', '6:164', '6:165'}", "_ON = {'7:76', '7:77', '7:78', '7:79'}"), ('range(161, 166)', 'range(76, 80)'),
     ("x.startswith('6:')", "x.startswith('7:')"), ("== '6:%d' % a_", "== '7:%d' % a_"), ("return '6:%d: %s'", "return '7:%d: %s'"), ("r'\\b6:%d:\\d+'", "r'\\b7:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_6_*.txt')", "glob.glob('/home/claude/yamalar/ariza_7_*.txt')"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_6_b38k.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_7_b20k.txt'"),
     ("BOL = \"'Bekledikleri; dosdoğru din; yeryüzünün halifeleri'\"", "BOL = \"'Sâlih ve Semûd; Lût ve kavmi'\""),
     ("for _n in range(7, 35): _J", "for _n in range(7, 44): _J"), ("B33, B34 = [_R['B%d' % _n].splitlines() for _n in range(6, 35)]", "B33, B34, B35, B36, B37, B38, B39, B40, B41, B42, B43 = [_R['B%d' % _n].splitlines() for _n in range(6, 44)]"),
     ("'B34_HEPSI': (B34[-1] if B34 else '?'),", "'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'), 'B37_HEPSI': (B37[-1] if B37 else '?'), 'B38_HEPSI': (B38[-1] if B38 else '?'), 'B39_HEPSI': (B39[-1] if B39 else '?'), 'B40_HEPSI': (B40[-1] if B40 else '?'), 'B41_HEPSI': (B41[-1] if B41 else '?'), 'B42_HEPSI': (B42[-1] if B42 else '?'), 'B43_HEPSI': (B43[-1] if B43 else '?'),"),
     ("B32, B33, B34): print(", "B32, B33, B34, B35, B36, B37, B38, B39, B40, B41, B42, B43): print("),
     ("sûre 6'nın okunmuş bütün ARIZA dosyaları", "sûre 7'nin okunmuş bütün ARIZA dosyaları"),
     ]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
_AN = """ANILIS = "7:78 kök صبح ('fe-esbahû' 3. kelime — oluş fiili): tetik listesinde yok; 7:79 kök ولي ('fe-tevellâ' 1. kelime — yüz çevirme): tetik listesinde yok"\n"""
out = re.sub(r'ANILIS = ".*"\n', lambda m_: _AN, out)
out = re.sub(r"for nn in \('01', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22'):", out)
for l in out.split('\n'):
    for bad in ('b40', "'40'", "'161'", "'165'", '6_161_165', "'6:", 's6/'):
        if bad in l: print('KONTROL', bad, l[:160])
open('/home/claude/b22/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)

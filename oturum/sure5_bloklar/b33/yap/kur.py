src = open('/home/claude/b32/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("5:109", "'inne _ 'allâm ğuyûb'", 2, 'say 5:109 12-15', "harekesiz 'inneke ente 'allâmu'l-ğuyûb' (12-15. kelime)", ('dizi 5 109 12 15', "inne _ 'allâm ğuyûb", '12-15', "biçim farkı (dizi 5 109 12 15): basılmamış eş yazım eş")),
 ("5:110", "'iz qâle allâh 'îsâ ibn meryem'", 2, 'say 5:110 1-6', "harekesiz 'iz qâle'llâhu yâ 'îse'bne meryem' (1-6. kelime)", ('dizi 5 110 1 6', "iz qâle allâh 'îsâ ibn meryem", '1-6', "biçim farkı (dizi 5 110 1 6): basılmamış eş önek")),
 ("5:110", "''îsâ ibn meryem'", 3, 'say 5:110 4-6', "harekesiz 'yâ 'îse'bne meryem' (4-6. kelime; biçim öğesi 'yâ' — nida öneki harekesiz kalıpta; ◇ lemma dizisi 'dizi 5 110 4 6' sûre içi 6, harekesiz kalıp 3)", ('dizi 5 110 4 6', "'îsâ ibn meryem", '4-6', "biçim farkı (dizi 5 110 4 6)")),
 ("5:110", "'ellezî kefera min'", 2, 'say 5:110 56-58', "harekesiz 'llezîne keferû minhum' (56-58. kelime; biçim öğesi 'min' — zamir eki ve yazım farkı; ◇ lemma dizisi 'dizi 5 110 56 58' sûre içi 4, harekesiz kalıp 2)", ('dizi 5 110 56 58', "ellezî kefera min", '56-58', "biçim farkı (dizi 5 110 56 58): basılmamış eş zamir eki; 5:73 yazım eş; 5:78 zamir eki")),
]
'''
VF = '''VF_YAZI = {109: {5: "'fe-yeqûlu'"}, 110: {10: "'ve 'alâ'", 20: "'ve kehlen'", 21: "'ve iz'", 27: "'ve iz'", 34: "'fe-tenfuxu'", 36: "'fe-tekûnu'", 39: "'ve tubri'u'", 43: "'ve iz'", 47: "'ve iz'", 55: "'fe-qâle'"}}
sys.path.insert(0, '/home/claude/b33/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b33/yap/I_head.py', encoding='utf-8').read() + open('/home/claude/b33/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('ARIZA oluşturucu — bölüm 14-2', 'ARIZA oluşturucu — bölüm 15-1'), ('# blok 32 (5:106-108)', '# blok 33 (5:109-110)'), ('/b32/', '/b33/'), ("es_edat.py', '32'", "es_edat.py', '33'"), ('range(1, 33)', 'range(1, 34)'),
     ("'--plan', '32', '--numarasiz')", "'--plan', '33', '--numarasiz')"),
     ('ariza_5_106_108', 'ariza_5_109_110'), ('(106, 108)', '(109, 110)'), ("'106', '108', '32'", "'109', '110', '33'"), ("'106', '108'", "'109', '110'"),
     ("BEK = []", "BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b32.txt', encoding='utf-8').read() + ']')"),
     ("'30', '31', '32')", "'30', '31', '32', '33')"),
     ("BOL = \"'Soru sormama; bahîra ve sâibe; vasiyet ve şahitlik'\"", "BOL = \"'Elçilerin toplanması; İsâ'ya verilen nimetler; havariler ve sofra'\""),
     ("    B13 = run('/home/claude/sunum/bolum13_kurallar.py', '109', '110', '33').splitlines()\n", "    B13 = run('/home/claude/sunum/bolum13_kurallar.py', '109', '110', '33').splitlines()\n    B14 = run('/home/claude/sunum/bolum14_kurallar.py', '109', '110', '33').splitlines()\n"),
     ("'B13_HEPSI': (B13[-1] if B13 else '?'),", "'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'),"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_5_b31.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_5_b33.txt'"),
     ]
for a, b in R:
    assert a in out, a
    out = out.replace(a, b)
for l in out.split('\n'):
    for bad in ('b32', "'32'", "'106'", "'108'", '5_106_108'):
        if bad in l and 'nn in' not in l and 'bekleyen_ariza_5_b32' not in l: print('KONTROL', bad, l[:160])
open('/home/claude/b33/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)

src = open('/home/claude/b34/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("5:116", "'iz qâle allâh 'îsâ ibn meryem'", 2, 'say 5:116 1-6 --on', "harekesiz 've iz qâle'llâhu yâ 'îse'bne meryem' (1-6. kelime)", ('dizi 5 116 1 6', "iz qâle allâh 'îsâ ibn meryem", '1-6', "biçim farkı (dizi 5 116 1 6): 5:110 önek")),
 ("5:116", "'inne _ 'allâm ğuyûb'", 2, 'say 5:116 41-44', "harekesiz 'inneke ente 'allâmu'l-ğuyûb' (41-44. kelime)", None),
 ("5:116", "''îsâ ibn meryem'", 3, 'say 5:116 4-6', "harekesiz 'yâ 'îse'bne meryem' (4-6. kelime; biçim öğesi 'yâ' — nida öneki harekesiz kalıpta; ◇ lemma dizisi 'dizi 5 116 4 6' sûre içi 6, harekesiz kalıp 3)", None),
 ("5:116", "'en qâle mâ'", 2, 'say 5:116 21-23', "harekesiz 'en eqûle mâ' (21-23. kelime)", ('dizi 5 116 21 23', "en qâle mâ", '21-23', "biçim farkı (dizi 5 116 21 23): basılmamış eş fiil çekimi, zamir eki")),
 ("5:116", "'min dûn allâh'", 2, 'say 5:116 13-15', "harekesiz 'min dûni'llâh' (13-15. kelime)", None),
 ("5:116", "''alime mâ fî'", 2, 'say 5:116 32-34', "harekesiz 'ta'lemu mâ fî' (32-34. kelime)", ('dizi 5 116 32 34', "'alime mâ fî", '32-34', "biçim farkı (dizi 5 116 32 34): 5:97 fiil çekimi")),
 ("5:117", "''abede allâh rabb rabb'", 2, 'say 5:117 9-12', "harekesiz 'u'budû'llâhe rabbî ve rabbekum' (9-12. kelime)", None),
 ("5:117", "''alâ kull şey''", 5, 'say 5:117 26-28', "harekesiz ''alâ kulli şey'' (26-28. kelime)", None),
]
'''
VF = '''VF_YAZI = {116: {1: "'ve iz'", 11: "'ve ummiye'", 30: "'fe-qad'", 36: "'ve lâ'"}, 117: {12: "'ve rabbekum'", 13: "'ve kuntu'", 19: "'fe-lemmâ'", 25: "'ve ente'"}}
sys.path.insert(0, '/home/claude/b35/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b35/yap/I_head.py', encoding='utf-8').read() + open('/home/claude/b35/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('ARIZA oluşturucu — bölüm 15-2', 'ARIZA oluşturucu — bölüm 16-1'), ('# blok 34 (5:111-115)', '# blok 35 (5:116-117)'), ('/b34/', '/b35/'), ("es_edat.py', '34'", "es_edat.py', '35'"), ('range(1, 35)', 'range(1, 36)'),
     ("'--plan', '34', '--numarasiz')", "'--plan', '35', '--numarasiz')"),
     ('ariza_5_111_115', 'ariza_5_116_117'), ('(111, 115)', '(116, 117)'), ("'111', '115', '34'", "'116', '117', '35'"), ("'111', '115'", "'116', '117'"),
     ("BEK = []", "BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b34.txt', encoding='utf-8').read() + ']')"),
     ("'30', '31', '32', '33', '34')", "'30', '31', '32', '33', '34', '35')"),
     ("BOL = \"'Elçilerin toplanması; İsâ'ya verilen nimetler; havariler ve sofra'\"", "BOL = \"'İsâ'ya soru; doğruların fayda gördüğü gün'\""),
     ("    B14 = run('/home/claude/sunum/bolum14_kurallar.py', '116', '117', '35').splitlines()\n", "    B14 = run('/home/claude/sunum/bolum14_kurallar.py', '116', '117', '35').splitlines()\n    B15 = run('/home/claude/sunum/bolum15_kurallar.py', '116', '117', '35').splitlines()\n"),
     ("'B14_HEPSI': (B14[-1] if B14 else '?'),", "'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'),"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_5_b34.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_5_b35.txt'"),
     ]
for a, b in R:
    assert a in out, a
    out = out.replace(a, b)
for l in out.split('\n'):
    for bad in ('b34', "'34'", "'111'", "'115'", '5_111_115'):
        if bad in l and 'nn in' not in l and 'bekleyen_ariza_5_b34' not in l: print('KONTROL', bad, l[:160])
open('/home/claude/b35/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)

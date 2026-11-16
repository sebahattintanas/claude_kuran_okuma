src = open('/home/claude/b23/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_BAS = {l.strip()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("5:75", "'mesîh ibn meryem'", 3, 'say 5:75 2-4', "harekesiz 'l-mesîhu'bnu meryem' (2-4. kelime)", None),
 ("5:76", "'min dûn allâh'", 2, 'say 5:76 3-5', "harekesiz 'min dûni'llâh' (3-5. kelime)", None),
 ("5:77", "'qâle ehl kitâb'", 3, 'say 5:77 1-3', "harekesiz 'qul yâ ehle'l-kitâb' (1-3. kelime)", None),
 ("5:77", "'lâ ittebe'a ehvâ''", 2, 'say 5:77 10-12 --on', "önek kesilmiş 've lâ tettebi'û ehvâ'' (10-12. kelime; biçim öğesi 'tettebi'û' — ölçüm kalıbında 2MP yasak biçimi; ◇ lemma dizisi 'dizi 5 77 10 12' sûre içi 3, başka çekim eşleri dahil)", ('dizi 5 77 10 12', "lâ ittebe'a ehvâ'", '10-12', "biçim farkı (dizi 5 77 10 12): basılmamış eş fiil çekimi, zamir eki; basılmamış eş fiil çekimi, zamir eki; öneksiz eş koşusu (dizi 5 77 10 12): basılmamış eş → önek kesilmiş sûre içi 2; basılmamış eş → önek kesilmiş sûre içi 2 — tutuyor")),
 ("5:77", "''an sevâ' sebîl'", 2, 'say 5:77 21-23', "harekesiz ''an sevâ'i's-sebîl' (21-23. kelime)", None),
]
'''
VF = '''VF_YAZI = {75: {12: "'ve ummuhû'"}, 76: {11: "'ve lâ'", 13: "'ve'llâhu'"}, 77: {10: "'ve lâ'", 18: "'ve edallû'", 20: "'ve dallû'"}}
sys.path.insert(0, '/home/claude/b24/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b24/yap/I_parca.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('ARIZA oluşturucu — bölüm 10-2', 'ARIZA oluşturucu — bölüm 10-3'), ('# blok 23 (5:71-74)', '# blok 24 (5:75-77)'), ('/b23/', '/b24/'), ("es_edat.py', '23'", "es_edat.py', '24'"), ('range(1, 24)', 'range(1, 25)'), ("'--plan', '23'", "'--plan', '24'"),
     ('ariza_5_71_74', 'ariza_5_75_77'), ('(71, 74)', '(75, 77)'), ("'71', '74', '23'", "'75', '77', '24'"), ("'71', '74'", "'75', '77'")]
for a, b in R:
    assert a in out, a
    out = out.replace(a, b)
out = out.replace("'21', '22', '23')", "'21', '22', '23', '24')")
for l in out.split('\n'):
    for bad in ('b23', "'23'", "'71'", "'74'", '5_71_74'):
        if bad in l and 'nn in' not in l: print('KONTROL', bad, l[:200])
open('/home/claude/b24/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)

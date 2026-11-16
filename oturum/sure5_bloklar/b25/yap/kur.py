src = open('/home/claude/b24/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_BAS = {l.strip()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("5:78", "'ellezî kefera min'", 2, 'say 5:78 2-4', "harekesiz 'llezîne keferû min' (2-4. kelime; biçim öğesi 'min' — ölçüm kalıbında 'min' + ad bitişiği; ◇ lemma dizisi 'dizi 5 78 2 4' sûre içi 4, 'minhum' / 'min' + ad eşleri dahil)", None),
 ("5:78", "''îsâ ibn meryem'", 2, 'say 5:78 10-12 --on', "önek kesilmiş 've 'îsâ'bni meryem' (10-12. kelime; biçim öğesi — ölçüm kalıbı harekesiz elif yazımlı ad, öneksiz; ◇ lemma dizisi 'dizi 5 78 10 12' sûre içi 6, i'râb ve önek eşleri dahil)", ('dizi 5 78 10 12', "'îsâ ibn meryem", '10-12', "biçim farkı (dizi 5 78 10 12): basılmamış eş önek; basılmamış eş i'râb, önek; basılmamış eş i'râb, önek; basılmamış eş i'râb, önek; basılmamış eş i'râb, önek; öneksiz eş koşusu (dizi 5 78 10 12): basılmamış eş → önek kesilmiş sûre içi 1; basılmamış eş → önek kesilmiş sûre içi 3; basılmamış eş → önek kesilmiş sûre içi 3; basılmamış eş → önek kesilmiş sûre içi 6; basılmamış eş → önek kesilmiş sûre içi 3")),
 ("5:79", "'bi'se mâ kâne'", 3, 'say 5:79 7-9 --on', "önek kesilmiş 'le-bi'se mâ kânû' (7-9. kelime)", None),
 ("5:80", "'ra'â kesîr min'", 2, 'say 5:80 1-3 --on', "önek kesilmiş 'terâ kesîran minhum' (1-3. kelime)", None),
]
'''
VF = '''VF_YAZI = {78: {10: "'ve 'îsâ'bni'", 16: "'ve kânû'"}, 79: {}, 80: {16: "'ve fi'l-'azâbi'"}, 81: {1: "'ve lev'", 5: "'ve'n-nebiyyi'", 6: "'ve mâ'", 12: "'ve lâkinne'"}}
sys.path.insert(0, '/home/claude/b25/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b25/yap/I_parca.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('ARIZA oluşturucu — bölüm 10-3', 'ARIZA oluşturucu — bölüm 11-1'), ('# blok 24 (5:75-77)', '# blok 25 (5:78-81)'), ('/b24/', '/b25/'), ("es_edat.py', '24'", "es_edat.py', '25'"), ('range(1, 25)', 'range(1, 26)'),
     ("'--plan', '24')", "'--plan', '25', '--numarasiz')"), ("es_lemma.py', *BLOKLAR)", "es_lemma.py', *BLOKLAR, '--numarasiz')"),
     ('ariza_5_75_77', 'ariza_5_78_81'), ('(75, 77)', '(78, 81)'), ("'75', '77', '24'", "'78', '81', '25'"), ("'75', '77'", "'78', '81'"),
     ("BEK = []", "BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b24.txt', encoding='utf-8').read() + ']')"),
     ("geriye_donuk_5_b23.txt", "geriye_donuk_5_b25.txt"), ("'21', '22', '23', '24')", "'21', '22', '23', '24', '25')"),
     ("    B8 = run('/home/claude/sunum/bolum8_kurallar.py', '78', '81', '25').splitlines()", "    B8 = run('/home/claude/sunum/bolum8_kurallar.py', '78', '81', '25').splitlines()\n    B9 = run('/home/claude/sunum/bolum9_kurallar.py', '78', '81', '25').splitlines()\n    B10 = run('/home/claude/sunum/bolum10_kurallar.py', '78', '81', '25').splitlines()"),
     ("'B8_HEPSI': (B8[-1] if B8 else '?'),", "'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'),")]
for a, b in R:
    assert a in out, a
    out = out.replace(a, b)
for l in out.split('\n'):
    for bad in ('b24', "'24'", "'75'", "'77'", '5_75_77'):
        if bad in l and 'nn in' not in l: print('KONTROL', bad, l[:200])
open('/home/claude/b25/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)

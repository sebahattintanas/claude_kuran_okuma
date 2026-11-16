import re
src = open('/home/claude/b19/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("5:59", "'qâle ehl kitâb'", 3, 'say 5:59 1-3', "harekesiz 'qul yâ ehle'l-kitâb' (1-3. kelime)", None),
 ("5:62", "'ekl suht bi'se mâ kâne'", 2, 'say 5:62 8-12 --on', "önek kesilmiş 've eklihimu's-suhta le-bi'se mâ kânû' (8-12. kelime)", None),
 ("5:62", "'bi'se mâ kâne'", 3, 'say 5:62 10-12 --on', "önek kesilmiş 'le-bi'se mâ kânû' (10-12. kelime)", None),
 ("5:63", "'ekl suht bi'se mâ kâne'", 2, 'say 5:63 8-12 --on', "önek kesilmiş 've eklihimu's-suhta le-bi'se mâ kânû' (8-12. kelime)", None),
 ("5:63", "'bi'se mâ kâne'", 3, 'say 5:63 10-12 --on', "önek kesilmiş 'le-bi'se mâ kânû' (10-12. kelime)", None),
]
'''
VF = '''VF_YAZI = {59: {11: "'ve mâ'", 14: "'ve mâ'", 18: "'ve enne'"}, 60: {13: "'ve ğadibe'", 15: "'ve ce'ale'", 18: "'ve'l-xanâzîra'", 19: "'ve 'abede'", 24: "'ve edallu'"}, 61: {1: "'ve izâ'", 5: "'ve qad'", 8: "'ve hum'", 12: "'ve'llâhu'"}, 62: {1: "'ve terâ'", 7: "'ve'l-'udvâni'", 8: "'ve eklihimu'"}, 63: {4: "'ve'l-ahbâru'", 8: "'ve eklihimu'"}}
sys.path.insert(0, '/home/claude/b20/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b20/yap/I_parca.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('blok 19 (5:55-58)', 'blok 20 (5:59-63)'), ('bölüm 7-3', 'bölüm 9-1'), ('/b19/', '/b20/'),
     ("es_edat.py', '19'", "es_edat.py', '20'"), ('range(1, 20)', 'range(1, 21)'), ("'--plan', '19'", "'--plan', '20'"), ("'55', '58', EMS", "'59', '63', EMS"),
     ("gloss_tara.py', '55', '58', '19'", "gloss_tara.py', '59', '63', '20'"), ('ariza_5_55_58', 'ariza_5_59_63'), ('(55, 58)', '(59, 63)'),
     ("'55', '58', '19'", "'59', '63', '20'"), ("'55', '58')", "'59', '63')"),
     ("BOL = \"'Velî edinme; Allah'ın sevdiği kavim; dinle alay edenler'\"", "BOL = \"'Kitap ehlinin tutumu; bağlı el sözü; Tevrat ve İncil'i ayakta tutma'\""),
     ("geriye_donuk_5_b17.txt", "geriye_donuk_5_b19.txt"),
     ("BEK = []", "BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b19.txt', encoding='utf-8').read() + ']')"),
     ("    B7 = run('/home/claude/sunum/bolum7_kurallar.py', '59', '63', '20').splitlines()\n",
      "    B7 = run('/home/claude/sunum/bolum7_kurallar.py', '59', '63', '20').splitlines()\n    B8 = run('/home/claude/sunum/bolum8_kurallar.py', '59', '63', '20').splitlines()\n"),
     ("'B7_HEPSI': (B7[-1] if B7 else '?'),", "'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'),"),
     ("print(B6)", "print(B6); print(B7); print(B8)")]
for a, b in R:
    assert a in out, a
    out = out.replace(a, b)
out = re.sub(r"for nn in \([^)]*\)", "for nn in ('06', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20')", out)
for l in out.split('\n'):
    for bad in ('b19', "'19'", '55', '58'):
        if bad in l and 'nn in' not in l and '5:55' not in l and '5:58' not in l and 'geriye_donuk' not in l and 'bekleyen' not in l: print('KONTROL', bad, l[:140])
open('/home/claude/b20/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)

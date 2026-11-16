import re
src = open('/home/claude/b17/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('I = list(BEK) + ['); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("5:51", "'eyy ellezî âmene'", 16, 'say 5:51 1-3', "harekesiz 'yâ eyyuhe'llezîne âmenû' (1-3. kelime)", None),
 ("5:51", "'eyy ellezî âmene lâ'", 6, 'say 5:51 1-4', "harekesiz 'yâ eyyuhe'llezîne âmenû lâ' (1-4. kelime)", None),
 ("5:51", "'eyy ellezî âmene lâ ittexaze'", 2, 'say 5:51 1-5', "harekesiz 'yâ eyyuhe'llezîne âmenû lâ tettexizu' (1-5. kelime)", None),
 ("5:51", "'inne allâh lâ hedâ qavm'", 2, 'say 5:51 17-21', "harekesiz 'inne'llâhe lâ yehdi'l-qavm' (17-21. kelime)", None),
 ("5:51", "'allâh lâ hedâ qavm'", 3, 'say 5:51 18-21 --on', "önek kesilmiş 'llâhe lâ yehdi'l-qavm' (18-21. kelime)", None),
 ("5:51", "'inne allâh lâ'", 3, 'say 5:51 17-19', "harekesiz 'inne'llâhe lâ' (17-19. kelime)", None),
 ("5:54", "'eyy ellezî âmene'", 16, 'say 5:54 1-3', "harekesiz 'yâ eyyuhe'llezîne âmenû' (1-3. kelime)", None),
]
'''
VF = '''VF_YAZI = {51: {7: "'ve'n-nasârâ'", 12: "'ve men'", 15: "'fe-innehû'"}, 52: {1: "'fe-tera'", 13: "'fe-'asa'", 22: "'fe-yusbihû'"}, 53: {1: "'ve yeqûlu'", 14: "'fe-asbahû'"}, 54: {9: "'fe-sevfe'", 14: "'ve yuhibbûnehû'", 25: "'ve lâ'", 35: "'ve'llâhu'"}}
sys.path.insert(0, '/home/claude/b18/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b18/yap/I_parca.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('blok 17 (5:48-50)', 'blok 18 (5:51-54)'), ('/b17/', '/b18/'), ("BOL = \"'Küfürde yarışanlar; Tevrat, İncil ve Kitap ile hüküm'\"", "BOL = \"'Velî edinme; Allah'ın sevdiği kavim; dinle alay edenler'\""),
     ("es_edat.py', '17'", "es_edat.py', '18'"), ('range(1, 18)', 'range(1, 19)'), ("'--plan', '17'", "'--plan', '18'"), ("'48', '50', EMS", "'51', '54', EMS"),
     ("gloss_tara.py', '48', '50', '17'", "gloss_tara.py', '51', '54', '18'"), ('(48, 50)', '(51, 54)'), ('ariza_5_48_50', 'ariza_5_51_54'),
     ("'48', '50', '17'", "'51', '54', '18'"), ("'48', '50')", "'51', '54')"), ('geriye_donuk_5_b13.txt', 'geriye_donuk_5_b17.txt'),
     ("BEK = []", "BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b17.txt', encoding='utf-8').read() + ']')")]
for a, b in R:
    assert a in out, a
    out = out.replace(a, b)
out = re.sub(r"for nn in \([^)]*\)", "for nn in ('06', '10', '11', '12', '13', '14', '15', '16', '17', '18')", out)
# bölüm 7 aracı ve D3 dışı / anılış yer tutucuları
out = out.replace("    B6 = run('/home/claude/sunum/bolum6_kurallar.py', '51', '54', '18', '--tazelik-yok').splitlines()",
                  "    B6 = run('/home/claude/sunum/bolum6_kurallar.py', '51', '54', '18', '--tazelik-yok').splitlines()\n    B7 = run('/home/claude/sunum/bolum7_kurallar.py', '51', '54', '18').splitlines()")
out = out.replace("'B6_HEPSI': (B6[-1] if B6 else '?'),", "'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,")
assert "'B7_HEPSI'" in out and "B7 = run" in out
for l in out.split('\n'):
    for bad in ('b17', '48', '50'):
        if bad in l and 'nn in' not in l and 'geriye_donuk_5_b17' not in l and 'bekleyen_ariza_5_b17' not in l and '5:48' not in l and '5:50' not in l: print('KONTROL', bad, l[:140])
open('/home/claude/b18/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)

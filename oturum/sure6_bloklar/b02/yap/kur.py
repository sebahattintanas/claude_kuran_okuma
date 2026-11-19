# sûre 6 blok 1 ARIZA oluşturucusu — sûre 5 blok 36 üreticisinden; denetim betikleri paralel (kullanıcı uyarısı: ilerleme ağır)
import re
src = open('/home/claude/s5/b36/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("6:6", "'min qabl min'", 2, 'say 6:6 5-7', "harekesiz 'min qablihim min' (5-7. kelime)", ('dizi 6 6 5 7', "min qabl min", '5-7', "biçim farkı (dizi 6 6 5 7): basılmamış eş zamir eki, önek")),
 ("6:7", "'qâle ellezî kefera in zâ illâ'", 2, 'say 6:7 9-14', "harekesiz 'le-qâle'llezîne keferû in hâzâ illâ' (9-14. kelime)", ('dizi 6 7 9 14', "qâle ellezî kefera in zâ illâ", '9-14', "biçim farkı (dizi 6 7 9 14): basılmamış eş önek")),
 ("6:10", "'mâ kâne _ istuhzi'e'", 2, 'say 6:10 10-13', "harekesiz 'mâ kânû bihî yestehzi'ûn' (10-13. kelime)", None),
 ("6:10", "'resûl min qabl'", 2, 'say 6:10 3-5', "harekesiz 'bi-rusulin min qablik' (3-5. kelime)", ('dizi 6 10 3 5', "resûl min qabl", '3-5', "biçim farkı (dizi 6 10 3 5): basılmamış eş i'râb, önek")),
]
'''
VF = '''VF_YAZI = {6: {16: "'ve erselne'", 20: "'ve ce'alne'", 25: "'fe-ehleknâhum'", 27: "'ve enşe'nâ'"}, 7: {1: "'ve lev'", 7: "'fe-lemesûhu'"}, 8: {1: "'ve qâlû'", 6: "'ve lev'"}, 9: {1: "'ve lev'", 6: "'ve le-lebesnâ'"}, 10: {1: "'ve le-qadi'", 6: "'fe-hâqa'"}, 11: {}}
sys.path.insert(0, '/home/claude/b02/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b02/yap/I_head.py', encoding='utf-8').read() + open('/home/claude/b02/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
# paralel denetim koşusu
a = out.index("    AYN = (run('/home/claude/sunum/ayn_kontrol.py'"); b = out.index("    REP = {")
PAR = '''    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '6', '11'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '6', '11', '02'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '6', '11', '02'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '6', '11', '02', '--tazelik-yok')}
    for _n in range(7, 17): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '6', '11', '02')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16 = [_R['B%d' % _n].splitlines() for _n in range(6, 17)]
'''
out = out[:a] + PAR + out[b:]
R = [('# blok 36 (5:118-120) ARIZA oluşturucu — bölüm 16-2', '# sûre 6 blok 2 (6:6-11) ARIZA oluşturucu — bölüm 1-2'), ('/b36/', '/b02/'),
     ("es_edat.py', '36'", "es_edat.py', '02'"), ('range(1, 37)', 'range(1, 3)'),
     ("'--plan', '36', '--numarasiz')", "'--plan', '2', '--numarasiz')"),
     ('ariza_5_118_120', 'ariza_6_6_11'), ('bag_5_118_120', 'bag_6_6_11'), ('(118, 120)', '(6, 11)'), ("'118', '120', '36'", "'6', '11', '02'"), ("'118', '120'", "'6', '11'"),
     ("_ON = {'5:118', '5:119', '5:120'}", "_ON = {'6:6', '6:7', '6:8', '6:9', '6:10', '6:11'}"), ('range(118, 121)', 'range(6, 12)'),
     ("x.startswith('5:')", "x.startswith('6:')"), ("== '5:%d' % a_", "== '6:%d' % a_"), ("return '5:%d: %s'", "return '6:%d: %s'"), ("r'\\b5:%d:\\d+'", "r'\\b6:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_5_*.txt')", "glob.glob('/home/claude/yamalar/ariza_6_*.txt')"),
     ("BEK = []", "BEK = []"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_5_b36.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_5_hazirlik6.txt'"),
     ("BOL = \"'İsâ'ya soru; doğruların fayda gördüğü gün'\"", "BOL = \"'Gökleri ve yeri yaratan; yüz çeviren kavimler'\""),
     ("'B15_HEPSI': (B15[-1] if B15 else '?'),", "'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'),"),
     ("sûre 5'in okunmuş bütün ARIZA dosyaları", "sûre 6'nın okunmuş bütün ARIZA dosyaları"),
     ("print(GLS); print(KUR); print(B5); print(B6); print(B7); print(B8)", "print(GLS)\nfor _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16): print([l for l in _x if l.startswith('HATA') or 'hata' in l])"),
     ]
R += [("MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()", "MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']")]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
out = re.sub(r"VF_YAZI_ESKI = \{.*\n", "VF_YAZI_ESKI = {}\n", out)
out = re.sub(r"for nn in \('06', [^)]*\):", "for nn in ('01', '02'):", out)
for l in out.split('\n'):
    for bad in ('b36', "'36'", "'118'", "'120'", '5_118_120', "'5:"):
        if bad in l: print('KONTROL', bad, l[:160])
open('/home/claude/b02/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)

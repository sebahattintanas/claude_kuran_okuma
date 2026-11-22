# sûre 6 blok 1 ARIZA oluşturucusu — sûre 5 blok 36 üreticisinden; denetim betikleri paralel (kullanıcı uyarısı: ilerleme ağır)
import re
src = open('/home/claude/s5/b36/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("6:118", "'ekele mimmâ zekere ism allâh 'alâ'", 2, 'say 6:118 1-6', "harekesiz 'fe-kulû mimmâ zukira'smu'llâhi 'aleyhi' (1-6. kelime)", ('dizi 6 118 1 6', "ekele mimmâ zekere ism allâh 'alâ", '1-6', 'biçim farkı (dizi 6 118 1 6): 6:119 önek')),
 ("6:118", "'zekere ism allâh 'alâ'", 3, 'say 6:118 3-6', "harekesiz 'zukira'smu'llâhi 'aleyhi' (3-6. kelime); biçim öğesi ''alâ' zamir eki (lemma dizisi sûre içi 4, nakarat3 3)", ('dizi 6 118 3 6', "zekere ism allâh 'alâ", '3-6', 'biçim farkı (dizi 6 118 3 6): 6:119 yazım eş; 6:121 yazım eş; basılmamış eş elif yazımı, fiil çekimi, zamir eki; öneksiz eş koşusu (dizi 6 118 3 6): 6:119 → önek kesilmiş sûre içi 3; 6:121 → önek kesilmiş sûre içi 1; basılmamış eş → önek kesilmiş sûre içi 1')),
 ("6:118", "'zekere ism allâh'", 4, 'say 6:118 3-5', "harekesiz 'zukira'smu'llâh' (3-5. kelime)", ('dizi 6 118 3 5', "zekere ism allâh", '3-5', 'biçim farkı (dizi 6 118 3 5): 6:119 yazım eş; 6:121 yazım eş; basılmamış eş fiil çekimi, zamir eki')),
 ("6:119", "'ekele mimmâ zekere ism allâh 'alâ'", 2, 'say 6:119 4-9', "harekesiz 'te'kulû mimmâ zukira'smu'llâhi 'aleyhi' (4-9. kelime)", ('dizi 6 119 4 9', "ekele mimmâ zekere ism allâh 'alâ", '4-9', 'biçim farkı (dizi 6 119 4 9): 6:118 önek')),
 ("6:119", "'zekere ism allâh 'alâ'", 3, 'say 6:119 6-9', "harekesiz 'zukira'smu'llâhi 'aleyhi' (6-9. kelime); biçim öğesi ''alâ' zamir eki (lemma dizisi sûre içi 4, nakarat3 3)", ('dizi 6 119 6 9', "zekere ism allâh 'alâ", '6-9', 'biçim farkı (dizi 6 119 6 9): 6:118 yazım eş; 6:121 yazım eş; basılmamış eş elif yazımı, fiil çekimi, zamir eki; öneksiz eş koşusu (dizi 6 119 6 9): 6:118 → önek kesilmiş sûre içi 3; 6:121 → önek kesilmiş sûre içi 1; basılmamış eş → önek kesilmiş sûre içi 1')),
 ("6:119", "'inne rabb _ a'lem'", 2, 'say 6:119 26-29', "harekesiz 'inne rabbeke huve a'lemu' (26-29. kelime)", None),
 ("6:119", "'zekere ism allâh'", 4, 'say 6:119 6-8', "harekesiz 'zukira'smu'llâh' (6-8. kelime)", ('dizi 6 119 6 8', "zekere ism allâh", '6-8', 'biçim farkı (dizi 6 119 6 8): 6:118 yazım eş; 6:121 yazım eş; basılmamış eş fiil çekimi, zamir eki')),
 ("6:119", "'ğayr 'ilm inne'", 2, 'say 6:119 24-26', "harekesiz 'bi-ğayri 'ilmin inne' (24-26. kelime)", None),
 ("6:120", "'cezâ bi-mâ kâne'", 2, 'say 6:120 9-11', "harekesiz 'se-yuczevne bi-mâ kânû' (9-11. kelime)", ('dizi 6 120 9 11', 'cezâ mâ kâne', '9-11', 'biçim farkı (dizi 6 120 9 11): basılmamış eş fiil çekimi')),
 ("6:121", "'zekere ism allâh 'alâ'", 3, 'say 6:121 5-8', "harekesiz 'yuzkeri'smu'llâhi 'aleyhi' (5-8. kelime); biçim öğesi ''alâ' zamir eki (lemma dizisi sûre içi 4, nakarat3 3)", ('dizi 6 121 5 8', "zekere ism allâh 'alâ", '5-8', 'biçim farkı (dizi 6 121 5 8): 6:118 yazım eş; 6:119 yazım eş; basılmamış eş elif yazımı, fiil çekimi, zamir eki; öneksiz eş koşusu (dizi 6 121 5 8): 6:118 → önek kesilmiş sûre içi 3; 6:119 → önek kesilmiş sûre içi 3; basılmamış eş → önek kesilmiş sûre içi 1')),
 ("6:121", "'zekere ism allâh'", 4, 'say 6:121 5-7', "harekesiz 'yuzkeri'smu'llâh' (5-7. kelime)", ('dizi 6 121 5 7', "zekere ism allâh", '5-7', 'biçim farkı (dizi 6 121 5 7): 6:118 yazım eş; 6:119 yazım eş; basılmamış eş fiil çekimi, zamir eki')),
]
'''

VF = '''VF_YAZI = {119: {1: "'ve mâ'", 10: "'ve qad'", 20: "'ve inne'"}, 120: {1: "'ve zerû'", 4: "'ve bâtinahû'"}, 121: {1: "'ve lâ'", 9: "'ve innehû'", 11: "'ve inne'", 17: "'ve in'"}}
sys.path.insert(0, '/home/claude/b28/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b28/yap/I_head.py', encoding='utf-8').read() + open('/home/claude/b28/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
# paralel denetim koşusu
a = out.index("    AYN = (run('/home/claude/sunum/ayn_kontrol.py'"); b = out.index("    REP = {")
PAR = '''    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '118', '121'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '118', '121', '28'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '118', '121', '28'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '118', '121', '28', '--tazelik-yok')}
    for _n in range(7, 30): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '118', '121', '28')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29 = [_R['B%d' % _n].splitlines() for _n in range(6, 30)]
'''
out = out[:a] + PAR + out[b:]
R = [("K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k}", "K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k and not (k + ' --medde' in sayim.S2 and sayim.S2[k + ' --medde'][0] != n)}  # sûre 6 bölüm 5 denetimi kuralı 6 (TEKIL_MEDDE)"),
     ('# blok 36 (5:118-120) ARIZA oluşturucu — bölüm 16-2', '# sûre 6 blok 28 (6:118-121) ARIZA oluşturucu — bölüm 14-2'), ('/b36/', '/b28/'),
     ("es_edat.py', '36'", "es_edat.py', '28'"), ('range(1, 37)', 'range(1, 29)'),
     ("'--plan', '36', '--numarasiz')", "'--plan', '28', '--numarasiz')"),
     ('ariza_5_118_120', 'ariza_6_118_121'), ('bag_5_118_120', 'bag_6_118_121'), ('(118, 120)', '(118, 121)'), ("'118', '120', '36'", "'118', '121', '28'"), ("'118', '120'", "'118', '121'"),
     ("_ON = {'5:118', '5:119', '5:120'}", "_ON = {'6:118', '6:119', '6:120', '6:121'}"), ('range(118, 121)', 'range(118, 122)'),
     ("x.startswith('5:')", "x.startswith('6:')"), ("== '5:%d' % a_", "== '6:%d' % a_"), ("return '5:%d: %s'", "return '6:%d: %s'"), ("r'\\b5:%d:\\d+'", "r'\\b6:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_5_*.txt')", "glob.glob('/home/claude/yamalar/ariza_6_*.txt')"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_5_b36.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_6_b26k.txt'"),
     ("BOL = \"'İsâ'ya soru; doğruların fayda gördüğü gün'\"", "BOL = \"'Hakem olarak Allah; üzerine Allah'ın adı anılan'\""),
     ("'B15_HEPSI': (B15[-1] if B15 else '?'),", "'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'),"),
     ("sûre 5'in okunmuş bütün ARIZA dosyaları", "sûre 6'nın okunmuş bütün ARIZA dosyaları"),
     ("print(GLS); print(KUR); print(B5); print(B6); print(B7); print(B8)", "print(GLS)\nfor _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29): print([l for l in _x if l.startswith('HATA') or 'hata' in l])"),
     ]
R += [("MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()", "MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']")]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
out = re.sub(r"VF_YAZI_ESKI = \{.*\n", "VF_YAZI_ESKI = {}\n", out)
out = re.sub(r"for nn in \('06', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28'):", out)
for l in out.split('\n'):
    for bad in ('b36', "'36'", "'118'", "'120'", '5_118_120', "'5:"):
        if bad in l: print('KONTROL', bad, l[:160])
_mk = """MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)"""
assert _mk in out
out = out.replace(_mk, _mk + "\nMKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde")
open('/home/claude/b28/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)

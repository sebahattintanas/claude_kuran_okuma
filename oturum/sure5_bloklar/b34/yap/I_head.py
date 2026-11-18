_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_111_115.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'5:111', '5:112', '5:113', '5:114', '5:115'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_111_115.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '5:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '5:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(111, 116))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "5:111 'iz' (1. kelime — morph T, zaman); 5:112 'iz' (1. kelime — morph T, zaman); 5:114 kök أخر ('âxirinâ' 16. kelime — sonraki): tetik listesinde yok; 5:115 kök بعد ('ba'du' 8. kelime — morph T, sonra): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
# blok 34 commit'inden sonraki esmâ düzeltmesi yeniden koşusu: araç farkı blok 33 commit'ine (2f1e117) göre — arac_degisim'in ilk koşu çıktısı
ARAC = 'değişen araçlar (repo HEAD ile fark): sunum/bolum13_kurallar.py, sunum/bolum5_kurallar.py, sunum/kelime_kontrol.py, sunum/mutasyon_sina.py, sunum/yasakli.sh; sunum/sinifla.py (SON 115); sunum/basilan.txt +7'
EMH = run('/home/claude/sunum/esma_muhur.py', '111', '115', '34')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b34/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 35)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b5:%d:\d+' % a_, s_) for a_ in range(111, 116))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)

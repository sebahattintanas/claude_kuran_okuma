_BAS = {l.strip() for l in open('/home/claude/sunum/basilan.txt', encoding='utf-8') if l.strip()}
def _numarasiz(m):
    refs = [x.strip() for x in m.group(1).split(',')]
    kal = [x for x in refs if ':'.join(x.split(':')[:2]) in _BAS]
    n = len(refs) - len(kal)
    return '(' + ', '.join(kal + (['okunmuş %d konum' % n] if n else [])) + ')'
ESL = re.sub(r'\((\d+:\d+:\d+(?:, \d+:\d+:\d+)*)\)', _numarasiz, ESL)
_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_71_74.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'5:71', '5:72', '5:73', '5:74'}
D3DISI = ', '.join(sorted(_U - _BAG - _ON, key=lambda x: tuple(map(int, x.split(':')))))
ANILIS = "5:71 kök عمي (''amû' 5. ve 12. kelime — körlük) ve kök صمم ('sammû' 6. ve 13. kelime — sağırlık): duyu kaybı, tetik listesinde yok; 5:72 kök نور ('n-nâru' 29. kelime — ateş) ve kök جنن ('l-cennete' 27. kelime — cennet): K listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '71', '74', '23')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b23/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 24)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b5:%d:\d+' % a_, s_) for a_ in range(71, 75))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)

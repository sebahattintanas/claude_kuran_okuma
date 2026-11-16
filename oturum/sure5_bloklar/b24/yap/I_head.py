_BAS = {l.strip() for l in open('/home/claude/sunum/basilan.txt', encoding='utf-8') if l.strip()}
def _numarasiz(m):
    refs = [x.strip() for x in m.group(1).split(',')]
    kal = [x for x in refs if ':'.join(x.split(':')[:2]) in _BAS]
    n = len(refs) - len(kal)
    return '(' + ', '.join(kal + (['okunmuş %d konum' % n] if n else [])) + ')'
def _son(e):
    m = re.match(r'(b\d+) (say|dizi|lem) (\S+)( \S+)?( \S+)?( \S+)? (\[.*\])$', e.strip())
    if not m: return e
    p = [x.strip() for x in m.groups()[2:6] if x]
    ay = p[0].split(':')[0] + ':' + p[0].split(':')[1] if ':' in p[0] else p[0] + ':' + p[1]
    return e if ay in _BAS else '%s %s numarasız %s' % (m.group(1), m.group(2), m.group(7))
SON = '; '.join(_son(e) for e in SON.split('; '))
ESL = re.sub(r'\((\d+:\d+:\d+(?:, \d+:\d+:\d+)*)\)', _numarasiz, ESL)
_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_75_77.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'5:75', '5:76', '5:77'}
D3DISI = ', '.join(sorted(_U - _BAG - _ON, key=lambda x: tuple(map(int, x.split(':')))))
ANILIS = "5:75 kök أكل ('ye'kulâni' 15. kelime — yeme) ve kök طعم ('t-ta'âma' 16. kelime — yemek): beslenme, tetik listesinde yok; 5:75 kök نظر ('nzur' 17. ve 23. kelime — bakma): emir, duyu tetik listesinde yok; 5:76 kök ضرر / نفع ('darran' 10., 'nef'an' 12. kelime): tetik listesinde yok; 5:75 kök خلو (\'xalet\' 8. kelime — gelip geçme) ve kök قبل (\'qablihi\' 10. kelime; 5:77 \'qablu\' 17. kelime — önce): zaman, tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '75', '77', '24')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b24/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 25)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b5:%d:\d+' % a_, s_) for a_ in range(75, 78))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)

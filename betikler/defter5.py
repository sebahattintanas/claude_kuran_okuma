# -*- coding: utf-8 -*-
"""defter v5 — 'fig' alanı regex yerine morfoloji etiketleriyle yeniden kuruldu.

ESKİ (regex, hatalı):
  MAILLA / LAILLA  — 'ما … إلا' ve 'لا … إلا' kalıplarını regex'le arıyordu.
                      HASR (إنما/ما…إلا) ile İSTİSNÂ (…إلا X) ayrımını yapamıyordu.
  QASEM            — kök 'قسم' veya ayet başı 'وَٱل' kaba tahmini.
  SUAL             — yalnız 'وما أدراك' kalıbı.

YENİ (etiket tabanlı):
  HASR     RES etiketi  — olumsuzluk + إلا, "ancak/sadece"      (2:9)
  ISTISNA  EXP etiketi  — kümeden çıkarma, "…hariç"             (2:34)
  QASEM    'P|PREF|LEM:و' + ardından GEN isim  = vâv-ı kasem; artı قسم/حلف kökü
  MM       V + aynı kökten VN (mef'ûl-i mutlak), bitişik
  AMMA     أمّا taksimi (أ/إ korunarak; إمّا dışarıda)
  KELLA    كلا
  NEHY     PRO etiketi (nehiy lâ'sı)
  IDRAB    RET etiketi (بل)
  DIKKAT   ATT etiketi (ألا / ها)
"""
import json, re, unicodedata
from collections import defaultdict, Counter

tok = defaultdict(list)
for ln in open('morph.txt', encoding='utf-8'):
    p = ln.rstrip('\n').split('\t')
    if len(p) < 4: continue
    loc = p[0].split(':')
    if len(loc) == 5: loc = loc[1:]
    if len(loc) != 4: continue
    tok[(int(loc[0]), int(loc[1]))].append(
        {'w': int(loc[2]), 'g': int(loc[3]), 'ar': p[1], 'pos': p[2], 'f': p[3]})

def sadk(w):
    w = unicodedata.normalize('NFC', w)
    w = re.sub(r'[\u064B-\u0652\u0670\u06DD\u06D6-\u06ED\u0640]', '', w)
    return w.replace('ٱ', 'ا').replace('آ', 'ا')     # أ / إ KORUNUR
AMMA = {'أما', 'فأما', 'وأما'}

D = json.load(open('defter.json'))
for r in D:
    k = (r['k'][0], r['k'][1])
    S = tok.get(k, [])
    fig = []
    P = [s['f'].split('|') for s in S]
    if any('RES' in x for x in P): fig.append('HASR')
    if any('EXP' in x for x in P): fig.append('ISTISNA')
    if any('PRO' in x for x in P): fig.append('NEHY')
    if any('RET' in x for x in P): fig.append('IDRAB')
    if any('ATT' in x for x in P): fig.append('DIKKAT')
    # vâv-ı kasem: bare P + PREF + LEM:و, sonraki segment DET/isim ve GEN
    for i, s in enumerate(S):
        p = s['f'].split('|')
        if s['pos'] == 'P' and 'PREF' in p and 'LEM:و' in p and p[0] == 'P':
            for t in S[i+1:i+4]:
                if 'GEN' in t['f'].split('|'): fig.append('QASEM'); break
            break
    if any(re.search(r'ROOT:(قسم|حلف)', s['f']) for s in S):
        if 'QASEM' not in fig: fig.append('QASEM')
    # mef'ûl-i mutlak: fiil + aynı kökten masdar (VN)
    for i in range(len(S)-1):
        a, b = S[i], S[i+1]
        ra = re.search(r'ROOT:([^|]+)', a['f']); rb = re.search(r'ROOT:([^|]+)', b['f'])
        if ra and rb and ra.group(1) == rb.group(1) and a['pos'] == 'V' and 'VN' in b['f'].split('|'):
            fig.append('MM'); break
    kel = [s for s in S if s['g'] == 1]
    if any(sadk(s['ar']) in AMMA for s in S): fig.append('AMMA')
    if any(sadk(s['ar']).startswith('كلا') and len(sadk(s['ar'])) <= 4 for s in S): fig.append('KELLA')
    r['fig'] = fig

json.dump(D, open('defter.json', 'w', encoding='utf-8'), ensure_ascii=False)
c = Counter()
for r in D:
    for f in r['fig']: c[f] += 1
print('yeni fig dağılımı (ayet sayısı):', dict(c.most_common()))
print()
print('ESKİ -> YENİ karşılaştırma:')
print('  MAILLA 201 + LAILLA 122  ->  HASR %d + ISTISNA %d' % (c['HASR'], c['ISTISNA']))
print('  QASEM 231 (kaba)         ->  QASEM %d' % c['QASEM'])
print('  MM 175 (V+N)             ->  MM %d (V+VN)' % c['MM'])

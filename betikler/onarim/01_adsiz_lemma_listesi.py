# -*- coding: utf-8 -*-
"""ONARIM 1a — adsız aktör lemma listesini KORPUSTAN üret.

Proje kuralı: lemma/kök anahtarları elle yazılmaz, korpustan kopyalanır.
aktor2.py'deki ADSIZ_KOK sözlüğü bu kurala uymuyordu: altı anahtarın biri
('karye') YANLIŞ YAZILMIŞ ve korpusta hiç eşleşmiyor (57 token ölü).

Bu betik kökleri ÇAPA KONUMLARDAN (sûre:ayet:kelime) türetir; hiçbir Arapça
dizge elle yazılmaz. Çıktı: adsiz_lemma_listesi.json (deterministik sıralı).
"""
import re, json
from collections import defaultdict, Counter

# çapa konumlar: okumada görülen, kökü istenen tokenler (yalnız SAYI)
CAPA = {
    'racül':  (4, 34, 1),     # "erkekler kadınlar üzerine kâim"
    'imrae':  (27, 23, 3),    # "onlara hükmeden bir kadın"
    'nefer':  (46, 29, 4),    # "cinlerden bir grup"
    'ferîk':  (2, 75, 7),     # "onlardan bir grup"
    'tâife':  (3, 69, 2),     # "kitap ehlinden bir grup"
    'karye':  (27, 56, 12),   # "şehrinizden çıkarın"
}

TOK = defaultdict(dict)
for ln in open('morph.txt', encoding='utf-8'):
    p = ln.rstrip('\n').split('\t')
    if len(p) < 4: continue
    loc = p[0].split(':')
    if len(loc) == 5: loc = loc[1:]
    if len(loc) != 4: continue
    s, a, w = int(loc[0]), int(loc[1]), int(loc[2])
    TOK[(s, a)].setdefault(w, []).append(p)

def kok_of(s, a, w):
    for p in TOK[(s, a)].get(w, []):
        m = re.search(r'ROOT:([^|]+)', p[3])
        if m: return m.group(1)
    return None

KOK = {}
for et, (s, a, w) in CAPA.items():
    k = kok_of(s, a, w)
    assert k, 'çapa bulunamadı: %s %s' % (et, (s, a, w))
    KOK[et] = k

# her kök için lemma envanteri (yalnız isim POS)
inv = defaultdict(Counter)
feat = defaultdict(set)
for ln in open('morph.txt', encoding='utf-8'):
    p = ln.rstrip('\n').split('\t')
    if len(p) < 4: continue
    m = re.search(r'ROOT:([^|]+)', p[3])
    if not m: continue
    kk = m.group(1)
    if kk not in KOK.values(): continue
    lm = re.search(r'LEM:([^|]+)', p[3])
    if not lm: continue
    inv[kk][(lm.group(1), p[2])] += 1
    for f in p[3].split('|'):
        if f in ('M', 'F', 'MS', 'FS', 'MP', 'FP', 'MD', 'FD'): feat[(kk, lm.group(1))].add(f)

OUT = []
for et in sorted(KOK):
    kk = KOK[et]
    for (lm, pos), n in sorted(inv[kk].items(), key=lambda x: (-x[1], x[0][0])):
        OUT.append({'i': len(OUT), 'capa_etiket': et, 'kok': kk, 'lemma': lm,
                    'pos': pos, 'n': n, 'cins': sorted(feat[(kk, lm)])})

json.dump(OUT, open('adsiz_lemma_listesi.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('çapadan türetilen kökler:')
for et in sorted(KOK):
    print('  %-8s -> %s  (lemma sayısı %d)' % (et, KOK[et], len(inv[KOK[et]])))
print('\nadsiz_lemma_listesi.json: %d kayıt' % len(OUT))
print('\nindeks  etiket    pos   n     cins')
for r in OUT:
    print('  %3d   %-8s  %-4s  %-4d  %s' % (r['i'], r['capa_etiket'], r['pos'], r['n'], ','.join(r['cins'])))

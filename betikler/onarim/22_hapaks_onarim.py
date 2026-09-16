# -*- coding: utf-8 -*-
"""22_hapaks_onarim.py — ONARIM 14 (P0 #10, aday 926).

ARIZA: `hapaks` alanı bir kökün NADİRLİĞİNİ ölçmek istiyor ama TOKEN sayıyor,
AYET değil. Korpusta tek ayette geçen 420 kökün 21'i, o ayette birden çok token
taşıdığı için hapaks sayılmıyor. En çarpıcı vaka 29:41: sûrenin adını taşıyan
kök (عنكب) korpusta yalnız o ayette geçiyor, iki token, hapaks DEĞİL, ayet
yıldızsız; yedi ayet sonra 29:48'in خطط kökü tek token olduğu için sayılıyor ve
ayet ★★★.

ONARIM: yeni alan `hapaks2` — korpusta tek AYETTE geçen kök.
Eski `hapaks` alanı KORUNUR (protokol: hiçbir eski alan silinmez).
`yildiz2` ayrıca yazılır: aynı formül, hapaks yerine hapaks2 ile.

kaybedilen == 0 SAVI: hapaks2 ⊇ hapaks gösterilir.
"""
import json, collections
import kuran_akis

D = json.load(open('defter.json', encoding='utf-8'))
AKIS = kuran_akis.kelime_akisi()

ayet = collections.defaultdict(set)
token = collections.Counter()
for x in AKIS:
    if x['kok']:
        ayet[x['kok']].add(tuple(x['key']))
        token[x['kok']] += 1

HAP_ESKI = {k for k, v in ayet.items() if len(v) == 1 and token[k] == 1}
HAP_YENI = {k for k, v in ayet.items() if len(v) == 1}

print('=== ONARIM 14 — hapaks tanımı ===')
print('eski ölçüt (tek ayet VE tek token) : %d kök' % len(HAP_ESKI))
print('yeni ölçüt (tek ayet)              : %d kök' % len(HAP_YENI))
print('eklenen                            : %d kök' % len(HAP_YENI - HAP_ESKI))
print('KAYBEDİLEN                         : %d  <- sıfır olmalı' % len(HAP_ESKI - HAP_YENI))
assert not (HAP_ESKI - HAP_YENI), 'kaybedilen != 0 — onarım reddedilir'

eklenen = sorted(HAP_YENI - HAP_ESKI, key=lambda k: -token[k])
print('\neklenen kökler (token sayısıyla):')
for k in eklenen:
    a = list(ayet[k])[0]
    print('   %-8s %d token  →  %d:%d' % (k, token[k], a[0], a[1]))

# --- alanları yaz
koklar = collections.defaultdict(set)
for x in AKIS:
    if x['kok']:
        koklar[tuple(x['key'])].add(x['kok'])
for r in D:
    r['hapaks2'] = sorted(koklar[tuple(r['k'])] & HAP_YENI)

# --- yildiz2: aynı formül, hapaks yerine hapaks2
def zed(v):
    n = len(v); m = sum(v) / n
    s = (sum((x - m) ** 2 for x in v) / n) ** .5 or 1.0
    return [(x - m) / s for x in v]

n_ = [r['n'] for r in D]
ad_ = [len(r['A']) / max(r['n'], 1) for r in D]
rd_ = [len(r['R']) / max(r['n'], 1) for r in D]
hp_ = [len(r['hapaks2']) for r in D]
pa_ = [r['pas'] / max(sum(r['vf'].values()), 1) for r in D]
zs = {'n': zed(n_), 'allah': zed(ad_), 'rab': zed(rd_), 'hapaks': zed(hp_), 'pas': zed(pa_)}
for i, r in enumerate(D):
    z = {a: round(zs[a][i], 2) for a in zs}
    kir = r['z']['kafiye_kirik']
    mx = max(abs(v) for v in z.values())
    y = (3 if mx > 3 else 2 if mx > 2 else 1 if mx > 1.5 else 0) + (1 if kir and mx <= 1.5 else 0)
    r['z2'] = dict(z, kafiye_kirik=kir)
    r['yildiz2'] = min(y, 3)

esk = collections.Counter(r['yildiz'] for r in D)
yen = collections.Counter(r['yildiz2'] for r in D)
print('\n=== YILDIZ ETKİSİ ===')
print('eski : %s' % dict(sorted(esk.items())))
print('yeni : %s' % dict(sorted(yen.items())))
degis = [(tuple(r['k']), r['yildiz'], r['yildiz2']) for r in D if r['yildiz'] != r['yildiz2']]
print('değişen ayet: %d' % len(degis))
for k, a, b in degis:
    print('   %d:%-4d  ★%d → ★%d' % (k[0], k[1], a, b))

print('\nhapaks2 içeren ayet: %d  (eski hapaks: %d)'
      % (sum(1 for r in D if r['hapaks2']), sum(1 for r in D if r['hapaks'])))
json.dump(D, open('defter.json', 'w', encoding='utf-8'), ensure_ascii=False)
print('defter.json: hapaks2, z2, yildiz2 yazıldı (%d alan)' % len(D[0]))

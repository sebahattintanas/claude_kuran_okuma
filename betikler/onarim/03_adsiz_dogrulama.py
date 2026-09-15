# -*- coding: utf-8 -*-
"""ONARIM 1c — adsız aktör onarımının YANLIŞ NEGATİF DENETİMİ.
(MM dersi, aday 867: her onarım kendi yanlış negatif denetiminden geçmeli.)
"""
import re, json
from collections import defaultdict, Counter

tok = defaultdict(list)
for ln in open('morph.txt', encoding='utf-8'):
    p = ln.rstrip('\n').split('\t')
    if len(p) < 4: continue
    loc = p[0].split(':')
    if len(loc) == 5: loc = loc[1:]
    if len(loc) != 4: continue
    tok[(int(loc[0]), int(loc[1]))].append(p)

D = json.load(open('defter.json'))
DD = {tuple(r['k']): r for r in D}

print('=== (1) DÜŞEN AYETLER — hepsi artefakt mı? ===')
dusen = [tuple(r['k']) for r in D if r['adsiz'] and not r['adsiz2']]
print('düşen ayet: %d' % len(dusen))
for k in dusen:
    et = [x[1] for x in DD[k]['adsiz']]
    lm = []
    for p in tok[k]:
        m = re.search(r'LEM:([^|]+)', p[3])
        rt = re.search(r'ROOT:([^|]+)', p[3])
        if rt and m and rt.group(1) in ('فرق','مرأ','نفر','رجل','طوف','قري'):
            lm.append(m.group(1))
    print('  %-9s eski etiket=%-18s lemma=%s' % ('%d:%d' % k, ','.join(et), ','.join(lm)))

print()
print('=== (2) SINAMA KÜMESİ — okumada belgelenmiş vakalar ===')
SINAMA = [
    ((27, 23), True,  'kraliçe — DOĞRU pozitif (aday 802)'),
    ((27, 57), True,  "Lût'un karısı — eskiden KAÇIYORDU (aday 833)"),
    ((7, 83),  True,  "Lût'un karısı — eskiden kaçıyordu"),
    ((15, 60), True,  "Lût'un karısı — eskiden kaçıyordu"),
    ((28, 9),  True,  "Firavun'un karısı — eskiden kaçıyordu"),
    ((3, 35),  True,  "İmrân'ın karısı — eskiden kaçıyordu"),
    ((111, 4), True,  "Ebû Leheb'in karısı — eskiden kaçıyordu"),
    ((4, 4),   False, 'مَرِيئ (afiyetli) — eskiden YANLIŞ pozitifti'),
    ((4, 12),  True,  'gerçek kadın'),
    ((4, 128), True,  'gerçek kadın'),
    ((33, 50), True,  'gerçek kadın'),
]
gecti = 0
for k, bekle, aciklama in SINAMA:
    var = bool(DD[k]['adsiz2'])
    eski = bool(DD[k]['adsiz'])
    ok = (var == bekle)
    gecti += ok
    print('  %-8s beklenen=%-5s eski=%-5s yeni=%-5s  %s   %s' %
          ('%d:%d' % k, bekle, eski, var, 'GEÇTİ' if ok else '**DÜŞTÜ**', aciklama))
print('  sınama: %d/%d' % (gecti, len(SINAMA)))

print()
print('=== (3) imrae lemmasının TAM KAPSAMI ===')
hedef = set()
for k, ps in tok.items():
    for p in ps:
        if 'LEM:' in p[3] and re.search(r'ROOT:مرأ', p[3]):
            m = re.search(r'LEM:([^|]+)', p[3])
            if m and m.group(1).endswith('أَت'): hedef.add(k)
yak = {k for k in hedef if any(x[1] == 'imrae' for x in DD[k]['adsiz2'])}
print('امْرَأَت lemmalı ayet: %d | yeni alan yakaladı: %d | duyarlılık: %.3f' %
      (len(hedef), len(yak), len(yak) / len(hedef)))
eski_yak = {k for k in hedef if any(x[1] == 'imrae' for x in DD[k]['adsiz'])}
print('ESKİ duyarlılık: %.3f  ->  YENİ duyarlılık: %.3f' % (len(eski_yak)/len(hedef), len(yak)/len(hedef)))
yanlis = [tuple(r['k']) for r in D for x in r['adsiz2'] if x[1] == 'imrae' and tuple(r['k']) not in hedef]
print('yeni alanda imrae yanlış pozitif: %d' % len(yanlis))
print('kesinlik: %.3f -> %.3f' % (len(eski_yak)/max(1,sum(1 for r in D for x in r['adsiz'] if x[1]=='imrae')),
                                   len(yak)/max(1,sum(1 for r in D for x in r['adsiz2'] if x[1]=='imrae'))))

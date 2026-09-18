# -*- coding: utf-8 -*-
"""31_ikili.py — ONARIM 20 (aday 907/935/943'ün alt sınır kararı).

SORUN: `nakarat` alanının alt sınırı üç kelime. Okumada beş kez, sûre 29'da dört
kez, alt sınırın altında kalan gerçek tekrarlar kaydedildi — ama alt sınırı ikiye
indirmek korpusun %67,8'ini dolduruyor ve alanın YORUM değerini bitiriyor.

ÖLÇÜLEN BİLEŞİM (aday 943 verisi üzerine): alt sınır 2 ile eklenen 3762 kalıbın
  iki kelimesi de KÖK taşıyan : 1088  (%28,9)
  biri kök biri edat/zamir    : 2264  (%60,2)
  ikisi de edat/zamir         :  410  (%10,9)   ← saf gürültü
Yani iki kelimelik kalıpların %71'i en az bir işlev kelimesi içeriyor.

KARAR:
  1. `nakarat3` alt sınırı ÜÇTE KALIR — yorumda kullanılan alan odur.
  2. İki kelimelik lemma çiftleri, YALNIZ ikisi de kök taşıyorsa, ayrı bir alanda
     (`ikili`) sayılır. Bu alan SAYILIR ama YORUMA SOKULMAZ: 2635 ayette (%42,3)
     doluyor, yani tek başına ayırt edici değil.
  3. `ikili`nin işlevi, okuma sırasında 'alt sınırın altında kaldı' diye elle
     kaydedilen tekrarları ölçülebilir kılmaktır — iddia üretmek değil.

Eski alanlar KORUNUR.
"""
import json, collections

L = json.load(open('lemma_iskelet.json', encoding='utf-8'))
sure = collections.defaultdict(list)
for k, ws in L.items():
    s, a = k.split(':')
    sure[int(s)].append((int(a), ws))

dolu = collections.defaultdict(list)
kalip = 0
for s, ayetler in sure.items():
    idx = collections.defaultdict(set)
    for a, ws in ayetler:
        for i in range(len(ws) - 1):
            g = ws[i:i + 2]
            if all('|' in t for t in g):          # ikisi de kök taşıyor
                idx[' '.join(g)].add(a)
    for g, v in idx.items():
        if len(v) > 1:
            kalip += 1
            for a in v:
                dolu[(s, a)].append([g, len(v)])

D = json.load(open('defter.json', encoding='utf-8'))
for r in D:
    r['ikili'] = sorted(dolu.get(tuple(r['k']), []), key=lambda x: -x[1])

n = sum(1 for r in D if r['ikili'])
print('=== ONARIM 20 — `ikili` alanı ===')
print('kalıp     : %d' % kalip)
print('dolu ayet : %d / 6236 (%%%.1f)' % (n, 100 * n / 6236))
print()
print('ayırt edicilik karşılaştırması:')
print('  nakarat3 (3 kelime, lemma)       : 2260 ayet (%36,2)  ← YORUMDA KULLANILIR')
print('  ikili (2 kelime, ikisi de köklü) : %d ayet (%%%.1f)  ← SAYILIR, yoruma sokulmaz'
      % (n, 100 * n / 6236))
print('  2 kelime, kısıtsız               : 4230 ayet (%67,8)  ← REDDEDİLDİ')

IX = {tuple(r['k']): r for r in D}
print('\n=== SINAMA KÜMESİ — okumada "alt sınırın altında kaldı" diye kaydedilenler ===')
S = [((28, 5), (28, 41), 'جعل|جَعَلَ أمم|إِمام', 'aday 906'),
     ((29, 2), (29, 4), None, 'حسب — sûre 29 blok 1'),
     ((29, 53), (29, 54), None, 'يستعجلونك بالعذاب — sûre 29 blok 6'),
     ((29, 5), (29, 60), None, 'هو السميع العليم — mühürlü esmâ kalıbı'),
     ((29, 26), (29, 42), None, 'هو العزيز الحكيم — mühürlü esmâ kalıbı'),
     ((28, 30), (28, 46), None, 'ندي — ortak birim TEK lemma, yakalanamaz (aday 942)')]
gecen = 0
for a, b, bekle, not_ in S:
    ga = {x[0] for x in IX[a]['ikili']}
    gb = {x[0] for x in IX[b]['ikili']}
    ortak = ga & gb
    ok = bool(ortak)
    gecen += ok
    print('  %d:%-3d ↔ %d:%-3d  %-12s %s' %
          (a[0], a[1], b[0], b[1], 'YAKALANDI' if ok else 'yakalanmadı', not_))
    if ortak:
        print('     ortak: %s' % sorted(ortak))
print('  SONUÇ: %d/%d' % (gecen, len(S)))

json.dump(D, open('defter.json', 'w', encoding='utf-8'), ensure_ascii=False)
print('\ndefter.json: ikili yazıldı (%d alan)' % len(D[0]))

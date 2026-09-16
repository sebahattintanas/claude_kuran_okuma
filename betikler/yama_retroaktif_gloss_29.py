# -*- coding: utf-8 -*-
"""yama_retroaktif_gloss_29.py — sûre 29'da eklenen iki yeni kök (ركب, يأس)
11:42, 12:87 ve 12:110 okumalarında karşılıksız anma açığa çıkardı.
Aday 917'nin ikinci vakası. Karşılıklar kok_turkce.json'dan ALINIR, elle yazılmaz.
Gloss geçişi tüm alanlara uygulanır; anma parantez içinde ya da × ile olabilir."""
import json
import gloss_gecis

p = '/home/claude/repo/notlar/okuma_metni.json'
M = json.load(open(p, encoding='utf-8'))

HEDEF = [('11', '11:42'), ('12', '12:87'), ('12', '12:110')]
n = 0
for sure, ayet in HEDEF:
    rec = M[sure][ayet]
    for alan in ('olcum', 'mercek'):
        if alan not in rec:
            continue
        eski = rec[alan]
        yeni = gloss_gecis.gecir(eski)          # karşılık tablodan, elle değil
        if yeni != eski:
            rec[alan] = yeni
            n += 1
            print('yamalandı %s/%s' % (ayet, alan))

json.dump(M, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('toplam yama:', n)

# -*- coding: utf-8 -*-
"""yama_retroaktif_gloss_30.py — sûre 30'da eklenen iki yeni kök (عذر, بضع)
9:94 ve 12:65 okumalarında karşılıksız anma açığa çıkardı.
Aday 917'nin ÜÇÜNCÜ vakası — her yeni kök turu bir retroaktif tur gerektiriyor. Karşılıklar kok_turkce.json'dan ALINIR, elle yazılmaz.
Gloss geçişi tüm alanlara uygulanır; anma parantez içinde ya da × ile olabilir."""
import json
import gloss_gecis

p = '/home/claude/repo/notlar/okuma_metni.json'
M = json.load(open(p, encoding='utf-8'))

HEDEF = [('9', '9:94'), ('12', '12:65')]
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

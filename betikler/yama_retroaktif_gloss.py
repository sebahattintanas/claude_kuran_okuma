# -*- coding: utf-8 -*-
"""yama_retroaktif_gloss.py — sûre 28'de eklenen iki yeni kök (وصل, صرخ)
13:21 ve 14:22 okumalarında karşılıksız anma açığa çıkardı; turkce_denetim.py
şartı gereği (0 ihlâl) karşılıklar kok_turkce.json'dan ALINARAK eklenir.
Kök adı ELLE YAZILMAZ: okuma metnindeki anmanın kendisi kullanılır."""
import json

KT = json.load(open('kok_turkce.json', encoding='utf-8'))
p = '/home/claude/repo/notlar/okuma_metni.json'
M = json.load(open(p, encoding='utf-8'))

YAMA = [('13', '13:21', 'وصل'), ('14', '14:22', 'صرخ')]
n = 0
for sure, ayet, kok in YAMA:
    kar = KT[kok]                       # karşılık tablodan, elle değil
    rec = M[sure][ayet]
    eski = rec['olcum']
    yeni = eski.replace('%s ×' % kok, '%s *(%s)* ×' % (kok, kar))
    if yeni != eski:
        rec['olcum'] = yeni
        n += 1
        print('yamalandı %s: %s → %s *(%s)*' % (ayet, kok, kok, kar))

json.dump(M, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('toplam yama:', n)

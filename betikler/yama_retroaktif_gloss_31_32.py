# -*- coding: utf-8 -*-
"""yama_retroaktif_gloss_31_32.py — sûre 31'de eklenen 16, sûre 32'de eklenen 5 yeni kök,
daha ÖNCE okunmuş sûrelerde karşılıksız anma açığa çıkarmış olabilir.
Aday 917'nin dördüncü vakası. Karşılıklar kok_turkce.json'dan ALINIR, elle yazılmaz."""
import json, re, gloss_gecis

YENI = ['بثث','عمد','وقر','حمر','خدد','سبغ','صخر','صعر','فخر','قصد','عرو','غلظ','قلم','وثق','ختر','غيث',
        'جدد','مهن','جفو','ضجع','جرز']

# yeni köklerin korpustaki bütün ayetleri
AYET = {}
for l in open('morph.txt', encoding='utf-8'):
    p = l.rstrip('\n').split('\t'); s, a = p[0].split(':')[:2]
    for r in re.findall(r'ROOT:([^|\s]+)', p[3]):
        if r in YENI:
            AYET.setdefault(r, set()).add((int(s), int(a)))

p = '/home/claude/repo/notlar/okuma_metni.json'
M = json.load(open(p, encoding='utf-8'))
OKUNAN = {s for s in M if s.isdigit()}

hedef = sorted({(s, a) for r in YENI for (s, a) in AYET.get(r, ())
                if str(s) in OKUNAN and not (s in (31, 32))})
print('yeni kök taşıyan, DAHA ÖNCE okunmuş ayet:', len(hedef))

n = 0; yamalanan = []
for s, a in hedef:
    rec = M[str(s)].get('%d:%d' % (s, a))
    if not rec:
        continue
    for alan in ('olcum', 'mercek', 'dikey'):
        if alan not in rec:
            continue
        eski = rec[alan]; yeni = gloss_gecis.gecir(eski)
        if yeni != eski:
            rec[alan] = yeni; n += 1; yamalanan.append('%d:%d/%s' % (s, a, alan))

# güvenlik: okunan bütün kayıtlarda genel geçiş (karşılıksız anma kalmasın)
genel = 0
for s in OKUNAN:
    for k, rec in M[s].items():
        if not isinstance(rec, dict) or ':' not in k:
            continue
        for alan in ('olcum', 'mercek', 'dikey'):
            if alan in rec:
                y = gloss_gecis.gecir(rec[alan])
                if y != rec[alan]:
                    rec[alan] = y; genel += 1
json.dump(M, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('hedefli yama:', n, yamalanan[:20])
print('genel geçişte ek yama:', genel)

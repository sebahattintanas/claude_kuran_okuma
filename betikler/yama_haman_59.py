# -*- coding: utf-8 -*-
"""yama_haman_59.py — sûre 59 bloğunda kök همن (muheymin, 59:23) eklenince yama_retroaktif_gloss_59'un
genel geçişi, 28:6 / 28:8 kayıtlarındaki nakarat2 dizgesinde Hâmân adının harekesiz iskeletini kök sandı
ve 'muheymin' glossunu yapıştırdı (gloss_gecis harekesiz iskelet ↔ kök çakışması; aday 924 ailesi).
Bu betik yanlış glossu, denetimin kabul ettiği bir açıklama notuyla değiştirir (idempotent).
Araç değiştirilmez (dondurma); yalnız üç kayıt alanı. Kayıt: hasr_kayit.ARIZA (18, 24)."""
import json
p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
KOK = json.load(open('kok_turkce.json', encoding='utf-8'))
import unicodedata
kok = next(k for k in KOK if unicodedata.normalize('NFC', k) == unicodedata.normalize('NFC', 'همن'))
YANLIS = '%s *(%s)*' % (kok, KOK[kok])
DOGRU = "%s *(Hâmân adının harekesiz iskeleti; 'muheymin' kökü değil — sûre 59 çakışma yaması)*" % kok
HEDEF = [('28', '28:6', 'olcum'), ('28', '28:6', 'mercek'), ('28', '28:8', 'olcum')]
n = 0
for s, k, a in HEDEF:
    t = OM[s][k][a]
    if YANLIS in t:
        OM[s][k][a] = t.replace(YANLIS, DOGRU); n += 1
    assert DOGRU in OM[s][k][a], 'hedef alanda düzeltme yok — DUR: %s/%s' % (k, a)
# başka yerde yanlış gloss kalmış mı
kalan = [(s, k, a) for s in OM if s.isdigit() for k, v in OM[s].items() if isinstance(v, dict)
         for a in ('olcum', 'mercek', 'dikey', 'derin', 'derin2') if YANLIS in str(v.get(a, ''))
         and not (s == '59')]
assert not kalan, kalan
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('Hâmân çakışma yaması:', n, 'alan değişti; hedef', len(HEDEF))

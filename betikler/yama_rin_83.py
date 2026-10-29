# -*- coding: utf-8 -*-
"""yama_rin_83.py — sûre 83 bloğunda kök رين (râne, 83:14) eklenince yama_retroaktif_gloss_83'ün genel geçişi,
beş eski kaydın ölçüm satırındaki fâsıla kelimesinin harekesiz iskelet parçasını ('…rîn' ile biten çoğul ortaç)
kök sandı ve 'râne' glossunu yapıştırdı (gloss_gecis harekesiz iskelet ↔ kök çakışması; aday 924 ailesi;
sûre 59 Hâmân yamasının eşi). Bu betik yanlış glossu, denetimin kabul ettiği bir açıklama notuyla değiştirir
(idempotent). Araç değiştirilmez (dondurma); yalnız beş kayıt alanı. Kayıt: mutaffifin_kayit.ARIZA (11, 20)."""
import json, unicodedata
p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
KOK = json.load(open('kok_turkce.json', encoding='utf-8'))
kok = next(k for k in KOK if unicodedata.normalize('NFC', k) == unicodedata.normalize('NFC', 'رين'))
YANLIS = ' *(%s)*' % KOK[kok]
DOGRU = " *(fâsıla kelimesinin harekesiz iskelet parçası; 'râne' kökü değil — sûre 83 çakışma yaması)*"
HEDEF = [('28', '28:81'), ('29', '29:38'), ('39', '39:72'), ('40', '40:76'), ('43', '43:56')]
n = 0
for s, k in HEDEF:
    t = OM[s][k]['olcum']
    if YANLIS in t:
        OM[s][k]['olcum'] = t.replace(YANLIS, DOGRU, 1); n += 1
    assert DOGRU in OM[s][k]['olcum'] and YANLIS not in OM[s][k]['olcum'], 'hedef alanda düzeltme yok — DUR: %s' % k
kalan = [(s, k, a) for s in OM if s.isdigit() for k, v in OM[s].items() if isinstance(v, dict)
         for a in ('olcum', 'mercek', 'dikey', 'derin', 'derin2') if YANLIS in str(v.get(a, '')) and s != '83']
assert not kalan, kalan
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('râne çakışma yaması:', n, 'alan değişti; hedef', len(HEDEF))

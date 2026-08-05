# -*- coding: utf-8 -*-
"""kok_adlar.json üretimi: kavram_katalogu tersine çevrilir (430 kök),
kalan 1221 tek-lemma kök adlar_p1..p4.py'deki Claude-üretimi adlarla kapatılır.
Girdi: kok_frekans.json (morph.txt'den), kavram_katalogu.json, adlar_p1..4.py
Doğrulama: kapsama 1651/1651 olmalı; anahtarlar NFC-normalize."""
import json, unicodedata, importlib.util
N = lambda s: unicodedata.normalize('NFC', s)
frek = {N(k): v for k, v in json.load(open('kok_frekans.json')).items()}
katalog = json.load(open('kavram_katalogu.json'))
ters = {}
for ad, v in katalog.items():
    for k in v.get('kokler', []):
        ters.setdefault(N(k), []).append((ad, v.get('gecis', 0)))
claude_adlar = {}
for p in ['adlar_p1','adlar_p2','adlar_p3','adlar_p4']:
    spec = importlib.util.spec_from_file_location(p, f'{p}.py')
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    claude_adlar.update({N(k): v for k, v in m.ADLAR.items()})
sonuc = {}
for k in frek:
    if k in ters:
        s = sorted(ters[k], key=lambda x: -x[1])
        g = {"ad": s[0][0], "kaynak": "katalog", "frekans": frek[k]}
        if len(s) > 1: g["diger"] = [a for a, _ in s[1:]]
        sonuc[k] = g
    elif k in claude_adlar:
        sonuc[k] = {"ad": claude_adlar[k], "kaynak": "claude", "frekans": frek[k]}
assert len(sonuc) == len(frek), f"kapsama eksik: {len(sonuc)}/{len(frek)}"
json.dump(dict(sorted(sonuc.items(), key=lambda x: -x[1]['frekans'])),
          open('kok_adlar.json','w'), ensure_ascii=False, indent=1)
print('tamam:', len(sonuc), 'kök')

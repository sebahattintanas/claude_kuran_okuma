# -*- coding: utf-8 -*-
"""lafiz_vokatif_bayrak.py — aday 1030 kararı (2026-10-06, sûre 37 oturumu; kullanıcı): vokatif Allâhümme LAFIZ SAYILMAZ,
defter lafız alanı ve 435 K0 tanımı değişmez; ayrı 'vokatif' bayrağı tutulur.
Lemma ELLE YAZILMAZ: aday 1030'un ölçtüğü token kimliklerinden (aday_bulgular.json) morph.txt'te okunur;
aynı lemmanın korpustaki bütün tokenleri sayılır ve listeyle eşit olması doğrulanır."""
import json, re
A = json.load(open('/home/claude/repo/bulgular/aday_bulgular.json', encoding='utf-8'))
x = [d for v in A.values() if isinstance(v, list) for d in v if isinstance(d, dict) and d.get('no') == 1030][0]
tok = set(x['olculen']['token'])
lem, hepsi = set(), {}
satirlar = [l.rstrip('\n').split('\t') for l in open('morph.txt', encoding='utf-8')]
for p in satirlar:
    if len(p) >= 4 and p[0] in tok:
        lem.add(re.search(r'LEM:([^|]+)', p[3]).group(1))
assert len(lem) == 1, lem
L = lem.pop()
for p in satirlar:
    if len(p) >= 4 and re.search(r'LEM:([^|]+)', p[3]) and re.search(r'LEM:([^|]+)', p[3]).group(1) == L:
        hepsi[p[0]] = {'ayet': ':'.join(p[0].split(':')[:2]), 'yuzey': p[1], 'etiket': p[3]}
assert set(hepsi) == tok, (sorted(hepsi), sorted(tok))
out = {'karar': "aday 1030 — vokatif Allâhümme lafız SAYILMAZ (defter lafız alanı ve ONKAYIT_435_ek K0 değişmez); bu tablo ayrı bayraktır, aralık/mesafe raporlarında ayrıca işaretlenir.",
       'tarih': '2026-10-06', 'lemma': L, 'token_sayisi': len(hepsi), 'tokenler': hepsi}
json.dump(out, open('lafiz_vokatif.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('vokatif lafız bayrağı:', len(hepsi), 'token —', ', '.join(v['ayet'] for v in hepsi.values()))

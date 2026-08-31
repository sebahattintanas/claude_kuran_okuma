# -*- coding: utf-8 -*-
"""blok_dikey.py — bir ayet bloğunun ▽ dikey satırlarını üretir.
A parçası (komşuluk zenginleşmesi) BİRİNCİL, B (Allah medyan) etiketsiz.
Kullanım: python3 blok_dikey.py 21 21 40
"""
import sys, json, re
from collections import OrderedDict
import kuran_akis
from kuran_akis import kelime_akisi
from dikey_oku import dikey_oku

S = int(sys.argv[1]); A1 = int(sys.argv[2]); A2 = int(sys.argv[3])
KOK = json.load(open('kok_turkce.json', encoding='utf-8'))
AR = re.compile(r'^[\u0621-\u064A]{2,5}$')

AKIS = kelime_akisi()
ayet_kok = OrderedDict()
for x in AKIS:
    s, a = x['key']
    if s == S and A1 <= a <= A2 and x['kok']:
        ayet_kok.setdefault((s, a), [])
        if x['kok'] not in ayet_kok[(s, a)]:
            ayet_kok[(s, a)].append(x['kok'])

EKSIK = set()

def tr(ad):
    if AR.match(ad):
        if ad in KOK:
            return "%s *(%s)*" % (ad, KOK[ad])
        EKSIK.add(ad)
        return "%s *(KARŞILIK YOK)*" % ad
    return ad

BASLIK = ("DİKEY OKUMA — komşuluk zenginleşmesi (±6 kelime, Allah lafzı ve hedef kök "
          "hariç; ×kat = komşulukta gözlenen ÷ kökün korpustaki genel sıklığından "
          "beklenen; eşik 1.5). Allah medyan mesafesi İKİNCİL ve düz null ile "
          "hesaplanmıştır — etiket verilmiyor (aday 435). ⚠ = n<15.")

out = {}
for (s, a), kokler in ayet_kok.items():
    satirlar = []
    for k in kokler:
        r = dikey_oku(kok=k)
        n = r['gecis']
        uy = " ⚠" if n < 15 else ""
        def fmt(zs):
            zs = [z for z in zs if z[0] >= 1.5][:3]
            if not zs: return "—"
            return ' · '.join("%s ×%.1f" % (tr(z[1]), z[0]) for z in zs)
        satirlar.append("  · %s n=%d%s  ▸önce: %s  ▸sonra: %s  ▸Allah med=%d"
                        % (tr(k), n, uy, fmt(r.get('oncesi_zengin', [])),
                           fmt(r.get('sonrasi_zengin', [])), r['allah_medyan']))
    out["%d:%d" % (s, a)] = BASLIK + "\n" + "\n".join(satirlar)

json.dump(out, open('blok_dikey_%d_%d_%d.json' % (S, A1, A2), 'w'),
          ensure_ascii=False, indent=1)
for k, v in out.items():
    print("###", k)
    print(v.split("\n", 1)[1])
    print()
if EKSIK:
    print("KARŞILIK YOK:", ' '.join(sorted(EKSIK)))
else:
    print("karşılık eksiği yok")

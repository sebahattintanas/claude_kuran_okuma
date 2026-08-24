#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kafiye_seslendirme.py — KAFİYE SINIFINA GÖRE SESLENDİRME SETLERİ
=================================================================
ÖN-KAYIT (sonuca bakmadan yazıldı):
  seçim kuralı  : kafiye sınıfı = defter.json fs[2]
  filtre        : 8 <= mora <= 28  ·  mukattaa yok  ·  besmele-ayeti değil
  örnekleme     : uygun ayetler mutlak indekse (ai) göre sıralanır,
                  eşit aralıkla 8 ayet alınır (kiraz toplama yok)
  setler        : N(ârız) · A(açık) · R-ârız · R-çarpık · H(çarpık)
                  R sınıfı tek sınıf içinde kadans değişen tek sınıf → kontrast seti
  sentez        : tilavet_sentez.py — düz 110 Hz, HAREKE=0.20 sn (İKİSİ DE KEYFÎ)
ÇIKTI: her set için tek .wav (ayetler arası 0.6 sn sessizlik) + kafiye_setleri.json
"""
import json, os, sys, importlib.util
import numpy as np
from scipy.io import wavfile

REPO = '/home/claude/repo'
OUT  = '/mnt/user-data/outputs/kafiye_seslendirme'
os.makedirs(OUT, exist_ok=True)

spec = importlib.util.spec_from_file_location('ts', REPO + '/betikler/tilavet_sentez.py')
ts = importlib.util.module_from_spec(spec); spec.loader.exec_module(ts)

d = json.load(open(REPO + '/ciktilar/defter.json', encoding='utf-8'))
v = json.load(open(REPO + '/veri/kuran_veri.json', encoding='utf-8'))

AY = {}
for s in v['sureler']:
    for a in s['ayetler']:
        AY[(s['no'], a['no'])] = a

SETLER = {
    'N_ariz':   lambda r, a: r['fs'][2] == 'N' and a['fasila_tipi'] == 'ârız',
    'A_acik':   lambda r, a: r['fs'][2] == 'A' and a['fasila_tipi'] == 'açık',
    'R_ariz':   lambda r, a: r['fs'][2] == 'R' and a['fasila_tipi'] == 'ârız',
    'R_carpik': lambda r, a: r['fs'][2] == 'R' and a['fasila_tipi'] == 'çarpık',
    'H_carpik': lambda r, a: r['fs'][2] == 'H' and a['fasila_tipi'] == 'çarpık',
}
K = 8

def uygun(r, a):
    return 8 <= a['mora'] <= 28 and not a.get('mukattaa', 0)

rapor = {}
for ad, kural in SETLER.items():
    havuz = []
    for r in d:
        k = tuple(r['k'])
        a = AY[k]
        if uygun(r, a) and kural(r, a):
            havuz.append((r['ai'], k, r['fs'], a))
    havuz.sort()
    n = len(havuz)
    if n == 0:
        print('[!] %s boş' % ad); continue
    idx = [round(i * (n - 1) / (K - 1)) for i in range(K)] if n >= K else list(range(n))
    sec = [havuz[i] for i in sorted(set(idx))]

    parca = []; kayit = []
    ara = np.zeros(int(0.6 * ts.SR))
    for ai, k, fs, a in sec:
        y = ts.sentezle(a['ar_saf'], a.get('mukattaa', 0))
        parca.append(y); parca.append(ara)
        kayit.append(dict(ayet='%d:%d' % k, ai=ai, fasila_kelime=fs[0], kafiye_harf=fs[1],
                          sinif=fs[2], fasila_tipi=a['fasila_tipi'], mora=a['mora'],
                          ritim_kod=a['ritim_kod'], med_yuku_waqf=a['med_yuku_waqf'],
                          sure_sn=round(len(y) / ts.SR, 2), ar=a['ar_saf']))
    y = np.concatenate(parca)
    yol = os.path.join(OUT, '%s.wav' % ad)
    wavfile.write(yol, ts.SR, (y * 32767).astype(np.int16))
    rapor[ad] = dict(havuz_n=n, secilen=len(sec), toplam_sn=round(len(y) / ts.SR, 1),
                     ort_mora=round(float(np.mean([x['mora'] for x in kayit])), 1),
                     ayetler=kayit)
    print('%-9s havuz=%4d  seçilen=%d  %5.1f sn  ort mora %.1f  → %s.wav'
          % (ad, n, len(sec), len(y) / ts.SR, rapor[ad]['ort_mora'], ad))

rapor['_on_kayit'] = dict(
    secim='kafiye sınıfı = defter.json fs[2]; filtre 8<=mora<=28, mukattaa yok',
    ornekleme='ai sırasına göre eşit aralıklı %d ayet' % K,
    perde='DÜZ 110 Hz — KEYFÎ, metin perde buyurmaz',
    tempo='HAREKE=0.20 sn — KEYFÎ; ölçülen kārî aralığı 0.197–0.382 sn/hareke',
    uyari='Bu bir DEMO/dinleme çıktısıdır, bir TEST değildir. Hiçbir iddia türetilmez.')
json.dump(rapor, open(os.path.join(OUT, 'kafiye_setleri.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('\nkafiye_setleri.json yazıldı.')

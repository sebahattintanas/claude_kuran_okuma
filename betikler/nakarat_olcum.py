#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""nakarat_olcum.py — ON_KAYIT_nakarat.md protokolünü koşar."""
import json, os, subprocess, sys
import numpy as np, librosa

MP3 = '/home/claude/ses/mp3'
WAV = '/home/claude/ses/wav'
OUT = '/mnt/user-data/outputs/nakarat'
os.makedirs(WAV, exist_ok=True); os.makedirs(OUT, exist_ok=True)
SR = 22050
NAK = [13,16,18,21,23,25,28,30,32,34,36,38,40,42,45,47,49,51,53,55,57,59,61,
       63,65,67,69,71,73,75,77]

v = json.load(open('/home/claude/repo/veri/kuran_veri.json', encoding='utf-8'))
S55 = {a['no']: a for a in [x for x in v['sureler'] if x['no'] == 55][0]['ayetler']}

def wav_of(n):
    w = os.path.join(WAV, '%03d.wav' % n)
    if not os.path.exists(w):
        subprocess.run(['ffmpeg','-y','-loglevel','error','-i',
                        os.path.join(MP3,'055%03d.mp3'%n),'-ac','1','-ar',str(SR),w],
                       check=True)
    y, _ = librosa.load(w, sr=SR)
    return y

def kirp(y, oran=0.02):
    r = librosa.feature.rms(y=y, frame_length=1024, hop_length=256)[0]
    esik = r.max() * oran
    idx = np.where(r > esik)[0]
    if len(idx) == 0: return y, r
    a, b = idx[0]*256, min(len(y), (idx[-1]+1)*256)
    return y[a:b], r[idx[0]:idx[-1]+1]

kayit = {}
for n in range(1, 79):
    y = wav_of(n)
    yk, r = kirp(y)
    d = len(yk) / SR
    f0, vf, _ = librosa.pyin(yk, fmin=60, fmax=400, sr=SR, frame_length=1024)
    ok = ~np.isnan(f0)
    if ok.sum() >= 5:
        t = librosa.times_like(f0, sr=SR, hop_length=256)[ok]
        med = float(np.median(f0[ok]))
        egim = float(np.polyfit(t, f0[ok], 1)[0])
    else:
        med, egim = float('nan'), float('nan')
    m = S55[n]['mora']
    kayit[n] = dict(ayet=n, d=round(d,4), mora=m, dpm=round(d/m,5),
                    f0=round(med,2) if med==med else None,
                    egim=round(egim,3) if egim==egim else None,
                    rms=round(float(np.median(r)),5),
                    nakarat=n in NAK)
    print('%3d  d=%6.3f  mora=%3d  dpm=%.4f  f0=%6.1f  egim=%+7.2f  %s'
          % (n, d, m, d/m, med if med==med else -1, egim if egim==egim else 0,
             'NAK' if n in NAK else ''), flush=True)

def cv(x):
    x = np.asarray([v for v in x if v is not None and v == v], float)
    return float(x.std(ddof=1) / x.mean())

nak = [kayit[n] for n in NAK]
kon = [kayit[n] for n in range(2, 79) if n not in NAK]   # 55:1 hariç

son = {}
for alan in ['dpm', 'f0', 'rms']:
    a = [k[alan] for k in nak]; b = [k[alan] for k in kon]
    ca, cb = cv(a), cv(b)
    oran = ca / cb
    # permütasyon: etiketleri karıştır
    hep = np.array([x for x in a + b if x is not None and x == x], float)
    na = len(a)
    rng = np.random.default_rng(20260822)
    sim = np.empty(10000)
    for i in range(10000):
        p = rng.permutation(hep)
        sim[i] = (p[:na].std(ddof=1)/p[:na].mean()) / (p[na:].std(ddof=1)/p[na:].mean())
    pval = float((sim <= oran).mean())
    son[alan] = dict(cv_nakarat=round(ca,5), cv_kontrol=round(cb,5),
                     oran=round(oran,4), p_tek_yonlu=round(pval,5),
                     n_nak=len(a), n_kon=len(b))
    print('\n%-4s CV(nak)=%.5f  CV(kon)=%.5f  oran=%.4f  p=%.5f'
          % (alan, ca, cb, oran, pval))

# ikincil: sürüklenme
sira = np.arange(1, 32)
for alan in ['d', 'f0']:
    y = np.array([k[alan] for k in nak], float)
    ok = ~np.isnan(y)
    e, _ = np.polyfit(sira[ok], y[ok], 1)
    r = float(np.corrcoef(sira[ok], y[ok])[0,1])
    son.setdefault('suruklenme', {})[alan] = dict(egim=round(float(e),4), r=round(r,4))
    print('sürüklenme %-3s egim=%+.4f/tekrar  r=%+.3f' % (alan, e, r))

json.dump(dict(on_kayit='ON_KAYIT_nakarat.md', sure=55, kari='everyayah (ad bildirilmedi)',
               ayetler=list(kayit.values()), sonuc=son),
          open(os.path.join(OUT,'bulgu_nakarat_prozodi.json'),'w',encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('\nyazıldı.')

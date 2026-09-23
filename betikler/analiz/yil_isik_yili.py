# -*- coding: utf-8 -*-
"""Yıl sayıları → ışık yılı eşleşme testi. Ön-kayıt: notlar/ON_KAYIT_yil_isik_yili.md"""
import numpy as np, json
TEST={'31:14':2,'12:47':7,'28:27':8,'5:26':40,'46:15':40,'2:259':100,'18:25':309,'29:14':950,'2:96':1000}
L1={'Proxima':4.24,'Alfa Centauri AB':4.37,'Barnard':5.96,'Sirius':8.6,'Vega':25,'Arcturus':36.7,'Aldebaran':65.3,
    'Polaris':433,'Ülker':444,'Betelgeuse':548,'Orion Bulutsusu':1344,'Galaksi disk kalınlığı':1000,
    'Galaksi merkezi':26700,'Samanyolu yarıçapı':50000,'Büyük Macellan':160000,'Küçük Macellan':200000,'Andromeda':2500000}
L2={k:v for k,v in L1.items() if k not in ('Galaksi disk kalınlığı','Samanyolu yarıçapı')}
def eslesme(n,L): return [k for k,t in L.items() if abs(n-t)/t<=0.10]
YUV=np.array(list(range(2,13))+[15]+list(range(20,101,10))+list(range(200,1001,100)),float)
rng=np.random.default_rng(0); N=100000; k=len(TEST)
def say(arr,L):
    T=np.array(list(L.values()))
    return (np.abs(arr[...,None]-T)/T<=0.10).any(-1).sum(-1)
OUT={}
for lad,L in (('L1',L1),('L2',L2)):
    gz=sum(bool(eslesme(n,L)) for n in TEST.values())
    OUT[lad]={'gozlenen':gz,'eslesenler':{a:eslesme(n,L) for a,n in TEST.items() if eslesme(n,L)}}
    for nad in ('N1','N2'):
        arr = np.exp(rng.uniform(np.log(2),np.log(1000),(N,k))) if nad=='N1' else rng.choice(YUV,(N,k))
        s=say(arr,L); OUT[lad][nad]={'bos_ort':round(float(s.mean()),3),'p':round(float(((s>=gz).sum()+1)/(N+1)),4)}
json.dump(OUT,open('ciktilar/yil_isik_yili.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(json.dumps(OUT,ensure_ascii=False,indent=1))

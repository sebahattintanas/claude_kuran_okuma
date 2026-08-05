#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dis_sinav.py — MODELİN İLK DIŞ SINAVI
======================================
SORU: Öngörülen mora, GERÇEK kārî süresini öngörüyor mu?

ASIL SORU (ve testin bütün değeri burada):
  Mora, HARF SAYISINI yenebiliyor mu?
  Çünkü "uzun ayet uzun sürer" bilmek için tecvîde gerek yok.
  Eğer mora, harf sayısının üstüne bir şey EKLEMİYORSA,
  tecvîd modelimiz ölçülebilir hiçbir şey katmıyor demektir.

  → Bu bir NULL çıkabilir. Çıkarsa öyle yazacağız.

BEKLENTİ (önceden yazıyorum, sonuç ne olursa olsun değişmeyecek):
  - r(mora, süre) yüksek çıkacak (~0.9+) — ANLAMSIZ, uzunluk etkisi.
  - r(harf, süre) de yüksek çıkacak (~0.9+) — aynı sebep.
  - KRİTİK: kısmî korelasyon r(mora, süre | harf).
    Bu sıfıra yakınsa → tecvîd modeli ölçüme katkı yapmıyor.
    Belirgin pozitifse → med yapısı gerçek süreyi açıklıyor.

KURULUM:
  audio/1/050001.mp3 ... audio/1/050045.mp3     (kārî 1)
  audio/2/050001.mp3 ... audio/2/050045.mp3     (kārî 2)
  kuran_veri.json                                (aynı klasörde)

  pip install librosa numpy scipy

ÇALIŞTIRMA:  python dis_sinav.py
"""
import os, sys, json, warnings
warnings.filterwarnings('ignore')
import numpy as np

try:
    import librosa
except ImportError:
    sys.exit("[!] librosa yok:  pip install librosa")
from scipy import stats

SURE=50
MEDS={'A':2,'B':4,'C':6}
def birim(c): return MEDS[c] if c in MEDS else int(c)

def veri_yukle():
    if not os.path.exists('kuran_veri.json'):
        sys.exit("[!] kuran_veri.json bulunamadı (bu klasörde olmalı)")
    v=json.load(open('kuran_veri.json',encoding='utf-8'))
    s=next(x for x in v['sureler'] if x['no']==SURE)
    out=[]
    for a in s['ayetler']:
        kod=a['ritim_kod']
        out.append(dict(
            no=a['no'],
            mora=sum(birim(c) for c in kod),          # tecvîd modeli
            harf=len(kod),                             # NAİF TABAN
            med=sum(birim(c) for c in kod if c in MEDS),
            n_med=sum(1 for c in kod if c in MEDS),
            fasila=a['fasila_tipi'],
            muk=a.get('mukattaa',0),
        ))
    return out

def sure_olc(yol):
    """mp3 süresi — baştaki/sondaki sessizlik kırpılarak"""
    y,sr=librosa.load(yol,sr=22050,mono=True)
    ham=len(y)/sr
    yt,_=librosa.effects.trim(y,top_db=35)
    return ham, len(yt)/sr

def kismi_kor(x,y,z):
    """r(x,y | z) — z'nin etkisi çıkarıldıktan sonra x ile y"""
    x=np.asarray(x,float); y=np.asarray(y,float); z=np.asarray(z,float)
    rx=x-np.poly1d(np.polyfit(z,x,1))(z)      # x'in z'den artakalanı
    ry=y-np.poly1d(np.polyfit(z,y,1))(z)      # y'nin z'den artakalanı
    if np.std(rx)<1e-12 or np.std(ry)<1e-12: return 0.0,1.0
    return stats.pearsonr(rx,ry)

def main():
    A=veri_yukle()
    print("="*68)
    print("  MODELİN DIŞ SINAVI — Kāf sûresi, %d ayet"%len(A))
    print("="*68)

    kariler={}
    for k in ('1','2'):
        d=os.path.join('audio',k)
        if not os.path.isdir(d): print("\n[!] %s yok, atlanıyor"%d); continue
        print("\n── kārî %s ölçülüyor ──"%k)
        sr_ham=[]; sr_kirp=[]; idx=[]
        for a in A:
            f=os.path.join(d,"%03d%03d.mp3"%(SURE,a['no']))
            if not os.path.exists(f): continue
            try:
                ham,kirp=sure_olc(f)
            except Exception as e:
                print("   %s okunamadı: %s"%(f,e)); continue
            sr_ham.append(ham); sr_kirp.append(kirp); idx.append(a['no'])
            if a['no']<=3:
                print("   %d:%-3d  ham %.2f sn → kırpılmış %.2f sn  (mora %d)"%(
                      SURE,a['no'],ham,kirp,a['mora']))
        if len(idx)<10: print("   [!] yeterli dosya yok"); continue
        kariler[k]=dict(no=idx, sure=np.array(sr_kirp), ham=np.array(sr_ham))
        print("   toplam %d ayet · %.1f dk"%(len(idx),sum(sr_kirp)/60))

    if not kariler: sys.exit("\n[!] hiç ses bulunamadı. audio/1/ ve audio/2/ klasörlerini kontrol et.")

    for k,D in kariler.items():
        sec=[a for a in A if a['no'] in D['no']]
        mora=np.array([a['mora'] for a in sec],float)
        harf=np.array([a['harf'] for a in sec],float)
        med =np.array([a['med']  for a in sec],float)
        t=D['sure']

        print("\n" + "="*68)
        print("  KÂRÎ %s — %d ayet"%(k,len(t)))
        print("="*68)

        # 1) ham korelasyonlar (beklenen: ikisi de yüksek, ikisi de anlamsız)
        r_m,p_m=stats.pearsonr(mora,t)
        r_h,p_h=stats.pearsonr(harf,t)
        print("\n  1) HAM KORELASYONLAR  (ikisinin de yüksek çıkması BEKLENİYOR)")
        print("     r(mora, süre) = %.4f   (p=%.2e)"%(r_m,p_m))
        print("     r(harf, süre) = %.4f   (p=%.2e)"%(r_h,p_h))
        print("     r(mora, harf) = %.4f   ← ikisi birbirine ne kadar bağlı"%stats.pearsonr(mora,harf)[0])

        # 2) ASIL TEST — kısmî korelasyon
        print("\n  2) ASIL TEST — harf sayısı sabitlendiğinde mora hâlâ açıklıyor mu?")
        rp,pp=kismi_kor(mora,t,harf)
        print("     r(mora, süre | harf) = %.4f   (p=%.4f)"%(rp,pp))
        rp2,pp2=kismi_kor(harf,t,mora)
        print("     r(harf, süre | mora) = %.4f   (p=%.4f)   ← ters yön"%(rp2,pp2))
        print()
        if pp<0.05 and rp>0:
            print("     → TECVÎD MODELİ KATKI YAPIYOR: med yapısı, harf sayısının")
            print("       ötesinde gerçek süreyi açıklıyor.")
        elif pp>=0.05:
            print("     → NULL: mora, harf sayısının üstüne ölçülebilir bir şey EKLEMİYOR.")
            print("       Yani süre öngörümüz aslında 'uzun ayet uzun sürer'den ibaret.")
            print("       Tecvîd modeli süre için gereksiz demektir. Dürüst sonuç budur.")
        else:
            print("     → TERS YÖNDE: beklenmedik. İncelenmeli.")

        # 3) med yükü ayrı bir öngörücü mü?
        rmed,pmed=kismi_kor(med,t,harf)
        print("\n  3) SADECE MED SÜRESİ (harf sabitken)")
        print("     r(med, süre | harf) = %.4f   (p=%.4f)"%(rmed,pmed))

        # 4) tempo: veriden gelen gerçek sn/mora
        egim,kesme=np.polyfit(mora,t,1)
        print("\n  4) TEMPO — VERİDEN")
        print("     eğim = %.4f sn/mora   (biz 0.20 varsaymıştık)"%egim)
        print("     sabit = %.2f sn  (ayet başına sabit ek: nefes, duraklama)"%kesme)
        tahmin_saat=427667*egim/3600
        print("     → bu tempoyla TÜM KUR'ÂN: %.1f saat"%tahmin_saat)

        # 5) artıklar: model nerede yanılıyor?
        pred=egim*mora+kesme
        art=t-pred
        print("\n  5) MODEL NEREDE YANILIYOR? (en büyük 3 sapma)")
        for i in np.argsort(-np.abs(art))[:3]:
            a=sec[i]
            print("     %d:%-3d  gerçek %.2f sn · öngörü %.2f sn · sapma %+.2f  [%s%s]"%(
                SURE,a['no'],t[i],pred[i],art[i],a['fasila'],
                ", mukattaa" if a['muk'] else ""))

    # 6) kārîler arası — süre yapısı ne kadar ortak?
    if len(kariler)==2:
        k1,k2=kariler['1'],kariler['2']
        ortak=sorted(set(k1['no'])&set(k2['no']))
        t1=np.array([k1['sure'][k1['no'].index(n)] for n in ortak])
        t2=np.array([k2['sure'][k2['no'].index(n)] for n in ortak])
        print("\n" + "="*68)
        print("  KÂRÎLER ARASI")
        print("="*68)
        r12=stats.pearsonr(t1,t2)[0]
        print("\n  r(kārî1, kārî2) = %.4f  — ikisi aynı süre yapısını mı izliyor?"%r12)
        print("  tempo oranı: kārî2 / kārî1 = %.2f×"%(t2.sum()/t1.sum()))
        sec=[a for a in A if a['no'] in ortak]
        mora=np.array([a['mora'] for a in sec],float)
        rm1=stats.pearsonr(mora,t1)[0]; rm2=stats.pearsonr(mora,t2)[0]
        print("\n  METNİN PAYI:")
        print("    mora, kārî1'in süresinin %%%.0f'ini açıklıyor (r²)"%(100*rm1**2))
        print("    mora, kārî2'nin süresinin %%%.0f'ini açıklıyor (r²)"%(100*rm2**2))
        print("    kārîler birbirinin %%%.0f'ini açıklıyor"%(100*r12**2))
        print("\n  → metnin açıkladığı pay ile kārîler arası ortaklık arasındaki fark,")
        print("    metne değil İCRA GELENEĞİNE ait olan kısımdır.")

    print("\n" + "="*68)
    print("  Çıktının tamamını bana yapıştır. Null çıkarsa null yazacağız.")
    print("="*68)

if __name__=='__main__':
    main()

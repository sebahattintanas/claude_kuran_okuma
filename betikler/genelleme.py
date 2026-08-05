#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
genelleme.py — %80 GERÇEK Mİ, YOKSA KĀF'IN ÖZELLİĞİ Mİ?
========================================================
DURUM: dis_sinav.py, Kāf'ta modeli doğruladı — r(mora,süre|harf)=0.585/0.593,
       mora süre varyansının %80'ini açıklıyor. AMA: 1 sûre, 45 ayet, 2 kārî.
       Genelleme SINANMADI.

TEHLİKE: Kāf uzun-ayetli (ort 45 mora) ve %98 ârız kadanslı.
         Model yalnız BU rejimde çalışıyor olabilir.
         Ayrıca modelin sabit terimi (ayet başına ~0.85 sn nefes) kısa ayette
         toplamın %18'i, uzun ayette %4'ü — kısa ayet BAŞKA bir rejim.

SINANACAK KARŞIT SÛRELER:
    54 KAMER   55 ayet · ÇARPIK %100 · r(mora,harf)=0.927  ★ EN GÜÇLÜ SINAV
    80 ABASE   42 ayet · çarpık %45  · r=0.919 · 18 mora/ayet  ★ en iyi ayrışma
    55 Rahmân  78 ayet · ârız %97 · 30 mora/ayet · farklı rejim
    50 Kāf     45 ayet · ârız %100 · 45 mora/ayet ← taban, bulgumuz burada
   108 Kevser   3 ayet · korelasyon YOK, sadece ayet-başı hata
   103 Asr      3 ayet · mora=harf (r=1.0000), ayıramaz
     1 Fâtiha   7 ayet · ayrışma yok (r=0.999)

ÖNCEDEN YAZILMIŞ BEKLENTİ (değiştirilmeyecek):
  - Kısa/çarpık sûrelerde model DAHA KÖTÜ çalışacak. Sebebi: (a) sabit nefes payı
    oransal olarak büyük, (b) mora aralığı dar → korelasyon için az varyans,
    (c) 3-4 ayette istatistik zaten anlamsız.
  - Kevser'de n=3: KORELASYON HESAPLANAMAZ. Orada sadece ayet-başı hata bakılır.
  - GERÇEK SINAV: KAMER (çarpık %100, Kāf'ın tam zıddı) ve ABASE (18 mora/ayet).
    İkisi de Kāf'tan GÜÇLÜ ayrışmaya sahip — yani orada null çıkarsa
    "güç yetmedi" diyemeyiz. Pozitif çıkarsa → model rejimden bağımsız, %80 gerçek.
    Null çıkarsa → %80 Kāf'a özgü, ve bunu aynen yazarız.
  - Kevser/Asr/Fâtiha'da korelasyon HESAPLANAMAZ (mora≈harf). Bu modelin kusuru
    değil, kısa ayetin yapısı: med çeşitliliği yok, mora harf sayısına çöküyor.

KURULUM:
  1) İNDİR (kārî klasörünü kendin seç — elindeki audio/1, audio/2 hangi kārî ise):
       python genelleme.py --indir Husary_128kbps
     everyayah kārî klasörleri: Husary_128kbps, Abdul_Basit_Murattal_192kbps,
       Minshawy_Murattal_128kbps, Alafasy_128kbps, Abdurrahmaan_As-Sudais_192kbps ...
  2) SINA:
       python genelleme.py

  pip install librosa numpy scipy requests
"""
import os, sys, json, warnings
warnings.filterwarnings('ignore')
import numpy as np

SURELER=[108,103,1,54,80,55,50]
# GÜÇ ANALİZİYLE SEÇİLDİ (kuran_veri.json üzerinden hesaplandı):
#
#   sûre        n   mora/ayet  kadans      r(mora,harf)  test gücü
#   ─────────────────────────────────────────────────────────────────
#   108 Kevser   3      17     çarpık%100    0.866       n=3 → KORELASYON YOK,
#                                                          sadece ayet-başı hata
#   103 Asr      3      28     çarpık%100    1.0000      mora=harf, AYIRAMAZ
#     1 Fâtiha   7      27     ârız  %100    0.9990      ayrışma yok
#    54 KAMER   55      34     çarpık%100    0.9268      ★ EN GÜÇLÜ — Kāf'ın
#                                                          TAM ZIDDI kadans,
#                                                          Kāf'tan iyi ayrışma
#    80 ABASE   42      18     çarpık%45     0.9192      ★ en iyi ayrışma,
#                                                          çok kısa ayetler
#    55 Rahmân  78      30     ârız  %97     0.9635      farklı rejim: kısa
#                                                          ayetli, nakaratlı
#    50 Kāf     45      45     ârız  %100    0.9667      TABAN — bulgumuz burada
#
# ASIL SINAV: KAMER ve ABASE. İkisi de Kāf'tan GÜÇLÜ ayrışmaya sahip ve
# kadansları zıt. Orada da r(mora,süre|harf) pozitifse → %80 Kāf'a özgü değil.
# Kevser/Asr/Fâtiha korelasyon veremez — mora ile harf orada aynı şeyi ölçüyor.
# Bu, modelin kusuru değil, o sûrelerin yapısı: kısa ayette med çeşitliliği yok.
KLASOR='audio_genelleme'
MEDS={'A':2,'B':4,'C':6}
def birim(c): return MEDS[c] if c in MEDS else int(c)

def veri(sn):
    v=json.load(open('kuran_veri.json',encoding='utf-8'))
    s=next(x for x in v['sureler'] if x['no']==sn)
    return [dict(no=a['no'], mora=sum(birim(c) for c in a['ritim_kod']),
                 harf=len(a['ritim_kod']),
                 med=sum(birim(c) for c in a['ritim_kod'] if c in MEDS),
                 fasila=a['fasila_tipi'], muk=a.get('mukattaa',0)) for a in s['ayetler']], s

def indir(kari):
    import requests
    os.makedirs(KLASOR,exist_ok=True)
    v=json.load(open('kuran_veri.json',encoding='utf-8'))
    top=0
    for sn in SURELER:
        s=next(x for x in v['sureler'] if x['no']==sn)
        for a in s['ayetler']:
            ad="%03d%03d.mp3"%(sn,a['no'])
            yol=os.path.join(KLASOR,ad)
            if os.path.exists(yol): continue
            url="https://everyayah.com/data/%s/%s"%(kari,ad)
            try:
                r=requests.get(url,timeout=30)
                if r.status_code==200 and len(r.content)>2000:
                    open(yol,'wb').write(r.content); top+=1
                    if top%25==0: print("   %d indirildi..."%top)
                else:
                    print("   [!] %s → HTTP %d"%(ad,r.status_code))
            except Exception as e:
                print("   [!] %s → %s"%(ad,e))
    print("\n   toplam %d yeni dosya → %s/"%(top,KLASOR))
    print("   şimdi:  python genelleme.py")

def sure_olc(yol):
    import librosa
    y,sr=librosa.load(yol,sr=22050,mono=True)
    yt,_=librosa.effects.trim(y,top_db=35)
    return len(yt)/sr

def kismi(x,y,z):
    from scipy import stats
    x=np.asarray(x,float); y=np.asarray(y,float); z=np.asarray(z,float)
    if np.std(z)<1e-9: return stats.pearsonr(x,y)
    rx=x-np.poly1d(np.polyfit(z,x,1))(z); ry=y-np.poly1d(np.polyfit(z,y,1))(z)
    if np.std(rx)<1e-9 or np.std(ry)<1e-9: return 0.0,1.0
    return stats.pearsonr(rx,ry)

def main():
    from scipy import stats
    if not os.path.isdir(KLASOR):
        sys.exit("[!] %s yok. Önce:  python genelleme.py --indir <kari_klasoru>"%KLASOR)
    print("="*72)
    print("  GENELLEME SINAVI — %80 Kāf'a mı özgü?")
    print("="*72)
    HEP=[]
    for sn in SURELER:
        A,S=veri(sn)
        t=[]; sec=[]
        for a in A:
            f=os.path.join(KLASOR,"%03d%03d.mp3"%(sn,a['no']))
            if not os.path.exists(f): continue
            try: t.append(sure_olc(f)); sec.append(a)
            except Exception: pass
        if len(sec)<3: print("\n  %d %-10s → ses yok, atlandı"%(sn,S.get('ad_latin',''))); continue
        t=np.array(t)
        mora=np.array([a['mora'] for a in sec],float)
        harf=np.array([a['harf'] for a in sec],float)
        from collections import Counter
        fc=Counter(a['fasila'] for a in sec); bask=fc.most_common(1)[0]
        print("\n"+"─"*72)
        print("  %d. %-12s %d ayet · %.0f mora/ayet · %s %%%.0f"%(
            sn,S.get('ad_latin',''),len(sec),mora.mean(),bask[0],100*bask[1]/len(sec)))
        print("─"*72)
        if len(sec)<8:
            print("     n=%d — KORELASYON ANLAMSIZ. Ayet-başı hata:"%len(sec))
            eg=0.197; kes=0.85
            for i,a in enumerate(sec):
                p=eg*a['mora']+kes
                print("       %d:%-3d %2d mora · gerçek %5.2f sn · öngörü %5.2f · hata %+5.2f (%%%+.0f)"%(
                    sn,a['no'],a['mora'],t[i],p,t[i]-p,100*(t[i]-p)/t[i]))
            print("     (Kāf'tan ölçülen tempo 0.197 sn/mora ile — bu sûreye UYARLANMADI)")
            continue
        r_m=stats.pearsonr(mora,t); r_h=stats.pearsonr(harf,t)
        rp,pp=kismi(mora,t,harf)
        rh,ph=kismi(harf,t,mora)
        eg,kes=np.polyfit(mora,t,1)
        print("     r(mora,süre)=%.3f  ·  r(harf,süre)=%.3f  ·  r(mora,harf)=%.3f"%(
            r_m[0],r_h[0],stats.pearsonr(mora,harf)[0]))
        print("     ASIL: r(mora,süre|harf) = %+.3f  (p=%.4f)  %s"%(rp,pp,
              "← MODEL KATKI YAPIYOR" if pp<0.05 and rp>0 else "← null"))
        print("     ters: r(harf,süre|mora) = %+.3f  (p=%.4f)"%(rh,ph))
        print("     mora'nın açıkladığı: %%%.0f (r²)  ·  tempo %.3f sn/mora  ·  sabit %.2f sn"%(
            100*r_m[0]**2, eg, kes))
        HEP.append(dict(sn=sn,ad=S.get('ad_latin',''),n=len(sec),rp=rp,pp=pp,
                        r2=r_m[0]**2,eg=eg,kes=kes,mora=mora.mean(),
                        kadans=bask[0],kadans_p=100*bask[1]/len(sec)))

    if len(HEP)>=2:
        print("\n"+"="*72); print("  TOPLU GÖRÜNÜM"); print("="*72)
        print("\n  %-12s %4s %8s %9s %7s %8s %8s"%("sûre","n","kadans","r(m,s|h)","p","r²","tempo"))
        print("  "+"-"*62)
        for d in HEP:
            yz="*" if d['pp']<0.05 else " "
            print("  %-12s %4d %8s %+9.3f%s %7.4f %7.0f%% %8.3f"%(
                d['ad'][:12],d['n'],d['kadans'],d['rp'],yz,d['pp'],100*d['r2'],d['eg']))
        gecen=[d for d in HEP if d['pp']<0.05 and d['rp']>0]
        print("\n  → %d/%d sûrede model katkı yapıyor"%(len(gecen),len(HEP)))
        if len(gecen)==len(HEP):
            print("    MODEL REJİMDEN BAĞIMSIZ. %80 Kāf'a özgü değil.")
        elif len(gecen)==0:
            print("    KĀF'A ÖZGÜYMÜŞ. %80 genellenemez — bunu yazacağız.")
        else:
            print("    KISMÎ. Hangi rejimde çalıştığına bakılmalı:")
            for d in HEP:
                print("      %-12s %s  (%.0f mora/ayet, %s)"%(
                    d['ad'][:12],"✓" if d in gecen else "✗",d['mora'],d['kadans']))
        # tempo tutarlılığı
        eg=[d['eg'] for d in HEP]
        print("\n  TEMPO TUTARLILIĞI (aynı kārî, farklı sûreler):")
        print("    %.3f – %.3f sn/mora  (sd %.4f)"%(min(eg),max(eg),np.std(eg)))
        print("    → dar aralık = tempo kārînin sabiti; geniş = sûreye göre değişiyor")

    print("\n"+"="*72)
    print("  Çıktının tamamını yapıştır.")
    print("="*72)

if __name__=='__main__':
    if len(sys.argv)>2 and sys.argv[1]=='--indir': indir(sys.argv[2])
    elif len(sys.argv)>1 and sys.argv[1]=='--indir': sys.exit("[!] kārî klasörü belirt:\n    python genelleme.py --indir Husary_128kbps")
    else: main()

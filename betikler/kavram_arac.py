# -*- coding: utf-8 -*-
"""
KAVRAM SÖZLÜĞÜ ARACI
Her kavram için Kur'an'dan üç-adımlı profil çıkarır:
  1. Metinden öğren (komşu kavramlar, tanım-ayetleri)
  2. Katman imzaları (ses/zaman/yoğunluk/yapı)
  3. Zıttı (metnin kurduğu — kavram-zıt veya durum-karşıt)
Çıktı: kavram_sozlugu.json (okuma tarafının kullanacağı tanımlar)
"""
import json, re, statistics
from collections import defaultdict, Counter

veri=json.load(open('kuran_veri.json',encoding='utf-8'))
S={s['no']:s for s in veri['sureler']}
meal={}
try:
    m=json.load(open('/mnt/project/kuran_meal.json',encoding='utf-8'))
    for k,v in m.items():
        if isinstance(v,str): meal[k]=v
except: pass
MEDS={'A':2,'B':4,'C':6}
def birim(c): return MEDS[c] if c in MEDS else int(c)

# morfoloji
ay_kok=defaultdict(set)
for L in open('morph.txt',encoding='utf-8'):
    p=L.rstrip('\n').split('\t')
    if len(p)<4: continue
    mm=re.match(r'^(\d+):(\d+):',p[0])
    if not mm: continue
    key=(int(mm.group(1)),int(mm.group(2)))
    r=re.search(r'ROOT:([^\|]+)',p[3])
    if r: ay_kok[key].add(r.group(1))

order=[]; mora=[]
for no in range(1,115):
    for a in S[no]['ayetler']:
        order.append((no,a['no'])); mora.append(a.get('mora',0) or sum(birim(c) for c in a.get('ritim_kod','')))
gidx={k:i for i,k in enumerate(order)}
GENEL_MORA=statistics.mean(mora)
GENEL_YOG=statistics.mean(len(ay_kok.get(k,set())) for k in order)

# kök -> Türkçe ad sözlüğü (genişletilebilir)
ADLAR=json.load(open('kok_adlar.json',encoding='utf-8')) if __import__('os').path.exists('kok_adlar.json') else {}

GECMIS={'قصص','نوح','ابر','موسي','فرعن','عاد','ثمد','لوط','قوم','هلك','ارسل','كذب','قبل'}
GELECEK={'يوم','بعث','قيم','جنن','نار','عذب','جزي','حشر','صور','ساع','اخر','خلد'}
SIMDI={'ايي','ءمن','عبد','تقو','امر','قول','كتب','صلو','زكو'}
def zaman(k):
    ks=ay_kok.get(k,set()); g=len(ks&GECMIS); f=len(ks&GELECEK); s=len(ks&SIMDI)
    if g>=f and g>=s and g>0: return 'geçmiş'
    if f>=s and f>0: return 'gelecek'
    if s>0: return 'şimdi'
    return 'nötr'

def profil(kok, ad, zit_adaylari=None, durum_adaylari=None):
    kav=[k for k in order if kok in ay_kok.get(k,set())]
    if not kav: return None
    n=len(kav)
    # 1. komşular
    komsu=Counter()
    for k in kav:
        for kk in ay_kok.get(k,set()):
            if kk!=kok: komsu[kk]+=1
    komsu_adli=[(ADLAR.get(kk,kk),c) for kk,c in komsu.most_common(10)]
    # 2. katmanlar
    km=[mora[gidx[k]] for k in kav]
    ses=statistics.mean(km)
    ses_im='uzun' if ses>GENEL_MORA*1.1 else ('kısa' if ses<GENEL_MORA*0.9 else 'ortalama')
    zc=Counter(zaman(k) for k in kav)
    tumz=Counter(zaman(k) for k in order)
    zaman_im={z: round(100*zc[z]/n/(100*tumz[z]/len(order)),2) for z in ['geçmiş','şimdi','gelecek']}
    yog=statistics.mean(len(ay_kok.get(k,set())) for k in kav)
    yog_im='yoğun' if yog>GENEL_YOG*1.1 else ('seyrek' if yog<GENEL_YOG*0.9 else 'ortalama')
    konum=[]
    for k in kav:
        no,an=k; nn=len(S[no]['ayetler']); konum.append((an-1)/max(1,nn-1))
    yapi={'baş':round(100*sum(1 for x in konum if x<0.33)/n),
          'orta':round(100*sum(1 for x in konum if 0.33<=x<0.66)/n),
          'son':round(100*sum(1 for x in konum if x>=0.66)/n)}
    # 3. zıt
    zit={}
    if zit_adaylari:
        zc2=Counter()
        for k in kav:
            for kk in ay_kok.get(k,set()):
                if kk in zit_adaylari: zc2[kk]+=1
        zit={ADLAR.get(kk,kk):c for kk,c in zc2.most_common()}
    durum={}
    if durum_adaylari:
        dc=Counter()
        for k in kav:
            for kk in ay_kok.get(k,set()):
                if kk in durum_adaylari: dc[kk]+=1
        durum={ADLAR.get(kk,kk):c for kk,c in dc.most_common()}
    return {
        'ad':ad,'kok':kok,'ayet_sayisi':n,
        'komsu':komsu_adli,
        'ses':{'ort_mora':round(ses,1),'imza':ses_im},
        'zaman':zaman_im,
        'yogunluk':{'ort_kok':round(yog,1),'imza':yog_im},
        'yapi':yapi,
        'zit':zit,'durum':durum,
    }

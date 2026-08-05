# -*- coding: utf-8 -*-
"""
VARLIK OKUMA MAKİNESİ — tür-farkında
Bir varlık (kök/kelime) verince:
  1. TÜRÜNÜ belirler (kavram/peygamber/karşı-figür/kavim/yer/olay/sahne)
  2. Türe UYGUN okumayı yapar
  3. Zıt SADECE kavram ve peygamber/karşı-figürde aranır
Türleri metinden öğrendik; her tür kendi soru-setini alır.
"""
import json, re, statistics
from collections import defaultdict, Counter

veri=json.load(open('kuran_veri.json',encoding='utf-8'))
S={s['no']:s for s in veri['sureler']}
byk={(s['no'],a['no']):a['ar_saf'] for s in veri['sureler'] for a in s['ayetler']}
meal={}
try:
    m=json.load(open('/mnt/project/kuran_meal.json',encoding='utf-8'))
    for k,v in m.items():
        if isinstance(v,str): meal[k]=v
except: pass

ay_kok=defaultdict(set); ay_pos=defaultdict(list); ay_lem=defaultdict(set)
for L in open('morph.txt',encoding='utf-8'):
    p=L.rstrip('\n').split('\t')
    if len(p)<4: continue
    mm=re.match(r'^(\d+):(\d+):',p[0])
    if not mm: continue
    key=(int(mm.group(1)),int(mm.group(2)))
    r=re.search(r'ROOT:([^\|]+)',p[3]); l=re.search(r'LEM:([^\|]+)',p[3])
    if r: ay_kok[key].add(r.group(1))
    if l: ay_lem[key].add(l.group(1))
    ay_pos[key].append(p[3])

order=[]; morad={}
for no in range(1,115):
    for a in S[no]['ayetler']:
        order.append((no,a['no'])); morad[(no,a['no'])]=a.get('mora',0)
GENEL_MORA=statistics.mean(morad.values())
GENEL_YOG=statistics.mean(len(ay_kok.get(k,set())) for k in order)
ADLAR=json.load(open('kok_adlar.json',encoding='utf-8'))
def basit(t):
    # küçük/superscript harfleri tam harfe çevir (imlâ normalizasyonu)
    t=t.replace('\u06E6','\u064A').replace('\u06E5','\u0648')  # küçük ye→ye, küçük vav→vav
    t=t.replace('\u0670','\u0627')  # superscript elif→elif
    return re.sub(r'[^\u0621-\u064A]','',t)

GECMIS={'قصص','نوح','ابر','موسي','فرعن','عاد','ثمد','لوط','قوم','هلك','ارسل','كذب','قبل'}
GELECEK={'يوم','بعث','قيم','جنن','نار','عذب','جزي','حشر','صور','ساع','اخر','خلد'}
SIMDI={'ايي','ءمن','عبد','تقو','امر','قول','كتب','صلو','زكو'}
def zaman_of(k):
    ks=ay_kok.get(k,set()); g=len(ks&GECMIS); f=len(ks&GELECEK); s=len(ks&SIMDI)
    if g>=f and g>=s and g>0: return 'geçmiş'
    if f>=s and f>0: return 'gelecek'
    if s>0: return 'şimdi'
    return 'nötr'

# PN-etiketli lemma indeksi (özel isimleri sıfatlardan ayırmak için)
ay_pn_lem=defaultdict(set)
for _L in open('morph.txt',encoding='utf-8'):
    _p=_L.rstrip('\n').split('\t')
    if len(_p)<4: continue
    _mm=re.match(r'^(\d+):(\d+):',_p[0])
    if not _mm: continue
    if 'PN' in _p[3].split('|'):
        _lem=re.search(r'LEM:([^\|]+)',_p[3])
        if _lem: ay_pn_lem[(int(_mm.group(1)),int(_mm.group(2)))].add(_lem.group(1))

def ayetleri_bul(kok=None, kelime=None, lem=None, pn=None):
    if kok:
        return [k for k in order if kok in ay_kok.get(k,set())]
    if pn:  # SADECE özel isim (PN) etiketli — Sâlih peygamber vs sâlih sıfat
        return [k for k in order if any(pn in l for l in ay_pn_lem.get(k,set()))]
    if lem:
        return [k for k in order if any(lem in l for l in ay_lem.get(k,set()))]
    if kelime:
        return [k for k in order if re.search(kelime,basit(byk[k]))]
    return []

def tur_belirle(ayetler, kok=None, kelime=None, lem=None):
    """gramer + yaygınlık + desen ile tür tahmini"""
    n=len(ayetler)
    # özel isim mi? (PN etiketi) — SADECE aranan kelimenin kendisi
    pn=False
    for k in ayetler[:30]:
        for feat in ay_pos.get(k,[]):
            parts=feat.split('|')
            if 'PN' not in parts: continue
            # bu PN, aradığımız varlık mı? kök eşleşmeli
            if kok and ('ROOT:'+kok) in feat: pn=True
            elif kelime:
                # kelime aramasında: LEM aranan kelimeyle örtüşüyor mu
                lem=[x[4:] for x in parts if x.startswith('LEM:')]
                import re as _re
                if lem and _re.search(kelime, _re.sub(r'[^\u0621-\u064A]','',lem[0])): pn=True
    # fiil kökü mü? (V baskın)
    vcount=0
    for k in ayetler[:20]:
        for feat in ay_pos.get(k,[]):
            pass
    if n<=3: return 'tekil-sahne'
    kom=Counter()
    for k in ayetler:
        kom.update(ay_kok.get(k,set()))
    if pn:
        # özel isim: kavim/kişi ayrımı komşudan
        if kom.get('قوم',0)+kom.get('هلك',0)+kom.get('كذب',0) > n*0.4:
            return 'kavim'
        if kom.get('سمو',0) > n*0.3 and kom.get('قول',0) < n*0.3:
            return 'yer/âlem'
        return 'kişi'
    # PN olmasa da YER olabilir (arş, kürsî, cennet gibi mekân-nesneler):
    # komşusu Rab/gök yoğun + kendisi eylem yapmıyor (söz düşük)
    yer_isaret=['سمو','ربب','ستو','حمل','عظم']  # gök, Rab, istivâ, taşıma, azîm
    yer_skor=sum(kom.get(x,0) for x in yer_isaret)
    if yer_skor > n*0.6 and kom.get('قول',0) < n*0.4:
        return 'yer/âlem'
    return 'kavram'

def oku(ad, kok=None, kelime=None, lem=None, pn=None, tur=None, zit_adaylari=None):
    ayetler=ayetleri_bul(kok,kelime,lem,pn)
    if not ayetler:
        return {'ad':ad,'hata':'metinde bulunamadı'}
    if tur is None:
        tur=tur_belirle(ayetler,kok,kelime,lem)
        tur_kaynak='tahmin'
    else:
        tur_kaynak='verildi'
    n=len(ayetler)
    R={'ad':ad,'tur':tur,'tur_kaynak':tur_kaynak,'ayet_sayisi':n}
    # komşular (her tür için)
    kom=Counter()
    for k in ayetler:
        for kk in ay_kok.get(k,set()):
            if kk!=kok: kom[kk]+=1
    R['komsu']=[(ADLAR.get(kk,kk),c) for kk,c in kom.most_common(8)]
    # TÜRE GÖRE OKUMA
    if tur=='kavram':
        mo=[morad[k] for k in ayetler]
        R['ses']={'mora':round(statistics.mean(mo)),'imza':'uzun' if statistics.mean(mo)>GENEL_MORA*1.1 else ('kısa' if statistics.mean(mo)<GENEL_MORA*0.9 else 'ort')}
        zc=Counter(zaman_of(k) for k in ayetler); tz=Counter(zaman_of(k) for k in order)
        R['zaman']={z:round(100*zc[z]/n/(100*tz[z]/len(order)),2) for z in ['geçmiş','şimdi','gelecek']}
        yog=statistics.mean(len(ay_kok.get(k,set())) for k in ayetler)
        R['yogunluk']={'kok':round(yog,1),'imza':'yoğun' if yog>GENEL_YOG*1.1 else 'ort'}
        konum=[(k[1]-1)/max(1,len(S[k[0]]['ayetler'])-1) for k in ayetler]
        R['yapi']={'baş':round(100*sum(1 for x in konum if x<0.33)/n),'orta':round(100*sum(1 for x in konum if 0.33<=x<0.66)/n),'son':round(100*sum(1 for x in konum if x>=0.66)/n)}
        if zit_adaylari:
            zc2=Counter()
            for k in ayetler:
                for kk in ay_kok.get(k,set()):
                    if kk in zit_adaylari: zc2[kk]+=1
            R['zit']={ADLAR.get(kk,kk):c for kk,c in zc2.most_common(5)}
    elif tur=='kişi':
        # peygamber/karşı-figür: ne yapar + kiminle + karşısında
        R['okuma']='kişi: söz/eylem + kavim + Rab-ilişkisi'
        R['soz_yogun']=kom.get('قول',0)
    elif tur=='kavim':
        R['okuma']='kavim: elçi→tepki→kader'
        R['kader']={ADLAR.get(kk,kk):kom[kk] for kk in ['رسل','كذب','هلك','عذب'] if kk in kom}
    elif tur=='yer/âlem':
        R['okuma']='yer: kimin + nerede + nitelik'
    elif tur=='ilâhî-isim':
        # esmâ: hangi esmâ ile eşleşiyor (çift), fâsılada mı (ayet sonu)
        R['okuma']='ilâhî isim: eşleştiği esmâ + bağlam'
        # ayet sonu mu (fâsıla) — esmâ genelde ayet sonunda
        son=0
        for k in ayetler:
            t=basit(byk[k])
            R.setdefault('_',None)
        R['fasila_egilimi']='esmâ genelde ayet-sonu mührü'
    elif tur=='tekil-sahne':
        R['okuma']='tekil sahne — tek/az ayet, kıssa/misal'
        R['ayetler']=["%d:%d"%k for k in ayetler]
    # örnek ayetler (hepsi için)
    R['ornek']=["%d:%d"%k for k in ayetler[:3]]
    return R

if __name__=='__main__':
    import sys
    # test: her türden bir örnek
    testler=[
        ('hak','حقق',None,{'كفر','ضلل','بطل','ظلم','كذب'}),
        ('Mûsâ',None,r'موسى',None),
        ('Semûd',None,r'ثمود',None),
        ('Arş',None,r'العرش|عرش',None),
        ('karınca',None,r'النمل|نملة',None),
    ]
    for ad,kok,kel,zit in testler:
        r=oku(ad,kok,kel,zit)
        print("◆ %s → TÜR: %s (%d ayet)"%(r['ad'],r.get('tur','?'),r.get('ayet_sayisi',0)))
        if 'okuma' in r: print("   okuma: %s"%r['okuma'])
        if 'ses' in r: print("   ses:%s zaman:%s zıt:%s"%(r['ses']['imza'],max(r['zaman'],key=r['zaman'].get),list(r.get('zit',{}).keys())[:3]))
        if 'kader' in r: print("   kader:",r['kader'])
        print("   komşu:",[a for a,c in r['komsu'][:5]])
        print()

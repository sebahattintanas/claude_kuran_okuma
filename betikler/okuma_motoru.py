# -*- coding: utf-8 -*-
"""OKUMA MOTORU v2 — kök-anlam tablosu entegreli.
Karışık kökleri (nehir/gündüz, ilim/âlem, gök/isim...) lemma ile ayırır."""
import json, re
from collections import defaultdict
veri=json.load(open('kuran_veri.json',encoding='utf-8'))
byk={(s['no'],a['no']):a for s in veri['sureler'] for a in s['ayetler']}
meal={}
m=json.load(open('/mnt/project/kuran_meal.json',encoding='utf-8'))
for k,v in m.items():
    if isinstance(v,str): meal[k]=v

def norm(k):
    k=k.replace('أ','ا').replace('إ','ا').replace('آ','ا').replace('ٱ','ا').replace('ء','ا')
    return k.replace('ؤ','و').replace('ئ','ي')

# ayet başına (kök,lemma) çiftleri — hem kök hem lemma lazım (karışık ayrımı için)
ay_koklem=defaultdict(list); ay_pnlem=defaultdict(set)
for L in open('morph.txt',encoding='utf-8'):
    p=L.rstrip('\n').split('\t')
    if len(p)<4: continue
    mm=re.match(r'^(\d+):(\d+):',p[0])
    if not mm: continue
    key=(int(mm.group(1)),int(mm.group(2)))
    r=re.search(r'ROOT:([^\|]+)',p[3]); l=re.search(r'LEM:([^\|]+)',p[3])
    if r: ay_koklem[key].append((r.group(1), l.group(1) if l else ''))
    if l and 'PN' in p[3].split('|'): ay_pnlem[key].add(l.group(1))

katalog=json.load(open('varlik_katalog.json',encoding='utf-8'))
tablo=json.load(open('kok_anlam_tablosu.json',encoding='utf-8'))  # {kök:{lemma:kavram}}
# katalog arama kodları
kayitlar=re.findall(r"\('([^']+)',\('(kok|lem|pn|kelime)','([^']+)'\),'([^']+)'",open('varlik_katalog.py').read())
kok2ad={}; pn2ad={}
for ad,mod,val,tur in kayitlar:
    if ad not in katalog: continue
    if mod=='kok': kok2ad[norm(val)]=ad
    elif mod in ('lem','pn'): pn2ad[val]=ad
EK_KOK={'yer':'أرض','gök(çoğul)':'سمو','Hayy':'حيي','Kürsî':'كرس','şefaat':'شفع',
 'hesap':'حسب','melek':'ملك','nefs':'نفس','kalp':'قلب','zulüm':'ظلم','hikmet':'حكم'}
for ad,kok in EK_KOK.items():
    if ad in katalog: kok2ad[norm(kok)]=ad
for ad,v in katalog.items():
    if v.get('lem'): pn2ad[v['lem']]=ad

# kök-anlam tablosunun kavram→katalog-ad eşlemesi
# tablodaki kavram adı (nehir,gündüz,ilim,âlem...) katalogdaki adla eşleşmeli
KAVRAM2AD={'nehir':'nehir','ilim':'ilim','gök':'gök(çoğul)','melek':'melek','cennet':'cennet',
 'cin':'cin','kavim':'halk/kavim','zikir':'zikir','velî':None,'rüzgâr':'rüzgâr','ruh':'ruh',
 'kuş':'kuş','nefs':'nefs','kıyâmet':None,'esmâ:Kayyûm':'Kayyûm','hac':'hac',
 'gündüz':None,'âlem':None,'isim':None,'erkek':None,'delilik':None,'mülk':None,'kral':None,
 'insanlar':'insanlar/nâs','dostluk':None,'tartışma':None,'uğursuzluk':None,'alâmet':None,
 'rahatlik':None,'fesleğen':None,'nefes':None,'rekabet':None,'siper':None,'azarlama':None,'velâyet':None}


# ÖBEK KATMANI
try:
    OBEKLER=json.load(open('obek_tablosu.json',encoding='utf-8'))
    # üye→öbek haritası
    UYE2OBEK={}
    for tur,obekler in OBEKLER.items():
        for o in obekler:
            for uye in o['uyeler']:
                UYE2OBEK[uye]=(tur,o['ad'],o['not'])
except: OBEKLER={}; UYE2OBEK={}

def obekle(bulunan):
    """Bulunan varlıkları öbeklere grupla — aynı öbekten >=2 üye varsa öbek."""
    # ad eşleme: katalog-adı → öbek-üye-adı (basit)
    ADMAP={'gök(çoğul)':'gök','yer':'yer','nehir':'nehir','Hayy':'Hayy','Kürsî':'Kürsî'}
    normad=[ADMAP.get(a,a) for a in bulunan]
    obek_uyeleri=defaultdict(list)
    for a in normad:
        if a in UYE2OBEK:
            tur,adı,not_=UYE2OBEK[a]
            obek_uyeleri[(tur,adı,not_)].append(a)
    aktif=[(k,v) for k,v in obek_uyeleri.items() if len(v)>=2]
    return aktif

def oku(sure,ayet,goster=True):
    key=(sure,ayet)
    bulunan=[]
    for kok,lem in ay_koklem.get(key,[]):
        nk=norm(kok)
        # KARIŞIK kök mü? tabloya bak
        if kok in tablo:
            kavram=tablo[kok].get(lem)
            if kavram:
                ad=KAVRAM2AD.get(kavram)
                if ad and ad in katalog and ad not in bulunan: bulunan.append(ad)
            continue  # karışık kök işlendi, normal eşleştirmeye girme
        # temiz kök: normal eşleştirme
        if nk in kok2ad and kok2ad[nk] not in bulunan: bulunan.append(kok2ad[nk])
    # özel isimler
    for pnlem in ay_pnlem.get(key,set()):
        if pnlem in pn2ad and pn2ad[pnlem] not in bulunan: bulunan.append(pn2ad[pnlem])
    if goster:
        print("─"*54)
        print("  %d:%d"%(sure,ayet))
        print("  MEAL: "+meal.get("%d:%d"%(sure,ayet),"")[:110])
        print("  YAPISAL:")
        if not bulunan: print("     (saf ilâhî beyan — katalog varlığı yok)")
        for ad in bulunan:
            v=katalog.get(ad,{}); tur=v.get('tur','?'); alt=v.get('alt_tur','')
            s="     ◆ %-13s [%s%s]"%(ad,tur,'/'+alt if alt else '')
            if tur=='kavram' and v.get('zit'): s+=" zıt→%s"%list(v['zit'].keys())[0]
            elif tur=='ilâhî-isim' and v.get('esler'): s+=" eş→%s"%v['esler'][0][0]
            print(s)
        akt=obekle(bulunan)
        if akt:
            print("  ÖBEKLER (bağlam):")
            for (tur,adı,not_),uyeler in akt:
                print("     ◈ %s [%s]: %s"%(adı,tur,' + '.join(uyeler)))
                print("        %s"%not_)
        print()
    return bulunan

if __name__=='__main__':
    # karışık-kök testi: nehir vs gündüz ayırt ediliyor mu
    print("═══ KARIŞIK-KÖK AYRIMI TESTİ ═══\n")
    oku(2,164)   # gündüz geçer (nehir değil) — ayrım testi
    oku(2,25)    # nehir geçer (cennet nehirleri)
    oku(21,33)   # gece-gündüz-güneş-ay
    oku(2,255)   # Âyetü'l-Kürsî

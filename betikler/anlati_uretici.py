# -*- coding: utf-8 -*-
"""B: Ayet yapısal-anlatı üretici. ayet_okuma.json'a 'anlati' alanı ekler."""
import json, re
from collections import Counter, defaultdict

veri=json.load(open('kuran_veri.json',encoding='utf-8'))
order=[(s['no'],a['no']) for s in veri['sureler'] for a in s['ayetler']]
mora={}
for s in veri['sureler']:
    for a in s['ayetler']:
        if 'mora' in a: mora[(s['no'],a['no'])]=a['mora']
ORT=sum(mora.values())/len(mora)
tablo=json.load(open('kok_anlam_tablosu.json',encoding='utf-8'))
katalog=json.load(open('varlik_katalog.json',encoding='utf-8'))
obekler=json.load(open('obek_tablosu.json',encoding='utf-8'))
kayitlar=re.findall(r"\('([^']+)',\('(kok|lem|pn|kelime)','([^']+)'\),'([^']+)'",open('varlik_katalog.py').read())

def norm(k): return k.replace('أ','ا').replace('إ','ا').replace('آ','ا').replace('ٱ','ا').replace('ء','ا').replace('ؤ','و').replace('ئ','ي')
def hsz(s): return re.sub(r'[\u064B-\u0652\u0670\u0651]','',s)

kok2ad={}; pn2ad={}
for ad,mod,val,tur in kayitlar:
    if ad not in katalog: continue
    if mod=='kok': kok2ad[norm(val)]=ad
    elif mod in ('lem','pn'): pn2ad[val]=ad
for ad,v in katalog.items():
    if v.get('kok'): kok2ad[norm(v['kok'])]=ad
EK_KOK={'yer':'أرض','gök(çoğul)':'سمو','Hayy':'حيي','Kürsî':'كرس','şefaat':'شفع',
 'hesap':'حسب','nefs':'نفس','kalp':'قلب','zulüm':'ظلم','hikmet':'حكم','Rab':'ربب',
 'gün/yevm':'يوم','din':'دين','karınca':'نمل','ehad/teklik':'أحد'}
for ad,kok in EK_KOK.items():
    if ad in katalog: kok2ad[norm(kok)]=ad
for ad,v in katalog.items():
    if v.get('lem'): pn2ad[v['lem']]=ad
KAVRAM2AD={'nehir':'nehir','ilim':'ilim','gök':'gök(çoğul)','melek':'melek','cennet':'cennet',
 'cin':'cin','kavim':'halk/kavim','zikir':'zikir','rüzgâr':'rüzgâr','ruh':'ruh','kuş':'kuş',
 'nefs':'nefs','hac':'hac','insanlar':'insanlar/nâs','mülk':'mülk/hükümranlık','kral':'melik/mâlik'}

ay_koklem=defaultdict(list); ay_pn=defaultdict(set); ay_lemhsz=defaultdict(set)
for L in open('morph.txt',encoding='utf-8'):
    p=L.rstrip('\n').split('\t')
    if len(p)<4: continue
    mm=re.match(r'^(\d+):(\d+):',p[0])
    if not mm: continue
    key=(int(mm.group(1)),int(mm.group(2)))
    r=re.search(r'ROOT:([^\|]+)',p[3]); l=re.search(r'LEM:([^\|]+)',p[3])
    if r: ay_koklem[key].append((r.group(1),l.group(1) if l else ''))
    if l:
        if 'PN' in p[3].split('|'): ay_pn[key].add(l.group(1))
        ay_lemhsz[key].add(hsz(l.group(1)))
UYE2OBEK={}
for tur,obs in obekler.items():
    for o in obs:
        for uye in o['uyeler']: UYE2OBEK[uye]=(tur,o['ad'])
ADMAP={'gök(çoğul)':'gök','yer':'yer'}

def ayet_oku(key):
    bulunan=[]
    if 'الله' in ay_lemhsz.get(key,set()): bulunan.append('Allah')
    for kok,lem in ay_koklem.get(key,[]):
        nk=norm(kok)
        if kok in tablo:
            kav=tablo[kok].get(lem)
            if kav in KAVRAM2AD and KAVRAM2AD[kav] in katalog and KAVRAM2AD[kav] not in bulunan:
                bulunan.append(KAVRAM2AD[kav])
            continue
        if nk in kok2ad and kok2ad[nk] not in bulunan: bulunan.append(kok2ad[nk])
    for pnlem in ay_pn.get(key,set()):
        if pnlem in pn2ad and pn2ad[pnlem] not in bulunan: bulunan.append(pn2ad[pnlem])
    normad=[ADMAP.get(a,a) for a in bulunan]
    obu=defaultdict(list)
    for a in normad:
        if a in UYE2OBEK: obu[UYE2OBEK[a]].append(a)
    aktif=[{'ad':adı,'tur':tur,'uyeler':u} for (tur,adı),u in obu.items() if len(u)>=2]
    varliklar=[{'ad':ad,'tur':katalog.get(ad,{}).get('tur','?'),'alt_tur':katalog.get(ad,{}).get('alt_tur','')} for ad in bulunan]
    return varliklar,aktif

def teshis(vs):
    """Ayet türünü baskınlığa göre teşhis et."""
    t=Counter(v['tur'] for v in vs); alt=Counter(v['alt_tur'] for v in vs if v['alt_tur'])
    tekil=t.get('tekil-sahne',0); kisi=t.get('kişi',0); kavim=t.get('kavim',0)
    karsi=alt.get('karşı-figür',0); ahiret=t.get('âhiret-öğesi',0)
    kozmos=alt.get('kozmos-olayı',0); ibadet=alt.get('insan-ibadeti',0)
    hukum=t.get('hüküm-kategori',0); merkez=t.get('ilâhî-merkez',0)
    esma=t.get('ilâhî-isim',0); kavram=t.get('kavram',0)
    adlar=[v['ad'] for v in vs]
    if tekil: return "hikmet-sahnesi"
    if karsi and kisi>karsi: return "kıssa-çatışması"
    if karsi: return "karşı-figür sahnesi"
    if kavim and kisi: return "kavim-kıssası"
    if kavim: return "kavim-hatırlatması"
    if kisi: return "kıssa-sahnesi"
    # tevhîd: merkez + (esmâ veya tevhid/ehad kavramı), başka baskın tür yok
    if merkez and (esma or 'tevhid' in adlar or 'ehad/teklik' in adlar) and kozmos<2 and ahiret<2:
        return "tevhîd-beyanı"
    if kozmos>=2: return "kozmos-beyanı"
    if ahiret>=2: return "âhiret-sahnesi"
    if ahiret==1 and kavram==0: return "âhiret-anı"
    if hukum or ibadet: return "hüküm/ibadet ayeti"
    if merkez and kavram: return "beyan/hitap"
    if merkez: return "ilâhî beyan"
    if kavram>=2: return "kavram-örgüsü"
    if kavram==1: return "tek-kavram beyanı"
    return "beyan"

def anlat(key,vs,obs):
    if not vs: return "Bu ayette katalog varlığı yok — saf vurgu, hitap ya da bağlaç ayeti olabilir."
    tip=teshis(vs)
    t=Counter(v['tur'] for v in vs)
    c=[f"Bu ayet bir {tip}."]
    if t.get('ilâhî-merkez'):
        esma=[v['ad'].replace('esmâ:','') for v in vs if v['tur']=='ilâhî-isim']
        if esma: c.append(f"Merkezde Allah, yanında {', '.join(esma[:3])}.")
        else: c.append("Merkezde Allah duruyor.")
    pey=[v['ad'] for v in vs if v.get('alt_tur')=='peygamber']
    kf=[v['ad'] for v in vs if v.get('alt_tur')=='karşı-figür']
    if pey and kf: c.append(f"{', '.join(pey)} karşısında {', '.join(kf)} — çatışma ekseni.")
    elif pey: c.append(f"Sahnede {', '.join(pey)}.")
    elif kf: c.append(f"Sahnede karşı-figür: {', '.join(kf)}.")
    kavimler=[v['ad'] for v in vs if v['tur']=='kavim']
    if kavimler: c.append(f"Kavim: {', '.join(kavimler)}.")
    iyiler=[v['ad'] for v in vs if v.get('alt_tur')=='iyi-kavram']
    karsilar=[v['ad'] for v in vs if v.get('alt_tur')=='karşı-kavram']
    if iyiler and karsilar:
        c.append(f"Kavram ekseni gerilimli: {', '.join(iyiler[:3])} karşısında {', '.join(karsilar[:2])}.")
    elif len(iyiler)>=2: c.append(f"Kavramlar birlikte örülüyor: {', '.join(iyiler[:4])}.")
    elif iyiler: c.append(f"Taşıdığı kavram: {iyiler[0]}.")
    elif karsilar: c.append(f"Karşı-kavram: {', '.join(karsilar[:2])}.")
    koz=[v['ad'] for v in vs if v.get('alt_tur')=='kozmos-olayı']
    if len(koz)>=2: c.append(f"Kozmos sahnede: {', '.join(koz[:4])}.")
    ah=[v['ad'] for v in vs if v['tur']=='âhiret-öğesi']
    if ah: c.append(f"Âhiret öğesi: {', '.join(ah[:3])}.")
    for o in obs:
        c.append(f"Öbek — {o['ad']} ({'+'.join(o['uyeler'])}), {o['tur']}.")
    if not kf and not karsilar and tip in ('tevhîd-beyanı','kozmos-beyanı','hikmet-sahnesi'):
        c.append("Karşıtlık yok — gerilimsiz beyan.")
    s,a=map(int,key.split(':'))
    m=mora.get((s,a),0)
    if m: c.append(f"Ses: {'uzun' if m>=ORT else 'kısa'} ayet ({m} mora).")
    return " ".join(c)

if __name__=='__main__':
    yeni={}
    for key in order:
        k="%d:%d"%key
        vs,obs=ayet_oku(key)
        if vs: yeni[k]={'varliklar':vs,'obekler':obs,'anlati':anlat(k,vs,obs)}
    json.dump(yeni,open('ayet_okuma.json','w',encoding='utf-8'),ensure_ascii=False)
    print("✓ ayet_okuma.json — %d ayet (anlatı dahil, %.0f%%)"%(len(yeni),100*len(yeni)/6236))
    for k in ['2:255','1:4','112:1','27:18','7:54','101:6','2:183']:
        if k in yeni: print("\n◆ %s\n  %s"%(k,yeni[k]['anlati']))

# -*- coding: utf-8 -*-
"""SICAK ANLATI ÜRETİCİ: yapı + hareket, akan cümle."""
import json, re
from collections import defaultdict, Counter
veri=json.load(open('kuran_veri.json',encoding='utf-8'))
order=[(s['no'],a['no']) for s in veri['sureler'] for a in s['ayetler']]
mora={}
for s in veri['sureler']:
    for a in s['ayetler']:
        if 'mora' in a: mora[(s['no'],a['no'])]=a['mora']
ORT=sum(mora.values())/len(mora)
ao=json.load(open('ayet_okuma.json',encoding='utf-8'))
def hsz(s): return re.sub(r'[\u064B-\u0652\u0670\u0651]','',s)
ay_feat=defaultdict(list); ay_lem=defaultdict(list)
for L in open('morph.txt',encoding='utf-8'):
    p=L.rstrip('\n').split('\t')
    if len(p)<4: continue
    mm=re.match(r'^(\d+):(\d+):',p[0])
    if not mm: continue
    key=(int(mm.group(1)),int(mm.group(2)))
    ay_feat[key].append(p[3])
    l=re.search(r'LEM:([^\|]+)',p[3])
    if l: ay_lem[key].append(hsz(l.group(1)))

def hareketler(key):
    feats=ay_feat.get(key,[]); lems=ay_lem.get(key,[])
    blob='|'.join(feats); h=[]
    if '|IMPV' in blob: h.append('emir')
    if 'VOC' in blob: h.append('nidâ')
    if 'INTG' in blob: h.append('soru')
    if 'RES' in blob or 'EXP' in blob or 'الا' in lems: h.append('sınırlama')
    if 'COND' in blob: h.append('koşul')
    if any(x in lems for x in ['لا','ما','لم','لن','ليس']): h.append('olumsuzlama')
    if blob.count('GEN')>=3: h.append('bağlama')
    if 'OATH' in blob: h.append('yemin')
    return h

# hareket → sıcak ifade parçası
def hareket_cumle(h,vs):
    parts=[]
    if 'nidâ' in h: parts.append("bir sesleniş/çağrıyla açılıyor")
    if 'emir' in h: parts.append("doğrudan buyuruyor")
    if 'soru' in h: parts.append("bir soruyla muhatabı içine çekiyor")
    if 'yemin' in h: parts.append("yeminle başlıyor")
    if 'sınırlama' in h: parts.append("'ancak/hariç' diyerek bir sınır çiziyor")
    if 'koşul' in h: parts.append("bir şarta bağlıyor")
    if 'bağlama' in h: parts.append("her şeyi bir iyelik zinciriyle birbirine bağlıyor")
    return parts

def teshis(vs):
    t=Counter(v['tur'] for v in vs); alt=Counter(v['alt_tur'] for v in vs if v['alt_tur'])
    if t.get('tekil-sahne'): return "hikmet-sahnesi"
    if alt.get('karşı-figür') and t.get('kişi',0)>alt.get('karşı-figür',0): return "kıssa-çatışması"
    if alt.get('karşı-figür'): return "karşı-figür sahnesi"
    if t.get('kavim') and t.get('kişi'): return "kavim-kıssası"
    if t.get('kavim'): return "kavim-hatırlatması"
    if t.get('kişi'): return "kıssa-sahnesi"
    if t.get('ilâhî-merkez') and (t.get('ilâhî-isim') or any(v['ad'] in('tevhid','ehad/teklik') for v in vs)) and alt.get('kozmos-olayı',0)<2:
        return "tevhîd-beyanı"
    if alt.get('kozmos-olayı',0)>=2: return "kozmos-beyanı"
    if t.get('âhiret-öğesi',0)>=2: return "âhiret-sahnesi"
    if t.get('hüküm-kategori') or alt.get('insan-ibadeti'): return "hüküm/ibadet ayeti"
    if t.get('ilâhî-merkez') and t.get('kavram'): return "beyan/hitap"
    if t.get('ilâhî-merkez'): return "ilâhî beyan"
    if t.get('kavram',0)>=2: return "kavram-örgüsü"
    return "beyan"

def anlat(key):
    k="%d:%d"%key
    d=ao.get(k)
    h=hareketler(key)
    if not d or not d['varliklar']:
        # varlık yok ama hareket olabilir
        parts=[]
        if 'nidâ' in h and 'emir' in h: parts.append("Bir sesleniş ve buyrukla açılıyor")
        elif 'nidâ' in h: parts.append("Bir seslenişle açılıyor (muhataba dönüyor)")
        elif 'emir' in h: parts.append("Doğrudan bir buyruk")
        elif 'soru' in h: parts.append("Bir soru — muhatabı içine çekiyor")
        elif 'yemin' in h: parts.append("Bir yeminle açılıyor")
        elif 'sınırlama' in h: parts.append("Bir 'ancak/hariç' ile sınır çiziyor")
        elif 'olumsuzlama' in h: parts.append("Bir olumsuzlama")
        m=mora.get(key,0)
        if parts:
            s=parts[0]
            if m: s+=f" — {'uzun' if m>=ORT else 'kısa'} ayet ({m} mora)."
            else: s+="."
            return s
        return "Bu ayette adlandırılmış varlık yok — kısa bir vurgu, geçiş ya da bağ ayeti."
    vs=d['varliklar']; obs=d['obekler']
    tip=teshis(vs)
    merkez=[v['ad'] for v in vs if v['tur']=='ilâhî-merkez']
    esma=[v['ad'].replace('esmâ:','') for v in vs if v['tur']=='ilâhî-isim']
    pey=[v['ad'] for v in vs if v.get('alt_tur')=='peygamber']
    kf=[v['ad'] for v in vs if v.get('alt_tur')=='karşı-figür']
    kavim=[v['ad'] for v in vs if v['tur']=='kavim']
    iyi=[v['ad'] for v in vs if v.get('alt_tur')=='iyi-kavram']
    kar=[v['ad'] for v in vs if v.get('alt_tur')=='karşı-kavram']
    koz=[v['ad'] for v in vs if v.get('alt_tur')=='kozmos-olayı']
    ah=[v['ad'] for v in vs if v['tur']=='âhiret-öğesi']
    c=[]
    hp=hareket_cumle(h,vs)
    # AÇILIŞ — harekete göre
    if 'nidâ' in h and 'emir' in h:
        c.append(f"Ayet bir çağrı: sesleniyor ve buyuruyor.")
    elif 'emir' in h:
        c.append(f"Ayet doğrudan buyurarak açılıyor.")
    elif 'soru' in h:
        c.append(f"Ayet bir {tip}, ama soru kipinde — muhatabı düşünmeye çağırıyor.")
    elif 'yemin' in h:
        c.append(f"Yeminle açılan bir {tip}.")
    else:
        c.append(f"Bu ayet bir {tip}.")
    # MERKEZ ve hareketi
    if merkez:
        if esma:
            c.append(f"Merkezde {merkez[0]} var; O'nu {', '.join(esma[:3])} olarak tanıtıyor.")
        else:
            c.append(f"Merkezde {merkez[0]} duruyor.")
        if 'bağlama' in h:
            c.append("Her şeyi O'na bağlıyor — iyelik zinciriyle sahiplik O'nda toplanıyor.")
    # KİŞİLER
    if pey and kf:
        c.append(f"{', '.join(pey)} ile {', '.join(kf)} karşı karşıya — sahne bir çatışma.")
    elif pey:
        c.append(f"Sahnede {', '.join(pey)}" + (", kavmiyle" if kavim else "") + ".")
    elif kf:
        c.append(f"Karşı-figür sahnede: {', '.join(kf)}.")
    elif kavim:
        c.append(f"Bir kavim anılıyor: {', '.join(kavim)}.")
    # KAVRAM HAREKETİ
    if iyi and kar:
        c.append(f"İki kutbu karşı koyuyor: {', '.join(iyi[:2])} ↔ {', '.join(kar[:2])}.")
    elif len(iyi)>=2:
        c.append(f"{', '.join(iyi[:3])} kavramlarını bir arada örüyor.")
    elif iyi:
        c.append(f"Taşıdığı kavram {iyi[0]}" + ("; ama bir sınıra bağlıyor" if 'sınırlama' in h else "") + ".")
    elif kar:
        c.append(f"Olumsuz kutbu anlatıyor: {', '.join(kar[:2])}.")
    # KOZMOS
    if len(koz)>=2:
        c.append(f"Kozmosu tanık gösteriyor: {', '.join(koz[:4])}.")
    # ÂHİRET
    if ah:
        c.append(f"Âhiretten bir sahne/öğe: {', '.join(ah[:3])}.")
    # ÖBEK
    for o in obs:
        rel={'bütünleyen':'tek bütün olarak','karşıt':'karşı kutup olarak','esmâ-çifti':'mühür gibi yan yana','sıralı-dizi':'bir dizi hâlinde'}.get(o['tur'],'')
        c.append(f"{' + '.join(o['uyeler'])} {rel} geçiyor ({o['ad']}).")
    # sınırlama vurgusu (merkez yoksa da)
    if 'sınırlama' in h and not merkez:
        c.append("Bir 'ancak/hariç' ile sınır çiziyor.")
    # KAPANIŞ: ses
    s,a=key; m=mora.get(key,0)
    if m:
        if m>=ORT*1.5: c.append(f"Uzun, genişleyen bir ayet ({m} mora) — beyan uzadıkça açılıyor.")
        elif m<=ORT*0.5: c.append(f"Kısa ve vurucu ({m} mora).")
        else: c.append(f"{'Uzun' if m>=ORT else 'Kısa'} ayet ({m} mora).")
    if not kf and not kar and tip in('tevhîd-beyanı','kozmos-beyanı','hikmet-sahnesi'):
        c.append("Baştan sona karşıtsız, tek yöne bakıyor.")
    return " ".join(c)

if __name__=='__main__':
    for key in [(2,255),(112,1),(1,1),(74,1),(2,30),(96,1),(7,54),(101,6)]:
        print("◆ %d:%d"%key); print("  "+anlat(key)); print()

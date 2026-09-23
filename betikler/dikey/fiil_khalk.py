# -*- coding: utf-8 -*-
"""خلق fiili bütün Kur'an'da. Ön-kayıt: notlar/ON_KAYIT_fiil_khalk.md"""
import collections, json, random
KEL=collections.OrderedDict()
for l in open('veri/morph.txt',encoding='utf-8'):
    p=l.rstrip('\n').split('\t'); s,a,w,g=map(int,p[0].split(':'))
    KEL.setdefault((s,a,w),[]).append(dict(f=p[1],pos=p[2],t=p[3].split('|')))
AY=collections.OrderedDict()
for (s,a,w),segs in KEL.items(): AY.setdefault((s,a),[]).append(((s,a,w),segs))
TIP={tuple(x['k']):x['tip'] for x in json.load(open('ciktilar/defter.json'))}
KISI={'1S','1P','2MS','2FS','2MP','2FP','2D','3MS','3FS','3MP','3FP','3D','3MD','3FD','2MD'}
EKLI={'1S','1P','2MS','2FS','2MP','2FP','2D','3MP','3FP','3D','3MD','3FD','2MD'}
lem=lambda sg:next((x[4:] for x in sg['t'] if x.startswith('LEM:')),'?')
kayit=[]
for (s,a),L_ in AY.items():
    for i,(key,segs) in enumerate(L_):
        vi=[j for j,sg in enumerate(segs) if sg['pos']=='V' and 'ROOT:خلق' in sg['t']]
        if not vi: continue
        v=segs[vi[0]]; kisi=next((x for x in v['t'] if x in KISI),'?'); pas='PASS' in v['t']
        suf=[sg for sg in segs[vi[0]+1:] if 'PRON' in sg['t'] and 'SUFF' in sg['t']]
        nesne=None; kaynak=None
        if not pas:
            ob=suf[1:] if kisi in EKLI else suf
            if ob: nesne='zamir:'+next((x for x in ob[0]['t'] if x in KISI),'?'); kaynak='ek'
            else:
                for j in range(i+1,min(i+5,len(L_))):
                    ss=L_[j][1]
                    if ss[0]['pos']=='P' and 'DET' not in ss[0]['t'] and 'CONJ' not in ss[0]['t']: continue  # edatla bağlı
                    n=[sg for sg in ss if sg['pos']=='N' and 'ACC' in sg['t'] and lem(sg)!='اللَّه']
                    if n: nesne=lem(n[0]); kaynak='isim'; break
        else:
            for j in range(i+1,min(i+4,len(L_))):
                n=[sg for sg in L_[j][1] if sg['pos']=='N' and 'NOM' in sg['t']]
                if n: nesne=lem(n[0]); kaynak='NOM'; break
            if not nesne: nesne='kişi:'+kisi; kaynak='kişi'
        kayit.append(dict(ayet=f'{s}:{a}',s=s,w=key[2],n=len(L_),kisi=kisi,pas=pas,nesne=nesne or 'belirsiz',kaynak=kaynak,
                          tip=TIP[(s,a)],metin=' '.join(''.join(x['f'] for x in sg) for _,sg in L_)))
OUT={}
ay={k['ayet'] for k in kayit}
OUT['O1']={'token':len(kayit),'ayet':len(ay),'sure':len({k['s'] for k in kayit}),
           'mekki_token':round(sum(k['tip']=='M' for k in kayit)/len(kayit),3)}
et=[k for k in kayit if not k['pas']]; ed=[k for k in kayit if k['pas']]
OUT['O2']={'etken':dict(collections.Counter(k['kisi'] for k in et).most_common()),'edilgen':dict(collections.Counter(k['kisi'] for k in ed).most_common()),
           '1P+3MS_etken_oran':round(sum(k['kisi'] in('1P','3MS') for k in et)/len(et),3)}
OUT['O3']={'etken_nesne':collections.Counter(k['nesne'] for k in et).most_common(20),
           'edilgen_naib':collections.Counter(k['nesne'] for k in ed).most_common(20)}
OUT['O4']=[(k['ayet'],k['kisi'],k['metin']) for k in et if k['kisi'] not in ('1P','3MS','1S')]
OUT['O5']={'ilk_kelime':sum(k['w']==1 for k in kayit),'goreli_ort':round(sum((k['w']-1)/max(1,k['n']-1) for k in kayit)/len(kayit),3)}
rnd=random.Random(0); orn=rnd.sample(kayit,25)
OUT['dogrulama_ornek']=[(k['ayet'],k['kisi'],'PASS' if k['pas'] else 'ACT',k['nesne'],k['metin']) for k in orn]
json.dump(dict(OUT,kayit=kayit),open('ciktilar/fiil_khalk.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
for k in ('O1','O2','O5'): print(k,OUT[k])
print('O3 etken nesne:',OUT['O3']['etken_nesne']); print('O3 edilgen:',OUT['O3']['edilgen_naib'])
print('O4',len(OUT['O4']))
for x in OUT['O4']: print('  ',x[0],x[1],x[2][:80])

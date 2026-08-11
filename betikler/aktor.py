# -*- coding: utf-8 -*-
"""defter v6 — AKTÖR KATMANI
Yeni alanlar (ayet başına):
  adli    [[kelime_sıra, lemma, tür], ...]  ayette geçen ADLI varlıklar
          tür: kisi / kavim / yer / kitap / gayb
  adsiz   [[kelime_sıra, işaretçi]]  ADSIZ aktör işaretçileri
          (رجل, امرأة, نفر, قوم+adsız, الذي+fiil öznesi, من+fiil, فريق, طائفة...)
  rol     {lemma: [rol,...]}  KAPALI SÖZLÜK — morfolojiden türetilir:
          fail      : NOM ve yakınında etken fiil
          meful     : ACC
          mecrur    : GEN (izâfet/harf-i cer)
          muhatap   : ayette 2. şahıs var ve ad nidâ ile anılmış (VOC)
          konusan   : ad قول fiiline bitişik özne konumunda
Ayrı tablo: aktor_tablosu.json — aktör başına ayet-ayet rol dizisi (dönüşüm).

SINIR: 'rol' i'râb + komşuluk üzerinden YAKLAŞIK türetilir; bağımlılık
       çözümlemesi değildir. Kıssa sınırı ve kıssa-başına sayım BU TURDA
       YAPILMAZ — sınır kararı tüm veri görülmeden verilmeyecek.
"""
import re, json
from collections import defaultdict, Counter

KAT = json.load(open('../repo/tablolar/varlik_katalog.json', encoding='utf-8'))
TUR = {k: v.get('tur') for k, v in KAT.items()}
# katalogdaki kişi adlarının Arapça lemma karşılıkları (PN taramasından)
PN_TUR = {
 'مُوسَى':'kisi','إِبْراهِيم':'kisi','نُوح':'kisi','عِيسَى':'kisi','يُوسُف':'kisi',
 'سُلَيْمان':'kisi','داوُۥد':'kisi','هارُون':'kisi','إِسْحاق':'kisi','يَعْقُوب':'kisi',
 'إِسْماعِيل':'kisi','آدَم':'kisi','مَرْيَم':'kisi','لُوط':'kisi','شُعَيْب':'kisi',
 'صالِح':'kisi','هُود':'kisi','زَكَرِيّا':'kisi','يَحْيَى':'kisi','يُونُس':'kisi',
 'لُقْمان':'kisi','فِرْعَوْن':'kisi','هامان':'kisi','قارُون':'kisi','إِدْرِيس':'kisi',
 'جالُوت':'kisi','طالُوت':'kisi','إِلْياس':'kisi','أَحْمَد':'kisi','عُزَيْر':'kisi',
 'مُحَمَّد':'kisi','ٱلْيَسَع':'kisi','ذُو ٱلْكِفْل':'kisi','إِسْرائِيل':'kisi',
 'شَيْطان':'gayb','إِبْلِيس':'gayb','جِبْرِيل':'gayb','مِيكال':'gayb',
 'هارُوت':'gayb','مارُوت':'gayb','ٱللَّه':'ilahi',
 'ثَمُود':'kavim','عاد':'kavim','قُرَيْش':'kavim','مَدْيَن':'kavim',
 'جَهَنَّم':'yer','جَنَّة':'yer','مَكَّة':'yer','بَكَّة':'yer','بابِل':'yer',
 'سَبَإ':'yer','مِصْر':'yer','طُوَى':'yer','سِينِين':'yer','ٱلطُّور':'yer',
 'قُرْءان':'kitab','تَوْراة':'kitab','إِنجِيل':'kitab','زَبُور':'kitab','فُرْقان':'kitab',
}
ADSIZ = {'رَجُل':'racül','ٱمْرَأَة':'imrae','نَفَر':'nefer','فَرِيق':'ferîk',
         'طائِفَة':'tâife','قَوْم':'kavm','أُمَّة':'ümmet','عَبْد':'abd','قَرْيَة':'karye'}

tok = defaultdict(list)
for ln in open('morph.txt', encoding='utf-8'):
    p = ln.rstrip('\n').split('\t')
    if len(p) < 4: continue
    loc = p[0].split(':')
    if len(loc) == 5: loc = loc[1:]
    if len(loc) != 4: continue
    tok[(int(loc[0]), int(loc[1]))].append(
        {'w': int(loc[2]), 'ar': p[1], 'pos': p[2], 'f': p[3]})

def lem(f):
    m = re.search(r'LEM:([^|]+)', f); return m.group(1) if m else ''

D = json.load(open('defter.json'))
aktor = defaultdict(list)     # lemma -> [[sure,ayet,rol...],...]
for r in D:
    k = (r['k'][0], r['k'][1]); S = tok.get(k, [])
    adli = []; adsiz = []; rol = {}
    ikinci = '2' in r.get('sahset', [])
    for i, s in enumerate(S):
        p = s['f'].split('|')
        L = lem(s['f'])
        if 'PN' in p and L and L != 'ٱللَّه':
            t = PN_TUR.get(L, 'diger')
            adli.append([s['w'], L, t])
            rr = []
            if 'NOM' in p: rr.append('fail')
            if 'ACC' in p: rr.append('meful')
            if 'GEN' in p: rr.append('mecrur')
            # nidâ ile anılmış mı
            if i > 0 and 'VOC' in S[i-1]['f'].split('|'): rr.append('muhatap')
            # قول fiiline bitişik mi
            for q in S[max(0,i-2):i]:
                if re.search(r'ROOT:قول', q['f']) and q['pos'] == 'V': rr.append('konusan'); break
            if rr: rol.setdefault(L, []).extend(rr)
            if t in ('kisi', 'gayb', 'kavim'):
                aktor[L].append([r['k'][0], r['k'][1], sorted(set(rr))])
        if L in ADSIZ and 'INDEF' in p:
            adsiz.append([s['w'], ADSIZ[L]])
    r['adli'] = adli
    r['adsiz'] = adsiz
    r['rol'] = {a: sorted(set(b)) for a, b in rol.items()}

json.dump(D, open('defter.json', 'w', encoding='utf-8'), ensure_ascii=False)
json.dump({a: v for a, v in aktor.items()}, open('aktor_tablosu.json', 'w', encoding='utf-8'), ensure_ascii=False)

print('adlı varlık içeren ayet: %d' % sum(1 for r in D if r['adli']))
print('adsız aktör işaretçisi içeren ayet: %d' % sum(1 for r in D if r['adsiz']))
print('her ikisi: %d' % sum(1 for r in D if r['adli'] and r['adsiz']))
print('aktör tablosu: %d aktör' % len(aktor))
c = Counter(t for r in D for _, _, t in r['adli'])
print('adlı varlık türleri:', dict(c.most_common()))
rc = Counter(x for r in D for v in r['rol'].values() for x in v)
print('rol dağılımı:', dict(rc))
ac = Counter(x[1] for r in D for x in r['adsiz'])
print('adsız işaretçiler:', dict(ac.most_common()))
print()
print('en çok geçen aktörler:', [(a, len(v)) for a, v in sorted(aktor.items(), key=lambda x: -len(x[1]))[:12]])

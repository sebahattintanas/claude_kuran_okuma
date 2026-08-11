# -*- coding: utf-8 -*-
"""okuma_baglantilari.json'daki elle kurulmuş bağları:
 (1) TERS-BAĞ ile simetrik hâle getir
 (2) KURALA eşle ve kuralı betikle doğrula
 (3) GÜVEN etiketi ver: dogrulandi / elle / yorum

KURAL TÜRLERİ (her biri betikle sınanabilir):
  L1 tam-ayet     : normalize ayet metni birebir aynı
  L2 lafiz        : >=3 kelimelik ortak dizi (lemma düzeyi)
  L3 iskelet      : lemma dizisi >=4, en fazla 2 terim farkla
  L4 kok-cift     : aynı iki kök yan yana, iki ayette de
  L5 kok-anlam    : aynı kök, farklı kavrama çözülüyor
  L6 figur        : aynı biçim etiketi (defter fig alanı)
  Y  yorum        : yukarıdakilerin hiçbiri — saf yargı
"""
import json, re, unicodedata
from collections import defaultdict
import kuran_akis as K

ak = K.kelime_akisi()
d = json.load(open('../repo/veri/kuran_veri.json'))
T = {}; LEM = defaultdict(list); KOK = defaultdict(list)
for s in d['sureler']:
    for a in s['ayetler']: T[(s['no'], a['no'])] = a['ar_saf']
for x in ak:
    k = (x['key'][0], x['key'][1])
    if x['lem_hsz']: LEM[k].append(x['lem_hsz'])
    if x['kok']: KOK[k].append(x['kok'])

def sad(x):
    x = unicodedata.normalize('NFC', x)
    x = re.sub(r'[\u064B-\u0652\u0670\u06DD\u06D6-\u06ED\u0640]', '', x)
    x = x.replace('ٱ','ا').replace('أ','ا').replace('إ','ا').replace('آ','ا').replace('ى','ي').replace('ة','ه')
    return re.sub(r'\s+', ' ', re.sub(r'[^\u0621-\u064A ]', ' ', x)).strip()

def ngram(L, n):
    return {tuple(L[i:i+n]) for i in range(len(L)-n+1)}

def kural(a, b):
    """iki ayet anahtarı arasındaki en güçlü doğrulanabilir kuralı döndür"""
    if a not in T or b not in T: return None, None
    if sad(T[a]) == sad(T[b]) and len(sad(T[a]).split()) >= 3: return 'L1', 'tam-ayet özdeşliği'
    La, Lb = LEM[a], LEM[b]
    for n in (5, 4, 3):
        ort = ngram(La, n) & ngram(Lb, n)
        if ort: return 'L2', '%d-kelimelik ortak lemma dizisi (%d adet)' % (n, len(ort))
    # iskelet: aynı uzunlukta pencerede <=2 fark
    for w in range(6, 3, -1):
        for i in range(len(La)-w+1):
            for j in range(len(Lb)-w+1):
                f = sum(1 for p, q in zip(La[i:i+w], Lb[j:j+w]) if p != q)
                if f <= 2: return 'L3', '%d-terimlik iskelet, %d fark' % (w, f)
    ka, kb = KOK[a], KOK[b]
    ortk = set(ka) & set(kb)
    cift = set()
    for i in range(len(ka)-1):
        if (ka[i], ka[i+1]) in {(kb[j], kb[j+1]) for j in range(len(kb)-1)}: cift.add((ka[i], ka[i+1]))
    if cift: return 'L4', 'ortak bitişik kök çifti: %s' % ['+'.join(c) for c in list(cift)[:3]]
    if len(ortk) >= 3: return 'L5', 'ortak kök: %s' % sorted(ortk)[:5]
    return 'Y', 'doğrulanabilir lafzî temel YOK — saf yargı'

B = json.load(open('okuma_baglantilari.json', encoding='utf-8'))
ciftler = B['lafiz_ozdesligi']['cift']
sonuc = []; ters = defaultdict(list)
for c in ciftler:
    a_s, b_s, aciklama = c[0], c[1], c[2]
    def pars(s):
        out = []
        for p in s.split('|'):
            p = p.strip()
            m = re.match(r'^(\d+):(\d+)', p)
            if m: out.append((int(m.group(1)), int(m.group(2))))
        return out
    A_, B_ = pars(a_s), pars(b_s)
    if not A_ or not B_:
        sonuc.append({'a': a_s, 'b': b_s, 'aciklama': aciklama, 'kural': 'Y',
                      'gerekce': 'ayet aralığı — tekil anahtar çözülemedi', 'guven': 'elle'})
        continue
    a, b = A_[0], B_[0]
    kod, ger = kural(a, b)
    guven = 'dogrulandi' if kod in ('L1','L2','L3','L4') else ('elle' if kod == 'L5' else 'yorum')
    sonuc.append({'a': '%d:%d' % a, 'b': '%d:%d' % b, 'aciklama': aciklama,
                  'kural': kod, 'gerekce': ger, 'guven': guven})
    ters['%d:%d' % a].append('%d:%d' % b)
    ters['%d:%d' % b].append('%d:%d' % a)

B['lafiz_ozdesligi']['kural_kodlari'] = {
 'L1':'tam-ayet özdeşliği','L2':'>=3 kelimelik ortak lemma dizisi','L3':'iskelet (<=2 terim fark)',
 'L4':'ortak bitişik kök çifti','L5':'>=3 ortak kök (zayıf)','Y':'doğrulanabilir lafzî temel yok — saf yargı'}
B['lafiz_ozdesligi']['guven_etiketleri'] = {
 'dogrulandi':'betikle kontrol edildi, lafzî temel var','elle':'zayıf lafzî temel — ben kurdum','yorum':'lafzî temel yok, yargı'}
B['lafiz_ozdesligi']['denetlenmis_cift'] = sonuc
B['ters_bag'] = {k: sorted(set(v)) for k, v in sorted(ters.items())}
B['okuma_sirasi_carpikligi'] = {
 'sorun': 'Bağ yoğunluğu okuma sırasının eseri: erken sûreler okunurken geç sûrelere bağ kurulamıyordu. Bakara okunurken En\'âm daha okunmamıştı; En\'âm okunurken Bakara\'ya onlarca bağ kuruldu.',
 'olcum': None,
 'cozum': 'ters_bag alanı simetriyi kuruyor. Ama YÖN bilgisi korunuyor: bağı hangi ayeti okurken kurduğum aşağıda.'}
json.dump(B, open('okuma_baglantilari.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)

from collections import Counter
print('denetlenen çift: %d' % len(sonuc))
print('kural dağılımı:', dict(Counter(x['kural'] for x in sonuc)))
print('güven dağılımı:', dict(Counter(x['guven'] for x in sonuc)))
print('ters-bağ ile bağlanan ayet: %d' % len(ters))
print()
print('--- YORUM etiketli (lafzî temeli olmayan) çiftler ---')
for x in sonuc:
    if x['kural'] == 'Y': print('   %-8s %-8s %s' % (x['a'], x['b'], x['aciklama'][:60]))
print()
print('--- ELLE etiketli (zayıf temel) ---')
for x in sonuc:
    if x['guven'] == 'elle': print('   %-8s %-8s %s | %s' % (x['a'], x['b'], x['aciklama'][:45], x['gerekce'][:45]))

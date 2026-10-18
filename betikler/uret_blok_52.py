# -*- coding: utf-8 -*-
"""uret_blok_52.py — sûre 52 (Tûr) blok betiklerini üretir. BLOK BAŞINA KAYIT.

Değişiklik (2026-09-24): kayıt artık tur sonunu beklemiyor. Her blok betiği koşulduğunda
okuma_metni.json, mercek_kayit.json ve ilerleme o blok için yazılır; blok bilançosu (TAM SAYIM)
ve çıpa kararları da okuma_metni'ne yapılandırılmış alan olarak girer. Oturum yarıda kalsa da
okunmuş her blok kayıtlıdır.

Sûre numarası TEK değişkende (S). olcum_bicim.olcum(S, n), AR[(S, n)], OM[str(S)] hep S'den
türer — üç kez atlanan elle-değiştirme hatası (tur sonu notu) burada yapısal olarak kapalı.
Besmele korpustan (1:1'in ilk dört kelimesinin iskeleti) ayıklanır; Arapça sabit yok.
"""
import sys
S = 52
METIN = 'tur_metin_1'
KAYIT = 'tur_kayit'
# blok başı kayıt: blok okundukça listeye eklenir (başlık okuma sonrası yazılır)
BLOKLAR = [(1, 10), (11, 20), (21, 30), (31, 40), (41, 49)]
BASLIK = {
 (1, 10): "sûre 52 (Tûr) birinci blok — Tûr'a, açılmış ince deride satır satır yazılmış kitaba, mamur eve, yükseltilmiş tavana, kabarmış denize andolsun; Rabbinin azabı mutlaka gerçekleşecektir, onu savacak yoktur; o gün gök çalkalandıkça çalkalanır, dağlar yürüdükçe yürür",
 (11, 20): "sûre 52 (Tûr) ikinci blok — o gün vay boş söze dalıp oynayan yalanlayanlara; cehennem ateşine itilirler: yalanladığınız ateş budur, bu da mı büyü, yoksa görmüyor musunuz; girin, sabretseniz de etmeseniz de birdir, yaptıklarınızın karşılığını görüyorsunuz; sakınanlar bahçelerde ve nimettedir, Rablerinin verdikleriyle keyif sürerler, Rableri onları azaptan korumuştur; afiyetle yiyin için; dizili tahtlara yaslanırlar, onları iri gözlü hûrilerle eşleştirdik",
 (21, 30): "sûre 52 (Tûr) üçüncü blok — inananlara imanla uyan soylarını kattık, amellerinden bir şey eksiltmedik, herkes kazandığına rehindir; meyve ve et verdik; kadeh kapışırlar, boş söz ve günah yok; saklı inci gibi delikanlılar dolaşır; birbirlerine dönüp derler: biz önce ailemiz içinde korkardık, Allah lütfetti, bizi semûm azabından korudu, O'na dua ederdik, O iyiliği bol ve merhametlidir; öğüt ver, Rabbinin nimetiyle sen ne kâhinsin ne mecnun; yoksa şairdir, felaketini bekliyoruz mu diyorlar",
 (31, 40): "sûre 52 (Tûr) dördüncü blok — de ki: bekleyin, ben de sizinle bekleyenlerdenim; yoksa akılları mı bunu emrediyor, yoksa azgın bir topluluk mu; yoksa onu uydurdu mu diyorlar, hayır inanmıyorlar; doğruysalar benzeri bir söz getirsinler; yoksa hiçten mi yaratıldılar, yaratanlar kendileri mi; gökleri ve yeri onlar mı yarattı; Rabbinin hazineleri onlarda mı; dinledikleri bir merdivenleri mi var; kızlar O'nun, oğullar sizin mi; yoksa ücret istiyorsun da borç altında mı ezildiler",
 (41, 49): "sûre 52 (Tûr) beşinci ve son blok — yoksa gayb onlarda da onlar mı yazıyor; tuzak mı istiyorlar, tuzağa düşürülenler inkâr edenlerdir; Allah'tan başka ilâhları mı var, Allah ortak koştuklarından münezzehtir; gökten düşen parça görseler yığılmış bulut derler; onları çarpılacakları günlerine dek bırak, o gün tuzakları fayda vermez, yardım görmezler; zulmedenlere bundan başka azap da var; Rabbinin hükmüne sabret, sen gözlerimizin önündesin, kalktığında, gecede ve yıldızların çekilişinde Rabbini tesbih et",
}

SABLON = r'''# -*- coding: utf-8 -*-
"""blok_%(S)d_%(a)d_%(b)d.py — %(baslik)s

uret_blok_%(S)d.py tarafından ÜRETİLDİ — elle düzenleme. Ölçüm (›) defterden (olcum_bicim),
dikey (▽) blok_dikey JSON'undan, bilanço blok_bilanco'dan; yalnız meal ve mercek (◇) elle.
"""
import json, re, unicodedata
import olcum_bicim, gloss_gecis, blok_bilanco
from %(metin)s import MEAL, M
from %(kayit)s import CIPA, ARIZA

S, A1, A2 = %(S)d, %(a)d, %(b)d
REPO = '/home/claude/repo/notlar/'
DIK = json.load(open('blok_dikey_%%d_%%d_%%d.json' %% (S, A1, A2), encoding='utf-8'))
ESMA = json.load(open('esma_kayit.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {(s['no'], a['no']): a['ar'] for s in veri['sureler'] for a in s['ayetler']}
_H = re.compile('[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED]')
_isk = lambda w: _H.sub('', unicodedata.normalize('NFC', w)).replace('\u0671', '\u0627').replace('\ufeff', '')
BESMELE = [_isk(w) for w in AR[(1, 1)].split()[:4]]
if A1 == 1 and S not in (1, 9):
    _t = AR[(S, 1)].split()
    if [_isk(w) for w in _t[:4]] == BESMELE:
        AR[(S, 1)] = ' '.join(_t[4:])
    assert [_isk(w) for w in AR[(S, 1)].split()[:4]] != BESMELE, 'besmele ayıklanmadı — DUR'
for n in range(A1, A2 + 1):
    assert n in MEAL and n in M, 'meal/mercek eksik: %%d:%%d — DUR' %% (S, n)

p = REPO + 'okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
OM.setdefault(str(S), {})
for n in range(A1, A2 + 1):
    k = '%%d:%%d' %% (S, n)
    e = ESMA.get(k, {})
    OM[str(S)][k] = {"ar": AR[(S, n)], "meal": MEAL[n],
                     "olcum": olcum_bicim.olcum(S, n),
                     "mercek": M[n],
                     "dikey": DIK.get(k, "  · (ayette kök bulunmuyor — dikey satır yok)"),
                     "cipa": CIPA.get(n, dict(kademe=None, olgu=False, cipa=False)),
                     "esma": {x: e.get(x) for x in ('sinif_oto', 'sinif_el', 'e_oto', 'e_el', 'muhur', 'cift', 'ton', 'ton_kismi', 'bant')}}
    gloss_gecis.gecir_kayit(OM[str(S)][k])
bil = blok_bilanco.bilanco(S, A1, A2)
bil['ariza'] = ARIZA.get((A1, A2), [])
bil['cipa_L4'] = [n for n in range(A1, A2 + 1) if CIPA.get(n, {}).get('cipa')]
bil['tarayici_isabet'] = [a for a in bil['tarayici_v4_aday'] if CIPA.get(int(a.split(':')[1]), {}).get('cipa')]
OM[str(S)].setdefault('_bilanco', {})['%%d-%%d' %% (A1, A2)] = bil

# ilerleme — kayıttan koşulur (elle artırma YOK)
D = json.load(open('defter.json', encoding='utf-8'))
TAM = set(OM['ilerleme']['tam'])
assert S not in TAM, 'sûre %%d zaten TAM sayılıyor — çift sayım riski, DUR' %% S
oku_S = sorted(int(k.split(':')[1]) for k in OM[str(S)] if not k.startswith('_'))
OM['ilerleme']['kismi'][str(S)] = '%%d-%%d ayet düzeyinde (blok başı kayıt; %%d ayet)' %% (oku_S[0], oku_S[-1], len(oku_S))
# eski kural aynen korunur (secde_kapanis): TAM sûreler + 2:1-20; üstüne yalnız S'nin kayıtlı ayetleri
okunan = (sum(1 for r in D if r['k'][0] in TAM or (r['k'][0] == 2 and r['k'][1] <= 20))
          + sum(1 for r in D if r['k'][0] == S and r['k'][1] in set(oku_S)))
OM['ilerleme']['okunan_ayet'] = okunan
OM['ilerleme']['korpus_yuzde'] = round(100 * okunan / len(D), 1)
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

pm = REPO + 'mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
MK.setdefault(str(S), {})
for n in range(A1, A2 + 1):
    MK[str(S)]['%%d:%%d' %% (S, n)] = gloss_gecis.gecir(M[n])
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

print('blok %%d:%%d-%%d yazıldı · okuma_metni sûre %%d → %%d ayet · mercek_kayit → %%d · ilerleme %%d (%%%%%%s)'
      %% (S, A1, A2, S, len([k for k in OM[str(S)] if not k.startswith('_')]), len(MK[str(S)]),
         okunan, OM['ilerleme']['korpus_yuzde']))
print('kısmi:', OM['ilerleme']['kismi'])
'''

for a, b in BLOKLAR:
    ad = 'blok_%d_%d_%d.py' % (S, a, b)
    open(ad, 'w', encoding='utf-8').write(SABLON % dict(S=S, a=a, b=b, baslik=BASLIK[(a, b)], metin=METIN, kayit=KAYIT))
    print('üretildi:', ad)

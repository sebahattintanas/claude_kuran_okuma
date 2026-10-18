# -*- coding: utf-8 -*-
"""uret_blok_54.py — sûre 54 (Kamer) blok betiklerini üretir. BLOK BAŞINA KAYIT.

Değişiklik (2026-09-24): kayıt artık tur sonunu beklemiyor. Her blok betiği koşulduğunda
okuma_metni.json, mercek_kayit.json ve ilerleme o blok için yazılır; blok bilançosu (TAM SAYIM)
ve çıpa kararları da okuma_metni'ne yapılandırılmış alan olarak girer. Oturum yarıda kalsa da
okunmuş her blok kayıtlıdır.

Sûre numarası TEK değişkende (S). olcum_bicim.olcum(S, n), AR[(S, n)], OM[str(S)] hep S'den
türer — üç kez atlanan elle-değiştirme hatası (tur sonu notu) burada yapısal olarak kapalı.
Besmele korpustan (1:1'in ilk dört kelimesinin iskeleti) ayıklanır; Arapça sabit yok.
"""
import sys
S = 54
METIN = 'kamer_metin_1'
KAYIT = 'kamer_kayit'
# blok başı kayıt: blok okundukça listeye eklenir (başlık okuma sonrası yazılır)
BLOKLAR = [(1, 10), (11, 20), (21, 30), (31, 40), (41, 50), (51, 55)]
BASLIK = {
 (1, 10): "sûre 54 (Kamer) birinci blok — saat yaklaştı, ay yarıldı; bir işaret görseler yüz çevirip süregelen büyü derler; yalanladılar, heveslerine uydular, her iş yerine oturmuştur; içinde caydırma olan haberler, ulaşmış bir hikmet geldi, uyarılar fayda vermiyor; onlardan yüz çevir; çağıranın çağıracağı gün gözleri düşük, yayılmış çekirgeler gibi kabirlerden çıkarlar; onlardan önce Nûh kavmi yalanladı, kulumuza deli dediler; o Rabbine yenik düştüm, yardım et diye seslendi",
 (11, 20): "sûre 54 (Kamer) ikinci blok — göğün kapılarını boşanan suyla açtık, yeri pınarlarla fışkırttık, sular takdir edilmiş bir iş üzerine buluştu; onu tahtalardan ve çivilerden olan üzerinde taşıdık, gözlerimizin önünde akıyordu; onu bir işaret olarak bıraktık, öğüt alan var mı; azabım ve uyarılarım nasılmış; Kur'ân'ı öğüt için kolaylaştırdık; Âd yalanladı; uğursuz bir günde uğultulu bir rüzgâr gönderdik, insanları sökülmüş hurma kütükleri gibi koparıyordu",
 (21, 30): "sûre 54 (Kamer) üçüncü blok — azabım ve uyarılarım nasılmış; Kur'ân'ı öğüt için kolaylaştırdık; Semûd uyarıları yalanladı, içimizden tek bir insana mı uyacağız dediler, zikir aramızdan ona mı bırakıldı, o yalancı, şımarık; yarın kimin yalancı olduğunu bilecekler; dişi deveyi onlara sınama olarak gönderiyoruz, gözetle ve sabret; su aralarında paylaştırılmıştır; arkadaşlarına seslendiler, o girişti ve kesti; azabım ve uyarılarım nasılmış",
 (31, 40): "sûre 54 (Kamer) dördüncü blok — onların üzerine tek bir çığlık gönderdik, ağıl yapanın kuru çer çöpü gibi oldular; Kur'ân'ı öğüt için kolaylaştırdık; Lût kavmi uyarıları yalanladı; taş savuran bir rüzgâr gönderdik, Lût ailesini seher vakti kurtardık, katımızdan bir nimet olarak; o onları uyarmıştı, kuşkuya düştüler; konuklarından ayartmak istediler, gözlerini sildik; sabah erkenden yerleşik bir azap bastı; tadın azabımı ve uyarılarımı",
 (41, 50): "sûre 54 (Kamer) beşinci blok — Firavun ailesine uyarılar geldi, âyetlerimizin hepsini yalanladılar, onları üstün ve güç yetiren birinin yakalayışıyla yakaladık; sizin kâfirleriniz onlardan daha mı hayırlı, yoksa kitaplarda bir aklanma mı var; biz hep birlikte üstün geleceğiz mi diyorlar; o topluluk bozguna uğratılacak, arka dönecekler; asıl vaat edilen vakit Saattir, daha belâlı ve acıdır; suçlular sapıklık ve çılgınlık içinde, yüzüstü ateşte sürüklenecekler; her şeyi bir ölçüyle yarattık; emrimiz bir tektir, göz kırpışı gibi",
 (51, 55): "sûre 54 (Kamer) altıncı ve son blok — sizin benzerlerinizi helâk ettik, öğüt alan var mı; yaptıkları her şey kitaplardadır, küçük büyük her şey satır satır yazılmıştır; sakınanlar cennetlerde ve ırmak içinde, güç yetiren bir hükümdarın katında doğruluk oturağındadır",
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

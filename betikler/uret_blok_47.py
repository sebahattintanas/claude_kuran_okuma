# -*- coding: utf-8 -*-
"""uret_blok_47.py — sûre 47 (Muhammed) blok betiklerini üretir. BLOK BAŞINA KAYIT.

Değişiklik (2026-09-24): kayıt artık tur sonunu beklemiyor. Her blok betiği koşulduğunda
okuma_metni.json, mercek_kayit.json ve ilerleme o blok için yazılır; blok bilançosu (TAM SAYIM)
ve çıpa kararları da okuma_metni'ne yapılandırılmış alan olarak girer. Oturum yarıda kalsa da
okunmuş her blok kayıtlıdır.

Sûre numarası TEK değişkende (S). olcum_bicim.olcum(S, n), AR[(S, n)], OM[str(S)] hep S'den
türer — üç kez atlanan elle-değiştirme hatası (tur sonu notu) burada yapısal olarak kapalı.
Besmele korpustan (1:1'in ilk dört kelimesinin iskeleti) ayıklanır; Arapça sabit yok.
"""
import sys
S = 47
METIN = 'muhammed_metin_1'
KAYIT = 'muhammed_kayit'
# blok başı kayıt: blok okundukça listeye eklenir (başlık okuma sonrası yazılır)
BLOKLAR = [(1, 10), (11, 20), (21, 30), (31, 38)]
BASLIK = {
 (1, 10): "sûre 47 (Muhammed) birinci blok — inkâr edip Allah yolundan alıkoyanların işlerini boşa çıkardı; inanıp salih iş yapan ve Muhammed'e indirilene inananların kötülüklerini örttü, hâllerini düzeltti; bu, birinin bâtıla, ötekinin Rablerinden gelen hakka uymasındandır; inkâr edenlerle karşılaşınca boyunlarını vurun, sonra ya karşılıksız bırakma ya fidye, savaş yüklerini bırakıncaya kadar; Allah yolunda öldürülenlerin işlerini boşa çıkarmayacak, onları cennete sokacak; Allah'a yardım ederseniz size yardım eder; inkâr edenlere yıkım; indirileni hoş görmediler; yeryüzünde gezip öncekilerin sonuna bakmadılar mı",
 (11, 20): "sûre 47 (Muhammed) ikinci blok — Allah inananların mevlâsıdır, inkâr edenlerin mevlâsı yoktur; Allah inananları altından ırmaklar akan cennetlere sokar, inkâr edenler hayvanlar gibi yer, ateş onların barınağıdır; seni çıkaran kasabandan güçlü nice kasabayı helâk ettik; Rabbinden açık delil üzere olan, kötü işi süslü gösterilen gibi midir; sakınanlara vaat edilen cennetin örneği: bozulmayan su, tadı değişmeyen süt, şarap ve süzülmüş bal ırmakları — ateşte kalıp kaynar su içirilen gibi mi; seni dinleyip 'az önce ne dedi' diyenler; doğru yolu bulanların hidayeti artırıldı; kıyameti mi bekliyorlar, alametleri geldi; bil ki Allah'tan başka ilâh yoktur, bağışlanma dile; sûre indirilip savaş anılınca kalplerinde hastalık olanların ölüm baygınlığındaki bakışı",
 (21, 30): "sûre 47 (Muhammed) üçüncü blok — itaat ve güzel söz; iş kesinleşince Allah'a sadık olsalardı; yüz çevirirseniz yeryüzünde bozgunculuk yapıp akrabalığı mı koparacaksınız; Allah'ın lânet edip sağır ve kör ettikleri; Kur'ân'ı düşünmüyorlar mı, yoksa kalplerde kilitler mi var; hidayet belli olduktan sonra arkalarına dönenlere şeytan süslü gösterdi; indirileni hoş görmeyenlere 'bazı işlerde size uyacağız' dediler, Allah gizlediklerini bilir; melekler yüzlerine ve arkalarına vurarak canlarını alınca; Allah'ı öfkelendirene uydular, hoşnutluğunu hoş görmediler; kalplerinde hastalık olanlar Allah'ın kinlerini çıkarmayacağını mı sandı; dileseydik onları sana gösterirdik, sözün eğiliminden tanırsın",
 (31, 38): "sûre 47 (Muhammed) dördüncü ve son blok — cihad edenleri ve sabredenleri belirleyinceye kadar sizi sınayacağız; inkâr edip Allah yolundan alıkoyan ve Elçi'ye karşı çıkanlar Allah'a zarar veremez, işlerini boşa çıkaracak; Allah'a ve Elçi'ye itaat edin, işlerinizi boşa çıkarmayın; inkârcı olarak ölenleri Allah bağışlamaz; gevşemeyin, üstünken barışa çağırmayın, Allah sizinle, işlerinizi eksiltmez; dünya hayatı oyun ve oyalanma, mallarınızı istemez; isteseydi cimrilik ederdiniz, kinleriniz çıkardı; Allah yolunda harcamaya çağrılıyorsunuz, cimrilik eden kendine eder; Allah zengin, siz yoksulsunuz; yüz çevirirseniz yerinize sizin gibi olmayan bir topluluk getirir",
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

# -*- coding: utf-8 -*-
"""uret_blok_2.py — sûre 2 (Bakara) blok betiklerini üretir. BLOK BAŞINA KAYIT.

Değişiklik (2026-09-24): kayıt artık tur sonunu beklemiyor. Her blok betiği koşulduğunda
okuma_metni.json, mercek_kayit.json ve ilerleme o blok için yazılır; blok bilançosu (TAM SAYIM)
ve çıpa kararları da okuma_metni'ne yapılandırılmış alan olarak girer. Oturum yarıda kalsa da
okunmuş her blok kayıtlıdır.

Sûre numarası TEK değişkende (S). olcum_bicim.olcum(S, n), AR[(S, n)], OM[str(S)] hep S'den
türer — üç kez atlanan elle-değiştirme hatası (tur sonu notu) burada yapısal olarak kapalı.
Besmele korpustan (1:1'in ilk dört kelimesinin iskeleti) ayıklanır; Arapça sabit yok.
"""
import sys
S = 2
METIN = 'bakara_metin_1'
KAYIT = 'bakara_kayit'
# blok başı kayıt: blok okundukça listeye eklenir (başlık okuma sonrası yazılır)
BLOKLAR = [(21, 25), (26, 29), (30, 33), (34, 39), (40, 46), (47, 53), (54, 59), (60, 61), (62, 66), (67, 70), (71, 74), (75, 79)]
BASLIK = {
 (21, 25): "2:21-25 — ey insanlar, sizi yaratan Rabbinize kulluk edin; yeri döşek, göğü bina kılan O'dur; kulumuza indirdiğimizden şüphedeyseniz benzerinden bir sûre getirin; yapamazsanız yakıtı insanlar ve taşlar olan ateşten sakının; inanıp iyi işler yapanlara altlarından ırmaklar akan bahçeleri müjdele",
 (26, 29): "2:26-29 — Allah sivrisineği ve üstündekini misal vermekten çekinmez; inananlar onun hak olduğunu bilir, inkâr edenler ne demek istedi der; ahdi bozanlar, emredileni kesenler kaybedenlerdir; ölüydünüz diriltti, öldürecek, diriltecek, O'na döndürüleceksiniz; yerdekilerin hepsini sizin için yarattı, göğe yöneldi, yedi gök olarak düzenledi",
 (30, 33): "2:30-33 — Rabbin meleklere yeryüzünde bir halife kılacağım dedi; orada bozgunculuk yapacak birini mi dediler; ben sizin bilmediğinizi bilirim dedi; Âdem'e isimlerin hepsini öğretti, meleklere sundu; bize öğrettiğinden başka bilgimiz yok dediler; ey Âdem onlara isimlerini bildir; göklerin ve yerin gaybını bilirim dememiş miydim",
 (34, 39): "2:34-39 — meleklere Âdem'e secde edin dedik, İblîs dışında secde ettiler; ey Âdem sen ve eşin bahçede oturun, şu ağaca yaklaşmayın; şeytan onları kaydırıp çıkardı, inin dedik; Âdem Rabbinden kelimeler aldı, O tevbesini kabul etti; benden yol gösterici gelirse ona uyanlara korku yok; inkâr edip yalanlayanlar ateşin halkıdır",
 (40, 46): "2:40-46 — ey İsrâiloğulları nimetimi anın, ahdimi yerine getirin, yalnız benden korkun; indirdiğime iman edin, âyetlerimi az bedele satmayın; hakkı bâtılla karıştırmayın; namazı kılın, zekâtı verin, rükû edin; insanlara iyiliği emredip kendinizi unutuyor musunuz; sabır ve namazla yardım isteyin; onlar Rablerine kavuşacaklarını düşünürler",
 (47, 53): "2:47-53 — ey İsrâiloğulları nimetimi ve sizi âlemlere üstün kıldığımı anın; kimsenin kimse yerine bir şey ödeyemeyeceği günden sakının; sizi Firavun ailesinden kurtardık; denizi yardık, Firavun ailesini boğduk; Mûsâ ile kırk gece sözleştik, buzağıyı edindiniz; sizi bağışladık; Mûsâ'ya Kitabı ve furkanı verdik",
 (54, 59): "2:54-59 — Mûsâ kavmine: buzağıyla kendinize zulmettiniz, yaratanınıza tevbe edin; Allah'ı açıkça görmedikçe inanmayız dediniz, yıldırım sizi yakaladı; ölümünüzden sonra sizi dirilttik; bulutu gölge yaptık, helva ve bıldırcın indirdik; bu kasabaya girin, hitta deyin; zulmedenler sözü değiştirdi, gökten azap indirdik",
 (60, 61): "2:60-61 — Mûsâ kavmi için su istedi, asânla taşa vur dedik, on iki pınar fışkırdı; tek yiyeceğe katlanamayız, Rabbine dua et de yerin bitirdiklerinden çıkarsın dediniz; bir şehre inin; üzerlerine aşağılık ve yoksulluk vuruldu",
 (62, 66): "2:62-66 — iman edenler, Yahudiler, Hıristiyanlar, Sâbiîler — Allah'a ve âhiret gününe inanıp iyi iş yapanlara ödül; sizden söz aldık, Tûr'u üstünüze kaldırdık; sonra yüz çevirdiniz; Sebt'te sınırı aşanlara maymun olun dedik; bunu ibret ve öğüt kıldık",
 (67, 70): "2:67-70 — Mûsâ kavmine Allah bir inek boğazlamanızı emrediyor dedi; Rabbine dua et de ne olduğunu açıklasın dediler — ne yaşlı ne genç, orta yaşlı; rengi parlak sarı, bakanlara sevinç veren; sığırlar bize benzer göründü, Allah dilerse doğru yolu buluruz",
 (71, 74): "2:71-74 — 2:71-74 — yeri sürmeyen, ekini sulamayan, kusursuz, alacasız bir inek; şimdi gerçeği getirdin dediler ve boğazladılar; bir kişiyi öldürmüş, onun hakkında tartışmıştınız; bir parçasıyla ona vurun — Allah ölüleri böyle diriltir; sonra kalpleriniz taş gibi, daha da katı oldu; taşlardan ırmak fışkıranı, yarılıp su çıkanı, Allah korkusundan düşeni var",
 (75, 79): "2:75-79 — 2:75-79 — size inanacaklarını mı umuyorsunuz, içlerinden bir grup Allah'ın sözünü işitip anladıktan sonra değiştirirdi; inananlarla karşılaşınca inandık der, baş başa kalınca Allah'ın size açtığını onlara mı anlatıyorsunuz derler; Allah gizlediklerini ve açığa vurduklarını bilir; ümmîler kitabı bilmez, yalnız kuruntu ve zan; kitabı elleriyle yazıp bu Allah katındandır diyenlere vay",
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
OM_ONCE = set(OM[str(S)])
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
# SÛRE 2 ONARIMI (iskele_2): S'nin kayıtlı ayetleri 'S:A' ve eski birleşik 'S:A-B' anahtarlarından
# (eski kayıt 1-20: iki birleşik anahtar). 'A-B' biçimli eski blok özeti anahtarları okuma SAYILMAZ.
# 2:1-20 bu kümenin içinde olduğu için ayrıca eklenmez — çift sayım yok (şablonun 2:1-20 terimi kaldırıldı).
oku_S = set()
for k in OM[str(S)]:
    m = re.fullmatch(r'%%d:(\d+)(?:-(\d+))?' %% S, k)
    if m:
        oku_S.update(range(int(m.group(1)), int(m.group(2) or m.group(1)) + 1))
oku_S = sorted(oku_S)
assert oku_S == list(range(1, oku_S[-1] + 1)), 'sûre %%d kayıtlı ayetleri kesintili — DUR' %% S
OM['ilerleme']['kismi'][str(S)] = '1-%%d ayet düzeyinde (1-20 eski kayıt + 21-%%d blok başı kayıt; %%d ayet)' %% (oku_S[-1], oku_S[-1], len(oku_S))
okunan = (sum(1 for r in D if r['k'][0] in TAM)
          + sum(1 for r in D if r['k'][0] == S and r['k'][1] in set(oku_S)))
OM['ilerleme']['okunan_ayet'] = okunan
OM['ilerleme']['korpus_yuzde'] = round(100 * okunan / len(D), 1)
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

pm = REPO + 'mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
MK.setdefault(str(S), {})
# SÛRE 2: mercek_kayit['2']'de eski sıkıştırılmış ◇ notları var (2:22, 2:24 …). Üstüne yazmadan önce
# '_sikistirilmis_eski' altına bir kez arşivlenir (blok ilk kez yazılırken; yeniden koşuda arşivlenmez).
for n in range(A1, A2 + 1):
    k = '%%d:%%d' %% (S, n)
    if k not in OM_ONCE and k in MK[str(S)]:
        MK[str(S)].setdefault('_sikistirilmis_eski', {}).setdefault(k, MK[str(S)][k])
    MK[str(S)][k] = gloss_gecis.gecir(M[n])
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

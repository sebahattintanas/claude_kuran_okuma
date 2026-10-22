# -*- coding: utf-8 -*-
"""uret_blok_57.py — sûre 57 (Hadîd) blok betiklerini üretir. BLOK BAŞINA KAYIT.

Değişiklik (2026-09-24): kayıt artık tur sonunu beklemiyor. Her blok betiği koşulduğunda
okuma_metni.json, mercek_kayit.json ve ilerleme o blok için yazılır; blok bilançosu (TAM SAYIM)
ve çıpa kararları da okuma_metni'ne yapılandırılmış alan olarak girer. Oturum yarıda kalsa da
okunmuş her blok kayıtlıdır.

Sûre numarası TEK değişkende (S). olcum_bicim.olcum(S, n), AR[(S, n)], OM[str(S)] hep S'den
türer — üç kez atlanan elle-değiştirme hatası (tur sonu notu) burada yapısal olarak kapalı.
Besmele korpustan (1:1'in ilk dört kelimesinin iskeleti) ayıklanır; Arapça sabit yok.
"""
import sys
S = 57
METIN = 'hadid_metin_1'
KAYIT = 'hadid_kayit'
# blok başı kayıt: blok okundukça listeye eklenir (başlık okuma sonrası yazılır)
BLOKLAR = [(1, 6), (7, 10), (11, 15), (16, 19), (20, 22), (23, 26), (27, 29)]
BASLIK = {
 (1, 6): "sûre 57 (Hadîd) birinci blok — göklerde ve yerde ne varsa Allah'ı tesbih etti; göklerin ve yerin mülkü O'nun, diriltir ve öldürür; O ilk ve son, zâhir ve bâtın; gökleri ve yeri altı günde yarattı, sonra Arş'a istivâ etti; yere gireni, gökten ineni bilir, nerede olursanız sizinle; işler Allah'a döndürülür; geceyi gündüze, gündüzü geceye katar",
 (7, 10): "sûre 57 (Hadîd) ikinci blok — Allah'a ve elçisine iman edin, halef kılındığınız şeylerden harcayın; size ne oluyor ki iman etmiyorsunuz, elçi sizi Rabbinize çağırıyor; kuluna apaçık âyetler indiren O, sizi karanlıklardan aydınlığa çıkarmak için; size ne oluyor ki Allah yolunda harcamıyorsunuz, göklerin ve yerin mirası Allah'ın; fetihten önce harcayıp savaşanlar derece bakımından daha büyük; hepsine en güzeli vaat edildi",
 (11, 15): "sûre 57 (Hadîd) üçüncü blok — kim Allah'a güzel bir borç verir ki kat kat artırılsın; o gün inanan erkek ve kadınların ışığı önlerinde ve sağlarında koşar, müjdeleri cennetlerdir; münafık erkek ve kadınlar ışıktan pay ister, 'arkanıza dönün' denir, aralarına kapılı bir sur çekilir, içi rahmet dışı azap; 'sizinle değil miydik' — 'evet ama kendinizi fitneye düşürdünüz'; bugün fidye alınmaz, barınağınız ateş",
 (16, 19): "sûre 57 (Hadîd) dördüncü blok — inananların kalplerinin Allah'ı anmaya boyun eğme vakti gelmedi mi, önce kitap verilenler gibi olmasınlar, zaman uzadı ve kalpleri katılaştı; bilin ki Allah yeri ölümünden sonra diriltir; sadaka veren erkekler ve kadınlar, Allah'a güzel borç verenler — kat kat artırılır; Allah'a ve elçilerine inananlar sıddîklardır, inkâr edip yalanlayanlar cehennemliklerdir",
 (20, 22): "sûre 57 (Hadîd) beşinci blok — dünya hayatı oyun, eğlence, süs, övünme ve mal-evlat yarışı; bitkisi hoşa giden yağmur gibi, sonra kurur, sararır, çer çöp olur; âhirette azap, bağışlanma ve hoşnutluk; Rabbinizden bağışlanmaya ve gök ile yer genişliğinde cennete koşuşun; yerde ve canlarınızda uğrayan her musibet yaratılmadan önce bir kitaptadır",
 (23, 26): "sûre 57 (Hadîd) altıncı blok — kaybedilene üzülmeyesiniz, verilene şımarmayasınız diye; Allah böbürleneni sevmez; cimrilik edip cimriliği emredenler — Allah zengindir, övülendir; elçileri apaçık delillerle gönderdik, kitabı ve ölçüyü indirdik, demiri indirdik, onda çetin güç ve yararlar var; Nûh'u ve İbrâhîm'i gönderdik, soylarında peygamberlik ve kitap",
 (27, 29): "sûre 57 (Hadîd) yedinci ve son blok — izleri üzerine elçilerimizi, Meryem oğlu Îsâ'yı art arda gönderdik, ona İncîl'i verdik, uyanların kalplerine şefkat ve merhamet koyduk, ruhbanlığı uydurdular; ey inananlar, Allah'tan sakının, elçisine inanın, rahmetinden iki pay ve yürüyeceğiniz bir ışık; lütuf Allah'ın elindedir, dilediğine verir",
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

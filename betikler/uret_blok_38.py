# -*- coding: utf-8 -*-
"""uret_blok_38.py — sûre 38 (Sâd) blok betiklerini üretir. BLOK BAŞINA KAYIT.

Değişiklik (2026-09-24): kayıt artık tur sonunu beklemiyor. Her blok betiği koşulduğunda
okuma_metni.json, mercek_kayit.json ve ilerleme o blok için yazılır; blok bilançosu (TAM SAYIM)
ve çıpa kararları da okuma_metni'ne yapılandırılmış alan olarak girer. Oturum yarıda kalsa da
okunmuş her blok kayıtlıdır.

Sûre numarası TEK değişkende (S). olcum_bicim.olcum(S, n), AR[(S, n)], OM[str(S)] hep S'den
türer — üç kez atlanan elle-değiştirme hatası (tur sonu notu) burada yapısal olarak kapalı.
Besmele korpustan (1:1'in ilk dört kelimesinin iskeleti) ayıklanır; Arapça sabit yok.
"""
import sys
S = 38
METIN = 'sad_metin_1'
KAYIT = 'sad_kayit'
# blok başı kayıt: blok okundukça listeye eklenir (başlık okuma sonrası yazılır)
BLOKLAR = [(1, 10), (11, 20), (21, 30), (31, 40), (41, 50), (51, 60), (61, 70), (71, 80), (81, 88)]
BASLIK = {
 (1, 10): "sûre 38 (Sâd) birinci blok — tek harf ve zikir sahibi Kur'ân'a yemin; inkârcıların büyüklenmesi ve ayrılığı, helâk edilen nesillerin vakitsiz feryadı; içlerinden uyarıcıya şaşma: 'yalancı büyücü, ilâhları tek ilâh mı yaptı'; ileri gelenlerin 'ilâhlarınıza sabredin', 'son dinde işitmedik, uydurma'; 'zikir ona mı indirildi' — benim zikrimden şüphedeler; Rabbinin rahmet hazineleri ve göklerin mülkü onların mı?",
 (11, 20): "sûre 38 (Sâd) ikinci blok — hiziplerden bozguna uğrayacak önemsiz bir ordu; önceden yalanlayanlar: Nûh kavmi, Âd, kazıklar sahibi Firavun, Semûd, Lût kavmi, Eyke halkı — 'cezam hak oldu'; tek bir çığlığı bekleyenler ve 'Rabbimiz, payımızı acele ver'; 'söylediklerine sabret, güç sahibi kulumuz Dâvûd'u an': onunla tesbih eden dağlar, toplanmış kuşlar, güçlendirilen mülk, hikmet ve faslu'l-hıtâb",
 (21, 30): "sûre 38 (Sâd) üçüncü blok — mihraba duvardan giren iki davacı: doksan dokuz koyun ve bir koyun; Dâvûd'un hükmü, 'ortakların çoğu birbirine haksızlık eder'; sınandığını anlayan Dâvûd'un istiğfarı, secdesi ve bağışlanması; 'ey Dâvûd, seni yeryüzünde halife kıldık, hakla hükmet, hevâya uyma'; gök ve yer boşuna yaratılmadı; müminler bozguncularla bir mi; düşünülsün diye indirilen bereketli kitap; Dâvûd'a bağışlanan Süleymân",
 (31, 40): "sûre 38 (Sâd) dördüncü blok — akşamüstü Süleymân'a sunulan asil atlar; 'hayır sevgisini Rabbimi anmaktan sevdim', perdenin ardına gizlenen; atları geri getirtip bacaklarını ve boyunlarını sıvazlama; Süleymân'ın sınanması, tahtına bırakılan ceset ve inâbesi; 'Rabbim, beni bağışla, bana kimseye yakışmayacak bir mülk ver, sen Vehhâb'sın'; emriyle yumuşak esen rüzgâr, yapıcı ve dalgıç şeytanlar, zincirdekiler; 'bu bizim bağışımız, hesapsız'; katımızda yakınlık ve güzel dönüş",
 (41, 50): "sûre 38 (Sâd) beşinci blok — 'kulumuz Eyyûb'u an': şeytanın dokundurduğu yorgunluk ve azap; 'ayağını vur, işte serin yıkanma suyu ve içecek'; ailesi ve bir misli bağışlanıyor; demet ve yemin; 'onu sabırlı bulduk, ne güzel kul, evvâb'; güç ve basiret sahibi İbrâhîm, İshâk, Ya'kûb — yurdu anmakla arıtılmış seçkinler; İsmâîl, Elyesa, Zü'l-Kifl; 'bu bir zikirdir': sakınanlara güzel dönüş, kapıları açık Adn cennetleri",
 (51, 60): "sûre 38 (Sâd) altıncı blok — Adn cennetlerinde yaslanıp bol meyve ve içecek isteyenler, bakışını sınırlayan yaşıtlar; 'hesap günü için size vaat edilen bu, tükenmeyen rızkımız'; azgınlara kötü dönüş: cehennem, kötü döşek, kaynar su ve irin ve onun türünden çeşitler; dalıp giren kalabalığa 'merhaba yok' ve karşılığı 'asıl size merhaba yok, bunu bize siz hazırladınız'",
 (61, 70): "sûre 38 (Sâd) yedinci blok — 'Rabbimiz, bunu bize hazırlayanın azabını kat kat artır'; kötülerden saydıkları adamları göremeyenler: alay mı ettik, gözler mi kaydı; ateş ehlinin çekişmesi gerçektir; 'de ki: ben ancak uyarıcıyım; tek ve kahhâr Allah'tan başka ilâh yok, göklerin, yerin ve arasındakilerin Rabbi, azîz, ğaffâr'; büyük haber ve ondan yüz çevirenler; yüce topluluğun tartışması; 'bana ancak apaçık uyarıcı olduğum vahyediliyor'",
 (71, 80): "sûre 38 (Sâd) sekizinci blok — Rabbin meleklere 'çamurdan bir beşer yaratacağım; düzenleyip ruhumdan üflediğimde secdeye kapanın'; meleklerin hepsi secde etti, İblîs büyüklendi; 'iki elimle yarattığıma secdeden seni ne alıkoydu' — 'ben ondan hayırlıyım, beni ateşten, onu çamurdan yarattın'; 'çık oradan, kovulmuşsun, din gününe kadar lânetim üzerinde'; 'Rabbim, diriltilecekleri güne kadar mühlet ver' — 'sen mühlet verilenlerdensin'",
 (81, 88): "sûre 38 (Sâd) son blok — bilinen vaktin gününe kadar; İblîs'in yemini: 'izzetine andolsun, ihlâsa erdirilmiş kulların hariç hepsini azdıracağım'; 'hak budur, hakkı söylerim: cehennemi senden ve sana uyanlardan dolduracağım'; 'de ki: ücret istemiyorum, yükümlülük uyduranlardan değilim; o âlemler için bir zikirdir; haberini bir süre sonra bileceksiniz'",
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

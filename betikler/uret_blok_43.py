# -*- coding: utf-8 -*-
"""uret_blok_43.py — sûre 43 (Zuhruf) blok betiklerini üretir. BLOK BAŞINA KAYIT.

Değişiklik (2026-09-24): kayıt artık tur sonunu beklemiyor. Her blok betiği koşulduğunda
okuma_metni.json, mercek_kayit.json ve ilerleme o blok için yazılır; blok bilançosu (TAM SAYIM)
ve çıpa kararları da okuma_metni'ne yapılandırılmış alan olarak girer. Oturum yarıda kalsa da
okunmuş her blok kayıtlıdır.

Sûre numarası TEK değişkende (S). olcum_bicim.olcum(S, n), AR[(S, n)], OM[str(S)] hep S'den
türer — üç kez atlanan elle-değiştirme hatası (tur sonu notu) burada yapısal olarak kapalı.
Besmele korpustan (1:1'in ilk dört kelimesinin iskeleti) ayıklanır; Arapça sabit yok.
"""
import sys
S = 43
METIN = 'zuhruf_metin_1'
KAYIT = 'zuhruf_kayit'
# blok başı kayıt: blok okundukça listeye eklenir (başlık okuma sonrası yazılır)
BLOKLAR = [(1, 10), (11, 20), (21, 30), (31, 40), (41, 50), (51, 60), (61, 70), (71, 80), (81, 89)]
BASLIK = {
 (1, 10): "sûre 43 (Zuhruf) birinci blok — Hâ Mîm; apaçık Kitab'a yemin; onu akıl erdiresiniz diye Arapça bir Kur'an kıldık; o katımızdaki Ana Kitap'ta yücedir, hikmetlidir; aşırı gidiyorsunuz diye Zikr'i sizden çevirip bırakacak mıyız; öncekilere nice peygamber gönderildi, gelen her peygamberle alay ettiler; onlardan daha çetinleri helâk edildi, öncekilerin örneği geçti; gökleri ve yeri kim yarattı diye sorsan 'Azîz, Alîm yarattı' derler; yeri size döşek kılıp orada yollar açan",
 (11, 20): "sûre 43 (Zuhruf) ikinci blok — gökten ölçüyle su indirip ölü beldeyi dirilten, siz de böyle çıkarılacaksınız; bütün çiftleri yaratan, gemileri ve davarları binek kılan; üzerlerine yerleşince Rabbin nimetini anıp 'bunu bize boyun eğdiren münezzehtir, biz Rabbimize döneceğiz' demeniz için; O'na kullarından bir parça yakıştırdılar, insan apaçık nankör; kızları O'na, oğulları size mi; biri kızla müjdelenince yüzü kararır; süs içinde yetiştirilen, tartışmada açık konuşamayan; Rahmân'ın kulları melekleri dişi saydılar, yaratılışlarına tanık mı oldular; 'Rahmân dileseydi onlara kulluk etmezdik' — bilgileri yok, tahmin yürütüyorlar",
 (21, 30): "sûre 43 (Zuhruf) üçüncü blok — önceden verilmiş bir kitaba mı tutunuyorlar; hayır, 'atalarımızı bir yol üzere bulduk, izlerinden doğru yolu buluyoruz' dediler; senden önce her kasabanın şımarmışları da 'izlerine uyuyoruz' dedi; 'daha doğrusunu getirsem de mi?' — 'sizinle gönderileni inkâr ediyoruz'; öç alındı, yalanlayanların sonuna bak; İbrâhîm babasına ve kavmine: 'kulluk ettiklerinizden uzağım, beni yaratan hariç, O beni doğru yola iletecek'; onu ardından gelenlerde kalıcı söz kıldı; bunları ve atalarını hak ve apaçık elçi gelinceye dek yararlandırdım; hak gelince 'bu büyü' dediler",
 (31, 40): "sûre 43 (Zuhruf) dördüncü blok — 'bu Kur'an iki kasabadan büyük bir adama indirilmeli değil miydi'; Rabbinin rahmetini onlar mı paylaştırıyor, geçimi biz paylaştırdık, kimini kiminden derecelerle üstün kıldık; insanlar tek ümmet olmayacak olsa inkârcıların evlerine gümüş tavanlar, merdivenler, kapılar, tahtlar ve altın süsler — hepsi dünya hayatının geçimliği, âhiret sakınanlar için; Rahmân'ın zikrinden göz yumana bir şeytan arkadaş musallat edilir, yoldan alıkoyar, doğru yolda sanırlar; huzura gelince 'keşke aramızda iki doğu arası olsaydı, ne kötü arkadaş'; bugün azapta ortaklığınız fayda vermez; sağırlara sen mi işittireceksin",
 (41, 50): "sûre 43 (Zuhruf) beşinci blok — seni götürsek de onlardan öç alırız, vaat ettiğimizi sana göstersek de onlara güç yetiririz; sana vahyolunana tutun, dosdoğru yoldasın; o sana ve kavmine bir zikir, sorguya çekileceksiniz; önceki elçilere sor, Rahmân'dan başka kulluk edilecek ilâhlar kıldık mı; Mûsâ âyetlerle Firavun'a ve ileri gelenlerine gönderildi: 'âlemlerin Rabbinin elçisiyim'; âyetlere güldüler; her âyet kardeşinden büyüktü, dönsünler diye azapla yakalandılar; 'ey sihirbaz, Rabbine dua et, doğru yolu bulacağız'; azap kalkınca sözlerinden döndüler",
 (51, 60): "sûre 43 (Zuhruf) altıncı blok — Firavun kavmine seslendi: 'Mısır'ın mülkü benim değil mi, ırmaklar altımdan akıyor; ben şu hor ve derdini anlatamayandan hayırlı değil miyim; ona altın bilezikler atılmalı ya da yanında melekler gelmeli değil miydi'; kavmini hafife aldı, boyun eğdiler, yoldan çıkmış bir kavimdi; bizi öfkelendirince öç alındı, hepsi boğuldu, sonrakilere örnek kılındı; Meryem oğlu örnek getirilince kavmin gürültü kopardı: 'ilâhlarımız mı hayırlı o mu' — tartışmak için; o yalnızca nimet verilen, İsrâiloğullarına örnek kılınan bir kul; dileseydik yeryüzünde yerinize geçecek melekler var ederdik",
 (61, 70): "sûre 43 (Zuhruf) yedinci blok — o, saat için bir bilgidir, ondan şüphe etmeyin, bana uyun, bu dosdoğru yol; şeytan sizi alıkoymasın, apaçık düşmanınızdır; Îsâ apaçık kanıtlarla gelince: 'size hikmetle geldim, ayrılığa düştüğünüzün bir kısmını açıklayacağım; Allah'tan sakının, bana itaat edin; Allah benim de Rabbim sizin de Rabbiniz, O'na kulluk edin'; gruplar ayrılığa düştü, zulmedenlere acı günün azabından vay; ansızın gelecek saati mi bekliyorlar; o gün dostlar birbirine düşman, sakınanlar hariç; 'ey kullarım, bugün size korku yok'; âyetlerimize inanıp teslim olanlar; girin cennete, siz ve eşleriniz, sevindirileceksiniz",
 (71, 80): "sûre 43 (Zuhruf) sekizinci blok — etraflarında altın tepsiler ve kadehlerle dolaşılır, canların çektiği ve gözlerin hoşlandığı orada, siz orada ebedîsiniz; yaptıklarınıza karşılık miras kılınan cennet; orada bol meyve; suçlular cehennem azabında ebedî, azap hafifletilmez, ümitsizler; biz zulmetmedik, zalimler kendileriydi; 'ey Mâlik, Rabbin işimizi bitirsin' — 'kalacaksınız'; size hakkı getirdik, çoğunuz haktan hoşlanmıyordu; bir işe mi karar verdiler, biz de karar verenleriz; gizlediklerini ve fısıltılarını işitmediğimizi mi sanıyorlar, elçilerimiz yanlarında yazıyor",
 (81, 89): "sûre 43 (Zuhruf) dokuzuncu ve son blok — de ki: Rahmân'ın çocuğu olsaydı kulluk edenlerin ilki ben olurdum; göklerin, yerin ve Arş'ın Rabbi nitelendirmelerinden uzak; bırak onları, vaat edilen günlerine kavuşuncaya dek dalsınlar, oynasınlar; gökte de yerde de ilâh olan O, Hakîm, Alîm; göklerin, yerin ve arasındakilerin mülkü O'nun, saatin bilgisi O'nun katında, O'na döndürüleceksiniz; O'nu bırakıp yalvardıkları şefaate güç yetiremez, hakka bilerek şahitlik edenler başka; kendilerini kimin yarattığını sorsan 'Allah' derler, nasıl çevriliyorlar; 'ey Rabbim, bunlar iman etmeyen bir kavim'; onlardan yüz çevir, 'selâm' de, yakında bilecekler",
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

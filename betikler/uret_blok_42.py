# -*- coding: utf-8 -*-
"""uret_blok_42.py — sûre 42 (Şûrâ) blok betiklerini üretir. BLOK BAŞINA KAYIT.

Değişiklik (2026-09-24): kayıt artık tur sonunu beklemiyor. Her blok betiği koşulduğunda
okuma_metni.json, mercek_kayit.json ve ilerleme o blok için yazılır; blok bilançosu (TAM SAYIM)
ve çıpa kararları da okuma_metni'ne yapılandırılmış alan olarak girer. Oturum yarıda kalsa da
okunmuş her blok kayıtlıdır.

Sûre numarası TEK değişkende (S). olcum_bicim.olcum(S, n), AR[(S, n)], OM[str(S)] hep S'den
türer — üç kez atlanan elle-değiştirme hatası (tur sonu notu) burada yapısal olarak kapalı.
Besmele korpustan (1:1'in ilk dört kelimesinin iskeleti) ayıklanır; Arapça sabit yok.
"""
import sys
S = 42
METIN = 'shura_metin_1'
KAYIT = 'shura_kayit'
# blok başı kayıt: blok okundukça listeye eklenir (başlık okuma sonrası yazılır)
BLOKLAR = [(1, 10), (11, 20), (21, 30), (31, 40), (41, 50), (51, 53)]
BASLIK = {
 (1, 10): "sûre 42 (Şûrâ) birinci blok — Hâ Mîm, Ayn Sîn Qâf; Azîz ve Hakîm Allah sana ve öncekilere böyle vahyediyor; göklerdekiler ve yerdekiler O'nun; gökler üstlerinden çatlayacak gibi, melekler tesbih edip yerdekiler için bağışlanma diliyor; O'nu bırakıp dost edinenleri Allah gözetir, sen vekil değilsin; Arapça Kur'an ile şehirlerin anasını ve toplanma gününü uyarma, bir grup cennette bir grup saîrde; Allah dileseydi tek ümmet yapardı; dost ancak Allah, ölüleri diriltir; ayrılığa düştüğünüz şeyin hükmü Allah'a, 'O'na dayandım, O'na yöneliyorum'",
 (11, 20): "sûre 42 (Şûrâ) ikinci blok — göklerin ve yerin yaratıcısı, size ve davarlara eşler, O'nun benzeri gibi hiçbir şey yok; göklerin ve yerin anahtarları O'nun, rızkı bol verir ve daraltır; Nûh'a, sana, İbrâhîm, Mûsâ ve Îsâ'ya buyrulan din: dini ayakta tutun, ayrılığa düşmeyin; bilgi geldikten sonra taşkınlıkla ayrılığa düştüler; çağır ve emrolunduğun gibi dosdoğru ol, 'Allah bizim de Rabbimiz sizin de'; tartışanların delili çürük; kitabı hak ile ve mizanı indiren Allah, saat belki yakın; Allah kullarına lütufkâr; âhiret ekini / dünya ekini",
 (21, 30): "sûre 42 (Şûrâ) üçüncü blok — Allah'ın izin vermediğini dinden yol koyan ortaklar; zalimler kazandıklarından korkar, iman edenler cennet bahçelerinde; yakınlıkta sevgiden başka ücret istemiyorum; 'Allah'a yalan uydurdu' mu diyorlar, Allah bâtılı siler hakkı sözleriyle gerçekleştirir; tevbeyi kabul eden, kötülükleri affeden; rızkı bol verseydi yeryüzünde taşkınlık ederlerdi, ölçüyle indirir; umut kesildikten sonra yağmuru indiren; gökler, yer ve ikisinde yayılan canlılar O'nun âyetlerinden; başınıza gelen musibet ellerinizin kazandığıdır",
 (31, 40): "sûre 42 (Şûrâ) dördüncü blok — yeryüzünde âciz bırakamazsınız, Allah'tan başka dost ve yardımcı yok; denizde dağlar gibi akıp gidenler O'nun âyetlerinden, dilerse rüzgârı durdurur da durgun kalırlar ya da kazandıkları yüzünden helak eder, çoğunu affeder; âyetlerimiz hakkında tartışanlar kaçacak yer olmadığını bilecek; dünya hayatının geçimliği ve Allah katındaki daha hayırlı ve kalıcı olan: iman edip Rablerine dayananlar, büyük günahlardan kaçınıp öfkelenince bağışlayanlar, Rablerine icabet edip namaz kılanlar, işleri aralarında danışma olanlar, taşkınlığa uğrayınca karşı koyanlar; kötülüğün karşılığı denk kötülük, affedip düzeltenin ödülü Allah'a",
 (41, 50): "sûre 42 (Şûrâ) beşinci blok — zulme uğrayıp kendini savunanın aleyhine yol yok, yol insanlara zulmedip yeryüzünde haksız taşkınlık edenlerin aleyhine; sabredip bağışlamak azim isteyen işlerden; Allah'ın saptırdığına dost yok, zalimler azabı görünce dönüş yolu arar; ateşe sunulurken gizli göz ucuyla bakarlar, iman edenler: asıl hüsrana uğrayanlar kendilerini ve ailelerini kaybedenler; geri çevrilmesi olmayan gün gelmeden Rabbinize icabet edin; yüz çevirirlerse sen bekçi değilsin, sana düşen tebliğ; insan rahmete sevinir, kötülük dokununca nankördür; göklerin ve yerin mülkü Allah'ın: dilediğine kız, dilediğine erkek, ya da ikisini birlikte verir, dilediğini kısır kılar",
 (51, 53): "sûre 42 (Şûrâ) son blok — Allah beşerle ancak vahiyle, perde arkasından ya da elçi göndererek konuşur; böylece sana da emrimizden bir ruh vahyettik, kitap ve iman nedir bilmiyordun, onu kullarımızdan dilediğimizi doğru yola ilettiğimiz nur kıldık, sen de dosdoğru yola iletirsin; göklerdekiler ve yerdekiler kendisinin olan Allah'ın yolu; bütün işler Allah'a varır",
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

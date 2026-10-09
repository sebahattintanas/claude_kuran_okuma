# -*- coding: utf-8 -*-
"""uret_blok_37.py — sûre 37 (Sâffât) blok betiklerini üretir. BLOK BAŞINA KAYIT.

Değişiklik (2026-09-24): kayıt artık tur sonunu beklemiyor. Her blok betiği koşulduğunda
okuma_metni.json, mercek_kayit.json ve ilerleme o blok için yazılır; blok bilançosu (TAM SAYIM)
ve çıpa kararları da okuma_metni'ne yapılandırılmış alan olarak girer. Oturum yarıda kalsa da
okunmuş her blok kayıtlıdır.

Sûre numarası TEK değişkende (S). olcum_bicim.olcum(S, n), AR[(S, n)], OM[str(S)] hep S'den
türer — üç kez atlanan elle-değiştirme hatası (tur sonu notu) burada yapısal olarak kapalı.
Besmele korpustan (1:1'in ilk dört kelimesinin iskeleti) ayıklanır; Arapça sabit yok.
"""
import sys
S = 37
METIN = 'saffat_metin_1'
KAYIT = 'saffat_kayit'
# blok başı kayıt: blok okundukça listeye eklenir (başlık okuma sonrası yazılır)
BLOKLAR = [(1, 10), (11, 20), (21, 30), (31, 40), (41, 50), (51, 60), (61, 70), (71, 80), (81, 90)]
BASLIK = {
 (1, 10): 'sûre 37 (Sâffât) birinci blok — üç adsız topluluğa yemin, ilâhın birliği, göklerin ve doğuların Rabbi, dünya göğünün yıldızlarla süslenmesi, azgın şeytandan korunma, kulak verenin atışa tutulması ve kapanı izleyen alev.',
 (11, 20): "sûre 37 ikinci blok — 'onlara sor': yapışkan çamurdan yaratılış, şaşma ve alay, hatırlatılınca hatırlamama, 'apaçık büyü', 'toprak ve kemik olunca mı', 'evet, boyun eğmiş olarak', tek haykırış, 'vay bize, bu din günü'.",
 (21, 30): "sûre 37 üçüncü blok — ayrım günü, zalimlerin eşleriyle ve taptıklarıyla toplanması, cahîmin yoluna sevk ve durdurma, 'neden yardımlaşmıyorsunuz', teslimiyet, birbirine dönüp soruşma: 'sağ yandan gelirdiniz' / 'hayır, siz inanmıyordunuz, azgın bir kavimdiniz'.",
 (31, 40): "sûre 37 dördüncü blok — 'Rabbimizin sözü hak oldu', 'sizi azdırdık, biz de azgındık', azapta ortaklık, 'lâ ilâhe illa'llâh' denince büyüklenme, 'deli bir şair için mi', 'o hakkı getirdi', 'siz tadacaksınız', yalnız yaptığınızla — Allah'ın ihlâsa erdirilmiş kulları müstesna.",
 (41, 50): "sûre 37 beşinci blok — muhlas kullar: bilinen rızık, meyveler, nimet cennetleri, karşılıklı tahtlar, pınardan dolaştırılan beyaz kadeh (sersemletmez, sarhoş etmez), bakışını sınırlayan iri gözlü eşler — saklı yumurta gibi; ve 37:27'nin tekrarı: birbirine dönüp soruşma.",
 (51, 60): "sûre 37 altıncı blok — cennetteki biri: 'bir arkadaşım vardı, sen de mi doğrulayanlardansın, ölüp toprak ve kemik olunca mı cezalandırılacağız derdi'; yukarıdan bakış, cahîmin ortası; 'Allah'a yemin, az kalsın beni de helak edecektin; Rabbimin nimeti olmasa'; ilk ölümden başka ölüm yok — büyük kurtuluş.",
 (61, 70): "sûre 37 yedinci blok — 'çalışanlar bunun için çalışsın'; konukluk mu hayırlı, zakkum ağacı mı: zalimlere sınama, cahîmin dibinden çıkan, tomurcukları şeytan başları gibi; karınlar dolar, üstüne kaynar su, dönüş cahîme — çünkü atalarını sapmış buldular ve izlerinde koşturuluyorlar.",
 (71, 80): "sûre 37 sekizinci blok — öncekilerin çoğu saptı, uyarıcılar gönderildi, uyarılanların sonuna bak (Allah'ın muhlas kulları müstesna); Nûh kıssası: seslendi, icabet edildi, ailesiyle büyük sıkıntıdan kurtarıldı, soyu kalıcı kılındı, sonrakiler arasında 'Nûh'a selâm' bırakıldı — iyileri böyle ödüllendiririz.",
 (81, 90): "sûre 37 dokuzuncu blok — Nûh kıssasının kapanışı (inanan kullarımızdan; sonra ötekileri boğduk); İbrâhîm, Nûh'un yolundan: Rabbine sağlam kalple geldi; babasına ve kavmine: neye tapıyorsunuz, Allah'ı bırakıp uydurma ilâhlar mı, âlemlerin Rabbi hakkında ne sanıyorsunuz; yıldızlara bir bakış, 'ben hastayım', yüz çevirip gittiler.",
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

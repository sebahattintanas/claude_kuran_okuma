# -*- coding: utf-8 -*-
"""uret_blok_40.py — sûre 40 (Ğâfir) blok betiklerini üretir. BLOK BAŞINA KAYIT.

Değişiklik (2026-09-24): kayıt artık tur sonunu beklemiyor. Her blok betiği koşulduğunda
okuma_metni.json, mercek_kayit.json ve ilerleme o blok için yazılır; blok bilançosu (TAM SAYIM)
ve çıpa kararları da okuma_metni'ne yapılandırılmış alan olarak girer. Oturum yarıda kalsa da
okunmuş her blok kayıtlıdır.

Sûre numarası TEK değişkende (S). olcum_bicim.olcum(S, n), AR[(S, n)], OM[str(S)] hep S'den
türer — üç kez atlanan elle-değiştirme hatası (tur sonu notu) burada yapısal olarak kapalı.
Besmele korpustan (1:1'in ilk dört kelimesinin iskeleti) ayıklanır; Arapça sabit yok.
"""
import sys
S = 40
METIN = 'gafir_metin_1'
KAYIT = 'gafir_kayit'
# blok başı kayıt: blok okundukça listeye eklenir (başlık okuma sonrası yazılır)
BLOKLAR = [(1, 10), (11, 20), (21, 30), (31, 40), (41, 50), (51, 60), (61, 70), (71, 80), (81, 85)]
BASLIK = {
 (1, 10): "sûre 40 (Ğâfir) birinci blok — Hâ Mîm; kitabın azîz ve alîm Allah'tan indirilişi; günahı bağışlayan, tevbeyi kabul eden, cezası çetin; ayetler hakkında yalnız inkâr edenlerin tartışması; Nûh kavmi ve gruplar, elçiyi yakalamaya niyet, 'cezalandırmam nasıl oldu'; Rabbin sözü gerçekleşti; Arşı taşıyanların ve çevresindekilerin iman edenler için duası; Adn cennetleri, kötülüklerden korunma; inkâr edenlere seslenme: Allah'ın öfkesi",
 (11, 20): "sûre 40 (Ğâfir) ikinci blok — 'iki kez öldürdün, iki kez dirilttin, çıkmaya yol var mı?'; Allah tek anılınca inkâr, ortak koşulunca iman; ayetleri gösteren, gökten rızık indiren; dini hâlis kılarak dua edin; dereceleri yüksek, Arş'ın sahibi, rûhu dilediğine bırakan; buluşma günü: 'bugün mülk kimin?' — 'bir olan, kahredici Allah'ın'; her can kazandığıyla karşılık bulur; yaklaşan gün, gırtlağa dayanan kalpler; gözlerin hıyaneti ve göğüslerin gizlediği; hak ile hükmeden işiten, gören Allah",
 (21, 30): "sûre 40 (Ğâfir) üçüncü blok — yeryüzünde gezip öncekilerin sonuna bakmadılar mı, güçte üstündüler, Allah onları yakaladı; elçiler apaçık delillerle geldi; Mûsâ ayetler ve apaçık yetkiyle Firavun, Hâmân ve Kârûn'a: 'büyücü, yalancı'; iman edenlerin oğullarını öldürün, kadınlarını sağ bırakın; Firavun: 'bırakın Mûsâ'yı öldüreyim'; Mûsâ: 'Rabbime ve Rabbinize sığındım'; imanını gizleyen adam: 'Rabbim Allah dediği için mi öldüreceksiniz?', yalancıysa / doğruysa; 'bugün mülk sizin'; Firavun: 'size yalnız gördüğümü gösteriyorum'; iman eden: 'grupların gününün benzerinden korkuyorum'",
 (31, 40): "sûre 40 (Ğâfir) dördüncü blok — iman edenin konuşması sürüyor: Nûh, Âd, Semûd'un gidişatı, Allah kullara zulüm dilemez; çağrışma günü, arkaya dönüp kaçış, Allah'a karşı koruyucu yok; Yûsuf apaçık delillerle geldi, öldüğünde 'Allah artık elçi göndermez' dediniz; yetkisizce tartışanlar, büyüklenen zorba kalp mühürlenir; Firavun: 'Hâmân, bana kule yap, göklerin yollarına ulaşıp Mûsâ'nın ilâhına bakayım', kötü işi süslendi, tuzağı yıkımda; iman eden: 'bana uyun, sizi doğru yola ileteyim; dünya hayatı geçimlik, âhiret kalınacak yurt'; kötülük dengiyle, iyi iş hesapsız rızıkla",
 (41, 50): "sûre 40 (Ğâfir) beşinci blok — iman edenin son sözleri: 'ben sizi kurtuluşa çağırıyorum, siz beni ateşe'; 'beni inkâra çağırıyorsunuz, ben sizi azîz ve ğaffâra'; çağırdığınızın çağrısı yok, dönüş Allah'a; 'işimi Allah'a havale ediyorum'; Allah onu korudu, Firavun ailesini azap kuşattı: sabah akşam ateşe sunulurlar, kıyamet günü en çetin azaba; ateşte zayıflar ve büyüklenenler çekişir: 'hepimiz içindeyiz'; cehennem bekçilerine: 'Rabbinize dua edin'; 'elçiler gelmedi mi?' — 'evet' — 'öyleyse dua edin'",
 (51, 60): "sûre 40 (Ğâfir) altıncı blok — elçilere ve iman edenlere dünyada ve şahitler gününde yardım; zalimlere özürlerinin fayda vermediği gün; Mûsâ'ya hidâyet, İsrâiloğullarına kitap mirası, akıl sahiplerine öğüt; sabret, bağışlanma dile, akşam ve sabah tesbih et; yetkisizce tartışanların göğsünde kibir, Allah'a sığın; göklerin ve yerin yaratılışı insanınkinden büyük; kör ile gören bir olmaz; o saat gelecek; Rabbiniz: 'Bana dua edin, karşılık vereyim'",
 (61, 70): "sûre 40 (Ğâfir) yedinci blok — geceyi dinlenmeye, gündüzü göstermeye kılan Allah; 'İşte Rabbiniz Allah, her şeyin yaratıcısı — nasıl çevriliyorsunuz?'; ayetleri inkâr edenler de böyle çevrilir; yeri durak, göğü bina kılan, biçimlendiren, rızıklandıran; diri olan, dini O'na hâlis kılarak dua edin; 'De ki: men edildim, teslim olmakla emrolundum'; topraktan, nutfeden, alakadan yaratılış, bebeklik, güçlü çağ, yaşlılık, adı konmuş süre; dirilten ve öldüren, 'Ol' der olur; ayetler hakkında tartışanlar nasıl çevriliyor; kitabı ve elçileri yalanlayanlar yakında bilecek",
 (71, 80): "sûre 40 (Ğâfir) sekizinci blok — boyunlarda halkalar ve zincirlerle sürüklenme, kaynar su ve ateş; 'ortak koştuklarınız nerede?' — 'kaybolup gittiler, hayır, hiçbir şeye dua etmiyorduk'; yeryüzünde haksız sevinç ve şımarıklık; cehennemin kapılarından girin, büyüklenenlerin durağı; sabret, Allah'ın vaadi hak; senden önceki elçiler, kimi anlatıldı kimi anlatılmadı, izinsiz ayet yok; davarlar binmek ve yemek için, faydalar, davarlar ve gemiler üzerinde taşınma",
 (81, 85): "sûre 40 (Ğâfir) dokuzuncu ve son blok — ayetlerini gösteriyor, hangisini tanımazsınız; yeryüzünde gezip öncekilerin sonuna bakmadılar mı, daha çok ve daha güçlüydüler, kazandıkları fayda vermedi; elçiler açık delillerle geldiğinde yanlarındaki bilgiyle sevindiler; azabı görünce 'yalnız Allah'a iman ettik' dediler; o an imanları fayda vermedi — Allah'ın kulları arasında geçmiş yolu; inkâr edenler hüsrana uğradı",
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

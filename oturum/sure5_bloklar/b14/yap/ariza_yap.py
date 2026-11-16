# blok 14 (5:41) ARIZA oluşturucu — bölüm 7-1 (bölüm açılışı)
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b14/olcum.txt'
os.environ['SAY2'] = '/home/claude/b14/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b13.txt', encoding='utf-8').read() + ']')
VF_YAZI_ESKI = {33: {6: "'ve rasûlehû'", 7: "'ve yes'avne'", 18: "'ve erculuhum'", 30: "'ve lehum fi'l-âxirati'"}, 34: {9: "'fa'lemû'"}, 35: {6: "'ve'bteğû'", 9: "'ve câhidû'"}, 36: {11: "'ve mislehû'", 22: "'ve lehum 'azâbun'"}}
BOL = "'Küfürde yarışanlar; Tevrat, İncil ve Kitap ile hüküm'"


def sd(key):
    return sayim.S2[key][1]


def sic(key):
    n, d = sayim.S2[key]
    return 1 + len([x for x in d['basilan'] if x.startswith('5:')]) + d['okunmus_si'] + d['henuz_si']


def taban(key, ay):
    n, d = sayim.S2[key]
    p = [ay] + [x for x in d['basilan'] if x.startswith('5:') and x != ay]
    if d['okunmus_si']: p.append('okunmus_si %d' % d['okunmus_si'])
    if d['henuz_si']: p.append('henuz_si %d' % d['henuz_si'])
    return ' + '.join(p)


R5 = [
 ("5:41", "'fî âxir 'azâb 'azîm'", 2, 'say 5:41 64-67', "harekesiz 'fi'l-âxirati 'azâbun 'azîm' (64-67. kelime)", None),
 ("5:41", "'min ellezî qâle'", 2, 'say 5:41 9-11', "harekesiz 'mine'llezîne qâlû' (9-11. kelime)",
  ('dizi 5 41 9 11', "min ellezî qâle", '9-11', "çekim farkı — harekesiz kalıp fiil çekimini ayırıyor (terim: 'dizi 5 41 9 11')")),
 ("5:41", "'min allâh şey''", 2, 'say 5:41 48-50', "harekesiz 'mina'llâhi şey'â' (48-50. kelime)", None),
 ("5:41", "'erâde allâh en'", 2, 'say 5:41 54-56', "harekesiz 'yuridi'llâhu en' (54-56. kelime)",
  ('dizi 5 41 54 56', "erâde allâh en", '54-56', "çekim farkı — harekesiz kalıp fiil kipini ve şahsını ayırıyor (terim: 'dizi 5 41 54 56')")),
]
r5 = []
for ay, kal, nk, key, ad, dz in R5:
    s = sic(key)
    h = "%s nakarat3 %s %d (tür ic) / %s sûre içi %d (%s)" % (ay, kal, nk, ad, s, taban(key, ay))
    if s == nk:
        h += ' — tutuyor'
    else:
        dk, dad, dar, ger = dz
        ds = sic(dk)
        if ds == nk:
            h += " — tutmuyor; eşit aralıkla lemma dizisi '%s' (%s. kelime) sûre içi %d (%s) — tutuyor; gerekçe %s" % (dad, dar, ds, taban(dk, ay), ger)
        else:
            h += " — tutmuyor; eşit aralıkla lemma dizisi '%s' (%s. kelime) sûre içi %d (%s) — tutmuyor; gerekçe %s" % (dad, dar, ds, taban(dk, ay), ger)
    r5.append(h)

K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k}

VF_YAZI = {41: {14: "'ve lem tu'min'", 17: "'ve mine'llezîne hâdû'", 36: "'fe-xuzûhu'", 37: "'ve in lem'", 40: "'fa'hzerû'", 41: "'ve men'", 45: "'fe-len'", 63: "'ve lehum fi'l-âxirati'"}}
M41 = ("5:41 'Ey elçi!' ('yâ eyyuhe'r-rasûl', 'yâ' 1. kelimede 'ey' ile, 'eyy' ve 'hâ' 1. kelimede karşılıksız, 'elçi' 'rasûl' karşılığı (2. kelime; belirli)); "
 "'küfürde yarışanlar seni üzmesin' ('lâ yahzunke'llezîne yusâri'ûne fi'l-kufr', 'lâ' 3. kelimede olumsuz emir eki ile ('üzmesin' içinde; morph PRO), 'üz-' 'yahzunke' karşılığı (4. kelime; I. bab; LEM 'yahzun' (morph LEM ham biçim)), 'ke' 4. kelimede 'seni' ile, 'ellezîne' 5. kelimede '-anlar' ile (ism-i mevsûl; 'yarışanlar' içinde), "
 "'yarış-' 'yusâri'ûne' karşılığı (6. kelime; III. bab; LEM 'yusâri'u' (morph LEM ham biçim)), 'ûne' 6. kelimede karşılıksız (fail eki — 'yarışanlar' içinde), 'fî' 7. kelimede '-de' ile, 'küfür' 'kufr' karşılığı (8. kelime), sıralama: fail öne alındı); "
 "'Ağızlarıyla «İman ettik» deyip kalpleri iman etmemiş olanlardan' ('mine'llezîne qâlû âmennâ bi-efvâhihim ve lem tu'min qulûbuhum', 'min' 9. kelimede '-dan' ile ('olanlardan' içinde), 'ellezîne' 10. kelimede '-anlar' ile (ism-i mevsûl; 'olanlardan' içinde), 'de-' 'qâlû' karşılığı (11. kelime; I. bab; '-ip' zarf-fiil açılımı), "
 "'û' 11. kelimede karşılıksız (fail eki — 'deyip' içinde), 'iman et-' 'âmennâ' açılımı (12. kelime; IV. bab; söz içi), 'nâ' 12. kelimede 1P ile ('ettik' içinde), 'bi' 13. kelimede vasıta eki ile ('Ağızlarıyla' içinde), 'ağız' 'efvâh' karşılığı (13. kelime; çoğul '-lar'), 'him' 13. kelimede iyelik ile ('Ağızlarıyla' içinde), "
 "'ve' 14. kelimede karşılıksız (morph REM), 'lem' 14. kelimede olumsuzluk eki ile ('etmemiş' içinde; morph NEG), 'iman et-' 'tu'min' açılımı (15. kelime; IV. bab; 3FS), 'kalp' 'qalb' karşılığı (16. kelime; çoğul; iyelik ile 'kalpleri'), 'hum' 16. kelimede iyelik ile ('kalpleri' içinde), 'ol-' takdiri ('olanlardan' içinde), sıralama: söz öne alındı); "
 "'ve Yahudi olanlardan' ('ve mine'llezîne hâdû', 've' 17. kelimede 've' ile (morph CONJ), 'min' 17. kelimede '-dan' ile, 'ellezîne' 18. kelimede '-anlar' ile (ism-i mevsûl), 'Yahudi ol-' 'hâdû' açılımı (19. kelime; I. bab; LEM 'hâdu' (morph LEM ham biçim)), 'û' 19. kelimede karşılıksız (fail eki — 'olanlardan' içinde)); "
 "'Onlar yalana çokça kulak verenler' ('semmâ'ûne li'l-kezib', 'onlar' takdiri (mübteda takdiri), 'çokça kulak veren' 'semmâ'' açılımı (20. kelime; mübalağa; çoğul '-ler'), 'li' 21. kelimede yönelme eki ile ('yalana' içinde; fiil yönetimi takdiri), 'yalan' 'kezib' karşılığı (21. kelime)); "
 "'sana gelmemiş başka bir topluluk için çokça kulak verenlerdir' ('semmâ'ûne li-qavmin âxarîne lem ye'tûk', 'çokça kulak veren' 'semmâ'' açılımı (22. kelime; çoğul '-ler'), 'li' 23. kelimede 'için' ile, 'topluluk' 'qavm' karşılığı (23. kelime; nekre — 'bir' takdiri), 'başka' 'âxar' karşılığı (24. kelime; sıfat; çoğul), "
 "'lem' 25. kelimede olumsuzluk eki ile ('gelmemiş' içinde; morph NEG), 'gel-' 'ye'tû' karşılığı (26. kelime; I. bab; '-memiş' sıfat-fiil açılımı), 'û' 26. kelimede karşılıksız (fail eki — 'gelmemiş' içinde), 'ke' 26. kelimede yönelme eki ile ('sana' içinde; fiil yönetimi takdiri), '-dir' takdiri ('verenlerdir' içinde; isim cümlesi haberi), sıralama: sıfat cümlesi öne); "
 "'kelimeleri yerlerine konduktan sonra değiştirirler' ('yuharrifûne'l-kelime min ba'di mevâdi'ih', 'değiştir-' 'yuharrifûne' karşılığı (27. kelime; II. bab; LEM 'yuharrifu' (morph LEM ham biçim)), 'ûne' 27. kelimede karşılıksız (fail eki — 'değiştirirler' içinde), 'kelime' 'kelim' karşılığı (28. kelime; çoğul '-ler'), "
 "'min' 29. kelimede karşılıksız ('sonra' içinde), 'sonra' 'ba'd' karşılığı (30. kelime), 'yer' 'mevâdi'' karşılığı (31. kelime; çoğul; yönelme eki ile 'yerlerine'), 'hî' 31. kelimede iyelik ile ('yerlerine' içinde), 'kon-' takdiri ('konduktan' içinde; 'mevâdi'' açılımı), sıralama: fiil sona alındı); "
 "'«Size bu verilirse onu alın, o size verilmezse sakının» derler' ('yeqûlûne in ûtîtum hâzâ fe-xuzûhu ve in lem tu'tevhu fa'hzerû', 'de-' 'yeqûlûne' karşılığı (32. kelime; I. bab), 'ûne' 32. kelimede karşılıksız (fail eki — 'derler' içinde), 'in' 33. kelimede '-se' ile ('verilirse' içinde; morph COND), "
 "'ver-' 'ûtîtum' karşılığı (34. kelime; IV. bab; edilgen '-il'), 'tum' 34. kelimede 2MP ile ('Size' içinde; söz muhatabı), 'hâzâ' 35. kelimede 'bu' ile, 'fe' 36. kelimede karşılıksız (morph RSLT; şart cevabı), 'al-' 'xuzû' karşılığı (36. kelime; I. bab; emir 2MP), 'û' 36. kelimede 2MP ile ('alın' içinde), 'hu' 36. kelimede 'onu' ile, "
 "'ve' 37. kelimede karşılıksız (morph CONJ; virgül), 'in' 37. kelimede '-se' ile ('verilmezse' içinde; morph COND), 'lem' 38. kelimede olumsuzluk eki ile ('verilmezse' içinde; morph NEG), 'ver-' 'tu'tevhu' karşılığı (39. kelime; IV. bab; edilgen), 'û' 39. kelimede karşılıksız (nâib fâil eki 2MP — 'size' takdiri), 'hu' 39. kelimede 'o' ile, "
 "'fe' 40. kelimede karşılıksız (morph RSLT), 'sakın-' 'hzerû' karşılığı (40. kelime; I. bab; emir 2MP; LEM 'yahzeru' (morph LEM ham biçim)), 'û' 40. kelimede 2MP ile ('sakının' içinde), sıralama: söz öne alındı); "
 "'Allah kimin fitnesini isterse' ('ve men yuridi'llâhu fitneteh', 've' 41. kelimede karşılıksız (morph REM), 'men' 41. kelimede 'kimin' ile (morph COND; şart eki '-se' 'isterse' içinde), 'iste-' 'yuridi' karşılığı (42. kelime; IV. bab), lafız 43. kelimede 'Allah' ile, 'fitne' 'fitne' karşılığı (44. kelime; iyelik ile 'fitnesini'), 'hû' 44. kelimede iyelik ile ('fitnesini' içinde), sıralama: fiil sona alındı); "
 "'onun için Allah'a karşı hiçbir şeye güç yetiremezsin' ('fe-len temlike lehû mina'llâhi şey'â', 'fe' 45. kelimede karşılıksız (morph RSLT; şart cevabı), 'len' 45. kelimede olumsuzluk eki ile ('yetiremezsin' içinde; morph NEG), 'güç yetir-' 'temlike' açılımı (46. kelime; I. bab; 2MS; LEM 'meleket' (morph LEM ham biçim)), "
 "'li' 47. kelimede 'için' ile, 'hû' 47. kelimede 'onun' ile, 'min' 48. kelimede 'karşı' ile (yönelme eki 'Allah'a' içinde; fiil yönetimi takdiri), lafız 49. kelimede 'Allah' ile, 'şey' 'şey'' karşılığı (50. kelime; nekre — 'hiçbir' takdiri; yönelme eki ile 'şeye'), sıralama: fiil sona alındı); "
 "'Onlar, Allah'ın kalplerini temizlemek istemediği kimselerdir' ('ulâ'ike'llezîne lem yuridi'llâhu en yutahhira qulûbehum', 'ulâ'ike' 51. kelimede 'onlar' ile, 'ellezîne' 52. kelimede 'kimseler' ile (ism-i mevsûl; 'kimselerdir' içinde), 'lem' 53. kelimede olumsuzluk eki ile ('istemediği' içinde; morph NEG), "
 "'iste-' 'yuridi' karşılığı (54. kelime; IV. bab; '-diği' sıfat-fiil açılımı), lafız 55. kelimede 'Allah' ile (ilgi eki 'Allah'ın' içinde), 'en' 56. kelimede '-mek' ile (masdar; morph SUB), 'temizle-' 'yutahhira' karşılığı (57. kelime; II. bab), 'kalp' 'qalb' karşılığı (58. kelime; çoğul; iyelik ile 'kalplerini'), 'hum' 58. kelimede iyelik ile ('kalplerini' içinde), "
 "'-dir' takdiri ('kimselerdir' içinde; isim cümlesi haberi), sıralama: haber sona alındı); "
 "'Onlar için dünyada bir rezillik' ('lehum fi'd-dunyâ xizyun', 'li' 59. kelimede 'için' ile, 'hum' 59. kelimede 'onlar' ile, 'fî' 60. kelimede '-da' ile, 'dünya' 'dunyâ' karşılığı (61. kelime), 'rezillik' 'xizy' karşılığı (62. kelime; nekre — 'bir' takdiri)); "
 "'âhirette de onlar için büyük bir azap vardır' ('ve lehum fi'l-âxirati 'azâbun 'azîm', 've' 63. kelimede 'de' ile (morph CONJ), 'li' 63. kelimede 'için' ile, 'hum' 63. kelimede 'onlar' ile, 'fî' 64. kelimede '-te' ile, 'âhiret' 'âxir' karşılığı (65. kelime; belirli dişil), 'azap' ''azâb' karşılığı (66. kelime; nekre — 'bir' takdiri), "
 "'büyük' ''azîm' karşılığı (67. kelime; nekre — takdirsiz; sıfat), 'var' takdiri (isim cümlesi), '-dır' takdiri ('vardır' içinde; isim cümlesi haberi), sıralama: mübteda sona alındı)")
MEALS = (M41,)




def _bol(s, sep):
    out, d, cur, i = [], 0, '', 0
    while i < len(s):
        c = s[i]
        if c == '(': d += 1
        elif c == ')': d -= 1
        if d == 0 and s.startswith(sep, i):
            out.append(cur); cur = ''; i += len(sep); continue
        cur += c; i += 1
    out.append(cur)
    return out


MK = {}
for blok in MEALS:
    n = int(blok.split(' ', 1)[0].split(':')[1]); govde = blok.split(' ', 1)[1]
    for seg in _bol(govde, "; '"):
        seg = seg if seg.startswith("'") else "'" + seg
        j = seg.index("' (")
        tr = seg[1:j]; ic = seg[j + 3:].rstrip(')')
        parca = _bol(ic, ', ')
        MK.setdefault(n, []).append((tr, parca[0].strip("'"), parca[1:]))
open('/home/claude/b14/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '14')
BLOKLAR = [str(i) for i in range(1, 15)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR).replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '14').replace('\n', '; ')
EMS = open('/home/claude/b14/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '41', '41', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b14/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
MFARK = [(k, n, sayim.S2[k.replace(' --medde', '')][0]) for k, (n, d) in sayim.S2.items() if '--medde' in k]
MEDF = '; '.join("%s meddeli %d / meddesiz %d" % (k.replace(' --medde', ''), m, n) for k, n, m in MFARK)
MEDF += ' — fark yok, yeni eş yok' if all(n == m for k, n, m in MFARK) else ' — FARK VAR'
GLS = run('/home/claude/sunum/gloss_tara.py', '41', '41', '14').splitlines()

I = list(BEK) + [
 "bölüm 6 denetimi kurallarının uygulanışı (bölüm 5 kuralı 11 — bu bloktan önce değişen araçlar): sunum/bolum4_kurallar.py (kural 1: A1 kapsamı — morph'ta şahıs etiketli her kelime A1'de numarasıyla ya da ◇ alıntısıyla; kelime sayacı 'fa' / 'va' önekini ve 'li-' / 'bi-' önekli kelime başını tanıyor; kural 15: adsız ölçütü yalnız 'adsız' (ya da 'adlı aktör'), 'lafız' / 'gönderge lafız' ölçüt yerine geçmiyor), "
 "sunum/bolum5_kurallar.py (kural 3: lemma listesi virgülle bölünüyor, çakışma maddesinde kökü ve ayeti anılan ad o ayetlerdeki o köklü fiil LEM'iyle iskelet eşleniyor — normalleştirilmiş ad isabet; kural 4: anılış yalnız ◈ tetik maddesi ve tetik dışı maddesinin 'anılış:' bölümü, betik içi mutasyon assert'i, gloss türevli adaylar (zaman / beden / hayat-ölüm sözcükleri); kural 5: iki ayetle alıntılanan kalıpların ortak başı sayımla anılmalı; kural 6: aday 1039 ayetler arası çiftleri ◇ ile bayt eşleniyor), "
 "sunum/bolum6_kurallar.py (yeni; kural 2: çakışma grubu kapsamı ve grup başına tam bir kapalı karar; kural 7: ARIZA'ya yapıştırılan gloss_tara / es_edat / bolum5 çıktılarının tazeliği; kural 12: Türkçe alıntılar MEAL alt dizesi; kural 13: yıldız maddesi ⇔ blok_bilanco yıldız kaynağı; kural 14: esmâ kural adı ⇔ eş yapılı önceki kayıtların emsali; kural 16: lemma dizisi adında joker '_'), "
 "sunum/edat_etiket.py ve sunum/es_edat.py (kural 11: 'nahnu' zamir kümesinde; 'bel', 'mâzâ', 'ne', 'ni' tanınan listede; 'ğayr' isim olarak tablo dışında — gerekçe betikte), sunum/yasakli.sh (kural 10: 'önceki / sonraki' + 'ayet' büyük harfle başlayan biçimde de; sınama dosyasına büyük harfli satır eklendi), "
 "sunum/geriye_donuk.py (yeni; kural 9: bütün bölüm araçları — bolum4 / bolum5 / bolum6, es_edat tanınmayan, gloss_tara, kelime_kontrol, yasakli.sh — okunmuş bütün bloklarda; önceki dosyayla düşen / yeni isabet farkı başta), sunum/mutasyon_sina.py (yeni; kurallar 1-7, 12, 14-16 için bozulmuş kopya ve sağlam kayıt sınamaları — MUT_SONUC), "
 "b14/yap/ariza_yap.py (kural 2: çakışma maddesi araçla eş süzgeçle — bu bloğun karşılıklarına dokunan gruplar ve KÖK grupları; kural 7: araç çıktıları son yazımdan sonra yeniden koşulup kararlı olana dek yeniden yazılıyor); sunum/sinifla.py (SON 41); elle kalan: kural 8 (R5 gerekçesinde terimler say2 anahtarıyla, yalnız bir ölçüden), kural 13'ün yazım tarafı (yıldız maddesi bilanço biçimiyle)",
 "geriye dönük koşu (bölüm 6 kuralı 9 — komut 'python3 sunum/geriye_donuk.py b13 yamalar/geriye_donuk_5_b11.txt'): yamalar/geriye_donuk_5_b13.txt — GERI_P; önceki dosyadan düşen isabetlerin çoğu araç değişikliği ve satır biçimi farkı (dosyanın başında listeli); isabetler tam okuma sonu listesine, kayıtlar yeniden yazılmadı; "
 "öz denetim notu (bölüm 6 kuralı 10): yasakli.sh IZIN listesine blok 12'de eklenen 5:27:12 alıntısı izni (es_lemma çıktısının eski kayıt alıntısı) o bloğun öz denetim maddesinde anılmamıştı — burada anıldı; blok 13'te 5:39 R5 gerekçesi harekesiz sayımla lemma dizisi sayımını topluyordu (bölüm 6 denetimi bulgusu) — 5:34 / 5:39 'ان' iskeleti farkı yeniden açık, tam okuma sonu",
 "kök tablosu: ölçümde '???' 5:41 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 41 41 14'): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:41:65 آخِر 'degil' — 'fi'l-âxirati 'azâbun 'azîm', kural ''fi'l-âxira' emsali → degil' (âhiret) (esma_el_ekle → esma_kayit; bölüm 6 kuralı 14: eş yapılı önceki kayıtların emsali, genel kural yazılmadı); lafız 5:41 (43., 49. ve 55. kelime); Rab yok",
 "esma_kayit: 5:41 'mühür EVET ton denge' (ölçüm MÜHÜRSÜZ — uyuşmuyor; esmâ göndergesi âhiret, 'degil')",
 "ölçüm: 5:41 '{{1|biçim DIKKAT \\+ NEHY}}', '{{1|EDİLGEN 2/17 fiil, pas z=0,34}}', '{{1|fâsıla عظيم → م, N sınıfı}}', '{{1|simetri \\[6, 5, 33, 2\\]}}', '{{1|harf 298 → harf3 279, isaret 19}}', '{{1|dış düğüm 3}}' ve '{{1|İÇ düğüm 1}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 41 41 14'): KALAN_P",
 "ölçüm aktör: 5:41 aktör yok (ölçüm); 'r-rasûlu' münâdâ, 'llezîne' (5., 10., 18. ve 52. kelime) ism-i mevsûl, adsız",
 "ölçüm edim / kip (D2 ölçüm etiketiyle): 5:41 emir, yasak, nida, şart — IMPV 2 'fe-xuzûhu' (36.), 'fa'hzerû' (40.); PRO 1 'lâ' (3.); VOC 1 'yâ' (1.); COND 3 'in' (33., 37.), 'men' (41.); NEG 5 'lem' (14., 25., 38., 53.), 'len' (45.); EDİLGEN 2 'ûtîtum' (34.), 'tu'tevhu' (39.); biçim DIKKAT + NEHY",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 5:41 ★★★ (kaynak n, z=5,80)",
 "fâsıla: 5:40 ر (قدير) → 5:41 م (عظيم) — bölüm açılışında م'ye dönüş; N sınıfı; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref: 5:41 48:11 ve 5:17 (basılmış), 2:114 ve 3:176 (emsal olarak basıldı)",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:41 'fî âxir 'azâb 'azîm' süzgeç GEÇER; 'min ellezî qâle', 'min allâh şey'' ve 'erâde allâh en' GEÇMEZ",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15 — ölçüt: 1P / 1S / 2MS / 2FS / 2MP / 2FP / 2D / 3MS / 3FS / 3D / 3MD / 3FD / 3MP / 3FP zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 'lafız' / 'gönderge lafız' ölçüt yerine geçmez): "
 "5:41 muhatap 2MS (adsız — 'yahzunke', 'ye'tûk', 'temlike'), 3MP (adsız — 'yusâri'ûne', 'qâlû', 'hâdû', 'ye'tûk', 'yuharrifûne', 'yeqûlûne' failleri; iyelik 13., 16., 58. kelime; 'lehum'), söz içi 1P (adsız — 'âmennâ'), 3FS (adsız — 'tu'min'), söz muhatabı 2MP (adsız), 3MS (adsız — 'yuridi', 'yutahhira' failleri; 'mevâdi'ih', 'fitneteh', 'lehû', 'hu'), Allah (lafız), 'men', 'hâzâ', 'ulâ'ike', 'qavmin âxarîne', 'xizyun', ''azâbun 'azîm' — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): 'qâlû' sözü 'âmennâ' (söz içi, 12-12. kelime); 'yeqûlûne' sözü 'in ûtîtum hâzâ' ile açılan söz (33-40. kelime); söz içi 1P ve söz muhatabı 2MP 'adsız'; REM sapması (komut 'python3 sunum/bolum4_kurallar.py 41 41 14' — A3 aralığında morph REM): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 've lem' (14.), 've men' (41.) REM; 've mine' (17.), 've in' (37.), 've lehum' (63.) CONJ; 'fe-xuzûhu' (36.), 'fa'hzerû' (40.), 'fe-len' (45.) RSLT",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 5:41 ◈B قلب ('qulûbuhum' 16. kelime, 'qulûbehum' 58. kelime — B3; anlam notu: iman etmeyen kalpler / temizlenmeyen kalpler); ◈K yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 41 41 14'; aday kökler, gloss türevli adaylar ve morph T isimleri): TETIKDISI; anılış: 5:41 kök فوه ('bi-efvâhihim' 13. kelime — ağız, beden; B3 alanına yakın, tetik dışı); "
 "بعد ('ba'di' 30. kelime — 'sonra'); دنو ('d-dunyâ' 61. kelime — dünya, zaman / yurt); أخر ('l-âxirati' 65. kelime — âhiret; 'âxarîne' 24. kelime — başka); عظم (''azîm' 67. kelime — 'büyük'; kemik anlamında değil); oturum_tetik kuru koşu 1 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:41 (2:114, 3:176, 4:28, 9:47) (kontrol.py ile); blok geçişi 5:40 → 5:41 bölüm geçişi — ardışık bağ kurulmadı; D3 dışı bırakılan basılmış sayım eşleri: 'mina'llâhi şey'â' 5:17, 48:11; 'fi'l-âxirati 'azâbun 'azîm' 5:33; 'yuharrifûne'l-kelim' 4:46, 5:13; 'qâlû âmennâ' 3:119; 'ulâ'ike'llezîne' 49:3 — "
 "kalıp başına ölçüt: geniş nakarat kalıbı ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11); 5:33 ve 5:41 'fi'l-âxirati 'azâbun 'azîm' eşliği R5'te",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:41 bölüm açılışı; hitap açılır ('yâ eyyuhe'r-rasûl', 1-2. kelime); edim geçişi soru → emir, yasak, nida, şart; şahıs geçişi yok; şart → cevap (ayet içi; COND 'in' 33. kelime: 'in ûtîtum hâzâ' / 'fe-xuzûhu' (36. kelime)); şart → cevap (ayet içi; COND 'in' 37. kelime: 've in lem tu'tevhu' / 'fa'hzerû' (40. kelime)); "
 "şart → cevap (ayet içi; COND 'men' 41. kelime: 've men yuridi'llâhu fitnetehû' / 'fe-len temlike lehû mina'llâhi şey'â' (45. kelime))",
 "sözdizimi (okuma; morph etiketiyle): 5:41 'yâ eyyuhe'r-rasûl' — nidâ (morph VOC + ATT); 'lâ yahzunke' — yasak (morph PRO), faili 'llezîne yusâri'ûne'; 'mine'llezîne qâlû … ve mine'llezîne hâdû' — 'llezîne'nin açıklaması (morph P 'min'); 've lem tu'min' — istînâf (morph REM); 'semmâ'ûne' — mübtedası takdirli isim cümlesi (morph etiketi yok, okuma); "
 "'in ûtîtum … fe-xuzûhu' ve 've in lem tu'tevhu fa'hzerû' — şart / cevap (morph COND / RSLT); 've men yuridi'llâhu … fe-len temlike' — şart / cevap (morph REM + COND / RSLT); 'ulâ'ike'llezîne' — işaret + ism-i mevsûl; 'lehum fi'd-dunyâ xizyun' — isim cümlesi",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:41 'yâ eyyuhe'r-rasûl' ile açılıyor (1-2. kelime); kök أمن iki geçiş — 'âmennâ' (12. kelime, söz) / 'tu'min' (15. kelime, kalp); kök قلب iki geçiş (16. ve 58. kelime); kök رود iki geçiş (42. ve 54. kelime) — Allah'ın istemesi; kök أتي üç geçiş (26., 34., 39. kelime); "
 "5:41 en uzun ayet (n=67, n z=5,80); 'lehum fi'd-dunyâ xizyun ve lehum fi'l-âxirati 'azâbun 'azîm' dünya / âhiret karşıtlığı (basılmış eşi 2:114 — sayımın basılmış kümesinden); ayetler arası kalıp alıntısı yok",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 14'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + "'; çıktı aynen): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle): 'lâ yahzunke'llezîne yusâri'ûne' 5:41 'küfürde yarışanlar seni üzmesin' / 3:176 'İnkârda koşuşanlar seni üzmesin' ('kufr' 'küfür' / 'inkâr'; 'yusâri'u' 'yarış-' / 'koşuş-' — farklı); 'lehum fi'd-dunyâ xizyun' 5:41 'dünyada bir rezillik' / 2:114 'dünyada rezillik' (eş); "
 "'semmâ'' 5:41 'çokça kulak veren' / 9:47 (karşılık meal metninde) — tam okuma sonu; 'erâde allâh en' 5:41 'Allah'ın … istemediği' / 4:28 'Allah … ister' (eş)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 41 41 14'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:41 tarayıcı adayı yok (cipa_tarama5_adaylari.json); elçiye hitap, teselli — çıpa değil (olgu=False); L3 / L4 adayı yok",
 "aday 1039: ayet içi 5:41 ('âmennâ bi-efvâhihim' / 've lem tu'min qulûbuhum'; 'fe-xuzûhu' / 'fa'hzerû'; 'lehum fi'd-dunyâ xizyun' / 've lehum fi'l-âxirati 'azâbun 'azîm') — okuma; ayetler arası yok; eşleme betikle: ADAY_P",
 "aday 1041: kök رسل 5:41 'r-rasûlu' — elçiye doğrudan hitap; kök رود 5:41 'yuridi'llâh' (42. ve 54. kelime) — Allah'ın istemesi, fitne ve kalplerin temizlenmesi; kök أمن 5:41 insan (söz ile kalp ayrımı) — okuma",
 "bölüm: " + BOL + " bölümü, bölüm 7-1 — bölüm açılışı 5:41; bölüm dört blok (blok planından: 14, 15, 16, 17); başlıktaki 'küfürde yarışanlar' 5:41 ('yusâri'ûne fi'l-kufr'); 'Tevrat, İncil ve Kitap ile hüküm' sonraki bloklarda; bölüm 6 denetimi bulguları ve yeni kuralları bu ARIZA'nın başında; "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b14/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3 — betikle: komut 'python3 sunum/bolum5_kurallar.py 41 41 14'; lem_bozuk.py 14 çıktısı): 5:41:4 'yahzun', 5:41:6 'yusâri'u', 5:41:19 'hâdu', 5:41:27 'yuharrifu', 5:41:40 'yahzeru', 5:41:46 'meleket' — lem_bozuk bayrağı; meal maddesinde '(morph LEM ham biçim)' notlu; lemma adı listesinde notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 41 41 → AYN_SONUC; sunum/bolum4_kurallar.py 41 41 14 → KHATA_HEPSI; sunum/bolum5_kurallar.py 41 41 14 → B5_HEPSI; sunum/bolum6_kurallar.py 41 41 14 → B6_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; bekleyen kopyası bayt eşit (değişiklik yok); yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (sunum/sonradan.py --plan 14): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('rasûl', 'yahzun' (morph LEM ham biçim), 'yusâri'u' (morph LEM ham biçim), 'kufr', 'qâle', 'âmene', 'efvâh', 'qalb', 'hâdu' (morph LEM ham biçim), 'semmâ'', 'kezib', 'qavm', 'âxar', 'etâ', 'yuharrifu' (morph LEM ham biçim), 'kelim', 'ba'd', 'mevâdi'', 'âtâ', 'exaze', 'yahzeru' (morph LEM ham biçim), 'erâde', 'fitne', 'meleket' (morph LEM ham biçim), 'şey'', 'tahhara', 'dunyâ', 'xizy', 'âxir', ''azâb', ''azîm'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (41, 41): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_41_41.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_5_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for blok in MEALS for m in re.finditer(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", blok)}  # bölüm 6 kuralı 2: hemze ile biten ad dahil
KARAR = {}
for nn in ('06', '10', '11', '12', '13', '14'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()
GERI = open('/home/claude/yamalar/geriye_donuk_5_b13.txt', encoding='utf-8').read().splitlines()[:2]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    AYN = (run('/home/claude/sunum/ayn_kontrol.py', '41', '41').splitlines() or ['?'])[-1]
    KUR = run('/home/claude/sunum/bolum4_kurallar.py', '41', '41', '14').splitlines()
    KH = [l for l in KUR if l.startswith('HATA')]
    B5 = run('/home/claude/sunum/bolum5_kurallar.py', '41', '41', '14').splitlines()
    B5H = [l for l in B5 if l.startswith('HATA')]
    B6 = run('/home/claude/sunum/bolum6_kurallar.py', '41', '41', '14', '--tazelik-yok').splitlines()
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'),
           'MUT_SONUC': (MUT[-1] if MUT else '?'), 'GERI_P': ' / '.join(x.lstrip('# ') for x in GERI)}
    I_cur = list(I_HAM)
    for k, v in REP.items(): I_cur = [x.replace(k, v) for x in I_cur]
    I_cur[idx] = ("karşılık çakışması (bölüm 4 kuralı 4, bölüm 5 kuralı 3, bölüm 6 kuralı 2 — komut 'python3 sunum/cakisma.py' + sûre 5'in okunmuş bütün ARIZA dosyaları; bu bloğun karşılıklarına dokunan gruplar ve son dosyaya dokunan KÖK grupları; grup başına tam bir kapalı karar: 'çakışma değil' ya da 'çakışma — tam okuma sonu'): "
                  + ('; '.join(KARAR.get(l.split(' ←')[0].strip() if not l.startswith('KÖK') else 'KÖK ' + l.split()[1], l + ' — karar yok') for l in CAK_L) if CAK_L else 'bu bloğa dokunan çakışma yok'))
    if I_cur == onceki: break
    onceki = list(I_cur)
yaz(I_cur)
print('yazıldı', len(I_cur), 'tur', tur)
print('\n'.join(CAK_L))
print(GLS); print(KUR); print(B5); print(B6)

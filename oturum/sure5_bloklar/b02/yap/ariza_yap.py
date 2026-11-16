# blok 2 (5:3-4) ARIZA oluşturucu — bölüm 1-2 (bölüm kapanışı)
import sys, os, ast, subprocess
os.environ['OLC'] = '/home/claude/b02/olcum.txt'
os.environ['SAY2'] = '/home/claude/b02/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

VF_YAZI = {3: {4: "'ve'd-demu'", 5: "'ve lahmu'", 7: "'ve mâ'", 12: "'ve'l-munxaniqatu'", 13: "'ve'l-mevqûzetu'", 14: "'ve'l-muteraddiyetu'", 15: "'ve'n-natîhatu'", 16: "'ve mâ'", 22: "'ve mâ'", 26: "'ve en'", 37: "'fe-lâ'", 39: "'va'xşevni'", 44: "'ve etmemtu'", 47: "'ve radîtu'", 51: "'fe-meni'", 58: "'fe-inna'"},
           4: {9: "'ve mâ'", 18: "'fe-kulû'", 22: "'ve'zkurû'", 26: "'ve'ttequ'"}}

BOL = "'Ahitlere vefa; haram kılınanlar; dinin tamamlanması; helal yiyecekler'"


def sic(key):
    n, d = sayim.S2[key]
    return 1 + len([x for x in d['basilan'] if x.startswith('5:')]) + d['okunmus_si'] + d['henuz_si']


def taban(key, ay):
    n, d = sayim.S2[key]
    p = [ay] + [x for x in d['basilan'] if x.startswith('5:')]
    if d['okunmus_si']: p.append('okunmus_si')
    if d['henuz_si']: p.append('henuz_si')
    return ' + '.join(p)


R5 = [
 ("5:3", "'allâh ğafûr rahîm'", 5, 'say 5:3 59-61', "harekesiz 'llâhe ğafûrun rahîm' (59-61. kelime)", ('dizi 5 3 59 61', "allâh ğafûr rahîm", '59-61', "biçim / i'râb farkı — harekesiz kalıp lafzın mansub yazımını ayırıyor")),
 ("5:3", "'ellezî kefere min'", 2, 'say 5:3 33-35', "harekesiz 'llezîne keferû min' (33-35. kelime)", None),
 ("5:4", "'itteqâ allâh inne allâh'", 4, 'say 5:4 26-29 --on', "önek kesilmiş 've'ttequ'llâhe inna'llâh' (26-29. kelime)", None),
 ("5:4", "'itteqâ allâh inne'", 6, 'say 5:4 26-28 --on', "önek kesilmiş 've'ttequ'llâhe inne' (26-28. kelime)", ('dizi 5 4 26 28', "itteqâ allâh inne", '26-28', None)),
 ("5:4", "'ehalle lekum tayyibe'", 2, 'say 5:4 6-8', "harekesiz 'uhille lekumu't-tayyibât' (6-8. kelime)", None),
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
            h += (" — tutmuyor; eşit aralıkla lemma dizisi '%s' (%s. kelime) sûre içi %d (%s) — olası neden: nakarat3 'ان' kök anahtarı 'inne' / 'enne' / 'en' "
                  "biçimlerini birleştiriyor; nakarat3'ün fazla sûre içi eşleri okunmamış (fark test edilmedi)" % (dad, dar, ds, taban(dk, ay)))
    r5.append(h)

K1 = ['say 5:3 1-3', 'say 5:3 31-34', 'say 5:3 33-36', 'say 5:3 37-39 --on', 'say 5:3 38-39', 'say 5:3 40-43', 'say 5:3 44-46 --on', 'say 5:3 47-50 --on', 'say 5:3 51-54 --on',
      'say 5:3 16-18 --on', 'say 5:3 19-21', 'say 5:3 22-25 --on', 'say 5:3 26-28 --on', 'say 5:3 29-30', 'say 5:3 55-57',
      'lem 5:3:12', 'lem 5:3:13', 'lem 5:3:14', 'lem 5:3:15', 'lem 5:3:18', 'lem 5:3:21', 'lem 5:3:56',
      'say 5:4 1-2', 'say 5:4 1-4', 'say 5:4 3-4', 'say 5:4 5-8', 'say 5:4 9-12 --on', 'lem 5:4:12', 'lem 5:4:13', 'say 5:4 14-17', 'say 5:4 15-17',
      'say 5:4 18-21 --on', 'say 5:4 18-19 --on', 'say 5:4 22-24 --on', 'say 5:4 22-25 --on']
AD = {'say 5:3 1-3': "harekesiz 'hurrimet 'aleykumu'l-meyte'", 'say 5:3 31-34': "harekesiz 'el-yevme ye'ise'llezîne keferû'", 'say 5:3 33-36': "harekesiz 'llezîne keferû min dînikum'",
      'say 5:3 37-39 --on': "önek kesilmiş 'fe-lâ taxşevhum va'xşevn'", 'say 5:3 38-39': "harekesiz 'taxşevhum va'xşevn'", 'say 5:3 40-43': "harekesiz 'el-yevme ekmeltu lekum dînekum'",
      'say 5:3 44-46 --on': "önek kesilmiş 've etmemtu 'aleykum ni'metî'", 'say 5:3 47-50 --on': "önek kesilmiş 've radîtu lekumu'l-islâme dînâ'", 'say 5:3 51-54 --on': "önek kesilmiş 'fe-meni'dturra fî maxmasa'",
      'say 5:3 16-18 --on': "önek kesilmiş 've mâ ekele's-sebu''", 'say 5:3 19-21': "harekesiz 'illâ mâ zekkeytum'", 'say 5:3 22-25 --on': "önek kesilmiş 've mâ zubiha 'ale'n-nusub'",
      'say 5:3 26-28 --on': "önek kesilmiş 've en testaqsimû bi'l-ezlâm'", 'say 5:3 29-30': "harekesiz 'zâlikum fisq'", 'say 5:3 55-57': "harekesiz 'ğayra mutecânifin li-ism'",
      'lem 5:3:12': "lemma 'munxaniqa'", 'lem 5:3:13': "lemma 'mevqûze'", 'lem 5:3:14': "lemma 'muteraddiye'", 'lem 5:3:15': "lemma 'natîha'", 'lem 5:3:18': "lemma 'sebu''",
      'lem 5:3:21': "lemma 'zekkey'", 'lem 5:3:56': "lemma 'mutecânif'",
      'say 5:4 1-2': "harekesiz 'yes'elûneke mâzâ'", 'say 5:4 1-4': "harekesiz 'yes'elûneke mâzâ uhille lehum'", 'say 5:4 3-4': "harekesiz 'uhille lehum'", 'say 5:4 5-8': "harekesiz 'qul uhille lekumu't-tayyibât'",
      'say 5:4 9-12 --on': "önek kesilmiş 've mâ 'allemtum mine'l-cevârih'", 'lem 5:4:12': "lemma 'cevârih'", 'lem 5:4:13': "lemma 'mukellib'", 'say 5:4 14-17': "harekesiz 'tu'allimûnehunne mimmâ 'allemekumu'llâh'",
      'say 5:4 15-17': "harekesiz 'mimmâ 'allemekumu'llâh'", 'say 5:4 18-21 --on': "önek kesilmiş 'fe-kulû mimmâ emsekne 'aleykum'", 'say 5:4 18-19 --on': "önek kesilmiş 'fe-kulû mimmâ'",
      'say 5:4 22-24 --on': "önek kesilmiş 've'zkuru'sma'llâh'", 'say 5:4 22-25 --on': "önek kesilmiş 've'zkuru'sma'llâhi 'aleyh'"}
assert all(sayim.S2[k][0] == 1 for k in K1), [k for k in K1 if sayim.S2[k][0] != 1]
k1 = [AD[k] for k in K1]

MEAL3 = ("5:3 'Ölü hayvan, kan, domuz eti … size haram kılındı' ('hurrimet 'aleykumu'l-meytetu ve'd-demu ve lahmu'l-xinzîr', 'haram kıl-' 'hurrimet' açılımı (1. kelime; II. bab; edilgen — mealde edilgen; 'kıl-' açılım takdiri), "
 "''alâ' 2. kelimede '-e' ile (fiil yönetimi takdiri), 'kum' 2. kelimede 'siz' ile, 'ölü hayvan' 'meyte' açılımı (3. kelime; 'hayvan' açılım takdiri), 've' 4. kelimede karşılıksız (virgül; morph CONJ), "
 "'kan' 'dem' karşılığı (4. kelime), 've' 5. kelimede karşılıksız (virgül; morph CONJ), 'et' 'lahm' karşılığı (5. kelime), 'domuz' 'xinzîr' karşılığı (6. kelime; izafet), sıralama: nâib fâil dizisi öne, fiil sona alındı); "
 "'Allah'tan başkasının adı anılarak kesilen' ('ve mâ uhille li-ğayri'llâhi bihî', 've' 7. kelimede karşılıksız (virgül; morph CONJ), 'mâ' 7. kelimede '-en' ile, 'adı anılarak kesil-' 'uhille' açılımı (8. kelime; IV. bab; edilgen; kök tablosu karşılığı), "
 "'li' 9. kelimede '-ın' ile, 'başka' 'ğayr' karşılığı (9. kelime), lafız 10. kelimede 'Allah'tan' ile ('-tan' fiil yönetimi takdiri), 'bi' 11. kelimede karşılıksız, 'hî' 11. kelimede karşılıksız ('kesilen' içinde)); "
 "'boğularak ölmüş, vurularak ölmüş, yuvarlanarak ölmüş, boynuzlanarak ölmüş' ('ve'l-munxaniqatu ve'l-mevqûzetu ve'l-muteraddiyetu ve'n-natîhatu', 've' 12., 13., 14. ve 15. kelimede karşılıksız (virgül; morph CONJ), "
 "'boğularak öl-' 'munxaniqa' açılımı (12. kelime; ortaç; 'öl-' açılım takdiri), 'vurularak öl-' 'mevqûze' açılımı (13. kelime; edilgen ortaç), 'yuvarlanarak öl-' 'muteraddiye' açılımı (14. kelime; ortaç), "
 "'boynuzlanarak öl-' 'natîha' açılımı (15. kelime), '-miş' takdir (12-15. kelime; ortaç sıfatın durum biçimi)); "
 "'ve yırtıcı hayvanın yediği' ('ve mâ ekele's-sebu'', 've' 16. kelimede 've' ile, 'mâ' 16. kelimede '-diği' ile, 'ye-' 'ekele' karşılığı (17. kelime), 'yırtıcı hayvan' 'sebu'' açılımı (18. kelime; 'hayvan' açılım takdiri; '-ın' takdir)); "
 "'kesip temizledikleriniz dışında' ('illâ mâ zekkeytum', 'illâ' 19. kelimede 'dışında' ile, 'mâ' 20. kelimede '-dikleriniz' ile, 'kesip temizle-' 'zekkeytum' açılımı (21. kelime; II. bab; 'kesip' açılım takdiri), 'tum' 21. kelimede karşılıksız ('-dikleriniz' içinde)); "
 "'dikili taşlar üzerinde boğazlanan' ('ve mâ zubiha 'ale'n-nusub', 've' 22. kelimede karşılıksız (virgül; morph CONJ), 'mâ' 22. kelimede '-an' ile, 'boğazla-' 'zubiha' karşılığı (23. kelime; edilgen — mealde edilgen), "
 "''alâ' 24. kelimede 'üzerinde' ile, 'dikili taş' 'nusub' açılımı (25. kelime; çoğul '-lar')); "
 "'ve fal oklarıyla kısmet aramanız' ('ve en testaqsimû bi'l-ezlâm', 've' 26. kelimede 've' ile, 'en' 26. kelimede '-manız' ile (masdar), 'kısmet ara-' 'testaqsimû' açılımı (27. kelime; X. bab; 'kısmet' açılım takdiri), "
 "'û' 27. kelimede karşılıksız ('-manız' içinde), 'bi' 28. kelimede '-la' ile, 'fal okları' 'ezlâm' karşılığı (28. kelime; kök tablosu karşılığı)); "
 "'Bunlar yoldan çıkmaktır' ('zâlikum fisq', 'bu' 'zâlikum' karşılığı (29. kelime; tekil — '-lar' takdiri), 'yoldan çıkmak' 'fisq' açılımı (30. kelime; nekre — 'bir' takdiri yok), '-tır' takdir (30. kelime)); "
 "'Bugün inkâr edenler dininizden ümit kesti' ('yevme ye'ise'llezîne keferû min dînikum', 'bugün' 'yevm' açılımı (31. kelime; belirli — 'bu' açılım takdiri), 'ümit kes-' 'ye'ise' açılımı (32. kelime; 'ümit' açılım takdiri), "
 "'ellezîne' 33. kelimede '-enler' ile, 'inkâr et-' 'keferû' karşılığı (34. kelime), 'û' 34. kelimede karşılıksız (fail eki — '-enler' içinde), 'min' 35. kelimede '-den' ile, 'din' 'dîn' karşılığı (36. kelime), 'kum' 36. kelimede '-iniz' iyelik ile, sıralama: fiil sona alındı); "
 "'öyleyse onlardan korkmayın, benden korkun' ('fe-lâ taxşevhum va'xşevni', 'fe' 37. kelimede 'öyleyse' ile (morph REM), 'lâ' 37. kelimede '-ma-' ile, 'kork-' 'taxşevhum' karşılığı (38. kelime), 'û' 38. kelimede '-yın' ile, "
 "'hum' 38. kelimede 'onlardan' ile ('-dan' fiil yönetimi takdiri), 've' 39. kelimede karşılıksız (virgül; morph CONJ), 'kork-' 'xşevni' karşılığı (39. kelime; emir), 'û' 39. kelimede '-un' ile, 'ni' 39. kelimede 'benden' ile ('-den' fiil yönetimi takdiri)); "
 "'Bugün dininizi sizin için tamamladım' ('yevme ekmeltu lekum dînekum', 'bugün' 'yevm' açılımı (40. kelime; 'bu' açılım takdiri), 'tamamla-' 'ekmeltu' karşılığı (41. kelime; IV. bab), 'tu' 41. kelimede '-dım' ile, "
 "'li' 42. kelimede 'için' ile, 'kum' 42. kelimede 'sizin' ile, 'din' 'dîn' karşılığı (43. kelime), 'kum' 43. kelimede '-iniz' iyelik ile, sıralama: fiil sona alındı); "
 "'üzerinizdeki nimetimi tamamladım' ('ve etmemtu 'aleykum ni'metî', 've' 44. kelimede karşılıksız (virgül; morph CONJ), 'tamamla-' 'etmemtu' karşılığı (44. kelime; IV. bab), 'tu' 44. kelimede '-dım' ile, "
 "''alâ' 45. kelimede 'üzerinde' ile ('-ki' takdir), 'kum' 45. kelimede '-iniz' iyelik ile, 'nimet' 'ni'me' karşılığı (46. kelime), 'î' 46. kelimede '-im' iyelik ile, sıralama: fiil sona alındı); "
 "'ve sizin için din olarak İslâm'ı beğendim' ('ve radîtu lekumu'l-islâme dînen', 've' 47. kelimede 've' ile, 'beğen-' 'radîtu' karşılığı (47. kelime; kök tablosu 'razı olma'), 'tu' 47. kelimede '-dim' ile, 'li' 48. kelimede 'için' ile, "
 "'kum' 48. kelimede 'sizin' ile, 'İslâm' 'islâm' karşılığı (49. kelime; '-ı' belirtme), 'din' 'dîn' karşılığı (50. kelime; nekre), 'olarak' takdir (50. kelime; temyîz / hâl okuması), sıralama: fiil sona alındı); "
 "'Kim günaha meyletmeksizin açlık içinde zorda kalırsa' ('fe-meni'dturra fî maxmasatin ğayra mutecânifin li-ism', 'fe' 51. kelimede karşılıksız (nokta; morph REM), 'men' 51. kelimede 'kim … -sa' ile, "
 "'zorda kal-' 'dturra' açılımı (52. kelime; VIII. bab; edilgen — mealde etken 'kal-'), 'fî' 53. kelimede 'içinde' ile, 'açlık' 'maxmasa' karşılığı (54. kelime; nekre), 'ğayr' 55. kelimede '-meksizin' ile, "
 "'meylet-' 'mutecânif' karşılığı (56. kelime; ortaç), 'li' 57. kelimede '-a' ile ('-a' fiil yönetimi takdiri), 'günah' 'ism' karşılığı (57. kelime; nekre), sıralama: durum öne, fiil sona alındı); "
 "'şüphesiz Allah bağışlayandır, merhamet edendir' ('fe-inna'llâhe ğafûrun rahîm', 'fe' 58. kelimede karşılıksız (cevap; morph RSLT), 'inne' 58. kelimede 'şüphesiz' ile, lafız 59. kelimede 'Allah' ile, "
 "'bağışlayan' 'ğafûr' karşılığı (60. kelime), '-dır' takdir (60. kelime), 'merhamet eden' 'rahîm' açılımı (61. kelime; 'et-' açılım takdiri), '-dir' takdir (61. kelime))")
MEAL4 = ("5:4 'Sana kendileri için neyin helâl kılındığını soruyorlar' ('yes'elûneke mâzâ uhille lehum', 'sor-' 'yes'elûneke' karşılığı (1. kelime), 'ûne' 1. kelimede '-lar' ile, 'ke' 1. kelimede 'sana' ile ('-a' fiil yönetimi takdiri), "
 "'mâzâ' 2. kelimede 'neyin' ile, 'helâl kıl-' 'uhille' açılımı (3. kelime; IV. bab; edilgen — mealde edilgen), '-dığını' takdir (3. kelime; soru içeriğinin yan cümle biçimi), 'li' 4. kelimede 'için' ile, 'hum' 4. kelimede 'kendileri' ile, sıralama: fiil sona alındı); "
 "'De ki' ('qul', 'de-' 'qul' karşılığı (5. kelime), 'ki' takdir (5. kelime; söz açılışı)); "
 "'Size temiz şeyler helâl kılındı' ('uhille lekumu't-tayyibât', 'helâl kıl-' 'uhille' açılımı (6. kelime; edilgen — mealde edilgen), 'li' 7. kelimede '-e' ile ('-e' fiil yönetimi takdiri), 'kum' 7. kelimede 'siz' ile, "
 "'temiz şey' 'tayyibe' açılımı (8. kelime; çoğul '-ler'; 'şey' açılım takdiri), sıralama: fiil sona alındı); "
 "'yırtıcı hayvanlardan, Allah'ın size öğrettiğinden onlara öğreterek avcı olarak eğittiklerinizin avı da' ('ve mâ 'allemtum mine'l-cevârihi mukellibîne tu'allimûnehunne mimmâ 'allemekumu'llâh', "
 "'ve' 9. kelimede 'da' ile (morph CONJ), 'mâ' 9. kelimede '-dikleriniz' ile, 'eğit-' ''allemtum' karşılığı (10. kelime; II. bab), 'tum' 10. kelimede karşılıksız ('-dikleriniz' içinde), 'min' 11. kelimede '-dan' ile, "
 "'yırtıcı hayvan' 'cevârih' açılımı (12. kelime; çoğul '-lar'; kök tablosu 'avcı hayvan'), 'avcı olarak' 'mukellibîne' açılımı (13. kelime; ortaç; 'olarak' takdir), 'öğret-' 'tu'allimûnehunne' karşılığı (14. kelime; II. bab; '-erek'), "
 "'ûne' 14. kelimede karşılıksız (fail eki — '-erek' içinde), 'hunne' 14. kelimede 'onlara' ile ('-a' fiil yönetimi takdiri), 'min' 15. kelimede '-den' ile, 'mâ' 15. kelimede '-diği' ile, 'öğret-' ''allemekumu' karşılığı (16. kelime), "
 "'kum' 16. kelimede 'size' ile ('-e' fiil yönetimi takdiri), lafız 17. kelimede 'Allah'ın' ile ('-ın' takdir), 'av' takdir (9. kelime; 'mâ' göndergesinin açılımı), '-ı' iyelik takdiri (izafet; 'avı'), sıralama: ortaç tümleçleri öne alındı); "
 "'Onların sizin için tuttuklarından yiyin' ('fe-kulû mimmâ emsekne 'aleykum', 'fe' 18. kelimede karşılıksız (nokta; morph REM), 'ye-' 'kulû' karşılığı (18. kelime; emir), 'û' 18. kelimede '-in' ile, "
 "'min' 19. kelimede '-dan' ile, 'mâ' 19. kelimede '-dukları' ile, 'tut-' 'emsekne' karşılığı (20. kelime; IV. bab), 'ne' 20. kelimede 'onların' ile, ''alâ' 21. kelimede 'için' ile, 'kum' 21. kelimede 'sizin' ile, sıralama: fiil sona alındı); "
 "'ve üzerine Allah'ın adını anın' ('ve'zkuru'sma'llâhi 'aleyh', 've' 22. kelimede 've' ile, 'an-' 'zkurû' karşılığı (22. kelime; emir), 'û' 22. kelimede '-ın' ile, 'ad' 'ism' karşılığı (23. kelime; '-ı' iyelik, '-nı' belirtme), "
 "lafız 24. kelimede 'Allah'ın' ile ('-ın' takdir — izafet), ''alâ' 25. kelimede 'üzerine' ile, 'hi' 25. kelimede '-i' iyelik ile ('üzerine' içinde), sıralama: fiil sona alındı); "
 "'Allah'tan sakının' ('ve'ttequ'llâh', 've' 26. kelimede karşılıksız (nokta; morph CONJ), 'sakın-' 'ttequ' karşılığı (26. kelime; VIII. bab), 'û' 26. kelimede '-ın' ile, lafız 27. kelimede 'Allah'tan' ile ('-tan' fiil yönetimi takdiri)); "
 "'Şüphesiz Allah hesabı çabuk görendir' ('inna'llâhe serî'u'l-hisâb', 'inne' 28. kelimede 'şüphesiz' ile, lafız 29. kelimede 'Allah' ile, 'çabuk gören' 'serî'' açılımı (30. kelime; 'gören' açılım takdiri), "
 "'hesap' 'hisâb' karşılığı (31. kelime; masdar; '-ı' belirtme — izafet açılımı), '-dir' takdir (30. kelime), sıralama: haber izafeti çözüldü)")
ES = ("blok içi eş edat / lemma karşılıkları (karşılık seçimi tam okuma sonu): 've' — 've' ile (5:3 16., 26., 47. kelime; 5:4 22. kelime), 'da' ile (5:4 9. kelime), karşılıksız (5:3 4., 5., 7., 12., 13., 14., 15., 22., 39., 44. kelime; 5:4 26. kelime); "
 "'fe' — 'öyleyse' ile (5:3 37. kelime), karşılıksız (5:3 51., 58. kelime; 5:4 18. kelime); ''alâ' — '-e' ile (5:3 2. kelime), 'üzerinde' ile (5:3 24., 45. kelime), 'için' ile (5:4 21. kelime), 'üzerine' ile (5:4 25. kelime); "
 "'li' — '-ın' ile (5:3 9. kelime), 'için' ile (5:3 42., 48. kelime; 5:4 4. kelime), '-a' ile (5:3 57. kelime), '-e' ile (5:4 7. kelime); 'min' — '-den' ile (5:3 35. kelime; 5:4 15. kelime), '-dan' ile (5:4 11., 19. kelime); "
 "'mâ' — '-en' ile (5:3 7. kelime), '-diği' ile (5:3 16. kelime; 5:4 15. kelime), '-dikleriniz' ile (5:3 20. kelime; 5:4 9. kelime), '-an' ile (5:3 22. kelime), '-dukları' ile (5:4 19. kelime); "
 "'kum' — 'siz' (5:3 2. kelime; 5:4 7. kelime), 'sizin' (5:3 42., 48. kelime; 5:4 21. kelime), 'size' (5:4 16. kelime), '-iniz' (5:3 36., 43., 45. kelime); "
 "lemma 'harrame' 'haram kıl-' (5:3 1. kelime) / lemma 'ehalle' 'helâl kıl-' (5:4 3., 6. kelime; blok 1'de 'helâl say-' karşılığı da var — 5:2 5. kelime); lemma 'uhille' (5:3 8. kelime) 'adı anılarak kesil-' — kök هلل; lemma 'ehalle' kök حلل — ayrı lemmalar; "
 "lemma 'xaşiye' 'kork-' (5:3 38., 39. kelime); lemma 'dîn' 'din' (5:3 36., 43., 50. kelime); lemma 'yevm' 'bugün' (5:3 31., 40. kelime)")


KARAR = {
 'helâl kıl-': "'helâl kıl-' ← 'uhille', 'uhillet': bir lemma ('ehalle'; morph LEM eşit — 5:1 'uhillet', 5:4 'uhille') — çakışma değil",
 'helâl say-': "'helâl say-' ← 'muhilli', 'tuhillû': farklı lemma, bir kök (حلل) — 'muhillî' (ortaç, 5:1) ve 'ehalle' (5:2); karşılık seçimi tam okuma sonu",
 'kork-': "'kork-' ← 'taxşevhum', 'xşevni': bir lemma ('xaşiye'; morph LEM eşit) — çakışma değil",
 'tamamla-': "'tamamla-' ← 'ekmeltu', 'etmemtu': farklı lemma ve kök — 'ekmel' (كمل) ve 'etemme' (تمم), 5:3; karşılık seçimi tam okuma sonu",
 'ye-': "'ye-' ← 'ekele', 'kulû': bir lemma ('ekele'; morph LEM eşit — 5:3 'ekele', 5:4 'kulû') — çakışma değil",
 'öğret-': "'öğret-' ← ''allemekumu', 'tu'allimûnehunne': bir lemma (''alleme'; morph LEM eşit) — çakışma değil",
}


def cakisma():
    out = subprocess.run([sys.executable, '/home/claude/sunum/cakisma.py', '/home/claude/yamalar/ariza_5_1_2.txt', '/home/claude/yamalar/ariza_5_3_4.txt'], capture_output=True, text=True).stdout.strip()
    return out


I = [
 "kök tablosu: ölçümde '???' 5:3 ve 5:4 için ayrı sayıldı (yama öncesi koşuda 5:3 9 — beş kök; 5:4 0); beş yeni kök — خنق, وقذ, نطح, ذكو, زلم — yamalar/yama_kok_5_3.py → kok_ekle_5.py → kok_turkce 1616; karşılıktaki ayet sayısı kok_envanteri'nden (خنق, وقذ, نطح, ذكو 1 ayet; زلم 2 ayet); "
 "ölçüm yeniden koşuldu, '???' 0; dört kök hapaks (ölçüm HAPAKS alanı); karşılıklar tırnak taşıdığı için satır aynen alıntısı kök adında kesildi, karşılık metni yama dosyası ve kok_turkce ile bayt eşit; "
 "kök سبع tablo karşılığı 'yedi' — 5:3 'es-sebu'' (yırtıcı hayvan) kullanımını kapsamıyor; kök جرح karşılığı 5:4 'el-cevârih' (avcı hayvan) kullanımını kapsıyor; kök هلل karşılığı 'adı anılarak kesilme' 5:3 'uhille' kullanımını kapsıyor (karşılık gözden geçirme tam okuma sonu)",
 "esmâ: 5:3:60 غَفُور ve 5:3:61 رَحِيم 'ilahi' — 'fe-inna'llâhe ğafûrun rahîm', kural ''inne/enne' haberi → ilahi' (lafzın haberi) (esma_el_ekle → esma_kayit; e_el=? 0); kural adı kapalı listeyle karşılaştırıldı (bölüm 16 denetimi kuralı 1); "
 "morph 'fe-inne' (58. kelime) RSLT — şart cevabındaki 'inne' cümlesi, kural tipik biçimiyle uyumlu; 5:4 esmâ yok; lafız 5:3 iki geçiş, 5:4 dört geçiş; Rab yok",
 "esma_kayit: 5:3 ölçüm esmâ '{{1|غَفُور 60\\. sırada, SON konum, MÜHÜR \\| رَحِيم 61\\. sırada, SON konum, MÜHÜR}}' — satır aynen / esma_kayit çıktısı 'mühür EVET (ÇİFT) ton cemâl' (uyuşuyor); 5:4 esma_kayit çıktısı 'mühür hayır' — ölçüm 'esmâ yok' ile uyuşuyor",
 "ölçüm: 5:3 '{{1|biçim ISTISNA \\+ NEHY \\+ QASEM}}', '{{1|fâsıla رحيم → م, N sınıfı — KAFİYE KIRILMASI}}', '{{1|EDİLGEN 4/14 fiil, pas z=1,30}}', '{{1|HAPAKS: خنق}}', '{{1|sayı işareti سَبُع}}', '{{1|simetri \\[3, 7, 53, 1\\]}}', '{{1|harf 289 → harf3 276, isaret 13}}' ve '{{1|dış düğüm 3}}'; "
 "5:4 '{{2|fâsıla ٱلحساب → ب, ب sınıfı — KAFİYE KIRILMASI}}', '{{2|EDİLGEN 2/11 fiil, pas z=0,71}}', '{{2|simetri \\[3, 2, 7, 1\\]}}', '{{2|harf 144 → harf3 136, isaret 8}}' ve '{{2|dış düğüm 9}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); simetri alanı olmayan ayet yok",
 "ölçüm aktör: 5:3 '{{1|adlı إِسْلام 49\\. sırada \\(cins, rol meful\\)}}' — satır aynen, ◇ ve A1'de tam alıntı; ölçüm 'adlı' etiketi masdar özel adı ('el-islâm', morph PN VN) aktör sayıyor — 'radîtu' mef'ûlü, taraf değil (araç tanımı farkı); 5:4 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle): 5:3 emir, yasak, şart — COND 1 'men' (51.), IMPV 1 'xşevni' (39.), PRO 1 'lâ' (37.); biçim ISTISNA + NEHY + QASEM D2'de yazılmadı; QASEM etiketi kasem edatı olmadan (araç tanımı farkı, R5); "
 "5:4 soru, emir — IMPV 4 'qul' (5.), 'kulû' (18.), 'zkurû' (22.), 'ttequ' (26.), INTG 1 'mâzâ' (2.); biçim alanı yok",
 "yıldız: 5:3 ★★★, 5:4 ★★ — satır yıldız kaynağını adlandırmıyor; kaynak kapanış notunda bilançodan",
 "fâsıla: 5:2 ب (ٱلعقاب) → 5:3 م (رحيم, N sınıfı — ölçüm KAFİYE KIRILMASI) → 5:4 ب (ٱلحساب, ب sınıfı — ölçüm KAFİYE KIRILMASI); bölümde üç sınıf (د, ب, م); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref: 5:3 xref 2:173 ve 16:115 (basılmış), okunmuş bir ayet; 5:4 xref 3:19, 22:28, 22:34 ve 22:36 (basılmış), okunmuş bir ayet, okunmamış dört ayet — ◇'de basılmamışlar numarasız, sınıflama sinifla.py ile",
 "nakarat3 (R3: sayıyla özetlendi): 5:3 iki kalıp: bir kalıp süzgeç GEÇER, bir kalıp süzgeç GEÇMEZ; 5:4 üç kalıp: ikisi süzgeç GEÇER, biri GEÇMEZ",
 "araç tanımı farkları (R5; nakarat3 'tür ic' = sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; karşılaştırma nakarat3 kalıbının kelime sayısına eşit aralıkla; taban parantezde): " + '; '.join(r5)
 + "; 5:3 ölçüm 'sayı işareti سَبُع' — 'es-sebu'' yırtıcı hayvan, sayı değil (kök سبع 'yedi' ile karıştırma); 5:3 biçim QASEM — kasem edatı yok; 5:3 aktör 'adlı إِسْلام' — masdar özel ad",
 "aktör / ad (1017, R1): 5:3 muhatap 2MP (adsız), 'hurrimet', 'uhille', 'zubiha', 'dturra' failleri (adsız; edilgen), Allah (lafız), 'es-sebu'' ('ekele' faili), 'ellezîne keferû' ('ye'ise' faili), konuşan 1S (adsız; lafız göndergesine dönme okuması — ölçüm iltifât 0), ölçüm aktör 'el-islâm'; "
 "5:4 'yes'elûneke' faili 3MP (adsız), muhatap 2MS (adsız), söz içi ve söz dışı muhatap 2MP (adsız), 'uhille' failleri (adsız; edilgen), Allah (lafız), 'emsekne' faili 3FP (adsız; gönderge 'el-cevârih') — "
 "A1'e yazılmayanlar: 5:3 'li-ğayri'llâhi' (mecrur; lafız ayrıca anıldı), 'bihî' (mecrur zamir), 'min dînikum' (mecrur izafet), 'fî maxmasatin' ve 'li-ismin' (mecrur tekil nekreler); 5:4 'lehum' (mecrur zamir — soranlar, 'yes'elûneke' failinde anıldı), "
 "'mine'l-cevârih' ('min' + belirli çoğul), ''aleyhi' (mecrur zamir); blokta mecrur ilgi zamiri yok; 'kâne / leyse' ismi nekre yok",
 "söz / tırnak: 5:4 'qul' (5. kelime) — söz 6. kelimede açılıyor, 17. kelimede kapanıyor ('mimmâ 'allemekumu'llâh'; 18. kelime 'fe-kulû' morph REM — tırnak kapandı; emirlerin söz içinde sürmesi okuması da var, karar tam okuma sonu); 5:4 'yes'elûneke' (1. kelime) — soru bildirimi, soru içeriği dolaylı ('mâzâ uhille lehum'), tırnak yok; "
 "5:3'te söz fiili yok — 1S konuşan söz kalıbı taşımıyor, tırnak yok; morph 've' / 'fe' konumlarıyla kontrol edildi: 5:3 've'd-demu' (4.), 've lahmu' (5.), 've mâ' (7., 16., 22.), 've'l-munxaniqatu' (12.), 've'l-mevqûzetu' (13.), 've'l-muteraddiyetu' (14.), 've'n-natîhatu' (15.), 've en' (26.), 'va'xşevni' (39.), 've etmemtu' (44.), 've radîtu' (47.) CONJ; "
 "'fe-lâ' (37.), 'fe-meni' (51.) REM; 'fe-inna' (58.) RSLT; 5:4 've mâ' (9.), 've'zkurû' (22.), 've'ttequ' (26.) CONJ; 'fe-kulû' (18.) REM",
 "◈ tetik (alıntılar önek ve edatsız): 5:3 ◈K يوم ('el-yevme' 31. ve 40. kelime — K2), ◈B موت ('el-meytetu' 3. kelime — B4; ölü hayvan, yiyecek hükmü); 5:4 tetik yok; tetik listesinde olmayan canlı adları: 5:3 'el-xinzîr' (domuz), 'es-sebu'' (yırtıcı), 5:4 'el-cevârih' (avcı hayvanlar), 'mukellibîne' (kök كلب); "
 "5:3 ölüm biçimleri 'munxaniqa', 'mevqûze', 'muteraddiye', 'natîha' — kökleri tetik listesi dışında; oturum_tetik kuru koşu 2 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:3 (2:150, 2:173, 2:185, 3:19, 3:85, 9:120, 16:115, 70:43), 5:4 (3:19, 3:199, 14:51, 22:28, 22:34, 22:36, 40:17; 5:1 ve 5:2 sûre içi) (kontrol.py ile); "
 "bloklar arası sûre içi bağlar 5:1 → 5:4 (lemma 'ehalle') ve 5:2 → 5:4 (önek kesilmiş 've'ttequ'llâhe inna'llâh'; ölçüm nakarat3 tür ic) yalnız 5:4'ün D3'ünde; blok içi bağ yok (5:3 'uhille' kök هلل, 5:4 'uhille' kök حلل — biçim eş, lemma ayrı); "
 "22:28, 22:34, 22:36 bu oturumda blok 1 emsali olarak basılmıştı — bağları 5:4'te lemma dizisi 'zekera ism allâh' ile (ölçüm xref); "
 "D3 dışı bırakılan basılmış sayım eşleri (bütün sayımların 'okumada görüldü' kümesinden): 5:4 lemma 'ehalle' sayımındaki 22:30 (bağı 5:1'de); önek kesilmiş 've'ttequ'llâhe inne' ve 've'ttequ'llâhe inna'llâh' sayımlarındaki 49:1 ve 59:7 (bağları 5:2'de; genel kalıp) — 5:4'te bağ kurulmadı; "
 "D3 etiketleri 'sûre içi'; bağ kurallarında yalnız sayılan lemma / kalıp adı — hepsi say2'de",
 "◈A A4 (R9 + kapsam): 5:3 edim geçişi emir, yasak, nida → emir, yasak, şart (ayetler arası); şahıs geçişi yok (2 → 2); şart → cevap (ayet içi; COND 'men' 51. kelime / cevap 'fe-inna'llâhe' 58. kelime); "
 "5:4 bölüm kapanışı; edim geçişi emir, yasak, şart → soru, emir (ayetler arası); şahıs geçişi yok (2 → 2); soru → cevap (ayet içi; 'yes'elûneke' / 'qul'); söz açılır (6. kelime); söz kapanır (17. kelime) — edim kaynağı ölçüm edim alanı, şahıs kaynağı ölçüm baskın şahıs (5:3 ve 5:4 baskın 2)",
 "sözdizimi (okuma; 'atıf' / 'istînâf' / 'hâl' her geçişte morph etiketiyle; 'X'a atıf' yazımında X ma'tûf aleyh): 5:3 'hurrimet 'aleykumu'l-meytetu' — edilgen fiil cümlesi, nâib fâil dizisi; 've'd-demu' — 'el-meytetu'ya atıf (morph CONJ); 've lahmu'l-xinzîri' — 'el-meytetu'ya atıf (morph CONJ); "
 "'ve mâ uhille' — 'el-meytetu'ya atıf (morph CONJ), 'mâ' mevsûl; 've'l-munxaniqatu' — 'el-meytetu'ya atıf (morph CONJ); 've'l-mevqûzetu' — 'el-meytetu'ya atıf (morph CONJ); 've'l-muteraddiyetu' — 'el-meytetu'ya atıf (morph CONJ); 've'n-natîhatu' — 'el-meytetu'ya atıf (morph CONJ); "
 "'ve mâ ekele's-sebu'u' — 'el-meytetu'ya atıf (morph CONJ); 'illâ mâ zekkeytum' — istisna (morph EXP); 've mâ zubiha' — 'el-meytetu'ya atıf (morph CONJ); 've en testaqsimû' — 'el-meytetu'ya atıf (morph CONJ), 'en' masdar; 'zâlikum fisqun' — isim cümlesi; "
 "'el-yevme ye'ise'llezîne keferû' — fiil cümlesi, 'el-yevme' zaman zarfı (morph T); 'fe-lâ taxşevhum' — istînâf (morph REM), yasak; 'va'xşevni' — 'fe-lâ taxşevhum'a atıf (morph CONJ); 'el-yevme ekmeltu' — fiil cümlesi, 1S; "
 "'ve etmemtu' — 'ekmeltu'ya atıf (morph CONJ); 've radîtu' — 'ekmeltu'ya atıf (morph CONJ), 'dînen' temyîz / mef'ûl okumaları — karar tam okuma sonu; 'fe-meni'dturra' — istînâf (morph REM), şart; 'ğayra mutecânifin' — 'dturra' failinin durumu (mansub; morph etiketi yok); "
 "'fe-inna'llâhe' — şart cevabı (morph RSLT); 5:4 'yes'elûneke mâzâ uhille lehum' — soru bildirimi, 'mâzâ' soru (morph INTG); 'qul' — emir + söz; 'uhille lekumu't-tayyibâtu' — edilgen fiil cümlesi; 've mâ 'allemtum' — 'et-tayyibâtu'ya atıf (morph CONJ), 'mâ' mevsûl, takdirli ('sayd'); "
 "'mukellibîne' — ''allemtum' failinin durumu (mansub; morph etiketi yok); 'tu'allimûnehunne' — 'mukellibîne'den sonra durum cümlesi okuması (morph etiketi yok); 'fe-kulû' — istînâf (morph REM); 've'zkuru'sma'llâhi' — 'fe-kulû'ya atıf (morph CONJ); "
 "'ve'ttequ'llâh' — 'fe-kulû'ya atıf (morph CONJ); 'inna'llâhe serî'u'l-hisâb' — 'inne' cümlesi, ta'lîl okuması",
 "okuma (gözlem) (iddialar ölçüm ve morph ile denetlendi; sayı sözcükleri konum listesiyle betikle karşılaştırıldı): 5:3 haram kılınanlar 'hurrimet' (1. kelime) ile on bir kalem — 'mâ' mevsûlü üç geçiş (7., 16., 22. kelime) ve ölüm biçimleri dört geçiş (12., 13., 14., 15. kelime); "
 "5:3 'el-yevme' iki geçiş (31., 40. kelime) — ümit kesme / tamamlama; 5:3 1S fiil üç geçiş (41., 44., 47. kelime) — 'ekmeltu', 'etmemtu', 'radîtu'; 5:3 kök دين üç geçiş (36., 43., 50. kelime); "
 "5:3 'fe-meni'dturra' (51-52. kelime) 2:173 ve 16:115 ile yasak listesinin ardından zaruret istisnası; 5:4 kök علم üç geçiş (10., 14., 16. kelime) — eğitme / öğretme / Allah'ın öğretmesi; 5:4 lemma 'ehalle' iki geçiş (3., 6. kelime) — soru ve cevapta; "
 "bölüm 1 boyunca kök حلل altı geçiş (5:1 6., 15. kelime; 5:2 5., 25. kelime; 5:4 3., 6. kelime) — sûre başı helâl / haram ekseni",
 "meal (okuma, tam okuma sonu): " + MEAL3 + "; " + MEAL4 + "; " + ES,
 "KARSILIK_CAKISMA",
 "çıpa: 5:3 tarayıcı adayı (kökler لحم, موت; işaretler A_şart, D_yeti; cipa=False; cipa_tarama5_adaylari.json) — yiyecek yasağı ve zaruret istisnası, 'el-meyte' hüküm konusu, doğa iddiası değil (olgu=False); 5:4 tarayıcı vermedi (hüküm, olgu=False); L3 / L4 adayı yok",
 "aday 1039: ayet içi 5:3 ('fe-lâ taxşevhum' / 'va'xşevni'; 'hurrimet 'aleykum' / 'illâ mâ zekkeytum') — okuma; ayetler arası 5:3 / 5:4 ('hurrimet 'aleykum' / 'uhille lekum', blok içi)",
 "aday 1041: kök علم 5:4 ''allemtum' ve 'tu'allimûnehunne' (2MP — insan) ile ''allemekumu'llâh' (lafız) — bir kök ayet içinde insan ve Allah için — vaka (okuma); kök رضو 5:3 'radîtu' (1S) — blokta yalnız konuşan için",
 "bölüm: " + BOL + " bölümü, bölüm 1-2 — bölüm kapanışı 5:4; bölüm iki blok (blok planından: 1 ve 2); başlıktaki 'haram kılınanlar' 5:3 ('hurrimet'), 'dinin tamamlanması' 5:3 ('ekmeltu lekum dînekum'), 'helal yiyecekler' 5:4 ('uhille lekumu't-tayyibât'); "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetine düşen (5:3) blok yazılırken '_sikistirilmis_eski' altına arşivlenir; bölüm sonu bağımsız denetimi bu bloktan sonra (bulgular yamalar/bekleyen_ariza_5_b02.txt, sonraki bloğun ARIZA başı)",
 "SONRADAN",
 "korpusta 1 (kayıt; liste metin oluşturucusundaki say() dönüşleriyle): " + ', '.join(k1),
 "bağ: emsal 2:173, 16:115, 2:150, 2:185, 3:85, 3:19, 9:120, 70:43, 3:199, 40:17, 14:51 — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var (bölüm 16 denetimi kuralı 6); "
 "önceki basım (◇ sayımlarındaki 'okumada görüldü' numaralarından betikle, sunum/onceki_basim.py): ONCEKI; blok ayetleri emsalden önce basılan listesine işlendi; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('harrame', 'uhille', 'munxaniqa', 'mevqûze', 'muteraddiye', 'natîha', 'sebu'', 'zekkey', 'nusub', 'ezlâm', 'ekmel', 'islâm', 'maxmasa', 'mutecânif', 'ehalle', 'cevârih', 'mukellib'; morph LEM 'zekkey' ve 'ekmel' ham biçim — sunum/lem_norm.json); "
 "transliterasyon (sunum/translit_kontrol.py) yalnız ة / tanvin / 'l' birleşme yapıntıları; araç değişikliği: sunum/kelime_kontrol.py 1S ('tu', 'nî', 'ni', 'î') ve 3FP ('ne') zamir anahtarları (5:3 1S konuşan, 5:4 'emsekne'); sunum/morph_dok.py blok morph dökümü",
]


def yaz():
    items = [kes(x) for x in I]
    s = '\n (3, 4): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_3_4.txt', 'w', encoding='utf-8').write(s)


ONC = subprocess.run([sys.executable, '/home/claude/sunum/onceki_basim.py', '3', '4', "2:173 16:115 2:150 2:185 3:85 3:19 9:120 70:43 3:199 40:17 14:51"], capture_output=True, text=True).stdout.strip()
I = [x.replace('ONCEKI', ONC) for x in I]
SON = subprocess.run([sys.executable, '/home/claude/sunum/sonradan.py', '--plan', '2'], capture_output=True, text=True, cwd='/home/claude').stdout.strip().replace('\n', '; ')
I = [x.replace("SONRADAN", "sonradan basılan (bölüm 8 kuralı 1; bölüm 16 denetimi kuralı 3 — sunum/sonradan.py --plan 2): " + SON + " — blok 1 sayımlarında bu blokta basılan 5:4 (geriye dönük düzeltme yok)") for x in I]
I = [x for x in I if x != 'KARSILIK_CAKISMA'] if False else I
idx = I.index('KARSILIK_CAKISMA')
I[idx] = "karşılık çakışması (geçici)"
yaz()
c = cakisma()
I[idx] = ("karşılık çakışması (bölüm 10 denetimi kuralı 11; sunum/cakisma.py bölüm 1 ARIZA meal maddeleri (bloklar 1-2); bölüm 16 denetimi kuralı 11 — eş lemma listesi bölümün bütün meal kayıtlarından morph LEM'e göre, sunum/es_lemma.py): "
          + '; '.join(KARAR.get(l.split(' ←')[0], l + ' — karar yok') for l in c.splitlines()) + "; eş lemmaya farklı karşılık (es_lemma.py): ESLEMMA")
ESL = subprocess.run([sys.executable, '/home/claude/sunum/es_lemma.py', '1', '2'], capture_output=True, text=True).stdout.strip().replace('\n', '; ')
import unicodedata as _u
LADI = {'أَحَلَّ': "lemma 'ehalle'", 'حَرام': "lemma 'harâm'", 'عَلَّمَ': "lemma ''alleme'"}
for k, v in LADI.items(): ESL = ESL.replace(_u.normalize('NFC', k) + ':', v + ':')
assert not any('\u0600' <= ch <= '\u06ff' for ch in ESL), ESL
I[idx] = I[idx].replace('ESLEMMA', (ESL + " — karar: 'ehalle' ve ''alleme' karşılık seçimi tam okuma sonu; 'harâm' karşılığı bağlama göre (ihramlı / haram) — tam okuma sonu") if ESL else 'eş lemmaya farklı karşılık yok')
yaz()


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
for blok in (MEAL3, MEAL4):
    n = int(blok.split(' ', 1)[0].split(':')[1]); govde = blok.split(' ', 1)[1]
    for seg in _bol(govde, "; '"):
        seg = seg if seg.startswith("'") else "'" + seg
        j = seg.index("' (")
        tr = seg[1:j]; ic = seg[j + 3:].rstrip(')')
        parca = _bol(ic, ', ')
        MK.setdefault(n, []).append((tr, parca[0].strip("'"), parca[1:]))
open('/home/claude/b02/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)
print('yazıldı', len(I), 'veri.MK', {k: len(v) for k, v in MK.items()})

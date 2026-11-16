# blok 1 (5:1-2) ARIZA oluşturucu — bölüm 1-1 (sûre 5 açılışı); devir maddesi aynen başta
import sys, os, ast
os.environ['OLC'] = '/home/claude/b01/olcum.txt'
os.environ['SAY2'] = '/home/claude/b01/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim
from sayim import say

# kural13 (2): 've' / 'fe' kelimelerinin ◇ yazımı (ayet → kelime → yazım)
VF_YAZI = {1: {17: "'ve entum'"}, 2: {8: "'ve le'ş-şehra'", 11: "'ve le'l-hedye'", 13: "'ve le'l-qalâ'ide'", 15: "'ve lâ âmmîne'", 23: "'ve ridvânen'", 24: "'ve izâ'", 26: "'fe'stâdû'", 27: "'ve lâ yecrimennekum'", 38: "'ve te'âvenû'", 41: "'ve't-taqvâ'", 42: "'ve lâ te'âvenû'", 46: "'ve'l-'udvâni'", 47: "'ve'ttequ'llâh'"}}

BOL = "'Ahitlere vefa; haram kılınanlar; dinin tamamlanması; helal yiyecekler'"
DEVIR = open('/home/claude/b01/yap/devir_madde.txt', encoding='utf-8').read()


def sic(key):
    n, d = sayim.S2[key]
    return 1 + len([x for x in d['basilan'] if x.startswith('5:')]) + d['okunmus_si'] + d['henuz_si']


R5 = [
 ("5:1", "'eyy ellezî âmene'", 16, 'say 5:1 1-3', "harekesiz 'yâ eyyuhe'llezîne âmenû' (1-3. kelime)", "5:1 + 5:2 + henuz_si"),
 ("5:1", "'sayd entum harâm'", 2, 'say 5:1 16-18 --on', "önek kesilmiş 'es-saydi ve entum hurum' (16-18. kelime)", "5:1 + henuz_si"),
 ("5:2", "'eyy ellezî âmene lâ'", 6, 'say 5:2 1-4', "harekesiz 'yâ eyyuhe'llezîne âmenû lâ' (1-4. kelime)", "5:2 + henuz_si"),
 ("5:2", "'itteqâ allâh inne allâh'", 4, 'say 5:2 47-50 --on', "önek kesilmiş 've'ttequ'llâhe inna'llâh' (47-50. kelime)", "5:2 + henuz_si"),
 ("5:2", "'lâ cerame şene'ân qavm'", 2, 'say 5:2 27-30 --on', "önek kesilmiş 've lâ yecrimennekum şene'ânu qavm' (27-30. kelime)", "5:2 + henuz_si"),
 ("5:2", "'inne allâh şedîd 'iqâb'", 2, 'say 5:2 49-52', "harekesiz 'inna'llâhe şedîdu'l-'iqâb' (49-52. kelime)", "5:2"),
 ("5:2", "'eyy ellezî âmene'", 16, 'say 5:2 1-3', "harekesiz 'yâ eyyuhe'llezîne âmenû' (1-3. kelime)", "5:2 + 5:1 + henuz_si"),
 ("5:2", "'itteqâ allâh inne'", 6, 'say 5:2 47-49 --on', "önek kesilmiş 've'ttequ'llâhe inne' (47-49. kelime)", "5:2 + henuz_si"),
]
DZ = {'say 5:2 49-52': ('dizi 5 2 49 52', "inne allâh şedîd 'iqâb", '49-52'), 'say 5:2 47-49 --on': ('dizi 5 2 47 49', 'itteqâ allâh inne', '47-49')}
r5 = []
for ay, kal, nk, key, ad, taban in R5:
    s = sic(key)
    h = "%s nakarat3 %s %d (tür ic) / %s sûre içi %d (%s)" % (ay, kal, nk, ad, s, taban)
    if s == nk:
        h += ' — tutuyor'
    else:
        dk, dad, dar = DZ[key]
        h += (" — tutmuyor; eşit aralıkla lemma dizisi '%s' (%s. kelime) sûre içi %d (5:2 + henuz_si) — olası neden: nakarat3 'ان' kök anahtarı "
              "'inne' / 'enne' / 'en' biçimlerini birleştiriyor (biçim farkı); nakarat3'ün fazla sûre içi eşleri okunmamış (fark test edilmedi)" % (dad, dar, sic(dk)))
    r5.append(h)

K1 = [('say 5:1 4-5 --on', "önek kesilmiş 'evfû bi'l-'uqûd'"), ('lem 5:1:5', "lemma ''uqûd'"), ('say 5:1 6-7', "harekesiz 'uhillet lekum'"),
      ('say 5:1 14-16', "harekesiz 'ğayra muhilli's-sayd'"), ('lem 5:1:15', "lemma 'muhillî'"), ('say 5:1 19-23', "harekesiz 'inna'llâhe yahkumu mâ yurîd'"),
      ('say 5:1 21-23', "harekesiz 'yahkumu mâ yurîd'"), ('say 5:2 1-5', "harekesiz 'yâ eyyuhe'llezîne âmenû lâ tuhillû'"), ('say 5:2 4-7', "harekesiz 'lâ tuhillû şe'â'ira'llâh'"),
      ('say 5:2 5-7', "harekesiz 'tuhillû şe'â'ira'llâh'"), ('say 5:2 16-18', "harekesiz 'âmmîne'l-beyte'l-harâm'"), ('say 5:2 19-23', "harekesiz 'yebteğûne fadlen min rabbihim ve ridvânâ'"),
      ('say 5:2 20-23', "harekesiz 'fadlen min rabbihim ve ridvânâ'"), ('say 5:2 24-25 --on', "önek kesilmiş 've izâ halaltum'"), ('say 5:2 31-35', "harekesiz 'en saddûkum 'ani'l-mescidi'l-harâm'"),
      ('say 5:2 38-41 --on', "önek kesilmiş 've te'âvenû 'ale'l-birri ve't-taqvâ'"), ('say 5:2 42-46 --on', "önek kesilmiş 've lâ te'âvenû 'ale'l-ismi ve'l-'udvân'")]
k1 = [ad for key, ad in K1 if sayim.S2[key][0] == 1]
assert len(k1) == len(K1), [key for key, ad in K1 if sayim.S2[key][0] != 1]

MEAL1 = ("5:1 'Ey iman edenler' ('yâ eyyuhe'llezîne âmenû', 'yâ' 1. kelimede 'ey' ile, 'eyy' ve 'hâ' 1. kelimede karşılıksız, 'ellezîne' 2. kelimede '-enler' ile, "
 "'iman et-' 'âmenû' açılımı (3. kelime; IV. bab; 'iman' açılım takdiri), 'û' 3. kelimede karşılıksız (fail eki — '-enler' içinde)); "
 "'Akitleri yerine getirin' ('evfû bi'l-'uqûd', 'yerine getir-' 'evfû' açılımı (4. kelime; IV. bab; 'yerine' açılım takdiri), 'û' 4. kelimede '-in' ile (emir 2MP), "
 "'bi' 5. kelimede karşılıksız (mef'ûl '-i' ile), 'akit' ''uqûd' karşılığı (5. kelime; çoğul '-ler'), sıralama: fiil sona alındı); "
 "'Size okunacak olanlar dışında' ('illâ mâ yutlâ 'aleykum', 'illâ' 10. kelimede 'dışında' ile, 'mâ' 11. kelimede '-acak olanlar' ile ('olan' takdir), "
 "'oku-' 'yutlâ' karşılığı (12. kelime; edilgen — mealde edilgen 'okunacak'), ''alâ' 13. kelimede '-e' ile (fiil yönetimi takdiri), 'kum' 13. kelimede 'siz' ile, sıralama: istisna öne alındı); "
 "'davar hayvanları sizin için helâl kılındı' ('uhillet lekum behîmetu'l-en'âm', 'helâl kıl-' 'uhillet' açılımı (6. kelime; IV. bab; edilgen — mealde edilgen; 'kıl-' açılım takdiri), "
 "'li' 7. kelimede 'için' ile, 'kum' 7. kelimede 'sizin' ile, 'hayvan' 'behîme' karşılığı (8. kelime; tekil — '-lar' takdiri), 'davar' 'ne'am' karşılığı (9. kelime), "
 "'-ı' iyelik takdiri (8. kelime; izafet), sıralama: nâib fâil fiilden önce); "
 "'siz ihramlı iken avı helâl saymayanlar olarak' ('ğayra muhilli's-saydi ve entum hurum', 'ğayr' 14. kelimede '-mayanlar' ile, 'olarak' takdir (14. kelime; mansub), "
 "'helâl say-' 'muhilli' açılımı (15. kelime; ortaç; 'say-' açılım takdiri), 'av' 'sayd' karşılığı (16. kelime; '-ı' belirtme), 've' 17. kelimede 'iken' ile (morph CIRC), "
 "'entum' 17. kelimede 'siz' ile, 'ihramlı' 'harâm' karşılığı (18. kelime; nekre çoğul — tekil verildi, 'bir' takdiri yok), sıralama: 've entum hurum' öne alındı); "
 "'Şüphesiz Allah dilediğine hükmeder' ('inna'llâhe yahkumu mâ yurîd', 'inne' 19. kelimede 'şüphesiz' ile, lafız 20. kelimede 'Allah' ile, 'hükmet-' 'yahkumu' karşılığı (21. kelime; geniş zaman), "
 "'mâ' 22. kelimede '-diği' ile, '-ne' fiil yönetimi takdiri (22. kelime; 'dilediğine'), 'dile-' 'yurîdu' karşılığı (23. kelime; IV. bab), sıralama: fiil sona alındı)")
MEAL2 = ("5:2 'Ey iman edenler' ('yâ eyyuhe'llezîne âmenû', 'yâ' 1. kelimede 'ey' ile, 'eyy' ve 'hâ' 1. kelimede karşılıksız, 'ellezîne' 2. kelimede '-enler' ile, "
 "'iman et-' 'âmenû' açılımı (3. kelime; 'iman' açılım takdiri), 'û' 3. kelimede karşılıksız (fail eki — '-enler' içinde)); "
 "'Allah'ın nişanlarını … helâl saymayın' ('lâ tuhillû şe'â'ira'llâh', 'lâ' 4. kelimede '-ma-' ile (yasak), 'helâl say-' 'tuhillû' açılımı (5. kelime; IV. bab; 'say-' açılım takdiri), "
 "'û' 5. kelimede '-yın' ile, 'nişan' 'şe'â'ir' karşılığı (6. kelime; çoğul '-lar'), '-ı' iyelik takdiri (6. kelime; izafet), lafız 7. kelimede 'Allah'ın' ile ('-ın' takdir — izafet açılımı), "
 "sıralama: mef'ûl dizisi öne, yasak fiili sona alındı); "
 "'haram ayı' ('ve le'ş-şehra'l-harâm', 've' 8. kelimede karşılıksız (virgül; morph CONJ), 'lâ' 8. kelimede karşılıksız (morph NEG; yasak 'saymayın' fiilinde), "
 "'ay' 'şehr' karşılığı (9. kelime; '-ı' belirtme), 'haram' 'harâm' karşılığı (10. kelime)); "
 "'kurbanlığı' ('ve le'l-hedye', 've' 11. kelimede karşılıksız (virgül; morph CONJ), 'lâ' 11. kelimede karşılıksız (morph NEG), 'kurbanlık' 'hedy' karşılığı (12. kelime)); "
 "'gerdanlıkları' ('ve le'l-qalâ'ide', 've' 13. kelimede karşılıksız (virgül; morph CONJ), 'lâ' 13. kelimede karşılıksız (morph NEG), 'gerdanlık' 'qalâ'id' karşılığı (14. kelime; çoğul)); "
 "'ve Rablerinden lütuf ve hoşnutluk arayarak Haram Ev'e yönelenleri' ('ve lâ âmmîne'l-beyte'l-harâme yebteğûne fadlen min rabbihim ve ridvânen', 've' 15. kelimede 've' ile (morph CONJ), "
 "'lâ' 15. kelimede karşılıksız (morph NEG), 'yönel-' 'âmmîne' açılımı (16. kelime; ortaç '-enler'; '-i' belirtme), 'ev' 'beyt' karşılığı (17. kelime; '-e' — fiil yönetimi takdiri), "
 "'Haram' 'harâm' karşılığı (18. kelime), 'ara-' 'yebteğûne' karşılığı (19. kelime; VIII. bab; '-arak' — durum okuması), 'ûne' 19. kelimede karşılıksız (fail eki — '-arak' içinde), "
 "'lütuf' 'fadl' karşılığı (20. kelime; nekre — 'bir' takdiri yok), 'min' 21. kelimede '-den' ile, 'Rab' 'rabb' karşılığı (22. kelime), 'him' 22. kelimede '-leri' iyelik ile, "
 "'ve' 23. kelimede 've' ile, 'hoşnutluk' 'ridvân' karşılığı (23. kelime; nekre), sıralama: ortaç tümleci ortaçtan önce); "
 "'İhramdan çıktığınızda avlanın' ('ve izâ halaltum fe'stâdû', 've' 24. kelimede karşılıksız (nokta; morph REM), 'izâ' 24. kelimede '-dığınızda' ile (zaman), "
 "'ihramdan çık-' 'halaltum' açılımı (25. kelime; I. bab; 'ihram' açılım takdiri, '-dan' fiil yönetimi takdiri), 'tum' 25. kelimede '-nız' ile, 'fe' 26. kelimede karşılıksız (cevap; morph RSLT), "
 "'avlan-' 'stâdû' karşılığı (26. kelime; VIII. bab; emir), 'û' 26. kelimede '-ın' ile); "
 "'Sizi Haram Mescid'den alıkoydukları için bir kavme duyduğunuz kin sizi aşırı gitmeye sürüklemesin' ('ve lâ yecrimennekum şene'ânu qavmin en saddûkum 'ani'l-mescidi'l-harâmi en ta'tedû', "
 "'ve' 27. kelimede karşılıksız (nokta; morph CONJ), 'lâ' 27. kelimede '-me-' ile (yasak, 3MS — '-sin'), 'sürükle-' 'yecrimennekum' karşılığı (28. kelime; I. bab; EMPH 'nûn' karşılıksız), "
 "'kum' 28. kelimede 'sizi' ile, 'kin' 'şene'ân' karşılığı (29. kelime), 'kavim' 'qavm' karşılığı (30. kelime; nekre — 'bir' takdiri; '-e' fiil yönetimi takdiri), "
 "'duyduğunuz' takdir (29-30. kelime; izafet açılımı — 'duy-' açılım takdiri, '-unuz' iyelik takdiri), 'en' 31. kelimede '-dukları' ile ('için' takdir — ta'lîl okuması), "
 "'alıkoy-' 'saddûkum' karşılığı (32. kelime; I. bab), 'û' 32. kelimede '-lar' ile, 'kum' 32. kelimede 'sizi' ile, ''an' 33. kelimede '-den' ile, 'mescid' 'mescid' karşılığı (34. kelime), "
 "'Haram' 'harâm' karşılığı (35. kelime), 'en' 36. kelimede '-meye' ile ('-e' — fiil yönetimi takdiri), 'aşırı git-' 'ta'tedû' açılımı (37. kelime; VIII. bab; 'aşırı' açılım takdiri), "
 "'û' 37. kelimede karşılıksız (fail eki — masdar içinde), sıralama: ta'lîl öne, fiil sona alındı); "
 "'İyilik ve takvâ üzerinde yardımlaşın' ('ve te'âvenû 'ale'l-birri ve't-taqvâ', 've' 38. kelimede karşılıksız (nokta; morph REM), 'yardımlaş-' 'te'âvenû' karşılığı (38. kelime; VI. bab; emir), "
 "'û' 38. kelimede '-ın' ile, ''alâ' 39. kelimede 'üzerinde' ile, 'iyilik' 'birr' karşılığı (40. kelime), 've' 41. kelimede 've' ile, 'takvâ' 'taqvâ' karşılığı (41. kelime), sıralama: fiil sona alındı); "
 "'günah ve düşmanlık üzerinde yardımlaşmayın' ('ve lâ te'âvenû 'ale'l-ismi ve'l-'udvân', 've' 42. kelimede karşılıksız (virgül; morph CONJ), 'lâ' 42. kelimede '-ma-' ile (yasak), "
 "'yardımlaş-' 'te'âvenû' karşılığı (43. kelime; VI. bab), 'û' 43. kelimede '-yın' ile, ''alâ' 44. kelimede 'üzerinde' ile, 'günah' 'ism' karşılığı (45. kelime), 've' 46. kelimede 've' ile, "
 "'düşmanlık' ''udvân' karşılığı (46. kelime), sıralama: fiil sona alındı); "
 "'Allah'tan sakının' ('ve'ttequ'llâh', 've' 47. kelimede karşılıksız (nokta; morph CONJ), 'sakın-' 'ttequ' karşılığı (47. kelime; VIII. bab), 'û' 47. kelimede '-ın' ile, "
 "lafız 48. kelimede 'Allah'tan' ile ('-tan' — fiil yönetimi takdiri)); "
 "'Şüphesiz Allah'ın cezası çetindir' ('inna'llâhe şedîdu'l-'iqâb', 'inne' 49. kelimede 'şüphesiz' ile, lafız 50. kelimede 'Allah'ın' ile ('-ın' takdir — haberdeki izafet mübtedâya aktarıldı), "
 "'çetin' 'şedîd' karşılığı (51. kelime), '-dir' takdir (51. kelime), 'ceza' ''iqâb' karşılığı (52. kelime), '-sı' iyelik takdiri (52. kelime), sıralama: haber sona alındı)")
ES = ("blok içi eş edat / lemma karşılıkları (karşılık seçimi tam okuma sonu): 've' — 'iken' ile (5:1 17. kelime), 've' ile (5:2 15., 23., 41., 46. kelime), "
 "karşılıksız (5:2 8., 11., 13., 24., 27., 38., 42., 47. kelime); ''alâ' — '-e' ile (5:1 13. kelime), 'üzerinde' ile (5:2 39., 44. kelime); "
 "'lâ' — '-ma-' / '-me-' ile (5:2 4., 27., 42. kelime), karşılıksız (5:2 8., 11., 13., 15. kelime); 'en' — '-dukları' ile (5:2 31. kelime), '-meye' ile (5:2 36. kelime); "
 "'inne' — 'şüphesiz' ile (5:1 19. kelime, 5:2 49. kelime); 'kum' — 'siz' (5:1 13. kelime), 'sizin' (5:1 7. kelime), 'sizi' (5:2 28., 32. kelime); "
 "lemma 'harâm' — 'ihramlı' (5:1 18. kelime), 'haram' (5:2 10. kelime), 'Haram' (5:2 18., 35. kelime); lemma 'ehalle' — 'helâl kıl-' (5:1 6. kelime), 'helâl say-' (5:2 5. kelime); "
 "kök حلل — 'helâl say-' ('muhilli', 5:1 15. kelime), 'ihramdan çık-' ('halaltum', 5:2 25. kelime); 'şe'â'ir' 'nişan' — emsal 2:158 meali 'nişan', 22:32 ve 22:36 mealleri 'işaret' (karşılık çakışması, tam okuma sonu)")

I = [
 DEVIR,
 "hazırlık (sûre 5, kullanıcıyla, 2026-11-15): blok planı yamalar/blok_plani_5.txt (16 bölüm, 36 blok; kullanıcı onayı, başlıklar olduğu gibi); okuma_metni.json bölünmeden kalır (kullanıcı kararı — seçenek A; boyut her blokta ölçülür); "
 "dosya ailesi yamalar/iskele_5.py ile sûre 4 dosyalarından kuruldu (maide_metin_1, maide_kayit, uret_blok_5, aday_ekle_5_maide / AX_maide, AS_maide, kok_ekle_5, duzeltme_5, yama_retroaktif_gloss_5, maide_kapanis, maide_paket_md; "
 "cipa_tarama5_adaylari.json = tarayıcı v4 korpus koşusunun sûre 5 alt kümesi, 17 aday); yama betikleri yama_kayit_5 (boş CIPA / ARIZA çapası), yama_metin_5, yama_uret_5, yama_bag_5, yama_kok_5_sablon; "
 "sunum araçları sûre parametresine bağlandı (sunum/sure.py: altdize, kelime_kontrol, kontrol, kural13, kural14, onceki_basim, translit_kontrol, edat_etiket; denetim_5.sh; sinifla.py sûre 5 sürümü); "
 "bölüm 16 denetimi kuralları: sonradan.py '--plan NN' blok listesini blok planından üretir (kural 3); yasakli.sh 'önceki ayet' kalıbını, 'sonraki ayet' kalıbını, çekimlerini ve 'sûre N okun-' kalıbını tarar, tırnaklı kalıp adı izinli (kural 10, 15); "
 "bozuk morph LEM normalleştirmesi sunum/lem_norm.json'da bir defa yazıldı — lemma adı morph LEM'in ham transliterasyonu, normalleştirme yok (kural 9); kökteki esma_kayit.json / kok_turkce.json kopyaları kullanıcıya hatırlatıldı",
 "kök tablosu: ölçümde '???' 5:1 ve 5:2 için ayrı sayıldı — 0; yeni kök yok (okunan ayetlerde tabloda olmayan kök 0); kök anlamları ölçüm glossundan; kök شعر tablo karşılığı 'şair; farkında olma' — 5:2 'şe'â'ir' (nişanlar) kullanımını kapsamıyor; "
 "kök حرم karşılığı 'haram kılma, yasak' — 5:1 'hurum' (ihramlı) kullanımını dolaylı kapsıyor; kök قلد karşılığı 'gerdanlık (qalâid); anahtarlar (maqâlîd)' 5:2 kullanımını kapsıyor (karşılık gözden geçirme tam okuma sonu)",
 "esmâ: 5:1 ve 5:2 esmâ yok (ölçüm 'esmâ yok'; esma_kayit e_oto 0, e_el 0); esma_el dosyası yazılmadı; lafız 5:1 bir geçiş, 5:2 üç geçiş; Rab 5:2'de ('rabbihim', 22. kelime)",
 "esma_kayit: 5:1 ve 5:2 esma_kayit çıktısı 'mühür hayır' — ölçüm 'esmâ yok' ile uyuşuyor; son üç kelime 5:1 'sayd / harâm / lafız', 5:2 'lafız / şedîd / 'iqâb' (esma_kayit çıktısı)",
 "ölçüm: 5:1 '{{1|biçim DIKKAT \\+ ISTISNA}}', '{{1|fâsıla يريد → د, د sınıfı}}', '{{1|EDİLGEN 2/6 fiil, pas z=1,57}}', '{{1|simetri \\[3, 11, 17, 1\\]}}' ve '{{1|dış düğüm 0}}'; "
 "5:2 '{{2|biçim DIKKAT \\+ NEHY}}', '{{2|fâsıla ٱلعقاب → ب, ب sınıfı}}', '{{2|simetri \\[4, 8, 33, 1\\]}}', '{{2|harf 255 → harf3 240, isaret 15}}' ve '{{2|dış düğüm 7}}' — satır aynen (◇'de de; satir_aynen_kontrol.py ve satir_aynen_tam.py ile bayt eşitliği denetlendi); simetri alanı olmayan ayet yok",
 "ölçüm aktör: 5:1 ve 5:2 aktör yok; 5:2 Rab ölçüm Rab alanında (22. sıra)",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle): 5:1 emir, nida — IMPV 1 'evfû' (4.), VOC 1 'yâ' (1.); biçim DIKKAT + ISTISNA D2'de yazılmadı; 5:2 emir, yasak, nida — EMPH 1 'nûn' (28.), IMPV 3 'stâdû' (26.), 'te'âvenû' (38.), 'ttequ' (47.), "
 "NEG 4 'lâ' (8., 11., 13., 15.), PRO 3 'lâ' (4., 27., 42.), VOC 1 'yâ' (1.); biçim DIKKAT + NEHY D2'de yazılmadı; 5:2 'izâ' (24.) morph T — ölçüm edim alanında şart yok",
 "yıldız: 5:1 ★, 5:2 ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak kapanış notunda bilançodan",
 "fâsıla: önceki sûrenin son ayeti م (N sınıfı; numarasız — bu oturumda basılmadı) → 5:1 د (يريد, د sınıfı) → 5:2 ب (ٱلعقاب, ب sınıfı); blokta iki sınıf, 5:2 kafiyesi başka sınıf; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref: 5:1 xref yok; 5:2 xref 2:198, 48:25 ve 59:7 (basılmış), okunmuş iki ayet, okunmamış iki ayet — ◇'de basılmamışlar numarasız, sınıflama sinifla.py ile",
 "nakarat3 (R3: sayıyla özetlendi): 5:1 iki kalıp: bir kalıp süzgeç GEÇER, bir kalıp süzgeç GEÇMEZ; 5:2 altı kalıp: hepsi süzgeç GEÇER",
 "araç tanımı farkları (R5; nakarat3 'tür ic' = sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; karşılaştırma nakarat3 kalıbının kelime sayısına eşit aralıkla; taban parantezde; nakarat3 kalıpları transliterasyonla): " + '; '.join(r5),
 "aktör / ad (1017, R1): 5:1 muhatap 2MP (adsız; nidâ 'ellezîne âmenû'), 'uhillet' ve 'yutlâ' failleri (adsız; edilgen; nâib fâiller 'behîmetu'l-en'âm' ve 'mâ'ya dönen zamir), Allah (lafız), 'yahkumu' / 'yurîdu' faili 3MS (adsız; gönderge lafız); "
 "5:2 muhatap 2MP (adsız), Allah (lafız), 'âmmîne'l-beyte'l-harâm' (çoğul etken ortaç; mef'ûl dizisine atıf), 'yebteğûne' ve 'saddûkum' failleri 3MP (adsız), Rab, 'şene'ânu qavmin' ('yecrimennekum' faili) — "
 "A1'e yazılmayanlar: 5:1 'lekum' ve ''aleykum' muhatabın mecrur zamirleri (muhatap içinde anıldı); 5:2 'min rabbihim'deki 'him' (mecrur zamir, Rab izafeti), 'qavmin' izafetle mecrur nekre ('şene'ânu qavmin' fail izafeti olarak anıldı); blokta mecrur ilgi zamiri yok; 'kâne / leyse' ismi nekre yok",
 "söz / tırnak: blokta söz yok; lemma qâle blokta yok; tırnak yok; morph 've' / 'fe' konumlarıyla kontrol edildi: 5:1 've entum' (17.) CIRC; 5:2 've le'ş-şehra' (8.), 've le'l-hedye' (11.), 've le'l-qalâ'ide' (13.), 've lâ âmmîne' (15.), 've ridvânen' (23.), 've lâ yecrimennekum' (27.), "
 "'ve't-taqvâ' (41.), 've lâ te'âvenû' (42.), 've'l-'udvâni' (46.), 've'ttequ' (47.) CONJ; 've izâ' (24.), 've te'âvenû' (38.) REM; 'fe'stâdû' (26.) RSLT",
 "◈ tetik (alıntılar önek ve edatsız): 5:1 ◈B نعم ('el-en'âm' 9. kelime — B1; S1 lemma kısıtı 'ne'am' — davar); 5:2 tetik yok; tetik listesinde olmayan canlı adları: 5:1 'behîme' (hayvan; بهم), 5:1 'sayd' ve 5:2 'stâdû' (av; صيد), 5:2 'hedy' (kurbanlık; هدي) ve 'qalâ'id' (gerdanlık; قلد); "
 "oturum_tetik kuru koşu 2 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:1 (4:127, 22:28, 22:30, 22:34; 5:2 blok içi), 5:2 (2:158, 2:194, 2:196, 2:198, 2:217, 22:32, 22:36, 48:25, 49:1, 59:7; 5:1 blok içi) (kontrol.py ile); "
 "blok içi bağ 5:1 → 5:2 (harekesiz 'yâ eyyuhe'llezîne âmenû'; lemma 'ehalle' — izin / yasak) iki ayetin D3'ünde; sûre geçişinde (önceki sûrenin son ayeti → 5:1) bölüm geçişi kuralıyla ardışık bağ kurulmadı; "
 "D3 dışı bırakılan basılmış sayım eşi (kural14.py b3; bütün sayımların 'okumada görüldü' kümesinden): 5:1 harekesiz 'yâ eyyuhe'llezîne âmenû' sayımındaki 49:1 — bağı 5:2'de (önek kesilmiş 've'ttequ'llâhe inna'llâh'), 5:1'de genel hitap kalıbı, bağ kurulmadı; "
 "D3 etiketleri yalnız 'blok içi'; bağ kurallarında yalnız sayılan lemma / kalıp adı — hepsi say2'de",
 "◈A A4 (R9 + kapsam): 5:1 bölüm açılışı (sûre açılışı — kapalı listede 'sûre açılışı' yok); hitap açılır ('yâ eyyuhe'llezîne âmenû', 1-3. kelime); edim geçişi emir, şart → emir, nida ve şahıs geçişi 3 → 2 — kaynak önceki sûrenin son ayeti (ölçüm edim 'emir, şart', baskın 3; numarasız); "
 "5:2 hitap açılır ('yâ eyyuhe'llezîne âmenû', 1-3. kelime); edim geçişi emir, nida → emir, yasak, nida (ayetler arası); şahıs geçişi yok (2 → 2); 5:2 've izâ halaltum fe'stâdû' — 'izâ' zaman (morph T), ölçüm edimi şart değil, A4'te 'şart → cevap' yazılmadı; "
 "edim kaynağı ölçüm edim alanı, şahıs kaynağı ölçüm baskın şahıs (5:1 ve 5:2 baskın 2)",
 "sözdizimi (okuma; 'atıf' / 'istînâf' / 'hâl' her geçişte morph etiketiyle; 'X'a atıf' yazımında X ma'tûf aleyh): 5:1 'yâ eyyuhe'llezîne âmenû' — nida, 'ellezîne' münâdâ (mevsûl); 'evfû bi'l-'uqûd' — emir, 'bi' mef'ûle; "
 "'uhillet lekum behîmetu'l-en'âm' — edilgen fiil cümlesi, nâib fâil izafet; 'illâ mâ yutlâ 'aleykum' — istisna (morph EXP), 'mâ' mevsûl; 'ğayra muhilli's-saydi' — 'lekum' muhatabının durumu (mansub 'ğayra'; morph etiketi yok); "
 "'ve entum hurumun' — hâl (morph CIRC); 'inna'llâhe yahkumu mâ yurîd' — 'inne' cümlesi, haber fiil cümlesi, 'mâ' mevsûl; "
 "5:2 'lâ tuhillû şe'â'ira'llâh' — yasak (morph PRO), mef'ûl izafet; 've le'ş-şehra'l-harâm' — 'şe'â'ira'ya atıf (morph CONJ), 'lâ' olumsuzluğu tekrarlıyor (morph NEG); 've le'l-hedye' — 'şe'â'ira'ya atıf (morph CONJ); "
 "'ve le'l-qalâ'ide' — 'şe'â'ira'ya atıf (morph CONJ); 've lâ âmmîne'l-beyte'l-harâm' — 'şe'â'ira'ya atıf (morph CONJ), 'el-beyte' ortacın mef'ûlü; 'yebteğûne fadlen min rabbihim' — 'âmmîne'nin durumu okuması (morph etiketi yok); "
 "'ve ridvânen' — 'fadlen'e atıf (morph CONJ); 've izâ halaltum' — istînâf (morph REM), 'izâ' zaman; 'fe'stâdû' — 'izâ' cevabı (morph RSLT); 've lâ yecrimennekum' — 've izâ' cümlesine atıf (morph CONJ), yasak (morph PRO); "
 "'şene'ânu qavmin' — fail izafeti; 'en saddûkum' — 'en' masdar, ta'lîl okuması; 'en ta'tedû' — 'yecrimenne'nin mef'ûlü (masdar); 've te'âvenû' — istînâf (morph REM); 've't-taqvâ' — 'el-birri'ye atıf (morph CONJ); "
 "'ve lâ te'âvenû' — 've te'âvenû'ya atıf (morph CONJ); 've'l-'udvâni' — 'el-ismi'ye atıf (morph CONJ); 've'ttequ'llâh' — 've lâ te'âvenû'ya atıf (morph CONJ); 'inna'llâhe şedîdu'l-'iqâb' — 'inne' cümlesi (morph etiketi ACC), ta'lîl okuması",
 "okuma (gözlem) (iddialar ölçüm ve morph ile denetlendi; sayı sözcükleri konum listesiyle betikle karşılaştırıldı): 5:1 ve 5:2 'yâ eyyuhe'llezîne âmenû' (1-3. kelime) ile açılıyor; kök حلل 5:1'de iki geçiş (6., 15. kelime) — helâl kılma / helâl saymama, "
 "5:2'de iki geçiş (5., 25. kelime) — helâl saymama yasağı / ihramdan çıkma; kök حرم 5:1'de bir geçiş (18. kelime) — ihramlılık, 5:2'de üç geçiş (10., 18., 35. kelime) — ay, ev, mescid sıfatı; "
 "5:1 'ğayra muhilli's-saydi ve entum hurum' (14-18. kelime) / 5:2 've izâ halaltum fe'stâdû' (24-26. kelime) — av yasağı ihram süresine bağlanıyor, ihramdan çıkışla av emri; "
 "5:2 'lâ' yedi geçiş (4., 8., 11., 13., 15., 27., 42. kelime) — yasak dizisi; 5:2 kök عون emir / yasak çifti (38., 43. kelime) — 'el-birri ve't-taqvâ' / 'el-ismi ve'l-'udvân'",
 "meal (okuma, tam okuma sonu): " + MEAL1 + "; " + MEAL2 + "; " + ES,
 "çıpa: 5:1 ve 5:2 tarayıcı aday vermedi (cipa_tarama5_adaylari.json); 5:1 emir ve helâl kılma hükmü, 5:2 yasak ve emir hükümleri (olgu=False); L3 / L4 adayı yok",
 "aday 1039: ayet içi 5:1 ('uhillet lekum' / 'ğayra muhilli's-saydi ve entum hurum'), 5:2 ('ve te'âvenû 'ale'l-birri ve't-taqvâ' / 've lâ te'âvenû 'ale'l-ismi ve'l-'udvân') — okuma; ayetler arası 5:1 / 5:2 ('uhillet lekum' / 'lâ tuhillû', lemma 'ehalle', blok içi)",
 "aday 1041: blokta vaka yok (lafız ve Rab göndergeli kelimelerin kökleri blokta insan göndergeli kullanılmıyor; 5:1 'yahkumu' (lafız) — kök حكم blokta yalnız lafız için — okuma)",
 "bölüm: " + BOL + " bölümü, bölüm 1-1 — bölüm açılışı 5:1 (sûre 5 açılışı); bölüm sonraki blokta kapanır; mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetine düşen (5:2) blok yazılırken '_sikistirilmis_eski' altına arşivlenir; "
 "okuma_metni['5']'teki altı eski blok özeti okuma sayılmaz, kapanışta '_eski_ozet' altına",
 "sonradan basılan (bölüm 8 kuralı 1; bölüm 16 denetimi kuralı 3 — sunum/sonradan.py --plan 1): blok listesi boş (sûrenin açılış bloğu; oturumun önceki bloğu yok) — eskiyen sayım yok",
 "korpusta 1 (kayıt; liste metin oluşturucusundaki say() dönüşleriyle): " + ', '.join(k1),
 "bağ: emsal 22:28, 22:34, 22:30, 4:127, 2:158, 22:32, 22:36, 2:194, 2:217, 2:196, 2:198, 48:25, 59:7, 49:1 — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var (bölüm 16 denetimi kuralı 6); "
 "önceki basım yok (oturumun açılış bloğu; sunum/onceki_basim.py '—'); blok ayetleri emsalden önce basılan listesine işlendi; sayımlar işaretlemeden sonra (R5 eşit aralık sayımları ve lemma dizileri eklendikten sonra) sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla (''uqûd', 'ehalle', 'behîme', 'muhillî', 'şe'â'ir', 'hedy', 'qalâ'id', 'şene'ân'; sunum/lem_norm.json); ortaçlarda bab etiketi ◇'de yazılmadı; transliterasyon (sunum/translit_kontrol.py): 5:1 ة yapıntısı ('behîmetu'), 5:2 'lâ' + belirlilik 'l' ve tanvin 'n' birleşme yapıntıları — harf değişimi yok; sûre 5 açılış bloğu",
]
items = [kes(x) for x in I]
for x in items:
    assert '{{' not in x
s = '\n (1, 2): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
ast.literal_eval('{' + s + '}')
open('/home/claude/yamalar/ariza_5_1_2.txt', 'w', encoding='utf-8').write(s)
print('yazıldı', len(items))

# kural14 için yapılandırılmış meal verisi (veri.MK: ayet → [(tr, q, items)])
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
for blok in (MEAL1, MEAL2):
    n = int(blok.split(' ', 1)[0].split(':')[1]); govde = blok.split(' ', 1)[1]
    for seg in _bol(govde, "; '"):
        seg = seg if seg.startswith("'") else "'" + seg
        j = seg.index("' (")
        tr = seg[1:j]; ic = seg[j + 3:].rstrip(')')
        parca = _bol(ic, ', ')
        q = parca[0].strip("'"); MK.setdefault(n, []).append((tr, q, parca[1:]))
open('/home/claude/b01/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)
print('veri.MK', {k: len(v) for k, v in MK.items()})

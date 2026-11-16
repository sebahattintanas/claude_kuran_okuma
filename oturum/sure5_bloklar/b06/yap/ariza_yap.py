# blok 6 (5:15-17) ARIZA oluşturucu — bölüm 3-2
import sys, os, ast, subprocess, re
os.environ['OLC'] = '/home/claude/b06/olcum.txt'
os.environ['SAY2'] = '/home/claude/b06/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

VF_YAZI = {15: {14: "'ve ya'fû'", 22: "'ve kitâbun'"}, 16: {9: "'ve yuxricuhum'", 15: "'ve yehdîhim'"},
           17: {12: "'fe-men'", 24: "'ve ummehû'", 25: "'ve men'", 29: "'ve li'llâhi'", 32: "'ve'l-ardi'", 33: "'ve mâ'", 38: "'ve'llâhu'"}}
BOL = "'İsrâiloğullarının ve Nasârâ'nın misakı; kitap ehline gelen elçi; Mesih hakkında söz'"


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



TT = "biçim farkı — eş okunmamış, ayrıntı test edilmedi"
R5 = [
 ("5:15", "'ehl kitâb qad câ'e rasûl beyyen li' (LEM 'beyyen' morph LEM ham biçim)", 2, 'say 5:15 1-7', "harekesiz 'yâ ehle'l-kitâbi qad câ'akum rasûlunâ yubeyyinu lekum' (1-7. kelime)", None),
 ("5:17", "'leqad kefera ellezî qâle inne allâh huve mesîh ibn meryem qâle'", 2, 'say 5:17 1-11', "harekesiz 'leqad kefera'llezîne qâlû inna'llâhe huve'l-mesîhu'bnu meryeme qul' (1-11. kelime)", ('dizi 5 17 1 11', "qad kefera ellezî qâle inne allâh huve mesîh ibn meryem qâle", '1-11', TT)),
 ("5:17", "'leqad kefera ellezî qâle inne allâh'", 3, 'say 5:17 1-6', "harekesiz 'leqad kefera'llezîne qâlû inna'llâh' (1-6. kelime)", None),
 ("5:17", "'allâh mulk semâ' ard mâ beyn'", 2, 'say 5:17 29-34', "harekesiz 've li'llâhi mulku's-semâvâti ve'l-ardi ve mâ beynehumâ' (29-34. kelime)", None),
 ("5:17", "'şâ'e allâh 'alâ kull şey' qadîr'", 2, 'say 5:17 37-42', "harekesiz 'yeşâ' ve'llâhu 'alâ kulli şey'in qadîr' (37-42. kelime)", None),
 ("5:17", "'allâh mulk semâ' ard mâ'", 3, 'say 5:17 29-33', "harekesiz 've li'llâhi mulku's-semâvâti ve'l-ardi ve mâ' (29-33. kelime)", ('dizi 5 17 29 33', "allâh mulk semâ' ard mâ", '29-33', TT)),
 ("5:17", "'allâh 'alâ kull şey' qadîr'", 3, 'say 5:17 38-42', "harekesiz 've'llâhu 'alâ kulli şey'in qadîr' (38-42. kelime)", None),
 ("5:17", "''alâ kull şey' qadîr'", 4, 'say 5:17 39-42', "harekesiz ''alâ kulli şey'in qadîr' (39-42. kelime)", None),
 ("5:17", "''alâ kull şey''", 5, 'say 5:17 39-41', "harekesiz ''alâ kulli şey'' (39-41. kelime)", None),
 ("5:17", "'mulk semâ' ard'", 4, 'say 5:17 30-32', "harekesiz 'mulku's-semâvâti ve'l-ard' (30-32. kelime)", None),
 ("5:17", "'mesîh ibn meryem'", 3, 'say 5:17 8-10', "harekesiz 'l-mesîhu'bnu meryem' (8-10. kelime)", None),
 ("5:17", "'min allâh şey''", 2, 'say 5:17 14-16', "harekesiz 'mina'llâhi şey'en' (14-16. kelime)", None),
 ("5:17", "'fî ard cemî''", 2, 'say 5:17 26-28', "harekesiz 'fi'l-ardi cemî'an' (26-28. kelime)", None),
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
            h += (" — tutmuyor; eşit aralıkla lemma dizisi '%s' (%s. kelime) sûre içi %d (%s)" % (dad, dar, ds, taban(dk, ay))
                  + ('; fazla sûre içi eş okunmamış (fark test edilmedi)' if sd(key)['henuz_si'] else ''))
    r5.append(h)

K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k}

M15 = ("5:15 'Ey kitap ehli' ('yâ ehle'l-kitâb', 'yâ' 1. kelimede 'ey' ile (morph VOC), 'ehil' 'ehl' karşılığı (1. kelime; '-i' iyelik takdiri), 'kitap' 'kitâb' karşılığı (2. kelime; izafet), sıralama: izafet Türkçe sırasıyla); "
 "'Elçimiz size geldi' ('qad câ'akum rasûlunâ', 'qad' 3. kelimede karşılıksız (morph CERT; geçmiş '-di' içinde), 'gel-' 'câ'a' karşılığı (4. kelime), 'kum' 4. kelimede 'size' ile ('-e' fiil yönetimi takdiri), 'elçi' 'rasûl' karşılığı (5. kelime), 'nâ' 5. kelimede '-miz' iyelik ile, sıralama: fail öne, fiil sona alındı); "
 "'kitaptan gizlemekte olduğunuz şeylerin çoğunu size açıklıyor' ('yubeyyinu lekum kesîran mimmâ kuntum tuxfûne mine'l-kitâb', 'açıkla-' 'yubeyyinu' karşılığı (6. kelime; II. bab; LEM 'beyyen' (morph LEM ham biçim)), 'li' 7. kelimede '-e' ile, 'kum' 7. kelimede 'siz' ile, "
 "'çok' 'kesîr' karşılığı (8. kelime; iyelik ve belirtme takdiri), 'min' 9. kelimede '-in' ile (izafet), 'mâ' 9. kelimede 'şey' ile (çoğul takdiri), 'ol-' 'kuntum' karşılığı (10. kelime; '-makta ol-' — süreklilik), 'tum' 10. kelimede '-unuz' ile, "
 "'gizle-' 'tuxfûne' karşılığı (11. kelime; IV. bab; LEM 'uxfiye' (morph LEM ham biçim)), 'ûne' 11. kelimede karşılıksız ('olduğunuz' içinde), 'min' 12. kelimede '-tan' ile, 'kitap' 'kitâb' karşılığı (13. kelime), sıralama: fiil sona alındı); "
 "'çoğunu da affediyor' ('ve ya'fû 'an kesîr', 've' 14. kelimede 'da' ile (morph CONJ), 'affet-' ''afâ' karşılığı (14. kelime; '-iyor'), ''an' 15. kelimede karşılıksız (mef'ûl belirtme ile), 'çok' 'kesîr' karşılığı (16. kelime; iyelik ve belirtme takdiri), sıralama: fiil sona alındı); "
 "'Size Allah'tan bir nur ve apaçık bir kitap geldi' ('qad câ'akum mina'llâhi nûrun ve kitâbun mubîn', 'qad' 17. kelimede karşılıksız (morph CERT), 'gel-' 'câ'a' karşılığı (18. kelime), 'kum' 18. kelimede 'size' ile ('-e' fiil yönetimi takdiri), 'min' 19. kelimede karşılıksız ('Allah'tan' içinde), "
 "lafız 20. kelimede 'Allah'tan' ile, 'nur' 'nûr' karşılığı (21. kelime; nekre — 'bir' takdiri), 've' 22. kelimede 've' ile (morph CONJ), 'kitap' 'kitâb' karşılığı (22. kelime; nekre — 'bir' takdiri), 'apaçık' 'mubîn' karşılığı (23. kelime; etken ortaç), sıralama: tümleç öne, fiil sona alındı)")
M16 = ("5:16 'Allah onunla … iletir' ('yehdî bihi'llâh', 'ilet-' 'yehdî' karşılığı (1. kelime; geniş zaman), 'bi' 2. kelimede '-la' ile, 'hî' 2. kelimede 'onun' ile (gönderge kitap), lafız 3. kelimede 'Allah' ile, sıralama: fail öne, fiil sona alındı); "
 "'rızasına uyanları' ('meni'ttebe'a ridvânehu', 'men' 4. kelimede '-anları' ile (ilgi; çoğul okuma), 'uy-' 'ttebe'a' karşılığı (5. kelime; VIII. bab), 'rıza' 'ridvân' karşılığı (6. kelime; '-a' fiil yönetimi takdiri), 'hu' 6. kelimede iyelik ile ('rızasına' içinde), sıralama: tümleç öne); "
 "'esenlik yollarına' ('subule's-selâm', 'yol' 'sebîl' karşılığı (7. kelime; çoğul '-lar'; iyelik takdiri; yönelme — fiil yönetimi takdiri), 'esenlik' 'selâm' karşılığı (8. kelime; izafet)); "
 "'kendi izniyle onları karanlıklardan nura çıkarır' ('ve yuxricuhum mine'z-zulumâti ile'n-nûri bi-iznih', 've' 9. kelimede karşılıksız (noktalı virgül; morph CONJ), 'çıkar-' 'yuxricu' karşılığı (9. kelime; IV. bab; geniş zaman), 'hum' 9. kelimede 'onları' ile, 'min' 10. kelimede '-dan' ile, "
 "'karanlık' 'zuleme' karşılığı (11. kelime; çoğul '-lar'), 'ilâ' 12. kelimede '-a' ile, 'nur' 'nûr' karşılığı (13. kelime), 'bi' 14. kelimede '-yle' ile, 'izin' 'izn' karşılığı (14. kelime; iyelik ile 'izni'), 'hî' 14. kelimede 'kendi' ile (gönderge lafız), sıralama: 'bi-iznih' öne, fiil sona alındı); "
 "'ve onları dosdoğru bir yola iletir' ('ve yehdîhim ilâ sırâtin mustaqîm', 've' 15. kelimede 've' ile (morph CONJ), 'ilet-' 'yehdî' karşılığı (15. kelime; geniş zaman), 'him' 15. kelimede 'onları' ile, 'ilâ' 16. kelimede '-a' ile, 'yol' 'sırât' karşılığı (17. kelime; nekre — 'bir' takdiri), "
 "'dosdoğru' 'mustaqîm' karşılığı (18. kelime; etken ortaç), sıralama: fiil sona alındı)")
M17 = ("5:17 'Andolsun' ('leqad', 'le' 1. kelimede 'andolsun' ile (morph EMPH), 'qad' 1. kelimede karşılıksız (morph CERT; '-miştir' içinde)); "
 "'diyenler inkâr etmiştir' ('kefera'llezîne qâlû', 'inkâr et-' 'kefera' açılımı (2. kelime; '-miştir'), 'ellezîne' 3. kelimede '-enler' ile, 'de-' 'qâlû' karşılığı (4. kelime), 'û' 4. kelimede karşılıksız (fail eki — '-enler' içinde), sıralama: söz öne, fiil sona alındı); "
 "'Şüphesiz Allah, Meryem oğlu Mesih'tir' ('inna'llâhe huve'l-mesîhu'bnu meryem', 'inne' 5. kelimede 'şüphesiz' ile, lafız 6. kelimede 'Allah' ile, 'huve' 7. kelimede karşılıksız (fasıl zamiri), 'Mesih' 'mesîh' karşılığı (8. kelime; özel ad; '-tir' takdir), "
 "'oğul' 'ibn' karşılığı (9. kelime; '-u' iyelik), 'Meryem' 'meryem' karşılığı (10. kelime; özel ad; izafet), sıralama: izafet Türkçe sırasıyla); "
 "'De ki' ('qul', 'de-' 'qul' karşılığı (11. kelime; emir 2MS), 'ki' takdir (11. kelime; söz açılışı)); "
 "'Allah'a karşı kim bir şeye güç yetirebilir' ('fe-men yemliku mina'llâhi şey'en', 'fe' 12. kelimede karşılıksız (morph SUP), 'men' 12. kelimede 'kim' ile (soru; morph INTG), 'güç yetir-' 'yemliku' açılımı (13. kelime; yeterlik '-ebil-' takdiri; LEM 'meleket' (morph LEM ham biçim)), "
 "'min' 14. kelimede 'karşı' ile, lafız 15. kelimede 'Allah'a' ile ('karşı' yönetimi), 'şey' 'şey'' karşılığı (16. kelime; nekre — 'bir' takdiri; '-e' fiil yönetimi takdiri), sıralama: fiil sona alındı); "
 "'Eğer Allah Meryem oğlu Mesih'i, annesini ve yeryüzündekilerin hepsini helâk etmek isterse' ('in erâde en yuhlike'l-mesîha'bne meryeme ve ummehû ve men fi'l-ardi cemî'an', 'in' 17. kelimede 'eğer' ile (şart; morph COND), 'iste-' 'erâde' karşılığı (18. kelime; IV. bab; '-se' şart eki), "
 "'Allah' takdir (18. kelime; fail zamiri — gönderge lafız), 'en' 19. kelimede '-mek' ile (masdar; morph SUB), 'helâk et-' 'yuhlike' açılımı (20. kelime; IV. bab), 'Mesih' 'mesîh' karşılığı (21. kelime; '-i' belirtme), 'oğul' 'ibn' karşılığı (22. kelime; '-u' iyelik), "
 "'Meryem' 'meryem' karşılığı (23. kelime), 've' 24. kelimede karşılıksız (virgül; morph CONJ), 'anne' 'umm' karşılığı (24. kelime), 'hû' 24. kelimede iyelik ile ('annesini' içinde), 've' 25. kelimede 've' ile (morph CONJ), 'men' 25. kelimede '-ler' ile (ilgi; 'yeryüzündekiler'), "
 "'fî' 26. kelimede '-de' ile ('-ki' takdir), 'yeryüzü' 'ard' karşılığı (27. kelime), 'hepsi' 'cemî'' karşılığı (28. kelime; belirtme takdiri), sıralama: fiil sona alındı); "
 "'Göklerin, yerin ve ikisi arasındakilerin mülkü Allah'ındır' ('ve li'llâhi mulku's-semâvâti ve'l-ardi ve mâ beynehumâ', 've' 29. kelimede karşılıksız (nokta; morph REM), 'li' 29. kelimede '-ın' ile (aidiyet), lafız 29. kelimede 'Allah' ile, 'mülk' 'mulk' karşılığı (30. kelime; '-ü' iyelik), "
 "'gök' 'semâ'' karşılığı (31. kelime; çoğul '-ler'; izafet), 've' 32. kelimede karşılıksız (virgül; morph CONJ), 'yer' 'ard' karşılığı (32. kelime; izafet), 've' 33. kelimede 've' ile (morph CONJ), 'mâ' 33. kelimede '-kiler' ile (ilgi), "
 "'ara' 'beyn' karşılığı (34. kelime; yer eki takdiri), 'humâ' 34. kelimede 'ikisi' ile (ikil), '-dır' takdir (29. kelime; isim cümlesi), sıralama: haber sona alındı); "
 "'dilediğini yaratır' ('yaxluqu mâ yeşâ'', 'yarat-' 'yaxluqu' karşılığı (35. kelime; geniş zaman), 'mâ' 36. kelimede '-diğini' ile (ilgi), 'dile-' 'yeşâ'' karşılığı (37. kelime), sıralama: fiil sona alındı); "
 "'Allah her şeye güç yetirendir' ('ve'llâhu 'alâ kulli şey'in qadîr', 've' 38. kelimede karşılıksız (nokta; morph REM), lafız 38. kelimede 'Allah' ile, ''alâ' 39. kelimede '-e' ile ('-e' fiil yönetimi takdiri), 'her' 'kull' karşılığı (40. kelime), 'şey' 'şey'' karşılığı (41. kelime), "
 "'güç yetiren' 'qadîr' açılımı (42. kelime), '-dir' takdir (42. kelime), sıralama: haber sona alındı)")
MEALS = (M15, M16, M17)
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
open('/home/claude/b06/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '6')
ESL = run('/home/claude/sunum/es_lemma.py', '5', '6').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '6').replace('\n', '; ')
EMS = open('/home/claude/b06/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '15', '17', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b06/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
MFARK = [(k, n, sayim.S2[k.replace(' --medde', '')][0]) for k, (n, d) in sayim.S2.items() if '--medde' in k]
MEDF = '; '.join("%s meddeli %d / meddesiz %d" % (k.replace(' --medde', ''), m, n) for k, n, m in MFARK)
MEDF += ' — fark yok, yeni eş yok' if all(n == m for k, n, m in MFARK) else ' — FARK VAR'

I = [
 "kök tablosu: ölçümde '???' 5:15, 5:16 ve 5:17 için ayrı sayıldı — 0; yeni kök yok (okunan ayetlerde tabloda olmayan kök 0); ölçüm glossunun karşılamadığı kullanımlar (bölüm 2 denetimi kuralı 9, tarama): kök بني 'bina, yapma' 5:17 ''bnu' / ''bne' (oğul) kullanımını kapsamıyor (blok 5'te 'benî' için de kayıtlı); "
 "kök ملك 'mülk; melik' 5:17 'yemliku' (güç yetirme, sahip olma) kullanımını kısmen kapsıyor; kök سلم 'esenlik; teslim olma' 5:16 's-selâm' kullanımını kapsıyor; kök رضو 'razı olma, hoşnutluk' 5:16 'ridvânehu'; kök خفي 'gizleme, gizli olan' 5:15 'tuxfûne'; kök صرط 'yol, sırât' 5:16 'sırâtin'; kök هلك 'helâk' 5:17 'yuhlike' — kapsıyor; tam okuma sonu",
 "esmâ: 5:15:21 نُور 'degil' — 'qad câ'akum mina'llâhi nûrun', kural 'esmâ adı esmâ dışı göndergeyle → degil' (gelen nur); 5:15:23 مُبِين 'degil' — 'nûrun ve kitâbun mubîn', kural 'esmâ adı esmâ dışı göndergeyle → degil' (kitabın sıfatı); "
 "5:16:8 سَلام 'degil' — 'subule's-selâm', kural 'esmâ adı esmâ dışı göndergeyle → degil' (yolların izafeti); 5:16:13 نُور 'degil' — 'mine'z-zulumâti ile'n-nûr', kural 'esmâ adı esmâ dışı göndergeyle → degil' (karanlıklar karşıtı); "
 "5:17:42 قَدِير 'ilahi' — 've'llâhu 'alâ kulli şey'in qadîr', kural ''ve'llâhu X' kuralı → ilahi' (esma_el_ekle → esma_kayit; e_el=? 0); kural adları kapalı listeyle karşılaştırıldı; 'degil' göndergeleri A1'de; "
 "yorum kaydı (tam okuma sonu, kullanıcı kararı gerektirir): 5:16 'subule's-selâm' izafetinde 'es-selâm' esmâ adı olarak da okunabilir ('Selâm'ın yolları') — 'degil' kararı gönderge yollar olduğu için, onaya açık; 5:15 'nûr' göndergesi (elçi / kitap) tefsir konusu, 'degil' kararı değişmiyor; lafız 5:15 bir, 5:16 bir, 5:17 dört geçiş; Rab yok",
 "esma_kayit: 5:15 ölçüm esmâ '{{1|نُور 21\\. sırada, SON konum, MÜHÜRSÜZ \\| مُبِين 23\\. sırada, SON konum, MÜHÜRSÜZ}}' / esma_kayit 'mühür EVET (ÇİFT) ton denge' (uyuşmuyor); 5:16 ölçüm esmâ '{{2|سَلام 8\\. sırada, ORTA konum, MÜHÜRSÜZ \\| نُور 13\\. sırada, ORTA konum, MÜHÜRSÜZ}}' / esma_kayit 'mühür hayır' (uyuşuyor); "
 "5:17 ölçüm esmâ '{{3|قَدِير 42\\. sırada, SON konum, MÜHÜRSÜZ}}' / esma_kayit 'mühür EVET ton celâl' (uyuşmuyor) — mühür ölçütleri farklı (araç tanımı farkı); 5:15'te esma_kayit 'degil' adlarını mühüre sayıyor (§8)",
 "ölçüm: 5:15 '{{1|yıldız yok}}', '{{1|fâsıla مبين → ن, N sınıfı}}', '{{1|sayı işareti كَثِير, كَثِير}}', '{{1|simetri \\[4, 7, 15, 1\\]}}', '{{1|harf 96 → harf3 89, isaret 7}}', '{{1|dış düğüm 1}}' ve '{{1|İÇ düğüm 1}}'; "
 "5:16 '{{2|yıldız yok}}', '{{2|fâsıla مستقيم → م, N sınıfı}}', '{{2|simetri \\[3, 1, 15, 1\\]}}', '{{2|harf 80 → harf3 76, isaret 4}}' ve '{{2|dış düğüm 1}}'; "
 "5:17 '{{3|fâsıla قدير → ر, R sınıfı}}', '{{3|simetri \\[6, 1, 10, 2\\]}}', '{{3|harf 164 → harf3 155, isaret 9}}', '{{3|dış düğüm 5}}' ve '{{3|İÇ düğüm 2}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); 5:16'da İÇ düğüm alanı yok",
 "ölçüm aktör: 5:17 '{{3|adlı مَسِيح 8\\. sırada \\(kisi, rol fail\\+meful\\)}}', '{{3|adlı مَرْيَم 10\\. sırada \\(kisi, rol mecrur\\)}}', '{{3|adlı مَسِيح 21\\. sırada \\(kisi, rol fail\\+meful\\)}}', '{{3|adlı مَرْيَم 23\\. sırada \\(kisi, rol mecrur\\)}}' — sözdiziminde 8. kelime söz içi haber ('inne' cümlesi), 21. kelime 'yuhlike' mef'ûlü; ölçüm rolü 'fail+meful' iki konumu ayırt etmiyor (araç tanımı farkı, §8); 5:15 ve 5:16 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle): 5:15 nida — CERT 2 'qad' (3., 17.), VOC 1 'yâ' (1.); 5:16 haber — kip yok; 5:17 soru, emir, şart — CERT 1 'qad' (1.), COND 1 'in' (17.), EMPH 1 'le' (1.), IMPV 1 'qul' (11.), INTG 1 'men' (12.); blokta edilgen fiil yok",
 "yıldız: 5:17 ★★★; 5:15 ve 5:16 yıldız yok — satır yıldız kaynağını adlandırmıyor; kaynak kapanış notunda bilançodan",
 "fâsıla: 5:14 ن (يصنعون) → 5:15 ن (مبين) → 5:16 م (مستقيم) → 5:17 ر (قدير, R sınıfı); N sınıfı 5:14-16 boyunca, ر 5:17'de (ölçüm kırılma demiyor); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref: 5:15 xref okunmamış iki ayet (sûre içi 1); 5:16 xref 14:1 (basılmış); 5:17 xref 9:31, 14:8 ve 48:11 (basılmış), okunmuş iki ayet, okunmamış iki ayet (sûre içi 2) — sınıflama sinifla.py ile, basılmamışlar numarasız",
 "nakarat3 (R3: sayıyla özetlendi): 5:15 bir kalıp: süzgeç GEÇER; 5:16 kalıp yok; 5:17 on iki kalıp: onu süzgeç GEÇER, ikisi GEÇMEZ; bütün kalıplar tür ic",
 "araç tanımı farkları (R5; bölüm 2 denetimi kuralı 1: nakarat3 'tür' alanı 'tam' ya da 'ic' — ikisi de sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si — taban sayımın kendi sözlüğünden betikle; karşılaştırma eşit aralıkla; nakarat3 kalıp adları ham LEM ile, bozuk LEM notlu): " + '; '.join(r5),
 "aktör / ad (1017, R1): 5:15 muhatap 2MP (adsız; nidâ 'ehle'l-kitâbi'), 'rasûlunâ', konuşan 1P (adsız), 3MS (adsız — elçi), Allah (lafız), 'nûrun ve kitâbun mubîn'; 5:16 Allah (lafız), 'meni'ttebe'a ridvânehu', 3MS / 3MP (adsız); "
 "5:17 'llezîne qâlû', Allah (lafız), 'l-mesîhu'bnu meryem' / 'l-mesîha'bne meryeme' (adlı kişi), muhatap 2MS (adsız; 'qul'), 'men' (soru), 'ummehû', 'men fi'l-ardi', 3D 'beynehumâ' — "
 "A1'e yazılmayanlar: 5:15 'lekum' (muhatap içinde anıldı), 'mimmâ' (ilgi; 'kesîran' tümleci); 5:17 'mâ' 33. ve 36. kelime (mevsûl; meal maddesinde); blokta 'kâne / leyse' ismi nekre yok ('kuntum' ismi muhatap)",
 "söz / tırnak: 5:17 'qâlû' (4. kelime) — söz 5. kelimede açılıyor, 10. kelimede kapanıyor ('inna'llâhe huve'l-mesîhu'bnu meryem'; 11. kelime 'qul' anlatı içi emir); 'qul' (11. kelime) — söz 12. kelimede açılıyor, 28. kelimede kapanıyor (29. kelime 've li'llâhi' morph REM — sözün açıkça bittiği yer okuma kararı; söz sonu 42. kelimeye dek de okunabilir, tam okuma sonu); "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:15 've ya'fû' (14.), 've kitâbun' (22.) CONJ; 5:16 've yuxricuhum' (9.), 've yehdîhim' (15.) CONJ; 5:17 'fe-men' (12.) SUP, 've ummehû' (24.), 've men' (25.), 've'l-ardi' (32.), 've mâ' (33.) CONJ, 've li'llâhi' (29.), 've'llâhu' (38.) REM",
 "◈ tetik (alıntılar önek ve edatsız): 5:17 ◈K سمو ('s-semâvâti' 31. kelime — K1), أرض ('l-ardi' 27. ve 32. kelime — K1); 5:17 ◈B خلق ('yaxluqu' 35. kelime — B1); 5:15 ve 5:16 tetik yok; "
 "tetik listesinde olmayan zaman adı ve organ adı (bölüm 2 denetimi kuralı 9, tarama): 5:15 'kuntum tuxfûne' (süreklilik, zaman adı değil) — zaman adı yok; 5:16 'z-zulumâti' / 'n-nûri' (karanlık / ışık — tetik listesinde değil; ölçüm kökü نور 'nûr, ışık'); 5:17 'umm' (akrabalık adı, tetik dışı); organ adı yok; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:15 (42:30), 5:16 (2:142, 2:257, 14:1), 5:17 (2:284, 3:47, 9:31, 14:8, 48:11) (kontrol.py ile); blok içi bağ yok; bölüm içi blok geçişi 5:14 → 5:15 sayımlı eş vermedi; "
 "D3 dışı bırakılan basılmış sayım eşleri: lemma 'uxfiye' (5:15 11. kelime) sayımındaki 40:19 ve 60:1 (bağları blok 5'te) ve 2:284 (bağı 5:17'de); lemma 'ridvân' (5:16 6. kelime) sayımındaki 5:2 ve 48:29 (genel lemma; bağları bölüm 1-2'de); "
 "bölüm 2 denetimi kuralı 10 (genel hitap kalıbında bağ ölçütü bir): 'yâ ehle'l-kitâb' (5:15 1-2. kelime) hitabının eşlerinin hiçbirine bağ kurulmadı (okunmuş yedi eş, basılmış eş yok); 'ilâ sırâtin mustaqîm' ve ''alâ kulli şey'' genel kalıplarında bağ yalnız emsal olarak basılan, bağlamı eş ayetlere (2:142 'yehdî', 2:284 'yeşâ'') — gerekçe: eşlerin geri kalanı basılmadı, bağ ölçütü 'kalıp + bağlam'",
 "◈A A4 (R9 + kapsam): 5:15 hitap açılır ('yâ ehle'l-kitâbi', 1-2. kelime); edim geçişi haber → nida (ayetler arası); şahıs geçişi 3 → 2 (ayetler arası); 5:16 edim geçişi nida → haber (ayetler arası); şahıs geçişi 2 → 3 (ayetler arası); "
 "5:17 edim geçişi haber → soru, emir, şart (ayetler arası); şahıs geçişi yok (3 → 3); söz açılır / kapanır (5-10. ve 12-28. kelime); şart COND 'in' 17. kelime: 'erâde en yuhlike' / 'fe-men yemliku' — cevap öne alınmış",
 "sözdizimi (okuma; 'atıf' / 'istînâf' / 'hâl' her geçişte morph etiketiyle; 'X'a atıf' yazımında X ma'tûf aleyh): 5:15 'yâ ehle'l-kitâbi' — nidâ; 'qad câ'akum rasûlunâ' — fiil cümlesi; 'yubeyyinu lekum' — 'rasûlunâ'nın hâli ya da sıfatı (morph etiketi yok); 've ya'fû' — 'yubeyyinu'ya atıf (morph CONJ); "
 "'qad câ'akum mina'llâhi nûrun' — yeni cümle (morph etiketi yok); 've kitâbun' — 'nûrun'a atıf (morph CONJ); 5:16 'yehdî bihi'llâhu' — 5:15 'kitâbun mubîn'in sıfatı okunabilir (morph etiketi yok; ayet başında bağlaç yok); 've yuxricuhum' — 'yehdî'ye atıf (morph CONJ); 've yehdîhim' — 'yuxricuhum'a atıf (morph CONJ); "
 "5:17 'leqad kefera' — yemin 'le' + 'qad'; 'inna'llâhe huve'l-mesîh' — söz içi 'inne' cümlesi, 'huve' fasıl zamiri; 'qul' — emir; 'fe-men yemliku' — soru (morph SUP 'fe' + INTG 'men'); 'in erâde' — şart, cevabı öne alınmış; 've ummehû' ve 've men fi'l-ardi' — 'l-mesîha'ya atıf (morph CONJ); "
 "'ve li'llâhi mulku' — istînâf (morph REM); 'yaxluqu mâ yeşâ'' — yeni cümle; 've'llâhu 'alâ kulli şey'in qadîr' — istînâf (morph REM)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile denetlendi; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için): 5:15 'yâ ehle'l-kitâb' nidâsıyla açılıyor (1-2. kelime) — bölümde kitap ehline yeni hitap; 5:15 'qad câ'akum' iki geçiş (3-4. ve 17-18. kelime) — elçi / nur ve kitap; 5:15 lemma 'kesîr' iki geçiş (8. ve 16. kelime) — açıklanan / affedilen; "
 "5:16 'mine'z-zulumâti ile'n-nûr' 2:257 ve 14:1 ile; 5:17 'l-mesîhu'bnu meryem' (8-10. kelime) ve 'l-mesîha'bne meryeme' (21-23. kelime) — söz içi iddia / şart içi helâk; 5:17 ''alâ kulli şey'in qadîr' kalıbı (39-42. kelime) ölçüm nakarat3'te süzgeç GEÇER; 5:17 'leqad kefera' ile açılıyor (1. kelime) — yemin pekiştirmesi",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (sunum/es_edat.py — morph etiketli, zamirler birleşik): " + ES
 + "; eş lemmaya farklı karşılık (sunum/es_lemma.py, bloklar 5-6): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (bölüm 2 denetimi kuralı 6): ''afâ' 5:15 'affet-' / 42:30 'affet-' (eş); 'zuleme' / 'nûr' 5:16 'karanlık' / 'nur' — 2:257 ve 14:1 'karanlık' / 'aydınlık' (fark); 'sırât mustaqîm' 5:16 'dosdoğru bir yol' / 2:142 (eş); "
 "'mesîh ibn meryem' 5:17 'Meryem oğlu Mesih' / 9:31 (eş); 'yemliku … mina'llâhi şey'en' 5:17 'güç yetir-' / 48:11 'güç yetir-' (eş — emsal karşılığı benimsendi); 'fi'l-ardi cemî'an' 5:17 'yeryüzündekilerin hepsi' / 14:8 'yeryüzündekilerin tamamı' (fark); "
 "'yaxluqu mâ yeşâ'' 5:17 / 3:47 'dilediğini yaratır' (eş); 'qadîr' 5:17 'güç yetiren' / 2:284 'güç yetiren' (eş) — tam okuma sonu",
 "KARSILIK_CAKISMA",
 "çıpa: 5:15 tarayıcı adayı (kök نور; F_ölçü) — çıpa değil: 'nûr' gelen elçi / kitap için (olgu=False); 5:17 tarayıcı adayı (kök أرض, خلق, سمو; A_şart) — çıpa değil: şart helâk tehdidinde, gökler ve yer mülk kapsamı, doğa iddiası yok (olgu=False); 5:16 tarayıcı vermedi (cipa_tarama5_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: ayet içi 5:15 ('yubeyyinu lekum kesîran' / 've ya'fû 'an kesîr'), 5:16 ('z-zulumâti' / 'n-nûri'), 5:17 ('inna'llâhe huve'l-mesîhu'bnu meryem' / 'en yuhlike'l-mesîha'bne meryeme') — okuma; ayetler arası yok",
 "aday 1041: kök ملك 5:17 'yemliku' (soru — insanın güç yetirmesi, olumsuz cevaplı) ve 'mulku' (lafız) — lafız göndergeli kökün insan için soru içinde kullanımı; kök قول 5:17 'qâlû' (insan) / 'qul' (Peygamber) — okuma",
 "bölüm: " + BOL + " bölümü, bölüm 3-2; bölüm üç blok (blok planından: 5, 6 ve 7); başlıktaki 'kitap ehline gelen elçi' 5:15 ('yâ ehle'l-kitâbi qad câ'akum rasûlunâ'), 'Mesih hakkında söz' 5:17 ('inna'llâhe huve'l-mesîhu'bnu meryem'); mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; "
 "medde taraması (bölüm 2 denetimi kuralı 2; sunum/medde.py b06/say2.txt — --medde satırları say2'de): " + MED + "; " + MEDF,
 "ham LEM (bölüm 2 denetimi kuralları 4-5; sunum/lem_bozuk.py 06): 5:15:6 'beyyen', 5:17:13 'meleket' — meal maddelerinde ve R5 kalıp adında '(morph LEM ham biçim)' notlu; aracın bayraklamadığı ham biçim: 5:15:11 'uxfiye' (edilgen görünümlü LEM, fiil etken IV. bab) — notlu",
 "sonradan basılan (bölüm 8 kuralı 1; bölüm 16 denetimi kuralı 3; bölüm 1 denetimi kuralı 1 — lemma dizileri dahil; sunum/sonradan.py --plan 6): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('ehl', 'kitâb', 'rasûl', 'kesîr', 'nûr', 'mubîn', 'ridvân', 'sebîl', 'selâm', 'zuleme', 'izn', 'sırât', 'mustaqîm', 'mesîh', 'ibn', 'meryem', 'şey'', 'umm', 'ard', 'cemî'', 'mulk', 'semâ'', 'beyn', 'kull', 'qadîr'); ortaçlarda bab etiketi ◇'de yazılmadı; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları ve 5:17 'meryeme ve ummehû' hemze sınırı yapıntısı (translit_kontrol 'm' farkı — iskelet tekilleştirmesi hemze ayrımından önce); wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]


def yaz():
    items = [kes(x) for x in I]
    s = '\n (15, 17): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_15_17.txt', 'w', encoding='utf-8').write(s)


idx = I.index('KARSILIK_CAKISMA')
I[idx] = 'karşılık çakışması (geçici)'
yaz()
CAK = run('/home/claude/sunum/cakisma.py', '/home/claude/yamalar/ariza_5_12_14.txt', '/home/claude/yamalar/ariza_5_15_17.txt')
KARAR = {}
exec(open('/home/claude/b05/yap/karar.py', encoding='utf-8').read())
if os.path.exists('/home/claude/b06/yap/karar.py'): exec(open('/home/claude/b06/yap/karar.py', encoding='utf-8').read())
I[idx] = ("karşılık çakışması (sunum/cakisma.py bölüm 3 ARIZA meal maddeleri (bloklar 5-6); kararlar morph LEM eşitliğine göre): "
          + ('; '.join(KARAR.get(l.split(' ←')[0], l + ' — karar yok') for l in CAK.splitlines()) if CAK else 'çakışma yok'))
yaz()
print('yazıldı', len(I))
print(CAK)
print('\n'.join(r5))
print(MEDF)

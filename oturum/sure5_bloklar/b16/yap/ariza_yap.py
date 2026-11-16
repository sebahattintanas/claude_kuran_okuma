# blok 16 (5:45-47) ARIZA oluşturucu — bölüm 7-3
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b16/olcum.txt'
os.environ['SAY2'] = '/home/claude/b16/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
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
 ("5:45", "'men lem hakeme mâ enzele allâh zâ _'", 2, 'say 5:45 23-30 --on', "önek kesilmiş 've men lem yahkum bi-mâ enzele'llâhu fe-ulâ'ike hum' (23-30. kelime)",
  ('dizi 5 45 23 30', "men lem hakeme mâ enzele allâh zâ _", '23-30', "önek kesilmiş sayım ('say 5:45 23-30 --on') ve lemma dizisi ('dizi 5 45 23 30') sûre içi 3 (5:44, 5:45, 5:47); nakarat3 8 kelimelik kalıbı 2 ayet sayıyor — fark açıklanmadı, tam okuma sonu")),
 ("5:45", "'lem hakeme mâ enzele allâh zâ _'", 3, 'say 5:45 24-30', "harekesiz 'lem yahkum bi-mâ enzele'llâhu fe-ulâ'ike hum' (24-30. kelime)", None),
 ("5:45", "'mâ enzele allâh'", 5, 'say 5:45 26-28', "harekesiz 'bi-mâ enzele'llâh' (26-28. kelime)", None),
 ("5:46", "'musaddiq mâ beyn yed min'", 2, 'say 5:46 7-11', "harekesiz 'musaddiqan li-mâ beyne yedeyhi min' (7-11. kelime)", None),
 ("5:47", "'men lem hakeme mâ enzele allâh zâ _'", 2, 'say 5:47 8-15 --on', "önek kesilmiş 've men lem yahkum bi-mâ enzele'llâhu fe-ulâ'ike hum' (8-15. kelime)",
  ('dizi 5 47 8 15', "men lem hakeme mâ enzele allâh zâ _", '8-15', "önek kesilmiş sayım ('say 5:47 8-15 --on') ve lemma dizisi ('dizi 5 47 8 15') sûre içi 3 (5:44, 5:45, 5:47); nakarat3 8 kelimelik kalıbı 2 ayet sayıyor — fark açıklanmadı, tam okuma sonu")),
 ("5:47", "'lem hakeme mâ enzele allâh zâ _'", 3, 'say 5:47 9-15', "harekesiz 'lem yahkum bi-mâ enzele'llâhu fe-ulâ'ike hum' (9-15. kelime)", None),
 ("5:47", "'mâ enzele allâh'", 5, 'say 5:47 11-13', "harekesiz 'bi-mâ enzele'llâh' (11-13. kelime)", None),
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

VF_YAZI = {45: {1: "'ve ketebnâ'", 7: "'ve'l-'ayne'", 9: "'ve'l-enfe'", 11: "'ve'l-uzune'", 13: "'ve's-sinne'", 15: "'ve'l-curûha'", 17: "'fe-men tesaddeqa'", 20: "'fe-huve'", 23: "'ve men lem'", 29: "'fe-ulâ'ike'"}, 46: {1: "'ve qaffeynâ'", 13: "'ve âteynâhu'", 17: "'ve nûrun'", 18: "'ve musaddiqan'", 24: "'ve hudan'", 25: "'ve mev'izatan'"}, 47: {1: "'ve'l-yahkum'", 8: "'ve men lem'", 14: "'fe-ulâ'ike'"}}
M45 = ("5:45 'Onlara orada şunu yazdık' ('ve ketebnâ 'aleyhim fîhâ', 've' 1. kelimede karşılıksız (morph CONJ), 'yaz-' 'ketebnâ' karşılığı (1. kelime; I. bab), 'nâ' 1. kelimede 1P ile ('yazdık' içinde), ''alâ' 2. kelimede yönelme eki ile ('Onlara' içinde; fiil yönetimi takdiri), 'him' 2. kelimede 'onlar' ile ('Onlara' içinde), 'fî' 3. kelimede '-da' ile ('orada' içinde), 'hâ' 3. kelimede 'ora' ile ('orada' içinde), 'şu' takdiri ('şunu' içinde; 'enne' cümlesinin önü), sıralama: fiil sona alındı); "
 "'cana can, göze göz, buruna burun, kulağa kulak, dişe diş karşılıktır' ('enne'n-nefse bi'n-nefsi ve'l-'ayne bi'l-'ayni ve'l-enfe bi'l-enfi ve'l-uzune bi'l-uzuni ve's-sinne bi's-sinn', 'enne' 4. kelimede karşılıksız (iki nokta ile), 'can' 'nefs' karşılığı (5. ve 6. kelime), 'bi' 6. kelimede yönelme eki ile ('cana' içinde; karşılık), "
 "'ve' 7. kelimede karşılıksız (morph CONJ; virgül), 'göz' ''ayn' karşılığı (7. ve 8. kelime), 'bi' 8. kelimede yönelme eki ile ('göze' içinde), 've' 9. kelimede karşılıksız (morph CONJ; virgül), 'burun' 'enf' karşılığı (9. ve 10. kelime), 'bi' 10. kelimede yönelme eki ile ('buruna' içinde), 've' 11. kelimede karşılıksız (morph CONJ; virgül), 'kulak' 'uzun' karşılığı (11. ve 12. kelime), 'bi' 12. kelimede yönelme eki ile ('kulağa' içinde), "
 "'ve' 13. kelimede karşılıksız (morph CONJ; virgül), 'diş' 'sinn' karşılığı (13. ve 14. kelime), 'bi' 14. kelimede yönelme eki ile ('dişe' içinde), 'karşılık' takdiri ('karşılıktır' içinde; 'bi' açılımı), '-tır' takdiri ('karşılıktır' içinde; 'enne' haberi), sıralama: karşılanan öne alındı); "
 "'yaralar da kısastır' ('ve'l-curûha qısâs', 've' 15. kelimede 'da' ile (morph CONJ), 'yara' 'curûh' karşılığı (15. kelime; çoğul '-lar'), 'kısas' 'qısâs' karşılığı (16. kelime; nekre — takdirsiz), '-tır' takdiri ('kısastır' içinde; haber)); "
 "'Kim onu sadaka olarak bağışlarsa' ('fe-men tesaddeqa bih', 'fe' 17. kelimede karşılıksız (morph REM), 'men' 17. kelimede 'kim' ile (morph COND; şart eki '-se' 'bağışlarsa' içinde), 'sadaka olarak bağışla-' 'tesaddeqa' açılımı (18. kelime; V. bab), 'bi' 19. kelimede belirtme eki ile ('onu' içinde; fiil yönetimi takdiri), 'hî' 19. kelimede 'onu' ile, sıralama: fiil sona alındı); "
 "'bu onun için bir keffarettir' ('fe-huve keffâratun leh', 'fe' 20. kelimede karşılıksız (morph RSLT; şart cevabı), 'huve' 20. kelimede 'bu' ile, 'keffaret' 'keffâra' karşılığı (21. kelime; nekre — 'bir' takdiri), 'li' 22. kelimede 'için' ile, 'hû' 22. kelimede 'onun' ile, '-tir' takdiri ('keffarettir' içinde; haber), sıralama: haber sona alındı); "
 "'Kim Allah'ın indirdiğiyle hüküm vermezse' ('ve men lem yahkum bi-mâ enzele'llâh', 've' 23. kelimede karşılıksız (morph CONJ), 'men' 23. kelimede 'kim' ile (morph COND; şart eki '-se' 'vermezse' içinde), 'lem' 24. kelimede olumsuzluk eki ile ('vermezse' içinde; morph NEG), 'hüküm ver-' 'yahkum' açılımı (25. kelime; I. bab), "
 "'bi' 26. kelimede vasıta eki ile ('indirdiğiyle' içinde), 'mâ' 26. kelimede '-diği' ile (ism-i mevsûl; 'indirdiğiyle' içinde), 'indir-' 'enzele' karşılığı (27. kelime; IV. bab), lafız 28. kelimede 'Allah' ile (ilgi eki 'Allah'ın' içinde), sıralama: şart sona alındı); "
 "'işte onlar zalimlerin ta kendileridir' ('fe-ulâ'ike humu'z-zâlimûn', 'fe' 29. kelimede 'işte' ile (morph RSLT; şart cevabı), 'ulâ'ike' 29. kelimede 'onlar' ile, 'hum' 30. kelimede 'ta kendileri' ile (ayırma zamiri), 'zalim' 'zâlim' karşılığı (31. kelime; çoğul '-ler'), '-dir' takdiri ('kendileridir' içinde; isim cümlesi haberi))")
M46 = ("5:46 'Onların izleri üzerinde, önündeki Tevrat'ı doğrulayıcı olarak Meryem oğlu İsa'yı ardlarından gönderdik' ('ve qaffeynâ 'alâ âsârihim bi-'îsa'bni meryeme musaddiqan li-mâ beyne yedeyhi mine't-tevrâh', 've' 1. kelimede karşılıksız (morph CONJ), 'ardlarından gönder-' 'qaffeynâ' açılımı (1. kelime; II. bab; LEM 'qaffey' (morph LEM ham biçim)), 'nâ' 1. kelimede 1P ile ('gönderdik' içinde), "
 "''alâ' 2. kelimede 'üzerinde' ile, 'iz' 'eser' karşılığı (3. kelime; çoğul '-ler'; iyelik ile 'izleri'), 'him' 3. kelimede 'onların' ile, 'bi' 4. kelimede belirtme eki ile ('İsa'yı' içinde; fiil yönetimi takdiri), 'İsa' ''îsâ' karşılığı (4. kelime; özel ad), 'oğul' 'ibn' karşılığı (5. kelime; iyelik ile 'oğlu'), 'Meryem' 'meryem' karşılığı (6. kelime; özel ad), "
 "'doğrulayıcı' 'musaddiq' karşılığı (7. kelime; nekre — takdirsiz; 'olarak' takdiri), 'li' 8. kelimede belirtme eki ile ('Tevrat'ı' içinde; fiil yönetimi takdiri), 'mâ' 8. kelimede '-deki' ile (ism-i mevsûl; 'önündeki' içinde), 'ön' 'beyn' açılımı (9. kelime; 'beyne yedeyh' — iki elinin arası), 'el' 'yed' karşılığı (10. kelime; ikil; 'önündeki' açılımı içinde), 'hî' 10. kelimede iyelik ile ('önündeki' içinde), "
 "'min' 11. kelimede karşılıksız (beyan 'min'i), 'Tevrat' 'tevrâ' karşılığı (12. kelime; özel ad), sıralama: hâl öne, fiil sona alındı); "
 "'ona da içinde hidayet ve nur bulunan, önündeki Tevrat'ı doğrulayıcı, sakınanlar için hidayet ve öğüt olan İncil'i verdik' ('ve âteynâhu'l-incîle fîhi hudan ve nûrun ve musaddiqan li-mâ beyne yedeyhi mine't-tevrâti ve hudan ve mev'izatan li'l-muttaqîn', 've' 13. kelimede 'da' ile (morph CONJ), 'ver-' 'âteynâ' karşılığı (13. kelime; IV. bab), 'nâ' 13. kelimede 1P ile ('verdik' içinde), 'hu' 13. kelimede 'ona' ile (yönelme eki — fiil yönetimi takdiri), "
 "'İncil' 'incîl' karşılığı (14. kelime; özel ad; belirtme eki ile 'İncil'i'), 'fî' 15. kelimede 'içinde' ile, 'hî' 15. kelimede karşılıksız ('içinde' iyeliği), 'hidayet' 'hudâ' karşılığı (16. kelime; nekre — takdirsiz), 've' 17. kelimede 've' ile (morph CONJ), 'nur' 'nûr' karşılığı (17. kelime; nekre — takdirsiz), 'bulun-' takdiri ('bulunan' içinde), "
 "'ve' 18. kelimede karşılıksız (morph CONJ; virgül), 'doğrulayıcı' 'musaddiq' karşılığı (18. kelime; nekre — takdirsiz), 'li' 19. kelimede belirtme eki ile ('Tevrat'ı' içinde), 'mâ' 19. kelimede '-deki' ile ('önündeki' içinde), 'ön' 'beyn' açılımı (20. kelime), 'el' 'yed' karşılığı (21. kelime; ikil; 'önündeki' açılımı içinde), 'hî' 21. kelimede iyelik ile ('önündeki' içinde), "
 "'min' 22. kelimede karşılıksız (beyan 'min'i), 'Tevrat' 'tevrâ' karşılığı (23. kelime), 've' 24. kelimede karşılıksız (morph CONJ; virgül), 'hidayet' 'hudâ' karşılığı (24. kelime; nekre — takdirsiz), 've' 25. kelimede 've' ile (morph CONJ), 'öğüt' 'mev'iza' karşılığı (25. kelime; nekre — takdirsiz), 'li' 26. kelimede 'için' ile, 'sakınan' 'muttaqî' karşılığı (26. kelime; VIII. bab ortacı; çoğul '-lar'), 'ol-' takdiri ('olan' içinde), sıralama: sıfatlar öne, fiil sona alındı)")
M47 = ("5:47 'İncil ehli, Allah'ın onda indirdiğiyle hüküm versin' ('ve'l-yahkum ehlu'l-incîli bi-mâ enzele'llâhu fîh', 've' 1. kelimede karşılıksız (morph CONJ), 'li' 1. kelimede emir eki ile ('versin' içinde; morph IMPV öneki), 'hüküm ver-' 'yahkum' açılımı (1. kelime; I. bab; 3. şahıs emir), 'ehil' 'ehl' karşılığı (2. kelime; iyelik ile 'ehli'), 'İncil' 'incîl' karşılığı (3. kelime; özel ad), "
 "'bi' 4. kelimede vasıta eki ile ('indirdiğiyle' içinde), 'mâ' 4. kelimede '-diği' ile (ism-i mevsûl; 'indirdiğiyle' içinde), 'indir-' 'enzele' karşılığı (5. kelime; IV. bab), lafız 6. kelimede 'Allah' ile (ilgi eki 'Allah'ın' içinde), 'fî' 7. kelimede '-da' ile ('onda' içinde), 'hî' 7. kelimede 'o' ile ('onda' içinde), sıralama: fiil sona alındı); "
 "'Kim Allah'ın indirdiğiyle hüküm vermezse' ('ve men lem yahkum bi-mâ enzele'llâh', 've' 8. kelimede karşılıksız (morph CONJ), 'men' 8. kelimede 'kim' ile (morph COND; şart eki '-se' 'vermezse' içinde), 'lem' 9. kelimede olumsuzluk eki ile ('vermezse' içinde; morph NEG), 'hüküm ver-' 'yahkum' açılımı (10. kelime; I. bab), "
 "'bi' 11. kelimede vasıta eki ile ('indirdiğiyle' içinde), 'mâ' 11. kelimede '-diği' ile (ism-i mevsûl; 'indirdiğiyle' içinde), 'indir-' 'enzele' karşılığı (12. kelime; IV. bab), lafız 13. kelimede 'Allah' ile (ilgi eki 'Allah'ın' içinde), sıralama: şart sona alındı); "
 "'işte onlar fâsıkların ta kendileridir' ('fe-ulâ'ike humu'l-fâsiqûn', 'fe' 14. kelimede 'işte' ile (morph RSLT; şart cevabı), 'ulâ'ike' 14. kelimede 'onlar' ile, 'hum' 15. kelimede 'ta kendileri' ile (ayırma zamiri), 'fâsık' 'fâsiq' karşılığı (16. kelime; çoğul '-lar'), '-dir' takdiri ('kendileridir' içinde; isim cümlesi haberi))")
MEALS = (M45, M46, M47)






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
open('/home/claude/b16/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '16')
BLOKLAR = [str(i) for i in range(1, 17)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR).replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '16').replace('\n', '; ')
EMS = open('/home/claude/b16/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '45', '47', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b16/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
MFARK = [(k, n, sayim.S2[k.replace(' --medde', '')][0]) for k, (n, d) in sayim.S2.items() if '--medde' in k]
MEDF = '; '.join("%s meddeli %d / meddesiz %d" % (k.replace(' --medde', ''), m, n) for k, n, m in MFARK)
MEDF += ' — fark yok, yeni eş yok' if all(n == m for k, n, m in MFARK) else ' — FARK VAR'
GLS = run('/home/claude/sunum/gloss_tara.py', '45', '47', '16').splitlines()

I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11): bu blokta araç değişmedi; sunum/sinifla.py (SON 47); bölüm 6 kurallarının araçları (bolum4 / bolum5 / bolum6_kurallar, mutasyon_sina — MUT_SONUC) koşuldu",
 "kök tablosu: ölçümde '???' 5:45-47 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 45 47 16'): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:46:17 نُور 'degil' — 'hudan ve nûrun', kural 'esmâ adı esmâ dışı göndergeyle → degil' (İncil'deki nur) (esma_el_ekle → esma_kayit; bölüm 6 kuralı 14 — betikle, sapma B6_ESMA); 5:45 ve 5:47 esmâ yok; lafız 5:45, 5:47; 5:46 lafız yok; Rab yok",
 "esma_kayit: 5:45 'mühür hayır' (uyuşuyor), 5:46 'mühür hayır' (sınıf E/E; ölçüm MÜHÜRSÜZ — uyuşuyor), 5:47 'mühür hayır' (uyuşuyor)",
 "ölçüm: 5:45 '{{1|fâsıla ٱلظلمون → ن, N sınıfı}}', '{{1|simetri \\[4, 2, 22, 1\\]}}', '{{1|harf 146 → harf3 139, isaret 7}}' ve '{{1|dış düğüm 0}}'; 5:46 '{{2|lafız YOK · Rab YOK}}', '{{2|fâsıla للمتقين → ن, N sınıfı}}', '{{2|simetri \\[10, 4, 15, 3\\]}}', '{{2|harf 124 → harf3 117, isaret 7}}' ve '{{2|dış düğüm 3}}'; "
 "5:47 '{{3|aktör: adlı إِنجِيل 3\\. sırada \\(kitab, rol mecrur\\)}}', '{{3|fâsıla ٱلفسقون → ن, N sınıfı}}', '{{3|simetri \\[6, 4, 11, 1\\]}}', '{{3|harf 67 → harf3 65, isaret 2}}' ve '{{3|dış düğüm 0}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 45 47 16'): KALAN_P",
 "ölçüm aktör: 5:45 aktör yok; 5:46 adlı İsa, Meryem (kişi, mecrur), Tevrat (kitap, mecrur), İncil (kitap, meful); 5:47 adlı İncil (kitap, mecrur) — A1'de 'adlı aktör' etiketiyle",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle): 5:45 şart — COND 2 'men' (17., 23.), NEG 1 'lem' (24.); 5:46 haber, kip yok; 5:47 emir, şart — IMPV 1 'l-yahkum' (1.), COND 1 'men' (8.), NEG 1 'lem' (9.)",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 5:45 ★ (kaynak n, z=1,97); 5:47 ★ (kaynak allah, z=1,97); 5:46 yıldız yok",
 "fâsıla: 5:44 ن (الكافرون) → 5:45 ن (الظالمون) → 5:46 ن (للمتقين) → 5:47 ن (الفاسقون); hepsi N sınıfı; 5:44 / 5:45 / 5:47 kapanışları 'humu'l-…' ile üç sıfat (kâfirûn / zâlimûn / fâsiqûn); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref: 5:45 ve 5:47 xref yok; 5:46 3:138 (emsal olarak basıldı) ve okunmuş başka ayetler",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, joker '_' ile; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:45 ve 5:47 'men lem hakeme mâ enzele allâh zâ _', 'lem hakeme mâ enzele allâh zâ _' ve 'mâ enzele allâh' süzgeç GEÇER; 5:46 'musaddiq mâ beyn yed min' GEÇER",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15 — ölçüt: 1P / 1S / 2MS / 2FS / 2MP / 2FP / 2D / 3MS / 3FS / 3D / 3MD / 3FD / 3MP / 3FP zamirlerin hepsi 'adsız', etiketin kendi parantezinde; adlı aktör ölçümün 'aktör: adlı' alanından): "
 "5:45 konuşan 1P (adsız), 3MP (adsız), 3FS (adsız — 'fîhâ'), 3MS (adsız — 'tesaddeqa', 'yahkum', 'enzele' failleri; 'bihî', 'huve', 'leh'), Allah (lafız), 'men', 'qısâs', 'keffâratun'; 5:46 konuşan 1P (adsız), 3MP (adsız), 3MS (adsız — 'yedeyhi', 'âteynâhu', 'fîhi'), İsa, Meryem, Tevrat, İncil (adlı aktör); "
 "5:47 'ehlu'l-incîl' (adlı aktör), 3MS (adsız — 'l-yahkum', 'yahkum', 'enzele' failleri; 'fîh'), Allah (lafız), 'men' — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): blokta 'qâle' yok, söz aralığı yok (A3 —); 5:45 ve 5:46 konuşan 1P doğrudan anlatım; REM sapması (komut 'python3 sunum/bolum4_kurallar.py 45 47 16' — A3 aralığında morph REM): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:45 've' (1., 7., 9., 11., 13., 15., 23.) CONJ, 'fe-men' (17.) REM, 'fe-huve' (20.) ve 'fe-ulâ'ike' (29.) RSLT; 5:46 've' (1., 13., 17., 18., 24., 25.) CONJ; 5:47 've' (1., 8.) CONJ, 'fe-ulâ'ike' (14.) RSLT",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 5:45 ◈B عين ('l-'ayne' 7. kelime, 'l-'ayni' 8. kelime — B3; anlam notu: kısasta göz); 5:46 ◈B يدي ('yedeyhi' 10. ve 21. kelime — B3; anlam notu: 'beyne yedeyh' — önündeki, mecaz); 5:47 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 45 47 16'): TETIKDISI; anılış: 5:45 kök نفس ('n-nefse' 5., 'n-nefsi' 6. kelime — can), أنف ('l-enfe' 9., 'l-enfi' 10. kelime — burun, beden), أذن ('l-uzune' 11., 'l-uzuni' 12. kelime — kulak, beden), سنن ('s-sinne' 13., 's-sinni' 14. kelime — diş, beden), "
 "جرح ('l-curûha' 15. kelime — yara, beden), قصص ('qısâs' 16. kelime — kısas); B3 alanına yakın organ adları tetik listesi dışında — 5:45 ◈B'de yalnız عين; 5:46 أثر ('âsârihim' 3. kelime — iz); oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:45 (2:178), 5:46 (57:27, 3:138), 5:47 (3:82) (kontrol.py ile); blok geçişi 5:44 → 5:45: ayetler arası kalıp 'lem yahkum bi-mâ enzele'llâhu fe-ulâ'ike hum' (5:44, 5:45, 5:47) — sayım 'say 5:45 24-30' / 'say 5:47 9-15' (sûre içi 5:44, 5:45, 5:47); bölüm içi tekrar, ardışık bağ yerine sayımla kayıt; "
 "ayetler arası kalıp 'hudan ve nûr' (5:44, 5:46) — sayım 'say 5:46 16-17' (sûre içi 5:44, 5:46); D3 dışı bırakılan basılmış sayım eşleri: 5:46 'bni meryem' 5:17 ve başkaları; 'mev'izatan li'l-muttaqîn' 2:66 — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:45 edim geçişi emir, yasak, şart → şart; şahıs geçişi yok; şart → cevap (ayet içi; COND 'men' 17. kelime: 'fe-men tesaddeqa bih' / 'fe-huve keffâratun leh' (20. kelime)); şart → cevap (ayet içi; COND 'men' 23. kelime: 've men lem yahkum bi-mâ enzele'llâh' / 'fe-ulâ'ike humu'z-zâlimûn' (29. kelime)); "
 "5:46 edim geçişi şart → haber; şahıs geçişi 3 → 1; 5:47 edim geçişi haber → emir, şart; şahıs geçişi 1 → 3; şart → cevap (ayet içi; COND 'men' 8. kelime: 've men lem yahkum bi-mâ enzele'llâh' / 'fe-ulâ'ike humu'l-fâsiqûn' (14. kelime))",
 "sözdizimi (okuma; morph etiketiyle): 5:45 'enne'n-nefse bi'n-nefs' — 'enne' cümlesi (morph ACC), 'ketebnâ' fiilinin mef'ûlü; 've'l-curûha qısâs' — isim cümlesi (morph etiketi yok, okuma); 'fe-men tesaddeqa' — istînâf (morph REM) + şart (COND); 'fe-huve keffâratun' — cevap (RSLT); 5:46 'musaddiqan' (7. ve 18. kelime) — nekre ACC (morph etiketi yalnız ACC; işlev okuması tam okuma sonu); "
 "'fîhi hudan ve nûrun' — 'l-incîle'nin sıfatı (morph etiketi yok, okuma); 5:47 've'l-yahkum' — gaib emri (morph 'li' IMPV öneki); 've men lem yahkum … fe-ulâ'ike' — şart / cevap (COND / RSLT)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:45 beş organ çifti 'bi' ile (نفس, عين, أنف, أذن, سنن — her organ iki geçiş); ayetler arası kalıp 'lem yahkum bi-mâ enzele'llâhu fe-ulâ'ike hum' (5:44, 5:45, 5:47) — kapanış sıfatları kâfirûn / zâlimûn / fâsiqûn; "
 "ayetler arası kalıp 'hudan ve nûr' (5:44, 5:46) — Tevrat ve İncil için; 5:46 'musaddiqan li-mâ beyne yedeyhi mine't-tevrâh' ayet içinde İsa ve İncil için tekrar (kök صدق, بين, يدي ikilemeleri); bölümün 'İncil ile hüküm' kısmı 5:46-47'de ('l-incîle', 'ehlu'l-incîl')",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 16'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + "'; çıktı aynen): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle): 'qısâs' 5:45 'kısas' / 2:178 (emsal metninde) — tam okuma sonu; 've âteynâhu'l-incîl' 5:46 'İncil'i verdik' / 57:27 — tam okuma sonu; 'hudan ve mev'izatan li'l-muttaqîn' 5:46 'sakınanlar için hidayet ve öğüt' / 3:138 — tam okuma sonu; 'fe-ulâ'ike humu'l-fâsiqûn' 5:47 / 3:82 — tam okuma sonu",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 45 47 16'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:45 tarayıcı adayı (kök عين; A_şart) — çıpa değil: kısas hükmü, doğa iddiası yok (olgu=False); 5:46 ve 5:47 tarayıcı adayı yok; L3 / L4 adayı yok",
 "aday 1039: blokta ayet içi ve ayetler arası karşıt çift kaydı yok; eşleme betikle: ADAY_P",
 "aday 1041: kök حكم 5:47 'l-yahkum' (İncil ehli) / 'lem yahkum' — hükmün kaynağı lafız ('enzele'llâh'), hükmedenler insan; kök صدق 5:45 'tesaddeqa' (insan) / 5:46 'musaddiqan' (İsa ve İncil) — okuma",
 "bölüm: " + BOL + " bölümü, bölüm 7-3 — bölüm dört blok (14, 15, 16, 17); başlıktaki 'İncil ile hüküm' 5:46-47 ('l-incîle', 'ehlu'l-incîl'); 'Kitap ile hüküm' blok 17'de; "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b16/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3 — betikle: komut 'python3 sunum/bolum5_kurallar.py 45 47 16'; lem_bozuk.py 16 çıktısı): 5:46:1 'qaffey' — lem_bozuk bayrağı; meal maddesinde '(morph LEM ham biçim)' notlu; lemma adı listesinde notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 45 47 → AYN_SONUC; sunum/bolum4_kurallar.py 45 47 16 → KHATA_HEPSI; sunum/bolum5_kurallar.py 45 47 16 → B5_HEPSI; sunum/bolum6_kurallar.py 45 47 16 → B6_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (sunum/sonradan.py --plan 16): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('ketebe', 'nefs', ''ayn', 'enf', 'uzun', 'sinn', 'curûh', 'qısâs', 'tesaddeqa', 'keffâra', 'hakeme', 'enzele', 'zâlim', 'qaffey' (morph LEM ham biçim), 'eser', ''îsâ', 'ibn', 'meryem', 'musaddiq', 'beyn', 'yed', 'tevrâ', 'âtâ', 'incîl', 'hudâ', 'nûr', 'mev'iza', 'muttaqî', 'ehl', 'fâsiq'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]


def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (45, 47): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_45_47.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_5_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('06', '10', '11', '12', '13', '14', '15', '16'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()
GERI = open('/home/claude/yamalar/geriye_donuk_5_b13.txt', encoding='utf-8').read().splitlines()[:2]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    AYN = (run('/home/claude/sunum/ayn_kontrol.py', '45', '47').splitlines() or ['?'])[-1]
    KUR = run('/home/claude/sunum/bolum4_kurallar.py', '45', '47', '16').splitlines()
    KH = [l for l in KUR if l.startswith('HATA')]
    B5 = run('/home/claude/sunum/bolum5_kurallar.py', '45', '47', '16').splitlines()
    B5H = [l for l in B5 if l.startswith('HATA')]
    B6 = run('/home/claude/sunum/bolum6_kurallar.py', '45', '47', '16', '--tazelik-yok').splitlines()
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'),
           'MUT_SONUC': (MUT[-1] if MUT else '?'), 'GERI_P': ' / '.join(x.lstrip('# ') for x in GERI), 'B6_ESMA': ('; '.join(l[5:] for l in B6 if 'esmâ kural' in l and l.startswith('HATA')) or 'sapma 0')}
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

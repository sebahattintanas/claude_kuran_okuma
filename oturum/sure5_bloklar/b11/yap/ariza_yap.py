# blok 11 (5:31-32) ARIZA oluşturucu — bölüm 5-2 (bölüm kapanışı)
import sys, os, ast, subprocess, re
os.environ['OLC'] = '/home/claude/b11/olcum.txt'
os.environ['SAY2'] = '/home/claude/b11/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

VF_YAZI = {31: {1: "'fe-be'asa'", 20: "'fe-uvâriye'", 23: "'fe-asbaha'"}, 32: {18: "'fe-ke'ennemâ qatele'", 22: "'ve men ahyâhâ'", 24: "'fe-ke'ennemâ ahye'", 28: "'ve leqad'"}}
BOL = "'Âdem'in iki oğlu; bir canı öldürmek'"


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



R5 = []
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
                  + ('; tutmuyor — lemma dizisindeki fazla sûre içi eş okunmamış (fark test edilmedi)' if (sd(key)['henuz_si'] or sd(dk)['henuz_si']) else ''))
    r5.append(h)

K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k}

M31 = ("5:31 'Derken Allah … bir karga gönderdi' ('fe-be'asa'llâhu ğurâben', 'fe' 1. kelimede 'derken' ile (morph CONJ), 'gönder-' 'be'asa' karşılığı (1. kelime), lafız 2. kelimede 'Allah' ile, 'karga' 'ğurâb' karşılığı (3. kelime; nekre — 'bir' takdiri), sıralama: fail öne, fiil sona alındı); "
 "'yeri eşeleyen' ('yebhasu fi'l-ard', 'eşele-' 'yebhasu' karşılığı (4. kelime; '-en' sıfat-fiil açılımı; LEM 'yebhasu' (morph LEM ham biçim)), 'fî' 5. kelimede belirtme eki ile ('yeri' içinde; fiil yönetimi takdiri), 'yer' 'ard' karşılığı (6. kelime), sıralama: sıfat cümlesi öne); "
 "'kardeşinin cesedini nasıl örteceğini ona göstermek için' ('li-yuriyehû keyfe yuvârî sev'ete exîh', 'li' 7. kelimede 'için' ile (morph PRP; amaç), 'göster-' 'yuriye' karşılığı (7. kelime; IV. bab; masdar '-mek' açılımı; LEM 'erey' (morph LEM ham biçim — PASS etiketli)), 'hû' 7. kelimede 'ona' ile ('-a' fiil yönetimi takdiri), "
 "'keyfe' 8. kelimede 'nasıl' ile, 'ört-' 'yuvârî' karşılığı (9. kelime; III. bab; '-eceğini' açılımı; LEM 'vuriye' (morph LEM ham biçim)), 'ceset' 'sev'e' açılımı (10. kelime; 'ayıp yer' — ceset açılımı; iyelik ve belirtme), 'kardeş' 'ex' karşılığı (11. kelime), 'hî' 11. kelimede iyelik ile ('kardeşinin' içinde), sıralama: amaç öne, fiil sona alındı); "
 "'Vay bana' ('yâ veyletâ', 'yâ' 13. kelimede karşılıksız (morph VOC; 'vay' içinde), 'vay' 'veyl' karşılığı (13. kelime; nidâ), 'î' 13. kelimede 'bana' ile ('-a' fiil yönetimi takdiri; 'ten' elifiyle)); "
 "'Şu karga gibi olup kardeşimin cesedini örtmekten âciz mi kaldım' ('e-'aceztu en ekûne misle hâze'l-ğurâbi fe-uvâriye sev'ete exî', 'e' 14. kelimede 'mi' ile (soru; morph INTG), 'âciz kal-' ''aceztu' açılımı (14. kelime; LEM ''acez' (morph LEM ham biçim)), 'tu' 14. kelimede 1S ile ('kaldım' içinde), "
 "'en' 15. kelimede '-mek' ile (masdar; morph SUB; '-ten' fiil yönetimi takdiri), 'ol-' 'ekûne' karşılığı (16. kelime; '-up' bağ), 'gibi' 'misl' karşılığı (17. kelime), 'hâ' 18. kelimede karşılıksız (morph ATT; 'şu' içinde), 'şu' 'zâ' karşılığı (18. kelime), 'karga' 'ğurâb' karşılığı (19. kelime), "
 "'fe' 20. kelimede karşılıksız (morph CAUS; 've' — '-ip' bağıyla), 'ört-' 'uvâriye' karşılığı (20. kelime; III. bab; masdar açılımı), 'ceset' 'sev'e' açılımı (21. kelime), 'kardeş' 'ex' karşılığı (22. kelime), 'î' 22. kelimede iyelik ile ('kardeşimin' içinde), sıralama: fiil sona alındı); "
 "'dedi' ('qâle', 'de-' 'qâle' karşılığı (12. kelime), sıralama: söz öne alındı); "
 "'ve pişmanlık duyanlardan oldu' ('fe-asbaha mine'n-nâdimîn', 'fe' 23. kelimede 've' ile (morph CAUS), 'ol-' 'asbaha' karşılığı (23. kelime; IV. bab; 'kâne' ailesi), 'min' 24. kelimede '-dan' ile, 'pişmanlık duyan' 'nâdim' açılımı (25. kelime; etken ortaç; çoğul '-lar'), sıralama: fiil sona alındı)")
M32 = ("5:32 'Bu yüzden' ('min ecli zâlik', 'min' 1. kelimede karşılıksız ('yüzünden' içinde), 'yüzünden' 'ecl' açılımı (2. kelime; 'sebep'), 'zâlike' 3. kelimede 'bu' ile); "
 "'İsrâiloğullarına şunu yazdık' ('ketebnâ 'alâ benî isrâ'îl', 'yaz-' 'ketebnâ' karşılığı (4. kelime), 'nâ' 4. kelimede '-dık' ile, ''alâ' 5. kelimede yönelme eki ile ('İsrâiloğullarına' içinde), 'oğul' 'buneyy' karşılığı (6. kelime; çoğul; LEM 'buneyy' (morph LEM ham biçim)), 'İsrâil' 'isrâ'îl' karşılığı (7. kelime; özel ad), 'şu' takdir (4. kelime; mef'ûl açılımı — 'ennehû' cümlesi), sıralama: fiil sona alındı); "
 "'Kim, bir cana karşılık ya da yeryüzünde bir bozgunculuk olmaksızın bir canı öldürürse' ('ennehû men qatele nefsen bi-ğayri nefsin ev fesâdin fi'l-ard', 'enne' 8. kelimede karşılıksız (iki nokta ile açıklama), 'hû' 8. kelimede karşılıksız (şân zamiri), 'men' 9. kelimede 'kim' ile (şart; morph COND), 'öldür-' 'qatele' karşılığı (10. kelime; şart eki), "
 "'can' 'nefs' karşılığı (11. kelime; nekre — 'bir' takdiri; belirtme), 'bi' 12. kelimede karşılıksız ('olmaksızın' içinde), 'olmaksızın' 'ğayr' açılımı (12. kelime), 'can' 'nefs' karşılığı (13. kelime; yönelme eki ile 'cana'), 'karşılık' takdir (13. kelime), 'ev' 14. kelimede 'ya da' ile (morph CONJ), "
 "'bozgunculuk' 'fesâd' karşılığı (15. kelime; nekre — 'bir' takdiri), 'fî' 16. kelimede '-de' ile, 'yeryüzü' 'ard' karşılığı (17. kelime), sıralama: şart öne, fiil sona alındı); "
 "'sanki bütün insanları öldürmüş gibidir' ('fe-ke'ennemâ qatele'n-nâse cemî'an', 'fe' 18. kelimede karşılıksız (morph RSLT; şart cevabı), 'ke'enne' 18. kelimede 'sanki' ile, 'mâ' 18. kelimede karşılıksız (morph PREV), 'öldür-' 'qatele' karşılığı (19. kelime; '-müş gibi' açılımı), 'insan' 'nâs' karşılığı (20. kelime; çoğul '-lar'; belirtme), 'bütün' 'cemî'' karşılığı (21. kelime), sıralama: fiil sona alındı); "
 "'kim de onu yaşatırsa' ('ve men ahyâhâ', 've' 22. kelimede 'de' ile (morph CONJ), 'men' 22. kelimede 'kim' ile (şart; morph COND), 'yaşat-' 'ahyâ' karşılığı (23. kelime; IV. bab; şart eki), 'hâ' 23. kelimede 'onu' ile (gönderge can), sıralama: fiil sona alındı); "
 "'sanki bütün insanları yaşatmış gibidir' ('fe-ke'ennemâ ahye'n-nâse cemî'an', 'fe' 24. kelimede karşılıksız (morph RSLT), 'ke'enne' 24. kelimede 'sanki' ile, 'mâ' 24. kelimede karşılıksız (morph PREV), 'yaşat-' 'ahyâ' karşılığı (25. kelime; '-mış gibi' açılımı), 'insan' 'nâs' karşılığı (26. kelime; çoğul '-lar'), 'bütün' 'cemî'' karşılığı (27. kelime), sıralama: fiil sona alındı); "
 "'Andolsun, elçilerimiz onlara apaçık delillerle geldi' ('ve leqad câ'ethum rusulunâ bi'l-beyyinât', 've' 28. kelimede karşılıksız (nokta; morph REM), 'le' 28. kelimede 'andolsun' ile (morph EMPH), 'qad' 28. kelimede karşılıksız (morph CERT), 'gel-' 'câ'et' karşılığı (29. kelime), 'hum' 29. kelimede 'onlara' ile ('-a' fiil yönetimi takdiri), "
 "'elçi' 'rasûl' karşılığı (30. kelime; çoğul '-ler'), 'nâ' 30. kelimede '-imiz' iyelik ile, 'bi' 31. kelimede '-le' ile, 'apaçık delil' 'beyyine' açılımı (31. kelime; çoğul '-ler'), sıralama: fail öne, fiil sona alındı); "
 "'sonra onlardan çoğu bunun ardından yeryüzünde mutlaka aşırı gidenlerdir' ('summe inne kesîran minhum ba'de zâlike fi'l-ardi le-musrifûn', 'summe' 32. kelimede 'sonra' ile (morph CONJ), 'inne' 33. kelimede karşılıksız (pekiştirme; 'mutlaka' ile ortak), 'çok' 'kesîr' karşılığı (34. kelime; iyelik ile 'çoğu'), 'min' 35. kelimede '-dan' ile, 'hum' 35. kelimede 'onlar' ile, "
 "'ba'd' 36. kelimede 'ardından' ile, 'zâlike' 37. kelimede 'bunun' ile, 'fî' 38. kelimede '-de' ile, 'yeryüzü' 'ard' karşılığı (39. kelime), 'le' 40. kelimede 'mutlaka' ile (morph EMPH), 'aşırı giden' 'musrif' açılımı (40. kelime; etken ortaç; çoğul '-ler'; '-dir' haber eki), sıralama: haber sona alındı)")
MEALS = (M31, M32)


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
open('/home/claude/b11/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '11')
ESL = run('/home/claude/sunum/es_lemma.py', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '11').replace('\n', '; ')
EMS = open('/home/claude/b11/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '31', '32', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b11/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
MFARK = [(k, n, sayim.S2[k.replace(' --medde', '')][0]) for k, (n, d) in sayim.S2.items() if '--medde' in k]
MEDF = '; '.join("%s meddeli %d / meddesiz %d" % (k.replace(' --medde', ''), m, n) for k, n, m in MFARK)
MEDF += ' — fark yok, yeni eş yok' if all(n == m for k, n, m in MFARK) else ' — FARK VAR'


M = {}; exec(open('/home/claude/yamalar/metin_5_31_32.txt', encoding='utf-8').read(), {'MEAL': {}, 'M': M})
M_A1 = ' '.join(M[a][M[a].index('◈A'):M[a].index(' A2 ')] for a in range(31, 33))
GLS = run('/home/claude/sunum/gloss_tara.py', '31', '32', '11').splitlines()
GKAP = GLS[0] if GLS else 'KAPSAMAYAN ?'

AYN = 'AYN_SONUC'
I = [
 "kök tablosu: ölçümde '???' 5:31 için 1 (kök بحث — 4. kelime 'yebhasu') — kök tabloya eklendi (yamalar/yama_kok_5_31.py → kok_ekle_5.py; anlam 'eşeleme, kazıp arama'; 1 ayet; docstring dosya adı ve bölümle — bölüm 4 kuralı 16; yama_kok_5_24.py docstring'i de düzeltildi), ölçüm yeniden alındı, '???' 0; 5:32 '???' 0; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 31 32 11'): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:31-32 esmâ yok (ölçüm); lafız 5:31 bir geçiş ('be'asa'llâhu'); 5:32 lafız yok (konuşan 1P 'ketebnâ'); Rab yok",
 "esma_kayit: 5:31 'mühür hayır' (sınıf A/A), 5:32 'mühür hayır' (sınıf 0/0) — ölçüm esmâ yok (uyuşuyor)",
 "ölçüm: 5:31 '{{1|biçim DIKKAT}}', '{{1|EDİLGEN 1/9 fiil, pas z=0,30}}', '{{1|HAPAKS: بحث}}', '{{1|hapaks z=3,28}}', '{{1|fâsıla ٱلندمين → ن, N sınıfı}}', '{{1|simetri \\[6, 9, 20, 2\\]}}', '{{1|harf 106 → harf3 102, isaret 4}}' ve '{{1|dış düğüm 0}}'; "
 "5:32 '{{2|lafız YOK · Rab YOK}}', '{{2|sayı işareti كَثِير}}', '{{2|fâsıla لمسرفون → ن, N sınıfı}}', '{{2|simetri \\[6, 3, 33, 2\\]}}', '{{2|harf 167 → harf3 160, isaret 7}}' ve '{{2|dış düğüm 0}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 31 32 11'): KALAN_P",
 "ölçüm aktör: 5:32 '{{2|aktör: adlı إِسْرائِيل 7\\. sırada \\(kavim, rol mecrur\\)}}' — 'benî'nin muzâfun ileyhi (blok 5'teki 5:12 kaydıyla eş); 5:31 aktör yok (karga 'ğurâben' nekre, kardeşler adsız)",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle): 5:31 soru, nida — INTG 1 'e' (14.), VOC 1 'yâ' (13.); biçim DIKKAT D2'de yazılmadı; ölçüm EDİLGEN 1 — 'li-yuriyehû' (7.) morph PASS etiketli, anlam etken IV. bab 'göstermek' (morph etiket kuşkulu; LEM 'erey' ham; araç tanımı farkı, §8); "
 "5:32 şart — CERT 1 'qad' (28.), COND 2 'men' (9., 22.), EMPH 2 'le' (28., 40.)",
 "yıldız: 5:31 ★★★ (kaynak hapaks), 5:32 ★★ — satır yıldız kaynağını adlandırmıyor; kaynak kapanış notunda bilançodan",
 "fâsıla: 5:30 ن (ٱلخسرين) → 5:31 ن (ٱلندمين) → 5:32 ن (لمسرفون); bölüm boyunca N sınıfı; 5:30 ve 5:31 'fe-asbaha mine'l-…' kalıbıyla bitiyor ('xâsirîn' / 'nâdimîn'); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref: 5:31 ve 5:32 xref yok",
 "araç tanımı farkları (R5): blokta nakarat3 kalıbı yok — karşılaştırılacak madde yok (şablon: nakarat3 'tür' alanı 'tam' / 'ic' — sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; eşi okunmamış hükümde '(eş okunmamış, fark test edilmedi)')",
 "nakarat3 (R3: sayıyla özetlendi): 5:31 ve 5:32 'bağ: YOK' — kalıp yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9): 5:31 Allah (lafız), 'ğurâben', 3MS (adsız — karga, lafız, katil kardeş), 'exîh', söz içi 1S (adsız), 'l-ğurâbi', 'n-nâdimîn'; 5:32 konuşan 1P (adsız), 'benî isrâ'île' (adlı), 'ennehû' (şân zamiri), 'men' (şart ismi; failleri 3MS adsız), 'nefsen', 'n-nâse', 3FS, 'rusulunâ', 3MP (adsız), 'kesîran minhum', 'le-musrifûn' — "
 "betik denetimi: KHATA_ADSIZ; blokta 'li-X' söz muhatabı yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): 5:31 'qâle' (12. kelime) — söz 13-22. kelime ('yâ veyletâ … sev'ete exî'; 23. kelime 'fe-asbaha' morph CAUS — anlatı); 5:32 'ketebnâ' (4. kelime) — yazılan hüküm 8-27. kelime (söz biçimli içerik; 'qâle'siz, tırnak yok); 28. kelime 've leqad' morph REM — anlatıya dönüş; "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 31 32 11' — A3 aralığında morph REM): KREM_P; morph 've' / 'fe' konumlarıyla kontrol edildi: 5:31 'fe-be'asa' (1.) CONJ, 'fe-uvâriye' (20.) CAUS, 'fe-asbaha' (23.) CAUS; 5:32 'ev' (14.) CONJ, 'fe-ke'ennemâ' (18., 24.) RSLT, 've men' (22.) CONJ, 've leqad' (28.) REM, 'summe' (32.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 5:31 ◈K أرض ('l-ardi' 6. kelime — K1; anlam notu: karganın eşelediği yer); 5:32 ◈K أرض ('l-ardi' 17. ve 39. kelime — K1; anlam notu: bozgunculuk ve aşırılık yeri), أجل ('ecli' 2. kelime — K2; anlam notu: 'min ecli' — 'bu yüzden', süre / ecel anlamında değil — tetik aracı kökü mekanik okur); "
 "5:32 ◈B أنس ('n-nâse' 20. ve 26. kelime — B1), حيي ('ahyâhâ' 23. kelime, 'ahye' 25. kelime — B4; anlam notu: can yaşatma); tetik listesinde olmayan adlar (elle): 5:31 'ğurâben' (karga — hayvan adı, kök غرب tetik dışı; B1 alanı yalnız طير / دبب kökleriyle), 'sev'ete' (ceset — beden; kök سوأ tetik dışı); 5:32 'nefsen' / 'nefsin' (can — kök نفس tetik dışı); oturum_tetik kuru koşu 2 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:31 eş yok, 5:32 (13:31, 18:74, 27:76, 57:25) (kontrol.py ile); blok geçişi 5:30 → 5:31 bölüm içi — sayımlı eş yok, bağ kurulmadı; D3 dışı bırakılan basılmış sayım eşi yok",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:31 edim geçişi haber → soru, nida (ayetler arası); şahıs geçişi yok; söz açılır (13. kelime); söz kapanır (22. kelime); 5:32 edim geçişi soru, nida → şart (ayetler arası); şahıs geçişi yok; şart → cevap (ayet içi; COND 'men' 9. kelime); şart → cevap (ayet içi; COND 'men' 22. kelime); bölüm kapanışı",
 "sözdizimi (okuma; morph etiketiyle): 5:31 'fe-be'asa'llâhu' — 5:30'a atıf (morph CONJ); 'yebhasu fi'l-ardi' — 'ğurâben'in sıfatı (morph etiketi yok); 'li-yuriyehû' — amaç (morph PRP); 'keyfe yuvârî' — 'yuriye'nin öbür tümleci (soru ismi); 'yâ veyletâ' — nidâ; 'e-'aceztu' — soru (morph INTG); 'en ekûne' — masdar (morph SUB); 'fe-uvâriye' — sonuç (morph CAUS, mansub); "
 "'fe-asbaha' — sonuç (morph CAUS); 5:32 'min ecli zâlike' — sebep; 'ennehû' — 'ketebnâ'nın mef'ûlü, şân zamiri; 'men qatele … fe-ke'ennemâ' — şart / cevap (morph COND / RSLT); 've men ahyâhâ' — şart cümlesine atıf (morph CONJ); 've leqad' — istînâf (morph REM), yemin; 'summe inne' — atıf (morph CONJ)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:31 'fe-be'asa'llâhu ğurâben' ile açılıyor (1-3. kelime); kök غرب (karga) iki geçiş (3. ve 19. kelime), وري (örtme) iki geçiş (9. ve 20. kelime), سوأ (ceset) iki geçiş (10. ve 21. kelime) — karganın gösterdiği / kardeşin yapamadığı; "
 "5:32 'qatele … n-nâse cemî'an' / 'ahyâ … n-nâse cemî'an' — ölçüm kök ikilemesi قتل, حيي, أنس, جمع; 5:32 'bi-ğayri nefsin' kalıbının basılmış eşi 18:74 (sayımın basılmış kümesinden); 5:31 ve 5:30 'fe-asbaha mine'l-' ile bitiyor (5:30 7-9. kelime, 5:31 23-25. kelime)",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 11'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py 1 2 3 4 5 6 7 8 9 10 11'; çıktı aynen): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle): 'benî isrâ'îl' 5:32 'İsrâiloğulları' / 27:76 (eş); 'bi-ğayri nefs' 5:32 'bir cana karşılık … olmaksızın' / 18:74 'Bir cana karşılık olmaksızın' (eş); 'n-nâse cemî'an' 5:32 'bütün insanlar' / 13:31 'bütün insanlar' (eş); 'rusulunâ bi'l-beyyinât' 5:32 'elçilerimiz … apaçık delillerle' / 57:25 'elçilerimizi apaçık delillerle' (eş) — tam okuma sonu",
 "KARSILIK_CAKISMA",
 "çıpa: 5:31 tarayıcı adayı (kök أرض; B_ta'lîl) — çıpa değil: karganın yeri eşelemesi anlatı içinde, doğa iddiası yok (olgu=False); 5:32 tarayıcı adayı (kök أرض, حيي; A_şart) — çıpa değil: şartlı hüküm, can yaşatma ahlaki hüküm (olgu=False); L3 / L4 adayı yok",
 "aday 1039: ayet içi 5:31 ('yuvârî sev'ete exîh' / 'e-'aceztu'), 5:32 ('men qatele nefsen' / 've men ahyâhâ'; 'qatele'n-nâse cemî'an' / 'ahye'n-nâse cemî'an') — okuma; ayetler arası 5:30 / 5:32 (5:30 6. kelimedeki öldürme / 'men qatele nefsen'; bloklar arası)",
 "aday 1041: kök حيي 5:32 'ahyâhâ' / 'ahye' — insanın can yaşatması (diriltme anlamı lafızda başka ayetlerde; burada mecaz: öldürmeden alıkoyma) — okuma; kök بعث 5:31 'be'asa'llâhu' — lafzın karga göndermesi (5:12 'be'asnâ' — temsilci gönderme ile kök eşi)",
 "bölüm: " + BOL + " bölümü, bölüm 5-2 — bölüm kapanışı 5:32; bölüm iki blok (blok planından: 10 ve 11); başlıktaki 'bir canı öldürmek' 5:30 ('fe-qatelehû') ve 5:32 ('men qatele nefsen'); mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; "
 "bölüm sonu bağımsız denetimi bu bloktan sonra (bulgular yamalar/bekleyen_ariza_5_b11.txt); medde taraması (sunum/medde.py b11/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (elle; lem_bozuk.py 11 çıktısı ve aracın bayraklamadığı biçimler): 5:31:4 'yebhasu', 5:31:7 'erey' (PASS etiketli), 5:31:14 ''acez' — lem_bozuk bayrağı; 5:31:9 'vuriye' (edilgen görünümlü LEM), 5:32:6 'buneyy' — aracın bayraklamadığı; meal maddelerinde '(morph LEM ham biçim)' notlu; başka maddede bu adlar geçmiyor",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 31 32 → AYN_SONUC; sunum/bolum4_kurallar.py 31 32 11 → KHATA_HEPSI",
 "sonradan basılan (sunum/sonradan.py --plan 11): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('ğurâb', 'ard', 'sev'e', 'ex', 'veyl', 'misl', 'nâdim', 'ecl', 'buneyy', 'isrâ'îl', 'nefs', 'ğayr', 'fesâd', 'nâs', 'cemî'', 'rasûl', 'beyyine', 'kesîr', 'musrif'); transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]
def yaz():
    items = [kes(x) for x in I]
    s = '\n (31, 32): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_31_32.txt', 'w', encoding='utf-8').write(s)


idx = I.index('KARSILIK_CAKISMA')
I[idx] = 'karşılık çakışması (geçici)'
yaz()
AYN = (run('/home/claude/sunum/ayn_kontrol.py', '31', '32').splitlines() or ['?'])[-1]
I = [x.replace('AYN_SONUC', AYN) for x in I]
KUR = run('/home/claude/sunum/bolum4_kurallar.py', '31', '32', '11').splitlines()
KH = [l for l in KUR if l.startswith('HATA')]
REP = {'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
       'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h) or 'adsız / söz muhatabı hatası 0'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
       'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?')}
for k, v in REP.items(): I = [x.replace(k, v) for x in I]
import glob
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_5_*.txt'), key=lambda p: int(p.split('_')[-2]))
CAK = run('/home/claude/sunum/cakisma.py', *DOS)
KYENI = set(re.findall(r"'([^']+)' '(?:[^']|'(?=[a-zâîû]))+' (?:karşılığı|açılımı)", ' '.join(MEALS)))
CAK_L = [l for l in CAK.splitlines() if l.startswith('KÖK') or l.split(' ←')[0] in KYENI]
KARAR = {}
exec(open('/home/claude/b06/yap/karar.py', encoding='utf-8').read()); exec(open('/home/claude/b10/yap/karar.py', encoding='utf-8').read())
if os.path.exists('/home/claude/b11/yap/karar.py'): exec(open('/home/claude/b11/yap/karar.py', encoding='utf-8').read())
I[idx] = ("karşılık çakışması (bölüm 4 kuralı 4 — komut 'python3 sunum/cakisma.py' + sûre 5'in okunmuş bütün ARIZA dosyaları; Türkçe fiil kökü eşlemesi betikle, son dosyaya dokunan gruplar; kararlar morph LEM eşitliğine göre): "
          + ('; '.join(KARAR.get(l.split(' ←')[0].strip() if not l.startswith('KÖK') else 'KÖK ' + l.split()[1], l + ' — karar yok') for l in CAK_L) if CAK_L else 'bu bloğa dokunan çakışma yok'))
yaz()
print('yazıldı', len(I))
print('\n'.join(CAK_L))
print(GLS); print(KUR)

# blok 8 (5:20-23) ARIZA oluşturucu — bölüm 4-1 (bölüm açılışı)
import sys, os, ast, subprocess, re
os.environ['OLC'] = '/home/claude/b08/olcum.txt'
os.environ['SAY2'] = '/home/claude/b08/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

VF_YAZI = {20: {1: "'ve iz'", 14: "'ve ce'alekum'", 16: "'ve âtâkum'"}, 21: {9: "'ve lâ'", 13: "'fe-tenqalibû'"},
           22: {7: "'ve innâ'", 13: "'fe-in yaxrucû'", 16: "'fe-innâ'"}, 23: {12: "'fe-izâ'", 14: "'fe-innekum'", 16: "'ve 'ale'llâhi'", 18: "'fe-tevekkelû'"}}
BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b07.txt', encoding='utf-8').read() + ']')
BOL = "'Mûsâ ve kavmi: kutsal topraklar; kırk yıl'"


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



TT = "(eş okunmamış, fark test edilmedi)"
R5 = [
 ("5:20", "'zekera ni'me allâh 'alâ iz'", 2, 'say 5:20 6-10', "harekesiz 'zkurû ni'meta'llâhi 'aleykum iz' (6-10. kelime)", ('dizi 5 20 6 10', "zekera ni'me allâh 'alâ iz", '6-10', "biçim farkı — 'ni'me' yazımı ة / ت (5:11 okundu)")),
 ("5:20", "'zekera ni'me allâh 'alâ'", 3, 'say 5:20 6-9', "harekesiz 'zkurû ni'meta'llâhi 'aleykum' (6-9. kelime)", ('dizi 5 20 6 9', "zekera ni'me allâh 'alâ", '6-9', "biçim farkı — 'ni'me' yazımı ة / ت ve 've' öneki (5:7, 5:11 okundu)")),
 ("5:20", "'ehad min 'âlem'", 2, 'say 5:20 20-22', "harekesiz 'ehaden mine'l-'âlemîn' (20-22. kelime)", None),
 ("5:22", "'inne len dexale'", 2, 'say 5:22 7-9', "harekesiz 've innâ len nedxulehâ' (7-9. kelime)", ('dizi 5 22 7 9', "inne len dexale", '7-9', TT)),
 ("5:23", "'en kâne mu'min'", 3, 'say 5:23 19-21', "harekesiz 'in kuntum mu'minîn' (19-21. kelime)", None),
 ("5:23", "'ve 'alâ allâh tevekkel' (LEM 'tevekkel' morph LEM ham biçim)", 2, 'say 5:23 16-18', "harekesiz 've 'ale'llâhi fe-tevekkelû' (16-18. kelime)", ('dizi 5 23 16 18', "'alâ allâh tevekkel", '16-18', "önek farkı — 'fe' (5:23) / 'fe' + 'li' (5:11 okundu)")),
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
                  + ('; tutmuyor — lemma dizisindeki fazla sûre içi eş okunmamış (fark test edilmedi)' if (sd(key)['henuz_si'] or sd(dk)['henuz_si']) else ''))
    r5.append(h)

K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k}

M20 = ("5:20 'Hani Mûsâ kavmine demişti' ('ve iz qâle mûsâ li-qavmih', 've' 1. kelimede karşılıksız (morph REM; ayet başı), 'iz' 1. kelimede 'hani' ile (zaman; morph T), 'de-' 'qâle' karşılığı (2. kelime; geçmiş anlatı '-mişti'), 'Mûsâ' 'mûsâ' karşılığı (3. kelime; özel ad), "
 "'li' 4. kelimede '-e' ile, 'kavim' 'qavm' karşılığı (4. kelime), 'hî' 4. kelimede iyelik ile ('kavmine' içinde), sıralama: fiil sona alındı); "
 "'Ey kavmim' ('yâ qavmi', 'yâ' 5. kelimede 'ey' ile (morph VOC), 'kavim' 'qavm' karşılığı (5. kelime), 'î' 5. kelimede '-im' iyelik ile (söz içi 1S)); "
 "'Allah'ın üzerinizdeki nimetini anın' ('zkurû ni'meta'llâhi 'aleykum', 'an-' 'zkurû' karşılığı (6. kelime; emir), 'û' 6. kelimede '-ın' ile, 'nimet' 'ni'me' karşılığı (7. kelime; '-i' iyelik takdiri), lafız 8. kelimede 'Allah'ın' ile ('-ın' takdir), "
 "''alâ' 9. kelimede 'üzerinde' ile ('-ki' takdir), 'kum' 9. kelimede '-iniz' iyelik ile, sıralama: fiil sona alındı); "
 "'içinizden nebiler kıldı' ('iz ce'ale fîkum enbiyâ'', 'iz' 10. kelimede karşılıksız (zaman; morph T — iki nokta ile açıklama), 'kıl-' 'ce'ale' karşılığı (11. kelime), 'fî' 12. kelimede '-den' ile ('iç' açılımı), 'kum' 12. kelimede iyelik ile ('içinizden' içinde), "
 "'nebi' 'nebiyy' karşılığı (13. kelime; çoğul '-ler'), sıralama: fiil sona alındı); "
 "'sizi hükümdarlar kıldı' ('ve ce'alekum mulûken', 've' 14. kelimede karşılıksız (virgül; morph CONJ), 'kıl-' 'ce'ale' karşılığı (14. kelime), 'kum' 14. kelimede 'sizi' ile, 'hükümdar' 'melik' karşılığı (15. kelime; çoğul '-lar'; nekre), sıralama: fiil sona alındı); "
 "'ve âlemlerden hiç kimseye vermediğini size verdi' ('ve âtâkum mâ lem yu'ti ehaden mine'l-'âlemîn', 've' 16. kelimede 've' ile (morph CONJ), 'ver-' 'âtâ' karşılığı (16. kelime; IV. bab), 'kum' 16. kelimede 'size' ile ('-e' fiil yönetimi takdiri), 'mâ' 17. kelimede '-diğini' ile (ilgi), "
 "'lem' 18. kelimede '-me-' ile (olumsuz geçmiş; morph NEG), 'ver-' 'yu'ti' karşılığı (19. kelime; IV. bab), 'hiç kimse' 'ehad' karşılığı (20. kelime; nekre; yönelme — fiil yönetimi takdiri), 'min' 21. kelimede '-den' ile, 'âlem' ''âlem' karşılığı (22. kelime; çoğul '-ler'), sıralama: fiil sona alındı)")
M21 = ("5:21 'Ey kavmim' ('yâ qavmi', 'yâ' 1. kelimede 'ey' ile (morph VOC), 'kavim' 'qavm' karşılığı (1. kelime), 'î' 1. kelimede '-im' iyelik ile (söz içi 1S)); "
 "'Allah'ın size yazdığı kutsal toprağa girin' ('dxulu'l-arda'l-muqaddesete'lletî ketebe'llâhu lekum', 'gir-' 'dxulu' karşılığı (2. kelime; emir), 'û' 2. kelimede '-in' ile, 'toprak' 'ard' karşılığı (3. kelime; '-a' fiil yönetimi takdiri), 'kutsal' 'muqaddese' karşılığı (4. kelime; edilgen ortaç), "
 "'elletî' 5. kelimede '-dığı' ile, 'yaz-' 'ketebe' karşılığı (6. kelime), lafız 7. kelimede 'Allah'ın' ile (sıfat cümlesi faili; izafet takdiri), 'li' 8. kelimede '-e' ile, 'kum' 8. kelimede 'siz' ile, sıralama: sıfat cümlesi öne, fiil sona alındı); "
 "'arkanıza geri dönmeyin' ('ve lâ tertaddû 'alâ edbârikum', 've' 9. kelimede karşılıksız (noktalı virgül; morph REM), 'lâ' 9. kelimede '-me-' ile (yasak; morph PRO), 'geri dön-' 'tertaddû' açılımı (10. kelime; VIII. bab; 'geri' açılım takdiri), 'û' 10. kelimede '-yin' ile, "
 "''alâ' 11. kelimede yönelme eki ile ('arkanıza' içinde; fiil yönetimi takdiri), 'arka' 'dubur' karşılığı (12. kelime; çoğul — Türkçede tekil), 'kum' 12. kelimede '-nız' iyelik ile, sıralama: fiil sona alındı); "
 "'yoksa hüsrana uğramış olarak dönersiniz' ('fe-tenqalibû xâsirîn', 'fe' 13. kelimede 'yoksa' ile (morph CAUS), 'dön-' 'tenqalibû' karşılığı (13. kelime; VII. bab; geniş zaman), 'û' 13. kelimede 2MP ile ('dönersiniz' içinde), "
 "'hüsrana uğramış' 'xâsir' açılımı (14. kelime; etken ortaç; çoğul; 'olarak' hâl takdiri), sıralama: hâl öne, fiil sona alındı)")
M22 = ("5:22 'Dediler ki' ('qâlû', 'de-' 'qâlû' karşılığı (1. kelime), 'û' 1. kelimede '-ler' ile, 'ki' takdir (1. kelime; söz açılışı)); "
 "'Ey Mûsâ' ('yâ mûsâ', 'yâ' 2. kelimede 'ey' ile (morph VOC), 'Mûsâ' 'mûsâ' karşılığı (2. kelime; özel ad)); "
 "'Orada zorba bir kavim var' ('inne fîhâ qavmen cebbârîn', 'inne' 3. kelimede karşılıksız (pekiştirme), 'fî' 4. kelimede '-da' ile, 'hâ' 4. kelimede 'ora' ile ('orada' içinde; gönderge kutsal toprak), 'kavim' 'qavm' karşılığı (5. kelime; nekre — 'bir' takdiri), "
 "'zorba' 'cebbâr' karşılığı (6. kelime; sıfat; çoğul — Türkçede tekil), 'var' takdir (6. kelime; isim cümlesi), sıralama: sıfat öne); "
 "'onlar oradan çıkıncaya kadar biz oraya asla girmeyeceğiz' ('ve innâ len nedxulehâ hattâ yaxrucû minhâ', 've' 7. kelimede karşılıksız (noktalı virgül; morph CONJ), 'inne' 7. kelimede karşılıksız (pekiştirme), 'nâ' 7. kelimede 'biz' ile, 'len' 8. kelimede 'asla' ile (morph NEG; gelecek olumsuz), "
 "'gir-' 'nedxulu' karşılığı (9. kelime; gelecek '-me-yeceğiz' açılımı), 'hâ' 9. kelimede 'oraya' ile ('-ya' fiil yönetimi takdiri), 'hattâ' 10. kelimede '-ıncaya kadar' ile, 'çık-' 'yaxrucû' karşılığı (11. kelime), 'û' 11. kelimede 'onlar' ile, 'min' 12. kelimede '-dan' ile, "
 "'hâ' 12. kelimede 'ora' ile ('oradan' içinde), sıralama: zaman öne, fiil sona alındı); "
 "'Eğer oradan çıkarlarsa, biz de mutlaka gireriz' ('fe-in yaxrucû minhâ fe-innâ dâxilûn', 'fe' 13. kelimede karşılıksız (morph REM), 'in' 13. kelimede 'eğer' ile (şart; morph COND), 'çık-' 'yaxrucû' karşılığı (14. kelime; şart eki), 'û' 14. kelimede '-lar' ile, "
 "'min' 15. kelimede karşılıksız ('oradan' içinde), 'hâ' 15. kelimede 'ora' ile ('oradan' içinde), 'fe' 16. kelimede 'de' ile (morph RSLT; şart cevabı), 'inne' 16. kelimede 'mutlaka' ile, 'nâ' 16. kelimede 'biz' ile, 'giren' 'dâxil' karşılığı (17. kelime; etken ortaç; geniş zaman açılımı), sıralama: fiil sona alındı)")
M23 = ("5:23 'Korkanlardan, Allah'ın kendilerine nimet verdiği iki adam dedi ki' ('qâle raculâni mine'llezîne yaxâfûne en'ame'llâhu 'aleyhim', 'de-' 'qâle' karşılığı (1. kelime), 'adam' 'racul' karşılığı (2. kelime; ikil — 'iki' sayı açılımı), 'min' 3. kelimede '-dan' ile, "
 "'ellezîne' 4. kelimede '-anlar' ile ('korkanlardan' içinde), 'kork-' 'yaxâfûne' karşılığı (5. kelime), 'ûne' 5. kelimede karşılıksız ('-anlar' içinde), 'nimet ver-' 'en'ame' açılımı (6. kelime; IV. bab; '-diği' sıfat-fiil), lafız 7. kelimede 'Allah'ın' ile (sıfat cümlesi faili; izafet takdiri), "
 "''alâ' 8. kelimede karşılıksız ('kendilerine' içinde), 'humâ' 8. kelimede 'kendilerine' ile (ikil; '-e' fiil yönetimi takdiri), 'ki' takdir (1. kelime; söz açılışı), sıralama: fail ve sıfatları öne, fiil sona alındı); "
 "'Onların üzerine kapıdan girin' ('dxulû 'aleyhimu'l-bâb', 'gir-' 'dxulû' karşılığı (9. kelime; emir), 'û' 9. kelimede '-in' ile, ''alâ' 10. kelimede 'üzerine' ile, 'him' 10. kelimede 'onların' ile, 'kapı' 'bâb' karşılığı (11. kelime; '-dan' fiil yönetimi takdiri), sıralama: fiil sona alındı); "
 "'kapıdan girdiğinizde şüphesiz galip gelirsiniz' ('fe-izâ dexaltumûhu fe-innekum ğâlibûn', 'fe' 12. kelimede karşılıksız (noktalı virgül; morph REM), 'izâ' 12. kelimede '-diğinizde' ile (zaman; morph T), 'gir-' 'dexaltum' karşılığı (13. kelime), 'tum' 13. kelimede 2MP ile ('girdiğinizde' içinde), "
 "'hû' 13. kelimede 'kapıdan' ile (gönderge kapı; '-dan' fiil yönetimi takdiri), 'fe' 14. kelimede karşılıksız (morph RSLT; cevap), 'inne' 14. kelimede 'şüphesiz' ile, 'kum' 14. kelimede 2MP ile ('gelirsiniz' içinde), 'galip gelen' 'ğâlib' açılımı (15. kelime; etken ortaç; geniş zaman açılımı), sıralama: zaman öne); "
 "'İnanıyorsanız yalnız Allah'a dayanın' ('ve 'ale'llâhi fe-tevekkelû in kuntum mu'minîn', 've' 16. kelimede karşılıksız (nokta; morph REM), ''alâ' 16. kelimede '-a' ile, lafız 17. kelimede 'Allah'a' ile, 'yalnız' takdir (16-17. kelime; takdim ile hasr okuması), 'fe' 18. kelimede karşılıksız (morph SUP), "
 "'dayan-' 'tevekkelû' açılımı (18. kelime; V. bab; emir; LEM 'tevekkel' (morph LEM ham biçim)), 'û' 18. kelimede '-ın' ile, 'in' 19. kelimede şart eki ile ('inanıyorsanız' içinde; morph COND), 'ol-' 'kuntum' karşılığı (20. kelime; 'inanıyor' açılımı içinde), 'tum' 20. kelimede 2MP ile ('inanıyorsanız' içinde), "
 "'inanan' 'mu'min' karşılığı (21. kelime; etken ortaç; 'inan-' fiil açılımı), sıralama: şart öne, fiil sona alındı)")
MEALS = (M20, M21, M22, M23)


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
open('/home/claude/b08/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '8')
ESL = run('/home/claude/sunum/es_lemma.py', '8').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '8').replace('\n', '; ')
EMS = open('/home/claude/b08/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '20', '23', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b08/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
MFARK = [(k, n, sayim.S2[k.replace(' --medde', '')][0]) for k, (n, d) in sayim.S2.items() if '--medde' in k]
MEDF = '; '.join("%s meddeli %d / meddesiz %d" % (k.replace(' --medde', ''), m, n) for k, n, m in MFARK)
MEDF += ' — fark yok, yeni eş yok' if all(n == m for k, n, m in MFARK) else ' — FARK VAR'


M = {}; exec(open('/home/claude/yamalar/metin_5_20_23.txt', encoding='utf-8').read(), {'MEAL': {}, 'M': M})
M_A1 = ' '.join(M[a][M[a].index('◈A'):M[a].index(' A2 ')] for a in range(20, 24))
GLS = run('/home/claude/sunum/gloss_tara.py', '20', '23', '08').splitlines()
GKAP = GLS[0] if GLS else 'KAPSAMAYAN ?'

I = list(BEK) + [
 "kök tablosu: ölçümde '???' 5:20, 5:21, 5:22 ve 5:23 için ayrı sayıldı — 0; yeni kök yok (okunan ayetlerde tabloda olmayan kök 0); gloss kapsam taraması (bölüm 3 denetimi kuralı 8; sunum/gloss_tara.py 20 23 08 — meal karşılığının baştaki dört harfi ölçüm glossunda aranır): " + GKAP + "; tarama dışı (meal maddesinde karşılık / açılım kalıbı olmayan) kelimeler elle değerlendirilmedi — tam okuma sonu",
 "esmâ: 5:20:15 مَلِك 'degil' — 've ce'alekum mulûken', kural 'çoğul insan göndergeli → degil' (hükümdarlar); 5:20:20 أَحَد 'degil' — 'mâ lem yu'ti ehaden', kural 'olumsuz nekre ehad → degil'; 5:22:6 جَبّار 'degil' — 'qavmen cebbârîne', kural 'çoğul insan göndergeli → degil' (zorba kavim); "
 "5:23:21 مُؤْمِن 'degil' — 'in kuntum mu'minîn', kural 'çoğul insan göndergeli → degil' (inananlar) (esma_el_ekle → esma_kayit; e_el=? 0); kural adları kapalı listeyle ve geçmiş kayıtlarla karşılaştırıldı ('olumsuz nekre ehad → degil' sûre 3 kayıtlarında); "
 "'degil' göndergeleri A1'de betikle arandı (bölüm 3 denetimi kuralı 6): " + '; '.join("%s %s" % (k, 'A1 VAR' if k in M_A1 else 'A1 YOK') for k in ("'mulûken'", "'ehaden'", "'qavmen cebbârîne'", "'mu'minîn'")) + "; 5:21 esmâ yok; lafız 5:20 bir, 5:21 bir, 5:23 iki geçiş; 5:22 lafız yok; Rab yok",
 "esma_kayit: 5:20 'mühür EVET (ÇİFT) ton karma', 5:22 'mühür EVET ton celâl' (sınıf E/E), 5:23 'mühür EVET ton cemâl' — ölçüm esmâları MÜHÜRSÜZ (uyuşmuyor; esma_kayit 'degil' adlarını mühüre sayıyor, araç tanımı farkı, §8); 5:21 'mühür hayır' (uyuşuyor)",
 "ölçüm: 5:20 '{{1|yıldız yok}}', '{{1|fâsıla ٱلعلمين → ن, N sınıfı}}', '{{1|sayı işareti أَحَد}}', '{{1|simetri \\[3, 1, 10, 1\\]}}', '{{1|harf 96 → harf3 91, isaret 5}}' ve '{{1|dış düğüm 1}}'; 5:21 '{{2|biçim NEHY}}', '{{2|fâsıla خسرين → ن, N sınıfı}}', '{{2|harf 71 → harf3 68, isaret 3}}', '{{2|dış düğüm 0}}' ve '{{2|bağ: YOK \\(esit2, nakarat3, xref üçü de boş\\)}}'; "
 "5:22 '{{3|lafız YOK · Rab YOK}}', '{{3|fâsıla دخلون → ن, N sınıfı}}', '{{3|simetri \\[4, 7, 12, 1\\]}}', '{{3|harf 77 → harf3 73, isaret 4}}' ve '{{3|dış düğüm 0}}'; 5:23 '{{4|fâsıla مؤمنين → ن, N sınıfı}}', '{{4|simetri \\[4, 8, 12, 1\\]}}', '{{4|harf 102 → harf3 99, isaret 3}}' ve '{{4|dış düğüm 1}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); İÇ düğüm alanı blokta yok",
 "ölçüm aktör: 5:20 '{{1|adlı مُوسَى 3\\. sırada \\(kisi, rol fail\\+konusan\\)}}'; 5:22 '{{3|adlı مُوسَى 2\\. sırada \\(kisi, rol fail\\+muhatap\\)}}' — sözdiziminde nidâ (münâdâ), fail değil (araç tanımı farkı, §8); 5:23 '{{4|aktör: adsız `racül` 2\\. sırada}}' — nekre ikil fail; 5:21 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle): 5:20 emir, nida — IMPV 1 'zkurû' (6.), NEG 1 'lem' (18.), VOC 1 'yâ' (5.); 5:21 emir, yasak, nida — IMPV 1 'dxulu' (2.), PRO 1 'lâ' (9.), VOC 1 'yâ' (1.), biçim NEHY D2'de yazılmadı; 5:22 nida, şart — COND 1 'in' (13.), NEG 1 'len' (8.), VOC 1 'yâ' (2.); "
 "5:23 emir, şart — COND 1 'in' (19.), IMPV 2 'dxulû' (9.), 'tevekkelû' (18.); 'izâ' (5:23 12. kelime) morph T, cevaplı zaman — ölçüm COND sayımında değil; 'iz' (5:20 1. ve 10. kelime) morph T; blokta edilgen fiil yok",
 "yıldız: blokta yıldız yok (5:20-23)",
 "fâsıla: 5:19 ر (قدير) → 5:20 ن (ٱلعلمين) → 5:21 ن (خسرين) → 5:22 ن (دخلون) → 5:23 ن (مؤمنين); bölüm açılışında R → N geçişi, blok boyunca N sınıfı; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref: 5:20 xref 14:6 (basılmış); 5:23 xref okunmuş bir ayet; 5:21 ve 5:22 xref yok — sınıflama sinifla.py ile, basılmamışlar numarasız",
 "nakarat3 (R3: sayıyla özetlendi): 5:20 üç kalıp: ikisi süzgeç GEÇER, biri GEÇMEZ; 5:21 kalıp yok; 5:22 bir kalıp: süzgeç GEÇMEZ; 5:23 iki kalıp: biri süzgeç GEÇER, biri GEÇMEZ; bütün kalıplar tür ic",
 "araç tanımı farkları (R5; bölüm 2 denetimi kuralı 1: nakarat3 'tür' alanı 'tam' ya da 'ic' — sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si — taban sayımın kendi sözlüğünden betikle; karşılaştırma eşit aralıkla; bölüm 3 denetimi kuralı 12: eşi okunmamış hükümde gerekçe '(eş okunmamış, fark test edilmedi)', eşi okunmuşsa gerekçe okunmuş ayetin biçiminden): " + '; '.join(r5),
 "aktör / ad (1017, R1; bölüm 3 denetimi kuralı 5 — söz içi 1P / 1S / 2MP her geçişte 'adsız'; 3MP zamir ölçütü: fiil faili ya da zamir göndergesi anıldığında 'adsız' yazılır): 5:20 Mûsâ (adlı), 'li-qavmihî', söz içi 1S (adsız), muhatap 2MP (söz içi, adsız), Allah (lafız), 3MS (adsız — lafız), 'enbiyâ'e', 'mulûken', 'ehaden', 'l-'âlemîn'; "
 "5:21 söz içi 1S (adsız), muhatap 2MP (söz içi, adsız), 'l-arda'l-muqaddesete', Allah (lafız), 'xâsirîn'; 5:22 3MP (adsız), Mûsâ (adlı, nidâ), söz içi 1P (adsız), 3FS (kutsal toprak), 'qavmen cebbârîne', 3MP (adsız); 5:23 'raculâni', 'llezîne yaxâfûne', 3MP (adsız), Allah (lafız), 3D, muhatap 2MP (söz içi, adsız), 3MP (adsız — zorba kavim), 'l-bâbe', 'mu'minîn' — "
 "A1'e yazılmayanlar: 5:20 'fîkum' (muhatap içinde anıldı), 'mâ' 17. kelime (mevsûl; meal maddesinde); 5:22 'minhâ' 15. kelime (3FS içinde); blokta 'kâne / leyse' ismi nekre yok ('kuntum' ismi muhatap)",
 "söz / tırnak (bölüm 3 denetimi kuralı 7): 5:20 'qâle' (2. kelime) — söz 5. kelimede açılıyor, ayet sonunda kapanmıyor; 5:21 baştan sona söz (Mûsâ'nın sözü sürüyor; 'qâle' yok), 14. kelimede kapanıyor — tırnak 5:20 meal başında açılıp 5:21 meal sonunda kapandı; 5:22 'qâlû' (1. kelime) — söz 2-17. kelime; 5:23 'qâle' (1. kelime) — söz 9-21. kelime "
 "(16. kelime 've 'ale'llâhi' morph REM — söz içinde sürüyor: 'REM sapması', gerekçe 2MP muhatap ve emir sürüyor); morph 've' / 'fe' konumlarıyla kontrol edildi: 5:20 've iz' (1.) REM, 've ce'alekum' (14.), 've âtâkum' (16.) CONJ; 5:21 've lâ' (9.) REM, 'fe-tenqalibû' (13.) CAUS; 5:22 've innâ' (7.) CONJ, 'fe-in yaxrucû' (13.) REM, 'fe-innâ' (16.) RSLT; "
 "5:23 'fe-izâ' (12.) REM, 'fe-innekum' (14.) RSLT, 've 'ale'llâhi' (16.) REM, 'fe-tevekkelû' (18.) SUP",
 "◈ tetik (alıntılar önek ve edatsız; bölüm 3 denetimi kuralı 3 — alt sınıf kökten: أرض → K1, قلب → B3): 5:21 ◈K أرض ('l-arda' 3. kelime — K1; anlam notu: 'kutsal toprak', vaat edilen yer); 5:21 ◈B قلب ('tenqalibû' 13. kelime — B3; anlam notu: 'dönmek', organ anlamında değil — tetik aracı kökü mekanik okur); 5:20, 5:22, 5:23 tetik yok; "
 "tetik listesinde olmayan zaman / organ / yer adları (bölüm 2 denetimi kuralı 9, tarama): 5:20 'iz' (1. ve 10. kelime; zaman edatı); 5:21 'edbârikum' (12. kelime; arka — organ / yön adı, kök دبر tetik dışı); 5:22 'hattâ' (10. kelime; zaman sınırı); 5:23 'izâ' (12. kelime; zaman edatı), 'l-bâbe' (11. kelime; kapı — yer); oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8; bölüm 3 denetimi kuralı 11 — genel kalıplarda bir ölçüt): D3 eşleri bag listesiyle birebir — 5:20 (2:54, 14:6, 33:9, 61:5; 5:11 sûre içi), 5:21 (3:149), 5:22 (26:130), 5:23 eş yok (kontrol.py ile); bölüm geçişi 5:19 → 5:20 bağ kurulmadı; "
 "5:20 'zekera ni'me allâh 'alâ iz' (beş kelime) dizisinin basılmış eşlerinin hepsi bağlı (5:11, 14:6, 33:9); dört kelimelik 'zekera ni'me allâh 'alâ' dizisindeki 5:7 ve 35:3 D3 dışı — gerekçe: 'iz' ile gelen anma kalıbı ölçüt, kısa dizi genel; "
 "5:23 ''alâ allâh tevekkel' (genel kalıp) basılmış eşleri 3:122, 5:11 ve 64:13 hepsi D3 dışı (bağ yok; ölçüt bir); 5:20 'qâle mûsâ li-qavmih' basılmış eşleri 2:54, 14:6, 61:5 hepsi bağlı",
 "◈A A4 (R9 + kapsam; bölüm 3 denetimi kuralı 2): 5:20 bölüm açılışı; edim geçişi nida → emir, nida (ayetler arası); şahıs geçişi 2 → 3 (ayetler arası); söz açılır (5. kelime); 5:21 edim geçişi emir, nida → emir, yasak, nida (ayetler arası); şahıs geçişi 3 → 2 (ayetler arası); söz kapanır (14. kelime); "
 "5:22 edim geçişi emir, yasak, nida → nida, şart (ayetler arası); şahıs geçişi 2 → 3 (ayetler arası); söz açılır (2. kelime); söz kapanır (17. kelime); şart → cevap (ayet içi; COND 'in' 13. kelime); 5:23 edim geçişi nida, şart → emir, şart (ayetler arası); şahıs geçişi 3 → 2 (ayetler arası); söz açılır (9. kelime); söz kapanır (21. kelime); şart → cevap (ayet içi; COND 'in' 19. kelime) — cevap öne alınmış; "
 "liste dışı gözlem (A4'e yazılmadı): 5:20-21'de muhatap kavim (2MP), 5:22'de konuşan kavim (1P), 5:23'te muhatap kavim (2MP)",
 "sözdizimi (okuma; 'atıf' / 'istînâf' / 'hâl' her geçişte morph etiketiyle; 'X'a atıf' yazımında X ma'tûf aleyh): 5:20 've iz qâle' — istînâf (morph REM), zaman 'iz'; 'yâ qavmi' — nidâ; 'zkurû' — emir; 'iz ce'ale' — 'ni'mete'nin açıklaması (zaman); 've ce'alekum' ve 've âtâkum' — 'ce'ale'ye atıf (morph CONJ); 'mâ lem yu'ti' — mevsûl + olumsuz; "
 "5:21 'yâ qavmi' — nidâ (5:20 sözünün sürmesi); 'dxulu' — emir; 'lletî ketebe' — 'l-arda'nın sıfatı (mevsûl); 've lâ tertaddû' — istînâf (morph REM), yasak; 'fe-tenqalibû' — sebep / sonuç (morph CAUS, mansub); 5:22 'qâlû' — yeni cümle; 'inne fîhâ' — 'inne' cümlesi; 've innâ' — 'inne' cümlesine atıf (morph CONJ); "
 "'hattâ yaxrucû' — gaye; 'fe-in yaxrucû' — istînâf (morph REM), şart; 'fe-innâ dâxilûn' — şart cevabı (morph RSLT); 5:23 'qâle raculâni' — yeni cümle; 'en'ame'llâhu 'aleyhimâ' — 'raculâni'nin sıfatı; 'fe-izâ dexaltumûhu' — istînâf (morph REM), zaman; 'fe-innekum' — cevap (morph RSLT); 've 'ale'llâhi' — istînâf (morph REM); 'fe-tevekkelû' — morph SUP",
 "okuma (gözlem) (iddialar ölçüm ve morph ile denetlendi; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için, aralık sonu dahil): 5:20 've iz qâle mûsâ li-qavmih' ile açılıyor (1-4. kelime) — 2:54 ve 61:5 ile kalıp eşi; 5:20 'zkurû ni'meta'llâhi 'aleykum' (6-9. kelime) 5:7 ve 5:11 ile — sûre içinde anma emri, burada Mûsâ'nın sözünde; "
 "5:21 'dxulu' (2. kelime) / 5:22 'len nedxulehâ' (8-9. kelime) / 5:23 'dxulû' (9. kelime) — kök دخل dört ayetin üçünde, 5:22'de iki geçiş (9. ve 17. kelime); 5:22 'fe-innâ dâxilûn' (16-17. kelime) şart cevabı; 5:23 've 'ale'llâhi fe-tevekkelû' 5:11 ile önek farkıyla eş",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (sunum/es_edat.py 8 — morph etiketli, zamirler birleşik): " + ES
 + "; eş lemmaya farklı karşılık (bölüm 3 denetimi kuralı 10 — komut 'python3 sunum/es_lemma.py 8'; bölüm 4'ün bu bloğu): " + (ESL or 'yok')
 + "; bölümler arası eş lemma karşılığı (elle): 'ard' 5:21 'toprak' / 5:17 'yeryüzü', 5:17 ve 5:18 'yer'; 'qavm' 5:20-22 'kavim' (eş); emsal meal karşılık farkları (bölüm 2 denetimi kuralı 6): 'qâle mûsâ li-qavmihî yâ qavmi' 5:20 'Mûsâ kavmine demişti: Ey kavmim' / 2:54 ve 61:5 (eş); "
 "'zkurû ni'meta'llâhi 'aleykum' 5:20 'anın' / 14:6 'hatırlayın' (fark); 'tenqalibû xâsirîn' 5:21 'hüsrana uğramış olarak dönersiniz' / 3:149 (eş); 'cebbâr' 5:22 'zorba' / 26:130 'zorbalar' (eş) — tam okuma sonu",
 "KARSILIK_CAKISMA",
 "çıpa: 5:20-23 tarayıcı aday vermedi (cipa_tarama5_adaylari.json); anma emri, giriş emri, ret sözü, giriş ve tevekkül emri (olgu=False); L3 / L4 adayı yok",
 "aday 1039: ayet içi 5:21 (''dxulu'l-arda' / 've lâ tertaddû 'alâ edbârikum'), 5:22 ('len nedxulehâ' / 'fe-innâ dâxilûn') — okuma; ayetler arası 5:21 / 5:22 (''dxulu' / 'len nedxulehâ'), 5:22 / 5:23 ('len nedxulehâ' / ''dxulû 'aleyhimu'l-bâb') — blok içi",
 "aday 1041: kök نعم 5:20 'ni'meta'llâhi' (lafzın nimeti) ve 5:23 'en'ame'llâhu' (lafzın nimet vermesi) — insan göndergeli kullanım yok; kök ملك 5:20 'mulûken' — insanlar için hükümdarlık (lafız göndergeli 'mulk' 5:17-18 ile kök eşi) — okuma",
 "bölüm: " + BOL + " bölümü, bölüm 4-1 — bölüm açılışı 5:20; bölüm iki blok (blok planından: 8 ve 9); başlıktaki 'kutsal topraklar' 5:21 (''dxulu'l-arda'l-muqaddesete'); 'kırk yıl' blok 9'da; mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; "
 "bölüm 3 denetimi bulguları ve yeni kuralları bu ARIZA'nın başında; uygulanan araç değişiklikleri: sunum/yasakli.sh kelime sınırı Türkçe harf sınıfıyla (kural 1; 'değil' yanlış pozitifi giderildi), sunum/ayn_kontrol.py (kural 4; ayn / hemze düşmesi bütün alıntı biçimlerinde — bölüm 3 bulgusu 5'i yeniden üretiyor), sunum/gloss_tara.py (kural 8); "
 "ÖNEMLİ DÜZELTME: bloklar 5-7'de yasakli.sh dosya argümanı verilmeden koşulmuştu (standart girdiyi bekleyip zaman aşımına düştü; 'temiz' kaydı yanlış) — bu bloktan itibaren dosyalarla koşuluyor, kayıtlar geriye dönük yeniden yazılmadı (§8); medde taraması (sunum/medde.py b08/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 2 denetimi kuralları 4-5, bölüm 3 kuralı 9; sunum/lem_bozuk.py 08): 5:23:18 'tevekkel' — meal maddesinde ve R5 kalıp adında '(morph LEM ham biçim)' notlu; aracın bayraklamadığı ham biçim yok",
 "sonradan basılan (bölüm 8 kuralı 1; bölüm 16 denetimi kuralı 3; bölüm 1 denetimi kuralı 1 — lemma dizileri dahil; sunum/sonradan.py --plan 8): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('mûsâ', 'qavm', 'ni'me', 'nebiyy', 'melik', 'ehad', ''âlem', 'ard', 'muqaddese', 'dubur', 'xâsir', 'cebbâr', 'dâxil', 'racul', 'bâb', 'ğâlib', 'mu'min'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları ve hemze sınırı yapıntısı (5:22 'cebbârîne ve innâ', 5:23 'yaxâfûne en'ame' — iskelet tekilleştirmesi hemze ayrımından önce); wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi; ayn_kontrol 0",
]


def yaz():
    items = [kes(x) for x in I]
    s = '\n (20, 23): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_20_23.txt', 'w', encoding='utf-8').write(s)


idx = I.index('KARSILIK_CAKISMA')
I[idx] = 'karşılık çakışması (geçici)'
yaz()
CAK = run('/home/claude/sunum/cakisma.py', '/home/claude/yamalar/ariza_5_20_23.txt')
KARAR = {}
if os.path.exists('/home/claude/b08/yap/karar.py'): exec(open('/home/claude/b08/yap/karar.py', encoding='utf-8').read())
I[idx] = ("karşılık çakışması (bölüm 3 denetimi kuralı 10 — komut 'python3 sunum/cakisma.py yamalar/ariza_5_20_23.txt'; bölüm 4'ün bu bloğu; kararlar morph LEM eşitliğine göre; Türkçe fiil kökü eşlemesi elle — 'gir-' / 'giren', 'dön-' / 'geri dön-' gözden geçirildi): "
          + ('; '.join(KARAR.get(l.split(' ←')[0], l + ' — karar yok') for l in CAK.splitlines()) if CAK else 'çakışma yok'))
yaz()
print('yazıldı', len(I))
print(CAK)
print('\n'.join(r5))
print(MEDF)
print(GKAP)

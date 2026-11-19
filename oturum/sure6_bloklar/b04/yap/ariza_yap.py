# sûre 6 blok 4 (6:16-19) ARIZA oluşturucu — bölüm 2-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b04/olcum.txt'
os.environ['SAY2'] = '/home/claude/b04/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {}
BOL = "'Mülk kimin; şahit olarak Allah'"


def sd(key):
    return sayim.S2[key][1]


def sic(key):
    n, d = sayim.S2[key]
    return 1 + len([x for x in d['basilan'] if x.startswith('6:')]) + d['okunmus_si'] + d['henuz_si']


def taban(key, ay):
    n, d = sayim.S2[key]
    p = [ay] + [x for x in d['basilan'] if x.startswith('6:') and x != ay]
    if d['okunmus_si']: p.append('okunmus_si %d' % d['okunmus_si'])
    if d['henuz_si']: p.append('henuz_si %d' % d['henuz_si'])
    return ' + '.join(p)


R5 = [
 ("6:17", "''alâ kull şey''", 2, 'say 6:17 14-16', "harekesiz ''alâ kulli şey'' (14-16. kelime)", None),
 ("6:18", "'_ qâhir fevq 'abd'", 2, 'say 6:18 1-4', "harekesiz 've huve'l-qâhiru fevqa 'ibâdih' (1-4. kelime)", None),
 ("6:19", "'berî' mimmâ eşrake'", 2, 'say 6:19 35-37', "harekesiz 'berî'un mimmâ tuşrikûn' (35-37. kelime)", None),
]
r5 = []
for ay, kal, nk, key, ad, dz, *tr_ in R5:
    s = sic(key)
    h = "%s nakarat3 %s %d (tür %s) / %s sûre içi %d (%s)" % (ay, kal, nk, (tr_[0] if tr_ else 'ic'), ad, s, taban(key, ay))  # bölüm 11 denetimi kuralı 3
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

VF_YAZI = {16: {7: "'ve zâlike'"}, 17: {1: "'ve in'", 10: "'ve in'"}, 18: {1: "'ve huve'", 5: "'ve huve'"}, 19: {10: "'ve beynekum'", 11: "'ve ûhiye'", 17: "'ve men'", 34: "'ve innenî'"}}
sys.path.insert(0, '/home/claude/b04/yap')
from seg import meals
MEALS = meals()


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
open('/home/claude/b04/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '04')
BLOKLAR = [str(i) for i in range(1, 5)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '4', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b04/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '16', '19', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b04/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b04/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '16', '19', '04').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_16_19.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:16', '6:17', '6:18', '6:19'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_16_19.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(16, 20))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:19 kök أخر ('uxrâ' 25. kelime — başka): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '16', '19', '04')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b04/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 5)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(16, 20))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: sunum/edat_etiket.py EDLEM'e 'zâ' (ذا) ve 'eyy' (أي) — bölüm 15 denetimi kuralı 15: es_edat 6:16 ve 6:19 başlıklarını tanımıyordu; sunum/bolum17_kurallar.py kural 3 ortak lemma dizisinde 'dizi S a i j' anahtarını da kabul eder (zamir eki farkında harekesiz eş yok — 6:16 / 40:9 'rahimehû' / 'rahimtehû'); sunum/yasakli.sh IKI kümesine 'türlü türlü' — bölüm 8 kuralı 16: kapsamayan kök listesindeki صرف kök anlamı Türkçe ikileme, araç çıktısı aynen; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 118",
 "kök tablosu: ölçümde '???' 6:16, 6:17, 6:18 ve 6:19 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 16 19 04'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
   "esmâ: 6:16 'l-fevzu'l-mubîn' (8-9. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (kurtuluşun sıfatı); "
 "6:17 'fe-huve 'alâ kulli şey'in qadîr' (13-17. kelime) ve 6:18 've huve'l-hakîmu'l-xabîr' (5-7. kelime) — esma_el 'ilahi', kural 'zamirin haberi' (Allah) — 'huve' göndergesi 6:17 3. kelimedeki lafız; "
 "6:19 'llâhu şehîdun beynî ve beynekum' (7-10. kelime) — esma_el 'ilahi', kural 'lafzın haberi' (Allah); "
 "lafız 6:17 ve 6:19; Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7); 'zamirin haberi' kapalı listede (sûre 6 hazırlığı varsayılan kararı, onaya açık)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 16 19 04'; bölüm 13 denetimi kuralı 2: esma_el eklendikten sonra; bölüm 15 denetimi kuralı 5; 6:16 ve 6:17 muhur EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, araç tanımı farkı): " + EMH,
 "ölçüm: 6:16 '{{1|fâsıla ٱلمبين → ن, N sınıfı}}', '{{1|simetri \\[3, 1, 5, 1\\]}}', '{{1|harf 39 → harf3 36, isaret 3}}', '{{1|dış düğüm 1}}' ve '{{1|EDİLGEN 1/2 fiil, pas z=2,52}}'; "
 "6:17 '{{2|fâsıla قدير → ر, R sınıfı}}', '{{2|simetri \\[3, 1, 10, 1\\]}}', '{{2|harf 62 → harf3 56, isaret 6}}' ve '{{2|dış düğüm 2}}'; "
 "6:18 '{{3|fâsıla ٱلخبير → ر, R sınıfı}}', '{{3|harf 34 → harf3 32, isaret 2}}' ve '{{3|dış düğüm 0}}'; "
 "6:19 '{{4|fâsıla تشركون → ن, N sınıfı}}', '{{4|simetri \\[6, 19, 27, 2\\]}}', '{{4|harf 150 → harf3 137, isaret 13}}', '{{4|dış düğüm 2}}', '{{4|sayı işareti واحِد}}' ve '{{4|EDİLGEN 1/10 fiil, pas z=0,24}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 16 19 04'): KALAN_P",
 "ölçüm aktör: 6:19 '{{4|aktör: adlı قُرْءان 14\\. sırada \\(kitab, rol fail\\)}}' — edilgen 'ûhiye' naib-i faili; 6:16, 6:17 ve 6:18 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:16 şart — COND 1 'men' (1.), CERT 1 'fe-qad' (5.); "
 "6:17 şart — COND 2 'in' (1., 10.), NEG 1 'fe-lâ' (5.); 6:18 haber, kip yok; 6:19 soru, emir — IMPV 4 'qul' (1., 6., 26., 29.), INTG 2 'eyyu' (2.), 'e'innekum' (19.), EMPH 1 'le-teşhedûne' (20.), NEG 1 'lâ' (27.); "
 "morph REM ('ve' 6:16 7.; 6:19 11.), RSLT ('fe' 6:16 5.; 6:17 5. ve 13.), ACC ('inne' 6:19 19., 30. ve 34.; 'enne' 6:19 21.), EXP ('illâ' 6:17 8.), PRP ('li' 6:19 15.), PREV ('mâ' 6:19 30.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:16 ★★ (kaynak pas, z=2,52); 6:19 ★★ (kaynak n, z=2,61); 6:17 ve 6:18 yıldız yok",
 "fâsıla: 6:15 م → 6:16 ن (ٱلمبين) → 6:17 ر (قدير) → 6:18 ر (ٱلخبير) → 6:19 ن (تشركون) — N sınıfından R sınıfına geçiş ve dönüş; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:16 40:9 (emsal olarak basıldı); 6:17 10:107 (emsal olarak basıldı) ve okunmuş 1 ayet; 6:18 yok; 6:19 3:18 (emsal olarak basıldı) ve okunmamış 1 ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:17 ''alâ kull şey'' süzgeç GEÇMEZ; 6:18 '_ qâhir fevq 'abd' GEÇER; 6:19 'berî' mimmâ eşrake' GEÇMEZ; 6:16 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; edilgen fiilde 'naib-i faili' — bölüm 11 denetimi kuralı 17; açık naib-i failde 'adsız' yazılmaz — sûre 6 bölüm 1 denetimi kuralı 6): "
 "6:16 3MS ('yusraf' edilgen — naib-i faili zamir, gönderge 6:15 7. kelime; diğerleri adsız — gönderge 'men' ve 6:15 6. kelime); 6:17 muhatap 2MS (adsız), 3MS ('yemseske' 2. kelime — fail lafız 3. kelime; diğerleri adsız — gönderge lafız ve 'durr'); "
 "6:18 3MS (adsız — gönderge 6:17 3. kelimedeki lafız); 6:19 muhatap 2MS ve 2MP, konuşan 1S (adsız; söz içi), 3MS ('ûhiye' edilgen — naib-i faili 'l-qur'ânu' 14. kelime; diğerleri adsız) — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): "
 "6:19 'qul' (1.) ardından söz 2-5. kelime, 'qul' (6.) ardından söz 7-25. kelime (REM sapması 6:19 (11. kelime) — 've ûhiye' söz içinde istînâf, söz 25. kelimeye dek sürer), 'qul' (26.) ardından söz 27-28. kelime, 'qul' (29.) ardından söz 30-37. kelime — ayet içi kapanışlar; "
 "6:16, 6:17 ve 6:18 söz yok; mealde tırnaksız, iki nokta ile (blok meal biçimi); A3'te ve A4'te 'söz açılır' / 'söz kapanır'; 'qul' 6:19 (bölüm 10 denetimi kuralı 8); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 16 19 04' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 6:16 'fe-qad' (5.) RSLT, 've zâlike' (7.) REM; 6:17 've in' (1., 10.) CONJ, 'fe-lâ' (5.), 'fe-huve' (13.) RSLT; 6:18 've huve' (1., 5.) CONJ; "
 "6:19 've beynekum' (10.), 've men' (17.), 've innenî' (34.) CONJ, 've ûhiye' (11.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:16 ◈K يوم ('yevme'izin' 4. kelime — K2; anlam notu: azabın çevrildiği gün)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 16 19 04'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:16 (40:9); 6:17 (10:107); 6:19 (3:18); 6:18 D3 yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "ayetler arası kalıp yok; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:16 şahıs geçişi 1 → 3, edim geçişi emir → şart, şart → cevap; 6:17 şart → cevap (1. ve 10. kelime); 6:18 edim geçişi şart → haber; "
 "6:19 söz açılır / kapanır (2-5., 7-25., 27-28. ve 30-37. kelime, ayet içi), şahıs geçişi 3 → 2, edim geçişi haber → soru, bölüm kapanışı; "
 "şahıs beraberliği yok (sûre 6 bölüm 1 denetimi kuralı 9)",
 "sözdizimi (okuma; morph etiketiyle): 6:16 'men yusraf' — şart (morph COND); 'fe-qad rahimeh' — şart cevabı ve tahkik (morph RSLT + CERT); 6:17 'in yemseske' — şart (morph COND); 'fe-lâ kâşife' — cins nefyi (morph NEG); 'illâ huve' — istisna (morph EXP); "
 "6:18 've huve'l-qâhiru' — isim cümlesi; 6:19 'eyyu şey'in' — soru (morph INTG); 'li-unzirakum' — amaç (morph PRP); 'e'innekum le-teşhedûne' — soru, tekit (morph INTG + ACC + EMPH); 'innemâ' — kasr (morph ACC + PREV)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:16 'men yusraf 'anhu yevme'izin' ile açılıyor (sayım: 'say 6:16 1-4'); "
 "6:16 4-7. kelime 40:9 ile lemma dizisinde eş, zamir eki farkı (sayım: 'dizi 6 16 4 7'); 6:17 've in yemseske'llâhu bi-durr' ile açılıyor — 10:107 ile eş (sayım: 'say 6:17 1-4'); 6:17 'durr' / 'xayr' karşıtlığı; "
 "6:19 kök شهد ikilemesi ('şehâdeten', 'şehîdun', 'le-teşhedûne', 'eşhed'); 6:19 'âliheten uxrâ' / 'ilâhun vâhid' karşıtlığı; 6:19 'qul' ile açılıyor",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 04'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3): "
 "'yevme'izin' 6:16 'O gün' / 40:9 'O gün' (emsal metninde) — çakışma değil; "
 "'ve in yemseske'llâhu bi-durr' 6:17 'Allah sana bir zarar dokundurursa' / 10:107 'Allah sana bir zarar dokundurursa' (emsal metninde) — çakışma değil; "
 "'yemseske'llâhu bi-durr' 6:17 'Allah sana bir zarar dokundurursa' / 10:107 'Allah sana bir zarar dokundurursa' (emsal metninde) — çakışma değil; "
 "'fe-lâ kâşife lehû illâ huve' 6:17 'onu O'ndan başka kaldıracak yoktur' / 10:107 'onu O'ndan başka kaldıracak yoktur' (emsal metninde) — çakışma değil; "
 "'kâşife lehû illâ huve' 6:17 'onu O'ndan başka kaldıracak yoktur' / 10:107 'onu O'ndan başka kaldıracak yoktur' (emsal metninde) — çakışma değil; "
 "'llâhu' 6:19 'Allah' / 3:18 'Allah' (emsal metninde) — çakışma değil; "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9): 6:16 'yusraf' IMPF JUS (şart) — meal şart 'çevrilirse'; 'rahimeh' PERF — meal '-miştir'; 6:17 'yemseske' IMPF JUS (şart) — meal şart 'dokundurursa'; "
 "6:19 'li-unzirakum' IMPF SUBJ — meal istek 'uyarayım diye'; 'le-teşhedûne' IMPF IND — meal şimdiki zaman soru 'ediyorsunuz'; 'eşhed' IMPF IND — meal geniş zaman olumsuz 'etmem'; 'tuşrikûn' IMPF — meal '-dukları'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 16 19 04'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:16, 6:17, 6:18 ve 6:19 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:17 ('durr' / 'xayr'); 6:19 ('âliheten uxrâ' / 'ilâhun vâhid'); 6:16 ve 6:18 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök شهد 6:19 ('şehâdeten', 'şehîdun', 'le-teşhedûne', 'eşhed') — şahitlik bağı; lafız 6:17 ve 6:19 — 'huve' göndergesi 6:18; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 2-2 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm iki blok (3, 4); bu blok bölümü kapatıyor; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b04/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 16 19 04'; lem_bozuk.py 04 çıktısı): lem_bozuk bayrağı yok; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 16 19 → AYN_SONUC; sunum/bolum4_kurallar.py 16 19 04 → KHATA_HEPSI; sunum/bolum5_kurallar.py 16 19 04 → B5_HEPSI; sunum/bolum6_kurallar.py 16 19 04 → B6_HEPSI; sunum/bolum7_kurallar.py 16 19 04 → B7_HEPSI; sunum/bolum8_kurallar.py 16 19 04 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 16 19 04 → B9_HEPSI; sunum/bolum10_kurallar.py 16 19 04 → B10_HEPSI; sunum/bolum11_kurallar.py 16 19 04 → B11_HEPSI; sunum/bolum12_kurallar.py 16 19 04 → B12_HEPSI; sunum/bolum13_kurallar.py 16 19 04 → B13_HEPSI; sunum/bolum14_kurallar.py 16 19 04 → B14_HEPSI; sunum/bolum15_kurallar.py 16 19 04 → B15_HEPSI; sunum/bolum16_kurallar.py 16 19 04 → B16_HEPSI; sunum/bolum17_kurallar.py 16 19 04 → B17_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok, IKI kümesine 'türlü türlü' eklendi",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 4 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('yevm', 'iz', 'qad', 'rahime', 'zâ', 'fevz', 'mubîn', 'in', 'messe', 'allâh', 'durr', 'lâ', 'kâşif', 'illâ', ''alâ', 'kull', 'şey'', 'qadîr', 'qâhir', 'fevq', ''abd', 'hakîm', 'xabîr', 'inne', 'şehide', 'enne', 'ma'a', 'ilâh', 'âxar', 'berî'', 'mimmâ', 'eşrake'); lemmasız öğe joker '_' ('huve'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (16, 19): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_16_19.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b03.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '16', '19'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '16', '19', '04'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '16', '19', '04'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '16', '19', '04', '--tazelik-yok')}
    for _n in range(7, 18): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '16', '19', '04')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17 = [_R['B%d' % _n].splitlines() for _n in range(6, 18)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
           'MUT_SONUC': (MUT[-1] if MUT else '?'), 'GERI_P': ' / '.join(x.lstrip('# ') for x in GERI), 'B6_ESMA': ('; '.join(l[5:] for l in B6 if 'esmâ kural' in l and l.startswith('HATA')) or 'sapma 0')}
    I_cur = list(I_HAM)
    for k, v in REP.items(): I_cur = I_cur[:len(BEK)] + [x.replace(k, v) for x in I_cur[len(BEK):]]  # bölüm 9 kuralı 9: taşınan denetim maddelerine yer tutucu değişimi uygulanmaz
    I_cur[idx] = ("karşılık çakışması (bölüm 4 kuralı 4, bölüm 5 kuralı 3, bölüm 6 kuralı 2 — komut 'python3 sunum/cakisma.py' + sûre 6'nın okunmuş bütün ARIZA dosyaları; bu bloğun karşılıklarına dokunan gruplar ve son dosyaya dokunan KÖK grupları; grup başına tam bir kapalı karar: 'çakışma değil' ya da 'çakışma — tam okuma sonu'): "
                  + ('; '.join(KARAR.get(l.split(' ←')[0].strip() if not l.startswith('KÖK') else 'KÖK ' + l.split()[1], l + ' — karar yok') for l in CAK_L) if CAK_L else 'bu bloğa dokunan çakışma yok'))
    if I_cur == onceki: break
    onceki = list(I_cur)
yaz(I_cur)
print('yazıldı', len(I_cur), 'tur', tur)
print('\n'.join(CAK_L))
print(GLS)
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17): print([l for l in _x if l.startswith('HATA') or 'hata' in l])

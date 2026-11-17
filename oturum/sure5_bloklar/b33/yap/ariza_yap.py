# blok 33 (5:109-110) ARIZA oluşturucu — bölüm 15-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b33/olcum.txt'
os.environ['SAY2'] = '/home/claude/b33/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b32.txt', encoding='utf-8').read() + ']')
VF_YAZI_ESKI = {33: {6: "'ve rasûlehû'", 7: "'ve yes'avne'", 18: "'ve erculuhum'", 30: "'ve lehum fi'l-âxirati'"}, 34: {9: "'fa'lemû'"}, 35: {6: "'ve'bteğû'", 9: "'ve câhidû'"}, 36: {11: "'ve mislehû'", 22: "'ve lehum 'azâbun'"}}
BOL = "'Elçilerin toplanması; İsâ'ya verilen nimetler; havariler ve sofra'"


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
 ("5:109", "'inne _ 'allâm ğuyûb'", 2, 'say 5:109 12-15', "harekesiz 'inneke ente 'allâmu'l-ğuyûb' (12-15. kelime)", ('dizi 5 109 12 15', "inne _ 'allâm ğuyûb", '12-15', "biçim farkı (dizi 5 109 12 15): basılmamış eş yazım eş")),
 ("5:110", "'iz qâle allâh 'îsâ ibn meryem'", 2, 'say 5:110 1-6', "harekesiz 'iz qâle'llâhu yâ 'îse'bne meryem' (1-6. kelime)", ('dizi 5 110 1 6', "iz qâle allâh 'îsâ ibn meryem", '1-6', "biçim farkı (dizi 5 110 1 6): basılmamış eş önek")),
 ("5:110", "''îsâ ibn meryem'", 3, 'say 5:110 4-6', "harekesiz 'yâ 'îse'bne meryem' (4-6. kelime; biçim öğesi 'yâ' — nida öneki harekesiz kalıpta; ◇ lemma dizisi 'dizi 5 110 4 6' sûre içi 6, harekesiz kalıp 3)", ('dizi 5 110 4 6', "'îsâ ibn meryem", '4-6', "biçim farkı (dizi 5 110 4 6)")),
 ("5:110", "'ellezî kefera min'", 2, 'say 5:110 56-58', "harekesiz 'llezîne keferû minhum' (56-58. kelime; biçim öğesi 'min' — zamir eki ve yazım farkı; ◇ lemma dizisi 'dizi 5 110 56 58' sûre içi 4, harekesiz kalıp 2)", ('dizi 5 110 56 58', "ellezî kefera min", '56-58', "biçim farkı (dizi 5 110 56 58): basılmamış eş zamir eki; 5:73 yazım eş; 5:78 zamir eki")),
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

VF_YAZI = {109: {5: "'fe-yeqûlu'"}, 110: {10: "'ve 'alâ'", 20: "'ve kehlen'", 21: "'ve iz'", 27: "'ve iz'", 34: "'fe-tenfuxu'", 36: "'fe-tekûnu'", 39: "'ve tubri'u'", 43: "'ve iz'", 47: "'ve iz'", 55: "'fe-qâle'"}}
sys.path.insert(0, '/home/claude/b33/yap')
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
open('/home/claude/b33/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '33')
BLOKLAR = [str(i) for i in range(1, 34)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '33', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b33/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '109', '110', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b33/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b33/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '109', '110', '33').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_109_110.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'5:109', '5:110'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_109_110.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '5:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '5:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(109, 111))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "5:109 kök جمع ('yecme'u' 2. kelime — toplama): tetik listesinde yok; 5:110 'iz' (1. kelime, 12. kelime, 21. kelime, 27. kelime, 43. kelime, 47. kelime ve 52. kelime — morph T, zaman); 5:110 kök أذن ('bi-iznî' 33., 38., 42. ve 46. kelime — izin; kök anlamı 'kulak', organ anlamında kullanılmıyor): tetik listesinde yok; 5:110 kök كفف ('kefeftu' 48. kelime — alıkoyma; kök anlamı 'avuç', organ anlamında kullanılmıyor): tetik listesinde yok; 5:110 kök سحر ('sihrun' 62. kelime — büyü): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '109', '110', '33')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b33/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 34)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b5:%d:\d+' % a_, s_) for a_ in range(109, 111))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bölüm 14 denetiminin araç kuralları — sunum/bolum14_kurallar.py yeni (kurallar 2, 3, 4, 5, 6, 7, 8, 10; kural 6 taşınan denetim maddelerini süzer — bekleyen metni örnek harf anıyor); "
 "sunum/cakisma.py, sunum/bolum7_kurallar.py ve sunum/bolum9_kurallar.py Türkçe alıntıdaki iç kesmeyi ('Kur'an') gloss_tara regex'iyle okur — KÖK 'an-' yapıntısı düştü (kural 1); sunum/cakisma_sina.txt yeni — cakisma.py kesme okumasının sınama girdisi (kural 1); sunum/bolum9_kurallar.py kural (2): Arapça kök anmayan KÖK 'çakışma değil' kararı üye kökleriyle denetlenir (kural 1); "
 "sunum/edat_etiket.py EDLEM kümesine 'hîne' ve 'lâkinne' (kural 9); sunum/geriye_donuk.py bolum14_kurallar'ı geriye dönük kümeye alır (kural 1 ve kural 2-10 geriye dönük uygulandı); "
 "sunum/yasakli.sh 'beş' sayısı + iyelik dalı 'beşik' adını dışlar (bölüm 8 kuralı 2 yanlış pozitifi; sunum/yasakli_test.txt'e sayı + iyelik OLUMLU ve 'beşikte' OLUMSUZ satırı) ve IZIN listesine 3:46 emsal alıntısı (bölüm 10 denetimi kuralı 10 — yeni izin dosyaya özgü ve tırnaklı); sunum/mutasyon_sina.py bölüm 14 sınamaları (kural 1: KÖK 'an-' yokluğu, Arapça kök anmayan KÖK kararı mutasyonu ve cakisma.py eski regex mutasyonu — girdi sunum/cakisma_sina.txt; kural 9: 'hîne', 'lâkinne' tanınıyor ve edat_etiket.py kaydı silinince tanınmıyor; kurallar 2-8 ve 10: bozuk kayıtta isabet); mutasyon_sina — MUT_SONUC; "
 "geriye dönük koşu son araç değişikliğinden sonra yeniden üretildi (GERI_P); yeni 78 — bolum14_kurallar 54 (kural 2: 22, kural 8: 14, kural 10: 5, kural 3: 4, kural 6: 3, kural 7: 3, kural 4: 2, kural 5: 1), "
 "bolum9_kurallar kural (2) KÖK kararı 19 (bölüm 14 denetimi kuralı 1 genişlemesi; okunmuş bloklarda Arapça kök anmayan 'çakışma değil' kararları), bolum13_kurallar 2 (blok 22 R5 satırı; basılan değişti), "
 "çakışma grubu karar sayısı 1 (blok 31 'üz-' — kesme okuması), es_edat tanınmayan 1 (blok 32 'zâ'), gloss_tara KAPSAMAYAN 1 (blok 32 kapsam sayımı, TARANMAYAN değil); "
 "düşen 4 — araç değişti 2 (es_edat 'lâkinne', 'hîne' artık tanınıyor), basılan değişti 2; kayıtlar geriye dönük yeniden yazılmadı; hat sırası (bölüm 13 denetimi kuralı 2): esma_el_ekle ve esma_kayit ARIZA üretiminden önce koşuldu",
 "kök tablosu: ölçümde '???' 5:109 ve 5:110 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 109 110 33'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:110 'mubîn' (63. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (büyünün sıfatı); 5:109 esmâ yok; lafız 5:109 ve 5:110; Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 109 110 33'; bölüm 13 denetimi kuralı 2: esma_el eklendikten sonra): " + EMH,
 "ölçüm: 5:109 '{{1|fâsıla ٱلغيوب → ب, ب sınıfı — KAFİYE KIRILMASI}}', '{{1|EDİLGEN 1/4 fiil, pas z=1,10}}', '{{1|simetri \\[3, 5, 8, 1\\]}}', '{{1|harf 62 → harf3 58, isaret 4}}', '{{1|dış düğüm 3}}' ve '{{1|İÇ düğüm 1}}'; "
 "5:110 '{{2|fâsıla مبين → ن, N sınıfı}}', '{{2|simetri \\[6, 47, 56, 2\\]}}', '{{2|harf 285 → harf3 275, isaret 10}}' ve '{{2|dış düğüm 10}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 109 110 33'): KALAN_P",
 "ölçüm aktör: 5:109 aktör yok; 5:110 '{{2|adlı عِيسَى 4\\. sırada \\(kisi, rol meful\\+muhatap\\)}}' — münadâ ve söz muhatabı; '{{2|adlı مَرْيَم 6\\. sırada \\(kisi, rol mecrur\\)}}' — 'ibn' muzâfun ileyhi; "
 "'{{2|adlı تَوْراة 25\\. sırada \\(kitab, rol meful\\)}}' ve '{{2|adlı إِنجِيل 26\\. sırada \\(kitab, rol meful\\)}}' — ''allemtuke' mef'ûlleri; '{{2|adlı إِسْرائِيل 50\\. sırada \\(kavim, rol mecrur\\)}}' — 'benî' muzâfun ileyhi",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 5:109 soru — INTG 1 'mâzâ' (6.), NEG 1 'lâ' (9.); "
 "5:110 emir, nida — VOC 1 'yâ' (4.), IMPV 1 'zkur' (7.), NEG 1 'in' (59.), RES 1 'illâ' (61.); ölçüm biçim alanı '{{2|biçim DIKKAT \\+ HASR}}' (yalnız bu maddede; HASR gerekçesi 'in' NEG + 'illâ' RES — 59. ve 61. kelime); "
 "morph REM ('fe' 5:110 55.), ATT ('hâ' 5:110 60.) ve T ('yevme' 5:109 1.; 'iz' 5:110 1., 12., 21., 27., 43., 47. ve 52.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 5:109 ★ (kaynak pas, z=1,10; kafiye kırığı); 5:110 ★★★ (kaynak n, z=5,37)",
 "fâsıla: 5:108 ن (ٱلفسقين) → 5:109 ب (ٱلغيوب) → 5:110 ن (مبين); 5:109 kafiye kırılması (ölçüm bayrağı); 5:110 etken ortaç sıfatla kapanıyor; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1 — basılmış hedefler numarasıyla, basılmamışlar sinifla sayısıyla): 5:109 4:171, 5:104 (emsal olarak basıldı) ve okunmuş 2 ayet; 5:110 2:87, 3:46, 3:49 (emsal olarak basıldı), okunmuş 6 ayet ve henüz okunmamış 1 ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:109 'inne _ 'allâm ğuyûb' süzgeç GEÇER; 5:110 'iz qâle allâh 'îsâ ibn meryem' ve ''îsâ ibn meryem' GEÇER, 'ellezî kefera min' GEÇMEZ",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "fail olmayan mecrur çoğul ad ve mecrur ilgi zamiri A1'de yazılmaz — bölüm 11 denetimi kuralları 16 ve 19; fiilden önce gelen lafız 'mübtedâ' — bölüm 12 denetimi kuralı 11; edilgen fiilde 'naib-i faili' — bölüm 11 denetimi kuralı 17; A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5): "
 "5:109 Allah (lafız; 'yecme'u' faili), 'r-rusule' ('yecme'u' mef'ûlü), 3MS (adsız — 'fe-yeqûlu'), muhatap 2MP (adsız; söz içi — 'ucibtum' naib-i faili), 3MP (adsız — 'qâlû'), konuşan 1P (adsız; söz içi), muhatap 2MS (adsız; söz içi); "
 "5:110 Allah (lafız; 'qâle' faili), 'yâ 'îse' (münadâ; adlı), muhatap 2MS (adsız; söz içi), konuşan 1S (adsız; söz içi), 3FS (adsız; söz içi — 'fîhâ', 'fe-tekûnu'), 3MP (adsız; söz içi — 'ci'tehum', 'keferû', 'minhum'), 'llezîne' ('qâle' faili; söz içi); "
 "'l-ğuyûb' (5:109 15. kelime) ve 'bi'l-beyyinâti' (5:110 54. kelime) — mecrur çoğul — A1'de yazılmadı — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4 — söz yalnız قول fiilinden sonra): 5:109 'fe-yeqûlu' (5.) ardından söz 6-7. kelime, 'qâlû' (8.) ardından söz 9-15. kelime; 5:110 'qâle' (2.) ardından söz 4-63. kelime, söz içinde 'fe-qâle' (55.) ardından iç söz 59-63. kelime; "
 "mealde tırnaksız, iki nokta ile (emsal biçimi — 3:49 emsal mealinde söz iki nokta ile, tırnaksız); A3'te ve A4'te 'söz açılır' / 'söz kapanır'; 'qul' yok (bölüm 10 denetimi kuralı 8); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 109 110 33' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "REM sapması 5:110 (55. kelime) — 'fe-qâle' söz içinde istînâf: Allah'ın anlatısında yeni cümle, meal 'de' ile bağlıyor; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:109 'fe-yeqûlu' (5.) CONJ; 5:110 've 'alâ' (10.), 've kehlen' (20.), 've iz' (21., 27., 43., 47.), 've'l-hikmete' (24.), 've't-tevrâte' (25.), 've'l-incîle' (26.), 've tubri'u' (39.) ve 've'l-ebrasa' (41.) CONJ, 'fe-tenfuxu' (34.) ve 'fe-tekûnu' (36.) CONJ, 'fe-qâle' (55.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 5:109 ◈K يوم ('yevme' 1. kelime — K2; anlam notu: toplanma günü); "
 "5:110 ◈B أنس ('n-nâse' 17. kelime — B1; anlam notu: konuşulan insanlar); 5:110 ◈B طير ('t-tayri' 32., 'tayran' 37. kelime — B1; anlam notu: kuş biçimi ve kuş oluş); 5:110 ◈B خلق ('taxluqu' 28. kelime — B2; anlam notu: çamurdan biçim yaratma, izinle); 5:110 ◈B موت ('l-mevtâ' 45. kelime — B4; anlam notu: ölüleri çıkarma)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 109 110 33'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 2 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:110 (2:87, 3:46, 3:49); 5:109 D3 eşi yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "ayetler arası kalıp yok; ayet içi kalıp 'bi-iznî' (5:110 33., 38., 42. ve 46. kelime — kök أذن ×4); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:109 bölüm açılışı; söz açılır / kapanır (6-7. ve 9-15. kelime); edim geçişi emir → soru; 5:110 söz açılır / kapanır (4-63. kelime); edim geçişi soru → emir, nida",
 "sözdizimi (okuma; morph etiketiyle): 5:109 'yevme yecme'u'llâhu' — zaman zarfı (morph T; amili mahzuf — okuma); 'fe-yeqûlu' — atıf (morph CONJ); 'mâzâ ucibtum' — soru (morph INTG); 'lâ 'ilme lenâ' — cins olumsuzluğu (morph NEG); 'inneke ente' — tekit (morph ACC); "
 "5:110 'iz qâle'llâhu' — zaman (morph T); 'yâ 'îse'bne meryem' — nida (morph VOC); 'zkur ni'metî' — emir (morph IMPV); 've iz' — atıf ve zaman (morph CONJ + T); 'fe-qâle'llezîne' — istînâf (morph REM); 'in hâzâ illâ' — olumsuzluk ve istisna, hasr (morph NEG + RES)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:109 'yevme yecme'u'llâhu'r-rusul' ile açılıyor; 5:109 kök علم ikilemesi (''ilme' 10. / ''allâmu' 14. kelime); "
 "5:110 'iz qâle'llâhu' ile açılıyor; 5:110 kök أذن dörtlemesi ('bi-iznî' 33., 38., 42. ve 46. kelime); 5:110 kök طير ikilemesi ('t-tayri' 32. / 'tayran' 37. kelime)",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 33'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit): 'n-nâse fi'l-mehdi ve kehlen' 5:110 'beşikte ve olgunluk çağında insanlarla' / 3:46 'Beşikte de olgunluk çağında da insanlarla' (emsal metninde) — çakışma değil; "
 "'ke-hey'eti't-tayr' 5:110 'kuş biçiminde' / 3:49 'kuş biçiminde' (emsal metninde) — çakışma değil; 'l-ekmehe ve'l-ebras' 5:110 'doğuştan körü ve alacalıyı' / 3:49 'doğuştan körü ve alacalıyı' (emsal metninde) — çakışma değil; "
 "'bi-rûhi'l-qudus' 5:110 'kutsal ruhla' / 2:87 'kutsal ruhla' (emsal metninde) — çakışma değil",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): 'iz' — çakışma değil (5:110 'Hani' ve '-diğinde' — cümle başı ve zaman yan cümlesi)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 109 110 33'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:109 ve 5:110 tarayıcı vermedi (cipa_tarama5_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: ayet içi 5:110 ('fi'l-mehdi' / 'kehlen') — okuma (yaş evresi); 5:109 yok; ayetler arası yok; eşleme betikle: ADAY_P",
 "aday 1041: kök أذن 5:110 ('bi-iznî' ×4) — izin bağı; kök قول 5:109 ('fe-yeqûlu', 'qâlû') ve 5:110 ('qâle', 'fe-qâle') — söz bağı; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 15-1 (bölüm 7 kuralı 9 — blok_plani_5.txt'ten) — bölüm iki blok (33, 34); bu blok bölümü açıyor; başlıktaki 'Elçilerin toplanması' 5:109, 'İsâ'ya verilen nimetler' 5:110; 'havariler ve sofra' sonraki blokta; "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b33/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 109 110 33'; lem_bozuk.py 33 çıktısı): 5:109:7 'ucîbet', 5:110:39 'tubri'u' — lem_bozuk bayrağı; meal maddesinde '(morph LEM ham biçim)' notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 109 110 → AYN_SONUC; sunum/bolum4_kurallar.py 109 110 33 → KHATA_HEPSI; sunum/bolum5_kurallar.py 109 110 33 → B5_HEPSI; sunum/bolum6_kurallar.py 109 110 33 → B6_HEPSI; sunum/bolum7_kurallar.py 109 110 33 → B7_HEPSI; sunum/bolum8_kurallar.py 109 110 33 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 109 110 33 → B9_HEPSI; sunum/bolum10_kurallar.py 109 110 33 → B10_HEPSI; sunum/bolum11_kurallar.py 109 110 33 → B11_HEPSI; sunum/bolum12_kurallar.py 109 110 33 → B12_HEPSI; sunum/bolum13_kurallar.py 109 110 33 → B13_HEPSI; sunum/bolum14_kurallar.py 109 110 33 → B14_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme: ariza_5_109_110.txt için 3:46 emsal alıntısı 'beşikte de olgunluk çağında da insanlarla' ('de … da' bağlacı — sayma kalıbı değil; bölüm 10 denetimi kuralı 10)",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 33 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('inne', ''allâm', 'ğuyûb', 'iz', 'qâle', 'allâh', ''îsâ', 'ibn', 'meryem', 'ellezî', 'kefera', 'min'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (109, 110): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_109_110.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_5_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('06', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()
GERI = open('/home/claude/yamalar/geriye_donuk_5_b33.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    AYN = (run('/home/claude/sunum/ayn_kontrol.py', '109', '110').splitlines() or ['?'])[-1]
    KUR = run('/home/claude/sunum/bolum4_kurallar.py', '109', '110', '33').splitlines()
    KH = [l for l in KUR if l.startswith('HATA')]
    B5 = run('/home/claude/sunum/bolum5_kurallar.py', '109', '110', '33').splitlines()
    B5H = [l for l in B5 if l.startswith('HATA')]
    B6 = run('/home/claude/sunum/bolum6_kurallar.py', '109', '110', '33', '--tazelik-yok').splitlines()
    B7 = run('/home/claude/sunum/bolum7_kurallar.py', '109', '110', '33').splitlines()
    B8 = run('/home/claude/sunum/bolum8_kurallar.py', '109', '110', '33').splitlines()
    B9 = run('/home/claude/sunum/bolum9_kurallar.py', '109', '110', '33').splitlines()
    B10 = run('/home/claude/sunum/bolum10_kurallar.py', '109', '110', '33').splitlines()
    B11 = run('/home/claude/sunum/bolum11_kurallar.py', '109', '110', '33').splitlines()
    B12 = run('/home/claude/sunum/bolum12_kurallar.py', '109', '110', '33').splitlines()
    B13 = run('/home/claude/sunum/bolum13_kurallar.py', '109', '110', '33').splitlines()
    B14 = run('/home/claude/sunum/bolum14_kurallar.py', '109', '110', '33').splitlines()
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
           'MUT_SONUC': (MUT[-1] if MUT else '?'), 'GERI_P': ' / '.join(x.lstrip('# ') for x in GERI), 'B6_ESMA': ('; '.join(l[5:] for l in B6 if 'esmâ kural' in l and l.startswith('HATA')) or 'sapma 0')}
    I_cur = list(I_HAM)
    for k, v in REP.items(): I_cur = I_cur[:len(BEK)] + [x.replace(k, v) for x in I_cur[len(BEK):]]  # bölüm 9 kuralı 9: taşınan denetim maddelerine yer tutucu değişimi uygulanmaz
    I_cur[idx] = ("karşılık çakışması (bölüm 4 kuralı 4, bölüm 5 kuralı 3, bölüm 6 kuralı 2 — komut 'python3 sunum/cakisma.py' + sûre 5'in okunmuş bütün ARIZA dosyaları; bu bloğun karşılıklarına dokunan gruplar ve son dosyaya dokunan KÖK grupları; grup başına tam bir kapalı karar: 'çakışma değil' ya da 'çakışma — tam okuma sonu'): "
                  + ('; '.join(KARAR.get(l.split(' ←')[0].strip() if not l.startswith('KÖK') else 'KÖK ' + l.split()[1], l + ' — karar yok') for l in CAK_L) if CAK_L else 'bu bloğa dokunan çakışma yok'))
    if I_cur == onceki: break
    onceki = list(I_cur)
yaz(I_cur)
print('yazıldı', len(I_cur), 'tur', tur)
print('\n'.join(CAK_L))
print(GLS); print(KUR); print(B5); print(B6); print(B7); print(B8)

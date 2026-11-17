# blok 31 (5:101-105) ARIZA oluşturucu — bölüm 14-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b31/olcum.txt'
os.environ['SAY2'] = '/home/claude/b31/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b30.txt', encoding='utf-8').read() + ']')
VF_YAZI_ESKI = {33: {6: "'ve rasûlehû'", 7: "'ve yes'avne'", 18: "'ve erculuhum'", 30: "'ve lehum fi'l-âxirati'"}, 34: {9: "'fa'lemû'"}, 35: {6: "'ve'bteğû'", 9: "'ve câhidû'"}, 36: {11: "'ve mislehû'", 22: "'ve lehum 'azâbun'"}}
BOL = "'Soru sormama; bahîra ve sâibe; vasiyet ve şahitlik'"


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
 ("5:101", "'eyy ellezî âmene lâ'", 6, 'say 5:101 1-4', "harekesiz 'yâ eyyuhe'llezîne âmenû lâ' (1-4. kelime)", None),
 ("5:101", "'eyy ellezî âmene'", 16, 'say 5:101 1-3', "harekesiz 'yâ eyyuhe'llezîne âmenû' (1-3. kelime)", None),
 ("5:104", "'mâ enzele allâh'", 2, 'say 5:104 6-8', "harekesiz 'mâ enzele'llâh' (6-8. kelime; biçim öğesi — lemma dizisi 'dizi 5 104 6 8' sûre içi 6, harekesiz kalıp 2)", None),
 ("5:105", "'ilâ allâh merci' cemî' nebbe'e mâ kâne'", 2, 'say 5:105 12-18', "harekesiz 'ile'llâhi merci'ukum cemî'an fe-yunebbi'ukum bi-mâ kuntum' (12-18. kelime)", None),
 ("5:105", "'eyy ellezî âmene'", 16, 'say 5:105 1-3', "harekesiz 'yâ eyyuhe'llezîne âmenû' (1-3. kelime)", None),
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

VF_YAZI = {101: {12: "'ve in'", 23: "'ve'llâhu'"}, 103: {6: "'ve lâ sâ'ibetin'", 8: "'ve lâ vasîletin'", 10: "'ve lâ hâmin'", 12: "'ve lâkinne'", 19: "'ve ekseruhum'"}, 104: {1: "'ve izâ'", 9: "'ve ile'r-rasûli'", 17: "'e-ve-lev'", 23: "'ve lâ'"}, 105: {16: "'fe-yunebbi'ukum'"}}
sys.path.insert(0, '/home/claude/b31/yap')
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
open('/home/claude/b31/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '31')
BLOKLAR = [str(i) for i in range(1, 32)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '31', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b31/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '101', '105', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b31/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b31/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '101', '105', '31').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_101_105.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'5:101', '5:102', '5:103', '5:104', '5:105'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_101_105.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '5:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '5:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(101, 106))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "5:101 kök سوأ ('tesu'kum' 11. kelime — üzme, kötülük): tetik listesinde yok; 5:102 kök قبل ('qablikum' 5. kelime — önce): zaman, tetik listesinde yok; 5:102 kök صبح ('asbahû' 7. kelime — 'ol-'; kök anlamı sabah, zaman anlamında kullanılmıyor): tetik listesinde yok; 5:104 'izâ' (1. kelime — morph T, zaman şartı); 5:105 kök نفس ('enfusekum' 5. kelime — kendi): tetik listesinde yok; 5:105 'izâ' (10. kelime — morph T, zaman); 5:105 kök جمع ('cemî'an' 15. kelime — hep): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '101', '105', '31')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b31/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 32)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b5:%d:\d+' % a_, s_) for a_ in range(101, 106))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bölüm 13 denetiminin araç kuralları — sunum/bolum13_kurallar.py yeni (kurallar 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12; basılmamış xref hedefi numarasız, sayıyla yazılır); "
 "sunum/denetim_5.sh 3. argüman NN verilince bolum13_kurallar kural 2'yi (esma_muhur) hat sonunda koşar (kural 2); sunum/geriye_donuk.py bolum13_kurallar'ı geriye dönük kümeye alır (kural 6 — bölüm 13 kuralları okunmuş bloklara uygulandı); "
 "sunum/gloss_tara.py kesmeli Türkçe karşılığı ('Kur'an') okur — 5:101:17 TARANMAYAN çıkıyordu (kural 5 — bölüm 7 kuralı 5); sunum/mutasyon_sina.py bölüm 13 sınamaları ve gloss_tara sınaması ve kural14 SUB muafiyeti sınamaları (kural 9; 'yok' sağlam kayıt, 'mutp' yama dışı dosya mutasyonu); mutasyon_sina — MUT_SONUC; "
 "blok 29'daki sunum/kural14.py değişikliğinin gerekçesi (bölüm 13 denetimi bulgu 8, kural 9): kural14 kural 4 zamir / ilgi zamiri karşılığındaki yönelme ekini arar, morph SUB 'mâ' (zarfiyye) 'sürece' gibi bağlaçla karşılanır — muafiyet yalnız 'morph SUB' notlu öğede, sağlam ve bozuk kayıtta sınandı; "
 "geriye dönük koşu son araç değişikliğinden sonra yeniden üretildi (GERI_P); yeni 508 — bolum13_kurallar 504 (kural 1: 214, kural 7: 78, kural 5: 71, kural 9: 35, kural 8: 22, kural 2: 21, kural 11: 15, kural 3: 13, kural 12: 13, kural 6: 10, kural 4: 9, kural 10: 3), gloss_tara KAPSAMAYAN 3 (blok 29, 30 ve 31 kayıtları; gloss kapsam sayımı, TARANMAYAN değil), es_edat tanınmayan başlık 1 (blok 31: 'hîne' T, 'lâkinne' ACC — edat_etiket kümesinde yok); "
 "düşen 1 — araç değişti 1; kayıtlar geriye dönük yeniden yazılmadı; hat sırası (bölüm 13 denetimi kuralı 2): esma_el_ekle ve esma_kayit ARIZA üretiminden önce koşuldu",
 "kök tablosu: ölçümde '???' 5:103 için 2 (HAPAKS alanı ve kökler alanı; kök سيب — 7. kelime 'sâ'ibetin') — kök tabloya eklendi (yamalar/yama_kok_5_101.py → kok_ekle_5.py; anlam 'başıboş salıverme (sâ'ibe)'; 1 ayet; docstring dosya adı ve bölümle — bölüm 4 kuralı 16), ölçüm yeniden alındı, '???' 0; 5:101, 5:102, 5:104 ve 5:105 '???' 0; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 101 105 31'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:101 'ğafûrun' (24. kelime) ve 'halîm' (25. kelime) — esma_el 'ilahi', kural ''ve'llâhu X' kuralı'; 5:102, 5:103, 5:104 ve 5:105 esmâ yok; lafız dört ayet (5:101, 5:103, 5:104, 5:105), 5:102 lafız yok; Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 101 105 31'; bölüm 13 denetimi kuralı 2: esma_el eklendikten sonra): " + EMH,
 "ölçüm: 5:101 '{{1|fâsıla حليم → م, N sınıfı}}', '{{1|EDİLGEN 3/8 fiil, pas z=1,81}}', '{{1|simetri \\[6, 2, 10, 2\\]}}', '{{1|harf 106 → harf3 101, isaret 5}}' ve '{{1|dış düğüm 3}}'; "
 "5:102 '{{2|fâsıla كفرين → ن, N sınıfı}}', '{{2|harf 35 → harf3 33, isaret 2}}' ve '{{2|dış düğüm 0}}'; "
 "5:103 '{{3|HAPAKS: سيب}}', '{{3|hapaks z=3,28}}', '{{3|fâsıla يعقلون → ن, N sınıfı}}', '{{3|sayı işareti أَكْثَر}}', '{{3|simetri \\[3, 4, 8, 1\\]}}', '{{3|harf 93 → harf3 85, isaret 8}}' ve '{{3|dış düğüm 0}}'; "
 "5:104 '{{4|fâsıla يهتدون → ن, N sınıfı}}', '{{4|EDİLGEN 1/8 fiil, pas z=0,38}}', '{{4|simetri \\[3, 1, 13, 1\\]}}', '{{4|harf 106 → harf3 102, isaret 4}}', '{{4|dış düğüm 8}}' ve '{{4|İÇ düğüm 1}}'; "
 "5:105 '{{5|fâsıla تعملون → ن, N sınıfı}}', '{{5|simetri \\[3, 2, 6, 1\\]}}', '{{5|harf 90 → harf3 86, isaret 4}}' ve '{{5|dış düğüm 0}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 101 105 31'): KALAN_P",
 "ölçüm aktör: 5:101 '{{1|adlı قُرْءان 17\\. sırada \\(kitab, rol fail\\)}}' — 'yunezzelu' naib-i faili; 5:102, 5:103, 5:104 ve 5:105 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 5:101 yasak, nida, şart — VOC 1 'yâ' (1.), PRO 1 'lâ' (4.), COND 2 'in' (8., 12.); ölçüm biçim alanı '{{1|biçim DIKKAT \\+ NEHY}}' (yalnız bu maddede); "
 "5:102 haber — CERT 1 'qad' (1.); 5:103 haber — NEG 5 'mâ' (1.), 'lâ' (6., 8., 10., 20.); 5:104 soru, emir, şart — COND 1 'lev' (17.), IMPV 1 'te'âlev' (4.), INTG 1 'e' (17.), NEG 2 'lâ' (20., 23.); "
 "5:105 emir, nida — VOC 1 'yâ' (1.), IMPV 1 ''aleykum' (4.; morph NV IMPV), NEG 1 'lâ' (6.); ölçüm biçim alanı '{{5|biçim DIKKAT}}' (yalnız bu maddede); "
 "morph REM ('ve' 5:101 23., 5:103 12., 5:104 1.; 'fe' 5:105 16.), CIRC ('ve' 5:103 19.), SUP ('ve' 5:104 17.) ve T ('hîne' 5:101 15., 'izâ' 5:104 1. ve 5:105 10.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 5:101 ★ (kaynak pas, z=1,81); 5:103 ★★★ (kaynak hapaks, z=3,28); 5:102, 5:104 ve 5:105 yıldız yok",
 "fâsıla: 5:100 ن (تفلحون) → 5:101 م (حليم) → 5:102 ن (كفرين) → 5:103 ن (يعقلون) → 5:104 ن (يهتدون) → 5:105 ن (تعملون); bölüm açılışındaki 5:101 م, ardından dört ayet (5:102, 5:103, 5:104, 5:105) ن (ölçümde kafiye bayrağı yok); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1 — basılmış hedefler numarasıyla, basılmamışlar sinifla sayısıyla): 5:101 2:225 (emsal olarak basıldı), 3:155 (emsal olarak basıldı) ve okunmuş 1 ayet; 5:102 xref yok; 5:103 xref yok; "
 "5:104 2:170 (emsal olarak basıldı), 4:171 (emsal olarak basıldı), okunmuş 6 ayet ve henüz okunmamış 1 ayet (sûre içi 1); 5:105 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:101 'eyy ellezî âmene lâ' ve 'eyy ellezî âmene' süzgeç GEÇER; 5:104 'mâ enzele allâh' GEÇMEZ; 5:105 'ilâ allâh merci' cemî' nebbe'e mâ kâne' ve 'eyy ellezî âmene' GEÇER; 5:102 ve 5:103 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "fail olmayan mecrur çoğul ad ve mecrur ilgi zamiri A1'de yazılmaz — bölüm 11 denetimi kuralları 16 ve 19; fiilden önce gelen lafız 'mübtedâ' — bölüm 12 denetimi kuralı 11; edilgen fiilde 'naib-i faili' — bölüm 11 denetimi kuralı 17; A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5): "
 "5:101 hitap, 3MP (adsız — 'âmenû'), muhatap 2MP (adsız), 3FS (adsız — 'tubde' naib-i faili, 'tesu'kum', ''anhâ'; gönderge 'eşyâ'e'), 'l-qur'ânu' ('yunezzelu' naib-i faili — 3MS fiil uyumu), Allah (lafız; ''afa' faili; 23. kelimede mübtedâ); "
 "5:102 'qavmun' ('se'elehâ' faili — 3MS fiil uyumu), 3FS (adsız — 'se'elehâ' mef'ûlü, 'bihâ'), muhatap 2MP (adsız — 'qablikum'), 3MP (adsız — 'asbahû'); "
 "5:103 Allah (lafız; 'ce'ale' faili — 3MS fiil uyumu; 17. kelimede mecrur), 'llezîne keferû' ('lâkinne' ismi), 3MP (adsız — 'keferû', 'yefterûne', 'ekseruhum', 'ya'qilûn'); "
 "5:104 'qîle' (3MS fiil uyumu; edilgen; naib-i faili söz), 3MP (adsız — 'lehum', 'qâlû', 'âbâ'uhum', 'ya'lemûne', 'yehtedûn'), muhatap 2MP (adsız; söz içi — 'te'âlev'), Allah (lafız; 'enzele' faili), elçi ('r-rasûli' — adlı rol), konuşan 1P (adsız; söz içi — 'hasbunâ', 'vecednâ', 'âbâ'enâ'), 3MS (adsız; söz içi — ''aleyhi'); "
 "5:105 hitap, 3MP (adsız — 'âmenû'), muhatap 2MP (adsız), 'men dalle' ('yadurrukum' faili — 3MS fiil uyumu), Allah (lafız; 13. kelimede haber), 3MS (adsız — 'dalle', 'fe-yunebbi'ukum'); "
 "'eşyâ'e' (5:101 7. kelime; mecrur çoğul) ve 'mâ' (5:104 6. kelime; mecrur ilgi zamiri) A1'de yazılmadı — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): 5:104 iki söz — 'qîle' sözü (4-10. kelime) ve 'qâlû' sözü (12-16. kelime) — mealde tırnaksız, iki nokta ile (emsal biçimi); A3'te ve A4'te 'söz açılır' / 'söz kapanır'; 5:101, 5:102, 5:103 ve 5:105 söz yok (A3 —); 'qul' yok (bölüm 10 denetimi kuralı 8); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 101 105 31' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:101 've in' (12.) CONJ, 've'llâhu' (23.) REM; 5:103 've lâ' (6., 8., 10.) CONJ, 've lâkinne' (12.) REM, 've ekseruhum' (19.) CIRC; "
 "5:104 've izâ' (1.) REM, 've ile'r-rasûli' (9.) CONJ, 'e-ve-lev' (17.) SUP, 've lâ' (23.) CONJ; 5:105 'fe-yunebbi'ukum' (16.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 5:101 ◈K حين ('hîne' 15. kelime — K2; anlam notu: Kur'an'ın indiriliş vakti); 5:103 ◈K بحر ('bahîratin' 5. kelime — K1; anlam notu: kök anlamı deniz, 'bahîra' adanmış hayvan adı — deniz anlamında kullanılmıyor)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 101 105 31'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:101 (3:155), 5:104 (2:170); 5:102, 5:103 ve 5:105 D3 eşi yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; 5:101 bağı ölçüm xref adıyla); "
 "ayetler arası kalıp 'yâ eyyuhe'llezîne âmenû' (5:101, 5:105) — sayım 'say 5:101 1-3' ve lemma dizisi 'dizi 5 101 1 3' / 'dizi 5 105 1 3'; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:101 bölüm açılışı (bölüm 10 denetimi kuralı 2); hitap açılır; edim geçişi emir, nida, şart → yasak, nida, şart; şart → cevap ('in' 8. ve 12. kelime); 5:102 edim geçişi yasak, nida, şart → haber; şahıs geçişi 2 → 3; "
 "5:103 geçiş yok; 5:104 söz açılır / kapanır (4-10. ve 12-16. kelime); edim geçişi haber → soru, emir, şart; şart → cevap ('lev' 17. kelime — cevap mahzuf); 5:105 hitap açılır; edim geçişi soru, emir, şart → emir, nida; şahıs geçişi 3 → 2",
 "sözdizimi (okuma; morph etiketiyle): 5:101 'lâ tes'elû' — yasak (morph PRO); 'in tubde lekum tesu'kum' — şart ve cevap (morph COND); 'hîne yunezzelu'l-qur'ânu' — zaman (morph T) ve edilgen (morph PASS); 've'llâhu ğafûrun halîm' — istînâf (morph REM); "
 "5:102 'qad se'elehâ' — kesinlik (morph CERT); 'summe' — sıralı atıf (morph CONJ); 5:103 'mâ ce'ale'llâhu min bahîratin' — olumsuz ve istiğrak (morph NEG + P); 've lâkinne'llezîne' — istidrâk (morph REM + ACC); 've ekseruhum lâ ya'qilûn' — hâl (morph CIRC); "
 "5:104 've izâ qîle lehum' — istînâf, zaman şartı ve edilgen (morph REM + T + PASS); 'te'âlev' — emir (morph IMPV); 'e-ve-lev kâne' — soru ve şart (morph SUP + INTG + COND); "
 "5:105 ''aleykum enfusekum' — ism-i fiil emri (morph NV IMPV); 'izâ'htedeytum' — zaman (morph T); 'fe-yunebbi'ukum' — istînâf (morph REM)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:101 ve 5:105 'yâ eyyuhe'llezîne âmenû' ile açılıyor; "
 "5:101 kök سأل ikilemesi ('tes'elû' 5. / 13. kelime) ve kök بدو ikilemesi ('tubde' 9. / 18. kelime); 5:104 kök أبو ikilemesi ('âbâ'enâ' 16. / 'âbâ'uhum' 19. kelime) ve kök قول ikilemesi ('qîle' 2. / 'qâlû' 11. kelime); "
 "5:103 dört hayvan adı ('bahîratin', 'sâ'ibetin', 'vasîletin', 'hâmin') bir 'mâ … min' olumsuzu altında",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 31'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit): ''afa'llâhu 'anhâ' 5:101 'Allah onları affetti' / 3:155 'Allah onları affetti' (emsal metninde) — çakışma değil; "
 "'ğafûrun halîm' 5:101 'bağışlayandır, halîmdir' / 3:155 'bağışlayandır, halîmdir' (emsal metninde) — çakışma değil; "
 "''aleyhi âbâ'enâ' 5:104 'Atalarımızı üzerinde bulduğumuz' / 2:170 'atalarımızı üzerinde bulduğumuz' (emsal metninde) — çakışma değil; "
 "'e-ve-lev kâne âbâ'uhum' 5:104 'Ataları bir şey bilmeyen ve doğru yolu bulamayan kimseler olsa da mı' / 2:170 'Ataları hiçbir şeye akıl erdirmiyor ve doğru yolu bulamıyor olsalar da mı' (emsal metninde) — çakışma — tam okuma sonu",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 101 105 31'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:101, 5:102, 5:103, 5:104 ve 5:105 tarayıcı vermedi (cipa_tarama5_adaylari.json); doğa iddiası yok (olgu=False); L3 / L4 adayı yok",
 "aday 1039: ayet içi 5:105 ('dalle' / 'htedeytum') — okuma; 5:101, 5:102, 5:103 ve 5:104 ayet içi karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök سأل 5:101'de ('tes'elû' 5. ve 13.) ve 5:102'de ('se'elehâ' 2.) — sorma yasağı ve önceki kavmin sorması; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 14-1 (bölüm 7 kuralı 9 — blok_plani_5.txt'ten) — bölüm iki blok (31, 32); bu blok bölümü açıyor; başlıktaki 'Soru sormama' 5:101-102, 'bahîra ve sâibe' 5:103; 'vasiyet ve şahitlik' sonraki blokta; "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b31/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 101 105 31'; lem_bozuk.py 31 çıktısı): 5:103:21 ''aqalu', 5:105:7 'yadurre' — lem_bozuk bayrağı; meal maddesinde '(morph LEM ham biçim)' notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 101 105 → AYN_SONUC; sunum/bolum4_kurallar.py 101 105 31 → KHATA_HEPSI; sunum/bolum5_kurallar.py 101 105 31 → B5_HEPSI; sunum/bolum6_kurallar.py 101 105 31 → B6_HEPSI; sunum/bolum7_kurallar.py 101 105 31 → B7_HEPSI; sunum/bolum8_kurallar.py 101 105 31 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 101 105 31 → B9_HEPSI; sunum/bolum10_kurallar.py 101 105 31 → B10_HEPSI; sunum/bolum11_kurallar.py 101 105 31 → B11_HEPSI; sunum/bolum12_kurallar.py 101 105 31 → B12_HEPSI; sunum/bolum13_kurallar.py 101 105 31 → B13_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 31 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('eyy', 'ellezî', 'âmene', 'lâ', 'mâ', 'enzele', 'allâh', 'ilâ', 'merci'', 'cemî'', 'nebbe'e', 'kâne', 'ğafûr', 'halîm'); 'vaṣîle' adı ص için 'ṣ' ile — okunmuş 'vesîle' (س) ayrı lemma; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; 'e-ve-lev' (5:104 17. kelime) bir kelime, tire ile; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (101, 105): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_101_105.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_5_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('06', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()
GERI = open('/home/claude/yamalar/geriye_donuk_5_b31.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    AYN = (run('/home/claude/sunum/ayn_kontrol.py', '101', '105').splitlines() or ['?'])[-1]
    KUR = run('/home/claude/sunum/bolum4_kurallar.py', '101', '105', '31').splitlines()
    KH = [l for l in KUR if l.startswith('HATA')]
    B5 = run('/home/claude/sunum/bolum5_kurallar.py', '101', '105', '31').splitlines()
    B5H = [l for l in B5 if l.startswith('HATA')]
    B6 = run('/home/claude/sunum/bolum6_kurallar.py', '101', '105', '31', '--tazelik-yok').splitlines()
    B7 = run('/home/claude/sunum/bolum7_kurallar.py', '101', '105', '31').splitlines()
    B8 = run('/home/claude/sunum/bolum8_kurallar.py', '101', '105', '31').splitlines()
    B9 = run('/home/claude/sunum/bolum9_kurallar.py', '101', '105', '31').splitlines()
    B10 = run('/home/claude/sunum/bolum10_kurallar.py', '101', '105', '31').splitlines()
    B11 = run('/home/claude/sunum/bolum11_kurallar.py', '101', '105', '31').splitlines()
    B12 = run('/home/claude/sunum/bolum12_kurallar.py', '101', '105', '31').splitlines()
    B13 = run('/home/claude/sunum/bolum13_kurallar.py', '101', '105', '31').splitlines()
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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

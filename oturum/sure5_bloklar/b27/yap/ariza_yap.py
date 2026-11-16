# blok 27 (5:87-89) ARIZA oluşturucu — bölüm 12-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b27/olcum.txt'
os.environ['SAY2'] = '/home/claude/b27/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b26.txt', encoding='utf-8').read() + ']')
VF_YAZI_ESKI = {33: {6: "'ve rasûlehû'", 7: "'ve yes'avne'", 18: "'ve erculuhum'", 30: "'ve lehum fi'l-âxirati'"}, 34: {9: "'fa'lemû'"}, 35: {6: "'ve'bteğû'", 9: "'ve câhidû'"}, 36: {11: "'ve mislehû'", 22: "'ve lehum 'azâbun'"}}
BOL = "'Helalleri haram kılmama; yemin keffareti; içki ve kumar'"


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
 ("5:87", "'eyy ellezî âmene lâ'", 6, 'say 5:87 1-4', "harekesiz 'yâ eyyuhe'llezîne âmenû lâ' (1-4. kelime)", None),
 ("5:87", "'eyy ellezî âmene'", 16, 'say 5:87 1-3', "harekesiz 'yâ eyyuhe'llezîne âmenû' (1-3. kelime)", None),
 ("5:87", "'inne allâh lâ'", 3, 'say 5:87 13-15', "harekesiz 'inne'llâhe lâ' (13-15. kelime)", None),
 ("5:87", "'allâh lâ ahbeb' (LEM 'ahbeb' (morph LEM ham biçim))", 2, 'say 5:87 14-16', "harekesiz 'llâhe lâ yuhibbu' (14-16. kelime)", ('dizi 5 87 14 16', "allâh lâ ahbeb", '14-16', "biçim farkı (dizi 5 87 14 16): basılmamış eş i'râb, önek")),
 ("5:88", "'ittaqâ allâh ellezî'", 2, 'say 5:88 7-9 --on', "önek kesilmiş 've'ttequ'llâhe'llezî' (7-9. kelime)", None),
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

VF_YAZI = {87: {11: "'ve lâ'"}, 88: {1: "'ve kulû'", 7: "'ve'ttequ'"}, 89: {7: "'ve lâkin'", 12: "'fe-keffâratuhû'", 26: "'fe-men'", 29: "'fe-siyâmu'", 37: "'ve'hfezû'"}}
sys.path.insert(0, '/home/claude/b27/yap')
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
open('/home/claude/b27/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '27')
BLOKLAR = [str(i) for i in range(1, 28)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '27', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b27/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '87', '89', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b27/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b27/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '87', '89', '27').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_87_89.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'5:87', '5:88', '5:89'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_87_89.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '5:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '5:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(87, 90))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "5:89 'izâ' ('izâ haleftum' 35. kelime — morph T, zaman); 5:89 kök يمن ('eymânikum' 6. kelime — yemin; kök anlamı 'sağ el', organ anlamında kullanılmıyor): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '87', '89', '27')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b27/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 28)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b5:%d:\d+' % a_, s_) for a_ in range(87, 90))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bölüm 11 denetiminin araç kuralları — sunum/bolum11_kurallar.py yeni (kurallar 1, 2, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17); "
 "sunum/bolum9_kurallar.py kural 5 'tür tam' nakarat3 kalıplarını da kapsar (kural 3); sunum/bolum10_kurallar.py kural 6 sayıyı yalnız ◇ 'Ölçüm xref' cümlesinde arar, k=0 iken '(sûre içi 0)' istemez (kural 4), kural 3 kapalı sözlük yalnız 'çakışma değil' / 'çakışma — tam okuma sonu' (kural 8; önceki blokların kararları yön karşılaştırmasında eski sözlükle okunur); "
 "sunum/lem_bozuk.py PASS etiketsiz fiilde edilgen biçimli LEM'i bayraklar (kural 5), sunum/ham_elle.txt'ten 'udxile' satırı çıkarıldı (araç bayraklıyor); sunum/medde_fark.py yeni — medde satırı sinifla sınıflarıyla (kural 6; ARIZA aynen taşır); sunum/geriye_donuk.py bolum11_kurallar ve 'basılan değişti' düşüş sınıfı (kural 18); "
 "sunum/mutasyon_sina.py bölüm 11 sınamaları (kural 18 hariç: geriye dönük koşunun kendisi sınama gerektirmeyecek kadar uzun, düşüş sınıfı geriye dönük dosyada görünür); mutasyon_sina — MUT_SONUC; geriye dönük koşu son araç değişikliğinden sonra yeniden üretildi (GERI_P); "
 "yeni 126 — bolum10_kurallar 71 (kural 3: 38 — okunmuş bloklarda 'bilinçli fark' / '— tam okuma sonu' yazımlı eski kararlar; kural 6: 33 — eski ◇'lerde xref sayısı 'Ölçüm xref' cümlesinde değil), bolum11_kurallar 54 (kurallar 1, 2, 6, 7, 9-17 okunmuş bloklardaki eski kayıtlara uygulandı; kurallar o bloklarda yoktu), bolum9_kurallar 1 (kural 3: 5:86 'tür tam' R5 satırı); düşen 13 — araç değişti; kayıtlar geriye dönük yeniden yazılmadı",
 "kök tablosu: ölçümde '???' 5:87, 5:88 ve 5:89 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 87 89 27'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:88 'mu'minûn' (12. kelime) — esma_el 'degil', kural 'çoğul insan göndergeli' (inananlar); 5:87 ve 5:89 esmâ yok; lafız 5:87, 5:88 ve 5:89'da; Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); "
 "gönderge 'entum' (muhatap 2MP) — A1'de 'mu'minûn' 'entum' haberi olarak yazıldı (bölüm 11 denetimi kuralı 7: A1'de anılan kural esma_el ile eş)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 87 89 27'): " + EMH,
 "ölçüm: 5:87 '{{1|fâsıla ٱلمعتدين → ن, N sınıfı}}', '{{1|simetri \\[3, 2, 11, 1\\]}}', '{{1|harf 72 → harf3 68, isaret 4}}' ve '{{1|dış düğüm 2}}'; "
 "5:88 '{{2|fâsıla مؤمنون → ن, N sınıfı}}', '{{2|harf 57 → harf3 51, isaret 6}}' ve '{{2|dış düğüm 4}}'; "
 "5:89 '{{3|fâsıla تشكرون → ن, N sınıfı}}', '{{3|sayı işareti عَشَرَة, ثَلاثَة}}', '{{3|simetri \\[3, 1, 7, 1\\]}}', '{{3|harf 207 → harf3 197, isaret 10}}' ve '{{3|dış düğüm 2}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 87 89 27'): KALAN_P",
 "ölçüm aktör: 5:87, 5:88 ve 5:89 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 5:87 yasak, nida — VOC 1 'yâ' (1.), PRO 2 'lâ' (4., 11.), NEG 1 'lâ' (15.); ölçüm biçim alanı '{{1|biçim DIKKAT \\+ NEHY}}' (yalnız bu maddede); "
 "5:88 emir — IMPV 2 'kulû' (1.), 'ttequ' (7.); 5:89 emir, şart — COND 1 'men' (26.), IMPV 1 'hfezû' (37.), NEG 2 'lâ' (1.), 'lem' (27.); ölçüm biçim alanı '{{3|biçim QASEM}}' (yalnız bu maddede; ayette kasem edatı yok, araç 'eymân' / 'haleftum' kökünü biçim sayıyor — araç tanımı farkı, okuma); "
 "morph REM ('ve' 5:88 1.; 've lâkin' 5:89 7.; 'fe' 5:89 12. ve 26.; 've' 5:89 37.), RSLT ('fe' 5:89 29.) ve AMD ('lâkin' 5:89 7.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 5:87 ★ (kaynak allah, z=1,82); 5:88 ★★ (kaynak allah, z=2,80); 5:89 ★★★ (kaynak n, z=3,46)",
 "fâsıla: 5:86 م (ٱلجحيم) → 5:87 ن (ٱلمعتدين) → 5:88 ن (مؤمنون) → 5:89 ن (تشكرون); bölüm açılışında kafiye ن'ye dönüyor; blok içi kafiye değişmiyor; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6 — basılmamış hedefler sinifla sayısıyla): 5:87 2:190 (emsal olarak basıldı) ve okunmuş 1 ayet; 5:88 16:114 ve 60:11 (emsal olarak basıldı) ve okunmamış 2 ayet; 5:89 2:196 ve 2:225 (emsal olarak basıldı)",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:87 'eyy ellezî âmene lâ', 'eyy ellezî âmene' ve 'inne allâh lâ' süzgeç GEÇER, 'allâh lâ ahbeb' GEÇMEZ; 5:88 'ittaqâ allâh ellezî' GEÇMEZ; 5:89 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap' ile; alıntı ve kelime numarası ◇ konumuyla eş; fail olmayan mecrur çoğul ad A1'de yazılmaz — bölüm 11 denetimi kuralı 19, kullanıcı kararı bekleniyor): "
 "5:87 hitap ('yâ eyyuhe'llezîne âmenû'), 3MP (adsız — 'âmenû'), muhatap 2MP (adsız), Allah (lafız; 'ehalle' faili — 3MS fiil uyumu; 'inne' ismi), 3MS (adsız — 'yuhibbu'), 'l-mu'tedîn' ('yuhibbu' mef'ûlü); "
 "5:88 muhatap 2MP (adsız), Allah (lafız; 'razaqa' faili — 3MS fiil uyumu; 'ttequ' mef'ûlü), 3MS (adsız — 'bihî'), 'mu'minûn' ('entum' haberi; esmâ göndergesi); "
 "5:89 Allah (lafız; 'yu'âxizu' ve 'yubeyyinu' faili — 3MS fiil uyumu), muhatap 2MP (adsız), 3MS (adsız — 'yu'âxizukum', 'keffâratuhû', 'yecid', 'âyâtihî'), 3MP (adsız — 'kisvetuhum'), 'men' (şart ismi), 'ehlîkum' ('tut'imûne' mef'ûlü); "
 "'mesâkîne' (mecrur nekre çoğul; ''aşerati' muzâfun ileyhi) A1'de yazılmadı — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): bu blokta söz yok (A3 —); 'qul' yok (bölüm 10 denetimi kuralı 8); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 87 89 27' — A3 aralığında morph REM): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:87 've lâ' (11.) CONJ; 5:88 've kulû' (1.) REM, 've'ttequ' (7.) CONJ; 5:89 've lâkin' (7.), 'fe-keffâratuhû' (12.), 'fe-men' (26.), 've'hfezû' (37.) REM, 'fe-siyâmu' (29.) RSLT",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 5:89 ◈K يوم ('eyyâmin' 31. kelime — K2; anlam notu: oruç tutulan üç gün); 5:87 ve 5:88 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 87 89 27'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:87 (2:190), 5:88 (16:114, 60:11), 5:89 (2:225, 2:196) (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:87 bölüm açılışı (bölüm 10 denetimi kuralı 2); hitap açılır; edim geçişi haber → yasak, nida; şahıs geçişi 3 → 2; 5:88 edim geçişi yasak, nida → emir; 5:89 edim geçişi emir → emir, şart; şart → cevap ('men' 26. kelime)",
 "sözdizimi (okuma; morph etiketiyle): 5:87 'yâ eyyuhe'llezîne âmenû' — nida (morph VOC); 'lâ tuharrimû' ve 'lâ ta'tedû' — yasak (morph PRO); 'mâ ehalle'llâhu lekum' — 'tayyibât' sıfatı mevsûl; 'inne'llâhe lâ yuhibbu' — tekit ve olumsuzluk (morph ACC + NEG); "
 "5:88 'kulû mimmâ razaqakumu'llâhu halâlen tayyiben' — emir; 'halâlen tayyiben' mansub nekre (morph ACC); 'llezî entum bihî mu'minûn' — lafzın sıfatı mevsûl, isim cümlesi; "
 "5:89 'lâ yu'âxizukumu'llâhu … lâkin yu'âxizukum' — olumsuz / olumlu karşıtlık (morph NEG + AMD); 'bi-mâ 'aqqadtumu' — 'mâ' masdar; 'keffâratuhû it'âmu … ev kisvetuhum ev tahrîru raqabetin' — mübteda ve 'ev' ile seçenekli haber (morph CONJ); "
 "'men lem yecid' — şart (morph COND + NEG), 'siyâmu selâseti eyyâmin' — cevap (morph RSLT önekli); 'izâ haleftum' — zaman (morph T); 'hfezû eymânekum' — emir (morph IMPV); 'kezâlike yubeyyinu'llâhu' — teşbih edatı (morph P 'ke')",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:87 'yâ eyyuhe'llezîne âmenû' ile açılıyor; kök عدو ikilemesi 'ta'tedû' / 'l-mu'tedîn' (12., 17. kelime); "
 "5:87 'tayyibâti' ve 5:88 'tayyiben' (6. kelime) — kök طيب; 5:87 'ehalle' ve 5:88 'halâlen' — kök حلل; 5:89 kök يمن dört kelimede ('eymânikum' 6. ve 34., 'l-eymâne' 11., 'eymânekum' 38. kelime)",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 27'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp): 'lâ ta'tedû inne'llâhe lâ yuhibbu'l-mu'tedîn' 5:87 / 2:190 'sınırı aşmayın. Şüphesiz Allah sınırı aşanları sevmez' (emsal metninde) — çakışma değil; "
 "'mimmâ razaqakumu'llâhu halâlen tayyiben' 5:88 / 16:114 'Allah'ın size rızık olarak verdiği helâl ve temiz şeylerden' (emsal metninde) — çakışma değil; 've'ttequ'llâhe'llezî entum bihî mu'minûn' 5:88 'İnandığınız Allah'tan sakının' / 60:11 'İnandığınız Allah'a karşı sakının' — yönelme / ayrılma eki farkı, çakışma değil; "
 "'lâ yu'âxizukumu'llâhu bi'l-lağvi fî eymânikum' 5:89 / 2:225 (emsal metninde) — meal birebir, çakışma değil; 'fe-men lem yecid fe-siyâmu selâseti eyyâmin' 5:89 'Kim bulamazsa, üç gün oruç tutmak gerekir' / 2:196 'Bulamayan … üç gün … oruç tutar' — cümle yapısı farkı, çakışma değil; "
 "'raqabe' karşılığı 'köle' (kök رقب tablo anlamı 'gözetme, kollama'; mecaz — 'boyun'; gloss taraması listesinde)",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 87 89 27'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:87, 5:88 ve 5:89 tarayıcı vermedi (cipa_tarama5_adaylari.json); doğa iddiası yok (olgu=False); L3 / L4 adayı yok",
 "aday 1039: ayet içi 5:87 ('tuharrimû' / 'ehalle'), 5:89 ('lâ yu'âxizukumu'llâhu bi'l-lağvi' / 'yu'âxizukum bi-mâ 'aqqadtumu'l-eymâne') — okuma; ayetler arası 5:87 / 5:88 ('lâ tuharrimû tayyibâti' / 'halâlen tayyiben'); 5:88 ayet içi karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök حلل 5:87 'ehalle' ve 5:88 'halâlen' — helâl kılma / helâl rızık; kök يمن 5:89'da dört kelimede — boş yemin, bağlanan yemin, keffaret, koruma; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 12-1 (bölüm 7 kuralı 9 — blok_plani_5.txt'ten) — bölüm iki blok (27, 28); bu blok bölümü açıyor; başlıktaki 'Helalleri haram kılmama' 5:87, 'yemin keffareti' 5:89; 'içki ve kumar' sonraki blokta; "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b27/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 87 89 27'; lem_bozuk.py 27 çıktısı): 5:87:16 'ahbeb', 5:89:2 'yu'âxizu', 5:89:36 'halef', 5:89:40 'beyyenu' — lem_bozuk bayrağı; meal maddesinde '(morph LEM ham biçim)' notlu; lemma adı listesinde notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 87 89 → AYN_SONUC; sunum/bolum4_kurallar.py 87 89 27 → KHATA_HEPSI; sunum/bolum5_kurallar.py 87 89 27 → B5_HEPSI; sunum/bolum6_kurallar.py 87 89 27 → B6_HEPSI; sunum/bolum7_kurallar.py 87 89 27 → B7_HEPSI; sunum/bolum8_kurallar.py 87 89 27 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 87 89 27 → B9_HEPSI; sunum/bolum10_kurallar.py 87 89 27 → B10_HEPSI; sunum/bolum11_kurallar.py 87 89 27 → B11_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 27 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('eyy', 'ellezî', 'âmene', 'lâ', 'inne', 'allâh', 'ahbeb' (morph LEM ham biçim), 'ittaqâ'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (87, 89): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_87_89.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_5_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('06', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()
GERI = open('/home/claude/yamalar/geriye_donuk_5_b27.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    AYN = (run('/home/claude/sunum/ayn_kontrol.py', '87', '89').splitlines() or ['?'])[-1]
    KUR = run('/home/claude/sunum/bolum4_kurallar.py', '87', '89', '27').splitlines()
    KH = [l for l in KUR if l.startswith('HATA')]
    B5 = run('/home/claude/sunum/bolum5_kurallar.py', '87', '89', '27').splitlines()
    B5H = [l for l in B5 if l.startswith('HATA')]
    B6 = run('/home/claude/sunum/bolum6_kurallar.py', '87', '89', '27', '--tazelik-yok').splitlines()
    B7 = run('/home/claude/sunum/bolum7_kurallar.py', '87', '89', '27').splitlines()
    B8 = run('/home/claude/sunum/bolum8_kurallar.py', '87', '89', '27').splitlines()
    B9 = run('/home/claude/sunum/bolum9_kurallar.py', '87', '89', '27').splitlines()
    B10 = run('/home/claude/sunum/bolum10_kurallar.py', '87', '89', '27').splitlines()
    B11 = run('/home/claude/sunum/bolum11_kurallar.py', '87', '89', '27').splitlines()
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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

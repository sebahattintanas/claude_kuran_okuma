# sûre 6 blok 24 (6:100-103) ARIZA oluşturucu — bölüm 12-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b24/olcum.txt'
os.environ['SAY2'] = '/home/claude/b24/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {}
BOL = "'Taneyi ve çekirdeği yaran; gözler O'nu idrak etmez'"


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
 ("6:102", "'rabb lâ ilâh illâ _'", 2, 'say 6:102 3-7', "harekesiz 'rabbukum lâ ilâhe illâ huve' (3-7. kelime)", ('dizi 6 102 3 7', "rabb lâ ilâh illâ _", '3-7', "biçim farkı (dizi 6 102 3 7): basılmamış eş i'râb, zamir eki")),
 ("6:102", "''alâ kull şey''", 2, 'say 6:102 13-15', "harekesiz ''alâ kulli şey'in' (13-15. kelime); biçim öğesi ''alâ' zamir eki (lemma dizisi sûre içi 3, nakarat3 2)", None),
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

K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k and not (k + ' --medde' in sayim.S2 and sayim.S2[k + ' --medde'][0] != n)}  # sûre 6 bölüm 5 denetimi kuralı 6 (TEKIL_MEDDE)

VF_YAZI = {100: {1: "'ve ce'alû'", 5: "'ve xalaqahum'", 6: "'ve xaraqû'", 9: "'ve benâtin'", 13: "'ve te'âlâ'"}, 101: {3: "'ve'l-ardi'", 8: "'ve lem'", 12: "'ve xalaqa'", 15: "'ve huve'"}, 102: {12: "'ve huve'"}, 103: {4: "'ve huve'", 7: "'ve huve'"}}
sys.path.insert(0, '/home/claude/b24/yap')
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
open('/home/claude/b24/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '24')
BLOKLAR = [str(i) for i in range(1, 25)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '24', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b24/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '100', '103', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b24/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b24/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '100', '103', '24').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_100_103.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:100', '6:101', '6:102', '6:103'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_100_103.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(100, 104))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '100', '103', '24')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b24/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 25)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(100, 104))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: blok 23 sonrası 6:96 kullanıcı kararı ('ilahi') — sunum/bolum6_kurallar.py kuralı 14 (bölüm 8 kuralı 2) kapalı listesine ve KW sözlüğüne 'tamlama içinde ad' eklendi (esma_el.py emsali 36:38:7-8); sunum/mutasyon_sina.py blok 23 olumlu ve isabetsiz sınamaları ('mutyok' yardımcısı); 6:96 kaydı yamalar/esma_el_6_96_karar.txt; bu blokta sunum/bolum10_kurallar.py kuralı 1 (eş kurallı esma_el kayıtları ayrı parantez taşıyabilir — her kaydın parantezi esmâ maddesindeki anışlardan biriyle bayt eşit; 6:103:9 morph ADJ 'sıfat' gereği) ve sunum/bolum19_kurallar.py kuralı 5 ('degil' esmâ dışı gönderge / 'ilahi' çerçeve etiketi karar ayrılığı, esmâ maddesi önceki 'degil' kaydını anıyorsa geçer — وَكِيل 6:66:9 / 6:102:16) değişti; mutasyon_sina b10 kural 1 ve b19 kural 5 olumlu + isabetsiz sınamaları; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 242",
 "geriye dönük koşu (bu blokta araç değişti — komut 'python3 sunum/geriye_donuk.py b24 yamalar/geriye_donuk_6_b23k.txt'): GERI_P; yeni yalnız blok 24 satırları (gloss KAPSAMAYAN — tam okuma sonu; kelime_kontrol ZAMİR KAYITSIZ), düşen 0; önceki koşu (6:96 kullanıcı kararı sonrası, komut 'python3 sunum/geriye_donuk.py b23k yamalar/geriye_donuk_6_b23k.txt') yeni sınıflar: basılan değişti (6:63 xref — 27:63 ve 6:97 sonradan basıldı), kayıt değişti (blok 23 esma_kayit maddesi — 6:96 e_el=? 0 oldu; عَلِيم kural etiketleri 'zamirin haberi' / ''inne/enne' haberi' / 'tamlama içinde ad' — tam okuma sonu); düşen yok; kayıt geriye yazılmadı",
 "kullanıcı kararı (6:96, 2026-11-22): 'zâlike taqdîru'l-'azîzi'l-'alîm' (9-12. kelime) — 'ilahi' (tamlama içinde ad, göndergesi Allah; emsal 36:38:7-8); blok 23 ARIZA'sındaki 'kullanıcı kararı (tam okuma sonu)' kaydı kapandı; esma_kayit 6:96 e_el=1",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 100 103 24'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:101 'bedî'u's-semâvâti ve'l-ard' (1-3. kelime) ve 've huve bi-kulli şey'in 'alîm' (15-18. kelime) — esma_el 'ilahi', kural 'zamirin haberi' (Allah); 6:102 'zâlikumu'llâhu rabbukum lâ ilâhe illâ huve xâliqu kulli şey'in' (1-10. kelime) — esma_el 'ilahi', kural 'lafzın haberi' (Allah); 've huve 'alâ kulli şey'in vekîl' (12-16. kelime) — esma_el 'ilahi', kural 'zamirin haberi' (Allah) — وَكِيل lemmasında 6:66:9 'degil' kaydıyla karar ayrılığı: gönderge ayrılığı (6:66'da elçi, esmâ dışı gönderge; burada Allah); 6:103 've huve'l-latîfu'l-xabîr' (7-9. kelime) — esma_el 'ilahi', 'l-latîf' kural 'zamirin haberi' (Allah), 'l-xabîr' kural 'zamirin haberi' (Allah; 'l-latîf'in sıfatı) (yamalar/esma_el_6_100_103.txt); 6:100 esmâ yok; "
 "6:100 lafız (2. kelime), 6:102 lafız (2. kelime) ve Rab (3. kelime); 6:101 ve 6:103 lafız yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 100 103 24'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: 6:100 '{{1|fâsıla يصفون → ن, N sınıfı}}', '{{1|harf 73 → harf3 65, isaret 8}}' ve '{{1|dış düğüm 2}}'; "
 "6:101 '{{2|fâsıla عليم → م, N sınıfı}}', '{{2|simetri \\[4, 4, 8, 1\\]}}', '{{2|harf 71 → harf3 62, isaret 9}}' ve '{{2|dış düğüm 6}}'; "
 "6:102 '{{3|fâsıla وكيل → ل, ل sınıfı}}', '{{3|simetri \\[4, 7, 12, 1\\]}}', '{{3|harf 58 → harf3 52, isaret 6}}' ve '{{3|dış düğüm 2}}'; "
 "6:103 '{{4|fâsıla ٱلخبير → ر, R sınıfı}}', '{{4|simetri \\[3, 3, 6, 1\\]}}', '{{4|harf 42 → harf3 41, isaret 1}}' ve '{{4|dış düğüm 0}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 100 103 24'): KALAN_P",
 "ölçüm aktör: 6:100, 6:101, 6:102 ve 6:103 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:100 haber — kip yok; 6:101 soru — INTG 1 'ennâ' (4.), NEG 1 've lem' (8.); "
 "6:102 emir — IMPV 1 'fa'budûhu' (11.), NEG 1 'lâ' (4.), biçim ISTISNA ('illâ' 6.); 6:103 haber — NEG 1 'lâ' (1.); "
 "morph CIRC ('ve' 6:100 5.), REM ('ve' 6:101 12., 15.; 'fe' 6:102 11.; 've' 6:103 4., 7.), EXP ('illâ' 6:102 6.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:100, 6:101, 6:102 ve 6:103 yıldız yok",
 "fâsıla: 6:99 ن → 6:100 ن (يصفون) → 6:101 م (عليم) → 6:102 ل (وكيل) → 6:103 ر (ٱلخبير) — N, ل ve R sınıfları (ölçüm); 6:101-103 ardışık harf değişimi; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:100 okunmuş 2 ayet; 6:101 2:117 ve 39:62 (emsal olarak basıldı) ve okunmuş 4 ayet; 6:102 39:62 (emsal olarak basıldı) ve okunmuş 1 ayet; 6:103 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:100, 6:101 ve 6:103 nakarat3 yok; 6:102 'rabb lâ ilâh illâ _' süzgeç GEÇER ve ''alâ kull şey'' süzgeç GEÇMEZ",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; gönderge rol adıyla yazılmaz — sûre 6 bölüm 4 denetimi kuralı 4): "
 "6:100 3MP ('ve ce'alû', 've xaraqû', 'yesifûn' — tartışmalı; 've xalaqahum' eki — gönderge 'l-cinne' 4. kelime, tartışmalı), 3MS ('ve xalaqahum', 'lehû', 'subhânehû', 've te'âlâ' — gönderge lafız 2. kelime); "
 "6:101 3MS ('yekûnu' — fiil uyumu, fail 7. kelime; 'lehû', 'lehû', 've xalaqa', 've huve' — gönderge 6:100 2. kelime), 3FS ('tekun' — fiil uyumu, fail 11. kelime); "
 "6:102 muhatap 2MP ('rabbukum', 'fa'budûhu'), 3MS ('huve', 'fa'budûhu' eki, 've huve' — gönderge lafız 2. kelime); "
 "6:103 3FS ('tudrikuhu' — fiil uyumu, fail 3. kelime), 3MS ('tudrikuhu' eki, 've huve', 'yudriku', 've huve' — gönderge 6:102 2. kelime) — betik denetimi: KHATA_ADSIZ; "
 "edilgen yok (6:100-103)",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:100-103 söz yok — söz fiili yok (okuma); mealde tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 100 103 24' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 6:100 've ce'alû' (1.), 've xaraqû' (6.), 've benâtin' (9.), 've te'âlâ' (13.) CONJ, 've xalaqahum' (5.) CIRC; 6:101 've'l-ardi' (3.), 've lem' (8.) CONJ, 've xalaqa' (12.), 've huve' (15.) REM; 6:102 've huve' (12.) CONJ; "
 "6:103 've huve' (4. ve 7.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:100 ◈B خلق ('xalaqahum' 5. kelime — B2); 6:101 ◈K سمو ('s-semâvâti' 2. kelime — K1); 6:101 ◈K أرض ('l-ardi' 3. kelime — K1); 6:101 ◈B خلق ('xalaqa' 12. kelime — B2); 6:102 ◈B خلق ('xâliqu' 8. kelime — B2); 6:103 ◈B بصر ('l-ebsâru' 3. kelime — B3)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 100 103 24'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:101 (2:117); 6:102 (39:62); 6:100 ve 6:103 bağ yok; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:100 şahıs geçişi yok, edim geçişi emir → haber; 6:101 şahıs geçişi yok, edim geçişi haber → soru; 6:102 şahıs geçişi 3 → 2, şahıs sayısında beraberlik (ölçüm baskın 2), edim geçişi soru → emir; 6:103 şahıs geçişi 2 → 3, edim geçişi emir → haber, bölüm kapanışı; "
 "ölçüm iltifât 6:100-103 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:100 've xalaqahum' — hâl cümlesi (morph CIRC); 'subhânehû' — mastar, tenzih (morph ACC); "
 "6:101 'bedî'u's-semâvâti' — mahzuf mübtedanın haberi (morph NOM); 'ennâ yekûnu' — soru (morph INTG); 've lem tekun' — olumsuz cümle (morph CONJ + NEG); "
 "6:102 'lâ ilâhe illâ huve' — cins nefyi ve istisna (morph NEG + EXP); 'fa'budûhu' — sonuç fâsı ve emir (morph REM + IMPV); "
 "6:103 'lâ tudrikuhu'l-ebsâr' — olumsuz cümle (morph NEG); 've huve yudriku' — yeni cümle (morph REM)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:101 'bedî'u's-semâvâti ve'l-ard' — 2:117 ile eş (sayım: 'say 6:101 1-3'; lemma dizisi 'dizi 6 101 1 3'); "
 "6:102 'xâliqu kulli şey'in' ve 've huve 'alâ kulli şey'in vekîl' — 39:62 ile eş (sayım: 'say 6:102 8-10', 'say 6:102 12-16'; lemma dizileri 'dizi 6 102 8 10', 'dizi 6 102 12 16'); 6:100 kök بني ikilemesi; 6:101 kök شيأ, كلل, كون ikilemeleri; 6:102 kök أله, شيأ, كلل ikilemeleri; 6:103 kök بصر, درك ikilemeleri",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 24'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 "'bedî'u's-semâvâti ve'l-ard' 6:101 'göklerin ve yerin eşsiz yaratıcısıdır' / 2:117 'göklerin ve yerin eşsiz yaratıcısıdır' (emsal metninde) — çakışma değil (bayt eşit); 'xâliqu kulli şey'in' 6:102 'her şeyin yaratıcısıdır' / 39:62 'her şeyin yaratıcısıdır' (emsal metninde) — çakışma değil (bayt eşit); "
 "'ve huve 'alâ kulli şey'in vekîl' 6:102 'O her şey üzerine vekîldir' / 39:62 'O her şey üzerine vekîldir' (emsal metninde) — çakışma değil (bayt eşit); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:100 'ce'alû' PERF — meal 'kıldılar'; 'xalaqa' PERF — meal 'yarattı'; 'xaraqû' PERF — meal 'uydurdular'; 'te'âlâ' PERF — meal 'yücedir'; 'yesifûn' IMPF IND — meal 'nitelendirdiklerinden'; "
 "6:101 'yekûnu' IMPF IND — meal 'olur'; 'tekun' IMPF JUS ('lem' ile) — meal 'olmamışken'; 'xalaqa' PERF — meal 'yarattı'; 6:102 'fa'budûhu' IMPV — meal 'kulluk edin'; 6:103 'tudriku' IMPF IND — meal 'idrak etmez'; 'yudriku' IMPF IND — meal 'idrak eder'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 100 103 24'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:100 tarayıcı adayı (kök خلق; D_yeti) — çıpa değil: yaratma bildirimi, ölçü / mekanizma yok (olgu=False); 6:101, 6:102 ve 6:103 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:100 ('benîne' / 've benâtin'); 6:101 ('s-semâvâti' / 've'l-ardi'); 6:103 ('lâ tudrikuhu'l-ebsâru' / 'yudriku'l-ebsâra'); 6:102 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök خلق 6:100 ('xalaqahum'), 6:101 ('ve xalaqa') ve 6:102 ('xâliqu'); kök كلل 6:101 ve 6:102; kök شيأ 6:101 ve 6:102; kök علم 6:100 (''ilmin') ve 6:101 (''alîm'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 12-2 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm blokları 23 ve 24; bu blok bölümü kapatıyor; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b24/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 100 103 24'; lem_bozuk.py 24 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 100 103 → AYN_SONUC; sunum/bolum4_kurallar.py 100 103 24 → KHATA_HEPSI; sunum/bolum5_kurallar.py 100 103 24 → B5_HEPSI; sunum/bolum6_kurallar.py 100 103 24 → B6_HEPSI; sunum/bolum7_kurallar.py 100 103 24 → B7_HEPSI; sunum/bolum8_kurallar.py 100 103 24 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 100 103 24 → B9_HEPSI; sunum/bolum10_kurallar.py 100 103 24 → B10_HEPSI; sunum/bolum11_kurallar.py 100 103 24 → B11_HEPSI; sunum/bolum12_kurallar.py 100 103 24 → B12_HEPSI; sunum/bolum13_kurallar.py 100 103 24 → B13_HEPSI; sunum/bolum14_kurallar.py 100 103 24 → B14_HEPSI; sunum/bolum15_kurallar.py 100 103 24 → B15_HEPSI; sunum/bolum16_kurallar.py 100 103 24 → B16_HEPSI; sunum/bolum17_kurallar.py 100 103 24 → B17_HEPSI; sunum/bolum18_kurallar.py 100 103 24 → B18_HEPSI; sunum/bolum19_kurallar.py 100 103 24 → B19_HEPSI; sunum/bolum20_kurallar.py 100 103 24 → B20_HEPSI; sunum/bolum21_kurallar.py 100 103 24 → B21_HEPSI; sunum/bolum22_kurallar.py 100 103 24 → B22_HEPSI; sunum/bolum23_kurallar.py 100 103 24 → B23_HEPSI; sunum/bolum24_kurallar.py 100 103 24 → B24_HEPSI; sunum/bolum25_kurallar.py 100 103 24 → B25_HEPSI; sunum/bolum26_kurallar.py 100 103 24 → B26_HEPSI; sunum/bolum27_kurallar.py 100 103 24 → B27_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 24 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('ce'ale', 'allâh', 'şerîk', 'bedî'', 'semâ'', 'ard', 'xâliq', 'kull', 'şey'', ''alâ', 'vekîl', 'rabb', 'lâ', 'ilâh', 'illâ'); joker '_' lemmasız öğede ('dizi 6 102 3 7', 'dizi 6 102 12 16' — 'huve'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (100, 103): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_100_103.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b24.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '100', '103'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '100', '103', '24'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '100', '103', '24'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '100', '103', '24', '--tazelik-yok')}
    for _n in range(7, 28): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '100', '103', '24')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27 = [_R['B%d' % _n].splitlines() for _n in range(6, 28)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27): print([l for l in _x if l.startswith('HATA') or 'hata' in l])

# sûre 6 blok 2 (6:6-11) ARIZA oluşturucu — bölüm 1-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b02/olcum.txt'
os.environ['SAY2'] = '/home/claude/b02/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {}
BOL = "'Gökleri ve yeri yaratan; yüz çeviren kavimler'"


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
 ("6:6", "'min qabl min'", 2, 'say 6:6 5-7', "harekesiz 'min qablihim min' (5-7. kelime)", ('dizi 6 6 5 7', "min qabl min", '5-7', "biçim farkı (dizi 6 6 5 7): basılmamış eş zamir eki, önek")),
 ("6:7", "'qâle ellezî kefera in zâ illâ'", 2, 'say 6:7 9-14', "harekesiz 'le-qâle'llezîne keferû in hâzâ illâ' (9-14. kelime)", ('dizi 6 7 9 14', "qâle ellezî kefera in zâ illâ", '9-14', "biçim farkı (dizi 6 7 9 14): basılmamış eş önek")),
 ("6:10", "'mâ kâne _ istuhzi'e'", 2, 'say 6:10 10-13', "harekesiz 'mâ kânû bihî yestehzi'ûn' (10-13. kelime)", None),
 ("6:10", "'resûl min qabl'", 2, 'say 6:10 3-5', "harekesiz 'bi-rusulin min qablik' (3-5. kelime)", ('dizi 6 10 3 5', "resûl min qabl", '3-5', "biçim farkı (dizi 6 10 3 5): basılmamış eş i'râb, önek")),
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

VF_YAZI = {6: {16: "'ve erselne'", 20: "'ve ce'alne'", 25: "'fe-ehleknâhum'", 27: "'ve enşe'nâ'"}, 7: {1: "'ve lev'", 7: "'fe-lemesûhu'"}, 8: {1: "'ve qâlû'", 6: "'ve lev'"}, 9: {1: "'ve lev'", 6: "'ve le-lebesnâ'"}, 10: {1: "'ve le-qadi'", 6: "'fe-hâqa'"}, 11: {}}
sys.path.insert(0, '/home/claude/b02/yap')
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
open('/home/claude/b02/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '02')
BLOKLAR = [str(i) for i in range(1, 3)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '2', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b02/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '6', '11', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b02/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b02/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '6', '11', '02').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_6_11.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:6', '6:7', '6:8', '6:9', '6:10', '6:11'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_6_11.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(6, 12))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:6 kök هلك ('ehleknâ' 4. kelime, 'fe-ehleknâhum' 25. kelime — helâk), kök قبل ('qablihim' 6. kelime — önce), kök بعد ('ba'dihim' 29. kelime — art), kök أخر ('âxarîn' 31. kelime — başka): tetik listesinde yok; 6:7 kök سحر ('sihrun' 15. kelime — büyü): tetik listesinde yok; 6:9 kök رجل ('raculen' 5. kelime — adam): tetik listesinde yok; 6:10 kök قبل ('qablike' 5. kelime — önce): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '6', '11', '02')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b02/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 3)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(6, 12))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: sunum/edat_etiket.py EDLEM'e 'kem' (كم) ve 'levlâ' (لولا) — bölüm 15 denetimi kuralı 15: es_edat tanınmayan 0; mutasyon_sina — MUT_SONUC; geriye dönük koşu gerekmez (tanıma kümesi genişledi, eski kayıtlarda bu edatların başlığı yok); "
 "basilan satır sayısı (blok anı): 105",
 "kök tablosu: ölçümde '???' 6:7 6. kelime için 1 — yeni kök قرطس ('kâğıt, sayfa (kırtâs)'; yamalar/yama_kok_6_7.py → kok_ekle_6.ISTEK; kok_turkce 1624); ölçüm yeniden alındı, '???' 0; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 6 11 02'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
  "esmâ: 6:7 'in hâzâ illâ sihrun mubîn' (12-16. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (büyünün sıfatı); "
 "6:6, 6:8, 6:9, 6:10 ve 6:11 esmâ yok; lafız yok; Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 6 11 02'; bölüm 13 denetimi kuralı 2: esma_el eklendikten sonra; bölüm 15 denetimi kuralı 5; 6:7 muhur EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, araç tanımı farkı): " + EMH,
 "ölçüm: 6:6 '{{1|fâsıla ءاخرين → ن, N sınıfı}}', '{{1|simetri \\[4, 7, 12, 1\\]}}', '{{1|harf 140 → harf3 136, isaret 4}}' ve '{{1|dış düğüm 6}}'; "
 "6:7 '{{2|fâsıla مبين → ن, N sınıfı}}', '{{2|simetri \\[3, 1, 10, 1\\]}}', '{{2|harf 70 → harf3 65, isaret 5}}' ve '{{2|dış düğüm 2}}'; "
 "6:8 '{{3|fâsıla ينظرون → ن, N sınıfı}}', '{{3|simetri \\[3, 2, 6, 1\\]}}', '{{3|harf 57 → harf3 53, isaret 4}}', '{{3|dış düğüm 1}}' ve '{{3|EDİLGEN 3/5 fiil, pas z=3,10}}'; "
 "6:9 '{{4|fâsıla يلبسون → ن, N sınıfı}}', '{{4|harf 44 → harf3 42, isaret 2}}' ve '{{4|dış düğüm 0}}'; "
 "6:10 '{{5|fâsıla يستهزءون → ن, N sınıfı}}', '{{5|simetri \\[3, 7, 10, 1\\]}}', '{{5|harf 60 → harf3 56, isaret 4}}', '{{5|dış düğüm 2}}', '{{5|EDİLGEN 1/5 fiil, pas z=0,81}}' ve '{{5|esit2 → 21:41 oran 0,9910 kademe YAKIN}}'; "
 "6:11 '{{6|fâsıla ٱلمكذبين → ن, N sınıfı}}', '{{6|harf 42 → harf3 40, isaret 2}}', '{{6|dış düğüm 0}}' ve '{{6|esit2 → 27:69 oran 0,8974 kademe BENZER}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 6 11 02'): KALAN_P",
 "ölçüm aktör: 6:9 '{{4|aktör: adsız `racül` 5\\. sırada}}' (A1'de 'raculen'); 6:6, 6:7, 6:8, 6:10 ve 6:11 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:6 soru — INTG 1 'e-lem' (1.), NEG 2 'e-lem' (1.), 'lem' (13.); "
 "6:7 şart — COND 1 'lev' (1.), EMPH 1 'le-qâle' (9.), NEG 1 'in' (12.), RES 1 'illâ' (14.); ölçüm biçim alanı '{{2|biçim DIKKAT \\+ HASR}}' ('hâzâ' ATT 13., 'in … illâ'); "
 "6:8 şart — COND 1 've lev' (6.), EMPH 1 'le-qudiye' (9.), NEG 1 'lâ' (12.); 6:9 şart — COND 1 've lev' (1.), EMPH 2 'le-ce'alnâhu' (4.), 've le-lebesnâ' (6.); "
 "6:10 haber — CERT 1 ve EMPH 1 'le-qadi' (1.); 6:11 emir — IMPV 3 'qul' (1.), 'sîrû' (2.), 'nzurû' (6.); "
 "morph EXH ('levlâ' 6:8 2.), CAUS ('fe' 6:10 6.), REM ('ve' 6:7 1.; 6:10 1.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:6 ★ (kaynak n, z=1,97); 6:8 ★★★ (kaynak pas, z=3,10); 6:7, 6:9, 6:10 ve 6:11 yıldız yok",
 "fâsıla: 6:5 ن → 6:6 ن (ءاخرين) → 6:7 ن (مبين) → 6:8 ن (ينظرون) → 6:9 ن (يلبسون) → 6:10 ن (يستهزءون) → 6:11 ن (ٱلمكذبين) — bölüm boyunca ن sınıfı; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:6 36:31 (emsal olarak basıldı) ve okunmuş 5 ayet; 6:7 5:110 (basılmış) ve okunmuş 1 ayet; 6:8 okunmuş 1 ayet; 6:9 yok; 6:10 21:41 (emsal olarak basıldı) ve okunmuş 1 ayet; 6:11 yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:6 'min qabl min' süzgeç GEÇMEZ; 6:7 'qâle ellezî kefera in zâ illâ' GEÇER; 6:10 'mâ kâne _ istuhzi'e' GEÇER (6:5 kalıbıyla eş ad), 'resûl min qabl' GEÇMEZ; 6:8, 6:9 ve 6:11 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap' ile; 1. şahıs çoğul 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "fail olmayan mecrur çoğul ad ve mecrur ilgi zamiri A1'de yazılmaz — bölüm 11 denetimi kuralları 16 ve 19; A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; edilgen fiilde 'naib-i faili' — bölüm 11 denetimi kuralı 17): "
 "6:6 konuşan 1P (adsız), 3MP (adsız — 6:1 11. kelime ve 'qarnin'), muhatap 2MP (adsız), 3FS (adsız — 'l-enhâra'); 6:7 konuşan 1P, muhatap 2MS, 3MP ve 3MS (adsız), 'le-qâle' faili 'llezîne'; "
 "6:8 3MP (adsız), edilgen 3MS ('unzile' naib-i faili 'melekun', 'le-qudiye' naib-i faili 'l-emru'), konuşan 1P; 6:9 konuşan 1P, 3MS (adsız — elçi), 3MP (adsız), aktör 'raculen'; "
 "6:10 edilgen 3MS ('stuhzi'e'), muhatap 2MS, 'fe-hâqa' faili 'mâ', 3MP (adsız); 6:11 muhatap 2MS ve 2MP (adsız), 'kâne' fiil uyumu (''âqibetu') — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:7 'le-qâle' (9.) ardından söz 12-16. kelime — ayet içi kapanış; "
 "6:8 've qâlû' (1.) ardından söz 2-5. kelime — ayet içi kapanış; 6:11 'qul' (1.) ardından söz 2-10. kelime — ayet içi kapanış; 6:6, 6:9 ve 6:10 söz yok; "
 "mealde tırnaksız, iki nokta ile ya da söz fiili sonda (blok meal biçimi); A3'te ve A4'te 'söz açılır' / 'söz kapanır'; 'qul' 6:11 (bölüm 10 denetimi kuralı 8); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 6 11 02' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 6:6 've erselne' (16.), 've ce'alne' (20.), 've enşe'nâ' (27.) CONJ, 'fe-ehleknâhum' (25.) CONJ; 6:7 've lev' (1.) REM, 'fe-lemesûhu' (7.) CONJ; "
 "6:8 've qâlû' (1.), 've lev' (6.) CONJ; 6:9 've lev' (1.), 've le-lebesnâ' (6.) CONJ; 6:10 've le-qadi' (1.) REM, 'fe-hâqa' (6.) CAUS",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:6 ◈K أرض ('l-ardi' 11. kelime — K1; anlam notu: nesillerin yerleştirildiği yer); 6:6 ◈K سمو ('s-semâ'e' 17. kelime — K1; anlam notu: bol yağmurun geldiği gök); "
 "6:6 ◈K نهر ('l-enhâra' 21. kelime — K1; anlam notu: altlarından akan ırmaklar); 6:7 ◈B يدي ('eydîhim' 8. kelime — B3; anlam notu: kitabı elleriyle yoklama); "
 "6:11 ◈K أرض ('l-ardi' 4. kelime — K1; anlam notu: gezilecek yeryüzü); 6:8, 6:9 ve 6:10 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 6 11 02'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 6 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:6 (36:31); 6:7 (5:110); 6:10 (21:41); 6:11 (27:69); 6:8 ve 6:9 D3 yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "ayetler arası kalıp yok; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:6 şahıs geçişi 3 → 1, edim geçişi haber → soru; 6:7 söz açılır (12.) / kapanır (16., ayet içi), şahıs geçişi 1 → 3, edim geçişi soru → şart, şart → cevap; "
 "6:8 söz açılır (2.) / kapanır (5., ayet içi), şart → cevap; 6:9 şahıs geçişi 3 → 1, şart → cevap; 6:10 şahıs geçişi 1 → 3, edim geçişi şart → haber; "
 "6:11 söz açılır (2.) / kapanır (10., ayet içi), şahıs geçişi 3 → 2, edim geçişi haber → emir, bölüm kapanışı",
 "sözdizimi (okuma; morph etiketiyle): 6:6 'e-lem yerav' — soru ve olumsuzluk (morph INTG + NEG); 'kem ehleknâ' — çokluk 'kem'; 'mâ lem numekkin' — ilgi ve olumsuzluk (morph REL + NEG); "
 "6:7 'lev … le-qâle' — şart ve cevap (morph COND + EMPH); 'in hâzâ illâ' — olumsuzluk ve istisna (morph NEG + RES); 6:8 'levlâ' — teşvik (morph EXH); 've lev … le-qudiye' — şart ve cevap; "
 "6:9 've lev … le-ce'alnâhu' — şart ve cevap; 6:10 'le-qadi' — tekit (morph EMPH + CERT); 'fe-hâqa' — sonuç (morph CAUS); 6:11 'qul' — emir ve söz",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:6 'e-lem yerav kem ehleknâ' ile açılıyor — 36:31 ile eş (sayım: 'say 6:6 1-4'); "
 "6:6 kök هلك ikilemesi ('ehleknâ' / 'fe-ehleknâhum') — helâk ve inşâ karşıtlığı; 6:7 'in hâzâ illâ sihrun mubîn' — 5:110 ile eş (sayım: 'say 6:7 12-16'); 6:8 ve 6:9 kök ملك tekrarı (melek); "
 "6:10 've le-qadi'stuhzi'e bi-rusulin min qablik' ile açılıyor — 21:41 ile eş (sayım: 'say 6:10 1-5 --on'); 6:10 'mâ kânû bihî yestehzi'ûn' — 6:5 ile eş (sayım: 'say 6:10 10-13'); 6:11 'qul sîrû fi'l-ard' ile açılıyor — 27:69 ile eş (sayım: 'say 6:11 1-4')",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 02'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7): "
 "'e-lem yerav kem ehleknâ' 6:6 'Görmediler mi, kendilerinden önce nice nesilleri helâk ettik' / 36:31 'Görmediler mi, kendilerinden önce nice nesilleri helâk ettik' (emsal metninde) — çakışma değil; "
 "'bi-rusulin min qablik' 6:10 'Andolsun, senden önceki elçilerle de alay edildi' / 21:41 'Andolsun, senden önceki elçilerle de alay edildi' (emsal metninde) — çakışma değil; "
 "'mâ kânû bihî yestehzi'ûn' 6:10 'alay ettikleri şey' / 21:41 'alaya aldıkları şey' (emsal metninde) — çakışma — tam okuma sonu; "
 "'qul sîrû fi'l-ard' 6:11 'De ki: Yeryüzünde gezin' / 27:69 'De ki: Yeryüzünde gezin' (emsal metninde) — çakışma değil; "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9): 6:6 'tecrî' IMPF IND — meal 'akar' sıfat fiili; 6:7 ve 6:8 'lev' şartında PERF — meal '-seydik' / '-salardı', cevap '-erlerdi' / 'olurdu'; 6:8 'yunzarûn' IMPF — meal 'verilmezdi' (şart cevabına bağlı geçmiş); "
 "6:9 'yelbisûn' IMPF — meal 'karıştırdıkları' sıfat fiili",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or ''),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 6 11 02'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:6, 6:7, 6:8, 6:9, 6:10 ve 6:11 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:6 ('fe-ehleknâhum' / 've enşe'nâ'); 6:9 ('melekan' / 'raculen'); 6:7, 6:8, 6:10 ve 6:11 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök ملك 6:8 ('melekun', 'melekan') ve 6:9 ('melekan') — melek isteği bağı; kök هزأ 6:10 ('stuhzi'e', 'yestehzi'ûn') ve 6:5 — alay bağı; kök أرض 6:6 ve 6:11 — yeryüzü bağı; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 1-2 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm iki blok (1, 2); bu blok bölümü kapatıyor; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b02/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 6 11 02'; lem_bozuk.py 02 çıktısı): 6:6:22 'cerey', 6:7:7 'lemesu', 6:8:13 'yunzaru', 6:9:6 'lebes' — lem_bozuk bayrağı; meal maddesinde '(morph LEM ham biçim)' notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 6 11 → AYN_SONUC; sunum/bolum4_kurallar.py 6 11 02 → KHATA_HEPSI; sunum/bolum5_kurallar.py 6 11 02 → B5_HEPSI; sunum/bolum6_kurallar.py 6 11 02 → B6_HEPSI; sunum/bolum7_kurallar.py 6 11 02 → B7_HEPSI; sunum/bolum8_kurallar.py 6 11 02 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 6 11 02 → B9_HEPSI; sunum/bolum10_kurallar.py 6 11 02 → B10_HEPSI; sunum/bolum11_kurallar.py 6 11 02 → B11_HEPSI; sunum/bolum12_kurallar.py 6 11 02 → B12_HEPSI; sunum/bolum13_kurallar.py 6 11 02 → B13_HEPSI; sunum/bolum14_kurallar.py 6 11 02 → B14_HEPSI; sunum/bolum15_kurallar.py 6 11 02 → B15_HEPSI; sunum/bolum16_kurallar.py 6 11 02 → B16_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 2 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; 5:110 bağı sûre 5 okumasında basılmış ayetle; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('min', 'qabl', 'qâle', 'ellezî', 'kefera', 'in', 'zâ', 'illâ', 'mâ', 'kâne', 'istuhzi'e', 'resûl'); lemmasız öğe joker '_' ('bi'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (6, 11): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_6_11.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_5_hazirlik6.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '6', '11'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '6', '11', '02'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '6', '11', '02'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '6', '11', '02', '--tazelik-yok')}
    for _n in range(7, 17): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '6', '11', '02')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16 = [_R['B%d' % _n].splitlines() for _n in range(6, 17)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16): print([l for l in _x if l.startswith('HATA') or 'hata' in l])

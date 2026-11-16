# blok 20 (5:59-63) ARIZA oluşturucu — bölüm 9-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b20/olcum.txt'
os.environ['SAY2'] = '/home/claude/b20/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b19.txt', encoding='utf-8').read() + ']')
VF_YAZI_ESKI = {33: {6: "'ve rasûlehû'", 7: "'ve yes'avne'", 18: "'ve erculuhum'", 30: "'ve lehum fi'l-âxirati'"}, 34: {9: "'fa'lemû'"}, 35: {6: "'ve'bteğû'", 9: "'ve câhidû'"}, 36: {11: "'ve mislehû'", 22: "'ve lehum 'azâbun'"}}
BOL = "'Kitap ehlinin tutumu; bağlı el sözü; Tevrat ve İncil'i ayakta tutma'"


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
 ("5:59", "'qâle ehl kitâb'", 3, 'say 5:59 1-3', "harekesiz 'qul yâ ehle'l-kitâb' (1-3. kelime)", None),
 ("5:62", "'ekl suht bi'se mâ kâne'", 2, 'say 5:62 8-12 --on', "önek kesilmiş 've eklihimu's-suhta le-bi'se mâ kânû' (8-12. kelime)", None),
 ("5:62", "'bi'se mâ kâne'", 3, 'say 5:62 10-12 --on', "önek kesilmiş 'le-bi'se mâ kânû' (10-12. kelime)", None),
 ("5:63", "'ekl suht bi'se mâ kâne'", 2, 'say 5:63 8-12 --on', "önek kesilmiş 've eklihimu's-suhta le-bi'se mâ kânû' (8-12. kelime)", None),
 ("5:63", "'bi'se mâ kâne'", 3, 'say 5:63 10-12 --on', "önek kesilmiş 'le-bi'se mâ kânû' (10-12. kelime)", None),
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

VF_YAZI = {59: {11: "'ve mâ'", 14: "'ve mâ'", 18: "'ve enne'"}, 60: {13: "'ve ğadibe'", 15: "'ve ce'ale'", 18: "'ve'l-xanâzîra'", 19: "'ve 'abede'", 24: "'ve edallu'"}, 61: {1: "'ve izâ'", 5: "'ve qad'", 8: "'ve hum'", 12: "'ve'llâhu'"}, 62: {1: "'ve terâ'", 7: "'ve'l-'udvâni'", 8: "'ve eklihimu'"}, 63: {4: "'ve'l-ahbâru'", 8: "'ve eklihimu'"}}
sys.path.insert(0, '/home/claude/b20/yap')
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
open('/home/claude/b20/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '20')
BLOKLAR = [str(i) for i in range(1, 21)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR).replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '20').replace('\n', '; ')
EMS = open('/home/claude/b20/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '59', '63', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b20/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
MFARK = [(k, n, sayim.S2[k.replace(' --medde', '')][0]) for k, (n, d) in sayim.S2.items() if '--medde' in k]
MEDF = '; '.join("%s meddeli %d / meddesiz %d" % (k.replace(' --medde', ''), m, n) for k, n, m in MFARK)
MEDF += ' — fark yok, yeni eş yok' if all(n == m for k, n, m in MFARK) else ' — FARK VAR'
GLS = run('/home/claude/sunum/gloss_tara.py', '59', '63', '20').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_59_63.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'5:59', '5:60', '5:61', '5:62', '5:63'}
D3DISI = ', '.join(sorted(_U - _BAG - _ON, key=lambda x: tuple(map(int, x.split(':')))))
ANILIS = "5:59 kök قبل ('min qablu' 16-17. kelime — önceden; 17. kelime 'qablu'); 5:61 'izâ' ('ve izâ' 1. kelime — morph T, zaman)"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '59', '63', '20')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b20/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 21)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b5:%d:\d+' % a_, s_) for a_ in range(59, 64))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; bölüm 8 denetiminden kurallar araçlara işlendi: sunum/r5_on.py (kural 1), sunum/bolum6_kurallar.py (kurallar 2 ve 8), sunum/esma_muhur.py (kural 3), sunum/bolum8_kurallar.py (kurallar 1, 3, 4, 5, 6, 14, 15), "
 "sunum/bolum4_kurallar.py (kural 7), sunum/bolum5_kurallar.py (kural 9), sunum/geriye_donuk.py (kural 10; bolum8 eklendi), sunum/bolum7_kurallar.py (kurallar 11, 12, 13), sunum/es_edat.py (kural 15), sunum/yasakli.sh ve sunum/yasakli_test.txt (kural 16; 'bölüm N denetiminden' satırı aynen taşındığından art arda eş sözcük taramasının dışında); bu blokta ayrıca: sunum/bolum7_kurallar.py kural 13 (yalnız GEÇMEZ'li nakarat3 parçasında süzgeç ad başına okunuyor; hemze kürsüsü ؤ / ئ iskelete girmiyor), sunum/bolum8_kurallar.py kural 5 (hemze sonlu lemma adlı kalıp adı) ve kural 6 (es_lemma satırları satır sonuyla bölünüyor); "
 "mutasyon_sina — MUT_SONUC; geriye dönük koşu yeniden üretildi (GERI_P); düşen isabetlerin sınıfı (bölüm 8 kuralı 10): kayıt değişti 0, araç değişti 3 — blok 14 KÖK 'yetir-' (bölüm 8 kuralı 12 iletisi değişti), blok 14 KÖK 'et-' ve blok 17 KÖK 'kıl-' (bölüm 8 kuralı 11 kök kümesi değişti)",
 "kök tablosu: ölçümde '???' 5:59-63 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 59 63 20'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:59-63 esmâ yok; esma_el kaydı yok; lafız 5:59, 5:60 (2 geçiş), 5:61; 5:62 ve 5:63 lafız yok; 5:63 ölçüm Rab 3. sırada — 'r-rabbâniyyûne', Rab adı değil (bölüm 6 kuralı 14 — betikle: B6_ESMA)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 59 63 20'): " + EMH,
 "ölçüm: 5:59 '{{1|fâsıla فسقون → ن, N sınıfı}}', '{{1|EDİLGEN 2/5 fiil, pas z=1,95}}', '{{1|simetri \\[4, 4, 11, 1\\]}}', '{{1|harf 75 → harf3 75, isaret 0}}' ve '{{1|dış düğüm 10}}'; 5:60 '{{2|fâsıla ٱلسبيل → ل, ل sınıfı — KAFİYE KIRILMASI}}', '{{2|harf 115 → harf3 109, isaret 6}}' ve '{{2|dış düğüm 4}}'; "
 "5:61 '{{3|fâsıla يكتمون → ن, N sınıfı}}', '{{3|harf 75 → harf3 69, isaret 6}}' ve '{{3|dış düğüm 0}}'; 5:62 '{{4|fâsıla يعملون → ن, N sınıfı}}', '{{4|harf 64 → harf3 61, isaret 3}}' ve '{{4|dış düğüm 0}}'; 5:63 '{{5|fâsıla يصنعون → ن, N sınıfı}}', '{{5|harf 68 → harf3 66, isaret 2}}' ve '{{5|dış düğüm 0}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 59 63 20'): KALAN_P",
 "ölçüm aktör: 5:59-63 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle): 5:59 soru, emir, nida — IMPV 1 'qul' (1.), VOC 1 'yâ' (2.), INTG 1 'hel' (4.), RES 1 'illâ' (7.), biçim HASR; 5:60 soru, emir — IMPV 1 'qul' (1.), INTG 1 'hel' (2.); 5:61 haber — CERT 2 'qad' (5., 9.); 5:62 haber — EMPH 1 'le' (10.); 5:63 haber — EMPH 1 'le' (10.); morph EXH 'levlâ' (5:63 1.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 5:59 ★ (kaynak pas, z=1,95); 5:60 ★ (kaynak n, z=1,55; kafiye kırığı); 5:61, 5:62 ve 5:63 yıldız yok",
 "fâsıla: 5:58 ن (يعقلون) → 5:59 ن (فسقون) → 5:60 ل (السبيل; kafiye kırığı) → 5:61 ن (يكتمون) → 5:62 ن (يعملون) → 5:63 ن (يصنعون); 5:62 / 5:63 kapanışı 'le-bi'se mâ kânû' + IMPF 3MP; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref: 5:59 3:64 ve 2:136 (emsal olarak basıldı) ve okunmuş ve henüz okunmamış başka ayetler; 5:60 25:34 (emsal olarak basıldı) ve okunmuş başka ayetler; 5:61, 5:62 ve 5:63 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, joker '_' ile; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:59 'qâle ehl kitâb' süzgeç GEÇER, 'min qabl enne' ve 'âmene allâh mâ' GEÇMEZ; 5:60 ''an sevâ' sebîl' GEÇMEZ; 5:62 'ekl suht bi'se mâ kâne' ve 'bi'se mâ kâne' GEÇER, 're'â kesîr min' GEÇMEZ; 5:63 'ekl suht bi'se mâ kâne' ve 'bi'se mâ kâne' GEÇER; 5:61 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap' ile; alıntı ve kelime numarası ◇ konumuyla eş): "
 "5:59 muhatap 2MS (adsız), muhatap 2MP (adsız; söz içi), konuşan 1P (adsız; söz içi), 3MS (adsız — 'unzile' naib-i faili), Allah (lafız); 5:60 muhatap 2MS (adsız), konuşan 1S (adsız; söz içi), muhatap 2MP (adsız; söz içi), 3MS (adsız — 'le'ane', 'ğadibe', 'ce'ale', ''abede' failleri; 'le'anehu', ''aleyhi'), 3MP (adsız — 'minhumu'), Allah (lafız), 'men'; "
 "5:61 3MP (adsız — 'câ'ûkum', 'qâlû', 'dexalû', 'xaracû', 'kânû', 'yektumûn' failleri; 've hum'), muhatap 2MP (adsız), konuşan 1P (adsız; söz içi), 3MS (adsız — 'bihî'), Allah (lafız); 5:62 muhatap 2MS (adsız), 3MP (adsız — 'yusâri'ûne', 'kânû', 'ya'melûn' failleri; 'minhum', 'eklihimu'), 3MS (adsız — 'bi'se' faili); "
 "5:63 3MS (adsız — 'yenhâhumu', 'bi'se' failleri), 3MP (adsız — 'yenhâhumu' mef'ûlü, 'kânû', 'yasna'ûn' failleri; 'qavlihimu', 'eklihimu'), rabbaniler ve âlimler — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): 5:59 'qul' sözü (A3, 2-20. kelime); 5:60 'qul' sözü (A3, 2-27. kelime); 5:61 'qâlû' sözü 'âmennâ' (A3, 4. kelime); REM sapması (komut 'python3 sunum/bolum4_kurallar.py 59 63 20' — A3 aralığında morph REM): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:59 've mâ' (11., 14.), 've enne' (18.) CONJ; 5:60 've ğadibe' (13.), 've ce'ale' (15.), 've'l-xanâzîra' (18.), 've 'abede' (19.), 've edallu' (24.) CONJ; 5:61 've izâ' (1.), 've hum' (8.) CONJ, 've qad' (5.) CIRC, 've'llâhu' (12.) REM; 5:62 've terâ' (1.) REM, 've'l-'udvâni' (7.), 've eklihimu' (8.) CONJ; 5:63 've'l-ahbâru' (4.), 've eklihimu' (8.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 5:59-63 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 59 63 20'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:59 (3:64, 2:136), 5:60 (25:34), 5:61 (3:167) (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6); 5:62 ve 5:63 D3 eşi yok; "
 "ayetler arası kalıp 'eklihimu's-suhta le-bi'se mâ kânû' (5:62, 5:63) — sayım 'say 5:62 8-12 --on'; bölüm içi tekrar, ardışık bağ yerine sayımla kayıt; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7 — betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:59 edim geçişi haber → soru, emir, nida; şahıs geçişi 3 → 1; 5:60 edim geçişi soru, emir, nida → soru, emir; şahıs geçişi 1 → 3; 5:61 edim geçişi soru, emir → haber; şahıs geçişi yok; 5:62 ve 5:63 edim geçişi yok (haber); şahıs geçişi yok",
 "sözdizimi (okuma; morph etiketiyle): 5:59 'hel tenqimûne' — soru (morph INTG); 'illâ en âmennâ' — istisna (morph RES + SUB); 've enne ekserakum' — atıf (morph CONJ + ACC); 5:60 'men le'anehu'llâh' — 'şerr'in açıklaması (morph REL, okuma); 5:61 've qad dexalû' — hâl (morph CIRC); 've'llâhu a'lemu' — istînâf (morph REM); "
 "5:62 've terâ' — istînâf (morph REM); 'le-bi'se' — yerme (morph EMPH + PERF); 5:63 'levlâ' — teşvik / kınama (morph EXH)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:59 ve 5:60 'qul' ile açılıyor — Kitap ehline hitap; 5:59 kök نزل ikilemesi 'unzile' (bize / önceden); 5:60 kök شرر ikilemesi 'bi-şerrin' / 'şerrun'; "
 "5:61 'dexalû bi'l-kufr' / 'xaracû bih' — küfürle giriş ve çıkış (aday 1039); 5:62 ve 5:63 'eklihimu's-suhta le-bi'se mâ kânû' kapanışı paylaşıyor — 'ya'melûn' / 'yasna'ûn' fiil farkıyla",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 20'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + "'; çıktı aynen): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle): 'qul yâ ehle'l-kitâb' 5:59 'Ey Kitap ehli' / 3:64 'Ey kitap ehli' (emsal metninde) — tam okuma sonu; 'ulâ'ike şerrun mekânen' 5:60 'yer bakımından daha kötü' / 25:34 'yerce daha kötü' — tam okuma sonu",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle): " + MKK,
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 59 63 20'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:59-63 tarayıcı adayı yok; L3 / L4 adayı yok",
 "aday 1039: 5:61 ('dexalû bi'l-kufr' / 'xaracû bih'); ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök شرر 5:60 'bi-şerrin' (karşılık) / 'şerrun' (yer); kök كون 5:61-63 'kânû' + IMPF 3MP kalıbı ('yektumûn', 'ya'melûn', 'yasna'ûn') — okuma",
 "bölüm: " + BOL + " bölümü, bölüm 9-1 (bölüm 7 kuralı 9 — blok_plani_5.txt'ten) — bölüm iki blok (20, 21); başlıktaki 'Kitap ehlinin tutumu' 5:59-63; 'bağlı el sözü' ve 'Tevrat ve İncil'i ayakta tutma' blok 21'de; "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b20/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9 — betikle: komut 'python3 sunum/bolum5_kurallar.py 59 63 20'; lem_bozuk.py 20 çıktısı): 5:59:5 'naqamu', 5:62:4 'yusâri'u', 5:63:13 'sana'u' — lem_bozuk bayrağı; meal maddesinde '(morph LEM ham biçim)' notlu; lemma adı listesinde notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 59 63 → AYN_SONUC; sunum/bolum4_kurallar.py 59 63 20 → KHATA_HEPSI; sunum/bolum5_kurallar.py 59 63 20 → B5_HEPSI; sunum/bolum6_kurallar.py 59 63 20 → B6_HEPSI; sunum/bolum7_kurallar.py 59 63 20 → B7_HEPSI; sunum/bolum8_kurallar.py 59 63 20 → B8_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (sunum/sonradan.py --plan 20): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('qâle', 'ehl', 'kitâb', 'hel', 'naqamu' (morph LEM ham biçim), 'min', 'illâ', 'en', 'âmene', 'allâh', 'mâ', 'enzele', 'ilâ', 'qabl', 'enne', 'eksar', 'fâsiq', 'nebbe'e', 'şerr', 'zâ', 'mesûbe', ''ind', 'men', 'le'ane', 'ğadibe', ''alâ', 'ce'ale', 'qirade', 'xınzîr', ''abede', 'tâğût', 'ulâ'i', 'mekân', 'edall', ''an', 'sevâ'', 'sebîl', "
 "'izâ', 'câ'e', 'qad', 'dexale', 'kufr', 'xarace', 'a'lem', 'kâne', 'keteme', 're'â', 'kesîr', 'yusâri'u' (morph LEM ham biçim), 'fî', 'ism', ''udvân', 'ekl', 'suht', 'bi'se', ''amile', 'levlâ', 'nehâ', 'rabbâniyyîn', 'ahbâr', 'qavl', 'sana'u' (morph LEM ham biçim)); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (59, 63): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_59_63.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_5_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('06', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()
GERI = open('/home/claude/yamalar/geriye_donuk_5_b19.txt', encoding='utf-8').read().splitlines()[:2]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    AYN = (run('/home/claude/sunum/ayn_kontrol.py', '59', '63').splitlines() or ['?'])[-1]
    KUR = run('/home/claude/sunum/bolum4_kurallar.py', '59', '63', '20').splitlines()
    KH = [l for l in KUR if l.startswith('HATA')]
    B5 = run('/home/claude/sunum/bolum5_kurallar.py', '59', '63', '20').splitlines()
    B5H = [l for l in B5 if l.startswith('HATA')]
    B6 = run('/home/claude/sunum/bolum6_kurallar.py', '59', '63', '20', '--tazelik-yok').splitlines()
    B7 = run('/home/claude/sunum/bolum7_kurallar.py', '59', '63', '20').splitlines()
    B8 = run('/home/claude/sunum/bolum8_kurallar.py', '59', '63', '20').splitlines()
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
print(GLS); print(KUR); print(B5); print(B6); print(B7); print(B8)

# sûre 6 blok 3 (6:12-15) ARIZA oluşturucu — bölüm 2-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b03/olcum.txt'
os.environ['SAY2'] = '/home/claude/b03/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_6_b02.txt', encoding='utf-8').read() + ']')
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
 ("6:12", "'ellezî xasira nefs _ lâ âmene'", 2, 'say 6:12 20-25', "harekesiz 'llezîne xasirû enfusehum fe-hum lâ yu'minûn' (20-25. kelime)", None),
 ("6:12", "''alâ nefs rahme'", 2, 'say 6:12 10-12', "harekesiz ''alâ nefsihi'r-rahme' (10-12. kelime)", None),
 ("6:13", "'_ semî' 'alîm'", 2, 'say 6:13 7-9 --on', "önek kesilmiş 've huve's-semî'u'l-'alîm' (7-9. kelime)", None),
 ("6:14", "'qâle ğayr allâh'", 2, 'say 6:14 1-3', "harekesiz 'qul eğayra'llâh' (1-3. kelime)", None),
 ("6:14", "'kâne min muşrik'", 2, 'say 6:14 22-24', "harekesiz 'tekûnenne mine'l-muşrikîn' (22-24. kelime)", ('dizi 6 14 22 24', "kâne min muşrik", '22-24', "biçim farkı (dizi 6 14 22 24): basılmamış eş fiil çekimi")),
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

VF_YAZI = {12: {6: "'ve'l-ardi'", 23: "'fe-hum'"}, 13: {1: "'ve lehû'", 6: "'ve'n-nehâri'", 7: "'ve huve'"}, 14: {8: "'ve'l-ardi'", 9: "'ve huve'", 11: "'ve lâ yut'amu'", 21: "'ve lâ tekûnenne'"}, 15: {}}
sys.path.insert(0, '/home/claude/b03/yap')
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
open('/home/claude/b03/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '03')
BLOKLAR = [str(i) for i in range(1, 4)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '3', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b03/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '12', '15', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b03/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b03/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '12', '15', '03').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_12_15.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:12', '6:13', '6:14', '6:15'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_12_15.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(12, 16))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:12 kök نفس ('nefsihi' 11. kelime, 'enfusehum' 22. kelime — kendi), kök جمع ('le-yecma'annekum' 13. kelime — topla-): tetik listesinde yok; 6:14 kök ولي ('veliyyen' 5. kelime — dost): tetik listesinde yok; 6:15 kök عظم (''azîmin' 9. kelime — büyük): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '12', '15', '03')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b03/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 4)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(12, 16))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: sunum/edat_etiket.py EDLEM'e 'n' (ن, morph EMPH tekit nunu) — bölüm 15 denetimi kuralı 15: es_edat 6:14 'n' başlığını tanımıyordu; sunum/yasakli.sh IZIN'e ('ariza_6_12_15.txt', 'ilk, evvel') çifti — bölüm 10 denetimi kuralı 10: kapsamayan kök listesindeki أول kök anlamı araç çıktısı aynen (blok 34 emsali); sûre 6 bölüm 1 denetiminin araç kuralları bu bloktan önce işlendi ve commit edildi (sunum/bolum17_kurallar.py kural 1-7, 9-14; sunum/bolum5_kurallar.py kural 13 boş kök alanı; mutasyon_sina 181 / 181 — bölüm 1 sınamaları sûre 6 ortamında; geriye dönük koşu yamalar/geriye_donuk_6_b03.txt: bolum17_kurallar isabet 28 — kural 1: 3, 2: 1, 3: 4, 4: 10, 5: 1, 6: 2, 7: 1, 9: 1, 10: 1, 11: 1, 12: 2, 13: 1; kayıtlar geriye dönük yeniden yazılmadı); mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 111",
 "kök tablosu: ölçümde '???' 6:12, 6:13, 6:14 ve 6:15 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 12 15 03'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
   "esmâ: 6:13 've huve's-semî'u'l-'alîm' (7-9. kelime) — esma_el 'ilahi', kural 'zamirin haberi' (Allah) — 'huve' göndergesi 6:12 8. kelimedeki lafız; "
 "6:14 'eğayra'llâhi ettexizu veliyyen' (2-5. kelime) ve 'evvele men eslem' (18-20. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (esmâ dışı gönderge); "
 "6:12 ve 6:15 esmâ yok; lafız 6:12 ve 6:14; Rab 6:15 (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7); 'zamirin haberi' kapalı listede (sûre 6 hazırlığı varsayılan kararı, onaya açık)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 12 15 03'; bölüm 13 denetimi kuralı 2: esma_el eklendikten sonra; bölüm 15 denetimi kuralı 5; 6:14 muhur EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, araç tanımı farkı): " + EMH,
 "ölçüm: 6:12 '{{1|fâsıla يؤمنون → ن, N sınıfı}}', '{{1|simetri \\[3, 2, 17, 1\\]}}', '{{1|harf 102 → harf3 97, isaret 5}}' ve '{{1|dış düğüm 3}}'; "
 "6:13 '{{2|fâsıla ٱلعليم → م, N sınıfı}}', '{{2|harf 39 → harf3 36, isaret 3}}' ve '{{2|dış düğüm 0}}'; "
 "6:14 '{{3|fâsıla ٱلمشركين → ن, N sınıfı}}', '{{3|simetri \\[4, 14, 19, 1\\]}}', '{{3|harf 93 → harf3 90, isaret 3}}', '{{3|dış düğüm 3}}', '{{3|İÇ düğüm 1}}' ve '{{3|EDİLGEN 2/9 fiil, pas z=0,94}}'; "
 "6:15 '{{4|fâsıla عظيم → م, N sınıfı}}', '{{4|harf 30 → harf3 29, isaret 1}}', '{{4|dış düğüm 2}}' ve '{{4|esit2 → 39:13 oran 1,0000 kademe TAM · 39:13 oran 1,0000 kademe TAM}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 12 15 03'): KALAN_P",
 "ölçüm aktör: 6:12, 6:13, 6:14 ve 6:15 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:12 soru, emir — IMPV 2 'qul' (1., 7.), INTG 1 'li-men' (2.), EMPH 2 'le-yecma'annekum' (13.), NEG 2 'lâ' (17., 24.); "
 "6:13 haber, kip yok; 6:14 soru, emir — IMPV 2 'qul' (1., 13.), INTG 1 'eğayra' (2.), NEG 2 'lâ' (11., 21.), EMPH 1 'tekûnenne' (22.); 6:15 emir, şart — IMPV 1 'qul' (1.), COND 1 'in' (4.); "
 "morph REM ('fe' 6:12 23.; 've' 6:13 7.; 6:14 9. ve 21.), ACC ('inne' 6:14 14.; 6:15 2.), SUB ('en' 6:14 16.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:15 ★★ (kaynak rab, z=2,05); 6:12, 6:13 ve 6:14 yıldız yok",
 "fâsıla: 6:11 ن → 6:12 ن (يؤمنون) → 6:13 م (ٱلعليم) → 6:14 ن (ٱلمشركين) → 6:15 م (عظيم) — N sınıfı içinde ن / م nöbeti; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:12 4:87 (emsal olarak basıldı) ve okunmuş 2 ayet; 6:13 yok; 6:14 okunmuş 2 ayet ve okunmamış 2 ayet (sûre içi 1); 6:15 39:13 (emsal olarak basıldı) ve okunmuş 1 ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:12 'ellezî xasira nefs _ lâ âmene' süzgeç GEÇER, ''alâ nefs rahme' GEÇMEZ; 6:13 '_ semî' 'alîm' GEÇMEZ; 6:14 'qâle ğayr allâh' ve 'kâne min muşrik' GEÇMEZ; 6:15 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; edilgen fiilde 'naib-i faili' — bölüm 11 denetimi kuralı 17; açık naib-i failde 'adsız' yazılmaz — sûre 6 bölüm 1 denetimi kuralı 6): "
 "6:12 muhatap 2MS ve 2MP (adsız), 3MS (adsız — gönderge lafız ve 'yevmi'), 3MP (adsız — gönderge 'llezîne'); 6:13 3MS (adsız — gönderge 6:12 8. kelimedeki lafız ve 'mâ'); "
 "6:14 muhatap 2MS, konuşan 1S (adsız; 'umirtu' edilgen — naib-i faili 1S zamir), 3MS (adsız — gönderge lafız; 'yut'amu' edilgen — naib-i faili zamir), 'eslem' (adsız — gönderge 'men'); 6:15 muhatap 2MS, konuşan 1S (adsız) — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:12 'qul' (1.) ardından söz 2-6. kelime, 'qul' (7.) ardından söz 8. kelime — ayet içi kapanışlar; "
 "6:14 'qul' (1.) ardından söz 2-12. kelime (REM sapması 6:14 (9. kelime) — 've huve yut'imu' söz içinde istînâf, söz 12. kelimeye dek sürer), 'qul' (13.) ardından söz 14-20. kelime — ayet içi kapanışlar; 21-24. kelime ('ve lâ tekûnenne', morph REM) söz dışı; 6:15 'qul' (1.) ardından söz 2-9. kelime — ayet içi kapanış; 6:13 söz yok; "
 "mealde tırnaksız, iki nokta ile (blok meal biçimi); A3'te ve A4'te 'söz açılır' / 'söz kapanır'; 'qul' 6:12, 6:14 ve 6:15 (bölüm 10 denetimi kuralı 8); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 12 15 03' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 6:12 've'l-ardi' (6.) CONJ, 'fe-hum' (23.) REM; 6:13 've lehû' (1.), 've'n-nehâri' (6.) CONJ, 've huve' (7.) REM; 6:14 've'l-ardi' (8.), 've lâ yut'amu' (11.) CONJ, 've huve' (9.), 've lâ tekûnenne' (21.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:12 ◈K سمو ('s-semâvâti' 5. kelime — K1; anlam notu: mülkü sorulan gökler); 6:12 ◈K أرض ('l-ardi' 6. kelime — K1; anlam notu: mülkü sorulan yer); "
 "6:12 ◈K يوم ('yevmi' 15. kelime — K2; anlam notu: toplanılacak kıyamet günü); 6:13 ◈K ليل ('l-leyli' 5. kelime — K1; anlam notu: gecede barınanlar); 6:13 ◈K نهر ('n-nehâri' 6. kelime — K1; anlam notu: gündüzde barınanlar); "
 "6:13 ◈B سمع ('s-semî'u' 8. kelime — B3; anlam notu: işiten); 6:14 ◈K سمو ('s-semâvâti' 7. kelime — K1; anlam notu: yaratılan gökler); 6:14 ◈K أرض ('l-ardi' 8. kelime — K1; anlam notu: yaratılan yer); "
 "6:15 ◈K يوم ('yevmin' 8. kelime — K2; anlam notu: azabı korkulan büyük gün)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 12 15 03'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:12 (4:87); 6:15 (39:13); 6:13 ve 6:14 D3 yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "ayetler arası kalıp yok; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:12 söz açılır / kapanır (2-6. ve 8. kelime, ayet içi), şahıs geçişi 2 → 3, edim geçişi emir → soru, bölüm açılışı; 6:13 edim geçişi soru → haber; "
 "6:14 söz açılır / kapanır (2-12. ve 14-20. kelime, ayet içi), şahıs geçişi 3 → 1, edim geçişi haber → soru; 6:15 söz açılır / kapanır (2-9. kelime, ayet içi), edim geçişi soru → emir, şart → cevap; "
 "şahıs beraberliği yok (sûre 6 bölüm 1 denetimi kuralı 9)",
 "sözdizimi (okuma; morph etiketiyle): 6:12 'li-men' — soru (morph INTG); 'le-yecma'annekum' — tekit (morph EMPH, önek ve son ek); 'lâ raybe' — cins nefyi (morph NEG); 'fe-hum lâ yu'minûn' — istînâf (morph REM); "
 "6:13 've lehû mâ' — haber öne alınmış isim cümlesi; 've huve' — istînâf (morph REM); 6:14 'eğayra'llâhi' — soru (morph INTG); 'innî umirtu en ekûne' — tekit ve masdar (morph ACC + SUB); 'lâ tekûnenne' — yasak ve tekit (morph NEG + EMPH); "
 "6:15 'innî exâfu in 'aseytu' — tekit ve şart (morph ACC + COND)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:12 'qul li-men mâ fi's-semâvâti ve'l-ard' ile açılıyor (sayım: 'say 6:12 1-6'); "
 "6:12 'le-yecma'annekum ilâ yevmi'l-qiyâmeti lâ raybe fîh' — 4:87 ile eş (sayım: 'say 6:12 13-19'); 6:13 'l-leyli' / 'n-nehâri' karşıtlığı; 6:14 kök طعم ikilemesi ('yut'imu' / 'yut'amu') — etken / edilgen karşıtlığı; "
 "6:15 'qul innî exâfu in 'aseytu rabbî 'azâbe yevmin 'azîm' ile açılıyor — 39:13 ile tam eş (sayım: 'say 6:15 1-9'); 6:12, 6:14 ve 6:15 'qul' ile açılıyor",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 03'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3): "
 "'le-yecma'annekum ilâ yevmi'l-qiyâmeti lâ raybe fîh' 6:12 'Sizi kıyamet gününe mutlaka toplayacaktır; onda şüphe yoktur' / 4:87 'Sizi kıyamet gününe mutlaka toplayacaktır; onda şüphe yoktur' (emsal metninde) — çakışma değil; "
 "'qul' 6:15 'De ki' / 39:13 'De ki' (emsal metninde) — çakışma değil; "
 "'innî exâfu in 'aseytu rabbî 'azâbe yevmin 'azîm' 6:15 'Rabbime isyan edersem büyük bir günün azabından korkarım' / 39:13 'Rabbime isyan edersem büyük bir günün azabından korkarım' (emsal metninde) — çakışma değil; "
 "''azâbe yevmin 'azîm' 6:15 'büyük bir günün azabından' / 39:13 'büyük bir günün azabından' (emsal metninde) — çakışma değil; "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9): 6:12 'yu'minûn' IMPF IND — meal geniş zaman olumsuz 'inanmazlar'; 6:14 'ettexizu' IMPF IND — meal geniş zaman soru 'edinirim'; 'yut'imu' / 'yut'amu' IMPF — meal 'doyurur' / 'doyurulmaz'; 'tekûnenne' IMPF + EMPH — meal yasak 'olma'; "
 "6:15 'exâfu' IMPF — meal geniş zaman 'korkarım'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 12 15 03'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:12, 6:13, 6:14 ve 6:15 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:13 ('l-leyli' / 'n-nehâri'); 6:14 ('yut'imu' / 'yut'amu'); 6:12 ve 6:15 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök سمو ve أرض 6:12 ve 6:14 — göklerin ve yerin sahibi / yaratıcısı bağı; kök يوم 6:12 ('yevmi') ve 6:15 ('yevmin') — kıyamet günü / büyük gün bağı; kök قول 6:12, 6:14 ve 6:15 ('qul') — söz emri; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 2-1 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm iki blok (3, 4); bu blok bölümü açıyor; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b03/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 12 15 03'; lem_bozuk.py 03 çıktısı): lem_bozuk bayrağı yok; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 12 15 → AYN_SONUC; sunum/bolum4_kurallar.py 12 15 03 → KHATA_HEPSI; sunum/bolum5_kurallar.py 12 15 03 → B5_HEPSI; sunum/bolum6_kurallar.py 12 15 03 → B6_HEPSI; sunum/bolum7_kurallar.py 12 15 03 → B7_HEPSI; sunum/bolum8_kurallar.py 12 15 03 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 12 15 03 → B9_HEPSI; sunum/bolum10_kurallar.py 12 15 03 → B10_HEPSI; sunum/bolum11_kurallar.py 12 15 03 → B11_HEPSI; sunum/bolum12_kurallar.py 12 15 03 → B12_HEPSI; sunum/bolum13_kurallar.py 12 15 03 → B13_HEPSI; sunum/bolum14_kurallar.py 12 15 03 → B14_HEPSI; sunum/bolum15_kurallar.py 12 15 03 → B15_HEPSI; sunum/bolum16_kurallar.py 12 15 03 → B16_HEPSI; sunum/bolum17_kurallar.py 12 15 03 → B17_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 3 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('ellezî', 'xasira', 'nefs', 'lâ', 'âmene', ''alâ', 'rahme', 'semî'', ''alîm', 'qâle', 'ğayr', 'allâh', 'kâne', 'min', 'muşrik'); lemmasız öğe joker '_' ('hum', 'huve'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (12, 15): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_12_15.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_5_hazirlik6.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '12', '15'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '12', '15', '03'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '12', '15', '03'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '12', '15', '03', '--tazelik-yok')}
    for _n in range(7, 18): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '12', '15', '03')
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

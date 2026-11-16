# blok 20 (5:59-63) ARIZA oluşturucu — bölüm 9-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b22/olcum.txt'
os.environ['SAY2'] = '/home/claude/b22/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b21.txt', encoding='utf-8').read() + ']')
VF_YAZI_ESKI = {33: {6: "'ve rasûlehû'", 7: "'ve yes'avne'", 18: "'ve erculuhum'", 30: "'ve lehum fi'l-âxirati'"}, 34: {9: "'fa'lemû'"}, 35: {6: "'ve'bteğû'", 9: "'ve câhidû'"}, 36: {11: "'ve mislehû'", 22: "'ve lehum 'azâbun'"}}
BOL = "'Tebliğ emri; İsrâiloğullarının misakı; Mesih ve teslis'"


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
 ("5:67", "'mâ enzele ilâ min rabb'", 3, 'say 5:67 4-8', "harekesiz 'mâ unzile ileyke min rabbik' (4-8. kelime; biçim öğesi 'ileyke' — ölçüm kalıbında 2MS biçim öğesi; ◇ lemma dizisi 'dizi 5 67 4 8' sûre içi 4, 'ileyhim' / 'ileykum' eşleri dahil)", None),
 ("5:67", "'inne allâh lâ hedâ qavm'", 2, 'say 5:67 19-23', "harekesiz 'inna'llâhe lâ yehdi'l-qavm' (19-23. kelime)", None),
 ("5:67", "'allâh lâ hedâ qavm'", 3, 'say 5:67 20-23', "harekesiz 'llâhe lâ yehdi'l-qavm' (20-23. kelime)", ('dizi 5 67 20 23', "allâh lâ hedâ qavm", '20-23', "biçim farkı (dizi 5 67 20 23): 5:51 yazım eş; basılmamış eş i'râb, önek")),
 ("5:67", "'inne allâh lâ'", 3, 'say 5:67 19-21', "harekesiz 'inna'llâhe lâ' (19-21. kelime)", None),
 ("5:68", "'zâde kesîr min mâ enzele ilâ min rabb tuğyân kufr'", 2, 'say 5:68 16-25 --on', "önek kesilmiş 've le-yezîdenne kesîran minhum mâ unzile ileyke min rabbike tuğyânen ve kufran' (16-25. kelime)", None),
 ("5:68", "'mâ enzele ilâ min rabb'", 3, 'say 5:68 19-23', "harekesiz 'mâ unzile ileyke min rabbik' (19-23. kelime; biçim öğesi 'ileyke' — ölçüm kalıbında 2MS biçim öğesi; ◇ lemma dizisi 'dizi 5 68 19 23' sûre içi 4, 'ileyhim' / 'ileykum' eşleri dahil)", None),
 ("5:68", "'eqâme tevrâ incîl mâ enzele'", 2, 'say 5:68 8-12', "harekesiz 'tuqîmu't-tevrâte ve'l-incîle ve mâ unzile' (8-12. kelime)", ('dizi 5 68 8 12', "eqâme tevrâ incîl mâ enzele", '8-12', "biçim farkı (dizi 5 68 8 12): 5:66 fiil çekimi, zamir eki")),
 ("5:68", "'fe-lâ te'se 'alâ qavm'", 2, 'say 5:68 26-29 --on', "önek kesilmiş 'fe-lâ te'se 'ale'l-qavm' (26-29. kelime)", None),
 ("5:68", "'qâle ehl kitâb'", 3, 'say 5:68 1-3', "harekesiz 'qul yâ ehle'l-kitâb' (1-3. kelime)", None),
 ("5:69", "'ellezî âmene ellezî'", 2, 'say 5:69 2-4', "harekesiz 'llezîne âmenû ve'llezîne' (2-4. kelime; biçim öğesi 've' öneki — ölçüm kalıbı 'ellezî' biçimlerini önekle ayırıyor; ◇ lemma dizisi 'dizi 5 69 2 4' sûre içi 3)", ('dizi 5 69 2 4', "ellezî âmene ellezî", '2-4', "biçim farkı (dizi 5 69 2 4): 5:55 önek; basılmamış eş önek — ölçüm kalıbı 've' önekli 'ellezî' ile öneksiz biçimi ayırmıyor; öneksiz eş koşusu (dizi 5 69 2 4): 5:55 → önek kesilmiş sûre içi 1; basılmamış eş → önek kesilmiş sûre içi 1 — kalan fark tam okuma sonu")),
 ("5:70", "'mîsâq buneyy isrâ'îl'", 2, 'say 5:70 3-5', "harekesiz 'mîsâqa benî isrâ'îl' (3-5. kelime)", None),
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

VF_YAZI = {67: {9: "'ve in'", 12: "'fe-mâ'", 15: "'ve'llâhu'"}, 68: {10: "'ve'l-incîle'", 11: "'ve mâ'", 16: "'ve le-yezîdenne'", 25: "'ve kufran'", 26: "'fe-lâ'"}, 69: {4: "'ve'llezîne'", 6: "'ve's-sâbi'ûne'", 7: "'ve'n-nasârâ'", 11: "'ve'l-yevmi'", 13: "'ve 'amile'", 15: "'fe-lâ'", 18: "'ve lâ'"}, 70: {6: "'ve erselnâ'", 18: "'ve ferîqan'"}}
sys.path.insert(0, '/home/claude/b22/yap')
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
open('/home/claude/b22/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '22')
BLOKLAR = [str(i) for i in range(1, 23)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR).replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '22').replace('\n', '; ')
EMS = open('/home/claude/b22/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '67', '70', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b22/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
MFARK = [(k, n, sayim.S2[k.replace(' --medde', '')][0]) for k, (n, d) in sayim.S2.items() if '--medde' in k]
MEDF = '; '.join("%s meddeli %d / meddesiz %d" % (k.replace(' --medde', ''), m, n) for k, n, m in MFARK)
MEDF += ' — fark yok, yeni eş yok' if all(n == m for k, n, m in MFARK) else ' — FARK VAR'
GLS = run('/home/claude/sunum/gloss_tara.py', '67', '70', '22').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_67_70.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'5:67', '5:68', '5:69', '5:70'}
D3DISI = ', '.join(sorted(_U - _BAG - _ON - {'5:64'}, key=lambda x: tuple(map(int, x.split(':')))))
ANILIS = "5:69 kök أخر ('l-âxiri' 12. kelime — âhiret); 5:70 'kullemâ' (9. kelime — morph T, zaman şartı; kök كلل); 5:70 kök نفس ('enfusuhum' 15. kelime — can); 5:70 kök قتل ('yaqtulûn' 19. kelime — öldür-)"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '67', '70', '22')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b22/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 23)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b5:%d:\d+' % a_, s_) for a_ in range(67, 71))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; bölüm 9 denetiminden kurallar araçlara işlendi: sunum/bolum9_kurallar.py (yeni; kurallar 1, 2, 3, 4, 5, 6, 7, 9, 10, 11), sunum/r5_gerekce.py (yeni; kural 4 — gerekçe biçim farkı betikle), sunum/bolum4_kurallar.py (kural 8 — açık adlı fail; 'fiil uyumu' ölçütü), "
 "sunum/bolum7_kurallar.py (kural 12 — ◇ ⇔ ARIZA tetik kümesi S1 süzgeciyle), sunum/kural13.py (kural 13 — uzun ünlü korunur, tekilleştirme zayıf harf atımından sonra yapılmaz), sunum/bolum8_kurallar.py (kural 14 — kalıp adı yalnız R5 satır başından), "
 "sunum/geriye_donuk.py (kural 14 — bolum9_kurallar ve kural13 eklendi), sunum/commit_kos.sh (yeni; kural 15 — commit durumuyla koşu; sınama: 'sonradan.py --plan 21' commit 18a5ceb ile eskiyen 18, canlı 27), ARIZA üreticisi (kural 9 — taşınan denetim maddelerine yer tutucu değişimi yok), "
 "sunum/bolum6_kurallar.py (kural 14 emsal: kayıt kendi yorumunda 'sıfatı' anıyor ve emsal 'X'in sıfatı' ise eş), sunum/mutasyon_sina.py (bölüm 9 sınamaları); kural 8'in [okuma] kısmı bu bloğun A1'inde uygulandı (5:70 'câ'ehum', 'tehvâ'); "
 "mutasyon_sina — MUT_SONUC; geriye dönük koşu son araç değişikliğinden sonra yeniden üretildi (GERI_P); düşen 55 — araç değişti: bolum8_kurallar (5) 33 (kural 14: düzyazıdan ad yakalanmıyor), bolum8_kurallar (6) 12, bolum7_kurallar (4) 7 (S1 süzgeci; 'ni'me' ve 'ism' yanlış pozitifleri), bolum7_kurallar (13) 3; yeni 238 — bolum8_kurallar (6) 67 (eski bloklarda karar eksiği), bolum9_kurallar (3) 61, (5) 26, (4) 23, (6) 11, (1) 7, (2) 7, (11) 5, (10) 2, (9) 2, (7) 1, bolum4_kurallar 17 (kural 8 açık fail), es_edat 3, gloss_tara 3, kural13 2, bolum7_kurallar (13) 1 — tam okuma sonu listesi, kayıtlar geriye dönük yeniden yazılmadı",
 "kök tablosu: ölçümde '???' 5:67-70 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 67 70 22'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:69 'l-âxiri' (12. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' ('yevm' sıfatı, âhiret günü); 5:67, 5:68 ve 5:70 esmâ yok; lafız 5:67 (2 geçiş), 5:69; 5:68 ve 5:70 lafız yok; Rab 5:67 ('rabbike', 8. sırada) ve 5:68 ('rabbikum', 'rabbike', 15. ve 23. sırada) — Rab adı (bölüm 6 kuralı 14 — betikle: B6_ESMA; emsal kayıtları 'yevm'in sıfatı' — bu kayıt da sıfat olarak anıyor)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 67 70 22'): " + EMH,
 "ölçüm: 5:67 '{{1|fâsıla ٱلكفرين → ن, N sınıfı}}', '{{1|EDİLGEN 1/6 fiil, pas z=0,62}}', '{{1|simetri \\[3, 4, 7, 1\\]}}', '{{1|harf 97 → harf3 92, isaret 5}}' ve '{{1|dış düğüm 1}}'; "
 "5:68 '{{2|fâsıla ٱلكفرين → ن, N sınıfı}}', '{{2|EDİLGEN 2/7 fiil, pas z=1,30}}', '{{2|simetri \\[8, 10, 18, 2\\]}}', '{{2|harf 131 → harf3 125, isaret 6}}' ve '{{2|dış düğüm 4}}'; "
 "5:69 '{{3|fâsıla يحزنون → ن, N sınıfı}}', '{{3|simetri \\[3, 1, 17, 1\\]}}', '{{3|harf 95 → harf3 92, isaret 3}}' ve '{{3|dış düğüm 2}}'; 5:70 '{{4|fâsıla يقتلون → ن, N sınıfı}}', '{{4|harf 93 → harf3 87, isaret 6}}' ve '{{4|dış düğüm 2}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 67 70 22'): KALAN_P",
 "ölçüm aktör: 5:68 '{{2|adlı تَوْراة 9\\. sırada \\(kitab, rol meful\\)}}', '{{2|adlı إِنجِيل 10\\. sırada \\(kitab, rol meful\\)}}' — 'tuqîmû' mef'ûlleri; 5:69 '{{3|adlı صابِئ 6\\. sırada \\(cins, rol fail\\)}}', '{{3|adlı نَصْرانِيّ 7\\. sırada \\(cins, rol fail\\)}}' — sözdiziminde 'inne' ismine atıf (okuma); "
 "5:70 '{{4|adlı إِسْرائِيل 5\\. sırada \\(kavim, rol mecrur\\)}}', '{{4|adsız `ferîk` 16\\. sırada}}', '{{4|adsız `ferîk` 18\\. sırada}}' — 'mîsâqa benî' muzâfun ileyhi ve mef'ûller; 5:67 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle): 5:67 emir, nida, şart — IMPV 1 'belliğ' (3.), VOC 1 'yâ' (1.), COND 1 'in' (9.), NEG 3 'lem' (10.), 'mâ' (12.), 'lâ' (21.), biçim DIKKAT; 5:68 emir, yasak, nida — IMPV 1 'qul' (1.), VOC 1 'yâ' (2.), PRO 1 'lâ' (26.), EMPH 2 'le' ve te'kid nûnu (16.), biçim NEHY; "
 "5:69 şart — COND 1 'men' (8.), NEG 2 'lâ' (15., 18.); 5:70 haber — CERT 1 'qad' (1.), EMPH 1 'le' (1.), NEG 1 'lâ' (13.); morph T 'kullemâ' (5:70 9.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 5:68 ★ (kaynak n, z=1,87); 5:67, 5:69 ve 5:70 yıldız yok",
 "fâsıla: 5:66 ن (يعملون) → 5:67 ن (الكفرين) → 5:68 ن (الكفرين) → 5:69 ن (يحزنون) → 5:70 ن (يقتلون); kafiye kırığı yok; 5:67 / 5:68 kapanışı 'l-qavm' + 'l-kâfirîn'; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref: 5:67 33:39 (emsal olarak basıldı); 5:68 3:64 ve 5:59 (basılmış) ve okunmuş ve henüz okunmamış başka ayetler; 5:69 2:62 (emsal olarak basıldı) ve okunmuş başka ayetler; 5:70 2:87 (emsal olarak basıldı) ve okunmuş başka ayetler",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, joker '_' ile; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:67 'mâ enzele ilâ min rabb', 'inne allâh lâ hedâ qavm', 'allâh lâ hedâ qavm' ve 'inne allâh lâ' süzgeç GEÇER; "
 "5:68 'zâde kesîr min mâ enzele ilâ min rabb tuğyân kufr', 'mâ enzele ilâ min rabb', 'eqâme tevrâ incîl mâ enzele', 'fe-lâ te'se 'alâ qavm' ve 'qâle ehl kitâb' süzgeç GEÇER; 5:69 'ellezî âmene ellezî' GEÇMEZ; 5:70 'mîsâq buneyy isrâ'îl' GEÇMEZ",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap' ile; alıntı ve kelime numarası ◇ konumuyla eş): "
 "5:67 muhatap 2MS (adsız — elçi; nida edilen 'r-rasûlu'), 3MS (adsız — 'unzile' naib-i faili; 'risâletehû'; 'ya'simu', 'yehdî' failleri), Rab, Allah (lafız); "
 "5:68 muhatap 2MS (adsız), Kitap ehli (nida edilen), muhatap 2MP (adsız; söz içi), Tevrat ve İncil (adlı kitaplar), 3MS (adsız — 'unzile' naib-i faili, 'yezîdenne' faili), 3MP (adsız — 'minhum'), Rab; "
 "5:69 iman edenler, Yahudi olanlar, Sâbiîler ve Nasârâ, 3MP (adsız — 'âmenû', 'hâdû', 'yahzenûn' failleri; ''aleyhim', 'hum'), 3MS (adsız — 'âmene', ''amile' failleri; gönderge 'men'), Allah (lafız); "
 "5:70 konuşan 1P (adsız), İsrâiloğulları (adlı kavim), 3MP (adsız — 'ileyhim', 'câ'ehum', 'enfusuhum'; 'kezzebû', 'yaqtulûn' failleri), 'rasûlun' ('câ'ehum' faili — 3MS fiil uyumu), 'enfus' ('tehvâ' faili — 3FS fiil uyumu) — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): 5:68 'qul' sözü (A3, 2-15. kelime); 5:67, 5:69 ve 5:70 söz yok; REM sapması (komut 'python3 sunum/bolum4_kurallar.py 67 70 22' — A3 aralığında morph REM): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:67 've in' (9.), 've'llâhu' (15.) REM, 'fe-mâ' (12.) RSLT; 5:68 've'l-incîle' (10.), 've mâ' (11.), 've kufran' (25.) CONJ, 've le-yezîdenne' (16.) REM, 'fe-lâ' (26.) REM; "
 "5:69 've'llezîne' (4.), 've's-sâbi'ûne' (6.), 've'n-nasârâ' (7.), 've'l-yevmi' (11.), 've 'amile' (13.), 've lâ' (18.) CONJ, 'fe-lâ' (15.) RSLT; 5:70 've erselnâ' (6.), 've ferîqan' (18.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 5:67 ◈B أنس ('n-nâsi' 18. kelime — B1; anlam notu: elçinin korunduğu insanlar); 5:69 ◈K يوم ('l-yevmi' 11. kelime — K2; anlam notu: 'l-yevmi'l-âxir' — âhiret günü); 5:68 ve 5:70 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 67 70 22'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:67 (33:39), 5:69 (2:62), 5:70 (2:87) (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde ya da ölçüm xref satırında emsali buluyor — bölüm 9 kuralı 3); 5:68 D3 eşi yok; ayetler arası kalıp 'mâ unzile ileyke min rabbik' (5:67, 5:68) — sayım 'say 5:68 19-23'; blok içi tekrar (bölüm 9 kuralı 6), ardışık bağ yerine sayımla kayıt; "
 "ayetler arası kalıp 'le-yezîdenne kesîran minhum mâ unzile ileyke min rabbike tuğyânen ve kufran' (5:64, 5:68) — sayım 'say 5:68 16-25 --on'; bölüm dışı tekrar, ardışık bağ yerine sayımla kayıt; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7 — betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:67 edim geçişi şart → emir, nida, şart; şahıs geçişi 3 → 2; 5:68 edim geçişi emir, nida, şart → emir, yasak, nida; şahıs geçişi yok; 5:69 edim geçişi emir, yasak, nida → şart; şahıs geçişi 2 → 3; 5:70 edim geçişi şart → haber; şahıs geçişi 3 → 1",
 "sözdizimi (okuma; morph etiketiyle): 5:67 'yâ eyyuhe'r-rasûl' — nida (morph VOC + ATT); 'in lem tef'al' — şart (morph COND + NEG); 'fe-mâ bellağte' — şart cevabı (morph RSLT + NEG); 've'llâhu ya'simuke' — istînâf (morph REM); "
 "5:68 'lestum 'alâ şey'in hattâ tuqîmû' — olumsuz isim cümlesi ve gaye ('leyse' + 'hattâ'); 'lâ te'se' — nehy (morph PRO); 5:69 'inne'llezîne' — 'inne' ismi (morph ACC); 'men âmene' — şart, 'inne' haberi (morph COND); 'fe-lâ xavfun' — şart cevabı (morph RSLT); "
 "5:70 'le-qad exaznâ' — te'kid (morph EMPH + CERT); 'kullemâ câ'ehum' — zaman şartı (morph T); 'ferîqan kezzebû' — mef'ûl öne alınmış (okuma)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:67 'yâ eyyuhe'r-rasûl' ile açılıyor — elçiye hitap; kök بلغ ikilemesi 'belliğ' / 'bellağte' — emir ve şart cevabı; "
 "5:68 'qul yâ ehle'l-kitâb' ile açılıyor — 5:59 açılışıyla eş; 5:68 'le-yezîdenne kesîran minhum … tuğyânen ve kufran' 5:64 ile eş kalıp; 5:70 kök رسل ikilemesi 'erselnâ' / 'rusulen' / 'rasûlun' ve kök فرق ikilemesi 'ferîqan' / 'ferîqan'",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 22'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + "'; çıktı aynen): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp): 'inne'llezîne âmenû ve'llezîne hâdû' 5:69 'iman edenler, Yahudi olanlar' / 2:62 'İman edenler, Yahudi olanlar' (emsal metninde) — çakışma değil; 33:39 ve 2:87 bağları ölçüm xref lemma üçlüsüyle, kalıp eşi değil — meal karşılaştırması yazılmadı",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle): " + (MKK or 'yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 67 70 22'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:67-70 tarayıcı adayı yok; L3 / L4 adayı yok",
 "aday 1039: 5:67 ('belliğ' / 'fe-mâ bellağte'); 5:70 ('ferîqan kezzebû' / 'ferîqan yaqtulûn'); ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök بلغ 5:67 'belliğ' (emir) / 'bellağte' (olumsuz şart cevabı); kök رسل 5:67 'r-rasûl' / 'risâle' ve 5:70 'erselnâ' / 'rusulen' / 'rasûlun' — okuma",
 "bölüm: " + BOL + " bölümü, bölüm 10-1 (bölüm 7 kuralı 9 — blok_plani_5.txt'ten) — bölüm üç blok (22, 23, 24); başlıktaki 'Tebliğ emri' 5:67, 'İsrâiloğullarının misakı' 5:70; 'Mesih ve teslis' blok 23-24'te; "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b22/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9 — betikle: komut 'python3 sunum/bolum5_kurallar.py 67 70 22'; lem_bozuk.py 22 çıktısı): 5:67:3 'belliğ', 5:67:16 'ya'simu', 5:69:5 'hâdu', 5:69:20 'yahzun' — lem_bozuk bayrağı; 5:70:4 'buneyy' (sunum/ham_elle.txt) — elle ham listesi; meal maddesinde '(morph LEM ham biçim)' notlu; lemma adı listesinde notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 67 70 → AYN_SONUC; sunum/bolum4_kurallar.py 67 70 22 → KHATA_HEPSI; sunum/bolum5_kurallar.py 67 70 22 → B5_HEPSI; sunum/bolum6_kurallar.py 67 70 22 → B6_HEPSI; sunum/bolum7_kurallar.py 67 70 22 → B7_HEPSI; sunum/bolum8_kurallar.py 67 70 22 → B8_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (sunum/sonradan.py --plan 22): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('eyy', 'rasûl', 'belliğ' (morph LEM ham biçim), 'mâ', 'enzele', 'ilâ', 'min', 'rabb', 'in', 'lem', 'fe'ale', 'risâle', 'allâh', 'ya'simu' (morph LEM ham biçim), 'nâs', 'inne', 'lâ', 'hedâ' (morph LEM ham biçim), 'qavm', 'kâfir', "
 "'qâle', 'ehl', 'kitâb', 'leyse', ''alâ', 'şey'', 'eqâme', 'tevrâ', 'incîl', 'zâde', 'kesîr', 'tuğyân', 'kufr', 'te'se', 'fe-lâ', 'ellezî', 'âmene', 'hâdu' (morph LEM ham biçim), 'sâbi'', 'nasrânî', 'men', 'yevm', 'âxir', ''amile', 'sâlih', 'xavf', 'yahzun' (morph LEM ham biçim), "
 "'qad', 'exaze', 'mîsâq', 'buneyy' (morph LEM ham biçim), 'isrâ'îl', 'ersele', 'kullemâ', 'câ'e', 'hevâ', 'nefs', 'ferîq', 'kezzebe', 'qatele'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (67, 70): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_67_70.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_5_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('06', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()
GERI = open('/home/claude/yamalar/geriye_donuk_5_b21.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    AYN = (run('/home/claude/sunum/ayn_kontrol.py', '67', '70').splitlines() or ['?'])[-1]
    KUR = run('/home/claude/sunum/bolum4_kurallar.py', '67', '70', '22').splitlines()
    KH = [l for l in KUR if l.startswith('HATA')]
    B5 = run('/home/claude/sunum/bolum5_kurallar.py', '67', '70', '22').splitlines()
    B5H = [l for l in B5 if l.startswith('HATA')]
    B6 = run('/home/claude/sunum/bolum6_kurallar.py', '67', '70', '22', '--tazelik-yok').splitlines()
    B7 = run('/home/claude/sunum/bolum7_kurallar.py', '67', '70', '22').splitlines()
    B8 = run('/home/claude/sunum/bolum8_kurallar.py', '67', '70', '22').splitlines()
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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

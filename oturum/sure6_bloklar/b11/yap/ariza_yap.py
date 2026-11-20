# sûre 6 blok 11 (6:46-49) ARIZA oluşturucu — bölüm 5-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b11/olcum.txt'
os.environ['SAY2'] = '/home/claude/b11/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {}
BOL = "'Darlık ve bolluk; kulakları ve gözleri almak'"


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
 ("6:46", "'nazara keyf sarref âye'", 2, 'say 6:46 17-20', "harekesiz 'unzur keyfe nusarrifu'l-âyât' (17-20. kelime)", None),
 ("6:46", "'qâle ra'â in'", 3, 'say 6:46 1-3', "harekesiz 'qul era'eytum in' (1-3. kelime)", ('dizi 6 46 1 3', "qâle ra'â in", '1-3', "biçim farkı (dizi 6 46 1 3): 6:40 fiil çekimi, zamir eki; 6:47 fiil çekimi, zamir eki")),
 ("6:47", "'qâle ra'â in etâ 'azâb allâh'", 2, 'say 6:47 1-6', "harekesiz 'qul era'eytekum in etâkum 'azâbu'llâh' (1-6. kelime)", None),
 ("6:47", "'qâle ra'â in'", 3, 'say 6:47 1-3', "harekesiz 'qul era'eytekum in' (1-3. kelime)", ('dizi 6 47 1 3', "qâle ra'â in", '1-3', "biçim farkı (dizi 6 47 1 3): 6:40 yazım eş; 6:46 fiil çekimi, zamir eki")),
 ("6:49", "''azâb mâ kâne'", 3, 'say 6:49 5-7', "harekesiz 'l-'azâbu bi-mâ kânû' (5-7. kelime)", ('dizi 6 49 5 7', "'azâb mâ kâne", '5-7', "biçim farkı (dizi 6 49 5 7): 6:30 fiil çekimi, zamir eki; basılmamış eş yazım eş")),
 ("6:49", "'ellezî kezzebe âye'", 2, 'say 6:49 1-3', "harekesiz 've'llezîne kezzebû bi-âyâtinâ' (1-3. kelime)", None),
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

VF_YAZI = {46: {7: "'ve ebsârakum'", 8: "'ve xateme'"}, 47: {}, 48: {1: "'ve mâ'", 6: "'ve munzirîn'", 7: "'fe-men'", 9: "'ve aslaha'", 10: "'fe-lâ'", 13: "'ve lâ'"}, 49: {1: "'ve'llezîne'"}}
sys.path.insert(0, '/home/claude/b11/yap')
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
open('/home/claude/b11/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '11')
BLOKLAR = [str(i) for i in range(1, 12)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '11', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b11/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '46', '49', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b11/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b11/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '46', '49', '11').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_46_49.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:46', '6:47', '6:48', '6:49'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_46_49.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(46, 50))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:46 kök صدف ('yasdifûn' 23. kelime — yüz çevirme): tetik listesinde yok; 6:47 kök هلك ('yuhleku' 11. kelime — helâk): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '46', '49', '11')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b11/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 12)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(46, 50))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: araç değişmedi ise yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 164",
 "kök tablosu: ölçümde '???' 6:46-49 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 46 49 11'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: blokta esmâ yok (ölçüm 6:46-49); esma_el kaydı yok; "
 "lafız 6:46 ve 6:47; Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 46 49 11'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: 6:46 '{{1|fâsıla يصدفون → ن, N sınıfı}}', '{{1|harf 90 → harf3 89, isaret 1}}' ve '{{1|dış düğüm 3}}'; "
 "6:47 '{{2|fâsıla ٱلظلمون → ن, N sınıfı}}', '{{2|harf 55 → harf3 55, isaret 0}}', '{{2|dış düğüm 2}}', '{{2|İÇ düğüm 1}}', '{{2|biçim HASR}}' ve '{{2|EDİLGEN 1/4 fiil, pas z=1,10}}'; "
 "6:48 '{{3|fâsıla يحزنون → ن, N sınıfı}}', '{{3|harf 66 → harf3 65, isaret 1}}', '{{3|dış düğüm 2}}' ve '{{3|biçim HASR}}'; "
 "6:49 '{{4|fâsıla يفسقون → ن, N sınıfı}}', '{{4|harf 45 → harf3 43, isaret 2}}' ve '{{4|dış düğüm 0}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 46 49 11'): KALAN_P",
 "ölçüm aktör: 6:46-49 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:46 soru, emir, şart — COND 1 'in' (3.), IMPV 2 'qul' (1.), 'unzur' (17.), INTG 2 'era'eytum' (2.), 'men' (11.); "
 "6:47 soru, emir, şart — COND 1 'in' (3.), IMPV 1 'qul' (1.), INTG 2 'era'eytekum' (2.), 'hel' (10.), RES 1 'illâ' (12.); 6:48 şart — COND 1 'men' (7.), NEG 3 'mâ' (1.), 'lâ' (10.), 'lâ' (13.), RES 1 'illâ' (4.); 6:49 haber — kip yok; "
 "morph REM ('fe' 6:48 7.), RSLT ('fe' 6:48 10.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:46-49 yıldız yok",
 "fâsıla: 6:45 ن → 6:46 ن (يصدفون) → 6:47 ن (ٱلظلمون) → 6:48 ن (يحزنون) → 6:49 ن (يفسقون) — N sınıfı sürüyor; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:46 28:71 (emsal olarak basıldı) ve okunmuş 2 ayet; 6:47 6:40 (basılmış) ve okunmuş 2 ayet; 6:48 18:56 (emsal olarak basıldı) ve okunmamış 1 ayet; 6:49 yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:46 'nazara keyf sarref âye' ve 'qâle ra'â in' süzgeç GEÇER; 6:47 'qâle ra'â in etâ 'azâb allâh' ve 'qâle ra'â in' GEÇER; 6:49 ''azâb mâ kâne' GEÇER, 'ellezî kezzebe âye' GEÇMEZ; "
 "6:48 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; edilgen fiilde naib-i faili zamir 'adsız' ile — sûre 6 bölüm 2 denetimi kuralı 5; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; gönderge rol adıyla yazılmaz — sûre 6 bölüm 4 denetimi kuralı 4): "
 "6:46 muhatap 2MS, muhatap 2MP (söz içi), 3MS ('exaze' 4. kelime — fail 5. kelime; zamirler adsız — gönderge lafız, 'ilâhun' ve 'sem'akum'), konuşan 1P, 3MP (adsız — gönderge 6:33 11. kelime); "
 "6:47 muhatap 2MS, muhatap 2MP (söz içi), 3MS ('etâkum' 4. kelime — fail 5. kelime; 'yuhleku' edilgen — naib-i faili 'l-qavmu' 13. kelime); "
 "6:48 konuşan 1P, 3MS (adsız — gönderge 'men' 7. kelime), 3MP (adsız — gönderge 'men' 7. kelime); "
 "6:49 3MP (adsız — gönderge 'llezîne'), konuşan 1P, 3MS ('yemessuhumu' 4. kelime — fail 5. kelime) — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): "
 "6:46 'qul' (1.) ardından söz 2-16. kelime — ayet içi kapanış; 17-23. kelime ('unzur', IMPV 2MS) söz dışı; 6:47 'qul' (1.) ardından söz 2-14. kelime — ayet içi kapanış; 6:48 ve 6:49 söz yok; mealde tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 46 49 11' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 6:46 've ebsârakum' (7.), 've xateme' (8.) CONJ; 6:48 've mâ' (1.), 've munzirîn' (6.), 've aslaha' (9.), 've lâ' (13.) CONJ, 'fe-men' (7.) REM, 'fe-lâ' (10.) RSLT; 6:49 've'llezîne' (1.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:46 ◈B سمع ('sem'akum' 6. kelime — B3); 6:46 ◈B بصر ('ebsârakum' 7. kelime — B3); 6:46 ◈B قلب ('qulûbikum' 10. kelime — B3; anlam notu: işitme, görme ve kalbin alınması)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 46 49 11'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:46 (28:71); 6:48 (18:56); 6:47 ve 6:49 D3 eşi yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "ayetler arası kalıp 'qul era'eyt' (6:46, 6:47) — sayım 'dizi 6 46 1 3', 'dizi 6 47 1 3'; blok içi tekrar (bölüm 9 kuralı 6), ardışık bağ yerine sayımla kayıt; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:46 şart → cevap ('in' 3. kelime / 'men ilâhun' 11. kelime), söz açılır / kapanır, şahıs geçişi 3 → 2, edim geçişi haber → soru, emir, şart; 6:47 şart → cevap ('in' 3. kelime / 'hel yuhleku' 10. kelime), söz açılır / kapanır, şahıs geçişi yok; 6:48 şart → cevap ('men' 7. kelime / 'fe-lâ xavfun' 10. kelime), şahıs geçişi 2 → 3, edim geçişi soru, emir, şart → şart; 6:49 şahıs geçişi yok, edim geçişi şart → haber, bölüm kapanışı; "
 "şahıs beraberliği yok (sûre 6 bölüm 1 denetimi kuralı 9); ölçüm iltifât 6:46-49 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:46 'era'eytum' — soru (morph INTG); 'in exaze'llâhu … men ilâhun' — şart ve soru cümlesi (morph COND + INTG); 'unzur keyfe' — emir ve soru zarfı (morph IMPV); "
 "6:47 'hel yuhleku illa'l-qavmu' — soru ve hasr (morph INTG + RES); 6:48 've mâ … illâ' — hasr (morph CONJ + NEG + RES); 'fe-men … fe-lâ' — istînâf, şart ve cevabı (morph REM + COND + RSLT); "
 "6:49 've'llezîne' — atıf (morph CONJ); 'bi-mâ kânû' — sebep (morph P + REL)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:46 'men ilâhun ğayru'llâhi ye'tîkum' — 28:71 ile eş (sayım: 'say 6:46 11-15'); 6:46 kök أله ikilemesi; "
 "6:48 've mâ nursilu'l-murselîne illâ mubeşşirîne ve munzirîn' — 18:56 ile eş (sayım: 'say 6:48 1-6'); 6:48 kök رسل ikilemesi; 6:48 'fe-men âmene' / 6:49 've'llezîne kezzebû' karşıtlığı",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 11'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 "'men ilâhun ğayru'llâhi ye'tîkum' 6:46 'Allah'tan başka hangi ilâh onu size getirebilir' / 28:71 'Allah'tan başka hangi ilâh size bir ışık getirebilir' (emsal metninde) — çakışma — tam okuma sonu ('onu' / 'bir ışık' — kalıp dışı nesne); "
 "'qâle ra'â in' 6:46 'Bana haber verin' / 28:71 'Söyleyin bakalım' (emsal metninde) — çakışma — tam okuma sonu ('haber ver-' / 'söyle-' — soru deyimi); "
 "'ve mâ nursilu'l-murselîne illâ mubeşşirîne ve munzirîn' 6:48 'Biz elçileri ancak müjdeleyici ve uyarıcı olarak göndeririz' / 18:56 'Biz elçileri ancak müjdeleyici ve uyarıcı olarak göndeririz' (emsal metninde) — çakışma değil; "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:46 'qul' IMPV — meal 'De'; 'ra'eytum' PERF (soru) — meal 'haber verin'; 'exaze', 'xateme' PERF (şart) — meal 'alsa', 'mühürlese'; 'ye'tî' IMPF IND — meal 'getirebilir'; 'unzur' IMPV — meal 'Bak'; 'nusarrifu' IMPF IND — meal 'açıklıyoruz'; 'yasdifûn' IMPF IND — meal 'çeviriyorlar'; "
 "6:47 'qul' IMPV — meal 'De'; 'ra'eyte' PERF (soru) — meal 'haber verin'; 'etâ' PERF (şart) — meal 'gelse'; 'yuhleku' IMPF IND edilgen — meal 'helâk edilir'; "
 "6:48 'nursilu' IMPF IND — meal 'göndeririz'; 'âmene', 'aslaha' PERF (şart) — meal 'iman eder', 'düzeltirse'; 'yahzenûn' IMPF IND — meal 'üzülmezler'; "
 "6:49 'kezzebû' PERF — meal 'yalanlayanlar'; 'yemessu' IMPF IND — meal 'dokunacaktır'; 'kânû' PERF + 'yefsuqûn' IMPF IND — meal 'çıkmakta olmaları'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 46 49 11'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:46, 6:47, 6:48 ve 6:49 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:46 ('exaze'llâhu' / 'ye'tîkum bih'; 'nusarrifu'l-âyât' / 'yasdifûn'); 6:47 ('bağteten' / 'cehreten'); 6:48 ('mubeşşirîne' / 'munzirîn'); 6:49 yok; "
 "ayetler arası 6:48 / 6:49 ('fe-men âmene' / 've'llezîne kezzebû'); eşleme betikle: ADAY_P",
 "aday 1041: kök أخذ 6:42 ('fe-exaznâhum'), 6:44 ('exaznâhum') ve 6:46 ('exaze'); kök قلب 6:43 ('qulûbuhum') ve 6:46 ('qulûbikum'); kök بغت 6:44 ('bağteten') ve 6:47 ('bağteten'); kök عذب 6:47 ve 6:49; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 5-2 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm iki blok (10, 11); bu blok bölümü kapatıyor; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b11/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 46 49 11'; lem_bozuk.py 11 çıktısı): lem_bozuk bayrağı 6:46 19. kelime صَرَّفْ, 6:48 15. kelime يَحْزُن — meal maddelerinde (morph LEM ham biçim) notu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 46 49 → AYN_SONUC; sunum/bolum4_kurallar.py 46 49 11 → KHATA_HEPSI; sunum/bolum5_kurallar.py 46 49 11 → B5_HEPSI; sunum/bolum6_kurallar.py 46 49 11 → B6_HEPSI; sunum/bolum7_kurallar.py 46 49 11 → B7_HEPSI; sunum/bolum8_kurallar.py 46 49 11 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 46 49 11 → B9_HEPSI; sunum/bolum10_kurallar.py 46 49 11 → B10_HEPSI; sunum/bolum11_kurallar.py 46 49 11 → B11_HEPSI; sunum/bolum12_kurallar.py 46 49 11 → B12_HEPSI; sunum/bolum13_kurallar.py 46 49 11 → B13_HEPSI; sunum/bolum14_kurallar.py 46 49 11 → B14_HEPSI; sunum/bolum15_kurallar.py 46 49 11 → B15_HEPSI; sunum/bolum16_kurallar.py 46 49 11 → B16_HEPSI; sunum/bolum17_kurallar.py 46 49 11 → B17_HEPSI; sunum/bolum18_kurallar.py 46 49 11 → B18_HEPSI; sunum/bolum19_kurallar.py 46 49 11 → B19_HEPSI; sunum/bolum20_kurallar.py 46 49 11 → B20_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 11 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('nazara', 'keyf', 'âye', 'qâle', 'ra'â', 'in', 'etâ', ''azâb', 'allâh', 'mâ', 'kâne', 'ellezî', 'kezzebe', 'sarref' (morph LEM ham biçim)); lemmasız öğe joker yok; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (46, 49): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_46_49.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b09.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '46', '49'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '46', '49', '11'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '46', '49', '11'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '46', '49', '11', '--tazelik-yok')}
    for _n in range(7, 21): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '46', '49', '11')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20 = [_R['B%d' % _n].splitlines() for _n in range(6, 21)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20): print([l for l in _x if l.startswith('HATA') or 'hata' in l])

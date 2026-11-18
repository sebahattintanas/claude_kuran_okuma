# blok 34 (5:111-115) ARIZA oluşturucu — bölüm 15-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b34/olcum.txt'
os.environ['SAY2'] = '/home/claude/b34/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
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
 ("5:112", "'itteqâ allâh in kâne mu'min'", 2, 'say 5:112 17-21', "harekesiz 'ttequ'llâhe in kuntum mu'minîn' (17-21. kelime)", ('dizi 5 112 17 21', "itteqâ allâh in kâne mu'min", '17-21', "biçim farkı (dizi 5 112 17 21): basılmamış eş önek")),
 ("5:112", "''alâ mâ'ide min semâ''", 2, 'say 5:112 12-15', "harekesiz ''aleynâ mâ'ideten mine's-semâ'' (12-15. kelime)", None),
 ("5:112", "'itteqâ allâh in'", 6, 'say 5:112 17-19', "harekesiz 'ttequ'llâhe in' (17-19. kelime; biçim öğesi 'in' — ölçüm kalıbı harekesiz 'ان' ile 'in' / 'inne' / 'en' ayırmıyor; ◇ lemma dizisi 'dizi 5 112 17 19' sûre içi 2, nakarat 6)", ('dizi 5 112 17 19', "itteqâ allâh in", '17-19', "biçim farkı (dizi 5 112 17 19): basılmamış eş önek; öneksiz eş koşusu (dizi 5 112 17 19): basılmamış eş → önek kesilmiş sûre içi 5")),
 ("5:112", "'in kâne mu'min'", 3, 'say 5:112 19-21', "harekesiz 'in kuntum mu'minîn' (19-21. kelime)", None),
 ("5:112", "''îsâ ibn meryem'", 3, 'say 5:112 4-6', "harekesiz 'yâ 'îse'bne meryem' (4-6. kelime; biçim öğesi 'yâ' — nida öneki harekesiz kalıpta; ◇ lemma dizisi 'dizi 5 112 4 6' sûre içi 6, harekesiz kalıp 3)", None),
 ("5:114", "''alâ mâ'ide min semâ''", 2, 'say 5:114 8-11', "harekesiz ''aleynâ mâ'ideten mine's-semâ'' (8-11. kelime)", None),
 ("5:114", "''îsâ ibn meryem'", 2, 'say 5:114 2-4', "harekesiz ''îse'bnu meryem' (2-4. kelime; biçim öğesi 'ibn' — ölçüm kalıbı i'râb ve önek eşlerini ayırıyor; ◇ lemma dizisi 'dizi 5 114 2 4' sûre içi 6, nakarat 2)", ('dizi 5 114 2 4', "'îsâ ibn meryem", '2-4', "biçim farkı (dizi 5 114 2 4): basılmamış eş i'râb, önek; 5:78 i'râb, önek; 5:110 i'râb, önek; 5:112 i'râb, önek; basılmamış eş i'râb, önek; öneksiz eş koşusu (dizi 5 114 2 4): basılmamış eş → önek kesilmiş sûre içi 1; 5:78 → önek kesilmiş sûre içi 1; 5:110 → önek kesilmiş sûre içi 3; 5:112 → önek kesilmiş sûre içi 3; basılmamış eş → önek kesilmiş sûre içi 3")),
 ("5:115", "'qâle allâh inne'", 2, 'say 5:115 1-3', "harekesiz 'qâle'llâhu innî' (1-3. kelime)", ('dizi 5 115 1 3', "qâle allâh inne", '1-3', "biçim farkı (dizi 5 115 1 3): basılmamış eş önek")),
 ("5:115", "'fe-men kefera ba'd'", 2, 'say 5:115 6-8 --on', "harekesiz 'fe-men yekfur ba'd' (6-8. kelime)", ('dizi 5 115 6 8', "fe-men kefera ba'd", '6-8', "biçim farkı (dizi 5 115 6 8): basılmamış eş yazım eş")),
 ("5:115", "'ehad min 'âlem'", 2, 'say 5:115 15-17', "harekesiz 'ehaden mine'l-'âlemîn' (15-17. kelime)", None),
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

VF_YAZI = {111: {1: "'ve iz'", 8: "'ve bi-rasûlî'", 11: "'ve'şhed'"}, 113: {6: "'ve tatma'inne'", 8: "'ve na'leme'", 12: "'ve nekûne'"}, 114: {16: "'ve âxirinâ'", 17: "'ve âyeten'", 19: "'ve'rzuqnâ'", 20: "'ve ente'"}, 115: {6: "'fe-men'", 10: "'fe-innî'"}}
sys.path.insert(0, '/home/claude/b34/yap')
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
open('/home/claude/b34/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '34')
BLOKLAR = [str(i) for i in range(1, 35)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '34', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b34/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '111', '115', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b34/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b34/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '111', '115', '34').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_111_115.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'5:111', '5:112', '5:113', '5:114', '5:115'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_111_115.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '5:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '5:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(111, 116))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "5:111 'iz' (1. kelime — morph T, zaman); 5:112 'iz' (1. kelime — morph T, zaman); 5:114 kök أخر ('âxirinâ' 16. kelime — sonraki): tetik listesinde yok; 5:115 kök بعد ('ba'du' 8. kelime — morph T, sonra): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
# blok 34 commit'inden sonraki esmâ düzeltmesi yeniden koşusu: araç farkı blok 33 commit'ine (2f1e117) göre — arac_degisim'in ilk koşu çıktısı
ARAC = 'değişen araçlar (repo HEAD ile fark): sunum/bolum13_kurallar.py, sunum/bolum5_kurallar.py, sunum/kelime_kontrol.py, sunum/mutasyon_sina.py, sunum/yasakli.sh; sunum/sinifla.py (SON 115); sunum/basilan.txt +7'
EMH = run('/home/claude/sunum/esma_muhur.py', '111', '115', '34')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b34/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 35)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b5:%d:\d+' % a_, s_) for a_ in range(111, 116))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: blok akışı (sunum/sinifla.py SON, sunum/basilan.txt — §3 adım 2 ve emsal işaretlemesi); "
 "sunum/bolum5_kurallar.py '-dir' taraması emir kipindeki fiil kökünü ('indir', 'rızıklandır' — meal maddesinde 'X-' karşılığı) ek saymıyor (bölüm 5 kuralı 9 yanlış pozitifi); sunum/bolum5_kurallar.py 'fe-' / 've-' önekli kalıp öğesini önek dışında LEM'e bağlıyor (bölüm 5 kuralı 5 ile bölüm 7 kuralı 12 çelişkisi — 'fe-men') ve say2 anahtarı alıntısını ('dizi …' — bölüm 14 denetimi kuralı 8) ortak kalıp saymıyor (bölüm 6 kuralı 5); "
 "sunum/bolum13_kurallar.py kural 11 ''X olan' 'AR' açılımı' biçimini tanıyor ('teslim olan' 'muslim' — bölüm 13 denetimi kuralı 11 yanlış pozitifi); "
 "sunum/kelime_kontrol.py zamir anahtarlarına ayrık 2MS 'ente' (kelime_kontrol kural 12 — 5:114 've ente'); sunum/yasakli.sh IZIN listesine gloss_tara çıktısındaki أول kök anlamı (bölüm 10 denetimi kuralı 10 — yeni izin dosyaya özgü ve tırnaklı); sunum/mutasyon_sina.py bu düzeltmelerin sınamaları (bölüm 5 kuralları 5 ve 9, bölüm 6 kuralı 5, bölüm 13 denetimi kuralı 11 ve kelime_kontrol kural 12: düzeltilmiş araçta isabet yok, istisna / regex geri alınınca isabet); mutasyon_sina — MUT_SONUC; "
 "geriye dönük koşu son araç değişikliğinden sonra yeniden üretildi (GERI_P); yeni 14 — basılan değişti 13 (bu bloğun ayetleri basıldı: blok 05, 19, 22, 25 ve 31 kayıtlarının xref / R5 sınıflaması), gloss_tara KAPSAMAYAN 1 (blok 33 kapsam sayımı, TARANMAYAN değil); düşen 10 — araç değişti 6 (sinifla SON), basılan değişti 4; kayıtlar geriye dönük yeniden yazılmadı",
 "kök tablosu: ölçümde '???' 5:111, 5:112, 5:113, 5:114 ve 5:115 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 111 115 34'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:112 'mu'minîn' (21. kelime) — esma_el 'degil', kural 'çoğul insan göndergeli' (inananlar); 5:114 'li-evvelinâ' (15. kelime) ve 'âxirinâ' (16. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (öncekilerimiz ve sonrakilerimiz — bizim sıfatımız) — 15. kelime ölçüm esmâ alanında yok, esma_kayit e_oto listesinde; "
 "5:115 'ehaden' (15. kelime) — esma_el 'degil', kural 'olumsuz nekre ehad' (hiç kimse); 5:111 ve 5:113 esmâ yok;  lafız 5:112 ve 5:115; Rab 5:112 ve 5:114 (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 111 115 34'; bölüm 13 denetimi kuralı 2: esma_el eklendikten sonra): " + EMH,
 "ölçüm: 5:111 '{{1|fâsıla مسلمون → ن, N sınıfı}}', '{{1|simetri \\[3, 1, 5, 1\\]}}', '{{1|harf 65 → harf3 62, isaret 3}}' ve '{{1|dış düğüm 1}}'; "
 "5:112 '{{2|fâsıla مؤمنين → ن, N sınıfı}}', '{{2|simetri \\[3, 4, 10, 1\\]}}', '{{2|harf 88 → harf3 85, isaret 3}}', '{{2|dış düğüm 4}}' ve '{{2|İÇ düğüm 1}}'; "
 "5:113 '{{3|fâsıla ٱلشهدين → ن, N sınıfı}}', '{{3|simetri \\[3, 9, 13, 1\\]}}', '{{3|harf 66 → harf3 65, isaret 1}}' ve '{{3|dış düğüm 0}}'; "
 "5:114 '{{4|fâsıla ٱلرزقين → ن, N sınıfı}}', '{{4|simetri \\[3, 2, 8, 1\\]}}', '{{4|harf 102 → harf3 98, isaret 4}}' ve '{{4|dış düğüm 0}}'; "
 "5:115 '{{5|fâsıla ٱلعلمين → ن, N sınıfı}}', '{{5|mm2: \\[11, عذب}}', '{{5|sayı işareti أَحَد}}', '{{5|simetri \\[3, 5, 9, 1\\]}}', '{{5|harf 74 → harf3 69, isaret 5}}' ve '{{5|dış düğüm 0}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 111 115 34'): KALAN_P",
 "ölçüm aktör: 5:111, 5:113 ve 5:115 aktör yok; 5:112 '{{2|adlı عِيسَى 4\\. sırada \\(kisi, rol meful\\+muhatap\\)}}' — münadâ ve söz muhatabı; '{{2|adlı مَرْيَم 6\\. sırada \\(kisi, rol mecrur\\)}}' — 'ibn' muzâfun ileyhi; "
 "5:114 '{{4|adlı عِيسَى 2\\. sırada \\(kisi, rol fail\\+konusan\\)}}' — 'qâle' faili ve söz sahibi; '{{4|adlı مَرْيَم 4\\. sırada \\(kisi, rol mecrur\\)}}' — 'ibn' muzâfun ileyhi; '{{4|adlı \\S+ 5\\. sırada \\(diger, rol meful\\)}}' — münadâ ('llâhumme')",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 5:111 emir — IMPV 2 'âminû' (6.), 've'şhed' (11.); "
 "5:112 soru, emir, nida, şart — VOC 1 'yâ' (4.), INTG 1 'hel' (7.), IMPV 1 'ttequ' (17.), COND 1 'in' (19.); 5:113 haber — CERT 1 'qad' (10.); "
 "5:114 emir, nida — VOC 1 'llâhumme' (5.; mîm eki), IMPV 2 'enzil' (7.), 've'rzuqnâ' (19.); 5:115 şart — COND 1 'fe-men' (6.), NEG 1 'lâ' (13.); "
 "morph REM ('ve' 5:111 11., 5:114 20.; 'fe' 5:115 6.), RSLT ('fe' 5:115 10.), INT ('en' 5:111 5.), SUB ('en' 5:112 10., 5:113 3. ve 9.) ve T ('iz' 5:111 1., 5:112 1.; 'ba'du' 5:115 8.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 5:111, 5:112, 5:113, 5:114 ve 5:115 yıldız yok",
 "fâsıla: 5:110 ن (مبين) → 5:111 ن (مسلمون) → 5:112 ن (مؤمنين) → 5:113 ن (ٱلشهدين) → 5:114 ن (ٱلرزقين) → 5:115 ن (ٱلعلمين); blok boyunca ن sınıfı, kafiye kırılması yok; 5:111, 5:112, 5:113 ve 5:115 çoğul ortaç / çoğul adla kapanıyor; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1 — basılmış hedefler numarasıyla, basılmamışlar sinifla sayısıyla): 5:111 okunmuş 1 ayet; 5:112 okunmuş 5 ayet; 5:113 xref yok; 5:114 xref yok; 5:115 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:112 'itteqâ allâh in kâne mu'min', ''alâ mâ'ide min semâ'', 'itteqâ allâh in', 'in kâne mu'min' ve ''îsâ ibn meryem' süzgeç GEÇER; "
 "5:114 ''alâ mâ'ide min semâ'' GEÇER, ''îsâ ibn meryem' GEÇMEZ; 5:115 'qâle allâh inne', 'fe-men kefera ba'd' ve 'ehad min 'âlem' GEÇMEZ",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "fail olmayan mecrur çoğul ad ve mecrur ilgi zamiri A1'de yazılmaz — bölüm 11 denetimi kuralları 16 ve 19; fiilden önce gelen lafız 'mübtedâ' — bölüm 12 denetimi kuralı 11; edilgen fiilde 'naib-i faili' — bölüm 11 denetimi kuralı 17; A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5): "
 "5:111 konuşan 1S (adsız; söz içi — Allah'ın 5:110'dan süren sözü), muhatap 2MP (adsız; söz içi), 3MP (adsız; söz içi — 'qâlû'), konuşan 1P (adsız; söz içi), muhatap 2MS (adsız; söz içi); "
 "5:112 'l-havâriyyûne' ('qâle' faili), 'yâ 'îse' (münadâ; adlı), 'rabbuke' ('yestetî'u' faili), muhatap 2MS (adsız; söz içi), 3MS (adsız; söz içi — 'yunezzile'), konuşan 1P (adsız; söz içi), 3MS (adsız — 'qâle' 16.), muhatap 2MP (adsız; söz içi); "
 "5:113 3MP (adsız — 'qâlû'), konuşan 1P (adsız; söz içi), 3FS (adsız; söz içi — 'minhâ', ''aleyhâ'), 'qulûbunâ' ('tatma'inne' faili), muhatap 2MS (adsız; söz içi); "
 "5:114 ''îse'bnu' ('qâle' faili; adlı), 'llâhumme' (münadâ), muhatap 2MS (adsız; söz içi), konuşan 1P (adsız; söz içi), 3FS (adsız; söz içi — 'tekûnu'); "
 "5:115 Allah (lafız; 'qâle' faili), konuşan 1S (adsız; söz içi), 3FS (adsız; söz içi — 'munezziluhâ'), muhatap 2MP (adsız; söz içi), 3MS (adsız; söz içi — 'yekfur', 'u'azzibuhû'); "
 "'l-havâriyyîne' (5:111 4. kelime), 'mine's-semâ'i' (5:112 15. ve 5:114 11. kelime), 'mine'ş-şâhidîn' (5:113 15. kelime), 'r-râziqîn' (5:114 22. kelime) ve 'mine'l-'âlemîn' (5:115 17. kelime) — mecrur — A1'de yazılmadı — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4 — söz yalnız قول fiilinden sonra): 5:111 Allah'ın 5:110'da açılan sözü sürüyor ('evhaytu' 1S — 1-13. kelime), içinde 'qâlû' (9.) ardından iç söz 10-13. kelime; "
 "'en âminû bî ve bi-rasûlî' (5-8. kelime) vahyin içeriği — söz biçimli içerik ('evhaytu' وحي fiili, قول değil); "
 "5:112 'qâle' (2.) ardından söz 4-15. kelime, 'qâle' (16.) ardından söz 17-21. kelime; 5:113 'qâlû' (1.) ardından söz 2-15. kelime; 5:114 'qâle' (1.) ardından söz 5-22. kelime; 5:115 'qâle' (1.) ardından söz 3-17. kelime; "
 "mealde tırnaksız, iki nokta ile (blok meal biçimi; emsal mealleri tırnaklı — biçim farkı, kayıt); A3'te ve A4'te 'söz açılır' / 'söz sürüyor' / 'söz kapanır'; 'qul' yok (bölüm 10 denetimi kuralı 8); "
 "geriye dönük kayıt: blok 33'te 5:110 A4 'söz kapanır (63. kelime, ayet içi)' yazıldı — 5:111 'evhaytu' (1S) sözün sürdüğünü gösteriyor; basılmış metin değiştirilmedi — tam okuma sonu; "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 111 115 34' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "REM sapması 5:111 (11. kelime) — 've'şhed' söz içinde istînâf: iman beyanından sonra yeni emir cümlesi, meal noktalı virgülle ayırıyor; "
 "REM sapması 5:114 (20. kelime) — 've ente' söz içinde istînâf: dua cümlelerinden sonra isim cümlesi, meal noktalı virgülle ayırıyor; "
 "REM sapması 5:115 (6. kelime) — 'fe-men' söz içinde istînâf: vaatten sonra şart cümlesi, meal noktalı virgülle ayırıyor; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:111 've iz' (1.), 've bi-rasûlî' (8.) CONJ, 've'şhed' (11.) REM; 5:113 've tatma'inne' (6.), 've na'leme' (8.), 've nekûne' (12.) CONJ; "
 "5:114 've âxirinâ' (16.), 've âyeten' (17.), 've'rzuqnâ' (19.) CONJ, 've ente' (20.) REM; 5:115 'fe-men' (6.) REM, 'fe-innî' (10.) RSLT",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 5:112 ◈K سمو ('s-semâ'i' 15. kelime — K1; anlam notu: sofranın inişi istenen yer); "
 "5:113 ◈B قلب ('qulûbunâ' 7. kelime — B3; anlam notu: yatışması istenen kalpler); 5:114 ◈K سمو ('s-semâ'i' 11. kelime — K1; anlam notu: duada sofranın inişi istenen yer)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 111 115 34'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:112 (3:52, 61:14); 5:111, 5:113, 5:114 ve 5:115 D3 eşi yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "ayetler arası kalıp ''aleynâ mâ'ideten mine's-semâ'i' (5:112, 5:114) — lemma dizisi 'dizi 5 112 12 15' / 'dizi 5 114 8 11'; ayetler arası kalıp ''îse'bn' (5:112, 5:114) — lemma dizisi 'dizi 5 112 4 6' / 'dizi 5 114 2 4'; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11); "
 "5:111 / 3:52 lemma eşi 'dizi 5 111 11 13' (okuma — bağ kurulmadı: harekesiz kalıp 'bi-ennenâ' / 'bi-ennâ' yazımıyla ayrışıyor)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:111 söz sürüyor / kapanır (13. kelime, ayet içi); edim geçişi emir, nida → emir; 5:112 söz açılır / kapanır (4-15. ve 17-21. kelime); edim geçişi emir → soru, emir, nida, şart; şart → cevap (cevap mahzuf); "
 "5:113 söz açılır / kapanır (2-15. kelime); edim geçişi soru, emir, nida, şart → haber; 5:114 söz açılır / kapanır (5-22. kelime); edim geçişi haber → emir, nida; 5:115 söz açılır / kapanır (3-17. kelime); bölüm kapanışı; edim geçişi emir, nida → şart; şart → cevap (ayet içi)",
 "sözdizimi (okuma; morph etiketiyle): 5:111 've iz evhaytu' — atıf ve zaman (morph CONJ + T); 'en âminû' — açıklama edatı (morph INT); 've'şhed' — istînâf, emir (morph REM + IMPV); 'bi-ennenâ' — tekit (morph ACC); "
 "5:112 'iz qâle' — zaman (morph T); 'yâ 'îse'bne meryem' — nida (morph VOC); 'hel yestetî'u' — soru (morph INTG); 'en yunezzile' — masdar edatı (morph SUB); 'in kuntum' — şart (morph COND; cevap mahzuf); "
 "5:113 'en ne'kule', 'en qad sadaqtenâ' — masdar edatı (morph SUB); 'qad' — tahkik (morph CERT); 5:114 'llâhumme' — nida (mîm eki, morph VOC); 've ente xayru'r-râziqîn' — istînâf (morph REM); "
 "5:115 'innî' — tekit (morph ACC); 'fe-men yekfur' — şart (morph REM + COND); 'fe-innî' — cevap (morph RSLT); 'lâ u'azzibuhû' — olumsuzluk (morph NEG)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:111 've iz evhaytu ile'l-havâriyyîn' ile açılıyor; 5:111 kök أمن ikilemesi ('âminû' 6. / 'âmennâ' 10. kelime); "
 "5:112 kök قول ikilemesi ('qâle' 2. / 'qâle' 16. kelime); 5:114 kök رزق ikilemesi ('ve'rzuqnâ' 19. / 'r-râziqîn' 22. kelime); 5:115 kök عذب üçlemesi ('u'azzibuhû' 11., ''azâben' 12. ve 'u'azzibuhû' 14. kelime); "
 "5:112 ve 5:114 ''aleynâ mâ'ideten mine's-semâ'' — istek ve dua eş kalıpla (sayım: 'say 5:112 12-15')",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 34'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit): 'qâle'l-havâriyyûn' 5:112 'havariler demişti' / 3:52 'Havârîler' (emsal metninde) — çakışma değil; "
 "'qâle'l-havâriyyûn' 5:112 'havariler demişti' / 61:14 'havarilerin de' (emsal metninde) — çakışma değil",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): 'iz' — çakışma değil (5:110, 5:111 ve 5:112 'Hani'); 'î' — çakışma değil (5:110 'benim', 5:111 'Bana', 5:115 'ben' — durum eki farkı)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 111 115 34'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:112 tarayıcı adayı (kök سمو; A_şart) — çıpa değil: gök anması istek bağlamı, doğa iddiası yok (olgu=False); 5:111, 5:113, 5:114 ve 5:115 tarayıcı vermedi (cipa_tarama5_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: ayet içi 5:114 ('li-evvelinâ' / 've âxirinâ') — okuma (önceki / sonraki kuşak); 5:111, 5:112, 5:113 ve 5:115 yok; ayetler arası yok; eşleme betikle: ADAY_P",
 "aday 1041: kök نزل 5:112 ('yunezzile'), 5:114 ('enzil') ve 5:115 ('munezziluhâ') — istek, dua ve vaat bağı; kök ميد 5:112 ve 5:114 ('mâ'ideten'); kök قول blok boyunca söz açıcı; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 15-2 (bölüm 7 kuralı 9 — blok_plani_5.txt'ten) — bölüm iki blok (33, 34); bu blok bölümü kapatıyor; başlıktaki 'havariler ve sofra' 5:111-115; "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b34/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 111 115 34'; lem_bozuk.py 34 çıktısı): lem_bozuk bayrağı yok; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 111 115 → AYN_SONUC; sunum/bolum4_kurallar.py 111 115 34 → KHATA_HEPSI; sunum/bolum5_kurallar.py 111 115 34 → B5_HEPSI; sunum/bolum6_kurallar.py 111 115 34 → B6_HEPSI; sunum/bolum7_kurallar.py 111 115 34 → B7_HEPSI; sunum/bolum8_kurallar.py 111 115 34 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 111 115 34 → B9_HEPSI; sunum/bolum10_kurallar.py 111 115 34 → B10_HEPSI; sunum/bolum11_kurallar.py 111 115 34 → B11_HEPSI; sunum/bolum12_kurallar.py 111 115 34 → B12_HEPSI; sunum/bolum13_kurallar.py 111 115 34 → B13_HEPSI; sunum/bolum14_kurallar.py 111 115 34 → B14_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme: ariza_5_111_115.txt için gloss_tara çıktısındaki أول kök anlamı, tırnaklı (araç çıktısı aynen; bölüm 10 denetimi kuralı 10)",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 34 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('itteqâ', 'allâh', 'in', 'kâne', 'mu'min', ''alâ', 'mâ'ide', 'min', 'semâ'', ''îsâ', 'ibn', 'meryem', 'qâle', 'inne', 'men', 'fe-men', 'kefera', 'ba'd', 'ehad', ''âlem', 'şehide', 'enne', 'muslim'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (111, 115): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_111_115.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_5_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('06', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()
GERI = open('/home/claude/yamalar/geriye_donuk_5_b34.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    AYN = (run('/home/claude/sunum/ayn_kontrol.py', '111', '115').splitlines() or ['?'])[-1]
    KUR = run('/home/claude/sunum/bolum4_kurallar.py', '111', '115', '34').splitlines()
    KH = [l for l in KUR if l.startswith('HATA')]
    B5 = run('/home/claude/sunum/bolum5_kurallar.py', '111', '115', '34').splitlines()
    B5H = [l for l in B5 if l.startswith('HATA')]
    B6 = run('/home/claude/sunum/bolum6_kurallar.py', '111', '115', '34', '--tazelik-yok').splitlines()
    B7 = run('/home/claude/sunum/bolum7_kurallar.py', '111', '115', '34').splitlines()
    B8 = run('/home/claude/sunum/bolum8_kurallar.py', '111', '115', '34').splitlines()
    B9 = run('/home/claude/sunum/bolum9_kurallar.py', '111', '115', '34').splitlines()
    B10 = run('/home/claude/sunum/bolum10_kurallar.py', '111', '115', '34').splitlines()
    B11 = run('/home/claude/sunum/bolum11_kurallar.py', '111', '115', '34').splitlines()
    B12 = run('/home/claude/sunum/bolum12_kurallar.py', '111', '115', '34').splitlines()
    B13 = run('/home/claude/sunum/bolum13_kurallar.py', '111', '115', '34').splitlines()
    B14 = run('/home/claude/sunum/bolum14_kurallar.py', '111', '115', '34').splitlines()
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

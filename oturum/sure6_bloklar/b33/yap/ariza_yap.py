# sûre 6 blok 33 (6:139-141) ARIZA oluşturucu — bölüm 16-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b33/olcum.txt'
os.environ['SAY2'] = '/home/claude/b33/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {}
BOL = "'Ekinlerde ve hayvanlarda pay; sekiz eş'"


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
 ("6:139", "'in kâne meyte'", 2, 'say 6:139 12-14', "harekesiz 've in yekun meyteten' (12-14. kelime)", ('dizi 6 139 12 14', 'in kâne meyte', '12-14', 'biçim farkı (dizi 6 139 12 14): sûre içi eş yok; öneksiz eş koşusu (dizi 6 139 12 14): sûre içi eş yok')),
 ("6:140", "'qad xasira ellezî'", 2, 'say 6:140 1-3', "harekesiz 'qad xasira'llezîne' (1-3. kelime)", None),
 ("6:141", "'_ ellezî enşe'e'", 2, 'say 6:141 1-3', "harekesiz 've huve'llezî enşe'e' (1-3. kelime)", ('dizi 6 141 1 3', "_ ellezî enşe'e", '1-3', 'biçim farkı (dizi 6 141 1 3): 6:98 zamir eki; öneksiz eş koşusu (dizi 6 141 1 3): 6:98 → önek kesilmiş sûre içi 1')),
 ("6:141", "'semer izâ esmera'", 2, 'say 6:141 19-21', "harekesiz 'semerihî izâ esmera' (19-21. kelime)", None),
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

VF_YAZI = {139: {1: "'ve qâlû'", 9: "'ve muharramun'", 12: "'ve in'"}, 140: {9: "'ve harramû'", 18: "'ve mâ'"}, 141: {1: "'ve huve'", 6: "'ve ğayra'", 8: "'ve'n-naxle'", 9: "'ve'z-zer'a'", 12: "'ve'z-zeytûne'", 13: "'ve'r-rummâne'", 15: "'ve ğayra'", 22: "'ve âtû'", 26: "'ve lâ'"}}
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
ONC = run('/home/claude/sunum/onceki_basim.py', '139', '141', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b33/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b33/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '139', '141', '33').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_139_141.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:139', '6:140', '6:141'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_139_141.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(139, 142))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:139 kök بطن ('butûni' 4. kelime — karın); 6:140 kök قتل ('qatelû' 4. kelime — öldürme), kök ولد ('evlâdehum' 5. kelime — çocuk); 6:141 kök حصد ('hasâdih' 25. kelime — hasat), 'izâ' (20. kelime — zaman zarfı, morph T, kök yok): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '139', '141', '33')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b33/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 34)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(139, 142))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bölüm 15 kapanışında sunum/bolum31_kurallar.py eklendi (kural 1-5), sunum/bolum19_kurallar.py KURAL_ATIF bölüm 15, sunum/geriye_donuk.py bolum31 satırı, sunum/mutasyon_sina.py b31 sınamaları; bu blokta araç değişikliği yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 305",
 "geriye dönük koşu (bölüm 15 kapanışı, komut 'python3 sunum/geriye_donuk.py b31k yamalar/geriye_donuk_6_b28k.txt'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 139 141 33'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:139 'innehû hakîmun 'alîm' (20-22. kelime) — esma_el 'ilahi', kural ''inne/enne' haberi' (Allah) ve ''alîm' (22. kelime) için kural ''inne/enne' haberi' (Allah; morph ADJ ile 'hakîm'in sıfatı) (yamalar/esma_el_6_139_141.txt); "
 "حَكِيم ve عَلِيم lemmalarında önceki 'ilahi' kayıtlarıyla karar eş; 'innehû' zamirinin göndergesi lafız (A1'de); 6:140 ve 6:141 esmâ yok; 6:140 lafız (12. ve 15. kelime); 6:139 ve 6:141 lafız yok; blokta Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 139 141 33'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 6:139 esma_kayit 'mühür EVET (ÇİFT)' — ölçüm MÜHÜR ile uyuşuyor): " + EMH,
 "ölçüm: 6:139 '{{1|esmâ حَكِيم 21\\. sırada, SON konum, MÜHÜR \\| عَلِيم 22\\. sırada, SON konum, MÜHÜR}}', '{{1|fâsıla عليم → م, N sınıfı}}', '{{1|sayı işareti زَوْج}}', '{{1|simetri \\[3, 2, 15, 1\\]}}', '{{1|harf 101 → harf3 93, isaret 8}}' ve '{{1|dış düğüm 0}}'; "
 "6:140 '{{2|fâsıla مهتدين → ن, N sınıfı}}', '{{2|simetri \\[3, 1, 14, 1\\]}}', '{{2|harf 89 → harf3 82, isaret 7}}' ve '{{2|dış düğüm 1}}'; "
 "6:141 '{{3|fâsıla ٱلمسرفين → ن, N sınıfı}}', '{{3|simetri \\[3, 1, 28, 1\\]}}', '{{3|harf 158 → harf3 141, isaret 17}}' ve '{{3|dış düğüm 1}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 139 141 33'): KALAN_P",
 "ölçüm aktör: 6:139, 6:140 ve 6:141 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:139 şart — COND 1 'in' (12.), FUT 1 'se-yeczîhim' (18.); ölçüm biçim DIKKAT (D2'de yazılmadı); "
 "6:140 haber — CERT 2 'qad' (1.), 'qad' (16.), NEG 1 'mâ' (18.); 6:141 emir, yasak — IMPV 2 'kulû' (17.), 've âtû' (22.), PRO 1 'lâ' (26.), NEG 1 'lâ' (29.); ölçüm biçim NEHY (D2'de yazılmadı); "
 "morph RSLT ('fe-hum' 6:139 15.), REM ('ve mâ' 6:140 18.), ACC ('innehû' 6:139 20., 'innehû' 6:141 28.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:141 ★ (kaynak n, z=1,97); 6:139 ve 6:140 yıldız yok",
 "fâsıla: 6:138 ن → 6:139 م (عليم) → 6:140 ن (مهتدين) → 6:141 ن (ٱلمسرفين) — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:139 xref yok; 6:140 okunmuş 1 ayet; 6:141 okunmamış 1 ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:139 'in kâne meyte' süzgeç GEÇMEZ; 6:140 'qad xasira ellezî' süzgeç GEÇMEZ; 6:141 '_ ellezî enşe'e' süzgeç GEÇMEZ, 'semer izâ esmera' süzgeç GEÇMEZ",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; gönderge rol adıyla yazılmaz — sûre 6 bölüm 4 denetimi kuralı 4; tekil zamirin birden çok ada gidişi 'tartışmalı' (sûre 6 bölüm 15 denetiminden GONDERGE_KAPSAM elle)): "
 "6:139 3MP ('ve qâlû' — tartışmalı; 'fe-hum' — tartışmalı; 'se-yeczîhim', 'vasfehum' ekleri — gönderge 've qâlû' 1. kelime), konuşan 1P ('li-zukûrinâ', 'ezvâcinâ' — söz içi), 3MS ('yekun', 'fîhi' — gönderge 'mâ' 2. kelime; 'se-yeczîhim' — gizli zamir, gönderge 6:138 19. kelime; 'innehû' — gönderge 6:138 19. kelime); "
 "6:140 3MS ('xasira' — fiil uyumu, fail 3. kelime; 'razaqahumu' — fiil uyumu, fail 12. kelime), 3MP ('qatelû', 'evlâdehum', 've harramû', 'razaqahumu' eki, 'dallû', 'kânû' — gönderge 'llezîne' 3. kelime); "
 "6:141 3MS ('ve huve', 'enşe'e', 'innehû', 'yuhibbu' — gönderge 6:140 12. kelime; 'ukuluhû', 'semerihî', 'esmera', 'haqqahû', 'hasâdih' — tartışmalı, gönderge 've'n-naxle' 8. kelime), muhatap 2MP ('kulû', 've âtû', 'tusrifû')",
 "6:139-141 gönderge zinciri: 6:139 've qâlû' 3MP öznesi 6:138 1. kelimedeki 3MP özneyle eş topluluğa bağlanabilir; 6:141 've huve' 6:140 lafzına gider (okuma; tartışmalı)",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:139 've qâlû' (1.) ardından söz 2-11. kelime — 'ezvâcinâ' (11.) 1P ile kapanır; 12. kelimeden sonra anlatı ('fe-hum' 3MP); 6:140 ve 6:141 söz yok — söz fiili yok (okuma); mealde 'dediler' sona alındı, tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 139 141 33' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 6:139 've qâlû' (1.), 've muharramun' (9.), 've in' (12.) CONJ; 6:140 've harramû' (9.) CONJ, 've mâ' (18.) REM; 6:141 've huve' (1.), 've ğayra' (6.), 've'n-naxle' (8.), 've'z-zer'a' (9.), 've'z-zeytûne' (12.), 've'r-rummâne' (13.), 've ğayra' (15.), 've âtû' (22.), 've lâ' (26.) CONJ; "
 "'fe' konumları: 6:139 'fe-hum' (15.) RSLT",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:139 ◈B نعم ('l-en'âmi' 6. kelime — B1); 6:139 ◈B زوج ('ezvâcinâ' 11. kelime — B2; eş anlamında, üreme anlamı yok (okuma)); 6:139 ◈B موت ('meyteten' 14. kelime — B4); 6:141 ◈K يوم ('yevme' 24. kelime — K2); 6:140 ◈K / ◈B tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 139 141 33'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — blokta bağ yok; ayetler arası kalıp yok (kontrol.py ile); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:139 söz açılır (2. kelime), söz kapanır (11. kelime, ayet içi), şart → cevap (ayet içi; COND 'in' 12. kelime), şahıs geçişi yok, edim geçişi haber → şart; 6:140 şahıs geçişi yok, edim geçişi şart → haber; "
 "6:141 şahıs geçişi yok, edim geçişi haber → emir, yasak, hitap açılır (ayet içi; 17. kelime muhatap 2MP — sûre 6 bölüm 15 denetiminden MUHATAP_DEGISIMI elle); "
 "ölçüm iltifât 6:139-141 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:139 'in yekun meyteten fe-hum fîhi şurakâ'' — şart ve cevap bağlacı (morph COND + RSLT); 6:140 'qad xasira'llezîne' — pekiştirme ve ilgi zamirli özne (morph CERT + REL); "
 "6:140 'mâ kânû muhtedîn' — olumsuz yardımcı fiil haberi (morph NEG); 6:141 'lâ tusrifû' — yasak (morph PRO); 6:141 'izâ esmera' — zaman zarfı (morph T)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:140 1-3. kelime — 6:31 ve 10:45 ile harekesiz eş (sayım: 'say 6:140 1-3'); 6:141 19-21. kelime — 6:99 ile harekesiz eş (sayım: 'say 6:141 19-21'); "
 "6:140 kök أله ikilemesi; 6:141 kök أكل, ثمر, سرف, شبه, عرش, غير ikilemeleri; 6:141 'muteşâbihen ve ğayra muteşâbih' (14-16. kelime) ve 'izâ esmera' (20-21. kelime) 6:99 ile sûre içi ortak",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 33'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp): emsal yok; "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:139 'qâlû' PERF — meal 'dediler'; 'yekun' IMPF JUS (şart) — meal 'olursa'; 'yeczî' IMPF IND ('se' ile) — meal 'cezalandıracaktır'; "
 "6:140 'xasira' PERF ('qad' ile) — meal 'uğramıştır'; 'qatelû' PERF — meal 'öldürenler'; 'harramû' PERF — meal 'kılanlar'; 'razaqa' PERF — meal 'verdiğini'; 'dallû' PERF ('qad' ile) — meal 'saptılar'; 'kânû' PERF ('mâ' ile) — meal 'olmadılar'; "
 "6:141 'enşe'e' PERF — meal 'inşâ edendir'; 'kulû' IMPV — meal 'yiyin'; 'esmera' PERF ('izâ' ile) — meal 'verdiğinde'; 've âtû' IMPV — meal 'verin'; 'tusrifû' IMPF JUS ('lâ' ile) — meal 'etmeyin'; 'yuhibbu' IMPF IND ('lâ' ile) — meal 'sevmez'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle): 'qad' + PERF 6:140'ta '-mıştır' ve '-dılar' ile — 'Kesinlikle' zarfı 16. kelimede 'qad' karşılığı",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 139 141 33'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:139, 6:140 ve 6:141 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:139 ('li-zukûrinâ' / 'ezvâcinâ'); 6:141 ('ma'rûşâtin' / 've ğayra ma'rûşâtin'); 6:140 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök نعم 6:139 ('l-en'âmi') — 6:136 ve 6:138 ile bölüm içi; kök حرم 6:139 ('ve muharramun') ve 6:140 ('ve harramû'); kök جزي 6:139 ('se-yeczîhim') — 6:138 ile bölüm içi; kök شرك 6:139 ('şurakâ''); kök علم 6:139 (''alîm') ve 6:140 (''ilmin'); kök غير 6:140 ('bi-ğayri') ve 6:141 ('ve ğayra', 've ğayra'); kök كون 6:139 ('yekun') ve 6:140 ('kânû'); kök أله 6:140 ('llâhu', 'llâh'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 16-2 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm blokları 32, 33 ve 34; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b33/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 139 141 33'; lem_bozuk.py 33 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 139 141 → AYN_SONUC; sunum/bolum4_kurallar.py 139 141 33 → KHATA_HEPSI; sunum/bolum5_kurallar.py 139 141 33 → B5_HEPSI; sunum/bolum6_kurallar.py 139 141 33 → B6_HEPSI; sunum/bolum7_kurallar.py 139 141 33 → B7_HEPSI; sunum/bolum8_kurallar.py 139 141 33 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 139 141 33 → B9_HEPSI; sunum/bolum10_kurallar.py 139 141 33 → B10_HEPSI; sunum/bolum11_kurallar.py 139 141 33 → B11_HEPSI; sunum/bolum12_kurallar.py 139 141 33 → B12_HEPSI; sunum/bolum13_kurallar.py 139 141 33 → B13_HEPSI; sunum/bolum14_kurallar.py 139 141 33 → B14_HEPSI; sunum/bolum15_kurallar.py 139 141 33 → B15_HEPSI; sunum/bolum16_kurallar.py 139 141 33 → B16_HEPSI; sunum/bolum17_kurallar.py 139 141 33 → B17_HEPSI; sunum/bolum18_kurallar.py 139 141 33 → B18_HEPSI; sunum/bolum19_kurallar.py 139 141 33 → B19_HEPSI; sunum/bolum20_kurallar.py 139 141 33 → B20_HEPSI; sunum/bolum21_kurallar.py 139 141 33 → B21_HEPSI; sunum/bolum22_kurallar.py 139 141 33 → B22_HEPSI; sunum/bolum23_kurallar.py 139 141 33 → B23_HEPSI; sunum/bolum24_kurallar.py 139 141 33 → B24_HEPSI; sunum/bolum25_kurallar.py 139 141 33 → B25_HEPSI; sunum/bolum26_kurallar.py 139 141 33 → B26_HEPSI; sunum/bolum27_kurallar.py 139 141 33 → B27_HEPSI; sunum/bolum28_kurallar.py 139 141 33 → B28_HEPSI; sunum/bolum29_kurallar.py 139 141 33 → B29_HEPSI; sunum/bolum30_kurallar.py 139 141 33 → B30_HEPSI; sunum/bolum31_kurallar.py 139 141 33 → B31_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 33 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal yok — ölçüm xref adayları (6:140 okunmuş 1 ayet; 6:141 okunmamış 1 ayet) harekesiz sayım anahtarıyla bulunmadı ya da okunmamış; emsal dosyası üretilmedi; önceki basım (sunum/onceki_basim.py): " + ONC + "; say2.txt sayımı basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('in', 'kâne', 'meyte', 'qad', 'xasira', 'ellezî', 'enşe'e', 'semer', 'izâ', 'esmera'); joker '_' yalnız lemmasız 'huve' öğesinde ('_ ellezî enşe'e' — 6:98 adıyla eş); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (139, 141): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_139_141.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b31k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '139', '141'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '139', '141', '33'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '139', '141', '33'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '139', '141', '33', '--tazelik-yok')}
    for _n in range(7, 32): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '139', '141', '33')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31 = [_R['B%d' % _n].splitlines() for _n in range(6, 32)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'B31_HEPSI': (B31[-1] if B31 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31): print([l for l in _x if l.startswith('HATA') or 'hata' in l])

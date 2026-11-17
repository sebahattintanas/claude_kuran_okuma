# blok 32 (5:106-108) ARIZA oluşturucu — bölüm 14-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b32/olcum.txt'
os.environ['SAY2'] = '/home/claude/b32/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
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
 ("5:106", "'eyy ellezî âmene'", 16, 'say 5:106 1-3', "harekesiz 'yâ eyyuhe'llezîne âmenû' (1-3. kelime)", None),
 ("5:106", "'zû 'adl min'", 2, 'say 5:106 13-15', "harekesiz 'zevâ 'adlin minkum' (13-15. kelime)", None),
 ("5:106", "'inne izen min'", 2, 'say 5:106 48-50', "harekesiz 'innâ izen le-mine' (48-50. kelime)", None),
 ("5:107", "'inne izen min'", 2, 'say 5:107 23-25', "harekesiz 'innâ izen le-mine' (23-25. kelime)", None),
 ("5:108", "'allâh lâ hedâ qavm'", 3, 'say 5:108 18-21 --on', "önek kesilmiş 've'llâhu lâ yehdi'l-qavm' (18-21. kelime)", ('dizi 5 108 18 21', "allâh lâ hedâ qavm", '18-21', "biçim farkı (dizi 5 108 18 21): basılmamış eş i'râb, önek; basılmamış eş i'râb, önek")),
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

VF_YAZI = {106: {25: "'fe-esâbetkum'", 32: "'fe-yuqsimâni'", 40: "'ve lev'", 44: "'ve lâ'"}, 107: {1: "'fe-in'", 7: "'fe-âxarâni'", 15: "'fe-yuqsimâni'", 21: "'ve mâ'"}, 108: {15: "'ve'ttequ'", 17: "'ve'sme'û'", 18: "'ve'llâhu'"}}
sys.path.insert(0, '/home/claude/b32/yap')
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
open('/home/claude/b32/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '32')
BLOKLAR = [str(i) for i in range(1, 33)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '32', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b32/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '106', '108', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b32/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b32/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '106', '108', '32').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_106_108.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'5:106', '5:107', '5:108'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_106_108.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '5:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '5:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(106, 109))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "5:106 'izâ' (6. kelime — morph T, zaman); 5:106 kök أخر ('âxarâni' 17. kelime — başka): tetik listesinde yok; 5:106 kök بعد ('ba'di' 30. kelime — sonra): zaman, tetik listesinde yok; 5:107 kök أخر ('fe-âxarâni' 7. kelime — başka): tetik listesinde yok; 5:107 kök ولي ('l-evleyâni' 14. kelime — en layık): tetik listesinde yok; 5:108 kök دنو ('ednâ' 2. kelime — daha yakın): tetik listesinde yok; 5:108 kök وجه ('vechihâ' 7. kelime — yüz; burada 'gerçek yüzüyle' deyimi, organ anlamında kullanılmıyor): tetik listesinde yok; 5:108 kök يمن ('eymânun' 12., 'eymânihim' 14. kelime — yemin; kök anlamı 'sağ el', organ anlamında kullanılmıyor): tetik listesinde yok; 5:108 'ba'de' (13. kelime — morph T, zaman)"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '106', '108', '32')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b32/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 33)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b5:%d:\d+' % a_, s_) for a_ in range(106, 109))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: yalnız blok akışı (sunum/sinifla.py SON, sunum/basilan.txt — §3 adım 2 ve emsal işaretlemesi); denetim kuralı değişmedi; mutasyon_sina — MUT_SONUC; "
 "geriye dönük koşu son araç değişikliğinden sonra (blok 31) üretildi: GERI_P",
 "kök tablosu: ölçümde '???' 5:106, 5:107 ve 5:108 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 106 108 32'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:106 'ehadekumu' (8. kelime) — esma_el 'degil', kural 'çoğul insan göndergeli' (biriniz; 'kum' zamirli, insan öznesi); 5:107 ve 5:108 esmâ yok; lafız 5:106, 5:107 ve 5:108; Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 106 108 32'; bölüm 13 denetimi kuralı 2: esma_el eklendikten sonra): " + EMH,
 "ölçüm: 5:106 '{{1|fâsıla ٱلءاثمين → ن, N sınıfı}}', '{{1|sayı işareti أَحَد, اثْنَيْن, ثَمَن}}', '{{1|simetri \\[4, 13, 18, 1\\]}}', '{{1|harf 220 → harf3 212, isaret 8}}' ve '{{1|dış düğüm 2}}'; "
 "5:107 '{{2|fâsıla ٱلظلمين → ن, N sınıfı}}', '{{2|EDİLGEN 1/6 fiil, pas z=0,62}}', '{{2|mm2: \\[8, قوم}}', '{{2|simetri \\[4, 1, 21, 1\\]}}', '{{2|harf 127 → harf3 125, isaret 2}}' ve '{{2|dış düğüm 0}}'; "
 "5:108 '{{3|fâsıla ٱلفسقين → ن, N sınıfı}}', '{{3|EDİLGEN 1/6 fiil, pas z=0,62}}', '{{3|simetri \\[3, 1, 6, 1\\]}}', '{{3|harf 102 → harf3 95, isaret 7}}' ve '{{3|dış düğüm 1}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 106 108 32'): KALAN_P",
 "ölçüm aktör: 5:106, 5:107 ve 5:108 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 5:106 nida, şart — VOC 1 'yâ' (1.), COND 3 'in' (20., 34.), 'lev' (40.), NEG 2 'lâ' (36., 44.), EMPH 1 'le' (50.); "
 "ölçüm biçim alanı '{{1|biçim DIKKAT \\+ QASEM}}' (yalnız bu maddede; QASEM gerekçesi kök قسم — 'fe-yuqsimâni' 32. kelime); "
 "5:107 şart — COND 1 'in' (1.), EMPH 2 'le' (17., 25.), NEG 1 'mâ' (21.); ölçüm biçim alanı '{{2|biçim QASEM}}' (yalnız bu maddede; QASEM gerekçesi kök قسم — 'fe-yuqsimâni' 15. kelime); "
 "5:108 emir — IMPV 2 'ttequ' (15.), 'sme'û' (17.), NEG 1 'lâ' (19.); "
 "morph REM ('fe' 5:106 32.; 've' 5:106 40., 5:107 21., 5:108 15. ve 18.), RSLT ('fe' 5:107 7.), ANS ('izen' 5:106 49., 5:107 24.) ve T ('izâ' 5:106 6., 'hîne' 5:106 10., 'ba'de' 5:108 13.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 5:106 ★★★ (kaynak n, z=4,10); 5:107 ve 5:108 yıldız yok",
 "fâsıla: 5:105 ن (تعملون) → 5:106 ن (ٱلءاثمين) → 5:107 ن (ٱلظلمين) → 5:108 ن (ٱلفسقين); 5:106, 5:107 ve 5:108 etken ortaç çoğulu ile kapanıyor (ölçümde kafiye bayrağı yok); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1 — basılmış hedefler numarasıyla, basılmamışlar sinifla sayısıyla): 5:106 2:180 (emsal olarak basıldı) ve okunmuş 1 ayet; 5:107 xref yok; 5:108 okunmuş 1 ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:106 'eyy ellezî âmene' süzgeç GEÇER, 'zû 'adl min' ve 'inne izen min' GEÇMEZ; 5:107 'inne izen min' GEÇMEZ; 5:108 'allâh lâ hedâ qavm' GEÇER",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "fail olmayan mecrur çoğul ad ve mecrur ilgi zamiri A1'de yazılmaz — bölüm 11 denetimi kuralları 16 ve 19; fiilden önce gelen lafız 'mübtedâ' — bölüm 12 denetimi kuralı 11; edilgen fiilde 'naib-i faili' — bölüm 11 denetimi kuralı 17; A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5): "
 "5:106 hitap, 3MP (adsız — 'âmenû'), muhatap 2MP (adsız), 'l-mevtu' ('hadara' faili), 'musîbetu'l-mevti' ('esâbe' faili), 3D (adsız — 'tahbisûnehumâ' mef'ûlü), 3MD (adsız — 'fe-yuqsimâni'), Allah (lafız; yemin edilen), konuşan 1P (adsız; söz içi), 3MS (adsız; söz içi — 'bihî', 'kâne'); "
 "5:107 ''usira' (edilgen; naib-i faili 4-6. kelime), 3D / 3MD (adsız — iki şahit ve yerlerine geçen iki kişi), 'fe-âxarâni' (mübtedâ), 'l-evleyâni' (bedel), 3MP (adsız — ''aleyhimu'), Allah (lafız; yemin edilen), konuşan 1P (adsız; söz içi); "
 "5:108 3MP (adsız — 'ye'tû', 'yaxâfû', 'eymânihim'), 3FS (adsız — 'vechihâ'), 'eymânun' ('turadde' naib-i faili), muhatap 2MP (adsız), Allah (lafız; 16. kelimede 'ttequ' mef'ûlü, 18. kelimede mübtedâ), 3MS (adsız — 'yehdi'); "
 "'l-âsimîn' (5:106 51. kelime) ve 'z-zâlimîn' (5:107 26. kelime) — mecrur çoğul — A1'de yazılmadı — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): 5:106 ve 5:107 yemin sözü ('fe-yuqsimâni bi'llâh' ardından; 5:106 36-51., 5:107 17-26. kelime) mealde tırnaksız, iki nokta ile (emsal biçimi); A3'te ve A4'te 'söz açılır' / 'söz kapanır'; 5:108 söz yok (A3 —); 'qul' yok (bölüm 10 denetimi kuralı 8); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 106 108 32' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "REM sapması 5:106 (40. kelime) — 've lev' vasliyye: yemin sözünün içinde istînâf değil, 'akraba da olsa' tekit bağı (meal 'da olsa'); "
 "REM sapması 5:107 (21. kelime) — 've mâ 'tedeynâ' yeminin sonraki cevabı: söz içinde yeni cümle, meal virgülle bağlıyor (atıf okunuşu); "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:106 'fe-esâbetkum' (25.) CONJ, 'fe-yuqsimâni' (32.) REM, 've lev' (40.) REM, 've lâ' (44.) CONJ; 5:107 'fe-in' (1.) ve 'fe-yuqsimâni' (15.) CONJ, 'fe-âxarâni' (7.) RSLT, 've mâ' (21.) REM; "
 "5:108 've'ttequ' (15.) ve 've'llâhu' (18.) REM, 've'sme'û' (17.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 5:106 ◈K أرض ('l-ardi' 24. kelime — K1; anlam notu: yolculuk edilen yeryüzü); 5:106 ◈K حين ('hîne' 10. kelime — K2; anlam notu: vasiyet anı); "
 "5:106 ◈B موت ('l-mevtu' 9., 'l-mevti' 27. kelime — B4; anlam notu: ölümün gelişi ve ölüm musibeti); 5:108 ◈B سمع ('sme'û' 17. kelime — B3; anlam notu: dinleme emri)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 106 108 32'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:106 (2:180); 5:107 ve 5:108 D3 eşi yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "ayetler arası kalıp 'innâ izen le-mine' (5:106, 5:107) — sayım 'say 5:106 48-50' ve lemma dizisi 'dizi 5 106 48 50' / 'dizi 5 107 23 25'; ayetler arası kalıp 'fe-yuqsimâni bi'llâh' (5:106, 5:107) — sayım 'say 5:106 32-33 --on'; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:106 hitap açılır; söz açılır / kapanır (36-51. kelime); edim geçişi emir, nida → nida, şart; şart → cevap ('in' 20. ve 34., 'lev' 40. kelime — 'lev' cevabı mahzuf); "
 "5:107 söz açılır / kapanır (17-26. kelime); edim geçişi nida, şart → şart; şahıs geçişi 2 → 3; şart → cevap ('in' 1. kelime); 5:108 bölüm kapanışı (bölüm 10 denetimi kuralı 2); edim geçişi şart → emir",
 "sözdizimi (okuma; morph etiketiyle): 5:106 'şehâdetu beynikum' — mübtedâ; 'izâ hadara' — zaman (morph T); 'in entum darabtum' — şart (morph COND); 'fe-yuqsimâni bi'llâh' — istînâf ve yemin (morph REM); 've lev kâne' — vasliyye şart (morph REM + COND); 'innâ izen' — tekit ve cevap (morph ACC + ANS); "
 "5:107 'fe-in 'usira' — atıf ve şart (morph CONJ + COND); 'fe-âxarâni' — şart cevabı (morph RSLT); 'le-şehâdetunâ' — yemin cevabı tekidi (morph EMPH); 've mâ 'tedeynâ' — istînâf ve olumsuz (morph REM + NEG); "
 "5:108 'en ye'tû' — masdar cümlesi (morph SUB); 've'ttequ'llâhe' — istînâf ve emir (morph REM + IMPV); 've'sme'û' — atıf (morph CONJ); 've'llâhu lâ yehdi' — istînâf (morph REM)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:106 'yâ eyyuhe'llezîne âmenû' ile açılıyor; "
 "5:106 kök شهد ikilemesi ('şehâdetu' 4. / 'şehâdete' 46. kelime) ve kök موت ikilemesi ('l-mevtu' 9. / 'l-mevti' 27. kelime); 5:107 kök حقق üçlemesi ('stehaqqâ' 5., 'stehaqqa' 12., 'ehaqqu' 18. kelime); "
 "5:106 ve 5:107 'fe-yuqsimâni bi'llâh' ve 'innâ izen le-mine' kalıplarını paylaşıyor; 5:108 kök يمن ikilemesi ('eymânun' 12. / 'eymânihim' 14. kelime)",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 32'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit): 'hadara ehadekumu'l-mevt' 5:106 'ölüm geldiğinde' / 2:180 'ölüm geldiğinde' (emsal metninde) — çakışma değil; "
 "'l-vasiyye' 5:106 'vasiyet' / 2:180 'vasiyet' (emsal metninde) — çakışma değil",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): 'in' — çakışma değil (5:106 '-se' ve 5:107 'Eğer', önceki blokta '-sa' — ünlü uyumu ve cümle başı); ''alâ' — çakışma değil (5:107 'aleyh' ve 5:108 '-yla', önceki blokta 'karşı' ve 'üzerinde' — fiil yönetimi)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 106 108 32'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:106 tarayıcı adayı (kök أرض, موت; A_şart, D_yeti, F_ölçü) — çıpa değil: yolculuk ve ölüm anması hüküm bağlamı, doğa iddiası yok (olgu=False); 5:107 ve 5:108 tarayıcı vermedi (cipa_tarama5_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: ayet içi 5:106 ('minkum' / 'min ğayrikum'), 5:107 ('le-şehâdetunâ' / 'şehâdetihimâ'), 5:108 ('eymânun' / 'eymânihim') — okuma; ayetler arası 'l-âsimîn' (5:106) / 'z-zâlimîn' (5:107) kapanış eşliği — okuma; eşleme betikle: ADAY_P",
 "aday 1041: kök شهد 5:106 ('şehâdetu' 4., 'şehâdete' 46.), 5:107 ('le-şehâdetunâ' 17., 'şehâdetihimâ' 20.) ve 5:108 ('bi'ş-şehâdeti' 5.) — 5:106, 5:107 ve 5:108 şahitlik bağı; kök قسم 5:106 ve 5:107 'fe-yuqsimâni'; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 14-2 (bölüm 7 kuralı 9 — blok_plani_5.txt'ten) — bölüm iki blok (31, 32); bu blok bölümü kapatıyor; başlıktaki 'vasiyet ve şahitlik' 5:106-108; bölüm sonu bağımsız denetimi bu bloktan sonra; "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b32/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 106 108 32'; lem_bozuk.py 32 çıktısı): 5:106:28 'yahbisu', 5:106:32 'aqsamu', 5:107:2 ''usira' — lem_bozuk bayrağı; meal maddesinde '(morph LEM ham biçim)' notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 106 108 → AYN_SONUC; sunum/bolum4_kurallar.py 106 108 32 → KHATA_HEPSI; sunum/bolum5_kurallar.py 106 108 32 → B5_HEPSI; sunum/bolum6_kurallar.py 106 108 32 → B6_HEPSI; sunum/bolum7_kurallar.py 106 108 32 → B7_HEPSI; sunum/bolum8_kurallar.py 106 108 32 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 106 108 32 → B9_HEPSI; sunum/bolum10_kurallar.py 106 108 32 → B10_HEPSI; sunum/bolum11_kurallar.py 106 108 32 → B11_HEPSI; sunum/bolum12_kurallar.py 106 108 32 → B12_HEPSI; sunum/bolum13_kurallar.py 106 108 32 → B13_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 32 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('eyy', 'ellezî', 'âmene', 'zû', ''adl', 'min', 'inne', 'izen', 'allâh', 'lâ', 'hedâ', 'qavm'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; 've mâ 'tedeynâ' (5:107 21-22. kelime) ayrı yazıldı; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (106, 108): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_106_108.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_5_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('06', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()
GERI = open('/home/claude/yamalar/geriye_donuk_5_b31.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    AYN = (run('/home/claude/sunum/ayn_kontrol.py', '106', '108').splitlines() or ['?'])[-1]
    KUR = run('/home/claude/sunum/bolum4_kurallar.py', '106', '108', '32').splitlines()
    KH = [l for l in KUR if l.startswith('HATA')]
    B5 = run('/home/claude/sunum/bolum5_kurallar.py', '106', '108', '32').splitlines()
    B5H = [l for l in B5 if l.startswith('HATA')]
    B6 = run('/home/claude/sunum/bolum6_kurallar.py', '106', '108', '32', '--tazelik-yok').splitlines()
    B7 = run('/home/claude/sunum/bolum7_kurallar.py', '106', '108', '32').splitlines()
    B8 = run('/home/claude/sunum/bolum8_kurallar.py', '106', '108', '32').splitlines()
    B9 = run('/home/claude/sunum/bolum9_kurallar.py', '106', '108', '32').splitlines()
    B10 = run('/home/claude/sunum/bolum10_kurallar.py', '106', '108', '32').splitlines()
    B11 = run('/home/claude/sunum/bolum11_kurallar.py', '106', '108', '32').splitlines()
    B12 = run('/home/claude/sunum/bolum12_kurallar.py', '106', '108', '32').splitlines()
    B13 = run('/home/claude/sunum/bolum13_kurallar.py', '106', '108', '32').splitlines()
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
